#!/usr/bin/env python3
"""Install Blender addons from the plugin directory.

Cross-platform: works on Windows, macOS, and Linux. Supports both
user-level and system-wide installs. Handles .zip files and directories.

Usage:
    # List available addons:
    uv run python tools/install_addon_blender.py --list

    # Install a specific addon (by name or partial match):
    uv run python tools/install_addon_blender.py --addon SimplyCloth3
    uv run python tools/install_addon_blender.py --addon "Auto-Rig"

    # Install all addons:
    uv run python tools/install_addon_blender.py --all

    # Install the MCP addon (default behavior):
    uv run python tools/install_addon_blender.py

    # System-wide install (Linux only):
    uv run python tools/install_addon_blender.py --addon SimplyCloth3 --system

    # Skip auto-enable:
    uv run python tools/install_addon_blender.py --addon SimplyCloth3 --no-enable
"""

from __future__ import annotations

import contextlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

IS_WINDOWS = sys.platform.startswith("win")
IS_MACOS = sys.platform == "darwin"
IS_LINUX = sys.platform.startswith("linux")

DEFAULT_ADDON_NAME = "blender_mcp_addon"


def candidate_blender_paths() -> list[str]:
    """Return platform-specific Blender executable candidates."""
    env_path = os.environ.get("BLENDER_EXECUTABLE")
    if IS_WINDOWS:
        return [
            env_path,
            r"C:\Program Files\Blender Foundation\Blender\blender.exe",
            r"C:\Program Files (x86)\Blender Foundation\Blender\blender.exe",
            "blender.exe",
            "blender",
        ]
    if IS_MACOS:
        return [
            env_path,
            "/Applications/Blender.app/Contents/MacOS/Blender",
            "/usr/local/bin/blender",
            "blender",
        ]
    return [
        env_path,
        os.path.expanduser("~/App/blender-5.2.0-linux-x64/blender"),
        "/usr/bin/blender",
        "/usr/local/bin/blender",
        "/snap/bin/blender",
        "blender",
    ]


def find_blender_path() -> str | None:
    """Find the Blender executable on the system."""
    for path in candidate_blender_paths():
        if not path:
            continue
        try:
            result = subprocess.run(
                [path, "--version"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if result.returncode == 0:
                return path
        except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
            continue
    return None


def run_blender_subprocess(blender_path: str, args: list[str], timeout: int = 10) -> subprocess.CompletedProcess[str]:
    """Run a Blender subprocess with cross-platform display hints."""
    env = os.environ.copy()
    if IS_LINUX:
        env.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")
    return subprocess.run(
        [blender_path, *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
        check=False,
    )


def find_blender_version(blender_path: str) -> str:
    """Return the short Blender version (``major.minor``)."""
    result = run_blender_subprocess(blender_path, ["--version"], timeout=10)
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            if line.strip().startswith("Blender"):
                parts = line.split()
                if len(parts) >= 2:
                    version_parts = parts[1].split(".")
                    if len(version_parts) >= 2:
                        return f"{version_parts[0]}.{version_parts[1]}"
    return "5.1"


def clean_addon_name(name: str) -> str:
    """Clean addon name for use as Blender module name."""
    name = re.sub(r"[_\s]+", "_", name)
    name = re.sub(r"[^a-zA-Z0-9_.]", "", name)
    name = name.strip("_").lower()
    return name or "addon"


def find_addon_module(path: Path) -> str | None:
    """Find the addon module name from a directory (has __init__.py)."""
    if (path / "__init__.py").exists():
        return path.name
    for child in path.iterdir():
        if child.is_dir() and (child / "__init__.py").exists():
            return child.name
    return None


def extract_addon_from_zip(zip_path: Path, temp_dir: Path) -> tuple[Path, str] | None:
    """Extract a zip and return (extracted_dir, module_name)."""
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(temp_dir)
    except zipfile.BadZipFile:
        print(f"  ERROR: {zip_path.name} is not a valid zip file")
        return None

    # Find addon module (directory with __init__.py)
    for init_file in temp_dir.rglob("__init__.py"):
        module_dir = init_file.parent
        if module_dir == temp_dir:
            continue
        if module_dir.parent == temp_dir:
            return module_dir, module_dir.name

    # Single-file addon: find .py files and wrap in directory
    py_files = list(temp_dir.rglob("*.py"))
    if py_files:
        py_file = py_files[0]
        if py_file.parent == temp_dir:
            # Single .py file at root - create wrapper directory
            module_name = clean_addon_name(py_file.stem)
            module_dir = temp_dir / module_name
            module_dir.mkdir(exist_ok=True)
            shutil.move(str(py_file), str(module_dir / "__init__.py"))
            return module_dir, module_name

    return None


def list_available_addons(plugin_dir: Path) -> list[tuple[str, str, str]]:
    """List available addons. Returns [(display_name, source_path, type)]."""
    addons = []
    if not plugin_dir.exists():
        return addons

    for item in sorted(plugin_dir.iterdir()):
        if item.name.startswith("."):
            continue
        if item.is_dir():
            # Standard addon (has __init__.py)
            if (item / "__init__.py").exists():
                addons.append((item.name, str(item), "directory"))
            # Complex addon directory (multiple sub-addons)
            elif any(child.is_dir() for child in item.iterdir()):
                addons.append((item.name, str(item), "directory"))
        elif item.suffix == ".zip":
            display_name = item.stem
            display_name = re.sub(r"_DownloadPirate\.com$", "", display_name)
            display_name = re.sub(r"\s*V?\d+(\.\d+)*$", "", display_name)
            addons.append((display_name, str(item), "zip"))
    return addons


def enable_addon_by_name(blender_path: str, module_name: str) -> bool:
    """Enable a specific addon by module name."""
    enable_code = f"""
import bpy

try:
    bpy.ops.preferences.addon_enable(module="{module_name}")
    print("Addon '{module_name}' enabled successfully")
except Exception as e:
    print(f"Failed to enable addon: {e}")

try:
    bpy.ops.wm.save_userpref()
    print("User preferences saved")
except Exception as e:
    print(f"Failed to save preferences: {e}")
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(enable_code)
        temp_script = f.name
    try:
        result = run_blender_subprocess(
            blender_path,
            ["--background", "--python", temp_script],
            timeout=15,
        )
        print("  Enable output:", result.stdout.strip())
        if result.stderr:
            print("  Enable errors:", result.stderr[:300])
        return result.returncode == 0
    finally:
        with contextlib.suppress(OSError):
            os.unlink(temp_script)


def install_addon(
    blender_path: str,
    addon_source: Path,
    module_name: str,
    *,
    user_install: bool = True,
    auto_enable: bool = True,
) -> bool:
    """Install a single addon to Blender."""
    version = find_blender_version(blender_path)

    if user_install:
        home = Path.home()
        addons_path = home / ".config" / "blender" / version / "extensions" / "user_default"
    else:
        if not IS_LINUX:
            print("  ERROR: System-wide install is only supported on Linux.")
            return False
        addons_path = Path(f"/usr/share/blender/{version}/scripts/addons")

    try:
        addons_path.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"  ERROR: Cannot create directory {addons_path}. Permission denied.")
        return False

    addon_dest = addons_path / module_name
    try:
        if addon_dest.exists():
            shutil.rmtree(addon_dest)

        shutil.copytree(addon_source, addon_dest)

        for root, dirs, files in os.walk(addon_dest):
            for d in dirs:
                os.chmod(Path(root) / d, 0o755)
            for f in files:
                os.chmod(Path(root) / f, 0o644)

        print(f"  Installed to: {addon_dest}")

        if auto_enable:
            version_major = int(version.split(".")[0])
            if version_major >= 5:
                print(f"  Blender 5.x: extension auto-discovered, enable in Edit > Preferences > Extensions")
            elif enable_addon_by_name(blender_path, module_name):
                print(f"  Addon enabled and saved to preferences")
            else:
                print(f"  Manual enable: Edit > Preferences > Add-ons > search '{module_name}'")
        return True
    except (OSError, shutil.Error) as e:
        print(f"  ERROR during installation: {e}")
        return False


def resolve_addon(
    plugin_dir: Path, addon_query: str
) -> tuple[Path, str] | None:
    """Resolve an addon query to (source_path, module_name)."""
    addons = list_available_addons(plugin_dir)

    # Exact match first
    for display_name, source_path, addon_type in addons:
        if addon_query.lower() == display_name.lower():
            source = Path(source_path)
            if addon_type == "zip":
                temp_dir = Path(tempfile.mkdtemp(prefix="blender_addon_"))
                result = extract_addon_from_zip(source, temp_dir)
                if result:
                    return result
                return None
            return source, source.name

    # Partial match
    for display_name, source_path, addon_type in addons:
        if addon_query.lower() in display_name.lower():
            source = Path(source_path)
            if addon_type == "zip":
                temp_dir = Path(tempfile.mkdtemp(prefix="blender_addon_"))
                result = extract_addon_from_zip(source, temp_dir)
                if result:
                    return result
                return None
            return source, source.name

    return None


def get_all_addons(plugin_dir: Path) -> list[tuple[Path, str]]:
    """Get all installable addons as (source_path, module_name) pairs."""
    addons = list_available_addons(plugin_dir)
    results = []
    for display_name, source_path, addon_type in addons:
        source = Path(source_path)
        if addon_type == "zip":
            temp_dir = Path(tempfile.mkdtemp(prefix="blender_addon_"))
            result = extract_addon_from_zip(source, temp_dir)
            if result:
                results.append(result)
        else:
            results.append((source, source.name))
    return results


def parse_args(argv: list[str]) -> dict:
    """Parse CLI arguments."""
    args = {
        "list": "--list" in argv or "-l" in argv,
        "all": "--all" in argv,
        "addon": None,
        "user_install": "--system" not in argv and "--system-wide" not in argv,
        "auto_enable": "--no-enable" not in argv and "--disable-auto-enable" not in argv,
    }
    for i, arg in enumerate(argv):
        if arg == "--addon" and i + 1 < len(argv):
            args["addon"] = argv[i + 1]
    return args


def main() -> int:
    script_dir = Path(__file__).parent
    plugin_dir = script_dir.parent / "plugin"

    print("=" * 60)
    print("Blender Addon Installer")
    print("=" * 60)
    print()

    args = parse_args(sys.argv[1:])

    if args["list"]:
        print(f"Available addons in {plugin_dir}:\n")
        addons = list_available_addons(plugin_dir)
        if not addons:
            print("  No addons found.")
            return 1
        for i, (name, path, addon_type) in enumerate(addons, 1):
            print(f"  {i}. {name} ({addon_type})")
        print(f"\nUsage: {sys.argv[0]} --addon <name>")
        return 0

    print("Searching for Blender...")
    blender_path = find_blender_path()
    if not blender_path:
        print("ERROR: Blender not found. Set BLENDER_EXECUTABLE env var.")
        return 1
    print(f"Found: {blender_path}\n")

    version = find_blender_version(blender_path)
    print(f"Blender version: {version}")
    print(f"Mode: {'User' if args['user_install'] else 'System-wide'}")
    print(f"Auto-enable: {'ON' if args['auto_enable'] else 'OFF'}\n")

    to_install: list[tuple[Path, str]] = []

    if args["addon"]:
        result = resolve_addon(plugin_dir, args["addon"])
        if not result:
            print(f"Addon '{args['addon']}' not found in {plugin_dir}")
            print("Use --list to see available addons.")
            return 1
        to_install.append(result)
    elif args["all"]:
        to_install = get_all_addons(plugin_dir)
        if not to_install:
            print("No addons found in plugin directory.")
            return 1
    else:
        # Default: install the MCP addon
        mcp_addon = Path(__file__).parent.parent.parent / DEFAULT_ADDON_NAME
        if not mcp_addon.exists():
            print(f"MCP addon not found at {mcp_addon}")
            print("Use --addon <name> or --all to install other addons.")
            return 1
        to_install.append((mcp_addon, DEFAULT_ADDON_NAME))

    print(f"Installing {len(to_install)} addon(s)...\n")
    success_count = 0
    for source, module_name in to_install:
        print(f"Installing: {module_name}")
        if install_addon(
            blender_path,
            source,
            module_name,
            user_install=args["user_install"],
            auto_enable=args["auto_enable"],
        ):
            success_count += 1
        print()

    print(f"Done: {success_count}/{len(to_install)} addons installed.")
    return 0 if success_count == len(to_install) else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""PSD to PNG Converter - supports composite, per-group, and per-layer export."""

import argparse
import os
import re
import sys
import time
from pathlib import Path

from psd_tools import PSDImage


def sanitize(name: str) -> str:
    return re.sub(r'[^\w\-]', '_', name).strip('_')


def print_tree(psd, indent=0):
    for layer in psd:
        prefix = "  " * indent
        kind = "📁" if layer.is_group() else "📄"
        hidden = "" if layer.visible else " [HIDDEN]"
        print(f"{prefix}{kind} {layer.name}{hidden}")
        if layer.is_group():
            print_tree(layer, indent + 1)


def export_composite(psd_path: str, output_path: str | None = None) -> str:
    base = Path(psd_path).stem
    if output_path is None:
        output_path = f"{base}.png"

    print(f"[composite] {psd_path} -> {output_path}")
    t0 = time.time()
    psd = PSDImage.open(psd_path)
    psd.composite().save(output_path)
    elapsed = time.time() - t0
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"  done in {elapsed:.1f}s ({size_mb:.1f} MB)")
    return output_path


def export_groups(psd_path: str, output_dir: str) -> list[str]:
    base = Path(psd_path).stem
    os.makedirs(output_dir, exist_ok=True)

    psd = PSDImage.open(psd_path)
    print(f"[groups] {psd_path} -> {output_dir}/")

    t0 = time.time()
    outputs = []

    for i, layer in enumerate(psd):
        if not layer.is_group():
            continue
        name = sanitize(layer.name)
        out = os.path.join(output_dir, f"{base}_group_{i:02d}_{name}.png")
        print(f"  📁 {layer.name} -> {out}")
        layer.composite().save(out)
        outputs.append(out)

    elapsed = time.time() - t0
    size_total = sum(os.path.getsize(f) for f in outputs) / (1024 * 1024)
    print(f"  done in {elapsed:.1f}s, {len(outputs)} groups ({size_total:.1f} MB total)")
    return outputs


def export_layers_recursive(psd, output_dir: str, base: str, prefix: str = "") -> list[str]:
    outputs = []
    for i, layer in enumerate(psd):
        if layer.is_group():
            sub = os.path.join(output_dir, sanitize(layer.name))
            os.makedirs(sub, exist_ok=True)
            outputs.extend(export_layers_recursive(layer, sub, base, f"{prefix}{i}_"))
        else:
            name = sanitize(layer.name)
            out = os.path.join(output_dir, f"{base}_layer_{prefix}{i}_{name}.png")
            layer.composite().save(out)
            outputs.append(out)
            print(f"    📄 {layer.name} -> {out}")
    return outputs


def export_layers(psd_path: str, output_dir: str) -> list[str]:
    base = Path(psd_path).stem
    os.makedirs(output_dir, exist_ok=True)

    psd = PSDImage.open(psd_path)
    print(f"[layers] {psd_path} -> {output_dir}/")

    t0 = time.time()
    outputs = export_layers_recursive(psd, output_dir, base)

    elapsed = time.time() - t0
    size_total = sum(os.path.getsize(f) for f in outputs) / (1024 * 1024)
    print(f"  done in {elapsed:.1f}s, {len(outputs)} layers ({size_total:.1f} MB total)")
    return outputs


def main():
    parser = argparse.ArgumentParser(
        description="PSD to PNG Converter (supports groups)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python3 psd2png.py file.psd                    # composite (flattened)
  python3 psd2png.py file.psd -o output.png      # composite custom name
  python3 psd2png.py file.psd --groups -d out/   # export per top-level group
  python3 psd2png.py file.psd --layers -d out/   # export all layers (tree)
  python3 psd2png.py file.psd --tree             # show layer tree only
  python3 psd2png.py psd/ --groups -d design/    # batch convert dir
""",
    )
    parser.add_argument("input", nargs="+", help="PSD file(s) or directory")
    parser.add_argument("-o", "--output", help="Output file or directory")
    parser.add_argument("--groups", action="store_true", help="Export each top-level group as PNG")
    parser.add_argument("--layers", action="store_true", help="Export all layers (preserves tree)")
    parser.add_argument("--tree", action="store_true", help="Show layer tree only")
    parser.add_argument("-d", "--outdir", help="Output directory")
    args = parser.parse_args()

    psd_files = []
    for path in args.input:
        p = Path(path)
        if p.is_dir():
            psd_files.extend(sorted(p.glob("*.psd")))
        elif p.is_file() and p.suffix.lower() == ".psd":
            psd_files.append(p)
        else:
            print(f"skipping: {path}", file=sys.stderr)

    if not psd_files:
        print("no PSD files found", file=sys.stderr)
        sys.exit(1)

    print(f"found {len(psd_files)} PSD file(s)\n")

    for psd in psd_files:
        if args.tree:
            print(f"=== {psd.name} ===")
            psd_obj = PSDImage.open(str(psd))
            print_tree(psd_obj)
            print()
            continue

        if args.layers:
            out = args.outdir or f"{psd.stem}_layers"
            export_layers(str(psd), out)
        elif args.groups:
            out = args.outdir or f"{psd.stem}_groups"
            export_groups(str(psd), out)
        else:
            out = args.output
            if out and len(psd_files) > 1:
                out = os.path.join(out, f"{psd.stem}.png")
            export_composite(str(psd), out)


if __name__ == "__main__":
    main()

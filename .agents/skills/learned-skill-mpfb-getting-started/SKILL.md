---
name: mpfb-getting-started
description: AI agent guide for creating and controlling MakeHuman Face Builder (MPFB) characters via Blender MCP's execute_blender_code tool
source: learned
---

# MPFB (MakeHuman Face Builder) — AI Agent Guide via Blender MCP

## When to Use
- When an AI agent needs to create 3D human characters in Blender programmatically
- When the user asks to generate, customize, or rig a human model
- When building character creation pipelines through Blender MCP
- When the user wants to export characters for animation or game engines

## Prerequisites
- **Blender must be running** with MPFB addon enabled (v2.0.16+, requires Blender 4.2+)
- **Blender MCP server must be connected** — verify first with `health_check()`
- MPFB addon installed in Blender (via Extensions or Add-ons panel)

---

## How It Works

The agent uses Blender MCP's `execute_blender_code` tool to run Python code inside Blender. MPFB exposes two interfaces:

1. **bpy operators**: `bpy.ops.mpfb.*` — traditional Blender operator interface (**primary, most reliable**)
2. **Service classes**: `from mpfb.services import *` — direct Python API for programmatic control (**may fail in code execution context**)

**Critical learning:** Service class imports can fail silently or throw `TypeError: 'NoneType' object is not subscriptable`. The most reliable workflow is to create via operator, customize via shape keys, then refit.

---

## Core Pattern

```python
# Always verify connectivity first
health_check()

# Execute MPFB code through Blender MCP
execute_command(
    action="execute_blender_code",
    args={"code": "import bpy; from mpfb.services import HumanService, TargetService ..."}
)
```

---

## Complete API Reference

### Service Classes (Primary Interface)

#### HumanService — Character Creation

```python
from mpfb.services import HumanService, TargetService, RigService, ObjectService

# Create a human with specific phenotype
macro = TargetService.get_default_macro_info_dict()  # default values at 0.5
macro["gender"] = 0.8       # 0=female, 1=male
macro["muscle"] = 0.7       # 0=thin, 1= muscular
macro["weight"] = 0.4       # 0=thin, 1=heavy
macro["height"] = 0.6       # 0=short, 1=tall
macro["proportions"] = 0.5

basemesh = HumanService.create_human(
    macro_detail_dict=macro,
    extra_vertex_groups=True,
    mask_helpers=True,
    detailed_helpers=True,
    scale=0.1
)

# Refit the human after phenotype changes (deforms mesh geometry)
HumanService.refit(basemesh)

# Add a builtin rig to an existing basemesh
rig = HumanService.add_builtin_rig(basemesh, "default", import_weights=True)
# Rig types: "default", "gameengine", "cmu_mb", "mixamo"
# Rigify: "rigify.human_toes", "rigify.human_standard"
```

#### TargetService — Shape Key / Phenotype Control

```python
from mpfb.services import TargetService

# Set individual phenotype values directly on existing human
TargetService.set_target_value(basemesh, "weight", 0.4)
TargetService.set_target_value(basemesh, "muscle", 0.7)
TargetService.set_target_value(basemesh, "age", 0.3)

# Get current phenotype as dict
macro = TargetService.get_macro_info_dict_from_basemesh(basemesh)
# Returns: {"gender": 0.8, "muscle": 0.7, "weight": 0.4, ...}

# Bulk load targets (visemes, face units)
targets = [
    {"target": "viseme_aa", "value": 0.0},
    {"target": "viseme_PP", "value": 0.0},
]
TargetService.bulk_load_targets(basemesh, targets)

# Bake shape keys (irreversible — converts to mesh data)
TargetService.bake_targets(basemesh)

# Prune zero-weight shape keys (clean up)
TargetService.prune_shapekeys(basemesh, cutoff=0.0001)
```

#### RigService — Rigging & Animation

```python
from mpfb.services import RigService

# Add a builtin rig to basemesh
rig = HumanService.add_builtin_rig(basemesh, "default", import_weights=True)
# Rig types: "default", "gameengine", "cmu_mb", "mixamo"
# Rigify: "rigify.human_toes", "rigify.human_standard"

# Find bones by name (pose or edit mode)
hip_bone = RigService.find_pose_bone_by_name("mixamorig:Hips", armature_object)
elbow_bone = RigService.find_edit_bone_by_name("ArmL", armature_object)

# Get bone world space location
loc = RigService.get_world_space_location_of_pose_bone("mixamorig:Hips", armature_object)

# Add IK constraint to a pose bone
RigService.add_ik_constraint_to_pose_bone(
    "LeftFoot", armature_object, target_object, chain_length=2
)

# Copy pose between rigs
RigService.copy_pose(source_armature, target_armature, only_rotation=False)

# Identify what rig type is on an armature
rig_type = RigService.identify_rig(armature_object)
# Returns: "default", "gameengine", "mixamo", "rigify.human_toes", etc.
```

#### ObjectService — Object Discovery

```python
from mpfb.services import ObjectService

# Find basemesh from any object in the character hierarchy
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")

# Find rig/armature
rig = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Skeleton")

# Find all clothes meshes
clothes = ObjectService.find_all_objects_of_type_amongst_nearest_relatives(basemesh, "Clothes")

# Check object types
ObjectService.object_is_basemesh(obj)      # True/False
ObjectService.get_object_type(obj)         # Returns: "Basemesh", "Skeleton", "Clothes", etc.

# Object manipulation
ObjectService.activate_blender_object(obj, deselect_all=True)
ObjectService.deselect_and_deactivate_all()
ObjectService.delete_object(obj)
ObjectService.link_blender_object(obj, parent=rig)
```

#### FaceService — Expressions & Lip Sync

```python
from mpfb.services import FaceService

# Load face shape key packs for animation
FaceService.load_targets(basemesh,
    load_microsoft_visemes=True,    # 23 Microsoft phoneme shapes
    load_meta_visemes=False,        # 15 Meta visemes
    load_arkit_faceunits=False)     # 52 ARKit blendshapes

# Apply a saved expression
expression = {"viseme_aa": 0.8, "viseme_PP": 0.3}
FaceService.set_expression(basemesh, expression)

# Clear all expressions
FaceService.clear_expression(basemesh)
```

#### AssetService — File & Asset Management

```python
from mpfb.services import AssetService

# Find asset files matching pattern
files = AssetService.find_asset_files_matching_pattern(asset_roots, "*.mhclo")

# Get absolute path for an asset by name
path = AssetService.find_asset_absolute_path("pants", "clothes")

# List available clothes assets
roots = AssetService.get_asset_roots("clothes")

# List custom rigs
custom_rigs = AssetService.get_custom_rigs()
```

#### ExportService — Character Export

```python
from mpfb.services import ExportService

# Create deep copy of character for export
export_copy = ExportService.create_character_copy(
    basemesh, name_suffix="_export", place_in_collection=None
)

# Bake modifiers and remove helpers (final cleanup for export)
ExportService.bake_modifiers_remove_helpers(
    basemesh, bake_masks=True, bake_subdiv=True,
    remove_helpers=True, also_proxy=True
)
```

#### ClothesService — Clothing Application

```python
from mpfb.services import ClothesService

# Fit clothes/bodypart to human shape
ClothesService.fit_clothes_to_human(clothes_obj, basemesh, set_parent=False)
```

### bpy Operators (Secondary Interface)

| Operator | Description | Use Case |
|----------|-------------|----------|
| `bpy.ops.mpfb.create_human()` | Create human from scratch | Quick creation |
| `bpy.ops.mpfb.human_from_presets(filepath)` | Load from preset JSON | Reuse character presets |
| `bpy.ops.mpfb.human_from_mhm(filepath)` | Import MHM file | Load MakeHuman characters |
| `bpy.ops.mpfb.load_rig()` | Load rig from .mpfbskel | Apply custom rigs |
| `bpy.ops.mpfb.save_rig()` | Save current rig to JSON | Preserve rig state |
| `bpy.ops.mpfb.refit_human()` | Refit assets after modeling | Update after shape changes |
| `bpy.ops.mpfb.prune_human()` | Remove zero-weight shape keys | Clean up mesh |
| `bpy.ops.mpfb.bake_shapekeys()` | Bake shape keys to mesh | Finalize geometry |
| `bpy.ops.mpfb.load_clothes()` | Load MHCLO clothes file | Apply clothing |
| `bpy.ops.mpfb.export_copy()` | Create export-ready copy | Prepare for export |
| `bpy.ops.mpfb.setup_hair()` | Setup hair on basemesh | Add hair |
| `bpy.ops.mpfb.delete_helpers()` | Delete helper geometry | Cleanup before export |

---

## Complete Workflows

### Workflow 1: Create a Character from Scratch (Reliable Operator Path)

```python
code = """
import bpy

# Step 1: Create human with default phenotype (no args accepted by operator)
bpy.ops.mpfb.create_human()
print("✓ Default human created")

# Step 2: Rename to target name
basemesh = bpy.data.objects.get("Human")
if basemesh:
    basemesh.name = "male_1"
    print(f"✓ Renamed to: {basemesh.name}")
else:
    print("✗ No 'Human' object found")

# Step 3: Customize phenotype via shape keys (see Workflow 2)
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 2: Customize Phenotype via Shape Keys (Most Reliable Method)

**Critical:** Service class imports (`from mpfb.services import TargetService`) can fail silently in code execution context. Use shape key manipulation as the fallback.

```python
code = """
import bpy

# Find existing basemesh
basemesh = bpy.data.objects.get("male_1")  # or "Human"
if not basemesh:
    print("ERROR: No basemesh found — create one first")
else:
    # Get shape key blocks — always prefer name lookup over index
    kb = basemesh.data.shape_keys.key_blocks

    # Discover available shape keys (run once to learn your character's layout):
    # for k in kb: print(f"{k.index}: {k.name}")
    # Output typically: 0=Base, 1-6=race, 7=female, 8=male, 9=breast_size, 10=breast_firmness

    # Gender: key "male" (index 8) and key "female" (index 7) — set inversely
    try:
        kb["male"].value = 0.85   # Male phenotype (higher = more male)
        kb["female"].value = 0.15 # Female phenotype (lower = less female)
    except KeyError:
        # Fallback to index if names don't match
        kb[8].value = 0.85
        kb[7].value = 0.15

    # Race: keys [1-6] = race subtypes (set equal for universal blend)
    for i in range(1, 7):
        kb[i].value = 0.33

    # Breast: keys [9-10] = size/firmness (zero out for male)
    try:
        kb["breast_size"].value = 0.0
        kb["breast_firmness"].value = 0.0
    except KeyError:
        kb[9].value = 0.0
        kb[10].value = 0.0

    print("Shape key phenotype applied")

    # CRITICAL: Call refit to deform the mesh!
    basemesh.select_set(True)
    bpy.context.view_layer.objects.active = basemesh
    bpy.ops.mpfb.refit_human()
    print("✓ Refit applied — mesh geometry updated")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 3: Customize via Service Classes (When Available)

Use this when service classes work. **Always have shape key fallback ready.**

```python
code = """
import bpy
from mpfb.services import TargetService, ObjectService

# Find the basemesh (assuming it's the active object)
active_obj = bpy.context.active_object
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")

if basemesh:
    # Get current phenotype
    try:
        macro = TargetService.get_macro_info_dict_from_basemesh(basemesh)
        print(f"Current: {macro}")
    except Exception as e:
        print(f"Warning: Could not get macro dict: {e}")

    # Customize via service class
    try:
        TargetService.set_target_value(basemesh, "muscle", 0.8)
        TargetService.set_target_value(basemesh, "weight", 0.3)
        TargetService.set_target_value(basemesh, "height", 0.7)

        # Refit after changes
        from mpfb.services import HumanService
        HumanService.refit(basemesh)
    except Exception as e:
        print(f"Warning: Service class failed, use shape key fallback")

else:
    print("No basemesh found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 4: Add Face Animation Shape Keys

```python
code = """
import bpy
from mpfb.services import FaceService, ObjectService

active_obj = bpy.context.active_object
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")

if basemesh:
    # Load Microsoft visemes (23 phoneme shapes for lip sync)
    FaceService.load_targets(basemesh,
        load_microsoft_visemes=True,
        load_meta_visemes=False,
        load_arkit_faceunits=True)
    
    print("Loaded face shape keys for animation")
else:
    print("No basemesh found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 5: Apply Rigify Rig & IK Controls

```python
code = """
import bpy
from mpfb.services import RigService, ObjectService

active_obj = bpy.context.active_object
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")
rig = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Skeleton")

if basemesh and rig:
    # Generate Rigify rig
    rigify_rig = RigService.generate_rigify_rig(rig, name="rigify_standard", meta_rig_action="hide")
    
    # Add IK constraint to left hand
    target_obj = bpy.data.objects.get("LeftHandIK")
    if target_obj:
        RigService.add_ik_constraint_to_pose_bone(
            "mixamorig:LeftHand", rigify_rig, target_obj, chain_length=3
        )
    
    print(f"Generated Rigify rig: {rigify_rig.name}")
else:
    print("Basemesh or rig not found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 6: Prepare Character for Export

```python
code = """
import bpy
from mpfb.services import ExportService, ObjectService

active_obj = bpy.context.active_object
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")

if basemesh:
    # Create export copy (bakes shapekeys, removes helpers)
    export_copy = ExportService.create_character_copy(
        basemesh, name_suffix="_export", place_in_collection=None
    )
    
    # Bake modifiers and clean up
    ExportService.bake_modifiers_remove_helpers(
        export_copy, bake_masks=True, bake_subdiv=True,
        remove_helpers=True, also_proxy=True
    )
    
    print(f"Export copy ready: {export_copy.name}")
else:
    print("Basemesh not found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 7: Apply Clothing

```python
code = """
import bpy
from mpfb.services import ObjectService, ClothesService, AssetService

basemesh = bpy.context.active_object

# Find available clothes
clothes_roots = AssetService.get_asset_roots("clothes")
print(f"Available clothes roots: {clothes_roots}")

# Find a specific clothing asset
pants_path = AssetService.find_asset_absolute_path("pants", "clothes")
if pants_path:
    # Load the clothes file
    bpy.ops.mpfb.load_clothes(filepath=pants_path)
    
    # Fit to human shape (called automatically on import)
    print(f"Clothing loaded from: {pants_path}")
else:
    print("Pants asset not found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

---

## Asset Management & Installation

### Directory Structure for Custom Assets

MPFB discovers assets from directories that follow a specific structure. Your custom assets (e.g., `mpfb2_assets/`) must follow this layout:

```
custom_assets/
├── config/                    ← Optional: configuration files
│   ├── log_levels.json        ← Logging configuration
│   ├── eye_settings.default.json  ← Default eye material settings
│   └── importer_presets.default.json  ← Import defaults
├── cache/                     ← MPFB runtime cache
├── logs/                      ← Runtime logs
└── data/                      ← Main asset directory (scanned by MPFB)
    ├── clothes/               ← Clothing (.mhclo files)
    ├── hair/                  ← Hair assets (.mhclo files)
    ├── eyes/                  ← Eyes (.mhclo files)
    ├── eyebrows/              ← Eyebrows (.mhclo files)
    ├── eyelashes/             ← Eyelashes (.mhclo files)
    ├── skins/                 ← Skin materials (.mhmat files)
    ├── proxymeshes/           ← Proxy meshes for clothing collision
    ├── targets/               ← Shape key targets (.target + .thumb pairs)
    │   ├── animal/            ← Animal feature targets (ears, noses, etc.)
    │   └── arms/              ← Arm detail targets (elbow dimples, etc.)
    └── packs/                 ← Pack definitions (.json files)
        ├── animal01.json      ← Animal features pack
        └── arms01.json        ← Arm details pack
```

**Valid subdirectories MPFB scans:** `clothes`, `hair`, `eyes`, `eyebrows`, `eyelashes`, `skins`, `proxymeshes`, `targets`, `packs`

### How Asset Roots Work

MPFB searches for assets in **3 locations** (in order of priority):

| Priority | Location | Example |
|----------|----------|---------|
| 1 | Default MPFB addon data | `~/.config/blender/5.2/extensions/blender_org/mpfb/data/` |
| 2 | **Second root** (custom assets) | `/home/raka/Animation/mpfb2_assets` |
| 3 | MakeHuman user data | `~/Documents/makehuman/v1py3/data/` |

Assets from higher priority locations override same-named assets from lower priority.

### Installing Custom Assets via Blender MCP

#### Method A: Set `mpfb_second_root` via Python (Recommended for Agents)

**Note:** This approach targets the addon prefs directly. If it fails, use Method B (UI) instead.

```python
code = """
import bpy
import os

# Path to your custom assets directory
asset_path = '/home/raka/Animation/mpfb2_assets'

# Verify path exists
if not os.path.exists(asset_path):
    print(f"ERROR: Asset path does not exist: {asset_path}")
else:
    # Try to set the second root preference
    prefs = bpy.context.preferences
    
    # Try common addon package names — MPFB may use any of these
    success = False
    for pkg in ['blender_org.mpfb', '__main__.mpfb', 'mpfb']:
        try:
            addon_prefs = prefs.addons[pkg].preferences
            addon_prefs.mpfb_second_root = asset_path
            bpy.ops.wm.preferences_save()
            print(f'Second root set to: {asset_path} (via {pkg})')
            success = True
            break
        except Exception:
            pass
    
    if not success:
        print(f"Warning: Could not find addon prefs. Use Method B (Blender UI) instead.")
        print(f"Edit → Preferences → MPFB → Secondary asset root → {asset_path}")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

#### Method B: Set via Blender UI (Manual Fallback)

If Method A fails, set it manually in Blender:

1. Open **Blender**
2. Go to **Edit → Preferences** (or press `Alt + P`)
3. Find the **MPFB** panel in the sidebar
4. Locate **"Secondary asset root"** field
5. Enter absolute path: `/home/raka/Animation/mpfb2_assets`
6. Click **Save Preferences**
7. **Restart Blender** — changes only take effect after restart

### Configuring Asset Directories

MPFB's `LocationService` manages paths. You can configure them programmatically:

```python
code = """
import bpy
from mpfb.services import LocationService, AssetService

# Get current asset roots
clothes_roots = AssetService.get_asset_roots("clothes")
print(f"Clothes discovery paths: {clothes_roots}")

hair_roots = AssetService.get_asset_roots("hair")
print(f"Hair discovery paths: {hair_roots}")

# Check if MakeHuman user data is enabled
mh_enabled = LocationService.is_mh_user_data_enabled()
print(f"MakeHuman user data enabled: {mh_enabled}")

# Get the second root (if set)
second_root = LocationService.get_second_root()
print(f"Second root: {second_root}")

# List all target files in custom assets
import os
targets_dir = '/home/raka/Animation/mpfb2_assets/data/targets'
if os.path.exists(targets_dir):
    for subdir in os.listdir(targets_dir):
        target_path = os.path.join(targets_dir, subdir)
        print(f"Target subdirectory: {target_path}")
        for file in os.listdir(target_path):
            if file.endswith('.target'):
                print(f"  - {file}")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Target Files (.target + .thumb)

Shape key targets come in **pairs**:
- `{name}.target` — The actual shape key data (XML/JSON format)
- `{name}.thumb` — Thumbnail image for UI display

Example target structure:
```
data/targets/animal/
├── culturalibre_faun_face.target    ← Faun face shape keys
├── culturalibre_faun_face.thumb     ← Thumbnail
├── titleknown_catgirl_ears.target   ← Cat ears shape keys
└── titleknown_catgirl_ears.thumb    ← Thumbnail
```

Apply targets to a character:
```python
code = """
import bpy
from mpfb.services import TargetService, ObjectService

basemesh = bpy.context.active_object
target_path = '/home/raka/Animation/mpfb2_assets/data/targets/animal/titleknown_catgirl_ears.target'

# Load target from file
import json
with open(target_path, 'r') as f:
    target_data = json.load(f)

# Apply targets to basemesh
if isinstance(target_data, list):
    TargetService.bulk_load_targets(basemesh, target_data)
else:
    TargetService.set_target_value(basemesh, target_data['target'], target_data['value'])

print(f"Applied target from: {target_path}")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Asset Packs (.json in packs/)

Pack definitions are JSON files that bundle multiple targets or assets:

```python
code = """
import json

# Load pack definition
pack_path = '/home/raka/Animation/mpfb2_assets/data/packs/animal01.json'
with open(pack_path, 'r') as f:
    pack_data = json.load(f)

print(f"Pack: {json.dumps(pack_data, indent=2)}")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Config Files

MPFB reads configuration from the `config/` directory:

| File | Purpose |
|------|---------|
| `log_levels.json` | Logging verbosity (`{"default": 3}`) |
| `eye_settings.default.json` | Default eye material properties (iris color, pupil size, etc.) |
| `importer_presets.default.json` | Import defaults (subdiv levels, helper masks, etc.) |

**Example importer presets:**
```json
{
  "add_subdiv_modifier": true,
  "detailed_helpers": true,
  "extra_vertex_groups": true,
  "feet_on_ground": true,
  "import_body": true,
  "import_clothes": true,
  "mask_base_mesh": true,
  "rig_as_parent": true,
  "scale_factor": "METER",
  "skin_material_type": "ENHANCED",
  "subdiv_levels": 1
}
```

---

## Phenotype Reference Table

All phenotype values are floats from **0.0 to 1.0**:

| Property | Description | 0.0 | 1.0 |
|----------|-------------|-----|-----|
| `gender` | Gender lean | Female | Male |
| `age` | Age | Baby/Child | Elderly |
| `muscle` | Muscle mass | Thin | Muscular |
| `weight` | Body weight | Underweight | Overweight |
| `proportions` | Body proportions | Short limbs | Long limbs |
| `height` | Height | Very short | Very tall |
| `cupsize` | Breast size (female) | Small | Large |
| `firmness` | Breast firmness (female) | Low | High |

**Race distribution** (via TargetService macro dict — must sum to ~1.0):
```python
"race": {
    "asian": 0.33,
    "caucasian": 0.33,
    "african": 0.33
}
```

**Note:** When using **shape key manipulation** (Workflow 2), race is controlled by keys [1–6] directly on the mesh. These are NOT the same as the TargetService macro dict — shape keys store raw blend values (set each to `0.33` for equal blend across all six race subtypes). The two approaches are independent; use whichever interface works in your context.

---

## Object Type Names

MPFB labels objects with `object_type` property for discovery:

| Type | Description |
|------|-------------|
| `"Basemesh"` | Main human mesh |
| `"Skeleton"` | Main armature/rig |
| `"Subrig"` | Sub-rig armatures (hands, fingers) |
| `"Proxymeshes"` | Body proxy mesh for clothing |
| `"Clothes"` | Clothing meshes |
| `"Eyes"`, `"Eyebrows"`, `"Eyelashes"` | Facial body parts |
| `"Tongue"`, `"Teeth"` | Internal facial parts |
| `"Hair"` | Hair geometry |

---

## Agent Best Practices

### 1. Always Verify First
```python
# Step 1: Check Blender MCP connectivity
health_check()

# Step 2: Find existing basemesh if any
execute_command(action="get_scene_info")
```

### 2. Prefer Shape Key Manipulation Over Service Classes
**Critical learning:** Service class imports (`from mpfb.services import TargetService`) can fail silently or throw `TypeError: 'NoneType' object is not subscriptable` in code execution context. The most reliable approach is:

1. Create human via operator: `bpy.ops.mpfb.create_human()` (no args)
2. Customize phenotype by directly setting shape key values on the mesh
3. Call `bpy.ops.mpfb.refit_human()` to deform the mesh

Service classes work when called from Blender's UI context, but in agent code execution they may fail. **Shape key manipulation is always reliable.**

### 3. Handle Missing Objects Gracefully
Always check if the basemesh exists before operating:
```python
code = """
import bpy
from mpfb.services import ObjectService
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(bpy.context.active_object, "Basemesh")
if not basemesh:
    print("ERROR: No basemesh found — create one first")
"""
```

### 4. Discover Shape Keys by Name Before Using Indices
Shape key names are more reliable than indices across MPFB versions. Always discover first:
```python
code = """
import bpy
basemesh = bpy.data.objects.get("male_1")
if basemesh and basemesh.data.shape_keys:
    for k in basemesh.data.shape_keys.key_blocks:
        print(f"Index {k.index}: name='{k.name}', value={k.value:.3f}")
"""
```

### 5. Bake Shape Keys Before Export
Shape keys are deformable — bake them with `ExportService.bake_modifiers_remove_helpers()` before exporting to GLB for stable mesh data.

### 6. Clean Up Helpers After Finalizing
Delete helper geometry (`mpfb.delete_helpers()`) before export to reduce file size and prevent issues.

### 7. Use Absolute Paths for Assets
All file paths (MHM, MHCLO, JSON presets) must be absolute paths accessible from Blender's filesystem.

---

## Pitfalls

- **Blender not running**: `execute_blender_code` will fail. Ensure Blender is open with MPFB enabled.
- **MPFB addon not loaded**: If `ModuleNotFoundError: No module named 'mpfb'`, the MPFB addon isn't installed or isn't activated in Blender.
- **Basemesh not found**: After creating a human, always verify `basemesh.name` exists before calling other services.
- **Shape key conflicts**: Loading face shape keys twice will create duplicates — check if they're already loaded.
- **Baking is irreversible**: `TargetService.bake_targets()` and `ExportService.bake_modifiers_remove_helpers()` cannot be undone.
- **Rig weight transfer**: When switching rigs, use `RigService.autotransfer_weights()` to preserve mesh deformation.
- **Scale matters**: MPFB uses `scale=0.1` by default (Blender units). Adjust for your scene's scale requirements.
- **Code must be valid Python**: Syntax errors in `execute_blender_code` will fail silently — test code locally first.
- **Service class imports can fail silently**: `from mpfb.services import TargetService` may throw `TypeError: 'NoneType' object is not subscriptable`. Always fallback to shape key manipulation if service classes don't work.
- **Shape key values don't deform mesh until refit**: After setting shape key values, you MUST call `bpy.ops.mpfb.refit_human()` to apply the geometry changes. Without it, values sit in shape keys but don't deform the mesh.
- **Operator parameters are panel-bound**: `bpy.ops.mpfb.create_human()` does NOT accept phenotype keyword arguments — it reads from `NEW_HUMAN_PROPERTIES` panel state. Pass no arguments and customize afterward via shape keys.

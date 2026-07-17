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

1. **bpy operators**: `bpy.ops.mpfb.*` — traditional Blender operator interface
2. **Service classes**: `from mpfb.services import *` — direct Python API for programmatic control

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

### Workflow 1: Create a Character from Scratch

```python
code = """
import bpy
from mpfb.services import HumanService, TargetService, RigService, ObjectService

# Step 1: Define phenotype
macro = TargetService.get_default_macro_info_dict()
macro["gender"] = 0.8    # male-leaning
macro["muscle"] = 0.6
macro["weight"] = 0.4
macro["height"] = 0.5
macro["age"] = 0.3

# Step 2: Create human
basemesh = HumanService.create_human(
    macro_detail_dict=macro,
    extra_vertex_groups=True,
    mask_helpers=True,
    detailed_helpers=True
)

# Step 3: Add default rig
rig = HumanService.add_builtin_rig(basemesh, "default", import_weights=True)

print(f"Created human: basemesh={basemesh.name}, rig={rig.name}")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 2: Customize an Existing Character

```python
code = """
import bpy
from mpfb.services import TargetService, ObjectService

# Find the basemesh (assuming it's the active object)
active_obj = bpy.context.active_object
basemesh = ObjectService.find_object_of_type_amongst_nearest_relatives(active_obj, "Basemesh")

if basemesh:
    # Get current phenotype
    macro = TargetService.get_macro_info_dict_from_basemesh(basemesh)
    print(f"Current: {macro}")

    # Customize
    TargetService.set_target_value(basemesh, "muscle", 0.8)
    TargetService.set_target_value(basemesh, "weight", 0.3)
    TargetService.set_target_value(basemesh, "height", 0.7)

    # Refit after changes
    from mpfb.services import HumanService
    HumanService.refit(basemesh)
else:
    print("No basemesh found")
"""
execute_command(action="execute_blender_code", args={"code": code})
```

### Workflow 3: Add Face Animation Shape Keys

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

### Workflow 4: Apply Rigify Rig & IK Controls

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

### Workflow 5: Prepare Character for Export

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

### Workflow 6: Apply Clothing

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

**Race distribution** (must sum to ~1.0):
```python
"race": {
    "asian": 0.33,
    "caucasian": 0.33,
    "african": 0.33
}
```

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

### 2. Use Service Classes Over Operators
Service classes (`HumanService`, `TargetService`) are more reliable and programmatic than operators. Only use `bpy.ops.mpfb.*` when a service method isn't available.

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

### 4. Bake Shape Keys Before Export
Shape keys are deformable — bake them with `ExportService.bake_modifiers_remove_helpers()` before exporting to GLB for stable mesh data.

### 5. Clean Up Helpers After Finalizing
Delete helper geometry (`mpfb.delete_helpers()`) before export to reduce file size and prevent issues.

### 6. Use Absolute Paths for Assets
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

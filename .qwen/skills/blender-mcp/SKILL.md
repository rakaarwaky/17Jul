---
name: blender-mcp
description: Complete guide for AI agents to control Blender 3D via MCP tools — scene ops, object manipulation, rendering, asset import, and AI 3D generation
source: learned
---

# BlenderArwaky MCP — AI Agent Guide

## When to Use
- When an AI agent needs to create, modify, or render 3D scenes in Blender
- When the user asks to create 3D objects, models, environments, or renders
- When the user wants to import/export 3D assets (GLB/GLTF)
- When AI 3D generation from text prompts is needed
- When the user needs viewport screenshots for visual feedback

## Prerequisites
- Blender must be running with the **BlenderArwaky addon** enabled (port 9876)
- MCP server must be started: `uv run blender-arwaky`
- Verify connectivity first with `health_check()` before any operations

---

## Core Workflow Pattern

### Step 1: Always Start with Discovery

```python
# Check Blender is connected
health_check()

# Discover what you can do
list_commands(domain="all")  # or filter by domain: "scene", "object", "render", "asset", "generation"
```

### Step 2: Execute Actions via `execute_command`

All operations go through the single universal tool:

```python
execute_command(
    action="ACTION_NAME",
    args={"param1": "value1", "param2": [x, y, z]}
)
```

---

## Complete Action Reference

### Scene Operations

| Action | Purpose | Key Args |
|--------|---------|----------|
| `get_scene_info` | Inspect current scene — objects, counts, render engine | none |
| `cleanup_scene` | Remove all objects from scene | `mode`: "all" / "objects" / "meshes" |
| `setup_environment` | Set HDRI lighting | `hdri_id`, `strength` (0.0-10.0) |

**Usage:**
```python
# Inspect scene before modifying
execute_command(action="get_scene_info")

# Clean slate
execute_command(action="cleanup_scene", args={"mode": "all"})

# Studio lighting via HDRI
execute_command(
    action="setup_environment",
    args={"hdri_id": "default_studio", "strength": 1.0}
)
```

### Object Operations

| Action | Purpose | Key Args |
|--------|---------|----------|
| `create_primitive` | Add basic shapes | `primitive_type`: "CUBE"/"SPHERE"/"CYLINDER"/"CONE"/"TORUS"/"PLANE"/"GRID"/"MONKEY" |
| `set_object_transform` | Move, rotate, scale objects | `object_name`, `location: [x,y,z]`, `rotation: [x,y,z]`, `scale: [x,y,z]` |
| `get_object_info` | Inspect a specific object | `object_name` |
| `delete_object` | Remove an object | `object_name` |
| `set_material` | Assign material to object | `object_name`, `material_name` |
| `apply_modifier` | Add/subdivide modifiers | `object_name`, `modifier_name`: "SUBSURF"/"BEVEL"/etc. |
| `place_asset` | Position an imported asset | `asset_id`, `location`, `rotation`, `scale` |

**Usage:**
```python
# Create a sphere at origin with custom scale
execute_command(
    action="create_primitive",
    args={"primitive_type": "SPHERE", "location": [0, 0, 0], "scale": [1, 1, 1]}
)

# Move it
execute_command(
    action="set_object_transform",
    args={"object_name": "Sphere", "location": [3, 0, 0]}
)

# Apply subdivision modifier
execute_command(
    action="apply_modifier",
    args={"object_name": "Sphere", "modifier_name": "SUBSURF"}
)
```

### Viewport & Rendering

| Action | Purpose | Key Args |
|--------|---------|----------|
| `get_viewport_screenshot` | Capture current viewport as PNG | `max_size`: max dimension in pixels (default 800) |
| `render` | Full frame render to file | `output_path`, `resolution_x`, `resolution_y` |

**Usage:**
```python
# Get a visual check of the scene
execute_command(action="get_viewport_screenshot", args={"max_size": 1200})

# Render at 4K
execute_command(
    action="render",
    args={"output_path": "/tmp/render.png", "resolution_x": 3840, "resolution_y": 2160}
)
```

### Import / Export

| Action | Purpose | Key Args |
|--------|---------|----------|
| `import_glb` | Import GLB/GLTF model | `file_path` (absolute path) |
| `export_model` | Export object to file | `object_name`, `file_path`, `export_format`: "glb"/"obj" |

**Usage:**
```python
# Import a GLB model
execute_command(
    action="import_glb",
    args={"file_path": "/tmp/model.glb"}
)

# Export selected object
execute_command(
    action="export_model",
    args={"object_name": "MyObject", "file_path": "/tmp/export.glb", "export_format": "glb"}
)
```

### Custom Blender Python

| Action | Purpose | Key Args |
|--------|---------|----------|
| `execute_blender_code` | Run arbitrary bpy Python code | `code`: Python string |

**Usage:**
```python
# Any Blender Python operation
execute_command(
    action="execute_blender_code",
    args={"code": "import bpy; bpy.ops.object.mode_set(mode='EDIT')}"}
)
```

### Asset Providers (Poly Haven + Sketchfab)

| Action | Purpose | Key Args |
|--------|---------|----------|
| `search_all_assets` | Search across providers | `query`, `asset_type`: "hdri"/"texture"/"model", `limit` |
| `download_asset` | Download and import asset | `asset_id`, `provider`: "polyhaven"/"sketchfab", `resolution` |

**Usage:**
```python
# Search for sunset HDRIs
execute_command(
    action="search_all_assets",
    args={"query": "sunset", "asset_type": "hdri", "limit": 5}
)
```

### AI 3D Generation (Hyper3D Rodin + Hunyuan3D)

| Action | Purpose | Key Args |
|--------|---------|----------|
| `start_generation` | Start text-to-3D generation | `prompt`: description string |
| `poll_generation` | Check generation job status | `job_id` |
| `import_generated_asset` | Import generated model into scene | `job_id`, `name` |

**Usage:**
```python
# Start AI generation
result = execute_command(
    action="start_generation",
    args={"prompt": "a medieval shield with gold trim"}
)
job_id = result.get("job_id")

# Poll until done (repeat every 5s, max ~30 times)
execute_command(action="poll_generation", args={"job_id": job_id})

# Import when ready
execute_command(
    action="import_generated_asset",
    args={"job_id": job_id, "name": "Medieval_Shield"}
)
```

---

## Common Workflows

### Workflow 1: Create a Scene from Scratch

```python
# 1. Verify connectivity
health_check()

# 2. Inspect current scene
execute_command(action="get_scene_info")

# 3. Clean up
execute_command(action="cleanup_scene", args={"mode": "all"})

# 4. Add objects
execute_command(
    action="create_primitive",
    args={"primitive_type": "PLANE", "location": [0, 0, 0]}
)
execute_command(
    action="create_primitive",
    args={"primitive_type": "SPHERE", "location": [0, 2, 0], "scale": [1.5, 1.5, 1.5]}
)

# 5. Set lighting
execute_command(
    action="setup_environment",
    args={"hdri_id": "default_studio"}
)

# 6. Visual check
execute_command(action="get_viewport_screenshot")

# 7. Render
execute_command(
    action="render",
    args={"output_path": "/tmp/scene.png"}
)
```

### Workflow 2: Generate AI Asset and Place It

```python
# 1. Start generation
gen_result = execute_command(
    action="start_generation",
    args={"prompt": "a low-poly tree with green foliage"}
)

# 2. Poll until complete (loop in agent logic)
while True:
    status = execute_command(action="poll_generation", args={"job_id": gen_result["job_id"]})
    if status.get("status") in ("DONE", "COMPLETED"):
        break
    # Wait and retry...

# 3. Import into scene
execute_command(
    action="import_generated_asset",
    args={"job_id": gen_result["job_id"], "name": "Tree"}
)

# 4. Position it
execute_command(
    action="set_object_transform",
    args={"object_name": "Tree", "location": [5, 0, 3]}
)
```

### Workflow 3: Build a Product Display

```python
# Clean scene
execute_command(action="cleanup_scene")

# Add ground plane
execute_command(
    action="create_primitive",
    args={"primitive_type": "PLANE", "location": [0, 0, 0], "scale": [10, 10, 1]}
)

# Import product (GLB)
execute_command(
    action="import_glb",
    args={"file_path": "/tmp/product.glb"}
)

# Position and scale
execute_command(
    action="set_object_transform",
    args={"object_name": "product", "location": [0, 0, 0.5], "scale": [2, 2, 2]}
)

# Studio lighting
execute_command(
    action="setup_environment",
    args={"hdri_id": "default_studio"}
)

# Screenshot for review
execute_command(action="get_viewport_screenshot", args={"max_size": 1024})
```

---

## Agent Best Practices

### 1. Always Verify First
Before any scene manipulation, call `health_check()` and `get_scene_info()`. Know what you're working with.

### 2. Use Object Names Carefully
- Blender auto-generates names (e.g., "Sphere", "Cube.001")
- After creating an object, check its name via `get_object_info` or `get_scene_info`
- When using `execute_blender_code`, you can rename: `bpy.context.active_object.name = 'MyObject'`

### 3. Coordinate System
- Blender uses `[X, Y, Z]` where Z is up
- Rotation uses Euler angles in radians `[rx, ry, rz]`
- Scale is multiplicative `[sx, sy, sz]`

### 4. Handle Async Operations
AI generation (`start_generation`) is async — always poll with `poll_generation` until status is DONE/FAILED before importing.

### 5. Error Handling
All tools return JSON. Check for `"error"` keys in responses:
```python
result = execute_command(action="...", args={...})
if "error" in result:
    # Handle error — retry, adjust params, or report to user
```

### 6. File Paths Must Be Absolute
`import_glb`, `export_model`, and `render` all require absolute file paths. Use `/tmp/` for temporary files.

### 7. Use `execute_blender_code` as Escape Hatch
When a specific operation isn't available through the catalog, write raw bpy code:
```python
execute_command(
    action="execute_blender_code",
    args={"code": "import bpy; bpy.context.scene.render.engine = 'CYCLES'"}
)
```

---

## Pitfalls

- **Blender not running**: `health_check()` will fail. Ensure Blender is open with the addon enabled.
- **Object name collisions**: Blender auto-names objects — always verify names after creation.
- **Missing HDRI files**: `setup_environment` requires HDRI files to be downloaded first. Use known IDs like "default_studio".
- **Generation timeouts**: AI generation can take 2-5 minutes. Poll every 5 seconds, max ~30 attempts (150s total).
- **Absolute paths required**: Relative paths will fail in import/export/render operations.
- **Addon not enabled**: If `ImportError` occurs, the BlenderArwaky addon is not installed or not activated.
- **Scene state persistence**: Operations modify the live Blender scene — changes are permanent unless you clean up.

# AGENT.md — "Silent Summit" Luxury Hoodie Forest Scene

## Project Overview

**Scene:** Misty pine forest — moody, dramatic, mysterious
**Action:** Luxury hoodie dramatic reveal — single male model walks through fog, stops, reveals product, final power pose
**Cast:** 1 character — `male_1` (model)
**Mood:** Moody, dramatic, premium — "worn by silence, made for the summit"
**Deliverable:** 3D animated fashion film, 25 seconds (750 frames @ 30fps), 8 camera cuts
**Engine:** Blender 5.2 (`~/App/blender-5.2.0-linux-x64/blender`, symlinked as `./Blender/blender`) — Cycles via HIP ROCm
**GPU:** AMD Radeon RX 6800 XT (16 GB VRAM) — HIP ROCm
**Format:** Vertical video, 9:16 portrait aspect ratio (1080×1920)
**Frame rate:** 30 fps
**Pipeline:** Blender only — no external apps (no ComfyUI, no SDXL)

---

## Documentation Index

| File | Contents |
|------|----------|
| `AGENT.md` | Project overview, directory structure, naming rules, versioning |
| `CONCEPTS.md` | Creative brief, visual identity, shot list, camera specs, beat map |
| `PIPELINE.md` | Workflow, phase gates, render specs, troubleshooting |
| `REQUIREMENTS.md` | System, software, asset, and render requirements |

---

## Directory Structure

```
17Jul/
├── AGENT.md                    # This file — entry point
├── CONCEPTS.md                 # Creative brief, visual identity, shot list
├── PIPELINE.md                 # Workflow, phase gates, render specs, troubleshooting
├── REQUIREMENTS.md             # System, software, asset, and render requirements
├── Blender -> ~/App/blender-5.2.0-linux-x64/   # Symlink to Blender
├── assets/
│   └── character/
│       └── male_1/
│           ├── male_1.abc                      # Alembic cache — animation embedded
│           ├── male_1.fbx                      # FBX export — mesh reference only
│           └── textures/
│               ├── hoodie_diffuse.png           # Hoodie base color
│               ├── hoodie_normal.png            # Hoodie normal map
│               ├── hoodie_roughness.png         # Hoodie roughness
│               ├── hoodie_metalness.png         # Hoodie metalness (zippers)
│               ├── hoodie_ao.png                # Hoodie ambient occlusion
│               ├── hoodie_displacement.png      # Hoodie displacement
│               ├── pants_diffuse.png            # Pants base color
│               ├── pants_normal.png             # Pants normal map
│               ├── skin_diffuse.png             # Skin base color
│               └── skin_normal.png              # Skin normal map
├── design/                     # Reference files — READ-ONLY
├── scenes/                     # Blender .blend work files
│   └── NOTES.md                # Production decisions log
├── renders/
│   ├── frames/                 # PNG sequence output
│   └── final/                  # Final MP4
└── scripts/                    # Utility scripts
```

---

## Naming Rules

### Blender Scene Files
**Pattern:** `{project}_{version}_{stage}.blend`

- `hoodie_v01_layout.blend` — initial scene layout
- `hoodie_v02_lighting.blend` — lighting pass
- `hoodie_v03_render.blend` — render-ready
- `hoodie_final.blend` — final delivered version

### Exported Assets
**Pattern:** `{character}_{asset}.{ext}`

- `male_1.abc` — Alembic with embedded animation
- `male_1.fbx` — FBX mesh reference

### Textures
**Pattern:** `{asset}_{map}.{ext}`

- `hoodie_diffuse.png` — hoodie base color
- `hoodie_normal.png` — hoodie normal map
- `pants_diffuse.png` — pants base color
- `skin_diffuse.png` — skin base color

### Renders
**Pattern:** `{scene}_{res}_{fps}.mp4`

- `hoodie_1080x1920_30fps.mp4` — final master
- `hoodie_web.mp4` — web-optimized variant

### Camera Files
**Pattern:** `CAM_S{number}`

- `CAM_S01` through `CAM_S08` — one per shot

### Documentation
**Pattern:** `UPPERCASE_WITH_UNDERSCORES.md`

---

## Versioning

| Type | Pattern | Example |
|------|---------|---------|
| Iterative saves | `v01`, `v02`, `v03` | `hoodie_v01.blend` |
| Milestone saves | `v{number}_{stage}` | `hoodie_v05_lighting.blend` |
| Final | Keep both | `hoodie_final.blend` + last WIP `hoodie_v05_render.blend` |

---

## Characters

### Male Model (`male_1`)

| Attribute | Value |
|-----------|-------|
| **Role** | Solo model — luxury hoodie showcase |
| **Build** | Athletic, 180-185cm |
| **Outfit** | Luxury hoodie (oversized, heavyweight cotton) + dark tapered pants |
| **Footwear** | Premium black sneakers or boots |
| **Hair** | Short or styled, natural |
| **Expression** | Confident, subtle, mysterious |
| **Animation** | Walk cycle → stop/turn → hood adjustment → power pose |

### Hoodie Design Specs
- **Fit:** Oversized, drop shoulder
- **Fabric:** Heavyweight cotton (350+ GSM)
- **Features:** Kangaroo pocket, ribbed cuffs/hem, metal zipper (optional), drawstring hood
- **Color:** Charcoal/dark grey (primary), with subtle texture variation
- **Branding:** Minimal — small embossed logo on chest or sleeve (if any)

---

## Environment

### Misty Pine Forest
- **Trees:** Tall pine trunks — vertical rhythm, dense spacing
- **Ground:** Pine needle carpet, mossy patches, fallen logs
- **Atmosphere:** Thick volumetric fog — heavier at ground, thinner at canopy
- **Lighting:** Overcast ambient + dramatic single key light
- **Props:** Weathered stump, faint trail (optional)

---

## Technical Specs

| Spec | Value |
|------|-------|
| Resolution | 1080×1920, 9:16 portrait |
| Frame Rate | 30 fps |
| Duration | 25 seconds (750 frames) |
| Engine | Cycles HIP ROCm (quality) / EEVEE (draft) |
| GPU | AMD RX 6800 XT — 16 GB VRAM |
| Output | PNG sequence → H.264 MP4 |
| Pipeline | Blender only — no external apps |

---

## Agent Instructions

- **Read this file first** before taking any action on this project.
- **Do not overwrite** `design/` contents — they are read-only references.
- **Blender only** — no ComfyUI, no SDXL, no external rendering apps.
- **Import ABC, not FBX** — animation only exists in the `.abc` files.
- **Version scenes:** save as `hoodie_v01.blend`, `hoodie_v02.blend`, etc.
- **Document decisions:** log deviations in `scenes/NOTES.md`.
- **Ask before heavy simulations:** confirm with user before baking fluid/cloth/hair.
- **Blender launch:** always use `~/App/blender-5.2.0-linux-x64/blender` or `./Blender/blender`.
- **Cycles render:** use GPU Compute (HIP ROCm).

---

## Asset Tracking

Record exported assets in `assets/INDEX.md`:

```
male_1.abc                 — Alembic cache with walk + reveal animation (embedded)
male_1.fbx                 — FBX mesh reference for hoodie model
textures/hoodie_diffuse.png — Hoodie base color, 4K resolution
```

---

## Development Roadmap

| Phase | Status | Goal |
|-------|--------|------|
| Pre-production | ✅ Done | Concept, scenario, shot list, references |
| Character Creation | ⬜ Pending | Build male model + hoodie in MB-Lab/manual |
| Hoodie Modeling | ⬜ Pending | Model luxury hoodie with PBR materials |
| Animation | ⬜ Pending | Walk, reveal, hood adjustment, power pose |
| Scene Layout | ⬜ Pending | Forest environment, fog, lighting |
| Camera Work | ⬜ Pending | 8 cameras locked per shot list |
| Rendering | ⬜ Pending | Cycles final render, MP4 encode |

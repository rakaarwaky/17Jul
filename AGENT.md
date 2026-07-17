# AGENT.md — "Silent Summit" Luxury Hoodie Forest Scene

## Project Overview

**Scene:** Misty pine forest — luxury hoodie dramatic reveal
**Cast:** 1 character — `male_1`
**Deliverable:** 3D animated fashion film, 750 frames (25s @ 30fps), 8 camera cuts
**Pipeline:** Blender only — no external apps

---

## Documentation Index

| File | Contents |
|------|----------|
| `AGENT.md` | This file — entry point |
| `CONCEPTS.md` | Creative brief, environment, character, lighting, shot list |
| `PIPELINE.md` | Workflow, risk register, troubleshooting |
| `PROGRESS.md` | Phase gates, checklists, exit criteria |
| `REQUIREMENTS.md` | System, assets, render specs, performance |

---

## Directory Structure

```
17Jul/
├── AGENT.md
├── CONCEPTS.md
├── PIPELINE.md
├── PROGRESS.md
├── REQUIREMENTS.md
├── blender-arwaky → ~/mcp-arwaky/blender-arwaky/  (symlink, ignored)
├── assets/
│   └── character/
│       └── male_1/
│           ├── male_1.abc
│           ├── male_1.fbx
│           └── textures/
├── design/                    # Reference PSD/PNG — READ-ONLY
├── psd/                       # PSD source files
├── scenes/
│   └── NOTES.md
├── renders/
│   ├── frames/
│   └── final/
└── scripts/
```

---

## Naming Rules

| Type | Pattern | Example |
|------|---------|---------|
| Scene files | `{project}_{version}_{stage}.blend` | `hoodie_v01_layout.blend` |
| Character assets | `{character}_{asset}.{ext}` | `male_1.abc` |
| Textures | `{asset}_{map}.{ext}` | `hoodie_diffuse.png` |
| Renders | `{scene}_{res}_{fps}.mp4` | `hoodie_1080x1920_30fps.mp4` |
| Cameras | `CAM_S{number}` | `CAM_S01` – `CAM_S08` |
| Docs | `UPPERCASE_WITH_UNDERSCORES.md` | `AGENT.md` |

---

## Versioning

| Type | Pattern | Example |
|------|---------|---------|
| Iterative | `v01`, `v02`, `v03` | `hoodie_v01.blend` |
| Milestone | `v{number}_{stage}` | `hoodie_v05_lighting.blend` |
| Final | Keep both | `hoodie_final.blend` + last WIP |

---

## Agent Instructions

- Read this file first before any action.
- `design/` and `psd/` are READ-ONLY — do not modify.
- Blender only — no ComfyUI, no SDXL, no external apps.
- Import ABC, not FBX — animation is only in `.abc`.
- Version scenes: `hoodie_v01.blend`, `hoodie_v02.blend`, etc.
- Log decisions in `scenes/NOTES.md`.
- Ask before heavy simulations (fluid, cloth, hair).
- Blender binary: `~/App/blender-5.2.0-linux-x64/blender`
- Cycles render: GPU Compute (HIP ROCm).

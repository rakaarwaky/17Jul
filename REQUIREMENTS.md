# Requirements — "Silent Summit" Hoodie Forest Scene

---

## System Requirements

| Component | Specification |
|-----------|---------------|
| **OS** | Linux |
| **GPU** | AMD Radeon RX 6800 XT (16 GB VRAM) |
| **Render** | Cycles via HIP ROCm |
| **Blender** | v5.2 (`~/App/blender-5.2.0-linux-x64/blender`) |
| **Python** | Bundled with Blender 5.2 |
| **Storage** | ~50 GB free (character ABC ~1.5GB + textures + renders) |

---

## Software Requirements

| Software | Path | Purpose |
|----------|------|---------|
| **Blender 5.2** | `~/App/blender-5.2.0-linux-x64/blender` | Main 3D application |
| **Blender MCP** | `~/mcp-arwaky/blender-arwaky/` | Agent-Blender bridge |
| **FFmpeg** | System PATH | PNG sequence → MP4 encode |

---

## Blender Add-ons (Required)

Open Blender → Edit → Preferences → Add-ons → search & check:

| Add-on | Purpose |
|--------|---------|
| **LoopTools** | Bridge, relax, circle, space vertices — hoodie modeling |
| **Bool Tool** | Boolean operations UI — pocket/zipper modeling |
| **Node Wrangler** | Shader node shortcuts — PBR material setup |
| **3D View: Pie Menu** | Quick access tools |
| **Mesh: Edit Mesh Tools** | Extra modeling ops |
| **Animation: Add Camera Rigs** | Camera rig presets |
| **Import-Export: Import Images as Planes** | Background plate import |
| **Import-Export: FBX format** | Asset exchange |
| **Import-Export: Alembic format** | Import character ABC files (animation) |
| **Mesh: 3D-Print Toolbox** | Mesh inspection, manifold check |

### Add-on Directory

`~/.config/blender/5.2/scripts/addons/`

---

## Asset Requirements

### Character (`male_1`)

| Asset | Format | Status |
|-------|--------|--------|
| Body model | .blend / .abc | ⬜ Pending |
| Hoodie model | .blend | ⬜ Pending |
| Pants model | .blend | ⬜ Pending |
| Footwear | .blend | ⬜ Pending |
| Animation (walk + reveal + pose) | .abc | ⬜ Pending |

### PBR Texture Sets

| Asset | Maps Required | Resolution |
|-------|---------------|------------|
| Hoodie | Diffuse, Normal, Roughness, Metalness, AO, Displacement | 4096×4096 |
| Pants | Diffuse, Normal, Roughness | 2048×2048 |
| Skin | Diffuse, Normal | 2048×2048 |

### Environment

| Asset | Method | Status |
|-------|--------|--------|
| Pine trees | Array/duplicate trunks | ⬜ Pending |
| Ground plane | Displacement modifier + procedural | ⬜ Pending |
| Volumetric fog | Volume Scatter shader domain | ⬜ Pending |

---

## Scene Requirements

| Spec | Value |
|------|-------|
| Resolution | 1080×1920 (9:16 portrait) |
| Frame Rate | 30 fps |
| Duration | 750 frames (25 seconds) |
| Cameras | 8 (CAM_S01 – CAM_S08) |
| Character | 1 (male_1) |

---

## Render Requirements

| Setting | Final | Preview |
|---------|-------|---------|
| Engine | Cycles | Eevee |
| Device | GPU Compute (HIP ROCm) | GPU |
| Samples | 512 | 64 |
| Denoising | OpenImageDenoise | OFF |
| Output | 16-bit PNG | Viewport |
| Encoding | H.264 CRF 18 | — |

---

## Pipeline Requirements

| Rule | Detail |
|------|--------|
| **Blender only** | No ComfyUI, no SDXL, no external rendering apps |
| **Animation in ABC** | No manual keyframes in Blender — import .abc and enable Cache Playback |
| **Blender binary** | Always use `~/App/blender-5.2.0-linux-x64/blender` — never system `blender` |
| **HIP ROCm** | GPU render device — not CUDA, not OptiX |
| **Version scenes** | `hoodie_v01.blend`, `hoodie_v02.blend`, etc. |

---

## Performance Requirements

| Metric | Target |
|--------|--------|
| Polycount (character) | <100k |
| Polycount (environment) | <200k |
| Texture memory | <8 GB VRAM |
| Single frame render (Cycles 512s) | <120s |
| Full render (750 frames) | <10 hours |
| Final MP4 size | <500 MB |

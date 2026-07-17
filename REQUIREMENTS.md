# Requirements — "Silent Summit" Hoodie Forest Scene

---

## System

| Component | Specification |
|-----------|---------------|
| **OS** | Linux |
| **GPU** | AMD Radeon RX 6800 XT (16 GB VRAM) |
| **Render** | Cycles via HIP ROCm |
| **Blender** | v5.2 (`~/App/blender-5.2.0-linux-x64/blender`) |
| **Python** | Bundled with Blender 5.2 |
| **Storage** | ~50 GB free |

---

## Software

| Software | Path | Purpose |
|----------|------|---------|
| **Blender 5.2** | `~/App/blender-5.2.0-linux-x64/blender` | Main 3D app |
| **Blender MCP** | `~/mcp-arwaky/blender-arwaky/` | Agent-Blender bridge |
| **FFmpeg** | System PATH | PNG → MP4 encode |

---

## Blender Add-ons

| Add-on | Purpose |
|--------|---------|
| **LoopTools** | Modeling — hoodie topology |
| **Bool Tool** | Boolean ops — pocket/zipper |
| **Node Wrangler** | Shader shortcuts — PBR setup |
| **3D View: Pie Menu** | Quick access |
| **Mesh: Edit Mesh Tools** | Extra modeling ops |
| **Animation: Add Camera Rigs** | Camera rig presets |
| **Import-Export: Import Images as Planes** | BG plate import |
| **Import-Export: FBX format** | Asset exchange |
| **Import-Export: Alembic format** | ABC import |
| **Mesh: 3D-Print Toolbox** | Mesh inspection |

Add-on dir: `~/.config/blender/5.2/extensions/user_default/`

---

## Assets

### Character (`male_1`)

| Asset | Format | Status |
|-------|--------|--------|
| Body model | .blend / .abc | ⬜ Pending |
| Hoodie model | .blend | ⬜ Pending |
| Pants model | .blend | ⬜ Pending |
| Footwear | .blend | ⬜ Pending |
| Animation | .abc | ⬜ Pending |

### PBR Textures

| Asset | Maps | Resolution |
|-------|------|------------|
| Hoodie | Diffuse, Normal, Roughness, Metalness, AO, Displacement | 4096×4096 |
| Pants | Diffuse, Normal, Roughness | 2048×2048 |
| Skin | Diffuse, Normal | 2048×2048 |

### Environment

| Asset | Method | Status |
|-------|--------|--------|
| Pine trees | Array/duplicate trunks | ⬜ Pending |
| Ground plane | Displacement + procedural | ⬜ Pending |
| Volumetric fog | Volume Scatter shader | ⬜ Pending |

---

## Scene

| Spec | Value |
|------|-------|
| Resolution | 1080×1920 (9:16 portrait) |
| Frame Rate | 30 fps |
| Duration | 750 frames (25 seconds) |
| Cameras | 8 (CAM_S01 – CAM_S08) |
| Character | 1 (male_1) |

---

## Render

### Cycles (Final)

| Setting | Value |
|---------|-------|
| Engine | Cycles |
| Device | GPU Compute (HIP ROCm) |
| Resolution | 1080×1920, 100% |
| Samples | 512 |
| Denoising | OpenImageDenoise (auto) |
| Light Paths | Max bounces 8 (diffuse/glossy), 4 (transmission) |
| Film | Transparent |
| Tile size | 256×256 |
| Adaptive Sampling | ON, threshold 0.01 |
| Viewport denoise | ON |

#### Volumetric Fog Notes
- Volume scatter = 2-4x render time per frame
- Adaptive sampling aggressively
- Test at 128 samples before 512

### Eevee (Preview)

| Setting | Value |
|---------|-------|
| Engine | Eevee |
| Resolution | 1080×1920, 100% |
| Samples | 64 max |
| AO | ON, distance 5m, factor 1.0 |
| Shadows | High resolution, soft |
| Bloom | OFF |
| Motion Blur | OFF |
| Volumetrics | ON |

### Compositing

```
[Render Layers]──[Alpha Over]──[Color Grade]──[Output]
      |                 ↑
      |    [BG Image Plate]
      |
      └──[Glare]──[Mist]
```

### Color Grading
- **Shadows:** Cool blue-grey
- **Midtones:** Neutral, slight desaturation
- **Highlights:** Warm skin tone preservation
- **Contrast:** Medium-high
- **Saturation:** Slightly reduced

### Color Management

| Setting | Value |
|---------|-------|
| View Transform | Filmic (ACES) — Medium High Contrast |
| Display | sRGB |
| Output | Rec.709 |

### Encoding

```bash
# Final
ffmpeg -framerate 30 -i renders/frames/%04d.png \
  -c:v libx264 -preset medium -crf 18 \
  -pix_fmt yuv420p renders/final/hoodie_1080x1920_30fps.mp4

# Web
ffmpeg -framerate 30 -i renders/frames/%04d.png \
  -c:v libx264 -preset slow -crf 22 \
  -pix_fmt yuv420p renders/final/hoodie_web.mp4
```

### Output Formats

| Format | Specs |
|--------|-------|
| PNG sequence | 16-bit RGBA — `renders/frames/%04d.png` |
| MP4 H.264 | CRF 18, yuv420p, 30fps, 1080×1920 |
| EXR (optional) | 32-bit float |

### Quality Targets

| Metric | Target |
|--------|--------|
| File size | <500 MB |
| Bitrate | 20–30 Mbps |
| Banding | None |
| Fireflies | None (denoised) |
| Fog quality | Smooth, no stepping |
| Skin tone | Natural, warm |
| Fabric texture | Visible weave in CU shots |

---

## Pipeline Rules

| Rule | Detail |
|------|--------|
| **Blender only** | No ComfyUI, no SDXL, no external apps |
| **Animation in ABC** | No manual keyframes — import .abc, Cache Playback |
| **Blender binary** | `~/App/blender-5.2.0-linux-x64/blender` only |
| **HIP ROCm** | GPU render — not CUDA, not OptiX |
| **Version scenes** | `hoodie_v01.blend`, `hoodie_v02.blend`, etc. |

---

## Performance

| Metric | Target |
|--------|--------|
| Polycount (character) | <100k |
| Polycount (environment) | <200k |
| Texture memory | <8 GB VRAM |
| Single frame (Cycles 512s) | <120s |
| Full render (750 frames) | <10 hours |
| Final MP4 | <500 MB |

# Production Pipeline & Quality Checklist — "Silent Summit" Hoodie Forest Scene

**Created:** 2026-07-17
**Scope:** 1 character (male model) in misty pine forest. Animation embedded in Alembic (.abc) — no rigging or manual keyframing required. Blender-only pipeline.

---

## 1. Pipeline & Workflow Overview

```
[PHASE 1] Character Asset Creation
   └─ male_1 — MB-Lab body + hoodie modeling + PBR textures

[PHASE 2] Animation (Walk + Reveal + Power Pose)
   └─ Bake animation into Alembic (.abc) — no Blender keyframes needed

[PHASE 3] Blender Scene Integration
   ├─ Import ABC ► Scene Layout ► Lighting & Environment
   ├─ Volumetric fog + pine forest geometry
   └─ Render (Cycles GPU HIP ROCm)

[PHASE 4] Final Delivery
   ├─ PNG sequence renders
   ├─ FFmpeg MP4 encode (9:16, 30fps)
   └─ Package assembly
```

---

## 2. Phase Gates Overview

| Gate | Status | Description |
|:-----|:-------|:------------|
| **0 — Pre-production** | ✅ PASSED | Concept, scenario, shot list, references locked |
| **1 — Character Asset** | ⬜ PENDING | Build male model, model hoodie, create PBR textures |
| **2 — Animation** | ⬜ PENDING | Walk cycle, reveal sequence, power pose — bake to ABC |
| **3 — Scene Layout** | ⬜ PENDING | Import ABC, forest environment, camera lock |
| **4 — Lighting & Fog** | ⬜ PENDING | Volumetric fog, dramatic lighting, rim lights |
| **5 — Rendering** | ⬜ PENDING | Cycles final render, MP4 encode |

> **No Phase Skipping:** Each gate must be approved before proceeding.

---

## 3. Gate Details & Exit Criteria

### Gate 0 — Pre-production ✅ PASSED

- [X] **Concept locked:** Luxury hoodie dramatic reveal in misty pine forest
- [X] **Shot list:** 8 shots, 750 frames, 25 seconds
- [X] **Technical specs:** 1080×1920, 30fps, Cycles HIP ROCm
- [X] **Mood board:** Moody, dramatic, low-key lighting

---

### Gate 1 — Character Asset ⬜ PENDING

**Description:** Create the male model and luxury hoodie with full PBR materials.

#### Checklist

- [ ] **Body model:** Build male model in MB-Lab or manual sculpt (athletic, 180-185cm)
- [ ] **Hoodie model:** Oversized luxury hoodie — drop shoulder, kangaroo pocket, ribbed cuffs/hem, metal zipper
- [ ] **Pants model:** Dark tapered pants — slim fit, clean silhouette
- [ ] **Footwear:** Black premium sneakers or boots
- [ ] **UV unwrap:** Clean UVs for all garments — minimal stretching
- [ ] **PBR textures:** Create full texture set per garment:
  - Diffuse / Base Color
  - Normal Map
  - Roughness
  - Metalness (zipper/hardware only)
  - Ambient Occlusion
  - Displacement (optional)
- [ ] **Material setup:** Principled BSDF nodes connected, roughness values tuned:
  - Hoodie fabric: roughness ~0.7-0.8, no metalness
  - Metal zipper: roughness ~0.2, metalness ~0.9
  - Skin: SSS enabled, roughness ~0.3-0.5
  - Pants: roughness ~0.6
- [ ] **Polycount check:** Character mesh <100k polygons

#### Exit Criteria
- Male model with hoodie visible in viewport
- All PBR textures assigned and rendering correctly in Eevee preview
- No visual artifacts (UV seams, stretching, material errors)

---

### Gate 2 — Animation ⬜ PENDING

**Description:** Create walk, reveal, and power pose animations — bake to Alembic.

#### Animation Sequence

| Beat | Action | Frames | Duration |
|:-----|:-------|:-------|:---------|
| Walk | Slow confident walk through fog | 001-220 | 7.3s |
| Stop/Turn | Stops, turns toward camera | 221-320 | 3.3s |
| Hood Reveal | Raises/adjusts hood — hero moment | 321-420 | 3.3s |
| Detail Poses | Subtle fabric-touch gestures | 421-590 | 5.7s |
| Power Pose | Stands tall, hood up, dominant | 591-670 | 2.7s |
| Hold/Fade | Holds final pose | 671-750 | 2.7s |

#### Checklist

- [ ] **Walk cycle:** Smooth, confident stride — no urgency
- [ ] **Stop/turn:** Natural deceleration, subtle body shift
- [ ] **Hood adjustment:** Arm raises to hood, pulls it up — deliberate, premium feel
- [ ] **Detail gestures:** Hands brush fabric, check cuffs — subtle product interaction
- [ ] **Power pose:** Shoulders back, chin up, dominant stance
- [ ] **Bake to ABC:** Export all animation as `male_1.abc` — verify playback in Blender
- [ ] **No manual keyframes:** Everything in ABC — only Cache Playback in Blender

#### Exit Criteria
- Animation plays smoothly in Blender viewport (Eevee preview)
- ABC file loads without error
- Frame range matches SCENARIO.md (750 frames)

---

### Gate 3 — Scene Layout ⬜ PENDING

**Description:** Import ABC, set up forest environment, position model, lock cameras.

#### Checklist

- [ ] **ABC import:** Import `male_1.abc` into Blender scene — verify animation playback
- [ ] **Material reconnect:** Attach PBR textures to Principled BSDF (Alembic doesn't carry materials)
- [ ] **Scale check:** Verify real-world scale — model should be ~180cm tall
- [ ] **Forest geometry:**
  - Pine tree trunks (array/duplicate along path)
  - Ground plane with displacement (pine needles, moss)
  - Fallen logs, rocks (optional)
- [ ] **Camera setup:** Create 8 cameras per SCENARIO.md:
  - `CAM_S01` through `CAM_S08`
  - Position and keyframe per shot list
  - Track-To constraints on TARGET_* empties
- [ ] **Timeline:** Set frame range to 1-750

#### Exit Criteria
- All 8 cameras positioned and animated
- Model visible and animated in all camera views
- Forest geometry blocking complete

---

### Gate 4 — Lighting & Fog ⬜ PENDING

**Description:** Dramatic moody lighting with volumetric fog — the atmosphere sells the luxury feel.

#### Checklist

- [ ] **Volumetric fog:** Domain object with Volume Scatter shader
  - Density: 0.02-0.05 (adjustable)
  - Color: slight cool blue-grey tint
  - Anisotropy: 0.7 (forward scattering)
- [ ] **Key light:** Single dramatic side light
  - Warm or cool depending on shot
  - Low angle for dramatic shadows
- [ ] **Rim light:** Edge separation from dark background
  - Catches hood edge, shoulders, fabric texture
- [ ] **Fill light:** Subtle ambient from HDRI (overcast sky)
- [ ] **Ground bounce:** Soft reflection from forest floor
- [ ] **Light animation:** Key light intensity shifts per shot (reveal = brighter)
- [ ] **Shadow settings:** Soft shadows, contact shadows enabled

#### Exit Criteria
- Fog visible and atmospheric in Eevee preview
- Dramatic lighting visible — moody, not flat
- Rim light separates model from background

---

### Gate 5 — Rendering ⬜ PENDING

**Description:** Final high-quality Cycles render, MP4 encode, delivery package.

#### Checklist

- [ ] **Test render:** 50-frame sequence at 256 samples — user review
- [ ] **Quality check:** No fireflies, banding, or artifacts
- [ ] **Full render:** 750 frames at 512 samples
- [ ] **FFmpeg encode:**
  ```bash
  ffmpeg -framerate 30 -i renders/frames/%04d.png \
    -c:v libx264 -preset medium -crf 18 \
    -pix_fmt yuv420p renders/final/hoodie_1080x1920_30fps.mp4
  ```
- [ ] **QA:** Verify 30fps playback, no compression artifacts
- [ ] **Package:** Scene file + renders + documentation

#### Exit Criteria
- Final MP4 delivered at `renders/final/hoodie_1080x1920_30fps.mp4`
- File size <500 MB
- No visual issues

---

## 4. Dependency Flow

```
[Gate 0] Pre-production ✅
    │
    ▼
[Gate 1] Character Asset — create model + textures
    │
    ▼
[Gate 2] Animation — walk/reveal/pose → ABC export
    │
    ▼
[Gate 3] Scene Layout — import ABC, forest, cameras
    │
    ▼
[Gate 4] Lighting & Fog — dramatic atmosphere
    │
    ▼
[Gate 5] Rendering — Cycles final → MP4
```

---

## 5. Risk Register

| Risk | Impact | Mitigation |
|:-----|:-------|:-----------|
| Hoodie fabric looks flat | High | Use high-res normal maps + displacement; test in Cycles early |
| Fog too thick/thin | Medium | Adjust density per shot; use volume Scatter node controls |
| Render times excessive (Cycles + fog) | High | Use Eevee for preview; lower samples for test renders |
| ABC animation mismatch | Medium | Verify frame range immediately after import |
| Model looks plastic | Medium | Tune SSS on skin, roughness on fabric; avoid pure black |
| Low contrast in moody lighting | Medium | Ensure rim light is strong enough; check histogram |

---

## 6. Decision Log

- [X] **Pipeline:** Blender only — no external apps
- [X] **Character count:** 1 (male model)
- [X] **Duration:** 25 seconds / 750 frames
- [X] **Environment:** Misty pine forest
- [X] **Mood:** Moody, dramatic, premium
- [X] **Product:** Luxury hoodie (oversized, heavyweight)
- [X] **Animation method:** Baked in Alembic — no manual keyframes in Blender

---

## 7. Render Specifications

### Output Formats

| Format | Specs |
|--------|-------|
| PNG sequence | 16-bit RGBA, lossless — `renders/frames/%04d.png` |
| MP4 H.264 | CRF 18–20, yuv420p, 30fps, 1080×1920 |
| EXR (optional) | 32-bit float, for Cycles HDR compositing if needed |

### GPU: AMD Radeon RX 6800 XT (16 GB VRAM)

- **Render Device:** Cycles → GPU Compute → HIP ROCm
- **VRAM available:** ~16 GB — handles volumetric fog + character without tiling

### Cycles Settings (Final Quality)

| Setting | Value |
|---------|-------|
| Render Engine | Cycles |
| Device | GPU Compute (HIP ROCm) |
| Resolution | 1080×1920, 100% |
| Samples | 512 |
| Denoising | OpenImageDenoise (auto) |
| Light Paths | Max bounces 8 (diffuse/glossy), 4 (transmission) |
| Film | Transparent (for compositing with BG plate) |
| Tile size | 256×256 (optimal for HIP ROCm) |
| Adaptive Sampling | ON, noise threshold 0.01 |
| Viewport denoise | ON for faster iteration |

#### Volumetric Fog Render Notes
- Volume scatter adds significant render time — expect 2-4x longer per frame
- Use **adaptive sampling** aggressively — fog areas are noisy but low-detail
- Test fog density at 128 samples before committing to 512

### Eevee Settings (Draft / Preview)

| Setting | Value |
|---------|-------|
| Render Engine | Eevee |
| Resolution | 1080×1920, 100% |
| Samples | 64 max |
| Ambient Occlusion | ON, distance 5m, factor 1.0 |
| Shadows | High resolution, soft |
| Bloom | OFF (add in compositor if needed) |
| Motion Blur | OFF |
| Volumetrics | ON (for fog preview — lower quality than Cycles) |

### Compositing Node Setup

```
[Render Layers]──[Alpha Over]──[Color Grade]──[Output]
      |                 ↑
      |    [BG Image Plate] (if using forest photo backdrop)
      |
      └──[Glare]──[Mist]
```

#### Color Grading Notes
- **Shadows:** Cool blue-grey (forest atmosphere)
- **Midtones:** Neutral, slight desaturation
- **Highlights:** Warm skin tone preservation
- **Contrast:** Medium-high — moody, not flat
- **Saturation:** Slightly reduced overall — premium feel

### Encoding

```bash
# Final MP4 — high quality
ffmpeg -framerate 30 -i renders/frames/%04d.png \
  -c:v libx264 -preset medium -crf 18 \
  -pix_fmt yuv420p renders/final/hoodie_1080x1920_30fps.mp4

# Web-optimized variant
ffmpeg -framerate 30 -i renders/frames/%04d.png \
  -c:v libx264 -preset slow -crf 22 \
  -pix_fmt yuv420p renders/final/hoodie_web.mp4
```

### Color Management

| Setting | Value |
|---------|-------|
| View Transform | Filmic (ACES) — Medium High Contrast |
| Look | None (custom grading in compositor) |
| Display | sRGB |
| Output | Rec.709 |

### Quality Targets

| Metric | Target |
|--------|--------|
| File size | <500 MB |
| Bitrate | 20–30 Mbps |
| Banding | None visible |
| Fireflies | None (denoised) |
| Fog quality | Smooth, no stepping artifacts |
| Skin tone | Natural, warm, not orange |
| Fabric texture | Visible weave/detail in CU shots |

---

## 8. Troubleshooting

### Blender MCP Not Responding

**Symptom:** `mcp_blender_mcp_get_scene_info` times out or is unreachable

**Fix:**
1. Make sure Blender is open with the Blender MCP plugin active
2. Edit > Preferences > Add-ons > search "blender-mcp" > enable
3. Restart Blender and the agent
4. Check port: default is 8080
5. Use correct binary: `~/App/blender-5.2.0-linux-x64/blender` or `./Blender/blender`

### Cycles GPU Compute Error (HIP ROCm)

**Symptom:** "No compatible GPU found" or "HIP error"

**Fix:**
1. Edit > Preferences > System > Cycles Render Devices
2. Select **HIP ROCm** (not CUDA or OptiX)
3. Verify: should show "AMD Radeon RX 6800 XT"
4. Check driver: `rocminfo` or `hipconfig` in terminal
5. Fallback: CPU render or switch to Eevee

### Volumetric Fog Too Heavy / Too Thin

**Symptom:** Fog obscures model or is invisible

**Fix:**
1. Select fog domain object → Material Properties
2. Adjust Volume Scatter **Density**:
   - Too thick: lower from 0.05 → 0.02
   - Too thin: raise from 0.02 → 0.04
3. Adjust **Anisotropy**: 0.7 = forward scatter (good for dramatic fog)
4. Check fog domain bounds — must encompass entire scene
5. For Eevee preview: enable Volumetrics in Render Properties

### Fog Renders Noisy / Grainy

**Symptom:** Volume scatter produces heavy noise in Cycles

**Fix:**
1. Increase samples (256 → 512) — fog needs more samples than surfaces
2. Enable **Adaptive Sampling** with lower threshold (0.01 → 0.005)
3. Use **Clamp Indirect** to reduce fireflies from volume bounces
4. In Compositor: add subtle denoising pass for volume specifically
5. Reduce light bounces if not critical (8 → 4)

### Render Is Extremely Slow

**Symptom:** 1 frame takes >60s, total render time prohibitive

**Fix:**
1. Volumetric fog is the main culprit — it multiplies render time 2-4x
2. Switch to Eevee for layout/animation preview
3. Reduce samples: 128 for test renders, 256 for quality checks
4. Disable motion blur if not needed
5. Simplify fog: lower density, reduce domain size
6. Render in background: `blender -b file.blend -a`

### Hoodie Fabric Looks Flat / Plastic

**Symptom:** Hoodie material lacks texture depth

**Fix:**
1. Connect **Normal Map** to Principled BSDF Normal input
2. Increase normal map strength (0.5 → 1.0)
3. Add **Displacement** node for micro-surface detail
4. Set roughness to 0.7-0.8 (not too smooth)
5. Ensure UV unwrap is clean — no stretching
6. Use high-res textures (2048x2048 minimum for CU shots)

### ABC Animation Mismatch

**Symptom:** Animation doesn't play or frame range is wrong

**Fix:**
1. Import ABC via File > Import > Alembic
2. Check timeline: set frame range to 1-750
3. Select ABC object → Object Properties > Animation
4. Ensure Cache Playback is enabled
5. Verify frame count matches SCENARIO.md
6. If animation is offset: adjust start frame in ABC import settings

### Model Looks Plastic (Skin)

**Symptom:** Skin appears waxy or unrealistic

**Fix:**
1. Enable **Subsurface Scattering (SSS)** on skin material
2. Set SSS color to warm red/orange (not pure white)
3. SSS radius: 1.0-2.0mm for realistic skin
4. Roughness: 0.3-0.5 (not too smooth)
5. Add subtle **Subsurface** randomization
6. In Cycles: increase SSS bounces if needed

### Shadow Acne (Speckles on Surfaces)

**Symptom:** Fine noise pattern on surfaces near contact areas

**Fix:**
1. Increase shadow bias (0.05–0.1)
2. Enable contact shadows (Eevee: Contact Shadows ON, distance 0.1m)
3. For Cycles: increase light sample count
4. Use shadow catcher for ground contact

### Color Banding in Fog Gradient

**Symptom:** Fog shows visible stepping/banding

**Fix:**
1. Enable dithering: Render Properties > Film > Dither
2. Use 16-bit PNG output (not 8-bit)
3. In Eevee: increase volumetric samples
4. Add subtle film grain in Compositor

### Hair Cards Cause Performance Drop

**Symptom:** Viewport lag with hair visible

**Fix:**
1. Reduce card count: 2000-3000 cards sufficient
2. Use LOD: simplify distant cards
3. In viewport: set hair to bounding box mode
4. Parent hair to empty first, then to head bone

### Emergency Workarounds

| Problem | Temporary Fix |
|---------|---------------|
| MCP down | Continue via Blender UI manually, log in NOTES.md |
| GPU out of memory | Render in tiles or switch to CPU |
| Fog too heavy for viewport | Hide fog domain in viewport, show only in render |
| Alembic playback slow | Disable modifiers on ABC object, check disk speed |
| Texture memory high | Reduce resolution to 1024, use UDIM tiles |

### How to Use This Guide

1. Identify the symptom in the section heading
2. Apply fixes in order (first listed = most common cause)
3. Re-test after each fix
4. If unresolved, add entry to `scenes/NOTES.md` with:
   - What was tried
   - Blender version
   - GPU/CPU specs
   - Error messages (from Blender console)

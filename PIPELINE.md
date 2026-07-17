# Pipeline — "Silent Summit" Hoodie Forest Scene

---

## Workflow

```
[PHASE 1] Character Asset Creation
   └─ male_1 — MB-Lab body + hoodie modeling + PBR textures

[PHASE 2] Animation (Walk + Reveal + Power Pose)
   └─ Bake into Alembic (.abc)

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

## Dependency Flow

```
Gate 0 — Pre-production
    │
    ▼
Gate 1 — Character Asset
    │
    ▼
Gate 2 — Animation → ABC export
    │
    ▼
Gate 3 — Scene Layout
    │
    ▼
Gate 4 — Lighting & Fog
    │
    ▼
Gate 5 — Rendering → MP4
```

---

## Risk Register

| Risk | Impact | Mitigation |
|:-----|:-------|:-----------|
| Hoodie fabric looks flat | High | High-res normal maps + displacement; test in Cycles early |
| Fog too thick/thin | Medium | Adjust density per shot; volume Scatter node controls |
| Render times excessive | High | Eevee for preview; lower samples for test renders |
| ABC animation mismatch | Medium | Verify frame range immediately after import |
| Model looks plastic | Medium | Tune SSS on skin, roughness on fabric |
| Low contrast in moody lighting | Medium | Ensure rim light is strong enough; check histogram |

---

## Decision Log

- **Pipeline:** Blender only — no external apps
- **Character count:** 1 (male model)
- **Duration:** 25 seconds / 750 frames
- **Environment:** Misty pine forest
- **Mood:** Moody, dramatic, premium
- **Product:** Luxury hoodie (oversized, heavyweight)
- **Animation method:** Baked in Alembic — no manual keyframes in Blender

---

## Troubleshooting

### Blender MCP Not Responding

**Symptom:** `mcp_blender_mcp_get_scene_info` times out

**Fix:**
1. Blender open with MCP plugin active
2. Edit > Preferences > Add-ons > search "blender-mcp" > enable
3. Restart Blender and agent
4. Check port: default 9876
5. Binary: `~/App/blender-5.2.0-linux-x64/blender`

### Cycles GPU Compute Error (HIP ROCm)

**Symptom:** "No compatible GPU found" or "HIP error"

**Fix:**
1. Edit > Preferences > System > Cycles Render Devices
2. Select **HIP ROCm** (not CUDA/OptiX)
3. Verify: "AMD Radeon RX 6800 XT"
4. Check driver: `rocminfo` or `hipconfig`
5. Fallback: CPU or Eevee

### Volumetric Fog Too Heavy / Too Thin

**Fix:**
1. Select fog domain → Material Properties
2. Adjust Volume Scatter **Density**: thick → 0.02, thin → 0.04
3. **Anisotropy**: 0.7 (forward scatter)
4. Domain bounds must encompass entire scene

### Fog Renders Noisy

**Fix:**
1. Increase samples (256 → 512)
2. Adaptive Sampling threshold: 0.01 → 0.005
3. Clamp Indirect to reduce fireflies
4. Reduce light bounces (8 → 4)

### Render Is Extremely Slow

**Fix:**
1. Fog multiplies render time 2-4x — main culprit
2. Eevee for layout/animation preview
3. Samples: 128 test, 256 quality
4. Render background: `blender -b file.blend -a`

### Hoodie Fabric Looks Flat

**Fix:**
1. Connect Normal Map to Principled BSDF
2. Normal strength: 0.5 → 1.0
3. Add Displacement node
4. Roughness: 0.7-0.8
5. Clean UV unwrap, high-res textures (2048x2048 min)

### ABC Animation Mismatch

**Fix:**
1. Import via File > Import > Alembic
2. Timeline: 1-750
3. Cache Playback enabled
4. Verify frame count matches CONCEPTS.md

### Model Looks Plastic (Skin)

**Fix:**
1. Enable SSS on skin material
2. SSS color: warm red/orange
3. SSS radius: 1.0-2.0mm
4. Roughness: 0.3-0.5

### Shadow Acne

**Fix:**
1. Shadow bias: 0.05–0.1
2. Contact shadows ON (Eevee)
3. Increase light samples (Cycles)

### Color Banding in Fog

**Fix:**
1. Dithering: Render Properties > Film > Dither
2. 16-bit PNG output
3. Film grain in Compositor

### Emergency Workarounds

| Problem | Fix |
|---------|-----|
| MCP down | Manual Blender UI, log in NOTES.md |
| GPU OOM | Tiles or CPU fallback |
| Fog heavy viewport | Hide domain, show in render only |
| ABC slow | Disable modifiers, check disk speed |

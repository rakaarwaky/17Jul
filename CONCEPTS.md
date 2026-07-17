# CONCEPTS — "Silent Summit" Luxury Hoodie Showcase

**Created:** 2026-07-17

---

## Creative Brief

A single male model reveals a luxury hoodie in a misty pine forest. Moody, cinematic, and dramatic — the forest itself becomes a character. The hoodie is the hero. Every frame sells premium craftsmanship.

**Tagline:** *"Worn by silence. Made for the summit."*

---

## Visual Identity

| Attribute | Value |
|-----------|-------|
| **Product** | Luxury hoodie — premium heavyweight fabric, oversized fit, minimalist branding |
| **Color Palette** | Deep forest greens, charcoal, misty whites, warm skin tones |
| **Mood** | Moody, dramatic, mysterious, premium |
| **Lighting** | Low-key — volumetric fog, dappled light through canopy, rim light separation |
| **Texture Emphasis** | Fabric weave, hood drape, stitched seams, zipper detail, cuff ribbing |

---

## Environment

### Misty Pine Forest
- **Ground:** Pine needle carpet, mossy rocks, fallen logs
- **Trees:** Tall pine trunks, dense canopy filtering light
- **Atmosphere:** Thick volumetric fog/mist drifting through the scene
- **Ground Level:** Low-lying mist pooling around ankles
- **Sky:** Overcast, muted grey-blue visible through canopy gaps

### Props (Optional)
- Weathered wooden stump (model can lean/sit)
- Faint trail/path through the pines
- Single beam of light breaking through canopy (dramatic accent)

---

## Character

### Male Model (`male_1`)
- **Build:** Athletic, 180-185cm
- **Outfit:** Luxury hoodie (oversized, heavyweight cotton) + dark tapered pants
- **Footwear:** Premium sneakers or boots (black)
- **Expression:** Confident, subtle, mysterious — minimal emotion, maximum presence
- **Hair:** Short or styled, natural
- **Action:** Dramatic reveal — walking through mist, stopping, turning to camera, hood adjustment, final power pose

---

## Lighting Design

```
[OVERCAST SKY] ─── soft top-down ambient fill
        │
[FOG/VOLUMETRIC] ─── atmospheric depth, mystery
        │
[KEY LIGHT] ─── single warm/cool accent from side (dramatic)
        │
[RIM LIGHT] ─── edge separation from dark forest background
        │
[GROUND BOUNCE] ─── subtle moss/earth reflection
```

### Lighting Presets
1. **Fog Entry:** Low contrast, everything softened by mist
2. **Reveal Moment:** Key light intensifies as model stops and turns
3. **Detail Showcase:** Rim light catches fabric texture and hood edges
4. **Final Shot:** Dramatic low-angle with backlight silhouette

---

## Camera Language

| Shot Type | Purpose | Lens Range |
|-----------|---------|------------|
| **Extreme Wide (EWS)** | Establish forest isolation | 18-24mm |
| **Full Body (FULL)** | Walk and movement | 35-50mm |
| **Medium (MED)** | Torso + hoodie details | 50-85mm |
| **Close-Up (CU)** | Fabric texture, stitching, zipper | 85-105mm |
| **Detail (DET)** | Macro — seam, drawstring, logo | 100mm+ |

### Camera Movement Vocabulary
- **Slow dolly push-in** — tension building
- **Tracking lateral** — following walk
- **Low-angle tilt up** — power/reveal moment
- **Rack focus** — fog to model transition
- **Static with subtle drift** — breathing room

---

## Narrative Arc (25 seconds)

```
[0-5s]   MYSTERY     — Fog, forest, distant figure approaching
[5-12s]  APPROACH    — Model walks through mist, hoodie partially obscured
[12-17s] REVEAL      — Model stops, turns, hood adjustment — PRODUCT HERO
[17-22s] DETAIL      — Close-ups: fabric, stitching, fit, movement
[22-25s] POWER       — Final dramatic pose, fade to black
```

---

## Technical Specs

| Spec | Value |
|------|-------|
| Resolution | 1080×1920 (9:16 portrait) |
| Frame Rate | 30 fps |
| Duration | 25 seconds (750 frames) |
| Render Engine | Blender Cycles (HIP ROCm) |
| GPU | AMD Radeon RX 6800 XT (16 GB VRAM) |
| Output | PNG sequence → H.264 MP4 |

---

## Differentiation from Previous Project

| Aspect | Previous (Beach) | New (Forest Hoodie) |
|--------|------------------|---------------------|
| Characters | 4 (3F + 1M) | 1 (M) |
| Environment | Open beach | Dense pine forest |
| Lighting | Bright golden hour | Moody low-key |
| Mood | Fashion show, confident | Dramatic reveal, mysterious |
| Pipeline | Blender + ComfyUI SDXL | Blender only (no external apps) |
| Duration | 26.7s (800f) | 25s (750f) |
| Product | Bikini/swimwear | Luxury hoodie |

---
---

# SHOOT LIST — "Silent Summit" Luxury Hoodie Reveal

**Total:** 750 frames (25s @ 30fps) — 8 camera cuts.

---

## Production Metadata
- **Aspect Ratio:** 9:16 Portrait (1080 × 1920)
- **Frame Rate:** 30 fps
- **Total Duration:** 25 seconds (750 frames)
- **Format:** Luxury hoodie dramatic reveal — premium fashion film
- **Camera Style:** Cinematic — mix of wide atmospheric and tight detail shots
- **Main Environment:** Misty pine forest — moody, dramatic

---

## Camera Naming Convention

Each shot uses a dedicated camera: `CAM_S01` through `CAM_S08`.
All cameras use vertical sensor fit and linear camera dolly keyframes.

---

## Shot List

### S01 — Extreme Wide Establishing (Forest Fog)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S01` |
| **Frames** | `001–100` (100f) |
| **Time** | 0.0–3.3s |
| **Type** | Extreme Wide Shot (EWS) |
| **Lens** | **18mm** — Panoramic |
| **Framing** | Dense pine forest corridor, thick fog rolling through tree trunks, distant silhouetted figure barely visible deep in the mist — mystery |
| **Camera** | Slow push-in dolly through the fog corridor toward the distant figure |
| **Movement** | Steady forward dolly — 2.5m travel |
| **Focus** | Deep DOF (F/8) — fog does the softening naturally |
| **Vibe** | **MYSTERY** — who is out there? atmospheric dread |

### S02 — Full Body Walk (Approach Through Mist)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S02` |
| **Frames** | `101–220` (120f) |
| **Time** | 3.3–7.3s |
| **Type** | Full Body Shot (FULL) |
| **Lens** | **35mm** — Slightly wide |
| **Framing** | `male_1` full body walking toward camera through fog, hoodie partially zipped, hands in pockets, pine trees flanking the path |
| **Camera** | Lateral tracking dolly matching walk speed, slight parallax on foreground trees |
| **Movement** | Right-to-left lateral tracking — trees pass in foreground for depth |
| **Focus** | Mid DOF (F/4.0) — model sharp, foreground trees soft |
| **Vibe** | **APPROACH** — confident, unhurried, premium presence |

### S03 — Medium Shot (Torso Reveal)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S03` |
| **Frames** | `221–320` (100f) |
| **Time** | 7.3–10.7s |
| **Type** | Medium Shot (MED) |
| **Lens** | **50mm** — Portrait standard |
| **Framing** | `male_1` waist-up, stops walking, slight turn toward camera. Fog swirls around him. Hoodie front fully visible — heavyweight fabric, oversized fit |
| **Camera** | Slow push-in dolly from front-right angle, closing distance as he stops |
| **Movement** | Forward dolly + subtle tilt up to eye level |
| **Focus** | Mid-shallow DOF (F/2.8) — model sharp, background soft |
| **Vibe** | **TRANSITION** — from approach to reveal, tension building |

### S04 — Hood Adjustment (Hero Reveal Moment)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S04` |
| **Frames** | `321–420` (100f) |
| **Time** | 10.7–14.0s |
| **Type** | Medium Close-Up (MCU) — Hero Shot |
| **Lens** | **85mm** — Portrait cinematic |
| **Framing** | `male_1` chest-up, reaching up to adjust/raise hood. Key light catches fabric edge. Eyes visible under hood shadow. **THIS IS THE HERO FRAME** |
| **Camera** | Low-angle slight tilt up — power pose. Slow dolly push-in |
| **Movement** | Forward dolly + low-angle crane rise — model dominates frame |
| **Focus** | Shallow DOF (F/1.8) — eyes + hood sharp, forest melts away |
| **Vibe** | **REVEAL** — product hero moment, dramatic, iconic |

### S05 — Close-Up Detail (Fabric & Stitching)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S05` |
| **Frames** | `421–510` (90f) |
| **Time** | 14.0–17.0s |
| **Type** | Close-Up (CU) — Product Detail |
| **Lens** | **100mm** — Macro detail |
| **Framing** | Tight on hoodie fabric: heavyweight cotton weave, drawstring detail, hood seam, kangaroo pocket edge. Fingers grazing fabric |
| **Camera** | Slow tracking pan across fabric surface, left to right |
| **Movement** | Lateral pan — 15cm travel across the chest area |
| **Focus** | Very shallow DOF (F/1.4) — single plane sharp, everything else bokeh |
| **Vibe** | **CRAFTSMANSHIP** — texture, quality, premium material |

### S06 — Detail Shot (Zipper & Cuff)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S06` |
| **Frames** | `511–590` (80f) |
| **Time** | 17.0–19.7s |
| **Type** | Detail (DET) — Macro |
| **Lens** | **105mm** — Macro |
| **Framing** | Zipper pull close-up → hand zipping up → cut to cuff ribbing detail at wrist |
| **Camera** | Static with rack focus — zipper → cuff transition |
| **Movement** | Minimal — rack focus pull between two detail points |
| **Focus** | Very shallow DOF (F/1.4) — selective focus pull |
| **Vibe** | **DETAIL** — hardware, precision, luxury finishing |

### S07 — Full Body Power Pose (Final Stance)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S07` |
| **Frames** | `591–670` (80f) |
| **Time** | 19.7–22.3s |
| **Type** | Full Body Shot (FULL) — Power |
| **Lens** | **28mm** — Wide cinematic |
| **Framing** | `male_1` full body, standing tall in fog, hood up, hands at sides. Pine trees framing him on both sides. Ground mist at feet |
| **Camera** | Low-angle static — model towers, slight upward tilt |
| **Movement** | Static with subtle breathing drift (handheld feel) |
| **Focus** | Mid DOF (F/2.8) — model sharp, background atmospheric |
| **Vibe** | **POWER** — dominant, premium, confident final stance |

### S08 — Extreme Wide Fade Out (Forest Silhouette)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S08` |
| **Frames** | `671–750` (80f) |
| **Time** | 22.3–25.0s |
| **Type** | Extreme Wide Shot (EWS) — Finale |
| **Lens** | **24mm** — Wide panoramic |
| **Framing** | `male_1` silhouetted figure in center of forest corridor, fog engulfing, light fading — iconic final image |
| **Camera** | Slow dolly out — widening the frame, model becomes small in the vast forest |
| **Movement** | Backward dolly + slight crane rise — retreat into the mist |
| **Focus** | Deep DOF (F/8) — atmospheric |
| **Vibe** | **FADE** — mysterious, memorable, iconic exit |

---

## Frame Distribution Summary

| Shot | Camera | Type | Frames | Duration |
|:-----|:-------|:-----|:-------|:---------|
| S01 | CAM_S01 | EWS Establishing | 001–100 | 3.3s |
| S02 | CAM_S02 | FULL Walk | 101–220 | 4.0s |
| S03 | CAM_S03 | MED Torso | 221–320 | 3.3s |
| S04 | CAM_S04 | MCU Hero Reveal | 321–420 | 3.3s |
| S05 | CAM_S05 | CU Fabric Detail | 421–510 | 3.0s |
| S06 | CAM_S06 | DET Zipper/Cuff | 511–590 | 2.7s |
| S07 | CAM_S07 | FULL Power Pose | 591–670 | 2.7s |
| S08 | CAM_S08 | EWS Fade Out | 671–750 | 2.7s |

---

## Character Screen Time

| Character | Total Frames | Percentage | Shots Featured |
|:----------|:-------------|:-----------|:---------------|
| `male_1` | 750f | 100% | S01–S08 (all shots) |

---

## Narrative Beat Map

```
[0-3.3s]   S01  MYSTERY    — Fog, forest, distant figure
[3.3-7.3s] S02  APPROACH   — Walking through mist
[7.3-10.7s] S03 TRANSITION — Stops, turns, hoodie visible
[10.7-14s] S04  REVEAL     — Hood adjustment — HERO MOMENT
[14-17s]   S05  DETAIL     — Fabric texture showcase
[17-19.7s] S06  CRAFT      — Zipper, cuff, hardware
[19.7-22.3s] S07 POWER    — Final power stance
[22.3-25s] S08  FADE       — Silhouette in mist — end
```

---

## Camera Technical Notes

- **Sensor:** Full frame 36×24mm, sensor fit = VERTICAL (for 9:16 portrait)
- **Forest atmosphere:** Volumetric fog in all shots — thick at ground level, thinner at canopy
- **Lighting:** Low-key throughout — single dramatic key light shifts position per shot
- **Color grade:** Desaturated greens, cool shadows, warm skin tones preserved
- **All cameras use Track-To constraints** pointing at TARGET_* empties
- Camera animation keyframed with LINEAR interpolation by default

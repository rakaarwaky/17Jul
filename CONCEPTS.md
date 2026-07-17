# CONCEPTS — "Silent Summit" Luxury Hoodie Showcase

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

### Hoodie Design Specs
- **Fit:** Oversized, drop shoulder
- **Fabric:** Heavyweight cotton (350+ GSM)
- **Features:** Kangaroo pocket, ribbed cuffs/hem, metal zipper (optional), drawstring hood
- **Color:** Charcoal/dark grey (primary), with subtle texture variation
- **Branding:** Minimal — small embossed logo on chest or sleeve (if any)

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

## Narrative Arc

```
[0-5s]   MYSTERY     — Fog, forest, distant figure approaching
[5-12s]  APPROACH    — Model walks through mist, hoodie partially obscured
[12-17s] REVEAL      — Model stops, turns, hood adjustment — PRODUCT HERO
[17-22s] DETAIL      — Close-ups: fabric, stitching, fit, movement
[22-25s] POWER       — Final dramatic pose, fade to black
```

---

## Differentiation from Previous Project

| Aspect | Previous (Beach) | New (Forest Hoodie) |
|--------|------------------|---------------------|
| Characters | 4 (3F + 1M) | 1 (M) |
| Environment | Open beach | Dense pine forest |
| Lighting | Bright golden hour | Moody low-key |
| Mood | Fashion show, confident | Dramatic reveal, mysterious |
| Pipeline | Blender + ComfyUI SDXL | Blender only |
| Duration | 26.7s (800f) | 25s (750f) |
| Product | Bikini/swimwear | Luxury hoodie |

---

# SHOOT LIST

**8 camera cuts, 750 frames (25s @ 30fps)**

---

## Camera Naming

`CAM_S01` through `CAM_S08` — vertical sensor fit, linear keyframes.

---

## Shot List

### S01 — Extreme Wide Establishing (Forest Fog)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S01` |
| **Frames** | `001–100` (100f / 3.3s) |
| **Type** | EWS |
| **Lens** | **18mm** — Panoramic |
| **Framing** | Dense pine forest corridor, thick fog, distant silhouetted figure barely visible |
| **Movement** | Slow push-in dolly — 2.5m travel |
| **Focus** | Deep DOF (F/8) |
| **Vibe** | **MYSTERY** — atmospheric dread |

### S02 — Full Body Walk (Approach Through Mist)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S02` |
| **Frames** | `101–220` (120f / 4.0s) |
| **Type** | FULL |
| **Lens** | **35mm** — Slightly wide |
| **Framing** | `male_1` full body walking toward camera, hoodie partially zipped, hands in pockets |
| **Movement** | Lateral tracking dolly — trees pass in foreground for parallax |
| **Focus** | Mid DOF (F/4.0) |
| **Vibe** | **APPROACH** — confident, unhurried |

### S03 — Medium Shot (Torso Reveal)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S03` |
| **Frames** | `221–320` (100f / 3.3s) |
| **Type** | MED |
| **Lens** | **50mm** — Portrait standard |
| **Framing** | `male_1` waist-up, stops walking, slight turn. Hoodie front fully visible |
| **Movement** | Forward dolly + subtle tilt up to eye level |
| **Focus** | Mid-shallow DOF (F/2.8) |
| **Vibe** | **TRANSITION** — tension building |

### S04 — Hood Adjustment (Hero Reveal Moment)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S04` |
| **Frames** | `321–420` (100f / 3.3s) |
| **Type** | MCU — Hero Shot |
| **Lens** | **85mm** — Portrait cinematic |
| **Framing** | `male_1` chest-up, reaching to adjust hood. Key light catches fabric. Eyes under hood shadow. **HERO FRAME** |
| **Movement** | Forward dolly + low-angle crane rise |
| **Focus** | Shallow DOF (F/1.8) |
| **Vibe** | **REVEAL** — product hero, dramatic, iconic |

### S05 — Close-Up Detail (Fabric & Stitching)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S05` |
| **Frames** | `421–510` (90f / 3.0s) |
| **Type** | CU — Product Detail |
| **Lens** | **100mm** — Macro |
| **Framing** | Tight on hoodie fabric: cotton weave, drawstring, hood seam, kangaroo pocket |
| **Movement** | Lateral pan — 15cm across chest |
| **Focus** | Very shallow DOF (F/1.4) |
| **Vibe** | **CRAFTSMANSHIP** — texture, quality |

### S06 — Detail Shot (Zipper & Cuff)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S06` |
| **Frames** | `511–590` (80f / 2.7s) |
| **Type** | DET — Macro |
| **Lens** | **105mm** — Macro |
| **Framing** | Zipper pull close-up → hand zipping → cuff ribbing at wrist |
| **Movement** | Rack focus pull between two detail points |
| **Focus** | Very shallow DOF (F/1.4) |
| **Vibe** | **DETAIL** — hardware, precision |

### S07 — Full Body Power Pose (Final Stance)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S07` |
| **Frames** | `591–670` (80f / 2.7s) |
| **Type** | FULL — Power |
| **Lens** | **28mm** — Wide cinematic |
| **Framing** | `male_1` full body, hood up, hands at sides. Trees framing. Ground mist at feet |
| **Movement** | Static with subtle breathing drift |
| **Focus** | Mid DOF (F/2.8) |
| **Vibe** | **POWER** — dominant, confident |

### S08 — Extreme Wide Fade Out (Forest Silhouette)

| Field | Value |
|:------|:------|
| **Camera** | `CAM_S08` |
| **Frames** | `671–750` (80f / 2.7s) |
| **Type** | EWS — Finale |
| **Lens** | **24mm** — Wide panoramic |
| **Framing** | `male_1` silhouetted in forest corridor, fog engulfing, light fading |
| **Movement** | Backward dolly + crane rise — retreat into mist |
| **Focus** | Deep DOF (F/8) |
| **Vibe** | **FADE** — mysterious, iconic exit |

---

## Frame Distribution

| Shot | Camera | Type | Frames | Duration |
|:-----|:-------|:-----|:-------|:---------|
| S01 | CAM_S01 | EWS | 001–100 | 3.3s |
| S02 | CAM_S02 | FULL | 101–220 | 4.0s |
| S03 | CAM_S03 | MED | 221–320 | 3.3s |
| S04 | CAM_S04 | MCU | 321–420 | 3.3s |
| S05 | CAM_S05 | CU | 421–510 | 3.0s |
| S06 | CAM_S06 | DET | 511–590 | 2.7s |
| S07 | CAM_S07 | FULL | 591–670 | 2.7s |
| S08 | CAM_S08 | EWS | 671–750 | 2.7s |

---

## Beat Map

```
[0-3.3s]    S01  MYSTERY    — Fog, forest, distant figure
[3.3-7.3s]  S02  APPROACH   — Walking through mist
[7.3-10.7s] S03  TRANSITION — Stops, turns, hoodie visible
[10.7-14s]  S04  REVEAL     — Hood adjustment — HERO MOMENT
[14-17s]    S05  DETAIL     — Fabric texture showcase
[17-19.7s]  S06  CRAFT      — Zipper, cuff, hardware
[19.7-22.3s] S07 POWER     — Final power stance
[22.3-25s]  S08  FADE       — Silhouette in mist — end
```

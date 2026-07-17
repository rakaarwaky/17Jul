# MPFB2: Plugin Gratis & Open Source untuk Procedural Character Creation di Blender

> Generated 2026-07-17 · depth: standard · workspace: research/blender-character-plugins/

## Executive Summary

- **MPFB2** (MakeHuman for Blender 2) adalah tool gratis & open source **satu-satunya** yang terlengkap untuk pembuatan karakter manusia realistis secara procedural di Blender
- Mencakup **seluruh pipeline** dalam satu addon: body generation, rigging, skin materials, dan animation
- Berjalan **sepenuhnya di dalam Blender 4.2+** — tidak perlu aplikasi eksternal
- **551 GitHub stars, 1,118 commits**, aktif dikembangkan hingga Juni 2026
- **Batch generation & randomization** untuk produksi mass karakter

## Apa itu MPFB2?

MPFB2 (MakeHuman for Blender 2) adalah generator karakter manusia parametric yang berjalan sepenuhnya di dalam Blender. Tool ini menggantikan pipeline lama yang memerlukan MakeHuman sebagai aplikasi terpisah.

```
GitHub: https://github.com/makehumancommunity/mpfb2
Website: https://static.makehumancommunity.org/mpfb.html
Stars: 551 | Commits: 1,118 | Latest: v2.0.16 (June 2026)
Requires: Blender 4.2+
License: AGPL-3.0
```

## Fitur Utama

### 1. Parametric Body Generation
- **Morph slider system** untuk mengubah proporsi tubuh secara parametric
- **Topological transfer** dari MakeHuman assets
- **Asset library** dengan dozens of downloadable packs:
  - Clothes (dress, pants, shoes, underwear)
  - Hair
  - Body parts
  - Skins
  - Accessories

### 2. Procedural Skin Materials
Tiga jenis material skin yang tersedia:

| Material | Deskripsi |
|----------|-----------|
| **MakeSkin** | Plain/standard diffuse texture |
| **Skin Model v1** | Procedural bumps & structure di atas diffuse |
| **Eye Model v1** | Fully procedural, tanpa image textures |

### 3. Auto-Rigging
Empat jenis rig pilihan:

1. **Default** — Rig standar untuk Blender
2. **GameEngine** — Rig untuk game engine
3. **CMU MB** — Rig dari CMU Motion Base
4. **Mixamo** — Rig untuk Mixamo animasi

Plus **Rigify integration** dengan satu tombol yang menangani extras yang tidak ditangani Rigify standar.

### 4. Animation Support
- **Mixamo integration** untuk animasi
- **Pose library** untuk menyimpan dan memuat pose
- **Lip sync** support

### 5. Batch Generation & Randomization
- **Randomizing phenotype** — variasi bentuk tubuh
- **Randomizing skin** — variasi tekstur kulit
- **Randomizing body parts** — variasi anggota tubuh
- **Randomizing clothes** — variasi pakaian
- **Batch generation** — produksi mass karakter

## Workflow

### Single Character
```
Create Character → Load Skin → Add Clothes/Bodyparts → Add Rig → Generate Rig
```

### Batch Production
```
Set Randomization Parameters → Batch Generate → Export
```

### Mixamo Integration
1. Create "reduced doll" (strip assets, bake shapekeys, remove helpers)
2. Export FBX ke Mixamo
3. Download animation
4. Snap animation back ke character

## Komunitas & Status Pengembangan

| Metric | Value |
|--------|-------|
| GitHub Stars | 551 |
| Commits | 1,118 |
| Latest Release | v2.0.16 (June 13, 2026) |
| Blender Compatibility | 4.2+ |
| License | AGPL-3.0 |
| Status | Active |

## Instalasi

1. Download dari GitHub: https://github.com/makehumancommunity/mpfb2
2. Buka Blender 4.2+
3. Edit → Preferences → Add-ons → Install from Disk
4. Pilih file ZIP yang didownload
5. Enable add-on "MakeHuman Community: MPFB"

## Referensi

[1] MPFB2 Overview — https://static.makehumancommunity.org/mpfb/about.html
[2] MPFB2 GitHub — https://github.com/makehumancommunity/mpfb2
[3] MPFB2 Documentation — https://static.makehumancommunity.org/mpfb.html
[4] MPFB2 Rigging — https://static.makehumancommunity.org/mpfb/docs/rigging_posing/rigify.html
[5] MPFB2 Materials — https://static.makehumancommunity.org/mpfb/docs/materials/overview.html
[6] MPFB2 Mixamo — https://static.makehumancommunity.org/mpfb/docs/rigging_posing/mixamo.html

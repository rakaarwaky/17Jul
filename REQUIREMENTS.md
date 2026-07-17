# Blender Plugin Requirements

> Generated 2026-07-17

## Overview

Dokumen ini berisi daftar plugin Blender yang diperlukan untuk proyek character creation dan clothing simulation.

## Daftar Plugin

### 1. MPFB2 (MakeHuman for Blender 2)

| Aspek | Detail |
|-------|--------|
| **Nama** | MPFB2 (MakeHuman for Blender 2) |
| **Fungsi** | Character creation (body, rigging, skin, animation) |
| **Tipe** | Gratis & Open Source |
| **Harga** | Gratis |
| **Blender Version** | 4.2+ |
| **License** | AGPL-3.0 |
| **Download** | https://github.com/makehumancommunity/mpfb2 |

#### Fitur Utama
- Parametric body generation dengan morph slider
- Procedural skin materials
- Auto-rigging (4 rig types + Rigify)
- Animation support (Mixamo integration)
- Batch generation & randomization

#### Instalasi
1. Download ZIP dari GitHub
2. Buka Blender 4.2+
3. Edit → Preferences → Add-ons → Install from Disk
4. Pilih file ZIP
5. Enable "MakeHuman Community: MPFB"

---

### 2. Simply Cloth

| Aspek | Detail |
|-------|--------|
| **Nama** | Simply Cloth |
| **Fungsi** | Clothing simulation & design |
| **Tipe** | Premium (Berbayar) |
| **Harga** | ~$20-40 (estimasi) |
| **Blender Version** | 3.x - 4.x |
| **License** | Commercial |
| **Download** | https://blendermarket.com/products/simply-cloth |

#### Fitur Utama
- Paint-to-cloth (gambar langsung di mesh)
- Point-to-cloth algorithm
- Real-time cloth simulation
- Workflow intuitif untuk pemula

#### Contoh Penggunaan
```
Hoodie:
1. Create base mesh
2. Paint hoodie shape
3. Add hood detail
4. Simulate & adjust

Sweatpants:
1. Create leg mesh
2. Paint sweatpants pattern
3. Add waistband
4. Simulate cloth drape
```

#### Instalasi
1. Beli di Blender Market
2. Download file .zip
3. Buka Blender → Edit → Preferences → Add-ons
4. Install from Disk → pilih file .zip
5. Enable "Simply Cloth"

---

## Workflow Integration

### Character + Clothing Pipeline

```
Step 1: MPFB2
├── Create character body
├── Add skin material
├── Add rig
└── Export/prepare mesh

Step 2: Simply Cloth
├── Paint clothing pattern
├── Add cloth simulation
├── Adjust wrinkles & folds
└── Finalize materials

Step 3: Animation
├── Use MPFB2 rig
├── Mixamo animation
└── Export final result
```

### MCP Integration

Kedua plugin **bisa dioperasikan** via blender-arwaky MCP:

```python
# MPFB2
import bpy
bpy.ops.mpfb.new_human()

# Simply Cloth
bpy.ops.simply_cloth.paint_to_cloth()
```

## Kebutuhan Sistem

### Blender
- Version: 4.2+ (untuk MPFB2)
- RAM: 8GB+ recommended
- GPU: Dedicated GPU recommended untuk cloth simulation

### Storage
- MPFB2: ~50MB (addon) + ~500MB (asset packs)
- Simply Cloth: ~20MB (addon)

## Status

| Plugin | Status | Prioritas |
|--------|--------|-----------|
| MPFB2 | ✅ Installed & Enabled | Tinggi |
| Simply Cloth | Perlu dibeli | Tinggi |

## Catatan

1. MPFB2 sudah terinstall dan enabled di Blender 5.2
2. Simply Cloth berbayar, perlu purchase dulu di Blender Market
3. Kedua plugin kompatibel dengan Blender 5.x
4. Keduanya bisa dikontrol via MCP blender-arwaky

### Instalasi MPFB2 (Blender 5.2)
- **Status:** Berhasil diinstall dan enabled
- **Lokasi:** `/home/raka/.config/blender/5.2/scripts/addons/mpfb/`
- **Patch:** locationservice.py sudah di-patch untuk kompatibilitas Blender 5.2
- **Akses:** View3D > Properties > MPFB

# Simply Cloth: Plugin Blender untuk Clothing Simulation

> Generated 2026-07-17 · depth: standard · workspace: research/blender-clothing/

## Executive Summary

- **Simply Cloth** adalah addon Blender premium untuk simulasi dan pembuatan pakaian 3D
- Dikembangkan oleh **JLAB**, menawarkan workflow intuitif untuk clothing design
- Fitur utama: **paint-to-cloth**, **point-to-cloth algorithm**, dan cloth simulation
- Cocok untuk membuat hoodie, sweatpants, dan berbagai jenis pakaian lainnya
- **Berbayar** (~$20-40 estimasi), tersedia di Blender Market

## Apa itu Simply Cloth?

Simply Cloth adalah addon Blender yang dirancang khusus untuk mempermudah pembuatan simulasi dan desain pakaian 3D. Tool ini menawarkan workflow yang intuitif dan tidak memerlukan pengetahuan mendalam tentang cloth simulation.

```
Platform: Blender Market
Developer: JLAB
Harga: ~$20-40 (estimasi)
Blender Version: 3.x - 4.x
License: Commercial
```

## Fitur Utama

### 1. Paint-to-Cloth
- **Gambar langsung** di mesh untuk membuat pakaian
- Tidak perlu manual modeling untuk bagian sederhana
- Brush tools untuk menggambar pola pakaian

### 2. Point-to-Cloth Algorithm
- **Convert points/vertices** menjadi cloth mesh
- Algoritma otomatis untuk pembuatan pakaian
- Cocok untuk pembuatan pakaian kompleks

### 3. Cloth Simulation
- **Real-time simulation** untuk preview
- Parameter yang mudah dikontrol
- Support untuk berbagai jenis kain

### 4. Workflow Intuitif
- **Step-by-step interface** yang user-friendly
- Tidak perlu setup complex cloth physics
- One-click simulation

## Contoh Penggunaan

### Membuat Hoodie
```
1. Create base mesh (cylinder/box)
2. Paint hoodie shape dengan paint-to-cloth
3. Add hood detail
4. Simulate & adjust
5. Add materials & textures
```

### Membuat Sweatpants
```
1. Create leg mesh
2. Paint sweatpants pattern
3. Add waistband
4. Simulate cloth drape
5. Adjust wrinkles & folds
```

## Perbandingan dengan Tools Lain

| Feature | Simply Cloth | Divine Cloth | Blender Built-in |
|---------|--------------|--------------|------------------|
| Paint-to-Cloth | Ya | Tidak | Tidak |
| Point-to-Cloth | Ya | Tidak | Tidak |
| Real-time Sim | Ya | Ya | Ya |
| Pre-made Assets | Terbatas | Ya | Tidak |
| Price | ~$20-40 | ~$25-50 | Gratis |
| Learning Curve | Mudah | Menengah | Sulit |

## Integrasi dengan MCP

Simply Cloth **bisa dioperasikan** via blender-arwaky MCP menggunakan `execute_blender_code`.

### Contoh Command
```python
import bpy
# Paint-to-cloth operation
bpy.ops.simply_cloth.paint_to_cloth()

# Add simulation
bpy.ops.simply_cloth.add_simulation()
```

### Catatan
- Operator names perlu dicek langsung di Blender (F3 → search)
- Tidak ada dokumentasi publik untuk API
- Perlu trial & error untuk menemukan nama operator yang benar

## Kelebihan

1. **Workflow Intuitif** - Mudah dipelajari untuk pemula
2. **Paint-to-Cloth** - Fitur unik yang tidak ada di tools lain
3. **Real-time Preview** - Langsung lihat hasil simulasi
4. **Support Berbagai Kain** - Cotton, silk, denim, dll
5. **Regular Updates** - Developer aktif memperbarui

## Kekurangan

1. **Berbayar** - Tidak gratis seperti MPFB2
2. **Limited Documentation** - Dokumentasi tidak lengkap
3. **Blender Market Only** - Tidak tersedia di Blender Extensions
4. **No API Documentation** - Sulit untuk automation tanpa eksplorasi manual

## Instalasi

### Cara Standard
1. Beli di Blender Market
2. Download file .zip
3. Buka Blender → Edit → Preferences → Add-ons
4. Install from Disk → pilih file .zip
5. Enable "Simply Cloth"

### Cara via MCP
```python
import bpy
import os

# Install addon via Python
addon_path = "/path/to/simply-cloth.zip"
bpy.ops.preferences.addon_install(filepath=addon_path)
bpy.ops.preferences.addon_enable(module="simply_cloth")
```

## Sumber

- Blender Market: https://blendermarket.com/products/simply-cloth
- Developer: JLAB
- Video Review: [Referensi video yang diberikan user]

## Catatan untuk Automation

Untuk mengontrol Simply Cloth via MCP, perlu ditemukan:
1. **Operator names** - Cari di F3 menu atau Python console
2. **Parameter names** - Cek signature operator
3. **Workflow sequence** - Urutan operasi yang benar

Contoh eksplorasi:
```python
import bpy
# List semua operators
print([op for op in dir(bpy.ops) if 'cloth' in op.lower()])

# Cek operator tertentu
help(bpy.ops.simply_cloth)
```

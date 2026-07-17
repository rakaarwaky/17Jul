---
name: mpfb-getting-started
description: Step-by-step guide for installing, configuring, and creating your first character with MPFB (MakeHuman Face Builder) Blender addon
source: learned
---

# MPFB (MakeHuman Face Builder) — Installation & Getting Started

## When to Use
- When helping users install MPFB as a Blender addon
- When setting up MPFB for the first time (user data directory, asset packs)
- When creating a new character from scratch in MPFB
- When users need guidance on character customization workflow

## Procedure

### Step 1: Install MPFB from Blender Extension Platform
1. **Enable online access** in Blender preferences — this is required for finding MPFB in the extension marketplace
2. Go to the **"Get Extensions"** tab in Blender
3. Search for and install **MPFB** (MakeHuman Face Builder)
4. MPFB was released as stable in late January 2025 and is available on Blender's extension platform

### Step 2: Configure MPFB User Data Directory
1. Open **Add-on Preferences** (settings panel for the addon)
2. Set the **user data directory** — this is where MPFB stores all its data including asset packs
3. The directory **must already exist** before pointing MPFB at it
4. You can choose any directory you prefer
5. **Save preferences and restart Blender** — settings won't take effect until restart

### Step 3: Install System Asset Packs
After restarting, MPFB should appear on the **N shelf** (right panel). Press **N** key if not visible.

1. Open the **asset packs webpage** via the button under **"System and Resources"** panel
2. Browse available asset packs — skins, clothes, hair styles
3. At minimum, install the **MakeHuman System Assets** pack
4. In Blender, go to **"Apply Assets and Library Settings"** panel
5. Click **"Install Asset Pack"** and browse to the downloaded zip file

### Step 4: Create a Character From Scratch
1. Go to the **"New Human"** panel
2. Select **"From Scratch"** option
3. Choose basic traits (gender, age range, etc.) — choices don't matter much as everything can be changed later

### Step 5: Fine-Tune the Character
In the **"Model"** panel:
- Adjust **weight**, **muscularity**, and other body proportions
- Use detail settings for facial features (nose size, eye shape, etc.)
- Settings are fully adjustable at any time

### Step 6: Add Skin Texture
1. Go to **"Apply Assets and Skins"** panel
2. Browse available skin textures from installed asset packs
3. Apply desired skin texture

### Step 7: Add Rig
1. Go to the **rig panel**
2. Choose a rig type — needed because body parts (eyes, clothes) added later will be auto-rigged
3. For basic use, default options work fine

### Step 8: Attach Body Parts & Clothing
Using the asset panels:
- **Eyes, eyebrows, eyelashes** — common facial features
- **Hair** — various styles from asset packs
- **Clothing** — necessary for proper rendering/export
- Adjust properties like eye color, hair style, etc.

### Step 9: Use Rig Helpers for Posing
1. Add **rig helpers** (IK controls) to the default rig
2. These make posing much easier
3. Enter **Pose Mode** and adjust hand/arm positions using the IK controls

### Step 10: Save & Load Characters
Use MPFB's built-in save system (separate from Blender's blend file save):
1. Go to **"Manage Save Files"** panel
2. Save character settings — allows loading the character in a new scene
3. To reload: go to **"New Human > From Save File"** panel and load the saved character

## Pitfalls
- **Forgetting to enable online access**: MPFB won't appear in the extension marketplace without it
- **User data directory doesn't exist**: MPFB requires the directory to be created before you can set it as the data path
- **Not restarting after config changes**: Addon preferences only take effect after saving and restarting Blender
- **Skipping system asset pack**: MPFB works without it, but you'll have no skins, clothes, or hair styles
- **MPFB panel not visible**: Press **N** key to show/hide the right-side N-panel where MPFB tabs appear
- **Saving only blend file**: While this works, MPFB's own save system is better for reusing characters across scenes

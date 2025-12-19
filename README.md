> DDLC 中文 Mod 模板 v5 目前处于早期开发阶段（可视为刚刚新建文件夹），请暂时不要使用本版本模板！我们还在决定 v5 版本的翻译、开发方向。  
> 如果您有简体中文 DDLC 同人模组创作需求，请您暂时先使用 DDLC 中文 Mod 模板 [2.0](https://github.com/imgradeone/DDLCModTemplate-Chinese-next) 或 [4.0](https://github.com/DokiMod/DDLCModTemplate-Chinese-future)，或者暂时直接使用 [DDLC Mod Template 2.0](https://github.com/Bronya-Rand/DDLCModTemplate2.0) 修改字体等配置。

# 文思泉涌**新**出发 - DDLC 中文 Mod 模板 v5
基于 "Bronya Rand" 的 [DDLC Mod Template (5.0)](https://github.com/Bronya-Rand/DDLCModTemplate2.0) 开发，由 DokiMod 翻译、修改

中文模组开发社的各位，欢迎回来！

<p align="center">
  <img src=".github/IMAGES/ddlcmt-open-graph.png"/>
</p>

<p align="center">
   <a href="https://github.com/Bronya-Rand/DDLCModTemplate2.0/releases/latest">
      <img src=".github/IMAGES/download.png">
   </a>
   &nbsp;&nbsp;
   <a href="https://ko-fi.com/K3K22K8SU">
      <img src="https://www.ko-fi.com/img/githubbutton_sm.svg">
   </a>
</p>

## 目录
- [📖 Overview](#-overview) 
- [📋 Credit Requirements (Important)](#-credit-requirements) 
- [✨ Features](#-features) 
- [🚀 Quick Start](#-quick-start) 
- [📦 Building & Distribution](#-building--distribution)
- [🎯 Platform-Specific Guides](#-platform-specific-guides)
- [📚 Additional Resources](#-additional-resources)
- [👏 Credits](#-credits)

## 📖 Overview

DDLC 中文 Mod 模板 v5 是 Azariel Del Carmen (bronya_rand) 开发的 [DDLC Mod Template (5.0)](https://github.com/Bronya-Rand/DDLCModTemplate2.0) 的中文翻译版本，由 DokiMod 修改、翻译，旨在为 DDLC 中文同人创作者提供现代化、简易化、遵循 [Team Salvato's IP 准则](https://teamsalvato.com/ip-guidelines/) 的中文同人模组开发环境。

该模板专为 Ren'Py 8 构建，提供了制作 DDLC 同人模组所需的一切资源，兼具现代功能、跨平台支持与代码优化。

该模板**十分适合：**
- 初次接触同人模组创作且正在寻求坚实基础的同人创作者
- 想将引擎升级到 Ren'Py 8 的、经验丰富的同人创作者
- 寻求跨平台支持的开发者 (Windows x64, macOS, Linux)

> [!NOTE]
> **DDLC Mod Template 与 DDLC 中文 Mod 模板与 Team Salvato 完全无关，且并非为 DDLC 续作《Doki Doki Literature Club Plus!》设计。请勿将该模板（含上游模板）及其代码用于非官方 DDLC 补丁等其他用途。**

> [!NOTE] 
> 由于 Python 2 已于 2020 年 1 月 1 日停止支持，Ren'Py 7 已在 Ren'Py 8.4 发布后终止支持，[DDLC Mod Template 2.0](https://github.com/Bronya-Rand/DDLCModTemplate2.0) 已暂停 Python 2 分支开发，因此 DDLC 中文 Mod 模板 v5 将不会继续兼容 Python 2 / Ren'Py 7。由此带来不便，烦请谅解。

---

## ✨ Features

### Core Features

- ✅ **顺应 Team Salvato 的准则要求** - Includes required splashscreen (disclaimer) and follows all IP guidelines for fan mods.
- 🐍 **Python 3 & Ren'Py 8 优化** - Clean, modern code optimized for the latest Ren'Py.
- 📚 **Original DDLC Scripts Included** - Reference the original game scripts for learning purposes.
- 🌐 **Cross-Platform Support** - Build for Windows, macOS, Linux, and Android.
- 🎨 **Automatic GUI Coloring** - Customize GUI and menu button colors without editing assets.
- 🖼️ **Dynamic Super Resolution (DSR/DSP)** - Universal resolution template supporting custom resolutions.
- 📝 **Player Name Change** - Allow players to correct or change their name in-game.
- 💬 **Enhanced Console & Poem Responses** - Improved Monika console and cleaner poem response system.

### Gameplay Features

- 🎮 **无屏蔽模式** - Option to show more sensitive content.
- 📹 **实况主模式** - Protect personal information while streaming/recording.
- 📖 **NVL 支持** - Full NVL (novel-style) dialogue support thanks to Yagamirai01.

### Returned DDLC Features

Classic DDLC features restored and improved:
- 👻 **Ghost Menu** - Dan's spooky easter egg.
- 💔 **Character Kill Scripts** - Sayori and Monika deletion scripts.
- 📄 **Special Poems** - Act 2 random poems _(now improved!)_.

### Optional Extras

> [!IMPORTANT]
> Download `DDLCModTemplate-X.X.X-Extras.zip` to access these optional features.

- 💥 **Better Blue Screens of Death** - Create custom BSODs on all platforms.
- 🖼️ **Gallery System** - Showcase your artwork and CGs.
- 🏆 **Achievements Menu** - Reward players for completing milestones.
- 🎮 **[BETA] Discord Rich Presence** - Show mod activity on Discord.

---

## 🚀 Quick Start

### Prerequisites
1. **[Ren'Py 8.X](https://www.renpy.org/latest.html)** 
2. **[DDLC (PC Version)](https://ddlc.moe/)**
3. **[This DDLC Mod Template](https://github.com/Bronya-Rand/DDLCModTemplate2.0/releases)**

### Installation Steps

1. **Extract Ren'Py** to a folder of your choice.
> [!WARNING]
> Do not extract Ren'Py to a cloud storage folder (e.g. Google Drive, OneDrive, etc.) as it will cause issues when testing your mod.

2. **Create a new folder** in the `renpy-8.X.X-sdk` folder and extract the DDLC Mod Template ZIP into it.

3. **Extract DDLC assets** - Open `DDLC-1.1.1-pc.zip` and copy these RPA files into the mod template's `game` folder:
   - `audio.rpa`
   - `fonts.rpa`
   - `images.rpa`

4. **Launch the template**
   - Open the Ren'Py Launcher.
   - Select the DDLC Mod Template project.
   - Click _Launch Project_ to test it.

🎉 You're ready to start modding!

---

## 📦 Building & Distribution

When you're ready to release your mod:

1. Open the **Ren'Py Launcher**.
2. Click on **Build Distributions**.
3. **Uncheck all options** in `Build Packages` and check **Ren'Py 8 DDLC Compliant Mod**.
4. Click **Build**.

This creates a cross-platform mod package ZIP file (marked with `-Renpy8-DDLCMod` in the filename) containing your mod files ready for distribution.

> [!TIP]
> Always test your mod thoroughly before building and distributing!

---

## 🎯 Platform-Specific Guides

### Android

Making your mod work on Android requires additional considerations, especially for complex features or non-mobile-friendly code.

📱 **Read the full guide:** [Android Mod Guide](./Documentation/Android%20Mod%20Guide.pdf)

> [!NOTE]
> For older templates, refer to the PDF included in your template's ZIP file as the latest guide may not match your version.

### Linux

Linux users must run mods using the included launcher script (at least once):

```bash
./LinuxLauncher.sh
```

### macOS

macOS support is included out of the box. Build distributions include macOS packages automatically.

---

## 📋 Credit Requirements

> [!IMPORTANT]
> **You MUST credit this template in your mod.** By default, a credits screen is enabled in-game (either in the Extras screen or as a standalone button). You can use the default implementation or choose one of the alternatives below.

### Default Credit Text

Include this in your mod's credits screen and/or `credits.txt` file:

```
This mod was made possible by bronya_rand's DDLC Mod Template 2.0: https://github.com/Bronya-Rand/DDLCModTemplate2.0
```

### Alternative Credit Methods

If you prefer a different approach, you may use one of these alternatives:

1. **Custom Splash Screen** - Feature the Team Salvato logo alongside a Bronya Rand logo ([available here](.github/IMAGES/Logos/)).
2. **Disclaimer Mention** - Add a line to your game's disclaimer: "This mod was made possible using bronya_rand's mod template".
3. **Presplash Screen** - Include a Bronya Rand logo ([available here](.github/IMAGES/Logos)) in your presplash.
4. **Custom Idea** - Contact me via Discord or Reddit with your proposed credit method for approval.

---

## 📚 Additional Resources

### Documentation

- 📱 [Android Mod Guide](./Documentation/Android%20Mod%20Guide.pdf) - Complete guide for Android porting
- 🎮 [Discord RPC Guide](./Documentation/Discord%20RPC%20Guide.pdf) - Set up Discord Rich Presence
- 📝 [New Poem Game Guide](./Documentation/New%20Poemgame%20Guide.pdf) - In-depth poem game documentation

### Community & Support

- 💬 **DDMC Discord** - Get help and share your mods with the community
- 🐛 **Issues** - Report bugs on [GitHub Issues](https://github.com/Bronya-Rand/DDLCModTemplate2.0/issues)
- ☕ **Support Development** - [Buy me a Ko-fi](https://ko-fi.com/K3K22K8SU)

---

## 👏 Credits

Thanks to the following people for their contributions to the DDLC Mod Template:

> [!NOTE]
> This list goes from the past to present.

- Dan Salvato (DDLC)
- renpytom (Ren'Py)
- MAS Team (template base before revamping)
- alicerunsonfedora (Xcode)
- Terra (In-depth poem game)
- Yagamirai01 (NVL)
- Alexxonder (Auto Color Adjustments)
- Elckarow (Python 3 updates, New poem responses/effects)
- NekoLaiS (Cryllic compatibility)
- The DDMC Community (Feature suggestions and feedback)
- Pseurae (Donation/Act 3 GL2 Fix)
- Lezalith (New Console (4.1.1+))
- RS/6000 (New Mod Template Logo (4.2.1+))
- Tulkas (Android Gestures)
- FiT (Weiss Chibi Branding Icon Design)
- Retronika (Supplemental code for the Gallery system)

---

<p align="center">
   <b>Copyright © 2019-2025 Azariel "Bronya Rand" Del Carmen (bronya_rand). All rights reserved. Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato. Copyright © 2017 Team Salvato. All rights reserved.</b>
</p>

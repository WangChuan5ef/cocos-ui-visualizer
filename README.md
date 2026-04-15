# Cocos UI Visualizer

[中文](#中文版本) | [English](#english-version)

---

## English Version

### Overview

**Cocos UI Visualizer** is a powerful Python tool for previewing and analyzing Cocos2d-x UI files (`.csb` and `.json` formats). It provides an interactive GUI that allows you to visualize UI layouts, inspect node properties, debug animations, and validate resource references in real-time.

### Features

- ✨ **Real-time Preview**: Load and display Cocos UI files instantly
- 🔍 **Node Inspection**: Explore the complete node hierarchy with detailed properties
- 🎨 **Visual Debugging**: Toggle panel fill, show hidden nodes, and inspect rendering layers
- 📦 **Resource Fallback**: Automatic fallback handling for missing texture references
- 🎭 **Animation Support**: Preview and analyze animations and special effects
- 📂 **Batch Processing**: Load entire folders of UI files for bulk testing
- 🌐 **Bilingual Interface**: Support for Chinese and English

### Requirements

- Python 3.8 or higher
- Windows 10/11 (with support for other platforms planned)

### Installation

#### Option 1: Automatic Installation (Recommended)

Run the one-click installer:

```bash
python install.py
```

This will automatically:
- Check Python version compatibility
- Install required dependencies
- Set up the environment

#### Option 2: Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/WangChuanSef/cocos-ui-visualizer.git
cd cocos-ui-visualizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python cocos/cocos_gui.py [path_to_ui_folder_or_file]
```

### Usage

#### Starting the Application

```bash
python cocos/cocos_gui.py
```

Or specify a UI folder directly:

```bash
python cocos/cocos_gui.py "path/to/ui/folder"
```

#### GUI Controls

| Feature | Description |
|---------|-------------|
| **Panel Fill** | Toggle background panel visibility for cleaner node visualization |
| **Show Hidden** | Display hidden nodes and their hierarchy |
| **Node Inspector** | Click nodes to view detailed properties and animation data |
| **Resource Browser** | Browse and validate texture and resource references |
| **Zoom Controls** | Scale and pan the viewport for detailed inspection |

### Recommended Testing Files

For validation, test with these files (in order):
- `activity_atmosphere_fx_race.csb`
- `login_logo.csb`
- `login_new.csb`

**Testing Checklist:**
- Test with "Panel Fill: OFF, Show Hidden: OFF"
- Test with "Panel Fill: ON, Show Hidden: ON"
- Verify that previously missing backgrounds now display correctly

### Troubleshooting

**Issue**: Resources not loading
- **Solution**: Ensure the UI folder structure matches the expected layout with all texture assets in the correct paths

**Issue**: Hidden nodes not visible
- **Solution**: Enable "Show Hidden" toggle in the menu bar

**Issue**: Animation not playing
- **Solution**: Check that all referenced animation assets are present in the resource folder

### Recent Updates

**Version 1.0.0**
- Fixed ProjectNode child file state handling
- Improved ListView content rendering
- Enhanced special effects node blending
- Added resource fallback mechanism
- Implemented proper runtime display layer handling

### Project Structure

```
cocos-ui-visualizer/
├── cocos/
│   ├── cocos_gui.py              # Main GUI application
│   ├── cocos_parser.py           # CSB/JSON file parser
│   ├── cocos_runtime.py          # Runtime rendering engine
│   ├── CSParseBinary_generated.h # Binary format definitions
│   └── ui/                       # UI resources folder (add your assets here)
├── install.py                    # One-click installer
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore configuration
└── README.md                     # This file
```

### Contributing

Found a bug or have a feature request? Please feel free to open an issue or submit a pull request.

### Author

Created by **WangChuanSef**

- Bilibili: [http://space.bilibili.com/1642823606](http://space.bilibili.com/1642823606)
- GitHub: [https://github.com/WangChuanSef](https://github.com/WangChuan5ef)

### License

This project is provided as-is for educational and development purposes.

---

## 中文版本

### 项目简介

**Cocos UI 可视化工具** 是一个功能强大的Python工具，用于预览和分析Cocos2d-x UI文件（`.csb` 和 `.json` 格式）。它提供了一个交互式GUI，让您可以实时可视化UI布局、检查节点属性、调试动画和验证资源引用。

### 核心功能

- ✨ **实时预览**: 即时加载和显示Cocos UI文件
- 🔍 **节点检查器**: 探索完整的节点层级及详细属性
- 🎨 **可视化调试**: 切换背景面板、显示隐藏节点、检查渲染层
- 📦 **资源回退机制**: 自动处理缺失的纹理引用
- 🎭 **动画支持**: 预览和分析动画及特效
- 📂 **批量处理**: 加载整个文件夹进行批量测试
- 🌐 **双语界面**: 支持中文和英文

### 系统要求

- Python 3.8 及以上版本
- Windows 10/11（其他平台支持已规划）

### 安装方法

#### 方式一：自动安装（推荐）

运行一键安装程序：

```bash
python install.py
```

安装程序会自动：
- 检查Python版本兼容性
- 安装所需依赖包
- 配置开发环境

#### 方式二：手动安装

1. 克隆仓库：
```bash
git clone https://github.com/WangChuanSef/cocos-ui-visualizer.git
cd cocos-ui-visualizer
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python cocos/cocos_gui.py [UI文件夹或文件路径]
```

### 使用说明

#### 启动应用

```bash
python cocos/cocos_gui.py
```

或直接指定UI文件夹：

```bash
python cocos/cocos_gui.py "path/to/ui/folder"
```

#### GUI 控制说明

| 功能 | 说明 |
|------|------|
| **背景面板** | 切换背景面板显示，用于清晰查看节点 |
| **显示隐藏** | 显示隐藏节点及其层级关系 |
| **节点检查器** | 点击节点查看详细属性和动画数据 |
| **资源浏览器** | 浏览并验证纹理和资源引用 |
| **缩放控制** | 缩放和平移视口进行详细检查 |

### 推荐测试文件

用于验证的推荐测试文件（按顺序）：
- `activity_atmosphere_fx_race.csb`
- `login_logo.csb`
- `login_new.csb`

**测试清单：**
- 测试"背景面板关、显示隐藏关"的状态
- 测试"背景面板开、显示隐藏开"的状态
- 验证之前缺失的背景现在是否正确显示

### 故障排查

**问题**: 资源无法加载
- **解决**: 确保UI文件夹结构与预期一致，所有纹理资源都在正确的路径中

**问题**: 隐藏节点不可见
- **解决**: 在菜单栏中启用"显示隐藏"选项

**问题**: 动画无法播放
- **解决**: 检查所有引用的动画资源是否存在于资源文件夹中

### 最新更新

**版本 1.0.0**
- 修复ProjectNode子文件状态处理
- 改进ListView内容渲染
- 增强特效节点混合模式
- 实现资源回退机制
- 优化运行时显示层处理

### 项目结构

```
cocos-ui-visualizer/
├── cocos/
│   ├── cocos_gui.py              # 主GUI应用程序
│   ├── cocos_parser.py           # CSB/JSON文件解析器
│   ├── cocos_runtime.py          # 运行时渲染引擎
│   ├── CSParseBinary_generated.h # 二进制格式定义
│   └── ui/                       # UI资源文件夹（将您的资源添加到此处）
├── install.py                    # 一键安装程序
├── requirements.txt              # Python依赖列表
├── .gitignore                    # Git忽略配置
└── README.md                     # 本文件
```

### 贡献指南

发现bug或有功能建议？欢迎提交Issue或Pull Request。

### 作者信息

由 **WangChuanSef** 创建

- Bilibili: [http://space.bilibili.com/1642823606](http://space.bilibili.com/1642823606)
- GitHub: [https://github.com/WangChuanSef](https://github.com/WangChuan5ef)

### 许可证

本项目以"现状"形式提供，仅供教育和开发使用。

---

**Last Updated**: April 15, 2026

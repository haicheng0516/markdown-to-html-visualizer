# Markdown to HTML Visualizer

🎨 自动将测试报告 Markdown 转换为带图表的 HTML 可视化报告

## ✨ 功能特性

- ✅ Markdown 转 HTML（支持表格、代码块）
- ✅ 自动生成图表（Chart.js）
- ✅ 响应式设计
- ✅ 单文件输出
- ✅ 打印友好

## 🚀 快速开始

### 安装
```bash
git clone https://github.com/haicheng0516/markdown-to-html-visualizer.git
cd markdown-to-html-visualizer
pip install markdown2 jinja2 --break-system-packages
```

### 使用
```bash
python3 converter.py your_report.md
```

## 💼 在 Claude Agent Teams 中使用

在项目的 `CLAUDE.md` 中添加：
```python
import subprocess
subprocess.run([
    "python3",
    "~/markdown-to-html-visualizer/converter.py",
    "reports/报告.md"
])
```

## 📊 生成的图表

1. **测试通过率饼图** - 显示通过/失败比例
2. **问题优先级分布柱状图** - 显示 P0/P1/P2/P3 问题数量

## 🎨 自定义

修改 `templates/report.html` 可自定义样式和图表类型。

## 📄 License

MIT

## 👤 作者

haicheng0516 - https://github.com/haicheng0516

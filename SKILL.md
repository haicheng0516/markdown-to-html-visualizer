# Markdown to HTML Visualizer Skill

## 功能

将 Markdown 测试报告自动转换为带图表的 HTML 可视化报告。

## 使用场景

- 测试报告生成后自动创建 HTML 版本
- 添加图表：通过率、问题分布、时间线等
- 单个 HTML 文件，可直接在浏览器打开

## 触发条件

当生成以下类型的 Markdown 文件时自动转换：
- `reports/*测试报告*.md`
- `reports/*Test_Report*.md`
- `reports/*缺陷清单*.md`

## 使用方法

### 在 Claude Agent Teams 中使用

在项目的 `CLAUDE.md` 中添加：
```python
import subprocess
subprocess.run([
    "python3",
    "~/markdown-to-html-visualizer/converter.py",
    "reports/报告.md"
])
```

### 手动使用
```bash
python3 ~/markdown-to-html-visualizer/converter.py reports/测试报告.md
```

## 安装
```bash
# 克隆仓库
git clone https://github.com/seacity/markdown-to-html-visualizer.git ~/markdown-to-html-visualizer

# 安装依赖
pip install markdown2 jinja2 --break-system-packages
```

## 生成的图表

1. **测试通过率饼图** - 通过/失败比例
2. **问题优先级分布柱状图** - P0/P1/P2/P3 数量

## 依赖

- Python 3.6+
- markdown2
- jinja2

## 输出示例

输入：`reports/Testnet_实测报告_20260317.md`  
输出：`reports/Testnet_实测报告_20260317.html`

打开 HTML 可看到：
- 格式化的报告内容
- 交互式图表（Chart.js）
- 响应式布局
- 可打印版本

---

**作者**: seacity  
**GitHub**: https://github.com/haicheng0516/markdown-to-html-visualizer  
**License**: MIT

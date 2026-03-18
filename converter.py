#!/usr/bin/env python3
"""
Markdown to HTML Visualizer
自动将测试报告 Markdown 转为带图表的 HTML
"""

import re
import sys
import json
from pathlib import Path
from datetime import datetime

try:
    import markdown2
    from jinja2 import Template
except ImportError:
    print("缺少依赖，正在安装...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown2", "jinja2", "--break-system-packages"])
    import markdown2
    from jinja2 import Template


def parse_test_report(md_content):
    """解析测试报告，提取统计数据"""
    stats = {
        'total_tests': 0,
        'passed': 0,
        'failed': 0,
        'p0_count': 0,
        'p1_count': 0,
        'p2_count': 0,
        'p3_count': 0,
    }

    # 提取测试通过率
    pass_match = re.search(r'通过[：:]\s*(\d+)', md_content)
    fail_match = re.search(r'失败[：:]\s*(\d+)', md_content)
    if pass_match:
        stats['passed'] = int(pass_match.group(1))
    if fail_match:
        stats['failed'] = int(fail_match.group(1))
    stats['total_tests'] = stats['passed'] + stats['failed']

    # 提取问题优先级
    p0_match = re.search(r'P0[：:\s]+(\d+)', md_content, re.IGNORECASE)
    p1_match = re.search(r'P1[：:\s]+(\d+)', md_content, re.IGNORECASE)
    p2_match = re.search(r'P2[：:\s]+(\d+)', md_content, re.IGNORECASE)
    p3_match = re.search(r'P3[：:\s]+(\d+)', md_content, re.IGNORECASE)

    if p0_match:
        stats['p0_count'] = int(p0_match.group(1))
    if p1_match:
        stats['p1_count'] = int(p1_match.group(1))
    if p2_match:
        stats['p2_count'] = int(p2_match.group(1))
    if p3_match:
        stats['p3_count'] = int(p3_match.group(1))

    return stats


def convert_to_html(md_file_path):
    """转换 Markdown 为 HTML"""
    md_path = Path(md_file_path)

    if not md_path.exists():
        print(f"错误：文件不存在 {md_file_path}")
        return None

    # 读取 Markdown
    md_content = md_path.read_text(encoding='utf-8')

    # 解析统计数据
    stats = parse_test_report(md_content)

    # 转换 Markdown 为 HTML
    html_content = markdown2.markdown(md_content, extras=['tables', 'fenced-code-blocks'])

    # 读取 HTML 模板
    template_path = Path(__file__).parent / 'templates' / 'report.html'
    template_content = template_path.read_text(encoding='utf-8')

    # 渲染模板
    template = Template(template_content)
    final_html = template.render(
        title=md_path.stem,
        content=html_content,
        stats=stats,
        generated_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        source_file=md_path.name
    )

    # 输出 HTML
    html_path = md_path.with_suffix('.html')
    html_path.write_text(final_html, encoding='utf-8')

    print(f"✅ 已生成: {html_path}")
    return str(html_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python converter.py <markdown_file.md>")
        sys.exit(1)

    convert_to_html(sys.argv[1])

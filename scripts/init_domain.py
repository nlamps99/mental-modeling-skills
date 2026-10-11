#!/usr/bin/env python3
"""
init_domain.py - 领域认知脚手架初始化脚本
用法:
    python scripts/init_domain.py "领域名称" [动机说明]
示例:
    python scripts/init_domain.py "分布式系统" "解决高并发架构瓶颈与故障恢复"
"""

import sys
import os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("错误: 请提供目标领域名称！")
        print("用法: python scripts/init_domain.py \"领域名称\" [动机说明]")
        print("示例: python scripts/init_domain.py \"分布式系统\" \"掌握高可用架构设计与容灾推演\"")
        sys.exit(1)

    domain_name = sys.argv[1].strip()
    motivation = sys.argv[2].strip() if len(sys.argv) > 2 else "从零建立该领域的直觉认知模型与实战反应力。"
    today_str = datetime.now().strftime("%Y-%m-%d")

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(project_root, "templates", "COGNITIVE_CANVAS.md")
    domain_dir = os.path.join(project_root, "domains", domain_name)

    os.makedirs(domain_dir, exist_ok=True)

    # 读取模板
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 替换变量
    content = content.replace("[例如：微观经济学 / Rust异步运行时 / 认知行为疗法 / 推荐系统架构]", domain_name)
    content = content.replace("YYYY-MM-DD", today_str)
    content = content.replace("为什么要在此时吃透这个领域？要解决什么现实问题？", motivation)

    canvas_path = os.path.join(domain_dir, "CANVAS.md")
    with open(canvas_path, "w", encoding="utf-8") as f:
        f.write(content)

    # 创建工作草稿文件
    stage_files = {
        "01_materials_and_entities.md": f"# {domain_name} - 阶段 1: 感性素材与本体草图\n\n在此记录向 AI 索取的 5 个极端案例，并手写最初提炼的 3~5 个不可简化硬实体。\n",
        "02_relational_topology.md": f"# {domain_name} - 阶段 2: 四维拓扑网络\n\n记录向上找根（母规律）、横向借脑（同构映射）、拮抗对偶（解毒剂）与因果回路推演。\n",
        "03_falsification_probing.md": f"# {domain_name} - 阶段 3: 红队反例击穿记录\n\n记录 AI 抛出的 3 个极端反例，标定模型的失效边界与前提红线。\n",
        "04_sparring_and_decisions.md": f"# {domain_name} - 阶段 4: 两难沙盒对练与产生式\n\n记录与 AI 考官的极端灰度对练，以及沉淀的 IF-THEN 实战产生式。\n",
    }

    for filename, initial_content in stage_files.items():
        filepath = os.path.join(domain_dir, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(initial_content)

    print(f"\n🎉 恭喜！领域 [{domain_name}] 的认知工作区已创建成功：")
    print(f"📁 工作目录: domains/{domain_name}/")
    print(f"📄 认知画布: domains/{domain_name}/CANVAS.md")
    print(f"\n💡 下一步建议：")
    print(f"1. 打开 domains/{domain_name}/CANVAS.md 查看总览")
    print(f"2. 打开 AI 对话框，输入指令：/start {domain_name} 开始第一阶段素材浸润！\n")

if __name__ == "__main__":
    main()

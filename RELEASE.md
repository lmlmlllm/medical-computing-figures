# 1.44.1 — public source edition

公开分发准备日期：2026-10-23。该版本由本机稳定版 1.44.1 整理，原创内容采用 MIT 许可。仓库提供技能入口、5 个绘图／检查脚本、样式、89 条案例卡和可直接运行的 MedSAM／MedRAG 示例。公开版不包含本机历史审计、运行环境或第三方论文原件；完整范围见 [README](README.md) 和 [NOTICE](NOTICE.md)。

## 本次实际执行

- 使用公开目录按 README 执行规格检查、方法图生成和结果图生成，三条命令均成功。
- 37 项有限检查通过，包含 10 行公开汇总值与转录表／映射核对、SVG 可编辑文字、PDF 文字和矢量对象，以及两张 PNG 和两份 PDF 页面实际查看。详见 [公开检查记录](verification/public-source-smoke.json)。
- 5 个脚本、入口及示例输入沿用稳定版原字节。3 份 MedSAM 规格结构检查通过，89 个案例卡链接存在；当前 STATUS 与 catalog 的数量核对一致。
- 原准备阶段发现结果示例缺少其引用的原始转录 CSV，已补齐；公开 STATUS 的简写格式曾不能被目录检查器读取，已改为其支持的明确格式并复测通过。两项修正不改变绘图代码或科学数据。

执行环境为原开发主机 macOS、Python 3.14.0、PyMuPDF 1.28.2 及原绘图依赖。原版本的完整本机宿主验收与本次公开版烟测分别记录；本次没有重新开展全部科学案例或其他智能软件的宿主测试。

## 复现

按 README 安装 Python 依赖后执行三条示例命令。目录数量核对可运行：

    python scripts/check_catalog_summary.py --status STATUS.md --catalog references/catalog.jsonl

ZIP 使用 `medical-computing-figures/` 顶层目录。解压到宿主支持的技能目录，保留完整目录结构；已存在同名安装时先比较，不应混用两个不同副本。ZIP 校验值见随附 `.sha256` 文件；包内 `MANIFEST.json` 列出其余源码文件的 SHA-256。

其他支持 Agent Skills 的宿主可按 README 的官方安装方式使用；Claude Code、Gemini CLI 和其他操作系统尚未实测。生成的数据图展示原论文的公开汇总值，不代表重跑原始模型。图文核验仍需要当前研究材料和实际看图。

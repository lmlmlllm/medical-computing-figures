# SVG 连线修复检查

当图稿有本技能生成的可编辑 SVG，审读者提出删除、恢复或保留连线时，用 `scripts/check_svg_repair.py` 核对当前路径的实际端点；修复后可再核对实际后图。图源的关系 ID 不能代替可见路径坐标。

```sh
python scripts/check_svg_repair.py \
  --svg current.svg --bindings nodes.json --plan repair-plan.json \
  --after-svg revised.svg --out new-check.json
```

输出文件必须是新文件，父目录已存在；输入和输出路径拒绝符号链接。工具只用 Python 3.9+ 标准库，本机已用 Python 3.14 实际运行。退出码 0 表示本次几何/操作核对支持，1 表示输入或操作不符，2 表示几何未能评估。检查没有通过时保留输出，不把未知填成存在或缺失。

## 先绑定真实图形

`nodes.json` 显式把视觉节点 ID 绑定到 SVG 的矩形 group ID。一个视觉框可同时表达多个科学实体，此处只记录这个物理框。先实际看完整 SVG 的配套渲染，确认每个框及其标签；别名框单独绑定。必要的分叉点可以绑定到一条实际路径的某个顶点，保持其“分叉”角色，不自动解释为源实体之间的科学传递。

```json
{
  "schema": "mcf-svg-node-bindings-v1",
  "convention": "mcf-separated-shaft-head-v1",
  "nodes": [
    {"id": "pseudo", "shape_id": "GROUP_pseudo_assignment"},
    {"id": "aux", "shape_id": "BOX_O_Lpatch"},
    {"id": "slide", "shape_id": "BOX_O_Lslide"}
  ],
  "excluded_arrows": {},
  "non_arrow_shafts": {}
}
```

这是字段示例。实际检查要覆盖图中所有纳入范围的箭头端点节点；例图的完整绑定见[CLAM](../tests/batches/svg-repair-geometry-01/inputs/clam-bindings-02.json)、[HIL](../tests/batches/svg-repair-geometry-01/inputs/hil-bindings-02.json)、[DINO](../tests/batches/svg-repair-geometry-01/inputs/dino-bindings.json)。

分叉点另给出 `point_from_arrow`、`vertex_index` 及非空 `connected_to_arrows`。前两项从实际支线路径取得坐标；后者指定必须接触的其他载体路径，检查前图和后图都应满足。例如 HIL 的 meal 分叉还必须接触 `meal_kf` 主干，不能仅让两条支线一起移动后仍共享同一个标识。

普通分隔线有时也带 `--shaft` 后缀。用 `non_arrow_shafts` 明列其 ID 和看图依据，不按名称猜它是箭头。图例样例箭头用 `excluded_arrows` 明列理由；输出保留这些排除。真正箭头的头部缺失时不能将它改列为分隔线来制造通过。

## 无边框文字的声明锚点

没有矩形的原生文字可以使用 `text_attachment`，但它只核对**调用者预先声明的文字原点偏移**。它不测量字形轮廓，也不证明箭头接触了文字边界。先看完整图，记录为何把该偏移作为连接位置；不能用箭头自身坐标作为动态锚点，不能虚构一个框来增加覆盖率。

一个节点只能选择 `shape_id`、`point_from_arrow`、`text_attachment` 中的一种。`text_attachment` 必须包含四个字段：

- `runs`：按顺序给出每个实际文字 run 的 `group_id` 和完整 `text`，包括有意义的下标。
- `glyphs`：按上述 run 的实际顺序列出所有单字符字形的 `group_id`、`text`、`relative_pt` 和原始 `style`。相对位置以首字符实际 x/y 为原点，第一项为 `[0, 0]`。
- `offset_pt`：相对于首字符原点的有限二维数值偏移；在构建编辑副本前固定。
- `review_note`：非空看图及声明依据。工具只验证字段存在，真实性仍由作者负责。

完整的已执行例子见 [UA-MT 绑定](../tests/batches/svg-text-endpoint-01/run-03/bindings.json)。其中 `Previous teacher θ′` 和 `(t−1)` 的 24 个实际字符共同构成 `TEXT_previous_teacher`，偏移 `[88.65625, 8]`。从前后 SVG 分别提取当前文字坐标；同一绑定允许全部字符刚性平移且连线随动，拒绝缺下标、字符单独移动或内容变化。不要为后图重新拟合偏移来掩盖断连。

支持范围很窄：逐字符原生 `text`，独立的纯 ID 分组祖先，标量 x/y，正字号、常规 400 字重的 DejaVu Sans、start 锚定、六位十六进制填色。只允许文字自身、围绕其原点的零角度 `rotate`；祖先变换及其他定位/呈现属性未评估。文档样式只允许本渲染器的内嵌字体声明和固定默认描边样式；任意 CSS 不解析。遮挡、字体实际实现、裁切和科学含义仍需看图。输出暴露声明类型、计算位置、原点、偏移、完整 run 字符串和 `glyph_ink_contact_checked: false`。

文字祖先中的 `svg` 只能是文档真实根；嵌套视口改变坐标系，保持未评估。原始 XML 中除 XML 声明外的处理指令也保持未评估，避免 `xml-stylesheet` 被 XML 解析器丢弃后漏过样式边界；工具不取回外部样式。

目前实际测试的是一个文字**源端点**；不能据此声称文字目标、一般排版或任意编辑器兼容性已验证。UA-MT 新清单包含 17 条原有形状/分叉关联和 1 条声明文字端口关联；原批次的 17/18 结果保持原版本范围。

## 提出完整操作

`remove` 和 `preserve` 指定当前箭头 ID 及声称的起止节点。检查器直接读 SVG 的 shaft/head 路径，以端点落在矩形边界、明确分叉点或上述声明文字端口的位置建立清单；端点未绑定或匹配多个节点时保持未评估。坐标容差固定为 0.25 pt。

`restore` 指定拟恢复的箭头 ID 和节点对：当前已存在的节点对不能再当作缺失边恢复。移除后的 ID 可供恢复边沿用。`required_edges` 记录根据文章、已确认规格或当前测试要求必须存在的关系；它的科学依据由绘图者另行核对。只有删除错边而没有恢复必需目标，会报告 `required_edge_missing`。

```json
{
  "schema": "mcf-svg-repair-plan-v1",
  "remove": [{"arrow_id": "EDGE_R21", "source": "pseudo", "target": "slide"}],
  "restore": [{"arrow_id": "EDGE_R21", "source": "pseudo", "target": "aux"}],
  "preserve": [],
  "required_edges": [{"source": "pseudo", "target": "aux"}]
}
```

给出 `--after-svg` 后，工具比较实际后图的全部纳入箭头 ID/起点/终点与拟定后图，而非只检查修复目标。折线形状可变，端点与保留边应满足要求。仅检查计划时，输出的 `actual_after_graph_matches` 为 null，不能称实际图已修复。

## 适用范围与已测试证据

支持本技能的分离 shaft/head 命名约定、单段 M/L/Z 原生路径、轴对齐矩形、明确分叉点及上述受限声明文字端口。除文字自身的限定零角度旋转外，变换、曲线、光栅/marker 箭头、缺失或反向头部、节点端点歧义会拒绝或标为未评估。不能把工具用于未核对的任意 SVG。

它核对路径坐标与操作集合。遮挡/裁切后的可见性、完整 CSS、文字标签、颜色/线型的科学意义及文章依据仍需实际查看和联合审阅；DINO 的梯度与两种 EMA 尤其不能只凭端点相同判为科学含义不变。

[固定开发测试](../tests/batches/svg-repair-geometry-01/README.md)当前第三轮 12/12 通过：拒绝 CLAM/HIL 历史错误建议、核对其实际修复、核对 DINO 的既有折线编辑，并运行具体格式和写入负对照。分叉接触另有预定 2 项软件检查，2/2 通过；它们与原 12 项分开。首轮失败、测试记录程序退出及旧工具错误接受脱离主干支线的记录均保留。这里没有新增独立读者样本或重计原科学验收分母。

文字扩展的 [14 项固定开发对照](../tests/batches/svg-text-endpoint-01/run-03/result.json)为 14/14；另行预定 [7 项样式对照](../tests/batches/svg-text-endpoint-01/style-after-02/result.json)为 7/7。样式修复前只通过 1/7，另 6 项错误接受记录保留。原 12 项与 2 项分叉检查已在当前代码重跑通过。以上均为软件控制，不合并成科学准确率，也不替代独立代码审阅或实际图像检查。


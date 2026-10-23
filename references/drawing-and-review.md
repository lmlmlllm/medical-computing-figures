# 绘制、回读、交付

先定主图/补图的任务与面板间证据关系，再选泳道、多分支、局部展开、层级架构、时间线、矩阵或真实数据图。必要模块框、token、张量和算子应保留；装饰和长文字不能掩盖核心连接。

## 同一研究的多图一致性

用一份简短图组计划说明每张图回答的问题、来源、共用术语和前后承接关系，再保留各图自身的规格与数据映射。区分原文图号和本次交付图号；只制作方法图与结果图子集时，不称为完成整篇论文的图组。

方法与结果能够对应，须有原始材料支持的配置联系：模型版本、检索/处理设置、队列与划分、评价单位、指标和分母应一致，或明确说明差异。相同算法名称、配色或并列位置不能建立这种联系。将来源中的宽泛工具框架收窄到一个实际评价配置时，保留这个选择及省略项，不让结果看似适用于所有配置。

统一标签、单位、语义颜色和图注交叉引用，但不以排版统一替代上述核对。实质性方法变更后，检查受影响的结果图和图注；未重新运行的性能保留为原配置结果，不能迁给新配置。纯外观修改则比较每张受影响图的语义与数据映射，再实际查看整组渲染。跨图关系的测试范围应独立记录，不能仅凭两张单图各自通过就声称图组一致。

选择任务子集后重新汇总时，先固定集合及选择依据，逐表/配置保留原始点值与来源键，再生成明确命名的新统计量。已发表的旧均值与本次由已舍入点值计算的新均值属于不同对象；等任务权重不能混成按问题人数加权，原报±也不能直接合成为新均值误差。同步范围、分母、主图、明细、图注和比较方向，共享端点不自动成为独立重复。[MedRAG 四图实例](../tests/batches/medrag-examination-subset-01/README.md)仅验证一项公开汇总数据的派生展示；原实验未重跑，旧七图保留。

## 可编辑与视觉

关键文字、节点、关系线、面板/系列分别可改，稳定ID写进SVG对象。验证实际输出中的完整ID集合也唯一，包含派生字形和箭头对象；不能只检查语义规格ID。核对文字组到PDF字形的绑定覆盖且不重复，防止字典按重名键覆盖证据。图像像素不变仍可能存在可编辑寻址错误，见[fNIRS重复ID修复](../tests/batches/fnirs-channel-contributions-01/DELIVERY.md)。此检查在该例有限复测，未称所有导出工具均已覆盖。不要用整图PNG包装为SVG冒充矢量。真实影像等栅格层可保留，明确可编辑范围。默认白底、低饱和语义色、深色字、留白和对齐；仅色彩不承担关键区别。整套图统一角色与别名。当前 style.json 是迁移的暂定配置，并非本用户新技能已确认偏好。

图源与渲染输出分开保留。字号以最终尺寸为准：预览放大可读不等于印刷尺寸可读。大图必要时拆面板。绘制后实际看完整PNG/PDF页面及箭头端点、共享模块、图例等局部，记录观察尺寸。检查裁切、碰撞、字体、方向、图例、图号。缺陷→修正→重看；文件存在或脚本成功不能替代这一步。

声明物理尺寸时同时核对PDF页面尺寸、栅格像素数及PNG嵌入的分辨率。以150 ppi渲染PDF不保证生成的PNG也写入150 ppi元数据；engineering-01曾输出尺寸正确但标为约96 ppi的预览。屏幕查看及文件几何核验不称为实际打印测试。

更换预览生成器后，主图哈希相同不代表预览像素也相同。PDF光栅化与PNG缩放可能产生不同的取整尺寸和文字边缘；分别保留审阅者实际看到的版本，再查看最终预览。figure-set-01保留了620→619像素的版本关系；ECG仅补写密度字段则通过像素与原PNG数据块哈希证明未改图。

## 数据图

保留原始输入或合法小型公开汇总表、字段映射、单位/分母/聚合层级、代码、环境版本、命令和输出。只画输入支持的图；不反推个体预测，不伪造显著性/区间/热图/掩膜。误差线须记录其定义、样本层级和来源。存在重复测量不能把点当独立受试者。汇总表重绘是数据适配，不是原实验复现。

生成式图片只可作被允许的示意素材，不替代精确连接、实验或患者影像；遵守工具和目标期刊要求。期刊未指定时输出可调整SVG、PNG和适用PDF，不称可直接投稿。

## 工具

`render.py` 读取语义规格和显式布局，用 Matplotlib 生成含文字的SVG、PDF、PNG、逐节点/关系清单和caption。SVG文本保留为 `<text>`；节点/线有gid。其默认流程连线用箭头，supervision用虚线并有图例，非有向关系无箭头；必须核对该约定是否适合当前图。复杂张量图可使用自定义脚本，不强行塞入渲染器。

`check_spec.py` 检查唯一ID、端点、来源引用、必需字段与语义变化。未知/冲突产生需审查状态。自动检查不能证明医学正确，也不能读像素。`plot_results.py` 只支持映射明确的公开汇总点图；其他统计任务使用适合的标准绘图库。

## 修改与验收

科学内容改变：新规格明确变更事实/测试假设，同步节点、边、标签、图例、图注；原性能不得转给新模型。纯外观改变：语义快照比较相同，再看渲染是否引入含义变化。

语义JSON相同不能证明缩短后的可见文字含义相同。重排、换行或删字后，逐项核对主体、条件、单位和证据范围是否仍在图中可读；正确图注不能代替图内遗漏的关键限定。[脑—脊髓接口重排](../tests/batches/brain-spine-interface-01/README.md)曾在核心规格不变时丢失“实验者定义”和反馈声明的范围，最终恢复并复看。

严格阈值变更需同步参数、比较符号、示例、标签与图注；检查值恰等于阈值的边界。conformal-pathology-01 用给定模拟 p 值核验 c 与 ε=1−c 的联动，不把集合选择测试当成 p 值构造或统计覆盖验证。

对照测试在自绘隔离副本中，一次变一项；中性文件名，先固定输入/关键清单/预期，再交独立阅读者。报告正确对照误报、错误漏报、不足不可判定和复测历史。开发自测、独立模型复核、人工专家审核分别命名。图→文审阅者先看图和图例，再看规格/原文。

独立盲读者不得制作错误副本、预期或故障键，也不得继承这些内容的会话历史。先冻结只看图的记录，再开放图注、来源和任务请求；评分前始终不开放答案。材料不足测试另用未见过完整输入的新会话，并移除能反推出缺失量的派生值、图像和说明。已看过完整数值后再遮住一个标签，只能检验显式缺口报告，不能证明信息不足时没有补答案。

解除参数共享时，同时修改参数实体、绑定关系、可见连线、模块标签及图注；不同名称连接同一参数实体或保留共同总线，仍可能表示共享。集合参数框同时含独立 W_k 和共享 λ 时，规格应逐项记录绑定方式，不能把整个集合统一标成共享。还要检查继承的关系条件、状态、来源引用和初始化说明，避免图中已写“变体”，规格仍把它归给原论文。当前有限实例与保留的失败见 [MoDL 三图测试](../tests/host/modl-three-figure-01/DELIVERY.md)。

修改冻结范围时，先把具有不同更新状态的参数子集拆分为可辨对象，再同步状态标签、优化目标、所属网络绑定和图注。新增更新边不能误替代仍须保留的更新边；“可训练”表示优化资格，不自动断言每个参数的数值改变。训练策略变化还需复核依赖该策略的输出解释，例如参考空间对齐或整合效果，未验证时不能沿用原方法的结果主张。[scArches假设性解冻测试](../tests/batches/scarches-specified-unfreezing-change-01/README.md)提供一个同案例的有限示例；这段操作细化尚未在另一案例独立验证。


每图交付：spec + editable SVG或其他约定源 + PNG/PDF预览/导出 + caption + 复现命令/数据映射 + 精简检查记录。不能只交提示词或脚本。

按实际复现依赖和分发许可建立文件白名单，再核对压缩包成员；包含所需输入、代码、环境说明及已保存结果。阅读缓存、源文截图／抽取全文和无关历史不随工作目录递归打包；需要分发的来源材料另核实许可。外部运行时或工具依赖须在复现说明中明确，不能把包内有脚本称为无需外部环境。[七图交付实例](../tests/host/modl-three-figure-02/README.md)分别保留原作者归档与实际重放的干净包。

## 经测试发现的读图风险

多条相似分支不可复制前一图的视觉读数。逐条记录箭头头部所在节点/方位，必要时放大局部后再对应稳定ID；发现定位疑点时保留初次判断并单独复测。独立模型也会把错误定位到相邻分支，不能只按“发现了某个错误”计通过。重定向还可能使原路径消失：先核对实际存在与缺失的线，再提出删除／恢复，不能根据正确流程想当然地列出未画出的原线。conformal-pathology-01 首次检出两处错接，却多记两条原线，导致修复建议不完整；初次记录和来源知情定向复看分别保留。

提出端点重定向修复时，明确列出当前错边、应移除边、应恢复边和必须保留的边。若必需边已缺失，写明恢复或重连，不能只写“保留”；导出后核对错边消失、必需边存在、其他边不变，并实际看图。[HIL评价参考对照](../tests/batches/hil-reference-loop-control-01/README.md)两阶段均检出并定位错连，却因把缺失边说成仍可保留而得到完整修复0/1。已知答案指导的根修复另记，不追改读者评分。此处是已有规则再次失效后的操作细化。随后同一读者定向复查能明确提出恢复缺边，见本批记录；其结构化缺失边条目另有继承措辞矛盾，保留缺陷。该复查不是新盲测。随后在[CLAM端点恢复对照](../tests/batches/clam-edge-restoration-control-01/README.md)中将该要求应用于不同医学图和新读者，两阶段完整修复仍为0/1：错图的Y输入实际存在却被误称缺失，真正缺失的辅助目标又被列为保留。该结果保留为跨案例应用失败，不证明提示改善。

当前边状态必须另有本图线迹依据：先确认起点、分叉/交叉和箭头头部落点，必要时查看局部并记录范围；看不清的端点保持待判。再用原文判定应有关系，不能把来源要求直接填成图中存在或缺失的事实。报告与JSON内部自洽只是文字一致性检查。这项操作细化尚待新的独立样本验证。

当已有采用本技能分离shaft/head约定的可编辑SVG，可按[SVG修复检查用法](svg-repair-check.md)从实际路径核对操作集合，并在实际后图核对全部纳入端点。矩形、分叉载体、普通分隔线和图例排除先逐项人工绑定；缺失/歧义或不受支持格式保持未评估。明确分叉须在前后图接触指定载体，不能仅让标识随支线移动。该工具是可编辑图稿的几何辅助；文字内部一致性、端点一致和科学含义一致分别核查。


## 整套解释图的交付

整套图先固定主图／补图分工、任务顺序、配置身份、指标单位和数值覆盖表。同一端点重复出现时明确标记；同名配置不能自行合并成一次运行。统计方法的身份颜色与准确率等连续色标分开，跨页保持尺度一致。

只有汇总表时，画表所支持的点值或矩阵。定性摘要须在图内及图注说明省略的定量细节，并实际查看原曲线以保留关键局部反向变化。保留 ± 数值不意味着已核实其推导；不把它们重新解释成置信区间或跨运行误差。

多页补图按一个语义图、多个页面计数。每页分别检查字体、SVG／PDF 几何、PNG 密度和实际可读性；明确 PNG 对应的 PDF 页，不能默认第 0 页。合订阅读 PDF 可由已核验单图合并，并逐页核对几何和渲染等价；保留各图可编辑源。

## 真实多通道波形

固定记录、导联顺序、校准、时间窗、采样时间及共同尺度后再绘制。以单位和显式刻度解释幅值，标清缩放或偏置；小幅值导联在预览中不清楚时提供完整矢量图或适当局部，不默默对每条自动缩放。记录是否抽样、简化或滤波；声称保留全部样本时核对实际导出路径的顶点数量及与输入的映射，而不仅检查内存绘图数组。

独立读取真实数据，再从 SVG 的轴/路径反算时间与幅值，能发现数据、导联、单位或丢点问题；另查 PDF 路径、字体和 PNG 密度。程序通过后仍需实际看整图与预览。单标签错误测试保留相同数据和正确图注，先冻结图像含义，再提供来源，分别报告检测、准确位置、单位倍数解释和正确对照误报。修复单独生成并复看，不回写首次审阅。

[signal-waveform-01](../tests/batches/signal-waveform-01/README.md)提供一个真实记录的完整示例。随包原始波形/头文件有明确 CC BY 4.0 归属、完整许可和哈希；与未分发的论文原图分开声明。当前记录专用解码器不是通用信号格式库。

## 窗口内容变更的同步

将窗口边界作为一个明确的选择参数，由它派生索引、截取数据、全记录范围标记、局部坐标和图注。保留原版本，再生成新的完整交付；比较原记录不变量和实际改变的样本成员。原时间与窗口内时间两面板应能直接核对幅值顺序，若幅度或尺度改变须另行说明。不能只移动高亮框或改标题。

[signal-window-01](../tests/batches/signal-window-01/README.md)将同一真实导联的选择从[2,4)秒改为[6,8)秒，两窗各1000点，相对末点均1.998秒。独立源数据与实际SVG/PDF路径核对验证了对应；错用相邻样本幅值、旧原点及旧范围三个软件副本分别被拒绝。它们是有限程序敏感性测试，不是模型读图准确率。语义规格的关系仍须有稳定ID和来源字段，数值路径正确不能代替规格完整性。

## 栅格图像与可编辑叠加

披露图像保留为栅格层，将边界、ROI 和文字作为独立可编辑对象；从实际导出检查嵌入像素与叠加几何的对应。PDF 可能倒序编码图像行并用放置变换恢复方向，数值比较须应用实际放置矩阵（CTM），不能仅凭存储行序判定翻转。低分辨率预览用于可读性检查；源像素小于一个预览像素时，精确边界占用仍须由像素数据和矢量坐标核验。

## 生存阶梯与同步计数

由一个截止参数及逐行退出账目生成曲线、两类删失、风险／累计计数、端点标签与图注；保留真实事件的水平后垂直角点，删失本身不降阶，不用线性连线或平滑替代。重合来源删失可按独特时刻画一个标记，但披露重数；行政端点用可区分的空心标记，中心不偏移、文字向内且不被边界裁掉。两版共同区间比较恢复的数据坐标，不能把轴比例改变当作数值改变；表列与时间刻度对齐，并明确退出前／含当时刻累计的区别。从实际 SVG/PDF 核对角点、标记中心和表格文字，处理导出库等价的路径表示而不放宽数学容差。[survival-display-01](../tests/batches/survival-display-01/README.md)保留完整示例、首轮检查器修正及有限软件控制；低密度预览和程序通过仍不代替实际看图与来源范围核对。

## 数值矩阵的字段变更与缺失

由明确的行／列成员驱动单元、标签、数量摘要和图注，保留源行列定位与原始数值。比较同一来源的字段扩展时先固定共享色域和映射；颜色由未舍入值计算，文字按单独声明的规则舍入。新值超出已核验色域应报错或明确重新设计，不能静默裁剪或自动缩放共同单元。缺失采用与低值不同的颜色并写 `NA`，图例明确；完整 ID 与重复测量分组须可读。

核对实际 SVG/PDF 单元几何、文字及颜色，而不只比较绘图数组。PDF 原生 DeviceGray/DeviceRGB 的数值与颜色管理后的显示 RGB 可能不同；选择与冻结合同一致的解释并保留首轮失败，不为通过而放宽容差。本批只处理其明确的原生路径与文字结构，纵向文字还依赖行内约束和实际看图。[protein-matrix-01](../tests/batches/protein-matrix-01/README.md)提供四列→八列的两个独立可编辑交付；缩略图逐格阅读有限时打开完整 PNG 或 PDF。

## 双向概率矩阵的成员变更

变更图像或文本成员时，同步分数矩阵、两方向概率的行列标签、形状、归一化分母、损失聚合与图注。共有分数不变，不代表共有概率也不变：被删成员处于某方向的归一化集合内时，须重新计算该方向的全部概率。把分数、logits和概率分别命名、标轴与定色域；格内舍入只用于显示，不能作为下游计算输入。

逐格连接输入、全精度计算、对象映射和实际SVG/PDF，另核对成员标签；只检查同一程序生成的两份数组不足以证明导出正确。源论文规定等批大小而测试改为不等大小时，图内说明这是测试扩展，不把原性能移给修改方法。[multimodal-contrastive-01](../tests/batches/multimodal-contrastive-01/README.md)保留3×3→2×3/3×2的模拟示例、已知答案的软件错误副本及修复；这些测试不作为独立盲读准确率。

## 条件路由的绘制与内容修改

把决策输出和被送入分支的数据分别画清；在选择器与每条路径上标条件，若互斥选择，直接写明只执行一条。反查实际箭头头部、方向和目标对象，不能只核对规格中的端点ID。复杂度类别不同于图面板编号；跨面板命名引用也应明说其对象和作用。

将某类问题改走其他路径时，同步类别到目的地的条件、保留与删除的节点、上下文反馈、标签及图注。删除循环后，旧图注或来源注记不能仍把当前图称为原方法。只改路由政策不等于重训分类器或验证性能；明确为本地测试，保留原版与首次问题。[rag-routing-01](../tests/batches/rag-routing-01/README.md)的C→单次检索测试删除四节点／五边，并保持A及分类器输出类别不变；程序敏感性与执行者自查不称独立盲审。

## 空间小图的支撑与消息方向

将无向支撑画成无箭头连线，将示意的邻居到目标聚合画成定向箭头并保留自环含义。剪枝示例固定节点身份和坐标，只删除声明的边；节点颜色或分组标签不能被误读为真实细胞类型。模拟拓扑标明给定半径、任意单位与非研究结果，不绘制未计算的注意力权重。

节点中心、边和组标签须在实际预览核对叠放层级与遮挡。空间批次首稿曾被连线盖住节点，第二稿左移标签仍压在水平边上；第三稿提高节点层级并将标签移到斜侧空隙后复看。不能只靠坐标未越界来验收。关闭可选分支后，同时删除节点、边、剪枝示意和组标签，保留完整支撑与重构路径；[spatial-graph-01](../tests/batches/spatial-graph-01/README.md)给出两版可编辑图及换色保持测试。


## 配置策略改变与阶段边界

将配置计划、拟合权重、验证证据和未见图像画成不同对象；设置线与数据线用图例解释，不用虚线暗示证据不足。条件分支在节点或路径上明确条件，集成标签写清按折还是按配置。固定单一配置后，同步删去候选选择器及所有依赖，保留仍执行的折集成和后处理选择，移除旧的数值说明与图注。来源解释性补线在规格和交付说明中标为解释，不能把程序端点通过当成代码或实验支持。配置批次还显示了重排风险：路径穿标题、文字越框、上层节点遮住设置线都需实际查看修正，单纯几何未越界不够。


## 标注、筛选与抽样审查的画法

把标注产物、拟合模型、候选掩膜和最终纳入集合画成不同对象；训练线与数据线说明类型，避免进入和离开同一节点的两条线共用重合端口而形成假反馈。时间先后与数据收集即便同为实线，也用就近标签区别。复杂处理若只掌握步骤组，应明确组内并非完整执行次序。将抽样改成全量人工审查时，更新样本节点、审核/接受决策、发布对象、关系类型、分母和图注；移除原流程结果，不把扩大审查范围当成效果已验证。材料不足的标签同样必须可读，不能因“不可判定”就跳过渲染检查。


## 转置、残差和参数约定

显式标注关键接口的轴顺序。残差加法至少有两个可辨输入，并确认旁路究竟来自原始输入还是已归一化/变换后的表示。将参数共享约定放在相应模块附近或清楚的说明面板中，用文字覆盖颜色含义；不把同色或重复方框当成共享证据。修改共享方式时同步模块标签、约定、关系条件、规格和图注，保留未变的形状/运算；原论文经验结果不能随结构图变更迁入。概览与代码细节不同可声明粒度，但不可悄悄增删训练机制。


## 点区间图与结果度量修改

把阈值作为明确标注的离散行，以点和区间端点绑定源表；独立横轴须就近声明。短区间在大范围内难读时保留精确数值，不能为美化截断负值或合成曲线。换算结果度量时同步变换估计值、上下端点、单位、轴限、标签及图注；固定正因子的变换应保持端点顺序，并披露原表舍入。净干预减少当量不是观测到的手术/活检计数。实际查看总标题、副标题和面板标题之间的间距：全部在画布内仍可能互相覆盖。本批先保留两类首稿问题，再另存修复并复看。


## 窗参数、网格与显示边界

窗口长度、hop、FFT点数、补值和去趋势分别声明，由样本索引推导窗中心、频点及显示单元边界。窗支撑不等于单元宽度；边缘无显示数据须说明，不应看似零功率。改窗时重算样本成员、谱值、坐标、数量、标签和图注；频点加密不能单独声称提高可分辨能力。对同一数量的比较固定色域，外观改变保持数值映射。检查色条本身是否被自动栅格化，不能仅凭主面板的矢量单元声称全部可编辑。见[有限时频实例](../tests/batches/signal-timefreq-01/README.md)，不外推到不同API的窗中心约定。


## 注意力矩阵和越界颜色

把分数、softmax 输入、权重和值输出分开命名，行/列身份就近标注；V 的旁路进入加权乘法，不能误接分数或 softmax。屏蔽 logits 写明确的负无穷/排除标记，与数值零区别；保留全精度计算和单独显示舍入。修改允许集合时同步单元、路径、行和、标题与图注。发散色图核对零点及端点，新值超出共享色域时拒绝或显式标出饱和范围，不能默默取端点颜色。注意力错误对照曾出现 O=3.401 超过色域3，首轮检查未发现；历史30/30与新增检查后的30/31均保留，修订图以≥3和图注解释并复看。参见[有限实例](../tests/batches/attention-core-01/README.md)。


## 跳跃分支的接口绘制

在跳跃连接上显式显示复制/裁剪后的空间大小，并为融合的两个输入保留独立端点；邻近方块不等于已完成拼接。通道数与空间尺寸使用不同标签位置或明确C、H/W符号；合并两个连续卷积时保留中间尺寸及操作次数。修改输入后同步主干、上卷积、裁剪区间、融合和输出标签。半开区间写明索引约定，局部约定不冒充原代码。接口示意中用类别特征框表示未计算输出，不以合成掩膜替代。[U-Net接口实例](../tests/batches/segmentation-shapes-01/README.md)保留可编辑节点/路径，并分别记录已知错误与材料不足。


## 森林图中的方向、重叠与原生标记

正比值使用与任务相符的对数坐标，参考值1、区间端点及比较方向应可核对。列标题、数值、favor标签和图注共同定义方向，不能只交换一种。用分隔和文字明确总体包含此前亚组，菱形不自动表示荟萃汇总。数值审计应检查导出SVG/PDF的实际标记与区间路径；整页背景也可能是填充路径，按几何匹配数据对象，不凭填充总数判定。[已测示例](../tests/batches/effect-estimates-01/README.md)保留该检查器失败以及看图后脚注修订。


## 聚合图保留矩阵轴、原始身份与输出身份

矩阵乘法图应显示轴方向、ID对齐和运算定义。本例使用genes×cells的X、groups×cells的H和Y=XHᵀ；原始样本条与输出组标签分开，0/1成员标签让读者不依赖颜色。不同量纲或取值范围的矩阵使用明确的独立色标。原生图可以忠实绘出一份错误规格，不能以SVG/PDF检查代替语义判断。冻结期望也需核实：发现手算预期错误时保留原失败，按输入字段另行复算并记录更正，不能改数据去满足错误清单。见[保留R04错误与修复证据](../tests/batches/pseudobulk-units-01/expected-errata-01.json)。


## 差值图的坐标、界限与单位联动

每个点对应已核实的一对读数；平均值作横轴、指定方向的差值作纵轴，原始ID留在数据映射中。均值线、SD界限和零线用标签与线型共同区分，不以颜色或“95%”字样代替误差定义。点超出界限时保留该点，不删点或调整界限使图更整齐。

显示单位变化时同步换算坐标、均值、SD、界限、轴范围、单位与图注，保留原始文件单位。源文用舍入中间量得到的界限可能与未舍入重算不同；先根据源精度固定容差再核验，不改数据追求逐位相同。原生SVG/PDF可忠实绘出错误统计量，导出检查不能代替源数据审查。[本批](../tests/batches/measurement-agreement-01/README.md)实际定位了标准误替代SD、反向标签和错配三类错误。


## 抽样依赖与条件记忆更新

多个概率条目共同定义一次抽样分布时，先用明确分组或汇聚表达整体，再连接到各抽样槽。单箭头从某个概率卡片下方出发，可能把整个分布误读为该条目专属的输入；文字和正确数值不足以补救这个视觉暗示。多个槽保持原始ID，并说明负载和位置编码共同选择。

将当前读取和随后写入分面板／分阶段；条件变化时同步阈值比较、通过／失败、被移除与保留的成员及图注。未知输出不画推测的空库、具体成员或指向空白的结果箭头。明确当前图是完整算法、单个查询还是一次内部迭代。[有限模拟例](../tests/batches/memory-selection-01/README.md)保留原箭头缺陷、输入不足测试失败和单独修复。


## 校准率与预测计数

将校准频率和箱内人数放在明确区分的坐标轴上；若计数轴各自缩放，保留各轴刻度和数值，不能只凭柱高作跨面板数量比较。改变分箱时同步成员、均值、条件频率、数量、标题和图注，保留原预测向量。空箱不画伪零点。

不确定性带按实际生成量命名：校准假设下的一致性带与曲线估计周围的置信带不同。没有实施相应算法就不沿用参考图的带或评分数值。[公开天气数据例](../tests/batches/calibration-binning-01/README.md)仅验证分箱表达，不代表临床或CORP方法复现。

## CORP curves, bands and support
Preserve the observed forecast domain of the fitted curve. In this verified author convention, horizontal maximal PAV blocks are joined linearly only between supported knots; extending the curve to0 or1 invents support. Keep counts on an explicitly labelled count axis. For a band-target change, update bank, bounds, finite counts, title/legend, caption and spec together while holding forecasts/outcomes/fit/scores fixed. Signed MCB,−DSC,UNC bars make the decomposition readable; label the original score and the same-sample scope. Unknown estimates and absent input columns must agree. Correct controls, reversed-sign/target-mismatch/support-extrapolation failures and repairs are in [current CORP deliveries](../tests/batches/calibration-isotonic-01/DELIVERY.md).

## Classwise p-values and bounded data displays
Pair candidate-class values with distinct marker shapes and direct labels. Link count traces to those points by stable case/class IDs, show the strict threshold, then derive the displayed prediction sets from unrounded values. Connectors between paired values mean comparison, not a causal transition. With missing test truth, retain computable p-values/sets and explicitly withhold truth-based error counts. A hard-coded sample-count label or fixed-row layout is an input contract: validate it before output or compute it dynamically. Unequal-stratum numeric support does not prove a fixed six-case graphic accepts arbitrary counts. [Current example and reproduced label failure](../tests/batches/conformal-version-01/DELIVERY.md).

## 条件混淆热图与零／缺失状态
保持真实类和赋值类的轴身份稳定；换行／列分母时同步重算全部分数、标题、公式、图例和图注，原始计数不变。用未舍入分数定色，单独声明百分数显示精度，区分精确零、很小的正值和无分母NA。实际缺失一个矩阵时，保留可计算面板并去掉缺失面板的数值和观测总数。核对原生SVG/PDF单元坐标、颜色和文字；XML缩进不等于可见多行文字。复用公开表的专用适配器应校验来源身份，不能把任意修改值继续归给原论文。[本例](../tests/batches/confusion-matrix-01/DELIVERY.md)的原表和研究图未随包分发。

## ROC/PR的原生坐标检查
声明连接线的计算规则。TP/FP计数空间的线性混合通常在PR空间形成非线性段，不能只对端点做直线插值。用不同标记区分可达到的整组阈值与混合位置，并用引线消除临近点标签歧义。类别权重改变时同步坐标、支持量、基线、规格和图注。标签实际缺失时保留分数组信息，去除全部ROC/PR数值及基线；不从已知论文或旁路文件重建缺失标签。核对SVG/PDF中实际路径、点和基线，即使底层计算JSON正确也可能画错。

## Sampling arrows and repeated inputs

For coordinate transforms, show the selected output point, input sampling location and enough neighbour/weight evidence to disambiguate direction. Inspect actual arrow endpoints as well as recorded values. Repeated labelled aliases may reduce crossing wires, but retain one scientific entity and explicitly state same input. Color changes require wording checks in legends and region labels. [Registration example](../tests/batches/registration-warp-01/DELIVERY.md) records these observed fixes.

Graph retrieval displays should label matrix row/column node order, undirected versus directed edges, probability-vector orientation, continuation versus restart and one-step versus stable values. Place frequency/specificity and count contributions where readers can inspect them. Raw passage scores are not probabilities. Missing seed mappings leave downstream values unknown; an alias must name its original count map.

For phase portraits use explicit axes/units, isotropic scaling when vector direction is compared, distinct component-nullcline styles and zero-vector markers. State that scaled arrow tips are display endpoints, not integrated future states. Recheck label collisions after parameter changes; validate native arrow endpoints, table components and nullcline equations separately.

Align channel IDs across traces, timing columns, interpolation brackets, markers, weights and contributions. Keep signed amplitude scales explicit; show the declared interpolation point rather than silently rounding. A sum alone can hide a timing error: both an authorized q3 sample and an erroneous q6 sample produced total9 in the test. Inspect channel locations as well as aggregate values. Missing-input wording must agree in the table, caption and footer.

Align CIF step curves and risk tables to the same time mapping. Keep same-time censors in the just-before-time denominator and weight increments by pre-event overall survival. Preserve per-group observed support and show sparse tails. Missing event types permit risk counts only: remove probability curves and their legend swatches, and ensure unknown messages remain legible over grids.

For path attribution, keep path colors consistent across feature space, signed integrands, component estimates and convergence. Include each coordinate derivative in a curved-path integrand; distinguish numerical estimates from exact references. Label coincident curves explicitly. Missing baseline means missing paths/attributions, never a silently substituted zero baseline.

When illustrating RNA-to-cell fraction conversion, show reference columns, type-aligned size factors, raw coefficients and normalization as distinct steps. Pair fraction bars with fitted-expression displays to expose cases where equally good fits have different labels. Missing size factors withhold the cell-side branch; retain only independently determined RNA-side outputs. Use labels and hatch/line styles beyond color.

Compare P/Q on a shared numeric color range and signed mismatch on its own labeled scale. Separate the vector sum from the update arrow and show sampled cost along a fixed initial direction as such, not as successive optimized iterations. Check short-arrow shaft and head geometry at export size; default endpoint shrinking can reverse a short shaft. Coordinate absence must leave map-dependent panels unknown.

## Editable equations across export formats

When an equation is essential to a method, inspect its actual native glyph baselines, accents, fraction rules and vector geometry in the final SVG and PDF, using pinned fonts and a tolerance fixed before the comparison. Editable text alone does not establish matching placement. The [PASTE2 export repair](../tests/batches/paste2-partial-coupling-01/README.md) used one 72 dpi mathematical layout to place ordinary editable glyphs and fraction rules in all formats; its first repair hid the group behind the background, so layer visibility also required actual viewing. Retain failed exports and recheck the final whole figure and affected details. This specific implementation is not a verified universal renderer: ordinary shaping, combining marks and other font/engine combinations require their own checks. Package required font bytes with their licenses, use process-local activation, and state that SVG font dependencies differ from embedded PDF fonts.


共享布局也需覆盖普通文字、连续空格和组合重音。若原生后端对组合字符重新定位，只有在实际字体的轮廓和变换给出等价证据时才替换为独立显示字形，同时保留原公式、原 Unicode 和替换记录；可见字形等价不等于文本提取一致。逐字形文字仍可编辑，但整标签修改应回到源码，并说明编辑粒度。[LOUPE 的波浪号修复](../tests/batches/loupe-sampling-01/README.md)已完成原生复测与精确包重放；此实现不保证其他字体、编辑器或组合字符同样适用。

字体文件路径与 SVG 的字体族、字重、斜体声明须同时核对；嵌入了正确字体，不代表实际文本选中了它。PDF 使用显式粗体文件而 SVG 文本缺少字重声明时，可能出现字形和字距差异，尽管基线、数值及 PNG 都正确。核对实际使用的渲染器所选字形及字体度量，保留空格的间距检查；同时捕获字体日志与警告，不能只检查一种消息通道。[ESM 首轮原生失败](../tests/batches/esm-threshold-burden-01/output-audit/native-01/native-report.md)提供实际反例，修复复测与隔离重放状态见该批记录。此规则已写入，尚不构成跨字体或通用排版保证。

[ESM修复复测](../tests/batches/esm-threshold-burden-01/README.md)使用受控静态CairoSVG解析实际样式并显式绑定固定字体，完成原生检查与精确包重放。此证据限定于该渲染路径，不证明浏览器CSS字体解析；空格的显式度量探针须与实际有墨迹文字绘制调用分开计数。浏览器被策略阻止时保留未验证状态，不通过换协议或替代浏览器绕过限制。


公式中的下划线、插入符与花括号作为源记号保存，正式图应渲染为实际上下标。保留结构化公式与最终可见文字，逐项核对上下标附着对象、求和条件、嵌套索引和原生基线；连接后的字符串相同不能证明数学结构相同。脚本拆成独立字形段时需检查相邻段边界及多行间距。[UA-MT修订](../tests/batches/uamt-uncertainty-gating-01/DELIVERY.md)保留首版裸记号问题和第二版重叠拒绝，第三版以1pt段间距、1.60行距通过有限核对；这些数值仅是该图实现，不是通用字号或排版标准。作用范围文字应放在所属节点内或明确连接，避免位置靠近另一分支而改变归属。


用于原生字形、字体和几何比较的契约，也须把实际文件哈希放入导出前冻结记录；只有规格与布局已冻结，或日志显示先生成契约，并不证明该契约字节已前置封存。漏项时保留原记录及未评估范围，另建一次先固定契约、后导出的有限复测，并核对所有输入和输出。新复测不能倒填历史时序；用相同字节沿用既有原生审计时，明确区分证据复用与重新逐对象检查。见[RAG契约复测](../tests/batches/rag-marginalization-01/DELIVERY.md)，此程序要求尚未在另一案例独立验证。


UA-MT端点对照已完成受限应用：先封存原审读再给几何清单；文字源端点若超出工具约定，明示排除并继续看图/对文核验，不能虚造矩形计作全图通过。见[17/18范围与实际修复](../tests/batches/uamt-mean-entropy-edge-control-01/README.md)。辅助前后承诺相同，不推论准确率提升。


无边框文字需要端点核对时，可以在实际看图后声明相对于完整原生文字原点的固定端口，见[文字端口规则](svg-repair-check.md)。前后图共享同一绑定，覆盖有意义的下标、完整字形成员、相对位置和受支持样式；后图不得重拟合偏移。报告应区分矩形边界/分叉接触与调用者声明文字端口，不能借此声称字形墨迹接触。无法解析的样式、XML样式处理指令或嵌套视口保持未评估；持续保留实际查看和来源核对。[有限开发与独立增量证据](../tests/batches/svg-text-endpoint-01/README.md)只覆盖所列平坦原生文字来源。


选取报告表的部分行时，逐行核对单位；宽泛列标题不能把后续计数或时间行变成百分比。原报差值与展示比例的相减结果不一致时，保留原报差值和配套CI并说明未明原因，不自行改值或声称已证实舍入。图旁标明实际分析总体，详细排除和定义限定放入随图交付的完整图注。[EndoMind限定实例](../tests/batches/endomind-reported-risk-differences-01/README.md)将三个相关终点绘成独立点区间行，未汇总为总体效应。


并列展示筛查与条件性随访比例时，就近绑定各自结局、路径、时间窗和分母；共享百分比轴不建立共同估计目标。同一照护事件可满足多个结局定义，不能因分栏就把事件或人数当成独立、不重叠的数量。见[ACCESS限定图](../tests/batches/access-screening-denominators-01/DELIVERY.md)：这是既有分母规则在本例后的窄化说明，尚未跨另一案例独立行为验证。


对事件门控设备图，先依据来源区分校准→候选事件→拒绝→计数→定时动作；拒绝支路回到来源支持的监测阶段。人工启停表示控制可用性，不能自动等同于执行器开/关。通信、供电和生物靶向各自标明角色；数值冲突就近连接受影响操作，同时保留未知。见[单例及限定范围](../tests/batches/bladder-event-gated-control-01/README.md)，不将定性流程通过当作控制代码或效果复现。原生核对报告中的图例数量应由实际清单计算，避免继承旧用例的固定数量措辞；本次只改一处报告键名，重跑后除键名外完全一致。


回归预测区间图应把逐例残差、保留并列值的排序、有限样本阶次和区间分开绑定。明确校准数与原文总样本数的转换；阶次越界须按所选来源展示无界结果，不能夹到最大残差或绘图窗口。参数改变同步数值、端点、候选纳入、箭头与图注；直接解释名义未覆盖参数，区分候选响应与缺失真值。默认插值分位数不能替代已声明的阶次规则。[三图模拟例及保留的失败](../tests/batches/split-conformal-rank-01/README.md)验证这一有限链条，不证明统计覆盖。实际渲染输入必须与规格来源哈希一致，而非只检查另一位置的同名文件。


普通原生文字跨SVG/PDF核对时，先区分设计锚点、左起点、字母基线、布局advance与墨迹bbox，比较同一种坐标。需要共享定位时可预先计算共同左起点/基线，并保留名义对齐锚点，避免各导出后端分别按不同字号度量计算居中偏移。[split-conformal文字修复](../tests/batches/split-conformal-text-anchors-01/README.md)在固定字体、单行非数学且无旋转的287个字符串上，以不变0.002pt阈值和实际单属性偏移对照支持这一做法。字体族fallback声明须对照实际原件核验，不把旧有列表误称新字体替换；仍需检查PDF嵌入字体并实际看图。共享原点/基线不承诺逐字形或浏览器相同，历史检查器失败和真实导出失败分别保留。


## 原生医学影像切面与可编辑覆盖层

用实际体素间距决定平面纵横比及共同物理比例，图像边缘位于首末体素中心外半个体素；十字线与标尺从同一坐标变换生成。表示重排后从实际新数组取切片，并同时更新仿射矩阵与点索引；保留斜切和空间身份限定。合法MR栅格可嵌入SVG/PDF，文字、十字线、方向和比例尺保持独立对象。

除全图视觉复看，还需解码实际嵌入栅格并按容器放置方向核对显示矩阵；PDF负向图像矩阵可能使原始XObject行序与页面相反。不要以源数组正确或预览看似相同代替该检查。本例灰度LUT曾使部分uint8像素降低1级，显式RGB灰度输入修复后按原逐像素标准验证；不据此声称所有色表都会出错。[出图与失败修复证据](../tests/batches/medical-volume-reindex-01/README.md)限定于该数据、窗口和记录的导出环境。


异形点标记的位置核查应比较共同定义的中心或锚点，不能把菱形较低的边界与圆形中心混比。先核对源坐标、身份键与页面变换；需要判断实际栅格偏移时再量取真实输出中心，单凭缩小预览的边缘高低不足以作确定错误指控。修复须同步权威显示坐标、派生绑定、图源和相关导出，保留原始记录及未涉及点。[空间坐标对照](../tests/batches/spatial-capture-identity-control-01/README.md)保留一个正确图误报族和建议覆盖不足，后续实际修复另列通过；此细化尚未另案例独立验证，不证明误报心理机制或一般检出准确率。


## 模型组变化与分段原生文字

改变模型分组时，沿预处理、潜变量、先验和噪声的组索引检查影响，再同步图、规格及图注。区分仍保留的样本/原条件元数据与真正参与模型的分组维度；不可因视图不变就沿用旧中心化结果、拟合参数或因子身份。[MOFA+局部配置图对](../tests/batches/mofa-grouping-transfer-01/delivery-01/README.md)提供一次实际双组→合并组的限定例证，不能泛化为所有似然或缺失模式的操作。

核对PDF字距时，检查源字体、实际/W及text操作符，再检查重新打开文件后解释器给出的字符原点。浮点字宽正确仍可能在连续排字中出现累计偏移。必要时按固定字体度量定位原生字符并保留片段/字符/科学ID对应，完整标签仍从源文件修改再导出；保留纯空格。报告文字提取的具体排序设置：本例sort=False删除新增换行后保持字符顺序，sort=True实际会重排并插入空格。逐字符定位没有验证所有编辑器的整段编辑、浏览器SVG或其他文字整形路径。


中心化图须标明输入是原始变换后X，还是旧分组内中心化Y，以及当前均值的计算范围。总体零均值不足以证明实现了指定的X中心化目标；完整观测下原组均值相等是本例的等价条件。只有旧Y且无原组偏移信息时，重复中心化不能恢复这些信息。修复时将“所需原始输入尚未提供/需取回”与“图源修改已完成”分别标注，依次同步输入身份、运算、活动依赖、可见标签、绑定和图注；原建议评分与后来实际修复分别报告。[有限对照与修复证据](../tests/batches/mofa-centering-control-01/README.md)不外推到缺失观测或其它变换。


显示目标要求位于指定处理器之后时，检查输出端口前驱和完整路径，并保留硬件处理、软件Source、处理器与显示Sink的角色区别；不能以模块名称推断频段、记录位置或运行效果。审图出现“如果这条额外支路……”时，仍先核实支路本身是否存在，再判断条件。单独复看可用于核实端点，初读误读及撤回各自保留。[Open Ephys对照](../tests/batches/open-ephys-signal-chain-01/README.md)支持本例的来源追踪与前提核查细化；读者修复建议覆盖不足和后来实际图源/绑定/图注同步分开报告，不回填评分或宣称普遍无误。


绘制已报告指标时，分别绑定数据集、方法/输入身份和metric字段，核对多级表头；源表顺序、报告精度、均值层级与未知离散度同时保留。少量类别可用不连线点及直接标值，截取坐标范围须明确，不能把视觉差距解释为显著性。字段修复从源CSV重新推导点、标签和绑定，并重放交付包。[MedMNIST有限例](../tests/batches/medmnist-reported-auc-01/README.md)保留纯图不可评估范围、后验字体oracle纠错及来源措辞勘误，不把原生一致当作科学正确。


区间图将“来源报告的统计对象”与数值/几何分开绑定：评价样本CI、训练运行SD/SE及模型集成各有不同层级。图上短标签与完整图注应从同一语义字段生成，修复该字段时同步绑定和导出，同时保留正确来源CSV、报告精度及端点；不以显示对称性替代来源定义。[CheXpert有限对照](../tests/batches/chexpert-reported-ci-01/README.md)以15个真实报告值验证了此闭环。原生字体资源检查应允许有依据的连字分子集，并核实每个子集实际映射/字形，而非仅放宽资源数；后验判据纠错须保留原失败和时序。


按阶段给模型参数实体和角色实例分别命名，再画谁产生何种输出。离线注释模型、推理生成模型与解码评分量不能因名称相近而合并。角色归属变化时，从一个权威语义字段同步端点、活动绑定、标签、图注和原生导出，保留未变条件与上下文。条件路线的视觉提示须注明只编码条件部分，不能冒充完整计算边；依赖分组也不自动规定时间顺序。[Self-RAG 有限对照](../tests/batches/selfrag-reflection-producer-01/README.md)提供一次实际修复和最终 ZIP 重放证据，原建议覆盖不足与执行通过分别记录。


### 参数状态与计算依赖的有限细化

按当前来源阶段分别核对跨步参数更新、前向/密度计算及求偏导的变量。冻结参数不自动删除经过它的计算或输入梯度；一次partial-z也不自动证明其他参数跨步冻结。状态符号、计算箭头和完整优化程序应按各自表达范围核查。状态修改从权威字段派生到标签、图注、规格和绑定，并检查非目标计算路径保留。见[multiDGD开发例](../tests/batches/multidgd-inference-update-01/README.md)：实际修复及ZIP重放支持本例，原读者建议不足和早期过强判断仍保留。

原生样式预期应分别固定实线/虚线的连接与端点属性，不以全局实线选项推定虚线行为；当前运行库的修复证据不外推到其他后端。新增细化尚未另案独立行为回归。


### 共同空间变换和监督目标

绘制合成图像—标签对时，从共同空间增强后的解剖变量分出强度生成与类别映射两条路径，再分别接入网络和监督。核对共同网格、空间对应和类别保留条件，避免以分辨率一致代替对应证明；未执行数组变换时只表述有依据的条件性后果。目标来源修改后，从同一权威字段同步路线端点、可见表达、规格、绑定与图注。训练使用合成强度与上游标签/验证影像来源分别说明。见[SynthSeg有限开发例及实际ZIP重放](../tests/batches/synthseg-target-alignment-01/README.md)，其评分遗漏和修复历史保留。

交付状态记录的活动证据路径须声明并验证相对于包内当前位置的解析基点。历史运行记录可保留原路径，但应明确是历史来源而非可移植依赖；在最终归档形成后实际解压执行，不能用打包前的新目录重放代替最终ZIP证据。


### 百分数显示与原始表格事实

将打印源值、精确内部比例和声明单位分开保存，从同一活动转换生成点位、数值标签、规格绑定和图注。两组值共用坐标时检查单位与显示倍率；不靠轴范围调整掩盖转换错误。保留源打印精度，少量类别可用不连线点与直接标值；统计分母、离散度和方法缩写各自按来源核对，不从数据划分或常见缩写补推。

[校准百分数实例](../tests/batches/calibration-percent-conversion-01/README.md)用20个真实报告值验证了单倍率修改的46叶同步、原生文本/点位及最终归档重放。两阶段阅读的不足与实际执行分开报告；这项细化尚未在另一独立任务中完成行为回归。最终ZIP之后的验收记录作为单独不可变证据，保留打包时pending快照，不反写历史。


## 状态分叉与原生绘制顺序：ECG 有限验证补充

当残差块有前处理状态与后处理状态两个输出时，把分叉落实到承载该状态的实际线段；核对分叉点、箭头端点、输出定义和跨块消费者，最后一块的未消费输出单独注明。整图覆盖须包括上层网络及完整展开块，不能仅靠局部结构正确替代整图核验。

原生检查同时核对形状和字形的绘制顺序；分别正确的两份清单仍可能让后绘背景或覆盖物遮住内容。声明支持的SVG属性／样式和字体描述符集合，检查实际嵌入字体与PDF实际使用的资源、字符代码、映射、字形和字宽。窄格式检查不称通用渲染器或安全验证；不支持的表示明确报错。

上述检查在[ECG修复图](../tests/batches/ecg-residual-state-01/native-audit-01/repaired-native-audit-01.json)实际运行，并由整图PNG／PDF查看补充。检查器加固在首次导出后、修复导出前完成；边界探针是内存XML和事件序列，不伪称端到端恶意PDF测试。最终交付另做真实ZIP解压→错误输入修复→导出重放，不能用打包前文件一致代替。见[重放记录](../tests/batches/ecg-residual-state-01/final-zip-replay-01/replay-readback.json)。

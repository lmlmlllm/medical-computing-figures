# 图文联合理解

先给出本图的一句科学任务与不能推出的结论；按当前图的依赖阅读，不用摘要代替方法。每条关键结论都能回到文件、版本、章节/页/面板或代码/输出字段。只报告可核查结论和依据，不需要输出内部推理过程。

## 科学对象与关系

- 区分患者、病灶、样本、图像、切片、细胞、特征、参数、预测、标签、损失与检索证据。核对别名、单位、分母与分析单位。
- 关系记录起止、类型、方向/无方向、条件、阶段、层级和来源。数据流、计算依赖、监督、优化、时间、组成、分组、邻近、关联、激活/抑制、因果、证据支持、假说不可混为一类。
- 先看原图图例和正文再解释箭头/虚线/颜色。相邻不等于证明，分类不等于谱系，空间邻近/解释热图不等于因果机制。无依据连线不能仅改成虚线就进入正式稿。
- 图中可见、图注明确、正文支持、代码支持、输出核验、作者解释、执行者推断、冲突与不足分别记录。读取代码不等于运行；运行不等于核对输出。
- 两方向检查：材料要求什么，图是否准确表达；读者仅看实际渲染和图例会理解什么，来源是否支持。科学逻辑和视觉质量单独验收。

涉及“未展示、已省略、没有结果”的主张时，绑定具体图号、面板和结果形式，并实际查看相关图；轨迹未展示不自动意味着汇总条也不存在。正文、图例与可见结果不一致时，保留冲突及影响，不凭标签补出运行成功数、容差设置或数据归属。[HIL来源限定修订](../tests/batches/hil-controller-boundaries-01/README.md)将Fig8轨迹与Fig9B汇总条分开表达。此为有限案例后的操作规则，尚未在另一论文独立验证。

## 任务特异核对

**研究设计**：来源、纳排、标注、层级、时间、分割和拟合边界必须按真实设计画；泄漏风险指出而不私自改成理想流程。内/外/时间验证按实际设计命名。

沿着“抽样来源→患者划分→选取一次检查→具体比较子集”核对每个N；百分比分配不自动给出筛选后的整数人数。一人一次测试检查不意味着训练也只有一次；多个读者重复评估同一病例不增加独立患者数。原文train/tune标签即使比例不常见也不能自行交换。记录测试被留出的原文声明，与实际核验患者不重叠分开；不同国家不自动意味着模型没接触过该国开发数据。

结局阳性时间窗与阴性纳入所需随访条件分别核对，保留“未活检”“从未阳性”等适用人群。缺少读片意见或技术质量筛选会改变比较分母，不能把完整测试集N转贴到每个结果面板。数量冲突先核对版本；无法消解时保留来源原数与矛盾，展示有依据的最终队列不等于已还原完整纳排账目。

**架构/优化**：输入表示、共享/独立参数、融合位置、算子接口、冻结/更新、训练/推理；concat与逐元素操作不同。标签→损失→更新不能变成部署依赖。未知张量形状/轴不补齐。保留决定核心创新的模块。

解释关键推导时，分清精确恒等式、局部近似与额外假设；核对实际忽略的项及其成立条件，不用泛称“近似”替代具体论证缺口。固定部分变量的精确子问题解，只支持该子问题，不能据此外推整体目标的等价最小化、下降或收敛。[MoDL 修正实例](../tests/host/modl-three-figure-02/README.md)保留初次交叉项遗漏及后续限定。

**类条件校准与预测集合**：把模型拟合、校准和推理分别画出。校准真值可用于选择对应类别的参考分组；固定模型分别产生校准分数与测试候选类别分数。不能因为校准使用标签，就把测试真值连入推理；测试真值的事后评价依赖另列。类 p 值不自动是类别概率，也不要求和为一。

集合基数处置与真值排除的覆盖错误分开：单元素是候选，未必正确；多元素是备选标签，不是并发诊断；空集不含任何标签，是覆盖失败，但不单独证明分布外输入。若来源展示分类用到真值，不能将这些分类当成部署时可见状态。对补充公式与代码的计数、并列、自身贡献或版本冲突逐项保留，不能只换分数正负方向就称已消解。名义置信参数、经验覆盖与临床保证分别表述。

**生成与采样**：先分开表示模型训练、噪声预测训练和固定参数生成，逐阶段核对冻结与更新。自编码器后验采样、训练时已知的扰动噪声、生成初始潜变量及可能存在的逐步采样噪声是不同对象，不能共用标签或监督箭头。

噪声预测并不自动等于更新后的潜状态；采样器还可能依赖当前状态和调度参数。沿迭代反馈追到循环终点，确认解码器接收的是哪一个实际对象。固定参数操作不意味着没有随机性，某个采样器名称也不足以证明具体实验为确定性生成。代码默认值只属于被读版本，未核实的实验配置、检查点对应及正文/图注冲突继续保留；不同数据集上的方法不自动构成同一患者的联合多模态输入。

**图计算与读出**：节点特征、邻接/边信息、逐层节点状态与整图表示分别标明。邻居聚合更新节点状态，不自动产生一个整图向量；全局读出须核对约简的是节点轴还是每个节点的特征轴。把原子节点数N与特征宽度C/F、分子数及患者数分开，嵌入的每位置维数也不能贴到最终序列向量。

原文列出的多种GNN可能是备选模型；先固定具体变体，再核对该变体的层数、非线性和读出，不能拼接其他变体的配置。图中省略号与正文层数可属抽象差异，但图漏画的操作仍须核对。论文明确声明的局限（例如未考虑立体化学）应保留为来源事实；尚未检查的实现细节继续标为未知，不因代码未审计而将已有文字证据也抹成未知。

**RAG/GraphRAG**：语料处理、索引/图谱构建、查询、检索、排序（若实施）、上下文、生成和评价；语料、训练数据、测试问题分别标清。离线/在线按实现判断，动态构建允许。向量检索≠图谱检索≠GNN。命中、引用存在、答案正确分别评价。

**评价总体、支持方向与条件分母**：逐项声明计数总体、参考对象和支持方向。响应声明、参考声明、检索块不能互换；双向支持不意味着同一“正确”交集。条件利用率的分母只含已被检索支持的参考声明。可能重叠的噪声类别不能画成互斥分割或直接相加；忠实于上下文不等于参考正确，也不证明内部因果来源。按正式定义核对，未知实现不补默认值。见 [RAGChecker 有限迁移](../tests/batches/ragchecker-evidence-metrics-01/README.md)。

**条件路由与执行层次**：分别核对论文的算法选择概念、实现中的实际调用顺序，以及离线评估对预计算答案的选择。缓存选择脚本可证明类别到已有答案的映射，不能单独证明在线请求只调用一个后端。策略类别、原图面板字母和模型输出标签分别命名；有局部交叉引用错误时保留冲突，使用明确策略名定位。

区分当前问题、路由决策、离线参考答案及训练监督。多条候选路径是否互斥必须有依据，不能把示例问题的并列看成同一问题全部执行；参考答案被保存用于评价，也不意味着进入推理模型。上下文回路只画已支持的信息与终止条件，不能补固定轮数或全历史。论文描述的失败回填与代码的独立标签池合并也须分开，不将固定提交认作已核实的实验运行。[rag-routing-01](../tests/batches/rag-routing-01/README.md)只验证部分来源支持的关系和有限图稿测试。

**联邦与分布式训练**：站点内的数据保管、跨站点的参数/更新、验证分数及执行顺序分别核对。箭头先到验证节点再以时间线连到训练时，仍须明确本地训练是否使用收到的模型。消息的来源/目的地与实际发送时机不同，不能从图的纵向位置推断发送顺序。聚合权重须按来源定义，不把本地迭代数自动改为患者数。

区分当前、更新后、最终和最佳模型；核对哪个候选被哪个验证分数选择，以及测试发生在何时。多结局窗口不自动意味着一个共享双输出模型。部分检查点身份已知时保留已知部分，未知范围只覆盖未明确的站点或阶段。局部数据保管、传输加密、锁图标及部分更新研究均不能单独证明形式化隐私保证；不要把尚未说明的统计拟合子集或传输通路补成理想化协议。

按参数族分别核对本地更新、聚合资格、同步赋值与副本身份：不参与平均不等于冻结，共同赋值也不等于各客户端在同步之间始终是同一参数实体。可学习参数、计算得到的统计量和优化器状态分开；SGD名称不能证明无状态。共享或保留规则须限定训练/测试阶段，不能把训练期排除规则扩张为所有阶段从不共享。实现未说明的运行统计、计数器、重置和通信路径继续保留未知。[FedBN参数族图](../tests/batches/fedbn-parameter-ownership-01/README.md)支持这条有限归纳。

**多视角/模态/组学**：同人/同样本对应、跨层级对齐、融合位置、缺失输入条件。视角不自动成为不同模态。细胞不是生物学重复；表达、空间、降维坐标区分；探索聚集不能画成已验证机制。

对于人工解除配对或模态遮蔽，分别记录原始生物对象、派生记录、各记录的可用模态和构造输入池。派生记录不增加独立生物学重复；某条记录缺失模态不等于其同源观测已从整个数据池删除。优化/验证成员、推断输入与评价参考分别核查；成员未知时不推定独立留出，也不直接判定泄漏。整块缺失的占位零、测量零和模型估计保持不同状态。见[MultiVI限定解释图](../tests/batches/multivi-missingness-01/README.md)。

**跨模态匹配与矩阵方向**：分开原始采集配对、训练时采样、标签构造的相似度和模型嵌入产生的预测。无原始配对要求不等于无标签监督；全组合对数不等于独立患者数，训练批次的对角线也不自动是唯一正例。实际输入若为报告句子，不要把整份报告与一句文本混为同一分析单位。

先写明矩阵的行、列和每方向锚点，再核对相似度到概率的算子轴。反向分布通常需要先转置分数、再归一化，不能直接转置正向概率；两个方向的损失各按自己的锚点分母聚合。正文的标签余弦、代码的标签点积、注释声称的裁剪以及实际执行路径分别核查，不用“都是相似度”合并。图、正文、固定提交及真实运行身份不一致时，明确当前图依据哪一条局部路径，同时保留未解决的差异。[multimodal-contrastive-01](../tests/batches/multimodal-contrastive-01/README.md)只验证固定代码片段的静态含义和自编模拟代数，没有重跑MedCLIP或证明全文方法一致。

**计算扰动与实验支持**：候选网络、表达拟合后的预测关系、计算干预和实际实验读出分层表达。motif或可及性支持的方向不等于每条直接调控边已实验证实；拟合系数也不能直接改名为已证实机制。使用所画具体应用的输入，不能把总览里的多组学输入复制到只使用启动子先验的应用。

按实现区分表达变化量与绝对表达、固定的干预输入、计算传播及投影所依赖的观察数据。预测局部状态方向不等于直接追踪细胞谱系；保留细胞状态/发育阶段限定，不能把早期效应推广到全部阶段。独立实验的细胞组成或标志物读出支持到哪个表型，就把证据关系连接到该表型比较；不要回连成整个网络通过验证或既有模型的训练输入。图示已发表计算模拟时标明来源及预测性质；本地新造的测试数据另按模拟测试管理。

**信号/工程**：物理采集、变换、软件与操作分开；采样率/窗长/单位/设备方向/控制反馈要有来源。原型或仿真不能变成已验证临床闭环。

**结果**：每个系列/掩膜/解释图追溯到输入、模型版本和实际输出。核对比较队列、统计单位、分母、重复测量、误差含义和不确定性。只有汇总数值时不补统计推断。需要新分析则指出缺口；未经授权不重跑训练或研究。

工作量图先核对计数对象和纳入范围：同一参与者可以对应多次操作，总数可能包含复核或共识环节。缺少完整记录时，不用“人数×固定次数”替代来源总数，也不按差额编造组成；操作减少不能直接换算时间、人员或成本。按分配组分析与实际接受流程分别记录，交叉或故障不自动改变原分析组。并列面板可共享组身份，但操作次数和每人率须各用明确单位。源表单位与正文冲突时保留原标签，并依据方法、结果和独立出处确定展示尺度，不能只复制百分号。见[MASAI汇总结果图](../tests/batches/masai-workload-01/README.md)；该图仅检验13个报告值，没有验证操作计时或试验效果。

**解释与归因**：预测输出、解释图及其评价参照是不同对象。标出解释方法实际需要的输入、模型访问和阶段；不能把所有方法画成只由预测标量生成热图。解释分数的归一化或概率含义必须有依据；缺少真实输出时只画明确的对象/运算关系，不合成研究热图。

区分定位、模型权重敏感性、同架构重复性和跨架构一致性。逐项核对比较对象、统计单位、基线与期望方向：随机化权重后图仍相似，与重复训练后图保持相似，回答不同问题，不能共用“越高越好”结论。来源的操作性通过标准如“无显著差异”须如实归属，不扩写为统计等价证明或临床有效性；图中示例不代表发生率。ROI是指定任务的评价参照，框内像素也不等于精确病灶边界；定位吻合不能单独证明因果机制、完整模型忠实性或患者获益。

## 处理不足与冲突

先比较版本、阶段和抽象层级，仍矛盾则保留冲突和影响。未知关系标为 undecidable，不能计正确。可完成有据部分或清楚标识的局部草稿。无原始编辑源时交付称“从原图重建”，不能称“修改原始图源”。


## 条件反馈与报告边界

闭环图分别追踪传感／测量、数据传输、控制命令、物理供能和刺激作用。实验观察不自动成为反馈输入；手工改变实验状态不自动成为控制器的人工覆盖。按原图逐条保留阈值方向、开关条件和返回路径，正文示例时长不能替代未知的执行调度。离体人组织实验、活体原型与临床使用分开；缺少关键补充方法时可完成已支持的功能图，但案例保持部分语义核验。

持续预测与允许更新是不同条件。当前系数、转移矩阵及模型内部历史不等于目标标签或生理测量；提示停止后能否继续用模型，应按原文核查。分别追踪连续控制输出、用于评价的状态、EMG刺激标定和EMG响应评价，不能因波形对齐就补出自动误差反馈。每个时标紧邻其操作，区分采集、预测、命令更新、参数更新批次、脉冲与总延迟。见[脑—脊髓接口限定图](../tests/batches/brain-spine-interface-01/README.md)，实现未知继续保留。

区分“未报告”和“未实施”。例如来源描述按观察位置分组，不足以断言已经证明没有随机化；写成“所读来源未报告随机位置干预”，同时保留积极可核实的分组事实。来源正文概括与实际曲线局部变化有张力时，两者并列定位，不用未知幅度抹去可见方向。

## 真实波形的校准与时序

将原始数字值、头文件增益/基线、换算后物理量、图上坐标和可见单位连成可核查链条。按具体格式核对端序、交织顺序、导联身份、缺失值及适用的初值/校验和；不要假定基线为零或所有通道同增益。保存来源版本和原始字节，明确本地做了哪些变换。发布数据采样率与设备原始采样率分开，已发布重采样数据不能称为未经处理的原始采集。

以真实采样时间定位数据。N/fs 的名义时长与最后一个样本的 (N−1)/fs 不同；多个并发导联不能画成先后发生或不同受试者。显示单位变化须同时换算数值与刻度；正确图注不能补救图内 mV/µV 标签冲突。图上平直段或其他可疑形态先回查输入，再区分来源特征、显示问题及上游成因未知，不凭形状作临床解释。

## 局部窗口与时间原点

同一连续记录的局部展开要核对原始样本索引、半开区间、原记录时间和窗口内时间。用整数索引及实际采样率定义坐标，明确原点关系；窗口相对0秒不表示新记录或独立重复。局部图共享同一批幅值时，仅横轴平移不能暗示重采样、幅值归一化或新事件。换窗属于数据成员变化，相关高亮范围、括号、绝对刻度、原点、标签与图注必须随之更新。区分任务指定选择与来源实际检出的事件，不赋予任意窗临床含义。

## 真实图像与像素标注

以具体 TIFF 的位深、黑白极性和方向核对解码，网站概述不能替代成员元数据。人工边界像素、填充实例标签与模型预测分别定义；保留字面图像值，图像与标注共用裁剪、方向及像素中心／外缘约定。换窗时同步局部原点平移、ROI、坐标标签与图注。打印 DPI 不提供物理像素校准，不能据此添加 µm 比例尺。

## 描述性生存与行政截止

先核对记录时间、事件编码、进入约定及已知删失信息；未知临床零点不能改名为入院或治疗开始。任务定义截止 τ 时，声明 `T*=min(T,τ)`、`E*=E 且 T<=τ`，恰在 τ 的事件仍保留，`T>τ` 的行政删失与保留的来源删失分开。死亡／删失同刻共用退出前风险集；“t 前在险”与“累计至 t（含 t）”是不同计数约定，截止前在险数不必等于行政删失数。显示重现和来源文中已公布结果不建立非信息删失、死因裁定或临床有效性；同一队列换截止不变成独立分组或新的治疗比较。

## 蛋白矩阵的测量层级与来源尺度

先分清完整测量 ID、源个体／样本组和技术重复，保留非数字 ID 与源顺序。测量行数不是独立生物样本数；后缀的具体重复、稀释或时间含义未建立时保留未知。核对字段后缀、单位和上游处理的来源，不把 `_N` 自动解释为标准化。选择字段或补充真实缺失覆盖时披露选择目的，不把技术切片包装为生物差异筛选。

源值、缺失掩码和显示舍入分别保留。未知处理不补写为已归一化；缺失不当作零或推断的机制。固定同一来源尺度的跨版本比较时，共有单元应保持源值与色彩含义；同色标不证明跨蛋白绝对丰度可比、统计显著或机制成立。[protein-matrix-01](../tests/batches/protein-matrix-01/README.md)仅验证一张公开表的有限显示。

## 空间支撑、注意力和分支剪枝

空间物理坐标产生的邻接支撑、表达特征、可学习注意力及加权聚合分别核对。半径邻接可为无向，行归一化注意力不必对称；`(T M)_i`接收邻居j的信息，不能据A的无向性把聚合也画成无方向。spot不必等于单细胞，PCA/UMAP不等于组织坐标；代码另有KNN路径时不能把半径路径的对称性外推过去。

预聚类标签、人工细胞类型真值及下游空间域聚类是不同对象。可选分支只删除其支撑中的跨标签边时，保留所有节点、自环以及另一完整分支；不能暗示整个模型阻断了跨标签信息。分别声明共享特征、独立注意力参数、编码器权重的转置绑定和注意力复用。移除分支须同步融合式、条件和专属依赖。

固定代码前向与论文公式不一致时，注明当前图采用哪一版本，保留损失、末层激活、默认参数和实际运行身份的冲突。训练内重构、保存前截零及下游应用分开；单切片示意不能直接推出3D重建或临床效用。[MCF019-F1](../cases/MCF019-stagate/MCF019-F1.json)仍为部分语义核验。


## 配置、模型拟合与经验选择

先区分数据集层面的固定设计和推断配置、训练得到的参数、折外验证证据与最终推断输入。规则生成配置不等于学习网络权重。核对所有候选是否总会训练、条件分支的触发标准，以及选择分数是否同时被当成独立评价。折模型集成与不同配置集成分别定位。若原文先在整个训练集计算数据集统计，不将其改画成每折独立拟合；若当前代码已重写，不用其名称证明旧论文运行。预印本和期刊版的图号、方法与结果范围分别记录。见[配置流程实例](../tests/batches/configuration-planning-01/README.md)。


## 标注数据引擎中的模型版本与质量依据

解释“模型—数据—训练”循环前，逐阶段确认是谁标注、哪些数据训练哪个版本、哪些掩膜进入发布集合。自动数据生成器与使用已生成数据训练的后续模型可以不同；不能因总览画成循环，就补上发布数据训练生成它的模型这一条边。将自动置信评分、稳定性、人工修正后的实测比较分开，标明抽样单位及统计分母。若质量程序也指导阈值选择，而来源没有给样本独立性证据，保留这一缺口，不标成独立测试或全量人工认证。见[SAM数据引擎实例](../tests/batches/annotation-engine-01/README.md)；规则适用于有真实阶段与来源支持的标注、伪标签和质量流程。


## 运算轴、共享轴与运算的作用范围

张量方法图应分别记录输入/输出轴顺序、算子混合的轴，以及参数在哪些切片或模块实例间共享。转置改变轴位置，需要同步更新后续算子与形状标签；相同模块名或形状不能证明跨层共享参数。用原图、公式和对应版本代码核对，而非套用某个网络的默认结构。若子运算按切片独立应用、前置归一化却使用其它切片的统计量，把独立性限定在该子运算，不扩大到整块。见[MLP-Mixer限定实例](../tests/batches/axis-mixing-01/README.md)；其完整训练正则化不在核验范围。


## 离散决策分析结果与区间身份

先区分点估计、重采样均值、边际区间和配对差值区间。只有几个阈值的汇总表时，仅绘制这些点及其来源区间，不补成连续曲线；不同阈值改变损益权重，不是时间过程。净获益可为负，None=0与Full−比较策略=0是不同参照。对显示为0.0000的端点保留舍入边界，不自动称为严格正值。配对差值采用来源报告值，不能用舍入列或边际区间端点相减替代。[decision-curve-01](../tests/batches/decision-curve-01/README.md)验证了这些有限数据映射边界。


## 时频数量与单位身份

由信号校准、窗函数、DFT约定、单双边处理和归一化共同确定谱的数量与单位。PSD、幅度和幅度谱密度不能只换色条标签；单边处理核对DC/Nyquist与内部频点。dB写明10或20倍对数、参考量、数值下限和色域饱和。对非平稳信号，加窗Parseval比较同一加权均方，不能据此声称原始均方不变。只有热图或缺少校准/归一化材料时，相关单位与量值保持不可判定。[signal-timefreq-01](../tests/batches/signal-timefreq-01/README.md)验证了一个真实记录上的有限变换与两个归一化反例。


## 注意力分数、允许集合与值向量

分开 Q/K 的特征宽度、键数量、查询位置和 V 的值轴，再核对缩放及 softmax 归一化集合。逐查询的键权重与沿查询归一化不同；允许集合改变时重新计算权重和输出，不能只把旧概率置零。掩码位于 logits 还是归一化之后须有明确证据，核对对角及全屏蔽行处理。完整解码器的输入右移与局部因果掩码分别说明，不把一个算子画成完整模型；多头投影/拼接不能凭层叠外观自动补入。A 是值权重，O 是值空间向量，不自动是类别概率或机制解释。[attention-core-01](../tests/batches/attention-core-01/README.md)只验证固定模拟数组的单头核及三类已知错误。


## 空间尺寸、裁剪与通道融合

把C与H/W分别追踪；卷积、池化、上采样/上卷积的核、步幅、padding及通道映射须由当前来源支持。裁剪保留C，拼接要求其余轴一致并累加C，逐元素相加保留C，三者不能替换名称。输入变化沿所有主干和跳跃分支传播，重新核对裁剪端点及最终投影；1×1投影不能自动恢复旧尺寸。保留瓶颈入口和后续卷积输出的不同状态，不用一个尺寸覆盖整块。来源特定的偶数池化要求不推广为所有U-Net的限制。局部中心裁剪约定与作者代码偏移、完整坐标对齐分开；最终类别特征、概率与实际标签掩膜也分开。[segmentation-shapes-01](../tests/batches/segmentation-shapes-01/README.md)只验证整数接口及小型模拟索引。


## 效应量身份与比较方向

分别核对事件数、原始比例与模型估计量；从分子分母可算出的风险比不能替代已调整Cox估计。写明结局时间、组别方向、调整、区间含义及来源版本。反向比较使用1/r及[1/upper,1/lower]，同步列顺序与有利方向；从已四舍五入的汇总值取倒数须披露，不能称为重拟合。总体与其亚组的成员重叠，不能作为新的独立组或再次合并。原图按统计信息加权的方块大小缺少具体权重时，可采用披露的等大标记，不能从事件数或区间宽度臆造权重。[RECOVERY有限汇总示例](../tests/batches/effect-estimates-01/README.md)同时保留初步/最终版本区别和未绘制的正文数值冲突。


## 单细胞矩阵的归组与生物学重复

同时核对cellID、原始样本、条件、细胞类型和输出组。先按明确ID对齐元数据，再按来源支持的层级聚合；不能把行序相同当成样本对应。保留样本身份的伪bulk与重分配后形成的伪重复是不同对象，即使两者都有相同列数和每列细胞数。缺少样本标识时，条件、细胞数和矩阵外观不能补出独立重复数。也不能把所有细胞级模型一概称为忽略样本：混合模型可能显式建模重复。[有限模拟例](../tests/batches/pseudobulk-units-01/README.md)读取了固定提交的聚合/重排代码，未执行差异表达分析。


## 测量一致性的配对身份、方向和误差定义

先以来源ID核对同一对象的两种测量，再确定使用哪次读数；文件行序、重复读数和独立对象数不能互相替代。写清差值是A−B还是B−A，使点位、轴标签、界限和“高于/低于”解释一致。总体均值不变仍可能掩盖错配造成的SD、界限和个体点位变化。

mean±2SD、mean±2SE、均值置信区间和界限本身的置信区间是不同对象。保留来源的乘数与估计口径，不自动把2改成1.96。样本量和均值不能补出个体点或SD；缺少材料时界限保持不可判定。示范数据和一张差值图不建立正态性、临床接受阈值或器械可互换性。见[公开配对数据开发例](../tests/batches/measurement-agreement-01/README.md)。


## 记忆读取、替换与证据实际缺失

先区分持久记忆库、当前查询的临时抽样、记忆负载／位置编码、读取键和写入比较特征；它们都叫embedding时也不能合并。记忆库容量K、批大小B和抽样槽数分别追溯。重复抽中同一ID仍是同一记忆项，不增加独立个体或自动复制持久库。

沿执行顺序核对先读后写，以及完整批次中的第几个候选更新；当前解码后才产生的新记忆不能回填成当前查询已经使用的输入。相对置信阈值须指出比较对象和预测来源，保留相似度与置信度两项条件及严格边界。论文公式与固定代码不同，明确图依据哪一版本，不混拼成已验证的原方法。

材料不足测试应核对实际交付的输入和所有依赖，不能仅隐藏标签或把参数设空，而继续附带能够提供该值的原输入。保留可知部分，缺失所影响的判定和结果继续不可判定。[本批R14](../tests/batches/memory-selection-01/README.md)记录了此类首次失败及实际删字段后的修复。


## 校准分箱、条件分母与样本支持

核对预测/结局的配对键、分析单位、时间窗和共同样本。分箱要明确边界闭合规则、空箱策略、横坐标是均值还是中点，以及观测率的箱内分母。零个样本没有可估计事件率，不能与非空箱的零事件混同。实现中的参数名字不保证实际生效；沿真正的绘图字段检查。

曲线因分箱变化不表示预测模型或性能改善。把点与成员记录、数量一一映射，注明连接线只是描述性连接。材料不足须实际移除结局，同时核对页眉、图注和各面板；局部unknown文字不能抵消另一处虚称已知的标签。参见[校准批次](../tests/batches/calibration-binning-01/README.md)。

## Monotone calibration and inferential targets (MCF030-F2 follow-up)
Distinguish unchanged forecast probabilities, paired observed outcomes, a same-sample isotonic estimate, a calibration-null consistency band, and an estimate-centred confidence band. Read the actual resampling order, support handling, finite-replicate denominator, quantile convention and boundary correction. Pointwise bands are not simultaneous bands; a displayed level does not establish observed coverage or independence. If observations are absent, fitted PAV, its confidence band and empirical score terms are unknown. A null consistency band may still be constructible from forecast probabilities under its stated calibration model; do not claim all uncertainty construction logically requires observed outcomes.
For empirical Brier decomposition preserve S=MCB−DSC+UNC, MCB=S−SC and DSC=UNC−SC. Same-sample PAV improvement does not demonstrate external performance. Trace repeated/tied forecasts through weighted grouping and maximal constant blocks. See [CORP source and test scope](../tests/batches/calibration-isotonic-01/DELIVERY.md).

## Source-version identity and conformal rank construction
A resolved release tag does not prove exact archived bytes or which run generated a paper result. Keep a documented disagreement when class strata, tie smoothing, numerator self terms or threshold conventions differ. State score polarity and compare complete formulas: reversing probability to nonconformity alone cannot erase a self/tie discrepancy. Interpret p-values as classwise tests rather than a normalized probability vector. True calibration labels select the reference strata; true test labels enter optional evaluation only. [Executed source-aware example](../tests/batches/conformal-version-01/DELIVERY.md) retains its source-partial status.

## 混淆矩阵的坐标、分母与重复标注
先从源表和更正记录核对真实类别轴、预测／赋值类别轴及类别顺序。行归一化与列归一化改变条件问题，不能只换色标标签。计数单位可能是序列输出间隔或其重复标注；记录、患者和独立观测数不能互相替代。汇总读者计数不提供个人矩阵、平均F1、方差或多数票结果。来源图注与Methods单位冲突时保留差异，明确本地图采用的有据解释和自行声明的分母，不据颜色相似就声称复现原绘图实现。见[有限真实源表适配](../tests/batches/confusion-matrix-01/DELIVERY.md)。

## ROC/PR：阈值、并列分数与条件分母
先确认分数方向、正类、分析单位、阈值包含规则与每类支持量。同分数必须作为一个阈值组进入；组内分数位置或TP/FP混合点不是额外可达到的确定性阈值。ROC的FP/N、TP/P与PR的TP/P、TP/(TP+FP)回答不同条件问题。零预测阳性时precision未定义，绘图端点约定不能当观察值。类别内恒定权重可保持ROC而改变PR和P/(P+N)基线；权重和原始行数分别写明，不把新权重称作新增样本或未来人群验证。见[有限示例](../tests/batches/precision-recall-01/DELIVERY.md)。

## Coordinate maps and training-only branches

Before explaining registration arrows, name map domain/codomain, displacement versus coordinates, component order, positive directions and units. A pull-sampling location is not a forward displacement of a visible object. Retain scientific preconditions such as affine alignment, and distinguish training-loss inputs from network inputs. Smoothness does not itself establish invertibility. See [tested scope](../tests/batches/registration-warp-01/transfer-rules.md).

Graph diffusion: distinguish distinct-passage frequency, seed reset weights, one update, stationary mass and count-weighted raw document scores. Correct final ranks do not establish correct intermediates: a nonseed specificity error may leave ranks unchanged. Locate offline extraction/synonymy and online query linking separately; read code version and invocation before equating implementation defaults to published tuned values.

Local kinetics: separate stored variable order, plotted coordinate order and derivative order. For horizontal spliced s and vertical unspliced u, vectors are(ds,du); RNA velocity is the spliced component. A component nullcline is not a trajectory, and a zero component is not a full stationary state. Source state-switch notation conflicts may leave trajectory formulas unresolved while unambiguous local equations still support a bounded exercise.

For sampled multichannel systems, separate common event/travel time from channel-local recording time. Subtract each recording start before converting delay to a sample index; establish units and indexing. A timing-control edge is not a transported waveform. Source schematic channels, device elements and own test channels are distinct counts. A signed scalar sum does not establish image formation or clinical performance.

For competing first events, define allowed transitions and the estimand before plotting. An absorbing endpoint classifies first-event history; it does not forbid later biological events. Censoring is not another disease state. Distinguish unconditional CIF from cause-specific1−KM. Rounded same-month ordering may follow a source coding convention without identifying true sequence.

Attribution requires a specified scalar output, baseline and path. Completeness constrains the signed sum to F(input)−F(baseline), not necessarily F(input), and does not identify each component. A low-output baseline is not automatically medically meaningful. A printed equation can conflict with elementary algebra; preserve that conflict rather than treating publication as a numerical oracle.

For bulk deconvolution, distinguish cell fractions, RNA fractions, size proxies and raw regression coefficients. A size-scaled reference and coefficient closure define the displayed estimand; sum-to-one and a small residual alone cannot verify it. Preserve gene/type joins, complete versus selected gene universe and assumptions linking library size to RNA content. Source code version is separate from the original publication version.

For embedding methods, distinguish conditional probabilities, symmetric joint similarities, globally normalized map kernels, scalar pair contributions, vector gradients and signed updates. A sum-to-one check does not establish the intended symmetry or normalization domain. Preserve paper/code sign conflicts; a local derivative check supports its tested convention without proving the whole optimizer or biological meaning of a map.

## Partial transport and downstream geometry

For partial matching, identify coupling entries as transported mass, its row/column capacity inequalities and the total transported mass. A nonnegative coupling is not automatically a confidence matrix or a required one-to-one assignment; a particular feasible solution may nevertheless be sparse or one-to-one. Keep the objective's cost-mixing weight distinct from its overlap/mass parameter. Separate expression, physical coordinates, within-slice distances and the coupling. Alignment into a common coordinate system and optional display-axis assignment are later operations with their own assumptions; feasibility of a zero-mass coupling does not establish a defined downstream projection. The [PASTE2 example](../tests/batches/paste2-partial-coupling-01/README.md) supports this bounded interpretation while preserving unread supplementary formulas and implementation limits.


## 概率、实现与训练替代对象

分别标明学习参数、概率、离散实现和连续训练替代量。约束概率的均值可推导期望数量，但不能据此画成每次离散实现的精确数量，也不能直接约束连续替代量的均值。训练时可微的对象、最终离散对象和后续重训练是不同阶段；来源未给出选择、冻结或初始化规则时，不用一条连接补成完整算法。[LOUPE 有限案例](../tests/batches/loupe-sampling-01/README.md)保留这些未知，没有生成 MRI 或数值掩膜。


## 分类条件、返回集合与上下文

当一个预测条件控制返回对象时，先确定它是否也是分类头输入、损失条件或执行调度依据；来源只规定解码条件，不能自动增加头到头的输入边或跳过计算的时间顺序。共同编码的上下文与最后返回的证据成员分别建模，未被选入返回集合的内容仍可能参与编码。阈值、分支与回退必须连同适用条件表达：严格大于不能改成大于等于，全部合格项不能改成单项，空集合回退不能扩展到其他分支；来源未说明的并列、空输入或截断规则保留未知。MultiVerS 的给定 claim–abstract 示例见 [限定测试](tested-rules.md)，不据此认定返回证据有因果忠实性或临床有效性。


### 条件选择、单项损失与完整更新

当多个候选预测头汇合到一个训练输出时，用选择条件或明确公式说明返回哪一项；不能让读者将汇合误读为求和或融合。区分单样本事实损失直接更新的头、共享表示引起的间接预测变化，以及完整目标中的全局正则项。推理中的两头差值还须给出同一输入、固定参数、相减方向与估计对象；条件均值差不能换成已观测的个体潜在结果差。因果识别和定理适用条件须独立于优化结果。该规则在TARNet/CFR限定解释图中验证，未验证其他模型或真实因果分析。


### 首次达阈事件与潜在评估负担

阈值结果图除分母外，还要保留事件计数的规则：一段住院期间首次满足条件、所有达阈住院和每次模型输出不是同一数量。回顾性首次达阈策略能支持潜在评估量，不能直接变成已发送报警、重复报警次数、临床响应或人员耗时。NNE等已报告指标须保留发表更正与源单位措辞，不从四舍五入PPV反推精确值或声称跨重复住院均为独立人员。该条件规则在ESM已报告汇总量图中验证，未验证临床部署或原模型实现。


### 条件区间与先前状态依赖

同一输入区间可以对应固定输出，也可以要求保留先前状态。比较两者时，应在相同输入条件下分别给出已知先前状态及其保留结果；中间输入区间不能自动画成中间输出、零值或关闭。标明这些是条件性备选情形，不能让排列或箭头暗示一条实际时间轨迹。输出选择与连续物理执行分开；等号、启动、缺输入、未完成斜坡和操作顺序未说明时继续保留未知，来源中的时间公式冲突也不由绘图自行修复。该区别在 [aDBS限定图](../tests/batches/adbs-state-buffer-01/README.md)中核验，未执行控制器或验证临床效果。


### 条件误差的坐标角色与叠加证据

先写出被评分位置和用于对齐的参考坐标系，再解释矩阵横纵轴；文献符号与界面坐标按角色对应，不能据此推定代码转置。交换两个角色时误差可不相等；在两处显示同一约束也不证明底层量对称。期望位置误差、结构内物理距离、局部置信度、类别覆盖层和特定实验试剂的满足判据应分别命名。单条约束满足不能升级为整个结构正确。见[PAE参考坐标系案例](../tests/batches/pae-reference-frame-01/README.md)；原文高低含义冲突、运行身份和原始数值缺口保留，新规则文字尚未在另一案例独立回归。


### 有向采样、测度权重与阈值角色

先区分被计量的对象、采样方向及聚合方式，再连接距离列表和最终分数。来自两侧的有向距离可以不同；对称总分不意味着两个方向相等，接受的表面元素须携带自身面积，不能自动按点数或两个比例的简单平均计算。距离容差与分数截点分别标明单位、来源和用途；参考标注是指定流程产生的比较标准，未标注区域不等于空区域。见[分割指标限定案例](../tests/batches/surface-metric-roles-01/README.md)；图注补足的简写不能脱离图注单独迁移，来源冲突与数值实现未知保留。新规则文字尚未在另一案例独立回归。


### 估计、依赖人群的映射与显示

固定的上游估计不保证下游图形固定：先区分估计值、候选人群与邻接/转移权重、低维映射及后续插值显示，逐阶段说明子集变化会重算哪些量。相同对象在两个条件下重复比较，应保留共同对象身份，不能累加成独立样本；局部区域的方向也不能推广到全图。源内符号、归一化或平滑角色冲突需逐项保留，不据示意箭头补出物理速度、因果轨迹或几何定理。见[RNA velocity映射案例](../tests/batches/velocity-mapping-stage-01/README.md)；完整图注为交付组成，局部范围歧义保留，新归纳文字尚未跨案例独立回归。

### 观测、几何推导与外部校准

先分清仪器直接观测、由观测推导的几何量和依赖校准的估计量，再画出每类输入的来源。直径变面积等非线性变换须保留平方和参考量，量纲一致不能替代校准依据。源文复用同一符号时，区分目标记录和校准阶段的角色；某些系数在受试者、状态或部位间的条件性复用，不等于全部几何量相等。让假设就近依附所限定的几何或模型，避免靠近另一输入线而改变读者理解。见[超声校准案例](../tests/batches/ultrasound-calibration-stage-01/README.md)：完整图注与图稿成套使用，源方程冲突及注释归属歧义保留；新规则文字尚未跨案例独立回归。



### 注意力操作的来源、索引与状态

逐个操作绑定 Q、K、V 的来源：编码、潜变量自注意力和输出解码可以采用不同归属。指向投影输入的箭头不表示原始数组等于投影后的张量；查询索引决定输出索引数，通道宽度另由变换确定。同形状状态可以更新内容，重复深度也不自动意味着共享权重。查询构造的学习、位置和输入特征按任务条件表达，不能把查询画成预测或目标。

[Perceiver IO 有限解释](../tests/batches/perceiver-io-query-roles-01/README.md)固定检验上述区别并保留 E.1/E.2 来源冲突。PDF 文本包含屏外重复标签时结合真实页面与原生坐标判断，不能仅按抽取字符串改图。此段为终评后归纳，尚未跨另一案例独立回归。


### 选择性评价的目标、接受集合与表格身份

把训练目标、训练后校准目标和实际接受比例分别命名。已报告的模型级复用关系应积极保留；缺少逐运行配对或checkpoint资料，不能改写成列间必定重训。接受集风险的分母为接受对象，覆盖比例的分母为全部评价对象；标签用于误差统计，不自动进入无标签阈值校准。软选择权重与二值接受计数分开，空接受集风险未定义。

均值和报告的±量按行列双键配对，保留精度及重复出现的值；轴集合相同也不能转置。上下文提到SE不能代替独立估计量定义，印刷0.00不证明真实零变异，跨运行均值不能反演个体计数或改成合并比率。见[SelectiveNet限定测试](../tests/batches/selectivenet-evaluation-01/README.md)：源内概率界冲突继续保留，不复原曲线或显著性高亮。此为终评后归纳，尚未跨另一案例独立回归。


### 全量预测、局部训练选择与伪监督

先区分预测汇总的对象全集与辅助训练选择的极端子集。选中对象的身份和特征进入计算模块，伪标签进入损失；把二者合成一条箭头会改变监督含义。互斥等假设及“否则跳过”必须就近写明受影响的分支，不能让读者误以为整个训练模块被跳过。选择数量符号需定义，来源未给出的并列名次、小样本或重叠选择策略仍保持未知。

逐阶段区分 patch 注意力归一化、类别概率和显示百分位，以及训练真实类别与显示预测类别。显示参考分布可放入完整图注，但不能由热图推导病理真值或因果解释。见[CLAM限定测试](../tests/batches/clam-training-pseudolabel-01/README.md)：源公式冲突保留，已知维度与未知实现分开；本段在有限终评后归纳，尚未跨另一案例独立行为回归。


### 特征与细胞表示的耦合、先验与优化角色

共享潜在维度不等于观测对象配对，也不等于编码器共享参数。先明确图顶点和每类嵌入所代表的实体，再把细胞表示与对应特征表示连接到同一数据解码器；概率模型的内积参数不能直接改画成观测矩阵相等。观测先验图、拟合图似然及特征/细胞后验正则分别标明。

对抗训练中，监督目标的身份、优化方向和直接作用的参数应分别表达。更新卡片可以列出全部被训练模块，但不能暗示每一损失直接作用于每个模块；完整图注需限定该路径。用明确的同名引用减少跨面板长线时，仍保留一个科学实体。[GLUE限定测试](../tests/batches/glue-feature-cell-coupling-01/README.md)验证上述表达并保留四处源内差异；此段为终评后归纳，尚未跨另一案例独立回归。


### 缺失条件、时间间隔与循环状态

观测掩码、测量值和距上次观测的间隔分别建模；按来源核对间隔递推使用前一时刻还是当前时刻的掩码，当前有观测不意味着传入间隔为零。观测值保持与缺失值插补的条件应就近写明；最后观测、训练均值和隐藏状态不能互换。输入衰减与隐藏衰减分别标注参数、约束和作用层级。

逐项区分线性映射与逐元素缩放、重置和状态混合；共同输入列表不自动表示共用权重或先求一个原始和。保留原文的门控混合约定、跨时刻共享参数及最终状态/逐步输出的区别。名称中的“衰减”不能替代单调性条件核查，数学限定与已验证代码行为分别记录。见[GRU-D限定测试](../tests/batches/grud-missingness-decay-01/DELIVERY.md)：原图例乘法范围错误已修复，来源张力与初始状态未知保留；此段为有限终评后归纳，尚未跨另一案例独立行为回归。


### 教师／学生的梯度、参数平均与运行状态

停止梯度不等于教师权重在训练中永久不变。把损失梯度、参数 EMA 和输出统计的运行状态分别命名；逐项记录更新对象、输入归属、聚合轴以及旧／新时刻，并从当前来源核对更新顺序。相同网络架构不等于参数绑定，单个网络在不同视图间复用参数也不意味着教师与学生共享参数。两个单独定义的动量参数不必在数值上不相等。

简化多视图计算时，保留视图集合、同视图排除条件和损失归一化；两项平均不能静默当作完整配对求和。见[DINO限定测试](../tests/batches/dino-update-roles-01/DELIVERY.md)：教师参数与中心状态使用不同数学对象和更新路径，源内符号差异及初始中心未知保留。此规则在读取 UA-MT 全文前已固定，并在[UA-MT限定测试](../tests/batches/uamt-uncertainty-gating-01/DELIVERY.md)完成跨另一医学论文的有界应用检查；该开发案例通过独立图文和24项证据评估，不构成新保留论文或一般正确率估计。不得把 DINO 的具体更新顺序套到所有教师方法。


### 随机预测、熵与选择后归一化

逐项写清平均的数学对象和轴：教师参数跨训练步的 EMA、同一输入的随机预测概率均值、类别轴上的熵及体素选择不是同一操作。先求平均概率再求熵与先逐次求熵再平均通常不同，须按来源保留次序。选择比较符、掩码作用于分子还是分母、归一化对象和空集合条件均属于方法含义；来源未给出的稳定项或跳过规则不得补写。

标准方法与消融变体的输入集合分别核对；教师一致性目标与用于估计不确定性的 MC 均值未被原文等同，图中也不自动合并。低熵不证明预测正确，阈值上升不保证变化中预测的实际接受数单调。阈值 H、损失权重 λ 和参数平均 α 分别标明用途，二分类 ln2 范围不得泛化到任意类别数。[UA-MT案例](../tests/batches/uamt-uncertainty-gating-01/DELIVERY.md)提供有限来源核验与可编辑图；本段是验收后的规则归纳，尚未跨另一案例独立验证。


### 检索条件、潜在文档与边缘化次序

先给出检索集合和概率权重的条件，再说明每个文档怎样进入生成器。权重参与边缘化，文档文本参与上下文，二者不是同一条计算路径。每个文档使用同一个模型的参数，不表示分别拟合的模型变体也共享权重。

逐项保留求和与乘积的对象、位置和范围：先形成整段文档条件概率再对文档求和，与先逐词混合再形成序列概率，一般不同。词位置上的潜在文档贡献可变化，不自动意味着生成前缀触发新的检索查询、显式硬选择或不同文档集合。数学条件关系不能充当运行调用轨迹。通用解码算法须由真实任务的贪心／beam 设置限定；微调阶段没有文档标签监督，也不能抹去初始化时的检索监督。

见[RAG限定案例](../tests/batches/rag-marginalization-01/DELIVERY.md)。来源中的 FEVER 实现限定、参数措辞冲突及归一化／缓存等未知继续保留。本段为本例归纳，尚未跨另一案例验证；此前“数学对象、轴和不交换次序”的一般规则在读取本例方法前已固定，本例不验证 UA-MT 特有的熵或体素选择规则。


### 波形状态、条件更新与显示参照

共同的更新公式不代表不同波形共用数值状态。分别标明峰值、信号／噪声估计及阈值的所属域；局部分类所选的更新行与最终联合接受条件分开，备选行不画成累积执行。常态下的派生阈值公式也不能自动升级为所有覆盖规则下的不变量；来源没有说明重算、恢复或重复处理时，保留具体未知。

按原图与方法判断延迟波形用于显示对齐还是检测输入，面板顺序本身不能创建变换路径。事件时间可支持 RR 历史，前一波形的斜率仍需要波形来源；初始化时长和所需心搏数不能代替初值或历史填充算法。见[QRS限定图](../tests/batches/qrs-signal-state-01/README.md)：既有分类、先前状态和初始化规则在阅读方法前固定并作有限应用；此段为终评后新增的限定表述，尚未在另一案例独立行为回归。


### 配对模态与拟合后注释转移

同一源细胞的多模态配对、源数据到空间参考的学习对应，以及拟合后的注释转移，应分别表达。先核对源轴和目标轴，再检查转置、收缩及条件权重的位置；同源注释行必须与映射矩阵源行相符。注释出现在转移公式中，不意味着它参与拟合目标。来源仅定义加权转移时，不自动把输出称为空间均值、实测值或一一细胞匹配。

方法允许的可选分支与某次运行是否启用分别记录；方法级密度条件也不能由可选筛选分支自行推出。见[Tangram限定案例](../tests/batches/tangram-paired-spatial-transfer-01/README.md)。本段为该例后的归纳，尚未跨另一案例独立行为验证；不把其M、f或MERFISH密度设定推广到其他空间方法。


### 临时文本、接受状态与检索触发

前瞻草稿、已接受前缀、用于检索的查询和实际取得的文档应各自命名。先定位候选何时被接受，再安排共同的状态更新；用于构造查询的临时句子不能因此自动进入重生成上下文。直接接受与重生成两种条件分支各产生一次选择，不画成同时累计两个候选。

同一组词元概率可以分别控制是否检索和如何构造查询，阈值对象及不等号边界需分别核对。后续迭代规则不能抹掉首步初始化例外；原图卡片叠放不能证明文档历史累计，概念回线也不能代替精确停止代码。见[FLARE限定案例](../tests/batches/flare-forward-sentence-01/DELIVERY.md)：本段为终评后归纳，尚未跨另一案例独立行为验证；它不把FLARE的具体查询方案或未知回退迁移到其他系统。


### 物理通道、回归角色与被扣除项

采集中的源—检测器配对、组织贡献和处理后的信号分别命名；器件间距不自动表示光学深度，来源假设的敏感性不能画成已证实的纯信号分离。回归图逐项区分协变量、拟合目标、通道或样本特定系数、构成的贡献与最后被减去的量。若来源扣除的是系数加权组合，不能直接把原始信号或某个主成分送入减法；原目标信号作为被减数时保留对应输入。

见[fNIRS限定案例](../tests/batches/fnirs-channel-contributions-01/DELIVERY.md)：所选GLM-PCA2范围与其他分支分开，解释性方程不补齐未报告的中心化、截距或求解器。本段为验收后归纳，尚未跨另一案例独立行为验证。


## 医学体数据的索引与物理空间

区分存储索引、体素中心、图中局部毫米坐标和头信息给出的世界坐标。先确定当前文件采用的有效空间变换及单位，不能凭文件名、最近方向字母或scanner/MNI代码断言真实参考身份。轴置换与翻转只改变数组表示时，原生斜切仍存在；“near-axial”等近似方向不等于已重采样到世界正交平面。任意技术测试点不能画成病灶或临床标注。[有限IXI实例](../tests/batches/medical-volume-reindex-01/README.md)仅核验给定qform下的一份衍生体数据；上游处理链和确切参考仍未知。

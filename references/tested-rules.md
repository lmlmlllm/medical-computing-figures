# 条件规则与验证入口

这些是来源限定的绘图经验。不能将案例参数、性能或创新直接移入另一篇研究。默认先执行 understanding.md，再按图的职责选本表。

| 可迁移要求 | 来源与实例 | 适用边界与验证 |
|---|---|---|
| 同一模块在训练、推理阶段的输入和可更新状态分开标注 | MCF001-F2；MedSAM | image encoder/mask decoder 更新、prompt encoder 冻结仅是该版本事实；受控反向箭头、冻结冲突、跨阶段标签输入及实际修复见 tests/controlled |
| 总量标签保留数据池和划分层级 | MCF001-F2；MCF004-F2 | 发展/验证图像对不能写成全体训练量；患者、扫描、序列、切片按各自来源，不统一改成患者独立 |
| 可选配置与同时运行的分支区别表达 | MCF002-F2；MedRAG | 原模块选项不是全部并联模型；示例明确固定 MedCorp / RRF-4 / GPT-3.5 配置 |
| 查询、答案选项、检索上下文和评价答案分开 | MCF002-F2；examples/medrag | 该文 question-only retrieval；不要假定所有RAG如此；评价金标准不接到生成输入 |
| 汇总表只支持相应点值，误差定义须独立核验 | MCF002-F3与Table6；examples/results | 十个真实准确率可重绘；原表比例标准差不自动改成跨种子SD或95%CI；不合成ROC |
| 多视角的共享参数、缺失掩码和融合位置显式可读 | MCF004-F1；examples/multiview | 无位置编码+共享backbone的集合性质不能移植给独立slot分支；实质变更图明确失去整模型置换不变保证 |
| 配对模态保留同一细胞层级，观测与潜变量分开 | MCF003-F1/F2；examples/totalvi | 同细胞RNA/蛋白配对不是同donor的多个独立重复；潜在嵌入不等于物理空间或机制验证 |
| 图索引、社区摘要与查询时汇总分开 | MCF005-F1；examples/graphrag | 所读v2的global search：社区层级、map评分、过滤和reduce；不是GNN、医学临床验证或所有GraphRAG的通用固定设计 |
| 后验近似与条件似然分开，符号依方法定义 | MCF006-F1；examples/scvi | 2018模型q(l)为log-normal；NB分量均值μ不同于含零膨胀均值(1−π)μ；原文歧义已记录，不外推当前软件默认 |
| 信号采样、记录时长、输出间隔和评价单位分开 | MCF007-ED1；tests/batches/signal-01 | 200Hz、30s、每256样本一次输出来自本研究；输出间隔不等于窗口、感受野或延迟；区间重复于患者内；集合评价不是多数票 |
| 设备的物理供能、刺激、观察和控制分别表达 | MCF008-F1；tests/batches/engineering-01 | 感应供能不是数据传输；ECG观察不是自动反馈；动物原型、离体人体组织和未来临床设想分开。功能块图不冒称完整电路图 |
| 差值区间须对应同一比较、统计单位与具体算法 | MCF009-F2与官方Table2a；tests/batches/uncertainty-01 | 使用作者报告的配对差值CI，不从两个边际CI或舍入比例重算；不同队列的Wald/聚类与加权bootstrap不混称跨种子SD |
| 每行分母与权重分开，区间跨零必须完整显示 | MCF009-F2；tests/batches/uncertainty-01 | 敏感度/特异度分母不同；非加权N不是加权有效样本量。零线不是非劣效界值；共用坐标不允许合并国家效应。原文未指定的bootstrap算法保持未知 |
| 配套方法图与结果图须有来源支持的配置联系 | MCF002；tests/batches/figure-set-01 | §5.1/Table6和Appendix B.3支持MedCorp/RRF-4/32/完整模型版本；两图各自正确仍不保证配对正确。共享命名/配色不是配置相同的证据；不把改检索器后的方法与原性能相连 |
| 样本数附着于真实阶段、统计单位与比较可用性 | MCF009-F1；tests/batches/research-design-01 | 分配百分比不等于最终人数；完整测试集、可读片子集和嵌套读者研究分别标注，同一病例的多个读者不是新患者 |
| 阳性结局窗口与条件性阴性随访分别表达 | MCF009-F1；tests/batches/research-design-01 | 39/27个月阳性窗口不能套作全部阴性随访；≥21个月条件保留未活检/从未阳性等人群范围。特定数字不可迁移 |
| 原文矛盾与绘图错误分别定位 | MCF009-F1；tests/batches/research-design-01 | 显式保留31,766−5,990与25,856的来源冲突，不自行改成5,910；来源未知不升级为泄漏事实或充分独立验证 |
| 预测、模型访问与解释图分别保留其接口 | MCF010-F1；tests/batches/interpretability-01 | 八种方法不强套一个内部算法；预测标量不是生成所有解释图的充分输入。无真实输出时画对象关系，不合成研究热图 |
| 度量的含义和方向随评价问题核对 | MCF010-F1；tests/batches/interpretability-01 | 像素AUPRC是定位评价；权重随机化后的SSIM降低与重复训练的稳定性不同。50个图对不是50个模型，具体判据只归属于该论文 |
| 来源示例与操作性标准保留适用边界 | MCF010-F1；tests/batches/interpretability-01 | 选择性pass示例不支持发生率；无显著差异不证明等价。ROI可遗漏其他预测信号，定位或权重敏感性不单独证明机制或临床效益 |
| 候选网络、拟合关系、计算扰动与实验支持分别表达 | MCF011-F1；tests/batches/perturbation-01 | motif候选方向与组内表达拟合不证明每条因果边；斑马鱼应用无scATAC输入，不移植鼠示例的模态配置。两组实验只支持所述noto表型范围 |
| 模拟的量、参照数据与适用阶段不可省略 | MCF011-F1；tests/batches/perturbation-01 | 传播表达变化并固定目标TF变化；局部投影使用未扰动细胞参照，不生成未观测状态。初次审阅补回“早期”分化限定，重画与定向复测记录保留 |
| 原文计算预测与本地模拟测试分开标记 | MCF011-F1；tests/batches/perturbation-01 | 此图归纳已发表预测和实验，不声称本地重跑。若另造测试数据须明确模拟；来源约25/sample与40–50/experiment的范围歧义继续保留 |
| 节点聚合、全图读出和另一模态的池化分别核对 | tests/batches/graph-method-01 | GraphDTA所画GCN变体用邻接更新逐原子表示，再跨节点做全局max得到分子向量；逐节点跨特征max不等于全图读出。蛋白分支独立，不能将其pooling作为药物分支的证据 |
| 变体、对象层级和已知局限须保持来源范围 | tests/batches/graph-method-01 | 四种GNN为备选；三层GCN和每位置128维来自详细Methods。原图省略号不算冲突；未考虑立体化学是论文明确局限，具体边编码/标准化仍未审计。不推断亲和力单位或临床作用 |
| 站点保管、参数上传、分数上传和执行顺序分别表达 | MCF013-ED9；tests/batches/federated-01 | EXAM来源支持记录留在医院、更新送聚合、分数送选择；图上消息端点不等于发送时机。聚合权重n_k在该文是本地训练迭代数，不能通用化为患者数 |
| 明示本地训练使用收到的模型，保留候选与阶段区别 | tests/batches/federated-01/independent-retest.json | 初次独立审阅发现参数只到验证节点、训练依赖隐含；补明后定向复测关闭。执行顺序线仍不承载参数；最终全局、最佳全局与最佳本地不合并；每个结局窗口单独说明 |
| 部分来源已知不能扩写为全部未知或全部已知 | MCF013-ED9；federated-01 | CDH最佳全局模型明确，MVH/NCH具体检查点未明确；MGB统计拟合范围、BN状态及形式化隐私协议继续保留未知，不因局部保管或SSL而补造保证 |
| 分开表示学习、噪声估计训练与生成时的状态更新 | MCF014-F5；tests/batches/generation-01 | Medfusion先训练自编码器，再冻结其权重训练噪声估计器；采样重复使用固定参数。重建参照、已知扰动目标和请求类别不互换；不同影像领域不等于同一患者多模态融合 |
| 噪声估计、当前潜变量和解码器输入按计算对象核对 | MCF014-F5；generation-01 | DDIM使用估计值、当前状态和日程更新潜变量，最终潜变量才解码。原图总览省略的采样运算不能从字面连接改写成直接解码噪声；观察图像、重建图像和生成图像分别命名 |
| 固定参数不等于确定性采样，数字图尺寸不等于页面适配 | generation-01/independent-review.json与independent-retest.json | 独立建议后补明η相关采样随机性可能存在，正式实验η仍未知；代码默认不当作论文设置。210×371mm时9pt的文字缩到较小页面会变小，需重排和重新看图，不能保留原字号宣称 |
| 反馈系统分开画传感、数据、控制、供能与刺激 | MCF015-F3；tests/batches/closed-loop-01 | 离体人心实验中 ECG 进入控制，光学映射只作观察；手工刺激用于改变心率，不是控制器人工覆盖。Tx→Rx 是感应供能；受控反向箭头已定位修复 |
| 条件性计时检查不得改画为无条件截止策略 | closed-loop-01 | 保留原图严格阈值、开关状态和返回路径；正文的 10 s 示例与图中条件检查不能补写成已知调度器。补充方法缺失时保持部分核验；100 bpm 刺激率不是未知的上阈值 |
| 论文图集分别核查实验配置、共享别名和数据覆盖 | tests/batches/paper-suite-01 | Table 6 与 Table 7 是两个实验家族；同名配置不等于相同归档运行或独立重复。主图平均值、补图完整任务值及重复端点有明确分工；本例覆盖 258 个唯一表格值 |
| 方法身份配色与数值色标分别使用 | paper-suite-01/F3、F4、S1 | 蓝色圆点／紫色方块及文字区分方法，cividis 固定 0–100 表达准确率；不靠方法颜色表达好坏，也不隐藏低值。源 ± 含义不足时保留数值与未知，不能重新解释为 CI |
| 概括趋势须与实际曲线的局部变化一起核对 | paper-suite-01/F5；claim-C09-retest.json | BioASQ 最后区间下降、PubMedQA 局部上升约束正文概括。已知方向与未知幅度分开；没有数值输入时只作明确标注的定性图，不造曲线或最优点 |
| 未报告的方法不能写成已证实未实施 | paper-suite-01/F5-wording-retest.json | 分组位置与准确率的关联不证明位置干预；“原文未报告随机位置干预”比“位置未随机化”更符合所读证据。此措辞修订已同步图、规格、映射和图注并复看 |
| 波形数字值、校准、坐标与可见单位一起核验 | tests/batches/signal-waveform-01 | 60,000 个真实样本从原始字节至 SVG 逐点核对；mV→µV 单标签错误的首次独立终评检测/定位各 1/1，正确对照目标误报 0/1；正确图注不能代替正确图内单位 |
| 名义时长、样本时间与发布前处理分别表达 | signal-waveform-01 | 5,000 个 500 Hz 样本的末点是 9.998 s，名义窗口 10 s；源 400→500 Hz 处理与本地仅单位换算分开。末端恒定段先查输入，上游成因未知，不据图作诊断 |
| 同一记录局部展开保留样本成员、半开区间与时间原点 | tests/batches/signal-window-01 | 原记录时间k/fs与窗口内(k−k0)/fs分别标注；2秒窗口的最后相对采样点1.998秒，不新增端点或独立记录 |
| 换窗同步数据、范围标记、刻度、原点和图注 | signal-window-01 | [2,4)→[6,8)改变996/1000对应幅值；14000实际SVG点及PDF路径核验、三种软件定点错误检出。共享尺度与整条记录保持不变；不是临床事件分析 |
| 具体 TIFF 元数据与标注含义优先于网站概述 | tests/batches/image-overlay-01 | 此成员为 450×450、8-bit 图像配 1-bit WhiteIsZero 人工边界；边界像素不等于填充实例或模型预测，打印 DPI 不提供 µm 校准 |
| 图像与边界共用裁剪／坐标，实际导出按放置变换核验 | image-overlay-01 | 同窗同向、半整数外缘与局部平移同步；基线 255 项及 14 导出隔离重现已完成，三种软件控制均检出预设错误。PDF 倒序编码与不透明 RGBA 曾需修正检查器解释，图稿未变；预览不是精确像素占用测试 |
| 截止时刻事件、来源删失与行政删失按明确规则分开 | [survival-display-01](../tests/batches/survival-display-01/README.md) | `T*=min(T,τ)`，`E*=E 且 T<=τ`；同刻死亡先用退出前风险集。180→90 天为任务限制，不是临床阈值；未知零点与删失假设不因绘图通过而成立 |
| 生存阶梯、退出前风险与累计计数同步，跨版本比较数据坐标 | survival-display-01 | 429 项独立技术检查、三种 SVG 错误检出、14 导出隔离重现；来源标记重数披露，行政端点不偏移。轴比例改变不表示共同区间结果变化；不是模型准确率、预后或治疗效应验证 |
| 完整测量 ID 与生物样本组分别标明 | [protein-matrix-01](../tests/batches/protein-matrix-01/README.md) | 30 行属于两个源鼠 ID 组，保留源顺序和后缀未知；不是 30 只独立动物。字段技术选择目的写入图注；一张公开表的切片不支持生物效应推断 |
| 字段扩展固定共享色标，源精度与文字舍入分开 | protein-matrix-01 | 四列→八列共有 120 格源值、实际颜色与文字一致；未舍入值驱动固定 0–7 色标，`.3g` 仅用于文字。不宣称该色域适合所有蛋白数据或跨蛋白绝对丰度可比 |
| 缺失掩码绑定单元、NA 文字和独立图例 | protein-matrix-01 | 修订版 210 个有值格、30 个 NA；174 项分组软件检查及数值／列名／NA→0 三种控制、14 导出隔离重现。有限软件敏感性与两阶段模型读图分别记录，不称专家验收或普遍准确率 |
| 类似分支逐条核对箭头头部、端点与消失的原路径 | tests/independent-review{,-retest}.json；conformal-pathology-01 | 曾错定位相邻分支；conformal 首轮目标检出2/2但多记两条不存在原线，完整清单／修复0/2，定向来源知情复看更正2/2。初次失败不覆盖 |
| 类条件校准真值与测试真值按阶段分开 | [conformal-pathology-01](../tests/batches/conformal-pathology-01/README.md) | 校准标签选择真类参考；测试真值只事后评价。两种错接被定位，键指导修复14导出与正确对照一致；来源公式／代码冲突未解决 |
| 集合基数、覆盖错误与名义置信设置分开 | conformal-pathology-01 | strict p>ε，c=.95→.99 的模拟给定值 {C}→{B,C}；empty 排除真值，多标签不是并发诊断。35项有限检查不验证 p 构造或临床覆盖 |
| 固定行列身份、归一化对象和转置时机 | [multimodal-contrastive-01](../tests/batches/multimodal-contrastive-01/README.md) | 目标与预测分别命名；反向先转置分数再归一化。三个已知答案的软件控制定位至Q_text、P_image、S，正确对照0发现；不作为独立读图准确率 |
| 删除成员同步两方向形状、分母和损失 | multimodal-contrastive-01 | 模拟3×3→2×3/3×2；正向共同两行不变，反向概率重算。90个SVG/PDF单元与输入映射核对、23导出隔离重放；未运行原研究代码或验证真实医学相似度 |
| 区分概念路由、实际调用与缓存答案评估 | [rag-routing-01](../tests/batches/rag-routing-01/README.md) | 论文选择器与代码离线答案选择分别说明；当前问题和类别决策分别入图，参考答案只用于离线训练／评价。代码快照与真实运行身份未核实，来源仍为partial |
| 路由条件改变同步删除专属回路与旧图注 | rag-routing-01 | 模拟C→B路径删除四节点／五边；71与58项有限原生对象检查，三类已知答案错误定位并修复21导出。首次修改版来源注记错误保留，修订后全图/预览已看；不推断策略表现 |
| 空间无向支撑不等于对称注意力或无向消息 | [spatial-graph-01](../tests/batches/spatial-graph-01/README.md) | 六点给定拓扑区分无向半径支撑和j→i聚合；有向支撑错误被原生路径检查检出。没有计算注意力或细胞通信结果 |
| 可选分支剪边保点，完整分支仍可传跨标签信息 | spatial-graph-01 | 开启100项、关闭78项有限原生检查；三个已知答案错误被定位，正确对照0发现，修复21导出等于旧基线。关闭版删除四节点／五边与aware示意；不是原研究效果验证 |
| 自定义规格也须逐关系定位证据并解析相对路径 | spatial-graph-01/verification/spec-completeness-review.json | 原生图稿检查曾漏掉规格字段缺口；新交付141/115/141字段检查和9个负例通过，18个非映射导出字节不变。原首次验收保留；字段完整不等于科学含义已证明 |
| 矩阵语义对象覆盖所有计算端点，成员标签不能代替数组 | [spec-evidence-02](../tests/batches/spec-evidence-02/README.md) | 原元素表只列I/T成员，未声明被关系引用的标签、嵌入、分数与概率矩阵；补齐数组/损失对象及结果字段、形状、分母。18个元数据负例拒绝，126单元原生/标量核验；不是科学错误计数 |
| 字段修补另存交付，以导出和输入哈希连接既有视觉证据 | [spec-evidence-01](../tests/batches/spec-evidence-01/README.md)；spec-evidence-02 | RAG18个、MedCLIP27个非映射导出保持字节；分别21/31导出来源隔离重现。旧验收与首次评分不回填，不将元数据回归称为新的看图或独立审阅 |
| 将配置计划、拟合模型、验证证据与推断输入分开 | [MCF020-F2 / configuration-planning-01](../tests/batches/configuration-planning-01/README.md) | 条件级联、折集成与配置集成分别表达；207/188/207 项开发原生检查，三错/一正确/一不足对照及21导出OS回放。预印本来源仍partial，SQ解释线未代码核实；不将CV选择分数当独立性能 |
| 固定配置后删去选择器和全部相关路径 | configuration-planning-01 | 固定2D绘图政策删S、OS、SA、SQ，保留5折模型与后处理选择；图注和数值范围同步。仅模拟结构变更，不继承原论文结果 |
| 按阶段区分标注模型、专用生成器与发布数据 | [MCF021-F1 / annotation-engine-01](../tests/batches/annotation-engine-01/README.md) | 两阶段标注→专用生成器，不补发布数据回训该生成器；3个版本各135/135有限检查，原始共用端口问题经实际看图修复。只适用于有来源支持的模型/数据版本 |
| 置信过滤、实测成对比较和抽样分母分别表达 | annotation-engine-01 | 预测IoU、受检掩膜对与全发布集合不同；已知3错/1正确/1不足，保留首轮标签越界和133/133修订。全量审核模拟版删除原质量数值；质量样本复用未知，无独立测试/效果主张 |
| 分开记录运算轴、参数共享轴和层实例范围 | [MCF022-F1 / axis-mixing-01](../tests/batches/axis-mixing-01/README.md) | token MLP沿S、跨C共享，channel MLP相反；转置与固定形状明确，同形状不等于跨深度共享。规则以当前材料为准；3套图各217/217有限检查及换色/取消共享变更 |
| 限定独立运算的范围并核查残差输入 | axis-mixing-01 | MLP切片独立不等于含LayerNorm的整块独立；原X/U分别旁路至加法，池化轴明确。3个已知错修复、1正确0误报、1不足保留；首稿212/217排版失败保留，完整训练正则化未核验 |
| 离散汇总值区分点估计、重采样均值与配对区间 | [MCF023-T4 / decision-curve-01](../tests/batches/decision-curve-01/README.md) | 25行/100数值转录；主图115项原生检查。混用均值与相减边际区间两个错误被定位并修复，0.0000边界和原表舍入差保留；不重建完整曲线 |
| 指标变换同步点与区间、分母与解释 | decision-curve-01 | 固定阈值的正因子将ΔNB转为净活检减少当量/100人，53项检查；百分数当概率错误被检出修复。不是实际避免活检次数或临床效果；24导出OS回放，来源知情自测 |
| 由校准、单双边和归一化确定谱单位与dB参考 | [signal-timefreq-01](../tests/batches/signal-timefreq-01/README.md) | 同一真实ECG的直接DFT与全部窗加权Parseval核对；遗漏翻倍与fs除数错误定位修复。不是原始均方不变、临床解释或独立读图准确率 |
| 窗长变更联动样本、中心、频点与图注 | signal-timefreq-01 | 256→128为75×129→77×65；三个版本各32/32，窗起点误标中心反例修复。27导出OS重现、从交付规格另重绘9个一致文件；18处旧导出相对路径失效保留 |
| 在最终物理尺寸查看，并修复残留标签 | tests/history/failures.jsonl | 初始5.10pt辅助文字、假设变体仍叫MedSAM、图例与数值重叠均留下历史；最终再渲染查看 |

figure-set-01 验证两图子集；paper-suite-01 进一步验证七张解释图／八页的分工、一致性与完整表值覆盖，但不是原论文全部定量图的替代或正式投稿验收。closed-loop-01 验证来源支持的反馈关系表达，补充方法缺失仍限制语义范围；没有运行控制器或验证临床部署。有限模型审阅与程序核对不等于人工专家审核。

| 规则 | 证据 | 已运行检查 | 范围 |
|---|---|---|---|
| 注意力按 Q/K 宽度缩放、按查询在键集合归一化 | [MCF024-F2 / attention-core-01](../tests/batches/attention-core-01/README.md) | 固定模拟三位置二维输入；独立Decimal与实际42单元核对，3错误定位/3修复、1正确0误报、1不足 | 单头核；不是原模型、医学结果或独立盲读 |
| 掩码变更同步 L/A/O，颜色越界需披露 | [attention-core-01](../tests/batches/attention-core-01/README.md) | 三版31项检查、全屏蔽及未披露越界实际拒绝、27+9导出隔离一致；首次越界遗漏保留 | 不保证任意库全屏蔽行为；字节一致不代替看图 |


## U-Net有限空间/通道接口（1.27.0）

| 条件规则 | 来源与测试 | 实际证据 | 不适用或未验证范围 |
|---|---|---|---|
| 裁剪保留C；concat匹配H/W并累加C；add不可替代 | [MCF025-F1 / segmentation-shapes-01](../tests/batches/segmentation-shapes-01/README.md) | 3错误定位与修复、1正确0误报、1不足不可判定；10图各31项有限检查 | 来源知情自测；作者代码/精确偏移未核验 |
| 输入尺寸变化同步所有分支及输出；输出特征不等于掩膜 | [segmentation-shapes-01](../tests/batches/segmentation-shapes-01/README.md) | 572→388与588→404；6正式图像实际看；27+9隔离导出一致 | 不等于训练、神经前向、完整tiling或研究性能；C2索引夹具为模拟 |


## 汇总效应量与反向比较（1.28.0）

| 条件规则 | 来源与测试 | 实际证据 | 不适用或未验证范围 |
|---|---|---|---|
| 调整估计不等于原始风险比；总体不是独立第四组 | [MCF026-F3 / effect-estimates-01](../tests/batches/effect-estimates-01/README.md) | 3已知错误定位与修复，1正确0误报，1不足不可判定 | 来源知情自测；不验证原试验模型拟合或因果假设 |
| 反向比较同步1/r、反序倒数区间、事件列与favor方向 | [effect-estimates-01](../tests/batches/effect-estimates-01/README.md) | Decimal独立计算误差≤2.23e−16；原生对数几何；6最终图像实际看；27+9隔离导出一致 | 已四舍五入的4行来源汇总；不是新CI、P值、权重或患者级重分析 |


## 单细胞归组与统计单位（1.29.0）

| 条件规则 | 来源与测试 | 实际证据 | 未验证范围 |
|---|---|---|---|
| keyed cellID对齐、细胞类型筛选、原始计数按样本求和 | [MCF027-F3 / pseudobulk-units-01](../tests/batches/pseudobulk-units-01/README.md) | 3×12X、4×12H、3×4Y；10图各33原生检查；6无效输入拒绝 | 模拟输入；未验证真实单细胞数据、上游归一化或DE模型 |
| 重分配后的伪重复不能改名成为新的生物学样本 | [同批次](../tests/batches/pseudobulk-units-01/README.md) | 3错误定位修复、1正确0误报、1不足不可判定；27+9隔离导出一致 | 来源知情自查；非盲审、独立或专家验收 |
| 冻结数值期望出错时保留失败并独立复算 | [R04保留更正](../tests/batches/pseudobulk-units-01/expected-errata-01.json) | 原清单13/14通过、1手算错误；CSV逐项21/18支持另行更正，数据/图源未改 | 更正发生在观察后，不冒充新预注册或独立测试 |


## 测量一致性图（1.30.0）

| 条件规则 | 来源与测试 | 实际证据 | 未验证范围 |
|---|---|---|---|
| 按受试者ID配对、固定首次读数、明确large−mini方向 | [MCF028-F2 / measurement-agreement-01](../tests/batches/measurement-agreement-01/README.md) | 17公开配对读数、68值来源核对；10图各21项检查 | 其他仪器/队列、重复测量模型未验证 |
| 2SD界限不同于2SE及均值CI；只有n和均值时保留不足 | [同批次](../tests/batches/measurement-agreement-01/README.md) | 3错误定位修复、1正确0误报、1不足不可判定；6无效输入拒绝 | 没有置信区间、正态性或临床阈值分析 |
| 单位换算与源舍入差异有明确映射 | [同批次](../tests/batches/measurement-agreement-01/README.md) | L/min→L/s、配色保持、27+9隔离导出一致；原文两处冲突保留 | 来源知情开发自查，不是独立/专家或器械有效性验收 |


## 记忆读写与实际缺失输入（1.31.0）

| 条件规则 | 来源与测试 | 实际证据 | 未验证范围 |
|---|---|---|---|
| 读取键与写入比较特征分开，K/B/槽数分开；重复ID不增加个体 | [MCF029-F2 / memory-selection-01](../tests/batches/memory-selection-01/README.md) | 固定2D代码局部，11图各26项检查；3已知错例定位修复、1正确0误报 | 模拟向量；无张量、模型、GPU或随机序列复现 |
| 当前读先于候选写；相对置信门保留严格边界 | [同批次](../tests/batches/memory-selection-01/README.md) | cN0.45→0.40同步保留／替换，读取不变；36+9隔离导出一致 | 仅一查询行、一次候选迭代；完整论文仍partial |
| 概率分组连到所有槽；材料不足实际删字段 | [同批次](../tests/batches/memory-selection-01/README.md) | 2视觉缺陷保留修复；R14旧稿25/26失败，真实缺字段后26/26；8无效输入拒绝 | 来源知情开发自查，不是独立／专家审核 |


## 校准分箱与条件频率（1.32.0）

| 条件规则 | 实际证据 | 范围 |
|---|---|---|
| 平均预测不等于箱中点，分母为箱内n；空箱不补零 | [MCF030-F2 / calibration-binning-01](../tests/batches/calibration-binning-01/README.md)：92天公开数据，3已知错误检出修复、1正确0误报；8有效稿×25项检查 | 执行者知情开发测试，非盲审/专家或临床验证 |
| 分箱变化同步全部统计和标签，换色保持语义 | 9/10/11→8/10/12；中间面板不变，原预测不变；15个当前等价图像视图已看 | 无模型拟合、PAV、不确定性带或评分分解 |
| 缺结局保留可知计数并核对所有文本 | 原页眉错误24/25保留；修复25/25；7非法输入拒绝；36+9隔离导出一致 | 源R二进制对象与CSV等同未验证；原图仍partial |

## CORP follow-up — calibration-isotonic-01, 1.33 candidate
18 fixed requirements passed within source-aware developer scope:78 numerical checks,221/221 valid native checks across8deliveries,3known errors with7expected native failures,1correct control with0false positives,3repairs and9invalid-input rejections. Public92-day EMOS observations yielded9maximal PAV blocks; selected R numeric functions and own Python fitting agreed, using saved synthetic R draw banks for both90% pointwise targets. The source CSV/RDA comparison passed its fixed tolerance. Neither R RNG identity, coverage nor clinical utility was tested.
11specs now contain8elements/4relations and source locators;77scientific/visual files stayed byte-identical.54exports replayed under original/old-input, network and outside-write denial. Float-binary Fraction failure, independent-oracle float handling, SVG rounding checker failure, visual spacing, missing-target wording and nested-sandbox failure are retained with separate repairs. These are development tests, not new independent or expert review. [Current files and reproduction](../tests/batches/calibration-isotonic-01/DELIVERY.md).

## Conformal version continuation — 1.34 candidate
Existing MCF016-F1 stays semantic_partial. The author v1.0.0 tag points to the prior pinned commit, and six selected functions actually ran in current R4.5.1. Own arithmetic with saved draws passed74original checks; a separately frozen A3/B4-stratum supplement passed20. Eight valid deliveries passed248native checks. Three faults (normalization, inclusive equality, pooled strata) caused24expected failures; all3were found,1correct control had0false positives and3repairs passed. Ten actual CLI packets were rejected before rendering.54exports reproduced with original/old-source, network and outside-write denial, including a packet with no test truth.
Semantic self-targeting, interpreter-path loss of the virtualenv, and a reproduced fixed6-case label accepting7calibration cases were repaired with history retained. These developer tests neither settle the paper/code discrepancy nor validate population coverage or clinical use. [Figures and commands](../tests/batches/conformal-version-01/DELIVERY.md).

## Confusion-matrix continuation — 1.35
MCF007-F2 adds one partial source figure from an existing paper. The official12×12×2absolute counts were actually read by two paths. Local development completed16requirements and208valid native checks; all3known faults were found and repaired, with0false positives on the correct control. One earlier missing-panel XML-whitespace false positive is retained separately.55isolated files and11delivered-spec files matched; the portable importer/render code separately reproduced121files with original-directory/network/outside-write denial. Its source guard rejects changed data before plotting under the paper's identity.
The release carries own code/links/evidence only. Its7-check numerical smoke is explicitly simulated and does not substitute for the separate local real-data work. Source normalization, wording conflicts and distribution terms remain partial. [Adapter, evidence and limits](../tests/batches/confusion-matrix-01/DELIVERY.md).

## Precision–recall continuation — 1.36
MCF031-F2 adds one partial source figure and one paper. Twenty published illustrative scores support a focused native reconstruction;100rounded TableA fields agree with exact count interpolation.16fixed developer requirements,216valid native checks,3known errors/0misses,1correct/0false positives,3repairs and19invalid-CLI rejections passed.121exports were byte-identical in two OS-isolated runs, with8main and11missing-truth read denials;11delivered-spec exports also matched. Twelve current output images were actually viewed. A label-target ambiguity was repaired and retained. These are same-developer checks on an illustrative example, not clinical, original-code, new held-out or expert validation; source hull and figure-number conflicts remain. [Current entry](../tests/batches/precision-recall-01/DELIVERY.md).

## Registration pull sampling and auxiliary supervision

[registration-warp-01](../tests/batches/registration-warp-01/DELIVERY.md): explicit map direction and row/column order, identity addition, neighbour arithmetic, coupled branch/loss removal, labelled input aliases and palette-consistent wording.16fixed requirements;288valid native checks;3known errors detected/repaired and1correct0false positives;132strict isolated exports. All values simulated, original3D/learned model untested. See [conditions and counterexamples](../tests/batches/registration-warp-01/transfer-rules.md).

[graph-diffusion-01](../tests/batches/graph-diffusion-01/DELIVERY.md):16fixed requirements;342valid native checks;3known faults detected/repaired,1correct0false positives;14change checks,24CLI rejections;132strict isolated exports plus11recipe exports. Separates seed weighting, stationary diffusion and raw count scoring; demonstrates a nonseed error invisible in final ranks. All numbers simulated; no original model, medical, independent or expert validation. [Conditions](../tests/batches/graph-diffusion-01/transfer-rules.md).

[velocity-phase-01](../tests/batches/velocity-phase-01/DELIVERY.md):16fixed requirements,360valid native checks,3known faults detected/repaired,1correct0false positives,20change checks,27CLI rejections,132strict isolated plus11recipe exports. Tests coordinate/component order, zero vectors, conditional parameter effects and computable components under missing input. All supplied values simulated; no original model, posterior, fate, held-out or expert validation. [Conditions](../tests/batches/velocity-phase-01/transfer-rules.md).

[beamforming-delay-01](../tests/batches/beamforming-delay-01/DELIVERY.md):16fixed requirements,405valid native checks,3known faults detected/repaired,1correct0false positives,21change checks,32CLI rejections,132strict isolated plus11recipe exports. Tests local time references, interpolation, unnormalized signed sums and partial missing input. All values simulated; no original acquisition, acoustic field, adaptive fit, B-mode, clinical, held-out or expert validation. [Conditions](../tests/batches/beamforming-delay-01/transfer-rules.md).

[competing-incidence-01](../tests/batches/competing-incidence-01/DELIVERY.md):1384public MGUS2 rows;5256R-software comparisons,39numeric groups,569valid native checks,33change checks,11CLI rejections,154strict isolated plus11recipe exports.3wrong figures detected/repaired,1correct0FP. Original expectation overpredicted3KM changes and remains failed; material leakage, row-order pin bug, early probe failure and visual repairs retained. Same-executor descriptive reproduction; no CI/regression/causal/expert claims. [Conditions](../tests/batches/competing-incidence-01/transfer-rules.md).

[integrated-gradients-01](../tests/batches/integrated-gradients-01/DELIVERY.md): own smooth polynomial only;45numeric groups,15API/10CLI rejections,36change checks,438valid native checks;3known faults detected/repaired,1correct0FP;132OS-isolated plus11recipe exports.8unique previews and8PDF rasters actually viewed. Source printed algebra conflict remains semantic_partial. ENOSPC failure and reversible cache recovery retained. No real-data, neural-network, clinical or expert validation. [Conditions](../tests/batches/integrated-gradients-01/transfer-rules.md).

[cell-fraction-01](../tests/batches/cell-fraction-01/DELIVERY.md): own complete-gene unweighted simulation;15numeric cases/52checks including24input rejects,44changes,9CLI rejects,714valid native checks;3known wrong estimates detected/repaired,1correct0FP;132OS-isolated+11recipe exports identical.8unique previews and8PDF rasters actually viewed. Initial arithmetic, JSON serialization and canvas-tolerance failures retained. Current author overview/code only: semantic_partial, no whole-MuSiC, real-data, clinical or expert validation. [Conditions](../tests/batches/cell-fraction-01/transfer-rules.md).

[embedding-affinity-01](../tests/batches/embedding-affinity-01/DELIVERY.md): original supplied-affinity four-point simulation,14numeric cases/69checks incl30rejects and8finite-difference cases;3212valid native checks,53changes,10CLI rejects;3faults detected/repaired,1correct0finalFP;132OS-isolated+11recipe exports identical.8previews and8PDF rasters actually viewed. Spacing, multiline parsing, short-arrow and appearance-metadata failures retained. SourceFigure1/Algorithm1 conflict remains semantic_partial. [Conditions](../tests/batches/embedding-affinity-01/transfer-rules.md).

## 派生模态记录与评价参考（1.44.1-dev）

[MultiVI单图开发迁移](../tests/batches/multivi-missingness-01/README.md)在布局前固定8项，最终独立计分8项通过；原始细胞、两条互补记录、构造池、缺失/观测零/推断及两种汇总指标分别表达。独立读者先看图再核对来源；未新设错误对照，不计算TP/FP。原始间距缺陷和陈旧状态字段均保留修复证据。17文件白名单包在本机隔离重绘一致，10项实际禁读成立；部分训练转录、精确划分成员及PR面积实现仍有限制。上述新增规则尚未经另一批单独行为回归，不将本例扩张为完整MultiVI研究复现。


## 控制角色、时标与可见限定（1.44.1-dev）

[脑—脊髓接口单图](../tests/batches/brain-spine-interface-01/README.md)在布局前固定8项，最终独立来源知情计分8通过、0失败、0未观察、0不可判定。18对象/20关系区分提示更新、EMG标定、在线命令、电作用、测量与两种评价；原始图先独立只看图再给来源，紧凑版和最终版为来源知情复看，不新增TP/FP或保留论文计数。原样式/溢出/字号问题、重排时可见主体与范围限定丢失、审计脚本和状态文字问题均保留修复证据。13文件ZIP在本机拒读18份既有禁读文件并拒绝网络的隔离环境实际重绘，SVG/PDF/PNG逐字节一致；非致命字体发现警告保留。原生252×300mm、最小8pt，不称180mm期刊验收。ED1仅图注、姿势/评价表示/公式冲突和控制器实现未知仍保留；不称模型运行、临床验证或通用准确率。此后新增的文字限定检查规则尚未经另一批单独行为回归。


## 操作次数、分析组与报告尺度（本地1.44.1-dev）

[MASAI两面板汇总图](../tests/batches/masai-workload-01/README.md)在作者计划前固定8项，独立最终计分8通过、0失败、0未观察、0不可判定。13个来源报告值经独立转录、先图后文阅读及原生坐标核对；两次71项检查分别覆盖交付与精确ZIP重绘，不合并为科学准确率。保留原表per1000/百分号冲突、按分配分析与实际读片偏离、共识读片纳入及操作组成/时间未知。9文件包在本机禁读7份既有文件、拒绝网络和目录外写入的环境重绘，三种导出逐字节一致。首版线条遮字/重音遗漏、路径解析器错误、三次启动失败及字体发现警告均保留。205×140mm、最小8pt；未重跑试验、重算区间或新增保留论文。上述规则文字在终评冻结后归纳，尚未在另一任务单独完成行为回归。

## 部分质量耦合与跨格式公式（本地 1.44.1-dev）

[PASTE2 四面板原创图](../tests/batches/paste2-partial-coupling-01/README.md)先固定 36 元素、49 关系与 8 项要求，最终独立计分 8 项通过。图中区分容量不等式、总质量、成本混合权重及后续投影；零质量的投影适用性和补充方法缺口保留。先图后文阅读及来源知情复审未设置新错误对照，不计算 TP/FP。

第四版原生公式偏移超过 0.25 pt，第五版共享文字布局发生遮挡，两次失败均保留。第六版实际 183 个数学字形、两条分数线及 75 个矢量对象通过原定容差；普通文字另行核对。原生文字和路径保持可编辑，尺寸 280 × 284 mm、最小 8.4 pt。17 文件精确 ZIP 在本机操作系统隔离环境重绘六份导出逐字节一致，五项真实文件拒读、网络和目录外写入拒绝成立。精确字体是 SVG 的显式依赖；没有任意编辑器、跨机器或印刷保证。

以上两条条件规则在最终评估固定后归纳，尚未在另一案例完成独立行为回归；后续 LOUPE 首轮原生审计也发现文字/重音位置缺陷，其独立修复与复测见下节；不能把 PASTE2 的修复成功扩张为通用导出能力。正式原图高清版本、S1–S5、求解器、真实配准结果和生物学/临床验证均不在本次范围。


## 概率实现、训练替代量与原生重音（本地 1.44.1-dev）

[LOUPE 原创三面板图](../tests/batches/loupe-sampling-01/README.md)固定 30 元素、34 关系和 8 项要求，独立终评 8 通过、0 失败、0 未观察、0 不可判定。区分共享概率参数、期望二值数量、连续前向掩膜、固定傅里叶算子与仅更新 O/θ 的目标；最终二值选择和重训练初始化仍未知。先图后文阅读及后续来源知情复看未增加新错误对照或保留论文计数。

第四版原生文字偏移及 SVG 波浪号碰撞失败保留；第五版 1,287 字形、43 矢量满足原定 0.25 pt 容差。190 × 270 mm、最小 8.1 pt，三个组合波浪号采用字体证明的等价独立字形，原始 Unicode 不同。18 文件精确 ZIP 在本机沙箱重建 8 个导出逐字节一致，六项既有文件禁读、网络及目录外写入拒绝成立。字体警告、检查脚本路径错误，以及完成记录在冻结后追加字段的缺陷与独立更正记录保留。上述新增规则在终评后归纳；不称通用渲染、实物打印、跨宿主或专家验证，也没有执行原 MRI 模型。


## 共享上下文与条件返回（本地 1.44.1-dev）

[MultiVerS 原创三面板图](../tests/batches/multivers-context-decoding-01/README.md)在布局前固定 22 元素、23 关系和 8 项要求；独立终评 8 通过、0 失败、0 未观察、0 不可判定。图和完整图注区分给定输入对、共享编码与各头读出、预测标签控制的返回集合及严格阈值/条件性单句回退。原 SciFact 定义与简化定义、并列/空输入/截断等未知保留；没有执行原模型或新增保留论文。

第三版原生帽号和连续空格偏移失败保留。第四版共享文字布局后，独立复测全部 1,674 字形、34 矢量和 8 箭头满足原定 0.25 pt；350 × 292.25 mm、最小 8.085 pt。七个组合帽号采用字体证明的独立字形，原始 Unicode/轮廓不相同，忽略明确的无墨迹轮廓后才有可见轮廓等价。19 文件精确 ZIP 在本机固定沙箱重建七个规范导出逐字节一致；七项既有文件禁读及网络、目录外写入拒绝成立。渲染环境记录中的运行路径另行核对，不纳入字节相同范围。上述条件返回规则在终评冻结后归纳，尚未在另一任务完成独立行为回归；无跨宿主、任意编辑器或专家验收承诺。


[TARNet/CFR 三面板解释](../tests/batches/tarnet-factual-counterfactual-01/README.md)原定8项独立终评通过。汇合点选择公式修复了首稿的混合歧义；事实损失贡献与完整正则更新、固定两头条件均值差与识别假设分别表达。1025字形/63路径原生检查及32成员精确ZIP隔离重放完成，9导出字节一致，布局仅1033字体路径正规化。原生/渲染/阅读失败和4处来源差异继续保留；不增加新保留论文或专家验收数量。


[ESM报告汇总量图](../tests/batches/esm-threshold-burden-01/README.md)原定8项独立终评通过：8标量、20语义标签和3系列表达33%/12%/18%的不同分母及更正NNE8的首次达阈住院策略。762字形/24向量复测、静态精确字体SVG查看与22成员ZIP隔离重放完成，8规范产物字节一致。历史SVG字重失败、冻结映射元数据歧义与浏览器访问拒绝保留；浏览器字体解析、临床效果和原始数据复现未验证。


[aDBS中间区间比较](../tests/batches/adbs-state-buffer-01/README.md)原定8项独立终评通过。18对象/10关系将固定中间幅度与已知先前高/低幅度的条件保留分开，阈值等号、初始化、动态执行和blanking来源冲突保留。945字形/21矢量满足原定0.25pt、最小8.5pt；安全静态SVG核验不等于浏览器验证。21成员精确ZIP在本机隔离环境重绘9份规范产物逐字节一致，13份既有文件禁读及网络/目录外写入拒绝成立。首稿溢出、CSS审计误判和沙箱启动失败保留。终评后归纳先前状态依赖规则，尚未在另一案例独立回归；没有数值仿真、设备/临床验证或新增保留论文。


[FedBN参数族与聚合范围](../tests/batches/fedbn-parameter-ownership-01/README.md)原定F01–F08独立终评8/8。布局前10对象/10关系固定，本地两类可学习参数、周期性非BN平均与副本赋值、统计状态及测试例外分别表达；源内范围/术语/记号冲突与实现未知保留。348字形/25矢量、最小8.8pt，原生和精确字体静态SVG满足原定0.25pt；317实际绘制与317轮廓构造、31空格探针分开。27成员精确ZIP本机OS隔离重绘10份规范输出逐字节一致，16既有文件禁读及网络/目录外写入拒绝成立。原作者绘制证据误标和原重放“套接字创建拒绝”措辞均保留，更正分别归属清洁说明和同配置实际连接探针。终评后新增参数族/副本/阶段规则，尚未在另一案例独立回归；不增加新保留论文、原实验或专家验收计数。


[PAE参考坐标系与证据层](../tests/batches/pae-reference-frame-01/README.md)原定P01–P08独立终评8/8。20对象/21关系明确被评分位置、对齐坐标系、可能非对称的期望误差及同一交联的两处标记；物理距离判据与类别覆盖层分开。387字形/16路径、最小10.5pt，原生及精确字体静态SVG满足0.25pt；364实际绘制、364轮廓与23空格探针分别记录。28成员精确ZIP本机隔离重放10份规范输出逐字节一致，前后各50项控制含32个既有禁读文件，网络实际连接被拒。姓氏少n误报经实际原生证据撤回，无字母修复；原误报、根旧分类、N2映射范围澄清及全部运行失败保留。新规则文字未在另一案例独立回归；不增加新保留论文、原实验或专家验收数量。


[分割指标与容差角色](../tests/batches/surface-metric-roles-01/README.md)原定S01–S08独立终评8/8，范围为原创图与完整图注。21对象/33关系分开体积重叠、两侧有向距离及各自面积权重、距离容差和分数截点。889字形/18路径、最小9.5pt；757实际绘制、757轮廓和132空格探针分开，原生及静态SVG误差满足0.25pt。28成员精确ZIP在本机OS隔离重绘10份规范输出逐字节一致，前后各76控制含29个既有禁读文件，网络实际连接被拒。三条先图后文意见保持原文，两项由图注补足、DSC展开可选；四处来源/代码冲突及审计、重放、检查器失败保留。新增规则文字未在另一案例独立回归；没有数值指标、模型、临床或新保留论文验收。

[RAGChecker评价总体与条件分母](../tests/batches/ragchecker-evidence-metrics-01/README.md)的原定RC01–RC08独立终评8/8，30个有限检查均有证据。原创图与完整图注区分11指标的计数对象、支持方向、条件利用率和可重叠噪声类别。40成员ZIP在本机OS隔离重放10份规范输出含环境元数据逐字节一致；原边框误报、来源差异、范围措辞更正和运行失败保留。[单独两图对照](../tests/batches/ragchecker-denominator-control-01/README.md)的独立只看图与来源知情阶段均检出并定位解释1/1错误，正确图0/1误报；答案知情修复10产物与基线一致。评分顺序失败已保留并由新评分者重做，结果不并入本例八项；新归纳文字尚未跨案例独立回归。


[RNA velocity估计、映射与显示](../tests/batches/velocity-mapping-stage-01/README.md)的原定VM01–VM08独立终评8/8，34有限检查通过。21对象/26关系区分固定估计、计算性去除beta细胞、重新映射与流线显示，同一53细胞不重复计样本。1048字形最小10.4pt，四类最大误差均低于0.25pt；独立标签与节点颜色编辑已重导出和实际查看。25成员精确ZIP在本机五阶段OS隔离重绘10份规范输出含环境元数据逐字节一致，前后各102控制含41个既有文件实际禁读。方向文字范围歧义Q01、可选限定语V01、源内公式冲突、实现未知及审计/准备失败保留。仅计MCF053-F2一个部分核验单元；新规则文字未跨案例回归，未执行原RNA velocity实验。

[超声几何与动脉压力校准](../tests/batches/ultrasound-calibration-stage-01/README.md)的原定UC01–UC08独立终评8/8、31有限检查通过。15对象/18关系区分回波观测、直径/面积推导、外部袖带与几何校准及条件性压力估计，面积比保持平方。691字形最小9pt；基线、字距、字号、矢量最大差分别0.0009765625、0.0046875、0、0.0000122070313pt；独立原生/字体/墨迹检查、四类实际查看和两类独立副本编辑完成。27成员精确ZIP在同一OS配置五阶段七命令重绘10规范输出含环境元数据，逐字节一致；前后各102控制含40既有文件实际禁读及4项真实connect EPERM。三条初读歧义与三项Stage2建议保留；后者7类局限中4类由后续执行证据补足，来源未知/冲突仍在。557/556模块记录对应553/552独立文件的口径已补明。原方程7/8冲突、README修订和只读核验失败均保留；只计MCF054-F1一个部分核验单元，新规则文字未跨案例回归，未执行原测量或临床研究。



[Perceiver IO查询角色](../tests/batches/perceiver-io-query-roles-01/README.md)原定PI01–PI08独立8/8、32有限检查通过。11对象/14关系将三种注意力的Q/K/V来源、O查询与输出索引、通道宽度、潜变量形状与更新内容分开；任务查询示例有条件。835字形最小9pt，四类原生最大误差低于0.25pt，四类实际查看及两类独立副本编辑完成。27成员精确ZIP在本机五阶段七命令OS隔离重绘10规范输出含环境元数据逐字节一致，前后各102控制含40既有文件禁读及4真实connect EPERM。四项初读歧义、五项建议、E.1/E.2冲突、已知共享变体与初始化/宽度未知保留；旧读者中断及核验失败不被后续成功覆盖。只计MCF055-F2一个部分核验单元，入库一致性已核实；另行两图对照的图像优先及来源核对阶段均检出并严格定位1/1错接，正确图误报0/1，来源核对为主。评分者先封存断言后接收密钥；同一对照不重复计样本。评分后修复10规范文件与固定正确对照逐字节一致，不计新盲测、不并入32项；新归纳文字未跨案例回归。


[SelectiveNet训练目标与接受集风险](../tests/batches/selectivenet-evaluation-01/README.md)完成原定SE01–SE08独立8/8及36有限检查，作为MCF056-F2部分核验入库。25格均按训练行/校准列核对，50小数字符串与25个±保持原样；实际1239字形最小约9.2pt，四类最大原生误差均低于0.25pt。30成员ZIP在本机同一OS隔离配置重放10规范输出（含环境元数据）逐字节一致，前后各116控制包含45个既有数据文件拒读与4次真实connect拒绝。两类局部编辑和三阶段顺序独立读图完成，三处可选建议未实施；±定义、逐运行对应、来源概率界冲突与Figure2b/Table4疑问保留。原检查器/环境失败保留，不称原模型或统计实验复现。 本批归纳训练/校准/实测覆盖率、接受集分母和二维数值配对规则；新增文字尚未在另一案例完成独立行为回归。


[CLAM训练伪标签与注意力显示](../tests/batches/clam-training-pseudolabel-01/README.md)已完成原定CL01–CL08独立8/8及32有限检查，作为MCF057-F1部分核验入库。23对象/32关系/5主张、48项图内文字；1,520字形最小9pt，四类原生最大误差均低于0.25pt。互斥条件作用域与B定义两项必改已修复并独立复测；两类编辑与四视图完成。27成员ZIP在同一OS配置7条命令/5阶段重放10规范输出（含环境元数据）逐字节一致，前后各136控制含56个既有数据文件禁读和4次真实connect拒绝。三处源记号/公式冲突、实现未知、可选建议及历史失败保留，不称原实验或专家验收。本批归纳全量预测与训练子集、选中身份与伪目标、条件作用域及三种归一化角色；新增规则文字尚未在另一案例完成独立行为回归。


[GLUE特征与细胞耦合](../tests/batches/glue-feature-cell-coupling-01/README.md)完成原定GL01–GL08独立8/8和32检查。双输入解码器区分细胞表示与特征表示；观测重建目标、两类后验正则及模态监督分别表达，对抗项的直接数据编码器路径由完整图注明确。三阶段读图、原生与两项编辑验证完成；27成员ZIP的10规范输出含环境元数据在同一OS配置重放逐字节一致。四处源记号差异、可选建议和全部失败保留。新规则文字在本次有限验收后归纳，尚未在另一案例独立行为回归；不计研究复现或新保留论文。


[GRU-D缺失条件与衰减](../tests/batches/grud-missingness-decay-01/DELIVERY.md)已完成原定GD01–GD08独立8/8和32项检查，作为MCF059-F3部分核验入库。19对象/28关系/5主张、44项文字在布局前冻结；首稿F01乘法范围错误已修复，历史保留。三阶段读图、原生核对和两项局部编辑完成；1,580字形最小10.5pt，四类最大误差低于0.25pt。27成员ZIP在同一OS配置8命令重放10规范文件含环境元数据，逐字节一致；前后各140控制含58既有文件禁读及4真实connect拒绝。四项可读性建议、R23绑定冗余、来源张力、初始化与实现未知保留。新增规则尚未跨另一案例独立行为回归；不称原研究、专家、浏览器/编辑器或印刷验收。整体目标进行中，稳定1.44.0未改。

[GRU-D单独时间条件对照](../tests/batches/grud-temporal-mask-control-01/README.md)固定一错一对：仅图阶段确定TP0/FN1、条件疑点1，来源核对阶段确定TP1/FN0并准确定位、解释和提出修正1/1；两个阶段正确图的目标及全部无据语义误报均0/1。首次评分政策曝光顺序偏差保留，新评分者先读固定政策、分类封存后再接收答案；两图与读者记录未改，不重复计样本。评分后答案知情修复27输入、10规范输出与原版逐字节一致，完整预览及PDF独立渲染已实际查看。初始化未知、可选建议及来源张力保留；不计新盲测、跨案例回归或原研究复现。


[DINO教师、学生与中心状态](../tests/batches/dino-update-roles-01/DELIVERY.md)完成原定 DI01–DI08 的24项独立模型检查，24支持、0失败、0未评估；MCF060-F2仅作部分核验入库。15对象/23关系/5主张，42项文字；实际1,860字形最小12pt，独立原生SVG/PDF验证无整图栅格包装，梯度/参数EMA/中心EMA线型各自明确。两类局部编辑、先图后文阅读和同机OS重放完成。原包历史状态文字另在metadata02修订：科学内容及全部可见图文件不变，只更新状态与依赖哈希；新28成员ZIP的10规范输出含环境记录重放逐字节一致，7命令、前后各40控制，独立有限复核通过，不新增24项分母。原状态缺陷、审阅曝光限制、图像缩放、源符号/优化器差异、H记号建议及初始化未知保留。该规则在本例验收后写入，随后在读取UA-MT全文前固定并完成另一医学论文的有限应用检查；不是研究复现、新保留论文或专家验收。


[UA-MT不确定性选择](../tests/batches/uamt-uncertainty-gating-01/DELIVERY.md)完成原定UA01–UA08的24项独立模型评估，24支持、0失败、0未评估；MCF061-F1仅计一个部分核验单元。18对象/25关系/5主张保持原文监督域、先概率平均后熵、严格选择和分母，以及参数EMA区别。首版四项展示问题均修复，第二版上下标间距拒绝保留；第三版43文字对象/142原生段/1744字形最小12pt，独立原生检查覆盖全部字形、49上下标段、46矢量及78使用字符字体轮廓。两项实际编辑通过；28成员ZIP的10规范输出含环境记录在同机OS配置重放逐字节一致，7命令、前后各40控制。六项来源未知、图像缩放、审阅者知情复测及检查器失败均保留；不计研究复现、专家验收、新保留论文或本例受控错误检出率。DINO更新对象规则在本例全文前已固定，完成有界跨案例应用；新归纳的熵/选择和数学排版规则尚未跨另一案例验证。


[UA-MT单独阈值方向对照](../tests/batches/uamt-threshold-direction-control-01/README.md)固定一错一对；仅图和来源核对阶段的明确检出、严格定位、解释均1/1，正确图目标及全部无据科学误报均0/1。仅图修复仍为条件性、明确修复计0/1；来源核对后的明确正确修复1/1。政策先读、断言先封存、答案后开放；没有追溯升级初读结论。评分后恢复严格小于号，17输入和10规范输出与正确对照逐字节一致，预览及PDF渲染实际查看。原24项、病例数量和未知范围不变，不计新盲测或一般准确率。


[RAG检索与边缘化](../tests/batches/rag-marginalization-01/DELIVERY.md)作为MCF062-F1一个部分核验单元入库。22元素/33关系/6主张，49文字/142原生段/2268字形最小12pt；先图后文与任务分组修订复核、原生全对象审计、两项外观编辑及28成员ZIP重放完成。原固定24项终评为23支持、0失败、1未评估，原因是production03原生契约未列入早期哈希冻结。其后先固定16输入含契约再新导出，10规范文件与原版/ZIP/已有OS重放逐字节一致；独立有限复测支持当前24项，只有RG08.1重评，其余23项经字节一致性沿用，历史缺口未被追认。原OS重放7命令、前后各40控制仍限作者同机执行；新复测没有重新执行完整原生审计或OS重放。六类未知、三处来源差异、R1/R2建议、审阅曝光与所有失败保留。新归纳规则尚未跨另一案例验证；此前数学对象/轴/不交换次序的一般规则完成有界跨案例应用，不扩展为UA-MT熵/体素规则全部已验证。


[RAG单独文档混合算子对照](../tests/batches/rag-mixture-operator-control-01/README.md)：固定一错一对，仅图与来源核对阶段的明确检出、严格定位、后果解释及已明确提出的正确修复均1/1；正确图目标及全部无据科学误报均0/1。政策先读、44组断言先封存、答案后开放，条件疑点和来源措辞冲突不计检出或误报。计分后恢复内层求和，16输入及10规范输出与基线逐字节一致，完整预览与PDF渲染实际查看（后者显示缩小）。首次碰撞、ENOSPC、显示截断和补读记录保留。原24项、历史缺口、六类未知、三处来源差异及目录计数不变；不计新盲测、一般准确率或跨案例回归。


[QRS信号、条件状态与显示对齐](../tests/batches/qrs-signal-state-01/README.md)完成冻结 QS01.1–QS08.3 的24项独立模型证据评估：24支持、0失败、0未评估；按MCF063-F1部分核验入库。20对象/28关系/4主张在布局前固定。两阶段读图及定向措辞复查、独立原生SVG/PDF检查、两项实际外观编辑和28成员精确包重放完成。原生2,221字形最小13pt；PDF字形前进量最大误差0.006328125pt。独立显式FreeType静态路径的提示后前进量误差另计0.24853515625pt，均在原定0.25pt内；默认Quartz路径字体身份仍未确定，不作通用SVG兼容性保证。本机作者OS隔离7命令重放10规范文件逐字节一致，前后各40控制。来源未知、更正未读、编辑准备失败与审查器修正保留；没有ECG/检测器实验、错误/正确对照、新保留论文或专家验收。新增规则文字尚未在另一案例单独验证。


[QRS输出箭头对照](../tests/batches/qrs-output-direction-control-01/README.md)：QRS单独输出方向对照完成：固定一错一对，仅图与来源阶段的明确检出、严格定位、后果解释和明确修复建议均1/1，正确图目标及全部无据科学误报均0/1。政策先读、181条断言先封存、答案后公开；根核对208处原文引用。两个条件问题及原文转录问题分别处理，不重计样本。计分后恢复识别→脉冲，16输入、10规范输出和PDF渲染与基线逐字节一致；修复预览与PDF整页实际查看。两次评分输出截断已补读，显示片段和未知项保留。不新增科学规则、跨案例回归或原24项分母。


[HIL物理与仿真边界](../tests/batches/hil-controller-boundaries-01/README.md)：原定24项有限证据检查均获支持；MCF064-F1按一个部分核验单元入库。物理控制器、模拟CGM、估计状态、预测状态和第一项控制量分别表达；已告知餐食与未告知参数扰动不合并。比较边需绑定具体变量和基准，血糖轨迹对照不自动成为MATLAB与板端的计时对照；名义配置网格也不是成功运行数。首稿标签穿线、比较范围澄清及颜色编辑记录错写均保留并处理。当前33标签/1991字形、16元素/20关系，根执行原生核对和10文件精确包重放；不把有限检查称为控制器实验、临床验证、通用字体兼容或新的OS隔离测试。新归纳规则尚未跨另一篇论文验证。


[HIL评价参考错接对照](../tests/batches/hil-reference-loop-control-01/README.md)固定一错一对；仅图与来源阶段检出、严格定位和后果解释均1/1，但明确完整修复及含恢复要求的协议复合匹配均0/1。读者要求“保留”已被重定向移除的比较边，失败如实保留；正确图目标及全部无据科学误报均0/1。评分后根明确恢复REF→CMP并消除REF→KF，16输入、10规范输出和PDF光栅与author03逐字节一致，完整预览和PDF已看。原规则再次出现执行缺口，现细化错边/移除/恢复/保留四项核对；新措辞尚无独立行为回归。来源Fig8/Fig9B冲突保留条件性并另行修订主图。没有新论文、原图、OS隔离或盲修复样本。


[HIL来源限定修订](../tests/batches/hil-controller-boundaries-01/README.md)将Fig8 Quadprog血糖轨迹与Fig9B CVXOPT汇总条分开说明，并保留与省略结果正文的冲突。原author03固定24项保持旧版本范围；author04另有预定6项增量独立复核，6支持/0失败/0未评估。20关系、24向量和32其余标签不变，CMP.role收窄；当前33标签/2022字形，16输入预冻结、原生核对、实际整图查看和28成员包10输出重放完成。首轮ENOSPC失败保留，未知归属/容差/运行数不补齐；仍为semantic_partial，不新增病例、论文、盲测或OS隔离。


HIL修复要求的单次同读者复查已完成：能同时指出错边与缺失边并明确删除/恢复，正确图不提出改线，来源冲突及未知保留。根按事先两项检查作范围限定评估，两项获支持；结构化正确图“缺失边”内部另有继承措辞矛盾，未掩盖或计成新零误报证明。原两阶段完整修复0/1保留，未新增独立样本或新规则回归。 见[限定复查](../tests/batches/hil-reference-loop-control-01/repair-followup-root-assessment-01.json)。


2026-10-14 UTC，[CLAM端点恢复对照](../tests/batches/clam-edge-restoration-control-01/README.md)将显式当前/删除/恢复/保留要求应用于另一医学图和新任务读者。固定一错一对，两阶段对真实错接的检出、严格定位、后果解释均1/1，但完整修复及完整协议匹配均0/1；真正缺失的辅助目标未被识别或承诺恢复。正确图目标及全部无据科学误报均0/1；错图每阶段另有1项无据缺陷指控、2项当前边误读，分母不变。57组断言/54组边先分类封存，根核对290处引用后开放答案；最终评分81处精确证据读回。随后根已知答案修复，14输入、10输出和PDF光栅与正确基线逐字节一致，完整预览与PDF实际查看；原失败及未知保留，无读者复测。此跨案例应用揭示显式操作表仍不能保证线迹识别正确，新增先追踪当前端点再比来源的操作细化尚待新样本验证。不增加70条/64篇目录或原CLAM32项分母，不称一般准确率、提示改善、研究复现或新OS隔离。


2026-10-14 UTC，[SVG实际端点与修复操作](../tests/batches/svg-repair-geometry-01/README.md)新增标准库检查器及用法。直接读取自绘SVG的矩形、shaft/head和明确分叉，不以语义ID代替端点；核对删除/恢复/保留、必需边和实际后图完整有向路径清单。CLAM/HIL历史错误建议被拒绝，其实际修复匹配；DINO既有折线编辑保持20流程端点、4图例排除明确。原定12项当前run03为12/12，旧版8项独立有限复核另列。首轮普通分隔线误识别与测试程序退出保留；其G08/G09偶然拒绝未计作特定控制证明。根随后发现动态分叉随支线一起移走仍被旧工具错误接受，已保存falsepass，并添加前后图对指定载体路径的实际接触核对；预定追加2项软件检查2/2及2项独立增量复核均支持。原12、旧8、新2范围不合并成科学准确率。既有CLAM/HIL读者完整修复0/1不改；无新读者、论文、图稿或原科学项计数。当前70条/64篇与稳定1.44.0、入口原字节保持；补充仅在本地1.44.1-dev，未发布新稳定包。任意SVG、CSS/遮挡、标签/线型和科学语义仍需实际查看与来源核验。整体目标保持active。


2026-10-15，[UA-MT均值—熵端点对照](../tests/batches/uamt-mean-entropy-edge-control-01/README.md)完成既有案例的三阶段独立模型审读：一错一对一个故障，各阶段检出/定位/解释/完整修复/复合指标1/1；每阶段正确图目标及全部科学误报各0/1。572组断言先封存，根588处引用核对后开放答案；首版分类错误保留，02修正7标签，最终评分一次。几何辅助无科学修订，不能声称提高准确率。工具覆盖17/18箭头，文字源R24明确排除但科学/可见核验保留。根计分后实际修复，16输入和10输出与基线及既有ZIP逐字节一致，完整预览/PDF实际查看，后SVG17条端点与计划一致。构造短段、最终汇总命名碰撞及字段层级错误保留；修复非新盲样本。无新论文、原24项、OS隔离或一般准确率证明；70条/64篇及稳定1.44.0、入口未变，目标active。


[声明文字端口软件扩展](../tests/batches/svg-text-endpoint-01/README.md)：24个原生字形、两个完整run与固定偏移共同绑定UA-MT文字源；不从箭头或侧车包围盒推断实际字形边界。当前14/14文字、7/7样式、12/12原几何、2/2原分叉分别通过。根样式1/7失败历史与独立旧版探针保留；独立有限审阅中的PI/嵌套视口0/2经两个拒绝检查修复，独立增量2/2。其余六审阅条件沿用未改代码的历史有限检查，非新全面审计。两份静态渲染实际查看，当前输入与所看版本一致。这里只增加受限软件能力，不增加论文、科学读者样本、完整图文核验数或准确率；文字目标端点及其他字体/编辑器尚未验证。


## 报告差值和分析分母的跨案例应用（本地1.44.1-dev）

[EndoMind三个检出终点](../tests/batches/endomind-reported-risk-differences-01/README.md)在全文阅读前固定既有三条规则：原报差值/CI配对、实际分析分母、兼容单位及不合并相关终点。独立转录与先图后文读图均核对17标量；根按预先8项作有界证据汇总，8支持，非独立最终评分。保留PDR−0.8与显示比例相减−0.7之间的未明差异，不擅自“修正”原报量；462/452仅称论文排除后的ITT。实际两版原生核验及外观编辑、22成员包8输出同机重绘支持本例；59项软件检查每版另计，不是科学准确率。首次字体发现/比较选择器失败、SDR和多重性未知保留。不是新保留论文、试验复现或错误数值读者测试。


2026-10-15，[EndoMind报告差值对照](../tests/batches/endomind-reported-contrast-control-01/README.md)完成一错一对来源核对：检出、定位、解释、明确完整修复建议及复合匹配各1/1，正确图两类科学误报各0/1；仅图阶段不评来源正确性。分类先封存、答案后公开，最终57处回答引文与32处分类引用核对一致。根计分后只恢复PDR数字与点，10输入、8输出与正确基线及ZIP逐字节一致；完整预览与PDF实际查看。原报−0.8与显示率差−0.7的原因继续未知。两次比较脚本失败保留，不改变初始评分、原8项、历史CLAM/HIL失败或71条/65篇目录。没有新盲修复、专家审核、一般准确率或OS隔离结论。稳定1.44.0及入口保持；整体目标active。


[Tangram配对空间转移](../tests/batches/tangram-paired-spatial-transfer-01/README.md)把预先固定的身份层级、测量/推断与轴/方向规则用于新的组学论文；固定8项独立证据支持。源内RNA–ATAC配对不等于与空间参考逐细胞实测配对，RNA学得的M可在拟合后转移同源排列的A；可选f的数学含义与特定运行未知分别保存。全图和三种导出实际查看，外观改色保持原生文本/坐标/关系，同机21成员包重放8输出。来源张力、偏差与范围见报告；这不增加受控错误样本或一般准确率。新归纳的条件转移措辞尚未在另一案例独立测试。


2026-10-15，[Tangram ATAC分支对照](../tests/batches/tangram-atac-branch-control-01/README.md)在先追踪当前端点、再核对来源的既有流程下完成一次新读者应用。固定一错一对：来源知情检出/定位/解释/明确完整修复/复合匹配各1/1，正确图两类误报各0/1；错侧额外无据指控0，18条当前有向边另查无误。读者明确删除A→FIT并新增当前缺失的A→TRANSFER，保留其余关系及可选f条件；仅图阶段未计来源正确性。89组断言和410处引用先核对，答案后开放；根已知答案实际修复，9输入8导出与正确图、主图及ZIP一致，PDF整图实际复看。本例仅支持这一流程的有限应用，不证明提示因果改善；CLAM/HIL原完整修复0/1继续保留，不增加论文、科学分母、OS隔离或一般准确率结论。


[FLARE较后迭代](../tests/batches/flare-forward-sentence-01/DELIVERY.md)在详细根阅读前固定对象身份、条件路由及查询/生成区分三条既有规则，完成一张新开发图的固定8项独立评估，8支持。独立读者先只看图，后读官方来源；原生139项各版及差分9项、21成员包两类8输出重放单列软件证据。临时句子只用于选定的查询构造，重生成仍用旧前缀；首句初始化、两个阈值、解释性追加公式和来源未知各有范围。来源曝光、字体枚举与只读探查失败保留。本例未增加受控错误样本、新heldout或一般准确率；新归纳的临时/接受状态文字尚未跨另一案例行为回归。


2026-10-15 UTC，[FLARE重新生成输入对象对照](../tests/batches/flare-context-input-control-01/README.md)完成一错一对：来源知情检出、定位、解释、明确完整修复建议和复合匹配各1/1，正确图两类误报各0/1；仅图阶段不评分。204条断言先封存，根1,131处引用核对后公开答案；最终403处读者引用、10处原文引用、149处pin引用一致。根评分后恢复公式中的旧接受前缀，9输入、8规范输出与正确副本、主图及ZIP逐字节一致，PNG/PDF整图实际查看。最初箭头构造方案因判据不足被拒绝；封存API失败、显示脚本错误和评分后无关摘要暴露如实保存。历史CLAM/HIL完整修复0/1、FLARE主图8项及73条/67篇目录保持。无新盲修复、专家审核、一般准确率或新OS隔离；稳定1.44.0和入口未改。下一批fNIRS已核对原文/整图，13元素11关系语义规格固定并待独立核对，尚未出图或入库。整体目标active。


[fNIRS通道与PC贡献](../tests/batches/fnirs-channel-contributions-01/DELIVERY.md)把既有物理/计算角色及假设边界规则用于一个新医学信号开发案例；固定8项独立证据支持。13元素11关系明确协变量、目标、拟合系数和被扣除项，来源冲突与模型默认值未知保留。当前原生185项各版及21成员两次8输出重放单列软件证据。旧183检查遗漏重复ID，增加输入/实际SVG唯一性检查后旧对照失败两项；修复PDF/PNG不变。仅一个partial单元，不增加新heldout或一般准确率；本例后归纳文字尚未跨另一案例独立验证。


2026-10-15 UTC，[fNIRS减数操作对象对照](../tests/batches/fnirs-subtraction-operand-control-01/README.md)完成一错一对：来源知情检出、定位、解释、明确完整修复及复合匹配各1/1，正确图两类误报各0/1；仅图阶段不评分。170条断言先分类封存、根逐条引文核对后公开答案；最终10处精确引文与35处pin引用一致。读者明确把第一PC恢复为通道系数加权的双PC贡献，并保留已有定义/输入线。根评分后实际修图，9输入8规范输出与正确图、主图及实际ZIP逐字节一致，完整PNG/PDF已看。单项操作数变化不拆成两个错误；SCI来源措辞和实现未知保留。历史CLAM/HIL完整修复0/1不变；无新盲修复、heldout、研究复现或一般准确率。74条/68篇目录、稳定1.44.0及入口保持。下一批ACCESS已完成原表/正文及独立数字转录，3行报告值与11元素11关系排版前规格已固定，尚未出图或入库；整体目标active。


2026-10-15 UTC，[ACCESS筛查与条件性随访](../tests/batches/access-screening-denominators-01/DELIVERY.md)完成固定AX01–AX08独立评估，8支持、0失败、0未评。当前图保留81/81、18/82及16/25三组报告值与区间，区分随机人数、分析分母、筛查路径及阳性转诊子集。PR01图注修复后整图复看；50文本组/1312字形及三组实际数值映射核对，外观版只变一处填色。22成员包两次10输入重放均复现8规范导出；初次字体枚举失败、原生灰色假失败及comment假通过保留。CI构造、AI随访精确起点等未知保留；无新OS隔离、heldout、试验复现或一般准确率。终评后窄化同一照护事件可满足多个结局的措辞，尚未跨另一案例独立验证。分母显示对照预审完成，尚未构造或评分；整体目标active。


[ACCESS分母对照](../tests/batches/access-followthrough-denominator-control-01/README.md)：来源知情单故障的检出/定位/解释/明确完整修复/复合各1/1，正确对照两类误报各0/1。既有案例的完整人群81与转诊子集25不能互换；修复只恢复分母，不按错误分母重算百分比或区间。90条先分类断言和146处引用已核对；根已知答案实际修复10输入8输出与基线/ZIP相同。本例支持有限同案例应用，不证明跨案例泛化或提示因果改善；CLAM/HIL历史0/1保留。


[CLAM独立实际编辑](../tests/batches/clam-independent-edit-01/DELIVERY.md)补充既有规则的实际执行证据：先沿当前线迹确认错误端点、缺失端点和已有监督，再依原文形成编辑计划并重绘。此同案例新编辑者的实际完整修复终点1/1，精确输入重绘四导出相同；历史建议完整修复0/1保持。它说明本次可完成实际修复，不证明提示改善、一般准确率或新论文迁移。单图无正确对照分母，原生/字节检查与科学评估分列。没有据此新增通用科学规则。


[HIL独立实际编辑](../tests/batches/hil-independent-edit-01/DELIVERY.md)补充既有分离控制环与评价参考规则的实际执行证据：新编辑者识别错接及缺失比较输入，实际重定向并保留合法反馈；固定实际完整修复终点1/1，六输入四导出独立重绘一致。额外来源限定与一个错接故障分别记录。历史建议完整修复0/1保持；不是新论文、正确对照误报率或提示改善实验。此结果与CLAM实际编辑分别列示，不合并为一般准确率或新增通用科学规则。


## 2026-10-17：参数来源、更新状态与条件输出的有限迁移

[scArches条件适配器](../tests/batches/scarches-condition-adaptors-01/DELIVERY.md)把旧参数/新参数、冻结/更新、计算/优化分开；固定16元素22关系，独立最终8项支持。规则只验证于该泛化CVAE说明：冻结不代表不参与计算，新条件连接同时存在于编码器和解码器；不得搬用到未核查的模型实现。

潜在表示用于整合，不使普通带条件重建自动成为批次校正表达。观察协变量、模型参数及补齐缺失基因的零占位分别解释，不能互换为监督真值、参数计算或生物学零值。原文基模型差异与记号冲突仍保留。

图注的主语范围也需核对阶段：可说明读出没有额外训练步骤，不能由此否认此前查询拟合产生适配模型。本批初版图注确有该问题，来源审阅后单独修正；未倒填为图像初读检出。受限静态SVG检查与浏览器兼容性分开，转换器丢失虚线/字体的失败不能冒充图稿通过或图稿错误。


[scArches 参数更新错接与实际修复](../tests/batches/scarches-parameter-update-control-01/README.md)为既有“冻结仍计算、更新有明确对象”规则补充同案例执行证据：一处更新箭头错接的两阶段检出/定位/解释/修复建议各1/1，正确对照目标误报0/1；来源知情实际编辑另评1/1。只重定向目标线迹，43其余向量和50文本保持；5输入重绘9输出一致。先图后源、计划先于图源编辑、分类先于答案的记录各自保留，不将源ID辅助的实施计作新盲诊断。初读零填充疑问和输出措辞建议经原文核对后不强制改图；来源支持与实现未知分别处理。错误路径显著性、来源记号未决及同机/静态查看范围限定仍在。本批没有新增通用科学规则或提示改善因果结论，也不回写旧失败。


[scArches 假设性编码器解冻](../tests/batches/scarches-specified-unfreezing-change-01/README.md)补充实质内容变更的有限证据：原本共同冻结的继承参数拆为编码器/解码器子集，改变一组状态时保留另两组新增条件参数的优化路径；参数来源、优化资格和计算绑定分别表达。可训练不保证每个值变化，尤其新研究的一热输入在旧条件槽为零。改变编码器后，同步收紧Z的参考对齐/整合措辞，不能只改状态标签而沿用原方法性能。当前18元素25关系的独立8项通过，五输入九输出实际重放一致；仅一项同案例假设变更，无模型实验、一般准确率或新heldout证据。以上细化尚未在另一独立案例完成行为验证。


## 2026-10-17：事件拒绝、频率门控与控制可用性

[MCF071-F4膀胱设备方法图](../tests/batches/bladder-event-gated-control-01/README.md)支持一项有限表达规则：根据实际流程把校准参数、候选事件、事件拒绝、频率计数与定时动作分别表示。来源规定的拒绝支路必须在计数前生效；被拒候选返回监测，不能凭视觉简化直接触发执行器。控制软件暂停/恢复与LED开关是不同状态；无线数据通信也不自动表示无线供电。

原文数值互相冲突时，把冲突编号贴在受影响步骤附近，完整图注解释其计算后果。可核验定性路径与未解决采样率、历史窗或边界阈值分别验收，不能用8项图稿通过宣称原算法已复现。本例BC01–BC08独立8通过、5输入9输出重放相同，但三处来源冲突和记账/复位未知仍在；电池实验配置为Methods分配支持的推断。该方法图批次只含一项开发案例，未做错误/正确对照；后续对照单列于下文，仍无跨案例行为改善证据。


[膀胱拒绝支路对照及实际修复](../tests/batches/bladder-event-rejection-control-01/README.md)为上述规则补充同案例执行证据：单条拒绝支路错接到存活事件计数，在图像优先和来源知情两阶段的定位、解释及完整修复建议各1/1，正确对照确定误报0/1；实际编辑另评1/1。修复必须恢复拒绝返回监测，同时保留非拒绝候选进入计数；不能交换标签或让全部候选绕过计数。42文字/45其余向量保持，5输入9输出独立重放一致。原文三处数值冲突被识别为来源问题且保持未知，不是重构图误报。原Fig4的LED关闭后回采样路径可以按需进一步明确，但不由此补造计数复位/重触发实现。这是一项同案例行为测试，未证明跨案例或提示因果改善，不改写原图批次的范围。

## 已发表任务子集的跨图重汇总

[MedRAG 三任务四图测试](../tests/batches/medrag-examination-subset-01/README.md)为已有图组规则增加一次真实汇总数据内容变更证据：先按源定义固定任务集合，再逐表/配置重算三任务等权均值，原点值与原报±保持；新量明确标为由已舍入点值派生，不能沿用源五任务平均或推断新不确定性。范围图、主结果、明细、规格和图注共同更新；总体比较方向须重新检查，本例有三组模型的局部均值方向与源五任务结果不同。两表共享名义配置仍保留表键，不作独立重复。129组源值与43均值由两条独立路径核对，172个原生数值单元及23输出重绘检查完成；独立读图6完整+2部分的初评保留，根以旧稿91文件和原生/复现证据补齐8项。只支持这一案例的有限迁移，不是新论文、全七图改版、模型实验、一般准确率或新OS隔离证明。


## 残差阶次与无界区间的有限演示

[split-conformal-rank-01](../tests/batches/split-conformal-rank-01/README.md)用明确模拟数据完成三张图：七个残差保留并列观测，以校准数m而非总训练样本数或去重值数计算ceil((m+1)(1-alpha))；观察阶次越界时按来源定义使用+infinity。闭端点纳入候选，无界箭头与有限坐标窗口分开；alpha是名义未覆盖水平，候选纳入比例不是经验覆盖率。参数变更同步阶次/阈值/端点/几何/候选/文字/图注。独立7例、4状态、28归属及213数值文本对象核对一致，60原生区间组件另验；三图先看图审阅发现alpha未定义，修复后数值/几何不变。

实际--inputs文件须与被引用的来源哈希绑定，不能仅核对另一份规格相对路径；本次同形改值输入已在输出前拒绝。20规范输出从当前50文件干净副本重放相同，67成员ZIP逐字节/CRC读回。严格0.002pt文字定位156/287未达标保留，0.1pt独立读回是不同范围，不能替代前者；墨迹bbox中心也不是精确字形放置锚点。另两次检查器假设错误保留并单独修正。无统计覆盖验证、原实验复现、新错误检出/误报率或专家验收；本条归纳尚未在另一案例独立回归。


### 2026-10-17：普通原生文字的可比原点与基线

[三图非语义修复](../tests/batches/split-conformal-text-anchors-01/README.md)将名义居中/左对齐锚点与实际导出起点分开保存。不能用PDF墨迹bbox宽度代替布局advance来重建SVG text-anchor；旧156项失败中151项横向估计受此影响，而7项基线确有后端度量差异。对本固定DejaVu Sans/Matplotlib3.11.2单行非数学文本，预先按统一100pt无hint度量缩放与OS/2垂直指标计算左起点/基线，再向各后端显式输出left/baseline。独立287目标在生成前封存，同一0.002pt合同全部通过，最大目标差0.000036018pt；两份0.01pt原生单属性偏移各精确检出，原件坐标误报0/287。54项不变性/结构检查、实际看图及20输出逐字节重放支持这一次修复。首次字体字符串检查器假设失败保留，原156历史失败不回写。该证据不等于逐字形advance/轮廓/墨迹或浏览器一致，也不证明跨字体、数学、多行、旋转或跨机器通用；未新增研究样本或覆盖验证。


### 2026-10-17：连贯阶次错误的来源判读与独立实际编辑

[单故障对照及修复](../tests/batches/split-conformal-rank-control-01/README.md)为既有残差阶次/内容同步规则补充同案例执行证据：漏掉有限样本+1后，阶次、q、区间与成员标签可以全部内部自洽；来源知情的判定仍须定位定义，而不能仅用算术一致认定方法正确。独立来源阶段的检出/定位/解释/完整建议/复合各1/1，正确对照两类误报0/1；一般名义alpha域的无界分支后果也完整保留为同一故障的派生指控。

独立读者封存计划后实际改配置，恢复C7/q1.6及闭端点8.4/11.6，同时保留七个输入残差和预测10，实际完整修复另评1/1。固定独立原生预期103文字/22向量、实际PNG/PDF查看及10输入重新准备规格/11输出逐字节重放均完成。修复建议与实际编辑分开计数，原53个ID及条件/未知不重写；分类先于给键，七个指控侧面不扩成七个故障。没有新通用科学规则、跨案例行为或提示改善因果结论；新真值/覆盖率仍未知，旧文字失败历史保留。


## 公开MRI衍生体数据的三切面与索引重排

[medical-volume-reindex-01](../tests/batches/medical-volume-reindex-01/README.md)完成一份真实公开MRI衍生体数据的原数组、实际换轴/翻转与实际移动点三图。出图前独立oracle固定200,860个体素、两点和六个原生平面；原始值逐位保持，全部世界坐标最大差5.6843e-14mm。独立实际SVG/PDF的18个嵌入平面共63,822次像素比较无差异，物理几何最大误差3.26485e-5mm。来源知情读者仅2项完整、6项部分，原生检查和根72/72规范输出重放补足固定8项；不称一次读者全项通过。127成员包及48处来源路径/哈希已回读。

原灰度LUT的5,082次-1级偏差、预览DPI修复及检查器解释/序列化失败保留。由此归纳体素中心、数组/仿射/点同步、原生像素核验和空间身份限定；新细化尚未在另一体数据独立测试。仅给定qform的有限技术绘图，不增加论文/目录/heldout或误报率样本，不证明通用解析、原scanner/MNI空间、临床、跨机器/浏览器、印刷或新OS隔离。


## 体素值保持与空间映射正确须分别核验

[体数据仿射同步对照](../tests/batches/medical-volume-transform-control-01/README.md)为前述规则补充同一MRI衍生个体的有限执行证据：实际换轴/翻转后，正确原始数组和精确嵌入像素不能替代来源世界坐标检查。根据含翻转平移项的索引映射计算AoldQ，并由一个权威活动矩阵生成世界坐标、方向和物理几何；忠实导出错误矩阵仍会产生科学错误。本例错误点偏移73.3858mm，来源阶段检出/定位/解释各1/1，正确对照两类确定误报各0/1。

完整修复建议应明确保留原始NIfTI及其原始头信息；本例遗漏该明确要求，所以建议及复合评分0/1保持。后续实际计划与编辑保留原件，修改12个矩阵数值项，独立实际修复另评1/1；19个生成输出在18输入新进程重放中相同。修复后全部200,860体素的世界坐标及21,274次原生像素比较通过。规范文件相同与完整规格版本/审核状态不同分别报告，不能为字节一致而删除必要版本记录。

低分辨率预览的像素中心采样与原生嵌入矩阵核验应分列：本次150dpi的646/10530不符保留，600dpi同坐标诊断为0/10530；它支持本例采样栅格限制，不证明转换器内部舍入机制或任意预览可靠性。以上仍是一个已开发个体/单故障的条件证据，未在另一体数据独立回归，不提升为通用空间解析、临床或跨环境保证。


## 2026-10-17 非零校准与多源标注：BIDMC有限扩展

[双时间窗实际图稿](../tests/batches/medical-waveform-calibration-events-01/delivery-01/DELIVERY.md)补充已有波形/局部时间窗规则，同一公开记录不扩增论文或独立样本分母。

- 校准绑定保留通道标签、交织索引、显式baseline、gain及源单位，先提升数值类型再减baseline，不能用ADC zero替代显式baseline。本记录PLETH baseline=-63710已超出int16；三个通道的两窗原始字节到实际数值/几何由独立预期核对。当前代码仅支持所准入format16布局，不代表通用WFDB解析。
- 多标注者/多格式分别保留身份和原样本号。335保留事件支持本记录CSV sample−1，但五个ann1 CSV事件未出现在二进制且与ann2同刻，原因未知。保留CSV作绘图输入及冲突记录，不删除、自动合并或外推成通用索引规则。两窗没有同刻或恰落边界事件，这些绘制行为仍未测试。
- 内容修改先固定不变量和重算项。起点0→30秒后重选成员、幅值、事件与区间文字；局部横坐标网格可以相同，不能要求每个数字都变化。读图者确认源数据已有平台和局部极值，不由外形推断病理、设备饱和或绘图错误。

每个SVG/PDF含11,250波形顶点与24/22事件刻线，固定0.002pt合同最大误差0.000048060pt；根新进程24输出相同。先图后源的42条观察及不确定性保留，读者部分/未评端点由独立原生和根执行证据补充，不回填为其全项通过。8.5pt文字和完整导出实际查看，没有明确需改缺陷；可读性建议、源单位/标记定义/跨格式原因未知及五次前检/审计失败继续保留。新增条件经验只受本记录/本机渲染支持，尚未跨另一记录独立回归。


## 2026-10-18 UTC：捕获点复合身份、像素坐标与过滤同步

[两切片实际图稿](../tests/batches/spatial-capture-identity-filter-01/README.md)增加一项真实公开Visium坐标输出的有限适配证据，未增加论文、目录或保留迁移样本。

- 捕获点以(section_id, barcode)绑定源记录与原生图形。两文件各4,992行，条码字符串全部跨切片复用；相同条码或数组地址不能合并观测，也不支持生物学配对。独立检查9,984个复合记录与实际绑定；这仍是正例，尚无该故障检出率证据。
- 数组地址与完整图像像素分开使用：本地六邻接由数组差定义，显示用像素列作x、像素行向下作y，保持等像素比例。源in_tissue是提供的二元输出，不由显示掩膜推断分割正确、细胞数量、解剖方向或微米尺度。两个矢量格式的实际点位和页面变换分别核验。
- all→in_tissue=1过滤以两端均保留产生诱导子图，并保留度为零的点；同步点/边数、度数、图例和图注。局部视图先固定锚点及六个原始邻居，再与保留集相交，显示全部内部边；不能把视窗内其它点加入集合，也不能只保留锚点辐条。锚点局部度等于全图度有完整原始邻域依据，不能外推到所有局部节点。

每种SVG/PDF跨两范围核对17,317点和32条局部边，全图50,577条边记录另验；固定0.002pt容差下最大PDF误差0.000036361pt。根27生产输入、8次新进程生成48规范输出相同。独立读者32条原记录和SP01直接/其余7项部分核验保持，125次来源引用可定位；分工补证不回填为读者全项通过。原“1 edges”实际缺陷修复为“1 edge”，数据/几何保持；历史运行与审计器失败保留。浏览器预览受策略阻止，Cairo实际字体选择未核验；原生字体嵌入和PNG/PDF观察另列。本新增经验仅受两份坐标输出/当前本机实现支持，尚未跨另一数据集独立回归。


## 2026-10-18：跨切片坐标故障与正确对照误报

[单点坐标对照](../tests/batches/spatial-capture-identity-control-01/README.md)为既有复合身份规则补充同案例证据：同一barcode/数组地址仍须取本切片的源像素对。来源知情检出、定位、解释各完整1/1；目标源行缺失时保留未知1/1。完整建议因未明确同步派生绑定仅部分1/1；实际恢复两坐标分量并重新prepare/render后，独立实际修复另计1/1，19输入重放11项相同，不追认原建议。

正确B出现一个确定行偏移误报族，目标与任意科学误报控制图各1/1。独立原生和实际PNG测量表明菱形中心位于两侧圆点之间；不同轮廓下缘不是相同位置锚点。应按中心/约定锚点比较，并将预览目读不确定与确定源矛盾分开。该建议来自有限反例，尚未证明后续读者准确率改善，亦未确定本读者误报机制。13处重复主张不计13次试验，所有原断言/分类/一次评分保持。


## MOFA+ 分组变更与实际字符位置的有限证据

[分组迁移图对](../tests/batches/mofa-grouping-transfer-01/delivery-01/README.md)实际改变模型组而保留双视图：合并未按组中心化的X后重新中心化，使用新K_pool/Z_pool/W_pool，同步组先验、噪声索引、标签和图注。冻结K01–K12由独立来源知情读者逐项支持；这是一组相关方面和一次局部配置变更，不是12项独立样本。完整数据、Gaussian显示和未运行新拟合的边界保留；原始条件元数据不会自动保留旧模型组先验分支。规则文字是该有限试验后的归纳，尚未在另一案例独立回归。

相同嵌入字体不保证实际字距一致。本批先保留源/W整数截断失败，再保留浮点/W合格但当前MuPDF路径字符原点仍偏移的失败。以冻结文字片段原点加固定TTF hmtx累计值逐字符显式定位后，384片段/3106字符在原定0.002pt容差下由独立原生检查通过；原始Unicode、空格、字体和源语义绑定保留。source/W、实际字符原点、bbox和未观测末游标分别报告，未把任何一种替代另一种。SVG浏览器、其他文字整形/字体、任意编辑器和跨平台表现仍未验证；新表述不构成通用排版保证。


## MOFA+ 合并组中心化的条件与修复范围

[同案例中心化对照](../tests/batches/mofa-centering-control-01/README.md)区分“输出总体均值为零”与“按当前模型组对同一原始X中心化”。在完整观测、两个非空原组、相同变换与特征下，目标原组块为Y_old,g + 1(mu_g−mu_pool)ᵀ，mu_pool按N_g加权。旧Y直接堆叠可均值为零；只有原组逐特征均值相等时才与目标相同。未知实际均值不支持声称每个实例必不同，也不阻止定位该流程缺少一般保证。

仅有旧Y不能靠再次中心化恢复已去掉的原组均值；需要同一原始X或有来源的等价偏移信息。实际图按已确认路径表达输入需保留/取回、计算尚未执行，并同步活动节点、操作关系、绑定、图注与规格。读者两阶段检出/定位/解释完整，但修复建议1/2因同步不完整而保留；后续实际修复及32输入重放成功单独记录，不补分。新文字来自同一论文一组相关对照，尚未在另一数据案例独立验证，不构成普遍检出率或数值研究复现。


## 指定处理后的信号来源与条件性疑点（Open Ephys开发单例）

目标明确要求显示某个命名处理阶段之后的信号时，从输出端口逆向追踪实际前驱及路径；从Source绕过该阶段是目标来源不匹配，不能据此断言两个信号数值一定不同、该配置普遍非法或软件运行失败。物理采集可已有滤波，软件Source不等于完全原始信号；模块名称也不自动限制信号频段。源图中的替换弧线与数据流、反馈分别解释。

条件性疑点、可选建议与未知也必须具有真实可见的前提：先核实线或汇合是否存在，不能给不存在的支路添加解释或修复要求。可对同一候选单独复看；保留初次误读和随后撤回，不因后来更正而改写原记录。本例初读正确B出现一个不存在旁路/汇合的确定视觉误读族，目标类确定误报仍为0；两种结果分别报告。来源阶段同时增加文字与复看，不证明哪一项导致更正或读者心理机制。

[冻结对照及交付](../tests/batches/open-ephys-signal-chain-01/README.md)只有一个受控边源错误、一张正确对照和两个相关阶段。每阶段检出1/1、定位1/1、解释2/2、修复建议1/2、目标误报0/1；实际修复随后另行完成。建议若缺底层源/规格/绑定同步，不能由执行者后来的完整修复补成满分。这是已有同步和证据分类要求在本例的细化，新增文字尚未经另一案例独立行为验证，不外推总体准确率。


## MedMNIST：指标身份、来源可判定范围与字体判据纠错

相邻指标都落在合理范围内时，按数据集、方法/输入身份、metric字段追溯多级表头；点与标注一致只证明渲染忠实，不证明取对源列。[本例](../tests/batches/medmnist-reported-auc-01/README.md)纯图阶段隐藏错列不可评估，来源阶段才定位ACC0.812替代AUC0.857。普通语言明确身份/字段和派生同步即可构成完整建议，不强求未曝光私有文件名。实际修复另行执行字段更改、CSV重建、点/标签/绑定同步及精确ZIP重放；不由后来执行补评分。已报告均值不支持新增CI、显著性或ROC，图像数不是患者数。该有限开发对照不支持总体检出率或来源提示因果效应。

原生预期应核实固定运行库实际生效的字体度量路径；本例normal采用OS/2，lp是后备路径。最初每图16项baseline失败保留，见输出后改正oracle并保持全部容差和图稿不变；修复复核使用该已封v2。退出0不是内容通过，也不能把后验纠错记成预导出通过。该规则只受当前运行库/字体/布局支持，迁移需重新核实。包内旧来源措辞另以显式勘误撤回，冻结输入哈希不是其叙述真实的证明。新增细化尚未在另一案例独立行为回归。


## CheXpert：报告区间含义与概率集成层级

数值、端点和渲染完全一致，仍可能把抽样置信区间误标成训练运行间SD。按来源分别绑定指标、区间定义、评价单位、训练运行及checkpoint集成层级；30个模型概率的平均不等于30个AUROC均值，也不自动形成30个独立重复。只提供相互矛盾的候选标签时，原来源含义仍不可判定；补充来源后的判断不能追溯改写图像阶段。[本例](../tests/batches/chexpert-reported-ci-01/README.md)实际恢复全局interval_kind并重新生成可见标签、图注和绑定，保留15个报告值及原始舍入端点；不反推SD、不对称化CI、不凭排序/区间重叠产生显著性。源内排名冲突作为来源问题保留。

同一个固定TTF可因多字符连字产生多个PDF字体子集，字体文件数不能直接当作资源数预期。应从冻结整形记录及实际运行库规则推出角色，再核对ToUnicode/CID/GID、实际文字使用、字宽和保留字形轮廓。本例原每图1161/1162失败中的单资源假设，经看输出后以固定fl整形及标准CharacterTracker/fontTools规则改正；旧失败和全部原几何容差保留，修复前冻结v3。此为有限工程判据纠错，不追认原检查首次通过。一次开发对照及同机重放不支持总体检出率、提示因果效应或跨字体/平台保证；新增规则尚未另案例独立回归。


## Self-RAG：按阶段核对模型角色与解码量

图中产生“critic score”不自动意味着调用独立 critic 模型。按原文分别确定哪个参数实体在推理中产生 token、哪个模型仅用于离线训练材料构建，以及哪些量用于候选选择。[本例](../tests/batches/selfrag-reflection-producer-01/README.md)从 separate_C 改回 M 后，同步生产者关系、活动实体、可见标签、图注与导出绑定，保持检索器、条件路线和上下文；候选评分不能反过来改变阶段归属。一次实际修复通过并不补足盲审建议中遗漏的导出同步，本例建议仍为1/2。

表达条件的路径只绑定相应条件部分，不把它记作完整计算关系。No 条件提示进入 M 的延续角色，并不替代真实的 M→候选生成边；ISREL(x,d) 与 ISSUP(x,d,y) 的分组也不规定发射时序。原布局预检的条件绑定歧义及穿字竖线分别保留，修正后实际出图复看，不能用预检代替查看。

固定字体的原生预期应在导出前从实际整形规则推导。本例将 CheXpert 中发现的多字符连字分子集规则应用到新的 fl/fi/ffl 文本：导出前冻结预期，正确、错误和修复各1683项原生核对通过，未放宽容差或见输出后修改 oracle。这增加了同一字体/运行库下不同内容的有限支持，仍不证明跨字体、平台或任意编辑器兼容。两个相关读图阶段不提供来源提示的因果效应或总体准确率。


## multiDGD：固定参数、表示偏导与状态同步

来源确认普通推理只优化新细胞表示时，分别记录参数是否跨步更新、前向/密度是否计算，以及对哪些变量求偏导。固定theta仍可参与预测并传递关于z的梯度；固定phi仍可贡献潜在密度。对当前参数值求一次partial-z，不足以推断theta在后续步骤必定不变；该跨步状态应由相应方法阶段支持。观测深度s、预测均值y和学习到的特征离散度r也须分开绑定。

[本例实际修复](../tests/batches/multidgd-inference-update-01/README.md)恢复一个theta权威状态，再生成十个标签/主张/图注表现及规格、原生绑定，保留计算依赖。状态图示是参数角色断言，不冒充目标函数到参数的完整计算边。图中未展示更新算法，不自动构成违反当前抽象层级的错误；本例初读的完整性过强判断已单列保留。读者来源阶段建议仅1/2，后续完整执行不补分；两个阶段相关，不能推断来源提示的因果效果。

相同线型配置中，实线和虚线的连接属性可能独立。当前Matplotlib运行库只设solid_joinstyle未固定dash_joinstyle，导致原图对每张16项原生样式不符。显式设置虚线miter后，修复稿在原预期/容差下2633项通过；旧失败保留，未改盲审图或事后放宽判据。这些文字是本有限案例后的归纳，不是跨工具、字体、平台或另一科学案例的普遍验证。


## SynthSeg：共同网格与共同空间变换分别核对

生成图像及监督目标共享空间变换时，分别追踪二者使用哪一版解剖标签；形状、索引域或HR网格相同不证明位置一一对应。目标的类别映射q与图像的强度退化路径分开表达。固定q下，未变换标签q(L0)替代q(L)是否产生实际差异取决于保留类别位置是否变化；恒等、标签对称或被q消去的变化可相等，不能从源路径问题直接推出必然损失或性能下降。

[SynthSeg开发例](../tests/batches/synthseg-target-alignment-01/README.md)从一个权威目标来源恢复L，同步九个语义/显示/图注字段、R07端点及原生绑定。三处文字和一条路线是同一错误的表现，不扩大独立错误数。训练使用合成强度不意味着标签图上游或验证选择从未使用真实影像；来源范围及推理输入另行限定。读者未覆盖的上游来源和建议中缺失的完整同步继续单列，不能以执行者后来的修复补分。

最终包内活动定位符须从记录实际所在目录解析；原工作目录中的相对路径不能直接当作可移植路径。该例包02的五处状态证据定位错误经包03修复，并从包03实际解压重绘验证，旧失败与导出时pending快照保持。此处新增科学与交付细化受一个开发图对和同机重放支持，未形成一般检出率、来源提示因果效应或跨平台保证。


## 已报告百分数：单位转换与源精度分别绑定

绘制百分数时分别保存源表打印值、内部比例和显示单位，并规定只发生一次明确的转换。相同数值格式或一致坐标不能证明单位正确；同一倍率造成多处点、标签和图注错误仍是一项错误家族。由一个活动字段重算完整依赖，包括数值、直接标值、坐标、语义/原生映射、图注及导出；原始事实、模型身份、精度和未核实分母保持独立。

[Guo2017校准开发例](../tests/batches/calibration-percent-conversion-01/README.md)的20个已报告ECE单元经过实际错误输入修复及最终ZIP解压重放。ECE的样本数加权与15等宽置信度箱不等于等箱平均；模型名SD在该表表示stochastic depth，不能当作误差棒。源文数据划分不能未经核实变成每行n。真实数据不足时不补置信区间、可靠性曲线或显著性。

纯图的源忠实度保留NA；“这组数值较小，可考虑调整坐标范围”可属于条件性呈现建议，不能自动归入来源错误误报。揭键前逐条判定主张及其前提；后来执行者完整修复不提高原读者解释/建议分数。本例解释与建议各1/2，未形成检出率、来源提示因果效应或独立行为回归。


## MCF080：重复残差块的两种状态与完整图覆盖

Ribeiro2020 Figure3的同一残差块类型产生两个不同角色：加法和z供下一skip，BN→ReLU→Dropout后的x供下一main。修复tap时，同步实际路径、分叉点、四个实例的状态定义、通用公式、标签、图注和来源归属；保留主路径以及最后一块没有后继skip消费者的边界。相同块类型不推出共享参数，展开用的虚线不作为计算边。一次共享规则扰动算一个错误测试，不按四个实例扩增样本。

[本例证据](../tests/batches/ecg-residual-state-01/root-final-acceptance-01.json)：全27元素／28张量边／2展开关系；实际1权威＋37派生字段修复；独立原生检查与整图查看；最终ZIP解压后17输入、11输出逐字节重放一致。只在材料支持的算子／状态抽象下记完整图核验，不据此推定完整可执行架构、原始实验或临床效用。

修复验收与原读者表现分开：原建议1/2及4个不支持句子实例保留；正确对照0/1目标误报不代表所有陈述正确。此规则细化由本开发案例支持，尚未作为新规则在另一案例做独立行为回归。


## MCF081-F3 — late interaction reductions and native mathematical typography

For a source-defined `sum_i max_j cosine`, draw each document candidate into every applicable local maximum and carry exactly one local scalar per query position into the query sum. Replacing max by mean can remain internally coherent while changing source fidelity; keep axis, local output, labels, equation, caption and provenance synchronized when restoring the source method. Shared BERT does not establish separately unspecified projection tying; an offline enclosure indicates precomputation/storage, not frozen training parameters. Evidence: `cases/MCF081-colbert-late-interaction/MCF081-F3.json`.

Source notation is an input representation, not proof of a finished formula. Formal math export must place indices and operator limits as actual native glyphs, then check actual glyph mapping/advance, attachment/row clearance and whole/detail pixels. Here six logical labels became48 positioned runs plus15 unchanged text records; graph21/33 stayed fixed. Original raw notation and its limitation remain historical. Actual79-member ZIP replay preserved17 repaired inputs and8 original exports before regenerating8 formal exports from extracted typography. Byte identity reuses initial native acceptance; it is not a second native audit. This is one bounded development example, not a general parser or performance guarantee; no cross-case rule regression is claimed.


## MCF025-F1 whole reassessment — fusion interfaces and synchronized repair

For corresponding C-channel cropped/upsampled operands, channel concatenation yields2C while indexwise addition yieldsC; a following convolution must consume the selected input width while its output width may stay unchanged. Equal shape alone does not prove feature correspondence or source fidelity. Under fixed aligned operands and an immediate linear convolution, concatenation permits independent operand subkernels; addition followed by that convolution induces the same subkernel on both summands. This conditional local distinction does not establish inevitable network predictions or performance.

A source-faithful operator repair must synchronize all instances and their operand/receiving interfaces, labels, formulas, scientific relation descriptions, caption and provenance, then regenerate and inspect actual native outputs. This case applied1authority+42derivedchanges and retained1018leaves, all28mainmaps/4copies/4logicaljoins and39relations. Four scales remain one shared-rule test. Source-reader explanation/proposal each1/2 and two unsupported color descriptions remain separate from the actual repaired artifact acceptance. Evidence: [whole-case acceptance](../tests/batches/unet-whole-reassessment-01/root-final-acceptance-01.json).

Inspect native file semantics within an explicit parser envelope. SVG style without a type attribute uses the CSS default ([SVG2 styling](https://www.w3.org/TR/SVG2/styling.html#StyleElement)); a validator must not require an attribute the standard defaults. U-Net v4 corrected this specific false rejection without changing formal output; earlier failed native records remain. Package manifests also require duplicate-key/nonfinite-JSON rejection and closed fields before writes. Those corrected tools passed bounded pure probes and actual104member ZIP extraction/17input+8export replay. Byte identity retains the original accepted native result; it is not another independent native test. No cross-case behavioral regression or universal parser guarantee is claimed.



## totalVI whole figure — probability roles and source-bounded queries

For paired modalities, preserve the common cell axis while separating feature axes. Trace posterior distributions, their means and their samples independently; decoder parameters, latent nuisance quantities and feature-specific global dispersions have different roles. A mixture probability needs an explicit component assignment: with pi=Pr(BG), foreground weight is 1−pi, and a posterior query such as E[(1−pi)beta alpha] is not simply an observed count or an arbitrary point estimate. Changing a convention must synchronize labels, definitions, caption and every affected derived expression; repeated manifestations remain one shared-rule error.

Source prose and algorithm may disagree at a boundary. This example retains alpha>1 versus ReLU+1/[1,infinity), so separately specified component means do not imply guaranteed unequal numeric values. Whole-figure task callouts retain all named uses while documenting the further Methods-level conditioning and integration; source-supported grouping is not an invented direct computational edge. Evidence: [MCF003 whole-case record](../cases/MCF003-totalvi/MCF003-F1-whole-reassessment-01.json).

A native inspector must distinguish applicable paint state: a fill-only PDF drawing can have no dash value; painted strokes still require the frozen dash, geometry, cap/join, opacity and font checks. The retained v1 false rejection was corrected in v2 without changing tolerances. Final simple-vector/text artifacts passed actual native inspection and whole/detail views, then exact ZIP extraction replay. This bounded development result does not validate arbitrary PDF syntax, editors or environments. Original reader repair remains partial despite complete later execution; these refinements precede the planned two-paper transfer freeze.


## 2026-10-19：当前 RAG 全流程与宿主来源路径维护

- 相对来源文件以输入规格所在目录解析；导出前确认存在，再按交付规格目录重新计算相对路径。当前 render.py 对含本地文件的直接 API 调用要求输入规格路径，避免依赖进程工作目录；来源缺失在创建输出前失败。8项来源路径测试、修复后16项核心与2项调度复测通过。测试固定当前源文件路径关系，不声称将外部文件自动复制进交付包。
- 假设的实质方法修改应在目的、图中标签、图注与来源依赖中明确，单纯结构检查不等于这些内容正确。当前 changed_spec.json 的旧元数据及路径错误、失败产物和修复前程序均保留。仅外观修改保持关系与文本语义。
- MedRAG 本次只覆盖固定 GPT-3.5／MedCorp／RRF-4 配置，问题进入检索、选项进入生成、gold仅进入评分；不能把 Figure1 的基准组成称为算法流程。GraphRAG 索引、查询和模型评价角色分开；原文附录标题与提示角色不一致时，保留冲突并明确主文依据。两项为既有论文来源限定维护，未计新独立迁移。
- 实际宿主看图须保留 imageView 等可观察事件与当时文件哈希；完成文字的看图自述不能补足缺失轨迹。当前1个端到端案例保留3次尝试，第三次的8次实际事件仅支持该次。原固定回归54项、5个路由调用、1个端到端案例及修复后8／16／2项复测保持各自分母。
- 本段在本批导出和最终 ZIP 重放结束后归纳。两图各39文件，实际重建5项准备与8项导出一致；原生18380／15087项是技术断言，不是独立科学试验。宿主3.13.9、核心3.14.0及 ZIP 3.14.0依赖分别记录；本次结果不证明跨平台、专家审阅、研究复现或新稳定发布。没有把本段新增文字追认成此前已冻结规则或新增跨案例迁移检验。

证据：[当前宿主回读](../tests/host/m2-current-1.44.1-dev-01/root-host-readback-01.json)、[源修复及复测](../tests/host/m2-current-1.44.1-dev-01/source-repair-01/verification-02/local-source-results.json)、[两工作流交付](../tests/batches/m2-rag-workflow-01/README.md)。原11类失败／证据局限见执行报告；其中4个早期原生JSON被当时检查器覆写、初始字节未另存，不能宣称每个中间报告均有原始字节快照。

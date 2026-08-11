“鸢尾花书”的整体布局数学 + Python编程 + 可视化 + 机器学习实践工具数据可视化 Python编程线性代数数学基础概率统计实践回归、降维分类、聚类数据分析数学

“鸢尾花书”的学习顺序

Python零基础Python有基础草稿、Python 打磨、视频清华社五审五校上架

1编程不难100% 2024, 01进行中

2可视之美100% 2024, 01进行中

3数学要素100% 完成完成完成

4矩阵力量100% 完成完成完成

5统计至简100% 完成完成完成

6数据有道50% TBD

7机器学习100 % 2024年中进行中分册进度状态

Book 1《编程不难》预备编程不难聊聊巨蟒安装使用 Anaconda

JupyterLab，用起来

Python数据类型

Python运算

Python控制结构

Python函数

Python面向对象编程Python语法，边学边用语法聊聊可视化二维和三维可视化

Seaborn可视化数据绘图数学应用使用Spyder

Streamlit 搭建Apps

Streamlit 机器学习 AppsNumPy索引和切片

NumPy常见运算

NumPy数组规整

NumPy线性代数

NumPy爱因斯坦求和约定聊聊NumPy

数组Scikit -Learn数据

Scikit -Learn回归

Scikit -Learn降维

Scikit -Learn分类

Scikit -Learn聚类Scikit -Learn机器学习机器学习数据Pandas可视化

Pandas索引切片

Pandas规整

Plotly统计可视化

Pandas时间序列聊聊Pandas

SymPy符号数学

SciPy数学运算

Statsmodels 统计模型

Book 2《可视之美》图说可视之美数学 + 艺术说图布局美化色彩空间颜色映射色彩代数数列函数二次型网格曲面三维等高线箭头图立体几何三维线图三维三维散点隐函数参数方程复数装饰二维极坐标平面等高线热图和其他平面几何平面线图平面散点模式 + 随机模式 + 随机

Dirichlet分布贝塞尔曲线繁花曲线分形网络图几何心形线瑞利商奇异值分解立体几何变换平面几何变换距离

Book 3《数学要素》基础算数几何代数概率统计概率统计坐标系二维三维微积分导数偏导数微分积分优化入门线性代数向量鸡兔同笼三部曲数学要素解析几何距离圆锥曲线函数可视化代数函数超越函数二元函数数列

Book 4《矩阵力量》向量定义运算范数空间几何曲线曲面矩阵定义运算微积分多元微分拉格朗日乘子法数据矩阵力量向量空间矩阵分解各种分解

Cholesky 分解特征值分解奇异值分解分块矩阵定义几何变换投影数据投影直线到超平面多元统计入门数据空间数据分解数据应用

Book 5《统计至简》统计概率统计全景统计描述贝叶斯派贝叶斯统计推断马尔科夫链概率频率派频率统计推断概率密度估计椭圆高斯随机贝叶斯分类马氏距离线性回归主成分分析古典概率模型离散随机变量离散分布连续随机变量连续分布条件概率一元二元多元条件协方差矩阵随机变量的函数蒙特卡洛模拟统计至简

Book 6《数据有道》Book 7《机器学习》机器学习回归回归分析多元线性回归非线性回归正则化贝叶斯回归高斯过程分类决策树核技巧支持向量机高斯判别分析朴素贝叶斯分类k近邻聚类谱聚类密度聚类层次聚类最大期望算法高斯混合模型K均值聚类降维主成分分析截断型奇异值分解主成分分析进阶主成分分析与回归核主成分分析典型相关分析开源资源

com/Visualize -ML

bilibili.

com/513194466

zhihu.

com/people/jamestong -xue

专属邮箱：jiang.

visualize.

Page 1 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com Preface

前言感谢首先感谢大家的信任。作者仅仅是在学习应用数学科学和机器学习算法时多读了几本数学书多做了些思考和知识整理而已。知者不言，言者不知。知者不博，博者不知。水平有限，把自己有限所学所思斗胆和大家分享，作者权当无知者无畏。希望大家在 B站视频下方和 Github多提意见，让这套书成为作者和读者共同参与创作的优质作品。特别感谢清华大学出版社的栾大成老师。从选题策划、内容创作、装帧设计，栾老师事无巨细、一路陪伴。每次和栾老师交流，我都能感受到他对优质作品的追求、对知识分享的热情。出来混总是要还的曾几何时，考试是我们学习数学的唯一动力。考试是头悬梁的绳，是锥刺股的锥。我们中的绝大多数人从小到大为各种考试埋头题海数学味同嚼蜡甚至让人恨之入骨。数学给我们带来了无尽的折磨。我们憎恨数学，恐惧数学，恨不得一走出校门就把数学抛之脑后、老死不相往来。可悲可笑的是我们其中很多人可能会在毕业的五年或十年以后因为工作需要不得不重新学习微积分线性代数、概率统计悔恨当初没有学好数学走了很多弯路没能学以致用从而迁怒于教材和老师。这一切不能都怪数学，值得反思的是我们学习数学的方法、目的。再给自己一个学数学的理由为考试而学数学，是被逼无奈的举动。而为数学而数学，则又太过高尚而遥不可及。相信对于绝大部分的我们来说，数学是工具、是谋生手段，而不是目的。我们主动学数学，是想用数学工具解决具体问题。现在，这套书给大家一个 “学数学用数学 ”的全新动力——数据科学机器学习。数据科学和机器学习已经深度融合到我们生活的方方面面而数学正是开启未来大门的钥不是所有人生来都握有一副好牌但是掌握 “数学 + 编程 + 机器学习 ”绝对是王牌。这次，学习数学不再是为了考试、分数、升学，而是投资时间、自我实现、面向未来。未来已来，你来不来？本套丛书如何帮到你

Page 2 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 为了让大家学数学、用数学，甚至爱上数学，作者可谓颇费心机。在创作这套书时，作者尽量克服传统数学教材的各种弊端让大家学习时有兴趣看得懂、有思考更自信、用得着。为此，丛书在内容创作上突出以下几个特点：◄ 数学 + 艺术——全彩图解极致可视化，让数学思想跃然纸上生动有趣、一看就懂提高大家的数据思维、几何想象力、艺术感；◄ 零基础——从零开始学习 Python编程从写第一行代码到搭建数据科学和机器学习应用；◄ 知识网络 ——打破数学板块之间的壁垒让大家看到数学代数几何、线性代数微积分、概率统计等板块之间的联系，编织一张绵密的数学知识网络；◄ 动手——授人以鱼不如授人以渔和大家一起写代码用Streamlit 创作数学动画

App；◄ 学习生态 ——构造自主探究式学习生态环境“微课视频 + 纸质图书 + 电子图书 + 代码文件 +

可视化工具 + 思维导图 ”，提供各种优质学习资源；◄ 理论 + 实践——从加减乘除到机器学习丛书内容安排由浅入深螺旋上升，兼顾理论和实在编程中学习数学，学习数学时解决实际问题。虽然本书标榜 “从加减乘除到机器学习 ”

但是建议读者朋友们至少具备高中数学知识。读者正在学习或曾经学过大学数学 (微积分线性代数、概率统计 )

这套书就更容易读了。聊聊数学数学是工具。锤子是工具，剪刀是工具，数学也是工具。数学是思想。数学是人类思想的高度抽象的结晶体。在其冷酷的外表之下，数学的内核实际上就是人类朴素的思想。学习数学时，知其然，更要知其所以然。不要死记硬背公式定理，理解背后的数学思想才是关键。如果你能画一幅图、用大白话描述清楚一个公式、一则定理，这就说明你真正理解了它。数学是语言。就好比世界各地不同种族有自己的语言，数学则是人类共同的语言和逻辑。学这门语言极其精准、高度抽象，放之四海而皆准。虽然我们中绝大多数人没有被数学女神选中，不能为人类的对数学认知开疆扩土；但是，这丝毫不妨碍我们使用数学这门语言。就好比，我们不会成为语言学家，我们完全可以使用母语和外语交流。数学是体系。代数、几何、线性代数、微积分、概率统计、优化方法等等，看似一个个孤岛，实际上都是数学网络的一条条织线。建议大家学习时，特别关注不同数学板块之间的联系，见树，更要见林。数学是基石。拿破仑曾说 “数学的日臻完善和这个国强民富息息相关。”数学是科学进步的根基，是经济繁荣的支柱，是保家卫国的武器，是探索星辰大海的航船。数学是艺术。数学和音乐、绘画、建筑一样，都是人类艺术体验。通过可视化工具，我们会在看似枯燥的公式、定理、数据背后，发现数学之美。数学是历史，是人类共同记忆体。”历史是过去，又属于现在，同时在指引未来。”数学是人类的集体学习思考她把人的思维符号化形式化，进而记录积累、传播、创新

Page 3 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 骨、泥板石板、竹简、木牍纸草、羊皮卷活字印刷、纸质书到数字媒介，这一过程持续了数千年，至今绵延不息。数学是无穷无尽的想象力是人类的好奇心是自我挑战的毅力是一个接着一个的问题是看似荒诞不经的猜想是一次次胆大包天的批判性思考是敢于站在前人的臂膀之上的勇气是孜孜不倦地延展人类认知边界的不懈努力。家园、诗、远方诺瓦利斯曾说：“哲学就是怀着一种乡愁的冲动到处去寻找家园。在纷繁复杂的尘世，数学纯粹的就像精神的世外桃源。数学是，一束光，一条巷，一团不灭的希望，一股磅礴的力量，一个值得寄托的避风港。打破陈腐的锁链把功利心暂放一边我们一道怀揣一分乡愁心存些许诗意踩着艺术维度，投入数学张开的臂膀驶入她色彩斑斓变幻无穷的深港感受久违的归属一睹更美、更好的远方。Page 4 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com Acknowl edgement

# 致谢

To my parents.

谨以此书献给我的母亲父亲

Page 5 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com How to Us e the B ook

使用本书丛书资源本系列丛书提供的配套资源有以下几个：◄ 纸质图书；◄ PDF文件，方便移动终端学习；请大家注意，纸质图书经过出版社五审五校修改，内容细节上会和 PDF文件有出入。◄ 每章提供思维导图，纸质书提供全书思维导图海报；◄ Python代码文件，直接下载运行，或者复制、粘贴到Jupyter运行；◄ Python代码中有专门用Streamlit开发数学动画和交互 App的文件；◄ 微课视频，强调重点、讲解难点、聊聊天。在纸质书中为了方便大家查找不同配套资源，作者特别设计了如下几个标识。引出本书或本系列其他图书相关内容提醒读者格外注意的知识点每章配套微课视频二维码配套 Python代码完成核心计算和制图用Streamlit开发制作App应用介绍数学工具、机器学习之间联系数学家、科学家、艺术家等语录代码中核心 Python

库函数和讲解思维导图总结本章脉络和核心内容相关数学家生平贡献介绍每章结束总结或升华本章内容本书核心参考和推荐阅读文献微课视频本书配套微课视频均发布在 B站——生姜 DrGinger：bili bili.

com/5 131944 66

Page 6 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 微课视频是以“聊天”的方式和大家探讨某个数学话题的重点内容讲讲代码中可能遇到的难点，甚至侃侃历史、说说时事、聊聊生活。本书配套的微课视频目的是引导大家自主编程实践探究式学习，并不是“照本宣科 ”。纸质图书上已经写得很清楚的内容，视频课程只会强调重点。需要说明的是，图书内容不是视频的“逐字稿”。代码文件本系列丛书的 Pytho n代码文件下载地址为：com/Visualize -ML

Python代码文件会不定期修改，请大家注意更新。图书配套的 PDF文件和勘误也会上传到这个GitHub账户。因此，建议大家注册 GitHub账户给书稿文件夹标星 (star) 或分支克隆 (fork)。考虑再三，作者还是决定不把代码全文印在纸质书中，以便减少篇幅，节约用纸。本书编程实践例子中主要使用 “鸢尾花数据集 ”

数据来源是 Scikit-learn库

Seaborn库。外，系列丛书封面设计致敬梵高《鸢尾花》要是给本系列丛书起个昵称的话作者乐见“鸢尾花

App开发本书几乎每一章都至少有一个用 Strea mlit开发的App

用来展示数学动画数据分析、机器学习算法。Streamlit 是个开源的 Python库能够方便快捷搭建部署交互型网页 App。Streamlit 非常简单易用、很受欢迎。Streamlit兼容目前主流的 Python数据分析库比如 NumPy

Pandas

Scikit-

learn、PyTorch、TensorFlow 等等。Streamlit还支持 Plotly

Bokeh、Altair等交互可视化库。本书中很多 App设计都采用 Strea mlit + Plotly 方案。此外，本书专门配套教学视频手把手和大家一起做 App。大家可以参考如下页面，更多了解 Streamlit：io/gallery

stream lit.

io/library/api -reference

实践平台本书作者编写代码时采用的 IDE (integra ted development environme nt) 是Spyder

目的是给大家提供简洁的 Python代码文件。但是，建议大家采用 Jupyter Lab或Jupyter notebo ok作为本系列丛书配套学习工具。简单来说，Jupyter集合“浏览器 + 编程 + 文档 + 绘图 + 多媒体 + 发布”众多功能与一身适合探究式学习。Page 7 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 运行 Jupyter无需 IDE，只需要浏览器。Jupyter容易分块执行代码。Jupyter支持 inline打印结果，直接将结果图片打印在分块代码下方。Jupyte r还支持很多其他语言，比如 R和Julia。使用 markdown文档编辑功能，可以编程同时写笔记，不需要额外创建文档。Jupyter中插入图片和视频链接都很方便。此外，还可以插入 Latex公式。对于长文档，可以用边栏目录查找特定内容。Jupyter发布功能很友好，方便打印成 HTML、PDF等格式文件。Jupyter也并不完美，目前尚待解决的问题有几个。Jupyter中代码调试不方便，需要安装专门插件 (比如debugger )。Jupyter没有 variable explorer

要么 inline打印数据要么将数据写到 csv

或Excel文件中再打开。图像结果不具有交互性，比如不能查看某个点的值，或者旋转3D图形，可以考虑安装 (jupyter -matplotli b)。注意，利用 Altair或Plotly绘制的图像支持交互功能。定义函数，目前没有快捷键直接跳转到其定义。但是，很多开发者针对这些问题都开发了插件，请大家留意。大家可以下载安装 Anaconda

JupyterLab

Spyder

PyCharm等常用工具都集成在 Anaconda

下载 Anacon da的地址为：anacond a.

com/

学习步骤大家可以根据自己的偏好制定学习步骤，本书推荐如下步骤。浏览本章思维导图，把握核心脉络1

下载本章配套

Python代码文件2

观看微课视频，阅读本章正文内容3

用Jupyter创建笔记，编程实践4

尝试开发数学动画、机器学习 App5

翻阅本书推荐参考文献6

学完每章后，大家可以在平台上发布自己的 Jupyter笔记进一步听取朋友们的意见这样做还可以提高自己学习的动力。意见建议欢迎大家对本系列丛书提意见和建议，丛书专属邮箱地址为：◄ jiang.

visualize.

c om

也欢迎大家在B站视频下方留言互动。Page 8 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com Contents

# 目录

Page 9 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

0 Introducti on

绪论图解 + 编程 + 实践 + 数学板块融合

0.1本册在鸢尾花书的定位首先祝贺大家完成 “数学”板块的学习同时欢迎大家来到鸢尾花书第三板块 ——实践。“实践”这个板块我们将会把学到的编程可视化，特别是数学工具应用到具体的数据科学、机器学习算法中，并在实践中加深对这些工具的理解。“实践”这个板块有两本书：《数据有道》、《机器学习》。鸢尾花书读者应该知道机器学习可以大致分为：a) 有监督学习；b) 无监督学习。有监督学习可以进一步分为：a.

1) 分类；2) 回归。无监督学习也可以分为两类：b.

1) 聚类；2) 降维。《数据有道》着重讲解 a.

2) 回归、b.

2) 降维，这两个板块。《机器学习》则强调 a.

1) 分类、1) 聚类。编程《编程不难》《可视之美》数学《矩阵力量》《统计至简》实践《数据有道》《机器学习》丛书板块《数学要素》图1.

鸢尾花书板块布局

Page 10 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 0.

2结构：4大板块《数据有道》可以归纳为4大板块：数据处理、时间数据、回归、降维。数据处理时间数据缺失值离群值数据转换插值数据有道时间数据移动窗口随机过程入门回归非线性回归贝叶斯回归正则化多元线性回归回归分析降维主成分分析正交回归主元回归典型相关分析图2.《数据有道》板块布局数据处理第1章总括介绍常见数据类型、处理、模型。第2章讲解如何处理数据中的缺失值。第3章介绍处理离群值的常用工具，这一章和机器学习算法联系紧密。第4章讲解常用数据转换方法，本章也相当于对统计知识的回顾。第5章特别介绍插值，注意插值和回归的区别。时间数据这个板块介绍一类特殊数据 ——具有时间戳的数据，也叫时间序列。第6章讲解如何处理时间数据、发现数据的趋势、时间序列分解等内容。时间数据的特征随时间动态变化，这是第7章特别强调的一点。第7章中，大家会看到均值、标准差 (波动率 )、相关性系数、回归系数都可以随时间变化。第8章是随机过程入门，介绍布朗运动、几何布朗运动，以及用几何布朗运动完成股价走势的蒙特卡罗模拟。这一章是《统计至简》第15章的延伸。回归这个版块都和回归有关。第9章首先利用一元 OLS线性回归讲解回归分析，本章中大家会学到方差分析、拟合优度

F检验、t检验置信区间、预测区间对数似然函数信息准则等概这一章相对较为无聊，建议大家学习时没有必要全部掌握。实践时再回来有针对性地学习。Page 11 | 正文前 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGing er

bi libili.

com/513194 466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 第10章讲解多元线性回归，回归分析的维度提高。这一章请大家多从几何、数据视角思考回归分析。第11章利用正则化解决多元线性回归过拟合、多重共线性的问题。这一章一共介绍三种正则化：a) 岭回归；b) 套索回归；c) 弹性网络回归。第12章介绍如何将贝叶斯推断用在回归分析中。学习这一章时，建议大家回顾《统计至简》第20 ~ 22章。这一章最后从贝叶斯推断视角理解正则化。第13章讲解非线性回归，需要大家掌握多项式回归，并理解过拟合。此外，这一章还介绍了逻辑回归，逻辑回归既可以用来回归分析，也可以用来分类。降维第14、15章讲解主成分分析。第14章侧重从应用角度讲解，第15章则区分六种不同的技术鸢尾花书在不同的板块都或多或少地介绍过主成分分析，这样安排的目的是当大家从线性代数、概率统计、优化、数据等不同角度透彻理解主成分分析。对读者来说，这种抽丝剥茧、逐层深入的讲解方式，不至于信息过载。第16、17章分别介绍以主成分分析为基础的两种回归方法：正交回归、主元回归。虽然这两章介绍的是回归方法，但是它们都离不开主成分分析。此外，第17章还介绍了偏最小二乘回归。第18章介绍典型相关分析。典型相关分析方法的目的是找到两组数据的整体相关性的最大线性组合。# 0.3特点：应用《数据有道》一册的最大特点就是 “应用”。本书除了使用鸢尾花数据之外，本书还经常使用股票数据。在学习本册时希望大家不要仅仅满足于 “调用”Python库要知其然，更要知其所以然清楚这些函数底层的算法逻辑。《数学要素》、《矩阵力量》、《统计至简》这三册介绍的数学工具对于本册至关重要，特别是线性代数、概率统计等数学工具。因此，不建议大家跳过“数学”

板块三本书，直接学习本册内容。《数据有道》相当于《机器学习》的基础。此外，本册的 “回归”、“降维”这两个板块还会以

“综述”方式出现在《机器学习》一册。此外，在数据科学、机器学习实践中，大家会发现《数据有道》一册的很多工具都可以用在特征工程。《数据有道》和《机器学习》还给大家更多在线开源资源，帮助大家扩展学习。掌握数据分析的技能需要长年累月地和浩如烟海的数据 “摸爬滚打 ”

不可能一蹴而就。大家在学习本册时，能够一边学理论、一边搞实践。下面，我们正式开始本册的学习之旅！Page 1 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 1 All Is Number

万物皆数从数据科学、机器学习视角再看数字但凡满足以下两个条件的理论便可以称之为优质理论基于几个有限的变量准确描述大量观能对对未来观测值做出确定的预测。A theory is a good theory if it satisfies two requirements

it must accurately describe a large class of

observations on the basis of a model that contains only a few arbitrary elements

and it must make

definite predictions about the results of future obser vations.

—— 史蒂芬·霍金 (Stephen Hawking) | 英国理论物理学家宇宙学家 | 1942 ~ 2018

数据表格线性代数视角概率统计视角数据分类定量连续离散有标签，有监督学习代数视角标签有无无标签，无监督学习混合，半监督学习定性万物皆数定类定序机器学习有监督回归分类无监督降维聚类机器学习一般流程特征工程

Page 2 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 1.

1从表格说起四个视角这是一个有关数字的故事，故事的开端便是形如图1所示的表格数据。任何表都可以看成是由行 (row) 和列 (column ) 构成。从线性代数角度来看，图1这个表格本质上是一个矩阵。《矩阵力量》介绍过矩阵的每一行可以看成是一个行向量 (row vector)

每一列为列向量 (column vector)。比如，将图1这个矩阵记做 X

X可以写成一组列向量 X = [x1

x2, …, xD]。X当然也可以写成一组行向量 X = [x(1), x(2), …, x(n)]T。注意，在《机器学习》一册中为了方便 x(1)

x(2), …

x(n) 偶尔也会被视作为列向量体说明。从统计角度来看，表格的每一列可以视作一个随机变量的样本数据。图1则代表 D个随机变量 (X1, X2, …, XD) 的样本数据。X1, X2

…, XD可以构成 D元随机变量列向量 χ = [X1

X2, …, XD]T。从代数角度来看图1表格的每一列相当于变量 (x1

x2, …, xD) 的取值。比如，我们会在回归分析的解析式中看到这种记法 y = b0 + b1x1 + b2x2 + … + bDxD。# Column

Row1 2 D .

nn 1n 2

图1.

表格数据

Page 3 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 定量数据、定性数据数据一般可以分为定量数据 (quantitative data) 和定性数据 (qualitative data)

具体分类如图2所定量数据指的是，可以采用数值表达的数据，比如股票价格、人体高度、气温等等。定性数据，也叫类别数据 (categorical data )

指的是描述事物的特征属性等文字或符号如姓名、颜色、国家、性别、五星评价等等。# DataQuantitative data

Discrete dataContinuous data

Ordinal dataNominal data

Qualitative data

图2.

数据分类连续数据、离散数据定量数据，还可以进一步分为连续数据 (continuous dat a) 和离散数据 (discrete data)。连续数据是指在一定区间内可以任意取值的数据，比如气温、GDP数据等等。离散数据只能采取特定值，比如说个数 (整数)、一到五星好评、骰子点数等等。一天24小时之内的温度数据不可能被持续记录，按一定时间频率需要采样。举个例子，比如，每小时记录一个温度数值。图3所示为某国家 GDP数据，虽然为年度数据，当数据量足够大时，GDP增长曲线看上去是连续曲线；但是，当展开局部数据时，可以发现这条所谓的连续数据实际上是相邻点相连构成的“折线”。1960 1965 1970 1975 1980 1985 1990 1995 2000 2005 2010 2015 2020051015GDP

× 1012

Page 4 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 图3.

采样数据定类数据、定序数据定性数据也可以分为定类数据 (nominal data) 和定序数据 (ordinal data)。简单来说，定类数据没有任何内在顺序或排序，定序数据指具有内在顺序或排序的数据。定类数据，也叫名义数据，用来表征事物类别，比如血型 A、B、AB和O。定序数据，也叫有序数据不仅能够代表事物的类别还可以据此特征排序比如学生成绩

A、B、C、D和F。此外，区间数据 (interval data) 也可以看做时一种定序数据比如身高区间数据，160 cm以下 (包括160 cm)

160 cm到170 cm (包括170 cm)

170 cm到180 cm (包括180 cm)

和180 cm以上。混合很多时候，一个表格常常是各种数据的集合体。如图4所示，表格每一行代表一个学生的某些基本数据。表格第1列为为学生姓名表格第2列为性别 (定类数据 )

表格第3列为身高 (连续定量数据 )，第4列为成绩 (定序数据 )，第5列为血型 (定类数据 )。大家已经很熟悉的鸢尾花数据也是混合数据表格。如图5所示，表格的第一列为序号，之后四列为花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征的连续数据。最后一列为鸢尾花分类

Male

Male

FemaleFemale

Male

FemaleMaryJames

Shawn

Alice

Bill

JuliaGender Height

168Name

A

A+

A+A

B

B+Grade

AB

B

BO

A

ABlood

图4.

学生数据

Page 5 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

IndexSepal length

X1Sepal width

X2Petal length

X3Petal width

X4Species

C

49Setosa

C1

Versicolor

C252

149Virginica

C3

# 1505.1 3.5 1.4 0.2

# 4.9 3 1.4 0.2

# 4.7 3.2 1.3 0.2

# 5.3 3.7 1.5 0.2

5 3.3 1.4 0.2

7 3.2 4.7 1.4

# 6.4 3.2 4.5 1.5

# 6.9 3.1 4.9 1.5

# 5.1 2.5 3 1.1

# 5.7 2.8 4.1 1.3

# 6.3 3.3 6 2.5

# 5.8 2.7 5.1 1.9

# 7.1 3 5.9 2.1

# 6.2 3.4 5.4 2.3

# 5.9 3 5.1 1.8... ... ... ... ...

... ... ... ... ...

... ... ... ... ...

图5.

鸢尾花数据表格，单位为厘米 (cm)

有标签、无标签数据根据输出值有无标签如图6所示数据可以分为有标签数据 (labelled data) 和无标签数据

(unlabelled data)。鸢尾花数据显然是有标签数据。删去鸢尾花最后一列标签，我们便得到无标签有标签数据和无标签数据是机器学习中常见的两种数据类型，它们在不同的应用场景中有不同的用途。简单来说，有标签数据是指已经被人工或其他方式标注了类别或标签的数据。在有标签数据中，每个样本都有对应的标签或分类信息。有标签数据通常用于监督学习 (super vised learning)，即机器学习模型可以利用已知的标签信息进行训练并在后续的预测过程中使用这些信息进行分类或回归。无标签数据是指没有标签或分类信息的数据。在无标签数据中，样本只有特征信息，而没有对应的标签信息。无标签数据通常用于无监督学习 (unsupervised learning)

即机器学习模型需要通过自己的学习过程，从数据中发现并学习出有意义的模式和结构。无监督学习通常包括聚类、降维和异常检测等任务。Page 6 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 在实际应用中，有标签数据和无标签数据往往同时存在。例如，在文本分类任务中，可以有大量已经标注好类别的文本数据 (有标签数据 )

但同时还存在大量未分类的文本数据 (无标签数据)，可以利用这些无标签数据进行半监督学习 (semi -supervised lear ning)。# X y

Input variables

or featuresUnobservedUnsupervised learning

NaN

UnlabeledX y

Input variables

or featuresResponse

variableSupervised learning

LabeledX y

Input variables

or featuresMixedSemi -supervised learning

LabeledNaN

Unlabeled

图6.

根据有无标签分类数据

# 1.2机器学习方法分类人工智能 (Artificial Intelligence

AI) 是一套算法系统它通过模拟人类智慧感知环境，经过分析计算，进而可以执行设定的行为动作。机器学习机器学习是实现人工智能的一大类方法和技术。机器学习算法的特点是，从样本数据中分析并获得某种规律，再利用这个规律对未知数据进行预测。它是涉及概率、统计、矩阵论、代数学、优化方法、数值方法、算法学等多领域的交叉学科。# Machine learning

Unsupervised learningSupervised learning

RegressionClassification

Dimensionality reductionClustering

图7.

机器学习分类

Page 7 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 机器学习适合处理的问题有如下特征：(a) 大数据；(b) 黑箱或复杂系统，难以找到控制方程

(gover ning equations)。机器学习需要通过数据的训练。如图7所示，简单来说，机器学习可以分为以下两大类：◄ 有监督学习也叫监督学习训练练有标签值样本数据并得到模型通过模型对新样本进行

◄ 无监督学习训练没有标签值的数据，并发现样本数据的结构和分布。此外，半监督学习结合无监督学习和监督学习。Clustering ClassificationRegression Dimension reduction(a) (b)

(c) (d)Quantitative CategoricalUnsupervised learning Supervised learning

图8.

根据数据是否有标签标签类型细分机器学习算法图片来自《矩阵力量》第25章有监督学习如图8所示有监督学习可以进一步分为分类 (classification )

回归 (regression)。分类问题是指将数据集划分为不同的类别或标签。给定一个输入，分类模型的目标是预测它所属的类别，如垃圾邮件分类、图像识别和情感分析等。分类问题的输出是一个离散值或类别标

Page 8 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 回归问题是指根据已知的输入和输出数据，建立一个数学模型来预测输出值。给定一个输入，回归模型的目标是预测它的输出值，如房价预测、股票价格预测和天气预测等。回归问题的输出是一个连续的值或数值。总的来说，分类问题与离散的输出相关，目标是将数据划分为不同的类别或标签，而回归问题与连续的输出相关，目标是预测数值型数据的结果。本书将介绍如下几种回归算法：◄ 线性回归 (linear regression)，本书第10、11章；◄ 贝叶斯回归 (Bayesian regression)，本书第12章；◄ 岭回归 (ridge regression)，本书第13章；◄ 套索回归 (LASSO regression)，本书第13章；◄ 弹性网络回归 (elastic net regression)

本书第13章；◄ 多项式回归 (Polynomial regression)

本书第14章；◄ 逻辑回归 (logistic regression)，本书第15章；◄ 正交回归 (orthogonal regression )，本书第18章；◄ 主元回归 (principal componen t regression )

本书第19章；◄ 偏最小二乘回归 (partial least squ ares regression )

本书第19章。《机器学习》一册将将专门介绍分类算法。注意，很多分类算法也可以用来完成回归分析这也是《机器学习》一册要介绍的内容。无监督学习如图8所示无监督学习主要分为绍聚类 (clustering)

降维 (dimensionality reduction)。降维是指将高维数据映射到低维空间的过程，以便更好地理解和分析数据。通常情况下，高维数据在进行可视化、建模和处理时都会面临计算资源、时间复杂度和维数灾难等问题。维可以减少数据维度，压缩数据，去除冗余信息，提高模型效率和准确度。聚类是指将数据集中相似的数据分为一类的过程，以便更好地分析和理解数据。聚类分析是一种无监督学习方法它不需要标记的训练数据而是根据数据点之间的相似性或距离关系将它们分为不同的簇或群组。聚类可以用于数据挖掘、图像处理、文本分类、市场细分和生物信息学等领域。常见的聚类算法包括 K均值聚类、层次聚类和 DBSCAN 等。总的来说，降维是指将高维数据映射到低维空间的过程，目的是减少数据维度、压缩数据、去除冗余信息，而聚类是指将相似的数据分为一类的过程，目的是更好地分析和理解数据。本书将主要介绍如下降维算法：Page 9 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com ◄ 主成分分析 (princi pal component analysis )

本书第15

16章；◄ 因子分析 (Factor Analysis)，本书第19章；◄ 典型相关分析 (canonical correlati on analysis )

本书第20章。《机器学习》一册将将专门介绍聚类算法。# 1.3机器学习流程图9所示为机器学习的一般流程。具体分步流程通常包括以下步骤：◄ 收集数据从数据源获取数据集这可能包括数据清理去除无效数据和处理缺失值等。◄ 特征工程：对数据进行预处理，包括数据转换、特征选择、特征提取和特征缩放等。◄ 数据划分：将数据集划分为训练集、验证集和测试集等。训练集用于训练模型，验证集用于选择模型并进行调参，测试集用于评估模型的性能。◄ 选择模型：选择合适的模型，例如线性回归、决策树、神经网络等。◄ 训练模型使用训练集对模型进行训练并对模型进行评估可以使用交叉验证等方法进行模型选择和调优。◄ 测试模型：使用测试集评估模型的性能，并进行模型的调整和改进。◄ 应用模型：将模型应用到新数据中进行预测或分类等任务。◄ 模型监控：监控模型在实际应用中的性能，并进行调整和改进。以上是机器学习的一般分步流程，不同的任务和应用场景可能会有一些变化和调整。应用中，还需要考虑数据的质量、模型的可解释性、模型的复杂度和可扩展性等问题。Page 10 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Input dataBlack boxReal world

Original data

Processed data

Training setCollect data

Process data

Validation set

Machine

learningLearning

Evaluation

Trained modelYes

deployValidateFeature extraction

Feature selection

MonitorPredictTest setModel selection

Pass?

NoEvaluateTune parametersFeature engineering

图9.

机器学习一般流程

1.4特征工程从原始数据中最大化提取可用信息的过程就叫做特征工程 (feature engineering)。特征很好理解，比如鸢尾花花萼长度宽度、花瓣长度宽度，人的性别、身体、体重等，都是特征。特征工程是机器学习中非常重要的一个环节指的是对原始数据进行特征提取特征转换、特征选择和特征创造等一系列操作，以便更好地利用数据进行建模和预测。具体来说，特征工程包括以下方法：◄ 特征提取 (Feature Extraction )

将原始数据转换为可用于机器学习算法的特征向量。注意，这个特征向量不是特征值分解中的特征向量。Page 11 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com ◄ 特征转换 (Feature Transformation )

对原始特征进行数值变换使其更符合算法的假设。如，在回归问题中，可以对数据进行对数转换或指数转换等。◄ 特征选择 (Feature Selection )

选择最具有代表性和影响力的特征。例如，可以使用相关性分析、PCA等方法选择最相关或最重要的特征。◄ 特征创造 (Featur e Creation )

根据原始特征创造新的特征。例如，在房价预测问题中，可以根据房屋面积和房龄创建新的特征。◄ 特征缩放 (Feature Scaling )

将特征缩放到相同的尺度或范围内避免某些特征对模型训练的影响过大。例如，在神经网络中，可以使用标准化或归一化等方法对数据进行缩放。特征工程在机器学习中扮演着至关重要的角色，它可以提高模型的精度、泛化能力和效率。在实际应用中需要根据具体问题选择合适的特征工程方法并不断尝试和改进以达到最佳效相信大家都听过“ 垃圾进垃圾出 (garbage in

garbage out

GIGO) ”。这句话的含义很简单，将错误的、无意义的数据输入计算机系统，计算机自然也一定会输出错误、无意义的结果。科学、机器学习领域，很多时候数据扮演核心角色。以至于在数据分析建模时，大部分的精力都花在了处理数据上。特征工程很好的混合了专业知识、数学能力。虽然丛书不会专门讲解特征工程，但是本书的很多内容都可以用于特征工程。本书第一个板块 “数据处理 ”中介绍的缺失值离散值处理可以视作特征预处理。而缺失值、离散值也经常使用各种机器学习算法。本书中的数据转换插值、正则化主成分分析、因子分析典型性分析也都是特征工程的此外，《统计至简》一册中的统计描述统计推断，《机器学习》一册的独立成分分析

(independent component analysis

ICA)、线性判别分析 (linear discriminant analysis

LDA)、聚类算法等也都可以用于特征工程。本章首先简要介绍了观察数据的不同视角 (表格、线性代数、概率统计、代数 )。然后，讲解了数据分类。大家特别需要注意根据数据有无标签可以把机器学习分成两个大类 ——有监督学习而有监督学习又可以细分为回归、分类。无监督学习则进一步分为降维、聚类。《数据有道》主要讲解回归、降维，《机器学习》则介绍分类、聚类。本章最后又聊了聊机器学习的一般流程，以及特征工程。本书几乎所有内容都可以服务特征

Page 12 | Chapter 1万物皆数 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

有关特征工程，大家可以参考这本开源专著：feat.

engineering/

Scikit-learn也有大量特征工程工具，请大家参考：org/stable/module s/feature_selection.

html

Page 1 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 2 Dealing with Missing Data

缺失值用代数、统计、机器学习算法补齐缺失值若上天再给一次机会，让我重新开始学业，我定会听从柏拉图，先学数学。# If I were again beginning my studies

I would follow the advice of Plato and start with mathematics.

—— 伽利略·伽利莱 (Galilei Galileo ) | 意大利物理学家数学家及哲学家 | 1564 ~ 1642

◄ df.

dropna(axis = 0

how = 'any') 中 axis = 0为按行删除设置 axis = 1表示按列删除。= 'any' 时，表示某行或列只要有一个缺失值，就删除该行或列；当 how = 'all'，表示该行或列全部都为缺失值时，才删除该行或列

◄ df.

isna 判断Pandas 数据帧是否为缺失值是便用 True占位否便用 False占位

◄ df.

notna 判断Pandas 数据帧是否为非缺失值是缺失值使用 False占位不是缺失值采用 True占位

◄ missingno.

matrix 绘制缺失值热图

◄ numpy.

NaN 产生NaN占位符

◄ numpy.

random.

uniform 产生满足连续均匀分布的随机数

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

pairplot 绘制成对特征分析图

◄ sklearn.

impute.

KNNImputer 使用k近邻插补

◄ sklearn.

impute.

MissingIndicator 将数据转换为相应的二进制矩阵 (True和False)

以指示数据中缺失值的存在位置

◄ sklearn.

impu te.

SimpleImputer 使用缺失值所在的行 /列中的统计数据平均值 ('mean')

('median') 或者众数 ('most_frequent') 来填充也可以使用指定的常数 'constant'

Page 2 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

产生原因采集过程处理过程储存过程填补方法可视化缺失值缺失值删除插值模型多重插补

Page 3 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 2.

1缺失值小传在数据分析中，缺失值是指数据集中某些观测值或属性值没有被记录或采集到的情况。各种原因，数据中缺失值不可避免。缺失值通常被编码为空白，NaN或其他占位符。处理缺失值是数据预处理中重要一环。图1.

数据中缺失值产生的原因有很多。比如，在数据采集阶段，设备故障、人为失误、方法局限、拒绝参与调查、信息不完整等等可以造成数据缺失。另外，数据数据存储阶段也可能引入缺比如，数据存储失败、存储器故障等等。填补缺失值的方法有很多种，包括：► 删除缺失值直接删除缺失值所在的行或列但这可能会导致数据的丢失和分析结果的偏

► 插值法：通过插值方法填补缺失值如均值插值、中位数插值最近邻插值、多项式插值

► 模型法：使用回归决策树或神经网络等模型预测缺失值但需要先对数据进行训练和测试，可能会导致模型的过拟合和不准确。► 多重填补法：使用多个模型进行填补，可以提高填补缺失值的准确性和可靠性。本章后文将专门介绍常见填补缺失值的方法。NaN：非数

Page 4 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com NaN常用于表示缺失值。NaN是not a nu mber的缩写，中文含义是 “非数”。numpy.

nan 可以用来产生 NaN。举个例子，如果想要在已知数据帧 df中，增加用NaN做占位符一列，就可以用

df['holder '] = n p.

nan，其中 'holder '为这一列的标题 (header)。一些 Numpy函数在统计计算时，遇到缺失值会报错。表1第二列 Num py函数遇到缺失值

NaN，会直接报错。而表1第三列函数，计算时忽略 NaN。表1.

比较 Numpy函数处理缺失值差异遇到 NaN，报错计算时，忽略NaN

均值 numpy.

mean numpy.

nanmean

中位数 numpy.

median nump y.

nanmedian

最大值 numpy.

max numpy.

nanmax

最小值 numpy.

min numpy.

nanmin

方差 numpy.

var numpy.

nanvar

标准差 numpy.

std numpy.

nans td

分位 numpy.

quantile numpy.

nanquantile

百分位 numpy.

percentile numpy.

nanpercentile

原始数据中缺失值的样式没有特定标准利用 pandas读取数据时可以设置缺失值样式。如read_csv 读取 CSV文件时可以利用 na_values 设置缺失值样式比如 na_values = 'Null'

如 na_values = '?

' 等等。在Pandas数据帧中，也用 NaT表达缺失值。以鸢尾花数据为例本章以鸢尾花数据讲解如何处理缺失值。图2所示为完整的鸢尾花数据成对特征分析图，其中有150个数据点。Page 5 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

图2.

鸢尾花原始数据，成对特征分析图在鸢尾花原始数据中完全随机引入缺失值 NaN

将数据存为 iris_df_NaN

数据的形式如图3

图4所示为含有缺失值得鸢尾花可视化图像。sepal length (cm) sepal width (cm) petal length (cm) petal width (cm)

0 5.1 NaN NaN 0.2

1 NaN NaN 1.4 0.2

2 4.7 3.2 1.3 0.2

3 NaN NaN NaN NaN

4 NaN NaN 1.4 NaN

.. ... ... ... ...

145 6.7 NaN 5.2 2.3

146 6.3 2.5 5.0 NaN

147 6.5 3.0 5.2 NaN

148 6.2 NaN NaN 2.3

149 5.9 3.0 NaN 1.8

图3.

鸢尾花样本数据，随机引入缺失值

Page 6 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

图4.

鸢尾花数据可视化，引入缺失值

2.2可视化缺失值位置为了准确获取缺失值位置数量等信息，对于 Pandas数据帧数据可以采用 isna 或 notna 方查找缺失值采用 iris_df_NaN.

isna，返回具体位置数据是否为缺失值。数据缺失的话，为True；为False。图5所示为 iris_df_NaN.

isna 结果。Page 7 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

sepal length (cm) sepal width (cm) .

petal width (cm) species

0 False True ... False False

1 True True ... False False

2 False False ... False False

3 True True ... True False

4 True True ... True False

.. ... ... ... ... ...

145 False True ... False False

146 False False ... True False

147 False False ... True False

148 False True ... False False

149 False False ... False False

图5.

判断数据是否为缺失值图6所示为采用 seaborn.

heatmap 可视化数据缺失值，热图的每一条黑色条带代表一个缺失使用缺失值热图可以粗略观察得到缺失值分布情况。Sepal length Sepal width Petal length Petal width Species150 data points

图6.

缺失值可视化，每条黑带代表缺失值查找非缺失值方法 notna 正好和 isna 相反，iris_df_NaN.

notna 判断数据是否为 “非缺失值 ”；如果数据没有缺失，则为 True。图7所示为iris_df_NaN.

notna 结果。Page 8 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

sepal length (cm) sepal width (cm) .

petal width (cm) species

0 True False ... True True

1 False False ... True True

2 True True ... True True

3 False False ... False True

4 False False ... False True

.. ... ... ... ... ...

145 True False ... True True

146 True True ... False True

147 True True ... False True

148 True False ... True True

149 True True ... True True

图7.

判断数据是否为 “非缺失值”

Sepal length Sepal width Petal length Petal width Species150 data points

图8.

缺失值可视化，每条白带代表缺失值非缺失值变化线图另外，可以安装 missingno，并调用 missingno.

matrix 绘制缺失值热图，具体如图9所示。幅图最右侧还展示每行非缺失值数据数量的变化线图线图最小取值为1

最大取值为5。1时，每行只有一个非缺失值；取值为5时，该行不存在缺失值。观察这幅线图，可以帮助我们解读缺失值分布特征。Page 9 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

图9.

missingno.

matrix 绘制缺失值热图，每条白带代表缺失值总结缺失值信息对于 pandas数据帧也可以采用 info 显示数据非缺失值数量和数据类型。图10所示为

iris_df_NaN.

info 结果。isnull .

sum * 100 / len(df) 则计算每列缺失值的百分比。<class 'pandas.

core.

frame.

DataFrame'>

RangeIndex: 150 entries, 0 to 149

Data columns (total 5 columns):

Column Non -Null Count Dtype

--- ------ -------------- -----

0 sepal length (cm) 85 non-null float64

1 sepal width (cm) 94 non-null float64

2 petal length (cm) 91 non-null float64

3 petal width (cm) 84 non-null float64

4 species 150 non -null int32

dtypes: float64(4), int32(1)

memory usage: 5.

4 KB

图10.

info 总结样本数据特征也可以采用 sklearn.

impute.

MissingIndicator 函数将数据转换为相应的二进制矩阵 (True和

False，相当于1和0)，以指示数据中缺失值的存在位置。Page 10 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 2.

3处理缺失值图11总结常用处理缺失值的方法。对于表格数据，一般情况，每一行代表一个样本数据，每一列代表一个特征。处理存在缺失值数据集的基本策略是舍弃包含缺失值的整行或整列。但是，这是以丢失可能有价值的数据为代更好的策略是估算缺失值，即从数据的已知部分推断出缺失值，这种方法统称插补

(imputat ion)。本章后续主要介绍连续数据的删除和插补方法。本书第6章将专门介绍时间序列数据的插补。# DeletionDeleting rows

Deleting columns

Pairwise deletion

ImputationGeneralCategorical Logistic regression

Make NaN as new cl ass

Multiple imputation

ContinuousMean, mode, or median

Multiple imputation

Regression

TimeseriesHandle missing data

图11.

处理缺失值的方法分类

# 2.4删除：最基本方法本节简单介绍 Pandas数据帧 dropna 方法。对于某一个数据帧 df，df.

dropna(axis = 0

how = 'any' ) 中 axis = 0为按行删除设置 axis = 1表示按列删除。how = 'any' 时表示某行或列只要有一个缺失值就删除该行或列如图12所示。如图13所示当how = 'all'

表示该行或列全部都为缺失值时才删除该行或列。dropna 方法默认设置为 axis = 0，how = 'any'。Page 11 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

dropna(axis=0, how='any' )

图12.

Pandas数据帧中删除含有至少一个缺失值所在的行

dropna(axis=0, how=' all')

图13.

Pandas数据帧中删除全为缺失值行图14所示为删除缺失值后的鸢尾花数据规则为删除含有至少一个缺失值所在的行。4，可以发现非缺失数据点明显减小。图14中所剩数据便是图9中最右侧线图值为5对应的数据

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

Page 12 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 图14.

鸢尾花数据，删除含有至少一个缺失值所在的行一般情况每列数据代表一个特征，删除整列特征的情况也并不罕见。不管是删除缺失值所在的行或列，都会浪费大量有价值的信息。成对删除成对删除 (pairwise deletion) 是一种特别的删除方式进行多特征联立时成对删除只删除掉需要执行运算特征包含的缺失数据；以估算方差协方差矩阵为例，如图15所示，计算 X1和X3的相关性，只需要删除 X1和X3中缺失值对应的数据点。# X1X2X3X4 X1X3

Pairwise deletion

图15.

成对删除

# 2.5单变量插补相对删除缺失值，更常用的方法是，采用一定的方法补全缺失值，我们称之为插补

(imputation)。如图11所示，分类数据和连续数据采用的方法也稍有差别。注意，选取采用插补方法要格外小心如果填充方法不合理会引入数据噪音并造成数据分析结果不准确。时间数据采用的插补方法不同于一般数据。Pandas数据帧有基本插补功能，特别是对于时间数据，可以采用插值 (interpolation)、向前填充、向填充。这部分内容，我们将在本书插值和时间序列部分详细介绍。单变量插补：统计插补本节专门介绍，单变量插补。单变量插补也称统计插补，仅使用第 j个特征维度中的非缺失值插补该特征维度中的缺失值。本节采用的函数是sklearn.

impute.

SimpleImputer。SimpleImputer 可以使用缺失值所在的行 /列中的统计数据平均值 ('mean ')

中位数 ('media n')

或者众数 ('most _frequ ent') 来填充也可以使用指定的常数 'constant'。如果某个特征是是连续数据可以根据在其他所有非缺失值平均值或中位数来填充该缺失

Page 13 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 如果某个特征是是分类数据则可以利用该特征非缺失值的众数即出现频率最高的数值来补齐缺失值。图16所示为采用中位数插补鸢尾花缺失值。观察图16，可以发现插补得到的数据形成“十字”图

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

图16.

鸢尾花数据，采用中位数插补缺失值

# 2.6 k近邻插补本节介绍 k近邻插补。k近邻算法 (k-nearest neighbors algorithm

k-NN) 是最基本有监督学习方法之一，k-NN中的 k指的是“近邻”的数量。k-NN思路很简单——“近朱者赤，近墨者黑 ”。地说，小范围投票，少数服从多数 (major ity rule )。《机器学习》第2章专门介绍 k近邻算法这种监督学习方法。本节介绍 k近邻插补的函数为 sklearn.

impute.

KNNImputer。利用 KNNImputer 插补缺失值时，先给定距离缺失值数据最近的 k个样本将这 k个值等权重平均或加权平均来插补缺失值。图17所示为采用 k近邻插补鸢尾花数据结果。Page 14 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

图17.

鸢尾花数据，最近邻插补

2.7多变量插补多变量插补，利用其它特征数据来填充某个特征内的缺失值。具体来说，多变量插补将缺失值所在变量视为预测目标变量使用其他已知变量作为预测变量通过建立回归或分类模型来预测缺失值，并进行填补。相比于单变量插补方法，多变量插补能够更充分地利用数据集中的信息，从而提高填补结果的准确性和可靠性。多变量插补的常见方法包括线性回归、随机森林、神经网络等。多变量插补通常将缺失值建模为其他特征的函数用该函数估算合理的数值以填充缺失整个过程可以用迭代循环方式进行。比较来看，单变量插一般仅考虑单一特征进行插补，而多变量插补考虑不同特征数据的联系。图18所示为采用 sklearn.

impu te.

IterativeImputer 函数完成多变量插补，补齐鸢尾花数据中缺

Page 15 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)

Sepal length (cm) Sepal width (cm) Petal length (cm) Petal width (cm)Species 0

Setosa 1

Versicolor 2

Virginica

图18.

鸢尾花数据，多变量插补

Bk6_Ch02_01.

py 绘制本章大部分图像。缺失值是指数据集中某些观测值或属性值没有被记录或采集到的情况。缺失值可能会影响数据分析结果的准确性和偏差，产生原因包括数据采集问题、处理问题、参与者拒绝回答等。方法包括删除缺失值、插值法、模型法和多重填补法。注意要根据具体情况选择最合适的处理方法，以确保数据分析的准确性和可靠性。有关数据帧处理缺失值，请大家参考：pydata.

org/pandas -docs/s table/user_guide/missing_data.

html

Page 16 | Chapter 2缺失值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com sklearn .

impute.

IterativeImpu ter 函数非常灵活可以和各种估算器联合使用比如决策树回归、贝叶斯岭回归等等。感兴趣的读者可以参考：org/stable/modules/impute.

html

Page 1 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 3 Detecting Outliers

离群值利用统计方法和机器学习算法发现、处理离群值数学领域，提出问题比解决问题，更珍贵。In mathematics the art of proposing a question must be held of higher value than solving it.

—— 格奥尔格·康托尔 (Georg Cantor ) | 德国数学家 | 1845 ~ 1918

◄ numpy.

percentile 计算百分位

◄ pandas.

D ataFrame 构造pandas 数据帧

◄ seaborn.

boxplot 绘制箱型图

◄ seaborn.

histplot 绘制直方图

◄ seaborn.

kdeplot 绘制概率密度估计曲线

◄ seaborn.

pairplot 绘制成对分析图

◄ seaborn.

rugplot 绘制rug图像

◄ seaborn.

scatterplot 绘制散点图

◄ sklearn.

covariance.

EllipticEnvelope 协方差椭圆法检测离群值

◄ sklearn.

ensemble.

Isolati onForest 孤立森林检测离群值

◄ sklearn.

s vm.

OneClassSVM 支持向量机检测离群值

◄ stats.

probplot 绘制QQ图

Page 2 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 3.

1离群值小传离群值 (outlier)

又称逸出值、离群值是指数据集中与其他数据点有显著差异的数据点就是说明显地偏大或偏小。离群值可能是由于异常情况、错误测量、数据录入错误或意外事件等原因而产生。离群值可能会对数据分析和建模造成问题，因为它们可能导致误差或偏差，并降低模型的准确性。因此，数据分析师通常会对数据集中的离群值进行检测和处理。常见的离群值检测方法包括基于统计学的方法、基于距离的方法、基于密度的方法和基于模型的方法。处理离群值的方法包括删除、替换、调整或利用异常值建立新的模型等。图1.

离群值破坏力离群值可以具有很强的破坏力。比如，离群值可能给最大值、最小值、极差、平均值、方差、标准差、线性相关性系数、分位等统计量计算带来偏差。图2所示为离群值对线性回归 (linear regression) 的影响。再举个例子，实践中，大家会发现离群值对于时间序列相关性系数计算破坏力更大。这一章专门介绍各种发现离群值的工具。Page 3 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

图2.

离群点对回归分析的影响工具如图3所示，判断离群值的方法有很多。本章将围绕图3中主要方法展开。这幅图也相当于是本章的思维导图。最简单的方法是观察样本数据的最大值和最小值根据生活常识或专业知识判断围是否合理。比如，鸢尾花数据集中，如果出现某个样本点的花萼长度为5.

2米，这显然是个离再举例，鸢尾花任何特征数值肯定不能是负数。确定离群值之后，需要合理处理。常见的办法有，比如通过设为 NaN将其删除，或者填充。填充的方法很多，可以参考上一章内容。# Statistics -basedNonparametricHistogram

rug plot

Boxplot

Kernel -based

Scatter plot

ParametricGaussian -based Univariate

Multivariate

Regression -based

Distance -based

Density -based

Clustering -based

Timeseries analysisHandle outliersQQ plot

图3.

处理离群点的常见方法

Page 4 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

3.2直方图：单一特征分布鸢尾花书《统计至简》第2章专门介绍过直方图 (histogram )。可以通过观察数据的直方图来初步判断单一特征的分布情况以及可能存在的离群值。百分位图4所示鸢尾花四个特征数据的直方图。将数据顺序排列，离群值肯定出现分布的两端。如，在图4上，绘制1%和99%百分位所在位置。可以1%和99%百分位用来界定数据分布的 “左尾”和“右尾”。回顾一下，百分位 (percentile) 是指一个数值在一组数据中的排名位置表示该数值小于等于百分位数的观测值所占的百分比。例如，50%百分位数是中位数，表示一半的数据小于等于中位数，另一半的数据大于等于中位数。另外，25%

50%和75%这三个百分位也同样重要图5给出了鸢尾花四个特征的这三个百分位所在位置。下一节讲解箱型图时，将使用25%、50%和75%这三个百分位。Sepal length, X10 2 4 6 8

Sepal width, X20 2 4 6 8

Petal length, X30 2 4 6 8

Petal width, X40 2 4 6 8Count Count

Count Count1% percentile50% percentile99% percentile 1% percentile

99% percentile

1% percentile

99% percentile1% percentile

99% percentile

图4.

鸢尾花数据直方图，以及1%和99%百分位

Page 5 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length, X10 2 4 6 8

Sepal width, X20 2 4 6 8

Petal length, X30 2 4 6 8

Petal width

X40 2 4 6 825% percentile50% percentile75% percentile

25% percentile

75% percentile

25% percentile

75% percentile25% percentile

75% percentileCount

CountCount

Count

图5.

鸢尾花数据直方图，以及25%、50%和75%百分位山脊图图6所示为采用 joypy绘制的山脊图也可以用来发现分类数据中潜在离群值。《可视之美》曾专门介绍过山脊图。# 0.00 0.05 0.10 0.15 0.05 0.10 0.15

图6.

标普500日收益率数据

Page 6 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 概率密度估计 + rug图概率密度估计图像也可以用来观察异常值。概率密度估计 (Probability Density Estimation ) 是指根据有限样本数据推断出未知概率密度函数的过程常用于探索性数据分析和模型构建中。过估计概率密度函数，可以更好地理解数据的分布特征、模型参数和模型拟合度。高斯核密度估计 (Gaussian Kernel Density Estimation )

或高斯 KDE

是一种常用的概率密度估计方法，基于高斯核函数对数据进行平滑处理，估计未知的概率密度函数。该方法对连续变量的数据有较好的适用性，可以用于探索数据分布、识别离群值和构建概率模型等任务。图7所示为高斯 KDE图像，叠加 rug图。图上同样标出1%和99%百分位点位置。rug图是一种数据可视化方法，用于展示数据分布和密度。它将每个数据点在 x轴上表示为一条短线，形成了数据点的密度分布图。rug图通常与直方图或核密度图结合使用，可以更直观地显示数据集的分布情况。《统计至简》专门讲解概率密度估计，请大家回顾高斯核密度估计。Sepal length, X1 Sepal width, X2

Petal length, X3 Petal width, X4Density

DensityDensity

Density1% percentile

99% percentile1% percentile

99% percentile

1% percentile

99% percentile1% percentile

99% percentile

图7.

KDE密度估计，叠加 rug图缩尾调整缩尾调整 (winsorize) 是将超出变量特定百分位范围的数值替换为其特定百分位数值的方法。缩尾调整通过截断分布的长尾部分来减少异常值对估计结果的影响。在实际应用中，我们可以根据领域知识或经验选择合适的截断点，并将超出截断点的异常值设置为固定的截断值。缩尾调整

Page 7 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 可以改善分布拟合和参数估计的稳定性和精度，但也可能引入信息损失和偏差。在选择截断点时需要谨慎，并在分析前后进行敏感性分析。请参考如下链接学习如何使用 scipy.

stats.

mstats.

wins orize 函数进行缩尾调整：s cipy.

org/doc/scipy/reference/generated /scipy.

stats.

mstats.

winsorize.

html

3.3散点图：成对特征分布本章前文所讲的可视化方案均用来发现单一特征可能存在的离群值。采用散点图，发现成对特征数据可能存在的离散点。鸢尾花书读者对散点图肯定很熟悉。散点图 (scatter plot) 是一种常用的数据可视化方法，用于展示两个变量之间的关系。散点图将每个数据点表示为一个点，在二维坐标系上绘制，其中一个变量在横轴上表示，另一个变量在纵轴上表示。散点图可以帮助我们直观地观察变量之间的相关性、趋势和异常值，是探索性数据分析和建模中不可或缺的工具。散点图还可以用于比较不同组之间的变化和趋势，或者用不同的颜色或形状表示不同的组或类别。图8所示为鸢尾花数据花萼长度、花萼宽度散点图。图8中还绘制了单一特征的 rug图。此外，也可以使用如图9成对特征数据来观察数据分布，以及可能存在的离群值。Sepal length, X1Sepal width, X2

图8.

散点图，横轴花萼长度，纵轴花萼宽度

Page 8 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal length

x1Sepal width

x2 Petal length

x3 Petal width

x4Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

图9.

鸢尾花数据成对特征分析图

3.4 QQ图：分位数 -分位数《统计至简》第9章专门介绍过 QQ图。QQ图 (Quantile -Quantile plot ) 是一种用于检查数据是否符合某种理论分布的数据可视化方

QQ图将样本数据的分位数与理论分布的分位数进行比较，并将它们绘制在同一坐标系中。如果数据符合理论分布，则点将沿着一条直线分布。如果数据偏离理论分布，则点将偏离直线。通过观察点的分布情况我们可以判断数据是否符合某种理论分布或者是否存在偏差或离群值等问题。QQ图常用于正态性检验、分布拟合和模型诊断等任务。QQ图的横坐标通常是理论分布的分位数，纵坐标通常是样本数据的分位数。在正态 QQ图中，横坐标通常是标准正态分布的分位数，或 Z分数；纵坐标是样本数据的分位数。在其他类型的QQ图中，横坐标和纵坐标的标尺将取决于所使用的理论分布和样本数据的类型。图10所示为 QQ图原理，图中横轴为正态分布的分位数。Page 9 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

02468

2 1 0 1 2Theoretical (standard

normal) quantilesEmpirical

quantiles

A

y(i)

x(i)

CDF1.

00q(i) = ecdf( y(i))

q(i)

00CDF1.

q(i)

x(i) = ppf( q(i), µ = 0, σ = 1)

图10.

QQ图原理，横轴为正态分布，图片来自《统计至简》第9章图11到图14分别给出鸢尾花四个特征数据的直方图和 QQ图。容易发现不同的数据分布，对应特定的 QQ图分布特点。《统计至简》第9章介绍过如何通过 QQ图形态判断原始数据分布特点请大家自行回顾，本节不再重复。Page 10 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Normal distributionEmperical distribution

Sepal length, X1Count

图11.

花萼长度直方图和 QQ图

Count

Sepal width

X2Normal distributionEmperical distribution

图12.

花萼宽度直方图和 QQ图

Count

Petal length

X3 Normal distributionEmperical distribution

图13.

花瓣长度直方图和 QQ图

Page 11 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Count

Petal width

X4 Normal distributionEmperical distribution

图14.

花瓣宽度直方图和 QQ图

3.5箱型图：上界、下界之外样本《统计至简》第2章专门介绍箱型图。箱型图 (box plot) 是一种展示数据分布和离群值的方法。箱型图通过绘制数据的四分位数

(Q1、Q2、Q3) 和可能的离群值来呈现数据的位置和离散程度。箱型图常用于探索性数据分析和统计推断，可用于比较不同组之间的数据分布和趋势。图15所示为箱型图原理。Q1也叫下四分位，Q2也叫中位数，Q3也称上四分位。Q1 1.

5 × IQR Q3 + 1.

5 × IQR

Q1

25 percentileQ3

75 percentileInterquartile range ( IQR)

Q2, median

50 percentileOutliers Outliers

图15.

箱型图原理箱型图的四分位间距 (interquartile range) 的定义为：31 IQR Q Q=− (1)

在 [Q1 – 1.

5 × IQR, Q3 + 1.

5 × IQR] 之外的样本数据则可能是离群点。图16所示为鸢尾花数据的箱型图。Q3 + 1.

5 × IQR也称上界，Q1 – 1.

5 × IQR叫下界。Page 12 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

0 2 4 6 8Sepal length, X1

Sepal width, X2

Petal length, X3

Petal width, X4

图16.

鸢尾花箱型图

# 3.6 Z分数：样本数据标准化从大到小排列一组 n个样本数据，离群值肯定出现在序列的两端。首先计算出数据的样本均值

x，和样本标准差 s。若任何数据点与均值的偏差绝对值大于三倍标准差，则可以判定数据点为离群点，即满足下式的 x可能是离群值：3 x x s− (2)

大家需要注意极大的离群值会“污染”样本均值。因此，实践中，也常用样本中位数作为基三倍标准差 ±3s相当于99.

7%置信度，对应显著性水平α = 0.

0 03。此外，也可以采用两倍标准差 ±2s，这相当于95%置信度，即 α = 0.

图17展示了《统计至简》第9章介绍的68–95–99.

7法则，请大家回顾。注意，图17中并不区分总体标准差 σ和样本标准差 s，并假设均值为0。Page 13 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

13%~0.

68 (68%)~0.

95 (95%)

6745σ 0.

6745σ Quartiles25% 25% 25% 25%

10%

5%10%

5%10-quantiles

20-quantiles

90% -1.

645σ 1.

645σ

Percentiles1%

98%~0.

997 (99.

1%

33σ 2.

33σ±2σ

±3σ

图17.

标准差，注意图中并不区分总体标准差 σ和样本标准差 s

Z分数

Z分数 (Z score) 是一种用于标准化数据的方法。Z分数表示一个数据点距离均值的标准差数目，通常用于将不同尺度和分布的数据标准化为标准正态分布。Z分数可以帮助我们比较不同数据点之间的相对位置和大小，判断数据是否偏离均值，并进行异常值检测和离群值分析。应用中，Z分数也经常用于构建模型、计算概率和决策阈值等任务。从Z分数角度，(2) 相当于：3xxzs−= (3)

也就是任何数据点的 Z分数绝对值大于3

即 z分数大于3或小于−3

可以判定数据点为离图18所示为鸢尾花数据四个特征的 Z分数。《统计至简》第9章还介绍过 Z分数。Page 14 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Z-score, Z1 4 2 0 2 4

Z-score, Z2 4 2 0 2 4

Z-score, Z3 4 2 0 2 4

Z-score, Z4 4 2 0 2 4Count

CountCount

Count±3, 99.

±2, 95.

45%±3, 99.

±2, 95.

±3, 99.

±2, 95.

45%±3, 99.

±2, 95.

图18.

鸢尾花 Z分数

3.7马氏距离和其他方法对于二维乃至多维的情况，我们也可以使用 Z分数。这个 Z分数就是马氏距离 (Mahalanobis

distance)。马氏距离是一种考虑不同特征之间相关性的距离度量方法。马氏距离可以通过将样本点与数据集的均值向量进行比较，并考虑数据集的协方差矩阵来计算。与欧几里得距离不同，马氏距离可以捕捉不同特征之间的相关性和尺度差异因此更适用于高维数据或特征相关的数据分析任务。马氏距离常用于聚类、分类、异常检测和模式识别等任务。马氏距离定义如下：T 1,d−= − − x q x q Σ x q (4)

其中，查询点 q一般为数据质心，Σ为样本数矩阵 X方差协方差矩阵。如果样本数据分布近似服从多元高斯分布马氏距离则可以作为判定离群值的有效手段。19 (a) 所示为，不同的马氏距离等高线对应不同的置信区间。图19 (b) 而所示为 ±σ ~ ±4σ置信区

Page 15 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

99%98%97%96%95%

图19.

协方差椭圆：(a) 95% ~ 99% 置信区间；(b) ±σ ~ ±4σ置信区间

Scikit-learn提供一个 covariance.

EllipticEnvelope 对象，它就是利用马氏距离椭圆来判断离群图20所示为鸢尾花花萼长度花萼宽度的散点图和马氏距离为2的旋转椭圆。这个旋转椭圆之外的样本点可能是离群值。有关马氏距离、卡方分布、置信区间关系，请大家参考《统计至简》第23章。Sepal length, X1Sepal width, X2

图20.

鸢尾花数据前两个特征构造的协方差椭圆，马氏距离为2

Page 16 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 代码 Bk6_Ch03_01.

py 绘制本章前文主要图片。概率密度估计检测离群值马氏距离实际上假设数据服从多元正态分布。当多特征数据分布情况较大偏离多元正态分布，马氏距离就会失效。这时我们可以用概率密度估计来检测离群值。如图21所示，KDE概率密度估计没有预设数据分布假设。有关 KDE概率密度估计，大家可以回顾《统计至简》第18章。# Sepal lengthSepal width

Sepal width

Sepal length

图21.

概率密度估计判断离群值，左图散点颜色对应数据 KDE概率密度估算值机器学习方法机器学习中很多算法都可以用来判断离群值。图22所示为用支持向量机和孤立森林算法判断鸢尾花数据中可能存在的离群值。更多机器学习算法，请大家参考《机器学习》一书。Page 17 | Chapter 3离群值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

Sepal lengthSepal width

Sepal lengthSepal width

图22.

支持向量机和孤立森林算法判定离群值

Bk6_Ch03_02.

py 绘制图21和图22。离群值指的是数据集中与其他值相差较远的异常值。离群值可能会对数据分析结果产生较大的影响，导致模型不准确或偏差。离群值的产生原因包括测量误差、数据录入错误、采集异常、样本选择偏差等。解决方法包括删除离群值、修正离群值、分别分析离群值等。注意事项包括要对数据进行探索性分析，了解数据分布和异常值的特点合理处理离群值避免对分析结果造成负面影响。时，在进行离群值处理时需要谨慎，避免过度修正，影响数据的真实性和可靠性。Scikit-learn中有更多利用机器学习方法检测离群值的方法请参考下例。org/stable/modules/outlier_detection.

htm l

建议大家学完丛书《机器学习》一册内容，再回过头来自学这几个例子。Page 1 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 4 Data Transformation s

数据转换代数和统计方法处理数据，以便后续回归、分类或聚类没有数据，就得出结论，这是大错特错。It is a capital mistake to theorize before one has data.

—— 阿瑟·柯南·道尔 (Arthur Conan Doyle ) | 英国小说作家医生 | 1859 ~ 1930

◄ numpy.

random.

exponential 产生满足指数分布随机数

◄ pandas.

plotting.

parallel_coordinates 绘制平行坐标图

◄ scipy.

stats.

boxcox Box -Cox数据转换

◄ scipy.

stats.

probplot 绘制QQ图

◄ scipy.

stats.

yeojohnson Yeo –Johnson 数据转换

◄ seaborn.

distplot 绘制概率直方图

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

jointplot 绘制联合分布和边际分布

◄ seaborn.

kdeplo t 绘制KDE核概率密度估计曲线

◄ seaborn.

violinplot 绘制数据小提琴图

◄ sklearn.

preprocessing.

MinMaxScaler 归一化数据

◄ sklearn.

preprocessing.

PowerTransformer 广义幂变换

◄ sklearn.

preprocessing.

StandardScaler 标准化数据

Page 2 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 4.

1数据转换本章介绍数据转换 (data transformation) 的常见方法。数据转换是数据预处理的重要一环，用来转换要分析的数据集，使其更方便后续建模，比如回归分析、分类、聚类、降维。注意，数据预处理时，一般先处理缺失值、离群值，然后再数据转换。数据转换的外延可以很广。函数 (比如指数函数、对数函数 )、中心化、标准化、概率密度估计、插值、回归分析主成分分析、时间序列分析平滑降噪等某种意义上都可以看做是数据比如，经过主成分分析处理过的数据可以成为其他算法的输入。图1总结本章要介绍的几种主要数据转换方法。下一章专门介绍插值。图1可以用作本章思维

Statistics -basedDemean

Standardization

Normalization

Power

transformationBox-Cox

Yeo-Johnson

ECDF

transformation

Copula

OthersKDE

Interpolation

Regression

PCA

Timeseries analysisData transformation

图1.

常见数据转换方法

# 4.2中心化：去均值数据中心化 (centralize

dem ean)

也叫去均值，是基于统计最基本的数据转换。对于一个给定特征去均值数据 (demeaned data

centered data ) 的定义为

mean Y X X=− (1)

其中，mean(X) 计算期望值或均值。Page 3 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 一般情况，多特征数据每一列数据代表一个特征。多特征数据的中心化，相当于每一列数据分别去均值。对于均值几乎为0的数据，去均值处理效果肯定不明显。原始数据本节用四种可视化方案展示数据它们分别是热图

KDE分布、小提琴图和平行坐标图。2 ~ 图5所示为这四种可视化方案展示的鸢尾花原始四个特征数据。相信丛书读者对前三种可视化方案应该很熟悉。这里简单介绍图5所示平行坐标图 (parallel

coordin ate plot)。一个正交坐标系可以用来展示二维或三维数据但是对于高维多元数据正交坐标系则显得而平行坐标图，可以用来可视化多特征数据。平行坐标图采用多条平行且等间距的轴，以折线形式呈现数据。图5还用不用颜色折线代表分类标签。02468

Sepal length Sepal width Petal length Petal width

图2.

鸢尾花数据，原始数据矩阵 X

µ1 = 5.

843, σ1 = 0.

825µ2 = 3.

057, σ2 = 0.

µ3 = 3.

758, σ3 = 1.

759µ4 = 1.

199, σ4 = 0.

0 2 4 6 80.

0Probability densitySepal length

Sepal width

Petal length

Petal width

图3.

鸢尾花数据四个特征上分布，KDE估计

Page 4 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

Sepal length Sepal width Petal length Petal width02468

图4.

鸢尾花原始数据，小提琴图

Setosa Versicolor Virginica

Sepal length Sepal width Petal length Petal width8

图5.

鸢尾花数据，平行坐标图中心化数据图6 ~ 图9则用这四种可视化方案展示去均值后鸢尾花数据。《矩阵力量》介绍过对于多特征数据去均值相当于将数据质心移动到0

但是对数据分布的离散度没有任何影响。3 2 13

Sepal length Sepal width Petal length Petal width

Page 5 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 图6.

数据热图，去均值

0Probability density

4 2 0 2 4Sepal length

Sepal width

Petal length

Petal width

图7.

数据KDE分布估计，去均值

Sepal length Sepal width Petal length Petal width 10123

图8.

小提琴图，去均值

Setosa Versicolor Virginica

Sepal length Sepal width Petal length Petal width0

3 2 13

图9.

平行坐标图，去均值

Page 6 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 4.

3标准化：Z分数标准化 (standardi zation ) 对原始数据先去均值然后再除以标准差

mean

stdXXZX−= (2)

处理得到的数值实际上是原始数据的 Z分数，表达若干倍的标准差偏移。比如，某个数值处理后结果为3，这代表数据距离均值3倍标准差偏移。注意，Z分数的正负代表偏离均值的方向。在机器学习中

standardization 和normalization 通常分别翻译为标准化和归一化。这两种预处理方法的主要区别在于对数据的缩放方式不同。标准化通常是指将数据缩放到均值为0，标准差为1的标准正态分布上。标准化可以通过先减去均值，再除以标准差来实现。标准化可以使得不同特征之间的数值尺度相同，避免某些特征对模型的影响过大，从而提高模型的鲁棒性和稳定性。归一化 (normalization ) 通常是指将数据缩放到 [0

1]或[-1

1]的区间上。归一化可以通过线性变换、MinMaxScaler 等方法来实现。归一化可以使得不同特征的权重相同，避免某些特征对模型的影响过大，从而提高模型的准确性和泛化能力。很多文献混用 standardization 和normalization

大家注意区分。图10、图11和图12分别展示的是经过标准化处理的鸢尾花数据的热图

KDE分布曲线和平行坐标图。《统计至简》一册讲过主成分分析 (Principal Component Analysis

PCA) 之前先对数据进行标准化。经过标准化后的数据，再求协方差矩阵，得到的实际上是原始数据的相关性系数矩阵。3 2 13

Sepal length Sepal width Petal length Petal width

Page 7 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 图10.

热图，标准化

4Probability density

2 0 2 4Sepal length

Sepal width

Petal length

Petal width

图11.

KDE分布估计，标准化

Sepal length Sepal width Petal length Petal widthSetosa Versicolor Virginica

2 13

图12.

平行坐标图，标准化

4.4归一化：取值在0和1之间归一化 (normali zation) 常指数据首先减去其最小值然后再除以 range(X)

即max(X) –

min(X)：min

max minXX

XX−

− (3)

通过上式归一化得到的数据取值范围在 [0, 1] 之间。图13、图14分别展示归一化鸢尾花数据的小提琴图和平行坐标图。Page 8 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

Sepal length Sepal width Petal length Petal width1.

图13.

小提琴图，归一化

Setosa Versicolor Virginica

Sepal length Sepal width Petal length Petal width

图14.

平行坐标图，归一化其他转换另外一种类似归一化的数据转换方式数据先去均值然后再除以 range( X)

mean

max minxXxXX−=−

(4)

这种数据处理的特点是，处理得到的数据取值范围约在 [−0.

5, 0.

5] 之间。还有一种数据转换使用箱型图的四分位间距 (interquartile range) 作为分母来缩放数据：meanXX

IQR X− (5)

其中

31 IQR Q Q=−。Page 9 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com Bk6_Ch04_01.

py 绘制本章之前几乎所有图像。# 4.5广义幂转换广义幂转换 (power transform)

也称 Box-Cox

是一种用于对非正态分布数据进行转换的方

Box-Cox转换通过一系列参数 λ的取值将数据的概率密度函数进行幂函数变换使得变换后的数据更加接近正态分布。Box-Cox转换可以通过最大似然估计或数据探索的方式来确定最优的λ值。Box-Cox转换可以帮助我们改善非正态分布数据的统计性质如方差齐性、线性关系和偏度等从而提高模型的准确性和稳定性。Box-Cox转换广泛应用于回归分析、时间序列分析、贝叶斯分析等领域。Box-Cox转换具体为：ln 0x

x

x

 

− =

 =  (6)

其中，x为原始数据

x(λ) 代表经过 Box-Cox转换后的新数据

λ为转换参数。注意，Box-Cox转换要求参与转换的数据为正数。在进行 Box-Cox转换之前，需要确保数据都是正数。如果数据包含负数或零，可以先对数据进行平移或加上一个较小的正数使得数据都变成正数然后再进行 Box-Cox转换。另外，如果数据中存在较小的负数或零也可以考虑使用其他的转换方法如 Yeo-Johnson转换它可以处理包含负数的数据。实际上，Box-Cox转换代表一系列转换。其中，λ = 0.

5时，叫平方根转换；λ = 0时，叫对数

λ = −1时，为倒数转换。大家观察上式可以发现，它无非就是两个单调递增函数。Box-Cox转换通过优化 λ参数让转换得到的新数据明显地展现出正态性 (normality)。正态性指的是一个随机变量服从高斯分布的特性。正态分布是一种常见的概率分布，其概率密度函数呈钟形曲线，具有单峰性、对称性和连续性。如果一个数据集或随机变量的分布近似于正态分布，那么它就具有正态性，也称为正态分布性。正态性在统计分析中非常重要，因为很多经典的统计方法，如 t检验、方差分析等，都基于正态分布的假设。如果数据不服从正态分布，可能会影响到模型的可靠性和精度，需要采取相应的数据预处理或选择适当的非参数方法。Page 10 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

(a) original data (b) transformed data

图15.

原始数据和转换数据的直方图

NormalOriginal data

NormalTransformed data

图16.

原始数据和转换数据的 QQ图

Yeo-Johnson 转换前文提过 Yeo-Johnson可以处理负值，具体数学工具为：2110, 0

ln 1 0, 0

2, 02

ln 1 2, 0x

x

xx

x

xx

x x







−+− 



+ = +−

=

−− −

−+− = (7)

Bk6_Ch04_0 2.

py绘制图15和图16。sklearn.

p reprocessing.

PowerTransformer 函数同时支持

‘yeo-johnson’和‘box-cox’ 两种方法。Page 11 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

com 4.

6经验累积分布函数《统计至简》第9章一册提到经验累积分布函数 (Empirical Cumulative Distribution

Function, ECDF ) 实际上也是一种重要的数据转换函数。ECDF是一种非参数的数据转换方法。ECDF的特点是简单易懂不需要对数据进行任何假设或参数估计适用于任何类型的数据分布，包括连续型和离散型数据。通过将原始数据转换为概率分布函数，可以更好地理解数据的分布情况，并与理论分布进行比较，从而判断数据是否符合某种分布模型。图17所示为样本数据和其经验累积分布的关系。如图18所示，u = ECDF (x) 代表经验累积分布函数；其中，x为原始样本数值，u为其 ECDF

u的取值范围为 [0, 1]。u = ECDF (x)具有单调递增特性。u = ECDF (x) 对应 Scikit-learn中的 sklearn.

preprocessi ng.

QuantileTransformer 函数。图19所示为鸢尾花数据四个特征的ECDF图像。# PDF

ECDF 1

图17.

ECDF函数转换样本数据

u = ECDF( x)

x1

图18.

ECDF函数原理

Page 12 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

Sepal length

Sepal width

Petal length

Petal widthEmpirical CDF

图19.

鸢尾花数据四个特征的 ECDF

散点图如图19所示经过 ECDF转换鸢尾花四个特征的样本数据都变成了 [0

1] 区间的数据。组数据肯定也有自己的分布特点。图20所示为花萼长度、花萼宽度 ECDF散点图和概率密度等高线。图21所示为鸢尾花数据 ECD F的成对特征图。# Sepal length ECDF

u1Sepal width ECDF

0 101

图20.

鸢尾花花萼长度、花萼宽度 ECDF散点图容易发现 param etric (theoretical ) CDF 和empirical CDF的取值范围都是 [0

1]，而且是一一对应关系，这就是我们反复提到过的

CDF曲线是很好的映射函数可以将任意取值范围的数值映射到 (0, 1) 区间而且得到的具体数值有明确的含义即累积概率值可以解释。Page 13 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

x4Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

图21.

鸢尾花数据 ECDF的成对特征图

Bk6_Ch04_0 3.

py绘制图20和图21。连接函数大家肯定会问，有没有一种分布可以描述图20、图21所示概率分布？答案是肯定的！这就是连接函数 (copula)。连接函数是一种描述协同运动 (co-movement ) 的方法。定义向量： 12 D x x x

(8)

它们各自的边缘经验累积概率分布值可以构成如下向量：  1 2 1 1 2 2 ECDF ECDF ECDFD D D u u u x x x =

(9)

其中

ECDFj j jux= 为Xj的边缘累积概率分布函数

uj的取值范围为 [0

图22所示为以二元为例展示原数据和 ECDF的关系。Page 14 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

x1x201

0 1u1

x1

x2

u2x1

x2u1u2

u2 = ECDF 2(x2)u1 = ECDF 1(x1)

图22.

x1和x2，和 u1和u2的关系反方向来看 (9)：  1 1 1

1 2 1 1 2 2 ECDF ECDF ECDFD D D x x x u u u− − −=

(10)

1ECDFj j jxu−= 为逆累积概率分布函数 (inverse empirical cumulative dis tribution function )

也就是累积概率分布函数

ECDFj j jux= 的反函数。连接函数 C可以被定义为：1 1 1

1 2 1 1 2 2, ,.

ECDF ECDF ,ECDF ,.

,ECDFD D D C u u u u u u− − −= (11)

连接函数的概率密度函数，也就是 copula PDF可以通过下式求得：1 2 1 2

12, ,.

, ,.

DD

Dc u u u C u u uu u u=    (12)

图23展示的是几种常见连接函数其中最常用的是高斯连接函数 (Gaussian copula)。本书不做展开讲解，请感兴趣的读者自行学习。Page 15 | Chapter 4数据转换 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https: //github.

com /Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visuali ze.

Gaussian

Student -t

Frank

Clayton

GumbelElliptical

ArchimedeanCopula

图23.

常见连接函数在机器学习中，数据转换是将原始数据进行处理或转换，以更好地适应模型的需求。数据转换方法包括中心化、标准化、归一化、对数转换、指数转换和广义幂转换等方法。法可以根据数据的分布特点、度量单位、取值范围和变量之间的关系进行选择和应用。正确的数据转换可以提高模型的预测精度，从而提高模型的应用效果。然而，不同的数据转换方法可能对同一数据集产生不同效果，需要进行比较和评估。如下网页专门介绍 Scikit-learn预处理，请大家参考：org/stable/modules/pre processing.

html

此外，Scikit-learn有大量的数据转换函数，请大家学习如下两例：org /stable/auto_examples/preproc essing/plot_all_scaling.

html

org/stable /auto_exampl es/preprocessing/plot_map_data_to_normal.

html

Statsmodels支持连接函数，请大家参考：statsmodels.

org/dev/examples/notebooks/generated/copula.

html

Page 1 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 5 Interpo lation

插值分段插值函数，通过已知数据点人们思考皆，浮皮潦草，泛泛而谈；现实世界却，盘根错节，千头万绪。# We think in generalities

but we live in details.

—— 阿尔弗雷德·怀特海 (Alfred Whitehead) | 英国数学家哲学家 | 1861 ~ 1947

◄ scipy.

interpolate.

interp1d 一维插值

◄ scipy.

interpolate.

lagrange 拉格朗日多项式插值

◄ scipy.

interpolate.

interp 2d 二维插值，网格化数据

◄ matplotlib.

pyplot.

pcolormesh 绘制填充颜色网格数据

◄ scipy.

interpolate.

griddata 二维插值，散点化数据

◄ matplotlib.

pyplot.

imshow 绘制数据平面图像

Page 2 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 5.

1插值插值是通过已知数据点之间的值来估计未知点的值的方法，它可以用于填补数据缺失或者进行数据平滑处理。插值方法通常基于已知数据点之间的关系，通过数学函数或者曲线拟合等方法来预测未知数据点的值。如图1所示的蓝色点为已知数据点插值就是根据这几个离散的数据点估算其他点对应的 y

插值可分为内插 (interpolation) 和外插 (extrap olation)。内插是在已知数据点之间进行插值，估计出未知点的值。而外插则是在已知数据点的范围之外进行插值，从而预测超出已知数据点范围的未知点的值。在进行外插时，需要考虑插值函数是否能够正确地拟合未知数据点，并且需要注意不要过度依赖插值函数来进行预测，以免导致不可靠的预测结果。xy

Interpolation Extrapolation Extrapolation

图1.

插值的意义常见插值方法图2总结常用的插值的算法。图2相当于本章的思维导图。本章主要介绍如下几种方法：◄ 常数插值 (constant interpolation)

比如向前 (previous或forward )

向后 (next或backward )

邻近 (nearest)；◄ 线性插值 (linear interpolation)；◄ 二次插值 (quadratic interpolation)

本章不做介绍；◄ 三次插值 (cubic interpolation)；◄ 拉格朗日插值 (Lagrange polynomial interpolation )。Page 3 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 本章最后还要介绍二维插值 (bivariate interpolation)

二维插值将一元插值的方法推广到二此外，对于时间序列，处理缺失值或者获得颗粒度更高的数据，都可以使用插值。图3所示为利用线性插值插补时间序列数据中的缺失值。《可视之美》介绍的贝塞尔曲线本质上也是插值。贝塞尔曲线是一种通过一系列控制点来定义曲线形状的数学函数。在计算机图形学和计算机辅助设计中，常使用贝塞尔曲线来生成平滑的曲线形状。PiecewiseConstant Forward /previous

Backward/next

Nearest interpolation

PolynomialLinear interpolation

Quadratic interpolation

Cubic interpolation

Lagrange polynomial

interpolation

MultivariateBivariate interpolationInterpolation

图2.

插值的分类

Jan Feb Mar Apr Jan Feb Mar AprMissing

Missing

Missing

图3.

时间序列插值分段函数

Page 4 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 虽然，一些插值分段函数构造得到的曲线整体看上去平滑。但是绝大多数情况，插值函数是分段函数，因此插值也称分段插值 (piec ewise interpolation)。《数学要素》第11章介绍过分段函数。对于一元函数 f(x)

分段函数是指自变量 x在不同取值范围对应不同解析式的函数。每两个相邻的数据点之间便对应不同解析式：1nn

nf x x x x

f x x x xfx

f x x x x−

− 



 =





(1)

其中，n为已知点个数。注意，上式中 fi(x) 代表一个特定解析式。分段函数虽然由一系列解析式构成，但是分段函数还是一个函数。如图4所示已知数据点一共有五个 —— (x(1)

y(1))、(x(2)

y(2))、(x(3)

y(3))、(x(4)

y(4))、(x(5)

y(5))。比如，分段函数 f(x) 在 [x(1)

x(2)] 区间的解析式为f1(x)。f1(x) 通过 (x(1)

y(1))、(x(2)

y(2)) 两个已知数据图4实际上就是线性插值。(1) 还告诉我们对于内插，n个已知点可以构成 n – 1个区间即分段函数有 n – 1个解析

xy

Interpolation(x(1), y(1))(x(2), y(2))

(x(3), y(3))(x(4), y(4))

(x(5), y(5))

f1(x)f2(x)f3(x)f4(x)

图4.

分段函数拟合、插值大家经常混淆拟合和插值这两种方法。插值和拟合有一个相同之处，它们都是根据已知数据点，构造函数，从而推断得到更多数据点。Page 5 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 插值和回归都是用于对数据进行预测的方法，但两者有明显的区别。插值是用于填补已有数据点之间的空缺，预测未知点的值。回归则是预测自变量和因变量之间的关系。插值通常使用插值函数，如多项式插值；而回归则通过拟合数据点的回归方程来预测因变量的值。插值通常用于数据平滑处理、数据填补等。回归则常用于预测和建模。插值要求原始数据点之间要有一定的连续性和平滑性；而回归则对数据点的分布没有明显要求。插值得到的是精确的函数值，但在超出已有数据范围时可能不准确；而回归得到的是变量之间的大致关系，可以预测未来的趋势。需要根据具体情况选择合适的方法。当数据缺失或需要平滑处理时，可以使用插值方法；需要建立模型并预测未来趋势时，可以使用回归方法。插值一般得到分段函数分段函数通过所有给定的数据点如图5 (a)

(b) 所示。回归拟合得到的函数尽可能靠近样本数据点，如图5 (c)、(d) 所示。图6比较二维插值和二维回归。(a) linear interpolation (b) cubic interpolation

(c) linear regression (d) polynomial regression

图5.

比较一维插值和回归

Page 6 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

(a) linear interpolation (b) polynomial regression

图6.

比较二维插值和二维回归

# 5.2常数插值：分段函数为阶梯状本节介绍常用的三种常数插值方法。向前向前常数插值对应的分段函数为：1 1 2

2 2 3

1n n n

nf x x x x x

f x x x x xfx

f x x x x x−−

−=  



=  =



=  

(2)

如图7所示向前常数插值用区间 [x(i)

x(i + 1)] 左侧端点即 x(i)

对应的 y(i)

作为常数函数的图7中红色划线为真实函数取值。对于数据帧 df，如果存在 NaN的话，df.

fillna(method = 'ffill') 便对应向前常数插补。Page 7 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

0 1 2 3 4 5 6

x01

1y

f1(x)f2(x)f3(x)

f4(x)

f5(x)

f6(x)

图7.

向前常数插值向后向后常数插值对应的分段函数为：2 1 2

3 2 3

1n n n

nf x x x x x

f x x x x xfx

f x x x x x−

−=  



=  =



=  

(3)

如图8所示，向后常数插值和图7正好相反。对于数据帧 df，如果存在 NaN的话，df.

fillna(method = ' bfill') 对应向后常数插补。0 1 2 3 4 5 6

x01

1yf1(x) f2(x)

f3(x)

f4(x)

f5(x)f6(x)

图8.

向后常数插值最邻近最邻近插值的分段函数为：Page 8 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

1 2 2 3

2nn

nn

nxxf x x x x

x x x xf x x xfx

xxf x x x x− +=  



 ++=  =





 +=  

(4)

如图9所示，最邻近常数插值相当于 “向前”和“向后”常数插值的 “折中”。分段插值函数同样是阶梯状，只不过阶梯发生在两个相邻已知点中间处。0 1 2 3 4 5 6

x01

1y

f1(x)f2(x)f3(x)

f4(x)

f5(x)

f6(x)f7(x)

图9.

最邻近常数插值

5.3线性插值：分段函数为线段对于线性插值，区间 [x(i), x(i + 1)] 对应的 fi(x) 为：slopeii

ii

i iiyyf x x x y

xx+

++

+−= − +−

(5)

容易发现，上式就是《数学要素》第11章介绍的一元函数的点斜式。也就是说，不考虑区间的话上式代表通过 (x(i)

y(i))、(x(i + 1)

y(i + 1)) 两点的一条直线。图10所示为线性插值结果。白话说，线性插值就是用任意两个相邻已知点连接成的线段来估算其他未知点的值。Page 9 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

0 1 2 3 4 5 6

x01

1yf1(x)f2(x)

f3(x)

f4(x)f5(x)f6(x)

图10.

线性插值

5.4三次样条插值：光滑曲线拼接图11所示为三次样条插值的结果。虽然，整条曲线看上去连续、光滑，实际上它是由四个函数拼接起来的分段函数。对于三次样条插值，每一段的分段函数是三次多项式：i i i i if x a x b x c x d= + + + (6)

其中，ai、bi、ci、di为需要求解的系数。0 1 2 3 4 5 6

x01

1yf1(x)f2(x)

f3(x)

f4(x)f5(x)f6(x)

图11.

三次样条插值为了求解系数，我们需要构造一系列等式。类似线性插值，每一段三次函数通过区间 [x(i), x(i +

1)] 左右两点，即：Page 10 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

111,2,.

1,2,.

, 1ii

i

ii

if x y i n

f x y i n++ = = −

= = −  (7)

曲线之所以看起来很平滑是因为除两端样本数据点以外内部数据点处一阶和二阶导数

11,2,.

1,2,.

, 2ii

ii

ii

iif x f x i n

f x f x i n++

+

++

+= = − = = −  (8)

对于三次样条插值，一般还设定两端样本数据点处二阶导数为0：0n

nfx

fx−== (9)

插值中系数求解一般都是用矩阵运算完成。举个例子，在三次样条插值中，需要解出一个三对角线方程组，这个方程组可以用矩阵形式表示。具体来说，需要先确定每个小区间内的多项式系数，然后利用这些系数和每个小区间的边界点构造一个三对角矩阵方程组利用三对角矩阵求解方法，可以得到每个小区间内的多项式系数，从而得到整个分段函数。本章不展开讲解。Bk6_Ch05_01.

py 完成插值并绘制图7 ~ 图11。Python进行一维插值函数为

scipy.

interpolate.

interp1d，二维插值的函数为scipy.

interp olate.

interp2 d。# 5.5拉格朗日插值拉格朗日插值 (Lagrange interpolation ) 不同于本章前文介绍的插值方法。前文介绍的插值方法得到的都是分段函数，而拉格朗日插值得到的是一个高次多项式函数 f(x)。f(x) 相当是由若干多项式函数叠加而成：1n

i

if x f x

== (10)

1,k n

i

i ik

k k ixxf x y

xx=−=

− (11)

fi(x) 展开来写：Page 11 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

1 2 1 1

1 2 1 1 2i i n

i

ii i i i i i nx x x x x x x x x x

f x y

x x x x x x x x x x−+

−+− − − − −

=

− − − − −

(12)

比如，f1(x) 展开来写：11 2 1 3 1n

nx x x x x x

f x y

x x x x x x− − −

=

− − −

(13)

f2(x) 展开来写：22 1 2 3 2n

nx x x x x x

f x y

x x x x x x− − −

=

− − −

(14)

举个例子比如，n = 3

也就是有三个样本数据点 {(x(1)

y(1)), (x(2)

y(2)), (x(3)

y(3))} 的时候

f(x) 为

1 2 32 3 1 3 1 2

1 2 3

1 2 1 3 2 1 2 3 3 1 3 2

f x f x f xx x x x x x x x x x x x

f x y y y

x x x x x x x x x x x x− − − − − −

=  +  + 

− − − − − −

(15)

观察上式，f(x) 相当于三个二次函数叠加得到。将三个数据点 {(x(1)

y(1)), (x(2)

y(2)), (x(3)

y(3))}

逐一代入上式可以得到：1 1 2 2 3 3, , f x y f x y f x y= = = (16)

也就是说，多项式函数 f(x) 通过给定的已知点。图12所示为拉格朗日插值结果。0 1 2 3 4 5 6

x01

1yf(x)

图12.

拉格朗日插值

Page 12 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

龙格现象有一点需要大家注意的是已知点数量 n不断增大拉格朗日插值函数多项式函数次数不断提高，插值多项式的插值逼近效果未必好。如图13所示，插值多项式 (红色曲线 ) 区间边缘处出现振荡问题，这一现象叫做龙格现象 (Runge's phenomenon )。图13.

龙格现象

Bk6_Ch05_0 2.

py完成拉格朗日插值，并绘制图12。# 5.6二维插值如图14所示，以二维线性插值为例，二维线性插值相当于处理了三个一维线性插值。对于二维线性插值，先将二维坐标系中的点分别按照横坐标和纵坐标排序。然后，找到待插值点所在的四个相邻的点。分别对这四个点在横坐标和纵坐标上进行一维线性插值，得到在横向和纵向上的两个插值结果。将上述两个插值结果加权平均，作为待插值点的二维线性插值结果。其中，权重的计算基于待插值点相对于四个相邻点在横向和纵向上的距离距离越远的点权重越

Page 13 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

KnownKnown

KnownKnownInterpolated

图14.

二维线性插值原理举个例子图15中 × 为给定的已知数据。图16和图17所示为分别通过线性插值、三次样条插值完成的二维插值结果。二维插值用到的函数是 scipy.

interpolate.

interp2d。图15.

已知数据点

Page 14 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

图16.

二维插值，规则网格，线性插值图17.

二维插值，规则网格，三次样条

Bk6_Ch05_0 3.

py完成二维插值，并绘制图16和图17。不规则散点大家可能已经注意到，图15给定的已知数据是规整的网格数据。当数据并不是规整的网格数据，而是不规则的散点时，我们也可以用 scipy.

interpolate.

griddata 完成二维插值。图18、图19、图20分别所示为利用最邻近线性、三次样条方法完成不规则散点的二维插值。Page 15 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

图18.

二维插值，不规则散点，最近邻图19.

二维插值，不规则散点，线性插值图20.

二维插值，不规则散点，三次样条插值

Page 16 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com Bk6_Ch05_0 4.

py完成不规则散点插值，并绘制图18、图19、图20。更多插值方法

matplotlib.

pyplot.

imshow 绘图函数自带大量二维插值方法，请大家参考图21。none nearest bilinear bicubic spline16 spline36

hanning hamming hermite kaiser quadric catrom

gaussian bessel mitchell sinc lanczos blackman

图21.

imshow 函数插值方法

Bk6_Ch05_0 5.

py绘制图21。插值是一种通过已知数据点推断出连续函数在其他位置上取值的方法。在实际问题中，我们常常只知道一些离散的数据点，但需要通过这些数据点来推断出函数在其他位置的取值。以通过拟合一条曲线、平面或者高维曲面来达到这个目的，从而实现对函数的估计。在机器学习中，插值可以用于对数据进行处理和预处理。插值可以通过拟合一条平滑的曲线或者曲面来填充数据中的缺失值，从而获得完整的数据集，这可以提高模型的准确性和可靠性。Page 17 | Chapter 5插值 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。co m/Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 请大家格外注意插值和回归都是处理数据的方法但插值是通过已知的数据点之间的值来估计未知点的值，而回归是通过已知的数据点来拟合一个函数，预测未知点的值。插值的目的是将数据点之间的缺失值或噪声进行平滑处理，而回归的目的是对数据进行预测和建模。虽然两者都是通过已知数据点来估计未知点的值，但它们的目的和使用场景是不同的。Page 1 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 6 Time Series

时间数据具有时间戳的数据序列我们能看到的有限长的未来，但是面对无限多的问题。# We can only see a short distance ahead

but we can see plenty there that needs to be done.

—— 艾伦·图灵 (Alan Turing ) | 英国计算机科学家数学家，人工智能之父 | 1912 ~ 1954

◄ statsmodels.

api.

t sa.

seasonal_dec ompose 季节性调整

◄ numpy.

random.

uniform 生成满足均匀分布的随机数

◄ df.

ffill 向前填充缺失值

◄ df.

bfill 向后填充缺失值

◄ df.

interpolate 插值法填充缺失值

◄ seaborn.

boxplot 绘制箱型图

◄ seaborn.

lineplot 绘制线图

Page 2 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

处理缺失值向前向后线性插值时间数据趋势项季节项循环项随机项时间序列分解季节调整

Page 3 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

com 6.

1时间序列数据时间序列 (timeseries ) 是一种特殊的数据类型是指按照时间顺序排列的数据集合其中每个数据点都与特定的时间点相关联。时间戳 (timestamp ) 可以精确到年份，月份，日期，甚至是小时、分、秒。简单来说，时间序列可以用来描述某个变量随时间变化的趋势和模式。例如，一支股票的价格随时间变化的数据集就是一个时间序列每个数据点对应着一个特定的日期和该日期下的股票另一个例子是天气数据，例如每小时记录的温度、湿度和风速，它们也可以被组织成时间序列，以便分析和预测气象变化趋势。如图1所示历史数据 (historical data) 是指已经发生的数据它们是用来分析和理解过去发生的事件和趋势的。预测数据 (forecasted data) 是指未来可能发生的数据它们是根据历史数据和模型进行推算得出的。历史数据可以用来训练模型，帮助模型学习过去的规律和趋势，从而提高预测的准确性。测数据则可以用来制定决策、规划资源和制定策略。历史数据和预测数据是相互依存的，历史数据是预测数据的基础，预测数据又可以帮助我们更好地理解历史数据。在时间序列分析中，历史数据和预测数据是两个不可或缺的部分。t t 5Now

t 1 t + 1 t + 5

Past FutureLag = 5

图1.

图2所示为2020年度中9支股票的每个营业日股价数据。图2中数据共有253行，每行代表一个日期及当日股价水平；时间数据表格共有10列，第1列为时间戳，其余9列每列为股价数据。除去时间戳一列和表头，图2可以看成一个矩阵。Page 4 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Date TSLA TSM COST NVDA FB AMZN AAPL NFLX GOOGL

2-Jan-2020 86.

05 58.

26 281.

10 239.

51 209.

78 1898.

01 74.

33 329.

81 1368.

3-Jan-2020 88.

60 56.

34 281.

33 235.

68 208.

67 1874.

97 73.

61 325.

90 1361.

6-Jan-2020 90.

31 55.

69 281.

41 236.

67 212.

60 1902.

88 74.

20 335.

83 1397.

7-Jan-2020 93.

81 56.

60 280.

97 239.

53 213.

06 1906.

86 73.

85 330.

75 1395.

8-Jan-2020 98.

43 57.

01 284.

19 239.

98 215.

22 1891.

97 75.

04 339.

26 1405.

9-Jan-2020 96.

27 57.

48 288.

75 242.

62 218.

30 1901.

05 76.

63 335.

66 1419.

... ... ... ... ...

21-Dec-2020 649.

86 104.

44 364.

25 533.

29 272.

79 3206.

18 128.

04 528.

91 1734.

22-Dec-2020 640.

34 103.

55 361.

32 531.

13 267.

09 3206.

52 131.

68 527.

33 1720.

23-Dec-2020 645.

98 103.

37 361.

18 520.

37 268.

11 3185.

27 130.

76 514.

48 1728.

24-Dec-2020 661.

77 105.

57 363.

86 519.

75 267.

40 3172.

69 131.

77 513.

97 1734.

28-Dec-2020 663.

69 105.

75 370.

33 516.

00 277.

00 3283.

96 136.

49 519.

12 1773.

29-Dec-2020 665.

99 105.

16 371.

99 517.

73 276.

78 3322.

00 134.

67 530.

87 1757.

30-Dec-2020 694.

78 108.

49 373.

71 525.

83 271.

87 3285.

85 133.

52 524.

59 1736.

31-Dec-2020 705.

67 108.

63 376.

04 522.

20 273.

16 3256.

93 132.

49 540.

73 1752.

图2.

股票收盘股价数据图3利用线图可视化股票收盘股价走势。图3 (b) 右图初始股价归一化处理，这些曲线更容易比较不同股票的涨跌情况。0500100015002000250030003500Adjusted closing price

TSLA

TSM

COSTNVDA

FB

AMZNAAPL

NFLX

GOOGL2020 Jan

2020 Mar

2020 May

2020 Jul

2020 Sep

2020 Nov

2021 Jan

2020 Jan

2020 Mar

2020 May

2020 Jul

2020 Sep

2020 Nov

2021 Jan12345678Normalized price(a) (b)

图3.

股票收盘股价走势，和初始值归一化，时间序列数据

Page 5 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 我们先介绍损益 (Profit and Loss

PnL) 这个概念。损益 PnL是指某个交易或投资策略在一定时期内的总收益或总损失。它是通过将所有交易的盈利和亏损加总起来得出的。正的 PNL 表示盈利，负的 PNL 表示亏损。如图4所示只考虑某只股票收盘价 S在t时刻和 t – 1时刻 (工作日 ) 的变动，通过如下公式计算出 t时刻的日损益：1 PnLt t tSS−=− (1)

Date stampStock

price

t 3StSt 1St 2

St 3

Intraday

t 2 t 1 t

图4.

某股票的价格变动下面介绍收益率 (return ) 这个概念。在不考虑分红 (dividend ) 的条件下，单日简单回报率

(daily simple return) 可以这样计算：1tt

t

tSSrS−

−−= (2)

股票分红是指上市公司根据其盈利情况在向股东分配利润之后以现金或股票形式再次向股东发放一部分盈利的行为。这种行为使得持有公司股票的股东可以从公司利润中获得收益，同时也是上市公司回报投资者、增强投资者信心的一种方式。分红通常以每股派息或每股送股的形式实施，也可以同时采用这两种方式。量化金融建模还经常使用日对数回报率 (daily log return)：1lnt

t

tSrS−=

 (3)

对数收益率的计算结果具有可加性，也就是说，多个时间段的对数收益率之和等于总时间段的对数收益率。这个特性在计算投资组合收益率时非常有用。量化金融建模时一般会假设股价服从对数正态分布这样对数收益率的分布更加接近正态分布，这对于一些金融模型的应用很实用，例如对冲基金、风险管理和投资组合优化等。续经常使用日对数收益率。图5所示为只股票在不同年份的日收益率分布利用高斯分布估计样本分布多数情况下似乎是个不错的选择。图6所示为利用 KDE估算得到概率密度。大家可以发现数据的统计量 (均值、方差、均方差、偏度、峰度 ) 随着时间变化。Page 6 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

# 0.15 0.10 0.05 0.00 0.05 0.10 0.15

图5.

收益率数据山脊图，按年分类

# 0.15 0.10 0.05 0.00 0.05 0.10 0.15

图6.

收益率数据 KDE山脊图，按年分类鸢尾花数据，我们可以打乱数据的先后排列。但是时间序列是一个顺序序列，数据的先后顺序一般情况是不允许打乱的。有些情况，我们可以不考虑数据点的时间，比如图7所示回归分析中的散点图。本书第10、11章将介绍线性回归模型。Page 7 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

# 0.1 0.1 0.0

x 0.

图7.

线性 OLS回归分析和散点图

6.2处理时间序列缺失值时间数据序列在分析建模之前，也需要注意数据中的缺失值和异常值处理。本节从时间序列角度加以补充缺失值处理。本书第2、3章分别介绍如何处理缺失值和异常值。前文强调，时间序列数据是顺序观察的数据；因此在处理缺失值时，有其特殊性。比如，时间序列出具可以采用均值众数、中位数插值等一般方法也可以采用如向前向后这种方

Page 8 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

DeletionDeleting rows

Deleting columns

Pairwise deletion

ImputationGeneralCategorical Logistic regression

Make NaN as new cl ass

Multiple imputation

ContinuousMean, mode, or median

Multiple imputation

Linear regression

TimeseriesHandle missing data

Data with trend, but

without seasonalityData without trend

and seasonality

Data with trend and

with seasonalityMean, mode, or median

Random sample imputation

Linear regression

Seasonal adjustment +

interpolationForward fill, backward fill

图8.

处理缺失值图9 ~ 图11比较三种不同处理时间序列缺失值的基本方法。# Price level

Date?

图9.

向前插值填充缺失值

Page 9 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Price level

Date?

图10.

向后插值填充缺失值

Price level

Date?

图11.

线性插值填充缺失值

Bk6_Ch0 6_01.

py绘制图9 ~ 图11。# 6.3从时间数据中发现趋势本节利用美国失业率数据介绍如何从时间数据中发现趋势。图12所示为失业率的原始数据。数据从1950年开始到2021年，每月有一个数据点。观察图12这幅图虽然存在“噪音”

我们已经能够大致看到失业率的按照年份的大致走势。下一章会介绍移动平均的方法来消除 “噪音”。Page 10 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 观察图12的局部图中我们还发现不同年份中一年内失业率存在某种特定的 “模式”。说，图中的 “噪音”可能存在重要的价值！图13所示为按月同比规律。同比是一种比较方式，用于比较同一时间段内两年或多年的某项指标的变化情况。同比通常表示为百分比或比率，可以用来分析和评估一个公司或经济指标在不同年份间的表现。同比的计算方法是将当前时间段的指标值减去同一时间段上一年的指标值然后将差值除以上一年的指标值，再乘以100%。这个计算结果就是同比指标，可以表示为百分比。与历史同时期比较，例如2005年7月份与2004年7月份相比称其为同比。相比图12，图13

更容易发现失业率变化规律。# Unemployment rate14

1959 1969 1979 1989 1999 2009 2019

图12.

原始失业率数据和局部放大图

2000 2005 2010 201510

4Unemployment rateJan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Page 11 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 图13.

失业率，按月同比图14所示为年内环比数据。环比是一种比较方式，用于比较相邻两个时间段内某项指标的变化情况。环比指标通常表示为百分比或比率，可以用来分析和评估一个公司或经济指标在不同时间段内的表现。环比的计算方法是，将当前时间段的指标值减去上一个时间段的指标值，然后将差值除以上一个时间段的指标值，再乘以100%。这个计算结果就是环比指标，可以表示为百分比。与上一统计段比较，例如2005年7月份与2005年6月份相比较称其为环比。我们似乎发现失业率存在某种年度周期规律。一年之内春天的失业率往往较低，这似乎和春天农业生产用工有而每一年的一月份的失业率显著提高这可能和圣诞节新年节庆之后用工下降有关。为了进一步看到失业率随年度变化我们可以用箱型图对年内失业率数据加以归纳如图15

箱型图的均值代表年度失业率的平均水平。箱型图的四分位间距 IQR告诉我们年度失业率的变化幅度。显然，失业率在2020年出现“前所未闻 ”的大起大落。图16所示为月份失业率箱型图。比较月份失业率的平均值变化，一月份的平均失业率确实陡然升高，这也印证了之前的猜测。下一节，我们就介绍如何将不同的成分从原始时间数据从分离

4Unemployment rate2000

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec

图14.

失业率，年内环比

Page 12 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Unemployment rate14

图15.

年度失业率数据箱型图

Unemployment rate14

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec

图16.

月份失业率数据箱型图

Bk6_Ch06_0 2.

py绘制本节图像。# 6.4时间序列分解时间序列有如图17所示的几种主要的组成部分。具体定义如下：Page 13 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com ◄ 趋势项 (trend component ) T(t)

表征时间序列中确定性的非季节性长期总体趋势通常呈现出线性或非线性的持续上升或者持续下降。当一个时间序列数据长期增长或者长期下降时，表示该序列有趋势。在某些场合，趋势代表着“转换方向”。例如从增长的趋势转换为下降趋势。◄ 季节项 (seasonal comp onent ) S(t)

表征时间序列中确定性的周期季节性成分是在连续时间内

(例如连续几年内 ) 在相同时间段 (例如月或季度 ) 重复性的系统变化。当时间序列中的数据受到季节性因素的影响时，表示该序列具有季节性。季节性总是一个已知并且固定的频率。◄ 循环项 (long-run cycle c ompone nt) C(t)。循环项代表是相对周期更长 (例如几年或者十几年) 的重复性变化，但一般没有固定的平均周期，往往与大型经济体的经济周期息息相关。于时间跨度较短，循环项很难体现出来，这时可能就被当作趋势项来分析了。当时间序列数据存在不固定频率的上升和下降时，表示该序列有周期性。这些波动经常由经济活动引起，并且与“商业周期”有关。周期波动通常至少持续两年。◄ 随机项 (stochastic component ) I(t)

表征时间序列中随机的不规则成分体现出一定的自相关性以及持续时间内无法预测的周期。该成分可以是噪声，但不一定是。往往认为随机项包含有与业务自身密切相关的信息。# Linear

Nonlinear

Short -term

movementsCyclic

Seasonal

Random or irregularComponents

of timeseriesLong -term

movements

图17.

时间序列成分许多时间序列同时包含趋势、季节性以及周期性。基于以上的主要成分，一个时间序列可以有以下几种组合模型。加法模型加法模型 (additive model)，各个成分直接相加得到：X t T t S t C t I t= + + + (4)

Page 14 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 这可能是最常用的时间序列分解方式。如果一个时间序列仅仅由趋势项 T(t) 和随机项 I(t) 构

X t T t I t=+ (5)

X(t) = T(t) + I(t)T(t)

I(t)

图18.

累加分解，原始数据 X(t)被分解为趋势成分 T(t)和噪音成分 I(t)

标普500指数长期来看随时间增长按照经济周期涨跌短期来看指数每天波动不止。趋势成分 (trend component ) TR(t) 就可以描述这种时间序列的长期行为而不规则成分 (irreg ular

component ) IR(t) 描述的就是噪音成分或者说是随机运动成分。T(t)

X(t) = T(t) + S(t) + I(t)

I(t)S(t)

图19.

累加分解，原始数据 X(t)被分解为趋势成分 T(t)

季节成分 S(t) 和噪音成分 I(t)

乘法模型乘法模型 (multiplicative model )

各个成分直接相乘得到

Page 15 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

X t T t S t C t I t=    (6)

如果只考虑趋势项 T(t) 和随机项 I(t)：X t T t I t= (7)

1X(t) = T(t) × I(t)T(t)

I(t)

图20.

累乘分解，原始数据 X(t)被分解为趋势成分 T(t)和噪音成分 I(t)

考虑季节成分的乘法模型：X t T t S t I t=   (8)

1X(t) = T(t) × S(t) × I(t)

1T(t)

S(t)

I(t)

图21.

累乘分解，原始数据 X(t)被分解为趋势成分 T(t)和噪音成分 I(t)

当然，时间序列还可以存在其他分解模型。比如对数加法模型 (log-additive model )，时间序列取对数后由各个成分相加得到：lnX t T t S t C t I t= + + + (9)

Page 16 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 上式相当于对X(t) 进行对数转换。对于更复杂的时间序列分解模型，本书不做介绍。# 6.5季节调整季节性调整 (seasonal adjustment) 是一种经济学上的数据处理技术用于消除某些变量在特定季节内的周期性波动。季节性调整的目的是将原始数据中的季节性因素剔除，从而更准确地了解某个经济指标的实际趋势。季节性调整通常应用于具有季节性波动的经济指标，例如销售额、就业率、消费水平等。于不同季节的天气节日、促销活动等因素都会影响这些指标的变化因此原始数据往往会出现季节性波动。季节性调整的方法通常是通过构建季节性模型来预测和剔除季节性波动常用的方法包括移动平均法、指数平滑法和回归分析等。调整后的数据更能反映出经济指标的实际趋势，有助于进行更准确的分析和决策。本节利用 scipy.

stats.

tsa.

seasonal_decompose 函数完成本章前文失业率数据的季节性调整。个函数同时支持加法模型

seasonal_decompose(series

model='add itive')

和乘法模型，seasonal_deco mpose(se ries

model='multi plicative')。本节采用的是默认的加法模型。图22所示为失业率数据的分解。图22 (a) 为原始数据图22 (b) 为趋势成分图22 (c) 为季节成分，图22 (d) 为噪音成分。注意，图22四副子图的纵轴尺度完全不同。2004 2008 2012 2016 2020Random Seasonal Trend Original

(b)(a)

(c)

(d)

图22.

失业率数据的分解

Page 17 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 图23、图24、图25三幅图分别展示这四种成分。scipy.

stats.

tsa.

seasonal_decompose 函数采用比较简单卷积方法进行季节调整对于更复杂的季节性调整，建议大家了解 X11模型。X11模型是一种用于季节性调整的统计方法它是 Census Bureau 在1967年开发的

ARIMA模型的一种扩展。X11模型能够预测和剔除原始数据中的季节性因素，从而更准确地反映某个经济指标的趋势。本书不展开讲解 X11模型。2004 2008 2012 2016 2020Trend14

图23.

比较原始数据和趋势成分

2004 2008 2012 2016 2020 0.

4 0.

3 0.

2 0.

3Seasonal

图24.

季节成分

Page 18 | Chapter 6时间数据 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGing er

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

2004 2008 2012 2016 2020 20246Irregular

图25.

噪音成分

Bk6_Ch06_ 03.

py绘制本节图像。时间序列是一种按时间顺序排列的数据序列，用于描述某个现象、变量或指标随时间变化的时间序列常用于经济学、金融学、气象学、医学等领域，例如股票价格、气温、血压等指时间序列中可能存在缺失值和离群值，这些异常值可能会影响时间序列分析的准确性。缺失值的方法包括插值法、回归法、拉格朗日插值法等。处理离群值的方法包括删除、替换、缩尾等，具体选择哪种方法需要根据实际情况来确定。时间序列分解是一种将时间序列分解为趋势项季节项、循环项随机项等等成分方法。节调整是时间序列分析的一种重要应用用于消除时间序列中的季节性因素以便更好地分析序列的趋势和周期性。时间序列分析是一种非常重要的统计方法，可以帮助我们了解和预测经济、自然和社会现象的趋势和变化规律，对于决策和规划具有重要意义。Page 1 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 7 Rolling Window

移动窗口移动窗口展示数据之间动态关系没有一种语言比数学更普遍更简单、更没有错误更不晦涩……更容易表达所有自然事物的不变关系。它用同一种语言解释所有现象，仿佛要证明宇宙计划的统一性和简单性，并使主导所有自然原因的不变秩序更加明显。There cannot be a language more universal and more simple

more free from errors and

obscurities.

more worthy to express the invariable relations of all natural th ings than mat hematics .

interprets all phenomena by the same language

as if to attes t the unity and simplicity of the plan of the

universe

and to make still more evident that unchangeable order which presides over all natural

causes .

—— 约瑟夫·傅里叶 (Joseph Fouri er) | 法国数学家物理学家 | 1768 ~ 1830

◄ df.

ewm .

mean 计算数据帧 df EWMA 平均值

◄ df.

ewm .

std 计算数据帧 df EWMA 标准差/波动率

◄ df.

rolling .

corr 计算数据帧 df的移动相关性

◄ df.

rolling .

kurt 计算数据帧 df滚动峰度

◄ df.

rolling .

max 计算数据帧 df滚动最大值

◄ df.

rolling .

mean 计算数据帧 df滚动均值

◄ df.

rolling .

min 计算数据帧 df滚动最小值

◄ df.

rolling .

quantile 计算数据帧 df滚动百分位值

◄ df.

rolling .

skew 计算数据帧 df滚动偏度

◄ df.

rolling .

std 计算数据帧 df MA平均值

◄ statsmodels.

regression.

rolling.

RollingOLS 计算移动OLS线性回归系数

Page 2 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

简单移动平均简单移动波动率回望窗口长度加权移动平均衰减系数半衰期移动窗口线性相关系数回归系数

Page 3 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 7.

1移动窗口移动窗口 (rolling window

moving window ) 是一种重要的时间序列统计计算方法。移动窗口按照一定规律沿着历史数据移动每一个位置都产生一个统计量比如最大值、最小值平均值、加权平均值、标准差等等。移动窗口方法可以消除时间序列中的随机噪声，减少数据波动，更好地反映数据的趋势和周期性。随着移动窗口不断滚动，特定统计量不断产生；因此，通过移动窗口得到的数据是序列数据，也就是时间序列。移动窗口的宽度叫做回望窗口长度 (lookback window length)。# Historical data

Lookback window

Rolling

图1.

移动窗口

Historical data

图2.

移动窗口不断移动产生新的时间序列最大、最小如图3所示利用长度为100营业日的回望窗口我们可以得到移动最大值 (橙色 ) 和移动最小值 (绿色 ) 曲线。随着移动窗口移动到每一个位置，便利用回望窗口内的数据产生一个最大值和最小值。当移动窗口最左端和历史数据的最左端对齐时，产生第一个数据；而这个数据位于移动

Page 4 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 窗口的最右端。因此，移动窗口数据长度比历史数据长度短。对于某个数据帧数据 df，移动最大值和最小值时间序列可以利用 df.

rolling .

max 和df.

rolling .

min 两个函数计算得到。# Price

Max, 100

Min, 100Price level4500

图3.

移动最大和最小，回望窗口长度为100

简单移动平均简单移动平均数 (simple moving average

SMA)，是时间序列分析中常用的一种方法滑时间序列数据。SMA的计算方法是将某一时间段内的数据求平均值，然后移动到下一个时间段内，继续计算平均值，如此重复直到计算完整个时间序列。SMA具体运算如下：1 2 2 1

SMA_

1 2 2 1

k L k L k k k

k

k L k L k k k

kL

iL

ix x x x xxL

x x x x x

LxL− + − + − −

−+

+− + − −

−

=++=

++=+ + +

+

=++

 (1)

SMA有助于消除短期波动带来的数据噪音，突出长期趋势。移动平均相当于一个滤波器；望窗口长度影响着统计量数据平滑度。SMA的计算过程中，每个数据点的权重相等，因此对于较短的时间段，SMA能够更好地反映数据的短期趋势和波动性但对于长期趋势和周期性较弱的数据，则可能不太准确。图5比较回望窗口分别为50、100和150三种情况的移动平均值。可以发现，回望窗口越长，得到的统计量时间序列看起来越平滑。Page 5 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 对于数据帧数据 df，移动平均可以用 df.

rol ling .

mean 计算得到。对于采样频率为营业日的数据，常见的移动窗口回望长度可以是5天 (一周 )

10天 (两周 )

20天 (一个月 )

60天 (一个季度)、125/126天 (半年 ) 或250/252天 (一年 ) 等等。# L data points

in lookback window

t = k L + 1 t = k t = T t = 0

图4.

回望窗口内数据序号

Price

Mean, 50

Mean, 100

Mean, 150Price level4500

图5.

移动平均，不同窗口长度其他统计量此外，移动窗口还可以帮助我们理解数据统计特点的动态特征。图6所示为日收益率的移动期望、波动率、偏度和峰态。波动率 (volatility) 就是标准差。可以发现数据的统计特征随着时间移动不断改变。对于数据帧数据 df，df.

rolling .

std、df.

rolling .

skew 和df.

rolling .

kurt 可以分别计算滚动标准差、偏度和峰度。Page 6 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 请大家改变回望窗口长度比较结果。1Return

005Mean

0000.

025Volatility Skew Kurtosis0.

图6.

日收益率的移动期望、波动率 (标准差 )、偏度和峰态类似地，图7所示为日收益率的95%和5%移动百分位变化。对于数据帧数据 df，rolling .

quantile 计算滚动百分位值。10Daily log return95% percentile

5% percentile

图7.

移动百分位，95%和5%

Page 7 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 7.

2移动波动率回望窗口长度为 L的条件下，时间序列移动波动率为：daily_

1kiL

kL

ixL 

=+−−−= (2)

其中，µ为回望窗口内数据 xi的平均值。时间序列波动率的大小可以反映时间序列数据的风险程度，即数据变化的不确定性程度。通常情况下，波动率越大，数据变化的不确定性越高，风险也就越大。在金融市场分析中，时间序列波动率被广泛应用于风险管理和投资决策。例如，股票的波动率可以帮助投资者评估其风险水平，从而做出更明智的投资决策。当L足够大，且µ几乎为0时，(2) 可以简化为：(

da ly)

iL

kL i

ix

L+−

== (3)

(3) 相当于对回望窗口内 (xi)2数据，施加完全相同的权重1/L；因此，这种波动率也被叫做移动平均波动率 (moving average volatility)。# Historical data

Lookback window

RollingEqually weightedWeight

图8.

移动平均

(3) 常用来计算股票收益率的波动率。图10所示为不同窗口长度条件下得到的移动平均波动可以发现，窗口长度越长数据越平缓，但是对数据变化响应越缓慢。白话说，回望窗口长度越长窗口内相对更具影响力的 “陈旧”数据越尾大不掉代谢的周期下一节介绍的指数加权移动平均 EWMA，便很好地解决这一问题；哪怕回望窗口越长，EWMA计算得到的波动率也能更快地跟踪数据变化规律。Page 8 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

图9.

尾大不掉的 “陈旧”数据

Window = 50

Window = 100

Window = 250MA volatility0.

010.

020.

030.

04Daily return squared0.

0000.

0050.

0100.

图10.

移动平均 MA单日波动率，不同窗口长度此外，±2σ波动率带常用来检测时间数据中可能存在的异常值。+2σ曲线被称之为 +2σ上轨，−2σ曲线常被称之为 −2σ下轨。图11~图13分别展示窗口长度为50天、100天和250天的 ±2σ移动平均 MA波动率带宽。Page 9 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

050.

000.

050.

10Daily log return

图11.

±2σ移动平均 MA波动率带宽，窗口长度50天

050.

000.

050.

10Daily log return

图12.

±2σ移动平均 MA波动率带宽，窗口长度100天

050.

000.

050.

10Daily log return

图13.

±2σ移动平均 MA波动率带宽，窗口长度250天

Page 10 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

时间平方根法则时间平方根法则 (square root of time) 可以将日波动率转化为年化波动率

annual daily 250= (4)

式中的250代表假设一年有250营业日。图14所示为不同窗口长度条件下，移动平均 MV年化波动率随时间变化情况。Window = 50

Window = 100

Window = 250MA annualized volatility

图14.

移动平均 MV年化波动率百分数，不同窗口长度

Bk6_Ch07_0 1.

py绘制上一节和本节主要图像。# 7.3指数加权移动平均指数加权移动平均 (exponentially -weighted moving average

EWMA ) 可以用来计算平均值准差、方差、协方差和相关性等等。EWMA是对前文的简单移动平均的改进。EWMA方法的特点是，对窗口内越近期的数据给予更高权重，越陈旧数据越低权重。权重的衰减过程为指数衰这种方法可以在平滑数据的同时保留较新数据的影响。指数加权移动平均数 (exponential moving av erage

EMA, or exponentially w eighte d moving

average ) 定义为：Page 11 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

1 2 22

EWMA2

_10.

1k L k L k kL

kL

Lk x x x x xxL    

+−−

− + − − −++ + + + −

−=

 (5)

其中，λ为衰减系数 (deca y factor)。# L data points

in lookback window

t = k L + 1 t = k t = T t = 0Exponentially weightedWeight

图15.

回望窗口内数据指数加权移动平均图16所示为 EWMA权重随衰减系数变化。EWMA weight0.

1 5 10 15 20

Lag day, iλ = 0.

λ = 0.

λ = 0.

λ = 0.

λ = 0.

图16.

EWMA权重随衰减系数变化

EWMA中半衰期 (half lif e

HL ) 指的是权重衰减一半的时间具体定义如下

ln 1 2 1

2 lnHLHL =  = (6)

图17所示为半衰期 HL随衰减系数 λ变化。Page 12 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Decay factor, λ 0.

90 0.

92 0.

94 0.

96 0.

98Half life70

图17.

半衰期随衰减系数变化

Bk6_Ch07 _02.

py绘制图16和图17。图18所示为衰减因子不同条件下，EWMA平均值变化情况。对比三条曲线，不难发现衰减系数 λ

越小 (比如红线 )

EWMA平均值更贴近真实趋势 (蓝线 )

但是平滑度降低。# Price level4500

2500λ = 0.

λ = 0.

λ = 0.

图18.

指数加权移动平均给定数据帧数据 df，df.

ewm .

mean 可以用来计算指数加权移动平均。这个函数可以还是使用平滑系数 α。衰减因子 λ与平滑系数α有关系如下：1=− (7)

Page 13 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 容易得到 α和半衰期 HL关系：ln 0.

51 expHL=−

 (8)

# 7.4 EWMA 波动率用EWMA方法计算波动率时，常使用如下迭代公式：2 2 2

11+1n n n r   −−=− (9)

其中，λ 为衰减因子 (decay factor )；σn 是当前时刻的波动率；σn-1是上一时刻的波动率；rn-1是上一时刻的回报率。如下所示，列出四个时间点 n

n − 1、n − 2和n – 3的EWMA波动率计算式

2 2 2

2 2 2

1 2 2

2 2 2

2 3 3

2 2 2

3 4 4+1

+1

+1

+1n n n

n n n

n n n

n n nr

r

r

r  

  

  

  −−

− − −

− − −

− − −=−



=−

=−

=− (10)

将 (10) 几个算式依次迭代，可以得到：2 2 2 2 2 3 2 4 2

1 2 3 4 4 1n n n n n n r r r r       − − − − − = − + + + + (11)

Historical data

Lookback window

RollingExponentially weightedWeight

图19.

指数加权移动平均计算波动率图20所示为不同衰减因子条件下 EWMA单日波动率。相比 MA方法，EWMA可以更快跟踪数据变化。衰减因子越小，跟踪速度越快。Page 14 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

EWMA volatility0.

010.

020.

030.

040.

05Daily return squared0.

0000.

0050.

0100.

λ = 0.

λ = 0.

λ = 0.

图20.

EWMA单日波动率，不同衰减因子图21~图23分别展示衰减因子为0.

99、0.

975和0.

94的±2σ移动平均 MA波动率带宽。# Daily log return

# 0.10 0.050.000.050.10

图21.

±2σ EWMA波动率带宽，λ = 0.

Page 15 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Daily log return

# 0.10 0.050.000.050.10

图22.

±2σ EWMA波动率带宽，λ = 0.

Daily log return

# 0.10 0.050.000.050.10

图23.

±2σ EWMA波动率带宽，λ = 0.

时间平方根法则将EWMA日波动率得到年化波动率。图24比较六个年化波动率。Page 16 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Annualized volatility, %

020406080 MA, 50

EWMA, λ = 0.

94EWMA, λ = 0.

975EWMA, λ = 0.

99MA, 100

MA, 250

图24.

比较6个年化波动率

# 7.5相关性系数除了平均值、波动率等，相关性系数也随着时间不断变化。rolling .

corr 可以计算数据帧

df的移动相关性。图25所示为移动相关性系数。在处理数据时，但凡发现移动相关性系数发生剧烈波动时，都需要大家格外小心。因为移动相关性系数的陡然增大、降低，都可能是由为数不多的几个数据点造成的。而这几个数据点有可能是离群值，值得我们深入探究。2016 2017 2018 2019 2020 20210.6

1Rolling correlation

图25.

移动相关性

Bk6_Ch07_03.

py 绘制图25。Page 17 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

7 .6回归系数类似地，回归系数也随着移动窗口数据不断变化。图26和图27用statsmodels.

regression.

rollin g.

RollingOLS 计算移动 OLS线性回归系数。0Slope, b1Upper CI

Lower CI

图26.

回归斜率系数，移动窗口长度100

# 0.01 0.000.010.02Intercept, b0

Lower CIUpper CI

图27.

回归截距系数，移动窗口长度100

Page 18 | Chapter 7移动窗口 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com /Visualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibil i.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Bk6_Ch07_04.

py 绘制图26和图27。总结来说，时间序列分析中移动窗口是一种常用的技术用于对时间序列数据进行平滑处理和预测分析。通过在时间序列上滑动固定大小的窗口，计算每个窗口中数据点的平均值或加权平均值来平滑数据。简单移动平均法 SMA是最基本的移动窗口方法，它将窗口内的数据点简单平均处理，对于时间序列的短期波动有较好的平滑效果。移动波动率是指在移动窗口内计算的标准差或方差，它通常用于评估时间序列的波动性。指数加权移动平均法 EWMA是一种加权移动平均方法，它通过指数函数来计算每个数据点的权重使得较近期的数据点的权重更大好地捕捉跟踪到时间序列变化趋势。此外，相关性系数、线性回归系数也都随时间 (移动窗口变

Page 1 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 8 Fundamentals of Stochastic Processes

随机过程入门一连串随机事件动态关系的定量描述不断重复地观察这些运动给我极大的满足；它们并非来自水流，也不是源于水的蒸发，这些运动的源头是颗粒自发的行为。These motions were suc h as to satisfy me

after frequently repeated obs ervation

that they arose neither

from currents in the fluid

nor from its gradual evaporation

but belonged to the p article itself.

—— 罗伯特·布朗 (Robert Brown ) | 英国植物学家 | 1773 ~ 1 858

◄ matplotlib.

patches.

Circle 绘制正圆

◄ np.

random.

normal 产生服从正态分布随机数

◄ numpy.

cumsum 累加

◄ numpy.

flipud 上下翻转矩阵

◄ seaborn.

distplot 绘制频率直方图和 KDE曲线

Page 2 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

离散形式几何布朗运动股价模拟具有一定相关性股价模拟随机过程入门维纳过程布朗运动无漂移漂移具有一定相关性

Page 3 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 8.

1布朗运动：来自花粉颗粒无规则运动

1827年，英国著名植物学家罗伯特·布朗通过显微镜观察悬浮于水中的花粉发现花粉颗粒迸裂出的微粒呈现出不规则的运动后人称之为布朗运动 (Brownian mo tion)。这里一个有趣的细节是，实际上花粉自身在水中并没有呈现出布朗运动，而是其崩裂出的微粒。爱因斯坦在1905年第一个解释布朗运动现象。图1.

平面上的随机运动罗伯特 ·布朗 (Robert Brown)

英国植物学家 | 1773 ~ 1858

丛书关键词：随机布朗运动几何布朗运动蒙特卡罗模拟布朗运动定义如果一个过程满足如下性质则称 X(t) 为布朗运动 (Browni an motion )。过程初始值为0：00X= (1)

X(t) 几乎处处连续。布朗运动是一种连续时间的运动，其轨迹是连续的，并且其微小变化是连续的。X(t) 布朗运动的增量是相互独立的，并且服从正态分布。对于所有0 ≤ s < t，2~ 0, XX Nt ts s −− (2)

对于 t > 0，X(t) 是均值为0，方差为σ2t的正态随机变量。也就是说，X(t) 的密度函数为：Page 4 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

221 2x

2epXtxfxt t −=

 (3)

注意，布朗运动在时间上是平稳的，即均值和方差不随时间的推移而改变。此外，布朗运动的变化是由随机因素驱动的，因此变化不可预测。维纳过程特别地，如果σ = 1

这个过程被称作标准布朗运动过程 (standard Brownian motion pr ocess )

也叫做维纳过程，本章用大写 B表示。维纳过程 (Wiener process ) 得名于诺伯特·维纳 (Norbert

Wiener )。诺伯特 ·维纳 (Norbert Wiener)

美国数学家 | 1894 ~ 1964

丛书关键词：维纳过程蒙特卡罗模拟假设 t = 0时，B(0) = 0，微粒位置在原点处。在t时刻，如果 x为微粒所在位置，对应的概率密度为：x1 2ep

2Btxfxt t−=

 (4)

B(t) 也可以描述为：0, B t N t

(5)

这说明 B(t) 服从均值为0、方差为 t的正态分布。图2所示为标准差随 t变化。Page 5 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

1 5 10 15 201.02.03.04.0

tStandard deviation

图2.

维纳过程标准差随时间 t变化图3所示为 (4) 所示概率密度随 x

t变化曲面，图中仅仅保留曲线随位置 x变化曲线。样理解图3中的曲线，随着时间不断推移，微粒的运动范围不断扩大。也就是说，随着t增大，微粒出现在远离原点的 “偏远”位置的可能性增大。注意，图3的纵轴是概率密度，不是概率值；但是，概率密度也代表可能性。如果把视角换成时间 t，我们得到图4。原点是微粒出发的位置，我们发现随着 t增大，概率密度值不断减小。这说明微粒位于原点及其附近的可能性随着 t增大而减小。而远离原点的位置，微粒出现的可能性却随着时间 t增大而增大。介于其间的位置，概率密度先增大后减小，可以用“涟漪”形容这种现象，微粒从原点汹涌而至，而又倏忽散去，雨散云飞。图5所示为维纳过程概率密度随x、t变化等高线。由于维纳过程概率密度函数期望值为0，大家可以发现当 t为定值时，概率密度的最大值出现在 x = 0处。这就是为什么图5 (b) 的平面等高线关于 x = 0对称。10 5 0 5 10

xPDF

x0510

1051015200.

1PDF

t(a) (b)

Page 6 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图3.

维纳过程概率密度曲线随 x变化，t快照

x0510

1051015200.

1PDF

t10 15 200.

3PDF

t(a) (b)

图4.

维纳过程概率密度曲线随 t变化，x快照

x0510

1051015200.

1PDF

t

10 5 0 5 10

x5101520

tx = 0(a) (b)

图5.

维纳过程概率密度随x、t变化等高线

Bk6_Ch08 _01.

py绘制图2。请大家自行绘制本节其他图像。# 8.2无漂移布朗运动一维

Page 7 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 无漂移布朗运动 (zero -drift Brownian motion) 和标准布朗运动的关系为

X t B t= (6)

上式相当于漂移项为0。漂移项通常是指趋势项，即随机过程的长期趋势。在无漂移布朗运动中，随机游走的漂移项为0，因此其表现为在一条平均线附近上下波动。ΔX为X在小段时间Δt内位置变化：Xt =  (7)

其中，随机数ε服从标准正态分布 N(0, 1)，这说明

20, X t N t 

xX(t0) = 0

1 tX(t1)

2 tX(t2) X(t3)

3 t

4 t

X(t4)

5 tX(t5)

图6.

某个微粒的一维无漂移布朗运动在t0 = 0时刻，微粒的位移 X(t0) = 0。如图6所示，tn时刻，微粒的位移为 X(tn) 可以写成一系列微小移动之和：0 1 2 1

n n n

nn

n n n

nn

in

i

iX t X t X t

X t t

X t t t

X t t t t t

t

   

      

−−

−

−−

−

=

== +

= + 

= +  + 

+  +  + +  + 

= (8)

1 nnt t t−  = −。图7给出的是100个微粒的的200步无漂移布朗运动轨迹。这就好比在 t = 0时刻，在数轴原点同时释放100个微粒，让它做沿着 x轴无漂移布朗运动。图7右侧直方图为 t = 200时刻，微粒在x轴上所处位置的分布。同时图7也绘制出

t 和

2t 这四条曲线。图7就可以用《统计至简》第9章讲过的68-95-99.

7法则，请大家思考。Page 8 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0x

0 50 100 150 200

t(n)0.

00 0.

01 0.

02 0.

Probability density

图7.

100个微粒一维无漂移布朗运动轨迹和运动范围图7的每一个微粒随机漫步的路径，都是不同的。换句话说，任意两个微粒的运动轨迹相同的概率几乎为零。图8所示为微粒在不同 t在x轴上分布的快照图中我们也可以看到68-95-99.

7法则。50 50 0 50 50 0 50 50 0 50 50 0 50 50 00.08

020.

00(a) n = 40 (b) n = 80 (c) n = 120 (d) n = 160 (e) n = 200Probability density

X(t40) X(t80) X(t120) X(t160) X(t200)

图8.

100个微粒无漂移布朗运动轨迹在不同时刻位置分布的快照

Bk6_Ch08 _02.

py绘制图7和图8。二维在二维平面里，微粒的随机漫步更像布朗运动中炸裂的花粉颗粒一样。在tn时刻，X(tn) 为微粒的横坐标值，Y(tn) 为微粒的纵坐标值：Page 9 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

1in

ni

i

jn

nj

jX t t

Y t t

=

=

=

==

=

 (9)

图9所示为某个微粒从原点出发完全的二维无漂移布朗运动运动过程显得 “浑浑噩噩 ”

无可恋”。图9.

平面二维无漂移随机漫步

Bk6_Ch08 _03.

p y绘制图9。# 8.3漂移布朗运动：确定 + 随机前面介绍了零漂移布朗运动，微粒的运动只具有随机成分，而没有确定成分。如果在零漂移布朗运动基础上引入确定成分我们便得到漂移布朗运动 (Browni an motion with dr ift)

DriftRandomX t t B t=+

(10)

其中，µ 为漂移率，σ 为标准差。2, X t N t t 

如果把上式看做是物体直线运动的话

µt相当于是匀速运动部分也就是漂移，确定的成如图10所示，漂移率 µ可以为正，可以为负，当然也可以为0 (无漂移 )。σB(t) 相当于随机漫步，可以理解为噪音，即随机成分，代表不确定性。打个比方，µt就是浩浩汤汤的历史进程，大势所趋。σB(t) 就是时时刻刻的生活细节，琐碎

Page 10 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

t

t

t

t

ttµtσB(t)

µt + σB(t)

µtσB(t)

µt + σB(t)

图10.

解构定向漂移布朗运动图11所示为漂移布朗运动概率密度随 x、t变化曲面。类似图3，图11中仅仅保留曲线随位置 x

变化曲线。类似无漂移布朗运动随着时间不断推移漂移布朗运动微粒的运动范围不断扩大。同时，我们能够看到概率密度的对称轴随着时间增大而移动。图12所示为含漂移布朗运动概率密度曲线随 t变化，在不同 x点上的快照。图13所示为含漂移布朗运动概率密度随x

t变化等高线图中能够明显地看到 (10) 漂移项。x0510

1051015200.

1PDF

tPDF

10 5 0 5 10

x(a) (b)

图11.

漂移布朗运动概率密度曲线随 x变化，t快照

Page 11 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

x0510

1051015200.

1PDF

t 5

t10 15 200.

3PDF(a) (b)

图12.

含漂移布朗运动概率密度曲线随 t变化，x快照

x0510

1051015200.

1PDF

t

10 5 0 5 10

x5101520

tx = 0(a) (b)

图13.

含漂移布朗过程概率密度随x、t变化等高线离散形式为了方便蒙特卡洛模拟，我们也需要得到含漂移布朗过程的离散形式。首先，写出 (10) 的微分形式：d d dX t t B t=+ (11)

这样，(10) 的离散化形式可以写成：X t t t   =  +   (12)

然后，把上式写成累加形式：Page 12 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

1in

ni

iX t n t t  =

==   +   (13)

图14给出的是100个微粒的的200步含漂移布朗运动轨迹。能够明显地看到运动轨迹 “整体”

表现出“向上”的运动趋势，这来自于定向漂移成分 µt。此外，这些轨迹在时间 t处的期望值就是

t

图14右侧直方图为 t = 200时刻，微粒在x轴上所处位置的分布。图7也绘制出

tt 和

2tt 这四条曲线。图15所示为微粒在不同 t在x轴上分布的快照，图中我们也可以看到68-95-99.

7法则。0 50 100 150 200

t(n)0.

00 0.

01 0.

02 0.

Probability density80

20x

图14.

100个微粒一维含漂移布朗运动轨迹和运动范围

0 40 80 0 40 80 0 40 80 0 40 80 0 40 80

X(t40) X(t80) X(t120) X(t160) X(t200)0.

020.

00Probability density(a) n = 40 (b) n = 80 (c) n = 120 (d) n = 160 (e) n = 200

图15.

100个微粒含漂移布朗运动轨迹在不同时刻位置分布的快照

Bk6_Ch08 _04.

py绘制图14和图15。Page 13 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

8.4具有一定相关性布朗运动本节介绍如何据此产生满足一定相关性的布朗运动。《统计至简》第15章介绍如何产生具有一定相关性的随机数，请大家回顾。如图16所示，给定固定时间间隔

t，tX 为在

t满足一定相关性布朗运动分步步长构成的矩阵为：Et t t =  + X X ZR (14)

也就是说，E, t N t tXX Σ

而是 R是Σ的Cholesky分解的三角矩阵。图16中，矩阵

Z为随机数矩阵，服从 N(0, I)。图17、图18所示为具有正相关的两条漂移布朗运动蒙特卡洛模拟结果。图19、图20所示为具有负相关的两条漂移布朗运动蒙特卡洛模拟结果。Z R @ = ΔX

L × nn × n

L × nE(X)Δt +

t

图16.

计算具有一定相关性布朗运动矩阵运算

Page 14 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

2 0 2

ΔX14

4ΔX2

图17.

分步步长的散点图，ρ = 0.

0X1

X2 204060

0 50 100 150 200

n

图18.

两条具有正相关关系的行走轨迹，ρ = 0.

Page 15 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

2 0 2

ΔX14

4ΔX2

图19.

分步步长的散点图，ρ = −0.

0 50 100 150 200

n0204060

X1

X2

图20.

两条具有正相关关系的行走轨迹，ρ = −0.

Bk6_Ch08 _05.

py绘制图17 ~ 图20。# 8.5几何布朗运动满足下式的随机微分方程的过程被称作几何布朗运动 (Geometric Brownian motion

G BM)：d d dX t X t t X t B t=+ (15)

Page 16 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 其中，X(t) > 0。上式也可以写成：dddXtt B tXt=+ (16)

利用伊藤引理 (Ito's Lemma )，求解得到 X(t)：0 exp2X t X t B t= − +  (17)

伊藤引理是随机微积分的重要定理之一，用于计算随机过程的微分。简单来说，伊藤引理是泰勒展开在随机微积分中的应用它是通过将泰勒展开的思想推广到随机微积分中得到了一般的随机微分方程的解析式。泰勒展开是将一个函数展开成一个多项式的形式，而伊藤引理是将一个随机过程展开成一个多项式 (一般为二阶 ) 加一个随机项的形式。《数学要素》第17章介绍过泰勒展开，请大家回顾。X(t) 的期望值为：E 0 expX t X t  = (18)

X(t) 的方差：2 2var 0 exp 2 exp 1X t X t t  =− (19)

X(t) 的标准差为：2std 0 exp exp 1X t X t t  =− (20)

对X(t) 求对数得到：2ln ln 0 exp2

ln 02X t X t B t

X t B t

 = − +  

= + − +  (21)

可以发现 lnX(t) 为布朗运动也就是说 lnX(t) 的概率密度服从高斯分布。离散形式

(21) 的离散形式为：ln ln2X t t X t t t + − = −  +   (22)

Page 17 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 有了上式，我们就可以进行蒙特卡洛模拟。图21所示为100个微粒几何布朗运动轨迹。22所示为微粒在不同时刻位置分布的快照。0 50 100 150 200

t(n)0.

00 0.

01 0.

02 0.

Probability density 2050

0100150200

x

图21.

100个微粒几何布朗运动轨迹

0 100 200 0 100 200 0 100 200 0 100 200 0 100 200

X(t40) X(t80) X(t120) X(t160) X(t200)0.

000.

040.

08Probability density(a) n = 40 (b) n = 80 (c) n = 120 (d) n = 160 (e) n = 200

图22.

100个微粒几何布朗运动轨迹在不同时刻位置分布的快照

Bk6_Ch08 _06.

py绘制图21和图22。模拟股票股价走势实践中，几何布朗运动常用来模拟股票股价走势。如图23所示，长期观察股票股价，可以发现走势，而且股价不能为负值。更重要的是，股价对数收益率分布可以用高斯分布来描述。Page 18 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Compute returns

图23.

某只股价走势、收益率

# 8.6股价模拟

S0为初始股价，经过一小段时间 Δt，股价变化 ΔS：0exp2S S t t  = −  +   (23)

µ 收益率期望值，σ为收益率波动率，ε 随机数服从标准正态分布。图24总结整个蒙特卡洛模拟股价走势过程。历史数据用来校准模型。图25所示为 S&P 500指数在一段时间内的走势。图26所示为其日对数回报率。图27给出日对数回报率的分布情况，我们可以计算得到均值和方差，这些参数可以用来校准模型。图28所示为蒙特卡洛模拟结果。这种方法缺陷很明显，历史数据未必能够代表未来趋势。此外，由于假设回报率服从正态分布，没有考虑到 “厚尾”问题，也就是所谓的 “黑天鹅”问题。# Historical dataCalibrate parameters

Monte Carlo simulationProjection

S0

图24.

基于历史数据估计参数，和蒙特卡洛模拟预测未来股价可能走势

Page 19 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

2500Adjusted closing price

图25.

S&P 500价格水平数据

10Daily return

图26.

S&P 500日对数回报率

µdaily = 0.

σdaily = 0.

# 00.05 0.00 0.05 0.10

Daily returnFrequency

100200300400

图27.

S&P 500日对数回报率分布

Page 20 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Simulation horizon (days)6000

30000 10 20 30 40 506000

# 30000.0000 0.0005 0.0010

PDF

图28.

S&P 50 0蒙特卡洛模拟此外，图29所示的二叉树也可以用来模拟股票股价，本书不做展开。图29.

二叉树随机路径模拟股票股价

Bk6_Ch08 _07.

py绘制图25 ~ 图28。# 8.7相关股价模拟当时间戳为列方向时，下式为几何布朗过程计算对数回报率矩阵 X矩阵运算式：Page 21 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Tdiag

2tt

= −  + Σ

Xμ ZR

图30所示为上式矩阵运算过程。μ为股价年化期望收益率行向量。Σ为化方差协方差矩阵。是由随机数发生器产生的服从标准正态分布的线性无关随机数

Z为列方向数据矩阵每列代表一个变量；上三角矩阵 R来自 Chol esky分解Σ得到。Δt设定为1/252。Z R × = X

n × DD × D

n × Dμ

+Σ

Tdiag

2Σ

× Δt

×sqrt(Δt)chol D × D

图30.

几何布朗过程离散式的矩阵运算过程，列方向矩阵模拟多路径相关股价走势具体矩阵运算过程如图31所示其中矩阵 Z和矩阵 X的形状为 n ×

D × npaths。npaths为蒙特卡罗模拟轨迹的数量。Page 22 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Z R × = X

n × D × npathsD × Dμ

+Σ

Tdiag

2Σ

× Δt

×sqrt(Δt)chol

n × D × npathsD × D

Number of paths Number of paths

图31.

几何布朗过程离散式的矩阵运算过程，多路径图32所示为几只股票真实股价和归一化股价走势图。图33所示为日收益率的协方差矩阵、相关性系数矩阵。图34所示为协方差矩阵的 Cholesky分解。图35所示为一组相关性股价的模拟。种模拟方法的显著缺点是 Cholesky分解当协方差矩阵过大 Cholesky分解可能会不稳定。只有正定矩阵才能 Cholesky分解。大家如果感兴趣可以搜索 Benson-Zangar i蒙特卡洛模拟，这种方法避免 Cholesky分解，本书不展开讲解。# TSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGL3.

0100020003000

图32.

几只股票走势和初值归一化股价

Page 23 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

TSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGL

TSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGL

TSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGLTSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGL

图33.

协方差矩阵和相关性系数矩阵热图

Σ L R = @

图34.

对协方差矩阵进行 Cholesky分解

TSLA

TSM

COST

NVDA

FB

AMZN

AAPL

NFLX

GOOGLSimulated price level

图35.

一组蒙特卡罗模拟相关性股价结果

Page 24 | Chapter 8随机过程入门 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com /513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

随机是指在一定的概率分布下，不确定的事件或过程。随机过程是指随机变量随时间变化的布朗运动是一种最基本的连续时间随机过程，它是随机微积分的基础，因其随机性而具有广泛应用，如金融领域的股价预测、自然界中颗粒的扩散行为等。维纳过程也称标准布朗运动过几何布朗运动中，随机变量的对数服从布朗运动。在金融学中，股价往往被认为是一种几何布朗运动。本章介绍如何利用几何布朗运动单一模拟股价走势，以及具有特定相关性股价走势。Page 1 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 9 Regression Analysis

回归分析线性回归结果不能拿来就用真理太复杂了，除了近似，我们别无他法。Truth is much too complicated to allow anything but approximations.

—— 约翰·冯·诺伊曼 (John von Neumann) | 美国籍数学家 | 1903 ~ 1957

◄ scipy.

stats.

kurtosis 计算峰度

◄ scipy.

stats.

normaltest Omnibus 正态检验

◄ scipy.

stats.

ske w 计算偏度

◄ scipy.

stats.

ppf 求解t分布的逆累积分布函数

◄ scipy.

stats.

sf 求解t分布的互补累积分布函数 CCDF = 1 - CDF

◄ seaborn.

distplot 绘制直方图，叠合 KDE曲线

◄ seaborn.

pairplot 绘制成对分析图

◄ seaborn.

regplot 绘制回归图像

◄ statsmodels.

api.

add_constant 线性回归增加一列常数1

◄ statsmod els.

api.

OLS 最小二乘法函数

◄ statsmodels.

graphics.

tsaplots.

plot_acf 绘制自相关结果

◄ statsmodels.

stats.

anova.

anova_lm 获得ANOVA表格

Page 2 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

拟合优度修正决定系数区间置信区间预测区间信息准则 AIC

BIC决定系数三个平方和自由度

MSR，MSE

F检测方差分析SST

SSE

SSR

一元回归F检验统计量备择假设原假设临界值

t检验统计量备择假设原假设临界值

MLE：对数似然函数残差分析，自相关检测，条件数

Page 3 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 9.

1线性回归：一个表格、一条直线一个表格大家是否还记得我们在《统计力量》第24章结尾给出过图1这个表格。图1这个表格汇总某个线性回归分析的结果。本章的主要目的就是和大家理解这个表格各项数值的含义。下面首先介绍这个表格具体来自哪个线性回归。# OLS Regression Results

==============================================================================

Dep.

Variable: AAPL R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 549.

Date: XXXXXXXXXXX Prob (F-statistic): 4.

55e -65

Time: XXXXXXXXXXX Log-Likelihood: 678.

No. Observations: 252 AIC: -1352.

Df Residuals: 250 BIC: -1345.

Df Model: 1

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const 0.

0018 0.

001 1.

759 0.

080 -0.

000 0.

SP500 1.

1225 0.

048 23.

446 0.

000 1.

028 1.

==============================================================================

Omnibus: 52.

424 Durbin -Watson: 1.

Prob(Omnibus): 0.

000 Jarque -Bera (JB): 210.

Skew: 0.

777 Prob(JB): 1.

68e -46

Kurtosis: 7.

203 Cond.

No.6.

==============================================================================

图1.

一元线性回归结果一条直线图2所示为这个一元 OLS线性回归的自变量因变量散点数据以及分布特征。自变量为一段时间内标普500股票指数日收益率，因变量为某只特定股票的同期日收益率。观察散点图，我们可以发现明显的 “线性”关系。从金融角度，股指可以 “解释”同一个市场上股票的涨跌。图1是利用 statsm odels.

api .

OLS 函数构造的线性模型结果。再次强调，线性回归不代表 “因果关系 ”。Page 4 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

# 0.1 0.1 0.0

S&P 500 daily return, x 0.

0AAPL daily return, y

# 0.1 0.1 0.0

S&P 500 daily return, x 0.

0AAPL daily return, y(a) (b)

图2.

日收益率数据关系图3所示为用用seaborn.

joint plot 绘制回归图，并且绘制边际分布。# 0.1 0.1 0.0

S&P 500 daily log return, x 0.

0AAPL daily log return, y

图3.

用seaborn.

jointplot 绘制回归直线统计特征图4 (a) 所示为数据的协方差矩阵。Page 5 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.《统计至简》第12、24章介绍过如何从条件概率角度理解线性回归。假设 X和Y的均值为0，请大家根据这个协方差矩阵写出线性回归解析式。图4 (b) 所示为相关性系数矩阵热图。《矩阵力量》第23章介绍过相关性系数可以看成是 “标准差向量”之间夹角具体如图4

(c) 所示。θy,y = 0°θx,y = 34°

AAPL, yS&P 500, xAAPL, y S&P 500, x

θx,y = 34°θy,y = 0°ρy,y = 1ρx,y = 0.

AAPL, yS&P 500, xAAPL, y S&P 500, x

ρx,y = 0.

83ρx,x = 1var y,y =

00087cov x,y =

00053

AAPL, yS&P 500, xAAPL, y S&P 500, x

cov x,y =

00053var x,x =

00047(b) (c) (c)

图4.

[y, x] 数据的协方差矩阵、相关性和夹角热图图5所示为两个标准差向量的箭头图。夹角越小，说明因变量向量 y和自变量向量x越相也就是说，夹角越小，自变量向量 x能更充分解释因变量向量 y。本章后文还会利用这个几何视角解释回归分析结果。本章内容相对比较枯燥，建议大家主要理解 ANOVA。大家有实际需要时再回头查阅本章其余内容。σx = 0.

0217σx = 0.

0294

# 0.00 0.020.000.02

θx,y = 34°0.

图5.

标准差向量空间角度解释夹角

Page 6 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

Bk6_Ch 09_01.

py绘制本节图像。# 9.2方差分析 ANOVA

本节开始先介绍如何理解图6所示的 ANOVA 表格结果。ANOVA 的含义是方差分析 (Analysis

of Variance )。方差分析是一种用于确定线性回归模型中不同变量对目标变量解释程度的统计技方差分析通过比较模型中不同的变量的平均方差，来确定哪些变量对目标变量的解释程度更

ANOVA 是图1的重要组成部分之一。df sum_sq mean_sq F PR(>F)

x 1.

0 0.

149314 0.

149314 549.

729877 4.

547141e -65

Residual 250.

0 0.

067903 0.

000272 NaN NaN

图6.

一元线性回归 ANO VA表格，来自本书第6章表1所示为标准 ANOVA 表格对应的统计量。标准 ANOVA表格比图6多一行。表1有五列：第1列为计算方差的三个来源；第2列df代表自由度 (degree s of freedom)；自由度是指在计算统计量时可以随意变化的独立数据点的数量。第3列SS代表平方和 (Sum of Squares )；平方和通常用于描述数据的变异程度，即它们偏离平均值的程度。第4列MS代表均方和 (Mean Sum of Squares )；在统计学中，均方和是一种平均值的度量，其计算方法是将平方和除以自由度。第5列F代表F-test统计量。F检验是一种基于方差比较的统计检验方法，用于确定两个或多个样本之间是否存在显著性差异。表中 n代表参与回归的非 NaN样本数量。k代表回归模型参数数量，包括截距项。D代表因变量的数量，因此 k = D + 1 (+1代表常数项参数 )。下面将逐个解密表1中的每一个值的含义，以及它们和线性回归的关系。表1.

ANOVA 表格

Source df SS MS F Significance

Page 7 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com Regress or DFR = D = k − 1 SSR MSR = SSR/ DFR F = MSR/MSE p-value of F-test

Residu als DFE = n – D – 1 = n − k SSE MSE = SSE/DFE

Total DFT = n − 1 SST

三个平方和为了理解 ANOVA 表格，我们首先要了解三个平方和：◄ 总离差平方和 (Sum of Squares for T otal

SST)，也称 TSS (total sum o f squa res)。总离差平方和

SST描述所有观测值与总体均值之间差异的平方和，用来评整个数据集的离散程度。◄ 残差平方和 (Sum of Squares for Error

SS E)，也称 RSS (residual s um of squ ares)。残差平方和

SSE反映了因变量中无法通过自变量预测的部分也称为误差项可以用于检查回归模型的拟合程度和判断是否存在异常值。在回归分析中，常用通过最小化残差平方和来确定最佳的回归系数。◄ 回归平方和 (Sum of Squ ares for Reg ression

S SR)，也称 ESS (explained sum of s quares)。平方和 SSR反映了回归模型所解释的数据变异量的大小用于评估回归模型的拟合程度以及自变量对因变量的影响程度。图7给出计算三个平方和所需的数值。表2总结了三个平方和的定义。x

01ˆy b b x=+

,iixyi-th sample

Predicted

ˆiiyy−

iyy−

ix

iy

ˆiy

y

ˆiyy−

图7.

通过一元线性回归模型分解因变量的变化表2.

三个平方和的定义平方和定义图像

Page 8 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 总离差平方和

(Sum of Square s for T otal, S ST)

=1SST =n

i

iyy−

x

ix

iyy−

01ˆy b b x=+

回归平方和

(Sum of Squares for Reg ression, SS R)

1ˆ SSRn

i

iyy

==−

x

ix

ˆiyy−

01ˆy b b x=+

残差平方和

(Sum of Squares for Err or, SSE )

1ˆ SSEn

ii

iyy

==−

x

ˆiiyy−

ix

01ˆy b b x=+

等式关系对于线性回归来说方差分析实际上就是把SST分解成残差平方和 SSE

回归平方和 SSR

SST SSR SSE=+ (1)

2 2 2

=1 1 1

SST SSR SSEˆˆn n n

i i i i

i i iy y y y y y

==− = − + −  

(2)

上式的证明并不难本节不做展开讲解本章后续会用向量几何视角解释以上等式关系。章后续将介绍由这三个平方和引出的一些列有关回归的统计量特别是R-squared和Adj.

square d。# 9.3总离差平方和SST

总离差平方和 (Sum of Squares for T otal

SS T) 代表因变量 y所有样本点与期望值

y 的差异：=1SST =n

i

iyy− (3)

其中，期望值

y 为：Page 9 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

=11=n

i

iyyn (4)

如图8所示，SST可以看做一系列正方形面积之和。这些正方形的边长为

iyy−。图8中这些正方形的一条边都在期望值

y 这个高度上。01ˆy b b x=+

iyx

0b

y

iyy−

1SSTn

i

iyy

==−

图8.

总离差平方和 SST

总离差自由度DFT

总离差自由度 (degree of freedom total

DFT ) 的定义为

DFT 1 n=− (5)

n是样本数据的数量 (NaN除外)。三个自由度关系总离差自由度 DFT、回归自由度 DFR、残差自由度 DFE三者关系为：DFR DFR DFE DFEDFT 1 DFR DFE 1 1 n k n k D n D= − = + = − + − = + − −

(6)

k是回归模型的参数，其中包括截距项。1 kD=+ (7)

D为参与回归模型的特征数，也就是因变量的数量。举个例子，对于一元线性回归，D = 1，k = 2。如果参与建模的样本数据为 n = 252，几个自由度分别为：Page 10 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

DFT 252 1 251

DFR 1 1

DFE 1 252 2 250kD

kD

n k n D= − =

= + == − = =

= − = − − = − = (8)

平均总离差 MST

平均总离差 (mean s quare total, MST) 的定义为：1 SSTMST var1 DFTn

i

iyy

Yn=−

= = =− (9)

实际上，总离差 MST便是因变量Y样本数据方差。看到这里，大家应该理解为什么本章的内容叫“方差分析 ”了。# 9.4回归平方和 SSR

回归平方和 (Sum of Square s for Reg ression

SSR) 代表回归方程计算得到的预测值

ˆiy 和期望值

y

之间的差异：1ˆ SSRn

i

iyy

==− (10)

图9所示为回归平方和 SSR的几何意义。图9中的每个正方形边长为

ˆiyy−。注意，图中所有正方形的一个顶点都在回归直线上。01ˆy b b x=+x

0b

y

ˆiyy−

ˆiy

1ˆ SSRn

i

iyy

==−

Page 11 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 图9.

回归平方和回归自由度 DFR

回归自由度 (degrees of freedom for regression model

DFR) 为

DFR 1 kD= − = (11)

平均回归平方 MSR

平均回归平方 (mean square regressio n

MSR ) 为

SSR SSR SSRMSRDFR 1 kD= = =− (12)

# 9.5残差平方和 SSE

残差平方和 (Sum of Squa res fo r Error

S SE) 定义如下

11ˆ SSEnn

i i i

iiyy 

=== = − (13)

相信大家对残差平方和 SSE已经很熟悉。比如，在最小二乘法中，我们通过最小化残差平方和SSE优化回归参数。图10所示为残差平方和 SSE的示意图。图中每个正方形的边长为

ˆiiyy−。对于 OLS一元线性回归，我们期待图中蓝色正方形面积之和最小。01ˆy b b x=+

iy

ˆiyError

ˆi i iyy=−

x

0b

11ˆ SSEnn

i i i

iiyy 

=== = −

Page 12 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 图10.

残差平方和 SSE

残差自由度 DFE

残差自由度 (degrees of freedom for error

DFE) 为

DFE 1 n k n D= − = − − (14)

残差平均值 MSE

残差平均值 (mean squared error , MSE ) 为：SSE SSE SSEMSEDFE 1 n k n D= = =− − − (15)

均方根残差 RMSE

均方根残差 (Root mean square error

RMSE ) 为MSE的平方根

SSE SSE SSERMSE MSEDFE 1 n p n D= = = =− − − (16)

9.6几何视角：勾股定理大家别忘了《矩阵力量》反复提到的线性回归几何视角！一个直角三角形看到 (2) 中三个求和，我们下面用向量范数算式完成三个求和运算：=1

1SST

ˆ ˆ SSR

ˆ ˆ SSEn

i

i

n

i

i

n

ii

iy y y

y y y

yy=

== − = −

= − = −

= − = −



y1

y1

yy (17)

根据 (2)，我们可以得到如下等式：2 2 2

2 2 2

SST SSR SSEˆˆ yy− = − + −y 1 y 1 y y

(18)

Page 13 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 相信大家一眼就会看出来，(18) 代表着直角三角形勾股定理！如图11 (a) 所示，y−y1就是斜边对应的向量，斜边长度为

y−y1。ˆy−y1为第一条直角

ˆy−y1代表回归模型解释的部分。ˆ−yy为第二条直角边，代表残差项，也就是回归模型不能解释的部分。注意，图11中

y−y1和

ˆy−y1的起点为

y1的终点，这相当于去均值。如图11 (b) 所示，这个勾股定理还可以写成：2 2 2

SST SSR SSE=+ (19)

此外，请大家注意图中θ，θ是向量

y−y1和向量

ˆy−y1的夹角，下一节会用到它。θ θ

y−y1

ˆy−y1

ˆ=−ε y y

SST

SSE

SSR(a) (b)

图11.

几何角度看三个平方和四个直角三角形图11的直角三角形是图12这个四面体的一个面 (灰色底色 )。而图12这个四面体的四个面都是直角三角形！现在请大家自己试着理解这个四面体和四个直角三角形的含义下一章会深入分析。Page 14 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

Hyperplane spanned by column vectors of X ε = y ŷ y

HOrigin

θ

y−y1

ˆy−y1

y1

ˆy

图12.

四面体的四个面都是直角三角形

# 9.7拟合优度：评价拟合程度如图13所示，向量

y−y1和向量

ˆy−y1之间夹角θ越小，说明误差越小，代表拟合效果越

y−y1

y−y1

y−y1

y−y1

ˆy−y1

ˆy−y1

ˆy−y1

ˆy−y1

ˆ=−ε y y

ˆ=−ε y y

ˆ=−ε y y

ˆ=−ε y y

图13.

因变量向量和预测值向量夹角从大到小在回归模型创建之后很自然就要考虑这个模型是否能够很好地解释数据即考察这条回归线对观察值的拟合程度也就是所谓的拟合优度 (goodness of fit)。拟合优度是指一个统计模型与观测数据之间的拟合程度，即模型能够多好地解释数据。简单地说，拟合优度是回归分析中考察样本数据点对于回归线的贴合程度。决定系数 (coefficie nt of determ ination

R2) 是定量化反映模型拟合优度的统计量。从几何角度来看，R2是图12中θ余弦值 cosθ的平方：2 2cos R= (20)

利用图11 (b) 直角三角形三边之间的关系，R2可以整理为：Page 15 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

2SSR SSE=1SST SSTR=− (21)

当预测值越接近样本值，R2越接近1；相反，若拟合效果越差，R2越接近0。拟合优度可以帮助评估回归模型的可靠性和预测能力，并对模型进行改进和优化。一元线性回归特别地，对于一元线性回归决定系数是因变量与自变量的相关系数的平方与模型系数 b1

也有直接关系。,2 2 X

XY

YRb== 

 (22)

, 1Y

XY

Xb= (23)

也就是说，在一元线性回归中，R2的平方根等于线性相关系数的绝对值。也就是说，当 ρ等于1或−1时，R2为1，表示因变量完全由自变量解释；当 ρ等于0时，R2为0，表示自变量对因变量没有任何解释能力。因此，R2越接近1，表示自变量对因变量的解释能力越强，线性相关系数ρ的绝对值也越大，反之亦然。因此，线性相关系数 ρ和决定系数 R2都是衡量变量之间线性关系强弱的重要指标它们可以帮助我们理解自变量对因变量的解释能力评估模型的拟合优度以及选择最佳的回归模型。修正决定系数但是，仅仅使用 R2是不够的。对于多元线性模型，不断增加解释变量个数 D时，R2将不断我们可以利用修正决定系数 (adjusted R squared )。简单来说，修正决定系数考虑到自变量的数目对决定系数的影响，避免了当自变量数量增加时决定系数的人为提高。修正决定系数的具体定义为：adj

2MSE1MST

SSE1SST 1

1 SSE1SST

1 SSE11 SSTR

nk

n

n

nk

nRnk

n

nD=−

−=−−

−=−−

−= − −−

−=−−− (24)

Page 16 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 修正决定系数的作用在于当模型中自变量的数量增加时它能够惩罚过拟合 (overfitting)

并避免了决定系数因为自变量个数增加而提高的问题。因此，在比较不同模型的拟合优度时，使用修正决定系数会更加准确，能够更好地刻画模型的解释能力。过拟合是指一个模型在训练数据上表现良好，但在测试数据上表现较差的现象。在过拟合的情况下，模型过度地学习了训练数据的特征和噪声，导致其在测试数据上的预测能力下降。过拟合通常发生在模型复杂度过高或者训练数据太少的情况下。例如，在一元线性回归中，如果使用高次多项式来拟合数据，就容易出现过拟合的情况。在这种情况下，模型会过度拟合训练数据，导致其在新数据上的预测能力下降。为了避免过拟合，可以采取以下方法：增加训练数据量、降低模型复杂度、采用正则化

(regularization ) 技术等。本书第11章将讲解正则化回归。# 9.8 F检验：模型参数不全为0

在线性回归中，F检验用于检验线性回归模型是否显著。它通过比较回归平方和和残差平方和的大小来判断模型是否具有显著的解释能力。统计量

F检验的统计量为：# SSR

SSR MSR 1

SSE MSE SSE 1

SSR

SSR 11,SSE SSE

1nkkFk

nk

nDDF k n kD

nD−−= = =−

−

 − −= = − −

−−

(25)

原假设、备择假设假设检验 (hypothesis testing ) 是统计学中常用的一种方法用于根据样本数据推断总体参数是否符合某种假设。假设检验通常包括两个假设：原假设和备择假设。原假设 (null hypothesis ) 是指在实验或调查中假设成立的一个假设通常认为其成立。备择假设 (alternative hypothesis ) 是指当原假设不成立时我们希望成立的另一个假设。Page 17 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 通过收集样本数据并根据统计学原理计算出样本统计量的概率分布我们可以计算出拒绝原假设的概率。如果这个概率小于预设的显著性水平 (比如0.

05)，就可以拒绝原假设，认为备择假设成立。反之，如果这个概率大于预设的显著性水平，就不能拒绝原假设。F检验是单尾检验，原假设 H0、备择假设 H1分别为：0 1 2

: 0 for at least one D

jH b b b

H b j= = = =



(26)

具体来说，F检验的零假设是模型的所有回归系数都等于零，即自变量对因变量没有显著的如果 F检验的 p值小于设定的显著性水平就可以拒绝零假设认为模型是显著的变量对因变量有显著的影响。临界值

(25) 得到的 F值和临界值 Fα进行比较。临界值 Fα可根据两个自由度 (k − 1和 n − k) 以及置信水平α查表获得。1 − α 为置信度或置信水平，通常取α = 0.

05或α = 0.

这表明，当作出接受原假设的决定时，其正确的可能性为95%或99%。1 1, F F k n k− − − (27)

在该置信水平上拒绝零假设 H0

不认为自变量系数同时具备非显著性即所有系数不太可能同时为零。否则，接受 H0，自变量系数同时具有非显著性，即所有系数很可能同时为零。举个例子给定条件α = 0.

01，F1–α(1, 250) = 6.

7373。图6结果告诉我们，F = 549 .

7 > 6.

7373，表明可以显著地拒绝H0。也可以用图6中p值，-value P 1,p F F k n k=  − − (28)

如果 p值小于α，则可以拒绝零假设 H0。Bk6_Ch09_02.

py计算图6所示方差分析表格中统计量。Page 18 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 9.

9 t检验：某个回归系数是否为0

在线性回归中

t检验主要用于检验线性回归模型中某个特定自变量的系数是否显著。地，t检验的零假设是特定回归系数等于零，即自变量对因变量没有显著的影响。如果 t检验的 p

值小于设定的显著性水平就可以拒绝零假设认为该自变量的系数是显著不为零的即自变量对因变量有显著的影响。需要注意的是

t检验一般用来检验一个特定自变量的系数是否显著而不能判断模型整体是否显著。如果需要判断模型整体的显著性，可以使用前文介绍的 F检验。原假设、备择假设对于一元线性回归，t检验原假设和备择假设分别为：0 1 1,0

1 1 1,0:

: H b b

H b b= (29)

一般

1,0b取0，也就是检验回归系数是否为0。1,0b也可以取其他值。统计量

b1的t检验统计量：1 1,0

1ˆ

ˆSEbbbt

b−= (30)

1ˆb

为最小二乘法 OLS线性回归估算得到的系数，1ˆSEb 为其标准误：11MSE 2 ˆSEn

i

i

nn

ii

iinb

x x x x

=

==−==

−−

 (31)

上式中，MSE为本章前文介绍的残差平均值 (mean s quared error )

n是样本数据的数量 (除

NaN)。标准误越大，回归系数的估计值越不可靠。临界值如果下式成立，接受零假设 H0：1 2, 2 1 2, 2 nn t T t− − − −−   (32)

Page 19 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 否则，则拒绝零假设 H0。特别地，如果原假设和备择假设为：11: 0

: 0Hb

Hb=

 (33)

如果 (32) 成立，接受零假设 H0，即回归系数不具有显著统计性；白话说，也就是 b1 = 0，意味着自变量和因变量不存在线性关系。否则，则拒绝零假设 H0，即回归系数具有显著统计性。截距项系数对于一元线性回归，对截距项系数 b0的假设检验程序和上述类似。b0的t检验统计值：0 0,0

0ˆ

ˆSEbbbt

b−= (34)

0ˆb

为最小二乘法 OLS线性回归估算得到的系数，0ˆSEb 为其标准误：11ˆSE2n

i

i

n

i

ixbnnxx

=

=



 =+−−

 (35)

举个例子

t检验统计值 T服从自由度为 n – 2的t分布。本节采用的 t检验是双尾检测。在统计学中，双尾假设检验是指在假设检验过程中假设被拒绝的区域位于一个统计量分布的两个尾端者对于一个参数或者统计量是否等于某一特定值不确定其比该值大或小而是存在两种可能性，因此需要在两个尾端进行检验。比如给定显著性水平 α = 0.

05和自由度 n – 2 = 252 – 2 = 250

可以查表得到 t值

1 2, 2 0.975, 250 1.969498n tt−−== (36)

Python中，可以用 stats.

ppf(1 - alpha/2, DFE) 计算上式两值。由于学生t-分布对称，所以：2, 2 0.

025, 250 1.

969498ntt−= =− (37)

如图1所示，tb1 = 23.

446，因此：1 0.975, 250btt (38)

Page 20 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 表明参数 b1的t检验在 α = 0.

05水平下是显著的，也就是可以显著地拒绝 H0: b1 = 0，从而接受H1: b1 ≠ 0。回归系数的标准误差越大，回归系数的估计值越不可靠。而tb0 = 1.

759，因此：0 0.975, 250btt (39)

则表明参数b0的t检验在 α = 0.

05水平下是不显著的，也就是不能显著地拒绝 H0: b0 = 0。管模型含有截距项但若该项的出现是统计上不显著的 (即统计上等于零 )

则从任何实际方面考虑，都可认为这个结果是一个过原点回归模型。因此，系数b1的1 – α 置信区间为：1 1 2, 2 1ˆˆ SEn b t b−− (40)

这个置信区间的的含义是，真实b1在以上区间的概率为1 – α。系数 b0的1 – α 置信区间为：0 1 2, 2 0ˆˆ SEn b t b−− (41)

同理，真实b0在以上区间的概率为1 – α。# Rejection region

Reject H0Rejection region

Reject H01 α

α/2 α/2Fail to reject H0

图14.

双尾检验

9.10置信区间：因变量均值的区间本书前文在介绍一元线性回归中，大家都应该见过类似图15的图像。图中的带宽代表预测值的置信区间。预测值

ˆiy，的1 – α置信区间：1 2, 22

11ˆ MSEi

i

n n

k

kxx

ytnxx−−

=−

   +

− (42)

Page 21 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 置信区间的宽度为：1 2, 22

112 MSEi

n n

k

kxx

tnxx−−

=

 −   +

 − (43)

随着

ixx− 不断增大，置信区间宽度不断增大。ixx= 时，置信区间宽度最窄。MSE (mean square error) 减小，置信区间宽度减小。在回归分析中，预测值置信区间用于评估回归模型的预测能力。通常，预测值的置信区间越窄，说明模型预测的精度越高。# 0.15 0.10 0.05 0.00 0.05 0.10 0.15

x 0.

15 0.

10 0.

050.

000.

050.

100.

y

图15.

一元线性回归线置信区间

9.11预测区间：因变量特定值的区间预测区间 (prediction interval ) 是指回归模型估计时对于自变量给定的某个值 xp

求出因变量yp的个别值的估计区间：1 2, 22

11ˆ MSE 1p

pn n

k

kxx

ytnxx−−

=−

   + +

− (44)

与预测值的置信区间不同，预测区间同时考虑了预测的误差和未来观测值的随机性。Page 22 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 预测区间包含两个方面的误差回归方程中的估计误差和对未来观测值的随机误差。值的置信区间不同，预测区间考虑了未来观测值的随机性，因此通常比置信区间更宽。# 0.15 0.10 0.05 0.00 0.05 0.10 0.15

x 0.

15 0.

10 0.

050.

000.

050.

100.

y

图16.

一元线性回归线预测区间

# 9.12对数似然函数：用在最大似然估计 MLE

似然函数是一种关于统计模型中的参数的函数，表示模型参数中的似然性。残差的定义为：ˆi i iyy=− (45)

在OLS线性回归中，假设残差服从正态分布 N(0, σ2)，因此：2ˆ1Pr exp2 2ii

iyy

 −=− (46)

似然函数为：11ˆ1P exp2 2iinn

i

iiyy

L  == − = = −    (47)

Page 23 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 常用对数似然 ln(L)：1SSEln P ln 2 π22n

i

inL == =−  − (48)

注意，MLE中的σ为：2SSE

n= (49)

这样 ln(L) 可以写成：1ln P ln 2 π22n

i

innL 

== =−  − (50)

有似然函数和对数似然函数，请大家回顾《统计至简》第16、24章。# 9.13信息准则：选择模型的标准

AIC和BIC是线性回归模型选择中常用的信息准则，用于在多个模型中选择最优模型。AIC为赤池信息量准则 (Akaike information criterio n

AIC )，定义如下

PenaltyAIC 2 2ln kL=− (51)

其中，k = D + 1；L是似然函数。AIC鼓励数据拟合的优良性；但是，尽量避免出现过度拟合。(51) 中2k项为惩罚项

(penalty)。贝叶斯信息准则 (Bayesian Inf ormation Crit erion

BIC ) 也称施瓦茨信息准则 (Schwarz

infor mation c riterion , SIC)，定义如下。PenaltyBIC ln 2ln k n L=  −

(52)

其中，n为样本数据数量。BIC的惩罚项比AIC大。在使用 AIC和BIC进行模型选择时，应该选择具有最小 AIC或BIC值的模型。这意味着，较小的 AIC或BIC值表示更好的模型拟合和更小的模型复杂度。需要注意的是

AIC和BIC都是用来选择模型的工具但并不保证选择的模型就是最优模在实际应用中，应该将 AIC和BIC作为指导，结合领域知识和经验来选择最优模型。还需要对模型的假设和限制进行检验，以确保模型的可靠性和实用性。Page 24 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

com 9.

14残差分析：假设残差服从均值为0正态分布残差分析 (residual analysis ) 通过残差所提供的信息对回归模型进行评估分析数据是否存在可能的干扰。残差分析的基本思想是，如果回归模型能够很好地拟合数据，那么残差应该是随机分布的，没有明显的模式或趋势。因此，对残差的分布进行检查可以提供关于模型拟合优度的残差分析通常包括以下步骤：► 绘制残差图。残差图是观测值的残差与预测值之间的散点图。如果残差呈现出随机分布、没有明显的模式或趋势，那么模型可能具有较好的拟合优度。► 检查残差分布。通过绘制残差直方图或核密度图来检查残差分布是否呈现出正态分布或近似正态分布。如果残差分布不是正态分布，那么可能需要采取转换或其他措施来改善模型的拟

► 检查残差对自变量的函数形式。通过绘制残差与自变量之间的散点图或回归曲线，来检查残差是否随自变量的变化而呈现出系统性变化。如果存在这种关系，那么可能需要考虑增加自变量、采取变量转换等方法来改善模型的拟合。图17所示为残差的散点图。图18所示为残差分布的直方图。理想情况下，我们希望残差为均值为0的正态分布。为了检测残差的正态性，本节利用 Omnibus正态检验。# 0.15 0.10 0.05 0.00 0.05 0.10 0.15

x 0.

15 0.

10 0.

050.

000.

050.

100.

15Residual

图17.

残差散点图

Page 25 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

# 0.05 0.00 0.05 0.10

Residual25

0Density

图18.

残差分布直方图

Omnibus 正态检验 (Omnibus test for normality ) 用于检验线性回归中残差是否服从正态分

Omnibus 正态检验利用残差的偏度 S和峰度 K

检验残差分布为正态分布的原假设。# Omnibus

正态检验的统计值为偏度平方、超值峰度平方两者之和。Omnibus正态检验利用χ2检验 (Chi-

squared test)。代码中我们利用 scipy.

s tats.

normaltest 复现了本章前文的 Omnibus正态检验统计量值。《统计至简》第2章讲过偏度、峰度，请大家回顾。# 9.15自相关检测：Durbin -Watson

Durbin-Watson用于检验序列的自相关。在线性回归中，自相关 (autocorrelation ) 用来分析模型中的残差与其在时间上的延迟版本之间的相关性。当模型中存在自相关时，它可能表明模型中遗漏了某些重要的变量，或者模型中的时间序列数据未被正确处理。自相关可以通过检查残差图来诊断。如果残差图表现出明显的模式，例如残差值之间存在周期性关系或呈现出聚集在某个区域的情况，那么就可能存在自相关。在这种情况下，可以通过引入更多的自变量或使用时间序列分析方法来修正模型。图19所示为残差的自相关图。Page 26 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

Lag0 5 10 15 200.

图19.

残差自相关

Durbin-Watson检测的统计量为：1ˆˆ

ˆn

i i i i

i

n

ii

iy y y y

DW

yy−−

=

=− − −

=

−

 (53)

上式本质上检测残差序列与残差的滞后一期序列之间的差异大小。DW值的取值区间为0 ~

当DW值很小时 (DW < 1)，表明序列可能存在正自相关。当DW值很大时 (DW > 3) 表明序列可能存在负自相关。当DW值在2附近时 (1.

5 < DW < 2.

5 )，表明序列无自相关。其余的取值区间表明无法确定序列是否存在自相关。有关，请大家参考：https://www.

statsmodels.

org/devel/generated/statsmodels.

stats.

stattools.

dur bin_watson.

html

9.16条件数：多重共线性在线性回归中条件数 (condition number) 常用来检验设计矩阵 Xk×k是否存在多重共线性

(multicollinearity )。多重共线性是指在多元回归模型中，独立变量之间存在高度相关或线性关系的情况。线性会导致回归系数的估计不稳定使得模型的解释能力降低甚至导致模型的预测精度下降。对XTX进行特征值分解，得到最大特征值 λmax和最小特征值 λmin。条件数的定义为两者的比值的平方根：Page 27 | Chapter 9回归分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

visual ize.

ml@gma il.

max

mincondition number

= (54)

一般来说，条件数小于30，可以不必担心多重共线性。下一章讲到多元回归分析时，条件数的作用更明显。Bk6_Ch 09_03.

py代码复现图1中除ANOVA 以外的其他统计量值。线性回归是一种用于研究自变量与因变量之间关系的统计模型。方差分析可以评估模型的整体拟合优度，其中的 F检验可以用来线性模型整体显著性

t检验可以评估单个系数的显著性。拟合优度指模型能够解释数据变异的比例，常用 R2来度量。AIC和BIC用于模型选择，可以在模型拟合度相似的情况下，选出最简单和最有解释力的模型。自相关指误差项之间的相关性，可以使用 Durbin -Watson检验进行检测。条件数是用于评估多重共线性的指标，如果条件数过大，可能存在严重的多重共线性问题。综上，这些概念是线性回归分析中非常重要的指标，可以帮助我们评估模型的拟合程度、系数显著性、预测能力和多重共线性等问题。这一章的内容很有难度，现在不要求大家掌握所有的知识点。Scikit-learn也提供线性回归分析工具，请大家参考如下网页：https://scikit -learn.

org/ stable/auto _exam ples/inspection /plot_linear_model_coef ficien t_interpretation.

html

Page 1 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 10 Multivariate Linear Regression

多元线性回归用多个解释变量来预测响应变量结果科学不知道它对想象力的依赖。Scien ce does not know its debt to imagination.

—— 拉尔夫·沃尔多·爱默生 (Ralph Waldo Emerson ) | 美国思想家文学家 | 1942 ~ 2018

◄ matplotlib.

pyplot.

quiver 绘制箭头图

◄ numpy.

arccos 反余弦函数

◄ numpy.

cov 计算协方差矩阵

◄ numpy.

identit y 构造单位矩阵

◄ numpy.

linalg.

det 计算矩阵的行列式值

◄ numpy.

linalg.

inv 求矩阵逆

◄ numpy.

linalg.

matrix_rank 计算矩阵的秩

◄ numpy.

matrix 构造矩阵

◄ numpy.

ones 构造全1矩阵或向量

◄ numpy.

ones_like 按照给定矩阵或向量形状构造全1矩阵或向量

◄ plot_wireframe 绘制线框图

◄ scipy.

stats.

cdf F分布累积分布函数

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

jointp lot 绘制联合分布 /散点图和边际分布

◄ seaborn.

kdeplot 绘制KDE核概率密度估计曲线

◄ seaborn.

pairplot 绘制成对分析图

◄ statsmodels.

api.

add_constant 线性回归增加一列常数1

◄ statsmodels.

api.

OLS 最小二乘法函数

◄ statsmodels.

stats .

outliers_influence.

variance_infl ation_factor 计算方差膨胀因子

Page 2 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

四组正交关系多重共线性线性代数优化问题最小二乘法投影

QR分解

SVD分解多元回归三个平方和SST

SSESSR

t检验统计量备择假设原假设临界值条件概率视角

Page 3 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 10.

1多元线性回归这一章将探讨多元线性回归。多元线性回归是一种统计分析方法，用于研究两个或多个自变量与一个因变量之间的关系。它通过拟合一个包含多个自变量的线性模型来预测因变量的值。多元线性回归的表达式如下：0 1 1 2 2 ...DD y b b x b x b x  = + + + + + (1)

其中，b0为截距项

b1, b２…, bD代表自变量系数

ε为残差项，D为自变量个数。几何角度来看，多元线性回归得到一个超平面 (hyperplane)。用矩阵运算表达 (1)：0 1 1 2 2

ˆDD b b b b= + + + + +

yy 1 x x x ε

(2)

其中，1为全1列向量。换一种方式来写 (2)：ˆ=+

yy Xbε (3)

 

1,1 1, 1 0

2,1 2, 2 1

12 1

,1 ,11

1, , ,

1D

D

D nD

n

n n D n D nDxx y b

xx y b

xx y b



+

+   

   

    = = = = =   

        X 1 x x x y b ε

(4)

矩阵 X常被称作设计矩阵 (design matrix )。图1所示矩阵运算对应 (3)。X b @ = ε y +

图1.

多元线性回归模型矩阵运算预测值构成的列向量 ŷ，通过下式计算得到：Page 4 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

ˆ=y Xb (5)

残差向量的算式为：ˆ=−=−ε y y y Xb (6)

如图2所示，第i个观测点的残差项，可以通过下式计算得到：ˆi i i i iy y y=−=− xb

X b @ = ε y +

x(i)εi yi

图2.

计算第i个观测点的残差项图3所示为多元OLS线性回归数据关系。也就是说，ˆy可以看成设计矩阵 X的列向量线性组

y

ε = y ŷ1

x1

x2

ŷ = b 01 + b 1x1 + b 2x2 + .

+ b D-1xD-1 + b DxDx3

xD 1ŷ ε Hyperplane spanned by column vectors

of 1, x1, x2, .

, xD-1 and xD

bD 1

bDb3b2b1b0

图3.

多元OLS线性回归数据关系

Page 5 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

注意，矩阵 X为n行，D + 1列，第一列为全1列向量；增加一列全1列向量目的是为了引入常数项。如图4所示，如果数据都已经中心化 (去均值 )，则可以不必考虑常数项。ε = y ŷŷ = b 1x1 + b 2x2 + .

+ b D-1xD-1 + b DxD

ŷ ε Hyperplane spanned by column

vectors of x1, x2, .

, xD-1 and xD

bD 1

bDb3b2b1x1

x2

Centralize

x3

xD 1Centralize

yy

图4.

多元OLS线性回归数据关系，中心化数据

# 10.2优化问题：OLS

一般通过如下两种方式求得线性回归参数：◄ 最小二乘法 (Ordinary Least Square

OLS)，因变量和拟合值之间的欧氏距离最小化；◄ 最大似然概率估计 (Maximum Likelihood Estimation

MLE)，用样本数据反推最可能的模型参

OLS线性最小二乘法通过最小化残差值平方和 SSE来计算得到最佳的拟合回归线参数

arg min SSE

b (7)

对于多元线性回归，残差平方和 SSE为：222 T T

1SSEn

i

i

== =  = = = − − = − ε ε ε ε ε y Xb y Xb y Xb (8)

OLS多元线性优化问题的目标函数可以写成：Page 6 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Tf= − −b y Xb y Xb (9)

f(b) 可以整理为：T

T T T

T T T T T T

T T T T T

Quadratic termLinear term Constant2f= − −

= − −

= − − +

= − +b y Xb y Xb

y b X y Xb

y y y Xb b X y b X Xb

b X Xb b X y y y

(10)

观察上式，发现f(b) 可以看成一个多元二次函数含有二次项、一次项和常数项。因此，对于二元回归不考虑常数项系数 b0的话

b1和b2构成的曲面 f(b1

b2) 为椭圆抛物面，如图5所示。b1b2f(b1, b2)

图5.

f(b1, b2) 函数曲面

f(b) 梯度向量如下：ff=bbb (11)

f(b) 为连续函数，取得极值时，梯度向量为零向量：TTf =  − = b 0 X Xb X y 0 (12)

如果

TXX 可逆，b的解为：1TT−=b X X X y (13)《矩阵力量》介绍过，如果

TXX 不可逆，可以用奇异值分解求伪逆。f(b) 的黑塞矩阵为：2T

T2

2ff==bb X Xbb (14)

Page 7 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 下面判断 f(b) 黑塞矩阵为正定矩阵从而判定极值点为最小值点。对于任意非零向量 a，下式恒大于等于0：2 TTT0 = =  a X X a Xa Xa Xa (15)

等号成立时，即Xa = 0，即当X列向量线性相关，我们暂时不考虑这种情况。因此，对于 X

为列满秩，f(b) 黑塞矩阵为正定矩阵

f(b) 在极值点处取得最小值。模型拟合值向量 ŷ为：1TTˆ−==y Xb X X X X y (16)

残差向量 ε为：1TT−=−ε y X X X X y (17)

1TT−X X X X

为《矩阵力量》第9章介绍的帽子矩阵 (hat ma trix) H

它常出现在矩阵投影运

1TT−=H X X X X (18)

帽子矩阵 H为幂等矩阵 (idempotent matrix)

幂等矩阵是指一个矩阵与自身相乘后仍等于它本身的矩阵，即满足 H2 = H。幂等矩阵在线性代数中有广泛的应用，特别是在投影、几何变换等领在投影中，幂等矩阵可以用来描述一个向量在一个子空间上的投影；在几何变换中，幂等矩阵可以用来描述一个对象在进行相应变换后仍等于它本身。最简单的幂等矩阵就是单位矩阵 I，满足 I2 = I。利用帽子矩阵 H，ˆ==−y Hy

ε I H y (19)

10.3几何解释：投影图6所示为多维空间视角下的数据矩阵；矩阵 X = [x1, x2, …, xD] 每一列代表一个特征，每一列可以看做一个向量。鸢尾花书《矩阵力量》一书中，我们反复探讨过这一点。Page 8 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Column perspectivex1

x2

x1x2.

n × D

图6.

多维空间视角下的矩阵 X

不考虑常数项，预测值向量 ŷ可以通过下式计算得到：1 1 2 2ˆDD b b b= + + +y x x x

(20)

(20) 说明预测值向量 ŷ是自变量向量 x1

x2, …, xD的线性组合。如果 x1, x2, …, xD构成一个超平面 H，ŷ在H这个平面内。有了这一思想构造因变量向量 y和自变量向量 x1

x2, …, xD的线性回归模型相当于 y向x1

x2, …, xD构成的超平面 H投影。如图7所示，预测值向量 ŷ是因变量向量 y在H的投影结果：ˆ=+yyε (21)

简单来说，从向量投影的角度来理解多元线性回归可以将回归问题看作是将因变量向量在自变量向量所张成的子空间上的投影。# D dimension al hyperplane spanned by

column vectors of X (x1, x2, .

, xD-1, xD)ε = y ŷ y

x1x2xD-1

xD

H

Centroid

图7.

几何角度解释多元最小二乘法线性回归

Page 9 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 而残差项向量 ε是预测值向量 ŷ是因变量向量 y两者之差：ˆ=−ε y y (22)

残差项向量 ε垂直于 x1, x2, …, xD构成的超平面 H。由上所述，残差 ε (ε = y – ŷ) 是无法通过 (x0, x1, .

, xD-1, xD) 解释部分向量，垂直于超平面：T0 ⊥  =ε X X ε (23)

得到

T T T0− =  = X y Xb X Xb X y (24)

这和上一节得到的结果完全一致但是从几何视角看OLS

让求解过程变得非常简洁。请大家再次注意，只有 X为列满秩时，XTX才存在逆。此外，我们可以很容易在 X最左侧加入一列全1向量1

残差项向量 ε则垂直于1

x1, x2

xD构成的超平面 H。《统计至简》介绍过 OLS线性回归假设条件。OLS线性回归的假设条件是用来保证模型的有效性和可靠性。简单来说，这些假设条件主要包括线性关系、正态分布、同方差性、独立性和残差之和为零。首先，线性关系假设要求因变量和自变量之间的关系是线性的，即在自变量变化时，因变量的变化量是按照线性关系变化的。这个假设是 OLS回归分析的前提条件，否则回归结果将会失其次，正态分布假设要求模型的残差应该满足正态分布。正态分布是概率论和统计学中最为重要的分布之一，如果残差不满足正态分布，可能会导致回归结果失真。同方差性假设要求残差的方差在各个自变量取值下都相等。如果残差的方差不相等，会导致回归结果的可靠性下降。独立性假设要求各个观测值之间是独立的，即一个观测值的取值不受其他观测值的影响。果存在相关性，回归结果可能会失真。最后，残差之和为零要求模型的残差的总和为零，这是保证回归分析的正确性的必要条件。总之，这些假设条件对于 OLS线性回归的结果具有重要影响需要在回归分析中进行检验和表1所示为用矩阵方式表达 OLS线性回归假设。表1.

用矩阵运算表达 OLS线性回归假设假设矩阵表达线性模型

=+y Xbε

Page 10 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 残差服从正态分布

2ˆ,N ε X 0 I

残差期望值为0

E=ε X 0

残差同方差性

1 1 2 1

2 1 2 2

12var cov , cov ,

cov , var cov ,ˆ var

cov , cov , varn

n

n n n    

    

    





==



ε X I

矩阵 X不存在多重共线性

Trank 1

det 0D=+

X

XX

10.4二元线性回归为了方便大家理解，本节用实例讲解二元线性回归。二元线性回归解析式为：0 1 1 2 2ˆb b b= + +y 1 x x (25)

图8所示为二元 OLS线性回归数据关系。y

ε = y ŷ1

ŷ = b 01 + b 1x1 + b 2x2 x1

x2ŷ ε Plane spanned by column

vectors of 1, x1, and x2

b2b1b0

图8.

二元 OLS线性回归数据关系本节介绍利用两个股票日收益率解释 S&P 500日收益率。图9所示为参与回归数据 [y, x1, x2]

的散点图。图10所示为 [y, x1, x2] 数据的成对特征分析图。图11所示为 [y

x1, x2] 数据的协方差矩阵相关性和夹角热图。图12所示为二元 OLS线性回归结果。图13所示为三维数据散点图和回归平面。Page 11 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

1S&P 500, y

图9.

二元线性回归数据

S&P 500, y MCD, x2 AAPL, x10.

1 0.

0 0.

1 0.

1 0.

0 0.

1 0.

0 0.

1 0.

1S&P 500, y AAPL, x1 MCD, x2

Page 12 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 图10.

二元线性回归数据 [y, x1, x2] 成对特征分析图

S&P 500, y

MCD, x2AAPL, x1

S&P 500, y

MCD, x2AAPL, x1

S&P 500, y

MCD, x2AAPL, x1S&P 500, y

MCD, x2AAPL, x1S&P 500, y

MCD, x2AAPL, x1S&P 500, y

MCD, x2AAPL, x1(b) (c) (c)

# 0.00047 0.00053 0.00044

# 0.000440.00053 0.00087 0.00045

# 0.00045 0.000641 0.83 0.8

# 0.80.83 1 0.61

# 0.61 10° 34° 36°

36°34° 0° 52°

52° 0°

图11.

[y, x1, x2] 数据的协方差矩阵、相关性和夹角热图

OLS Regression Results

==============================================================================

Dep.

Variable: SP500 R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 607.

Date: XXXXXXXXXXXXXXXX Prob (F-statistic)

69e -96

Time: XXXXXXXXXXXXXXXX Log-Likelihood

831.

No. Observations: 252 AIC: -1656.

Df Residuals: 249 BIC: -1646.

Df Model: 2

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const -0.

0006 0.

001 -0.

984 0.

326 -0.

002 0.

AAPL 0.

3977 0.

024 16.

326 0.

000 0.

350 0.

MCD 0.

4096 0.

028 14.

442 0.

000 0.

354 0.

==============================================================================

Omnibus: 37.

744 Durbin -Watson: 1.

Prob(Omnibus): 0.

000 Jarque -Bera (JB): 157.

Skew: 0.

492 Prob(JB): 5.

67e -35

Kurtosis: 6.

749 Cond.

No.9.

==============================================================================

图12.

二元 OLS线性回归分析结果

Page 13 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

1S&P 500, y

图13.

三维空间，回归平面

Bk6_Ch 10_01.

py完成本节二元线性回归。# 10.5多元回归本节介绍一个多元回归问题构造多元 OLS线性回归模型用12只股票日收益率预测 S&P

500日收益率。图14所示股价数据。Normalized closing price3.

0SP500

TSLA

WMT

MCD

USBF

GM

COST

JNJYUM

NFLX

JPM

PFE

Page 14 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 图14.

股价数据，起始值归一化根据股价水平计算得到的日收益率。图15所示为日收益率热图。图16所示为 [y, X] 数据协方差矩阵。图17所示为均方差 (即波动率 ) 直方图。图18所示为 [y, X] 数据相关性系数矩阵热图。图19所示为几只不同股票股价收益率和 S&P

500收益率相关性系数柱状图。利用余弦相似性，根据相关性系数矩阵，可以计算得到 [y, X] 标准差向量夹角，矩阵热图如图20所示。图21所示为多元OLS线性回归解。# X y SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ 0.

图15.

[y, X] 日收益率热图

Page 15 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJSP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

图16.

[y, X] 数据协方差矩阵

SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJDaily volatility (standard deviation)0.

图17.

日波动率柱状图

Page 16 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

000 0.

463 0.

359 0.

505 0.

417 0.

571 0.

386 0.

433 0.

341 0.

390 0.

340 0.

517 0.

463 1.

000 0.

211 0.

238 0.

044 0.

150 0.

420 0.

052 0.

143 -0.

009 -0.

039 0.

353 0.

359 0.

211 1.

000 0.

148 -0.

021 0.

160 0.

282 0.

020 -0.

040 0.

111 0.

104 0.

562 0.

505 0.

238 0.

148 1.

000 0.

152 0.

508 0.

188 0.

132 -0.

003 0.

352 0.

305 0.

358 0.

417 0.

044 -0.

021 0.

152 1.

000 0.

456 -0.

127 0.

908 0.

309 0.

631 0.

497 -0.

193 0.

571 0.

150 0.

160 0.

508 0.

456 1.

000 -0.

003 0.

438 0.

276 0.

488 0.

410 0.

180 0.

386 0.

420 0.

282 0.

188 -0.

127 -0.

003 1.

000 -0.

183 -0.

143 -0.

074 -0.

011 0.

468 -0.

433 0.

052 0.

020 0.

132 0.

908 0.

438 -0.

183 1.

000 0.

338 0.

608 0.

455 -0.

167 0.

341 0.

143 -0.

040 -0.

003 0.

309 0.

276 -0.

143 0.

338 1.

000 0.

227 0.

238 0.

011 0.

390 -0.

009 0.

111 0.

352 0.

631 0.

488 -0.

074 0.

608 0.

227 1.

000 0.

721 0.

039 0.

340 -0.

039 0.

104 0.

305 0.

497 0.

410 -0.

011 0.

455 0.

238 0.

721 1.

000 0.

045 0.

517 0.

353 0.

562 0.

358 -0.

193 0.

180 0.

468 -0.

167 0.

011 0.

039 0.

045 1.

000 0.

570 0.

193 0.

149 0.

243 0.

327 0.

365 -0.

013 0.

331 0.

479 0.

269 0.

308 0.

229 1.

000SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJSP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

图18.

[y, X] 数据相关性系数矩阵热图

SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJCorrelation coefficient with S&P 5001.

图19.

股价收益率和 S&P 500收益率相关性系数柱状图

Page 17 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJSP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ0.

0 62.

4 69.

0 59.

7 65.

3 55.

2 67.

3 64.

3 70.

1 67.

1 70.

1 58.

9 55.

4 0.

0 77.

8 76.

2 87.

5 81.

4 65.

1 87.

0 81.

8 90.

5 92.

3 69.

3 78.

0 77.

8 0.

0 81.

5 91.

2 80.

8 73.

6 88.

9 92.

3 83.

6 84.

0 55.

8 81.

7 76.

2 81.

5 0.

0 81.

3 59.

4 79.

2 82.

4 90.

2 69.

4 72.

2 69.

0 76.

3 87.

5 91.

2 81.

3 0.

0 62.

9 97.

3 24.

7 72.

0 50.

9 60.

2 101.

1 70.

2 81.

4 80.

8 59.

4 62.

9 0.

0 90.

2 64.

0 74.

0 60.

8 65.

8 79.

6 68.

3 65.

1 73.

6 79.

2 97.

3 90.

2 0.

0 100.

6 98.

2 94.

2 90.

6 62.

1 90.

3 87.

0 88.

9 82.

4 24.

7 64.

0 100.

6 0.

0 70.

2 52.

6 62.

9 99.

6 70.

1 81.

8 92.

3 90.

2 72.

0 74.

0 98.

2 70.

2 0.

0 76.

9 76.

2 89.

4 61.

1 90.

5 83.

6 69.

4 50.

9 60.

8 94.

2 52.

6 76.

9 0.

0 43.

8 87.

8 74.

1 92.

3 84.

0 72.

2 60.

2 65.

8 90.

6 62.

9 76.

2 43.

8 0.

0 87.

4 72.

9 69.

3 55.

8 69.

0 101.

1 79.

6 62.

1 99.

6 89.

4 87.

8 87.

4 0.

0 76.

2 78.

9 81.

4 76.

0 70.

9 68.

6 90.

7 70.

7 61.

4 74.

4 72.

1 76.

8 0.

图20.

[y, X] 标准差向量夹角矩阵热图，余弦相似性

Page 18 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

OLS Regression Results

==============================================================================

Dep.

Variable: SP500 R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 32.

Date: XXXXXXXXXXXXXXXX Prob (F-statistic)

03e -31

Time: XXXXXXXXXXXXXXXX Log-Likelihood

493.

No. Observations: 127 AIC: -961.

Df Residuals: 114 BIC: -924.

Df Model: 12

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const -0.

0005 0.

000 -1.

038 0.

302 -0.

001 0.

TSLA 0.

0248 0.

011 2.

248 0.

027 0.

003 0.

WMT 0.

0272 0.

041 0.

667 0.

506 -0.

054 0.

MCD 0.

1435 0.

057 2.

536 0.

013 0.

031 0.

USB 0.

0164 0.

051 0.

322 0.

748 -0.

084 0.

YUM 0.

1469 0.

047 3.

114 0.

002 0.

053 0.

NFLX 0.

0972 0.

021 4.

539 0.

000 0.

055 0.

JPM 0.

1415 0.

055 2.

583 0.

011 0.

033 0.

PFE 0.

0546 0.

033 1.

662 0.

099 -0.

010 0.

F -0.

0068 0.

036 -0.

187 0.

852 -0.

078 0.

GM -0.

0105 0.

027 -0.

388 0.

699 -0.

064 0.

COST 0.

2176 0.

059 3.

713 0.

000 0.

101 0.

JNJ 0.

2414 0.

056 4.

350 0.

000 0.

131 0.

==============================================================================

Omnibus: 7.

561 Durbin -Watson: 1.

Prob(Omnibus): 0.

023 Jarque -Bera (JB): 8.

Skew: 0.

400 Prob(JB): 0.

0147

Kurtosis: 3.

978 Cond.

No.56.

==============================================================================

图21.

多元OLS线性回归分析结果

Bk6_Ch 10_02.

py完成本节多元线性回归。# 10.6正交关系第一个直角三角形通过上一章学习，大家都很清楚第一个勾股关系：2 2 2

2 2 2

SST SSR SSEˆˆ yy− = − + −y 1 y 1 y y

(26)

具体如图22所示。上一章提到这一个直角三角形可以帮助我们解释 R2。Page 19 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

Hyperplane spanned by column vectors of X ε = y ŷ y

HOrigin

θ

y−y1

ˆy−y1

y1

ˆy

图22.

第一个直角三角形第二个直角三角形除了 (26) 这个重要的直角三角形的勾股定理之外还有另外一个重要的直角三角形勾股定理

2 2 2 2 2

2 2 2 2 2ˆ ˆ ˆ= + − = +y y y y y ε (27)

具体如图23所示。图23这个直角很容易理解。残差向量

ε垂直于超平面 H内的一切向量，显然

ε垂直

Hyperplane spanned by column vectors of X ε = y ŷ y

HOrigin

θ

ˆy

图23.

第二个直角三角形

Page 20 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

第三个直角三角形此外，《矩阵力量》第22章介绍过，向量

y−y1垂直于向量

y1：T0 yy−= 1 y 1 (28)

具体如图24所示。上式体现的核心思想就是

y 中可以被均值解释的部分为

y1。Hyperplane spanned by column vectors of X y

HOrigin

θ

y−y1

y1

图24.

第三个直角三角形第四个直角三角形

OLS假设残差之和为0：10n

i

i

== (29)

注意，如果总残差不为0

就说明预测值的总和与实际观测值的总和不相等这意味着模型存在偏差，不能很好地解释数据。对应向量运算：TT0==1ε ε 1 (30)

残差向量可以写成：ˆˆ yy = − = − − −ε y y y 1 y 1 (31)

上式左乘1T，得到：Page 21 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

T T T

00ˆ yy= − − −1ε 1 y 1 1 y 1

(32)

即

Tˆ 0 y−= 1 y 1 (33)

也就是说，如图25所示，ˆy−y1垂直于向量

Tˆ 0 yy−= 1 y 1 (34)

上式体现的核心思想就是

ˆy 的均值也是

Hyperplane spanned by column vectors of X HOrigin

θ

ˆy−y1

y1

ˆy

图25.

第四个直角三角形

# 10.7三个平方和这一节介绍对于多元 OLS线性回归如何求解SST

SSR和SSE这三个平方和。对于多元 OLS线性回归模型，SST可以通过矩阵运算求得：TSST =n−Jy I y (35)

其中矩阵 J为全1方阵，形状为 n × n：# T1 1 1

1 1 1

1 1 1nn



==



J 11

(36)

Page 22 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com SSR可以通过矩阵运算求得：TSSR =n−Jy H y (37)

其中矩阵 H为本书前文所讲的帽子矩阵，形状为 n × n：1TT−=H X X X X (38)

同样，对于多元 OLS线性回归模型，SSE可以通过矩阵运算求得：TSSE = − y I H y (39)

对于多元 OLS线性回归模型，MSE的矩阵运算为：# T T T 2

TT

TMSE =

2nk

nk

nk

nk−

−

−+=−

−=−

−=−I H y

y y y Hy y H y

y y y Hy

y I H y (40)

上式推导过程采用帽子矩阵重要的性质。# 10.8 t检验对于多元 OLS线性回归模型模型系数 b0

b1、b2 … bD的协方差矩阵 C可以通过下式计算

12Tˆ−=C X X (41)

T

2ˆMSEnk==−εε (42)

矩阵 C的对角线元素 Cj+1, j+1为

ˆ

jb的方差，非对角线元素为

ˆ

jb 和

ˆ

kb的协方差。ˆ

jb

的标准误

ˆSEjb 为：1, 1ˆSEj j jb++=C (43)

对于多元线性回归，假设检验原假设和备择假设分别为：Page 23 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

0 ,0

1 ,0:

: jj

jjH b b

H b b= (44)

bj的t检验统计值：ˆSEjj

j

jbbT

b−= (45)

类似地，如果下式成立，接受零假设 H0：1 2, 1 2, n k j n k t T t− − − −−   (46)

否则，则拒绝零假设 H0。系数 bj的1 – α 置信区间为：1 2, ˆˆ SEj n k jb t b−− (47)

对于多元 OLS线性模型，预测值

ˆiy，的1 – α置信区间：# T 1T

1 2, 2ˆ MSEi i i

n yt−

−−   x X X x (48)

x(i) 为矩阵 X的第i行：,1 ,2 , 1i

i i i Dx x x=x

(49)

类似地，对于多元 OLS线性回归模型，yp的预测区间估计为：# T 1T

1 2, 2ˆ MSE 1i i i

n yt−

−−   + x X X x (50)

10.9多重共线性线性回归模型的解释变量不满足相互独立的基本假设前提下如果模型的解释变量存在多重共线性，将导致最小二乘法得到的模型参数估计量非有效且方差变大参数估计量经济含义不合上一章介绍过采用条件数 (Condition numbe r) 来判定多重共线性。对XTX进行特征值分解，得到最大特征值 λmax和最小特征值λmin。条件数的定义为两者的比值的平方根。条件数小于30，可以不必担心多重共线性。如果 XTX可逆，XTX的行列式值不为0：Tdet 0  XX (51)

Page 24 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 这里再介绍一个评价共线性的度量指标方差膨胀因子 (variance inflation factor

VIF )，也称为方差扩大因子。一个还有 n个解释变量的矩阵

ˆ

tX，对于其中的任意解释变量

,itX，其对应的方差膨胀因子

VIFi 可由下式计算：21VIF1i

iR=− (52)

其中

iR是解释变量

,itX与其解释变量

,,jtX j i 回归模型的决定系数：, 0 ,

1,=+n

i t j j t t

j j iXX  

=+ (53)

当某个变量

,itX 能被其他变量完全线性解释时，iR的值趋近于1，iVIF的值将趋近于无穷所以，各个变量的 VIF值越小，说明共线性越弱。最常用的 VIF阈值是10，即解释变量的

VIF值都不大于10时，认为共线性在可接受范围内；此外，VIF ≤ 5也是比较常见的、但相对而言更为严格的判断标准。# 10.0条件概率视角看多元线性回归《统计至简》第12章介绍过，多元线性回归本质上就是条件概率中的条件期望值。如果随机变量向量χ和γ服从多维高斯分布：, N            χ χχ χγ

γ μ Σ Σ

(54)

其中，χ为随机变量 Xi构成的列向量，γ为随机变量 Yj构成的列向量：# DMXY

XY

XY   

   

   ==   

   

   χγ

(55)

Page 25 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

χ γ

χ

γ χ

Σγγµχ

µγ

图26.

均值向量、协方差矩阵形状，图片来自鸢尾花书《统计至简》第12章如图27所示，给定 χ = x的条件下 γ的条件期望为：1E−

图27.

给定 χ = x的条件下 γ的期望值的矩阵运算图片来自鸢尾花书《统计至简》第12章对于本例，我们对 (56) 进行转置得到：1EEy−= + −XX Xy x

by x X ΣΣ

(57)

[y, X] 对应的协方差矩阵如图28所示。图29为对 ΣXX求逆。Page 26 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

SP500SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

XXy

yΣXX ΣXyΣyX Σyy

图28.

[y, X] 协方差矩阵

ΣXX (ΣXX) 1TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

图29.

分块协方差矩阵求逆如图30所示，截距系数之外的多元线性回归系数向量为：1~D−=XX Xy bΣΣ (58)

Page 27 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

com 如图31所示，b0为：0 1~EED b=− y X b (59)

其中，E(X) 为行向量。(ΣXX) 1@ ΣXyTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

SP500=

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJb1~D

图30.

求线性回归参数，除截距以外

= b0 E(y) E(X)TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ@

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJb1~D

图31.

求截距系数

Bk6_Ch 10_03.

py完成本节运算。Page 28 | Chapter 10多元线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gma il.

OLS线性回归是一种在机器学习中常用的算法它可以通过最小化残差平方和来建立线性模型，从而用于预测和分析因变量与自变量之间的关系。OLS线性回归适用于数据分析、预测模型、异常检测、特征工程等多种机器学习任务。通过使用 OLS线性回归，可以得出自变量对因变量的影响程度、探索自变量之间的关系、预测因变量的取值，以及识别异常值等。OLS线性回归是一种简单但可靠的机器学习算法，为数据分析和预测建模提供了强大的工具和方法。鸢尾花书从不同视角介绍过 OLS线性回归。《数学要素》从代数、几何、优化角度讲过线性回归，《矩阵力量》从线性代数、正交投影、矩阵分解视角分析线性回归。《统计至简》又增加了条件概率、MLE这两个视角。鸢尾花书有关 OLS线性回归的讲解至此告一段落，本书后续将介绍回归中的正则化、贝叶斯回归、非线性回归等话题。Page 1 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 11 Regularized Regression

正则化回归利用正则项，缩减挑选特征，构造简洁模型遇到数学难题，别犯愁；困扰我的难题比你的大得多。Do not worry t oo much about your difficulties in mathematics

I can assure you that mine are still

greater.

—— 阿尔伯特·爱因斯坦 (Albert Einstein ) | 理论物理学家 | 1879 ~ 1955

◄ seaborn.

lineplot 绘制线图

◄ sklearn.

l inear_model.

E lasticNet 求解弹性网络回归问题

◄ sklearn.

linear_model.

lars_path 生成Lasso回归参数轨迹图

◄ sklearn.

linear_mo del.

Lasso 求解套索回归问题

◄ sklearn.

linear_model.

Ridge 求解岭回归问题

◄ sklearn.

metrics.

mean_squared_error 计算均方误差 MSE

◄ statsmodels.

api.

add_constant 线性回归增加一列常数1

◄ statsmodels.

api.

OLS 最小二乘法函数

Page 2 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

套索回归正则化岭回归弹性网络回归

Page 3 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 11.

1正则化：抑制过度拟合正则化 (regularization) 可以用来抑制过度拟合。本书前文提过，所谓过度拟合，是指模型参数过多或者结构过于复杂。正则项 (regularizer

regularization term

penalty term ) 通常被加在目标函数 (objective function)

正则项可以让估计参数变小甚至为0

这一现象也叫特征缩减 (shrinkage)。本章将采用图形方式来讲解如何在多元线性回归目标函数中引入正则项。本章将 L1正则项

L2正则项以及 L1和L2混合正则项利用在多变量线性回归中。L1正则化为回归参数的 L1范数，L2正则化为回归参数的 L2范数。鸢尾花书中在谈及 Lp范数时，会采用相对严格的数学记号 Lp。OLS优化问题对于多元线性 OLS回归，优化问题为：2arg min −

by Xb (1)

对于二元线性 OLS回归不考虑常数项系数

b1和b2两个回归参数形成如图1所示曲面。易发现曲面为二次椭圆曲面。b1b2f(b1, b2)

图1.

二元线性 OLS回归参数曲面

L2正则化线性 OLS中引入 L2正则项可以得到岭回归 (ridge regression)

regularize22

rarg min −+

by Xb b (2)

Page 4 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 白话说，L2正则化是回归参数各个元素平方之和。α这个惩罚系数是用户决定的。注意，一般文献中上式惩罚系数用 λ

本章和Scikit-learn保持一致采用α。(2) 相当于图1曲面叠加了 L2正则项曲面，具体如图2。L2正则项曲面等高线为正圆面，对应的最小值点为原点。叠加得到的岭回归参数曲面最小值位置朝原点发生明显偏移。当 (2) 中参数α

越大，正则项影响越大，求解优化问题得到的回归参数越靠近原点。b1b2f(b1, b2)

b2

b1

b1b2L2 regularizer

图2.

岭回归参数曲面

L1正则化线性 OLS中引入 L1正则项可以得到套索回归 (LASSO regression)

r2

regulariz2

e1arg min2n−+

by Xb b (3)

注意，(3) 中多元线性 OLS回归优化项除以2n，n为样本数据数量。此外，不同文献套索回归的目标函数稍有不同，本章和Scikit-learn保持一致。白话说，L1正则化是回归参数各个元素绝对值之和。Page 5 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

鸢尾花书《矩阵力量》介绍过 L1正则项曲面等高线为旋转正方形。(3) 相当于在图1二次椭圆抛物面上叠加图1曲面叠加。图3所示为这一过程。套索回归可以进行特征选择，从而有效减少回归模型所依赖的特征数量本章后文将从不同角度详细讲解这一

b1b2f(b1, b2)

L1 regularizerb1b2

b1b2

图3.

套索回归参数曲面

L1 + L2正则化线性 OLS中以不同比例同时引入 L1和L2正则项可以得到弹性网络回归 (elastic net

regression)：2 1 21 1arg min22n− − + + 

by Xb b b (4)

其中，参数ρ用来调和 L1和L2正则项的比例。图4所示如何构造得到弹性网络回归系数曲弹性网络回归相当于岭回归和套索回归的合体。Page 6 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

f(b1, b2)

L1 regularizer

b1b2L2 regularizer

b2

b1b2

b1

图4.

弹性网络回归参数曲面

# 11.2岭回归如前文所述，岭回归引入 L2正则项来缩减模型参数岭回归的优化目标函数为

OLS L2 regularizerf  = − +b y Xb b

(5)

图5所示为给定α条件下

(5) 如何构造得到岭回归目标函数参数曲面等高线图。注意，本节假设回归问题为二元只有 b1和b2两个回归参数并且不考虑常数项系数。如前文所述，(5) 目标函数中 OLS部分对应椭圆抛物面，最小值点为红色 ×；红色 ×为二元

OLS线性回归参数解的位置。(5) 中L2正则项则对应正圆抛物面，最小值点为蓝色 ×，位于原点。原点处，参数系数为全

Page 7 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

根据《数学要素》一书中介绍的二次曲面内容两个二次曲面叠加得到的一般还是一个二次曲面。(5) 对应的曲面 f(b1

b2) 仍然是一个椭圆抛物面最小值点为黄色 ×；黄色 × 为给定α条件下岭回归参数的优化解。容易发现，黄色 × 位于红色 × 和蓝色 × 之间；相对 OLS线性回归参数红色 ×，岭回归参数黄色 ×，更靠近原点。f(b1, b2)

L2 regularizerb2

b1b2

b1b2

b1OLS

图5.

构造岭回归优化问题参数曲面不断增大 L2约束项参数α

可以发现岭回归参数优化解不断靠近原点如图6所示。图6分图中的等高线为岭回归曲面 f(b1, b2)。当约束项参数α不断增大，f(b1, b2) 曲面中L2正则项

(正圆曲面 ) 影响力不断增强。参数α不断增大，f(b1, b2) 曲面等高线也从旋转椭圆渐渐变成正圆，最小值点也渐渐靠近 (收缩到 ) 原点。Page 8 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

图6.

不断增大α，岭回归参数位置变化构造一个线性回归问题，利用12只股票的日收益率解释标普500涨跌。图7所示为利用 OLS

多元线性回归得到的这个回归问题的参数。Page 9 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

OLS Regression Results

==============================================================================

Dep.

Variable: SP500 R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 32.

Date: XXXXXXXXXXXXXXXX Prob (F-statistic)

03e -31

Time: XXXXXXXXXXXXXXXX Log-Likelihood

493.

No. Observations: 127 AIC: -961.

Df Residuals: 114 BIC: -924.

Df Model: 12

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const -0.

0005 0.

000 -1.

038 0.

302 -0.

001 0.

TSLA 0.

0248 0.

011 2.

248 0.

027 0.

003 0.

WMT 0.

0272 0.

041 0.

667 0.

506 -0.

054 0.

MCD 0.

1435 0.

057 2.

536 0.

013 0.

031 0.

USB 0.

0164 0.

051 0.

322 0.

748 -0.

084 0.

YUM 0.

1469 0.

047 3.

114 0.

002 0.

053 0.

NFLX 0.

0972 0.

021 4.

539 0.

000 0.

055 0.

JPM 0.

1415 0.

055 2.

583 0.

011 0.

033 0.

PFE 0.

0546 0.

033 1.

662 0.

099 -0.

010 0.

F -0.

0068 0.

036 -0.

187 0.

852 -0.

078 0.

GM -0.

0105 0.

027 -0.

388 0.

699 -0.

064 0.

COST 0.

2176 0.

059 3.

713 0.

000 0.

101 0.

JNJ 0.

2414 0.

056 4.

350 0.

000 0.

131 0.

==============================================================================

Omnibus: 7.

561 Durbin -Watson: 1.

Prob(Omnibus): 0.

023 Jarque -Bera (JB): 8.

Skew: 0.

400 Prob(JB): 0.

0147

Kurtosis: 3.

978 Cond.

No.56.

==============================================================================

图7.

多元 OLS线性回归解利用 sklearn.

linear_model.

Ridge 函数，我们可以求解上述问题的岭回归参数。设定不同的α

值，可以获得一系列岭回归参数。图8所示为随着α增大，岭回归参数变化。可以发现，α增大时，参数逐步最大限度接近0，但是不等于0。这一点和本章后文将介绍的套索回归和弹性网络回归截然不同。用残差平均值 MSE来量化岭回归参数和 OLS参数的差距：ridge OLS ridge OLS21MSE

1D=−+b b b b (6)

图9所示为随着α增大，岭回归参数和 OLS参数的差距不断增大。Page 10 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

11001011020.

00CoefficientsJPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLXOLS

图8.

随着α增大，岭回归参数变化

10 410 310 210 11001011020.014

004Coefficient error

图9.

和OLS相比，岭回归参数误差

Bk6_Ch 11_01.

py绘制本节图像。# 11.3几何角度看岭回归从另外一个角度看岭回归岭回归可以看做是 OLS线性回归问题加一个约束条件。Page 11 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

2arg min

subject to: 0 c−

−by Xb

b (7)

(7) 中的约束条件中 c是一个阈值就是把回归参数限制在一定范围之内

2 2 2 2

0 1 2 D b b b b c+ + + + 

(8)

注意，(7) 中阈值 c越小，对应惩罚系数 α越大。不考虑常数系数，D = 2时，12b b c+ (9)

上式为一个正圆面，圆心位于原点，半径为

OLS对应的是旋转椭圆等高线和 (9) 正圆相切就是约束条件下优化解，也就是岭回归系数。b2

b1OLS solution

Ridge solution

图10.

约束角度看岭回归图11所示为正圆面半径

c取不同值时，岭回归回归系数的优化解位置变化。b2

b1b2

b1b2

b1b2

b1

Page 12 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图11.

c取不同值时，岭回归优化系数位置多元 OLS线性回归系数 b的解：1TT−=b X X X y (10)

根据本书前文介绍的内容

OLS线性回归的优化问题解存在且唯一的条件是 X列满秩。如果，不满足 X列满秩这个条件，则表明X列向量存在线性相关，即多重共线性。当X列与列之间线性相关或者线性相关较大时

XTX的行列式等于或接近于0

无法求解 (10) 中XTX一项的逆，会使得 OLS解不稳定，而岭回归线性回归系数 b的解为：1TT−=+b X X I X y (11)

比较 (10)，可以发现 (11) 中变为求解XTX + αI的逆；将 XTX 加上矩阵 αI 变成非奇异矩阵并可以进行求逆运算。而 αI 为对角矩阵对角线上元素为 α

其余为0，形状酷似 “山岭”

是“岭回归”名称的由来。图12.

αI对角矩阵引入的“山岭”

11.4套索回归斯坦福大学教授 Robert Tibshirani 在1996年首次提出将 L1范数作为 OLS正则项得到 Lasso

Lasso是least absolu te shr inkage and selection ope rator的缩写。套索的优化目标函数为：r

OLL1 regular

Size1

2fn = − +b y Xb b

(12)

Page 13 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图13所示为给定α条件下

(12) 如何构造得到套索回归目标函数参数曲面等高线图。所述，(12) 目标函数中 OLS部分对应椭圆抛物面，最小值点为红色 ×；红色 ×为二元 OLS线性回归参数解的位置。(12) 中L1正则项曲面等高线对应旋转正方形最小值点为蓝色 ×

位于原点。容易发现，黄色 × 位于红色 × 和蓝色 × 之间；相对 OLS线性回归参数红色 ×，岭回归参数黄色 ×，更靠近原点。f(b1, b2)

L1 regularizerb2

b1

b2

b1b2

b1

图13.

构造套索回归优化问题参数曲面图14所示为不断增大 α，套索回归参数位置变化；可以发现套索回归采用 L1正则化，可以导致参数估计结果为0。Page 14 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

图14.

不断增大 α，套索回归参数位置变化利用 sklearn.

linear_mode l.

Lasso 可以获得套索回归的结果，利用本章前文的代码，将岭回归函数，换成套索回归函数，对于同一个问题，可以得到图15。该图所示为随着α增大，套索回归参数变化。观察图15

可以发现在回归模型中

α增大，一些特征快速收缩为0

这个过程也是一个特征选择的过程。在套索回归中，系数越小表示对结果的影响越小，系数为0表示该特征没有对结果的影响，因此套索回归可以用于特征选择和降维。因此套索回归可以删除没有必要的特征，产生更为简洁的回归模型。特别地，sklear n.

linear_model.

lars_path 函数可以用来生成套索回归参数轨迹图。图16所示为和OLS相比，套索回归参数误差。Page 15 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

00CoefficientsJPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

10 410 310 510 610 7

图15.

随着α增大，套索回归参数变化

10 410 310 510 610 70.014

004Coefficient error

图16.

和OLS相比，套索回归参数误差

11.5几何角度看套索回归类似地，本节从几何角度看套索回归。套索回归，可以看做是 OLS线性回归问题，加一个约束条件：1arg min

subject to: 0 c−

−by Xb

b (13)

(7) 中的约束条件中 c也是一个阈值，即：Page 16 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0 1 2 D b b b b c+ + + + 

(14)

不考虑常数系数，D = 2时，12b b c+ (15)

上式为一个旋转正方形，中心位于原点。OLS对应的是旋转椭圆等高线可以和 (15) 旋转正方形相切，或在顶点处相交，如图17所示。图17.

套索回归的 L1正则项如图18所示对于同一个OLS优化问题不同的 c阈值大小会在不同位置得到套索回归系前文说过，岭回归系数可以无限接近于0，但是不等于0；不同于岭回归，套索回归的参数可以直接为0。套索回归参数的这种特点叫做稀疏性 (sparsity)。稀疏性是指在套索回归中，某些特征系数被稀疏化为0

使得模型参数更加简化和易于解释同时也减少了数据维度提高了模型的泛化能力。当样本数据矩阵特征过多但是只有少数特征对回归模型有贡献去掉剩下的特征对模型没有什么影响。也就是说，回归模型只关注系数向量中非零项特征就足够了。因此，区别于岭回归，套索回归可以进行特征选择。b2

b1b2

b1b2

b1b2

b1

图18.

c取不同值时，套索回归优化系数位置

Page 17 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

2 1 0

x12 1 0

x12 1 0

x12 1 0

x12 1 0

x12 1 0

x1(a) p = 0.

05 (b) p = 0.

2 (c) p = 0.

(d) p = 1 (e) p = 1.

5 (f) p = 2

(g) p = 4 (h) p = 8 (i) p = inf2

2x2

2x2

2x22

2x2

2x2

2x22

2x2

2x2

2x22 1 0

x12 1 0

x12 1 0

x1

图19.

p取不同值时，Lp范数等高线形状变化；注意，严格来讲只有 p ≥ 1才是范数有大家可能会问，为什么 L1正则项会有这种稀疏性效果？回顾丛书《矩阵力量》一书中给出的图19。图19中给出，p取不同值时，Lp范数等高线形状变化。可以发现，p > 1时，Lp范数等高线形状连续光滑，没有尖点。只有 p ≤ 1时，等高线图出现顶点尖点；但是当 p < 1时，目标函数为非凸函数，优化问题求解困难。正是这个突出尖点的存在，且满足凸优化问题，让套索回归产生稀疏的向量解。再次强调，数学上严格来讲，只有 p ≥ 1才是 Lp范数。相信大家现在理解为什么，L2范数作为正则项，无法产生稀疏性效果。二维平面下 L2正则项的等高线是正圆；与正方形相比，正圆根本没有棱角。因此 OLS等高线和这个正圆相切时，得到任意系数为0的机会几乎为零。这也就是为什么 L2正则化不具备稀疏性的原因。Page 18 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 以上结论不仅仅适用于二维，三维甚至更多维度同样适用。图20比较三维空间的 L1和L2

正则项等高线曲面。《数学要素》一本在超椭圆相关内容中介绍过图20图像。图20 (a) 中，L1正则项存在大量突出尖点；这些尖点都对应着部分系数为0。图20 (b) 给出的正球体 (L2正则 )

任意一丁点扰动比如计算误差收敛等等，都会让回归系数不能恰好为0。(a) L1 regularizer (b) L2 regularizer

图20.

三维空间的 L1和L2正则项此外，有些问题希望一些特征参数同时为0，或者同时不为0。这时可以设计，组 lasso

(group lasso) 惩罚项来实线这一目标。与传统的 lasso回归不同之处在于，组 lasso回归在 L1正则化项中增加了对特征分组的惩罚项。这个惩罚项是对组内系数的 L1范数进行惩罚，从而鼓励组内特征系数共享相同的值或者趋近于零。因此，组 lasso可以同时选择重要的特征和重要的特征这个方法在处理高维数据时特别有效，因为它可以减少特征的数量，避免过拟合，而且还可以保留组内特征之间的相关性。图21所示为三维空间中两种lasso惩罚项结构。图21.

三维空间中组 lasso惩罚项混合 L1和L2正则项的弹性网络回归方法可以克服 L2正则项的不具备稀疏性这一缺点；这是我们下一节要介绍的内容。Page 19 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 11.

6弹性网络回归弹性网络回归 (elastic net regression) 以不同比例同时引入 L1和L2正则项对应的目标函数

Elastic net regularize22

2 1 2

OLSr1 1

22fn− = − + + 

b y Xb b b

(16)

注意，α为正则项惩罚系数，参数ρ用来调和 L1和L2正则项的比例。α和ρ都是用户输入的数值。图22所示为构造弹性网络回归优化问题参数曲面等高线的过

f(b1, b2)

L1 regularizerL2 regularizer

Elastic net r egularizer

图22.

构造弹性网络回归优化问题参数曲面等高线图23所示为不断增大 α，弹性网络回归参数位置变化。可以发现 α增大，回归系数 b1不断靠近0，甚至为0。图24所示为回归系数运动轨迹，弹性网络回归系数靠近0的“速度”慢于套索回

Page 20 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

图23.

不断增大 α，弹性网络回归参数位置变化

α increases

图24.

不断增大 α，弹性网络回归参数变化轨迹

Page 21 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

本节前文介绍，参数ρ用来调和 L1和L2正则项的比例；下面看一下参数ρ对弹性网络正则项形状的影响。图25和图26分别展示二维平面和三维空间中弹性网络正则项形状随ρ变化。大，弹性网络正则项越接近 L1，稀疏性越强；ρ越小，弹性网络正则项越接近 L2，稀疏性越弱。ρ increases

图25.

不断增大ρ，二维平面弹性网络正则项等高线形状

ρ increases

图26.

不断增大ρ，三维空间弹性网络正则项等高线形状图27所示为随着α增大，弹性网络回归参数变化，也就是套索回归参数轨迹图。注意，在这一过程中，参数ρ不变。sklearn.

linear_model.

ElasticNet 函数可以用来求解弹性网络回归问题。此外，sklearn.

l inear _model.

enet_path 可以专门绘制套索回归参数轨迹图。00CoefficientsJPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

10 410 310 510 610 7

Page 22 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图27.

随着α增大，弹性网络回归参数变化图28比较套索回归和弹性网络回归参数随α变化；同样颜色的实线是套索回归参数，划线是弹性网络回归参数。容易发现，套索回归参数更快收缩到0。弹性网络回归是套索回归和岭回归的结合体，它继承了套索回归的稀疏性，可以用来筛选特征，缩减无关参数。但是，由于引入岭回归 L2正则项，弹性网络回归在淘汰特征的过程要慢于套索回归。00CoefficientsJPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

10 410 310 510 610 7

图28.

比较套索回归和弹性网络回归参数随α变化图29所示为和OLS相比，弹性网络回归参数误差。004Coefficient error

10 410 310 510 610 7

图29.

和OLS相比，弹性网络回归参数误差

Page 23 | Chapter 11正则化回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/Visua lize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https: //space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

正则化是一种常用的机器学习技术，用于减小模型的复杂度和提高泛化能力。它通过在损失函数中添加一个正则项，强制模型参数的取值不要过大，从而避免模型过拟合。正则化技术包括

L1正则化和 L2正则化两种

L1正则化将模型参数向0稀疏化

L2正则化将模型参数平滑化于不同的数据集和模型结构可以选择不同的正则化方法。正则化技术在实际应用中被广泛使用，可以提高模型的预测能力和稳定性，避免过拟合和欠拟合等问题。推荐大家阅读 Statistical Learning with S parsi ty

The Lasso and Generalizations。本书是稀疏统计学习专著。图书 PDF文件可以免费从如下网址下载。https://web.

stanford.

edu/~hastie/Sta tLearnSparsity/

有关岭回归，建议大家阅读 Lecture notes on ridge regression。下载地址如下：https://arxiv.

org/abs/15 09.

09169

Page 1 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com 12 Bayesian Regre ssion

贝叶斯回归用贝叶斯推断求解回归模型参数审视数学，你会发现它不仅是颠扑不破的真理而且是至高无上的美丽 ——那种冷峻而朴素的美，不需要唤起人们任何的怜惜没有绘画和音乐的浮华装饰纯粹，只有伟大艺术才能展现出来的严格完美。# Mathematics

rightly viewed

possesses not only truth

but supreme beauty — a beauty cold and austere

like that of sculpture

without a ppeal to any part of our w eaker nat ure

without the gorgeous trappings

of painting or music

yet sublimely pure

and capable of a stern perfection such as only the greatest art

can show.

—— 伯特兰·罗素 (Bertrand Russell ) | 英国哲学家数学家 | 1872 ~ 1970

◄ pymc3.

Normal 定义正态先验分布

◄ pymc3.

HalfNormal 定义半正态先验分布

◄ pymc3.

plot_posterior 绘制后验分布

◄ pymc3.

sample 产生随机数

◄ pymc3.

traceplot 绘制后验分布随机数轨迹图

Page 2 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

贝叶斯回归贝叶斯定理正则化岭回归无信息先验概率似然证据因子联合后验先验套索回归后验似然 × 先验比例

PyMC3模拟

Page 3 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com 12.

1回顾贝叶斯推断简单来说，贝叶斯推断 (Baye sian inference) 就是结合“经验 (先验 )”和“实践 (样本 )”

得出“结论

(后验 )”。贝叶斯推断把模型参数看作随机变量。在得到样本之前，根据主观经验和既有知识给出未知参数的概率分布叫做先验分布 (prior)。获得样本数据后，根据贝叶斯定理，基于给定的样本数据先计算似然分布 (likelihood)

然后模型参数的后验分布 (prior)。上面这段文字对应如下这个公式：# Likelihood Prior

Posterior

|

|

|||

|dX

X

Xf x ffx

f x f



  



=



(1)

最后根据参数的后验分布进行统计推断。贝叶斯推断对应的优化问题为最大化后验概率

(Maximum A Posteriori , MAP )。本章介绍如何利用贝叶斯推断完成线性回归。大家如果对 (1) 感到陌生的话，请回顾《统计至简》第20、21两章。线性回归模型为了配合贝叶斯推断，把多元线性回归模型写成：0 1 1 2 2ˆi i i i

DD y x x x   = + + + +

(2)

其中，i为样本序号，D为特征数。当D = 1时，一元线性回归模型为：0 1 1ˆiiyx=+ (3)

似然似然函数可以写成：0 1 1 2 2

| 2211| exp2 2πi i i i

nDD

iy x x x

f   

 

=− + + + +=−

 γyθ

(4)

这意味着假设残差ε服从 N(0, σ2)。贝叶斯定理利用贝叶斯定理，我们可以得到后验分布：Page 4 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

|

|||ffff

=γ

γ

γyθθθyy (5)

最大后验优化：MAP |ˆ arg max | f =γ

θθ θ y (6)

如图1所示，随着样本不断引入，MAP优化结果不断接近真实参数。θ0θ1

xy

Actual

ActualPredicted

xy

xy

xy

xy

xyActual

ActualPredicted

PredictedActual

Actualθ0θ1

Posterior

Posterior

PosteriorActualActualMAP

ActualMAP

MAP

图1.

贝叶斯回归后验概率随样本变化由于后验 ∝ 似然 × 先验，最大后验优化等价于：Page 5 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

MAP |ˆ arg max | ff =γ

θθ y θ θ (7)

为了避免算数下溢，取对数后，优化问题可以写成：MAP |ˆ arg max ln | ff =γ

θθ y θ θ (8)

鸢尾花书之前介绍过算术下溢 (arithmetic underflow) 也称为浮点数下溢 (floating point

underflow)，是指计算机浮点数计算的结果小于可以表示的最小数。(8) 进一步整理为：MAP |ˆ arg max ln | ln ff =+γ

θθ y θ θ (9)

12.2贝叶斯回归：无信息先验《统计至简》第20章介绍过无信息先验 (uninformative prior)。没有先验信息或者先验分布不清楚我们可以用常数或均匀分布作为先验分布比如 f(θ)

= 1。最大后验优化就可以写成：MAP |ˆ arg max ln | f =γ

θθ y θ (10)

这和 MLE的目标函数一致：MLEˆ arg max ln ; f =

θθ y θ (11)

将 (4) 代入

ln |fyθ 得到：| 0 1 1 2 2 221

Constant

Constant11ln | ln2 2π

1ln2 2πn

i i i i

DD

if y x x x n

n    

 

==− − + + + + +

−=− + γyθ

yXθ

(12)

忽略常数，最大化后验 MAP优化问题等价于如下最小化问题：MAP 2ˆ arg min=−

θθ y Xθ (13)

这和前文的 OLS线性回归优化问题一致。Page 6 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com 12.

3使用 PyMC 3完成贝叶斯回归本节利用 PyMC3完成模型为 y = θ0 + θ1x1贝叶斯回归。如图2所示，黑色线为真实模型，参数为截距θ0 = 1、斜率θ1 = 2。图2中蓝色散点为样本点。# Actual

y = 1 + 2 x

# 0.0 0.2 0.4 0.6

8 1.

图2.

真实模型和样本点图3所示为三个参数的后验分布随机数轨迹图。随机数轨迹由 PyMC3中马尔科夫链蒙特卡洛

(Markov Chain Monte Carlo , MCMC) 生成。图中只绘制达到平稳状态后的轨迹。每个参数模拟两条轨迹。前文提过残差ε服从 N(0, σ2)，所以残差也是一个模型参数。本章配套代码中，残差的先验分布为半正态分布 (half normal dis tribution)

如图4所示。有关半正态分布，大家可以参考：https://www.

pymc.

io/projects/docs/en/latest/api/distributions/generated/pymc.

HalfNormal.

html

(a) θ0

# 0.6 0.8 1.0 1.2 1.4 0 200 400 600 800

0 200 400 600 800

0 200 400 600 8001.5

4(b) θ1

# 1.2 1.6 2.0 2.4

(c) σ

# 0.4 0.5 0.6 0.7

Page 7 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com 图3.

后验分布随机数轨迹图

0 2 4PDF

σ = 0.

σ = 0.

σ = 1.

σ = 1.

σ = 2.

图4.

半正态分布概率密度曲线图5所示为后验分布随机数的直方图。直方图合并两条 MCMC轨迹。图中均值可以视作

MAP的优化解。HDI代表最大密度区间 (highest density interval)

即后验分布的可信区间。区间越窄，后验分布的确信度越高。图6所示为参数θ0和θ1后验分布随机生数构成的分布。图7所示为贝叶斯线性回归的结果，图中红色线为预测模型。图中的浅蓝色线为50条后验分布的采样函数，它们对应图6中的50个散点。红色线相当于这些浅蓝色线 “取平均”。(a) θ0

# 1.0 0.5 1.5Mean = 1.04

94% HDI

# 1.3 0.81

# 1.0 1.5 2.0 2.52.3 1.5Mean = 1.9

94% HDI(b) θ1 (c) σ

8Mean = 0.

94% HDI

# 0.55 0.37

图5.

后验分布直方图

θ12.

θ00.

8 1.

0 1.

2 1.

Page 8 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com 图6.

参数θ0和θ1后验分布随机生数构成的分布

ActualPredicted

y = 1.

04 + 1.

88 x

y = 1 + 2 x

# 0.0 0.2 0.4 0.6

8 1.

图7.

贝叶斯线性回归结果

Bk6_Ch12_01.

ipynb 绘制本节图像。# 12.4贝叶斯视角理解 Ridge正则化上一章的岭回归可以从贝叶斯推断角度理解。本章中假设线性回归参数服从正态分布：221exp2 2πjj

j f 

=−  (14)

图8所示为先验分布随 τ变化。τ越大代表越不确信，τ越小代表确信程度越高。τ = 1

τ = 2

τ = 3

τ = 4

τ = 50.

4 2 0 2 4PDF

图8.

先验分布随 τ变化

Page 9 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

(8) 所示的优化问题等价于：20 1 1 2 2

22221111arg max ln exp ln exp22 2π 2πi i i i

nDDDj

ijy x x x    

  == − + + + +   − + −       

θ

(15)

上式目标函数可以分为两部分整理。大家已经清楚，第一部分为：Constant1ln2 2πn −−+yXθ

(16)

第二部分为：Constant1ln2 2πD −+θ

(17)

忽略常数后，(15) 优化问题进一步整理为：22arg max22−−−

θyXθθ (18)

将上式最大化问题调整为最小化问题：22 221arg min2

−+

θyXθθ (19)

令

2= (20)

(19) 等价于：r O r L l S L2 regu a izearg min  −+

θyXθθ

(21)

这和上一章的岭回归优化问题完全一致。《统计至简》第20章介绍过先验的影响力很大

MAP的结果向先验均值 “收缩”。种效果常被称作贝叶斯收缩 (Baye s shrinkage)。根据 (20)

σ保持不变条件下

τ越小代表确信度越高

λ越大，通过 MAP得到的优化解向原点0 (先验均值 ) 收缩。图9上可以看到，优化解随着约束项参数λ不断增大运动轨迹，“收缩”的这种现象显而易见。Page 10 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

λ increasesOLS solution

θ0 θ1

(0, 0)

图9.

不断增大 λ，岭回归优化解变化路径

# 12.5贝叶斯视角理解套索正则化如果先验分布为拉普拉斯分布：1exp2j jjfbb



=− (22)

σ = 1

σ = 2

σ = 3

σ = 4

σ = 5

4 2 0 2 41.0

图10.

先验分布随 b变化

Page 11 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

com (8) 所示的优化问题等价于：0 1 1 2 2

22111arg max ln exp ln2p

2π1ex2i i i i

nDDD

ijjx x x

by

b    

  == − + + + + −+ 

 

 −



θ

(23)

也是分两部分来看上式。第一部分和上一节完全相同：Constant1ln2 2πn −−+yXθ

(24)

第二部分为：# Constant Constant1 11 1ln ln22D

j

jb b b bDD

=− + =− + θ

(25)

忽略常数后，优化问题为：2 11arg max2 b−−−

θyXθθ (26)

最大化问题调整为最小化问题得到：212arg minb−+

θyXθθ (27)

令

b= (28)

(27) 等价于

21arg min −+

θyXθθ (29)

这和上一章套索回归的优化问题的目标函数本质上一致。图11所示为不断增大 λ，套索回归参数变化轨迹；可以发现参数变化轨迹有两段，第一段从

OLS结果为起始点，几乎沿着斜线靠近 y轴 (θ0 = 0)，直至到达 y轴。到达 y轴时，回归系数 θ0为第二段，沿着 y轴朝着原点运动。请大家自己思考从贝叶斯推断视角来看，套索回归的先验概率分布应该是什么？Page 12 | Chapter 12贝叶斯回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

m l@gmail.

λ increasesOLS solution

θ0 θ1

(0, 0)

图11.

不断增大 λ，套索回归优化解变化轨迹贝叶斯回归是一种基于贝叶斯理论的回归分析方法，它不仅考虑了自变量与因变量之间的线性关系，还考虑了模型的不确定性和误差。在贝叶斯回归中，模型的参数被视为概率变量，因此可以通过贝叶斯定理来计算模型参数的后验分布，从而得到对未来数据的预测结果。贝叶斯回归不仅可以有效地避免过拟合和欠拟合等问题还可以处理噪声和缺失数据等复杂情况具有广泛的应用前景。从贝叶斯回归角度理解正则化回归，可以将正则化项视为参数的先验分布。正则化回归通过在损失函数中加入先验分布来约束模型参数的取值范围从而避免过拟合和提高泛化能力。贝叶斯回归中先验分布可以通过经验知识或者领域知识来确定这种方法可以更好地适应实际问题的复杂性和不确定性。因此，正则化回归可以看作是贝叶斯回归在参数估计中的一种特殊情想深入学习贝叶斯推断和贝叶斯回归的读者可以参考开源图书 Bayesian Modeling and

Computation in Python：https:/ /bayesi ancomputationbook.

c om/welcome.

ht ml

Page 1 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 13 Moving Beyon d Linearity

非线性回归寻找因变量和自变量之间关系的非线性模型科学不去尝试辩解，甚至几乎从来不解读；科学主要工作就是数学建模。模型是一种数学构造；基于少量语言说明，每个数学构造描述观察到的现象。数学模型合理之处是它具有一定的普适此外，数学模型一般具有优美的形式 ——也就是不管它能解释多少现象它必须相当简洁。# The sciences do not try to explain

they hardly even try to interpret

they mainly make models.

By a

model is meant a mathematic al constru ct wh ich

with the a ddition of certain verbal interpretations

describes observed phenomena.

The justification of such a mathematic al construct is solely and

precisely that it is expected to work .

—— 约翰·冯·诺伊曼 (John von Neumann) | 美国籍数学家 | 190 3 ~ 1957

◄ matplotlib.

pyplot.

contour 绘制等高线线图

◄ matplotlib.

pyplot.

contourf 绘制填充等高线图

◄ matplotlib.

pyplot.

getp 获绘图对象的属性

◄ matplotlib.

pyplot.

plot_wireframe 绘制线框图

◄ matplotlib.

pyplot.

scatter 绘制散点图

◄ matplotlib.

pyplot.

setp 设置绘图对象的一个或者多个属性

◄ numpy.

random.

normal 产生服从高斯分布的随机数

◄ numpy.

random.

rand 产生服从均匀分布的随机数

◄ numpy.

random.

randn 产生服从标准正态分布的随机数

◄ scipy.

special.

expit

◄ seaborn.

jointplot 绘制联合分布 /散点图和边际分布

◄ seaborn.

kdeplot 绘制概率密度估计曲线

◄ seaborn.

scatterplot 绘制散点图

◄ sklearn.

linear_model.

LinearR egression 最小二乘法回归

◄ sklearn.

linear_model.

LogisticRegression 逻辑回归函数，也可以用来分类

◄ sklearn.

pipeline.

Pipeline 将许多算法模型串联起来形成一个典型的机器学习问题工作流

◄ sklearn.

preprocessing.

FunctionTransformer 根据函数对象或者自定义函数处理样本数据

◄ sklearn.

preprocessing.

PolynomialFeatures 建模过程中构造多项式特征

Page 2 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

非线性回归线性对数模型多项式回归线性 -对数逻辑回归对数 -线性模型概率视角逻辑函数分类一元二元

Page 3 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 13.

1线性回归本书前文介绍过线性回归，白话说，线性回归使用直线、平面或超平面来预测。多元线性回归的数学表达式如下：0 1 1 2 2 ...DD y b b x b x b x  = + + + + + (1)

可以发现 x1

x２,…, xD这几个变量的次数都是一次这也就是 “线性”一词的来由。图1所示为最小二乘法多元线性回归数据关系。y

ε = y ŷ1

x1

x2

ŷ = b 01 + b 1x1 + b 2x2 + .

+ b D-1xD-1 + b DxDx3

xD 1ŷ ε Hyperplane spanned by column vectors

of 1, x1, x2, .

, xD-1 and xD

bD 1

bDb3b2b1b0

图1.

最小二乘法多元线性回归数据关系此外，特征还可以进行线性组合得到一系列新特征：1, 1 2

2 , 1 2

, ,k k k D k D k Dv v v  = + + + =z x x x x x x

(2)

即

 11

1,1 1,

2,1 2,

,1 ,pp

p

p

D

D D pvv

vv

vv    ==   





=



Z z z X X

x x x

(3)

然后可以用最小二乘求解回归系数：1TTˆ−=y Z Z Z Z y (4)

Page 4 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图2所示为线性组合的数据关系得到的模型可以通过 (3) 反推得到基于 x1

x２,…, xD这几个变量的线性模型。本书后续介绍的基于主成分分析的回归方法采用的就是这一思路。ε = y ŷx1

x2

x3

xjz1 = ϕ1(x1, x2, .

, xD)

z2 = ϕ2(x1, x2, .

, xD)

zp = ϕp(x1, x2, .

, xD)ŷ = b 1z1 + b 2z2 + .

+ b pzpy

图2.

特征线性组合线性回归虽然简单，但是并非万能。图3给出的三组数据都不适合用线性回归来描述。就介绍如何采用几种非线性回归方法来解决线性回归不能解决的问题。图3.

线性回归失效的三个例子

13.2线性对数模型本书前文介绍过数据转换一些回归问题可以对输入或输出进行数据转换甚至对两者同时进行数据转换，之后再来构造线性模型。本节介绍几个例子。Page 5 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 观察图4 (a)

容易发下样本数据呈现出“指数”形状而且输出值y大于0；容易想到对输出值

y取对数，得到图4 (b)。而图4 (b) 展现出明显的线性回归特征，便于进行线性回归建模。利用以上思路便可以得到所谓对数 -线性模型：01 lny b b x  = + + (5)

图5所示为通过拟合得到的对数 -线性模型。0100015002000250030003500

y

101102103

ln(y)

1 2 3 4 5 6

x1 2 3 4 5 6

x(a) (b)

图4.

类似“指数”形状的样本数据

0100015002000250030003500

y

101102103

ln(y)

1 2 3 4 5 6

x1 2 3 4 5 6

xFitted

DataFitted

Data

图5.

对数 -线性模型反过来，当数据呈现类似 “对数”形状时 (见图6 (a))

可以对输入 x去对数得到图6 (b)。图6 (b)，可以发现数据展现出一定的线性关系。这样我们就可以使用线性 -对数模型：Page 6 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

01 ln y b b x  = + + (6)

图7所示为得到的线性 -对数模型。1 2 3 4 5 6

x123456

y

123456

y

1002×1004×1006×100

ln(x)(a) (b)

图6.

类似“对数”形状的样本数据

1 2 3 4 5 6

x123456

y

123456

y

1002×1004×1006×100

ln(x)Fitted

DataFitted

Data

图7.

线性 -对数模型此外，我们可以理解同时对输入和输出数据取对数，然后再构造线性回归模型；这种模型叫做双对数模型：01 ln lny b b x  = + + (7)

Page 7 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 需要注意的是，进行对数变换的前提是，所有的观测值都必须大于0。当观测值中存在0或者小于0的数值可以对所有的观测值加 −min( x) + 1

然后再进行对数变换。Bk6_Ch 13_01.

py绘制本节图像。# 13.3非线性回归非线性回归是一种回归分析方法建立自变量与因变量之间的非线性关系模型用于预测连续变量的值。非线性回归需要应对线性回归无法解决的复杂问题。有些情况下，简单的将数据做对数处理是不够的，需要对数据做进一步处理。模型如下所

y f x =+ (8)

f(x) 可以是任意函数，比如多项式函数，逻辑函数，甚至是分段函数。(8) 中 f(x) 可以是多项式得到多项式回归 (polynomial regression)。比如，一元三次多项式回

0 1 2 3y b b x b x b x= + + + (9)

图8所示为一元三次多项式回归模型数据关系。ε = y

ŷŷ = b 1x + b 2x2 + b 3x3y

xb0

f2(x) = x2

f3(x) = x3f1(x) = x

图8.

一元三次多项式回归

Page 8 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图9所示为利用一元三次多项式回归模型来拟合样本数据。下一节，我们将仔细讲解多项式

xyData

Fitted

图9.

一元三次多项式回归模型逻辑回归 (logistic regression ) 也是一种重要的非线性回归模型。一元逻辑回归模型如下：linear model1

1 expy

b b x=



+ − + 

(10)

图10所示为拟合数据得到的逻辑回归模型。图11所示为逻辑回归模型数据关系，逻辑回归模型可以看做时线性模型通过逻辑函数转换得到。xy

图10.

逻辑回归模型

Page 9 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

ε = y ŷŷ y1

s = b 0 + b1x

x b1b0

xf(b0 + b1x)

图11.

逻辑回归数据关系逻辑回归虽然是个回归模型，但是常被用作分类模型，用于二分类。下一章将讲解逻辑回归。此外，我们还可以用分段函数来拟合数据。如图12所示，两段线性函数用来拟合样本数据，效果也是不错的。xyData

Fitted

图12.

分段函数模型非参数回归 (non-parametric regression ) 也是一种非常重要的非线性拟合方法。本章前面介绍的回归模型都有自身的 “参数”

但是非参数回归模型并不假设回归函数的具体形式。参数回归分析时假定变量之间某种关系，然后估计参数；而非参数回归，则让数据本身说话。比如，图13所示为采用最邻近回归 (k-nearest neighbor regression )。最邻近可以用来分类，也可以用来构造回归模型。Page 10 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 鸢尾花书《机器学习》一书讲介绍最邻近方法。xy

图13.

最邻近回归

13.4多项式回归多项式回归是回归分析的一种形式多项式回归是指回归函数的自变量的指数大于1。项式回归中，一元回归模型最佳拟合线不是直线而是一条拟合了数据点的多项式曲线。图14所示为第一到五次一元函数的形状。x

x2x3

x4x5

图14.

一次到五次一元函数自变量 x 和因变量 y 之间的关系被建模为关于 x 的m 次多项式：0 1 2ˆm

m y b b x b x b x= + + + +

(11)

其中，m为多项式函数最高次项系数。图15所示为一元多项式回归数据关系。Page 11 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.《矩阵力量》第9章介绍过采用矩阵运算得到多项式回归系数，请大家回顾。ε = y

ŷŷ = b 0 + b 1z1 + b 2z2 + .

+ b mzmy

xz1 = f1(x) = x

z2 = f2(x) = x2

z3 = f3(x) = x3

zm = fm(x) = xmb0

图15.

一元多项式回归数据关系图16所示为采用一次到四次一元多项式回归模型拟合样本数据。多项式回归的最大优点就是可以通过增加自变量的高次项对数据进行逼近。# Data Fitted

y

xDegree 1

y

xDegree 2

y

xDegree 3

y

xDegree 4

图16.

一元多项式回归，一次到四次

Page 12 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

但是，对于多项式回归次数越高，越容易产生过度拟合 (overfi tting) 问题。过拟合发生的原因是，使用过于复杂的模型，导致模型过于精确地描述训练数据。如图17所示，采用过高次数的多项式回归模型模型过于复杂过度捕捉训练数据中的细节信息甚至是噪音。但是，使用该模型预测其他样本数据时，会无法良好地预测未来观察结果。丛书后续还要深入探讨过拟合问

Data Fitted

y

xDegree 12

y

xDegree 13

y

xDegree 14

y

xDegree 15

图17.

一元多项式回归过度拟合，12次到15次此外，多项式回归可以有多个特征而特征和特征之间可以形成较为复杂的多项式关系。如，下式给出的是二元二次多项式回归：1 2 0 1 1 2 2 3 1 2 4 1 5 2

f x x b b x b x b x x b x b x= + + + + + (12)

(12) 相当于以一定比例组合图18所示的六个平面。提高多项式项次数，可以获得更加复杂的曲线或曲面，这样可以描述更加复杂的数据关系。因此不论因变量与其它自变量的关系如何，一般都可以尝试用多项式回归来进行分析。图19所示为 (12) 所示的数据关系。图18.

六个二元平面 /曲面

Page 13 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

ε = y

ŷŷ = b 0 + b 1z1 + b 2z2 + b 3z3 + b 4z4 + b 5z5y

x1

x2z1 = x 1

z2 = x 2

z3 = x 1x2

z4 = (x1)2

z5 = (x2)2b0

图19.

二元二次多项式回归数据关系

Bk6_Ch 13_02.

py绘制本节图像。# 13.5逻辑回归图20给出一组数据的散点图取值为1的数据点被标记为蓝色取值为0的数据点被标记为图21给出三种可以描述红蓝散点数据的函数。线性函数显然不适合这一问题。阶跃函数虽然可以捕捉函数从0到1的跳变，但是函数本身不光滑。逻辑函数似乎能够胜任描述红蓝三点数据的任务。线性函数的因变量一般为连读数据；辑函数的因变量为离散数值，即分类数据。Page 14 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

图20.

红蓝数据的散点图图21.

可以描述红蓝数据的函数逻辑函数回顾《数学要素》12章讲过的逻辑函数。最简单的逻辑函数：11x

xxefxee−==++ (13)

更一般的一元逻辑函数：1 expfxb b x=+ − + (14)

图22所示为b1影响一元逻辑函数图像的陡峭程度。图中，b0 = 0。可以发现函数呈现 S形，取值范围在 [0, 1] 之间；函数在左右两端无限接近0或1。函数的这一性质，方便从概率角度解释，这是下一节要介绍的内容。Page 15 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

b1 = 1

b1 = 2

b1 = 3

b1 = 4

b1 = 5

-3 -2 -1 0 1 2 300.

-3 -2 -1 0 1 2 300.

b1 = 1b1 = 2b1 = 3b1 = 4b1 = 5

图22.

b1影响一元逻辑函数图像的陡峭程度找到 f(x) = 1/2位置：0111

2 1 expfxb b x==+ − + (15)

整理得到 f(x) = 1/2对应的 x值：1bxb=− (16)

也就是当 b1确定时，b0决定逻辑函数位置。注意，图23中，b1 = 0。3 2 1 0 1 2 3b0 = 2

b0 = 1

b0 = 0

b0 = 1

b0 = 2

图23.

b0决定逻辑函数位置，b1 = 0

图24所示为根据数据的分布，选取不同的逻辑函数参数。Page 16 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

图24.

根据数据的分布，选取不同的逻辑函数参数

Bk6_Ch13_03.

py 绘制逻辑函数图像。多元对于多元情况，逻辑函数的一般式如下：0 1 1 2 21, ,...,1 expD

DDf x x xb b x b x b x=+ − + + +

(17)

利用矩阵运算表达多元逻辑函数：T1

1 expf=+−xbx (18)

其中

 

 T

T

0 1 21D

Dx x x

b b b b=

=x

b

(19)

令

T

0 1 1 2 2 DD s b b x b x b x= = + + +x b x

(20)

(18) 可以记做：1 expfss=+− (21)

(20) 相当于是线性回归，经过如 (21) 逻辑函数映射，得到逻辑回归。图25所示为逻辑回归和线性回归之间关系。图25这幅图已经让我们看到神经网络 (neural network) 的一点影子逻辑函数

f(s) 类似激活函数 (activation function)。特别地，对于二元逻辑函数：Page 17 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0 1 1 2 21,1 expf x xb b x b x=+ − + + (22)

ε = y

ŷŷ = f(bTx)y1

x1

x2

s = bTx

x3

xD

1bD

bDb3b2b1b0

sf(s)

图25.

逻辑回归和线性回归之间关系概率视角形似 (14) 是逻辑分布的 CDF曲线，对应的表达式：1 1 1, tanh2 2 21 expxF x ss x

s−= = + −− +

 (23)

其中，µ为位置参数，s为形状参数。注意，对于逻辑分布，s > 0。逻辑回归可以用来解决二分类，标签为0或1；这是因为逻辑回归可以用来估计事件发生的可能性。标签为1对应的概率为：011Pr 11 exp b b xyx−=+=+ (24)

标签为0对应的概率为：01expPr 0 1 Pr 11 expb b x

b b xy x y x−+= − =+ +==− (25)

Page 18 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图26所示为标签为1和为0的概率关系。y = 0y = 11.

0Probability

x

图26.

标签为1和为0的概率关系显然，对于二分类问题对于任意一点 x

标签为1的概率和标签为0的概率相加为1

P 0 P 1 1y x y x= + = = (26)

白话说，某一点要么标签为1，要么标签为0，如图27所示。81Probability

x

图27.

逻辑回归模型用于二分类问题优势率 (odds ratio

OR )，比值比缩写词为 OR的对数值

01Pr 1 1OR odds ratioexp Pr 0 b b xyx

yx=

− = += = = (27)

分界 OR = 1，两者概率相同：Page 19 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0111exp b b x−+= (28)

整理得到：01 0 b b x+= (29)

即

1bxb=− (30)

本章后文介绍如何用 sklearn中逻辑回归函数解决三分类问题。# 13.6逻辑函数完成分类问题单特征本节介绍用 sklearn.

linear_mod el.

LogisticRegression 逻辑回归模型，根据鸢尾花花萼长度这一单一特征数据进行分类。图28所示为鸢尾花花萼长度数据和真实三分类 y之间关系。# Setosa

y = 0Versicolor

y = 1Virginica

y = 2Real y2

Sepal length, x14 5 6 7 8Setosa, y = 0

Versicolor, y = 1

Virginica, y = 2

图28.

鸢尾花花萼长度和真实分类之间关系图29所示为鸢尾花花萼长度数据分类概率密度估计。这幅图实际上已经能够透露出比较合适的分类区间。Page 20 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0Probability density

Sepal length, x14 5 6 7 8Setosa, y = 0

Versicolor, y = 1

Virginica, y = 2

图29.

鸢尾花花萼长度数据分类概率密度估计

sklearn .

linear_model.

LogisticRe gression 模型结果可以输出各个分类的概率得到的图像如图

30所示。比较三个类别的概率，可以进行分类预测。Sepal length, x14 5 6 7 8Probability1.

0Setosa, y = 0

Versicolor, y = 1

Virginica, y = 2

图30.

逻辑回归估算得到的分类概率图31所示为鸢尾花分类预测结果。Page 21 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Sepal length

x14 5 6 7 8Setosa

ŷ = 0Predicted ŷVirginica

ŷ = 2

Versicolor, ŷ = 1

Setosa, y = 0

Versicolor, y = 1

Virginica, y = 22

图31.

鸢尾花花萼长度和预测分类之间关系

Bk6_Ch13_0 4.

py绘制本节图像。双特征本节介绍用 sklearn.

linear_mod el.

LogisticRegression 逻辑回归模型，根据鸢尾花花萼长度和花萼宽度这两个特征数据进行分类。图32所示为鸢尾花花萼长度和花萼宽度两个特征数据散点图和分类边际分布概率密度估计

Page 22 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Setosa, y = 0

Versicolor, y = 1

Virginica, y = 2

4 5 6 7 8

Sepal length, x1 (cm)4

2Sepal width, x2 (cm)5

图32.

鸢尾花双特征数据和分类边际分布图33 ~ 图35三幅图分别给出鸢尾花双特征分类概率预测曲面。比较三个曲面高度可以得到分类决策边界。在分类问题中决策边界 (decision boundar y) 指的是将不同类别样本分开的平面或

Sepal length, x1Sepal width, x21.

图33.

鸢尾花双特征分类预测，ŷ = 0

Page 23 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Sepal length, x1Sepal width, x21.

图34.

鸢尾花双特征分类预测，ŷ = 1

Sepal length, x1Sepal width, x21.

图35.

鸢尾花双特征分类预测，ŷ = 2

2Sepal width

x2 (cm)Setosa

C1 Versicolor

C2 Virginica

4 5 6 7 8

Sepal length, x1 (cm)

Page 24 | Chapter 13非线性回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https: //spac e.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图36.

利用逻辑回归得到的分类决策边界

Bk6_Ch13_0 5.

py绘制本节图像。非线性回归是一种用于建模非线性关系的统计方法。在非线性回归中，因变量和自变量之间的关系不是线性的，而是可以通过非线性函数来描述。需要非线性回归的原因是许多自然现象和实际问题都不是线性的例如，随着时间的推移人口增长率和经济增长率并不是线性的，这就需要非线性回归模型。常见的非线性回归方法包括多项式回归指数回归、对数回归幂函数回归、逻辑回归每种方法都有其优缺点，例如多项式回归可以拟合大部分的非线性关系，但容易出现过拟逻辑回归将自变量和因变量之间的关系建模为一种逻辑函数，如 sigmoid函数。从概率视角来看，逻辑回归可以将输出解释为给定输入的条件下，观察到给定类别的概率。它将自变量映射到一个概率值，该值介于0和1之间，并使用这个概率来预测分类结果。欢迎读者阅读 An Introduction to Statistical Learning

With Applicati ons in R一书第七章下载地址。https ://www .

statlearning.

c om/

Page 1 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 15 Principal Component Analysis

主成分分析处理多维数据，通过降维发现数据隐藏规律忽视数学会损害所有知识，因为不了解数学的人无法了解世界上的其他科学或事物。更糟糕的是，那些无知的人无法感知自己的无知，因此不寻求补救。Neglect of mathematics work injury to all knowledge

since he who is ignorant of it cannot know the

other sciences or things of this world.

And what is worst

those w ho are th us ign orant are unable to

perceive their own ignorance

and so do not seek a remedy.

—— 罗吉尔·培根 (Roger Bacon ) | 英国哲学家 | 1214 ~ 1294

◄ numpy.

corrcoef 计算相关性系数矩阵

◄ numpy.

cov 计算协方差矩阵

◄ numpy.

linalg.

eig 特征值分解

◄ numpy.

linalg .

svd 奇异值分解

◄ numpy.

mea n 计算均值

◄ numpy.

random.

multivariate_normal 产生多元正态分布随机数

◄ numpy.

std 计算均方差

◄ numpy.

var 计算方差

◄ numpy.

zeros_like 产生形如输入矩阵的全0矩阵

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

jointplot 绘制联合分布和边际分布

◄ seaborn.

kde plot 绘制KDE核概率密度估计曲线

◄ seaborn.

lineplot 绘制线图

◄ seaborn.

pairplot 绘制成对分析图

◄ sklearn.

decomposition.

PCA 主成分分析函数

◄ yellowbrick.

features.

PCA 绘制PCA双标图

Page 2 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

一般步骤特征值分解特征值排序，确定主成分降维投影视角线性组合投影视角椭圆视角奇异值分解，四种类型协方差矩阵数据还原与误差可视化主成分分析双标图陡坡图

Page 3 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 15.

1原始数据主成分分析主成分分析 (principal c omponent analysis

PCA) 最初由卡尔·皮尔逊 (Karl Pearson) 在1901提主成分分析是数据降维的重要方法之一。通过线性变换，主成分分析将原始多维数据投影到一个新的正交坐标系，将原始数据中的最大方差成分提取出来。卡尔 ·皮尔逊 (Karl Pearson )

英国数学家 | 1857 ~ 1936

常被誉为现代统计科学的创立者；丛书关键词：相关性系数线性回归主成分分析举个例子，主成分分析实际上寻找数据在主元空间内投影。图1所示杯子，它是一个3D物体，在一张图展示杯子而且尽可能多地展示杯子细节就需要从空间多个角度观察杯子并找到合适角度。这个过程实际上是将三维数据投影到二维平面过程。这也是一个降维过程，即从三维变成二维。图2展示杯子六个平面上投影结果。H1

H2

H3H4

H5H6

图1.

咖啡杯六个投影方向

Page 4 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

H1

H2

H3H4

H5H6

图2.

咖啡杯在六个方向投影图像以鸢尾花数据为例本章以鸢尾花数据为例介绍如何利用主成分分析处理数据。图3所示为鸢尾花原始数据矩阵 X

构成的热图。数据矩阵 X有150个数据点，即150行；矩阵 X有4个特征，即4列。02468

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x4150 data points

图3.

鸢尾花数据，原始数据矩阵 X

Page 5 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 对原始数据进行统计分析。首先以行向量表达数据矩阵X质心：1 2 3 4 Sepal length

Sepal width

Petal length

Petal width

843 3.

057 3.

758 1.

x x x x=

Xμ (1)

µ6

图4.

鸢尾花数据四个特征上均值然后，计算 X每一列均方差，以行向量表达：1 2 3 4 Sepal length

Sepal width

Petal length

Petal width

825 0.

434 1.

759 0.

x x x x=

Xσ (2)

X第三个特征，也就是花瓣长度 x3对应的均方差最大。图5所示为 KDE估计得到的鸢尾花四个特征分布图。µx1 = 5.

843, σx1 = 0.

825µx2 = 3.

057, σx2 = 0.

µx3 = 3.

758, σx3 = 1.

759µx4 = 1.

199, σx4 = 0.

0 2 4 6 80.

0Probability densitySepal length, x1

Sepal width, x2

Petal length, x3

Petal width, x4

图5.

鸢尾花数据四个特征上分布，KDE估计利用 seabo rn.

pairplot 函数可以绘制如图6所示成对特征分析图；成对特征分析图方便展示每一对数据特征之间的关系，而对角线图像则展示每一个特征单独的统计规律。由于鸢尾花数据存在三个分类，所以可以利用 seabo rn.

pairplo t 函数展示具有分类特征的成对分析图，具体如图7所示。图7这幅图让我们看到了每一类别数据特征之间和自身的分布规

Page 6 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

x4Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

图6.

鸢尾花数据成对特征分析图，不分类

Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

x4Sepal length

x1 Sepal width

x2 Petal length

x3 Petal width

x4Virginica Versicolor Setosa

Page 7 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图7.

鸢尾花数据成对特征分析图，分类计算数据矩阵 X协方差矩阵 Σ：1 3 4 21

Sepal length

Petal length

Petal width

Sepal width

686 0.

042 1.

274 0.

# 0.042 0.190 0.330 0.122

# 1.274 0.3a

30 3.e

116 1.296

# 0.516 0.122 1.S pal length,

Se

9p

8l width

2 6 0 5 1

x x x xx

x

 =





−

−

− − −

− Σ

4Petal length,

Petal width, x

x

 (3)

接下来，协方差矩阵Σ将用于特征值分解。在PCA中，有时候会对数据进行标准化是因为不同特征的单位和尺度不同可能会对 PCA

的结果产生影响。如果不进行标准化处理，那么在协方差矩阵的计算过程中，某些特征的方差较大，将会对 PCA的结果产生更大的影响，而这些特征不一定是最重要的。因此，为了消除这种影响，我们需要对数据进行标准化处理。标准化的目的是将不同特征的值域缩放到相同的范围使得所有特征的平均值为0

为1，从而消除不同特征间的单位和尺度差异，使得所有特征具有相同的重要性。原始数据标准化的结果是 Z分数。Z分数的协方差矩阵实际上是原始数据的相关性系数矩阵。总结来说，在进行 PCA之前如果数据中的特征具有不同的度量单位或者特征值的范围变化很大，那么就应该考虑进行标准化。标准化可以使得 PCA的结果更加准确和可靠，避免某些特征在主成分分析中被过度强调或者忽略。但是需要注意的是，有些情况下，标准化并不适用于所有数据集，例如当数据中的特征已经被精心设计或处理过时标准化可能会使得信息损失或降低

PCA的效果。计算数据矩阵X相关性系数矩阵 P：1 3 4 21

Sepal length

Petal length

Petal width

Sepal width

000 0.

118 0.

872 0.

# 0.118 1.000 0.428 0.366

# 0.872 0.4a

28 1.e

000 0.963

# 0.818 0.366 0.S pal length,

Se

6p

0l width

9 3 1 0 0

x x x xx

x

 =





−

−

− − −

− Ρ

4Petal length,

Petal width, x

x

 (4)

观察相关性系数矩阵 P

可以发现花萼长度 x1和花萼宽度 x2线性负相关花瓣长度 x3和花萼宽度 x2线性负相关，花瓣宽度 x4和花萼宽度 x2线性负相关。# 15.2特征值分解对Σ特征值分解得到：1−=Σ VΛV (5)

其中，V是正交矩阵，满足 VVT = I。实际上 Σ为对称矩阵，因此上式为谱分解，即

T=Σ VΛV。Page 8 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 特征值矩阵Λ为：023



=



Λ (6)

特征向量构成的矩阵 V为： 1 2 3 4

1,1 1,2 1,3 1,41

2,1 2,2 2,3 2,4 2

3 3,1 3,2 3,3 3,4

4 4,1 4,2 4,3 4,40.

361 0.

656 0.

582 0.

315Sepal length,

# 0.084 0.730 0.597 0.319Sepal width,

0Petal length,

Petal width, v v v v x

v v v v x

x v v v v

x v v v v=

−− 

 − ==

 V v v v v

13 24PC1, PC3, PC2, PC4, .856 0.173 0.076 0.479

# 0.358 0.075 0.545 0.753





 −

−−

vv vv

(7)

矩阵 V每一列代表一个主成分该主成分中每一个元素相当于原始数据特征的系数。图8所示为不同主成分的系数线图。# Sepal length

x1Sepal width

x2Petal length

x3Petal width

x40.

8PC1, v1PC3, v3

PC4, v4PC2, v2Coefficients

图8.

V系数线图如图9所示，V和自己转置 VT乘积为单位阵 I，即：T= V V I (8)

展开上式得到：Page 9 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

   T

T

T2

1 2 3 4 1 2 3 4 1 2 3 4 T

T

T T T T

1 1 1 2 1 3 1 4

T T T T

2 1 2 2 2 3 2 4

T T T T

3 1 3 2 3 3 3 4

T T T T

4 1 4 2 4 3 4 41 0 0 0

0 1 0 0

0 0 1 0

0 0 0 1



=





 

 

  = = = 

 

 v

vv v v v v v v v v v v vv

v

v v v v v v v v

v v v v v v v vIv v v v v v v v

v v v v v v v v (9)

Sepal length, x1

Sepal width, x2

Petal length, x3

Petal width, x4

PC1, v1

PC2, v2

PC3, v3

PC4, v4

V @ VT= ISepal length, x1

Sepal width, x2

Petal length, x3

Petal width, x4

# 1.0 0.5 0.0 0.5 1.0

图9.

特征矩阵 V和自身转置的乘积为单位矩阵I

如果对鸢尾花数据先进行标准化处理，即使用每一列变成Z分数；再计算得到的矩阵 V则

12 341

PC1, PC2, PC3, PC4, Sepal length,

Sepal width,

Petal length,

Petal width, 0.

521 0.

377 0.

720 0.

# 0.269 0.923 0.244 0.124

# 0.580 0.024 0.142 0.801

# 0.565 0.067 0.634 0.524x

x

x

 =  

−

−−

−

−−

vv vvV

4x (10)

可以发现 (7) 和 (10) 明显不同，下一章将对比这两种技术路线。# 15.3正交空间矩阵 V有D个列向量，对应D个正交基，如下：Page 10 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

 1,1 1,2 1, 1 1,

2,1 2,2 2, 1 2,

1 2 1

1,1 1,2 1, 1 1,

,1 ,2 , 1 ,.

DD

DD

D D D D D D

D D D D D Dv v v v

v v v v

v v v v

v v v v−

−

−

− − − − −

−





==





V v v v v

(11)

任意列向量 vi每一个元素都包含X列向量 [x1, x2, .

, xD] 成分，即列向量 vi为 [x1, x2, .

, xD] 线性组合。1 1,1 1 2,1 2 1,1 1 ,1

2 1,2 1 2,2 2 1,2 1 ,2

1, 1 2, 2 1, 1 ,.

D D D D

D D D D

D D D D D D D D Dv v v v

v v v v

v v v v−−

−−

−−= + + + +

= + + + +

= + + + +v x x x x

v x x x x

v x x x x (12)

图10所示为线性组合构造正交空间 [v1, v2, .

, vD]。注意，[x1, x2, .

, xD] 类似于 [e1, e2, .

, eD]，它们代表方向向量，而不是具体的数据。# Orthogonalize

x1

x2

x3

xD 1v1

v2

v3

vD 1x1x2.

v1v2.

vDx1x2xD

v1v2vD

图10.

线性组合构造正交空间 [v1, v2, .

, vD]

如图11所示以v1为例，第一主成分方向上

v1等价于由v1

1比例x1，v2

1比例x2，v3

以及 vD,1比例 xD线性组合构造。从另外一个角度，[x1, x2, .

, xD] 在向量v1上标量投影值分别为v1,1, v2,1, .

, vD,1。图12所示为鸢尾花数据主成分分析第一主成分 v1的构造情况。Page 11 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Project

x1

x2

x3

xD 1v1

x1x2.

vD 1,1

vD,1v4,1v3,1v2,1v1,1

v1

v1,1

v2,1

vD,1.

图11.

构造第一主成分 v1

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x40.

8PC1, v1v1,1 = 0.

v2,1 = 0.

084v3,1 = 0.

v4,1 = 0.

358Coefficients

图12.

构造第一主成分 v1，鸢尾花数据如图13所示第二主成分 v2方向上

v2等价于由v1

2比例x1，v2

2比例x2，v3

2比例 x3.

vD,2比例 xD线性构造。图14所示为鸢尾花数据主成分分析第二主成分 v2的构造情况。Page 12 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Project

x1

x2

x3

xD

1v2x1x2.

vD

vD,2v4,2v3,2v2,2v1,2

v2

v1,2

v2,2

vD,2.

图13.

构造第二主成分 v2

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x40.

8PC2, v2v1,2 = 0.

656v2,2 = 0.

v3,2 = 0.

173 v4,2 = 0.

075Coefficients

图14.

构造第二主成分 v2，鸢尾花数据如图15所示第三主成分 v3方向上

v3等价于由v1

3比例x1，v2

3比例x2，v3

3比例 x3.

vD,3比例 xD线性构造。图16所示为鸢尾花数据主成分分析第三主成分 v3的构造情况。Page 13 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Project

x1

x2

x3

xD

1v3x1x2.

v3

v1,3

v2,3

vD,3.

vD

vD,3v4,3v3,3v2,3v1,3

图15.

构造第三主成分 v3

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x40.

8PC3, v3

v1,3 = 0.

582v2,3 = 0.

v3,3 = 0.

076v4,3 = 0.

545Coefficients

图16.

构造第三主成分 v3，鸢尾花数据

Page 14 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 15.

4投影结果图17所示为投影后得到的新特征数据矩阵 Z。这幅热图，蓝色色系数据接近0，红色色系数据接近8；可以发现矩阵 Z四个新特征 (z1

z2, z3和z4) 从左到右颜色差异逐渐减小即方差不断减

02468

PC1, z1 PC2

z2 PC3

z3 PC4

z4150 data points

图17.

新特征数据矩阵 Z

对转换数据 Z进行统计分析，以行向量表达数据矩阵 Z质心：1 2 4 3PC1, PC2, PC4, PC3, 5.

502 5.

326 0.

631 0.

z z z z

=−

Zμ

(13)

数据矩阵 Z质心和原始数据矩阵 X质心之间的关系如下所示：1 2 3 4

12 3Sepal length

Sepal width

Petal length

Petal width

PC1, PC2, PC3, 0.

521 0.

377 0.

720 0.

# 0.269 0.923 0.244 0.124

# 0.580 0.024 0.142 0.801

# 0.565 0.067 0.635.843 3.057 3.758 1.199

4x x x x−

−−

−

−−=

=

ZX

vv vμ μ V

1 2 4 3PC4,

PC1, PC2, PC4, PC3, 0

2 5.502 5.3 6 ..52

# 0.631 033

z z z z















=−

v

(14)

Page 15 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

注意，若使用 sklearn.

dec omposition.

PCA 函数进行主成分分析，则会发现数据矩阵Z质心均为0；这是因为数据已经标准化。Z每一列均方差，以行向量表达：1 2 3 4 PC1, PC2, PC3, PC4, 2.

056 0.

492 0.

279 0.

z z z z=

Zσ (15)

Z每一列方差，以行向量表达：1 2 3 42

PC1, PC2, PC3, PC4, 4.

228 0.

242 0.

078 0.

z z z z=

Zσ (16)

图18所示为KDE估计得到的转换数据 Z四个特征分布图。PC1, z1

PC2, z2

PC3, z3

PC4, z4

µz1 = 5.

502, σz1 = 2.

056µz2 = 5.

326, σz2 = 0.

492µz3 = 0.

631, σz3 = 0.

279µz4 = 0.

033, σz4 = 0.

0PDF2.

0 2 4 6 8 10 12 2

图18.

转换数据 Z四个特征上分布，KDE估计作为对比，图19所示为已经中心化的数据 Xc朝V投影的结果。对比图18和图19，我们可以发现方差没有变化。唯一的区别是，图19中所有特征的均值均为0。注意，V是通过对协方差矩阵特征值分解得到的。Page 16 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

PC1

PC2

PC3

PC4

6 4 2 0 2 4 60.00.51.01.52.03.0PDF2.5

图19.

转换数据 Z四个特征上分布，KDE估计；数据已经中心化图20所示为转换数据 Z协方差矩阵和相关性系数矩阵热图。图21所示为不分类条件下，转换数据 Z成对特征分析图；根据本节计算结果，可以知道转换数据 Z任意两列数据之间的线性相关性系数为0，也就是正交。图22所示为分类条件下，转换数据Z成对特征分析图。Z的协方差矩阵 ΣZ和X的协方差矩阵 ΣX之间关系如下：Tvar==X X ΣV X ΣV (17)

图20所示为转换数据 Z协方差矩阵和相关性系数矩阵热图。有关协方差运算，请大家回顾《统计至简》第14章。PC1, z1PC2

z2PC3, z3PC4

z4 PC1

z1PC2, z2PC3

z3PC4, z4PC1

PC2, z2

PC3, z3

PC4, z4PC1, z1

PC2, z2

PC3, z3

PC4, z44.

0231

1(a) covariance matrix of Z (b) correlation matrix of Z

图20.

转换数据 Z协方差矩阵和相关性系数矩阵热图

Page 17 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 图21所示为不分类条件下，转换数据 Z成对特征分析图；根据本节计算结果，可以知道转换数据 Z任意两列数据之间的线性相关性系数为0，也就是正交。图22所示为分类条件下，转换数据Z成对特征分析图。下一章还会用椭圆代表散点的分布情况。PC1, v1 PC2

v2 PC3

v3 PC4

v4PC1, v1 PC2

v2 PC3

v3 PC4

图21.

转换数据 Z成对特征分析图，不分类

Page 18 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

PC1, v1 PC2

v2 PC3

v3 PC4

v4PC1, v1 PC2

v2 PC3

v3 PC4

v4Virginica Versicolor Setosa

图22.

转换数据 Z成对特征分析图，分类

15.5还原主成分 v1和v2上的投影结果可以用来还原部分原始数据。残差数据矩阵E，即原始热图和还原热图色差，利用下式计算获得：ˆ=−Ε X X (18)

图23所示为 z1还原 X部分数据。图24所示为 z1还原 X部分数据。图25所示为 [z1, z2] 还原

X部分数据。比较原始数据和图25所示 [z1

z2] 还原 X部分数据可以得到误差热图如图26所

Page 19 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

02468

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x4150 data points

图23.

z1还原 X部分数据

02468

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x4150 data points

图24.

z2还原 X部分数据

Page 20 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

02468

Sepal length

x1Sepal width

x2Petal length

x3Petal width

x4150 data points

图25.

[z1, z2] 还原 X部分数据

02468

Sepal length,

x1Sepal width

x2Petal length

x3Petal width

x4150 data points

图26.

误差 E

Page 21 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 15.

6双标图双标图 (biplot) 是主成分分析中常用的可视化方案。它能够将高维数据投影到二维或三维空间中，并用散点图的形式展示出来，同时还能够显示原始数据和主成分的信息。一般情况，平面双标图的横坐标和纵坐标分别表示 PCA的前两个主成分，每个点代表一个样本数据。通过观察双标图，可以发现不同样本之间的相似性和差异性。如果两个点在双标图上非常接近，那么它们在原始数据中的特征值也可能非常接近，反之亦然。同时，双标图还能够帮助我们找出数据中的异常值和离群点，这些点在双标图上往往会距离其他点较远。除了用于可视化，双标图还能够用来评估 PCA的效果。如果双标图中的数据点分布较为均匀且没有聚集在一起，那么说明 PCA的效果较好，主成分能够较好地解释数据的方差；如果双标图中的数据点呈现出聚集或者明显的分块现象那么说明 PCA的效果可能不太理想主成分并不能完全解释数据的方差。如图27所示，双标图相当于原始数据特征向量向主成分构造的平面投影结果。比如，x1向量向v1-v2平面投影

x1在v1方向投影得到的标量值为 v1

1，x1在v2方向投影得到的标量值为 v1

两个值对应 V矩阵第一行前两列数值。v1v2Plane spanned by v1 and v2x1

v1,1v1,2Sepal length, x1

Sepal width, x2

Petal length, x3

Petal width, x4V

v1,1 v1,2

图27.

双标图原理图28所示为鸢尾花原始数据 PCA分解后得到的双标图。该图横纵坐标分别是第一主成分 v1和第二主成分 v2。如图28所示在双标图上，如果两个特征向量夹角越小说明两个特征相似度越高，也就是相关性系数越高。比如图中，花萼长度 x3和花萼宽度 x4，在双标图上几乎重合，说明两者相关性极高，(4) 中给出的两者相关性高达0.

963，这也印证了这一点。Page 22 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Sepal width, x2

Sepal length, x1

Petal length, x3

Petal width, x4

PC1, v10 1

1PC2, v2

图28.

v1-v2平面双标图，基于鸢尾花原始数据图29所示为向量 x1

x2、x3和x4向v1-v2平面投影结果和矩阵 V之间的数值关系。x1

v1v2x2

v1v2

x3

v1v2x4

v1v2

v1,1 = 0.

361v1,2 = 0.

v2,1 = 0.

084v2,2 = 0.

v3,1 = 0.

v3,2 = 0.

173v4,1 = 0.

v4,2 = 0.

075v1,1v1,2

v2,1v2,2

v3,1v3,2

v4,1v4,2

图29.

向量 x1、x2、x3和x4向v1-v2平面投影结果图30所示为向量 x1、x2、x3和x4向v3-v4平面投影结果。Page 23 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

Sepal width

x2Sepal length

x1Petal width

Petal length, x3

PC3, v30 1 1PC4, v3

图30.

v3-v4平面双标图，基于鸢尾花原始数据双标图还可以基于标准化后数据；图31所示为基于鸢尾花标准化数据后的双标图，投影值对应 (10)。Sepal width, x2

Sepal length, x1

Petal width, x4

Petal length, x3

PC1, v10 1 1PC2, v2

图31.

平面双标图，基于鸢尾花标准化数据

Page 24 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 此外，除了特征向量之外，双标图还会绘制数据点投影，如图32所示。图32采用

yellowbrick.

fe atures.

PCA 绘制。该函数绘制的双标图基于标准化鸢尾花数据。双标图中，点与点之间的距离，反映它们对应的样本之间的差异大小，两点相距较远，对应样本差异大；两点相距较近，对应样本差异小，存在相似性。PC1, v1PC2

v2Virginica Versicolor Setosa

Sepal width, x2

Sepal length, x1

Petal length, x3Petal width, x4

图32.

平面双标图，标准化数据图33给出的是由前三个主成分构造的空间也就是将原始数据和它的四个特征向量投影到这个三维正交空间。该图也是采用 yellowbri ck.

features.

PCA 绘制。Sepal width, x2

Sepal length

x1Petal length

x3Petal width

x4PC3, v3Virginica Versicolor Setosa

图33.

三维双标图

Page 25 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

# 15.7陡坡图《统计至简》第25章介绍过，第j个特征值λj 对方差总和的贡献百分比为：1100%j

D

i

i



=

 (19)

上式分母是数据总方差。协方差矩阵 Σ的迹——方阵对角线元素之和——等于特征值之和，请大家回顾《统计至简》第13章。(19) 这个比值可以用来衡量第 j个主成分对数据的解释能力。如果已释方差较大，那么说明第j个主成分能够较好地解释数据的方差，即它包含了较多的信息。如果已释方差较小，那么说明第 k个主成分对数据的解释能力较弱，不足以对数据进行有效的降维和特征提取。前p个特征值累积解释总方差的百分比为：1100%p

j

j

D

i

i

=

=

 (20)

这个比值代表前 p个主成分所能解释的已释方差之和占所有主成分已释方差之和的比例。计已释方差和百分比能够用来评估 PCA的降维效果它衡量了前 p个主成分能够解释数据方差的通常来说，我们希望通过选择适当的主成分数 p

使累计已释方差和百分比达到预设的阈值

(比如80%或90%)，以保留尽可能多的原始数据信息。通过观察累计已释方差和百分比的变化趋势，我们可以得出选择适当主成分数的建议，以及对 PCA的降维效果进行评估和比较。图34给出图像可视化 (19) 和 (20)。鸢尾花数据的主成分分析特征值如下：1 2 3 4=4.228, =0.242, =0.078, =0.023    (21)

PCA主成分顺序根据各个主成分维度方向方差贡献大小排序。第一主成分方向上的方差最大，也就是这个方向最有力地解释了数据的分布。当第一主成分的方差贡献不足 (比如小于

50%)，我们就要依次引入其它主成分。如图34所示，第一和第二主成分两者已释方差之和为

Page 26 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

λ1 = 4.

λ2 = 0.

9776

Principal componentsPC2

z2 PC3

z3 PC4

z4 PC1

z14.

Variance

λCumulative variance explained (%)0.

图34.

Bk6_Ch 15_01.

py绘制本章前文大部分图片。# 15.8分析鸢尾花照片本节用 PCA分析一章鸢尾花照片。图35所示为作者拍的一章鸢尾花照片，经过黑白化处理后的每个像素都是 [0, 1] 范围内的数字。所以整幅图片可以看成一个数据矩阵。《可视之美》一册专门介绍过彩色和黑白图像之间转换。Page 27 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

0 500 1000 1500 2000 2500

图35.

鸢尾花图片，经过黑白处理图36所示为利用 SVD分解得到的奇异值随主成分变化。图37所示为特征值随主成分变化。38所示为累积解释方差百分比随主成分变化。我们可以发现前10个主成分已经解释超过90%的方

100101102103

Principal component1200

0Singular value

图36.

奇异值随主成分变化

Page 28 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

100101102103

Principal component500

0Eigen value

图37.

特征值随主成分变化

100101102103

Principal component94

85Cumulative variance

explained (%)100

图38.

累积解释方差百分比随主成分变化图39所示为利用第1主元还原鸢尾花图片，左图为还原结果，右图为误差。左图中，鸢尾花还难觅踪影。图40所示为利用第1

2主元还原鸢尾花照片图41所示为利用前4个主元还原鸢尾花照片，在两幅图的左图中我们仅仅能够看到 “格子”。图42的左图利用前16个主元还原照片，我们已经能够看到鸢尾花的样子，注意这幅图的秩为16。图43所示为利用前64个主元还原鸢尾花图片，图形已经很清晰。相比原图片，图43的数据发生大幅压缩。这种利用 PCA进行图像降维方法用途很广泛。比如，在人脸识别中，特征脸 (eigenface ) 是一种基于 PCA的特征提取方法，用于将人脸图像转换成低维特征向量进行分类或识别。特征脸是指由PCA分解出来的主成分图像它们是一组基于训练数据集的线性组合每个特征脸表示了一个数据集中的特定方向，可以看作是数据集的主要特征或重要性征。特征脸的提取过程可以分为以下几步

1) 对人脸图像进行预处理比如灰度化、尺度归一化、去除噪声等。2) 将预处理后的图像转换成向量形式。3) 将向量集合进行 PCA降维，得到一组主成分向量，也就是特征脸。4）将人脸图像向量投影到主成分向量上，得到每个人脸的特征向量表示。特征脸在人脸识别中的作用是对人脸图像进行有效的特征提取和降维使得原始图像数据被压缩到一个低维空间中，并且保留了原始数据中的大部分信息。通过比较人脸图像的特征向量之间的相似度，可以进行人脸识别、验证等应用。Page 29 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

X reproduced with 1 PC Error

0 1000 20000

0 1000 2000

图39.

利用第1主元还原鸢尾花照片

X reproduced with 2 PCs Error

0 1000 20000

0 1000 2000

图40.

利用第1、2主元还原鸢尾花照片

X reproduced with 4 PCs Error

0 1000 20000

0 1000 2000

图41.

利用第1、2、3、4主元还原鸢尾花照片

Page 30 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

X reproduced with 16 PCs Error

0 1000 20000

0 1000 2000

图42.

利用前16个主元还原鸢尾花照片

X reproduced with 64 PCs Error

0 1000 20000

0 1000 2000

图43.

利用前64个主元还原鸢尾花照片

Bk6_Ch 15_02.

py绘制本节图片。鸢尾花照片也在文件夹中。主成分分析是一种广泛使用的数据降维和特征提取技术它可以将高维数据降至低维保留数据的主要特征和结构。PCA通过寻找一组最能解释数据变异性的线性组合，即主成分，来实现数据降维和特征提取。主成分是原始特征的线性组合，它们的排序代表了它们的重要性。常，我们只需要保留前几个主成分，因为它们可以解释大部分数据的变异性。Page 31 | Chapter 15主成分分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://github.

com/Visualize -ML

本书配套微课视频均发布在 B站——生姜 DrGinger

https://space.

bilibili.

com/513194466

欢迎大家批评指教，本书专属邮箱：jiang.

visualize.

ml@gmail.

com 一般的 PCA步骤包括中心化 (标准化 ) 数据计算协方差矩阵计算特征值和特征向量排序特征值和对应的特征向量、选择前 p个主成分、计算投影矩阵并对数据进行降维。在计算特征值和特征向量时我们通常使用特征值分解当然也可以使用奇异值分解这是下一章要介绍的内容。PCA的投影可以帮助我们理解数据的结构和关系。投影到第一二主成分方向上的投影数据通常成椭圆形状，其中椭圆的长轴方向表示最大的方差方向，短轴方向表示最小的方差方向。线性组合，我们可以将主成分重新组合成原始数据并通过双标图和陡坡图来分析 PCA的效果。双标图可以帮助我们了解主成分之间的相关性陡坡图可以帮助我们了解主成分的贡献程度。在PCA中，理解数据和分析结果的视角非常重要。这涉及到如何选择主成分和如何解释它们，以及如何应用 PCA的结果。选择主成分时，我们通常考虑主成分的贡献程度和解释能力，以及降维后的数据能否保留足够的信息。解释主成分时，我们需要考虑主成分的物理意义和应用背应用 PCA的结果时，我们可以利用降维后的数据进行可视化、聚类、分类等分析。总之，主成分分析是一种强大的数据降维和特征提取技术，它可以帮助我们更好地理解和分析数据。在应用 PCA时，需要注意数据预处理、主成分选择和解释、以及降维后的数据应用等问下一章将比较六种不同的 PCA技术路线。Page 1 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 15 Dive into Princi pal Component Analysis

主成分分析进阶区分六条基本 PCA技术路线我发现了 !

Eureka!

—— 阿基米德 (Archimedes) | 数学家发明家、物理学家 | 287 ~ 212 BC

◄ numpy.

cov 计算协方差矩阵

◄ numpy.

linalg.

e ig 特征值分解

◄ numpy.

linalg.

svd 奇异值分解

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

kdeplo t 绘制KDE核概率密度估计曲线

◄ seaborn.

pairplot 绘制成对分析图

◄ sklearn.

decomposition.

PCA 主成分分析函数

Page 2 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

六条PCA路线SVD

格拉姆矩阵协方差矩阵相关性系数矩阵标准化数据矩阵中心化数据矩阵原始数据矩阵

EVD

Page 3 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 15.

1从“六条技术路线 ”说起来自《矩阵力量》的表格表1来自《矩阵力量》第25章本章将讲解表1中六条 PCA技术路线的细节并比较它们的表1.

六条PCA技术路线，来自《矩阵分解》第25章对象方法结果原始数据矩阵 X 奇异值分解 X = UXSXVXT

格拉姆矩阵 G = XTX

本章中用 “修正”的格拉姆矩阵

T

1n−XXG= 特征值分解 G = VXΛXVXT

中心化数据矩阵

Ec=−X X X 奇异值分解 Xc = UcScVcT

协方差矩阵

TEE

1n−−

−X X X XΣ= 特征值分解 Σ = VcΛcVcT

标准化数据 (z分数 )

diag diagE−

==−XZ X X D

D Σ 奇异值分解 ZX = UZSZVZT

相关性系数矩阵

2 diag diag−−=

=PDΣD

D Σ 特征值分解 P = VZΛZVZT

比较六个输入矩阵表1中有六个输入矩阵，它们都衍生自原始数据矩阵 X。如图1所示，原始数据矩阵 X的形状为n × D。Page 4 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

数据的两个视角行向量 x(i)

列向量 xj

两个方阵格拉姆矩阵 G

余弦相似度矩阵 C

统计视角质心 E(X)

中心化数据 Xc

协方差矩阵 Σ

相关性系数矩阵 P标准化数据 ZXX

µX

n × D

n × D

n × DD × D

D × D

1 × D

D × 1

D × D

D × D

图1.

X衍生得到的几个矩阵，来自《矩阵力量》X的格拉姆矩阵 G为：T=G X X (1)

格拉姆矩阵 G形状为 D × D。G的主对角线元素是 X的每一列向量 L2模的平方。中心化 (去均值 ) 矩阵 Xc为：Ec=−X X X (2)

即X的每一列分别减去各自的均值得到 Xc。几何角度，X的质心位于 E(X)，Xc的质心则位于原点0。样本数据矩阵 X的协方差矩阵Σ为：# TTEE

11cc

nn−−

==−−X X X X XXΣ (3)

Page 5 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 容易发现，协方差相当于特殊的格拉姆矩阵。请大家特别注意，为了方便和协方差比较，本章中G特别定义为：T

1n=−XXG (4)

标准化 (stand ardization或z-score normalization ) 数据矩阵 ZX为

1E−=−XZ X X D (5)

其中 D为：22 diag diag

D







=



=D Σ

(6)

(5) 中的每一列都是每个特征的 Z分数。ZX的质心也位于原点，不同的是 ZX每个特征的标准差都是1。线性相关性系数矩阵 P为：11−−=PDΣD (7)

P实际上是 ZX的协方差，即：T

1n=−XXZZP (8)

比较SVD和EVD

主成分分析的核心数学工具为奇异值分解 (Sing ular Value Decomposition

SVD) 和特征值分解

(Eigen Decomposition, EVD)。《矩阵力量》强调过 SVD和EVD在主成分分析中具有等价性这也就是为什么表1看上去是六种技术路线，实际上可以归纳为三大类技术路线。下面简单说明一下。对原始矩阵 X进行经济型 SVD分解：T=X X X X U S V (9)

其中，SX为对角方阵。将 (9) 代入 (1)：2T=X X X G V S V (10)

上式便是格拉姆 G的特征值分解。Page 6 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 对中心化数据矩阵 Xc经济型 SVD分解：T

c c c c=X U S V (11)

而协方差矩阵 Σ则可以写成：T

1c

ccn=−SΣ V V (12)

相信大家在上式中能够看到协方差矩阵 Σ的特征值分解。请大家注意 (11) 中奇异值和 (12) 中特征值关系：_

_1cj

cjs

n=− (13)

同样，对标准化数据矩阵 ZX进行经济型 SVD分解：T=X Z Z ZZ U S V (14)

相关性系数矩阵 P则可以写成：T

1n=−Z

ZZSP V V (15)

上式相当于对 P特征值分解。本章下面将分别讲解特征值分解1) 协方差矩阵

2）格拉姆矩阵

3) 相关性系数矩阵成主成分分析。并利用诸如热图、饼图、直方图、陡坡图、双标图、椭圆等可视化工具分析三种本章以下三节将采用完全相似的结构方便大家比较三大类不同 PCA技术路线的异同。# 15.2协方差矩阵本节讲解利用特征值分解协方差矩阵Σ完成主成分分析。特征值分解图2所示为特征值分解协方差矩阵 Σ。Σ的对角线元素为方差，其他元素为协方差。Σ的迹代表方差之和：2 2 2 2

1traceD

Dj

j   

== + + + =  Σ

(16)

图2中Σ为对称矩阵，因此对Σ的特征值分解实际上是谱分解。Page 7 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com Λc为对角矩阵，对角线元素为特征值，特征值从大到小排列。Xc投影到规范正交基 Vc中得到

Yc，即 Yc = XcVc。Λc主对角线上的特征值实际上是 Yc的方差也就是说 Λc是Yc的协方差矩阵。因此，在主成分分析中，特征值也叫主成分方差。Λc的方差，即特征值，之和为：1traceD

c D j

j   

== + + =  Λ

(17)

Σ = Vc @ Λc VcT@

图2.

特征值分解协方差矩阵 Σ

图16对比格拉姆矩阵 G和ΛX。下面，我们进一步分析这两个矩阵。Σ Λc (a) (b)

X1

X2

X3

X4

X1 X2 X3 X4 PC1 PC2 PC3 PC4PC1

PC2

PC3

PC40.

686 0.

0421.

2740.

# 0.5160.190 0.330

# 0.330 3.116 0.122

1221.

# 1.296 0.5814.228 0

# 00.243 0

0 0.0780

0 0.024

图3.

对比协方差矩阵Σ和Λc热图分解前后大家在本书第12章已经见过图4和图5。如图4所示数据矩阵 X中第三列即 X3，的方差最大

X3对方差和 trace(Σ) 贡献超过

68%。Page 8 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.0 1.0 2.0 3.0 4.00.6860.1903.1160.581

X1X2X3X4

X1, 15.

0%X2, 4.

X3, 68.

X4, 12.

Variance(a) (b)

图4.

协方差矩阵 Σ的主对角线成分，即方差我们在《矩阵力量》第13章提过特征值分解前后矩阵的迹不变也就是说协方差矩阵Σ的迹trace(Σ) 等于的特征值方阵 Λc迹trace(Λc)：trace tracec=ΣΛ (18)

11DD

jj

jj

=== (19)

也就是说，PCA不改变数据各个特征方差总和。而第j个特征值λj 对trace(Λc) 的贡献百分比为：1100%j

D

i

i



=

 (20)

如图5所示，第一主成分的贡献超过92%，解释了数据中大部分 “方差”。数据分析中，如果原始数据特征很多彼此之间又具有复杂的相关性那么我们就可以考虑利用主成分分析对数据进行“降维”，减少特征的数量。而这个过程又保留了原始数据主要的信息。PC1, 92.

PC2, 5.

2280.

2430.

0780.

# 0.0 1.0 2.0 3.0 4.0(a) (b)

PC1PC2PC3PC4

图5.

Λc的主对角线成分，协方差矩阵 Σ的特征值陡坡图上一章介绍过我们经常用陡坡图可视化前 p个主成分解释总方差的百分比即累积贡献率

Page 9 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

1100%p

j

j

D

i

i

=

=

 (21)

图6所示为特征值分解协方差矩阵 Σ获得的陡坡图。观察陡坡图，可以帮助我们确定选取多少个主成分。0PC variance4

04080

2060100

Ratio of explained (%)

PC2 PC3 PC4 PC1

图6.

陡坡图，特征值分解协方差矩阵 Σ

特征向量矩阵图7所示为特征向量矩阵 Vc热图。Vc的每一列便代表一个主成分的方向，即Vc = [vc_1, vc_2,

vc_3, vc_4] 从左到右分别是第一、二、三、四主成分。这些主成分方向两两正交。在主成分分析中，Vc叫主成分系数，也称为载荷 (loading )。注意，有一些参考文献中，载荷还要乘上特征值的平方根，即

jjv。Vc也可以通过经济型SVD分解中心化矩阵 Xc得到。# 0.36 0.66

# 0.085 0.58

860.

# 0.36 0.73 0.6

# 0.17 0.076 0.32

# 0.075 0.48

# 0.55 0.75

PC1 PC2 PC3 PC4vc_1 vc_2 vc_3 vc_4Vc

图7.

特征向量矩阵 Vc热图投影由于 Vc为正交矩阵满足 VcTVc = VcVcT = I

因此 Vc本身也是规范正交基。如图8所示，将中心化矩阵 Xc投影到 Vc这个规范正交基中得到数据矩阵 Yc

即 Yc = XcVc。通过图8中的Yc每一列的色差，我们就可以看出来不同的次序主成分对数据总体方差的解释力度。Page 10 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.《矩阵力量》第18章介绍过 SVD分解的优化视角。利用 L2范数，Vc的第一列列向量实际上是如下优化问题的解：_1arg max

subject to: 1cc=

=vv X v

v (22)

前文提过，ΛX本身是Yc的协方差矩阵。ΛX为对角方阵，因此 Yc的任意两列之间线性相关系数为0。也就是说，Vc完成了 Xc的正交化，注意不是原始数据矩阵 X的正交化。请大家思考 Yc的每一列的均值是多少？Yc的质心位置是什么？为什么？Yc Xc = @ Vc

图8.

将中心化数据 Xc投影到 Vc

双标图如图9所示，双标图是可视化特征向量矩阵 Vc的重要方法。以图9中蓝色背景的双标图为例中心化数据 Xc投影到第一二主成分平面内的结果如四个箭头所示。比如，X1、X2、X3、X4在PC1上贡献的分量分别为0.

36、−0.

085、0.

86、0.

36，这正是如图7所示的 Vc第一列 vc_1。我们还可以把投影数据的散点图也画在双标图上大家已经在上一章看到很多例子再重复。Page 11 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

PC1PC2

PC1

PC1PC3

PC4PC3

PC2

PC2 PC3PC4 PC4xc_1xc_2xc_3xc_4

xc_1xc_1

xc_1xc_1 xc_1xc_2

xc_2

xc_2xc_2 xc_2xc_3

xc_3

xc_3

xc_3 xc_3xc_4 xc_4

xc_4 xc_4 xc_40.

36 0.

图9.

Vc双标图，特征值分解协方差矩阵 Σ

数据还原、误差将 (11) 展开写成：TT

_1 _1

T

_2 _2

_1 _ 2 _

T

_ _

T T T T

_1 _1 _1 _ 2 _ 2 _ 2 _ _ _ _ _ _

1c

ccc c

c c

c c c c D

cD cD

D

c c c c c c c D c D c D c j c j c j

js

s

s

s s s s

= 

 

  =  

 

   

= + + + = U

SVv

vX u u u

v

u v u v u v u v

(23)

图10所示为用第一主成分逼近估计 Xc，即：T

_1 _1 _1

First principalˆ

c c c cs=X u v

(24)

Page 12 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 图中可以看到，ˆ

cX和Xc非常相似；ˆ

cX是个150 × 4矩阵，ˆ

cX的秩还是1。请大家回顾如何用张量积计算

ˆ

cX。图10中的 E为误差，即

ˆ

cc=−E X X。E Xc =

ˆ

cX

图10.

第一主成分估计 Xc

要想还原原始数据 X，我们还需要考虑 (2) 这个等式关系，即：T

_ _ _

1EED

c c j c j c j

js

== + = +  X X X u v X (25)

如果利用第一主成分估计原始数据矩阵 X的话，可以利用：T

_1 _1 _1 Ec c cs+X u v X (26)

上式中，E(X) 为行向量，计算用到了广播原则。大家可能会问，图2中特征值分解仅仅获得了 Vc，没有 Uc。难道我们还需要再对Xc做SVD

答案是不需要。《矩阵力量》第10章介绍过 “二次投影 ”，也就是说 Xc可以写成：T

c c c c c==X X I X V V (27)

将Vc展开，上式可以写成：TT

_1

T

_2

_1 _ 2 _

T

_

T T T T

_1 _1 _ 2 _ 2 _ _ _ _

1c

cc

c

c c c c c D

cD

D

c c c c c c c c D c D c c j c j

j=



= 





= + + + = V

Vv

vX X v v v

v

X v v X v v X v v X v v

(28)

所以，(24) 可以写成：T

_1 _1 _1 _1ˆ

c c c c c c c= = X X v v X v v (29)

Page 13 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com (26) 则可以写成：_1 _1 Ec c c  +X X v v X (30)

如果用第一、二主成分还原 X，上式需要再加一项：_1 _1 _ 2 _ 2

Centroid First principal Second principalEc c c c c c  +  +X X v v X v v X

(31)

鸢尾花书在不同位置反复强调数据单位，也就是量纲。如果原始数据的每列数据的量纲不一致，比如高度、质量、时间、温度、密度、百分比、股价、收益率、GDP等等。利用特征值分解协方差矩阵完成PCA就会有麻烦因为大家通过图9可以看到每一个主成分是若干特征的 “线性融哪怕每一列数据的量纲一致比如鸢尾花前四列的单位都是厘米 cm

这种 PCA技术路线还会受到不同特征方差大小影响。解决这些问题的方法是特征值分解线性相关系数矩阵，这是本章后文要讨论的话题。椭圆：投影之前如图11所示，协方差矩阵 Σ椭球 (马氏距离为1) 在六个平面上的投影。通过旋转椭圆的形状位置、旋转角度我们可以读出标准差相关性系数等重要信息。图12比较数据 X的分类和合并协方差矩阵对应的椭圆。对椭圆、合并方差这些概念感到陌生的话，请回顾《统计至简》第13章。2 cm 2 cm 0 cm 2 cm0 cm2 cm

X1 µ1 X2 µ2 X3 µ3 X2 µ2 X3 µ3 X4 µ4

图11.

马氏距离1椭圆，协方差矩阵 Σ

Page 14 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

Setosa Versicolor Virginica

Pooled covariance matrix

X1 µ1 X2 µ2 X3 µ3 X2 µ2 X3 µ3 X4 µ4 0.

8 cm 0.

8 cm 0 cm 0.

8 cm0 cm0.

8 cm

图12.

马氏距离1椭圆，数据 X的分类、合并协方差矩阵Σ

椭圆：投影之后将中心化数据 Xc投影到 Vc得到的结果为 Yc：c c c=Y X V (32)

Yc的协方差矩阵就是 X的协方差矩阵的特征值矩阵。图13所示为 Yc的协方差矩阵在六个平面上的投影，这些椭圆都是正椭圆。Yc的协方差矩阵实际上就是Σ的特征值矩阵。图14比较数据 Yc的分类和合并协方差矩阵对应的椭圆。Page 15 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

PC1 PC2 PC3PC2 PC3 PC4 2 cm 2 cm 0 cm 2 cm0 cm2 cm

图13.

马氏距离1椭圆，Yc的协方差矩阵

PC1 PC2 PC3PC2 PC3 PC4Setosa Versicolor Virginica

Pooled covariance matrix

图14.

马氏距离1椭圆，数据 Yc的分类、合并协方差矩阵 Σ

Page 16 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 15.

3格拉姆矩阵特征值分解图15所示为特征值分解格拉姆矩阵 G。注意，前文提过为了便于和协方差矩阵比较本章中用的格拉姆矩阵 G实际上是 XTX/(n –

图15中的格拉姆矩阵 G为对称矩阵，因此这个特征值分解同样是谱分解。VX为正交矩阵，满足 VXTVX = VXVXT = I。ΛX为对角矩阵，对角线元素为特征值，特征值从大到小排列。图16对比格拉姆矩阵 G和ΛX。下面，我们进一步分析这两个矩阵。G = VX @ ΛX VXT@

图15.

特征值分解格拉姆矩阵 G

G ΛX (a) (b)

# 35.069 17.942

94223.

3817.

# 7.5719.600 11.237

# 11.237 17.3343.570

5705.

# 5.833 2.02961.801 0

# 02.117 0

0 0.0800

0 0.024X1

X2

X3

X4

X1 X2 X3 X4 PC1 PC2 PC3 PC4PC1

PC2

PC3

PC4

图16.

对比 G和ΛX热图分解前后

G和ΛX的主对角线之和相同，即 trace(G) = trace(ΛX)。如图17所示，矩阵 G的主对角成分为矩阵 X的每一列向量的模除以 n – 1

代表某个特征相对于原点的分散情况即“不去均值”的方

Page 17 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 而trace(G) 相当于数据整体相对于原点的分散度量。如图17所示，矩阵 X的第一列和第二列贡献最大。经过特征值分解之后如图18所示第一主成分解释了大部分数据分散情况达96.

X1X2X3X4

0699.

60017.

3342.

X1, 54.

X2, 15.

0%X3, 27.

1%X4, 3.

0 20 40 60(a) (b)

图17.

G的主对角线成分

0 20 40 60PC1PC2PC3PC4

8012.

1170.

0800.

PC1, 96.

PC2, 3.

3%(a) (b)

图18.

ΛX的主对角线成分，格拉姆矩阵 G的特征值陡坡图图19所示为在特征值分解格拉姆矩阵 G主成分分析的陡坡图。# PC2 PC3 PC4 PC160

0PC variance

04080

2060100

Ratio of explained (%)

图19.

陡坡图，特征值分解格拉姆矩阵 G

特征向量矩阵图20所示为特征向量矩阵VX热图。显然，图20不同于图7。Page 18 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.75 0.28

380.

510.

# 0.170.55 0.68

# 0.71 0.06 0.32

# 0.34 0.48

# 0.54 0.75

PC1 PC2 PC3 PC4vX_1 vX_2 vX_3 vX_4VX

图20.

特征向量矩阵 VX热图投影图21是将原始数据 X投影到 VX，即 YX = XVX。YX的特点是其格拉姆矩阵为对角方阵，也就是说 YX的列向量两两正交。注意，两两正交不代表线性无关。YX X = @ VX

图21.

将原始数据 X投影到 VX

正交矩阵 VX也是一个规范正交基，VX是因原始数据 X而生。前文提到，Vc同样是一个规范正交基，但是 Vc是因中心化数据矩阵 Xc而生。我们当然可以将X投影到 Vc这个规范正交基中大家可以自行验证 XVc的协方差和XcVc相同，都是对角方阵。也就是说，XVc的列向量也是线性无关。但是，XVc的质心不再是原点。双标图图22所示为 VX的双标图。请大家自行比较图9和图22。Page 19 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

PC1PC2

PC1

PC1PC3

PC4PC3

PC2

PC2 PC3PC4 PC4x1x2

x3x4

x1 x1

x1x1x1x2 x2

x2

x2x2x3x3

x3x3

x3x4 x4

x4x4x4

图22.

VX双标图，特征值分解格拉姆矩阵 G

数据还原、误差由于本节中 PCA分析直接采用特征值分解格拉姆矩阵 G

根据 (1)

利用第一主成分还原原始数据 X时我们不需要加入质心成分：_1 _1XX X Xv v (33)

如果用第一、二主成分还原X，上式也需要再加一项：_1 _1 _ 2 _ 2

First principal Second principal  + X X X X X Xv v Xv v

(34)

Page 20 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

E X

ˆX =

图23.

第一主成分估计 X

椭圆：投影之前图24所示为格拉姆矩阵 G对应的旋转椭圆。G相当于“不去均值 ”的协方差矩阵。观察图24，我们发现椭圆的朝向都是一三象限，而且椭圆都细长。比较图11和图24，大家应该理解为什么需要去均值。X1 X2 X3 X2 X3 X4 8 cm 8 cm 0 cm 8 cm0 cm8 cm

图24.

马氏距离1椭圆，“不去均值 ”的协方差矩阵 Σ

椭圆：投影之后经过 YX = XVX投影之后，图25所示 YX协方差矩阵对应的椭圆。Page 21 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

PC1 PC2 PC3PC2 PC3 PC4 8 cm 8 cm 0 cm 8 cm0 cm8 cm

图25.

马氏距离1椭圆，YX的协方差矩阵

15.4相关性系数矩阵标准化数据 ZX相当于是 Z分数，因此消除了特征量纲影响。因此，特征值分解相关系数矩阵不再受量纲影响。此外，标准化数据每一列特征数据均值均为0，方差为1。这也消除了较大方差特征的影响。特征值分解图26所示为特征值分解相关性系数矩阵 P

P的主对角线都是1

P对角线之外的元素都是线性相关系数。图27对比相关性系数矩阵 P和ΛZ热图。同样地，P和ΛZ主对角线之和相同，即

trace( P) = trace(ΛZ)。P = VZ @ ΛZ VZT@

图26.

特征值分解相关性系数矩阵 P

Page 22 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

P ΛZ (a) (b)

X1

X2

X3

X4

X1 X2 X3 X4 PC1 PC2 PC3 PC4PC1

PC2

PC3

PC42.

918 0

# 00.914 0

0 0.1470

0 0.0211 0.118

1180.

8720.

# 0.8181 0.428

# 0.428 1 0.366

3660.

# 0.963 1

图27.

对比相关性系数矩阵 P和ΛZ热图分解前后图4中，X3对方差和 trace(Σ) 贡献超过68%

而 X3的贡献小于5%。而图28中每个特征经过标准化之后，贡献率完全相同。方差小特征也可能含有重要的信息，利用特征值分解相关性系数完成PCA，可以消除这种顾虑。X1, 25% X2, 25%

X3, 25% X4, 25%

0 1 2X1X2X3X4(a) (b)

图28.

相关性系数矩阵 P主对角线成分

PC1, 73.

PC2, 22.

0 1 2PC1PC2PC3PC4

9180.

9140.

1470.

021(a) (b)

图29.

ΛZ的主对角线成分，相关性系数矩阵 P特征值陡坡图

Page 23 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 图30所示为特征值分解相关性系数矩阵 P主成分分析结果陡坡图。第一主成分贡献小于

80%。04080

2060100

Ratio of explained (%)2

0PC variance3

PC2 PC3 PC4 PC1

图30.

陡坡图，特征值分解相关性系数矩阵 P

特征向量矩阵图31所示为特征向量矩阵 VZ热图。这幅图和图7、图20均不同。PC1 PC2 PC3 PC40.

52 0.

# 0.27 0.72

580.

# 0.56 0.92 0.24

# 0.024 0.14 0.12

# 0.067 0.80

# 0.63 0.52vZ_1 vZ_2 vZ_3 vZ_4VZ

图31.

特征向量矩阵 VZ热图投影图32所示为标准化数据 Z投影到 VZ得到数据矩阵 YZ。同样地，正交矩阵 VZ也是一个规范正交基，而VZ是因中心化数据 ZX而生。请大家将原数据 X

中心化 Xc也投影到 VZ中并检验结果的协方差矩阵和质心。Page 24 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

YZ Z = VZ

图32.

中心化数据 Z投影到VZ

双标图图33所示为 VZ双标图，请大家比较本章三幅双标图。# PC1PC2

PC1

PC1PC3

PC4PC3

PC2

PC2 PC3PC4 PC4z1z2z3

z4

z1 z1

z1z1 z1z2z2

z2 z2 z2z3 z3

z3z3 z3z4 z4

z4 z4

z4

图33.

VZ双标图，特征值分解格相关性系数矩阵 P

Page 25 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

数据还原、误差图34所示为第一主成分估计 ZX：_1 _1X X X XZ Z v v (35)

E Z =

ˆZ

图34.

第一主成分还原 ZX

ZX可以写成：__

1ED

jj

j−

== − =   X X X XZ X X D Z v v (36)

用VZ还原 X：__

1ED

jj

j==  +

 X X X X Z v v D X (37)

用VZ第一主成分估计 X：_1 _1

First principalE   +X X X X Z v v D X

(38)

其中，D起到缩放的作用，E(X) 是平移的作用。椭圆：投影之前图35所示为投影之前相关性系数矩阵 P对应的椭圆。请大家特别和前文协方差矩阵对应椭圆进行比较。Page 26 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

Z1 Z2 Z3Z2 Z3 Z4 2 2 0 202

图35.

马氏距离1椭圆，相关性系数矩阵 P

椭圆：投影之后图36所示为投影之后正椭圆的位置和形状。# PC1 PC2 PC3PC2 PC3 PC4 2 2 0 202

图36.

马氏距离1椭圆，YZ的协方差矩阵

Page 27 | Chapter 15主成分分析进阶 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

Bk6_Ch 15_01.

py绘制本章大部分图片。主成分分析是鸢尾花书的 “常客”

我们用椭圆、数据格拉姆矩阵、协方差矩阵特征值分解、奇异值分解线性组合、优化随机变量的线性函数等等视角探讨过主成分分析。换句话来说，机器学习常用的数学工具在主成分分析处达到了一种融合大家也看到了数学板块实际上不是一个个孤立的个体，它们有其内在联系和网络。鸢尾花书有关主成分分析专题内容到此为止下两章我们将主要介绍和主成分分析相关的回归算法。此外，本书还会在最后一章比较奇异值分解和因子分析的异同。《机器学习》一册还要综述常见降维算法其中还包括核主成分分析 KPCA

KPCA相当于 PCA的升级版。在用椭圆理解数据解释主成分分析方面以下论文给本章很多启发欢迎大家阅读

https://a rxiv.

org/pdf/1302.

4881 .

Page 1 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 16 Orthogonal Distance Regression

正交回归输入和输出数据都参与主成分分析，构造正交空间数学展现出秩序、对称和有限 ——这些都是美的极致形态。The mathematical sciences particularly exhibit order

symmetry

and limitations

and these are the

greatest forms of the beautiful.

—— 亚里士多德 (Aristotle ) | 古希腊哲学家 | 384 ~ 322 BC

◄ numpy.

linalg.

eig 特征值分解

◄ numpy.

linalg.

svd 奇异值分解

◄ numpy.

mean 计算均值

◄ numpy.

std 计算均方差

◄ numpy.

var 计算方差

◄ pandas_datareader.

get_data_yahoo 下载股价数据

◄ scipy.

odr 正交回归

◄ scipy.

odr.

Model 构造正交回归模型

◄ scipy.

odr.

ODR 设置正交回归数据、模型和初始自

◄ scipy.

odr.

RealData 加载正交回归数据

◄ statsmodels.

a pi.

add_constant 增加OLS常数项

◄ statsmodels.

api.

OLS 最小二乘法线性回归

Page 2 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

正交回归模型投影视角几何视角变量数量二元一元多元

Page 3 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 16.

1主成分与回归本章主要介绍一种和主成分分析息息相关的回归方法 ——正交回归 (orthogo nal regression )。正交回归，也叫做正交距离回归 (Orthogonal Distance Regression

ODR)，又叫全线性回归

(total linear regression)。正交回归通过将自变量通过主成分分析转换成互相正交的新变量，来消除自变量之间的多重共线性问题，从而提高回归分析的准确性和稳定性。具体来说，正交回归通过以下步骤实现

1) 对自变量进行主成分分析得到主成分变量它们互相正交。2) 对因变量和主成分变量进行回归分析，得到每个主成分变量的回归系数。3) 根据主成分变量的回归系数和主成分分析的结果，计算出每个自变量的回归系数和截距项。正交回归的优点之一是消除自变量之间的多重共线性，提高回归分析的准确性和稳定性。交回归可以在保证预测准确性的前提下，降低自变量的维度，提高回归模型的可解释性。正交回归的缺点是计算复杂度较高，需要进行主成分分析和回归分析等多个步骤。此外，由于正交回归是基于主成分分析的因此它可能会失去一些原始自变量的信息因此需要在可接受的误差范围内进行权衡。举个例子，平面上最小二乘法线性回归 OLS仅考虑纵坐标方向上误差如图1 (a) 所示；正交回归 TLS同时考虑横纵两个方向误差，如图1 (b) 所示。(a) (b)

图1.

对比 OLS和TLS线性回归从主成分分析角度正交回归特点是输入数据 X和输出数据 y都参与主成分分析。按照特征值从小到大顺序排列特征向量 [v1, v2, .

, vD, vD+1]，用其中前 D个向量 [v1, v2, .

, vD] 构造一个全新超平面 H。利用 vD+1垂直于超平面 H便可以求解出回归系数。Page 4 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 下面用两特征 X = [x1

x2] 数据作例子聊一下主成分回归的思想。如图2所示，x1和x2为输入数据，y为输出数据；通过主成分分析

x1、x2和y正交化之后得到 v1

v2和v3 (根据特征值从小到大排列 )；v1、v2和v3两两正交。第一主成分 v1和第二主成分 v2构造平面 H。v3垂直于平面

H，通过这层关系求解出正交回归系数。v1v2v3

HHy

x1x2

OrthogonalizePlane spanned by column

vectors of x1 and x2Output

Second principal component

First principal component Plane spanned by column

vectors of v1 and v2

图2.

通过主成分分析构造正交空间前文介绍的线性回归采用算法叫做普通最小二乘法 (Ordinary Least squares

OLS )；而正交回归采用的算法叫做完全最小二乘法 (Total Least Squares

TLS)。如图3所示，最小二乘回归，将 y投影到 x1和x2构造的平面上。而对于正交回归，将y投影到H，得到ŷ。而残差，ε = y – ŷ，平行于 v3。再次强调，平面 H是由第一主成分 v1和第二主成分

v2构造。此外，建议读者完成本章学习之后，回过头来再比较图3和图4。这样，相信大家会更清楚

OLS和TLS之间的区别。Page 5 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

ε = y ŷ y

x1x2Center of data

Plane spanned by column

vectors of x1 and x2

图3.

最小二乘回归，将 y投影到 x1和x2构造的平面上

y

v1v2H

v3

H

Plane spanned by column

vectors of v1 and v2ŷ

图4.

正交回归，将输出数据 y投影到 H

下一节首先用一元正交回归给大家建立正交回归的直观印象本章后续将逐步扩展到二元回归和多元回归。# 16.2一元正交回归设定一元正交回归解析式如下：01 y b b x=+ (1)

Page 6 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 其中，b0为截距项，b1为斜率。如图5所示

x-y平面上任意一点 (x(i)

y(i)) 和正交回归直线距离可以利用下式获得

11ii

iy b b x

d

b−+

=

+ (2)

当i = 1 ~ n时，di构成列向量为 d：11bb

b−+=

+yxd (3)

di

(x(i), y(i))

图5.

正交投影几何关系构造如下优化问题，b0和b1为优化变量，优化目标为最小化欧氏距离平方和：2T

0, 1arg min ,

bbf b b==d d d (4)

将 (3) 代入 f(b0, b1) 得到：T

0 1 0 1

01 2

1,1b b b b

f b bb− + − +

=+y x y x (5)

为了方便计算，也引入全1向量1，它和 x形状一样为n行1列向量；f(b0, b1) 展开整理为下

Page 7 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

2 T 2 T T T T

0 0 1 1 0 1

01 2

12 2 2

1nb b b b b bf b bb+ + − − +=+x 1 x x y 1 x y y y (6)

f(b0, b1) 对b0偏导为0，构造如下等式：TT

01 01

01, 2 2 201f b b nb b

bb +−==+x 1 y 1 (7)

f(b0, b1) 对b1偏导为0，构造如下等式：2 T 2 T T T T T T T

0 0 1 1 0 1 1 01 10

2 22

1112 2 2 2 , 2 2 201 1nb b b b b b b f b b bb

bb b + + − − + +−= − =+ + x 1 x x y 1 x y y y x x x 1 x y (8)

观察 (7)，容易用 b1表达b0：TT

01 EEbbbn−= = −y 1 x 1yx (9)

T

T

1E

En

i

i

n

i

ix

nn

y

nn=

=



 =



===



x1x

y1y (10)

将 (9) 给出 b0解析式代入 (8) 获得仅含有b1的一元二次方程：11 10 b kb+ − = (11)

T T T T T T

T T T T T T

var var

co ,vxy

xy x ynnkn

n n n n

nn



  − − +=−

   − − −      =

=− −−

=x x x lx l y y y ly l

x y x ly l

x x x lx l y y y ly l

x y x ly l

xy

xyT T T

T T T (12)

上式，不区分求解方差协方差时，1/(n – 1)和1/n之间差别。求解 (11) 一元二次方程，得到 b1解如下：2kkb−  += (13)

将 (12) 给出的 k，代入 (13)，整理得到 b1解：Page 8 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

2 222

2y x x y xy x y

xy x yb      

  −

=−+ (14)

发现 b1两个解即主成分分析 (principa l comp onent analysis

PCA) 主元方向。构造 [x, y] 数据矩阵，它的协方差矩阵 Σ 可以记做：2x xy x y

xy x y y   

   =

Σ (15)

对Σ进行特征值分解，得到两个特征向量：222 2 2 2

22 2 2 22

1y x x y xy x y

xy x y

y x x y xy x y

xy x y      

  

      

  ++

=





−+

=



−−

−−

v

v (16)

Σ两个特征值，从大到小排列：22 2 2 2

2 2 2 2

22x

xxy x y

xy

x y xy

yy

y x     

       +−= + + 

 +−= − +  (17)

特征值较大的特征向量为正交回归直线切线向量；特征值较小特征向量对应直线法线向量，这样求得 b1斜率。有了上述思路，便可以用PCA分解来获得正交回归系数，这是下一节要讲解的内容。如下代码首先介绍如何利用 scipy.

odr 可以求解得到正交回归系数。构造线性函数

linear_func(b, x)，利用 scipy.

odr.

Model(linear_func) 创建线性模型；然后，采用 scipy.

odr.

RealData

加载数据，再用 scipy.

od r.

ODR 整合数据、模型和初始值，输出为 odr。odr.

run 求解回归问然后，用 pprint 打印结果。Beta: [0.

00157414 1.

43773257]

Beta Std Error: [0.

00112 548 0.

05617699]

Beta Covarianc e: [[ 1.

21904872e -02 -2.

43641786e -02]

[-2.

43641786e -02 3.

03712371e+01]]

Residual Variance: 0.

000103909324594 80641

Inverse Condition #: 0.

22899877744275976

Reason(s) for Halting:

Sum of squares conve rgence

一元正交回归的解析式为：# 1.4377 0.00157yx=+ (18)

Page 9 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 下一节将介绍如下采用主成分分析来求解一元正交回归系数并比较正交回归和最小二乘法线性回归。# 16.3几何角度看正交回归图6所示为正交回归和PCA分解关系发现主元回归直线通过数据中心 (E(x)

E(y))，回归直线方向和主元方向 v1平行，垂直于次元 v2方向。即，次元方向 v2和直线法向量 n平行。v2 // nSecond principal component

First principal component

(E(x), E(y))v2

v1

n

图6.

正交回归和PCA分解关系对于 (1) 所示一元一次函数，构造二元 F(x, y) 函数如下：01 ,Fy b b x xy+=− (19)

F(x, y) 法向量即平面上形如 (1) 直线法向量 n可以通过下式求解

T

1,1b FF

xy  == −   n (20)

如前文所示，n方向即PCA分解第二主元方向，即次元方向。为了方便计算，假设数据已经经过中心化处理，即已经完成如下运算：, EE= − = −x x x y y y (21)

Page 10 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 由于 x和y已经是中心化向量，协方差矩阵可以通过下式运算得到：T T T

T

T T T   = = =       x x x x yΣ x y x y x y

y y x y y (22)

为了方便计算，本节计算协方差矩阵不考虑系数1/(n – 1)。由于 n为Σ次元方向：TT

22 TT=  = x x x yΣn n n n

y x y y (23)

将 (20) 代入 (23)，整理得到如下两个等式：# TT TT

1 2 1 11

2 TT TT

1211bb bb

b

−=      =      −− − =−      x x x y x x x y

y x y y y x y y (24)

联立 (24) 两个等式，用λ2表示 b1：1TT

1_ TLS 2b −=−x x x y (25)

下式为本书前文获得的一元线性回归 OLS中b1解：1TT

1_ OLSb−=x x x y (26)

对比 OLS和TLS；当 (25) 中λ2为0时，两种回归方法得到斜率完全一致。λ2 = 0时，y和x

完全线性相关。数据中心化前后，回归直线梯度向量不变；中心化之前的回归直线通过 (E(x), E(y)) 一点，01 EE bb=+yx (27)

获得回归式截距项b0表达式：01EEbb=− yx (28)

图7所示为一元正交回归数据之间关系。发现自变量 x列向量和因变量 y列向量数据都参与

PCA分解得到正交化向量 v1和v2

然后用特征值中较大值对应特征向量 v1作为一元正交回归直线切线向量。更为简单计算方法是，用特征值较小值对应特征向量 v2作为一元正交回归直线法向

Page 11 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

y

xv1

v2ŷ = b1xLine spanned by column

vector of v1

Centralize Orthogonalize Derive

v2 ŷ

图7.

一元正交回归 TLS数据关系图8所示为最小二乘法 OLS一元线性回归系数，对应的一元 OLS解析式为：# 1.1225 0.0018yx=+ (29)

图9比较 OLS和TLS结果。# OLS Regression Results

==============================================================================

Dep.

Variable: AAPL R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 549.

Date: Thu

07 Oct 2021 Prob (F -statistic)

55e -65

Time: 07:08:46 Log -Likelihood: 678.

No. Observations: 252 AIC: -1352.

Df Residuals: 250 BIC: -1345.

Df Model: 1

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const 0.

0018 0.

001 1.

759 0.

080 -0.

000 0.

SP500 1.

1225 0.

048 23.

446 0.

000 1.

028 1.

==============================================================================

Omnibus: 52.

424 Durbin -Watson: 1.

Prob(Omnibus): 0.

000 Jarque -Bera (JB): 210.

Skew: 0.

777 Prob(JB): 1.

68e -46

Kurtosis: 7.

203 Cond.

No.6.

==============================================================================

图8.

最小二乘法 OLS一元线性回归结果

Page 12 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.10 0.00 0.10

S&P 500 daily return, market

100.

000.

10AAPL daily returnOLSTLS

图9.

比较 OLS和TLS结果

Bk6_Ch 16_01.

py绘制本节图像。# 16.4二元正交回归这一节用主成分分析讨论二元正交回归。首先也是对数据进行中心化处理：1 1 1 2 2 1

EE , E = − = − = −x x x x x x y y y (30)

根据 PCA计算法则，首先求解协方差矩阵。由于 x1、x2和y已经为中心化矩阵，因此协方差矩阵Σ通过下式计算获得。Page 13 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

  

 T

1 2 1 2

T T T T

1 1 1 1 2 1

T T T T

2 1 2 2 1 2 2 2

T T T T

12=

   

   ==   

      Σ x x y x x y

x x x x x x y

x x x y x x x x x y

y y x y x y y (31)

为了方便计算，本节也计算不考虑系数1/(n – 1)。正交回归解析式表达：0 1 1 2 2b b xy bx++= (32)

构造二元F(x1, x2, y) 函数如下：1 2 0 1 1 2 2,, F y yx x b b x b x + =+− (33)

F(x1, x2

y) 法向量即平面 f(x1

x2) 法向量 n通过下式求解

 T

T

12, , 1F F Fbbx x y  = = −  n (34)

n平行于Σ矩阵 PCA分解特征值最小特征向量，即：# T T T

1 1 1 2 1

T T T

3 3 3 2 1 2 2 2 3

T T T

12

=  =

x x x x x y

Σv v x x x x x y n n

y x y x y y (35)

整理得到：# T T T

T T T 1 1 1 2 1 1 1

1 1 3 1 1 2 2 1T T T

2 1 2 2 2 2 3 2T T T

T T T 2 1 1 2 2 3 2 2

12 11bbbb

bb

bb



    − + =     =      + − =     −−    x x x x x yx x x x x y

x x x x x y

x x x x x yy x y x y y (36)

n平行于Σ矩阵 PCA分解特征值最小特征向量v3

构造如下等式并求解 b1和b2

1 1 1,3

2 3 2 2,3

3,3 11b b v

b k b k v

v    

    =  =    

    −−    v (37)

根据 (37) 最后一行，可以求得 k

3,31kv−= (38)

b1和b2构成的列向量为：1,3 1

2,3 2 3,31v b

v b v −=   (39)

回归方程常数项通过下式获得：Page 14 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

0 1 2

2E E Ebbb=−  y x x (40)

为了方便多元正交回归运算，令：1 2 1 2=  = x x X x x y X y (41)

协方差矩阵 Σ为：TT

TT=X X X yΣ

y X X y (42)

上式Σ也不考虑系数1/(n – 1)：TT

3 3 3 3 TT=  = X X X yΣv v n n

y X y y (43)

构造 b = [b1, b2]T这样重新构造特征值和特征向量以及 Σ之间关系：211b

b==−−bn (44)

将 (44) 代入 (43)，整理得到 b：TT

1TT

33 TT11−     =  = −     −−    bb X X X yb X X X y

y X y y (45)

下一节将使用 (45) 这一解析式计算正交回归解析式系数。图10回顾本章第一节介绍的二元正交回归坐标转换过程。数据 [x1

x2, y] 中心化后用PCA正交化获得正交系 [v1

v2, v3]。v1, v2和v3对应特征值由大到前两个主元向量 v1和v2相互垂直构成了一个平面 H

特征值最小主元 v3垂直于该平面。为H平面法向量，n和v3两者平行。图10还比较了 OLS和TLS回归结果。值得大家注意的是，如图10上半部分所示，对于最小二乘回归 OLS，ŷ在x1和x2构造的平面上；而如图10下半部分，正交回归 TLS中，ŷ在v1和v2构造平面 H上。Page 15 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

yy

x1x2

x2

x1v1v2v3

H

HPlane spanned by column

vectors of x1 and x2

Plane spanned by column

vectors of v1 and v2OLS

TLS

图10.

几何角度解释二元正交回归坐标转换图11解释二元正交回归数据关系。如前文反复强调，输入数据和输出数据都参与主成分分析，也就是正交化过程因此特征向量既有“输入”成分也有“输出”成分呈现“你中有我有你”。y

x1

x2v1

v2

v3ŷ = b 1x1 + b 2x2Principal components

Last componentPlane spanned by column

vectors of v1 and v2

Centralize Orthogonalize Derive

v3 ŷ

Page 16 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 图11.

二元正交回归数据关系利用上一节介绍的 scipy .

odr，可以求解一个二元正交回归的结果如下。利用主成分分析，我们可以获得相同正交回归的系数。Beta: [-0.

00061177 0.

40795725 0.

44382723]

Beta Std Erro r: [0.

00057372 0.

02454606 0.

02864744]

Beta Covariance: [[ 5.

46486647e -03 -2.

24817813e-02 1.

00466594e-02]

[-2.

24817813e -02 1.

00032390e+01 -7.

07446738e+00]

[ 1.

00466594e -02 -7.

07446738e+0 0 1.

36253753e+01]]

Residual Variance: 6.

02314210079386e -05

Inverse Condition #: 0.

16900716799896934

Reason(s) for Halting :

Sum of squares conve rgence

二元正交回归的平面解析式为：12 0.4079 0.4438 0.00061y x x= + − (46)

图12所示为最小二乘法 OLS二元线性回归结果，对应的平面解析式如下：12 0.3977 0.4096 0.006y x x= + − (47)

OLS Regression Results

==============================================================================

Dep.

Variable: SP500 R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 607.

Date: Thu

07 Oct 2021 Prob (F -statistic)

69e -96

Time: 07:31:57 Log -Likelihood: 831.

No. Observations: 252 AIC: -1656.

Df Residuals: 249 BIC: -1646.

Df Model: 2

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const -0.

0006 0.

001 -0.

984 0.

326 -0.

002 0.

AAPL 0.

3977 0.

024 16.

326 0.

000 0.

350 0.

MCD 0.

4096 0.

028 14.

442 0.

000 0.

354 0.

==============================================================================

Omnibus: 37.

744 Durbin -Watson: 1.

Prob(Omnibus): 0.

000 Jarque -Bera (JB): 157.

Skew: 0.

492 Prob(JB): 5.

67e -35

Kurtosis: 6.

749 Cond.

No.9.

==============================================================================

图12.

最小二乘法 OLS二元线性回归结果图13比较 OLS和TLS二元回归结果。Page 17 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

100.

000.

AAPLMCD

S&P 5000.

10OLS

TLS

图13.

比较 OLS和TLS二元回归结果

Bk6_Ch16_02.

py完成本节回归运算。# 16.5多元正交回归下面，把上述思路推广到 D维度 X矩阵。首先中心化数据，获得如下两个中心化 X, y向量：, E1T

nDn= − = −X I ll X y y y (48)

为了表达方便，假设 X和y已经为中心化数据；这样，构造回归方程式时，不必考虑常数项

b0，即回归方程中没有截距项：1 1 2 2 1 1 D D D D y b x b x b x b x−− = + + + +

(49)

为了进行 PCA分解，首先计算 [X, y] 矩阵协方差矩阵。X和y均是中心化数据不考虑系数1/(n – 1)

协方差矩阵通过下式简单运算获得

Page 18 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

T T T

T

11 T T T

, ,DD+  +   = = =       X X X X yΣ X y X y X y

y y X y y (50)

上述协方差矩阵行列宽度均为 D + 1。对它进行特征值分解得到：1−=ΣVΛV (51)

 1

1 2 1

1 2 1,DD

D

D

DD



   



+

+

+





=    







=Λ

V v v v v

(52)

特征值矩阵对角线特征值从左到右，由大到小。有了本章之前内容铺垫，相信读者已经清楚正交回归的矩阵运算过程，具体如图14所示。n × (D + 1)[X, y] Σ

(D + 1) × ( D + 1)V

Eigenvalue descends b

kCompute

covariance matrixEigen

decomposition

图14.

多元正交回归矩阵运算过程

V中第1到第 D个行向量 [v1, v2, .

, vD] 构造超平面 H，而 vD+1垂直于该超平面。构造 F(x1, x2, .

, xD, y) 函数：1 2 1 1 2 2 1 1, ,.

, ,D D D D D F x x x y b x b x b x b x y−− = + + + + −

(53)

F(x1, x2, .

, xD, y) 法向量即平面上 f(x1, x2, .

, xD) 法向量 n通过下式求解： 

1T

T

12 ,...., , 11D

DF F Fb b bx x y    = = − = −     bn

(54)

这样重新构造特征值 λD+1和特征向量 vD+1以及Σ之间关系。注意，n 平行 vD+1。n对应Σ矩阵PCA分解特征值最小特征向量，即：Page 19 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

TT

1 1 1 1 TT D D D D+ + + +=  = X X X yΣv v n n

y X y y (55)

求解获得多元正交回归系数列向量 b解：TT

1 TLS 1 TT11DD−

++    =  = −     −−    bb X X X yb X X X y

y X y yTT (56)

对比多元线性最小二乘系数向量结果：1TT

OLS−=b X X X y (57)

发现当λD+1等于0时，y完全被 X列向量解释，即两个共线性。这里我们再次区分一下最小二乘法和正交回归。最小二乘法寻找因变量和自变量之间残差平方和最小超平面；几何角度上讲，将因变量投影在自变量构成超平面 H，使得残差向量垂直 H。正交回归则通过正交化自变量和因变量，构造一个新正交空间；这个新正交空间基底向量为分解得到主元向量，具体如图15所示。# D dimension al hyperplane

spanned by column vectors

of v1, .

, vD-1 and vDvq 1vq+1y

H

vD

v2

v1v3ŷn // vq+1

vD-1x1xD-1

OrthogonalizeD dimension al hyperplane

spanned by column vectors

of x1, x2, .

, xD-1 and xD

x2xD

xD-2

图15.

几何角度解释多元正交回归

Page 20 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com n平行于数据 [X

y] PCA分解特征值最小特征向量 vD+1

构造如下等式并求解b1

, bD：1, 1 1

2, 1 2

1, 11

11D

D

D

DD D

DDv b

v b

kk

v b

v+

+

+

+

++ 

 

 

 = =  =

 

 

   

   −−



− bbv

(58)

求解 k得到：1, 11

DDkv++−= (59)

求解b得到：1, 1 1

2, 1 2

1, 1

,11D

D

DD

DD Dv b

v b

v

v b+

+

++

+ 

 − == 

   b

(60)

b0通过下式求得。0 1 2E E E ED

Db

bb

b



 =−



y x x x

(61)

图16展示多元正交回归运算数据关系。看到数据 [X, y] 均参与到了正交化中；正交化结果为

D + 1个正交向量 [v1, v2, .

, vD, vD+1]。通过向量 vD+1垂直 v1, v2, .

, vD构成超平面，推导出多元正交回归解析式。Page 21 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

y

x1

x2

v2

v3

v4

vD+1.

vDŷ = b 1x1 + b 2x2 + .

+ b D-1xD-1 + b DxDŷPrincipal components

Last componentD dimension al hyperplane spanned by

column vectors of v1, .

, vD-1 and vD

Centralize Orthogonalize

x3

xD 1Derive

vD+1 ŷ

图16.

多元正交回归运算数据关系图17所示直方图，比较多元 TLS回归和多元 OLS回归系数。const

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

COSTOLS

TLS0.

00Coefficients

图17.

比较多元 TLS回归和多元 OLS回归系数

Page 22 | Chapter 16正交回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

Bk6_Ch 16_03.

py完成本节回归运算。正交回归和最小二乘法回归都是回归分析中的方法，但它们之间有很大的区别。OLS通过最小化实际观测值与预测值之间的误差平方和，来确定回归系数。这种方法非常直观且易于理解但存在一些缺点例如当数据存在多重共线性时

OLS的估计结果可能会变得不稳定，且估计结果受到极端值的影响较大。与OLS不同，正交回归是一种基于主成分分析的回归方法。它通过将自变量通过主成分分析转换成互相正交的新变量来消除自变量之间的多重共线性问题从而提高回归分析的准确性和稳定性。因此，正交回归方法相对于 OLS方法更加鲁棒适用于多重共线性较强的数据集同时也能够在保证预测准确性的前提下，降低自变量的维度，提高回归模型的可解释性。Page 1 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 17 Principal Components Regression

主元回归输入特征主成分分析，输出数据投影到选定主元超平面大理石中我看到了天使，我拿起刻刀不停雕刻，直到还它自由。I saw the angel in the marble and carved until I set him free.

—— 米开朗琪罗 (Michelangelo ) | 文艺复兴三杰之一 | 1475 ~ 1564

◄ seaborn.

heatmap 绘制数据热图

◄ seaborn.

joint plot 绘制联合分布和边际分布

◄ seaborn.

k deplot 绘制KDE核概率密度估计曲线

◄ seaborn.

lineplot 绘制线图

◄ seaborn.

relplot 绘制散点图和曲线图

◄ sklearn.

decomposition.

PCA 主成分分析函数

◄ statsmodels.

api.

add_constant 线性回归增加一列常数1

◄ statsmodels.

api.

OLS 最小二乘法函数

Page 2 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

主元回归模型投影视角和PCA关系偏最小二乘回归最小二乘法主元数量

Page 3 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 17.

1主元回归本节讲解主元回归 (Principal Comp onents Regression

PCR)。主元回归类似本章前文介绍的正交回归。多元正交回归中自变量和因变量数据 [X

y] 利用正交化按照特征值从大小排列特征向量，用 [v1, v2, .

, vD] 构造一个全新超平面

vD+1垂直于超平面关系求解出正交化回归系数。而主元回归，因变量数据 y完全不参与正交化即仅仅 X 参与 PCA分解获得特征值由大到小排列 D个主元 V = (v1, v2, .

, vD)；这 D个主元方向 (v1, v2, .

, vD) 两两正交。选取其中 k (k < D)

个特征值较大主元 (v1, v2, .

, vk)，构造超平面；最后一步，用最小二乘法将因变量 y投影在超平面图1提供一个例子，X有三个维度数据，X = [x1, x2, x3]。首先对 X列向量PCA分解，获得正交化向量 [v1, v2, v3]。然后，选取作为 v1和v2主元，构造一个平面；用最小二乘法，将因变量 y投影在平面上，获得回归方程。再次请大家注意，主元回归因变量 y数据并不参与正交化；主元回归选取前 P (P < D) 个特征值较大主元 VD×P (v1

v2, .

, vP)，构造一个超平面。x1x2Orthogonalization

of x1, x2, and x3

yx3

v1v2v3

Pv1v2v3

Project y to principal

components

ŷ

图1.

主元回归原理

Page 4 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 17.

2原始数据下载如图2所示为归一化股价数据，将其转化为日收益率，作为数据 X和y；其中 S&P 500

日收益率为数据 y，其余股票日收益率作为数据 X。图3所示为数据 X和y的热图。Normalized closing price3.

0SP500

TSLA

WMT

MCD

USBF

GM

COST

JNJYUM

NFLX

JPM

PFE

图2.

股价走势，归一化数据

X y SP500

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ

图3.

数据 X和y的热图

Page 5 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 图4几个分图给出的是数据 X和y的KDE分布。# 0.1 0.0

# 0.1 0.0

# 0.1 0.0

# 0.1 0.040

0Density40

0Density

0Density40

0DensityS&P 500

TSLA

WMT

MCDUSB

YUM

NFLX

JPM

PFE

FGM

COST

JNJ

图4.

数据X和y的KDE分布

17.3主成分分析对数据 X进行主成分分析，可以获得如表1所示的前四个主成分 VD×p参数。可以利用热图和线图对VD×p进行可视化，如图5所示。表1.

前四个主成分

PC1 PC2 PC3 PC4

TSLA -0.

947 -0.

004 0.

256 0.

WMT -0.

073 0.

016 -0.

193 0.

MCD -0.

056 0.

076 -0.

111 0.

USB -0.

021 0.

503 0.

122 -0.

YUM -0.

044 0.

188 -0.

037 0.

NFLX -0.

281 -0.

133 -0.

776 -0.

JPM -0.

019 0.

442 0.

167 -0.

PFE -0.

045 0.

174 0.

187 0.

F -0.

004 0.

457 -0.

179 0.

GM 0.

007 0.

491 -0.

360 0.

COST -0.

096 -0.

027 -0.

203 0.

JNJ -0.

042 0.

108 0.

021 0.

Page 6 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

PC1

PC2

PC3

PC4PC1

PC2

PC3

PC4PC1PC3PC2

PC4TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJTSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ1.

v1v2v3v4VD × p

图5.

前四个主成分可视化图5所示 VD×p两两正交，具有如下性质：T

D p D p p p  = V V I (1)

图6所示为 (1) 计算热图。VD × p VD × pT@ = Ip × p

图6.

VD×p两两正交

Page 7 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 17.

4数据投影如图7所示，原始数据 X在p维正交空间 (v1, v2, .

, vp) 投影得到数据 Zn×p：n p n D D p  =Z X V (2)

图8所示为 Zn×p数据热图。Zn×p

n × p= @ Xn×D VD×p

n × DD × p

v1vp.

图7.

PCA分解部分数据关系

PC1 PC2 PC3 PC4Zn×p

图8.

前四个主成分数据图9所示为 Zn×p每列主成分数据的分布情况。容易注意到，第一主成分数据解释最大方差。Page 8 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.1 0.020

0Density

PC1

PC2

PC3

PC4

图9.

前四个主成分数据分布图10所示为Zn×p数协方差矩阵热图。0028

PC2 PC3 PC40.

0017

00067

00038

PC1PC2 PC3 PC4 PC10.

002 5

# 0.002 0

0015

0010

0005

0000

图10.

前四个主元的协方差矩阵前四个主成分对应的奇异值分别为：1 2 3 40.

5915, 0.

4624, 0.

2911, 0.

2179s s s s= = = = (3)

所对应的特征值：2 2

2 2

2 2

2 2

# 40.59150.00281 126

# 0.46240.00171 126

# 0.29110.000671 126

# 0.21790.000381 126s

n

s

n

s

n

s

n





= = =−

= = =−

= = =−

= = =− (4)

Page 9 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 这四个特征值对应图10热图对角线元素。如图11所示陡坡图，前四个主元解释了84.

87%方

0Variance explained (%)0.

0020

0015

0010

0005

00000.

0025

Variance

Principal component1 2 3 4

图11.

转化矩阵 Zn×P仅包含 X部分信息两者信息之间差距通过下式计算获得如图12：T

n D n P D P n D   =+ X Z V E (5)

X E

=

ˆX

图12.

Zn×P还原数据和 X信息差距

# 17.5最小二乘法主元回归最后一步，用最小二乘法把因变量 y投影在数据Zn×P构造空间中：,1 1 ,2 2 ,ˆ .

Z Z Z P Pb b b= + + +y z z z (6)

Page 10 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 写成矩阵运算： ,1

Z

P n P Z

ZPb

b

b



==

y z z z Z b

(7)

图13所示为上述运算过程。y = × Zn×P bZ

n × PP × 1+

n × 1 n × 1ε

图13.

最小二乘法回归获得 y = Zn×PbZ + ε

根据本书前文讲解内容最小二乘法解，获得 bZ：1TT

1TTZ n P n P n P

n D D P n D D P n D D P−

  

−

     =

=b Z Z Z y

X V X V X V y (8)

如图13所示，y、拟合数据

ˆy 和数据 Zn×P关系如下：ˆ

ˆn P Z

n P Z

=+

=

=−y Z b ε

y Z b

ε y y (9)

图14所示为最小二乘法线性回归结果。系数向量 bZ结果如下： T0.

1039 0.

1182 0.

0941 0.

0418Z− − −=b (10)

Page 11 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

OLS Regression Results

==============================================================================

Dep.

Variable: SP500 R -squared: 0.

Model: OLS Adj.

R -squared: 0.

Method: Least Squares F -statistic: 37.

Date: XXXXXXXXXX Prob (F-statistic): 1.

82e -20

Time: XXXXXXXXXX Log-Likelihood: 450.

No. Observations: 127 AIC: -891.

Df Residuals: 122 BIC: -876.

Df Model: 4

Covariance Type: nonrobust

==============================================================================

coef std err t P>|t| [0.

025 0.

975]

------------------------------------------------------------------------------

const -0.

0003 0.

001 -0.

520 0.

604 -0.

002 0.

PC1 -0.

1039 0.

012 -8.

647 0.

000 -0.

128 -0.

PC2 0.

1182 0.

015 7.

689 0.

000 0.

088 0.

PC3 -0.

0941 0.

024 -3.

854 0.

000 -0.

142 -0.

PC4 -0.

0418 0.

033 -1.

283 0.

202 -0.

106 0.

==============================================================================

Omnibus: 9.

631 Durbin -Watson: 2.

Prob(Omnibus): 0.

008 Jarque -Bera (JB): 21.

Skew: 0.

092 Prob(JB): 1.

85e -05

Kurtosis: 5.

021 Cond.

No.1.

==============================================================================

图14.

最小二乘法线性回归结果下面将系数向量 bZ利用 (v1, v2, .

, vP) 转换为 bX，具体过程图15所示：1TT

X D P Z D P n P n P n P−

    ==b V b V Z Z Z y (11)

v1vPbX

D × 1P × 1bZ VD×P

D × P= ×

图15.

bz和bx之间转换关系系数 bX可以通过下式计算得到： T0.

1039 0.

1182 0.

0941 0.

0418X D P Z D P  − − − ==b V b V (12)

图16所示为系数 bX直方图。Page 12 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJ0.

0bX coefficients

图16.

系数 bX直方图这样获得 y、拟合数据

ˆy 和数据 X之间关系，如图17所示：ˆ

ˆX

X=+

=

=−y Xb ε

y Xb

ε y y (13)

X

n × Dy @ + ε bX

D × 1

n × 1=

n × 1

图17.

y和数据 X之间回归方程计算截距项系数 b0：0 1 2E E E EDX b=−y x x x b

(14)

计算截距项系数 b0：0 1 2

00034057E E E EDX b=−

=−y x x x b

(15)

最后主元回归函数可以通过下式计算得到：Page 13 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

   

 

 1

0 1 1 2 2 0 1 2 0 1 2

0 1 2 3 4

0 1 2 3 4

4ˆD D D D X

D

D P Z

z

z

z

zb

by b b x b x b x b x x x b x x x

b

b z z z z

b

bb z z z zb

b



 = + + + + = + = +





=+





 =+



b

Vb

(16)

图18展示主元回归计算过程数据关系。x1

x2

x3

v2

v3

vP

vP+1.

ŷ = b 1x1 + b 2x2 + .

+ b D-1xD-1 + b DxDŷ

High variance

principal components

ŷ = w1v1 + w2v2 + .

+ vPvPε = y ŷ

ŷ ε

Low variance

componentsP dimension al hyperplane spanned by

column vectors of v1, .

, vP-1 and vP

Centralize Orthogonalize

图18.

主元回归数据关系

Page 14 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 17.

6改变主元数量对于主元回归当改变参与最小二乘法线性回归的主元数量时线性回归结果会有很大变本节将重点介绍主元数量对主元回归的影响。图19所示为主元数量从4增加到9时，累计已释方差和百分比变化情况。图20和图21展示两个视角观察参与主元回归主元数量对于系数的影响。5 6 7 8 9 4Variance explained (%)

Number of principal components

图19.

主元数量对累计已释方差和百分比

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJPC1~4 PC1~5 PC1~6 PC1~7 PC1~8 PC1~90.

图20.

参与主元回归主元数量对于系数的影响

Page 15 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

TSLA

WMT

MCD

USB

YUM

NFLX

JPM

PFE

F

GM

COST

JNJPC1~4

PC1~5

PC1~6

PC1~7

PC1~8

PC1~90.

图21.

参与主元回归主元数量对于系数的影响，第二视角

Bk6_Ch 17_01.

py完成主元回归运算图像。# 17.7偏最小二乘回归本章最后介绍偏最小二乘回归 (partial least squares regression

PLS)。类似主元回归，偏最小二乘回归也是一种降维回归方法。PLS在降低自变量维度的同时，建立自变量和因变量之间的线性关系模型，因此常被用于处理高维数据分析和建立多元回归模型。不同于主元回归偏最小二乘回归利用因变量数据 y和自变量数据 X (形状为 n × q) 之间相关性构造一个全新空间。y和X投影到新空间来确定一个线性回归模型。另外一个不同点，偏最小二乘回归采用迭代算法 (iterative algorithm)。偏最小二乘法处理多元因变量为方便区分一元因变量被定义为 y (形状为 n × 1)

变量被定义为 Y (形状为 n × p)。偏最小二乘回归迭代方法很多，本节介绍较为经典一元因变量对多元自变量迭代算法。迭代算法主要由七步构成；其中，第二步到第七步为循环。第一步获得中心化自变量数据矩阵 X(0) 和因变量数据向量 y(0)：Page 16 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

0 0 0 0 T

0 TE1

1qn

n = − = 

=

= − − X I ll X x x x

y y y I ll y

(17)

偏最小二乘回归是迭代运算，上标 (0) 代表迭代代次。(X(0))T

q × n× y(0)=

n × 1w1

q × 1

图22.

计算权重系数列向量 w1

第二步计算 y(0) 和X(0) 列向量相关性，构建权重系数列向量 w1：# T00 00

1 1

T00 00

T2 00 2

T 0000cov ,

cov , 1

cov ,qqn    = = =    xy xy

xy xyw X y

xy xy

(18)

其中，列向量 w1行数为 q行。图22所示获得权重系数列向量计算过程；过程也可看做是一个投影运算，即将 (X(0))T 投影到

y(0)。为方便计算，将列向量 w1单位化：2,1 1

,1qw

w

w



==



www

(19)

列向量 w1每个元素大小代表着 y(0) 和X(0) 列向量相关性。第三步，利用上一步获得权重系数列向量 w1和X(0) 构造偏最小二乘回归主元向量

1 1,1 1 2,1 2 ,1 1 qq w w w= + + + =z x x x X w

(20)

Page 17 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 图23所示为计算偏最小二程回归主元列向量 z1。这样理解，主元列向量 z1为X(0) 列向量通过加权构造；y(0) 和X(0) 某一列向量相关性越高这一列获得权重越高在主元列向量 z1成分越高。同样，过程等价于投影过程，即 X(0) 投影到 w1。X(0)× z1 = w1

q × 1

n × 1 n × q

图23.

计算偏最小二程回归主元列向量 z1

将自变量数据矩阵 X(0) 和因变量数据向量 y(0)投影到主元 z1方向上。第四步把自变量数据矩阵 X(0)投影到主元列向量 z1上，获得系数向量 v1。先以 X(0)第一列解释投影过

Line spanned by column vector of z1z1

1 1,1 1ˆ v=xz

1x

11ˆ=−εxx

图24.

X(0)第一列投影在主元列向量 z1

如图24所示，将 X(0) 第一列投影到主元列向量 z1，得到

1ˆx：1 1,1 1ˆ v=xz (21)

残差 ε则垂直于主元列向量 z1，计算获得系数 v1,1：Page 18 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

0 0 0 T T T

1 1 1 1 1 1 1 1,1 1

T00 T

1,1 TT

1 1 1 1ˆ 0 v

v⊥  = − = − =

 = =εzz εz x x z x z

xz zx

z z z z

(22)

上式说明偏最小二乘法回归核心仍是 OLS。同样，把X(0) 第二列投影在主元列向量 z2，计算得到系数 v2,1：# T00 T

2,1 TT

1 1 1 1v==xz zx

z z z z (23)

类似，获得 X(0) 每列投影在主元列向量 z2系数这些系数一个列向量 v1。下式计算列向量

TT0 0 00

11 2,1 1

1 T 0 T T00 T

11 1111

,1qv

v

v



= = = =



X z X X w Σwvzz wΣw w X X w

(24)

第五步根据最小二乘回归原理，利用列向量 v1和z1估算，并到拟合矩阵

0ˆX：00 TT

1 1 1 1ˆ==X z v X w v (25)

原始数据矩阵 X和拟合数据矩阵

0ˆX 之差便是残差矩阵 E(0)：0 0 0 0 0 0 TT

1 1 1 1ˆ= − = − = −E X X X X w v X I w v (26)

而残差矩阵 E(0) 便是进入迭代过程第二步数据矩阵 X(1)：1 0 0 0 0 T

11ˆ = = − = −X E X X X I w v (27)

数据矩阵 X(1) 和原始数据 X(0) 之间关系如图25所示。X(0)= z1

1 × q

n × 1 n × q× (v1)T

X(1) +

n × qExplained Residual Original

图25.

计算得到数据矩阵 X(1)

Page 19 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

第六步把因变量数据列向量 y(0) 投影于主元列向量 z1上，获得系数 b1。类似第四步，如图26所示，用最小二乘法计算获得系数 b1：0 0 0 T T T

1 1 1 1 1 1

T00 T

1 TT

1 1 1 1ˆ 0 b

b⊥  = − = − =

 = =εzz εz y y z y z

yz zy

z z z z

(28)

Line spanned by column vector of z1z1

1,1 1ˆ v=yz

00ˆ=−εyy

0y

图26.

y(0) 向量投影在主元列向量 z1

第七步根据 OLS原理，利用列向量 b1和z1估算因变量列向量 y，并到拟合

0ˆy：# T00 T

11 0 11

11 TT

1 1 1 1ˆ b= = =y z z z y zyzz z z z (29)

原始因变量列向量 y(0) 和拟合列向量

0ˆy 之差便是残差向量 ε(0)：0 T

0 1 0 0 0 11

T

11ˆ = = − = −z y zε y y y yzz (30)

而残差向量 ε(0) 便是进入迭代循环第二步数据向量 y(1)。如图27所示，0ˆy 解释部分 y(0)。Page 20 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

y(0)=

n × 1+

n × 1 n × 1y(1)z1 y(0)=

n × 1+

n × 1 n × 1y(1)Original

Explained

Residualb1z1 b1×

图27.

估算 y(0)

重复迭代将数据矩阵 X(1) 和数据向量 y(1) 带入如上迭代运算第二步到第七步。重复第二步得到权重系数列向量 w2：# T11

2 T11=Xy

w

Xy (31)

重复第三步，利用权重系数列向量 w2和X(1) 构造偏最小二乘回归第二主元向量

22=z X w (32)

重复第四步，把自变量数据残差矩阵 X(1) 投影于第二主元列向量 z2上获得系数向量 v2

TT1 1 11

22 2,2 2

2 T 1 T T11 T

22 2222

,2qv

v

v



= = = =



X z X X w Σwvzz wΣw w X X w

(33)

重复第五步，用列向量 v2和z2估算，并到拟合矩阵

1ˆX：11 TT

2 2 2 2ˆ==X z v X w v (34)

X(1) 和拟合数据矩阵

1ˆX 之差便是残差矩阵 E(1)，E(1)便是再次进入迭代过程第二步数据矩阵

X(2)：2 1 1 1 1 T

22ˆ = = − = −X E X X X I w v (35)

Page 21 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

X(1)= z2

1 × q

n × 1 n × q× (v2)T

X(2) +

n × qExplained Residual

图28.

计算得到数据矩阵 X(2)

X(0)= [z1, z2]

2 × q

n × 2 n × q× [v1, v2]T

X(2) +

n × qExplained Residual Original

图29.

前两个主元 z1和z1还原数据矩阵 X(0)

图25和图28相结合获得图29

这即前两个主元 z1和z1还原数据矩阵 X(0)。随着主元数量不断增多，偏最小二乘回归更精确地还原原始数据 X(0)；即说，对数据 X(0)方差解释力度越强。重复第六步，把因变量数据列向量 y(1) 投影在主元列向量 z2上获得系数 b2

T11 T

2 TT

2 2 2 2b==yz zy

z z z z (36)

重复第七步，利用 b2和z2得到拟合列向量

1ˆy：22ˆ b=yz (37)

列向量 y(1) 和拟合数据列向量

1ˆy 之差便是残差向量 ε(1)：0 2 1 1 1

22ˆ b = = − = −ε y y y y z (38)

而残差向量 ε(1) 也是进入下一次迭代过程第二步数据向量 y(2)。Page 22 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

y(1)=

n × 1+

n × 1 n × 1y(2)z1 y(1)=

n × 1+

n × 1 n × 1y(2)Original

Explained

Residualb2z2 b2×

图30.

估算 y(1)

图31结合图27和图30

这幅图中前两个主元 z1和z1还原部分数据列向量 y(0)。同理，随着主元数量不断增多，偏最小二乘回归更精确地还原原始因变量列向量 y(0)；即，对y(0)方差解释力度越强。截止目前，迭代循环已经完成两次。y(0)=

n × 1+

n × 2 n × 1y(2)OriginalExplained

Residual[b1, b2]T× [z1, z2]

2 × 1

图31.

前两个主元 z1和z1还原部分数据列向量 y(0)

Scikit-learn中PLS回归的函数为 sklearn.

cross_decomposition.

PLSRegression。主元回归 PCR是一种基于主成分分析的回归方法它在回归建模之前先对自变量进行主成分分析，将自变量降维成少量的主成分变量，然后再对这些主成分变量进行回归分析。PCR的基本思想是将自变量通过主成分分析转换成少数互相正交的主成分变量从而消除自变量之间的多重共线性问题，提高回归分析的准确性和稳定性。在降维过程中，PCR保留了自变量中最主要的信息因此相比于直接使用全部自变量的回归分析

PCR可以显著提高回归模型的准确性和可解释性。Page 23 | Chapter 17主元回归 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 3194466

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 偏最小二乘 PLS也是一种基于主成分分析和回归分析的统计建模方法它是对 PCR的一种改进，主要用于解决多重共线性和高维数据分析问题。与PCR不同的是

PLS在主成分分析的过程中不仅仅考虑了自变量之间的方差还考虑了自变量和因变量之间的协方差从而将主成分分析与回归分析相结合得到了一组互相正交的主成分变量，每个主成分变量都包含了自变量和因变量的信息，可以用于回归分析。下例展示如何使用偏最小二乘回归。这个例子还比较了本书最后一章要介绍的典型相关分请大家自行阅读学习：https://scikit -learn.

org/stable/auto_examples/cross_decomposition/plot_c ompare_cross_decomposition.

html

Page 1 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 18 Canonical Correlation Analysis

典型相关分析找到两组数据的整体相关性的最大线性组合人类生而好奇，这正是科学的火种。# Men love to wonder

and that is the seed of science.

—— 拉尔夫·爱默生 (Ralph Waldo Emerson ) | 美国思想家文学家 | 1803 ~ 1882

◄ numpy.

linalg .

eig 特征值分解

◄ numpy.

linalg.

inv 矩阵求逆

◄ seaborn.

heatmap 绘制热图

◄ seaborn.

jo intplot 绘制散点图，含边缘分布

◄ seaborn.

pairplot 成对散点图

◄ seaborn.

scatterplot 绘制散点图

◄ sklearn.

cross_decomposition.

CCA 典型相关分析

Page 2 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

典型相关分析原理线性组合视角优化问题特征值分解随机变量视角

Page 3 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 18.

1典型相关分析原理典型相关分析 (Canonical Correlation Analysis

CCA) 是一种用于探究两组变量之间关系的多元统计分析方法。其核心思想是将两组变量分别投影到新的低维空间中，使得这两组变量在新空间中的投影尽可能相关。CCA常用于处理两组多元变量之间的关系。通过 CCA可以发现这两组变量中的某些维度之间存在相关性，这种相关性可以帮助研究者更好地理解两组变量之间的关系。在CCA中，研究者需要先对两组变量进行标准化处理，然后计算它们的相关系数矩阵。着，CCA会生成一组线性组合，使得两组变量在新的低维空间中的投影尽可能相关。这些线性组合称为典型变量，相关系数则称为典型相关系数。最终的结果是一组典型变量和对应的典型相关原理下面以 X和Y为例介绍典型相关分析原理。n × p数据矩阵 X可以写成：12 n p p=X x x x

(1)

n × q数据矩阵 Y可以写成：12 n q q=Y y y y

(2)

注意，X和Y的行数一致。X朝向量 u1投影结果为 s1：11 np=s X u (3)

其中，u1的形状为 p × 1，s1的形状为 n × 1。注意，很多参考文献中，向量一般记做 a和b，投影结果一般记做 u和v；但是本书 u和v特指代表投影方向的向量，所以本章依然沿用这种记法。展开 (3) 得到如下线性组合形式：1 1 2 1,1 1 2,1 2 ,1

,1p p p

pu

u

u u u

u



 = = + + 



s x x x x x x

(4)

Y朝向量 v1投影结果为 t1：11 nq=t Y v (5)

Page 4 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 其中，v1的形状为 q × 1，t1的形状为 n × 1。p和q可以不相等，也就是说 u1、v1形状可能不同。但是 s1、t1形状相同。展开 (5) 得到如下线性组合形式：1 1 2 1,1 1 2,1 2 ,1

,1q q q

qv

v

v v v

v



 = = + + 



t y y y y y y

(6)

X ZX a1 u1 @ =

n × p n × pp × 1

n × 1

Y ZY b1 v1 @ =

n × q n × qq × 1

n × 1Maximize the correlation between U1 and V1U1V1

Standardize Project

Standardize Project

图1.

典型相关分析原理

Page 5 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

com 优化问题如图1所示典型相关分析 CCA的问题便是找到 u1和v1

使得 s1和t1相关性最大。注意，如图1所示，从数据角度来看，一般情况 X和Y都先经过标准化处理。随机变量用随机变量来写的话，S1对应 s1，T1对应 t1。随机变量 S1可以写成如下线性变换：2 T

1 1 1,1 2,1 ,1 1,1 1 2,1 2 ,1 p p p

pX

X

S u u u u X u X u X

X



 = = = + + + 



uχ

(7)

同理，随机变量 T1可以写成：2 T

1 1 1,1 2,1 ,1 1,1 1 2,1 2 ,1 q q q

qY

Y

T v v v v Y v Y v Y

Y



 = = = + + + 



vγ

(8)

S1和T1是第一对典型变量 (first pair of canonical variables)。S1和T1的相关性系数为：1 1 1 1cov ,corr ,

var , var ,STST

S S T T= (9)

这样寻找第一对典型变量的优化问题可以写成：,argmax corr , ST

uv (10)

有关随机变量的线性变换，请大家回顾《统计至简》第14章。寻找更多典型变量如图2所示再找到第一对典型变量之后依然最大化相关性系数可以找到第二对典型变量

(second pair of canonical variables )。约束条件是第一、第二对典型变量不相关。用向量来写，s2也是

12 px x x

的线性组合：Page 6 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

2 2 1 2 1,1 1 2,1 2 ,1

,2p p p

pu

u

u u u

u



 = = = + + 



s Xu x x x x x x

(11)

上式相当于 X朝u2投影。t2为

12 qy y y

的线性组合：2 1 2 1,2 1 2,2 2 ,2

,2q q q

qv

v

v v v

v



 = = + + 



t y y y y y y

(12)

上式相当于 Y朝v2投影。通过最大化的 s2和t2相关性系数，可以找到第二对典型变量。这步优化问题的约束条件为：T

T

T

T

0=

=

=

=uu

vv

uv

vu (13)

x1

x2

x3

xp 1

xps1

s2y1

y2

yqt1

t2

Canonical correlationmax(corr( s1, t1))

max(corr( s2, t2)).

s1 s2 t1 t2

图2.

线性组合角度看 CCA

随机变量 S2可以写成：Page 7 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

2 T

2 2 1,2 2,2 ,2 1,2 1 2,2 2 ,2 p p p

pX

X

S u u u u X u X u X

X



 = = = + + + 



uχ

(14)

随机变量 T2可以写成：2 T

2 2 1,2 2,2 ,2 1,2 1 2,2 2 ,2 q p q

qY

Y

T v v v v Y v Y v Y

Y



 = = = + + + 



vγ

(15)

同理，为了求解 U2和V2，约束条件为：12cov , 0

cov , 0

cov , 0

cov , 0UU

VV

UV

VU=

=

=

= (16)

考虑到一般情况下 X和Y已经标准化，E(X) = 0且E(Y) = 0。这样 E(U1) = 0，E(V1) = 0。这个步骤最多重复 min( p

q) 次，可以最多找到 min( p

q) 对典型变量。min( p, q) 对应 X和Y

的列数最小值。# 18.2从一个协方差矩阵考虑《统计至简》第13章特别介绍过协方差矩阵分块。[X, Y] 的协方差矩阵可以按图3所示形式分成四个子块。ΣXX为X的协方差矩阵，ΣYY为Y的协方差矩阵，它俩都是方阵。ΣXY、ΣYX都是 X

Y的互协方差矩阵 (cross -covariance matrix)

互为转置。S1和T1各自的方差、协方差为：T

1 1 1 1

T

1 1 1 1

T

1 1 1 1var ,

var ,

cov ,ST

ST

ST=

=

=XX

YY

XYuΣu

vΣv

uΣv (17)

如果大家对上式概念模糊的话，请回顾《统计至简》第14章。Page 8 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

p q

p

qΣXX

ΣYYΣXY

ΣYX

图3.

[X, Y] 的协方差矩阵分块这样，(9) 的相关性系数可以写成：T

11TT

1 1 1 1corr , ST=XY

XX YYuΣv

uΣ u v Σ v (18)

观察上式，大家是否发现它实际上是个瑞利商 (Rayleigh quotient )。我们在《矩阵力量》第14章了解过瑞利商。优化结果利用拉格朗日乘子法，我们可以求得优化问题的解。此处，省略推导过程，直接给出结果。向量 u是

11−−=XX XY YY YX PΣ Σ Σ Σ 的特征向量。如图4所示，P为p × p方阵。向量 v是

11−−=YY YX XX XY QΣ Σ Σ Σ 的特征向量。如图5所示，Q为q × q方阵。值得大家注意的是，如图1所示，一般 CCA算法中，数据先要经过标准化处理。也就是说图3

中真正参与运算的是相关性系数矩阵，而非协方差矩阵。本章下面要使用的 sklearn .

cross_decompo sition.

CCA 函数就是先对数据标准化，再进行 CCA

(ΣXX) 1@ΣXY @ @ (ΣYY) 1ΣYX

p × p p × qq × q q × p= P

p × p

图4.

11−−

XX XY YY YXΣ Σ Σ Σ 对应运算

Page 9 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

(ΣXX) 1@ ΣXY @ (ΣYY) 1ΣYX

p × p p × qq × q q × p@ = Q

q × q

图5.

11−−

YY YX XX XYΣ Σ Σ Σ 对应运算

18.3以鸢尾花数据为例本节以鸢尾花数据为例介绍如何完成典型相关分析。如所示，我们把鸢尾花数据4列均分为 X和Y两个矩阵。X代表花萼 (长度、宽度 )，Y代表花瓣 (长度、宽度 )。# X Y

150 × 4 150 × 2 150 × 2Sepal length

Sepal width

Petal length

Petal widthSepal Petal

图6.

把鸢尾花数据均分成两个子块典型相关分析就是将花萼数据 X的两列合成一列 s1

将花瓣数据 Y的两列合成一列 t1。过合适的组合方式，让 s1和t1的相关性最大。可以理解为找到花萼、花瓣之间 “整体”关系。图7所示为鸢尾花数据的相关性系数矩阵。请大家特别关注热图中黄色框高亮的两个子块，花萼和花瓣之间最大的相关性存在于花萼长度和花瓣长度 (0.

87)。87更大的相关性系数是0.

96，这个相关性系数是花瓣长度、宽度之间的关系，而非花萼、花瓣之间的关系。此外，CCA分析中，图7的相关性系数矩阵就相当于图3的协方差矩阵。Page 10 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

Sepal length, X1

Sepal width, X2

Petal length, X3

Petal width, X4Sepal length, X1

Sepal width, X2

Petal length, X3

Petal width, X41 0.

12 0.

87 0.

# 0.12 1

1 0.43

# 0.43 0.37

# 0.82 0.370.87 0.96

961.

图7.

鸢尾花数据的相关性系数矩阵

CCA结果通过 CCA分析，我们得到的结果如图8 (a) 所示。大家可以在本章代码中自行验算，可以发现图8 (a) 中每一列均值均为0。# S1S2T1T2

2 1012

S1 S2 T1 T2S1

S2

T1

T2(a) (b)

# 0.940.94 1.00

000.

0 0000 0

图8.

CCA分析结果图8 (b) 所示为图8 (a) 结果的相关性系数矩阵。S1和T1的相关性系数达到0.

此外，大家发现图8 (b) 中很多相关性系数为0的情况这就是本章前文介绍的优化问题约束条件。图9所示为用散点图可视化 S1和T1的关系。图9 (b) 还考虑了鸢尾花分类。观察图9 (a)，大家可能已经发现 S1和T1均方差明显不同。图10所示为 CCA结果成对特征散点图。Page 11 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

S1 2.

0 0.

0 2.

S1 2.

0 0.

0 2.

0Setosa

Versicolor

Virginica(a) (b)

图9.

S1和T1的散点图

S1 S2 T1 T2S1

S2

T1

T2

图10.

CCA结果成对特征散点图投影大家可能会好奇到底怎样的 u1、v1让S1和T1的相关性系数如此之大？sklearn.

cross_decompo sition.

CCA 函数同样返回 u1、v1，具体如图11所示。Page 12 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.92 0.46

# 0.39 0.89U

u1 u2V

v1 v2

# 0.94 1.45

# 0.33 1.57

图11.

CCA投影向量结果假设 X = [x1

x2] 已经标准化

x1和x2按如下方式线性组合得到 s1

1 150 2 1 1 2 1 20.

920.

92 0.

390.

39= = = − −s X u x x x x (19)

大家可以自己验证 u1为单位向量。同样，假设 Y = [y1

y2] 已经标准化

y1和y2按如下方式线性组合得到 t1

1 150 2 1 1 2 1 20.

940.

94 0.

330.

33= = = − −t Y v y y x x (20)

X Y

150 × 4 150 × 2 150 × 2Sepal length

Sepal width

Petal length

Petal widthSepal Petal Standardized data

(z scores)

图12.

标准化的鸢尾花数据

Page 13 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

X

150 × 2u1 @ = s1

150 × 1Y

150 × 2v1 @ = t1

150 × 1

图13.

通过投影计算 s1和t1

特征值分解下面我们利用特征值分解自行求解 u1、v1。根据图4和图5，我们先需要计算 P和Q两个方具体过程如图14、图15所示。(ΣXX) 1@ ΣXY @ @ (ΣYY) 1ΣYX = P

# 0.73 0.37

# 0.30 0.171.01

# 1.01 0.120.12 0.87 0.82

# 0.43 0.3713.72

# 13.72 13.21 13.21 0.87

# 0.82 0.43

图14.

计算矩阵 P

# 13.72 13.21 13.21 0.87

# 0.82 0.43

371.

# 1.01 0.120.12 0.87 0.82

# 0.43 0.37@ (ΣYY) 1ΣYX (ΣXX) 1@ ΣXY @ = Q

# 0.41 0.461.19

图15.

计算矩阵 Q

然后对 P和Q分别进行特征值分解，具体如图16、图17所示。注意，图17中矩阵 V的第2列向量 v2和图11中不同但是两者为倍数关系即共线。Page 14 | Chapter 18典型相关分析 | Book 6《数据有道》| 鸢尾花书从加减乘除到机器学习本PDF文件为作者草稿发布目的为方便读者在移动终端学习终稿内容以清华大学出版社纸质出版物为准。版权归清华大学出版社所有，请勿商用，引用请注明出处。代码及 PDF文件下载：https://git hub.

com/V isualize-ML

本书配套微课视频均发布在B站——生姜DrGinger

https ://space.

bilibili.

com/51 31944 66

欢迎大家批评指教，本书专属邮箱：jiang.

v isualize.

ml@gmail.

# 0.73 0.37

# 0.30 0.170.92 0.46

# 0.39 0.89 0.92 0.46

# 0.390.89 0.89

# 0.02 00P = @ @U

U 1ΛP u1 u2

图16.

矩阵 P特征值分解

021.

# 0.711.57 0.94 0.68

# 0.33 0.731.31

# 0.41 0.461.19 0.89

# 0.02 00Q = @ @V

V 1ΛQ v1 v2

图17.

矩阵 Q特征值分解

Bk6_Ch 18_01.

py完成本章 CCA分析及可视化。至此，我们完成了《数据有道》一册学习！恭喜大家，走完了鸢尾花书6/7的旅程！本册两个核心话题是回归、降维。鸢尾花书中线性回归、主成分分析被反反复复提及，原因很简单，这两种算法实际上是各种数据工具的合体。我们可以从代数、几何、数据、概率统计、线性组合、向量空间、矩阵分解、优化各种角度理解线性回归、主成分分析。这也是鸢尾花书想给大家“灌输”的理念——见树又见林。数据可以是各种各样的形式，比如数字、文本、图像等等。但是，这些数据并不是随意的，需要经过处理和清洗才能用于机器学习。Garbage in, garbage out!

我们不能让机器学习算法去学习一些无用的垃圾数据吧！而《数据有道》介绍的算法常被用于特征工程。大家已经清楚，回归、降维、分类、聚类是机器学习的四大类问题。本册关注机器学习中的回归、降维这两类问题。鸢尾花书最后一册《机器学习》则关注经典分类、聚类算法。让我们在《机器学习》一册再见！
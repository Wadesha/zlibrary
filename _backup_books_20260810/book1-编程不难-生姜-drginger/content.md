# Book1 编程不难 生姜 DrGinger Z Library

> 来源文件：pre_Book1_编程不难_生姜_DrGinger_Z_Library.txt
> 字符数（约）：569244
> 语言：zh
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Page 1  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Preface 前言

感谢首先感谢大家的信任。

作者仅仅是在学习应用数学科学和机器学习算法时，多读了几本数学书，多做了些思考和知识整理而已。知者不言，言者不知。知者不博，博者不知。水平有限，把自己有限所学所思斗胆和大家分享，作者权当无知者无畏。希望大家在B 站视频下方和Github 多提意见，让这套书成为作者和读者共同参与创作的优质作品。

特别感谢清华大学出版社的栾大成老师。从选题策划、内容创作、装帧设计，栾老师事无巨细、一路陪伴。每次和栾老师交流，我都能感受到他对优质作品的追求、对知识分享的热情。

出来混总是要还的曾经，考试是我们学习数学的唯一动力。考试是头悬梁的绳，是锥刺股的锥。我们中的绝大多数人从小到大为各种考试埋头题海，数学味同嚼蜡，甚至让人恨之入骨。

数学给我们带来了无尽的折磨。我们憎恨数学，恐惧数学，恨不得一走出校门就把数学抛之脑后、老死不相往来。

可悲可笑的是，我们其中很多人可能会在毕业的五年或十年以后，因为工作需要，不得不重新学习微积分、线性代数、概率统计，悔恨当初没有学好数学、走了很多弯路、没能学以致用， 从而迁怒于教材和老师。

这一切不能都怪数学，值得反思的是我们学习数学的方法、目的。

再给自己一个学数学的理由为考试而学数学，是被逼无奈的举动。而为数学而数学，则又太过高尚而遥不可及。

相信对于绝大部分的我们来说，数学是工具、是谋生手段，而不是目的。我们主动学数学， 是想用数学工具解决具体问题。

现在，这套书给大家一个“学数学、用数学”的全新动力——数据科学、机器学习。

数据科学和机器学习已经深度融合到我们生活的方方面面，而数学正是开启未来大门的钥匙。不是所有人生来都握有一副好牌，但是掌握“数学 + 编程 + 机器学习”绝对是王牌。这次，学习数学不再是为了考试、分数、升学，而是投资时间、自我实现、面向未来。

未来已来，你来不来？

本套丛书如何帮到你

Page 2  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 为了让大家学数学、用数学，甚至爱上数学，作者可谓颇费心机。在创作这套书时，作者尽量克服传统数学教材的各种弊端，让大家学习时有兴趣、看得懂、有思考、更自信、用得着。

为此，丛书在内容创作上突出以下几个特点： ◄ 数学 + 艺术——全彩图解，极致可视化，让数学思想跃然纸上、生动有趣、一看就懂，同时提高大家的数据思维、几何想象力、艺术感； ◄ 零基础——从零开始学习Python 编程，从写第一行代码到搭建数据科学和机器学习应用； ◄ 知识网络——打破数学板块之间的壁垒，让大家看到数学代数、几何、线性代数、微积分、 概率统计等板块之间的联系，编织一张绵密的数学知识网络； ◄ 动手——授人以鱼不如授人以渔，和大家一起写代码、用Streamlit 创作数学动画、交互 App； ◄ 学习生态——构造自主探究式学习生态环境“微课视频 + 纸质图书 + 电子图书 + 代码文件 + 可视化工具 + 思维导图”，提供各种优质学习资源； ◄ 理论 + 实践——从加减乘除到机器学习，丛书内容安排由浅入深、螺旋上升，兼顾理论和实践；在编程中学习数学，学习数学时解决实际问题。

虽然本书标榜“从加减乘除到机器学习”，但是建议读者朋友们至少具备高中数学知识。如果读者正在学习或曾经学过大学数学 (微积分、线性代数、概率统计)，这套书就更容易读了。

聊聊数学数学是工具。锤子是工具，剪刀是工具，数学也是工具。

数学是思想。数学是人类思想的高度抽象的结晶体。在其冷酷的外表之下，数学的内核实际上就是人类朴素的思想。学习数学时，知其然，更要知其所以然。不要死记硬背公式定理，理解背后的数学思想才是关键。如果你能画一幅图、用大白话描述清楚一个公式、一则定理，这就说明你真正理解了它。

数学是语言。就好比世界各地不同种族有自己的语言，数学则是人类共同的语言和逻辑。数学这门语言极其精准、高度抽象，放之四海而皆准。虽然我们中绝大多数人没有被数学女神选中，不能为人类的对数学认知开疆扩土；但是，这丝毫不妨碍我们使用数学这门语言。就好比， 我们不会成为语言学家，我们完全可以使用母语和外语交流。

数学是体系。代数、几何、线性代数、微积分、概率统计、优化方法等等，看似一个个孤岛，实际上都是数学网络的一条条织线。建议大家学习时，特别关注不同数学板块之间的联系， 见树，更要见林。

数学是基石。拿破仑曾说“数学的日臻完善和这个国强民富息息相关。”数学是科学进步的根基，是经济繁荣的支柱，是保家卫国的武器，是探索星辰大海的航船。

数学是艺术。数学和音乐、绘画、建筑一样，都是人类艺术体验。通过可视化工具，我们会在看似枯燥的公式、定理、数据背后，发现数学之美。

数学是历史，是人类共同记忆体。”历史是过去，又属于现在，同时在指引未来。”数学是人类的集体学习思考，她把人的思维符号化、形式化，进而记录、积累、传播、创新、发展。从甲

Page 3  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 骨、泥板、石板、竹简、木牍、纸草、羊皮卷、活字印刷、纸质书，到数字媒介，这一过程持续了数千年，至今绵延不息。

数学是无穷无尽的想象力，是人类的好奇心，是自我挑战的毅力，是一个接着一个的问题， 是看似荒诞不经的猜想，是一次次胆大包天的批判性思考，是敢于站在前人的臂膀之上的勇气， 是孜孜不倦地延展人类认知边界的不懈努力。

家园、诗、远方诺瓦利斯曾说：“哲学就是怀着一种乡愁的冲动到处去寻找家园。” 在纷繁复杂的尘世，数学纯粹的就像精神的世外桃源。数学是，一束光，一条巷，一团不灭的希望，一股磅礴的力量，一个值得寄托的避风港。

打破陈腐的锁链，把功利心暂放一边，我们一道怀揣一分乡愁、心存些许诗意、踩着艺术维度，投入数学张开的臂膀，驶入她色彩斑斓、变幻无穷的深港，感受久违的归属，一睹更美、更好的远方。

Page 4  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Acknowledgement 致谢

To my parents.

谨以此书献给我的母亲父亲

Page 5  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com How to Use the Book 使用本书

丛书资源本系列丛书提供的配套资源有以下几个： ◄ 纸质图书； ◄ PDF 文件，方便移动终端学习；请大家注意，纸质图书经过出版社五审五校修改，内容细节上会和PDF 文件有出入。

◄ 每章提供思维导图，纸质书提供全书思维导图海报； ◄ Python 代码文件，直接下载运行，或者复制、粘贴到Jupyter 运行； ◄ Python 代码中有专门用Streamlit 开发数学动画和交互App 的文件； ◄ 微课视频，强调重点、讲解难点、聊聊天。

在纸质书中为了方便大家查找不同配套资源，作者特别设计了如下几个标识。

引出本书或本系列其他图书相关内容提醒读者格外注意的知识点每章配套微课视频二维码配套Python代码完成核心计算和制图用Streamlit开发制作App应用介绍数学工具、机器学习之间联系数学家、科学家、 艺术家等语录代码中核心Python 库函数和讲解思维导图总结本章脉络和核心内容相关数学家生平贡献介绍每章结束总结或升华本章内容本书核心参考和推荐阅读文献

微课视频本书配套微课视频均发布在B 站——生姜DrGinger： ◄ https://space.bilibili.com/513194466

Page 6  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 微课视频是以“聊天”的方式，和大家探讨某个数学话题的重点内容，讲讲代码中可能遇到的难点，甚至侃侃历史、说说时事、聊聊生活。

本书配套的微课视频目的是引导大家自主编程实践、探究式学习，并不是“照本宣科”。

纸质图书上已经写得很清楚的内容，视频课程只会强调重点。需要说明的是，图书内容不是视频的“逐字稿”。

代码文件本系列丛书的Python 代码文件下载地址为： ◄ https://github.com/Visualize-ML Python 代码文件会不定期修改，请大家注意更新。图书配套的PDF 文件和勘误也会上传到这个GitHub 账户。因此，建议大家注册GitHub 账户，给书稿文件夹标星 (star) 或分支克隆 (fork)。

考虑再三，作者还是决定不把代码全文印在纸质书中，以便减少篇幅，节约用纸。

本书编程实践例子中主要使用“鸢尾花数据集”，数据来源是Scikit-learn 库、Seaborn 库。此外，系列丛书封面设计致敬梵高《鸢尾花》，要是给本系列丛书起个昵称的话，作者乐见“鸢尾花书”。

App 开发本书几乎每一章都至少有一个用Streamlit 开发的App，用来展示数学动画、数据分析、机器学习算法。

Streamlit 是个开源的Python 库，能够方便快捷搭建、部署交互型网页App。Streamlit 非常简单易用、很受欢迎。Streamlit 兼容目前主流的Python 数据分析库，比如NumPy、Pandas、Scikit- learn、PyTorch、TensorFlow 等等。Streamlit 还支持Plotly、Bokeh、Altair 等交互可视化库。

本书中很多App 设计都采用 Streamlit + Plotly 方案。此外，本书专门配套教学视频手把手和大家一起做App。

大家可以参考如下页面，更多了解Streamlit： ◄ https://streamlit.io/gallery ◄ https://docs.streamlit.io/library/api-reference 实践平台本书作者编写代码时采用的IDE (integrated development environment) 是Spyder，目的是给大家提供简洁的Python 代码文件。

但是，建议大家采用JupyterLab 或Jupyter notebook 作为本系列丛书配套学习工具。

简单来说，Jupyter 集合“浏览器 + 编程 + 文档 + 绘图 + 多媒体 + 发布”众多功能与一身，非常适合探究式学习。

Page 7  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 运行Jupyter 无需IDE，只需要浏览器。Jupyter 容易分块执行代码。Jupyter 支持inline 打印结果，直接将结果图片打印在分块代码下方。Jupyter 还支持很多其他语言，比如R 和Julia。

使用markdown 文档编辑功能，可以编程同时写笔记，不需要额外创建文档。Jupyter 中插入图片和视频链接都很方便。此外，还可以插入Latex 公式。对于长文档，可以用边栏目录查找特定内容。

Jupyter 发布功能很友好，方便打印成HTML、PDF 等格式文件。

Jupyter 也并不完美，目前尚待解决的问题有几个。Jupyter 中代码调试不方便，需要安装专门插件 (比如debugger)。Jupyter 没有variable explorer，要么inline 打印数据，要么将数据写到csv 或Excel 文件中再打开。图像结果不具有交互性，比如不能查看某个点的值，或者旋转3D 图形， 可以考虑安装 (jupyter-matplotlib)。注意，利用Altair 或Plotly 绘制的图像支持交互功能。对于自定义函数，目前没有快捷键直接跳转到其定义。但是，很多开发者针对这些问题都开发了插件， 请大家留意。

大家可以下载安装Anaconda，JupyterLab、Spyder、PyCharm 等常用工具都集成在Anaconda 中。下载Anaconda 的地址为： ◄ https://www.anaconda.com/ 学习步骤大家可以根据自己的偏好制定学习步骤，本书推荐如下步骤。

浏览本章思维导图， 把握核心脉络下载本章配套 Python代码文件观看微课视频，阅读本章正文内容用Jupyter创建笔记， 编程实践尝试开发数学动画、 机器学习App 翻阅本书推荐参考文献

学完每章后，大家可以在平台上发布自己的Jupyter 笔记，进一步听取朋友们的意见，共同进步。这样做还可以提高自己学习的动力。

意见建议欢迎大家对本系列丛书提意见和建议，丛书专属邮箱地址为： ◄ jiang.visualize.ml@gmail.com 也欢迎大家在B 站视频下方留言互动。

Page 8  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Contents 目录

Page 9  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

Introduction 绪论动手编程；知其然，不需要知其所以然

## 0.1 本册在全套丛书的定位

鸢尾花书共有7 册，分为三大板块——编程、数学、实践。

《编程不难》是鸢尾花书的第一本，也是“编程”板块的第一本，着重介绍如何零基础入门学 Python 编程。“编程”板块的第二本则探讨如何用Python 完成数学、数据可视化。

虽然《编程不难》主要讲解Python 编程，但是也离不开数学。本书尽量避免讲解数学概念公式，而是用图形、近乎口语化的语言描述程序设计、数据分析、机器学习背后常用数学思想。我们把理解这些数学工具的任务放在了鸢尾花书“数学”板块，也叫“数学三剑客”——《数学要素》

《矩阵力量》《统计至简》。

《编程不难》正文提供代码示例和讲解，而且会提供练习题目。每章还会配套Jupyter Notebook 代码文件。

编程 《编程不难》

《可视之美》

数学 《矩阵力量》

《统计至简》

实践 《数据有道》

《机器学习》

丛书板块 《数学要素》

图 1. “鸢尾花书”板块布局

Page 10  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 0.2 结构：8 大板块

本书一共有36 个话题，可以归纳为8 大板块——预备、语法、绘图、数组、数据、数学、机器学习、应用。

预备编程不难聊聊巨蟒 JupyterLab，用起来 LaTeX数学公式 Python数据类型 Python运算 Python控制结构 Python函数 Python面向对象编程 Python语法，边学边用语法聊聊可视化二维和三维可视化 Seaborn可视化数据绘图数学应用使用Spyder Streamlit搭建Apps Streamlit机器学习Apps NumPy索引和切片 NumPy常见运算 NumPy数组变形 NumPy数组规整 NumPy线性代数聊聊NumPy 数组 Scikit-Learn数据 Scikit-Learn回归 Scikit-Learn降维 Scikit-Learn分类 Scikit-Learn聚类 Scikit-Learn机器学习机器学习数据 Pandas索引切片 Pandas拼接和合并 Pandas重塑和透视 Pandas常见运算 Pandas时间序列聊聊Pandas SymPy符号数学 SciPy数学运算 Statsmodels统计模型

图 2. 《编程不难》板块布局

预备这部分有3 章，占全书1/12。全书第1 章聊了聊Python 编程，Python 和可视化、数学、机器学习有什么关系。这一章最关键的任务是成功安装并测试Anaconda。

## 第2 章介绍如何使用JupyterLab。对于鸢尾花书系列图书，JupyterLab 特别适合大家进行探究

式学习。第2 章中，学习并熟练使用快捷键可以极大提高生产力。

## 第3 章介绍如何用LaTeX 语言在JupyterLab markdown 中编写常用数学表达。注意，本章不

会介绍如何利用LaTeX 撰写论文等文档，感兴趣的读者可以自行学习。

语法这部分有6 章，占全书1/6，主要介绍Python 基本语法。

## 第4 章主要介绍注释、缩进、变量、包、Python 风格等基础概念。

Page 11  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 第5 章讲解Python 常用数据类型，比如数字、字符串、列表、字典。这一章还介绍了线性代

数中的矩阵和向量这两个概念。

## 第6 章讲解Python 常见运算，比如算术、比较、逻辑、赋值、成员、身份等运算符。学习

时，请大家注意这些运算符的优先级。

## 第7 章介绍Python 控制结构，比如条件语句、循环语句、迭代器等概念。这一章还介绍了线

性代数中的向量内积和矩阵乘法这两种重要数学概念，请大家务必掌握其运算规则。

## 第8 章介绍Python 函数，比如自定义函数、匿名函数，以及如何构造模块、库。

## 第9 章简介Python 面向对象编程，其中包括属性、方法、装饰器、父类、子类等概念。这一

章仅仅介绍了Python 面向对象编程的冰山一角。

绘图可视化是鸢尾花书核心的特色之一，所以特别创作了《可视之美》一册专门讲解数学、数据可视化。《编程不难》中的绘图仅仅蜻蜓点水介绍了本册常用的可视化工具，因此这部分仅仅安排了3 章，占全书1/12，主要介绍Matplotlib、Plotly、Seaborn 这三个库中最常用的几种可视化函数。

## 第10 章首先介绍了一幅图的重要组成元素，并讲解如何用Matplotlib 和Plotly 绘制线图。

## 第11 章介绍几种最常用的二维和三维可视化方案，比如散点图、等高线图、热图、网格面等

等。大家如果对可视化特别感兴趣的话，也可以平行学习《可视之美》。

## 第12 章主要介绍如何用Seaborn 完成样本数据统计描述，这章讲解的可视化方案包括直方

图、小提琴图、箱型图散点图、概率密度分布等等。

数据这个板块主要介绍NumPy，一共有6 章，占全书1/6。NumPy 是一个用于科学计算和数据分析的Python 库。它提供了高效的多维数组对象，以及用于对这些数组执行各种数学、逻辑、统计操作的函数。在机器学习中，NumPy 具有重要的作用，因为它为数据处理、数值计算和数组操作提供了强大的工具，为机器学习算法的实现和优化提供了基础支持。

## 第13 章介绍数组、数列、网格数据、随机数、导入、导出等NumPy 库基本概念。

## 第14 章介绍如何对NumPy 数组进行索引和切片。请大家务必注意视图、副本这两个概念。

## 第15 章介绍NumPy 常见运算，比如基本算术、代数、统计运算。请大家务必掌握广播原

则。

## 第16 章介绍NumPy 中常用的各种数组变形方法。第17 章进一步介绍了数组堆叠、重复、分

块等规整操作。

Page 12  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 第18 章走马观花介绍地介绍NumPy 的linalg 模块中常用的线性代数工具，比如向量的模、

向量内积、矩阵乘法、Cholesky 分解、特征值分解、奇异值分解等。想要进一步深入学习线性代数工具，请大家参考鸢尾花书《矩阵力量》。

数组这个板块主要介绍Pandas，一共有6 章，占全书1/6。Pandas 是一个用于数据分析和数据处理的Python 库，它提供了高效的数据结构和数据操作工具，特别适用于处理和分析结构化数据。

在机器学习中，Pandas 具有重要的作用，因为它能高效地加载、处理、清洗、转换、探索、分析数据，为机器学习建模和分析提供了强大的支持。

## 第19 章介绍如何创建数据帧DataFrame，以及常见数据帧操作。

## 第20 章讲解如何对Pandas DataFrame 进行索引和切片，比如提取特定行列、特定行列、条件

索引、多层索引等等。

## 第21 章讲解如何利用concat()、join()、merge() 方法对DataFrame 进行拼接和合并。

## 第22 章介绍如何用pivot()、stack()、unstack() 方法对DataFrame 进行重塑和透视。

## 第23 章介绍Pandas 中各种运算，比如四则运算、统计运算，以及用groupby()、apply() 方法

完成聚合和自定义操作。

## 第24 章讲解Pandas 时间序列数据，包括缺失值、移动平均、统计分析等操作。

数学这个板块主要介绍SymPy、SciPy、Statsmodels 三个库，一共有3 章，占全书1/12。

## 第25 章介绍SymPy，SymPy 是一个 Python 的符号数学计算库。大家可以用这一章回顾或了

解常用的代数、微积分、线性代数概念。

## 第26 章讲解如何用SciPy 完成插值、积分、线性代数、优化、统计等运算。

## 第27 章介绍Statsmodels 模块，并介绍如何利用Statsmodels 完成线性回归、主成分分析、概

率密度估计。

机器学习这个板块主要介绍Scikit-learn，一共有6 章，占全书1/6。Scikit-learn 是一个用于机器学习和数据挖掘的Python 库，它建立在NumPy、SciPy 和Matplotlib 等库的基础之上，提供了丰富的机器学习算法、工具和函数，用于实现各种机器学习任务，如分类、回归、聚类、降维、模型选择等。

## 第28 章简述了有标签数据、无标签数据、回归、降维、分类、聚类等机器学习概念。

Page 13  |  正文前  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 第29 章介绍了Scikit-learn 中数据集、产生样本数据、处理缺失值、处理离群值、特征缩放

等方法。

第30 ~ 33 章分别介绍了回归、降维、分类、聚类四个机器学习问题。

应用这一板块有3 章，占全书1/12。

## 第34 章介绍如何使用Spyder 完成Python 编程开发。这一章介绍的Spyder 是为下一章开发

Streamlit 提供IDE 工具。

## 第35 章介绍如何用Streamlit 搭建应用App。Streamlit 是一个用于创建交互式数据应用程序的

Python 库。它的主要目标是让数据科学家、工程师和开发人员能够快速、轻松地将数据融入到应用程序中，而无需深入了解前端开发。使用 Streamlit，可以将数据可视化、机器学习模型、分析结果等内容转化为具有用户界面的应用，从而方便地与用户进行交互。

## 第36 章中，我们将用Streamlit 开发几个数学学习、机器学习应用Apps。

## 0.3 特点：知其然，不需要知其所以然

《编程不难》极力避免“Python 语法工具书”这种大而全范式。

《编程不难》想要以轻松、图解方式，为零基础入门读者提供可读性高、学以致用的内容。

学习时，期待大家立刻有“收获感”，并有持续动力、兴趣继续深入学习。因此在创作这本书时， 作者定下的目标是——力争让大家在阅读本书时兴致勃勃、眼界大开，读完本书后感觉收获满满、意犹未尽。

作为鸢尾花书系列的第一本，《编程不难》格外强调“零基础入门”学习Python，因此本书力争给大家提供“保姆式”手把手式的教学体验；鉴于此，如果Python 有经验的读者觉得本书在行文上显得“婆婆妈妈”，请体谅。

值得反复强调的是，学习Python 编程时，希望大家一定要吸取英语学习失败的教训，不能死磕语法。千万不要死记硬背，一定要边学边用、活学活用、以用为主。

由于《编程不难》强调“零基础”学习Python 编程，不需要大家掌握Python 库中常用函数背后的数学工具、数学思想；也就是说，“知其然，不需要知其所以然”。即便《编程不难》提到了某些数学工具，我们也只用文字和图像方式介绍，因此大家在本书中不会看到各种编号公式。

下面，让我们正式开启鸢尾花书第一本《编程不难》的学习之旅。

Page 1  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Python 101 聊聊“巨蟒” 有用废话多是ChatGPT 生成，安装测试Anaconda 是关键

悟知天地纵横交错，万物相生相联之网。而你我也系其中一环，一念一动皆牵动周身。

There is urgency in coming to see the world as a web of interrelated processes of which we are integral parts, so that all of our choices and actions have consequences for the world around us.

—— 阿尔弗雷德·怀特海 (Alfred Whitehead)  |  英国数学家、哲学家  |  1861 ~ 1947

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

Page 2  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 1.1 ChatGPT：用Python 写成的人工智能工具

本节很多问题都采用ChatGPT 答案，作者对回答文本略加编辑。本书中，ChatGPT 的答案用标识。建议大家在学习时，不管是概念、程序、数学上遇到问题，都可以使用类似ChatGPT 工具作为助手。值得注意的是，ChatGPT 经常犯错，大家注意甄别。

什么是ChatGPT？

ChatGPT 是一种基于自然语言处理 (Natural Language Processing, NLP) 技术的人工智能（AI）应用程序，它是由OpenAI 公司开发的一种大规模预训练语言模型。ChatGPT 使用深度神经网络来模拟人类的对话过程，它可以理解和生成人类语言，可以用于实现聊天机器人、智能客服、智能助手等应用。ChatGPT 还可以帮助用户进行文本自动生成、文本摘要、文本分类、情感分析等任务。ChatGPT 使用Python 编程语言进行搭建。在搭建ChatGPT 时，OpenAI 使用了Python 的深度学习框架TensorFlow 和 PyTorch，以及一些其他的Python 库和工具来完成。

## 1.2 Python？巨蟒？

Python 的用途极为广泛，特别是在机器学习、深度学习领域。Python 免费开源，语言语法友好，而且社区活跃。这就是为什么“鸢尾花书”系列会选择Python 作为编程语言。

图 1. Python 应用场景

我们为什么要学Python？

如图 1 所示，Python 具有广泛的用途，比如： ► 机器学习：Python 在数据科学和机器学习领域非常受欢迎，因为它有很多强大的库和工具，如 NumPy、Pandas、Scikit-learn 等。

► 深度学习：Python 的深度学习工具，比如PyTorch、TensorFlow，常用来开发各种人工智能应用，比如智能设备、无人驾驶、自然语言处理工具等。

Page 3  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► Web 开发：Python 可以用于Web 开发，有许多流行的Web 框架，如Django、Flask 等。

► 自动化脚本：Python 可以用于自动化任务，例如自动备份、自动化测试、爬虫等。

► 游戏开发：Python 可以用于游戏开发，如Pygame 等库和工具。

► 系统管理和网络编程：Python 可以用于系统管理和网络编程，例如网络爬虫、服务器开发、安全工具等。

什么是Python？

Python 是一种高级编程语言，由Guido van Rossum 于1991 年首次发布。它是一种解释型语言，使用动态类型系统和自动内存管理。Python 具有简单易学、易于阅读和编写、可移植性强等特点，广泛应用于Web 开发、数据分析、人工智能、科学计算、自动化等领域。Python 语言具有丰富的标准库和第三方库，可支持各种编程任务，例如文件处理、网络编程、GUI 开发、图像处理、 数据可视化、机器学习等。Python 的语法简洁清晰，易于阅读和理解，因此也被广泛应用于教育和科研领域。Python 语言的解释器可用于不同的操作系统，例如Windows、MacOS、Linux 等，因此Python 具有很好的跨平台性。

图 2 所示为本书涉及到的9 个重要的Python 数学运算和可视化库。

scikit

图 2. 《编程不难》涉及到的Python 库

Python 中，什么是模块、包、库？

在Python 中，模块、包、库是三个常见的概念。它们的含义如下： 模块 (Module)：是一个Python 程序文件，包含了一组相关的函数、类、变量和常量等，可供其他程序引用。Python 中的模块是一种可重用的代码组件，可用于将相关的代码组织到一起，以便更好地管理和维护代码。一个模块可以包含多个函数、类、变量和常量等，可以被其他模块或程序引用和调用。

包 (Package)：是一组相关的模块的集合，用于组织Python 代码的层次结构。一个包是一个文件夹，其中包含其他模块或子包。包是一种通过模块命名空间进行模块组织的方式，可用于更好地组织和管理大型代码库。

库 (Library)：是由一组模块和包组成的软件组件，提供了一系列函数、类、变量和常量等，用于解决特定问题。Python 标准库是 Python 官方提供的一组库，包含了大量的模块和功能，可以直接使用。此外，还有第三方库，如NumPy、Pandas、Matplotlib 等， 用于数据处理、科学计算、可视化等领域。

需要注意的是，模块是最小的可重用代码单元，而包和库是由多个模块组成的更大的结构。在Python 中，通常使用import 语句来引入需要使用的包、库或模块。

Page 4  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com scikit

图 3. 《编程不难》每章涉及的核心工具

我们为什么要学Python？

作者认为，面向人工智能时代的教育，特别是数学教育，必须结合编程、可视化、实际应用。而 Python 既是编程工具，也拥有大量可视化工具，同时可以用来完成各种数据科学、机器学习任务。

基于这样的考虑，鸢尾花书整套图书在创作时都采用了“编程 + 可视化 + 数学 + 机器学习”这个内核，只不过各个分册的侧重各有不同。

对于初高中生、大学生，学习Python 有很多好处，比如： ► 培养编程思维：Python 作为一种编程语言，可以帮助大家培养编程思维能力。大家可以通过编写简单的程序和解决各种问题，锻炼逻辑思考、问题解决和创造力等能力。

► 高效地学习数学及其他学科：将公式、模型写成Python 代码的过程，本身就是一种“习题”。而且这类习题比传统课本习题更能激发大家的兴趣。

► 图形化强化记忆：公式、定理、定义、解题技巧 … 大家考完试也就忘记了。但是利用Python 编程，把公式、定理、定义变成一幅幅活生生的图形之后，这些概念将会深深地刻在大家脑中，甚至一辈子不会忘记。

► 提高学习效率：Python 可以用于自动化各种重复性的任务，如数据处理、文本处理等。大家可以通过编写Python 程序来自动化这些任务，从而节省时间和精力，提高学习效率。

Page 5  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 为未来的学习和职业做准备：Python 是一种非常流行的编程语言，它在数据科学、机器学习、人工智能等领域有很多应用，大家可以通过学习Python，为未来的学习和职业做准备，提前掌握一些必要的技能和知识。

► 增强实践能力：学习Python 可以让大家更容易地将学到的知识应用到实践中，例如编写简单应用程序、游戏、网站等，这有助于大家增强实践能力和探索新领域的能力。

► 培养团队合作意识：学习Python 可以让大家更容易地与他人合作，例如在编写程序时可以分工合作、交流想法等，这有助于培养团队合作意识和沟通能力。

未来已来，你来不来？

怎么学Python？

和汉语、英语一样，Python 也是语言。只不过，Python 是人和机器交互的语言。Python 的语法有绝对的对错，不能模棱两可。错误的命令，要么出bug，要么得出错误的结果。

在学习 Python 的过程中，大家一定要吸取英语教育的教训。很多人之所以在学了十几年的英语之后仍然不会说，就是因为他们只注重死记硬背词汇、语法，而没有真正把语言用起来，进行口头和书面交流。

因此，在学习 Python 时，大家不妨“功利”一些，边学边练——在学习中就马上开始编码code 和调试debug。

学习Python 和学习英语有什么相似之处？

学习Python 和学习英语有一些相似之处，以下是其中一些： 都需要掌握基础知识：学习Python 和学习英语都需要掌握基础知识，Python 的基础语法、数据类型、流程控制语句、函数等，英语的基本词汇、语法、发音等。

都需要不断练习：学习Python 和学习英语都需要不断地练习，Python 需要编写程序来实践，英语需要口语练习和写作练习。

都需要实践和应用：学习Python 和学习英语都需要不断地实践和应用，Python 可以应用到数据处理、人工智能、游戏开发等领域，英语可以应用到国际交流、留学、工作等方面。

都需要耐心和坚持：学习Python 和学习英语都需要耐心和坚持，需要花费大量时间和精力来学习和练习，才能达到良好的掌握和应用水平。

总之，学习Python 和学习英语都需要掌握基础知识、不断练习、实践和应用，同时也需要耐心和坚持。虽然二者是不同的领域， 但都是对自己未来发展非常有帮助的技能。

鸢尾花书有编程、可视化、数学、机器学习这几个重要的元素，而这几个元素都离不开Python。下面我们逐一聊一下。

## 1.3 Python 和可视化有什么关系？

Python 和可视化有很密切的关系。Python 中有很多强大的可视化库和工具，可以帮助用户对数据进行可视化呈现。

以下是Python 和可视化的一些关系：

Page 6  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 数据可视化：Python 中有许多数据可视化的库，例如Matplotlib、Seaborn、Plotly 等，可以帮助用户将数据可视化呈现出来，从而更好地理解数据的分布、趋势等信息。本书的绘图部分将蜻蜓点水地讲解Matplotlib、Seaborn、Plotly 常用绘图命令。“鸢尾花书”的《可视之美》一册将专门讲解数据可视化这一话题。

► 图像处理：Python 中有许多图像处理的库，例如OpenCV 等，可以帮助用户进行图像处理和分析， 同时也可以将处理后的图像进行可视化呈现。

► 交互式可视化：Python 中也有许多用于交互式可视化的库，例如Bokeh、Altair 等，可以帮助用户建立交互式的数据可视化应用程序。

► 3D 可视化：Python 中也有许多用于3D 可视化的库，例如Mayavi、VisPy 等，可以帮助用户对三维数据进行可视化呈现。

## 1.4 Python 和数学有什么关系？

Python 和数学有着密切的关系。Python 是一种非常适合数学建模和数据分析的编程语言，拥有大量的数学计算库和工具。

以下是Python 和数学的一些关系： ► 数学计算：Python 中有很多用于数学计算的库和工具，例如NumPy、SciPy 等，可以帮助用户进行矩阵运算、微积分、最优化、统计分析等数学计算任务。

► 数据分析：Python 中有很多用于数据分析的库和工具，例如Pandas、Matplotlib、Seaborn 等，可以帮助用户对数据进行统计分析、可视化呈现等。

► 数学建模：Python 中还有很多用于数学建模的库和工具，例如SymPy 等，可以帮助用户进行数学建模和优化任务。

► 教学和研究：Python 也被广泛应用于数学教学和研究领域，例如用Python 实现数学实验、数学模型的探索、算法的实现等。

## 1.5 Python 和机器学习有什么关系？

Python 与机器学习有非常密切的关系。Python 是一种简单易学、可读性强的编程语言，同时也拥有丰富的第三方库和工具，这使得Python 成为机器学习领域的重要工具之一。

机器学习是一种应用人工智能的技术，通过让计算机从数据中学习并改善性能，来实现对未知数据的预测和决策。

Python 在机器学习领域的应用非常广泛，主要有以下几个方面： ► 数据处理和分析：Python 中有许多用于数据处理和分析的库，例如Pandas、NumPy 和SciPy，这些库能够帮助用户轻松地处理和分析数据。

► 机器学习框架：Python 中也有许多用于机器学习的框架，例如TensorFlow、PyTorch 和Scikit-Learn 等，这些框架可以帮助用户更加高效地进行机器学习建模和预测。

Page 7  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 可视化工具：Python 中的Matplotlib 和Seaborn 等可视化库，可以帮助用户更加清晰地理解数据和模型，以及呈现结果。

► 自然语言处理：Python 中的自然语言处理库，例如NLTK 和Spacy 等，可以帮助用户进行文本数据的处理、分析和预测。

什么是机器学习？

机器学习是一种人工智能技术，它使计算机系统能够通过数据和经验自主学习和改进，而无需显式地编程指令。简单来说，机器学习是通过训练算法从数据中学习模式和规律，然后利用这些模式和规律来进行预测或决策。在机器学习中，模型是通过训练算法从大量数据中学习而来的，这些数据被称为训练数据集。训练数据集包含已知结果的输入输出对，这些输入输出对用于训练模型来预测未知数据的输出。训练数据集中的数据越多，训练时间越长，模型就越准确。机器学习可以应用于各种领域，例如语音识别、图像识别、自然语言处理、推荐系统和金融分析等。它已成为当今科技领域中最热门和最具前途的领域之一。

## 1.6 集成开发环境

Python 有很多常用的IDE (集成开发环境)，比如： ► JupyterLab：基于Web 的交互式开发环境，支持多种编程语言，包括Python，可以快速编写、测试和共享代码，非常适合数据科学和机器学习领域。作者认为，JupyterLab 和Jupyter Notebook 非常适合大家做探究式学习。目前，《编程不难》、《可视之美》两册的配套的代码多是Jupyter 笔记。这个话题后文将详细介绍如何使用JupyterLab。

► Spyder：基于Qt 开发的Python IDE，提供了一个集成的开发环境，包括编辑器、调试器和控制台， 非常适合科学计算和数据分析。虽然“鸢尾花书”剩余几册的代码都是在Spyder 中完成，建议初学者还是在JupyterLab 中分段运行代码。对于MATLAB 转Python 的读者来说，Spyder 可能是最容易上手的IDE。在所有的Python IDE 中，Spyder 最像MATLAB。

► PyCharm：JetBrains 公司开发的跨平台Python IDE，提供了许多功能，包括代码智能提示、代码自动完成、调试和单元测试等。建议有Python 开发经验的读者使用PyCharm 运行本书代码。

什么是集成开发环境？

集成开发环境 (Integrated Development Environment，简称IDE) 是一种用于软件开发的工具。它通常包括一个代码编辑器、一个调试器和一个构建工具，以及其他功能，例如自动补全、语法高亮、代码重构等。IDE 的目的是提供一个集成的工作环境，使开发人员能够更高效地编写、调试和测试代码。使用IDE 可以极大地提高开发效率。例如，它可以帮助开发人员在编写代码时自动补全函数名称、参数等，减少打错代码的风险；它可以提供一些调试工具来检测和修复代码中的错误，使得开发人员更容易发现问题；它可以通过自动构建工具来编译和构建代码，减少手动操作的繁琐过程。总之，IDE 是一种开发人员必备的工具，可以让开发人员更加专注于编写高质量的代码。

表 1. 比较三个常用的IDE 维度 JupyterLab Spyder PyCharm 适用场景数据科学、机器学习、交互式科学计算、数据分析通用编程、开发编辑器基于Web 的文本编辑器 Qt 构建的文本编辑器 IntelliJ IDEA 编辑器调试器内置的交互式调试器内置的调试器内置的调试器插件支持丰富的插件生态系统插件支持较少丰富的插件生态系统社区支持由Jupyter 项目支持由Spyder 社区支持由JetBrains 公司支持

Page 8  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 扩展性支持自定义和扩展可以自定义外观和行为支持自定义和扩展学习曲线平缓友好稍微陡峭收费与否免费免费有免费和付费版本平台支持支持Windows、Mac 和Linux 支持Windows、Mac 和Linux 支持Windows、Mac 和Linux

Anaconda Anaconda 可谓“科学计算全家桶”，包含科学计算领域可能用到的大部分 Python 工具，包括 Python 解释器、常用的第三方库、包管理器、IDE 等。前文提到的JupyterLab、Spyder、PyCharm 这三个IDE 都在Anaconda 中。

什么是Anaconda？

Anaconda 是一个流行的Python 发行版，由Anaconda, Inc.开发和维护，旨在为数据科学、机器学习和科学计算提供一个全面的工具包。Anaconda 集成了许多常用的Python 库和工具，如NumPy、SciPy、Pandas、Matplotlib、Scikit-learn、Jupyter Notebook 等。

它还包括一个名为conda 的软件包管理器，可以帮助用户安装、更新和管理Python 库和依赖项。Anaconda 还提供了一个名为 Anaconda Navigator 的图形用户界面，用户可以通过这个界面轻松地管理他们的Python 环境、安装和卸载库、启动Jupyter Notebook 等操作。除了Python 环境和库之外，Anaconda 还包括许多其他工具和应用程序，如Spyder、PyCharm、VS Code、R 语言环境等等，使得它成为数据科学家和研究人员的首选工具之一。Anaconda 可以安装在多个平台上，包括 Windows、Linux 和 Mac OS X。

安装Anaconda 下文手把手教大家如何在Windows 上安装、测试Anaconda，有经验的读者可以跳过。

对于Mac 用户，大家可以参考如下链接安装Anaconda： https://docs.anaconda.com/anaconda/install/mac-os/ 要是想特别安装某个版本的Python，请参考： https://pythonhowto.readthedocs.io/zh_CN/latest/install.html 注意，Anaconda 安装后大概占用5G 空间。有Python 开发经验的读者，可以根据需求自行分别安装 JupyterLab、Spyder、PyCharm。

在Windows 上安装Anaconda 可以按照以下步骤进行： a) 下载。在Anaconda 官网 (https://www.anaconda.com/) 下载适合大家操作系统的Anaconda 版本， 选择对应的Python 版本 (一般建议选择最新版Python3.x)，并下载对应的安装程序。注意，Anaconda 不断推出新版本，大家下载的版本号肯定和下图的版本号不同。建议大家从官网下载最新版本安装程序。

图 4. 安装程序图标

b) 运行安装程序：下载完毕后，双击下载文件运行安装程序。在安装程序打开后，点击“Next”进入下一步。

Page 9  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 5. 运行安装程序

c) 阅读协议：阅读协议并同意“I Agree”，然后点击“Next”。

图 6. 阅读协议

d) 安装类型：推荐默认“Just Me”；对于多用户PC，可以选择“All Users”；然后点击“Next”。

图 7. 安装类型

e) 安装路径：可以指定Anaconda 的安装路径 (建议零基础读者选择默认路径)，然后点击“Next”。

Page 10  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 8. 安装路径

f) 配置环境变量：选择是否将Anaconda 添加到系统环境变量中，建议勾选该选项，这样就可以在命令行中使用Anaconda 的工具了。然后点击“Install”进行安装。

图 9. 安装选择

g) 等待安装完成：安装过程可能持续10 分钟左右。等待安装完成后，会弹出“Installation Complete” 对话框，点击“Next”。如果这步持续时间过长 (超过一小时)，建议强制停止安装，删除安装包。关机再开机，重新下载安装包从头开始再尝试安装。

图 10. 等待安装完成

Page 11  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 11. 安装完成

图 12. 广告时间，点Next

h) 完成安装：点击“Finish”完成Anaconda 的安装。之后会跳出两个网页，不需要理会，关闭即可。

图 13. 确认完成

安装完成后，可以在“开始菜单”中找到Anaconda 的安装目录，并启动“Anaconda Navigator”来使用 Anaconda 的工具和功能。同时，也可以在命令行中使用Anaconda 的工具和命令，例如使用“conda”命令来管理Python 的虚拟环境和安装依赖包等。

测试JupyterLab 这是本节最后，也是最关键的一个任务。

要打开并测试JupyterLab，可以按照以下步骤进行：

Page 12  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a) 找到并打开Anaconda Navigator (需要1 分钟左右，稍安勿躁)，点击JupyterLab 对应的Launch。

马上一个网页将会跳出来，建议大家默认使用Chrome 浏览器，Firefox 或Edge 也都可以。

图 14. Anaconda Navigator 界面

b) 进入JupyterLab 界面，点击Notebook (Python 3)，创建Jupyter Notebook。

图 15. JupyterLab 界面

图 16. 创建Jupyter Notebook

c) 在下面窗口中输入，1 + 2，然后点击“Ctrl + Enter”快捷键，运行并得到3 这个结果。大家也可以尝试 “Shift + Enter”快捷键，运行代码同时生成新区块，大家自己可以先玩一会。下一节将专门讲解如何使用 JupyterLab。

Page 13  |  Chapter 1 聊聊“巨蟒”  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Ctrl + Enter

图 17. 运算

这一节的习题只需要大家完成Anaconda 安装，并测试JupyterLab。

* 这道题目很基础，本书不给答案。

Page 1  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Using JupyterLab JupyterLab，用起来！

特别适合探究式学习，代码、绘图、脚本、公式 …

教育不是为生活做准备；教育就是生活本身。

Education is not a preparation for life; education is life itself.

—— 约翰·杜威 (John Dewey)  |  美国著名哲学家、教育家、心理学家  |  1859 ~ 1952

◄ ax.plot_wireframe() 用于在三维子图ax 上绘制网格曲 ◄ fig.add_subplot(projection='3d') 用于在图形对象fig 上添加一个三维子图 ◄ matplotlib.pyplot.figure() 用于创建一个新的图形窗口或画布，用于绘制各种数据可视化图表 ◄ matplotlib.pyplot.grid() 在当前图表中添加网格线 ◄ matplotlib.pyplot.plot() 绘制折线图 ◄ matplotlib.pyplot.scatter() 绘制散点图 ◄ matplotlib.pyplot.subplot() 用于在一个图表中创建一个子图，并指定子图的位置或排列方式 ◄ matplotlib.pyplot.subplots() 创建一个包含多个子图的图表，返回一个包含图表对象和子图对象的元组 ◄ matplotlib.pyplot.title() 设置当前图表的标题，相当于对于特定轴ax 对象ax.set_title()

◄ matplotlib.pyplot.xlabel() 设置当前图表x 轴的标签，相当于对于特定轴ax 对象ax.set_xlabel()

◄ matplotlib.pyplot.xlim() 设置当前图表x 轴显示范围，相当于对于特定轴ax 对象ax.set_xlim() 或 ax.set_xbound()

◄ matplotlib.pyplot.xticks() 设置当前图表x 轴刻度位置，相当于对于特定轴ax 对象ax.set_xticks()

◄ matplotlib.pyplot.ylabel() 设置当前图表y 轴的标签，相当于对于特定轴ax 对象ax.set_ylabel()

◄ matplotlib.pyplot.ylim() 设置当前图表y 轴显示范围，相当于对于特定轴ax 对象ax.set_ylim() 或 ax.set_ybound()

◄ matplotlib.pyplot.yticks() 设置当前图表y 轴刻度位置，相当于对于特定轴ax 对象ax.set_yticks()

◄ numpy.arange() 生成一个包含给定范围内等间隔的数值的数组 ◄ numpy.linspace() 生成在指定范围内均匀间隔的数值，并返回一个数组 ◄ numpy.meshgrid() 用于生成多维网格化数据 ◄ plotly.express.data.iris() 从Plotly 库里加载鸢尾花数据集 ◄ plotly.express.scatter() 绘制可交互的散点图 ◄ plotly.graph_objects.Figure() 用于创建一个新的图形对象，用于绘制各种交互式数据可视化图表 ◄ plotly.graph_objects.Surface() 绘制可交互的网格曲面 ◄ seaborn.scatterplot() 绘制散点图

Page 2  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 2.1 啥是JupyterLab？

JupyterLab 集合“浏览器 + 编程 + 文档 + 绘图 + 多媒体 + 发布”众多功能与一身。“鸢尾花书”不同场合反复提过，对于初学者，哪怕是有开发经验的读者来说，JupyterLab 都特别适合探究式学习。目前 《数学要素》、《可视之美》中，几乎所有的代码都是用JupyterLab 写的。如果大家对JupyterLab 反馈正面，其他分册也考虑提供Jupyter Notebook 配套文件。

这一话题将和大家聊一聊如何使用JupyterLab。注意，本节不求“事无巨细”地介绍JupyterLab，而是要全景地浏览JupyterLab 的主要功能，保证“够用就好”，以便大家轻装上阵。

对于JupyterLab 的外观、窗口布局等细节问题，这个话题就不展开了，大家如果有需要可以很容易搜索到结果。当大家对JupyterLab 熟悉之后，建议大家了解如何用JupyterLab 的debug 功能。此外，很多开发者专门针对JupyterLab 开发各种小插件，很多插件的确能提高工作效率，也建议大家自行了解。

大家JupyterLab 用熟之后，会发现这一节最重要的内容只有——快捷键。

什么是JupyterLab？

JupyterLab 是一个交互式开发环境，可以让用户创建和共享Jupyter 笔记本、代码、数据和文档。它是Jupyter Notebook 的升级版本，提供了更强大的功能和更直观的用户界面。JupyterLab 支持多种语言，包括Python、R、Julia 和Scala 等。它还提供了多个面向数据科学的扩展，如JupyterLab Git、JupyterLab LaTeX 和JupyterLab Debugger 等，使得数据科学家和开发人员可以更加高效地进行数据分析、机器学习和模型开发等工作。JupyterLab 的主要特点包括：基于web 的用户界面，可以让用户同时在一个界面中管理多个笔记本和文件。支持多种文件格式，包括Jupyter 笔记本、Markdown 文档、Python 脚本和CSV 文件等。可以通过拖放和分栏等方式来组织和管理笔记本和文件。提供了一组内置的编辑器、终端、文件浏览器和输出查看器等工具。可以通过扩展系统来扩展和定制JupyterLab 的功能。

## 2.2 使用JupyterLab：立刻用起来

新建Notebook 大家首先通过Anaconda Navigator (上一节内容) 打开JupyterLab。

如图 1 所示，不管点击A 或B 都会看到C 这个图标，点击C 就会生成一个Notebook。此外，新建 Notebook 前，点击图 1 中D，我们可以改变文件路径。

A C B D

图 1. 新建Notebook

如图 2 所示，Notebook 界面的有很多板块。

Page 3  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

B A D C

图 2. JupyterLab 中新建Notebook 界面

JupyterLab 中的cell 是什么？

在JupyterLab 中，Cell (单元格) 是指一个包含代码或文本的矩形区域，它是用户编写和执行代码、编写文本和渲染Markdown 的基本单位。Cell 可以包含多种类型的内容，包括代码、Markdown、LaTeX 公式等。JupyterLab 中的Cell 可以通过交互式的方式进行编辑和执行。例如，在Code Cell 中，用户可以编写Python 代码，并使用Shift+Enter 快捷键执行代码并显示结果；在Markdown Cell 中，用户可以使用Markdown 语法编写文本，并使用Shift+Enter 快捷键渲染Markdown 文本。JupyterLab 中的Cell 还支持多种交互式扩展，例如使用IPython Magic 命令、使用自动完成、代码补全和代码调试等。Cell 也可以被复制、剪切、粘贴、移动和删除，使得用户可以轻松地组织和管理笔记本中的内容。

对于初学者，大家先注意4 点： ► 图 2 中的A 对应的是Notebook 默认的名字。右键可以对文件进行各种操作，比如重命名、剪切、复制、粘贴、删除等等。

► 图 2 中的B 是Notebook 中第一个cell。在Notebook 里，一个基本的代码块被称作一个cell。注意， 一个Notebook 可以有若干cell；而一个cell 理论上可以有无数行代码。

► 图 2 中的C 对应的是cell 的几个常见操作——复制并向下粘贴、向上、向下、向上加cell、向下加 cell、删除cell。

► 图 2 中的D 对应的操作——保存文件、向下加cell、剪切cell、复制cell、粘贴cell、运行当前cell 后移动 (或创建) 到下一个cell、停止运行、重启kernel、重启重跑所有cell、code/markdown 转换。

删除当前cell 向下加cell 向上加cell 光标向下光标向上复制并向下粘贴

图 3. C 对应的是cell 的几个常见操作

Page 4  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com code/markdown转换重启重跑所有cell 重启kernel 停止运行运行当前cell后移动到 (或创建) 下一个cell 粘贴cell (来自复制/剪切)

复制所在cell 剪切所在cell 向下加cell 保存Notebook文件

图 4. D 对应的是cell 的几个常见操作

JupyterLab 中的kernel 是什么？

JupyterLab 中，内核 (kernel) 是指与特定编程语言交互的后台进程，它负责编译和执行用户在JupyterLab 中编写的代码，并返回执行结果。内核与JupyterLab 之间通过一种称为“Jupyter 协议”的通信协议进行交互。打开一个新的notebook 或console 时， JupyterLab 会自动启动一个内核，这个内核将与该notebook 或console 中编写的代码进行交互。在notebook 或console 中编写代码，并使用内核来执行它们。内核还可以保存笔记本中的变量和状态，使得大家可以在多个代码单元格之间共享变量和状态。

JupyterLab 支持多种编程语言的内核，可以在启动notebook 或console 时选择要使用的内核。例如，如果想使用Python 内核，可以选择“Python 3”内核。一旦选择了内核，JupyterLab 将与该内核建立连接，并使用它来执行该notebook 或console 中编写的代码。如果希望在notebook 或console 中使用其他语言的内核，需要先安装并配置这些内核。

代码 vs 文本 Jupyter 的cell 常用两种状态——代码、文本。文本也叫markdown。两种状态之间可以相互转换。

顾名思义，代码状态的cell 中的内容会被视为“代码”，# 开头的部分会被视作为“注释” 文本markdown 状态下，整个cell 的内容可以是文本/Latex 公式/超链接/图片等等，这个cell 不会被当成代码执行。图 4 中的“code/markdown”选项可以帮助我们在两种cell 状态切换。

我们常在JupyterLab 中敲入各种Latex 公式，本书后续将会见缝插针地讲解如何用Latex 写各种公式。

多数时候为了提高切换效率，我们通常使用快捷键。下面介绍JupyterLab 中常用的快捷键。

本节配套的Jupyter Notebook 文件BK_2_Topic_1.02_1.ipynb 向大家展示如何在Jupyter Notebook 中进行探究式学习。本节配套的微课视频会逐cell 讲解这个Notebook 文件。

JupyterLab 中的markdown 是什么？

在JupyterLab 中，Markdown 是一种轻量级标记语言，可以用于编写文档、笔记和报告等。通过使用Markdown 语法，用户可以在 JupyterLab 中轻松地创建格式化文本、插入图片、添加链接、创建列表等。Markdown 语法非常简单，易于学习和使用。例如，使

Page 5  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 用Markdown 语法，用户可以使用井号 (#) 来创建标题，使用“-”或“*”符号加上空格来创建bullet list，使用双星号(**)来加粗文本，使用单星号 (*) 来斜体文本等。用户可以在Markdown 单元格中编写Markdown 语法，然后使用Shift+Enter 键来渲染 Markdown 文本。JupyterLab 中的Markdown 支持LaTeX 语法，用户可以使用LaTeX 语法来插入数学公式，从而方便地创建数学笔记和报告。

## 2.3 快捷键：这一章最有用的内容

建议大家使用快捷键完成常见cell 操作。JupyterLab 的快捷键分成两种状态：a) 编辑模式；b) 命令模式。

编辑模式，允许大家向cell 中敲入代码或markdown 文本。表 1 总结编辑模式下常用快捷键。为了帮助大家识别这些快捷键组合，图 5 给出标准键盘主键盘上各个按键的位置。

图 5. 标准键盘，Mac 的command 对应ctrl

命令模式，单击 esc  进入命令模式，这时可以通过键盘键入命令快捷键。表 2 总结命令模式下常用快捷键。

注意，表格中的加号 + 表示“一起按下”，不是让大家按加号键。加号 + 前后的按键没有先后顺序。

此外，本书GitHub 中还给出JupyterLab 快捷键的cheat sheet，建议大家专门将其打印出来，编程的时候放在一边参考。

表 1 和表 2 两个表格中都是常用默认快捷键。如果大家对某个快捷键组合不满意，可以自行修改。特别是需要在多个IDE 之间转换时，由于不同IDE 的默认快捷键不同，一般都会将常用快捷键统一设置成自己习惯的组合。JupyterLab 中修改快捷键的路径为Settings → Advanced Settings Editor (或esc → ctrl + ,)

→ 搜索Keyboard Shortcuts。注意，不建议初学者修改默认快捷键。

表 1. 编辑模式，常用快捷键快捷键组合功能 esc

进入“命令”模式；鼠标左键单击任何cell 返回，或单击enter 返回编辑模式 ctrl M 进入“命令”模式

Page 6  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ctrl S 保存；尽管JupyterLab 会自动保存，建议大家还是要养成边写边存的好习惯 enter shift

执行 + 跳转；运行当前cell 中的代码，光标跳转到下一cell enter ctrl

执行；运行当前cell 中的代码 enter alt

执行 + 创建cell；运行当前cell 中的代码，并在下方创建一个新cell shift - ctrl

分割；在光标所在位置将代码/文本分割成两个cells ctrl / 注释/撤销注释；对所在行，或选中行进行注释/撤销注释操作 ctrl [ 向左缩进；行首减四个空格 ctrl ]

向右缩进；行首加四个空格 ctrl A 全选；全选当前cell 内容 ctrl Z 撤销；撤销上一个键盘操作 Z shift ctrl

重做：恢复刚才撤销命令对应操作，相当于“撤销撤销” ctrl C 复制；复制选中的代码或文本 ctrl X 剪切；剪切选中的代码或文本 ctrl V 粘贴；粘贴复制/剪切的代码或文本 ctrl F 查询；实际上就是浏览器的搜索 home 跳到某一行开头 end

跳到某一行结尾 ctrl home

跳到多行cell 第一行开头 ctrl end

跳到多行cell 最后一行结尾 tab 代码补齐；忘记函数拼写时，可以给出前一两个字母，按tab 键得到提示 shift tab

对键入的函数提供帮助文档 ctrl B 展开/关闭左侧sidebar

表 2. 命令模式，常用快捷键快捷键组合功能 esc

编辑模式下，进入“命令”模式；鼠标左键单击任何cell 返回，或单击enter 返回编辑模式 esc M 在按下esc 进入编辑模式后，将当前cell 从代码markdown 转成文本 esc Y 将当前cell 从文本markdown 转成代码 enter 从命令模式进入编辑模式，或者鼠标左键单击任何cell esc A 插入；在当前cell 上方插入新cell esc B 插入；在当前cell 下方插入新cell esc D D 删除；在按下esc 进入编辑模式后，连续按两下D，删除当前cell esc 重启kernel；在按下esc 进入编辑模式后，连续按两下零0，重启kernel esc Dctrl B 展开/关闭左侧sidebar esc Dctrl A 选中所有cells esc Dshift

选中当前和上方cell，不断按shift + ▲不断选中更上一层cell esc Dshift

选中当前和下方cell，不断按shift + ▼不断选中更下一层cell shift M 合并；将所有选中的cells 合并；如果没有多选cell，则将当前cell 和下方cell 合并

Page 7  |  Chapter 2 JupyterLab，用起来  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com enter shift

执行 + 跳转；运行当前cell 中的代码，光标跳转到下一cell；和编辑模式一致 enter ctrl

执行；运行当前cell 中的代码；和编辑模式一致 enter alt

执行 + 创建cell；运行当前cell 中的代码，并在下方创建一个新cell；和编辑模式一致 esc 一级标题，等同于markdown 状态下 # esc 二级标题，等同于markdown 状态下 ## esc 三级标题，等同于markdown 状态下 ###，以此类推

这一章的习题很简单，请大家从零开始复刻Bk1_Ch2_01.ipynb，并在创建Jupyter Notebook 文档的过程使用快捷键。

* 这道题目很基础，本书不给答案。

Page 1  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Mathematical Expressions in LaTeX LaTeX 数学表达用JupyterLab markdown 编写常用数学表达

依我看来，世间万物皆数学。

But in my opinion, all things in nature occur mathematically.

—— 勒内·笛卡尔 (René Descartes)  |  法国哲学家、数学家、物理学家  |  1596 ~ 1650

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

Page 2  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 3.1 什么是LaTeX

LaTeX 是一种用于排版科学和技术文档的系统。根据官网介绍，LaTeX 的正确发音为Lah- tech 或Lay-tech。

与常见的字处理软件不同，LaTeX 使用纯文本文件作为输入，并通过预定义的命令和语法描述文档结构和格式。LaTeX 可以处理复杂的数学公式、表格、图表和引用，并提供高级功能如自动编号和交叉引用。

LaTeX 是开源的，可在多个操作系统上运行，并有丰富的扩展包和模板可供使用。LaTeX 被广泛应用于学术界和科技领域。通过使用LaTeX，用户可以轻松创建高质量、规范的学术论文、 期刊文章和演示文稿。

本章不会讲怎么用LaTeX 写论文，仅仅介绍如何在Jupyter Notebook 的markdown 中嵌入 Latex 数学符号、各类常用公式，比如图 1、图 2 两个例子。

LaTeX 更像是编程，比如图 1 中，\begin{bmatrix}代表左侧方括号 [，\end{bmatrix} 代表右侧方括号。\cdots 代表水平省略号，\vdots 代表竖直省略号，\ddots 代表对角省略号。

再比如图 2 中，-{\frac {1}{2} 为分式，第1 个 {} 内为分子，第2 个 {} 内为分母。

\left( 代表左括号，\right) 代表右括号。\sqrt 代表根号。LaTeX 语句非常直观，很容易理解，本章后文不再逐一讲解LaTeX 语句。

注意，在JupyterLab markdown 单元格中，要在文本中inline 插入一个简单的公式，需要用使用左右 $ (半角) 将公式括起来，比如$E=mc^2$。要让公式单独一行需要用左右 $$ 将公式括起来，比如$$E=mc^2$$。

这一章大家现用现学，千万别死记硬背。

矩阵 1,1 1,2 1, 2,1 2,2 2, ,1 ,2 , n n m n m n a a a a a a A a a a        =         $$A_{m\times n} = \begin{bmatrix} a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\ a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\ \vdots  & \vdots  & \ddots & \vdots  \\ a_{m,1} & a_{m,2} & \cdots & a_{m,n} \end{bmatrix}$$

图 1. 用LaTeX 写矩阵

Page 3  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

一元高斯概率密度函数 ( )

exp X f       −   = −             −   −       $$f_X(x)={\frac {1}{\sigma {\sqrt {2\pi }}}} \exp \left({-{\frac {1}{2}} \left({\frac {x-\mu }{\sigma}}\right)^{2}}\right)$$

图 2. 用LaTeX 写一元高斯概率密度函数

## 3.2 字母和符号

字母样式英文中常用字母样式主要有：正体aA (regular)、粗体Aa (bold)、斜体Aa (italic)、粗体斜体 Aa (bold italic)、无衬线体 (sans-serif)、衬线体 (serif)、花体 (calligraphy) 上标Aa (superscript)、下标Aa (subscript)。

无衬线体是指在字母末端没有装饰性衬线，如图 3 (a) 所示。无衬线体字体的设计更加简洁， 直接，没有额外的装饰。无衬线体常常被用于数字屏幕上，比如计算机屏幕、手机、平板电脑等，因为在低分辨率的显示条件下，无衬线体更容易阅读。常用的无衬线体字体有Arial、Roboto 等。本书图片注释文字很多便采用Roboto。Roboto 是Google 开源字体。

衬线体是指在字母末端有装饰性衬线的字体，如图 3 (b) 所示。这些图 3 (c) 所示小线条使得衬线体在打印和长段落文字中更易于阅读。它们在印刷物、书籍、报纸等传统媒体中广泛使用。最常见的衬线字体莫过于Times New Roman。鸢尾花书中大量使用Times New Roman，特别是在公式中。

注意，ISO 标准推荐向量、矩阵记号采用粗体、斜体、衬线体，比如a、b、x、A、B、X。

鸢尾花书采用这一样式。

此外，还必须要提到编程中常用的另外一种字体——等宽字体 (monospaced font, Mono)。在 Mono 字体中，每个字符 (包括字母、数字、标点符号、空格等) 都占据相同的水平宽度，这使得每列字符在视觉上都保持对齐，使得排版看起来整齐和规整。

在编程中需要对齐代码，使其易于阅读和维护，因此Mono 字体在代码编辑器中得到广泛应用。最常见的Mono 字体为Courier New。鸢尾花书很多地方也会采用Courier New。

本书读者顺序读到此处应该非常熟悉本书代码 (图 4) 这种Mono 字体，它就是Google 开源字体Roboto Mono Light。Roboto Mono Light 是无衬线等宽字体。

Page 4  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

(a)

(b)

(c)

图 3. 比较无衬线体、衬线体，图片改编自Wikipedia

AaBbCc OoXxYy IiLlMmNn 1234567890+>< (){}[]@-#%!/\

图 4. 等宽字体Roboto Mono Light

表 1. 数学中字母样式 LaTeX 样式说明 $ {AaBbCc} $ AaBbCc 斜体，大部分数学符号、表达式 $ \mathrm {AaBbCc} $ AaBbCc 正体，公式中的单位或文字 $ \mathbf {AaBbCc} $ AaBbCc 粗体，向量、矩阵 $ \boldsymbol {AaBbCc} $ AaBbCc 粗体、斜体，向量、矩阵 $ \mathtt {AaBbCc} $ AaBbCc 等宽字体，常用于代码 $ \mathcal {ABCDEF} $

花体，用于表示数学中的集合、代数结构、算子 $ \mathbb {CRQZN} $

黑板粗体 (blackboard bold)，常用来表达各种集合 $\text {Aa Bb Cc}$ Aa Bb Cc 用来写公式中的文字 $\mathrm{d}x$ ISO 规定导数符号d 为正体

Page 5  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $\operatorname{T}$ T 运算符

表 2. 各种字母英文读法英文字母英文表达 A capital a, cap a, upper case a a small a, lower case a A italic capital a, italic cap a a italic a A boldface capital a, bold cap a a boldface a, bold small a A bold italic cap a a bold italic small a A Gothic capital a a Gothic a A script capital a a script a

标记数学符号、表达式中还常用各种特殊标记 (accent)，表 3 总结常用特殊标记。

表 3. 数学中字母标记 LaTex 数学表达英文读法 $x'$ $x^{\prime}$ x x prime $x'’$ x x double prime $\overrightarrow{AB}$ AB a vector pointing from A to B $\underline{x}$ x underline $\hat{x}$ ˆx x hat $\bar{x}$ x bar $\dot{x}$ x dot $\tilde{x}$ x tilde $x_i$ x subscript i, x sub i $x^i$ x to the n, x to the nth, x to the n-th power x raised to the n-th power $\ddot{x}$ x double dot

Page 6  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $x^*$ * x star, x super asterisk $x\dagger$ †

x dagger $x\ddagger$ ‡ x double dagger ${\color{red}x}$ red x

希腊字母表 4 总结常用大小写希腊字母，表 5 给出常用作变量的希腊字母。比如，鸢尾花书《统计至简》就会用到。

表 4. 希腊字母，大小写小写 LaTeX 大写 LaTeX 英文拼写英文发音 α $\alpha$ Α $A$ alpha /ˈælfə/ β $\beta$ Β $B$ beta /ˈbeɪtə/ γ $\gamma$ Γ $\Gamma$ gamma /ˈɡæmə/ δ $\delta$ Δ $\Delta$ delta /ˈdeltə/ ε $\epsilon$ Ε $E$ epsilon /ˈepsɪlɑːn/ ζ $\zeta$ Ζ $Z$ zeta /ˈziːtə/ η $\eta$ Η $H$ eta /ˈiːtə/ θ $\theta$ Θ $\Theta$ theta /ˈθiːtə/ ι $\iota$ Ι $I$ iota /aɪˈoʊtə/ κ $\kappa$ Κ $K$ kappa /ˈkæpə/ λ $\lambda$ Λ $\Lambda$ lambda /ˈlæmdə/ μ $\mu$ Μ $M$ mu /mjuː/ ν $\nu$ Ν $N$ nu /njuː/ ξ $\xi$ Ξ $\Xi$ /ksaɪ/ 或 /zaɪ/ 或 /ɡzaɪ/ ο $\omicron$ Ο $O$ omicron /ˈɑːməkrɑːn/ π $\pi$ Π $\Pi$ pi /paɪ/ ρ $\rho$ Ρ $P$ rho /roʊ/ σ $\sigma$ Σ $\Sigma$ sigma /ˈsɪɡmə/ τ $\tau$ Τ $T$ tau /taʊ/ υ $\upsilon$ Υ $Y$ upsilon /ˈʊpsɪlɑːn/ φ $\phi$ Φ $\Phi$ phi /faɪ/ χ $\chi$ Χ $X$ chi /kaɪ/ ψ $\psi$ Ψ $\Psi$ psi /saɪ/ ω $\omega$ Ω $\Omega$ omega /oʊˈmeɡə/

表 5. 希腊字母，变量 LaTeX 样式 LaTeX 样式

Page 7  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $\vartheta$  $\varrho$

$\varkappa$

$\varphi$  $\varpi$  $\varepsilon$  $\varsigma$ 

常用符号表 6 总结常用符号。

此外，请大家注意区分：- 不间断连字符 (nonbreaking hyphen)、− 减号 (minus sign)、– 短破折号 (en dash)、— 长破折号 (em dash)、_ 下划线 (underscore)、/ 前斜线 (forward slash)、\ 反斜线 (backward slash, backslash, reverse slash)、| 竖线 (vertical bar, pipe)。

表 6. 常用符号 LaTex 数学表达英文读法中文表达 $\times$  multiplies, times 乘 $\div$  divided by 除以 $\otimes$  tensor product 张量积 $($ ( open parenthesis, left parenthesis, open round bracket, left round bracket 左圆括号 $)$ )

close parenthesis, right parenthesis, close round bracket, right round bracket 右圆括号 $[$ [ open square bracket, left square bracket 左方括号 $]$ ]

close square bracket, right square bracket 右方括号 $\{$ { open brace, left brace, open curly bracket, left curly bracket 左大括号 $\}$ } close brace, right brace, close curly bracket, right curly bracket 右大括号 $\pm$  plus or minus 正负号 $\mp$

Minus or plus 负正号 $<$  less than 小于 $\leq$  less than or equal to 小于等于 $\ll$

much less than 远小于 $>$  greater than 大于号 $\geq$  greater than or equal to 大于等于 $\gg$

much greater than 远大于 $=$ = equals, is equal to 等于 $\equiv$  is identical to 完全相等 $\approx$  is approximately equal to 约等于 $\propto$  proportional to 正比于 $\partial$  partial derivative 偏导

Page 8  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $\nabla$  del, nabla 梯度算子 $\infty$  infinity 无穷 $\neq$  does not equal, is not equal to 不等于 $\parallel$

parallel 平行 $\perp$ ⊥ perpendicular to 垂直 $\angle$  angle 角度 $\triangle$

triangle 三角形 $\square$

square 正方形 $\sim$ ~ similar 相似 $\exists$  there exists 存在 $\forall$  for all 任意 $\subset$  is proper subset of 真子集 $\subseteq$  is subset of 子集 $\varnothing$  empty set 空集 $\supset$  is proper superset of 真超集 $\supseteq$  is superset of 超集 $\cap$  intersection 交集 $\cup$  union 并集 $\in$  is member of 属于 $\notin$  is not member of 不属于 $\N$

set of natural numbers 自然数集合 $\Z$

set of integers 整数集合 $\rightarrow$ → arrow to the right 向右箭头 $\leftarrow$  arrow to the left 向左箭头 $\mapsto$

maps to 映射 $\implies$  implies 推出 $\uparrow$  arrow pointing up, upward arrow 向上箭头 $\Uparrow$  arrow pointing up, upward arrow 向上箭头 $\downarrow$  arrow pointing down, downward arrow 向下箭头 $\Downarrow$  arrow pointing down, downward arrow 向下箭头 $\therefore$  therefore sign 所以 $\because$

because sign 因为 $\star$

asterisk, star, pointer 星号 $!$ !

exclamation mark, factorial 叹号，阶乘 $| x |$ absolute value of x 绝对值

Page 9  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $\lfloor x \rfloor$   the floor of x 向下取整 $\lceil x \rceil$   the ceiling of x 向上取整 $x!$ !

x factorial 阶乘

## 3.3 代数

表 7 ~ 表 12 总结了一些常用的LaTeX 代数表达式，请大家自行学习。

表 7. 几个多项式有关的数学表达 LaTeX 数学表达 $x^{2}-y^{2} = \left(x+y\right)\left(x-y\right)$ ( )( )

y y y − = + −

$a_{n}x^{n}+a_{n-1}x^{n-1}+\dotsb + a_{2}x^{2} + a_{1}x + a_{0}$ n n n n a x a a x a x a − − + + + + +

$\sum_{k=0}^{n}a_{k}x^{k}$ n k k k a x =

$ ax^{2}+bx+c=0\ (a\neq 0) $ 0 ( 0)

ax bx a + + = 

表 8. 几个根式有关的数学表达 LaTeX 数学表达 ${\sqrt[{n}]{a^{m}}}=(a^{m})^{1/n}=a^{m/n}=(a^{1/n})^{m}=({\s qrt[{n}]{a}})^{m}$ 1/ / 1/ ( )

( )

( )

n m n n n n a a a a a = = = =

$\left({\sqrt {1-x^{2}}}\right)^{2}$ ( )

−

表 9. 几个分式有关的数学表达 LaTeX 数学表达 $\frac {1}{x+1}+{\frac {1}{x-1}}={\frac {2x}{x^{2}- 1}}$ + = + − −

$x_{1,2}={\frac {-b\pm {\sqrt {b^{2}-4ac}}}{2a}}$ 1,2 b b ac a − − =

表 10. 几个和函数有关的数学表达

Page 10  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com LaTeX 数学表达 $f(x)=ax^{2}+bx+c~~{\text{ with }}~~a,b,c\in \mathbb {R} ,\ a\neq 0$ ( )

with   , , , f x ax bx a b c a = + +  

$f(x_1, x_2) = x_1^2 + x_2^2 + 2x_1x_2$ ( , )

f x x x x = + +

$\log_{b}(xy)=\log_{b}x+\log_{b}y$ log ( )

log log b b b xy y = +

$\ln(xy)=\ln x+\ln y{\text{  for  }} x>0 {\text{  and  }} y>0$ ln( )

ln ln   for 0  and xy y y = +  

$f(x)=a\exp \left(-{\frac {(x- b)^{2}}{2c^{2}}}\right)$ ( )

( )

exp b f x a   − = −    

表 11. 几个三角恒等式 LaTeX 数学表达 $\sin ^{2}\theta +\cos ^{2}\theta =1$ sin cos   + =

$\sin 2\theta =2\sin \theta \cos \theta$ sin2 2sin cos    =

$\sin(\alpha \pm \beta )=\sin \alpha \cos \beta \pm \cos \alpha \sin \beta$ sin( )

sin cos cos sin        = 

$\tan(\alpha \pm \beta )=\frac {\tan \alpha \pm \tan \beta }{1\mp \tan \alpha \tan \beta }$ tan tan tan( )

tan tan         =

表 12. 几个和微积分有关数学表达 LaTeX 数学表达 $\exp(x)=\sum _{k=0}^{\infty }{\frac {x^{k}}{k!}}=1+x+{\frac {x^{2}}{2}}+{\frac {x^{3}}{6}}+{\frac {x^{4}}{24}}+\cdots $ exp( )

!

k k k  = = = + + + + + 

$ \left(\sum _{i=0}^{n}a_{i}\right)\left(\sum _{j=0}^{n}b_{j}\right)=\sum _{i=0}^{n}\sum _{j=0}^{n}a_{i}b_{j}$ n n n n j j j j a b a b = = = =     =          

$\exp(x) =\lim _{n\to \infty }\left(1+{\frac {x}{n}}\right)^{n}$ exp( )

lim 1 n n n →   = +    

$\frac {\mathrm{d}}{\mathrm{d}x} \exp(f(x)) =f'(x)

\exp(f(x))$ d exp( ( ))

( )exp( ( ))

f x f f x  =

$\int_{a}^{b}f(x) \mathrm {d} x$ ( )d b a f x 

$\int _{-\infty }^{\infty }\exp(- x^{2})\mathrm{d}x={\sqrt {\mathrm{\pi} }}$ exp( )d   − − = 

Page 11  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com $\int _{-\infty }^{\infty }\int _{- \infty }^{\infty } \exp \left({- \left(x^{2}+y^{2}\right)} \right) {\mathrm{d}x} {\mathrm{d}y} = \pi$ ( )

( )

exp d d y x y    − − − + = 

$\frac {\partial ^{2}f}{\partial x^{2}}=f''_{xx}=\partial _{xx}f=\partial _{x}^{2}f$ f f f f   = =  =  

${\frac {\partial ^{2}f}{\partial y \partial x}}={\frac {\partial }{\partial y}}\left({\frac {\partial f}{\partial x}}\right)=f''_{xy}$ xy f f f y x y       = =       

## 3.5 线性代数

表 13 和表 14 总结了一些常用的LaTeX 线性代数相关表达式，请大家自行学习。

表 13. 几个和向量有关的表达 LaTeX 数学表达 $\mathbf {a} = {\begin{bmatrix} a_{1} \\ a_{2} \\ a_{3} \\\ end{bmatrix}} = [a_{1}\ a_{2}\ a_{3}]^{\operatorname {T} }$ T [ ]

a a a a a a     = =       a

$\left\|\mathbf {a} \right\|=\sqrt {a_{1}^{2}+a_{2}^{2}+a_{3}^{2}}$ a a a = + + a

$\mathbf {a} \cdot \mathbf {b} = a_{1}b_{1} + a_{2}b_{2} + a_{3}b_{3}$ 1 1 2 2 3 3 a b a b a b  = + + a b

$\mathbf {a} \cdot \mathbf {b} =\left\|\mathbf {a} \right\|\left\|\mathbf {b} \right\|\cos \theta $ cos  = a b a b

$\|\mathbf {x} \|_{p}=\left(\sum _{i=1}^{n}\left|x_{i}\right|^{p}\right)^{1/p}$ 1/ p n p p =   =      ‖ ‖

表 14. 几个和矩阵有关的表达 LaTeX 数学表达 $\mathbf {A} = {\begin{bmatrix} 1 & 2\\ 3 & 4 \\ 5 & 6 \end{bmatrix}}$     =       A

Page 12  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com \mathbf {A} ={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\end{bmatrix}} n n mn a a a a a a a a a       =       A

$\left(\mathbf {A} +\mathbf {B} \right)^{\operatorname {T} }=\mathbf {A} ^{\operatorname {T} }+\mathbf {B} ^{\operatorname {T} }$ ( )

T T T + = + A B A B $\left(\mathbf {AB} \right)^{\operatorname {T} }=\mathbf {B} ^{\operatorname {T} }\mathbf {A} ^{\operatorname {T} }$ ( )

T T T = AB B A $ \left(\mathbf {A} ^{\operatorname {T} }\right)^{-1}=\left(\mathbf {A} ^{- 1}\right)^{\operatorname {T} }$ ( )

( )

T T − − = A A

$\mathbf {u} \otimes \mathbf {v} = \mathbf {u} \mathbf {v} ^ {\operatorname {T}} = {\begin{bmatrix}u_{1} \\ u_{2} \\ u_{3} \\ u_{4} \end{bmatrix}} {\begin{bmatrix} v_{1}&v_{2}&v_{3} \end{bmatrix}} = {\begin{bmatrix} u_{1}v_{1} & u_{1}v_{2} & u_{1}v_{3} \\ u_{2}v_{1} & u_{2}v_{2} & u_{2}v_{3} \\ u_{3}v_{1} & u_{3}v_{2} & u_{3}v_{3} \\ u_{4}v_{1} & u_{4}v_{2} & u_{4}v_{3} \end{bmatrix}}$   1 1 1 2 1 3 2 1 2 3 T 3 1 3 2 3 3 4 1 4 3 u v u v u v u u v u v u v u u v u v u v u u v u v u v u              = = =             u uv

$\det {\begin{bmatrix} a & b \\ c & d \end{bmatrix}} = ad-bc$ det a b ad bc  = −    

## 3.6 概率统计

表 15 总结了一些常用的LaTeX 概率统计相关表达式，请大家自行学习。

表 15. 几个和概率统计有关的表达 LaTeX 数学表达 $\Pr(A\vert B)={\frac {\Pr(B\vert A)\Pr(A)}{\Pr(B)}} Pr( | )Pr( )

Pr( | )

Pr( )

B A A A B B =

$ f_{X\vert Y=y}(x)={\frac {f_{X,Y}(x,y)}{f_{Y}(y)}}$ , | ( , )

( )

( )

X Y X Y y Y f x y f f y = =

$\operatorname {var} (X) = \operatorname {E} \left[X^{2}\right]-\operatorname {E} var( )

E E[ ]

X X X   = −  

Page 13  |  Chapter 3 LaTeX 数学公式  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com [X]^{2}$ $\operatorname {var} (aX+bY)=a^{2}\operatorname {var} (X) + b^{2}\operatorname {var} (Y) + 2ab \operatorname {cov} (X,Y)

var( )

var( )

var( )

cov( , )

aX bY a X b Y ab X Y + = + +

$\operatorname {E} [X]=\int _{- \infty }^{\infty }xf_{X}(x) \operatorname {d}x$ E[ ]

( )d X X xf  − = 

$ X\sim N(\mu ,\sigma ^{2})$ ~ ( , )

X N 

$\frac {\exp \left(-{\frac {1}{2}}\left({\mathbf {x} }-{\boldsymbol {\mu }}\right)^{\mathrm {T} }{\boldsymbol {\Sigma }}^{-1}\left({\mathbf {x} }- {\boldsymbol {\mu }}\right)\right)}{\sqrt {(2\pi )^{k}|{\boldsymbol {\Sigma }}|}}$ ( )

( )

T exp (2 ) | | k  −   − − −     μ Σ μ Σ

Page 1  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Fundamentals of Grammar in Python Python 语法，边学边用吸取英语学习失败的教训，不能死磕语法

当你建造空中楼阁时，它不会倒塌；空中楼阁本应属于高处。现在，撸起袖子把地基夯实。

If you have built castles in the air, your work need not be lost; that is where they should be. Now put the foundations under them.

—— 亨利·戴维·梭罗 (Henry David Thoreau)  |  作家、诗人  |  1817 ~ 1862

◄ float() Python 内置函数，将指定的参数转换为浮点数类型，如果无法转换则会引发异常 ◄ for ... in ... Python 循环结构，用于迭代遍历一个可迭代对象中的元素，每次迭代时执行相应的代码块 ◄ from numpy import * 从NumPy 库中导入了所有函数和对象，使得我们可以直接使用NumPy 的所有功能，无需使用前缀"numpy."来调用。不建议使用这种方法 ◄ from numpy import array 从NumPy 库中导入了array 函数，使得我们可以直接使用array 函数而无需使用 "numpy.array"来创建数组 ◄ if ... elif .. else Python 条件语句，用于根据多个条件之间的关系执行不同的代码块，如果前面的条件不满足则逐个检查后续的条件 ◄ if ... else ... Python 条件语句，用于在满足if 条件时执行一个代码块，否则执行另一个else 代码块 ◄ import numpy as np 将NumPy 库导入为别名np，使得我们可以使用np 来调用NumPy 的函数和方法 ◄ import numpy 将NumPy 库导入到当前的Python 环境中，调用时使用完整的numpy 作为前缀 ◄ input() Python 内置函数，用于从用户处接收输入 ◄ int() Python 内置函数，用于将指定的参数转换为整数类型，如果无法转换则会引发异常 ◄ list() Python 内置函数，将元组、字符串等等转换为列表 ◄ numpy.arange() 创建一个包含给定范围内等间隔的数值的数组 ◄ numpy.array() 输入数据转换为NumPy 数组，从而方便进行数值计算和数组操作 ◄ numpy.random.rand() 在[0, 1) 区间，即0 (包含) 到1 (不包含) 之间，内生成特定形状满足连续均匀的随机数 ◄ print() Python 内置函数，将指定的内容输出到控制台或终端窗口，方便用户查看程序的运行结果或调试信息 ◄ range() Python 内置函数，用于生成一个整数序列，可用于循环和迭代操作 ◄ set() Python 内置函数，创建一个无序且不重复元素的集合，可用于去除重复元素或进行集合运算 ◄ str() Python 内置函数，用于将指定的参数转换为字符串类型

Page 2  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 4.1 Python 也有语法?

和汉语、英语、法语等人类语言一样，Python 也是语言。只不过Python 是编程语言，是人和计算机交互语言。凡是语言就有语法——一套约定交流规则。

有了类似ChatGPT 这样的自然语言处理工具，人类的确可以直接使用人类语言和机器交流。但是， 考虑到ChatGPT 也是用Python 开发而成，Python 不过是退隐幕后罢了。

图 1. Python 也是语言

Python 语法使用数量极少的英文词汇，而且都是很基本的词汇。

Python 和英语都有一些关键词，例如Python 中的if、else、for、while 等关键词，和英语中的if、 else、for、while 等单词是一样的。

Python 和英语都有语法结构，例如Python 中的if 语句和英语中的条件句都是用来表示条件语句的结构。

Python 和英语都有一些语法规则，例如Python 中的缩进规则和英语中的句子结构规则都是用来规范语法的。

Python 语法相对来说比英语语法容易掌握，因为Python 语法的规则和规范性更强。

表 1 总结Python 中常用英文关键词。

Page 3  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 请大家注意大小写，特别是True、False、None 需要首字母大写。

表 1. Python 中常用英语关键词英语汉语介绍 and 和逻辑操作符，要求两个条件都满足时才返回True argument 参数 print('Hey you!') 中的 'Hey you' 是函数 print() 的输入参数 as 作为用于别名，可以给模块、函数或类指定另一个名称，比如import numpy as np assert 断言用于测试代码的正确性，如果条件不成立则会引发异常 boolean 布尔值 True 和 False 是两个布尔值 break 中断用于跳出循环语句 class 类定义一个类，包含属性和方法 complex 复数 3 + 4j 是一个复数 condition 条件 if x > 0: 是一个条件语句 continue 继续用于跳过当前循环的剩余部分，继续执行下一次循环 def 定义定义一个函数 del 删除用于删除变量或对象 dictionary 字典 {'name': 'James', 'age': 18} 是一个字典 elif 否则如果用于在if 语句中添加多个条件判断 else 否则用于if 语句中，当所有条件都不满足时执行 except 除外用于捕获异常。

False 假表示布尔值为假。

finally 最后用于定义无论是否发生异常都要执行的代码块 float 浮点数

## 3.14 是一个浮点数

for 循环用于迭代遍历序列、集合或其他可迭代对象 from 来自用于从模块中导入特定函数、类或变量，比如from numpy import random function 函数 print() 是一个函数 global 全局用于在函数中引用全局变量 if 如果用于条件判断，比如if x > 0: import 导入用于导入模块，比如import numpy in 在用于检查元素是否存在于序列、集合或其他可迭代对象中 integer 整数 3 是一个整数 is 是用于检查两个对象是否相同 lambda 匿名定义一个匿名函数 list 列表 [1, 2, 3] 是一个列表 loop 循环 for i in range(10): 是一个循环语句 module 模块 import math 导入了 Python 的 math 模块 None 空表示一个空值或缺少值 not 非逻辑操作符，将True 变为False，将False 变为True object 对象 my_object = MyClass() 中 my_object 是一个 MyClass 类的对象 or 或逻辑操作符，只要一个条件满足就返回True package 包 import numpy 导入了 Python 的 numpy 包 pass 跳过用于占位符，不执行任何操作

Page 4  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com raise 引发异常用于引发异常，比如，raise ValueError("Invalid value.")

return 返回用于从函数中返回值 set 集合 {1, 2, 3} 是一个集合 statement 语句 x = 5 是一个赋值语句 string 字符串 Hey you!' 是一个字符串 True 真表示布尔值为真 try 尝试用于包含可能引发异常的代码块，比如try: except ValueError: tuple 元组 (1, 2, 3) 是一个元组 variable 变量 x = 5 中 x 是一个变量 while 当用于创建循环，只要条件为真就重复执行代码块 with 使用用于自动管理资源，例如文件句柄或数据库连接 yield 产生用于生成器函数，暂停函数执行并返回一个值

Python vs C 语言 Python 是一种高级的面向对象编程语言。C 语言是一种编译型语言，非常适合编写底层的系统软件，例如操作系统、编译器和设备驱动程序等。C 语言的优势在于其对硬件和操作系统的底层控制，而这也是Python 所缺乏的。Python 在处理复杂的数据结构和算法时，通常比C 语言慢得多。

Python 的优势主要是其强大的第三方库和工具生态系统，使得Python 可以用于更高层次的机器控制和自动化任务，例如数据处理、机器学习和自然语言处理等。

什么是面向对象编程语言？什么是编译型语言？

面向对象编程语言是一种编程范式，它将现实世界中的概念和模型转化为计算机程序中的类和对象。面向对象编程中的核心概念包括封装、继承和多态性。

编译型语言是指需要先通过编译器将源代码转换成可执行代码的编程语言。在编译过程中，编译器会对代码进行语法分析、词法分析、语义分析、优化等操作，将源代码转换成二进制可执行文件。编译型语言的执行速度更快，但开发效率较低，因为需要编写和编译源代码。

学习板块本书有关Python 语法主要包括以下几个板块： ► 基础语法 (本章)：注释、缩进、变量、包、代码风格等。

► 数据类型 (第5 章)：数字、字符串、列表、元组、字典等。

► 运算符 (第6 章)：算术运算符、比较运算符、逻辑运算符、位运算符等。

► 控制结构 (第7 章)：条件语句、循环语句、异常处理语句等。

► 函数和模块 (第8 章)：函数和模块的定义和使用。

► 面向对象编程 (第9 章)：定义类、对象、方法、属性等。

Page 5  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 4.2 注释：不被执行，却很重要

Python 注释 (comment) 就是在写Python 代码时，为了方便自己和别人理解代码，添加的文字说明。

这些文字说明不会被Python 解释器 (interpreter) 执行，只是为了让代码更易读懂和更易维护。

在Python 代码中，我们可以使用 # (hash, hashtag, hashmark) 符号来添加注释。

当Python 解释器读取代码时，如果遇到 # 符号，它就会将 # 所在行后面的内容视为注释，而不是代码的一部分。

注意，# 后面的字符开始直到该行的结尾都被认为是注释。

#注释：整行、单行尾部如图 2 所示，可以把注释 (图中高亮部分) 看作是给代码添加的“贴纸”，用来解释代码的用途、原理、变量的含义等等。机器遇到图中高亮部分文字就自然跳过。

图 2 展示了两种注释：1) 整行注释；2) 单行尾部注释。

import numpy as np # 导入名为NumPy的第三方库，并将其重命名为np x_array = np.arange(10) # x_array有10个元素 # 这行代码使用NumPy库中的函数numpy.arange()

# 创建了一个名为x_array的一维数组 # 包含从0到9共10个整数 print(x_array) # 打印数组 a b

图 2. 举例说明Python 代码中的注释

下面简单讲解图 2 中这段代码。

a  将numpy (正式名称为NumPy) 导入到当前Python 环境中，并给numpy 一个别名np。这样我们可以使用np 来调用NumPy 的函数和方法。这是一种在Python 中较为常用的导入第三方库的方法。本章后文还会介绍其他几种导入库的方法。

b  np.arange() 调用numpy (别名np) 库中的arange() 函数。如图 3 所示，np.arange(10) 产生 0 ~ 9 这 10 个整数构成的数组，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])，并赋值给变量x_array。本书第13 到18 章专门介绍NumPy。

c  利用print() 函数打印变量x_array 中保存的array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])。

请大家在JupyterLab 中练习图 2 中这段代码。

Page 6  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com numpy.arange(10)

图 3. 一维NumPy 数组

在Jupyter Notebook 中，markdown 的功能和comment 显然不同。Markdown 相当于笔记，可以是标题、文本段落、列表、图片、链接等等。而comment 是在代码块中添加对具体代码的说明和解释。

再次提醒，JupyterLab 中comment 和uncomment 默认快捷键为 ctrl + /。

'''或"""注释：多行此外，我们还可以用三个引号 ('''或""") 来添加多行注释。

比如，要在Python 代码中添加一段多行注释，来描述一个函数的功能和用法，那么可以使用三个引号来实现。图 4 是一个例子。

def my_function(x, y): """

这个自定义函数计算两个数值x和y的和函数输入为: x: The first number to be added.

y: The second number to be added.

函数输出为: The sum of x and y.

"""

return x + y # 打印结果 print(my_function(1.5, 2))

a b my_function y x + y 4 spaces

图 4. 用三个引号来添加多行注释

图 4 中，a 利用def 定义了一个名为“my_function”的函数，然后使用三个引号来添加多行注释。

“my_function”是个自定义函数，括号 () 内有两个输入x 和y。

在Python 中，自定义函数是一种将一段可重用代码封装起来的方法。大家可能会好奇，Python 各种库已经提供大量函数，我们为什么还需要自定义函数？首先，除了通用函数之外，我们需要各种满足个人定制化要的函数。自定义函数让代码模块化，便于管理和维护。一旦创建了一个函数，我们可以在不同的地方多次调用它，而不必重复编写相同的代码。将部分代码封装在自定义函数中，还可以提高代码的可读性，让代码更简洁，方便调试，降低错误。

本书第8 章将专门讲解自定义函数。

Page 7  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 注意，a 这句以冒号 (colon) : 结束。表 2 列出Python 中使用冒号的几种常见情况，本书后文都会涉及到。

b 用return 返回自定义函数的输出——x 和y 的和。

b 一句在return 之前有4 个空格，叫做缩进 (indentation)。本章后文将专门介绍缩进的作用。

注意，中文输入法下的单、双引号都是“全角引号”，Python 解释器会抛出语法错误。在Python 中，只有半角引号（'）和双半角引号（"）才可以用来定义字符串，而全角引号则不能用于字符串的定义。此外，使用圆括号、中括号等符号时也需要注意全角、半角问题，避免语法错误。

c 利用自定义函数“my_function”计算 1.5 和2 之和，然后用print() 打印结果。

在上面的例子中，我们使用了三个引号来包裹函数的注释文字，这个注释可以跨越多行，并且被 Python 解释器忽略掉，不会被当作代码执行。这样，其他程序员在阅读我们的代码时，就可以清晰地了解这个函数的作用、输入和输出参数、以及函数的返回值。

前文提过，为了保证字母、数字、符号、空格等显示时宽度一致，本书正文示例代码采用的字体为 Roboto Mono Light。

表 2. Python 使用冒号的常见情况情况语法索引和切片 string_obj[start:end:step_size]  # 字符串 list_obj[start:end:step_size]    # 列表 tuple_obj[start:end:step_size]   # 元组 numpy_array[start:end:step_size] # NumPy array 字典键值对 dict_obj{key:value}              # 字典条件语句 if condition_1: # 代码块，注意缩进 elif condition_2: # 代码块，注意缩进 else: # 代码块，注意缩进循环语句 for element in iterable: # 代码块，注意缩进

while condition: # 代码块，注意缩进定义函数 def function_name(arguments): # 代码块，注意缩进 lambda 函数 lambda variables: expression 定义类 class ClassName: # 代码块，注意缩进异常处理 try: # 代码块，注意缩进 except SomeException: # 代码块，注意缩进 finally: # 代码块，注意缩进上下文管理 with context_manager: # 代码块，注意缩进；第35 和36 章中使用streamlit 库时会用到

Page 8  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 4.3 缩进：四个空格，标识代码块

相信大家已经在图 4 和表 2 发现了缩进 (indentation)。

在 Python 中，缩进是非常重要的。缩进是指在代码行前面留出的空格 (space) 或制表符 (tab →)，它们用于表示代码块的开始和结束。换句话说，缩进用于指示哪些代码行属于同一个代码块。

在其他编程语言中，通常使用花括号或关键字来表示代码块的开始和结束 (比如MATLAB 用end 表示代码块结束)。但在 Python 中，使用缩进来代替。

注意，在Python 中，缩进的大小没有严格规定，一般情况下建议使用四个空格作为缩进，并不鼓励用制表符tab 缩进。特别反对混用四个空格、tab 缩进。

Python 中常见的需要缩进的场合包括for 循环，while … 循环，if … else … 判断语句，函数定义以及类的定义等。同一缩进级别里的代码属于同一逻辑块。这些需要使用缩进的场合往往都是需要使用冒号 : 来表示下一行需要使用缩进。

注意，如果缩进有误编译器会报错，报错内容为IndentationError: unindent does not match any outer indentation level。

Code block, first level (no space is allowed at the first line)

Third level Second level

图 5. 缩进形成不同的代码级别

条件语句在if … elif … else … 语句中，它们所控制的代码块需要缩进，以表示它们属于条件语句。图 9 这段代码用if … elif … else … 语句判断输入数值正负。图 6 所示为代码的流程图。编程时，流程图 (flowchart)

用于表示算法的逻辑结构和程序的执行流程。它可以帮助我们更好地理解代码的执行顺序、条件分支和循环结构。

从这个流程图结果来看，三个条件分支实际上将图 7 实数轴 (number line) 分为三个部分。

下面介绍代码中重要语句。

a 首先利用Python 内置 input() 输入从用户获取数值输入，然后用float() 将其转化为浮点数 (float)

并存在变量x 中。

b 是条件语句的开始，它使用关键字 if 来引导一个条件的判断。在这里，条件是检查变量 x 是否大于零。大于号 > 用来判断。

Page 9  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 本书第6 章会专门讲解用于判断的运算。

如果这个条件为真True，即 x 确实大于零，则下面缩进的代码块会被执行。如图 8 (a) 所示，当输入为8 时 (x = 8)，x > 0 结果为True，则执行缩进中的代码块print("x is positive")，打印消息。

如果x > 0 判断结果为False，则不执行缩进中代码，直接进入c 。

注意，在一个条件语句中，可以只有 if 分支，没有elif 或else 分支。

c 是条件语句中的 elif (else if 的缩写) 分支,在之前的条件 if x > 0: 不满足时执行。这句用于检查变量 x 是否等于零，如果满足条件，则打印另一条消息。如图 8 (b) 所示，当输入为0 时 (x = 0)，x == 0 结果为True，则执行缩进中的代码块print("x is zero")，打印消息。两个相连等号 == 用来判断是否相等。

在一个条件语句中，可以没有elif，也可以有若干elif。

d 条件语句的 else 分支，用于处理在之前的条件不满足时的情况。之前条件包括if，可能没有、也可能若干elif 分支。如图 8 (c) 所示，当输入为−8 时，则执行 else 缩进中的代码块print("x is positive")， 打印消息。

e 这一句也在 else 分支中。如果x 为负数，对x 变号计算绝对值，并赋值给abs_x。

此外，还请大家注意if、elif、else 最后需要以半角冒号 : 结束。这个冒号还在英文输入法下的半角冒号。

本书第7 章将专门讲解几种常见控制结构。

else if x > 0: elif x == 0: False False True print()

True print()

Start End

图 6. 条件判断流程图

Page 10  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 表 3. 流程图中最常用标识名称标识解释开始 (start)

流程的起始点结束 (end, terminal)

流程的结束点箭头 (flowline, arrowhead)

用来表达过程的次序流程 (process)

表示一个操作、任务或活动的步骤判断 (decision)

菱形，根据条件的不同，决定不同的流程走向

Zero Negative Positive

图 7. 将一根实数轴分为三个部分

(a)

(c)

(b)

x = 8 x = 0 x = -8

图 8. 三条不同路径

Page 11  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a # 定义变量x，从用户输入中获取数值 x = float(input("请输入一个数值："))

# 定义变量abs_x，用来存放绝对值 abs_x = x # 如果x为正数 if x > 0: print("x is positive")

# 如果x为零 elif x == 0: print("x is zero")

# 如果x为负数 else: print("x is negative")

# 计算负数绝对值 abs_x = -x print("该数值的绝对值为：", abs_x)

4 spaces e Zero Negative Positive b

图 9. 条件语句中使用缩进

循环语句在for、while 等循环语句中，循环体内的代码块需要缩进，以表示它们属于循环语句。在Python 中，for 循环是一种迭代结构，用于遍历可迭代对象 (如列表、元组、字符串等) 中的元素，执行特定的操作。

如图 11 代码所示，a 定义了一个字符串，赋值给变量x_string。在Python 中，字符串 (string) 是一种数据类型，用于表示文本数据。字符串是由一系列字符组成的，可以包含字母、数字、符号以及空格等字符。定义字符串时，可以使用单引号 ' ' 或双引号 " " 包裹起来，两种方式是等效的。

本书第5 章将专门介绍各种常见数据类型，比如字符串、列表、字典等等。

b 在每次迭代时，i_str 会依次取得可迭代对象x_string 中的元素，然后执行循环体内的print()操作。当可迭代对象中的所有元素都被遍历完毕，循环就会结束。

图 11 代码的流程图如图 10 所示。

注意，for … in … 最后也需要以半角冒号 : 结束。

Page 12  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Loop ends?

False True print()

Start End

图 10. for 循环流程图

a b x_string = 'Python is FUN!' # 利用for循环打印每个字符 for i_str in x_string: print(i_str)

4 spaces t h s P y F U o N !

U N !

P y t h o s F

图 11. for 循环语句中使用缩进

## 4.4 变量：一个什么都能装的箱子

在Python 中，变量 (variable) 是用于存储数据值的标识符。本章开始到现在大家已经在不同代码中看到变量的影子。这些变量用于引用内存中的值，这些值可以是数字、字符串、列表、字典、函数等各种类型的数据。如图 12 所示，简单来说，变量就是个“箱子”。

表 4 为Python 中常见数据类型。

表 4. Python 中常见数据类型数据类型 type()

特点举例数字 (Number)

int float 包括整数、浮点数等 x = 10 y = 3.14 字符串 (String)

str 一系列字符的序列 s = 'hello world' 列表 (List)

list 一组有序的元素，可以修改 a = [1, 2, 3, 4]

b = ['apple', 'banana', 'orange']

元组 (Tuple)

tuple 一组有序的元素，不能修改 c = (1, 2, 3, 4)

d = ('apple', 'banana', 'orange')

集合 (Set)

set 一组无序的元素，不允许重复 e = {1, 2, 3, 4} f = {'apple', 'banana', 'orange'} 字典 (Dictionary)

dict 一组键-值对，键必须唯一 g = {'name': 'Tom', 'age': 18} 布尔 (Boolean)

bool 代表True 和False 两个值 x = True y = False None 类型 NoneType 代表空值或缺失值 z = None

Page 13  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

在Python 中，变量是动态类型的，这意味着我们可以在运行时为变量分配不同类型的值。不需要提前声明变量的类型，Python 会根据所赋予的值自动确定其类型。也就是说，这个Python 中的箱子什么都能装。在Python 中，可以使用内置的type() 函数来判定数据的类型。type() 函数返回一个表示对象类型的值。

variable 1 (int)

## 1.0 (float)

'1' (str)

[1] (list)

(1) (tuple)

{1} (set)

{1:1.0} (dict)

True (bool)

图 12. Python 变量就是个“箱子”，什么都能装

什么是动态类型语言？

动态类型语言是指在运行时可以自动判断变量的数据类型的编程语言。动态类型语言不需要在编写代码时显式地指定变量的数据类型，而是在程序运行时自动进行类型检查。

与之相对的是静态类型语言。静态类型语言中，每个变量都必须在声明时指定其数据类型，编译器会在编译时检查变量是否被正确使用。比如，C 语言是一种静态类型语言。int x = 10; int y = 20; x 和y 都被声明为整数类型 (int)，编译器会在编译时检查它们是否被正确使用。

变量命名规则 Python 中的变量命名规则和建议如下： ► 变量名必须是一个合法的标识符，即由字母、数字和下划线组成，且不能以数字开头。例如，x、 my_var、var_1 等都是合法的标识符。注意，变量名不能以数字开头，比如1_variable 作为变量名不合法。

► 变量名区分大小写。例如，my_var 和My_var 是不同的变量名。

► 变量名应该具有描述性，能够清晰地表达其所代表的内容。例如，name 可以代表人名，age 可以代表年龄等。

► 变量名应该尽量简洁明了，但不要过于简短或过于复杂。避免使用单个字母或缩写作为变量名，除非上下文明确。

► 变量名不应该与Python 中的保留函数 (关键字) 重名，否则会导致语法错误。例如，不能使用if、 else、while 等关键字作为变量名。

Page 14  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 在特定的上下文中，可以使用特定的命名约定。例如，类名应该使用驼峰命名法 (camelCase)，函数名和变量名应该使用下划线分隔法 (snake_case) 等。

有关Python 内置函数用法，请参考： https://docs.python.org/zh-cn/3/library/functions.html

驼峰、蛇形命名法常见有两种变量命名法——camel case、snake case。下面简单比较两者。

► 驼峰命名法 (camel case) 得名于其类似于骆驼背部的形状，其中单词之间的空格被移除，而每个单词首字母一般大写。在驼峰命名法中，通常有两种常见的变体：小驼峰命名法 (lower camel case)，比如firstName、totalAmount，和大驼峰命名法 (upper camel case)，比如FirstNames、 TotalAmount。大驼峰命名法也叫帕斯卡命名法 (Pascal case)。Pascal case 在C#中应用更多。

► 蛇形命名法 (snake case) 以其类似于蛇的形状而得名，其中单词之间用下划线 _ 分隔，而且所有字母都是小写，例如 first_name 或 total_amount。

注意，Python 社区变量名一般普遍采用蛇形命名法；Python 面向对象编程 (Object-Oriented Programming, OOP) 中的类 (class) 定义一般采用驼峰命名法。而Java 和JavaScript 等语言则更常使用驼峰命名法。

变量赋值本章读到这里，相信大家都已经清楚，我们可以使用等号 = 将一个值赋给一个变量。

可以同时给多个变量赋值，用逗号分隔每个变量，并使用等号将值分配给变量。例如： x, y, z = 1, 2, 3 可以使用链式赋值的方式给多个变量赋相同的值。例如： x = y = z = 0 可以使用增量赋值的方式对变量进行递增或递减。例如： x += 1  # 等价于 x = x + 1

## 4.5 使用import 导入包

在图 2 中，我们已经用过import 导入numpy 包。

在Python 中，包是一组相关的模块和函数的集合，用于实现特定的功能或解决特定的问题。包通常由一个顶层目录和一些子目录和文件组成，其中包含了实现特定功能的模块和函数。

Page 15  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Python 中有很多常用的包，包括数据处理和可视化、机器学习和深度学习、网络编程、Web 开发等。其中，常用的可视化包包括Matplotlib、Seaborn、Plotly 等，机器学习常用的包包括NumPy、 Pandas、Statsmodels、Scikit-learn、TensorFlow、Streamlit 等。

Matplotlib 是Python 中最流行的绘图库之一，可用于创建各种类型的静态图形，如线图、散点图、 柱状图、等高线图等。

Seaborn 是基于Matplotlib 的高级绘图库，提供了更美观、更丰富的图形元素和绘图样式。

Plotly 是一款交互式绘图库，可用于创建各种类型的交互式图形，如散点图、热力图、面积图、气泡图等，支持数据可视化的各个方面，包括统计学可视化、科学可视化、金融可视化等。

NumPy 是Python 中常用的数值计算库，提供了数组对象和各种数学函数，用于高效地进行数值计算和科学计算。

Pandas 是Python 中常用的数据处理库，提供了高效的数据结构和数据分析工具，可用于数据清洗、 数据处理和数据可视化。

Scikit-learn 是Python 中常用的机器学习库，提供了各种常见的机器学习算法和模型，包括分类、回归、聚类、降维等。

TensorFlow 是谷歌开发的机器学习框架，提供了各种深度学习模型和算法，可用于构建神经网络、 卷积神经网络、循环神经网络等深度学习模型。

Streamlit 可以通过简单的Python 脚本快速构建交互式数据分析、机器学习应用程序。

本书前文介绍过如何安装、更新、删除某个具体包，下面我们聊一聊如何在Python 中导入包。

导入包下面以NumPy 为例介绍几种常用的导入包的方式。

第一种，直接导入整个NumPy 包： import numpy 这种方式会将整个NumPy 包导入到当前的命名空间中，需要使用完整的包名进行调用，例如： a = numpy.array([1, 2, 3])

第二种，导入NumPy 包并指定别名： import numpy as np 这种方式会将NumPy 包导入到当前的命名空间中，并使用别名np 来代替NumPy，例如： a = np.array([1, 2, 3])

第三种，导入NumPy 包中的部分模块或函数： from numpy import array 这种方式会将NumPy 包中的array 函数导入到当前的命名空间中，可以直接调用该函数，例如： a = array([1, 2, 3])

第四种，导入NumPy 包中的所有模块或函数：

Page 16  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from numpy import * 这种方式会将NumPy 包中的所有函数和模块导入到当前的命名空间中，可以直接调用任意函数或模块，例如： a = array([1, 2, 3])

b = random.rand(3, 3)

在实际应用中，可以根据需要选择和使用适当的导入方式。一般来说，建议使用第二种 (导入 NumPy 包并指定别名) 或第三种方式 (导入部分模块或函数)，这样既可以简化代码，又不会导入太多无用的函数或模块，从而提高代码的可读性和性能。

## 4.6 Pythonic：Python 风格

"Pythonic" 翻译成中文可以是 "符合Python 风格的"、"Python 风格的" 等。让 Python 代码 Pythonic 是指遵循 Python 社区的最佳实践和代码风格，使代码更加易读、易维护、易扩展和高效。

以下是一些让 Python 代码 Pythonic 的方法： ► 遵循 PEP8 规范：PEP8 是 Python 社区的代码风格指南，包括缩进、命名、代码结构、注释等。编写符合 PEP8 规范的代码可以提高代码的可读性和可维护性。

► 使用 Python 内置函数和数据结构：Python 提供了许多内置函数和数据结构，如列表、字典、集合、 生成器、装饰器、lambda 表达式等。使用这些功能可以使代码更加简洁、高效和易于理解。

► 使用异常处理机制：Python 的异常处理机制可以使代码更加健壮和容错。在编写代码时应该预见到可能的异常情况，并使用 try/except 块来处理这些异常情况。

► 避免使用全局变量：全局变量可以使代码更加难以理解和维护，因为它们可能会被其他代码意外修改。应该尽量避免使用全局变量，而是使用函数或类来封装状态和行为。

► 使用函数式编程风格：函数式编程风格强调函数的不可变性和无状态性，使得代码更加简洁、高效和易于测试。应该尽可能使用纯函数，避免使用副作用和可变状态。

► 使用面向对象编程风格：面向对象编程风格可以使代码更加模块化和易于扩展。使用类和对象可以封装状态和行为，使代码更加结构化和易于维护。

► 编写文档和测试：编写文档和测试可以使代码更加易读、易于理解和易于维护。

有关PEP8，请参考： https://peps.python.org/pep-0008/ 如果在Python 编程中遇到问题或者bug，可以去以下几个地方寻求帮助： ► 官方文档：Python 官方文档提供了丰富的资源，包括语言参考手册、标准库参考手册、教程、示例代码等。可以先在官方文档中查找相关信息，寻找解决问题的方法。

► https://stackoverflow.com/：这是一个广泛使用的程序员问答社区，拥有庞大的用户群体和丰富的问题解答资源。可以在这里提出你的问题，或者搜索其他人遇到的类似问题的解决方法。

Page 17  |  Chapter 4 Python 语法基础  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 此外，ChatGPT 之类的助手工具也可以帮助我们解决编程中遇到的问题。

本章题目仅是请大家在JupyterLab 中复刻所有示例代码，并逐行注释加强理解。

* 题目不提供答案。

希望大家学习Python 时，一定要吸取英语学习失败的教训，千万不能死磕Python 语法。要用为主、学为辅，边学边用，活学活用。

Page 1  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Data Types in Python Python 数据类型字符串、列表、元组、字典…蜻蜓点水，了解就好

每个人都是天才。但是，如果您以爬树的能力来判断一条鱼，那么那条鱼终其一生都会相信自己是愚蠢的。

Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.

—— 阿尔伯特·爱因斯坦 (Albert Einstein)  |  理论物理学家  |  1879 ~ 1955

◄ copy.deepcopy() 创建指定对象的深拷贝 ◄ dict() Python 内置函数，创建一个字典数据结构 ◄ emunerate() Python 内置函数，返回索引和元素，可用于在循环中同时遍历序列的索引和对应的元素 ◄ float() Python 内置函数，将指定的参数转换为浮点数类型，如果无法转换则会引发异常 ◄ int() Python 内置函数，用于将指定的参数转换为整数类型，如果无法转换则会引发异常 ◄ len() Python 内置函数，返回指定序列，字符串、列表、元组等等，的长度，即其中元素的个数 ◄ list() Python 内置函数，将元组、字符串等等转换为列表 ◄ math.ceil() 将给定数值向上取整，返回不小于该数值的最小整数 ◄ math.e math 模块提供的常量，表示数学中的自然常数e 的近似值 ◄ math.exp() 计算以自然常数e 为底的指数幂 ◄ math.floor() 将给定数值向下取整，返回不大于该数值的最大整数 ◄ math.log() 计算给定数值的自然对数 ◄ math.log10() 计算给定数值的以10 为底的对数 ◄ math.pi math 模块提供的常量，表示数学中的圆周率的近似值 ◄ math.pow() 计算一个数的乘幂 ◄ math.round() 将给定数值进行四舍五入取整 ◄ math.sqrt() 计算给定数值的平方根 ◄ print() Python 内置函数，将指定的内容输出到控制台或终端窗口，方便用户查看程序的运行结果或调试信息 ◄ set() Python 内置函数，创建一个无序且不重复元素的集合，可用于去除重复元素或进行集合运算 ◄ str() Python 内置函数，用于将指定的参数转换为字符串类型 ◄ type() Python 内置函数，返回指定对象的数据类型

Page 2  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 5.1 数据类型有哪些?

通过上一章学习，我们知道Python 是一种动态类型语言，它支持多种数据类型。以下是Python 中常见的数据类型： ► 数字 (number) 类型：整数、浮点数、复数等。

► 字符串 (string) 类型：表示文本的一系列字符。

► 列表 (list) 类型：表示一组有序的元素，可以修改。

► 元组 (tuple) 类型：表示一组有序的元素，不能修改。

► 集合 (set) 类型：表示一组无序的元素，不允许重复。

► 字典 (dictionary) 类型：表示键-值对，其中键必须是唯一的。

► 布尔 (Boolean) 类型：表示True 和False 两个值。

► None 类型：表示空值或缺失值。

注意大小写问题，True、False、None 都是首字母大写。此外，注意Python 代码都是半角字符， 只有注释、Markdown 才能出现全角字符。

Python 还支持一些高级数据类型，如生成器 (Generator)、迭代器 (Iterator)、函数 (Function)、类 (Class) 等。

注意，对于Python 初学者，完全没有必要死记硬背每一种数据类型的操作方法。对于数据类型等Python 语法细节，希望大家蜻蜓点水，轻装上阵，边用边学。

## 5.2 数字：整数、浮点数、复数

Python 有三种内置数字类型： ► 整数 (int)：表示整数值，没有小数部分。例如，88、-88、0 等。

► 浮点数 (float)：表示实数值，可以有小数部分。例如，3.14、-0.5、2.0 等。

► 复数 (complex)：表示由实数和虚数构成的数字。

什么是复数？

复数是数学中的一个概念，由实部和虚部组成。它可以表示为 a + bi 的形式，其中 a 是实部，b 是虚部，而 i 是虚数单位，满足 i2 = -1。复数在数学和物理等领域中有广泛的应用。

复数扩展了实数域，使得可以处理平面上的向量运算、波动和振荡等问题。它在电路分析、信号处理、量子力学、调频通信等领域具有重要作用。复数还能用于描述周期性事件、解析函数和几何形状等。

Page 3  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 通过复数的运算，我们可以进行加法、减法、乘法和除法等操作，同时也可以求解方程、解析函数和变换等数学问题。复数的使用使得我们能够更好地描述和理解许多实际问题，扩展了数学的应用范围。

图 1 是一些示例，请大家在JupyterLab 中自行练习。

a b x = 88     # 整数 y = -8.88  # 浮点数 z = 8 + 8j # 虚数 print(type(x))

# <class 'int'> print(type(y))

# <class 'float'> print(type(z))

# <class 'complex'> Real Imaginary

图 1. Python 中三类数值

在Python 中，数字类型可以进行基本的算术操作，例如加法 (+)、减法 (-)、乘法 (*)、除法 (/)、取余数 (%)、乘幂 (**) 等。数字类型还支持比较运算符，如等于 (==)、不等于 (!=)、大于 (>)、小于 (<)、 大于等于 (>=)、小于等于 (<=)。此外，本书后文还会介绍自加运算 (+=)、自减运算 (-=)、自乘运算 (*=)、自除运算 (/=) 等。

本书第6 章将专门介绍Python 常见运算符。

类型转换在Python 中，可以使用内置函数将一个数字类型转换为另一个类型。下面是常用的数字类型转换函数： ► int(x)：将x 转换为整数类型。如果x 是浮点数，则会向下取整；如果x 是字符串，则字符串必须表示一个整数。

► float(x)：将x 转换为浮点数类型。如果x 是整数，则会转换为相应的浮点数；如果x 是字符串，则字符串必须表示一个浮点数。

► complex(x)：将x 转换为复数类型。如果x 是数字，则表示实部，虚部为0；如果x 是字符串， 则字符串必须表示一个复数；如果x 是两个参数，则分别表示实部和虚部。

► str(x)：将x 转换为字符串类型。如果x 是数字，则表示为字符串；如果x 是布尔类型，则返回 'True'或'False'字符串。

图 2 一些示例，请大家在JupyterLab 中自行练习。

需要注意的是，如果在类型转换过程中出现了不合理的转换，例如将一个非数字字符串转换为数字类型，就会导致ValueError 异常。

Page 4  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 本书第7 章将专门介绍如何处理异常。

a b x = 88.8 y = 8 # 将浮点数转换为整数 x_to_int = int(x)

print(x_to_int)  # 88 # 将整数转换为浮点数 y_to_float = float(y)

print(y_to_float)  # 8.0 # 将整数转换为复数 y_to_complex = complex(y)

print(y_to_complex)  # (8+0j)

# 将数字转换为字符串 x_to_str = str(x)

print(x_to_str)  # '88.8' .

Real Imaginary

图 2. Python 中数值转换

什么是异常？

在Python 中，异常 (exception) 是指在程序执行期间出现的错误或异常情况。当出现异常时，程序的正常流程被中断，转而执行异常处理的代码块，以避免程序崩溃或产生不可预知的结果。

Python 中有许多不同类型的异常，每种异常都代表了特定类型的错误。以下是一些常见的异常类型：ValueError (数值错误)：当函数接收到一个不合法的参数值时引发。TypeError (类型错误)：当使用不兼容的类型进行操作或函数调用时引发。IndexError (索引错误)：当尝试访问列表、元组或字符串中不存在的索引时引发。FileNotFoundError (文件未找到错误)：当尝试打开不存在的文件时引发。ZeroDivisionError (零除错误)：当尝试将一个数除以零时引发。

可以使用try-except 语句来捕获并处理这些异常，以便在程序出现问题时执行适当的操作或提供错误信息。

特殊数值有很很多场合还需要用到特殊数值，比如圆周率pi、自然对数底数e 等等。在Python 中，可以使用 Math 模块来引入这些特殊值，请大家在JupyterLab 中练习。

a b import math print(math.pi)      # 输出π的值 print(math.e)       # 输出e的值 print(math.sqrt(2)) # 输出根号2的值

Page 5  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 3. Math 模块中的特殊数值

除了这些特殊数值外，Math 模块还提供了许多其他数学函数，比如四舍五入round()、上入取整数 ceil()、下舍取整数 floor()、乘幂运算pow()、指数函数exp()、以e 为底数的对数log()、以10 为底数的对数log10()等等。

注意，大家日后会发现我们一般很少用到Math 模块，为了方便向量化运算我们会直接采用 NumPy、Pandas 中的运算函数。

## 5.3 字符串：用引号定义的文本

Python 中字符串 (string) 是一个常见的数据类型，常常用于表示文本信息。本节介绍一些常用的字符串用法。

字符串定义使用单引号'、双引号"、三引号'''或"""将字符串内容括起来即可定义字符串。请大家在JupyerLab 中练习图 7 代码。三引号'''或"""一般用来创建多行字符串。

注意，空格、标点符号都是字符串的一部分。使用加号 + 将多个字符串连接起来，使用乘号 * 复制字符串。数字字符串仅仅是文本，不能直接完成算数运算，需要转化成整数、浮点数之后才能进行算数运算。

请大家用len() 函数获得图 7 每个字符串的长度，即字符串中字符个数。

注意，Python 中长度为0 的字符串也是字符串类型，比如str_test = ''; type(str_test)。

+ J e a s !

y , H e y , J e a H e s !

图 4. 字符串相加

*

图 5. 数字字符串乘法

+

图 6. 数字字符串加法

Page 6  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b str1 = 'I am learning Python 101!' print(str1)

# 打印 str2 = "Python is fun. Machine learning is fun too."

print(str2)

# 打印 # 使用加号 + 将多个字符串连接起来 str4 = 'Hey, ' + 'James!' print(str4)

# 'Hey, James!' # 使用乘号*将一个字符串复制多次 str5 = 'Python is FUN! '  # 字符串最后有一个空格 str6 = str5 * 3 print(str6)

# 'Python is FUN! Python is FUN! Python is FUN!' # 字符串中的数字仅仅是字符 str7 = '123' str8 = str7 * 3 print(str8)

str9 = '456' str10 = str9 + str7 print(str10)

print(type(str10))

e f g h t h s P y F U o N !

!

H e y , J a e s !

H e y , J a e s

图 7. 字符串定义和操作

索引、切片在Python 中，可以通过索引 (indexing) 和切片 (slicing) 来访问和操作字符串中的单个字符、部分字符。

如图 8 所示，字符串中的每个字符都有一个对应的索引位置，索引从0 开始递增。可以使用方括号 []

来访问指定索引位置的字符。

可以使用负数索引来从字符串的末尾开始计算位置。例如，-1 表示倒数第一个字符，-2 表示倒数第二个字符，依此类推。请大家自行在JupyterLab 中练习图 10。

图 10 代码中使用了for 循环来遍历字符串中的每个字符，并打印出字符及其对应的序号。enumerate()

函数来同时获取字符和它们的索引位置。enumerate() 函数会返回一个迭代器，包含每个字符及其对应的索引。然后，通过 for 循环遍历迭代器，依次打印出每个字符和它们的序号。

本书第7 章将专门介绍for 循环。

在代码中，f-字符串 (formatted string) 是一种用于格式化字符串的语法。它以字母 "f" 开头，并使用花括号（{}）来插入变量或表达式的值。在这个特定的例子中，f-字符串用于构建一个带有变量值的字符串。通过在字符串中使用花括号和变量名，可以在字符串中插入变量的值。在这种情况下，使用了两个变量 {char} 和 {index}。当代码执行时，{char} 会被替换为当前循环迭代的字符，{index} 会被替换为对应字符的索引值。这样就创建了一个字符串，包含了字符及其对应的序号信息。

Page 7  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com y , J e a H e s !

Index a = 'Hey, James' a[0]

a[1]

a[2]

a[-3]

a[-2]

a[-1]

y , J e a H e s !

H e y e s !

图 8. 字符串的索引

切片是指从字符串中提取出一部分子字符串。可以使用半角冒号 : 来指定切片的起始位置start 和结束end 位置。语法为 string[start:end]，包括start 序号对应的字符，但是不包括end 位置的字符，相当于“左闭右开”区间。

切片还可以指定步长 (step)，用于跳过指定数量的字符。语法为 string[start:end:step]。

注意，复制字符串可以采用string_name[:] 实现。

Python 中还有很多字符串“花式”切片方法，大家没有必要花大力气去“精雕细琢”。大概知道字符串有哪些常见的索引、切片方法就足够了，等到用到时再去特别学习。还是那句话，别死磕Python 语法！

Inde a = 'Hey, James' a[:3]

y , J e a H e s !

a[1:6]

a[::2]

a[::-1]

y H e y , J e y e a H !

y , J e a H e s !

H y a e !

图 9. 字符串的切片

需要注意的是，索引和切片操作不会改变原始字符串，而是返回一个新的字符串。

Page 8  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b e f g h y , a H e e s J !

greeting_str = 'Hey, James!' # 打印字符串长度 print('字符串的长度为：')

print(len(greeting_str))

# 打印每个字符和对应的序号 for index, char in enumerate(greeting_str): print(f"字符：{char}，序号：{index}")

# 单个字符索引 print(greeting_str[0])

print(greeting_str[1])

print(greeting_str[-1])

print(greeting_str[-2])

# 切片 # 取出前3个字符，序号为0、1、2 print(greeting_str[:3])

# 取出序号1、2、3、4、5，不含0，不含6 print(greeting_str[1:6])

# 指定步长2，取出第0、2、4 ...

print(greeting_str[::2])

# 指定步长-1，倒序 print(greeting_str[::-1])

j k H e !

s y H e y , e J y a H e !

y , a H e e s J !

图 10. 字符串索引和切片从0 计数 vs 从1 计数从0 计数和从1 计数是在数学和编程中常见的计数方式。

从0 计数 (zero-based counting) 将第一个元素的索引或位置标记为0，即从0 开始计数。例如，对于一个包含n 个元素的序列，它们的索引分别为0、1、2、...、n − 1。在计算机科学和编程中，Python 使用从0 计数的方式。

从1 计数 (one-based counting) 将第一个元素的索引或位置标记为1，即从1 开始计数。例如，对于一个包含n 个元素的序列，它们的索引分别为1、2、3、...、n。MATLAB 使用从1 计数方式；统计学 (样本)、线性代数 (矩阵、向量) 等通常使用从1 计数的方式。

相比来看，从1 计数更符合人类直观理解的习惯。从1 计数在数学、统计学、数值计算等领域中较为常见。编程角度来看，从0 计数在计算机科学中更常见，因为它与计算机内存和数据结构的底层表示方式相匹配。它使得处理数组、列表和字符串等数据结构更加高效和一致。

在实际编程中，理解和适应使用不同的计数方式是重要的。需要根据具体情况选择适当的计数方式，以确保正确地处理索引、循环和算法等操作。同时，注意在不同的领域和语境中遵循相应的计数习惯和规则。

Page 9  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 字符串方法 Python 提供了许多用于字符串处理的常见方法。下面是一些常见的字符串方法及其示例。

len() 返回字符串的长度，比如下例。

string = "Hello, James!"

length = len(string)

print(length)

lower() 和upper() 将字符串转换为小写或大写，比如下例。

string = "Hello, James!"

lower_string = string.lower()

upper_string = string.upper()

print(lower_string)  # 输出 "hello, james!"

print(upper_string)  # 输出 "HELLO, JAMES!"

以下是一些常见的 Python 字符串方法及其作用：capitalize():将字符串的第一个字符转换为大写，其他字符转换为小写。count() 统计字符串中指定子字符串的出现次数。find() 在字符串中查找指定子字符串的第一次出现，并返回索引值。isalnum() 检查字符串是否只包含字母和数字。isalpha() 检查字符串是否只包含字母。isdigit() 检查字符串是否只包含数字。join() 将字符串列表或可迭代对象中的元素连接为一个字符串。replace() 将字符串中的指定子字符串替换为另一个字符串。split() 将字符串按照指定分隔符分割成子字符串，并返回一个列表。

注意，这些方法大家也不需要死记硬背！了解就好，轻装上阵。数据分析、机器学习中更常用的 NumPy 数组、Pandas 数据帧，这都是本书后续要重点介绍的内容。

## 5.4 列表：存储多个元素的序列

在 Python 中，列表 (list) 是一种非常常用的数据类型，可以存储多个元素，并且可以进行增删改查等多种操作。

图 13 代码生成的是一个特殊的列表，我们称之为混合列表，原因是这个列表中每个元素都不同。如图 11 所示，这个列表中序号为4 的元素 (从左到右第5 个元素) 还是个列表，相当于嵌套。

Index 1.0 '12ab' True [1,1.0,'1']

{1} {1:1.0} int float str bool list set dict

图 11. 混合列表

图 13 还给出 list 常用的索引方法，请大家在JupyterLab 中练习。列表的索引、切片方式和字符串类似，我们不再展开。其中大家需要注意的是如果列表中的某个元素也是列表，我们可以通过二次索引来进一步索引、切片，如图 12 所示。

Page 10  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 请大家在JupyterLab 中练习图 14 给出的list 常见方法、操作。

1.0 '12ab' True [1,1.0,'1']

{1} {1:1.0} '1' 1.0 a[4]

a[4][1]

1.0 a b a[2]

a[2][2]

a

图 12. 混合列表的索引

a b e f g h j k # 创建一个混合列表 my_list = [1, 1.0, '1', True, [1, 1.0, '1'], {1}, {1:1.0}]

print('列表长度为')

print(len(my_list))

# 打印每个元素和对应的序号 for index, item in enumerate(my_list): type_i = type(item)

print(f"元素：{item}，序号：{index}，类型：{type_i}")

# 列表索引 print(my_list[0])

print(my_list[1])

print(my_list[-1])

print(my_list[-2])

# 列表切片 # 取出前3个元素，序号为0、1、2 print(my_list[:3])

# 取出序号1、2、3，不含0，不含4 print(my_list[1:4])

# 指定步长2，取出第0、2、4、6 print(my_list[::2])

# 指定步长-1，倒序 print(my_list[::-1])

# 提取列表中的列表某个元素 print(my_list[4][1])

图 13. 列表索引和切片

Page 11  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b e f g h j # 创建一个混合列表 my_list = [1, 1.0, '12ab', True, [1, 1.0, '1'], {1}, {1:1.0}]

print(my_list)

# 修改某个元素 my_list[2] = '123' print(my_list)

# 在列表指定位置插入元素 my_list.insert(2, 'inserted')

print(my_list)

# 在列表尾部插入元素 my_list.append('tail')

print(my_list)

# 通过索引删除 del my_list[-1]

print(my_list)

# 删除某个元素 my_list.remove('123')

print(my_list)

# 判断一个元素是否在列表中 if '123' in my_list: print("Yes")

else: print("No")

# 列表翻转 my_list.reverse()

print(my_list)

# 将列表用所有字符连接，连接符为下划线 _ letters = ['J', 'a', 'm', 'e', 's']

word = '_'.join(letters)

print(word)

图 14. 列表常用方法、操作

视图 vs 浅复制 vs 深复制如果用 = 直接赋值，是非拷贝方法，结果是产生一个视图 (view)。这两个列表是等价的，修改其中任何 (原始列表、视图) 一个列表都会影响到另一个列表。

如图 15 所示，用等号 = 赋值得到的list_2 和list_1 共享同一地址，这就是我们为什么称list_2 为视图。视图这个概念是借用自NumPy。

我们在本书后续还要聊到NumPy array 的视图和副本这两个概念。

而通过copy() 获得的list_3 和list_1 地址不同。请大家自行在JupyterLab 中练习图 16。

Page 12  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com list_1 list_2 = list_1 list_3 = list_1.copy()

图 15. 视图，还是副本？

a b list1 = [1, 2, 3, 4]

# 赋值，视图 list2 = list1 # 拷贝，副本 (浅拷贝)

list3 = list1.copy()

list2[0] = 'a' list2[1] = 'b' list3[2] = 'c' list3[3] = 'd' print(list1)

print(list2)

print(list3)

e

图 16. 视图 vs 副本

可惜事情并没有这么简单。在 Python 中，列表是可变对象，因此在复制列表时会涉及到深复制和浅复制的概念。

浅复制 (shallow copy) 只对list 的第一层元素完成拷贝，深层元素还是和原list 共用。

深复制 (deep copy) 是创建一个完全独立的列表对象，该对象中的元素与原始列表中的元素是不同的对象。

注意，特别是对于嵌套列表，建议大家采用copy.deepcopy() 深复制。图 17 代码比较不同复制，请大家自行学习。

Page 13  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a import copy list1 = [1, 2, 3, [4, 5]]

print('原始list')

print(list1)

# 深复制，适用于嵌套列表 list_deep = copy.deepcopy(list1)

# 只深复制一层 list2 = list1.copy()

list3 = list1[:]

list4 = list(list1)

list5 = [*list1]

# 修改元素 list_deep[3][0] = 'deep' list_deep[2] = 'worked_0' list2[3][0] = 'abc' list2[2] = 'worked_1' list3[3][0] = 'X1' list3[2] = 'worked_2' list4[3][0] = 'X2' list4[2] = 'worked_3' list5[3][0] = 'X3' list5[2] = 'worked_4' print('新list')

print(list1)

print(list_deep)

print(list2)

print(list3)

print(list4)

print(list5)

e b f g h j k

图 17. 浅复制、深复制

## 5.5 其他数据类型：元素、集合、字典

元组

Page 14  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 在Python 中，元组 (tuple) 是一种不可变的序列类型，用圆括号 () 来表示。元组一旦创建就不能被修改，这意味着你不能添加或删除其中的元素。

tuple 和list 都是序列类型，可以存储多个元素，它们都可以通过索引访问和修改元素，支持切片操作。但是，两者有明显区别，元组使用圆括号 ( ) 表示，而列表使用方括号 [ ] 表示。元组是不可变的， 而列表是可变的。这意味着元组的元素不能被修改、添加或删除，而列表可以进行这些操作。

元组的优势在于它们比列表更轻量级，这意味着在某些情况下，它们可以提供更好的性能和内存占用。本书不展开介绍元组。

集合在Python 中，集合 (set) 是一种无序的、可变的数据类型，可以用来存储多个不同的元素。使用花括号 {} 或者 set() 函数创建集合，或者使用一组元素来初始化一个集合。

number_set = {1, 2, 3, 4, 5} word_set = set(["apple", "banana", "orange"])

可以使用 add() 方法向集合中添加单个元素，使用 update() 方法向集合中添加多个元素。

fruit_set = set(["apple", "banana"])

fruit_set.add("orange")

fruit_set.update(["grape", "kiwi"])

删除元素：使用 remove() 或者 discard() 方法删除集合中的元素，如果元素不存在，remove() 方法会引发 KeyError 异常，而 discard() 方法则不会。

fruit_set.remove("banana")

fruit_set.discard("orange")

集合的好处是可以用交集、并集、差集等集合操作来操作集合，如图 18 所示。

set1 = {1, 2, 3, 4} set2 = {3, 4, 5, 6} set3 = set1 & set2  # 交集 set4 = set1 | set2  # 并集 set5 = set1 - set2  # 差集

A B A B A B A B A B A B −

图 18. 交集、并集、差集

字典在 Python 中，字典是一种无序的键值对 (key-value pair) 集合。

可以使用大括号 {} 或者 dict() 函数创建字典，键 (key) 值 (value) 对之间用冒号 : 分隔。有关字典这种数据类型本书不做展开，请大家自行学习图 19。

Page 15  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 注意，使用大括号 {} 创建字典时，字符串键key 用引号；而使用 dict() 创建字典时，字符串键不使用引号。

再次强调，数据分析、机器学习实践中，我们更关注的数据类型是NumPy 数组、Pandas 数据帧， 这是本书后续要着重讲解的内容。

a b f g h # 使用大括号创建字典 person = {'name': 'James', 'age': 88, 'gender': 'male'} # 使用 dict() 函数创建字典 fruits = dict(apple=88, banana=888, cherry=8888)

# 访问字典中的值 print(person['name'])

print(fruits['cherry'])

# 修改字典中的值 person['age'] = 28 print(person)

# 添加键值对 person['city'] = 'Toronto' print(person)

# 删除键值对 del person['gender']

print(person)

# 获取键、值、键值对列表 print(person.keys())

print(person.values())

print(person.items())

e j name key age gender value James male apple key banana cherry value

图 19. 有关字典的常见操作

## 5.6 矩阵、向量：线性代数概念

矩阵、向量抛开本章前文这些数据类型，数学上我们最关心的数据类型是——矩阵、向量。

简单来说，矩阵 (matrix) 是一个由数值排列成的矩形阵列，其中每个数值都称为该矩阵的元素。矩阵通常使用大写、斜体、粗体字母来表示，比如A、B、V、X。

向量 (vector) 是一个有方向和大小的量，通常表示为一个由数值排列成的一维数组。向量通常使用小写字母加粗体来表示，例如x、a、b、v、u。

Page 16  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 如图 20 所示，一个n × D (n by capital D) 矩阵X，n 是矩阵行数 (number of rows in the matrix)，D 是矩阵列数 (number of columns in the matrix)。矩阵X 的行索引就是1、2、3、...、n。矩阵X 的列索引就是 1、2、3、...、D。

x1,1代表矩阵第1 行、第1 列元素，xi,j代表矩阵第i 行、第j 列元素。

n × D n rows D columns First row First column ith row jth column xi,j 1,1 1,2 1, 2,1 2,2 2, ,1 ,2 , D D n D n n n D        =       X

图 20. n × D  矩阵X

从数据、统计、线性代数、几何角度解释，什么是矩阵？

矩阵是一个由数字或符号排列成的矩形阵列。简单来说，矩阵就是个表格。矩阵在数据、统计、线性代数和几何学中扮演着重要的角色。

从数据的角度来看，矩阵可以表示为一个包含行和列的数据表。每个单元格中的数值可以代表某种测量结果、观察值或特征。数据科学家和分析师使用矩阵来存储和处理数据，从中提取有用的信息。比如，一张黑白照片中的数据就可以看做是个矩阵。

从统计学的角度来看，矩阵可以用于描述多个变量之间的关系。例如，协方差矩阵用于衡量变量之间的相关性，而相关矩阵则提供了变量之间的线性相关性度量。统计学家使用这些矩阵来推断模式、关联和依赖性，以及进行数据分析和建模。

从线性代数的角度来看，矩阵可以用于表示线性方程组的系数矩阵。通过矩阵运算，例如矩阵乘法、求逆和特征值分解，可以解决线性方程组、求解特征向量和特征值等问题。线性代数中的矩阵理论提供了处理线性关系的强大工具。

从几何学的角度来看，矩阵可以用于表示几何变换。通过将向量表示为矩阵的列或行，可以应用平移、旋转、缩放等几何变换。

矩阵乘法用于组合多个变换，从而实现更复杂的几何操作。在计算机图形学和计算机视觉中，矩阵在处理和表示二维或三维对象的位置、方向和形状方面起着重要作用。

总而言之，矩阵是一个在数据、统计、线性代数和几何学中广泛应用的数学工具，它能够表示和处理多个变量之间的关系、解决线性方程组、进行几何变换等。

几何视角看：行向量、列向量行向量 (row vector) 是由一系列数字或符号排列成的一行序列。列向量 (column vector) 是由一系列数字或符号排列成的一列序列。

矩阵可以视作由一系列行向量、列向量构造而成。这相当于硬币的正反两面，即一体两面。

我们可以用嵌套列表方式来表达矩阵，如

Page 17  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 2-dimensional space Row vectors 3-dimensional space Column vectors x1 x2 x2 x3 x1 3 × 2 1 × 2 A a1 a2 a(1)

a(2)

a(3)

图 21. 行向量和列向量

2-dimensional space Column vectors 3-dimensional space Row vectors x1 x2 x2 x3 x1 3 × 2 2 × 1 A Transpose 2 × 3 B = AT b1 b2 b3 b(1)

b(2)

图 22. 转置之后矩阵的行向量和列向量

Page 18  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b # 用嵌套列表构造矩阵 A = [[0,5], [3,4], [5,0]]

# 取出行向量 print(A[0])

print([A[0]])

print(A[1])

print([A[1]])

print(A[2])

print([A[2]])

# 取出列向量 print([row[0] for row in A])

print([[row[0]] for row in A])

print([row[1] for row in A])

print([[row[1]] for row in A])

a 3 × 2 A

图 23. 用列表构造矩阵

什么是矩阵转置？

矩阵转置是指将矩阵的行和列对调，得到一个新的矩阵。原矩阵的第 i 行会变成新矩阵的第 i 列，原矩阵的第 j 列会变成新矩阵的第 j 行。这个操作不改变矩阵的元素值，只是改变了它们的排列顺序。

鸢尾花数据从统计数据角度，n 是样本个数，D 是样本数据特征数。如图 24 所示，鸢尾花数据集，不考虑标签 (即鸢尾花三大类setosa、versicolor、virginica)，数据集本身n = 150，D = 4。

Page 19  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Index Sepal length X1 Sepal width X2 Petal length X3 Petal width X4 Species C Setosa C1 Versicolor C2 Virginica C3 5.1 3.5 1.4 0.2 4.9 1.4 0.2 4.7 3.2 1.3 0.2 5.3 3.7 1.5 0.2 3.3 1.4 0.2 3.2 4.7 1.4 6.4 3.2 4.5 1.5 6.9 3.1 4.9 1.5 5.1 2.5 1.1 5.7 2.8 4.1 1.3 6.3 3.3 2.5 5.8 2.7 5.1 1.9 7.1 5.9 2.1 6.2 3.4 5.4 2.3 5.9 5.1 1.8 ...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

图 24. 鸢尾花数据，数值数据单位为厘米 (cm)

什么是鸢尾花数据集？

鸢尾花数据集是一种经典的用于机器学习和模式识别的数据集。数据集的全称为安德森鸢尾花卉数据集 (Anderson's Iris data set)， 是植物学家埃德加·安德森 (Edgar Anderson) 在加拿大魁北克加斯帕半岛上的采集的鸢尾花样本数据。它包含了150 个样本，分为三个不同品种的鸢尾花 (山鸢尾、变色鸢尾和维吉尼亚鸢尾)，每个品种50 个样本。每个样本包含了四个特征：花萼长度、花萼宽度、花瓣长度和花瓣宽度。

鸢尾花数据集由统计学家罗纳德·费舍尔 (Ronald Fisher) 在1936 年引入，并被广泛用于模式识别和机器学习的教学和研究。这个数据集是机器学习领域的一个基准测试数据集，被用来评估分类算法的性能。

鸢尾花数据集在机器学习应用中有很多用途。它经常被用来进行分类任务，即根据花的特征将其分为不同的品种。许多分类算法和模型，如K 近邻、决策树、支持向量机和神经网络等，都可以使用鸢尾花数据集进行训练和测试。

由于鸢尾花数据集是一个相对简单的数据集，它也常用于机器学习的入门教学和实践。通过对这个数据集的分析和建模，学习者可以了解特征工程、模型选择和评估等机器学习的基本概念和技术。矩阵是一个由数字或符号排列成的矩形阵列。简单来说，矩阵就是个表格。矩阵在数据、统计、线性代数和几何学中扮演着重要的角色。

如图 25 所示，X 任一行向量代表一朵特定鸢尾花样本花萼长度、花萼宽度、花瓣长度和花瓣宽度测量结果。而X 某一列向量为鸢尾花某个特征 (花萼长度、花萼宽度、花瓣长度、花瓣宽度) 的样本数据。

Page 20  |  Chapter 5 Python 数据类型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X x(i)

150 × 4 150 × 4 xj 4-dimensional space 150-dimensional space Row vectors Column vectors 150 × 4

图 25. 矩阵可以分割成一系列行向量或列向量

请大家完成下面1 道题目。

Q1. 本章的唯一的题目就是请大家在JupyterLab 中练习本章正文给出的示例代码。

* 不提供答案。

Page 1  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Basic Calculations in Python Python 常见运算从加减乘除开始学运算符

有时人们不想听到真相，因为他们不想打碎自己的幻象。

Sometimes people don't want to hear the truth because they don't want their illusions destroyed.

—— 弗里德里希·尼采 (Friedrich Nietzsche)  |  德国哲学家  |  1844 ~ 1900

◄ + 算术运算符，加法；将两个数值相加或连接两个字符串 ◄ - 算术运算符，减法；从一个数值中减去另一个数值 ◄ * 算术运算符，乘法；将两个数值相乘 ◄ / 算术运算符，除法；将一个数值除以另一个数值，得到浮点数结果 ◄ % 算术运算符，取余数；计算两个数相除后的余数 ◄ ** 算术运算符，乘幂；将一个数值的指数幂次方 ◄ == 比较运算符，等于；判断两个值是否相等，返回一个布尔值 (True 或False)

◄ != 比较运算符，不等于；判断两个值是否不相等，返回一个布尔值 (True 或False)

◄ > 比较运算符，大于；判断左边的值是否大于右边的值，返回一个布尔值 (True 或False)

◄ < 比较运算符，小于；判断左边的值是否小于右边的值，返回一个布尔值 (True 或False)

◄ >= 比较运算符，大于等于；判断左边的值是否大于或等于右边的值，返回一个布尔值 (True 或False)

◄ <= 比较运算符，小于等于；判断左边的值是否小于或等于右边的值，返回一个布尔值 (True 或False)

◄ and 逻辑运算符，与；判断两个条件是否同时为真，如果两个条件都为真，则返回True；否则返回False ◄ or 逻辑运算符，或；判断两个条件是否有一个为真，如果至少有一个条件为真，返回True；否则返回False ◄ not 逻辑运算符，非；对一个条件进行取反，如果条件为真，则返回False；如果条件为假，则返回True ◄ = 赋值运算符，等于；将等号右侧的值赋给左侧的变量，即将右侧的值存储到左侧的变量中 ◄ += 赋值运算符，自加运算；将变量与右侧的值相加，并将结果赋值给该变量，例如，a += b 等价于a = a + b ◄ -= 赋值运算符，自减运算；将变量与右侧的值相减，并将结果赋值给该变量，例如，a -= b 等价于a = a - b ◄ *= 赋值运算符，自乘运算；将变量与右侧的值相乘，并将结果赋值给该变量，例如，a *= b 等价于a = a * b ◄ /= 赋值运算符，自除运算；将变量与右侧的值相除，并将结果赋值给该变量，例如，a /= b 等价于a = a / b ◄ in 成员运算符；检查某个值是否存在于指定的序列 (如列表、元组、字符串等) 中，如果存在则返回True，否则返回 False ◄ not in 成员运算符；检查某个值是否不存在于指定的序列 (如列表、元组、字符串等) 中，如果不存在则返回True， 否则返回False。

◄ is 身份运算符；检查两个变量是否引用同一个对象，如果是则返回True，否则返回False ◄ is not 身份运算符；检查两个变量是否不引用同一个对象，如果不是则返回True，否则返回False

Page 2  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 6.1 几类运算符

Python 中的运算符可以分为以下几类： ► 算术运算符：用于数学运算，例如加法 (+)、减法 (-)、乘法 (*)、除法 (/)、取余数 (%)、 乘幂 (**) 等。

► 比较运算符：用于比较两个值之间的关系，例如等于 (==)、不等于 (!=)、大于 (>)、小于 (<)、大于等于 (>=)、小于等于 (<=) 等。

► 逻辑运算符：用于处理布尔型数据，例如与 (and)、或 (or)、非 (not) 等。

► 赋值运算符：用于给变量赋值，例如等号 (=)、自加运算 (+=)、自减运算 (-=)、自乘运算 (*=)、自除运算 (/=)。

► 成员运算符：用于检查一个值是否为另一个值的成员，例如in、not in 等。

► 身份运算符：用于检查两个变量是否引用同一个对象，例如is、is not 等。

以上是Python 中常见的运算符，可以根据不同的场景选择合适的运算符进行操作。

Arithmetic operators +

× / &

~ ^ >> << Membership operators not in in is not is and or not ！= =< >= == > < ** % // Assignment operators += /= = *= %= **= //= Identity operators Bitwise operators Logical operators

图 1. 常用运算符

## 6.2 算术运算符

Python 算术运算符用于数学运算，包括加法、减法、乘法、除法、取模和幂运算等。下面分别介绍这些算术运算符及其使用方法。

加减法

Page 3  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 加法运算符 (+) 用于将两个数值相加或将两个字符串拼接起来。

请大家在JupyterLab 中自行练习图 2。

当进行加法运算时，如果操作数的类型不一致，Python 会自动进行类型转换。如果一个数是整数， 而另一个是浮点数，则整数会被转换为浮点数，然后进行加法运算。运算结果为浮点数。加法时，如果一个数是整数，而另一个是复数，则整数会被转换为复数，然后进行加法运算。结果为复数。如果一个操作数是浮点数，而另一个是复数，则浮点数会被转换为复数，然后进行加法运算。运算结果为复数。

减法运算符 - 用于将两个数值相减，不支持字符串运算，错误信息为TypeError: unsupported operand type(s) for -: 'str' and 'str'。

a b # 数值加法 a = 10    # 整数 b = 20.0  # 浮点数 c = a + b # 浮点数 print(c)

# 字符串拼接 str_a = "10"    # str(a)

str_b = "20.0"  # str(b)

str_c = str_a + str_b print(str_c)

.

.

+

图 2. 加法

乘除法乘法运算符 (*) 用于将两个数值相乘或将一个字符串重复多次。

注意，NumPy 数组完成矩阵乘法 (matrix multiplication) 时用的运算符为 @。

a b # 数值乘法 a = 10    # 整数 b = 20.0  # 浮点数 c = a * b # 浮点数 print(c)

# 字符串复制 str_a = "10"    # str(a)

str_b = "20.0"  # str(b)

str_c = str_a * 3 str_d = str_b * 2 print(str_c)

print(str_d)

.

.

.

图 3. 乘法除法运算符 / 用于将两个数值相除，结果为浮点数。

Page 4  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 在Python 中，正斜杠 / (forward slash) 和反斜杠 \ (backward slash) 具有不同的用途和含义。在路径表示中，正斜杠 / 用作目录分隔符，用于表示文件系统路径。在除法运算中，正斜杠用作除法操作符。

在Windows 文件路径表示中，反斜杠用作目录分隔符。在字符串中，反斜杠 \ 用作转义字符， 用于表示特殊字符或字符序列，比如： ► \n 换行符，将光标位置移到下一行开头。

► \r 回车符，将光标位置移到本行开头。

► \t 水平制表符，也即 Tab 键，一般相当于四个空格。

► \\ 反斜线；在使用反斜杠作为转义字符时，为了表示反斜杠本身，需要使用两个连续的反斜杠 \\。

► \' 单引号 ► \" 双引号 ► \ 在字符串行尾的续行符，即一行未完，转到下一行继续写。

取模运算符 % 用于获取两个数值相除的余数，比如10 % 3 的结果为1。幂运算符 ** 用于将一个数值的幂次方，比如 2**3 的结果为8。

什么是转义字符？

转义字符是一种在字符串中使用的特殊字符序列，以反斜杠 \ 开头。在Python 中，转义字符用于表示一些特殊字符、控制字符或无法直接输入的字符。通过使用转义字符，我们可以在字符串中插入换行符、制表符、引号等特殊字符。

括号在Python 中，运算符有不同的优先级。有时我们需要改变运算符的优先级顺序，可以使用圆括号 (parentheses) 来改变它们的顺序。圆括号可以用于明确指定某些运算的执行顺序，确保它们在其他运算之前或之后进行。

请大家自行比较下两例： result = 2 + 3 * 4 result = (2 + 3) * 4 根据运算符的优先级规则，乘法运算 * 具有更高的优先级，因此先执行乘法，然后再进行加法。所以结果是 14。如果我们想先执行加法运算，然后再进行乘法运算，可以使用圆括号来改变优先级。

## 6.3 比较运算符

Python 比较运算符用于比较两个值，结果为True 或False。

Page 5  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

相等、不等相等运算符 == 比较两个值是否相等，返回True 或False。不等运算符 != 比较两个值是否不相等， 返回True 或False。

a b x = 5 y = 3 print(x == y)    # False print(x == 5)    # True print(x != y)    # True print(x != 5)    # False print(x != 5.0)  # False

图 4. 相等、不等

大于、大于等于大于运算符 > 比较左边的值是否大于右边的值，返回True 或False。大于等于运算符 >= 比较左边的值是否大于等于右边的值，返回True 或False。

a b x = 5 y = 3 print(x > y)   # True print(x > 10)  # False print(x >= y)  # True print(x >= 5)  # True

图 5. 大于、大于等于

小于、小于等于小于运算符 < 比较左边的值是否小于右边的值，返回True 或False。小于等于运算符 <= 比较左边的值是否小于等于右边的值，返回True 或False。

a b x = 5 y = 3 print(x < y)   # False print(x < 10)  # True print(x <= y)  # False print(x <= 5)  # True

图 6. 小于、小于等于

Page 6  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 6.4 逻辑运算符

Python 中有三种逻辑运算符，分别为and、or 和not，这些逻辑运算符可用于布尔类型的操作数上。

这三种逻辑运算符实际上体现的是真值表 (truth table) 的逻辑。

如图 7 所示，真值表是一个逻辑表格，用于列出逻辑表达式的所有可能的输入组合和对应的输出结果。它展示了在不同的输入情况下，逻辑表达式的真值 True 或假值 False。下面对每种逻辑运算符进行详细的讲解。

False True False True A False False True True B False False False True A and B False True False True A False False True True B False True True True A or B False True A True False not A

图 7. 真值表

和运算符and 当左右两边的操作数都为True 时，返回True，否则返回False。或运算符or 当左右两边的操作数至少有一个为True 时，返回True，否则返回False。取非运算符not 对一个布尔类型的操作数取反，如果操作数为True，返回False，否则返回True。请大家在JupyterLab 自行练习图 8。

逻辑运算符常用于条件判断、循环控制等语句中。通过组合不同的逻辑运算符，可以实现复杂的逻辑表达式。

a b # 和 and print(True and True)

print(True and False)

print(False and True)

print(False and False)

# 或 or print(True or True)

print(True or False)

print(False or True)

print(False or False)

# 非 not print(not True)

print(not False)

图 8. 逻辑运算符

Page 7  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 6.5 赋值运算符

Python 中的赋值运算符用于将值分配给变量，下面逐一讲解。

等号 = 将右侧的值赋给左侧的变量。

加等于 += 将右侧的值加到左侧的变量上，并将结果赋给左侧的变量。

减等于 -= 将右侧的值从左侧的变量中减去，并将结果赋给左侧的变量。

乘等于 *= 将右侧的值乘以左侧的变量，并将结果赋给左侧的变量。

除等于 /= 将左侧的变量除以右侧的值，并将结果赋给左侧的变量。

取模等于 %= 将左侧的变量对右侧的值取模，并将结果赋给左侧的变量。

幂等于 **= 将左侧的变量的值提高到右侧的值的幂，并将结果赋给左侧的变量。

a b a = 5 print(a)

a += 3  # 等同于 a = a + 3，此时 a 的值为 8 print(a)

a -= 3  # 等同于 a = a - 3，此时 a 的值为 5 print(a)

a *= 2  # 等同于 a = a * 2，此时 a 的值为 10 print(a)

a /= 5  # 等同于 a = a / 5，此时 a 的值为 2.0 print(a)

a %= 3  # 等同于 a = a % 3，此时 a 的值为 2.0 print(a)

a **= 3 # 等同于 a = a ** 3，此时 a 的值为 8.0 print(a)

e f g

图 9. 赋值运算

## 6.6 成员运算符

Python 中成员运算符用于测试是否存在于序列中。共有两个成员运算符：a) in：如果在序列中找到值，返回True，否则返回False。b) not in：如果在序列中没有找到值，返回True，否则返回False。

图 10 是成员运算符的示例代码，请大家在JupyterLab 中自行练习。

Page 8  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b # 定义一个列表 my_list = [1, 2, 3, 4, 5]

# 判断元素是否在列表中 print(3 in my_list)  # True print(6 in my_list)  # False # 判断元素是否不在列表中 print(3 not in my_list)  # False print(6 not in my_list)  # True

图 10. 成员运算

## 6.7 身份运算符

Python 身份运算符包括is 和is not，用于判断两个对象是否引用同一个内存地址。请大家回顾上一章介绍的视图、浅复制、深复制这三个概念。简单来说，浅复制只复制对象的一层内容，不涉及到嵌套的可变对象。深复制创建一个全新的对象，并递归地复制原始对象及其嵌套的可变对象。每个对象的副本都是独立的，修改原始对象或其嵌套对象不会影响深复制的对象。深复制涉及到多层嵌套的可变对象，确保每个对象都被复制。

请大家自行练习图 11 给出代码。

a b import copy a = [1, 2, 3]

b = a # 视图 b 引用 a 的内存地址 c = [1, 2, 3]

d = a.copy()

print(a is b)

# 输出 True，因为 a 和 b 引用同一个内存地址 print(a is not c)

# 输出 True，因为 a 和 c 引用不同的内存地址 print(a == c)

# 输出 True，因为 a 和 c 的值相等 print(a is not d)

# 输出 True，因为 a 和 d 引用不同的内存地址 print(a == d)

# 输出 True，因为 a 和 d 的值相等 a_2_layers = [1, 2, [3, 4]]

d_2_layers = a_2_layers.copy()

e_2_layers = copy.deepcopy(a_2_layers)

print(a_2_layers is d_2_layers)

print(a_2_layers[2] is d_2_layers[2]) # 请特别关注 print(a_2_layers is e_2_layers)

print(a_2_layers[2] is e_2_layers[2])

e f g h j k

Page 9  |  Chapter 6 Python 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 11. 身份运算

## 6.8 优先级

在 Python 中，不同类型的运算符优先级是不同的，当一个表达式中有多个运算符时，会按照优先级的顺序依次计算，可以使用括号改变运算顺序。下面是 Python 中常见的运算符优先级列表，从高到低排列： ► 括号运算符：()，用于改变运算顺序。

► 正负号运算符：+x，-x，用于对数字取正负。

► 算术运算符：**，*，/，//，%，用于数字的算术运算。

► 位运算符：~，&，|，^，<<，>>，用于二进制位的运算。

► 比较运算符：<，<=，>，>=，==，!=，用于比较大小关系。

► 身份运算符：is，is not，用于判断两个对象是否相同。

► 成员运算符：in，not in，用于判断一个元素是否属于一个集合。

► 逻辑运算符：not，and，or，用于逻辑运算。

这部分我们不再展开介绍，如果后续用到的话，请大家自行学习。

什么是位运算符？

Python 提供了一组位运算符 (bitwise operator)，用于在二进制级别对整数进行操作。这些位运算符将整数的二进制表示作为操作数，并对每个位进行逻辑运算。

请大家完成下面1 道题目。

Q1. 本章的唯一的题目就是请大家在JupyterLab 中练习本章正文给出的示例代码。

* 不提供答案。

Page 1  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Control Flow Statements in Python Python 控制结构日后尽量避免for 循环，争取用向量化绕行

幸存下来的不是最强壮的物种，也不是最聪明的物种，而是对变化最敏感的物种。

It is not the strongest of the species that survives, nor the most intelligent, but the one most responsive to change.

—— 查尔斯·达尔文 (Charles Darwin)  |  进化论之父  |  1809 ~ 1882

◄ enumerate() 用于在迭代过程中同时获取元素的索引和对应的值 ◄ for ... in ... Python 循环结构，用于迭代遍历一个可迭代对象中的元素，每次迭代时执行相应的代码块 ◄ if ... elif .. else Python 条件语句，用于根据多个条件之间的关系执行不同的代码块，如果前面的条件不满足则逐个检查后续的条件 ◄ if ... else ... Python 条件语句，用于在满足if 条件时执行一个代码块，否则执行另一个else 代码块 ◄ itertools.combinations() 用于生成指定序列中元素的所有组合，并返回一个迭代器 ◄ itertools.combinations_with_replacement() 用于生成指定序列中元素的所有带有重复元素的组合，并返回一个迭代器 ◄ itertools.permutations() 用于生成指定序列中元素的所有排列，并返回一个迭代器 ◄ itertools.product() 用于生成多个序列的笛卡尔积 (所有可能的组合)，并返回一个迭代器 ◄ try ... except ... Python 中的异常处理结构，用于尝试执行一段可能会出现异常的代码，如果发生异常则会跳转到对应的异常处理块进行处理，而不会导致程序崩溃 ◄ while ◄ zip() 用于将多个可迭代对象按对应位置的元素打包成元组的形式，并返回一个新的可迭代对象，常用于并行遍历多个序列

Page 2  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 7.1 什么是控制结构？

在 Python 中，控制结构是一种用于控制程序流程的结构，包括条件语句、循环语句和异常处理语句。这些结构可以根据不同的条件决定程序运行的路径，并根据需要重复执行代码块或捕获和处理异常情况。

这一节我们用实例全景展示这几种常见的控制结构。

条件语句条件语句在程序中用于根据不同的条件来控制执行不同的代码块。Python 中最常用的条件语句是 if 语句，if 语句后面跟一个布尔表达式，如果布尔表达式为真，就执行 if 语句块中的代码，否则执行 else 语句块中的代码。还有 elif 语句可以用来处理多种情况。

图 1 是一个简单例子，如果成绩大于等于 60 分，输出 "及格"，否则输出 "不及格"。图 1 中代码对应的流程图 (flowchart) 如图 2 所示。

注意，代码中用到了本书第4 章讲的“四空格”缩进，还用到了上一章讲过的 >= 判断运算，忘记的话请回顾。此外，大家在JupyterLab 练习图 1 给出代码时，注意字符串要用半角引号。

b score = 95 if score >= 60: print("及格")

else: print("不及格")

4 spaces 4 spaces if block else block a

图 1. 用if 判断是否成绩及格

Start Condition if score >= 60: if block else block End Fals e True

图 2. 用if 判断是否成绩及格，流程图

循环语句

Page 3  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 循环语句用于在程序中重复执行相同的代码块，直到某个条件满足为止。Python 中有两种循环语句：for 循环和 while 循环。

本书前文几次使用过for 循环，相信大家已经不再陌生。简单来说，for 循环通常用于遍历序列，例如列表或字符串。在 for 循环中，代码块会在每个元素上执行一次，直到循环结束。

请大家在JupyterLab 中自行练习图 3 代码。

b # 循环字符串内字符 str_for_loop = 'Matplotlib' for str_idx in str_for_loop: print(str_idx)

# 循环list中元素 list_for_loop = ['Matplotlib', 'NumPy', 'Seaborn', 'Pandas', 'Plotly', 'SK-learn']

for item_idx in list_for_loop: print(item_idx)

# 循环中嵌入 if 判断 packages_visual = ['Matplotlib', 'Seaborn', 'Plotly']

for item_idx in list_for_loop: print('=================')

print(item_idx)

if item_idx in packages_visual: print('A visualization tool')

# 嵌套 for 循环 for item_idx in list_for_loop: print('===============')

print(item_idx)

for item_idx in item_idx: print(item_idx)

4 spaces 4 spaces 4 spaces 4 spaces 8 spaces 8 spaces a e g f

图 3. 四个for 循环例子

while 循环会重复执行代码块，直到循环条件不再满足为止。循环条件在每次循环开始前都会被检查。

图 4 给出的例子为使用 while 循环输出 0 到 4。本书不展开介绍while 循环。

Page 4  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b i = 0 while i < 5: print(i)

i += 1 4 spaces a

图 4. while 循环例子

异常处理语句异常处理语句用于捕获和处理程序中出现的异常情况。Python 中的异常处理语句使用 try 和 except 关键字，try 语句块包含可能引发异常的代码，而 except 语句块用于处理异常情况。

图 5 是一个例子，使用 try 和 except 捕获除数为零的异常。本章不展开讲解 try … except，大家日后用到时再深入探究。

b try: x = 1 / 0 except ZeroDivisionError: print("除数不能为零")

4 spaces 4 spaces a

图 5. 用 try … except 捕捉异常

## 7.2 条件语句

打个比方，条件语句相当于开关。如图 6 (a) 所示，当只有一个 if 语句时，它的功能就像是一个单刀单掷开关 (Single Pole Single Throw, SPST)。如果条件满足，就执行分支中相应的代码。

如图 6 (b) 所示，if-else 语句相当于单刀双掷开关 (Single Pole Double Throw, SPDT)。当条件语句中分别由if 和 else 两个分支，根据条件的真假，可以有两个选项来执行不同的操作。

如图 6 (c) 所示，if-elif-else 语句相当于单刀三掷开关 (Single Pole Triple Throw, SPTT)，有三个不同选择。

(c) SPTT elif if else (a) SPST if (b) SPDT if else

图 6. 不同开关

嵌套 if 判断

Page 5  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 大家可能好奇，如果图 1 中赋值能否为用户输入？此外，如果用户输入错误是否有提示信息？我们当然可以在图 2 基础上用多层判断完成这些需求。图 7 给出的代码可以完成上述要求，对应的流程图如图 8 所示。

在这个代码中：首先，使用input() 函数获取用户输入的数值，并将其存储在value 变量中。使用 isdigit() 方法检查输入是否是一个数值。如果是数值，则执行if 语句块内的代码。将数值转换为整数类型，并存储在number 变量中。

使用嵌套的if 语句来检查number 是否在0~100 之间。如果在该范围内，则继续执行内部的if 语句块。

在内部的if 语句块中，判断number 是否小于60。如果小于60，则打印"不及格"；否则打印"及格 "。

如果输入的数值不在0 ~ 100 之间，将打印"数值不在0 ~ 100 之间"。

如果输入不是一个数值，将打印"输入不是一个数值"。

请大家判断图 7 中代码第一层if 对应的代码块是什么？

注意，上述代码假设用户输入的数值为整数。如果需要支持浮点数，请相应地调整代码。

a 4 spaces 8 spaces 12 spaces 12 spaces 4 spaces 4 spaces 3rd level: if block 3rd level: else block 2nd level: if block 2nd level: else block value = input("请输入一个数值: ")

# 第一层 if value.isdigit(): number = int(value)

# 第二层 if 0 <= number <= 100:

# 第三层 if number < 60: print("不及格")

else: print("及格")

# 第三层结束

else: print("数值不在0~100之间")

# 第二层结束

else: print("输入的不是一个数值")

# 第一层结束 1st level: else block b

图 7. 用if 判断是否成绩及格，三层判断

Page 6  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Condition Condition Condition if value.isdigit(): Start if 0 <= number <= 100: if number < 60: 3rd level if block 3rd level else block True True True False False False 2nd level else block 1st level else block End

图 8. 用if 判断是否成绩及格，三层判断，流程图

if...elif...else 语句 if...elif...else 语句用于判断多个条件，如果第一个条件成立，则执行if 语句中的代码块；如果第一个条件不成立，但第二个条件成立，则执行elif 语句中的代码块；如果前面的条件都不成立，则执行else 语句中的代码块。

注意，elif 的语句数量没有上限。但是，如果代码中elif 数量过多，需要考虑简化代码结构。

图 9 代码判断一个数是正数、负数还是0。请大家根据图 8 修改图 9 中代码。

b a num = input('输入一个整数')

num = int(num)

if num > 0: print("num is positive")

elif num < 0: print("num is negative")

else: print("num is zero")

4 spaces 4 spaces 4 spaces e

图 9. if...elif...else 语句

break、continue、pass 语句在Python 的if 条件语句、for 循环语句中，可以使用break、continue 和pass 来控制循环的行为。

break 语句可以用来跳出当前循环。当循环执行到break 语句时，程序将立即跳出循环体，继续执行循环外的语句。下面是一个使用break 的例子，该循环会在i 等于3 时跳出。

Page 7  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b a for i in range(1, 6): if i == 3: break print(i)

4 spaces 8 spaces

图 10. 使用break

continue 语句可以用来跳过当前循环中的某些语句。当循环执行到continue 语句时，程序将立即跳过本次循环，继续执行下一次循环。下面是一个使用continue 的例子，该循环会在i 等于3 时跳过本次循环。

b a for i in range(1, 6): if i == 3: continue print(i)

4 spaces 8 spaces

图 11. 使用continue

pass 语句什么也不做，它只是一个空语句占位符。在需要有语句的地方，但是暂时不想编写任何语句时，可以使用pass 语句。下面是一个使用pass 的例子，该循环中的所有元素都会被输出。

a 4 spaces for i in range(1, 6): pass print(i)

图 12. 使用pass

## 7.3 for 循环语句

本节介绍for 循环一些常见用法。

计算向量内积下例展示如何利用for 循环计算向量内积。我们用两个list 代表向量。

Page 8  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a # 计算向量内积 # 定义向量a和b a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 0]

# 初始化内积为0 dot_product = 0 # 使用for循环计算内积 for i in range(len(a)): dot_product += a[i] * b[i]

# 打印内积 print("向量内积为：", dot_product)

4 spaces b

图 13. 计算向量内积

什么是向量内积？

向量内积 (inner product)，也称为点积 (dot product)、标量积 (scalar product)，是在线性代数中常见的一种运算，它是两个向量之间的一种数学运算。

给定两个 n 维向量 a = [a1, a2, ..., an] 和 b = [b1, b2, ..., bn]，它们的内积定义为a · b = a1b1 + a2b2 + ... + anbn。这个公式的意义是将两个向量的对应分量相乘，然后将乘积相加，从而得到它们的内积。

例如，如果有两个二维向量分别为 a = [1, 2] 和 b = [3, 4]，则它们的内积为：a · b = 1 × 3 + 2 × 4 = 11。向量内积的结果是一个标量，也就是一个值，而不是向量。它可以用来计算向量之间的夹角，衡量它们的相似性，以及用于向量空间的正交分解等。

在实际应用中，向量内积被广泛用于机器学习、计算机视觉、信号处理、物理学等领域。在机器学习中，向量内积常用于计算特征之间的相似度，从而进行分类、聚类等任务。在计算机视觉中，向量内积可以用于计算两个图像之间的相似度。

range(start [, stop, step])

range() 是Python 内置的函数，用于生成一个整数序列，常用于for 循环中的计数器。参数为： ● start 是序列起始值； ● stop 是序列结束值 (不包含)； ● step 是序列中相邻两个数之间的步长 (默认为1)。

range() 函数生成的是一个可迭代对象，而不是一个列表。这样做的好处是，可以节省内存空间，尤其在需要生成很长的序列时。

下面是一些使用range() 函数的示例： a) 生成从0 到4 的整数序列 for i in range(4 + 1): print(i)

b) 生成从10 到20 的整数序列 for i in range(10, 20 + 1): print(i)

c) 生成从1 到10 的奇数序列 for i in range(1, 10 + 1, 2):

Page 9  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com print(i)

d) 生成从10 到1 的倒序整数序列 for i in range(10, 1 - 1, -1): print(i)

d) 将range() 生成的可迭代对象变成list： list(range(10, 1 - 1, -1))

请大家在JupyterLab 中自行运行如上几段段代码。

使用enumerate()

在Python 中，enumerate() 是一个用于在迭代时跟踪索引的内置函数。enumerate() 函数可以将一个可迭代对象转换为一个由索引和元素组成的枚举对象。

下面是一个简单的例子，展示了如何在for 循环中使用enumerate() 函数。

a fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits): print(index, fruit)

4 spaces

图 14. 使用enumerate()，从0 开始索引

在这个例子中，fruits 列表中的每个元素都会被遍历一遍，每次遍历都会获得该元素的值和其在列表中的索引。这些值分别被赋给index 和fruit 变量，并打印输出。

需要注意的是，enumerate 函数的默认起始索引为0，但是也可以通过传递第二个参数来指定起始索引。例如，如果想要从1 开始索引，可以使用以下代码。

a fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits,1): print(index, fruit)

4 spaces

图 15. 使用enumerate()，从1 开始索引

使用zip()

在Python 中，zip() 函数可以将多个可迭代对象的元素组合成元组，然后返回这些元组组成的迭代器。在for 循环中使用zip() 函数可以方便地同时遍历多个可迭代对象，且当这些可迭代对象的长度不同时，zip() 函数会以最短长度的可迭代对象为准进行迭代。

如果想要打印出每个学生的姓名和对应的成绩，可以使用zip() 函数和for 循环，代码如所示。

Page 10  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a 4 spaces names = ['Alice', 'Bob', 'Charlie']

scores = [80, 90, 75]

for name, score in zip(names, scores): print(name, score)

图 16. 使用zip() 同步遍历多个对象

在这个例子中，zip() 函数将names 和scores 两个列表按照位置进行组合，然后返回一个迭代器，其中的每个元素都是一个元组，元组的第一个元素为names 列表中对应位置的元素，第二个元素为scores 列表中对应位置的元素。在for 循环中使用了两个变量name 和score，分别用来接收每个元组中的两个元素，然后打印出来即可。

需要注意的是，如果可迭代对象的长度不相等，zip()函数会以最短长度的可迭代对象为准进行迭代。

计算向量内积：使用zip()

可以使用 Python 的内置函数 zip() 和运算符 *，对两个向量中的对应元素逐一相乘并相加，实现向量内积运算。以下为示例代码，请大家对比图 13。

a 4 spaces # 计算向量内积 # 定义向量a和b a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 0]

# 初始化内积为0 dot_product = 0 # 使用for循环计算内积 for a_i, b_i in zip(a, b): dot_product += (a_i * b_i)

# 打印内积 print("向量内积为：", dot_product)

图 17. 使用zip() 计算向量内积

在此示例中，通过 zip() 函数将两个list，a 和 b，中对应位置的元素组合成了元组，然后使用 for 循环逐个遍历并相乘求和，最终得到了向量内积的结果。

矩阵乘法：三层for 循环下面介绍如何使用嵌套for 循环完成矩阵乘法。

图 18 所示为两个2 × 2 矩阵相乘如何得到矩阵C 的每一个元素。

Page 11  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 矩阵A 的第一行元素和矩阵B 第一列对应元素分别相乘，再相加，结果为矩阵C 的第一行、第一列元素c1,1。

矩阵A 的第一行元素和矩阵B 第二列对应元素分别相乘，再相加，得到c1,2。

同理，依次获得矩阵C 的c2,1和c2,2两个元素。

@ = @ 1×4 + 2×3 = 10 @ 1×2 + 2×1 = 4 @ 3×4 + 4×3 = 24 @ 3×2 + 4×1 = 10 = = = = A B C c1,1 c1,2 c2,1 c2,2 a1 a1 a2 a2 a(1)

a(2)

a(1)

a(2)

图 18. 矩阵乘法规则，两个2 × 2 矩阵相乘为例

什么是矩阵乘法？

矩阵乘法 (matrix multiplication) 是一种线性代数运算，用于将两个矩阵相乘。对于两个矩阵A 和B，它们的乘积AB 的元素是通过将A 的每一行与B 的每一列进行内积运算得到的。

具体而言，假设A 是一个m×n 的矩阵，B 是一个n×p 的矩阵，则它们的乘积C = AB 是一个m×p 的矩阵，其中第i 行第j 列的元素ci,j为A 的第i 行与B 的第j 列的内积。如果A 的第i 行元素为ai,1, ai,2, ..., ai,n，B 的第j 列元素为b1,j, b2,j, ..., bn,j，则C = AB 的第i 行第j 列的元素为ai,1b1,j + ai,2b2,j + ... + ai,nbn,j。

矩阵乘法在许多领域都有广泛的应用，例如线性代数、信号处理、图形学和机器学习等。在机器学习中，矩阵乘法通常用于计算神经网络的前向传播过程，其中输入矩阵与权重矩阵相乘，得到隐藏层的输出矩阵。

Page 12  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com First layer of for loop Second layer of for loop Third layer of for loop A B b(1)

b(2)

b(j)

ai a1 a2 a3 ci,j c1,1 c1,2 c2,1 c3,1 c3,2 c2,2

图 19. 矩阵乘法规则，三层for 循环

Page 13  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 定义矩阵 A 和 B A = [[1, 2, 10, 20], [3, 4, 30, 40], [5, 6, 50, 60]]

B = [[4, 2], [3, 1], [40, 20], [30, 10]]

# 定义全 0 矩阵 C 用来存放结果 C = [[0, 0], [0, 0], [0, 0]]

# 矩阵乘法 # 遍历 A 的行 for i in range(len(A)): # len(A) 给出 A 的行数

# 遍历 B 的列 for j in range(len(B[0])): # len(B[0]) 给出 B 的列数

# 这一层相当于消去 k 所在的维度，即压缩 for k in range(len(B)): C[i][j] += A[i][k] * B[k][j]

# 完成对应元素相乘，再求和 # 输出结果 for row in C: print(row)

4 spaces 8 spaces 12 spaces b a

图 20. 使用嵌套for 循环计算矩阵乘法

向量化向量化运算是使用NumPy 等库的一种高效运算处理方式，可以避免使用for 循环。图 21、图 22 所示为利用NumPy 完成向量内积、矩阵乘法运算。

但这不意味着前文自己写代码计算向量内积、矩阵乘法是无用功！在前文的代码练习中，一方面我们掌握如何使用for 循环，此外理解了向量内积、矩阵乘法两种数学工具的运算规则。

Page 14  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np # 定义向量a和b；准确来说是一维数组 a = np.array([1, 2, 3, 4, 5])

b = np.array([6, 7, 8, 9, 0])

# 计算向量内积 dot_product = np.dot(a,b)

# 打印内积 print("向量内积为：", dot_product)

图 21. 使用numpy.dot() 计算向量内积

import numpy as np # 定义矩阵 A 和 B A = np.array([[1, 2, 10, 20], [3, 4, 30, 40]])

B = np.array([[1, 3], [2, 4], [10, 30], [20, 40]])

C = A @ B; print(C)

D = B @ A; print(D)

a b A B @ = C = D A B @

图 22. 使用NumPy 计算矩阵乘法

## 7.4 列表生成式

在Python 中，列表生成式 (list comprehension) 是一种简洁的语法形式，用于快速生成新的列表。

它的语法形式为 [expression for item in iterable if condition]，其中expression 表示要生成的元素，item 表示迭代的变量，iterable 表示迭代的对象，if condition 表示可选的过滤条件。

举个例子，假设我们想要生成一个包含1 到10 之间所有偶数的列表，我们可以使用如下列表生成式。

a even_numbers = [num for num in range(1, 11)

if num % 2 == 0] # 一行放不下 print(even_numbers) # Output: [2, 4, 6, 8, 10]

图 23. 使用列表生成式，获得1 ~ 10 之间所有偶数列表

Page 15  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 在上述代码中，我们使用列表生成式创建了一个包含1 到10 之间所有偶数的列表。具体来说，我们使用range(1, 11)迭代1 到10 的数字，对每个数字进行取模操作，只保留余数为0 的数字，即偶数， 最终将这些数字存储到一个新的列表中。

使用列表生成式还可以嵌套，比如下例。

a matrix = [[i * j for j in range(1, 4)]

for i in range(1, 4)]

print(matrix)

# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

图 24. 嵌套生成式列表

在上述代码中，我们使用嵌套的列表生成式创建了一个3 × 3 的矩阵。具体来说，我们使用外部的列表生成式迭代1 到3 的数字，对每个数字使用内部的列表生成式迭代1 到3 的数字，计算它们的乘积并将结果存储到一个新的二维列表中。请大家用上述代码生成图 20 中全0 矩阵C。

使用列表生成式可以大大简化代码，提高代码的可读性和可维护性。

矩阵转置：一层列表生成式如下代码展示如何用一层列表生成式转置矩阵。

def transpose(matrix): transposed = []

rows = len(matrix)

cols = len(matrix[0])

for j in range(cols): transposed_row = [matrix[i][j]

for i in range(rows)]

transposed.append(transposed_row)

return transposed # 示例用法 A = [[1, 2, 3], [4, 5, 6]]

# 调用自定义函数 B = transpose(A)

b a

图 25. 利用一层列表生成式完成矩阵转置

矩阵转置：两层列表生成式如下代码展示如何用两层列表生成式转置矩阵。

Page 16  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com def transpose_2(matrix): transposed = []

rows = len(matrix)

cols = len(matrix[0])

transposed = [[(matrix[j][i])

for j in range(rows)]

for i in range(cols)]

return transposed # 示例用法 A = [[1, 2, 3], [4, 5, 6]]

# 调用自定义函数 B = transpose_2(A)

a

图 26. 利用两层列表生成式完成矩阵转置

计算矩阵逐项积：两层列表生成式矩阵逐项积是指两个相同矩阵中相应位置上的元素进行逐一相乘，得到一个新的矩阵。

def hadamard_prod(M1, M2): if (len(M1) != len(M2) or len(M1[0]) != len(M2[0])): raise ValueError("Matrices must have the same shape")

result = [[M1[i][j] * M2[i][j]

for j in range(len(M1[0]))]

for i in range(len(M1))]

return result A = [[1, 2], [3, 4]]

B = [[2, 3], [4, 5]]

# 计算矩阵逐项积 C = hadamard_prod(A, B)

a

图 27. 利用两层列表计算矩阵逐项积

笛卡儿积这个3 × 3 的矩阵本质上是个笛卡儿积 (Cartesian product)。

数学上，如果集合A 中有a 个元素，集合B 中有b 个元素，那么A 和B 的笛卡儿积就有a × b 个元素。举个简单的例子，假设有两个集合：A = {1, 2} 和 B = {'a', 'b'}。

它们的笛卡尔积为 {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}。

图 19 中给出的矩阵乘法原理也可以看成是笛卡儿积。

Page 17  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 28. 笛卡儿积

column1 = [1, 2, 3, 4]

column2 = ['a', 'b', 'c']

cartesian_product = [(x, y) for x in column1 for y in column2]

print(cartesian_product)

a b

图 29. 笛卡儿积，列表，采用列表生成式

column1 = [1, 2, 3, 4]

column2 = ['a', 'b', 'c']

cartesian_product = [[(x, y) for x in column1] for y in column2]

for prod_idx in cartesian_product: print(prod_idx)

a

图 30. 笛卡儿积，嵌套列表，采用列表生成式

[[(1, 'a'), (2, 'a'), (3, 'a'), (4, 'a')]

[(1, 'b'), (2, 'b'), (3, 'b'), (4, 'b')]

[(1, 'c'), (2, 'c'), (3, 'c'), (4, 'c')]]

(1, 'a')  (2, 'a')  (3, 'a')  (4, 'a')

(1, 'b')  (2, 'b')  (3, 'b')  (4, 'b')

(1, 'c')  (2, 'c')  (3, 'c'), (4  'c')

'a' 'b' 'c'

图 31. 嵌套列表

Page 18  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from itertools import product column1 = [1, 2, 3, 4]

column2 = ['a', 'b', 'c']

cartesian_product = list(product(column1, column2))

print(cartesian_product)

a b

图 32. 笛卡儿积，列表，采用itertools.product 生成，采用列表生成式

## 7.5 迭代器

itertools 是Python 标准库中的一个模块，提供了用于创建和操作迭代器的函数。迭代器是一种用于遍历数据集合的对象，它能够逐个返回数据元素，而无需提前将整个数据集加载到内存中。

itertools 模块包含了一系列用于高效处理迭代器的工具函数，这些函数可以帮助我们在处理数据集时节省内存和提高效率。它提供了诸如组合、排列、重复元素等功能，以及其他有关迭代器操作的函数。

不放回排列 itertools.permutations 是Python 标准库中的一个函数，用于返回指定长度的所有可能排列方式。下面举例如何使用itertools.permutations 函数。

假设有一个字符串string = 'abc'，我们想要获取它的所有字符排列方式，可以按照以下步骤操作。

a b import itertools string = 'abc' perms_all = itertools.permutations(string)

# 返回一个可迭代对象perms，其中包含了string的所有排列方式 # 全排列 for perm_idx in perms_all: print(''.join(perm_idx))

e

图 33. 3 个字符全排列

这就好比，一个袋子里有三个球，它们分别印有a、b、c，先后将所有球取出排成一排共有6 种排列，具体如图 34 所示。

a b b a a b a b b a a b b a 图 34. 3 个元素无放回抽取3 个，结果有6 个排列

Page 19  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

itertools.permutations 函数还有一个可选参数r，用于指定返回的排列长度。如果不指定r，则默认返回与输入序列长度相同的排列。例如，我们可以通过以下方式获取string 的所有长度为2 的排列。

a import itertools string = 'abc' # 3个不放回取2个的排列 perms_2 = itertools.permutations(string, 2)

# 返回一个包含所有长度为2的排列的可迭代对象perms for perm_idx in perms_2: print(''.join(perm_idx))

图 35. 3 个字符无放回取2 个排列

还是以前文小球为例，如图 36 所示，3 个元素无放回抽取2 个，结果有6 个排列。大家可能已经发现这个结果和一致。这也不难理解，袋子里一共有3 个球，无放回拿出两个之后，第三个球是什么字母已经确定，没有任何悬念。

a b b a a a b b a b

图 36. 3 个元素无放回抽取2 个，结果有6 个排列

不放回组合 itertools.combinations 是Python 中的一个模块，它提供了一种用于生成组合的函数。

使用itertools.combinations 函数，需要导入itertools 模块，然后调用combinations 函数，传入两个参数：一个可迭代对象和一个整数，表示要选择的元素个数。该函数会返回一个迭代器，通过迭代器你可以获得所有可能的组合。

a import itertools string = 'abc' # 3个取2个的组合 combs_2 = itertools.combinations(string, 2)

# 返回一个包含所有长度为2的组合的可迭代对象combs_2 for combo_idx in combs_2: print(''.join(combo_idx))

图 37. 3 个字符无放回取2 个组合

Page 20  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

a b a b a b

图 38. 3 个元素无放回抽取2 个，结果有3 个组合

什么是排列？什么是组合？

排列是指从一组元素中按照一定顺序选择若干个元素形成的不同序列，每个元素只能选取一次。

组合是指从一组元素中无序地选择若干个元素形成的不同集合，每个元素只能选取一次。

有放回排列前文介绍的排列、组合都是无放回抽样，下面聊聊有放回抽样。还是以小球为例，如图 39 所示，有放回抽样就是从口袋中摸出一个球之后，记录字母，然后将小球再放回口袋。下一次抽取时，这个球还有被抽到的机会。

什么是有放回？什么是无放回？

有放回抽取是指在进行抽样时，每次抽取后将被选中的元素放回原始集合中，使得下一次抽取时仍然有可能选中同一个元素。无放回抽取是指在进行抽样时，每次抽取后将被选中的元素从原始集合中移除，使得下一次抽取时不会再选中相同的元素。简而言之，有放回抽取可以多次选中相同元素，而无放回抽取每次选中后都会从集合中移除，确保不会重复选中同一元素。

a b

图 39. 有放回抽样 itertools 模块中的itertools.product 函数可以用于生成有放回排列。它接受一个可迭代对象和一个重复参数，用于指定每个元素可以重复出现的次数。

Page 21  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a import itertools string = 'abc' # 定义元素列表 elements = list(string)

# 指定重复次数 repeat = 2 # 生成有放回排列 permutations = itertools.product(elements, repeat=repeat)

# 遍历并打印所有排列 for permutation_idx in permutations: print(''.join(permutation_idx))

b

图 40. 3 个字符有放回取2 个排列

a b a b b a a b b b a a b a

图 41. 3 个元素有放回抽取2 个，结果有9 个排列

有放回组合 itertools 模块中的itertools.combinations_with_replacement 函数可以用于生成有放回组合。该函数接受一个可迭代对象和一个整数参数，用于指定从可迭代对象中选择元素的个数。

a import itertools string = 'abc' # 定义元素列表 elements = list(string)

# 指定组合长度 length = 2 # 生成有放回组合 combos = itertools.combinations_with_replacement(elements, length)

# 遍历并打印所有组合 for combination_idx in combos: print(''.join(combination_idx))

图 42. 3 个字符有放回取2 个的组合

Page 22  |  Chapter 7 Python 控制结构  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b a a b b a b a b

图 43. 3 个元素有放回抽取2 个，结果有6 个组合

除了练习本章给出的代码示例之外，请大家完成下面几道题目。

Q1. 给定一个整数列表 [3, 5, 2, 7, 1]，找到其中的最大值和最小值，并打印两者之和。

Q2. 使用 while 循环输出 1 到 10 的所有奇数。

Q3. 输入一个数字并将其转换为整数，如果输入的不是数字，则提示用户重新输入直到输入数字为止。

Q4. 求100 以内的素数。

Q5. 请用至少两种不同办法计算1-100 中奇数之和。

Q6. 写两个函数分别计算矩阵行、列方向元素之和。

Q7. 写两个函数分别计算矩阵行、列方向元素平均值。

* 题目答案在Bk1_Ch07_01.ipynb。

Page 1  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Functions in Python Python 函数内置函数、自定义函数、Lambda 函数 …

很多人在二十五岁便垂垂老矣，直到七十五岁才入土为安。

Many people die at twenty five and aren't buried until they are seventy five.

—— 本杰明·富兰克林 (Benjamin Franklin)  |  美国政治家  |  1706 ~ 1790

◄ numpy.linalg.det 计算一个方阵的行列式 ◄ numpy.linalg.inv 计算一个方阵的逆矩阵 ◄ numpy.linalg.eig 计算一个方阵的特征值和特征向量 ◄ numpy.linalg.svd 计算一个矩阵的奇异值分解 ◄ numpy.random.rand 生成0~1 之间均匀分布的随机数 ◄ numpy.random.randn 生成符合标准正态分布的随机数 ◄ numpy.random.randint 生成指定范围内的整数随机数 ◄ def ... (return ...) Python 中用于定义函数的关键字，其中def 用于定义函数名称和参数列表，return 用于指定函数返回的结果，可以没有函数返回 ◄ matplotlib.pyplot.grid() 在当前图表中添加网格线 ◄ matplotlib.pyplot.plot() 绘制折线图 ◄ matplotlib.pyplot.subplots() 创建一个包含多个子图的图表，返回一个包含图表对象和子图对象的元组 ◄ matplotlib.pyplot.title() 设置当前图表的标题 ◄ matplotlib.pyplot.xlabel() 设置当前图表x 轴的标签 ◄ matplotlib.pyplot.xlim() 设置当前图表x 轴显示范围 ◄ matplotlib.pyplot.xticks() 设置当前图表x 轴刻度位置 ◄ matplotlib.pyplot.ylabel() 设置当前图表y 轴的标签 ◄ matplotlib.pyplot.ylim() 设置当前图表y 轴显示范围 ◄ matplotlib.pyplot.yticks() 设置当前图表y 轴刻度位置 ◄ numpy.linspace() 用于在指定的范围内创建等间隔的一维数组，可以指定数组的长度 ◄ numpy.sin() 用于计算给定弧度数组中每个元素的正弦值 ◄ lambda 创建匿名函数 (没有函数名) 的关键字，通常用于简单的函数定义或作为函数的参数传递 ◄ map() 内置函数，用于对一个可迭代对象中的每个元素应用指定的函数，并返回一个新的可迭代对象

Page 2  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 8.1 什么是Python 函数?

这本书学到这里，相信大家对函数这个概念已经不陌生。简单来说，在Python 中，函数是一段可重复使用的代码块，用于执行特定任务或完成特定操作。函数可以接受输入参数，并且可以返回具体值、 或者不返回任何值作为结果。

比如，大家已经非常熟悉的 print()，这个函数的输入参数是要打印的字符串，在完成打印之后，这个函数并没有任何的输出值。

再举个几例子，很多函数都返回具体值，比如len() 返回list 元素个数，range() 生成一个可以用在 for 循环的整数序列，list() 可以创建列表或将其他对转化为列表。

再者，很多数值操作、科学计算的函数都打包在NumPy、SciPy 这样的库中，比如大家已经见过的 numpy.array() 等等。

通过使用函数，可以将代码分解成小块，每个块都完成一个特定的任务。这使得代码更易于理解、 测试和维护。同时，函数也可以在不同的上下文中重复使用，提高代码的重用性和可维护性。

代数角度，什么是函数？

从代数角度来看，函数是一种数学概念，描述了输入和输出之间的关系。它将一个集合中的每个元素映射到另一个集合中的唯一元素。函数用公式、图表或描述性语言定义，具有定义域和值域的概念。函数在数学中被用于解决问题、建模现实世界，并具有单值性、唯一性等特性。代数中的函数描述了数学方程、曲线和变换，并帮助我们理解数学关系及其应用。

几种函数类型在Python 中，有以下几种函数类型： ► 内置函数：Python 解释器提供的函数，例如print()、len()、range()等。

► 自定义函数：由用户定义的函数。

► Lambda 函数：也称为匿名函数，是一种简单的函数形式，可以通过lambda 关键字定义。

► 生成器函数：是一种特殊的函数，用于生成一个迭代器，可以使用yield 关键字定义。本章不展开介绍生成器函数。

► 方法：是与对象相关联的函数，可以使用"."符号调用。例如字符串类型的方法，可以使用字符串变量名.方法名()的形式调用。大家会在Pandas 中经常看到这种用法。

为什么需要自定义函数？

既然NumPy、SciPy、SymPy 等等库中提供大量可重复利用的函数，为什么还要兴师动众“自定义函数”？

这个答案其实很简单。现成的函数面向一般需求，不能满足大家的各种“私人订制”需求。

此外，自定义函数在Python 中的作用是提高代码复用性、模块化和组织性，抽象和封装复杂问题， 使代码结构和逻辑更清晰，增加可扩展性和灵活性。通过封装可重复使用的代码块为函数，避免重复编写相同的代码，并将大型任务分解为小型函数，使程序更易理解和维护。自定义函数提高代码的可读性、可维护性，并支持程序扩展和修改，使代码更结构化和可管理。

Page 3  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 包、模块、函数在 Python 中，一个包 (package) 是一组相关模块 (module) 的集合，一个模块是包含 Python 定义和语句的文件。而一个函数则是在模块或者在包中定义的可重用代码块，用于执行特定任务或计算特定值。

通常情况下，一个模块通常是一个.py 文件，包含了多个函数和类等定义。一个包则是一个包含了多个模块的目录，通常还包括一个特殊的__init__.py 文件，用于初始化该包。

在使用时，需要使用import 关键字导入模块或者包，从而可以使用其中定义的函数和类等。而函数则是模块或包中定义的一段可重用的代码块，用于完成特定的功能。

因此，包中可以包含多个模块，模块中可以包含多个函数，而函数是模块和包中的可重用代码块。

以NumPy 为例，NumPy 是Python 中用于科学计算的一个库，其包含了很多有用的数值计算函数和数据结构。下面是NumPy 库中常见的模块和函数的介绍： numpy.linalg 这个模块提供了一些线性代数相关的函数，包括矩阵分解、行列式计算、特征值和特征向量计算等。常见的函数有： ► numpy.linalg.det：计算一个方阵的行列式。

► numpy.linalg.inv：计算一个方阵的逆矩阵。

► numpy.linalg.eig：计算一个方阵的特征值和特征向量。

► numpy.linalg.svd：计算一个矩阵的奇异值分解。

numpy.random 这个模块提供了随机数生成的函数，包括生成服从不同分布的随机数。常见的函数有： ► numpy.random.rand：生成0~1 之间均匀分布的随机数。

► numpy.random.randn：生成符合标准正态分布的随机数。

► numpy.random.randint：生成指定范围内的整数随机数。

数学函数在代数中，函数是一种数学关系，它将一个或多个输入值映射 (mapping) 到唯一的输出值。函数可以用一个规则或方程式来表示，其中输入值称为自变量，输出值称为因变量。

从代数角度来看，函数是一种数学对象，用于描述两个集合之间的关系。一个函数将一个集合中的每个元素 (称为输入) 映射到另一个集合中的唯一元素 (称为输出)。

数学上，函数的定义包括以下要素： ► 定义域 (domain)：定义域是输入变量可能的取值范围。它是函数的输入集合。

► 值域 (range)：值域是函数的输出可能的取值范围。它是函数的输出集合。

► 规则 (rule)：规则定义了输入和输出之间的映射关系。它描述了如何根据给定的输入计算输出。

如图 1 所示，函数也可以有不止一个输入，比如二元函数 f(x1, x2) 便有2 个输入。

函数可以用各种方式定义，包括通过公式、算法、图表或描述性语言。它可以是连续的、离散的或混合的，具体取决于输入和输出的集合的性质。

Page 4  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Function f(x)

Input x Output f(x)

Function f(x1, x2)

Inputs x1, x2 Output f(x1, x2)

图 1. 一元函数、二元函数的映射

函数描述了不同变量之间的依赖关系，并且可以用来表示数学问题的模型。函数可以通过数学符号、图表或文字描述来表示，它们在代数中广泛应用于方程求解、图形绘制和数值计算等领域。

一句话概括来说，函数就是映射，输入值映射到唯一的输出值。如图 2 所示，我们设计了两个函数：左侧函数Shape() 输入为彩色几何图形，函数输出为图形形状；右侧函数Color() 输入还是彩色几何形状，函数输出为图形颜色。

Color()

Shape()

图 2. 识别颜色、形状的函数

单射、满射单射、非单射、满射和非满射是函数映射中的性质，描述了输入值和输出值之间的关系。

单射 (injective) 是指函数中不同的输入值对应着不同的输出值，即每个输出值只有一个对应的输入值。

非单射 (non-injective) 是指函数中存在多个不同的输入值对应着相同的输出值，即至少有一个输出值有多个对应的输入值。

Page 5  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 满射 (surjective) 是指函数的所有可能的输出值都能够被映射到，即每个输出值都有至少一个对应的输入值。

非满射 (non-surjective) 是指函数中存在至少一个输出值无法被映射到，即存在某些输出值没有对应的输入值。

图 3 所示为单射、非单射、满射、非满射构成的“四象限”。单射、非单射更关注输入值，而满射、 非满射则关注输出值。同时满足单射与满射叫双射 (bijective)，也叫一一映射。

Surjective Non-surjective Injective Non-injective

图 3. 单射、非单射、满射、非满射构成的四象限

Page 6  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Surjective Non-surjective Injective Non-injective

图 4. 单射、非单射、满射、非满射构成的四象限，具体实例

一元、二元、三元、多元在数学中，函数的元 (arity) 指的是函数接受的参数个数。

常见的函数元数包括： 一元函数 (unary function) 接受一个参数。例如，f1(x) = x 是一个一元函数，它接受一个参数 x。

二元函数 (binary function) 接受两个参数。例如，f2(x1, x2) = x1 + x2 是一个二元函数，它接受两个参数 x1 和 x2。

三元函数 (ternary function) 接受三个参数。例如，f3(x1, x2, x3) = x1 + x2 + x3是一个三元函数，它接受三个参数 x1、x2 和 x3。

多元函数 (n-ary function) 接受 n 个参数。多元函数的参数个数可以是任意多个，例如fn(x1, x2, …, xn)

= x1 + x2 + … + xn是一个多元函数，它接受任意n 个参数 x1、x2、...、xn。

数学函数 vs 编程函数代数角度的函数概念与计算机编程中的函数概念有些相似，但也有一些不同之处。在代数中，函数是描述输入和输出之间关系的抽象概念，而在编程中，函数是可执行的代码块，用于执行特定的任务。

然而，两者之间的基本思想都是处理输入并生成输出。

Page 7  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 数学上的函数和编程上的函数在概念和应用上存在一些异同之处。

无论是数学上的函数，还是编程上的函数，它们都涉及输入和输出。数学函数接受输入值并产生相应的输出值，而编程函数接受参数但是未必返回结果。

数学上的函数和编程上的函数都有一个定义域和一个规则，描述了如何将输入转换为输出。无论是通过公式、算法还是逻辑操作，函数都定义了输入和输出之间的关系。

无论是数学上的函数，还是编程上的函数的概念都具有可重用性。无论是在数学中还是在编程中， 函数可以在多个场景中被多次调用和使用，避免了重复编写相同的代码。

数学上的函数和编程上的函数显然也有很大区别。数学函数通常用符号、公式或描述性语言来表示，如 f(x) = x2。而编程函数则以编程语言的语法和结构来定义和表示，如 def square(x): return x**2。编程函数可以包含额外的程序控制结构，如条件语句、循环等，以实现更复杂的逻辑和操作。

总体而言，数学上的函数更关注描述数学关系，而编程上的函数更侧重于实现特定的计算或操作。

虽然两者有相似的概念，但具体的表示方式、范围和应用场景可能会有所不同。

## 8.2 自定义函数

无输入、无返回在 Python 中，我们可以自定义函数来完成一些特定的任务。函数通常接受输入参数并返回输出结果。但有时我们需要定义一个函数，它既没有输入参数，也不返回任何结果。这种函数被称为没有输入、没有返回值的函数。

定义这种函数的方法和定义其他函数类似，只是在定义函数时省略了输入参数和 return 语句。比如下例，这个函数名为 say_hello，它不接受任何输入参数，执行函数体中的代码时会输出字符串 "Hello!"。

b a Function block 4 spaces def say_hello(): # 自定义函数：打印问候 # 输入：无 # 输出：无 print("Hello!")

# 调用自定义函数 say_hello()

图 5. 无输入、无输出函数下面，我们再看一个复杂的例子。这个例子，我们也定义了一个无输入、无输出函数用来美化线图。图 6 所示为利用Matplotlib 绘制的一元一次函数、一元二次函数线图美化之后的结果。

本书第10 章将专门介绍如何绘制线图，此外鸢尾花书《可视之美》将专门介绍Python 可视化专题。

Page 8  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a)

(b)

f(x)

f(x)

图 6. 绘制线图并美化 a Function block # 导入包 import matplotlib.pyplot as plt # 导入 Matplotlib 库中的 pyplot 模块，并将其命名为 plt import numpy as np # 导入 NumPy 库，并将其命名为 np # 自定义函数 def beautify_line_chart(): # 添加标签 plt.xlabel("x")

plt.ylabel("f(x)")

# 设置坐标轴范围 plt.xlim(-2, 2)

plt.ylim(-2, 2)

# 设置横纵轴刻度 plt.xticks([-2,-1,0,1,2])

plt.yticks([-2,-1,0,1,2])

# 添加网格线 plt.grid(True)

# 横纵轴统一标尺 plt.gca().set_aspect('equal', adjustable='box')

# 显示图形 plt.show()

x_array = np.linspace(-2,2,101)

# 使用NumPy的linspace函数创建一个包含101个元素的数组 # 这些元素均匀地分布在区间[-2, 2]上，左闭右闭 # 绘制直线 fig, ax = plt.subplots(figsize = (4,4))

# plt.subplots()返回值解包为两个变量：fig 和 ax # fig图形窗口对象，可以用于设置图形窗口的属性 # ax 是坐标轴对象，用于绘制具体的图形和设置坐标轴的属性 # figsize=(4, 4) 表示图形窗口的宽度为4英寸，高度为4英寸 y_array = x_array # 一次函数 y = x plt.plot(x_array, y_array)

beautify_line_chart() # 调用自定义函数绘制美化的线图 # 绘制抛物线 fig, ax = plt.subplots(figsize = (4,4))

y_array = x_array**2 - 2 # 二次函数 plt.plot(x_array, y_array)

beautify_line_chart() # 调用自定义函数绘制美化的线图 4 spaces b e f g h j k o n

Page 9  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 7. 无输入、无输出函数，装饰线图

多个输入、单一返回一个函数可以有多个输入参数，一个或多个返回值。下面是一个示例函数，它有两个输入参数a 和 b，返回它们的和。

b a Function block 4 spaces # 自定义函数 def add_numbers(a, b): result = a + b return result sum = add_numbers(3, 5) # 调用函数 print(sum)  # 输出8

图 8. 两个输入、一个输出函数

下面这个例子中，我们定义了一个名为arithmetic_operations()的函数，它有两个参数a 和b。在函数体内，我们进行了四个基本的算术运算，并将其结果存储在四个变量中。最后，我们使用return 语句返回这四个变量。当我们调用这个函数时，我们将a 和b 的值作为参数传递给函数，函数将返回四个值。

我们将这四个返回值存储在一个元组result 中，并使用索引访问和打印这四个值。

b a Function block 4 spaces # 自定义函数 def arithmetic_operations(a, b): add = a + b sub = a - b mul = a * b div = a / b return add, sub, mul, div # 调用函数并输出结果 a, b = 10, 5 result = arithmetic_operations(a, b)

print("Addition: ", result[0])

print("Subtraction: ", result[1])

print("Multiplication: ", result[2])

print("Division: ", result[3])

图 9. 两个输入、多个输出函数

部分输入有默认值在Python 中，我们可以为自定义函数中的某些参数设置默认值，这样在调用函数时，如果不指定这些参数的值，就会使用默认值。这种设置默认值的参数称为默认参数。

Page 10  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 下面是一个例子，展示如何在自定义函数中设置默认参数。greet()函数有两个参数：name 和 greeting。name 是必需的参数，没有默认值。而greeting 是可选的，默认值为'Hello'。

当我们调用greet()函数时，如果只传入了name 参数，那么greeting 就会使用默认值'Hello'。如果需要自定义问候语，可以在调用时传入自定义的值，如上面的第二个调用例子所示。

需要注意的是，默认参数必须放在非默认参数的后面。在函数定义中，先定义的参数必须先被传入，后定义的参数后被传入。如果违反了这个顺序，Python 解释器就会抛出SyntaxError 异常。

b a Function block 4 spaces # 自定义函数 def greet(name, greeting='Hello'): print(f"{greeting}, {name}!")

# 使用默认的问候语调用函数 greet('James')  # 输出 "Hello, James!"

# 指定自定义的问候语调用函数 greet('James', 'Good morning')

# 输出 "Good morning, James!"

图 10. 函数输入有默认值

将矩阵乘法打包成一个函数上一章中，我们自定义了计算矩阵乘法代码。为了方便“多次调取”，下面我们将这段代码写成一个自定义函数。改良版的自定义函数，根据输入函数的形状，自行判断矩阵乘法结果矩阵的形状。

Page 11  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b a # 自定义函数 def matrix_multiplication(A,B): # 定义全 0 矩阵 C 用来存放结果 C = [[0] * len(B[0]) for i in range(len(A))]

# 遍历 A 的行 for i in range(len(A)): # len(A) 给出 A 的行数 # 遍历 B 的列 for j in range(len(B[0])): # len(B[0]) 给出 B 的列数 # 这一层相当于消去 k 所在的维度，即压缩 for k in range(len(B)): C[i][j] += A[i][k] * B[k][j]

# 完成对应元素相乘，再求和

return C

# 定义矩阵 A 和 B A = [[1], [2], [3]]

B = [[1, 2, 3]]

print('A @ B = ')

C = matrix_multiplication(A,B) # 调用自定义函数 for row in C: print(row)

print('B @ A = ')

D = matrix_multiplication(B,A) # 调用自定义函数 for row in D: print(row)

e f g h = C B A @ = D B A @

图 11. 将矩阵乘法打包成一个函数

大家可能会问怎么在自定义函数内添加一个判断语句来检查两个矩阵的尺寸是否匹配。如果不匹配，就抛出一个异常并提示错误信息。

以下是修改后的代码示例。

在函数中，我们使用 len(A[0]) 和 len(B) 来检查第一个矩阵的列数是否等于第二个矩阵的行数。如果不相等，我们就使用 raise 语句抛出一个 ValueError 异常，并输出错误信息。这样，在调用函数时，如果输入的两个矩阵无法相乘，就会得到一个错误提示。

Page 12  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b a # 自定义函数 def matrix_multiplication(A,B):

# 检查两个矩阵形状是否匹配 if len(A[0]) != len(B): raise ValueError("Error: check matrix sizes")

else: # 定义全 0 矩阵 C 用来存放结果 C = [[0] * len(B[0]) for i in range(len(A))]

# 遍历 A 的行 for i in range(len(A)): # len(A) 给出 A 的行数 # 遍历 B 的列 for j in range(len(B[0])): # len(B[0]) 给出 B 的列数 # 这一层相当于消去 p 所在的维度，即压缩 for k in range(len(B)): C[i][j] += A[i][k] * B[k][j]

# 完成对应元素相乘，再求和 return C

# 定义矩阵 A 和 B A = [[1], [2], [3], [4]]

B = [[1, 2, 3]]

print('A @ B = ')

C = matrix_multiplication(A,B) # 调用自定义函数 for row in C: print(row)

print('B @ A = ')

D = matrix_multiplication(B,A) # 会报错

图 12. 将矩阵乘法打包成一个函数，增加矩阵形状不匹配的报错信息

帮助文档在 Python 中，可以使用 docstring 来编写函数的帮助文档，即在函数定义的第一行或第二行写入字符串来描述函数的作用、参数、返回值等信息。通常使用三个单引号（'''）或三个双引号（"""）来表示 docstring，如下所示。如果要查询这个文档，可以使用 Python 内置的 help() 函数或者 __doc__ 属性来查看。

Page 13  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a # 计算向量内积 def inner_prod(a,b):

''' 自定义函数计算两个向量内积输入： a：向量，类型为数据列表 b：向量，类型为数据列表输出： c：标量参考： https://mathworld.wolfram.com/InnerProduct.html ''' # 检查两个向量元素数量是否相同 if len(a) != len(b): raise ValueError("Error: check a/b lengths")

# 初始化内积为0 dot_product = 0 # 使用for循环计算内积 for i in range(len(a)): dot_product += a[i] * b[i]

return dot_product # 查询自定义函数文档，两种办法 help(inner_prod)

print(inner_prod.__doc__)

# 定义向量a和b a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = a[::-1]

# 调用函数 c = inner_prod(a,b)

# 打印内积 print("向量内积为：", c)

b

图 13. 自定义函数中的帮助文档

## 8.3 更多自定义线性代数函数

产生全0 矩阵：一层for 循环下面举例如何用一层for 循环产生全0 矩阵。本书后文会介绍如何利用numpy.zeros() 和 numpy.zeros_like() 生成全0 矩阵。

下一章专门介绍如何自定义函数。

Page 14  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 自定义函数产生全0矩阵 def create_zeros_matrix(rows, cols): matrix = []

for _ in range(rows): row_idx = [0] * cols matrix.append(row_idx)

return matrix # 调用自定义函数 create_zeros_matrix(3, 4)

4 spaces 8 spaces a b e f g h          

图 14. 产生全0 矩阵

产生单位矩阵矩阵：一层for 循环下面举例如何用一层for 循环产生单位矩阵。本书后文会介绍如何利用numpy.identity() 产生单位矩阵。

# 自定义函数产生单位矩阵 def identity_matrix(size): matrix = []

for i in range(size): row = [0] * size row[i] = 1 matrix.append(row)

return matrix # 调用自定函数 identity_matrix = identity_matrix(4)

4 spaces 8 spaces a b e f g             h

图 15. 产生单位矩阵

产生对角方阵：一层for 循环下面举例如何用一层for 循环产生对角方阵。本书后文会介绍如何利用numpy.diag() 产生对角方阵。

# 自定义函数产生对角方阵 def diagonal_matrix(values): size = len(values); matrix = []

for i in range(size): row = [0] * size matrix.append(row)

matrix[i][i] = values[i]

return matrix # 对角线元素 diagonal_values = [4, 3, 2, 1]

# 调用自定义函数 diagonal_matrix = diagonal_matrix(diagonal_values)

4 spaces 8 spaces a b e f g h            

图 16. 产生对角方阵

Page 15  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

提取对角线元素：一层for 循环下面举例如何用一层for 循环提取矩阵 (未必是方阵) 对角线元素。大家会发现numpy.diag() 也可以用来提取矩阵对角线元素。

def extract_main_diagonal(matrix):

rows = len(matrix); cols = len(matrix[0])

size = min(rows, cols)

diagonal = [matrix[i][i] for i in range(size)]

return diagonal matrix = [[1, 2, 3], [4, 5, 6]]

main_diagonal = extract_main_diagonal(matrix)

main_diagonal a b

图 17. 提取对角线元素

计算方阵迹方阵的迹是指矩阵中主对角线上元素的总和。通常用tr(A)表示，其中A 是方阵。

def trace(matrix): rows = len(matrix)

cols = len(matrix[0])

if rows != cols: raise ValueError("Matrix is not square")

diagonal_sum = sum(matrix[i][i] for i in range(rows))

return diagonal_sum # 示例用法 A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

trace_A = trace(A)

print("矩阵的迹为:", trace_A)

a b

图 18. 提取对角线元素

判断矩阵是否对称：两层for 循环下面举例如何用两层for 循环判断矩阵是否对称。本书后文会介绍如何利用numpy.diag() 产生对角方阵。

Page 16  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a def is_symmetric(matrix): rows = len(matrix)

cols = len(matrix[0])

# 首先判断矩阵是否为方阵 if rows != cols: return False # 判断矩阵元素是否沿对称轴镜像对称 for i in range(rows): for j in range(cols): if matrix[i][j] != matrix[j][i]: return False return True # 两个矩阵 A = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

B = [[1, 2, 3], [2, 4, 0], [0, 5, 6]]

print("是否为对称矩阵:", is_symmetric(A))

print("是否为对称矩阵:", is_symmetric(B))

b

图 19. 判断矩阵是否为对称矩阵矩阵转置来判断对称矩阵的方法。如果矩阵等于其转置，那么它是对称的，否则不是。

def is_symmetric_2(matrix): rows = len(matrix)

cols = len(matrix[0])

# 首先判断矩阵是否为方阵 if rows != cols: return False # 获得转置矩阵 tranposed = [[(matrix[j][i])

for j in range(rows)]

for i in range(rows)]

if(matrix == tranposed): return True return False # 两个矩阵 A = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

B = [[1, 2, 3], [2, 4, 0], [0, 5, 6]]

print("是否为对称矩阵:", is_symmetric_2(A))

print("是否为对称矩阵:", is_symmetric_2(B))

a b

图 20. 利用矩阵转置判断矩阵是否对称

Page 17  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 矩阵行列式 2 × 2 矩阵 A = a b       的行列式值为det(A) = ad – bc。

def determinant_2x2(matrix): if len(matrix) != 2 or len(matrix[0]) != 2: raise ValueError("Matrix must be 2x2")

a = matrix[0][0]

b = matrix[0][1]

c = matrix[1][0]

d = matrix[1][1]

det = a*d - b*c return det # 示例用法 A = [[3, 2], [1, 4]]

det = determinant_2x2(A)

print("矩阵行列式:", det)

a b

图 21. 2 × 2 矩阵的行列式值

矩阵逆 2 × 2 矩阵 A = a b       的逆为 b a ad bc −     − −   。

def inverse_2x2(matrix): if len(matrix) != 2 or len(matrix[0]) != 2: raise ValueError("Matrix must be 2x2")

a = matrix[0][0]

b = matrix[0][1]

c = matrix[1][0]

d = matrix[1][1]

det = a * d - b * c if det == 0: raise ValueError("Matrix is not invertible")

inv_det = 1 / det inv_matrix = [[d * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]

return inv_matrix A = [[2, 3], [4, 5]]

inv_matrix = inverse_2x2(A)

a b

图 22. 2 × 2 矩阵的行列式值

Page 18  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 8.4 递归

在函数定义时，函数体内的代码块需要缩进，以表示该代码块属于函数体。

在这个例子中，我们定义fibonacci() 函数生成斐波那契数列 (Fibonacci sequence) 接受一个整数 n，它返回 Fibonacci 数列的第 n 项。如果 n 小于或等于 1，它将直接返回 n。否则，它将调用两次自己，并将 n-1 和 n-2 作为参数传递给它们。最终，当 n 达到 0 或 1 时，递归将停止，返回相应的值。

通过使用 for 循环来输出 Fibonacci 数列的前 10 项，可以看到这个函数在工作时是如何递归调用自己的。

《可视之美》介绍如何可视化斐波那契数列。《数学要素》将专门介绍斐波那契数列。《矩阵力量》讲解如何用线性代数工具求解斐波那契数列通项公式。

b a # 使用递归函数生成 Fibonacci 数列 def fibonacci(n): # 如果 n 小于或等于 1，它将直接返回 n if n <= 1: return n # 否则，它将调用两次自己 # 并将 n-1 和 n-2 作为参数传递给它们 else: return fibonacci(n-1) + fibonacci(n-2)

# 通过使用 for 循环来输出 Fibonacci 数列的前 10 项 for i in range(10): print(fibonacci(i))

4 spaces 8 spaces e f

图 23. 使用递归方法生成斐波那契数列

什么是斐波那契数列？

斐波那契数列是一组数字，其中每个数字都是前两个数字的和。斐波那契数列的前几个数字是 0、1、1、2、3、5、8、13、21、 34 等等。斐波那契数列是计算机科学中常用的例子，用于介绍递归和动态规划等概念。在植物学中，叶子、花瓣和果实的排列顺序可以遵循斐波那契数列。许多音乐家和作曲家使用斐波那契数列的规律来创建旋律和和弦。

## 8.5 匿名函数

在Python 中，匿名函数也被称为lambda 函数，是一种快速定义单行函数的方式。使用lambda 函数可以避免为简单的操作编写大量的代码，而且可以作为其他函数的参数来使用。

匿名函数的语法格式为：lambda arguments: expression。其中，arguments 是参数列表，expression 是一个表达式。当匿名函数被调用时，它将返回expression 的结果。

Page 19  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

下面是一些使用匿名函数的例子。

a b my_list = [1, 2, 3, 4, 5]

# 将列表中的所有元素加 1 list_plus_1 = list(map(lambda x: x+1, my_list))

print(list_plus_1)

# [2, 3, 4, 5, 6]

# 将列表中的所有元素分别求平方 list_squared = list(map(lambda x: x**2, my_list))

print(list_squared)

# [1, 4, 9, 16, 25]

图 24. lambda 函数

在这个例子中，我们定义了一个匿名函数lambda x: x + 1，该函数接受一个参数x 并返回x 加1。然后我们使用map()将这个函数应用于列表my_list 中的每个元素，并将结果存储在list_plus_1 列表中。类似地，我们还计算了my_list 中的每个元素的平方。

在Python 中，map()是一种内置的高阶函数，它接受一个函数和一个可迭代对象作为输入，将函数应用于可迭代对象的每个元素并返回一个可迭代对象，其中每个元素都是应用于原始可迭代对象的函数的结果。

## 8.6 构造模块、库

简单来说，若干函数可以打包成一个模块，几个模块可以打包成一个库。本节简单聊一聊如何创建模块、创建库，对于大部分读者来说这一节可以跳过不读。

自定义模块在Python 中，我们可以将几个相关的函数放在一个文件中，这个文件就成为一个模块。下面是一个例子。假设我们有两个函数，一个是计算圆的面积，一个是计算圆的周长，我们可以将这两个函数放在一个文件中，例如我们可以创建一个名为 "circle.py" 的文件，并将以下代码添加到该文件中。我们首先导入了math 模块，然后定义了两个函数area()和circumference()，分别用于计算圆的面积和周长。

Page 20  |  Chapter 8 Python 函数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import math def area(radius): return math.pi * radius**2 def circumference(radius): return 2 * math.pi * radius # 将其存为文件circle.py

图 25. 构造模块circle.py

在本章配套的代码中，我们调用了circle.py。使用import 语句导入了circle 模块，并命名为cc，然后通过cc.area()、cc.circumference() 调用函数。

自定义库在Python 中，可以使用setuptools 库中的setup()函数将多个模块打包成一个库。本章配套代码中给出的例子对应的具体步骤如下： 创建一个文件夹，用于存放库的代码文件，例如命名为mylibrary。

在mylibrary 文件夹中创建一个名为setup.py 的文件，引入setuptools 库，并使用setup()函数来描述库的信息，包括名称、版本、作者、依赖、模块文件等信息。

在mylibrary 文件夹中创建一个名为__init__.py 的空文件 (内容空白)，用于声明这个文件夹是一个 Python 包。

在mylibrary 文件夹中创建多个模块文件，这些模块文件包含需要打包的函数或类。比如，mylibrary 中含有linear_alg.py 和circle.py 两个模块。linear_alg.py 有矩阵乘法、向量内积两个函数。circle.py 有计算圆面积、周长两个函数。

本章配套的代码中给出如何调用自定义库。

请大家完成下面题目。

Q1. 请大家把本章第3 节介绍的有关线性代数函数打包成一个模块，并存成一个.py 文件；然后，从 Jupyter Notebook 中分别调用这些函数。

* 不提供答案。

Page 1  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Object-Oriented Programming in Python Python 面向对象编程 OOP 听起来很玄乎。其实就像个筐，什么都能装

机会总是青睐做好准备的人。

Chance favors the prepared mind.

—— 路易·巴斯德 (Louis Pasteur)  |  法国微生物学家、化学家  |  1822 ~ 1895

◄ class 定义一个类，类是一种数据结构，包含属性和方法，用于创建实例对象 ◄ def __init__() 用于初始化对象的属性，在对象创建时自动调用 ◄ self 表示当前对象的引用，用于访问对象的属性和调用对象的方法 ◄ @property 装饰器，将方法转换为属性，使得方法像属性一样访问 ◄ @classmethod 装饰器，将方法定义为类方法，而不是实例方法 ◄ cls 用于访问类的属性和调用类的方法 ◄ super().__init__() 调用父类的构造方法，用于在子类的构造方法中初始化父类的属性

Page 2  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 9.1 什么是面向对象编程?

本章蜻蜓点水介绍面向对象编程基本用法。对于大部分读者来说，本章可以跳过不读。如果对面向对象编程感兴趣的话，请继续阅读本章。

面向对象编程 (Object-Oriented Programming, OOP) 是一种编程范式，它将数据和操作数据的方法组合在一起，形成一个对象。在面向对象编程中，一个对象拥有一组属性 (用来描述对象的特征) 和方法 (用来设定对象的行为)。对象可以与其他对象互动，实现特定的功能。面向对象编程强调封装、继承和多态等概念，使程序更易于维护和扩展。

在 Python 中，一切皆为对象，可以通过 class 关键字来定义一个类，类中可以包含属性和方法，然后通过实例化对象来使用类中的属性和方法。

打个比方，OOP 中的类 (class) 就好比图 1 中的成套餐具，相当一种模板。盘子好比属性 (attribute)， 用来装各种食物 (数据)；刀叉好比方法 (method)，用来用餐 (操作)。而实例 (instance) 则相当于一个个具体的套餐，盘中餐可以是凉菜、炒饭、炒面等等。

Attributes Method (knife)

Method (fork)

Instances Class

图 1. 面向对象编程中的属性、方法

图 2 这段代码定义了一个名为Rectangle 的类，它具有构造函数来初始化矩形的宽度和高度，并提供了两个方法来计算矩形的周长和面积。

Page 3  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 定义一个名为Rectangle的类 class Rectangle: # 创建Rectangle对象时执行一些初始化工作 def __init__(self, width, height): # 设置实例变量self.width来存储传入的宽度参数 self.width = width # 设置实例变量self.height来存储传入的高度参数 self.height = height

# 定义一个名为circumference的方法，用于计算矩形的周长 def circumference(self): # 返回矩形的周长，计算公式为2*(宽度 + 高度)

return 2*(self.width + self.height)

# 定义一个名为area的方法，用于计算矩形的面积 def area(self): # 返回矩形的面积，计算公式为宽度 * 高度 return self.width * self.height # 使用Rectangle类 # 定义矩形，宽5，高10 rect_width_5_height_10 = Rectangle(5, 10)

print('矩形周长')

print(rect_width_5_height_10.circumference())

print('矩形面积')

print(rect_width_5_height_10.area())

b a e f width height Attributes: self.width self.height Methods: self.circumference()

self.area()

图 2. 定义、使用“矩形”类

下面详细介绍图 2 代码。

a 定义了一个矩形类，名称为Rectangle。Rectangle 有两个属性 width 和 height。类是一个代码模板，用于创建具有相似属性和行为的对象。Rectangle 有两个方法：circumference (计算周长)、area (计算面积)。

b 中关键字class 是用来创建对象的模板，它是面向对象编程的基础。关键词class 把数据 (属性) 和操作 (方法) 封装起来，这样便于代码模块化，方便维护。此外，类之间可以通过继承机制建立关系，本章后面将介绍。

c 中__init__(self, ...) 方法是Python 中的一个特殊构造方法，用于在创建类的实例时进行初始化操作。

在__init__方法的参数列表中，第一个参数通常被命名为self，它指向类的实例对象。

注意，__中有两个半角下划线_ (underscore)；init 四个字母均为小写字母；self 四个字母也均为小写字母。

self 参数在调用类的其他方法时自动传递，可以通过self 访问类的属性和其他方法。在 __init__方法内部，可以定义初始化对象时需要执行的逻辑，例如设置对象的初始状态，为对象设置属性的初始值等。

d 用def 定义了circumference()这个方法，用来计算矩形周长，并用return 返回计算结果。

e 用def 定义了area()这个方法，用来计算矩形面积，并用return 返回计算结果。

Page 4  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f 调用了自定义的Rectangle 对象，将其命名为rect_width_5_height_10。输入的参数为：矩形宽度5、矩形高度10。

大家练习时，利用rect_width_5_height_10.width 打印矩形宽度。

注意，调用属性时不加圆括号 ()。

然后，rect_width_5_height_10.circumference() 调用矩形对象的circumference()

方法计算这个矩形的周长。rect_width_5_height_10.area() 调用矩形对象的area() 方法计算面积。

注意，使用方法时需要圆括号 ()。

请大家自行练习图 2 代码，使用Rectangle 定义宽度为6、高度为8 的矩形对象，并计算矩形的周长、面积。

## 9.2 定义属性

在图 3 代码a 中，我们定义一个叫Chicken 的类，这个类有以下属性：(1) name (名字)；(2) age (鸡龄)；(3) color (毛色)；(4) weight (体重)。

图 3 代码中c 使用__init__方法来初始化Chicken 这个类的属性。

接下来，图 3 创建一只名为“小红”的黄色小鸡，命名为chicken_01；然后，创建了一只名为“小黄”的红色色小鸡，命名为chicken_02。请大家在练习的时候，也打印chicken_02 的属性。

此外，在后续代码中还可以覆盖对象属性。比如，如果对象chicken_01 的年龄写错，也可以用 chicken_01.age = 5 覆盖。

图 4 中也定了Chicken 类，图 4 和图 3 的代码的最大不同的是图 4 中在定义Chicken 类时给color、 weight 两个属性默认值。

图 4 代码e 调用Chicken 类时，覆盖了默认毛色，但是保留体重默认值。

注意，图 3 中定义的Chicken 类，不能通过chicken_01 = Chicken() 直接定义一个实例。会产生如下错误。

TypeError: Chicken.__init__() missing 4 required positional arguments: 'name', 'age', 'color', and 'weight' 将图 3 改成图 5 后，在e 中利用Chicken 类创建实例chicken_01 时不需要赋值。

然后，如f 所示，再对chicken_01 的每个属性分别赋值。

Page 5  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 创建了一个名为 "Chicken" 的类 class Chicken: def __init__(self, name, age, color, weight): # 初始化对象的属性 # 设置实例变量self.name来存储小鸡名字 self.name = name # 设置实例变量self.age来存储小鸡年龄 self.age = age # 设置实例变量self.color来存储小鸡体色 self.color = color # 设置实例变量self.weight来存储小鸡体重 self.weight = weight # 调用Chicken类 chicken_01 = Chicken("小红", 1, "黄色", 1.5)

chicken_02 = Chicken("小黄", 1.2, "红色", 2)

print('==小鸡的名字=='); print(chicken_01.name)

print('==小鸡的年龄，yr=='); print(chicken_01.age)

print('==小鸡的颜色=='); print(chicken_01.color)

print('==小鸡的体重，kg=='); print(chicken_01.weight)

b a e Attributes: self.name self.age self.color self.weight

图 3. 定义、使用“鸡”类

# 创建了一个名为 "Chicken" 的类 class Chicken: def __init__(self, name, age, color = '黄色', weight = '2'): # 初始化对象的属性；毛色默认 '黄色'，体重默认 2 (kg)

# 设置实例变量self.name来存储小鸡名字的参数 self.name = name # 设置实例变量self.age来存储小鸡名字的年龄 self.age = age # 设置实例变量self.color来存储小鸡名字的颜色 self.color = color # 设置实例变量self.weight来存储小鸡名字的体重 self.weight = weight # 调用Chicken类 chicken_01 = Chicken(name = "小红", age = 1, color = '白色') # 覆盖默认 color print('==小鸡的名字=='); print(chicken_01.name)

print('==小鸡的年龄，yr=='); print(chicken_01.age)

print('==小鸡的颜色=='); print(chicken_01.color)

print('==小鸡的体重，kg=='); print(chicken_01.weight)

b a e Attributes: self.name self.age self.color self.weight

图 4. 定义、使用“鸡”类，设置默认参数变量 (color, weight)

Page 6  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 创建了一个名为 "Chicken" 的类 class Chicken: def __init__(self): # 初始化对象的属性 # 设置实例变量self.name来存储小鸡名字的参数 self.name = '' # 设置实例变量self.age来存储小鸡名字的年龄 self.age = '' # 设置实例变量self.color来存储小鸡名字的颜色 self.color = '' # 设置实例变量self.weight来存储小鸡名字的体重 self.weight = '' # 调用Chicken类，然后赋值 chicken_01 = Chicken()

chicken_01.name = '小红' chicken_01.age = 1 chicken_01.color = '黄色' chicken_01.weight = 1.5 b a f Attributes: self.name self.age self.color self.weight e

图 5. 定义、使用“鸡”类，创建实例时不需要参数

## 9.3 定义方法

图 6 给出一个例子，代码a 定义一个ListStatistics 类来计算一个浮点数列表的长度、和、平均值、 方差。

d 定义的list_mean() 方法计算平均值时用到了list_length() 方法。

e 定义的list_variance() 方法还有一个输入ddof，ddof 默认值为1。

f 调用ListStatistics 类创建对象。

g 计算两个方差；第一个方差相当于粽子方差，第二个方差相当于样本无偏方差。

此外，我们在第4 章介绍过，Python 变量名一般采用蛇形命名法，比如list_mean()；Python 面向对象编程中的类定义一般采用驼峰命名法，比如ListStatistics。

Page 7  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 创建 ListStatistics 类 class ListStatistics: # 构造函数，用于初始化属性 def __init__(self, data): # ListStatistics包含一个data属性来存储浮点数列表 self.data = data

# 下面定义了4个方法 # 方法1：计算列表的长度，即元素的数量 def list_length(self): return len(self.data)

# 方法2：计算列表元素之和 def list_sum(self): return sum(self.data)

# 方法3：计算列表元素平均值 def list_mean(self): return sum(self.data)/self.list_length()

# 方法4：计算列表元素方差 def list_variance(self, ddof = 1): # Delta自由度 ddof 默认为 1；无偏样本方差 sum_squares = sum((x_i - self.list_mean())**2 for x_i in self.data)

return sum_squares/(self.list_length() - ddof)

# 创建一个浮点数列表 data = [8.8, 1.8, 7.8, 3.8, 2.8, 5.6, 3.9, 6.9]

# 创建ListStatistics对象实例 float_list = ListStatistics(data)

# 使用float_list对象计算列表长度 print("列表长度：", float_list.list_length())

# 使用float_list对象计算列表和 print("列表和：", float_list.list_sum())

# 使用float_list对象计算列表平均值 print("列表平均值：", float_list.list_mean())

# 使用float_list对象计算列表方差 print("列表方差：", float_list.list_variance())

print("列表方差 (ddof = 0)：", float_list.list_variance(0))

b a Attribute: self.data Methods: self.list_length()

self.list_sum()

self.list_mean()

self.list_variance()

e f g

图 6. 定义、使用“列表统计量”类

## 9.4 装饰器

在Python 中，装饰器 (decorator) 是一种特殊的语法，用于在不修改函数代码的情况下，为函数添加额外的功能或修改函数的行为。

如图 7 所示，d 中装饰器 @property 用于将一个方法转换为只读属性，可以像访问属性一样访问该方法，而无需使用括号调用它。

f 中装饰器 @data.setter 装饰器用于在 @property 装饰的方法后定义一个 setter 方法，这样可以在设置属性时执行一些逻辑或验证，对属性的赋值进行控制。

Page 8  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com h 中装饰器 @classmethod 装饰器用于定义类方法。类方法是在类上而不是在实例上调用的方法。

不同于self，类方法的第一个参数通常被命名为 cls，它表示类本身而不是实例简单来说，cls 是一个约定俗成的名字，表示类本身，而不是类的实例。

i 用于逐个判断一个列表中的所有元素是否都是数值，比如float 或int 类型。

j 创建了ListStatistics 类的实例，命名为float_list_obj。由于data 中有一个非数值元素，在k 赋值时会报错。

# 定义了一个 ListStatistics 类 class ListStatistics: # 构造函数，用于初始化属性 def __init__(self): self._data = []

@property # @property 将方法转换为只读属性 def data(self): return self._data

@data.setter # setter 设置属性时执行一些逻辑或验证 def data(self, new_list): if self._are_all_numeric(new_list): self._data = new_list else: print("错误：列表中元素必须全部是数值")

@classmethod # @classmethod 装饰器用于定义类方法 # 逐个判断列表所有元素是否都是数值 def _are_all_numeric(cls, input_list): for element in input_list: if not isinstance(element, (int, float)): return False return True # 创建一个浮点数列表 data = [8.8, 1.8, 7.8, 3.8, 2.8, 5.6, '3.9', 6.9]

# 创建实例 float_list_obj = ListStatistics()

# 尝试设置含非数值元素的列表，会输出错误消息 float_list_obj.data = data b a g j f h k

图 7. 定义、使用“列表统计量”类，使用装饰器

Page 9  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 9.5 父类、子类

在面向对象编程中，父类 (parent class) 和子类 (child class) 之间是一种继承关系。父类，也称基类、 超类，在继承关系中层次更高；子类，也称派生类，可以继承父类的属性和方法，从而实现代码的重用和扩展。子类可以有多个，并且一个子类也可以再被其他类继承，形成继承的层级结构。

简单来说，父类提供了一个通用模板。如图 8 所示，盘子 + 刀叉，这个组合就相当于父类。而午餐、晚餐一方面继承了“盘子 + 刀叉”，并在此基础上进行了扩展和订制。

午餐的餐具组合为：父类 (盘子 + 刀叉) + 碗；晚餐的餐具组合为：父类 (盘子 + 刀叉) + 酒杯。

Attributes Method (knife)

Method (fork)

Parent class Child class Child class

图 8. 面向对象编程中，父类、子类关系

图 9 代码演示了如何定义父类 Animal 和子类 Chicken、Rabbit、Pig。

首先，a  定义了一个 Animal 父类。

e 定义了Animal 的两个属性——名字、年龄；Animal 有两个方法——吃饭f 、睡觉g 。

b  c  d 分别定义了三个子类 Chicken、Rabbit、Pig。它们分别继承了父类 Animal 的属性和方法，并且分别定义了自己的属性和方法。

当一个类继承自另一个类时，子类可以通过super().__init__() 来调用父类的构造方法，以便在实例化子类时，也能初始化从父类继承的属性。

比如，h 定义了Chicken 类专属属性 color，表示鸡的颜色。

i 定义了Chicken 类专属方法lay_egg，表示鸡下蛋。Rabbit、Pig 也有各自的专属属性和方法。

Page 10  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 父类，动物 class Animal: def __init__(self, name, age): self.name = name self.age = age def eat(self): print(f"{self.name} is eating.")

def sleep(self): print(f"{self.name} is sleeping.")

# 子类，鸡 class Chicken(Animal): def __init__(self, name, age, color): super().__init__(name, age)

self.color = color def lay_egg(self): print(f"{self.name} is laying an egg.")

# 子类，兔 class Rabbit(Animal): def __init__(self, name, age, speed): super().__init__(name, age)

self.speed = speed def jump(self): print(f"{self.name} is jumping.")

# 子类，猪 class Pig(Animal): def __init__(self, name, age, weight): super().__init__(name, age)

self.weight = weight def roll(self): print(f"{self.name} is rolling around.")

chicken1 = Chicken("chicken1", 1, "white")

chicken1.eat(); chicken1.lay_egg()

rabbit1 = Rabbit("rabbit1", 2, 10)

rabbit1.sleep(); rabbit1.jump()

pig1 = Pig("pig1", 3, 100)

pig1.eat(); pig1.roll()

a b f e g h j k

图 9. 定义、使用父类 (动物)、子类 (鸡、兔、猪)

请大家完成下面2 道题目。

Q1. 参考图 2，写一个名为Circle 的类，参数为半径，定义两个方法分别计算圆的周长、面积。提示，需要导入math.pi 圆周率近似值。

Q2. 请大家在练习图 6 代码时，再增加4 个方法，分别计算最大值、最小值、极差 (最大值 – 最小值)、标准差。

* 两道题目很简单，本书不提供答案。

Page 11  |  Chapter 9 Python 面向对象编程  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

本章只是Python 面向对象编程OOP 冰山一角，希望大家在需要用到OOP 时深入学习。

Page 1  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Fundamentals of Visualization 聊聊可视化主要了解Matplotlib、Plotly 两个工具

一个人可以被摧毁，但不能被打败。

A man can be destroyed but not defeated.

—— 欧内斯特·海明威 (Ernest Hemingway)  |  美国、古巴记者和作家  |  1899 ~ 1961

◄ matplotlib.gridspec.GridSpec() 创建一个规则的子图网格布局 ◄ matplotlib.pyplot.grid() 在当前图表中添加网格线 ◄ matplotlib.pyplot.plot() 绘制折线图 ◄ matplotlib.pyplot.subplot() 用于在一个图表中创建一个子图，并指定子图的位置或排列方式 ◄ matplotlib.pyplot.subplots() 创建一个包含多个子图的图表，返回一个包含图表对象和子图对象的元组 ◄ matplotlib.pyplot.title() 设置当前图表的标题，相当于对于特定轴ax 对象ax.set_title()

◄ matplotlib.pyplot.xlabel() 设置当前图表x 轴的标签，相当于对于特定轴ax 对象ax.set_xlabel()

◄ matplotlib.pyplot.xlim() 设置当前图表x 轴显示范围，相当于对于特定轴ax 对象ax.set_xlim()

◄ matplotlib.pyplot.xticks() 设置当前图表x 轴刻度位置，相当于对于特定轴ax 对象ax.set_xticks()

◄ matplotlib.pyplot.ylabel() 设置当前图表y 轴的标签，相当于对于特定轴ax 对象ax.set_ylabel()

◄ matplotlib.pyplot.ylim() 设置当前图表y 轴显示范围，相当于对于特定轴ax 对象ax.set_ylim()

◄ matplotlib.pyplot.yticks() 设置当前图表y 轴刻度位置，相当于对于特定轴ax 对象ax.set_yticks()

◄ numpy.arange() 创建一个具有指定范围、间隔和数据类型的等间隔数组 ◄ numpy.cos() 用于计算给定弧度数组中每个元素的余弦值 ◄ numpy.exp() 计算给定数组中每个元素的e 的指数值 ◄ numpy.linspace() 用于在指定的范围内创建等间隔的一维数组，可以指定数组的长度 ◄ numpy.sin() 用于计算给定弧度数组中每个元素的正弦值 ◄ numpy.tan() 用于计算给定弧度数组中每个元素的正切值 ◄ plotly.express.line() 用于创建可交互的线图 ◄ plotly.graph_objects.Scatter() 用于创建可交互的散点图、线图 ◄ scipy.stats.norm() 创建一个正态分布对象，可用于计算概率密度、累积分布等

Page 2  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 10.1 解剖一幅图

本章和接下来两章介绍如何实现鸢尾花书中最常见的可视化方案。这三章内容本着“够《编程不难》

用就好”为原则，不会特别深究某个具体可视化方案中的呈现细节，也不会探究其他高阶的可视化方案。

鸢尾花书《可视之美》专注提供可视化的“家常菜菜谱”。

图 1. 解剖一幅图，来源https://matplotlib.org/stable/gallery/showcase/anatomy.html

如图 1 所示，一幅图的基本构成部分包括以下几个部分： ► 图像区域 (Figure)：整个绘图区域的边界框，可以包含一个或多个子图。

► 子图区域 (Axes)：实际绘图区域，包含坐标轴、绘制的图像和文本标签等。

► 坐标轴 (Axis)：显示子图数据范围并提供刻度标记和标签的对象。

► 脊柱 (Spine)：连接坐标轴和图像区域的线条，通常包括上下左右四条。

► 标题 (Title)：描述整个图像内容的文本标签，通常位于图像的中心位置或上方，用于简要概括图像的主题或内容。

Page 3  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 刻度 (Tick)：刻度标记，表示坐标轴上的数据值。

► 标签 (Label)：用于描述坐标轴或图像的文本标签。

► 图例 (Legend)：标识不同数据系列的图例，通常用于区分不同数据系列或数据类型。

► 艺术家 (Artist)：在Matplotlib 中，所有绘图元素都被视为艺术家对象，包括图像区域、子图区域、 坐标轴、刻度、标签、图例等等。

可视化工具图 1 这幅图是用Matplotlib 库绘制。Matplotlib 是Python 中最基础的绘图工具。鸢尾花书中最常用的绘图库包括：Matplotlib、Seaborn、Plotly。

Matplotlib 可能是Python 中最常用的绘图库，Matplotlib 具有丰富的绘图功能和灵活的使用方式。

Matplotlib 可以绘制多种类型的图形，包括折线图、散点图、柱状图、饼图、等高线图等各种二维、三维图像，还可以进行图像处理和动画制作等。图 25、图 26、图 27 给出Matplotlib 中常见的可视化方案。

Seaborn 是基于Matplotlib 的高级绘图库，专注于统计数据可视化。它提供了多种高级数据可视化技术，包括分类散点图、热图 (热力图)、箱线图、分布图等，可以快速生成高质量的统计图表。Seaborn 适用于数据分析、数据挖掘和机器学习等领域。

注意，Matplotlib 和Seaborn 生成的都是静态图，即图片。

Plotly 是一个交互式可视化库，可以生成高质量的静态和动态图表。它提供了丰富的图形类型和交互式控件，可以通过滑块、下拉列表、按钮等方式动态控制图形的显示内容和样式。Plotly 适用于Web 应用、数据仪表盘和数据科学教育等领域。类似Plotly 的Python 库还有Bokeh、Altair、Pygal 等。

鸢尾花书中，大家会发现PDF 书稿、纸质书图片一般会使用Matplotlib、Seaborn 生成的矢量图，配套的JupyterLab Notebook、Streamlit 则倾向于采用Plotly。

本书第六大板块“数据”会介绍Pandas 本身、Seaborn 的统计描述可视化方案。

## 10.2 使用Matplotlib 绘制线图

下面我们聊一下如何用Matplotlib 可视化正弦、余弦函数，图 2 所示代码生成图 3。下面我们逐块讲解这段代码；此外，请大家在JupyterLab 中复刻这段代码，并绘制图 3。

大家会在鸢尾花书中发现，我们用Python 代码生成的图像和书中的图像很多细节上并不一致。产生这种偏差的原因有很多。

首先，为了保证矢量图像质量及可编辑性，每幅Python 代码生成的图形都会经过多道后期处理。后期处理的工具包括 (但不限于) Inkscape、MS Visio、Adobe Illustrator。使用怎样的工具要根据图片类型、图片大小等因素考虑。

也就是说哪怕图 2 这种简单的线图中的所有“艺术家 (artist)”，即所有元素，都被加工过。比如，图中的数字、英文、希腊字母都是手动添加上去的 (为了保证文本可编辑)。此外，从时间角度来看，一些标注、艺术效果用Python 写代码方生成并不“划算”。

但是，加工过程仅仅是为了美化图像，并没有篡改数据本身。不篡改数据是一条铁律，希望大家谨记。

Page 4  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

a b f # 导入包 import numpy as np import matplotlib.pyplot as plt # 生成横轴数据 x_array = np.linspace(0, 2*np.pi, 100)

# 正弦函数数据 sin_y = np.sin(x_array)

# 余弦函数数据 cos_y = np.cos(x_array)

# 设置图片大小 fig, ax = plt.subplots(figsize=(8, 6))

# 绘制正弦和余弦曲线 ax.plot(x_array, sin_y, label='sin', color='b', linewidth=2)

ax.plot(x_array, cos_y, label='cos', color='r', linewidth=2)

# 设置标题、横轴和纵轴标签 ax.set_title('Sine and cosine functions')

ax.set_xlabel('x')

ax.set_ylabel('f(x)')

# 添加图例 ax.legend()

# 设置横轴和纵轴范围 ax.set_xlim(0, 2*np.pi)

ax.set_ylim(-1.5, 1.5)

# 设置横轴标签和刻度标签 x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2)

x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

ax.set_xticks(x_ticks)

ax.set_xticklabels(x_ticklabels)

# 横纵轴采用相同的scale ax.set_aspect('equal')

plt.grid()

# 将图片存成SVG格式 plt.savefig('正弦_余弦函数曲线.svg', format='svg')

# 显示图形 plt.show()

e g h j k n o

图 2. 用Matplotlib 绘制正弦、余弦线图

Inkscape 是开源免费的矢量图形编辑软件，支持多种矢量图形格式，适用于绘制矢量图形、图标、 插图等。MS Visio 特别适合做示意图、流程图等矢量图像。Adobe Illustrator 是Adobe 公司开发的专业矢量图形编辑软件，功能强大，广泛用于图形设计、插图、标志设计等。比如鸢尾花书的封面都是用 Adobe Illustrator 设计，鸢尾花书中复杂的图像也都是在这个软件设计生成。此外，也推荐大家使用 CorelDRAW。CorelDRAW 是Corel 公司开发的矢量图形编辑软件，具有类似于Adobe Illustrator 的功能，是一种流行的矢量图形处理工具。

Page 5  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sine and cosine functions π 2π π 3π sin cos 0.0 0.5 1.0 1.5 1.5 1.0 0.5 f(x)

图 3. 正弦、余弦函数线图

产生等差数列 import numpy as np 这句代码的意思是将 NumPy (Python 代码中叫numpy) 库导入到当前的 Python 程序中，并为其取一个简短的别名 np。

这意味着我们可以使用 np 来代替 numpy 来调用 NumPy 库中的函数和方法，例如 np.linspace()，np.sin()，np.cos() 等。这样做的好处是可以简化代码，减少打字量，并且提高代码的可读性。通常，人们将 numpy 取别名为 np，这是因为它的缩写简短且容易记忆。

numpy.linspace() 是 NumPy 库中的一个函数，用于生成在给定范围内等差数列。由于在导入 numpy 时，我们将其命名为np，因此代码中大家看到的是np.linspace()。

2π

图 4. 用numpy.linspace() 生成等差数列

上面的代码中，0 是数值序列的起始值，2*np.pi 是数值序列的结束值，100 是数值序列的数量。

因此，x_array = np.linspace(0, 2*np.pi, 100) 在 [0, 2π] 闭区间内生成一个100 个数值等差数列。

numpy.linspace(start, stop, num=50, endpoint=True)

这个函数的重要输入参数： ● start：起始点的值。

● stop：结束点的值。

● num：要生成的数据点数量，默认为 50。

● endpoint：布尔值，指定是否包含结束点。如果为 True，则生成的数据点包括结束点；如果为 False，则生成的数据点不包括结束点。默认为 True。

Page 6  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 请大家在JupyterLab 中自行学习下例。

import numpy as np

arr = np.linspace(0, 1, num=11)

print(arr)

arr_no_endpoint = np.linspace(0, 1, num=10, endpoint=False)

print(arr_no_endpoint)

什么是NumPy 数组array？

NumPy 中最重要的数据结构是ndarray (n-dimensional array)，即多维数组。一维数组是最简单的数组形式，类似于Python 中的列表。它是一个有序的元素集合，可以通过索引访问其中的元素。一维数组只有一个轴。二维数组是最常见的数组形式，可以看作是由一维数组组成的表格或矩阵。它有两个轴，通常称为行和列。我们可以使用两个索引来访问二维数组中的元素。多维数组是指具有三个或更多维度的数组。

正弦、余弦如图 5 所示， numpy.sin() 和 numpy.cos() 是 NumPy 库中的数学函数，用于计算给定角度的正弦和余弦值。这两个函数的输入既可以是弧度值 (比如numpy.pi/2)，也可以是数组 (一维、二维、多维)。

注意，NumPy 中numpy.deg2rad()将角度转换为弧度，numpy.rad2deg()将弧度转换为角度。

2π 2π numpy.sin()

numpy.cos()

图 5. 生成正弦、余弦数据

创建图形、轴对象 fig, ax = plt.subplots(figsize=(8, 6)) 用于创建一个新的 Matplotlib 图形fig 和一个轴ax 对象，并设置图形的大小为 (8, 6)，单位为英寸。

通过创建图形和轴对象，我们可以在轴上绘制图表、设置轴的标签和标题、调整轴的范围等。fig, ax = plt.subplots() 这一句代码常常是开始绘图的第一步，它创建了一个具有指定大小的图形和轴对象，为后续绘图操作提供了一个可用的基础。

需要注意的是，plt 是 Matplotlib 的一个常用的别名，通常通过 import matplotlib.pyplot as plt 引入。所以在使用 plt.subplots() 函数之前，需要确保已经正确导入了 Matplotlib 库。

添加子图此外，我们还可以使用使用add_subplot() 方法创建一个新的子图对象，并指定其所在的行、 列、编号等属性。

Page 7  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

a b import numpy as np import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

y = np.sin(x)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y)

plt.show()

图 6. add_subplot() 方法创建一个新的子图对象

在这个例子中，我们使用add_subplot() 方法创建了一个新的子图对象，并将其添加到Figure 对象中。其中，1, 1, 1 参数表示子图在1 行1 列的第1 个位置，即占据整个Figure 对象的空间。然后，我们在子图中绘制了一个正弦曲线。最后，使用plt.show()函数显示Figure 对象，即可在屏幕上显示绘制的图像。

绘制曲线 ax.plot(x_array, sin_y, label='sin', color='blue', linewidth=2) 用于在轴对象 ax 上绘制正弦曲线。x_array 为 x 轴数据，sin_y 为 y 轴数据。

label='sin' 设置了曲线的标签为 'sin'，color='blue' 设置曲线的颜色为蓝色， linewidth=2 设置曲线的线宽为 2。在Matplotlib 中，linewidth 参数表示线条的宽度。它的单位是点 (point, pt)，通常用于测量线条、字体等绘图元素的大小。在Matplotlib 中，默认情况下，一个点等于 1/72 inch。

图片输出格式 Matplotlib 可以输出多种格式的图片，其中一些是矢量图。以下是一些常见的输出格式及其特点： ► PNG (Portable Network Graphics)：PNG 是一种常见的位图格式，支持透明度和压缩。PNG 格式输出的图片不是矢量图，因此在放大时会失去清晰度，但是可以保持较高的分辨率和细节。

► JPG/JPEG (Joint Photographic Experts Group)：JPG 是一种常见的有损压缩位图格式，用于存储照片和复杂的图像。与PNG 不同，JPG 格式输出的图片是有损的，压缩率高时会失去一些细节，但是文件大小通常较小。

► EPS (Encapsulated PostScript)：EPS 是一种矢量图格式，可以在很多绘图软件中使用。EPS 格式输出的图片可以无限放大而不失真，适合于需要高品质图像的打印和出版工作。

► PDF (Portable Document Format)：PDF 是一种常见的文档格式，可以包含矢量图和位图。与EPS 类似，PDF 格式输出的图片也是矢量图，可以无限放大而不失真，同时具有可编辑性和高度压缩的优势。存成PDF 很方便插入Latex 文档。

► SVG (Scalable Vector Graphics)：SVG 是一种基于XML 的矢量图格式，可以用于网页和打印等多种用途。SVG 格式输出的图片可以无限放大而不失真，且文件大小通常较小。鸢尾花书的图片首选 SVG 格式。

Page 8  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 注意，EPS、PDF 和SVG 是矢量图格式，可以无限放大而不失真 (比如图 7 (b))，适合于需要高品质图像的打印和出版工作。在需要高品质图像的场合，最好使用这些矢量图格式。

(a)

(b)

图 7. 比较非矢量、矢量图

子图图 8 所示一行两列子图。请大家在JupyterLab 中给图 9 代码逐行添加注释，并复刻图 8。

《可视之美》将介绍更多子图可视化方案。

π 2π π 2π 0.0 0.5 1.0 1.5 1.5 1.0 0.5 f(x)

Sine function Cosine function f(x)

图 8. 一行、两列子图

Page 9  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b e g import numpy as np import matplotlib.pyplot as plt x = np.linspace(0, 2 * np.pi, 100)

y_sin = np.sin(x)

y_cos = np.cos(x)

# 创建图形对象和子图布局 fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# 在左子图中绘制正弦函数曲线，设置为蓝色 ax1.plot(x, y_sin, color='blue')

ax1.set_title('Sine function')

ax1.set_xlabel('x')

ax1.set_ylabel('f(x)', rotation='horizontal', ha='right')

ax1.set_xlim(0, 2*np.pi)

ax1.set_ylim(-1.5, 1.5)

x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi)

x_ticklabels = [r'$0$', r'$\pi$', r'$2\pi$']

ax1.set_xticks(x_ticks)

ax1.set_xticklabels(x_ticklabels)

ax1.grid(True)

ax1.set_aspect('equal')

# 在右子图中绘制余弦函数曲线，设置为红色 ax2.plot(x, y_cos, color='red')

ax2.set_title('Cosine function')

ax2.set_xlabel('x')

ax2.set_ylabel('f(x)', rotation='horizontal', ha='right')

ax2.set_xlim(0, 2*np.pi)

ax2.set_ylim(-1.5, 1.5)

ax2.set_xticks(x_ticks)

ax2.set_xticklabels(x_ticklabels)

ax2.grid(True)

ax2.set_aspect('equal')

# 调整子图之间的间距 plt.tight_layout()

# 显示图形 plt.show()

a f ax1 ax2 ax1 ax2

图 9. 绘制一行两列子图

Page 10  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 10.3 图片美化

颜色在 Matplotlib 中，可以使用多种方式指定线图的颜色，包括 RGB 值、预定义颜色名称、十六进制颜色码和灰度值。

可以使用 RGB (R 是red，G 是green，B 是blue) 来指定颜色，其中每个元素的值介于 0 到 1 之间。

例如，(1, 0, 0) 表示纯红色，(0, 1, 0) 表示纯绿色。使用 RGBA 值指定“颜色 + 透明度 (A)”。

如图 11 所示，RGB 三原色模型实际上构成了一个色彩“立方体”——一个色彩空间。也就是说在这个立方体中藏着无数种色彩。

鸢尾花书《矩阵力量》将会用RGB 三原色模型讲解线性代数中向量空间 (vector space) 这个重要概念。

Green (0, 1, 0)

#00FF00 Blue (0, 0, 1)

#0000FF Red (1, 0, 0)

#FF0000

图 10. RGB 三原色模型

图 11. RGB 三原色模型“立方体”

Page 11  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

什么是RGB 颜色模式？

RGB (红绿蓝) 颜色模式是一种使用红、绿、蓝三个基本颜色通道来表示颜色的方法。在RGB 模式中，通过调整每个通道的强度 (从0 到255 的值，Matplotlib 中0 到1 的值) 来创建各种颜色。通过组合不同强度的红、绿和蓝，可以形成几乎所有可见光颜色。

RGB 颜色模式被广泛应用于计算机图形、数字图像处理和网页设计等领域，它提供了一种直观、灵活且广泛支持的方式来表示和操作颜色。

Matplotlib 提供了一些常见颜色的预定义名称，例如 'red'、'green'、'blue' 等。图 24 所示为在 Matplotlib 中已经预定义名称的颜色。

大家还可以使用十六进制颜色码来指定颜色。它以 '#' 开头，后面跟着六位十六进制数。例如， '#FF0000' 表示纯红色，'#00FF00' 表示纯绿色。

我们还可以使用灰度值来指定颜色，取值介于 0 到 1 之间，表示不同的灰度级别。'0' 表示黑色，'1' 表示白色。比如，color='0.5' 代表灰度值为0.5 的灰色。

使用色谱 Matplotlib 中还有一种渐变配色方案——colormap。在Matplotlib 中，colormap 用于表示从一个端到另一个端的颜色变化。这个变化可以是连续的，也可以是离散的。

在Matplotlib 中，colormap 主要用于绘制二维图形，如热图、散点图、等高线图等。它用于将数据值映射到不同的颜色，以显示数据的变化和模式。Colormap 可以直译为“色彩映射”，鸢尾花书一般称之为“色谱”。图 12 所示为几种常见的色谱。鸢尾花书中最常用的色谱为RdYlBu。

《可视之美》将专门讲解色谱。

(d) 四季 spring summer autumn winter (e) 冷、热、彩虹 hot cool rainbow (f) 反向发散 RdBu RdYlBu RdYlGn Spectral coolwarm bwr viridis plasma cividis (a) 均匀 (b) 单色渐变 Greys Blues Reds (c) 双色渐变 GnBu OrRd BuPu (d) 三色渐变 YlGnBu YlOrBr PuBuGn

图 12. 几种常用色谱

Page 12  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 13 所示为利用色谱渲染一组曲线。图 13 左图所示为一元高斯概率密度分布曲线随均值µ 变化，图 13 右图所示为曲线随标准差σ 变化。

本书第26 章会介绍获得图 13 两幅子图的代码。

0.0 0.1 0.2 0.3 0.4 0.5 fX(x)

0.0 0.1 0.2 0.3 0.4 0.5 fX(x)

µ =  3 µ =  2 µ =  1 µ = 0 µ = 1 µ = 2 µ = 3 σ = 1.0 σ = 1.5 σ = 2.0 σ = 2.5 σ = 3.0 σ = 3.5 σ = 4.0

图 13. 用色谱渲染一组曲线

什么是高斯分布？

高斯分布 (Gaussian distribution)，也称为正态分布 (Normal distribution)，是统计学中常用的概率分布模型之一。它具有钟形曲线的形状，呈对称分布。高斯分布的概率密度函数可以由两个参数完全描述：均值 (mean) 和标准差 (standard deviation)。均值决定了分布的中心位置，标准差决定了分布的展开程度。

高斯分布在自然界和社会现象中广泛存在，例如身高、体重、温度等连续型随机变量常常服从高斯分布。中心极限定理也说明了许多独立同分布的随机变量的总和趋向于高斯分布。

高斯分布在统计学和数据分析中有着重要的应用，可用于描述数据集的分布特征、进行假设检验、构建回归模型等。在机器学习和人工智能领域，高斯分布在概率密度估计、聚类分析、异常检测等算法中被广泛使用。

什么是概率密度函数？

概率密度函数 (Probability Density Function，简称PDF) 是概率论和统计学中用于描述连续型随机变量的概率分布的函数。它表示了变量落在某个特定取值范围内的概率密度，而不是具体的概率值。

一元连续随机变量的概率密度函数是非负函数，并且在整个定义域上的积分等于1。对于给定的连续型随机变量，通过PDF 可以计算出在不同取值范围内的概率密度值，从而了解变量的分布特征和概率分布形状。

以正态分布为例，其概率密度函数即高斯函数，可以描述变量取值的概率密度。在某个特定取值处，概率密度函数的值越高，表示该取值的概率越大。概率密度函数在统计分析、数据建模、概率推断等领域广泛应用，可用于计算概率、推断参数、生成模拟数据等。

其他细节美化图 2 中还提供图片美化命令，下面逐一说明。

► ax.set_title('Sine and cosine functions') 设置图表的标题为 "Sine and cosine functions"，即正弦和余弦函数。

Page 13  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► ax.set_xlabel('x') 设置横轴标签为 "x"。ax.set_ylabel('f(x)') 设置纵轴标签为 "f(x)"。

► ax.legend() 添加图例legend，用于标识不同曲线或数据系列。

► ax.set_xlim(0, 2*np.pi) 设置横轴范围从 0 到 2π。ax.set_ylim(-1.5, 1.5) 设置纵轴范围从 −1.5 到 1.5。

► x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2) 生成横轴刻度的位置，从 0 到 2π，间隔为 π/2。

► x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'] 设置横轴刻度的标签，分别为 0, π/2, π, 3π/2, 2π。在代码中，r'$\frac{\pi}{2}$' 是一个特殊的字符串，用于表示数学公式中的文本。在这个字符串前面的 r 前缀表示该字符串是一个“原始字符串”，即不对字符串中的特殊字符进行转义。

► 在这个特殊字符串中，使用了 LaTeX 符号来表示一个分数。具体来说，\frac{\pi}{2} 表示一个分数，分子是π，分母是2。当这个字符串被用作横轴刻度的标签时，它会在图表中显示为 "π/2"

的形式。这种表示方法可以用于在图表中显示复杂的数学公式或符号。

► ax.set_xticks(x_ticks) 设置横轴刻度的位置。

► ax.set_xticklabels(x_ticklabels) 设置横轴刻度的标签。

► ax.set_aspect('equal') 设置横纵轴采用相同的比例，保持图形在绘制时不会因为坐标轴的比例问题而产生形变。

## 10.4 可视化极坐标

看到图 5 所示的正弦、余弦数据点，大家是否想到了极坐标 (polar coordinates)。

如图 14 左图所示，O 是极坐标的极点 (pole)，从O 向右引一条射线作为极轴 (polar axis)，规定逆时针角度为正。这样，平面上任意一点P 的位置可以由线段OP 的长度r 和极轴到OP 的角度θ 来确定。(r, θ) 就是P 点的极坐标。

θ P (r, θ)

O Polar axis O P (x, y)

x = rcos(θ)

y = rsin(θ)

图 14. 从极坐标系到平面直角坐标系

一般，r 称为极径 (radial coordinate 或radial distance)，θ 称为极角 (angular coordinate 或polar angle 或azimuth)。

Page 14  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 如图 14 所示，平面上，极坐标 (r, θ) 可以转化为直角坐标系坐标 (x, y)。

换个角度来看，如果我们图 5 所示余弦点作为横坐标，正弦点作为纵坐标，画在在一幅图上，我们便可以得到圆心位于原点、半径为1 的正圆，也叫单位圆 (unit circle)，具体如图 15 所示。

1.5 1.0 0.5 0.0 0.5 1.0 1.5 x = cos(θ)

1.5 1.0 0.5 0.0 0.5 1.0 1.5 y = sin(θ)

图 15. 单位圆

下面聊聊绘制图 15 的代码。

Page 15  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b g # 导入包 import numpy as np import matplotlib.pyplot as plt # 生成数据 theta_array = np.linspace(0, 2*np.pi, 120, endpoint = False)

sin_y = np.sin(theta_array)

cos_y = np.cos(theta_array)

# 用hsv色谱产生一组渐变色，颜色种类和散点数相同 colors = plt.cm.hsv(np.linspace(0, 1, len(cos_y)))

# 设置图片大小 fig, ax = plt.subplots(figsize=(6, 6))

# 绘制正圆，横轴坐标为 cos，纵轴坐标为 sin ax.plot(cos_y, sin_y, zorder = 1, color = 'k', lw = 0.25)

ax.scatter(cos_y, sin_y, marker = '.', s = 88, c=colors, edgecolor='w', zorder = 2, lw = 0.25)

ax.axhline(0, c = 'k', zorder = 1)

ax.axvline(0, c = 'k', zorder = 1)

ax.set_xlabel(r'$x = cos(\theta)$')

ax.set_ylabel(r'$y = sin(\theta)$')

# 设置横轴和纵轴范围 ax.set_xlim(-1.5, 1.5)

ax.set_ylim(-1.5, 1.5)

ax.grid(True)

# 横纵轴采用相同的scale ax.set_aspect('equal')

ax.spines['top'].set_visible(False)

ax.spines['right'].set_visible(False)

ax.spines['bottom'].set_visible(False)

ax.spines['left'].set_visible(False)

a e f

图 16. 绘制单位圆

Page 16  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com y = sin(θ)

x = cos(θ)

1.0 0.5 0.0 0.5 1.0 1.0 0.5 0.0 0.5 1.0

图 17. 单位圆原理

下面分别讲解每幅子图对应的代码。

Page 17  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 导入包 import numpy as np import matplotlib.pyplot as plt # 生成数据 theta_array = np.linspace(0, 2*np.pi, 120, endpoint = False)

sin_y = np.sin(theta_array)

cos_y = np.cos(theta_array)

colors = plt.cm.hsv(np.linspace(0, 1, len(cos_y)))

# 设置子图长宽比例 fig, axes = plt.subplots(2, 2, figsize = (8,8), gridspec_kw = { 'width_ratios':[3, 1], 'height_ratios':[1, 3]})

# 刻度 radian_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2)

radian_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

level_ticks = [-1, -0.5, 0, 0.5, 1]

# 关闭左下角子图 axes[1,0].axis('off')

a b

图 18. 生成数据，设置子图布局

# 左上角子图：正弦曲线 axes[0,0].plot(theta_array, sin_y, color = 'k', lw = 0.25)

axes[0,0].scatter(theta_array, sin_y, marker = '.', s = 38, c=colors, edgecolor='w', zorder = 2)

# 图片美化 axes[0,0].set_xlim(0, 2 * np.pi)

axes[0,0].set_ylim(-1.2, 1.2)

axes[0,0].set_xticks(radian_ticks)

axes[0,0].set_xticklabels(radian_ticklabels)

axes[0,0].set_yticks(level_ticks)

axes[0,0].grid()

axes[0,0].spines['top'].set_visible(False)

axes[0,0].spines['right'].set_visible(False)

axes[0,0].spines['bottom'].set_visible(False)

axes[0,0].spines['left'].set_visible(True)

axes[0,0].set_aspect('equal', adjustable='box')

a b

图 19. 绘制左上角子图

Page 18  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 右上角子图：单位圆 axes[0,1].plot(cos_y, sin_y, color = 'k', lw = 0.25, zorder = 1)

axes[0,1].scatter(cos_y, sin_y, marker = '.', s = 38, c=colors, edgecolor='w', zorder = 2)

# 图片美化 axes[0,1].axhline(0, c = 'k', zorder = 1)

axes[0,1].axvline(0, c = 'k', zorder = 1)

axes[0,1].set_xlim(-1.2, 1.2)

axes[0,1].set_ylim(-1.2, 1.2)

axes[0,1].set_xticks(level_ticks)

axes[0,1].set_yticks(level_ticks)

axes[0,1].set_xticklabels([])

axes[0,1].set_yticklabels([])

axes[0,1].set_xlabel(r'$x = cos(\theta)$')

axes[0,1].set_ylabel(r'$y = sin(\theta)$')

axes[0,1].grid()

axes[0,1].set_aspect('equal', adjustable='box')

axes[0,1].spines['top'].set_visible(False)

axes[0,1].spines['right'].set_visible(False)

axes[0,1].spines['bottom'].set_visible(False)

axes[0,1].spines['left'].set_visible(False)

a b

图 20. 绘制右上角子图

# 右下角子图：余弦曲线 axes[1,1].plot(cos_y, theta_array, color = 'k', lw = 0.25, zorder = 1)

axes[1,1].scatter(cos_y, theta_array, marker = '.', s = 38, c=colors, edgecolor='w', zorder = 2)

# 图片美化 axes[1,1].set_ylim(0, 2 * np.pi)

axes[1,1].set_xlim(-1.2, 1.2)

axes[1,1].set_xticks(level_ticks)

axes[1,1].set_yticks(radian_ticks)

axes[1,1].tick_params(axis='x', labelrotation=90)

axes[1,1].set_yticklabels(radian_ticklabels)

axes[1,1].grid()

axes[1,1].spines['top'].set_visible(False)

axes[1,1].spines['right'].set_visible(False)

axes[1,1].spines['bottom'].set_visible(True)

axes[1,1].spines['left'].set_visible(False)

axes[1,1].set_aspect('equal', adjustable='box')

a b

图 21. 绘制右下角子图

Page 19  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 10.5 使用Plotly 绘制线图

此外，我们还可以用Plotly 绘制具有交互属性的图形，比如图 22，对应的代码如图 23。

plotly.graph_objects 是Plotly 库中的一个模块，它提供了创建和操作图形对象的类和方法。

通过go 的别名，我们可以方便地使用plotly.graph_objects 模块中的各种类和函数。在 plotly.graph_objects 模块中，有许多类可用于创建各种类型的图形，如scatter、bar、 surface 等。

通过go 模块，我们可以创建一个Figure 对象，用于容纳和管理我们的图形。Figure 对象是一个图形容器，可以添加多个轨迹 (trace)，设置整体布局和样式，并最终显示或保存图形。

fig.add_trace(go.Scatter(x=x, y=y_sin, mode='lines', name='Sine')) 的作用是向图形对象 fig 中添加一个轨迹，其中包含了一条正弦曲线的数据和样式。go.Scatter 创建了一个散点图 (scatter plot) 的轨迹对象。x=x 指定了横轴的数据，即之前生成的 x 值数组。y=y_sin 指定了纵轴的数据，即正弦函数的 y 值数组。mode='lines' 设置了散点图的显示模式为连线模式，表示将数据点用线连接起来。name='Sine' 设置了轨迹的名称为 "Sine"，在图例中显示。通过 add_trace 方法，我们将该轨迹添加到 fig 图形对象中，使得该正弦曲线在图形中显示出来。

0.0 0.5 1.0 1.5 1.5 1.0 0.5 f(x)

Sine Cosine

图 22. 用Plotly 绘制具有交互性质的曲线

Page 20  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com g import numpy as np import plotly.graph_objects as go import plotly.io as pio pio.kaleido.scope.default_format = "svg"

# 注意！请首先在Anaconda Prompt安装pip install -U kaleido # 生成 x 值 x = np.linspace(0, 2 * np.pi, 100)

# 生成正弦和余弦函数的 y 值 y_sin = np.sin(x)

y_cos = np.cos(x)

# 创建图形对象 fig = go.Figure()

# 添加正弦曲线 fig.add_trace(go.Scatter(x=x,y=y_sin,mode='lines',name='Sine'))

# 添加余弦曲线 fig.add_trace(go.Scatter(x=x,y=y_cos,mode='lines',name='Cosine'))

# 设置横轴和纵轴范围 fig.update_layout(xaxis_range=[0, 2 * np.pi], yaxis_range=[-1.5, 1.5])

# 设置横轴和纵轴标签 fig.update_xaxes(title_text='x')

fig.update_yaxes(title_text='f(x)')

# 添加网格 fig.update_xaxes(showgrid=True, gridwidth=0.25, gridcolor='lightgray')

fig.update_yaxes(showgrid=True, gridwidth=0.25, gridcolor='lightgray')

# 显示图形 fig.show()

# 将fig保存为SVG格式 fig.write_image("fig.svg")

a b e f h j k

图 23. 用Plotly 绘制线图

请大家完成下面3 道题目。

Q1. 大家可以在本章配套代码中找到图 1 对应的Matplotlib 官方提供的代码文件。本书将Python 代码文件命名为Q1_Assignment_Anatomy_of_a_figure.py。请大家给这个代码文件中的代码逐行中文注释，并在 JupyterLab 中进行探究式学习。

Q2. Matplotlib 提供丰富的可视化方案实例，图 25、图 26、图 27 大部分子图对应的代码都在如下链接中， 请大家在JupyterLab 复刻每幅子图，并补充必要注释。

https://matplotlib.org/stable/plot_types/index.html

Page 21  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com * 本章习题不提供答案。

black dimgray dimgrey gray grey darkgray darkgrey silver lightgray lightgrey gainsboro whitesmoke white snow rosybrown lightcoral indianred brown firebrick maroon darkred red mistyrose salmon tomato darksalmon coral orangered lightsalmon sienna seashell chocolate saddlebrown sandybrown peachpuff peru linen forestgreen limegreen darkgreen green lime seagreen mediumseagreen springgreen mintcream mediumspringgreen mediumaquamarine aquamarine turquoise lightseagreen mediumturquoise azure lightcyan paleturquoise darkslategray darkslategrey teal darkcyan aqua cyan darkturquoise cadetblue powderblue lightblue deepskyblue skyblue lightskyblue steelblue aliceblue dodgerblue lightslategray lightslategrey slategray slategrey lightsteelblue cornflowerblue royalblue ghostwhite lavender midnightblue navy darkblue mediumblue blue slateblue darkslateblue mediumslateblue mediumpurple rebeccapurple blueviolet indigo darkorchid darkviolet mediumorchid thistle plum violet purple darkmagenta fuchsia magenta orchid mediumvioletred deeppink hotpink lavenderblush palevioletred crimson pink lightpink darkgoldenrod goldenrod cornsilk gold lemonchiffon khaki palegoldenrod darkkhaki ivory beige lightyellow lightgoldenrodyellow olive yellow olivedrab yellowgreen darkolivegreen greenyellow chartreuse lawngreen honeydew darkseagreen palegreen lightgreen bisque darkorange burlywood antiquewhite tan navajowhite blanchedalmond papayawhip moccasin orange wheat oldlace floralwhite

图 24. Matplotlib 已定义名称的颜色

Page 22  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a) plot()

(b) scatter()

(c) bar()

(d) stem()

(e) step()

(f) fill_between()

(g) stackplot()

(h) imshow()

(i) contour()

(j) contourf()

(k) quiver()

(l) streamplot()

图 25. Matplotlib 常见可视化方案，第一组

Page 23  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a) hist()

(b) boxplot()

(c) errorbar()

(d) violinplot()

(e) eventplot()

(f) hist2d()

(g) hexbin()

(h) pie()

(i) tricontour()

(j) tricontourf()

(k) tripcolor()

(l) triplot()

图 26. Matplotlib 常见可视化方案，第二组

Page 24  |  Chapter 10 聊聊可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a) scatter()

(b) plot_surface()

(c) plot_wireframe()

(d) plot_trisurf()

(e) voxels()

(f) bar3d()

(g) contour()

(h) contour(extend3d = True)

(i) contourf()

(j) plot()

(k) contour() + plot_wireframe()

(l) stem()

图 27. Matplotlib 常见可视化方案，第三组

Page 1  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 2D and 3D Visualizations 二维和三维可视化平面上的散点图、等高线、热图

文明的传播像是星星之火可以燎原；首先是星星之火，然后是闪烁的炬火，最后是燎原烈焰，排山倒海、势不可挡。

The spread of civilization may be likened to a fire; first, a feeble spark, next a flickering flame, then a mighty blaze, ever increasing in speed and power.

—— 尼古拉·特斯拉 (Nikola Tesla)  |  发明家、物理学家  |  1856 ~ 1943

◄ Axes3D.plot_surface() 绘制三维曲面 ◄ matplotlib.pyplot.contour() 绘制等高线图，轴对象可以为三维 ◄ matplotlib.pyplot.contourf() 绘制平面填充等高线，轴对象可以为三维 ◄ numpy.cumsum() 计算给定数组中元素的累积和，返回一个具有相同形状的数组 ◄ numpy.exp() 计算给定数组中每个元素的e 的指数值 ◄ numpy.linspace() 在指定的范围内创建等间隔的一维数组 ◄ numpy.meshgrid() 生成多维网格化数组 ◄ plotly.express.data.iris() 导入鸢尾花数据集 ◄ plotly.express.imshow() 绘制可交互的热图 ◄ plotly.express.line() 创建可交互的折线图的图形 ◄ plotly.express.scatter() 创建可交互的散点图 ◄ plotly.express.scatter_3d() 创建可交互的三维散点图 ◄ plotly.graph_objects.Contour() 绘制可交互的等高线图 ◄ plotly.graph_objects.Scatter3d() 绘制可交互的散点、线图 ◄ plotly.graph_objects.Surface() 绘制可交互的三维曲面 ◄ seaborn.heatmap() 绘制热图 ◄ seaborn.load_dataset() Seaborn 库中用于加载示例数据集 ◄ seaborn.scatterplot() 创建散点图

Page 2  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 11.1 二维可视化方案

散点、线图、等高线、热图是鸢尾花书最常见的四类平面可视化方案。

► 散点图 (scatter plot)：散点图用于展示两个变量之间的关系，其中每个点的位置表示两个变量的取值。可以通过设置点的颜色、大小、形状等属性来表示其他信息。

► 线图 (line plot)：线图用于展示数据随时间或其他变量而变化的趋势。线图由多个数据点连接而成， 通常用于展示连续数据。

► 等高线图 (contour plot)：等高线图用于展示二维数据随着两个变量的变化而变化的趋势。每个数据点的值表示为等高线的高度，从而形成连续的轮廓线。

► 热图 (heatmap)：热图用于展示二维数据的值，其中每个值用颜色表示。热图常用于数据分析中，用于显示数据的热度、趋势等信息。建议使用Seaborn 库绘制热图。

上一章，我们介绍了如何用Matplotlib 和Plotly 绘制线图，本章将主要介绍散点图、平面等高线、 热图这三大类可视化方案。

## 11.2 平面散点

二维散点图是平面直角坐标系 (也叫笛卡儿坐标系) 中一种用于可视化二维数据分布的图形表示方法。它由一系列离散的数据点组成，其中每个数据点都由两个坐标值。

Matplotlib 中的scatter() 函数可以用于创建散点图。可以使用matplotlib.pyplot.scatter() 函数来指定数据点的坐标和其他绘图参数，例如颜色、大小等。请大家自行在JupyterLab 中实践图 3 给出的代码。

鸢尾花书《数学要素》第5 章专门讲解笛卡儿坐标系。

y Quadrant I Quadrant II Quadrant III Quadrant IV Origin (a, b)

图 1. 笛卡儿坐标系，平面直角坐标系什么是平面直角坐标系？

平面直角坐标系，也称笛卡儿坐标系，是一种二维空间中的坐标系统，由两条相互垂直的直线组成。其中一条直线称为x 轴，另一条直线称为y 轴。它们的交点称为原点，通常用O 表示。平面直角坐标系可以用来描述二维空间中点的位置，其中每个点都可以由一对有序实数 (a, b) 表示，分别表示点在a 轴和b 轴上的距离。x 轴和y 轴的正方向可以是任意方向，通常x 轴向右，y 轴向上。平面直角坐标系是解析几何中重要的工具，用于研究点、直线、曲线以及它们之间的关系和性质。

Page 3  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 特别推荐大家使用seaborn.scatterplot() 函数来创建二维散点图，并传递数据点的坐标和其他可选参数。还可以使用plotly.graph_objects.Scatter() 函数创建可交互的散点图，并指定数据点的坐标、样式等参数。本节下面利用Seaborn 和Plotly 这两个库中函数绘制散点图。

Seaborn 图 2 所示为利用seaborn.scatterplot() 绘制鸢尾花数据集的散点图。这两幅散点图的横轴都是花萼长度，纵轴为花萼宽度。图 2 (b) 用颜色标识鸢尾花类别。

使用 seaborn.scatterplot() 函数的基本语法如下： import seaborn as sns sns.scatterplot(data=data_frame, x="x_variable", y="y_variable")

其中，x_variable 是数据集中表示 x 轴的变量列名，y_variable 是表示 y 轴的变量列名， data_frame 是包含要绘制的数据的 Pandas DataFrame 对象。

我们还可以指定hue 参数，用于对数据点进行分组并在图中用不同颜色表示的列名，size 参数指定了数据点的大小根据 value 列的值进行缩放。除了 hue 和 size，还可以使用其他参数如 style、 palette、alpha 等来进一步定制散点图的外观和风格。

species setosa versicolor virginica Sepal length (cm)

Sepal width (cm)

Sepal length (cm)

Sepal width (cm)

(a)

(b)

图 2. 使用seaborn.scatterplot() 绘制鸢尾花数据集散点图

Page 4  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b j # 导入包 import matplotlib.pyplot as plt from sklearn.datasets import load_iris import numpy as np # 加载鸢尾花数据集 iris = load_iris()

# 提取花萼长度和花萼宽度作为变量 sepal_length = iris.data[:, 0]

sepal_width = iris.data[:, 1]

target = iris.target fig, ax = plt.subplots()

# 创建散点图 plt.scatter(sepal_length, sepal_width, c=target, cmap='rainbow')

# 添加标题和轴标签 plt.title('Iris sepal length vs width')

plt.xlabel('Sepal length (cm)')

plt.ylabel('Sepal width (cm)')

# 设置横纵轴刻度 ax.set_xticks(np.arange(4, 8 + 1, step=1))

ax.set_yticks(np.arange(1, 5 + 1, step=1))

# 设定横纵轴尺度1:1 ax.axis('scaled')

# 增加刻度网格，颜色为浅灰 ax.grid(linestyle='--', linewidth=0.25, color=[0.7,0.7,0.7])

# 设置横纵轴范围 ax.set_xbound(lower = 4, upper = 8)

ax.set_ybound(lower = 1, upper = 5)

# 显示图形 plt.show()

e f g h k iris.data iris.target

图 3. 用Matplotlib 绘制散点图

Plotly 图 4 所示为使用plotly.express.scatter() 绘制鸢尾花数据集散点图。在本章配套的Jupyter Notebook 中大家可以看到这两幅子图为可交互图像。

plotly.express.scatter() 用来可视化两个数值变量之间的关系，或者展示数据集中的模式和趋势。这个函数的基本语法如下： import plotly.express as px fig = px.scatter(data_frame, x="x_variable", y="y_variable")

fig.show()

Page 5  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 其中，data_frame 是包含要绘制的数据的 Pandas DataFrame 对象，x_variable 是数据集中表示 x 轴的变量列名，y_variable 是表示 y 轴的变量列名。可以根据需要添加其他参数，例如 color、size、symbol 等，以进一步定制散点图的外观。

最后，通过 fig.show() 方法显示绘制好的散点图。

《可视之美》将专门讲解散点图。

Sepal length (cm)

Sepal width (cm)

Sepal length (cm)

Sepal width (cm)

(a)

(b)

species setosa versicolor virginica

图 4. 使用plotly.express.scatter() 绘制鸢尾花数据集散点图

Page 6  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b e # 导入包 import numpy as np import seaborn as sns import plotly.express as px # 从seaborn中导入鸢尾花样本数据 iris_sns = sns.load_dataset("iris")

fig = px.scatter(iris_sns, x="sepal_length", y="sepal_width", width = 600, height = 600, labels={"sepal_length": "Sepal length (cm)", "sepal_width":  "Sepal width (cm)"})

# 修饰图像 fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])

xticks = np.arange(4,8+1)

yticks = np.arange(1,5+1)

fig.update_layout(xaxis = dict(tickmode = 'array', tickvals = xticks))

fig.update_layout(yaxis = dict(tickmode = 'array', tickvals = yticks))

fig.show()

fig = px.scatter(iris_sns, x="sepal_length", y="sepal_width", color="species", width = 600, height = 600, labels={"sepal_length": "Sepal length (cm)", "sepal_width": "Sepal width (cm)"})

# 修饰图像 fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])

fig.update_layout(xaxis = dict(tickmode = 'array', tickvals = xticks))

fig.update_layout(yaxis = dict(tickmode = 'array', tickvals = yticks))

fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left",x=0.01))

fig.show()

f g h

图 5. 用Plotly 绘制散点图

## 11.3 平面等高线

等高线原理等高线图是一种展示三维数据的方式，其中相同数值的数据点被连接成曲线，形成轮廓线。

形象地说，如图 6 所示，二元函数相当于一座山峰。在平行于x1x2平面在特定高度切一刀，得到的轮廓线就是一条等高线。这是一条三维空间等高线。然后，将等高线投影到x1x2平面，我们便得到一条平面等高线。

Page 7  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com x1 x2 f(x1, x2)

x1 x2 f(x1, x2)

图 6. 平行x1x2平面切f(x1, x2) 获得等高线，然后等高线投影到x1x2平面

什么是二元函数？

二元函数是指具有两个自变量和一个因变量的函数。它接受两个输入，并返回一个输出。一般表示为 y = f(x1, x2)，其中 x1 和 x2 是自变量，y 是因变量。二元函数常用于描述和分析具有两个相关变量之间关系的数学模型。它可以用于表示二维空间中的曲面、 表达物理或经济关系、进行数据建模和预测等。在可视化二元函数时，常使用三维图形或等高线图。三维图形以 x1 和 x2 作为坐标轴，将因变量 y 的值映射为曲面的高度。等高线图则使用等高线来表示 y 值的等值线，轮廓线的密集程度反映了函数值的变化。

一系列轮廓线的高度一般用不同的颜色或线型表示，使得我们可以通过视觉化方式看到数据的分布情况。如图 7 所示，将一组不同高度的等高线投影到平面便得到右侧平面等高线。右侧子图还增加了色谱条，用来展示不同等高线对应的具体高度。这一系列高度可以是一组用户输入的数值。大家可能已经发现，等高线图和海拔高度图原理完全相同。类似的图还有，等温线、等降水线、等距线等等。

Matplotlib 的填充等高线是在普通等高线的基础上添加填充颜色来表示不同区域的数据密度。可以使用contourf() 函数来绘制填充等高线。

图 7 左图则是三维等高线，这是下一章要介绍的内容。

x1 x2 f(x1, x2)

x1 x2

图 7. 将不同高度 (值) 对应的一组等高线投影到x1x2平面

网格数据为了绘制平面等高线，我们需要利用numpy.meshgrid() 产生网格数据。numpy.meshgrid()

接受一维数组作为输入，并生成二维、三维乃至多维数组来表示网格坐标。

原理上，如图 8 所示，numpy.meshgrid() 函数会将输入的一维数 (x1_array 和x2_array) 组扩展为二维数组 (xx1 和xx2)，其中一个数组的每一行都是输入数组的复制，而另一个数组的每一列都是输入数组的复制。这样，通过组合这两个二维数组的元素，就形成了一个二维网格。

Page 8  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com xx1, xx2 = numpy.meshgrid(x1, x2)

提供两个一维数组 x1 和 x2 作为输入。函数将生成两个二维数组 xx1 和 xx2，用于表示一个二维网格。

请大家在JupyterLab 中自行学习下例。

import numpy as np

x1 = np.arange(10)

# 第一个一维数组 x2 = np.arange(5)

# 第二个一维数组

xx1, xx2 = np.meshgrid(x1, x2)

x2_array (x1, x2)

numpy.linspace()

numpy.linspace()

numpy.meshgrid()

x1_array xx2 xx1 x2_array x1_array

图 8. 用numpy.meshgrid() 生成二维网络数据

Matplotlib 图 9 所示为利用Matplotlib 中等高线可视化二元函数 ( )

( )

, exp f x x = − − 。填充等高线的原理是通过在等高线之间创建颜色渐变来表示不同区域的数值范围。这样可以增强等高线图的可视化效果， 更直观地展示数据的分布和变化。

在 Matplotlib 中，填充等高线可以通过使用 contourf() 函数实现。该函数与 contour() 函数类似，但会填充等高线之间的区域。

Page 9  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

matplotlib.pyplot.contour(X,Y,Z,levels,cmap)

下面是 contour() 函数的常用输入参数： ● X：二维数组，表示数据点的横坐标。

● Y：二维数组，表示数据点的纵坐标。

● Z：二维数组，表示数据点对应的函数值或高度。

● levels：用于指定绘制的等高线层级或数值列表。

● colors：用于指定等高线的颜色，可以是单个颜色字符串、颜色序列或 colormap 对象。

● cmap：颜色映射，用于将数值映射为颜色。可以是预定义的 colormap 名称或 colormap 对象。

● linestyles：用于指定等高线的线型，可以是单个线型字符串或线型序列。

● linewidths：用于指定等高线的线宽，可以是单个线宽值或线宽序列。

● alpha：用于指定等高线的透明度。

请大家在JupyterLab 中自行学习下例。

import matplotlib.pyplot as plt import numpy as np

# 创建二维数据 x = np.linspace(-2, 2, 100)

y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2  # 示例函数，可以根据需要自定义

# 绘制等高线图 plt.contour(X, Y, Z, levels = np.linspace(0,8,16 + 1), cmap = 'RdYlBu_r')

# 添加颜色图例 plt.colorbar()

# 显示图形 plt.show()

0.4 0.3 0.2 0.1 0.0 0.1 0.2 0.3 0.4 0.4 0.3 0.2 0.1 0.0 0.1 0.2 0.3 0.4 (a)

(b)

x1 x1 x2 x2

图 9. 用Matplotlib 生成的平面 (填充) 等高线

Page 10  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b e f # 导入包 import numpy as np import matplotlib.pyplot as plt # 生成数据 x1_array = np.linspace(-3,3,121)

x2_array = np.linspace(-3,3,121)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

ff = xx1 * np.exp(- xx1**2 - xx2 **2)

# 等高线 fig, ax = plt.subplots()

CS = ax.contour(xx1, xx2, ff, levels = 20, cmap = 'RdYlBu_r', linewidths = 1)

fig.colorbar(CS)

ax.set_xlabel('$\it{x_1}$'); ax.set_ylabel('$\it{x_2}$')

ax.set_xticks([]); ax.set_yticks([])

ax.set_xlim(xx1.min(), xx1.max())

ax.set_ylim(xx2.min(), xx2.max())

ax.grid(False)

ax.set_aspect('equal', adjustable='box')

# 填充等高线 fig, ax = plt.subplots()

CS = ax.contourf(xx1, xx2, ff, levels = 20, cmap = 'RdYlBu_r')

fig.colorbar(CS)

ax.set_xlabel('$\it{x_1}$'); ax.set_ylabel('$\it{x_2}$')

ax.set_xticks([]); ax.set_yticks([])

ax.set_xlim(xx1.min(), xx1.max())

ax.set_ylim(xx2.min(), xx2.max())

ax.grid(False)

ax.set_aspect('equal', adjustable='box')

g h

图 10. 用Matplotlib 生成平面等高线，代码

Plotly 图 11 所示为利用plotly.graph_objects.Contour() 绘制的 (填充) 等高线。

Page 11  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 0.5 0.25 0.0 0.25 0.5 (a)

(b)

x1 x1 x2 x2 0.5 0.25 0.0 0.25 0.5

图 11. 用Plotly 生成的平面 (填充) 等高线

a b # 导入包 import numpy as np import matplotlib.pyplot as plt # 生成数据 x1_array = np.linspace(-3,3,121)

x2_array = np.linspace(-3,3,121)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

ff = xx1 * np.exp(- xx1**2 - xx2 **2)

# 等高线设置 levels = dict(start=-0.5,end=0.5,size=0.05)

data = go.Contour(x=x1_array,y=x2_array,z=ff, contours_coloring='lines', line_width=2, colorscale = 'RdYlBu_r', contours=levels)

# 创建布局 layout = go.Layout( width=600,   # 设置图形宽度 height=600,  # 设置图形高度 xaxis=dict(title=r'$x_1$'), yaxis=dict(title=r'$x_2$'))

# 创建图形对象 fig = go.Figure(data=data, layout=layout)

fig.show()

图 12. 用Plotly 生成平面等高线，代码

Page 12  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 11.4 热图

在 Matplotlib 中，可以使用 matplotlib.pyplot.imshow() 函数来绘制热图 (heatmap)，也叫热力图。

imshow() 函数可以将二维数据矩阵的值映射为不同的颜色，从而可视化数据的密度、分布或模式。

鸢尾花书中一般会用Seaborn 绘制静态热图，特别是在可视化矩阵运算。

seaborn.heatmap(data, vmin, vmax, cmap, annot)

下面是函数的常用输入参数： ● data：二维数据数组，要绘制的热图数据。

● vmin：可选参数，指定热图颜色映射的最小值。

● vmax：可选参数，指定热图颜色映射的最大值。

● cmap：可选参数，指定热图的颜色映射。可以是预定义的颜色映射名称或 colormap 对象。

● annot：可选参数，控制是否在热图上显示数据值。默认为 False，不显示数据值；设为 True 则显示数据值。

● xticklabels：可选参数，控制是否显示 X 轴的刻度标签。可以是布尔值或标签列表。

● yticklabels：可选参数，控制是否显示 Y 轴的刻度标签。可以是布尔值或标签列表。

请大家在JupyterLab 中自行学习下例。

import seaborn as sns import numpy as np

# 创建二维数据 data = np.random.rand(10,10)

# 绘制热图 sns.heatmap(data, vmin=0, vmax=1, cmap='viridis', annot=True, xticklabels=True, yticklabels=True)

(a)

(b)

图 13. 使用Seaborn、Plotly 热图可视化鸢尾花数据集

Page 13  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b # 导入包 import matplotlib.pyplot as plt import seaborn as sns # 从seaborn中导入鸢尾花样本数据 iris_sns = sns.load_dataset("iris")

# 绘制热图 fig, ax = plt.subplots()

sns.heatmap(data=iris_sns.iloc[:,0:-1], vmin = 0, vmax = 8, ax = ax, yticklabels = False, xticklabels = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width'], cmap = 'RdYlBu_r')

图 14. 用Seaborn 生成热图，代码

a # 导入包 import matplotlib.pyplot as plt import seaborn as sns import plotly.express as px # 从seaborn中导入鸢尾花样本数据 iris_sns = sns.load_dataset("iris")

fig = px.imshow(iris_sns.iloc[:,0:-1], text_auto=False, width = 600, height = 600, x = None, zmin=0, zmax=8, color_continuous_scale = 'viridis')

# 隐藏 y 轴刻度标签 fig.update_layout(yaxis=dict(tickmode='array',tickvals=[]))

# 修改 x 轴刻度标签 x_labels = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']

x_ticks  = list(range(len(x_labels)))

fig.update_xaxes(tickmode='array',tickvals=x_ticks, ticktext=x_labels)

fig.show()

b

图 15. 用Plotly 生成热图，代码

## 11.5 三维可视化方案

本章介绍常见四种三维空间可视化方案。图 16 所示为三维直角坐标系和三个平面。

Page 14  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 散点图 (scatter plot) 用于展示三维数据的离散点分布情况。每个数据点在三维空间中的位置由其对应的三个数值确定。通过散点图，可以观察数据点的分布、聚集程度和可能的趋势。

线图 (line plot) 可用于表示在三维空间中的曲线或路径。通过将连续的点用线段连接，可以呈现数据的演变过程或路径的形态。线图在表示运动轨迹、时间序列数据等方面很有用。

网格面图 (mesh surface plot) 展示了三维空间中表面或曲面的形状。通过将空间划分为网格，然后根据每个网格点的数值给予相应的高度或颜色，可以可视化复杂的三维数据，例如地形地貌、物理场、函数表面等。

三维等高线图 (3D contour plot) 在三维空间中绘制了等高线的曲线。这种图形通过将等高线与垂直于平面的轮廓线相结合，可以同时显示三个维度的信息。它适用于表示等值线密度、梯度分布等。

鸢尾花书《数学要素》第6 章专门介绍三维直角坐标系。

+x +y +z (a, b, c)

O (0, 0, 0)

a b yz-plane xy-plane xz-plane

图 16. 三维直角坐标系和三个平面

三维视图视角学过机械工程制图的同学知道，在三维空间中，我们可以将立体物体的投影投射到不同的平面上， 以便更好地理解其形状和结构。

以下是常见的三维立体在不同面的投影方式： ► 俯视投影 (top view) 把立体物体在垂直于其底面的平面上投影的方式。这种投影显示了物体的顶部视图，可以揭示物体在水平方向上的外形和布局。

► 侧视投影 (side view) 将立体物体在垂直于其侧面的平面上投影的方式。这种投影显示了物体的侧面视图，可以展示物体在垂直方向上的外形和结构。

► 正视投影 (front view) 把立体物体在垂直于其正面的平面上投影的方式。这种投影显示了物体的正面视图，可以展示物体在前后方向上的外形和特征。

Page 15  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 斜视投影 (isometric view) 将立体物体在等角度投射到平面上的方式。它显示了物体的斜面视图，保留了物体在三个维度上的比例关系，使观察者能够同时感知物体的长度、宽度和高度。

这些不同面的投影方式可以提供不同的视角，帮助我们从多个方面理解和分析立体物体。选择合适的投影方式取决于我们关注的特定方面和目的。特别是用Matplotlib、Plotly 绘制三维图像时，选择合适的投影方式至关重要。

在Matplotlib 中，ax.view_init(elev, azim, roll) 方法用于设置三维坐标轴的视角，也叫相机照相位置。这个方法接受三个参数：elev、azim 和 roll，它们分别表示仰角、方位角和滚动角。

► 仰角 (elevation)：elev 参数定义了观察者与 xy 平面之间的夹角，也就是观察者与 xy 平面之间的旋转角度。当 elev 为正值时，观察者向上倾斜，负值则表示向下倾斜。

► 方位角 (azimuth)：azim 参数定义了观察者绕 z 轴旋转的角度。它决定了观察者在 xy 平面上的位置。

azim 的角度范围是 −180 到 180 度，其中正值表示逆时针旋转，负值表示顺时针旋转。

► 滚动角 (roll)：roll 参数定义了绕观察者视线方向旋转的角度。它决定了观察者的头部倾斜程度。正值表示向右侧倾斜，负值表示向左侧倾斜。

通过调整这三个参数的值，可以改变三维图形的视角，从而获得不同的观察效果。例如，增加仰角可以改变观察者的俯视角度，增加方位角可以改变观察者在 XY 平面上的位置，增加滚动角可以改变观察者的头部倾斜程度。

类比的话，这三个角度和图 17 所示飞机的三个姿态角度类似。

Pitch Roll Yaw

图 17. 飞机姿态的的三个角度

如图18 所示，鸢尾花书中调整三维视图视角一般只会用elev、azim，几乎不用使用roll。

Page 16  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Elevation y z Azimuth

图18. 仰角和方位角示意图

请大家在JupyterLab 中练习如下代码，并调整仰角、方位角大小观察图像变化。

注意，ax = fig.gca(projection='3d') 已经被最新版本Matplotlib 弃用，正确的语法为ax = fig.add_subplot(projection='3d')。

a b e f g import matplotlib.pyplot as plt # 导入Matplotlib的绘图模块 fig = plt.figure()

# 创建一个新的图形窗口 ax = fig.add_subplot(projection='3d')

# 在图形窗口中添加一个3D坐标轴子图 ax.set_xlabel('x')

ax.set_ylabel('y')

ax.set_zlabel('z')

# 设置坐标轴的标签 ax.set_proj_type('ortho')

# 设置投影类型为正交投影 (orthographic projection)

ax.view_init(elev=30, azim=30)

# 设置观察者的仰角为30度，方位角为30度，即改变三维图形的视角 ax.set_box_aspect([1,1,1])

# 设置三个坐标轴的比例一致，使得图形在三个方向上等比例显示 plt.show()

# 显示图形 h

图19. 设置三维图像观察视角

Page 17  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 有关Matplotlib 三维视图视角，请参考： https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html

ax.view_init (elev=90, azim=-90)

y ax.view_init (elev=0, azim=-90)

z ax.view_init (elev=0, azim=0)

y z ax.view_init (elev=-90, azim=90)

y ax.view_init (elev=0, azim=90)

z ax.view_init (elev=0, azim=180)

y z

图20. 几个特殊视角

两种投影方法此外，大家还需要注意投影方法。上述代码采用的是正交投影。

在Matplotlib 中，ax.set_proj_type() 方法用于设置三维坐标轴的投影类型。Matplotlib 提供了两种主要的投影类型： ► 透视投影 (perspective projection) 是默认的投影类型，如图21 (a) 所示。简单来说就是近大远小，它模拟了人眼在观察远处物体时的视觉效果，使得远离观察者的物体显得较小。透视投影通过在观察者和图形之间创建一个虚拟的透视点，从而产生远近比例和景深感。设置方式为： ax.set_proj_type('persp')。

► 正交投影 (orthographic projection) 是另一种投影类型，如图21 (b) 所示。它在观察者和图形之间维持固定的距离和角度，不考虑远近关系，保持了物体的形状和大小。正交投影在某些情况下可能更适合于一些几何图形的呈现，尤其是在需要准确测量物体尺寸或进行定量分析时。设置方式为： ax.set_proj_type('ortho')。

Plotly 的三维图像也是默认透视投影，想要改成正交投影对应的语法为： fig.layout.scene.camera.projection.type = "orthographic"

图22 展示了3D 绘图时改变焦距对透视投影的影响。需要注意的是，Matplotlib 会校正焦距变化所带来的“缩放”效果。

Page 18  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 透视投影中，默认焦距为1，对应90 度的视场角 (Field of View, FOV)。增加焦距 (1 至无穷大) 会使图像变得扁平，而减小焦距 (1 至0 之间) 则会夸张透视效果，增加图像的视觉深度。当焦距趋近无穷大时，经过缩放校正后，会得到正交投影效果。

注意，鸢尾花书中三维图像绝大部分都是正交投影。

(a)

(b)

图21. 透视投影和正交投影，来源：https://github.com/rougier/scientific-visualization-book

(a) focal length = (b) focal length = 5 (c) focal length = 1 (d) focal length = 0.2

图22. 投影焦距对结果影响；参考：https://matplotlib.org/stable/gallery/mplot3d/projections.html

## 11.6 三维散点

上一章我们利用平面散点可视化鸢尾花数据集，这一节将用三维散点图可视化这个数据集。图23 所示为利用Matplotlib 绘制的三维散点图，这幅图用不同颜色表征鸢尾花分类。类似图19，请大家将图23 投影到不同平面上。

本章配套的Jupyter Notebook 还用Plotly 绘制了散点图，请大家自行学习。

Page 19  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Petal length

图23. 用Matplotlib 和绘制散点图

a b e f g # 导入包 import matplotlib.pyplot as plt import numpy as np from sklearn import datasets # 加载鸢尾花数据集 iris = datasets.load_iris()

# 取出前三个特征作为横纵坐标和高度 X = iris.data[:, :3]

y = iris.target # 创建3D图像对象 fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# 绘制散点图 ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)

# 设置坐标轴标签 ax.set_xlabel('Sepal length')

ax.set_ylabel('Sepal width')

ax.set_zlabel('Petal length')

# 设置坐标轴取值范围 ax.set_xlim(4,8); ax.set_ylim(1,5); ax.set_zlim(0,8)

# 设置正交投影 ax.set_proj_type('ortho')

# 显示图像 plt.show()

图24. 用Matplotlib 和绘制散点图，代码

Page 20  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a import plotly.express as px # 导入鸢尾花数据 df = px.data.iris()

fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length', size = 'petal_width', color='species')

fig.update_layout(autosize=False,width=500,height=500)

fig.layout.scene.camera.projection.type = "orthographic"

fig.show()

b

图25. 用Plotly 绘制散点图，代码

## 11.7 三维线图

图26 所示为利用Matplotlib 绘制“线图 + 散点图”可视化微粒的随机漫步。并且用散点的颜色渐进变化展示时间维度。本章配套的Jupyter Notebook 也用Plotly 绘制相同图像，请大家自行学习。

《数据有道》将专门介绍随机漫步。

图26. 用Matplotlib 绘制微粒随机漫步线图

什么是随机漫步？

随机漫步是指一个粒子或者一个系统在一系列离散的时间步骤中，按照随机的方向和大小移动的过程。每个时间步骤，粒子以随机的概率向前或向后移动一个固定的步长，而且每个时间步骤之间的移动是相互独立的。随机漫步模型常用于模拟不确定性和随

Page 21  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 机性的系统，例如金融市场、扩散过程、分子运动等。通过模拟大量的随机漫步路径，可以研究粒子或系统的统计特性和概率分布。

a e # 导入包 import matplotlib.pyplot as plt import numpy as np import plotly.graph_objects as go # 生成随机游走数据 num_steps = 300 t = np.arange(num_steps)

x = np.cumsum(np.random.standard_normal(num_steps))

y = np.cumsum(np.random.standard_normal(num_steps))

z = np.cumsum(np.random.standard_normal(num_steps))

# 用 Matplotlib 可视化 fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y,z,color = 'darkblue')

ax.scatter(x,y,z,c = t, cmap = 'viridis')

ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

# 设置正交投影 ax.set_proj_type('ortho')

# 设置相机视角 ax.view_init(elev = 30, azim = 120)

# 显示图像 plt.show()

# 用 Plotly 可视化 fig = go.Figure(data=go.Scatter3d( x=x, y=y, z=z, marker=dict(size=4,color=t,colorscale='Viridis'), line=dict(color='darkblue', width=2)))

fig.layout.scene.camera.projection.type = "orthographic"

fig.update_layout(width=800,height=700)

fig.show()  # 显示绘图结果 b f

图27. 用Matplotlib 和Plotly 可视化随机行走，代码

## 11.8 三维网格面

图28 所示为利用Axes3D.plot_surface() 绘制的三维网格曲面。请大家思考如何在图片中加入 colorbar。本章配套的Jupyter Notebook 也用Plotly 绘制的三维曲面，请大家自行学习。

Page 22  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图28. 用Matplotlib 绘制网格曲面

Page 23  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b # 导入包 import matplotlib.pyplot as plt import numpy as np import plotly.graph_objects as go # 生成曲面数据 x1_array = np.linspace(-3,3,121)

x2_array = np.linspace(-3,3,121)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

ff = xx1 * np.exp(- xx1**2 - xx2 **2)

# 用 Matplotlib 可视化三维曲面 fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx1, xx2, ff, cmap='RdYlBu_r')

# 设置坐标轴标签 ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('f(x1,x2)')

# 设置坐标轴取值范围 ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-0.5,0.5)

# 设置正交投影 ax.set_proj_type('ortho')

# 设置相机视角 ax.view_init(elev = 30, azim = 150)

plt.tight_layout()

plt.show()

# 用 Plotly 可视化三维曲面 fig = go.Figure(data=[go.Surface(z=ff, x=xx1, y=xx2, colorscale='RdYlBu_r')])

fig.layout.scene.camera.projection.type = "orthographic"

fig.update_layout(width=800,height=700)

fig.show()

图29. 用Matplotlib 和Plotly 可视化三维网格面，代码

## 11.9 三维等高线

图30 所示为用Matplotlib 绘制的三维等高线，这些等高线投影到水平面便得到上一章介绍的平面等高线。本章配套的Jupyter Notebook 也用Plotly 绘制的三维“曲面 + 等高线”，请大家自行学习。

鸢尾花书《可视之美》将介绍更多三维等高线的用法。

Page 24  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图30. 用Matplotlib 绘制三维等高线 a b # 导入包 import matplotlib.pyplot as plt import numpy as np import plotly.graph_objects as go # 生成曲面数据 x1_array = np.linspace(-3,3,121)

x2_array = np.linspace(-3,3,121)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

ff = xx1 * np.exp(- xx1**2 - xx2 **2)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.contour(xx1, xx2, ff, cmap='RdYlBu_r', levels = 20)

# 设置坐标轴标签 ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('f(x1,x2)')

# 设置坐标轴取值范围 ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-0.5,0.5)

# 设置正交投影 ax.set_proj_type('ortho')

# 设置相机视角 ax.view_init(elev = 30, azim = 150)

plt.tight_layout()

plt.show()

contour_settings = {"z": {"show":True,"start":-0.5, "end":0.5, "size": 0.05}} fig = go.Figure(data=[go.Surface(x=xx1,y=xx2,z=ff, colorscale='RdYlBu_r', contours = contour_settings)])

fig.layout.scene.camera.projection.type = "orthographic"

fig.update_layout(width=800, height=700)

fig.show()  # 显示绘图结果

Page 25  |  Chapter 11 二维和三维可视化  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图31. 用Matplotlib 和Plotly 可视化三维等高线，代码

请大家完成下面3 道题目。

Q1. 分别用Matplotlib、Seaborn、Plotly 绘制鸢尾花数据集，花瓣长度、宽度散点图，并适当美化图像。

Q2. 分别用Matplotlib 和Plotly 绘制如下二元函数等高线图，并用语言描述图像特点 (等高线形状、疏密分布、增减、最大值、最小值等等)。

( )

( )

( )

( )

( )

( )

( )

( )

( )

( )

( )

, , , , , , , , , , , f x x f x x f x x f x x f x x f x x f x x x x f x x f x x f x x x x f x x x x = = = + = − = + = − − = + + = − = = = + +

Q3. 请用分别用Matplotlib 和Plotly 中网格面、三维等高线可视化以上几个二元函数。

* 本章不提供答案。

Page 1  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Descriptive Statistics Using Seaborn Seaborn 可视化数据使用Seaborn 完成样本数据统计描述

理性永恒，其他一切皆有终结之时。

Reason is immortal, all else mortal.

—— 毕达哥拉斯 (Pythagoras)  |  古希腊哲学家、数学家  |  570 ~ 495 BC

◄ pandas.plotting.parallel_coordinates() 绘制平行坐标图 ◄ seaborn.boxplot() 绘制箱型图 ◄ seaborn.heatmap() 绘制热图 ◄ seaborn.histplot() 绘制频数/概率/概率密度直方图 ◄ seaborn.jointplot() 绘制联合分布和边缘分布 ◄ seaborn.kdeplot() 绘制KDE 核概率密度估计曲线 ◄ seaborn.lineplot() 绘制线图 ◄ seaborn.lmplot() 绘制线性回归图像 ◄ seaborn.pairplot() 绘制成对分析图 ◄ seaborn.swarmplo() 绘制蜂群图 ◄ seaborn.violinplot() 绘制小提琴图

Page 2  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 12.1 Seaborn

本书前文介绍用Seaborn 绘制热图。实际上，Seaborn 的真正价值体现在统计可视化上。简单来说， Seaborn 是一个用于数据可视化的Python 库，它基于Matplotlib，并提供了一组高级的绘图函数和样式设置，可以轻松创建具有吸引力和专业外观的统计图表。

Seaborn 提供了多种可视化方案，包括但不限于： ► 分布图：包括直方图、核密度图、箱线图等，用于展示数据的分布情况。

► 散点图：用于观察两个变量之间的关系，可以通过散点图添加颜色或大小编码第三个变量。

► 线性关系图：通过绘制线性回归模型的置信区间，展示两个变量之间的线性关系。

► 分类图：包括条形图、点图、计数图等，用于比较不同类别之间的数值关系。

► 矩阵图：如热图和聚类图，用于显示数据的相似性和聚类结构。

本章以鸢尾花数据为例介绍如何用Seaborn 可视化样本数据分布。

样本数据分布是指在统计学中，对于一组收集到的数据，对其进行统计和描述的方式。

一元样本数据分布是指只包含一个随机变量的样本数据分布，例如鸢尾花花萼长度。可视化一元样本分布的方法有：直方图 (histogram)、核密度估计 (Kernel Density Estimation, KDE)、毛毯图 (rug plot)、 分散图 (strip plot)、小提琴图 (violin plot)、箱型图 (box plot)、蜂群图 (swarm plot)等等。

二元样本数据分布则涉及两个随机变量，例如鸢尾花花萼长度、花萼关系之间的关系。这种分布一般叫联合分布 (joint distribution)。我们可以通过相关性系数量化联合分布。

边缘分布 (marginal distribution) 是指在多元数据分布中，对某一个或几个变量进行统计，而忽略其他变量的分布。例如，在花萼长度、花萼关系的二元数据分布中，对花萼长度的边缘分布就是仅考虑花萼长度变量的数据分布。

可视化二元样本分布的方法有散点图 (scatter plot)、散点图 + 边缘直方图、散点图 + 毛毯图、散点图 + 回归图、频率热图、二元KDE 等等图形和图形组合。

多元样本数据分布则涉及两个以上随机变量，例如鸢尾花花萼长度、花萼宽度、花瓣长度、花瓣宽度。多元样本数据的可视化方案有热图、聚类热图 (cluster map)、平行坐标图 (parallel plot)、成对特征散点图、Radviz 等等。特别地，我们还可以用协方差矩阵、相关性系数矩阵来量化随机变量之间的关系。

而热图可以用来可视化协方差矩阵、相关性系数矩阵。

除此之外，我们在采用上述可视化方案时，还可以考虑分类，比如鸢尾花种类。

下面我们来逐一展示这些统计可视化方案。

## 12.2 一元

直方图直方图是一种常用的数据可视化图表，用于显示数值变量的分布情况。如图 1 所示，将数据划分为不同的区间 (也称"柱子")，一般计算每个区间内的数据频数 (样本数量)；简单来说，这个过程就是“查

Page 3  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 数”。然后，通过绘制每个区间的柱状条形来表示相应的频数。比如，图 1 中深蓝的“柱子”对应区间的样本数量为25，因此“柱子”的高度为25。

直方图的 x 轴表示变量的取值范围，而y 轴表示频数、概率、概率密度。图 1 中深蓝的“柱子”对应的频数为25，样本总数为150，因此这个柱子对应的概率为25/150。柱子的宽度为0.2，因此这个深蓝色柱子的概率密度为25/150/0.2。

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Count Count = 25 Box

图 1. 直方图原理

图 2 所示为鸢尾花花萼长度样本数据的直方图，纵轴为频数。

如果图 2 的纵轴为概率，图 2 的这些“柱子”的高度之和为1。如果图 2 的纵轴为概率密度，图 2 的这些 “柱子”的面积之和为1。

图 2 这张图上还用ax.axvline() 绘制了花萼长度样本均值的位置。请大家修改本章配套Jupyter Notebook，将“均值 ± 标准差”这两条直线也画上去。

注意，标准差是方差的平方根。样本标准差、样本、均值三者的单位相同。

Page 4  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Count

图 2. 鸢尾花花萼长度样本数据直方图，纵轴为频数

a b # 导入包 import matplotlib.pyplot as plt import pandas as pd import seaborn as sns # 导入鸢尾花数据 iris_sns = sns.load_dataset("iris")

# 绘制花萼长度样本数据直方图 fig, ax = plt.subplots(figsize = (8, 6))

sns.histplot(data=iris_sns, x="sepal_length", binwidth=0.2, ax = ax)

# 纵轴三个选择：频率、概率、概率密度 ax.axvline(x = iris_sns.sepal_length.mean(), color = 'r', ls = '--')

# 增加均值位置竖直参考线 e

图3. 用Seaborn 绘制直方图，代码

seaborn.histplot() 是 Seaborn 库中用于绘制直方图的函数。这个函数的重要输入有， data 一般为Pandas 数据帧，x 为横轴标签。此外，stat 指定纵轴类型，比如'count'对应频数， 'probability'对应概率，'density' 对应概率密度。可以用bins 指定直方图区间数量， binwidth 定义区间宽度。

利用seaborn.histplot()绘制鸢尾花数据直方图时，如果指定hue = 'species'，我们便得到每个类别鸢尾花单独的直方图，具体如图 4 所示。seaborn.histplot() 还可以用来绘制二维直方热图，本章后文将介绍。此外，本章配套的Jupyter Notebook 还给出函数其他用法。

注意，图 4 直方图纵轴为概率密度值。

Page 5  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

0.7 0.6 0.5 0.4 0.3 0.2 0.1 0.0 Density Species setosa versicolor virginica

图 4. 鸢尾花花萼长度样本数据直方图，考虑鸢尾花分类，纵轴为概率密度

# 绘制花萼长度样本数据直方图，考虑鸢尾花分类 fig, ax = plt.subplots(figsize = (8,6))

sns.histplot(data = iris_sns,  x="sepal_length", hue  = 'species', binwidth=0.2, ax = ax, element="step", stat = 'density')

# 纵轴为概率密度 a

图5. 用Seaborn 绘制直方图，考虑鸢尾花分类，使用时须配合前文代码

在直方图中，以下是频数、概率和概率密度的确切定义如下： 频数 (frequency)：直方图中每个区间内的样本数量被称为频数。它表示了数据落入该区间的次数或计数。

概率 (probability)：是指某个事件发生的可能性。在直方图中，可以将频数除以总观测值的数量，得到每个区间的概率。这样计算得到的概率是相对频率，表示该区间中的观测值出现的相对概率。

概率密度 (probability density)：是指在概率分布函数中某一点附近单位自变量取值范围内的概率。

在直方图中，概率密度可以通过将每个区间的频数除以该区间的宽度得到。概率密度函数描述了变量的分布形状，而不是具体的概率值。

直方图可以显示数据的分布形状，如对称 (symmetry)、偏态 (skewness)、峰度 (kurtosis) 等，以及数据的中心趋势和离散程度。通过观察直方图，我们可以直观地了解数据的分布特征，如数据的集中程度、范围和异常值等。

《统计至简》第1 章将专门讲解直方图、偏态、峰度等概念。

核密度估计KDE

Page 6  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 核密度估计 (Kernel Density Estimation, KDE) 是一种非参数方法，用于估计连续变量的概率密度函数 (Probability Density Function, PDF)。它通过将每个数据点视为一个核函数 (通常是高斯核函数)，在整个变量范围内生成一系列核函数，然后将这些核函数进行平滑和叠加，从而得到连续的概率密度估计曲线。具体原理如图 6 所示。

图 6. 高斯核密度估计原理

核密度估计的目标是通过在数据点附近生成高斯分布的核函数，捕捉数据的分布特征和结构。具体地说，每个数据点的核函数会在其附近产生一个小的高斯分布，然后将所有核函数叠加在一起。通过调整核函数的带宽参数，可以控制估计曲线的平滑程度和敏感度。

本书第27 章将介绍如何使用Statsmodels 中的核密度估计函数；《统计至简》第17 章将专门讲解核密度估计原理。

图 7 所示为利用seaborn.kdeplot() 绘制的鸢尾花花萼长度数据高斯核密度估计PDF。可以这样理解， 图 7 是图 2 直方图的“平滑”处理结果。

图 7 的横轴还有用seaborn.rugplot() 绘制的毛毯图。毛毯图常用于展示数据在一维空间上的分布。它通过在坐标轴上绘制短线，或称为"毛毯"，表示数据点的位置和密度。这种图形通常用于辅助其他类型的图表，如直方图或密度图，以更清晰地显示数据的分布特征。

5.0 6.0 7.0 8.0 Sepal length (cm)

4.0 0.6 0.5 0.4 0.3 0.2 0.1 0.0 Density

图 7. 鸢尾花花萼长度样本数据核密度估计

Page 7  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 5.0 6.0 7.0 8.0 Sepal length (cm)

4.0 0.5 0.4 0.3 0.2 0.1 0.0 Density Species setosa versicolor virginica

图 8. 鸢尾花花萼长度样本数据核密度估计，考虑鸢尾花分类

在用seaborn.kdeplot() 绘制花萼长度样本数据核密度估计曲线时，我们还可以用hue 来绘制三类鸢尾花种类各自的分布，具体如图 8 所示。

换个角度理解图 8，图 8 中三条曲线叠加便得到图 7。图 9 这幅图更好地解释了这一点。用 seaborn.kdeplot() 绘制这幅图时，需要设置multiple="stack"。

4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

0.6 0.5 0.4 0.3 0.2 0.1 0.0 Density Species setosa versicolor virginica

图 9. 三条KDE 曲线叠加特别地，在利用绘制核密度估计曲线时，如果设置multiple = 'fill'，我们便获得图 10。图中每条曲线准确来说，都是“后验概率 (posterior)”。而这个后验概率值可以用来完成分类。也就是说，给定具体花萼长度，比较该点处红蓝绿三条曲线对应的宽度，最宽的曲线对应的鸢尾花种类可以作为该点的鸢尾花分类预测值。因此，这个后验概率值也叫“成员值 (membership score)”。

想要理解后验概率这个概念，需要大家深入理解贝叶斯定理，《统计至简》第18、19 章将专门介绍利用贝叶斯定理完成分类。

Page 8  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 1.0 0.8 0.6 0.4 0.2 0.0 Posterior Species setosa versicolor virginica 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

图 10. 后验概率曲线

b # 绘制花萼长度样本数据，高斯核密度估计 fig, ax = plt.subplots(figsize = (8,6))

sns.kdeplot(data=iris_sns, x='sepal_length', bw_adjust=0.3, fill = True)

sns.rugplot(data=iris_sns, x='sepal_length')

# 绘制花萼长度样本数据，高斯核密度估计，考虑鸢尾花类别 fig, ax = plt.subplots(figsize = (8,6))

sns.kdeplot(data=iris_sns, x='sepal_length', hue = 'species', bw_adjust=0.5, fill = True)

sns.rugplot(data=iris_sns, x='sepal_length', hue = 'species')

# 绘制花萼长度样本数据，高斯核密度估计，考虑鸢尾花类别，堆叠 fig, ax = plt.subplots(figsize = (8,6))

sns.kdeplot(data=iris_sns, x='sepal_length', hue= 'species', multiple='stack', bw_adjust=0.5)

# 绘制后验概率 (成员值)

fig, ax = plt.subplots(figsize = (8,6))

sns.kdeplot(data=iris_sns, x='sepal_length', hue='species', bw_adjust=0.5, multiple = 'fill')

e

图11. 用Seaborn 绘制高斯核密度估计，使用时须配合前文代码

什么是贝叶斯定理？

贝叶斯定理是一种用于更新概率推断的数学公式。它描述了在获得新信息后如何更新我们对某个事件发生概率的信念。贝叶斯定理基于先验概率（我们对事件发生的初始信念）和条件概率（给定新信息的情况下事件发生的概率），通过计算后验概率（在获得新信息后事件发生的概率）来实现更新。贝叶斯定理在统计学、机器学习和人工智能等领域具有广泛应用。

分散点图

Page 9  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 分散点图 (strip plot) 一般用来可视化一组分类变量与连续变量的关系。在分散图中，每个数据点通过垂直于分类变量的轴上的一个点表示，连续变量的取值则沿着水平轴展示。这种图形通常用于可视化分类变量和数值变量之间的关系，以观察数据的分布、聚集和离散程度，同时也可以用于比较不同分类变量水平下的数值变量。

seaborn.stripplot() 是 Seaborn 库中用于绘制分散点图的函数。需要注意的是，分散点图适用于较小的数据集，当数据点重叠较多时，可考虑使用 seaborn.swarmplot() 函数来避免重叠点问题。

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Petal length Species setosa versicolor virginica

图 12. 分散点图

# 绘制鸢尾花花萼长度分散点图 fig, ax = plt.subplots(figsize = (8,6))

sns.stripplot(data=iris_sns, x='sepal_length', y='species', hue='petal_length', palette='RdYlBu_r', ax = ax)

a

图13. 用Seaborn 绘制分散点图，考虑鸢尾花分类，使用时须配合前文代码

蜂群图蜂群图 (swarm plot) 是一种用于可视化分类变量和数值变量关系的图表类型。它通过在分类轴上对数据进行分散排列，避免数据点的重叠，以展示数值变量在不同类别下的分布情况。每个数据点在分类轴上的位置表示其对应的数值大小，从而呈现出数据的密度和分布趋势。

蜂群图可以帮助我们比较不同类别之间的数值差异和趋势，适用于数据探索、特征分析和可视化报告等场景。图 14 所示为利用seaborn.swarmplot() 绘制蜂群图。图 15 所示为考虑鸢尾花分类的蜂群图。

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

图 14. 蜂群图

Page 10  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Species setosa versicolor virginica

图 15. 蜂群图，考虑鸢尾花分类

# 绘制花萼长度样本数据，蜂群图 fig, ax = plt.subplots(figsize = (8,4))

sns.swarmplot(data=iris_sns, x="sepal_length", ax = ax)

# 绘制花萼长度样本数据，蜂群图，考虑分类 fig, ax = plt.subplots(figsize = (8,4))

sns.swarmplot(data=iris_sns, x="sepal_length", y = 'species', hue = 'species', ax = ax)

a b

图16. 用Seaborn 绘制蜂群图，使用时须配合前文代码

箱型图箱型图 (box plot) 是一种常用的统计图表，用于展示数值变量的分布情况和异常值检测。它通过绘制数据的五个关键统计量 (最小值、第一四分位数Q1、中位数Q2、第三四分位数Q3、最大值) 以及可能存在的异常值来提供对数据的直观概览。

Q1   1.5 × IQR Q3 + 1.5 × IQR Q1 25 percentile Q3 75 percentile Interquartile range (IQR)

Q2, median 50 percentile Outliers Outliers

图 17. 箱型图原理

Page 11  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 什么是四分位？

四分位是统计学中用于描述数据集分布的概念，将数据按大小顺序分成四等份。第一个四分位数 Q1 表示25%的数据小于或等于它，第二个四分位数 Q2 是中位数，表示50%的数据小于或等于它，第三个四分位数 Q3 表示75%的数据小于或等于它。四分位可以帮助了解数据的中心趋势、分散程度和异常值。四分位与盒须图、离群值检测等统计分析方法密切相关。

图 18 所示为利用seaborn.boxplot() 绘制的鸢尾花花萼长度样本数据的箱型图。图 19 所示为考虑鸢尾花分类的箱型图。

箱型图的主要元素包括： ► 箱体 (box)：由第一四分位数Q1和第三四分位数Q3之间的数据范围组成。箱体的高度表示数据的四分位距IQR = Q3 − Q1，箱体的中线表示数据的中位数。

► 须 (whisker)：延伸自箱体的线段，表示数据的整体分布范围。通常，须的长度为 1.5 倍的四分位距。但是，仔细观察图 18，我们会发现用Seaborn 绘制的箱型图左须距离Q1、右须距离Q3宽度并不相同。根据Seaborn 的技术文档，左须、右须延伸至该范围 [Q1 − 1.5 × IQR, Q3 + 1.5 × IQR] 内最远的样本点，具体如图 20 所示。更为极端的样本会被标记为异常值。

► 异常值 (outliers)：范围 [Q1 − 1.5 × IQR, Q3 + 1.5 × IQR] 之外的数据点，被认为是异常值，可能表示数据中的极端值或异常观测。

通过观察箱型图，可以快速了解数据的中心趋势、离散程度以及是否存在异常值等关键信息。

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

图 18. 箱型图

4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Species setosa versicolor virginica

图 19. 箱型图，考虑鸢尾花分类

Page 12  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Q1   1.5 × IQR Q3 + 1.5 × IQR Q1 Q3 Q2 Q1 Q3 Q2

图 20. Seaborn 绘制箱型图左须、右须位置

# 绘制鸢尾花花萼长度箱型图 fig, ax = plt.subplots(figsize = (8,2))

sns.boxplot(data=iris_sns, x='sepal_length', ax = ax)

# 绘制鸢尾花花萼长度箱型图，考虑鸢尾花分类 fig, ax = plt.subplots(figsize = (8,3))

sns.boxplot(data=iris_sns, x='sepal_length', y = 'species', ax = ax)

b a

图21. 用Seaborn 绘制箱型图，使用时须配合前文代码

小提琴图小提琴图 (violin plot) 是一种用于可视化数值变量分布的图表类型。它结合了核密度估计曲线和箱型图的特点，可以同时展示数据的分布形状、中位数、四分位数和离群值等信息。seaborn.violinplot() 是 Seaborn 库中用于绘制小提琴图的函数。

小提琴图的主要组成部分包括： ► 背景形状：由核密度估计曲线组成，表示数据在不同值上的概率密度。

► 中位数线：位于核密度估计曲线的中间位置，表示数据的中位数。

► 四分位线：分别位于核密度估计曲线的 25% 和 75% 位置，表示数据的四分位范围。

► 离群值点：位于核密度估计曲线之外的离群值数据点。

图 22 所示为用seaborn.violinplot() 绘制的鸢尾花花萼长度样本数据的小提琴图。图 23 为考虑鸢尾花分类的小提琴图。图 24 所示为“蜂群图 + 小提琴图”可视化方案。

4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

图 22. 小提琴图

Page 13  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

Species setosa versicolor virginica

图 23. 小提琴图，考虑鸢尾花分类 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

Species setosa versicolor virginica

图 24. 蜂群图 + 小提琴图，考虑鸢尾花分类

# 绘制花萼长度样本数据，小提琴图 fig, ax = plt.subplots(figsize = (8,2))

sns.violinplot(data=iris_sns, x='sepal_length', ax = ax)

# 绘制花萼长度样本数据，小提琴图，考虑分类 fig, ax = plt.subplots(figsize = (8,4))

sns.violinplot(data=iris_sns, x='sepal_length', y='species', ax = ax)

# 蜂群图 + 小提琴图，考虑鸢尾花分类 sns.catplot(data=iris_sns, x='sepal_length', y='species', kind='violin', color='.9', inner=None)

sns.swarmplot(data=iris_sns, x='sepal_length', y='species', size=3)

b a

图25. 用Seaborn 绘制小提琴图，使用时须配合前文代码

Page 14  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 12.3 二元

散点图散点图是一种数据可视化图表，用于展示两个变量之间的关系。它通过在坐标系中以点的形式表示每个数据点，横轴代表一个变量，纵轴代表另一个变量。散点图可以帮助我们观察和分析数据点之间的趋势、分布和相关性。通过观察点的聚集程度和分布形状，我们可以推断两个变量之间的关系类型，如线性正相关、线性负相关、线性无关，甚至是非线性关系。

图 26 所示为利用seaborn.scatterplot() 绘制的散点图，散点图的横轴为花萼长度、纵轴为花萼宽度。

通过观察散点趋势，可以发现花萼长度、花萼宽度似乎似乎存在线性正相关。但是实际情况可能并非如此。本章最后将通过线性相关性系数进行量化确认。

图 26 这幅图中，我们还用毛毯图分别可视化花萼长度、花萼宽度的分布情况。

用不同颜色散点代表鸢尾花分类，我们便得到图 27 所示散点图。观察这幅图中蓝色点，即setosa 类，我们可以发现更强的线性正相关性。

2.0 2.5 3.0 3.5 4.0 4.5 Sepal width (cm)

1.5 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

4.0

图 26. 散点图 + 毛毯图

Page 15  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

4.0 Species setosa versicolor virginica 2.0 2.5 3.0 3.5 4.0 4.5 Sepal width (cm)

1.5

图 27. 散点图 + 毛毯图，考虑鸢尾花分类

# 鸢尾花散点图 + 毛毯图 fig, ax = plt.subplots(figsize = (4,4))

sns.scatterplot(data=iris_sns, x='sepal_length', y='sepal_width')

sns.rugplot(data=iris_sns, x='sepal_length', y='sepal_width')

# 鸢尾花散点图 + 毛毯图，考虑鸢尾花分类 fig, ax = plt.subplots(figsize = (4,4))

sns.scatterplot(data=iris_sns, x='sepal_length', y='sepal_width', hue = 'species')

sns.rugplot(data=iris_sns, x='sepal_length', y='sepal_width', hue = 'species')

a b

图28. 用Seaborn 绘制二元散点图 + 毛毯图，使用时须配合前文代码

二元直方图本章前文，我们将一元样本数据划分成不同区间便可以绘制一元直方图。类似地，如果我们把图 26 所示平面划分成如图 29 所示一系列格子，计算每个格子中的样本数，我们便可以绘制类似图 30 二元直方图。显然，这种可视化方案并不理想。一方面“柱子”的高度很难确认，而且固定某个特定视角之后，一些较矮的“柱子”必定会被遮挡。因此，在实践中我们常常使用二元直方热图作为可视化方案。

Page 16  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 29. 二元直方图原理

图 30. 二元直方图，柱状图可视化方案

二元直方热图由一个矩形网格组成，其中每个单元格的颜色代表了对应的数据频数、概率、概率密度。通常，行和列代表两个不同的随机变量，而单元格中的颜色强度表示频数、概率、概率密度。

二元直方热图可以帮助我们观察两个变量之间的关系以及它们的分布模式。通过观察颜色的变化和集中区域，我们可以得出关于两个变量之间的相关性、联合分布和潜在模式的初步结论。

所示为利用seaborn.displot() 绘制的二元直方热图，横轴为鸢尾花花萼长度，纵轴为花萼宽度。如图 32 所示，二元直方热图沿着某个方向压缩便得到一元直方图；反过来看，直方图沿着特定方向展开便得到二元直方热图。

Page 17  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length (cm)

2.0 2.5 3.0 3.5 4.0 4.5 Sepal width (cm)

图 31. 鸢尾花花萼长度、花萼宽度的二元直方热图 Sepal width (cm)

Sepal length (cm)

Collapse Expand Collapse Expand

图 32. 一元直方图和二元直方热图之间关系

# 鸢尾花二元频率直方热图 sns.displot(data=iris_sns, x="sepal_length", y="sepal_width", binwidth=(0.2, 0.2), cbar=True)

a

图33. 用Seaborn 绘制二元直方热图，使用时须配合前文代码

Page 18  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 联合分布前文的高斯核函数KDE 也可以用在估算二元联合分布。图 34 所示为seaborn.kdeplot() 绘制鸢尾花花萼长度、花萼宽度联合分布概率密度估计等高线。图 34 (b) 还考虑了鸢尾花三个不同类别。

Sepal width (cm)

Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

(a)

(b)

Species setosa versicolor virginica

图 34. 鸢尾花花萼长度、花萼宽度的联合分布，高斯核密度估计

什么是联合分布？

联合分布是统计学中用于描述两个或多个随机变量同时取值的概率分布。它提供了关于多个变量之间关系的信息，包括它们的联合概率、相互依赖程度以及共同变化的模式。联合分布可以以多种形式呈现，如概率质量函数（离散变量）或概率密度函数（连续变量）。通过分析联合分布，我们可以洞察变量之间的相关性、条件概率以及预测和推断未来事件的可能性。联合分布在概率论、统计建模、数据分析和机器学习等领域具有广泛应用。

# 联合分布概率密度等高线 sns.displot(data=iris_sns, x='sepal_length', y='sepal_width', kind='kde')

# 联合分布概率密度等高线，考虑分布 sns.kdeplot(data=iris_sns, x='sepal_length', y='sepal_width', hue = 'species')

a b

图35. 用Seaborn 绘制联合分布概率密度等高线，使用时须配合前文代码

边缘分布图 36 所示为利用seaborn.jointplot() 可视化“联合分布 + 边缘分布”。

seaborn.jointplot() 函数用于创建联合图，结合了两个变量的散点图和各自的边缘分布图。它可以帮助我们同时可视化两个变量之间的关系以及它们的边缘分布。seaborn.jointplot() 函数默认情况下会绘制散点图和边缘直方图。散点图展示了两个变量之间的关系，而边缘直方图则分别显示了每个变量的边缘分布情况。

Page 19  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 本章配套Jupyter Notebook 还提供seaborn.jointplot() 其他几种可视化方案，请大家自行学习。

Sepal width (cm)

Sepal width (cm)

Sepal length (cm)

Sepal length (cm)

(a)

(b)

图 36. 鸢尾花花萼长度、花萼宽度的联合分布和边缘分布

什么是边缘分布？

边缘分布是指在多变量数据集中，针对单个变量的分布情况。它表示了某个特定变量在与其他变量无关时的概率分布。边缘分布可以通过将多变量数据集投影到某个特定变量的轴上来获得。通过分析边缘分布，我们可以了解每个变量单独的分布特征，包括均值、方差、偏度、峰度等统计量，以及分布的形状和模式。边缘分布对于探索数据集的特征、进行单变量分析和了解数据的单个方面非常有用。

# 联合分布、边缘分布 sns.jointplot(data=iris_sns, x='sepal_length', y='sepal_width', kind = 'kde', fill = True)

# 联合分布、边缘分布，考虑鸢尾花分类 sns.jointplot(data=iris_sns, x='sepal_length', y='sepal_width', hue = 'species', kind='kde')

a b

图37. 用Seaborn 绘制联合分布和边缘分布，使用时须配合前文代码

线性回归图 38 所示为利用seaborn.lmplot() 绘制的鸢尾花花萼长度、花萼宽度之间的线性回归关系图。

seaborn.lmplot() 函数默认情况下会绘制散点图和拟合的线性回归线。散点图展示了两个变量之间的关系，而线性回归线表示了拟合的线性关系。

除了基本语法外，seaborn.lmplot() 还支持其他参数，例如hue 参数用于指定一个额外的分类变量， 可以通过不同的颜色展示不同类别的数据点和回归线。

《数据有道》第9、10 章专门介绍线性回归。

Page 20  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal width (cm)

Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

(a)

(b)

图 38. 鸢尾花花萼长度、花萼宽度的线性回归关系

# 可视化线性回归关系 sns.lmplot(data=iris_sns, x='sepal_length', y='sepal_width')

# 可视化线性回归关系，考虑鸢尾花分类 sns.lmplot(data=iris_sns, x='sepal_length', y='sepal_width', hue = 'species')

b a

图39. 用Seaborn 可视化线性回归关系，使用时须配合前文代码

## 12.4 多元

分散点图、小提琴图我们当然可以使用一元可视化方案展示多元数据的特征，如所示。但是这两幅图最致命的缺陷是仅仅展示单个特征分布，并没有展示特征之间的联系。下面我们聊聊其他能够可视化多元特征之间关系的可视化方案。

Page 21  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length Sepal width Petal length Petal width Sepal length Sepal width Petal length Petal width Species setosa versicolor virginica Species setosa versicolor virginica

图 40. 分散点图、小提琴图，多特征

iris_melt = pd.melt(iris_sns, 'species', var_name='measurement')

# 数据从宽格式 (wide format) 转换为长格式 (long format)

# 绘制多特征分散图 sns.stripplot(data=iris_melt, x='value', y='measurement', hue='species', dodge=True, alpha=.25, zorder=1, legend=True)

plt.grid()

# 绘制多特征小提琴图 sns.violinplot(data=iris_melt, x='value', y='measurement', hue='species', dodge=True, alpha=.25, zorder=1, legend=True)

plt.grid()

b a

图41. 用Seaborn 绘制多特征分散点图、小提琴图，使用时须配合前文代码

聚类热图 seaborn.clustermap()函数用于创建聚类热图，它能够可视化数据集中的聚类结构和相似性。聚类热图使用层次聚类算法对数据进行聚类，并以热图的形式展示聚类结果。

聚类热图的原理是通过计算数据点之间的相似性（例如欧几里得距离或相关系数），然后使用层次聚类算法将相似的数据点分组为聚类簇。层次聚类将数据点逐步合并形成聚类树状结构，根据相似性的距离进行聚类的层次化过程。聚类热图将聚类树状结构可视化为热图，同时显示数据点的排序和聚类关系。

Page 22  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length Sepal width Petal length Petal width

图 42. 鸢尾花数据集，聚类热图

# 聚类热图 sns.clustermap(iris_sns.iloc[:,:-1], cmap = 'RdYlBu_r', vmin = 0, vmax = 8)

a

图43. 用Seaborn 绘制聚类热图，使用时须配合前文代码

《机器学习》将专门介绍各种聚类算法。

什么是聚类？

机器学习中的聚类是一种无监督学习方法，用于将数据集中的样本按照相似性进行分组或聚集。聚类算法通过自动发现数据的内在结构和模式，将相似的样本归为一类，从而实现数据的分组和分类。聚类的目标是使得同一类别内的样本相似度高，而不同类别之间的样本相似度低。聚类算法通常基于样本之间的距离或相似性度量进行操作，例如欧几里得距离、余弦相似度等。常见的聚类算法包括K 均值聚类、层次聚类、DBSCAN、高斯混合模型等。

成对特征散点图 seaborn.pairplot() 函数用于创建成对特征散点图矩阵，可视化多个变量之间的关系和分布。它会将数据集中的每对特征绘制为散点图，并展示变量之间的散点关系和单变量的分布。

Page 23  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length (cm)

Sepal width (cm)

Petal length (cm)

Petal width (cm)

Sepal length (cm)

Sepal width (cm)

Petal length (cm)

Petal width (cm)

Species 0, Setosa 1, Versicolor 2, Virginica

图 44. 鸢尾花数据成对特征散点图，考虑分类标签

seaborn.pairplot() 函数会根据数据集中的每对特征生成散点图，并以网格矩阵的形式展示。对角线上的图形通常是单变量的直方图或核密度估计图，表示每个变量的分布情况。非对角线上的图形是两个变量之间的散点图，展示它们之间的关系。

此外，seaborn.pairplot()函数还支持其他参数，例如hue 参数用于根据一个分类变量对散点图进行颜色编码，使不同类别的数据点具有不同的颜色。

通过使用seaborn.pairplot()函数，我们可以轻松地可视化多个变量之间的关系和分布。这对于探索变量之间的相关性、识别数据中的模式和异常值等非常有用。

# 绘制成对特征散点图 sns.pairplot(iris_sns, hue = 'species')

a

图45. 用Seaborn 绘制成对特征散点图，使用时须配合前文代码

Page 24  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 平行坐标图平行坐标图是一种可视化多个连续变量之间关系的图形方法。它使用平行的垂直线段来表示每个变量，这些线段相互平行并沿着水平轴排列。每个变量的值通过垂直线段在对应的轴上进行表示。

在平行坐标图中，每个数据样本由一条连接不同垂直线段的折线表示。这条折线的形状和走势反映了数据样本在不同变量之间的关系。通过观察折线的走势，我们可以识别出变量之间的相对关系，例如正相关、负相关或无关系。同时，我们也可以通过折线的位置和形状来比较不同样本之间的差异。

Setosa Versicolor Virginica Sepal length Sepal width Petal length Petal width

图 46. 鸢尾花数据，平行坐标图平行坐标图常用于数据探索、特征分析和模式识别等任务。它能够帮助我们发现多个变量之间的关系、观察变量的分布模式，并对数据样本进行可视化比较。此外，通过添加颜色映射或其他可视化元素，还可以在平行坐标图中显示附加信息，例如类别标签或异常值指示。

注意，目前Seaborn 并没有绘制平行坐标图的工具，本章配套的Jupyter Notebook 中采用的是 pandas.plotting.parallel_coordinates() 函数。

from pandas.plotting import parallel_coordinates # 可视化函数来自pandas # 绘制平行坐标图 parallel_coordinates(iris_sns, 'species', colormap=plt.get_cmap("Set2"))

plt.show()

a b

图47. 用Pandas 绘制平行坐标图，使用时须配合前文代码

类似平行坐标图的可视化方案还有安德鲁斯曲线 (Andrews curves)。在安德鲁斯曲线中，每个特征被映射为一个三角函数（通常是正弦函数和余弦函数），并按照给定的顺序排列。本章配套的Jupyter Notebook 用pandas.plotting.andrews_curves() 绘制了鸢尾花样本数据的安德鲁斯曲线。

Page 25  |  Chapter 12 Seaborn 可视化数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 量化多特征样本数据任意两个随机变量关系的最方便的工具莫过于协方差矩阵、相关性系数矩阵。

这是上一章已经介绍过的内容，本章不再赘叙。

请大家完成下面2 道题目。

Q1. 请大家分别绘制鸢尾花花萼宽度、花瓣长度、花瓣宽度的直方图、KDE 概率密度估计。

Q2. 请大家绘制鸢尾花花萼长度、花瓣长度的散点图、二元直方热图、联合分布KDE 等高线。

* 本章题目不提供答案。

Page 1  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Fundamentals of NumPy 聊聊NumPy 本节的核心是用NumPy 产生不同类型数组

重要的不是生命的长度，而是深度。

It is not the length of life, but the depth.

—— 拉尔夫·沃尔多·爱默生 (Ralph Waldo Emerson)  |  美国思想家、文学家  | 1942 ~ 2018

◄ math.ceil() 向上取整 ◄ matplotlib.cm 是Matplotlib 中的一个模块，用于颜色映射 ◄ matplotlib.patches.Circle() 创建正圆图形 ◄ matplotlib.pyplot.contour() 绘制等高线图 ◄ matplotlib.pyplot.contourf() 绘制填充等高线图 ◄ matplotlib.pyplot.scatter() 绘制散点图 ◄ numpy.arange()根据指定的范围以及设定的步长，生成一个等差数组 ◄ numpy.array() 创建array 数据类型 ◄ numpy.empty() 创建指定形状NumPy 空 (未初始化) 数组 ◄ numpy.empty_like() 创建一个与给定输入数组具有相同形状的未初始化数组 ◄ numpy.exp()计算括号中元素的自然指数 ◄ numpy.eye() 用于创建单位矩阵 ◄ numpy.full() 创建一个指定形状且所有元素值相同的数组 ◄ numpy.full_like() 创建一个与给定输入数组具有相同形状且所有元素值相同的数组 ◄ numpy.linspace() 在指定的间隔内,返回固定步长等差数列 ◄ numpy.logspace() 创建在对数尺度上均匀分布的数组 ◄ numpy.meshgrid() 创建网格化数据 ◄ numpy.ones_like() 用来生成和输入矩阵形状相同的全1 矩阵 ◄ numpy.random.multivariate_normal() 用于生成多元正态分布的随机样本 ◄ numpy.random.uniform() 产生满足连续均匀分布的随机数 ◄ numpy.zeros()返回给定形状和类型的新数组，用零填充 ◄ numpy.zeros_like() 用来生成和输入矩阵形状相同的零矩阵 ◄ seaborn.heatmap() 绘制热图

Page 2  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 13.1 什么是NumPy?

NumPy 是Python 科学计算中非常重要的一个库，它提供了快速、高效的多维数组对象及其操作方法，是众多其他科学计算库的基础。

NumPy 最重要的功能之一是提供了高效的多维数组对象ndarray，可以用来表示向量、矩阵和更高维的数组。它是Python 中最重要的科学计算数据结构，支持广泛的数值运算和数学函数操作。

此外，如果大家需要处理有标签、多维数组数据的话，推荐使用Xarray。Xarray 可以看作是在 ndarray 的基础上，增加了标签和元数据的功能。Xarray 可以对多个数组进行向量化计算，避免了循环操作，提高了计算效率。Xarray 提供了多种统计分析函数，可以方便地对多维数组数据进行统计分析。本书将不会展开讲解Xarray。

NumPy 提供了多种数组操作方法，包括数组索引、切片、迭代、转置、变形、合并等，以及广播 (broadcasting) 机制，使得数组操作更加方便、高效。这些话题是本书后续要展开讲解的内容。本书后文会专门讲解广播。

NumPy 提供了丰富的数学函数库，包括三角函数、指数函数、对数函数、逻辑函数、统计函数、随机函数等，能够满足大多数科学计算需要。

“鸢尾花书”中《数学要素》一册将大量使用这些函数库来可视化常见函数。

NumPy 支持多种文件格式的读写操作，包括文本文件、二进制文件、CSV 文件等。NumPy 基于C 语言实现，因此可以利用底层硬件优化计算速度，同时还支持多线程、并行计算和向量化操作，使得计算更加高效。

NumPy 提供了丰富的线性代数操作方法，包括矩阵乘法、求逆矩阵、特征值分解、奇异值分解等， 可以方便地解决线性代数问题。

本书中会简要介绍这些常见线性代数操作，详细讲解请大家参考“鸢尾花书”中的《矩阵力量》一册。

NumPy 可以与Matplotlib 库集成使用，方便地生成各种图表，如线图、散点图、柱状图等。相信大家在本书前文已经看到基于NumPy 数据绘制的平面、三维图像。

NumPy 提供了一些常用的数据处理方法，如排序、去重、聚合、统计等，方便对数据进行预处理。

即便如此，“鸢尾花书”中我们更常用Pandas 处理数据，本书后续将专门介绍Pandas。

Python 中许多数据分析和机器学习的库都是基于NumPy 创建。Scikit-learn 是一个流行的机器学习库，它基于NumPy、SciPy 和Matplotlib 创建，提供了各种机器学习算法和工具，如分类、回归、聚类、降维等。PyTorch 是一个开源的机器学习框架，它基于NumPy 创建，提供了张量计算和动态计算图等功能，可以用于构建神经网络和其他机器学习算法。TensorFlow 是一个深度学习框架，它基于NumPy 创建，提供了各种神经网络算法和工具，包括卷积神经网络、循环神经网络等。

“鸢尾花书”中的《数据有道》专门讲解回归、降维这两类机器学习算法，而《机器学习》一册则侧重分类、聚类。

Page 3  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 13.2 手动构造数组

从numpy.array() 说起我们可以利用numpy.array() 手动生成一维、二维、三维等数组。下面首先介绍如何使用 numpy.array() 这个函数。

numpy.array(object, dtype)

这个函数的重要输入参数： ● object 转换为数组的输入数据，可以是列表、元组、其他数组或类似序列的对象。

● dtype 参数用于指定数组的数据类型。如果不指定dtype 参数，则NumPy 会自动推断数组的数据类型。

请大家在JupyterLab 中自行学习下例。

import numpy as np

# 从列表中创建一维数组 arr1 = np.array([1, 2, 3, 4])

# 指定数组的数据类型 arr2 = np.array([1, 2, 3, 4], dtype=float)

# 从元组中创建二维数组 arr3 = np.array([(1, 2, 3), (4, 5, 6)])

# 指定最小维度 arr4 = np.array([1, 2, 3, 4], ndmin=2)

NumPy 中的array 是什么？

在NumPy 中，array 是一种多维数组对象，它可以用于表示和操作向量、矩阵和张量等数据结构。array 是NumPy 中最重要的数据结构之一，它支持高效的数值计算和广播操作，可以用于处理大规模数据集和科学计算。与Python 中的列表不同，array 是一个固定类型、固定大小的数据结构，它可以支持多维数组操作和高性能数值计算。array 的每个元素都是相同类型的，通常是浮点数、 整数或布尔值等基本数据类型。在创建array 时，用户需要指定数组的维度和类型。例如，可以使用numpy.array() 函数创建一个一维数组或二维数组，也可以使用numpy.zeros() 函数或numpy.ones() 函数创建指定大小的全0 或全1 数组，还可以使用 numpy.random 模块生成随机数组等。除了基本操作之外，NumPy 还提供了许多高级的数组操作，例如数组切片、数组索引、数组重塑、数组转置、数组拼接和分裂等。

本节配套的Jupyter Notebook 文件BK_2_Topic_4.01_1.ipynb，请大家边读正文边在Notebook 中探究学习。

首先定义两个可视化函数。

Page 4  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np import seaborn as sns import matplotlib.pyplot as plt import math from matplotlib import cm # 定义二维数组可视化函数 def visualize_2D(array, title, vmax, vmin):

fig_width  = math.ceil(array.shape[1] * 0.5)

fig_length = math.ceil(array.shape[0] * 0.5)

fig, ax = plt.subplots(figsize=(fig_width, fig_length))

sns.heatmap(array, vmax = vmax, vmin = vmin, annot = True,      # 增加注释 fmt = ".0f",       # 注释数值的格式 square = True,     # 热图方格为正方形 cmap = 'RdYlBu_r', # 指定色谱 linewidths = .5,   # 方格线宽 cbar = False,      # 不显示色谱条 yticklabels=False, # 不显示纵轴标签 xticklabels=False, # 不显示横轴标签 ax = ax)           # 指定绘制热图的轴 f e

图1. 自定义函数，可视化二维数组

a b # 定义一维数组可视化函数 def visualize_1D(array, title): fig, ax = plt.subplots()

colors = cm.RdYlBu_r(np.linspace(0,1,len(array)))

for idx in range(len(array)): circle_idx = plt.Circle((idx, 0), 0.5, facecolor=colors[idx], edgecolor = 'w')

ax.add_patch(circle_idx)

ax.text(idx, 0, s = str(array[idx]), horizontalalignment = 'center', verticalalignment = 'center')

ax.set_xlim(-0.6, 0.6 + len(array))

ax.set_ylim(-0.6, 0.6)

ax.set_aspect('equal', adjustable='box')

ax.axis('off')

f e g h

图2. 自定义函数，可视化一维数组

Page 5  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 手动生成一维数组在NumPy 中，一维数组是最基本的数组类型，也被称为一维ndarray。它只有一个维度，并且可以包含多个元素，其中每个元素都是相同的数据类型。

图 3 所示为利用numpy.array() 生成的一维数组。这个数组的形状为 (7, )，长度为7，维度为1。和本书前文介绍的list 一样，NumPy 数组的索引也是从0 开始。下一话题专门讲解NumPy 数组索引和切片。再次强调，如图 3 所示，本书可视化一维数组时用圆形。

3  2  1 a = numpy.array([-3, -2, -1, 0, 1, 2, 3])

Index axis = 0

图 3. 手动生成一维数组

a b # 定义一维数组 a_1D = np.array([-3, -2, -1, 0, 1, 2, 3])

print(a_1D)

print(a_1D.shape)

print(len(a_1D))

print(a_1D.ndim)

print(a_1D.size)

# 可视化 visualize_1D(a_1D, '手动，一维')

f e

图4. 一维NumPy 数组，使用时配合前文代码

下面区分一下形状、长度、维度、大小这四个特征： ► 形状：可以使用shape 属性来获取数组的形状，即每个维度上的大小，例如，如果数组arr 是一个二维数组，则可以使用arr.shape 来获取其形状。

► 长度：可以使用len()函数来获取数组的长度，例如，如果数组arr 是一个一维数组，则可以使用 len(arr)来获取其长度。

► 维数：可以使用ndim 属性来获取数组的维数，例如，如果数组arr 是一个二维数组，则可以使用 arr.ndim 来获取其维数。

► 大小：可以使用size 属性来获取数组的大小，即所有元素的个数，例如，如果数组arr 是一个二维数组，则可以使用arr.size 来获取其大小。

手动生成二维数组图 5 所示为利用numpy.array() 生成的二维数组。利用V 方法，大家可以发现图 5 中数组的维度都是 2。此外，numpy.matrix() 专门用来生成二维矩阵，请大家自行学习。

请大家注意图 5 中中括号 [] 的数量。特别强调，本书中，行向量、列向量都被视作特殊的二维数组。也就是说，行向量是一行多列矩阵，而列向量是多行一列矩阵。

Page 6  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 3  2  1 3  2  1 numpy.array([[-3, -2, -1],[0,  1,  2]])

numpy.array([[-3, -2, -1, 0,  1,  2]])

numpy.array([[-3],[-2],[-1],[0],[1],[2],[3]])

axis = 1 axis = 0 axis = 1 axis = 0 axis = 0 axis = 1

图 5. 手动生成二维数组

a b # 定义二维数组 a_2D = np.array([[-3, -2, -1], [0,  1,  2]])

print(a_2D)

# 可视化 visualize_2D(a_2D, '手动，二维', 3, -3)

print(a_2D.shape)

print(a_2D.shape[0])  # 行数 print(a_2D.shape[1])  # 列数 print(a_2D.ndim)

print(a_2D.size)

print(len(a_2D))

f e g h

图6. 二维NumPy 数组，形状为 (2, 3)，使用时配合前文代码

a b # 定义二维数组，行向量 (两层中括号)

a_row_vector = np.array([[-3, -2, -1, 0, 1, 2, 3]])

# 可视化 visualize_2D(a_row_vector, '手动，行向量', 3, -3)

print(a_row_vector.shape)

print(a_row_vector.ndim)

图7. 二维NumPy 数组，形状为 (1, 7)，使用时配合前文代码

a b # 定义二维数组，列向量 a_col_vector = np.array([[-3], [-2], [-1], [0], [1], [2], [3]])

# 可视化 visualize_2D(a_col_vector, '手动，列向量', 3, -3)

print(a_col_vector.shape)

print(a_col_vector.ndim)

图8. 二维NumPy 数组，形状为 (7, 1)，使用时配合前文代码

Page 7  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 手动生成三维数组图 9 所示为利用numpy.array() 生成的三维数组，这个数组的形状为 (2, 3, 4)，也就是2 页、3 行、4 列。Jupyter Notebook 文件展示如何获取三维数组的第0 页和第1 页。

3D array 2D array 2D array axis = 2 axis = 1 axis = 0

图 9. 手动生成三维数组

a b # 定义三维数组 a_3D = np.array([[[-12, -11, -10, -9], [-8,  -7,  -6,  -5], [-4,  -3,  -2,  -1]], [[0,   1,   2,   3], [4,   5,   6,   7], [8,   9,   10,  11]]])

print(a_3D.shape)

print(a_3D.ndim)

# 可视化 visualize_2D(a_3D[0], '手动，三维，第一页', 12, -12)

print(a_3D[0].shape)

visualize_2D(a_3D[1], '手动，三维，第二页', 12, -12)

e f

图10. 三维NumPy 数组，形状为 (2, 3, 4)，使用时配合前文代码

我们也可以用numpy.array() 将列表list 转化为NumPy 数组。

a b # 一维数组 list_1D  = [-3, -2, -1, 0, 1, 2, 3]

array_1D = np.array(list_1D)

print(array_1D.shape)

# 二维数组 list_2D  = [[-3, -2, -1, 0, 1, 2, 3]]

array_2D = np.array(list_2D)

print(array_2D.shape)

# 三维数组 list_3D  = [[[-3, -2, -1, 0, 1, 2, 3]]]

array_3D = np.array(list_3D)

print(array_3D.shape)

图11. 将列表list 转化为NumPy 数组

Page 8  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 13.3 生成数列

在NumPy 中我们常用以下三个函数生成数列： ► numpy.arange(start, stop, step)。生成等差数列，从起始值start 开始，以步长step 递增，直到结束值 stop (不包含stop)。例如，numpy.arange(1, 11, 2) 将生成一个等差数列 [1, 3, 5, 7, 9]。实际上， numpy.arange() 和前文介绍的range() 函数颇为相似。

► numpy.linspace(start, stop, num, endpoint)。生成等间距数列，从起始值start 开始，到结束值stop 结束，num 指定数列的长度 (元素的个数)，默认为50。endpoint 参数指定是否包含结束值。例如， numpy.linspace(1, 10, 5) 生成一个等间距数列 [1, 3.25, 5.5, 7.75, 10]。

► numpy.logspace(start, stop, num, endpoint, base)：生成等比数列，从base 的start 次幂开始，到base 的stop 次幂结束，num 指定数列的长度，默认为50。endpoint 和dtype 参数与numpy.linspace() 函数相同。例如，numpy.logspace(0, 4, 5, base=2) 将生成一个等比数列 [1, 2, 4, 8, 16]。

相信大家对numpy.linspace() 函数已经不陌生，本书前文在讲可视化时已经介绍过这个函数。我们经常会在二维可视化中用到numpy.linspace()。

什么是数列？

数列是指一列按照一定规律排列的数，它通常用一个公式来表示，也可以用递推关系式来定义。数列中的每个数称为数列的项， 用an来表示第n 项。数列在数学中具有广泛的应用，它是许多数学分支的基础，如数学分析、概率论、统计学、离散数学和计算机科学等。在数学中，数列是一种有序的集合，通常用于研究数学对象的性质和行为，例如函数、级数、微积分和代数等。数列可以分为等差数列、等比数列和通项公式不规则数列等几种类型。等差数列的项之间的差是固定的，比如1、2、3、4 … 100。等比数列的相邻项之间的比是固定的，比如2、4、8、16 … 2048。

代码示例结果 import numpy as np np.arange(5)

array([0, 1, 2, 3, 4])

np.arange(5, dtype = float)

array([0., 1., 2., 3., 4.])

np.arange(10,20)

array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

np.arange(10,20,2)

array([10, 12, 14, 16, 18])

np.arange(10,20,2, dtype = float)

array([10., 12., 14., 16., 18.])

np.linspace(0, 5, 11)

array([0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5. ])

np.logspace(0, 4, 5, base=10)

array([1.e+00, 1.e+01, 1.e+02, 1.e+03, 1.e+04])

np.logspace(0, 4, 5, base=2)

array([ 1.,  2.,  4.,  8., 16.])

## 13.4 生成网格数据

本书前文提过numpy.meshgrid() 函数。numpy.meshgrid() 可以生成多维网格数据，它可以将多个一维数组组合成一个 N 维数组，并且可以方便地对这个 N 维数组进行计算和可视化。

在科学计算中，常常需要对多维数据进行可视化，比如绘制 3D 曲面图、等高线图等。

numpy.meshgrid() 可以方便地生成网格数据，使得我们可以对多维数据进行可视化。

Page 9  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 对于二元函数f(x1, x2)，我们可以使用 numpy.meshgrid() 生成横坐标和纵坐标的网格点，然后计算每个网格点的函数值，最后将网格点和对应的函数值作为输入，绘制出如图 12 所示的 3D 曲面图。

《可视之美》将介绍如何生成图 12 这幅图。

如图 13 所示，numpy.meshgrid() 还可以用来生成三维网格数据。在《可视之美》一册中，大家可以看到大量利用三维网格数据完成的可视化方案。

x2 x1 f(x1, x2)

x2 x1

图 12. 三维空间看二维网络状坐标

(x1, x2, x3)

x3 array

图 13. 三维网格

Page 10  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np import matplotlib.pyplot as plt x1_array = np.linspace(-3, 3, 21)

x2_array = np.linspace(-3, 3, 21)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

# 二元函数 ff = xx1 * np.exp(-xx1**2 - xx2**2)

print(xx1.shape)

# 可视化 fig = plt.figure()

ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(xx1, xx2, ff, rstride=1, cstride=1, color = 'grey')

ax.scatter(xx1, xx2, ff, c = ff, cmap = 'RdYlBu_r')

ax.set_proj_type('ortho')

plt.show()

e f

图14. 可视化二元函数

## 13.5 特殊数组

表 1 总结NumPy 中常用来生成特殊数组的函数、用途、示例。表 1 第二列都是由ChatGPT 生成的答案。请大家在JupyterLab 中练习使用这些函数。

表 1. 用NumPy 函数生成特殊数组函数用途代码示例 numpy.empty()

numpy.empty() 创建一个指定大小的、未初始化的数组的函数。它返回一个数组对象，其元素的值是随机的，取决于数组在内存中的位置。

因此，使用numpy.empty()创建的数组的值是不确定的。

import numpy as np np.empty([4,4])

numpy.empty_like()

numpy.empty_like() 创建与给定数组具有相同形状和数据类型的未初始化数组的函数。它返回一个新的数组对象，其元素的值是随机的，取决于数组在内存中的位置。因此，使用 numpy.empty_like()创建的数组的值是不确定的。

import numpy as np A = np.array([[1, 2, 3], [4, 5, 6]])

np.empty_like(A)

numpy.eye()

numpy.eye() 创建一个二维数组，表示单位矩阵的函数。它返回一个N × N 的矩阵，其中对角线上的元素为1，其他元素为0。可以通过指定参数N，来指定矩阵的大小。

import numpy as np np.eye(5)

numpy.full()

numpy.full() 创建一个指定大小和给定值的数组的函数。它返回一个数组对象，其所有元素都初始化为指定的值。可以通过指定参数来指定数组的大小和数据类型，以及所填充的值。

import numpy as np np.full((3,3), np.inf)

Page 11  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com numpy.full_like()

numpy.full_like() 创建与给定数组具有相同形状和数据类型，且所有元素都是指定值的数组的函数。它返回一个新的数组对象，其所有元素都初始化为指定的值。可以通过指定参数来指定所填充的值。

import numpy as np A = np.array([[1, 2, 3], [4, 5, 6]])

np.full_like(A, 100)

numpy.ones()

numpy.ones() 创建一个指定大小的全1 数组的函数。它返回一个数组对象，其所有元素都是1。

可以通过指定参数来指定数组的大小和数据类型。

import numpy as np np.ones((5,5))

numpy.ones_like()

numpy.ones_like() 创建与给定数组具有相同形状和数据类型，且所有元素都是1 的数组的函数。它返回一个新的数组对象，其所有元素都是1。可以通过指定参数来指定所创建数组的数据类型。

import numpy as np A = np.array([[1, 2, 3], [4, 5, 6]])

np.ones_like(A)

numpy.zeros()

numpy.zeros() 创建一个指定大小的全0 数组的函数。它返回一个数组对象，其所有元素都是 0。可以通过指定参数来指定数组的大小和数据类型。

import numpy as np np.zeros((5,5))

numpy.zeros_like()

numpy.zeros_like()是一个用于创建与给定数组具有相同形状和数据类型，且所有元素都是0 的数组的函数。它返回一个新的数组对象，其所有元素都是0。可以通过指定参数来指定所创建数组的数据类型。

import numpy as np A = np.array([[1, 2, 3], [4, 5, 6]])

np.zeros_like(A)

什么是单位矩阵？

单位矩阵是一个非常特殊的方阵，它的对角线上的元素全都是1，而其余元素全都是0。常用符号表示单位矩阵的是I 或者E，它的大小由下标表示，例如，I2表示2 × 2 的单位矩阵。类似地，I3表示3 × 3 的单位矩阵，以此类推。单位矩阵是在矩阵运算中非常重要的一个概念，它可以被看作是矩阵乘法中的“1”，即任何矩阵与单位矩阵相乘，其结果都是该矩阵本身。单位矩阵在许多应用中都有广泛的应用，例如，单位矩阵可以用来表示标准正交基等。在计算矩阵的逆时，单位矩阵也起到了关键作用，因为一个矩阵A 的逆矩阵可以通过A 和单位矩阵的运算来计算，即AA−1 = A−1A = I。

## 13.6 随机数

NumPy 中还有大量产生随机数的函数。图 15 所示为满足二元连续均匀分布、二元高斯分布的随机数。请大家翻阅帮助文档了解这些函数的用法，并在JupyterLab 中动手实践。表 1 总结NumPy 中常用随机数发生器函数和随机数分布图像。

“鸢尾花书”《统计至简》一册将专门讲解各种常用概率分布。

Page 12  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a)

(b)

图 15. 分别满足二元连续均匀分布、二元高斯分布的随机数

a b import numpy as np import matplotlib.pyplot as plt # 生成随机数，服从连续均匀分布 num = 2000 X_uniform = np.random.uniform(low=-3, high=3, size=(num,2))

fig, ax = plt.subplots(figsize = (5,5))

ax.scatter(X_uniform[:,0],  # 散点横轴坐标 X_uniform[:,1],  # 散点纵轴坐标 s = 100,         # 散点大小 marker = '.',    # 散点marker样式 alpha = 0.5,     # 透明度 edgecolors = 'w')# 散点边缘颜色 ax.set_aspect('equal', adjustable='box')

ax.set_xlim(-3, 3)

ax.set_ylim(-3, 3)

ax.set_xticks((-3,0,3))

ax.set_yticks((-3,0,3))

图16. 服从连续均匀的随机数

Page 13  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np import matplotlib.pyplot as plt # 生成随机数，服从二元高斯分布 num = 2000 mu    = np.array([0, 0])      # 质心 rho   = 0  # 相关性系数 Sigma = np.array([[1, rho], [rho, 1]])  # 协方差矩阵 X_binormal = np.random.multivariate_normal(mu, Sigma, size=num)

fig, ax = plt.subplots(figsize = (5,5))

ax.scatter(X_binormal[:,0], X_binormal[:,1], s = 100, marker = '.', alpha = 0.5, edgecolors = 'w')

ax.set_aspect('equal', adjustable='box')

ax.set_xlim(-3, 3)

ax.set_ylim(-3, 3)

ax.set_xticks((-3,0,3))

ax.set_yticks((-3,0,3))

图17. 服从二元高斯分布随机数

表 2. 常用随机数发生器随机数服从的分布函数随机数分布图像连续均匀分布 numpy.random.uniform()

均匀整数 numpy.random.randint()

Beta 分布 numpy.random.beta()

泊松分布 numpy.random.poisson()

Page 14  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 指数分布 numpy.random.exponential()

几何分布 numpy.random.geometric()

二项分布 numpy.random.binomial()

正态分布 numpy.random.normal()

多元正态分布 numpy.random.multivariate_normal()

对数正态分布 numpy.random.lognormal()

学生t-分布 numpy.random.standard_t()

Dirichlet 分布 numpy.random.dirichlet()

概率统计中，随机是什么意思？

在概率统计中，随机指的是一个事件的结果是不确定的，而且每种可能的结果出现的概率是可以计算的。随机事件是由各种随机变量所描述的，随机变量是一个具有不确定结果的数学变量，其值取决于随机事件的结果。概率统计学家使用随机变量和概率分布来描述随机事件的结果和出现的概率。随机事件的结果可能是离散的，例如掷骰子的结果是1、2、3、4、5 或6，也可能是连续的，例如衡量人的身高或重量。概率统计学家使用各种数学方法和技术，例如概率、期望值和方差等，来分析和理解随机事件和随机变量的性质和行为。概率统计的研究在现代科学和工程中有着广泛的应用，例如金融、生物学、医学、物理学等领域。

什么是随机数发生器？

随机数生成器是一种用于生成随机数的计算机程序或硬件设备。随机数生成器可分为真随机数生成器和伪随机数生成器两种。真随机数生成器的输出完全基于物理过程，如大气噪声、放射性衰变或者热噪声等，其生成的随机数序列是完全随机且不可预测的。真随机数生成器通常需要专门的硬件设备支持。伪随机数生成器则使用计算机算法生成伪随机数，其看似随机，但是实际上是可预测的，因为它们是由固定的算法和种子值生成的。伪随机数生成器通常使用伪随机数序列和随机种子，以便在需要时生成

Page 15  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 随机数。随机数生成器在计算机科学、加密学、模拟实验、游戏设计、统计分析等领域中被广泛使用。在加密学中，随机数生成器通常用于生成安全密钥和初始化向量等关键数据，以保证加密算法的强度和安全性。在模拟实验和游戏设计中，随机数生成器用于模拟不可预测的因素，如掷骰子、扑克牌等。

## 13.7 数组导入、导出

numpy.savetxt() 可以把numpy array 写成txt、CSV 文件。numpy.genfromtxt() 可以用来读入txt、 CSV 文件。图 18 所示为鸢尾花表格和热图。大家在本书后文，特别是在《矩阵力量》一册中会看到，我们大量使用热图可视化矩阵运算。

5.1 3.5 1.4 0.2 4.9 3.0 1.4 0.2 4.7 3.2 1.3 0.2 4.6 3.1 1.5 0.2 5.0 3.6 1.4 0.2 5.4 3.9 1.7 0.4 4.6 3.4 1.4 0.3 5.0 3.4 1.5 0.2 4.4 2.9 1.4 0.2 4.9 3.1 1.5 0.1 5.4 3.7 1.5 0.2 4.8 3.4 1.6 0.2 4.8 3.0 1.4 0.1 4.3 3.0 1.1 0.1 5.9 3.0 5.1 1.8 ...

...

...

...

图 18. 鸢尾花数据表格和热图

Page 16  |  Chapter 13 聊聊NumPy  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np import matplotlib.pyplot as plt import seaborn as sns from sklearn.datasets import load_iris from numpy import genfromtxt # 导入鸢尾花数据 iris = load_iris()

# 将numpy array存成CSV文件 np.savetxt("Iris_data.csv", iris.data, delimiter=",")

# 将 CSV 文件读入存成numpy array Iris_Data_array = genfromtxt('Iris_data.csv', delimiter=',')

# 可视化 fig, ax = plt.subplots(figsize = (5,5))

sns.heatmap(Iris_Data_array,   # 鸢尾花数据数组 cmap = 'RdYlBu_r', # 指定色谱 ax = ax,           # 指定轴 vmax = 8,          # 色谱最大值 vmin = 0,          # 色谱最小值 xticklabels = [],  # 不显示横轴标签 yticklabels = [],  # 不显示纵轴标签 cbar = True)       # 显示色谱条

图19. 用热图可视化鸢尾花数据

请大家完成下面3 道题目。

Q1. 用至少两种办法生成一个3 × 4 二维NumPy 数组，数组的每个值都是10。

Q2. 利用numpy.meshgrid() 和 matplotlib.pyplot.contour() 绘制二元函数 ( )

( )

, exp f x x = − − 的平面等高线。

Q3. 在 [0, 1] 范围内生成1000 个满足连续均匀随机数，并用matplotlib.pyplot.hist()绘制频率直方图。

* 题目答案在Bk1_Ch13_02.ipynb。

Page 1  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Indexing and Slicing NumPy Arrays NumPy 索引和切片获取数组的部分成分

做数学的艺术在于找到包含所有普遍性萌芽的特殊情况。

The art of doing mathematics consists in finding that special case which contains all the germs of generality.

—— 大卫·希尔伯特 (David Hilbert)  |  德国数学家  |  1862 ~ 1943

◄ numpy.concatenate() 沿指定轴将多个数组连接成一个新的数组 ◄ numpy.copy() 深拷贝数组，对新生成的对象修改删除操作不会影响到原对象 ◄ numpy.newaxis 在使用它的位置上为数组增加一个新的维度，可以用于在指定位置对数组进行扩展或重塑 ◄ numpy.r_() 用于按行连接数组 ◄ numpy.reshape() 用于重新调整数组的形状 ◄ numpy.squeeze() 从数组的形状中删除大小为1 的维度，从而返回一个形状更紧凑的数组 ◄ numpy.take() 根据指定的索引从数组中获取元素，创建一个新的数组来存储这些元素 ◄ numpy.vstack() 将多个数组按行堆叠

Page 2  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 14.1 什么是索引、切片?

这个话题聊一聊NumPy 数组的索引 (indexing) 和切片 (slicing)。简单来说，数组中的某个元素可以通过索引来访问。切片指的是从数组中提取“子数组”的操作。

需要注意的是，NumPy 数组使用基于0 的整数索引。此外，NumPy 的切片操作返回的是原数组的视图 (view) 而不是副本 (copy)，因此对切片操作所得到的数组进行修改会直接影响到原数组。本话题后续将专门讲解视图和副本之间的区别。

本节配套的Jupyter Notebook 文件是Bk1_Ch14_01.ipynb。

## 14.2 一维数组索引、切片

索引一维数组可以使用索引来访问和操作数组中的某个元素。如图 1 所示，索引是一个整数值，它指定了要访问的元素在数组中的位置。一维数组的索引从0 开始，到数组长度 (len(a)) 减1 结束。如图 1 所示，想要取出数组a 的第一个元素，可以用a[0] 或 a[-11]。a[-1] 或a[10] 则取出数组a 的最后一个元素。请大家在Bk1_Ch14_01.ipynb 尝试取出数组不同位置元素。

Index a = numpy.arange(-5, 5 + 1)

3  2  1 5  4 3  2  1 5  4 a[0]

a[1]

a[2]

a[-3]

a[-2]

a[-1]

图 1. 一维数组的索引

行向量、列向量上一个话题特别强调过，本书中行向量、列向量都被视作特殊的二维数组。也就是说，行向量是一行多列矩阵，而列向量是多行一列矩阵。

在 NumPy 中， numpy.newaxis 是一个特殊的索引，用于增加数组的维度。它的作用是在数组的某个位置添加一个新的轴，从而改变数组的维度。

Page 3  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 具体来说，使用 numpy.newaxis 将会在数组的一个指定位置添加一个新的维度。如图 2 所示，对于一个一维数组 a，我们可以使用 a[:, numpy.newaxis] 将其转换为一个二维数组，其中新的维度被添加在列的方向上。这个操作将会把数组变成一个列向量。

a[numpy.newaxis, :] 则把一维数组变成行向量。本书后文还会介绍利用numpy.reshape() 函数完成 “升维”及其他变形。Bk1_Ch14_01.ipynb 还给出其他“升维”方法，请大家自行学习。

3  2  1 5  4 a = numpy.arange(-5, 5 + 1)

(11,)

1D array 2D array a[:, numpy.newaxis]

(1, 11), 1 × 11 a[numpy.newaxis, :]

numpy.squeeze()

numpy.squeeze()

(11, 1), 11 × 1 图 2. 一维数组“升维”

相反地，在NumPy 中，numpy.squeeze() 函数用于从数组的形状中删除单维度的条目。这意味着它可以去掉数组中的长度为1 的维度，并返回一个新的数组，其维度数目更少。

例如，对于一个形状为 (1, 3, 1, 5) 的四维数组，可以使用 numpy.squeeze(a) 函数将其转换为形状为 (3, 5) 的二维数组，其中长度为1 的第1 和第3 维被删除。如果在调用 numpy.squeeze() 时指定了参数 axis，则只有该轴上长度为1 的维度会被删除。

numpy.squeeze() 函数可以帮助我们简化数组的形状，使其更符合我们的需求。在某些情况下，例如在机器学习模型的输入中，我们需要使用具有特定形状的数组，而 numpy.squeeze() 可以帮助我们将数据变形为所需的形状。

切片切片访问一维数组中的“子数组”，即多个元素。切片是一个包含开始索引和结束索引的范围，用冒号分隔。开始索引指定要获取的第一个元素的位置，结束索引指定要获取的最后一个元素的位置+1。

图 3 所示为一维数组连续切片。图 4 中，将步长设为2 分别提取数组中的奇数、偶数。图 5 中，将步长设为-1 将数组倒序排序。Bk1_Ch14_01.ipynb 中还给出其他步长设置，请大家自行学习。

Page 4  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 5  4 a[1:3]

a[[1,2]]

5  4 a[0:3]

a[:3]

a[[0,1,2]]

a[-3:]

a[8:]

图 3. 一维数组连续切片 5  4 a[1::2]

a[::2]

4  2 5  3

图 4. 一维数组以固定步长切片，步长为2 a[::-2]

5  4 2  3 a[::-1]

图 5. 一维数组倒序

整数索引、切片在NumPy 中，可以使用整数索引来访问和修改数组中的元素。整数索引是一种非常基本的索引方法，它允许使用一个整数或整数数组来访问数组的元素。

使用整数索引时，大家可以传递一个整数来访问数组的单个元素，或者传递一个整数数组来访问数组的多个元素。大家已经在图 1 看到这一点。

Page 5  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 如果传递一个整数数组，则该数组的每个元素将被视为索引，从而返回一个新的数组，该数组包含原始数组中相应索引处的元素。如图 6 所示，整数索引为数组 [0, 1, 2, -1]，我们提取一维数组的第1、 2、3 和最后一个 (-1) 元素，结果还是一维数组。

同时，我们可以用numpy.r_[0:3, -1]构造一个数组，也能提取相同的元素组合。numpy.r_() 是一个用于将切片对象转换为一个沿着第一个轴堆叠的 NumPy 数组的函数。它可以在数组创建和索引时使用。它的作用类似于 numpy.concatenate() 和 numpy.vstack()，但是使用切片对象作为索引来方便快捷地创建数组。

5  4 a[[0, 1, 2, -1]]

5  4 a[np.r_[0:3, -1]]

图 6. 一维数组整数索引，输入为数组

布尔索引、切片布尔索引 (Boolean indexing) 是一种使用布尔值来选择数组中的元素的技术。在使用布尔索引时，可以通过一些条件来生成一个布尔数组，该布尔数组与要索引的数组具有相同的形状，然后使用该布尔数组来选择要访问的数组元素。图 7 所示为利用布尔值切片我们分别提取数组中大于1、小于0 的元素。

a[a > 1]

a[a < 0]

5  4 5  4

图 7. 一维数组布尔值切片

## 14.3 视图 vs 副本

在NumPy 中，有两种不同的方式来创建新的数组对象：视图 (view) 和副本 (copy)。

视图是原始数组的一个新视图，而副本是原始数组的一个新副本。它们的区别在于它们如何处理原始数据的内存和共享。

视图是原始数组的一个新视图，一种重新排列、重新解释。视图是原始数组共享相同的数据，不会创建新的内存。换句话说，视图是原始数组的一个不同的“窗口”，它可以访问原始数组的相同数据块。

当对视图进行更改时，原始数组也会发生相应的更改。

副本则是原始数组的一份完整的拷贝，修改副本不会影响原始数组。当对数组进行切片或使用 numpy.copy() 方法时，将生成一个副本。副本的创建可以使用numpy.copy() 方法或者numpy.array()

函数的参数copy = True 来实现。

如图 8 所示，本节之前的各种索引、切片方法实际上创建的都只是原数组的视图，改变这些视图就会修改原数组，并“牵一发动全身”地改变所有视图。而numpy.copy() 则创建了全新的内存，即副本。

Page 6  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a = numpy.arange(-5, 5 + 1)

3  2  1 5  4 a[0]

a[-1]

a[numpy.newaxis, :]

a[::2]

5  3 a[np.r_[0:3, -1]]

5  4 a[a < 0]

5  4 a[::2].copy()

5  3 a[a < 0].copy()

5  4

图 8. 视图，还是副本？

在Bk1_Ch14_01.ipynb 这个示例中，首先创建了一个一维数组 a，然后创建了一个切片视图 s，该视图选择了数组 a 中的第二个和第三个元素。接下来，将视图中的第一个元素设置为 1000，这也会修改原始数组 a 中的元素。最后，用a.copy() 创建了一个整数数组索引副本 c，该副本选择了数组 a 中的第二个和第四个元素。然后，将副本中的第一个元素设置为 888，但这不会修改原始数组 a 中的元素。本章后文的二维、三维数组在视图、副本方面的性质和一维数组完全一致。

可以使用numpy.may_share_memory() 函数来判断两个数组是否共享内存。

在NumPy 中，还有一些函数需要注意视图和副本的问题，比如numpy.reshape()、 numpy.transpose()、numpy.ravel()、numpy.flatten() 等等。这个话题非常重要，本书后文还会涉及。

## 14.4 二维数组索引、切片

取出单一元素要取出二维NumPy 数组中特定索引的元素，可以使用索引操作符 [] 来访问。可以将需要访问的元素的行索引和列索引作为参数传递给这个操作符。图 9 所示为从二维数组a 中取出单一元素，a[0, 0] 代表第0 行、第0 列。请大家特别注意a[[1], [2]] 的结果为一维数组。

Page 7  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 5  4  3 7  6 2  1 a[0,0]

5  4  3 7  6 2  1 a[1,2]

5  4  3 7  6 2  1 a[[1],[2]]

array([0])

a[1][2]

图 9. 取出单一元素

取出行要取出二维NumPy 数组中特定行的元素，也是使用索引操作符 [] 来访问。你可以将需要访问的行的索引作为第一个参数传递给这个操作符，用冒号 : 表示需要访问的列范围。图 10 所示，取出第0 行， 只需a[0]，结果为一维数组。而a[[0], :] 取出第0 行，结果为二维数组。

5  4  3 7  6 5  4  3 5  4  3 7  6 2  1 a[0]

a[0,:]

5  4  3 7  6 2  1 a[[0],:]

a[0,np.newaxis]

5  4  3 7  6 2  1 a[[0,2]]

a[[0,2],:]

7  6 5  4  3 5  4  3 5  4  3 7  6

图 10. 取出行

取出列类似地，如图 11 所示，我们也可以取出特定列。本书前文提过，numpy.newaxis 是一个常用的 NumPy 函数，它用于在数组中添加一个新的维度。具体来说，numpy.newaxis 用于在现有数组的指定位置插入一个新的维度，从而改变数组的形状。

注意，在NumPy 多维数组的索引和切片操作中，省略号 ... 可以用于代替多个连续冒号 :，从而简化操作。具体来说，省略号可以用于表示在某个维度上使用完整的切片范围。需要注意的是，省略号只能在索引或切片操作的开头、结尾或中间使用，而不能重复出现。此外，当数组的维度比较大时，省略号可以显著提高代码的可读性和简洁性，因为它避免了写很多个冒号 : 的重复代码。

Page 8  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 5  4  3 7  6 2  1 a[:,[0,2,4]]

a[:,0::2]

5  3 5  4  3 7  6 2  1 a[:,0]

a[ ,0]

7  2 5  4  3 7  6 2  1 a[:,[0]]

a[:,0,np.newaxis]

5  4  3 7  6 2  1 a[np.newaxis,:,0]

7  2

图 11. 取出列

图 12 所示为取出特定行列组合的方法。

5  4  3 7  6 2  1 a[1,2::]

5  4  3 7  6 2  1 5  4  3 7  6 2  1 a[::2,:-1:2]

a[:,[0,2]][[0, 2], :]

a[[0, 2], :][:,[0,2]]

a[np.ix_([0, 2], [0, 2])]

a[1::,[0,2,4]]

a[1::,0::2]

图 12. 取出特定的行列组合

图 12 中，numpy.ix_() 是 NumPy 提供的一个函数，用于将多个一维索引数组转换为一个用于多维数组索引的元组。这个元组可以用于同时对多个维度进行索引，从而方便地选择数组中的子集。使用 numpy.ix_() 可以让代码更加简洁和易读，避免了使用多个索引数组或切片来对多维数组进行索引的复杂性和难以理解的问题。在科学计算和数据分析中，使用 numpy.ix_() 可以方便地进行数据筛选和子集提取，提高代码效率和可读性。

布尔索引、切片类似本章前文，二维数组也可以采用布尔索引、切片。举个例子，如图 13 所示，取出二维数组大于 0 的元素，结果为一元数组。本章配套代码还提供其他输出形式，请大家自行学习。

Page 9  |  Chapter 14 NumPy 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 5  4  3 7  6 2  1 a[a>0]

图 13. 取出大于0 的元素

本章配套代码还介绍如何对三维数组进行索引、切片，也请大家自行学习。

请大家完成下面3 道题目。

Q1. 创建一个一维数组，形状为 (10, )，用满足在 [−1, 1] 均匀分布随机数填充。切片操作提取前5 个元素，并将结果倒序输出。

Q2. 创建一个二维数组，形状为 (3, 4)，用满足在 [−1, 1] 均匀分布随机数填充。使用切片操作选取其中的第一行和第三行。同时，使用切片操作取出第二、四列。

Q3. 创建一个三维数组，形状为 (4, 5, 6)，用满足在 [−1, 1] 均匀分布随机数填充。使用切片操作选取其中的axis = 0、1 维度上的所有元素，以及axis = 2 维度上的前两个元素。

* 题目不提供答案。

Page 1  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Basic Computations in NumPy NumPy 常见运算使用NumPy 完成算术、代数、统计运算

生活只有两件好事：发现数学和教数学。

Life is good for only two things: discovering mathematics and teaching mathematics.

—— 西梅翁·德尼·泊松 (Siméon Denis Poisson)  |  法国数学家  |  1781 ~ 1840

◄ numpy.abs() 计算绝对值、复数模 ◄ numpy.add() 加法运算 ◄ numpy.argmax() 返回数组中最大元素的索引 ◄ numpy.argmin() 返回数组中最小元素的索引 ◄ numpy.array() 创建array 数据类型 ◄ numpy.average() 计算数组元素的加权平均值 ◄ numpy.broadcast_to() 用于将数组广播到指定的形状 ◄ numpy.corrcoef() 计算数组中元素的协方差矩阵，自由度ddof 没有影响 ◄ numpy.cos() 计算余弦值 ◄ numpy.cov() 计算数组中元素的协方差矩阵，默认自由度ddof 为0 ◄ numpy.divide() 除法运算 ◄ numpy.exp() 对数组中的每个元素进行指数运算 ◄ numpy.maximum() 逐元素地比较两个数组，并返回元素级别上的较大值组成的新数组 ◄ numpy.multiply() 乘法运算 ◄ numpy.power() 乘幂运算 ◄ numpy.random.multivariate_normal() 用于生成多元正态分布的随机样本 ◄ numpy.random.randint() 在指定范围内产生随机整数 ◄ numpy.random.uniform() 产生满足连续均匀分布的随机数 ◄ numpy.reshape() 用于将数组重新调整为指定的形状 ◄ numpy.sin() 计算正弦值 ◄ numpy.std() 计算数组中元素的标准差，默认自由度ddof 为0 ◄ numpy.subtract() 减法运算 ◄ numpy.var() 计算数组中元素的方差，默认自由度ddof 为0 ◄ sklearn.datasets.load_iris 导入鸢尾花数据

Page 2  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 15.1 加减乘除乘幂

在NumPy 中，基本的加减乘除、乘幂运算如下： ► 加法：使用 + 运算符或 numpy.add() 函数实现。

► 减法：使用 - 运算符或 numpy.subtract() 函数实现。

► 乘法：使用 * 运算符或 numpy.multiply() 函数实现。

► 除法：使用 / 运算符或 numpy.divide() 函数实现。

► 乘幂：使用 ** 运算符或 numpy.power() 函数实现。

下面，我们先聊一聊相同形状的数组之间的加减乘除乘幂运算。

本节配套的Jupyter Notebook 文件是Bk1_Ch15_01.ipynb。

一维数组图 1 所示为两个等长度一维数组之间的加、减、乘、除、乘幂运算。这一组运算都是逐项完成，也就是对应位置完成运算。

2  1 + = 2  1 - 4  3  2 = 2  1 * 4  2 = 2  1 / 1  0.5 0 0.5 = 2  1 ** =

图 1. 一维数组加、减、乘、除、乘幂

二维数组图 2 所示为二维数组之间的加、减、乘、除、乘幂运算。类似运算也可以用在三维、多维数组上。

Page 3  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com + = = = = = - * / **

图 2. 二维数组加、减、乘、除、乘幂，空白网格代表矩阵的每个元素均为2

## 15.2 广播原则

简单来说，NumPy 的广播原则 (broadcasting) 指定了不同形状的数组之间的算术运算规则，将形状较小的数组扩展为与形状较大的数组相同，再进行运算，以提高效率。

下面，我们首先以一维数组为例介绍什么是广播原则。

一维数组和标量图 3 所示一维数组和标量之间完成加、减、乘、除、乘幂运算，大家可以发现图 3 可以替代

2  1 + = 2  1 - 4  3  2 = 2  1 * 4  2 = 2  1 / 1  0.5 0 0.5 = 2  1 ** =

图 3. 一维数组和标量加、减、乘、除、乘幂，广播原则

一维数组和列向量图 4 和图 5 所示为将广播原则用在一维数组和列向量的加法和乘法上。广播过程相当于把一维数组 (5,) 展成 (3, 5) 二维数组，把列向量 (3, 1) 也展成 (3, 5) 二维数组。运算结果也是二维数组。

这两幅图中，大家还会看到，行向量、列向量之间的运算也可以获得同样的结果，请大家在 JupyterLab 中自己完成。

Page 4  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 2  1 + = + = 2  1 + = 2  1 2  1 2  1

图 4. 一维数组和列向量加法，广播原则

2  1 * = 2  1 4  2 6  3 2  1 4  2 6  3 * = 2  1 2  1 2  1 2  1 4  2 6  3 * = 2  1

图 5. 一维数组和列向量乘法，广播原则

二维数组和标量图 6 所示二维数组和标量的运算相当于图 2。

+ = = = = = - * / **

图 6. 二维数组和标量加、减、乘、除、乘幂，广播原则

Page 5  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

二维数组和一维数组图 7 所示为二维数组和一维数组之间的广播原则运算。二维数组的形状为 (4, 6)，一维数组的形状为 (6, )。

图 7 等价于图 8。图 8 中，行向量是二维数组，形状为 (1, 6)。

注意，当前NumPy 不支持 (4, 6) 和 (4, ) 之间的广播运算，会报错。这种情况，要用 (4, 6) 和 (4, 1)

之间的广播原则。

+ = = * + = = *

图 7. 二维数组和一维数组加、乘，广播原则

+ = = * + = = *

图 8. 二维数组和行向量加、乘，广播原则

二维数组和列向量图 9 所示为二维数组和列向量之间的广播运算。二维数组的形状为 (4, 6)，列向量形状为 (4, 1)。它们在行数上匹配。

+ = = * + = = *

图 9. 二维数组和列向量加、乘，广播原则

Page 6  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 15.3 常见函数

NumPy 还提供大量常用函数。

NumPy 中还给出很多常用常数，比如numpy.pi (圆周率)、numpy.e (欧拉数、自然底数)、 numpy.Inf (正无穷)、numpy.NAN (非数) 等等。

函数 NumPy 函数图像 f(x) = xp 幂函数 (power function)

numpy.power(x,2)

f(x)

numpy.power(x,3)

f(x)

f(x) = sin(x)

正弦函数 (sine function)

numpy.sin()

f(x)

f(x) = arcsin(x)

反正弦函数 (inverse sine function)

numpy.arcsin()

f(x)

Page 7  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f(x) = cos(x)

余弦函数 (sine function)

numpy.cos()

f(x)

f(x) = arccos(x)

反余弦函数 (inverse cosine function)

numpy.arccos()

f(x)

f(x) = tan(x)

正切函数 (tangent function)

numpy.tan()

f(x)

f(x) = arctan(x)

反正切函数 (inverse tangent function)

numpy.arctan()

f(x)

f(x) = sinh(x)

双曲正弦函数 (hyperbolic sine function)

numpy.sinh()

f(x)

f(x) = cosh(x)

双曲余弦函数 (hyperbolic sine function)

numpy.cosh()

f(x)

Page 8  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f(x) = tanh(x)

双曲正切函数 (hyperbolic tangent function)

numpy.tanh()

f(x)

f(x) = | x | 绝对值函数 (absolute function)

numpy.abs()

f(x)

( )

f x =   向下取整函数 (floor function)

numpy.floor()

f(x)

( )

f x =   向上取整函数 (ceil function)

numpy.ceil()

f(x)

f(x) = sgn(x)

符号函数 (sign function)

numpy.sign()

f(x)

f(x) = exp(x) = ex 指数函数 (exponential function)

numpy.exp()

f(x)

Page 9  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f(x) = ln(x)

对数函数 (logarithmic function)

numpy.log()

f(x)

a b import numpy as np import matplotlib.pyplot as plt # 自定义可视化函数 def visualize_fx(x_array, f_array, title, step = False):

fig, ax = plt.subplots(figsize = (5,5))

ax.plot([-5,5],[-5,5], c = 'r', ls = '--', lw = 0.5)

if step: ax.step(x_array, f_array)

else: ax.plot(x_array, f_array)

ax.set_xlim(-5, 5)

ax.set_ylim(-5, 5)

ax.axvline(0, c = 'k')

ax.axhline(0, c = 'k')

ax.set_xticks(np.arange(-5, 5+1))

ax.set_yticks(np.arange(-5, 5+1))

ax.set_xlabel('x')

ax.set_ylabel('f(x)')

plt.grid(True)

ax.set_aspect('equal', adjustable='box')

fig.savefig(title + '.svg', format='svg')

e f

图10. 自定义可视化函数

Page 10  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b # 幂函数，p = 2 x_array = np.linspace(-5,5,1001)

f_array = np.power(x_array, 2)

visualize_fx(x_array, f_array, '幂函数_p=2')

# 反正弦函数 x_array_ = np.copy(x_array)

x_array_[(x_array_ < -1) | (x_array_ > 1)] = np.nan f_array = np.arcsin(x_array_)

visualize_fx(x_array_, f_array, '反正弦函数')

# 正切函数 f_array = np.tan(x_array)

f_array[:-1][np.diff(f_array) < 0] = np.nan visualize_fx(x_array, f_array, '正切函数')

# 向下取整函数 f_array = np.floor(x_array)

visualize_fx(x_array, f_array, '向下取整函数', True)

# 对数函数 x_array_ = np.copy(x_array)

x_array_[x_array_<=0] = np.nan f_array = np.log(x_array_)

visualize_fx(x_array_, f_array, '对数函数')

e g f

图11. 可视化一元函数，使用时配合前文代码

## 15.4 统计运算

图 12 所示为求最大值的操作。给定二维数组A，A.max() 计算整个数组中最大值。而A.max(axis = 0)

在列方向计算最大值，结果为一维数组。A.max(axis = 1) 在行的方向上计算最大值，结果同样为一维数组。而A.max(axis = 1, keepdims = True) 的结果为列向量 (二维数组)。

此外，计算最小值、求和、均值、方差、标准差等统计运算遵循相同的规则，请大家参考本章 Jupyter Notebook。

注意，计算方差、标准差时，NumPy 默认分母为n (样本数量)，而不是n – 1；为了计算样本方差或标准差，需要设定ddof = 1。

Page 11  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com A A.max()

A A.max(axis = 0)

A A.max(axis = 1)

1D array A A.max(axis = 1, keepdims = True)

图 12. 沿不同轴求最大值

什么是方差？

方差是统计学中衡量数据分散程度的一种指标，用于衡量一组数据与其平均值之间的偏离程度。方差的计算是将每个数据点与平均值的差的平方求和，并除以数据点的个数n 减1，即n − 1。方差越大，数据点相对于平均值的离散程度就越高，反之亦然。方差常用于数据分析、建模和实验设计等领域。方差开平方结果为标准差。

NumPy 还提供计算协方差矩阵、相关性系数矩阵的函数。图 13 (a) 所示为鸢尾花数据协方差矩阵， 图 13 (b) 为相关性系数矩阵。

0.12 0.87 0.82 0.12 0.43 0.43 0.37 0.82 0.37 0.87 0.96 0.96 1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4 0.69 0.042 1.3 0.52 3.0 0.042 0.19 0.33 0.12 1.3 0.33 3.1 1.3 1.3 0.58 0.12 0.52 2.5 2.0 1.5 1.0 0.5 0.0 (a)

(b)

图 13. 鸢尾花数据协方差矩阵、相关性系数矩阵

Page 12  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a b import numpy as np import matplotlib.pyplot as plt import seaborn as sns from sklearn.datasets import load_iris # 导入鸢尾花数据 iris = load_iris()

iris_data_array = iris.data print(iris_data_array.max()) # 整个矩阵的最大值 print(iris_data_array.max(axis = 0)) # 每列最大值 print(np.argmax(iris_data_array, axis=0)) # 每列最大值位置 print(iris_data_array.max(axis = 1)) # 每行最大值位置 print(np.average(iris_data_array, axis = 0)) # 每列均值 # 计算每一列方差 print(np.var(iris_data_array, axis = 0))

# 注意，NumPy中默认分母为n print(np.var(iris_data_array, axis = 0, ddof = 1))

# 将分母设为n - 1 # 计算每一列标准差 print(np.std(iris_data_array, axis = 0))

# 计算协方差矩阵；注意转置 SIGMA = np.cov(iris_data_array.T, ddof = 1)

print(SIGMA)

# 可视化协方差矩阵 fig, ax = plt.subplots(figsize = (5,5))

sns.heatmap(SIGMA, cmap = 'RdYlBu_r', annot = True, ax = ax, fmt = ".2f", square = True, xticklabels = [], yticklabels = [], cbar = True)

# 计算协方差矩阵；注意转置 CORR = np.corrcoef(iris_data_array.T)

print(CORR)

fig, ax = plt.subplots(figsize = (5,5))

sns.heatmap(CORR, cmap = 'RdYlBu_r', annot = True, ax = ax, fmt = ".2f", square = True, xticklabels = [], yticklabels = [], cbar = True)

e f g h j k

图14. NumPy 中的统计运算

什么是协方差矩阵？

协方差矩阵是一个方阵，其中的元素代表了数据中各个维度之间的协方差。协方差是用来衡量两个随机变量之间的关系的统计量，它描述的是两个变量的变化趋势是否相似，以及它们之间的相关性强度。协方差矩阵可以用于多变量分析和线性代数中的特征值分解、奇异值分解等计算。在机器学习领域，协方差矩阵常用于数据降维、主成分分析、特征提取等方面。

Page 13  |  Chapter 15 NumPy 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 什么是相关系数矩阵？

相关性系数矩阵是一个方阵，其中的元素代表了数据中各个维度之间的相关性系数。相关性系数是用来衡量两个变量之间线性关系的程度，它取值范围在-1 到1 之间，数值越接近于1 或-1，说明两个变量之间的线性关系越强；数值越接近于0，说明两个变量之间的线性关系越弱或不存在。相关性系数矩阵可以用于多变量分析、线性回归等领域，通常与协方差矩阵一起使用。在机器学习领域，相关性系数矩阵常用于特征选择和数据可视化等方面。

请大家完成下面3 道题目，它们的目的都是利用NumPy 计算并可视化公式。

Q1. 给定如下一元高斯函数，参数a = 1, b = 2, c = 1。请用NumPy 和Matplotlib 线图可视化函数函数图像。

( )

( )

exp b f x a   − = −    

Q2. 给定如下二元高斯函数。请用NumPy 和Matplotlib 三维网格面可视化二元函数图像。

( )

( )

, exp f x x = − −

Q3. 下式为二元高斯分布的概率密度函数，请用NumPy 和Matplotlib 填充等高线可视化这个二元函数图像。参数具体为µX = 0, µY = 0, σX = 1, σY = 1, ρX,Y = 0.6。

( )

, exp 2(1 )

X X Y Y X X Y Y X Y y y f x y                        − − − −     = − − +          −   −           

* 题目答案请参考Bk1_Ch15_02.ipynb。

Page 1  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Reshaping NumPy Arrays NumPy 数组变形重塑数组的维数、形状

哪里有物质，哪里就有几何学。

Where there is matter, there is geometry.

—— 约翰内斯·开普勒 (Johannes Kepler)  |  德国天文学家、数学家  |  1571 ~ 1630

◄ numpy.flatten() 用于将多维数组转换为一维数组。与 numpy.ravel() 不同的是，numpy.flatten() 返回数组的副本，而不是原始数组的视图 ◄ numpy.flip() 用于沿指定轴翻转数组的元素顺序 ◄ numpy.fliplr() 沿着水平方向 (左右方向) 翻转数组的元素顺序 ◄ numpy.flipud() 沿着垂直方向 (上下方向) 翻转数组的元素顺序 ◄ numpy.ravel() 用于将多维数组转换为一维数组，按照 C 风格的顺序展平数组元素 ◄ numpy.reshape() 将原始数组重新排列成新的形状，只要新形状的元素数量与原始数组相同即可 ◄ numpy.rot90() 默认将数组按指定次数逆时针旋转 90 度 ◄ numpy.shares_memory() 用于检查两个数组是否共享相同的内存位置 ◄ numpy.transpose() 转置运算，即将数组的行和列进行互换

Page 2  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

a = numpy.arange(-7, 7 + 1)

numpy.reshape(a, (-1,1))

numpy.reshape (a, (3,5))

numpy.transpose()

array.T numpy.reshape (a, (5,3), order = 'F')

numpy.ravel()

numpy.rot90()

numpy.flip()

numpy.fliplr()

numpy.flipud()

numpy.transpose()

array.T numpy.reshape (a, (1,-1))

Page 3  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 16.1 从reshape() 函数说起

在 NumPy 中，要改变数组的形状 (也称重塑数组)，可以使用 numpy.reshape() 函数。reshape() 函数允许你指定一个新的形状，然后返回一个拥有相同数据但具有新形状的数组。

下面我们先了解一下这个话题的核心函数——numpy.reshape()。

numpy.reshape(a, newshape, order='C')

这个函数的重要输入参数： ● a 参数是要被重塑的数组，可以是一个数组对象，也可以是一个 Python 列表、元组等支持迭代的对象。

● newshape 参数是新的形状，可以是一个整数元组或列表，也可以是一个整数序列。

● order 参数表示重塑数组的元素在内存中存储的顺序，可以是 'C' (按行顺序存储) 或 'F' (按列顺序存储)，默认值为 'C'。

下面是numpy.reshape() 函数一些常见用法： a) 改变数组的维度：可以将一个数组从一维改为二维、三维等。例如： import numpy as np a = np.arange(12)            # 创建一个长度为12 的一维数组 b = np.reshape(a, (3, 4))    # 改变为3 行4 列的二维数组 c = np.reshape(a, (2, 3, 2)) # 改变为2 个3 行2 列的三维数组 b) 展开数组：可以将一个多维数组展开为一维数组。例如： import numpy as np a = np.array([[1, 2], [3, 4]])

b = np.reshape(a, -1)  # 将二维数组展开为一维数组 c) 改变数组的顺序：可以改变数组在内存中的存储顺序。例如： import numpy as np a = np.arange(6).reshape((2, 3))      # 创建一个2 行3 列的二维数组 b = np.reshape(a, (3, 2), order='F')  # 按列顺序存储注意：numpy.reshape() 函数并不会改变数组的数据类型和数据本身，只会改变其形状。如果改变后的形状与原数组的元素数量不一致，将会抛出 ValueError 异常。

请大家在JupyterLab 中自行运行如上三段代码。

更多有关numpy.reshape() 函数的用法，请大家参考如下技术文档： https://numpy.org/doc/stable/reference/generated/numpy.reshape.html 下面结合实例详细讲解如何利用numpy.reshape() 完成数组变形。

本节配套的Jupyter Notebook 文件是BK_2_Ch16_1.ipynb。

## 16.2 一维数组 → 行向量、列向量

一维数组 → 行向量本书前文提过，行向量、列向量都是特殊矩阵。因此，行向量、列向量都是二维数组。也就是说， 行向量是一行若干列的数组，形状为1 × D。列向量是若干行一列的数组，形状为n × 1。

Page 4  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 7  6  5  4  3  2  1 7  6  5  4  3  2  1 a = numpy.arange(-7, 7 + 1)

(15,)

(1, 15), 1 × 15 1D array 2D array numpy.reshape(a, (1,-1))

图 1. 将一维数组转换为行向量

如图 1 所示，用a = numpy.arange(-7, 7+1) 生成的是一个一维数组a，这个数组有15 个元素。由于数组为一维，所以可视化时采用了“圆圈”，而不是方块。利用numpy.reshape(a, (1, -1))，我们将a 转化为形状为 (1, 15) 的二维数组，也称行向量，即1 × 15 矩阵。

注意，使用 -1 作为形状参数时，numpy.reshape() 会根据数组中的数据数量和其它指定的维数来自动计算该维度的大小。

一维数组 → 列向量如图 2 所示，利用numpy.reshape(a, (-1, 1))，我们可以把一维数组numpy.arange(-7, 7+1) 转化为形状为 (15, 1) 的二维数组，也称列向量，即15 × 1 矩阵。

7  6  5  4  3  2  1 a = numpy.arange(-7, 7 + 1)

(15,)

(15, 1), 15 × 1 1D array 2D array numpy.reshape (a, (-1,1))

图 2. 将一维数组转换为列向量

## 16.3 一维数组 → 二维数组

用a = numpy.arange(-7, 7+1) 生成的数组有15 个元素，可以被3、5 整除，因此一维数组a 可以写成3 × 5 矩阵。如图 3 所示，我们可以分别按先行后列、先列后行两种形式重塑数组。

Page 5  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 7  6  5  4  3  2  1 a = numpy.arange(-7, 7 + 1)

(15,)

1D array (3, 5), 3 × 5 2D array numpy.reshape(a, (3,-1))

7  6  5  4  3 2  1 (3, 5), 3 × 5 2D array numpy.reshape(a, (3,-1), order = 'F')

图 3. 将一维数组转换为3 × 5 矩阵，先行后列，先列后行

图 4 所示为将numpy.arange(-7, 7+1) 一维数组写成5 × 3 矩阵。图 4 给出了先行后列、先列后行两种顺序。如图 5 所示已经完成转换的3 × 5 数组，通过numpy.reshape() 可以进一步转化为5 × 3 数组。此外，请比较numpy.reshape() 和numpy.resize() 用法的异同。

7  6  5  4  3  2  1 a = numpy.arange(-7, 7 + 1)

(15,)

1D array (5, 3), 5 × 3 2D array numpy.reshape(a, (5,-1))

2D array numpy.reshape(a, (5,-1), order = 'F')

7  6  5 4  3  2 (5, 3), 5 × 3

图 4. 将一维数组转换为5 × 3 矩阵，先行后列，先列后行

(3, 5), 3 × 5 numpy.reshape(numpy.reshape(a, (3,-1)), (5,-1))

7  6  5  4  3 2  1 (5, 3), 5 × 3 7  6  5 4  3  2 numpy.reshape(a, (3,-1))

图 5. 将3 × 5 矩阵转换为5 × 3 矩阵，先行后列

## 16.4 一维数组 → 三维数组

图 6 所示为将numpy.arange(-13, 13+1) 一维数组转化成形状为3 × 3 × 3 的三维数组。

Page 6  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (27,)

7  6  5  4  3  2  1 13 12 11 10  9  8 a = numpy.arange(-13, 13 + 1)

numpy.reshape(a, (3, 3, 3))

13 12 11 10  9  8 7  6  5 4  3  2 (3, 3, 3), 3 × 3 × 3 3D array

图 6. 将一维数组转换为三维数组

## 16.5 视图 vs 副本

本书前文特别提过，NumPy 中要特别注意视图 (view)、副本 (copy) 的区别。简单来说，视图和副本是NumPy 中的两种不同的数组对象。

视图是指一个数组的不同视角或者不同形状的表现方式，视图和原始数组共享数据存储区，因此在对视图进行操作时，会影响原始数组的数据。视图可以通过数组的切片、转置、重塑等操作创建。

副本则是指对一个数组的完全复制，副本和原始数组不共享数据存储区，因此对副本进行操作不会影响原始数组。使用numpy.reshape() 也需要注意视图、副本问题。

本节配套的Jupyter 笔记中，大家可以看到，我们用numpy.shares_memory() 判断两个数组是否指向同一个内存。

如图 7 所示，numpy.reshape() 仅仅改变了观察同一数组的视角，也就是改变了index。

注意，不同函数的历史、未来版本可能存在不一致，需要大家自行判断。

7  6  5  4  3  2  1 7  6  5  4  3  2  1 numpy.reshape(a, (1,-1))

numpy.reshape(a, (3,-1))

7  6  5  4  3 2  1 7  6  5 4  3  2 numpy.reshape(a, (5,-1))

a = numpy.arange(-7, 7 + 1)

图 7. 视图，还是副本？

Page 7  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 16.6 转置

如图 8 所示，一个n × D 矩阵A 转置得到D × n 矩阵B，整个过程相当于矩阵A 绕主对角线镜像。具体来说，矩阵A 位于 (i, j) 的元素转置后的位置为 (j, i)，即行列序号互换。这就是，为什么位于主对角线上的元素转置前后位置不变。矩阵A 的转置 (the transpose of a matrix A) 记作AT或A'。为了和求导记号区分，本书仅采用AT记法。

B = AT A = BT A B n × D D × n a1 a2 a3 a4 a1 T a2 T a3 T a4 T

图 8. 矩阵转置，图片来自《矩阵力量》第4 章需要大家特别注意的是，NumPy 的numpy.transpose() 方法和.T 属性都返回原始数组的转置，两者都返回原始数组的视图，而不是副本。

“鸢尾花书”中《矩阵力量》第4 章将专门讲解矩阵的转置运算。

图 9 所示为二维数组的转置。行向量转置得到列向量，反之亦然。3 × 5 矩阵转置得到5 × 3 矩阵。而一维数组的转置不改变形状。

7  6  5  4  3  2  1 (1, 15), 1 × 15 (15, 1), 15 × 1 numpy.transpose()

(3, 5), 3 × 5 7  6  5  4  3 2  1 (5, 3), 5 × 3 numpy.transpose()

图 9. 二维数组的转置

Page 8  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 16.7 扁平化

扁平化可以理解图 1、图 2、图 3 等numpy.reshape() 的“逆操作”。完成扁平化的方法有很多，比如 array.ravel()、array.reshape(-1)、array.flatten()。大家也可以使用numpy.ravel()、numpy.flatten()

这两个函数。图 10 所示为将二维转化为一维数组。

(5, 3), 5 × 3 2D array 7  6  5 4  3  2 7  6  5  4  3  2  1 (15,)

1D array numpy.ravel()

图 10. 二维数组转化为一维数组

请大家格外注意，ravel()、reshape(-1) 返回的是原始数组的视图，而不是其副本。因此，如果修改新数组中的任何元素，原始数组也会受到影响。如果需要返回一个数组副本，可以使用flatten()函数。

本节配套的Jupyter 笔记中给出一个详细的例子，请大家自行学习。

## 16.8 其他操作

如图 11 所示，numpy.rot90() 的作用是将一个数组逆时针旋转90 度。默认情况下，这个函数会将数组的前两个维度 axes=(0, 1) 进行旋转。此外，还可以利用参数k (正整数) 逆时针旋转k × 90 度。默认，k = 1。

注意，numpy.rot90() 的结果也是返回原始数组的视图，而不是副本。

(3, 5), 3 × 5 7  6  5  4  3 2  1 numpy.rot90()

(5, 3), 5 × 3

图 11. 3 × 5 矩阵逆时针旋转90 度

numpy.flip() 函数用于翻转数组中的元素，即将数组沿着一个或多个轴翻转。numpy.flip(A, axis=None) 中，A 是要进行翻转的数组，axis 指定要翻转的轴。如图 12 所示，如果不指定 axis，则默认将整个数组沿着所有的轴进行翻转。类似的函数还有numpy.fliplr()、numpy.flipud()，请大家自行学习。

Page 9  |  Chapter 16 NumPy 数组变形  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (3, 5), 3 × 5 7  6  5  4  3 2  1 numpy.flip()

(3, 5), 3 × 5

图 12. 3 × 5 矩阵沿着两个轴翻转

下面，是有关使用numpy.reshape() 函数的三道习题，请大家完成。

Q1. 首先生成一个一维数组 [1, 2, 3, 4, 5, 6]，然后将其转换为一个形状为 (2, 3) 的二维数组，并打印结果。注意，元素按先行后列顺序存储。最后，想办法判断转换前后的数组是视图，还是副本。

Q2. 将一个二维数组 [[1, 2], [3, 4], [5, 6]] 转换为一个形状为 (6,) 的一维数组，并打印结果。注意，按先列后行顺序存储。

Q3. 将一个三维数组 [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] 转换为一个形状为 (2, 4) 的二维数组，并按列顺序存储，最后打印结果。

* 这三道题目很基础，本书不给答案。

Page 1  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Manipulating NumPy Arrays NumPy 数组规整重塑数组的维数、形状

我不能教任何人任何东西。我只能让他们思考。

I cannot teach anybody anything. I can only make them think.

—— 苏格拉底 (Socrates)  |  古希腊哲学家  |  470 ~ 399 BC

◄ numpy.append() 用于将值添加到数组的末尾，生成一个新的数组，并不会修改原始数组 ◄ numpy.arange() 创建一个具有指定范围、间隔和数据类型的等间隔数组 ◄ numpy.block() 用于按照指定的块结构组合多个数组，生成一个新的数组 ◄ numpy.column_stack() 按列堆叠多个数组，生成一个新的二维数组 ◄ numpy.concatenate() 沿指定轴连接多个数组，生成一个新的数组 ◄ numpy.delete() 用于删除数组中指定位置的元素，生成一个新的数组，并不会修改原始数组 ◄ numpy.hsplit() 用于沿水平方向分割数组为多个子数组 ◄ numpy.hstack() 按水平方向堆叠多个数组，生成一个新的数组 ◄ numpy.insert() 用于在数组的指定位置插入值，生成一个新的数组，并不会修改原始数组 ◄ numpy.ravel() 用于将多维数组转换为一维数组，按照 C 风格的顺序展平数组元素 ◄ numpy.repeat() 将数组中的元素重复指定次数，生成一个新的数组 ◄ numpy.reshape() 用于改变数组的形状，重新排列数组元素，但不改变原始数据本身 ◄ numpy.resize() 用于调整数组的形状，并可以在必要时重复数组的元素来填充新的形状 ◄ numpy.row_stack() 按行堆叠多个数组，生成一个新的数组 ◄ numpy.split() 用于将数组沿指定轴进行分割成多个子数组 ◄ numpy.squeeze() 用于从数组的形状中去除维度为1 的维度，使得数组更紧凑 ◄ numpy.stack() 用于沿新的轴将多个数组堆叠在一起，生成一个新的数组 ◄ numpy.swapaxes() 用于交换数组的两个指定轴的位置 ◄ numpy.tile() 用于将数组沿指定方向重复指定次数，生成一个新的数组 ◄ numpy.transpose() 完成矩阵转置，即将数组的行和列进行互换 ◄ numpy.vsplit() 用于沿垂直方向分割数组为多个子数组 ◄ numpy.vstack() 按垂直方向堆叠多个数组，生成一个新的数组

Page 2  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 本书前文介绍的numpy.swapaxes()、numpy.reshape()、numpy.resize()、numpy.transpose()、 numpy.squeeze()、numpy.ravel() 等等都算是对NumPy 数组进行规整的函数。本章将介绍其他几种常用规整函数。

## 17.1 堆叠

沿行堆叠用numpy.arange() 产生如图 1 所示的两个一维等长数组。图 2 所示为三种办法将两个等长一维数组沿行axis = 0 方向堆叠，结果为二维数组。

numpy.stack() 函数将沿着指定轴将多个数组堆叠在一起，返回一个新的数组；默认轴为axis = 0。

numpy.row_stack() 函数将多个数组沿着行方向进行堆叠，生成一个新的数组。numpy.vstack() 将多个数组沿着垂直方向（行方向）进行堆叠，生成一个新的数组。

a1 5  4  3 a2

图 1. 两个等长一维数组

numpy.stack((a1, a2))

numpy.row_stack((a1, a2))

numpy.vstack((a1, a2))

5  4  3 a2 a1 5  4  3 Axis = 0

图 2. 沿行axis = 0 方向堆叠

沿列堆叠图 3 所示为沿列axis = 1 方向堆叠两个一维等长数组。图中给出两种办法。

numpy.column_stack() 将多个一维数组沿着列方向进行堆叠，生成一个新的二维数组。

numpy.stack((a1, a2),axis=1)

numpy.column_stack((a1, a2))

5  4  3 a2 a1 Axis = 1

图 3. 沿列axis = 1 方向堆叠

如图 4 所示，用numpy.hstack() 堆叠一维数组的结果还是一个一维数组。numpy.hstack() 将多个数组沿着水平方向 (列方向) 进行堆叠，生成一个新的数组。为了获得图 3 结果，需要先将两个一维数组变形为列向量，然后用numpy.hstack() 函数沿列堆叠，具体如图 5 所示。

Page 3  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com numpy.hstack((a1, a2))

5  4  3 a2 a1 5  4  3

图 4. 沿列axis = 1 方向堆叠，用numpy.hstack()

numpy.reshape(-1,1)

5  4  3 a2 a1 Axis = 1 numpy.hstack()

图 5. 沿列axis = 1 方向堆叠，两个列向量

拼接我们还可以用numpy.concatenate() 完成数组拼接。如所示，利用numpy.concatenate()，我们可以分别完成沿行、列方向数组拼接。

numpy.concatenate((), axis=1)

numpy.concatenate((), axis=0)

图 6. 用numpy.concatenate() 拼接

堆叠结果为三维数组此外，利用numpy.stack()，我们还可以将二维数组堆叠为三维数组。图 7 所示为沿三个不同方向堆叠结果的效果图。

Axis = 0 Axis = 1 Axis = 2

Page 4  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 7. 沿着三个不同方向堆叠举个例子，给定图 8 所示两个形状相同的二维数组。它俩按图 7 所示为沿三个不同方向堆叠的结果如图 9 所示。

图 8. 两个形状相同的二维数组

Axis = 0 Axis = 1 Axis = 2 Axis = 0 Axis = 1 Axis = 2 Axis = 0 Axis = 1 Axis = 2

图 9. 得到三个不同的三维数组

## 17.2 重复

numpy.repeat() 和numpy.tile() 都可以用来重复数据。numpy.repeat() 和numpy.tile() 的区别在于重复的对象不同。numpy.repeat() 重复的是分别数组中的每个元素。numpy.repeat() 还可以指定具体的轴，以及不同元素重复的次数，请大家参考其技术文档。

numpy.tile() 重复的是整个数组，如图 11 所示。本章配套Jupyter Notebook 还提供其他示例，请大家自行练习。

Page 5  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com a numpy.repeat(a,2)

numpy.repeat(a,3)

图 10. 利用numpy.repeat() 重复一维数组

a numpy.tile(a,2)

numpy.tile(a,3)

图 11. 利用numpy.tile() 重复一维数组

## 17.3 分块矩阵

合成 numpy.block() 函数用于将多个数组沿不同的轴组合成一个分块矩阵。它接受一个嵌套列表作为输入，每个列表代表一个块矩阵，然后根据指定的轴将这些块矩阵组合在一起。

在图 12 给出的例子中，我们创建了四个小的矩阵，并使用 numpy.block() 函数将它们组合成一个分块矩阵 M。

分块矩阵经常用来简化某些线性代数运算，鸢尾花书《矩阵力量》将专门介绍分块矩阵。

numpy.block()

图 12. 四个二维数组合成一个矩阵

什么是分块矩阵？

分块矩阵是由多个小矩阵组合而成的大矩阵。它将一个大的矩阵划分为若干个小的矩阵，这些小矩阵可以是实数矩阵、向量矩阵或者其他的矩阵形式。通常情况下，分块矩阵可以使用一个方括号将小矩阵组合在一起，然后按照一定的规则排列。分块矩阵可以简化一些复杂的矩阵计算，同时也常常用于表示具有特定结构的矩阵，例如对角矩阵或者上下三角矩阵等。

切割 numpy.split() 函数可以将一个数组沿指定轴分割为多个子数组。numpy.split() 接受三个参数：要分割的数组、分割的索引位置、沿着哪个轴进行分割。图 13 所示为将一个一维数组三等分得到三个子数组。本章配套的Jupyter Notebook 中，大家可以看到如何设定分割索引位置，请自行练习。

Page 6  |  Chapter 17 数组规整  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 14 所示为利用numpy.split() 将二维数组沿不同轴三等分。大家也可以分别尝试使用 numpy.hsplit() 和numpy.vsplit() 完成类似操作。本章配套Jupyter Notebook 中还介绍如何使用 numpy.append()、numpy.insert()、numpy.delete() 完成附加、插入、删除操作，请大家自行学习。

numpy.split(a,3)

图 13. 将一维数组三等分 numpy.split (A,3)

numpy.vsplit (A,3)

numpy.split (A,3, axis = 1)

numpy.hsplit (A,3)

图 14. 将二维数组三等分，沿不同轴

下面，是有关NumPy 数组规整的三道习题，请大家完成。

Q1. 请生成 [0, 1] 区间内的连续均匀两个随机数数组，数组形状为 (10,)。将它俩分别按行、按列堆叠起来形成二维数组。

Q2. 请生成 [0, 1] 区间内的连续均匀一个随机数数组，数组形状为 (12,12)。将它分别按行、按列三等分。

Q3. 请生成 [0, 1] 区间内的连续均匀两个随机数数组，数组形状分别为 (8, 5)、(3, 5)。用几种不同办法将它们拼接成一个数组。

* 这三道题目很基础，本书不给答案。

Page 1  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Linear Algebra in NumPy NumPy 线性代数 NumPy 中的重要线性代数计算

我的大脑只是一个接收器。宇宙中有一个核心，我们从中获得知识、力量和灵感。这个核心的秘密我没有深入了解，但我知道它的存在。

My brain is only a receiver, in the Universe there is a core from which we obtain knowledge, strength and inspiration. I have not penetrated into the secrets of this core, but I know that it exists.

—— 尼古拉·特斯拉 (Nikola Tesla)  |  发明家、物理学家  |  1856 ~ 1943

◄ numpy.linalg.cholesky() 计算Cholesky 分解 ◄ numpy.linalg.dot() 计算向量的点积 ◄ numpy.linalg.eig() 计算矩阵的特征值和特征向量 ◄ numpy.linalg.inv() 计算矩阵的逆 ◄ numpy.linalg.lstsq() 求最小二乘解 ◄ numpy.linalg.norm() 计算向量的范数 ◄ numpy.linalg.pinv() 计算矩阵的Moore-Penrose 伪逆 ◄ numpy.linalg.solve() 求解线性方程组 ◄ numpy.linalg.svd() 计算奇异值分解

Page 2  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 18.1 NumPy 的linalg 模块

NumPy 库的linalg 模块提供了许多用于线性代数计算的函数，包括矩阵分解和向量计算。

以下是一些常见的linalg 函数： ► numpy.linalg.inv()：计算矩阵的逆。

► numpy.linalg.pinv()：计算矩阵的Moore-Penrose 伪逆。

► numpy.linalg.solve()：求解线性方程组Ax = b，其中A 是一个矩阵，b 是一个向量。

► numpy.linalg.lstsq()：最小二乘解。

linalg 模块还提供了许多向量计算函数，包括： ► numpy.linalg.norm()：计算向量的范数。

► numpy.linalg.dot()：计算向量的点积。

以下是linalg 中常用的矩阵分解函数： ► numpy.linalg.cholesky()：计算Cholesky 分解。

► numpy.linalg.eig()：计算矩阵的特征值和特征向量。

► numpy.linalg.svd()：计算奇异值分解。

这些函数在许多科学计算中都非常有用，例如，在机器学习中，可以使用矩阵分解函数进行降维和特征提取，而向量计算函数则可用于计算距离和相似性度量等。需要注意的是，这些函数都要求输入参数为NumPy 数组，并返回NumPy 数组作为输出。

什么是矩阵分解？

矩阵分解是一种将一个矩阵分解为若干个矩阵的乘积的数学技术。这种分解可以帮助我们更好地理解和处理矩阵数据。常见的矩阵分解包括Cholesky 分解、特征值分解 (EVD)、奇异值分解 (SVD) 等等。矩阵分解在很多领域都有广泛的应用，比如在机器学习、数据分析、信号处理、图像处理等方面。

本节配套的Jupyter Notebook 文件是Bk1_Ch18_01.ipynb。

## 18.2 拆解矩阵

一组行向量本书前文提到鸢尾花数据矩阵X 的形状为150 × 4。也就是说，如图 1 热图所示，X 可以看成是由 150 个行向量上下堆叠而成。每个行向量的形状为1 × 4。图 1 特别展示了x(1) (X 第1 行，数组第0 行)、 x(2) (X 第2 行，数组第1 行)、x(51) (X 第51 行，数组第50 行)、x(101) (X 第101 行，数组第100 行)。

Page 3  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X 150 × 4 x(1)

## 5.1 3.5 1.4

0.2

## 4.9 3.0 1.4

0.2 x(2)

x(51)

## 7.0 3.2 4.7

1.4 x(101)

## 6.3 3.3 6.0

2.5 1 × 4

图 1. X 可以看做由一组行向量构成

一组列向量此外，如图 1 热图所示，X 可以看成是由4 个列向量左右排列而成，即 X = [x1, x2, x3, x4]。每个列向量的形状为150 × 1。请大家回忆，我们如何设定索引获得NumPy 数组的行向量、列向量。

X 150 × 4 150 × 1 x1 x2 x3 x4

图 2. X 可以看做由一组列向量构成

## 18.3 向量运算

几何角度看向量在二维空间中，一个向量a 可以表示为一个有序的数对 (a1, a2)、[a1, a2]、[a1, a2]T。向量也可以用一个有向线段来表示，线段的起点为原点 (0, 0)，终点为 (a1, a2)。其中，a1表示向量在水平方向上的投影；y 表示向量纵轴方向上的投影。

用勾股定理，我们可求得图 3 中向量a 的长度，即向量的模，为 a a = + a 。在NumPy 中计算向量模的函数为numpy.linalg.norm()。

(0, 0)

[a1, a2]

a a1 a2

图 3. 向量起点、终点、大小和方向

Page 4  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 在Bk1_Ch18_01.ipynb 中，我们还计算了x(1)、x(2)、x(51)、x(101)这四个向量的单位向量。单位向量是长度为1 的向量，可以用来表示某个向量方向。比如，的单位向量就是x(1)除以自己的模 ( )1 ，即 ( )

( )

。

什么是向量的模？

向量的模 (也称为向量的长度) 是指一个向量从原点到其终点的距离，它是一个标量，表示向量的大小。向量的模通常用两个竖线 ||a|| 来表示，其中 a 表示向量。对于 n 维向量 a = [a1, a2, ..., an]，它的模定义为 n a a a = + + a 。a 就是向量各个分量的平方和的平方根。这个公式可以用勾股定理推导得出，因为一个向量的模就是从原点到它的终点的距离，而这个距离可以用勾股定理计算。比如，2 维向量a = [3, 4] 的模 (长度) 为 = + = a 。

向量内积本书前文在讲for 循环时介绍过向量内积 (inner product)，又叫标量积 (scalar product)、点积 (dot product)。给定两个 n 维向量 a = [a1, a2, ..., an] 和 b = [b1, b2, ..., bn]，它们的内积定义为a · b = a1b1 + a2b2 + ... + anbn。内积结果a · b 显然为标量。

如图 4 所示，我们分别计算向量内积x(1) · x(2)、x(1) · x(51)、x(1) · x(101)。建议大家在JupyterLab 中用手输入算式计算图中三个向量内积。

再次强调，向量内积的运算前提是两个向量维数相同，结果为标量。NumPy 中计算向量内积的函数为numpy.dot()。

x(1)

## 5.1 3.5 1.4

0.2

## 4.9 3.0 1.4

0.2 x(2)

· = 37.5 x(1)· x(2)

x(1)

## 5.1 3.5 1.4

0.2 x(51)

· = 53.8 x(1)· x(51)

x(1)

## 5.1 3.5 1.4

0.2 x(101)

· = 52.6 x(1)· x(101)

## 7.0 3.2 4.7

1.4

## 6.3 3.3 6.0

2.5

图 4. 向量内积

向量夹角在Bk1_Ch18_01.ipynb 中，我们计算得到x(1)、x(2)的夹角约为3°，x(1)、x(51)的夹角约为22°，x(1)、 x(101)的夹角约为31°。

这显然不是巧合，x(1)、x(2)分别代表两朵鸢尾花，它们同属Setosa，因此最为相似。而x(51)属于 Versicolour，x(101)属于Virginica。这就是向量夹角在机器学习中的一个应用举例。

什么是向量夹角？

Page 5  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 向量夹角是指两个向量之间的夹角，它是一个标量，通常用弧度或角度来表示。向量夹角的计算是通过向量内积和向量模的关系得出的。对于两个非零向量 a 和 b，它们的夹角 θ 定义为cos(θ) = (a · b) / (||a|| ||b||)。其中 a · b 是向量 a 和 b 的内积，||a|| 和 ||b|| 分别是向量 a 和 b 的模。注意，这个公式只适用于非零向量，因为对于零向量，它没有方向，因此无法定义夹角。此外，cos(θ) 可以看成是a 和 b 的单位向量的向量内积，即cos(θ) = (a/||a||) · (b/||b||)。

通过向量夹角的计算，我们可以判断两个向量之间的相对方向。如果两个向量的夹角为零度，表示它们的方向相同；如果夹角为 90 度，表示它们互相垂直；如果夹角为180 度，表示它们的方向相反。在机器学习中，可以通过计算向量夹角来度量两个样本之间的相似性。

## 18.4 矩阵运算

矩阵乘法本书前文介绍过矩阵乘法，假设A 是一个m×n 的矩阵，B 是一个n×p 的矩阵，则它们的乘积C = AB 是一个m×p 的矩阵，相当于“消去”n。Python 中可以使用@作为NumPy 的矩阵乘法运算符。

在本节配套的Jupyter Notebook 文件中大家可以看到两个有趣的矩阵乘法。

G = (a) Gram Matrix of X @ X XT @ X XT = (b) Gram Matrix of XT H 4 × 4 4 × 150 150 × 4 150 × 4 4 × 150 150 × 150

图 5. 两个格拉姆矩阵

如图 5 (a) 所示，鸢尾花数据矩阵的转置XT乘X 得到G。XT的形状为4 × 150，X 的形状为150 × 4。

G = XTX 的结果形状为4 × 4。G 有自己的名字，叫X 的格拉姆矩阵 (Gram matrix)。图 5 (b) 所示的H = XXT的结果形状为150 × 150。H 相当是XT的格拉姆矩阵。

Page 6  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 什么是格拉姆矩阵？

格拉姆矩阵 (Gram matrix) 是一个重要的矩阵，它由向量集合的内积组成。给定一个向量集合{x1, x2, ..., xn}，则其对应的格拉姆矩阵G 定义为G = [gi,j]，其中gi,j = xi · xj，表示第i 个向量和第j 个向量的内积。格拉姆矩阵是对称矩阵。

格拉姆矩阵在许多应用中都有广泛的应用，例如在机器学习中的支持向量机 (Support Vector Machine, SVM) 算法和核方法 (kernel method) 中，格拉姆矩阵可以用来计算向量之间的相似度和距离，从而实现非线性分类和回归。此外，格拉姆矩阵也可以用于矩阵分解、图像处理、信号处理等领域。

格拉姆矩阵有很多有趣的性质，《矩阵力量》一册将详细介绍。这里大家仅仅需要知道格拉姆矩阵为对称矩阵。G 的主对角线上元素是xiTxi，即xi · xi。如图 6 上图所示，G 的主对角线第一元素g1,1 = x1Tx1 = x1 · x1。如图 6 下图所示，G 的主对角线第二元素g2,2 = x2Tx2 = x2 · x2。请大家自行计算G 的主对角线剩余两个元素。

如图 7 所示，显然g2,1  = g1,2。也就是说，x2Tx1 = x1Tx2 = x2 · x1 = x1 · x2。

G = @ x1 T x1 G = @ x2 T x2 g1,1 g2,2

图 6. 格拉姆矩阵G 主对角线元素

Page 7  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com G = @ G = @ x2 T g2,1 g1,2 x1 x2 x1 T

图 7. G 为对称矩阵

矩阵的逆矩阵的逆可以被看作是一种倒数的概念。并不是所有格拉姆矩阵，恰好前文的格拉姆矩阵G 存在逆，记做G−1。如图 8 所示，G 乘G−1结果为单位阵I。不难看出来，G−1也是个对称矩阵。

I = @ G G 1

图 8. 格拉姆矩阵G 的逆

什么是矩阵的逆？

矩阵的逆是一个重要的概念，它是指对于一个可逆的 (即非奇异的) n × n 矩阵A，存在一个n × n 矩阵B，使得AB = BA = I，其中I 是单位矩阵。B 被称为A 的逆矩阵，通常用A−1表示。矩阵的逆可以被看作是一种倒数的概念，它可以使我们在矩阵运算中除以矩阵，从而解决线性方程组和其他问题。如果我们需要求解一个线性方程组Ax = b，其中A 是一个可逆矩阵，那么可以使用矩阵的逆来计算x = A−1b，从而得到方程的解。需要注意的是，并非所有矩阵都有逆矩阵，只有可逆矩阵才有逆矩阵。对于一个不可逆矩阵，它可能是奇异的 (即行列式为0)，也可能是非方阵。在实际应用中，矩阵的逆通常通过LU 分解、QR 分解、Cholesky 分解等方法来计算，而不是直接求解逆矩阵。

Page 8  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 18.5 几个常见矩阵分解

Cholesky 分解所幸前文的格拉姆矩阵G 也是个正定矩阵 (positive definite matrix)，我们可以对它进行Cholesky 分解。如图 9 所示，L 是个下三角矩阵，它的转置LT为上三角矩阵。L 和LT的乘积也相当于“平方”。

NumPy 中完成Cholesky 分解的函数为numpy.linalg.cholesky()。

《矩阵力量》第12 章专门讲解Cholesky 分解，这本书第21 章将介绍正定性。

G L LT = @

图 9. 对格拉姆矩阵G 进行Cholesky 分解

什么是Cholesky 分解？

Cholesky 分解是一种将对称正定矩阵分解为下三角矩阵和其转置矩阵乘积的数学技术。给定一个对称正定矩阵A，Cholesky 分解可以将其表示为A = LLT，其中L 是下三角矩阵，LT是其转置矩阵。Cholesky 分解是一种高效的矩阵分解方法，它可以在数值计算中减少误差，同时可以加速线性方程组的求解，特别是对于大型的稠密矩阵。因此，Cholesky 分解在很多领域都有广泛的应用，例如统计学、金融学、物理学、工程学等。Cholesky 分解也是一些高级技术的基础，例如蒙特卡洛模拟、Kalman 滤波等等。

什么是正定矩阵？

Cholesky 分解是一种将对称正定矩阵分解为下三角矩阵和其转置矩阵乘积的数学技术。给定一个对称正定矩阵A，Cholesky 分解可以将其表示为A = LLT，其中L 是下三角矩阵，LT是其转置矩阵。Cholesky 分解是一种高效的矩阵分解方法，它可以在数值计算中减少误差，同时可以加速线性方程组的求解，特别是对于大型的稠密矩阵。因此，Cholesky 分解在很多领域都有广泛的应用，例如统计学、金融学、物理学、工程学等。Cholesky 分解也是一些高级技术的基础，例如蒙特卡洛模拟、Kalman 滤波等等。

特征值分解EVD 图 10 所示为对格拉姆矩阵G 的特征值分解。V 的每一列对应特征向量，Λ 的主对角线元素为特征值。

G V Λ = @ V 1 @ λ1 λ2 λ3 λ4

图 10. 对格拉姆矩阵G 进行EVD 分解

什么是特征值分解？

Page 9  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 特征值分解 (Eigenvalue Decomposition, EVD) 是一种将一个方阵分解为一组特征向量和特征值的数学技术。对于一个n × n 的矩阵 A，如果存在非零向量v 和常数λ，使得Av = λv，那么v 就是矩阵A 的特征向量，λ 就是对应的特征值。将所有特征向量排列成一个矩阵V，将所有特征值排列成一个对角方阵Λ，那么矩阵A 就可以表示为A = VΛV−1。特征值分解可以帮助我们理解矩阵的性质和结构，以及实现很多数学算法。它在很多领域都有广泛的应用，比如图像处理、机器学习、信号处理、量子力学等。特征值分解也是一些高级技术的基础，例如奇异值分解、QR 分解、LU 分解等。

仔细观察，大家可以已经发现图 10 中V 和V−1关于主对角线对称，即VT = V−1。这并不是巧合，原因是格拉姆矩阵G 为对称矩阵。而对称矩阵的特征值分解又叫谱分解 (spectral decomposition)。也就是说，G 的谱分解可以写成G = VΛVT。

I V = @ VT

图 11. 谱分解中V 的特点 《矩阵力量》第13、14 章专门讲解特征值分解。

什么是谱分解？

谱分解 (Spectral Decomposition) 是将对称矩阵分解为一组特征向量和特征值的数学技术，即对称矩阵的特征值分解。对于一个对称矩阵A，谱分解可以将其分解为A = QΛQT，其中Q 是由矩阵A 的特征向量组成的正交矩阵，Λ 是由矩阵A 的特征值组成的对角矩阵。谱分解在很多领域都有广泛的应用，例如图像处理、信号处理、量子力学等。谱分解可以帮助我们理解对称矩阵的性质和结构，从而帮助我们分析和处理各种问题。谱分解也是很多高级技术的基础，例如奇异值分解、主成分分析、矩阵函数等。

奇异值分解SVD 奇异值分解可谓“最重要的矩阵分解，没有之一”。图 12 所示为对鸢尾花数据矩阵X 的奇异值分解。

图 12 中S 的主对角线上的元素叫奇异值。大家会在Bk1_Ch18_01.ipynb 看到，图 10 中特征值开方的结果就是图 12 中的奇异值，这当然不是巧合！

X U S VT = @ @ s1 s2 s3 s4 150 × 4 150 × 4 4 × 4 4 × 4

图 12. 对X 进行SVD 分解

什么是奇异值分解？

奇异值分解 (Singular Value Decomposition, SVD) 是一种将一个矩阵分解为三个矩阵乘积的数学技术。给定一个矩阵A，它可以表示为 A = USVT，其中U 和V 是正交矩阵，S 是对角矩阵，对角线上的元素称为奇异值。SVD 可以将一个矩阵的信息分解为不同奇异值所对应的向量空间，并按照奇异值大小的顺序进行排序，使得我们可以仅使用前面的奇异值和相应的向量空间来近似地表示原始矩阵。这种分解在降维、压缩、数据处理和模型简化等领域中有着广泛的应用，例如推荐系统、图像压缩、语音识别等。

Page 10  |  Chapter 18 NumPy 线性代数  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 如图 13 所示，U 的转置UT和自己乘积为单位阵。如图 14 所示，V 和自身转置VT乘积为单位阵。大家是否已经发现图 11 和图 14 竟然相同，这当然也不是巧合。

实际上，图 12 是四种奇异值分解中的一种。《矩阵力量》第15、16 章专门讲解奇异值分解，并揭开各种“巧合”背后的数学原理。

I UT = @ U 150 × 4 4 × 150

图 13. U 的特点 I V = @ VT

图 14. V 的特点

请大家完成下面5 道题目。

Q1. 本节配套笔记计算了鸢尾花数据矩阵X 的若干行向量的模、单位向量、夹角，请大家计算X 的4 个列向量的模、单位向量、两两列向量内积、两两夹角。并说明两两列向量内积和图 5 (a) 中格拉姆矩阵的关系。

Q2. 请大家用热图可视化图 5 (a) 中的G 的第2 行第3 列元素如何计算得到。

Q4. 请对图 5 (b) 中的格拉姆矩阵进行Cholesky 分解，并解释报错的原因。

Q4. 请对图 5 (b) 中的格拉姆矩阵进行特征值分解，并比较其特征值和图 10 中特征值关系。

Q5. 请对XT进行奇异值分解，比较和图 12 中SVD 分解的关系。

* 本节不提供答案。

Page 1  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Fundamentals of Pandas 聊聊Pandas Pandas DataFrame 类似Excel 表格，有行列标签

数字是知识的终极形态；数字就是知识本身。

Numbers are the highest degree of knowledge. It is knowledge itself.

—— 柏拉图 (Plato)  |  古希腊哲学家  |  424/423 ~ 348/347 BC

◄ pandas.DataFrame() 创建Pandas 数据帧 ◄ pandas.DataFrame.add_prefix() 给DataFrame 的列标签添加前缀 ◄ pandas.DataFrame.add_suffix() 给DataFrame 的列标签添加后缀 ◄ pandas.DataFrame.axes 同时获得数据帧的行标签、列标签 ◄ pandas.DataFrame.columns 查询数据帧的列标签 ◄ pandas.DataFrame.count() 返回数据帧每列 (默认axis=0) 非缺失值数量 ◄ pandas.DataFrame.describe() 用于生成关于数据帧统计摘要信息 ◄ pandas.DataFrame.drop() 用于从DataFrame 中删除指定的行或列 ◄ pandas.DataFrame.head() 用于查看数据帧的前几行数据，默认情况下，返回数据帧的前 5 行 ◄ pandas.DataFrame.iiterrows() 遍历DataFrame 的行 ◄ pandas.dataframe.iloc() 通过整数索引来选择 DataFrame 的行和列的索引器 ◄ pandas.DataFrame.index 查询数据帧的行标签 ◄ pandas.DataFrame.info 获取关于数据帧摘要信息 ◄ pandas.DataFrame.isnull() 用于检查DataFrame 中的每个元素是否为缺失值NaN ◄ pandas.DataFrame.iteritems() 遍历DataFrame 的列 ◄ pandas.dataframe.loc() 通过标签索引来选择 DataFrame 的行和列的索引器 ◄ pandas.DataFrame.nunique() 计算数据帧中每一列的唯一值/独特值数量 ◄ pandas.DataFrame.reindex() 用于重新排序DataFrame 的列标签 ◄ pandas.DataFrame.rename() 对DataFrame 的索引标签、列标签或者它们的组合进行重命名 ◄ pandas.DataFrame.reset_index() 将DataFrame 的行标签重置为默认的整数索引，默认并将原来的行标签转换为新的一列 ◄ pandas.DataFrame.set_axis() 重新设置DataFrame 的行或列标签 ◄ pandas.DataFrame.set_index() 改变DataFrame 的索引结构 ◄ pandas.DataFrame.shape 返回一个元组，其中包含数据帧的行数、列数 ◄ pandas.DataFrame.size 用于返回数据帧中元素，即数据单元格总数 ◄ pandas.DataFrame.sort_index() 按照索引的升序或降序对DataFrame 进行重新排序，默认 axis = 0 ◄ pandas.DataFrame.tail() 用于查看数据帧的后几行数据，默认情况下，返回数据帧的后 5 行 ◄ pandas.DataFrame.to_csv() 将DataFrame 数据保存为CSV 格式文件 ◄ pandas.DataFrame.to_string() 将DataFrame 数据转换为字符串格式 ◄ pandas.DataFrame.values 返回数据帧中的实际数据部分作为一个多维NumPy 数组 ◄ pandas.Series() 创建Pandas Series ◄ seaborn.heatmap() 绘制热图 ◄ seaborn.load_dataset() 加载Seaborn 示例数据集

Page 2  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 19.1 什么是Pandas?

Pandas 是一个开源的Python 数据分析库，它提供了一种高效、灵活、易于使用的数据结构，可以完成数据操作、数据清洗、数据分析和数据可视化等任务。Pandas 最基本的数据结构是Series 和 DataFrame。DataFrame 在本书中被叫做数据帧。

Series 是一种类似于一维数组的对象，相当于NumPy 一维数组；而DataFrame 是一种二维表格型的数据结构，可以容纳多种类型的数据，并且可以进行各种数据操作。本章主要介绍DataFrame。

Pandas 还提供了大量的数据处理和操作函数，例如数据筛选、数据排序、数据聚合、数据合并等等。因此，Pandas 成为了Python 数据科学和机器学习领域的重要工具之一。

比较NumPy Array、Pandas DataFrame NumPy Array 和Pandas DataFrame 都是Python 中重要的数据类型，但是两者存在区别。

NumPy array 是多维数组对象，一般要求所有元素具有相同的数据类型，即本书前文提到的同质性 (homogeneous)，从而保证高效存储运算。

Pandas DataFrame 是一个二维表格数据结构，类似于Excel 表格，包含行标签和列标签。Pandas DataFrame 由多个列组成，每个列可以是不同的数据类型。举个例子，鸢尾花数据集前4 列都是定量数据 (quantitative data)，而最后一列鸢尾花标签是定性数据 (qualitative data)。

NumPy array 使用整数索引，类似于Python 列表。Pandas DataFrame 支持自定义行标签和列标签， 可以使用标签而不仅仅是整数索引进行数据访问。

注意，本章中的行标签、列标签特指数据帧的标签；而对于数据帧，行索引、列索引则是指行列整数索引，这一点类似NumPy 二维数组。默认情况下，数据帧行标签、列标签均为基于0 的整数索引。

如图 1 所示，给一个NumPy 二维数组加上行标签和列标签，我们便得到了一个Pandas DataFrame。

当然，Pandas DataFrame 也可以转化成NumPy 数组。这是本章后续要介绍的内容。

n × D n rows D columns X1 X2 X3 X4 axis = 0 axis = 1 Index Columns pandas.DataFrame()

pandas.DataFrame.to_numpy()

axis = 0 axis = 1

图 1. 比较NumPy array 和Pandas DataFrame，以及两者的相互转化

Page 3  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Pandas DataFrame 更适用于处理结构化数据，如表格、CSV 文件、SQL 数据库查询结果等等。

此外，Pandas DataFrame 还支持时间序列数据。Pandas DataFrame 中的时间序列数据通常是指具有时间索引的数据，其中时间可以是一系列日期、时间戳或时间间隔，对应于数据的每个行或每个数据点。

Pandas DataFrame 提供大量数据操作、处理缺失值、数据过滤、数据合并、数据透视等更高级的数据分析功能。

实际应用中，Pandas 和NumPy 常常一起使用，Pandas 负责数据的组织、清洗和分析，而NumPy 负责底层数值计算。

如何学习Pandas 学习Pandas 需要从以下几个板块入手： Pandas 基础知识：需要学习Pandas 的数据结构，包括Series 和DataFrame，掌握如何创建、读取、 修改、删除、索引和切片等操作，以及如何处理缺失值和重复值等数据清洗技巧。

数据操作：Pandas 提供了丰富的数据操作函数，例如数据筛选、排序、合并、聚合、透视等等。需要学习这些函数的用法和应用场景，以便在数据分析和处理中灵活运用。

数据可视化：Pandas 本身具备一些基本可视化工具；同时Pandas 可以与Matplotlib、Seaborn、 Plotly 等库结合使用，进行数据可视化，大家需要学习如何使用这些库进行可视化和图表绘制。

时间序列：Pandas 中的时间序列是一种强大的数据结构，用于处理时间相关的数据，它能够轻松地对时间索引的数据进行清理、切片、聚合和频率转换等操作。同时，配合Statsmodels 等Python 库，可以进一步完成时间序列分析、建模模拟、机器学习等。

## 19.2 创建数据帧：从字典、列表、NumPy 数组 …

在 Pandas 中，可以使用多种方法创建 DataFrame，下面介绍几种常用方法。

字典dict 可以用Python 中的字典dict 来创建Pandas DataFrame。字典的键 key 将成为DataFrame 的列标签， 而字典的值value 将成为DataFrame 的列数据。图 2 给出了一个示例。

a 将pandas 导入，并定义别名pd。运行后，Pandas 库将被导入，然后可以使用别名pd 来调用 Pandas 的函数和类，例如pd.DataFrame()、pd.Series() 等等。

b 构造一个字典。字典的键分别是'Integer'、'Greek'，对应DataFrame 的列标签。每个键对应的值是一个列表，这些列表将成为DataFrame 中相应列的数据。

请确保字典中的每个值 (列表) 的长度相同，以便正确创建DataFrame。如果长度不一致，将会引发异常，异常信息为'ValueError: All arrays must be of the same length'。

c 利用pandas.DataFrame() 创建一个二维数据结构称为DataFrame。

Page 4  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com d 利用pandas.DataFrame.set_index() 将数据帧的 'Integer' 这一列设置为行标签，原理如图 3 所示。此外，可以用pandas.DataFrame.reset_index() 重置行标签，将行标签设置为从0 开始的整数索引，同时加一个原来的行标签转换成一个新的列。使用pandas.DataFrame.reset_index() 时，如果设置 drop=True，原来的行标签将会被删除。

import pandas as pd # 用字典 dict 创建数据帧 dict_eg = {'Integer': [1, 2, 3, 4, 5], 'Greek': ['alpha','beta','gamma', 'delta','epsilon']} df_from_dict = pd.DataFrame(data=dict_eg)

# 采用默认行索引，Zero-based numbering # 将特定列设定为索引 df_from_dict2 = df_from_dict.set_index('Integer')

a b

图 2. 用字典创建Pandas 数据帧

X1 X2 X3 X4 X1 X2 X3 X4 pandas.DataFrame.set_index('X1')

pandas.DataFrame.reset_index()

图 3. 设置DataFrame 的索引

列表list 还可以使用Python 中的列表 list 来创建Pandas DataFrame。列表 list 每个列代表DataFrame 的一列数据，如图 4 所示。

Page 5  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd # 用列表 list 创建数据帧 list_fruits = [['apple',  11], ['banana', 22], ['cherry', 33], ['durian', 44]]

df_list1 = pd.DataFrame(list_fruits)

# 采用默认行索引、列标签，Zero-based numbering # 设定行索引 df_list1.set_axis(['a', 'b', 'c', 'd'], axis='index')

# 设定行标签 df_list1.set_axis(['Fruit', 'Number'], axis='columns')

# 设定行索引、列标签 df_list2 = pd.DataFrame(list_fruits, columns=['Fruit', 'Number'], index = ['a', 'b', 'c', 'd'])

b a e

图 4. 用列表创建Pandas 数据帧图 4 中a 构造了一个4 行、2 列的列表。b 利用 pandas.DataFrame() 将列表转化为Pandas 数据帧。

pandas.DataFrame() 这个函数的重要参数有pandas.DataFrame(data = …, index = …, columns = …)。其中，data 可以是各种数据类型，包括字典、列表、NumPy 数组、Pandas Series 等。这些数据将用于构建 DataFrame 的内容。而index 用于指定行标签的数据。注意，index 是一个可选参数，默认为从0 开始的整数索引。函数中columns 参数用于指定列标签的数据。它也是一个可选参数，默认为从0 开始的整数索引。b 创建的数据帧的行标签、列标签均为默认从0 开始的整数索引。

对于已经创建的数据帧，可以通过pandas.DataFrame.set_axis() 修改行标签 ( e )、列标签 ( d )。

而e 创建数据帧时设定了行标签、列标签。

NumPy 数组要使用二维NumPy 数组创建Pandas DataFrame，可以直接将二维NumPy 数组作为参数传递给 Pandas.DataFrame() 函数。NumPy 数组每一行的元素将成为DataFrame 的一行，而每一列的元素将成为 DataFrame 的一列。

图 5 中a 利用numpy.random.normal() 函数生成一个形状为 (10, 4) 的二维数组，数组中的元素是从高斯分布中随机抽取的样本数据。

b 利用pandas.DataFrame() 创建数据帧，并设置列标签。

c 则是在for 循环中生成列表，然后再将其转化成数据帧。

Pandas 还支持从Excel 文件、SQL 数据库、JSON、HTML 等数据来源中读取数据来创建 DataFrame。

Page 6  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import numpy as np np_array = np.random.normal(size = (10,4))

# 形状为(10, 4)的二维数组 df_np = pd.DataFrame(np_array, columns=['X1', 'X2', 'X3', 'X4'])

# 用 for 循环生成列表 data = []

# 创建一个空list for idx in range(10): data_idx = np.random.normal(size = (1,4)).tolist()

data.append(data_idx[0])

# 注意，用list.append() 速度相对较快 df_loop = pd.DataFrame(data, columns = ['X1','X2','X3','X4'])

b a

图 5. 用NumPy 数组创建Pandas 数据帧

## 19.3 数据帧操作：以鸢尾花数据为例

本书前文介绍过鸢尾花数据集 (Fisher's Iris data set)。这一节我们利用鸢尾花数据集介绍常用数据帧操作。

导入鸢尾花数据图 6 所示为从Seaborn 库中导入鸢尾花数据集。

a 导入Seaborn 库时使用的as sns 是给Seaborn 库起了一个别名，以方便在代码中使用。

b 利用seaborn.load_dataset() 函数导入鸢尾花数据集，格式为数据帧。在Seaborn 中，"iris"数据集通常是以Pandas DataFrame 的形式加载的，它包含了150 行和5 列，具体如表 1 所示。每个鸢尾花样本在DataFrame 中都有一个唯一的行标签 (也是默认行整数索引)，通常从0 到149。

鸢尾花样本DataFrame 列标签有5 个：(第0 列) 'sepal_length' 萼片长度，浮点数类型；(第1 列)

'sepal_width' 萼片宽度，浮点数类型；(第2 列) 'petal_length'：花瓣长度，浮点数类型；(第3 列)

'petal_width' 花瓣宽度，浮点数类型；(第4 列) 'species'：鸢尾花的品种，字符串类型。

c 利用seaborn.heatmap() 可视化鸢尾花数据集前四列，具体如图 7 所示。c 代码中iris_df.iloc[:, 0:4]

利用pandas.dataframe.iloc[] 对Pandas DataFrame 进行切片操作，用于从DataFrame 中选择特定的行和列。[:, 0:4]: 这是对DataFrame 进行切片的部分。在iloc 中，第一个冒号 : 表示选择所有的行，而0:4 表示选择列的范围，即列索引位置从0 到3，不包括4。Python 的切片操作通常是左闭右开区间，所以0:4 选择了索引位置0、1、2 和3 的列。

下一章专门介绍Pandas 数据帧的索引和切片。

Page 7  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import seaborn as sns import matplotlib.pyplot as plt iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 用热图可视化鸢尾花数据 fig,ax = plt.subplots(figsize = (5,9))

sns.heatmap(iris_df.iloc[:, 0:4], cmap = 'RdYlBu_r', ax = ax, vmax = 0, vmin = 8, cbar_kws = {'orientation':'vertical'}, annot=False)

# 将热图以SVG格式保存 fig.savefig('鸢尾花数据dataframe.svg', format='svg')

a b

图 6. 从Seaborn 中导入鸢尾花数据集，格式为数据帧

表 1. 鸢尾花样本数据构成的数据帧 Index sepal_length sepal_width petal_length petal_width species 5.1 3.5 1.4 0.2 setosa 4.9 1.4 0.2 setosa 4.7 3.2 1.3 0.2 setosa 4.6 3.1 1.5 0.2 setosa 3.6 1.4 0.2 setosa ...

...

...

...

...

...

6.7 5.2 2.3 virginica 6.3 2.5 1.9 virginica 6.5 5.2 virginica 6.2 3.4 5.4 2.3 virginica 5.9 5.1 1.8 virginica

pandas.DataFrame.to_csv() 将DataFrame 数据保存为CSV (逗号分隔值，comma-separated values) 文件。CSV 是一种常见的文本文件格式，用于存储表格数据，每行代表一条记录，每个字段由逗号或其他特定字符分隔。

pandas.DataFrame.to_string() 将DataFrame 数据转换为字符串格式。

Page 8  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 7. 热图可视化鸢尾花数据集数据帧

数据帧基本信息 Pandas 提供很多函数查询数据帧信息，表 2 介绍几个常用函数。

表 2. 获取数据帧基本信息的几个常用函数 (属性、方法)

函数用法 pandas.DataFrame.index

查询数据帧的行标签。

比如iris_df.index 的结果为'RangeIndex(start=0, stop=150, step=1)'。

如果想要知道行标签的具体值，则用 list(iris_df.index)。

以下是获取数据帧行数的几种不同方法： iris_df.shape[0]

len(iris_df)

len(iris_df.index)

len(iris_df.axes[0])

pandas.DataFrame.columns

查询数据帧的列标签。

比如iris_df.columns 的结果为'Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], dtype='object')'。同样list(iris_df.columns) 可以得到列标签的列表。

以下是获取数据帧列数的几种不同方法： iris_df.shape[1]

Page 9  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com len(iris_df.T) # T len(iris_df.columns)

len(iris_df.axes[0]

pandas.DataFrame.axes

同时获得数据帧的行标签、列标签。

比如iris_df.axes 的结果为[RangeIndex(start=0, stop=150, step=1), Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], dtype='object')]。

pandas.DataFrame.values

用于返回数据帧中的实际数据部分作为一个多维 NumPy 数组。返回的数组可以用于进行数值计算、传递给其他库或以其他方式处理数据。

比如，iris_df.values 返回的是二维NumPy 数组。

pandas.DataFrame.info 获取关于数据帧摘要信息，比如数据帧的结构、数据类型、缺失值情况、内存占用等基本信息，对于数据的初步探索和诊断非常有用。

pandas.DataFrame.describe()

Statistics

用于生成关于数据帧统计摘要信息。它提供了数据的基本统计信息，如计数、均值、标准差、最小值、最大值和分位数等。本书后文将专门介绍数据帧运算，其中包括统计运算。

比如，iris_df.describe()计算鸢尾花列数据统计值。

如果想要打印小数点后一位，可以用iris_df.describe().round(1)。

pandas.DataFrame.nunique()

.nunique

用于计算数据帧中每一列的唯一值/独特值 (unique value) 数量。

比如，对于鸢尾花数据来说，最后一列 (species) 的唯一值个数为3。

类似地，pandas.unique() 可以计算得到数据帧某一列的具体唯一值。

比如，iris_df['species'].unique() 的结果为 array(['setosa', 'versicolor', 'virginica'], dtype=object)。

pandas.DataFrame.head()

用于查看数据帧的前几行数据，默认情况下，返回数据帧的前 5 行。

比如，iris_df.head(2) 返回数据帧前2 行。

pandas.DataFrame.tail()

用于查看数据帧的后几行数据，默认情况下，返回数据帧的后 5 行。

比如，iris_df.tail(2) 返回数据帧后2 行。

pandas.DataFrame.shape 用于获取数据帧的维度信息。函数返回一个元组，其中包含数据帧的行数、列数。

比如，iris_df.shape 返回的结果为 (150, 5)。

Page 10  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

pandas.DataFrame.size 用于返回数据帧中元素，即数据单元格总数，就是数据帧行数乘以列数的结果。

比如，iris_df.size 返回的结果为750。

pandas.DataFrame.count()

.count()

返回数据帧每列 (默认axis=0) 非缺失值数量。这个函数可以快速了解每列中有多少个有效的非缺失数据，这对于数据清洗和数据质量的检查非常有用。将参数设置为axis=1，可以查询每行的非缺失值数量。

比如，iris_df.count() * 100 / len(iris_df) 计算每一列非缺失值的百分比。

pandas.DataFrame.isnull()

用于检查DataFrame 中的每个元素是否为缺失值NaN。函数返回一个与原始 DataFrame 结构相同的布尔值DataFrame，其中的每个元素都对应于原始 DataFrame 中的一个元素，并且其值为True 表示该元素是缺失值，False 表示该元素不是缺失值。

比如，iris_df.isnull().sum() * 100 / len(iris_df) 计算每一列缺失值百分比。

循环如图 8 所示，在Pandas 中可以使用iterrows() 方法来遍历DataFrame 的行，或者使用iteritems() 或 items() 方法来循环DataFrame 的列。另外，还可以直接使用for 循环来遍历DataFrame 的列。

import pandas as pd import seaborn as sns iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 遍历数据帧的行 for idx, row_idx in iris_df.iterrows(): print('=================')

print('Row index =',str(idx))

print(row_idx['sepal_length'], row_idx['sepal_width'])

# 遍历数据帧的列 for column_idx in iris_df.iteritems(): print(column_idx)

a b

图 8. 遍历数据帧行、列

修改数据帧 Pandas 还提供了各种修改数据帧行标签、列标签函数，如。

Page 11  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

表 3. 修改数据帧行标签、列标签函数用法 pandas.DataFrame.rename()

对DataFrame 的索引标签、列标签或者它们的组合进行重命名。

需要注意的是，rename()方法默认返回新的DataFrame，如果想要在原地修改 DataFrame，可以将inplace=True 参数设置为True。

比如，对列标签重命名： iris_df.rename(columns={'sepal_length': 'X1', 'sepal_width':  'X2', 'petal_length': 'X3', 'petal_width':  'X4', 'species':      'Y'})

比如，对行标签重命名，给每个行标签前面加前缀idx_： iris_df.rename(lambda x: f'idx_{x}')

每个行标签后面加后缀_idx： iris_df.rename(lambda x: f'{x}_idx')

pandas.DataFrame.add_suffix() 给DataFrame 的列标签添加后缀，并返回一个新的DataFrame，原始 DataFrame 保持不变。这个方法对于在合并多个DataFrame 时，避免列名冲突很有用。通过添加后缀，可以清楚地区分来自不同DataFrame 的列。

比如，iris_df_suffix = iris_df.add_suffix('_col')

以上数据帧要想除去列标签后缀_col，可以用： iris_df_suffix.rename(columns = lambda x: x.strip('_col'))

pandas.DataFrame.add_prefix() 给DataFrame 的列标签添加前缀，并返回一个新的DataFrame，原始 DataFrame 保持不变。这个方法对于在合并多个DataFrame 时，避免列名冲突很有用。通过添加前缀，可以清楚地区分来自不同DataFrame 的列。

比如，iris_df_prefix = iris_df.add_prefix('col_').head()

以上数据帧要想除去列标签前缀col_，可以用： iris_df_prefix.rename(columns = lambda x: x.strip('col_'))

更改列标签顺序如图 9 所示，数据帧创建后，列标签的顺序可以根据需要进一步修改。

Page 12  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X1 X2 X3 X4 X1 X2 X3 X4 df[new_col_order]

df.reindex(colums = new_col_order)

df.loc[:, new_col_order]

df.iloc[:, new_col_order_0_based]

df.set_axis(new_col_order, axis = 1)

图 9. 修改列标签顺序 pandas.DataFrame.reindex() 方法用于重新排序DataFrame 的列标签。

一般来讲，pandas.DataFrame.loc() 可以用来索引、切片数据帧；当然这个方法也可以用来重新排序列标签。下一章将专门介绍数据帧索引和切片。

pandas.DataFrame.iloc() 是 pandas 中用于通过整数索引来选择 DataFrame 的行和列的索引器。与 pandas.DataFrame.loc 不同，iloc 使用整数索引而不是标签索引。

import pandas as pd import seaborn as sns iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 自定义列标签顺序 new_col_order = ['species', 'sepal_length', 'petal_length', 'sepal_width', 'petal_width']

df_1 = iris_df[new_col_order]

df_2 = iris_df.reindex(columns=new_col_order)

df_3 = iris_df.loc[:, new_col_order]

df_4 = iris_df.iloc[:, [4,0,2,1,3]]

df_5 = iris_df.set_axis(new_col_order, axis=1)

a b e

图 10. 修改列标签顺序

更改行标签顺序图 11 介绍几种修改行标签顺序的方法。

a 用pandas.DataFrame.reindex() 重新排序DataFrame 的行标签。

b 用pandas.DataFrame.loc() 通过定义行标签来重新排序DataFrame 行顺序。下一章还会用这个函数在axis = 0 方向进行索引、切片。c 用pandas.DataFrame.loc() 通过定义整数行标签来重新排序 DataFrame 行顺序。d pandas.DataFrame.sort_index() 按照索引的升序或降序对DataFrame 进行重新排序，默认 axis = 0。

Page 13  |  Chapter 19 聊聊Pandas  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

a b import pandas as pd import seaborn as sns iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 取出前5行，并修改行索引 iris_df_ = iris_df.iloc[:5,:].rename(lambda x: f'idx_{x}')

# 重新排序列索引 new_order = ['idx_4','idx_2','idx_0','idx_3','idx_1']

df_1 = iris_df_.reindex(new_order)

df_2 = iris_df_.loc[new_order]

new_order_int = [4, 2, 0, 3, 1]

iris_df_.iloc[new_order_int]

iris_df_.sort_index(ascending=False)

图 11. 修改行标签顺序删除 pandas.DataFrame.drop() 方法用于从DataFrame 中删除指定的行或列。默认情况下，drop() 方法不对原始DataFrame 做修改，而是返回一个修改后的副本。将inplace 参数设置为True，inplace = True, 可以在原地修改DataFrame，而不返回一个新的DataFrame。

import pandas as pd import seaborn as sns iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 删除特定行 iris_df.drop(index=[0,1])

# 删除特定列 iris_df.drop(columns='species')

a b

图 12. 删除特定行、列

Pandas 库最佳参考资料莫过于“Pandas 之父”Wes McKinney 创作的Python for Data Analysis，全书开源，地址为： https://wesmckinney.com/

Page 1  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Indexing and Slicing Pandas DataFrame Pandas 索引和切片利用DataFrame 的行列标签、整数索引

生命就是一个实验。实验做的越多，越好。

All life is an experiment. The more experiments you make, the better.

—— 拉尔夫·沃尔多·爱默生 (Ralph Waldo Emerson)  |  美国思想家、文学家  | 1942 ~ 2018

◄ pandas.dataframe.iloc() 通过整数索引来选择 DataFrame 的行和列的索引器 ◄ pandas.DataFrame.isin() 于检查DataFrame 中的元素是否在给定的值序列中 ◄ pandas.dataframe.loc() 通过标签索引来选择 DataFrame 的行和列的索引器 ◄ pandas.DataFrame.query() 筛选和过滤DataFrame 数据的方法 ◄ pandas.DataFrame.where() 在DataFrame 中根据条件对元素进行筛选和替换的方法 ◄ pandas.MultiIndex.from_arrays() 用于从多个数组创建多级索引的方法 ◄ pandas.MultiIndex.from_frame() 用于从DataFrame 创建多级索引的方法 ◄ pandas.MultiIndex.from_product() 用于从多个可迭代对象的笛卡尔积创建多级索引的方法 ◄ pandas.MultiIndex.from_tuples() 用于从元组列表创建多级索引的方法

Page 2  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 20.1 数据帧的索引和切片

Pandas 的数据帧和NumPy 数组这两种数据结构在Python 数据科学生态系统中都扮演着重要的角色，但它们在索引和切片上有一些异同之处。

NumPy 数组一般是一个多维的、同质的数据结构，意味着NumPy 数组通常包含相同数据类型的元素，并且维度是固定的。NumPy 数组使用基于0 的整数索引。

Pandas 数据帧一般是一个二维的、异质的数据结构，可以包含不同数据类型的列，并且可以拥有拥有灵活的行和列标签。

NumPy 数组使用整数索引来访问元素，类似于Python 的列表索引。例如，对于二维数组array，可以使用array[row_index, column_index] 来获取元素。

上一章提过，行标签、列标签特指数据帧的标签；而对于数据帧，行索引、列索引则是指行列整数索引，这一点类似NumPy 二维数组。默认情况下，数据帧行标签、列标签均为基于0 的整数索引。

Pandas 数据帧使用行列标签来进行索引和切片。类似NumPy 数组，Pandas 数据帧还可以使用.iloc[]

属性可以通过整数索引完成索引、切片。

n × D n rows D columns X1 X2 X3 X4 axis = 0 axis = 1 Index Columns n ...

...

D ...

D n ...

idx_0 idx_1 idx_2 idx_3 idx_n ...

图 1. 比较NumPy array 和Pandas DataFrame 索引

## 20.2 提取特定列

图 2 所示为从数据帧取出特定一列的几种方法。

其中，pandas.DataFrame.loc[] 是Pandas 中用于基于标签进行索引和切片重要工具，允许通过指定行标签、列标签来选择数据帧中的特定行和列，或者获取特定行或列上的值。

而pandas.DataFrame.iloc[] 是Pandas 中用于基于整数位置进行索引和切片的工具，方括号内的索引规则和NumPy 二维数组完全一致。pandas.DataFrame.iloc[] 允许通过指定行的整数位置和列的整数位置来选择数据帧中的特定行和列，或者获取特定行或列上的值。

Page 3  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 特别需要大家注意的是左侧的方法返回的是Pandas Series (相当于一维数组)，而右边的方法返回的是Pandas DataFrame (相当于二维数组)。

X1 X2 X3 X4 df[['X1']]

df.loc[:,['X1']]

df.iloc[:,[0]]

X1 DataFrame df['X1']

df.X1 df.loc[:,'X1']

df.iloc[:,0]

Series

图 2. 提取一列图 3 所示为从数据帧中取出连续多列的几种方法。相比而言，采用pandas.DataFrame.iloc[] 取出连续多列最方便。类似NumPy 数组，还可以利用pandas.DataFrame.iloc[]等间隔提取特定列，比如 df.iloc[:, ::2] 从第0 行开始每2 列取一列。图 4 则展示从数据帧取出不连续多列的方法。

X1 X2 X3 X4 df[['X1','X2','X3']]

df.loc[:,['X1','X2','X3']]

df.iloc[:,0:3]

df.iloc[:,:3]

X1 X2 X3

图 3. 提取多列，连续 X4 X1 X2 X3 X4 df[['X1', 'X4']]

df.loc[:,['X1', 'X4']]

df.iloc[:,[0, 3]]

X1

图 4. 提取多列，不连续

## 20.3 提取特定行

图 5 所示为提取特定一行的几种方法。也需要大家注意的是，左侧提取结果为Pandas Series，右侧提取结果为Pandas DataFrame。此外，'idx_0' 为认为设定的行标签；数据帧采用的是默认从0 开始的整数索引，则其行标签、行整数索引都是0。

Page 4  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X1 X2 X3 X4 df.loc[['idx_0']]

df.iloc[[0]]

DataFrame df.loc['idx_0']

df.iloc[0]

Series X1 X2 X3 X4 X1 X2 X3 X4

图 5. 提取一行

图 6 所示为从数据帧中取出连续多行的几种方法。相比而言，采用pandas.DataFrame.iloc[] 取出连续多行比较容易。类似NumPy 数组，还可以利用pandas.DataFrame.iloc[]等间隔提取特定行，比如 df.iloc[::2] 从第0 行开始每2 行取一行。图 7 则展示从数据帧取出不连续多行的方法。

X1 X2 X3 X4 df.iloc[0:3]

df.iloc[:3]

df.iloc[[0,1,2]]

df.loc[['idx_0','idx_1','idx_2']]

X1 X2 X3 X4

图 6. 提取多行，连续

X1 X2 X3 X4 df.iloc[[0,50,100]]

df.loc[['idx_0','idx_50','idx_100']]

X1 X2 X3 X4

图 7. 提取多行，不连续

## 20.4 提取特定元素

利用pandas.DataFrame.iloc[row_position, column_position]，我们可以取得数据帧的特定位置元素， 这一点和NumPy 二维数组相同；本章配套代码提供若干示例，请大家自行学习。

本节要特别介绍at 和 iat 方法。它俩是 Pandas DataFrame 中的快速访问器，用于在 DataFrame 中访问单个元素。

Page 5  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com at 是基于标签的访问器，可以通过标签 (行标签、列标签) 快速获取数据帧单个元素，速度比 loc 快。

iat 是基于整数索引的访问器，可以通过整数索引 (行索引、列索引) 快速获取单个元素，速度比 iloc 快。

注意，使用 at 和 iat 访问器，只能访问单个元素，返回结果为具体元素。如果需要访问多个元素， 应该使用 loc 或 iloc。

X1 X2 X3 X4 df.at['idx_0', 'X1']

df.iat[0, 0]

df.loc['idx_0', 'X1']

df.iloc[0,0]

5.1 5.1 X1 df.loc[['idx_0'], ['X1']]

df.iloc[[0],[0]]

图 8. 提取特定元素

## 20.5 条件索引

在Pandas 中，条件索引是通过布尔条件 (Boolean expression) 筛选数据帧中的行的一种技术。这意味着可以基于某些条件从数据帧中选择满足这些条件的特定行。条件索引使用布尔运算，如>、<、 ==、!=、&、| 等等，来生成布尔值的数据帧，然后根据这些布尔值来筛选数据帧。

布尔条件如图 9 所示，左侧的df 为鸢尾花数据集前4 列构成的数据帧。布尔运算 (df > 6) | (df < 1.5) 通过 | 或运算结合两个不等式，含义是数据帧中满足大于6 或小于1.5 的元素设为True，否则设为False。图 9 右侧的热图中深蓝色色块代表True，浅蓝色色块代表False。图 9 右侧这种方案还会用在可视化数据帧中缺失值。

(df > 6) | (df < 1.5)

X1 X2 X3 X4 X1 X2 X3 X4

图 9. 满足条件的布尔数据帧

Page 6  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 10 利用布尔数据帧筛选满足条件的行。其中，a 创建了一个布尔条件数据帧，用于筛选iris_df 中 "sepal_length"列大于等于7 的行。b 使用上面创建的布尔条件condition 对iris_df 进行筛选，得到一个新的DataFrame iris_df_filtered，其中只包含"sepal_length"列大于等于7 的行，具体如图 11 所示。

import pandas as pd import seaborn as sns iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 使用 drop(..., inplace=True) 删除一列 iris_df.drop(columns='species', inplace=True)

condition = iris_df['sepal_length'] >= 7 # 创建了一个布尔条件condition数据帧 iris_df_filtered = iris_df[condition]

# 只包含"sepal_length"列大于等于7的行 a b

图 10. 利用布尔条件筛选数据帧

df[df['sepal_length'] >= 7]

X1 X2 X3 X4 X1 X2 X3 X4

图 11. 满足条件的布尔数据帧

loc[]

实践中，一般更常用 loc[] 筛选满足条件的数据帧。举个例子，图 11 筛选可以通过这句话完成 df.loc[df.loc[:,'sepal_length'] >= 7, :]。

本章配套Jupyter Notebook 给出更多实例，请大家自行学习。

表 1. 利用loc[] 筛选示例示例 (假设df 为鸢尾花数据集)

说明 df.loc[df.loc[:,'species'] == 'versicolor', :]

df.loc[df.species == 'versicolor', :]

条件：鸢尾花种类 'species' 为 (==)

'versicolor' df.loc[(df.sepal_length < 6.5) & (df.sepal_length > 6)]

条件：鸢尾花花萼长度 'sepal_length' 小于 (<) 6.5 且 (&) 大于 (>) 6

Page 7  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com df.loc[(df.loc[:, 'sepal_length'] < 6.5) & (df.loc[:, 'sepal_length'] > 6)]

df.loc[(df.loc[:, 'sepal_length'] < 6.5) & (df.loc[:, 'sepal_length'] > 6), ['petal_length', 'petal_width']]

条件：鸢尾花花萼长度 'sepal_length' 小于 (<) 6.5 且 (&) 大于 (>) 6 返回：df 中'petal_length'和 'petal_width'两列，同时满足两个条件 df.loc[df['species'] != 'virginica']

条件：鸢尾花种类 'species' 不是 (!=)

'virginica' df.loc[df['species'].isin(['virginica','setosa'])]

df.loc[df.species.isin(['virginica','setosa'])]

条件：鸢尾花种类 'species' 在 (isin) 列表 ['virginica','setosa'] 之中 df.loc[~df.species.isin(['virginica','setosa']), ['petal_length', 'petal_width']]

条件：鸢尾花种类 'species' 不在 (~ … isin) 列表 ['virginica','setosa'] 之中返回：df 中'petal_length'和 'petal_width'两列，满足条件所有行

query()

query(expression) 是Pandas 中的一个方法，用于对数据帧进行查询操作。它允许通过指定一定的查询条件来筛选数据，并返回满足条件的行。其中，expression 是一个字符串，表示查询表达式，描述了筛选条件。通常，expression 由列名和运算符组成，可以使用布尔运算符，如==、!=、> 、<、>=、<= 等，来指定条件。还可以使用and、or 和not 等逻辑运算符来组合多个条件。默认inplace = False，即不在原地修改数据帧。如果inplace=True，则会直接在原始数据帧上进行修改，不返回一个新的数据帧。

表 2 给出若干示例，query() 内的条件很容易理解，请大家自行学习。

表 2. 利用query() 筛选示例示例 (假设df 为鸢尾花数据集)

df.query('sepal_length > 2*sepal_width')

df.query("species == 'versicolor'")

df.query("not (sepal_length > 7 and petal_width > 0.5)")

df.query("species != 'versicolor'")

df.query("abs(sepal_length-6) > 1")

df.query("species in ('versicolor','virginica')")

df.query("sepal_length >= 6.5 or sepal_length <= 4.5")

df.query("sepal_length <= 6.5 and sepal_length >= 4.5")

Page 8  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 20.6 多层索引

在Pandas 中，多级索引 (multi-index) 是一种特殊的索引类型，允许在数据帧的行或列上具有多个层次的索引。这使得我们可以在更复杂的高维数据集上进行分层操作和查询。

多层行标签图 12 所示为用列表创建两层行标签数据帧。

import pandas as pd import numpy as np # 创建列表、数据 index_arrays = [['A','A','B','B','C','C','D','D'], range(1,9)]

data = np.random.randint(0,9,size=(8,4))

# 创建多层行索引 row_idx = pd.MultiIndex.from_arrays(index_arrays, names=['I','II'])

# 创建DataFrame df = pd.DataFrame(data, index=row_idx, columns=['X1','X2','X3','X4'])

a b

图 12. 用列表构造多层行标签

a 利用pandas.MultiIndex.from_arrays() 构造两层行标签，结果为： MultiIndex([('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5), ('C', 6), ('D', 7), ('D', 8)], names=['I', 'II'])

b 构造两层行标签数据帧，如图 13 左图所示。图 14 所示为用loc[] 对两层行标签索引、切片。类似地，我们还可以利用pandas.MultiIndex.from_tuples() 从元组列表创建多级索引。此外， pandas.MultiIndex.from_frame() 是用于从DataFrame 创建多级索引的方法。请大家参考本章配套的 Jupyter Notebook 自行学习。

Page 9  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X1 X2 X3 X4 II I A B C D X1 X2 X3 X4 II I A B C D A B C D 2 levels df.reset_index()

1 level

图 13. 两层行标签 X1 X2 X3 X4 II I A B C D df.loc[[('A', 1)]]

X1 X2 X3 X4 II I A X1 X2 X3 X4 df.loc[('A', 1)]

df.loc[('A', 1),'X1']

X1 X2 X3 X4 II df.loc['A']

X1 X2 X3 X4 II I A B Pandas series df.loc[('A', 1):('C',1)]

图 14. 两层行标签，索引、切片

图 15 利用中利用pandas.MultiIndex.from_product()从多个可迭代对象的笛卡尔积创建多层行索引。图 15 产生如图 16 两个双层行标签数据帧。

Page 10  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import numpy as np # 示例数据 data = np.random.randint(0,9,size=(8,4))

# 两组列表 categories = ['A','B','C','D']

types = ['X', 'Y']

# 创建多层行索引，先categories，再types idx_1 = pd.MultiIndex.from_product([categories, types], names=['I', 'II'])

df_1 = pd.DataFrame(data, index=idx_1, columns=['X1','X2','X3','X4'])

# 创建多层行索引，先types，再categories idx_2 = pd.MultiIndex.from_product([types, categories], names=['I', 'II'])

df_2 = pd.DataFrame(data, index=idx_2, columns=['X1','X2','X3','X4'])

a b

图 15. 用多个可迭代对象的笛卡尔积构造多层行标签

X1 X2 X3 X4 X Y X Y X Y X Y II I A B C D 2 levels X1 X2 X3 X4 A B C D A B C D II I X Y 2 levels

图 16. 两层行标签，笛卡尔积

图 17 所示为将DataFrame 的索引转换为字符串类型，并且每个索引元素中的多个级别值用下划线连接成一个字符串。

Page 11  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X1 X2 X3 X4 X Y X Y X Y X Y II I A B C D 2 levels df.index = df.index.map('_'.join)

X1 X2 X3 X4 A_X A_Y B_X B_Y C_X C_Y D_X D_Y

图 17. 两层行标签降为一层

多层列标签图 18 所示为用列表创建两层列标签数据帧，如图 19 左图所示。本章配套的Jupyter Notebook 还介绍了利用笛卡尔积、元组、数据帧创建多层列标签数据帧，请大家自行学习。图 20 所示为利用loc[] 对多层列标签进行索引、切片。

import pandas as pd import numpy as np # 示例数据 data = np.random.randint(0,9,size=(8,4))

# 创建两层列标签列表 col_arrays = [['A',  'A',  'B',  'B'], ['X1', 'X2', 'X3', 'X4']]

# 创建两层列索引 multi_col = pd.MultiIndex.from_arrays(col_arrays, names=['I','II'])

# 创建DataFrame df = pd.DataFrame(data, columns=multi_col)

a

图 18. 用列表构造多层列标签

Page 12  |  Chapter 20 Pandas 索引和切片  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com df.columns = df.columns.map('_'.join)

A_X1 A_X2 B_X3 B_X4 X1 X2 X3 X4 A B I II

图 19. 两层行标签降为一层

df.A.X1 df.loc[:,'A'].X1 df.loc[:,('A','X1')]

df.loc[:,'A'].loc[:,'X1']

X1 X2 X3 X4 A B I II df.loc[:,['A']]

X1 X2 A I II X1 A I II df.loc[:,[('A','X1')]]

X1 II df.loc[:,'A'].loc[:,['X1']]

图 20. 两层列标签，索引、切片

Page 1  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Joining and Merging Pandas DataFrames Pandas 拼接和合并介绍concat()、join()、merge() 三种方法

希望，是一个醒来的梦想。

Hope is a waking dream.

—— 亚里士多德 (Aristotle)  |  古希腊哲学家  |  384 ~ 322 BC

◄ pandas.concat() 将多个数据帧在特定轴 (行、列) 方向进行拼接 ◄ pandas.DataFrame.drop() 删除数据帧特定列 ◄ pandas.DataFrame.join() 将两个数据集按照索引或指定列进行合并 ◄ pandas.DataFrame.merge() 按照指定的列标签或索引进行数据库风格的合并

Page 2  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 21.1 Pandas 数据帧拼接、合并

Pandas 是一种用于数据处理和分析的Python 库，它提供了多种数据规整方法来整理和准备数据，使之能够更方便地进行分析和可视化。下面总结一些常用的数据规整方法。

将不同数据源的数据合并成一个数据集是数据规整的常见需求之一。Pandas 提供了多种方法进行数据合并和连接，比如，方法 concat() 将多个数据帧在特定轴方向进行拼接。方法 join() 将两个数据集按照索引或指定列进行合并。方法merge() 按照指定的列标签或索引进行数据库风格的合并。

本章将介绍这三种方法。

## 21.2 拼接：pandas.concat()

pandas.concat() 是 pandas 库中的一个函数，用于将多个数据结构按照行或列的方向进行合并。它可以将数据连接在一起，形成一个新的 DataFrame。

这个函数的主要参数为pandas.concat(objs, axis=0, join='outer', ignore_index=False)。

参数objs: 这是一个需要连接的对象的列表，比如 [df1, df2, df3]。

参数axis 指定连接的轴向，可以是 0 或 1，默认为0；0 表示按行连接 (如图 2 所示)，1 表示按列连接 (如图 3 所示)。

参数join 指定拼接的方式，可以是 'inner'、'outer'，默认是 'outer'。'inner' 表示内连接，只保留两个数据集中共有的列/行。'outer' 表示外连接，保留所有列/行，缺失值用 NaN 填充。

图 1 给出的代码比较 'outer' 和 'inner'和两种拼接方式。

import pandas as pd # 创建两个数据帧 df1 = pd.DataFrame({'X1': [1, 2, 3], 'X2': ['X', 'Y', 'Z']}, index=[0, 1, 2])

df2 = pd.DataFrame({'X3': ['A', 'B', 'C'], 'X4': [4, 5, 6]}, index=[1, 2, 3])

# 'outer' 方法拼接 df_outer = pd.concat([df1, df2], join='outer', axis=1)

# 'inner' 方法拼接 df_inner = pd.concat([df1, df2], join='inner', axis=1)

a b

图 1. 用concat() 拼接，比较 'outer' 和 'inner'

a 的结果如图 4 所示，图中 × 代表NaN 缺失值。b 的结果如图 5 所示。

Page 3  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 参数ignore_index 为布尔值，默认为False；如果设置为 True，将会重新生成索引，忽略原来的索引。

X1 X2 X3 X4 X1 X2 X3 X4 X1 X2 X3 X4 pandas.concat([df1,df2])

axis = 0 axis = 0

图 2. 利用pandas.concat() 完成轴方向拼接，axis = 0 (默认)

X1 X2 X3 X4 X1 X2 X3 X4 pandas.concat([df1,df2], axis = 1)

axis = 1 axis = 1 axis = 1

图 3. 利用pandas.concat() 完成轴方向拼接，axis = 1

Page 4  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X3 X4 join = 'outer' df1 df2 X1 X2 X3 X4 X1 X2 pd.concat([df1, df2], join='outer', axis=1)

图 4. 利用pandas.concat() 完成合并，join = 'outer' join = 'inner' X3 X4 X1 X2 X1 X2 X3 X4 pd.concat([df1, df2], join='inner', axis=1)

df1 df2

图 5. 利用pandas.concat() 完成合并，join = 'inner'

## 21.3 合并：pandas.join()

在 Pandas 中，join 是 DataFrame 对象的一个方法，用于按照索引 (默认) 或指定列合并两个 DataFrame。

这个函数的主要参数为DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='')。

参数other 是要连接的另一个 DataFrame。

参数on 是指定连接的列名或列标签级别 (多级列标签的情况) 的名称。如果不指定，将会以两个 DataFrame 的索引为连接依据。

参数how 指定连接方式，可以是 'left' (左连接)、'right' (右连接)、'outer' (外连接)、'inner' (内连接) 或 'cross' (交叉连接)，默认是 'left'。图 6 代表比较 'left'、'right'、'outer'、'inner' 这四种方法。

如图 7 所示，'left' 使用左侧 DataFrame 的索引或指定列进行合并。

如图 8 所示，'right' 使用右侧 DataFrame 的索引或指定列进行合并。

如图 9 所示，'outer' 使用两个 DataFrame 的并集索引或指定列进行合并，缺失值用 NaN 填充。

如图 10 所示，'inner' 使用两个 DataFrame 的交集索引或指定列进行合并。

如图 11 代码所示，'cross' 连接是一种笛卡尔积的连接方式，它会将两个 DataFrame 的所有行进行组合，从而得到两个 DataFrame 之间的所有可能组合。图 12 给出这种合并方法的图解。

Page 5  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 'cross' 这种连接方式在 SQL 中称为 "CROSS JOIN"。'cross' 连接方式适用于较小的 DataFrame，因为连接后的结果行数会呈指数增长。如果 DataFrame 较大，这种连接方式可能会导致非常庞大的结果，从而占用大量的内存和计算资源。因此，在使用 'cross' 连接时，应该谨慎操作，确保不会导致资源耗尽。

当连接的两个 DataFrame 中存在同名的列时，可以通过lsuffix 和 rsuffix 这两个参数为左边和右边的列名添加后缀 (suffix)，避免列名冲突。

import pandas as pd # 创建两个数据帧 df1 = pd.DataFrame({'X1': [1, 2, 3], 'X2': ['X', 'Y', 'Z']}, index=[0, 1, 2])

df2 = pd.DataFrame({'X3': ['A', 'B', 'C'], 'X4': [4, 5, 6]}, index=[1, 2, 3])

# 'left' 方法合并 df_left = df1.join(df2, how='left')

# 'right' 方法合并 df_right = df1.join(df2, how='right')

# 'outer' 方法合并 df_outer = df1.join(df2, how='outer')

# 'inner' 方法合并 df_inner = df1.join(df2, how='inner')

a b

图 6. 用join() 合并，比较 'left'、'right'、'outer'、'inner'

X3 X4 how = 'left' df1 df2 X1 X2 X3 X4 X1 X2 df1.join(df2, how='left')

图 7. 利用pandas.join() 完成合并，join = 'left'

X3 X4 how = 'right' df1 df2 X1 X2 X3 X4 X1 X2 df1.join(df2, how='right')

图 8. 利用pandas. join() 完成合并，join = 'right'

Page 6  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

X3 X4 how = 'outer' df1 df2 X1 X2 X3 X4 X1 X2 df1.join(df2, how='outer')

图 9. 利用pandas. join() 完成合并，join = 'outer' how = 'inner' X3 X4 X1 X2 X1 X2 X3 X4 df1.join(df2, how='inner')

df1 df2

图 10. 利用pandas. join() 完成合并，join = 'inner'

import pandas as pd # 创建两个数据帧 df1 = pd.DataFrame({'A': ['X', 'Y', 'Z']})

df2 = pd.DataFrame({'B': [1, 2]})

# 使用 'cross' 连接 df_cross = df1.join(df2, how='cross')

a

图 11. 用join() 合并，how = 'cross'

how = 'cross' X3 X4 X1 X2 df1.join(df2, how='cross')

df1 df2 X Y Z X1 X2 X3 X4 X Y X Y Z Z X Y Z

图 12. 利用pandas. join() 完成合并，join = 'cross'

Page 7  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 21.4 合并：pandas.merge()

实践中，相较本章前文介绍的两种方法，merge() 更灵活，可以处理更多种合并情况。merge() 可以通过指定列标签合并 (参数left_on 和 right_on，或on)，可以指定索引 (left_index 和 right_index) 合并。

merge() 还支持'left'、'right'、'outer'、'inner' 或 'cross'五种合并方法。

基于单个列合并图 13 所示为merge() 通过参数on 指定同名列标签，完成df_left 和df_right 两个数据帧合并，合并方法为 how = 'left'。如图 14 所示，当两个数据帧有同名列标签时，合并后同名标签会加后缀以便区分，默认标签为 (“_x”, “_y”)。

how = 'left' X N b M X a b pandas.merge(df_left, df_right, how = 'left', on = 'X')

df_left.merge(df_right, how = 'left', on = 'X')

left right M X N a b

图 13. 利用pandas.merge() 完成合并，how = 'left'

how = 'left' X M b M X a b pandas.merge(df_left, df_right, how = 'left', on = 'X')

df_left.merge(df_right, how = 'left', on = 'X')

left right M_x X M_y a b

图 14. 利用pandas.merge() 完成合并，how = 'left'，有列标签重名的情况

Page 8  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 基于左右列合并图 15 ~ 图 18 所示为merge() 通过指定左右数据帧的列标签 (left_on 和 right_on) 完成合并。此外， merge() 还可以指定多个列标签进行合并操作。

how = 'left' Y N b M X a b M X Y N a b b pandas.merge(df_left, df_right, how = 'left', left_on = 'X', right_on = 'Y')

df_left.merge(df_right, how = 'left', left_on = 'X', right_on = 'Y')

left right

图 15. 利用pandas.merge() 完成合并，how = 'left'

how = 'right' Y N b M X a b M X Y N b b pandas.merge(df_left, df_right, how = 'right', left_on = 'X', right_on = 'Y')

df_left.merge(df_right, how = 'right', left_on = 'X', right_on = 'Y')

left right

图 16. 利用pandas.merge() 完成合并，how = 'right' how = 'inner' Y N b M X a b M X Y N b b pandas.merge(df_left, df_right, how = 'inner', left_on = 'X', right_on = 'Y')

left right

图 17. 利用pandas.merge() 完成合并，how = 'inner'

Page 9  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com M X Y N b b a how = 'outer' Y N b M X a b pandas.merge(df_left, df_right, how = 'outer', left_on = 'X', right_on = 'Y')

df_left.merge(df_right, how = 'outer', left_on = 'X', right_on = 'Y')

left right

图 18. 利用pandas.merge() 完成合并，how = 'outer'

独有图 19 总结常用几种合并几何运算，merge() 可以直接完成前5 种，目前merge() 暂不直接支持剩下3 种。这3 种合并集合运算为： 左侧独有 (left exclusive)：只保留左侧 DataFrame 中存在，而右侧 DataFrame 中不存在的行。

右侧独有 (right exclusive)：只保留右侧 DataFrame 中存在，而左侧 DataFrame 中不存在的行。

全外独有 (full outer exclusive)：保留左侧 DataFrame 中不存在于右侧 DataFrame，同时右侧 DataFrame 中不存在于左侧 DataFrame 的行。

但是，我们可以利用merge() 完成图 19，具体代码如图 20 所示。

left right left right left right left right left right left right left right (a) left (b) right (c) inner (d) outer (e) cross (f) left exclusive (g) right exclusive (h) outer exclusive

图 19. 总结常用合并集合运算

图 20 中的a 首先利用merge() 完成左连接合并。在 pandas 的 merge() 方法中，indicator 参数用于指定是否添加一个特殊的列，该列记录了每行的合并方式。这个特殊的列名可以通过 indicator 参数进行自定义，默认为 "_merge"。"_merge" 列可以取三个值： "left_only": 表示该行只在左边的 DataFrame 中存在，即左连接中独有的行。

"right_only": 表示该行只在右边的 DataFrame 中存在，即右连接中独有的行。

Page 10  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com "both": 表示该行在两个 DataFrame 中都存在，即连接方式中共有的行。

在b 中，通过设定筛选条件，left_exl['_merge'] == 'left_only'，我们可以保留合并后的“左侧独有” 行。结果如图 21 所示。

同理，c 完成右连接合并，d 通过设定筛选条件保留数据帧中“右侧独有”行，结果如图 22 所示。类似地，e 完成外连接合并，f 通过设定筛选条件保留“全外独有”行，结果如图 23 所示。

import pandas as pd # 创建两个数据帧 left_data = { 'M': [ 1,   2,   3], 'X': ['a', 'b', 'c']} left_df = pd.DataFrame(left_data)

right_data = { 'X': ['b', 'c', 'd'], 'N': [ 22,  33,  44]} right_df = pd.DataFrame(right_data)

# LEFT EXCLUSIVE left_exl = left_df.merge(right_df, on='X', how='left', indicator=True)

left_exl = left_exl[ left_exl['_merge'] == 'left_only'].drop( columns=['_merge'])

# RIGHT EXCLUSIVE right_exl = left_df.merge(right_df, on='X', how='right', indicator=True)

right_exl = right_exl[ right_exl['_merge'] == 'right_only'].drop( columns=['_merge'])

# FULL OUTER EXCLUSIVE outer_exl = left_df.merge(right_df, on='X', how='outer', indicator=True)

outer_exl = outer_exl[ outer_exl['_merge'] != 'both'].drop( columns=['_merge'])

a b e f

图 20. 利用merge() 完成左侧独有、右侧独有、全外独有

Page 11  |  Chapter 21 Pandas 合并和拼接 |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X N b M X a b left right M X N a

图 21. 利用pandas.merge() 完成合并，左侧独有

X N b M X a b left right M X N

图 22. 利用pandas.merge() 完成合并，右侧独有

a X N b M X a b left right M X N

图 23. 利用pandas.merge() 完成合并，全外独有

更多有关合并、比较的方法，请参考： https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

Page 1  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Reshaping and Pivoting Pandas DataFrames Pandas 重塑和透视主要介绍pivot()、stack()、unstack() 方法

善良一点，因为你遇到的每个人都在打一场更艰苦的战斗。

Be kind, for everyone you meet is fighting a harder battle.

—— 柏拉图 (Plato)  |  古希腊哲学家  |  424/423 ~ 348/347 BC

◄ pandas.DataFrame.pivot() 用于将数据透视成新的行和列形式的函数 ◄ pandas.DataFrame.stack() 将 DataFrame 中的列转换为多级索引的行形式的函数 ◄ pandas.DataFrame.unstack() 将 DataFrame 中的多级索引行转换为列形式的函数 ◄ pandas.melt() 将宽格式数据转换为长格式数据的函数，将多个列“融化”成一列 ◄ pandas.pivot_table() 根据指定的索引和列对数据进行透视，并使用聚合函数合并重复值的函数 ◄ pandas.wide_to_long() 将宽格式数据转换为长格式数据的函数，类似于 melt()，但可以处理多个标识符列和前缀

Page 2  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 22.1 数据帧的重塑和透视

在Pandas 中，数据帧的重塑和透视操作是指通过重新组织数据的方式，使数据呈现出不同的结构， 以满足特定的分析需求。

具体来说，数据帧重塑 (reshaping) 是指改变数据的行和列的排列方式。数据帧透视 (pivoting) 是指通过旋转数据的行和列，以重新排列数据，并根据指定的聚合函数来生成新的数据帧。这样做可以更好地展示数据的结构和统计特征。

长格式、宽格式是本章重要概念。如图 1 所示，长格式 (long format) 和宽格式 (wide format) 是两种不同的数据存储形式。如图 1 (a) 所示，长格式类似流水账，每一行代表一个观察值，比如某个学生某科目期中考试成绩。如图 1 (b) 所示，宽格式更像是“矩阵”，每一行代表一个特定观察条件，比如某个特定学生的学号。此外，宽格式数据的列用于表示不同的特征或维度，比如特定科目。显然，长格式、宽格式之间可以很容易相互转化。Pandas 提供很多方法用来完成数据帧的重塑和透视。

Subject Science Art Math Student ID NaN NaN NaN NaN Midterm Math Art Science Art Math Science Art Math Student ID Subject (a) long format (b) wide format

图 1. 比较长格式、宽格式

本章要介绍的重塑和透视操作如下。

pivot() 函数用于根据一个或多个列创建一个新的数据透视表。pivot_table() 与 pivot() 类似，它也可以执行透视操作，但是它允许对重复的索引值进行聚合，产生一个透视表。它对于处理有重复数据的情况更加适用。

stack() 函数用于将数据帧从宽格式转换为长格式。melt() 函数也可以用于将数据从宽格式转换为长格式，类似于stack()。

unstack() 函数是stack() 的逆操作，用于将数据从长格式转换为宽格式，也就是将数据从索引转换为列。

下面，我们分别介绍这几种方法。

Page 3  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 22.2 长格式转换为宽格式：pivot()

pivot() 可以理解为一种长格式转换为宽格式的特殊情况。pivot()需要指定三个参数：index，columns 和values，它们分别代表新DataFrame 的行索引、列索引和填充数据的值。

举个例子，图 2 左图表格为一个班级四名学生 (学号分别为1、2、3、4) 的各科 (Math、Art、Science)

期中、期末成绩，这个表格就是所谓的长格式，相当于“流水账”。

图 2 右图则是期中考试成绩“矩阵”，行标签 (index) 为学生学号 'ID'，列标签 (columns) 为三门科目 'Subject'，数据 (values) 为期中考试成绩 'Midterm'。

由于每名学生仅仅选修两门科目，因此大家在图 2 右图中会看到NaN。

进一步，图 2 右图数据帧横向求和，得到学生总成绩；而纵向求平均值，便是各科平均成绩。这是下一章要介绍的操作。

图 3 对应上述操作的代码。请大家自行提取同学各科期末考试成绩，科目为行标签，学号为列标签。

注意，使用pivot() 时，必须指定index 和columns，这两列的值将用于创建新的行和列。

此外，请大家思考如果，如果参数values = ['Midterm', 'Final']，结果会怎样？

df.pivot( index='Student ID', columns='Subject', values='Midterm')

Subject Science Art Math Student ID NaN NaN NaN NaN Final Midterm Math Art Science Art Math Science Art Math Student ID Subject

图 2. 利用pivot() 提取学生各科期中考试成绩，学号为行标签，科目为列标签

Page 4  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd data = { 'Student ID':['1','1','2','2','3','3','4','4'], 'Subject':   ['Math','Art','Science','Art', 'Math','Science', 'Art','Math'], 'Midterm':   [4, 5, 3, 5, 4, 5, 3, 5], 'Final':     [3, 4, 5, 3, 4, 4, 4, 5]} df = pd.DataFrame(data)

df.pivot(index='Student ID', columns='Subject', values='Midterm')

a

图 3. 利用pivot() 将长格式转换为宽格式，代码

我们可以用pivot_table() 完成和图 2 一样的操作，df.pivot_table(index='Student ID', columns = 'Subject', values='Midterm')。

和pivot() 不同的是，pivot_table() 可以不用指定columns。如图 4 所示。利用pivot_table()，我们可以把数据帧学号、科目转化为双层行索引。

df.pivot_table(index=['Subject', 'Student ID'], values=['Midterm','Final'])

Final Midterm Math Art Science Art Math Science Art Math Student ID Subject Midterm Final Subject Student ID Art Math Science

图 4. 利用pivot_table() 将学号、科目转化为双层行索引

Page 5  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd data = { 'Student ID':['1','1','2','2', '3','3','4','4'], 'Subject':   ['Math', 'Art', 'Science', 'Art', 'Math','Science', 'Art','Math'], 'Midterm':   [4, 5, 3, 5, 4, 5, 3, 5], 'Final':     [3, 4, 5, 3, 4, 4, 4, 5]} df = pd.DataFrame(data)

df.pivot_table(index=['Subject', 'Student ID'], values=['Midterm','Final'])

a

图 5. 利用pivot_table() 将长格式转换为宽格式，代码

## 22.3 宽格式转换为长格式：stack()

方法stack() 是一种将列逐级转换为层次化索引的操作。如果DataFrame 的列是层次化索引，那么 stack()会将最内层的列转换为最内层的索引。该函数返回一个Series 或DataFrame，具体取决于原始数据的维度。

df.stack().reset_index().rename(columns={0: 'Final'})

Final Art Math Science ID Subject Art Math Science Art Math Science Art Math Science Subject Science Art Math ID

图 6. 利用stack() 将宽格式转换为长格式

Page 6  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import numpy as np student_ids = [1, 2, 3, 4]

subjects = ['Art', 'Math', 'Science']

np.random.seed(0)

# 使用随机数生成成绩数据 scores = np.random.randint(3, 6, size=(len(student_ids),len(subjects)))

# 创建数据帧 df = pd.DataFrame(scores, index=student_ids, columns=subjects)

# 修改行列名称 df.columns.names = ['Subject']

df.index.names = ['Student ID']

# 将长格式转化为宽格式 df.stack().reset_index().rename(columns={0: 'Final'})

a

图 7. 利用stack() 将宽格式转换为长格式，代码

melt() 将原始数据中的多列合并为一列，并根据其他列的值对新列进行重复。可以理解为stack() 的一种泛化形式。melt() 需要指定id_vars 参数，表示保持不变的列，同时还可以选择value_vars 参数来指定哪些列需要被转换。请大家自行练习图 8 给出的示例。

import pandas as pd data = { 'Student ID': ['1', '2', '3', '4'], 'Art':        [4, 3, 5, 4], 'Math':       [3, 4, 5, 3], 'Science':    [5, 4, 3, 4]} df = pd.DataFrame(data)

df.columns.names = ['Subject']

melted_df = df.melt(id_vars='Student ID', var_name='Subject', value_vars=['Art','Math','Science'], value_name='Score')

a

图 8. 利用melt() 将宽格式转换为长格式，代码

多层列标签如果数据帧有多层列标签，可以有选择地选取特定级别列标签完成stack() 操作。

数据帧中A、B 代表两个班级，每个班级Class 有4 名同学 (学号1、2、3、4)，这些同学都选了3 门课程 (Art、Math、Science)。数据帧的数据部分为同学们的期末成绩。

请大家思考如果采用df.stack(level=["Subject"])，结果会怎样？

Page 7  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd data = { ('A', 'Art'):     [4, 3, 5, 4], ('A', 'Math'):    [3, 4, 5, 3], ('A', 'Science'): [5, 4, 3, 4], ('B', 'Art'):     [3, 4, 5, 4], ('B', 'Math'):    [4, 5, 3, 3], ('B', 'Science'): [5, 3, 4, 5]} # 创建多层行标签数据帧 df = pd.DataFrame(data, index=[1, 2, 3, 4])

# 添加行标签名称 df.columns.names = ['Class', 'Subject']

df.index.names = ['Student ID']

# 选择 'Class' 进行 stack() 操作 stacked_df = df.stack(level='Class')

# stacked_df = df.stack(level=0)

a

图 9. 利用stack() 将宽格式转换为长格式，选择特定列级别，代码

Subject Science Art Math Class A B A B A B A B ID Science Art Math Subject Science Art Math ID A B Class df.stack(level='Class')

图 10. 利用stack() 将宽格式转换为长格式，选择特定列级别

Page 8  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 22.4 长格式转换为宽格式：unstack()

在 Pandas 中，unstack() 是一个用于数据透视的方法，它用于将一个多级索引的 Series 或 DataFrame 中的其中选定级别转换为列。这在处理分层索引数据时非常有用。

如图 11 所示，左侧的数据帧df 有3 层行索引。第0 层为Class，第1 层为Student ID，第2 层为 Subject。第0 层Class 有两个值A、B，代表有两个班级。第1 层Student ID 有四个值1、2、3、4，代表每个班级学生的学号。第2 层有三个值Art、Math、Science，代表三个科目。

Art Math Science A Art Math Science Art Math Science Art Math Science Final Student ID Subject Class Art Math Science B Art Math Science Art Math Science Art Math Science df.unstack(0)

df.unstack('Class')

Art Math Science Art Math Science Art Math Science Art Math Science A Student ID Subject B df.unstack([1,2])

df.unstack(['Student ID','Subject'])

Art Math Science Art Math Science Art Math Science Art Math Science A Student ID Subject B pandas.DataFrame.transpose()

df.T

图 11. 利用unstack() 将长格式转换为宽格式

Page 9  |  Chapter 22 Pandas 重塑和透视  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com df.unstack(0) 或 df.unstack('Class') 将第0 层Class 行索引转换成两列——A、B。请大家尝试， df.unstack(1)、df.unstack('Student ID')、df.unstack(2)、df.unstack('Subject')，并比较结果。

df.unstack([1,2]) 或 df.unstack(['Student ID', 'Subject']) 将第1、2 层行索引转换成两层列标签。请大家尝试 df.unstack([2,1]) 或 df.unstack(['Subject','Student ID'])，以及尝试其他组合，比如 [0, 2]、[2, 0]、[0, 1]、[1, 0]，并比较结果。

import pandas as pd import numpy as np # 创建班级、学号和科目的所有可能组合 classes =  ['A', 'B']

student_ids = [1, 2, 3, 4]

subjects =    ['Art', 'Math', 'Science']

# 使用随机数生成成绩数据 length = len(classes)*len(student_ids)*len(subjects)

scores = np.random.randint(3, 6, size=(length))

# 创建多级索引 index = pd.MultiIndex.from_product( [classes, student_ids, subjects], names=['Class', 'Student ID', 'Subject'])

# 创建数据帧 df = pd.DataFrame(scores, index=index, columns=['Final'])

# df.unstack(0)

df.unstack('Class')

a

图 12. 利用unstack() 将长格式转换为宽格式，代码

Pandas 中重塑和透视操作灵活多样，本章介绍的方法仅仅是冰山一角而已。实践中，大家可以根据需求自行学习使用其他方法操作，建议大家继续阅读如下链接。

https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html

Page 1  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Basic Computations in Pandas DataFrame Pandas 常见运算特别介绍groupby()、apply() 方法

别弄乱了我的圆!

Don’t disturb my circles!

—— 阿基米德 (Archimedes)  |  数学家、发明家、物理学家  |  287 ~ 212 BC

◄ pandas.DataFrame.apply() 将一个自定义函数或者lambda 函数应用到数据帧的行或列上，实现数据的转换和处理 ◄ pandas.DataFrame.corr() 计算DataFrame 中列之间Pearson 相关系数 (样本)

◄ pandas.DataFrame.count() 计算DataFrame 每列的非缺失值的数量 ◄ pandas.DataFrame.cov() 计算DataFrame 中列之间的协方差矩阵 (样本)

◄ pandas.DataFrame.describe() 计算DataFrame 中数值列的基本描述统计信息，如平均值、标准差、分位数等 ◄ pandas.DataFrame.groupby() 在分组后的数据上执行聚合、转换和其他操作，从而对数据进行更深入的分析和处理 ◄ pandas.DataFrame.kurt() 计算DataFrame 中列的峰度 (四阶矩)

◄ pandas.DataFrame.kurtosis() 计算DataFrame 中列的峰度 (四阶矩)

◄ pandas.DataFrame.max() 计算DataFrame 中每列的最大值 ◄ pandas.DataFrame.mean() 计算DataFrame 中每列的平均值 ◄ pandas.DataFrame.median() 计算DataFrame 中每列的中位数 ◄ pandas.DataFrame.min() 计算DataFrame 中每列的最小值 ◄ pandas.DataFrame.mode() 计算DataFrame 中每列的众数 ◄ pandas.DataFrame.nunique() 计算DataFrame 中每列中的唯一值数量 ◄ pandas.DataFrame.quantile() 计算DataFrame 中每列的指定分位数值，如四分位数、特定百分位等 ◄ pandas.DataFrame.rank() 计算DataFrame 中每列元素的排序排名 ◄ pandas.DataFrame.skew() 计算DataFrame 中列的偏度 (三阶矩)

◄ pandas.DataFrame.std() 计算DataFrame 中列的标准差 (样本)

◄ pandas.DataFrame.sum() 计算DataFrame 中每列元素的总和 ◄ pandas.DataFrame.var() 计算DataFrame 中列的方差 (样本)

Page 2  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 23.1 四则运算

在Pandas 中，可以通过简单的语法实现各列之间的四则运算。以鸢尾花数据帧为例，图 1 中代码所示为鸢尾花数据帧花萼长度 (X1)、花萼宽度 (X2) 两列之间的运算。

a 对花萼长度去均值 (demean)，即X1 − E(X1)。其中，X_df_['X1'].mean() 计算列均值。也可以用 pandas.DataFrame.sub() 完成减法运算。

b 对花萼宽度去均值，即X2 − E(X2)。

c 计算花萼长度、宽度之和，即X1 + X2。也可以用pandas.DataFrame.add() 完成加法运算。

d 计算花萼长度、宽度之差，即X1 − X2。

e 计算花萼长度、宽度乘积，即X1X2。也可以用pandas.DataFrame.mul() 完成乘法运算。

f 计算花萼长度、宽度比例，即X1/X2。也可以用pandas.DataFrame.div() 完成除法运算。

import seaborn as sns import pandas as pd iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 X_df = iris_df.copy()

X_df.rename(columns = {'sepal_length':'X1', 'sepal_width':'X2'}, inplace = True)

X_df_ = X_df[['X1','X2', 'species']]

# 数据转换 X_df_['X1 - E(X1)'] = X_df_['X1'] - X_df_['X1'].mean()

X_df_['X2 - E(X2)'] = X_df_['X2'] - X_df_['X2'].mean()

X_df_['X1 + X2'] = X_df_['X1'] + X_df_['X2']

X_df_['X1 - X2'] = X_df_['X1'] - X_df_['X2']

X_df_['X1 * X2'] = X_df_['X1'] * X_df_['X2']

X_df_['X1 / X2'] = X_df_['X1'] / X_df_['X2']

X_df_.drop(['X1','X2'], axis=1, inplace=True)

# 可视化 sns.pairplot(X_df_, corner=True, hue="species")

a b e f

图 1. 鸢尾花数据帧花萼长度 (X1)、花萼宽度 (X2) 两列之间的运算

图 2 所示为经过上述转换后用seaborn.pairplot() 绘制的成对特征散点图。我们在鸢尾花书《统计至简》还会用到这幅图。

Page 3  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X1   E(X1)

X2   E(X2)

X1 + X2

## X1   X2

## X1X2

## X1/X2

X2   E(X2)

X1 + X2

## X1   X2

## X1X2

## X1/X2

Setosa Versicolor Virginica

图 2. 鸢尾花花萼长度、宽度特征完成转换后的成对特征散点图

## 23.2 统计运算

Pandas 中还给出大量用于统计运算 (也叫聚合操作) 的方法，表 1 总结常用的几种方法。

在数据分析中，聚合操作 (aggregation) 通常用于从大量数据中提取出有意义的摘要信息，以便更好地理解数据的特征和行为。

常见的聚合操作包括计算平均值、求和、计数、标准差、方差、相关性等。这些操作可以帮助我们了解数据的集中趋势、离散程度、相关性等特征，从而做出更准确的分析和决策。

图 3 所示为pandas.DataFrame.cov() 计算得到的鸢尾花前四列协方差矩阵热图。当然，在计算协方差时，我们也可以考虑到数据标签。图 5 所示为三个不同标签数据各自的协方差矩阵、相关性系数热图。

此外，pandas.DataFrame.agg() 方法用于对 DataFrame 中的数据进行自定义聚合操作。该方法按照指定的函数对数据进行聚合，可以是内置的统计函数，也可以是自定义的函数。

Page 4  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 比如，iris_df.iloc[:,0:4].agg(['sum', 'min', 'max', 'std', 'var', 'mean']) 对鸢尾花数据帧前四列进行各种统计计算。

表 1. Pandas 中常用统计运算方法函数名称描述 pandas.DataFrame.corr()

计算DataFrame 中列之间Pearson 相关系数 (样本)

pandas.DataFrame.count()

计算DataFrame 每列的非缺失值的数量 pandas.DataFrame.cov()

计算DataFrame 中列之间的协方差矩阵 (样本)

pandas.DataFrame.describe()

计算DataFrame 中数值列的基本描述统计信息，如平均值、标准差、分位数等 pandas.DataFrame.kurt()

计算DataFrame 中列的峰度 (四阶矩)

pandas.DataFrame.kurtosis()

计算DataFrame 中列的峰度 (四阶矩)

pandas.DataFrame.max()

计算DataFrame 中每列的最大值 pandas.DataFrame.mean()

计算DataFrame 中每列的平均值 pandas.DataFrame.median()

计算DataFrame 中每列的中位数 pandas.DataFrame.min()

计算DataFrame 中每列的最小值 pandas.DataFrame.mode()

计算DataFrame 中每列的众数 pandas.DataFrame.quantile()

计算DataFrame 中每列的指定分位数值，如四分位数、特定百分位等 pandas.DataFrame.rank()

计算DataFrame 中每列元素的排序排名 pandas.DataFrame.skew()

计算DataFrame 中列的偏度 (三阶矩)

pandas.DataFrame.sum()

计算DataFrame 中每列元素的总和 pandas.DataFrame.std()

计算DataFrame 中列的标准差 (样本)

pandas.DataFrame.var()

计算DataFrame 中列的方差 (样本)

pandas.DataFrame.nunique()

计算DataFrame 中每列中的唯一值数量

Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Covariance matrix 0.69 0.042 1.3 0.52 3.0 0.042 0.19 0.33 0.12 1.3 0.33 3.1 1.3 1.3 0.58 0.12 0.52 2.5 2.0 1.5 1.0 0.5 0.0 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Correlation matrix 0.12 0.87 0.82 0.12 0.43 0.43 0.37 0.82 0.37 0.87 0.96 0.96 1.0 0.8 0.6 0.4 0.2 0.0 0.2 0.4

图 3. 鸢尾花数据协方差矩阵、相关性系数矩阵热图

Page 5  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 22.3 分组聚合：groupby()

在 Pandas 中，groupby() 是一种非常有用的数据分组聚合计算方法。groupby() 按照某个或多个列的值对数据进行分组，然后对每个分组进行聚合操作。图 4 代码介绍如何使用 groupby() 方法，并结合 mean()、std()、var()、cov() 和 corr() 对分组后的数据进行聚合操作。

图 5、图 6 所示为考虑鸢尾花分类的协方差矩阵、相关性系数矩阵热图。其中， groupby(['species']).cov() 得到的数据帧为两层行索引。根据前文介绍的多层行索引数据帧切片方法， groupby_cov.loc['setosa'] 提取鸢尾花类别为'setosa'的协方差矩阵。也可以用groupby_cov.xs('setosa') 提取相同数据。此外，我们也可以用iris_df.loc[iris_df['species'] == 'setosa'].cov() 专门计算鸢尾花类别为 'setosa'的协方差矩阵。

import seaborn as sns import pandas as pd iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 分组计算统计量 groupby_mean = iris_df.groupby(['species']).mean()

groupby_std  = iris_df.groupby(['species']).std()

groupby_var  = iris_df.groupby(['species']).var()

groupby_cov  = iris_df.groupby(['species']).cov()

groupby_corr = iris_df.groupby(['species']).corr()

a b e

图 4. 鸢尾花数据帧groupby(['species']) 计算统计量

Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 'species' == 'setosa' 'species' == 'versicolor' 'species' ==  'virginica' 0.12 0.1 0.1 0.14 0.016 0.016 0.01 0.01 0.012 0.012 0.009 0.009 0.03 0.006 0.006 0.011 0.27 0.085

## 0.085 0.098

0.18 0.18 0.056 0.056 0.083 0.083 0.041 0.041 0.22 0.073 0.073 0.039 0.4 0.094 0.094 0.1 0.3 0.3 0.049 0.049 0.071 0.071 0.048 0.048 0.3 0.049 0.049 0.075

图 5. 协方差矩阵热图，考虑分类

Page 6  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 0.53 0.53 0.75 0.75 0.55 0.55 0.56 0.56 0.66 0.66 0.79 0.79 0.74 0.74 0.27 0.27 0.28 0.28 0.18 0.18 0.23 0.23 0.33 0.33 0.46 0.46 0.86 0.86 0.28 0.28 0.4 0.4 0.54 0.54 0.32 0.32 'species' == 'setosa' 'species' == 'versicolor' 'species' ==  'virginica'

图 6. 相关性系数矩阵热图，考虑分类标签

还是用上一章的例子，给出如何用groupby() 汇总学生成绩。

import pandas as pd import numpy as np # 创建班级、学号和科目的所有可能组合 classes = ['A', 'B']

stu_ids = [1, 2, 3, 4]

subjects = ['Art', 'Math', 'Science']

# 使用随机数生成成绩数据 np.random.seed(0)

length = len(classes ) * len(stu_ids) * len(subjects)

data = np.random.randint(3, 6, size=(length))

# 创建多行标签数据帧 index = pd.MultiIndex.from_product( [classes, stu_ids, subjects], names=['Class', 'Student ID', 'Subject'])

df = pd.DataFrame(data, index=index, columns=['Score'])

# 1) 每个班级各个科目平均成绩 class_subject_avg = df.groupby( ['Class', 'Subject'])['Score'].mean()

# 2) 每个班级各个学生的平均成绩 class_student_avg = df.groupby( ['Class', 'Student ID'])['Score'].mean()

# 3) 两个班级放在一起各个科目平均成绩 both_class_avg = df.groupby( 'Subject')['Score'].mean()

# 4) 两个班级每个同学总成绩，并排名 student_total_score = df.groupby( ['Class','Student ID'])['Score'].sum().sort_values( ascending=False)

a b

图 7. 利用groupby() 汇总学生成绩，代码

Page 7  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Art Math Science A Art Math Science Art Math Science Art Math Science Final Student ID Subject Class Art Math Science B Art Math Science Art Math Science Art Math Science df.groupby(['Class', 'Subject'])['Score'].mean()

Art Math Science A B Art Math Science 3.25 4.00 Score Class Subject 4.00 4.00 3.75 3.75 Art Math Science 3.50 4.00 Score Subject 3.88 df.groupby('Subject')['Score'].mean()

A B 3.33 4.33 Score Class Student ID 3.33 3.67 3.67 4.67 3.67 3.67 df.groupby(['Class', 'Student ID'])['Score'].mean()

df.groupby(['Class', 'Student ID'])['Score'].sum().sort_values(ascending=False)

A B 3.33 4.33 Score Class Student ID 3.33 3.67 3.67 4.67 3.67 3.67 B B A

图 8. 利用groupby() 汇总学生成绩

Page 8  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 22.4 自定义操作：apply()

在 Pandas 中，可以使用 apply() 方法对 DataFrame 的行或列进行自定义函数的运算。apply() 方法是 Pandas 中最重要和最有用的方法之一，它可以实现 DataFrame 数据的处理和转换，也可以实现计算和数据清洗等功能。

如图 9 代码所示，a 定义函数map_fnc()，这个函数的目的是将花萼长度sepal_length 转化为等级。

转化的规则为，如果sepal_length < 5，等级为D；如果5 <= sepal_length < 6，等级为C；如果6 <= sepal_length < 7，等级为B；其余情况 (sepal_length > 6)，等级为A。b 利用apply() 将自定义函数用在数据帧iris_df['sepal_length'] 上。

import seaborn as sns import pandas as pd iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 定义函数将花萼长度映射为等级 def map_fnc(sepal_length): if sepal_length < 5: return 'D' elif 5 <= sepal_length < 6: return 'C' elif 6 <= sepal_length < 7: return 'B' else: return 'A' # 使用 apply 函数将 sepal_length 映射为等级并添加新列 iris_df['ctg'] = iris_df['sepal_length'].apply(map_fnc)

b a

图 9. 鸢尾花数据帧使用apply() 自定义函数，对于特定一列

apply() 方法可以接受一个函数作为参数，这个函数将会被应用到 DataFrame 的每一行或每一列上。

这个函数可以是Pandas 中已经定义好的函数，可以是自定义函数，也可以是匿名lambda 函数。

比如，图 10 代码使用apply() 和lambda 函数计算鸢尾花数据集中每个类别中最小的花瓣宽度。

a 等价于iris_df.groupby('species')['sepal_length'].min()。

图 11 中apply() 的输入先是匿名lambda 函数，对象定义为row，代表数据帧的每一行。而lambda 函数调用自定函数map_petal_width()，这个函数有两个输入。

Page 9  |  Chapter 23 Pandas 常见运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import seaborn as sns import pandas as pd iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 使用apply() 和lambda函数计算每个类别中最小的花瓣宽度 iris_df.groupby('species')['sepal_length'].apply( lambda x: x.min())

# iris_df.groupby('species')['sepal_length'].min()

a

图 10. 鸢尾花数据帧使用apply() 匿名lambda 函数，对于特定一列

import seaborn as sns import pandas as pd iris_df = sns.load_dataset("iris")

# 从Seaborn中导入鸢尾花数据帧 # 计算鸢尾花各类花瓣平均宽度 mean_X2_by_species = iris_df.groupby( 'species')['petal_width'].mean()

# 定义映射函数 def map_petal_width(petal_width, species): if petal_width > mean_X2_by_species[species]: return "YES"

else: return "NO"

# 使用 map 方法将花瓣宽度映射为是否超过平均值 iris_df['greater_than_mean'] = iris_df.apply(lambda row: map_petal_width(row['petal_width'], row['species']), axis=1)

a b

图 11. 鸢尾花数据帧使用apply() 匿名lambda 函数，对于特定两列

此外，在 Pandas 中，可以使用 map() 方法对 Series 或DataFrame 特定列进行自定义函数的运算。这个映射关系可以由用户自己定义，也可以使用 Pandas 中已经定义好的函数。

除了 apply() 和 map() 方法之外，Pandas DataFrame 还提供applymap()、transform() 等方法，请大家自行学习使用。需要大家注意，applymap() 用于对 DataFrame 中的每个元素应用同一个函数，返回一个新的 DataFrame。

有关数据帧分组聚合操作，请大家继续阅读： https://pandas.pydata.org/docs/user_guide/groupby.html

Page 1  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Timeseries Data in Pandas Pandas 时间序列数据时间戳作为索引值，实现对时间序列数据的标记和运算

很难做出预测，尤其是对未来的预测。

It is difficult to make predictions, especially about the future.

—— 尼尔斯·玻尔 (Niels Bohr)  |  丹麦物理学家  |  1885 ~ 1962

◄ df.bfill() 向后填充缺失值 ◄ df.ffill() 向前填充缺失值 ◄ df.interpolate() 插值法填充缺失值 ◄ df.rolling().corr() 计算数据帧df 的移动相关性 ◄ df.rolling().mean() 计算数据帧df 滚动均值 ◄ df.rolling().std() 计算数据帧df MA 平均值 ◄ joypy.joyplot() 绘制山脊图 ◄ numpy.random.uniform() 生成满足均匀分布的随机数 ◄ plotly.express.bar() 绘制可交互条形图 ◄ plotly.express.histogram() 绘制可交互直方图 ◄ plotly.express.imshow() 绘制可交互热图 ◄ plotly.express.line() 绘制可交互二维线图 ◄ plotly.express.scatter() 绘制可交互散点图 ◄ seaborn.heatmap() 绘制热图 ◄ statsmodels.api.tsa.seasonal_decompose() 季节性调整 ◄ statsmodels.regression.rolling.RollingOLS() 计算移动OLS 线性回归系数

Page 2  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 24.1 什么是时间序列?

时间序列 (timeseries) 是指按照时间顺序排列的一系列数据点或观测值，通常是等时间间隔下的测量值，如每天、每小时、每分钟等。时间序列数据通常用于研究时间相关的现象和趋势，例如股票价格、 气象数据、经济指标等。图 1 (a) 所示为标普500 (S&P 500) 数据。

## S&P

(a)

(b)

图 1. 标普500 数据，含有缺失值

时间序列分析是一种重要的数据分析方法，它可以用于预测未来的趋势和变化，评估现有趋势的稳定性和可靠性，并发现异常点和异常趋势。时间序列分析通常包括以下几个步骤： ► 数据预处理：对数据进行清洗、去噪、填补缺失值等操作，以提高数据质量和可靠性。

► 时间序列的可视化：对数据进行绘图，以了解数据的分布、趋势和周期性。

► 时间序列的统计分析：对数据进行时间序列分解、平稳性检验、自相关性检验等统计分析，以评估数据的稳定性和相关性。

► 时间序列的建模和预测：根据统计分析的结果，建立合适的时间序列模型，进行未来趋势的预测和评估。

比如，在图 1 (a) 中被局部放大的曲线上，大家已经看到了缺失值。图 1 (b) 用热图可视化缺失值的位置。在本章配套的代码中，大家会看到经过计算缺失值的占比约为3.5%。

本章仅仅采用“图解”介绍部分时间序列分析，《数据有道》一册将专门介绍时间序列相关话题。

Pandas 中的时间序列功能在Python 中，Pandas 库提供了强大的时间序列处理和分析功能，使得时间序列的处理和分析变得更加简单和高效。在 Pandas 中，时间序列分析的主要方法包括： ► 创建时间序列：可以通过 pandas.date_range() 方法创建一个时间范围，或者将字符串转换为时间序列对象。

► 时间序列索引：可以使用时间序列作为 DataFrame 的索引，从而方便地进行时间序列分析。

Page 3  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ► 时间序列的切片和索引：可以使用时间序列的标签或位置进行切片和索引。

► 时间序列的重采样：可以将时间序列转换为不同的时间间隔，例如将日频率的数据转换为月频率的数据。

► 移动窗口函数：可以对时间序列数据进行滑动窗口操作，计算滑动窗口内的统计指标，例如均值、 方差等。

► 时间序列的分组操作：可以将时间序列数据按照时间维度进行分组，从而进行聚合操作，例如计算每月的平均值、最大值等。

► 时间序列的聚合操作：可以对时间序列数据进行聚合操作，例如计算每周、每月、每季度的总和、 平均值等。

► 时间序列的可视化：可以使用 Pandas、Matplotlib、Seaborn、Plotly 等库对时间序列数据进行可视化，例如绘制线形图、散点图、直方图等。

## 24.2 缺失值

缺失值 (missing value) 指的是数据集中的某些值缺失或未被记录的情况。它们可能是由于测量设备故障、记录错误、样本丢失或数据清洗不完整等原因导致的。缺失值可能在数据分析和建模中产生严重的影响，因为它们会导致数据样本的大小不一致，使得数据的统计分布和关系不准确或无法得出。另外，许多机器学习算法无法处理缺失值，必须对其进行处理或者删除。

图 2. 缺失值在数据处理中，通常需要对缺失值进行识别、处理或删除。一些处理缺失值的方法包括： ► 删除带有缺失值的样本或变量。

► 使用常量填充缺失值，例如用零、平均值、中位数等常量填充。

► 使用回归模型、插值方法等技术，对缺失值进行预测和填充。

► 对于分类变量，可以创建一个新的类别来表示缺失值。

在选择处理方法时，需要根据具体情况和数据分析的目的来决定。

图 1 中的缺失值则对应非营业日，比如周六日、节假日等。将这些缺失值删除之后，我们便得到图 3 所示的趋势。为了醒目地观察每年趋势，我们绘制了图 4。

鸢尾花书《数据有道》将介绍处理缺失值的各种方法。

Page 4  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a)

(b)

## S&P

图 3. 标普500 数据，删除缺失值

## S&P

图 4. 标普500 数据，按年观察趋势

什么是离群值？

在统计学和数据分析中，离群值 (outlier) 指的是在数据集中与其他数据值显著不同的异常值。它们可能是由于测量误差、实验异常、录入错误、样本损坏或数据处理错误等因素导致的。离群值具有比其他数据点更大或更小的数值，与其他数据点之间的差异通常非常显著。

离群值会对数据分析结果产生影响，比如对平均值、方差、相关性等统计指标的计算都会受到其影响。因此，在数据分析和建模中，需要对离群值进行识别、处理或删除。常见的方法包括使用箱线图或3σ准则等方法来识别离群值，并根据具体情况进行处理或删除。如果离群值确实是数据中真实存在的异常值，则可能需要对其进行单独分析或建立针对其的模型。

Page 5  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 本章不会介绍如何处理离群值，相关内容请参考《数据有道》。

## 24.3 移动平均

时间序列的移动平均 (moving average, MA) 是一种常用的平滑技术，用于去除序列中的噪声和波动，以便更好地观察和分析序列的长期趋势。

移动平均通过计算序列中一段固定长度（通常称为窗口）内数据点的平均值来平滑序列。窗口的大小决定了平滑的程度，较大的窗口将平滑更多的波动，但可能会导致较长的滞后。

具体步骤如下： ► 1) 选择窗口的大小，例如10 个数据点。

► 2) 从序列的起始位置开始，计算窗口内数据点的平均值。

► 3) 将该平均值作为移动平均的第一个数据点，记录下来。

► 4) 移动窗口向后滑动一个数据点的位置。

► 5) 重复步骤2 至4，计算新窗口内的平均值，并记录下来。

► 6) 继续滑动窗口直到到达序列的末尾，得到一系列移动平均值。

移动平均的计算可以使用简单移动平均 (Simple Moving Average, SMA) 或加权移动平均 (Weighted Moving Average, WMA) 来进行。简单移动平均对窗口内的每个数据点赋予相等的权重，而加权移动平均则可以根据需求赋予不同的权重，以更强调某些数据点的重要性。

Historical data Lookback window Rolling

图 5. 移动窗口

通过计算移动平均，时间序列中的短期波动可以平滑，从而更容易观察到长期趋势和周期性变化。

移动平均在金融分析、经济预测和数据分析等领域得到广泛应用。

Page 6  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## S&P

Jul 2021 Jan 2022 Jul 2022

## SP500

## MA20

## MA10

MA5

图 6. 标普500 数据，移动平均

## 24.4 收益率

为了量化股票市场的每日涨跌，我们需要计算股票的日收益率。计算当日收益率时需要知道两个关键数据点：股票的当日收盘价、前一日收盘价。

日收益率的计算公式为：日收益率 = (当日收盘价 − 前一日收盘价) / 前一日收盘价。将这个公式应用于具体的股票数据，就可以计算出每个交易日的日收益率。图 7 所示为标普500 的日收益率。

Daily return (%)

图 7. 标普500 数据日收益率

为了更方便观察每年涨跌情况，我们绘制了图 8。

Page 7  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Daily return (%)

图 8. 标普500 数据日收益率，按年观察趋势

## 24.5 统计分析

市场涨跌越越剧烈，曲线波动越剧烈。图 8 这些曲线类似随机行走，为了发现规律，我们需要借助统计工具。

年度分布图 9 所示为下载所有数据计算得到日收益率绘制的分布图。大家可以从分布中计算得到均值和标准差。这个任务交给大家自行完成。图 10 所示为年度日收益率分布变化情况。

为了更好的量化股票的波动情况，我们需要一个指标——波动率 (volatility)。波动率是衡量其价格变动幅度的指标，常用的量化方法为历史波动率 (historical volatility)。历史波动率本质上就是一定回望窗口内收益率样本数据的标准差。

图 11 所示为利用水平柱状图可视化日收益率的年度均值、波动率 (标准差)。

此外，我们还可以使用山脊图 (ridgeline plot) 可视化每年收益率的分布情况，具体如图 12 所示。

Joypy 是一个Python 库，用于创建山脊图。山脊图是一种可视化工具，用于展示多个连续变量在一个维度上的分布，并且能够显示不同组之间的比较。

山脊图的特点是将多个曲线图，通常是核密度估计曲线，沿着一个共享的垂直轴线堆叠显示，形成一座山脉状的图形。每个曲线代表一个组或类别，可以通过颜色或其他视觉属性进行区分。要使用Joypy 绘制山脊图，需要首先安装Joypy 库，并导入joyplot 模块。

Page 8  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Daily return (%)

0.6 0.4 0.2 0.0 Probability density

图 9. 所有下载历史数据日收益率分布

Daily return (%)

图 10. 日收益率分布，按年

(a)

(b)

Average of daily return 0.05 0.00 0.05 0.10 0.0 0.5 1.0 1.5 2.0 Volatility of daily return

图 11. 水平柱状图可视化收益率均值、标准差 (波动率)，按年

Page 9  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 12. 山脊图，按年

季度分布当然，我们也可以按季度分析收益率。图 13 所示为每个季度收益率的均值、标准差的柱状图。图 14 所示为每个季度收益率的山脊图。这幅图我们把纵轴的时间隐去。

Average of daily return 0.0 0.2 0.2 0.0 1.0 2.0 3.0 Volatility of daily return (a)

(b)

图 13. 水平柱状图可视化收益率均值、标准差 (波动率)，按季度

Page 10  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 14. 山脊图，按季度

移动波动率

Page 11  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 准确来说，历史波动率是根据过去一段时间内的股票价格数据计算得出的波动率。

可以选择一个时间窗口，例如20 营业日 (一个月)、60 营业日 (一个季度)、125 或126 营业日 (半年)、250 或252 营业日 (一年)，计算每个交易日的收益率，然后求得其标准差，最终得到历史波动率。

当这个回望窗口移动时，我们便得到移动波动率的时间序列数据。图 15 所示的移动波动率的回望窗口长度为250 天营业日。请大家自己修改回望窗口长度 (营业日数量)，比较移动波动率曲线。

《数据有道》还会专门介绍指数加权移动平均EWMA 方法计算的均值和波动率。

2.2 Volatility 2.0 1.8 1.6 1.4 1.2 1.0 0.8 0.6 0.4

图 15. 移动波动率

## 24.6 相关性

几个不同时间序列之间肯定也会存在相关性。图 16 所示为标普500 日收益率和三个汇率收益率之间的相关性系数矩阵热图。

JPY to USD CAD to USD CNY to USD

## S&P

1.00 1.00 1.00 1.00 0.16 0.18 0.19 0.30 0.16 0.18 0.19 0.25 0.16 0.16 0.25 0.30

图 16. 相关性系数矩阵相关性并不是一成不变的，也是随时间不断变化。如图 17 所示，当我们指定具体的移动窗口长度， 也可以计算移动相关性。

Page 12  |  Chapter 24 Pandas 时间序列数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 0.6 0.4 0.2 0.0 0.2 0.4 Correlation JPY to USD__CAD to USD JPY to USD__CNY to USD JPY to USD__SP500 CAD to USD__SP500 CNY to USD__SP500 CAD to USD__CNY to USD

图 17. 移动相关性

对时间序列历史数据完成分析后自然少不了预测这个环节。本书不会展开讲解，请大家参考《数据有道》。

请大家完成下面这道题目。

Q1. 请大家把本章配套代码中历史数据截止时间修改为最近日期，重新下载数据逐步完成本章前文时间序列分析。

* 本章不提供答案。

有关Pandas 中时间序列更多用法，请大家参考： https://pandas.pydata.org/docs/user_guide/timeseries.html 此外，Statsmodels 有大量时间序列分析工具： https://www.statsmodels.org/stable/user-guide.html#time-series-analysis

Page 1  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Symbolic Computation in SymPy SymPy 符号运算 SymPy 是一个 Python 的符号数学计算库

等式仅仅是数学中无聊至极的那部分；我努力从几何角度观察万物。

Equations are just the boring part of mathematics. I attempt to see things in terms of geometry.

—— 斯蒂芬·霍金 (Stephen Hawking)  |  英国理论物理学家和宇宙学家  |  1942 ~ 2018

◄ sympy.abc import x 定义符号变量x ◄ sympy.abc() 引入符号变量 ◄ sympy.collect() 合并同类项 ◄ sympy.cos() 符号运算中余弦 ◄ sympy.diff() 求解符号导数和偏导解析式 ◄ sympy.Eq() 定义符号等式 ◄ sympy.evalf() 将符号解析式中未知量替换为具体数值 ◄ sympy.exp() 符号自然指数 ◄ sympy.expand() 展开代数式 ◄ sympy.factor() 对代数式进行因式分解 ◄ sympy.integrate() 符号积分 ◄ sympy.is_decreasing() 判断符号函数的单调性 ◄ sympy.lambdify() 将符号表达式转化为函数 ◄ sympy.limit() 求解极限 ◄ sympy.Matrix() 构造符号函数矩阵 ◄ sympy.plot_implicit()绘制隐函数方程 ◄ sympy.plot3d() 绘制函数的三维曲面 ◄ sympy.series() 求解泰勒展开级数符号式 ◄ sympy.simplify() 简化代数式 ◄ sympy.sin() 符号运算中正弦 ◄ sympy.solve() 求解符号方程组 ◄ sympy.solve_linear_system() 求解含有符号变量的线型方程组 ◄ sympy.symbols() 创建符号变量 ◄ sympy.sympify() 化简符号函数表达式 ◄ sympy.utilities.lambdify.lambdify() 将符号代数式转化为函数

Page 2  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 25.1 什么是SymPy?

SymPy 是一个基于Python 的符号数学库，它可以执行代数运算、解方程、微积分、离散数学以及其他数学操作。与NumPy、Pandas 等科学计算库不同，SymPy 主要关注的是符号计算而不是数值计算。具体来说，SymPy 可以处理未知变量和数学符号，而不仅仅是数值，这在一些数学研究和工程应用中非常有用。

本章主要介绍SymPy 中代数、线性代数运算。此外，SymPy 还可以进行微积分运算，比如极限、 导数、偏导数、泰勒展开、积分等。这部分内容需要一定的数学分析知识，我们将会在鸢尾花书《数学要素》一册展开讲解。

## 25.2 代数

因式分解图 1 所示为利用SymPy 完成因式分解。

a 从sympy 导入symbols 和factor，其中symbols 用来定义符号变量，factor 用来完成因式分解。b 这两句的作用是将 SymPy 库中的数学符号以美观的形式打印出来。

c 定义了x 和y 两个符号变量。symbols 还可以定义带下角标的变量，比如x1, x2 = symbols('x1 x2')。

也可以用from sympy.abc import x, y 的形式定义符号变量。

此外，用sympy.symbols() 定义变量时还可以提出符号的假设条件。比如，k = sympy.symbols('k', integer=True) 这一句定义符号变量k，并假定k 为整数。z = sympy.symbols('z', real=True) 定义了符号变量 z，并假定z 为实数。

d 定义了 y − 。e 对 y − 进行因式分解，结果为( )( )

y y − + 。反过来，可以用 sympy.expand() 展开( )( )

y y − + ，结果为 y − 。

from sympy import symbols, factor # 从sympy中导入symbols, factor from sympy import init_printing init_printing("mathjax")

x, y = symbols('x y')

# 用sympy.symbols (简做symbols) 定义x和y两个符号变量 f = x**2 - y**2 f_factored= factor(f)

a b e

图 1. 因式分解

Page 3  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 替换图 2 中a 定义字符串，b 将字符串转化为符号表达式 + + + 。

c 用符号y 替代符号x，符号表达式变为 y y y + + + 。

d 用0 替代x，结果为1。

from sympy import symbols, sympify x, y = symbols('x y')

str_expression = 'x**3 + x**2 + x + 1' # 将字符串转化为符号表达式 str_2_sym = sympify(str_expression)

# 将符号x替换为y str_2_sym.subs(x, y)

# 将符号x替换为0 str_2_sym.subs(x, 0)

a b

图 2. 用sympy.sympify 将字符串转化为符号表达式

特殊符号数值 SymPy 还可以定义定义特殊符号数值，表 1 给出几个例子。比如，sympy.sympify() 将2 转化为符号数值2，然后进一步判断其是否为整数，是否为实数。再比如，from sympy import Rational; Rational(1, 2)

这两句的结果为1 2 。想要知道表格中结果的浮点数形式，可以用.evalf()，比如exp(2).evalf() 的结果为 7.38905609893065。

表 1. 用sympy 定义特殊符号数值代码结果 from sympy import sympify sympify(2).is_integer sympify(2).is_real True True from sympy import Rational Rational(1, 2)

from sympy import sqrt 1 / (sqrt(2) + 1)

+

from sympy import pi expr = pi ** 2 π from sympy import exp exp(2)

2e from sympy import factorial factorial(5)

5!

from sympy import binomial binomial(5, 4)

C =

from sympy import gamma gamma(5)

( )

( )

5 1 !

4 3 2 1  = − = =

Page 4  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 区间表 2 总结如何用sympy.Interval() 定义各种区间，默认区间左闭、右闭。oo (两个小写英文字母o) 代表正无穷。注意，大家自己在同一个Jupyter Notebook 练习时，from sympy import Interval, oo 只需要导入一次，不需要重复导入。

此外，用sympy.Interval() 定义的区间还可以进行集合运算，比如Interval(0, 2) - Interval(0, 1) 结果为 (1, 2]。再比如，Interval(0, 1) + Interval(1, 2) 的结果为 [0, 2]。

利用.has() 还可以判断区间是否包含具体元素，比如先定义intvl = Interval.Lopen(0, 1)，得到区间 (0, 1]。然后利用intvl.has(0) 或intvl.contains(0) 判断左开右闭区间是否包括元素0，结果为False。

表 2. 用sympy.Interval()定义区间代码结果 from sympy import Interval, oo Interval(0, 1, left_open=False, right_open=False)

[0, 1]

from sympy import Interval, oo Interval(0, 1, left_open=True, right_open=True)

(0, 0)

from sympy import Interval, oo Interval(0, 1, left_open=False, right_open=True)

# Interval.Ropen(0, 1)

[0, 1)

from sympy import Interval, oo Interval(0, 1, left_open=True, right_open=False)

# Interval.Lopen(0, 1)

(0, 1]

from sympy import Interval, oo Interval(0, oo, left_open=False, right_open=True)

[0, ∞)

from sympy import Interval, oo Interval(-oo, 0, left_open=True, right_open=True)

(−∞, 0)

from sympy import Interval, S Interval(0, 1).complement(S.Reals)

(−∞, 0) ∪ (1, ∞)

求解等式图 3 代码介绍如何用sympy.solve() 求解等式。a 定义等式 x = ，b 求解等式结果为  1,1 − 。

c 定义等式 ax bx + + = 。d 求解等式结果为 , b b ac b b ac a a       −  − −+  −− 。

from sympy import symbols,solve,Eq x = symbols('x')

# 定义等式 x**2 = 1 equation_1 = Eq(x**2, 1)

solve(equation_1, x)

a,b,c = symbols("a,b,c", real=True)

# 定义等式 a*x**2+b*x = -c equation_2 = Eq(a*x**2+b*x+c, 0)

solve(equation_2, x)

a b

图 3. 用sympy.solve() 求解等式

Page 5  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 函数图 4 代码用sympy.lambdify() 将符号函数 ( )

exp − − 转化为Python 函数，从而可以进行数值运算。图 5 所示为代码绘制的二元高斯函数曲面。

from sympy import symbols, exp, lambdify import numpy as np import matplotlib.pyplot as plt x1, x2 = symbols('x1 x2')

# 定义符号变量 f_gaussian_x1x2 = exp(-x1**2 - x2**2)

# 将符号表达式转换为Python函数 f_gaussian_x1x2_fcn = lambdify([x1,x2],f_gaussian_x1x2)

xx1,xx2 = np.meshgrid(np.linspace(-3,3,201), np.linspace(-3,3,201))

ff = f_gaussian_x1x2_fcn(xx1,xx2)

# 可视化 fig = plt.figure()

ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(xx1,xx2,ff, rstride=10, cstride=10)

ax.set_proj_type('ortho')

ax.view_init(azim=-120, elev=30)

ax.grid(False)

ax.set_xlabel('x1')

ax.set_ylabel('x2')

ax.set_zlabel('f(x1,x2)')

ax.set_xlim(-3,3)

ax.set_ylim(-3,3)

ax.set_zlim(0,1)

ax.set_box_aspect(aspect = (1,1,1))

fig.savefig('二元高斯函数.svg', format='svg')

a b

图 4. 用sympy.lambdify() 将符号表达式转化为Python 函数

Page 6  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 0.0 0.2 0.4 0.6 0.8 1.0 f(x1,x2)

x1 x2

图 5. 二元高斯函数曲面

## 25.3 线性代数

NumPy 是Python 科学计算中非常重要的一个库，它提供了快速、高效的多维数组对象及其操作方法，是众多其他科学计算库的基础。

矩阵图 6 中代码用sympy.Matrix() 定义矩阵、列向量。

a 从sympy 导入Matrix 函数。

b 定义2 行、3 列矩阵A。函数sympy.shape() 可以用来获取矩阵形状。举个例子，先用from sympy import shape 导入shape，然后shape(A) 返回元组 (2,3) 即矩阵形状。A.T 可以完成矩阵转置。对矩阵A 的索引和切片方法和NumPy 数组一致。比如，A[0,0] 提取矩阵第1 行、第1 列元素。A[-1,-1] 提取矩阵最后一行、最后一列元素。A[0,:] 提取矩阵第一行，A.row(0) 也可以用来提取矩阵第1 行。A[:,0] 提取矩阵第一列，A.col(0) 也可以提取矩阵第一列。

此外，A.row_del(0) 可以用来删除第1 行元素。A.row_insert() 可以用来在特定位置插入行向量。类似地，A.col_del(0) 可以用来删除第1 列元素。A.col_insert() 可以用来在特定位置插入列向量。

c 定义列向量a。

from sympy import Matrix # 定义矩阵 A = Matrix([[1, 2, 3], [3, 2, 1]])

# 定义列向量 a = Matrix([1, 2, 3])

a b

图 6. 用sympy.matrix() 定义矩阵

Page 7  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 7 定义的矩阵A 为 a b   =     A 。

from sympy import Matrix, symbols A = Matrix(2, 2, symbols('a:d'))

b

图 7. 用sympy.matrix() 定义全符号矩阵

表 3 给出了几种产生特殊矩阵的方法。此外，A.is_symmetric() 判断矩阵A 是否为对称阵， A.is_diagonal() 判断矩阵A 是否为对角阵，A.is_lower 判断矩阵A 是否为下三角，A.is_upper 判断矩阵A 是否为上三角纠正，A.is_square 判断矩阵A 是否为方阵，A.is_zero_matrix 判断矩阵A 是否为全0 矩阵， A.is_diagonalizable() 判断矩阵A 是否可以对角化。A.is_positive_definite 判断矩阵A 是否为正定。

表 3. 用sympy 函数产生特殊矩阵矩阵类型代码结果单位矩阵 from sympy import eye A = eye(3)

         

全0 矩阵 from sympy import zeros A = zeros(3, 3)

         

全1 矩阵 from sympy import ones A = ones(3, 3)

1 1 1 1 1 1 1 1 1          

对角方阵 from sympy import diag A = diag(1, 2, 3)

         

上三角矩阵 from sympy import ones A = ones(3)

A.upper_triangular()

         

下三角矩阵 from sympy import ones A = ones(3)

A.lower_triangular()

         

运算图 8 代码给出矩阵相关的常用运算。

a 和b 给出两种矩阵乘法运算符，建议大家使用 @，和NumPy 矩阵乘法符号保持一致。

Page 8  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com c 和d 给出两种矩阵逆运算符。

e 将符号矩阵转化为浮点数NumPy 数组。

f 计算矩阵Q 的逆，结果为 b a ad bc −     − −   。

g 计算矩阵Q 的行列式，结果为ad – bc。

h 计算矩阵Q 的迹，结果为a + d。

from sympy import Matrix,symbols A = Matrix([[1, 3], [-2, 3]])

B = Matrix([[0, 3], [0, 7]])

A.T   # 矩阵转置 A + B # 加法 A - B # 减法 3*A   # 标量乘矩阵 A.multiply_elementwise(B) # 逐项积 A * B # 矩阵乘法 A @ B # 矩阵乘法 Matrix_2x2 = Matrix([[1.25, -0.75], [-0.75, 1.25]])

Matrix_2x2**-1   # 矩阵逆 Matrix_2x2.inv() # 矩阵逆 # 将符号矩阵转化为浮点数numpy数组 np.array(Matrix_2x2).astype(np.float64)

a, b, c, d = symbols('a b c d')

Q = Matrix([[a, b], [c, d]])

Q.inv()   # 矩阵逆 Q.det()   # 行列式 Q.trace() # 迹 a b e f g h

图 8. 用sympy 中常见矩阵运算

正定性正定性是线性代数、优化方法、机器学习重要的数学概念。下面我们用一个2 × 2 矩阵A2×2介绍正定性。

矩阵A2×2是正定，意味着f(x) = xT @ A2×2 @ x 是个开口朝上的抛物面，形状像是碗。除了 (0, 0)， f(x) = xT @ A2×2 @ x 均大于0。(0, 0) 为最小值，图中箭头都背离 (0, 0)。

矩阵A2×2是半正定，意味着f(x) = xT @ A2×2 @ x 是个开口朝上的山谷面。除了 (0, 0)，f(x) = xT @ A2×2 @ x 均大于等于0。山谷的谷底都是极小值，图中箭头都背离谷底所在直线。

Page 9  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 矩阵A2×2是负定，意味着f(x) = xT @ A2×2 @ x 是个开口朝下的抛物面。除了 (0, 0)，f(x) = xT @ A2×2 @ x 均小于0。(0, 0) 为最大值，图中箭头都指向 (0, 0)。

矩阵A2×2是半负定，意味着f(x) = xT @ A2×2 @ x 是个开口朝下的山脊面。除了 (0, 0)，f(x) = xT @ A2×2 @ x 均小于等于0。山脊的顶端都是极大值，图中箭头指向山脊顶端所在直线。

矩阵A2×2不定，意味着f(x) = xT @ A2×2 @ x 是个马鞍面，(0, 0) 为鞍点。f(x) = xT @ A2×2 @ x 符号不定。图中有些箭头背离 (0, 0)，有些指向 (0, 0)。

正定性矩阵A 和函数三维可视化二维可视化正定 ( )

, f x x   =     = + A

f(x1, x2)

x1 x2

x1 x2

正定 ( )

, f x x   =     = + A

f(x1, x2)

x1 x2

x1 x2

正定 ( )

1.5 0.5 0.5 1.5 , 1.5 1.5 f x x x x   =     = + + A

f(x1, x2)

x1 x2

x1 x2

半正定 ( )

, f x x   =     = A

f(x1, x2)

x1 x2

x1 x2

Page 10  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 半正定 ( )

0.5 0.5 0.5 0.5 , 0.5 0.5 f x x x x −   =   −   = − + A

f(x1, x2)

x1 x2

x1 x2

半正定 ( )

, f x x   =     = A

f(x1, x2)

x1 x2

x1 x2

负定 ( )

, f x x −   =   −   = − − A

f(x1, x2)

x1 x2

x1 x2

负定 ( )

, f x x −   =   −   = − − A

f(x1, x2)

x1 x2

x1 x2

负定 ( )

1.5 0.5 0.5 1.5 , 1.5 1.5 f x x x x − −   =   − −   = − − − A

f(x1, x2)

x1 x2

x1 x2

半负定 ( )

, f x x −   =     = − A

f(x1, x2)

x1 x2

x1 x2

Page 11  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 半负定 ( )

0.5 0.5 0.5 0.5 , 0.5 0.5 f x x x x −   =   −   = − + − A

f(x1, x2)

x1 x2

x1 x2

半负定 ( )

, f x x   =   −   = − A

f(x1, x2)

x1 x2

x1 x2

不定 ( )

, f x x   =   −   = − A

f(x1, x2)

x1 x2

x1 x2

不定 ( )

, f x x −   =     = − + A

f(x1, x2)

x1 x2

x1 x2

不定 ( )

, f x x x x   =     = A

f(x1, x2)

x1 x2

x1 x2

矩阵分解图 9 完成符号矩阵 a abc abc b   =     A 的特征值和特征向量。

Page 12  |  Chapter 25 SymPy 符号运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sympy import Matrix,symbols a, b, c, d = symbols('a b c d')

A = Matrix([[a**2, 2*a*b*c], [2*a*b*c, b**2]])

# 特征值 A.eigenvals()

# 特征向量 A.eigenvects()

a b

图 9. 用sympy 完成符号矩阵的特征值分解图 10 完成矩阵     =       A 的奇异值分解。U 的结果为 2 2 6 6 6 3 2 2 6 6     =     −     U ，S 的结果为   =     S ，V 的结果为 2 2 2 2 2 2 2 2   − =       V 。请大家分别计算V.T @ V，V @ V.T，U.T @ U。

from sympy import Matrix A = Matrix([[0, 1],[1, 1],[1, 0]])

# 奇异值分解 U, S, V = A.singular_value_decomposition()

a

图 10. 用sympy 完成矩阵的奇异值分解

请大家注意，SymPy 目前很多功能还不够完善。大家想要处理更为复杂的符号运算，建议使用 Mathematica 或MATLAB Symbolic Math Toolbox。

Page 1  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Scientific Computation Using SciPy SciPy 数学运算插值、积分、线性代数、优化、统计 ...

无限！没有其他问题能如此深刻地触动人类的精神。

The infinite! No other question has ever moved so profoundly the spirit of man.

—— 大卫·希尔伯特 (David Hilbert)  |  德国数学家  |  1862 ~ 1943

◄ scipy.cluster.vq.kmeans() k 均值聚类 ◄ scipy.constants.pi 圆周率 ◄ scipy.constants.golden 黄金分割比 ◄ scipy.constants.c 真空中光速 ◄ scipy.fft.fft() 一维傅里叶变换 ◄ scipy.integrate.quad() 定积分 ◄ scipy.interpolate.interp1d() 一元插值 ◄ scipy.interpolate.griddata()在不规则数据点上进行数据插值 ◄ scipy.io.loadmat() 导入MATLAB 文件 ◄ scipy.io.savemat() 保存MATLAB 文件 ◄ scipy.linalg.inv() 矩阵逆 ◄ scipy.linalg.det() 行列式 ◄ scipy.linalg.pinv() Moore-Penrose 伪逆 ◄ scipy.linalg.eig() EVD 特征值分解 ◄ scipy.linalg.cholesky() Cholesky 分解 ◄ scipy.linalg.qr() QR 分解 ◄ scipy.linalg.svd() SVD 奇异值分解 ◄ scipy.ndimage.gaussian_filter() 高斯滤波 ◄ scipy.ndimage.convolve() 多维卷积 ◄ scipy.optimize.root() 求根 ◄ scipy.optimize.minimize() 最小化 ◄ scipy.signal.convolve() 卷积 ◄ scipy.sparse.linalg.inv() 稀疏矩阵的逆 ◄ scipy.sparse.linalg.norm() 稀疏矩阵范数 ◄ scipy.spatial.distance.euclidean() 欧氏距离 ◄ scipy.spatial.distance_matrix() 距离矩阵 ◄ scipy.special.factorial() 阶乘 ◄ scipy.special.gamma() Gamma 函数 ◄ scipy.special.beta() Beta 函数 ◄ scipy.special.erf() 误差函数 ◄ scipy.special.comb() 组合数 ◄ scipy.stats.norm() 一元高斯分布 ◄ scipy.stats.multivariate_normal() 多元高斯分布 ◄ scipy.stats.gaussian_kde() 高斯核密度估计

Page 2  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 26.1 什么是SciPy？

SciPy 是一个Python 的开源科学计算库，SciPy 构建在NumPy 之上，并提供了许多有用的功能，用于数值计算、优化、统计和信号处理等科学与工程领域。一些具体的用途包括： ► 数据预处理和特征工程：SciPy 提供了丰富的工具用于数据的插值、滤波、变换等，这些在数据预处理和特征工程中很有用。

► 优化问题：SciPy 中的optimize 模块包含了各种常用的优化算法，可用于解决机器学习中的参数优化问题，例如模型训练中的参数调整。

► 数值计算：SciPy 提供了高效的数值计算工具，例如求解线性代数问题、解微分方程、积分等，在数值计算密集型的机器学习任务中很有帮助。

► 统计分析：SciPy 中的stats 模块提供了许多常用的统计分析函数，例如概率分布函数、假设检验等，可以用于数据分析和模型评估。

► 信号处理：SciPy 中的signal 模块提供了信号处理的工具，例如滤波、傅里叶变换等，这些在处理时间序列数据或图像数据时非常有用。

► SciPy 强大且灵活，因此在机器学习领域也有广泛的应用。在机器学习领域，SciPy 主要用于数据预处理、特征工程、优化问题、数值计算、统计分析以及信号处理等方面。

本章介绍如何使用SciPy 中几个常见函数。

表 1. SciPy 常用模块以及示例函数模块名称描述举例 scipy.cluster 聚类 scipy.cluster.vq.kmeans() k 均值聚类 scipy.constants 数学和物理常数 scipy.constants.pi 圆周率 scipy.constants.golden 黄金分割比 scipy.constants.c 真空中光速 scipy.fft 快速傅里叶变换 scipy.fft.fft() 一维傅里叶变换 scipy.integrate 积分 scipy.integrate.quad() 定积分 scipy.interpolate 插值和拟合 scipy.interpolate.interp1d() 一元插值 scipy.interpolate.griddata()在不规则数据点上进行数据插值 scipy.io 数据输入输出 scipy.io.loadmat() 导入MATLAB 文件 scipy.io.savemat() 保存MATLAB 文件 scipy.linalg 线性代数 scipy.linalg.inv() 矩阵逆 scipy.linalg.det() 行列式 scipy.linalg.pinv() Moore-Penrose 伪逆 scipy.linalg.eig() EVD 特征值分解 scipy.linalg.cholesky() Cholesky 分解 scipy.linalg.qr() QR 分解 scipy.linalg.svd() SVD 奇异值分解 scipy.ndimage n 维图像处理 scipy.ndimage.gaussian_filter() 高斯滤波 scipy.ndimage.convolve() 多维卷积 scipy.odr 正交回归 (正交距离回归)

scipy.optimize 优化算法 scipy.optimize.root() 求根 scipy.optimize.minimize() 最小化 scipy.optimize.curve_fit() 拟合 scipy.signal 信号处理 scipy.signal.convolve() 卷积 scipy.sparse 稀疏矩阵工具 scipy.sparse.linalg.inv() 稀疏矩阵的逆 scipy.sparse.linalg.norm() 稀疏矩阵范数 scipy.spatial 空间数据结构和算法 scipy.spatial.distance.euclidean() 欧氏距离

Page 3  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com scipy.spatial.distance_matrix() 距离矩阵 scipy.special 特殊数学函数 scipy.special.factorial() 阶乘 scipy.special.gamma() Gamma 函数 scipy.special.beta() Beta 函数 scipy.special.erf() 误差函数 scipy.special.comb() 组合数 scipy.stats 统计 scipy.stats.norm() 一元高斯分布 scipy.stats.multivariate_normal() 多元高斯分布 scipy.stats.gaussian_kde() 高斯核密度估计

## 26.2 距离

图 1 所示的平面上两点，(8, 8) 和 (2, 0)，之间的欧氏距离为( )

( )

− + − = 。利用SciPy 函数 scipy.spatial.distance.euclidean([8,8],[2,0])，我们可以得到同样结果。

y (2,0)

(8,8)

Euclidean distance

图 1. 平面上两点之间的欧氏距离

图 2 所示为利用随机数发生器生成的26 个平面坐标，对应26 个字母；其中B 和S 重叠，D 和O 重叠。图中彩色线为两两成对坐标连线，距离远的用暖色系颜色渲染，距离近的用冷色系颜色渲染。图 3 所示为成对距离矩阵。

Page 4  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com W H L G J C U Q Y K D(O)

E R P Z N A T V X M B(S)

F I y

图 2. 平面上26 个点之间的两两欧氏距离 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

图 3. 成对欧氏距离矩阵

图 4 所示为绘制图 2 和图 3 代码。下面我们分析其中一些关键语句。

Page 5  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

import matplotlib.pyplot as plt import itertools import numpy as np import matplotlib as mpl import seaborn as sns import string from scipy.spatial import distance_matrix from scipy.spatial.distance import euclidean import os # 如果文件夹不存在，创建文件夹 if not os.path.isdir("Figures"): os.makedirs("Figures")

# 产生随机数 num = 26 np.random.seed(0)

data = np.random.randint(10 + 1, size=(num, 2))

labels = list(string.ascii_uppercase)

cmap = mpl.cm.get_cmap('RdYlBu_r')

fig, ax = plt.subplots()

# 绘制成对线段 for i, d in enumerate(itertools.combinations(data, 2)): d_idx = euclidean(d[0],d[1])

plt.plot([d[0][0],d[1][0]], [d[0][1],d[1][1]], color = cmap(d_idx/np.sqrt(2)/10),lw = 1)

ax.scatter(data[:,0],data[:,1], marker = 'x',color = 'k',s = 50,zorder=100)

# 添加标签 for i, txt in enumerate(labels): ax.annotate(txt,(data[i,0] + 0.2, data[i,1] + 0.2))

ax.set_xlim(0, 10); ax.set_ylim(0, 10)

ax.set_xticks(np.arange(11))

ax.set_yticks(np.arange(11))

plt.xlabel('x'); plt.ylabel('y')

ax.grid(ls='--',lw=0.25,color=[0.5,0.5,0.5])

ax.set_aspect('equal', adjustable='box')

fig.savefig('Figures/成对距离连线.svg', format='svg')

# 计算成对距离矩阵 pairwise_distances = distance_matrix(data, data)

fig, ax = plt.subplots()

sns.heatmap(pairwise_distances, cmap = 'RdYlBu_r', square = True, xticklabels = labels,yticklabels = labels, ax = ax)

fig.savefig('Figures/成对距离矩阵热图.svg', format='svg')

a b n h j g e f k

图 4. 计算、可视化成对距离，代码

a 导入 Python 标准库中的 string 模块。Python 中的 string 模块提供了许多字符串处理相关的函数和常量，可以方便地进行字符串操作。比如，string.ascii_uppercase: 包含所有大写 ASCII 字母 (A-Z) 的字符串，string.digits: 包含所有数字 (0-9) 的字符串。

Page 6  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b 从scipy.spatial 中导入distance_matrix 函数，用于计算多个点之间的成对距离矩阵。它接受点坐标的数组或列表，然后计算每两个点之间的距离，并返回一个矩阵，其中的每个元素表示两个点之间的距离。

c 从 scipy.spatial.distance 模块中导入了 euclidean 函数，用来计算两点欧氏距离。

d 设置随机数生成器的种子seed 为 0，从而使随机数的生成具有确定性，保证实验结果可重复性。

e 在 [0, 10] 区间之内生成随机整数，形状为26 行、2 列。

f 生成A-Z 大写字母字符串，并将其转换为列表。

g 从matplotlib 通过cm.get_cmap() 函数来获取一个名为 'RdYlBu_r' 的颜色映射对象。'RdYlBu_r' 是一个预定义的颜色映射名称，它表示一种从红色Rd 到黄色Yl 再到蓝色Bu 的颜色渐变，且颜色映射反向 (末尾带 _r 表示反向)。鸢尾花书也管颜色映射叫色谱。

颜色映射对象通常被用于将数据的数值范围 [0, 1] 映射到一系列颜色中的某个位置。这个数值范围一般默认为 [0, 1]，其中 0 对应着颜色映射的起始位置，1 对应着颜色映射的结束位置。颜色映射会将 [0, 1] 区间内的数据值线性地映射到预定义的颜色序列上。在使用 Matplotlib 中的颜色映射对象时，可以使用 matplotlib.colors.Normalize() 函数将数据规范化到 [0, 1] 区间，然后再将规范化后的数据传递给颜色映射对象来获取对应的颜色。《可视之美》还会进一步介绍非线性映射，以及如何构造颜色映射。

Bu Yl Rd 0.0 0.5 1.0 Bu Yl Rd 0.0 0.5 1.0 Color mapping Color mapping Min Max Normalize

图 5. 颜色映射

h 使用了 Python 中的 enumerate 函数和 itertools.combinations 函数，用于在数据 data 的所有两两组合之间进行循环迭代，并在每次迭代中获取索引和组合数据。

i 利用scipy.spatial.distance.euclidean() 计算两个点之间的欧氏距离。

k 把图 3 欧氏距离转化为 [0, 1] 之间的数。显然在图 3 平面上，最大的距离为10  。

l 通过for 循环利用annotate() 给每个散点添加字母标签。

m 计算26 个散点的成对距离矩阵，这个矩阵的大小为26 × 26。这个矩阵的主对角线 (图 3 虚线) 的元素代表某个点到自身的距离，即0。我们容易发现，图 3 这个矩阵沿着主对角线对称；因此这个距离矩

Page 7  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 阵也叫对称矩阵 (symmetric matrix)。换个角度来看，我们只需要这个26 × 26 矩阵中除主对角线以外， 下三角 (图 6) 或上三角矩阵的元素信息。

n 利用seaborn.heatmap() 绘制成对距离热图。

A B C D E F G H I J K L M N O P Q R S T U V W X Y B C D E F G H I J K L M N O P Q R S T U V W X Y Z

图 6. 剔除主对角线元素的下三角矩阵

图 7 代码绘制图 6。和图 4 代码不同的是，在生成成对距离矩阵之后，我们还生成了一个 (剔除主对角线) 下三角矩阵的面具 (mask)。在鸢尾花书中，mask 一般被直译为面具，也常被翻译做蒙皮、掩码、遮罩等等。

a 用了NumPy 库中的函数来创建一个面具"mask"，用于过滤计算得到的"pairwise_ds"数组。

numpy.ones_like() 创建了一个与"pairwise_ds"数组形状相同的全为1 的布尔类型数组。"dtype=bool"指定数组元素的数据类型为布尔类型 (True 或False)，所有元素都被设置为True。numpy.triu() 函数的"triu"代表"triangle upper"，它是"numpy"库中的函数，用于获取矩阵的上三角部分 (包括对角线)，而将下三角部分设置为0。

如b 所示，使用seaborn.heatmap 绘制热图时，mask 中对应位置为True 的单元格的成对距离矩阵数据将不会被显示。

Page 8  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import matplotlib.pyplot as plt import numpy as np import seaborn as sns import string from scipy.spatial import distance_matrix # 产生随机数 num = 26 np.random.seed(0)

data = np.random.randint(10 + 1, size=(num, 2))

labels = list(string.ascii_uppercase)

# 计算成对距离矩阵 pairwise_ds = distance_matrix(data, data)

# 产生蒙皮/面具 mask = np.triu(np.ones_like(pairwise_ds, dtype=bool))

fig, ax = plt.subplots()

sns.heatmap(pairwise_distances, mask = mask, cmap = 'RdYlBu_r', square = True, xticklabels = labels, yticklabels = labels, ax = ax)

fig.savefig('下三角.svg', format='svg')

b a

图 7. 可视化成对距离矩阵下三角部分 (不含主对角线元素)，代码

## 26.3 插值

插值 (interpolation) 是通过已知数据点之间的值来估计未知点的值的方法，它可以用于填补数据缺失或者进行数据平滑处理。

如图 8 所示的蓝色点为已知数据点，插值就是根据这几个离散的数据点估算其他点对应的y 值。

y Interpolation Extrapolation Extrapolation

图 8. 插值的意义

Page 9  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 插值可分为内插 (interpolation) 和外插 (extrapolation)。内插是在已知数据点之间进行插值，估计出未知点的值。而外插则是在已知数据点的范围之外进行插值，从而预测超出已知数据点范围的未知点的值。在进行外插时，需要考虑插值函数是否能够正确地拟合未知数据点，并且需要注意不要过度依赖插值函数来进行预测，以免导致不可靠的预测结果。

图 9 比较六种插值方法，下面结合图 10 逐一介绍。

(a) linear (b) quadratic (c) cubic (d) previous (e) next (f) nearest

图 9. 比较六种不同插值方法 a 创建一个2 行3 列的图形子图网格，并设置图形的尺寸和共享坐标轴属性。参数2, 3 指定了网格的行数 (2) 和列数 (3)，即总共有6 个子图。sharex='col'指定每一列子图将共享相同的x 轴，而 sharey='row'指定每一行子图将共享相同的y 轴。这样设置可以使得网格中的子图在x 轴和y 轴方向上有一致的刻度和范围。

b 中的flatten() 多维数组转换为一维数组。在这里，函数被应用于"axes"轴对象，将二维的子图网格数组转换成了一维数组。

c 列表列出6 种插值方法。

d 调用SciPy 库中的interp1d 函数来进行一维插值。其中，x 这是一个一维数组或列表，表示原始数据点的横坐标，即自变量。y 也是一个一维数组或列表，表示原始数据点的纵坐标，即因变量。

参数kind 用于指定插值方法。其中，'linear' 为线性插值。在两个相邻数据点之间进行线性插值，即使用直线来连接两个数据点。如图 9 (a) 所示，多点线性插值结果一般为折线。'quadratic' 是二次插值，相邻点之间通过二次函数连接。如图 9 (b) 所示，二次插值产生的曲线较为平滑。

'cubic' 是三次插值，相邻点之间通过三次次函数连接。如图 9 (c) 所示，三次插值产生的曲线非常平滑，能够更好地逼近数据点之间的曲线。

'nearest' 代表最近邻插值。如图 9 (d) 所示，'nearest'使用与插值点最近的数据点的值作为插值结果。

Page 10  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 'previous' 代表前向插值。如图 9 (e) 所示，使用插值点之前的数据点的值作为插值结果。

'next' 代表后向插值。如图 9 (f) 所示，使用插值点之后的数据点的值作为插值结果。

import numpy as np import matplotlib.pyplot as plt from scipy.interpolate import interp1d # 生成随数据 np.random.seed(8)

x = np.linspace(0, 10, 10)

y = np.random.rand(10) * 10 x_fine = np.linspace(0, 10, 1001)

# 创建一个图形对象，包含六个子图 fig, axes = plt.subplots(2, 3, figsize=(6, 9), sharex = 'col', sharey = 'row')

axes = axes.flatten()

# 六种插值方法 methods = ['linear','quadratic','cubic', 'previous','next','nearest']

for i, method in enumerate(methods):

# 创建 interp1d 对象 f = interp1d(x, y, kind=method)

# 生成插值后的新数据点 y_fine = f(x_fine)

# 绘制子图 axes[i].plot(x, y, 'o', label='Data', markeredgewidth=1.5, markeredgecolor = 'w', zorder = 100)

axes[i].plot(x_fine,y_fine,label='Interpolated')

axes[i].set_title(f'Method: {method}')

axes[i].legend()

axes[i].set_xlim(0, 10)

axes[i].set_ylim(0, 10)

axes[i].set_aspect('equal', adjustable='box')

plt.tight_layout()

fig.savefig('不同插值方法.svg', format='svg')

a e b

图 10. 比较六种插值方法，代码

大家经常混淆拟合和插值这两种方法。插值和拟合有一个相同之处，它们都是根据已知数据点，构造函数，从而推断得到更多数据点。

Page 11  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 插值和回归都是用于对数据进行预测的方法，但两者有明显的区别。插值是用于填补已有数据点之间的空缺，预测未知点的值。回归则是预测自变量和因变量之间的关系。插值通常使用插值函数，如多项式插值；而回归则通过拟合数据点的回归方程来预测因变量的值。插值通常用于数据平滑处理、数据填补等。回归则常用于预测和建模。插值要求原始数据点之间要有一定的连续性和平滑性；而回归则对数据点的分布没有明显要求。插值得到的是精确的函数值，但在超出已有数据范围时可能不准确；而回归得到的是变量之间的大致关系，可以预测未来的趋势。

需要根据具体情况选择合适的方法。当数据缺失或需要平滑处理时，可以使用插值方法；当需要建立模型并预测未来趋势时，可以使用回归方法。

插值一般得到分段函数，分段函数通过所有给定的数据点，如图 11 (a)、(b) 所示。回归拟合得到的函数尽可能靠近样本数据点，如图 11 (c)、(d) 所示。

(a) linear interpolation (b) cubic interpolation (c) linear regression (d) polynomial regression

图 11. 比较一维插值和回归

## 26.4 高斯分布

高斯分布 (Gaussian Distribution)，也称为正态分布 (Normal Distribution)，是概率论和统计学中最重要且广泛应用的分布之一。高斯分布以数学家卡尔·弗里德里希·高斯 (Carl Friedrich Gauss) 的名字命名。

一元高斯分布概率密度函数 (Probability Density Function, PDF) 的特点是钟形曲线，对称分布，均值 µ 和标准差σ 决定了分布的位置和形状。均值决定了曲线的中心，标准差决定了曲线的宽窄程度。图 12 (a) 所示均值µ 对一元高斯分布概率密度函数形状影响。图 12 (b) 所示标准差σ 对一元高斯分布概率密度函数形状影响。

Page 12  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

什么是概率密度函数？

概率密度函数是用于描述连续随机变量的概率分布的数学函数。它指定了随机变量落在不同取值范围内的概率密度，而不是具体的概率值。一元随机变量的PDF 在整个取值范围内的面积等于1，因为随机变量必然会在某个取值范围内取值。

(a)

(b)

图 12. 一元高斯分布PDF，均值µ、标准差σ 分别影响

图 13 绘制图 12 两幅子图。下面讲解图 13 中代码中最要的语句。

a 从scipy.stats 模块导入norm 子模块，为一元正态分布对象。导入norm 模块后，可以使用其中提供的函数和方法来进行正态分布相关的操作，比如计算概率密度函数PDF、累积分布函数CDF、随机样本的生成等。

b 中np.linspace(0, 1, len(mu_array)) 返回一个由0 到1 之间等间隔的数值构成的数组，数组的长度与mu_array 的长度相同。mu_array 是之前定义的不同的均值取值。这些 [0, 1] 之间的数用到颜色映射。

c 则利用 scipy.stats.norm.pdf(x, loc, scale) 函数；其中，x 为需要计算概率密度的数值，可以是一个数值或一个数组。loc 为正态分布的均值，loc 是location 的简写。scale 代表正态分布的标准差。

d 设定曲线图例的字符串。其中，'$\mu$ = '是一个字符串，表示希腊字母"μ"。

e 用于在绘制的图表中添加图例，ncol 是一个整数参数，用于设置图例的列数。

Page 13  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import matplotlib.pyplot as plt from matplotlib import cm from scipy.stats import norm x_array = np.linspace(-6, 6, 200)

mu_array = np.linspace(-4, 4, 9)

# 设定均值一系列取值 colors = cm.RdYlBu(np.linspace(0,1,len(mu_array)))

# 均值对一元高斯分布PDF影响 fig, ax = plt.subplots(figsize = (5,4))

for idx, mu_idx in enumerate(mu_array): pdf_idx = norm.pdf(x_array,scale = 1,loc = mu_idx)

legend_idx = '$\mu$ = ' + str(mu_idx)

plt.plot(x_array, pdf_idx, color=colors[idx], label = legend_idx)

plt.legend(ncol=3)

ax.set_xlim(x_array.min(),x_array.max())

ax.set_ylim(0,1)

ax.set_xlabel('x')

ax.set_ylabel('PDF, $f_X(x)$')

sigma_array = np.linspace(0.5,5,10)

# 设定标准差一系列取值 colors = cm.RdYlBu(np.linspace(0,1,len(sigma_array)))

# 标准差对一元高斯分布PDF影响 fig, ax = plt.subplots(figsize = (5,4))

for idx, sigma_idx in enumerate(sigma_array): pdf_idx = norm.pdf(x_array, scale = sigma_idx)

legend_idx = '$\sigma$ = ' + str(sigma_idx)

plt.plot(x_array, pdf_idx, color=colors[idx], label = legend_idx)

plt.legend()

ax.set_xlim(x_array.min(),x_array.max())

ax.set_ylim(0,1)

ax.set_xlabel('x')

ax.set_ylabel('PDF, $f_X(x)$')

a b e

图 13. 可视化一元高斯分布概率密度函数，代码

Page 14  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a) ρ =  0.9 PDF PDF PDF PDF PDF PDF PDF PDF PDF (b) ρ =  0.7 (c) ρ =  0.5 (d) ρ =  0.3 (e) ρ = 0.0 (f) ρ = 0.3 (g) ρ = 0.5 (h) ρ = 0.7 (i) ρ = 0.7 y y y y y y y y y

图 14. 二元高斯分布PDF，曲面

Page 15  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import matplotlib.pyplot as plt from scipy.stats import multivariate_normal rho_array = [-0.9, -0.7, -0.5, -0.3, 0, 0.3, 0.5, 0.7, 0.9]

sigma_X = 1; sigma_Y = 1 # 标准差 mu_X = 0;    mu_Y = 0    # 期望 width = 4 X = np.linspace(-width,width,321)

Y = np.linspace(-width,width,321)

XX, YY = np.meshgrid(X, Y)

XXYY = np.dstack((XX, YY))

# 曲面 fig = plt.figure(figsize = (8,8))

for idx, rho_idx in enumerate(rho_array): # 质心 mu    = [mu_X, mu_Y]

# 协方差 Sigma = [[sigma_X**2, sigma_X*sigma_Y*rho_idx], [sigma_X*sigma_Y*rho_idx, sigma_Y**2]]

# 二元高斯分布 bi_norm = multivariate_normal(mu, Sigma)

f_X_Y_joint = bi_norm.pdf(XXYY)

ax = fig.add_subplot(3,3,idx+1,projection='3d')

ax.plot_wireframe(XX, YY, f_X_Y_joint, rstride=10, cstride=10, color = [0.3,0.3,0.3], linewidth = 0.25)

ax.contour(XX,YY, f_X_Y_joint,15, cmap = 'RdYlBu_r')

ax.set_xlabel('$x$'); ax.set_ylabel('$y$')

ax.set_zlabel('$f_{X,Y}(x,y)$')

ax.view_init(azim=-120, elev=30)

ax.set_proj_type('ortho')

ax.set_xlim(-width, width); ax.set_ylim(-width, width)

ax.set_zlim(f_X_Y_joint.min(),f_X_Y_joint.max())

# ax.axis('off')

plt.tight_layout()

fig.savefig('二元高斯分布，曲面.svg', format='svg')

plt.show()

a b e f g h j

图 15. 网格曲面可视化二元高斯分布PDF，代码

Page 16  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a) ρ =  0.9 (b) ρ =  0.7 (c) ρ =  0.5 (d) ρ =  0.3 (e) ρ = 0.0 (f) ρ = 0.3 (g) ρ = 0.5 (h) ρ = 0.7 (i) ρ = 0.7 y y y y y y y y y

图 16. 二元高斯分布PDF，平面填充等高线

Page 17  |  Chapter 26 SciPy 数学运算  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 平面填充等高线 fig = plt.figure(figsize = (8,8))

for idx, rho_idx in enumerate(rho_array): mu    = [mu_X, mu_Y]

Sigma = [[sigma_X**2, sigma_X*sigma_Y*rho_idx], [sigma_X*sigma_Y*rho_idx, sigma_Y**2]]

bi_norm = multivariate_normal(mu, Sigma)

f_X_Y_joint = bi_norm.pdf(XXYY)

ax = fig.add_subplot(3,3,idx+1)

ax.contourf(XX, YY, f_X_Y_joint, levels = 12, cmap='RdYlBu_r')

ax.set_xlabel('$x$')

ax.set_ylabel('$y$')

ax.set_xlim(-width, width)

ax.set_ylim(-width, width)

ax.axis('off')

plt.tight_layout()

fig.savefig('二元高斯分布，等高线.svg', format='svg')

plt.show()

a b

图 17. 平面填充等高线可视化二元高斯分布PDF，代码

Page 1  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Statistical Modeling Using Statsmodels Statsmodels 统计模型简介线性回归、主成分分析、概率密度估计

教育点燃火焰，绝非填鸭灌输。

Education is the kindling of a flame, not the filling of a vessel .

—— 苏格拉底 (Socrates)  |  古希腊哲学家  |  470 ~ 399 BC

◄ statsmodels.api.nonparametric.KDEUnivariate() 构造一元KDE ◄ statsmodels.graphics.boxplots.violinplot() 小提琴图 ◄ statsmodels.graphics.gofplots.qqplot() QQ 图 ◄ statsmodels.graphics.plot_grids.scatter_ellipse() 散点椭圆 ◄ statsmodels.multivariate.factor.Factor() 因子分析 ◄ statsmodels.multivariate.pca.PCA() 主成分分析 ◄ statsmodels.nonparametric.kde.KDEUnivariate() 单变量核密度估计 ◄ statsmodels.nonparametric.kernel_density.KDEMultivariate() 构造多元KDE ◄ statsmodels.regression.linear_model.OLS() OLS 线性回归 ◄ statsmodels.regression.linear_model.WLS() 加权OLS 线性回归 ◄ statsmodels.regression.rolling.RollingOLS() 移动OLS 线性回归 ◄ statsmodels.tsa.ar_model.AutoReg() AR 模型 ◄ statsmodels.tsa.arima.model.ARIMA() ARIMA 模型 ◄ statsmodels.tsa.seasonal.seasonal_decompose() 季节性分解

Page 2  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 27.1 什么是Statsmodels?

Statsmodels 是一个Python 库，用于估计统计模型并进行统计数据分析。在机器学习领域， Statsmodels 虽然没有像scikit-learn 这样的机器学习库那么全面，但是Statsmodels 提供了许多统计方法和模型，用于探索数据、进行假设检验、进行预测和模型拟合等。

Statsmodels 主要用于以下任务。

► 最小二乘线性回归 (Ordinary Least Square Regression)，用于拟合线性模型和探索线性关系。

► 方差分析 (Analysis of Variance, ANOVA)，用于比较多个组之间的差异。

► 主成分分析 (Principal Component Analysis, PCA)。

► 时间序列分析，如ARIMA 模型。

► 非参数方法 (Nonparametric Methods)，比如核密度估计 (Kernel Density Estimation, KDE)。

► 统计假设检验 (statistical hypothesis testing)。

► 分位图，又称QQ 图 (Quantile-Quantile plot)。

本章介绍如何使用Statsmodels 中几个常见函数。

表 1. Statsmodels 常用模块以及示例函数模块描述举例 statsmodels.graphics 统计绘图 statsmodels.graphics.boxplots.violinplot() 小提琴图 statsmodels.graphics.plot_grids.scatter_ellipse() 散点椭圆 statsmodels.graphics.gofplots.qqplot() QQ 图 statsmodels.multivariate 多元统计 statsmodels.multivariate.pca.PCA() 主成分分析 statsmodels.multivariate.factor.Factor() 因子分析 statsmodels.regression 回归分析 statsmodels.regression.linear_model.OLS() OLS 线性回归 statsmodels.regression.rolling.RollingOLS() 移动OLS 线性回归 statsmodels.regression.linear_model.WLS() 加权OLS 线性回归 statsmodels.nonparametric 非参数方法 statsmodels.nonparametric.kde.KDEUnivariate() 单变量核密度估计 statsmodels.tsa 时间序列 statsmodels.tsa.ar_model.AutoReg() AR 模型 statsmodels.tsa.arima.model.ARIMA() ARIMA 模型 statsmodels.tsa.seasonal.seasonal_decompose() 季节性分解

## 27.2 平面散点图 + 椭圆

上一章在介绍高斯分布时，我们知道了二元高斯分布和椭圆的关系。

平面散点图 (scatter plot) 是一种常用的可视化方式，用于展示两个变量之间的关系。它将各个数据点表示为笛卡尔坐标系上的点。scatter_ellipse 函数是 statsmodels.graphics.plot_grids 模块的一部分，用于创建带有椭圆表示置信区间的散点图。简单来说，scatter_ellipse 函数在基本散点图的基础上添加了椭圆，用于展示样本数据的置信区间。

图 1 所示为鸢尾花数据的“平面散点图 + 椭圆”。图 2、图 3、图 4 这三幅图考虑了鸢尾花标签。

注意，scatter_ellipse 函数默认图像线条颜色为黑色。图 1 ~ 图 4 这四幅图在后期处理时修改了颜色。

此外，图中下三角相关性系数矩阵热图来自本书第23 章。

鸢尾花书《统计至简》第23 章将会介绍这四幅图背后的数学工具。

Page 3  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal width, X2 Petal length, X3 0.12 0.87 0.43 0.82 0.37 0.96 X1 X2 X3 X2 X3 X4 ρ = 0.87 ρ =  0.12 ρ = 0.82 ρ =  0.37 ρ =  0.43 ρ = 0.96

图 1. 平面散点图 + 椭圆，鸢尾花数据集 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal width, X2 Petal length, X3 ρ = 0.27 ρ = 0.74 ρ = 0.28 ρ = 0.23 ρ = 0.18 ρ = 0.33 'species' == 'setosa' 0.74 0.27 0.18 0.28 0.23 0.33 X1 X2 X3 X2 X3 X4

图 2. 平面散点图 + 椭圆，鸢尾花数据集，'species' == 'setosa'

Page 4  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 'species' == 'versicolor' 0.53 0.75 0.56 0.55 0.66 0.79 X1 X2 X3 X2 X3 X4 Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal width, X2 Petal length, X3 ρ = 0.75 ρ = 0.53 ρ = 0.55 ρ = 0.66 ρ = 0.56 ρ = 0.79

图 3. 平面散点图 + 椭圆，鸢尾花数据集，'species' == 'versicolor' Sepal length, X1 Sepal width, X2 Petal length, X3 Petal width, X4 Sepal width, X2 Petal length, X3 ρ = 0.86 ρ = 0.46 ρ = 0.28 ρ = 0.54 ρ = 0.40 ρ = 0.32 X1 X2 X3 X2 X3 X4 'species' ==  'virginica' 0.46 0.86 0.40 0.28 0.54 0.32

图 4. 平面散点图 + 椭圆，鸢尾花数据集，'species' == 'virginica'

Page 5  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 5 所示为绘制图 1 ~ 图 4 的代码。

a 从 statsmodels 库的 plot_grids 模块中访问 scatter_ellipse 函数。

b 绘制平面散点图 + 椭圆。scatter_ellipse 函数中，level (默认0.9) 是一个可选参数，用于控制绘制椭圆时表示置信区间的置信水平 (confidence level)。置信区间是一个范围，用于表示对一个未知参数的估计。一个 95% 的置信区间意味着我们有 95% 的置信度认为真实的参数值位于该区间内。

c 用loc 选取鸢尾花不同标签样本数据。

import matplotlib.pyplot as plt import numpy as np import seaborn as sns from statsmodels.graphics.plot_grids import scatter_ellipse # 导入鸢尾花数据 data_raw = sns.load_dataset('iris')

labels = ['Sepal length','Sepal width', 'Petal length','Petal width']

fig = plt.figure(figsize=(8,8))

scatter_ellipse(data_raw.iloc[:,:-1], varnames=labels, fig=fig)

fig.savefig('散点 + 椭圆.svg', format='svg')

for s_idx in data_raw.species.unique(): data= data_raw.loc[data_raw.species == s_idx].iloc[:,:-1]

fig = plt.figure(figsize=(8,8))

scatter_ellipse(data, varnames=labels, fig=fig)

fig.savefig('散点 + 椭圆 ' + s_idx + '.svg', format='svg')

b a

图 5. 平面散点图 + 椭圆，代码

## 27.3 最小二乘线性回归

最小二乘 (Ordinary Least Square, OLS) 线性回归 (linear regression) 是一种用于建立线性模型的统计学方法，其目标是通过找到最佳拟合直线来预测因变量和一个或多个自变量之间的线性关系。这种方法被广泛应用于各种领域，包括数据分析、机器学习等等。

如图 6 (a) 所示，在最小二乘线性回归中，我们尝试找到一条直线，使得所有数据点到这条线的距离之和最小。这里的“距离”通常是指因变量与回归线预测值之间的差异，称为残差。图 6 (b) 中灰色线段就是残差。

我们的目标是最小化所有数据点的残差平方和，因此称为“最小二乘”。

Page 6  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com (a)

(b)

图 6. 一元线性回归

图 7 代码绘制图 6 (b)。

a 产生用于回归的样本数据。

b 中sm.add_constant(x_data) 是 statsmodels 中的一个函数，用于在矩阵或数组 x_data 的左侧添加全 1 常数列，目的是为了计算截距项。

c 进行最小二乘线性回归分析。

d 调用 fit() 方法来对模型进行拟合，从而得到对应的回归系数和其他相关统计信息。

e 打印回归结果，具体如图 8 所示。

鸢尾花书《数据有道》将逐一介绍图 8 这些回归分析结果。

f 中results.params 保存线性回归结果，results.params[1] 为斜率b1，results.params[0] 为截距b0。一元线性回归的解析式为y = b1x + b0。

g 绘制预测值 (predicted value) 散点图，图 6 (b) 中的 ×。图 6 (b) 中的蓝色点 ● 为样本数据。

h 绘制样本值 ● 和预测值 × 连线线段。这个线段代表误差。

本书第30 章还会继续介绍Scikit-Learn 中的回归算法工具。

Page 7  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import statsmodels.api as sm import matplotlib.pyplot as plt # 生成随机数据 num = 50 np.random.seed(0)

x_data = np.random.uniform(0,10,num)

y_data = 0.5 * x_data + 1 + np.random.normal(0, 1, num)

data = np.column_stack([x_data,y_data])

# 添加常数列 X = sm.add_constant(x_data)

# 创建一元OLS线性回归模型 model = sm.OLS(y_data, X)

# 拟合模型 results = model.fit()

# 打印回归结果 print(results.summary())

# 预测 x_array = np.linspace(0,10,101)

predicted = results.params[1] * x_array + results.params[0]

fig, ax = plt.subplots()

ax.scatter(x_data, y_data)

ax.scatter(x_data, results.fittedvalues, color = 'k', marker = 'x')

ax.plot(x_array, predicted, color = 'r')

data_ = np.column_stack([x_data,results.fittedvalues])

ax.plot(([i for (i,j) in data_], [i for (i,j) in data]), ([j for (i,j) in data_], [j for (i,j) in data]), c=[0.6,0.6,0.6], alpha = 0.5)

ax.set_xlabel('x'); ax.set_ylabel('y')

ax.set_aspect('equal', adjustable='box')

ax.set_xlim(0,10); ax.set_ylim(-2,8)

fig.savefig('一元线性回归.svg', format='svg')

b a e f g h

图 7. 一元OLS 线性回归，代码 OLS Regression Results ============================================================================== Dep. Variable:                      y   R-squared:                       0.656 Model:                            OLS   Adj. R-squared:                  0.649 Method:                 Least Squares   F-statistic:                     91.59 Date:                XXXXXXXXXXXXXXXX   Prob (F-statistic):           1.05e-12 Time:                        XXXXXXXX   Log-Likelihood:                -67.046 No. Observations:                  50   AIC:                             138.1 Df Residuals:                      48   BIC:                             141.9 Df Model:                           1 Covariance Type:            nonrobust ============================================================================== coef    std err          t      P>|t|      [0.025      0.975]

------------------------------------------------------------------------------ const          0.9928      0.296      3.358      0.002       0.398       1.587 x1             0.4693      0.049      9.570      0.000       0.371       0.568 ============================================================================== Omnibus:                        1.199   Durbin-Watson:                   2.274 Prob(Omnibus):                  0.549   Jarque-Bera (JB):                1.213 Skew:                           0.283   Prob(JB):                        0.545 Kurtosis:                       2.487   Cond. No.                         13.6 ==============================================================================

图 8. 一元OLS 线性回归结果

Page 8  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 27.4 主成分分析

主成分分析 (principal component analysis, PCA) 是数据降维的重要方法之一。简单来说，通过线性变换，主成分分析将原始多维数据投影到一个新的正交坐标系，将原始数据中的最大方差成分提取出来。

举个例子，主成分分析实际上寻找数据在主元空间内投影。图 9 所示杯子，它是一个3D 物体，在一张图展示杯子，而且尽可能多地展示杯子细节，就需要从空间多个角度观察杯子并找到合适角度。这个过程实际上是将三维数据投影到二维平面过程。这也是一个降维过程，即从三维变成二维。图 10 展示杯子六个平面上投影结果。

H1 H2 H3 H4 H5 H6

图 9. 咖啡杯六个投影方向

Page 9  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com H1 H2 H3 H4 H5 H6

图 10. 咖啡杯在六个方向投影图像

Xn × D ΣD × D VD × D Descending eigenvalues λ Calculate covariance matrix Eigen decomposition Select p eigenvectors with highest eigenvalues Project data or centralized data to the selected PCs Covariance matrix Matrix of eigenvectors Reduced data Λ Selected eigenvectors n × D D × D D × p n × p Zn × p VD × p XVD × p

图 11. 主成分分析一般技术路线：特征值分解协方差矩阵

如图 11 所示，PCA 的一般步骤如下： ◄ 计算原始数据Xn × D的协方差矩阵ΣD × D； ◄ 对Σ 特征值分解，获得特征值λi与特征向量矩阵VD × D； ◄ 对特征值λi从大到小排序，选择其中特征值最大的p 个特征向量；

Page 10  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ◄ 将原始数据 (中心化数据) 投影到这p 个正交向量构建的低维空间中，获得得分Zn × p。

很多时候，在第一步中，我们先标准化 (standardization) 原始数据，即计算X 的Z 分数。标准化防止不同特征上方差差异过大。而有些情况，对原始数据Xn × D进行中心化 (去均值) 就足够了，即将数据质心移到原点。

下面，我们用不同年期利率时间序列数据介绍如何使用Statsmodels 函数完成主成分分析。图 12 所示为2022 年8 个不同年期利率走势，也就是说数据有8 个特征 (维度)。

我们先看一下图 16 代码。

a 导入pandas_datareader。pandas_datareader 从多种数据源获取金融和经济数据，并将这些数据转换为 Pandas DataFrame 的形式。要想使用这个库，先需要安装。如b 所示，在Anaconda prompt 使用 pip install pandas_datareader 安装这个库。

c 从statsmodels.multivariate.pca 导入主成分分析函数pca。

d 利用pandas_datareader 从FRED (Federal Reserve Economic Data) 下载利率数据，数据格式为 Pandas 数据帧。

e 用dropna() 删除数据帧中NaN。f 用rename() 修改数据帧列标签。

g 用seaborn.lineplot() 绘制利率走势线图。

h 用pct_change() 计算日收益率。如图 13 所示，日收益率是用来衡量股票、利率在一天内的价格变动幅度的指标。日收益率通常以百分比形式表示，计算方法为：日收益率 = (当日收盘价 − 前一日收盘价) / 前一日收盘价 × 100%。日收益率数据X 是下文主成分分析对象。

i 用seaborn.pairplot() 绘制成对散点图，用来理解变量之间的关系和分布情况。对角线上的子图默认是每个变量的直方图，图 14 将对角线子图修改为概率密度估计线图，这是下一节要介绍的内容。非对角线上的图形是变量之间的散点图，图 14 仅仅保留了下三角部分子图。

j 计算日收益率数据X 相关性系数矩阵。k 用seaborn.heatmap() 可视化相关性系数矩阵。

如图 14 所示，从时间序列的涨跌，我们可以看到明显的联动性 (co-movement)。图 15 所示的相关性系数矩阵则“量化”联动性。主成分分析PCA 便可以帮助我们分析这种联动性。

Page 11  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Interest rate, % 2022-01 2022-03 2022-05 2022-07 2022-09 2022-11 2023-01

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr

图 12. 不同年期利率时间序列数据

Daily return, % 2023-01 2022-01 2022-03 2022-05 2022-07 2022-09 2022-11 0.3 0.2 0.1 0.0 0.1

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr

图 13. 不同年期利率日收益率时间序列数据

Page 12  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr 1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr 0.74 0.66 0.88 0.55 0.74 0.90 0.51 0.69 0.84 0.98 0.47 0.63 0.78 0.95 0.98 0.40 0.50 0.64 0.83 0.89 0.94 0.37 0.47 0.59 0.79 0.86 0.92 0.98

## 0.5 yr 1 yr

2 yr 5 yr 7 yr 10 yr 20 yr 1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr

图 14. 成对特征散点图，下三角

0.74 0.66 0.55 0.51 0.47 0.40 0.37 0.74 0.88 0.74 0.69 0.63 0.50 0.47 0.66 0.88 0.90 0.84 0.78 0.64 0.59 0.55 0.74 0.90 0.98 0.95 0.83 0.79 0.51 0.69 0.84 0.98 0.98 0.89 0.86 0.47 0.63 0.78 0.95 0.98 0.94 0.92 0.40 0.50 0.64 0.83 0.89 0.94 0.98 0.37 0.47 0.59 0.79 0.86 0.92 0.98

## 0.5 yr 1 yr

2 yr 5 yr 7 yr 10 yr 20 yr 30 yr

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr 1.0 0.9 0.8 0.7 0.6 0.5 0.4

图 15. 相关性系数矩阵

Page 13  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import numpy as np import matplotlib.pyplot as plt import pandas_datareader as pdr # pip install pandas_datareader import seaborn as sns import statsmodels.multivariate.pca as pca # 下载数据 df = pdr.data.DataReader(['DGS6MO','DGS1', 'DGS2','DGS5', 'DGS7','DGS10', 'DGS20','DGS30'], data_source='fred', start='01-01-2022', end='12-31-2022')

df = df.dropna()

# 修改数据帧列标签 df = df.rename(columns={'DGS6MO': '0.5 yr', 'DGS1': '1 yr', 'DGS2': '2 yr', 'DGS5': '5 yr', 'DGS7': '7 yr', 'DGS10': '10 yr', 'DGS20': '20 yr', 'DGS30': '30 yr'})

# 绘制利率走势 fig, ax = plt.subplots(figsize = (6,3))

sns.lineplot(df,markers=False,dashes=False, palette = "husl",ax = ax)

ax.legend(loc='lower right',ncol=3)

# 计算日收益率 X_df = df.pct_change()

X_df = X_df.dropna()

# 可视化收益率 fig, ax = plt.subplots(figsize = (6,3))

sns.lineplot(X_df,markers=False, dashes=False,palette = "husl",ax = ax)

ax.legend(loc='upper right',ncol=3)

# 成对特征散点图 sns.pairplot(X_df, corner=True, diag_kind="kde")

# 相关性系数矩阵 C = X_df.corr()

fig, ax = plt.subplots()

sns.heatmap(C, ax = ax, annot=True, cmap = 'RdYlBu_r', square = True)

a b h j g e f k

图 16. 下载分析利率数据，代码

图 17 所示的陡坡图 (scree plot) 是PCA 重要的可视化方案，用于帮助确定保留多少主成分。

首先，将原始数据进行主成分分析，计算出各个主成分及其对应的特征值，方差解释比例。

然后，将每个主成分的特征值绘制在一个陡坡图上 (图 17 左纵轴)。横轴表示主成分的序号，纵轴表示对应的特征值。

Page 14  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 通常，特征值会从大到小排列。观察陡坡图，寻找特征值开始急剧下降的拐点。这些拐点所对应的主成分通常是数据中最重要的部分，包含了最多的信息。拐点之后的主成分的贡献较小，可以考虑不予保留。

此外，我们还可以通过量化方法来决定保留主成分的数量。

图 17 右纵轴展示累积解释总方差百分比。我们可以发现，前3 个主成分解释超过95%的方差。这样做可以在保留重要信息的同时降低数据的维度。也就是说，利用主成分分析，我们可以把8 个维度降到 3 个维度，并尽可能保证数据的重要信息。

Cumulative ratio of explained variance (%)

Eigen value λ (PC variance)

Principal component, PCj

图 17. 陡坡图

在主成分分析中，载荷 (loadings) 是一个重要的概念，用于表示原始数据特征与各个主成分之间的线性关系。载荷反映了原始数据在每个主成分上的投影权重，从而帮助我们理解主成分的含义和解释。

具体来说，对于每个主成分，都有一组载荷值与之对应。图 18 所示为前3 主成分载荷。

这些载荷值构成了一个向量，表示了原始特征在主成分上的投影权重。载荷值可以为正或负，它们的绝对值越大，表示该主成分与对应特征之间的关系越强。

在PCA 的过程中，主成分的计算涉及到特征值分解数据的协方差矩阵Σ，Σ = VΛVT。从数学角度来看，载荷本质上就是V。

鸢尾花书《矩阵力量》第13、14 章将专门介绍特征值分解。

在主成分分析中，主成分得分 (principal component score) 是指原始数据在降维后的主成分空间中的投影值。如图 19 所示，主成分分数是在进行数据降维后，将原始数据点映射到新的主成分空间中的一种表示。

如图 20 所示，每个主成分都是原始特征的线性组合。大家可以自行计算所有主成分得分的相关性系数矩阵，容易发现这个矩阵为单位阵。

由于我们仅仅保留3 个主成分，图 20 便代表降维 (8 维到3 维) 过程。

注意，虽然主成分分析和线性回归都使用线性模型，但它们的目的和使用方式不同。

Page 15  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 主成分分析是用于降维的一种无监督学习方法，目的是找到一组新的变量，使得这些变量能够最大程度地解释原始数据中的方差。这些新的变量称为主成分，它们是原始数据中所有变量的线性组合。主成分分析通常用于数据探索和可视化，以及在高维数据中寻找最重要的特征。

而线性回归是用于预测的一种有监督学习方法，目的是通过拟合一个线性函数来预测一个连续的目标变量。线性回归通常用于建立输入变量和输出变量之间的关系，并用于预测新的输出变量值。

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr 0.4 0.2 0.0 0.2 0.4 0.6 PC1 PC2 PC3

图 18. 前三主成分载荷

0.2 0.1 0.0 0.1 0.2 0.3 0.4 Principal component scores 2023-01 2022-01 2022-03 2022-05 2022-07 2022-09 2022-11 PC1 PC2 PC3

图 19. 前三主成分得分

Page 16  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr PC1 PC2 PC3 Raw data Principal component scores Correlation Correlation PCA

图 20. 从原始数据到主成分得分

如图 21 所示，我们用三组主成分分析“还原”原始数据，得到的结果我们称之为还原数据。这个过程实际上将主成分分数反向投影到原始数据空间。

在PCA 中，我们通过将原始数据投影到主成分上得到主成分分数。而将主成分分数反向投影回原始数据空间，得到的数据就是还原数据 (approximated data)。

投影数据与原始数据的关系是，通过主成分分析的投影过程，将原始数据映射到主成分空间，并且反向投影过程可以近似地重构出原始数据。

然而，由于PCA 是一种降维技术，反向投影得到的数据会在重构过程中损失一些细节信息，因此反向投影出的数据可能与原始数据存在差异。图 22 和图 23 分别用散点图、线图可视化原始数据、还原数据、误差。

接着图 16 代码，图 24 代码完成主成分分析。

a 利用statsmodels.multivariate.pca.PCA() 完成主成分分析。

Page 17  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 下面简单介绍这个函数的关键参数。ncomp 指定返回主成分数量，默认返回和原数据特征数一致的主成分数量。standardize 指定是否标准化数据，如果 standardize = True 相当于对原始数据相关性系数矩阵进行特征值分解，来完成主成分分析运算。demean 指定是否去均值，如果standardize = True，默认数据已经去均值。method = 'svd' (默认) 代表利用奇异值分解进行主成分分解，method = 'eig' 代表利用特征值分解完成PCA。

b 提取特征值，从大到小排列。特征值分解将协方差矩阵转化为一组特征向量和特征值。这些特征值排列从大到小的意义在于决定了主成分的重要性和解释力。

主成分分析的目标之一是将原始数据映射到一组新的主成分上，这些主成分按照重要性递减排列。

换句话说，通过选择前几个特征值较大的主成分，我们能够保留大部分原始数据的方差信息，同时实现数据的降维。这有助于更好地理解数据的结构、模式。

c 增加双y 轴的右侧纵轴对象。

d 提取前3 主成分。从特征值分解结果来看，这三个主成分对应的特征值分别约为1537、288、 95。三者之和占总特征值超过95%。

e 用前3 主成分创建还原数据。

## 0.5 yr

1 yr 2 yr 5 yr 7 yr 10 yr 20 yr 30 yr Approximated data PC1 PC2 PC3 Scores Project

图 21. 从主成分得分 (前3 个主成分) 到还原数据

Page 18  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Approximated Original (a) 0.5 yr Approximated Original (c) 2 yr Approximated Original (e) 7 yr Approximated Original (g) 20 yr Approximated Original (b) 1 yr Approximated Original (d) 5 yr Approximated Original (f) 10 yr Approximated Original (h) 30 yr

图 22. 比较原始数据和还原数据 (前三主成分还原)，散点图

Page 19  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Date Data (a) 0.5 yr Date Data (c) 2 yr Date Data (e) 7 yr Date Data (g) 20 yr Date Data (b) 1 yr Date Data (d) 5 yr Date Data (f) 10 yr Date Data (h) 30 yr Original Approximated Error

图 23. 比较原始数据和还原数据 (前三主成分还原)，线图

Page 20  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 主成分分析 pca_model = pca.PCA(X_df, standardize=True)

variance_V = pca_model.eigenvals # 计算主成分的方差解释比例 explained_var_ratio = variance_V / variance_V.sum()

PC_range = np.arange(len(variance_V)) + 1 labels = ['$PC_' + str(index) + '$' for index in PC_range]

# 陡坡图 fig, ax1 = plt.subplots(figsize = (6,3))

ax1.plot(PC_range, variance_V, 'b', marker = 'x')

ax1.set_xlabel('Principal Component')

ax1.set_ylabel('Eigen value $\lambda$ (PC variance)', color='b')

ax1.set_ylim(0,1600); ax1.set_xticks(PC_range)

ax2 = ax1.twinx()

ax2.plot(PC_range, np.cumsum(explained_var_ratio)*100, 'r', marker = 'x')

ax2.set_ylabel('Cumulative ratio of explained variance (%)', color='r')

ax2.set_ylim(20,100)

ax2.set_xlim(PC_range.min() - 0.1,PC_range.max() + 0.1)

# PCA载荷 loadings= pca_model.loadings[['comp_0','comp_1','comp_2']]

fig, ax = plt.subplots(figsize = (6,4))

sns.lineplot(data=loadings, markers=True, dashes=False, palette = "husl")

plt.axhline(y=0, color='r', linestyle='-')

# 用前3主成分获得还原数据 X_df_ = pca_model.project(3)

# 比较原始数据和还原数据 # 线图 fig, axes = plt.subplots(4,2,figsize=(4,8))

axes = axes.flatten()

for col_idx, ax_idx in zip(list(X_df_.columns),axes): sns.lineplot(X_df_[col_idx],ax = ax_idx)

sns.lineplot(X_df[col_idx],ax = ax_idx)

sns.lineplot(X_df[col_idx] - X_df_[col_idx], c = 'k', ax = ax_idx)

ax_idx.set_xticks([]); ax_idx.set_yticks([])

ax_idx.axhline(y = 0, c = 'k')

# 散点图 fig, axes = plt.subplots(4,2,figsize=(4,8))

axes = axes.flatten()

for col_idx, ax_idx in zip(list(X_df_.columns),axes): sns.scatterplot(x = X_df_[col_idx], y = X_df[col_idx], ax = ax_idx)

ax_idx.plot([-0.3, 0.3],[-0.3, 0.3],c = 'r')

ax_idx.set_aspect('equal', adjustable='box')

ax_idx.set_xticks([]); ax_idx.set_yticks([])

ax_idx.set_xlim(-0.3, 0.3); ax_idx.set_ylim(-0.3, 0.3)

a b e

图 24. 主成分分析，使用时需要配合前文代码

Page 21  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 27.5 概率密度估计：高斯KDE

本书第12 章介绍过如何用Seaborn 可视化高斯核密度估计结果。对于一元随机变量，高斯核密度通过在数据点附近生成高斯分布的核函数，然后将所有核函数叠加在一起得到一条曲线；这条曲线就是概率密度函数 (Probability Density Function, PDF)，用来描述样本数据的分布情况。

这一节聊一聊如何用Statsmodels 库函数完成高斯KDE，并可视化一元、二元概率密度函数。

图 25 所示为用高斯KDE 估计得到的鸢尾花花萼长度概率密度函数。图 25 曲线和横轴包围的面积为 1。图 26、图 27、图 28 所示为考虑鸢尾花标签的花萼长度概率密度函数。

4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length, X1 1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0 PDF

图 25. 鸢尾花数据花萼长度概率密度函数，基于高斯KDE

4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length, X1 1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0 PDF

图 26. 花萼长度X1概率密度函数，基于高斯KDE，考虑标签，'species' == 'setosa'

4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length, X1 1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0 PDF

Page 22  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 27. 花萼长度X1概率密度函数，基于高斯KDE，考虑标签，'species' == 'versicolor' 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 Sepal length, X1 1.4 1.2 1.0 0.8 0.6 0.4 0.2 0.0 PDF

图 28. 花萼长度X1概率密度函数，基于高斯KDE，考虑标签，'species' == 'virginica'

图 29 所示为绘制图 25 ~ 图 28 的代码。下面聊一聊代码中的主要语句。

a 导入statsmodels 中的api (全称为application programming interface) 模块。在statsmodels 中，api 包含了用户常用的函数、类和工具，用于执行各种统计分析和建模任务。

b 从sklearn.datasets 导入load_iris。c 用load_iris() 导入鸢尾花数据集。d 提取标签，这个数据集的标签为0、1、2，分别对应'setosa'、'versicolor'、'virginica'。e 将NumPy 数组转化为Pandas 数据帧。

f 用iloc[] 提取数据帧的第0 列。

g 创建自定义可视化函数。

h 中fill_between() 是 Matplotlib 库中的一个函数，用于在两条曲线之间填充颜色。

i 导入非参数核密度估计sm.nonparametric.KDEUnivariate() 函数，用来创建和操作单变量数据的核密度估计对象。这个函数的输入为样本的单一变量数据。

j 调用 fit() 方法计算核密度估计，其中bw 调节核函数带宽 (band width)。

k 利用evaluate() 计算给定数组核密度估计值，以便后续可视化。

l 用自定义函数visualize() 绘制概率密度函数曲线，'#00448A'为一个十六进制颜色值 RGB 颜色值。在十六进制颜色表示法中，颜色值由六个字符组成，前两个字符表示红色分量、中间两个字符表示绿色分量，最后两个字符表示蓝色分量。每个字符可以取值从 00 到 FF，对应十进制的 0 到 255。在颜色 #00448A 中：前两个字符 00 表示红色分量为 0；中间两个字符 44 表示绿色分量为 68；最后两个字符 8A 表示蓝色分量为 138。

m 创建高斯KDE 对象时考虑鸢尾花分类。

图 31 ~ 图 35 所示为联合概率密度估计结果。

Page 23  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import statsmodels.api as sm import matplotlib.pyplot as plt import pandas as pd from sklearn.datasets import load_iris # 从Scikit-Learn库加载鸢尾花数据 iris = load_iris()

y = iris.target X_df = pd.DataFrame(iris.data)

X1_df = X_df.iloc[:,0]

# 自定义可视化函数 def visualize(x1,pdf,color): fig, ax = plt.subplots(figsize = (8,3))

ax.fill_between(x1, pdf, facecolor = color,alpha = 0.2)

ax.plot(x1, pdf,color = color)

ax.set_ylim([0,1.4])

ax.set_xlim([4,8])

ax.set_ylabel('PDF')

ax.set_xlabel('Sepal length, $x_1$')

# 不考虑标签 KDE = sm.nonparametric.KDEUnivariate(X1_df)

KDE.fit(bw=0.1)

x1 = np.linspace(4,8,101)

f_x1 = KDE.evaluate(x1)

visualize(x1,f_x1,'#00448A')

# 考虑鸢尾花标签，用KDE描述样本数据花萼长度分布 colors = ['#FF3300','#0099FF','#8A8A8A']

x1 = np.linspace(4,8,161)

for idx in range(3): KDE_C_i = sm.nonparametric.KDEUnivariate(X1_df[y==idx])

KDE_C_i.fit(bw=0.1)

f_x1_given_C_i = KDE_C_i.evaluate(x1)

visualize(x1,f_x1_given_C_i,colors[idx])

a b e f h g j k

图 29. 一元概率密度估计，代码

SciPy 也有完成概率密度估计的函数。

Page 24  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import matplotlib.pyplot as plt # 定义可视化函数 def plot_surface(xx1, xx2, surface, x1_s, x2_s, z_height, color, title_txt): fig = plt.figure(figsize=(8,3))

ax = fig.add_subplot(1, 2, 1, projection='3d')

ax.plot_wireframe(xx1, xx2, surface, cstride = 8, rstride = 8, color = [0.7,0.7,0.7], linewidth = 0.25)

ax.scatter(x1_s, x2_s, x2_s*0, c=color)

ax.contour(xx1, xx2, surface,20, cmap = 'RdYlBu_r')

ax.set_proj_type('ortho')

ax.set_xlabel('Sepal length, $x_1$')

ax.set_ylabel('Sepal width, $x_2$')

ax.set_zlabel('PDF')

ax.set_xticks([]); ax.set_yticks([])

ax.set_zticks([])

ax.set_xlim(x1.min(), x1.max())

ax.set_ylim(x2.min(), x2.max())

ax.set_zlim([0,z_height])

ax.view_init(azim=-120, elev=30)

ax.set_title(title_txt)

ax.grid(False)

ax = fig.add_subplot(1, 2, 2)

ax.contourf(xx1, xx2, surface, 12, cmap='RdYlBu_r')

ax.contour(xx1, xx2, surface, 12, colors='w')

ax.set_xticks([]); ax.set_yticks([])

ax.set_xlim(x1.min(), x1.max())

ax.set_ylim(x2.min(), x2.max())

ax.set_xlabel('Sepal length, $x_1$')

ax.set_ylabel('Sepal width, $x_2$')

ax.set_aspect('equal', adjustable='box')

ax.set_title(title_txt)

a b e f h g

图 30. 定义可视化函数

Page 25  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length, X1 PDF Sepal width, X2

图 31. 花萼长度、花萼宽度 (X1, X2) 联合概率密度函数，基于高斯KDE

import numpy as np import statsmodels.api as sm import pandas as pd from sklearn.datasets import load_iris import scipy.stats as st # 导入鸢尾花数据 iris = load_iris()

X_1_to_4 = iris.data; y = iris.target feature_names = ['Sepal length, $X_1$','Sepal width, $X_2$', 'Petal length, $X_3$','Petal width, $X_4$']

X_df = pd.DataFrame(X_1_to_4)

X1_2_df = X_df.iloc[:,[0,1]]

x1 = np.linspace(4,8,161); x2 = np.linspace(1,5,161)

xx1, xx2 = np.meshgrid(x1,x2)

positions = np.vstack([xx1.ravel(), xx2.ravel()])

colors = ['#FF3300','#0099FF','#8A8A8A']

KDE = st.gaussian_kde(X1_2_df.values.T)

f_x1_x2 = np.reshape(KDE(positions).T, xx1.shape)

x1_s = X1_2_df.iloc[:,0]

x2_s = X1_2_df.iloc[:,1]

z_height = 0.5 title_txt = '$f_{X1, X2}(x_1, x_2)$, evidence' plot_surface(xx1, xx2, f_x1_x2, x1_s, x2_s, z_height, '#00448A', title_txt)

a b e

图 32. 可视化证据因子

Page 26  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length, X1 PDF Sepal width, X2

图 33. 花萼长度、花萼宽度 (X1, X2) 联合概率密度函数，基于高斯KDE，考虑标签，'species' == 'setosa'

Sepal length, X1 PDF Sepal width, X2

图 34. 花萼长度、花萼宽度 (X1, X2) 联合概率密度函数，基于高斯KDE，考虑标签，'species' == 'versicolor'

Sepal length, X1 PDF Sepal width, X2

图 35. 花萼长度、花萼宽度 (X1, X2) 联合概率密度函数，基于高斯KDE，考虑标签，'species' == 'virginica'

Page 27  |  Chapter 27 Statsmodels 统计模型  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 考虑不同鸢尾花分类 for idx in range(3): KDE_idx = st.gaussian_kde(X1_2_df[y==idx].values.T)

f_x1_x2_given_C_i = np.reshape(KDE_idx(positions).T, xx1.shape)

x1_s_C_i = X1_2_df.iloc[:,0][y==idx]

x2_s_C_i = X1_2_df.iloc[:,1][y==idx]

z_height = 1 title_txt = 'Likelihood' plot_surface(xx1, xx2, f_x1_x2_given_C_i, x1_s_C_i, x2_s_C_i, z_height, colors[idx], title_txt)

a b

图 36. 可视化似然函数

Page 1  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Machine Learning in Scikit-Learn Scikit-Learn 机器学习利用Scikit-Learn 库完成回归、降维、分类、聚类

合理即存在，存在即合理。

What is rational is actual and what is actual is rational.

—— 黑格尔 (Hegel)  |  德国哲学家  |  1770 ~ 1831

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

## XXXXX

◄

Page 2  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 28.1 什么是机器学习?

人工智能、机器学习、深度学习、自然语言处理人工智能的外延十分宽泛，泛指指计算机系统通过模拟人的思维和行为，实现类似于人的智能行为。人工智能领域包含了很多技术和方法，如机器学习、深度学习、自然语言处理、计算机视觉等。

机器学习 (Machine Learning，ML) 是人工智能 (Artificial Intelligence，AI) 的一个子领域，是通过计算机算法自动地从数据中学习规律，并用所学到的规律对新数据进行预测或者分类的过程。本书这个板块将会着重介绍Python 中Scikit-Learn 这个机器学习工具。

深度学习是一种机器学习的子领域，它是通过建立多层神经网络模型，自动地从原始数据中学习到更高级别的特征和表示，从而实现对复杂模式的建模和预测。Python 中常用的深度学习工具有 TensorFlow、PyTorch、Keras 等，这些工具不在本书讨论范围内。

自然语言处理 (Natural Language Processing, NLP) 是计算机科学与人工智能领域的一个重要分支，旨在通过计算机技术对人类语言进行分析、理解和生成。自然语言处理主要应用于自然语言文本的处理和分析，如文本分类、情感分析、信息抽取、机器翻译、问答系统等。

Deep learning Machine learning Artificial intelligence

图 1. 人工智能、机器学习、深度学习机器学习适合处理的问题有如下特征：(a) 大数据；(b) 黑箱或复杂系统，难以找到控制方程 (governing equations)。机器学习需要通过数据的训练。

机器学习分类如图 2 所示，简单来说，机器学习可以分为以下两大类： ◄ 有监督学习 (supervised learning)，也叫监督学习，训练有标签值样本数据并得到模型，通过模型对新样本进行推断。有监督学习可以进一步分为两大类：回归 (regression)，分类 (classification)。本书

## 第30 章介绍常用回归算法，第32 章介绍常用分类算法。

Page 3  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ◄ 无监督学习 (unsupervised learning)训练没有标签值的数据，并发现样本数据的结构和分布。无监督学习可以分类两大类：降维 (dimensionality reduction)、聚类 (clustering)。本书第31 章介绍常用降维算法，第32 章介绍常用聚类算法。

Machine learning Unsupervised learning Supervised learning Regression Classification Dimensionality reduction Clustering

图 2. 机器学习分类 Regression Classification Linear regression Nonlinear regression Ensemble methods Decision trees Neural network Support vector machine Naïve Bayes k-nearest neighbors Discriminant analysis

图 3. 监督学习常见方法

Clustering k-means k-medoids Fuzzy C-means Hierarchical

## DBSCAN

Neutral network Gaussian mixture model Spectral clustering Hidden Markov model

图 4. 常用聚类方法

Page 4  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

机器学习流程图 5 所示为机器学习的一般流程。

Input data Black box Real world Original data Processed data Training set Collect data Process data Validation set Machine learning Learning Evaluation Trained model Yes, deploy Validat e Feature extraction Feature selection Monitor Predict Test set Model selection Pass?

No Evaluate Tune parameters Feature engineering

图 5. 机器学习一般流程

具体分步流程通常包括以下步骤： ◄ 收集数据：从数据源获取数据集，这可能包括数据清理、去除无效数据和处理缺失值等。

◄ 特征工程：对数据进行预处理，包括数据转换、特征选择、特征提取和特征缩放等。

◄ 数据划分：将数据集划分为训练集、验证集和测试集等。训练集用于训练模型，验证集用于选择模型并进行调参，测试集用于评估模型的性能。

◄ 选择模型：选择合适的模型，例如线性回归、决策树、神经网络等。

◄ 训练模型：使用训练集对模型进行训练，并对模型进行评估，可以使用交叉验证等方法进行模型选择和调优。

Page 5  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com ◄ 测试模型：使用测试集评估模型的性能，并进行模型的调整和改进。

◄ 应用模型：将模型应用到新数据中进行预测或分类等任务。

◄ 模型监控：监控模型在实际应用中的性能，并进行调整和改进。

以上是机器学习的一般分步流程，不同的任务和应用场景可能会有一些变化和调整。在实际应用中，还需要考虑数据的质量、模型的可解释性、模型的复杂度和可扩展性等问题。

## 28.2 有标签数据、无标签数据

根据输出值有无标签，如图 6 所示，数据可以分为有标签数据 (labelled data) 和无标签数据 (unlabelled data)。鸢尾花数据显然是有标签数据。删去鸢尾花最后一列标签，我们便得到无标签数据。

有标签数据和无标签数据是机器学习中常见的两种数据类型，它们在不同的应用场景中有不同的用途。

简单来说，有标签数据对应有监督学习，无标签数据对应无监督学习。

X y Input variables or features Unobserved Unsupervised learning NaN Unlabeled X y Input variables or features Response variable Supervised learning Labeled X y Input variables or features Mixed Semi-supervised learning Labeled NaN Unlabeled

图 6. 根据有无标签分类数据

有监督学习中，如果标签为连续数据，对应的问题为回归 (regression)，如图 7 (a)。如果标签为分类数据，对应的的问题则是分类 (classification)，如图 7 (c)。

无监督学习中，样本数据没有标签。如果目标是寻找规律、简化数据，这类问题叫做降维 (dimensionality reduction)，比如主成分分析目的之一就是找到数据中占据主导地位的成分，如图 7 (b)。

如果模型的目标是根据数据特征将样本数据分成不同的组别，这种问题叫做聚类 (clustering)，如图 7 (b)。

Page 6  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Clustering Classification Regression Dimension reduction (a)

(b)

(c)

(d)

Quantitative Categorical Unsupervised learning Supervised learning

图 7. 根据数据是否有标签、标签类型细分机器学习算法

## 28.3 回归

回归是机器学习中一种常见的任务，用于预测一个连续变量的值。常见的回归算法包括线性回归、 非线性回归、正则化、贝叶斯回归和基于分类算法的回归。

线性回归 (linear regression) 通过构建一个线性模型来预测目标变量。最简单的线性回归算法是一元线性回归，多元线性回归则是利用多个特征来预测目标变量。

非线性回归 (nonlinear regression) 目标变量与特征之间的关系不是线性的。多项式回归 (polynomial regression) 是非线性回归的一种形式，通过将特征的幂次作为新的特征来构建一个多项式模型。逻辑回归 (logistic regression) 既是一种二分类算法，可以用于非线性回归。

正则化 (regularization) 正则化通过向目标函数中添加惩罚项来避免模型的过拟合。常用的正则化方法有岭回归、Lasso 回归、弹性网络回归。岭回归通过向目标函数中添加 L2 惩罚项来控制模型复杂度。

Lasso 回归通过向目标函数中添加 L1 惩罚项，它不仅能够控制模型复杂度，还可以进行特征选择。弹性网络是岭回归和Lasso 回归的结合体，它同时使用 L1 和 L2 惩罚项。

贝叶斯回归 (Bayesian regression) 是一种基于贝叶斯定理的回归算法，它可以用来估计连续变量的概率分布。

基于分类算法的回归，比如kNN 算法是一种基于距离度量的分类算法，但也可以用于回归任务。支持向量回归 (Support Vector Regression, SVR) 则是一种基于支持向量机 (Support Vector Machine, SVM) 的回归算法，它通过寻找一个最优的边界，来预测目标变量。

Page 7  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 8 比较线性回归、多项式回归、逻辑回归三种回归算法。

(a)

(b)

(c)

y y y

图 8. 比较回归算法，线性回归、多项式回归、逻辑回归

## 28.4 降维

降维是指将高维数据转换为低维数据的过程，这个过程可以提取出数据的主要特征，并去除噪声和冗余信息。降维可以有效地减少计算成本，加速模型训练和预测，并提高模型的准确性和可解释性。

以下是机器学习中常用的降维算法： 主成分分析 (Principal Component Analysis, PCA) 通过线性变换将高维数据映射到低维空间。利用特征值分解、奇异值分解都可以完成主成分分析。

核主成分分析 (Kernel Principal Component Analysis, KPCA) 是一种非线性降维算法，它使用核函数将数据映射到高维空间，然后使用PCA 在新的空间中进行降维。

典型相关分析 (Canonical Correlation Analysis, CCA) 是一种统计学习算法，它通过最大化两个变量之间的相关性来降低维度。

流形学习 (Manifold Learning) 是一种非线性降维算法，它通过保持局部结构的连续性来将高维数据映射到低维空间。流形学习可以发现数据中的非线性关系和流形结构。

这些降维算法都有不同的优点和适用场景，根据数据的特点和需求选择适合的算法进行建模。

## 28.5 分类

在机器学习中，分类是指根据给定的数据集，通过对样本数据的学习，建立分类模型来对新的数据进行分类的过程。下面简述一些常用的分类算法。

最近邻算法 (KNN)：基于样本的特征向量之间的距离进行分类预测，即找到与待分类数据距离最近的 K 个样本，根据它们的类别进行投票决策。

朴素贝叶斯算法 (Naive Bayes)：利用贝叶斯定理计算样本属于某个类别的概率，并根据概率大小进行分类决策。

Page 8  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 支持向量机 (SVM)：利用间隔最大化的思想来进行分类决策，可以通过核函数将低维空间中线性不可分的样本映射到高维空间进行分类。

决策树算法 (Decision Tree)：通过对样本数据的特征进行划分，构建一个树形结构，从而实现对新数据的分类预测。

我们可以通过比较决策边界的形状大致知道采用的是哪一种分类算法，图 9 给出四个例子。本书第 30 章将专门介绍几种分类算法。

(a)

(b)

(c)

(d)

图 9. 比较分类算法决策边界，最近邻、朴素贝叶斯、支持向量机、决策树

## 28.6 聚类

在机器学习中，聚类是指将数据集中的样本按照某种相似性指标进行分组的过程。常用的聚类算法包括。

k 均值算法 (kMeans)：将样本分为 k 个簇，每个簇的中心点是该簇中所有样本点的平均值。

高斯混合模型 (Gaussian Mixture Model, GMM)：将样本分为多个高斯分布，每个高斯分布对应一个簇，采用 EM 算法进行迭代优化。

层次聚类算法 (Hierarchical Clustering) 将样本分为多个簇，可以使用自底向上的凝聚层次聚类或自顶向下的分裂层次聚类。

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) 是基于密度的聚类算法，可以自动发现任意形状的簇。

Page 9  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 谱聚类算法 (Spectral Clustering) 是基于样本之间的相似度来构造拉普拉斯矩阵，然后对其进行特征值分解来实现聚类。

图 10 比较四种k 均值、高斯混合模型、DBSCAN、谱聚类算法结果。

(a)

(b)

(c)

(d)

图 10. 比较聚类算法，k 均值、高斯混合模型、DBSCAN、谱聚类

## 28.7 什么是Scikit-Learn?

Scikit-learn 是一个流行的 Python 机器学习库，提供完成机器学习任务各种工具。Scikit-learn 和前文介绍的NumPy、SciPy、Pandas、Matplotlib 等重要工具联系紧密。

以下是 Scikit-learn 中的主要工具： 数据集：Scikit-learn 中包含多个标准数据集，还提供生成样本数据的函数。这些数据集可以用于测试和评估机器学习模型的性能。

数据预处理 (data preprocessing)。数据预处理是机器学习的重要一步，它包括数据清洗、数据重构和数据变换。Scikit-learn 提供了各种数据预处理工具，包括特征缩放、归一化、标准化、处理缺失值、 数据编码等。Scikit-Learn 数据本书下一章 (第29 章) 要探讨的话题。

监督学习模型：Scikit-learn 支持多种监督学习模型，包括线性回归、逻辑回归、支持向量机、决策树、随机森林、神经网络等。

无监督学习模型：Scikit-learn 支持多种无监督学习模型，包括聚类、降维、密度估计等。这些模型可以用于在没有标签的情况下对数据进行分析和理解。

Page 10  |  Chapter 28 Scikit-Learn 机器学习  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 模型选择和评估：Scikit-learn 提供了各种工具，用于选择最佳模型和评估模型的性能。这些工具包括交叉验证、网格搜索、评估指标等。

管道：Scikit-learn 中的管道工具可用于将数据预处理和模型训练流程组合在一起，使得处理和训练过程更加高效和简单。

总的来说，scikit-learn 提供了一个全面的机器学习工具包，使得机器学习的建模和评估过程更加高效和方便。

Page 1  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Data and Data Preprocessing in Scikit-Learn Scikit-Learn 数据数据集、缺失值、离群值、特征缩放 …

三种激情，简单却无比强烈，支配着我的生活：对爱的渴望、对知识的追求以及对人类苦难的无法忍受的怜悯。这些激情，如狂风，将我吹来吹去，任性地，越过痛苦的深海，到了绝望的边缘。

Three passions, simple but overwhelmingly strong, have governed my life: the longing for love, the search for knowledge, and unbearable pity for the suffering of mankind. These passions, like great winds, have blown me hither and thither, in a wayward course, over a deep ocean of anguish, reaching to the very verge of despair.

—— 伯特兰·罗素 (Bertrand Russell)  |  英国哲学家、数学家  |  1872 ~ 1970

◄ sklearn.covariance.EllipticEnvelope() 使用基于高斯分布的椭圆包络方法检测异常值 ◄ sklearn.covariance.mahalanobis() 计算马哈拉诺比斯距离来检测异常值 ◄ sklearn.covariance.RobustCovariance() 使用鲁棒协方差估计进行异常值检测 ◄ sklearn.datasets.fetch_lfw_people() 人脸数据集 ◄ sklearn.datasets.fetch_olivetti_faces() 奥利维蒂人脸数据集 ◄ sklearn.datasets.load_boston() 波士顿房价数据集 ◄ sklearn.datasets.load_breast_cancer() 乳腺癌数据集 ◄ sklearn.datasets.load_diabetes() 糖尿病数据集 ◄ sklearn.datasets.load_digits() 手写数字数据集 ◄ sklearn.datasets.load_iris() 鸢尾花数据集 ◄ sklearn.datasets.load_linnerud() Linnerud 体能训练数据集 ◄ sklearn.datasets.load_wine() 葡萄酒数据集 ◄ sklearn.datasets.make_blobs() 生成聚类数据集 ◄ sklearn.datasets.make_circles() 生成圆环形状数据集 ◄ sklearn.datasets.make_classification() 生成合成的分类数据集 ◄ sklearn.datasets.make_moons() 生成月牙形状数据集 ◄ sklearn.datasets.make_regression() 生成合成的回归数据集 ◄ sklearn.ensemble.IsolationForest() 使用隔离森林方法检测异常值 ◄ sklearn.impute.IterativeImputer() 使用多个回归模型来估计缺失值 ◄ sklearn.impute.KNNImputer() 使用最近邻样本的值来进行插补 ◄ sklearn.impute.SimpleImputer() 提供了一些基本的插补策略来处理缺失值 ◄ sklearn.neighbors.LocalOutlierFactor() 使用局部离群因子方法检测异常值 ◄ sklearn.preprocessing.MaxAbsScaler() 通过除以每个特征的“最大绝对值”完成特征缩放 ◄ sklearn.preprocessing.MinMaxScaler() 通过除以每个特征的“最大值减最小值”完成特征缩放 ◄ sklearn.preprocessing.PowerTransformer() 对特征应用幂变换来使数据更加服从高斯分布 ◄ sklearn.preprocessing.QuantileTransformer() 将特征转换为均匀分布 ◄ sklearn.preprocessing.RobustScaler() 通过减去中位数并除以IQR 来对特征进行缩放 ◄ sklearn.preprocessing.StandardScaler() 标准化特征缩放 ◄ sklearn.svm.OneClassSVM() 使用支持向量机方法进行单类异常值检测

Page 2  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 29.1 Scikit-Learn 中有关数据的工具

除了完成监督学习、无监督学习之外，Scikit-Learn 还提供了丰富的样本数据集、样本数据生成函数和数据处理方法，用于实现机器学习算法的训练、评估和预测。本章主要介绍如下内容。

► 样本数据集。Scikit-Learn 的样本数据集包含在sklearn.datasets 模块中，比如 sklearn.datasets.load_iris() 可以用来加载鸢尾花数据集。

► 生成样本数据。Scikit-Learn 还提供数据集生成函数，比如 sklearn.datasets.make_blobs()、 sklearn.datasets.make_classification()。

► 特征工程。Scikit-Learn 还提供处理缺失值、处理离群值、特征缩放、数据分割等数据特征工程工具。

► 数据分割。将样本数据划分为训练集和测试集。

## 29.2 样本数据集

表 1 所示为Scikit-Learn 中常用数据集。

表 1. Scikit-Learn 常用数据集函数介绍 sklearn.datasets.load_boston()

波士顿房价数据集，包含506 个样本，每个样本有13 个特征，常用于回归任务。

sklearn.datasets.load_iris()

鸢尾花数据集，包含150 个样本，每个样本有4 个特征，常用于分类任务。

sklearn.datasets.load_diabetes()

糖尿病数据集，包含442 个样本，每个样本有10 个特征，常用于回归任务。

sklearn.datasets.load_digits()

手写数字数据集，包含1797 个样本，每个样本是一个8x8 像素的图像，常用于分类任务。

sklearn.datasets.load_linnerud()

Linnerud 体能训练数据集，包含20 个样本，每个样本有3 个特征，常用于多重输出回归任务。

sklearn.datasets.load_wine()

葡萄酒数据集，包含178 个样本，每个样本有13 个特征，常用于分类任务。

sklearn.datasets.load_breast_cancer()

乳腺癌数据集，包含569 个样本，每个样本有30 个特征，常用于分类任务。

sklearn.datasets.fetch_olivetti_faces()

奥利维蒂人脸数据集，包含400 张64x64 像素的人脸图像，常用于人脸识别任务。

sklearn.datasets.fetch_lfw_people()

人脸数据集，包含13233 张人脸图像，常用于人脸识别和验证任务。

图 1 展示导入Scikit-Learn 鸢尾花数据所用代码，下面讲解其中关键语句。

a 从sklearn.datasets 模块导入load_iris。

b 导入鸢尾花样本数据集对象，将其命名为iris。

注意，导入数据时，如果采用X, y = load_iris(as_frame=True, return_X_y=True)，返回的X 为Pandas DataFrame，y 为Pandas Series。请大家自己练习使用这个语句。

c 通过iris.data 提取鸢尾花数据集的4 个特征，结果为NumPy 数组。

d 通过iris.feature_names 提取鸢尾花4 个特征名称，结果为 ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']。

Page 3  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com e 通过iris.target 提取鸢尾花数据集的标签，结果也是NumPy 数组。

f 利用numpy.unique() 返回独特标签值——0、1、2。

g 利用iris.target_names 提取鸢尾花问题标签，结果为 ['setosa', 'versicolor', 'virginica']。

h 将鸢尾花前4 个特征NumPy 数组创建成Pandas 数据帧。i 用describe() 对数据帧做统计汇总， 结果如表 2 所示。

from sklearn.datasets import load_iris import numpy as np import pandas as pd # 导入鸢尾花数据 iris = load_iris()

# 鸢尾花数据前4个特征，NumPy数组 X = iris.data print(iris.feature_names)

# 鸢尾花数据标签：0、1、2 y = iris.target print(np.unique(y))

# 鸢尾花文字标签 print(iris.target_names)

# 创建数据帧 X_df = pd.DataFrame(X, columns = ['X1','X2','X3','X4'])

round(X_df.describe(),2)

b a e g h f iris.data iris.target

## X1 X2 X3 X4

图 1. 导入Scikit-Learn 中鸢尾花数据

表 2. 鸢尾花数据集的统计总结

X1, sepal length (cm) X2, sepal width (cm) X3, petal length (cm) X4, petal width (cm)

count mean 5.84 3.06 3.76 1.20 std 0.83 0.44 1.77 0.76 min 4.30 2.00 1.00 0.10 25% 5.10 2.80 1.60 0.30 50% 5.80 3.00 4.35 1.30 75% 6.40 3.30 5.10 1.80 max 7.90 4.40 6.90 2.50

## 29.3 生成数据

表 3 总结Scikit-Learn 中常用来生成样本数据集的函数。图 2 所示为表 3 中一些函数生成的样本数据集。图中颜色代表不同分类标签。图 4 为对应代码，下面介绍其中重要语句。

表 3. Scikit-Learn 中常用来生成样本数据集函数

Page 4  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com sklearn.datasets.make_regression()

生成合成的回归数据集，下一章将会用到这个函数。

sklearn.datasets.make_classification()

生成合成的分类数据集，可以指定样本数、特征数、类别数等。

sklearn.datasets.make_blobs()

生成聚类数据集，可以指定样本数、特征数、簇数等 sklearn.datasets.make_moons()

生成月牙形状数据集 sklearn.datasets.make_circles()

生成圆环形状数据集

(a)

(b)

(c)

(d)

(e)

(f)

图 2. 生成样本数据集，有标签 a 从sklearn.preprocessing 模块导入StandardScaler()。StandardScaler()是scikit-learn 中的一个预处理类，用于在机器学习流程中对数据进行标准化处理。标准化是数据预处理的一种常见方式，目的是将数据的特征值缩放成均值为0，标准差为1 的分布，即计算Z 分数，以消除不同特征之间的尺度差异。本章后文将介绍更多预处理方法。

b 中sklearn.datasets.make_circles() 生成环形数据集的函数，结果如图 2 (a) 所示。数据点位于两个同心圆上，可以用于测试机器学习算法。参数n_samples 设定数据点数量，默认为100。参数noise 为添加到数据中的高斯噪声的标准差。参数factor 为内外圆之间的比例因子。factor 取值在0 到1 之间，0.0 表示两个圆重叠，1.0 表示完全分离的两个圆。

c 中sklearn.datasets.make_moons() 用于生成月牙形状的数据集，结果如图 2 (b) 所示。这个函数可以用于测试在非线性数据上表现良好的算法。参数n_samples 指定生成的数据点数量。参数noise 指定添加到数据中的高斯噪声的标准差。

d 中sklearn.datasets.make_blobs() 生成一个由多个高斯分布组成的数据集，结果如图 2 (c) 所示。参数n_samples 为生成的样本数。参数n_features 为每个样本的特征数。参数centers 是要生成的数据的质心数量，或高斯分布质心的具体位置。参数cluster_std 为每个聚类的标准差，用于控制每个聚类中数据点的分布紧密程度。

e 对sklearn.datasets.make_blobs() 生成的数据集进行几何变换 (缩放 + 旋转)，结果如图 2 (d) 所示。

大家要是想知道具体的几何变换，需要采用特征值分解。

f 在利用sklearn.datasets.make_blobs() 时，每个高斯分布指定不同的标准差，结果如图 2 (e) 所示。

Page 5  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com g 中sklearn.datasets.make_classification() 生成一个虚拟的分类数据集，可以用于测试和演示分类算法，结果如图 2 (f) 所示。

h 采用2 行3 列子图布局可视化上述样本数据集。

i 利用前文导入的StandardScaler() 对X 标准化。标准化是特征缩放的一种。在机器学习中，特征缩放是一个重要的预处理步骤，其目的是为了在不同特征之间建立更好的平衡，以便模型能够更好地进行学习和预测。

注意，标准化仅仅是对单一特征样本数据进行“平移 + 缩放”，这并不影响特征之间的相关性。也就是说，标准化前后数据的相关性系数矩阵不变。

上述函数生成的数据集如果不考虑标签的话，也可以用于测试聚类算法，如图 3 所示。

(a)

(b)

(c)

(d)

(e)

(f)

图 3. 生成样本数据集，无标签

表 4 总结Scikit-Learn 中常用特征缩放函数。

表 4. Scikit-Learn 中常用特征缩放的函数函数介绍 sklearn.preprocessing.MaxAbsScaler()

通过除以每个特征的“最大绝对值”来将特征缩放到 [-1, 1] 的范围内，保留了特征的正负关系，助于防止异常值对数据缩放的影响。

sklearn.preprocessing.MinMaxScaler()

通过除以每个特征的“最大值减最小值”将特征缩放到指定范围之内，默认范围为 (0, 1)。它可以保留特征之间的线性关系，适用于受异常值影响较小的数据。

sklearn.preprocessing.Normalizer()

将样本行向量缩放到单位范数 (默认是L2 范数) 的方法。适用于特征的大小不重要，而只关心方向的情况。

sklearn.preprocessing.PowerTransformer()

对特征应用幂变换来使数据更加服从高斯分布。它支持Yeo-Johnson 和Box-Cox 变换，用于处理不符合正态分布的数据。

sklearn.preprocessing.QuantileTransformer()

将特征转换为均匀分布，从而使得变换后的数据服从指定的分位数。可以用来减少离群值的影响，特别是在数据分布不均匀的情况下。

sklearn.preprocessing.RobustScaler()

通过减去中位数并除以IQR 来对特征进行缩放。本书前文提过，IQR = Q3 – Q1。这种特征缩放对异常值具有鲁棒性，不会受到异常值的影响。适用于数据包含许多离群值的情况。

Page 6  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com sklearn.preprocessing.StandardScaler()

StandardScaler 通过将特征缩放到均值为0，方差为1 的标准正态分布来进行标准化。它适用于要求输入数据具有相似的尺度的机器学习算法。

import matplotlib.pyplot as plt import numpy as np from sklearn.preprocessing import StandardScaler from sklearn.datasets import make_circles, make_moons from sklearn.datasets import make_blobs, make_classification n_samples = 500 # 产生环形数据集 circles = make_circles(n_samples=n_samples, factor=0.5, noise=0.1)

# 产生月牙形状数据集 moons = make_moons(n_samples=n_samples, noise=0.1)

# blobs = make_blobs(n_samples=n_samples, centers = 4, cluster_std = 1.5)

# 几何变换 transformation = [[0.4, 0.2], [-0.4, 1.2]]

X = np.dot(blobs[0], transformation)

rotated = (X,blobs[1])

# 不同稀疏程度 varied = make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5])

# 用于测试分类算法的样本数据集 classif = make_classification(n_samples=n_samples, n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1)

datasets = [circles, moons, blobs, rotated, varied, classif]

# 可视化 fig, axes = plt.subplots(2,3,figsize=(6,4))

axes = axes.flatten()

for dataset_idx, ax_idx in zip(datasets, axes): X, y = dataset_idx # 标准化 X = StandardScaler().fit_transform(X)

ax_idx.scatter(X[:, 0], X[:, 1], s=18, c=y, cmap='Set3', edgecolors="k")

ax_idx.set_xlim(-3, 3)

ax_idx.set_ylim(-3, 3)

ax_idx.set_xticks(())

ax_idx.set_yticks(())

ax_idx.set_aspect('equal', adjustable='box')

b a e g h f

图 4. 生成样本数据集，代码

Page 7  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 29.4 处理缺失值

在数据分析中，缺失值是指数据集中某些观测值或属性值没有被记录或采集到的情况。由于各种原因，数据中缺失值不可避免。缺失值通常被编码为空白，NaN 或其他占位符 (比如−1)。处理缺失值是数据预处理中重要一环。

图 5. 缺失值

数据中缺失值产生的原因有很多。比如，在数据采集阶段，设备故障、人为失误、方法局限、拒绝参与调查、信息不完整等等可以造成数据缺失。另外，数据数据存储阶段也可能引入缺失值；比如，数据存储失败、存储器故障等等。

填补缺失值的方法有很多种，包括： ► 删除缺失值：直接删除缺失值所在的行或列，但这可能会导致数据的丢失和分析结果的偏差。

► 插值法：通过插值方法填补缺失值，如均值插值、中位数插值、最近邻插值、多项式插值等。

► 模型法：使用回归、决策树或神经网络等模型预测缺失值，但需要先对数据进行训练和测试，可能会导致模型的过拟合和不准确。

► 多重填补法：使用多个模型进行填补，可以提高填补缺失值的准确性和可靠性。

本书前文在介绍Pandas 时，我们了解了一些Pandas 中处理缺失值的方法。表 5 所示为Scikit-Learn 中常用处理缺失值方法。需要注意的是，表 5 中方法通常用于数值型数据。

表 5. Scikit-Learn 中常用来处理缺失值的函数函数介绍 sklearn.impute.SimpleImputer()

提供了一些基本的插补策略来处理缺失值，例如使用均值、中位数、众数进行插补 sklearn.impute.IterativeImputer()

使用多个回归模型来估计缺失值，每次迭代都更新缺失值的估计 sklearn.impute.KNNImputer()

使用最近邻样本的值来进行插补。它使用欧氏距离或其他指定的距离度量来选择最近邻

下面用图 8 介绍如何使用最邻近插补。

Page 8  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

Sepal length Sepal width Petal length Petal width Species 150 data points

图 6. 鸢尾花数据集中引入缺失值，每条黑带代表缺失值位置

Sepal length (cm)

Sepal width (cm)

Petal length (cm)

Petal width (cm)

Sepal length (cm)

Sepal width (cm)

Petal length (cm)

Petal width (cm)

Species 0, Setosa 1, Versicolor 2, Virginica

图 7. 鸢尾花数据，最近邻插补

a 从sklearn.impute 模块导入KNNImputer() 函数。KNNImputer() 完成k 近邻插补。k 近邻算法 (k- nearest neighbors algorithm, k-NN) 是最基本有监督学习方法之一，k-NN 中的k 指的是“近邻”的数量。k- NN 思路很简单——“近朱者赤，近墨者黑”。本书后文将介绍这种算法。

Page 9  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b 利用numpy.random.uniform() 产生 [0, 1) 之间连续均匀随机数NumPy 数组，数组形状和鸢尾花特征数据形状一致。

c 将原先生成的随机数数组 mask 中小于等于 0.4 的元素标记为 True，其余元素标记为 False。这样，mask 数组中的元素将形成一个“面具” (布尔掩码)，用来选择哪些位置将被置为缺失值。

大家也可以使用numpy.random.choice() 函数来完成上述操作。这个函数用于从给定的一维数组或类似序列中按指定概率值随机抽取元素。比如numpy.random.choice([True, False], p = (0.4, 0.6), size = (150, 4))，列表 [True, False] 为要从中进行抽样的序列源，p 是概率分布数组，用于指定从序列中每个元素被选中的概率。我们还可以指定是否允许重复抽取，默认允许重复抽取。

d 将 X_NaN 数组中根据 mask 中对应位置为 True 的元素，设置为缺失值 (NaN)。换句话说，该代码将 X_NaN 数组中部分元素置为缺失值，而其他元素保持不变。

为了准确获取缺失值位置、数量等信息，对于Pandas 数据帧数据可以采用isna() 或 notna() 方法。

e 采用iris_df_NaN.isna()，返回具体位置数据是否为缺失值。数据缺失的话，为True；否则，为 False。sklearn.impute.MissingIndicator() 也可以用来获取缺失值位置。

f 为采用seaborn.heatmap() 可视化数据缺失值，图 6 所示热图的每一条黑色条带代表一个缺失值。

使用缺失值热图可以粗略观察得到缺失值分布情况。

g 创建了一个KNNImputer 对象，用于执行k 最近邻插补。参数n_neighbors 指定了在插补过程中要考虑的最近邻样本的数量。

h 将KNNImputer 应用于具有缺失值的数据数组 X_NaN。fit_transform() 方法将执行两个步骤：拟合 (fit) 和转换 (transform)。拟合时，KNNImputer 将根据已知数据 (非缺失值) 来训练最近邻模型。转换时，使用训练过的模型，KNNImputer 将执行k 最近邻插补，将缺失值填充为预测的值。KNNImputer 返回结果被存储在 X_NaN_kNN 中，其中包含了插补后的数据。

h 用seaborn.pairplot() 绘制成对散点图可视化插补后结果，如图 7 所示。

Page 10  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sklearn.datasets import load_iris from sklearn.impute import KNNImputer import matplotlib.pyplot as plt import numpy as np import pandas as pd import seaborn as sns # 导入鸢尾花数据 X, y = load_iris(as_frame=True, return_X_y=True)

# 引入缺失值 X_NaN = X.copy()

mask = np.random.uniform(0,1,size = X_NaN.shape)

mask = (mask <= 0.4)

X_NaN[mask] = np.NaN iris_df_NaN = X_NaN.copy()

iris_df_NaN['species'] = y # 可视化缺失值位置 is_NaN = iris_df_NaN.isna()

print(iris_df_NaN.isnull().sum() * 100 / len(iris_df_NaN))

fig, ax = plt.subplots()

ax = sns.heatmap(is_NaN, cmap='gray_r', cbar=False)

# 用kNN插补 knni = KNNImputer(n_neighbors=5)

X_NaN_kNN = knni.fit_transform(X_NaN)

iris_df_kNN = pd.DataFrame(X_NaN_kNN, columns=X_NaN.columns, index=X_NaN.index)

iris_df_kNN['species'] = y sns.pairplot(iris_df_kNN, hue='species', palette = "bright")

b a e g h f h

图 8. 处理缺失值，代码

## 29.5 处理离群值

离群值 (outlier)，又称逸出值、离群值，是指数据集中与其他数据点有显著差异的数据点，也就是说明显地偏大或偏小。离群值可能是由于异常情况、错误测量、数据录入错误或意外事件等原因而产生。离群值可能会对数据分析和建模造成问题，因为它们可能导致误差或偏差，并降低模型的准确性。

因此，数据分析师通常会对数据集中的离群值进行检测和处理。

常见的离群值检测方法包括基于统计学的方法、基于距离的方法、基于密度的方法和基于模型的方法。处理离群值的方法包括删除、替换、调整或利用异常值建立新的模型等。

表 6 所示为Scikit-Learn 中常用处理离群值函数。

Page 11  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 9. 离群点表 6. Scikit-Learn 中常用来处理离群值的函数函数介绍 sklearn.ensemble.IsolationForest()

使用隔离森林方法检测异常值 sklearn.svm.OneClassSVM()

使用支持向量机方法进行单类异常值检测 sklearn.covariance.EllipticEnvelope()

使用基于高斯分布的椭圆包络方法检测异常值 sklearn.neighbors.LocalOutlierFactor()

使用局部离群因子方法检测异常值 sklearn.covariance.RobustCovariance()

使用鲁棒协方差估计进行异常值检测 sklearn.covariance.mahalanobis()

计算马哈拉诺比斯距离来检测异常值

图 11 所示代码介绍如何使用Scikit-Learn 处理离群值。这段代码参考了Scikit-Learn 官方示例。

a 从sklearn.svm 模块中导入OneClassSVM 类，该类实现支持向量机 (Support Vector Machine, SVM)

中的单类异常值检测方法。本书后续将专门介绍支持向量机。

b 从sklearn.covariance 模块中导入EllipticEnvelope 类，该类实现基于高斯分布的椭圆包络方法，用于检测异常值。椭圆包络假设正常数据点是从多元高斯分布中产生，然后构建一个椭圆来包围正常数据点，从而将异常数据点识别为离这个椭圆很远的点。

c 从sklearn.ensemble 导入IsolationForest 类，该类实现隔离森林 (Isolation Forest) 方法，用于检测异常值。隔离森林利用随机分割数据来构建一棵或多棵树，并通过观察数据点在树中的深度来确定异常值。

d 定义了一个名为 blobs_params 的字典，其中包含了一些参数设置。random_state=0 用于控制随机数生成的种子值。n_samples=n_inliers 控制生成的总样本数。n_features=2 设定每个数据点的特征数量为 2，即两个特征。

e 构造了4 组数据集。

f 用EllipticEnvelope() 创建椭圆包络的异常值检测模型。参数contamination 用于指定异常值的比例。具体来说，它表示数据中异常值的比例。这个参数是一个介于 0 和 0.5 之间的值，通常需要根据具体问题进行调整。参数random_state 用于控制随机数生成的种子值，以确保每次运行得到相同的结果。

Page 12  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com g 使用 OneClassSVM() 创建一个基于支持向量机的异常值检测模型。参数nu 用于指定异常值的比例，通常在 0 和 1 之间。kernel="rbf" 指定支持向量机所使用的核函数的类型。"rbf" 表示径向基函数 (Radial Basis Function)，也称为高斯核。这个核函数在支持向量机中常用于处理非线性问题。gamma=0.1 是支持向量机模型的核函数参数。较小的 gamma 值会使得支持向量具有更远的影响范围，可能会导致决策边界更平滑；较大的 gamma 值则会使支持向量的影响范围更小，可能会导致决策边界更复杂。

h 使用 IsolationForest() 创建一个基于隔离森林的异常值检测模型。

i 使用 fit() 方法对样本数据进行拟合，然后使用 predict() 方法来预测数据点是否为异常值。

j 用平面等高线可视化异常值检测模型的决策边界。

图 10. 用Scikit-Learn 判断离群点

Page 13  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import matplotlib.pyplot as plt import numpy as np from sklearn.datasets import make_blobs, make_moons from sklearn.svm import OneClassSVM from sklearn.covariance import EllipticEnvelope from sklearn.ensemble import IsolationForest # 生成数据 n_samples = 500 outliers_fraction = 0.10 n_outliers = int(outliers_fraction * n_samples)

n_inliers  = n_samples - n_outliers X_outliers = np.random.uniform(low=-6,high=6, size=(n_outliers,2))

np.random.RandomState(0)

blobs_params = dict(random_state=0, n_samples=n_inliers, n_features=2)

datasets = [ make_blobs(centers=[[0, 0], [0, 0]], cluster_std=0.5, **blobs_params)[0], make_blobs(centers=[[2, 2], [-2, -2]], cluster_std=[0.5, 0.5], **blobs_params)[0], make_blobs(centers=[[2, 2], [-2, -2]], cluster_std=[1.5, 0.3], **blobs_params)[0],

## 4.0 * (make_moons(n_samples=n_samples, noise=0.05,

random_state=0)[0]- np.array([0.5, 0.25]))]

# 处理离群值 anomaly_algorithms = [ EllipticEnvelope(contamination=outliers_fraction, random_state=42), OneClassSVM(nu=outliers_fraction, kernel="rbf", gamma=0.1), IsolationForest(contamination=outliers_fraction, random_state=42)]

# 网格化数据，用来绘制等高线 xx, yy = np.meshgrid(np.linspace(-7, 7, 150), np.linspace(-7, 7, 150))

xy = np.c_[xx.ravel(), yy.ravel()]

colors = np.array(["#377eb8", "#ff7f00"])

# 可视化 fig = plt.figure(figsize=(8,12))

plot_idx = 1 for idx, X in enumerate(datasets): X = np.concatenate([X, X_outliers], axis=0)

for algorithm in anomaly_algorithms: algorithm.fit(X)

y_pred = algorithm.fit(X).predict(X)

ax = fig.add_subplot(4,3,plot_idx); plot_idx += 1 Z = algorithm.predict(xy)

Z = Z.reshape(xx.shape)

# 绘制边界 ax.contour(xx, yy, Z, levels=[0], linewidths=2, colors="black")

# 绘制散点数据集 ax.scatter(X[:, 0], X[:, 1], s=10, color=colors[(y_pred + 1) // 2])

ax.set_xlim(-7, 7); ax.set_ylim(-7, 7)

ax.set_xticks(()); ax.set_yticks(())

b a e g h f h j

图 11. 处理离群值，代码

Page 14  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 29.6 训练集 vs 测试集

在机器学习中，训练集和测试集是用于训练和评估模型性能的两个关键数据集。Scikit-Learn 库提供了工具和函数来处理和划分这些数据集。

Random select Features, X Target, y X y Split Training set Test set

图 12. 拆分数据集为训练集和测试集

训练集 (training set) 是用来训练机器学习模型的数据集。模型在训练集上学习数据的模式、关系和特征，以便能够做出预测 (回归、降维、分类、聚类等等)。训练集通常包含已知的输入特征和对应的目标输出，用于模型进行学习和参数调整。

测试集 (test set) 是用于评估机器学习模型性能的数据集。一旦模型在训练集上进行了学习，它需要在测试集上进行预测，以便判断模型在未见过的数据上的表现如何。测试集应该是与训练集相互独立的样本，以确保对模型的泛化能力进行准确评估。

在划分数据集时，常见的做法是将大部分数据用于训练 (例如80%)，少部分用于测试 (例如20%)。

通过在测试集上评估模型的性能，可以获得模型在真实环境中的表现，并帮助检测过拟合等问题。图 13 所示为将鸢尾花数据集拆分为训练集和测试集。

图 14 代码完成数据拆分以及可视化，下面介绍其中关键语句。

a 从sklearn.model_selection 模块导入train_test_split。train_test_split 将数据集划分为训练集和测试集，以便在机器学习模型的开发和评估过程中使用。train_test_split 函数的作用是将输入的数据集 (通常是特征矩阵和对应的标签向量) 分成两个部分：一个用于训练模型，另一个用于评估模型的性能。这是为了确保模型在未见过的数据上表现良好，以避免过拟合。

b 用 train_test_split 函数将输入的数据集 X 和 y 划分为训练集和测试集，并将划分后的数据分别赋值给了 X_train、X_test、y_train 和 y_test 四个变量。

X 为输入的特征矩阵，包含样本的特征信息。

y 为输入的标签向量，包含与特征对应的目标值。

参数test_size 为 0.2，表示将数据的 20% 作为测试集，剩余 80% 作为训练集。这个参数决定了训练集和测试集的划分比例。

X_train 为训练集的特征矩阵，包含用于训练机器学习模型的特征数据。

Page 15  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X_test 为测试集的特征矩阵，包含用于评估模型性能的特征数据。

y_train 为训练集的标签向量，包含训练集样本对应的目标值。

y_test 为测试集的标签向量，包含测试集样本对应的目标值。

c 创建一个包含1 行、2 列的子图布局。gridspec_kw={'width_ratios': [4, 1]} 参数用于控制每个子图的宽度比例，这里设置了第一个子图的宽度为第二个子图的 4 倍。

d 将np.c_[X,y] 转化成Pandas DataFrame，以便后续可视化。e 将 np.c_[X_train, y_train] 转化为训练集Pandas DataFrame。f 将np.c_[X_test, y_test] 转化为测试集Pandas DataFrame。

Sepal length, X1 Sepal width, X2 Petal width, X4 Petal length, X3 Species, Y Sepal length, X1 Sepal width, X2 Petal width, X4 Petal length, X3 Species, Y Sepal length, X1 Sepal width, X2 Petal width, X4 Petal length, X3 Species, Y Split Training set Test set

图 13. 拆分鸢尾花数据集为训练集和测试集

Page 16  |  Chapter 29 Scikit-Learn 数据  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sklearn.datasets import load_iris from sklearn.model_selection import train_test_split import matplotlib.pyplot as plt import pandas as pd import numpy as np import seaborn as sns # 导入鸢尾花数据 X,y = load_iris(return_X_y=True)

# 拆分鸢尾花数据集为训练集和测试集 X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2)

# 自定义可视化函数 def visualize(df): fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [4, 1]})

sns.heatmap(df.iloc[:,0:-1], cmap='RdYlBu_r', yticklabels = False, cbar=False, ax = axs[0])

sns.heatmap(df.iloc[:,[-1]], cmap='Set3', yticklabels = False, cbar=False, ax = axs[1])

# 转化为Pandas DataFrame columns = ['Sepal length, X1', 'Sepal width, X2', 'Petal length, X3', 'Petal width, X4', 'Species']

df_full = pd.DataFrame(np.c_[X,y], columns = columns)

visualize(df_full)

# 训练集 df_train = pd.DataFrame(np.c_[X_train, y_train], columns = columns)

visualize(df_train)

# 测试集 df_test = pd.DataFrame(np.c_[X_test, y_test], columns = columns)

visualize(df_test)

b a e f X y

图 14. 拆分鸢尾花数据集为训练集和测试集，代码

Page 1  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Regression Methods in Scikit-Learn Scikit-Learn 回归一元线性回归、二元线性回归、多项式回归

想象力比知识更重要，因为知识是有限的，而想象力概括世界上的一切，推动着进步，并且是知识进化的源泉。

Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution. It is, strictly speaking, a real factor in scientific research.

—— 阿尔伯特·爱因斯坦 (Albert Einstein)  |  理论物理学家  |  1879 ~ 1955

◄ sklearn.linear_model.LinearRegression 线性回归模型类，用于建立和训练线性回归模型 ◄ sklearn.preprocessing.PolynomialFeatures 特征预处理类，用于生成多项式特征，将原始特征的幂次组合以扩展特征空间，用于捕捉更复杂的非线性特征关系

Page 2  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 30.1 聊聊回归

回归分析是一种基础但很重要的机器学习方法，回归常用来研究变量之间的关系，并可以用来预测趋势。

本书前文第27 章已经介绍过用Statsmodels 库完成一元线性回归。一元线性回归是一种基本的统计分析方法，用于探究两个连续变量之间的关系。“一元”表示模型中只有一个自变量 (independent variable)。自变量也叫解释变量 (explanatory variable) 或回归元 (regressor)、外生变量 (exogenous variables)、预测变量 (predictor variables)。本章后续还会介绍二元、多元回归。

而“线性回归”则表明模型假设自变量与因变量之间存在线性关系，如图 1 所示。

y

图 1. 平面上，一元线性回归

因变量 (dependent variable) 也叫被解释变量 (explained variable)、或回归子 (regressand)、内生变量 (endogenous variable)、响应变量 (response variable)。

在一元线性回归中，我们试图找到一条直线，该直线最好地拟合了自变量和因变量之间的数据关系。

具体来说，我们要找到一条直线，使得所有数据点到这条直线的垂直距离之差 (残差) 平方和最小化。残差项 (residuals) 也叫误差项 (error term)、干扰项 (disturbance term)或噪音项 (noise term)。图 2 中灰色线段便代表残差。

如图 3 所示，残差平方和代表图中所有蓝色正方形的面积。这些蓝色正方形的边长便是残差。这种方法叫做最小二乘法 (Ordinary Least Square, OLS)。

Page 3  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Observed Predicted Error y 0b

图 2. 一元线性回归中的残差

Error y 0b

图 3. 残差平方和的几何意义

如图 4 所示，线性回归并不适合所有回归分析；很多时候，我们还需要非线性回归。

非线性回归是指自变量和因变量之间存在着非线性关系的回归模型。在非线性回归中，自变量和因变量的关系不再是简单的线性关系，而可能是多项式关系、指数关系、对数关系等其他非线性形式。非线性回归可以通过拟合曲线或曲面来捕捉数据的非线性关系。本章后续将会介绍多项式回归、逻辑回归两种非线性回归。

Page 4  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 4. 线性回归并不适合所有回归分析

## 30.2 一元线性回归

本书第27 章介绍用 statsmodels.regression.linear_model.OLS() 完成OLS 一元线性回归。本节采用相同样本数据，但是Scikit-Learn 函数完成线性回归。

y = b0 + b1x1 x1 b1 b0

图 5. 一元OLS 线性回归数据关系

a 从sklearn.linear_model 导入LinearRegression。LinearRegression 提供了许多方法和属性，使你能够创建、训练和使用线性回归模型。

b 创建了一个名为LR 的LinearRegression 对象，然后你可以使用这个对象来调用线性回归模型的方法，如拟合数据、进行预测以及评估模型性能等。

例如，可以使用LR.fit(X, y)方法来拟合训练数据，其中X 是输入特征数据，y 是对应的目标输出数据。然后，可以使用LR.predict(X_new)来对新的输入特征数据X_new 进行预测。

c 中LR 对象调用fit(X, y[, sample_weight]) 来拟合模型。其中X 为自变量的数据，y 为因变量的数据。该方法会求解最小二乘法的参数，拟合出一条线性回归模型，该模型可以用 来预测新的数据。如果指定了sample_weight 参数，则表示样本的权重，可以用于加权最小二乘法。

d 中coef_用来获取线性回归模型的系数。该属性返回一个数组，其中包含每个自变量对应的系数值，可以用于分析模型的特征重要性。

e 中intercept_用来获取线性回归模型的截距。该属性返回一个标量，表示线性回归模型的截距值。

f 中predict(X) 用来对新的数据进行预测，其中X 为自变量的数据。该方法会根据已经拟合的线性回归模型，对给定的自变量数据进行预测，返回对应的因变量数据。

Page 5  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 6 中沿y 轴方向的灰色线段代表误差，显然这些线段并不垂直红色线。如图 7 所示，如果代表误差的灰色线段绘制于红色线的话，这种回归模型叫正交回归 (orthogonal regression)。正交回归和前文介绍的主成分分析有关。正交回归的一种常见方法是主成分回归 (Principal Component Regression，PCR)，其中主成分分析PCA 用于寻找数据中的主要方差方向，然后利用这些主成分进行回归。

鸢尾花书《数据有道》将专门介绍正交回归。

图 6. 一元OLS 线性回归示例

图 7. 一元正交线性回归示例

Page 6  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import matplotlib.pyplot as plt from sklearn.linear_model import LinearRegression # 生成随机数据 num = 50 np.random.seed(0)

x_data = np.random.uniform(0,10,num)

y_data = 0.5 * x_data + 1 + np.random.normal(0, 1, num)

x_data = x_data.reshape((-1, 1))

# 将x调整为列向量 data = np.column_stack([x_data,y_data])

# 创建回归对象并进行拟合 LR = LinearRegression()

# 使用LinearRegression()构建了一个线性回归模型 LR.fit(x_data, y_data)

slope = LR.coef_ # 斜率 intercept = LR.intercept_ # 截距 x_array = np.linspace(0,10,101).reshape((-1, 1))

# 预测 predicted = LR.predict(x_array)

data_ = np.column_stack([x_data,LR.predict(x_data)])

fig, ax = plt.subplots()

ax.scatter(x_data, y_data)

ax.scatter(x_data, LR.predict(x_data), color = 'k', marker = 'x')

ax.plot(x_array, predicted, color = 'r')

ax.plot(([i for (i,j) in data_], [i for (i,j) in data]), ([j for (i,j) in data_], [j for (i,j) in data]), c=[0.6,0.6,0.6], alpha = 0.5)

ax.set_xlabel('x'); ax.set_ylabel('y')

ax.set_aspect('equal', adjustable='box')

ax.set_xlim(0,10); ax.set_ylim(-2,8)

b a e f

图 8. 一元OLS 线性回归，代码

## 30.3 二元线性回归

二元线性回归是一种线性回归模型，其中有两个自变量和一个因变量，它旨在分析两个自变量和因变量之间的线性关系。如图 10 所示，二元线性回归解析式在三维空间为一平面。

Page 7  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com y = b0 + b1x1 + b2x2 x1 x2 b2 b1 b0

图 9. 二元OLS 线性回归数据关系

图 10. 二元线性回归示例

图 11 代码绘制图 10，下面介绍其中关键语句。

a 利用numpy.random.randn() 生成自变量数据，两个特征，100 个样本点。

b 中fig 是一个Matplotlib 中的Figure 对象，表示一个绘图窗口或画布，可以在这个画布上添加不同类型的子图图轴对象。add_subplot(111, projection='3d') 是在fig 上添加一个子图的操作。其中，111 表示子图的布局。在这里，111 表示一个1 × 1 的网格，即只有一个子图。projection='3d' 指定子图的投影方式为3D 投影。这意味着，我们可以在该子图中创建一个三维的可视化场景，可以用于绘制三维数据点、曲线、表面等。

c 利用numpy.column_stack() 将两个一维数组按列堆叠在一起，形成一个二维数组，代表了坐标。

其中，x1_grid.flatten() 和 x2_grid.flatten() 将二维数组扁平化为一维数组。

d 将输入特征数据 X_grid 传递给已训练的线性回归模型 LR，然后获得预测输出值，这些预测输出值被存储在 y_pred 变量中。

e 利用numpy.reshape() 调整之前计算得到的预测结果数组 y_pred 的形状，使其与另一个数组 x1_grid 具有相同的形状。

Page 8  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f 用plot_wireframe() 绘制二元线性回归平面。

import numpy as np import matplotlib.pyplot as plt from sklearn.linear_model import LinearRegression # 随机生成数据集 np.random.seed(0)

n_samples = 100 X = np.random.randn(n_samples, 2)

y = -3 * X[:,0] + 2 * X[:,1] + 1 + 0.5*np.random.randn(n_samples)

# 创建线性回归模型并拟合数据 LR = LinearRegression()

y_predicted = LR.fit(X, y)

slope = LR.coef_ # 斜率 intercept = LR.intercept_ # 截距 fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# 绘制三维样本散点 ax.scatter(X[:,0], X[:,1], y)

# 生成回归平面的数据点 x1_grid, x2_grid = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))

X_grid=np.column_stack((x1_grid.flatten(),x2_grid.flatten()))

# 预测回归平面上的响应变量 y_pred = LR.predict(X_grid)

y_pred = y_pred.reshape(x1_grid.shape)

# 绘制回归平面 ax.plot_wireframe(x1_grid, x2_grid, y_pred)

ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')

ax.set_zlabel('y')

ax.set_xlim([-3,3]); ax.set_ylim([-3,3])

ax.set_proj_type('ortho'); ax.view_init(azim=-120, elev=30)

b a e f

图 11. 二元OLS 线性回归，代码

有了二元线性回归，理解多元线性回归就很容易了。如图 12 所示，多元线性回归是一种线性回归的扩展形式，用于建立一个预测模型来描述多个输入特征与一个连续的目标输出之间的线性关系。

Page 9  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com x1 x2 xD ...

y = b0 + b1x1 + b2x2 + ... + bD 1xD 1 + bDxD x3 xD 1 bD 1 bD b3 b2 b1 b0

图 12. 多元OLS 线性回归数据关系

## 30.4 多项式回归

多项式回归 (polynomial regression) 是一种线性回归的扩展，它允许我们通过引入多项式 (例如，二次、三次、四次等) 来建模非线性关系。如图 13 所实话，在多项式回归中，我们不仅使用自变量的原始值，还将其不同阶数作为额外的特征，从而能够更好地拟合数据中非线性模式。

从函数图像角度来讲，如图 14 所示，多项式回归曲线好比若干曲线叠加的结果。

多项式回归的阶数影响着模型的灵活性。如图 15 所示，较低的阶数 (比如图 15 (a)、(b)) 可能无法很好地捕捉数据中的复杂关系，而较高的阶数 (比如图 15 (e)、(f)) 可能会导致过度拟合。阶数越高，模型越能够适应训练数据，但也越容易在测试数据或实际应用中表现不佳。

过拟合是指模型在训练数据上表现得很好，但在新数据上表现较差的现象。当多项式回归的阶数过高时，模型可能会过度适应训练数据中的噪声和细节，从而失去了泛化能力。这意味着模型对于新的、 未见过的数据可能无法进行准确的预测，因为它在训练数据上“记住了”许多细微的变化，而这些变化可能在真实数据中并不存在。

图 16 中代码绘制图 15。下面介绍其中关键语句。

Page 10  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com y = b0 + b1x + b2x2 + b2x3 + ... + bmxm x2 x3 ...

bm b3 b2 b1 b0

图 13. 多项式回归数据关系

x2 x3 x4 x5 b3 b2 b1 b0 b4 b5

图 14. 一元五次函数可以看做是6 个图像叠加的结果

a 从sklearn.preprocessing 导入PolynomialFeatures。在机器学习中，有时候原始特征并不足够表达数据的复杂关系，这时可以引入多项式特征。多项式特征是原始特征的幂次组合，通过引入这些特征， 可以更好地拟合数据的非线性关系。PolynomialFeatures 类的作用就是将原始特征转换为高次的多项式特征。它可以通过设置特定的阶数来生成不同阶数的多项式特征。

b 定义列表，列表中整数为指定的多项式回归阶数。

c 用PolynomialFeatures 原始特征转换为高次的多项式特征。参数 degree 设置多项式的阶数。这个阶数决定了生成的多项式回归的最高阶数 (次数)。

Page 11  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com d 中X.reshape(-1, 1) 将一维数据 X 进行形状变换，将其转换为一个二维数组，其中列数为 1。这是因为 fit_transform 方法接受的输入应该是一个二维数组，其中每行代表一个样本，每列代表一个特征。

在运行代码时，请大家自行查看这一行结果，并用seaborn.heatmap() 可视化结果。

e 创建一个 LinearRegression 类的实例，并将其赋值给变量 poly_reg。通过这个实例，可以访问回归模型的方法和属性，例如模型的拟合、预测等。

f 加载样本数据，训练回归模型。

g 使用已经训练好的线性回归模型对多项式特征转换后的数据进行预测。

h 这行代码连续完成了：多项式特征转换 + 模型预测。首先将输入数据 x_array 进行多项式特征转换，然后使用已经训练好的回归模型 poly_reg 对转换后的数据进行预测，并返回预测结果。

i 提取系数b1、b2、b3 … j 提取截距b0。

k 创建一个包含线性方程的字符串。这一句代码首先将截距插入到字符串中。其中，{:.1f} 是一个占位符，将用来插入一个浮点数，并保留一位小数。.format(intercept) 是 Python 字符串的 .format() 方法，用于将特定值插入到格式化字符串中的占位符。

l 利用for 循环，将多项式回归系数项插入到字符串中。'{:.1f}x^{}'.format(coef[j], j) 是一个格式化字符串，用于将系数的值 coef[j] 和次数 j 插入到字符串中的占位符位置。{:.1f} 表示插入一个浮点数， 并保留一位小数；^{} 表示插入一个整数。

m 用text() 在子图上打印多项式回归解析式。

Page 12  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 1.1 0.5 y = − 0.2 2.3 1.3 0.2 y = − + − + 1.2 0.2 0.2 0.05 y = − − + 0.3 0.7 0.3 y = + − 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (a) degree = 1 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (b) degree = 2 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (c) degree = 3 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (d) degree = 4 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (e) degree = 7 0.0 1.0 2.0 3.0 4.0 2.0 1.0 0.0 1.0 2.0 (f) degree = 8

图 15. 阶数对多项式回归曲线影响

Page 13  |  Chapter 30 Scikit-Learn 回归  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import matplotlib.pyplot as plt from sklearn.preprocessing import PolynomialFeatures from sklearn.linear_model import LinearRegression # 生成随机数据 np.random.seed(0)

num = 30 X = np.random.uniform(0,4,num)

y = np.sin(0.4*np.pi * X) + 0.4 * np.random.randn(num)

data = np.column_stack([X,y])

x_array = np.linspace(0,4,101).reshape(-1,1)

degree_array = [1,2,3,4,7,8]

fig, axes = plt.subplots(3,2,figsize=(10,20))

axes = axes.flatten()

for ax, degree_idx in zip(axes,degree_array): poly = PolynomialFeatures(degree = degree_idx)

X_poly = poly.fit_transform(X.reshape(-1, 1))

# 训练线性回归模型 poly_reg = LinearRegression()

poly_reg.fit(X_poly, y)

y_poly_pred = poly_reg.predict(X_poly)

data_ = np.column_stack([X,y_poly_pred])

y_array_pred = poly_reg.predict( poly.fit_transform(x_array))

# 绘制散点图 ax.scatter(X, y, s=20)

ax.scatter(X, y_poly_pred, marker = 'x', color='k')

ax.plot(([i for (i,j) in data_], [i for (i,j) in data]), ([j for (i,j) in data_], [j for (i,j) in data]), c=[0.6,0.6,0.6], alpha = 0.5)

ax.plot(x_array, y_array_pred, color='r')

ax.set_title('Degree = %d' % degree_idx)

# 提取参数 coef = poly_reg.coef_ intercept = poly_reg.intercept_ # 回归解析式 equation = '$y = {:.1f}'.format(intercept)

for j in range(1, len(coef)): equation += ' + {:.1f}x^{}'.format(coef[j], j)

equation += '$' equation = equation.replace("+ -", "-")

ax.text(0.05, -1.8, equation)

ax.set_aspect('equal', adjustable='box')

ax.set_xlim(0,4)

ax.grid(False)

ax.set_ylim(-2,2)

b a e f g h j k xp ...

xp ...

y

图 16. 多项式回归，代码

Page 1  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Dimensionality Reduction in Scikit-Learn Scikit-Learn 降维通过投影、旋转这两个几何视角理解主成分分析

读书好比生火，每一个字都是一个火花。

To learn to read is to light a fire; every syllable that is spelled out is a spark.

—— 雨果 (Victor Hugo)  |  法国文学家  |  1802 ~ 1885

◄ sklearn.preprocessing.StandardScaler() 用于对数据进行标准化处理 ◄ sklearn.decomposition.PCA() 执行主成分分析PCA 以减少数据维度 ◄ sklearn.covariance.EmpiricalCovariance() 计算基于样本的经验协方差矩阵

Page 2  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 31.1 降维

降维 (dimensionality reduction) 是机器学习和数据分析领域中的重要概念，指的是将高维数据映射到低维空间中的过程。在现实世界中，很多数据集都具有很高的维度，每个数据点可能包含大量特征或属性。然而，高维数据在处理和分析时可能会面临一些问题，例如计算复杂度增加、维度诅咒、可视化困难等。

维度诅咒 (curse of dimensionality) 用来描述数据特征 (维度) 增加时，数据特征空间体积指数增大。

如所示，一个特征选取6 个采样点，一维空间就6 个点，二维空间有36 (62) 个点，三维空间有216 (63)

个点。如所示，四维空间有1296 (64) 个点。而10 个特征则达到惊人的60466176 (610)个点。

而降维的目标是通过保留尽可能多的信息，将高维数据投影到一个更低维的子空间，以便更有效地处理和分析数据，减少计算负担，提高模型的性能和可解释性。

图 1. 一维、二维、三维

图 2. 四维

本书第27 章介绍过主成分分析。简单来说，主成分分析 (Principal Component Analysis, PCA) 将原始特征投影到新的正交特征空间上，以保留最大方差的特征。PCA 能够去除数据中的冗余信息，提取最重要的特征。本章还会采用几何视角继续探讨如何用PCA 完成降维。

此外，我们也可以利用流形学习完成非线性降维。流形学习 (manifold learning) 是一种无监督学习方法，用于在高维数据中发现潜在的低维结构。在高维空间中，数据点通常是分散的，而流形学习算法的

Page 3  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 目标是将这些分散的数据点映射到一个低维流形中，从而更好地理解数据的结构和特征。本书不展开讲解流形学习。

本书前文主要是从数据角度介绍如何使用主成分分析完成数据降维和近似还原；本章则要用几何视角和大家聊聊主成分分析，让大家深度理解主成分分析背后的思想。

当然想要真正理解主成分分析，离不开线性代数、概率统计工具，这是鸢尾花书《矩阵力量》、 《统计至简》要解决的问题。

## 31.2 主成分分析

本书前文介绍过，一般情况，PCA 的基本思路是将数据投影到由主成分构成的新坐标系中，其中主成分是一组方向上方差最大的基向量。

为了方便讨论，如图 3 所示，我们先对数据进行去均值 (中心化) 处理。几何上来看，就是把数据的质心 (centroid) µ 移动到原点0。

此外，图 3 中椭圆和散点的关系是通过协方差矩阵联系起来的。本书前文介绍高斯分布时，大家已经建立了各种协方差矩阵和椭圆的联系。

µ = 0 µ

图 3. 将质心移到原点

本书前文介绍过，在进行PCA 前一般要对数据进行标准化 (standardization)。标准化可以消除数据不同特征尺度不同的影响，标准化过程还完成了去单位化，每个特征数据都变成了Z 分数。PCA 的目标是找到数据中方差最大的方向，即主成分。如果某个特征具有很大的方差，即使它在原始数据中不是最主要的特征，它在PCA 中仍然可能成为主成分，导致降维后损失了其他重要信息。标准化可以将所有特征的标准差调整为1，从而避免方差主导的问题。而标准化包含两步——平移、缩放。其中，平移就是数据去均值，即中心化。

想要了解主成分分析，就必须理解数据投影 (projection)。图 4 所示为二维数据最简单的投影，分别向横轴、纵轴投影。在平面上，二维数据可以用散点图可视化。散点的横轴坐标就是数据的第一特征， 散点的纵坐标就是数据的第二特征。因此，图 4 的投影过程实际上就是将数据的第一、第二特征分离， 然后分别计算各个特征的均值、标准差。由于数据已经中心化，各个特征的均值为0。

Page 4  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 我们在《矩阵力量》中会详细了解数据投影使用的数学工具。

X1 µ = 0 X1 X2 X2

图 4. 分别向横轴、纵轴投影，并绘制一维数据分布

主成分分析的目标是将原始数据投影到一个新的坐标系中，使得投影后的数据具有最大的方差。通过这种方式，可以捕获数据中的主要变化方向，从而实现数据降维和特征提取。在进行投影时，第一个主成分的方向被选择为能够使投影后方差最大化的方向。

显然，图 4 所示的两个投影方向并不完美，我们可以尝试找到更好的投影方向。

如图 5 所示，平面散点朝16 个不同方向投影，并计算投影结果的方差值。从图 5 中每个投影结果的分布宽度，用标准差量化，我们就可以得知C、K 这两个方向就是我们要找的第一主成分方向。G、O 这两个方向也值得我们关注，因为这两个方向上投影结果的方差 (标准差的平方) 最小。

Page 5  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com A B C D E F G H I J K L M N O P

图 5. 二维数据分别朝16 个不同方向投影

换个视角来看，如图 6 所示，主成分分析无非就是在不同的坐标系中看同一组数据。数据朝不同方向投影会得到不同的投影结果，对应不同的分布；朝椭圆长轴方向投影，得到的数据标准差最大；朝椭圆短轴方向投影得到的数据标准差最小。v1对应的便是第一主成分PC1。这里用到的几何工具就是旋转 (rotation)。

从椭圆的视角来看，图 6 中，v1第一主成分PC1 方向就是椭圆长轴所在方向，v2第二主成分PC2 方向就是椭圆短轴所在方向。显然，v1和v2垂直！我们管这个新的直角坐标系叫做 [v1, v2]。原来数据的坐标系记做 [e1, e2]。图 6 的坐标系旋转也完成了旋转椭圆到正椭圆的几何转换过程。图 7 所示为在 [v1, v2] 中看数据投影。

大家可能要问，究竟采用怎样的数学工具才能计算得到v1和v2？

这就需要我们首先计算协方差矩阵Σ，然后对协方差矩阵Σ 进行特征值分解。特征向量就是我们要找的主成分方向。

Page 6  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com v1 v2 v1 v2 Rotate e1 e2 [e1, e2]

[v1, v2]

e1 e2

图 6. 坐标系旋转 A B C D E F G H I J K L M N O P

图 7. 换个坐标系看投影

Page 7  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

此外，除了特征值分解协方差矩阵，还有其他不同的主成分分析技术路线。鸢尾花书《数据有道》

会专门比较不同技术路线的异同。

虽然，我们不会具体介绍计算协方差、特征值分解背后的数学工具，以及这两个工具和椭圆的联系；但是大家可能已经发现，想要深入理解主成分分析，离不开概率统计、线性代数、几何这些视角。

这都是鸢尾花“数学三剑客”要介绍的内容。

在主成分分析中，主成分通常是原始特征的线性组合。也就是说，PCA 是一种线性降维方法，它只能捕捉数据中的线性相关性。如果数据具有复杂的非线性关系，PCA 可能无法很好地捕捉这些模式，从而导致信息丢失。

而核主成分分析 (Kernel Principal Component Analysis) 在高维特征空间中使用核技巧 (kernel trick) 来进行PCA，从而能够处理非线性关系。核PCA 可以解决传统PCA 无法处理的非线性问题。在处理非线性数据时，传统PCA 可能会损失数据的重要信息，因为它只能发现线性关系。核PCA 通过将数据映射到高维特征空间，将数据从原始空间中的非线性关系转化为高维空间中的线性关系，因此可以有效地保留数据的非线性结构信息。

与传统的主成分分析不同，核PCA 不直接使用原始数据来计算主成分，而是通过将数据映射到高维特征空间来获取主成分。核技巧的基本思想是通过核函数 (kernel function) 将数据映射到高维特征空间中，从而使得线性模型能够处理非线性数据。常用的核函数包括，径向基核函数 (radial basis function kernel, RBF kernel)，也叫高斯核函数，多项式核 (polynomial kernel)，Sigmoid 核 (Sigmoid kernel)。我们在本书第32 章讲解支持向量机 (Support Vector Machine, SVM) 还会用到核技巧。本书不展开讲解核主成分分析。

下面，我们还是利用本书前文用过的利率数据，用几何视角 (投影、旋转) 和Scikit-Learn 函数，和大家分别聊聊两特征、三特征主成分分析。

## 31.2 两特征PCA

首先还是导入利率数据。这部分内容大家已经在本书前文用过，下面简单介绍。

a 中，pandas_datareader 是一个用于从各种数据源中获取金融和经济数据的 Python 库。大家在使用前，需要用pip install pandas_datareader 安装库，大家可以回顾本书第1 章如何安装库。

通常，pandas_datareader 用于从互联网上的各种金融数据提供商获取数据，例如股票市场数据、货币汇率、股票指数、债券价格等。类似前文，如b ，我们下文利用pandas_datareader 从FRED 下载半年期、一年期利率历史数据。

c 修改数据帧列标题。d 计算利率日收益率。e 删除数据帧的缺失值。f 对数据进行标准化。

Page 8  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import pandas as pd import numpy as np import matplotlib.pyplot as plt from sklearn.preprocessing import StandardScaler import pandas_datareader as pdr # 需要先安装库 pip install pandas_datareader import seaborn as sns # 下载数据，两个 tenors df = pdr.data.DataReader(['DGS6MO','DGS1'], data_source='fred', start='01-01-2022', end='12-31-2022')

df = df.dropna()

# 修改数据帧的column names df = df.rename(columns={'DGS6MO': 'X1', 'DGS1': 'X2'})

# 计算日收益率 X_df = df.pct_change()

# 删除缺失值 X_df = X_df.dropna()

# 数据标准化 scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_df)

b a e f

图 8. 导入利率历史数据，代码

图 9 所示为标准化数据的散点图。在这幅图上，我们还用椭圆代表数据的分布；更准确地说，这些椭圆代表了数据的协方差矩阵。这些椭圆等高线实际上是马氏距离 (Mahalanobis distance)。与欧氏距离 (Euclidean distance) 不同，马氏距离考虑了数据之间的协方差结构，因此可以更准确地捕捉数据的相关性和分布情况。图 9 这些同心椭圆就是马氏距离的等距线。

Page 9  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X2, standardized X1, standardized

图 9. 标准化数据的散点图

a 从 Scikit-Learn 机器学习库中导入 EmpiricalCovariance 类。这个类是 Scikit-Learn 中用于计算数据集的经验协方差矩阵。

b 生成网格化数据，用来可视化马氏距离等高线。

c 中用EmpiricalCovariance 的fit 方法接受标准化数据集 X_scaled 作为参数，并使用这个数据集来拟合估计器，从而计算出协方差矩阵。然后，大家可以用COV.covariance_获得协方差矩阵的具体值。

大家会发现，协方差矩阵对角线元素均为1，请大家思考为什么？

d 根据样本协方差矩阵计算网格化数据的马氏距离平方值。这里需要大家格外注意，网格数据点应该与原始数据集 X_scaled 具有相同的特征维度 (两列)。这就是为什么我们需要用e 调整马数组形状， 以便后续可视化。

此外，大家需要注意，输出的结果为马氏距离的平方。f 开平方后获得马氏距离。

g 绘制马氏距离填充等高线。大家会发现这些等高线都是椭圆，而且椭圆的半长轴和横轴夹角为 45 度。大家需要《矩阵力量》《统计至简》的数学工具才能理解为什么夹角为45 度。

h 用散点可视化标准化样本数据。这些样本数据的质心位于原点 (0, 0)。

Page 10  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sklearn.covariance import EmpiricalCovariance x1_array = np.linspace(-6,6,601)

x2_array = np.linspace(-6,6,601)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

xx12 = np.c_[xx1.ravel(), xx2.ravel()]

# 加载学习样本数据 COV = EmpiricalCovariance().fit(X_scaled)

# 计算网格化数据的马氏距离 mahal_sq_Xc = COV.mahalanobis(xx12)

mahal_sq_dd = mahal_sq_Xc.reshape(xx1.shape)

mahal_dd = np.sqrt(mahal_sq_dd)

fig, ax = plt.subplots()

# 绘制马氏距离填充等高线 plt.contourf(xx1, xx2, mahal_dd, cmap='Blues_r', levels=np.linspace(0,6,13))

# 绘制样本数据 (标准化) 散点图 plt.scatter(X_scaled[:,0],X_scaled[:,1], s = 38, edgecolor = 'w', alpha = 0.5, marker = '.', color = 'k')

# 绘制样本数据质心 plt.plot(X_scaled[:,0].mean(),X_scaled[:,1].mean(), marker = 'x', color = 'k', markersize = 18)

ax.axvline(x = 0, c = 'k'); ax.axhline(y = 0, c = 'k')

ax.grid('off'); ax.set_aspect('equal', adjustable='box')

ax.set_xbound(lower = -6, upper = 6)

ax.set_ybound(lower = -6, upper = 6)

b a e f g h Σ

图 10. 马氏距离等高线，使用时配合前文代码

下面利用Scikit-Learn 中的主成分分析工具完成样本数据的PCA 分析。

a 从Scikit-learn 库中导入PCA (Principal Component Analysis) 类。

b 创建了一个PCA 对象的实例，并且指定了降维后的维度为2。本例中，样本数据的特征数 (维度)

为2，PCA 分析前后后维度不变。

c 在PCA 对象上拟合 (训练) 样本数据。这个过程会计算数据的协方差矩阵，然后找到主成分方向。

d 用属性components_获得PCA 主成分的载荷 (loadings)，这个矩阵的每一行代表一个主成分方向。矩阵经过转置 (transpose) 后，每一列代表一个主成分。本书前文提过，这些主成分向量是本质上是原始特征数据的线性组合。我们把这个转置后的矩阵记做V。

e 计算VT @ V，大家可以发现结果近似为2 × 2 单位矩阵 (identity matrix) I。

f 计算V @ VT，可以发现结果同样近似为2 × 2 单位矩阵I。满足以上两个条件的矩阵V 叫做正交矩阵 (orthogonal matrix)，这是《矩阵力量》要讲解的重要概念之一。

g 取出矩阵V 的第1 列v1，即第一主成分方向。h 取出矩阵V 的第2 列v2，即第二主成分方向。

Page 11  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sklearn.decomposition import PCA # 主成分分析 # 主成分数量设定为2 pca = PCA(n_components=2)

# 拟合PCA模型 pca.fit(X_scaled)

# 获取loadings（主成分方向向量）

loadings = pca.components_.T V = loadings print(np.round(V.T @ V))

print(np.round(V @ V.T))

v1 = V[:,[0]] # 第一主成分方向 v2 = V[:,[1]] # 第二主成分方向 b a e f g h v1 v2 X1 X2 PC1 PC2 V v1 X1 X2 PC1 v2 X1 X2 PC2 V VT @ = I = I V VT @

图 11. 主成分分析，使用时配合前文代码

图 12 展示了数据的主成分方向。容易发现，v1对应椭圆的长轴方向，v2对应椭圆的短轴方向。图 13 在前文可视化基础上又可视化了两个主成分方向。

X2, standardized X1, standardized v1 v2 X1 X2 PC1 PC2 v1 v2 V v1 X1 X2 PC1 v2 X1 X2 PC2

图 12. 主成分方向

Page 12  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com # 自定义绘制向量函数 def draw_vector(vector,RBG): array = np.array([[0, 0, vector[0], vector[1]]], dtype=object)

X, Y, U, V = zip(*array)

plt.quiver(X, Y, U, V,angles='xy', scale_units='xy',scale=1,color = RBG, zorder = 1e5)

fig, ax = plt.subplots()

# 绘制马氏距离等高线 plt.contourf(xx1, xx2, mahal_dd, cmap='Blues_r', levels=np.linspace(0,6,13))

# 绘制标准化数据散点图 plt.scatter(X_scaled[:,0],X_scaled[:,1], s = 38, edgecolor = 'w', alpha = 0.5, marker = '.', color = 'k')

# 绘制质心 plt.plot(X_scaled[:,0].mean(),X_scaled[:,1].mean(), marker = 'x', color = 'k', markersize = 18)

# 可视化两个主成分方向 draw_vector(v1,'r')

draw_vector(v2,'r')

# 绘制两条参考线 ax.plot(x1_array,x1_array*v1[1]/v1[0], 'r', lw = 0.25, ls = 'dashed')

ax.plot(x1_array,x1_array*v2[1]/v2[0], 'r', lw = 0.25, ls = 'dashed')

ax.axvline(x = 0, c = 'k'); ax.axhline(y = 0, c = 'k')

ax.grid('off')

ax.set_aspect('equal', adjustable='box')

ax.set_xbound(lower = -6, upper = 6)

ax.set_ybound(lower = -6, upper = 6)

b a e f g

图 13. 绘制主成分方向，使用时配合前文代码

图 14 所示为数据朝第一主成分方向v1投影的结果。根据前文介绍的内容，大家应该清楚朝v1投影的得到结果的方差最大。图 15 所示为数据朝第一主成分方向v2投影的结果，对应方差最小。

[v1, v2] 本身也是一个直角坐标系，在 [v1, v2] 中看到的数据如图 16 所示。绘制这三幅图的代码，请大家参考本章配套文件。

Page 13  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com X2, standardized X1, standardized Project Project

图 14. 朝第一主成分方向投影 X2, standardized X1, standardized Project Project

图 15. 朝第二主成分方向投影

Page 14  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com PC2 PC1

图 16. [v1, v2] 中看数据散点

## 31.4 三特征PCA

既然，我们可以用一个旋转椭圆代替二维散点图；这一节，我们则把三维散点抽象成一个椭球。

图 17 所示为在直角坐标系 [e1, e2, e3] 中看椭球。显然这是一个旋转椭球。红色箭头v1、绿色箭头 v2、蓝色箭头v3分别指向了椭球的三个主轴方向。这三个方向也就是主成分分析中三个主成分方向。

主成分分解得到的载荷矩阵V 的每一个列依次对应红色箭头v1、绿色箭头v2、蓝色箭头v3。[v1, v2, v3] 也是一个三维直角坐标系。数据在v1上投影结果的方差最大，在v2上投影结果的方差次之，在v3上投影结果的方差最小。

图 18 所示为在平面直角坐标系 [e1, e2] 中看椭球。也就是说，椭球在 [e1, e2] 投影为旋转椭圆。图 18 这个椭圆就是图 9 中马氏距离为1 的椭圆。

图 18 还展示了红色箭头v1、绿色箭头v2、蓝色箭头v3在 [e1, e2] 中的投影。

图 19 所示为在平面直角坐标系 [e1, e3] 中看椭球。

图 20 所示为在平面直角坐标系 [e2, e3] 中看椭球。

鸢尾花书《可视之美》将专门介绍这种可视化方案。

Page 15  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 2.0 1.0 0.0 1.0 2.0 2.0 1.0 0.0 1.0 2.0 2.0 1.0 0.0 1.0 2.0 v1 v2 v3 e1 e2 e3 e1 e2 e3 X3, standardized

图 17. [e1, e2, e3] 中看椭球 1.0 v1 v2 v3 e1 e2 X1, standardized X2, standardized 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0

图 18. [e1, e2] 中看椭球

Page 16  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com v1 v2 v3 e1 e3 X1, standardized 1.0 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0 X3, standardized

图 19. [e1, e3] 中看椭球 v1 v2 v3 e2 e3 X2, standardized 1.0 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0 X3, standardized

图 20. [e2, e3] 中看椭球由于 [v1, v2, v3] 也是一个三维直角坐标系，我们当然也可以在 [v1, v2, v3] 中观察椭球。如图 21 所示，在 [v1, v2, v3] 中，我们看的是正椭球。这幅图中，我们还看到了 [e1, e2, e3]。图 22 所示为在 [v1, v2] 中看椭球；而e1、e2、e3在 [v1, v2]，即第一、第二主成分方向，中的投影也叫双标图 (biplot)。双标图可以用于可视化原始多维数据在主成分分析下的投影降维结果。

图 23 所示为在 [v1, v3] 中看椭球。图 24 所示为在 [v2, v3] 中看椭球。

Page 17  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com v1 v2 v3 e1 e2 e3 2.0 1.0 0.0 1.0 2.0 2.0 1.0 0.0 1.0 2.0 2.0 1.0 0.0 1.0 2.0 v1 v2 v3 PC3

图 21. [v1, v2, v3] 中看椭球 e1 e2 e3 1.0 v1 v2 PC1 PC2 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0

图 22. [v1, v2] 中看椭球

Page 18  |  Chapter 31 Scikit-Learn 降维  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

e1 e2 e3 v1 v3 PC1 1.0 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0 PC3

图 23. [v1, v3] 中看椭球

e1 e2 e3 v2 v3 PC2 1.0 2.0 0.0 1.0 2.0 1.0 2.0 0.0 1.0 2.0 PC3

图 24. [v2, v3] 中看椭球

Page 1  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Classification Methods in Scikit-Learn Scikit-Learn 分类 k 最近邻、朴素贝叶斯、支持向量机、核技巧

错误，是进步的代价。

Error is the price we pay for progress.

—— 阿尔弗雷德·怀特海 (Alfred Whitehead)  |  英国数学家、哲学家  |  1861 ~ 1947

◄ matplotlib.colors.ListedColormap() 创建离散颜色映射的函数。函数接受一个颜色列表作为输入，并生成一个离散的颜色映射对象，用于在可视化中区分不同的类别或数据值 ◄ sklearn.datasets.load_iris() 加载鸢尾花数据 ◄ sklearn.naive_bayes.GaussianNB() 实现高斯朴素贝叶斯分类器算法 ◄ sklearn.neighbors.KNeighborsClassifier() 实现k 最近邻分类器算法 ◄ sklearn.svm.SVC() 实现支持向量机分类器算法

Page 2  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 32.1 什么是分类？

本书前文介绍过，分类 (classification) 是有监督学习 (supervised learning) 中的一类问题。分类是指根据给定的数据集，通过对样本数据的学习，建立分类模型来对新的数据进行分类的过程。

如图 1 所示，大家已经清楚鸢尾花数据集分三类 (setosa ●、versicolor ●、virginica ●)。以花萼长度 (sepal length)、花萼宽度 (sepal width) 作为特征，大家如果采到一朵鸢尾花，花萼长度为6.5 厘米，花瓣长度为4.0 厘米。图 1 中 × 又叫查询点 (query point)。

根据已有数据，猜测这朵鸢尾花属于setosa ●、versicolor ●、virginica ●三类的哪一类可能性性更大，这就是分类问题。

Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

Sepal width (cm)

Sepal length (cm)

图 1. 用鸢尾花数据介绍分类算法

决策边界 (decision boundary) 是分类模型在特征空间中划分不同类别的分界线或边界。通俗地说， 决策边界就像是一道看不见的墙，把不同类别的数据点分隔开。

Page 3  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 对于鸢尾花数据集，决策边界就是将setosa ●、versicolor ●、virginica ● 这三类点“尽可能准确地”区分开的线或曲线。大家会在本章中看到，为了获得不同算法的决策边界，我们一般会用numpy.meshgrid()

生成一系列均匀网格数据，然后再分别预测每个网格点的分类，以此划定决策边界。

在简单的情况下，决策边界可能是一条直线；但在复杂的问题中，决策边界可能是一条弯曲的曲线，甚至是多维空间中的超平面。

模型训练过程就是调整模型的参数，使得决策边界能够最好地拟合训练数据，并且在未见过的数据上也能表现良好。

要注意的是，决策边界的好坏直接影响分类模型的性能。一个良好的决策边界能够很好地将数据分类，而一个不合适的决策边界可能导致模型预测错误。因此，选择合适的分类算法和调整模型参数是非常重要的，以获得有效的决策边界和准确的分类结果。

下面我们就用最通俗的语言，以几乎没有数学公式的方式，介绍几种常用分类算法。

## 32.2 k 最近邻分类

k 最近邻分类 (k-nearest neighbors)，简称kNN。

kNN 思路很简单——“近朱者赤，近墨者黑”。更准确地说，小范围投票，少数服从多数 (majority rule)，如图 2 所示。k 是参与投票的最近邻的数量，k 为用户输入值。

Neighborhood

图 2. k 近邻分类核心思想——小范围投票，少数服从多数

最近邻数量k 直接影响查询点分类结果；因此，选取合适k 值格外重要。

图 3 所示为k 取四个不同值时，查询点 × 预测分类结果变化情况。如图 3 (a) 所示，当 k = 4 时，查询点 × 近邻中，3 个近邻为 ● (C1)，1 个近邻为 ● (C2)；采用等权重投票，查询点 × 预测分类为● (C1)。

当近邻数量k 提高到8 时，近邻社区中，4 个近邻为 ● (C1)，4 个近邻为 ● (C2)，如图 3 (b) 所示；等权重投票的话，两个标签各占50%。因此k = 8 时，查询点 × 恰好在决策边界上。

Page 4  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 如图 3 (c) 所示，当 k = 12 时，查询点 × 近邻中5 个为 ● (C1)，7 个为 ● (C2)；等权重投票条件下， 查询点 × 预测标签为 ● (C2)。当 k = 16 时，如图 3 (c) 所示，查询点 × 预测标签同样为 ● (C2)。

k-NN 算法选取较小的k 值虽然能准确捕捉训练数据的分类模式；但是，缺点也很明显，容易受到噪声影响。

鸢尾花书《机器学习》会专门介绍k-NN 算法。

(a) k = 4;   C1 (3/4, 75%);    C2 (1/4, 25%)

(b) k = 8;   C1 (4/8, 50%);    C2 (4/8, 50%)

(c) k = 12;   C1 (5/12, 41.67%);    C2 (7/12, 58.33%)

(d) k = 16;   C1 (6/16, 37.5%);    C2 (10/16, 62.5%)

Neighborhood, k = 4 Neighborhood, k = 8 Neighborhood, k = 12 Neighborhood, k = 16 Query point, q

图 3. 近邻数量k 值影响查询点的分类结果

图 4 所示为利用kNN 算法确定的鸢尾花数据决策区域和决策边界。

图 5 为对应的代码。下面介绍其中重要的语句。

Page 5  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com setosa versicolor virginica 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

图 4. 根据花萼长度、花萼宽度，用k-NN 算法确定决策边界 a 利用sklearn.datasets.load_iris() 加载了鸢尾花数据集。本书前文介绍过，在scikit-learn 中， datasets 模块提供了一些经典的示例数据集。b 提取了鸢尾花数据集的前两列——花萼长度、花萼宽度 ——作为分类特征。c 提取鸢尾花分类标签。

d 用numpy.meshgrid() 生成网格化数据，这些就是用来预测分类的查询点。

e 用matplotlib.colors.ListedColormap() 创建离散色谱，即颜色映射，展示鸢尾花预测分类的区域。

f 用sklearn.neighbors.KNeighborsClassifier(k_neighbors) 创建了一个k 最近邻分类器对象kNN，并将k_neighbors 作为参数传递给这个分类器。这里的k_neighbors 指定了算法中要使用的最近邻居数量。

g 这行代码用训练数据X 和相应的标签y 来训练k 最近邻分类器kNN。在训练过程中，分类器会学习如何根据特征向量X 将其分配到相应的标签y 上。

h 利用numpy.c_() 将两个一维数组按列合并，形成一个新的二维数组，即查询点。numpy.ravel() 函数将二维数组展平成一维数组。

i 这行代码用之前训练好的k 最近邻分类器kNN 对查询点进行预测，得到预测的标签y_predict。

j 利用numpy.reshape() 将预测的标签y_predict 调整为与xx1 相同形状，以便后续可视化。

k 利用matplotlib.pyplot.contourf() 绘制分类区域。l 利用matplotlib.pyplot.contour() 绘制分类决策边界。m 利用seaborn.scatterplot() 绘制散点图展示鸢尾花数据集。

Page 6  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import numpy as np import matplotlib.pyplot as plt import seaborn as sns from matplotlib.colors import ListedColormap from sklearn import neighbors, datasets # 导入并整理数据 iris = datasets.load_iris()

X = iris.data[:, :2]

y = iris.target # 生成网格化数据 x1_array = np.linspace(4,8,101)

x2_array = np.linspace(1,5,101)

xx1, xx2 = np.meshgrid(x1_array,x2_array)

# 创建色谱 rgb = [[255, 238, 255], [219, 238, 244], [228, 228, 228]]

rgb = np.array(rgb)/255.

cmap_light = ListedColormap(rgb)

cmap_bold = [[255, 51, 0], [0, 153, 255], [138,138,138]]

cmap_bold = np.array(cmap_bold)/255.

k_neighbors = 4 # 定义kNN近邻数量k # 创建kNN分类器对象 kNN = neighbors.KNeighborsClassifier(k_neighbors)

kNN.fit(X, y) # 用训练数据训练kNN q = np.c_[xx1.ravel(), xx2.ravel()]

# 用kNN对一系列查询点进行预测 y_predict = kNN.predict(q)

y_predict = y_predict.reshape(xx1.shape)

# 可视化 fig, ax = plt.subplots()

plt.contourf(xx1, xx2, y_predict, cmap=cmap_light)

plt.contour(xx1, xx2, y_predict, levels=[0,1,2], colors=np.array([0, 68, 138])/255.)

sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y], ax = ax, palette=dict(setosa=cmap_bold[0,:], versicolor=cmap_bold[1,:], virginica=cmap_bold[2,:]), alpha=1.0, linewidth = 1, edgecolor=[1,1,1])

plt.xlim(4, 8); plt.ylim(1, 5)

plt.xlabel(iris.feature_names[0])

plt.ylabel(iris.feature_names[1])

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

ax.set_aspect('equal', adjustable='box')

a f k b e g h j R G B

图 5. 根据花萼长度、花萼宽度，用k-NN 算法确定决策边界，代码

Page 7  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 32.3 高斯朴素贝叶斯分类

高斯朴素贝叶斯分类 (Gaussian Naive Bayes, GNB) 是一种基于贝叶斯定理 (Bayes' theorem) 的分类算法。

什么是贝叶斯定理？

贝叶斯定理是一种概率论中用于计算条件概率的重要公式。它描述了在已知某个条件下，另一事件发生的概率。根据贝叶斯定理，我们可以通过已知的先验概率和条件概率，来计算更新后的后验概率。这个定理在统计学、机器学习和人工智能等领域广泛应用，尤其在贝叶斯推断和贝叶斯分类中起着重要作用。

贝叶斯定理、贝叶斯分类、贝叶斯推断中有两个重要概念——先验概率 (prior probability)、后验概率 (posterior probability)。

先验概率是指在考虑任何新证据之前，我们对一个事件或假设的概率的初始估计。它基于以前的经验、先前的观察或领域知识。这种概率是“先验”的，因为它不考虑新数据或新证据，只是基于我们事先已经了解的信息。先验概率可以帮助我们在没有新数据时做出初步的估计。

假设我们要研究某地区的流感发病率。在流感季节之前，我们可能会查阅历史数据、了解流感传播的模式以及人口的健康状况，从而得出在流感季节中某人患上流感的初始估计概率，这就是先验概率。

后验概率是指在考虑了新证据或数据后，我们对一个事件或假设的概率进行更新后的估计。在得到新的信息后，我们根据贝叶斯定理来更新先验概率，以得到后验概率。贝叶斯定理将先验概率和新的证据结合起来，提供了一个更准确的概率估计。

在流感季节中，我们开始收集实际发病数据，比如每天有多少人确诊患上流感。根据这些新数据， 我们可以使用贝叶斯定理来更新先前的先验概率，得到一个更准确的后验概率，以更好地预测未来发病率或做出相关决策。

图 6 所示为高斯朴素贝叶斯分类的流程图。

高斯朴素贝叶斯分类假设每个特征在给定类别下是条件独立的，即给定类别的情况下，每个特征与其他特征之间条件独立。这便是高斯朴素贝叶斯分类中“朴素”两个字的来由。然后，将每个类别的特征分布建模为高斯分布，这则是高斯朴素贝叶斯分类中“高斯”两个字的来由。

以图 6 为例，给定标签为C1 (红色点)，分别独立获得fX1|Y(x1 | C1) 和 fX2|Y(x2 | C1)。假设条件独立， fY,X1,X2(C1, x1, x2) = pY(C1)·fX1|Y(x1 | C1)·fX2|Y(x2 | C1)。

大家如果对上述内容有疑惑的话，请参考鸢尾花书《统计至简》第18、19 章。

在训练时，算法从训练数据中学习每个类别的各个特征的 (条件) 均值和方差，用于计算每个特征在该类别下的概率密度函数。

当有新的未标记样本输入时，算法将计算该样本在每个类别下的条件概率 (后验概率)，并选择具有最高概率的类别作为预测结果。

高斯朴素贝叶斯分类算法的优点是简单快速、易于实现和适用于高维数据。它还能够处理连续型数据，因为它假设数据分布是高斯分布。

Page 8  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com fX1|Y(x1 | C1)

C1 C2 C3 pY(C1)

pY(C2)

pY(C3)

Training data fX2|Y(x2 | C1)

fY,X1,X2(C1, x1, x2)

fY,X1,X2(C3, x1, x2)

fY,X1,X2(C1, x1, x2) = pY(C1)·fX1|Y(x1 | C1)·fX2|Y(x2 | C1)

fY,X1,X2(C2, x1, x2) = pY(C2)·fX1|Y(x1 | C2)·fX2|Y(x2 | C2)

fY,X1,X2(C3, x1, x2) = pY(C3)·fX1|Y(x1 | C3)·fX2|Y(x2 | C3)

fX1|Y(x1 | C2)

fX2|Y(x2 | C2)

fY,X1,X2(C2, x1, x2)

fX1|Y(x1 | C3)

fX2|Y(x2 | C3)

图 6. 高斯朴素贝叶斯分类过程

图 7 所示为利用高斯朴素贝叶斯分类算法获得的决策边界。图 8 所示为高斯朴素贝叶斯分类算法部分代码，请大家用图 8 替换图 5 对应语句。

Page 9  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com setosa versicolor virginica 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

图 7. 根据花萼长度、花萼宽度，用高斯朴素贝叶斯算法确定决策边界

a b from sklearn.naive_bayes import GaussianNB # 创建高斯朴素贝叶斯分类器对象 gnb = GaussianNB()

# 用训练数据训练kNN gnb.fit(X, y)

# 用高斯朴素贝叶斯分类器对一系列查询点进行预测 y_predict = gnb.predict(q)

图 8. 用高斯朴素贝叶斯算法确定决策边界，部分代码

## 32.4 支持向量机

图 9 所示为支持向量机 (Support Vector Machine, SVM) 核心思路。

如图 9 所示，一片湖面左右散布着蓝色 ● 红色 ● 礁石，游戏规则是，皮划艇以直线路径穿越水道， 保证船身恰好紧贴礁石。寻找一条路径，让该路径通过的皮划艇宽度最大。很明显，图 9 (b) 中规划的路径好于图 9 (a)。

图 9 (b) 中加黑圈 ○ 的五个点，就是所谓的支持向量 (support vector)。

Page 10  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 9 中深蓝色线，便是决策边界，也称分离超平面 (separating hyperplane)。特别提醒大家注意一点， 加黑圈 ○ 支持向量确定决策边界位置；其他数据并没有起到任何作用。因此，SVM 对于数据特征数量远高于数据样本量的情况也有效。

图 9 中两条虚线之间宽度叫做间隔 (margin)。支持向量机的优化目标为——间隔最大化。

(a)

(b)

Class 1, C1         Class 2, C2

图 9. 支持向量机原理

从数据角度，图 9 两类数据用一条直线便可以分割开来，这种数据叫做线性可分 (linearly separable)。线性可分问题采用硬间隔 (hard margin)；白话说，硬间隔指的是，间隔内没有数据点。

实践中，并不是所有数据都是线性可分。多数时候，数据线性不可分 (non-linearly separable)。如图 10 所示，不能找到一条直线将蓝色 ● 红色 ● 数据分离。

对于线性不可分问题，就要引入两种方法——软间隔 (soft margin) 和核技巧 (kernel trick)。

Page 11  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Class 1, C1         Class 2, C2

图 10. 线性不可分数据

白话说，如图 11 所示，软间隔相当于一个缓冲区 (buffer zone)。软间隔存在时，用决策边界分离数据时，有数据点侵入间隔，甚至超越间隔带。

Class 1, C1         Class 2, C2 图 11. 软间隔

Page 12  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 图 12 所示用支持向量机确定的决策边界。图 13 为支持向量机 (线性核) 算法部分代码，请大家用图 13 替换图 5 对应语句。线性核是SVM 中最简单的核函数之一。它适用于处理线性可分的数据集，即可以通过一个直线 (在二维空间中) 或一个超平面 (在高维空间中) 将不同类别的样本点分开。

setosa versicolor virginica 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

图 12. 根据花萼长度、花萼宽度，用支持向量机 (线性核，默认) 算法确定决策边界

a b from sklearn import svm # 创建支持向量机 (线性核) 分类器对象 SVM = svm.SVC(kernel='linear')

# 用训练数据训练kNN SVM.fit(X, y)

# 用支持向量机 (线性核) 分类器对一系列查询点进行预测 y_predict = SVM.predict(q)

图 13. 用支持向量机 (线性核，默认) 算法确定决策边界，部分代码

## 32.5 核技巧

核技巧将数据映射到高维特征空间，相当于数据升维。如图 14 所示，样本数据有两个特征，用平面可视化数据点位置。很明显图 14 给出的原始数据线性不可分。

Page 13  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 采用核技巧，将图 14 二维数据，投射到三维核曲面上；很明显，在这个高维特征空间，容易找到某个水平面，将蓝色 ● 红色 ● 数据分离。利用核技巧，分离线性不可分数据变得更容易。

通常，采用支持向量机解决线性不可分问题，需要并用软间隔和核技巧。如图 15 所示，SVM 分类环形数据中，核技巧配合软间隔。

Intersection curve (decision boundary)

Kernel surface Class 1, C1         Class 2, C2 Decision hyperplane Original data Mapped to kernel surface

图 14. 核技巧原理

Class 1, C1         Class 2, C2 Original data Decision boundary Contour of kernel surface Mapped to kernel surface

图 15. 核技巧配合软间隔

Page 14  |  Chapter 32 Scikit-Learn 分类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 高斯核，也称为径向基核 (Radial Basis Function Kernel)，是SVM 中常用的非线性核函数。它能够将数据映射到无穷维的特征空间，从而在低维空间中不可分的数据变得线性可分。

setosa versicolor virginica 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

图 16. 根据花萼长度、花萼宽度，用支持向量机 (高斯核) 算法确定决策边界

a b from sklearn import svm # 创建支持向量机 (高斯核) 分类器对象 SVM = svm.SVC(kernel='rbf', gamma= 'auto')

# 用训练数据训练kNN SVM.fit(X, y)

# 用支持向量机 (线性核) 分类器对一系列查询点进行预测 y_predict = SVM.predict(q)

图 17. 用支持向量机 (高斯核，默认) 算法确定决策边界，部分代码

Page 1  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Clustering Methods in Scikit-Learn Scikit-Learn 聚类 K 均聚类、四种高斯混合GMM 聚类

只有想象力无界的人，方能开创不可能的事。

Those who can imagine anything, can create the impossible.

—— 艾伦·图灵 (Alan Turing)  |  英国计算机科学家、数学家，人工智能之父  |  1912 ~ 1954

◄ matplotlib.patches.Ellipse() 创建并绘制椭圆形状的图形对象 ◄ matplotlib.pyplot.quiver() 绘制向量箭头 ◄ numpy.arctan2() 计算反正切，返回弧度值 ◄ numpy.linalg.svd() 完成奇异值分解 ◄ numpy.sqrt() 计算平方根 ◄ sklearn.cluster.KMeans() 执行K 均值聚类算法，将数据点划分成预定数量的簇 ◄ sklearn.mixture.GaussianMixture() 用于拟合高斯混合模型，以对数据进行聚类和概率密度估计

Page 2  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 33.1 聚类

本书前文介绍过，聚类 (clustering) 是无监督学习 (unsupervised learning) 中的一类问题。

聚类是指将数据集中的样本按照某种相似性指标进行分组的过程。常用的聚类算法包括。

如图 1 所示，删除鸢尾花数据集的标签，即target，仅仅根据鸢尾花花萼长度 (sepal length)、花萼宽度 (sepal width) 这两个特征上样本数据分布情况，我们可以将数据分成两簇 (clusters)。

在机器学习中，决定将数据分成多少个簇是一个重要而且有挑战性的问题，通常称为聚类数目的选择或者簇数选择。不同的聚类算法可能需要不同的方法来确定合适的聚类数目。本章后文在介绍具体算法时，会介绍如何选择合适的簇数。

Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

图 1. 用删除标签的鸢尾花数据介绍聚类算法

大家在使用Scikit-Learn 聚类算法时，会发现有些算法有predict() 方法。也就是说，如图 2 所示，已经训练好的模型，有可能你将全新的数据点分配到确定的簇中。有这种功能的聚类算法叫做归纳聚类 (inductive clustering)。本章后文要介绍的k 均值聚类、高斯混合模型都属于归纳聚类。如图 2 所示，归纳聚类算法也有决策边界。这就意味着归纳聚类模型具有一定的泛化能力，可以推广到新的、之前未见过的数据。

不具备这种能力的聚类算法叫做非归纳聚类 (non-inductive clustering)。

非归纳聚类只能对训练数据进行聚类，而不能将新数据点添加到已有的模型中进行预测。这意味着模型在训练时只能学习训练数据的模式，无法用于对新数据点进行簇分配。比如，层次聚类、DBSCAN 聚类都是非归纳聚类。

归纳聚类强调模型的泛化能力，可以适应新数据，而非归纳聚类则更侧重于建模训练数据内部的结构。

Page 3  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length (cm)

Sepal width (cm)

Sepal length (cm)

Sepal width (cm)

图 2. 归纳聚类算法

下面我们就用最通俗的语言，以几乎没有数学公式的方式，介绍几种常用聚类算法。

## 33.2 K 均值聚类

K 均值算法 (K-Means) 将样本分为 K 个簇，使得每个数据点与其所属簇的中心 (也叫质心 (centroid))

之间的距离最小化。一般情况，每个簇的中心点是该簇中所有样本点的平均值。

图 3 以二聚类为例，展示K 均值聚类的操作流程。从样本数据开始，首先从样本中随机选取2 个数据作为均值向量μ1和μ2的初始值，然后进入如下迭代循环。

a) 计算每一个样本点分别到均值向量μ1和μ2的距离； b) 比较每个样本到μ1和μ2距离，确定簇的划分； c) 根据当前簇，重新计算并更新均值向量μ1和μ2。

直到均值向量μ1和μ2满足迭代停止条件，得到最终的簇划分。

图 4 所示为利用K 均值算法根据鸢尾花花萼长度、花萼宽度特征划分为2 和3 簇两种情况。

根据前文介绍的内容，我们知道K 均值算法为归纳聚类算法；因此，如图 4 所示，K 均值算法可以用训练好的模型预测其他新样本数据的聚类，从而获得聚类决策边界。容易发现K 均值聚类算法决策边界为直线段。图 4 中的 × 为K 均值算法的簇质心。

图 5 代码绘制图 4 两幅子图，下面聊聊其中关键语句。

a 从sklearn.cluster 模块导入K 均值算法对象KMeans。请大家注意变量大小写。

b 加载经典鸢尾花数据集。在聚类算法中，我们仅仅用到鸢尾花的特征数据 (data)，不会用到标签数据 (target)。c 提取鸢尾花数据中的前两个特征 (花萼长度、花萼宽度) 数据。

d 利用matplotlib.colors.ListedColormap 创建离散颜色映射，以在图表中对不同的离散值进行颜色编码。颜色映射在本例中可视化鸢尾花聚类区域。

e 实例化了一个KMeans 对象，并指定了要进行的聚类数目。参数n_clusters 参数就是用来指定K 均值聚类算法 K 的值，即希望将数据划分成多少个簇。

Page 4  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com f 执行了 KMeans 聚类算法，拟合模型并预测数据点所属的簇标签。fit_predict(X) 同时拟合 (fit) 数据并预测 (prefict) 数据点所属的簇标签。大家也可以用fit(X).predict(X) 来分两步执行。其中，X 是一个二维数组，表示输入的数据，每行代表一个数据样本，每列代表一个特征。请大家自行查看返回结果。

g 利用训练好的KMeans 模型对全新的数据进行聚类预测。h 调整数组形状，用于后续可视化。

i 用填充等高线可视化聚类区域。j 用等高线可视化聚类决策边界。

k 获取 KMeans 聚类算法拟合后得到的聚类质心的坐标。l 用散点可视化聚类质心。

Training data Means initialization a) Calculate distances b) Assign clusters c) Update means Iterations Convergence

图 3. K 均值算法流程图

Page 5  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

4.0 5.0 6.0 7.0 8.0 Sepal length (cm)

5.0 4.0 3.0 2.0 1.0 Sepal width (cm)

(a)

(b)

图 4. K 均值聚类确定决策边界，簇数分别为2、3

Page 6  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com from sklearn import datasets from sklearn.cluster import KMeans import matplotlib.pyplot as plt import numpy as np from matplotlib.colors import ListedColormap # 导入并整理数据 iris = datasets.load_iris()

X = iris.data[:, :2]

# 生成网格化数据 x1_array = np.linspace(4,8,101)

x2_array = np.linspace(1,5,101)

xx1, xx2 = np.meshgrid(x1_array,x2_array)

# 创建色谱 rgb = [[255, 238, 255], [219, 238, 244], [228, 228, 228]]

rgb = np.array(rgb)/255.

cmap_light = ListedColormap(rgb)

# 采用KMeans聚类 kmeans = KMeans(n_clusters=2)

cluster_labels = kmeans.fit_predict(X)

# 预测聚类 Z = kmeans.predict(np.c_[xx1.ravel(), xx2.ravel()])

Z = Z.reshape(xx1.shape)

fig, ax = plt.subplots()

ax.contourf(xx1, xx2, Z, cmap=cmap_light)

ax.scatter(x=X[:, 0], y=X[:, 1], color=np.array([0, 68, 138])/255., alpha=1.0, linewidth = 1, edgecolor=[1,1,1])

# 绘制决策边界 levels = np.unique(Z).tolist(); ax.contour(xx1, xx2, Z, levels=levels,colors='r')

centroids = kmeans.cluster_centers_ ax.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=100, linewidths=1.5, color="r")

ax.set_xlim(4, 8); ax.set_ylim(1, 5)

ax.set_xlabel(iris.feature_names[0])

ax.set_ylabel(iris.feature_names[1])

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

ax.set_aspect('equal', adjustable='box')

a f k b e g h j

图 5. 根据花萼长度、花萼宽度，用K 均值聚类算法确定聚类决策边界，代码

Page 7  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 33.3 高斯混合

高斯混合模型 (Gaussian Mixture Model, GMM) 将样本分为多个高斯分布，每个高斯分布对应一个簇。与K 均值聚类不同，GMM 不仅能够将数据点分配到不同的簇，还可以为每个簇分配一个概率值， 表明数据点属于该簇的可能性。

如图 6 所示，多元高斯分布中，协方差矩阵决定高斯分布的形状。

Identity matrix Equal diagonal entries Unequal diagonal entries Non-diagonal matrix Covariance matrix Diagonal matrix

图 6. 协方差矩阵的形态影响高斯密度函数形状

如表 1 总结，scikit-learn 工具包中sklearn.mixture 高斯混合模型支持四种协方差矩阵——tied (平移)、spherical (球面)、diag (对角)和full (完全)。

tied 指的是，所有分量共享一个非对角协方差矩阵Σ。每个簇对应的多元高斯分布等高线为大小相等旋转椭圆。tied 对应的决策边界为直线。

spherical 指的是，每个分量协方差矩阵Σj (j = 1,2, …, K) 不同，但是每个分量Σj均为对角阵；且 Σj对角元素相同，即特征方差相同。每个簇对应的多元高斯分布等高线为正圆。spherical 对应的决策边界为圆形弧线。

diag 指每个分量有各自独立的对角协方差矩阵，也就是Σj为对角阵，特征条件独立；但是对Σj对角线元素大小不做限制。每个簇对应的多元高斯分布等高线正椭圆，diag 对应的决策边界为正圆锥曲线。

Page 8  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com full 指每个分量有各自独立协方差矩阵，即对Σj不做任何限制。full 对应的决策边界为任意圆锥曲线。

表 1. 根据方差-协方差矩阵特点将高斯混合模型分为4 类参数设置 Σi Σi特点多元高斯分布PDF 等高线决策边界 tied 相同非对角阵任意椭圆直线 spherica 不相同对角阵，对角线元素等值正圆正圆 diag 对角阵正椭圆正圆锥曲线 full 非对角阵任意椭圆圆锥曲线

和K 均值聚类算法一样，高斯混合模型GMM 也需要指定K 值；高斯混合模型也是利用迭代求解优化问题。不同的是，GMM 利用协方差矩阵，可以估算后验概率/成员值。前文提过，GMM 的协方差矩阵有四种类型，每种类型对应不同假设，获得不同决策边界类型。

K 均值聚类可以看作是高斯混合模型一个特例。如图 7 所示，K 均值聚类对应的GMM 特点是，各簇协方差矩阵Σj相同，Σj为对角阵，并且Σj主对角线元素相等。

µ1 µ2 µ3

图 7. K 均值聚类可以看作是高斯混合模型一个特例

图 8 ~ 图 11 所示为利用GMM 聚类鸢尾花数据。这四幅图采用四种不同的协方差矩阵完成GMM 聚类。大家可以通过比较这四幅图的椭圆形状很容易理解表 1。图 12 定义的可视化函数绘制了这四幅图中的椭圆和向量。图 13 是完成GMM 的代码，这段代码调用了图 12 的可视化函数。下面让我们聊聊这两段代码。

Page 9  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

图 8. K 均值聚类，协方差矩阵为 'tied' Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

图 9. K 均值聚类，协方差矩阵为 'spherical' Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

图 10. K 均值聚类，协方差矩阵为 'diag'

Page 10  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Sepal length (cm)

Sepal length (cm)

Sepal width (cm)

Sepal width (cm)

图 11. K 均值聚类，协方差矩阵为 'full' 让我们首先看看图 12 可视化代码。

a 从matplotlib.patches 导入Ellipse 类，Ellipse 用来绘制椭圆形状。

前文提过，GMM 可以有不同的协方差类型，包括 'full'、'tied'、'diag' 和 'spherical'，它们分别表示完整协方差矩阵、共享协方差矩阵、对角协方差矩阵和球状协方差矩阵。

b 这个条件判断语句检查GMM 对象的协方差类型是否为 'full'。根据技术文档，这种情况下，协方差矩阵形状为 (n_components, n_features, n_features)，三维NumPy 数组。其中，axis = 0 对应的是不同簇。也就是说，如图 11 所示，不同簇协方差矩阵不同，gmm.covariances_[j] 提取的是不同簇的协方差矩阵，结果为二维NumPy 数组。

c 判断GMM 对象的协方差类型是否为 'tied'。根据技术文档，这种情况下，协方差矩阵形状为 (n_features, n_features)，二维NumPy 数组。这意味着不同簇的协方差矩阵完全相同，如图 8 所示。

d 判断GMM 对象的协方差类型是否为 'diag'。根据技术文档，这种情况下，协方差矩阵形状为 (n_components, n_features)，二维NumPy 数组。其中，axis = 0 对应的是不同簇，axis = 1 对应的是不同特征的方差。也就是说，如图 10 所示，从GMM 对象的 gmm.covariances_[j] 属性中获取第 j 个分量的协方差矩阵，结果为一维数组；然后，使用 np.diag() 函数将其转换为对角矩阵形式，结果为二维数组。

e 判断GMM 对象的协方差类型是否为 'spherical'。根据技术文档，这种情况下，协方差矩阵形状为 (n_components,)，一维NumPy 数组。其中，axis = 0 对应不同簇。也就是说，如图 9 所示，将单位矩阵的每个维度上的方差都乘以相应的协方差值，从而形成一个球状的协方差矩阵。

f 实际上用奇异值函数numpy.linalg.svd() 完成的是协方差矩阵的特征值分解。这个矩阵分解，可以帮我们了解一个旋转椭圆的半长轴、半短轴的长度，以及椭圆的旋转角度。《矩阵力量》将具体讲解数学工具背后的原理。

g 计算椭圆长轴、短轴的长度。h 计算椭圆旋转角度弧度。

i 绘制GMM 每个簇的质心。

j 使用 Matplotlib 的 quiver 函数来在二维图中绘制箭头，用来表示椭圆长轴方向 (矩阵U 的第1 列)。k 绘制椭圆短轴方向 (矩阵U 的第2 列)。

Page 11  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com l 建了一个椭圆对象，指定了椭圆的中心坐标、长轴宽度、短轴宽度、旋转角度、边缘颜色和填充颜色。然后，我们使用 ax.add_patch() 将椭圆添加到图中。

from matplotlib.patches import Ellipse # 定义可视化函数 def make_ellipses(gmm, ax):

# 可视化不同簇 for j in range(0,K): # 四种不同的协方差矩阵 if gmm.covariance_type == 'full': covariances = gmm.covariances_[j]

elif gmm.covariance_type == 'tied': covariances = gmm.covariances_ elif gmm.covariance_type == 'diag': covariances = np.diag(gmm.covariances_[j])

elif gmm.covariance_type == 'spherical': covariances = np.eye(gmm.means_.shape[1])

covariances = covariances*gmm.covariances_[j]

# 用奇异值分解完成特征值分解 U, S, V_T = np.linalg.svd(covariances)

# 计算长轴、短轴长度 major, minor = 2 * np.sqrt(S)

# 计算椭圆长轴旋转角度 angle = np.arctan2(U[1,0], U[0,0])

angle = 180 * angle / np.pi

# 多元高斯分布中心 ax.plot(gmm.means_[j, 0],gmm.means_[j, 1], color = 'k',marker = 'x',markersize = 10)

# 绘制半长轴向量 ax.quiver(gmm.means_[j,0],gmm.means_[j,1], U[0,0], U[1,0], scale = 5/minor)

# 绘制半短轴向量 ax.quiver(gmm.means_[j,0],gmm.means_[j,1], U[0,1], U[1,1], scale = 5/major)

# 绘制椭圆 for scale in np.array([3, 2, 1]): ell = Ellipse(gmm.means_[j, :2], scale*minor, scale*major, angle, color=rgb[j,:], alpha = 0.18)

ax.add_artist(ell)

a f k b e g h j

图 12. 定义可视化函数图 13 和图 5 代码比较类似。这部分代码请大家自行学习。

Page 12  |  Chapter 33 Scikit-Learn 聚类  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import matplotlib.pyplot as plt from matplotlib.colors import ListedColormap import numpy as np from sklearn import datasets from sklearn.mixture import GaussianMixture # 创建色谱 rgb = [[255, 51, 0], [0, 153, 255], [138,138,138]]

rgb = np.array(rgb)/255.

cmap_bold = ListedColormap(rgb)

# 生成网格化数据 x1_array = np.linspace(4,8,101)

x2_array = np.linspace(1,5,101)

xx1, xx2 = np.meshgrid(x1_array,x2_array)

# 鸢尾花数据 iris = datasets.load_iris(); X = iris.data[:, :2]

K = 3 # 簇数 # 协方差类型 covariance_types = ['tied', 'spherical', 'diag', 'full']

for covariance_type in covariance_types: # 采用GMM聚类 gmm = GaussianMixture(n_components=K, covariance_type=covariance_type)

gmm.fit(X)

Z = gmm.predict(np.c_[xx1.ravel(), xx2.ravel()])

Z = Z.reshape(xx1.shape)

# 可视化 fig = plt.figure(figsize = (10,5))

ax = fig.add_subplot(1,2,1)

ax.scatter(x=X[:, 0], y=X[:, 1], color=np.array([0, 68, 138])/255., alpha=1.0, linewidth = 1, edgecolor=[1,1,1])

# 绘制椭圆和向量 make_ellipses(gmm, ax)

ax.set_xlim(4, 8); ax.set_ylim(1, 5)

ax.set_xlabel(iris.feature_names[0])

ax.set_ylabel(iris.feature_names[1])

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

ax.set_aspect('equal', adjustable='box')

ax = fig.add_subplot(1,2,2)

ax.contourf(xx1, xx2, Z, cmap=cmap_bold, alpha = 0.18)

ax.contour(xx1, xx2, Z, levels=[0,1,2], colors=np.array([0, 68, 138])/255.)

ax.scatter(x=X[:, 0], y=X[:, 1], color=np.array([0, 68, 138])/255., alpha=1.0, linewidth = 1, edgecolor=[1,1,1])

centroids = gmm.means_ ax.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=100, linewidths=1.5, color="k")

ax.set_xlim(4, 8); ax.set_ylim(1, 5)

ax.set_xlabel(iris.feature_names[0])

ax.set_ylabel(iris.feature_names[1])

ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])

ax.set_aspect('equal', adjustable='box')

a b

图 13. GMM 聚类代码，使用时配合前文代码

Page 1  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Know a Bit about Spyder 了解一下Spyder 下一章学习使用Streamlit 时会用到的IDE

舍得浪费一小时的人，绝没发现生命的价值。

A man who dares to waste one hour of time has not discovered the value of life.

—— 查尔斯·达尔文 (Charles Darwin)  |  英国博物学家、地质学家和生物学家  |  1809 ~ 1882

◄ ax.plot_wireframe() 用于在三维子图ax 上绘制网格曲 ◄ fig.add_subplot(projection='3d') 用于在图形对象fig 上添加一个三维子图 ◄ matplotlib.pyplot.figure() 用于创建一个新的图形窗口或画布，用于绘制各种数据可视化图表 ◄ matplotlib.pyplot.grid() 在当前图表中添加网格线 ◄ matplotlib.pyplot.plot() 绘制折线图 ◄ matplotlib.pyplot.scatter() 绘制散点图 ◄ matplotlib.pyplot.subplot() 用于在一个图表中创建一个子图，并指定子图的位置或排列方式 ◄ matplotlib.pyplot.subplots() 创建一个包含多个子图的图表，返回一个包含图表对象和子图对象的元组 ◄ matplotlib.pyplot.xlabel() 设置当前图表x 轴的标签，相当于对于特定轴ax 对象ax.set_xlabel()

◄ matplotlib.pyplot.xlim() 设置当前图表x 轴显示范围，相当于对于特定轴ax 对象ax.set_xlim() 或 ax.set_xbound()

◄ matplotlib.pyplot.xticks() 设置当前图表x 轴刻度位置，相当于对于特定轴ax 对象ax.set_xticks()

◄ matplotlib.pyplot.ylabel() 设置当前图表y 轴的标签，相当于对于特定轴ax 对象ax.set_ylabel()

◄ matplotlib.pyplot.ylim() 设置当前图表y 轴显示范围，相当于对于特定轴ax 对象ax.set_ylim() 或 ax.set_ybound()

◄ matplotlib.pyplot.yticks() 设置当前图表y 轴刻度位置，相当于对于特定轴ax 对象ax.set_yticks()

◄ numpy.arange() 生成一个包含给定范围内等间隔的数值的数组 ◄ numpy.linspace() 生成在指定范围内均匀间隔的数值，并返回一个数组 ◄ numpy.meshgrid() 用于生成多维网格化数据 ◄ seaborn.scatterplot() 绘制散点图

Page 2  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 34.1 啥是Spyder?

Spyder 是一个免费的、开源的科学计算集成开发环境 (IDE)，旨在为Python 编程语言提供高效的开发环境。Spyder 提供了许多实用的功能，例如代码编辑器、变量查看器、调试器、文件浏览器和交互式控制台等。

Spyder 支持许多流行的Python 库和框架，例如NumPy、SciPy、Pandas 和Matplotlib 等，可以帮助开发人员更轻松地进行科学计算和数据分析。

Spyder 的界面设计上参考了 MATLAB，比如变量查看器模仿了 MATLAB 中“工作空间”的功能。熟悉 MATLAB 的读者，很快就能上手 Spyder。Spyder 是许多科学家、研究人员和数据分析师的首选开发环境之一。

对于开发者，建议使用PyCharm，本书不展开介绍。

什么是PyCharm？

PyCharm 是一个由JetBrains 开发的集成开发环境（IDE），专门为Python 编程语言而设计。它是一个商业产品，但也提供了免费的社区版。PyCharm 提供了许多功能，如代码编辑器、调试器、自动代码补全、版本控制系统集成、代码重构和代码质量分析工具等。它还支持许多流行的Python 库和框架，如NumPy、SciPy、Pandas、Django 和Flask 等，可以帮助开发人员更轻松地进行 Web 开发、数据科学和机器学习等任务。PyCharm 还提供了许多高级功能，如Jupyter Notebook 集成、代码自动格式化、代码片段管理、可视化调试器、远程开发等等。这些功能使得PyCharm 成为许多Python 开发人员的首选工具之一。

界面安装Anaconda 后，Spyder 就已经安装好。打开Spyder 后，其界面如图 1 所示，主要包括 (1) 工具栏，(2) 当前文件路径，(3) Python 代码编辑器，(4) 变量显示区，(5) 交互界面。

快捷键Ctrl + N 在 (3) 创建一个新代码文件。

图 1. Spyder 默认界面工具栏 (1) 里包含了众多代码调试工具。代码的编写和修改则显示在Python 代码编辑器，交互界面用于显示代码的运行结果和生成的图片。在变量显示区可以查看当前变量的名称、占用空间和值。若用

Page 3  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 户习惯了使用MATLAB，还可以通过设置View → Windows layouts → MATLAB layout，使得Spyder 的界面接近MATLAB 的界面。

弹窗方式显示图片如果代码运行结果是以图片的方式显示，Spyder 默认显示方式是嵌入在控制台 (console) 中。若用户希望以弹窗的方式来显示图片，则可通过如下操作进行切换。

如图 2 所示，依次点击菜单栏的Tools → Preferences → Ipython console → Graphics → Graphics backend → Automatic。Automatic 对应的是以弹窗方式显示图片，Inline 对应的是图片在控制台中显示。

完成设置后，读者需要重新打开Spyder 才能使得新设置生效。

注意，快捷键 Ctrl + Alt + Shift + P 打开图 2。

图 3 展示以弹窗方式显示图片。

Inline Automatic Qt5 Qt4 Tkinter Automatic

图 2. 调整显示图片的方式

图 3. Spyder 中以弹窗的方式显示图片

图 4 所示为Spyder 图片弹窗的几个操作。(1) 可以用来拖拽二维图像，或旋转三维图像。(2) 可以用来放大图像。紧随其后的两个按钮分别打开图片边距、图片轴等设置。最后一个按钮可以用来手动保存图片，图片保存格式选择很多。

其中，PNG (Portable Network Graphics) 是一种无损压缩的位图图像格式，支持透明背景。JPG (Joint Photographic Experts Group) 是一种有损压缩的位图图像格式，对于彩色照片效果较好，但不支持透明背

Page 4  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 景。SVG (Scalable Vector Graphics) 是一种基于XML 的矢量图像格式，支持无损放大缩小。PDF (Portable Document Format)、EPS (Encapsulated PostScript) 也是矢量图像格式鸢尾花书中最常用的图片格式为SVG。

图 4. Spyder 图片弹窗的几个操作代码编辑器样式 Spyder 中的字体样式、大小和高亮颜色均可以进行修改，具体的修改方式如图 5 所示。

图 5. 修改Spyder 中代码的字体样式 (Tools → Preferences → Appearance)

Page 5  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 34.2 Spyder 用起来

本章配套文件Bk1_Ch34_01.py 核心代码如图 6 所示。这部分代码选自上一章Jupyter Notebook。

#%% 导入库 # =============================================== # 导入库 # ============================================== import numpy as np import matplotlib.pyplot as plt import seaborn as sns #%% 等差数列 # ============================================== # 等差数列 # ============================================== a0 = 1 # 首项 n = 10 # 项数 d = 2 # 公差 a_array = np.arange(a0, a0 + n*d, d)

print('打印等差数列'); print(a_array)

#%%% 可视化 fig = plt.figure(figsize = (8,8))

plt.scatter(np.arange(n), a_array)

plt.title('Arithmetic Progression')

plt.xlabel('Index, $n$'); plt.ylabel('Value, $a_n$')

#%% 二元函数 # ============================================== # 二元函数 # ============================================== x1_array = np.linspace(-3, 3, 301)

x2_array = x1_array xx1, xx2 = np.meshgrid(x1_array, x2_array)

ff = xx1 * np.exp(-xx1**2 - xx2**2)

#%%% 可视化 fig = plt.figure(figsize = (8,8))

ax = fig.add_subplot(projection='3d')

# 绘制二元函数网格曲面 ax.plot_wireframe(xx1, xx2, ff, rstride=10, cstride=10)

#%% 鸢尾花数据 # ============================================== # 鸢尾花数据 # ============================================== # 加载鸢尾花数据集 iris_df = sns.load_dataset('iris')

print('打印鸢尾花数据前5行'); print(iris_df.head())

#%%% 可视化 fig, ax = plt.subplots(figsize = (8,8))

ax = sns.scatterplot(data=iris_df, x="sepal_length", y="sepal_width", hue = "species")

ax.set_xlabel('Sepal length (cm)')

ax.set_ylabel('Sepal width (cm)')

ax.set_xticks(np.arange(4, 8 + 1, step=1))

ax.set_yticks(np.arange(1, 5 + 1, step=1))

ax.axis('scaled')

ax.grid(linestyle='--', linewidth=0.25, color=[0.7,0.7,0.7])

ax.set_xbound(lower = 4, upper = 8)

ax.set_ybound(lower = 1, upper = 5)

a b e g h j f print print

图 6. 使用Spyder 完成编程实践

Page 6  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 下面聊一聊图 6 中给出的代码。

首先请大家注意a 中 #%%。在Spyder 中，#%% 是一个特殊的注释标记，#%%的作用是将代码分隔成多个单独的代码块 (cell)，以便更好地组织和运行代码。

简单来说，在Spyder 中使用#%%标记时，代码编辑器将把代码分割成以#%%为分隔符的多个片段。这使得大家可以分别运行每个代码片段，而不必运行整个脚本。这对于测试和调试代码非常有用。

代码下文#%%%代表下一级代码块。

注意，Ctrl + Return 可以用来执行光标所在代码块。Ctrl + Shift + O 打开代码目录。

b 是用Ctrl + 4 快捷键生成的注释代码块。

在Python 中使用包或模块，通常需要先用import 导入。简单来说，导入是将外部代码引入到当前代码环境中的过程，使得可以使用这些包或模块中定义的函数、类、变量等。c 先后导入了numpy (别名np)、matplotlib.pyplot (别名plt)、seaborn (sns)。本书第4 章将专门讲解如何使用import。

d 中的np.arange() 采用numpy (别名np) 中的arange() 函数生成等差数列，并保存在变量a_array。

a_array 的数据形式叫NumPy array。NumPy array 是NumPy 库中的主要数据结构。它是一个多维数组对象，用于存储和处理大量同类型的数据。a_array 只有一维。大家可以用a_array.shape 获得数组形状。本书第4 板块专门介绍NumPy。

e 利用散点图可视化等差数列。fig = plt.figure(figsize = (8,8)) 创建一个宽8 英寸、高8 英寸的图形对象fig。1 英寸折合约2.54 厘米。绘制散点图的函数为matplotlib.pyplot.scatter() (别名plt.scatter())。

matplotlib.pyplot.title() (别名plt.title()) 添加图像标题，matplotlib.pyplot.xlabel() (别名plt.xlabel()) 添加横轴标题，matplotlib.pyplot.ylabel() (别名plt.ylabel()) 添加纵轴标题。本书第10 ~ 12 章介绍常用几种可视化方案；此外，《可视之美》一册专门讲解可视化。

f 中首先利用numpy.linspace() 函数在指定的区间 [-3, 3] 内生成指定数量 (301) 的等间隔数据。然后利用numpy.meshgrid() 生成网格化数据，分别保存在xx1、xx2 中。xx1 相当于是网格的横轴坐标， xx2 是网格的纵轴坐标。本书后文会专门讲解如何使用这个函数。xx1、xx2 也都是NumPy array，它们都是二维。

f 最后计算二元函数 ( )

( )

, exp f x x = − − 在网格化坐标 (xx1, xx2) 的函数值，保存在ff 中。

g 利用网格面可视化二元函数。ax = fig.add_subplot(projection='3d') 在图像对象fig 上创建一个三维轴对象ax。然后，在三维轴对象ax 绘制三维网格图。注意，rstride 和cstride 参数控制网格线的密度。

h 采用seaborn.load_dataset('iris') 加载鸢尾花数据集，赋值给变量 iris_df。鸢尾花数据集是这套鸢尾花书重要的分析对象，本书后续会深入介绍。数据iris_df 格式是Pandas dataframe，叫做数据帧；大家可以把数据帧理解成有标签的表格数据。本书第6 板块专门讲解Pandas 数据帧。

i 利用seaborn.scatterplot() 函数绘制散点图。本书第26 章介绍如何使用Seaborn。j 是对ax 轴对象进行装饰。

## 34.3 快捷键

Spyder 通过设定快捷键提高操作效率，表 1 列举了部分常用的默认快捷键。

Page 7  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 表 1. Spyder 常用快捷键快捷键组合功能 ctrl S 保存 enter shift

执行 + 跳转；运行当前cell 中的代码，光标跳转到下一cell enter ctrl

执行；运行当前cell 中的代码；F9 执行当前行/选中代码 ctrl 注释/撤销注释；对所在行，或选中行进行注释/撤销注释操作 ctrl [ 向左缩进；行首减四个空格 ctrl ]

向右缩进；行首加四个空格 ctrl D 删除光标所在行 ctrl F 查找 ctrl L 输入数字，跳转到某一行 ctrl G 打开函数定义 ctrl R 替代 ctrl Z 撤销；撤销上一个键盘操作 ctrl N 创建新代码文件 { shift ctrl

上下布置窗口 - shift ctrl

左右布置窗口 O shift ctrl

打开代码目录 ctrl C 复制；复制选中的代码或文本 ctrl X 剪切；剪切选中的代码或文本 ctrl V 粘贴；粘贴复制/剪切的代码或文本 home 跳到某一行开头 end

跳到某一行结尾 ctrl home

跳到代码文件第一行开头 ctrl end

跳到代码文件最后一行结尾 tab 代码补齐；忘记函数拼写时，可以给出前一两个字母，按tab 键得到提示

这些快捷键可以通过图 7 中的设置进行修改。如果大家同时使用JupyterLab 和Spyder，建议大家统一常见快捷键。

Page 8  |  Chapter 34 了解一下Spyder  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 7. 修改快捷键 (Tools → Preferences → Keyboard shortcuts)

本章唯一的题目就是在Spyder 中练习图 6 代码的编程实践。

* 这道题目很基础，本书不给答案。

本书除最后三章外都建议用JupyterLab；本书最后两章在介绍如何用Streamlit 搭建机器学习应用时会用Spyder。

Page 1  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Build Streamlit Apps Streamlit 搭建Apps 用Streamlit 搭建数学学习、数据科学、机器学习应用

没有对已有知识进行大量练习，你不太可能发现新事物；但更进一步，你应该从解决有趣的关系和有趣的问题中获得很多乐趣。

You’re unlikely to discover something new without a lot of practice on old stuff, but further, you should get a heck of a lot of fun out of working out funny relations and interesting things.

—— 理查德·费曼 (Richard P. Feynman)  |  美国理论物理学家  |  1918 ~ 1988

◄ streamlit.area_chart() 面积图 ◄ streamlit.bar_chart() 直方图 ◄ streamlit.button() 按钮，点击时会触发指定的动作 ◄ streamlit.checkbox() 复选框，用户可以选择或取消选择 ◄ streamlit.color_picker() 颜色选择器，用户可以选择颜色 ◄ streamlit.columns() 创建多列布局 ◄ streamlit.container() 是一个用于组织内容的容器 ◄ streamlit.date_input() 日期输入框，用户可以选择日期 ◄ streamlit.expander() 创建可展开的区域 ◄ streamlit.file_uploader() 文件上传器，用户可以上传文件 ◄ streamlit.header() 显示章节标题 ◄ streamlit.line_chart() 线图 ◄ streamlit.markdown() 显示 markdown 文本 ◄ streamlit.multiselect() 多选框，用户可以从给定选项中选择多个 ◄ streamlit.number_input() 数字输入框，用户可以输入数字 ◄ streamlit.plotly_chart() 展示Plotly 图像对象 ◄ streamlit.pyplot() 展示Matplotlib 图像对象 ◄ streamlit.radio() 一组单选按钮，用户可以从给定选项中选择一个 ◄ streamlit.select_slider() 选择滑块，用户可以从给定选项中选择一个值 ◄ streamlit.selectbox() 下拉选择框，用户可以从给定选项中选择一个 ◄ streamlit.sidebar() 创建侧边栏 ◄ streamlit.slider() 滑块，用户可以在指定范围内选择一个值 ◄ streamlit.tabs() 创建选项卡式的布局 ◄ streamlit.text_area() 多行文本输入框，用户可以输入多行文本 ◄ streamlit.text_input() 文本输入框，用户可以输入文本 ◄ streamlit.time_input() 时间输入框，用户可以选择时间 ◄ streamlit.title() 显示标题 ◄ streamlit.write() 显示字符串、数据帧、报错、函数、图像等等

Page 2  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

## 35.1 什么是Streamlit？

Streamlit 是一个用于构建数据科学和机器学习应用程序的开源 Python 库。Streamlit 能够以简单且快速的方式创建交互式应用程序，无需繁琐的前端开发。Streamlit 有如下主要功能。

用户交互：Streamlit 具有构建用户界面的功能，可以添加各种交互元素，例如滑块、下拉菜单和复选框，以使用户能够与应用程序进行互动，并动态地改变应用程序的行为。

数据可视化：Streamlit 提供了丰富的图表和可视化组件，能够直观地展示数据和模型的结果。

Streamlit 还支持Matplotlib、Seaborn、Plotly 等库创建图表，并将其集成到应用程序中。

模型展示：Streamlit 支持在应用程序中展示机器学习模型的结果。可以用Streamlit 加载模型并使用它们对新数据进行预测。这对于展示模型的性能、解释结果或进行实时预测非常有用。

部署和共享：Streamlit 提供了一个简单的部署机制，可以轻松地将应用程序部署到 Web 上，并与其他人共享。

本章主要介绍如何使用Streamlit 的核心功能，下两章分别介绍如何用Streamlit 创建数据分析、机器学习相关App 应用。

安装安装Anaconda 后，可以进一步安装Streamlit。如图 1 所示，对于Windows 用户，先打开Anaconda Navigator，点进入Environments，然后选择特定环境，左键点击打开下拉菜单，选择Open Terminal。大家也可以直接搜索打开Anaconda Prompt，进入。进入Prompt 之后，键入pip install streamlit (注意，全小写、半角空格) 安装。

Left click

图 1. 安装Streamlit

Page 3  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com 需要更新Streamlit，请使用pip install streamlit --upgrade。

对于macOS 和Linux 用户，请参考如下页面安装Streamlit： https://docs.streamlit.io/library/get-started/installation

安装测试为了测试Streamlit 安装成功，在Anaconda Prompt 中大家可以键入streamlit hello (注意，全小写、 半角空格)。如果在默认浏览器中成功打开如图 2 下图所示网页，则成功安装Streamlit。

如果不成功的话，请重新安装Streamlit。如有必要可以关机重新开机再尝试安装。还是安装失败的话，可以卸载Anaconda，再重新下载安装最新Anaconda 后，在尝试重新安装Streamlit。

图 2. 安装Streamlit

本章还提供了一个Streamlit 测试代码——streamlit_app_test.py。

大家将配套测试代码下载保存到特定文件夹路径 (比如C:\Users\james\Desktop\test_streamlit)，如果想要演示这个App，大家可以在Anaconda Prompt 键入streamlit_app_test.py 所在文件夹路径，比如cd C:\Users\james\Desktop\test_streamlit。其中，cd 表示"Change Directory"，即切换目录的意思。这是用于在命令行中导航文件系统的命令。

然后键入streamlit run streamlit_app_test.py。其中，streamlit run 是用于在Anaconda Prompt 中启动和运行Streamlit 应用程序的命令。

Page 4  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 3. 演示本章配套测试代码

IDE 虽然，Streamlit 社区中有用户创建了在JupyterLab 中开发Streamlit Apps 的库，但是作者建议大家还是用Spyder 或PyCharm 作为开发Streamlit Apps 的IDE。

比如，本章配套代码的例子streamlit_app_test.py 就是用Spyder 完成。

强调一下，在各种IDE 中运行Python 文件并不能打开浏览器查看Streamlit 应用程序。必须要用在 Anaconda Prompt 中运行streamlit run _name_of_your_streamlit_app.py (图 3) 才能查看交互应用程序。大家完全可以一边编程，一边在浏览器查看应用程序效果。如果程序运行一遍较快的话，可以在App 浏览器右上角选择Always rerun，这样一边编程，App 浏览器就跟着更新，这样方便debug。

图 4. Streamlit 应用页面设置

API (Application Programming Interface) 直译为应用程序编程接口。简单来说，API 就是指是一些预先定义好的函数。下面我们介绍几类常用的API 函数。

## 35.2 显示

图 5 代码利用Streamlit 的函数显示文字、图像，浏览器呈现的App 效果如图 6 所示。

a 将streamlit 导入，别名为st (这是Streamlit 官方通用别名，建议大家直接采用)。为了和官网技术文档保持一致，本章在介绍Streamlit 函数时，也会直接采用st.function()，而不是streamlit.function()。

b 利用st.title() 显示标题，这个函数的输入为str。

Streamlit 最近还推出了渲染文本的语法，:color[text to be colored]。比如，b 中 :red[Streamlit] 用红色渲染Streamlit。

c 利用st.header() 显示章节标题。d 利用st.markdown() 显示Markdown 文本。e 利用st.write() 显示数据帧。Streamlit 官网管st.write() 叫“瑞士军刀”，根据官方技术文档，st.write() 几乎可以显示各种对象，比如字符串、数据帧、报错、函数、模块、图像对象 (比如f )、sympy 符号数学表达式等等。

其他显示文本的函数还有，st.subheader()、st.captain()、st.code()、st.text()、st.latex()。

Page 5  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import streamlit as st import seaborn as sns import plotly.express as px # 显示标题 st.title('Welcome to the world of :red[Streamlit]')

# 显示章节标题 st.header('Pandas DataFrame')

# 显示 markdown 文本 st.markdown("Load :blue[Iris Data Set]")

# 从Seaborn导入鸢尾花数据帧 df = sns.load_dataset('iris')

# 显示数据帧 st.write(df)

# 显示章节标题 st.header('Visualize Using Heatmap')

fig = px.imshow(df.iloc[:,:-1])

# 显示热图 st.write(fig)

a b e f

图 5. 用于显示的函数

图 6. 用于显示的函数，浏览器App

## 35.3 可视化

Streamlit 目前本身可视化方案有限，比如线图 (st.line_chart())、面积图 (st.area_chart())、直方图 (st.bar_chart()) 等。但是Streamlit 支持其他主流Python 可视化库，比如Matplotlib、Plotly、Altair、

Page 6  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com Bokeh 等等。图 7 代码a 利用st.pyplot() 专门绘制Matplotlib 图像对象，大家自己打开App 会发现这幅图为静态图像，也就是一幅图片。而b 利用st.plotly_chart() 专门绘制Plotly 图像对象，这幅图就是可交互的，大家可以在浏览器App 中旋转、缩放这幅图。

import plotly.graph_objects as go import numpy as np import matplotlib.pyplot as plt import streamlit as st # 产生数据 x1_array = np.linspace(-3, 3, 301)

x2_array = np.linspace(-3, 3, 301)

xx1, xx2 = np.meshgrid(x1_array, x2_array)

# 二元函数的曲面数据 ff = xx1 * np.exp(-xx1**2 - xx2**2)

# Matplotly图像 fig = plt.figure(figsize = (8,8))

ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(xx1, xx2, ff, rstride=10, cstride=10)

st.pyplot(fig)

# Plotly图像 fig = go.Figure(data=[go.Surface(z=ff, x=xx1, y=xx2, colorscale = 'RdYlBu_r')])

st.plotly_chart(fig)

a b

图 7. Streamlit 中的可视化示例

## 35.4 输入工具

Streamlit 还支持各种输入工具 (input widget)，表 1 总结常用输入工具。

请大家自行练习图 8 中代码，并在浏览器查看输入工具效果。此外，建议大家查看每种输入工具返回值、类型，如a 、b 。

表 1. Streamlit 常用输入工具输入工具样式说明代码示例 import streamlit as st

按钮，点击时会触发指定的动作 st.button("Click me")

复选框，用户可以选择或取消选择 st.checkbox("Check me")

Page 7  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

一组单选按钮，用户可以从给定选项中选择一个 st.radio("Choose one:", ["Option 1", "Option 2", "Option 3"])

下拉选择框，用户可以从给定选项中选择一个 st.selectbox("Choose one:", ["Option 1", "Option 2", "Option 3"])

多选框，用户可以从给定选项中选择多个 st.multiselect("Choose many:", ["A","B","C","D"])

滑块，用户可以在指定范围内选择一个值 st.slider("Select a value:", 0.0, 10.0, 5.0)

滑块，用户可以从给定选项中选择一个值 st.select_slider("Select a value:", options=[1, 2, 3, 4, 5])

文本输入框，用户可以输入文本 st.text_input("Enter your name")

数字输入框，用户可以输入数字 st.number_input("Enter a number")

多行文本输入框，用户可以输入多行文本 st.text_area("Enter your message")

日期输入框，用户可以选择日期 st.date_input("Select a date")

时间输入框，用户可以选择时间 st.time_input("Select a time")

文件上传器，用户可以上传文件 st.file_uploader("Upload a file")

颜色选择器，用户可以选择颜色 st.color_picker("Pick a color")

Page 8  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import streamlit as st button_return = st.button("Click me")

st.write(button_return)

st.checkbox("Check me")

st.radio("Choose one:", ["A", "B", "C"])

st.selectbox("Choose one:", ["A", "B", "C"])

st.multiselect("Choose many:", ["A", "B", "C", "D"])

st.slider("Select a value:", 0.0, 10.0, 5.0)

st.select_slider("Select a value:", options=[1, 2, 3, 4, 5])

st.text_input("Enter your name")

st.number_input("Enter a number")

st.text_area("Enter your message")

st.date_input("Select a date")

st.time_input("Select a time")

st.file_uploader("Upload a file")

st.color_picker("Pick a color")

a b

图 8. Streamlit 的输入工具代码示例

## 35.5 App 布局

Streamlit 提供几种App 布局设计。

侧边栏 (sidebar) 对应的函数为st.sidebar()，是Streamlit 应用程序界面中的一个垂直边栏，可用于显示与主要内容相关的附加信息、控件和选项。侧边栏通常用于放置与应用程序设置、参数选择、数据过滤等相关的小部件。可以使用st.sidebar 方法来在侧边栏中添加小部件。

如图 9 所示，这个Streamlit 应用展示a、b、c 三个参数对抛物线 (f(x) = ax2 + bx + c) 影响。左侧边框中，用户可以通过st.slider() 滑动选择a、b、c 三个参数具体值。图 9 右侧主页面则分别打印函数，并展示函数图像。

Page 9  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com

图 9. Streamlit 应用的侧边框

图 10 所示为创建图 9 中Streamlit 应用的代码。

a 用 with st.sidebar: 创建了侧边框代码块。类似for loop，四个空格缩进用来表达代码块。

b 用st.latex() 打印LaTeX 公式，在侧边框展示 ( )

f x ax bx = + + 。

b 这一句还可以这样写，st.sidebar.latex(r'f(x) = ax^2 + bx + c')；这种写法不需要缩进，可以在侧边框代码块外部写。

c 用st.slider() 提供滑块输入工具，用户可以选择输入数值，这个数值赋值给变量a。min_value = -5.0 设定滑块最小值， max_value = 5.0 设定最大值，step = 0.01 设定滑块滑动步长，value = 1.0 设定滑块默认值。

d 和e 用同样输入工具给变量b、c 赋值。

f 创建SymPy 符号数学表达式。

g 利用sympy.lambdify() 将符号数学表达式转化为Python 函数。h 计算抛物线函数值。

i 用st.title() 创建应用标题。

j 用st.latex() 将SymPy 符号数学表达式以LaTeX 形式打印在主页面上。

k 用st.write() 将Matplotlib fig 对象显示在主页面上。

Page 10  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import streamlit as st import numpy as np from sympy import symbols,lambdify import matplotlib.pyplot as plt # 侧边框 with st.sidebar: st.header('Choose coefficients')

st.latex(r'f(x) = ax^2 + bx + c')

a = st.slider("a",min_value = -5.0, max_value = 5.0, step = 0.01, value = 1.0)

b = st.slider("b",min_value = -5.0, max_value = 5.0, step = 0.01, value = -2.0)

c = st.slider("c",min_value = -5.0, max_value = 5.0, step = 0.01, value = -3.0)

# 抛物线 x = symbols('x')

f_x = a*x**2 + b*x + c x_array = np.linspace(-5,5,101)

f_x_fcn = lambdify(x, f_x)

y_array = f_x_fcn(x_array)

# 主页面 st.title('Qudratic function')

st.latex(r'f(x) = ')

st.latex(f_x)

# 可视化 fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(x_array, y_array)

ax.set_xlim([-5, 5])

ax.set_ylim([-5, 5])

ax.set_aspect('equal', adjustable='box')

ax.set_xlabel('x')

ax.set_ylabel('f(x)')

st.write(fig)

a f k b e g h j

图 10. Streamlit 应用的侧边框，代码

此外，函数st.columns() 在Streamlit 应用程序中创建多列布局，可以将内容水平分割成几个部分。

通过这种方式，可以更好地控制内容的排列方式。

如图 11 所示，a  中st.columns(2) 创建两列，对象分别是col1、col2。我们还可以通过输入控制多列布局比例，比如 col1, col2 = st.columns([3, 1])，创建col1 和col2 比例为3:1。

再比如col_A, col_B, col_C = st.columns([2,1,1])，创建col_A, col_B, col_C 比例为2:1:1。

注意，目前st.columns() 只能用在主页面中，不能用在侧边框。

Page 11  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com b 在col1 分栏显示文字，c 在col2 分栏显示文字。类似侧边框，也可以用with col1: 这种语法形式创建代码块。

import streamlit as st # 在两列中显示不同的内容 col1, col2 = st.columns(2)

col1.write("This is column 1")

col1.latex(r'f(x) = ax^2 + bx + c')

col2.write("This is column 2")

a b

图 11. Streamlit 应用多列布局

st.tabs() 可以用来创建选项卡式的布局，将相关的内容分组在不同的选项卡中，从而使应用程序界面更加清晰和易于导航。请大家自行学习图 12。

st.expander() 创建可展开的区域，可以用来隐藏一些内容，让用户选择是否展开查看。请大家自行学习图 13。

st.container() 创建组织内容的容器，可以用于控制内容的对齐方式和排列顺序。

import streamlit as st # 创建两个选项卡，每个选项卡显示不同的内容 tab_A, tab_B = st.tabs(["Tab A", "Tab B"])

with tab_A: st.header("Tab A Title")

st.write('This is Tab A.')

with tab_B: st.header("Tab B Title")

st.write('This is Tab B.')

a b

图 12. Streamlit 应用多选项卡布局

Page 12  |  Chapter 35 Streamlit 搭建Apps  |  Book 1《编程不难》  |  鸢尾花书：从加减乘除到机器学习本PDF 文件为作者草稿，发布目的为方便读者在移动终端学习，终稿内容以清华大学出版社纸质出版物为准。

版权归清华大学出版社所有，请勿商用，引用请注明出处。

代码及PDF 文件下载：https://github.com/Visualize-ML 本书配套微课视频均发布在B 站——生姜DrGinger：https://space.bilibili.com/513194466 欢迎大家批评指教，本书专属邮箱：jiang.visualize.ml@gmail.com import streamlit as st import seaborn as sns import plotly.express as px # 显示标题 st.title('Iris Dataset')

# 从Seaborn导入鸢尾花数据帧 df = sns.load_dataset('iris')

# 第一个可展开区域 with st.expander("Open and view DataFrame"): # 显示数据帧 st.write(df)

# 第二个可展开区域 with st.expander("Open and view Heatmap"): fig = px.imshow(df.iloc[:,:-1])

# 显示热图 st.write(fig)

a b

图 13. Streamlit 应用可展开区域

请大家注意，本章仅仅介绍一些常用Streamlit 功能；Streamlit 近期获得很大关注，开发团队不断增加新的功能，推出新版版，因此语法也可能发生更新。想要更全面了解Streamlit 功能，请大家关注： https://docs.streamlit.io/library/api-reference Streamlit 社区开发者、用户开开发了很多小插件，请大家参考： https://extras.streamlit.app/

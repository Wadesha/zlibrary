第3卷第1期光学学报 Vol.

3, No. 1

# OPTICA SINICA

1983年1月 Acta Janua可1983

双光子激光的半经典理论汪志诚曹玲（兰州大学物理系）提要本文将 Lamb的半经典方法应用于单模双光子激光问题。得到了模振幅方程的定态解，并分析了其稳定性。结果表明，双光子激光对抽运和光场强度均有阈值要求。频率方程预示牵引效应。一、引言自从多光子激光的设想[1]被提出以来，对多光子过程的研究已取得了很大的进展。实验早已观察到双光子的吸收[2]和自发发射现象[3]。最近，成功地观测到双光子的受激发射和放大[4]。Hoshimiya等[5]用Lamb的半经典理论

Bulsara等[6]用随机过程理论

McNeil等[7]和Zubairy[8]分别用Lamb的量子理论对多光子激光问题进行了研究。Hoshimiya等考虑三能态的原子模型用Takatsuji等[9]所引入的正则变换化为二能态问题然后用Lamb的方法在弱场近似下进行了分析（三阶理论）。本文考虑的原子模型是多能态的用Narducci等[10]的方法消去中间能态化为二能态问题然后运用Lamb的半经典方法[11]对任意场强下的单模双光子激光问题进行探讨。二、布居数矩阵的运动方程仿照Lamb的作法，可以得到下述振幅方程和频率方程：dE0/dt + κE0 = (ω/2Q) χE0, (1)

dφ/dt = v - Ω + (1/2) Δχ, (2)

其中v+φ为模频率，Ω为无源腔模频率，Q为光腔的品质因素。引入激活介质的原子模型设光场 E(z

t) = E0(z

t)cos[vt-kz+φ(t)]及感生极化强度 P(z

t) = Pc(t)cos(vt-kz+φ) + Ps(t)sin(vt-kz+φ)

代入(1)和(2)式以确定光场的振幅和频率。定义单个原子密度矩阵为

ρ = [[ ρaa, ρab ], [ ρba, ρbb ]]

容易求得矩阵元的运动方程：将上式对t求导数，注意到被积函数和积分上限都与t有关，得

dPaa/dt = λa - γa Paa - (ikabE0(t)/ħ) (Pab e^{-iθ} - Pba e^{iθ})

dPbb/dt = λb - γb Pbb + (ikabE0(t)/ħ) (Pab e^{-iθ} - Pba e^{iθ})

dPab/dt = -(iθ(t) + γ) Pab - (ikabE0(t)/ħ) e^{-iθ} (Paa - Pbb) (5)

三、布居数矩阵运动方程的解

(5)式的形式解为:

Pab = (-i/ħ) ∫ dt' exp{-[iθ(t') + γ](t' - t)} kab E0(t') exp{i[(2v - ωab)t' - 2kz + 2φ(t')]} (Paa - Pbb)

由于 E0(t), φ(t'), ω(t')是时间的慢变函数，应用慢变近似可得:

Pab ≈ (-i kab E0(t) / 4ħ) e^{-iθ} [ (Paa - Pbb) / (γ - i(2v - ωab)) ]

Pba ≈ (i kab E0(t) / 4ħ) e^{iθ} [ (Paa - Pbb) / (γ + i(2v - ωab)) ]

其中 ωab = ωa - ωb。将Pab, Pba代入(5)式有

dPaa/dt = λa - γa Paa - R (Paa - Pbb)

dPbb/dt = λb - γb Pbb + R (Paa - Pbb) (6)

Paa = Ma(z) / [1 + (R/Rs) ]

Pbb = Mb(z) / [1 + (R/Rs)]

Paa - Pbb = N(z) / [1 + (R/Rs)]

其中式中 Rs, N(z)

Ma(z), Mb(z)是z和t的慢变函数

R是t的慢变函数。四、激活介质的极化强度单个原子的平均偶极矩为 <p> = <ξ(t) | p | ξ(t)>

将偶极矩算符和原子态矢量代入上式经运算可得

- ikab (ρab e^{iθ} - ρba e^{-iθ}) E0(t) sin(vt-kz+φ)

激活介质的宏观极化强度 P(z, t)为:

- ikab (Pab e^{iθ} - Pba e^{-iθ}) E0(t) sin(vt-kz+φ)

将此式中所含 z 的慢变量 N(z)

Ma(z), Mb(z)取平均值可求得感生极化强度的两个分量

Ps(t) = -kab E0(t) * (2v - ωab) * N / [1 + (R/Rs)]

Pc(t) = kaa Ma + kbb Mb + [kab E0(t) (2v - ωab) * Q / (2v - ωab)^2 + γ^2] / [1 + (R/Rs)]

其中 N, 后面

Mb 是慢变量 N(z)

Ma(z), Mb(z)对z的平均值。五、结果分析为了讨论双光子激光的定态运转引入无量纲的场强 I(t) = kab^2 E0(t) / (8ħγ Rs)。将(7)式代入(1)式得

dI/dt = A I (1 + B I^2) - I / Q, (8)

其中

A = Rs N γ (2v - ωab) / (kab^2)

B = R γ^2 (2v - ωab)^2 / (kab^2 γ^2) (9)

在定态下，dI/dt = 0

则得 A (1 + B I^2) - I/Q = 0。此式有一个解 I = 0，其它的解由二次方程

B I^2 - A Q I + 1 = 0 (10)

其解取决于判别式 Δ = A^2 Q^2 - 4 B。分别讨论 Δ < 0，Δ = 0 和 Δ > 0 三种情况。令 g = A^2 Q^2 / (4 B)

则相应三种情况为 g < 1

g = 1 和 g > 1。[4] M.

Lipes et al.; Phys.

Rev.

Lett.

, 1965, 15, No. 16 (Oct), 690.

[5] B.

Nikolaus et al.; Phys.

Rev.

Lett.

, 1981, vol. 1, No. 8 (Jul), 171.

[6] T.

Hihimiya et al.; J.

Appl.

Phys.

Japan, 1978, vol., No.12 (Dec), 2177.

[7] A.

Bulsara et al.; Phys.

Rev.

A, 1979, vol. 1, No. 5 (May), 2046.

[8] K.

McNeil, D.

Walls; J.

Phys.

(A), 1975, 8, No. 1 (Jan), 104.

[9] M.

Zubairy; Phys.

Lett.

, 1980, vol. 1A, No. 4 (Jan), 225.

[10] M.

# Takatsuji

# Physica

1977, vol. A

No. 2 (Jan)

265.

[11] L.

Narducci, W.

Manson; Phys.

Rev.

, 1977, 18A, No. 4 (Oct), 1665.

[12] M.

Sargent et al.

# Classical Physics

(Addison-Wesley Pub.

Inc.

, 1974).

Semiclassical theory of a two-photon laser

# WANG ZHICHENG AND CAO LIMIN

(Department of Physics

University of Lanzhou)

(Received 11 September 1981

revised 1 March 1982)

# Abstract

The semiclassical lamb method is applied to the problem of a single mode two-photon laser (TPL).

The steady-state solutions of the amplitude equation are obtained

and their stability properties are analysed.

# It is found that

for TPL there exist threshold requirements both for pumping and for the light field intensity.

The frequency equation predicts a mode-pulling effect.

Announcement - International Conference on Ellipsometry and Other Optical Methods for Surface and Thin Film Analysis

1983年6月7-10日将在法国巴黎召开"表面和薄膜分析的椭圆对称法及其他光学方法"的国际会议。组织委员会主席为F.

Abelès教授 (Prof. F.

Abelès

Laboratoire d'Optique des Solides, Université P.

et M.

Curie, 4

place Jussieu

75230 Paris Cedex 05

France)。会议将就以下各专题进行交流：表面和界面的粗糙度，表面增强的喇曼散射等；界面的电化学问题；有机膜和生物学上的问题；椭圆对称，反射率，差动反射率，电反射能力；导波和表面等离子体技术、发光中的进展；极薄表面层及其吸收；表面层生长的原位分析。光谱范围从紫外至红外。(黎风)

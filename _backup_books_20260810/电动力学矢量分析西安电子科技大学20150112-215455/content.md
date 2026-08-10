# 电动力学矢量分析西安电子科技大学20150112 215455

> 来源文件：pre_电动力学矢量分析西安电子科技大学20150112_215455.txt
> 字符数（约）：5086
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

电动力学 Electrodynamics

## 第0章 矢量分析 (Vector analysis)

白璐邮箱： blu@xidian.edu.cn 主页： http://web.xidian.edu.cn/bailu 电话：15291456996

本章内容 §0.1 矢量代数（vector analysis）

§0.2 微分（differential calculus）

§0.3 积分（integral calculus）

§0.4 曲线坐标系（curvilinear coordinates）

§0.5 Delta 函数（The Dirac Delta function）

§0.6 矢量场论（Theory of vector fields）

§0.1 矢量代数一、矢量运算标量：只有大小没有方向的物理量。如：质量，电荷等。

矢量：既有大小又有方向的物理量。如：速度，场强等。

矢量几何表示：有大小有方向的线段矢量代数表示： A = e_A A 大小： |A| = A 单位矢量： e_A = A / A 常矢量：大小和方向均不变的矢量。

注意：单位矢量不一定是常矢量。

1.矢量的加(减)法 A + B 交换律(commutative) A + B = B + A 结合律(associative) A + (B + C) = (A + B) + C 矢量的加法 2.标量乘矢量分配律(distributive)

α(A + B) = αA + αB

## A - B

3.矢量的点积（dot product）

A·B = AB cosθ 矢量的减法 A·B = B·A 交换律 A·(B+C) = A·B + A·C 分配率 A·A = A² = A 矢量 A 与 B 的夹角

4.矢量的矢积（cross product）

A × B = e_n AB sinθ A × B A × B = -B × A AB sinθ A × (B+C) = A × B + A × C 矢量 A 与 B 的叉积 A × A = 0 若 A ⊥ B，则 A × B = AB 若 A // B，则 A × B = 0

二、矢量代数的分量表示 A = A_x e_x + A_y e_y + A_z e_z A + B = (A_x + B_x) e_x + (A_y + B_y) e_y + (A_z + B_z) e_z A·B = A_x B_x + A_y B_y + A_z B_z A = √(A·A) = √(A_x² + A_y² + A_z²)

A·B = Σ_i Σ_j A_i B_j δ_ij δ_ij = e_i · e_j = { 1 if i = j; 0 if i ≠ j } 称为Kronecker delta

矢量的矢积的分量表示 A × B = e_x (A_y B_z - A_z B_y) + e_y (A_z B_x - A_x B_z) + e_z (A_x B_y - A_y B_x)

写成行列式形式为 A × B = | e_x e_y e_z; A_x A_y A_z; B_x B_y B_z | = Σ_i Σ_j Σ_k ε_ijk A_i B_j e_k ε_ijk 称为Levi-Civita symbol ε_ijk = { 1 if ijk=123,231,312; -1 if ijk=132,213,321; 0 otherwise } 矢量 A 与 B 的叉积 |A × B| = AB sinθ

三、矢量的三重积 1.标量三重积（scalar triple product）

A·(B × C) = B·(C × A) = C·(A × B)

2.矢量三重积（vector triple product）

A × (B × C) = B(A·C) - C(A·B) BAC-CAB rule A × (B × C) ≠ (A × B) × C not associative 例：利用BAC-CAB rule 证明 A × (B × C) + B × (C × A) + C × (A × B) = 0

四、位矢、场点、源点源点 r' 场点 r e_x · e_y = e_y · e_z = e_z · e_x = 0 e_x · e_x = e_y · e_y = e_z · e_z = 1

§0.2 微分（differential calculus）

一、梯度（gradient）

例：求梯度，已知 r = |r - r'| = √[(x - x')² + (y - y')² + (z - z')²]

∇r = ?

解： ∂r/∂x = (1/(2r)) * 2(x - x') = (x - x')/r ∂r/∂y = (y - y')/r, ∂r/∂z = (z - z')/r ∴ ∇r = e_x (x - x')/r + e_y (y - y')/r + e_z (z - z')/r = (r - r')/r ∇r = r̂

例： ∇(φψ) = ?

解： ∂(φψ)/∂x = φ ∂ψ/∂x + ψ ∂φ/∂x ∂(φψ)/∂y = φ ∂ψ/∂y + ψ ∂φ/∂y ∂(φψ)/∂z = φ ∂ψ/∂z + ψ ∂φ/∂z ∇(φψ) = (e_x ∂ψ/∂x + e_y ∂ψ/∂y + e_z ∂ψ/∂z)φ + (e_x ∂φ/∂x + e_y ∂φ/∂y + e_z ∂φ/∂z)ψ = φ∇ψ + ψ∇φ ∇(φψ) = φ∇ψ + ψ∇φ

例：已知

二、算符 ∇ （gradient）

定义：

三、散度 （divergence）

Geometrical Interpretation: A point of positive divergence is a source A point of negative divergence is a sink, or “drain”

例：求散度，已知 r = (x - x') e_x + (y - y') e_y + (z - z') e_z 求 ∇·r ∇·r = ∂(x - x')/∂x + ∂(y - y')/∂y + ∂(z - z')/∂z = 3 ∇·(r/r³) = (1/r³) ∇·r + r·∇(1/r³) = 3/r³ + r·(-3r̂/r⁴) = 3/r³ - 3/r³ = 0 (r ≠ 0)

∇·(r/r³) = ∂/∂x ((x - x')/r³) + ∂/∂y ((y - y')/r³) + ∂/∂z ((z - z')/r³)

= [r³ - (x - x') * 3r² * (x - x')/r] / r⁶ + [r³ - (y - y') * 3r² * (y - y')/r] / r⁶ + [r³ - (z - z') * 3r² * (z - z')/r] / r⁶ = [r³ - 3(x - x')² r] / r⁶ + [r³ - 3(y - y')² r] / r⁶ + [r³ - 3(z - z')² r] / r⁶ = [3r³ - 3r((x - x')² + (y - y')² + (z - z')²)] / r⁶ = [3r³ - 3r * r²] / r⁶ = 0

求证： ∇·(φA) = φ∇·A + ∇φ·A 证： ∇·(φA) = ∂(φA_x)/∂x + ∂(φA_y)/∂y + ∂(φA_z)/∂z = φ(∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z) + A_x ∂φ/∂x + A_y ∂φ/∂y + A_z ∂φ/∂z = φ∇·A + ∇φ·A

四、旋度 （curl）

例：求证 ∇ × (r/r³) = 0 证： [∇ × (r/r³)]_x = ∂/∂y ((z - z')/r³) - ∂/∂z ((y - y')/r³)

= (y - y') * (-3) * (z - z') / r⁵ - (z - z') * (-3) * (y - y') / r⁵ = 0 同理 [∇ × (r/r³)]_y = 0, [∇ × (r/r³)]_z = 0 ∴ ∇ × (r/r³) = 0

例：求证 ∇ × (φA) = ∇φ × A + φ∇ × A 证： [∇ × (φA)]_x = ∂(φA_z)/∂y - ∂(φA_y)/∂z = φ ∂A_z/∂y + A_z ∂φ/∂y - φ ∂A_y/∂z - A_y ∂φ/∂z = φ(∂A_z/∂y - ∂A_y/∂z) + (A_z ∂φ/∂y - A_y ∂φ/∂z)

= φ [∇ × A]_x + [∇φ × A]_x ∴ ∇ × (φA) = φ∇ × A + ∇φ × A

五、算符运算公式（Product Rules）

标量矢量

六、二重算符运算公式（second derivatives）

（1）

（2）梯度的旋度恒为零 （3）散度的梯度极少应用 （4）旋度的散度恒为零 （5）旋度的旋度

§0.3 积分（integral calculus）

一、线、面、体积分（ Line，surface，and volume integrals）

（1）线积分物理应用：力做功若积分与路径无关只与始末点的位置有关（这样的力被称为保守力）

闭合路径：

（2）面积分物理应用：通量闭合曲面：

（3）体 （平面）

位置矢量 r = e_x x + e_y y + e_z z 直角坐标系线元矢量 dl = e_x dx + e_y dy + e_z dz 面元矢量 dS = e_z dxdy dS = e_y dxdz dS = e_x dydz 体积元 dV = dxdydz 直角坐标系的长度元、面积元、体积元

2、球面坐标系坐标变量 r, θ, φ 坐标单位矢量 e_r, e_θ, e_φ 位置矢量 r = e_r r 球面坐标系线元矢量 dl = e_r dr + e_θ r dθ + e_φ r sinθ dφ 面元矢量 dS = e_r r² sinθ dθ dφ dS = e_θ r sinθ dr dφ dS = e_φ r dr dθ 体积元 dV = r² sinθ dr dθ dφ 球坐标系中的线元、面元和体积元

3、圆柱面坐标系坐标变量 ρ, φ, z 坐标单位矢量 e_ρ, e_φ, e_z 位置矢量 r = e_ρ ρ + e_z z 线元矢量 dl = e_ρ dρ + e_φ ρ dφ + e_z dz 面元矢量 dS = e_ρ ρ dφ dz dS = e_φ dρ dz dS = e_z ρ dρ dφ 体积元 dV = ρ dρ dφ dz

4、坐标单位矢量之间的关系直角坐标与圆柱坐标系 e_ρ = e_x cosφ + e_y sinφ e_φ = -e_x sinφ + e_y cosφ e_z = e_z 直角坐标系与柱坐标系之间坐标单位矢量的关系

圆柱坐标与球坐标系 e_ρ = e_r sinθ + e_θ cosθ e_φ = e_φ e_z = e_r cosθ - e_θ sinθ 柱坐标系与球坐标系之间坐标单位矢量的关系

直角坐标与球坐标系 e_r = e_x sinθ cosφ + e_y sinθ sinφ + e_z cosθ e_θ = e_x cosθ cosφ + e_y cosθ sinφ - e_z sinθ e_φ = -e_x sinφ + e_y cosφ

§0.5 Delta 函数（The Dirac Delta function）

一、δ函数的散度 V为包围原点的任意体积 ——Dirac delta Function

二、一维Dirac delta 函数

三、三维Dirac delta 函数常用公式：

§0.6 矢量场论（Theory of vector fields）

一、亥姆霍兹定理（Helmholtz theorem）

问题：若已知某矢量函数场 F 的散度和旋度，能否唯一确定 F 结论是否，可以举出很多反例，如： 还需要边界（条件）

Helmholtz theorem F(r) = -∇u(r) + ∇ × A(r)

其中 u(r) = ∫_V [∇'·F(r')] / (4π|r - r'|) dV' A(r) = ∫_V [∇'×F(r')] / (4π|r - r'|) dV' 由Helmholtz定理可知 1.矢量场的散度、旋度加边界条件才能唯一确定矢量场 2.任意矢量场均可表示为一个无旋场和一个无散场之和

二、势（Potentials）

定理1：无旋场下列定理等价 ——也称标量势存在定理

定理2：无散场下列定理等价 ——也称矢量势存在定理

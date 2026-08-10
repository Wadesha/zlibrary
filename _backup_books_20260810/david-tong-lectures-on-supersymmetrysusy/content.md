# David Tong Lectures on Supersymmetrysusy

> 来源文件：pre_David_Tong_Lectures_on_Supersymmetrysusy.txt
> 字符数（约）：433498
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Supersymmetric Field Theory University of Cambridge Part III Mathematical Tripos David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 OBA, UK http://www.damtp.cam.ac.uk/user/tong/susy.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources Here is a collection of useful textbooks on supersymmetry.

• Wess and Bagger “Supersymmetry” This is a strange little book, with chapters that are 2 pages long followed by several pages of key equations. It’s not particularly good for learning the subject, but makes a remarkably useful reference guide.

• Bailin and Love “Supersymmetric Gauge Field Theory and String Theory” Probably the best book covering the basics of supersymmetric Lagrangians.

• Dan Freedman and Toine Van Proeyen “Supergravity” As the name suggests, this book is mostly focussed on supergravity rather than global supersymmetry. But it kicks off with a really excellent description of classical field theory. The section on spinors in various dimensions is particularly useful.

• Steven Weinberg “The Quantum Theory of Fields, Volume III: Supersymmetry” The third volume of Weinberg’s magnum opus covers supersymmetry. As always, it contains many important things that are difficult to find elsewhere. As always, these things are sometimes frustratingly buried in unconventional notation and dressed with more indices than you can shake a stick at.

• John Terning “Modern Supersymmetry: Dynamics and Duality” This is one of the few books (possibly the only book) that describes the quantum dynamics of supersymmetric field theories, rather than just their classical action. (Weinberg has a chapter on the Seiberg-Witten solution, but it feels like his heart isn’t in it and any mention of Seiberg duality is noticeably absent.) There are, fortunately, many lecture notes that make up for the deficiency. You can find links on the course webpage.

Contents 1 Introduction 3

## 1.1 A First Look at Supersymmetry

2 The Supersymmetry Algebra 9

## 2.1 The Lorentz Group

2.1.1 Spinors and SL(2,C) 12 2.1.2 Lagrangians for Spinors 18 2.1.3 The Poincaré Group and its Extensions 20

## 2.2 The Supersymmetry Algebra

2.2.1 R-Symmetry 25 2.2.2 A Consequence: Energy is Positive 25

## 2.3 Representations on Particle States

2.3.1 Representations of the Poincaré Group 28 2.3.2 Massless Representations 30 2.3.3 Massive Representations 33

## 2.4 Extended Supersymmetry

2.4.1 Massless Representations 37 2.4.2 Massive Representations and BPS Bounds 40 2.4.3 Supersymmetry in Other Dimensions 42 3 Chiral Superfields 48

## 3.1 Superspace

3.1.1 The Geometry of Superspace 49 3.1.2 Superfields 52 3.1.3 Constraining Superfields 56 3.1.4 Chiral Superfields 58

## 3.2 And...Action

3.2.1 Integrating Over Superspace 60 3.2.2 The Action for Chiral Superfields 62 3.2.3 Supersymmetry of the Wess-Zumino Model Revisited 66 3.2.4 Non-Linear Sigma Models 68

## 3.3 Non-Renormalisation Theorems

3.3.1 R-Symmetry Revisited 72 3.3.2 The Power of Holomorphy 73 3.3.3 Integrating Out Heavy Fields 78 3.3.4 A Moduli Space of Vacua 79

## 3.4 A First Look at Supersymmetry Breaking

3.4.1 The Goldstino 83 3.4.2 The Witten Index 85 3.4.3 The O’Raifeartaigh Model 88 3.4.4 R-symmetry and the Nelson-Seiberg Argument 92 3.4.5 More Ways to (Not) Break Supersymmetry 94 4 Supersymmetric Gauge Theories 98

## 4.1 Abelian Gauge Theories

4.1.1 The Field Strength and Action 99 4.1.2 Supersymmetric QED 101

## 4.2 Non-Abelian Gauge Theories

4.2.1 Super Yang-Mills 106 4.2.2 Supersymmetric QCD 107

## 4.3 The Moduli Space of Vacua

4.3.1 The Moduli Space of SQED 112 4.3.2 The Moduli Space of SQCD 116 4.3.3 Briefly, Gauged Linear Sigma Models in 2d 121

## 4.4 Extended Supersymmetry

4.4.1 N = 2 Theories 125 4.4.2 N = 4 Theories 128 5 Boot Camp: Quantum Gauge Dynamics 129

## 5.1 Strong Coupling

5.1.1 The Beta Function 129 5.1.2 Confinement and the Mass Gap 131 5.1.3 Adding Matter 134 5.1.4 Chiral Symmetry Breaking 136 5.1.5 Phases of Massless QCD 137

## 5.2 Anomalies

5.2.1 Gauge Anomalies 142 5.2.2 Chiral (or ABJ) Anomalies 144 5.2.3 ’t Hooft Anomalies 146

## 5.3 Instantons

6 Supersymmetric QCD 155

## 6.1 Super Yang-Mills

6.1.1 Confinement and Chiral Symmetry Breaking 158 6.1.2 The Witten Index 160 6.1.3 A Superpotential 163

## 6.2 A First Look at SQCD

6.2.1 Symmetries 166 6.2.2 Runaway for N < N_c 168 6.2.3 Adding Masses 170 6.2.4 The Potential at Weak Coupling 174

## 6.3 A Second Look at SQCD

6.3.1 A Deformed Moduli Space for N = N_c 178 6.3.2 ’t Hooft Anomaly Matching 180 6.3.3 Confinement Without χSB for N = N_c +1 185

## 6.4 A Peek in the Conformal Window

6.4.1 Facts About Conformal Field Theories 190 6.4.2 Facts About Superconformal Field Theories 193 6.4.3 The Conformal Window for SQCD 195

## 6.5 Seiberg Duality

6.5.1 Matching Symmetries 198 6.5.2 Completing the Phase Diagram for SQCD 201 6.5.3 Deformations of the Theories 204 6.5.4 Why Seiberg Duality is Electromagnetic Duality 207 Acknowledgements These lecture notes owe a debt to Graham Shore, from whom I first learned supersymmetry, and to Philip Argyres’ wonderful notes on the subject. I’m also grateful to Ben Allanach and Fernando Quevedo, both previous lecturers of the supersymmetry course in Cambridge.

This is one of the more advanced courses in Part III. It assumes a familiarity with quantum field theory, in particular the renormalisation group. You will also need to be comfortable with some group theory.

Spinor Conventions We work in Minkowski space with signature (+,−,−,−). Spinor indices are raised and lowered with ψα = ϵαβψβ and ψ¯α˙ = ϵα˙β˙ ψ¯β˙ where the invariant, anti-symmetric tensor is ϵαβ = ϵα˙β˙ = −ϵβα = −ϵβ˙α˙ = (cid:32) (cid:33)

0 1 −1 0 Left-handed spinors are contracted as ψχ = ψαχα and right-handed spinors are contracted as ψ¯χ¯ = ψ¯α˙χ¯α˙. Sigma matrices are defined by (σµ)αα˙ = (1,σi)αα˙ and (σ¯µ)α˙α = ϵαβϵα˙β˙ σµββ˙ = (1,−σi)α˙α and the generators of the Lorentz group in the left-handed and right-handed spinor representation are, respectively, (σµν)αβ = i/4 (σµσ¯ν −σνσ¯µ)αβ and (σ¯µν)α˙β˙ = i/4 (σ¯µσν −σ¯νσµ)α˙β˙

1 Introduction Supersymmetry is the name given to a novel symmetry that relates bosons and fermions. In many ways it is a surprise that such a symmetry could exist at all. This is because bosons and fermions are, to put it mildly, different.

Bosons are gregarious. Put many of them in a box and they huddle together to form a macroscopic quantum object called a Bose-Einstein condensate. In contrast, fermions are loners, an isolation enforced by the Pauli exclusion principle. Put many fermions in a box and you get a more familiar, but ultimately even stranger, state of quantum matter called a Fermi surface.

Within the framework of relativistic quantum field theories, the difference between fermions and bosons is even more stark. Fermions are matter particles. Bosons are force carriers. Any symmetry that relates the two must somehow entail a unification of matter and force.

Of course, we know from our earlier lessons on Quantum Field Theory that the distinction between bosons and fermion can be traced to something that is, in some sense, rather minor. They differ only by the simple matter of ℏ/2 in their angular momentum, with the spin-statistics theorem then doing the heavy lifting that ensures the resulting particles have such different properties. However, this too highlights just how unusual supersymmetry must be. The angular momentum of a particle is a property that follows from the symmetries of spacetime. Anything that relates particles with different angular momentum must involve some kind of extension of the symmetries of spacetime. And that sounds interesting!

All of this means that it’s not at all obvious that something like supersymmetry can exist and we should, if nothing else, be curious about how it can come about. But why else should we care? In the rest of this introduction, I give three reasons why studying supersymmetric quantum field theories is worthwhile.

Reason 1: Strongly Interacting Quantum Field Theories Quantum field theory is hard. This is particularly true when coupling constants, which specify the strength of interactions, are not small. This means that we can no longer understand the physics using the familiar methods of perturbation theory and Feynman diagrams. In this case, the word “hard” typically means “no one knows how to solve it”.

Supersymmetric theories are not wildly different from other quantum field theories. They have a carefully curated collection of fields, with some interactions tuned to take certain values, but otherwise they exhibit many of the strongly coupled phenomena expected of any other quantum field theory. The magic of supersymmetry, however, is that in many cases we are able to make exact statements about the properties of the theory. This is because supersymmetry places certain restrictions on the kind of dynamics that can occur. Fortuitously, it turns out that these restrictions are not strong enough to stop interesting things happening, but are strong enough to allow us to solve certain aspects of the theory. In this way, supersymmetric field theories provide an important collection of toy models that allow us to understand what quantum field theory can do in regimes where we would otherwise have very little control.

Here is an example. The theory of the strong nuclear force, QCD, exhibits a remarkable property known as confinement. Quarks are always trapped inside hadrons and 我们从未单独观测到孤立的夸克。毫无疑问，量子色动力学理论具有这个特性——我们在数值模拟中可以清晰地看到——但我们距离从第一性原理证明禁闭还很遥远。然而，存在一些与量子色动力学相似但物质成分略有不同的超对称规范理论，其中的禁闭可以被解析地证明。（这源于著名的Seiberg-Witten对N=2超对称理论的解。）虽然超对称的禁闭证明不能直接应用于现实世界的量子色动力学，但它仍然为我们理解禁闭在那种背景下如何发生提供了很好的直觉。

这些讲座将非常着重于利用超对称来探讨强耦合量子场论的有趣方面。我们将了解现实世界量子色动力学中存在的主题，如禁闭和手征对称性破缺，并看看它们在更容易处理的超对称理论中如何表现。我们还将学习一些看似与量子色动力学无关，但能让我们洞察强相互作用量子场论能力的新颖概念。其中最重要的就是对偶性的概念，即两个看起来截然不同的量子场论实际上可能描述相同的物理。

理由二：数学

随着我们对超对称场论的理解加深，人们发现其中潜藏着日益复杂的数学结构。这些主要（但不限于）是几何学的思想。

超对称与数学之间的联系始于一些简单的量子力学模型，其解为（除其他外）Morse理论和指标定理提供了新的视角。但真正的乐趣始于我们转向超对称场论时。对d=1+1维超对称场论的理解导致了镜对称的发现，这是拓扑不同流形之间的关系。随着我们转向更高维的量子场论，我们发现了更为精巧的结构，其中一些为数学家所知，另一些则是全新的。显然，还有更多有待揭示。

在这些讲座中，我们将不会讨论与数学的联系，尽管我们会在进行中遇到Kähler几何的概念，这至少让我们感受到有趣的几何概念是如何自然地从超对称中产生的。关于超对称量子力学的配套讲座则更侧重于超对称的数学方面，尽管没有深入该主题。

理由三：我们的世界

那个价值百万美元的问题是：超对称与我们的世界有任何关系吗？相当令人失望的答案是：我们不知道。

目前当然没有实验证据表明超对称是自然在基本层面上的一个对称性。而且，我们并非没有努力尝试。为阐明细节，我将首先解释我们的世界是超对称的意味着什么。然后我将解释我们有哪些（或曾经有哪些！）理由认为这可能成立。

在任何超对称理论中，粒子成对出现——一个是玻色子，另一个是费米子——这对粒子共享它们的许多性质，例如它们的质量和它们经历的力。你不需要建造大型强子对撞机就能意识到，我们的世界肯定不具备这个特性！没有与电子质量相同、电荷相同的玻色子；也没有与光子性质相同的无质量费米子。（不，中微子不符合！）简而言之，不存在超对称。

然而，并非所有对称性都在我们周围的世界中显现出来。这是因为对称性破缺现象，理论的动态性做出一个选择，从而掩盖了潜在的对称性。我们知道存在许多对称性破缺的例子，有些平凡而熟悉，有些则更奇特。这里举两个例子。在磁体中，所有自旋沿特定方向排列，打破了潜在的旋转对称性。在标准模型中，电弱对称性被希格斯玻色子打破，这确保了（左手）电子和中微子在低能下看起来非常不同，尽管它们在高能下是不可区分的。

很可能超对称是我们世界的一个对称性，但由于破缺而在低能下隐藏起来。如果是这样，破缺伴随一个我们将称之为M_{susy}的能量标度。所有超对 partner——每个玻色子/费米子对的另一半——的质量将大致在M_{susy}附近。因此，要回答超对称是否存在于自然界的问题，我们还必须解决伴生问题：M_{susy}的标度是多少？

多年来，超对称曾被视为超越标准模型的最有望候选理论，其中M_{susy}≈1 TeV。在这个标度下，超对称为等级问题提供了一个引人注目的解决方案。

The question of why the Higgs mass is not driven to higher scales by quantum fluctuations. Furthermore, if you adopt this solution then it comes with a number of happy consequences, from the unification of coupling constants to enticing candidates for dark matter.

However, with the advent of the LHC we have now explored the TeV scale and there is no sign of the predicted superpartners. It’s not quite game over: it may well be that these extra particles are lurking just around the corner, tantalisingly out of reach of our current accelerator and will be found as we go to higher energies. But it’s certainly fair to say that the parameter space of allowed theories has shrunk dramatically, as have our reasons for believing in supersymmetry at the TeV scale. This means that if supersymmetry is a symmetry of our world, it now appears to be broken at some scale M_susy ≳ 1 TeV. But where?

There is reason to think that supersymmetry might show up by the time we reach the Planck scale M_pl ≈ 10^15 TeV. This reason is string theory. Of course, we don’t know that string theory is the right theory of quantum gravity but it is presently the only viable candidate where a microscopic quantum theory gives the Einstein equations emerging at large distances. And string theory appears to require supersymmetry. (I include the word “appears” here because there are some open questions about bosonic (i.e. non-supersymmetric) string theory that we don’t have a good handle on and it may be premature to throw this out as a viable theory.)

So if you buy into string theory, then you’ll most likely want supersymmetry to be manifest by the time you get M_pl. And, as we’ve seen above, it looks like it should be broken at some scale M_susy ≳ 1 TeV. But there are 15 orders of magnitude between the TeV scale and the Planck scale. Where in this range should we expect supersymmetry to be broken if not at the TeV scale, or just above it, to provide a solution to the hierarchy problem? Sadly, I don’t think that we have any good idea, and there are no hints from nature that it is more useful to have M_susy at some large scale ≫ TeV rather than another.

This leaves us with the current situation, one of no small befuddlement about what role, if any, supersymmetry has to play in our world. Given this, in these lectures we won’t make any attempt to describe how supersymmetry may appear in our world. In particular, we will not devote effort to constructing supersymmetric versions of the Standard Model (the simplest is known as the MSSM where the first M stands for “minimal” and you can guess the rest) nor will we describe the many subtleties that come with how supersymmetry might be broken and how this manifests itself. Instead we will focus on places where supersymmetry has proved invaluable, viewing the theories as toy models to guide us in our understanding of quantum field theories.

## 1.1 A First Look at Supersymmetry

To motivate some of what lies ahead, we’ll jump in with a particularly simple supersymmetric theory. The theory consists of a single, complex scalar ϕ together with a 2-component Weyl fermion ψ. (If you’re unfamiliar with Weyl fermions, we’ll describe their properties in detail in Section 2.1.)

The following action has kinetic terms for these two fields, together with some carefully tuned interactions: S = ∫ d^4x [ ∂_μϕ†∂^μϕ − iψ†σ^μ ∂_μ ψ̄ ] − [ |∂W/∂ϕ|^2 + 1/2 (∂^2W/∂ϕ^2) ψψ + 1/2 (∂^2W†/∂ϕ†^2) ψ̄ψ̄ ] (1.1)

Here σ^μ = (1, σ^i) with σ^i the usual collection of three Pauli matrices. Note that there is a relation between the scalar potential V(ϕ) = |W′(ϕ)|^2 and the scalar-fermion interactions, both of which are dictated by a function W(ϕ) known as the superpotential.

If we want a renormalisable theory, this function should be no more than cubic: W(ϕ) = 1/2 mϕ^2 + 1/3 λϕ^3 This ensures that the potential is a quartic polynomial, V(ϕ) = |mϕ + λϕ^2|^2, while the scalar-fermion interactions take the usual Yukawa form ϕψψ. Crucially, the function W(ϕ) should be holomorphic: it depends only on ϕ and not on ϕ†. This fact will take on increasing significance as these lectures progress, but for now we will just take this as given.

Even without doing any detailed calculations, we can see that there’s something curious about the action (1.1): the boson ϕ and the fermion ψ have the same mass |m|. Usually in quantum field theory, we shouldn’t ascribe too much meaning to such an observation since masses receive quantum corrections and there’s no guarantee that the physical masses of two distinct particles will coincide just because the masses in the Lagrangian are equal. However, for the particular action (1.1), it turns out that the equality of bosonic and fermionic masses persists in the full quantum theory. This arises because the action enjoys a rather surprising symmetry, with the infinitesimal variation given by: δϕ = √2 ϵψ and δψ = √2 iσ^μ ϵ̄_μ ∂_μϕ − √2 ϵ (∂W†/∂ϕ†) (1.2)

This is our first example of supersymmetry. It is a symmetry that relates the bosonic field ϕ with the fermionic field ψ. Because ψ is a Grassmann field, while ϕ is not, the infinitesimal object ϵ, which parameterises the transformation, must also be a Grassmann-valued Weyl spinor. You can’t tell just by staring at the action (1.1) that it is invariant under the supersymmetry transformation (1.2). Instead, it takes a calculation, one that turns out to be a little bit of a headache. (Some balm for this headache will be offered in Section 3.2.3.) The action (1.1) is the simplest supersymmetric theory in d = 3+1 dimensions. It is known as the Wess-Zumino model. The existence of such a symmetry opens up a number of questions. What, if anything, is the symmetry good for? Are there other theories that also exhibit such symmetry? What properties might they have? All of these will be answered as these lectures progress. There is also another question that might have occurred to you: why is it such a pain to see that the action (1.1) is invariant under supersymmetry? Usually, the existence of symmetries in an action jumps out at you. Indeed, one of the main advantages of working with the Lagrangian approach, rather than the Hamiltonian approach, is that all symmetries are manifest. Typically you need do little more than ensure that various indices are contracted in the right way. This suggests that there may be a better way to write the action (1.1) that makes supersymmetry as obvious as any other symmetry. And there is. Our first task in these lectures – one that will carry us through much of Sections 2, 3 and 4 – is to better understand the structure behind supersymmetry and the corresponding supersymmetric actions.

2 The Supersymmetry Algebra The purpose of this section is to describe, in mathematical terms, what supersymmetry actually is. Usually in physics, we think of symmetries as associated to groups. But, at least for continuous symmetries, these groups have an underlying algebra and often that contains all the information that we need. So it is with supersymmetry. We will describe the algebra that underlies supersymmetry and start to explore some of its representations. I should warn you that this section will be a little dry in flavour. There will be few fields and certainly no dynamics. These will come in later sections. But this section lays the necessary groundwork for the stories that are to come.

## 2.1 The Lorentz Group

Minkowski space R1,3 is the stage for relativistic quantum field theory. This space comes equipped with the Minkowski metric η_μν = diag(+1,−1,−1,−1). The set of symmetries of Minkowski space include Lorentz transformations of the form x_μ → Λ_μ x_ν where Λ^T η Λ = η. Embedded among these are a couple of discrete transformations: parity with Λ = diag(1,−1,−1,−1) and time reversal with Λ = diag(−1,1,1,1). The transformations that are continuously connected to the identity have det Λ = 1 and Λ^0 > 0 and form the Lorentz group SO(1,3). (The restriction to Λ^0 > 0 is sometimes written as SO^+(1,3).) Our main goal in this section is to spell out some properties of the spinor representations of the Lorentz group. In fact, strictly speaking the group SO(1,3) doesn’t have any spinor representations. However, there is a closely related group called Spin(1,3) that does admit spinors. This is the double cover, in the sense that SO(1,3) ∼ = Spin(1,3)/Z_2, where that Z_2 is the famous minus sign that spinors pick up under a 2π rotation, a minus sign that vectors like x_μ are oblivious to. The fact that there are spinors in our world is the statement that the true symmetry group is Spin(1,3) rather than SO(1,3). When we introduced spinors in the Quantum Field Theory course, we did so by first looking at the algebra so(1,3) that is shared by both groups Spin(1,3) and SO(1,3). A Lorentz transformation acting on a 4-vector can be written as Λ_μν = exp(− ω_μν M^μν) (2.1), where ω_μν are six numbers that specify what Lorentz transformation we’re doing, while M_μν = −M_νμ are a choice of six 4 × 4 anti-symmetric matrices that generate the different Lorentz transformations. The matrix indices are suppressed in the above expressions; in their full glory we would write (M^μν)_ρ^σ. So, for example (M^{01})_ρ^σ = i diag(1, 1, -1, -1) and (M^{12})_ρ^σ = i diag(0, -1, 1, 0) (2.2) (Note that the generators differ by a factor of i from those defined in the Quantum Field Theory lectures. This is compensated by an extra factor of i in the exponent (2.1).) The matrices generate the algebra so(1,3), [M_μν, M_ρσ] = i(η_νρ M_μσ − η_νσ M_μρ + η_μσ M_νρ − η_μρ M_νσ) (2.3) In the lectures on Quantum Field Theory, we then constructed the spinor representations by first looking at the Clifford algebra of gamma matrices, {γ^μ, γ^ν} = 2η^μν and, from these, constructing a new representation of the Lorentz algebra (2.3). Here, we’ll take a slightly different path. It will be useful to first extract a little 从代数 (2.3) 中获得更多信息。

六个不同的洛伦兹变换自然分解为三个旋转 J 和三个推促 K，其定义为： J_i = ε_{ijk} M_{jk} 和 K_i = M_{0i} 其中下标 j,k = 1,2,3 求和，且 ε_{123} = +1。旋转矩阵是厄米的，满足 J_i† = J_i，而推促矩阵是反厄米的，满足 K_i† = −K_i。这确保了 (2.1) 中的旋转生成一个紧致群，而推促是非紧致的。从洛伦兹代数中，我们发现这些生成元满足： [J_i, J_j] = iε_{ijk} J_k, [J_i, K_j] = iε_{ijk} K_k, [K_i, K_j] = −iε_{ijk} J_k 旋转构成一个 su(2) 子代数。这当然是预期之中的，并且与事实 SO(3) ≅ SU(2)/ℤ₂ 相关。

然而，我们可以在 so(1,3) 内找到两个相互对易的 su(2) 代数。为此我们取线性组合： A_i = (J_i + iK_i)/2 和 B_i = (J_i − iK_i)/2 这两者都是厄米的，满足 A_i† = A_i 和 B_i† = B_i。它们满足： [A_i, A_j] = iε_{ijk} A_k, [B_i, B_j] = iε_{ijk} B_k, [A_i, B_j] = 0 (2.4)

但我们知道 SU(2) 的表示：它们由整数或半整数 j ∈ ℤ/2 标记，在旋转的背景下，我们称之为“自旋”。表示的维数是 2j + 1。我们能在洛伦兹代数中找到两个 su(2) 子代数的事实告诉我们，所有表示必须携带两个这样的标签 (j₁, j₂)，其中 j₁, j₂ ∈ ℤ/2 (2.5)，并且维数为 (2j₁+1)(2j₂+1)。我们将在下文详细阐述这些表示的含义。但目前，我们可以通过计数来识别最简单的表示：我们有： (0,0)：标量 (1/2,0)：左手外尔旋量 (0,1/2)：右手外尔旋量 (1/2,1/2)：矢量 (1,0)：自对偶 2-形式 (0,1)：反自对偶 2-形式我们看到洛伦兹群的最小表示是左手和右手外尔旋量。我们称之为粒子物理自旋的量是在旋转 J 下的量子数：即 j = j₁ + j₂。

关于发现两个 su(2) 子代数这件事，有某种不寻常之处。毕竟，洛伦兹群同构于两个 SU(2) 的拷贝当然不是真的。这是因为 SU(2) 是一个紧致群：持续做旋转，你最终会回到起点。确实，两个 SU(2) 群的拷贝给出欧几里得空间 ℝ⁴ 的旋转群： Spin(4) ≅ SU(2)×SU(2)，其中 SO(4) ≅ Spin(4)/ℤ₂ 相比之下，洛伦兹群是非紧致的：持续推促，你会离起点越来越远。这如何在我们于 (2.4) 中找到的两个 su(2) 代数中体现出来呢？

答案有点微妙，可以在生成元 A_i 和 B_i 的实性性质中找到。回想一下 SU(2) 的所有整数 j ∈ ℤ 表示都是实的，而所有半整数自旋 j ∈ ℤ + 1/2 的表示是赝实的（这意味着，虽然不是实际的实，但该表示与其复共轭同构）。然而，(2.4) 中的 A_i 和 B_i 不具有这些性质。你可以从 (2.2) 中看到 J_i 和 K_i 都是纯虚的。这反过来意味着生成元 A_i 和 B_i 是彼此的复共轭： (A_i)⋆ = −B_i 这就是区分 SO(4) 和 SO(1,3) 的差异所在。李代数 so(1,3) 不包含两个相互对易的实李代数 su(2) 拷贝，而仅在适当的复化之后才包含。这意味着李代数 su(2)×su(2) 的某些复线性组合与 so(1,3) 同构。为了强调这一点，两者之间的关系有时写为： so(1,3) ≅ su(2)×su(2)⋆ 就我们的目的而言，这意味着表示 (j₁, j₂) 的复共轭交换两个量子数： (j₁, j₂)⋆ = (j₂, j₁)

标量表示 (0,0) 和矢量表示 (1/2,1/2) 都是实的，而左手和右手外尔旋量 (1/2,0) 和 (0,1/2) 在复共轭下交换。这最后一个陈述在我们继续讨论时将很重要。在量子场论的背景下，如果一个场出现在理论中，那么它的复共轭也会出现。这意味着如果你有一个左手旋量，你也会有一个右手的复共轭旋量。

2.1.1 旋量与 SL(2,ℂ)

发现旋量还有另一种方式，这次不涉及通过代数。我们将使用两个群之间存在同构的事实： Spin(1,3) ≅ SL(2,ℂ) (2.6)

为了看到这一点，我们首先注意到我们可以将闵可夫斯基空间中的点 x^μ 写成一个 2×2 厄米矩阵： X = x_μ σ^μ = ⎛ x₀ + x₃   x₁ − i x₂ ⎞ ⎝ x₁ + i x₂   x₀ − x₃ ⎠ 其中我们引入了 4-矢量 2×2 矩阵： σ^μ = (1, σ_i)，其中 σ₁ = ⎛ 0  1 ⎞，σ₂ = ⎛ 0  −i ⎞，σ₃ = ⎛ 1  0 ⎞ (2.7)

⎝ 1  0 ⎠     ⎝ i   0 ⎠     ⎝ 0  −1 ⎠ σ_i 当然是泡利矩阵。矩阵 X 是厄米的：X = X†。而且，4-矢量 x^μ 与 2×2 厄米矩阵之间显然存在一一对应关系。闵可夫斯基 inner product is particularly natural in this language: detX = (x0)² − (x1)² − (x2)² − (x3)² = xµxµ Now consider an SL(2,C) transformation that acts as X → X′ = SXS† (2.8)

with S ∈ SL(2,C). We have (X′)† = X′ and detX′ = detX since detS = 1. This means that the map (2.8) must be a Lorentz transformation.

In fact, it is not hard to see that we can implement all Lorentz transformations this way and we’ll give an explicit construction of the generators shortly. For now, we can just do some simple counting. A general complex 2×2 matrix has 4 complex entries. The requirement that its determinant is 1 reduces this to 3 complex parameters, or 6 real parameters. This agrees with the dimension of the Lorentz group: 6 = 3 rotations + 3 boosts. Moreover, the SL(2,C) transformation S = −1 does not act on X, which is the reason why SL(2,C) coincides with the double cover (2.6).

It is clear that the fundamental representation of SL(2,C) is not a 2×2 matrix: it is a 2-component, complex object ψ = (ψ1, ψ2) that transforms as ψα → Sαβ ψβ, α,β = 1,2 Clearly it is a complex two-dimensional representation. In terms of our previous classification (2.5), we take it to correspond to (1,0): it is what we call a left-handed Weyl spinor.

Given any complex representation of a Lie group, we can always form another representation by taking the conjugate. This is equivalent to the original if we can find a matrix C for which S⋆ = CSC⁻¹. In the present case, no such C exists and the matrix S and its conjugate S⋆ are inequivalent representations. We denote the complex conjugate as (ψα)† = ψ̄α̇ We’ve adopted two notational flourishes to distinguish the two representations. First, we use different indices α,β = 1,2 and α̇,β̇ = 1,2 for the two different representations. This is useful because the two indices are telling us that the objects transform in different ways. In addition, we also add a bar over any object, like ψ, that transforms in the conjugate representation. This allows us to identify these objects even when we suppress the indices. (Note that a bar on a Weyl spinor simply means complex conjugation while, as we learned in the Quantum Field Theory lectures, a bar on a Dirac spinor means complex transpose together with multiplication by γ0.) The complex conjugate spinor then transforms as ψ̄α̇ → (S⋆)α̇β̇ ψ̄β̇, α̇,β̇ = 1,2 In our previous classification (2.5) it is the representation (0,1). It is a right-handed Weyl spinor.

Some of the index conventions above (and below) differ from what you may have seen in other contexts and it’s worth quickly explaining why. Suppose that we’ve got a vector u that transforms in the fundamental of SU(N). We write the components as ua with a = 1,...,N. The vector u† transforms in the conjugate representation and we would write these components as (u†)a, with the index raised and no dots in sight. This reflects the fact that we can contract u† and u to form a singlet: (u†)aua. However, the representations of SL(2,C) have a different structure and, as we’ll see shortly, you can’t contract a spinor and its conjugate to get a singlet. That’s why we introduce the strange looking dotted indices, rather than raising the index, to distinguish the conjugate representation.

**Building Scalars from Spinors** The group SL(2,C) has the following invariant tensors ϵαβ = (0 1; −1 0), ϵα̇β̇ = (0 1; −1 0), and ϵαβ = (0 −1; 1 0), ϵα̇β̇ = (0 −1; 1 0)

Note that the ϵ with indices lowered differs by a minus sign from ϵαβ. This ensures that one is the inverse of the other: ϵαβϵβγ = δαγ. This, in turn, means that when we use epsilon symbols to raise and lower indices (as we will below) then if we choose to raise an index and subsequently lower it again then we don’t get a minus sign for our troubles.

Given, say, two left-handed Weyl fermions ψ and χ, we can use the epsilon tensors to form invariants. We define ψχ := ϵαβψαχβ = ψ1χ2 − ψ2χ1 To see that these are, indeed, invariants under SL(2,C), we just need to perform a transformation ψχ → Sγα Sδβ ϵαβ ψγχδ = (detS)ϵγδ ψγχδ = ψχ (2.9)

where, in the first equality we’ve used the fact that Sγα Sδβ ϵαβ = detS ϵγδ, which you can confirm simply by checking all the cases γ,δ = 1,2. In the second equality we’ve used the fact that detS = 1.

In some ways, the ϵ symbols play a role for spinors that is akin to role played by the metric ηµν for vectors. Of course, one key difference is that ϵαβ is anti-symmetric, but this tallies nicely with the fact that, in quantum field theory, spinors are anti-commuting Grassmann variables. We then have ψχ = ψ1χ2 − ψ2χ1 = −χ1ψ2 + χ2ψ1 = χψ In particular, ψψ = 2ψ1ψ2 is non-vanishing.

We can do something similar for right-handed fermions. However, a fiddly minus sign rears its head. We define χ̄ψ̄ := ϵα̇β̇ χ̄α̇ψ̄β̇ = χ̄1ψ̄2 − χ̄2ψ̄1 (2.10)

With anti-commuting spinors, we again have χ̄ψ̄ = ψ̄χ̄. Note that the ordering of the indices in (2.10) differs from (2.9). The reason for ch Choosing this different ordering, resulting in a minus sign difference in the definitions, is that it ensures that \((\psi\chi)^\dagger = \bar{\psi}\bar{\chi}\), since \[ (\psi\chi)^\dagger = (\psi_1\chi_2 - \psi_2\chi_1)^\dagger = \bar{\chi}_2\bar{\psi}_1 - \bar{\chi}_1\bar{\psi}_2 = \bar{\psi}_1\bar{\chi}_2 - \bar{\psi}_2\bar{\chi}_1 = \bar{\psi}\bar{\chi}.

\]

We can use the \(\epsilon\) symbols to raise and lower spinor indices, just as we use the Minkowski metric to raise and lower vector indices. We have \[ \psi^\alpha = \epsilon^{\alpha\beta}\psi_\beta, \quad \psi_\alpha = \epsilon_{\alpha\beta}\psi^\beta \quad \text{and} \quad \bar{\psi}^{\dot{\alpha}} = \epsilon^{\dot{\alpha}\dot{\beta}}\bar{\psi}_{\dot{\beta}}, \quad \bar{\psi}_{\dot{\alpha}} = \epsilon_{\dot{\alpha}\dot{\beta}}\bar{\psi}^{\dot{\beta}}.

\]

In this notation, the Lorentz scalars (2.10) become \[ \psi\chi = \psi^\alpha\chi_\alpha \quad \text{and} \quad \bar{\psi}\bar{\chi} = \bar{\psi}_{\dot{\alpha}}\bar{\chi}^{\dot{\alpha}}.

\]

Our fiddly minus sign difference between (2.9) and (2.10) has now transmuted into the following rule: for left-handed spinors we should contract (undotted) indices in the direction ↘, while for right-handed spinors we should contract (dotted) indices in the direction ↗.

We can ask how these new objects \(\psi^\alpha\) and \(\bar{\psi}^{\dot{\alpha}}\) fare under Lorentz transformations. We have \[ \psi^\alpha \rightarrow \epsilon^{\alpha\beta}S_\gamma{}^\psi_\beta = (S^{-1})^\alpha{}_\beta \psi^\beta, \]

\[ \bar{\psi}^{\dot{\alpha}} \rightarrow \epsilon^{\dot{\alpha}\dot{\beta}}(S^\star)_\dot{\gamma}{}^{\bar{\psi}}_{\dot{\beta}} = (S^{-1\dagger})^{\dot{\alpha}}{}_{\dot{\beta}} \bar{\psi}^{\dot{\beta}} \quad (2.11)

\]

where the equality follows from the following algebra \[ S_\gamma{}^\epsilon{}^{\alpha\beta}S_\delta{}^\gamma = \epsilon^{\delta\beta} \Rightarrow (ST)^\gamma{}_\alpha \epsilon^{\alpha\beta}S_\delta{}^\gamma = \epsilon_{\delta\beta} \Rightarrow \epsilon^{\alpha\beta}S_\delta{}^\gamma = (S^{-1}T)^\alpha{}_\beta \epsilon_{\gamma\delta} \]

with similar manipulations for the right-handed spinor. The matrices \(S^{-1}T\) don't form a new representation of \(SL(2,\mathbb{C})\); they are equivalent to the fundamental representation since, from above, we have \(\epsilon S \epsilon^{-1} = S^{-1}T\). This means that the covariant and contravariant left-handed spinors \(\psi_\alpha\) and \(\psi^\alpha\) transform in equivalent representations. Similarly, the right-handed spinors \(\bar{\psi}_{\dot{\alpha}}\) and \(\bar{\psi}^{\dot{\alpha}}\) transform in equivalent representations.

**Building Vectors from Spinors** A key take-away from our discussion above is that if you want to form a Lorentz scalar then you need a pair of left-handed fermions or a pair of right-handed fermions. Suppose that we instead have one object of each type, say a left-handed spinor \(\psi_\alpha\) and a right-handed spinor \(\bar{\psi}_{\dot{\alpha}}\). What kind of object can we then build? The answer is clear from the quantum numbers of these representations: \[ \left(\frac{1}{2},0\right) \otimes \left(0, \frac{1}{2}\right) = \left(\frac{1}{2}, \frac{1}{2}\right).

\]

This is the vector representation of the Poincaré group.

To explicitly construct the vector, we sandwich the Pauli matrices \[ (\sigma^\mu)^{\alpha\dot{\alpha}} = (1, \sigma^i)

\]

between two spinors. We write \[ \psi\sigma^\mu\bar{\chi} = \psi_\alpha (\sigma^\mu)^{\alpha\dot{\alpha}} \bar{\chi}_{\dot{\alpha}}.

\]

Note that, as shown above, the Pauli matrices \(\sigma^\mu\) should come with an index of each type – one undotted, and one dotted – and both subscripts. Taking the conjugate, we have \((\psi\sigma^\mu\bar{\chi})^\dagger = \chi\sigma^\mu\bar{\psi}\).

To see that the object does indeed transform as a 4-vector, we can contract this with any other 4-vector \(x_\mu\) to give \(\psi X \bar{\chi}\) with \(X = x_\mu \sigma^\mu\). But we know from (2.8) and (2.11) how each of these transforms: we then have \[ \psi X \bar{\chi} = \psi_\alpha X^{\alpha\dot{\alpha}} \bar{\chi}_{\dot{\alpha}} \rightarrow (\psi_\beta (S^{-1})^\beta{}_\alpha) (S_\delta{}^\alpha X^{\delta\dot{\delta}} (S^\star)_{\dot{\delta}}{}^{\dot{\alpha}}) (\bar{\chi}_{\dot{\beta}} (S^{\star-1})^{\dot{\beta}}{}_{\dot{\alpha}}) = \psi X \bar{\chi}.

\]

The fact that \(\psi X \bar{\chi}\) forms a singlet shows that \(\psi \sigma^\mu \bar{\chi}\) must transform as a vector. In fancy maths words, we say that the Pauli matrices act as the intertwiner between the different representations.

We can use the epsilon symbols to raise the spinor indices on the Pauli matrices \(\sigma^\mu_{\alpha\dot{\alpha}}\). This gives us a closely related set of matrices that we denote \[ (\bar{\sigma}^\mu)^{\dot{\alpha}\alpha} = \epsilon^{\alpha\beta} \epsilon^{\dot{\alpha}\dot{\beta}} \sigma^\mu_{\beta\dot{\beta}}.

\]

The bar on \(\bar{\sigma}\) doesn't denote anything to do with complex conjugation. The \(\bar{\sigma}^\mu\) are simply a different set of 2×2 matrices from \(\sigma^\mu\). Note that the indices have not only been raised, but also switched: \(\sigma^\mu\) has the undotted index first, while \(\bar{\sigma}^\mu\) has the dotted index first. If we define \(\epsilon = i\sigma_2\) then, viewed as matrix multiplication, we have \(\bar{\sigma}^\mu = \epsilon \sigma^{\mu T} \epsilon^T\). A quick calculation shows that \[ (\bar{\sigma}^\mu)^{\dot{\alpha}\alpha} = (1, -\sigma^i)^{\dot{\alpha}\alpha}.

\]

We can then similarly construct the vector \[ \bar{\chi}\bar{\sigma}^\mu\psi = \bar{\chi}_{\dot{\alpha}} (\bar{\sigma}^\mu)^{\dot{\alpha}\alpha} \psi_\alpha.

\]

This isn't a new object: you can check that \(\psi\sigma^\mu\bar{\chi} = -\bar{\chi}\bar{\sigma}^\mu\psi\).

**Generators of SL(2, C)** Finally we can give a description of the generators of \(SL(2,\mathbb{C})\). We define the anti-symmetrised product of sigma matrices, \[ (\sigma^{\mu\nu})_\alpha{}^\beta = \frac{1}{4}(\sigma^\mu \bar{\sigma}^\nu - \sigma^\nu \bar{\sigma}^\mu)_\alpha{}^\beta.

\]

These are linearly independent and so can be taken as a generator of \(SL(2,\mathbb{C})\). Because of the anti-symmetry in \(\mu\) and \(\nu\), there are six such generators which is the dimension of the Lorentz group. Indeed, we can see explicitly that these generate the Lorentz group by computing the commutator \[ [\sigma^{\mu\nu}, \sigma^{\rho\sigma}] = i(\eta^{\nu\rho}\sigma^{\mu\sigma} - \eta^{\nu\sigma}\sigma^{\mu\rho} + \eta^{\mu\sigma}\sigma^{\nu\rho} - \eta^{\mu\rho}\sigma^{\nu\sigma}).

\]

This reproduces the algebra of the Lorentz group (2.3) as promised. A left-handed spinor then transforms as \[ \psi_\alpha \rightarrow \exp\left(-\frac{i}{2} \omega_{\mu\nu} \sigma^{\mu\nu}\right)_\alpha{}^\beta \psi_\beta \quad (2.12)

\]

where \(\omega_{\mu\nu}\) are the same set of six numbers that specify the Lorentz transformation (2.1).

The conjugate representation is generated by \[ (\bar{\sigma}^{\mu\nu})_{\dot{\alpha}}{}^{\dot{\beta}} = \frac{1}{4}(\bar{\sigma}^\mu \sigma^\nu - \bar{\sigma}^\nu \sigma^\mu)_{\dot{\alpha}}{}^{\dot{\beta}}.

\]

These too satisfy the algebra of the Lorentz group. Correspondingly, a right-handed spinor transforms as \[ \bar{\psi}^{\dot{\alpha}} \rightarrow \exp\left(-\frac{i}{2} \omega_{\mu\nu} \bar{\sigma}^{\mu\nu}\right)^{\dot{\alpha}}{}_{\dot{\beta}} \bar{\psi}^{\dot{\beta}} \quad (2.13)

\]

Note that, from the positioning of the indices of \(\bar{\sigma}^{\mu\nu}\), these act naturally as generators on \(\bar{\psi}^{\dot{\alpha}}\), with the index raised.

**2.1.2 Lagrangians for Spinors** We can now describe how to construct Lagrangians from a Weyl spinor. Suppose that we have just a single left-handed Weyl spinor \(\psi_\alpha\) to play with. This necessarily comes with its conjugate, a right-handed spinor \(\bar{\psi}_{\dot{\alpha}} = \psi^\dagger_{\dot{\alpha}}\). We can then form a kinetic term \[ S = -\int d^4x \, i \bar{\psi}_{\dot{\alpha}} \bar{\sigma}^{\mu\dot{\alpha}\alpha} \partial_\mu \psi_\alpha. \quad (2.14)

\]

Upon quantisation, this theory gives a s single massless, left-handed fermion of helicity −1 and massless right-handed anti-particle of helicity +1. The theory has a global U(1) symmetry under which ψ → eiαψ; if the left-handed fermion has charge +1 then the right-handed fermion has charge −1, as befits an anti-particle.

We can add a mass term for a single Weyl fermion. This is known as a Majorana mass, S_{Maj} = ∫ d⁴x ( m ψψ + m⋆ ψ̄ψ̄ ) / 2 (2.15)

In general, we can take m ∈ C although any complex phase of m can be absorbed into ψ and, upon quantisation, the resulting particle has mass |m|. Importantly, the Majorana mass explicitly breaks the global U(1) symmetry, so there is no quantum number to distinguish particle from anti-particle. Upon quantisation, the theory consists of a single massive spin 1/2 particle that is now its own anti-particle.

Because the Majorana mass term explicitly breaks the U(1) symmetry, it is not allowed if the U(1) is gauged. Relatedly, it’s not possible to write down such a term for any fermion ψ that transforms in a complex representation of a gauge group. It is, however, possible to write down such terms for fermions in real representations.

Recovering Dirac Spinors All this discussion of spinors and, so far, not a gamma matrix or Clifford algebra in sight! Yet these played a central role in the discussion of spinors that we met in the Quantum Field Theory lectures. What’s going on?

The Dirac spinor is not an irreducible representation of the Lorentz group in d = 3+1 dimensions. Instead, it consists of independent left- and right-handed spinors. In our earlier notation: (1,0) ⊕ (0, 1/2) : Dirac spinor We write a Dirac spinor as a 4-component object, consisting of a left-handed Weyl fermion ψα and a right-handed Weyl fermion χ̄α̇ (note the index up), Ψ = ( χ̄α̇  ψα )

We also introduce the chiral basis of gamma matrices γμ = ( 0 σμ / σ̄μ 0 ) (2.16)

These obey the Clifford algebra {γμ, γν} = 2ημν. In the Quantum Field Theory lectures, we showed that the generators of Lorentz transformations for a Dirac spinor are Sμν = i/4 [γμ, γν] = ( i σμν 0 / 0 -i σ̄μν )

(As with our earlier definition of Mμν, this differs by a factor of i from the conventions in the Quantum Field Theory lectures.) Under a Lorentz transformation, a Dirac spinor transforms as Ψ → exp(-i/2 ωμν Sμν) Ψ. This reproduces the transformations of Weyl spinors that we saw in (2.12) and (2.13).

The Dirac action that we met in our Quantum Field Theory lectures is S_{Dirac} = -∫ d⁴x i Ψ̄ γμ ∂μ Ψ - M Ψ̄ Ψ where, for a Dirac spinor (but not a Weyl spinor!) the bar notation means Ψ̄ = Ψ† γ0. Decomposed in terms of Weyl fermions, it becomes S_{Dirac} = -∫ d⁴x i ψ̄ σ̄μ ∂μ ψ + i χ σμ ∂μ χ̄ - M(χ ψ + ψ̄ χ̄) (2.17)

The first term coincides with the kinetic term (2.14) for a left-handed fermion. The second term is simply a different way of writing this, with the derivative now acting on a right-handed fermion; if you play around lowering and raising indices then the second term can be massaged to look like the first.

The mass term in (2.17) is not of the Majorana type (2.15). First, the mass is necessarily real, M ∈ R, although it can be positive or negative. Second, because the mass term involves two distinct Weyl fermions it preserves a U(1) symmetry, under which the phase of ψ and χ rotate oppositely. The result is that, upon quantisation, the action (2.17) gives a particle of spin +1/2 and charge +1, together with a distinct anti-particle of spin +1/2 and charge −1, both with mass |M|.

It is possible to restrict the Dirac fermion Ψ to have the same content as a single Weyl fermion. In a general basis of gamma matrices, we do this by introducing a charge conjugation matrix. But in the chiral basis (2.16), it’s particularly simple: we just restrict χ̄ = ψ̄ ≡ ψ†. A Dirac spinor with such a restriction is called a Majorana spinor.

Throughout these lectures, we will have no need to resort to 4-component spinors. We will write everything in terms of 2-component Weyl fermions.

2.1.3 The Poincaré Group and its Extensions The continuous symmetries of Minkowski space comprise of Lorentz transformations together with spacetime translations. Combined, these form the Poincaré group. Spacetime translations are generated, as usual, by the momentum 4-vector Pμ. Their commutation relations with themselves and with the Lorentz generators Mμν are given by [Pμ, Pν] = 0 and [Mμν, Pσ] = i(Pμ ηνσ - Pν ημσ) (2.18)

The latter of these is equivalent to the statement that Pμ transforms as a 4-vector under Lorentz transformations. These commutation relations should be considered in conjunction with the Lorentz algebra (2.3), [Mμν, Mρσ] = i(ηνρ Mμσ - ηνσ Mμρ + ημσ Mνρ - ημρ Mνσ) (2.19)

Together, (2.18) and (2.19) form the algebra of the Poincaré group.

It’s not unusual for quantum field theories to exhibit further continuous symmetries. Say, a global U(1) symmetry that rotates the phase of a complex field, or perhaps a non-Abelian SU(N) symmetry under which a multiplet of fields transforms. The generators of these symmetries – which we’ll denote collectively as T – correspond to some conserved charge or isospin and are always Lorentz scalars. This means that they necessarily commute with the Poincaré generators, [Pµ,T] = [Mµν,T] = 0. One could ask: is it possible for something less trivial to happen, with the new generators transforming in some interesting fashion under the Poincaré group? For example, this would happen if the additional generators T themselves carried some spacetime index. If this were possible, the Poincaré group would be subsumed into a larger group. And that sounds interesting.

A theorem due to Coleman and Mandula greatly restricts this possibility. Roughly speaking, the theorem states that, in any spacetime dimension greater than d = 1+1, the symmetry group of any interacting quantum field theory must factorise as Poincaré × Internal (2.20). We won’t prove the Coleman-Mandula theorem here1. The gist of the proof is that Poincaré invariance already greatly restricts what can happen in, say, 2 to 2 scattering, with only the scattering angle left undetermined. Any internal symmetries that factorise, as in (2.20), put restrictions on the kinds of interactions that are allowed, for example enforcing conservation of electric charge. But if the generators T were to carry a spacetime index then they would put further constraints on the scattering angle itself and that would be overly restrictive, at best allowing scattering to occur only at discrete angles. But if one assumes that the scattering amplitudes are analytic functions of the angle then the amplitude must vanish for all angles and the theory is free.

1The original Coleman-Mandula paper is from 1967 and entitled “All Possible Symmetries of the S-matrix”. Witten’s “Introduction to Supersymmetry” lectures give a clear intuitive explanation of the theorem. A full proof can be found Weinberg vol III.

Like all no-go theorems in physics, the Coleman-Mandula theorem comes with a number of underlying assumptions. Some of these are eminently reasonable, such as locality and causality. But it may be possible to relax other assumptions to find interesting loopholes to the Coleman-Mandula theorem. Two such loopholes have proven to be extremely important.

• Conformal Invariance: The Coleman-Mandula theorem assumes that the theory has a mass gap, meaning that all particles are massive. Indeed, it studies symmetries of the S-matrix which is really only well defined for massive particles where we don’t have to worry about IR divergences. For theories of massless particles something interesting can, and often does, happen. The first interesting thing is that interacting massless theories typically exhibit scale invariance. This means that physics is unchanged under the symmetry xµ → λxµ. The associated symmetry generator is called D for “dilatation”. This can only be a symmetry of a theory that has no dimensionful parameters. In particular, no masses. The second interesting thing is more surprising. For reasons that are not entirely understood, theories that exhibit scale invariance also exhibit a further symmetry known as special conformal transformations of the form xµ → (xµ − aµx2)/(1 − 2a·x + a2x2). This transformation depends on a vector parameter aµ and the associated generator is a 4-vector Kµ. The resulting conformal algebra extends the Poincaré algebra (2.18) and (2.19) with the non-trivial commutators [D,Kµ] = −iKµ, [D,Pµ] = iPµ, [Kµ,Pν] = 2i(Dηµν − Mµν), [Mµν,Kσ] = i(Kνηµσ − Kµηνσ). Interacting conformal field theories crop up in many places in physics. In their Euclidean incarnation, they describe critical points, or second order phase transitions, that were the focus of our lectures on Statistical Field Theory. In d = 1+1 dimensions the conformal group has rather more structure and a detailed introduction can be found in the lectures on String Theory. We’ll meet examples of supersymmetric conformal field theories later in Section 6.4 when we discuss the low-energy physics of certain gauge theories.

• Supersymmetry: The second loophole to the Coleman-Mandula theorem is supersymmetry. As you may by now have guessed, exploiting this loophole will be the topic of the rest of these lectures.

## 2.2 The Supersymmetry Algebra

Supersymmetry evades the Coleman-Mandula no-go theorem because it is a different kind of symmetry. In contrast to the symmetries discussed above, it is not characterised by a Lie algebra. Instead it is characterised by a mathematical structure known as a Z₂-graded Lie algebra. For our purposes, this simply means that the algebra contains both commutation and anti-commutation relations.

A generalisation of the Coleman-Mandula theorem to graded Lie algebras was given by Haag, Lopuszanski and Sohnius. Roughly speaking, it says that the only possibility is supersymmetry. We will now, finally, explain what this means.

Supersymmetric theories have a new conserved charge that is a left-handed Weyl spinor Qα, together with its right-hand ed counterpart Q . This is known as the supercharge. It is possible to have multiple supercharges, a situation known as extended supersymmetry. We will discuss this in Section 2.4 and, for now, stick to just a single complex supercharge. This is known as N = 1 supersymmetry.

At the heart of the supersymmetry algebra is the anti-commutation relation {Qα ,Q̄α̇} = 2σµαα̇ Pµ (2.21)

It is no surprise that a spinor should have an anti-commutator. But the structure of this relation is interesting: it tells us that the supercharges should be viewed as the square-root of spacetime translations! Our goal in these lectures is to understand what, exactly, this means.

The full supersymmetry algebra comprises of commutation relations (2.18) and (2.19) of the Poincaré group, which remain unchanged, together with the (anti)-commutation relations of the supercharges. The first of these is [Mµν,Qα ] = (σµν)αβ Qβ and [Mµν,Q̄α̇] = (σ̄µν)α̇β̇ Q̄β̇ (2.22)

This is simply the statement that the supercharges transform under a Lorentz transformation in the manner expected of operators that are Weyl fermions. To see this, first recall from (2.12) that any spinor like Q transforms as Qα → Uαβ Qβ where U = exp(−iωµν σµν). But Q is also an operator acting on a Hilbert space and, viewed through this lens, we get a different expression for how it transforms. Any state in the Hilbert space transforms as |ϕ⟩ → V|ϕ⟩ with V = exp(−iωµν Mµν). Here, Mµν is the abstract generator of Lorentz transformations and its action on any state depends on the quantum number of that state. Correspondingly, operators O transform as O → VOV† since this ensures that the matrix elements ⟨ϕ′|O|ϕ⟩ remains unchanged. Equating these two ways in which the supercharge transforms, we have VQα V† = (UQ)α. The algebra (2.22) is the infinitesimal version of this transformation law.

The remaining commutation relations are somewhat less interesting, although no less important [Qα ,Pµ] = {Qα ,Qβ} = 0 (2.23)

There are, however, reasons why these commutators take this boring form.

First, why do we necessarily have [Qα ,Pµ] = 0? Clearly the right-hand side should be something with α and µ indices so that the commutator is covariant under Lorentz transformations. But that leaves the option for [Qα ,Pµ] = c(σµ)αα̇ Q̄α̇ for some c ∈ C. What forces us to have c = 0?

The answer to this lies in the Jacobi identity [Pµ,[Pν,Qα]] + [Pν,[Qα ,Pµ]] + [Qα ,[Pµ,Pν]] = 0 Clearly the last term vanishes, as [Pµ,Pν] = 0. If we choose [Qα ,Pµ] = c(σµ)αα̇ Q̄α̇ and, correspondingly, [Q̄α̇,Pµ] = c⋆(σ̄µ)α̇β Q̄β then the Jacobi identity becomes −cσναα̇ [Pµ,Q̄α̇] + cσµαα̇ [Pν,Q̄α̇] = |c|2(σνσ̄µ −σµσ̄ν)αβ Qβ = 0 This requires c = 0.

There is a similar reason for why we must have {Qα ,Qβ} = 0. Once again, there is an alternative since if we just try to pair up indices then we might think that {Qα ,Qβ} = c′(σµν)αβ Mµν would be acceptable for any c′ ∈ R. But if we take the commutator with Pρ then, from the argument above, the left-hand-side must vanish which, because [Pρ,Mµν] ≠ 0, tells us that c′ = 0.

(An aside: there’s actually a subtlety in this last discussion. While it is true that {Qα ,Qβ} = 0 when sandwiched between any finite energy states, some supersymmetric theories have multiple ground states and it turns out that {Qα ,Qβ} can be non-vanishing when evaluated on the infinite energy domain walls that interpolate between these ground states. This subtlety is interesting, at least if you care about domain walls, but somewhat beyond the scope of these lectures.)

2.2.1 R-Symmetry We started this section by noting that all internal symmetries must commute with the spacetime symmetries of the Poincaré group. But must they also commute with the supercharge Q? The answer is: almost.

All internal symmetries must commute with Q with one exception: it may be that theories admit an internal U(1) symmetry that acts as Qα → e−iλ Qα and Q̄α̇ → eiλ Q̄α̇ (2.24)

This U(1) symmetry is known as an R-symmetry and is sometimes denoted U(1)R. If we denote the generator as R then it has commutation relations [R,Qα ] = −Qα and [R,Q̄α̇] = +Q̄α̇ (2.25)

When we turn to theories of extended supersymmetry in Section 2.4, we’ll see different R-symmetry groups arising. But for theories with N = 1 symmetry we have only U(1)R. Nonetheless, this will play an important role when we come to analyse the dynamics of supersymmetric theories in later sections. We’ll see this, for example, in Section 3.3.

This, then, is the supersymmetry algebra: it comprises of the algebra of the Poincaré group (2.18) and (2.19), together with the algebra of the supercharges (2.21), (2.22) and (2.23) and, finally, the R-symmetry (2.25). The next question is: what can we do with it?

2.2.2 A Consequence: Energy is Positive Even before we write down any field theories, we can derive one feature of supersymmetric theories from the algebra alone. This follows from the key algebraic rela (2.21), {Q_\alpha, \bar{Q}_{\dot{\alpha}}} = 2\sigma^\mu_{\alpha\dot{\alpha}} P_\mu (2.26)

If we compute the expectation of the left-hand side in any state |\phi\rangle then we find that it is necessarily positive \langle\phi|Q_\alpha \bar{Q}_{\dot{\alpha}} + \bar{Q}_{\dot{\alpha}} Q_\alpha|\phi\rangle = |(Q_\alpha)^\dagger|\phi\rangle|^2 + |Q_\alpha|\phi\rangle|^2 \geq 0 (2.27)

The same must be true of the right-hand side \sigma^\mu_{\alpha\dot{\alpha}} \langle\phi|P_\mu|\phi\rangle \geq 0 If we set \alpha = \dot{\alpha} and sum over \alpha = 1,2 then we make use of the fact that tr\sigma^0 = 2 and tr\sigma^i = 0. This then reduces to the statement that the energy of any state in a supersymmetric theory is necessarily positive \langle\phi|P_0|\phi\rangle \geq 0 This is curious. Usually in physics, we don’t care about the overall value of the energy: if you add an overall constant to all energies, then physics remains unchanged. There are two places where this state of affairs no longer holds. The first is in gravity where the energy of the vacuum contributes as a cosmological constant. The second is, as we’ve seen above, in supersymmetric theories where energies are necessarily positive definite.

Physically, it’s far from clear if there is any deep relation between these two ideas. In fact, as we will see later in these lectures, the energy of the ground state acts as an order parameter for the breaking of supersymmetry. This means that the ground state energy is zero if supersymmetry is exact, otherwise it is non-zero. In our world, it’s clear that there is no supersymmetry visible at the TeV scale, while the cosmological constant is many of orders of magnitude smaller, at 10^{-3} eV. This makes it difficult to see how supersymmetry can help alleviate the cosmological constant problem.

However, at the formal mathematical level, the relationship between supersymmetry and gravity has proven rather useful. For example, there exists a greatly simplified proof of the positive energy theorem in general relativity, due to Witten, that uses ideas of supersymmetry.

There is one further piece of physics hiding in (2.26). For any other symmetry in field theory, we can think about gauging it. This means that we try to construct theories in which the symmetry is realised locally. Supersymmetry is no different. One can construct theories in which the associated infinitesimal parameter for supersymmetry transformations depends on x^\mu. From (2.26), we see that such theories necessarily enjoy a symmetry in which you do different translations at different points in space. But such transformations are diffeomorphisms and are the characteristic feature of general relativity. In other words, theories of local supersymmetry are necessarily theories of gravity! Such theories are known as supergravity, usually shortened to the ugly acronym “sugra”. We will mention supergravity only very briefly in this section. In subsequent sections our interest will be entirely on theories with global supersymmetry.

Given an algebra, our next task is to explore its representations. There are different ways that we could approach this. Ultimately, we will be interested in quantum field theories that enjoy supersymmetry and this means understanding the way supersymmetry acts on fields. This we will do in later sections. Here, to build some intuition, we will understand how supersymmetry acts on single particle states in the Hilbert space.

Without doing any work, we can guess that something interesting is going on. The supercharge Q_\alpha is a fermionic operator, both in the sense that it carries spin 1/2 and in the sense that it is naturally anti-commuting as in (2.21). This means that, schematically, we must have Q|fermion\rangle = |boson\rangle and Q|boson\rangle = |fermion\rangle (2.28)

This is the defining feature of supersymmetry.

In fact, it is straightforward to show that any representation of the supersymmetry algebra must have an equal number of bosonic and fermionic states. To this end, we introduce the fermionic number operator (-1)^F. This acts on bosonic states as (-1)^F|B\rangle = |B\rangle and (-1)^F|F\rangle = -|F\rangle Because Q swaps a bosonic state for a fermionic state, we necessarily have (-1)^F Q_\alpha = -Q_\alpha (-1)^F \Rightarrow \{(-1)^F, Q_\alpha\} = 0 The result that we now want follows straightforwardly from the algebra \{Q_\alpha, \bar{Q}_{\dot{\alpha}}\} = 2\sigma^\mu_{\alpha\dot{\alpha}} P_\mu. Suppose that we have a finite collection of one-particle states that form a representation of the supersymmetry algebra. We can take the following trace over elements of this multiplet tr \left[ (-1)^F\{Q_\alpha, \bar{Q}_{\dot{\alpha}}\} \right] = tr \left[ (-1)^F Q_\alpha \bar{Q}_{\dot{\alpha}} + (-1)^F \bar{Q}_{\dot{\alpha}} Q_\alpha \right]

= tr \left[ -Q_\alpha (-1)^F \bar{Q}_{\dot{\alpha}} + (-1)^F \bar{Q}_{\dot{\alpha}} Q_\alpha \right] = 0 Here the second equality we’ve uses the fact that \{(-1)^F, Q_\alpha\} = 0 while the final equality uses the cyclicity of the trace. The supersymmetry algebra then tells us that \sigma^\mu_{\alpha\dot{\alpha}} tr \left[ (-1)^F P_\mu \right] = 0 Note that \sigma^\mu_{\alpha\dot{\alpha}} sits outside the trace over states: it’s just a bunch of numbers as far as the trace is concerned. Meanwhile P_\mu sits inside the trace because it is an operator acting on states. We can choose these states to be momentum eigenstates, so that P_\mu|any state\rangle = p_\mu|any state\rangle. We then simply have \sigma^\mu_{\alpha\dot{\alpha}} p_\mu tr(-1)^F = 0 But tr(-1)^F...

F simply counts the number of bosonic states n_B minus the number of fermionic states n_F, tr(−1)^F = n_B − n_F = 0 The number of such states must be equal. The quantity tr(−1)^F is called the Witten index.

There’s actually a loophole in the discussion above. It may be that Q_α and Q_α̇ annihilate states in the supersymmetry multiplet. From the supersymmetry algebra (and the positivity conditions (2.27) that follows from it) this can only happen for states of zero energy which are necessarily the ground states of the system. This means that there may be a mismatch between the number of bosonic and fermionic ground states of a system. It is in studying such ground states that the Witten index really finds it teeth and we’ll revisit this in Section 3.4.2. More sophisticated examples can be found in the lectures on Supersymmetric Quantum Mechanics.

We now know that supersymmetry requires an equal number of bosonic and fermionic states. The next step is to understand exactly what kind of fermion is paired with what kind of boson.

2.3.1 Representations of the Poincaré Group

To set the scene, let’s first recall how we construct the irreducible representations of the Poincaré group. In fact, let’s start even more simply: how do we construct irreducible representations of the rotation group?

We work with the algebra so(3) = su(2) rather than the group. This is, of course, defined by the familiar commutation relations [J_i, J_j] = i ε_{ijk} J_k

To construct representations, the first thing we do is look to the Casimirs. These are operators that commute with all generators of the group. For su(2), there is just a single Casimir, C = Σ_{i=1}^3 J_i^2

Irreducible representations are labelled by their eigenvalue of the Casimir. For su(2), the eigenvalue of J^2 is j(j + 1) with the spin j taking values in j = 0, 1/2, 1, .... Each representation has dimension 2j + 1, with the states within a multiplet identified by their eigenvalue under, say, J_3 whose eigenvalue lies in |j_3| ≤ j. The result is the familiar one from quantum mechanics: states are labelled by |j, j_3⟩.

Now let’s turn to the Poincaré group. The irreducible representations are what we call “particles”. Again, they are characterised by the Casimirs. I won’t tell you how to construct Casimirs, but will instead just present you the result: the Poincaré group has two Casimirs, given by C_1 = P_μ P^μ and C_2 = W_μ W^μ

Here W_μ = (1/2) ε_{μνρσ} P^ν M^{ρσ} is the Pauli-Lubanski vector. It can be thought of as a relativistic version of angular momentum.

Representations of the Poincaré group are then labelled by the eigenvalues of C_1 and C_2. The first of these is simply the mass m of a particle: C_1 = m^2. What happens next is a little different depending on whether the particles are massive or massless.

• Massive Particles: In this case, we can always boost to the rest frame of the particle so that P_μ = (m, 0, 0, 0). In this frame, the Pauli-Lubanski vector is W_0 = 0 and W_i = −m J_i, with J_i the generators of rotations. This means that C_2 = −m^2 J^2 and so is specified by the eigenvalue of J^2. We find the familiar fact that massive particles are characterised by their mass m and spin j.

• Massless Particles: Now C_1 = m^2 = 0. There are some subtleties that we sweep under the rug here, but it turns out that the most interesting representations also have C_2 = W^2 = 0, so both Casimirs vanish. To characterise the representation, we choose a frame such that, say, P_μ = (E, 0, 0, E). There, we have W_μ = λ P_μ, so the constant of proportionality between W and P is determined by the eigenvalue of the U(1) rotation in the (x_1, x_2)-plane. The eigenvalue of this rotation is the helicity, h = 0, ±1/2, ±1, .... We learn that massless particles are characterised by (obviously) m = 0 and their helicity h.

Although the results are different for m = 0 and m ≠ 0, the strategy is the same. In each case, we boost to a preferred frame of the particle which is then characterised by how it transforms under the surviving symmetry group. This surviving symmetry — SU(2) for a massive particle, U(1) for a massless one — is called the little group.

There is a slight twist to the story when it comes to realising these representations on the Hilbert space of single particle states. For massive particles, the states take the form |p_μ; j, j_3⟩  (2.29)

where the momentum is restricted to obey p_μ p^μ = m^2 while the azimuthal angular momentum takes values in j_3 ≤ |j|. This fills out the 2j + 1 dimensional set of spin states. However, for massless particles, there is just a single state |p_μ; h⟩. This is because the helicity describes the representation of the Abelian group U(1) generated by M_{12} rather than the non-Abelian group SU(2) and irreducible representations of Abelian groups are one-dimensional.

The problem is that we know that massless particles also have internal degrees of freedom. For example, the photon necessarily has two polarisation states. Clearly we’re missing something. What we’re missing is the additional requirement that the The spectrum of states is invariant under CPT. For massive particles, this doesn’t buy us anything new: the set of states (2.29) is already invariant under CPT. However, for massless particles CPT flips h → −h and tells us that massless states must come in pairs |p_µ ;h⟩ and |p_µ ,−h⟩. This is the origin of the two polarisation states of the photon or graviton, or the two helicities of a massless Weyl spinor. Note that a massless scalar has helicity h = 0 and so is CPT self-conjugate. This means that there’s no requirement from CPT to add an additional degree of freedom in this case.

2.3.2 Massless Representations We now turn to the representations of the N = 1 supersymmetry algebra. The simple observation (2.28) tells us that we should expect representations to contain particles of different spin and this will turn out to be true. Once again we need to treat massless and massive particles separately.

The supersymmetry algebra also has two Casimirs. The first is familiar: C₁ = P_µ P^µ The fact that this is a Casimir tells us that all particles in a supersymmetric multiplet must have the same mass, C₁ = m².

In contrast, the other Casimir of the Poincaré group, W_µ W^µ, is not a Casimir of the supersymmetry algebra. This is because [W_µ ,Q_α ] ≠ 0 which, in turn, can be traced to the commutation relation [M_{µν} ,Q_α ] ≠ 0. But it was W_µ W^µ that told us that representations of the Poincaré group are characterised by the spin of a particle. The fact that W_µ W^µ is no longer a Casimir means that representations of the supersymmetry algebra can contain particles of different spin.

It is possible to construct a new Casimir. First define Y_µ = W_µ − Q_α \bar{σ}_{α\dot{β}µ} \bar{Q}^{\dot{β}} Then the second Casimir of the supersymmetry algebra turns out to be \tilde{C}_2 = (Y_µ P_ν − Y_ν P_µ )(Y^µ P^ν − Y^ν P^µ )

However, in what follows we won’t need this result. Instead we will build up a representation of the supersymmetry algebra more directly. Our strategy is to start from a particle (i.e. a representation of the Poincaré group) and then act on it with successive supersymmetry generators until we build up a representation of the full algebra.

It turns out that things are slightly simpler for massless representations. Consider a state |p_µ ,h⟩ of a massless particle of helicity h. We can again boost to a frame in which p_µ = (E,0,0,E). Restricted to act on such states, the supersymmetry algebra becomes {Q_α ,\bar{Q}_{\dot{α}}} = 2σ^µ_{α\dot{α}} P_µ = 2E(1+σ₃) = 4E \begin{pmatrix}1&0\\0&0\end{pmatrix}_{α\dot{α}} From the positivity condition (2.27), we see that Q_2 and \bar{Q}_{\dot{2}} necessarily annihilate this state, ⟨p_µ ,h|{Q_2 ,\bar{Q}_{\dot{2}}}|p_µ ,h⟩ = 0 ⇒ Q_2 |p_µ ,h⟩ = \bar{Q}_{\dot{2}} |p_µ ,h⟩ = 0 To build a representation of the full supersymmetry algebra, we only need consider the action of Q_1 and \bar{Q}_{\dot{1}}. But these act just like fermionic creation and annihilation operators. Specifically, if we rescale the operators to become a = \frac{Q_1}{\sqrt{4E}} \text{ and } a^† = \frac{\bar{Q}_{\dot{1}}}{\sqrt{4E}} ⇒ \{a,a^†\} = 1 \text{ and } \{a,a\} = \{a^†,a^†\} = 0 The representations of this algebra are straightforward: they consist of two states |0⟩ and |1⟩ such that a|0⟩ = 0 and |1⟩ = a^†|0⟩. This ensures that a^†|1⟩ = 0. For us, this means that we can start by taking a state which, by assumption, is annihilated by a, a|p_µ ,h⟩ = 0 The full supersymmetry multiplet then consists of |p_µ ,h⟩ and a^†|p_µ ,h⟩. The question is: what is the helicity of this second state? This follows from the commutation relation (2.22)

[M_{µν},Q_α ] = (σ_{µν})_{α}^{ β} Q_β \text{ and } [M_{µν},\bar{Q}_{\dot{α}}] = (\bar{σ}_{µν})^{\dot{α}}_{ \dot{β}} \bar{Q}^{\dot{β}} (2.30)

Restricting to rotations in the (x1,x2) plane, which is what we mean by helicity, we have [M_{12},Q_1] = \frac{1}{2} Q_1 \text{ and } [M_{12},Q_2] = -\frac{1}{2} Q_2 [M_{12},\bar{Q}_{\dot{1}}] = \frac{1}{2} \bar{Q}_{\dot{1}} \text{ and } [M_{12},\bar{Q}_{\dot{2}}] = -\frac{1}{2} \bar{Q}_{\dot{2}} The first equation tells us that Q_1 raises the helicity by 1/2. This suggests that the adjoint \bar{Q}_{\dot{1}} lowers the helicity by 1/2. To see that this is the case, we need to remember that, after lowering an index, Q^1 = -\bar{Q}_{\dot{2}} so we have [M_{12},\bar{Q}_{\dot{1}}] = -\frac{1}{2} \bar{Q}_{\dot{1}} So \bar{Q}_{\dot{1}} does indeed lower the helicity by 1/2 as anticipated. We learn that the massless representations of the supersymmetry algebra consist of just two states: |p_µ ,h⟩ \text{ and } |p_µ ,h-\frac{1}{2}⟩ = \frac{1}{\sqrt{4E}} Q_1 |p_µ ,h⟩ As we saw above, for massless states we must also add their CPT conjugates. The different representations of the supersymmetry algebra then arise by picking different starting helicities h. There are three representations that are most important: • If we start with h = 1 then we have \begin{tabular}{c|ccc} h & -1 & 0 & +1 \\ \hline multiplicity & 1 & 2 & 1 \\ \end{tabular} This is the matter content that we get from quantising a single Weyl spinor together with a complex scalar. This is known as a chiral multiplet. The chiral multiplets should be thought of as matter particles. We will devote Section 3 to studying field theories associated to chiral multiplets. Here we make a quick comment. The fact that any other internal symmetry generator must commute with Q means that the fermion and scalar in a given chiral multiplet must experience the same force. In particular, if one is charged under a gauge group then so is the other. We’ll see this explicitly when we construct supersymmetry gauge theories in Section 4.

• If we start with h = 1 then we have h/2  -1  -1  +1  +1  2  2 multiplicity 1 1 1 1 This is the matter content of a photon together with a single Weyl spinor. It is known as the gauge multiplet or vector multiplet.

We will devote Section 4 to the study of vector multiplets. There we will see that we can construct supersymmetric versions of Yang-Mills theory with gauge group G by taking dimG vector multiplets. As usual, the h = 1 gauge bosons transform in the adjoint of the gauge group. But now, so too, must its fermionic supersymmetric partner. In this context, the fermion is called a gaugino.

• If we start with h = 2 then we have h/2  -2  -3  +3  +2  2  2 multiplicity 1 1 1 1 This is the matter content of a graviton together with a helicity 3/2 spinor, sometimes known as a Rarita-Schwinger field or, in this context, the gravitino. They combine to form the supergravity multiplet.

If we keep going, we get massless fields with helicity h > 2. But there are strong restrictions that prohibit the existence of interacting theories with massless fields of such high helicity. (This statement is true in Minkowski spacetimes; there are remarkable "higher spin" theories that include an infinite tower of massless states in de Sitter or anti de Sitter spacetimes.) We also skipped the h = 3/2 multiplet for similar reasons; it turns out that the existence of a massless helicity 3/2 particle implies the existence of a local supersymmetry which, in turn, requires that the theory is coupled to gravity.

2.3.3 Massive Representations We next turn to massive representations of the supersymmetry algebra. In the rest frame of a particle we have pμ = (m,0,0,0). Acting on such states, the supersymmetry algebra becomes {Qα, Q̄α̇} = 2σμαα̇ Pμ = 2mσ0αα̇ = 2m ( 1 0; 0 1 )αα̇  (2.31)

This time, after rescaling, both Q1 and Q2 act as fermionic creation/annihilation operators aα = Qα/√(2m) and a†α̇ = Q̄α̇/√(2m) ⇒ {aα, a†α̇} = δαα̇ with {aα, aβ} = {a†α̇, a†β̇} = 0. We start with a state |Ω⟩ = |pμ; j, j3⟩ that we assume to be annihilated by aα|Ω⟩ = 0. Then the full supermultiplet consists of four states |Ω⟩ a†α̇|Ω⟩ and a†β̇|Ω⟩ a†α̇ a†β̇|Ω⟩

Again, the question is: what is the spin of these other states. We could use the commutation relations (2.30) to understand how the new states transform under the SU(2) little group but it’s a little fiddly while the end result is intuitive and straightforward. The initial state |Ω⟩ has spin j. The states a†α̇|Ω⟩ then sit in the tensor product of representations j ⊗ 1/2 = (j + 1/2) ⊕ (j − 1/2). The final state can be written as a†α̇ a†β̇|Ω⟩ = 1/2 εα̇β̇ a†α̇ a†β̇|Ω⟩, where the εα̇β̇ now contracts the creation operators to be a spin singlet. This means that the state a†α̇ a†β̇|Ω⟩ once again has spin j.

The upshot is that a massive supermultiplet contains two particles of spin j, a particle of spin j − 1/2 and a particle of spin j + 1/2. Note that the degeneracy of the two particles of spin j is precisely equal to the degeneracies of the other two particles: 2×(2j +1) = 2 (j + 1/2 +1) + 2 (j − 1/2 +1)

This is simply that statement that we saw previously: a supermultiplet must have an equal number of bosonic and fermionic degrees of freedom.

There are just two massive supermultiplets that will be of interest

• If we start with j = 0, we have j 0 1/2 multiplicity 2 1 This is the matter content of a massive complex scalar with a single massive Weyl fermion. We recognise it as the same matter content as the chiral multiplet that we met previously, now of course with all particles having a mass.

• If we start with j = 1, we have j 0 1/2 1/2 1 multiplicity 1 2 1 In other words, we have a massive spin 1 particle, two massive Weyl fermions, and a massive spin 0 particle. This is now more states than we found in the massless gauge multiplet. In fact, this collection of states is equivalent to a massless gauge multiplet and a massless chiral multiplet. But that makes sense. In quantum field theory, a massless gauge boson can become massive only through the Higgs mechanism, in which the gauge boson “eats” a scalar. The supersymmetric extension of this is that a massless vector multiplet “eats” a chiral multiplet to become the massive vector multiplet described above.

There’s one further subtlety that is worth flagging up. This is how parity acts on the two scalars in the massive chiral multiplet. It turns out that one of them is a scalar and the other a pseudoscalar. Here, the meaning of a “pseudoscalar” is that it picks up a minus sign under parity. This statement follows, like everything else in this section, from the supersymmetry algebra. We denote the parity operator as P to distinguish it from the momentum operator Pμ. By definition, we must have P ˆ PμP ˆ−1 = (P0,−Pi)

Meanwhile, parity also exchanges left-handed and right-handed spinors. This means that p Parity must exchange some combination of Q and Q̄. One can check that the supersymmetry algebra remains unchanged if we take P̂ Q_α P̂⁻¹ = (σ0)_αα̇ Q̄^α̇ and P̂ Q̄^α̇ P̂⁻¹ = -(σ0)^α̇α Q_α. (More generally one can include a complex phase in these relations but it will not affect our discussion here.)

Now our two scalar states in the massive chiral multiplet are |Ω⟩ and |Ω′⟩ = a₁†a₂†|Ω⟩ ∼ Q̄₁ Q̄₂ |Ω⟩. They obey Q_α|Ω⟩ = Q̄^α̇|Ω′⟩ = 0. Since parity exchanges Q_α and Q̄^α̇, it must also exchange |Ω⟩ and |Ω′⟩. This means that the parity eigenstates are P̂ (|Ω⟩±|Ω′⟩) = ±(|Ω⟩±|Ω′⟩) and we have one scalar (with the + sign) and one pseudoscalar (with the - sign) as advertised.

## 2.4 Extended Supersymmetry

It is possible for theories to exhibit more than one supersymmetry. This means that there is a collection of N supercharges Q^I_α and Q̄^{Iα̇}, I = 1,...,N. Each of these supercharges retains the same commutation relations with the generators of the Poincaré group, [M^{µν}, Q^I_α] = (σ^{µν})_α^β Q^I_β and [P^µ, Q^I_α] = 0, and the key part of the supersymmetry algebra holds for each generator separately {Q^I_α, Q̄^{Jα̇}} = 2σ^µ_{αα̇} P_µ δ^{IJ}.

However, there are two novelties. The first is that the anti-commutator of the supercharges with themselves can be more interesting {Q^I_α, Q^J_β} = ε_{αβ} Z^{IJ} and {Q̄^{Iα̇}, Q̄^{Jβ̇}} = ε^{α̇β̇} (Z†)_{IJ} (2.32). Here Z^{IJ} = -Z^{JI} is a central charge, meaning that it commutes with all other elements of the algebra. The exact nature of these central charges depends on the precise theory that we consider, but they must be constructed from other conserved quantities that are at hand. We’ll see the role that these central charges play shortly.

The second novelty is the R-symmetry group. Recall that for N = 1 we had a U(1) symmetry (2.24) that rotates the phase of the supercharge. For N > 1, the R-symmetry rotates the supercharges among themselves. For reasons that will become clear shortly, our primary interest will be in N = 2 and N = 4 supersymmetry. Here the R-symmetries are: • N = 2: The R-symmetry group is U(2) ≅ U(1)_R × SU(2)_R.

• N = 4: A priori, the R-symmetry group is U(4). However, it turns out that only SU(4) is realised on fields. This is equivalent to SU(4) = Spin(6). (This is sometimes written, a little inaccurately, as SO(6) but the supercharges transform in the spinor representation of Spin(6) which is not a representation of SO(6) = Spin(6)/Z₂.)

Theories with extended supersymmetry are a subset of those theories with N = 1 supersymmetry. This means that the representations of theories with N > 1 must be constructed by joining together the N = 1 supermultiplets that we described above. In the rest of this section, we explain how this works.

2.4.1 Massless Representations For representations on states |p^µ, h⟩ of massless particles, we proceed as before. We boost to a frame with p^µ = (E,0,0,E) and restrict attention to the algebra on such states. We then have {Q^I_α, Q̄^{Jα̇}} = 4E \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} δ^{IJ}.

As previously, we have Q^I_α|p^µ, h⟩ = Q̄^{Iα̇}|p^µ, h⟩ = 0. From (2.32), we then have Z^{IJ}|p^µ, h⟩ = 0 which tells us that the central charges play no role for the massless states. We’re left, as before, just with the Q^I_α and Q̄^{Iα̇} operators to deal with. These now form a collection of N fermionic creation and annihilation operators a^I = (1/√(4E)) Q^I_1 and a^I† = (1/√(4E)) Q̄^{I1̇} ⇒ {a^I, a^{J†}} = δ^{IJ} and {a^I, a^J} = {a^{I†}, a^{J†}} = 0.

We now start with some fiducial state |Ω⟩ = |p^µ, h⟩ satisfying a^I|Ω⟩ = 0 and build up the full representation by acting with successive creation operators. The end result is a collection of states |Ω⟩, a^{I†}|Ω⟩, a^{I†}a^{J†}|Ω⟩, ..., a^{1†}...a^{N†}|Ω⟩.

Our initial state |Ω⟩ has helicity h. If we act with p of the a^† excitation operators then there are \binom{N}{p} different states, each of which has helicity h − p/2. The full multiplet consists of 2^N different states. If we add the CPT conjugate states then we have 2^{N+1} states overall. Let’s now look at some specific examples.

N = 2 Supersymmetry Again, the different multiplets arise by considering initial states |Ω⟩ with different helicities. We’ll deal with each in turn.

• If we start with h = 1 then there are two states in the first level, a^{I†}|Ω⟩, each with h = 1/2, and a single state in the final level, a^{1†}a^{2†}|Ω⟩, with h = 0. After adding the CPT conjugate we end up with helicity multiplets: h: -1, 0, +1 multiplicity: 2, 4, 2 This is called a hypermultiplet. It consists of two chiral multiplets or, equivalently, two complex scalars and a Dirac fermion (i.e. two Weyl fermions). You might wonder why we needed to add the CPT conjugate in this case. After all, starting with h = +1 gave a single chiral multiplet which is already CPT self-conjugate. The answer to this is buried in the details of the SU(2) symmetry which acts on the scalars a^{I†}|Ω⟩ as a doublet. But this means that each of these scalars must be complex and that, in turn, requires that we add the CPT conjugate.

• If we start with h = 1/2 then we get two additional states with h = 0 and one with h = −1. Adding the CPT conjugate gives...

njugate gives h −1 −1 0 +1 +1 2 2 multiplicity 1 2 2 2 1 This is the N = 2 vector multiplet, comprising of an N = 1 vector multiplet and N = 1 chiral multiplet.

• If we start with h = 2 then, after adding the CPT conjugate, we end up with h −2 −3 −1 +1 +3 +2 2 2 multiplicity 1 2 1 1 2 1 This is the N = 2 supergravity multiplet. It comprises of an N = 1 supergravity multiplet together with an N = 1 vector multiplet.

There’s one important feature of the spectrum above that is worth highlighting. The fermions now come in pairs, meaning that they can be viewed as Dirac fermions rather than Weyl fermions. This puts restrictions on the kind of supersymmetric theories that we can build. In particular, it’s not possible to construct a chiral gauge theory with N > 1 supersymmetry. Here a chiral theory is one in which left- and right-handed fermions experience different forces, like in the Standard Model. Such theories are possible with N = 1 supersymmetry (or, indeed, N = 0 supersymmetry as in our world!). But any extended supersymmetry forces the theories to be vector-like.

N = 4 Supersymmetry We can play the same game with N = 4 supersymmetry.

• If we start with h = 1 then we get the following multiplet h −1 −1 0 +1 +1 2 2 multiplicity 1 4 6 4 1 This consists of an N = 2 vector multiplet with an N = 2 hypermultiplet and is the unique N = 4 multiplet that does not include gravity. Note that there is now no longer a distinction between forces and matter: once you specify the gauge group, all matter content is also fixed. Furthermore, all matter fields necessarily transform in the adjoint representation of the gauge group.

For once, we did not need to add the CPT conjugate to the above multiplet: it’s already CPT self- conjugate. As we saw above, it was almost possible to achieve this for the N = 2 matter representation but we fell at the last hurdle when we considered how the SU(2) symmetry acts on the scalars. But now we have no such concern. The scalars are the set of 6 states aI†aJ†|Ω⟩ and transform in the 6 of the SU(4) R-symmetry. But this is a real representation and there is no need to add the CPT conjugate.

• If we start with h = 2 then, after adding the CPT conjugate multiplet, we have h −2 −3 −1 −1 0 +1 +1 +3 +2 2 2 2 2 multiplicity 1 2 2 2 2 2 2 2 1 This is the N = 4 supergravity multiplet, comprising of an N = 2 supergravity multiplet and N = 2 vector multiplet.

You may have noticed that we jumped straight from N = 2 to N = 4, missing out N = 3 in the middle. If you try to build a multiplet of single particle states with N = 3 supersymmetry starting from, say, h = 1 or h = 1 then you’ll find that you’re obliged to add the CPT conjugate representation and you just end up with N = 4 supersymmetry after all. This observation is the key element of a proof that says any perturbative theory with N = 3 global supersymmetry necessarily has N = 4 supersymmetry.

The word “perturbative” is important in the above statement. This means that the theory is weakly coupled and the single particle states that we’re considering here are a good approximation to the spectrum of the theory. It turns out N = 3 supersymmetry can be realised in strongly coupled, interacting quantum field theories, with no perturbative regime.

N = 8 Supersymmetry If we go beyond N = 4 supersymmetry then we no longer have multiplets with helicities h ≤ 1. This means that we are now necessarily in the realm of local supersymmetry and supergravity. Furthermore, by the time we get beyond N = 8 supersymmetry the multiplets have particles with helicity h > 2. As we mentioned before, such theories are always free in Minkowski space and therefore of limited interest. In this sense, N = 8 is the maximum number of supersymmetries possible. The theory has a unique supergravity multiplet with the following degeneracies h −2 −3 −1 −1 0 +1 +1 +3 +2 2 2 2 2 multiplicity 1 8 28 56 70 56 28 8 1 N = 8 supergravity has some interesting properties and plays a role in string theory. However, we won’t discuss it further in this course.

2.4.2 Massive Representations and BPS Bounds Rather than repeating the whole story for massive representations, we will instead just focus on the novelty. This arises from the central charges ZIJ that appear in the supersymmetry algebra {QI,QJ} = ϵ ZIJ α β αβ For reasons that we now explain, this is where much of the power of extended supersymmetry comes from.

Our goal is to understand representations of this algebra, in conjunction with the original supersymmetry algebra which, in the rest frame of the particle, reads (2.31)

(cid:32) (cid:33)

1 0 {QI,Q ¯J} = 2m δIJ α α˙ 0 1 We’ll illustrate the story with N = 2 supersymmetry, although the general idea holds for any theory with extended supersymmetry. With N = 2, the anti-symmetric central charge is necessarily just a complex number Z ZIJ = 2ϵIJZ For simplicity, we take Z to be real. (Typically it’s not but we’ll dodge this issue for now and state the full result below.)

We then define the following combination of creation and annihilation operators a = 1 √ Q1 + Q ¯2 and b = 1 √ Q1 − Q ¯2 α √2 Q1 − Q ¯2 α √2 Q1 + Q ¯2 1 1 Note that we’ve mixed up α and α˙ indices. This is acceptable because we’re working in the rest frame of the particle and so have already broken Lorentz invariance. The choice of a and b operators is designed to disentangle the mass and central charge Z, so their commutation relations read {a ,a†} = 2(m+Z)δ and {b ,b†} = 2(m−Z)δ α β αβ α β αβ with all other anti-commutators vanishing. The {a ,a†} and {b ,b†} are both positive α β α β definite, so the corresponding right-hand sides must be too. But this is only true if the masses are bounded by the central charges, m ≥ |Z| This formula also holds if Z is complex; we just need to redefine the operators a and b using a phase to derive the same result. This formula is interesting. Although we haven’t seen yet any specific examples, recall that the central charge Z is some combination of conserved charges in the quantum field theory. We learn that the masses of particles is bounded by the charges. This is known as the BPS bound although in the present context the name Witten-Olive bound would be more appropriate.

What about the representation theory of the algebra? Crucially, this depends on whether m > |Z| or m = |Z|.

If m > |Z|, then we are in a situation very similar to the massive representation theory that we saw before. Both a† and b† act as creation operators and the result is α α that we have a multiplet comprising of 16 states. This is known as a long multiplet. We can also repeat this story with N supersymmetries to find that long multiplets have 22N states.

More interesting is what happens when m = |Z|. In this case, half of the creation operators do nothing. For example, when m = Z, the b operators must just vanish on all states in the multiplet. Now we’re back to the situation we met when discussing massless representations, with only a† acting as creation operators. The result is the hypermultiplet or vector multiplet that we saw above, each with 8 states, but now with a mass m = Z. This is known as a short multiplet.

The existence of short multiplets, whose mass is fixed to be m = |Z|, turns out to be a wonderfully powerful tool in the study of quantum field theories with extended supersymmetry. The basic idea is that one can usually solve quantum field theories at weak coupling. There we can identify the various states and understand the spectrum of long and short multiplets. As one moves into the strong coupling realm, we typically lose control over the dynamics. However, the short multiplets are special because their mass is pinned to be m = |Z|. The mass can’t deviate from |Z| because this would need there to be extra states in the Hilbert space and these can’t magically appear from nowhere as some parameter, like a coupling constant, is varied. The only way that the short multiplets can free themselves from this constraint is if two or more short multiplets become degenerate and then combine to become a long multiplet whose mass is no longer protected. By understanding when this can (or, better yet, can’t) happen we get a precious handle on the strong coupling dynamics of certain quantum field theories.

In this way, the study of short BPS multiplets shines a rare light into what happens at strong coupling. It allows us to effectively solve the dynamics of N = 2 and N = 4 gauge theories. It also allows us to understand the strong coupling limits of string theory, including the existence of M-theory, and to compute the microscopic entropy of certain BPS black hole solutions. It is, in short, a very useful tool.

The BPS trick is not available for N = 1 theories and so we won’t be wielding it for much of these lectures. (Actually, it can be used to compute the tension of domain walls and vortex strings in certain N = 1 theories, but not the masses of particle states.)

2.4.3 Supersymmetry in Other Dimensions Throughout these lectures, we will restrict ourselves to supersymmetric theories in d = 3 + 1 spacetime dimensions. There are, however, many interesting things to say about supersymmetric theories in other dimensions. Here we merely make a few very simple comments.

Supersymmetric Gauge Theories in Different Dimensions We’ve seen that the vector multiplet of N = 1 supersymmetry has a photon paired with a single massless Weyl spinor. This works because both have two internal degrees of freedom in d = 3+1 dimensions. We can ask: in what other spacetime dimensions might we be able to pair a photon with a fermion?

The number of polarisation states of a photon is d − 2. So the question really is: in what dimensions does a spinor have d−2 degrees of freedom? We will see that we can have a supersymmetric theory in which a photon pairs with a single fermion in d = 3,4,6 and 10 Lorentzian spacetime dimensions.

The story is simplest in d = 3+1 and d = 5+1. In even spacetime dimension Dirac spinor has 2^(d/2) complex components. But the irreducible representations of the Lorentz group are Weyl spinors with 2^((d-2)/2) complex components. While a complex scalar has two degrees of freedom, a complex spinor has the same number of degrees of freedom as the number of components. This is because the Dirac equation (or Weyl equation) is first order so these components include both "position" and "momentum". This means that if we want the number of degrees of freedom of a Weyl spinor to match those of a photon then we need to solve the equation 2^((d-2)/2) = d-2 The solutions are d = 4 and d = 6 as advertised.

In d = 3+1 dimensions we can choose to impose either a Majorana condition or a chiral projection to a Weyl fermion. However in d = 2 mod 8 spacetime dimensions, it is possible to impose both a Majorana and Weyl condition. This halves the number of degrees of freedom of a Weyl fermion. Attempting to match the degrees of freedom of a Majorana-Weyl fermion to a photon we have 2^((d-4)/2) = d-2 with d = 2 mod 8 The unique solution is d = 10.

Finally we’re left searching solutions in odd spacetime dimensions. It is not hard to see that there is just one possibility. In d = 2 + 1 dimensions, a photon has just a single polarisation state. Meanwhile, a Dirac spinor in d = 2 + 1 has two complex components. However we can impose a Majorana condition to make the spinor real. (For example, we can take the real Clifford algebra γ0 = iσ2, γ1 = σ1 and γ2 = σ3.)

So a Majorana spinor in d = 2+1 has two real components and, correspondingly, one degree of freedom, matching that of the photon.

If we’re not in the magic spacetime dimension d = 3,4,6 or 10 then we can still have supersymmetric theories that relate a photon to a fermion. But now we need to include extra scalar degrees of freedom as well to make up the numbers.

The fact that the number of fermion degrees of freedom increases exponentially with d, while the number of bosonic degrees of freedom increases only linearly, suggests that there may be a maximum spacetime dimension in which supersymmetry is possible.

Indeed this is the case. If we don’t wish to get our hands dirty with supergravity then d = 9 + 1 dimensions is the highest we can go. If we’re happy to include gravity in the mix then there is a unique supersymmetry theory in d = 10+1 dimensions known, reasonably enough, as eleven dimensional supergravity. It is extremely interesting and describes the low-energy behaviour of M-theory.

Extended Supersymmetry and Higher Dimensions There is a close relationship between supersymmetric theories in higher dimensions and extended supersymmetry. In particular, theories with N = 2 supersymmetry naturally descend from d = 5+1 dimensions while those with N = 4 supersymmetry come from d = 9+1 dimensions. (This statement, taken at face value, is true only at the classical level. But there are also a myriad of subtle and wonderful connections at the quantum level, none of which will be touched upon in these lectures.)

To see this, we will briefly jump ahead of ourselves slightly and use the language of fields, rather than the language of single particle quantum states that we’ve invoked until now. The relationship between theories in different dimensions involves a process known as dimensional reduction. This means that we take the fields in a higher dimension and state, by fiat, that they are independent of certain spatial coordinates. For example, consider a gauge field A in, say, d = 5 + 1 dimensions. This means that M = 0,1,...,5. Upon dimensional reduction, we insist that this gauge field only depends on xµ with µ = 0,1,2,3. The gauge field itself then decomposes as A → (Aµ, ϕ4, ϕ5)

That is, we get a d = 3+1 dimensional gauge field Aµ together with two real scalars ϕ4 and ϕ5. But this is precisely the bosonic content of the N = 2 vector multiplet that we found above. A d = 5+1 Weyl fermion decomposes into two d = 3+1 Weyl fermions in a similar fashion (although you have to work a little harder playing around with the gamma matrices to see this).

Playing the same game with a d = 9+1 gauge field, we find a d = 3+1 gauge field together with 10 − 4 = 6 scalars. This is the bosonic content of the N = 4 vector multiplet that we found above. Decomposing a d = 9 + 1 Majorana-Weyl fermion completes the story, giving four d = 3+1 Weyl fermions.

Finally, if you dimensionally reduce eleven dimensional supergravity you find N = 8 supergravity in d = 3+1 dimensions.

Counting Supersymmetries The way in which we count supersymmetries in different dimensions can be rather bewildering when you first meet it. In d = 3 + 1 we count supersymmetries by the number of Weyl spinor supercharges QI with I = 1,...,N. But this is clearly specific to 4d. In other dimensions the counting depends on what kinds of minimal spinors we can construct. Moreover, if we dimensionally reduce then what is a minimal supersymmetry in a higher dimension typically becomes an extended supersymmetry in a lower dimension.

To avoid this confusion, it can be useful to count the number of components of the supercharges. We count these as N (rather than the calligraphic N.) These components are, sadly, also referred to as supercharges! Because spinors can be real in some dimensions, we count the number of real components or, equivalently, twice the number of complex components. This means that, in d = 3+1 dimensions, N = 1 supersymmetry has four supercharges, N = 2 has eight supercharges, and so on.

To orient you, here is a list of some of the most interesting classes of supersymmetric theories and how they are labelled in various dimensions. The list is by no means complete but gives some sense of the more compelling supersymmetric stories out there. The maximum number of supercharges is N = 32. These are all supergravity theories and can exist in any dimension d = 10 + 1 and below. Upon dimensional reduction, the number of minimal spinor supercharges N in various dimensions is

Dimension d 11 10 6 4 N=32 supercharges: Supersymmetry N 1 (1,1) (2,2) 8

This is not an exhaustive list: supersymmetric theories with N = 32 supercharges exist in all dimension d ≤ 11. But the dimensions listed above are, for various reasons, the most interesting and well studied.

Note the strange (n,n) notation in d = 5+1 and d = 9+1. This is because of one more subtlety of representations of the Clifford algebra. When d = 2 mod 4, the two types of Weyl spinor are not related by complex conjugation in Lorentzian signature. This means that you can have a spinor of one chirality without necessarily having the other. In contrast, when d = 0 mod 4 (including, as we saw in great detail, in d = 3+1) the complex conjugate of a left-handed spinor is a right-handed spinor, so if you have one then you always have the other. The notation (n,n) tells us how many left- and right-handed spinor supercharges we have.

There is another supergravity theory in d = 9 + 1 dimension which has also 32 supercharges but with N = (2,0) supersymmetry. This is more commonly known as Type IIB supergravity, with the N = (1,1) theory known as Type IIA. They are the low-energy descriptions of Type IIA and IIB string theories.

Theories with N = 16 supercharges can exist in dimensions d = 9 + 1 and below. Upon dimensional reduction, the associated supersymmetry is:

Dimension d 10 6 4 3 2 N=16 supercharges: Supersymmetry N (1,0) (1,1) 4 8 (8,8)

The most famous and well studied of these is the Yang-Mills theory associated to the N = 4 vector multiplet in d = 3 + 1. It has many remarkable properties, including electromagnetic duality and the fact that, at strong coupling, it is can be viewed as a theory of quantum gravity through the AdS/CFT correspondence. There are also interesting stories to tell about the quantum dynamics of the theories in d = 2+1 and d = 1+1 dimensions.

There is one further interesting theory with 16 supercharges. This is a strongly interacting superconformal quantum field theory in d = 5 + 1 dimensions with N = (2,0) supersymmetry. In some ways, it can be viewed as the grandfather of all quantum field theories. Given its importance, it has a remarkably rubbish name: it is simply called the (2,0) theory.

Theories with N = 8 supercharges exist in d = 5+1 dimensions and below. Upon dimensional reduction, the names of the supersymmetries that one finds are

Dimension d 6 4 3 2 N=8 supercharges: Supersymmetry N (1,0) 2 4 (4,4)

Again, the theories with N = 2 supersymmetry in d = 3+1 dimensions are the best studied and were first solved by Seiberg and Witten.

Theories with N = 4 supercharges exist in d = 3+1 dimensions and below. Upon dimensional reduction, this becomes

Dimension d 4 3 2 N=4 supercharges: Supersymmetry N 1 2 (2,2)

Much of the focus of these lectures notes will be on understanding the dynamics of N = 1 theories in d = 3+1 dimensions. But there are many beautiful stories in lower dimensions as well. In particular, the study of superconformal N = (2,2) theories in d = 1 + 1 dimensions is where one can first find the mathematical study of mirror symmetry. There are also interesting 2d theories with N = (0,4) supersymmetry.

Finally, theories with N = 2 supercharges exist in d = 2+1 dimensions and below. The dimensional reduction to d = 1+1 gives

Dimension d 3 2 N=2 supercharges: Supersymmetry N 1 (1,1)

There are also N = (0,2) theories that do not descend from d = 2 + 1 dimensions. Note that these are usually written as (0,2) rather than (2,0) to give an extra hint that we’re talking about 2d theories rather than the 6d theory mentioned above.

I’ve not included d = 0 + 1 theories in the above list, also known as quantum mechanics, but it’s not for want of things to say. You can read about supersymmetric quantum mechanics in the companion lecture notes.

3 Chiral Superfields

In the previous section we’ve understood how supersymmetry acts on single particles states in the Hilbert space. But, ultimately, we want to write down field theories that are invariant under supersymmetry. Part of this requires understanding how supersymmetry acts on fields. We've already seen a taster of this in the introduction. The action (1.1) was given by S = ∫ d⁴x [ ∂ₘϕ†∂ₘϕ − iψ̄ σ̄ᵐ∂ₘψ − |∂W/∂ϕ|² − (1/2)(∂²W/∂ϕ²)ψψ − (1/2)(∂²W†/∂ϕ†²)ψ̄ψ̄ ] (3.1)

This involves a complex scalar ϕ and a single Weyl fermion ψ. After our discussion in the last section, we now recognise this as the fields corresponding to a chiral multiplet. We claimed in the introduction that this action is invariant under the transformation δϕ = √2 εψ, δψα = √2 iσᵐαα̇ ε̄α̇ ∂ₘϕ − √2 (∂W†/∂ϕ†) εα (3.2)

There are a few questions that we'd like to ask. First: how can we construct actions like (3.1)? After all, it's not like we can just stare at the action and see that it's invariant under the transformations (3.2). It takes a bit of work to show this. Secondly, how are the transformations (3.2) related to the supercharges and supersymmetry algebra that we met in the previous section. The purpose of this section is to answer these questions. In particular, we'll see how we can rewrite the action (3.1) in a way that the supersymmetry is manifest. The trick to doing this is to combine the bosonic field ϕ and the fermionic field ψ into a single object known as a superfield.

## 3.1 Superspace

Usually, fields are functions of xᵐ, the coordinates of Minkowski space. But, as we've seen, supersymmetry is an extension of the Poincaré group. Correspondingly, superfields live not on Minkowski space, but on an extension of Minkowski space known as superspace. The coordinates of superspace are xᵐ, θα, θ̄α̇.

Here xᵐ, with m = 0,1,2,3 are the coordinates of Minkowski space. In superspace these are augmented with Grassmann-valued spinors θα and θ̄α̇. In other words, superspace is not a regular manifold of the kind that we know and love from courses on differential geometry. Instead it is an example of a supermanifold, with both commuting and anti-commuting dimensions.

3.1.1 The Geometry of Superspace In what follows, we'll explore the idea of fields on superspace and see how they encapsulate a collection of fields that transform into each other under supersymmetry. However, we could reasonably ask: how did we come up with the idea of superspace in the first place? There is, it turns out, a group theoretic answer to this. In general, if we're given a Lie group G, we might want to know what manifolds M accommodate a natural action of G. One obvious choice is to take the manifold to be the group itself: M = G. In this case, each element g ∈ G gives us a natural map M → M given by g′ ∈ M ↦ g·g′. A slightly less obvious choice is to take a coset space. This is the manifold M = G/H where H ⊂ G is a subgroup of G. A point {g} in the coset G/H is defined by the equivalence relation among elements of G g ≡ g·h for all h ∈ H. Again, any element g ∈ G gives us a natural map M = G/H → G/H defined by {g′} ∈ M ↦ {g·g′}. For example, the group G = SU(2) is, as a manifold, G = S³. We can consider the subgroup H = U(1) ⊂ SU(2) to get the coset SU(2)/U(1) ≅ S². (Mathematically, this is known as the Hopf fibration.) Obviously there is a natural action of SO(3) = SU(2)/Z₂ on S². This, somewhat abstract, way of thinking gives us a new perspective on Minkowski space itself. It can be viewed as the coset R¹·³ = G/H = Poincaré Group / Lorentz Group. Here a general element of the Poincaré group G is comprised of Lorentz boosts, generated by Mᵐᵛ, and translations generated by Pᵐ. We write this as g(ω,a) = exp[ − (1/2) ωᵐᵛ Mᵐᵛ + i aᵐ Pᵐ ].

Meanwhile, the Lorentz group H consists only of Lorentz boosts. This means that coset space can be parameterised just by aᵐ which we can equivalently think of as coordinates xᵐ = aᵐ on Minkowski space. The fact that Minkowski space can be viewed as a coset merely confirms something that we knew already: there is an action of the Poincaré group on Minkowski space. Now, however, we would like to construct a space on which the group of supersymmetry transformations naturally acts. These are given by g(ω,a,θ,θ̄) = exp[ − (1/2) ωᵐᵛ Mᵐᵛ + i aᵐ Pᵐ + i θα Qα + i θ̄α̇ Q̄α̇ ] (3.3)

with Qα and Q̄α̇ the supersymmetry generators that we met in the previous section. The spinors θα and θ̄α̇ should be viewed as parameterising the "amount" of supersymmetry transformation that we're doing, albeit with the "amount" now somewhat harder to quantify as it's a Grassmann valued object. With Grassmann elements of this kind, g is an element of a super Lie group which, in this case, is known as the super-Poincaré group. The coset construction continues to work in the same way and we define superspace to be Superspace = G/H = Super-Poincaré Group / Lorentz Group.

A point in superspace is now parameterised by xᵐ = aᵐ and the Grassmann-valued spinors θα and θ̄α̇ as advertised above.

Before we go on, a quick comment on nomenclature. The Lorentz group is, of course, SO(1,3). (Actually, strictly speaking if we want to include spinor representations it is SL(2,C) = Spin(1,3) but we'll ignore this double cover subtlety.) The Poincaré group is the semi-direct product ISO(1,3) = SO(1,3) ⋉ R⁴ and Minkowski space is R¹,³ = ISO(1,3)/SO(1,3). Meanwhile, the super-Poincaré group is usually written as ISO(1,3|1) with the additional "bar 1" or "slash 1" telling us that we have N = 1 supersymmetry. Superspace is then the "4+4" dimensional supermanifold R¹,³|⁴ = ISO(1,3|1)/SO(1,3). We'll have no need for any of this notation in these lectures.

The Action on Superspace The whole point of the coset construction of superspace is that it tells us how the supergroup acts. This will be important in what follows so let's flesh it out a little. First, we write the general element of the supergroup (3.3) as g(ω,x,θ,θ̄) = g̃(x,θ,θ̄)h(ω)

where h(ω) is a Lorentz transformation and g̃(x,θ,θ̄) is the representative of the coset g̃(x,θ,θ̄) = exp(ixPμ + iθαQα + iθ̄Q̄α̇)

This specifies a point (x,θ,θ̄) in superspace.

We now want to see how the momentum operator P and supercharges Q and Q̄ shift the point (x,θ,θ̄) in superspace. Let's start with the momentum operator. We introduce the supergroup element U(a) = exp(iaPμ)

Then we have U(a)g̃(x,θ,θ̄) = eiaPeixP+iθQ+iθ̄Q̄ = ei(x+a)P+iθQ+iθ̄Q̄ = g̃(x+a,θ,θ̄)

This gives us a familiar result: momentum generates translations, xμ → xμ + aμ Now we do the same for the supercharges. This time we will find a small twist to the story. We introduce the supergroup element V(ϵ,ϵ̄) = exp(iϵαQα + iϵ̄Q̄α̇)

Note that ϵα and ϵ̄ are Grassmann-valued spinors. They shouldn't be confused with the anti-symmetric εαβ matrices that we met earlier. (Sorry!) Now the action on superspace is given by V(ϵ,ϵ̄)g̃(x,θ,θ̄) = eiϵQ+iϵ̄Q̄ eixP+iθQ+iθ̄Q̄ (3.4)

The small twist is that Q and Q̄ do not anti-commute with each other. In fact, now that we've multiplied the supercharges with anti-commuting spinors ϵ and θ, we can talk about commutation relations rather than anti-commutation relations. We have QαQ̄α̇ + Q̄α̇Qα = 2σμαα̇Pμ ⇒ ϵα(QαQ̄α̇ + Q̄α̇Qα)θ̄α̇ = 2(ϵασμαα̇θ̄α̇)Pμ ⇒ [θ̄α̇Q̄α̇, ϵαQα] = 2(ϵσμθ̄)Pμ (3.5)

where the Grassmann nature of θ, ϵ, Q and Q̄ means that we pick up a minus sign in going from the first line to the second, turning { , } into [ , ].

We now evaluate (3.4) using the BCH formula e^A e^B = e^(A+B+1/2[A,B]+...)

The commutator (3.5), together with the fact that the higher commutator terms ... in the BCH formula all vanish in the present case, gives us the result V(ϵ,ϵ̄)g̃(x,θ,θ̄) = eixP+i(θ+ϵ)Q+i(θ̄+ϵ̄)Q̄+(ϵσθ̄)P−(θσϵ̄)P = g̃(x + iθσϵ̄ − iϵσθ̄, θ + ϵ, θ̄ + ϵ̄)

Here we see the twist. The supercharges shift the Grassmann coordinate in superspace as we might have anticipated. But, at the same time, they also shift the point in Minkowski space by a Grassmann bilinear xμ → xμ + iθσμϵ̄ − iϵσμθ̄ θ → θ + ϵ θ̄ → θ̄ + ϵ̄ (3.6)

Note that the shift in xμ due to the Grassmann bilinear can't be thought of as normal translation by some number. Instead, it's a more formal expression. Ultimately, we'll see how this manifests itself in terms of the superfields and their more familiar components.

3.1.2 Superfields A superfield is a function on superspace, Y = Y(x,θ,θ̄). To start, we take this to be a complex-valued function on superspace.

In principle, the superfield could transform in some non-trivial representation of the Lorentz group. For example it could carry a vector index μ or a spinor index α. However, rather remarkably, we will find all the fields that we need – scalar, spinor and vector – lurking within the simplest scalar superfield. (We will, however, come across superfields carrying spinor indices in Section 4.)

To see this, we Taylor expand the superfield in θ and θ̄. But this is easy because θ and θ̄ are Grassmann valued objects obeying, for example, θαθβ = −θβθα This means that the Taylor expansion truncates after some finite length. In particular we have θαθβθγ = 0. So the Taylor expansion of Y(x,θ,θ̄) stops after terms quadratic in θ and θ̄. Expanding the superfield out in this way then reveals a bunch of more familiar fields lurking within, Y(x,θ,θ̄) = ϕ(x) + θαψα(x) + θ̄α̇χ̄α̇(x) + θ²M(x) + θ̄²N(x)

+ θαθ̄α̇Vαα̇(x) + θ²θ̄α̇λ̄α̇(x) + θ̄²θαρα(x) + θ²θ̄²D(x) (3.7)

Here θ² = θαθα and θ̄² = θ̄α̇θ̄α̇.

There are a few things to say about this. First, note that the superfield does indeed contain all the fields that we usually care about: there are four complex scalars ϕ, M, N and D, two left-handed spinors ψ and ρ, two right-handed spinors χ̄ and λ and a vector Vαα̇ = σμαα̇Vμ.

Second, note that it contains many more fields that we might have thought from our analysis in the previous section! The representations on single particle states suggested that there should be a chiral multiplet containing a single complex scalar and a Weyl fermion and a vector multiplet containing a gauge field and a Weyl fermion. Yet the superfield Y contains a plethora of such fields. We will shortly see how we can impose further restrictions on Y that truncate the number of fields lying within to match our earlier expectation.

Our next task is to understand how superfields transform under supersymmetry transformations. We’ll again start with translations xµ → xµ +aµ which, as we have seen, are generated by the unitary operator U = exp(iaµP). Previously, we viewed this as a group element acting on superspace. But in quantum field theory, it has another avatar as an operator acting on the Hilbert space. The fields in quantum field theory are, of course, also operators and the superfield is no different. The action of U on such operators enacts the translation, meaning UY(x,θ,θ ¯ )U† = Y(x+a,θ,θ ¯ ). For infinitesimal aµ, we expand U = eiaP = 1+ia Pµ+O(a)2. We also Taylor expand the field, Y(x+a) = Y(x)+aµ∂ Y(x)+O(a2). Equating the terms linear in a we see that the translations are captured in the commutation relation on fields [P ,Y] = −i∂ Y (3.8)

µ µ

We can treat the action of the supercharges in a similar fashion. We again have the unitary operator V(ϵ,ϵ¯) = exp ( iϵαQ +iϵ¯ Q ¯α˙ )

α α˙

Acting on superfields, this gives VY(x,θ,θ ¯ )V† = Y(x+iθσµϵ¯−iϵσµθ ¯ ,θ+ϵ,θ ¯ +ϵ¯) where we’ve invoked the transformation of the superspace coordinate (3.6). If we now treat ϵ as an infinitesimal spinor and work to leading order in ϵ, we find the commutation relations [Q ,Y] = −i (−σµ θ ¯α˙∂ ) Y (3.9)

α α αα˙ µ

[Q ¯ ,Y] = +i (+θασµ ∂ ) Y (3.10)

α˙ α˙ αα˙ µ

In this expression, the derivatives with respect to Grassmann coordinates are defined by ∂α = ∂/∂θα with ∂α θβ = δβα and ∂α θ ¯β˙ = 0 ∂ ¯α˙ = ∂/∂θ ¯α˙ with ∂ ¯α˙ θ ¯β˙ = δβ˙α˙ and ∂ ¯α˙ θβ = 0

These Grassmann derivatives are themselves Grassmann. This means that they pick up a minus sign when they pass through other Grassmann variables. So, for example, if you wish to differentiate χβθγ, where both χ and θ are Grassmann variables, then you have ∂/∂χα (χβθγ) = δβαθγ and ∂/∂θα (χβθγ) = −δγαχβ where that extra minus sign in the second expression comes from dragging the ∂/∂θα through the χβ before it gets to attack its prey.

It’s useful to define differential operators associated to the right-hand sides of (3.8), (3.9) and (3.10). To this end, we write Pµ = −i∂µ Qα = −i∂α −σµ θ ¯α˙∂µ (3.11)

Q ¯α˙ = +i∂ ¯α˙ +θασµ ∂µ

Be warned: these differ from the operators Pµ, Qα and Q ¯α˙ only by the use of curly calligraphic script. You can check that anti-commutation relation of these differential operators is something familiar {Qα, Q ¯α˙} = 2σµαα˙ Pµ

together with {Qα, Qβ} = {Q ¯α˙, Q ¯β˙} = 0. This is telling us that P, Q and Q also furnish a representation of the supersymmetry algebra, now acting on fields on superspace.

Supersymmetry Transformation of Fields

We can unpack the supersymmetry transformations (3.9) and (3.10) to see how it acts on the individual fields sitting with Y. The infinitesimal change of the superfield is defined to be δY = i[ϵQ+ϵ¯Q,Y] = i(ϵQ+ϵ¯Q)Y (3.12)

Expanding out Y in terms of the components (3.7), the operators Q and Q act on each term. Q removes a θ (where there is one) and adds a θ∂ (where there aren’t too many θ’s already) Obviously Q is the conjugate. We then compare the various θ and θ and terms.

For example, the lowest term in Y is the scalar ϕ(x). To compute its variation, we look for the term in δY with neither θ’s nor θ’s. This comes from ∂α˙ acting on the term θψ and ∂α acting on θχ¯. The result is δϕ = ϵψ +ϵ¯χ¯ (3.13)

Meanwhile, the highest term in Y is the scalar D(x). To compute its variation, we find the term in δY that comes with the full complement of θ2θ ¯2. This happens comes from the θ∂ term in Q and the θ∂ term in Q. The net effect is that the variation of D(x) is a total derivative δD = ∂µ (ϵσµλ ¯ −ρσµϵ¯) (3.14)

This will prove to be part of the story as we proceed.

It takes a bit of work to get the transformation of all the remaining component fields in (3.7). You’ll have the pleasure of doing this work in the first examples sheet. The answer turns out to be δψµ = 2ϵMµ +(σµϵ¯)(i∂µϕ+Vµ) δχ¯µ = 2ϵ¯Nµ −(ϵσµ)(i∂µϕ−Vµ) δMµ = ϵ¯λ ¯µ − ∂µψσµϵ¯ δNµ = ϵρµ+ ϵσµ∂ µχ¯ δVµ = ϵσµλ ¯µ +ρσµϵ¯+ (∂νψσν σ¯ µϵ−ϵ¯σ¯ µσν∂νχ¯) (3.15) δλ ¯µ = 2ϵ¯D+ σ¯νσµϵ¯∂ V +iσ¯µϵ∂ M µ ν µ δρµ = 2ϵD− σνσ¯µϵ∂ V +iσµϵ¯∂ N µ ν µ

The variation of each has at least two terms, one with a derivative ∂ and one without.

3.1.3 Constraining Superfields

As we already commented, the superfield Y is too big. It has way more fields than we expect from the representation theory of Section 2.3. This is because Y is not an irreducible representation. It can be reduced to something smaller. The question is: how? We want to impose constraints on Y such that it remains a superfield. That means that whatever object we have after the constraint should also transform as (3.9) and (3.10) under supersymmetry transformations. So our first step to understanding the possible constraints is to figure out what kind of operations we can perform on superfields that keep them as superfields.

There are some obvious operations, albeit ones that won’t help with our constraint. If we have two superfields \( Y_1 \) and \( Y_2 \), then \(\alpha Y_1\) is a superfield for any \(\alpha \in \mathbb{C}\), as is \(Y_1 + Y_2\) and \(Y_1 Y_2\). For example, to see that \(Y_1 Y_2\) is a superfield, we need to note that \[ [Q_\alpha, Y_1 Y_2] = [Q_\alpha, Y_1] Y_2 + Y_1 [Q_\alpha, Y_2] = (Q_\alpha Y_1) Y_2 + Y_1 (Q_\alpha Y_2) = Q_\alpha (Y_1 Y_2)

\]

as required.

More pertinent for our purposes, if \(Y\) is a superfield then so too is \(\partial_\alpha Y\). However, crucially, neither \(\partial_\alpha Y\) nor \(\partial_{\dot{\alpha}} Y\) are superfields. Algebraically, this is because \[ [\epsilon_\alpha Q^\alpha, \partial_{\dot{\alpha}} \bar{Y}] = \epsilon_\alpha \sigma^\mu_{\alpha \dot{\alpha}} \partial_\mu \neq 0.

\]

To build some intuition for what’s going on, note that \(\partial_{\dot{\alpha}} Y\) doesn’t include, for example, the highest component \(\theta^2 \bar{\theta}^2 D\) term; there was such a term in \(Y\) but one of the \(\bar{\theta}\)’s is removed after acting with \(\partial_{\dot{\alpha}}\). However, acting with a supercharge \(Q_\alpha\) will generate such a term. In other words, it’s not consistent with supersymmetry to simply state by fiat that the last term vanishes, \(D(x) = 0\). Act with a supersymmetry transformation and this will no longer be true. It’s analogous to setting \(A_3 = 0\) in a vector field \(A_\mu\) and thinking that you’ve found an object with just three components, only to realise that \(A_3\) gets resurrected after a rotation.

However, there is a way forward. We define the covariant derivatives \[ D_\alpha = \partial_\alpha + i \sigma^\mu_{\alpha \dot{\alpha}} \bar{\theta}^{\dot{\alpha}} \partial_\mu, \]

\[ \bar{D}_{\dot{\alpha}} = -\bar{\partial}_{\dot{\alpha}} - i \theta^\alpha \sigma^\mu_{\alpha \dot{\alpha}} \partial_\mu.

\]

These are very similar to the \(Q_\alpha\) and \(\bar{Q}_{\dot{\alpha}}\) differential operators defined in (3.11), but with a relative minus sign difference (and an overall factor of \(i\) difference). Their key property is that they anti-commute with \(Q_\alpha\) and \(\bar{Q}_{\dot{\alpha}}\)

\[ \{D_\alpha, Q_\beta\} = \{D_\alpha, \bar{Q}_{\dot{\beta}}\} = \{\bar{D}_{\dot{\alpha}}, Q_\beta\} = \{\bar{D}_{\dot{\alpha}}, \bar{Q}_{\dot{\beta}}\} = 0, \qquad (3.16)

\]

The covariant derivatives also obey \[ \{D_\alpha, \bar{D}_{\dot{\beta}}\} = 2 \sigma^\mu_{\alpha \dot{\alpha}} P_\mu, \qquad (3.17)

\]

together with \(\{D_\alpha, D_\beta\} = \{\bar{D}_{\dot{\alpha}}, \bar{D}_{\dot{\beta}}\} = 0\).

From (3.16), we have \[ [\epsilon Q + \bar{\epsilon} \bar{Q}, D_\alpha] = [\epsilon Q + \bar{\epsilon} \bar{Q}, \bar{D}_{\dot{\alpha}}] = 0.

\]

This tells us that both \(D_\alpha Y\) and \(\bar{D}_{\dot{\alpha}} Y\) are superfields. For example, under the supersymmetry transformation (3.12), we have \[ \delta Y = i (\epsilon Q + \bar{\epsilon} \bar{Q}) Y \Rightarrow \delta(D_\alpha Y) = i (\epsilon Q + \bar{\epsilon} \bar{Q}) D_\alpha Y.

\]

Now we can discuss the various constraints that we can place on a superfield \(Y\). There are four of interest (of which, only three will play a major role in these lectures).

- A chiral superfield \(\Phi\) is defined by the constraint \[ \bar{D}_{\dot{\alpha}} \Phi = 0.

\]

- An anti-chiral superfield \(\Psi\) is defined by the constraint \[ D_\alpha \Psi = 0.

\]

Note that you can’t impose both chiral and anti-chiral conditions since the anti-commutator (3.17) would then require that the superfield is actually constant. Moreover, if \(\Phi\) is a chiral superfield then \(\bar{\Phi} = \Phi^\dagger\) is an anti-chiral superfield. (I give a simple way to see this at the end of Section 3.1.4.) The fact that we can’t impose both conditions simultaneously means that we can’t take \(\Phi\) to be real: chiral superfields are necessarily complex. We will see that chiral superfields correspond to the chiral multiplets that we met in Section 2.3.

- A real superfield \(V\) is defined by the simple requirement that \[ V = V^\dagger.

\]

We will postpone our discussion of real superfields to Section 4. There we will see that the real superfields correspond to the vector multiplet that we met in Section 2.3.

- Finally, a linear superfield \(J\) is defined \[ J = J^\dagger \quad \text{and} \quad D^2 J = \bar{D}^2 J = 0.

\]

These play a slightly less prominent role than the (anti)-chiral and real superfields. In particular, we won’t build supersymmetry actions out of linear superfields. However, it turns out that they are useful homes for certain composite operators in quantum field theory, most notably Noether currents associated to global symmetries.

We will spend the rest of this section studying the properties of chiral superfields.

3.1.4 Chiral Superfields A chiral superfield obeys the constraint \[ \bar{D}_{\dot{\alpha}} \Phi = 0. \qquad (3.18)

\]

We will first solve this equation to understand what it means for the superfield \(\Phi\). There’s a useful trick here. We introduce the coordinate \[ y^\mu = x^\mu + i \theta \sigma^\mu \bar{\theta}.

\]

The advantage of this coordinate is that we have \[ \bar{D}_{\dot{\alpha}} y^\mu = \left( -\bar{\partial}_{\dot{\alpha}} - i \theta^\alpha \sigma^\nu_{\alpha \dot{\alpha}} \partial_\nu \right) \left( x^\mu + i \theta^\beta \sigma^\mu_{\beta \dot{\beta}} \bar{\theta}^{\dot{\beta}} \right) = -i \theta^\alpha \sigma^\mu_{\alpha \dot{\alpha}} - i \partial_{\dot{\alpha}} \left( \theta^\beta \sigma^\mu_{\beta \dot{\beta}} \bar{\theta}^{\dot{\beta}} \right) = 0, \]

where to see that the two terms cancel, you have to remember that you pick up an extra minus sign as the \(\bar{\partial}_{\dot{\alpha}}\) passes through the \(\theta^\beta\). In addition, we have \[ \bar{D}_{\dot{\alpha}} \theta_\beta = 0.

\]

This means that if we view a general superfield as a function of \(\Phi = \Phi(y, \theta, \bar{\theta})\) then, of the three arguments, only \(D_\alpha \theta^\beta \neq 0\) and the condition (3.18) tells us \[ \bar{D}_{\dot{\alpha}} \Phi = 0 \Rightarrow \Phi = \Phi(y, \theta).

\]

In other words \(\Phi\) is almost a function only of \(\theta\) and not of \(\bar{\theta}\), the “almost” because there is in fact a \(\bar{\theta}\) buried in the \(y^\mu\). This means that we can expand in components \[ \Phi(y, \theta) = \phi(y) + \sqrt{2} \theta \psi(y) + \theta^2 F(y), \]

where the \(\sqrt{2}\) is a convention. We can then further Taylor Let us expand the y^μ to get the expression for a chiral superfield in components Φ(x,θ,θ ¯ ) = ϕ(x)+ 2θψ(x)+θ^2 F(x)

+ (i/2) θσ^μθ ¯ ∂_μ ϕ(x)− (1/√2) θ^2∂_μ ψ(x)σ^μθ ¯ − θ^2θ ¯^2 □ϕ(x)   (3.19)

with □ = ∂_μ ∂^μ. We see that the chiral superfield contains just three component fields: a complex scalar ϕ, a Weyl spinor ψ and another complex scalar F. The higher components of Φ(x) are simply derivatives of the first two fields.

This is much closer to what we expected based on our analysis in Section 2.3. There we found a chiral multiplet consists of single particle states associated to a complex scalar ϕ and a Weyl fermion ψ. However, we’ve also got a second complex scalar F. We will see later that this is an object known as an auxiliary field. For now it’s worth noticing that, in contrast to ϕ and ψ, there are no terms in the chiral superfield with ∂F. This will be important as we proceed.

The supersymmetry transformations of the chiral multiplet are δϕ = 2ϵψ δψ = √2 iσ^μϵ¯ ∂_μ ϕ+ √2 ϵF   (3.20)

δF = √2 iϵ¯ σ¯^μ∂_μ ψ

Note that F transforms as a total derivative, just like D in the original unconstrained superfield (3.14). We’ll see the relevance of this shortly.

There is a very similar story for the anti-chiral superfields. As we mentioned previously, these can be viewed as the complex conjugate of a chiral superfield. To see this, note that if a chiral superfield Φ(y,θ) is a function of y^μ and θ, then its conjugate Φ†(y ¯ ,θ ¯ ) is a function of y ¯^μ = x^μ−iθσ^μθ ¯ and θ ¯ . But it’s simple to check that D_α y ¯^μ = D_α θ ¯^˙α = 0 and so Φ† is indeed an anti-chiral superfield obeying D_α Φ† = 0. In components, we have Φ†(y ¯ ,θ ¯ ) = ϕ†(y ¯ )+ 2θ ¯ ψ ¯ (y ¯ )+θ ¯^2 F†(y ¯ )

We can then further expand out y ¯ further if we wish to get an expression analogous to (3.19), Φ†(x,θ,θ ¯ ) = ϕ†(x)+ 2θ ¯ ψ ¯ (x)+θ ¯^2 F†(x)

− (i/2) θσ^μθ ¯ ∂_μ ϕ†(x)+ (1/√2) θ ¯^2 θσ^μ ∂_μ ψ ¯ (x)− (1/4) θ^2θ ¯^2 □ϕ†(x)

## 3.2 And...Action

To construct actions that are invariant under Poincaré group, we take suitable Lagrangian densities of fields and integrate them over spacetime. Analogously, to construct actions that are invariant under supersymmetry, we take suitable Lagrangian densities of superfields and integrate them over superspace.

3.2.1 Integrating Over Superspace

First, let’s remind ourselves how Grassmann integration works. (It is, happily, much easier than normal integration!) If we have a single Grassmann variable θ then ∫ dθ 1 = 0   and   ∫ dθ θ = 1 This means that if we have a function f(x,θ) = f_0(x) + θf_1(x), then Grassmann integration picks out the component multiplying θ, ∫ dθ f(x,θ) = f_0(x)

In this manner, integration over Grassmann variables is the same thing as differentiation: dθ = ∂/∂θ. In particular, we have a Grassmann version of the fundamental theorem of calculus ∫ dθ = ∫ dθ ∂f/∂θ = 0   (3.21)

Here we will need to integrate over superspace, parameterised by θ and θ ¯^˙α. We define ∫ d^2θ = (1/2) ∫ dθ1 dθ2   and   ∫ d^2θ ¯ = −(1/2) ∫ dθ ¯1 dθ ¯2 Those strange factors of 1/2 are because θ^2 = θ^α θ_α = −2θ1θ2. We then have ∫ d^2θ θ^2 = −∫ dθ1 dθ2 (θ1 θ2) = 1 where the minus sign disappears when dθ2 moves past θ1. Note that the measure d^2θ ¯ comes with an extra minus sign but this cancels the corresponding minus sign in θ ¯^2 = θ ¯ _˙α θ ¯^˙α = +2θ ¯1 θ ¯2. Once again, we have ∫ d^2θ ¯ θ ¯^2 = 1. Finally, we also use the (not entirely logical) notation ∫ d^4θ = ∫ d^2θ d^2θ ¯

Now suppose that we build an action out of some function of superfields. That function will itself be a superfield that we will call K(x,θ,θ ¯ ) but, in contrast to what we’ve discussed so far, we’ll view K as a composite superfield whose components are functions of other fields. We then construct the action of the form S = ∫ d^4x d^4θ K(x,θ,θ ¯ )   (3.22)

The action is real if K is a real superfield, obeying K = K†. As we saw above, this is a valid constraint on a superfield. Under a supersymmetry transformation, we have δS = ∫ d^4x d^4θ δK where any superfield K must change as (3.12). This means that we have δK = ϵ^α(∂_α K − iσ^μ_{α ˙α} θ ¯^˙α ∂_μ K) + (−∂ ¯_˙α K + iθ^α σ^μ_{α ˙α} ∂_μ K)ϵ ¯^˙α But each of these terms involves a derivative. Those terms that are differentiated with respect to a Grassmann coordinate automatically vanish when integrated over superspace by virtue of (3.21). Meanwhile, those terms that involve a differential ∂_μ give at most a boundary term which, if fields drop off suitably quickly asymptotically, also vanishes. We learn that any action of the form (3.22) is necessarily invariant under supersymmetry: δS = 0

In fact, we can give an expression for the action. The superfield K has an expansion K(x,θ,θ ¯ ) = K_first(x)+...+θ^2θ ¯^2 K_last(x)

The action (3.22) simply picks up the last of these terms S = ∫ d^4x K_last(x)

We refer to terms in the action that come from integrating over all of superspace as D-terms. The name isn’t a great one but comes from the fact that the last component in a real superfield is often related to the superfield D.

eld is usually denoted D. In anticipation of this, in the general expansion of the superfield (3.7) we called the final term D. We also saw that it transforms as a total derivative under a supersymmetry transformation (3.14). This gives another way of seeing the result above: any Lagrangian given by a D-term transforms as a total derivative and so the action is invariant.

3.2.2 The Action for Chiral Superfields What does this mean for our chiral superfield Φ? As with any other field, we have a choice of what action to build. But, typically in quantum field theory, the simplest possibilities are the most interesting.

Because Φ is complex, we also necessarily have the anti-chiral superfield Φ† to play with. Multiplying these together gives a real superfield Φ†Φ that we can integrate over superspace to get the action, S = ∫ d⁴x d⁴θ Φ†Φ chiral This means that the action is given by the D-term of Φ†Φ. A short calculation, and some integration by parts, shows that the action becomes S = ∫ d⁴x [ ∂_μ ϕ† ∂^µ ϕ − i ψ ¯σ^µ ∂_µ ψ + F†F ] chiral where we have thrown away some total derivatives. These are just the standard kinetic terms for a complex scalar ϕ and Weyl fermion ψ. But now we see that there’s something special about F: it doesn’t have any kinetic terms. Moreover, this will continue to be true as we write down further supersymmetric interactions. This is what it means to be an auxiliary field.

Because there are no kinetic terms for F, it has no propagating degrees of freedom and, when quantised, doesn’t give rise to any particle states. That’s why it didn’t appear in our representation theory analysis of Section 2.3. Nonetheless, there is a good reason that F appears in the chiral superfield.

When looking at single particle states, we previously argued that there have to be equal number of bosonic and fermionic degrees of freedom. And there are. But now we’re looking at the action, we can ask two variants of this question. First, we can insist that the number of physical propagating degrees of freedom match. In the context of field theory, these are said to be “on-shell” degrees of freedom. This means that we count the degrees of freedom after imposing the equations of motion. The complex scalar field ϕ has two degrees of freedom, while the non-propagating scalar F has none. Meanwhile, the Weyl fermion ψ has two complex components but obeys a first order, rather than second order equation of motion which means that ψ counts both “position” and “momentum”. So the equation of motion cuts the number of on-shell degrees of freedom, giving two. This, of course, matches the degrees of freedom of ϕ.

However, we require the action to be invariant under supersymmetry for all field configurations, not just those that obey the equations of motion. And this motivates us to count the “off-shell” degrees of freedom, meaning the number of fields before equations of motion are imposed. The two complex scalars ϕ and F have two each, while the Weyl spinor ψ has four off-shell degrees of freedom because it contains two complex components. The presence of the auxiliary field F is required to match these off-shell degrees of freedom.

Next we want to write down supersymmetric masses and Yukawa-type interactions for these fields. These don’t arise from D-terms. Indeed, you could try writing down a more general function K(Φ, Φ†) and integrating over d⁴θ but you’ll find that it doesn’t generate the kind of interactions we want. (We’ll see what it does generate in Section 3.2.4.) Instead we have to do something different.

This something different is an option that arises only for chiral superfields. Roughly speaking, because a chiral superfield depends on only half of superspace, we can get a supersymmetric action by integrating it over only half of superspace.

More precisely, given a chiral superfield Φ the function W(Φ) is also a chiral superfield. In components it reads W(Φ) = W(ϕ) + √2 θ ψ ∂W/∂ϕ + θ² [ F ∂W/∂ϕ − 1/2 ψψ ∂²W/∂ϕ² ] + ...

where the +... are the extra terms on the second line of (3.19) that include a θ term. But, as you can see in (3.19), each of these is a total derivative and so will not contribute to the action. This means that, for the purposes of building an action, we can think of W(Φ) as a function only of θ and not of θ̄. This means that we can construct a supersymmetric action by integrating over only half of superspace S = ∫ d⁴x [ ∫ d²θ W(Φ) + ∫ d²θ̄ W†(Φ†) ]

where the second term is the Hermitian conjugate of the first and is needed to make the action real. This action picks out the θ² term in W(Φ) and is known as an F-term, so named because the auxiliary field in a chiral multiplet is usually called F.

We see in (3.20) that the F field (and, by extension any F term that multiplies θ² in a chiral multiplet) transforms as a total derivative under supersymmetry. This gives us another way to see that the action S is indeed invariant under supersy Putting together the D-term and F-term contributions, we get our final supersymmetric action S = S_chiral + S_W = ∫ d⁴x [ ∂_µ ϕ† ∂^µ ϕ − i ψ̄ σ̄^µ ∂_µ ψ + F†F + F (∂W/∂ϕ − 1/2 ∂²W/∂ϕ² ψψ) + h.c. ]

This is known as the Wess-Zumino action. The function W(Φ) is called the superpotential.

(An aside: There is a completely different object that is also called the Wess-Zumino action, or sometimes the Wess-Zumino-Witten or WZW action. This is a topological term that involves an integral over a higher dimensional space. It has nothing to do with supersymmetry. You can read about it in the lectures on Gauge Theory.)

As promised, the auxiliary field F appears only algebraically in the action. For such fields, it is legitimate to eliminate it by the equation of motion which, in this case, reads simply F + ∂W†/∂ϕ† = 0 and F† + ∂W/∂ϕ = 0 Putting this back into the action gives us an action just in terms of those fields that have propagating degrees of freedom, S = ∫ d⁴x [ ∂_µ ϕ† ∂^µ ϕ − i ψ̄ σ̄^µ ∂_µ ψ − |∂W/∂ϕ|² − 1/2 (∂²W/∂ϕ² ψψ + ∂²W†/∂ϕ†² ψ̄ ψ̄) ]

This is the form of the action that we met back in the introduction in (1.1). We see that the scalar potential is positive definite and takes the form V(ϕ, ϕ†) = |∂W/∂ϕ|² We still have to specify the form of the superpotential. In general, this can be any holomorphic function of ϕ. If we want to restrict ourselves to theories that are renormalisable then we should take a superpotential that is no greater than cubic. For example, we could take W(Φ) = m/2 Φ² + λ/3 Φ³ (3.23)

In general, both m and λ can be complex. This gives the potential V = |mϕ + λϕ²|² After expanding this out, the mass of the scalar field is |m|. Note that, in addition to the |ϕ|⁴ term, there are also cubic terms ϕ²ϕ† and ϕ†²ϕ. These give Feynman diagrams in which a single ϕ particle splits into two others which means that particle number is not conserved in the Wess-Zumino model and, relatedly, there is no way to distinguish particles from anti-particles. This is related to the fact the theory does not have a U(1) global symmetry in the presence of the general superpotential (3.23) with m, λ ≠ 0.

With a cubic superpotential, the equation of motion for the Weyl fermion is i σ̄^µ ∂_µ ψ + m* ψ̄ = −2λ* ϕ† ψ̄ The fermion also has mass |m|. There is no U(1) symmetry associated to this fermion and the mass is an example of a Majorana mass. Note also that the Yukawa term on the right-hand side specifies the interaction between the fermion and scalar and is characterised by the same coupling λ that determines the self-interaction of the scalar. This will have important consequences when we turn to the quantum theory.

Multiple Chiral Superfields There is a straightforward generalisation of the Wess-Zumino action to multiple chiral superfields Φ_i. We now take the action S = ∫ d⁴x d⁴θ Σ_i Φ_i† Φ_i + ∫ d⁴x (∫ d²θ W(Φ) + h.c.) (3.24)

where if we wish the theory to be renormalisable we should again restrict to a cubic superpotential W(Φ) = 1/2 m_ij Φ_i Φ_j + 1/3 λ_ijk Φ_i Φ_j Φ_k The resulting potential is V(ϕ) = Σ_i |∂W/∂ϕ_i|² Again, this is positive definite as it must be in a supersymmetric theory since the energy is necessarily positive.

As we have seen, for a single massive chiral multiplet the Weyl fermion necessarily has a Majorana mass. With two chiral multiplets, we may have a Dirac mass. Let’s call the chiral multiplets Φ and Φ̃. Then the simple superpotential W = m Φ Φ̃ gives rise to two Weyl equations, each of which mixes the spinors ψ and ψ̃, i σ̄^µ ∂_µ ψ + m* ψ̃̄ = 0 and i σ̄^µ ∂_µ ψ̃ + m* ψ̄ = 0 This is the Dirac equation, decomposed into two Weyl pieces. (Sorry for the ugliness of piling a bar on top of a tilde.) Note that it now has a U(1) symmetry, under which ψ and ψ̃ (or, equivalently the superfields Φ and Φ̃) rotate with opposite charges.

3.2.3 Supersymmetry of the Wess-Zumino Model Revisited It’s worth pausing for a recap. We’ve derived the Wess-Zumino model which, for a single chiral superfield, before integrating out F, is given by S = ∫ d⁴x [ ∂_µ ϕ† ∂^µ ϕ − i ψ̄ σ̄^µ ∂_µ ψ + F†F + F (∂W/∂ϕ − 1/2 ∂²W/∂ϕ² ψψ) + h.c. ]

Our arguments involving superspace have told us that this action is invariant under the supersymmetry transformations (3.20).

δϕ = 2εψ δψ = √2 i σ^µ ε̄ ∂_µ ϕ + √2 ε F δF = 2i ε̄ σ̄^µ ∂_µ ψ together with the hermitian conjugate transformations δϕ† = 2 ε̄ ψ̄ δψ̄ = −√2 i ε σ^µ ∂_µ ϕ† + √2 ε̄ F† δF† = 2i ε σ^µ ∂_µ ψ̄ But this is something that we can just check. It’s a little tedious but, given the importance of this result, it’s worth doing. From our discussion above, we know that the kinetic terms and the superpotential terms should be independently invariant. We can check each in turn. First the kinetic terms. We have δS_chiral = ∫ d^4x [ ∂_μ ϕ† ∂^μ δϕ − i δψ̄ σ̄^μ ∂_μ ψ + F† δF + h.c. ]

We’ve kept only half the terms, the other half buried in the hermitian conjugate. (Admittedly, there was some forethought involved in which terms to keep to ensure that they cancel among themselves.) Using the supersymmetry transformations above, we have δS_chiral = √2 ∫ d^4x [ ∂_μ ϕ† ε ∂^μ ψ − ∂_ν ϕ† ε σ^ν σ̄^μ ∂_μ ψ − i F† ε̄ σ̄^μ ∂_μ ψ + i F† ε̄ σ̄^μ ∂_μ ψ + h.c. ]

We see that the two terms with F† cancel immediately. For the other two terms we have a little bit of work to do. Note that, by integrating by parts twice, we can symmetrise over (μν) in the second term. But you can check that σ^(ν σ̄^μ) = η^{μν} which then ensures that the first two terms also cancel and δS_chiral = 0.

For the superpotential terms we have δS_W = ∫ d^4x [ δF + F δϕ − ∂W/∂ϕ ψ δψ − (1/2) ∂²W/∂ϕ² ψ ψ δϕ + h.c. ]

The final ∂³W/∂ϕ³ term multiplies ψ³ and so vanishes because ψ is a 2-component Grassmann field. We’re then left with δS_W = √2 ∫ d^4x [ i ε̄ σ̄^μ ∂_μ ψ + F ε ψ − i ψ σ^μ ε̄ ∂_μ ϕ − F ε ψ + h.c. ]

The F ε ψ terms cancel immediately. The other two cancel after an integration by parts, together with the fact that ψ σ^μ ε̄ = − ε̄ σ̄^μ ψ. We then have δS_W = 0 as promised.

There is also a version of this calculation after we have integrated out the auxiliary field F, replacing it with its equation of motion F = −∂W†/∂ϕ†. As we’ve seen, the Wess-Zumino action becomes S = ∫ d^4x [ ∂_μ ϕ† ∂^μ ϕ − i ψ̄ σ̄^μ ∂_μ ψ − |∂W/∂ϕ|² − (1/2) ∂²W/∂ϕ² ψ ψ − (1/2) ∂²W†/∂ϕ†² ψ̄ ψ̄ ]

We can also replace F in the supersymmetry transformations. These become δϕ = √2 ε ψ  and  δψ = √2 i σ^μ ε̄ ∂_μ ϕ − √2 ε ∂W†/∂ϕ† The calculation described above goes through with only minor modifications (although you can no longer treat the kinetic and superpotential terms independently). This is the supersymmetry invariance of the Wess-Zumino model that we promised back in the introduction.

3.2.4 Non-Linear Sigma Models The restriction to a cubic superpotential above is motivated by the requirement that the theory be renormalisable. But for theories of scalars, this requirement isn’t always at the top of our list. The reason is that these theories may arise as the low-energy description of something more interesting. In this situation, there’s no reason to think that the low-energy description should be valid at arbitrarily high-energy scales and so no reason to impose renormalisability.

An illustrative analogy can be found in QCD. At high energies this is a theory of quarks and gluons but at low energies, after confinement has imposed itself on the dynamics, it is a theory of light scalar particles called pions. We denote these fields as π_i(x) with i labelling the different pion fields. (For what it’s worth, i = 1,...,8 in QCD if we include mesons that contain up, down and strange quarks.) The low-energy dynamics of pions takes the form S_NLSM = ∫ d^4x g_{ij}(π) ∂_μ π^i ∂^μ π^j   (3.25)

Theories of this kind go by the unhelpful name of non-linear sigma models. The fields π_i can be thought of as coordinates on some manifold M that is called the target space. The interactions are hiding in the derivative terms and are packaged into a collection of functions g_{ij}(π) that can be viewed as a metric on M. The action (3.25) describes massless scalar fields, although it is always possible to add mass terms if necessary.

Actions of the type (3.25) arise in many places in physics. We first meet them in General Relativity as the action for particles (rather than fields) moving in a curved space or spacetime. But they also occur in many places in condensed matter physics and statistical physics. (The O(N) models discussed in the lectures on Statistical Field Theory are an example.) You can learn more about the specific metric g_{ij}(π) that describes pion dynamics in Section 5 of the lectures on Gauge Theory. Here, our interest is in writing down supersymmetric versions of non-linear sigma models.

We can achieve this simply by introducing more interesting D-terms. We consider n chiral superfields Φ_i with i = 1,...,n. We’ll denote the anti-chiral superfields as Φ̄_ī with the ī = 1,...,n index a useful reminder that these label anti-chiral fields. We then consider the action S = ∫ d^4x d^4θ K(Φ, Φ̄)   (3.26)

with K(Φ, Φ̄) any real function of these superfields. This function is known as the Kähler potential.

Previously, we took K = Σ Φ̄_ī Φ_i We will refer to this as the canonical Kähler potential. It is the form that we must take if we want our theory to renormalisable. But if we’re willing to entertain low-energy effective theories then we can take a general, real function K. To compute the resulting action, we simply need to compute the D-term of K(Φ, Φ†). This calculation is a little laborious but the result is quite beautiful.

The supersymmetric non-linear sigma model takes the form

S = ∫d⁴x [ gᵢⱼ̄( ∂ᵢϕⁱ ∂µϕ̄ʲ + ∂µψⁱσµψ̄ʲ − ψⁱσµ ∂µψ̄ʲ + FⁱF̄ʲ )

+ (1/2) ( ∂g/∂ϕᵏ )ᵢⱼ̄ ( ψᵏψⁱ F̄ʲ − i ψ̄ʲσµψⁱ ∂µϕᵏ ) + h.c.

+ (1/4) ( ∂²g/∂ϕᵏ∂ϕ̄ˡ )ᵢⱼ̄ (ψⁱψᵏ)(ψ̄ʲψ̄ˡ) ]

where the metric gᵢⱼ̄ is related to the Kähler potential as gᵢⱼ̄ = ∂²K / ∂ϕⁱ ∂ϕ̄ʲ

Note that this metric only has components with one holomorphic and one anti-holomorphic index. We can eliminate the auxiliary field F through its equation of motion gᵢⱼ̄ Fⁱ + (1/2) ( ∂g/∂ϕᵏ )ᵢⱼ̄ ψᵏψⁱ = 0   and   gᵢⱼ̄ F̄ʲ + (1/2) ( ∂g/∂ϕ̄ˡ )ᵢⱼ̄ ψ̄ˡψ̄ʲ = 0

Substituting this back into the action, we find S = ∫d⁴x [ gᵢⱼ̄( ∂ᵢϕⁱ ∂µϕ̄ʲ + Dµψⁱσµψ̄ʲ − ψⁱσµ Dµψ̄ʲ ) + Rᵢⱼ̄ₖₗ̄ (ψⁱψᵏ)(ψ̄ʲψ̄ˡ) ]

Rather wonderfully, all the terms now take a nice geometrical form. The kinetic term for the fermion involves a kind of covariant derivative, defined by Dµψⁱ = ∂µψⁱ + Γⁱⱼₖ ψʲ ∂µϕᵏ

where, for a metric given by (3.28), the Christoffel symbol is given by Γⁱⱼₖ = gⁱˡ̄ ∂gₗ̄ₖ / ∂ϕʲ

Meanwhile, the four-fermion interaction terms come multiplying the Riemann tensor. For a metric given by (3.28), this too takes a special form Rₘₙₚₚ = gᵐⁱ ∂Γⁱⱼₖ / ∂ϕ̄ˡ = gᵢⱼ̄ ∂²gₖₗ̄ / ∂ϕⁱ ∂ϕ̄ˡ − gₘⁿ̄ ∂gₚⁿ̄ / ∂ϕᵏ ∂gₘⱼ̄ / ∂ϕ̄ˡ

We have stumbled upon the mathematical framework of Kähler geometry. This is a particular form of complex geometry that can be placed on manifolds that are even dimensional and can be endowed with complex coordinates, like the ϕⁱ above. A Kähler manifold is a manifold that is endowed with a Kähler two-form Ω = 2i gᵢⱼ̄ dϕⁱ ∧ dϕ̄ʲ such that dΩ = 0

This requires that the gᵢⱼ̄ satisfies ∂gᵢⱼ̄ / ∂ϕᵏ = ∂gₖⱼ̄ / ∂ϕⁱ   and   ∂gᵢⱼ̄ / ∂ϕ̄ˡ = ∂gᵢₗ̄ / ∂ϕ̄ʲ

This condition is locally equivalent to the existence of a Kähler potential K(ϕ,ϕ̄), with the metric given by (3.28).

Finally, note that the Kähler potential is not unique. The action (3.26) is invariant under any shift K(Φ,Φ̄) → K(Φ,Φ̄) + Λ(Φ) + Λ̄(Φ̄)

where Λ(Φ) is any holomorphic function of Φⁱ. This is because Λ(Φ) is a chiral superfield and necessarily vanishes when integrated over all of superspace. These shifts are called Kähler transformations.

Supersymmetry has led us to the mathematical framework of Kähler geometry. This is just one of many close connections between supersymmetry and interesting geometric structures. Some of these connections are explored further in the lectures on Supersymmetric Quantum Mechanics.

Adding a Superpotential The supersymmetric non-linear sigma model (3.27) describes massless fields. We can always add an additional superpotential W(Φ) to the action. We won’t write down the full action, but simply comment that the scalar potential now takes the form V(ϕ,ϕ̄) = gᵢⱼ̄ (∂W/∂ϕⁱ)(∂W†/∂ϕ̄ʲ)

with gᵢⱼ̄ the inverse metric.

A Comment on Supergravity Throughout these lectures we will restrict ourselves to theories with global, or rigid, supersymmetry. As we’ve mentioned previously, if one extends supersymmetry to a gauge symmetry, making it local, then the resulting theory necessarily includes gravity. This is supergravity. In this case, the scalar potential for a bunch of chiral multiplets again has a fixed form, depending only on the Kähler potential K and superpotential W. It is V(ϕ,ϕ̄) = e^(K/M_pl²) [ gᵢⱼ̄ (DⁱW)(D̄ʲW†) − 3|W|²/M_pl² ]

where DⁱW = ∂W/∂ϕⁱ + (∂K/∂ϕⁱ)W/M_pl²

Here M_pl is the Planck mass. In the limit that M_pl → ∞, gravity becomes arbitrarily weak and the potential (3.30) reduces to our previous potential (3.29).

Perhaps surprisingly, the supergravity potential is not positive definite. This is related to the fact that supersymmetric theories can exist in anti-de Sitter spacetimes with a negative cosmological constant.

## 3.3 Non-Renormalisation Theorems

So far our discussion of supersymmetric theories has been entirely classical. But the great advantage of supersymmetry is that it allows us to gain control over the quantum dynamics of the theory. We can start to understand this already just with chiral multiplets. In this section we will show that the superpotential does not receive quantum corrections at any order in perturbation theory. This is known as a non-renormalisation theorem. In contrast, all bets are off with the Kähler potential: it is no more constrained than the kinetic terms in any other quantum field theory.

The original proof of the non-renormalisation theorem used Feynman diagrams for superfields. This means that we write down a diagram in which, say, the propagators correspond to superfields. These “super-Feynman diagrams” then encode a number of normal Feynman diagrams, some with bosons running in loops and others with fermions running in loops. One can then show that the most general super-Feynman diagram doesn’t contribute to the superpotential.

In these lectures, we’re not going to develop the machinery of superfield Feynman diagrams. Instead, we will give a much simpler argument that uses only the symmetries of the problem.

Before we get going, an important comment. Throughout these lectures, theories of chiral superfields will typically be viewed as low-energy effective actions. More precisely, they will be viewed as Wilsonian low-energy effective actions. This means that they describe physics only on some suitably large length scale, or equivalently at energies less than some UV cut-off, E ≤ Λ_UV. All short distance, or high energy, degrees of freedom have been integrated out but may, in some cases, leave an imprint on the low-energy degrees of freedom. We’ll see examples of this as we proceed.

A Wilsonian effective action already takes into account any quantum effects above the cut-off Λ_UV. But not those below. You need to use the action to compute, for example, loop diagrams to understand the low-energy quantum dynamics. But there are no UV divergences because the action comes equipped with an explicit cut-off.

There is another, more formal kind of effective action that is common in quantum field theory. This is the one particle irreducible, better known as 1PI, effective action. It arises as the Legendre transform of the (log of) the partition function. In contrast to the Wilsonian effective action, the 1PI effective action is best viewed as a classical action, with all quantum effects already taken into account. This can be problematic in the presence of massless particles since the 1PI effective action may have IR singularities. In contrast, there is no such problem with the Wilsonian effective action.

3.3.1 R-Symmetry Revisited Given a quantum field theory, one of the first things we should do is understand its symmetries. The kind of Wess-Zumino models (or, more generally non-linear sigma models) that we’ve described above could have many different Abelian or non-Abelian global symmetries acting on the chiral superfields Φ_i. However, there is one that is of particular importance. This is the U(1) R-symmetry. It is special because it does not commute with supersymmetry. Instead, as we saw in (2.25), it obeys [R, Q_α] = −Q_α and [R, \bar{Q}_{\dot{α}}] = +\bar{Q}_{\dot{α}} This means that the R-charge of the scalar ϕ and fermion ψ in a chiral superfield necessarily differ. If the scalar has charge r, then the other members of the multiplet have R[ϕ] = r ⇒ R[ψ] = r−1 and R[F] = r−2 (3.31)

Another way of saying this is to return to the expansion of a chiral superfield (3.19), Φ = ϕ + √2 θ ψ + θ² F + ...

We endow the supercoordinate θ with an R-charge R[θ] = +1 This tallies with our expression (3.11) for the supercharge Q ∼ ∂/∂θ + ... which tells us that Q and θ have opposite charges. The upshot is that if the superfield has R-charge R[Φ] = r, then the other charges in (3.31) follow.

So when do theories enjoy an R-symmetry? Let’s consider the simplest Wess-Zumino model (3.24) for a single chiral superfield. The D-term, which gives the kinetic terms, is clearly invariant under any R-symmetry. That leaves the superpotential. This multiplies d²θ but Grassmann integration acts in the same way as differentiation which means that the measure has charge R[d²θ] = −2 We see that the action is invariant under R-symmetry only if we can assign charges to the superfield such that the superpotential has charge R[W] = +2 (3.32)

When we have just a single superfield Φ, this is rather limiting. It holds only if the superpotential is a monomial W(Φ) = Φⁿ in which case we can assign R[Φ] = 2/n. For example, if we take W(ϕ) = ½ m ϕ² then the Lagrangian has an R-symmetry under which ϕ → e^{iα} ϕ and ψ → ψ. This case is a little boring because there are no interaction terms between ϕ and ψ so obviously we can rotate them independently. We could, however, take W(ϕ) = ⅓ λ ϕ³ in which case we have the Yukawa term ϕ ψ ψ which is invariant under the R-symmetry ϕ → e^{2iα/3} ϕ and ψ → e^{-iα/3} ψ. However, if we include both mass and Yukawa terms, there is no R-symmetry. The surprise, as we will now see, is that the lack of an R-symmetry doesn’t stop it being useful!

3.3.2 The Power of Holomorphy We will now see what the R-symmetry has to do with the non-renormalisation of the superpotential. I should warn you that the argument that follows, originally due to Seiberg, is extremely slick and was developed only after a more nuts and bolts argument using Feynman diagrams had been found. But the symmetry argument is both easier and, ultimately, more powerful.

There are a number of conceptual steps that we need to take before the non-renormalisation theorem becomes clear. These are all related to the parameters that appear in the superpotential, things like the mass m and Yukawa coupling λ in (3.23). Each of these parameters is naturally complex. Moreover, like the chiral superfields themselves, the superpotential must be a holomorphic function of these parameters. Of course, as written in (3.23), the superpotential is, by definition, a holomorphic function of parameters. There’s an m that sits in the first term and a λ in the second and these are complex. However, the point is that any quantum corrections to the superpotential m ust also be holomorphic in parameters. This greatly restrains the allowed quantum corrections.

There are two ways to argue that the superpotential must be holomorphic in parameters. The first is direct, but convoluted, and invokes a kind of supersymmetric Ward identity. The second way is to say a bunch of words that hopefully makes it obvious. We’re going to adopt the second way.

In any quantum field theory, we can view parameters as arising from some fixed, background scalar fields. This means that the parameters may come from some dynamical, but very heavy, scalar field with a potential that pins the value of the scalar to that of the parameter. If this is the case, we wouldn’t notice any difference at low energies because these new fields are so heavy. We would see the fluctuations of the parameter only at high energies.

This idea is realised in our world: in the Standard Model the scale of the masses of all elementary particles is set by the expectation value of the Higgs boson. It’s an idea that is extended dramatically in string theory where all dimensionless parameters of a low-energy theory also arise as the expectation value of some scalar. However, it is a way of thinking that has proven to be useful in many other arenas including, as we will now see, in supersymmetric theories. The new fields that replace the parameters are sometimes called spurions.

This change of perspective from parameters to spurions doesn’t change the low-energy behaviour of the theory. But, remarkably, it does allow us to put constraints on what this low-energy behaviour can be. These constraints are especially strong in supersymmetric theories because the spurion must be the lowest component of a chiral superfield. And, as such, the parameters must appear holomorphically in the superpotential.

To understand what this buys us, let’s return to the simple case of a single chiral superfield with superpotential W_tree = (1/2) m Φ^2 + (1/3) λ Φ^3 (3.33)

We refer to this as the tree-level superpotential. Our goal is to understand how it is changed by quantum corrections.

As we’ve seen above, this theory does not have an R-symmetry. Nonetheless, thinking of the parameters as spurions suggests that we could think of enlarged symmetries under which the parameters also transform. In this larger framework, the theory has two symmetries: one R-symmetry that we call U(1)_R and one global symmetry that commutes with supersymmetry that we call U(1)_F. The charges are: U(1)_R, U(1)_F Φ: 1, 1 m: 0, -2 λ: -1, -3 All components of the superfield have the same charge under U(1)_F, while the charge under U(1)_R tells us how the lowest scalar component of the superfield transforms, with other components given by (3.31). Relatedly, the superpotential is invariant under U(1)_F but has charge +2 under U(1)_R, as in (3.32).

I stress again that neither U(1)_R nor U(1)_F are symmetries of our theory since a true symmetry isn’t allowed to change parameters of the theory. Said another way, non-vanishing charges for m and λ are telling us that these symmetries are explicitly broken. Nonetheless, the spurions give a useful book-keeping device to characterise exactly how the symmetry is broken. Moreover, as we will now see, they also place strong constraints on the quantum corrections to theory.

Any quantum corrections to the superpotential must be consistent with the two symmetries U(1)_R and U(1)_F. Combined with holomorphy, this becomes a very powerful constraint on what can appear. We can form a single, dimensionless combination of superfields that carries no charge at all: this is λΦ/m. (The superfield has the same dimension as a scalar, namely [Φ] = 1. Meanwhile the mass and Yukawa coupling have dimensions [m] = 1 and [λ] = 0.) The only kinds of superpotentials that we can write down consistent with the symmetries are then of the form W_eff = m Φ^2 f(λΦ/m)

Note that holomorphy was key here. In most situations assigning a charge to a complex parameter isn’t particularly restrictive since, say, |λ|^2 carries no charges and so can appear anywhere. But the fact that only holomorphic quantities can appear in the superpotential is a game changer.

We still have an arbitrary function f(λΦ/m) that can appear. But this can be pinned down by studying the theory in different limits. First, for λ ≪ 1, we are in the weakly coupled limit. This means that for small λ we should reproduce the tree level superpotential (3.33), perhaps with corrections at order λ^2 or higher coming from loop diagrams. In other words, the expansion of f(x) about x = 0 must take the form f(x) = 1/2 + (1/3)x + O(x^2)

However, we should also have a well defined superpotential in the limit m → 0 in which we have massless particles. This tells us that we must have f(x) = 1/2 + (1/3)x or, equivalently, W_eff = (1/2) m Φ^2 + (1/3) λ Φ^3 = W_tree This is the result we promised: the superpotential receives no quantum corrections to any order in perturbation theory in λ.

(Looking forward: in Section 6, we will study)

the quantum dynamics of supersymmetric gauge theories. There we will find that superpotentials are, in some circumstances, dynamically generated. But even there they will not be perturbative effects. The superpotentials will arise either by some strong coupling effect or by an instanton effect.)

While the superpotential is immune to quantum corrections, this is not true of the Kähler potential. There are now no holomorphy restrictions and nothing to prohibit corrections of order λ² and higher. This means that the physical masses and Yukawa couplings do, in fact, receive quantum corrections. To see this, note that typically the Kähler potential will pick up quantum correction of the form

K(Φ,Φ†) = Φ†Φ → ZΦ†Φ

where Z = 1 + O(λ²) is sometimes, inappropriately, called the wavefunction renormalisation. This renormalisation factor will have a characteristic logarithmic form

Z = 1 + c|λ|² log |Λ_UV / m|² + ... (3.34)

Here c is a constant whose exact value can be calculated but isn’t of interest for our purposes and ... refers to higher loop corrections. This renormalisation changes the kinetic terms for each of the fields and the action is now

S = ∫ d⁴x d⁴θ (1/2) Z Φ†Φ + ∫ d⁴x d²θ (1/3) (m Φ² + λ Φ³) + h.c.

Importantly, supersymmetry ensures that there is just a single renormalisation Z for the superfield, meaning that each of the component fields ϕ, ψ and F experiences the same Z. In such a situation, we should work with the canonically normalised field Φ̂ = Z^{1/2} Φ and the action becomes

S = ∫ d⁴x d⁴θ (1/2) Φ̂†Φ̂ + ∫ d⁴x d²θ (1/(2Z)) (m Φ̂² + (λ/Z^{3/2}) Φ̂³) + h.c.

In this way, the non-renormalisation of the superpotential is not enough to protect the physical mass and Yukawa coupling, which are m_phys = m/Z and λ_phys = λ/Z^{3/2} respectively.

This may seem like a disappointing end to our non-renormalisation claim: the superpotential doesn’t change, but the physical parameters sitting within it do. Nonetheless, there’s something important going on here. That’s because supersymmetry has ensured that the mass m²_phys picks up only a multiplicative renormalisation.

This contrasts strongly with the mass renormalisation expected of a scalar field in a typical quantum field theory. Typically, this mass renormalisation is additive. In particular, any one of the three diagrams shown in Figure 1 would give a contribution of the form

m²_phys ∼ m²_UV + |λ|² Λ²

This is the statement that quantum fluctuations tend to push the mass of scalar fields up to the cut-off scale. In the absence of fine tuning (or some other explanation like symmetry breaking) scalars in quantum field theory are typically heavy. Yet this doesn’t happen in supersymmetric theories: miraculously, the additive renormalisation cancels between each of the diagrams above. This occurs because, as we have seen, the same coupling λ appears in the Yukawa coupling to the fermions and in the 3-point and 4-point vertices of the scalars. The result is that, in supersymmetric theories, there is no difficulty with the masses of scalars being small. In particular, if we choose to set m = 0 in the superpotential so that the chiral multiplet is massless then quantum corrections do not change this.

This is the key reason that supersymmetry has attracted the interest of phenomenologists. The mass of the Higgs boson is seemingly much lighter than the cut-off scale of the Standard Model, an issue referred to as the hierarchy problem. (See the lectures on Particle Physics for a non-technical account of this.) The existence of supersymmetry at, say, the TeV scale would provide a natural explanation of this. Sadly, there is no evidence that this is the explanation favoured by nature.

3.3.3 Integrating Out Heavy Fields

We may sometimes find ourselves in situations in which our theory has two or more fields with different masses. In this case, we can integrate out the heavier fields, leaving ourselves with an action just for the lighter ones. This will be an important tool for us later, so we pause here to see how it works.

Consider the theory of two chiral superfields Φ and Z, both with canonical Kähler potential K = Φ†Φ + Z†Z, and with superpotential

W = (1/2) M Z² + (1/2) λ Φ² Z (3.35)

In this example, Z is the heavy field with mass M while Φ is massless, but interacts with Z. If we care only about physics at energies E ≪ M, we can simply integrate out Z to leave ourselves with a theory for Φ.

Usually in quantum field theory, integrating out fields requires us to evaluate some complicated functional determinants or Feynman diagrams. But, at the level of the superpotential, things are straightforward. For a field configuration Φ, the heavy field will rapidly arrange itself to minimise its energy which it does by setting the derivative of W with respect to Z to zero.

by adjusting to \frac{\partial W}{\partial Z} = 0 \implies Z = -\frac{\Phi^2}{2M} Substituting this back into the superpotential gives our effective superpotential W = -\frac{\lambda}{8M} \Phi^4

This results in a \(\phi^6\) interaction for the scalar, together with the Yukawa-like interaction for the fermion.

We can also reach the same conclusion by analysing the (spurious) symmetries of the theory. This time there are two global symmetries, \(U(1)\) and \(U(1)\) in addition to the \(R\)-symmetry. The charges of various fields and parameters are

| Field | \(U(1)_R\) | \(U(1)_\Phi\) | \(U(1)_Z\) | | :--- | :---: | :---: | :---: | | \(\Phi\) | 1 | 1 | 0 | | \(Z\) | 0 | 0 | 1 | | \(M\) | 2 | 0 | -2 | | \(\lambda\) | 0 | -2 | -1 |

The unique superpotential consistent with these symmetries that does not involve \(Z\) is \(W \sim \lambda \Phi^4\) (3.36)

This symmetry argument doesn’t give the overall constant \(-1/8\) but, as we’ve seen above, that’s not difficult to get by simply solving the equation of motion.

Note that there’s a different philosophy at play here from when we showed the non-renormalisation of the superpotential (3.33). In the earlier case we insisted that the superpotential was well behaved as \(m \to 0\). However, in the present case the superpotential clearly diverges as \(M \to 0\). But this is to be expected: the theory involving \(\Phi\) alone is only supposed to make sense at energies \(E \ll M\). The fact that the superpotential diverges as \(M \to 0\) is telling us something physical: that we shouldn’t have discarded the field \(Z\) in this limit since it wasn’t heavy. This is a lesson that we will see several times as these lectures progress: our low-energy theory will break down in any limit where some field that we have ignored becomes massless.

There’s also a terminological issue here. Physicists refer to the superpotential (3.36) as “holomorphic” in \(\Phi\), \(\lambda\) and \(M\). Strictly speaking it’s not holomorphic in \(M\), but instead meromorphic because of the pole. As we explained above, the pole certainly has physical consequence, but we won’t belabour the point and will continue to take about holomorphy rather than the more accurate meromorphy.

3.3.4 A Moduli Space of Vacua We can see a twist on this same theme if we study the superpotential (3.35) in the limit \(M = 0\). We have \(W = \lambda \Phi^2 Z\) (3.37)

This theory has a feature that will become increasingly important as these lectures develop: there is not a unique ground state, or even a finite number of isolated ground states. Instead the potential energy is given by \(V(\phi,z) = \left| \frac{\partial W}{\partial \phi} \right|^2 + \left| \frac{\partial W}{\partial z} \right|^2 = |\lambda \phi z|^2 + \frac{1}{4} |\lambda \phi^2|^2\)

We’ve now resorted to our earlier notation of referring to the lowest scalar component of the superfields \(\Phi\) and \(Z\) by the lower case letter \(\phi\) and \(z\) respectively. The minima of the potential are given by \(V(\phi,z) = 0 \iff \phi = 0 \text{ and } z = \text{anything}\)

This means that the potential has a flat direction. Provided that \(\phi = 0\), there is no energy cost to turning on \(z\). We say that there is a moduli space of vacua. In such a situation, the choice of ground state \(z\) is not determined dynamically. Instead, to fully specify the theory, we must also state the expectation value of the field \(z\). Importantly, different choices of \(z\) give rise to different theories. For example, we can see immediately from the potential that the mass of \(\phi\) is \(m = |\lambda z|\). In other words, this is moduli space of inequivalent vacua.

Now the roles of \(z\) and \(\phi\) are reversed! Provided that \(z \neq 0\), the \(\phi\) field is massive while \(z\) is massless. We can again play the kind of game that we saw above: is there a superpotential \(W(Z)\) that we can write down that might arise after \(\Phi\) is integrated out? It’s simple to see that the answer is no. Everywhere along the moduli space, we have \(W(Z) = 0\)

This is important. Had we found \(W(Z) \neq 0\), it would have meant that there was a quantum generated potential that lifts the flat direction and that the true quantum theory has a preferred ground state. But the non-renormalisation theorem tells us that no such potential is generated. Instead we learn that the moduli space of ground states survives in the quantum theory.

The existence of a moduli space of inequivalent vacua is commonplace in supersymmetric theories but never happens in the absence of supersymmetry. In any non-supersymmetric theory, quantum corrections always generate a potential on the would-be moduli space. This is known as the Coleman-Weinberg potential and it picks the true ground state of the system, typically pushing the scalar either to \(z = 0\) or to \(z = \infty\).

We can get some intuition for the Coleman-Weinberg in a simple quantum mechanics example. Suppose that we have a quantum particle that can move in the \((x,y)\) plane but with a potential that we take to be \(V = x^2 y^2\) (toy model)

The classical system has two flat directions: \(x = 0\) and \(y = \text{anything}\); or \(y = 0\) and \(x = \text{anything}\). Suppose that we sit at some \(y \neq 0\) but classically set \(x = 0\). We then look at the quantum system by supposing that \(y\) is constant and quantising the \(x\) degree of freedom. But this is just a quantum harm A quantum oscillator with frequency given by ω = y. And the ground state energy of the quantum harmonic oscillator is E ∼ ℏω = ℏy. In this way, the quantisation of x gives rise to an energy that pushes y back towards the origin. Indeed, this quantum mechanical system has a unique ground state, localised around the origin.

The Coleman-Weinberg potential is the analogous phenomenon in quantum field theory. It is generic but is avoided in supersymmetric theories due to a delicate cancellation between bosons and fermions, very similar to those at play in the loop diagrams in Figure 1. We’ll be meeting many different vacuum moduli spaces as these lectures progress. Indeed, one of the emerging themes of these lectures is that the geometry of these moduli spaces contains important clues to the underlying physics.

For now, let’s go back to our field theory (3.37) and ask: what happens to the moduli space at z = 0? Here the ϕ field also becomes massless and it should no longer be valid to ignore it. But how do we see this if we’re focussed on the dynamics of z alone?

The answer to this can be found in the Kähler potential. Classically, this takes the canonical form K = Z†Z, corresponding to a flat metric ds² = dzdż = ∂²K / ∂z∂ż dzż However, as we saw above, when we integrate out the massive Φ field the Kähler potential receives a one-loop quantum correction (3.34) and becomes K = Z†Z (1 + c|λ|² log |Λ_UV / Z|² + ...)  (3.38)

where |Z| appears in the argument of the logarithm courtesy of the role it plays as the mass of Φ. This results in a metric on the moduli space given by ds² = dzdż = ( -c|λ|² log(zż/Λ²_UV) + constant + ... ) dzż We see that distances diverge as we approach z → 0. The log singularity at z = 0 is the sign that we have attempted to integrate out a massless particle at that point.

Figure 2. The classical moduli space on the left and the quantum corrected moduli space on the right, with its singularity at z = 0 revealing the massless particle and its negative signature at large z showing that the quantum theory is ill-defined.

There is also some strange behaviour for large |z|. When |z| ≫ Λ_UV, the first term is negative and, for large enough |z|, will overwhelm the constant term, giving us a negative metric. This, of course, is nonsensical. It’s telling us that our scalar theory doesn’t make sense at very high expectation values or, equivalently at very high energies. In other words, it is capturing the phenomenon of the Landau pole in ϕ⁴ theory, but now in a novel geometric fashion. A depiction of the classical and quantum moduli spaces is shown in Figure 2.

## 3.4 A First Look at Supersymmetry Breaking

A symmetry is said to be spontaneously broken if it acts non-trivially on the ground state. This means that the Noether charge Q for the symmetry fails to annihilate the vacuum, Q|0⟩ ≠ 0

Broken symmetries have important consequences. If a discrete symmetry is spontaneously broken then it implies the existence of multiple, isolated ground states. If a continuous symmetry is spontaneously broken then it implies the existence of a massless particle called a Goldstone boson. These ideas underlie Landau’s classification of phases of matter and were discussed in some detail in the lectures on Statistical Field Theory and the lectures on Gauge Theory. In this section, we will make a first pass at understanding when supersymmetry may be spontaneously broken and what the consequences are.

First, some basics. From the supersymmetry algebra {Q_α, Q̄_α̇} = 2σ^µ_αα̇ P_µ we can derive an expression for the Hamiltonian H = P₀ = (1/4){Q†₁, Q₁} + (1/4){Q†₂, Q₂}

We already noted in Section 2.2.2 that this implies that all states in a supersymmetric theory necessarily have energy E ≥ 0. This means that any state with E = 0 must be a ground state. These states obey E = ⟨0|H|0⟩ = 0 ⇔ Q_α|0⟩ = 0 In this case the supercharges annihilate the ground state which means that supersymmetry is unbroken. Conversely, supersymmetry is spontaneously broken if and only if the energy of the ground state is non-vanishing E = ⟨0|H|0⟩ > 0 ⇔ Q_α|0⟩ ≠ 0 In other words, the ground state energy E_ground is the order parameter for broken supersymmetry.

There is another way of looking at this. In theories of chiral multiplets (with a canonical Kähler potential) the potential energy is given by (3.29)

V(ϕ, ϕ̄) = Σ_i |F_i|² = Σ_i |∂W/∂ϕ_i|² The ground state energy is non-zero if and only if the F-term gets an expectation value in the vacuum F_i = -∂W†/∂ϕ̄_i ≠ 0 This is known as F-term supersymmetry breaking. (There is another option that involves vector multiplets known as D-term supersymmetry breaking.)

3.4.1 The Goldstino If a normal continuous symmetry is spontaneously broken, it results in a massless particle.

be known as a Goldstone boson. If supersymmetry is spontaneously broken, it results in a massless fermion that we call a Goldstino.

First, some intuition. When a normal, continuous symmetry is spontaneously broken, the symmetry sweeps out a manifold of equivalent ground states. The canonical example is the breaking of a U(1) symmetry that gives rise to the S¹ rim of the Mexican hat potential. The massless Goldstone mode then arises from fluctuations along this flat direction.

Something similar happens for supersymmetry. From the supersymmetry transformations (3.20), we see that when Fi ≠ 0, a supersymmetry transformation acting on the vacuum turns on a linear combination of fermions δψi = 2ϵFi This is the Goldstino.

There is a simple, hands-on way to see the existence of this massless fermion within the class of theories that we’re discussing here. The ground state of the system, whether supersymmetric or not, sits at ∂V/∂ϕi = 0  ⇒  Σj (∂²W/∂ϕi∂ϕj)(∂W†/∂ϕj) = 0 If supersymmetry is broken then Fj ≠ 0 for some j and the equation above then tells us that the matrix ∂²W/∂ϕi∂ϕj necessarily has an eigenvector with vanishing eigenvalue. But ∂²W/∂ϕi∂ϕj is the fermion mass matrix in our theory. So we learn that when supersymmetry is broken there is at least one massless fermion.

There is a more powerful, general approach to show the existence of the Goldstino that holds for the strongly coupled theories that we will discuss later. This is in close analogy to the original proof of Goldstone’s theorem and we just give a bare bones sketch here. The idea is to first construct the supercurrent Sµ. This is the conserved current associated to supersymmetry transformations and, like any other conserved current, obeys ∂µ Sµ = 0. The supercharge Qα arises from this current in the usual way: Qα = ∫d³x S⁰α The supercurrent obeys the algebra {Qα, S̄µα̇} = 2σναα̇ Tµν with Tµν the energy-momentum tensor. This reproduces the usual supersymmetry algebra (2.21) when integrated over space. The proof of the existence of a massless Goldstino then proceeds by computing the two-point function pµ⟨Sα(p)S̄α̇(−p)⟩ = −2σµαα̇ ηµν E₀ with E₀ the ground state energy. This tells us that whenever E₀ ≠ 0 there is a pole in the ⟨SS⟩ 2-point function at p = 0. This pole corresponds to a massless fermion, the Goldstino.

These lectures are very much focussed on more formal aspects of supersymmetry rather than any possible application to our world. Nonetheless, the existence of the Goldstino raises a puzzle. Clearly we don’t see supersymmetry at the energies we have explored so far, which is roughly speaking E ≲ 100 GeV or so. That, in itself, is not such a big issue since it may well be that supersymmetry is broken at some higher energy scale. But, in that case the argument above suggests that we would expect to see a massless Goldstino in our world and no such particle exists. (You might wonder if perhaps the neutrino could act as a Goldstino. This isn’t possible because the Goldstino is created from the vacuum and so should share its quantum numbers, while the neutrino carries electroweak charge.)

The resolution to this lies in supergravity. Recall that supergravity involves a local, or gauged, version of supersymmetry. When a normal gauge symmetry is broken, the would-be massless Goldstone boson is “eaten” by the Higgs mechanism and becomes massive. The same is true of gauged supersymmetry. In the context of supergravity, the would-be Goldstino is eaten by the gravitino and both become massive with mass of order E_{susy}, the supersymmetry breaking scale.

3.4.2 The Witten Index Not all theories can spontaneously break supersymmetry. There is a topological obstruction that they must overcome. This obstruction is the Witten index.

We met the Witten index briefly back in Section 2.3. It defined as the sum over all states Tr(−1)^F e^{−βH}   (3.39)

The trace is taken over the infinite number of states in the quantum field theory Fock space. Here F is the fermion number, so that the Witten index counts bosonic states with a +1 and fermionic states with a −1. In contrast to the discussion in Section 2.3, we’ve now included a factor of e^{−βH}, where H is the Hamiltonian. This acts as a regulator on the very high energy states. But, as we’ll now show, these high energy states don’t in fact contribute to the Witten index.

To make the discussion precise, we should really work on a compact space, like T³. This ensures that momentum is quantised and, correspondingly, the energy spectrum is discrete. There are then no subtleties in taking the trace.

The key fact about the Witten index is that any states with energy E > 0 necessarily come in boson-fermion pairs. This follows from the kind of representation theory that we did in Section 2.3. More precisely, if we define the combination of supercharges Q = Q₁ + Q₂† then, from the supersymmetry algebra (2.21), it is simple to see that these obey {Q, Q†} = H Consider the action of this operator on a state with energy \( H|\phi\rangle = E|\phi\rangle \) with \( E \neq 0 \). We can then define the fermionic creation and annihilation operators \( a = \sqrt{2E} \) such that \( \{a, a^\dagger\} = 1 \). This algebra has a two-dimensional irreducible representation \( |\phi\rangle \) and \( a^\dagger|\phi\rangle \), both with energy \( E \). One of these states is bosonic and the other fermionic, ensuring that they cancel in their contribution to the Witten index.

Note that the degeneracy of \( E > 0 \) states is true whether or not supersymmetry is broken. If supersymmetry is unbroken, it arises because of mass degeneracy of particles in a supermultiplet. If supersymmetry is broken then the degeneracy arises simply from the addition of a zero energy Goldstino mode. (More precisely, on a compact space it arises from the quantisation of the Goldstino zero mode.) In this case, there is no need for the masses of bosonic and fermionic particles to be equal.

This argument for the degeneracy of the spectrum breaks down for states of zero energy. For such supersymmetric ground states there is no obstacle to having just a single state obeying \( Q_\alpha|0\rangle = Q_\alpha^\dagger|0\rangle = 0 \). More generally, it may well be the case that a theory has multiple ground states. In this case, each ground state could be bosonic or fermionic. Here a "fermionic" ground state is nothing exotic: it just means that it sits in the sector of the Hilbert space with \( (-1)^F|0\rangle = -|0\rangle \) rather than \( (-1)^F|0\rangle = +|0\rangle \).

The upshot is that the Witten index (3.39) actually counts the difference in the number of \( E = 0 \) ground states \( \text{Tr}(-1)^F e^{-\beta H} = n_B(E = 0) - n_F(E = 0) \). In particular, the Witten index is independent of the value of \( \beta \). Moreover, it is actually independent of any other parameter in the theory. To see this, consider a generic spectrum of a supersymmetric theory. All \( E \neq 0 \) states come in pairs, while \( E = 0 \) states may be unpaired. As we vary parameters in the theory, some of the \( E = 0 \) ground states may get lifted and get non-zero energy. But they can only be lifted in pairs and the Witten index remains unchanged. In this sense, the Witten index provides a topological classification of theory. (Actually, this last statement is only true providing that asymptotic nature of the potential does not change. We’ll see an example below.)

All of this means that supersymmetry can only be spontaneously broken in theories with \( \text{Tr}(-1)^F = 0 \). In contrast, if \( \text{Tr}(-1)^F \neq 0 \) for some choice of parameters then the theory cannot break supersymmetry as the parameters are changed and this remains true even as the dynamics becomes strongly coupled.

An Example

All of the theories that we will explore in this section are weakly coupled and we can tell whether supersymmetry is broken simply by looking at the potential. This means that we don’t really have any need for the Witten index. It starts to show its teeth only for the strongly interacting theories that we will meet in Section 6. Nonetheless, it’s useful to get a feeling for how supersymmetric ground states are robust.

Consider a Wess-Zumino model with a single chiral superfield \( \Phi \) with a superpotential that is a polynomial of degree \( p+1 \), \( W(\phi) = a_{p+1} \phi^{p+1} + a_p \phi^p + \dots + a_1 \phi \). A supersymmetric ground state exists if there are solutions to the equation \( \frac{\partial W}{\partial \phi} = 0 \) (3.40). But there’s always a solution to this equation because we’re solving a polynomial over the complex numbers. In fact, there are always \( p \) such solutions (counted with multiplicity). As we vary the coefficients \( a \) the ground states move around, but they are never lifted. This reflects the fact that this theory has \( \text{Tr}(-1)^F e^{-\beta H} = p \). It’s a little fiddly to show that all ground states contribute the same \( +1 \) to the Witten index, rather than with different signs. You can find the argument in the lectures on Supersymmetric Quantum Mechanics where the Witten index plays a central role throughout.

There is, however, an important caveat to the statement that the theory always has \( p \) ground states. If we set \( a_{p+1} = 0 \) then the superpotential becomes a polynomial of degree \( p \) and the theory has \( p-1 \) ground states. It’s simple to see what happens here: as we take the limit \( a_{p+1} \to 0 \), one of the ground states starts heading off to infinity in field space \( \phi \to \infty \). This provides a salutary lesson: the Witten index can change if we change how the theory behaves in the asymptotic region of field space. We will see other examples below where, as we vary parameters, a moduli space of ground states emerges then disappears again. This also provides a scenario where the Witten index can jump.

3.4.3 The O’Raifeartaigh Model

The Witten index argument, together with some basics facts about roots of polynomials, means that you have to strive e to write down theories that break supersymmetry. Nonetheless, it’s not too difficult to achieve. The first model was constructed in 1975 by O’Raifeartaigh. It contains three chiral superfields that we call Y, Z and Φ with the superpotential W = Y(Φ^2 − µ^2) + mZΦ (3.41)

We take all fields to have a canonical Kähler potential so the theory is renormalisable. (We will relax this assumption below.) The parameter h is dimensionless, while [µ] = [m] = 1. It’s useful to note that the potential has an R-symmetry (a real one, not a spurious one) under which R[Y] = R[Z] = 2 and R[Φ] = 0.

The fields Y and Z act like Lagrange multipliers in the superpotential, setting ∂W/∂Y = h(Φ^2 − µ^2) = 0 and ∂W/∂Z = mΦ = 0 Clearly there’s no way to set both of these to zero so supersymmetry is spontaneously broken.

The potential of this model is given by V(y,z,ϕ) = (1/2) |hϕ^2 − hµ^2|^2 + |mϕ|^2 + |hyϕ + mz|^2 Note that y and z are just names of scalar fields here; they are not to be confused with coordinates on spacetime. The minima of the potential always sits at z = −hyϕ/m so the final term vanishes. What happens next depends on the ratio of parameters α = |hµ| / |m| If α < 1 then the minima is at ϕ = z = 0. If α > 1 then this minima splits into two minima at ϕ = ±something and a saddle. Importantly, in either case y is arbitrary: it is a flat direction.

It is simple to check that the whole superfield Y is massless. The fermion is the Goldstino while the phase of y is a Goldstone boson associated to a broken R-symmetry. The surprise is that |y| is also massless, with no symmetry reason to protect it. As we now explain, the classical moduli space parameterised by |y| doesn’t survive in the full quantum theory.

The Quantum Generated Potential Importantly, the mass spectrum of the O’Raifeartaigh model depends on the value of |y|: each point on this moduli space describes different physics. Furthermore, and in contrast to our earlier supersymmetric models, the masses of the bosons and fermions are different. This is important because it means that when we integrate out these heavy fields they will induce a Coleman-Weinberg potential on the moduli space parameterised by |y|. Here we give some general comments on the form of this potential.

Integrating out heavy fields in a 4d quantum field theory usually give three kinds of divergences: quartic, quadratic and logarithmic. In each case, bosons give rise to a positive potential and fermions a negative potential. In a supersymmetric theory, these exactly cancel which is the reason that moduli space of vacua are not lifted when supersymmetry is broken. As we now explain, when supersymmetry is spontaneously broken some, but not all, of this cancellation remains.

First the quartic divergences. These are given by V ∼ Str Λ_UV^4 where Λ_UV is the UV cut-off and Str is the supertrace which means that we sum over all complex bosonic fields minus the sum over all fermionic fields. (Note that we’re summing over the different fields of the theory here. This contrasts with the Witten index where we were performing the much larger sum over all states in the Hilbert space.) But supersymmetric theories have an equal number of bosonic and fermionic fields so all quartic divergences disappear regardless of whether supersymmetry is spontaneously broken or not.

Next up are the quadratic divergences. These take the form V ∼ Λ_UV^2 Str M^2 = Λ_UV^2 (Tr M_B^2 − Tr M_F^2)

Here M is the tree-level mass matrix, including both bosons and fermions. In the second equality we’ve written it in terms of a sum over bosonic and fermionic fields with their appropriate mass matrices M_B and M_F. Clearly this too vanishes when there is a degeneracy of masses. But a rather nice result says that it also vanishes when supersymmetry is spontaneously broken: Claim: Str M^2 = 0 for F-term supersymmetry breaking.

Proof: This holds generally in any theory with N superfields and a canonical Kähler potential. The proof involves just a little bit of algebra. First, the N × N mass matrix for a Weyl fermion is (M_F)_{ij} = ∂^2W/(∂ϕ_i ∂ϕ_j)

We write this in terms of the auxiliary field F̄_i = −∂W/∂ϕ_i as (M_F)_{ij} = −F̄_i,j. The mass-squared matrix that appears in the supertrace formula is the Hermitian matrix (M_F)^2 = M_F M_F^† = F̄_{i,j} F̄_{j,k}^* Meanwhile, we have to be a little more careful with the bosons because after supersymmetry breaking the real and complex parts of the scalar will typically have different mass. (This happens, for example, in the O’Raifeartaigh Model.) This means that we should break the bosons into real and imaginary pieces and consider the 2N × 2N mass matrix M_B^2 = [ ∂^2V/(∂ϕ_i ∂ϕ_j^*) ∂^2V/(∂ϕ_i ∂ϕ_l) ; ∂^2V/(∂ϕ_j^* ∂ϕ_k^*) ∂^2V/(∂ϕ_j^* ∂ϕ_l) ]

But V = F_i F̄_i. Plugging this expression into M_B^2 above and taking the trace (remembering that there’s a factor of 1 because we’re now working with real fields rather than complex)

gives the claimed result. □ All of which means that in a theory with spontaneously broken supersymmetry, the only contribution to the effective potential comes from the logarithmic divergences. It can be shown that these too take the form a supertrace over the mass matrix V = StrM⁴log (Λ²_UV / 64π²)

Again, this vanishes if supersymmetry is unbroken. But now it does not vanish if supersymmetry is spontaneously broken. This gives the quantum potential that lifts flat directions in this case.

The mass matrix M depends on the value of the field y, and hence V_eff should be viewed as a potential that lifts this flat direction. In any theory with a flat direction, quantum generated potentials typically push the field to one end or another. Computing the masses shows that here the true ground state of the system sits at y = 0. This is the unique ground state with spontaneously broken supersymmetry.

3.4.4 R-symmetry and the Nelson-Seiberg Argument We could continue exploring different models (and we will below!) but it is useful to first stop and try to understand some general features of supersymmetry breaking. To this end, let’s first look at a small extension of the O’Raifeartaigh model, W = Y(Φ₂² − μ²) + mZΦ₁ + h/2 Φ₁² + ν/2 Φ₂²  (3.42)

This differs from the O’Raifeartaigh model by the addition of the last two terms. Note that these two terms break the R-symmetry and this will be important shortly. For now, we can simply study the scalar potential arising from this superpotential. It is V(y, z, ϕ) = 1/2 |hϕ² − hμ² + 2ϵy|² + |mϕ|² + |hyϕ + mz + νϕ|² Now the theory does have a supersymmetric ground state, sitting at z = ϕ = 0 and y = hμ²/(2ϵ).

If, however, we now take ϵ → 0 to remove the last term in (3.42), then the supersymmetric vacuum moves off to infinity in field space y → ∞ and we once again find ourselves with a theory that breaks supersymmetry, one that appears to be very similar to the original O’Raifeartaigh model. However, in one way there is a key difference between them. To describe this difference we first need to explain what it means for theories to be “generic”.

All the theories we’re discussing in this section should be viewed as low-energy effective theories, coming from some unknown UV physics. But there is a mantra that can be applied to such low-energy theories: anything that is not forbidden is mandatory. This means that quantum effects will conspire to generate all possible terms in the potential provided that they are consistent with the symmetries of the theory. A low energy effective theory that includes all such terms, with no particular fine tuning of the coefficients, will be said to be “generic”.

In this sense, the O’Raifeartaigh model (3.41) is generic. It has an R-symmetry and there are no further terms that one can add consistent with this symmetry.

In contrast, the extension of the O’Raifeartaigh model (3.42) is not generic. It no longer has an R-symmetry, but we have not included Z² terms nor Φ³ terms nor many other terms that we could write down. Despite this, it turns out that the behaviour we have seen – namely the existence of a supersymmetric ground state – persists if we add all these extra terms. So it is sufficient for our discussion.

However, among this large class of theories that do not have an R-symmetry, we only find one that breaks supersymmetry if we set one of the coefficients to vanish: ϵ = 0. This is a very particular choice of coefficient. If the theory (3.42) arose as the low-energy limit of some other theory — one which itself did not have an R-symmetry — then there would be no reason to expect that ϵ = 0. For this reason, it’s unlikely that the supersymmetry breaking we’ve found in this model is actually useful.

In fact, one can make these kind of arguments more generally. Consider a theory with N chiral superfields Φᵢ and a potential W(ϕ). A supersymmetric ground state obeys ∂W/∂ϕᵢ = 0  (3.43)

Supersymmetry is broken if we can cook up a superpotential for which there are no solutions to this equation. But these are N equations in N variables and for a generic W they always have a solution. That means that a supersymmetric ground state can always be found.

It is, however, appropriate to restrict W by symmetry arguments and we might wonder if that will help us find a generic W that breaks supersymmetry. For example, suppose that W is invariant under a U(1) global symmetry under which the superfield Φᵢ transforms with charge qᵢ, Φᵢ → e^{iαqᵢ} Φᵢ In this case the superpotential can always be written as a function of W = W(Xᵢ) with Xᵢ the invariant ratios Xᵢ = Φᵢ/Φ₁^{qᵢ/q₁} = 2,...,N But now the conditions for a supersymmetric ground state are just ∂W/∂Xᵢ = 0 for i = 2,...,N which are N − 1 conditions for N − 1 variables. Again, for a generic W there will be a solution. We see that imposing global symmetries doesn’t help us in finding supersymmetry breaking potentials.

However, the story is different if there is an R-symmetr We take the superfields to transform with charges $r_i$, $$ \Phi_i \to e^{i\alpha r_i} \Phi_i.

$$ We again form the invariant ratios $$ \tilde{X}_i = \frac{\Phi_i^{r_1}}{\Phi_1^{r_i}}, \quad i=2,\dots,N.

$$ The key difference is that the superpotential must have R-charge $+2$. This means that it takes the form $$ W(\Phi_1, \tilde{X}_i) = \frac{\Phi_2^2}{r_1} \tilde{W}(\tilde{X}_i).

$$ The conditions for a supersymmetric ground state are now $\partial W/\partial \tilde{X}_i = 0$. But, as long as $\Phi_2^2/r_1 \neq 0$, we must also have $\tilde{W}(\tilde{X}_i) = 0$. This is now $N$ conditions on $N-1$ variables $\tilde{X}_i$ and generically there will not be a solution.

This is the Nelson-Seiberg argument. It says that models of supersymmetry breaking with generic superpotentials should have an R-symmetry. This is indeed true of the O’Raifeartaigh model.

Our main interest in these lectures is not to construct realistic supersymmetric theories, but rather to explore the strong coupling dynamics of quantum field theories. Nonetheless, it’s worth mentioning that the argument for the existence of an R-symmetry causes something of a headache if you’re trying to build realistic models in which supersymmetry is spontaneously broken. In some models, like the O’Raifeartaigh model, the non-supersymmetric ground state preserves the R-symmetry (recall that, ultimately, the quantum potential pushes us to $y = 0$). But this causes problems further down the line because, as we will see in Section 4, an R-symmetry prohibits masses for the superpartners of gauge fields, known as gauginos. But these must be heavy in any realistic theory.

Alternatively, we could cook up models in which both supersymmetry and the R-symmetry are spontaneously broken. But this then leads to a light Goldstone boson known as the R-axion. Again, we must find a way to give this a mass.

### 3.4.5 More Ways to (Not) Break Supersymmetry

In the remainder of this section, we briefly discuss a number of other simple models that illustrate different ways in which supersymmetry can be broken.

#### Runaway Potentials

Here is a model that looks like it breaks supersymmetry but, on closer inspection, does something different. It consists of two fields, $Z$ and $\Phi$, with superpotential $$ W = Z\Phi^2 - \lambda \Phi $$ It has an R-symmetry with $R[\Phi] = 2$ and $R[Z] = -2$ and a scalar potential given by $$ V = |h\phi^2|^2 + |hz\phi - \lambda|^2 $$ Clearly there is no way to set both terms to zero so we seem to again have a situation in which supersymmetry is broken. However, instead something slightly different is happening and the potential slopes to zero asymptotically. To see this, look at the direction with $\phi = \lambda / (hz)$ for which the potential is given by $$ V(z) = \left| \frac{\lambda^2}{2hz^2} \right| $$ Clearly $V(z) \to 0$ as $z \to \infty$. So it is better to say that this theory has no stable ground state at all: the field is pushed to $z \to \infty$ where supersymmetry is restored. We will see behaviour like this emerging dynamically in Section 6.

#### Metastable Supersymmetry Breaking

Let’s now consider a slightly different variant of the model (3.42) that breaks R-symmetry. We take the superpotential $$ W = Y(\Phi^2 - \mu^2) + m Z \Phi + \frac{\epsilon}{2} Z^2 $$ The potential is $$ V(y,z,\phi) = \frac{1}{2} \left| h\phi^2 - h\mu^2 \right|^2 + |m\phi + \epsilon z|^2 + |hy\phi + mz|^2 $$ This breaks R-symmetry and so, on general grounds, we might expect it to have a supersymmetric vacuum (provided that we have taken the superpotential to be suitably generic). This is indeed the case: the supersymmetric ground state is given by $\phi^2 = \mu^2$, $z = -m\phi/\epsilon$, and $y = m^2/(h\epsilon)$.

For $\epsilon$ very small, this ground state sits a long way from the origin of field space. Moreover, if we look close to the origin, $y = 0$, then the potential is very similar to the original O’Raifeartaigh model. In particular, when $\phi = z = 0$ there is a flat direction along $y$, albeit one that is not a global minimum of the potential. When we include quantum corrections, this will be lifted and, for suitable values of the parameters, we will find a local, supersymmetry breaking vacuum at the origin. A schematic sketch of this situation is shown in Figure 4.

Figure 4. A schematic sketch of the metastable minima at $y = 0$ that breaks supersymmetry and the global, supersymmetric ground state at $y \sim 1/\epsilon$. (The actual potential should be plotted in higher dimensions.)

In a quantum field theory, any local minima of a potential that is not the global minimum is a metastable state, with a finite lifetime. This means that if we initially sit in the supersymmetry breaking minimum, we will eventually tunnel out into the supersymmetric ground state. Nonetheless, it is possible to use such metastable minima to build phenomenologically viable models. You just need to make sure that “eventually” $\gg 100$ billion years (or whatever allows you to sleep easy at night).

#### Playing with the Kähler Potential

So far we haven’t discussed the simplest theory that breaks supersymmetry. This is a single chiral multiplet with superpotential $$ W = \mu^2 \Phi $$ Clearly $\partial W/\partial \phi = \mu^2 \neq 0$. But this feels too cheap. The ground state energy may be non-zero, but the theory is just a free massless fermion (the Goldstino!) and a free complex scalar. It’s hard to argue that there’s any deep physics in there.

Things change however if we consider a more general Kähler potential K = K(ϕ†ϕ). The fermion remains massless but a potential is now generated for the scalar, given by V(ϕ) = |µ|4 (∂2K / ∂ϕ∂ϕ†)−1 The price that we pay is that the theory is no longer renormalisable. Of course, as we’ve stressed above, given that we view these scalar field theory as low energy effective theories, that is not necessarily a bad thing.

For example, suppose that, when expanded around the origin, the Kähler potential takes the form K(ϕ,ϕ†) = |ϕ|2 − |ϕ|4 / M2 +...

This kind of behaviour can arise from integrating out heavy particles of mass M. (We found a log correction to the Kähler potential from integrating out particles in (3.38), but other interactions can give the power-law above.) We should view M as the UV cut-off of the theory. Other energy scales in the game should necessarily be much smaller than the cut-off which, for us, means µ ≪ M.

With such a Kähler potential, the actual potential energy reads V(ϕ,ϕ†) = |µ|4 (1+ |ϕ|2 / M2 +...)

This now has a minima at ϕ = 0. The net result is that the scalar ϕ has a mass m = 2µ2/M2.

A comment on the scales here. As we’ve mentioned repeatedly, all the theories in this section should be viewed as low-energy effective theories arising from some high energy completion. In the present case, our theory is valid at energy scales ∼ µ. We have integrated out stuff at the much higher scale M ≫ µ and this is what gives rise to the correction to the Kähler potential. It’s necessary that there is a separation of scales here. Although the scalar ϕ is not massless, it is light in the sense that 2µ2/M ≪ µ.

Different Kähler potentials can give the different kinds of behaviour that we saw above, including runaway potentials and metastable vacua.

4 Supersymmetric Gauge Theories Finally, we turn to the main subject of these lectures: supersymmetric gauge theory. In this section we will describe the classical structure of supersymmetric gauge theories. In Section 6 we turn to their quantum dynamics.

## 4.1 Abelian Gauge Theories

A gauge field A sits inside a real superfield satisfying V(x,θ,θ ) = V†(x,θ,θ ). Expanding out such a superfield in components, we have V(x,θ,θ ) = C(x)+θχ(x)+θ χ¯(x)+iθ2M(x)−iθ 2M†(x)+θσµθ A (x)

+ (i/2) (θ2θ λ¯ (x)+ σ¯µ∂ χ(x)) +(i/2) (θ 2θ λ(x)+ σµ∂ χ¯(x))

µ µ + (1/2) (θ2θ 2 D(x)− □C(x)) (4.1)

The real superfield contains two real scalars, C and D, and a complex scalar M, together with two Weyl fermions χ and λ . Importantly, it also contains a real vector field A . This will play the role of the gauge field in what follows. We’ve defined some of the components to include derivatives of others. This should simply be thought of as a redefinition of D(x) and λ(x), admittedly one that you wouldn’t write down unless you had an inkling of what was coming.

If A is to be a gauge field, then it must enjoy a gauge transformation. These too sit in a superfield. We start by taking a chiral superfield Ω Ω = ω + (√2)θρ+θ2G+iθσµθ ∂ ω − (1/√2) θ2∂ ρσµθ − (1/4)θ2θ 2□ω µ µ Then i(Ω−Ω†) is a real superfield. Consider the generalised gauge transformation V → V +i(Ω−Ω†) (4.2)

The vector component of the real superfield shifts as A → A −2∂ (Reω) := A +∂ α (4.3)

µ µ µ µ µ But this is precisely the form of a gauge transformation. But under this generalised gauge transformation, it’s not just A that shifts. The other fields in V(x,θ,θ) also transform as C → C −2Imω χ → χ+ 2iρ (4.4)

M → M +G Importantly, however, λ → λ and D → D remain unchanged. This can be traced to the extra derivative terms that we included in the superfield expansion (4.1) which were designed to soak up the shift by a chiral superfield.

We can now use this gauge transformation to simply set C = χ = M = 0. This is known as Wess-Zumino gauge. Note that it’s not a gauge choice that has done anything to fix A . It’s more a “super gauge choice” to fix the extraneous components in the superfield. In Wess-Zumino gauge, the superfield takes the simpler form V WZ = θσµθ A +θ2θ λ¯ +θ 2θλ+ (1/2)θ2θ 2D (4.5)

µ It contains a gauge field A , a Weyl fermion λ and an extra real scalar D that, as the top component of a superfield, will prove to be auxiliary. If we quantise A and λ then we find the single-particle excitations of the gauge multiplet that we anticipated in Section 2.3.2.

If you act with a supersymmetry transformation on V WZ, then it will take you out of Wess-Zumino gauge. This isn’t a big headache; it just means that you have to do a compensating transformation to put yourself back in Wess-Zumino gauge afterwards. The supersymmetry transformations then act on the fields A , λ and D as δA = ϵσ λ+λσ ϵ¯ µ µ µ δλ = ϵD+(σµνϵ)F (4.6)

µν δD = iϵσµ∂ λ¯ −i∂ λσ¯µϵ¯ µ µ Note that the supersymmetry transformations (3.15) alone give us a term proportional to ∂ A in δλ。补偿规范变换使我们回到Wess-Zumino规范会添加另一项，因此它变成规范不变的场强 F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu 最后，注意 V2 = θ^2\bar{\theta}^2 A_\mu A^\mu 和 V3 = 0 (4.7)

WZ 2 µ WZ 这在稍后构建超对称作用量时将很有用。

4.1.1 场强与作用量我们将从场强超场构建作用量，该超场由V构造而来： W_α = - \bar{D}^2 D_α 它有一些很好的性质。首先，它是一个手征超场，满足 D_α W_β = 0。这源于 D_β^3 = 0 的事实。其次，它在超场规范对称性(4.2)下不变：Ω†项立即被 D_α Ω† = 0 消除，而两个 \bar{D} 协力消除了Ω项。（你需要一个 \bar{D} 来越过 D，另一个 \bar{D} 来消除Ω。）其结果是，任何由W构成的作用量都将是规范不变的。

接下来，我们计算W的分量。这是一个直接的计算，但涉及的项数相当多。幸运的是，如果我们认识到W是一个手征超场，事情会变得更容易，因为这意味着我们只需要考虑θ项，而\bar{\theta}项则从展开式(3.19)自动得出。在分量形式中，场强超场为 W_α (x,θ) = λ_α (x)+θ^\beta D_α(x)+(σ_{\mu\nu}θ^\alpha)F^{\mu\nu}(x)‑iθ^2σ_μ\partial^\mu\bar{\lambda}^{\dot{α}}(x)+...

该手征超场W的第一个分量是一个旋量，而不是标量，这反映了W本身是一个旋量手征超场。重要的是，W包含场强 F_{\mu\nu}。

由于W是手征的，我们可以对它在超空间的一半上进行积分，得到超对称作用量。我们有 ∫ d^2θ W_α W^α = - \frac{1}{2} F_{\mu\nu}F^{\mu\nu} + \frac{1}{2} F_{\mu\nu}\star{F}^{\mu\nu} -2iλσ^\mu\partial_\mu\bar{λ} +\frac{1}{2}D^2 其中第二项涉及对偶场强 \star{F}_{\mu\nu} = \epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma} 这类似于 F_{\mu\nu}，但电场和磁场互换（其中一个带负号）。

项 iF_{\mu\nu}\star{F}^{\mu\nu} 是虚数，因此，乍一看，当加上厄米共轭 ∫ d^2\bar{\theta} \bar{W}_{\dot{α}}\bar{W}^{\dot{α}} 时，它似乎会抵消。然而，事实证明这项起着重要作用（至少在我们即将讨论的非阿贝尔理论中是这样），我们希望保留它。这是通过引入规范耦合常数 e^2 来实现的。因为这个耦合常数位于F项中，它必然是复数。我们定义 τ = \frac{\vartheta}{2π} + \frac{4πi}{e^2} 然后写出拉格朗日量 S_{\text{Maxwell}} = - ∫ d^4x \left[ ∫ \frac{iτ}{16π} d^2θ W_α W^α + \text{h.c.} \right]

= ∫ d^4x \left[ - \frac{1}{4e^2} F_{\mu\nu}F^{\mu\nu} + \frac{\vartheta}{32π^2} F_{\mu\nu}\star{F}^{\mu\nu} - \frac{i}{e^2} λσ^\mu\partial_\mu\bar{λ} + \frac{1}{2e^2}D^2 \right] (4.8)

这就是超对称麦克斯韦作用量。其传播的自由度是 U(1) 规范场和一个费米子 λ，在此背景下被称为超对称规范粒子（gaugino），或更具体地说，光微子（photino）。还有一个实的辅助场 D。

参数 e^2 是耦合常数。它在自由的麦克斯韦理论中不起任何作用，但在我们添加物质时将发挥作用。注意，我们采用的是 Maxwell 作用量前面有一个 1/e^2 因子的约定。正如我们将看到的，规范耦合随后不会出现在其他任何地方。这与我们首次在量子场论中遇到的约定不同，后者 Maxwell 项是正则归一化的，但协变导数内有一个规范耦合。两种约定通过重标度 A_μ → e A_μ 相关联。注意，光微子 λ 同样具有一个非常规归一化的动能项，带有 1/e^2。

最后，还有参数 ϑ。这被称为θ角。（我们使用了书法体 ϑ 以区别于超空间坐标 θ。）在经典层面上，θ角不起任何作用。因为它乘以一个全导数项 F_{\mu\nu}\star{F}^{\mu\nu} = 2\partial_\mu(\epsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma)

然而，在量子理论中，事情更有趣，在路径积分中加入此类拓扑项可以影响动力学。对于麦克斯韦理论，这是相当微妙的，但它构成了三维拓扑绝缘体故事的基础。这种效应在杨-米尔斯理论中更为显著，我们将在第6节进一步讨论。你可以在规范理论的讲座中阅读更多关于θ角的内容。

4.1.2 超对称量子电动力学接下来我们添加物质。它们以手征多重态 Φ_i 的形式出现，其中 i = 1,...,N。

我们希望它们在 U(1) 规范场下带电，因此在一个规范变换下 A_μ → A_μ + \partial_μ α 手征多重态的分量以电荷 q_i ∈ \mathbb{Z} 进行变换。这意味着最低分量变换为 ϕ_i → e^{iα q_i} ϕ_i (4.9)

出于必要性，手征多重态 Φ_i 中的费米子 ψ_i 和辅助场 F_i 必须具有相同的电荷， ψ_i → e^{iα q_i} ψ_i 和 F_i → e^{iα q_i} F_i (4.10)

由(4.3)，这个规范变换包含在一个更大的超场变换中，在该变换下 Φ_i → exp(-2i q_i Ω) Φ_i 注意，这实际上包含了比(4.9)和(4.10)更大的对称性，因为我们可以有，例如 ϕ_i → e^{iα q_i} ϕ_i，其中 α ∈ \mathbb{C}，而非 \mathbb{R}。这平移了...

模量 ϕ 的模和相位。用数学语言说，规范群已经从 U(1) 扩展到了其复化 U(1)_C。然而，这额外的部分也改变了向量多重态中的附加场，特别是场 C，其变换为 C → C + Im α，如式 (4.4) 所示。这意味着，如果我们利用这个额外的变换去到 Wess-Zumino 规范（令 C = 0），那么我们就不能再用它来变换 ϕ 了，于是我们又回到了更熟悉的 U(1) 规范变换，其中 α ∈ R。

我们到目前为止使用的正则 Kähler 势不是规范不变的： ∑_i Φ_i† Φ_i → ∑_i exp[ -2iq_i (Ω - Ω†) ] Φ_i Φ_i†。

不过，修正起来很简单。我们只需要使用新的 Kähler 势 K(Φ, Φ†, V) = ∑_i Φ_i† e^{2q_i V} Φ_i， 其中 V 的变换如式 (4.2) 所示，这使得整个表达式是规范不变的。在 Wess-Zumino 规范下，式 (4.7) 截断为 e^{2qV} = 1 + 2qV + q²V²。

在超空间上积分后得到： ∫ d⁴θ Φ_i† e^{2q_i V} Φ_i = ∫ d⁴x [ |D_μ ϕ_i|² - i ψ_i† σ̄^μ D_μ ψ_i + |F_i|² - 2q_i ( ϕ_i λ̄ ψ̄_i + ϕ_i† λ ψ_i ) + q_i D |ϕ_i|² ]。

这里的协变导数由下式给出： D_μ ϕ_i = ∂_μ ϕ_i - i q_i A_μ ϕ_i，以及 D_μ ψ_i = ∂_μ ψ_i - i q_i A_μ ψ_i。

那么，一个阿贝尔规范理论的完整作用量来自将麦克斯韦作用量 (4.8) 与物质场结合。它是 S = S_Maxwell + ∑_i ∫ d⁴x ∫ d⁴θ Φ_i† e^{2q_i V} Φ_i = ∫ d⁴x { - (1/(4e²)) F_μν F^μν + (ϑ/(32π²)) F_μν ⋆F^μν - (i/e²) λ σ^μ ∂_μ λ̄ + ∑_i [ |D_μ ϕ_i|² - i ψ_i† σ̄^μ D_μ ψ_i ] + (1/(2e²)) D² + ∑_i [ |F_i|² - 2q_i ( ϕ_i λ̄ ψ̄_i + ϕ_i† λ ψ_i ) + q_i D |ϕ_i|² ] }。

第一行包含动能项，第二行包含相互作用。注意，这里存在规范微子 λ 与手征多重态场之间的汤川耦合，其中 ϕ_i† 与 ψ_i 配对使得汤川项是规范不变的。此外，当我们积掉辅助场时会出现一个标量势。除非我们也添加一个超势，否则 F 项不起作用，而积掉 D 项则得到势： V(ϕ) = (1/(2e²)) D²，其中 D = ∑_i e² q_i |ϕ_i|²。

只要电荷 q_i 中有正有负（如我们下面将解释的，必须如此），该势就具有平坦方向，满足： ∑_i q_i |ϕ_i|² = 0。

真空模空间的存在是超对称规范理论的一个重要特征。我们将在 4.3 节更详细地研究它。

**初步探讨反常** 式 (4.11) 作为一个经典理论没有问题。但是，作为一个量子理论，它存在问题。事实证明，对于大多数电荷 q_i 的选择，这个量子理论是病态的。它存在一种不一致性，称为规范反常。

我们将在本讲座后面详细讨论反常，包括规范反常和其他反常。现在我们只提及，量子理论只有在电荷满足以下两个条件时才有意义： ∑_i q_i = 0，且 ∑_i q_i³ = 0。

这些条件并非超对称理论所特有。它们对任何具有与 U(1) 规范群耦合的外尔费米子的理论都成立。我们将在 5.2 节进一步说明这些条件的来源。现在，请注意它们要求我们既有正电荷也有负电荷的场，而这反过来确保了方程 (4.13) 存在 ϕ_i ≠ 0 的解。

一致性条件 (4.14) 存在非平凡解，但在大部分情况下，我们将使用平凡解，即手征多重态成对出现，使得对于每个电荷为 q_i 的 Φ_i，存在第二个我们称为 Φ̃_i 的手征多重态，其电荷为 -q_i。那么条件 (4.14) 就自动满足了。每一对 Φ_i 和 Φ̃_i 有时被称为一个“味”。如果说一个味具有电荷 q，那么意味着 Φ_i 的电荷为 q，而 Φ̃_i 的电荷为 -q。

最简单的例子是一个 U(1) 规范场与 N 个味（这意味着 2N 个手征多重态）相互作用，每个味的电荷为 +1。这个理论称为超对称 QED，或简称为 SQED。其作用量为 S_SQED = S_Maxwell + ∑_i ∫ d⁴x ∫ d⁴θ [ Φ_i† e^{2iV} Φ_i + Φ̃_i† e^{-2iV} Φ̃_i ]

= ∫ d⁴x { - (1/(4e²)) F_μν F^μν + (ϑ/(32π²)) F_μν ⋆F^μν - (i/e²) λ σ^μ ∂_μ λ̄ + ∑_i [ |D_μ ϕ_i|² + |D_μ ϕ̃_i|² - i ψ_i† σ̄^μ D_μ ψ_i - i ψ̃_i† σ̄^μ D_μ ψ̃_i ]

- [ √2 ∑_i ( ϕ_i† λ ψ_i - ϕ̃_i† λ ψ̃_i ) + h.c. ] - (e²/2) [ ∑_i ( |ϕ_i|² - |ϕ̃_i|² ) ]² }。

在这里，我们已经积掉了 D 项和 F 项，因此标量势具有式 (4.21) 的形式。

当我们在量子场论讲座中首次接触 QED 时，我们将一个狄拉克费米子与一个 U(1) 规范场耦合。这个狄拉克费米子包含两个手征费米子，一个是左手的 ψ，一个是右手的 χ̄，它们具有相同的电荷。如果我们对右手费米子取共轭，它就变成了一个左手的费米子 χ。现在我们有了两个左手的费米子 ψ 和 χ。

ions with equal and opposite charges. That’s precisely the fermionic matter content in each flavour in (4.15).

Adding Further Terms

There are further terms that we can add to the action (4.15) (or, indeed, to the more general action (4.11)). We can add any superpotential W(Φ) provided that it is gauge invariant. For example, we can always add to (4.15) the superpotential \[ \tilde{W}(\Phi, \tilde{\Phi}) = \sum_i m_i \Phi_i \tilde{\Phi}_i \]

This gives a mass \(|m_i|\) to each chiral multiplet. In particular, the fermions get a Dirac mass. Note that such mass terms are only possible if there are pairs of chiral superfields with opposite charges.

There is one further, slightly curious term that we can add. This is known as the Fayet-Iliopoulos term, \[ \mathcal{L}_{\text{FI}} = \int d^4\theta\, 2\zeta V = \zeta D \tag{4.16} \]

It is gauge invariant because D doesn’t shift under the generalised gauge symmetry (4.2). Here \(\zeta \in \mathbb{R}\) is the Fayet-Iliopoulos, or FI, parameter. Since this multiplies the D-term, it changes only the scalar potential (4.12) which becomes \[ V(\phi) = \frac{e^2}{2} \left( \sum_i q_i |\phi_i|^2 - \zeta \right)^2 \]

In particular, supersymmetric vacua with \(V(\phi) = 0\) now require some scalar field to get a non-vanishing expectation value which, in turn, breaks the \(U(1)\) gauge symmetry.

## 4.2 Non-Abelian Gauge Theories

We can repeat everything above for non-Abelian gauge fields. We work with a gauge group \(G\) with Lie algebra \[ [T_A, T_B] = i f_{ABC} T_C \]

The factor of \(i\) in the commutation relations ensures that the generators are Hermitian, so \((T_A)^\dagger = T_A\). We normalise the generators in the fundamental (i.e. minimal) representation as \[ \text{Tr} T_A T_B = \delta_{AB} \tag{4.17} \]

In what follows, generators \(T_A\) will always be taken to be in the fundamental representation. If we need generators in other representations \(R\) then we will denote them as \(T_A\). In these lectures we will mostly work with \[ G = SU(N)

\]

with the subscript on \(N\) short for the number of “colours”. We’ll also mention results for other gauge groups as we go and, for now, keep things general.

4.2.1 Super Yang-Mills

Constructing supersymmetric Yang-Mills theory is a slightly more fiddly version of what we did for Maxwell theory. We introduce a real superfield \(V\) in the adjoint of the gauge group. As usual, we can view an object in the adjoint representation as living in the Lie algebra by writing \[ V = V^A T_A, \quad A = 1,\dots,\text{dim}G \]

For \(G = SU(N)\), if we take \(T_A\) to be in the fundamental representation then this means that \(V\) is an \(N \times N\) matrix. In terms of the components, we have a gauge field, but this is now accompanied by a fermion \(\lambda\) and auxiliary field \(D\), both of which must also sit in the adjoint representation. Equivalently, all of them naturally live in the Lie algebra \[ A_\mu = A_\mu^A T_A, \quad \lambda_\alpha = \lambda_\alpha^A T_A, \quad D = D^A T_A \]

Again, for \(SU(N)\) this means that each of these should be thought of as an \(N \times N\) matrix (in addition to any vector or spinor index they carry). The fermion is again called a gaugino or sometimes a gluino.

We again want to generalise the usual non-Abelian gauge symmetry to something that can act on a superfield. We do this by taking an adjoint valued chiral superfield \(\Omega = \Omega^A T_A\). Since \(\Omega\) is in the Lie algebra, \(e^{i\Omega} \in G\) and this acts on the real superfield as \[ e^{2V} \rightarrow e^{-2i\Omega^\dagger} e^{2V} e^{2i\Omega} \]

From the Baker-Campbell-Hausdorff formula, \(e^X e^Y = e^{X+Y+\frac{1}{2}[X,Y]+...}\), we get the transformation law for the superfield itself \[ V \rightarrow V + i(\Omega - \Omega^\dagger) - i[V, \Omega + \Omega^\dagger] + \dots \]

We can use the shift that appears in the first term to once again go to Wess-Zumino gauge where the real superfield takes the form (4.5), now with all fields in the adjoint of \(G\). You can check that the remaining gauge symmetry acts on \(A_\mu\) in the usual way, \[ A_\mu \rightarrow U A_\mu U^{-1} + i U \partial_\mu U^{-1} \]

with \(U \in G\). The field strength lives in a chiral multiplet, defined as \[ W_\alpha = -\frac{1}{4} \bar{D}^2 \left( e^{-2V} D_\alpha e^{2V} \right)

\]

Evaluated in Wess-Zumino gauge, we use the fact that \(V^3 = 0\), as in (4.7), to expand \(e^{2V} = 1 + 2V + 2V^2\). A short calculation then shows that \[ W_\alpha(y, \theta) = -\frac{1}{4} \bar{D}^2 \left( D_\alpha V - [V, D_\alpha V] \right)

\]

\[ = \lambda_\alpha(y) + \theta^\alpha D(y) + (\sigma^{\mu\nu} \theta)_\alpha F_{\mu\nu}(y) - i \theta^2 (\sigma^\mu \bar{D} \bar{\lambda})_\alpha(y)

\]

with the non-Abelian field strength and covariant derivative defined by \[ F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - i [A_\mu, A_\nu] \quad \text{and} \quad D_\mu \lambda = \partial_\mu \lambda - i [A_\mu, \lambda]

\]

To construct the action, we again define the complexified gauge coupling \[ \tau = \frac{\vartheta}{2\pi} + \frac{4\pi i}{g^2} \tag{4.18} \]

The action is then given by \[ S_{\text{SYM}} = -\frac{1}{8\pi} \int d^4x \text{Tr} \left[ \int d^2\theta\, \tau W_\alpha W^\alpha + \text{h.c.} \right]

\]

\[ = \int d^4x \text{Tr} \left[ -\frac{1}{2g^2} F_{\mu\nu} F^{\mu\nu} + \frac{i\vartheta}{16\pi^2} F_{\mu\nu} \star F^{\mu\nu} - \frac{1}{g^2} \lambda \sigma^\mu D_\mu \bar{\lambda} + \frac{1}{2g^2} D^2 \right] \tag{4.19} \]

This is super Yang-Mills. After all that work, it’s actually a very simple theory: just Yang-Mills coupled to a single, adjoint Weyl fermion. The factor of 2 differences compared to the Maxwell action (4.8) can be traced to the normalisation convention (4.17).

4.2.2 Supersymmetric QCD

We can add matter transforming in any representation \(R\) of the gauge group. The matter sits, as always, in a chiral superfield \(\Phi\) that now transforms as \[ \Phi \rightarrow \exp\left(-2i \Omega^A T_A^R \right) \Phi \tag{4.20} \]

We construct a gauge invariant, supersymmetric action with the superfield expression \[ \int d^4x d^4\theta\, \]

Φ†e^{2V}Φ = D_μ ϕ† D_μ ϕ − i ψ̄ σ̄_μ D_μ ψ + F†F − \frac{1}{2} (ψ̄ λ_A T^A ϕ + ϕ† λ_A T^A ψ) + ϕ† D_A ϕ

Here the covariant derivatives include the gauge field transforming in the appropriate representation R.

Again, various anomaly cancellation conditions must be satisfied when coupling Weyl fermions to non-Abelian gauge groups in complex representations. The simplest way forward is to work instead with Dirac fermions. This means that we take pairs of chiral superfields, Φ transforming in some representation R and Φ̄ in the conjugate representation R̄. (In much of the literature, these superfields are denoted Q and Q̄ but we’ll stick with Φ and Φ̄ to avoid any unnecessary confusion with the supercharges.) The most common is to take R to be the fundamental representation. We could, for example, consider G = SU(N_c) gauge group with N_f flavours of fermions, each in the fundamental representation. The action is then

S_{SQCD} = ∫ d^4x Tr [− \frac{1}{2g^2} F_{μν} F^{μν} + \frac{θ}{16π^2} F ⋆F_{μν} − \frac{i}{g^2} λ σ_μ D_μ λ̄ + ∑_{i=1}^{N_f} (|D_μ ϕ_i|^2 + |D_μ ϕ̃_i|^2 − i ψ̄_i σ̄_μ D_μ ψ_i − i ψ̃_i σ_μ D_μ ψ̄_i) − √2 ∑_{i=1}^{N_f} (ϕ_i† λ ψ_i − ϕ̃_i λ̄ ψ̄_i + h.c.) − V(ϕ, ϕ̃)] (4.21)

Here the covariant derivatives are

D_μ ϕ = ∂_μ ϕ − i A_μ ϕ and D_μ ψ = ∂_μ ψ − i A_μ ψ

for the fields in the fundamental representation, and

D_μ ϕ̃ = ∂_μ ϕ̃ + i ϕ̃ A_μ and D_μ ψ̃ = ∂_μ ψ̃ + i ψ̃ A_μ

for those in the anti-fundamental representation. Finally, the scalar potential is again given by the D-terms

V(ϕ, ϕ̃) = \frac{1}{2g^2} ∑_{i=1}^{N_f} D_A^i D_A^i with D_A^i = −g^2 (ϕ_i† T^A ϕ_i − ϕ̃_i T^A ϕ̃_i†) (4.22)

with T^A the N_c × N_c generators in the fundamental representation. This is the action of supersymmetric QCD, or SQCD for short. In a nod to the real world, we refer to the fermions ψ and ψ̃ as quarks. Their supersymmetric scalar partners ϕ and ϕ̃ are called squarks.

Once again, we can also add masses for the quark multiplets by including the gauge invariant superpotential

W(Φ, Φ̃) = ∑_{i=1}^{N_f} m_i Φ̃_i Φ_i

This gives an extra term to the scalar potential

δL_{mass} = − ∑_{i=1}^{N_f} |m_i|^2 (|ϕ_i|^2 + |ϕ̃_i|^2)

as well as Dirac masses for ψ_i and ψ̃_i.

There is no FI parameter that we can add for non-Abelian theories. The non-Abelian analog of (4.16) would involve Tr D but the trace of the generators of any non-Abelian Lie algebra always vanishes. Fayet-Iliopoulos terms can only be introduced for U(1) gauge theories.

## 4.3 The Moduli Space of Vacua

In the absence of a superpotential, supersymmetric gauge theories do not have a unique ground state. Instead, the D-term potential has a flat direction with V(ϕ) = 0. This is the moduli space of vacua. It will turn out that this moduli space holds the key to understanding the quantum dynamics of supersymmetric gauge theories. For this reason, we will spend some time studying its structure.

Consider, for example, U(1) SQED with a single flavour. If we don’t turn on a FI parameter then the D-term is (4.15)

D = −g^2 (|ϕ|^2 − |ϕ̃|^2)

Clearly any solution with

|ϕ|^2 = |ϕ̃|^2 = v^2

has zero energy. To fully specify the classical theory, we must decide where on this moduli space we want to sit.

At all points on the moduli space, there are always massless particles. Indeed, the low-energy physics is dominated by the fluctuations along the moduli space, which always correspond to massless particles, together with their fermionic superpartners. Meanwhile, the masses of heavy particles typically depend on where you sit on the moduli space which, in the current example, means that value of v^2. Because ϕ is charged under the U(1) gauge field, when it gets an expectation value, the Higgs mechanism kicks in and the photon gets a mass of order

m^2 ∼ e^2 v^2

But the Yukawa terms in (4.15) mean that a particular combination of fermions also gets a mass, given by

m_{fermion} ∼ e v

The fact that this is the same as m is, of course, no coincidence: the photon, massive fermion and an additional massive scalar in the spectrum form a massive vector multiplet of the kind discussed in Section 2.3. The origin of the moduli space, at ϕ = ϕ̃ = 0, is special because here the vector multiplet becomes massless.

The Geometry of Moduli Space

We denote the moduli space of vacua as M. As we now explain, this manifold naturally comes with a number of interesting geometric structures.

First M is defined by the requirement that V(ϕ) = 0. In the absence of a superpotential, this is equivalent to D(ϕ) = 0. (Note that here ϕ denotes all chiral multiplet scalars and, for SQED and SQCD, this means both ϕ and ϕ̃.). However, we should also remember that the gauge group G acts on these scalars. The gauge symmetry is not really a symmetry of the theory, but rather a redundancy in our description. This means that any two values of ϕ related by a gauge transformation should be viewed as physically equivalent. The upshot is that the vacuum moduli space M is defined as the quotient

M = {ϕ|D(ϕ) = 0}/G (4.23)

We have stumbled upon a co construction known to mathematicians as the symplectic reduction. It’s particularly natural because, as we’ve seen above, the D-term constraint D(ϕ) = 0 is fully specified by the action of the group G. In this way, the group G gets to act twice: once as a constraint, and again as a quotient. Mathematicians call the constraint D(ϕ) = 0 the moment map. If G includes an Abelian factor, the associated FI parameter is known as the level.

There are two, further ways to describe the moduli space M. We will now describe these, but won’t prove the equivalence with (4.23). Instead, we will content ourselves with some heuristic justification, followed by some examples².

²A full proof can be found in the paper by Marcus Luty and Wati Taylor, Varieties of vacua in classical supersymmetric gauge theories.

The fact that the group G “acts twice”, is even more apparent if the second way of writing the moduli space: it is the holomorphic quotient M = {ϕ}/G (4.24) with G the complexified gauge group. This means that we take the real parameters α that usually specify a gauge transformation – that is ϕ → eiqαϕ for Abelian G or ϕ → eiαaTaϕ for non-Abelian – and quotient by transformations with α ∈ C. You should think of the D-term constraint in (4.23) as like a gauge-fixing condition for the non-Hermitian part of the G transformations.

In fact, looking back at our construction of supersymmetric gauge theories, the gauge transformations started life in a chiral superfield Ω where everything was complex. They became real only after moving to Wess-Zumino gauge. From the perspective of supersymmetric gauge theory, the equivalence of (4.23) and (4.24) is best seen by looking at the more general gauge transformations before imposing Wess-Zumino gauge.

The final description of the moduli space will, in some circumstances, turn out to be the most useful. The manifold M can alternatively be viewed as M = {Gauge invariant, holomorphic monomials}/{Algebraic relations} (4.25). This is a description of M in terms of what mathematicians call an algebraic variety. This definition is best elucidated by examples that we will turn to below, but here we give the basic gist.

There are three key ideas that we need to explain in this definition: gauge invariant, holomorphic, and the algebraic relations. We cover each in turn:

• Because gauge symmetry is merely a redundancy in our choice of description, it should be possible to describe the dynamics of massless particles in terms of some gauge invariant fields. This is the basic idea underlying the characterisation (4.25).

• It’s always possible to build such gauge invariant fields by taking combinations like ϕ†ϕ. These are invariant under G, but not invariant under the larger G that defines the moduli space according to (4.24). The need to impose invariance under G, or equivalently the need to impose the D-term constraint D = 0, means that we should work with holomorphic gauge invariant combinations, meaning monomials that involve ϕ alone and not ϕ†. Alternatively, and more physically, supersymmetry means that we should be able to describe the fields in terms of chiral multiplets, and these are necessarily holomorphic.

• Finally, it will turn out that, for some examples, not all of the gauge invariant combinations are independent. This is why there is the need to quotient by certain relations between them. This is best illustrated when we turn to examples below. Mathematically, the equivalence between the quotient constructions (4.23) and (4.24) and the algebraic description (4.25) goes by the name of geometric invariant theory.

4.3.1 The Moduli Space of SQED

We’ll start by looking at the simpler case of SQED. This is a U(1) gauge theory coupled to N flavours. If we set the FI parameter to zero for now, then the D-term condition is (4.15) (cid:88) |ϕi|2 −|ϕ ˜ |2 = 0 (4.26) i=1

In addition, we should quotient by the U(1) gauge action ϕi → eiβϕi and ϕ ˜ → e−iβϕ ˜ (4.27) i i

We started with 2N fields ϕ and ϕ. There is one real constraint (4.26) which, together with the quotient (4.27) reduces the complex dimension of the vacuum moduli space by one. We then have dimM = 2N −1 (4.28)

Let’s see how to reproduce this counting when thinking of M as an algebraic variety defined by (4.25). The gauge invariant monomial are the bilinears M i = ϕ ˜ ϕi (4.29) j j

We will refer to these, not entirely accurately, as “mesons”. There are N2 such fields and, at first glance, it looks like we have way too many. However, they are not all independent and this is where the algebraic relations in (4.25) come into play.

The meson matrix M is built from vectors ϕ and ϕ and so has, at most, rank 1. This means that there are N −1 eigenvalues that are guaranteed to vanish. In general, the determinant of an N ×N matrix A can be written as ϵ Ai1 ...AiN = detAϵ i1...iN j1 jN j1...jN

The rank 1 matrix M therefore obeys ϵ (M i1 −λδ i1)...(M iN −λδ iN) = det(M −λ)ϵ = λN−1(λ−λ )ϵ i1...iN j1 j1 jN jN j1...jN 0 j1...jN

This tells us that if we expand 对左侧的所有 λN−2 阶及更低阶项必须对秩为 1 的矩阵消失。换句话说，我们有约束 ϵ M i1M i2 = 0 (4.30)

i1...iN j1 j2 其他约束可通过与更多 M i 收缩得到。我们接下来的任务是计算这里有多少独立约束。指标 i₃,...,iₙ 是自由的，因此通过选择这些，我们可以限制 i₁ 和 i₂ 跑遍任意一对。但所得的约束并非全部独立。例如，存在一个来自 (i₁,i₂) = (1,2) 的约束，另一个来自 (i₁,i₂) = (1,3) 的约束。但将第一个约束除以第二个，并重新整理，可得到来自 (i₁,i₂) = (2,3) 的约束。实际上，不难让自己相信来自 (i₁,i₂) = (1, 除 1 外的任意数) 的约束是独立且足以给出所有其他约束的。显然这里有 N−1 个这样的约束。

对于每个这样的约束，我们仍有 (j₁,j₂) 指标自由。这些也进行了反对称化，并且我们上面为 (i₁,i₂) 给出的相同论证也适用于 (j₁,j₂)。这意味着来自 (4.30) 的总约束数为 (N−1)²。

由所有介子 (4.29) 满足约束 (4.30) 定义的代数簇 M 具有复维数 dimM = N² −(N−1)² = 2N −1 与我们之前的计数 (4.28) 一致。

真空模空间的度量真空模空间继承了一个自然的度量。确实，如果我们限制在极低的能量下，动力学就是无质量场的，对应于沿模空间的涨落。这就是我们在 3.2.4 节讨论的非线性 sigma 模型的范畴。一般地，我们知道不仅在 M 上有一个度量，而且这个度量必须是 Kähler 的。

计算这个度量很简单。这里我们为最简单的情况 N=1 种味道用两种不同的方法做。最简单的做法是从 Kähler 势开始 K = ϕ†ϕ+ϕ ˜†ϕ ˜ 注意，规范理论的 Kähler 势涉及像 e^{2qV} 这样的项，其中 V 是实超场，以确保规范不变性。我们只是在以下计算中将规范场设为零，因此 Kähler 势就是上面的典型形式。限制在模空间 (4.26)，我们有 |ϕ|² = |ϕ ˜|²。此外，如果我们使用介子场 M = ϕϕ，Kähler 势变为 K = 2|ϕ|² = 2 M†M (4.31)

相关的度量就是 |dM|² ds² = (4.32)

2|M| 我们立即看到度量在原点 M=0 是奇异的。这个奇异性告诉我们一些重要的东西：当 ϕ = ϕ = 0 时，有新的无质量自由度。这恰恰是光子及其超对称伙伴，它们在原点变为无质量，因为希格斯机制被关闭了。

这是我们以前见过的教训。当我们在 3.3 节积掉重场时，我们发现低能有效理论在重场变轻的点处有奇异性。这是低能有效理论的一个普遍特征，并且在当我们讨论这些理论的量子动力学时，这在 6 节将很重要。现在，这个教训值得再重复一次：低能有效作用量中的奇异性标志着新的无质量自由度的出现。

有一个更平凡的方法来做同样的计算，突出了我们对真空模空间的原始商描述 (4.23)。约束 (4.26) 的一般解是 ϕ = ve^{iα}e^{iβ} 且 ϕ ˜ = ve^{iα}e^{-iβ} 其中 v > 0。e^{±iβ} 被取为与规范作用 (4.27) 一致，因此 v 和 α 提供模空间 M 上的坐标。

此时，有一个重要的因子 2 我们必须处理。对应于 U(1) 规范变换的参数 β 的范围是 β ∈ [0,2π)。相比之下，我们有 α ∈ [0,π)。这是因为我们总是可以实施一个 β = π 的规范变换，它翻转 ϕ 和 ϕ 的符号，或者等价地，取 α → α+π。

M 上的度量继承自标量场的动能项。为此，我们将 v, α 和 β 提升为在时空上缓慢变化的场。协变导数是 D ϕ = (∂ v +iv(∂ α+∂ β −A ))e^{i(α+β)} µ µ µ µ µ D ϕ ˜ = (∂ v +iv(∂ α−∂ β +A ))e^{i(α−β)} µ µ µ µ µ 我们现在选择 A = ∂ β 来吸收 β 的变化。这就是 (4.23) 中的商如何体现在这个计算中。标量场的动能项，限制在真空模空间上，变为 L = |Dϕ|² +|Dϕ ˜|² = 2 (∂v² +v²∂α²) (4.33)

eff 我们将其解释为类似于我们之前讨论的非线性 sigma 模型 (3.25) 的度量。可以简单地检查，这与用介子场写的度量 (4.32) 一致。

乍一看，(4.33) 看起来像一个平坦度量。确实，它是。但它不是 C 上的平坦度量，因为角坐标 α 的周期不是 2π。相反，它是 C/Z 上的平坦度量，并且在 the origin v = 0. This is how we see the emergence of the massless photon at this point.

Turning on the FI Parameter

A small variation on this calculation provides yet another perspective on the importance of singularities in the low-energy effective action. We again consider SQED with N = 1 flavour, but this time turn on a FI parameter. The D-term constraint now reads |ϕ|² −|ϕ̃ |² = ζ (4.34)

We assume that ζ ≥ 0. In the ground state, we necessarily have |ϕ|² ≠ 0 meaning that the photon now gets a mass on all points of the moduli space.

We can see how this manifests itself in the moduli space metric. The condition (4.34) is solved by ϕ = √(v² +ζ)eiαeiβ and ϕ̃ = veiαe−iβ Our previous calculation to compute the metric on M is now a little more involved. The subtlety lies in figuring out what expression we should take for the gauge field A. The answer can be found in its equation of motion. Or, more precisely, the equation of motion in the limit e² → ∞ where we neglect the Maxwell term. This is the appropriate limit when the gauge field responds immediately to fluctuations in the scalar and gives Aµ = ∂µ α + ∂µ β It reduces to our previous, pure gauge, choice when ζ = 0. Inserting this expression into the kinetic terms for ϕ and ϕ̃, we compute the metric on the vacuum moduli space Leff = |Dϕ|² +|Dϕ̃ |² = (∂v)²/(v²+ζ) + (2v²/(2v²+ζ)²)(∂α)² (4.35)

Importantly, as we approach the origin, v² → 0, the metric is well approximated by ds² ≈ dv² +4v²dα² = dv² +v²d(2α)² That extra factor of 2 makes all the difference! We now get the flat metric with the angular coordinate 2α ∈ [0,2π) which means that close to v = 0 the metric really does look like flat space.

4.3.2 The Moduli Space of SQCD

We now play the same game for SQCD. We will take gauge group G = SU(Nc)

coupled to Nf fundamental flavours, ϕi in the fundamental representation and ϕ̃af in the anti-fundamental. Here a = 1,...,Nc is the gauge group index while i = 1,...Nf is the flavour index.

The generators (TA)ac in the fundamental representation are the set of Hermitian, traceless, complex N ×N matrices. Meanwhile, the generators in the anti-fundamental representation are simply T̄A = −TA. The N²c −1 D-term conditions (4.22) are then (ϕ†)i TA ϕi −(ϕ̃ TA ϕ̃†)i = 0 A = 1,...N²c −1 where there is an implicit sum over i = 1,...,Nf. To get a better sense of these constraints, let us first relax the requirement that TA is traceless. (This is what we would get if the gauge group was U(Nc) rather than SU(Nc).) In this case, the TAc provide a basis for all Hermitian matrices and the D-term condition is N²c constraints (ϕ†)a ϕib −(ϕ̃a ϕ̃†)ib = 0 a,b = 1,...Nc for U(Nc)

But the fact that we’re working with SU(Nc) rather than U(Nc) means that there’s no reason to set the trace to zero. So our true D-term constraint is (1/N) (ϕ†)a ϕib −(ϕ̃a ϕ̃†)ib = ( (ϕ†)c ϕic −(ϕ̃c ϕ̃†)ic ) δab (4.36)

At first glance, this looks like it’s still N²c conditions. But if you take the trace then you find that both sides are trivially equal. This means that, in fact, it’s only N²c −1 conditions, with no condition on the trace. This is what we wanted.

To understand the vacuum moduli space, we must first solve the equations (4.36). As we will now see, the nature of the solutions is different for Nf < Nc and Nf ≥ Nc. We deal with each in turn.

Nf < Nc

We’d like to count the dimension of the moduli space M, defined by (4.36) modulo gauge transformations. It’s tempting to think that there are just N²c − 1 constraints in (4.36) but how do we know that they are all independent? In fact, it’s simple to see that these constraints cannot all be independent when Nf < Nc because then we would have more constraints than degrees of freedom. Yet solutions to (4.36) certainly exist! To proceed, we use the fact that the D-terms and gauge symmetry are closely entwined. The D-terms only bite when the gauge symmetry does.

When Nf < Nc, we can always use an SU(Nc) gauge transformations and SU(Nf) flavour rotations to put the matrix ϕ in the block-diagonal form ϕi a = ( v ... 0 ; ... ; 0 ... vf ; 0 ... 0 ) (4.37)

Here the columns have length Nc and the rows length Nf. We can then use the other SU(Nc) to rotate ϕ to be in upper-diagonal form. (We can’t make it fully diagonal because we’ve already used up the SU(Nc) to diagonalise ϕ). However, now we invoke the D-term conditions (4.36). The only solutions to these conditions require that the off-diagonal terms in ϕ vanish. (You could check this for a simple case, say Nc = 3 and Nf = 2 to get...)

To get a feel for why this is the case. We're left with \[\tilde{\phi}^\dagger_i = \phi_i\]

As before, points on the moduli space related by a gauge transformation are to be physically identified. On a generic point on the moduli space (with \(v_i \neq v_j \neq 0\) when \(i \neq j\)) the gauge group is broken to \[SU(N_c) \rightarrow SU(N_c - N_f)\]

The number of broken gauge generators is then \[\text{# broken generators} = (N_c^2 - 1) - ((N_c - N_f)^2 - 1)\]

Each of these is eaten by one of the original \(2N_c N_f\) bosons \(\phi\) and \(\tilde{\phi}\). This means that the resulting vacuum moduli space has complex dimension \[\dim \mathcal{M} = 2N_c N_f - [\text{# broken generators}] = N_f^2\]

Note that we only divide out by the points on the moduli space related by the \(SU(N_c)\) gauge symmetry. There will still be points on the moduli space related by the flavour symmetry \(SU(N_f)\) but these are physically distinct vacua.

We can also view the moduli space as an algebraic variety. Once again, the holomorphic monomials are the meson fields \[M_j^i = \tilde{\phi}^a_j \phi^i_a\]

This time the name “meson” is more appropriate: we have contracted the gauge indices of \(\phi\) and \(\tilde{\phi}\) to form a gauge invariant composite. The mesons form \(N_f^2\) fields but, in contrast to SQED, there is no constraint on \(M\). The contracted gauge indices in the previous equation run over \(a = 1,...,N_c > N_f\) so there is no obstacle to \(M\) being maximal rank. We see immediately that \(\dim \mathcal{M} = N_f^2\), in agreement with our result above.

We can compute the metric on \(\mathcal{M}\) along the same lines as we saw for SQED. The Kähler potential is \[K = \phi^{\dagger i}_a \phi^a_i + \tilde{\phi}^a_i \tilde{\phi}^{\dagger i}_a\]

We want to write this in terms of the meson field. To do this, first note that for \(N_f < N_c\) the trace term on the right-hand side of the D-term vanishes when restricted to the moduli space and we have \[\phi^{\dagger i}_a \phi^a_j = \tilde{\phi}^a_j \tilde{\phi}^{\dagger i}_a\]

From this, we have \[(M^\dagger M)^i_j = \tilde{\phi}^{\dagger i}_a \phi^{\dagger a}_k \phi^k_b \tilde{\phi}^b_j = (\tilde{\phi}^{\dagger i}_a \tilde{\phi}^a_j)(\tilde{\phi}^{\dagger k}_b \tilde{\phi}^b_j)\]

where, in the last equality, we've used the previous relation. Taking the square root of this matrix equation tells us that \((\tilde{\phi}^\dagger \tilde{\phi})^i_j = (M^\dagger M)^{1/2\, i}_j\), and so the Kähler potential is \[K = 2 \text{Tr} \, M^\dagger M\]

Just like the Kähler potential for SQED, the resulting metric will have singularities whenever \(M^{-1}\) ceases to exist. Again, these singularities correspond to new degrees of freedom becoming massless. At a generic point on the moduli space, there will be massless gauge bosons associated to the unbroken \(SU(N_c - N_f)\) gauge symmetry. But along the loci on which \(M\) is not invertible we have an enhancement of the gauge group and new massless gauge bosons.

For \(N_f \geq N_c\), the story is different. First, we can now use \(SU(N_c)\) and \(SU(N_f)\) transformations to find solutions to the D-term equations, again in block-diagonal form \[\phi_i^a = \begin{pmatrix} v_1 & \dots & 0 & 0 \\ \vdots & \ddots & & \vdots \\ 0 & \dots & v_{N_c} & 0 \end{pmatrix} \quad \text{and} \quad \tilde{\phi}^{\dagger i}_a = \begin{pmatrix} \tilde{v}_1 & \dots & 0 & 0 \\ \vdots & \ddots & & \vdots \\ 0 & \dots & \tilde{v}_{N_c} & 0 \end{pmatrix}\]

with \[|v_a|^2 = |\tilde{v}_a|^2 + \rho, \quad a = 1,...,N_c\]

where \(\rho\) must be independent of \(a\). This reflects the fact that the trace term on the right-hand side of the D-term can now be non-zero.

At a generic point on \(\mathcal{M}\), the \(SU(N_c)\) gauge symmetry is completely broken. The complex dimension of the moduli space is therefore \[\dim \mathcal{M} = 2N_c N_f - (N_c^2 - 1)\]

How can we describe this moduli space as an algebraic variety? The meson fields provide \(N_f^2\) degrees of freedom, but now there are constraints of the kind we met for SQED since \(M\) is at most rank \(N_c\). In addition, there are also new gauge invariant fields. These are baryons, built from the totally anti-symmetric invariant tensor of \(SU(N_c)\), \[\mathcal{B}^{i_1 \dots i_{N_c}}_{a_1 \dots a_{N_c}} = \phi^{i_1}_{a_1} \dots \phi^{i_{N_c}}_{a_{N_c}} \epsilon^{a_1 \dots a_{N_c}}\]

\[= \tilde{\phi}_{a_1}^{i_1} \dots \tilde{\phi}_{a_{N_c}}^{i_{N_c}} \epsilon_{i_1 \dots i_{N_c}}^{a_1 \dots a_{N_c}}\]

Each of these is anti-symmetric in the \(N_c\) different flavour indices \(i_1,...,i_{N_c}\). There are then a bunch of further constraints between these baryons and mesons. Rather than doing this in full generality, we'll instead just describe how this works for the two cases that will prove most interesting in Section 6.

• \(N_f = N_c\): In this case, anti-symmetry properties mean that there is just a single baryon of each type \[\mathcal{B} = \phi^1_{a_1} \dots \phi^{N_c}_{a_{N_c}} \epsilon^{a_1 \dots a_{N_c}} \quad \text{and} \quad \tilde{\mathcal{B}} = \tilde{\phi}^{a_1}_1 \dots \tilde{\phi}^{a_{N_c}}_{N_c} \epsilon_{a_1 \dots a_{N_c}}\]

The meson \(M\) can have rank \(N_c\), so there are no constraints there. But there is a single relation between the mesons and baryons, given by \[\mathcal{B} \tilde{\mathcal{B}} = \det M\]

This means that there are \(N_c^2 + 2\) degrees of freedom in \(M\), \(\mathcal{B}\) and \(\tilde{\mathcal{B}}\) and a single relation, giving a moduli space of dimension \(\dim \mathcal{M} = N_c^2 + 1\) in agreement with (4.41). The relation will play a starring role when we come to consider the quantum theory in Section 6.3.

• \(N_f = N_c + 1\): Now there are \(N_f\) baryons of each type, \[\mathcal{B}_j^{i_1 \dots i_{N_c}} = \epsilon_{j i_1 \dots i_{N_c}}^{1 \dots N_c} \quad \text{and} \quad \tilde{\mathcal{B}}_j = \epsilon_{j i_1 \dots i_{N_c}}^{1 \dots N_c} \tilde{\mathcal{B}}^{i_1 \dots i_{N_c}}\]

This time the constraints are less obvious, but they turn out to be \[\text{Adj}(M)^j_i = \mathcal{B}_i \tilde{\mathcal{B}}^j \quad \text{and} \quad M^i_j \mathcal{B}_i = M^i_j \tilde{\mathcal{B}}^j = 0\]

where \(\text{Adj}(M)\) is the adjugate matrix, which is the transpose of the matrix of cofactors. The adjugate matrix is most familiar when \(M\) is invertible, in which case \(\text{Adj}(M) = (\det M) M^{-1}\). However, the conditions \(\mathcal{B} M = M \tilde{\mathcal{B}} = 0\) tell us that \(M\) has a zero eigenvalue and so is not invertible.

– 120 – At this point, things start to get a little messy! It turns out that not all the relations (4.43) are independent, but there’s no way to write them as a smaller set. Mathematicians say that the resulting variety is not a complete intersection. We’ll simply duck the issue which, it turns out, will not hinder us from understanding the physics.

There is one sense in which the use of the words “mesons” and “baryons” might be misleading. In QCD, mesons and baryons are bound states of quarks, stuck together because of confinement. But confinement is a surprising and poorly understood property of the quantum theory. Here we are not invoking anything so dramatic. Indeed, we haven’t yet discussed any quantum effects and what we’ve call SQCD might better be called SCCD for our current purposes. Instead, we’re using meson and baryon fields simply because they are gauge invariant and so free of any gauge redundancy. We’ll turn on the Q in SQCD in Section 6 where we’ll see how this tallies with ideas of confinement.

4.3.3 Briefly, Gauged Linear Sigma Models in 2d

We’ve learned that we can construct interesting geometric spaces as the moduli spaces of vacua of supersymmetric gauge theories. This kind of construction goes by the name of gauged linear sigma models. It turns out that it’s a particularly useful method when wielded in quantum field theories in d = 1+1 dimensions.

To see why, first consider the action for a non-linear sigma model in general d-dimensional spacetime S = ∫ddx g_{ij} ∂_µπ^i ∂^µπ^j (4.44)

Here π^i are coordinates on a manifold M with metric g_{ij}.

When d = 0 + 1, we’re dealing with the quantum mechanics of a particle moving on M. But we know what happens in this case: the wavefunction will spread over M and there will typically be a unique ground state.

This is conceptually very different from what happens in d = 3 + 1 dimensions. There, each point on M defines a different ground state of the system. There is no spread of the wavefunction.

The reason for this different behaviour can be traced to the long-distance property of the propagator. The propagator grows in d = 0 + 1 and d = 1 + 1 dimensions (logarithmically in the latter case) while it decays in d = 2+1 and higher. This fact – 121 – is closely related to the Mermin-Wagner theorem which says that global symmetries cannot be spontaneously broken in d = 0+1 and d = 1+1 dimensions. (We met this theorem in the lectures on Statistical Field Theory and Gauge Theory.)

In the context of non-linear sigma models of the type (4.44), this long-distance behaviour of the propagator is telling us that d = 0+1 and d = 1+1 dimensions are special because the wavefunction spreads over the manifold M. This means that the ground state of the system has a chance of knowing something about the global structure of the manifold M, like its topology. Indeed, studying the dynamics of low-dimensional quantum systems on M has been a very fruitful source of developments in mathematics. This beginnings of this story are told in the lectures on Supersymmetric Quantum Mechanics.

The story is particularly rich for theories in d = 1+1 dimensions where, in addition to the wavefunction spreading over M, the UV divergences of the quantum field theory mean that the metric on M is renormalised. At one-loop, the running is captured by the beautifully geometric RG equation ∂g_{ij} / ∂µ = R_{ij} (4.45)

where µ is the RG scale and R_{ij} the Ricci tensor. This formula is known as Ricci flow. It plays an important role in String Theory and has a number of applications in pure mathematics. Note that the flow stops only if the metric becomes Ricci flat, with R_{ij} = 0. At this point we have a 2d conformal field theory. However, not all manifolds admit such a Ricci flat metric.

Things become even more interesting when we throw supersymmetry into the mix. This is what we called N = (2,2) supersymmetry in Section 2.4.3. It not only gives us an important level of control over the dynamics but, as we’ve seen already in these lectures, dovetails nicely with some interesting mathematical structures. It turns out that the gauge theory approach to realising non-linear sigma models as the vacuum moduli space is particularly powerful in this context. Here we just give a hint of how this works.

First, the anomaly cancellation conditions (4.14) are for 4d quantum field theories and are not needed in two dimensions. (A 4d Weyl fermion reduces to a 2d Dirac fermion and so the theories we construct are not chiral in 2d.) This means that there is nothing to stop us considering U(1) coupled to N chiral multiplets of charge +1 in – 122 – d = 1+1 dimensions. The D-term condition is ∑_{i=1}^{N} |ϕ_i|^2 = ζ where we turn on a FI parameter ζ > 0. Taken on its own, this condition defines a sphere S^{2N−1}. But we still have to quotient by the U(1) action to get the vacuum moduli space and this gives M = S^{2N−1}/U(1) = CP^{N−1} Here CP^{N−1} is complex projective space, defined as the space of complex lines in C^N. This can also be seen in the defi Definition (4.24) of the moduli space.

Things get more interesting if we add, in addition, a chiral superfield P with charge −q. The D-term condition is now $$ D = |\phi_i|^2 - q|p|^2 - \zeta = 0 $$ After quotienting by the U(1) action, the vacuum moduli space is a non-compact manifold. But we now have the option of introducing a gauge invariant superpotential $$ W(P,\Phi) = P G(\Phi_1, \dots, \Phi_N)

$$ with G a homogeneous polynomial of degree q. The potential energy now also includes contributions from the F-terms $$ V = |p|^2 \sum_{i=1}^N \left| \frac{\partial G}{\partial \phi_i} \right|^2 + |G|^2 $$ If we choose G to be transverse, meaning $$ \frac{\partial G}{\partial \phi_i} = 0 \quad \forall i \quad \Leftrightarrow \quad \phi_i = 0 $$ then V = 0 only if p = 0 which means that we’re back onto the $\mathbb{CP}^{N-1}$ vacuum manifold. But now, in addition, we must satisfy G(ϕ) = 0. The resulting vacuum moduli space is now a compact manifold given by a degree q hypersurface, $M \subset \mathbb{CP}^{N-1}$.

To give a sense of why the gauge theory description is useful in understanding the geometric properties of the vacuum manifold, here’s a short anecdote. It turns out that the gauge theory flows to a conformal field theory only when q = N. (Only then does the FI parameter not run.) In this case, the vacuum moduli space X is a degree N hypersurface $\mathbb{CP}^{N-1}$. But it is known that such spaces define what mathematicians call a Calabi-Yau manifold. One of the key properties of these spaces (conjectured by Calabi and proven by Yau) is that they admit a Ricci flat metric. This ties in nicely with the gauge theory expectation because, as we have seen in (4.45), such a Ricci flat metric is necessary for conformal symmetry.

There are many more geometrical properties that can be extracted from a study of gauge theories in 2d dimensions, including mirror symmetry of Calabi-Yau manifolds³.

## 4.4 Extended Supersymmetry

We discussed the representations of extended supersymmetry algebras in Section 2.4. For theories with N = 2 supersymmetry (or eight supercharges) there are two different multiplets: $$ \begin{aligned} N=2 \text{ vector multiplet} &= N=1 \text{ vector multiplet } (A_\mu, \lambda_\alpha, D) \\ &+ N=1 \text{ chiral multiplet } (\phi, \chi_\alpha, F)

\end{aligned} $$ Here the chiral multiplet necessarily sits in the adjoint representation of the gauge group. There is also the N = 2 matter multiplet $$ \begin{aligned} N=2 \text{ hypermultiplet} &= N=1 \text{ chiral multiplet } (q, \psi_\alpha, F) \\ &+ N=1 \text{ chiral multiplet } (\tilde{q}, \tilde{\phi}, \tilde{F})

\end{aligned} $$ If the first of these transforms in the representation R of the gauge group then the second transforms in the conjugate representation $\bar{R}$. We can tune the matter content and interactions of N = 1 theories to give theories with extended supersymmetry.

With N = 4 there is just a single multiplet (at least restricting to non-gravitational theories) with content $$ \begin{aligned} N=4 \text{ vector multiplet} &= N=1 \text{ vector multiplet } (A_\mu, \lambda^1_\alpha, D) \\ &+ 3 \times N=1 \text{ chiral multiplets } (\phi^i, \lambda^{i+1}_\alpha, F_i) \quad i=1,2,3 \end{aligned} $$ In addition to the gauge field, we have three complex scalars and four Weyl fermions, all sitting in the adjoint representation of the gauge group.

To construct theories with N = 2 and N = 4 supersymmetry, we could try to build an extended superspace. It turns out that there is a superspace for N = 2 theories, known as harmonic superspace, but it’s rather cumbersome to work with. In contrast, there is no superspace for N = 4 theories. Instead, we will build Lagrangians for both by tuning the interactions of N = 1 theories. The key is to get Lagrangians that exhibit larger R-symmetries.

### 4.4.1 N = 2 Theories

N = 2 super Yang-Mills comprises of a vector multiplet V and an adjoint chiral multiplet Φ. The N = 2 Lagrangian is constructed by simply turning off any superpotential for Φ. It is $$ \begin{aligned} \mathcal{L} &= -\text{Tr} \left[ \int d^2\theta \frac{1}{8\pi i \tau} W^\alpha W_\alpha + \text{h.c.} \right] + \int d^4\theta \frac{1}{g^2} \Phi^\dagger e^{2V} \Phi \\ &= \text{Tr} \left[ -\frac{1}{4g^2} F_{\mu\nu} F^{\mu\nu} - \frac{i}{g^2} \lambda \sigma^\mu D_\mu \bar{\lambda} - \frac{i}{g^2} \bar{\chi} \sigma^\mu D_\mu \chi + \frac{1}{g^2} D_\mu \phi^\dagger D^\mu \phi \right] + \text{Tr} \frac{F \wedge F}{16\pi^2} \\ &\quad + \text{Tr} \frac{1}{g^2} \left[ \sqrt{2}i \lambda [\phi^\dagger, \chi] + \sqrt{2}i \bar{\lambda} [\phi, \bar{\chi}] - \frac{1}{2} [\phi^\dagger, \phi]^2 \right] \quad (4.46)

\end{aligned} $$ The potential term comes from integrating out the D-term from the N = 1 vector multiplet: we’ll look more closely at the moduli space of vacua below.

Of more immediate importance are the fermion terms: the two Weyl fermions λ and χ sit on the same footing in the final Lagrangian, despite their origins in different N = 1 multiplets. This means that there is an SU(2) symmetry that rotates them, under which they sit in a doublet 2. The bosonic field ϕ does not transform under this symmetry, which tells us that this must be an SU(2) R-symmetry. This is the smoking gun for N = 2 supersymmetry. There is also a U(1) symmetry, under which $R[\phi] = 2$ and $R[\lambda] = R[\chi] = 1$.

There is another way to derive the N = 2 Lagrangian. You can write down a minimal super Yang-Mills theory in d = 5+1 dimensions, consisting of a gauge field coupled to a Weyl fermion. Upon dimensional reduction, this gives the Lagrangian (4.46).

³ The use of gauge theories as a method to understand geometry was pioneered by Edward Witten in the paper Phases of N = 2 Theories. You can read more in Kentaro Hori’s lecture notes which comprise Part 2 and Part 3 of the book Mirror Symmetry.

couple matter to (4.46) in the form of hypermultiplets. These comprise of two chiral multiplet, Q and Q. (Note: until now the letter Q has always meant a supercharge, but it’s not unusual to also use it to denote a chiral multiplet, with Q standing for “quark”.) As we mentioned above, if Q sits in the representation R then ˜ ¯Q necessarily sits in the conjugate representation R. This suffices to determine the interaction with the vector multiplet V, (cid:90) (cid:104) (cid:105)

L = d4θ Q†e2VQ+Q ˜†e−2VQ ˜ vector

But in addition we should couple Q and Q to the N = 2 vector multiplet field Φ in such a way that the SU(2) symmetry between λ and χ remains. This is achieved by the superpotential term √ (cid:90)

L = 2 d2θ Q ˜ ΦQ+h.c.

chiral

The interactions between Q and Q themselves are greatly limited by the extended supersymmetry: we can add only mass terms W = 2mQQ

A general N = 2 theory is specified by the gauge group G and the representations R of any matter multiplets, together with their masses. (If G contains Abelian factors, we can also add FI terms. We will not include these in the following.) The scalar potential comes, as always, from integrating out D and F-terms. After some rearranging, the potential can be expressed as the sum of positive definite terms. For SU(N ), it is 1 g2 d (cid:88) imG (cid:32) (cid:88) (cid:33)2 d (cid:88) imG (cid:12) (cid:12)(cid:88) (cid:12) (cid:12) 2 V(ϕ,q,q˜) = Tr[ϕ†,ϕ]2 + q†TAq −q˜TAq˜† +g2 (cid:12) q˜TAq (cid:12)

g2 2 i R i i R i (cid:12) i R i(cid:12)

(cid:12) (cid:12)

A=1 i A=1 i (cid:88)

+ q†{ϕ† −m†,ϕ−m }q +q˜{ϕ† −m†,ϕ−m }q˜† (4.47)

i i i i i i i i

(Initially, the D-term contains both ϕ and the q’s and q˜’s. The first two terms on the first line both arise from this D-term, but the cross-term has sneaked into the third line, where it turns ϕ†ϕ into the anti-commutator {ϕ†,ϕ}.)

The hypermultiplet scalars q and q˜† transform as a doublet 2 under the SU(2) symmetry. Conversely, their fermionic superpartners ψ and ψ are singlets under SU(2) . The second and third terms in the potential (4.47) can be rewritten in way that makes the SU(2) symmetry manifest. We introduce the doublet (cid:32) (cid:33)

ω = i q˜†

The second term in (4.47) is a real D-term while the third is a complex F-term. But, with N = 2 supersymmetry they are better viewed as a potential V = 1 D ⃗2 arising g2 from triplet of D-terms (cid:88)

D ⃗A = g2 ω†TA⃗σω i R i

where ⃗σ are the Pauli matrices. The triplet D transforms in the 3 of SU(2) .

The potential (4.47) has some interesting properties. Let’s take the masses to vanish: m = 0. In this case, the second line takes the schematic form |ϕ|2(|q|2 +|q˜|2). That means that if we’re looking for vacuum states with V(ϕ,q,q˜) = 0 then there are two possibilities: either ϕ = 0 and the hypermultiplet scalars q,q˜ are turned on; or q˜ = q = 0 and the vector multiplet scalar ϕ is turned on. Geometrically, this means that the vacuum moduli space factorises as M = M ×M C H

There are defined as follows: • M is called the Coulomb branch. It is defined as the space q˜ = q = 0 with ϕ restricted to obey [ϕ†,ϕ] = 0 This is solved by ϕ sitting in the Cartan sub-algebra. For G = SU(N ). this means that ϕ = diag(ϕ ,...,ϕ ) with ϕ = 0. At a typical point, the gauge 1 Nc a a group is broken to the Cartan subalgebra with a bunch of surviving, massless photons. For example, for G = SU(N ), this means G → U(1)Nc−1. At some special points, the surviving gauge group will be enhanced further.

When the gauge group is broken to U(1)’s, all charged matter experiences a Coulomb force, hence the name of this branch of vacua.

• M is called the Higgs branch. It is defined as the space ϕ = 0 with q˜ and q constrained to obey the conditions ⃗A = 0 In addition, we should quotient by the action of G. At a general point, the gauge group is completely Higgsed, hence the name of this branch of vacua.

The Higgs branch has real dimension that is a multiple of four and is a special case of a Ka¨hler manifold, known as a hyperK¨ahler manifold. (For what it’s worth, a hyperKa¨hler manifold has three independent complex structures while a Ka¨hler manifold has just one.) The definition of the Higgs branch is an extension of the idea of symplectic reduction that gives a hyperK¨ahler metric and is known as the hyperK¨ahler quotient construction.

4.4.2 N = 4 Theories The more supersymmetry we have, the more restrictive the theory.

With N = 1 supersymmetry, we are free to specify the gauge group and (chiral) matter content. In addition to the gauge coupling and masses, both suitably complexified, we can also introduce any superpotential interactions that we wish.

With N = 2 supersymmetry, we are again free to specify the gauge group and (now non-chiral) matter content. But we have no freedom in the choice of interactions: the only arbitrary parameters are the gauge coupling and masses.

With N = 4 supersymmetry, we get to specify only the gauge group and gauge coupling. All other t 拉格朗日量中的项由超对称性决定。

构建N=4超对称杨-米尔斯理论有多种方式。它可以看作是从d=9+1维度最小超对称杨-米尔斯理论通过维数约化到d=3+1维度的结果。或者，也可以将其视为一个N=2理论，其中包含一个伴随表示的超多重态。该理论包含四个伴随表示的外尔费米子，它们在SU(4) R对称性的4表示中变换，以及六个实标量φ_i（i=1,...,6），在6表示中变换。标量势为 V(φ) = -g²/2 Σ_{i<j} [φ_i, φ_j]² 现在只有一个库仑分支，在该分支的某一般点上群G被破缺到其嘉当子代数。

5 短训班：量子规范动力学这些讲座的最终目的是理解超对称规范理论的量子动力学。但在此之前，我们确实需要理解一些关于普通规范理论的量子动力学。本节的目的就是提供必要的背景。

我需要提醒你的是，与这些讲义的其余部分不同，我们不会尝试证明本节中的任何陈述。事实上，其中一些陈述——比如禁闭现象——目前还无法被证明，尽管我们有压倒性的证据表明它确实发生，这些证据既来自数值计算，也来自玩具模型，尤其是超对称理论。（更不用说像你确实被禁闭粘合在一起这样的实验结果了。）其他现象——比如单圈β函数和反常——则有一些技术性计算作为基础。在这里我们略去技术细节，只陈述相关的事实，这意味着你可以放松下来，将本节视为类似歌曲中段的部分来享受。如果你想看到支撑这些结果的详细计算，它们都可以在规范理论的讲座中找到。

## 5.1 强耦合

我们在本节的兴趣将集中在非阿贝尔规范理论上。我们从杨-米尔斯理论开始。拉格朗日量为 L_YM = ∫ d⁴x (-1/(2g²) Tr F_{μν} F^{μν})  (5.1)

这里场强由F_{μν} = ∂_μ A_ν - ∂_ν A_μ - i[A_μ, A_ν]给出。如你所见，我们采用耦合常数放在动能项前面的约定。

5.1.1 β函数杨-米尔斯理论的关键特征使其既微妙又困难，即耦合常数g²在重整化群(RG)下是跑动的。在能标μ处，耦合常数由下式给出： 1/g²(μ) = 1/g²_0 - (b_0 / (4π)²) log(Λ_UV² / μ²)  (5.2)

其中g²_0是在紫外截断标度Λ_UV处计算的耦合常数。这里b_0是单圈β函数的系数，对于纯杨-米尔斯理论，它由下式给出： b_0 = (11/3) C₂(adj)

其中C₂(adj)是群论因子，称为二次卡西米尔算子。它还有另一个化身，即伴随表示的Dynkin指标。（注意，我们定义的I(R)与规范理论讲义中的定义相差一个因子2。）各种紧致李群的二次卡西米尔算子如表1所示。在这些讲座中，我们将几乎完全专注于规范群G = SU(N)的情况。

耦合常数的跑动通常用单圈β函数来概括： β(g) ≡ μ dg/dμ = - (b_0 / (4π)²) g³  (5.3)

其解给出了(5.2)式的对数行为。

β函数最重要的特征是前面的负号。这意味着理论在高能量下是弱耦合的，这种现象被称为渐近自由。反之，它意味着理论在低能量下是强耦合的。我们想要理解的正是这个低能物理。

这里我们说的低能量和高能量是什么意思？分界线在哪里？这个问题的答案可以在公式(5.2)中找到。这是因为我们可以构造一个强耦合标度： Λ = μ exp(-8π² / (b_0 g²(μ)))  (5.4)

它具有dΛ/dμ = 0的性质。换句话说，它是一个重整化群不变量。这就是杨-米尔斯理论变强的标度。

关于标度Λ的存在，已经有一些值得注意的地方。经典上，杨-米尔斯理论(5.1)没有量纲参数。这意味着没有任何东西可以设定一个标度。相反，只有一个无量纲的耦合常数g²。但对数跑动成功地将其转化为一个有量纲的参数Λ！一种理解方式是注意到，要定义量子理论，我们从一开始就必须引入一个有量纲的参数。这就是理论的紫外截断Λ_UV。强耦合标度(5.4)与紫外截断的关系是： Λ = Λ_UV exp(-8π² / (b_0 g²_0))

这意味着如果裸耦合是小的，g₀ ≪ 1（它应该是这样），那么物理标度Λ相对于紫外截断是指数压低的：Λ ≪ Λ_UV。

5.1.2 禁闭与质量能隙当耦合很小时，量子场论看起来与其经典对应物相似。例如，经典麦克斯韦理论预言 vides a decent guide to what you might expect from QED. In contrast, when the coupling is large, all bets are off. The quantum theory and classical theory may be completely different. Yang-Mills provides the archetypal example.

If you solve the classical Yang-Mills equations, you will find waves that propagate at the speed of light. This suggests that the quantum theory will give rise to a massless particle called a gluon, similar to the photon. Indeed, if you stare at the action there is no A² term that might suggest a mass.

Nonetheless, we now know that quantum Yang-Mills contains no massless particles. We say that the theory is gapped which means that the first excited state has a finite energy above the ground state. This additional energy is, of course, just E = mc² where m is the mass of the lightest particle in the theory. The gap is of order the strong coupling scale, m ∼ Λ.

We don’t currently have the technology to prove the Yang-Mills mass gap. Indeed, it is generally considered one of the most important and challenging open problems in mathematical physics. We do, however, have very compelling numerical evidence that this occurs, together with some intuition built from various toy models and heuristic explanations for why it occurs. You can read about some of these in the lectures on Gauge Theory. We’ll meet others later in these lectures.

In our world, the strong force is governed by an SU(3) gauge theory known as QCD. The associated strong coupling scale is Λ ≈ 300 MeV and is usually referred to as Λ_QCD. No massless gluons are seen in Nature, but there is good evidence for states known as glueballs with masses around the scale Λ.

The existence of a mass gap goes hand in hand with another phenomenon: this is confinement. To explain this, consider placing two charged test particles in the Yang-Mills field. To be specific, we’ll consider G = SU(N) and take a quark in the fundamental representation N and an anti-quark in N. We simply ask: what force do they feel?

It’s best to compute the potential energy between the two particles. You can first do this in the classical theory. There’s a little bit of group theoretic fiddliness but the final result is very intuitive: the potential energy scales with the separation r between particles as V(r) ∼ g²/r  (5.5)

This, of course, is the same scaling that we see in the Coulomb force of electromagnetism.

What about the quantum theory? If the separation between particles is small, meaning r ≪ 1/Λ, you don’t notice much difference. At these short distances the theory is weakly coupled and we again see the Coulomb-like potential (5.5) between test particles. We should replace the coupling constant in (5.5) with g²(μ) = g²(1/r) so it’s more accurate to say that the potential scales as V(r) ∼ log r/r but this is a mild correction to the physics.

In contrast, at large separation things are radically different. For distances r ≫ 1/Λ, the potential between test particles takes the form V(r) ∼ σr  (5.6)

The coefficient σ necessarily has dimension [σ] = 2 and this scale, like everything else in Yang-Mills, is set by σ ∼ Λ². For reasons that we will explain shortly, σ is called the string tension. The force law (5.6) is, to put it mildly, a dramatic departure from what we’re used to. The potential energy now increases with separation. Indeed, it costs an infinite amount of energy to pull the quark anti-quark pair to infinity. This kind of potential energy is said to be confining.

The phenomenon of confinement is, like the mass gap, something that we can’t prove from first principles. Once again, however, there is clear numerical evidence together with a plethora of heuristic explanations.

Figure 6. A rough sketch of the non-Abelian field lines in the Coulomb phase, on the left, and in the confining phase, on the right.

To get some very rough intuition for what’s going on, we can repeat Faraday’s old experiment (now in thought only!) and try to understand what the field lines look like. At short separation, in the Coulomb-like phase (5.5), the field lines form the familiar pattern, first spreading out radially before they bend over to combine with those emitted by the anti-particle. This is shown on the left-hand side of Figure 6. However, as the particles are separated to larger distances, the fact that the gauge field is massive makes itself known. The field lines no longer spread out, but instead lie closely together to form a collimated flux tube. This flux tube acts very much like a string, connecting the two quarks. If its tension, or energy per unit length, is σ then it gives rise to a confining force law like (5.6).

The above description of confinement should be taken with something of a pinch of salt. After all, we are in a strongly interacting quantum field theory and there is no single field configuration that governs the physics. Instead, there are many fields configurations that we should sum over that contribute to the path integral.

discussion above should be understood to mean that those field configurations that resemble the flux tube dominate.

The story above was told in terms of test particles. When we introduce dynamical matter fields into the theory, one would naively expect the associated particles to bind together like the test particles above. And, roughly speaking, this is indeed what happens, at least if the number of light species is small enough. (We’ll flesh out this statement shortly.) For example, in QCD the quarks bind together into mesons and baryons. Mesons contain a quark anti-quark pair while baryons contain three quarks and are a colour singlet by dint of the ϵabc invariant tensor. For G = SU(N) we would get mesons which again contain a quark anti-quark pair and baryons containing N quarks.

There is much more to say about confinement. In particular, the correct, mathematical description of the confining phase involves a non-local operator known as the Wilson loop W[C] = TrP exp( i ∮_C A ).

Here C is a closed curve in spacetime, while P stands for “path ordering”. In a Coulomb-like phase, the expectation value scales as ⟨W[C]⟩ ∼ exp(−L[C]) where L[C] is the length of the perimeter of C. Meanwhile, in the confining phase the expectation value scales as ⟨W[C]⟩ ∼ exp(−A[C]) where A[C] is the area spanned by the curve C. An explanation of why this is the right diagnostic, together with its significance, can be found in the lectures on Gauge Theory.

5.1.3 Adding Matter Until now, we’ve considered pure Yang-Mills and its response to test particles. Now we wish to add dynamical matter. The first thing that this does is change the beta function.

Suppose that we have a bunch of Weyl fermions transforming in some representation R_f and a bunch of scalars transforming in some representation R_s. Then the one-loop beta function (5.2) becomes b0 = (11/3)I(adj) − (1/6) Σ_f I(R_f) − (1/6) Σ_s I(R_s). (5.7)

Here the group theoretical factors are Dynkin indices. For the representation R, the Dynkin index I(R) is defined by the normalisation of the trace Tr_R T^A T^B = I(R) δ^AB / 2. (5.8)

Our previous normalisation (4.17) means that we’re taking the fundamental representation to have I(fund) = 1. Some examples of I(R) for SU(N) representations are collected in Table 2.

Strictly speaking, the beta function takes the form (5.7) only if the matter is massless. If the matter has some mass m, then the beta function runs like (5.7) for energies μ > m, but as we drop below the mass scale m the matter decouples and its contribution to the one-loop beta function is removed.

Table 2. Some group theoretic properties of SU(N) representations. Here □ is the symmetric representation and the anti-symmetric. Conjugate representations have I(R̄) = I(R) and A(R̄) = −A(R).

Irrep | dim | I(R) | A(R)

□ | N | 1 | 1 adj | N^2−1 | 2N | 0 sym | N(N+1)/2 | N+2 | N+4 anti | N(N−1)/2 | N−2 | N−4

Again, the first thing to notice is the signs. Both fermions and scalars give a contribution to the beta function that has the opposite sign to the gauge bosons. This means that if we have too much matter then we will have b0 < 0 and, correspondingly, β(g) > 0 and the theory will be weakly coupled in the infra-red. In this case, the quantum theory looks very much like classical Yang-Mills at low energies, with massless gauge bosons. Here we would like to understand what happens when b0 > 0 and the theory is strongly coupled.

To illustrate this, we will consider a specific set of matter particles. We take G = SU(N_c) with N_f flavours of quarks in the fundamental representation. This means that we have a collection of left-handed Weyl spinors ψ^i_α and ψ̃^{iα}_a. Here a = 1,...,N_c is the gauge index and i = 1,...,N_f the flavour index. We take ψ^i_α to transform in the fundamental N_c representation and ψ̃^{iα} in the anti-fundamental representation N̄_c. (If we take the complex conjugate of ψ, we get a Dirac spinor in the N_c representation.) The action is L_QCD = −(1/(2g^2)) Tr F^{μν} F_{μν} − Σ_{i=1}^{N_f} ( i ψ̄^i σ̄^μ D_μ ψ_i + i ψ̃̄_i σ̄^μ D_μ ψ̃^i ) (5.9)

with D_μ ψ = ∂_μ ψ − i A_μ ψ and D_μ ψ̃ = ∂_μ ψ + i ψ A_μ.

We could add a mass for the quarks by introducing terms like L_mass = Σ_{i=1}^{N_f} m_i ψ̃^i ψ_i + h.c.

However, our interest will be on the case with massless quarks, with m_i = 0.

You might wonder why this is interesting. After all, the quarks in our world aren’t massless. But they are almost massless! The up and down quarks have masses of a few MeV, much less than the relevant scale Λ_QCD ≈ 300 MeV. Meanwhile, the strange quark has a mass m_strange ≈ 95 MeV, still smaller than Λ_QCD although not by much.

This means that understanding the behaviour of massless QCD is not a bad starting point for understanding the full theory.

5.1.4 Chiral Symmetry Breaking The important observation is that massless QCD (5.9) has an extra symmetry that the massive theory doesn’t have, under which the ψ and ψ̃ fermions rotate independently. The global symmetry includes G = SU(N_f)_L × SU(N_f)_R × U(1)_V.

N × SU(N)_L × SU(N)_R

Here SU(N)_L acts on the ψ while SU(N)_R acts on the ψ̃, ψ → (L⋆)_ij ψ and ψ̃_i → R_i^j ψ̃_j with L ∈ SU(N)_L and R ∈ SU(N)_R. (In fact, the full symmetry of the classical theory is U(N)_L × U(N)_R; we’ll discuss these additional U(1) factors in Section 5.2.)

The group G is known as the chiral symmetry, chiral because it acts on Weyl spinors rather than Dirac spinors. This kind of symmetry only exists when the masses m = 0. The question that we want to ask is: what becomes of this chiral symmetry? The answer to this depends on the number of flavours N_f in a way that is not fully understood. However, for suitably small N_f the theory develops a vacuum expectation value

⟨ψ̃_i ψ_j⟩ ∼ Λ^3 δ_i^j

The formation of this condensate is a strong coupling effect and, like confinement, poorly understood. In contrast, the consequence of the condensate is both well understood and dramatic. First, note that the condensate does not preserve the chiral symmetry (5.11). Indeed, it transforms as

⟨ψ̃_i ψ_j⟩ → Λ^3 R_i^k (L†)_k^j

This is the phenomenon of chiral symmetry breaking, sometimes shortened to χSB. The surviving subgroup requires us to set L = R in (5.11), meaning

SU(N)_L × SU(N)_R → SU(N)_{f, diag}

The spontaneous breaking of chiral symmetry means that massless QCD actually has a moduli space of vacua, since each choice of L ≠ R in (5.12) gives a different, equally valid, ground state, albeit one that is entirely equivalent to the original because they are related by a global symmetry. The vacuum moduli space is the coset

M = [SU(N)_L × SU(N)_R] / SU(N)_{f, diag}

with dimension

dim M = N_f^2 - 1

There is an important difference between this vacuum moduli space and those that arise in supersymmetric theories. All points on M in QCD are equivalent because any point is related to any other by the action of a symmetry. This is not the case for the supersymmetric moduli space.

Nonetheless, there is one important feature that is common whenever we have flat directions and this is the importance of massless particles, corresponding to fluctuations along M. When the flat directions arise from broken symmetries, as in the present case, these massless particles are Goldstone bosons.

We learn something interesting. Yang-Mills theory has a mass gap. But massless QCD, at least for N_f > 1, does not. Even if the theory confines, giving massive baryons and glueballs, chiral symmetry breaking means that there are massless Goldstone bosons. These can be identified with certain meson states called pions.

Of course, in our world the pions are not massless. But this is because the constituent quarks are not exactly massless so the chiral symmetry is not exact. Nonetheless, the chiral symmetry is an approximate symmetry which, in turn, means that the would-be Goldstone bosons are light, but not exactly massless. Indeed, the pions are notably lighter than all other hadrons in QCD.

5.1.5 Phases of Massless QCD

We’re now in a position to describe the different phases of massless QCD as we vary N_c and N_f. There is much that we don’t yet understand (here “we” means everyone, not just those following these lectures!) and there are a few subtleties that I will sweep under the carpet. But, with broad brush, we can sketch the different phases of the theory.

We start with low N_f:

• When N_f = 0, we have pure Yang-Mills. The theory sits in the confining phase, with a mass gap.

• When N_f = 1, there is no chiral symmetry group (5.10) and so no chiral symmetry breaking. The theory is again thought to have a mass gap, with quarks bound in mesons and baryons.

• When 2 ≤ N_f ≤ N_f⋆ the theory confines and exhibits chiral symmetry breaking. This means that the low energy theory consists of freely interacting Goldstone bosons, parameterising the moduli space (5.13).

The big question here is: what is the maximum value N_f⋆ for which chiral symmetry breaking occurs? We don’t know the answer to this. Various approaches, including numerics, suggest that it is somewhere around

N_f⋆ ≈ 4 N_c

Our lack of knowledge of this simple question highlights just how poorly we understand strongly interacting field theories.

Now let’s jump to high values of N_f and we’ll then try to fill in the details in the middle.

• When N_f ≥ (11/2) N_c, the beta function is positive. You can see this from the general expression (5.7) which, for massless QCD, becomes

b_0 = (11 N_c - 2 N_f) / 3

This means that theory is weakly coupled in the infra-red: the low-energy physics consists of massless gluons, weakly interacting with massless quarks. As we go to smaller and smaller energies, the interactions become weaker and weaker. Strictly speaking, in the far IR, the physics is free.

On the flip side, these become arbitrarily strongly coupled in the UV, with the gauge coupling diverging at some very high scale. This doesn’t mean that we should discard them, but they don’t make sense at arbitrarily high energy scales. Said another way, we can’t take the UV cut-off Λ to infinity while keeping any low-energy interactions. Nonetheless, it's quite possible that these theories may arise as the low-energy limit of some other theory. We will see examples in Section 6 when we discuss supersymmetric extensions of QCD.

Figure 7. The beta function for N slightly below the asymptotic freedom bound has a zero which indicates the existence of an interacting conformal field theory.

That leaves us with the physics in the middle region. We'll keep working down from the asymptotic freedom bound 11Nc / 2.

• When N⋆⋆ < N < 11Nc / 2, things are more interesting. To see what happens, we need the two-loop beta function β(g) = − b0 / (4π)² g³ − b1 / (4π)⁴ g⁵ +...

with the one-loop coefficient b0 given in (5.14) and the two-loop coefficient b1 = (34Nc² / 3) − (Nf / 3)(Nc² − 1) − (10Nf / 3)Nc In the window of interest, b0 > 0 and b1 < 0, so we can play the one-loop contribution against the two-loop contribution to find a zero of the beta function g⋆² = −(4π)² (b0 / b1)

with β(g⋆) = 0. The beta function is shown in Figure 7. The existence of such a fixed point is telling us that we have an interacting conformal field theory: there are massless modes, but they are no longer free in the infra-red. This is known as the Banks-Zaks fixed point.

Importantly, when N lies just below the asymptotic freedom bound, so Nf = 11Nc / 2 − ϵ, this fixed point lies at g⋆ ≪ 1 which means that we can trust the analysis without having to worry about higher order corrections. Moreover, because g⋆ is small we can use perturbation theory to calculate anything that we want.

Figure 8. The expected phases of massless QCD. The asymptotic freedom bound is N = 11Nc / 2. The lower edge of the conformal window is not known but is expected to be somewhere around N ≈ 4Nc.

However, as N decreases, the value of the fixed point g⋆ increases until we can no longer trust the analysis above. The expectation is that we get a conformal field theory only for some range of N, lying within N⋆⋆ < N < 11Nc / 2. This is known as the conformal window. We don't currently know the value of N⋆⋆.

That leaves us with understanding what happens in the middle when N⋆ < N ≤ N⋆⋆. Our best guess is that there is no such regime, and the upper edge of the chiral symmetry breaking phase coincides with the lower edge of the conformal window, N⋆⋆ = N⋆. This guess is motivated partly by numerics and partly by a lack of any compelling alternative. For us, the lesson to take away is that strongly interacting quantum field theories are hard and even the most basic questions are beyond our current abilities. A summary of the expected behaviour of massless QCD is shown in Figure 8.

## 5.2 Anomalies

The next topic that we need to cover is anomalies. This is a beautiful subject and, in many ways, the place in which quantum field theory intersects most cleanly with topics in mathematics. Here we won't describe any of these mathematical underpinnings, but instead just cover the minimum material necessary for our later applications.

The main idea is to understand how certain symmetries manifest themselves in quantum field theory. To this end, consider a single left-handed Weyl fermion in d = 3+1 dimensions. The action is S = ∫ d⁴x i ψ† σ̄µ ∂µ ψ

This action is clearly invariant under the U(1) global symmetry ψ → eiα ψ, with the corresponding current jµ = ψ† σ̄µ ψ. To illustrate the anomaly, we will couple this current to a gauge field A with charge q ∈ Z. The action is now S = ∫ d⁴x i ψ† σ̄µ Dµ ψ where the covariant derivative contains the new coupling Dµ ψ = ∂µ ψ − i q Aµ ψ. This action is now invariant under the gauge symmetry ψ → e i q α(x) ψ and Aµ → Aµ + ∂µ α (5.15)

Before we proceed, I should mention that there are two distinct ways to think about the gauge field A and this distinction will be important when we come to look at the various implications of anomalies. They are: • A could be a dynamical gauge field. In the classical theory, this means that we treat it as a dynamical variable, with its own equation of motion, typically after adding a Maxwell term to the action. In the quantum theory, it means that we integrate over A in the path integral.

• A could be a background gauge field. This means that it is something fixed, under our control, and should be viewed as a parameter of the theory. Turning it on typically breaks Lorentz symmetry, but could be useful to explore how our system responds to the presence of an electric or magnetic field. In the quantum theory, A appears as a source on which the partition function depends.

We will consider gauge fields of both types in what follows. However, for now, we will consider A to be a background gauge field, something that is under our control. While the classical theory is clearly invariant under the gauge transformation (5.15), the question that we really want to ask is: what about the quantum theory? For this, we should turn to the path integral, with the partition function in Euclidean space defined Z[A] = DψDψ̄ exp − ∫d⁴x iψ̄ σ̄^µ D ψ

Clearly the action in the exponent remains invariant under gauge transformations. But now we must also worry about the measure in the path integral, and this takes some care to define. The statement of the anomaly is that the measure is not invariant under gauge transformations. Instead, it turns out that the measure, and hence the partition function, changes by a phase

Z[A] → exp( i q₃ / (32π²) ∫d⁴x α F^{⋆F_{µν} Z[A] (5.16)

with ⋆F_{µν} = ½ ε_{µνρσ} F^{ρσ}.

This subtlety only happens for fermions. If we have scalar fields charged under a symmetry, then the measure is perfectly invariant. At heart, this is related to the fact that there is no difficulty in giving masses to scalar fields while preserving symmetries, but giving masses for fermions necessarily breaks certain symmetries.

The purpose of this section is to understand the implication of this calculation and a number of variants. As we now explain, there are three different avatars of the anomaly. We deal with them each in turn.

5.2.1 Gauge Anomalies

The first implication of the anomaly (5.16) is that it is an obstruction to gauging. Although the action is invariant under the gauge symmetry, the measure is not and neither is the partition function. That means that we cannot promote the gauge field A to a dynamical field, where we integrate over it in the path integral. If we attempted to do this, we would get a sick theory.

There are a number of ways to see why the theory is sick but here is a simple one. Recall that when we first attempted to quantise the gauge field A in the lectures on Quantum Field Theory we had some work to do to decouple the negative norm states that arise from quantising A. That work ultimately boiled down to using the gauge invariance to remove these states. But in an anomalous theory, we no longer have that gauge invariance at our disposal and the Hilbert space will involve negative norm states. That’s bad.

The upshot is that a U(1) gauge theory, coupled to a single Weyl fermion, is not consistent. To proceed, we must have multiple, left-handed Weyl fermions ψ_i, each with some charge q_i. (If we have right-handed fermions, simply conjugate them to make them left-handed.) The phase in (5.16) is then proportional to the sum of q_i³. The gauge theory is consistent only if

∑ q_i³ = 0 (5.17)

This was one of the conditions that we met previously in (4.14). This condition is sometimes written in a different way. One, very simple way to solve this constraint is to take pairs of Weyl fermions with charges ±q. If we conjugate one of them to become a right-handed Weyl fermion, we then have a single Dirac fermion with charge q. These are called vector-like theories and QED is the most familiar example.

There are, however, more interesting solutions to (5.17) that do involve ± pairs. These are known as chiral gauge theories.

The discussion above holds for an Abelian gauge symmetry. There is a similar story for a non-Abelian gauge symmetry G. For a single Weyl fermion, transforming in the representation R of G, the anomaly is proportional to the group theoretic factor A(R). For the fundamental representation, A(R) = 1. For other representations, it is given by

Tr_R T_A {T_B, T_C} = A(R) Tr_adj T_A {T_B, T_C}

Some examples of A(R) for SU(N) representations are collected in Table 2. To be consistent, a non-Abelian gauge theory coupled to a bunch of left-handed Weyl fermions must obey

∑ A(R_i) = 0 (5.18)

which is the non-Abelian version of (5.17). If R is a complex representation, then it’s simple to show that A(R̄) = −A(R). This means that we can again always satisfy (5.18) by taking Dirac fermions, rather than Weyl fermions, since these have a left-handed fermion in a representation R and another in R̄.

One consequence of the relation A(R̄) = −A(R) is that A(R) = 0 for any real representation. This means that there is no obstacle to coupling a single Weyl fermion in a real representation to a non-Abelian gauge group. Indeed, we’ve seen this already in these lectures: pure super-Yang-Mills has a single adjoint Weyl fermion, but the adjoint representation is real so there is no problem.

Relatedly, here’s a comment that will prove useful shortly: only massless fermions contribute to the anomaly. If you have a Weyl fermion ψ in a complex representation R of a group G, then to give it a mass preserving G you need a second Weyl fermion ψ̃ in representation R̄. You can then write down a Dirac mass term m ψ ψ̃. But the two Weyl fermions ψ and ψ̃ cancel in their contribution to the anomaly. Alternatively, you can write down a Majorana mass m ψ ψ for any fermion in a real representation of G, but, as we have seen, there is no contribution to the anomaly from fermions in a real representation. This means that only fermions that cannot get a mass preserving G contribute to the anomaly for G.

When we previously discussed the requirements of anomaly cancellation in (4.14), we gave e a further condition on U(1) gauge theories. We asked that they also satisfy ∑ q = 0 (5.19)

This, it turns out, is a little more subtle and it follows from the requirement that the theory can be consistently coupled to gravity. There is no corresponding requirement for non-Abelian gauge theories (essentially because Tr T_A = 0 for any generator of a simply connected Lie algebra).

The upshot is that if you want to have a theory with a dynamical gauge field, then you better make sure that the anomaly (5.17) or (5.18) cancels. Furthermore, if you want your theory to be compatible with gravity, then you have one further hoop (5.19) to jump through.

5.2.2 Chiral (or ABJ) Anomalies

Here is a slight variant on the same calculation that leads to a physically very different conclusion. Again, consider a single Weyl fermion, now coupled to a background non-Abelian gauge field A in some representation R of the global symmetry G. It’s useful to think of G = SU(N), and R either the fundamental or adjoint representation. We can construct the partition function Z[A] = ∫ Dψ Dψ̄ exp[ -∫ d^4x ( i ψ̄ σ̄^µ D_µ ψ ) ]

now with D_µ ψ = ∂_µ ψ - i A_µ T_A ψ. We know that the partition function isn’t invariant under gauge transformations of G. But here we instead ask a different question: is it invariant under U(1) rotations of the fermion?

ψ → e^{i q α} ψ (5.20)

The answer is again no, with the partition function transforming as Z[A] → exp[ (i q I(R) / 16π^2) ∫ d^4x α Tr(F ⋆ F_µν) ] Z[A] (5.21)

with I(R) the Dynkin index defined previously in (5.8). This looks very similar to our previous result, but it should now be thought of a mixed anomaly between the U(1) symmetry (5.20) and the non-Abelian symmetry G. This can be seen in the coefficient q I(R) which is still cubic but now a mix of Abelian and non-Abelian generators.

An interesting consequence of this is that, in the presence of background gauge fields for G, the U(1) symmetry is no longer conserved. If we repeat Noether’s theorem, including the anomaly (5.21), we find that the U(1) current associated to the symmetry (5.20) now obeys ∂_µ j^µ = (q I(R) / 32π^2) Tr(F ⋆ F_µν) (5.22)

When the right-hand side is non-zero, the current is no longer conserved.

An important example of this occurs in the theory of massless QCD that we introduced in the last section. The gauge group is G = SU(N) and the Lagrangian is (5.9), L_QCD = - (1/(2g^2)) Tr(F_µν F^µν) - ∑_{i=1}^{f} ( i ψ̄_i σ̄^µ D_µ ψ_i + i ψ̃̄_i σ̄^µ D_µ ψ̃_i ) (5.23)

We have added extra fermions to cancel the gauge anomaly in G, as we should. But, as we will see, a mixed anomaly of the type (5.21) remains.

Classically, the theory (5.23) has a U(N_f)_L × U(N_f)_R global symmetry, with each factor rotating ψ and ψ̃ independently. We studied the SU(N_f)_L × SU(N_f)_R subgroup in some detail in the previous section, but didn’t mention the two U(1) factors. These are usually written as U(1)_B: ψ_i → e^{iβ} ψ_i and ψ̃_i → e^{-iβ} ψ̃_i U(1)_A: ψ_i → e^{iα} ψ_i and ψ̃_i → e^{iα} ψ̃_i (5.24)

The subscript B stands for “baryon” since this is the vector-like symmetry under which baryons are charged. Since ψ and ψ̃ have opposite charges under U(1)_B, there is no obstacle to gauging it should we wish. Moreover, the ± charges also cancel on the right-hand side of (5.22), and the U(1)_B current is conserved in the quantum theory. In contrast, the axial symmetry U(1)_A has the same charges for ψ and ψ̃. This means that the associated current is, following (5.22), no longer conserved. Instead, it obeys ∂_µ j^µ_A = (f / 16π^2) Tr(F ⋆ F_µν) (5.25)

Note that the gauge fields on the right-hand side are now dynamical SU(N) gauge fields that fluctuate. There is now no way to set them to zero. There is no axial U(1) symmetry in the quantum theory.

This also explains why we didn’t include U(1)_A when discussing chiral symmetry breaking in the previous section. Since it is not a symmetry, there is no corresponding Goldstone boson. (In the real world, the meson associated to U(1)_A is called the η′ and is significantly heavier than the pion Goldstone bosons.)

This, then, is the second avatar of the anomaly. It manifests itself as a symmetry of the classical theory that does not survive the quantisation procedure. In fact, this is how the anomaly was first discovered. In this context, it usually goes by the name of the chiral anomaly, or the ABJ anomaly after Adler, Bell and Jackiw who first uncovered this subtle effect of quantum field theory. (Yes, that Bell.)

There is one further way to think about the chiral anomaly. Non-Abelian gauge theories have an additional, topological term S_ϑ = ∫ d^4x Tr(F ⋆ F_µν) / 16π^2 This is the theta term. We already met it when constructing super Yang-Mills theory in (4.19). Comparing with the form of the mixed anomaly (5.21), we see that axial transformation (5.24) can be thought of as shifting the theta angle U(1)_A: ϑ → ϑ + 2α (5.26)

We’ve met this kind of idea previously in Section 3.3, where we found it useful to think of parameters – superpartners – transforming under symmetries (which, of course, means that the symmetries aren’t actually symmetries). In Section 6, we’ll learn how we can combine the shift of the ϑ angle with holomorphy in supersymmetric theories.

5.2.3 ’t Hooft Anomalies So far we have discussed two manifestations of the anomaly: • For a gauge symmetry, the anomaly better cancel. Or else.

• A mixed anomaly between a global symmetry and gauge symmetry means that the global symmetry isn’t.

But what if we have an anomaly just for a global symmetry? What are the consequences? From what we’ve discussed above, we know that the symmetry isn’t conserved if we couple it to background gauge fields. But nothing compels us to do so. So what else can we learn from this?

The answer is both subtle and powerful. An anomaly for a purely global symmetry puts strong constraints on the low-energy dynamics of the theory. The anomaly should be thought of as a robust way of characterising the theory, and this characterisation cannot change under RG flow, nor under any other deformation of the theory, providing that the symmetry remains unchanged. Such anomalies in global symmetries are referred to as ’t Hooft anomaly.

We will first explain the basic idea and then give a concrete example. Suppose that we have some quantum field theory – typically a non-Abelian gauge theory – that is weakly coupled in the UV, but flows to strong coupling in the IR. We will abstractly call the UV theory T<sub>UV</sub>. We assume that it has some global symmetry G<sub>F</sub>. This should be a true symmetry of the quantum theory, meaning that it has no mixed anomalies with the gauge symmetry.

This UV theory may have an anomaly for G<sub>F</sub>. If G<sub>F</sub> is Abelian, anomaly is simply (cid:80) q³ as in (5.17); if it is non-Abelian the anomaly is (cid:80) A(R) as in (5.18). Either way, we will denote this anomaly as A<sub>UV</sub> and assume A<sub>UV</sub> ̸= 0, The theory now flows under RG to a theory T<sub>IR</sub> in the IR which, as we’ve seen, will typically be very different. We have the following result: Claim: Either the symmetry G<sub>F</sub> is spontaneously broken, or the anomalies match meaning A<sub>UV</sub> = A<sub>IR</sub>.

This is a wonderfully powerful result. If G<sub>F</sub> is spontaneously broken then we necessarily have massless Goldstone bosons. But if G<sub>F</sub> is unbroken then we must have massless fermions that reproduce the anomaly. This is known as ’t Hooft anomaly matching.

Proof: The argument for ’t Hooft anomaly matching is very slick. Suppose that A<sub>UV</sub> ̸= 0 then we know from the discussion above that we’re not allowed to couple G<sub>F</sub> to dynamical gauge fields. That would lead to a sick theory.

To proceed, we introduce a bunch of extra massless Weyl fermions transforming under G<sub>F</sub>. We call these spectator fermions. These won’t interact directly with our original fields in T<sub>UV</sub>, but they are designed so that the total anomaly of the original fields and these new fermions vanishes: A<sub>UV</sub> + A<sub>spectator</sub> = 0 Now there’s nothing to stop us introducing dynamical gauge fields for G<sub>F</sub>. We do so, but with a very very small coupling constant. We’ll see the importance of this shortly.

Now let’s go back to our original theory T<sub>UV</sub>. It will flow to strong coupling at some scale Λ and we’d like to understand the physics T<sub>IR</sub> below this scale. If the gauge coupling for G<sub>F</sub> is small enough, then this RG flow takes place entirely unaffected by the presence of the G<sub>F</sub> gauge fields. This means that one of two things could have happened. It may be that the strong coupling dynamics of T<sub>UV</sub> spontaneously breaks the symmetry G<sub>F</sub>. (For example, as we’ve seen, this is expected to happen if we take G<sub>F</sub> to be the chiral symmetry of QCD.) This was the first possibility of our claim.

Alternatively, G<sub>F</sub> may be unbroken at low-energies. In this case, we’re left with T<sub>IR</sub>, together with the spectator fermions, all coupled to the G<sub>F</sub> gauge fields. But this can only be consistent if A<sub>IR</sub> + A<sub>spectator</sub> = 0 Clearly, this is only consistent if A<sub>IR</sub> = A<sub>UV</sub>. □

Triangle Diagrams Until now, we’ve explained the anomaly as a transformation of the fermion measure in the path integral. However, the anomalies also show up in perturbation theory when computing corrections to Ward identities like (5.25). In this way of looking at things, one has to compute so called triangle diagrams. Schematically, these take the form Anomaly = (cid:88)<sub>fermions</sub> where you sum over all Weyl fermions running in loops. The outer legs are currents, either gauge or global. The fact that there are three legs reflects the fact that the anomalies are always proportional to the cube of generators. Our three kinds of anomalies are related to the different types of currents on the legs • Gauge³: This is a gauge anomaly.

• Global × Gauge²: This is the chiral anomaly.

• Global³: This is the ’t Hooft anomaly.

An Application: Confinement Implies Chiral Symmetry Breaking We saw in the last section that massless QCD exhibits two, distinct strong coupling phenomena: confinement and chiral symmetry breaking. We will now show that they '’re not quite as unrelated as they first appear.

As we’ve seen, the U(1) symmetry of massless QCD is anomalous. The true symmetry group is therefore G = U(1)×SU(N)×SU(N)

F B f L f R

Let’s first compute the ’t Hooft anomalies in the ultra-violet, where the quarks contribute. There is no ’t Hooft anomaly for U(1)³ because this is a vector-like symmetry. In contrast, there is a ’t Hooft anomaly associated to the chiral, SU(N) factors. In fact, there are two. The first is the purely non-Abelian anomaly [SU(N)]³ : A = A(□) = −N_fL Here the anomaly A arises because each quark ψ carries a colour index a = 1,...,N_c. The ψ_fL fermions transform in the □ of SU(N)_c and A(□) = −1. But there are N_c such fermions. Hence the result N_c A(□) = −1. There is a similar anomaly for SU(N)_fR.

In addition, there is a mixed ’t Hooft anomaly between U(1) and SU(N)_f. This is [SU(N)]²×U(1) : A′ = qI(□) = N_fL which again simply counts the number of quarks.

Now the question is: what happens in the infra-red? For suitably low N_c, we’ve already explained the chiral symmetry G is expected to be broken down to U(1)×SU(N)_f diag, but we didn’t give any justification for this. The idea of ’t Hooft anomaly matching goes some way to help.

Here is the idea. We will assume that the theory confines and, moreover, that in the infra-red, the physics is described by weakly interacting mesons and baryons. (This is in contrast to the conformal field theories that we see at larger N_c.) In such a situation, ’t Hooft anomaly matching shows that the chiral symmetry must be broken.

Here is the argument. Suppose that G is unbroken in the infra-red. Then they must be massless fermions around that can reproduce the anomalies A and A′. Moreover, by assumption, these massless fermions must be bound states of quarks, either mesons or baryons.

Mesons certainly can’t do the job because these are bosons. Baryons, meanwhile, contain N_c quarks so these too are bosons when N_c is even. This is telling us that when N_c is even, a confining theory contains no fermions at low-energies and so certainly can’t reproduce the anomalies. We learn that chiral symmetry breaking must occur when N_c is even.

What about N_c odd? Now baryons are fermions. Is it possible that some of these baryons could be massless and reproduce the ’t Hooft anomalies? This time we have something of a calculation to do. First, you have to figure out what representations of G the baryons sit in. Then you have to figure out what combination of massless baryons could match the anomalies A and A′. It takes some work, but the answer is that the baryons can never reproduce the anomalies. (You can find the calculation in Section 5.6 of the lectures on Gauge Theory.) This means that if QCD confines into weakly interacting colour singlets, then chiral symmetry is necessarily broken.

## 5.3 Instantons

One of the new ingredients in these lectures is the Yang-Mills theta angle S_ϑ = ∫ d⁴x Tr F ⋆ Fµν which deserves some explanation.

First, the theta term is a total derivative, S_θ = ∫ d⁴x ∂_µ K_µ with K_µ = εµνρσTr (A_ν ∂_ρ A_σ − (2/3) A_ν A_ρ A_σ)

This means that it does not affect the classical equations of motion. Nonetheless, it can affect the quantum dynamics of gauge theories. This arises because the path integral receives contributions from field configurations that have something interesting going on at infinity so that the boundary term S_ϑ is non-vanishing. This something interesting can be found in the topology of the gauge group.

To explain this, we first Wick rotate so that we work in Euclidean spacetime R⁴. Configurations that have a finite action from the Yang-Mills term must asymptote to pure gauge, A_µ → i Ω ∂_µ Ω⁻¹ as x → ∞ with Ω ∈ G. This means that finite action, Euclidean field configurations involve a map Ω(x) : S³ → G with S³ = ∂R⁴. Maps of this kind fall into disjoint classes. This arises because the gauge transformations can “wind” around the spatial S³ in such a way that one gauge transformation cannot be continuously transformed into another. Such winding is characterised by homotopy theory. In the present case, the maps are labelled by an element of the homotopy group which is Π_1(G) = Z for all simple, compact Lie groups G. In words, this means that the winding of gauge transformations (5.27) at infinity is classified by an integer n.

This statement is most intuitive for G = SU(2) since SU(2) ∼ = S³ and the homotopy group counts the winding from one S³ to another. For higher dimensional G, it turns out that it’s sufficient to pick an SU(2) subgroup of G and consider maps which wind within that. You then need to check that these maps cannot be unwound within the larger G.

It can be shown that, in general, the winding n ∈ Z is computed by n(Ω) = (1/(24π²)) ∫_{S³} d³S εijk Tr(Ω ∂_i Ω⁻¹)(Ω ∂_j Ω⁻¹)(Ω ∂_k Ω⁻¹)

Evaluated on any configuration, the theta term becomes S_ϑ = ϑ n It is the contribution from configurations with n ≠ 0 in the path integral that means that observables in quantum gauge theories can depend on ϑ.

We can say more if we work in a regime in which the theory is weakly coupled. Here the path integral is dominated by the saddle points, which are solutions to the classical equations of motion. This means that any ϑ dependence should come from field equations that wind at infinity, so n ≠ 0, and solve the classical equations of motion, D_μ F^μν = 0 (5.30).

There is a cute way of finding solutions to this equation. The Yang-Mills action is S_YM = ∫ d^4x tr( -1/(2g^2) F_μν F^μν ).

Note that in Euclidean space, the action comes with a + sign. This is to be contrasted with the Minkowski space action (5.1) which comes with a minus sign. We can write this as S_YM = ∫ d^4x tr(1/(4g^2) (F_μν ∓ ⋆F_μν)^2 ) ± ∫ d^4x tr(1/(2g^2) F_μν ⋆F^μν ) ≥ 8π^2 |n| / g^2, where, in the last line, we’ve used the result (5.29). We learn that in the sector with winding n, the Yang-Mills action is bounded by 8π^2 n / g^2. The action is minimised when the bound is saturated. This occurs when F_μν = ± ⋆F_μν (5.31).

These are the (anti) self-dual Yang-Mills equations. The argument above shows that solutions to these first order equations necessarily minimise the action in a given topological sector and so must solve the equations of motion (5.30). In fact, it’s straightforward to see that this is the case since it follows immediately from the Bianchi identity D_μ ⋆F^μν = 0.

Solutions to the (anti) self-dual Yang-Mills equations (5.31) have finite action, which means that any deviation from the vacuum must occur localised in Euclidean spacetime. In other words, they are point-like objects in R^4. Because they occur for just an “instant of time” they are known as instantons.

There is much to say about instantons. You can read about the role they play in quantum Yang-Mills in the lectures on Gauge Theory and more about the structure of the solutions to (5.31) in the lectures on Solitons. For our purposes, it will suffice to point out that the contributions of instantons to any quantity comes with the characteristic factor e^{-S_instanton} = e^{-8π^2 |n| / g^2} e^{iϑ n} (5.32).

Famously, the function e^{-8π^2 / g^2} has vanishing Taylor expansion about the origin g^2 = 0. This is telling us that effects due to instantons are smaller than any perturbative contribution, which takes the form g^{2n}. Nonetheless, that doesn’t mean that instantons are useless since they can contribute to quantities that apparently vanish in perturbation theory.

The theta dependence e^{iϑ n} associated to an instanton is also interesting. It is a complex phase. The fact that it is complex can be traced to the ε^{μνρσ} tensor in S. This means that S contains a single time derivative and so, upon Wick rotation, still sits in the path integral with a factor of i. The fact that n ∈ Z means that ϑ is a periodic variable, with ϑ ∈ [0, 2π).

Instantons are usually referred to as non-perturbative effects. This is a little bit of a misnomer. The use of instantons requires weak coupling g^2 ≪ 1, so in this sense they are just as perturbative as usual perturbation theory. The name non-perturbative really means “not perturbative around the vacuum”. Instead, the perturbation theory occurs around the instanton solution.

This also means that the theta dependence (5.32) is only expected at weak coupling g^2 ≪ 1. As we’ve seen, in the far infra-red non-Abelian gauge theories are typically strongly coupled and the theta dependence of quantities can take a different form. We’ll see examples in what follows.

An Example: An Instanton in SU(2)

It is fairly straightforward to write down the instanton solutions with winding n = 1. For SU(2), such a configuration is given by A_μ = η^a_{μν} x_ν σ^a / (x^2 + ρ^2) (5.33).

Here ρ is a parameter whose role we will describe shortly. The η^a_{μν} are usually referred to as ’t Hooft matrices. They are three 4 × 4 matrices which provide an irreducible representation of the su(2) Lie algebra. They are given by η^1 = [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]], η^2 = [[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]], η^3 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]].

These matrices are self-dual: they obey 1/2 ε^{μνρσ} η^i_{ρσ} = η^i_{μν}. (Note that we’re not being careful about indices up vs down as we are in Euclidean space with no troublesome minus signs.) In the solution (5.33), the ’t Hooft matrices intertwine the su(2) group index a = 1,2,3 with the spacetime index μ and this implements the asymptotic winding of the gauge fields.

The associated field strength is given by F_μν = - 2ρ^2 η^a_{μν} σ^a / (x^2 + ρ^2)^2.

This inherits its self-duality from the ’t Hooft matrices: F_μν = ⋆F_μν and therefore solves the Yang-Mills equations of motion, D_μ F^μν = 0.

We can get some sense of the form of this solution. First, the non-zero field strength is localised around the origin x = 0. (By translational invariance, we can shift x^μ → x^μ - X^μ to construct a solution localised at any other point X^μ.) The solution depends on a par ameter ρ which can be thought of as the size of the instanton lump. The fact that the instanton has an arbitrary size follows from the classical conformal invariance of the Yang-Mills action.

6 Supersymmetric QCD

We now turn our attention to the quantum dynamics of supersymmetric gauge theories. Our focus will be on understanding the physics of super Yang-Mills and super QCD. There is, as we shall see, a wonderfully rich array of behaviour on display.

First, some basics. There are a number of facts that we’ve seen already in these lectures that we can combine to great effect in supersymmetric theories. First, we know that the gauge coupling runs 1/g²(µ) = - b₀ / (4π)² log(Λ²_UV / µ²)

where g² is the coupling constant evaluated at the cut-off scale Λ_UV. The general expression for the 1-loop beta function in non-supersymmetric theories is (5.7)

b₀ = (11/6) I(adj) - (1/6) Σ_f I(R_f) - (1/6) Σ_s I(R_s)

fermions scalars In supersymmetric theories this simplifies. Gauge bosons are necessarily accompanied by an adjoint Weyl fermion and chiral multiplets come in fermion/boson pairs. The upshot is that b₀ = (3/2) I(adj) - (1/2) Σ_chirals I(R) (6.1)

In the quantum theory, the running gauge coupling is replaced by the dynamical scale Λ, below which the non-Abelian gauge theory is strongly coupled. For reasons that will become clear shortly, we will refer to this as |Λ|. (It was always a real, positive energy scale so there’s nothing lost in doing this.) This was defined in (5.4) as |Λ| = µ exp(- 8π² / (b₀ g²(µ)))

It is RG invariant, meaning that Λ is independent of the scale µ.

Importantly, something novel happens in supersymmetric theories. This is because, as we have seen, the gauge coupling constant sits as the imaginary part of a complex coupling (4.18)

τ(µ) = ϑ/(2π) + 4πi / g²(µ) (6.2)

The theta angle does not run, essentially because it is a periodic variable ϑ ∈ [0,2π) and so has nowhere to go. This motivates us to define the complexified strong coupling scale Λ = µ exp(2πiτ(µ)/b₀) = |Λ| e^(iϑ/b₀) (6.3)

Recall from Section 3.3 that superpotentials are holomorphic in both fields and parameters. The complexified scale Λ is therefore crying out to sit in the superpotential. We’ll see many examples of this as we proceed.

The complexified scale also ties together two other ideas that we’ve encountered previously. First, when discussing what kinds of superpotentials can arise in a quantum theory in Section 3.3, we found it useful to think of a larger class of symmetries under which parameters also transform as so-called “spurions”. Of course, if a symmetry changes a parameter then it’s not a true symmetry of the theory but nonetheless we saw that these spurious symmetries can prove useful in restricting the kind of behaviour that can occur in supersymmetric theories.

Second, when discussing chiral anomalies in Section 5.2, we saw that a symmetry of the classical theory can fail to be a symmetry of the quantum theory by shifting the theta angle (5.26). In the supersymmetric context, a transformation of theta angle manifests itself as a complex rotation of Λ. This means that Λ acts as a spurion for anomalous U(1) symmetries. It also means that we can use anomalous symmetries to restrict the form of quantum corrections to a theory, just as we used other broken symmetries in Section 3.3. Again, we’ll see many examples of this as we proceed.

A Comment on Exact Beta Functions

There is an interesting, and somewhat subtle, story about higher order corrections to the beta function. We can write the one-loop correction in a more revealing way by inverting (6.3), τ(Λ;µ) = b₀ / (2πi) log(Λ/µ) (6.4)

Importantly, the periodicity of ϑ ∈ [0,2π) is manifest on both sides of this equation through ϑ → ϑ+2π ⇔ τ → τ +1 ⇔ Λ → Λe^(2πi/b₀)

Any corrections to (6.4) should retain this property. But that’s tricky to achieve while retaining the holomorphy implied by supersymmetry. The most general form of holomorphic corrections, consistent with the periodicity of ϑ, is τ(Λ;µ) = b₀ / (2πi) log(Λ/µ) + Σ_{n=1}^∞ a_n (Λ/µ)^(b₀n) (6.5)

for some unknown coefficients a_n. (The restriction to n > 0 comes from requiring that this is a weak coupling expansion and should not diverge as Λ → 0.) But these additional terms are proportional to e^(-8π²n/g²) and are identified as instanton effects (5.32). We see that all higher perturbative contributions vanish and, as far as perturbation theory is concerned, the beta function is one-loop exact.

The fact that the beta function is one-loop exact in supersymmetric theories is a striking statement. It appears to be even more striking when you actually compute the two-loop contribution and find that it doesn’t vanish! What’s going on?

The resolution is that one should be careful about what quantity is actually being computed. The holomorphic gauge coupling τ originates in a superpotential term ∫ d²θ τ W^α W_α such that 1/g² sits in front of the Yang-Mills action. The story that we told above assumes a renormalisation scheme in which this holomorphy is protected. Meanwhile, the physical gauge coupling is computed after a rescaling A → gA , so that the coupling now appears in vertices. But absorbing the gauge coupling into the gauge field in this way is not an entirely innocent thing to do and there is a price to pay in the form a Jacobian in the path integral. This means that while the holomorphic gauge coupling is one-loop exact, the physical gauge coupling can, and does, receive contributions at all loops. (It’s not dissimilar to our discussion in Section 3.3 where we saw that the physical parameters are renormalised even though the superpotential is not.) Nonetheless, it turns out that the one-loop exactness of the holomorphic gauge coupling puts strong constraints on the beta function for the physical gauge coupling which is known as the NSVZ beta function (after Novikov, Shifman, Vainshtein, and Zakharov). You can read more about these issues in the paper by Nima Arkani-Hamed and Hitoshi Muryama.

## 6.1 Super Yang-Mills

We will start our study of quantum dynamics with pure super Yang-Mills. The theory consists of a non-Abelian gauge field coupled to a single, adjoint Weyl fermion, S = ∫ d4x Tr[ -1/2g² F^μν F_μν - 2i λ σ^μ D_μ λ̄ + θ/(16π²) *F^μν F_μν ]

We will work with gauge group G = SU(N). The one-loop beta function (6.1) is b₀ = 3N_c and the theory flows to strong coupling at the scale |Λ|. The question that we want to answer is: what happens?

6.1.1 Confinement and Chiral Symmetry Breaking Our first port of call is to understand the global symmetries of the theory. Classically the theory has a U(1) symmetry, under which U(1) : λ → e^{iα}λ. This symmetry does not survive quantisation: it suffers an anomaly which can be viewed as a transformation of the theta angle U(1) : θ → θ + I(adj)α = θ + 2N_c α (6.6). Equivalently, we can think of the strong coupling scale (6.3) transforming as U(1) : Λ → e^{2iα/3}Λ. We say that Λ has R-charge R[Λ] = 2. As we’ve stressed repeatedly, the shift of θ means that U(1) is not a symmetry of the quantum theory.

However, all is not lost. We can see from (6.6) that a shift by α = 2π/2N_c transforms θ → θ + 2π. This means that a discrete Z_{2N_c} subgroup of the R-symmetry survives, rotating the fermion as λ → ωλ with ω^{2N_c} = 1. We learn that SU(N_c) super Yang-Mills has a discrete Z_{2N_c} R-symmetry.

Next we should start to understand the quantum dynamics. We don’t have enough control over the strong coupling physics of N = 1 supersymmetric theories to show from first principles that theory confines. (It turns out that we do have such control in theories with N = 2 supersymmetry.) We assume that, as with pure Yang-Mills, the theory confines with a mass gap. There is little doubt that this is correct.

Furthermore, as in non-supersymmetric QCD, a fermion bilinear forms ⟨Tr λλ⟩ ∼ Λ³ (6.7). This time supersymmetry does help us get a handle on this. We’ll see how as we proceed through this section and, in particular, will be able to pin down the dimensionless coefficient that sits in front of the right-hand side. But first let us understand the consequences of the condensate.

As in non-supersymmetric QCD, this condensate spontaneously breaks a symmetry. The difference is that in super Yang-Mills the condensate breaks our discrete R-symmetry, ⟨Tr λλ⟩ → ω² ⟨Tr λλ⟩. This, however, is a spontaneous breaking rather than an explicit breaking: the theory is invariant under Z_{2N_c} but the ground state is not. The discrete R-symmetry is broken to Z_{2N_c} → Z_2, where the surviving Z₂ acts as fermion parity λ → -λ. This is a subgroup of the Spin(1,3) Lorentz group and, as such, cannot be spontaneously broken.

When a continuous symmetry is spontaneously broken, we get massless Goldstone modes. When a discrete symmetry is spontaneously broken, we get multiple ground states. These ground states are characterised by the phase of the gluino condensate (6.7) which, in general, can take the form ⟨Tr λλ⟩ = a ω^{2k} Λ³, k = 0,1,...,N_c-1 (6.8) with ω = e^{πi/N_c} and a ∈ ℝ an undetermined coefficient. The upshot is that SU(N_c) super Yang-Mills has N_c distinct ground states that differ by the phase of the condensate (6.8).

Before we go on, it’s worth pointing out that the condensate takes the form Λ³ ∼ e^{-8π²/g² N_c} e^{iθ/N_c}. This isn’t of the form (5.32) expected from an instanton contribution. Roughly, it looks like the contribution from 1/N_c of an instanton! But we should acknowledge that the condensate arises in the strongly coupled regime of the theory and instantons are not a good guide to what’s going on.

So far we haven’t managed to figure out the overall constant a in front of the condensate. In non-supersymmetric theories, the equivalent calculation is not possible. But in supersymmetric theories it can be done, albeit with a fairly technical computation. Conceptually the idea is to deform the theory so that it is weakly coupled. We then compare the results.

compute the gluino condensate in that regime and argue, using holomorphy, that it remains unchanged as we move back. The end result is a = 16π2 (6.9)

There are (at least) two methods to get this result. One is to study the theory on R3 × S1 rather than R4. It turns out that the theory can be made weakly coupled when the S1 has radius R ≪ 1/|Λ|. Moreover, rather wonderfully, when placed on a circle instantons actually do fractionalise into N smaller objects and can be shown to generate the gluino condensate5. We’ll see another method to determine a = 16π2 later in these lectures.

6.1.2 The Witten Index There is another way to see the existence of N supersymmetric ground states. This is to compute the Witten index, defined in Section 3.4.2 as Tr(−1)F e−βH This counts the number of supersymmetric ground states of the theory, weighted with a sign.

The beauty of the Witten index is that it stays the same no matter what you do to the theory as long as you preserve supersymmetry. This means that if we can deform super Yang-Mills in some way so that the theory becomes weakly coupled, then we can just compute the Witten index using standard perturbative quantum field theory, safe in the knowledge that it can’t then change as we deform back to the strongly coupled regime that we care about. So the question becomes: how can we make super Yang-Mills weakly coupled?

The way to do this is fairly dramatic. We consider the theory on a spatial torus T3 and take the radius of each circle to be R, so that the volume is V = (2πR)3. We know5This calculation can be found in the paper by Davies, Hollowood, Khoze and Mattis. Bewarned: the computation of background determinants in this paper is incorrect, although the final answer is right.

that super Yang-Mills is weakly coupled in the UV, but flows to strong coupling at a scale |Λ|. If we take the spatial torus to be very small, so that R ≪ |Λ| then the RG flow never reaches strong coupling. Of course, the physics of the theory on such a tiny spatial torus is very different from the physics that we might care about. In particular, the size of space is now much smaller than the Compton wavelength of any massive particle so this is not going to be any good to compute, say, the S-matrix. But there’s one thing that we can compute and that’s the Witten index.

When we compactify space in this way, nearly all states will have an energy set by E ∼ 1/R. We can ignore these if we want to compute the number of ground states and focus only on those modes that, classically, have zero energy. These degrees of freedom come from both the gauge field and the fermions and we deal with each in turn.

On a torus T3, there are gauge configurations A that have vanishing field strength F = 0, but are nonetheless not gauge equivalent to the vacuum. These are parameterised by mutually commuting holonomies around each of the three different cycles U = TrP exp i A i = 1,2,3 i i where P is path ordering. We can use an SU(N) gauge transformation to diagonalise each of these, so that they read U i = diag(eiθ 1 i,...,eiθ N i c )

The zero energy modes are the coordinates θi, with i = 1,2,3 labelling the spatial directions and a = 1,...,N the gauge indices. Because U ∈ SU(N), these coordinates are not all independent but are constrained to obey Nc θa = 0 mod 2π (6.10)

a=1 We should quantise each of these periodic rotors θa, subject to this constraint. But this is essentially the same as the quantisation of a particle on a circle and we know that there is a unique ground state in which the wavefunction is independent of the θ’s. Physically, this can be understood because a non-zero momentum for θ corresponds to non-Abelian electric field F ̸= 0. This means that there’s no subtlety in quantising the gauge field and we get a unique ground state6.

6A different way to count ground states can be found in Witten’s original paper “Constraints on Supersymmetry Breaking”.

We’re left with the adjoint fermion. We impose periodic boundary conditions and the zero modes are simply the constant modes over the torus. We can again diagonalise the fermions by an SU(N) gauge transformation and write λ = diag(λ1,...,λNc)

α α α with α = 1,2 the spinor index. Each of these is a complex Grassmann mode. Because λ sits in the algebra su(N), these are constrained to obey Nc λa = 0 (6.11)

a=1 Let’s first recall what usually happens with such modes in quantum mechanics. A single Grassmann mode ψ has anti-commutation relations {ψ,ψ†} = 1 and gives rise to a qubit. This arises by first defining a fiducial state |0⟩ that obeys ψ|0⟩ = 0. The Hilbert space then consists of two states |0⟩ and ψ†|0⟩.

We can quantise the zero modes λa in the same way, except we have to make sure that the end result is gauge invariant. Diagonalising λ has already exhausted much of the gauge symmetry, but we’re still left with the Weyl group which permutes the λa. This means that any wavefunction must be invariant nt such permutations. We begin by again introducing a fiducial state that obeys λa|0⟩ = 0 for all α = 1,2 and a = 1,...,N. We can build zero energy excited states by acting with (λa)†, subject to the requirement of gauge invariance and (6.11). It’s straightforward to see that there is no such state where we excite just a single (λa)†: the requirement that it is invariant under permutations means that it has to take the form (cid:80) (λa)†|0⟩ but this vanishes by virtue of (6.10).

There is a single state with two (λa)† excited. We first construct the gauge invariant combination S = Trλλ = ϵαβλaλa and then build a ground state S†|0⟩. All gauge invariant states with more λ† excitations then arise by acting with further copies of S†. The end result is that there are N ground states, given by |k⟩ = (S†)k|0⟩ k = 0,...,N −1. The series ends at |N − 1⟩ because the Grassmann nature of λa, together with the constraint (6.10), means that (S†)Nc = 0.

Each of the states |k⟩ contains an even number of Grassmann operators and so contributes to the Witten index with the same sign. We learn that in the regime R ≪ 1/|Λ|, where the theory is weakly coupled, the Witten index of SU(N) super Yang Mills is given by Tr(−1)Fe−βH = N. But now we are at liberty to take R as large as we like, safe in the knowledge that the Witten index does not change. Indeed, the counting above agrees with the expectations from discrete chiral symmetry breaking (6.8), although the physics underlying these N states looks very different in the two regimes.

Other Gauge Groups: There is a similar story for other gauge groups G. The R-symmetry group of super Yang-Mills is Z_{2h}, where h is a group-theoretic quantity known as the dual Coxeter number. The value of h is shown for various groups G in Table 3. The fermionic condensate (6.7) then spontaneously breaks Z_{2h} → Z_2, giving h distinct vacua. Similarly, one can compute the Witten index on T3 to find the same result^7: Tr(−1)Fe−βH = h.

In fact, there is a further subtlety in the computation on T3. It turns out that the Witten index depends on the global structure of the gauge group meaning that, for example, the number of supersymmetric ground states for G = Spin(N) and G = SO(N) are different. You can read more about this in Yuji Tachikawa’s lecture notes.

6.1.3 A Superpotential: Later in this section we will derive Wilsonian effective actions for light degrees of freedom. But for super Yang-Mills there are no light degrees of freedom. The theory has a mass gap, with the lightest states having mass around ∼ |Λ|.

^7 The original Witten index paper contains a subtle mistake for Spin(N) gauge groups that was corrected by Witten in a subsequent appendix, with further elaborations in this paper.

Nonetheless, there is an interesting effective action that we can write down. It doesn’t involve any dynamical degrees of freedom and instead depends only the parameter Λ. We’ve already seen that the R-charge of this parameter is R[Λ] = 2/3 and the superpotential must have R-charge 2, which means that the only thing we can write down is W_eff = cΛ^3 (6.12), for some, as yet, undetermined constant c.

What’s the meaning of such an effective action when it doesn’t contain any dynamical fields? In fact, it’s just another way of capturing the gluino condensate (6.7). Here we explain why.

First, recall how we compute expectation values in the path integral. We add a source J(x) for the operator of interest. We then compute the path integral in the presence of the source Z[J] = ∫ D(fields)eiS_{SYM} exp i ∫ d^4x J Trλλ+h.c. (6.13). The expectation value is then given by ⟨Trλλ⟩ = ∂logZ/∂J |_{J=0}.

Now let’s go back to the original action for super Yang-Mills, written in terms of superfields (4.19) S_{SYM} = −∫ d^4x (iτ/8π) ∫ d^2θ TrW^αW_α +h.c. The lowest component of the chiral superfields is W_α = λ_αλ +.... But this means that a source for the gluino bilinear naturally arises if we promote the parameter τ to be a chiral superfield with its full complement of components τ = τ_τ + 2θψ +θ^2F_τ. The source appears as the F-term: J = F_τ/8π.

The low-energy effective action is what we get when we do the path integral, so Z[J] = eiS_eff. To write the effective action we again promote τ to a chiral superfield. There can be a complicated Kähler potential for τ but this doesn’t concern us. (It will give terms proportional to F_τ F_τ† but these will vanish when we set J = 0 in (6.13).) All we need for our purposes is the contribution to S_eff from an effective superpotential S_eff ⊃ ∫ d^4xd^2θ W_eff +h.c. = ∫ d^4x (∂W_eff/∂τ) F_τ +h.c.

The goal is to write down a W_eff that captures the right physics. Repeating the steps above, we have ⟨Trλλ⟩ = ∂S_eff/∂F_τ = 8πi ∂W_eff/∂τ.

this way, the effective superpotential is simply a device to encode the value of the gluino condensate.

With these path integral gymnastics under our belt, let’s now turn to the superpotential (6.12). As we’ve seen, it’s the only thing that we can write down consistent with the (anomalous) R-symmetry. In terms of τ it is

W_eff = cµ³ e^{2πiτ/Nc} ⇒ ⟨Trλλ⟩ = Λ³_eff

in agreement with our previous result (6.8). To match the normalisation (6.9), the coefficient c should be

c = N_c (6.14)

Note that W_eff hasn’t taught us anything new about the theory. In particular, there’s nothing to fix the coefficient c and we will have some work to do to make sure that it’s non-vanishing. However, it will turn out that W_eff will be useful in making contact with the results that we will derive from SQCD.

## 6.2 A First Look at SQCD

Now we add matter. We will consider supersymmetric QCD: SU(N_c) gauge theory coupled to N_f massless flavours. In superspace, the Lagrangian is

L_SQCD = Tr ∫ d²θ (iτ/(8π)) W_α W^α + h.c. + ∫ d⁴θ ∑_{i=1}^{N_f} (Φ_i^† e^{2V} Φ_i + ˜Φ_i^† e^{-2V} ˜Φ_i)

The action written in component fields can be found in (4.21).

Each flavour consists of two chiral multiplets, Φ in the fundamental representation N_c and ˜Φ in the conjugate representation N̄_c. The one-loop beta function (6.1) is

b_0 = 3N_c − N_f

For N_f ≥ 3N_c, the theory is non-renormalisable and infra-red free. Here the low-energy physics is easy. We want to understand what happens when N_f < 3N_c.

6.2.1 Symmetries The first step in understanding any quantum field theory is to get the symmetries nailed down. Let’s start with the classical symmetries. These are:

|       | SU(N_c) | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R' | |-------|---------|-----------|-----------|--------|--------|---------| | ϕ     | □       | □         | 1         | 1      | 1      | 0       | | ˜ϕ    | □       | 1         | □         | -1     | 1      | 0       | | ψ     | □       | □         | 1         | 1      | 1      | -1      | | ˜ψ    | □       | 1         | □         | -1     | 1      | -1      | | λ     | adj     | 1         | 1         | 0      | 0      | 1       |

Some obvious comments to make sure that we’re all on the same page. The first column denotes the SU(N_c) gauge symmetry; all others are flavour symmetries. For the non-Abelian symmetries, □ denotes the fundamental, □̄ denotes the anti-fundamental, and 1 means that it is a singlet.

(As an aside: the symmetries above are actually incomplete for N_c = 2 because the fundamental 2 is pseudoreal and so equivalent to the 2̄. This gives an enhanced SU(2N_f) symmetry. We won’t need this subtlety in what follows.)

Both U(1)_B and U(1)_A are flavour symmetries, as evidenced by the fact that the scalars and fermions in the same multiplet transform the same way. Meanwhile, U(1)_R' is an R-symmetry, meaning that the component fields in a chiral multiplet transform as

R[fermion] = R[boson]−1 (6.15)

We’ve called this symmetry U(1)_R' rather than U(1)_R for a reason that will become clear shortly. The choice of R[ϕ] = 0 is somewhat arbitrary since we could always define a new R-symmetry by combing it with any amount of the global A-symmetry. The important point is that the R-charge of the scalars ϕ and fermions ψ differ by 1. Note that the gluino λ always has charge +1 under the R-symmetry.

Not all the classical symmetries survive quantisation. U(1)_B is left unscathed as it is vector-like, but both U(1)_A and U(1)_R' suffer chiral anomalies. As we saw in (5.22), the current conservation equation becomes

∂_µ j^µ_A = Tr(F ⋆F_µν) / (32π²) with A = ∑_{fermions} q I(R)

where q is the charge and R the representation under SU(N_c). Again, it’s worth stressing that the complex scalars ϕ and ˜ϕ do not contribute to the anomaly. It is just the fermions that have this subtlety. For the two symmetries U(1)_A and U(1)_R', we have

A_A = N_f ×1 + N_f ×1 = 2N_f (6.16)

and

A_R' = N_f ×(−1) + N_f ×(−1) + 2N_c ×1 = 2(N_c − N_f)

However, we can form a linear combination of these currents that remains conserved. This is given by

R = R' + ((N_f − N_c)/N_f) A

This is an R-symmetry, rather than a flavour symmetry, because the chiral multiplet components still obey (6.15) and R[λ] = 1. (The convention of fixing the normalisation by insisting that R[λ] = 1 comes with the unhappy side effect that other charges are fractional.) We can now draw up a table of the true quantum symmetries of the theory:

|       | SU(N_c) | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_R     | |-------|---------|-----------|-----------|--------|------------| | ϕ     | □       | □         | 1         | 1      | N_f − N_c  | | ˜ϕ    | □       | 1         | □         | -1     | N_f − N_c  | | ψ     | □       | □         | 1         | 1      | −N_c       | | ˜ψ    | □       | 1         | □         | -1     | −N_c       | | λ     | adj     | 1         | 1         | 0      | 1          |

However, this misses some crucial information. This is because, as we’ve seen previously, it’s useful to keep the anomalous symmetry as a spurious symmetry. The full symmetry structure of the theory should be thought of as reinstating the anomalous U(1)_A, but with a transformation on Λ showing that it’s not a true symmetry of the theory:

|       | SU(N_c) | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R     | |-------|---------|-----------|-----------|--------|--------|------------| | Φ     | □       | □         | 1         | 1      | 1      | N_f − N_c  | | ˜Φ    | □       | 1         | □         | -1     | 1      | N_f − N_c  | | Λ^{b_0} | 1       | 1         | 1         | 0      | 2N_f   | 0          |

Some of the previous information is hidden in this table. In particular, the R-symmetry charge is that of the scalar component of the chiral multiplet and you have to remember that R[fermion] = R[boson]−1, together with the fact that R[λ] = 1. The final row shows how the anomalous symmetries act on Λ^{b_0} ∼ e^{iϑ}. We see that Λ^{b_0} transforms only under the anomalous U(1), with the charge given by (6.16). We’ll have cause to return to this table a number of times in what follows.

6.2.2 Runaway for N < N_{f c}

The dynamics of SQCD will depend crucially on the ratio N_{f} / N_{c}. We start with small number of colours N < N_{f c}. We already discussed the classical theory back in Section 4.3. The theory has a moduli space of vacua M parameterised by the N_{c}^2 gauge invariant, massless meson fields M_{i}^{j} = Φ \tilde{Φ}_{i}^{j}. At a generic point on the moduli space M, the gauge group is spontaneously broken to SU(N_{c}) → SU(N_{c} - N_{f}) (6.17). The mesons are neutral under SU(N_{c} - N_{f}) (otherwise they would break it further) so, at the classical level, we have massless SU(N_{c} - N_{f}) gauge bosons essentially decoupled from the massless mesons. We want to know what happens in the quantum theory.

We already know what will happen to the SU(N_{c} - N_{f}) gauge bosons: they will confine and get a mass. That leaves us with the mesons. It’s useful to start by asking: what could possibly happen? At the crudest level, the massless fields could remain massless, or they too could get a mass. If the latter happens, it would manifest itself in terms of a potential generated on the moduli space. And this potential would appear in the form of a superpotential. So we should check if it’s possible that quantum corrections generate a superpotential that lifts the moduli space.

Such a superpotential should be written in the terms of the low-energy meson fields and must respect the various symmetries of the problem. The meson field itself transforms in the (□,□) of SU(N_{f L}) × SU(N_{f R}), so to get something invariant we should consider detM. Under the remaining U(1) symmetries, the relevant charges are then

| U(1)_{B} | U(1)_{A} | U(1)_{R} | | detM | 0 | 2N_{f} | 2(N_{f} - N_{c}) | | Λ^{3N_{c} - N_{f}} | 0 | 2N_{f} | 0 |

Recall that the superpotential should have R-charge R[W] = 2 and must be neutral under U(1)_{A} and U(1)_{B}. There is a unique combination that is allowed by symmetries W_{eff} = C ( Λ^{3N_{c} - N_{f}} / detM )^{N_{c} - 1} / N_{f} (6.18)

with some coefficient underdetermined coefficient C = C(N_{c}, N_{f}).

We’ve learned that symmetries allow for a superpotential only of the specific form (6.18). But is it actually generated? In other words, is C ≠ 0? There is a general rule of thumb in quantum field theory that anything that isn’t prohibited by some symmetry or other principle always occurs. The superpotential (6.18) is constructed to be invariant under all symmetries. It is also physically sensible, with a positive power of Λ reflecting the fact that it could be generated by strong coupling effects. Indeed, it turns out that it is generated with the coefficient C(N_{c}, N_{f}) given by C(N_{c}, N_{f}) = N_{c} - N_{f} The result (6.18) is known as the Affleck-Dine-Seiberg, or ADS, superpotential. We’ll give an incomplete explanation of how to determine C(N_{c}, N_{f}) in Section 6.2.4.

Note that if we set N_{f} = 0, then the ADS superpotential agrees with our previous result (6.12) that captures the gluino condensate. However, when N_{f} ≥ 1, the superpotential W_{eff} is a function of dynamical fields M and tells us the fate of those fields.

First, let’s understand the physics of the superpotential W_{eff}. The moduli space of vacua is a large dimensional space but we can get a sense for what happens if we think of detM ∼ M^{N_{f}}. The superpotential is then W_{eff} ∼ M^{-N_{f}} / (N_{f} - N_{c}). If we ignore the Kähler potential, then the scalar potential takes the form V(M, M†) ∼ | ∂W_{eff} / ∂M |^2 → 0 as |M| → ∞

Figure 9. The runaway potential on the moduli space for N_{f} < N_{c} massless flavours.

This is rather striking behaviour. Classically we had an infinite number of vacua, forming the moduli space M. Quantum mechanically we have none! The potential is non-zero everywhere, asymptoting to V → 0 only as M → ∞ as shown schematically in Figure 9. This is known as a runaway potential. We have a quantum theory with no ground state. This is not something that we saw in non-supersymmetric QCD. Indeed, it should be clear that it arises in SQCD only because of the existence of massless scalars and their moduli space.

There are a number of caveats regarding the form of the potential, all deriving from the fact that we don’t have good control over the Kähler potential which, as we know from (3.29), affects the actual potential V(M). In some circumstances, it may well be possible that V(M) does not increase monotonically towards the interior of the moduli space but has some local, non-supersymmetric, minima at V(M) ≠ 0. If so, these would be metastable ground states, with some finite lifetime before tunnelling out and rolling down to infinity.

6.2.3 Adding Masses

The runaway behaviour arises for massless matter. What happens if we add a mass term? This arises from the addition of a superpotential to the our original theory, W_{mass} = m_{i}^{j} Q \tilde{Q}_{j}^{i} with m_{i}^{j} the mass matrix. (Sorry for the prolife ration of "M" variables. To remind you, M is the meson, m is the mass, and M is the moduli space!) We can always use the SU(N) symmetries to diagonalise the mass matrix m = diag(m ,...,m )

1 N However, in what follows we won't lose anything by considering a general m.

We care about the low-energy physics. We can again play the same game to determine the superpotential using symmetries and holomorphy. In addition to M and Λ, we now also have the mass matrix m. The transformation properties of the fields and parameters are SU(N) SU(N) U(1) U(1) U(1)

f L f R B A R M □ □ 0 2 2(N f −Nc)

Λ3Nc−N f 1 1 0 2N 0 m □ □ 0 −2 2Nc Again, we can ask: what possible superpotentials are consistent with the symmetry? The answer is that we can have any function W = f(x)

eff (Λ3Nc−N f /detM ) Nc− 1 Nf where f(x) is any holomorphic function of the unique holomorphic variable x that is invariant under all symmetries x = Tr(mM) (detM)^(1/(Nc−Nf)) / Λ3Nc−N We can pin down the function f(x) by taking various limits. In the limit m → 0 and Λ → 0, we must have f(x) = C + x so the superpotential is just the sum of the mass term and the dynamically generated superpotential (6.18), W = (N −N ) + Tr(mM)

eff c f (Λ3Nc−N f /detM ) Nc− 1 Nf But this limit encompasses all possible values of x, meaning that this is the exact superpotential.

What is the physics now? We can start by looking at the case N = 1 where there is just a single complex meson M = ΦΦ. The superpotential now has a critical point, ∂W/∂M = 0 ⇒ MNc = Λ3Nc−1 / mNc−1 This is an interesting result. First, there is now a supersymmetric minimum, with the potential sketched in Figure 10. Moreover, there are actually N such minima coming from taking the Nth root in (6.20). This is to be expected since it coincides with the Witten index for super-YangMills. As the mass m → 0, the minima move off to infinity in field space. In the opposite regime, |m| ≫ |Λ|, the flavour decouples and the theory reduces to super Yang-Mills.

Decoupling We can look more closely at what happens in the limit |m| ≫ |Λ|. For simplicity, we'll take m real in what follows. Clearly this theory should reduce to super Yang-Mills but, to make this precise, we need to be more careful about the strong coupling scales. In particular, when we try to decouple some heavy degrees of freedom like this, there are two strong coupling scales at play. This is because the running of the gauge coupling happens in two steps: • E > m: Here the gauge coupling runs with the beta function b = 3N −1 that is appropriate for N = 1 flavours. We have 0 c 1/g2(µ) = 1/g2 − (b0 / (4π)^2) log(Λ2 UV / µ^2)

If we continued this running to energies lower than m then we would hit strong coupling at a scale that we will call Λold = ΛUV e^(−8π^2/(b0 g0^2)) = me^(−8π^2/(b0 g2(m)))

where, in the second equality, we've used the fact that Λ is an RG invariant. This Λold is the scale Λ that appears in the formulae (6.19) and (6.20) above. However, when the chiral multiplets have a mass, it is better thought of as something of a counterfactual scale. The RG running never gets as low as Λold < m because something changes along the way ...

• E < m: Now the massive chiral multiplets decouple and no longer contribute to the beta function which becomes that of pure super Yang-Mills, with b′0 = 3Nc. We can continue the running of the gauge coupling with this new beta function, now starting at the scale m 1/g2(µ) = 1/g2(m) − (b′0 / (4π)^2) log(m^2 / µ^2)

Now it hits strong coupling at a scale that we will call Λnew = me^(−8π^2/(b′0 g2(m)))

This is the actual scale at which the gauge coupling becomes strong.

Comparing the two results above, we have the matching condition (Λold / m)^(b0) = (Λnew / m)^(b′0)

In principle there can be additional multiplicative factors that arise from the matching at scale m at higher loops. These go by the name of threshold effects. One can always choose a regularisation scheme in which they vanish.

The result (6.21) can be used generally. For our specific purposes, we decouple from the theory with N = 1 to pure super Yang-Mills, and this equation reads Λ3Nc−1 m = Λ3Nc old new In this case, Λnew > Λold. This is because the presence of matter slows the running of the coupling. When that matter is removed, the running speeds up and so raises the strong coupling scale.

We can now evaluate the formulae (6.19) and (6.20) in terms of the true, low-energy scale Λnew. First we determine the expectation value M in the vacuum (6.20). Then we substitute this into the superpotential (6.19) at the vacuum. A short calculation shows that W = N Λ3 eff c new This, of course, we've seen before. It is precisely the superpotential (6.12) for super Yang-Mills, now with the strong coupling scale Λnew. Even the coefficient (6.14) comes out correctly. In this way, the Affle Affleck-Dine-Seiberg superpotential correctly predicts the value of the gluino condensate in super Yang-Mills.

A General Mass Matrix

We can repeat the calculation above for \(N_f\) flavours and a general mass matrix \(m_{ij}\). We just need to find the critical point \[ \frac{\partial W_{\text{eff}}}{\partial M_{ij}} = 0 \]

of the superpotential (6.19). To do so, we should use Jacobi’s formula \[ \delta(\det M) = \text{tr}(\text{Adj}(M)\delta M) \tag{6.22} \]

with \(\text{Adj}(M)\) the adjugate matrix. If \(M\) is invertible then this coincides with the more familiar \(\delta(\det M) = (\det M)\text{tr}(M^{-1}\delta M)\). Assuming that \(M\) is indeed invertible, we find that the critical point obeys \[ M^i_j = (m^{-1})^i_j \left( \frac{\Lambda^{3N_c - N_f}}{\det M} \right)^{N_c - \frac{1}{2}N_f} \tag{6.23} \]

We take the determinant of both sides to find \[ \det M = \left( \frac{\Lambda^{3N_c - N_f}}{\det m} \right)^{N_c - \frac{1}{2}N_f} \quad \Rightarrow \quad M^i_j = (m^{-1})^i_j \left( \frac{\det m \, \Lambda^{3N_c - N_f}}{\det M} \right)^{1/N_c} \]

Again, we see that the vacua sit at a position inversely proportional to the mass, ensuring that they move off to infinity as \(m \to 0\). The \(N\)-th root on the right-hand side provides the phase ambiguity that gives rise to the \(N\) ground states expected from the Witten index.

6.2.4 The Potential at Weak Coupling

There is something special that happens when \(N_f = N_c - 1\). This is because, with this number of flavours, at a generic point on the moduli space \(M\) the gauge group is generically completely broken.

This is important. For any \(N_f < N_c - 1\), there is always a residual unbroken \(SU(N_c - N_f)\) non-Abelian gauge group which means that the theory is necessarily strongly coupled. However, for \(N_f = N_c - 1\) the theory can be weakly coupled.

However, weak coupling isn’t guaranteed. For simplicity, let’s consider the point on the moduli space where all scalars have the same expectation value (4.37), \[ \phi_i = \tilde{\phi}^{\dagger i} = \begin{pmatrix} v_a & \dots & 0 & 0 \\ \vdots & \ddots & & \vdots \\ 0 & \dots & v_a & 0 \end{pmatrix} \tag{6.24} \]

The Higgs mechanism halts the running of the gauge coupling at the scale \(v_a\) of breaking, so in the infra-red \(g^2 = g^2(v_a)\). This is small provided that \[ v_a \gg \Lambda \]

In other words, we can trust our weakly coupled intuition when we are far out on the \(N_f = N_c - 1\) moduli space, with \(|M| \sim v_a^2 \gg \Lambda\). This means that, in this regime, we should be able to compute the Affleck-Dine-Seiberg superpotential in some more traditional manner.

The form of the superpotential itself tells us where to look. When \(N_f = N_c - 1\), (6.18) becomes \[ W_{\text{eff}} = C_\star \frac{\Lambda^{2N_c+1}}{\det M} \tag{6.25} \]

with \(C_\star = C(N_c, N_c - 1)\). This is proportional to \(\Lambda^{b_0} \sim e^{-8\pi^2/g^2 + i\vartheta}\), which, as we saw in (5.32), is the characteristic signature of an instanton.

This gives a window of opportunity. Until now, our results for the quantum dynamics have relied on symmetries and, crucially, holomorphy. Supersymmetry, of course, bought us the latter. But this approach can only get us so far and, as we have stressed, there is nothing to fix the overall constant \(C_\star\). In particular, we need to check that it doesn’t vanish. This requires us to roll up our sleeves and do a weak coupling, instanton computation. And the theory with \(N_f = N_c - 1\) is the place to do it. The calculation is rather technical and we won’t describe it here\(^8\). But the result is \[ C_\star = 1 \]

Decoupling: From Weak to Strong Coupling

The single coefficient \(C_\star = 1\) for \(N_f = N_c - 1\) is sufficient for us to derive the coefficient \(C(N_c, N_f)\) for all other values of \(N_f < N_c\). We do this by decoupling arguments.

Let’s start with the theory with \(N_f = N_c - 1\) flavours. We will give a large mass \(m\) to \(k\) of these flavours. We then expect to flow down to the theory with \[ N'_f = N_f - (k + 1) \tag{6.26} \]

We want to derive the effective superpotential for this new theory.

\(^8\) The instanton calculation was first done by Affleck, Dine and Seiberg who showed that \(C_\star \neq 0\). The exact result \(C_\star = 1\) was first derived by Finnell and Pouliot.

Our starting point is the superpotential (6.19) for \(N_f = N_c - 1\)

\[ W = W_{\text{old}} + \text{Tr}(m M) \tag{6.27} \]

where now the coefficient \(C_\star = 1\) in front of the first term should be viewed as fixed by the weak-coupling instanton calculation. Note that we’ve added the subscript “old” to the strong coupling scale in anticipation of the fact that we will integrate out matter to flow to a new theory with \(N'_f\) flavours. We give a mass matrix of the form \[ m = \begin{pmatrix} 0 & 0 \\ 0 & \mathbb{1} \end{pmatrix} \]

The critical point \(\partial W / \partial M^i_j = 0\) solves, from (6.23), \[ m M = \frac{\Lambda_{\text{old}}^{2N_c+1}}{\det M} \mathbb{1} \tag{6.28} \]

We should pause to understand what this is telling us. The meson matrix \(M\) takes the form \[ M = \begin{pmatrix} \tilde{M} & 0 \\ 0 & Z \end{pmatrix} \]

where \(Z\) is a \(k \times k\) matrix and \(\tilde{M}\) is a \((N_c - k) \times (N_c - k)\) matrix. Note that the off-diagonal terms in \(M\) must vanish by the equation of motion (6.28).

At first glance, it looks tricky to solve the matrix equation (6.28) because of all those zeroes in the upper left corner of \(m\) make it difficult for the left-hand side to be equal to the identity matrix \(\mathbb{1}\). But the physics is actually clear. The massive \(k\) flavours in the matrix \(Z\) have an expectation value that’s stabilised as \(Z \sim 1/m\). Meanwhile, the remaining massless flavours in the matrix \(\tilde{M}\) have a runaway behaviour \(\tilde{M} \to \infty\) as we’ve seen before.

Here our interest is subtly different. We will in Integrate out the heavy degree of freedom Z. This means that we solve (6.28) only for Z and substitute it back in to get an effective action for M. This effective action will then tell us that M suffers a runaway, which we knew anyway. But our goal is only to find the overall coefficient C(N_c, N_f) in front of this runaway superpotential.

Focussing on the k × k part of (6.28) gives the matrix equation mZ = (Λ^{2N_c+1}_{old})/(det M det Z) 1_k.

Taking traces and determinants gives m Tr Z = Λ^{2N_c+1}_{old} / det M and (det Z)^{k+1} = (Λ^{2N_c+1}_{old})^k / (det M)^k m det Z.

If we substitute this back into the original superpotential (6.27), then we get a superpotential purely for the M mesons. It is W = (k + 1) (Λ^{2N_c+1}_{old} m^k / det M)^{1/(k+1)}.

From (6.26), we know that k + 1 = N_c - N_f'. Meanwhile, the kind of RG matching arguments that led us to (6.21) reveal that the numerator is the strong coupling scale associated to SU(N_c) with N_f' massless flavours Λ^{3N_c - N_f'}_{new} = Λ^{2N_c+1}_{old} m^k.

The upshot is that we reproduce the Affleck-Dine-Seiberg superpotential for the light meson fields as expected, W = (N_c - N_f') (Λ^{3N_c - N_f'}_{new} / det M)^{1/(N_c - N_f')}, but with the added bonus that we've derived the long-promised coefficient C(N_c, N_f) = N_c - N_f.

## 6.3 A Second Look at SQCD

We've seen that the moduli space of vacua is lifted for N_f < N_c. Now we look at what happens for higher N_f.

Our first observation is that the superpotential (6.18)

W = C_{eff} (Λ^{3N_c - N_f} / det M)^{1/(N_c - N_f)} is the only one allowed by the symmetries, regardless of N_f. But it makes no sense for N_f ≥ N_c. First, it clearly diverges when N_f = N_c. Moreover, for N_f < N_c < 3N_f it has negative powers of Λ, which means that the superpotential scales as e^{+1/g^2} (with some coefficient). But this diverges as g^2 → 0 and so isn't compatible with the weak coupling limit. In particular, we know that if we set g^2 = 0 then the theory is simply free and nothing can be going on. This rules out the possibility of a superpotential.

When N_f < 3N_c, the superpotential does have a positive power of Λ. But this corresponds to the situation where b < 0 and the theory is infra-red free and no superpotential can be generated. (Another way of saying this is that the putative strong coupling scale Λ is actually bigger than the UV cut-off and shouldn't be trusted.) We'll look at this theory in more detail below.

All of this means that for N_f ≥ N_c there is no possible superpotential that can arise. The moduli space of vacua survives and, correspondingly, there are necessarily massless degrees of freedom. Our goal is to understand them.

We will start in this section by looking at two special cases: N_f = N_c and N_f = N_c + 1. Both exhibit interesting phenomena. In later sections we'll then look at higher N_f.

6.3.1 A Deformed Moduli Space for N_f = N_c Recall that for N_f = N_c, the moduli space is parameterised by mesons M^i_j = Φ_j Φ̃^i and baryons B = ϕ^{a_1} ... ϕ^{a_{N_c}} ε_{a_1...a_{N_c}} and B̃ = ϕ̃^{a_1} ... ϕ̃^{a_{N_c}} ε_{a_1...a_{N_c}}.

These fields, gauge invariant composites, and parameters transform under the following symmetries:

|           | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R | |-----------|-----------|-----------|--------|--------|--------| | Φ         | □         | 1         | 1      | 1      | 0      | | Φ̃        | 1         | □         | -1     | 1      | 0      | | M         | □         | □         | 0      | 2      | 0      | | B         | 1         | 1         | N_c    | N_c    | 0      | | B̃        | 1         | 1         | -N_c   | N_c    | 0      | | Λ^{2N_c}  | 1         | 1         | 0      | 2N_c   | 0      |

The classical moduli space is defined as an algebraic variety, with a single constraint (4.42) between the fields det M - B̃B = 0. (6.29)

We know that this can't be lifted by a superpotential. But it turns out that the space is deformed. The quantum moduli space satisfies the constraint det M - B̃B = Λ^{2N_c}. (6.30)

There are a number of questions that spring to mind. First, what is the meaning of this deformation? And second, how do we know that it happens?

Let's start by answering the first of these. The mathematics is all about the singularities of the space, the physics all about their meaning. We can start by looking at a much simpler example. Consider the algebraic variety defined by xy = 0 with x, y ∈ ℂ. This is obviously the intersection of two complex lines. (The complex line, or often just "line" is the name given by algebraic geometers to what you used to think of as a plane.) The space is obviously singular at the origin x = y = 0. The way to see this mathematically is to look at the tangent vectors, δx and δy. These obey δx y + x δy = 0. (6.31)

For any point other than the origin, there is a unique complex tangent vector. For example, if x ≠ 0 then the tangent vector is δx since we necessarily have δy = 0. But at the origin there is no constraint on δx and δy which is telling us that the tangent vector is ill-defined and, correspondingly, 空间是奇异的。我们可以将此与变形后的空间 xy = ϵ² 进行比较。这是一个复一维空间，且在远离原点处看起来与 xy = 0 非常相似。但原点 x = y = 0 不再属于这个空间，这意味着奇异性现在被消除了。切向量仍必须满足 (6.31)，但现在对于满足 xy = ϵ² 的每个点，存在唯一的切向量。奇异空间和变形后的空间如图 11 所示。

这个简单的例子捕捉了模空间 M 的关键特征。经典模空间 (6.29) 是奇异的。这在原点 M = B = \tilde{B} = 0 处显然成立，但更普遍地说，在任意 B = \tilde{B} = 0 且介子矩阵满足 rank(M) ≤ N − 2 的子流形上，它都是奇异的。相比之下，量子模空间 (6.30) 是光滑的。所有奇异性都已被消除。这告诉我们什么？

正如我们在第 4.3 节众多示例中所见，模空间中的奇异性意味着存在新的无质量自由度。在当前情况下，这并不神秘：新的无质量自由度是规范玻色子。特别是，当 rank(M) = k ≤ N − 2 时，一个 SU(k) 规范群未被破缺。

但这些奇异性在量子理论中被消除了。这告诉我们，在模空间原点处那些经典上无质量的额外粒子，现在已经获得了质量。这就是著名的质量间隙问题！在这里，我们看到一个复杂的量子效应——即规范玻色子通过强相互作用获得质量——以一种令人惊讶的几何方式出现了。

现在回答第二个问题：我们如何知道模空间发生了量子变形？首先要注意的是，它与对称性是一致的，而且正如我们之前指出的，任何未被禁止的事情通常都会发生。当然，你可能没有意识到通过量子效应变形约束甚至是一种可能发生的事情，但上面关于消除奇异性意义的讨论希望能消除此类疑虑。然而，我们应努力寻找比这更有说服力的证据。事实上，有两个非常令人信服的理由相信变形确实发生了。

6.3.2’t Hooft反常匹配

我们描述的由量子修正约束所刻画的物理图像，假设了唯一的无质量自由度是介子和重子。这个图像必须满足许多有趣的约束条件。这些约束来自于’t Hooft反常。

理论的原始全局对称性是 G = SU(N)_F × SU(N)_L × SU(N)_R × U(1)_B × U(1)_R。在量子模空间的每个点上，’t Hooft反常必须匹配。在不同的点上，全局对称性破缺到某个子群 G → H，并且当我们绕 M 移动时，这个存活的子群 H 会变化。但重要的是，完整全局对称性 G 将完全未被破缺的点 M = B = \tilde{B} = 0 已被量子变形 (6.30) 移除。然而，存在两个点，其中存活的对称性 H 是最大的，反常匹配也最为严格。它们是

• B = \tilde{B} = 0 且 M = Λ²_{1/N_c}。在该点，存活的全局对称群是 H = SU(N)_{F_{diag}} × U(1)_B × U(1)_R (6.32)。这与非超对称 QCD 中的手征对称性破缺模式并无不同。

• M = 0 且 \tilde{B} = B = Λ^{N_c}。在该点，存活的全局对称群是 H = SU(N)_F × SU(N)_f × U(1)_R (6.33)。这是一种我们认为在非超对称 QCD 中不会发生的对称性破缺模式。非阿贝尔手征对称性未被破缺，但相比之下，重子数被破缺了。

我们现在依次在每个点进行反常匹配。接下来的内容中，我们将频繁参考本小节开头构建的对称性表格。

B = \tilde{B} = 0 的点

我们需要匹配 (6.32) 中给出的 H 的对称性反常，以及对称性之间的任何混合反常。我们将依次处理，首先从非阿贝尔 SU(N)_{F_{diag}} 对称性开始。

SU(N)³_{F_{diag}} ：在紫外区，我们有夸克 ψ 和 \tilde{ψ}。但它们对反常的贡献相互抵消，给出 A_{UV} = 0。在红外区，只有介子携带非阿贝尔电荷。在对角 SU(N)_{F_{diag}} 下，它按 □ ⊗ □ = adj ⊕ 1 变换。但伴随表示是实表示，不贡献反常，所以我们有 A_{IR} = 0。

SU(N)²_{F_{diag}} · U(1)_B ：在紫外区，夸克 ψ 和 \tilde{ψ} 携带相反的 U(1)_B 电荷，因此它们的贡献相互抵消，给出 A_{UV} = 0。在红外区，介子费米子不带 U(1)_B 电荷，所以也给出 A_{IR} = 0。

SU(N)²_{F_{diag}} · U(1)_R ：这更有趣一些。我们需要记住，表格中列出的电荷是手征多重态中玻色子的电荷，其中 R[费米子] = R[玻色子] − 1。在紫外区，我们有 A_{UV} = N_c × I(□) × (−1) + N_c × I(□) × (−1) = −2N_c，其中的 N_c 因子是因为每个夸克有 N_c 种颜色。同时，在红外区，费米介子的贡献是 = I(adj)×(−1) = −2N IR f Now there is no contribution from colour degrees of freedom because the mesons are confined. Instead there is only the SU(N ) group theory factor I(adj). Nonetheless, f diag we have A = A because we are working in the theory with N = N .

UV IR f c

U(1)2 ·U(1) : In the UV, the quarks contribute B R A = N N ×(+1)2 ×(−1)+N N ×(−1)2 ×(−1) = −2N N UV c f c f c f

In the IR, only the fermionic baryons contribute. These give A = (N )2 ×(−1)+(−N )2 ×(−1) = −2N2 IR c c c

Again, A = A .

UV IR

U(1)3: This time we have to remember that there are N2 − 1 gluinos with charge R c R[λ] = +1 in the UV. These didn’t contribute to any of the anomalies above, but they do now. Including both gluinos and quarks, we have A = (N2 −1)×(+1)3 +N N ×(−1)3 +N N ×(−1)3 = N2 −2N N −1 UV c c f c f c f c

In the IR, both mesons and baryons contribute to the anomaly, all with R-charge −1.

This is the first time that all the IR fields contributed and this means that it’s the first time we need to take into account the constraint (6.30). This is a constraint not just on the expectation values, but also on the fluctuations of the fields. This means that the number of massless IR fields is dimM = N2 +2−1 with the +2 the baryons B and B and the −1 coming from the constraint. The upshot is that the IR anomaly is A = dimM×(−1)3 = −N2 −1 IR f

Again, we see the anomaly matches with the UV.

There are two remaining anomalies, U(1)3 and U(1)2 ·U(1) . You can check that B R B both have A = A = 0 because U(1) is vector-like.

UV IR B

In addition, we can match mixed U(1)-gravitational anomalies. This simply means that the sum of U(1) charges must be the same in the UV and IR. However, in the present case these don’t really give anything new. For U(1) , we have ∑ q = 0 in both B B UV and IR. For U(1) all charges are q = ±1 so ∑ q = ∑ q3 and this reduces the R R R R U(1)3 calculation that we did above. When we consider other theories the matching of mixed gauge-gravitational anomalies will give more compelling results.

The Point with M = 0

We now need to match anomalies for H given in (6.33). The only real difference from the calculation above lies in the SU(N )3 anomaly. In the UV, just the quarks ψ f L contribute and give A = N ×A(□) = N UV c c

In the IR, the N2 mesons contribute. We have A = N ×A(□) = N IR f f

Again, A = A because we’re working in the theory with N = N . The anomaly UV IR f c matching for SU(N )2 ·U(1) works in much the same way, giving A = A = −N .

f L R UV IR c

The anomaly matching for U(1)3 works in the same way as we saw above.

The calculations of anomaly matching are straightforward. But the agreement is not entirely trivial. In particular, it’s clear that it works only when N = N . As we f c proceed, we’ll see anomaly matching working in more intricate ways.

Decoupling

There is a second way to see the need for the quantum deformation of the moduli space.

This uses a trick that we’ve seen before: we look at the fate of the theory when we give one flavour a mass and decouple it.

It’s not immediately obvious how to do this since, as we saw above, we don’t have a superpotential to start with! The trick is to view the constraint (6.30) itself as a superpotential W = X detM −B ˜B −Λ2Nc where we’ve introduced a new chiral superfield X whose sole role is to act as a Lagrange multiplier, imposing the constraint. We now add a mass for just one flavour. The superpotential is Wold = X detM −B ˜B −Λ2Nc + Tr(mM) (6.34)

We’ve added the superscript “old” because we’re playing an integrating out game. We’re going to look at what happens when |m| ≫ |Λold| so that we have one massive flavour and N = N −1 massless flavours. In this case, we should be able to f c re-derive the appropriate Affleck-Dine-Seiberg superpotential. Let’s see how it works.

The rest of the calculation is very similar to the decoupling that we saw in previous sections. The critical point for the mesons sits at ∂W/∂Mi = 0, or mM = −X detM 1 (6.35)

If we turn on a mass term for just the final Nth flavour, with m = diag(0,...,0,m).

The meson fields take the form M = M 0 0 Z with Z = Mff the final flavour and the off-diagonal terms set to zero at the critical point (6.35). The equation arising from ∂W/∂Z in (6.35) tells us that X = − detM

Meanwhile, the critical points for B and ˜B are ∂W = −XB = 0 and ∂W = −B ˜X = 0 ∂B ∂ ˜B which, since X ̸= 0, means that we must have B = ˜B = 0. So far Z is undetermined, but this is fixed by the equation of motion for X which, of course, is simply the constraint itself. It now reads Z det ˜M = Λ2Nc old

We now substitute this back into the superpotential (6.34). Only the final Tr(mM) = mZ term contributes and gives W = Λ2Ncm old = Λ2Nc+1 new det ˜M det ˜M with the now familiar RG matching giving Λ2Nc+1 = Λ2Ncm old. This we recognise as the Affleck-Dine-Seiberg superpotential (6.25) in the case N = N − 1 (with even The coefficient correct). Notice that the quantum deformation of the constraint was necessary for us to reproduce the known physics when we integrate out massive flavours. This is our first piece of evidence (beyond the symmetries) that the deformation actually occurs.

6.3.3 Confinement Without χSB for N_f = N_c + 1 The case of N_f = N_c + 1 also exhibits some rather startling behaviour and is worth exploring in some detail. Recall from Section 4.3 that, in addition to the mesons M^i, we now have N_f baryons of each type B_{i1...iN_c} = ε_{i1...iN_c i} and ˜B^{j} = ε^{j i1...iN_c} ˜B_{i1...iN_c}.

This satisfy the constraints (4.43)

Adj(M)^i_j = B^i ˜B_j and M^i_k B^k_j = M^i_k ˜B^{k} = 0 (6.36)

Recall that if the adjugate matrix Adj(M) is invertible then it is given by Adj(M) = (det M) M^{-1}. We can gather the various gauge fields together to list their symmetries in a now-familiar table

|        | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R | |--------|-----------|-----------|--------|--------|--------| | Φ      | □         | 1         | 1      | 1      | 1      | | ˜Φ     | 1         | □         | -1     | 1      | 1      | | M      | □         | □         | 0      | 2      | 2      | | B      | □         | 1         | N_c    | N_c    | N_c/N_f| | ˜B     | 1         | □         | -N_c   | N_c    | N_c/N_f| | Λ^{2N_c-1} | 1   | 1         | 0      | 2N_f   | 0      |

As we’ve already seen, there can be no superpotential generated on the moduli space. But, this time, there can be no quantum deformation of the constraints either! There is no possibility consistent with the symmetries and various weakly coupled limits. Our quantum moduli space has singularities.

What are we to make of this? As we’ve seen in several examples, the singularities signify new massless degrees of freedom. Classically, these degrees of freedom are gauge bosons. It’s tempting to conclude that the singularities in the quantum theory are telling us that the gauge bosons are free at the origin of the moduli space. However, it turns out that this is not the case. Instead, the quantum interpretation of the singularities is rather different.

In fact an obvious quantum interpretation suggests itself if we assume that the theory confines. This means that the low-energy fields are necessarily mesons and baryons which, in general, are constrained by (6.36). Geometrically, the singularities of M arise when the fluctuations of M, B and ˜B are no longer restricted to lie on M. Physically, this translates into the suggestion that the singularities of M might be due to unconstrained mesons and baryons. In particular, it would suggest that at the origin of moduli space M = B = ˜B = 0, we should think of the physics as described by free, massless mesons and baryons.

This interpretation of the singularity is rather remarkable, not least because we would have confinement without the accompanying chiral symmetry breaking. At the origin of moduli space, the full chiral symmetry G = SU(N_f)_L × SU(N_f)_R × U(1)_B × U(1)_R is unbroken. Famously, confinement without chiral symmetry breaking is not possible in QCD. (We sketched the argument in Section 5.2.3.) The suggestion is that this does happen in SQCD with N_f = N_c + 1.

The phenomenon of confinement without chiral symmetry breaking in SQCD sometimes goes by the name of s-confinement. It’s a rubbish name. Here “s” can stand for “smooth” or perhaps “screening” depending on taste.

More ’t Hooft Anomaly Matching There is a fairly stringent test that any proposal for confinement without chiral symmetry breaking must pass. This is ’t Hooft anomaly matching. Let’s see how we do.

SU(N_f)^3: In the UV, we have the quarks contributing to give A = N_c. In the IR, we have both mesons M, which contribute N_f and the baryons B which contribute -1 as they sit in □. Together they give A = N_f - 1 = N_c.

SU(N_f)^2 · U(1)_B: The quarks give A = N_c. In the infra-red, the mesons don’t contribute while the baryon B gives A = N_c.

SU(N_f)^2 · U(1)_R: Now things get more fiddly, largely because of the fractional R-charges. In the UV, the quarks give A = N_c (1 - 1/N_f) = - N_c^2 / (N_f (N_c + 1))

In the IR, both the meson and baryon contribute: A = N_f (2 - 1/N_f) + (-1)(2N_c/N_f - 1)

A little algebra reassuringly shows that A_UV = A_IR.

The remaining anomaly matching involving U(1)_R gets a little messy. For example, we have

U(1)_R: The mixed U(1)_R gravitational anomaly simply requires that we add up the R-charges. Including the gluinos, we have A_UV = (N_c^2 - 1) + 2N_c N_f (1 - N_c/N_f) = -N_c^2 + 2N_c - 2 Meanwhile, A_IR = (N_f^2 - 1) + 2N_f N_c (1/N_f - 1) = A_UV

U(1)_R^3: The calculation is the same as above, but with R^3 instead of R. We have A_UV = (N_c^2 - 1) + 2N_c N_f (1 - N_c/N_f)^3 = - (N_f^4 - 6N_f^3 + 12N_f^2 - 8N_f + 2) / N_f^2 Meanwhile, A_IR = (N_f^2 - 1) + 2N_f N_c (1/N_f - 1)^3 Again, we find A_UV = A_IR.

By now, you won’t be surprised to hear that all other ’t Hooft anomalies also match. The messier the computation, the more compelling the evidence. It certainly feels like there is something deep going on when these complicated algebraic expressions are found to agree.

Decoupling For N_f < N_c, we built up an impressive pattern of consistency, understanding how our new results can be used to imply our e Earlier ones. We can do this again here. But there’s a curious lesson awaiting us. You might think that we should impose the constraints (6.36) by introducing a bunch of Lagrange multipliers. This, it turns out, doesn’t work. Instead the constraints arise in a slightly different way. To see this, note that the symmetries allow us to introduce the superpotential

W = - det M - B M B (6.37)

Λ^{2N_c-1}

Using Jacobi’s formula (6.22), equations of motion from this superpotential are (ignoring the overall factor of Λ^{2N_c-1} for now)

∂W / ∂B = M B~ = 0, ∂W / ∂B~ = B M = 0, ∂W / ∂M^{i}_{j} = - Adj(M)^i_j + B^i B~_j = 0.

The upshot is that the superpotential (6.37) gives the constraints (6.36) as the equations of motion, rather than through a Lagrange multiplier. This, it turns out, is the way the constraints should be imposed when N = N_f + 1.

This is a much softer way to implement constraints. A Lagrange multiplier imposes a constraint absolutely in the path integral. In contrast, the classical equations of motion are merely a gentle suggestion that, at weak coupling, certain configurations carry more weight in the path integral. Presumably this is related to the fact that the unconstrained mesons and baryons manifest themselves at the origin.

There is one further unusual aspect of (6.37) and that’s the negative power of Λ. In previous sections, we discarded some possible superpotentials on the grounds that they scale as e^{+1/g^2} (with some appropriate exponent) and so didn’t reproduce our weak coupling needs. But in this case the constraints are classical constraints and the classical limit g → 0 simply imposes them more strenuously. So there’s nothing to be concerned about.

We know the deal by now. We introduce a mass for the last flavour, so the superpotential reads

W = - det M - B M B + Tr(m M) (old)

Λ^{2N_c-1}

with m = diag(0,...,0,m). The critical point of the meson now sits at

det M - B M B~ = Λ^{2N_c-1} m M (6.38) (old)

The meson and baryon fields can be shown to take the form,

M = diag(M, 0), B^i = (0, B), B~_i = (B~, 0)

with Z = M the final flavour. The constraints B M = M B~ = 0 tell us that Z = 0 if B, B~ ≠ 0. But we should still impose the equation of motion. And, indeed, Z drops out of the equation (6.38) which becomes

det M - B~ B = m Λ^{2N_c-1} = Λ^{2N_c} (new)

This, of course, is the quantum modified constraint (6.30) of the theory with N = N_f.

## 6.4 A Peek in the Conformal Window

At this point, we will jump to the other end of the flavour spectrum. We know that SQCD is no longer asymptotically free when N_f ≥ 3N_c. In this situation, the low-energy physics is easy: it is just weakly interacting gluons, gluinos and massless (s)quarks. What if we now lower N_f slightly below the asymptotic freedom bound. Here, too, the physics is well understood. This is for the same reason that we saw in non-supersymmetric QCD: there is a zero of the beta function at weak coupling where we trust the calculation. This is the Banks-Zaks fixed point. The argument holds for SQCD just as it does for normal QCD.

Now let’s lower N_f still further. The expectation is that we will continue to flow to an interacting conformal field theory for some range of N_f, presumably with a different CFT for each N_f and N_c. The question is: how low can N_f go? We don’t know the answer in the non-supersymmetric case. But it turns out, we do know the answer for SQCD. We flow to an interacting conformal field theory in the regime

3 N_c / 2 < N_f < 3 N_c (6.39)

This is the conformal window.

Obviously we should ask how we know the lower bound of the conformal window. This, it turns out, follows from certain properties of supersymmetric conformal field theories. In the rest of this section we will state these properties, although we won’t derive them. Then, in Section 6.5, we’ll turn to the outstanding question of what happens in the gap between N_f = N_c + 1 and the conformal window at N_f > 3N_c/2.

6.4.1 Facts About Conformal Field Theories

A conformal field theory (or CFT) describes the dynamics of interacting massless particles. Its defining feature is that it is invariant under scale transformations, also known as dilatations, x^μ → λ x^μ. Such a scaling would be broken by any dimensionful parameter, such as a mass, which is one way of seeing that conformal field theories can only describe massless excitations. Any relativistic, scale invariant theory appears to also enjoy a more dramatic additional symmetry known as special conformal transformations. This acts as

x^μ → (x^μ - a^μ x^2) / (1 - 2 a·x + a^2 x^2)

In d = 1 + 1 dimensions, there is a proof that scale invariance implies conformal invariance. In higher dimensions, the proofs are not complete but, nonetheless, it is thought to be true in any interacting conformal field theory. The generators of dilatations D and of special conformal transformations K take the form

D = -i x^μ ∂_μ, K_μ = -i (2 x_μ x^ν ∂_ν - x^2 ∂_μ)

They combine with the usual generators of the Poincaré algebra to form from the conformal algebra, which has the additional commutation relations [D,Kµ] = −iKµ, [D,Pµ] = iPµ [Kµ,Pν] = 2i(Dηµν −Mµν)

[Mµν,Kσ] = i(Kνηµσ −Kµηνσ)

The kinds of questions that we want to ask about conformal field theories are somewhat different from what we’re used to. We no longer care about the masses of particles because they’re all zero. Nor do we usually care about the S-matrix which is challenging to define in a theory of massless particles where there can be arbitrarily low energy excitations of increasingly long wavelengths.

Instead, in a CFT we care about correlation functions. In particular, we care about scaling dimensions. This means that we want to find operators O(x) that have the nice property O(λx) = λ−∆O(x)

with ∆ the scaling dimension. If we then look at the two-point function of these operators, we necessarily have ⟨O†(x)O(0)⟩ ∼ |x|2∆ These scaling dimensions are closely related to the critical exponents that were the focus in the lectures on Statistical Field Theory.

It’s useful to look to a free, massless scalar field as an example of a trivial CFT. Here the theory is described by the action S = ∫ ddx ∂µϕ∂µϕ The scaling dimension of ϕ coincides with what we often call the “engineering dimension”, or sometimes just “dimension”. It is ∆[ϕ] = d−2 We don’t have Lagrangian descriptions for interacting CFTs. The closest we can get is to write down the Lagrangian for a field theory in the UV that flows, in the IR, to an interacting CFT. This, for example, is what happens in massless (S)QCD with a suitable number of flavours. It may be that the resulting CFT is weakly coupled, such as for a Banks-Zaks fixed point, in which case we can compute the scaling dimensions ∆ perturbatively. Or it may be that resulting CFT is strongly coupled, in which case we need to turn to some other method. Other methods on the table include numerics, the ϵ expansion that we met in Statistical Field Theory, an approach known as the bootstrap and, as we will see, supersymmetry.

There is one important result that we will need. The interactions always serve to increase the scaling dimension. Or, said more precisely, the dimension of any scalar operator in a unitary, interacting CFT is bounded by ∆[O] ≥ d−2 This is known as the unitarity bound10. In the language of perturbative quantum field theory, this is telling us that the anomalous dimensions of operators are always positive. 10It is not too difficult to derive this bound. The key step is to quantise the theory on S3×R where we get to use the so-called state-operator map that relates local operators to states in the Hilbert space. Then you simply require the positivity of an arbitrary state |P Pµ|ϕ⟩|2 > 0 and the unitary bound follows after a few commutation relations using the conformal algebra. What is more challenging is to show that there is not a more stringent bound coming from some other requirement. You can find details in the excellent Lectures on Conformal Field Theory by Joshua Qualls.

In addition, any operator that saturates the bound corresponds to a free field. This means that it must decouple from everything else that’s going on in the theory.

Conformal field theories are of interest in many dimensions d. But our interests lie strictly in d = 3+1. The unitarity bound reads ∆[O] ≥ 1 (6.40)

Any operator with ∆[O] = 1 is free.

Perturbing Conformal Field Theories

Suppose that you sit at a conformal fixed point. As we mentioned above, typically there’s no action that can describe these dynamics directly but, for the sake of discussion, it will be useful to pretend. So lets call it SCFT. (If you’re worried about this, it’s better to think in terms of a partition function in the presence of sources.)

Now we perturb the CFT. We do this by adding an extra term to the action. This extra term is some operator O(x) which, if you’re in the setting of Lagrangian field theory, would be some combination of fields. The new action is S = SCFT + λ ∫ ddx O(x)

with λ the coefficient that governs the perturbation. The question is: what happens next?

The answer to this depends on the dimension ∆[O]. Roughly speaking, there are three possibilities • ∆ < d: Such perturbations are called relevant. They change the dynamics in the infra-red and should be thought of as initiating an RG flow from our original CFT to somewhere else. An example is a mass term for a free, massless scalar field. In this case, the end point is a gapped theory. However, it’s not true that a relevant deformation always pushes us to a gapped phase. We may, instead, flow to a different CFT.

• ∆ > d: These perturbations are irrelevant. They don’t change the low-energy dynamics of the CFT. An example is a ϕ6 interaction in d = 3+1 dimensions: it is important at high energies, but is insignificant at low energies.

• ∆ = d: These perturbations are called marginal. This arises when the parameter λ is dimensionless.

Now things are a little more subtle. Typically, once you deform the theory by an arbitrarily small, marginal perturbation perturbation, then the dimension of λ changes and runs under RG. It may become smaller as you flow to the IR and such perturbations are said to be marginally irrelevant. This happens, for example, for a ϕ4 deformation or Yukawa terms in d = 3+1. Alternatively, the perturbation may grow stronger as you flow towards the IR as is the case for the coupling constant of Yang-Mills. Such perturbations are said to be marginally relevant. Alternatively, it may be that λ doesn’t run at all under RG. In this case it is said to be exactly marginal and it means that we have a line of different conformal field theories, parameterised by λ. This situation is rare, but does occur for certain supersymmetric conformal field theories.

6.4.2 Facts About Superconformal Field Theories When a theory with N = 1 supersymmetry flows to an interacting conformal fixed point, it gives rise to a superconformal field theory (or SCFT). In addition to the supercharges Qα and Q̄α̇ there are now superconformal charges Sα and S̄α̇. Importantly, SCFTs necessarily have a U(1) symmetry. Recall that this was somewhat optional in ordinary quantum field theories. For example, U(1) is anomalous in super Yang-Mills and this is reflected in the transformation of the strong coupling scale Λ. But in an SCFT U(1) is not an option. These theories always have an R-symmetry. The N = 1 superconformal algebra augments the conformal algebra with the Grassmann generators. There are commutators [D, Qα] = ½ Qα, [D, Sα] = −½ Sα [R, Qα] = Qα, [R, Sα] = −Sα [Kµ, Qα] = iσµαα̇ S̄α̇, [Pµ, Sα] = iσµαα̇ Q̄α̇ and anti-commutators {Qα, Q̄α̇} = σµαα̇ Pµ, {Sα, S̄α̇} = 2σµαα̇ Kµ {Qα, Sβ} = Mµν σµναα̇ − i(D − ¾R) ϵαβ

Now there is a slight twist to the unitarity bound. The fact that the R-symmetry and dilatation operator sit within the same algebra means that there is a rather remarkable relation between them. It can be shown that the dimension of any operator is bounded by its R-charge ∆[O] ≥ ³⁄₂ |R[O]|.

Furthermore, chiral operators necessarily saturate this bound. Any chiral superfield Φ has ∆[Φ] = ³⁄₂ R[Φ] (6.41)

while any anti-chiral superfield Φ̄ has ∆[Φ̄] = −³⁄₂ R[Φ̄].

This is an extraordinarily powerful result. Usually in conformal field theories (at least in dimension d > 2) the scaling dimensions are extremely difficult to compute. And this remains true for most operators in a superconformal field theory. But there are a special class of operators – those described by chiral superfields – where the scaling dimension is trivial to compute. We just need to know its R-charge.

There is a way to get a feel for the factor of 3/2 in (6.41). Consider the Wess-Zumino model with W(Φ) = λΦ³, which leads to a V(ϕ) ∼ |ϕ|⁴ potential. This potential is classically marginal but one can show that it is marginally irrelevant at one-loop. This is the statement that λ → 0 in the infra-red, so that the theory becomes free at low energies. Nonetheless, the classical potential fixes the R-charge to be R[Φ] = 2/3 so that R[W] = 2 as it should. Correspondingly, ∆[Φ] = 1 in the infra-red which is indeed the right result for a free chiral multiplet.

The powerful result (6.41) also makes life easier in another way. If we have two chiral superfields Φ₁ and Φ₂ then Φ₁Φ₂ is also a chiral superfield. Their R-charges simply add: R[Φ₁Φ₂] = R[Φ₁]+R[Φ₂]. But so too do their dimensions: ∆[Φ₁Φ₂] = ∆[Φ₁]+∆[Φ₂]. This is unusual in a conformal field theory. Typically if you multiply operators together then you get divergences as their positions come close and regulating these divergences changes the dimension of the composite. But for chiral superfields, things are much easier. We say that the chiral operators form the chiral ring.

There is, however, a small fly in the ointment. You’ve got to be able to identify the correct R-symmetry that appears in the superconformal algebra. For example, suppose that your theory has an R-symmetry R and a global symmetry F. Then there’s nothing to stop us from saying that R + αF is also a valid R-symmetry for any α ∈ ℝ. How do we know that this isn’t the thing that we should use when computing dimensions?! This loophole threatens to make the wondrous relation (6.41) completely toothless. Happily, there is a procedure for figuring out what combination of symmetries forms the correct R-symmetry. This procedure is known as a-maximization. This is important for understanding many theories and we will describe the procedure in Section 7.2.4. However, as we’ll now see, it is not needed for SQCD.

6.4.3 The Conformal Window for SQCD We determined the symmetries of SQCD back in Section 6.2. The charges of the chiral superfields under the non-anomalous R-symmetry are R[Q] = R[Q̃] = (Nf − Nc)/(2Nc)

This means the R-charge of the meson M = Q̃Q is R[M] = (Nf − Nc)/Nc (6.42)

Given the discussion above, one might wonder if we should worry about mixing of U(1)R with U(1)F. Happily, the meson M is neutral under U(1)F and so its dimension is unambiguous.

RAL UNDER U(1) SO IT'S NOT SOMETHING THAT WE HAVE TO WORRY ABOUT. WE CAN SAY IMMEDIATELY THAT THE DIMENSION OF THE MESON OPERATOR IS

Δ[M] = 3(N_f − N_c)  (6.43)

LET'S FIRST TEST DRIVE THIS FORMULA BY LOOKING AT WHAT HAPPENS WHEN N_f ≥ 3N_c WHERE SQCD IS INFRA-RED FREE. AT THE EDGE, WE HAVE

N_f = 3N_c ⇒ Δ[M] = 2  (6.44)

BUT THIS IS PRECISELY WHAT WE EXPECT. THE THEORY IS EFFECTIVELY FREE IN THE INFRA-RED, SO THE FIELDS ϕ AND ϕ̃ BOTH HAVE THEIR CANONICAL DIMENSION Δ[ϕ] = Δ[ϕ̃] = 1 WHICH AGREES WITH THE RESULT (6.44). THE RESULT (6.44) IS TELLING US THAT THE SCALAR FIELDS ϕ AND ϕ̃ (TOGETHER WITH THEIR FERMIONIC PARTNERS) ARE FREE AT N_f = 3N_c.

NOTE THAT THERE'S ALREADY SOMETHING A LITTLE SURPRISING HERE. WE KNEW THAT THE THEORY WAS INFRA-RED FREE AT N_f = 3N_c, BUT ONLY BY COMPUTING THE BETA FUNCTION. IN CONTRAST, THE RESULT ABOVE USES ONLY THE NON-ANOMALOUS R-CHARGE! YET THE TWO COINCIDE. IT'S A SIGN THAT ALL THESE THINGS ARE INTERCONNECTED IN SQCD IN A WAY THAT DOESN'T HAPPEN IN THE ABSENCE OF SUPERSYMMETRY.

WHAT HAPPENS IF WE NOW CHANGE N_f? WE CAN START BY LOOKING AT N_f > 3N_c WHERE, AT FIRST GLANCE IT APPEARS THAT WE BECOME A LITTLE UNSTUCK. HERE THE THEORY REMAINS FREE AND SO WE SHOULD STILL HAVE Δ[M] = 2. BUT THAT'S NOT WHAT THE FORMULA (6.41) SEEMS TO BE TELLING US. HOWEVER, SINCE THE THEORY IS FREE IN THE IR, THE ANOMALOUS U(1) SYMMETRY IS REINCARNATED AND CAN NOW MIX WITH THE R-SYMMETRY, CHANGING THE ANSWER. THIS IS A SALUTARY WARNING: THERE CAN BE SUBTLETIES IN BLINDLY FOLLOWING (6.41).

NOW LET'S LOOK AT WHAT HAPPENS AS WE DECREASE N_f BELOW THE ASYMPTOTIC FREEDOM BOUND OF N_f = 3N_c. WE KNOW THAT WHEN N_f = 3N_c − ϵ, FOR SOME SMALL ϵ, WE'RE SITTING IN A WEAKLY COUPLED BANKS-ZAKSQUE SUPERCONFORMAL FIELD THEORY. THE FORMULA (6.43) TELLS US THAT THE MESON HAS DIMENSION

Δ[M] = 2 − (1/3N_c)ϵ + ...

IN OTHER WORDS, IT'S SLIGHTLY LESS THAN TWO. YOU SHOULD THINK OF THE MESON AS DESCRIBING A LOOSELY BOUND STATE OF ϕ AND ϕ̃. BUT AS N_f DECREASES, SO TOO DOES THE DIMENSION Δ[M]. THIS IS TELLING US THAT THE STATE IS BECOMING MORE AND MORE TIGHTLY BOUND. AT SOME POINT, THE BANKS-ZAKS SUPERCONFORMAL FIELD THEORY BECOMES STRONGLY COUPLED AND WE LOSE CONTROL OVER ITS DYNAMICS. BUT, BY THE MAGIC OF SUPERSYMMETRY, WE REMARKABLY KEEP CONTROL OVER THE DIMENSION OF THE CHIRAL MESON FIELD! EVENTUALLY, THE DIMENSION OF THE MESON HITS THE BOUND (6.40). THIS OCCURS WHEN

N_f = N_c ⇒ Δ[M] = 1

BUT, AS WE MENTIONED ABOVE, ANY SCALAR OPERATOR THAT HAS DIMENSION 1 IS NECESSARILY A FREE SCALAR FIELD. THIS EQUATION IS TELLING US THAT THE BINDING BETWEEN ϕ AND ϕ̃ HAS BECOME SO STRONG THAT THE COMPOSITE MESON OPERATOR M IS ACTUALLY NO LONGER COMPOSITE! IT IS ACTING JUST LIKE A FUNDAMENTAL SCALAR FIELD. MOREOVER, IT IS NOW DECOUPLED AND IS FREE.

HOW SHOULD WE THINK OF THIS? THE PROPOSAL IS THAT THE MESON BECOMING FREE SIGNIFIES THE END OF THE CONFORMAL WINDOW (6.39). IN FACT, WE WILL ARGUE SHORTLY THAT THE THEORY AT N_f = 3N_c/2 IS A COMPLETELY FREE THEORY IN THE IR WITH A WHOLE BUNCH OF OTHER FIELDS JOINING M IN THE SENSE THAT THEY BECOME NON-INTERACTING AT LOW ENERGIES.

TO ARGUE THIS, WE WILL TURN TO A NEW DESCRIPTION OF THE PHYSICS THAT HOLDS THROUGHOUT THE CONFORMAL WINDOW AND, ALSO, FOR N_f < 3N_c/2. THIS IS KNOWN AS THE DUAL DESCRIPTION.

## 6.5 SEIBERG DUALITY

THROUGHOUT THIS SECTION, OUR INTEREST HAS BEEN IN MASSLESS SQCD, DEFINED AS SU(N_c) GAUGE THEORY COUPLED TO N_f FLAVOURS Φ AND Φ̃.

WE'VE FOUND A PLETHORA OF INTERESTING PHYSICS AS N_f IS VARIED. BUT WE HAVEN'T YET UNDERSTOOD WHAT HAPPENS WHEN N_c + 2 ≤ N_f ≤ 3N_c/2. MOREOVER, AT THE LOWER END OF THE CONFORMAL WINDOW, WHERE WE MIGHT EXPECT A STRONGLY INTERACTING CFT, WE'VE SEEN THAT THE MESON BECOMES FREE. IT WOULD CERTAINLY BE GOOD TO UNDERSTAND THIS BETTER.

SOME LIGHT COMES FROM A RATHER REMARKABLE DIRECTION. CONSIDER THE FOLLOWING THEORY: SU(Ñ_c) GAUGE THEORY COUPLED TO Ñ_f FLAVOURS q AND q̃ AND Ñ_f^2 SINGLETS M.

IN THE ABSENCE OF THE SINGLETS, THIS CLEARLY COINCIDES WITH OUR EARLIER THEORY JUST WITH THE NUMBER OF COLOURS RENAMED AS Ñ_c. HOWEVER, WE ARRANGE THE SINGLETS AS A MATRIX M_ij WITH i,j = 1,...,N_f WHICH IS SUBSEQUENTLY COUPLED TO THE SQUARK SUPERFIELDS THROUGH THE SUPERPOTENTIAL

W = λ q̃ M q  (6.45)

WITH λ A DIMENSIONLESS COUPLING. THIS IS NOW A SLIGHT TWIST ON OUR ORIGINAL SQCD AND ITS DYNAMICS MAY DIFFER. WE'LL SEE HOW BELOW. NOTE THAT WE'VE GIVEN THE SINGLETS THE NAME M. YOU MAY RECALL THAT THIS IS ALSO THE NAME THAT WE GAVE TO THE MESON IN OUR ORIGINAL THEORY. THIS IS WHAT WRITERS CALL FORESHADOWING.

FOR OUR PURPOSES, IT'S PARTICULARLY INTERESTING TO CONSIDER THE CASE WHERE THE NUMBER OF COLOURS IN THE TWO THEORIES ARE RELATED BY

Ñ_c = N_f − N_c  (6.46)

THIS SECOND THEORY IS KNOWN AS MAGNETIC SQCD (OR mSQCD). WE'LL ALSO AT TIMES REFER TO THE ORIGINAL SU(N_c) SQCD AS THE ELECTRIC THEORY AND WE'LL ELUCIDATE THE REASONS BEHIND THESE NAMES AS WE GO ALONG. WE NOW MAKE THE FOLLOWING, SOMEWHAT ASTONISHING, CLAIM:

SU(N_c) SQCD AND SU(N_f − N_c) mSQCD HAVE THE SAME LOW-ENERGY PHYSICS.

relationship is known as Seiberg duality. The purpose of this section is to give evidence for the claim and to understand its consequences.

**6.5.1 Matching Symmetries**

First let’s look at some evidence. Given that the one of the two theories is always strongly coupled, it is challenging to do any direct calculations. The simplest thing that we can check is agreement of the symmetries.

**Gauge Symmetries are Redundancies**

First, the elephant in the room. The gauge symmetries are not the same! Should we care? The answer is no. Gauge symmetries are not true symmetries of a theory: they are merely a redundancy in the way we choose to describe the theory.

These are easy words to wheel out, but they also grate with other things we know about physics. The theory of electromagnetism is synonymous with U(1) gauge theory. The Standard Model of particle physics is defined as having gauge group SU(3) × SU(2) × U(1). If the gauge symmetry is something that isn’t actually inherent to a theory, but just a redundancy in our choice of description, why do we hang so much on it elsewhere?

The reason is that gauge symmetry is an extraordinarily useful redundancy when theories are weakly coupled. In that situation, attempting to describe the physics in terms of anything other than the gauge field, with particular gauge group, is so ridiculously complicated that it borders on the absurd. You could, for example, choose to describe quantum Maxwell theory in terms of the field strengths F_{μν} and all possible Wilson line operators exp(i∫A) which carry the gauge invariant information. But that’s certainly not easier than our usual gauge dependent description in terms of A.

This means that when gauge theories are weakly coupled, the description in terms of the gauge symmetry G is indispensable. But when things become strongly coupled, the story is very different. In this case, the gauge symmetry reveals itself for what it is: a redundancy. Seiberg duality makes this stark. You can describe the same physics using two very different gauge theories. Sometimes one formulation is best suited to the problem at hand because the physics is weakly coupled in those variables. Sometimes the other formulation is easiest. But neither formulation is ever wrong and the fact that the gauge symmetries don’t match in the two dual theories is a feature, not a bug.

**Global Symmetries**

The story is different for global symmetries. These must match. Moreover, as both theories are claimed to flow to the same infra-red physics, their UV ’t Hooft anomalies must match as well. Let’s see how we do.

It’s useful to list, one last time, how the various fields transform. In the electric theory, we have

|          | SU(N_c) | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R | |----------|---------|-----------|-----------|--------|--------|--------| | Φ        | □       | □         | 1         | 1      | 1      | N_f - N_c | | Φ̃        | □       | 1         | □         | -1     | 1      | N_f - N_c | | Λ_b^0    | 1       | 1         | 1         | 0      | 2N_f   | 0      |

with b_0 = 3N_c - N_f. For the magnetic theory, we have

|          | SU(N_f - N_c) | SU(N_f)_L | SU(N_f)_R | U(1)_B | U(1)_A | U(1)_R | |----------|---------------|-----------|-----------|--------|--------|--------| | q        | □             | □         | 1         | N_c    | -1     | N_c    | | q̃        | □             | 1         | □         | -N_c   | -1     | N_c    | | M        | 1             | □         | □         | 0      | 2      | 2(N_f - N_c) | | Λ̃_b̃^0   | 1             | 1         | 1         | 0      | -2N_f  | 0      |

Here Λ̃ is the strong coupling scale of the magnetic theory with b̃_0 = 3(N_f - N_c) - N_f = 2N_f - 3N_c the 1-loop beta function.

The normalisation of the non-anomalous U(1) charge is fixed, as usual, by the requirement that the (magnetic) gluinos have charge +1. (This, in turn, follows from the fact that the superspace coordinate has R[θ] = −1.) This, in turn, fixes the R-charge for the dual squarks which came be written as R[q] = R[q̃] = N_c/N_f = (N_f - N_c)/N_f, where we see that it mimics the form in the original theory. The requirement that the superpotential has R[W] = 2 then fixes the R-charge of the singlet M.

R[M] = 2(N_f - N_c)

But this is the same as the R-charge as the meson ΦΦ in the original electric theory. Moreover, because these are chiral fields, if their R-charges match then so too do their dimensions. This provides our first, and most important, entry in the dictionary relating the electric and magnetic theories: the singlet fields M in the magnetic theory correspond to the meson in the electric theory.

M ∼ ΦΦ

This matching provides an opportunity to reiterate a lesson from above. We have not attempted to match individual quarks and gluons on the two sides of the duality. This is because these are not gauge invariant objects and so have no physical meaning on their own. However, gauge invariant observables or fields should match across the duality.

Next the U(1) charges. We want to identify U(1)_B in the two theories but there’s an ambiguity in the normalisation. We’ve fixed this ambiguity in the table above by ensuring that the dual baryons b ∼ q^{N_f - N_c} and ˜ b ∼ q̃^{N_f - N_c} have the same U(1) charges as their electric counterparts B and ˜ B. Crucially, their R-charges also match. This then provides the second entry in our dictionary between the two theories: B ∼ b and ˜ B ∼ ˜ b.

b. We will look a little closer at the identification of these operators shortly.

’t Hooft Anomaly Matching Now we can play the increasingly familiar ’t Hooft it this.

That R-charge was determined by assuming that R[W] = 2 which is pre-judging the answer! This is not what we want for the present calculation. Instead, we need to remember that before we add the superpotential, M is just a free field, decoupled from everything else. This means that it has dimension ∆[M] = 1 and, correspondingly, R[M] = 2/3. This means that, from the perspective of the IR, the superpotential W = q̃Mq has dimension ∆[W] = R[W] = 3/2 + 2/3 * (N_c/N_f) = 1 + (3N_c)/(2N_f).

When we first enter the lower bound of the conformal window, we have N_f > N_c ⇒ ∆[W] < 3.

But this means that the superpotential is always a relevant deformation in the conformal window! (The measure in the action is d^4x d^2θ and [d^4x] = −4 while [d^2θ] = +1 which is why the bound for a relevant superpotential is ∆[W] < 3.)

The RG flows are shown in Figure 12. There are three fixed points in the magnetic theory: the free theory at g = λ = 0 that can be thought of as the starting point in the UV; the fixed point without a superpotential in the conformal window with λ = 0 and g ≠ 0; and the final fixed point with g,λ ≠ 0. The claim of Seiberg duality is that this final fixed point of the dual theory, shown as the red dot, coincides with the fixed point in the conformal window of the electric theory.

By the time we reach our final fixed point, shown by the red dot in the figure, we should now take R[W] = 2. This gives us the R-charge R[M] that we listed in the table with the corresponding dimension R[M] = 2(N_f − N_c)/N_f ⇒ ∆[M] = 3(N_f − N_c)/N_f.

It’s only when we reach this fixed point that the R-charge and dimension of M in the magnetic theory coincides with those of the meson in the original theory.

As we increase N_f ≥ 3N_c, there is no mystery about our electric theory: it is free in the infra-red. In contrast, the magnetic theory flows to strong coupling but now becomes the weakly interacting SU(N_c) theory in the infra-red. We see again that Seiberg duality is an example of a strong-weak coupling duality. When one theory is strongly coupled, the other may be weakly coupled and vice versa. This makes it useful.

Of course there are also regimes – notably in the middle of the conformal window – when both theories are strongly coupled. So the duality isn’t a magic bullet, solving all our woes. But it is a dramatic and unexpected step forward.

All of this means that the exact interpretation of Seiberg duality depends on the value of N_f/N_c. For small N_f, the electric theory flows to the weakly coupled magnetic theory. For large N_f, the opposite happens: the magnetic theory flows to a weakly coupled electric theory. While for N_f in the conformal window, both theories flow to the same infra-red fixed point. This is summarised in Figure 13. However, in all cases Seiberg duality is a statement about RG flows. This should be distinguished from other “exact dualities” of quantum field theories or many body systems, where there are two very different descriptions that hold at any energy scale. Examples of exact dualities includes the high/low temperature duality of the Ising model, or electromagnetic dualities of N = 2 and N = 4 supersymmetric theories.

6.5.3 Deformations of the Theories So far we’ve focussed on the fixed point. But both theories also have a moduli space of vacua, and this too should match. However, showing this isn’t straightforward because, as we saw in Section 4.3, there are some non-trivial constraints between the mesons and baryons.

Nonetheless, we can see roughly how things work. We’ve already seen that the singlets M are dual to the mesons in the electric theory ΦΦ ∼ M. (6.47)

The symmetries also allow us to match the baryon degrees of freedom B_{i1...iN_c} ∼ ε_{i1...iN_c j1...j Ñc} b^{j1...j Ñc}, B̃^{i1...iN_c} ∼ ε^{i1...iN_c j1...j Ñc} b_{j1...j Ñc}.

Each transforms in the (N_c)-antisymmetric representation of SU(N_f) which, of course, is equivalent to the (N_f − N_c)-antisymmetric representation.

The magnetic theory also has its own meson fields m̃ = q̃q and you might wonder what becomes of these. But the equation of motion for the singlets M is simply m̃ = 0 so these dual mesons don’t give us any further light degrees of freedom.

Masses and Expectation Values We can now perform some simple tests of the duality. Suppose that we turn on the electric meson fields to move out on the moduli space. To start we just turn on a single entry.

ϕ ˜ ϕ = … This breaks the gauge symmetry SU(N ) → SU(N − 1), now with N − 1 flavours.

We would like to see this behaviour in the dual theory. In fact, this is straightforward. Giving the singlet M the same expectation value, we have W mag ∼ q̃Mq = v q̃ q This is just a mass term for the dual squark and we can integrate it out, giving us SU(N ) with N −1 flavours. This is the expected dual.

Alternatively, we could give a mass to one of the quarks in the electric theory by adding the superpotential W el = mΦ 1 Φ 1 After integrating out this massive flavour, we’re left with SU(N ) with N −1 flavours. In the magnetic theory, this same mass deformation gives W mag = q̃Mq + mM The equation of motion for the singlet M then induces an expectation value for the dual squark q̃ q = −m This, in turn, breaks the dual gauge group SU(N ) → SU(N −1). The upshot is that we’re left with the dual theory of an SU(N −N −1) gauge group coupled to N −1 flavours. This is the expected result.

We see that these simple deformations respect the duality, with a mass term on one side mimicked by a Higgs effect on the other.

Matching RG Scales There’s a slight subtlety that we’ve brushed under the carpet so far. The key element in our dictionary relating mesons ΦΦ ∼ M can’t quite be right. This is because the quarks on the left-hand side are defined in the UV of SQCD and each have dimension 1 so ΦΦ has dimension 2. Meanwhile the singlet M is a free field in the dual theory so has dimension 1. So our dimensional analysis is amiss.

This should be straightforward to patch up: we just need some invariant RG scale to take up the slack. But this scale should be holomorphic and, moreover, we don’t want it to mess up the symmetries on the two sides. Either the electric RG scale Λ or magnetic scale Λ ˜ change the (admittedly spurious) U(1) charge. But we can introduce a new scale µ which is some geometric mean of the two Λ3Nc−N fΛ ˜3(N f −Nc)−N f = (−1)N f −NcµN f The scale µ is, by construction, invariant under all symmetries, spurious or otherwise. A better characterisation of the dictionary is then ΦΦ = M The strange looking minus sign in (6.48) is largely a convention, but it can be shown to ensure that the dual of the dual theory brings us back to the original.

The Theory N = N +1 Again f c We’ve advertised Seiberg duality as holding for N ≥ N + 2. But it also gives the right answer for N = N +1, at least if we include the additional term detM in the superpotential so that (6.45) becomes W ∼ det M + q̃Mq This is the expected superpotential (6.37) for the N = N +1 theory, with the dual quarks q and q̃ identified with the baryons B and B.

A Glimpse of the Superconformal Index Until now, we’ve given no more than plausible evidence for Seiberg duality. The symmetries and ’t Hooft anomalies match and it passes some simple tests as we deform the theory. It turns out that there is a much more quantitative test that the duality passes. This comes from computing an object known as the superconformal index.

The superconformal index is an extension of the Witten index. While the Witten index receives contributions only from the ground states, the superconformal index receives contributions from a much larger, but still restricted class of states. Moreover, it can be reliably computed for theories even at weak coupling.

The superconformal index is defined for superconformal theories on S3 ×R. It is a function of two variables, p and q, by tracing over all states I(p,q) = Tr(−1)F p j1+j2−1R q j1−j2−1 Here R is the R-charge of the state while j1 and j2 are the two angular momenta associated to the rotation group SO(4) = SU(2)×SU(2).

The formulae for the superconformal indices are fairly complicated and, at first glance, look very different for SQCD and mSQCD. It is a highly non-trivial mathematical fact that these formulae do, in fact, coincide.

6.5.4 Why Seiberg Duality is Electromagnetic Duality There is one feature of Seiberg duality that perhaps remains mysterious: why have we called the dual theory “magnetic” and the original theory “electric”? The answer to this gets to the heart of how to think about Seiberg duality and other related phenomena.

The basic idea goes back to Maxwell theory. The equations of motion are usually written as ∂ Fµν = Jµ and ∂ ⋆Fµν = 0 with Jµ the electric current. If there are no charged particles in the theory then Jµ = 0 and the Maxwell equations exhibit a surprising symmetry in which we exchange Fµν → ⋆Fµν. In terms of the underlying electric and magnetic fields, this means E → B and B → −E This is electromagnetic duality. It is broken in electromagnetism because our world has electric sources, but no magnetic sources.

However, one could imagine a theory in which there are particles carrying both electric and magnetic charges. The latter are called magnetic monopoles. In this case, Maxwell’s equations should be replaced by ∂ Fµν = J μ and ∂⋆Fμν = Jμ e m with Jμ and Jμ the electric and magnetic currents respectively. In such a theory, e m electromagnetic duality may be restored, now with the electric and magnetic particles interchanged. However, there is a consistency condition between electric charges qel and magnetic charges qmag : they can be shown to obey the Dirac quantisation condition qel qmag ∈ Z 2π A derivation of this can be found in the lectures on Gauge Theory. This has an interesting consequence. The electric charge is a measure of the strength of the electromagnetic force. (For example, the fine structure constant is α = q²el/4πϵ₀ℏc.) The Dirac quantisation condition tells us that if the electric charges are weakly coupled, then magnetic charges will necessarily be strongly coupled.

12 For more information about the superconformal index, see the lectures by Yuji Tachikawa or by Abhijit Gadde.

It’s not so easy to write down versions of QED that include both electric and magnetic charges. This is because we must work with the gauge field Aμ, and the resulting Bianchi identity ∂⋆Fμν = 0 immediately implies that there are no magnetic monopoles. However, the story becomes richer in certain non-Abelian gauge theories. It turns out that some non-Abelian gauge theories necessarily have magnetic monopoles arising as solitons. This means that although we start by writing a theory purely of electric charges, the actual theory includes both electric and magnetic charges. Examples of theories with solitonic magnetic monopoles include N = 2 and N = 4 super Yang-Mills. However, the N = 1 SQCD theories that we’ve been considering in this Section do not obviously contain magnetic monopoles. There are certainly no classical soliton solutions that one can construct that have magnetic charge. On the other hand, the theories are strongly coupled and it’s not at all clear what properties their excitations have. Part of the claim of Seiberg duality is that the dual description should really be thought of as a kind of electromagnetic duality, with the SU(Nc − Nf) gauge group related to the original SU(Nc) gauge group by something morally equivalent to swapping electric and magnetic fields. Correspondingly, the dual baryons b and ˜b should be viewed as some kind of magnetic excitation from the perspective of the original theory.

You may have noticed that I’m saying a lot of words here and not writing down any formulae! That’s because it’s difficult to make the above claims precise. There are, however, some hints that this is the right way to think about things. For example, the relationship (6.48) between the scales Λ³Nc−Nf ˜Λ²Nf −3Nc ∼ constant.

This formalises something that we’ve already seen: Seiberg duality is a strong-weak duality. As the gauge coupling in one theory gets smaller, the coupling in the other gets larger. This is reminiscent of the behaviour in electromagnetic duality. However, the best evidence that Seiberg duality should be viewed as electromagnetic duality comes from exploring other theories. In particular, N = 2 and N = 4 theories both exhibit a form of electromagnetic duality where both electric and magnetic degrees of freedom can be made manifest. The existence of a duality means that there are two formulations of the theory, one in which the electric objects are viewed as fundamental particles and the other in which magnetic objects are fundamental particles. In either of these descriptions, the other particles arise as solitons. It’s only when Seiberg duality is viewed within this larger context as one of many dualities among quantum field theories, that it becomes clearer that it is, indeed, a version of electromagnetic duality.

7 More Supersymmetric Gauge Dynamics

There are many more interesting properties of N = 1 gauge theories. In this section, we describe a few of them.

## 7.1 Other Gauge Groups

One obvious generalisation of the previous results comes from looking at other gauge groups. There is a similar story for both Sp(N) and SO(N) gauge groups, with a runaway potential for a small number of flavours and a dual description available in the conformal window. It turns out that SO(N) is significantly more complicated, with a number of twists and turns along the way13. Here we give the details only for the much simpler case Sp(N).

The classical Lie group Sp(N) is subgroup of SU(2N) that leaves invariant the anti-symmetric tensor J = 1 ⊗ iσ₂.

The group Sp(N) has dimension N(2N+1), rank N and the fundamental representation has dimension 2N. For the lowest rank we have Sp(1) = SU(2).

Be warned: you will find different naming conventions for this group in the literature. Some authors prefer USp(2N) to Sp(N), where the argument now describes the dimension of the smallest representation rather than the rank. More confusingly, other authors write Sp(2N) for Sp(N)!

7.1.1 Sp(N) Quantum Dynamics

In this section, we consider Sp(Nc) gauge theory coupled to 2Nf chiral multiplets Qi in the fundamental representation14. The representations of Sp(Nc) are pseudoreal which means that there’s no sense in which the m matter comes in conjugate pairs. Nonetheless, there’s a subtle effect in Sp(N) gauge theories called the Witten anomaly that means that Sp(N) gauge theories only make sense when coupled to an even number of fundamental Weyl fermions. Hence the 2N above.

13 A question on the examples sheet covers the key duality. You can find the full details in the original paper by Ken Intriligator and Nati Seiberg.

14 This theory was first discussed by Ken Intriligator and Philippe Pouliot.

To understand this theory, we can largely follow the path laid down in the previous section. The 1-loop beta function is given by b₀ = 3(N_c + 1) - N_f Next, the symmetries. In the case of N_f = 0, the U(1)_R symmetry is anomalous with a surviving Z_{2(N_c+1)}. This, in turn, is spontaneously broken to Z_2 by a gluino condensate ⟨Trλλ⟩ ≠ 0, giving N_c+1 ground states. Indeed, this coincides with the Witten index Tr(−1)^F e^{-βH} = N_c+1.

When N_f > 0, there is a surviving R-symmetry. Taking into account the anomaly, the symmetries of the theory are

Sp(N_c)  SU(2N_f)  U(1)_A   U(1)_R Q        □         □        1       1 Λ^{b₀}  1         1        2N_f    0

This is largely sufficient for us to understand what becomes of the quantum dynamics of this theory.

First, we should understand the classical dynamics. For Sp(N_c) gauge theories there are no baryons and the classical moduli space is parameterised solely by mesons, M_{ij} = Q_{ia} Q_{jb} J^{ab} (7.1)

with a,b = 1,...,2N_c the group index and i,j = 1,...,2N_f the flavour index. Importantly, these mesons are anti-symmetric in the flavour indices: M_{ij} = −M_{ji}.

When N_f ≤ N_c, there are no further constraints on these mesons. The classical moduli space has dimension dim M = N_f(2N_f − 1). At a generic point, the gauge group is broken from Sp(N_c) to Sp(N_c − N_f).

For N_f > N_c, there is a constraint arising from the fact that the mesons M_{ij} have rank(M) ≤ 2N_c. This classical constraint can be written as ε^{i₁...i_{2N_f}} M_{i₁i₂} M_{i₃i₄} ... M_{i_{2N_c+1}i_{2N_c+2}} = 0 (7.2)

At a generic point, the Sp(N_c) gauge group is broken completely. As with the SU(N_c) theories, this moduli space has singularities whenever the rank drops below the maximal. These signify the emergence of massless, unbroken gauge bosons.

So much for the classical theory. What about the quantum? Given our earlier results about SQCD, we might expect that a superpotential is generated, lifting the moduli space for some low N_f. We can use the symmetries above to determine what superpotential is possible. First, we need to form an object that is invariant under the SU(2N_f) flavour symmetry. For SU(N_c) SQCD, this was the determinant of the meson matrix. But for Sp(N_c), we have something a little different. This is because the meson (7.1) is necessarily anti-symmetric in the i,j flavour indices which means that it’s natural to consider the Pfaffian, defined by (Pf M)² = det M This has U(1) charges R[Pf M] = 2(N_f − N_c − 1) and A[Pf M] = 2N_f.

Runaway for N_f ≤ N_c The symmetries allow a unique dynamically generated superpotential W = C ( Λ^{3(N_c+1) - N_f} / Pf M )^{1/(N_c+1 - N_f)} (7.3)

for some coefficient C. This superpotential only makes sense for N_f ≤ N_c where it gives rise to a runaway potential, lifting all ground states. For the case N_f = N_c, the gauge group is completely broken and here the superpotential arises from an instanton with the characteristic signature Λ^{b₀}. An explicit weak coupling calculations shows that C ≠ 0 and the superpotential is indeed generated.

As for SQCD, giving the flavours a mass stabilises the vacua at a finite distance and reveals the N_c + 1 ground states expected by the Witten index. If we crank up the mass and integrate out the massive flavours, we can derive the runaway superpotential, together with the coefficient C, for all smaller values of N_f.

Deformed Moduli Space for N_f = N_c + 1 For N_f = N_c + 1, the classical constraint (7.2) reads Pf M = 0 For this choice of N_f, we have R[M_{ij}] = 0 and there is an opportunity for the classical constraint to pick up a quantum deformation to Pf M ∼ Λ^{2(N_c+1)} (7.4)

The classical moduli space had singularities arising from massless gauge bosons. These are removed in the quantum moduli space, signalling confinement.

To see this the quantum deformation does indeed occur, we can repeat the analysis of SQCD and integrate out the last flavour. The only real difference comes from the fact that M_{ij} is now anti-symmetric. We start with a superpotential imposing the constraint, together with a mass term for the final flavour which we call Z W_old = X(Pf M − Λ^{2(N_c+1)}) + mZ  with  Z = M_{2N_c+1,2N_c+2} (7.5)

where we’re not being too careful about the overall coefficient in front of the quantum deformation. (There are some annoying factors of 2 that appear in the Sp(N_c) analysis that aren’t there for SU(N_c).) We write the meson matrix as M = ( 0   Z )

( -Z  0 )

The equation of motion for Z and X give X = - m / Pf̃M   and   Z = Λ^{2(N_c+1)} / Pf̃M Substituting this back into the constrained superpotential (7.5) reproduces the expected runaway behaviour (7.3).

with the matched RG scales Λ^(2Nc+1) = Λ^(2(Nc+1)m).

We can also do some ’t Hooft anomaly matching. When M satisfies the quantum modified constraint (7.4), the global symmetry is broken to SU(2N_f)×U(1)_R → Sp(N_f)×U(1)_R. There is no need to match the Sp(N_f) anomalies because the relevant group theoretic cubic invariant simply vanishes for Sp(N_f). But we still have others: Sp(N_f)^2 ·U(1)_R: In the UV we have just the quarks with R[ψ] = −1. The ’t Hooft anomaly is A_UV = −2N_c. In the IR, we have only mesons. The chiral superfields have R-charge R[M] = 0, so the fermions have charge −1. They transform in the anti-symmetric representation of Sp(N_f). This has dimension dim(□) = N_f(2N_f − 1) − 1 and Dynkin index I(□) = 2N_f − 2. The ’t Hooft anomaly is then A_IR = −(2N_f − 2) = −2N_c. U(1)_R^3: In the UV we have both gluinos and quarks, contributing A_UV = N_c(2N_c + 1)×(+1)^3 + 4N_c N_f×(−1)^3 = −N_c(2N_c + 3). In the IR, we have just the mesons, giving A_IR = −N_f(2N_f − 1) − 1, which agrees with A_UV. A similar counting also shows that the mixed U(1)_R-gravitational anomaly matches.

Confinement Without χSB for N_f = N_c + 2. Now there can be neither a superpotential generated on the moduli space, nor a quantum deformation of the constraints. We are left with the classical moduli space, subject to the classical constraint (7.2). This space has a singularity at the origin. As with SQCD, the constraints are not imposed by a Lagrange multiplier, but instead arise as the equations of motion from the superpotential W = PfM / Λ^(2Nc+1). Once again, we propose that the quantum interpretation of this singularity is different from the classical interpretation. The gauge gauge bosons, which are classically massless, are thought to confine with the singularity at M = 0 arising because all ½ × (2N_f) × (2N_f − 1) elements of the anti-symmetric meson matrix M are massless. Once again, this proposal must pass the stringent tests of ’t Hooft anomaly matching. We have: SU(2N_f)^3: In the UV, the quarks give A_UV = 2N_c. In the infra-red, the mesons sit in the anti-symmetric representation and A_IR = A(□). This is given by A(□) = 2N_f − 4 = A_UV. SU(2N_f)^2 ·U(1)_R: The quarks now have R-charge R[ψ] = −(N_c + 1)/(N_c + 2) and so contribute to the UV ’t Hooft anomaly as A_UV = −2N_c(N_c + 1)/(N_c + 2). In the IR, the mesons have R-charge R[M] = 2/N_c and, of course, the fermions in this chiral multiplet have R-charge R[M] − 1. For SU(2N_f), the Dynkin index of the anti-symmetric representation is I(□) = 2N_f − 2, so we have A_IR = 2(N_f − 1)×(2/N_c − 1) = A_UV. U(1)_R^3: The gluinos and quarks give A_UV = N_c(2N_c + 1)×(+1)^3 + 4N_c N_f × (−1)^3 = (2N_f − 1)(N_c − 2)^3 / (N_f N_c^2). Meanwhile, the mesons give A_IR = N_f(2N_f − 1)× (−1)^3 = A_IR. U(1)_R: This time the mixed U(1)_R-gravitational anomaly gives a different counting. We have A_UV = N_c(2N_c + 1)×(+1) + 4N_c N_f × (−1) = −2N_c^2 + 5N_c − 2. Meanwhile, the mesons give A_IR = N_f(2N_f − 1)× (−1) = A_IR. Again, we see that all ’t Hooft anomalies match as they should.

7.1.2 Seiberg Duality. For N_f ≥ N_c + 3, we turn to a dual description. The claim is that Sp(N_c) with 2N_f chiral multiplets is dual to Sp(N_c) with 2N_f chiral multiplets q in the fundamental and singlets M_ij. Here M_ij sits in the anti-symmetric representation of the SU(2N_f) flavour symmetry and is coupled to the other fields through the superpotential W = M_ij q_i^a q_j^b J_ab, with a,b = 1,...,N_c and i,j = 1,...,N_f. The rank of the dual gauge group should be taken to be N_c = N_f − N_c − 2. One can perform all the same tests of Seiberg duality that we saw for SU(N) SQCD. The proposal passes them all. Figure 15. The phases of Sp(N_c) gauge theory with 2N_f massless, fundamental chiral multiplets. For now, we can use the duality to put together the phase diagram for Sp(N_c) with 2N_f fundamental chiral multiplets. It looks very similar to the SU(N) case, with just the numbers changing. Jumping first to large N_f, the original electric theory is infra-red free when N_f ≥ 3(N_c + 1). For N_c + 3 ≤ N_f ≤ 3(N_c + 1)/2, the magnetic theory is infra-red free. For 3(N_c + 1)/2 < N_f < 3(N_c + 1), both theories flow to the same conformal fixed point. The upshot is that the phase diagram for Sp(N_c) theories looks very similar to that of SU(N) SQCD. It is shown in Figure 15.

7.1.3 SU(2) Gauge Theory Revisited. As we mentioned at the beginning of this section, Sp(1) = SU(2). That means that we now have two different stories for SU(2) gauge theory, one presented here and the other in Section 6. We should check to make sure that they are consistent. Things start out looking fine. For N_f = 0, the Witten index tells us that there are two ground states. For N_f = 1, there is just a single meson field M and in both descriptions we have the superpotential W = Λ^5 / M. For N_f = 2, our two descriptions are the same, but with slightly different names for various objects. In the SU(N) language, we introduced f our mesons M, with i,j = 1,2 and two baryons B and B, making 6 in total. In the Sp(1) language, we only have mesons that, to avoid confusion, we’ll call M. These have i,j = 1,...,4 with the requirement that M = −M again making 6 in total. One can show that detM −BB = PfM. This means that both the classical constraint, and the quantum deformed constraint, coincide in the two descriptions.

There is a similar story when N = 3. Now in the SU(2) description there are 9 mesons M and 6 baryons B and B ˜, while in the Sp(1) description there are 1 ×6×5 mesons M.

Things start to get more interesting when we move into the realm N ≥ 4 where the dual description is available to us. The gauge invariant operators M, B and B still match the mesons M. But the dual descriptions are very different.

To see this, let’s look at SU(2) with N = 4 flavours. The two dual descriptions are based on SU(N − N ) and Sp(N − N − 2) gauge theories respectively, which happily coincide for N = 2 and N = 4. But the singlet fields which couple through a superpotential are different. The SU(N −N ) dual gives SU(2) with N = 4 flavours and W = (cid:80)4 ˜ q M q f i,j=1 i ij i. The global symmetry of this theory is SU(4)2×U(1), acting on the ˜q and q individually. Meanwhile the Sp(N −N −2) dual gives SU(2) with N = 8 chiral multiplets and W = (cid:80)8 q M f i,j=1 i ij i. Now we haven’t split the matter into two sets, q and ˜q. Correspondingly, the theory has a much larger SU(8) global symmetry. From our discussion above, both of these theories must flow to the same IR fixed point. This means that the first theory must develop the full SU(8) flavour symmetry in the infra-red. In fact, it turns out that there are a number of other ways to split the matter multiplets, giving different duals. You can read more about this in the lectures by Yuji Tachikawa.

For N ≥ 5, things start to look even more different. For example, when N = 5 one f f dual is an SU(3) gauge theory while the other is an Sp(2) = Spin(5) gauge theory. We see that dual theories can come in different forms: there is nothing that tells us that there is a unique dual (or, indeed, any dual) for a given gauge theory.

## 7.2 A Chiral Gauge Theory

A chiral gauge theory is defined to be one in which left and right handed fermions transform differently under the gauge group. In the supersymmetric context, this means that chiral multiplets do not come in conjugate pairs.

It’s not completely straightforward to write down consistent chiral gauge theories because we have to make sure that there are no gauge anomalies. Furthermore, in the absence of supersymmetry, chiral theories are those that we understand least, in large part because the Nielsen-Ninomiya theorem provides an obstacle to simulating these theories on a computer. Notably, the Standard Model is an example of a chiral gauge theory, albeit one where the chiral interactions are weakly coupled and so we can use perturbation theory to understand what’s going on.

The purpose of this section is to describe the dynamics of some simple supersymmetric chiral theories.

7.2.1 SU(N) with a Symmetric Consider a G = SU(N) gauge theory, with a single chiral multiplet S in the symmetric representation and N + 4 chiral multiplets Q in the anti-fundamental. This is a consistent chiral theory because the symmetric representation contributes A( ) = N+4 to the SU(N) anomaly, which is subsequently cancelled by the ˜Q with i = 1,...,N +4, each of which contributes A(□) = −1.

The symmetry structure of the theory is SU(N) SU(N +4) U(1) U(1)

F R S 1 N +4 −N−2 N+2 Q ˜ □ □ −(N +2) 1

There is a large classical moduli space, parameterised as always by gauge invariant, holomorphic monomials of the matter fields. These are: mesons : Mij = ˜Q iSQ ˜j flavour singlet : U = detS baryons : B = Q ˜N (7.6)

more baryons : B′ = (Q ˜ S)N where the baryons are contracted with an SU(N) epsilon symbol; there are (cid:0)N+4(cid:1) of them. As always, there are some constraints among these operators, including MN = UB2 and B′ = UB.

There is no superpotential that we can write down consistent with the symmetries, so this moduli space survives in the quantum theory. (The flavour singlet U has charge under U(1) , while other flavour singlets that you might think you could construct, such as det M or M4B2 vanish identically.)

We can move out along the moduli space in various directions, breaking the gauge and global symmetries in some manner. The physics far out along the moduli space can be understood using weakly coupled analysis (possibly with some strong coupling physics of the unbroken part of the gauge group still to deal with). Here we would like to understand what happens at the origin of the moduli space.

First note that there’s no issue with asymptotic freedom in these theories. As the number of flavours increases, so too does the number of colours and the theories are asymptotically free for all N. Howeve However, there is an issue with the unitarity bound (6.40). This tells us that any chiral operator in an interacting superconformal theory must have R-charge R[O] > 7/6 (7.7) where, crucially, R is the R-charge at the superconformal point. In general, this R may not coincide with the R-symmetry that we identify in the UV. Indeed, there’s an ambiguity in our choice of R-symmetry in the table above: we made a specific choice, but we could equally as well have chosen a new R-symmetry which involved the old one, together with a mix of U(1)_F. In general, the IR R-symmetry could be a mix R_IR = R + αF (7.8) for some α ∈ R. We don’t yet have any way to determine which combination should be identified with the R-symmetry of the conformal field theory.

We will, in fact, explain how we can identify R_IR in Section 7.2.4. But for now, let’s take the most general case (7.8) and look at the R-charges of two of our chiral operators, M and U. They are R_IR[M] = −αN and R_IR[U] = (N−2)/(N+2) + α(N+4) You can see immediately that, for large N, there is going to be a problem satisfying the unitarity bound (7.7). The first term for R_IR[U] is negative, so we must take α > 0. But then, for large enough N, we will necessarily have R_IR[M] < 0. A short calculation shows that there is no choice of R-symmetry for which R_IR[M] > 2/3 and R_IR[U] > 2/3 whenever N ≥ 13.

This suggests that the chiral theory flows to a free infra-red theory when N ≥ 13 and to an interacting SCFT when N < 13. In fact, for the intermediate case of N = 13, there is a choice for which R_IR[M] = R_IR[U] = 2/3, suggesting again that these fields may be free.

7.2.2 A Chiral Duality

To better understand the infra-red physics, we can try to find a dual description. It turns out that the chiral gauge theory described above has a rather startling dual15. It has gauge group G = Spin(8). This group, which is the double cover of SO(8), is rather special as it has three, inequivalent representations all of dimension 8. These are the vector 8_v, the spinor 8_s and the conjugate spinor 8_c. The dual theory has a single chiral multiplet p in the spinor representation and N + 4 chiral multiplets q in the vector representation. In addition, there are Spin(8) singlet fields M_ij and U and a superpotential W = M_ij q_i q_j + U p p (7.9) The symmetry structure of the theory is [Symmetry table: q in 8_v under Spin(8), fundamental of SU(N+4), U(1)_F charge -1, U(1)_R charge 1; p in 8_s under Spin(8), singlet of SU(N+4), U(1)_F charge N+4, U(1)_R charge -5; M in singlet of Spin(8), symmetric tensor of SU(N+4), U(1)_F charge 0, U(1)_R charge 2; U in singlet of Spin(8), singlet of SU(N+4), U(1)_F charge -2(N+4), U(1)_R charge 12]

Let’s first see why these two theories might be dual to each other. First, each have the same global symmetry SU(N+4)×U(1)^2. Note, however, that we haven’t yet made any attempt to match the two Abelian symmetries across the duality. We’ll do this shortly.

In addition, the gauge invariant chiral superfields match. For our Spin(8) theory, the obvious qq and pp mesons are killed by the equations of motion of the superpotential. (Indeed, this is largely the purpose of the superpotential.) We do, however, have the singlets M_ij and U whose names already suggest how they might map to the original theory, Q_i^T S Q_j ↔ M_ij detS ↔ U Moreover, we can use these to understand how the Abelian symmetries map across both sides of the duality. The symmetries match if we rescale the global symmetry a_F' = −N a_F. We can’t rescale the R-symmetry because it’s fixed by the requirement that R[gluino] = 1. However, the two R-symmetries on either side of the duality can differ by a flavour symmetry. You can check that the R-symmetries match if we take R' = R + (N+6)/(N(N+2)) F. With these redefinitions, our group of symmetries read [Symmetry table with redefined charges: q: 1/(2(N+2)), p: -(N+4)/(2(N+2)), M: (N+6)/(N+2), U: -N(N-2)/(N+2)]

These most likely aren’t the R-symmetries that you would have chosen. But they’re the R-symmetries we’ve got!

We haven’t yet discussed the baryons of either theory. It turns out that these too agree, as do the moduli spaces, but there’s a subtlety awaiting us so we will postpone that discussion to Section 7.2.3. Instead, with the symmetries in hand we can turn to the next check: ’t Hooft anomaly matching. For example, those involving the non-Abelian global symmetry are SU(N+4)^3: In the electric theory, we have A_el = N. In the magnetic theory, the q contribute A_mag = −8 while the mesons M contribute A_mag = (N + 4) + 4, so A_el = A_mag as it should. SU(N+4)^2·U(1)_F: In the electric theory, we have A_el = −N × (N + 2). In the magnetic theory we have A_mag = 8×(1/(2(N+2)))+(N+4+2)×(−N) = A_el. SU(N+4)^2·U(1)_R: Since R[Q] = 1/2 the corresponding fermions are uncharged and we have A_el = 0. In the magnetic theory, A_mag = 8×(−(N-2)/(2(N+2))−1)+(N+4+2)×(N+6−1)/(N+2) = 0. We won’t check all of the others.

, but here are a couple to give you a sense. For the mixed U(1)-gravitational anomaly we have U(1): This has \( A_{\text{el}} = (N^2 - 1) + \frac{1}{2}N(N + 1) \times (-N^{-2} - 1) = (N-2)(N+1) \) where the contributions are from the gluino and the \(S\) field respectively. In the Spin(8) magnetic theory, we have \[ A_{\text{mag}} = 28 + 8(N + 4) \left( \frac{N - 2}{2(N + 2)} - 1 \right) + 8 \left( \frac{N^2 + 4}{2(N + 2)} - 1 \right)

\]

\[ + \frac{1}{2}(N + 4)(N + 5) \left( \frac{N + 6}{N + 2} - 1 \right) - \frac{N(N - 2)}{N + 2} - 1 = \frac{(N-2)(N+1)}{N+2} \]

while for the \(U(1)^3\) anomaly we have U(1)\(^3\): This has \( A_{\text{el}} = -\frac{1}{2}N(N + 1) \left( \frac{N-2}{N+2} + 1 \right)^3 \). Meanwhile, \[ A_{\text{mag}} = 28 + 8(N + 4) \left( \frac{N - 2}{2(N + 2)} - 1 \right)^3 + 8 \left( \frac{N^2 + 4}{2(N + 2)} - 1 \right)^3 \]

\[ + \frac{1}{2}(N + 4)(N + 5) \left( \frac{N + 6}{N + 2} - 1 \right)^3 - \frac{N(N - 2)}{N + 2} - 1 \]

A little algebra (or Mathematica) shows you that \(A_{\text{el}} = A_{\text{mag}}\). Needless to say, the other 't Hooft anomalies involving U(1)\(_F\) and mixed U(1)\(_R\), U(1)\(_F\) also coincide. As always, the agreement of these fairly complicated algebraic expressions gives some confidence that the two theories are indeed related in some way.

Consequences for the Infra-Red Dynamics Let’s now run with the conjecture that these two theories are dual. The magnetic Spin(8) theory has the one-loop beta function given by \[ b_0 = \frac{3}{2} \times (8-2) - \frac{1}{2}(N + 5) = \frac{1}{2}(13-N)

\]

We see that the theory is asymptotically free only when N < 13. But this agrees perfectly with our previous analysis of the conformal window of the electric theory! The duality tells us that the chiral theory is indeed infra-red free when N ≥ 13, but the free theory is a Spin(8) gauge theory, with the matter described above. Needless to say, it’s unlikely that we would have guessed this starting the SU(N) gauge theory. Meanwhile, for 2 ≤ N ≤ 12, both theories are expected to flow to an interacting SCFT. The statement of Pouliot duality here is that, once we include the superpotential (7.9), the two theories flow to the same SCFT.

A Deformation of the Duality As always, given a duality we can deform it in different ways to derive new (or perhaps old) dualities. Indeed, understanding how connections in the web of different dualities is an important consistency check on any new proposal. There are many ways to deform our chiral duality. Here we just mention two particularly straightforward ones. First, suppose that we add \[ W = \det S \quad (7.10)

\]

to the electric side. We have the same gauge theory, just with this additional superpotential. It’s obvious what happens on the magnetic side: the superpotential (7.9) becomes \[ W = M q \tilde{q} + U (\tilde{p} p + 1)

\]

where we’re not being careful about including coefficients, dimensionful or otherwise, for these various terms. The equation of motion for U now means that \(p \neq 0\) in the ground state. This induces a Higgs mechanism and breaks the magnetic gauge symmetry Spin(8) → Spin(7) in such a way that the other chiral superfields q, that previously transformed in \(\mathbf{8}\), now transform in the \(\mathbf{8}\) spinor representation of Spin(7). This gives us a new duality: the electric chiral theory with superpotential (7.10) is dual to Spin(7) gauge theory with N+4 chiral multiplets in the spinor representation \(\mathbf{8}\), coupled to singlets through \(W = M q \tilde{q}\). (This is actually the original “Pouliot duality”.) The magnetic theory is now infra-red free for any N ≥ 11. This version of Pouliot duality has a surprising feature. Our original SU(N) theory was a chiral gauge theory. But its Spin(7) dual is non-chiral! In particular, for N ≥ 11, the chiral SU(N) theory flows in the infra-red to the non-chiral Spin(7) theory. There is a lesson in this: the question of whether or not a theory is chiral depends on the energy scale at which you look. It is not a property that is preserved under RG.

Another Deformation Alternatively, we could give an expectation value to \(U = \det S\). On the electric side, this gives a mass to the spinor p, allowing us to integrate it out. We’re left just with SO(8) gauge theory coupled to N+4 chiral multiplets in the \(\mathbf{8}\), still, of course, coupled to the superpotential \(W = M q \tilde{q}\). (I’m ignoring global issues of the gauge group here.) What happens on the original electric side? We give an expectation value to the symmetric \(S \neq 0\). This breaks SU(N) → SO(N), so we’re left with an SO(N) gauge theory coupled to N +4 fundamental chiral multiplets. The claim is that this is dual to the SO(8) theory above. In fact, this is part of the SO(N) Seiberg dualities which, in general, relate an SO(N\(_c\)) theory to an SO(N\(_f\)-N\(_c\)+4) theory.

7.2.3 Briefly, the Konishi Anomaly There’s a loose thread hanging from our discussion of Pouliot duality. The electric theory includes two baryon operators \[ B = Q^N \tilde{Q}^N \quad \text{and} \quad B' = (Q^N \tilde{S})^N \]

We haven’t yet seen what they map to on the magnetic side. Happily, the Spin(8) theory also contains two baryon operators which, schematically, take the form \[ b = q^4 p^2 \quad \text{and} \quad b'' = q^8 \]

Here the \(q^8\) in \(b''\) are contracted with an epsilon tensor. We need a little group theory to explain how b is put together. The vectors q combine in an anti-symmetric fashion into 35 + 35 and the latter is contracted with the two spinors which combine symmetrically into 35 so that the whole thing is a singlet of Spin(8).

It seems reasonable to think that these operators might map into each other under duality. To see this, we can check the flavour and R-symmetry charges. We have F[B] = −N(N + 2) and R[B] = N 4N F[B′] = 2N and R[B′] = N + 2 and F[b] = −N(N + 2) and R[b] = N 4(N − 2)

F[b′′] = 4N and R[b′′] = N + 2

It’s close but, sadly, no cigar! First, it’s clear that under the duality we should match b ←→ B But while the flavour charge of B′ and b′′ agree, their R-charge does not! What’s going on?

In fact, there is a subtlety in this duality that didn’t rear its head in our previous examples. To fully understand the structure of chiral superfields, we should include one further field from each theory, each of which involves the chiral superfield that houses the field strength. We call this W for the electric theory and W  ̃ for the magnetic α α theory. Then consider B′′ = (Q  ̃ N−4 S N−2) W  W  ̃  and b′ = q4 W  ̃  W  ̃  ̃  α α α α If we use the fact that R[W 2] = R[ ̃W ̃ 2] = 2, we find F[B′′] = F[b′′] and R[B′′] = R[b′′]

and F[b′] = F[B′] and R[b′] = R[B′]. So this solves our matching problem: the baryons on one side are paired chiral fields that include the field strength of the other b′ ←→ B′ b′′ ←→ B′′ But this also opens up a whole can of worms! Why are we suddenly including the field strength in the story? Or, said differently, why didn’t we include the field strength in

## Section 6 when discussing SU(N) SQCD?

The answer to this is a little subtle. Here I don’t give all the details, but sketch the basic idea. It turns out that one can derive an equation in SQCD that, for each chiral multiplet, reads D  ̄ 2(Q†Q) = ∂W  1 ∂Q + 8π2 Tr W  W  α α This equation is known as the Konishi anomaly and is the supersymmetric version of the chiral anomaly which says that a rotation Q → e^{iα} Q results in a shift of the theta angle. It tells us that, at least as far as the chiral ring is concerned, the operator Tr W  W  can be replaced by Q∂W/∂Q, so we’re not missing anything if we neglect it.

α α However, in other theories there are a number of these additional chiral multiplets, dressed with W  , that you need to include. This first rears its head in the duality for α SO(N) theories (which we didn’t describe in these lectures notes, in part to duck this particular issue). For the chiral duality that we’ve described above, it turns out that you need to include the extra B′′ and b′ (and, in fact, one further operator from each theory that depends linearly on W  or W  ̃ respectively).

α α

7.2.4 Briefly, a-Maximisation We’ve seen a few times in these lectures that many theories don’t have a unique R- symmetry. Instead, we can always add any linear combination of other Abelian flavour symmetries and this also provides a good candidate R-symmetry. This becomes an issue only when we flow to an interacting SCFT, where the R-symmetry dictates the dimension of chiral operators Δ[O] = R[O]_{IR} But for this to be useful, we need to know exactly what R-symmetry we’re dealing with in the infra-red.

Happily, there is a simple prescription to determine this. This prescription, known as a-maximisation, is straightforward to state but somewhat harder to prove. Here we just give the statement, dressed with a little context.

First, in any conformal field theory the trace of the stress tensor necessarily vanishes: ⟨T^μ_μ⟩ = 0. At least, this is true in flat space. But if the theory is placed on a curved manifold, there is a so-called trace anomaly and we get ⟨T^μ_μ⟩ = c/ (16π^2) C_{μνρσ} C^{μνρσ} − a/ (16π^2) *R^{μνρσ} *R_{μνρσ} where C_{μνρσ} is the Weyl tensor and *R^{μνρσ} is the dual of the Riemann tensor. (We proved the analogous statement for 2d CFTs in the lectures on String Theory.) The two coefficients a and c are known as central charges and provide a way to characterise the CFT.

Of the two, a is the more interesting. First, it can be proven that a always de- creases under RG flow. Second, in superconformal field theories it turns out that a is determined by the R-charge a = 3/32 Σ_{fermions} [3R[ψ]^2 − R[ψ]^4]

where the sum should be taken over left-handed Weyl fermions.

Once again, it’s important that we use the right R-symmetry R_{IR} when computing the central charge a. However, the beauty of this calculation is that it gives us a way to figure out what the right central charge is. Suppose that we have a collection of candidate central charges in the UV, parameterised by some coefficients α as in (7.8).

For each of these we can compute the would-be central charge a(α) = 3/32 Σ_{fermions} [3R(α)[ψ]^2 − R(α)[ψ]^4]

The R-symmetry that appears in the superconformal algebra turns out to the one One that maximises the value of a. This gives a simple way to compute R and, therefore, the IR dimensions of chiral operators in the SCFT.

## 7.3 Dynamical Supersymmetry Breaking

All the gauge theories that we’ve discussed so far have supersymmetric vacua with vanishing energy. In some cases these vacua are pushed off to infinity by a runway potential, but we can always rescue them by giving masses to the matter multiplets, bringing them in to finite distance. One might wonder: do all supersymmetric gauge theories have supersymmetric ground states? Or is it possible that some gauge theories spontaneously break supersymmetry, with a ground state that has energy E > 0? We already met some models that break supersymmetry back in Section 3.4. There, we worked only with chiral multiplets and the game was to cook up a superpotential for which no critical points exist. In searching for gauge theories that break supersymmetry, the game is similar. The difference is that now there is the option for the superpotential to be generated by quantum effects. Such theories are said to break supersymmetry dynamically.

Where should we look for dynamical supersymmetry breaking? An obvious obstacle is the Witten index. This is non-vanishing for super Yang-Mills theory with any gauge group. (It is given by the dual Coxeter number and is listed for all gauge groups in Table 3.) If we add matter in any vector-like representation, we can always give it a mass and reduce to super Yang-Mills with its non-vanishing Witten index. This suggests two places to look for supersymmetry breaking. • We could consider chiral gauge theories in which it’s not possible to give the matter mass. • Alternatively, we could consider gauge theories with a quantum moduli space of vacua for which the Witten index is ill-defined. It may then be possible to deform these theories in some other way that doesn’t involve giving masses.

In this section, we give two examples of dynamical supersymmetry breaking, one of each kind.

7.3.1 The SU(3)×SU(2) Model

One of the simplest chiral gauge theories we can write down is based on the gauge group G = SU(3)×SU(2). We introduce a collection of four chiral multiplets, with quantum numbers given by SU(3) SU(2) U(1) U(1) U(1) U(1)′ Y R A A Q 3 2 1 −1 1 1 U 3 1 −4 0 1 0 D 3 1 2 0 1 0 L 1 2 −3 3 0 1 Λ7 1 1 1 0 −4 0 Λ4 1 1 1 0 0 −4 We’ve also included both non-anomalous and anomalous U(1) symmetries in this table. Classically there is a U(1)4 symmetry, but quantum mechanically only a U(1)2 survives. The anomalous U(1) symmetries are U(1) and U(1)′, as shown by the transformation of the strong coupling scales. The exponents in these strong coupling scales can be traced to the one-loop beta functions, which are SU(3) : b0 = 9−2 = 7 and SU(2) : b0 = 6−2 = 4. If you know the smallest amount of particle physics, these quantum numbers should look very familiar! They are the representations of the quarks and leptons of the Standard Model. (The right-handed electron is missing.) The symmetry U(1) coincides (up to a normalisation) with the hypercharge symmetry of the Standard Model, here a global rather than gauge symmetry.

It’s curious that, as we shall see, this theory dynamically breaks supersymmetry although it doesn’t seem particularly useful for real-world purposes: the MSSM must include the Higgs fields (which, of course, also sit in chiral multiplets). Various phenomenological constraints means that supersymmetry breaking is thought to take place in an entirely different sector before being communicated to the Standard Model by so-called “messenger” fields. Here we study the theory simply to get a feeling for what chiral gauge theories do.

First, the classical moduli space. As we’ve seen, this is parameterised by the gauge invariant holomorphic monomials. For our current theory, there are three: ˜ ˜ ˜ ˜ Y1 = UQL, Y2 = DQL, Z = UQDQ where the SU(2) gauge indices are contracted with an ϵab symbol in each. These have R-charge R[Y1] = R[Y2] = 2 and R[Z] = −2. This means that we can add a tree level superpotential that preserves the R-symmetry, Wtree = λDQL = λY2 with λ a (classically) dimensionless constant. This superpotential is renormalisable and also preserves U(1).

The superpotential Wtree lifts the vacuum moduli space. To see this, note that the critical point requires ∂Wtree/∂L = 0 ⇒ DQ = 0 ⇒ ˜Y = Z = 0 and ∂Wtree/∂D = 0 ⇒ QL = 0 ⇒ ˜Y1 = ˜Y2 = 0. This means that if there is supersymmetric ground state then it necessarily sits at the origin of moduli space where the theory is strongly coupled.

Now let’s turn to the quantum dynamics. For λ suitably small, we can ignore the tree-level superpotential and import our results from Section 6. Things are easiest if we assume that |Λ3| ≫ |Λ2| so that the SU(3) dynamics becomes strong first. In this case we have SU(3) with N = 2 flavours which, we know, is the situation where a non-perturbative superpotential is generated by instantons. Adding this to our tree-level superpotential gives Λ7 W = λY + 3 (7.11)

The quantum generated superpotential gives a runaway that pushes the ground state towards infinity. Meanwhile, we’ve already seen that the tree level superpotential pushes the ground state towards the origin. The net result is shown in Figure 16, with a ground state that sits at energy E > 0 and hence breaks supersymmetry.

Figure 16. The tree level superpotential, shown in green competes with the dynamically induced superpotential, shown in red. The sum of the two, shown in blue, has a minimum at E > 0 and so breaks supersymmetry.

The above analysis was very quick. You might wonder if perhaps one can play off the two contributions to find a minimum at zero energy after all. In fact there’s a cute argument that say this can’t happen. Here’s why. First note that each of Y, Y and Z carry non-zero R-charge. Wherever the minimum of (7.11) sits, one of these must get an expectation value and so R-symmetry is broken with a corresponding Goldstone mode called an R-axion. This is a compact scalar. If supersymmetry is unbroken, then there must be another non-compact, massless scalar that joins with the R-axion to form the lowest component of a chiral multiplet. Usually such non-compact scalars take us out along the moduli space. But we’ve seen that the moduli space is lifted by the tree-level superpotential, so no such massless scalar exists and supersymmetry is necessarily broken.

We could be more precise, finding the minima of the potential in terms of the fundamental fields but this is a little fiddly. However, there’s one feature that is important. From the form of the superpotential (7.11), we would expect the expectation value v of the fundamental fields to scale as v ∼ λ1/7 This means that for λ ≪ 1, we have v ≫ |Λ3| ≫ |Λ2|. As long as the expectation values break the gauge group completely the theory is weakly coupled and we can compute everything reliably. In particular, we are free to use the canonical Kähler potential in this regime.

7.3.2 The Quantum Moduli Space Revisited

As a second example of supersymmetry breaking, we take a theory that has a moduli space of vacua, and hence an ill defined Witten index. We then deform it in such a way that supersymmetry is broken.

To this end, consider SU(2) gauge theory coupled to four chiral multiplets Φi, i = 1,...,,4, each in the fundamental representation. The gauge invariant operators consist of six mesons Mij = ΦiΦjϵab a b (This is the Sp(1) language of Section 7.1. In the SU(2) language of Section 6, both mesons and baryons are housed in the 4×4 matrix Mij = −Mji.)

Classically, the mesons obey the constraint PfM = 0 where the Pfaffian is defined by PfM = ϵ MijMkl ijkl

We now add six singlet fields S = −S to our original theory. These couple to the original fields through the tree-level superpotential W = λS ΦiΦj tree ij This lifts the moduli space parameterised by M which must take value M = 0, but the theory retains a classical moduli space, parameterised by the expectation values of Sij.

Now we turn to the quantum theory. We know from our discussion in Section 6.3 (or from Section 7.1) that, before adding the singlets, the quantum moduli space is deformed in the quantum theory and becomes PfM = Λ4. The superpotential of our theory with the singlets is now W = λS Mij + X(PfM − Λ4)

ij with X a Lagrange multiplier field. But it’s clear that the equations of motion of X and of Sij cannot be simultaneously satisfied: therefore this simple model breaks supersymmetry17.

17This model was first proposed by Izawa and Yanagida and Intriligator and Thomas.

In fact, we should be a little more careful. This theory has a flat direction, albeit one with energy E > 0. To see suppose that we place ourselves far out along the classical direction S ̸= 0. This gives the original quarks Φ a large mass and so they can be integrated out. The low-energy superpotential is W ∼ (λ2Λ4S Sij)1/2 eff ij The behaviour on Sij follows on symmetry grounds, including the fact that R[S] = 2. The behaviour on the couplings can be deduced from matching scales after integrating out the quarks, with Λ6new = Λ4old m2 = Λ4old λ2S2 and the superpotential is simply W = Λ3new as in (6.12).

If we assume a canonical Kähler potential for S, then the superpotential (7.12) results in the potential V ∼ |λΛ2|2 S S†ij / |S Sij| ij

As we vary the phases of different Sij components, this potential diverges in some directions, but also has flat directions in which V ∼ |λΛ2|2.

Because we’ve broken supersymmetry, these flat directions will surely be lifted by quantum effects. (They are sometimes called pseudo-flat directions for this reason). The concern is that these quantum effects might lead to a runaway behaviour, so that rather than breaking supersymmetry we instead have a theory with no good ground state. Integrating out the quarks gives a logarithmic correction to the Kähler potential for S, along the l lines of (3.38). You need to be careful about the signs, but it turns out that this causes the potential to grow as we move out along the flat directions. The ground state is pushed towards smaller values of S and breaks supersymmetry. Because this model is vector like, we could add masses for the quark fields. What then happens? To see this, it’s actually useful to add two mass terms: one for the quarks and another for S. After the quantum modification of the moduli space, the superpotential becomes W = λS Mij + m Mij + \tilde{m} PfS + X(PfM − Λ4)

Now there are supersymmetric ground states! They sit at Mij ∼ ε_{ijklm} (Λ4 / (Pf_m \tilde{m}))^{1/2} and S ∼ (Λ4 / (Pf_m \tilde{m}))^{1/2} The square roots allow for two different signs, and these are the two expected supersymmetric ground states since Tr(−1)^F e^{−βH} = 2 for SU(2) super Yang-Mills. But we can also see what happens as the masses are removed. As m → 0, we get a smooth limit for Mij (because Pf_m ∼ m^2). But as \tilde{m} → 0, the supersymmetric ground state decouples as S → ∞. Naively, one might think that this leads to runaway behaviour (as it does, for example, for SU(N) with N < N flavours). The novelty in the current case is that there is an infinite barrier between the supersymmetric ground state at S → ∞ and the supersymmetry breaking ground state at finite S. If you like, the maximum of this barrier must also have moved off to infinity as \tilde{m} → 0.

It is straightforward to construct generalisations of this model using other theories that exhibit a quantum deformed moduli space, including SU(N) with N = N and Sp(N) with N = N +1.

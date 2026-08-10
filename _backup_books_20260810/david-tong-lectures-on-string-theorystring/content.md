# David Tong Lectures on String Theorystring

> 来源文件：pre_David_Tong_Lectures_on_String_Theorystring.txt
> 字符数（约）：397946
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

January 2009 Preprint typeset in JHEP style - HYPER VERSION String Theory University of Cambridge Part III Mathematical Tripos Dr David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 0WA, UK http://www.damtp.cam.ac.uk/user/tong/string.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources • J. Polchinski, String Theory This two volume work is the standard introduction to the subject. Our lectures will more or less follow the path laid down in volume one covering the bosonic string. The book contains explanations and descriptions of many details that have been deliberately (and, I suspect, at times inadvertently) swept under a very large rug in these lectures. Volume two covers the superstring.

• M. Green, J. Schwarz and E. Witten, Superstring Theory Another two volume set. It is now over 20 years old and takes a slightly old-fashioned route through the subject, with no explicit mention of conformal field theory. However, it does contain much good material and the explanations are uniformly excellent. Volume one is most relevant for these lectures.

• B. Zwiebach, A First Course in String Theory This book grew out of a course given to undergraduates who had no previous exposure to general relativity or quantum field theory. It has wonderful pedagogical discussions of the basics of lightcone quantization. More surprisingly, it also has some very clear descriptions of several advanced topics, even though it misses out all the bits in between.

• P. Di Francesco, P. Mathieu and D. Sénéchal, Conformal Field Theory This big yellow book is affectionately known as the yellow pages. It’s a great way to learn conformal field theory. At first glance, it comes across as slightly daunting because it’s big. (And yellow). But you soon realise that it’s big because it starts at the beginning and provides detailed explanations at every step. The material necessary for this course can be found in chapters 5 and 6.

Further References: “String Theory and M-Theory” by Becker, Becker and Schwarz and “String Theory in a Nutshell” (it’s a big nutshell) by Kiritsis both deal with the bosonic string fairly quickly, but include more advanced topics that may be of interest. The book “D-Branes” by Johnson has lively and clear discussions about the many joys of D-branes. Links to several excellent online resources, including video lectures by Shiraz Minwalla, are listed on the course webpage.

Contents

## 0. Introduction

## 0.1 Quantum Gravity

## 1. The Relativistic String

## 1.1 The Relativistic Point Particle

1.1.1 Quantization 11 1.1.2 Einbein 13

## 1.2 The Nambu-Goto Action

1.2.1 Symmetries of the Nambu-Goto Action 17 1.2.2 Equations of Motion 18

## 1.3 The Polyakov Action

1.3.1 Symmetries of the Polyakov Action 20 1.3.2 Fixing a Gauge 22

## 1.4 Mode Expansions

1.4.1 The Constraints Revisited 26

## 2. The Quantum String

## 2.1 A Lightning Look at Covariant Quantization

2.1.1 Ghosts 30 2.1.2 Constraints 30

## 2.2 Lightcone Quantization

2.2.1 Lightcone Gauge 33 2.2.2 Quantization 36

## 2.3 The String Spectrum

2.3.1 The Tachyon 40 2.3.2 The First Excited States 41 2.3.3 Higher Excited States 45

## 2.4 Lorentz Invariance Revisited

## 2.5 A Nod to the Superstring

## 3. Open Strings and D-Branes

## 3.1 Quantization

3.1.1 The Ground State 54 3.1.2 First Excited States: A World of Light 55 3.1.3 Higher Excited States and Regge Trajectories 56 3.1.4 Another Nod to the Superstring 56

## 3.2 Brane Dynamics: The Dirac Action

## 3.3 Multiple Branes: A World of Glue

## 4. Introducing Conformal Field Theory

4.0.1 Euclidean Space 62 4.0.2 The Holomorphy of Conformal Transformations 63

## 4.1 Classical Aspects

4.1.1 The Stress-Energy Tensor 64 4.1.2 Noether Currents 66 4.1.3 An Example: The Free Scalar Field 67

## 4.2 Quantum Aspects

4.2.1 Operator Product Expansion 68 4.2.2 Ward Identities 70 4.2.3 Primary Operators 73

## 4.3 An Example: The Free Scalar Field

4.3.1 The Propagator 77 4.3.2 An Aside: No Goldstone Bosons in Two Dimensions 79 4.3.3 The Stress-Energy Tensor and Primary Operators 80

## 4.4 The Central Charge

4.4.1 c is for Casimir 85 4.4.2 The Weyl Anomaly 86 4.4.3 c is for Cardy 89 4.4.4 c has a Theorem 91

## 4.5 The Virasoro Algebra

4.5.1 Radial Quantization 94 4.5.2 The Virasoro Algebra 97 4.5.3 Representations of the Virasoro Algebra 99 4.5.4 Consequences of Unitarity 100

## 4.6 The State-Operator Map

4.6.1 Some Simple Consequences 104 4.6.2 Our Favourite Example: The Free Scalar Field 105

## 4.7 Brief Comments on Conformal Field Theories with Boundaries

## 5. The Polyakov Path Integral and Ghosts

## 5.1 The Path Integral

5.1.1 The Faddeev-Popov Method 111 5.1.2 The Faddeev-Popov Determinant 114 5.1.3 Ghosts 115

## 5.2 The Ghost CFT

## 5.3 The Critical “Dimension” of String Theory

5.3.1 The Usual Nod to the Superstring 120 5.3.2 An Aside: Non-Critical Strings 121

## 5.4 States and Vertex Operators

5.4.1 An Example: Closed Strings in Flat Space 124 2 An Example: Open Strings in Flat Space 125 5.4.3 More General CFTs 126

## 6. String Interactions

## 6.1 What to Compute?

6.1.1 Summing Over Topologies 129

## 6.2 Closed String Amplitudes at Tree Level

6.2.1 Remnant Gauge Symmetry: SL(2,C) 132 6.2.2 The Virasoro-Shapiro Amplitude 134 6.2.3 Lessons to Learn 137

## 6.3 Open String Scattering

6.3.1 The Veneziano Amplitude 143 6.3.2 The Tension of D-Branes 144

## 6.4 One-Loop Amplitudes

6.4.1 The Moduli Space of the Torus 145 6.4.2 The One-Loop Partition Function 148 6.4.3 Interpreting the String Partition Function 151 6.4.4 So is String Theory Finite? 154 6.4.5 Beyond Perturbation Theory? 155

## 6.5 Appendix: Games with Integrals and Gamma Functions

## 7. Low Energy Effective Actions

## 7.1 Einstein’s Equations

7.1.1 The Beta Function 161 7.1.2 Ricci Flow 165

## 7.2 Other Couplings

7.2.1 Charged Strings and the B field 165 7.2.2 The Dilaton 167 7.2.3 Beta Functions 169

## 7.3 The Low-Energy Effective Action

7.3.1 String Frame and Einstein Frame 170 7.3.2 Corrections to Einstein’s Equations 172 7.3.3 Nodding Once More to the Superstring 173

## 7.4 Some Simple Solutions

7.4.1 Compactifications 176 7.4.2 The String Itself 177 7.4.3 Magnetic Branes 179 7.4.4 Moving Away from the Critical Dimension 182 7.4.5 The Elephant in the Room: The Tachyon 185

## 7.5 D-Branes Revisited: Background Gauge Fields

7.5.1 The Beta Function 186 7.5.2 The Born-Infeld Action 189

## 7.6 The DBI Action

7.6.1 Coupling to Closed String Fields 191

## 7.7 The Yang-Mills Action

7.7.1 D-Branes in Type II Superstring Theories 197

## 8. Compactification and T-Duality

## 8.1 The View from Spacetime

8.1.1 Moving around the Circle 201

## 8.2 The View from the Worldsheet

8.2.1 Massless States 204 8.2.2 Charged Fields 204 8.2.3 Enhanced Gauge Symmetry 205

## 8.3 Why Big Circles are the Same as Small Circles

8.3.1 A Path Integral Derivation of T-Duality 208 8.3.2 T-Duality for Open Strings 209 8.3.3 T-Duality for Superstrings 210 8.3.4 Mirror Symmetry 210

## 8.4 Epilogue

Acknowledgements These lectures are aimed at beginning graduate students. They assume a working knowledge of quantum field theory and general relativity. The lectures were given over one semester and are based broadly on Volume one of the book by Joe Polchinski. I inherited the course from Michael Green whose notes were extremely useful. I also benefited enormously from the insightful and entertaining video lectures by Shiraz Minwalla.

I’m grateful to Anirban Basu, Niklas Beisert, Joe Bhaseen, Diego Correa, Nick Dorey, Michael Green, Anshuman Maharana, Malcolm Perry and Martin Schnabl for discussions and help with various aspects of these notes. I’m also grateful to the students, especially Carlos Guedes, for their excellent questions and superhuman typo-spotting abilities. Finally, my thanks to Alex Considine for infinite patience and understanding over the weeks these notes were written. I am supported by the Royal Society.

## 0. Introduction

String theory is an ambitious project. It purports to be an all-encompassing theory of the universe, unifying the forces of nature, including gravity, in a single quantum mechanical framework.

The premise of string theory is that, at the fundamental level, matter does not consist of point-particles but rather of tiny loops of string. From this slightly absurd beginning, the laws of physics emerge. General relativity, electromagnetism and Yang-Mills gauge theories all appear in a surprising fashion. However, they come with baggage. String theory gives rise to a host of other ingredients, most strikingly extra spatial dimensions of the universe beyond the three that we have observed. The purpose of this course is to understand these statements in detail.

These lectures differ from most other courses that you will take in a physics degree. String theory is speculative science. There is no experimental evidence that string theory is the correct description of our world and scant hope that hard evidence will arise in the near future. Moreover, string theory is very much a work in progress and certain aspects of the theory are far from understood. Unresolved issues abound and it seems likely that the final formulation has yet to be written. For these reasons, I’ll begin this introduction by suggesting some answers to the question: Why study string theory?

Reason 1. String theory is a theory of quantum gravity String theory unifies Einstein’s theory of general relativity with quantum mechanics. Moreover, it does so in a manner that retains the explicit connection with both quantum theory and the low-energy description of spacetime.

But quantum gravity contains many puzzles, both technical and conceptual. What does spacetime look like at the shortest distance scales? How can we understand physics if the causal structure fluctuates quantum mechanically? Is the big bang truly the beginning of time? Do singularities that arise in black holes really signify the end of time? What is the microscopic origin of black 黑洞熵以及它告诉我们什么？信息悖论的解决方案是什么？这些问题中的一部分将在本引言的后续部分进行回顾。无论弦理论是否是现实的真实描述，它都提供了一个框架，使人们可以开始探索这些问题。对于某些问题，弦理论已经给出了非常令人印象深刻且令人信服的答案。而对于其他问题，弦理论则几乎保持沉默。

理由二：弦理论可能是量子引力理论粗略来看，弦理论似乎是描述现实世界的一个极好的候选者。在低能下，它自然地引出了广义相对论、规范理论、标量场和手征费米子。换句话说，它包含了构成我们宇宙的所有要素。它也为宇宙常数的值提供了目前唯一可信的解释，尽管公平地说，我应该补充一点，这个解释对某些人来说是如此令人反感，以至于学术界相当有趣地分裂为这究竟是好事还是坏事。此外，弦理论还包含了一些目前尚无实验证据但被认为是超越标准模型物理学的可能候选者的想法。主要例子是超对称性和轴子。

然而，尽管粗略的图景看起来不错，但更精细的细节仍有待描绘。弦理论并未为低能物理提供独特的预测，而是提供了一系列令人困惑的可能性，这些可能性大多取决于那些额外维度中隐藏着什么。部分而言，这个问题是任何量子引力理论所固有的：正如我们即将回顾的，从普朗克尺度到大型强子对撞机探索的日常能量尺度，路途遥远。使用量子引力来提取粒子物理学的预测，类似于使用量子色动力学来提取咖啡机如何工作的预测。但仅仅因为困难，如果我们正在寻找令人信服的证据来证明弦理论描述了我们所生活的世界，这并不能带来多少安慰。

虽然弦理论目前无法提供可证伪的预测，但它确实激发了新的、富有想象力的提议，以解决粒子物理学和宇宙学中的未决问题。存在一些弦理论可能在未来的实验中显现自身的场景。也许我们会在大型强子对撞机上发现额外维度，也许我们会看到横跨天空的基本弦网络，或者也许我们会在宇宙微波背景辐射中探测到某种非高斯性的特征，这是暴胀期间D膜作用的标志。然而，我个人的感觉是，这些可能性都很渺茫，我们可能在有生之年都不会知道弦理论是对是错。当然，物理学的历史充满了错误的否定者，他们错误地暗示各种理论将永远无法被检验。运气好的话，我也会成为他们中的一员。

理由三：弦理论为规范理论提供了新的视角弦理论诞生于理解强相互作用的尝试。近四十年后，这仍然是该领域的主要动机之一。弦理论提供了分析量子场论中接地气方面的工具，这些方面与关于引力和黑 holes 的高深思想相去甚远。

与本课程直接相关的是投入时间学习弦理论的教学理由。其核心是共形场论和规范对称性的研究。我们将学到的技术并非弦理论所独有，而是适用于无数系统，这些系统直接应用于现实世界的物理学。

在更深层次上，弦理论为理解量子规范理论的某些方面提供了新的、非常令人惊讶的方法。其中最令人震惊的是AdS/CFT对应关系，最初由胡安·马尔达塞纳提出，它给出了强耦合量子场论与高维引力之间的关系。这些思想已被应用于从核物理到凝聚态物理的领域，并为强耦合现象提供了定性（且可以说是定量）的见解。

理由四：弦理论为数学提供了新的结果在过去的250年里，数学与物理学之间的密切关系几乎是一条单行道：物理学家从数学家那里借鉴了许多东西，但除了少数几个显著的例外，回馈甚少。近年来，这种情况发生了变化。弦理论和量子场论的思想和技术已被用来给出新的“证明”，并且或许更重要的是，为数学指明了新的方向和提供了新的见解。其中最著名的是镜像对称性，这是拓扑上不同的卡拉比-丘流形之间的一种关系。

上述四个理由也粗略地描述了弦理论社群：有“相对论者”、“唯象学家”、“场论者”和“数学家”。当然，这些不同子学科之间的界限 are not fixed and one of the great attractions of string theory is its ability to bring together people working in different areas — from cosmology to condensed matter to pure mathematics — and provide a framework in which they can profitably communicate. In my opinion, it is this cross-fertilization between fields which is the greatest strength of string theory.

## 0.1 Quantum Gravity

This is a starter course in string theory. Our focus will be on the perturbative approach to the bosonic string and, in particular, why this gives a consistent theory of quantum gravity. Before we leap into this, it is probably best to say a few words about quantum gravity itself. Like why it’s hard. And why it’s important. (And why it’s not).

The Einstein Hilbert action is given by S_EH = 1/(16πG) ∫ d^4x √(-g) R Newton’s constant G can be written as 8πG = ℏc / N M_pl^2 Throughout these lectures we work in units with ℏ = c = 1. The Planck mass M_pl defines an energy scale M_pl ≈ 2×10^18 GeV.

(This is sometimes referred to as the reduced Planck mass, to distinguish it from the scale without the factor of 8π, namely 1/√G ≈ 1×10^19 GeV).

There are a couple of simple lessons that we can already take from this. The first is that the relevant coupling in the quantum theory is 1/M_pl. To see that this is indeed the case from the perspective of the action, we consider small perturbations around flat Minkowski space, g_μν = η_μν + h_μν The factor of 1/M_pl is there to ensure that when we expand out the Einstein-Hilbert action, the kinetic term for h is canonically normalized, meaning that it comes with no powers of M_pl. This then gives the kind of theory that you met in your first course on quantum field theory, albeit with an infinite series of interaction terms, S_EH = ∫ d^4x [ (∂h)^2/M_pl + h(∂h)^2/M_pl^2 + h^2(∂h)^2/M_pl^2 + ... ]

Each of these terms is schematic: if you were to do this explicitly, you would find a mess of indices contracted in different ways. We see that the interactions are suppressed by powers of M_pl. This means that quantum perturbation theory is an expansion in the dimensionless ratio E^2/M_pl^2, where E is the energy associated to the process of interest. We learn that gravity is weak, and therefore under control, at low-energies. But gravitational interactions become strong as the energy involved approaches the Planck scale. In the language of the renormalization group, couplings of this type are known as irrelevant.

The second lesson to take away is that the Planck scale M_pl is very very large. The LHC will probe the electroweak scale, M_EW ∼ 10^3 GeV. The ratio is M_EW/M_pl ∼ 10^−15. For this reason, quantum gravity will not affect your daily life, even if your daily life involves the study of the most extreme observable conditions in the universe.

Gravity is Non-Renormalizable Quantum field theories with irrelevant couplings are typically ill-behaved at high-energies, rendering the theory ill-defined. Gravity is no exception. Theories of this type are called non-renormalizable, which means that the divergences that appear in the Feynman diagram expansion cannot be absorbed by a finite number of counterterms. In pure Einstein gravity, the symmetries of the theory are enough to ensure that the one-loop S-matrix is finite. The first divergence occurs at two-loops and requires the introduction of a counterterm of the form, Γ_ε ∼ 1/(ε M_pl^4) ∫ d^4x √(-g) R_μν R_ρσ R_λκ g^ρσ g^λκ g^μν with ε = 4−D. All indications point towards the fact that this is the first in an infinite number of necessary counterterms.

Coupling gravity to matter requires an interaction term of the form, S_int = ∫ d^4x h_μν T^μν + O(h^2)

This makes the situation marginally worse, with the first divergence now appearing at one-loop. The Feynman diagram shows particle scattering through the exchange of two gravitons. When the momentum k running in the loop is large, the diagram is badly divergent: it scales as 1/M_pl^4 ∫^∞ d^4k

Non-renormalizable theories are commonplace in the history of physics, the most commonly cited example being Fermi’s theory of the weak interaction. The first thing to say about them is that they are far from useless! Non-renormalizable theories are typically viewed as effective field theories, valid only up to some energy scale Λ. One deals with the divergences by simply admitting ignorance beyond this scale and treating Λ as a UV cut-off on any momentum integral. In this way, we get results which are valid to an accuracy of E/Λ (perhaps raised to some power). In the case of the weak interaction, Fermi’s theory accurately predicts physics up to an energy scale of 1/√G ∼ 100 GeV. In the case of quantum gravity, Einstein’s theory works to an accuracy of (E/M_pl)^2.

However, non-renormalizable theories are typically unable to describe physics at their cut-off scale Λ or beyond. This is because they are missing the true ultra-violet degrees of freedom which tame the hi high-energy behaviour. In the case of the weak force, these new degrees of freedom are the W and Z bosons. We would like to know what missing degrees of freedom are needed to complete gravity.

Singularities Only a particle physicist would phrase all questions about the universe in terms of scattering amplitudes. In general relativity we typically think about the geometry as a whole, rather than bastardizing the Einstein-Hilbert action and discussing perturbations around flat space. In this language, the question of high-energy physics turns into one of short distance physics. Classical general relativity is not to be trusted in regions where the curvature of spacetime approaches the Planck scale and ultimately becomes singular. A quantum theory of gravity should resolve these singularities.

The question of spacetime singularities is morally equivalent to that of high-energy scattering. Both probe the ultra-violet nature of gravity. A spacetime geometry is made of a coherent collection of gravitons, just as the electric and magnetic fields in a laser are made from a collection of photons. The short distance structure of spacetime is governed – after Fourier transform – by high momentum gravitons. Understanding spacetime singularities and high-energy scattering are different sides of the same coin.

There are two situations in general relativity where singularity theorems tell us that the curvature of spacetime gets large: at the big bang and in the center of a black hole. These provide two of the biggest challenges to any putative theory of quantum gravity.

Gravity is Subtle It is often said that general relativity contains the seeds of its own destruction. The theory is unable to predict physics at the Planck scale and freely admits to it. Problems such as non-renormalizability and singularities are, in a Rumsfeldian sense, known unknowns. However, the full story is more complicated and subtle. On the one hand, the issue of non-renormalizability may not quite be the crisis that it first appears. On the other hand, some aspects of quantum gravity suggest that general relativity isn’t as honest about its own failings as is usually advertised. The theory hosts a number of unknown unknowns, things that we didn’t even know that we didn’t know. We won’t have a whole lot to say about these issues in this course, but you should be aware of them. Here I mention only a few salient points.

Firstly, there is a key difference between Fermi’s theory of the weak interaction and gravity. Fermi’s theory was unable to provide predictions for any scattering process at energies above √(1/G). In contrast, if we scatter two objects at extremely high-energies in gravity — say, at energies E ≫ M_pl — then we know exactly what will happen: we form a big black hole. We don’t need quantum gravity to tell us this. Classical general relativity is sufficient. If we restrict attention to scattering, the crisis of non-renormalizability is not problematic at ultra-high energies. It’s troublesome only within a window of energies around the Planck scale.

Similar caveats hold for singularities. If you are foolish enough to jump into a black hole, then you’re on your own: without a theory of quantum gravity, no one can tell you what fate lies in store at the singularity. Yet, if you are smart and stay outside of the black hole, you’ll be hard pushed to see any effects of quantum gravity. This is because Nature has conspired to hide Planck scale curvatures from our inquisitive eyes. In the case of black holes this is achieved through cosmic censorship which is a conjecture in classical general relativity that says singularities are hidden behind horizons. In the case of the big bang, it is achieved through inflation, washing away any traces from the very early universe. Nature appears to shield us from the effects of quantum gravity, whether in high-energy scattering or in singularities. I think it’s fair to say that no one knows if this conspiracy is pointing at something deep, or is merely inconvenient for scientists trying to probe the Planck scale.

While horizons may protect us from the worst excesses of singularities, they come with problems of their own. These are the unknown unknowns: difficulties that arise when curvatures are small and general relativity says “trust me”. The entropy of black holes and the associated paradox of information loss strongly suggest that local quantum field theory breaks down at macroscopic distance scales. Attempts to formulate quantum gravity in de Sitter space, or in the presence of eternal inflation, hint at similar difficulties. Ideas of holography, black hole complimentarity and the AdS/CFT correspondence all point towards non-local effects and the emergence of spacetime. These are the deep puzzles of quantum gravity and their relationship to the ultra-violet properties of gravity is unclear.

As a final thought, let me mention the one observation that has an outside chance of being related to quantum gravity: the cosmological constant. With an energy scale of Λ ∼ 10−3 eV it appears to have little to do with ultra-violet physics. If it does have its origins in a theory of quantum gravity, it must either be due to some subtle “unknown unknown”, or because it is explained away as an environmental quantity as in string theory.

Is the Time Ripe?

Our current understanding of physics, embodied in the standard model, is valid up to energy scales of 103 GeV. This is 15 orders of magnitude away from the Planck scale. Why do we think the time is now ripe to tackle quantum gravity? Surely we are like the ancient Greeks arguing about atomism. Why on earth do we believe that we’ve developed the right tools to even address the question?

The honest answer, I think, is hubris. However, there is mild circumstantial evidence that the framework of quantum field theory might hold all the way to the Planck scale without anything very dramatic happening in between. The main argument is unification. The three coupling constants of Nature run logarithmically, meeting miraculously at the GUT energy scale of 1015 GeV. Just slightly later, the fourth force of Nature, gravity, joins them. While not overwhelming, this does provide a hint that perhaps quantum field theory can be taken seriously at these ridiculous scales. Historically I suspect this was what convinced large parts of the community that it was ok to speak about processes at 1018 GeV.

Finally, perhaps the most compelling argument for studying physics at the Planck scale is that string theory does provide a consistent unified quantum theory of gravity and the other forces. Given that we have this theory sitting in our laps, it would be foolish not to explore its consequences. The purpose of these lecture notes is to begin this journey.

## 1. The Relativistic String

All lecture courses on string theory start with a discussion of the point particle. Ours is no exception. We’ll take a flying tour through the physics of the relativistic point particle and extract a couple of important lessons that we’ll take with us as we move onto string theory.

## 1.1 The Relativistic Point Particle

We want to write down the Lagrangian describing a relativistic particle of mass m. In anticipation of string theory, we’ll consider D-dimensional Minkowski space R1,D−1. Throughout these notes, we work with signature ηµν = diag(−1,+1,+1,...,+1). Note that this is the opposite signature to my quantum field theory notes.

If we fix a frame with coordinates Xµ = (t,(cid:126)x) the action is simple: S = −m ∫ dt √(1−(cid:126)x·(cid:126)x) . (1.1)

To see that this is correct we can compute the momentum p(cid:126), conjugate to (cid:126)x, and the energy E which is equal to the Hamiltonian, p(cid:126) = m(cid:126)x / √(1−(cid:126)x·(cid:126)x) , E = √(m2 +p(cid:126)2) , both of which should be familiar from courses on special relativity.

Although the Lagrangian (1.1) is correct, it’s not fully satisfactory. The reason is that time t and space (cid:126)x play very different roles in this Lagrangian. The position (cid:126)x is a dynamical degree of freedom. In contrast, time t is merely a parameter providing a label for the position. Yet Lorentz transformations are supposed to mix up t and (cid:126)x and such symmetries are not completely obvious in (1.1). Can we find a new Lagrangian in which time and space are on equal footing?

One possibility is to treat both time and space as labels. This leads us to the concept of field theory. However, in this course we will be more interested in the other possibility: we will promote time to a dynamical degree of freedom. At first glance, this may appear odd: the number of degrees of freedom is one of the crudest ways we have to characterize a system. We shouldn’t be able to add more degrees of freedom at will without fundamentally changing the system that we’re talking about. Another way of saying this is that the particle has the option to move in space, but it doesn’t have the option to move in time. It has to move in time. So we somehow need a way to promote time to a degree of freedom without it really being a true dynamical degree of freedom! How do we do this? The answer, as we will now show, is gauge symmetry.

Consider the action, S = −m ∫ dτ √(−X ˙µX ˙νηµν) , (1.2)

where µ = 0,...,D − 1 and X ˙µ = dXµ/dτ. We’ve introduced a new parameter τ which labels the position along the worldline of the particle as shown by the dashed lines in the figure. This action has a simple interpretation: it is just the proper time ds along the worldline.

Naively it looks as if we now have D physical degrees of freedom rather than D −1 because, as promised, the time direction X0 ≡ t is among our dynamical variables: X0 = X0(τ). However, this is an illusion. To see why, we need to note that the action (1.2) has a very important property: reparameterization invariance. This means that we can pick a different parameter τ̃ on the worldline, related to τ by any monotonic function τ̃ = τ̃(τ).

Let’s check that the action is invariant under transformations of this type. The integration measure in the action changes as dτ = dτ̃|dτ/dτ̃|. Meanwhile, the velocities change as dXµ/dτ = (dXµ/dτ̃)(dτ̃/dτ). Putting this together, we see that the action can just as well be written in the τ̃ reparameterization, S = −m ∫ dτ̃ √(−η_{\mu\nu} (dXµ/dτ̃)(dXν/dτ̃)).

The upshot of this is that not all D degrees of freedom Xµ are physical. For example, suppose you find a solution to this system, so that you know how X0 changes with τ and how X1 changes with τ and so on. Not all of that information is meaningful because τ itself is not meaningful. In particular, we could use our reparameterization invariance to simply set τ = X0(τ) ≡ t (1.3)

If we plug this choice into the action (1.2) then we recover our initial action (1.1). The reparameterization invariance is a gauge symmetry of the system. Like all gauge symmetries, it’s not really a symmetry at all. Rather, it is a redundancy in our description. In the present case, it means that although we seem to have D degrees of freedom Xµ, one of them is fake.

The fact that one of the degrees of freedom is a fake also shows up if we look at the momenta, pµ = ∂L/∂Ẋµ = mẊν η_{\mu\nu} / √(−Ẋλ Ẋρ η_{λρ}) (1.4)

These momenta aren’t all independent. They satisfy pµ pµ + m² = 0 (1.5)

This is a constraint on the system. It is, of course, the mass-shell constraint for a relativistic particle of mass m. From the worldline perspective, it tells us that the particle isn’t allowed to sit still in Minkowski space: at the very least, it had better keep moving in a timelike direction with (p0)² ≥ m².

One advantage of the action (1.2) is that the Poincaré symmetry of the particle is now manifest, appearing as a global symmetry on the worldline Xµ → Λ^µ_ν Xν + cµ (1.6)

where Λ is a Lorentz transformation satisfying Λ^µ_ρ η_{\mu\nu} Λ^ν_σ = η_{ρσ}, while cµ corresponds to a constant translation. We have made all the symmetries manifest at the price of introducing a gauge symmetry into our system. A similar gauge symmetry will arise in the relativistic string and much of this course will be devoted to understanding its consequences.

1.1.1 Quantization It’s a trivial matter to quantize this action. We introduce a wavefunction Ψ(X). This satisfies the usual Schrödinger equation, i ∂Ψ/∂τ = HΨ.

But, computing the Hamiltonian H = Ẋµ pµ − L, we find that it vanishes: H = 0. This shouldn’t be surprising. It is simply telling us that the wavefunction doesn’t depend on τ. Since the wavefunction is something physical while, as we have seen, τ is not, this is to be expected. Note that this doesn’t mean that time has dropped out of the problem. On the contrary, in this relativistic context, time X0 is an operator, just like the spatial coordinates x⃗. This means that the wavefunction Ψ is immediately a function of space and time. It is not like a static state in quantum mechanics, but more akin to the fully integrated solution to the non-relativistic Schrödinger equation.

The classical system has a constraint given by (1.5). In the quantum theory, we impose this constraint as an operator equation on the wavefunction, namely (pµ pµ + m²)Ψ = 0. Using the usual representation of the momentum operator pµ = −i∂/∂Xµ, we recognize this constraint as the Klein-Gordon equation (−η_{\mu\nu} ∂/∂Xµ ∂/∂Xν + m²) Ψ(X) = 0 (1.7)

Although this equation is familiar from field theory, it’s important to realize that the interpretation is somewhat different. In relativistic field theory, the Klein-Gordon equation is the equation of motion obeyed by a scalar field. In relativistic quantum mechanics, it is the equation obeyed by the wavefunction. In the early days of field theory, the fact that these two equations are the same led people to think one should view the wavefunction as a classical field and quantize it a second time. This isn’t correct, but nonetheless the language has stuck and it is common to talk about the point particle perspective as “first quantization” and the field theory perspective as “second quantization”.

So far we’ve considered only a free point particle. How can we introduce interactions into this framework? We would have to first decide which interactions are allowed: perhaps the particle can split into two; perhaps it can fuse with other particles? Obviously, there is a huge range of options for us to choose from. We would then assign amplitudes for these processes to happen. There would be certain restrictions coming from the requirement of unitarity which, among other things, would lead to the necessity of anti-particles. We could draw diagrams associated to the different interactions — an example is given in the figure — and in this manner we would slowly build up the Feynman diagram expansion that is familiar from field theory. In fact, this was pretty much the way Feynman h himself approached the topic of QED. However, in practice we rarely construct particle interactions in this way because the field theory framework provides a much better way of looking at things. In contrast, this way of building up interactions is exactly what we will later do for strings.

1.1.2 Einbein There is another action that describes the relativistic point particle. We introduce yet another field on the worldline, e(τ), and write S = ∫ dτ e⁻¹(Ẋ² − e²m²), (1.8)

where we’ve used the notation Ẋ² = Ẋ^μ Ẋ^ν η_μν. For the rest of these lectures, terms like X² will always mean an implicit contraction with the spacetime Minkowski metric. This form of the action makes it look as if we have coupled the worldline theory to 1d gravity, with the field e(τ) acting as an einbein (in the sense of vierbeins that are introduced in general relativity). To see this, note that we could change notation and write this action in the more suggestive form S = −∫ dτ √(−g) (g_ττ Ẋ² + m²), (1.9)

where g = (g_ττ)⁻¹ is the metric on the worldline and e = −g_ττ.

Although our action appears to have one more degree of freedom, e, it can be easily checked that it has the same equations of motion as (1.2). The reason for this is that e is completely fixed by its equation of motion, Ẋ² + e²m² = 0. Substituting this into the action (1.8) recovers (1.2).

The action (1.8) has a couple of advantages over (1.2). Firstly, it works for massless particles with m = 0. Secondly, the absence of the annoying square root means that it’s easier to quantize in a path integral framework.

The action (1.8) retains invariance under reparameterizations which are now written in a form that looks more like general relativity. For transformations parameterized by an infinitesimal η, we have τ → τ̃ = τ − η(τ), δe = d/dτ (η(τ)e), δX^μ = η(τ) dX^μ/dτ (1.10)

The einbein e transforms as a density on the worldline, while each of the coordinates X^μ transforms as a worldline scalar.

## 1.2 The Nambu-Goto Action

A particle sweeps out a worldline in Minkowski space. A string sweeps out a worldsheet. We’ll parameterize this worldsheet by one timelike coordinate τ, and one spacelike coordinate σ. In this section we’ll focus on closed strings and take σ to be periodic, with range σ ∈ [0, 2π). (1.11)

We will sometimes package the two worldsheet coordinates together as σ^α = (τ, σ), α = 0,1. Then the string sweeps out a surface in spacetime which defines a map from the worldsheet to Minkowski space, X^μ(σ, τ) with μ = 0,...,D−1. For closed strings, we require X^μ(σ, τ) = X^μ(σ + 2π, τ).

In this context, spacetime is sometimes referred to as the target space to distinguish it from the worldsheet.

We need an action that describes the dynamics of this string. The key property that we will ask for is that nothing depends on the coordinates σ^α that we choose on the worldsheet. In other words, the string action should be reparameterization invariant. What kind of action does the trick? Well, for the point particle the action was proportional to the length of the worldline. The obvious generalization is that the action for the string should be proportional to the area, A, of the worldsheet. This is certainly a property that is characteristic of the worldsheet itself, rather than any choice of parameterization.

How do we find the area A in terms of the coordinates X^μ(σ, τ)? The worldsheet is a curved surface embedded in spacetime. The induced metric, γ_αβ, on this surface is the pull-back of the flat metric on Minkowski space, γ_αβ = η_μν ∂X^μ/∂σ^α ∂X^ν/∂σ^β. (1.12)

Then the action which is proportional to the area of the worldsheet is given by, S = −T ∫ d²σ √(−det γ). (1.13)

Here T is a constant of proportionality. We will see shortly that it is the tension of the string, meaning the mass per unit length.

We can write this action a little more explicitly. The pull-back of the metric is given by, γ_αβ = (Ẋ², Ẋ·X'; Ẋ·X', X'²), where Ẋ^μ = ∂X^μ/∂τ and X'^μ = ∂X^μ/∂σ. The action then takes the form, S = −T ∫ d²σ √((Ẋ)²(X')² + (Ẋ·X')²). (1.14)

This is the Nambu-Goto action for a relativistic string.

Action = Area: A Check If you’re unfamiliar with differential geometry, the argument about the pull-back of the metric may be a bit slick. Thankfully, there’s a more pedestrian way to see that the action (1.14) is equal to the area swept out by the worldsheet. It’s slightly simpler to make this argument for a surface embedded in Euclidean space rather than Minkowski space. We choose some parameterization of the sheet in terms of τ and σ, as drawn in the figure, and we write the coordinates of Euclidean space as X⃗(σ, τ). We’ll compute the area of the infinitesimal shaded region. The vectors tangent to the boundary are, dl⃗₁ = ∂X⃗/∂σ, dl⃗₂ = ∂X⃗/∂τ.

If the angle between these two vectors is θ, then the area is then given by ds² = |d⃗l₁||d⃗l₂|sinθ = dl₁²dl₂²(1−cos²θ) = dl₁²dl₂² −(d⃗l₁·d⃗l₂)² (1.15)

which indeed takes the form of the integrand of (1.14).

Tension and Dimension Let’s now see that T has the physical interpretation of tension. We write Minkowski coordinates as Xµ = (t,⃗x). We work in a gauge with X0 ≡ t = Rτ, where R is a constant that is needed to balance up dimensions (see below) and will drop out at the end of the argument. Consider a snapshot of a string configuration at a time when d⃗x/dτ = 0 so that the instantaneous kinetic energy vanishes. Evaluating the action for a time dt gives S = −T ∫dτdσR√(d⃗x/dσ)² = −T dt(spatial length of string) . (1.16)

But, when the kinetic energy vanishes, the action is proportional to the time integral of the potential energy, potential energy = T ×(spatial length of string) .

So T is indeed the energy per unit length as claimed. We learn that the string acts rather like an elastic band and its energy increases linearly with length. (This is different from the elastic bands you’re used to which obey Hooke’s law where energy increased quadratically with length). To minimize its potential energy, the string will want to shrink to zero size. We’ll see that when we include quantum effects this can’t happen because of the usual zero point energies.

There is a slightly annoying way of writing the tension that has its origin in ancient history, but is commonly used today T = 1/(2πα') (1.17)

where α' is pronounced “alpha-prime”. In the language of our ancestors, α' is referred to as the “universal Regge slope”. We’ll explain why later in this course.

At this point, it’s worth pointing out some conventions that we have, until now, left implicit. The spacetime coordinates have dimension [X] = −1. In contrast, the worldsheet coordinates are taken to be dimensionless, [σ] = 0. (This can be seen in our identification σ ≡ σ +2π). The tension is equal to the mass per unit length and has dimension [T] = 2. Obviously this means that [α'] = −2. We can therefore associate a length scale, lₛ, by α' = lₛ² (1.18)

The string scale lₛ is the natural length that appears in string theory. In fact, in a certain sense (that we will make more precise later in the course) this length scale is the only parameter of the theory.

Actual Strings vs. Fundamental Strings There are several situations in Nature where string-like objects arise. Prime examples include magnetic flux tubes in superconductors and chromo-electric flux tubes in QCD. Cosmic strings, a popular speculation in cosmology, are similar objects, stretched across the sky. In each of these situations, there are typically two length scales associated to the string: the tension, T and the width of the string, L. For all these objects, the dynamics is governed by the Nambu-Goto action as long as the curvature of the string is much greater than L. (In the case of superconductors, one should work with a suitable non-relativistic version of the Nambu-Goto action).

However, in each of these other cases, the Nambu-Goto action is not the end of the story. There will typically be additional terms in the action that depend on the width of the string. The form of these terms is not universal, but often includes a rigidity piece of form ∫L K², where K is the extrinsic curvature of the worldsheet. Other terms could be added to describe fluctuations in the width of the string.

The string scale, lₛ, or equivalently the tension, T, depends on the kind of string that we’re considering. For example, if we’re interested in QCD flux tubes then we would take T ∼ (1 GeV)² (1.19)

In this course we will consider fundamental strings which have zero width. What this means in practice is that we take the Nambu-Goto action as the complete description for all configurations of the string. These strings will have relevance to quantum gravity and the tension of the string is taken to be much larger, typically an order of magnitude or so below the Planck scale.

T ≲ M²ₚₗ = (10¹⁸ GeV)² (1.20)

However, I should point out that when we try to view string theory as a fundamental theory of quantum gravity, we don’t really know what value T should take. As we will see later in this course, it depends on many other aspects, most notably the string coupling and the volume of the extra dimensions.

1.2.1 Symmetries of the Nambu-Goto Action The Nambu-Goto action has two types of symmetry, each of a different nature.

• Poincaré invariance of the spacetime (1.6). This is a global symmetry from the perspective of the worldsheet, meaning that the parameters Λµ and cµ which label the symmetry transformation are constants and do not depend on worldsheet coordinates σα.

• Reparameterization invariance, σα → σ̃α(σ). As for the point particle, this is a gauge symmetry. It reflects the freedom to choose different coordinates on the worldsheet.

act that we have a redundancy in our description because the worldsheet coordinates σα have no physical meaning.

1.2.2 Equations of Motion To derive the equations of motion for the Nambu-Goto string, we first introduce the momenta which we call Π because there will be countless other quantities that we want to call p later, Πτµ = ∂L/∂Ẋµ = -T (Ẋ·X')X'µ - (X'²)Ẋµ / √((Ẋ·X')² - Ẋ²X'²)

Πσµ = ∂L/∂X'µ = -T (Ẋ·X')Ẋµ - (Ẋ²)X'µ / √((Ẋ·X')² - Ẋ²X'²)

The equations of motion are then given by, ∂Πτµ/∂τ + ∂Πσµ/∂σ = 0 These look like nasty, non-linear equations. In fact, there’s a slightly nicer way to write these equations, starting from the earlier action (1.13). Recall that the variation of a determinant is δ√(-γ) = (1/2)√(-γ)γαβδγαβ. Using the definition of the pull-back metric γαβ, this gives rise to the equations of motion ∂α(√(-detγ)γαβ∂βXµ) = 0 , (1.21)

Although this notation makes the equations look a little nicer, we’re kidding ourselves. Written in terms of Xµ, they are still the same equations. Still nasty.

## 1.3 The Polyakov Action

The square-root in the Nambu-Goto action means that it’s rather difficult to quantize using path integral techniques. However, there is another form of the string action which is classically equivalent to the Nambu-Goto action. It eliminates the square root at the expense of introducing another field, S = -1/(4πα') ∫ d²σ √(-g) gαβ ∂αXµ ∂βXν ηµν (1.22)

where g ≡ detgαβ. This is the Polyakov action. (Polyakov didn’t discover the action, but he understood how to work with it in the path integral and for this reason it carries his name. The path integral treatment of this action will be the subject of Chapter 5).

The new field is gαβ. It is a dynamical metric on the worldsheet. From the perspective of the worldsheet, the Polyakov action is a bunch of scalar fields Xµ coupled to 2d gravity.

The equation of motion for Xµ is ∂α(√(-g) gαβ ∂βXµ) = 0 , (1.23)

which coincides with the equation of motion (1.21) from the Nambu-Goto action, except that gαβ is now an independent variable which is fixed by its own equation of motion. To determine this, we vary the action (remembering again that δ√(-g) = -(1/2)√(-g) gαβ δgαβ = +(1/2)√(-g) gαβ δgαβ), δS = -T/2 ∫ d²σ [δgαβ (-√(-g) ∂αXµ ∂βXν ηµν) - (1/2) √(-g) gρσ ∂ρXµ ∂σXν ηµν δgαβ] = 0 .(1.24)

The worldsheet metric is therefore given by, gαβ = 2f(σ) ∂αX · ∂βX , (1.25)

where the function f(σ) is given by, f⁻¹ = gρσ ∂ρX · ∂σX A comment on the potentially ambiguous notation: here, and below, any function f(σ) is always short-hand for f(σ,τ): it in no way implies that f depends only on the spatial worldsheet coordinate.

We see that gαβ isn’t quite the same as the pull-back metric γαβ defined in equation (1.12); the two differ by the conformal factor f. However, this doesn’t matter because, rather remarkably, f drops out of the equation of motion (1.23). This is because the √(-g) term scales as f, while the inverse metric gαβ scales as f⁻¹ and the two pieces cancel. We therefore see that Nambu-Goto and the Polyakov actions result in the same equation of motion for X.

In fact, we can see more directly that the Nambu-Goto and Polyakov actions coincide. We may replace gαβ in the Polyakov action (1.22) with its equation of motion gαβ = 2f γαβ. The factor of f also drops out of the action for the same reason that it dropped out of the equation of motion. In this manner, we recover the Nambu-Goto action (1.13).

1.3.1 Symmetries of the Polyakov Action The fact that the presence of the factor f(σ,τ) in (1.25) didn’t actually affect the equations of motion for Xµ reflects the existence of an extra symmetry which the Polyakov action enjoys. Let’s look more closely at this. Firstly, the Polyakov action still has the two symmetries of the Nambu-Goto action, • Poincaré invariance. This is a global symmetry on the worldsheet.

Xµ → Λµν Xν + cµ .

• Reparameterization invariance, also known as diffeomorphisms. This is a gauge symmetry on the worldsheet. We may redefine the worldsheet coordinates as σα → σ̃α(σ). The fields Xµ transform as worldsheet scalars, while gαβ transforms in the manner appropriate for a 2d metric.

Xµ(σ) → X̃µ(σ̃) = Xµ(σ)

gαβ(σ) → g̃αβ(σ̃) = gγδ(σ) ∂σγ/∂σ̃α ∂σδ/∂σ̃β It will sometimes be useful to work infinitesimally. If we make the coordinate change σα → σ̃α = σα - ηα(σ), for some small η. The transformations of the fields then become, δXµ(σ) = ηα ∂αXµ δgαβ(σ) = ∇α ηβ + ∇β ηα where the covariant derivative is defined by ∇α ηβ = ∂α ηβ - Γσαβ ησ with the Levi-Civita connection associated to the worldsheet metric given by the usual expression, Γσαβ = (1/2) gσρ (∂α gβρ + ∂β gρα - ∂ρ gαβ)

Together with these familiar symmetries, there is also a new symmetry which is novel to the Polyakov action. It is called Weyl invariance.

• Weyl Invariance. Under this symmetry, Xµ(σ) → Xµ(σ), while the metric changes as gαβ(σ) → Ω²(σ) gαβ(σ) . (1.26)

Or, infinitesimally, we can write Ω2(σ) = e2φ(σ) for small φ so that δgαβ(σ) = 2φ(σ)gαβ(σ).

It is simple to see that the Polyakov action is invariant under this transformation: the factor of Ω2 drops out just as the factor of f did in equation (1.25), canceling between −g and the inverse metric gαβ. This is a gauge symmetry of the string, as seen by the fact that the parameter Ω depends on the worldsheet coordinates σ. This means that two metrics which are related by a Weyl transformation (1.26) are to be considered as the same physical state.

Figure 7: An example of a Weyl transformation

How should we think of Weyl invariance? It is not a coordinate change. Instead it is the invariance of the theory under a local change of scale which preserves the angles between all lines. For example the two worldsheet metrics shown in the figure are viewed by the Polyakov string as equivalent. This is rather surprising! And, as you might imagine, theories with this property are extremely rare. It should be clear from the discussion above that the property of Weyl invariance is special to two dimensions, for only there does the scaling factor coming from the determinant −g cancel that coming from the inverse metric. But even in two dimensions, if we wish to keep Weyl invariance then we are strictly limited in the kind of interactions that can be added to the action. For example, we would not be allowed a potential term for the worldsheet scalars of the form, ∫ d2σ √−g V(X).

These break Weyl invariance. Nor can we add a worldsheet cosmological constant term, µ ∫ d2σ √−g.

This too breaks Weyl invariance. We will see later in this course that the requirement of Weyl invariance becomes even more stringent in the quantum theory. We will also see what kind of interactions terms can be added to the worldsheet. Indeed, much of this course can be thought of as the study of theories with Weyl invariance.

1.3.2 Fixing a Gauge

As we have seen, the equation of motion (1.23) looks pretty nasty. However, we can use the redundancy inherent in the gauge symmetry to choose coordinates in which they simplify. Let’s think about what we can do with the gauge symmetry.

Firstly, we have two reparameterizations to play with. The worldsheet metric has three independent components. This means that we expect to be able to set any two of the metric components to a value of our choosing. We will choose to make the metric locally conformally flat, meaning gαβ = e2φ ηαβ, (1.27)

where φ(σ,τ) is some function on the worldsheet. You can check that this is possible by writing down the change of the metric under a coordinate transformation and seeing that the differential equations which result from the condition (1.27) have solutions, at least locally. Choosing a metric of the form (1.27) is known as conformal gauge.

We have only used reparameterization invariance to get to the metric (1.27). We still have Weyl transformations to play with. Clearly, we can use these to remove the last independent component of the metric and set φ = 0 such that, gαβ = ηαβ. (1.28)

We end up with the flat metric on the worldsheet in Minkowski coordinates.

A Diversion: How to make a metric flat

The fact that we can use Weyl invariance to make any two-dimensional metric flat is an important result. Let’s take a quick diversion from our main discussion to see a different proof that isn’t tied to the choice of Minkowski coordinates on the worldsheet. We’ll work in 2d Euclidean space to avoid annoying minus signs. Consider two metrics related by a Weyl transformation, g'αβ = e2φ gαβ. One can check that the Ricci scalars of the two metrics are related by, √g' R' = √g (R − 2∇2φ). (1.29)

We can therefore pick a φ such that the new metric has vanishing Ricci scalar, R' = 0, simply by solving this differential equation for φ. However, in two dimensions (but not in higher dimensions) a vanishing Ricci scalar implies a flat metric. The reason is simply that there aren’t too many indices to play with. In particular, symmetry of the Riemann tensor in two dimensions means that it must take the form, Rαβγδ = (gαγ gβδ − gαδ gβγ) R.

So R' = 0 is enough to ensure that R'αβγδ = 0, which means that the manifold is flat. In equation (1.28), we’ve further used reparameterization invariance to pick coordinates in which the flat metric is the Minkowski metric.

The equations of motion and the stress-energy tensor

With the choice of the flat metric (1.28), the Polyakov action simplifies tremendously and becomes the theory of D free scalar fields. (In fact, this simplification happens in any conformal gauge).

S = − 1/(4πα') ∫ d2σ ∂α X · ∂α X, (1.30)

and the equations of motion for Xµ reduce to the free wave equation, ∂α ∂α Xµ = 0. (1.31)

Now that looks too good to be true! Are the horrible equations (1.23) really equivalent to a free wave equation? Well, not quite. There is something that we’ve forgotten.

Then: we picked a choice of gauge for the metric gαβ. But we must still make sure that the equation of motion for gαβ is satisfied. In fact, the variation of the action with respect to the metric gives rise to a rather special quantity: it is the stress-energy tensor, Tαβ. With a particular choice of normalization convention, we define the stress-energy tensor to be Tαβ = − 2/√(−g) ∂S/∂gαβ.

We varied the Polyakov action with respect to gαβ in (1.24). When we set gαβ = ηαβ we get Tαβ = ∂αX · ∂βX − 1/2 ηαβ ηρσ ∂ρX · ∂σX. (1.32)

The equation of motion associated to the metric gαβ is simply Tαβ = 0. Or, more explicitly, T01 = Ẋ · X' = 0 T00 = T11 = 1/2 (Ẋ² + X'²) = 0 . (1.33)

We therefore learn that the equations of motion of the string are the free wave equations (1.31) subject to the two constraints (1.33) arising from the equation of motion Tαβ = 0.

Getting a feel for the constraints Let’s try to get some intuition for these constraints. There is a simple meaning of the first constraint in (1.33): we must choose our parameterization such that lines of constant σ are perpendicular to the lines of constant τ, as shown in the figure.

But we can do better. To gain more physical insight, we need to make use of the fact that we haven’t quite exhausted our gauge symmetry. We will discuss this more in Section 2.2, but for now one can check that there is enough remnant gauge symmetry to allow us to go to static gauge, X0 ≡ t = Rτ , so that (X0)' = 0 and Ẋ0 = R, where R is a constant that is needed on dimensional grounds. The interpretation of this constant will become clear shortly. Then, writing Xµ = (t, x⃗), the equation of motion for spatial components is the free wave equation, ẍ⃗ − x⃗'' = 0 while the constraints become ẋ⃗ · x⃗' = 0 ẋ⃗² + x⃗'² = R² (1.34)

The first constraint tells us that the motion of the string must be perpendicular to the string itself. In other words, the physical modes of the string are transverse oscillations. There is no longitudinal mode. We’ll also see this again in Section 2.2.

From the second constraint, we can understand the meaning of the constant R: it is related to the length of the string when x⃗ = 0, ∫ dσ √(d x⃗/dσ)² = 2πR .

Of course, if we have a stretched string with x⃗ = 0 at one moment of time, then it won’t stay like that for long. It will contract under its own tension. As this happens, the second constraint equation relates the length of the string to the instantaneous velocity of the string.

## 1.4 Mode Expansions

Let’s look at the equations of motion and constraints more closely. The equations of motion (1.31) are easily solved. We introduce lightcone coordinates on the worldsheet, σ± = τ ± σ , in terms of which the equations of motion simply read ∂+ ∂− Xµ = 0 The most general solution is, Xµ(σ,τ) = XµL(σ+) + XµR(σ−)

for arbitrary functions XµL and XµR. These describe left-moving and right-moving waves respectively. Of course the solution must still obey both the constraints (1.33) as well as the periodicity condition, Xµ(σ,τ) = Xµ(σ + 2π,τ) . (1.35)

The most general, periodic solution can be expanded in Fourier modes, XµL(σ+) = 1/2 xµ + 1/2 α' pµ σ+ + i √(α'/2) Σ_{n≠0} (1/n) ˜αµ_n e^{−inσ+} , XµR(σ−) = 1/2 xµ + 1/2 α' pµ σ− + i √(α'/2) Σ_{n≠0} (1/n) αµ_n e^{−inσ−} . (1.36)

This mode expansion will be very important when we come to the quantum theory. Let’s make a few simple comments here.

• Various normalizations in this expression, such as the α' and factor of 1/n have been chosen for later convenience.

• XL and XR do not individually satisfy the periodicity condition (1.35) due to the terms linear in σ±. However, the sum of them is invariant under σ → σ + 2π as required.

• The variables xµ and pµ are the position and momentum of the center of mass of the string. This can be checked, for example, by studying the Noether currents arising from the spacetime translation symmetry Xµ → Xµ + cµ. One finds that the conserved charge is indeed pµ.

• Reality of Xµ requires that the coefficients of the Fourier modes, αµ_n and ˜αµ_n, obey αµ_n = (αµ_{−n})* , ˜αµ_n = (˜αµ_{−n})* . (1.37)

1.4.1 The Constraints Revisited We still have to impose the two constraints (1.33). In the worldsheet lightcone coordinates σ±, these become, (∂+ X)² = (∂− X)² = 0 . (1.38)

These equations give constraints on the momenta pµ and the Fourier modes αµ_n and ˜αµ_n. To see what these are, let’s look at ∂− Xµ = ∂− XµR = pµ + αµ_0 + Σ_{n≠0} αµ_n e^{−inσ−} = Σ_{n} αµ_n e^{−inσ−} where in the second line the sum is over all n ∈ Z and we have defined αµ_0 to be αµ_0 ≡ √(α'/2) pµ .

The constraint (1.38) can then be written as (∂− X)² = Σ_{m,p} αµ_m · αµ_p e^{−i(m+p)σ−} = Σ_{m,p} αµ_m · αµ_p e^{−i(m+p)σ−} e^{-inσ} m n−m m,n ∑ ≡ α' L e^{-inσ} = 0 .

where we have defined the sum of oscillator modes, 1 ∑ L = α ·α . (1.39)

n n−m m We can also do the same for the left-moving modes, where we again define an analogous sum of operator modes, 1 ∑ L = α˜ ·α˜ . (1.40)

n n−m m with the zero mode defined to be, √ α' α˜µ ≡ pµ .

0 2 The fact that α˜µ = αµ looks innocuous but is a key point to remember when we come 0 0 to quantize the string. The L and L are the Fourier modes of the constraints. Any n n classical solution of the string of the form (1.36) must further obey the infinite number of constraints, L = L = 0 n ∈ Z .

n n We’ll meet these objects L and L again in a more general context when we come to n n discuss conformal field theory.

The constraints arising from L and L have a rather special interpretation. This is 0 0 because they include the square of the spacetime momentum pµ. But, the square of the spacetime momentum is an important quantity in Minkowski space: it is the square of the rest mass of a particle, p pµ = −M² .

So the L and L constraints tell us the effective mass of a string in terms of the excited 0 0 oscillator modes, namely 4 ∑ 4 ∑ M² = α ·α = α˜ ·α˜ (1.41)

α' n −n α' n −n n>0 n>0 Because both αµ and α˜µ are equal to √(α'/2) pµ, we have two expressions for the invariant 0 0 mass: one in terms of right-moving oscillators αµ and one in terms of left-moving oscillators α˜µ. And these two terms must be equal to each other. This is known as level matching. It will play an important role in the next section where we turn to the quantum theory.

## 2. The Quantum String

Our goal in this section is to quantize the string. We have seen that the string action involves a gauge symmetry and whenever we wish to quantize a gauge theory we’re presented with a number of different ways in which we can proceed. If we’re working in the canonical formalism, this usually boils down to one of two choices: • We could first quantize the system and then subsequently impose the constraints that arise from gauge fixing as operator equations on the physical states of the system. For example, in QED this is the Gupta-Bleuler method of quantization that we use in Lorentz gauge. In string theory it consists of treating all fields Xµ, including time X0, as operators and imposing the constraint equations (1.33) on the states. This is usually called covariant quantization.

• The alternative method is to first solve all of the constraints of the system to determine the space of physically distinct classical solutions. We then quantize these physical solutions. For example, in QED, this is the way we proceed in Coulomb gauge. Later in this chapter, we will see a simple way to solve the constraints of the free string.

Of course, if we do everything correctly, the two methods should agree. Usually, each presents a slightly different challenge and offers a different viewpoint.

In these lectures, we’ll take a brief look at the first method of covariant quantization.

However, at the slightest sign of difficulties, we’ll bail! It will be useful enough to see where the problems lie. We’ll then push forward with the second method described above which is known as lightcone quantization in string theory. Although we’ll succeed in pushing quantization through to the end, our derivations will be a little cheap and unsatisfactory in places. In Section 5 we’ll return to all these issues, armed with more sophisticated techniques from conformal field theory.

## 2.1 A Lightning Look at Covariant Quantization

We wish to quantize D free scalar fields Xµ whose dynamics is governed by the action (1.30). We subsequently wish to impose the constraints X ˙ ·X' = X ˙² + X'² = 0 . (2.1)

The first step is easy. We promote Xµ and their conjugate momenta Πµ = (1/2πα') X ˙µ to operator valued fields obeying the canonical equal-time commutation relations, [Xµ(σ,τ), Πν(σ',τ)] = iδ(σ − σ')δµν , [Xµ(σ,τ), Xν(σ',τ)] = [Πµ(σ,τ), Πν(σ',τ)] = 0 .

We translate these into commutation relations for the Fourier modes xµ, pµ, αµ and α˜µ. Using the mode expansion (1.36) we find [xµ, pν] = iδµν and [αµn, ανm] = [α˜µn, α˜νm] = n ηµν δn+m,0 , (2.2)

with all others zero. The commutation relations for xµ and pµ are expected for oper- ators governing the position and momentum of the center of mass of the string. The commutation relations of αµn and α˜µn are those of harmonic oscillator creation and anni- hilation operators in disguise. And the disguise isn’t that good. We just need to define (ignoring the µ index for now)

αn αn an = √n , a†n = √(−n) n > 0 (2.3)

Then (2.2) gives the familiar [an, a†m] = δnm. So each scalar field gives rise to two infinite towers of creation and annihilation operators, with αn acting as a rescaled annihilation operator for n > 0 and as a creation operator for n < 0. There are two towers because we have right-moving modes αn and left-moving modes α˜n.

d left-moving modes $\tilde{\alpha}_n$.

With these commutation relations in hand we can now start building the Fock space of our theory. We introduce a vacuum state of the string $|0\rangle$, defined to obey $\alpha_n^\mu|0\rangle = \tilde{\alpha}_n^\mu|0\rangle = 0$ for $n > 0$ (2.4)

The vacuum state of string theory has a different interpretation from the analogous object in field theory. This is not the vacuum state of spacetime. It is instead the vacuum state of a single string. This is reflected in the fact that the operators $x^\mu$ and $p^\mu$ give extra structure to the vacuum. The true ground state of the string is $|0\rangle$, tensored with a spatial wavefunction $\Psi(x)$. Alternatively, if we work in momentum space, the vacuum carries another quantum number, $p^\mu$, which is the eigenvalue of the momentum operator. We should therefore write the vacuum as $|0; p\rangle$, which still obeys (2.4), but now also $\hat{p}^\mu|0; p\rangle = p^\mu|0; p\rangle$ (2.5)

where (for the only time in these lecture notes) we’ve put a hat on the momentum operator $\hat{p}^\mu$ on the left-hand side of this equation to distinguish it from the eigenvalue $p^\mu$ on the right-hand side.

We can now start to build up the Fock space by acting with creation operators $\alpha_n^\mu$ and $\tilde{\alpha}_n^\mu$ with $n < 0$. A generic state comes from acting with any number of these creation operators on the vacuum, $(\alpha_{-1}^{\mu_1})^{n_{\mu_1}} (\alpha_{-2}^{\mu_2})^{n_{\mu_2}} ... (\tilde{\alpha}_{-1}^{\nu_1})^{n_{\nu_1}} (\tilde{\alpha}_{-2}^{\nu_2})^{n_{\nu_2}} ... |0; p\rangle$ Each state in the Fock space is a different excited state of the string. Each has the interpretation of a different species of particle in spacetime. We’ll see exactly what particles they are shortly. But for now, notice that because there’s an infinite number of ways to excite a string there are an infinite number of different species of particles in this theory.

2.1.1 Ghosts There’s a problem with the Fock space that we’ve constructed: it doesn’t have positive norm. The reason for this is that one of the scalar fields, $X^0$, comes with the wrong sign kinetic term in the action (1.30). From the perspective of the commutation relations, this issue raises its head in presence of the spacetime Minkowski metric in the expression $[\alpha_n^\mu, \alpha_m^{\nu\dagger}] = n \eta^{\mu\nu} \delta_{n,m}$.

This gives rise to the offending negative norm states, which come with an odd number of timelike oscillators excited, for example $\langle p'; 0 | \alpha_1^0 \alpha_{-1}^0 | 0; p \rangle \sim -\delta^D(p - p')$.

This is the first problem that arises in the covariant approach to quantization. States with negative norm are referred to as ghosts. To make sense of the theory, we have to make sure that they can’t be produced in any physical processes. Of course, this problem is familiar from attempts to quantize QED in Lorentz gauge. In that case, gauge symmetry rides to the rescue since the ghosts are removed by imposing the gauge fixing constraint. We must hope that the same happens in string theory.

2.1.2 Constraints Although we won’t push through with this programme at the present time, let us briefly look at what kind of constraints we have in string theory. In terms of Fourier modes, the classical constraints can be written as $L_n = \tilde{L}_n = 0$, where $L_n = \frac{1}{2} \sum_{m} \alpha_{n-m} \cdot \alpha_m$ and similar for $\tilde{L}_n$. As in the Gupta-Bleuler quantization of QED, we don’t impose all of these as operator equations on the Hilbert space. Instead we only require that the operators $L_n$ and $\tilde{L}_n$ have vanishing matrix elements when sandwiched between two physical states $|\text{phys}\rangle$ and $|\text{phys}'\rangle$, $\langle \text{phys}' | L_n | \text{phys} \rangle = \langle \text{phys}' | \tilde{L}_n | \text{phys} \rangle = 0$.

Because $L_n^\dagger = L_{-n}$, it is therefore sufficient to require $L_n | \text{phys} \rangle = \tilde{L}_n | \text{phys} \rangle = 0$ for $n > 0$ (2.6)

However, we still haven’t explained how to impose the constraints $L_0$ and $\tilde{L}_0$. And these present a problem that doesn’t arise in the case of QED. The problem is that, unlike for $L_n$ with $n \neq 0$, the operator $L_0$ is not uniquely defined when we pass to the quantum theory. There is an operator ordering ambiguity arising from the commutation relations (2.2). Commuting the $\alpha^\mu$ operators past each other in $L_0$ gives rise to extra constant terms.

Question: How do we know what order to put the $\alpha^\mu$ operators in the quantum operator $L_0$? Or the $\tilde{\alpha}^\mu$ operators in $\tilde{L}_0$?

Answer: We don’t! Yet. Naively it looks as if each different choice will define a different theory when we impose the constraints. To make this ambiguity manifest, for now let’s just pick a choice of ordering. We define the quantum operators to be normal ordered, with the annihilation operators $\alpha_i$, $n > 0$, moved to the right, $L_0 = \sum_{m=1}^{\infty} \frac{1}{2} \alpha_{-m} \cdot \alpha_m + \frac{1}{2} \alpha_0^2, \quad \tilde{L}_0 = \sum_{m=1}^{\infty} \frac{1}{2} \tilde{\alpha}_{-m} \cdot \tilde{\alpha}_m + \frac{1}{2} \tilde{\alpha}_0^2$.

Then the ambiguity rears its head in the different constraint equations that we could impose, namely $(L_0 - a)|\text{phys}\rangle = (\tilde{L}_0 - a)|\text{phys}\rangle = 0$ (2.7)

for some constant $a$.

As we saw classically, the operators $L_0$ and $\tilde{L}_0$ play an important role in determining the spectrum of the string because they include a term quadratic in the momentum $\alpha_0^\mu = \tilde{\alpha}_0^\mu = \sqrt{2} \alpha'^\mu$. )/2pµ. Combining the expression (1.41) with our constraint equation 0 0 for L and L , we find the spectrum of the string is given by, 0 0 (cid:32) (cid:33) (cid:32) (cid:33)

∞ ∞ 4 (cid:88) 4 (cid:88)

M2 = −a+ α ·α = −a+ α˜ ·α˜ α(cid:48) −m m α(cid:48) −m m m=1 m=1 We learn therefore that the undetermined constant a has a direct physical effect: it changes the mass spectrum of the string. In the quantum theory, the sums over αµ modes are related to the number operators for the harmonic oscillator: they count the number of excited modes of the string. The level matching in the quantum theory tells us that the number of left-moving modes must equal the number of right-moving modes.

– 31 – Ultimately, we will find that the need to decouple the ghosts forces us to make a unique choice for the constant a. (Spoiler alert: it turns out to be a = 1). In fact, the requirement that there are no ghosts is much stronger than this. It also restricts the number of scalar fields that we have in the theory. (Another spoiler: D = 26). If you’re interested in how this works in covariant formulation then you can read about it in the book by Green, Schwarz and Witten. Instead, we’ll show how to quantize the string and derive these values for a and D in lightcone gauge. However, after a trip through the world of conformal field theory, we’ll come back to these ideas in a context which is closer to the covariant approach.

## 2.2 Lightcone Quantization

We will now take the second path described at the beginning of this section. We will try to find a parameterization of all classical solutions of the string. This is equivalent to finding the classical phase space of the theory. We do this by solving the constraints (2.1) in the classical theory, leaving behind only the physical degrees of freedom.

Recall that we fixed the gauge to set the worldsheet metric to g = η .

αβ αβ However, this isn’t the end of our gauge freedom. There still remain gauge transforma- tions which preserve this choice of metric. In particular, any coordinate transformation σ → σ˜(σ) which changes the metric by η → Ω2(σ)η , (2.8)

αβ αβ can be undone by a Weyl transformation. What are these coordinate transformations?

It’s simplest to answer this using lightcone coordinates on the worldsheet, σ± = τ ±σ , (2.9)

where the flat metric on the worldsheet takes the form, ds2 = −dσ+dσ− In these coordinates, it’s clear that any transformation of the form σ+ → σ˜+(σ+) , σ− → σ˜−(σ−) , (2.10)

simply multiplies the flat metric by an overall factor (2.8) and so can be undone by a compensating Weyl transformation. Some quick comments on this surviving gauge symmetry: – 32 – • Recall that in Section 1.3.2 we used the argument that 3 gauge invariances (2 reparameterizations + 1 Weyl) could be used to fix 3 components of the world- sheet metric g . What happened to this argument? Why do we still have some αβ gauge symmetry left? The reason is that σ˜± are functions of just a single variable, not two. So we did fix nearly all our gauge symmetries. What is left is a set of measure zero amongst the full gauge symmetry that we started with.

• The remaining reparameterization invariance (2.10) has an important physical implication. Recall that the solutions to the equations of motion are of the form Xµ(σ+)+Xµ(σ−) which looks like 2D functions worth of solutions. Of course, L R we still have the constraints which, in terms of σ±, read (∂ X)2 = (∂ X)2 = 0 , (2.11)

+ − which seems to bring the number down to 2(D−1) functions. But the reparam- eterization invariance (2.10) tells us that even some of these are fake since we can always change what we mean by σ±. The physical solutions of the string are therefore actually described by 2(D −2) functions. But this counting has a nice interpretation: the degrees of freedom describe the transverse fluctuations of the string.

• The above comment reaches the same conclusion as the discussion in Section 1.3.2. There, in an attempt to get some feel for the constraints, we claimed that we could go to static gauge X0 = Rτ for some dimensionful parameter R. It is easy to check that this is simple to do using reparameterizations of the form (2.10). However, to solve the string constraints in full, it turns out that static gauge is not that useful. Rather we will use something called “lightcone gauge”.

2.2.1 Lightcone Gauge Wewouldliketogaugefixtheremainingreparameterizationinvariance(2.10). Thebest way to do this is called lightcone gauge. In counterpoint to the worldsheet lightcone coordinates (2.9), we introduce the spacetime lightcone coordinates, (cid:114)

X± = (X0 ±XD−1) . (2.12)

Note that this choice picks out a particular time direction and a particular spatial direction. ItmeansthatanycalculationsthatwedoinvolvingX± willnotbemanifestly Lorentz invariant. You might think that we needn’t really worry about this. We could try to make the following argument: “The equations may not look Lorentz invariant – 33 – but, since we started from a Lorentz in variant theory, at the end of the day any physical process is guaranteed to obey this symmetry”. Right?! Well, unfortunately not. One of the more interesting and subtle aspects of quantum field theory is the possibility of anomalies: these are symmetries of the classical theory that do not survive the journey of quantization. When we come to the quantum theory, if our equations don’t look Lorentz invariant then there’s a real possibility that it’s because the underlying physics actually isn’t Lorentz invariant. Later we will need to spend some time figuring out under what circumstances our quantum theory keeps the classical Lorentz symmetry.

In lightcone coordinates, the spacetime Minkowski metric reads ds² = -2dX⁺dX⁻ + Σᵢ₌₁ᴰ⁻² dXⁱdXⁱ This means that indices are raised and lowered with A⁺ = -A⁻ and A⁻ = -A⁺ and Aⁱ = Aᵢ. The product of spacetime vectors reads A·B = -A⁺B⁻ - A⁻B⁺ + AⁱBⁱ.

Let’s look at the solution to the equation of motion for X⁺. It reads, X⁺ = X⁺_L(σ⁺) + X⁺_R(σ⁻).

We now gauge fix. We use our freedom of reparameterization invariance to choose coordinates such that X⁺_L = ½x⁺ + ½α'p⁺σ⁺, X⁺_R = ½x⁺ + ½α'p⁺σ⁻.

You might think that we could go further and eliminate p⁺ and x⁺ but this isn’t possible because we don’t quite have the full freedom of reparameterization invariance since all functions should remain periodic in σ. The upshot of this choice of gauge is that X⁺ = x⁺ + α'p⁺τ. (2.13)

This is lightcone gauge. Notice that, as long as p⁺ ≠ 0, we can always shift x⁺ by a shift in τ.

There’s something a little disconcerting about the choice (2.13). We’ve identified a timelike worldsheet coordinate with a null spacetime coordinate. Nonetheless, as you can see from the figure, it seems to be a good parameterization of the worldsheet. One could imagine that the parameterization might break if the string is actually massless and travels in the X⁻ direction, with p⁺ = 0. But otherwise, all should be fine.

Solving for X⁻ The choice (2.13) does the job of fixing the reparameterization invariance (2.10). As we will now see, it also renders the constraint equations trivial. The first thing that we have to worry about is the possibility of extra constraints arising from this new choice of gauge fixing. This can be checked by looking at the equation of motion for X⁺, ∂₊∂₋X⁻ = 0 But we can solve this by the usual ansatz, X⁻ = X⁻_L(σ⁺) + X⁻_R(σ⁻).

We’re still left with all the other constraints (2.11). Here we see the real benefit of working in lightcone gauge (which is actually what makes quantization possible at all): X⁻ is completely determined by these constraints. For example, the first of these reads 2∂₊X⁻∂₊X⁺ = Σᵢ₌₁ᴰ⁻² ∂₊Xⁱ∂₊Xⁱ (2.14)

which, using (2.13), simply becomes ∂₊X⁻ = (1/(α'p⁺)) Σᵢ₌₁ᴰ⁻² ∂₊Xⁱ∂₊Xⁱ. (2.15)

Similarly, ∂₋X⁻ = (1/(α'p⁺)) Σᵢ₌₁ᴰ⁻² ∂₋Xⁱ∂₋Xⁱ. (2.16)

So, up to an integration constant, the function X⁻(σ⁺,σ⁻) is completely determined in terms of the other fields. If we write the usual mode expansion for X⁻_{L/R} X⁻_L(σ⁺) = ½x⁻ + ½α'p⁻σ⁺ + i√(α'/2) Σ_{n≠0} (1/n) α⁻ₙ e^{-inσ⁺}, X⁻_R(σ⁻) = ½x⁻ + ½α'p⁻σ⁻ + i√(α'/2) Σ_{n≠0} (1/n) α⁻ₙ e^{-inσ⁻}, then x⁻ is the undetermined integration constant, while p⁻, α⁻ₙ and α̃⁻ₙ are all fixed by the constraints (2.15) and (2.16). For example, the oscillator modes α⁻ₙ are given by, α⁻ₙ = (1/(2α'p⁺)) Σ_{m=-∞}^{+∞} Σᵢ₌₁ᴰ⁻² αⁱ_{n-m} αⁱ_m, (2.17)

A special case of this is the α⁻₀ = √(α'/2)p⁻ equation, which reads α'p⁻/2 = (1/(2p⁺)) [½α'pⁱpⁱ + Σᵢ₌₁ᴰ⁻² Σ_{n≠0} αⁱ_{-n}αⁱ_n]. (2.18)

We also get another equation for p⁻ from the α̃⁻₀ equation arising from (2.15)

α'p⁻/2 = (1/(2p⁺)) [½α'pⁱpⁱ + Σᵢ₌₁ᴰ⁻² Σ_{n≠0} α̃ⁱ_{-n}α̃ⁱ_n]. (2.19)

From these two equations, we can reconstruct the old, classical, level matching conditions (1.41). But now with a difference: M² = (2p⁺p⁻ - pⁱpⁱ)/α' = (4/α') Σᵢ₌₁ᴰ⁻² Σ_{n>0} αⁱ_{-n}αⁱ_n = (4/α') Σᵢ₌₁ᴰ⁻² Σ_{n>0} α̃ⁱ_{-n}α̃ⁱ_n. (2.20)

The difference is that now the sum is over oscillators αⁱₙ and α̃ⁱₙ only, with i = 1,...,D-2. We’ll refer to these as transverse oscillators. Note that the string isn’t necessarily living in the X⁰-X^{D-1} plane, so these aren’t literally the transverse excitations of the string. Nonetheless, if we specify the αⁱₙ then all other oscillator modes are determined. In this sense, they are the physical excitation of the string.

Let’s summarize the state of play so far. The most general classical solution is described in terms of 2(D − 2) transverse oscillator modes αⁱₙ and α̃ⁱₙ, together with a number of zero modes describing the center of mass and momentum of the string: xⁱ, pⁱ, p⁺ and x⁻. But x⁺ can be absorbed by a shift of τ in (2.13) and p− is constrained to obey (2.18) and (2.19). In fact, p− can be thought of as (proportional to) the lightcone Hamiltonian. Indeed, we know that p− generates translations in x+, but this is equivalent to shifts in τ.

2.2.2 Quantization

Having identified the physical degrees of freedom, let’s now quantize. We want to impose commutation relations. Some of these are easy: [x_i, p_j] = i δ_{ij}, [x_-, p_+] = -i; [α_i, α_j] = [α̃_i, α̃_j] = n δ_{ij} δ_{n+m,0} (2.21), all of which follow from the commutation relations (2.2) that we saw in covariant quantization. What to do with x+ and p−? We could implement p− as the Hamiltonian acting on states. In fact, it will prove slightly more elegant (but equivalent) if we promote both x+ and p− to operators with the expected commutation relation, [x+, p−] = -i (2.22). This is morally equivalent to writing [t, H] = -i in non-relativistic quantum mechanics, which is true on a formal level. In the present context, it means that we can once again choose states to be eigenstates of p^µ, with µ = 0,...,D, but the constraints (2.18) and (2.19) must still be imposed as operator equations on the physical states. We’ll come to this shortly. The Hilbert space of states is very similar to that described in covariant quantization: we define a vacuum state, |0; p⟩ such that p̂^µ |0; p⟩ = p^µ |0; p⟩, α_i |0; p⟩ = α̃_i |0; p⟩ = 0 for n > 0 (2.23) and we build a Fock space by acting with the creation operators α_{-n}^i and α̃_{-n}^i with n > 0. The difference with the covariant quantization is that we only act with transverse oscillators which carry a spatial index i = 1,...,D − 2. For this reason, the Hilbert space is, by construction, positive definite. We don’t have to worry about ghosts.

1 Mea Culpa: We’re not really supposed to do this. The whole point of the approach that we’re taking is to quantize just the physical degrees of freedom. The resulting commutation relations are not, in general, inherited from the larger theory that we started with simply by closing our eyes and forgetting about all the other fields that we’ve gauge fixed. We can see the problem by looking at (2 It is $$\frac{1}{2} \sum_{n} \alpha_i \alpha_i = \frac{1}{2} \sum_{n<0} \alpha_i \alpha_i + \frac{1}{2} \sum_{n>0} \alpha_i \alpha_i.$$ where we’ve left the sum over $i = 1,...,D -2$ implicit. We’ll now try to put this in normal ordered form, with the annihilation operators $\alpha_i$ with $n > 0$ on the right-hand side. It’s the first term that needs changing. We get $$\frac{1}{2} \sum_{n<0} \left[ \alpha_i \alpha_i - n(D-2) \right] + \frac{1}{2} \sum_{n>0} \alpha_i \alpha_i = \frac{1}{2} \sum_{n>0} \alpha_i \alpha_i + \frac{1}{2} \sum_{n>0} n.$$ The final term clearly diverges. But it at least seems to have a physical interpretation: it is the sum of zero point energies of an infinite number of harmonic oscillators. In fact, we came across exactly the same type of term in the course on quantum field theory where we learnt that, despite the divergence, one can still extract interesting physics from this. This is the physics of the Casimir force.

Let’s recall the steps that we took to derive the Casimir force. Firstly, we introduced an ultra-violet cut-off $\epsilon \ll 1$, probably muttering some words about no physical plates being able to withstand very high energy quanta. Unfortunately, those words are no longer available to us in string theory, but let’s proceed regardless. We replace the divergent sum over integers by the expression, $$\sum_{n=1}^{\infty} n \longrightarrow \sum_{n=1}^{\infty} n e^{-\epsilon n} = -\frac{\partial}{\partial \epsilon} \sum_{n=1}^{\infty} e^{-\epsilon n}$$ $$= -\frac{\partial}{\partial \epsilon} (1-e^{-\epsilon})^{-1}$$ $$= -\frac{1}{\epsilon^2} + \frac{1}{12} + O(\epsilon)$$ Obviously the $1/\epsilon^2$ piece diverges as $\epsilon \rightarrow 0$. This term should be renormalized away. In fact, this is necessary to preserve the Weyl invariance of the Polyakov action since it contributes to a cosmological constant on the worldsheet. After this renormalization, we’re left with the wonderful answer, first intuited by Ramanujan $$\sum_{n=1}^{\infty} n = -\frac{1}{12}.$$ While heuristic, this argument does predict the correct physical Casimir energy measured in one-dimensional systems. For example, this effect is seen in simulations of quantum spin chains.

What does this mean for our string? It means that we should take the unknown constant $a$ in the mass formula (2.25) to be, $$M^2 = \frac{4}{\alpha'} \left( N - \frac{D-2}{24} \right) = \frac{4}{\alpha'} \left( \tilde{N} - \frac{D-2}{24} \right). \tag{2.26}$$ This is the formula that we will use to determine the spectrum of the string.

Zeta Function Regularization

I appreciate that the preceding argument is not totally convincing. We could spend some time making it more robust at this stage, but it’s best if we wait until later in the course when we will have the tools of conformal field theory at our disposal. We will eventually revisit this issue and provide a respectable derivation of the Casimir energy in Section 4.4.1. For now I merely offer an even less convincing argument, known as zeta-function regularization.

The zeta-function is defined, for $\text{Re}(s) > 1$, by the sum $$\zeta(s) = \sum_{n=1}^{\infty} n^{-s}.$$ But $\zeta(s)$ has a unique analytic continuation to all values of $s$. In particular, $$\zeta(-1) = -\frac{1}{12}.$$ Good? Good. This argument is famously unconvincing the first time you meet it! But it’s actually a very useful trick for getting the right answer.

## 2.3 The String Spectrum

Finally, we’re in a position to analyze the spectrum of a single, free string.

2.3.1 The Tachyon

Let’s start with the ground state $|0;p\rangle$ defined in (2.23). With no oscillators excited, the mass formula (2.26) gives $$M^2 = -\frac{1}{\alpha'} \frac{D-2}{6}. \tag{2.27}$$ But that’s a little odd. It’s a negative mass-squared. Such particles are called tachyons. In fact, tachyons aren’t quite as pathological as you might think. If you’ve heard of these objects before, it’s probably in the context of special relativity where they’re strange beasts which always travel faster than the speed of light. But that’s not the right interpretation. Rather we should think more in the language of quantum field theory. Suppose that we have a field in spacetime — let’s call it $T(X)$ — whose quanta will give rise to this particle. The mass-squared of the particle is simply the quadratic term in the action, or $$M^2 = \left. \frac{\partial^2 V(T)}{\partial T^2} \right|_{T=0}$$ So the negative mass-squared in (2.27) is telling us that we’re expanding around a maximum of the potential for the tachyon field as shown in the figure. Note that from this perspective, the Higgs field in the standard model at $H = 0$ is also a tachyon.

The fact that string theory turns out to sit at an unstable point in the tachyon field is unfortunate. The natural question is whether the potential has a good minimum elsewhere, as shown in the figure to the right. No one knows the answer to this! Naive attempts to understand this don’t work. We know that around $T = 0$, the leading order contribution to the potential is negative and quadratic. But there are further terms that we can compute using techniques that we’ll describe in Section 6. An expansion of the tachyon potential around $T = 0$ looks like $$V(T) = M^2 T^2 + c_3 T^3 + c_4 T^4 +...$$ It turns out that the $T^3$ term in the potential does give rise to a minimum. But the T4 term destabilizes it again. Moreover, the T field starts to mix with other scalar fields in the theory that we will come across soon. The ultimate fate of the tachyon in the bosonic string is not yet understood. The tachyon is a problem for the bosonic string. It may well be that this theory makes no sense — or, at the very least, has no time-independent stable solutions. Or perhaps we just haven’t worked out how to correctly deal with the tachyon. Either way, the problem does not arise when we introduce fermions on the worldsheet and study the superstring. This will involve several further technicalities which we won’t get into in this course. Instead, our time will be put to better use if we continue to study the bosonic string since all the lessons that we learn will carry over directly to the superstring. However, one should be aware that the problem of the unstable vacuum will continue to haunt us throughout this course. Although we won’t describe it in detail, at several times along our journey we’ll make an aside about how calculations work out for the superstring.

2.3.2 The First Excited States We now look at the first excited states. If we act with a creation operator αj , then the level matching condition (2.25) tells us that we also need to act with a α˜i operator. This gives us (D−2)2 particle states, α˜i αj |0;p⟩ , (2.28)

each of which has mass M² = (1/α')(1 - (D-2)/24).

But now we seem to have a problem. Our states have space indices i,j = 1,...,D−2. The operators αi and α˜i each transform in the vector representation of SO(D −2) ⊂ SO(1,D−1) which is manifest in lightcone gauge. But ultimately we want these states to fit into some representation of the full Lorentz SO(1,D −1) group. That looks as if it’s going to be hard to arrange. This is the first manifestation of the comment that we made after equation (2.12): it’s tricky to see Lorentz invariance in lightcone gauge. To proceed, let’s recall Wigner’s classification of representations of the Poincaré group. We start by looking at massive particles in R1,D−1. After going to the rest frame of the particle by setting pµ = (p,0,...,0), we can watch how any internal indices transform under the little group SO(D − 1) of spatial rotations. The upshot of this is that any massive particle must form a representation of SO(D−1). But the particles described by (2.28) have (D − 2)2 states. There’s no way to package these states into a representation of SO(D−1) and this means that there’s no way that the first excited states of the string can form a massive representation of the D-dimensional Poincaré group. It looks like we’re in trouble. Thankfully, there’s a way out. If the states are massless, then we can’t go to the rest frame. The best that we can do is choose a spacetime momentum for the particle of the form pµ = (p,0,...,0,p). In this case, the particles fill out a representation of the little group SO(D−2). This means that massless particles get away with having fewer internal states than massive particles. For example, in four dimensions the photon has two polarization states, but a massive spin-1 particle must have three. The first excited states (2.28) happily sit in a representation of SO(D−2). We learn that if we want the quantum theory to preserve the SO(1,D − 1) Lorentz symmetry that we started with, then these states will have to be massless. And this is only the case if the dimension of spacetime is D = 26. This is our first derivation of the critical dimension of the bosonic string. Moreover, we’ve found that our theory contains a bunch of massless particles. And massless particles are interesting because they give rise to long range forces. Let’s look more closely at what massless particles the string has given us. The states (2.28) transform in the 24⊗24 representation of SO(24). These decompose into three irreducible representations: traceless symmetric ⊕ anti-symmetric ⊕ singlet (=trace). To each of these modes, we associate a massless field in spacetime such that the string oscillation can be identified with a quantum of these fields. The fields are: Gµν(X) , Bµν(X) , Φ(X) (2.29). Of these, the first is the most interesting and we shall have more to say momentarily. The second is an anti-symmetric tensor field which is usually called the anti-symmetric tensor field. It also goes by the names of the “Kalb-Ramond field” or, in the language of differential geometry, the “2-form”. The scalar field is called the dilaton. These three massless fields are common to all string theories. We’ll learn more about the role these fields play later in the course. The particle in the symmetric traceless representation of SO(24) is particularly interesting. This is a massless spin 2 particle. However, there are general arguments, due originally to Feynman and Weinberg, that any theory of interacting massless spin two particles must be equivalent to general relativity.

ould therefore identify the field G (X) with the metric of spacetime. Let’s pause briefly to review the thrust µν of these arguments.

Why Massless Spin 2 = General Relativity Let’s call the spacetime metric G (X). We can expand around flat space by writing µν G = η +h (X) .

µν µν µν Then the Einstein-Hilbert action has an expansion in powers of h. If we truncate to quadratic order, we simply have a free theory which we may merrily quantize in the usual canonical fashion: we promote h to an operator and introduce the associated µν creation and annihilation operators a and a† . This way of looking at gravity is µν µν anathema to those raised in the geometrical world of general relativity. But from a particle physics language it is very standard: it is simply the quantization of a massless spin 2 field, h .

µν 2AveryreadabledescriptionofthiscanbefoundinthefirstfewchaptersoftheFeynmanLectures on Gravitation.

– 43 – However, even on this simple level, there is a problem due to the indefinite signature ofthespacetimeMinkowskimetric. Thecanonicalquantizationrelationsofthecreation and annihilation operators are schematically of the form, [a ,a† ] ∼ η η +η η µν ρσ µρ νσ µσ νρ But this will lead to a Hilbert space with negative norm states coming from acting with time-like creation operators. For example, the one-graviton state of the form, a† |0(cid:105) (2.30)

0i suffers from a negative norm. This should be becoming familiar by now: it is the usual problem that we run into if we try to covariantly quantize a gauge theory. And, indeed, general relativity is a gauge theory. The gauge transformations are diffeomorphisms.

We would hope that this saves the theory of quantum gravity from these negative norm states.

Let’slookalittlemorecloselyatwhatthegaugesymmetrylookslikeforsmallfluctu- ations h . We’ve butchered the Einstein-Hilbert action and left only terms quadratic µν in h. Including all the index contractions, we find M2 (cid:90) (cid:20) 1 1 (cid:21)

S = pl d4x ∂ hρ ∂ hµν −∂ρhµν∂ h + ∂ h ∂ρhµν − ∂ hν ∂µhρ +...

EH 2 µ ρ ν µ ρν 2 ρ µν 2 µ ν ρ One can check that this truncated action is invariant under the gauge symmetry, h −→ h +∂ ξ +∂ ξ (2.31)

µν µν µ ν ν µ for any function ξ (X). The gauge symmetry is the remnant of diffeomorphism invari- ance, restricted to small deviations away from flat space. With this gauge invariance in hand one can show that, just like QED, the negative norm states decouple from all physical processes.

To summarize, theories of massless spin 2 fields only make sense if there is a gauge symmetry to remove the negative norm states. In general relativity, this gauge symme- try descends from diffeomorphism invariance. The argument of Feynman and Weinberg now runs this logic in reverse. It goes as follows: suppose that we have a massless, spin 2 particle. Then, at the linearized level, it must be invariant under the gauge symmetry (2.31) in order to eliminate the negative norm states. Moreover, this symmetry must survive when interaction terms are introduced. But the only way to do this is to ensure that the resulting theory obeys diffeomorpism invariance. That means the theory of any interacting, massless spin 2 particle is Einstein gravity, perhaps supplemented by higher derivative terms.

– 44 – We haven’t yet shown that string theory includes interactions for h but we will µν come to this later in the course. More importantly, we will also explicitly see how Einstein’s field equations arise directly in string theory.

A Comment on Spacetime Gauge Invariance We’ve surreptitiously put µ,ν = 0,...,25 indices on the spacetime fields, rather than i,j = 1,...,24. The reason we’re allowed to do this is because both G and B enjoy µν µν a spacetime gauge symmetry which allows us to eliminate appropriate modes. Indeed, this is exactly the gauge symmetry (2.31) that entered the discussion above. It isn’t possible to see these spacetime gauge symmetries from the lightcone formalism of the string since, by construction, we find only the physical states (although, by consistency alone, the gauge symmetries must be there). One of the main advantages of pushing through with the covariant calculation is that it does allow us to see how the spacetime gauge symmetry emerges from the string worldsheet. Details can be found in Green, Schwarz and Witten. We’ll also briefly return to this issue in Section 5.

2.3.3 Higher Excited States We rescued the Lorentz invariance of the first excited states by choosing D = 26 to ensure that they are massless. But now we’ve used this trick once, we still have to worry about all the other excited states. These also carry indices that take the range i,j = 1,...,D − 2 = 24 and, from the mass formula (2.26), they will all be massive and so must form representations of SO(D−1). It looks like we’re in trouble again.

Let’s examine the string at level N = N = 2. In the right-moving sector, we now have two different states: αi αj |0(cid:105) and αi |0(cid:105). The same is true for the left-moving sector, meaning that the total set of states at level 2 is (in notation that is hopefully obvious, but probably technically wrong)

(αi αj ⊕ αi ) ⊗ (α˜i α˜j ⊕ α˜i )|0;p⟩.

−1 −1 −2 −1 −1 −2 These states have mass M² = 4/α'. How many states do we have? In the left-moving sector, we have, ½(D−2)(D−1) + (D−2) = ½D(D−1) − 1.

But, remarkably, that does fit nicely into a representation of SO(D − 1), namely the traceless symmetric tensor representation.

In fact, one can show that all excited states of the string fit nicely into SO(D − 1) representations. The only consistency requirement that we need for Lorentz invariance is to fix up the first excited states: D = 26.

Note that if we are interested in a fundamental theory of quantum gravity, then all these excited states will have masses close to the Planck scale so are unlikely to be observable in particle physics experiments. Nonetheless, as we shall see when we come to discuss scattering amplitudes, it is the presence of this infinite tower of states that tames the ultra-violet behaviour of gravity.

## 2.4 Lorentz Invariance Revisited

The previous discussion allowed to us to derive both the critical dimension and the spectrum of string theory in the quickest fashion. But the derivation creaks a little in places. The calculation of the Casimir energy is unsatisfactory the first time one sees it. Similarly, the explanation of the need for massless particles at the first excited level is correct, but seems rather cheap considering the huge importance that we’re placing on the result.

As I’ve mentioned a few times already, we’ll shortly do better and gain some physical insight into these issues, in particular the critical dimension. But here I would just like to briefly sketch how one can be a little more rigorous within the framework of lightcone quantization. The question, as we’ve seen, is whether one preserves spacetime Lorentz symmetry when we quantize in lightcone gauge. We can examine this more closely.

Firstly, let’s go back to the action for free scalar fields (1.30) before we imposed lightcone gauge fixing. Here the full Poincaré symmetry was manifest: it appears as a global symmetry on the worldsheet, Xµ → Λµ Xν + cµ (2.32)

But recall that in field theory, global symmetries give rise to Noether currents and their associated conserved charges. What are the Noether currents associated to this Poincaré transformation? We can start with the translations Xµ → Xµ + cµ. A quick computation shows that the current is, Pα = T∂αXµ (2.33)

µ which is indeed a conserved current since ∂α Pµ = 0 is simply the equation of motion.

Similarly, we can compute the ½D(D − 1) currents associated to Lorentz transformations. They are, Jα = PαX − PαX µν µ ν ν µ It’s not hard to check that ∂α Jµν = 0 when the equations of motion are obeyed.

The conserved charges arising from this current are given by M = ∫ dσJτ . Using the mode expansion (1.36) for Xµ, these can be written as µν µν Mµν = (pµxν − pνxµ) − i ∑ (1/n)(αν αµ − αµ αν) − i ∑ (1/n)(α˜ν α˜µ − α˜µ α˜ν)

n −n n −n n n −n n n=1 n=1 ≡ lµν + Sµν + S ˜µν The first piece, lµν, is the orbital angular momentum of the string while the remaining pieces Sµν and S ˜µν tell us the angular momentum due to excited oscillator modes. Classically, these obey the Poisson brackets of the Lorentz algebra. Moreover, if we quantize in the covariant approach, the corresponding operators obey the commutation relations of the Lorentz Lie algebra, namely [Mρσ, Mτν] = ηστ Mρν − ηρτ Mσν + ηρν Mστ − ησν Mρτ However, things aren’t so easy in lightcone gauge. Lorentz invariance is not guaranteed and, in general, is not there. The right way to go about looking for it is to make sure that the Lorentz algebra above is reproduced by the generators Mµν. It turns out that the smoking gun lies in the commutation relation, [Mi−, Mj−] = 0 Does this equation hold in lightcone gauge? The problem is that it involves the operators p− and α−, both of which are fixed by (2.17) and (2.18) in terms of the other operators. So the task is to compute this commutation relation [Mi−, Mj−], given the commutation relations (2.21) for the physical degrees of freedom, and check that it vanishes. To do this, we re-instate the ordering ambiguity a and the number of spacetime dimension D as arbitrary variables and proceed.

The part involving orbital angular momenta li− is fairly straightforward. (Actually, there’s a small subtlety because we must first make sure that the operator lµν is Hermitian by replacing xµpν with ½(xµpν + pνxµ)). The real difficulty comes from computing the commutation relations [Si−, Sj−]. This is messy³. After a tedious computation, one finds, [Mi−, Mj−] = −(1/(p+)²) ∑_{n>0} (1/n) [ (D−2)/24 n + a − (D−2)/24 ] (αi αj − αj αi) + (α ↔ α˜)

³The original, classic, paper where lightcone quantization was first implemented is Goddard, Goldstone, Rebbi and Thorn "Quantum Dynamics of a Massless Relativistic String", Nucl. Phys. B56 (1973). A pedestrian walkthrough of this calculation can be found in the lecture notes by Gleb Arutyunov. A link is given on the course webpage.

The right-hand side does not, in general, vanish. We learn that the relativistic string can only be quantized in flat Minkowski space if we pick, D = 26 and a = 1.

## 2.5 A Nod to the Superstring

We won’t provide details of the superstring in this course, but will pause occasionally to make some pertinent comments. Although what follows is nothing more than a list of facts, it will hopefully be helpful in orienting you when you do come to study this material.

The key difference between the bosonic string and the superstring is the addition of fermionic modes on its worldsheet. The resulting worldsheet theory is supersymmetric. (At least in the so-called Neveu-Schwarz-Ramond formalism). Hence the name "superstring". Applying the kind of quantization procedure we’ve discussed in this section, one finds the following results: • The critical dimension of the superstring is D = 10.

• There is no tachyon in the spectrum.

• The massless bosonic fields G_μν, B_μν and Φ are all part of the spectrum of the superstring. In this context, B_μν is sometimes referred to as the Neveu-Schwarz 2-form. There are also massless spacetime fermions, as well as further massless bosonic fields. As we now discuss, the exact form of these extra bosonic fields depends on exactly what superstring theory we consider.

While the bosonic string is unique, there are a number of discrete choices that one can make when adding fermions to the worldsheet. This gives rise to a handful of different perturbative superstring theories. (Although later developments reveal that they are actually all part of the same framework which sometimes goes by the name of M-theory). The most important of these discrete options is whether we add fermions in both the left-moving and right-moving sectors of the string, or whether we choose the fermions to move only in one direction, usually taken to be right-moving. This gives rise to two different classes of string theory.

• Type II strings have both left and right-moving worldsheet fermions. The resulting spacetime theory in D = 10 dimensions has N = 2 supersymmetry, which means 32 supercharges.

• Heterotic strings have just right-moving fermions. The resulting spacetime theory has N = 1 supersymmetry, or 16 supercharges.

In each of these cases, there is then one further discrete choice that we can make. This leaves us with four superstring theories. In each case, the massless bosonic fields include G_μν, B_μν and Φ together with a number of extra fields. These are: • Type IIA: In the type II theories, the extra massless bosonic excitations of the string are referred to as Ramond-Ramond fields. For Type IIA, they are a 1-form C_μ and a 3-form C_μνρ. Each of these is to be thought of as a gauge field. The gauge invariant information lies in the field strengths which take the form F = dC.

• Type IIB: The Ramond-Ramond gauge fields consist of a scalar C, a 2-form C_μν and a 4-form C_μνρσ. The 4-form is restricted to have a self-dual field strength: F_5 = *F_5. (Actually, this statement is almost true...we’ll look a little closer at this in Section 7.3.3).

• Heterotic SO(32): The heterotic strings do not have Ramond-Ramond fields. Instead, each comes with a non-Abelian gauge field in spacetime. The heterotic strings are named after the gauge group. For example, the Heterotic SO(32) string gives rise to an SO(32) Yang-Mills theory in ten dimensions.

• Heterotic E₈ × E₈: The clue is in the name. This string gives rise to an E₈ × E₈ Yang-Mills field in ten-dimensions.

It is sometimes said that there are five perturbative superstring theories in ten dimensions. Here we’ve only mentioned four. The remaining theory is called Type I and includes open strings moving in flat ten dimensional space as well as closed strings. We’ll mention it in passing in the following section.

## 3. Open Strings and D-Branes

In this section we discuss the dynamics of open strings. Clearly their distinguishing feature is the existence of two end points. Our goal is to understand the effect of these end points. The spatial coordinate of the string is parameterized by σ ∈ [0,π].

The dynamics of a generic point on a string is governed by local physics. This means that a generic point has no idea if it is part of a closed string or an open string. The dynamics of an open string must therefore still be described by the Polyakov action. But this must now be supplemented by something else: boundary conditions to tell us how the end points move. To see this, let’s look at the Polyakov action in conformal gauge S = -1/(4πα') ∫ d²σ ∂_α X · ∂^α X.

As usual, we derive the equations of motion by finding the extrema of the action. This involves an integration by parts. Let’s consider the s string evolving from some initial configuration at τ = τ_i to some final configuration at τ = τ_f: δS = - (1/(2πα')) ∫_{τ_i}^{τ_f} dτ ∫_0^π dσ ∂_α X · ∂^α δX = ∫ d^2σ (∂_α ∂^α X)·δX + total derivative For an open string the total derivative picks up the boundary contributions (1/(2πα')) [∫_0^π dσ X˙·δX]_{τ=τ_f} - (1/(2πα')) [∫_{τ_i}^{τ_f} dτ X'·δX]_{σ=π} + (1/(2πα')) [∫_{τ_i}^{τ_f} dτ X'·δX]_{σ=0} The first term is the kind that we always get when using the principle of least action. The equations of motion are derived by requiring that δX^μ = 0 at τ = τ_i and τ_f and so it vanishes. However, the second term is novel. In order for it too to vanish, we require ∂_σ X^μ δX_μ = 0 at σ = 0,π There are two different types of boundary conditions that we can impose to satisfy this: • Neumann boundary conditions.

∂_σ X^μ = 0 at σ = 0,π (3.1)

Because there is no restriction on δX^μ, this condition allows the end of the string to move freely. To see the consequences of this, it’s useful to repeat what we did for the closed string and work in static gauge with X^0 ≡ t = Rτ, for some dimensionful constant R. Then, as in equations (1.34), the constraints read x˙·x' = 0 and x˙^2 + x'^2 = R^2 But at the end points of the string, x' = 0. So the second equation tells us that |dx/dt| = 1. Or, in other words, the end point of the string moves at the speed of light.

• Dirichlet boundary conditions δX^μ = 0 at σ = 0,π (3.2)

This means that the end points of the string lie at some constant position, X^μ = c^μ, in space.

At first sight, Dirichlet boundary conditions may seem a little odd. Why on earth would the strings be fixed at some point c^μ? What is special about that point? Historically people were pretty hung up about this and Dirichlet boundary conditions were rarely considered until the mid-1990s. Then everything changed due to an insight of Polchinski...

Let’s consider Dirichlet boundary conditions for some coordinates and Neumann for the others. This means that at both end points of the string, we have ∂_σ X^a = 0 for a = 0,...,p X^I = c^I for I = p+1,...,D-1 (3.3)

This fixes the end-points of the string to lie in a (p + 1)-dimensional hypersurface in spacetime such that the SO(1,D-1) Lorentz group is broken to, SO(1,D-1) → SO(1,p)×SO(D-p-1).

This hypersurface is called a D-brane or, when we want to specify its dimension, a Dp-brane. Here D stands for Dirichlet, while p is the number of spatial dimensions of the brane. So, in this language, a D0-brane is a particle; a D1-brane is itself a string; a D2-brane a membrane and so on. The brane sits at specific positions c^I in the transverse space. But what is the interpretation of this hypersurface?

It turns out that the D-brane hypersurface should be thought of as a new, dynamical object in its own right. This is a conceptual leap that is far from obvious. Indeed, it took decades for people to fully appreciate this fact. String theory is not just a theory of strings: it also contains higher dimensional branes. In Section 7.5 we will see how these D-branes develop a life of their own. Some comments: • We’ve defined D-branes that are infinite in space. However, we could just as well define finite D-branes by specifying closed surfaces on which the string can end.

• There are many situations where we want to describe strings that have Neumann boundary conditions in all directions, meaning that the string is free to move throughout spacetime. It’s best to understand this in terms of a space-filling D-brane. No Dirichlet conditions means D-branes are everywhere!

• The Dp-brane described above always has Neumann boundary conditions in the X^0 direction. What would it mean to have Dirichlet conditions for X^0? Obviously this is a little weird since the object is now localized at a fixed point in time. But there is an interpretation of such an object: it is an instanton. This “D-instanton” is usually referred to as a D(-1)-brane. It is related to tunneling effects in the quantum theory.

Mode Expansion We take the usual mode expansion for the string, with X^μ = X_L^μ(σ+) + X_R^μ(σ-) and X_L^μ(σ+) = (1/2)x^μ + α' p^μ σ+ + i √(α'/2) Σ_{n≠0} (1/n) α̃_n^μ e^{-inσ+}, X_R^μ(σ-) = (1/2)x^μ + α' p^μ σ- + i √(α'/2) Σ_{n≠0} (1/n) α_n^μ e^{-inσ-}. (3.4)

The boundary conditions impose relations on the modes of the string. They are easily checked to be: • Neumann boundary conditions, ∂_σ X^a = 0, at the end points require that α_n^a = α̃_n^a (3.5)

• Dirichlet boundary conditions, X^I = c^I, at the end points require that x^I = c^I , p^I = 0 , α_n^I = -α̃_n^I So for both boundary conditions, we only have one set of oscillators, say α_n. The α̃_n are then determined by the boundary conditions.

It’s worth pointing out that there is a factor of 2 difference in the p^μ term between the open string (3.4) and the closed string (1.36). This is to ensure that p μ for the open string retains the interpretation of the spacetime momentum of the string when σ ∈ [0,π]. To see this, one needs to check the Noether current associated to translations of Xμ on the worldsheet: it was given in (2.33). The conserved charge is then Pμ = ∫₀^π dσ (Pτ)^μ = ∫₀^π dσ Ẋ^μ = pμ as advertised. Note that we’ve needed to use the Neumann conditions (3.5) to ensure that the Fourier modes don’t contribute to this integral.

## 3.1 Quantization

To quantize, we promote the fields xᵃ and pᵃ and αμ to operators. The other elements in the mode expansion are fixed by the boundary conditions. An obvious, but important, point is that the position and momentum degrees of freedom, xᵃ and pᵃ, have a spacetime index that takes values a = 0,...,p. This means that the spatial wavefunctions only depend on the coordinates of the brane not the whole spacetime. Said another, quantizing an open string gives rise to states which are restricted to lie on the brane.

To determine the spectrum, it is again simplest to work in lightcone gauge. The spacetime lightcone coordinate is chosen to lie within the brane, X± = (X⁰ ± Xᵖ)

Quantization now proceeds in the same manner as for the closed string until we arrive at the mass formula for states which is a sum over the transverse modes of the string.

M² = (1/α') [ Σᵢ₌₁^{p-1} Σ_{n>0} α_{-n}ⁱ αₙⁱ + Σᵢ₌ₚ₊₁^{D-1} Σ_{n>0} α_{-n}ⁱ αₙⁱ - a ]

The first sum is over modes parallel to the brane, the second over modes perpendicular to the brane. It’s worth commenting on the differences with the closed string formula. Firstly, there is an overall factor of 4 difference. This can be traced to the lack of the factor of 1/2 in front of pμ in the mode expansion that we discussed above. Secondly, there is a sum only over α modes. The α̃ modes are not independent because of the boundary conditions.

In the mass formula, we have once again left the normal ordering constant a ambiguous. As in the closed string case, requiring the Lorentz symmetry of the quantum theory — this time the reduced symmetry SO(1,p)×SO(D−p−1) — forces us to choose D = 26 and a = 1. These are the same values that we found for the closed string. This reflects an important fact: the open string and closed string are not different theories. They are both different states inside the same theory.

More precisely, theories of open strings necessarily contain closed strings. This is because, once we consider interactions, an open string can join to form a closed string as shown in the figure. We’ll look at interactions in Section 6. The question of whether this works the other way — meaning whether closed string theories require open strings — is a little more involved and is cleanest to state in the context of the superstring. For type II superstrings, the open strings and D-branes are necessary ingredients. For heterotic superstrings, there appear to be no open strings and no D-branes. For the bosonic theory, it seems likely that the open strings are a necessary ingredient although I don’t know of a killer argument. But since we’re not sure whether the theory exists due to the presence of the tachyon, the point is probably moot. In the remainder of these lectures, we’ll view the bosonic string in the same manner as the type II string and assume that the theory includes both closed strings and open strings with their associated D-branes.

3.1.1 The Ground State The ground state is defined by αₙⁱ |0;p⟩ = 0 for n > 0 The spatial index now runs over i = 1,...,p−1,p+1,...,D −1. The ground state has mass M² = -1/α' It is again tachyonic. Its mass is half that of the closed string tachyon. As we commented above, this time the tachyon is confined to the brane. In contrast to the closed string tachyon, the open string tachyon is now fairly well understood and its potential is of the form shown in the figure. The interpretation is that the brane is unstable. It will decay, much like a resonance state in field theory. It does this by dissolving into closed string modes. The end point of this process – corresponding to the minimum at T > 0 in the figure – is simply a state with no D-brane. The difference between the value of the potential at the minimum and at T = 0 is the tension of the D-brane.

Notice that although there is a minimum of the potential at T > 0, it is not a global minimum. The potential seems to drop off without bound to the left. This is still not well understood. There are suggestions that it is related in some way to the closed string tachyon.

3.1.2 First Excited States: A World of Light The first excited states are massless. They fall into two classes: • Oscillators longitudinal to the brane, α₋₁ᵃ |0;p⟩ for a = 1,...,p−1 The spacetime indices a lie within the brane so this state transforms under the SO(1,p) Lorentz group. It is a spin 1 particle on the brane or, in other words, it is a photon. We introduce a gauge field A with a = 0,..

lying on the brane whose quanta are identified with this photon.

• Oscillators transverse to the brane, αI |0;p⟩ I = p+1,...,D−1 These states are scalars under the SO(1,p) Lorentz group of the brane. They can be thought of as arising from scalar fields φI living on the brane. These scalars have a nice interpretation: they are fluctuations of the brane in the transverse directions. This is our first hint that the D-brane is a dynamical object. Note that although the φI are scalar fields under the SO(1,p) Lorentz group of the brane, they do transform as a vector under the SO(D−p−1) rotation group transverse to the brane. This appears as a global symmetry on the brane worldvolume.

3.1.3 Higher Excited States and Regge Trajectories At level N, the mass of the string state is M2 = (N −1) α′ The maximal spin of these states arises from the symmetric tensor. It is Jmax = N = α′M2 +1 Plotting the spin vs. the mass-squared, we find straight lines. These are usually called Regge trajectories. (Or sometimes Chew-Frautschi trajectories). They are seen in Nature in both the spectrum of mesons and baryons. Some examples involving ρ-mesons are shown in the figure. These stringy Regge trajectories suggest a naive cartoon picture of mesons as two rotating quarks connected by a confining flux tube.

The value of the string tension required to match the hadron spectrum of QCD is T ∼ 1 GeV. This relationship between the strong interaction and the open string was one of the original motivations for the development of string theory and it is from here that the parameter α′ gets its (admittedly rarely used) name “Regge slope”. In these enlightened modern times, the connection between the open string and quarks lives on in the AdS/CFT correspondence.

3.1.4 Another Nod to the Superstring Just as supersymmetry eliminates the closed string tachyon, so it removes the open string tachyon. Open strings are an ingredient of the type II string theories. The possible D-branes are • Type IIA string theory has stable Dp-branes with p even.

• Type IIB string theory has stable Dp-branes with p odd.

The most important reason that D-branes are stable in the type II string theories is that they are charged under the Ramond-Ramond fields. (This was actually Polchinski’s insight that made people take D-branes seriously). However, type II string theories also contain unstable branes, with p odd in type IIA and p even in type IIB.

The fifth string theory (which was actually the first to be discovered) is called Type I. Unlike the other string theories, it contains both open and closed strings moving in flat ten-dimensional Lorentz-invariant spacetime. It can be thought of as the Type IIB theory with a bunch of space-filling D9-branes, together with something called an orientifold plane. You can read about this in Polchinski.

As we mentioned above, the heterotic string doesn’t have (finite energy) D-branes. This is due to an inconsistency in any attempt to reflect left-moving modes into right-moving modes.

## 3.2 Brane Dynamics: The Dirac Action

We have introduced D-branes as fixed boundary conditions for the open string. However, we’ve already seen a hint that these objects are dynamical in their own right, since the massless scalar excitations φI have a natural interpretation as transverse fluctuations of the brane. Indeed, if a theory includes both open strings and closed strings, then the D-branes have to be dynamical because there can be no rigid objects in a theory of gravity. The dynamical nature of D-branes will become clearer as the course progresses.

But any dynamical object should have an action which describes how it moves. Moreover, after our discussion in Section 1, we already know what this is! On grounds of Lorentz invariance and reparameterization invariance alone, the action must be a higher dimensional extension of the Nambu-Goto action. This is S = −T ∫ dp+1ξ √−detγ (3.6)

where T is the tension of the Dp-brane which we will determine later, while ξa, a = 0,...,p, are the worldvolume coordinates of the brane. γab is the pull back of the spacetime metric onto the worldvolume, γab = ηµν ∂Xµ/∂ξa ∂Xν/∂ξb This is called the Dirac action. It was first written down by Dirac for a membrane some time before Nambu and Goto rediscovered it in the context of the string.

To make contact with the fields φI, we can use the reparameterization invariance of the Dirac action to go to static gauge. For an infinite, flat Dp-brane we can choose Xa = ξa a = 0,...,p .

The dynamical transverse coordinates are then identified with the fluctuations φI through XI(ξ) = 2πα′φI(ξ) I = p+1,...,D−1 However, the Dirac action can’t be the whole story. It describes the transverse fluctuations of the D-brane, but has nothing to say about the U(1) gauge field A which lives on the D-brane. There must be some action which describes how this gauge field moves as well. We will return to this in Se

## Section 7

What’s Special About Strings?

We could try to quantize the Dirac action (3.6) for a D-brane in the same manner that we quantized the action for the string. Is this possible? The answer, at present, is no. There appear to be both technical and conceptual obstacles. The technical issue is just that it’s hard. Weyl invariance was one of our chief weapons in attacking the string, but it doesn’t hold for higher dimensional objects.

The conceptual issue is that quantizing a membrane, or higher dimensional object, would not give rise to a discrete spectrum of states which have the interpretation of particles. In this way, they appear to be fundamentally different from the string. Let’s get some intuition for why this is the case.

The energy of a string is proportional to its length. This ensures that strings behave more or less like familiar elastic bands. What about D2-branes? Now the energy is proportional to the area. In the back of your mind, you might be thinking of a rubber-like sheet. But membranes, and higher dimensional objects, governed by the Dirac action don’t behave as household rubber sheets. They are more flexible. This is because a membrane can form many different shapes with the same area. For example, a tubular membrane of length L and radius 1/L has the same area for all values of L; short and stubby, or long and thin. This means that long thin spikes can develop on a membrane at no extra cost of energy. In particular, objects connected by long thin tubes have the same energy, regardless of their separation. After quantization, this property gives rise to a continuous spectrum of states. A quantum membrane, or higher dimensional object, does not have the single particle interpretation that we saw for the string. The expectation is that the quantum membrane should describe multi-particle states.

## 3.3 Multiple Branes: A World of Glue

Consider two parallel Dp-branes. An open string now has options. It could either end on the same brane, or stretch between the two branes. Let’s consider the string that stretches between the two. It obeys XI(0,τ) = cI and XI(π,τ) = dI where cI and dI are the positions of the two branes. In terms of the mode expansion, this requires XI = cI + (dI −cI)σ/π + oscillator modes The classical constraints then read ∂ X ·∂ X = α’2p2 + |d −c|2/(4π2) + oscillator modes = 0 which means the classical mass-shell condition is M2 = |d −c|2/(2πα’)2 + oscillator modes The extra term has an obvious interpretation: it is the mass of a classical string stretched between the two branes. The quantization of this string proceeds as before. After we include the normal ordering constant, the ground state of this string is only tachyonic if |d −c|2 < 4π2α’. Or in other words, the ground state is tachyonic if the branes approach to a sub-stringy distance.

There is an obvious generalization of this to the case of N parallel branes. Each end point of the string has N possible places on which to end. We can label each end point with a number m,n = 1,...,N which tell us which brane it ends on. This label is sometimes referred to as a Chan-Paton factor.

Consider now the situation where all branes lie at the same position in spacetime. Each end point can lie on one of N different branes, giving N2 possibilities in total. Each of these strings has the mass spectrum of an open string, meaning that there are now N2 different particles of each type. It’s natural to arrange the associated fields to sit inside N ×N Hermitian matrices. We then have the open string tachyon T and the massless fields (φI)m , (Aa)m (3.7)

n n Here the components of the matrix tell us which string the field came from. Diagonal components arise from strings which have both ends on the same brane.

The gauge field A is particularly interesting. Written in this way, it looks like a U(N) gauge connection. We will later see that this is indeed the case. One can show that as N branes coincide, the U(1)N gauge symmetry of the branes is enhanced to U(N). The scalar fields φI transform in the adjoint of this symmetry.

## 4. Introducing Conformal Field Theory

The purpose of this section is to get comfortable with the basic language of two dimensional conformal field theory4. This is a topic which has many applications outside of string theory, most notably in statistical physics where it offers a description of critical phenomena. Moreover, it turns out that conformal field theories in two dimensions provide rare examples of interacting, yet exactly solvable, quantum field theories. In recent years, attention has focussed on conformal field theories in higher dimensions due to their role in the AdS/CFT correspondence.

A conformal transformation is a change of coordinates σα → σ˜α(σ) such that the metric changes by gαβ(σ) → Ω2(σ)gαβ(σ) (4.1)

A conformal field theory (CFT) is a field theory which is invariant under such transformations.

ant under these transformations. This means that the physics of the theory looks the same at all length scales. Conformal field theories care about angles, but not about distances.

A transformation of the form (4.1) has a different interpretation depending on whether we are considering a fixed background metric g_{αβ}, or a dynamical background metric. When the metric is dynamical, the transformation is a diffeomorphism; this is a gauge symmetry. When the background is fixed, the transformation should be thought of as an honest, physical symmetry, taking the point σ^α to point σ̃^α. This is now a global symmetry with the corresponding conserved currents.

In the context of string theory in the Polyakov formalism, the metric is dynamical and the transformations (4.1) are residual gauge transformations: diffeomorphisms which can be undone by a Weyl transformation.

In contrast, in this section we will be primarily interested in theories defined on fixed backgrounds. Apart from a few noticeable exceptions, we will usually take this background to be flat. This is the situation that we are used to when studying quantum field theory.

Much of the material covered in this section was first described in the ground breaking paper by Belavin, Polyakov and Zamalodchikov, “Infinite Conformal Symmetry in Two-Dimensional Quantum Field Theory”, Nucl. Phys. B241 (1984). The application to string theory was explained by Friedan, Martinec and Shenker in “Conformal Invariance, Supersymmetry and String Theory”, Nucl. Phys. B271 (1986). The canonical reference for learning conformal field theory is the excellent review by Ginsparg. A link can be found on the course webpage.

Of course, we can alternate between thinking of theories as defined on fixed or fluctuating backgrounds. Any theory of 2d gravity which enjoys both diffeomorphism and Weyl invariance will reduce to a conformally invariant theory when the background metric is fixed. Similarly, any conformally invariant theory can be coupled to 2d gravity where it will give rise to a classical theory which enjoys both diffeomorphism and Weyl invariance. Notice the caveat “classical”! In some sense, the whole point of this course is to understand when this last statement also holds at the quantum level.

Even though conformal field theories are a subset of quantum field theories, the language used to describe them is a little different. This is partly out of necessity. Invariance under the transformation (4.1) can only hold if the theory has no preferred length scale. But this means that there can be nothing in the theory like a mass or a Compton wavelength. In other words, conformal field theories only support massless excitations. The questions that we ask are not those of particles and S-matrices. Instead we will be concerned with correlation functions and the behaviour of different operators under conformal transformations.

4.0.1 Euclidean Space Although we’re ultimately interested in Minkowski signature worldsheets, it will be much simpler and elegant if we work instead with Euclidean worldsheets. There’s no funny business here — everything we do could also be formulated in Minkowski space. The Euclidean worldsheet coordinates are (σ^1, σ^2) = (σ^1, iσ^0) and it will prove useful to form the complex coordinates, z = σ^1 + iσ^2 and z̄ = σ^1 − iσ^2 which are the Euclidean analogue of the lightcone coordinates. Motivated by this analogy, it is common to refer to holomorphic functions as “left-moving” and anti-holomorphic functions as “right-moving”.

The holomorphic derivatives are ∂_z ≡ ∂_1 = (∂_1 − i∂_2)/2 and ∂_{z̄} ≡ ∂̄ = (∂_1 + i∂_2)/2 These obey ∂_z z = ∂_{z̄} z̄ = 1 and ∂_z z̄ = ∂_{z̄} z = 0. We will usually work in flat Euclidean space, with metric ds^2 = (dσ^1)^2 + (dσ^2)^2 = dz dz̄ (4.2)

In components, this flat metric reads g_{zz} = g_{z̄z̄} = 0 and g_{zz̄} = 1/2 With this convention, the measure factor is dz dz̄ = 2 dσ^1 dσ^2. We define the delta-function such that ∫ d^2z δ(z, z̄) = 1. Notice that because we also have ∫ d^2σ δ(σ) = 1, this means that there is a factor of 2 difference between the two delta functions. Vectors naturally have their indices up: v^z = (v^1 + iv^2) and v^{z̄} = (v^1 − iv^2). When indices are down, the vectors are v_z = (v^1 − iv^2)/2 and v_{z̄} = (v^1 + iv^2)/2.

4.0.2 The Holomorphy of Conformal Transformations In the complex Euclidean coordinates z and z̄, conformal transformations of flat space are simple: they are any holomorphic change of coordinates, z → z' = f(z) and z̄ → z̄' = f̄(z̄)

Under this transformation, ds^2 = dz dz̄ → |df/dz|^2 dz dz̄, which indeed takes the form (4.1). Note that we have an infinite number of conformal transformations — in fact, a whole functions worth f(z). This is special to conformal field theories in two dimensions. In higher dimensions, the space of conformal transformations is a finite dimensional group. For theories defined on R^{p,q}, the conformal group is SO(p+1, q+1) when p+q > 2.

A couple of particularly simple and important examples of 2d conformal transformations are • z → z' = z + a (translation)

• z → z' = λz (dilation)

• z → z' = e^{iθ} z (rotation)

• z → z' = 1/z (special conformal transformation)

+a: This is a translation.

• z → ζz: This is a rotation for |ζ| = 1 and a scale transformation (also known as a dilatation) for real ζ (cid:54)= 1.

For many purposes, it’s simplest to treat z and z¯ as independent variables. In doing this, we’re really extending the worldsheet from R2 to C2. This will allow us to make use of various theorems from complex methods. However, at the end of the day we should remember that we’re really sitting on the real slice R2 ⊂ C2 defined by z¯= z(cid:63).

## 4.1 Classical Aspects

We start by deriving some properties of classical theories which are invariant under conformal transformations (4.1).

– 63 – 4.1.1 The Stress-Energy Tensor One of the most important objects in any field theory is the stress-energy tensor (also known as the energy-momentum tensor). This is defined in the usual way as the matrix of conserved currents which arise from translational invariance, δσα = (cid:15)α .

In flat spacetime, a translation is a special case of a conformal transformation.

There’s a cute way to derive the stress-energy tensor in any theory. Suppose for the momentthatweareinflatspaceg = η . Recallthatwecanusuallyderiveconserved αβ αβ currents by promoting the constant parameter (cid:15) that appears in the symmetry to a function of the spacetime coordinates. The change in the action must then be of the form, (cid:90)

δS = d2σ Jα∂ (cid:15) (4.3)

forsomefunctionofthefields, Jα. Thisensuresthatthevariationoftheactionvanishes when (cid:15) is constant, which is of course the definition of a symmetry. But when the equations of motion are satisfied, we must have δS = 0 for all variations (cid:15)(σ), not just constant (cid:15). This means that when the equations of motion are obeyed, Jα must satisfy ∂ Jα = 0 The function Jα is our conserved current.

Let’s see how this works for translational invariance. If we promote (cid:15) to a function of the worldsheet variables, the change of the action must be of the form (4.3). But what is Jα? At this point we do the cute thing. Consider the same theory, but now coupled to a dynamical background metric g (σ). In other words, coupled to gravity.

αβ Then we could view the transformation δσα = (cid:15)α(σ)

as a diffeomorphism and we know that the theory is invariant as long as we make the corresponding change to the metric δg = ∂ (cid:15) +∂ (cid:15) .

αβ α β β α This means that if we just make the transformation of the coordinates in our original theory, then the change in the action must be the opposite of what we get if we just – 64 – transform the metric. (Because doing both together leaves the action invariant). So we have (cid:90) (cid:90)

∂S ∂S δS = − d2σ δg = −2 d2σ ∂ (cid:15)

αβ α β ∂g ∂g αβ αβ Note that ∂S/∂g in this expression is really a functional derivatives but we won’t be αβ carefulaboutusingnotationtoindicatethis. Wenowhavetheconservedcurrentarising from translational invariance. We will add a normalization constant which is standard in string theory (although not necessarily in other areas) and define the stress-energy tensor to be 4π ∂S T = −√ (4.4)

αβ g ∂gαβ If we have a flat worldsheet, we evaluate T on g = δ and the resulting expression αβ αβ αβ obeys ∂αT = 0. If we’re working on a curved worldsheet, then the energy-momentum αβ tensor is covariantly conserved, ∇αT = 0.

αβ The Stress-Energy Tensor is Traceless In conformal theories, T has a very important property: its trace vanishes. To see αβ this, let’s vary the action with respect to a scale transformation which is a special case of a conformal transformation, δg = (cid:15)g (4.5)

αβ αβ Then we have (cid:90) (cid:90)

∂S 1 √ δS = d2σ δg = − d2σ g(cid:15)Tα ∂g αβ 4π α αβ But this must vanish in a conformal theory because scaling transformations are a symmetry. So Tα = 0 This is the key feature of a conformal field theory in any dimension. Many theories have this feature at the classical level, including Maxwell theory and Yang-Mills theory in four-dimensions. However, it is much harder to preserve at the quantum level. (The weight of the world rests on the fact that Yang-Mills theory fails to be conformal at the quantum level). Technically the difficulty arises due to the need to introduce a scale when regulating the theories. Here we will be interested in two-dimensional theories – 65 – which succeed in preserving the conformal symmetry at the quantum level.

Looking Ahead: Even when the conformal invariance survives in a 2d quantum theory, the vanishing trace Tα = 0 will only turn out to hold in flat space. We will derive this result in section 4.4.2.

The Stress-Tensor in Complex Coordinates In complex coordinates, z = σ1 +iσ2, the vanishing of the trace Tα = 0 becomes T = 0 zz¯ Meanwhile, the conservation equation ∂ Tαβ = 0 becomes ∂Tzz = ∂ ¯ Tz¯z¯ = 0. Or, lowering the indices on T, ∂T = 0 and ∂T = 0 zz z¯z¯ In other words, T = T (z) is a holomorphic function while T = T (z¯) is an anti- zz zz z¯z¯ z¯z¯ holomorphic function. We will often use the simplified notation T (z) ≡ T(z and T(z̄) ≡ T(z̄)

zz z̄z̄

4.1.2 Noether Currents The stress-energy tensor Tαβ provides the Noether currents for translations. What are the currents associated to the other conformal transformations? Consider the infinitesimal change, z' = z + ε(z) , z̄' = z̄ + ε̄(z̄)

where, making contact with the two examples above, constant ε corresponds to a translation while ε(z) ∼ z corresponds to a rotation and dilatation. To compute the current, we’ll use the same trick that we saw before: we promote the parameter ε to depend on the worldsheet coordinates. But it’s already a function of half of the worldsheet coordinates, so this now means ε(z) → ε(z,z̄). Then we can compute the change in the action, again using the fact that we can make a compensating change in the metric, δS = −∫ d²σ δgαβ ∂S/∂gαβ = ∫ d²σ Tαβ (∂αδσβ) / 2π = ∫ d²z [Tzz (∂zδz) + Tz̄z̄ (∂z̄δz̄)] / 2π = ∫ d²z [Tzz ∂z ε + Tz̄z̄ ∂z̄ ε̄] / 2π (4.6)

Firstly note that if ε is holomorphic and ε̄ is anti-holomorphic, then we immediately have δS = 0. This, of course, is the statement that we have a symmetry on our hands. (You may wonder where in the above derivation we used the fact that the theory was conformal. It lies in the transition to the third line where we needed Tzz̄ = 0).

At this stage, let’s use the trick of treating z and z̄ as independent variables. We look at separate currents that come from shifts in z and shifts z̄. Let’s first look at the symmetry δz = ε(z) , δz̄ = 0 We can read off the conserved current from (4.6) by using the standard trick of letting the small parameter depend on position. Since ε(z) already depends on position, this means promoting ε → ε(z)f(z̄) for some function f and then looking at the ∂f terms in (4.6). This gives us the current Jz = 0 and Jz̄ = Tzz(z)ε(z) ≡ T(z)ε(z) (4.7)

Importantly, we find that the current itself is also holomorphic. We can check that this is indeed a conserved current: it should satisfy ∂α Jα = ∂z Jz + ∂z̄ Jz̄ = 0. But in fact it does so with room to spare: it satisfies the much stronger condition ∂z̄ Jz̄ = 0.

Similarly, we can look at transformations δz̄ = ε̄(z̄) with δz = 0. We get the anti-holomorphic current Jz̄ = Tz̄z̄(z̄)ε̄(z̄) and Jz = 0 (4.8)

4.1.3 An Example: The Free Scalar Field Let’s illustrate some of these ideas about classical conformal theories with the free scalar field, S = ∫ d²σ ∂α X ∂α X / 4πα' Notice that there’s no overall minus sign, in contrast to our earlier action (1.30). That’s because we’re now working with a Euclidean worldsheet metric. The theory of a free scalar field is, of course, dead easy. We can compute anything we like in this theory. Nonetheless, it will still exhibit enough structure to provide an example of all the abstract concepts that we will come across in CFT. For this reason, the free scalar field will prove a good companion throughout this part of the lectures.

Firstly, let’s just check that this free scalar field is actually conformal. In particular, we can look at rescaling σα → λσα. If we view this in the sense of an active transformation, the coordinates remain fixed but the value of the field at point σ gets moved to point λσ. This means, X(σ) → X(λ⁻¹σ) and ∂X(σ)/∂σα → ∂X(λ⁻¹σ)/∂σα = (1/λ) ∂X(σ̃)/∂σ̃ where we’ve defined σ̃ = λ⁻¹σ. The factor of λ⁻² coming from the two derivatives in the Lagrangian then cancels the Jacobian factor from the measure d²σ = λ²d²σ̃, leaving the action invariant. Note that any polynomial interaction term for X would break conformal invariance.

The stress-energy tensor for this theory is defined using (4.4), Tαβ = −(1/α') (∂α X ∂β X − (1/2) δαβ (∂X)²) , (4.9)

which indeed satisfies Tαα = 0 as it should. The stress-energy tensor looks much simpler in complex coordinates. It is simple to check that Tzz̄ = 0 while Tzz = −(1/α') ∂X ∂X and Tz̄z̄ = −(1/α') ∂̄X ∂̄X The equation of motion for X is ∂∂̄X = 0. The general classical solution decomposes as, X(z,z̄) = X(z) + X(z̄)

When evaluated on this solution, Tzz and Tz̄z̄ become holomorphic and anti-holomorphic functions respectively.

## 4.2 Quantum Aspects

So far our discussion has been entirely classical. We now turn to the quantum theory. The first concept that we want to discuss is actually a feature of any quantum field theory. But it really comes into its own in the context of CFT: it is the operator product expansion.

4.2.1 Operator Product Expansion Let’s first describe what we mean by a local operator in a CFT. We will also refer to these objects as fields. There is a slight difference in terminology between CFTs and more general quantum field theories. Usually in quantum field theory, one reserves the term “field” for the objects φ which sit in the action and are integrated over in the path integral. In contrast, in CFT the term “fi "field" refers to any local expression that we can write down. This includes φ, but also includes derivatives ∂nφ or composite operators such as eiφ. All of these are thought of as different fields in a CFT. It should be clear from this that the set of all "fields" in a CFT is always infinite even though, if you were used to working with quantum field theory, you would talk about only a finite number of fundamental objects φ. Obviously, this is nothing to be scared about. It's just a change of language: it doesn't mean that our theory got harder.

We now define the operator product expansion (OPE). It is a statement about what happens as local operators approach each other. The idea is that two local operators inserted at nearby points can be closely approximated by a string of operators at one of these points. Let's denote all the local operators of the CFT by O_i, where i runs over the set of all operators. Then the OPE is O_i(z,z¯)O_j(w,w¯) = ∑_k C_ij^k(z −w,z¯−w¯)O_k(w,w¯) (4.10)

Here C_ij^k(z − w,z¯− w¯) are a set of functions which, on grounds of translational invariance, depend only on the separation between the two operators. We will write a lot of operator equations of the form (4.10) and it's important to clarify exactly what they mean: they are always to be understood as statements which hold as operator insertions inside time-ordered correlation functions, ⟨O_i(z,z¯)O_j(w,w¯)...⟩ = ∑_k C_ij^k(z −w,z¯−w¯) ⟨O_k(w,w¯)...⟩ where the ... can be any other operator insertions that we choose. Obviously it would be tedious to continually write ⟨...⟩. So we don't. But it's always implicitly there.

There are further caveats about the OPE that are worth stressing • The correlation functions are always assumed to be time-ordered. (Or something similar that we will discuss in Section 4.5.1). This means that as far as the OPE is concerned, everything commutes since the ordering of operators is determined inside the correlation function anyway. So we must have O_i(z,z¯)O_j(w,w¯) = O_j(w,w¯)O_i(z,z¯). (There is a caveat here: if the operators are Grassmann objects, then they pick up an extra minus sign when commuted, even inside time-ordered products).

• The other operator insertions in the correlation function (denoted ... above) are arbitrary. Except they should be at a distance large compared to |z−w|. It turns out — rather remarkably — that in a CFT the OPEs are exact statements and have a radius of convergence equal to the distance to the nearest other insertion. We will return to this in Section 4.6. The radius of convergence is denoted in the figure by the dotted line.

• The OPEs have singular behaviour as z → w. In fact, this singular behaviour will really be the only thing we care about! It will turn out to contain the same information as commutation relations, as well as telling us how operators transform under symmetries. Indeed, in many equations we will simply write the singular terms in the OPE and denote the non-singular terms as +....

4.2.2 Ward Identities The spirit of Noether's theorem in quantum field theories is captured by operator equations known as Ward Identities. Here we derive the Ward identities associated to conformal invariance. We start by considering a general theory with a symmetry. Later we will restrict to conformal symmetries.

Games with Path Integrals We'll take this opportunity to get comfortable with some basic techniques using path integrals. Schematically, the path integral takes the form Z = ∫ Dφ e^{-S[φ]} where φ collectively denote all the fields (in the path integral sense...not the CFT sense!). A symmetry of the quantum theory is such that an infinitesimal transformation φ' = φ+εδφ leaves both the action and the measure invariant, S[φ'] = S[φ] and Dφ' = Dφ (In fact, we only really need the combination Dφe^{-S[φ]} to be invariant but this subtlety won't matter in this course). We use the same trick that we employed earlier in the classical theory and promote ε → ε(σ). Then, typically, neither the action nor the measure are invariant but, to leading order in ε, the change has to be proportional to ∂ε. We have Z → ∫ Dφ' exp(−S[φ'])

= ∫ Dφ exp(−S[φ]− ∫ J^α ∂_α ε / 2π)

= ∫ Dφ e^{-S[φ]} (1− ∫ J^α ∂_α ε / 2π)

where the factor of 1/2π is merely a convention and is shorthand for ∫ d^2σ √g. Notice that the current J^α may now also have contributions from the measure transformation as well as the action.

Now comes the clever step. Although the integrand has changed, the actual value of the partition function can't have changed at all. After all, we just redefined a dummy integration variable φ. So the expression above must be equal to the original Z. Or, in other words, ∫ Dφe^{-S[φ]} ∫ J^α ∂_α ε = 0 Moreover, this must hold for any ε(σ).

old for all ε. This gives us the quantum version of Noether’s theorem: the vacuum expectation value of the divergence of the current vanishes: ⟨∂ Jα⟩ = 0 .

We can repeat these tricks of this sort to derive some stronger statements. Let’s see what happens when we have other insertions in the path integral. The time-ordered correlation function is given by ⟨O1(σ1)...On(σn)⟩ = ∫ Dφ e^{-S[φ]} O1(σ1)...On(σn)

We can think of these as operators inserted at particular points on the plane as shown in the figure. As we described above, the operators O are any general expressions that we can form from the φ fields. Under the symmetry of interest, the operator will change in some way, say Oi → Oi + εδOi We once again promote ε → ε(σ). As our first pass, let’s pick a choice of ε(σ) which only has support away from the operator insertions as shown in the Figure 20. Then, δOi(σi) = 0 and the above derivation goes through in exactly the same way to give ⟨∂ Jα(σ)O1(σ1)...On(σn)⟩ = 0 for σ ≠ σi Because this holds for any operator insertions away from σ, from the discussion in Section 4.2.1 we are entitled to write the operator equation ∂ Jα = 0 But what if there are operator insertions that lie at the same point as Jα? In other words, what happens as σ approaches one of the insertion points? The resulting formulae are called Ward identities. To derive these, let’s take ε(σ) to have support in some region that includes the point σ, but not the other points as shown in Figure 21. The simplest choice is just to take ε(σ) to be constant inside the shaded region and zero outside. Now using the same procedure as before, we find that the original correlation function is equal to, ∫ Dφ e^{-S[φ]} (1 - 1/(2π) ∫ Jα ∂α ε) (O1 + εδO1) O2...On Working to leading order in ε, this gives - 1/(2π) ∫ ∂α ⟨Jα(σ)O1(σ1)...⟩ = ⟨δO1(σ1)...⟩ (4.11)

where the integral on the left-hand-side is only over the region of non-zero ε. This is the Ward Identity.

Ward Identities for Conformal Transformations Ward identities (4.11) hold for any symmetries. Let’s now see what they give when applied to conformal transformations. There are two further steps needed in the derivation. The first simply comes from the fact that we’re working in two dimensions and we can use Stokes’ theorem to convert the integral on the left-hand-side of (4.11) to a line integral around the boundary. Let n̂α be the unit vector normal to the boundary. For any vector Jα, we have ∫ ∂α Jα = ∮ Jα n̂α = ∮ (J1 dσ2 - J2 dσ1) = -i ∮ (Jz dz - Jz̄ dz̄)

where we have written the expression both in Cartesian coordinates σα and complex coordinates on the plane. As described in Section 4.0.1, the complex components of the vector with indices down are defined as Jz = 1/2 (J1 - iJ2) and Jz̄ = 1/2 (J1 + iJ2). So, applying this to the Ward identity (4.11), we find for two dimensional theories i/(2π) ∮ dz ⟨Jz(z,z̄)O1(σ1)...⟩ - i/(2π) ∮ dz̄ ⟨Jz̄(z,z̄)O1(σ1)...⟩ = ⟨δO1(σ1)...⟩ So far our derivation holds for any conserved current J in two dimensions. At this stage we specialize to the currents that arise from conformal transformations (4.7) and (4.8). Here something nice happens because Jz is holomorphic while Jz̄ is anti-holomorphic. This means that the contour integral simply picks up the residue, i/(2π) ∮ dz Jz(z) O1(σ1) = -Res[Jz O1]

where this means the residue in the OPE between the two operators, Jz(z) O1(w,w̄) = ... + Res[Jz O1(w,w̄)]/(z - w) + ...

So we find a rather nice way of writing the Ward identities for conformal transformations. If we again view z and z̄ as independent variables, the Ward identities split into two pieces. From the change δz = ε(z), we get δO1(σ1) = -Res[Jz(z) O1(σ1)] = -Res[ε(z) T(z) O1(σ1)] (4.12)

where, in the second equality, we have used the expression for the conformal current (4.7). Meanwhile, from the change δz̄= ε̄(z̄), we have δO1(σ1) = -Res[Jz̄(z̄) O1(σ1)] = -Res[ε̄(z̄) T̄(z̄) O1(σ1)]

where the minus sign comes from the fact that the dz̄ boundary integral is taken in the opposite direction.

This result means that if we know the OPE between an operator and the stress-tensors T(z) and T̄(z̄), then we immediately know how the operator transforms under conformal symmetry. Or, standing this on its head, if we know how an operator transforms then we know at least some part of its OPE with T and T̄.

4.2.3 Primary Operators The Ward identity allows us to start piecing together some OPEs by looking at how operators transform under conformal symmetries. Although we don’t yet know the action of general conformal symmetries, we can start to make progress by looking at the two simplest examples.

Translations: If δz = ε, a constant, then all operators transform as O(z − ε) = O(z) − ε∂O(z) + ... The Noether current for translations is the stress-energy tensor T. The Ward identity in the form (4.12) tells us that the OPE of T with any operator O must be of the form, T(z)O(w,w̄) = ... + ∂O(w,w̄)/(z − w) + ... (4.13)

Similarly, the OPE with T̄ is T̄(z̄)O(w,w̄) = ... + ∂̄O(w,w̄)/(z̄ − w̄) + ... (4.14)

Rotations and Scaling: The transformation z → z + εz and z̄ → z̄ + ε̄z̄ (4.15)

describes rotation for ε purely imaginary and scaling (dilatation) for ε real. Not all operators have good transformation properties under these actions. This is entirely analogous to the statement in quantum mechanics that not all states transform nicely under the Hamiltonian H and angular momentum operator L. However, in quantum mechanics we know that the eigenstates of H and L can be chosen as a basis of the Hilbert space provided, of course, that [H,L] = 0.

The same statement holds for operators in a CFT: we can choose a basis of local operators that have good transformation properties under rotations and dilatations. In fact, we will see in Section 4.6 that the statement about local operators actually follows from the statement about states.

Definition: An operator O is said to have weight (h, h̄) if, under δz = εz and δz̄ = ε̄z̄, O transforms as δO = −ε(hO + z∂O) − ε̄(h̄O + z̄∂̄O) (4.16)

The terms ∂O in this expression would be there for any operator. They simply come from expanding O(z − εz, z̄ − ε̄z̄). The terms hO and h̄O are special to operators which are eigenstates of dilatations and rotations. Some comments: • Both h and h̄ are real numbers. In a unitary CFT, all operators have h, h̄ ≥ 0. We will prove this is Section 4.5.4.

• The weights are not as unfamiliar as they appear. They simply tell us how operators transform under rotations and scalings. But we already have names for these concepts from undergraduate days. The eigenvalue under rotation is usually called the spin, s, and is given in terms of the weights as s = h − h̄. Meanwhile, the scaling dimension ∆ of an operator is ∆ = h + h̄.

• To motivate these definitions, it’s worth recalling how rotations and scale transformations act on the underlying coordinates. Rotations are implemented by the operator L = −i(σ₁∂₂ − σ₂∂₁) = z∂ − z̄∂̄ while the dilation operator D which gives rise to scalings is D = σα∂α = z∂ + z̄∂̄.

• The scaling dimension is nothing more than the familiar “dimension” that we usually associate to fields and operators by dimensional analysis. For example, worldsheet derivatives always increase the dimension of an operator by one: ∆[∂] = +1. The tricky part is that the naive dimension that fields have in the classical theory is not necessarily the same as the dimension in the quantum theory.

Let’s compare the transformation law (4.16) with the Ward identity (4.12). The Noether current arising from rotations and scaling δz = εz was given in (4.7): it is J(z) = zT(z). This means that the residue of the J O OPE will determine the 1/z² term in the T O OPE. Similar arguments hold, of course, for δz̄ = ε̄z̄ and T̄. So, the upshot of this is that, for an operator O with weight (h, h̄), the OPE with T and T̄ takes the form T(z)O(w,w̄) = ... + h O(w,w̄)/(z − w)² + ∂O(w,w̄)/(z − w) + ...

T̄(z̄)O(w,w̄) = ... + h̄ O(w,w̄)/(z̄ − w̄)² + ∂̄O(w,w̄)/(z̄ − w̄) + ...

Primary Operators A primary operator is one whose OPE with T and T̄ truncates at order (z − w)⁻² or order (z̄ − w̄)⁻² respectively. There are no higher singularities: T(z)O(w,w̄) = h O(w,w̄)/(z − w)² + ∂O(w,w̄)/(z − w) + non-singular T̄(z̄)O(w,w̄) = h̄ O(w,w̄)/(z̄ − w̄)² + ∂̄O(w,w̄)/(z̄ − w̄) + non-singular Since we now know all singularities in the T O OPE, we can reconstruct the transformation under all conformal transformations. The importance of primary operators is that they have particularly simple transformation properties. Focussing on δz = ε(z), we have δO(w,w̄) = −Res[ε(z)T(z)O(w,w̄)]

= −Res[ε(z) (h O(w,w̄)/(z − w)² + ∂O(w,w̄)/(z − w) + ...)]

We want to look at smooth conformal transformations and so require that ε(z) itself has no singularities at z = w. We can then Taylor expand ε(z) = ε(w) + ε'(w)(z − w) + ... We learn that the infinitesimal change of a primary operator under a general conformal transformation δz = ε(z) is δO(w,w̄) = −h ε'(w) O(w,w̄) − ε(w) ∂O(w,w̄) (4.17)

There is a similar expression for the anti-holomorphic transformations δz̄ = ε̄(z̄). Equation (4.17) holds for infinitesimal conformal transformations. It is a simple matter to integrate up to find how primary operators change under a finite conformal transformation, z → z̃(z) and z̄ → z̃̄(z̄)

The general transformation of a primary operator is given by O(z,z̄) → Õ(z̃,z̃̄) = O(z,z̄) (∂z̃/∂z)^{-h} (∂z̃̄/∂z̄)^{-h̃} (4.18)

It will turn out that one of the main objects of interest in a CFT is the spectrum of weights (h,h̃) of primary fields. This will be equivalent to computing the particle mass spectrum in a quantum field theory. In the context of statistical mechanics, the weights of primary operators are the critical exponents.

## 4.3 An Example: The Free Scalar Field

Let’s look at how all of this works for the free scalar field. We’ll start by familiarizing ourselves with some techniques using the path integral. The action is, S = ∫ d²σ (1/(4πα')) ∂_α X ∂^α X (4.19)

The classical equation of motion is ∂²X = 0. Let’s start by seeing how to derive the analogous statement in the quantum theory using the path integral. The key fact that we’ll need is that the integral of a total derivative vanishes in the path integral just as it does in an ordinary integral. From this we have, 0 = ∫ DX e^{-S} = ∫ DX e^{-S} (1/(2πα')) ∂²X(σ)

But this is nothing more than the Ehrenfest theorem which states that expectation values of operators obey the classical equations of motion, ⟨∂²X(σ)⟩ = 0

4.3.1 The Propagator The next thing that we want to do is compute the propagator for X. We could do this using canonical quantization, but it will be useful to again see how it works using the path integral. This time we look at, 0 = ∫ DX e^{-S} X(σ') = ∫ DX e^{-S} (1/(2πα')) [∂²X(σ) X(σ') + δ(σ - σ')]

So this time we learn that ⟨∂²X(σ) X(σ')⟩ = -2πα' δ(σ - σ') (4.20)

Note that if we’d computed this in the canonical approach, we would have found the same answer: the δ-function arises in this calculation because all correlation functions are time-ordered.

We can now treat (4.20) as a differential equation for the propagator ⟨X(σ) X(σ')⟩. To solve this equation, we need the following standard result ∂² ln(σ - σ')² = 4π δ(σ - σ') (4.21)

Since this is important, let’s just quickly check that it’s true. It’s a simple application of Stokes’ theorem. Set σ' = 0 and integrate over d²σ. We obviously get 4π from the right-hand-side. The left-hand-side gives ∫ d²σ ∂² ln(σ₁² + σ₂²) = ∫ d²σ ∂_α (2σ^α / (σ₁² + σ₂²)) = ∮ (2σ₁ dσ₂ - 2σ₂ dσ₁) / (σ₁² + σ₂²)

Switching to polar coordinates σ₁ + iσ₂ = r e^{iθ}, we can rewrite this expression as ∮ (2 dθ) = 4π confirming (4.21). Applying this result to our equation (4.20), we get the propagator of a free scalar in two-dimensions, ⟨X(σ) X(σ')⟩ = - (α'/2) ln(σ - σ')² The propagator has a singularity as σ → σ'. This is an ultra-violet divergence and is common to all field theories. It also has a singularity as |σ - σ'| → ∞. This is telling us something important that we will mention in Section 4.3.2.

Finally, we could repeat our trick of looking at total derivatives in the path integral, now with other operator insertions O₁(σ₁),...,Oₙ(σₙ) in the path integral. As long as σ,σ' ≠ σᵢ, then the whole analysis goes through as before. But this is exactly our criterion to write the operator product equation, X(σ) X(σ') = - (α'/2) ln(σ - σ')² + ... (4.22)

We can also write this in complex coordinates. The classical equation of motion ∂∂̄X = 0 allows us to split the operator X into left-moving and right-moving pieces, X(z,z̄) = X(z) + X(z̄)

We’ll focus just on the left-moving piece. This has the operator product expansion, X(z) X(w) = - (α'/2) ln(z - w) + ...

The logarithm means that X(z) doesn’t have any nice properties under the conformal transformations. For this reason, the “fundamental field” X is not really the object of interest in this theory! However, we can look at the derivative of X. This has a rather nice looking OPE, ∂X(z) ∂X(w) = - (α'/2) * 1/(z - w)² + non-singular (4.23)

4.3.2 An Aside: No Goldstone Bosons in Two Dimensions The infrared divergence in the propagator has an important physical implication. Let’s start by pointing out one of the big differences between quantum mechanics and quantum field theory in d = 3 + 1 dimensions. Since the language used to describe these two theories is rather different, you may not even be aware that this difference exists.

Consider the quantum mechanics of a particle on a line. This is a d = 0 + 1 dimensional theory of a free scalar field X. Let’s prepare the particle in some localized state – say a Gaussian wavefunction Ψ(X) ∼ exp(−X²/L²). What then happens? The wavefunction starts to spread out. And the spreading doesn’t stop. In fact, the would-be ground state of the system is a uniform wavefunction of infinite width, which isn’t a state in the Hilbert space because it is non-normalizable. Let’s now compare this to the situation of a free scalar field X in a d = 3 + 1 dimensional field theory. Now we think of this as a scalar without potential. The physics is very different: the theory has an infinite number of ground states, determined by the expectation value ⟨X⟩. Small fluctuations around this vacuum are massless: they are Goldstone bosons for broken translational invariance X → X + c.

We see that the physics is very different in field theories in d = 0+1 and d = 3+1 dimensions. The wavefunction spreads along flat directions in quantum mechanics, but not in higher dimensional field theories. But what happens in d = 1+1 and d = 2+1 dimensions? It turns out that field theories in d = 1 + 1 dimensions are more like quantum mechanics: the wavefunction spreads. Theories in d = 2+1 dimensions and higher exhibit the opposite behaviour: they have Goldstone bosons. The place to see this is the propagator. In d spacetime dimensions, it takes the form ⟨X(r)X(0)⟩ ∼ { 1/r^{d−2}  d ≠ 2 ln r      d = 2 which diverges at large r only for d = 1 and d = 2. If we perturb the vacuum slightly by inserting the operator X(0), this correlation function tells us how this perturbation falls off with distance. The infra-red divergence in low dimensions is telling us that the wavefunction wants to spread.

The spreading of the wavefunction in low dimensions means that there is no spontaneous symmetry breaking and no Goldstone bosons. It is usually referred to as the Coleman-Mermin-Wagner theorem. Note, however, that it certainly doesn’t prohibit massless excitations in two dimensions: it only prohibits Goldstone-like massless excitations.

4.3.3 The Stress-Energy Tensor and Primary Operators

We want to compute the OPE of T with other operators. Firstly, what is T? We computed it in the classical theory in (4.9). It is, T = − (1/α′) ∂X ∂X (4.24)

But we need to be careful about what this means in the quantum theory. It involves the product of two operators defined at the same point and this is bound to mean divergences if we just treat it naively. In canonical quantization, we would be tempted to normal order by putting all annihilation operators to the right. This guarantees that the vacuum has zero energy. Here we do something that is basically equivalent, but without reference to creation and annihilation operators. We write T = − (1/α′) : ∂X ∂X : ≡ − (1/α′) lim_{z→w} (∂X(z) ∂X(w) − ⟨∂X(z) ∂X(w)⟩) (4.25)

which, by construction, has ⟨T⟩ = 0.

With this definition of T, let’s start to compute the OPEs to determine the primary fields in the theory.

Claim 1: ∂X is a primary field with weight h = 1 and h̃ = 0.

Proof: We need to figure out how to take products of normal ordered operators T(z) ∂X(w) = − (1/α′) : ∂X(z) ∂X(z) : ∂X(w)

The operators on the left-hand side are time-ordered (because all operator expressions of this type are taken to live inside time-ordered correlation functions). In contrast, the right-hand side is a product of normal-ordered operators. But we know how to change normal ordered products into time ordered products: this is the content of Wick’s theorem. Although we have defined normal ordering in (4.25) without reference to creation and annihilation operators, Wick’s theorem still holds. We must sum over all possible contractions of pairs of operators, where the term “contraction” means that we replace the pair by the propagator, ⟨∂X(z) ∂X(w)⟩ = − α′ / (2 (z − w)^2)

Using this, we have T(z) ∂X(w) = − (1/α′) [ ∂X(z) (− α′ / (2 (z − w)^2)) + non-singular ]

Here the “non-singular” piece includes the totally normal ordered term : T(z) ∂X(w) :. It is only the singular part that interests us. Continuing, we have T(z) ∂X(w) = ∂X(w) / (z − w)^2 + ... = ∂X(w) / (z − w)^2 + ∂^2 X(w) / (z − w) + ...

This is indeed the OPE for a primary operator of weight h = 1. ∎

Note that higher derivatives ∂^n X are not primary for n > 1. For example, ∂^2 X has weight (h, h̃) = (2,0), but is not a primary operator, as we see from the OPE, T(z) ∂^2 X(w) = ∂_w [ ∂X(w) / (z − w)^2 ] + ... = 2 ∂X(w) / (z − w)^3 + 2 ∂^2 X(w) / (z − w)^2 + ...

The fact that the field ∂^n X has weight (h, h̃) = (n,0) fits our natural intuition: each derivative provides spin s = 1 and dimension Δ = 1, while the field X does not appear to be contributing, presumably reflecting the fact that it has naive, classical dimension zero. However, in the quantum theory, it is not correct to say that X has vanishing dimension: it has an ill-defined dimension due to the logarithmic behaviour of its OPE (4.22). This is responsible for the following, more surprising, result

Claim 2: The field : e^{ikX} : is primary with weight h = h̃ = α′ k^2 / 4.

This result is not what we would guess from the classical theory^5. Indeed, it’s obvious that it has a quantum origin because the weight is proportional to α′, which ch sits outside the action in the same place that (cid:126) would (if we hadn’t set it to one). Note also that this means that the spectrum of the free scalar field is continuous. This is related to the factthattherangeofX isnon-compact. Generally, CFTswillhaveadiscretespectrum.

Proof: Let’s first compute the OPE with ∂X. We have (cid:88) ∞ (ik)n ∂X(z) : eikX(w) : = ∂X(z) : X(w)n : n!

n=0 (cid:88) ∞ (ik)n (cid:18) α(cid:48) 1 (cid:19)

= : X(w)n−1 : − +...

(n−1)! 2 z −w n=1 iα(cid:48)k : eikX(w) : = − +... (4.26)

2 z −w 5We could, however, guess it with a little knowledge of renormalisation. Indeed, we previously derived this result in the lectures on Statistical Field Theory where we computed RG flows in the Sine-Gordon model; see Section 4.4.3 of those lectures.

– 81 – From this, we can compute the OPE with T.

T(z) : eikX(w) : = − : ∂X(z)∂X(z) : : eikX(w) : α(cid:48)

α(cid:48)k2 : eikX(w) : : ∂X(z)eikX(w) : = +ik +...

4 (z −w)2 z −w where the first term comes from two contractions, while the second term comes from a single contraction. Replacing ∂ by ∂ in the final term we get z w α(cid:48)k2 : eikX(w) : ∂ : eikX(w) : T(z) : eikX(w) := + w +... (4.27)

4 (z −w)2 z −w showing that : eikX(w) : is indeed primary. We will encounter this operator frequently later, but will choose to simplify notation and drop the normal ordering colons. Normal ordering will just be assumed from now on. (cid:3).

Finally, lets check to see the OPE of T with itself. This is again just an exercise in Wick contractions.

T(z)T(w) = : ∂X(z)∂X(z) : : ∂X(w)∂X(w) : α(cid:48)2 2 (cid:18) α(cid:48) 1 (cid:19)2 4 α(cid:48) : ∂X(z)∂X(w) : = − − +...

α(cid:48)2 2 (z −w)2 α(cid:48)2 2 (z −w)2 The factor of 2 in front of the first term comes from the two ways of performing two contractions; the factor of 4 in the second term comes from the number of ways of performing a single contraction. Continuing, 1/2 2T(w) 2 ∂2X(w)∂X(w)

T(z)T(w) = + − +...

(z −w)4 (z −w)2 α(cid:48) z −w 1/2 2T(w) ∂T(w)

= + + +... (4.28)

(z −w)4 (z −w)2 z −w We learn that T is not a primary operator in the theory of a single free scalar field. It is an operator of weight (h,h) = (2,0), but it fails the primary test on account of the (z −w)−4 term. In fact, this property of the stress energy tensor a general feature of all CFTs which we now explore in more detail.

## 4.4 The Central Charge

In any CFT, the most prominent example of an operator which is not primary is the stress-energy tensor itself.

– 82 – For the free scalar field, we have already seen that T is an operator of weight (h,h) = (2,0). This remains true in any CFT. The reason for this is simple: T has dimension αβ ∆ = 2 because we obtain the energy by integrating over space. It has spin s = 2 because it is a symmetric 2-tensor. But these two pieces of information are equivalent to the statement that T is has weight (2,0). Similarly, T has weight (0,2). This means that the TT OPE takes the form, 2T(w) ∂T(w)

T(z)T(w) = ...+ + +...

(z −w)2 z −w ¯¯ and similar for TT. What other terms could we have in this expansion? Since each term has dimension ∆ = 4, any operators that appear on the right-hand-side must be of the form (4.29)

(z −w)n where ∆[O ] = 4 − n. But, in a unitary CFT there are no operators with h, h < 0.

(We will prove this shortly). So the most singular term that we can have is of order (z −w)−4. Such a term must be multiplied by a constant. We write, c/2 2T(w) ∂T(w)

T(z)T(w) = + + +...

(z −w)4 (z −w)2 z −w and, similarly, ¯ ¯¯ c˜/2 2T(w¯) ∂T(w¯)

¯ ¯ T(z¯)T(w¯) = + + +...

(z¯−w¯)4 (z¯−w¯)2 z¯−w¯ The constants c and c˜are called the central charges. (Sometimes they are referred to as left-moving and right-moving central charges). They are perhaps the most important numbers characterizing the CFT. We can already get some intuition for the information contained in these two numbers. Looking back at the free scalar field (4.28) we see that it has c = c˜= 1. If we instead considered D non-interacting free scalar fields, we would get c = c˜ = D. This gives us a hint: c and c˜ are somehow measuring the number of degrees of freedom in the CFT. This is true in a deep sense! However, be warned: c is not necessarily an integer.

Before moving on, it’s worth pausing to explain why we didn’t include a (z −w)−3 term in the TT OPE. The reason is that the OPE must obey T(z)T(w) = T(w)T(z)

because, as explained previously, these operator equations are all taken to hold inside time-ordered correlation functions. So the quick answer is that a (z−w)−3 term would – 83 – not be invariant under z ↔ w. However, you may wonder how the (z − w)−1 term manages to satisfy this property. Let’s see how this works: c/2 2T(z) ∂T(z)

T(w)T(z) = + + +...

(z −w)4 (z −w)2 w−z Now we can Taylor expand T(z) = T(w)+(z−w)∂T(w)+... and ∂T(z) = ∂T(w)+....

Using this in the above expression, we find c/2 2T(w)+2(z −w)∂T(w) ∂T(w)

T(w)T(z) = + − +... = T(z)T(w)

(z −w)4 (z −w)2 z −w This trick of Taylor expanding saves the (z − w)−1 term. It wouldn’t work f or the (z − w)−3 term.

The Transformation of Energy

So T is not primary unless c = 0. And we will see shortly that all theories have c > 0. What does this mean for the transformation of T?

δT(w) = −Res[ε(z)T(z)T(w)]

= −Res (ε(z) + c/2 / (z − w)^4 + 2T(w) / (z − w)^2 + ∂T(w) / (z − w) + ...)

If ε(z) contains no singular terms, we can expand ε(z) = ε(w) + ε'(w)(z − w) + (1/2)ε''(w)(z − w)^2 + (1/6)ε'''(w)(z − w)^3 + ...

from which we find δT(w) = −ε(w)∂T(w) − 2ε'(w)T(w) − (1/12)ε'''(w) (4.30)

This is the infinitesimal version. We would like to know what becomes of T under the finite conformal transformation z → z̃(z). The answer turns out to be T(z̃) = (∂z̃/∂z)^{-2} [T(z) − (c/12) S(z̃, z)] (4.31)

where S(z̃, z) is known as the Schwarzian and is defined by S(z̃, z) = (∂^3 z̃ / ∂z^3) (∂z̃ / ∂z)^{-1} − (3/2) (∂^2 z̃ / ∂z^2)^2 (∂z̃ / ∂z)^{-2} (4.32)

It is simple to check that the Schwarzian has the right infinitesimal form to give (4.30). Its key property is that it preserves the group structure of successive conformal transformations.

4.4.1 c is for Casimir

Note that the extra term in the transformation (4.31) of T does not depend on T itself. In particular, it will be the same evaluated on all states. It only affects the constant term — or zero mode — in the energy. In other words, it is the Casimir energy of the system.

Let’s look at an example that will prove to be useful later for the string. Consider the Euclidean cylinder, parameterized by w = σ + iτ, σ ∈ [0, 2π)

We can make a conformal transformation from the cylinder to the complex plane by z = e^{-iw}

The fact that the cylinder and the plane are related by a conformal map means that if we understand a given CFT on the cylinder, then we immediately understand it on the plane. And vice-versa. Notice that constant time slices on the cylinder are mapped to circles of constant radius. The origin, z = 0, is the distant past, τ → −∞.

What becomes of T under this transformation? The Schwarzian can be easily calculated to be S(z, w) = 1/2. So we find, T_{cylinder}(w) = −z^2 T_{plane}(z) + c/24 (4.33)

Suppose that the ground state energy vanishes when the theory is defined on the plane: ⟨T_{plane}⟩ = 0. What happens on the cylinder? We want to look at the Hamiltonian, which is defined by H ≡ ∫ dσ T_{ττ} = −∫ dσ (T_{ww} + T_{w̄w̄})

The conformal transformation then tells us that the ground state energy on the cylinder is E = −2π(c + c̃)/24 (4.34)

This is indeed the (negative) Casimir energy on a cylinder. For a free scalar field, we have c = c̃ = 1 and the energy density E/2π = −1/12. This is the same result that we got in Section 2.2.2, but this time with no funny business where we throw out infinities.

An Application: The Lüscher Term

If we’re looking at a physical system, the cylinder will have a radius L. In this case, the Casimir energy is given by E = −2π(c + c̃)/24L. There is an application of this to QCD-like theories. Consider two quarks in a confining theory, separated by a distance L. If the tension of the confining flux tube is T, then the string will be stable as long as TL ≪ m, the mass of the lightest quark. The energy of the stretched string as a function of L is given by E(L) = TL + a − πc/24L + ...

Here a is an undetermined constant, while c counts the number of degrees of freedom of the QCD flux tube. (There is no analog of c̃ here because of the reflecting boundary conditions at the end of the string). If the string has no internal degrees of freedom, then c = 2 for the two transverse fluctuations. This contribution to the string energy is known as the Lüscher term.

4.4.2 The Weyl Anomaly

There is another way in which the central charge affects the stress-energy tensor. Recall that in the classical theory, one of the defining features of a CFT was the vanishing of the trace of the stress tensor, T^α_α = 0

However, things are more subtle in the quantum theory. While ⟨T^α_α⟩ indeed vanishes in flat space, it will not longer be true if we place the theory on a curved background. The purpose of this section is to show that ⟨T^α_α⟩ = −R/12 (4.35)

where R is the Ricci scalar of the 2d worldsheet. Before we derive this formula, some quick comments:

• Equation (4.35) holds for any state in the theory — not just the vacuum. This reflects the fact that it comes from regulating short distant divergences in the theory. But, at short distances all finite energy states look basically the same.

• Because ⟨T^α_α⟩ is the same for any state it must be equal to something that depends only on the background metric. This something should be local and must be dimension 2. The only candidate is the Ricci scalar R. For this reason, the formula ⟨T^α_α⟩ ∼ R is the most general possibility. The only question is : what is the coefficient. And, in particular, is it non-zero?

– 86 – • By a suitable choice of coordinates, we can always put any 2d metric in the form g = e2ωδ . In these coordinates, the Ricci scalar is given by αβ αβ R = −2e−2ω∂2ω (4.36)

which depends explicitly on the function ω. Equation (4.35) is then telling us that any conformal theory with c (cid:54)= 0 has at least one physical observable, (cid:104)Tα(cid:105), which takes different values on backgrounds related by a Weyl transformation ω.

This result is referred to as the Weyl anomaly, or sometimes as the trace anomaly.

• There is also a Weyl anomaly for conformal field theories in higher dimensions.

For example, 4d CFTs are characterized by two numbers, a and c, which appear as coefficients in the Weyl anomaly, c a (cid:104)Tµ(cid:105) = C Cρσκλ − R ˜ R ˜ρσκλ µ 4d 16π2 ρσκλ 16π2 ρσκλ where C is the Weyl tensor and R is the dual of the Riemann tensor.

• Equation (4.35) involves only the left-moving central charge c. You might wonder what’s special about the left-moving sector. The answer, of course, is nothing.

We also have c˜ (cid:104)Tα(cid:105) = − R α 12 In flat space, conformal field theories with different c and c˜are perfectly accept- able. However, if we wish these theories to be consistent in fixed, curved back- grounds, then we require c = c˜. This is an example of a gravitational anomaly.

• The fact that Weyl invariance requires c = 0 will prove crucial in string theory.

We shall return to this in Chapter 5.

We will now prove the Weyl anomaly formula (4.35). Firstly, we need to derive an intermediate formula: the T T OPE. Of course, in the classical theory we found zz¯ ww¯ that conformal invariance requires T = 0. We will now show that it’s a little more zz¯ subtle in the quantum theory.

Our starting point is the equation for energy conservation, ∂T = −∂T zz¯ zz Using this, we can express our desired OPE in terms of the familiar TT OPE, (cid:20) (cid:21)

c/2 ¯ ¯ ¯ ¯ ∂ T (z,z¯) ∂ T (w,w¯) = ∂ T (z,z¯) ∂ T (w,w¯) = ∂ ∂ +... (4.37)

z zz¯ w ww¯ z¯ zz w¯ ww z¯ w¯ (z −w)4 – 87 – Now you might think that the right-hand-side just vanishes: after all, it is an anti- holomorphic derivative ∂ of a holomorphic quantity. But we shouldn’t be so cavalier because there is a singularity at z = w. For example, consider the following equation, ∂ ¯ ∂ ln|z −w|2 = ∂ ¯ = 2πδ(z −w,z¯−w¯) (4.38)

z¯ z z¯ z −w We proved this statement after equation (4.21). (The factor of 2 difference from (4.21)

can be traced to the conventions we defined for complex coordinates in Section 4.0.1).

Lookingattheintermediatestepin(4.38),weagainhaveananti-holomorphicderivative of a holomorphic function and you might be tempted to say that this also vanishes. But you’d be wrong: subtle things happen because of the singularity and equation (4.38)

tells us that the function 1/z secretly depends on z¯. (This should really be understood as a statement about distributions, with the delta function integrated against arbitrary test functions). Using this result, we can write (cid:18) (cid:19)

1 1 1 π ∂ ¯ ∂ ¯ = ∂ ¯ ∂ ¯ ∂2∂ = ∂2∂ ∂ ¯ δ(z −w,z¯−w¯)

z¯ w¯ (z −w)4 6 z¯ w¯ z w z −w 3 z w w¯ Inserting this into the correlation function (4.37) and stripping off the ∂ ∂ derivatives z w on both sides, we end up with what we want, cπ T (z,z¯) T (w,w¯) = ∂ ∂ δ(z −w,z¯−w¯) (4.39)

zz¯ ww¯ z w¯ SotheOPEofT andT almostvanishes,butthere’ssomestrangesingularbehaviour zz¯ ww¯ going on as z → w. This is usually referred to as a contact term between operators and, as we have shown, it is needed to ensure the conservation of energy-momentum.

We will now see that this contact term is responsible for the Weyl anomaly.

We assume that (cid:104)Tα(cid:105) = 0 in flat space. Our goal is to derive an expression for (cid:104)Tα(cid:105)

α α close to flat space. Firstly, consider the change of (cid:104)Tα(cid:105) under a general shift of the metric δg . Using the definition of the energy-momentum tensor (4.4), we have αβ (cid:90)

δ(cid:104)Tα(σ)(cid:105) = δ Dφ e−STα(σ)

α α (cid:90) (cid:18) (cid:90) (cid:19)

1 √ = Dφ e−S Tα(σ) d2σ(cid:48) g δgβγT (σ(cid:48))

4π α βγ If we now restrict to a Weyl transformation, the change to a flat metric is δg = 2ωδ , αβ αβ so the change in the inverse metric is δgαβ = −2ωδαβ. This gives (cid:90) (cid:18) (cid:90) (cid:19)

δ(cid:104)Tα(σ)(cid:105) = − Dφ e−S Tα(σ) d2σ(cid:48) ω(σ(cid:48))Tβ (σ(cid:48)) (4.40)

α 2π α β – 88 – Now we see why the OPE (4.39) determines the Weyl anomaly. We need to change between complex coordinates and Cartesian coordinates, keeping track of factors of 2.

We have Tα(σ)Tβ (σ(cid:48)) = 16T (z,z¯) T (w,w¯)

α β zz¯ ww¯ Meanwhile, using the conventions laid down in 4.0.1, we have 8∂ ∂ δ(z −w,z¯−w¯) = z w¯ −∂2δ(σ −σ(cid:48)). This gives us the OPE in Cartesian coordinates cπ Tα(σ)Tβ (σ(cid:48)) = − ∂2δ(σ −σ(cid:48))

α β 3 We now plug this into (4.40) and integrate by parts to move the two derivatives onto the conformal factor ω. We’re left with, c c δ(cid:10 4) ⟨Tα⟩ = ∂²ω ⇒ ⟨Tα⟩ = − R/12 where, to get the final step, we’ve used (4.36) and, since we’re working infinitesimally, we can replace e^{-2ω} ≈ 1. This completes the proof of the Weyl anomaly, at least for spaces infinitesimally close to flat space. The fact that R remains on the right-hand-side for general 2d surfaces follows simply from the comments after equation (4.35), most pertinently the need for the expression to be reparameterization invariant.

4.4.3 c is for Cardy The Casimir effect and the Weyl anomaly have a similar smell. In both, the central charge provides an extra contribution to the energy. We now demonstrate a different avatar of the central charge: it tells us the density of high energy states.

We will study conformal field theory on a Euclidean torus. We’ll keep our normalization σ ∈ [0,2π), but now we also take τ to be periodic, lying in the range τ ∈ [0,β). The partition function of a theory with periodic Euclidean time has a very natural interpretation: it is related to the free energy of the theory at temperature T = 1/β.

Z[β] = Tr e^{-βH} = e^{-βF} (4.41)

At very low temperatures, β → ∞, the free energy is dominated by the lowest energy state. All other states are exponentially suppressed. But we saw in 4.4.1 that the vacuum state on the cylinder has Casimir energy H = −c/12. In the limit of low temperature, the partition function is therefore approximated by Z → e^{cβ/12} as β → ∞ (4.42)

Now comes the trick. In Euclidean space, both directions of the torus are on equal footing. We’re perfectly at liberty to decide that σ is “time” and τ is “space”. This can’t change the value of the partition function. So let’s make the swap. To compare to our original partition function, we want the spatial direction to have range [0,2π). Happily, due to the conformal nature of our theory, we arrange this through the scaling τ → (2π/β) τ, σ → (2π/β) σ Now we’re back where we started, but with the temporal direction taking values in σ ∈ [0,4π²/β). This tells us that the high-temperature and low-temperature partition functions are related, Z[4π²/β] = Z[β]

This is called modular invariance. We’ll come across it again in Section 6.4. Writing β' = 4π²/β, this tells us the very high temperature behaviour of the partition function Z[β'] → e^{cπ²/3β'} as β' → 0 But the very high temperature limit of the partition function is sampling all states in the theory. On entropic grounds, this sampling is dominated by the high energy states. So this computation is telling us how many high energy states there are.

To see this more explicitly, let’s do some elementary manipulations in statistical mechanics. Any system has a density of states ρ(E) = e^{S(E)}, where S(E) is the entropy. The free energy is given by e^{-βF} = ∫ dE ρ(E) e^{-βE} = ∫ dE e^{S(E)−βE} In two dimensions, all systems have an entropy which scales at large energy as S(E) → N E (4.43)

The coefficient N counts the number of degrees of freedom. The fact that S ∼ E is equivalent to the fact that F ∼ T², as befits an energy density in a theory with one spatial dimension. To see this, we need only approximate the integral by the saddle point S'(E*) = β. From (4.43), this gives us the free energy F ∼ N/(2T²)

We can now make the statement about the central charge more explicit. In a conformal field theory, the entropy of high energy states is given by S(E) ∼ cE This is Cardy’s formula. A more careful analysis of the coefficients shows that the high energy density of states scales as S(E) → 2π √(cE/6) − (c/24) (4.44)

where the offset is the Casimir energy (4.34) that we derived previously. This is the contribution from left-movers. There is a similar contribution from right-movers, depending on c̃.

4.4.4 c has a Theorem The connection between the central charge and the degrees of freedom in a theory is given further weight by a result of Zamolodchikov, known as the c-theorem. The idea of the c-theorem is to stand back and look at the space of all theories and the renormalization group (RG) flows between them.

Conformal field theories are special. They are the fixed points of the renormalization group, looking the same at all length scales. One can consider perturbing a conformal field theory by adding an extra term to the action, S → S + α ∫ d²σ O(σ)

Here O is a local operator of the theory, while α is some coefficient. These perturbations fall into three classes, depending on the dimension Δ of O.

• Δ < 2: In this case, α has positive dimension: [α] = 2 − Δ. Such deformations are called relevant because they are important in the infra-red. RG flow takes us away from our original CFT. We only stop flowing when we hit a new CFT (which could be trivial with c = 0).

• Δ = 2: The constant α is dimensionless. Such deformations are called marginal. The deformed theory defines a new CFT.

• Δ > 2: The constant α has negative dimension. These deformations are irrelevant. The infra-red physics is still described by the original CFT. But the ultra-violet physics is altered. We expect information is lost as we flow from an ultra-violet theory to the infra-red. The c-theorem makes this intuition precise. The theorem exhibits a function c on the space of all theories which monotonically decreases along RG flows. At the fixed points, c coincides with the central charge of the CFT.

A Thermodynamic Proof of the c-Theorem

There are a number of different proofs of the c-theorem. Here we give one that is particularly physical. The basic idea is to heat up the system to a finite temperature T and compute the speed of sound. The c-theorem follows from the requirement that the speed of sound does not exceed the speed of light (which, in our conventions, is simply 1). I should warn you that the style of argument in this section is somewhat different from the rest of these lectures. But, if nothing else, it reminds you that just because you’re learning string theory, you shouldn’t neglect basic physics!

Let’s first start with a CFT. For simplicity, we assume that c = c̃. Then, from (4.44), we have the asymptotic behaviour S(E) → 4π √(cER)

where we have dropped the c/24 offset, and the overall coefficient is 4π rather than 2π because we are including both left- and right-moving sectors. To compare with familiar, thermodynamic formulae we write this in terms of the spatial volume V = 2πR, so S(E) → 4π √(πcEV)

Now, the temperature is defined to be 1/T = ∂S/∂E = √(πcV)/(2√(3E)) ⇒ E = 2πT √(πcV/3)

From this, we can compute the entropy of a CFT as a function of temperature, rather than as a function of energy S(T) = 8π³cVT/3 ⇒ s(T) = 8π³cT/3 (4.45)

where s = S/V is the entropy density.

Now we’ll consider a more general situation. We’ll flow from some CFT in the UV with central charge c_UV to another CFT in the IR with central charge c_IR. It may be that the final theory is gapped – meaning that everything is massless – in which case c_IR = 0. Our goal is to prove that, regardless of the flow, we always have c_UV ≥ c_IR (with equality if there is no flow at all). To achieve this, we need to play around with some thermodynamic identities. In particular, we need the following result

Claim: s = ∂P/∂T (4.46)

with P the pressure.

Proof: Given the energy E = E(S,V), the first law of thermodynamics tells us dE = TdS − PdV The free energy is then defined as F(T,V) = E − TS and obeys dF = −SdT − PdV (4.47)

But the free energy is extensive and this means that it must, in fact, be proportional to V since this is the only extensive quantity that it can depend on. So F(T,V) = −P(T)V From this we learn that dF = − VdT − PdV − V(∂P/∂T)dT Comparing to (4.47) gives us the claimed result (4.46). ∎

Finally, we recall that the speed of sound in a system is given by (see, for example, the lectures on Fluid Mechanics)

c_s² = dP/dε where ε = E/V is the energy density. At fixed volume, we have dE = TdS ⇒ dε = Tds All of which means that we can express the speed of sound as c_s² = (1/T)(dP/ds) = (1/T)(dP/dT)(dT/ds) = (s/T)(dT/ds) = (d log T)/(d log s)

This is the key result that we need. Now we define a thermal c-function χ = s/T As we’ve seen in (4.45), when we have a CFT the function χ is proportional to the central charge: χ = 8π³c/3. If we flow from a CFT in the UV, with central charge c_UV, to a different CFT in the IR with central charge c_IR, then χ will interpolate between these two values (multiplied by 8π³/3) as we vary the temperature. To prove the c-theorem, we need to show that as we decrease the temperature, and so excite lower energy degrees of freedom, the function χ necessarily decreases. We do this by relating χ to the speed of sound, 1/c_s² = d log s/d log T = d log(χT)/d log T = 1 + d log χ/d log T By causality, we must have c_s² ≤ 1 (with equality when we have a CFT) and so d log χ/d log T ≥ 0 ⇒ dχ/dT ≥ 0 But this is what we wanted. We learn that we necessarily have c_UV ≥ c_IR. This is the c-theorem.

## 4.5 The Virasoro Algebra

So far our discussion has been limited to the operators of the CFT. We haven’t said anything about states. We now remedy this. We start by taking a closer look at the map between the cylinder and the plane.

4.5.1 Radial Quantization

To discuss states in a quantum field theory we need to think about where they live and how they evolve. For example, consider a two dimensional quantum field theory defined on the plane. Traditionally, when quantizing this theory, we parameterize the plane by Cartesian coordinates (t,x) which we’ll call “time” and “space”. The states live on spatial slices. The Hamiltonian generates time translations and hence governs the evolution of states.

However, the map between the cylinder and the plane suggests a different way to quantize a CFT on the plane. The complex coordinate on the cylinder is taken to be ω, while the coordinate 在平面上是 z。它们的关系为， ω = σ + iτ , z = e^{-iω} 在圆柱面上，态存在于恒定 σ 的空间切片上，并由哈密顿量演化，如图 24 所示： H = ∂ 映射到平面后，哈密顿量变为伸缩算子 D = z∂ + \bar{z}\bar{∂} 如果我们希望平面上的态能记住它们在圆柱面上的根源，它们应该存在于恒定半径的圆上。它们的演化由伸缩算子 D 支配。

这种处理理论的方法被称为径向量子化。

通常在量子场论中，我们关注时间序关联函数。圆柱面上的时间排序在平面上变为径向排序。关联函数中的算子按插入径向距离从大到小的顺序从左到右排列。

Virasoro 生成元让我们看看在平面上评估的应力张量 T(z) 变成了什么。在圆柱面上，我们会将 T 进行傅里叶展开。

T_{\text{cylinder}}(w) = - \sum_{m=-\infty}^{\infty} L_m e^{imw} + \frac{c}{24} 经过变换 (4.33) 到平面后，这变成了洛朗展开 T(z) = \sum_{m=-\infty}^{\infty} L_m z^{m+2} 同样，对于右移部分也有类似的陈述 \bar{T}(\bar{z}) = \sum_{m=-\infty}^{\infty} \tilde{L}_m \bar{z}^{m+2} 我们可以反转这些表达式，用 T(z) 表示 L_n。我们需要取一个合适的围道积分 L_n = \frac{1}{2\pi i} \oint dz \, z^{n+1} T(z) , \quad \tilde{L}_n = \frac{1}{2\pi i} \oint d\bar{z} \, \bar{z}^{n+1} \bar{T}(\bar{z}) \quad (4.48)

其中，如果我们只想得到 L_n 或 \tilde{L}_n，我们必须确保围道内没有其他算子插入。

在径向量子化中，L_n 是与共形变换 δz = z^{n+1} 相关的守恒荷。要看到这一点，回忆相应的 Noether 流，由 (4.7) 给出，是 J(z) = z^{n+1} T(z)。此外，围道积分 \oint dz 映射到圆柱面上空间切片周围的积分。这告诉我们 L_n 是一个守恒荷，其中“守恒”意味着它在圆柱面上的时间演化下，或在平面上的径向演化下是常数。类似地，\tilde{L}_n 是与共形变换 δ\bar{z} = \bar{z}^{n+1} 相关的守恒荷。

当我们进入量子理论时，守恒荷成为变换的生成元。因此，算子 L_n 和 \tilde{L}_n 生成共形变换 δz = z^{n+1} 和 δ\bar{z} = \bar{z}^{n+1}。它们被称为 Virasoro 生成元。特别地，我们最喜欢的两个共形变换是： • L_{-1} 和 \tilde{L}_{-1} 生成平面上的平移。

• L_0 和 \tilde{L}_0 生成伸缩和旋转。

系统的哈密顿量——它度量圆柱面上态的能量——被映射为平面上的伸缩算子。当作用于理论的态时，这个算子表示为 D = L_0 + \tilde{L}_0

4.5.2 Virasoro 代数如果我们有一些守恒荷，我们应该做的第一件事是计算它们的代数。这个代数的表示随后对理论的态进行分类。（例如，想想氢原子中的角动量）。对于共形对称性，我们想要确定 L_n 生成元所服从的代数。一个很好的事实是，对易关系实际上编码在 TT OPE 中。让我们看看这是如何工作的。

我们想计算 [L_m, L_n]。让我们将 L_m 写成对 dz 的围道积分，将 L_n 写成对 dw 的围道积分。（注意：z 和 w 现在都表示复平面上的坐标）。对易子是 [L_m, L_n] = \left( \frac{1}{2\pi i} \oint dz \frac{1}{2\pi i} \oint dw - \frac{1}{2\pi i} \oint dw \frac{1}{2\pi i} \oint dz \right) z^{m+1} w^{n+1} T(z) T(w)

这到底是什么意思？！我们需要记住，所有算子方程都应被视为存在于时间序关联函数内部。只是现在我们在 z 平面上工作，这个说法已经转变为径向序关联函数：外面的在左边，里面的在右边。

所以 L_m L_n 表示 z 在 w 外面，而 L_n L_m 表示 w 在 z 外面。

计算对易子的技巧是首先固定 w 并进行 dz 积分。得到的围道是， 一个围绕 w 的小圆圈，然后是一个围绕 z 的大圆圈，减去一个围绕 w 的大圆圈和一个围绕 z 的小圆圈。

换句话说，我们围绕固定点 w 进行 z 积分，得到 [L_m, L_n] = \frac{1}{2\pi i} \oint dw \, w^{n+1} \frac{1}{2\pi i} \oint dz \, z^{m+1} T(z) T(w)

= \frac{1}{2\pi i} \oint dw \, \text{Res}_{z=w} \left[ z^{m+1} w^{n+1} \left( \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} + ... \right) \right]

为了计算 z = w 处的留数，我们首先需要将 z^{m+1} 在点 w 附近进行泰勒展开， z^{m+1} = w^{m+1} + (m+1) w^m (z-w) + \frac{m(m+1)}{2} w^{m-1} (z-w)^2 + \frac{m(m^2-1)}{6} w^{m-2} (z-w)^3 + ...

留数随后从这三项中的每一项获得贡献， [L_m, L_n] = \frac{1}{2\pi i} \oint dw \, w^{n+1} \left[ w^{m+1} \partial T(w) + 2(m+1) w^m T(w) + \frac{c}{12} m(m^2-1) w^{m-2} \right]

为了继续，最简单的方法是对第一项进行分部积分。然后我们进行 w 积分。但对于前两项，得到的积分形式如 (4.48)，并给出 L_{m+n}。对于第三项，我们拾取极点。最终结果是 [L_m, L_n] = (m-n) L_{m+n} + \frac{c}{12} m(m^2-1) \delta_{m+n,0} 这就是 Virasoro 代数。它非常有名。L_n 满足完全相同的代数，只是 c 被 \tilde{c} 替换。当然，[L_m, \tilde{L}_n] = 0。c 的出现是 Virasoro代数中的额外项被称为“中心荷”。一般来说，中心荷是代数中与所有其他元素对易的额外项。

共形 = 微分同胚 + Weyl

我们可以为Virasoro代数建立一些直观理解。我们知道L生成共形变换δz = z^{n+1}。考虑一个密切相关的坐标变换δz = z^{n+1}。它们由向量场生成： l_n = z^{n+1}∂_z (4.49)

但计算它们的对易关系很简单： [l_n, l_m] = (m−n)l_{m+n} 这给出了Virasoro代数的第一部分。但中心项呢？关键要记住的是，正如我们在本章开头强调的，共形变换不仅仅是坐标的重新参数化：它是一个重新参数化，后跟一个补偿性的Weyl重标度。Virasoro代数中的中心项源于Weyl重标度。

4.5.3 Virasoro代数的表示有了守恒荷的代数，我们现在可以开始看到共形对称性如何将态分类为表示。

假设我们有一个态|ψ⟩，它是L_0和L̃_0的本征态： L_0|ψ⟩ = h|ψ⟩, L̃_0|ψ⟩ = h̃|ψ⟩ 回到圆柱面上，这对应于某个能量为 E = (c + c̃)/2π = h + h̃ − (c + c̃)/24 的态。因此，我们将本征值h和h̃称为态的能量。通过作用L_n算符，我们可以得到具有本征值 L_0 L_n|ψ⟩ = (L_n L_0 − n L_n)|ψ⟩ = (h − n)L_n|ψ⟩ 的进一步态。这告诉我们L_n根据n的符号是升算符或降算符。当n > 0时，L_n降低态的能量，L_{-n}提高态的能量。如果谱有下界，必须存在一些态被所有n > 0的L_n和L_{-n}湮灭。这样的态称为初级态。它们满足 L_n|ψ⟩ = L_{-n}|ψ⟩ = 0 对所有n > 0 在表示论的语言中，它们也称为最高权态。它们是能量最低的态。

Virasoro代数的表示现在可以通过作用升算符L_{-n}（n > 0）于初级态来构建。显然这导致一个无限高的态塔。以这种方式获得的所有态称为后代态。从一个初始初级态|ψ⟩，态塔展开...

|ψ⟩ L_{-1}|ψ⟩ L_{-1}^2|ψ⟩, L_{-2}|ψ⟩ L_{-1}^3|ψ⟩, L_{-1}L_{-2}|ψ⟩, L_{-3}|ψ⟩ 整个态集称为Verma模。它们是Virasoro代数的不可约表示。这意味着如果我们知道初级态的谱，那么我们就知道整个理论的谱。

一些注释： • 真空态|0⟩具有h = 0。这个态满足 L_n|0⟩ = 0 对所有n ≥ −1 (4.50)

注意这个态保持了最大数量的对称性：像所有初级态一样，它被n > 0的L_n湮灭，但它也被L_0和L_{-1}湮灭。这符合我们的直觉，即真空态应在尽可能多的对称性下不变。你可能认为我们可以更进一步，要求真空态满足L_n|0⟩ = 0对所有n。但这与Virasoro代数中的中心荷项不一致。条件(4.50)是我们能做到的最好情况。

• 这个讨论应该让你想起一些事情。我们在弦的协变量子化中看到了非常类似的情况，当时我们施加了条件(2.6)作为约束。我们将在第5节看到初级态与弦谱之间的联系。

• 有一个你应该意识到的微妙之处：Verma模中的态不一定都是独立的。可能某些态的线性组合为零。这个线性组合称为零态。零态的存在取决于h和c的值。例如，假设我们处于一个中心荷为c = 2h(5−8h)/(2h+1)的理论中，其中h是初级态|ψ⟩的能量。那么很容易检查以下组合具有零范数： L_{-2}|ψ⟩ − L_{-1}^2|ψ⟩/(2(2h+1)) (4.51)

• 初级态与第4.2.3节定义的初级算符之间有密切关系。事实上，初级态的能量h和h̃将恰好是理论中初级算符的权重。这种联系将在第4.6节描述。

4.5.4 幺正性的后果有一个物理要求理论必须遵守，我们至今尚未提及：幺正性。这是指在闵可夫斯基签名时空中概率守恒。如果我们有一个控制时间演化的厄米哈密顿量，幺正性立即成立。但到目前为止，我们的讨论在某种程度上是代数的，我们还没有强制执行这个条件。现在让我们这样做。

ace our footsteps back to the Euclidean cylinder and then back again to the Minkowski cylinder where we can ask questions about time evolution. Here the Hamiltonian density takes the form H = T + T = L_n e^{-inσ^+} + \bar{L}_n e^{-inσ^-} So for the Hamiltonian to be Hermitian, we require L_n = L_{-n}^† This requirement imposes some strong constraints on the structure of CFTs. Here we look at a couple of trivial, but important, constraints that arise due to unitarity and the requirement that the physical Hilbert space does not contain negative norm states.

• h ≥ 0: This fact follows from looking at the norm, |L_{-1}|ψ⟩|^2 = ⟨ψ|L_{-1}L_{+1}|ψ⟩ = ⟨ψ|[L_{-1}, L_{+1}]|ψ⟩ = 2h⟨ψ|ψ⟩ ≥ 0 The only state with h = 0 is the vacuum state |0⟩.

• c > 0: To see this, we can look at |L_{-n}|0⟩|^2 = ⟨0|[L_{-n}, L_n]|0⟩ = n(n^2 - 1) ≥ 0 (4.52)

So c ≥ 0. If c = 0, the only state in the vacuum module is the vacuum itself. It turns out that, in fact, the only state in the whole theory is the vacuum itself. Any non-trivial CFT has c > 0.

There are many more requirements of this kind that constrain the theory. In fact, it turns out that for CFTs with c < 1 these requirements are enough to classify and solve all theories.

## 4.6 The State-Operator Map

In this section we describe one particularly important aspect of conformal field theories: a map between states and local operators.

Firstly, let’s get some perspective. In a typical quantum field theory, the states and local operators are very different objects. While local operators live at a point in spacetime, the states live over an entire spatial slice. This is most clear if we write down a Schrödinger-style wavefunction. In field theory, this object is actually a wave-functional, Ψ[φ(σ)], describing the probability for every field configuration φ(σ) at each point σ in space (but at a fixed time).

Given that states and local operators are such very different beasts, it’s a little surprising that in a CFT there is an isomorphism between them: it’s called the state-operator map. The key point is that the distant past in the cylinder gets mapped to a single point z = 0 in the complex plane. So specifying a state on the cylinder in the far past is equivalent to specifying a local disturbance at the origin.

To make this precise, we need to recall how to write down wavefunctions using path integrals. Different states are computed by putting different boundary conditions on the functional integral. Let’s start by returning to quantum mechanics and reviewing a few simple facts. The propagator for a particle to move from position x_i at time τ_i to position x_f at time τ_f is given by G(x_f, x_i) = ∫_{x(τ_i)=x_i}^{x(τ_f)=x_f} Dx e^{iS} This means that if our system starts off in some state described by the wavefunction ψ_i(x_i) at time τ_i then (ignoring the overall normalization) it evolves to the state ψ_f(x_f, τ_f) = ∫ dx_i G(x_f, x_i) ψ_i(x_i, τ_i)

There are two lessons to take from this. Firstly, to determine the value of the wave-function at a given point x_f, we evaluate the path integral restricting to paths which satisfy x(τ_f) = x_f. Secondly, the initial state ψ(x_i) acts as a weighting factor for the integral over initial boundary conditions.

Let’s now write down the same formula in a field theory, where we’re dealing with wavefunctionals. We’ll work with the Euclidean path integral on the cylinder. If we start with some state Ψ_i[φ_i(σ)] at time τ_i, then it will evolve to the state Ψ_f[φ_f(σ), τ_f] = ∫_{φ(τ_i)=φ_i}^{φ(τ_f)=φ_f} Dφ_i Dφ_f e^{-S[φ]} Ψ_i[φ_i(σ), τ_i]

How do we write a similar expression for states after the map to the complex plane? Now the states are defined on circles of constant radius, say |z| = r, and evolution is governed by the dilatation operator. Suppose the initial state is defined at |z| = r_i. In the path integral, we integrate over all fields with fixed boundary conditions φ(r_i) = φ_i and φ(r_f) = φ_f on the two edges of the annulus shown in the figure, Ψ_f[φ_f(σ), r_f] = ∫_{φ(r_i)=φ_i}^{φ(r_f)=φ_f} Dφ_i Dφ_f e^{-S[φ]} Ψ_i[φ_i(σ), r_i]

This is the traditional way to define a state in field theory, albeit with a slight twist because we’re working in radial quantization. We see that the effect of the initial state is to change the weighting of the path integral over the inner ring at |z| = r_i.

Let’s now see what happens as we take the initial state back to the far past and, ultimately, to z = 0? We must now integrate over the whole disc |z| ≤ r_f, rather than the annulus. The only effect of the initial state is now to change the weighting of the path integral at the point z = 0. But that’s exactly what we mean by a local operator inserted at that point. This means that each local operator O(z = 0) defines a different state in the theory, Ψ[φ; r] = ∫_{φ(r)=φ} Dφ e^{-S[φ]} O(z = 0)

We’re now integrating over all field configurations within the disc, including all possible values of the field at z = 0, which is analogous to integrating over the boundary conditions Dφ on the inner circle.

• The state-operator map is only true in conformal field theories where we can map the cylinder to the plane. It also holds in conformal field theories in higher dimensions (where R×SD−1 can be mapped to the plane RD). In non-conformal field theories, a typical local operator creates many different states.

• The state-operator map does not say that the number of states in the theory is equal to the number of operators: this is never true. It does say that the states are in one-to-one correspondence with the local operators.

• You might think that you’ve seen something like this before. In the canonical quantization of free fields, we create states in a Fock space by acting with creation operators. That’s not what’s going on here! The creation operators are just about as far from local operators as you can get. They are the Fourier transforms of local operators.

• There’s a special state that we can create this way: the vacuum. This arises by inserting the identity operator 1 into the path integral. Back in the cylinder picture, this just means that we propagate the state back to time τ = −∞ which is a standard trick used in the Euclidean path integral to project out all but the ground state. For this reason the vacuum is sometimes referred to, in operator notation, as |1⟩.

4.6.1 Some Simple Consequences Let’s use the state-operator map to wrap up a few loose ends that have arisen in our study of conformal field theory.

Firstly, we’ve defined two objects that we’ve called “primary”: states and operators. The state-operator map relates the two. Consider the state |O⟩, built from inserting a primary operator O into the path integral at z = 0. We can look at, ∮ dz L |O⟩ = ∮ dz z^{n+1} T(z) O(z = 0)

2πi 2πi = ∮ dz z^{n+1} ( hO / z^2 + ∂O / z + ... ) (4.53)

2πi

You may wonder what became of the path integral ∫ Dφ e^{-S[φ]} in this expression. The answer is that it’s still implicitly there. Remember that operator expressions such as (4.48) are always taken to hold inside correlation functions. But putting an operator in the correlation function is the same thing as putting it in the path integral, weighted with e^{-S[φ]}.

From (4.53) we can see the effect of various generators on states • L_{-1} |O⟩ = |∂O⟩: In fact, this is true for all operators, not just primary ones. It is expected since L_{-1} is the translation generator.

• L_0 |O⟩ = h|O⟩: This is true of any operator with well defined transformation under scaling.

• L_n |O⟩ = 0 for all n > 0. This is true only of primary operators O. Moreover, it is our requirement for |O⟩ to be a primary state.

This has an important consequence. We stated earlier that one of the most important things to compute in a CFT is the spectrum of weights of primary operators. This seems like a slightly obscure thing to do. But now we see that it has a much more direct, physical meaning. It is the spectrum of energy and angular momentum of states of the theory defined on the cylinder.

## X X X X

|ψ> X X X X Figure 28:

Another loose end: when defining operators which carry specific weight, we made the statement that we could always work in a basis of operators which have specified eigenvalues under D and L. This follows immediately from the statement that we can always find a basis of eigenstates of H and L on the cylinder.

Finally, we can use this idea of the state-operator map to understand why the OPE works so well in conformal field theories. Suppose that we’re interested in some correlation function, with operator insertions as shown in the figure. The statement of the OPE is that we can replace the two inner operators by a sum of operators at z = 0, independent of what’s going on outside of the dotted line. As an operator statement, that sounds rather surprising. But this follows by computing the path integral up to the dotted line, by which point the only effect of the two operators is to determine what state we have. This provides us a way of understanding why the OPE is exact in CFTs, with a radius of convergence equal to the next-nearest insertion.

4.6.2 Our Favourite Example: The Free Scalar Field Let’s illustrate the state-operator map by returning yet again to the free scalar field. On a Euclidean cylinder, we have the mode expansion X(w,w̄) = x + α' p τ + i ∑_{n≠0} (1/n) ( α_n e^{inw} + ᾱ_n e^{inw̄} )

where we retain the requirement of reality in Minkowski space, which gave us α_n* = α_{-n} and ᾱ_n* = ᾱ_{-n}. We saw in Section 4.3 that X does not have good conformal properties. Before transforming to the z = e^{-iw} plane, we should work with the primary field on the cylinder, ∂ X(w,w̄)

¯) = − α e^{iw} with α ≡ i p / w n 0 2 2

Since ∂X is a primary field of weight h = 1, its transformation to the plane is given by (4.18) and reads ∂z^{-1} ∂ X(z) = ∂ X(w) = −i α' ∑ α / w 2 z^{n+1} and similar for ∂X. Inverting this gives an equation for α as a contour integral, α = i ∮ dz / (2πi) z^n ∂X(z) (4.54)

Just as the TT OPE allowed us to determine the [L_m, L_n] commutation relations in the previous section, so the ∂X∂X OPE contains the information about the [α_m, α_n] commutation relations. The calculation is straightforward, [α_m, α_n] = − ∮ dz / (2πi) ∮ dw / (2πi) ∮ dw / (2πi) ∮ dz / (2πi) z^m w^n ∂X(z) ∂X(w)

= − 2 / α' ∮ dw / (2πi) Res_{z=w} z^m w^n + ...

= 2 / α' ∮ dw / (2πi) w^{m+n-1} = 2 / α' m δ_{m+n,0} where, in going from the second to third line, we have Taylor expanded z around w. Hearteningly, the final result agrees with the commutation relation (2.2) that we derived in string theory using canonical quantization.

The State-Operator Map for the Free Scalar Field

Let’s now look at the map between states and local operators. We know from canonical quantization that the Fock space is defined by acting with creation operators α_{-m} with m > 0 on the vacuum |0⟩. The vacuum state itself obeys α_m |0⟩ = 0 for m > 0. Finally, there is also the zero mode α_0 ∼ p which provides all states with another quantum number. A general state is given by ∏_{m=1} α_{-m}^{k_m} |0;p⟩

Let’s try and recover these states by inserting operators into the path integral. Our first task is to check whether the vacuum state is indeed equivalent to the insertion of the identity operator. In other words, is the ground state wavefunctional of the theory on the circle |z| = r really given by Ψ_0[X_f] = ∫ DX e^{-S[X]} ? (4.55)

We want to check that this satisfies the definition of the vacuum state, namely α_m |0⟩ = 0 for m > 0. How do we act on the wavefunctional with an operator? We should still integrate over all field configurations X(z, z̄), subject to the boundary conditions at X(|z| = r) = X_f. But now we should insert the contour integral (4.54) at some |w| < r (because, after all, the state is only going to vanish after we’ve hit it with α_m, not before!). So we look at α_m Ψ_0[X_f] = ∫ DX e^{-S[X]} ∮ dw / (2πi) w^m ∂X(w)

The path integral is weighted by the action (4.19) for a free scalar field. If a given configuration diverges somewhere inside the disc |z| < r, then the action also diverges. This ensures that only smooth functions ∂X(z), which have no singularity inside the disc, contribute. But for such functions we have ∮ dw / (2πi) w^m ∂X(w) = 0 for all m ≥ 0

So the state (4.55) is indeed the vacuum state. In fact, since α_0 also annihilates this state, it is identified as the vacuum state with vanishing momentum.

What about the excited states of the theory?

Claim: α_{-m} |0⟩ = |∂^m X⟩. By which we mean that the state α_{-m} |0⟩ can be built from the path integral, α_{-m} |0⟩ = ∫ DX e^{-S[X]} ∂^m X(z = 0) (4.56)

Proof: We can check this by acting on |∂^m X⟩ with the annihilation operators α_n.

α_n |∂^m X⟩ ∼ ∫ DX e^{-S[X]} X_f(r) ∮ dw / (2πi) w^n ∂X(w) ∂^m X(z = 0)

We can focus on the operator insertions and use the OPE (4.23). We drop the path integral and just focus on the operator equation (because, after all, operator equations only make sense in correlation functions which is the same thing as in path integrals). We have ∮ dw / (2πi) w^n ∂^{m-1} (1 / (w - z)^2) |_{z=0} = ∮ dw / (2πi) w^n ∂^{m-1} (1 / w^2) = m! ∮ dw / (2πi) w^{n-m-1} = 0 unless m = n

This confirms that the state (4.56) has the right properties. ∎

Finally, we should worry about the zero mode, or momentum α_0 ∼ p. It is simple to show using the techniques above (together with the OPE (4.26)) that the momentum of a state arises by the insertion of the primary operator e^{ipX}. For example, |0;p⟩ ∼ ∫ DX e^{-S[X]} e^{ipX(z=0)} .

## 4.7 Brief Comments on Conformal Field Theories with Boundaries

The open string lives on the infinite strip with spatial coordinate σ ∈ [0,π]. Here we make just a few brief comments on the corresponding conformal field theories.

As before, we can define the complex coordinate w = σ + iτ and make the conformal map z = e^{-iw}. This time the map takes us to the upper-half plane: Im z ≥ 0. The end points of the string are mapped to the real axis, Im z = 0.

Much of our previous discussion goes through as before. But now we need to take care of boundary conditions at Im z = 0. Let’s first look at T_{αβ}. Recall that the stress-energy tensor exists because of translational invariance. We still have translational invariance in the direction parallel to the boundary — let’s call the associated tangent vector t_α. But translational invariance is broken perpendicular to the boundary — we call the normal vector nα. The upshot of this is that T_{αβ} remains a conserved current.

To implement Neumann boundary conditions, we insist that none of the current flows out of the boundary. The condition is T_{αβ} n^α t^β = 0 at Im z = 0 In complex coordinates, this becomes T_{zz} = T_{\bar{z}\bar{z}} at Im z = 0 There’s a simple way to implement this: we extend the definition of T_{zz} from the upper-half plane to the whole complex plane by defining T_{zz}(z) = T_{\bar{z}\bar{z}}(\bar{z})

For the closed string we had both functions T_{zz} and T_{\bar{z}\bar{z}} in the whole plane. But for the open string, we have just one of these – say, T_{zz} – in the whole plane. This contains the same information as both T_{zz} and T_{\bar{z}\bar{z}} in the upper-half plane. It’s simpler to work in the whole plane and focus just on T_{zz}. Correspondingly, we now have just a single set of Virasoro generators, L_n = \oint \frac{dz}{2\pi i} z^{n+1} T_{zz}(z)

There is no independent \bar{L}_n for the open string.

A similar doubling trick works when computing the propagator for the free scalar field. The scalar field X(z,\bar{z}) is only defined in the upper-half plane. Suppose we want to implement Neumann boundary conditions. Then the propagator is defined by \langle X(z,\bar{z}) X(w,\bar{w}) \rangle = G(z,\bar{z}; w,\bar{w})

which obeys \partial \bar{\partial} G = -2\pi \alpha' \delta(z - w, \bar{z} - \bar{w}) subject to the boundary condition \partial_\sigma G(z,\bar{z}; w,\bar{w})|_{\sigma=0} = 0 But we solve problems like this in our electrodynamics courses. A useful way of proceeding is to introduce an “image charge” in the lower-half plane. We now let X(z,\bar{z}) vary over the whole complex plane with its dynamics governed by the propagator G(z,\bar{z}; w,\bar{w}) = -\frac{\alpha'}{2} \ln|z - w|^2 - \frac{\alpha'}{2} \ln|z - \bar{w}|^2 (4.57)

Much of the remaining discussion of CFTs carries forward with only minor differences. However, there is one point that is simple but worth stressing because it will be of importance later. This concerns the state-operator map. Recall the logic that leads us to this idea: we consider a state at fixed time on the strip and propagate it back to past infinity τ → −∞. After the map to the half-plane, past infinity is again the origin. But now the origin lies on the boundary. We learn that the state-operator map relates states to local operators defined on the boundary.

This fact ensures that theories on a strip have fewer states than those on the cylinder. For example, for a free scalar field, Neumann boundary conditions require ∂X = \bar{∂}X at Im z = 0. (This follows from the requirement that ∂_σ X = 0 at σ = 0,π on the strip). On the cylinder, the operators ∂X and \bar{∂}X give rise to different states; on the strip they give rise to the same state. This, of course, mirrors what we’ve seen for the quantization of the open string where boundary conditions mean that we have only half the oscillator modes to play with.

## 5. The Polyakov Path Integral and Ghosts

At the beginning of the last chapter, we stressed that there are two very different interpretations of conformal symmetry depending on whether we’re thinking of a fixed 2d background or a dynamical 2d background. In applications to statistical physics, the background is fixed and conformal symmetry is a global symmetry. In contrast, in string theory the background is dynamical. Conformal symmetry is a gauge symmetry, a remnant of diffeomorphism invariance and Weyl invariance.

But gauge symmetries are not symmetries at all. They are redundancies in our description of the system. As such, we can’t afford to lose them and it is imperative that they don’t suffer an anomaly in the quantum theory. At worst, theories with gauge anomalies make no sense. (For example, Yang-Mills theory coupled to only left-handed fundamental fermions is a nonsensical theory for this reason). At best, it may be possible to recover the quantum theory, but it almost certainly has nothing to do with the theory that you started with.

Piecing together some results from the previous chapter, it looks like we’re in trouble. We saw that the Weyl symmetry is anomalous since the expectation value of the stress-energy tensor takes different values on backgrounds related by a Weyl symmetry: \langle T_{αβ} \rangle = -\frac{R}{12} g_{αβ} On fixed backgrounds, that’s merely interesting. On dynamical backgrounds, it’s fatal. What can we do? It seems that the only way out is to ensure that our theory has c = 0. But we’ve already seen that c > 0 for all non-trivial, unitary CFTs. We seem to have reached an impasse. In this section we will discover the loophole. It turns out that we do indeed require c = 0, but there’s a way to achieve this that makes sense.

## 5.1 The Path Integral

In Euclidean space the Polyakov action is given by, S_{Poly} = \frac{1}{4\pi \alpha'} \int d^2\sigma \sqrt{g} g^{αβ} ∂_α X^μ ∂_β X^ν δ_{μν} From now on, our analysis of the string will be in terms of the path integral. We integrate over all embedding coordinates X^μ and all worldsheet metrics g_{αβ}. Schematically, ing 4 pages. As a follow-up, he took another 2.5 pages to analyze the superstring in “Quantum geometry of fermionic strings,” Phys. Lett. B 103, 211 (1981).

the path integral is given by, Z = ∫ DgDX e^{-S Poly [X,g]} / Vol The “Vol” term is all-important. It refers to the fact that we shouldn’t be integrating over all field configurations, but only those physically distinct configurations not related by diffeomorphisms and Weyl symmetries. Since the path integral, as written, sums over all fields, the “Vol” term means that we need to divide out by the volume of the gauge action on field space.

To make the situation more explicit, we need to split the integration over all field configurations into two pieces: those corresponding to physically distinct configurations — schematically depicted as the dotted line in the figure — and those corresponding to gauge transformations — which are shown as solid lines. Dividing by “Vol” simply removes the piece of the partition function which comes from integrating along the solid-line gauge orbits.

In an ordinary integral, if we change coordinates then we pick up a Jacobian factor for our troubles. The path integral is no different. We want to decompose our integration variables into physical fields and gauge orbits. The tricky part is to figure out what Jacobian we get. Thankfully, there is a standard method to determine the Jacobian, first introduced by Faddeev and Popov. This method works for all gauge symmetries, including Yang-Mills and you will also learn about it in the “Advanced Quantum Field Theory” course.

5.1.1 The Faddeev-Popov Method We have two gauge symmetries: diffeomorphisms and Weyl transformations. We will schematically denote both of these by ζ. The change of the metric under a general gauge transformation is g → gζ. This is shorthand for, g_{αβ}(σ) → gζ_{αβ}(σ') = e^{2ω(σ)} (∂σ^γ/∂σ'^α) (∂σ^δ/∂σ'^β) g_{γδ}(σ)

In two dimensions these gauge symmetries allow us to put the metric into any form that we like — say, ĝ. This is called the fiducial metric and will represent our choice of gauge fixing. Two caveats: • Firstly, it’s not true that we can put any 2d metric into the form ĝ of our choosing. This is only true locally. Globally, it remains true if the worldsheet has the topology of a cylinder or a sphere, but not for higher genus surfaces. We’ll revisit this issue in Section 6.

• Secondly, fixing the metric locally to ĝ does not fix all the gauge symmetries. We still have the conformal symmetries to deal with. We’ll revisit this in the Section 6 as well.

Our goal is to only integrate over physically inequivalent configurations. To achieve this, first consider the integral over the gauge orbit of ĝ. For some value of the gauge transformation ζ, the configuration gζ will coincide with our original metric g. We can put a delta-function in the integral to get ∫ Dζ δ(g − ĝζ) = Δ_{FP}^{-1}[g] (5.1)

This integral isn’t equal to one because we need to take into account the Jacobian factor. This is analogous to the statement that ∫ dx δ(f(x)) = 1/|f'|, evaluated at points where f(x) = 0. In the above equation, we have written this Jacobian factor as Δ_{FP}^{-1}. The inverse of this, namely Δ_{FP}, is called the Faddeev-Popov determinant. We will evaluate it explicitly shortly. Some comments: • This whole procedure is rather formal and runs into the usual difficulties with trying to define the path integral. Just as for Yang-Mills theory, we will find that it results in sensible answers.

• We will assume that our gauge fixing is good, meaning that the dotted line in the previous figure cuts through each physically distinct configuration exactly once. Equivalently, the integral over gauge transformations Dζ clicks exactly once with the delta-function and we don’t have to worry about discrete ambiguities (known as Gribov copies in QCD).

• The measure is taken to be the analogue of the Haar measure for Lie groups, invariant under left and right actions Dζ = D(ζ'ζ) = D(ζζ').

When gauge fixing in Yang-Mills theory, the first thing we do is prove that the Faddeev-Popov determinant Δ_{FP} is gauge invariant. However, our route here is a little more subtle. As we’ve stressed above, the Weyl anomaly means that our original theory actually fails to be gauge invariant. We will see that the Faddeev-Popov determinant also fails but can, in certain circumstances, cancel the original failure leaving behind a well-defined theory.

The Faddeev-Popov procedure starts by inserting a factor of unity into the path integral, in the guise of 1 = ∫ Δ_{FP}[g] Dζ δ(g − ĝζ)

We’ll call the resulting path integral expression Z[ĝ] since it depends on the choice of fiducial metric ĝ. The first thing we do is use the δ(g − ĝζ) delta-function to do the integral over metrics, Z[ĝ] = ∫ DζDXDg Δ_{FP}[g] δ(g − ĝζ) e^{-S Poly [X,g]} / Vol = ∫ DζDX Δ_{FP}[ĝζ] e^{-S Poly [X,ĝζ]} / Vol (5.2)

At this stage the integrand depends on ĝζ, wh ere ζ is shorthand for a diffeomorphism and Weyl transformation. Everything in the equation is invariant under diffeomorphisms, but Weyl transformations are another matter. We know that quantum theory ∫ DXe^{−S_Poly} suffers a Weyl anomaly. The action S_Poly is invariant under Weyl rescalings, so the subtlety must come from the measure. Meanwhile, anticipating what’s to come, we will find a similar issue with the Faddeev-Popov determinant Δ_FP.

If, however, we find ourselves in the fortunate situation where the problems cancel then things would work out nicely. In that situation, everything on the right-hand side of (5.2) would conspire to be invariant under both diffeomorphisms and Weyl transformations and we could write

Z[ĝ] = ∫_Vol Dζ DX Δ_FP[ĝ] e^{−S_Poly[X,ĝ]}

But now, nothing depends on the gauge transformation ζ. Indeed, this is precisely the integration over the gauge orbits that we wanted to isolate and it cancels the “Vol” factor sitting outside. We’re left with

Z[ĝ] = ∫ DX Δ_FP[ĝ] e^{−S_Poly[X,ĝ]} (5.3)

This is the integral over physically distinct configurations — the dotted line in the previous figure. We see that the Faddeev-Popov determinant is precisely the Jacobian factor that we need.

Clearly the above discussion only flies if we find ourselves in a situation in which the theory (5.2) is genuinely Weyl invariant. Our next task is to understand when this happens which means that we need to figure out what becomes of Δ_FP when we do a Weyl transformation.

5.1.2 The Faddeev-Popov Determinant

We still need to compute Δ_FP[ĝ]. It’s defined in (5.1). Let’s look at gauge transformations ζ which are close to the identity. In this case, the delta-function δ(g − ĝ_ζ) is going to be non-zero when the metric g is close to the fiducial metric ĝ. In fact, it will be sufficient to look at the delta-function δ(ĝ − ĝ_ζ), which is only non-zero when ζ = 0. We take an infinitesimal Weyl transformation parameterized by ω(σ) and an infinitesimal diffeomorphism δσ^α = v^α(σ). The change in the metric is

δĝ_{αβ} = 2ωĝ_{αβ} + ∇_α v_β + ∇_β v_α

Plugging this into the delta-function, the expression for the Faddeev-Popov determinant becomes

Δ_FP^{−1}[ĝ] = ∫ Dω Dv δ(2ωĝ_{αβ} + ∇_α v_β + ∇_β v_α) (5.4)

where we’ve replaced the integral Dζ over the gauge group with the integral Dω Dv over the Lie algebra of the group since we’re near the identity. (We also suppress the subscript on v in the measure factor to keep things looking tidy).

At this stage it’s useful to represent the delta-function in its integral, Fourier form. For a single delta-function, this is δ(x) = ∫ dp exp(2πipx). But the delta-function in (5.4) is actually a delta-functional: it restricts a whole function. Correspondingly, the integral representation is in terms of a functional integral,

Δ_FP^{−1}[ĝ] = ∫ Dω Dv Dβ exp[ 2πi ∫ d^2σ √ĝ β^{αβ} (2ωĝ_{αβ} + ∇_α v_β + ∇_β v_α) ]

where β^{αβ} is a symmetric 2-tensor on the worldsheet.

We now simply do the Dω integral. It doesn’t come with any derivatives, so it merely acts as a Lagrange multiplier, setting

β^{αβ} ĝ_{αβ} = 0

In other words, after performing the ω integral, β^{αβ} is symmetric and traceless. We’ll take this to be the definition of β^{αβ} from now on. So, finally we have

Δ_FP^{−1}[ĝ] = ∫ Dv Dβ exp[ 4πi ∫ d^2σ √ĝ β^{αβ} ∇_α v_β ]

5.1.3 Ghosts

The previous manipulations give us an expression for Δ_FP^{−1}. But we want to invert it to get Δ_FP. Thankfully, there’s a simple way to achieve this. Because the integrand is quadratic in v and β, we know that the integral computes the inverse determinant of the operator ∇. (Strictly speaking, it computes the inverse determinant of the projection of ∇ onto symmetric, traceless tensors. This observation is important because it means the relevant operator is a square matrix which is necessary to talk about a determinant). But we also know how to write down an expression for the determinant Δ_FP, instead of its inverse, in terms of path integrals: we simply need to replace the commuting integration variables with anti-commuting fields,

β_{αβ} → b_{αβ} v_α → c_α

where b and c are both Grassmann-valued fields (i.e. anti-commuting). They are known as ghost fields. This gives us our final expression for the Faddeev-Popov determinant,

Δ_FP[g] = ∫ Db Dc exp[i S_ghost]

where the ghost action is defined to be

S_ghost = (1/2π) ∫ d^2σ √g b^{αβ} ∇_α c_β (5.5)

and we have chosen to rescale the b and c fields at this last step to get a factor of 1/2π sitting in front of the action. (This only changes the normalization of the partition function which doesn’t matter). Rotating back to Euclidean space, the factor of i disappears. The expression for the full partition function (5.3) is

Z[ĝ] = ∫ DX Db Dc exp(−S_Poly[X,ĝ] − S_ghost[b,c,ĝ])

Something lovely has happened. Although the ghost fields were introduced as some auxiliary constructs, they now appear on the same footing as the dynamical fields.

We learn that gauge fixing comes with a price: our theory has extra ghost fields. The role of these ghost fields is to cancel the unphysical gauge degrees of freedom, leaving only the D − 2 transverse modes of Xµ. Unlike lightcone quantization, they achieve this in a way which preserves Lorentz invariance.

Simplifying the Ghost Action The ghost action (5.5) looks fairly simple. But it looks even simpler if we work in conformal gauge, ĝ = e^{2ω} δ_{αβ} The determinant is ĝ = e^{2ω}. Recall that in complex coordinates, the measure is d²σ = ½d²z, while we can lower the index on the covariant derivative using ∇_z = g_{zz̄} ∇^{z̄} = 2e^{-2ω} ∇^{z̄}. We have S_ghost = 1/(2π) ∫ d²z (b_{zz} ∇^{z̄} c^z + b_{z̄z̄} ∇^z c^{z̄})

In deriving this, remember that there is no field b_{zz̄} because b is traceless. Now comes the nice part: the covariant derivatives are actually just ordinary derivatives. To see why this is the case, look at ∇^{z̄} c^z = ∂^{z̄} c^z + Γ^z_{z̄α} c^α But the Christoffel symbols are given by Γ^z_{z̄α} = ½ g_{zz̄} (∂_{z̄} g_{αz̄} + ∂_α g_{z̄z̄} - ∂_{z̄} g_{z̄α}) = 0 for α = z, z̄ So in conformal gauge, the ghost action factorizes into two free theories, S_ghost = 1/(2π) ∫ d²z (b_{zz} ∂^{z̄} c^z + b_{z̄z̄} ∂^z c^{z̄})

The action doesn’t depend on the conformal factor ω. In other words, it is Weyl invariant without any need to change b and c: these are therefore both neutral under Weyl transformations.

(It’s worth pointing out that b_{αβ} and c^α are neutral under Weyl transformations. But if we raise or lower these indices, then the fields pick up factors of the metric. So b^{αβ} and c_α would not be neutral under Weyl transformations).

## 5.2 The Ghost CFT

Fixing the Weyl and diffeomorphism gauge symmetries has left us with two new dynamical ghost fields, b and c. Both are Grassmann (i.e. anti-commuting) variables. Their dynamics is governed by a CFT. Define b_{zz} = b, b_{z̄z̄} = b̄ c^z = c, c^{z̄} = c̄ The ghost action is given by S_ghost = 1/(2π) ∫ d²z (b ∂ c̄ + b̄ ∂̄ c)

Which gives the equations of motion ∂̄ b = ∂ b̄ = ∂̄ c = ∂ c̄ = 0 So we see that b and c are holomorphic fields, while b̄ and c̄ are anti-holomorphic.

Before moving onto quantization, there’s one last bit of information we need from the classical theory: the stress tensor for the bc ghosts. The calculation is a little bit fiddly. We use the general definition of the stress tensor (4.4), which requires us to return to the theory (5.5) on a general background and vary the metric g_{αβ}. The complications are twofold. Firstly, we pick up a contribution from the Christoffel symbol that is lurking inside the covariant derivative ∇_α. Secondly, we must also remember that b_{αβ} is traceless. But this is a condition which itself depends on the metric: b_{αβ} g^{αβ} = 0. To account for this we should add a Lagrange multiplier to the action imposing tracelessness. After correctly varying the metric, we may safely retreat back to flat space where the end result is rather simple. We have T_{zz̄} = 0, as we must for any conformal theory. Meanwhile, the holomorphic and anti-holomorphic parts of the stress tensor are given by, T = 2 (∂c) b + c ∂b, T̄ = 2 (∂̄c̄) b̄ + c̄ ∂̄b̄. (5.6)

Operator Product Expansions We can compute the OPEs of these fields using the standard path integral techniques that we employed in the last chapter. In what follows, we’ll just focus on the holomorphic piece of the CFT. We have, for example, 0 = ∫ DbDc [ e^{-S_ghost} b(σ') ] = ∫ DbDc e^{-S_ghost} [ - ∂̄ c(σ) b(σ') + δ(σ - σ') ]

which tells us that ∂̄ c(σ) b(σ') = 2π δ(σ - σ')

Similarly, looking at δ/δc(σ) gives ∂̄ b(σ) c(σ') = 2π δ(σ - σ')

We can integrate both of these equations using our favorite formula ∂(1/z) = 2π δ(z, z̄). We learn that the OPEs between fields are given by b(z) c(w) = 1/(z - w) + ...

c(w) b(z) = 1/(w - z) + ...

In fact the second equation follows from the first equation and Fermi statistics. The OPEs of b(z) b(w) and c(z) c(w) have no singular parts. They vanish as z → w.

Finally, we need the stress tensor of the theory. After normal ordering, it is given by T(z) = 2 : ∂c(z) b(z) : + : c(z) ∂b(z) : We will shortly see that with this choice, b and c carry appropriate weights for tensor fields which are neutral under Weyl rescaling.

Primary Fields We will now show that both b and c are primary fields, with weights h = 2 and h = −1 respectively. Let’s start by looking at c. The OPE with the stress tensor is T(z) c(w) = 2 : ∂c(z) b(z) : c(w) + : c(z) ∂b(z) : c(w)

= - 2 ∂c(z)/(z - w) + ... = - c(w)/(z - w)^2 + ∂c(w)/(z - w) + ...

confirming that c has weight −1. When taking the OPE with b, we need to be a little more careful with minus signs. We get T(z) b(w) = 2 : ∂c(z) b(z) : b(w) + : c(z) ∂b(z) : b(w)

= -2 b(z) [ -1/(z - w)^2 ] + 2 b(w)/(z - w) + ∂b(w)/(z - w) + ...

showing that b has weight 2. As we’ve pointed out a number of times, conformal = diffeo + Weyl. We mentioned earlier that the fields b and c are neutral under Weyl transformations.

central under Weyl transformations. This is reflected in their weights, which are due solely to diffeomorphisms as dictated by their index structure: b and c.

The Central Charge Finally, we can compute the TT OPE to determine the central charge of the bc ghost system.

T(z)T(w) = 4 : ∂c(z)b(z):: ∂c(w)b(w): +2 : ∂c(z)b(z):: c(w)∂b(w): +2 : c(z)∂b(z):: ∂c(w)b(w): + : c(z)∂b(z):: c(w)∂b(w): For each of these terms, making two contractions gives a (z−w)−4 contribution to the OPE. There are also two ways to make a single contraction. These give (z −w)−1 or (z −w)−2 or (z −w)−3 contributions depending on what the derivatives hit. The end result is T(z)T(w) = −4 : ∂c(z)b(w): / (z −w)4 + 4 : b(z)∂c(w): / (z −w)2 − 4 : ∂c(z)∂b(w): / (z −w)4 + 2 : b(z)c(w): / (z −w)

− 4 : c(z)b(w): / (z −w)4 − 2 : ∂b(z)∂c(w): / (z −w)3 + 1 : c(z)∂b(w): / (z −w)4 − : ∂b(z)c(w): / (z −w)2 +...

After some Taylor expansions to turn f(z) functions into f(w) functions, together with a little collecting of terms, this can be written as, T(z)T(w) = −13 / (z −w)4 + 2T(w) / (z −w)2 + ∂T(w) / (z −w) +...

The first thing to notice is that it indeed has the form expected of TT OPE. The second, and most important, thing to notice is the central charge of the bc ghost system: it is c = −26.

## 5.3 The Critical “Dimension” of String Theory

Let’s put the pieces together. We’ve learnt that gauge fixing the diffeomorphisms and Weyl gauge symmetries results in the introduction of ghosts which contribute central charge c = −26. We’ve also learnt that the Weyl symmetry is anomalous unless c = 0. Since the Weyl symmetry is a gauge symmetry, it’s crucial that we keep it. We’re forced to add exactly the right degrees of freedom to the string to cancel the contribution from the ghosts.

The simplest possibility is to add D free scalar fields. Each of these contributes c = 1 to the central charge, so the whole procedure is only consistent if we pick D = 26.

This agrees with the result we found in Chapter 2: it is the critical dimension of string theory.

However, there’s no reason that we have to work with free scalar fields. The consistency requirement is merely that the degrees of freedom of the string are described by a CFT with c = 26. Any CFT will do. Each such CFT describes a different background in which a string can propagate. If you like, the space of CFTs with c = 26 can be thought of as the space of classical solutions of string theory.

We learn that the “critical dimension” of string theory is something of a misnomer: it is really a “critical central charge”. Only for rather special CFTs can this central charge be thought of as a spacetime dimension.

For example, if we wish to describe strings moving in 4d Minkowski space, we can take D = 4 free scalars (one of which will be timelike) together with some other c = 22 CFT. This CFT may have a geometrical interpretation, or it may be something more abstract. The CFT with c = 22 is sometimes called the “internal sector” of the theory. It is what we really mean when we talk about the “extra hidden dimensions of string theory”. We’ll see some examples of CFTs describing curved spaces in Section 7.

There’s one final subtlety: we need to be careful with the transition back to Minkowski space. After all, we want one of the directions of the CFT, X0, to have the wrong sign kinetic term. One safe way to do this is to keep X0 as a free scalar field, with the remaining degrees of freedom described by some c = 25 CFT. This doesn’t seem quite satisfactory though since it doesn’t allow for spacetimes which evolve in time — and, of course, these are certainly necessary if we wish to understand early universe cosmology. There are still some technical obstacles to understanding the worldsheet of the string in time-dependent backgrounds. To make progress, and discuss string cosmology, we usually bypass this issue by working with the low-energy effective action which we will derive in Section 7.

5.3.1 The Usual Nod to the Superstring The superstring has another gauge symmetry on the worldsheet: supersymmetry. This gives rise to more ghosts, the so-called βγ system, which turns out to have central charge +11. Consistency then requires that the degrees of freedom of the string have central charge c = 26−11 = 15.

However, now the CFTs must themselves be invariant under supersymmetry, which means that bosons come matched with fermions. If we add D bosons, then we also need to add D fermions. A free boson has c = 1, while a free fermion has c = 1/2. So, the total number of free bosons that we should add is D(1+1/2) = 15, giving us the critical dimension of the superstring: D = 10.

5.3.2 An Aside: Non-Critical Strings Although it’s a slight departure from our main narrative, it’s worth pausing to mention what Polyakov actually did in his four page paper. His main focus was not critical strings, with D = 26, but rather non-critical strings with D ≠ 26. From the discussion above, we know that these suffer from a Weyl anomaly.

namely. But it turns out that there is a way to make sense of the situation. The starting point is to abandon Weyl invariance from the beginning. We start with D free scalar fields coupled to a dynamical worldsheet metric g_{\alpha\beta}. (More generally, we could have any CFT). We still want to keep reparameterization invariance, but now we ignore the constraints of Weyl invariance. Of course, it seems likely that this isn’t going to have too much to do with the Nambu-Goto string, but let’s proceed anyway.

Without Weyl invariance, there is one extra term that it is natural to add to the 2d theory: a worldsheet cosmological constant \mu, S_{non-critical} = \frac{1}{4\pi\alpha'} \int d^2\sigma \sqrt{g} \left( g^{\alpha\beta} \partial_\alpha X^\mu \partial_\beta X_\mu + \mu \right)

Our goal will be to understand how the partition function changes under a Weyl rescaling. There will be two contributions: one from the explicit \mu dependence and one from the Weyl anomaly. Consider two metrics related by a Weyl transformation \hat{g}_{\alpha\beta} = e^{2\omega} g_{\alpha\beta} As we vary \omega, the partition function Z[\hat{g}] changes as \frac{1}{Z} \frac{\partial Z}{\partial \omega} = \frac{1}{Z} \int DX e^{-S} \left( - \frac{\partial S}{\partial \hat{g}_{\alpha\beta}} \frac{\partial \hat{g}_{\alpha\beta}}{\partial \omega} \right)

= \frac{1}{Z} \int DX e^{-S} \left( - \frac{1}{2\pi} \hat{g}^{\alpha\beta} T_{\alpha\beta} \right)

= \frac{c}{24\pi} \sqrt{\hat{g}} \hat{R} - \frac{1}{2\pi\alpha'} \mu e^{2\omega} = \frac{c}{24\pi} \sqrt{g} (R - 2\nabla^2 \omega) - \frac{1}{2\pi\alpha'} \mu e^{2\omega} where, in the last two lines, we used the Weyl anomaly (4.35) and the relationship between Ricci curvatures (1.29). The central charge appearing in these formulae includes the contribution from the ghosts, c = D - 26 We can now just treat this as a differential equation for the partition function Z and solve. This allows us to express the partition function Z[\hat{g}], defined on one worldsheet metric, in terms of Z[g], defined on another. The relationship is, Z[\hat{g}] = Z[g] \exp \left[ - \frac{1}{4\pi\alpha'} \int d^2\sigma \sqrt{g} \left( \frac{c\alpha'}{6} \left( g^{\alpha\beta} \partial_\alpha \omega \partial_\beta \omega + R\omega \right) + 2\mu e^{2\omega} \right) \right]

We see that the scaling mode \omega inherits a kinetic term. It now appears as a new dynamical scalar field in the theory. It is often called the Liouville field on account of the exponential potential term multiplying \mu. Solving this theory is quite hard^7. Notice also that our new scalar field \omega appears in the final term multiplying the Ricci scalar R. We will describe the significance of this in Section 7.2.1. We’ll also see another derivation of this kind of Lagrangian in Section 7.4.4.

## 5.4 States and Vertex Operators

In Chapter 2 we determined the spectrum of the string in flat space. What is the spectrum for a general string background? The theory consists of the b and c ghosts, together with a c = 26 CFT. At first glance, it seems that we have a greatly enlarged Hilbert space since we can act with creation operators from all fields, including the ghosts. However, as you might expect, not all of these states will be physical. After correctly accounting for the gauge symmetry, only some subset survives.

The elegant method to determine the physical Hilbert space in a gauge fixed action with ghosts is known as BRST quantization. You will learn about it in the “Advanced Quantum Field Theory” course where you will apply it to Yang-Mills theory. Although a correct construction of the string spectrum employs the BRST method, we won’t describe it here for lack of time. A very clear description of the general method and its application to the string can be found in Section 4.2 of Polchinski’s book.

Instead, we will make do with a poor man’s attempt to determine the spectrum of the string. Our strategy is to simply pretend that the ghosts aren’t there and focus on the states created by the fields of the matter CFT (i.e. the X^\mu fields if we’re talking about flat space). As we’ll explain in the next section, if we’re only interested in tree-level scattering amplitudes then this will suffice.

To illustrate how to compute the spectrum of the string, let’s go back to flat D = 26 dimensional Minkowski space and the discussion of covariant quantization in Section 2.1. We found that physical states |\Psi\rangle are subject to the Virasoro constraints (2.6) and (2.7) which read L_n |\Psi\rangle = 0 \quad \text{for } n > 0 L_0 |\Psi\rangle = a |\Psi\rangle and similar for \tilde{L}_n, \tilde{L}_n |\Psi\rangle = 0 \quad \text{for } n > 0 \tilde{L}_0 |\Psi\rangle = \tilde{a} |\Psi\rangle where we have, just briefly, allowed for the possibility of different normal ordering coefficients a and \tilde{a} for the left- and right-moving sectors. But there’s a name for states in a conformal field theory obeying these requirements: they are primary states of weight (a, \tilde{a}).

So how do we fix the normal ordering ambiguities a and \tilde{a}? A simple way is to first replace the states with operator insertions on the worldsheet using the state-operator map: |\Psi\rangle \rightarrow \mathcal{O}. But we have a further requirement on the operators \mathcal{O}: gauge invariance. There are two gauge symmetries: reparameterization invariance and Weyl symmetry. Both restrict the possible states.

Let’s start by

^7 A good review can be found in Seiberg’s article “Notes on Quantum Liouville Theory and Quantum Gravity”, Prog. Theor. Phys. Supl. 102 (1990) 319.

considering reparameterization invariance. In the last section, we happily placed operators at specific points on the worldsheet. But in a theory with a dynamical metric, this doesn’t give rise to a diffeomorphism invariant operator. To make an object that is invariant under reparameterizations of the worldsheet coordinates, we should integrate over the whole worldsheet. Our operator insertions (in conformal gauge) are therefore of the form, V ∼ d2z O (5.7)

Here the ∼ sign reflects the fact that we’ve dropped an overall normalization constant which we’ll return to in the next section.

Integrating over the worldsheet takes care of diffeomorphisms. But what about Weyl symmetries? The measure d2z has weight (−1,−1) under rescaling. To compensate, the operator O must have weight (+1,+1). This is how we fix the normal ordering ambiguity: we require a = a˜ = 1. Note that this agrees with the normal ordering coefficient a = 1 that we derived in lightcone quantization in Chapter 2.

This, then, is the rather rough derivation of the string spectrum. The physical states are the primary states of the CFT with weight (+1,+1). The operators (5.7) associated to these states are called vertex operators.

5.4.1 An Example: Closed Strings in Flat Space Let’s use this new language to rederive the spectrum of the closed string in flat space. We start with the ground state of the string, which was previously identified as a tachyon. As we saw in Section 4, the vacuum of a CFT is associated to the identity operator. But we also have the zero modes. We can give the string momentum pµ by acting with the operator eip·X. The vertex operator associated to the ground state of the string is therefore V ∼ d2z : eip·X : (5.8)

tachyon In Section 4.3.3, we showed that the operator eip·X is primary with weight h = h ˜ = α(cid:48)p2/4. But Weyl invariance requires that the operator has weight (+1,+1). This is only true if the mass of the state is M2 ≡ −p2 = − α(cid:48)

This is precisely the mass of the tachyon that we saw in Section 2.

Let’s now look at the first excited states. In covariant quantization, these are of the form ζ αµ α˜ν |0;p(cid:105), where ζ is a constant tensor that determines the type µν −1 −1 µν of state, together with its polarization. (Recall: traceless symmetric ζ corresponds µν to the graviton, anti-symmetric ζ corresponds to the B field and the trace of ζ µν µν µν corresponds to the scalar known as the dilaton). From (4.56), the vertex operator associated to this state is, V ∼ d2z : eip·X ∂Xµ∂ ¯ Xν : ζ (5.9)

excited µν where ∂Xµ gives us a αµ excitation, while ∂ ¯ Xµ gives a α˜µ excitation. It’s easy to −1 −1 check that the weight of this operator is h = h ˜ = 1+α(cid:48)p2/4. Weyl invariance therefore requires that p2 = 0 confirming that the first excited states of the string are indeed massless. However, we still need to check that the operator in (5.9) is actually primary. We know that ∂X is primary and we know that eip·X is primary, but now we want to consider them both sitting together inside the normal ordering. This means that there are extra terms in the Wick contraction which give rise to 1/(z−w)3 terms in the OPE, potentially ruining the primacy of our operator. One such term arises from a double contraction, one of which includes the eip·X operator. This gives rise to an offending term proportional to pµζ . The same kind of contraction with T ¯ gives rise to a term proportional to pνζ .

µν νµ In order for these terms to vanish, the polarization tensor must satisfy pµζ = pνζ = 0 µν µν which is precisely the transverse polarization condition expected for a massless particle.

5.4.2 An Example: Open Strings in Flat Space As explained in Section 4.7, vertex operators for the open-string are inserted on the boundary ∂M of the worldsheet. We still need to ensure that these operators are diffeomorphism invariant which is achieved by integrating over ∂M. The vertex operator for the open string tachyon is V ∼ ds : eip·X : tachyon ∂M We need to figure out the dimension of the boundary operator : eip·X :. It’s not the same as for the closed string. The reason is due to presence of the image charge in the propagator (4.57) for a free scalar field on a space with boundary. This propagator appears in the Wick contractions in the OPEs and affects the weights. Let’s see why this is the case. Firstly, we look at a single scalar field X, ∂X(z) : eipX(w,w¯) : = : X(w,w¯)n−1 : − − +...

(n−1)! 2 z −w 2 z −w¯ iα(cid:48)p ( 1 1 )

= − : eipX(w,w¯) : + +...

2 z −w z −w¯ With this result, we can now compute the OPE with T, α(cid:48)p2 ( 1 1 )2 T(z) : eipX(w,w¯) : = : eipX : + +...

4 z −w z −w¯ When the operator : eipX(w,w¯) : is placed on the boundary w = w¯, this becomes α(cid:48)p2 : eipX(w,w¯) : T(z) : eipX(w,w¯) := +...

(z −w)2 This tells us that the boundary operator : eip·X : is indeed primary with weight α'p².

For the open string, Weyl invariance requires that operators have weight +1 in order to cancel the scaling dimension of −1 coming from the boundary integral ∫ds. So the mass of the open string ground state is M² ≡ −p² = −1/α' in agreement with the mass of the open string tachyon computed in Section 3.

The vertex operator for the photon is V_photon^a ∼ ∫_∂M ds ζ_a : ∂X^a e^{ip·X} : (5.10)

where the index a = 0,...,p now runs only over those directions with Neumann boundary conditions that lie parallel to the brane worldvolume. The requirement that this is a primary operator gives p_a ζ^a = 0, while Weyl invariance tells us that p² = 0. This is the expected behaviour for the momentum and polarization of a photon.

5.4.3 More General CFTs Let’s now consider a string propagating in four-dimensional Minkowski space M, together with some internal CFT with c = 22. Then any primary operator of the internal CFT with weight (h,h̄) can be assigned momentum p^μ, for μ = 0,1,2,3 by dressing the operator with e^{ip·X}. In order to get a primary operator of weight (+1,+1) as required, we must have α'p² = 1−h We see that the mass spectrum of closed string states is given by M² = (h−1)/α' where h runs over the spectrum of primary operators of the internal CFT. Some comments: • Relevant operators in the internal CFT have h < 1 and give rise to tachyons in the spectrum. Marginal operators, with h = 1, give massless particles. And irrelevant operators result in massive states.

• Notice that requiring the vertex operators to be Weyl invariant determines the mass formula for the state. We say that the vertex operators are “on-shell”, in the same sense that external legs of Feynman diagrams are on-shell. We will have more to say about this in the next section.

## 6. String Interactions

So far, despite considerable effort, we’ve only discussed the free string. We now wish to consider interactions. If we take the analogy with quantum field theory as our guide, then we might be led to think that interactions require us to add various non-linear terms to the action. However, this isn’t the case. Any attempt to add extra non-linear terms for the string won’t be consistent with our precious gauge symmetries. Instead, rather remarkably, all the information about interacting strings is already contained in the free theory described by the Polyakov action. (Actually, this statement is almost true).

To see that this is at least feasible, try to draw a cartoon picture of two strings interacting. It looks something like the worldsheet shown in the figure. The worldsheet is smooth. In Feynman diagrams in quantum field theory, information about interactions is inserted at vertices, where different lines meet. Here there are no such points. Locally, every part of the diagram looks like a free propagating string. Only globally do we see that the diagram describes interactions.

## 6.1 What to Compute?

If the information about string interactions is already contained in the Polyakov action, let’s go ahead and compute something! But what should we compute? One obvious thing to try is the probability for a particular configuration of strings at an early time to evolve into a new configuration at some later time. For example, we could try to compute the amplitude associated to the diagram above, stipulating fixed curves for the string ends.

No one knows how to do this. Moreover, there are words that we can drape around this failure that suggests this isn’t really a sensible thing to compute. I’ll now try to explain these words. Let’s start by returning to the familiar framework of quantum field theory in a fixed background. There the basic objects that we can compute are correlation functions, ⟨φ(x₁)...φ(x_n)⟩ (6.1)

After a Fourier transform, these describe Feynman diagrams in which the external legs carry arbitrary momenta. For this reason, they are referred to as off-shell. To get the scattering amplitudes, we simply need to put the external legs on-shell (and perform a few other little tricks captured in the LSZ reduction formula).

The discussion above needs amendment if we turn on gravity. Gravity is a gauge theory and the gauge symmetries are diffeomorphisms. In a gauge theory, only gauge invariant observables make sense. But the correlation function (6.1) is not gauge invariant because its value changes under a diffeomorphism which maps the points x to another point. This emphasizes an important fact: there are no local off-shell gauge invariant observables in a theory of gravity.

There is another way to say this. We know, by causality, that space-like separated operators should commute in a quantum field theory. But in gravity the question of whether operators are space-like separated becomes a dynamical issue and the causal structure can fluctuate due to quantum effects. This provides another reason why we are unable to define local gauge invariant observables.

observables in any theory of quantum gravity. Let’s now return to string theory. Computing the evolution of string configurations for a finite time is analogous to computing off-shell correlation functions in QFT. But string theory is a theory of gravity so such things probably don’t make sense. For this reason, we retreat from attempting to compute correlation functions, back to the S-matrix.

The String S-Matrix The object that we can compute in string theory is the S-matrix. This is obtained by taking the points in the correlation function to infinity: x → ∞. This is acceptable because, just like in the case of QED, the redundancy of the system consists of those gauge transformations which die off asymptotically. Said another way, points on the boundary don’t fluctuate in quantum gravity. (Such fluctuations would be over an infinite volume of space and are suppressed due to their infinite action). So what we’re really going to calculate is a diagram of Figure 32: the type shown in the figure, where all external legs are taken to infinity. Each of these legs can be placed in a different state of the free string and assigned some spacetime momentum p. The resulting expression is the string S-matrix.

Using the state-operator map, we know that each of these states at infinity is equivalent to the insertion of an appropriate vertex operator on the worldsheet. Therefore, to compute this S-matrix element we use a conformal transformation to bring each of these infinite legs to a finite distance. The end result is a worldsheet with the topology of the sphere, dotted with vertex operators where the legs used to be.

However, we already saw in the previous section that the constraint of Weyl invariance meant that vertex operators are necessarily on-shell. Technically, this is the reason that we can only compute on-shell correlation functions in string theory.

6.1.1 Summing Over Topologies Figure 33: The Polyakov path integral instructs us to sum over all metrics. But what about worldsheets of different topologies? In fact, we should also sum over these. It is this sum that gives the perturbative expansion of string theory. The scattering of two strings receives contributions from worldsheets of the form + + + (6.2). The only thing that we need to know is how to weight these different worldsheets. Thankfully, there is a very natural coupling on the string that we have yet to consider and this will do the job. We augment the Polyakov action by S_string = S_Poly + λχ (6.3). Here λ is simply a real number, while χ is given by an integral over the (Euclidean) worldsheet χ = (1/4π) ∫ d²σ √g R (6.4), where R is the Ricci scalar of the worldsheet metric. This looks like the Einstein-Hilbert term for gravity on the worldsheet. It is simple to check that it is invariant under reparameterizations and Weyl transformations.

In four-dimensions, the Einstein-Hilbert term makes gravity dynamical. But life is very different in 2d. Indeed, we’ve already seen that all the components of the metric can be gauged away so there are no propagating degrees of freedom associated to g_αβ. So, in two-dimensions, the term (6.4) doesn’t make gravity dynamical: in fact, classically, it doesn’t do anything at all!

The reason for this is that χ is a topological invariant. This means that it doesn’t actually depend on the metric g_αβ at all – it depends only on the topology of the worldsheet. (More precisely, χ only depends on those global properties of the metric which themselves depend on the topology of the worldsheet). This is the content of the Gauss-Bonnet theorem: the integral of the Ricci scalar R over the worldsheet gives an integer, χ, known as the Euler number of the worldsheet. For a worldsheet without boundary (i.e. for the closed string) χ counts the number of handles h on the worldsheet. It is given by, χ = 2−2h = 2(1−g) (6.5), where g is called the genus of the surface. The simplest examples are shown in the figure. The sphere has g = 0 and χ = 2; the torus has g = 1 and χ = 0. For higher g > 1, the Euler character χ is negative.

Figure 34: Examples of increasingly poorly drawn Riemann surfaces with χ = 2, 0 and −2.

Now we see that the number λ — or, more precisely, e^λ — plays the role of the string coupling. The integral over worldsheets is weighted by, ∫ ∑_topologies ∑_metrics e^{-S_string} ∼ e^{-2λ(1−g)} ∫ DX Dg e^{-S_Poly}. For e^λ << 1, we have a good perturbative expansion in which we sum over all topologies. (In fact, it is an asymptotic expansion, just as in quantum field theory). It is standard to define the string coupling constant as g = e^λ. After a conformal map, tree-level scattering corresponds to a worldsheet with the topology of a sphere: the amplitudes are proportional to 1/g². One-loop scattering corresponds to toroidal worldsheets and, with our normalization, have no power of g. (Although, obviously, these are suppressed by g² relative to tree-level processes). The end result is that the sum over worldsheets in (6.2) becomes a sum over Riemann surfaces of increasing genus, with vertex operators inserted for the initial and final states. The Riemann surface of genus g is weighted by (g²)^{g-1}. While it may look like we’ve introduced a new parameter g into the theory and added the coupling (6.3) by hand, we will later see why this coupling is a necessary part of the theory and provide an interpretation for g.

Scattering Amplitudes We now have all the information that we need to explain how to compute string scattering amplitudes. Suppose that we want to compute the S-matrix for m states: we will label them as Λ_i and assign them spacetime momenta p_i. Each has a corresponding vertex operator V(p_i). The S-matrix element is then computed by evaluating the correlation function in the 2d conformal field theory, with insertions of the vertex operators.

A^{(m)}(Λ_i, p_i) = ∫ DX Dg e^{-S} Poly ∏_{i=1}^m V(p_i) / (g^2 Vol Λ_i)

topologies This is a rather peculiar equation. We are interpreting the correlation functions of a two-dimensional theory as the S-matrix for a theory in D = 26 dimensions!

To properly compute the correlation function, we should introduce the b and c ghosts that we saw in the last chapter and treat them carefully. However, if we’re only interested in tree-level amplitudes, then we can proceed naively and ignore the ghosts. The reason can be seen in the ghost action (5.5) where we see that the ghosts couple only to the worldsheet metric, not to the other worldsheet fields. This means that if our gauge fixing procedure fixes the worldsheet metric completely — which it does for worldsheets with the topology of a sphere — then we can forget about the ghosts. (At least, we can forget about them as soon as we’ve made sure that the Weyl anomaly cancels). However, as we’ll explain in 6.4, for higher genus worldsheets, the gauge fixing does not fix the metric completely and there are residual dynamical modes of the metric, known as moduli, which couple the ghosts and matter fields. This is analogous to the statement in field theory that we only need to worry about ghosts running in loops.

## 6.2 Closed String Amplitudes at Tree Level

The tree-level scattering amplitude is given by the correlation function of the 2d theory, evaluated on the sphere, A^{(m)} = ∫ DX Dg e^{-S} Poly ∏_{i=1}^m V(p_i) / (g^2 Vol Λ_i)

where V(p_i) are the vertex operators associated to the states.

We want to integrate over all metrics on the sphere. At first glance that sounds rather daunting but, of course, we have the gauge symmetries of diffeomorphisms and Weyl transformations at our disposal. Any metric on the sphere is conformally equivalent to the flat metric on the plane. For example, the round metric on the sphere of radius R can be written as ds² = 4R² dz dz̄ / (1 + |z|²)² which is manifestly conformally equivalent to the plane, supplemented by the point at infinity. The conformal map from the sphere to the plane is the stereographic projection. The south pole of the sphere is mapped to the origin; the north pole is mapped to the point at infinity. Therefore, instead of integrating over all metrics, we may gauge fix diffeomorphisms and Weyl transformations to leave ourselves with the seemingly easier task of computing correlation functions on the plane.

6.2.1 Remnant Gauge Symmetry: SL(2,C)

There’s a subtlety. And it’s a subtlety that we’ve seen before: there is a residual gauge symmetry. It is the conformal group, arising from diffeomorphisms which can be undone by Weyl transformations. As we saw in Section 4, there are an infinite number of such conformal transformations. It looks like we have a whole lot of gauge fixing still to do.

However, global issues actually mean that there’s less remnant gauge symmetry than you might think. In Section 4, we only looked at infinitesimal conformal transformations, generated by the Virasoro operators L_n, n ∈ Z. We did not examine whether these transformations are well-defined and invertible over all of space. Let’s take a look at this. Recall that the coordinate changes associated to L_n are generated by the vector fields (4.49), l_n = z^{n+1} ∂_z which result in the shift δz = ε z^{n+1}. This is non-singular at z = 0 only for n ≥ −1. If we restrict to smooth maps, that gets rid of half the transformations right away. But, since we’re ultimately interested in the sphere, we now also need to worry about the point at z = ∞ which, in stereographic projection, is just the north pole of the sphere. To do this, it’s useful to work with the coordinate u = 1/z. The generators of coordinate transformations for the u coordinate are l_n = z^{n+1} ∂_z = ∂_u / u^{n+1} ∂_z = -u^{1-n} ∂_u which is non-singular at u = 0 only for n ≤ 1.

Combining these two results, the only generators of the conformal group that are non-singular over the whole Riemann sphere are l_{-1}, l_0 and l_1 which act infinitesimally as l_{-1}: z → z + ε^{-1} l : z → (1+ε)z l : z → (1+εz)z

The global version of these transformations is l : z → z + α l : z → λz l : z → (1−βz)^{-1}

which can be combined to give the general transformation z → (az + b)/(cz + d) (6.6)

with a, b, c and d ∈ C. We have four complex parameters, but we’ve only got three transformations. What happened? Well, one transformation is fake because an overall scaling of the parameters doesn’t change z. By such a rescaling, we can always insist that the parameters obey ad−bc = 1

The transformations (6.6) subject to this constraint have the group structure SL(2;C), which is the group of 2×2 complex matrices with unit determinant. In fact, since the transformation is blind to a flip in sign of all the parameters, the actual group of global conformal transformations is SL(2;C)/Z, which is sometimes written as PSL(2;C). (This Z subtlety won’t be important for us in what follows).

The remnant global transformations on the sphere are known as conformal Killing vectors and the group SL(2;C)/Z is the conformal Killing group. This group allows us to take any three points on the plane and move them to three other points of our choosing. We will shortly make use of this fact to gauge fix, but for now we leave the SL(2;C) symmetry intact.

6.2.2 The Virasoro-Shapiro Amplitude

We will now compute the S-matrix for closed string tachyons. You might think that this is the least interesting thing to compute: after all, we’re ultimately interested in the superstring which doesn’t have tachyons. This is true, but it turns out that tachyon scattering is much simpler than everything else, mainly because we don’t have a plethora of extra indices on the states to worry about. Moreover, the lessons that we will learn from tachyon scattering hold for the scattering of other states as well.

The m-point tachyon scattering amplitude is given by the flat space correlation function A^{(m)}(p_1,...,p_m) = ∫ DX e^{-S} Poly / (g^2 Vol(SL(2;C))) ∏_{i=1}^m V(p_i)

where the tachyon vertex operator is given by, V(p_i) = g_s ∫ d^2z e^{ip_i·X} ≡ g_s ∫ d^2z V̂(z,p_i) (6.7)

Note that, in contrast to (5.8), we’ve added an appropriate normalization factor to the vertex operator. Heuristically, this reflects the fact that the operator is associated to the addition of a closed string mode. A rigorous derivation of this normalization can be found in Polchinski.

The amplitude can therefore be written as, A^{(m)}(p_1,...,p_m) = (g_s^{m-2} / Vol(SL(2;C))) ∫ ∏_{i=1}^m d^2z_i ⟨V̂(z_1,p_1)...V̂(z_m,p_m)⟩ where the expectation value ⟨...⟩ is computed using the gauge fixed Polyakov action. But the gauge fixed Polyakov action is simply a free theory and our correlation function is something eminently computable: a Gaussian integral, ⟨V̂(z_1,p_1)...V̂(z_m,p_m)⟩ = ∫ DX exp{ - (1/2πα') ∫ d^2z ∂X·∂̄X } exp{ i ∑_{i=1}^m p_i·X(z_i,z̄_i) }

The normalization in front of the Polyakov action is now 1/2πα' instead of 1/4πα' because we’re working with complex coordinates and we need to remember that ∂_σ ∂_α = 4∂∂̄ and d^2z = 2d^2σ.

The Gaussian Integral

We certainly know how to compute Gaussian integrals. Let’s go slow. Consider the following general integral, ∫ DX exp{ (1/2πα') ∫ d^2z X·∂∂̄X + iJ·X } ∼ exp{ (πα'/2) ∫ d^2z d^2z' J(z,z̄) G(z,z';z',z̄') J(z',z̄') }

Here the ∼ symbol reflects the fact that we’ve dropped a whole lot of irrelevant normalization terms, including det^{-1/2}(−∂∂̄). The inverse operator 1/∂∂̄ on the right-hand-side of this equation is shorthand for the propagator G(z,z';z',z̄') which solves ∂∂̄ G(z,z̄;z',z̄') = δ(z−z',z̄−z̄')

As we’ve seen several times before, in two dimensions this propagator is given by G(z,z̄;z',z̄') = (1/2π) ln|z−z'|^2

Back to the Scattering Amplitude

Comparing our scattering amplitude with this general expression, we need to take the source J to be J(z,z̄) = ∑_{i=1}^m p_i δ(z−z_i,z̄−z̄_i)

Inserting this into the Gaussian integral gives us an expression for the amplitude A^{(m)} ∼ (g_s^{m-2} / Vol(SL(2;C))) ∫ ∏_{i=1}^m d^2z_i exp{ (α'/2) ∑_{j,l} p_j·p_l ln|z_j−z_l|^2 }

The terms with j = l seem to be problematic. In fact, they should just be left out. This follows from correctly implementing normal ordering and leaves us with A^{(m)} ∼ (g_s^{m-2} / Vol(SL(2;C))) ∫ ∏_{i=1}^m d^2z_i ∏_{j<l} |z_j−z_l|^{α' p_j·p_l} (6.8)

Actually, there’s something that we missed. (Isn’t there always!). We certainly expect scattering in flat space to obey momentum conservation, so there should be a δ^{(26)}(∑_{i=1}^m p_i) in the amplitude. But where is it? We missed it because we were a little too quick in computing the Gaussian integral. The operator ∂∂ annihilates the zer mode, xµ, in the mode expansion. This means that its inverse, 1/∂∂̄, is not well-defined. But it’s easy to deal with this by treating the zero mode separately. The derivatives ∂² don’t see xµ, but the source J does. Integrating over the zero mode in the path integral gives us our delta function

∫ d^m x exp(i p·x) ∼ δ^26(p)

So, our final result for the amplitude is

A(m) ∼ g^{m-2} s δ^26(p) ∫ d^2z ∏_{i=1}^m ∏_{j<l} |z_j - z_l|^{α' p_j·p_l} / Vol(SL(2;C))

The Four-Point Amplitude

We will compute only the four-point amplitude for two-to-two scattering of tachyons. The Vol(SL(2;C)) factor is there to remind us that we still have a remnant gauge symmetry floating around. Let’s now fix this. As we mentioned before, it provides enough freedom for us to take any three points on the plane and move them to any other three points. We will make use of this to set

z₁ = ∞ , z₂ = 0 , z₃ = z , z₄ = 1

Inserting this into the amplitude (6.9), we find ourselves with just a single integral to evaluate,

A(4) ∼ g² δ^26(p) ∫ d^2z |z|^{α' p₂·p₃} |1−z|^{α' p₃·p₄}

(There is also an overall factor of |z₁|⁴, but this just gets absorbed into an overall normalization constant). We still need to do the integral. It can be evaluated exactly in terms of gamma functions. We relegate the proof to Appendix 6.5, where we show that

∫ d^2z |z|^{2a-2} |1−z|^{2b-2} = 2π Γ(a)Γ(b)Γ(c) / [Γ(1−a)Γ(1−b)Γ(1−c)]

where a+b+c = 1.

Four-point scattering amplitudes are typically expressed in terms of Mandelstam variables. We choose p₁ and p₂ to be incoming momenta and p₃ and p₄ to be outgoing momenta. We then define

s = −(p₁+p₂)² , t = −(p₁+p₃)² , u = −(p₁+p₄)²

These obey

s+t+u = −∑ p_i² = M² = −16/α'

where, in the last equality, we’ve inserted the value of the tachyon mass (2.27). Writing the scattering amplitude (6.10) in terms of Mandelstam variables, we have our final answer

A(4) ∼ g² δ^26(p) Γ(−1−α's/4)Γ(−1−α't/4)Γ(−1−α'u/4) / [Γ(2+α's/4)Γ(2+α't/4)Γ(2+α'u/4)]

This is the Virasoro-Shapiro amplitude governing tachyon scattering in the closed bosonic string.

Remarkably, the Virasoro-Shapiro amplitude was almost the first equation of string theory! (That honour actually goes to the Veneziano amplitude which is the analogous expression for open string tachyons and will be derived in Section 6.3.1). These amplitudes were written down long before people knew that they had anything to do with strings: they simply exhibited some interesting and surprising properties. It took several years of work to realise that they actually describe the scattering of strings. We will now start to tease apart the Virasoro-Shapiro amplitude to see some of the properties that got people hooked many years ago.

6.2.3 Lessons to Learn

So what’s the physics lying behind the scattering amplitude (6.12)? Obviously it is symmetric in s, t and u. That is already surprising and we’ll return to it shortly. But we’ll start by fixing t and looking at the properties of the amplitude as we vary s.

The first thing to notice is that A(4) has poles. Lots of poles. They come from the factor of Γ(−1−α's/4) in the numerator. The first of these poles appears when

−1−α's/4 = 0 ⇒ s = −4/α'

But that’s the mass of the tachyon! It means that, for s close to −4/α', the amplitude has the form of a familiar scattering amplitude in quantum field theory with a cubic vertex,

1/(s−M²)

where M is the mass of the exchanged particle, in this case the tachyon.

Other poles in the amplitude occur at s = 4(n−1)/α' with n ∈ Z+. This is precisely the mass formula for the higher states of the closed string. What we’re learning is that the string amplitude is summing up an infinite number of tree-level field theory diagrams,

∑_{n=0}^∞ 1/(s−M_n²)

where the exchanged particles are all the different states of the free string.

In fact, there’s more information about the spectrum of states hidden within these amplitudes. We can look at the residues of the poles at s = 4(n − 1)/α', for n = 0,1,.... These residues are rather complicated functions of t, but the highest power of momentum that appears for each pole is

A(4) ∼ ∑_{n=0}^∞ t^{2n} / (s−M_n²)

The power of the momentum is telling us the highest spin of the particle states at level n. To see why this is, consider a field corresponding to a spin J particle. It has a whole bunch of Lorentz indices, χ_{μ₁...μ_J}. In a cubic interaction, each of these must be soaked up by derivatives. So we have J derivatives at each vertex, contributing powers of (momentum)^{2J} to the numerator of the Feynman diagram. Comparing with the string scattering amplitude, we see that the highest spin particle at level n has J = 2n. This is indeed the result that we saw from the canonical quantization of the the string in Section 2.

Finally, the amplitude (6.12) has a property that is very different from amplitudes in field theory. Above, we framed our discussion by keeping t fixed and expanding in s. We could just have well done the opposite: fix s and look at poles in t. Now the string amplitude has the interpretation of an infinite number of t-channel scattering amplitudes, one for each state of the string = M. Usually in field theory, we sum up both s-channel and t-channel scattering amplitudes. Not so in string theory. The sum over an infinite number of s-channel amplitudes can be reinterpreted as an infinite sum of t-channel amplitudes. We don’t include both: that would be overcounting. (Similar statements hold for u). The fact that the same amplitude can be written as a sum over s-channel poles or a sum over t-channel poles is sometimes referred to as “duality”. (A much overused word). In the early days, before it was known that string theory was a theory of strings, the subject inherited its name from this duality property of amplitudes: it was called the dual resonance model.

High Energy Scattering

Let’s use this amplitude to see what happens when we collide strings at high energies. There are different regimes that we could look at. The most illuminating is s, t → ∞, with s/t held fixed. In this limit, all the exchanged momenta become large. It corresponds to high-energy scattering with the angle θ between incoming and outgoing particles kept fixed. To see this consider, for example, massless particles (our amplitude is really for tachyons, but the same considerations hold). We take the incoming and outgoing momenta to be

p₁ = (√s/2, √s/2, 0, ...), p₂ = (√s/2, -√s/2, 0, ...)

p₃ = (√s/2, √s/2 cosθ, √s/2 sinθ, ...), p₄ = (√s/2, -√s/2 cosθ, -√s/2 sinθ, ...)

Then we see explicitly that s → ∞ and t → ∞ with the ratio s/t fixed also keeps the scattering angle θ fixed.

We can evaluate the scattering amplitude A(4) in this limit by using Γ(x) ∼ exp(x ln x). We send s → ∞ avoiding the poles. (We can achieve this by sending s → ∞ in a slightly imaginary direction. Ultimately this is valid because all the higher string states are actually unstable in the interacting theory which will shift their poles off the real axis once taken into account). It is simple to check that the amplitude drops off exponentially quickly at high energies,

A(4) ∼ g² δ²⁶(Σpᵢ) exp[ - (α'/2)(s ln s + t ln t + u ln u) ] as s → ∞ (6.14)

The exponential fall-off seen in (6.14) is much faster than the amplitude of any field theory which, at best, fall off with power-law decay at high energies and, at worse, diverge. For example, consider the individual terms (6.13) corresponding to the amplitude for s-channel processes involving the exchange of particles with spin 2n. We see that the exchange of a spin 2 particle results in a divergence in this limit. This is reflecting something you already know about gravity: the dimensionless coupling is G E² (in four-dimensions) which becomes large for large energies. The exchange of higher spin particles gives rise to even worse divergences. If we were to truncate the infinite sum (6.13) at any finite n, the whole thing would diverge. But infinite sums can do things that finite sums can’t and the final behaviour of the amplitude (6.14) is much softer than any of the individual terms. The infinite number of particles in string theory conspire to render finite any divergence arising from an individual particle species.

Phrased in terms of the s-channel exchange of particles, the high-energy behaviour of string theory seems somewhat miraculous. But there is another viewpoint where it’s all very obvious. The power-law behaviour of scattering amplitudes is characteristic of point-like charges. But, of course, the string isn’t a point-like object. It is extended and fuzzy at length scales comparable to α'. This is the reason the amplitude has such soft high-energy behaviour. Indeed, this idea that smooth extended objects give rise to scattering amplitudes that decay exponentially at high energies is something that you’ve seen before in non-relativistic quantum mechanics. Consider, for example, the scattering of a particle off a Gaussian potential. In the Born approximation, the differential cross-section is just given by the Fourier transform which is again a Gaussian, now decaying exponentially for large momentum.

It’s often said that theories of quantum gravity should have a “minimum length”, sometimes taken to be the Planck scale. This is roughly true in string theory, although not in any crude simple manner. Rather, the minimum length reveals itself in different ways depending on which question is being asked. The above discussion highlights one example of this: strings can’t probe distance scales shorter than l = √α' simply because they are themselves fuzzy at this scale. It turns out that D-branes are much better probes of sub-stringy physics and provide a different view on the short distance structure of space.

cetime. We will also see another manifestation of the minimal length scale of string theory in Section 8.3.

Graviton Scattering Although we’ve derived the result (6.14) for tachyons, all tree-level amplitudes have this soft fall-off at high-energies. Most notably, this includes graviton scattering. As we noted above, this is in sharp contrast to general relativity for which tree-level scattering amplitudes diverge at high-energies. This is the first place to see that UV problems of general relativity might have a good chance of being cured in string theory.

Using the techniques described in this section, one can compute m-point tree-level amplitudes for graviton scattering. If we restrict attention to low-energies (i.e. much smaller than 1/ α(cid:48)), one can show that these coincide with the amplitudes derived from the Einstein-Hilbert action in D = 26 dimensions S = 1/(2κ²) ∫ d²⁶X √(-G) R where R is the D = 26 Ricci scalar (not to be confused with the worldsheet Ricci scalar which we call R). The gravitational coupling, κ² is related to Newton’s constant in 26 dimensions. It plays no role for pure gravity, but is important when we couple to matter. We’ll see shortly that it’s given by κ² ≈ g²(α(cid:48))¹² We won’t explicitly compute graviton scattering amplitudes in this course, partly because they’re fairly messy and partly because building up the Einstein-Hilbert action from m-particle scattering is hardly the best way to look at general relativity. Instead, we shall derive the Einstein-Hilbert action in a much better fashion in Section 7.

## 6.3 Open String Scattering

So far our discussion has been entirely about closed strings. There is a very similar story for open strings. We again compute S-matrix elements. Conformal symmetry now maps tree-level scattering to the disc, with vertex operators inserted on the boundary of the disc.

For the open string, the string coupling constant that we add to the Polyakov action requires the addition of a boundary term to make it well defined, χ = 1/(4π) ∫ d²σ √g R + 1/(2π) ∫_∂M ds k (6.15)

where k is the geodesic curvature of the boundary. To define it, we introduce two unit vectors on the worldsheet: tα is tangential to the boundary, while nα is normal and points outward from the boundary. The geodesic curvature is defined as k = −tα nβ ∇α tβ Boundary terms of the type seen in (6.15) are also needed in general relativity for manifolds with boundaries: in that context, they are referred to as Gibbons-Hawking terms.

The Gauss-Bonnet theorem has an extension to surfaces with boundary. For surfaces with h handles and b boundaries, the Euler character is given by χ = 2−2h−b Some examples are shown in Figure 38. The expansion for open-string scattering consists of adding consecutive boundaries to the worldsheet. The disc is weighted by 1/gₛ; the annulus has no factor of gₛ and so on. We see that the open string coupling is related to the closed string coupling by g_open² = gₛ (6.16)

One of the key steps in computing closed string scattering amplitudes was the implementation of the conformal Killing group, which was defined as the surviving gauge symmetry with a global action on the sphere. For the open string, there is again a residual gauge symmetry. If we think in terms of the upper-half plane, the boundary is Imz = 0. The conformal Killing group is composed of transformations z → (az + b)/(cz + d)

again with the requirement that ad−bc = 1. This time there is one further condition: the boundary Imz = 0 must be mapped onto itself. This requires a,b,c, d ∈ R. The resulting conformal Killing group is SL(2;R)/Z₂.

6.3.1 The Veneziano Amplitude Since vertex operators now live on the boundary, they have a fixed ordering. In computing a scattering amplitude, we must sum over all orderings. Let’s look again at the 4-point amplitude for tachyon scattering. The vertex operator is V(pᵢ) = gₛ ∫ dx e^(ipᵢ·X)

where the integral ∫ dx is now over the boundary and p² = 1/α(cid:48) is the on-shell condition for an open-string tachyon. The normalization gₛ is that appropriate for the insertion of an open-string mode, reflecting (6.16).

Going through the same steps as for the closed string, we find that the amplitude is given by A(4) ∼ gₛ² / Vol(SL(2;R)) ∫⁴ ∏ᵢ dxᵢ δ²⁶(∑ pᵢ) ∏_{j<l} |xⱼ − xₗ|^(2α(cid:48)pⱼ·pₗ) (6.17)

Note that there’s a factor of 2 in the exponent, differing from the closed string expression (6.8). This comes about because the boundary propagator (4.57) has an extra factor of 2 due to the image charge.

We now use the SL(2;R) residual gauge symmetry to fix three points on the boundary. We choose a particular ordering and set x₁ = 0, x₂ = x, x₃ = 1 and x₄ → ∞. The only free insertion point is x₂ = x but, because of the restriction of operator ordering, this must lie in the interval x ∈ [0,1].

The interesting part of the integral is then given by ∫₁⁰ A(4) ∼ g dx |x|²α'p₁·p₂|1−x|²α'p₂·p₃ This integral is well known: as shown in Appendix 6.5, it is the Euler beta function B(a,b) = ∫₀¹ dx xᵃ⁻¹(1−x)ᵇ⁻¹ = Γ(a)Γ(b)/Γ(a+b)

After summing over the different orderings of vertex operators, the end result for the amplitude for open string tachyon scattering is, A(4) ∼ g [B(−α's−1,−α't−1)+B(−α's−1,−α'u−1)+B(−α't−1,−α'u−1)]

This is the famous Veneziano Amplitude, first postulated in 1968 to capture some observed features of the strong interactions. This was before the advent of QCD and before it was realised that the amplitude arises from a string.

The open string scattering amplitude contains the same features that we saw for the closed string. For example, it has poles at s = (n−1)/α' = 0,1,2,...

which we recognize as the spectrum of the open string.

6.3.2 The Tension of D-Branes Recall that we introduced D-branes as surfaces in space on which strings can end. At the time, I promised that we would eventually discover that these D-branes are dynamical objects in their own right. We’ll look at this more closely in the next section, but for now we can do a simple computation to determine the tension of D-branes.

The tension T of a Dp-brane is defined as the energy per spatial volume. It has dimension [T] = p+1. The tension is telling us the magnitude of the coupling between the brane and gravity. Or, in our new language, the strength of the interaction between a closed string state and an open string. The simplest such diagram is shown in the figure, with a graviton vertex operator inserted. Although we won’t compute this diagram completely, we can figure out its most important property just by looking at it: it has the topology of a disc, so is proportional to 1/g. Adding powers of α' to get the dimension right, the tension of a Dp-brane must scale as T ∼ 1/(g l_s^{p+1}) (6.18)

where the string length is defined as l_s = √α'. The 1/g scaling of the tension is one of the key characteristic features of a D-brane.

I should confess that there’s a lot swept under the carpet in the above discussion, not least the question of the correct normalization of the vertex operators and the difference between the string frame and the Einstein frame (which we will discuss shortly). Nonetheless, the end result (6.18) is correct. For a fuller discussion, see Section 8.7 of Polchinski.

## 6.4 One-Loop Amplitudes

We now return to the closed string to discuss one-loop effects. As we saw above, this corresponds to a worldsheet with the topology of a torus. We need to integrate over all metrics on the torus.

For tree-level processes, we used diffeomorphisms and Weyl transformations to map an arbitrary metric on the sphere to the flat metric on the plane. This time, we use these transformations to map an arbitrary metric on the torus to the flat metric on the torus. But there’s a new subtlety that arises: not all flat metrics on the torus are equivalent.

6.4.1 The Moduli Space of the Torus Let’s spell out what we mean by this. We can construct a torus by identifying a region in the complex z-plane as shown in the figure. In general, this identification depends on a single complex parameter, τ ∈ C.

z ≡ z + 2π and z ≡ z + 2πτ Do not confuse τ with the Minkowski worldsheet time: we left that behind way back in Section 3. Everything here is Euclidean worldsheet and τ is just a parameter telling us how skewed the torus is. The flat metric on the torus is now simply ds² = dzdz̄ subject to the identifications above.

A general metric on a torus can always be transformed to a flat metric for some value of τ. But the question that interests us is whether two tori, parameterized by different τ, are conformally equivalent. In general, the answer is no. The space of conformally inequivalent tori, parameterized by τ, is called the moduli space M.

However, there are some values of τ that do correspond to the same torus. In particular, there are a couple of obvious ways in which we can change τ without changing the torus. They go by the names of the S and T transformations: • T : τ → τ+1: This clearly gives rise to the same torus, because the identification is now z ≡ z + 2π and z ≡ z + 2π(τ+1) ≡ z + 2πτ • S : τ → −1/τ: This simply flips the sides of the torus. For example, if τ = ia is purely imaginary, then this transformation maps τ → i/a, which can then be undone by a scaling.

It turns out that these two changes S and T are the only ones that keep the torus intact. They are sometimes called modular transformations. A general modular transformation is constructed from combinations of S and T and takes the form, τ → (aτ + b)/(cτ + d) with ad−bc = 1 (6.19)

where a, b, c and d ∈ Z. This is the group SL(2,Z). (In fact, we have our usual Z identification and the group is actually PSL(2,Z) = SL(2,Z)/Z₂). The moduli space M of the torus is given by M = C/SL(2;Z)

What does this space look like? Using T : τ → τ +1, we can always shift τ until it lies within the interval Reτ ∈ [−1,+1 ]

2 2 where the edges of the interval are identified. Meanwhile, S : τ → −1/τ inverts the – 146 – Figure 41: The fundamental domain.

modulus|τ|, sowecanusethistomapapointinsidethecircle|τ| < 1toapointoutside |τ| > 1. One can show that by successive combinations of S and T, it is possible to map any point to lie within the shaded region shown in the figure, defined by |τ| ≥ 1 and Reτ ∈ [−1,+1 ]

2 2 This is referred to as the fundamental domain of SL(2;Z).

We could have just as easily chosen one of the other fundamental domains shown in the figure. But the shaded region is the standard one.

Integrating over the Moduli Space In string theory we’re invited to sum over all metrics. After gauge fixing diffeomor- phismsandWeylinvariance, westillneedtointegrateoverallinequivalenttori. Inother words, weintegrateoverthefundamentaldomain. TheSL(2;Z)invariantmeasureover the fundamental domain is (cid:90) d2τ (Imτ)2 To see that this is SL(2;Z) invariant, note that under a general transformation of the form (6.19) we have d2τ Imτ d2τ → and Imτ → |cτ +d|4 |cτ +d|2 – 147 – There’s some physics lurking within these rather mathematical statements. The inte- gration over the fundamental domain in string theory is analogous to the loop integral over momentum in quantum field theory. Consider the square tori defined by Reτ = 0.

The tori with Imτ → ∞ are squashed and chubby. They correspond to the infra-red region of loop momenta in a Feynman diagram. Those with Imτ → 0 are long and thin. Those correspond to the ultra-violet limit of loop momenta in a Feynman dia- gram. Yet, as we have seen, we should not integrate over these UV regions of the loop since the fundamental domain does not stretch down that far. Or, more precisely, the thin tori are mapped to chubby tori. This corresponds to the fact that any putative UV divergence of string theory can always be reinterpreted as an IR divergence. This is the second manifestation of the well-behaved UV nature of string theory. We will see this more explicitly in the example of Section 6.4.2.

Finally, when computing a loop amplitude in string theory, we still need to worry about the residual gauge symmetry that is left unfixed after the map to the flat torus.

In the case of tree-level amplitudes on the sphere, this residual gauge symmetry was due to the conformal Killing group SL(2;C). For the torus, the conformal Killing group is generated by the obvious generators ∂ and ∂ . It is U(1)×U(1).

z z¯ Higher Genus Surfaces The moduli space M of the Riemann surface of genus g > 1 can be shown to have dimension, dimM = 3g −3 There are no conformal Killing vectors when g > 1. These facts can be demonstrated as an application of the Riemann-Roch theorem. For more details, see section 5.2 of Polchinski, or sections 3.3 and 8.2 of Green, Schwarz and Witten.

6.4.2 The One-Loop Partition Function We won’t compute any one-loop scattering amplitudes in string theory. Instead, we will look at something a little simpler: the one-loop vacuum to vacuum amplitude.

A Euclidean worldsheet with periodic time has the interpretation of a finite temper- ature partition function for the theory defined on a cylinder. In D = 26 dimensional spacetime, it is related to the cosmological constant in bosonic string theory.

Consider firstly the partition function of a theory on a square torus, with Reτ = 0.

Compactifying Euclidean time, with period (Imτ) is equivalent to putting the theory at temperature T = 1/(Imτ), Z[τ] = Tr e−2π(Imτ)H – 148 – where the Tr is over all states in the theory. For any CFT defined on a cylinder, the Hamiltonian given by c+c˜ H = L +L − 0 0 where the final term is the Casimir energy computed in Section 4.4.1.

What then is the interpretation of the vacuum amplitude Im(z)

computed on a torus with Reτ (cid:54)= 0? From the diagram, we see that the effect of such a skewed torus is to trans- 2πτ late a given point around the cylinder by Reτ. But we know which operator implements such a translation: it is exp(2πi(Reτ)P), where P is the momentum operator on Re(z)

2π the cylinder. After the map to the plane, this becomes the rotation operator Figure 42: P = L −L 0 0 So the vacuum amplitude on the torus has the interpretation of the sum over all states in the theory, weighted by Z[τ] = Tr e−2π(Imτ)(L0+L˜ 0)e−2πi(Reτ)(L0−L˜ 0)e2π(Imτ)(c+c˜)/24 We define q = e2πiτ , q¯= e−2πiτ¯ The partition function can then be written in slick notation as Z[τ] = Tr qL0−c/24 q¯L˜ 0−c˜/24 Let’s compute this for the free string. We know that each scalar field X decomposes into a zero mode and an infinite number harmonic oscillator modes α which create −n states of energy n. We’ll deal with the zero mode shortly but, for now, we focus on the oscillators. Acting d times with the operator α creates states with energy dn. This −n gives a contribution to TrqL0 of the form (cid:88) 1 qnd = But the Fock space of a single scalar field is built by acting with oscillator modes n ∈ Z+. Including the central charge, c = 1, the contribution from the oscillator modes of a single scalar field is therefore Tr q^{L_0 - c/24} = ∏_{n=1}^∞ 1/(q^{1/24} (1 - q^n))

There is a similar expression from the q̄^{L̃_0 - c̃/24} sector. We’re still left with the contribution from the zero mode p of the scalar field. The contribution to the energy H of the state on the worldsheet is ∫ dσ (α' p)^2 / (4π α') = α' p^2 / 2

The trace in the partition function requires us to sum over all states, which gives ∫ dp e^{-π α' (Im τ) p^2} / (2π) ∼ 1 / √(α' Im τ)

So, including both the zero mode and oscillators, we get the partition function for a single free scalar field, Z_scalar[τ] ∼ 1 / √(α' Im τ) * (q q̄)^{1/24} ∏_{n=1}^∞ 1/(1 - q^n) ∏_{n=1}^∞ 1/(1 - q̄^n)   (6.20)

where I haven’t been careful to keep track of constant factors.

To build the string partition function, we should really work in covariant quantization and include the ghost fields. Here we’ll cheat and work in lightcone gauge. This is dodgy because, if we do it honestly, much of the physics gets pushed to the p^+ = 0 limit of the lightcone momentum where the gauge choice breaks down. So instead we’ll do it dishonestly.

In lightcone gauge, we have 24 oscillator modes. But we have 26 zero modes. (You may worry that we still have to impose level matching...this is the dishonest part of the calculation. We’ll see partly where it comes from shortly). Finally, there’s a couple of extra steps. We need to divide by the volume of the conformal Killing group. This is just U(1)×U(1), acting by translations along the cycles of the torus. The volume is just Vol = 4π^2 Im τ. Finally, we also need to integrate over the moduli space of the torus. Our final result, neglecting all constant factors, is Z_string = ∫ d^2τ (1/(Im τ)) * (1/(α' Im τ))^{13} * (q q̄)^{24} ∏_{n=1}^∞ 1/(1 - q^n) ∏_{n=1}^∞ 1/(1 - q̄^n)   (6.21)

Modular Invariance

The function appearing in the partition function for the scalar field has a name: it is the inverse of the Dedekind eta function η(q) = q^{1/24} ∏_{n=1}^∞ (1 - q^n)

It was studied in the 1800s by mathematicians interested in the properties of functions under modular transformations T : τ → τ + 1 and S : τ → −1/τ. The eta-function satisfies the identities η(τ + 1) = e^{2πi/24} η(τ) and η(−1/τ) = −i τ η(τ)

These two statements ensure that the scalar partition function (6.20) is a modular invariant function. Of course, that kinda had to be true: it follows from the underlying physics.

Written in terms of η, the string partition function (6.21) takes the form Z_string = ∫ d^2τ (1/(Im τ)^2) * (1/√(Im τ)) * (1/(η(q) η̄(q̄)))^{24}

Both the measure and the integrand, are individually modular invariant.

6.4.3 Interpreting the String Partition Function

It’s probably not immediately obvious what the string partition function (6.21) is telling us. Let’s spend some time trying to understand it in terms of some simpler concepts.

We know that the free string describes an infinite number of particles with mass m^2 = 4(n − 1)/α', n = 0,1,.... The string partition function should just be a sum over vacuum loops of each of these particles. We’ll now show that it almost has this interpretation.

Firstly, let’s figure out what the contribution from a single particle would be? We’ll consider a free massive scalar field φ in D dimensions. The partition function is given by, Z = ∫ Dφ exp(−∫ d^Dx φ(−∂^2 + m^2)φ) ∼ det^{−1/2}(−∂^2 + m^2)

= exp(1/2 ∫ d^Dp/(2π)^D ln(p^2 + m^2))

This is the partition function of a field theory. It contains vacuum loops for all numbers of particles. To compare to the string partition function, we want the vacuum amplitude for just a single particle. But that’s easy to extract. We write the field theory partition function as, Z = exp(Z) = ∑_{n=0}^∞ Z^n / n!

Each term in the sum corresponds to n particles propagating in a vacuum loop, with the n! factor taking care of Bosonic statistics. So the vacuum amplitude for a single, free massive particle is simply Z_1 = 1/2 ∫ d^Dp/(2π)^D ln(p^2 + m^2)

Clearly this diverges in the UV range of the integral, p → ∞. There’s a nice way to rewrite this integral using something known as Schwinger parameterization. We make use of the identity ∫_0^∞ dl e^{-x l} = 1/x  ⇒  ∫_0^∞ dl e^{-x l} = −ln x

We then write the single particle partition function as Z_1 = ∫ d^Dp/(2π)^D ∫_0^∞ dl/(2l) e^{-(p^2 + m^2)l}   (6.22)

It’s worth mentioning that there’s another way to see that this is the single particle partition function that is a little closer in spirit to the method we used in string theory. We could start with the einbein form of the relativistic particle action (1.8). After fixing the gauge to e = 1, the exponent in (6.22) is the energy of the particle traversing a loop of length l. The integration measure dl/l sums over all possible sizes of loops.

We can happily perform the d^D p integral in (6.22). Ignoring numerical factors, we have Z = ∫_0^∞ dl e^{-m^2 l} / l^{1+D/2}  (6.23)

Note that the UV divergence as p → ∞ has metamorphosised into a divergence associated to small loops as l → 0.

Equation (6.23) gives the answer for a single particle of mass m. In string theory, we expect contributions from an infinite number of species of particles of mass m_n. Specializing to D = 26, we expect the partition function to be Z = ∫_0^∞ dl / l^{14} ∑_{n=0}^∞ e^{-m_n^2 l} But we know that the mass spectrum of the free string: it is given in terms of the L_0 and \tilde{L}_0 operators by m^2 = (4/α')(L_0 - 1) = (4/α')(\tilde{L}_0 - 1) = (4/α')(L_0 + \tilde{L}_0 - 2)

subject to the constraint of level matching, L_0 = \tilde{L}_0. It’s easy to impose level matching: we simply throw in a Kronecker delta in its integral representation, (1/2π) ∫_{-1/2}^{+1/2} ds e^{2πi s (L_0 - \tilde{L}_0)} = δ_{L_0, \tilde{L}_0}  (6.24)

Replacing the sum over species, with the trace over the spectrum of states subject to level matching, the partition function becomes, Z = ∫_0^∞ dl / l^{14} ∫_{-1/2}^{+1/2} ds Tr e^{2πi s (L_0 - \tilde{L}_0)} e^{-2(L_0 + \tilde{L}_0 - 2)l/α'}  (6.25)

We again use the definition q = exp(2πiτ), but this time the complex parameter τ is a combination of the length of the loop l and the auxiliary variable that we introduced to impose level matching, τ = s + 2li/α' The trace over the spectrum of the string once gives the eta-functions, just as it did before. We’re left with the result for the partition function, Z_string = ∫ d^2τ / (Imτ)^2 (1/Imτ) |η(q)|^{24} But this is exactly the same expression that we saw before. With a difference! In fact, the difference is hidden in the notation: it is the range of integration for d^2τ which can be found in the original expressions (6.23) and (6.24). Reτ runs over the same interval [-1/2, +1/2] that we saw in string theory. As is clear from this discussion, it is this integral which implements level matching. The difference comes in the range of Imτ which, in this naive analysis, runs over [0,∞). This is in stark contrast to string theory where we only integrate over the fundamental domain.

This highlights our previous statement: the potential UV divergences in field theory are encountered in the region Imτ ∼ l → 0. In the above analysis, this corresponds to particles traversing small loops. But this region is simply absent in the correct string theory computation. It is mapped, by modular invariance, to the infra-red region of large loops.

It is often said that in the g → 0 limit string theory becomes a theory of an infinite number of free particles. This is true of the spectrum. But this calculation shows that it’s not really true when we compute loops because the modular invariance means that we integrate over a different range of momenta in string theory than in a naive field theory approach.

So what happens in the infra-red region of our partition function? The easiest place to see it is in the l → ∞ limit of the integral (6.25). We see that the integral is dominated by the lightest state which, for the bosonic string is the tachyon. This has m^2 = -4/α', or (L_0 + \tilde{L}_0 - 2) = -2. This gives a contribution to the partition function of, ∫_0^∞ dl e^{+4l/α'} / l^{14} which clearly diverges. This IR divergence of the one-loop partition function is another manifestation of tachyonic trouble. In the superstring, there is no tachyon and the IR region is well-behaved.

So is String Theory Finite?

The honest answer is that we don’t know. The UV finiteness that we saw above holds for all one-loop amplitudes. This means, in particular, that we have a one-loop finite theory of gravity interacting with matter in higher dimensions. This is already remarkable.

There is more good news: One can show that UV finiteness continues to hold at the two-loops. And, for the superstring, state-of-the-art techniques using the “pure-spinor” formalism show that certain objects remain finite up to five-loops. Moreover, the exponential suppression (6.14) that we saw when all momentum exchanges are large continues to hold for all amplitudes.

However, no general statement of finiteness has been proven. The danger lurks in the singular points in the integration over Riemann surfaces of genus 3 and higher.

Beyond Perturbation Theory?

From the discussion in this section, it should be clear that string perturbation theory is entirely analogous to the Feynman diagram expansion in field theory. Just as in field theory, one can show that the expansion in g is asymptotic. This means that the series does not converge, but we can nonetheless make sense of it.

However, we know that there are many phenomena in quantum field theory that aren’t captured by Feynman diagrams. These include confinement in the strongly coupled regime and instantons and solitons in the weakly coupled regime. Does this mean that we are missing similarly interesting phenomena in string theory?

ory? The answer is almost certainly yes! In this section, I’ll very briefly allude to a couple of more advanced topics which allow us to go beyond the perturbative expansion in string theory. The goal is not really to teach you these things, but merely to familiarize you with some words.

One way to proceed is to keep quantum field theory as our guide and try to build a non-perturbative definition of string theory in terms of a path integral. We’ve already seen that the Polyakov path integral over worldsheets is equivalent to Feynman diagrams. So we need to go one step further. What does this mean? Recall that in QFT, a field creates a particle. In string theory, we are now looking for a field which creates a loop of string. We should have a different field for each configuration of the string. In other words, our field should itself be a function of a function: Φ(Xµ(σ)). Needless to say, this is quite a complicated object. If we were brave, we could then consider the path integral for this field, Z = DΦ eiS[Φ(X(σ))]

for some suitable action S[Φ]. The idea is that this path integral should reproduce the perturbative string expansion and, furthermore, defines a non-perturbative completion of the theory. This line of ideas is known as string field theory. It should be clear that this is one step further in the development: particles → fields → string fields. Or, in more historical language, if field theory is “second quantization”, then string field theory is “third quantization”.

String field theory has been fairly successful for the open string and some interesting non-perturbative results have been obtained in this manner. However, for the closed string this approach has been much less useful. It is usually thought that there are deep reasons behind the failure of closed string field theory, related to issues that we mentioned at the beginning of this section: there are no off-shell quantities in a theory of gravity. Moreover, we mentioned in Section 4 that a theory of interacting open strings necessarily includes closed strings, so somehow the open string field theory should already contain gravity and closed strings. Quite how this comes about is still poorly understood.

There are other ways to get a handle on non-perturbative aspects of string theory using the low-energy effective action (we will describe what the “low-energy effective action” is in the next section). Typically these techniques rely on supersymmetry to provide a window into the strongly coupled regime and so work only for the superstring. These methods have been extremely successful and any course on superstring theory would be devoted to explaining various aspects of such as dualities and M-theory.

Finally, in asymptotically AdS spacetimes, the AdS/CFT correspondence gives a non-perturbative definition of string theory and quantum gravity in the bulk in terms of Yang-Mills theory, or something similar, on the boundary. In some sense, the boundary field theory is a “string field theory”.

## 6.5 Appendix: Games with Integrals and Gamma Functions

The gamma function is defined by the integral representation Γ(z) = ∫_0^∞ dt t^{z-1}e^{-t} (6.26)

which converges if Re z > 0. It has a unique analytic expression to the whole z-plane. The absolute value of the gamma function over the z-plane is shown in the figure. Figure 43:

The gamma function has a couple of important properties. Firstly, it can be thought of as the analytic continuation of the factorial function for positive integers, meaning Γ(n) = (n−1)! n ∈ Z^+ Secondly, Γ(z) has poles at non-positive integers. More precisely when z ≈ −n, with n = 0,1,..., there is the expansion Γ(z) ≈ (−1)^n / (n! (z + n))

The Euler Beta Function

The Euler beta function is defined for x, y ∈ C by B(x,y) = Γ(x)Γ(y) / Γ(x+y)

It has the integral representation B(x,y) = ∫_0^1 dt t^{x-1}(1−t)^{y-1} (6.27)

Let’s prove this statement. We start by looking at Γ(x)Γ(y) = ∫_0^∞ du ∫_0^∞ dv e^{-u}u^{x-1}e^{-v}v^{y-1} We write u = a^2 and v = b^2 so the integral becomes Γ(x)Γ(y) = 4 ∫_0^∞ da ∫_0^∞ db e^{-(a^2+b^2)}a^{2x-1}b^{2y-1} = ∫_{-∞}^∞ da ∫_{-∞}^∞ db e^{-(a^2+b^2)}|a|^{2x-1}|b|^{2y-1} We now change coordinates once more, this time to polar a = r cos θ and b = r sin θ. We get Γ(x)Γ(y) = ∫_0^∞ r dr e^{-r^2} r^{2x+2y-2} ∫_0^{2π} dθ |cos θ|^{2x-1}|sin θ|^{2y-1} = Γ(x+y) × 4 ∫_0^{π/2} dθ (cos θ)^{2x-1}(sin θ)^{2y-1} = Γ(x+y) ∫_0^1 dt (1−t)^{y-1}t^{x-1} where, in the final line, we made the substitution t = cos^2 θ. This completes the proof.

The Virasoro-Shapiro Amplitude

In the closed string computation, we came across the integral C(a,b) = ∫ d^2z |z|^{2a-2}|1−z|^{2b-2} We will now evaluate this and show that it is given by (6.11). We start by using a trick. We can write |z|^{2a-2} = (1 / Γ(1−a)) ∫_0^∞ dt t^{-a}e^{-|z|^2 t} which follows from the definition (6.26) of the gamma function. Similarly, we can write |1−z|^{2b-2} = (1 / Γ(1−b)) ∫_0^∞ du u^{-b}e^{-|1−z|^2 u} We decompose the complex coordinate z = x+iy, so that the measure of the integral is d^2z.

= 2dxdy. We can then write the integral C(a,b) as ∫ d2zdudt C(a,b) = t−au−be−|z|2te−|1−z|2u Γ(1−a)Γ(1−b)

∫ dxdydudt = 2 t−au−be−(t+u)(x2+y2)+2xu−u Γ(1−a)Γ(1−b)

∫ dxdydudt ( u )2 u2 = 2 t−au−b exp −(t+u) x− +y2 −u+ Γ(1−a)Γ(1−b) t+u t+u Now we do the dxdy integral which is simply Gaussian. We find 2π ∫ ∞ t−au−b C(a,b) = dudt e−tu/(t+u)

Γ(1−a)Γ(1−b) t+u Finally, we make a change of variables. We write t = αβ and u = (1−β)α. In order for t and u to take values in the range [0,∞), we require α ∈ [0,∞) and β ∈ [0,1].

Taking into account the Jacobian arising from this transformation, which is simply α, the integral becomes 2π ∫ α1−a−b C(a,b) = dαdβ β−a(1−β)−be−αβ(1−β)

Γ(1−a)Γ(1−b) α But we recognize the integral over dα: it is simply ∫ ∞ dα α−a−be−βα(1−β) = [β(1−β)]a+b−1Γ(1−a−b)

We write c = 1−a−b. Finally, we’re left with 2πΓ(c) ∫ 1 C(a,b) = dβ (1−β)a−1βb−1 Γ(1−a)Γ(1−b)

But the final integral is the Euler beta function (6.27). This gives us our promised result, 2πΓ(a)Γ(b)Γ(c)

C(a,b) = Γ(1−a)Γ(1−b)Γ(1−c)

## 7. Low Energy Effective Actions

So far, we’ve only discussed strings propagating in flat spacetime. In this section we will consider strings propagating in different backgrounds. This is equivalent to having different CFTs on the worldsheet of the string.

There is an obvious generalization of the Polyakov action to describe a string moving in curved spacetime, ∫ 1 √ S = d2σ g gαβ∂ Xµ∂ Xν G (X) (7.1)

4πα’ α β µν Here g is again the worldsheet metric. This action describes a map from the world- αβ sheet of the string into a spacetime with metric G (X). (Despite its name, this metric µν is not to be confused with the Einstein tensor which we won’t have need for in this lecture notes).

Actions of the form (7.1) are known as non-linear sigma models. (This strange name has its roots in the history of pions). In this context, the D-dimensional spacetime is sometimes called the target space. Theories of this type are important in many aspects of physics, from QCD to condensed matter.

Although it’s obvious that (7.1) describes strings moving in curved spacetime, there’s something a little fishy about just writing it down. The problem is that the quantization of the closed string already gave us a graviton. If we want to build up some background metric G (X), it should be constructed from these gravitons, in much the same manner µν that a laser beam is made from the underlying photons. How do we see that the metric in (7.1) has anything to do with the gravitons that arise from the quantization of the string?

The answer lies in the use of vertex operators. Let’s expand the metric as a small fluctuation around flat space G (X) = δ +h (X)

µν µν µν Then the partition function that we build from the action (7.1) is related to the partition function for a string in flat space by ∫ ∫ Z = DXDg e−S Poly −V = DXDg e−S Poly(1−V + V2 +...)

where S is the action for the string in flat space given in (1.22) and V is the Poly expression ∫ 1 √ V = d2σ g gαβ∂ Xµ∂ Xν h (X) (7.2)

4πα’ α β µν But we’ve seen this before: it’s the vertex operator associated to the graviton state of the string! For a plane wave, corresponding to a graviton with polarization given by the symmetric, traceless tensor ζ and momentum pµ, the fluctuation is given by µν h (X) = ζ eip·X µν µν With this choice, the expression (7.2) agrees with the vertex operator (5.9). But in general, we could take any linear superposition of plane waves to build up a general fluctuation h (X).

µν We know that inserting a single copy of V in the path integral corresponds to the introduction of a single graviton state. Inserting eV in the path integral corresponds to a coherent state of gravitons, changing the metric from δ to δ + h . In this µν µν µν way we see that the background curved metric of (7.1) is indeed built of the quantized gravitons that we first met back in Section 2.

## 7.1 Einstein’s Equations

In conformal gauge, the Polyakov action in flat space reduces to a free theory. This fact was extremely useful, allowing us to compute the spectrum of the theory. But on a curved background, it is no longer the case. In conformal gauge, the worldsheet theory is described by an interacting two-dimensional field theory, ∫ S = d2σ G (X)∂ Xµ∂αXν (7.3)

4πα’ µν α To understand these interactions in more detail, let’s expand around a classical solution which we take to simply be a string sitting at a point x¯µ.

Xµ(σ) = x¯µ + α’Yµ(σ)

Here Yµ are the dynamical fluctuations about the point which we assume to be small.

The factor of α’ is there for dimensional reasons: since [X] = −1, we have [Y] = 0 and statements like Y ≪ 1 make sense. Expanding the Lagrangian gives [ √ α’ ]

G (X)∂Xµ∂Xν = α’ G (x¯)+ α’G (x¯)Yω + G (x¯)YωYρ +... ∂Yµ∂Yν µν µν µν,ω µν,ωρ Each of the coefficients G in the Taylor expansion are coupl coupling constants for the interactions of the fluctuations Yμ. The theory has an infinite number of coupling constants and they are nicely packaged into the function Gμν(X).

We want to know when this field theory is weakly coupled. Obviously this requires the whole infinite set of coupling constants to be small. Let’s try to characterize this in a crude manner. Suppose that the target space has characteristic radius of curvature r, meaning schematically that ∂G/∂X ~ 1/r. The radius of curvature is a length scale, so [r] = -1. From the expansion of the metric, we see that the effective dimensionless coupling is given by α' (7.4). This means that we can use perturbation theory to study the CFT (7.3) if the spacetime metric only varies on scales much greater than √α'. The perturbation series in √α'/r is usually called the α'-expansion to distinguish it from the g expansion that we saw in the previous section. Typically a quantity computed in string theory is given by a double perturbation expansion: one in α' and one in g.

If there are regions of spacetime where the radius of curvature becomes comparable to the string length scale, r ~ α', then the worldsheet CFT is strongly coupled and we will need to develop new methods to solve it. Notice that strong coupling in α' is hard, but the problem is at least well-defined in terms of the worldsheet path integral. This is qualitatively different to the question of strong coupling in g for which, as discussed in Section 6.4.5, we’re really lacking a good definition of what the problem even means.

7.1.1 The Beta Function Classically, the theory defined by (7.3) is conformally invariant. But this is not necessarily true in the quantum theory. To regulate divergences we will have to introduce a UV cut-off and, typically, after renormalization, physical quantities depend on the scale of a given process μ. If this is the case, the theory is no longer conformally invariant. There are plenty of theories which classically possess scale invariance which is broken quantum mechanically. The most famous of these is Yang-Mills.

As we’ve discussed several times, in string theory conformal invariance is a gauge symmetry and we can’t afford to lose it. Our goal in this section is to understand the circumstances under which (7.3) retains conformal invariance at the quantum level.

The object which describes how couplings depend on a scale μ is called the β-function. Since we have a functions worth of couplings, we should really be talking about a β-functional, schematically of the form βμν(G) ~ μ ∂Gμν(X;μ)/∂μ. The quantum theory will be conformally invariant only if βμν(G) = 0.

We now compute this for the non-linear sigma model at one-loop. Our strategy will be to isolate the UV divergence of the theory and figure out what kind of counterterm we should add. The beta-function will vanish if this counterterm vanishes.

The analysis is greatly simplified by a cunning choice of coordinates. Around any point x̄, we can always pick Riemann normal coordinates such that the expansion in Xμ = x̄μ + α'Yμ gives Gμν(X) = δμν - α' Rμλνκ(x̄)YλYκ + O(Y³). To quartic order in the fluctuations, the action becomes S = (1/4π) ∫ d²σ ∂Yμ∂Yν [δμν - (α'/3) Rμλνκ YλYκ].

We can now treat this as an interacting quantum field theory in two dimensions. The quartic interaction gives a vertex with the Feynman rule, ~ Rμλνκ (kμ·kν), where kμ is the 2d momentum (α = 1,2 is a worldsheet index) for the scalar field Yμ. It sits in the Feynman rules because we are talking about derivative interactions.

Now we’ve reduced the problem to a simple interacting quantum field theory, we can compute the β-function using whatever method we like. The divergence in the theory comes from the one-loop diagram.

It’s actually simplest to think about this diagram in position space. The propagator for a scalar particle is ⟨Yλ(σ)Yκ(σ')⟩ = -δλκ ln|σ - σ'|². For the scalar field running in the loop, the beginning and end point coincide. The propagator diverges as σ → σ', which is simply reflecting the UV divergence that we would see in the momentum integral around the loop.

To isolate this divergence, we choose to work with dimensional regularization, with d = 2+ε. The propagator then becomes, ⟨Yλ(σ)Yκ(σ')⟩ = δλκ ∫ d²⁺εk e^(ik·(σ-σ')) / (2π)²⁺ε k² → δλκ/ε as σ → σ'.

The necessary counterterm for this divergence can be determined simply by replacing YλYκ in the action with ⟨YλYκ⟩. To subtract the 1/ε term, we add the counterterm Rμλνκ YλYκ ∂Yμ∂Yν → Rμλνκ YλYκ ∂Yμ∂Yν - (1/ε) Rμν ∂Yμ∂Yν.

One can check that this can be absorbed by a wavefunction renormalization Yμ → Yμ + (α'/6ε) Rμν Yν, together with the renormalization of the coupling constant which, in our theory, is the metric Gμν. We require, Gμν → Gμν + (α'/ε) Rμν.

从这个结果我们得知理论的β函数以及共形不变性的条件。它是 β(G) = α'R = 0 (7.6)

这是一个神奇的结果！σ模型要求共形不变的条件是目标空间必须是Ricci平坦的：R = 0。或者换句话说，弦运动所处的背景时空必须服从真空爱因斯坦方程！我们看到广义相对论的方程也描述了二维σ模型的重整化群流。

还有更多神奇的事情即将出现，但值得暂停一下，做一些不同的评论。

上述计算有效地研究了平坦世界面上共形场论（7.3）中共形不变性的破坏。我们知道，这应该等同于弯曲世界面上Weyl不变性的破坏。由于这是一个如此重要的结果，让我们从另一个角度来看它是如何运作的。我们可以考虑世界面度规 g_{αβ} = e^{2φ} δ_{αβ} 那么，在维度正则化中，理论在 d = 2 + ε 维度上不是Weyl不变的，因为来自 g_{αβ} 的贡献并不完全抵消来自逆度规 g^{αβ} 的贡献。作用量是 S = ∫ d^{2+ε}σ (1/(4πα')) e^{φε} ∂_α X^μ ∂^α X^ν G_{μν}(X)

≈ ∫ d^{2+ε}σ (1/(4πα')) (1 + φε) ∂_α X^μ ∂^α X^ν G_{μν}(X)

其中，在这个表达式中，α = 1,2 的指标现在用 δ_{αβ} 来升降。如果我们在这个表达式中用重整化后的度规 (7.5) 替换 G_{μν}，我们看到即使当 ε → 0 时，仍然存在一个涉及 φ 的项， S = ∫ d^2σ (1/(4πα')) ∂_α X^μ ∂^α X^ν [G_{μν}(X) + α' φ R_{μν}(X)]

这表明Weyl不变性的破坏。确实，我们可以查看我们通常的Weyl不变性诊断，即 T_α 的消失。在共形规范下，它由下式给出 T_{αβ} = - (1/(4π)) (∂S/∂g^{αβ} + √g ∂S/∂φ) = -2π δ_{αβ} ⇒ T_α = - (1/2) R_{μν} ∂X^μ ∂X^ν 在这种看待事物的方式中，我们将β函数定义为 ∂X∂X 前面的系数，即 T_α = - (β_{μν}/(2α')) ∂X^μ ∂X^ν 再次，我们得到结果 β_{μν} = α' R_{μν}

7.1.2 Ricci流在弦理论中，我们只关心具有Ricci平坦度规的共形理论。（以及我们即将讨论的这个结果的推广）。然而，在物理学和数学的其他领域，重整化群流本身很重要。它通常被称为Ricci流， ∂G_{μν}/∂μ = α' R_{μν} (7.7)

它决定了度规如何随尺度 μ 变化。

作为一个说明性的简单例子，考虑半径为 r 的目标空间 S^2。这是凝聚态物理中的一个重要模型，它描述了一维Heisenberg自旋链的低能极限。它有时被称为O(3) σ模型。由于球体是一个对称空间，重整化群流的唯一效应是使半径具有尺度依赖性：r = r(μ)。β函数由下式给出 ∂r^2/∂μ = α'/(2π)

因此，当我们走向紫外（UV）时 r 变大，走向红外（IR）时 r 变小。由于耦合是 1/r，这意味着具有 S^2 目标空间的非线性σ模型是渐近自由的。在低能量下，理论是强耦合的，微扰计算——比如这个单圈β函数——不再可靠。特别地，可以证明 S^2 σ模型在红外中发展出一个质量间隙。

Ricci流 (7.7) 的思想最近被Perelman用来证明庞加莱猜想。事实上，Perelman使用了一个稍微推广的Ricci流版本，我们很快会看到。用弦理论的语言来说，他引入了膨胀子场。

## 7.2 其他耦合

我们已经理解了弦如何与背景时空度规耦合。但弦的其他模式呢？在第2节中，我们看到闭弦还有进一步的无质量态，它们与反对称张量 B_{μν} 和膨胀子 Φ 相关。我们现在将看到，如果这些场在时空中被开启，弦会如何反应。

7.2.1 带电弦与B场让我们首先看看弦如何与反对称场 B_{μν} 耦合。我们在第5.4.1节讨论了与该态相关的顶点算符。它在 (5.9) 中给出，并与引力子顶点算符具有相同的形式，但 ζ_{μν} 是反对称的。很容易将其指数化，得到弦在背景 B 场中传播的表达式。我们也将保留弯曲度规 G_{μν} 以获得一般作用量， S = ∫ d^2σ (1/(4πα')) √g [G_{μν}(X) ∂_α X^μ ∂^α X^ν g^{αβ} + i B_{μν}(X) ∂_α X^μ ∂_β X^ν ε^{αβ}] (7.8)

其中 ε^{αβ} 是反对称的2-张量，归一化为 g ε^{12} = +1。（因子 i 出现在作用量中是因为我们在欧几里得空间中，并且这个新项具有单个“时间”导数）。作用量在世界面重新参数化和Weyl重标度下保持不变。

那么这个新项的解释是什么？我们现在将表明，我们应该将场 B 视为类似于规范势 A in electromagnetism. The action (7.8) is telling us that the string is “electrically charged” under Bμν.

Gauge Potentials

We’ll take a short detour to remind ourselves about some pertinent facts in electromagnetism. Let’s start by returning to a point particle. We know that a charged point particle couples to a background gauge potential Aμ through the addition of a worldline term to the action, ∫ dτ Aμ(X) Ẋμ. (7.9)

If this relativistic form looks a little unfamiliar, we can deconstruct it by working in static gauge with X0 ≡ t = τ, where it reads ∫ dt [A0(X) + Ai(X) Ẋi]

which should now be recognizable as the Lagrangian that gives rise to the Coulomb and Lorentz force laws for a charged particle.

So what is the generalization of this kind of coupling for a string? First note that (7.9) has an interesting geometrical structure. It is the pull-back of the one-form A = Aμ dXμ in spacetime onto the worldline of the particle. This works because A is a one-form and the worldline is one-dimensional. Since the worldsheet of the string is two-dimensional, the analogous coupling should be to a two-form in spacetime. This is an anti-symmetric tensor field with two indices, Bμν. The pull-back of B onto the worldsheet gives the interaction, ∫ d²σ Bμν(X) ∂αXμ ∂βXν εαβ. (7.10)

This is precisely the form of the interaction we found in (7.8).

The point particle coupling (7.9) is invariant under gauge transformations of the background field Aμ → Aμ + ∂μα. This follows because the Lagrangian changes by a total derivative. There is a similar statement for the two-form Bμν. The spacetime gauge symmetry is, Bμν → Bμν + ∂μCν − ∂νCμ (7.11)

under which the Lagrangian (7.10) changes by a total derivative.

In electromagnetism, one can construct the gauge invariant electric and magnetic fields which are packaged in the two-form field strength F = dA. Similarly, for Bμν, the gauge invariant field strength H = dB is a three-form, Hμνρ = ∂μBνρ + ∂νBρμ + ∂ρBμν.

This 3-form H is sometimes known as the torsion. It plays the same role as torsion in general relativity, providing an anti-symmetric component to the affine connection.

7.2.2 The Dilaton

Let’s now figure out how the string couples to a background dilaton field Φ(X). This is more subtle. A naive construction of the vertex operator is not primary and one must work a little harder. The correct derivation of the vertex operators can be found in Polchinski. Here I will simply give the coupling and explain some important features.

The action of a string moving in a background involving profiles for the massless fields Gμν, Bμν and Φ(X) is given by S = 1/(4πα') ∫ d²σ √g [ Gμν(X) ∂αXμ ∂βXν gαβ + i Bμν(X) ∂αXμ ∂βXν εαβ + α' Φ(X) R(2) ] (7.12)

where R(2) is the two-dimensional Ricci scalar of the worldsheet. (Up until now, we’ve always denoted this simply as R but we’ll introduce the superscript from hereon to distinguish the worldsheet Ricci scalar from the spacetime Ricci scalar).

The coupling to the dilaton is surprising for several reasons. Firstly, we see that the term in the action vanishes on a flat worldsheet, R(2) = 0. This is one of the reasons that it’s a little trickier to determine this coupling using vertex operators.

However, the most surprising thing about the coupling to the dilaton is that it does not respect Weyl invariance! Since a large part of this course has been about understanding the implications of Weyl invariance, why on earth are we willing to throw it away now?! The answer, of course, is that we’re not. Although the dilaton coupling does violate Weyl invariance, there is a way to restore it. We will explain this shortly. But firstly, let’s discuss one crucially important implication of the dilaton coupling (7.12).

The Dilaton and the String Coupling

There is an exception to the statement that the classical coupling to the dilaton violates Weyl invariance. This arises when the dilaton is constant. For example, suppose Φ(X) = λ, a constant. Then the dilaton coupling reduces to something that we’ve seen before: it is S_dilaton = λχ, where χ is the Euler character of the worldsheet that we introduced in (6.4). This tells us something important: the constant mode of the dilaton, ⟨Φ⟩, determines the string coupling constant. This constant mode is usually taken to be the asymptotic value of the dilaton, Φ0 = lim_{X→∞} Φ(X) (7.13)

The string coupling is then given by g = e^{Φ0} (7.14)

So the string coupling is not an independent parameter of string theory: it is the expectation value of a field. This means that, just like the spacetime metric Gμν (or, indeed, like the Higgs vev) it can be determined dynamically.

We’ve already seen that our perturbative expansion around flat space is valid as long as g ≪ 1. But now we have a stronger requirement: we can only trust perturbation theory if the string is localized in regions of space where e^{Φ(X)} ≪ 1.

for all X. If the string ventures into regions where eΦ(X) is of order 1, then we will need to use techniques that don’t rely on string perturbation theory as described in Section 6.4.5.

7.2.3 Beta Functions We now return to understanding how we can get away with the violation of Weyl invariance in the dilaton coupling (7.12). The key to this is to notice the presence of α' in front of the dilaton coupling. It’s there simply on dimensional grounds. (The other two terms in the action both come with derivatives [∂X] = −1, so don’t need any powers of α').

However, recall that α' also plays the role of the loop-expansion parameter (7.4) in the non-linear sigma model. This means that the classical lack of Weyl invariance in the dilaton coupling can be compensated by a one-loop contribution arising from the couplings to Gμν and Bμν.

To see this explicitly, one can compute the beta-functions for the two-dimensional field theory (7.12). In the presence of the dilaton coupling, it’s best to look at the breakdown of Weyl invariance as seen by ⟨Tαα⟩. There are three different kinds of contribution that the stress-tensor can receive, related to the three different spacetime fields. Correspondingly, we define three different beta functions, ⟨Tαα⟩ = − 1/(2α') βμν(G) gαβ ∂μXν ∂αXβ − 1/(2α') βμν(B) εαβ ∂μXν ∂αXβ − 1/2 β(Φ) R(2) (7.15)

We will not provide the details of the one-loop beta function computations. We merely state the results8, βμν(G) = α' Rμν + 2α' ∇μ∇ν Φ − 1/4 Hμλκ Hνλκ βμν(B) = − α'/2 ∇λ Hλμν + α' ∇λΦ Hλμν β(Φ) = − α'/2 ∇²Φ + α'/2 ∇μΦ ∇μΦ − α'/24 Hμνλ Hμνλ A consistent background of string theory must preserve Weyl invariance, which now requires βμν(G) = βμν(B) = β(Φ) = 0.

## 7.3 The Low-Energy Effective Action

The equations βμν(G) = βμν(B) = β(Φ) = 0 can be viewed as the equations of motion for the background in which the string propagates. We now change our perspective: we look for a D = 26 dimensional spacetime action which reproduces these beta-function equations as the equations of motion. This is the low-energy effective action of the bosonic string, S = 1/(2κ²) ∫ d²⁶X √-G e^{-2Φ} (R − 1/12 Hμνλ Hμνλ + 4 ∂μΦ ∂μΦ) (7.16)

where we have taken the liberty of Wick rotating back to Minkowski space for this expression. Here the overall constant involving κ is not fixed by the field equations but can be determined by coupling these equations to a suitable source as described, for example, in 7.4.2. On dimensional grounds alone, it scales as κ² ∼ l_s²⁴ where α' = l_s².

Varying the action with respect to the three fields can be shown to yield the beta functions thus, δS = 1/(2κ²α') ∫ d²⁶X √-G e^{-2Φ} (δGμν βμν(G) − δBμν βμν(B)

− (2δΦ + Gμν δGμν) (βλλ(G) − 4β(Φ))

Equation (7.16) governs the low-energy dynamics of the spacetime fields. The caveat “low-energy” refers to the fact that we only worked with the one-loop beta functions which requires large spacetime curvature.

Something rather remarkable has happened here. We started, long ago, by looking at how a single string moves in flat space. Yet, on grounds of consistency alone, we’re led to the action (7.16) governing how spacetime and other fields fluctuate in D = 26 dimensions. It feels like the tail just wagged the dog. That tiny string is seriously high-maintenance: its requirements are so stringent that they govern the way the whole universe moves.

You may also have noticed that we now have two different methods to compute the scattering of gravitons in string theory. The first is in terms of scattering amplitudes that we discussed in Section 6. The second is by looking at the dynamics encoded in the low-energy effective action (7.16). Consistency requires that these two approaches agree. They do.

7.3.1 String Frame and Einstein Frame The action (7.16) isn’t quite of the familiar Einstein-Hilbert form because of that strange factor of e^{-2Φ} that’s sitting out front. This factor simply reflects the fact that the action has been computed at tree level in string perturbation theory and, as we saw in Section 6, such terms typically scale as 1/g².

It’s also worth pointing out that the kinetic terms for Φ in (7.16) seem to have the wrong sign. However, it’s not clear that we should be worried about this because, again, the factor of e^{-2Φ} sits out front meaning that the kinetic terms are not canonically normalized anyway.

To put the action in more familiar form , we can make a field redefinition. Firstly, it’s useful to distinguish between the constant part of the dilaton, Φ , and the part that varies which we call Φ. We defined the constant part in (7.13); it is related to the string coupling constant. The varying part is simply given by Φ = Φ−Φ (7.17)

In D dimensions, we define a new metric G as a combination of the old metric and µν the dilaton, (X) = e−4Φ˜/(D−2)G (X) (7.18)

µν µν Note that this isn’t to be thought of as a coordinate transformation or symmetry of the action. It’s merely a relabeling, a mixing-up, of the fields in the theory. We could make such redefinitions in any field theory. Typically, we choose not to because the fields already have canonical kinetic terms. The point of the transformation (7.18) is to get the fields in (7.16) to have canonical kinetic terms as well.

The new metric (7.18) is related to the old by a conformal rescaling. One can check that two metrics related by a general conformal transformation G ˜ = e2ωG , have µν µν Ricci scalars related by R ˜ = e−2ω (cid:0) R−2(D−1)∇2ω −(D−2)(D−1)∂ ω∂µω (cid:1)

(We used a particular version of this earlier in the course when considering D = 2 conformaltransformations). Withthechoiceω = −2Φ/(D−2)in(7.18),andrestricting back to D = 26, the action (7.16) becomes (cid:90) (cid:18) (cid:19)

1 (cid:112) 1 1 S = d26X −G ˜ R ˜ − e−Φ˜/3H Hµνλ − ∂ Φ ˜ ∂µΦ ˜ (7.19)

2κ2 12 µνλ 6 µ The kinetic terms for Φ are now canonical and come with the right sign. Notice that there is no potential term for the dilaton and therefore nothing that dynamically sets its expectation value in the bosonic string. However, there do exist backgrounds of the superstring in which a potential for the dilaton develops, fixing the string coupling constant.

– 171 – The gravitational part of the action takes the standard Einstein-Hilbert form. The gravitational coupling is given by κ2 = κ2e2Φ0 ∼ l24g2 (7.20)

0 s s The coefficient in front of Einstein-Hilbert term is usually identified with Newton’s constant 8πG = κ2 Note, however, that this is Newton’s constant in D = 26 dimensions: it will differ from Newton’s constant measured in a four-dimensional world. From Newton’s constant, we define the D = 26 Planck length 8πG = l24 and Planck mass M = l−1. (With the N p p p factor of 8π sitting there, this is usually called the reduced Planck mass). Comparing to (7.20), we see that weak string coupling, g (cid:28) 1, provides a parameteric separation between the Planck scale and the string scale, g (cid:28) 1 ⇒ l (cid:28) l s p s Often the mysteries of gravitational physics are associated with the length scale l . We understand string theory best when g (cid:28) 1 where much of stringy physics occurs at l (cid:29) l and can be disentangled from strong coupling effects in gravity.

s p The original metric G is usually called the string metric or sigma-model metric. It µν is the metric that strings see, as reflected in the action (7.1). In contrast, G is called µν the Einstein metric. Of course, the two actions (7.16) and (7.19) describe the same physics: we have simply chosen to package the fields in a different way in each. The choice of metric — G or G — is usually referred to as a choice of frame: string µν µν frame, or Einstein frame.

The possibility of defining two metrics really arises because we have a massless scalar field Φ in the game. Whenever such a field exists, there’s nothing to stop us measuring distances in different ways by including Φ in our ruler. Said another way, massless scalar fields give rise to long range attractive forces which can mix with gravitational forces and violate the principle of equivalence. Ultimately, if we want to connect to Nature, weneedtofindawaytomakeΦmassive. Suchmechanismsexistinthecontext of the superstring.

7.3.2 Corrections to Einstein’s Equations Now that we know how Einstein’s equations arise from string theory, we can start to try to understand new physics. For example, what are the quantum corrections to Einstein’s equations?

– 172 – On general grounds, we expect these corrections to kick in when the curvature r √ c of spacetime becomes comparable to the string length scale α(cid:48). But that dovetails very nicely with the discussion above where we saw that the perturbative expansion parameter for the non-linear sigma model is α(cid:48)/r2. Computing the next loop correction to the beta function will result in corrections to Einstein’s equations!

If we ignore H and Φ , the 2-loop sigma-model beta function can be easily computed and results in the α(cid:48) correction to Einstein’s equations: β = α(cid:48)R + α(cid:48)2R R λρσ +... = 0 µν µν 2 µλρσ ν Such two loop corrections also appear in the heterotic superstring. However, they are absent for the type II string theories, with the first corrections appearing at 4-loops from the perspective of the sigma-model.

String Loop Corrections Perturbative string theory has an α(cid:48) expansion and g expansion. We still have to discuss the l atter. Here an interesting subtlety arises. The sigma-model beta functions arise from regulating the UV divergences of the worldsheet. Yet the g expansion cares only about the topology of the string. How can the UV divergences care about the global nature of the worldsheet. Or, equivalently, how can the higher-loop corrections to the beta-functions give anything interesting?

The resolution to this puzzle is to remember that, when computing higher g corrections, we have to integrate over the moduli space of Riemann surfaces. But this moduli space will include some tricky points where the Riemann surface degenerates. (For example, one cycle of the torus may pinch off). At these points, the UV divergences suddenly do care about global topology and this results in the g corrections to the low-energy effective action.

7.3.3 Nodding Once More to the Superstring

In section 2.5, we described the massless bosonic content for the four superstring theories: Heterotic SO(32), Heterotic E₈ × E₈, Type IIA and Type IIB. Each of them contains the fields Gμν, Bμν and Φ that appear in the bosonic string, together with a collection of further massless fields. For each, the low-energy effective action describes the dynamics of these fields in D = 10 dimensional spacetime. It naturally splits up into three pieces,

S_superstring = S₁ + S₂ + S_fermi

Here S_fermi describes the interactions of the spacetime fermions. We won’t describe these here. But we will briefly describe the low-energy bosonic action S₁ + S₂ for each of these four superstring theories.

S₁ is essentially the same for all theories and is given by the action we found for the bosonic string in string frame (7.16). We’ll start to use form notation and denote Hμνλ simply as H₃, where the subscript tells us the degree of the form. Then the action reads

S₁ = 1/(2κ²) ∫ d¹⁰X √-G e^{-2Φ} (R - 1/2 |H₃|² + 4 ∂μΦ ∂^μΦ) (7.21)

There is one small difference, which is that the field H₃ that appears here for the heterotic string is not quite the same as the original H₃; we’ll explain this further shortly.

The second part of the action, S₂, describes the dynamics of the extra fields which are specific to each different theory. We’ll now go through the four theories in turn, explaining S₂ in each case.

• Type IIA: For this theory, H₃ appearing in (7.21) is H₃ = dB₂, just as we saw in the bosonic string. In Section 2.5, we described the extra bosonic fields of the Type IIA theory: they consist of a 1-form C₁ and a 3-form C₃. The dynamics of these fields is governed by the so-called Ramond-Ramond part of the action and is written in form notation as,

S₂ = -1/(4κ²) ∫ d¹⁰X √-G (|F₂|² + |F̃₄|²) + B₂ ∧ F₄ ∧ F₄

Here the field strengths are given by F₂ = dC₁ and F₄ = dC₃, while the object that appears in the kinetic terms is F̃₄ = F₄ - C₁ ∧ H₃. Notice that the final term in the action does not depend on the metric: it is referred to as a Chern-Simons term.

• Type IIB: Again, H₃ ≡ H₃. The extra bosonic fields are now a scalar C₀, a 2-form C₂ and a 4-form C₄. Their action is given by

S₂ = -1/(4κ²) ∫ d¹⁰X √-G (|F₁|² + |F₃|² + 1/2 |F̃₅|²) + C₀ ∧ H₃ ∧ F₃

where F₁ = dC₀, F₃ = dC₂ and F₅ = dC₄. Once again, the kinetic terms involve more complicated combinations of the forms: they are F̃₃ = F₃ - C₀ ∧ H₃ and F̃₅ = F₅ - 1/2 C₂ ∧ H₃ + 1/2 B₂ ∧ F₃. However, for type IIB string theory, there is one extra requirement on these fields that cannot be implemented in any simple way in terms of a Lagrangian: F̃₅ must be self-dual

F̃₅ = *F̃₅

Strictly speaking, one should say that the low-energy dynamics of type IIB theory is governed by the equations of motion that we get from the action, supplemented with this self-duality requirement.

• Heterotic: Both heterotic theories have just one further massless bosonic ingredient: a non-Abelian gauge field strength F₂, with gauge group SO(32) or E₈ × E₈. The dynamics of this field is simply the Yang-Mills action in ten dimensions,

S₂ = α'/(8κ²) ∫ d¹⁰X √-G Tr|F₂|²

The one remaining subtlety is to explain what H₃ means in (7.21): it is defined as H̃₃ = dB₂ - α' ω₃/4 where ω₃ is the Chern-Simons three form constructed from the non-Abelian gauge field A₁

ω₃ = Tr(A₁ ∧ dA₁ + 2/3 A₁ ∧ A₁ ∧ A₁)

The presence of this strange looking combination of forms sitting in the kinetic terms is tied up with one of the most intricate and interesting aspects of the heterotic string, known as anomaly cancelation.

The actions that we have written down here probably look a little arbitrary. But they have very important properties. In particular, the full action S_superstring of each of the Type II theories is invariant under N = 2 spacetime supersymmetry. (That means 32 supercharges). They are the unique actions with this property. Similarly, the heterotic superstring actions are invariant under N = 1 supersymmetry and, crucially, do not suffer from anomalies. The second book by Polchinski is a good place to start learning more about these ideas.

## 7.4 Some Simple Solutions

The spacetime equations of motion, β(G_μν) = β(B_μν) = β(Φ) = 0 have many solutions. This is part of the story of vacuum selection in string theory. What solution, if any, describes the world we see around us? Do we expect this putative solution to have other special properties, or is it just a random choice from the many possibilities? The answer is that we don’t really know, but there is currently no known principle which uniquely selects a solution which looks like our world — with the gauge groups, matter content and values of fundamental constants that we observe — from the many other possibilities. Of course, these questions should really be asked in the context of the superstring where a greater understanding of various non-perturbative effects such as D-branes and fluxes leads to an even greater array of possible solutions. Here we won’t discuss these problems. Instead, we’ll just discuss a few simple solutions that are well known. The first plays a role when trying to make contact with the real world, while the value of the others lies mostly in trying to better understand the structure of string theory.

7.4.1 Compactifications

We’ve seen that the bosonic string likes to live in D = 26 dimensions. But we don’t. Or, more precisely, we only observe three macroscopically large spatial dimensions. How do we reconcile these statements?

Since string theory is a theory of gravity, there’s nothing to stop extra dimensions of the universe from curling up. Indeed, under certain circumstances, this may be required dynamically. Here we exhibit some simple solutions of the low-energy effective action which have this property. We set H_μνρ = 0 and Φ to a constant. Then we are simply searching for Ricci flat backgrounds obeying R_μν = 0. There are solutions where the metric is a direct product of metrics on the space R^{1,3} × X (7.22)

where X is a compact 22-dimensional Ricci-flat manifold.

The simplest such manifold is just X = T^{22}, the torus endowed with a flat metric. But there are a whole host of other possibilities. Compact, complex manifolds that admit such Ricci-flat metrics are called Calabi-Yau manifolds. (Strictly speaking, Calabi-Yau manifolds are complex manifolds with vanishing first Chern class. Yau’s theorem guarantees the existence of a unique Ricci flat metric on these spaces).

The idea that there may be extra, compact directions in the universe was considered long before string theory and goes by the name of Kaluza-Klein compactification. If the characteristic length scale L of the space X is small enough then the presence of these extra dimensions would not have been observed in experiment. The standard model of particle physics has been accurately tested to energies of a TeV or so, meaning that if the standard model particles can roam around X, then the length scale must be L ≲ (TeV)^{-1} ∼ 10^{-16} cm.

However, one can cook up scenarios in which the standard model is stuck somewhere in these extra dimensions (for example, it may be localized on a D-brane). Under these circumstances, the constraints become much weaker because we would rely on gravitational experiments to detect extra dimensions. Present bounds require only L ≲ 10^{-5} cm.

Consider the Einstein-Hilbert term in the low-energy effective action. If we are interested only in the dynamics of the 4d metric on R^{1,3}, this is given by S_EH = ∫ d^{26}X √(-G) (1/(2κ^2)) ˜R = ∫ d^4X √(-G_{4d}) (Vol(X)/(2κ^2)) R_{4d} (There are various moduli of the internal manifold X that are being neglected here). From this equation, we learn that effective 4d Newton constant is given in terms of 26d Newton constant by, 8πG_{4d} = κ^2 / Vol(X)

Rewriting this in terms of the 4d Planck scale, we have l_p^{(4d)} ∼ g_s^{1/2} l_s / √(Vol(X)). To trust this whole analysis, we require g_s ≪ 1 and all length scales of the internal space to be bigger than l_s. This ensures that l_p^{(4d)} < l_s. Although the 4d Planck length is ludicrously small, l_p^{(4d)} ∼ 10^{-33} cm, it may be that we don’t have to probe to this distance to uncover UV gravitational physics. The back-of-the-envelope calculation above shows that the string scale l_s could be much larger, enhanced by the volume of extra dimensions.

7.4.2 The String Itself

We’ve seen that quantizing small loops of string gives rise to the graviton and B_μν field. Yet, from the sigma model action (7.12), we also know that the string is charged under the B_μν. Moreover, the string has tension, which ensures that it also acts as a source for the metric G_μν. So what does the back-reaction of the string look like? Or, said another way: what is the sigma-model describing a string moving in the background of another string?

Consider an infinite, static, straight string stretched in the X^1 direction. We can solve for the background near fields by coupling the equations of motion to a delta-function string source. This is the same kind of calculation that we’re used to in electromagnetism. The resulting spacetime fields are given by ds2 = f(r)−1(−dt2 +dX2)+ (cid:80)25 dX2 1 i=2 i B = (f(r)−1 −1)dt∧dX , e2Φ = f(r)−1 (7.23)

The function f(r) depends only on the transverse direction r2 = (cid:80)25 X2 and is given i=2 i by g2Nl22 f(r) = 1+ s s r22 Here N is some constant which we will shortly demonstrate counts the number of strings which source the background. The string length scale in the solutions is l = α(cid:48). The function f(r) has the property that it is harmonic in the space transverse to the string, meaning that it satisfies ∇2 f(r) = 0 except at r = 0.

R24 Let’s compute the B-field charge of this solution. We do exactly what we do in electromagnetism: we integrate the total flux through a sphere which surrounds the object. The string lies along the X1 direction so the transverse space is R24. We can consider a sphere S23 at the boundary of this transverse space. We should be integrating the flux over this sphere. But what is the expression for the flux?

To see what we should do, let’s look at the action for H in the presence of a string µνρ source. We will use form notation since this is much cleaner and refer to H simply µνρ as H . Schematically, the action takes the form (cid:90) (cid:90) (cid:90)

1 1 H ∧(cid:63)H + B = H ∧(cid:63)H +g2B ∧δ(ω)

g2 3 3 2 g2 3 3 s 2 s R26 R2 s R26 Here δ(ω) is a delta-function source with support on the 2d worldsheet of the string. The equation of motion is d(cid:63)H ∼ g2δ(ω)

3 s From this we learn that to compute the charge of a single string we need to integrate (cid:90)

(cid:63)H = 1 g2 3 s S23 After these general comments, we now return to our solution (7.23). The above discussion was schematic and no attention was paid to factors of 2 and π. Keeping in this spirit, the flux of the solution (7.23) can be checked to be (cid:90)

(cid:63)H = N g2 3 s S23 This is telling us that the solution (7.23) describes the background sourced by N coincident, parallel fundamental strings. Another way to check this is to compute the ADM mass per unit length of the solution: it is NT ∼ N/α(cid:48) as expected.

Note as far as the low-energy effective action is concerned, there is nothing that insists N ∈ Z. This is analogous to the statement that nothing in classical Maxwell theory requires e to be quantized. However, in string theory, as in QED, we know the underlying sources of the microscopic theory and N must indeed take integer values.

Finally, notice that as r → 0, the solution becomes singular. It is not to be trusted in this regime where higher order α(cid:48) corrections become important.

7.4.3 Magnetic Branes We’ve already seen that string theory is not just a theory of strings; there are also D-branes, defined as surfaces on which strings can end. We’ll have much more to say about D-branes in Section 7.5. Here, we will consider a third kind of object that exists in string theory. It is again a brane – meaning that it is extended in some number of spacetime directions — but it is not a D-brane because the open string cannot end there. In these lectures we will call it the magnetic brane.

Electric and Magnetic Charges You’re probably not used to talking about magnetically charged objects in electromagnetism. Indeed, in undergraduate courses we usually don’t get much further than pointing out that ∇ ·B = 0 does not allow point-like magnetic charges. However, in the context of quantum field theory, much of the interesting behaviour often boils down to understanding how magnetic charges behave. And the same is true of string theory. Because this may be unfamiliar, let’s take a minute to discuss the basics.

In electromagnetism in d = 3+1 dimensions, we measure electric charge q by integrating the electric field E (cid:126) over a sphere S2 that surrounds the particle, (cid:90) (cid:90)

q = E (cid:126) ·dS (cid:126) = (cid:63)F (7.24)

## S2 S2

In the second equality we have introduced the notation of differential forms that we also used in the previous example to discuss the string solutions.

Suppose now that a particle carries magnetic charge g. This can be measured by (cid:126)

integrating the magnetic field B over the same sphere. This means (cid:90) (cid:90)

(cid:126) (cid:126)

g = B ·dS = F (7.25)

## S2 S2

In d = 3+1 dimensions, both electrically and magnetically charged objects are particles. But this is not always true in any dimension! The reason that it holds in 4d is because both the field strength F and the dual field strength (cid:63)F are 2-forms. Clearly, this is rather special to four dimensions.

In general, suppose that we have a p-brane that is electrically charged under a suitable gauge field. As we discussed in Section 7.2.1, a (p + 1)-dimensional object naturally couples to a (p+1)-form gauge potential C through, p+1 (cid:90)

µ C p+1 where µ is the charge of the object, while W is the worldvolume of the brane. The (p+1)-form gauge potential has a (p+2)-form field strength G = dC_{p+1}. To measure the electric charge of the p-brane, we need to integrate the field strength over a sphere that completely surrounds the object. A p-brane in D-dimensions has a transverse space R^{D−p−1}. We can integrate the flux over the sphere at infinity, which is S^{D−p−2}. And, indeed, the counting works out nicely because, in D dimensions, the dual field strength is a (D −p−2)-form, *G = G ̃_{D−p−2}, which we can happily integrate over the sphere to find the charge sitting inside, q = ∫_{S^{D−p−2}} *G_{p+2} This equation is the generalized version of (7.24).

Now let’s think about magnetic charges. The generalized version of (7.25) suggests that we should compute the magnetic charge by integrating G_{p+2} over a sphere S^{p+2}. What kind of object sits inside this sphere to emit the magnetic charge? Doing the sums backwards, we see that it should be a (D−p−4)-brane.

We can write down the coupling between the (D−p−4)-brane and the field strength. To do so, we first need to introduce the magnetic gauge potential defined by *G_{p+2} = G ̃_{D−p−2} = dC ̃_{D−p−3} (7.26)

We can then add the magnetic coupling to the worldvolume W ̃ of a (D−p−4)-brane simply by writing ∫_{W ̃} µ̃ C ̃_{D−p−3} where µ̃ is the magnetic charge. Note that it’s typically not possible to write down a Lagrangian that includes both magnetically charged object and electrically charged objects at the same time. This would need us to include both C_{p+1} and C ̃_{D−p−3} in the Lagrangian, but these are not independent fields: they’re related by the rather complicated differential equations (7.26).

The Magnetic Brane in Bosonic String Theory After these generalities, let’s see what it means for the bosonic string. The fundamental string is a 1-brane and, as we saw in Section 7.2.1, carries electric charge under the 2-form B. The appropriate object carrying magnetic charge under B is therefore a (D−p−4) = (26−1−4) = 21-brane.

To stress a point: neither the fundamental string, nor the magnetic 21-brane are D-branes. They are not surfaces where strings can end. We are calling them branes only because they are extended objects.

The magnetic 21-brane of the bosonic string can be found as a solution to the low-energy equations of motion. The solution can be written in terms of the dual potential B ̃_{22} such that dB ̃_{22} = *dB_2. It is ds^2 = −dt^2 + ∑_{i=1}^{21} dX_i^2 + h(r) ∑_{i=22}^{25} dX_i^2 (7.27)

B ̃_{22} = (1−h(r)^{−2}) dt ∧ dX_1 ∧ ... ∧ dX_{21} e^{2Φ} = h(r)

The function h(r) depends only on the radial direction in R^4 transverse to the brane: r^2 = ∑_{i=22}^{25} X_i^2. It is a harmonic function in R^4, given by h(r) = 1 + \frac{N l_s^2}{r^2} The role of this function in the metric (7.27) is to warp the transverse R^4 directions. Distances get larger as you approach the brane and the origin, r = 0, is at infinite distance.

It can be checked that the solution carries N units of magnetic charge and has tension T ∼ \frac{N}{l_s^2 g_s^2}

Let’s summarize how the tension of different objects scale in string theory. The powers of α' = l_s^2 are entirely fixed on dimensional grounds. (Recall that the tension is mass per spatial volume, so the tension of a p-brane has [T] = p+1). More interesting is the dependence on the string coupling g_s. The tension of the fundamental string does not depend on g_s, while the magnetic brane scales as 1/g_s^2. This kind of 1/g_s^2 behaviour is typical of solitons in field theories. The D-branes sit between the two: their tension scales as 1/g_s. Objects with this behaviour are somewhat rarer (although not unheard of) in field theory.

In the perturbative limit, g_s → 0, both D-branes and magnetic branes are heavy. The coupling of an object with tension T to gravity is governed by Tκ^2 where the gravitational coupling scales as κ ∼ g_s^2 (7.20). This means that in the weak coupling limit, the gravitational backreaction of the string and D-branes can be neglected. However, the coupling of the magnetic brane to gravity is always of order one.

The Magnetic Brane in Superstring Theory Superstring theories also have a brane magnetically charged under B. It is a (D−p−4) = (10−1−4) = 5-brane and is usually referred to as the NS5-brane. The solution in the transverse R^4 again takes the form (7.27).

The NS5-brane exists in both type II and heterotic string. In many ways it is more mysterious than D-branes and its low-energy effective dynamics is still poorly understood. It is closely related to the 5-brane of M-theory.

7.4.4 Moving Away from the Critical Dimension The beta function equations provide a new view on the critical dimension D = 26 of the bosonic string. To see this, let’s look more closely at the dilaton beta function β(Φ) defined in (7.15): it takes the same form as the Weyl anomaly that we discussed back in Section 4.4.2. This means that if we consider a string propagating in D ≠ 26 then the Weyl anomaly sim simply arises as the leading order term in the dilaton beta function. So let’s relax the requirement of the critical dimension. The equations of motion arising from β(G_µν) and β(B_µν) are unchanged, while the dilaton beta function equation becomes β(Φ) = −(D−26)/(6α') ∇²Φ + α' ∇^µΦ ∇_µΦ − (1/24) H_µνλ H^µνλ = 0 (7.28)

The low-energy effective action in string frame picks up an extra term which looks like a run-away potential for Φ, S = 1/(2κ²) ∫ d^D X √-G e^{-2Φ} [ R − (1/12) H_µνλ H^µνλ + 4 ∂^µΦ ∂_µΦ − (D−26)/(3α') ]

This sounds quite exciting. Can we really get string theory living in D = 4 dimensions so easily? Well, yes and no. Firstly, with this extra potential term, flat D-dimensional Minkowski space no longer solves the equations of motion. This is in agreement with the analysis in Section 2 where we showed that full Lorentz invariance was preserved only in D = 26.

Another, technical, problem with solving the string equations of motion this way is that we’re playing a tree-level term off against a one-loop term. But if tree-level and one-loop terms are comparable, then typically all higher loop contributions will be as well and it is likely that we can’t trust our analysis.

The Linear Dilaton CFT In fact, there is one simple solution to (7.28) which we can trust. It is the solution to ∂^µΦ ∂_µΦ = (26−D)/(6α')

Recall that we’re working in signature (−,+,+,...), meaning that Φ takes a spacelike profile if D < 26 and a timelike profile if D > 26, Φ = X₁ √((26−D)/(6α'))   D < 26 Φ = X₀ √((D−26)/(6α'))   D > 26 This gives a dilaton which is linear in one direction. This can be compared to the study of the path integral for non-critical strings that we saw in 5.3.2. There are two ways of seeing the same physics.

The reason that we can trust this solution is that there is an exact CFT underlying it which we can analyze to all orders in α'. It’s called, for obvious reasons, the linear dilaton CFT. Let’s now look at this in more detail.

Firstly, consider the worldsheet action associated to the dilaton coupling. For now we’ll consider an arbitrary dilaton profile Φ(X), S_dilaton = 1/(4π) ∫ d²σ √g Φ(X) R^{(2)} (7.29)

Although this term vanishes on a flat worldsheet, it nonetheless changes the stress-energy tensor T_αβ because this is defined as T_αβ = −4π (∂S/∂g^αβ)|_{g=δ} The variation of (7.29) is straightforward. Indeed, the term is akin to the Einstein-Hilbert term in general relativity but things are simpler in 2d because, for example R_αβ = (1/2) g_αβ R. We have δ(√g g^αβ R_αβ) = √g g^αβ δR_αβ = √g ∇_α v^α where v^α = ∇_β δg^αβ − g_γδ ∇^α δg^γδ Using this, the variation of the dilaton term in the action is given by δS_dilaton = 1/(4π) ∫ d²σ √g (∇_α∇_βΦ − ∇²Φ g_αβ) δg^αβ which, restricting to flat space g_αβ = δ_αβ, finally gives us the stress-energy tensor of a theory with dilaton coupling T_dilaton_αβ = −∂_α ∂_β Φ + ∂²Φ δ_αβ Note that this stress tensor is not traceless. This is to be expected because, as we described above, the dilaton coupling is not Weyl invariant at tree-level. In complex coordinates, the stress tensor is T_dilaton = −∂²Φ , T̄_dilaton = −∂̄²Φ Linear Dilaton OPE The stress tensor above holds for any dilaton profile Φ(X). Let’s now restrict to a linear dilaton profile for a single scalar field X, Φ = Q X where Q is some constant. We also include the standard kinetic terms for D scalar fields, of which X is a chosen one, giving the stress tensor T = − (1/α') : ∂X ∂X : − Q ∂²X It is a simple matter to compute the TT OPE using the techniques described in Section 4. We find, T(z) T(w) = (c/2)/(z−w)^4 + 2T(w)/(z−w)^2 + ∂T(w)/(z−w) + ...

where the central charge of the theory is given by c = D + 6 α' Q² Note that Q² can be positive or negative depending on the whether we have a timelike or spacelike linear dilaton. In this way, we see explicitly how a linear dilaton gradient can absorb central charge.

7.4.5 The Elephant in the Room: The Tachyon We’ve been waxing lyrical about the details of solutions to the low-energy effective action, all the while ignoring the most important, relevant field of them all: the tachyon. Since our vacuum is unstable, this is a little like describing all the beautiful pictures we could paint if only that damn paintbrush would balance, unaided, on its tip.

Of course, the main reason for discussing these solutions is that they all carry directly over to the superstring where the tachyon is absent. Nonetheless, it’s interesting to ask what happens if the tachyon is turned on. Its vertex operator is simply V_tachyon ∼ ∫ d²σ g e^{ip·X} where p² = 4/α'. Piecing together a general tachyon profile V(X) from these Fourier modes and exponentiating, results in a potential on the worldsheet of the string S_potential = ∫ d²σ g α' V(X)

This is a relevant operator for the worldsheet CFT. Whenever such a relevant operator turns on, we should follow the RG flow to the infrared.

run until we land on another CFT.

The c-theorem tells us that c_IR < c_UV, but in string theory we always require c = 26.

The deficit, at least initially, is soaked up by the dilaton in the manner described above.

The end point of the tachyon RG flow for the bosonic string is not understood. It may be that there is no end point and the bosonic string simply doesn’t make sense once the tachyon is turned on. Or perhaps we haven’t yet understood the true ground state of the bosonic string.

## 7.5 D-Branes Revisited: Background Gauge Fields

Understanding the constraints of conformal invariance on the closed string backgrounds led us to Einstein’s equations and the low-energy effective action in spacetime. Now we would like to do the same for the open string. We want to understand the restrictions that consistency places on the dynamics of D-branes.

We saw in Section 3 that there are two types of massless modes that arise from the quantization of an open string: scalars, corresponding to the fluctuation of the D-brane, and a U(1) gauge field. We will ignore the scalar fluctuations for now, but will return to them later. We focus initially on the dynamics of a gauge field A_a, a = 0,...,p living on a Dp-brane.

The first question that we ask is: how does the end of the string react to a background gauge field? To answer this, we need to look at the vertex operator associated to the photon. It was given in (5.10)

V_photon ∼ ∫ dτ ζ_a ∂_τ X^a e^{ip·X} ∂M which is Weyl invariant and primary only if p^2 = 0 and p^a ζ_a = 0. Exponentiating this vertex operator, as described at the beginning of Section 7, gives the coupling of the open string to a general background gauge field A_a(X), S_end-point = ∫ dτ A_a(X) dX^a/dτ ∂M But this is a very familiar coupling — we’ve already mentioned it in (7.9). It is telling us that the end of the string is charged under the background gauge field A on the brane.

7.5.1 The Beta Function We can now perform the same type of beta function calculation that we saw for the closed string. To do this, it’s useful to first use conformal invariance to map the open string worldsheet to the Euclidean upper-half plane as we described in Section 4.7. The action describing an open string propagating in flat space, with its ends subject to a background gauge field on the D-brane splits up into two pieces S = S_Neumann + S_Dirichlet where S_Neumann describes the fluctuations parallel to the Dp-brane and is given by S_Neumann = ∫ d^2σ (1/(4πα')) ∂_α X^a ∂^α X^b δ_ab + i ∫ dτ A_a(X) Ẋ^a (7.30)

M ∂M Here a,b = 0,...,p. The extra factor of i arises because we are in Euclidean space.

Meanwhile, the fields transverse to the brane have Dirichlet boundary conditions and take range I = p+1,...,D−1. Their dynamics is given by S_Dirichlet = ∫ d^2σ (1/(4πα')) ∂_α X^I ∂^α X^J δ_IJ The action S_Dirichlet describes free fields and doesn’t play any role in the computation of the beta-function. The interesting part is S_Neumann which, for non-zero A_a(X), is an interacting quantum field theory with boundary. Our task is to compute the beta function associated to the coupling A_a(X). We use the same kind of technique that we earlier applied to the closed string. We expand the fields X^a(σ) as X^a(σ) = x̄^a(σ) + √α' Y^a(σ)

where x̄^a(σ) is taken to be some fixed background which obeys the classical equations of motion, ∂^2 x̄^a = 0 (In the analogous calculation for the closed string we chose the special case of x̄^a constant. Here we are more general). However, we also need to impose boundary conditions for this classical solution. In the absence of the gauge field A, we require Neumann boundary conditions ∂_σ X^a = 0 at σ = 0. However, the presence of the gauge field changes this. Varying the full action (7.30) shows that the relevant boundary condition is supplemented by an extra term, ∂_σ x̄^a + 2πα' i F^{ab} ∂_τ x̄_b = 0 at σ = 0 (7.31)

where the F_{ab} is the field strength F_{ab}(X) = ∂_a A_b - ∂_b A_a ≡ ∂A_b/∂X^a - ∂A_a/∂X^b The fields Y^a(σ) are the fluctuations which are taken to be small. Again, the presence of α' in the expansion ensures that Y^a are dimensionless. Expanding the action S_Neumann (which we’ll just call S from now on) to second order in fluctuations gives, S[x̄ + √α' Y] = S[x̄] + (1/(4π)) ∫ d^2σ ∂_α Y^a ∂^α Y^b δ_ab + i√α' ∫ dτ [ (∂_a A_b) Y^a Ẏ^b + (∂_c ∂_a A_b) Y^a Y^b ẋ̄^c + ... ]

∂M where all expressions involving the background gauge fields are now evaluated on the classical solution x̄. We can rearrange the boundary terms by splitting the first term up into two halves and integrating one of these pieces by parts, ∫ dτ (∂_a A_b) Y^a Ẏ^b = ∫ dτ [ ∂_a A_b Y^a Ẏ^b - ∂_a A_b Ẏ^a Y^b - ∂_c ∂_a A_b Y^a Y^b ẋ̄^c ]

Combining this with the second term means that we can write all interactions in terms of the gauge invariant field strength F_{ab}, S[\bar{x} + \alpha' Y] = S[\bar{x}] + \frac{1}{4\pi} \int d^2\sigma \partial Y^a \partial Y^b \delta_{ab} + i\alpha' \int d\tau F_{ab} Y^a \dot{Y}^b + \partial F_{ab} Y^a Y^b \dot{\bar{x}}^c + ... (7.32)

\partial M where the +... refer to the higher terms in the expansion which come with higher derivatives of F_{ab}, accompanied by powers of \alpha'. We can neglect them for the purposes of computing the one-loop beta function.

The Propagator This Lagrangian describes our interacting boundary theory to leading order. We can now use this to compute the beta function. Firstly, we should determine where possible divergences arise. The offending term is the last one in (7.32). This will lead to a divergence when the fluctuation fields Y^a are contracted with their propagator \langle Y^a(z,\bar{z}) Y^b(w,\bar{w}) \rangle = G^{ab}(z,\bar{z}; w,\bar{w})

We should be used to these free field Green’s functions by now. The propagator satisfies \partial \bar{\partial} G^{ab}(z,\bar{z}) = -2\pi \delta^{ab} \delta(z,\bar{z}) (7.33)

in the upper half plane. But now there’s a subtlety. The Y^a fields need to satisfy a boundary condition at Im z = 0 and this should be reflected in the boundary condition for the propagator. We discussed this briefly for Neumann boundary conditions in Section 4.7. But we’ve also seen that the background field strength shifts the Neumann boundary conditions to (7.31). Correspondingly, the propagator G(z,\bar{z}; w,\bar{w}) must now satisfy \partial_\sigma G^{ab}(z,\bar{z}; w,\bar{w}) + 2\pi \alpha' i F^a_{\ c} \partial_\tau G^{cb}(z,\bar{z}; w,\bar{w}) = 0 \quad \text{at} \quad \sigma = 0 (7.34)

In Section 4.7, we showed how Neumann boundary conditions could be imposed by considering an image charge in the lower half plane. A similar method works here. We extend G^{ab} \equiv G^{ab}(z,\bar{z}; w,\bar{w}) to the entire complex plane. The solution to (7.33) subject to (7.34) is given by G^{ab} = -\delta^{ab} \ln|z - w| - \frac{1}{2} \left( \frac{1 - 2\pi \alpha' F}{1 + 2\pi \alpha' F} \right)^{ab} \ln(z - \bar{w}) - \frac{1}{2} \left( \frac{1 + 2\pi \alpha' F}{1 - 2\pi \alpha' F} \right)^{ab} \ln(\bar{z} - w)

The Counterterm and Beta Function Let’s now return to the interacting theory (7.32) and see what counterterm is needed to remove the divergence. Since all interactions take place on the boundary, we should evaluate our propagator on the boundary, which means z = \bar{z} and w = \bar{w}. In this case, all the logarithms become the same and, in the limit that z \to w, gives the leading divergence \ln|z - w| \to \epsilon^{-1}. We learn that the UV divergence takes the form, \left[ -\delta^{ab} + \frac{1}{2} \left( \frac{1 - 2\pi \alpha' F}{1 + 2\pi \alpha' F} \right)^{ab} + \frac{1}{2} \left( \frac{1 + 2\pi \alpha' F}{1 - 2\pi \alpha' F} \right)^{ab} \right] \frac{2}{\epsilon} = -\frac{2}{\epsilon} \left( \frac{1}{1 - 4\pi^2 \alpha'^2 F^2} \right)^{ab} It’s now easy to determine the necessary counterterm. We simply replace Y^a Y^b in the final term with \langle Y^a Y^b \rangle. This yields -\frac{i 2\pi \alpha'^2}{\epsilon} \int d\tau \partial_\tau F_{ac} \dot{\bar{x}}^c \left( \frac{1}{1 - 4\pi^2 \alpha'^2 F^2} \right)^{ab} For the open string theory to retain conformal invariance, we need the associated beta function to vanish. This gives us the condition on the field strength F_{ab}: it must satisfy the equation \partial_\tau F_{ac} \left( \frac{1}{1 - 4\pi^2 \alpha'^2 F^2} \right)^{ab} = 0 (7.35)

This is our final equation governing the equations of motion that F_{ab} must satisfy to provide a consistent background for open string propagation.

7.5.2 The Born-Infeld Action Equation (7.35) probably doesn’t look too familiar! Following the path we took for the closed string, we wish to write down an action whose equations of motion coincide with (7.35). The relevant action was actually constructed many decades ago as a non-linear alternative to Maxwell theory: it goes by the name of the Born-Infeld action: S = -T_p \int d^{p+1}\xi \sqrt{-\det(\eta_{ab} + 2\pi \alpha' F_{ab})} (7.36)

Here \xi are the worldvolume coordinates on the brane and T_p is the tension of the Dp-brane (which, since it multiplies the action, doesn’t affect the equations of motion). The gauge potential is to be thought of as a function of the worldvolume coordinates: A_a = A_a(\xi). It actually takes a little work to show that the equations of motion that we derive from this action coincide with the vanishing of the beta function (7.35). Some hints on how to proceed are provided on Example Sheet 4.

For small field strengths, F_{ab} \ll 1/\alpha', the action (7.36) coincides with Maxwell’s action. To see this, we need simply expand to get S = -T_p \int d^{p+1}\xi \left( 1 + \frac{(2\pi \alpha')^2}{4} F_{ab} F^{ab} + ... \right)

The leading order term, quadratic in field strengths, is the Maxwell action. Terms with higher powers of F_{ab} are suppressed by powers of \alpha'.

So, for small field strengths, the dynamics of the gauge field on a D-brane is governed by Maxwell’s equations. However, as the electric and magnetic field strengths increase and become of order 1/\alpha', non-linear corrections to the dynamics kick in and are captured by the Born-Infeld action.

The Born-Infeld action arises from the one-loop beta function. It is the exact result for constant field strengths. If we want to understand the dynamics of gauge fields with large gradients, \partial F, then we will have determ Examine the higher loop contributions to the beta function.

## 7.6 The DBI Action

We’ve understood that the dynamics of gauge fields on the brane is governed by the Born-Infeld action. But what about the fluctuations of the brane itself. We looked at this briefly in Section 3.2 and suggested, on general grounds, that the action should take the Dirac form (3.6). It would be nice to show this directly by considering the beta function equations for the scalar fields φI on the brane. Turning these on corresponds to considering boundary conditions where the brane is bent. It is indeed possible to compute something along the lines of beta-function equations and to show directly that the fluctuations of the brane are governed by the Dirac action10.

More generally, one could consider both the dynamics of the gauge field and the fluctuation of the brane. This is governed by a mixture of the Dirac action and the Born-Infeld action which is usually referred to as the DBI action,

S = −T ∫ d^{p+1}ξ √{-det(γ_{ab} + 2πα' F_{ab})} DBI

As in Section (3.2), γ_{ab} is the pull-back of the spacetime metric onto the worldvolume,

γ_{ab} = η_{μν} ∂X^μ/∂ξ^a ∂X^ν/∂ξ^b

10 A readable discussion of this calculation can be found in the original paper by Leigh, Dirac-Born-Infeld Action from Dirichlet Sigma Model, Mod. Phys. Lett. A4: 2767 (1989).

The new dynamical fields in this action are the embedding coordinates X^μ(ξ), with μ = 0,...,D −1. This appears to be D new degrees of freedom while we expect only D − p − 1 transverse physical degrees of freedom. The resolution to this should be familiar by now: the DBI action enjoys a reparameterization invariance which removes the longitudinal fluctuations of the brane.

We can use this reparameterization invariance to work in static gauge. For an infinite, flat Dp-brane, it is useful to set

X^a = ξ^a, a = 0,...,p

so that the pull-back metric depends only on the transverse fluctuations X^I,

γ_{ab} = η_{ab} + δ_{IJ} ∂X^I/∂ξ^a ∂X^J/∂ξ^b

If we are interested in situations with small field strengths F_{ab} and small derivatives ∂X, then we can expand the DBI action to leading order. We have

S = −(2πα')^2 T ∫ d^{p+1}ξ (1/4 F_{ab} F^{ab} + 1/2 ∂_a φ^I ∂^a φ^I + ...)

p

where we have rescaled the positions to define the scalar fields φ^I = X^I/2πα'. We have also dropped an overall constant term in the action. This is simply free Maxwell theory coupled to free massless scalar fields φ^I. The higher order terms that we have dropped are all suppressed by powers of α'.

7.6.1 Coupling to Closed String Fields

The DBI action describes the low-energy dynamics of a Dp-brane in flat space. We could now ask how the motion of the D-brane is affected if it moves in a background created by closed string modes G_{μν}, B_{μν} and Φ. Rather than derive this, we’ll simply write down the answer and then justify each term in turn. The answer is:

S = −T ∫ d^{p+1}ξ e^{-Φ̃} √{-det(γ_{ab} + 2πα' F_{ab} + B_{ab})} DBI

Let’s start with the coupling to the background metric G_{μν}. It’s actually hidden in the notation in this expression: it appears in the pull-back metric γ_{ab} which is now given by

γ_{ab} = G_{μν} ∂X^μ/∂ξ^a ∂X^ν/∂ξ^b

It should be clear that this is indeed the natural place for it to sit.

Next up is the dilaton. As in (7.17), we have decomposed the dilaton into a constant piece and a varying piece: Φ = Φ_0 + Φ̃. The constant piece governs the asymptotic string coupling, g_s = e^{Φ_0}, and is implicitly sitting in front of the action because the tension of the D-brane scales as

T_p ∼ 1/g_s

This, then, explains the factor of e^{-Φ̃} in front of the action: it simply reunites the varying part of the dilaton with the constant piece. Physically, it’s telling us that the tension of the D-brane depends on the local value of the dilaton field, rather than its asymptotic value. If the dilaton varies, the effective string coupling at a point X in spacetime is given by g_eff = e^{Φ(X)} = g_s e^{Φ̃(X)}. This, in turn, changes the tension of the D-brane. It can lower its tension by moving to regions with larger g_eff.

Finally, let’s turn to the B field. This is a 2-form in spacetime. The function B_{ab} appearing in the DBI action is the pull-back to the worldvolume

B_{ab} = B_{μν} ∂X^μ/∂ξ^a ∂X^ν/∂ξ^b

Its appearance in the DBI action is actually required on grounds of gauge invariance alone. This can be seen by considering an open string, moving in the presence of both a background B_{μν}(X) in spacetime and a background A_a(X) on the worldvolume of a brane. The relevant terms on the string worldsheet are

∫ d^2σ (1/4πα') ε^{αβ} ∂_α X^μ ∂_β X^ν B_{μν} + ∫ dτ A_a Ẋ^a M ∂M

Under a spacetime gauge transformation

B_{μν} → B_{μν} + ∂_μ C_ν − ∂_ν C_μ (7.37)

the first term changes by a total derivative. This is fine for a closed string, but it doesn’t leave the action invariant for an open string because we pick up the boundary term. Let’s quickly look at what we get in more detail. Under the gauge transformation (7.37), we have

S = ∫ d^2σ ...

15) αβ ∂ Xµ ∂ Xν B B 4πα' α β µν ∫ −→ S + dσdτ εαβ ∂ Xµ ∂ Xν ∂ C B 2πα' α β µ ν ∫ = S + dσdτ εαβ ∂ (∂ Xν C )

B 2πα' α β ν ∫ ∫ 1 1 = S + dτ X ˙ν C = S + dτ X ˙a C B 2πα' ν B 2πα' a ∂M ∂M

where, in the last line, we have replaced the sum over all directions Xν with the sum over those directions obeying Neumann boundary conditions Xa, since X ˙I = 0 at the end-points for any directions with Dirichlet boundary conditions.

The result of this short calculation is to see that the string action is not invariant under (7.37). To restore this spacetime gauge invariance, this boundary contribution must be canceled by an appropriate shift of A in the second term, A → A − C (7.38)

a a 2πα' a

Note that this is not the usual kind of gauge transformation that we consider in electrodynamics. In particular, the field strength Fab is not invariant. Rather, the gauge invariant combination under (7.37) and (7.38) is B + 2πα' F ab ab

This is the reason that this combination must appear in the DBI action. This is also related to an important physical effect. We have already seen that the string in spacetime is charged under Bµν. But we’ve also seen that the end of the string is charged under the gauge field A on the D-brane. This means that the open string deposits B charge on the brane, where it is converted into A charge. The fact that the gauge invariant field strength involves a combination of both Fab and Bab is related to this interplay of charges.

## 7.7 The Yang-Mills Action

Finally, let’s consider the case of N coincident D-branes. We discussed this in Section 3.3 where we showed that the massless fields on the brane could be naturally packaged as N × N Hermitian matrices, with the element of the matrix telling us which brane the end points terminate on. The gauge field then takes the form (Aa)mn with a = 0,...,p and m,n = 1,...,N. Written this way, it looks rather like a U(N) gauge connection. Indeed, this is the correct interpretation. But how do we see this? Why is the gauge field describing a U(N) gauge symmetry rather than, say, U(1)N²?

The quickest way to see that coincident branes give rise to a U(N) gauge symmetry is to recall that the end point of the string is charged under the U(1) gauge field that inhabits the brane it’s ending on. Let’s illustrate this with the simplest example. Suppose that we have two branes. The diagonal components (Aa)11 and (Aa)22 arise from strings which begin and end on the same brane. Each is a U(1) gauge field. What about the off-diagonal terms (Aa)12 and (Aa)21? These come from strings stretched between the two branes. They are again massless gauge bosons, but they are charged under the two original U(1) symmetries; they carry charge (+1,−1) and (−1,+1) respectively. But this is precisely the structure of a U(2) gauge theory, with the off-diagonal terms playing a role similar to W-bosons. In fact, the only way to make sense of massless, charged spin 1 particles is through non-Abelian gauge symmetry.

So the massless excitations of N coincident branes are a U(N) gauge field (Aa)mn, together with scalars (φI)mn which transform in the adjoint representation of the U(N) gauge group. We saw in Section 3 that the diagonal components (φI)mm have the interpretation of the transverse fluctuations of the mth brane. Can we now write down an action describing the interactions of these fields?

In fact, there are several subtleties in writing down a non-Abelian generalization of the DBI action and such an action is not known (if, indeed, it makes sense at all). However, we can make progress by considering the low-energy limit, corresponding to small field strengths. The field strength in question is now the appropriate non-Abelian expression which, neglecting the matrix indices, reads Fab = ∂a Ab − ∂b Aa + i[Aa, Ab]

The low-energy action describing the dynamics of N coincident Dp-branes can be shown to be (neglecting an overall constant term), S = −(2πα')² Tp ∫ d^{p+1}ξ Tr ( 1/4 Fab Fab + 1/2 Da φI Da φI − 1/4 Σ_{I≠J} [φI, φJ]² ) (7.39)

We recognize the first term as the U(N) Yang-Mills action. The coefficient in front of the Yang-Mills action is the coupling constant 1/g²_YM. For a Dp-brane, this is given by α'² Tp, or g²_YM ∼ l_s^{p-3} g_s

The kinetic term for φI simply reflects the fact that these fields transform in the adjoint representation of the gauge group, Da φI = ∂a φI + i[Aa, φI]

We won’t derive this action in these lectures: the first two terms basically follow from gauge invariance alone. The potential term is harder to see directly: the quick ways to derive it use T-duality or, in the case of the superstring, supersymmetry.

A flat, infinite Dp-brane breaks the Lorentz group of spacetime to S(1,D−1) → SO(1,p) × SO(D−p−1) (7.40)

This unbroken group descends to the worldvolume of the D-brane where it classifies all low-energy excitations.

tations of the D-brane. The SO(1,p) is simply the Lorentz group of the D-brane worldvolume. The SO(D−p−1) is a global symmetry of the D-brane theory, rotating the scalar fields φI. The potential term in (7.39) is particularly interesting, V = − 1/2 Tr [φI,φJ]2 I≠J The potential is positive semi-definite. We can look at the fields that can be turned on at no cost of energy, V = 0. This requires that all φI commute which means that, after a suitable gauge transformation, they take the diagonal form, φI = φI ...

φI (7.41)

The diagonal component φI describes the position of the nth brane in transverse space RD−p−1. We still need to get the dimensions right. The scalar fields have dimension [φ] = 1. The relationship to the position in space (which we mentioned before in 3.2) is Xn = 2πα'φn (7.42)

where we’ve swapped to vector notation to replace the I index. The eigenvalues φI are not quite gauge invariant: there is a residual gauge symmetry — the Weyl group of U(N) — which leaves φI in the form (7.41) but permutes the entries by S_N, the permutation group of N elements. But this has a very natural interpretation: it is simply telling us that the D-branes are indistinguishable objects. When all branes are separated, the vacuum expectation value (7.41) breaks the gauge group from U(N) → U(1)^N. The W-bosons gain a mass M through the Higgs mechanism. Let’s compute this mass. We’ll consider a U(2) theory and we’ll separate the two D-branes in the direction XD ≡ X. This means that we turn on a vacuum expectation value for φD = φ, which we write as φ = φ1 0 0 φ2 (7.43)

The values of φ1 and φ2 are the positions of the first and second brane. Or, more precisely, we need to multiply by the conversion factor 2πα' as in (7.42) to get the position X of the m = 1st,2nd brane. Let’s compute the mass of the W-boson from the Yang-Mills action (7.39). It comes from the covariant derivative terms Dφ. We expand out the gauge field as A =

## A11 W

W† A22 with A11 and A22 describing the two U(1) gauge fields and W the W-boson. The mass of the W-boson comes from the [A,φ] term inside the covariant derivative which, using the expectation value (7.43), is given by Tr[A,φ]2 = −(φ2 −φ1)2|W|2 This gives us the mass of the W-boson: it is M_W^2 = (φ2 −φ1)^2 = T^2|X2 −X1|^2 where T = 1/2πα' is the tension of the string. But this has a very natural interpretation. It is precisely the mass of a string stretched between the two D-branes as shown in the figure above. We see that D-branes provide a natural geometric interpretation of the Higgs mechanism using adjoint scalars. Notice that when branes are well separated, and the strings that stretch between them are heavy, their positions are described by the diagonal elements of the matrix given in (7.41). However, as the branes come closer together, these stretched strings become light and are important for the dynamics of the branes. Now the positions of the branes should be described by the full N ×N matrices, including the off-diagonal elements. In this manner, D-branes begin to see space as something non-commutative at short distances. In general, we can consider N D-branes located at positions Xm, m = 1,...,N in transverse space. The string stretched between the mth and nth brane has mass M = |φn −φm| = T|Xn −Xm| which again coincides with the mass of the appropriate W-boson computed using (7.39). 7.7.1 D-Branes in Type II Superstring Theories As we mentioned previously, D-branes are ingredients of the Type II superstring theories. Type IIA has Dp-branes with p even, while Type IIB is home to Dp-branes with p odd. The D-branes have a very important property in these theories: they preserve half the supersymmetries. Let’s take a moment to explain what this means. We’ll start by returning to the Lorentz group SO(1,D − 1) now, of course, with D = 10. We’ve already seen that an infinite, flat Dp-brane is not invariant under the full Lorentz group, but only the subgroup (7.40). If we act with either SO(1,p) or SO(D − p − 1) then the D-brane solution remains invariant. We say that these symmetries are preserved by the solution. However, the role of the preserved symmetries doesn’t stop there. The next step is to consider small excitations of the D-brane. These must fit into representations of the preserved symmetry group (7.40). This ensures that the low-energy dynamics of the D-brane must be governed by a theory which is invariant under (7.40) and we have indeed seen that the Lagrangian (7.39) has SO(1,p) as a Lorentz group and SO(D −p−1) as a global symmetry group which rotates the scalar fields. Now let’s return to supersymmetry. The Type II string theories enjoy a lot of supersymmetry: 32 supercharges in total. The infinite, flat D-branes are invariant under half of these; if we act with one half of the supe Supersymmetry generators, the D-brane solutions don't change. Objects that have this property are often referred to as BPS states. Just as with the Lorentz group, these unbroken symmetries descend to the worldvolume of the D-brane. This means that the low-energy dynamics of the D-branes is described by a theory which is itself invariant under 16 supersymmetries.

There is a unique class of theories with 16 supersymmetries and a non-Abelian gauge field and matter in the adjoint representation. This class is known as maximally supersymmetric Yang-Mills theory and the bosonic part of the action is given by (7.39). Supersymmetry is realized only after the addition of fermionic fields which also live on the brane. These theories describe the low-energy dynamics of multiple D-branes.

As an illustrative example, consider D3-branes in the Type IIB theory. The theory describing N D-branes is U(N) Yang-Mills with 16 supercharges, usually referred to as U(N) N = 4 super-Yang-Mills. The bosonic part of the action is given by (7.39), where there are D−p−1 = 6 scalar fields φI in the adjoint representation of the gauge group. These are augmented with four Weyl fermions, also in the adjoint representation.

## 8. Compactification and T-Duality

In this section, we will consider the simplest compactification of the bosonic string: a background spacetime of the form R1,24 ×S1 (8.1)

The circle is taken to have radius R, so that the coordinate on S1 has periodicity X25 ≡ X25 +2πR We will initially be interested in the physics at length scales (cid:29) R where motion on the S1 can be ignored. Our goal is to understand what physics looks like to an observer livinginthenon-compactR1,24 Minkowskispace. Thisgeneralideagoesbythenameof Kaluza-Klein compactification. We will view this compactification in two ways: firstly from the perspective of the spacetime low-energy effective action and secondly from the perspective of the string worldsheet.

## 8.1 The View from Spacetime

Let’s start with the low-energy effective action. Looking at length scales (cid:29) R means that we will take all fields to be independent of X25: they are instead functions only on the non-compact R1,24.

Consider the metric in Einstein frame. This decomposes into three different fields on R1,24: a metric G ˜ , a vector A and a scalar σ which we package into the D = 26 µν µ dimensional metric as ds2 = G ˜ dXµdXν +e2σ (cid:0) dX25 +A dXµ (cid:1)2 (8.2)

µν µ Here all the indices run over the non-compact directions µ,ν = 0,...24 only.

The vector field A is an honest gauge field, with the gauge symmetry descend- ing from diffeomorphisms in D = 26 dimensions. To see this recall that under the transformation δXµ = Vµ(X), the metric transforms as δG = ∇ Λ +∇ Λ µν µ ν ν µ This means that diffeomorphisms of the compact direction, δX25 = Λ(Xµ), turn into gauge transformations of A , δA = ∂ Λ µ µ We’d like to know how the fields G , A and σ interact. To determine this, we simply µν µ insert the ansatz (8.2) into the D = 26 Einstein-Hilbert action. The D = 26 Ricci scalar R(26) is given by R(26) = R−2e−σ∇2eσ − e2σF Fµν µν where R in this formula now refers to the D = 25 Ricci scalar. The action governing the dynamics becomes (cid:90) (cid:90) (cid:18) (cid:19)

1 (cid:112) 2πR (cid:112) 1 S = d26X −G ˜(26) R(26) = d25X −G ˜ eσ R− e2σF Fµν +∂ σ∂µσ 2κ2 2κ2 4 µν µ The dimensional reduction of Einstein gravity in D dimensions gives Einstein gravity in D−1 dimensions, coupled to a U(1) gauge theory and a single massless scalar. This illustrates the original idea of Kaluza and Klein, with Maxwell theory arising naturally from higher-dimensional gravity.

The gravitational action above is not quite of the Einstein-Hilbert form. We need to again change frames, absorbing the scalar σ in the same manner as we absorbed the dilatoninSection7.3.1. Moreover, justasforthedilaton, thereisnopotentialdictating the vacuum expectation value of σ. Changing the vev of σ corresponds to changing R, so this is telling us that nothing in the gravitational action fixes the radius R of the compact circle. This is a problem common to all Kaluza-Klein compactifications11: there are always massless scalar fields, corresponding to the volume of the internal space as well as other deformations. Massless scalar fields, such as the dilaton Φ or the volume σ, are usually referred to as moduli.

If we want this type of Kaluza-Klein compactification to describe our universe — where we don’t see massless scalar fields — we need to find a way to “fix the moduli”. This means that we need a mechanism which gives rise to a potential for the scalar fields, makingthemheavyanddynamicallyfixingtheirvacuumexpectationvalue. Such mechanisms exist in the context of the superstring.

Let’snowalsolookattheKaluza-Kleinreductionoftheotherfieldsinthelow-energy effective action. The dilaton is easy: a scalar in D dimensions reduces to a scalar in D − 1 dimensions. The anti-symmetric 2-form has more structure: it reduces to a 2-form B, together with a vector field A = B.

µν µ µ25 11 The description of compactification on more general manifolds is a beautiful story involving aspects of differential geometry and topology. This story is told in the second volume of Green, Schwarz and Witten.

In summary, the low-energy physics of the bosonic string in D−1 dimensions consists of a metric G, two U(1) gauge fields A and A and two massless scalars Φ and σ.

µν µ µ

8.1.1 Moving around the Circle In the above discussion, we assumed that all fields are independent of the periodic direction X25. Let’s now look at what happens if we relax this constraint. It’s simplest to see the resulting physics if we look at the scalar field Φ where we don’t have to worry about cluttering equations with indices. In general, we can expand this field in Fourier modes around the circle Φ(Xµ;X25) = Φ (Xµ)einX25/R n=−∞ where reality requires Φ* = Φ . Ignoring the coupling to gravity for now, the kinetic terms for this scalar are n −n d26X ∂µΦ∂µΦ+(∂25Φ)2 = 2πR d25X ∂µΦn ∂µΦ−n + |Φn|2 n2/R2 n=−∞ This simple Fourier decomposition is telling us something very important: a single scalar field on R1,D−1 × S1 splits into an infinite number of scalar fields on R1,D−2, indexed by the integer n. These have mass M2 = n2/R2 (8.3)

For R small, all particles are heavy except for the massless zero mode n = 0. The heavy particles are typically called Kaluza-Klein (KK) modes and can be ignored if we’re probing energies << 1/R or, equivalently, distance scales >> R.

There is one further interesting property of the KK modes Φn with n ≠ 0: they are charged under the gauge field A arising from the metric. The simplest way to see this is to look at the appropriate gauge transformation which, from the spacetime perspective, is the diffeomorphism X25 → X25 + Λ(Xµ). Clearly, this shifts the KK modes Φn → exp(inΛ/R) Φn This tells us that the nth KK mode has charge n/R. In fact, one usually rescales the gauge field to A'µ = Aµ/R, under which the charge of the KK mode Φn is simply n ∈ Z.

## 8.2 The View from the Worldsheet

We now consider the Kaluza-Klein reduction from the perspective of the string. We want to study a string moving in the background R1,24 × S1. There are two ways in which the compact circle changes the string dynamics.

The first effect of the circle is that the spatial momentum, p, of the string in the circle direction can no longer take any value, but is quantized in integer units p25 = n ∈ Z The simplest way to see this is simply to require that the string wavefunction, which includes the factor eip·X, is single valued.

The second effect is that we can allow more general boundary conditions for the mode expansion of X. As we move around the string, we no longer need X(σ+2π) = X(σ), but can relax this to X25(σ +2π) = X25(σ)+2πmR m ∈ Z The integer m tells us how many times the string winds around S1. It is usually simply called the winding number.

Let’s now follow the familiar path that we described in Section 2 to study the spectrum of the string on the spacetime (8.1). We start by considering only the periodic field X25, highlighting the differences with our previous treatment. The mode expansion of X25 is now given by X25(σ,τ) = x25 + α' n τ + mR σ + oscillator modes which incorporates both the quantized momentum and the possibility of a winding number. Before splitting X25(σ,τ) into right-moving and left-moving parts, it will be useful to introduce the quantities pL = n/(α' R) + mR/R, pR = n/(α' R) − mR/R (8.4)

Then we have X25(σ,τ) = X25L(σ+)+X25R(σ−), where X25L(σ+) = ½ x25 + ½ α' pL σ+ + i √(α'/2) Σ_{n≠0} (1/n) α̃25n e−inσ+ , X25R(σ−) = ½ x25 + ½ α' pR σ− + i √(α'/2) Σ_{n≠0} (1/n) α25n e−inσ− This differs from the mode expansion (1.36) only in the terms pL and pR. The mode expansion for all the other scalar fields on flat space R1,24 remains unchanged and we don’t write them explicitly.

Let’s think about what the spectrum of this theory looks like to an observer living in D = 25 non-compact directions. Each particle state will be described by a momentum pµ with µ = 0,...,24. The mass of the particle is M2 = − Σ_{µ=0}^{24} pµ pµ As before, the mass of these particles is fixed in terms of the oscillator modes of the string by the L0 and L̃0 equations. These now read M2 = p2L/α' + (2/α')(Ñ −1) = p2R/α' + (2/α')(N −1)

where N and Ñ are the levels, defined in lightcone quantization by (2.24). (One should take the lightcone coordinate inside R1,24 rather than along the S1). The factors of −1 are the necessary normal ordering coefficients that we’ve seen in several guises in this course.

These equations differ from (2.25) by the presence of the momentum and winding terms around S1 on the right-hand side. In particular, level matching no longer tells us that N = Ñ, but instead N - Ñ = nm (8.5)

Expanding out the mass formula, we have M² = n²/R² + m²R²/α'² + 2(N + Ñ - 2) (8.6)

The new terms in this formula have a simple interpretation. The first term tells us that a string with n > 0 units of momentum around the circle gains a contribution to its mass of n/R. This agrees with the result (8.3) that we found from studying the KK reduction of the spacetime theory. The second term is even easier to understand: a string which winds m > 0 times around the circle picks up a contribution 2πmRT to its mass, where T = 1/2πα' is the tension of the string.

8.2.1 Massless States We now restrict attention to the massless states in R^{1,24}. This can be achieved in the mass formula (8.6) by looking at states with zero momentum n = 0 and zero winding m = 0, obeying the level matching condition N = Ñ = 1. The possibilities are • α_{-1}^μ ᾱ_{-1}^ν |0;p⟩: Under the SO(1,24) Lorentz group, these states decompose into a metric G_{μν}, an anti-symmetric tensor B_{μν} and a scalar Φ.

• α_{-1}^μ ᾱ_{-1}^{25} |0;p⟩ and α_{-1}^{25} ᾱ_{-1}^μ |0;p⟩: These are two vector fields. We can identify the sum of these (α_{-1}^μ ᾱ_{-1}^{25} + α_{-1}^{25} ᾱ_{-1}^μ)|0;p⟩ with the vector field A^μ coming from the metric and the difference (α_{-1}^μ ᾱ_{-1}^{25} - α_{-1}^{25} ᾱ_{-1}^μ)|0;p⟩ with the vector field Ã^μ coming from the anti-symmetric field.

• α_{-1}^{25} ᾱ_{-1}^{25} |0;p⟩: This is another scalar. It is identified with the scalar σ associated to the radius of S¹.

We see that the massless spectrum of the string coincides with the massless spectrum associated with the Kaluza-Klein reduction of the previous section.

8.2.2 Charged Fields One can also check that the KK modes with n ≠ 0 have charge n under the gauge field A^μ. We can determine the charge of a state under a given U(1) by computing the 3-point function in which two legs correspond to the state of interest, while the third is the appropriate photon. We have two photons, with vertex operators given by, V_±(p) ∼ ∫ d²z ζ_μ (∂X^μ ∂̄X̄^{25} ± ∂X^{25} ∂̄X̄^μ) e^{ip·X} where + corresponds to A^μ and − to Ã^μ and we haven’t been careful about the overall normalization. Meanwhile, any state can be assigned momentum n and winding m by dressing the operator with the factor e^{ip_L X^{25}(z) + ip_R X̄^{25}(z̄)}. As always, it’s simplest to work with the momentum and winding modes of the tachyon, whose vertex operators are of the form V_{m,n}(p) ∼ ∫ d²z e^{ip·X} e^{ip_L X^{25} + ip_R X̄^{25}} The charge of a state is the coefficient in front of the 3-point coupling of the field and the photon, ⟨V_±(p₁) V_{m,n}(p₂) V_{-m,-n}(p₃)⟩ ∼ δ^{25}(p) ζ_μ (p^μ_2 - p^μ_3)(p_L ± p_R)

The first few factors are merely kinematical. The interesting information is in the last factor. It is telling us that under A^μ, fields have charge p_L + p_R ∼ n/R. This is in agreement with the Kaluza-Klein analysis that we saw before. However, it’s also telling us something new: under Ã^μ, fields have charge p_L - p_R ∼ mR/α'. In other words, winding modes are charged under the gauge field that arises from the reduction of B_{μν}. This is not surprising: winding modes correspond to strings wrapping the circle and we saw in Section 7 that strings are electrically charged under B_{μν}.

8.2.3 Enhanced Gauge Symmetry With a circle in the game, there are other ways to build massless states that don’t require us to work at level N = Ñ = 1. For example, we can set N = Ñ = 0 and look at winding modes m ≠ 0. The level matching condition (8.5) requires n = 0 and the mass of the states is M² = (mR/α')² - 4/α' and states can be massless whenever the radius takes special values R² = 4α'/m² with m ∈ Z. Similarly, we can set the winding to zero m = 0 and consider the KK modes of the tachyon which have mass M² = n²/R² - 4/α' which become massless when R² = n²α'/4.

However, the richest spectrum of massless states occurs when the radius takes a very special value, namely R = √α' Solutions to the level matching condition (8.5) with M² = 0 are now given by • N = Ñ = 1 with m = n = 0. These give the states described above: a metric, two U(1) gauge fields and two neutral scalars.

• N = Ñ = 0 with n = ±2 and m = 0. These are KK modes of the tachyon field. They are scalars in spacetime with charges (±2,0) under the U(1)×U(1) gauge symmetry.

• N = Ñ = 0 with n = 0 and m = ±2. This is a winding mode of the tachyon field. They are scalars in spacetime with charges (0,±2) under U(1)×U(1).

• N = 1 and Ñ = 0 with n = m = ±1. These are two new spin 1 fields, α_{-1}^μ |0;p⟩. They carry charge (±1,±1) under the two U(1)×U(1).

• N = 0 and Ñ = 1 with n = -m = ±1. These are a further two spin 1 fields, ᾱ_{-1}^μ |0;p⟩, with charge (±1,∓1) under U(1)×U(1).

How do we interpret these new massless states? Let’s firstly look at the spin 1 fields. These are charged under U(1)×U(1). As we mentioned in Section 7.7, the only way to make sense of charged massless spin 1 fields is in terms of a non-Abelian gauge symmetry. Looking at the charges, we see that at the critical radius R = α', the theory develops an enhanced gauge symmetry U(1)×U(1) → SU(2)×SU(2). The massless scalars from the N = 0 now join with the previous scalars to form adjoint representations of this new symmetry. We move away from the critical radius by changing the vacuum expectation value for σ. This breaks the gauge group back to the Cartan subalgebra by the Higgs mechanism.

From the discussion above, it’s clear that this mechanism for generating non-Abelian gauge symmetries relies on the existence of the tachyon. For this reason, this mechanism doesn’t work in Type II superstring theories. However, it turns out that it does work in the heterotic string, even though it has no tachyon in its spectrum.

## 8.3 Why Big Circles are the Same as Small Circles

The formula (8.6) has a rather remarkable property: it is invariant under the exchange R ↔ α'/R (8.7) if, at the same time, we swap the quantum numbers m ↔ n (8.8). This means that a string moving on a circle of radius R has the same spectrum as a string moving on a circle of radius α'/R. It achieves this feat by exchanging what it means to wind with that it means to move.

As the radius of the circle becomes large, R → ∞, the winding modes become very heavy with mass ∼ R/α' and are irrelevant for the low-energy dynamics. But the momentum modes become very light, M ∼ 1/R, and, in the strict limit form a continuum. From the perspective of the energy spectrum, this continuum of energy states is exactly what we mean by the existence of a non-compact direction in space.

In the other limit, R → 0, the momentum modes become heavy and can be ignored: it takes way too much energy to get anything to move on the S1. In contrast, the winding modes become light and start to form a continuum. The resulting energy spectrum looks as if another dimension of space is opening up!

The equivalence of the string spectrum on circles of radii R and α'/R extends to the full conformal field theory and hence to string interactions. Strings are unable to tell the difference between circles that are very large and circles that are very small. This striking statement has a rubbish name: it is called T-duality.

This provides another mechanism in which string theory exhibits a minimum length scale: as you shrink a circle to smaller and smaller sizes, at R = α', the theory acts as if the circle is growing again, with winding modes playing the role of momentum modes.

The New Direction in Spacetime

So how do we describe this strange new spatial direction that opens up as R → 0? Under the exchange (8.7) and (8.8), we see that p_L and p_R transform as p_L → p_L, p_R → −p_R. Motivated by this, we define a new scalar field, Y25 = X25(σ+)−X25(σ−). It is simple to check that in the CFT for a free, compact scalar field all OPEs of Y25 coincide with the OPEs of X25. This is sufficient to ensure that all interactions defined in the CFT are the same.

We can write the new spatial direction Y directly in terms of the old field X, without first doing the split into left and right-moving pieces. From the definition of Y, one can check that ∂_τ X = ∂_σ Y and ∂_σ X = ∂_τ Y. We can write this in a unified way as ∂_α X = ε_{αβ} ∂^β Y (8.9) where ε_{αβ} is the antisymmetric matrix with ε_{τσ} = −ε_{στ} = +1. (The minus sign from ε_{στ} in the above equation is canceled by another from the Minkowski worldsheet metric when we lower the index on ∂^β).

The Shift of the Dilaton

The dilaton, or string coupling, also transforms under T-duality. Here we won’t derive this in detail, but just give a plausible explanation for why it’s the case. The main idea is that a scientist living in a stringy world shouldn’t be able to do any experiments that distinguish between a compact circle of radius R and one of radius α'/R. But the first place you would look is simply the low-energy effective action which, working in Einstein frame, contains terms like ∫ d^{25}X √{-G} e^{−2φ} R + ... A scientist cannot tell the difference between R and R̃ = α'/R only if the value of the dilaton is also ambiguous so that the term in front of the action remains invariant: i.e. R/g_s^2 = R̃/g̃_s^2. This means that, under T-duality, the dilaton must shift so that the coupling constant becomes g̃_s = α' g_s / R (8.10).

8.3.1 A Path Integral Derivation of T-Duality

There’s a simple way to see T-duality of the quantum theory using the path integral. We’ll consider just a single periodic scalar field X ≡ X + 2πR on the worldsheet. It’s useful to change normalization and write X = Rϕ, so that the field ϕ has periodicity 2π. The radius R of the circle now sits in front of the action, S[ϕ] = (R^2 / 4πα') ∫ d^2σ ∂_α ϕ ∂^α ϕ (8.11). The Euclidean partition function for this theory...

ory is Z = Dϕe−S[ϕ]. We will now play around with this partition function and show that we can rewrite it in terms of new variables that describe the T-dual circle.

The theory (8.11) has a simple shift symmetry ϕ → ϕ+λ. The first step is to make this symmetry local by introducing a gauge field A on the worldsheet which transforms as A → A − ∂λ. We then replace the ordinary derivatives with covariant derivatives ∂ϕ → Dϕ = ∂ϕ + A.

This changes our theory. However, we can return to the original theory by adding a new field, θ which couples as S[ϕ,θ,A] = (R²/4πα') ∫ d²σ Dϕ Dαϕ + (i/2π) ∫ d²σ θ εαβ ∂α Aβ. (8.12)

The new field θ acts as a Lagrange multiplier. Integrating out θ sets εαβ ∂α Aβ = 0. If the worldsheet is topologically R², then this condition ensures that A is pure gauge which, in turn, means that we can pick a gauge such that A = 0. The quantum theory described by (8.12) is then equivalent to that given by (8.11).

Of course, if the worldsheet is topologically R² then we’re missing the interesting physics associated to strings winding around ϕ. On a non-trivial worldsheet, the condition εαβ ∂α Aβ = 0 does not mean that A is pure gauge. Instead, the gauge field can have non-trivial holonomy around the cycles of the worldsheet. One can show that these holonomies are gauge trivial if θ has periodicity 2π. In this case, the partition function defined by (8.12), Z = ∫ Dϕ Dθ DA e−S[ϕ,θ,A] / Vol, is equivalent to the partition function constructed from (8.11) for worldsheets of any topology.

At this stage, we make use of a clever and ubiquitous trick: we reverse the order of integration. We start by integrating out ϕ which we can do by simply fixing the gauge symmetry so that ϕ = 0. The path integral then becomes Z = ∫ Dθ DA exp[ − (R²/4πα') ∫ d²σ Aα Aα + (i/2π) ∫ d²σ εαβ (∂α θ) Aβ ], where we have also taken the opportunity to integrate the last term by parts. We can now complete the procedure and integrate out Aα. We get Z̃ = ∫ Dθ exp[ − (R̃²/4πα') ∫ d²σ ∂α θ ∂α θ ], with R̃ = α'/R the radius of the T-dual circle. In the final integration, we threw away the overall factor in the path integral, which is proportional to √(α'/R). A more careful treatment shows that this gives rise to the appropriate shift in the dilaton (8.10).

8.3.2 T-Duality for Open Strings What happens to open strings and D-branes under T-duality? Suppose firstly that we compactify a circle in direction X transverse to the brane. This means that X has Dirichlet boundary conditions X = const ⇒ ∂σ X²⁵ = 0 at σ = 0,π.

But what happens in the T-dual direction Y? From the definition (8.9) we learn that the new direction has Neumann boundary conditions, ∂σ Y = 0 at σ = 0,π.

We see that T-duality exchanges Neumann and Dirichlet boundary conditions. If we dualize a circle transverse to a Dp-brane, then it turns into a D(p+1)-brane.

The same argument also works in reverse. We can start with a Dp-brane wrapped around the circle direction X, so that the string has Neumann boundary conditions. After T-duality, (8.9) changes these to Dirichlet boundary conditions and the Dp-brane turns into a D(p−1)-brane, localized at some point on the circle Y.

In fact, this was how D-branes were originally discovered: by following the fate of open strings under T-duality.

8.3.3 T-Duality for Superstrings To finish, let’s nod one final time towards the superstring. It turns out that the ten-dimensional superstring theories are not invariant under T-duality. Instead, they map into each other. More precisely, Type IIA and IIB transform into each other under T-duality. This means that Type IIA string theory on a circle of radius R is equivalent to Type IIB string theory on a circle of radius α'/R. This dovetails with the transformation of D-branes, since type IIA has Dp-branes with p even, while IIB has p odd. Similarly, the two heterotic strings transform into each other under T-duality.

8.3.4 Mirror Symmetry The essence of T-duality is that strings get confused. Their extended nature means that they’re unable to tell the difference between big circles and small circles. We can ask whether this confusion extends to more complicated manifolds. The answer is yes. The fact that strings can see different manifolds as the same is known as mirror symmetry.

Mirror symmetry is cleanest to state in the context of the Type II superstring, although similar behaviour also holds for the heterotic strings. The simplest example is when the worldsheet of the string is governed by a superconformal non-linear sigma-model with target space given by some Calabi-Yau manifold X. The claim of mirror symmetry is that this CFT is identical to the CFT describing the string moving on a different Calabi-Yau manifold Y. The topology of X and Y is not the same. Their Hodge diamonds are the mirror of each other; hence the name. The subject of mirror symmetry y is an active area of research in geometry and provides a good example of the impact of string theory on mathematics.

## 8.4 Epilogue

We are now at the end of this introductory course on string theory. We began by trying to make sense of the quantum theory of a relativistic string moving in flat space. It is, admittedly, an odd place to start. But from then on we had no choices to make. The relativistic string leads us ineluctably to conformal field theory, to higher dimensions of spacetime, to Einstein’s theory of gravity at low-energies, to good UV behaviour at high-energies and to Yang-Mills theories living on branes. There are few stories in theoretical physics where such meagre input gives rise to such a rich structure.

This journey continues. There is one further ingredient that it is necessary to add: supersymmetry. Even this is in some sense not a choice, but is necessary to remove the troublesome tachyon that plagued these lectures. From there we may again blindly follow where the string leads, through anomalies (and the lack thereof) in ten dimensions, to dualities and M-theory in eleven dimensions, to mirror symmetry and moduli stabilization and black hole entropy counting and holography and the miraculous AdS/CFT correspondence.

However, the journey is far from complete. There is much about string theory that remains to be understood. This is true both of the mathematical structure of the theory and of its relationship to the world that we observe. The problems that we alluded to in Section 6.4.5 are real. Non-perturbative completions of string theory are only known in spacetimes which are asymptotically anti-de Sitter, but cosmological observations suggest that our home is not among these. In attempts to make contact with the standard models of particle physics and cosmology, we typically return to the old idea of Kaluza-Klein compactifications. Is this the right approach? Or are we missing some important and subtle conceptual ingredient? Or is the existence of this remarkable mathematical structure called string theory merely a red-herring that has nothing to do with the real world?

In the years immediately after its birth, no one knew that string theory was a theory of strings. It seems very possible that we’re currently in a similar situation. When the theory is better understood, it may have little to do with strings. We are certainly still some way from answering the simple question: what is string theory really?

# Atomic Physics Oxford Master Series in Atomic Optical and Laser Physics Christopher J Foot Z Library

> 来源文件：pre_Atomic_Physics_Oxford_Master_Series_in_Atomic_Optical_and_Laser_Physics_Christopher_J_Foot_Z_Library.txt
> 字符数（约）：229568
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

The Oxford Master Series is designed for final year undergraduate and beginning graduate students in physics and related disciplines. It has been driven by a perceived gap in the literature today. While basic undergraduate physics texts often show little or no connection with the huge explosion of research over the last two decades, more advanced and specialized texts tend to be rather daunting for students. In this series, all topics and their consequences are treated at a simple level, while pointers to recent developments are provided at various stages. The emphasis is on clear physical principles like symmetry, quantum mechanics, and electromagnetism which underlie the whole of physics. At the same time, the subjects are related to real measurements and to the experimental techniques and devices currently used by physicists in academe and industry. Books in this series are written as course books, and include ample tutorial material, examples, illustrations, revision points, and problem sets. They can likewise be used as preparation for students starting a doctorate in physics and related fields, or for recent graduates starting research in one of these fields in industry.

Condensed Matter Physics

## 1. M. T. Dove: Structure and dynamics: an atomic view of materials

## 2. J. Singleton: Band theory and electronic properties of solids

## 3. A. M. Fox: Optical properties of solids

## 4. S. J. Blundell: Magnetism in condensed matter

## 5. J. F. Annett: Superconductivity

## 6. R. A. L. Jones: Soft condensed matter

Atomic, Optical, and Laser Physics

## 7. C. J. Foot: Atomic physics

## 8. G. A. Brooker: Modern classical optics

## 9. S. M. Hooker, C. E. Webb: Laser physics

Particle Physics, Astrophysics, and Cosmology

## 10. D. H. Perkins: Particle astrophysics

## 11. Ta-Pei Cheng: Relativity, gravitation, and cosmology

Statistical, Computational, and Theoretical Physics

## 12. M. Maggiore: A modern introduction to quantum field theory

## 13. W. Krauth: Statistical mechanics: algorithms and computations

## 14. J. P. Sethna: Entropy, order parameters, and complexity

Atomic Physics C. J. Foot Department of Physics University of Oxford Great Clarendon Street, Oxford OX2 6DP

Oxford University Press is a department of the University of Oxford. It furthers the University’s objective of excellence in research, scholarship, and education by publishing worldwide in Oxford New York Auckland Cape Town Dar es Salaam Hong Kong Karachi Kuala Lumpur Madrid Melbourne Mexico City Nairobi New Delhi Shanghai Taipei Toronto With offices in Argentina Austria Brazil Chile Czech Republic France Greece Guatemala Hungary Italy Japan South Korea Poland Portugal Singapore Switzerland Thailand Turkey Ukraine Vietnam

Oxford is a registered trade mark of Oxford University Press in the UK and in certain other countries Published in the United States by Oxford University Press Inc., New York © Oxford University Press 2005 The moral rights of the author have been asserted Database right Oxford University Press (maker)

First published 2005 Reprinted 2005 You must not circulate this book in any other binding or cover and you must impose this same condition on any acquirer A catalogue record for this title is available from the British Library Library of Congress Cataloging in Publication Data (Data available)

ISBN-10: 0 19 850695 3 (Hbk) Ean code 978 0 19 850695 9 ISBN-10: 0 19 850696 1 (Pbk) Ean code 978 0 19 850696 6 10 9 8 7 6 5 4 3 2 Typeset by Julie M. Harris using LATEX Printed in Great Britain on acid-free paper by Antony Rowe, Chippenham

Preface This book is primarily intended to accompany an undergraduate course in atomic physics. It covers the core material and a selection of more advanced topics that illustrate current research in this field. The first six chapters describe the basic principles of atomic structure, starting in Chapter 1 with a review of the classical ideas. Inevitably the discussion of the structure of hydrogen and helium in these early chapters has considerable overlap with introductory quantum mechanics courses, but an understanding of these simple systems provides the basis for the treatment of more complex atoms in later chapters. Chapter 7 on the interaction of radiation with atoms marks the transition between the earlier chapters on structure and the second half of the book which covers laser spectroscopy, laser cooling, Bose–Einstein condensation of dilute atomic vapours, matter-wave interferometry and ion trapping. The exciting new developments in laser cooling and trapping of atoms and Bose–Einstein condensation led to Nobel prizes in 1997 and 2001, respectively. Some of the other selected topics show the incredible precision that has been achieved by measurements in atomic physics experiments. This theme is taken up in the final chapter that looks at quantum information processing from an atomic physics perspective; the techniques developed for precision measurements on atoms and ions give exquisite control over these quantum systems and enable elegant new ideas from quantum computation to be implemented.

The book assumes a knowledge of quantum mechanics equivalent to an introductory university course, e.g. the solution of the Schrödinger equation in three dimensions and perturbation theory. This initial knowledge will be reinforced by many examples in this book; topics generally regarded as difficult at the undergraduate level are explained in some detail, e.g. degenerate perturbation theory. The hierarchical structure of atoms is well described by perturbation theory since the different layers of structure within atoms have considerably different energies associated with them, and this is reflected in the names of the gross, fine and hyperfine structures. In the early chapters of this book, atomic physics may appear to be simply applied quantum mechanics, i.e. we write down the Hamiltonian for a given interaction and solve the Schrödinger equation with suitable approximations. I hope that the study of the more advanced material in the later chapters will lead to a more mature and deeper understanding of atomic physics. Throughout this book the experimental basis of atomic physics is emphasised and it is hoped that the reader will gain some factual knowledge of atomic spectra.

The selection of topics from the diversity of current atomic physics is necessarily subjective. I have concentrated on low-energy and high-precision experiments which, to some extent, reflects local research interests that are used as examples in undergraduate lectures at Oxford. One of the selection criteria was that the material is not readily available in other textbooks, at the time of writing, e.g. atomic collisions have not been treated in detail (only a brief summary of the scattering of ultracold atoms is included in Chapter 10). Other notable omissions include: X-ray spectra, which are discussed only briefly in connection with the historically important work of Moseley, although they form an important frontier of current research; atoms in strong laser fields and plasmas; Rydberg atoms and atoms in doubly- and multiply-excited states (e.g. excited by new synchrotron and free-electron laser sources); and the structure and spectra of molecules.

I would like to thank Geoffrey Brooker for invaluable advice on physics (in particular Appendix B) and on technical details of writing a textbook for the Oxford Master Series. Keith Burnett, Jonathan Jones and Andrew Steane have helped to clarify certain points, in my mind at least, and hopefully also in the text. The series of lectures on laser cooling given by William Phillips while he was a visiting professor in Oxford was extremely helpful in the writing of the chapter on that topic. The following people provided very useful comments on the draft manuscript: Rachel Godun, David Lucas, Mark Lee, Matthew McDonnell, Martin Shotter, Claes-Göran Wahlström (Lund University) and the (anonymous) reviewers. Without the encouragement of Sönke Adlung at OUP this project would not have been completed. Irmgard Smith drew some of the diagrams. I am very grateful for the diagrams and data supplied by colleagues, and reproduced with their permission, as acknowledged in the figure captions. Several of the exercises on atomic structure derive from Oxford University examination papers and it is not possible to identify the examiners individually—some of these exam questions may themselves have been adapted from some older sources of which I am not aware.

Finally, I would like to thank Professors Derek Stacey, Joshua Silver and Patrick Sandars who taught me atomic physics as an undergraduate and graduate student in Oxford. I also owe a considerable debt to the book on elementary atomic structure by Gordon Kembles Woodgate, who was my predecessor as physics tutor at St Peter’s College, Oxford. In writing this new text, I have tried to achieve the same high standards of clarity and conciseness of expression whilst introducing new examples and techniques from the laser era.

Background reading It is not surprising that our language should be incapable of describing the processes occurring within the atoms, for it was invented to describe the experiences of daily life, and these consist only of processes involving exceedingly large numbers of atoms. Furthermore, it is very difficult to modify our language so that it will be able to describe these atomic processes, for words can only describe things of which we can form mental pictures, and this ability, too, is the result of daily experience. Fortunately, mathematics is not subject to this limitation, and it has been p It is possible to invent a mathematical scheme—the quantum theory—which seems entirely adequate for the treatment of atomic processes.

From The physical principles of the quantum theory, Werner Heisenberg (1930).

The point of the excerpt is that quantum mechanics is essential for a proper description of atomic physics and there are many quantum mechanics textbooks that would serve as useful background reading for this book. The following short list includes those that the author found particularly relevant: Mandl (1992), Rae (1992) and Griffiths (1995). The book Atomic spectra by Softley (1994) provides a concise introduction to this field. The books Cohen-Tannoudji et al. (1977), Atkins (1983) and Basdevant and Dalibard (2000) are very useful for reference and contain many detailed examples of atomic physics. Angular-momentum theory is very important for dealing with complicated atomic structures, but it is beyond the intended level of this book. The classic book by Dirac (1981) still provides a very readable account of the addition of angular momenta in quantum mechanics. A more advanced treatment of atomic structure can be found in Condon and Odabasi (1980), Cowan (1981) and Sobelman (1996).

Oxford C.J.F.

Web site: http://www.physics.ox.ac.uk/users/foot This site has answers to some of the exercises, corrections and other supplementary information.

Early atomic physics

## 1.1 Introduction

The origins of atomic physics were entwined with the development of quantum mechanics itself ever since the first model of the hydrogen atom by Bohr. This introductory chapter surveys some of the early ideas, including Einstein’s treatment of the interaction of atoms with radiation, and a classical treatment of the Zeeman effect. These methods, developed before the advent of the Schrödinger equation, remain useful as an intuitive way of thinking about atomic structure and transitions between the energy levels. The ‘proper’ description in terms of atomic wavefunctions is presented in subsequent chapters.

Before describing the theory of an atom with one electron, some experimental facts are presented. This ordering of experiment followed by explanation reflects the author’s opinion that atomic physics should not be presented as applied quantum mechanics, but it should be motivated by the desire to understand experiments. This represents what really happens in research where most advances come about through the interplay of theory and experiment.

## 1.2 Spectrum of atomic hydrogen

It has long been known that the spectrum of light emitted by an element is characteristic of that element.

例如，街灯中的钠，或火焰中的燃烧，会产生独特的黄色光。这种通过肉眼观察颜色的粗糙光谱学形式，构成了简单化学分析的基础。一种更复杂的方法是使用棱镜或衍射光栅在摄谱仪内色散光线，它显示原子的特征光谱由离散谱线组成，这些谱线是元素的“指纹”。早在19世纪80年代，夫琅禾费就使用摄谱仪测量了太阳光中一些前所未见谱线的波长，并由此推断出一种名为氦的新元素的存在。与原子不同，分子（即使是最简单的双原子分子）的光谱包含许多紧密排列的谱线，形成特征性的分子谱带；大分子和固体通常具有近乎连续的光谱，几乎没有尖锐特征。1888年，瑞典教授J.里德伯发现氢的光谱线遵循以下数学公式：

1/λ = R (1/n² - 1/n'²)      (1.1)

其中n和n'是整数；R是一个常数，即里德伯常数。n=2，n'=3,4,...的谱线系列现在称为巴耳末系，位于可见光区域。第一条在656nm处的线称为巴耳末-α（或Hα）线，它赋予了氢放电特有的红色——健康的红光表明大部分H₂分子已被放电中的电子轰击解离成原子。该系列的下一条线是位于486nm蓝光区域的巴耳末-β线，后续更短波长的线趋近于紫光区域的一个极限。为了描述这样的谱线系列，通常定义跃迁波长的倒数为波数 ν̃，单位是m⁻¹（或常用的cm⁻¹）：

ν̃ = 1/λ      (1.2)

波数可能看起来相当过时，但它们在原子物理学中非常有用，因为可以从测量的波长轻松计算，无需任何转换因子。实际上，用于特定量的单位与其测量方法相关，例如，分光镜和摄谱仪是按波长校准的。一个具有波数 ν̃ 的光子能量为 E = hcν̃。巴耳末公式隐含着一个更普遍的经验定律，称为里兹组合原理：光谱中某些谱线的波数可以表示为其他谱线的和（或差）：ν̃₃ = ν̃₁ ± ν̃₂。例如，巴耳末-β线（n=2 到 n'=4）的波数是巴耳末-α线（n=2 到 n'=3）和帕邢系第一条线（n=3 到 n'=4）的波数之和。如今这似乎显而易见，因为我们了解原子底层的能级结构，但它仍然是分析光谱的有用原理。检查跃迁波数的和与差能提供线索，从而推断出底层结构，就像纵横字谜一样——一些例子将在后续章节中给出。氢观测到的所有光谱线都可以表示为能级之间的差，如图1.1所示，其中能量与1/n²成正比。公式1.1预测的其他系列在实验上比巴耳末系更难观测。跃迁到n=1的线给出拉曼系，位于光谱的真空紫外区域。波长比巴耳末系更长的谱线系列位于红外区域（人眼不可见，早期光谱学家的主要探测工具——照相底片也不易感光）。下一节将探讨如何从理论上解释这些光谱。

## 1.3 玻尔理论

1913年，玻尔运用量子力学提出了氢原子的一个激进新模型。卢瑟福实验已知原子内部有一个非常小、致密、带正电的原子核。对于氢，这是一个质子，一个电子通过库仑力束缚其上。由于力与1/r²成正比，如同引力一样，从经典角度看，原子可以被视为一个微型太阳系，电子像行星绕太阳一样绕质子运行。然而，量子力学在小系统中很重要，只允许某些电子轨道。这可以从氢原子只在对应于离散能量之间跃迁的特定波长发光这一观测中推断出来。玻尔能够通过引入当时新颖的量子化思想来解释观测到的光谱，这一思想超越了以往任何经典理论。他取经典力学中的轨道，并对其施加量子化规则。

玻尔假设每个电子在一个圆形轨道上绕原子核运行，其半径r由向心加速度与质子库仑吸引力之间的平衡决定。对于质量为m、速度为v的电子，这给出：

mₑ v² / r = e² / (4πε₀ r²)      (1.3)

在SI单位制中，两个电荷量大小为e的静电相互作用强度由常数组合 e²/(4πε₀) 表征。这导致以下角频率ω = v/r与半径的关系：

ω² = [e²/(4πε₀)] / (mₑ r³)      (1.4)

这等效于行星轨道的开普勒定律，将周期2π/ω的平方与半径的立方联系起来（正如预期，因为所有步骤都是纯经典力学）。电子在这种轨道中的总能量是其动能和势能之和：

E = ½ mₑ v² - e²/(4πε₀ r)      (1.5)

利用公式1.3，我们发现动能的大小等于势能的一半（维里定理的一个例子）。考虑到动能和势能符号相反，我们得到：

E = - e²/(4πε₀) / (2r)      (1.6)

这个总能量是负的，因为电子被束缚在质子上，需要提供能量才能移除。为了更进一步，玻尔做出了以下假设。

假设I 存在某些允许的轨道，电子在这些轨道上具有固定能量。电子只有在这些允许的轨道之间跳跃时才损失能量，原子以给定波长的光的形式发射这些能量。

电子在允许的轨道上不辐射能量，这与经典电动力学相矛盾——一个在圆周运动中加速的带电粒子会辐射电磁波。玻尔模型并未解释电子为何不辐射，而是简单地将其作为一个最终被实验数据证实的假设接受下来。我们现在需要确定所有可能的经典轨道中哪些是允许的。有各种方法可以做到这一点，我们遵循许多基础文本中使用的标准方法，即假设角动量是约化普朗克常数ℏ（普朗克常数除以2π）的整数倍：

mₑ v r = n ℏ,      (1.7)

其中n是整数。将其与公式1.3结合，得到允许轨道的半径：

r = a₀ n²,      (1.8)

其中玻尔半径a₀由下式给出：

a₀ = ℏ² / [(e²/(4πε₀)) mₑ]      (1.9)

这是原子物理学中的自然长度单位。公式1.6和1.8结合给出著名的玻尔公式：

E = - [e²/(4πε₀)] / (2 a₀ n²)      (1.10)

正整数n称为主量子数。玻尔公式预测，在这些能级之间的跃迁中，原子发射的光的波数由下式给出：

ν̃ = R∞ (1/n² - 1/n'²)      (1.11)

该方程与公式1.1描述的原子氢观测光谱非常吻合。公式1.11中的里德伯常数R∞定义为：

hc R∞ = [e²/(4πε₀)]² mₑ / (2 ℏ²)      (1.12)

乘在里德伯常数前的hc因子是能量和波数之间的转换因子，因为R∞的值以m⁻¹（或常用的cm⁻¹）为单位给出。使用激光技术测量原子氢的光谱，得到了一个极其精确的里德伯常数值 R∞ = 10973731.568525 m⁻¹。然而，为绕固定原子核运动的电子计算的里德伯常数R∞与考虑原子核运动时的常数之间存在细微差别。

All hydrogen atoms in eqn 1.1 (we originally wrote R without a subscript but more strictly we should specify that it is the constant for hydrogen R∞). The theoretical treatment above has assumed an infinitely massive nucleus, hence the subscript ∞. In reality both the electron and proton move around the centre of mass of the system. For a nucleus of finite mass M the equations are modified by replacing the electron mass m by its reduced mass m = m_e M / (m_e + M). (1.13)

For hydrogen R∞' = R∞ [1 - (m_e / M_p)], (1.14)

where the electron-to-proton mass ratio is m_e / M_p ≈ 1/1836. This reduced-mass correction is not the same for different isotopes of an element, e.g. hydrogen and deuterium. This leads to a small but readily observable difference in the frequency of the light emitted by the atoms of different isotopes; this is called the isotope shift (see Exercises 1.1 and 1.2).

## 1.4 Relativistic effects

Bohr's theory was a great breakthrough. It was such a radical change that the fundamental idea about the quantisation of the orbits was at first difficult for people to appreciate—they worried about how the electrons could know which orbits they were going into before they jumped. It was soon realised, however, that the assumption of circular orbits is too much of an over-simplification. Sommerfeld produced a quantum mechanical theory of electrons in elliptical orbits that was consistent with special relativity. He introduced quantisation through a general rule that stated 'the integral of the momentum associated with a coordinate around one period of the motion associated with that coordinate is an integral multiple of Planck's constant'. This general method can be applied to any physical system where the classical motion is periodic. Applying this quantisation rule to momentum around a circular orbit gives the equivalent of eqn 1.7:8 8 This has a simple interpretation in terms of the de Broglie wavelength associated with an electron λ_dB = h/m_ev. The allowed orbits are those that have an integer multiple of de Broglie wavelengths around the circumference: 2πr = nλ_dB, i.e. they are standing matter waves. Curiously, this idea has some resonance with modern ideas in string theory.

me v × 2πr = nh. (1.15)

In addition to quantising the motion in the coordinate θ, Sommerfeld also considered quantisation of the radial degree of freedom r. He found that some of the elliptical orbits expected for a potential proportional to 1/r are also stationary states (some of the allowed orbits have a high eccentricity, more like those of comets than planets). Much effort was put into complicated schemes based on classical orbits with quantisation, and by incorporating special relativity this 'old quantum theory' could explain accurately the fine structure of spectral lines. The exact details of this work are now mainly of historical interest but it is worthwhile to make a simple estimate of relativistic effects. In special relativity a particle of rest mass m moving at speed v has an energy E(v) = γmc², (1.16)

where the gamma factor is γ = 1/√(1 - v²/c²). The kinetic energy of the moving particle is ΔE = E(v) - E(0) = (γ - 1)mc². Thus relativistic effects produce a fractional change in energy:9 9 We neglect a factor of 1 in the binomial expansion of the expression for γ at low speeds, v²/c² ≪ 1.

ΔE / E ≈ v² / c². (1.17)

This leads to energy differences between the various elliptical orbits of the same gross energy because the speed varies in different ways around the elliptical orbits, e.g. for a circular orbit and a highly elliptical orbit of the same gross energy. From eqns 1.3 and 1.7 we find that the ratio of the speed in the orbit to the speed of light is v / c = α / n, (1.18)

where the fine-structure constant α is given by α = e² / (4πε₀ℏc). (1.19)

This fundamental constant plays an important role throughout atomic physics.10 Numerically its value is approximately α ≈ 1/137 (see inside the back cover for a list of constants used in atomic physics). From eqn 1.17 we see that relativistic effects lead to energy differences of order α² times the gross energy. (This crude estimate neglects some dependence on principal quantum number and Chapter 2 gives a more quantitative treatment of this fine structure.) It is not necessary to go into all the refinements of Sommerfeld's relativistic theory that gave the energy levels in hydrogen very precisely, by imposing quantisation rules on classical orbits, since ultimately a paradigm shift was necessary. Those ideas were superseded by the use of wavefunctions in the Schrödinger equation. The idea of elliptical orbits provides a connection with our intuition based on classical mechanics and we often retain some traces of this simple picture of electron orbits in our minds. However, for atoms with more than one electron, e.g. helium, classical models do not work and we must think in terms of wavefunctions.

10 An electron in the Bohr orbit with n=1 has speed αc. Hence it has linear momentum meαc and angular momentum meαc a₀ = ℏ.

## 1.5 Moseley and the atomic number

At the same time as Bohr was working on his model of the hydrogen atom, H. G. J. Moseley measured the X-ray spectra of many elements. Moseley established that the square root of the frequency of the emitted lines is proportional to the atomic number Z (that he defined as the position of the atom in the periodic table, starting counting at Z = 1 for hydrogen), i.e.

√f ∝ Z. (1.20)

Moseley's original plot is shown in Fig. 1.2. As we shall see, this equation is a considerable simplification of the actual situation but it was remarkably powerful at the time. By ordering the elements using Z rather than relative atomic mass, as was done previously, several inconsistencies in the periodic table were resolved. There were still gaps that were later filled by the discovery of new elements. In particular, for the rare-earth elements that have similar chemical properties and are therefore difficult to distinguish, it was said 'in an afternoon, Moseley could solve the problem that had baffled chemists for many decades and establish the true number of possible rare earths' (Segrè 1980). Moseley's observations can be explained by a relatively simple model for atoms that extends Bohr's model for hydrogen.11 11 Tragically, Henry Gwyn Jeffreys Moseley was killed when he was only 28 while fighting in the First World War (see the biography by Heilbron (1974)).

A natural way to extend Bohr's atomic model to heavier atoms is to suppose that the electrons fill up the allowed orbits starting from the bottom. Each energy level only has room for a certain number of electrons so they cannot all go into the lowest level and they arrange themselves in shells, labelled by the principal quantum number, around the nucleus. This shell structure arises because of the Pauli exclusion principle and the electron spin, but for now let us simply consider it as an empirical fact that the maximum number of electrons in the n=1 shell is 2, the n=2 shell has 8 and the n=3 shell has 18, etc. For historical reasons, X-ray spectroscopists do not use the principal quantum number but label the shells by letters: K for n = 1, L for n = 2, M for n = 3 and so on alphabetically.12 This concept of electronic shells explains the emission of X-rays from atoms in the following way. Moseley produced X-rays by bombarding samples of the given element with electrons that 12 The chemical properties of the elements depend on this electronic structure, e.g. the inert gases have full shells of electrons and these stable configurations are not willing to form chemical bonds. The explanation of the atomic structure underlying the periodic table is discussed further in Section 4.1. See also Atkins (1994) and Grant and Phillips (2001).

## Chapter

Fig. 1.2 Moseley’s plot of the square root of the frequency of X-ray lines of elements against their atomic number. Moseley’s work established the atomic number Z as a more fundamental quantity than the ‘atomic weight’ (now called relative atomic mass). Following modern convention the units of the horizontal scales would be (10^8 Hz) at the bottom and (10^-10 m) for the log scale at the top. (Archives of the Clarendon Laboratory, Oxford; also shown on the Oxford physics website.)

13 The handwriting in the bottom right corner states that this diagram is the original for Moseley’s famous paper in Phil. Mag., 27, 703 (1914).

## 1.5 Moseley and the atomic number

had been accelerated to a high voltage in a vacuum tube. These fast electrons knock an electron out of an atom in the sample leaving a vacancy or hole in one of its shells. This allows an electron from a higher-lying shell to ‘fall down’ to fill this hole emitting radiation of a wavelength corresponding to the difference in energy between the shells. To explain Moseley’s observations quantitatively we need to modify the equations in Section 1.3, on Bohr’s theory, to account for the effect of a nucleus of charge greater than the +1e of the proton. For a nuclear charge Ze we replace e^2 / (4πε0) by Ze^2 / (4πε0) in all the equations, resulting in a formula for the energies like that of Balmer but multiplied by a factor of Z^2. This dependence on the square of the atomic number means that, for all but the lightest elements, transitions between low-lying shells lead to emission of radiation in the X-ray region of the spectrum. Scaling the Bohr theory result is accurate for hydrogenic ions, i.e. systems with one electron around a nucleus of charge Ze. In neutral atoms the other electrons (that do not jump) are not simply passive spectators but partly screen the nuclear charge; for a given X-ray line, say the K- to L-shell transition, a more accurate formula is

1/λ = R∞ ((Z − σ_K)^2 / 1^2 − (Z − σ_L)^2 / 2^2). (1.21)

The screening factors σ_K and σ_L are not entirely independent of Z and the values of these screening factors for each shell vary slightly (see the exercises at the end of this chapter). For large atomic numbers this formula tends to eqn 1.20 (see Exercise 1.4). This simple approach does not explain why the screening factor for a shell can exceed the number of electrons inside that shell, e.g. σ_K = 2 for Z = 74 although only one electron remains in this shell when a hole is formed. This does not make sense in a classical model with electrons orbiting around a nucleus, but can be explained by atomic wavefunctions—an electron with a high principal quantum number (and little angular momentum) has a finite probability of being found at small radial distances.

The study of X-rays has developed into a whole field of its own within atomic physics, astrophysics and condensed matter, but there is only room to mention a few brief facts here. When an electron is removed from the K-shell the atom has an amount of energy equal to its binding energy, i.e. a positive amount of energy, and it is therefore usual to draw the diagram with the K-shell at the top, as in Fig. 1.3. These are the energy levels of the hole in the electron shells. This diagram shows why the creation of a hole in a low-lying shell leads to a succession of transitions as the hole works its way outwards through the shells. The hole (or equivalently the falling electron) can jump more than one shell at a time; each line in a series from a given shell is labelled using Greek letters (as in the series in hydrogen), e.g. Kα, Kβ, .... The levels drawn in Fig. 1.3 have some sub-structure and this leads to transitions with slightly different wavelengths, as shown in Moseley’s plot. This is fine structure caused by relativistic effects that we considered for Sommerfeld’s theory; the substitution e^2 / (4πε0) → Ze^2 / (4πε0), as above, (or equivalently α → Zα) shows that fine structure is of order (Zα)^2 times the gross structure, which itself is proportional to Z^2. Thus relativistic effects grow as Z^4 and become very significant for the inner electrons of heavy atoms, leading to the fine structure of the L- and M-shells seen in Fig. 1.3. This relativistic splitting of the shells explains why in Moseley’s plot (Fig. 1.2) there are two closely-spaced curves for the Kα-line, and several curves for the L-series.

Nowadays much of the X-ray work in atomic physics is carried out using sources such as synchrotrons; these devices accelerate electrons by the techniques used in particle accelerators. A beam of high-energy electrons circulates in a ring and the circular motion causes the electrons to radiate X-rays. Such a source can be used to obtain an X-ray absorption spectrum.14 There are many other applications of X-ray emission, e.g. as a diagnostic tool for the processes that occur in plasmas in fusion research and in astrophysical objects. Many interesting processes occur at ‘high energies’ in atomic physics but the emphasis in this book is mainly on lower energies.

## 1.6 Radiative decay

An electric dipole moment −ex oscillating at angular frequency ω radiates a power15 P = e^2 x^2 ω^4 / (12π ε0 c^3). (1.22)

An electron in harmonic motion has a total energy16 of E = m_e ω^2 x^2 / 2, where x is the amplitude of the motion. This energy decreases at a rate equal to the power radiated: dE/dt = −(e^2 ω^2 / (6π ε0 m_e c^3)) E = −E / τ, (1.23)

where the classical radiative lifetime τ is given by 1/τ = e^2 ω^2 / (6π ε0 m_e c^3). (1.24)

For the transition in sodium at a wavelength of 589 nm (yellow light) this equation predicts a value of τ ≈ 16 ns ≈ 10^−8 s. This is very close to the experimentally measured value and typical of allowed transitions that emit visible light. Atomic lifetimes, however, vary over a very wide range,17 e.g. for the Lyman-α transition (shown in Fig. 1.1) the upper level has a lifetime of only a few nanoseconds.18,19 The classical value of the lifetime gives the fastest time in which the atom could decay on a given transition and this is often close to the observed lifetime for strong transitions. Atoms do not decay faster than a classical dipole radiating at the same wavelength, but they may decay more slowly (by many orders of magnitude in the case of forbidden transitions).20

## 1.7 Einstein A and B coefficients

The development of the ideas of atomic structure was linked to experiments on the emission, and absorption, of radiation from atoms, e.g. X-rays or light. The emission of radiation was considered as some...

14 Absorption is easier to interpret than emission since only one of the terms in eqn 1.21 is important, e.g. E_K = hcR∞(Z−σ_K)^2.

15 This total power equals the integral of the Poynting vector over a closed surface in the far-field of radiation from the dipole. This is calculated from the oscillating electric and magnetic fields in this region (see electromagnetism texts or Corney (2000)).

16 The sum of the kinetic and potential energies.

17 The classical lifetime scales as 1/ω^2. However, we will find that the quantum mechanical result is different (see Exercise 1.8).

18 Higher-lying levels, e.g. n = 30, live for many microseconds (Gallagher 1994).

19 Atoms can be excited up to configurations with high principal quantum numbers in laser experiments; such systems are called Rydberg atoms and have small intervals between their energy levels. As expected from the correspondence principle, these Rydberg atoms can be used in experiments that probe the interface between classical and quantum mechanics.

20 The ion-trapping techniques described in Chapter 12 can probe transitions with spontaneous decay rates less than 1 s^−1, using single ions confined by electric and magnetic fields—something that was only a ‘thought experiment’ for Bohr and the other founders of quantum theory. In particular, the effect of individual quantum jumps between atomic energy levels is observed. Radiative decay resembles radioactive decay in that individual atoms spontaneously emit a photon at a given time but taking the average...

hing over an ensemble of atoms gives exponential decay. This just has to happen in order to carry away the energy when an electron jumps from one allowed orbit to another, but the mechanism was not explained.21 In one of his many strokes of genius Einstein devised a way of treating the phenomenon of spontaneous emission quantitatively, based on an intuitive understanding of the process.22

Einstein considered atoms with two levels of energies, E1 and E2, as shown in Fig. 1.4; each level may have more than one state and the number of states with the same energy is the degeneracy of that level represented by g1 and g2. Einstein considered what happens to an atom interacting with radiation of energy density ρ(ω) per unit frequency interval. The radiation causes transitions from the lower to the upper level at a rate proportional to ρ(ω), where the constant of proportionality is B12. The atom interacts strongly only with that part of the distribution ρ(ω) with a frequency close to ω = (E2 - E1)/(cid:1), the atom's resonant frequency.23 By symmetry it is also expected that the radiation will cause transitions from the upper to lower levels at a rate dependent on the energy density but with a constant of proportionality B21 (the subscripts are in a different order for emission as compared to absorption). This is a process of stimulated emission in which the radiation at angular frequency ω causes the atom to emit radiation of the same frequency. This increase in the amount of light at the incident frequency is fundamental to the operation of lasers.24 The symmetry between up and down is broken by the process of spontaneous emission in which an atom falls down to the lower level, even when no external radiation is present. Einstein introduced the coefficient A21 to represent the rate of this process. Thus the rate equations for the populations of the levels, N1 and N2, are

dN2/dt = N1 B12 ρ(ω12) - N2 B21 ρ(ω12) - N2 A21   (1.25)

and

dN1/dt = -dN2/dt.   (1.26)

The first equation gives the rate of change of N2 in terms of the absorption, stimulated emission and spontaneous emission, respectively. The second equation is a consequence of having only two levels so that atoms leaving level 2 must go into level 1; this is equivalent to a condition that N1 + N2 = constant. When ρ(ω) = 0, and some atoms are initially in the upper level (N2(0)(cid:1)=0), the equations have a decaying exponential solution:

N2(t) = N2(0) exp(-A21 t),   (1.27)

where the mean lifetime25 is

1/τ = A21.   (1.28)

Einstein devised a clever argument to find the relationship between the A21- and B-coefficients and this allows a complete treatment of atoms interacting with radiation. Einstein imagined what would happen to such an atom in a region of black-body radiation, e.g. inside a box whose surface acts as a black body. The energy density of the radiation ρ(ω)dω between angular frequency ω and ω+dω depends only on the temperature T of the emitting (and absorbing) surfaces of the box; this function is given by the Planck distribution law:26

ρ(ω) = (cid:1)ω³ / (π²c³(exp((cid:1)ω/kT) - 1)).   (1.29)

Now we consider the level populations of an atom in this black-body radiation. At equilibrium the rates of change of N1 and N2 (in eqn 1.26) are both zero and from eqn 1.25 we find that

ρ(ω12) = A21 / [B21 (N1/N2) (B12/B21) - 1].   (1.30)

At thermal equilibrium the population in each of the states within the levels are given by the Boltzmann factor (the population in each state equals that of the energy level divided by its degeneracy):

N2 / N1 = (g2/g1) exp(-(cid:1)ω12 / kT).   (1.31)

Combining the last three equations (1.29, 1.30 and 1.31) we find27

A21 = (cid:1)ω12³ / (π²c³) * B21   (1.32)

and

B12 = (g2/g1) * B21.   (1.33)

The Einstein coefficients are properties of the atom.28 Therefore these relationships between them hold for any type of radiation, from narrow-bandwidth radiation from a laser to broadband light. Importantly, eqn 1.32 shows that strong absorption is associated with strong emission. Like many of the topics covered in this chapter, Einstein's treatment captured the essential features of the physics long before all the details of the quantum mechanics were fully understood.29

**1.8 The Zeeman effect**

This introductory survey of early atomic physics must include Zeeman's important work on the effect of a magnetic field on atoms. The observation of what we now call the Zeeman effect and three other crucial experiments were carried out just at the end of the nineteenth century, and together these discoveries mark the watershed between classical and quantum physics.30 Before describing Zeeman's work in detail, I shall briefly mention the other three great breakthroughs and their significance for atomic physics. Röntgen discovered mysterious X-rays emitted from discharges, and sparks, that could pass through matter and blacken photographic film.31 At about the same time, Bequerel's discovery of radioactivity opened up the whole field of nuclear physics.32 Another great breakthrough was J. J. Thomson's demonstration that cathode rays in electrical discharge tubes are charged particles whose charge-to-mass ratio does not depend on the gas in the discharge tube. At almost the same time, the observation of the Zeeman effect of a magnetic field showed that there are particles with the same charge-to-mass ratio in atoms (that we now call electrons). The idea that atoms contain electrons is very obvious now but at that time it was a crucial piece in the jigsaw of atomic structure that Bohr put together in his model.

In addition to its historical significance, the Zeeman effect provides a very useful tool for examining the structure of atoms, as we shall see at several places in this book. Somewhat surprisingly, it is possible to explain this effect by a classical-mechanics line of reasoning (in certain special cases). An atom in a magnetic field can be modelled as a simple harmonic oscillator. The restoring force on the electron is the same for displacements in all directions and the oscillator has the same resonant frequency ω0 for motion along the x-, y- and z-directions (when there is no magnetic field). In a magnetic field B the equation of motion for an electron with charge −e, position r and velocity v=ṙ is

m d²r/dt² = -m ω0² r - e v × B.   (1.34)

In addition to the restoring force (assumed to exist without further explanation), there is the Lorentz force that occurs for a charged particle moving through a magnetic field.33 Taking the direction of the field to be the z-axis, B = B e_z leads to

r̈ + 2Ω_L × r̈ + ω0² r = 0.   (1.35)

This contains the Larmor frequency

Ω_L = eB / (2m).   (1.36)

We use a matrix method to solve the equation and look for a solution in the form of a vector oscillating at ω:

r = Re { (x, y, z)ᵀ exp(-iωt) }.   (1.37)

Written in matrix form, eqn 1.35 reads

[ ω0² - 2iωΩ_L    2iωΩ_L      0 ] [x]   [ ω0²   0   0 ] [x]

[  2iωΩ_L    ω0² - 2iωΩ_L      0 ] [y] = [   0 ω0²   0 ] [y]

[     0           0        ω0² ] [z]   [   0   0 ω0² ] [z]

(1.38)

The eigenvalues ω² are found from the following determinant:

| ω0² - ω² - 2iωΩ_L     2iωΩ_L              0       | |    2iωΩ_L      ω0² - ω² - 2iωΩ_L      0       | = 0.   (1.39)

|        0                0           ω0² - ω² |

This gives (ω0² - ω²)[(ω0² - ω²)² + 4Ω_L² ω²] = 0. The solution ω = ω0 is obvious by inspection. The other two eigenvalues can be found exactly by solving the quadratic equation for ω² inside the square brackets. For an optical transition we always have Ω_L (cid:6) ω0 so the approximate eigenfrequencies are ω (cid:3) ω0 ± Ω_L. Substituting these values back into eqn 1.38 gives the eigenvectors corresponding to ω = ω0 - Ω_L, ω0 and ω0 + Ω_L, respectively, as

r = (cos((ω0 - Ω_L)t), -sin((ω0 - Ω_L)t), 0)ᵀ, (0, 0, cos(ω0 t))ᵀ and (cos((ω0 + Ω_L)t), sin((ω0 + Ω_L)t), 0)ᵀ.

The magnetic field does not affect motion along the z-axis and the angular frequency of the oscillation remains ω0. Inter Action with the magnetic field causes the motions in the x- and y-directions to be coupled together (by the off-diagonal elements ±2iωΩ of the matrix in eqn 1.38). The result is two circular motions in opposite directions in the xy-plane, as illustrated in Fig. 1.5. These circular motions have frequencies shifted up, or down, from ω₀ by the Larmor frequency. Thus the action of the external field splits the original oscillation at a single frequency (actually three independent oscillations all with the same frequency, ω₀) into three separate frequencies. An oscillating electron acts as a classical dipole that radiates electromagnetic waves and Zeeman observed the frequency splitting Ω_L in the light emitted by the atom.

This classical model of the Zeeman effect explains the polarization of the light, as well as the splitting of the lines into three components. The calculation of the polarization of the radiation at each of the three different frequencies for a general direction of observation is straightforward using vectors; however, only the particular cases where the radiation propagates parallel and perpendicular to the magnetic field are considered here, i.e. the longitudinal and transverse directions of observation, respectively. An electron oscillating parallel to B radiates an electromagnetic wave with linear polarization and angular frequency ω₀. This π-component of the line is observed in all directions except along the magnetic field; in the special case of transverse observation (i.e. in the xy-plane) the polarization of the π-component lies along ê_z. The circular motion of the oscillating electron in the xy-plane at angular frequencies ω₀ + Ω_L and ω₀ - Ω_L produces radiation at these frequencies. Looking transversely, this circular motion is seen edge-on so that it looks like linear sinusoidal motion, e.g. for observation along the x-axis only the y-component is seen, and the radiation is linearly polarized perpendicular to the magnetic field—see Fig. 1.6. These are called the σ-components and, in contrast to the π-component, they are also seen in longitudinal observation—looking along the z-axis one sees the electron’s circular motion and hence light that has circular polarization. Looking in the opposite direction to the magnetic field (from the positive z-direction, or θ = 0 in polar coordinates) the circular motion in the anticlockwise direction is associated with the frequency ω₀ + Ω_L.

In addition to showing that atoms contain electrons by measuring the magnitude of the charge-to-mass ratio e/m, Zeeman also deduced the sign of the charge by considering the polarization of the emitted light. If the sign of the charge was not negative, as we assumed from the start, light at ω₀ + Ω_L would have the opposite handedness—from this Zeeman could deduce the sign of the electron’s charge.

For situations that only involve orbital angular momentum (and no spin) the predictions of this classical model correspond exactly to those of quantum mechanics (including the correct polarizations), and the intuition gained from this model gives useful guidance in more complicated cases. Another reason for studying the classical treatment of the Zeeman effect is that it furnishes an example of degenerate perturbation theory in classical mechanics. We shall encounter degenerate perturbation theory in quantum mechanics in several places in this book and an understanding of the analogous procedure in classical mechanics is very helpful.

1.8.1 Experimental observation of the Zeeman effect

Figure 1.7(a) shows an apparatus suitable for the experimental observation of the Zeeman effect and Fig. 1.7(b–e) shows some typical experimental traces. A low-pressure discharge lamp that contains the atom to be studied (e.g. helium or cadmium) is placed between the pole pieces of an electromagnet capable of producing fields of up to about 1 T. In the arrangement shown, a lens collects light emitted perpendicular to the field (transverse observation) and sends it through a Fabry–Pérot étalon. The operation of such étalons is described in detail by Brooker (2003), and only a brief outline of the principle of operation is given here.

• Light from the lamp is collected by a lens and directed on to an interference filter that transmits only a narrow band of wavelengths corresponding to a single spectral line.

• The étalon produces an interference pattern that has the form of concentric rings. These rings are observed on a screen in the focal plane of the lens placed after the étalon. A small hole in the screen is positioned at the centre of the pattern so that light in the region of the central fringe falls on a detector, e.g. a photodiode. (Alternatively, the lens and screen can be replaced by a camera that records the ring pattern on film.)

• The effective optical path length between the two flat highly-reflecting mirrors is altered by changing the pressure of the air in the chamber; this scans the étalon over several free-spectral ranges while the intensity of the interference fringes is recorded to give traces as in Fig. 1.7(b–e).

## 1.9 Summary of atomic units

This chapter has used classical mechanics and elementary quantum ideas to introduce the important scales in atomic physics: the unit of length a₀ and a unit of energy hcR∞. The natural unit of energy is e²/(4πε₀) and this unit is called a hartree. This book, however, expresses energy in terms of the energy equivalent to the Rydberg constant, 13.6 eV; this equals the binding energy in the first Bohr orbit of hydrogen, or 1/2 a hartree. These quantities have the following values: a₀ = (4πε₀ℏ²)/(m e²) = 5.29 × 10⁻¹¹ m, (1.40)

hcR∞ = (e²/4πε₀)² m / (2ℏ²) = 13.6 eV. (1.41)

The use of these atomic units makes the calculation of other quantities simple, e.g. the electric field in a hydrogen atom at radius r = a₀ equals e/(4πε₀ a₀²). This corresponds to a potential difference of 27.2 V over a distance of a₀, or a field of 5 × 10¹¹ V m⁻¹.

Relativistic effects depend on the dimensionless fine-structure constant α: α = (e²/4πε₀)/(ℏ c) ≈ 1/137. (1.42)

The Zeeman effect of a magnetic field on atoms leads to a frequency shift of Ω_L in eqn 1.36. In practical units the size of this frequency shift is Ω_L = e B / (4π mₑ) = 14 GHz T⁻¹. (1.43)

Equating the magnetic energy ℏΩ_L with μ B, the magnitude of the energy for a magnetic moment μ in a magnetic flux density B, shows that the unit of atomic magnetic moment is the Bohr magneton μ_B = e ℏ / (2 mₑ) = 9.27 × 10⁻²⁴ J T⁻¹. (1.44)

This magnetic moment depends on the properties of the unpaired electron (or electrons) in the atom, and has a similar magnitude for all atoms. In contrast, other atomic properties scale rapidly with the nuclear charge; hydrogenic systems have energies proportional to Z², and the same reasoning shows that their size is proportional to 1/Z (see eqns 1.40 and 1.41). For example, hydrogenic uranium U⁺⁹¹ has been produced in accelerators by stripping 91 electrons off a uranium atom to leave a single electron that has a binding energy of 92² × 13.6 eV = 115 keV (for n = 1) and an orbit of radius a₀/92 = 5.75 × 10⁻¹³ m ≡ 575 fm. The transitions between the lowest energy levels of this system have short wavelengths in the X-ray region.

the electron units across the whole of atomic physics. In practice, however, the units mec2 = 0.511MeV. The gross energy of the spectra lie in the optical and infrared region, for example, the fine structure is calibrated in Hz (kHz, MHz and GHz); the equation for the angle of diffraction from a grating is expressed in terms of a wavelength; and for X-rays produced by tubes in which electrons are accelerated by high voltages it is natural to use keV.41 A table of useful conversion factors is given inside the back cover. 41Laser techniques can measure transition frequencies of around 10^15 Hz directly as a frequency to determine a precise value of the Rydberg constant, and there are no definite rules for whether a transition should be specified by its energy, wavelength or frequency. The survey of classical ideas in this chapter gives a historical perspective on the origins of atomic physics but it is not necessary, or indeed in some cases downright confusing, to go through a detailed classical treatment—the physics at the scale of atomic systems can only properly be described by wave mechanics and this is the approach used in the following chapters.42 42X-ray spectra are not discussed again in this book and further details can be found in Kuhn (1969) and other atomic physics texts.

Exercises

(1.1) Isotope shift The deuteron has approximately twice the mass of the proton. Calculate the difference in the wavelength of the Balmer-α line in hydrogen and deuterium.

(1.2) The energy levels of one-electron atoms The table gives the wavelength43 of lines observed in the spectrum of atomic hydrogen and singly-ionized helium. Explain as fully as possible the similarities and differences between the two spectra.

H(nm) He+(nm)

## 656.28 656.01

## 486.13 541.16

## 434.05 485.93

## 410.17 454.16

## 433.87 433.87

## 419.99 419.99

## 410.00 410.00

43These are the wavelengths in air with a refractive index of 1.0003 in the visible region.

(1.3) Relativistic effects Evaluate the magnitude of relativistic effects in the n = 2 level of hydrogen. What is the resolving power λ/(∆λ) min of an instrument that could observe these effects in the Balmer-α line?

(1.4) X-rays Show that eqn 1.21 approximates to eqn 1.20 when the atomic number Z is much greater than the screening factors.

(1.5) X-rays It is suspected that manganese (Z = 25) is very poorly mixed with iron (Z = 26) in a block of alloy. Predict the energies of the K-absorption edges of these elements and determine an X-ray photon energy that would give good contrast (between regions of different concentrations) in an X-ray of the block.

(1.6) X-ray experiments Sketch an apparatus suitable for X-ray spectroscopy of elements, e.g. Moseley’s experiment. Describe the principle of its operation and the method of measuring the energy, or wavelength, of X-rays.

(1.7) Fine structure in X-ray transitions Estimate the magnitude of the relativistic effects in the L-shell of lead (Z = 82) in keV. Also express your answer as a fraction of the Kα transition.

(1.8) Radiative lifetime For an electron in a circular orbit of radius r the electric dipole moment has a magnitude of D = −er and radiates energy at a rate given by eqn 1.22. Find the time taken to lose an energy of ℏω. Use your expression to estimate the transition rate for the n = 3 to n = 2 transition in hydrogen that emits light of wavelength 656nm.

Comment. This method gives 1/τ ∝ (er)^2ω^3, which corresponds closely to the quantum mechanical result in eqn 7.23.

(1.9) Black-body radiation Two-level atoms with a transition at wavelength λ=600nm, between the levels with degeneracies g1 = 1 and g2 = 3, are immersed in black-body radiation. The fraction in the excited state is 0.1. What is the temperature of the blackbody and the energy density per unit frequency interval ρ(ω) of the radiation at the transition frequency?

(1.10) Zeeman effect What is the magnitude of the Zeeman shift for an atom in (a) the Earth’s magnetic field, and (b) a magnetic flux density of 1T? Express your answers in both MHz, and as a fraction of the transition frequency ∆f/f for a spectral line in the visible.

(1.11) Relative intensities in the Zeeman effect Without an external field, an atom has no preferred direction and the choice of quantisation axis is arbitrary. In these circumstances the light emitted cannot be polarized (since this would establish a preferred orientation). As a magnetic field is gradually turned on we do not expect the intensities of the different Zeeman components to change discontinuously because the field has little effect on transition rates. This physical argument implies that oppositely-polarized components emitted along the direction of the field must have equal intensities, i.e. I σ+ = I σ− (notation defined in Fig. 1.6). What can you deduce about (a) the relative intensities of the components emitted perpendicularly to the field?

(b) the ratio of the total intensities of light emitted along and perpendicular to the field?

(1.12) Bohr theory and the correspondence principle This exercise gives an alternative approach to the theory of the hydrogen atom presented in Section 1.3 that is close to the spirit of Bohr’s original papers. It is somewhat more subtle than that usually given in elementary textbooks and illustrates Bohr’s great intuition. Rather than the ad hoc assumption that angular momentum is an integral multiple of ℏ (in eqn 1.7), Bohr used the correspondence principle. This principle relates the behaviour of a system according to the known laws of classical mechanics and its quantum properties.

Assumption II The correspondence principle states that in the limit of large quantum numbers a quantum system tends to the same limit as the corresponding classical system.

Bohr formulated this principle in the early days of quantum theory. To apply this principle to hydrogen we first calculate the energy gap between adjacent electron orbits of radii r and r′. For large radii, the change ∆r = r′ − r is small.

(a) Show that the angular frequency ω = ∆E/ℏ of radiation emitted when an electron makes a quantum jump between these levels is ω ≈ e^2/(4πε_0) ∆r / (2ℏ r^2).

(b) An electron moving in a circle of radius r acts as an electric dipole radiating energy at the orbital frequency ω given by eqn 1.4. Verify that this equation follows from eqn 1.3.

(c) In the limit of large quantum numbers, the quantum mechanical and classical expressions give the same frequency ω. Show that equating the expressions in the previous parts yields ∆r=2(a r)^(1/2).

(d) The difference in the radii between two adjacent orbits can be expressed as a difference equation.44 In this case ∆n=1 and ∆r ∝ r^(1/2) (1.45)

for large n.

This equation can be solved by assuming that the radius varies as some power x of the quantum number n, e.g. if one orbit is labelled by an integer n and the next by n+1, then r = a n^x and r′ = a(n+1)^x. Show that ∆r = a x n^{x−1} ∝ n^{x/2}. Determine the power x and the constant a.

Comment. We have found eqn 1.8 from the correspondence principle without considering angular momentum. The allowed energy levels are easily found from this equation as in Section 1.3. The remarkable feature is that, although the form of the equation was derived for high values of the principal quantum number, the result works down to n=1.

44A difference equation is akin to a differential equation but without letting the differences become infinitesimal.

(1.13) Rydberg atoms (a) Show that the energy of the transitions between two shells with principal quantum numbers n and n+1 is proportional to 1/n^3 for large n.

(b) Calculate the frequency of the transition between the n′ = 51 and n = 50 shells of a neutral atom.

(c) What is the size of an atom in these Rydberg states? Express your answer both in atomic units and in metres.

Web site: http://www.physics.ox.ac.uk/users/foot This site has answers to some of the exercises, corrections and other supplementary information.

The hydrogen atom

The simple hydrogen atom has had a great influence on the development of quantum theory, particularly in the first half of the twentieth century when the foundations of quantum mechanics were laid. As measurement techniques improved, finer and finer details were resolved in the spectrum of hydrogen until eventually splittings of the lines were observed that cannot be explained even by the fully relativistic formulation of quantum mechanics, but require the more advanced theory of quantum electrodynamics. In the first chapter we looked at the Bohr–Sommerfeld theory of hydrogen that treated the electron orbits classically and imposed quantisation rules upon them. This theory accounted for many of the features of hydrogen but it fails to provide a realistic description of systems with more than one electron, e.g. the helium atom. Although the simple picture of electrons orbiting the nucleus, like planets round the sun, can explain some phenomena, it has been superseded by the Schrödinger equation and wavefunctions. This chapter outlines the application of this approach to solve Schrödinger’s equation for the hydrogen atom; this leads to the same energy levels as the Bohr model but the wavefunctions give much more information, e.g. they allow the rates of the transitions between levels to be calculated (see Chapter 7). This chapter also shows how the perturbations caused by relativistic effects lead to fine structure.

## 2.1 The Schrödinger equation

The solution of the Schrödinger equation for a Coulomb potential is in every quantum mechanics textbook and only a brief outline is given here.1 The Schrödinger equation for an electron of mass me in a spherically-symmetric potential is [-ℏ^2/(2me) ∇^2 + V(r)] ψ = E ψ. (2.1)

1The emphasis is on the properties of the wavefunctions rather than how to solve differential equations.

2The operator for linear momentum is p = −iℏ∇ and for angular momentum it is ℓ = r × p. This notation differs in The Schrödinger equation is the quantum mechanical counterpart of the classical equation for the conservation of total energy expressed as the sum of kinetic and potential energies.2 In spherical polar coordinates we have ∇² = r² - l², (2.2)

where the operator l² contains the terms that depend on θ and φ, namely l² = -[sinθ ∂/∂θ (sinθ ∂/∂θ) + 1/sin²θ ∂²/∂φ²], (2.3)

and -ħ²l² is the operator for the orbital angular momentum squared. Following the usual procedure for solving partial differential equations, we look for a solution in the form of a product of functions ψ = R(r)Y(θ,φ). The equation separates into radial and angular parts as follows: 1/r² ∂/∂r (r² ∂R/∂r) + 2m/ħ² [E - V(r)] R = l²Y / R. (2.4)

Each side depends on different variables and so the equation is only satisfied if both sides equal a constant that we call b. Thus l²Y = bY. (2.5)

This is an eigenvalue equation and we shall use the quantum theory of angular momentum operators to determine the eigenfunctions Y(θ,φ).

2.1.1 Solution of the angular equation To continue the separation of variables we substitute Y = Θ(θ)Φ(φ) into eqn 2.5 to obtain 1/sinθ ∂/∂θ (sinθ ∂Θ/∂θ) + (b - m²/sin²θ) Θ = 0, (2.6)

The equation for Φ(φ) is the same as in simple harmonic motion, so3 Φ = Aeimφ + Be-imφ. (2.7)

The constant on the right-hand side of eqn 2.6 has the value m². Physically realistic wavefunctions have a unique value at each point and this imposes the condition Φ(φ + 2π) = Φ(φ), so m must be an integer.

The function Φ(φ) is the sum of eigenfunctions of the operator for the z-component of orbital angular momentum lz = -iħ ∂/∂φ. (2.8)

The function eimφ has magnetic quantum number m and its complex conjugate e-imφ has magnetic quantum number -m.4 A convenient way to find the function Y(θ,φ) and its eigenvalue b in eqn 2.5 is to use the ladder operators l+ = lx + ily and l- = lx - ily. These operators commute with l², the operator for the total angular momentum squared (because lx and ly commute with l²); therefore, the three functions Y, l+Y and l-Y are all eigenfunctions of l² with the same eigenvalue b (if they are non-zero, as discussed below). The ladder operators can be expressed in polar coordinates as: l+ = eiφ [∂/∂θ + i cotθ ∂/∂φ], l- = e-iφ [-∂/∂θ + i cotθ ∂/∂φ]. (2.9)

The operator l+ transforms a function with magnetic quantum number m into another angular momentum eigenfunction that has eigenvalue m+1. Thus l+ is called the raising operator.6 The lowering operator l- changes the magnetic quantum number in the other direction, m → m-1. It is straightforward to prove these statements and other properties of these operators;7 however, the purpose of this section is not to present the general theory of angular momentum but simply to outline how to find the eigenfunctions (of the angular part) of the Schrödinger equation.

Repeated application of the raising operator does not increase m indefinitely—for each eigenvalue b there is a maximum value of the magnetic quantum number8 that we shall call l, i.e. m_max = l. The raising operator acting on an eigenfunction with m_max gives zero since by definition there are no eigenfunctions with m > m_max. Thus solving the equation l+ Y = 0 (Exercise 2.11) we find that the eigenfunctions with m = m_max = l have the form Y ∝ sin^l θ e^ilφ. (2.10)

Substitution back into eqn 2.5 shows that these are eigenfunctions of l² with eigenvalue b = l(l+1), and l is the orbital angular momentum quantum number. The functions Y_l,m(θ,φ) are labelled by their eigenvalues in the conventional way.9 For l = 0 only m = 0 exists and Y_0,0 is a constant with no angular dependence. For l = 1 we can find the eigenfunctions by starting from the one with m = m_max = l = 1 (in eqn 2.10) and using the lowering operator to find the others: Y_1,1 ∝ sinθ e^iφ, Y_1,0 ∝ l- Y_1,1 ∝ cosθ, Y_1,-1 ∝ l- Y_1,0 ∝ sinθ e^-iφ.

This gives all three eigenfunctions expected for l = 1.10 For l = 2 this procedure gives Y_2,2 ∝ sin²θ e^i2φ, Y_2,1 ∝ ... (and so on down to Y_2,-2).

These are the five eigenfunctions with m = 2, 1, 0, -1, -2.11 Normalised angular functions are given in Table 2.1.

Any angular momentum eigenstate can be found from eqn 2.10 by repeated application of the lowering operator:12 Y_l,m ∝ (l-)^(l-m) sin^l θ e^ilφ. (2.11)

To understand the properties of atoms, it is important to know what the wavefunctions look like. The angular distribution needs to be multiplied by the radial distribution, calculated in the next section, to give the square of the wavefunction as |ψ(r,θ,φ)|² = R_nl(r)² |Y_l,m(θ,φ)|². (2.12)

This is the probability distribution of the electron, or -e|ψ|² can be interpreted as the electronic charge distribution. Many atomic properties, however, depend mainly on the form of the angular distribution and Fig. 2.1 shows some plots of |Y_l,m|². The function |Y_0,0|² is spherically symmetric. The function |Y_1,0|² has two lobes along the z-axis. The squared modulus of the other two eigenfunctions of l = 1 is proportional to sin²θ. As shown in Fig. 2.1(c), there is a correspondence between these distributions and the circular motion of the electron around the z-axis that we found as the normal modes in the classical theory of the Zeeman effect (in Chapter 1).13 This can be seen in Cartesian coordinates where Y_1,0 ∝ z/r, Y_1,1 ∝ (x + iy)/r, Y_1,-1 ∝ (x - iy)/r. (2.13)

Any linear combination of these is also an eigenfunction of l², e.g.

Y_1,-1 - Y_1,1 ∝ x/r = sinθ cosφ, (2.14)

Y_1,-1 + Y_1,1 ∝ iy/r = sinθ sinφ. (2.15)

These two real functions have the same shape as Y_1,0 ∝ z/r but are aligned along the x- and y-axes, respectively.14 In chemistry these distributions for l = 1 are referred to as p-orbitals.

2.1.2 Solution of the radial equation An equation for R(r) is obtained by setting eqn 2.4 equal to the constant b = l(l+1) and putting in the form for the potential energy V(r).

The Coulomb potential V(r) = -e² / 4πεr. The Schrödinger equation can be cast in a convenient form by the substitution P(r) = rR(r): -ℏ²/(2m) * d²P/dr² + (ℏ²l(l+1))/(2mr²) - e²/4πεr * P = EP = 0. (2.16)

The term proportional to l(l+1)/r² is the kinetic energy associated with the angular degrees of freedom; it appears in this radial equation as an effective potential that tends to keep wavefunctions with l ≠ 0 away from the origin. Dividing through this equation by E = -|E| (a negative quantity since E < 0 for a bound state) and making the substitution ρ² = 2m|E|r² / ℏ² (2.17) reduces the equation to the dimensionless form d²P/dρ² + (l(l+1)/ρ² - λ/ρ - 1)P = 0. (2.18)

The constant that characterises the Coulomb interaction strength is λ = e²/(4πε) * √(2m / ℏ²|E|). (2.19)

The standard method of solving such differential equations is to look for a solution in the form of a series. The series solutions have a finite number of terms and do not diverge when λ = 2n, where n is an integer. Thus, from eqn 2.19, these wavefunctions have eigenenergies given by E = - (2m e²/4πε)² / (ℏ² λ²) = -hcR∞ / n². (2.20)

This shows that the Schrödinger equation has stationary solutions at energies given by the Bohr formula. The energy does not depend on l; this accidental degeneracy of wavefunctions with different l is a special feature of the Coulomb potential. In contrast, degeneracy with respect to the magnetic quantum number ml arises because of the system's symmetry, i.e. an atom's properties are independent of its orientation in space, in the absence of external fields. The solution of the Schrödinger equation gives much more information than just the energies; from the wavefunctions we can calculate other atomic properties in ways that were not possible in the Bohr–Sommerfeld theory.

We have not gone through the gory details of the series solution, but we should examine a few examples of radial wavefunctions (see Table 2.2). Although the energy depends only on n, the shape of the wavefunctions depends on both n and l and these two quantum numbers are used to label the radial functions Rn,l(r). For n = 1 there is only the l = 0 solution, namely R1,0 ∝ e^-ρ. For n = 2 the orbital angular momentum quantum number is l=0 or 1, giving R2,0 ∝ (1-ρ)e^-ρ, R2,1 ∝ ρe^-ρ.

Table 2.2 Radial hydrogenic wavefunctions Rn,l in terms of the variable ρ = Zr/(na0), which gives a scaling that varies with n. The Bohr radius a0 is defined in eqn 1.40.

R1,0 = 2 (Z/a0)^(3/2) e^-ρ R2,0 = (2 (Z/a0)^(3/2)) / (√2) (1-ρ)e^-ρ R2,1 = (2 (Z/a0)^(3/2)) / (√2·√3) ρe^-ρ R3,0 = (2 (Z/a0)^(3/2)) / (3√3) (1 - 2ρ + 2/3 ρ²) e^-ρ R3,1 = (2 (Z/a0)^(3/2)) / (3√3·√2) ρ (1 - 1/2 ρ) e^-ρ R3,2 = (2 (Z/a0)^(3/2)) / (3√3·√6) ρ² e^-ρ Normalisation: ∫ Rn,l² r² dr = 1 These show a general feature of hydrogenic wavefunctions, namely that the radial functions for l = 0 have a finite value at the origin, i.e. the power series in ρ starts at the zeroth power. Thus electrons with l = 0 (called s-electrons) have a finite probability of being found at the position of the nucleus and this has important consequences in atomic physics.

Inserting |E| from eqn 2.20 into eqn 2.17 gives the scaled coordinate ρ = Zr/(na), (2.21) where the atomic number has been incorporated by the replacement e²/4πε → Ze²/4πε (as in Chapter 1). There are some important properties of the radial wavefunctions that require a general form of the solution and for future reference we state these results. The probability density of electrons with l = 0 at the origin is |ψn,l=0(0)|² = (1/π) (Z/(na))³. (2.22)

For electrons with l ≠ 0 the expectation value of 1/r³ is ⟨1/r³⟩ = ∫ R²n,l(r) r² dr / r³ = (Z³) / (l(l+1/2)(l+1) n³a0³). (2.23)

These results have been written in a form that is easy to remember; they must both depend on 1/a0³ in order to have the correct dimensions and the dependence on Z follows from the scaling of the Schrödinger equation. The dependence on the principal quantum number n also seems to follow from eqn 2.21 but this is coincidental; a counterexample is ⟨1/r⟩ = Z/(n²a0). (2.24)

## 2.2 Transitions

The wavefunction solutions of the Schrödinger equation for particular energies are standing waves and give a distribution of electronic charge -e|ψ(r)|² that is constant in time. We shall now consider how transitions between these stationary states occur when the atom interacts with electromagnetic radiation that produces an oscillating electric field E(t) = |E0| Re [e^{-iωt} e_rad] (2.25) with constant amplitude |E0| and polarization vector e_rad. If ω lies close to the atomic resonance frequency then the perturbing electric field puts the atom into a superposition of different states and induces an oscillating electric dipole moment on the atom (see Exercise 2.10). The calculation of the stimulated transition rate requires time-dependent perturbation theory (TDPT), as described in Chapter 7. However, the treatment from first principles is lengthy and we shall anticipate some of the results so that we can see how spectra relate to the underlying structure of the atomic energy levels. This does not require an exact calculation of transition rates, but we only need to determine whether the transition rate has a finite value or whether it is zero (to first order), i.e. whether the transition is allowed and gives a strong spectral line, or is forbidden.

The result of time-dependent perturbation theory is encapsulated in the golden rule (or Fermi’s golden rule); this states that the rate of transitions is proportional to the square of the matrix element of the perturbation. The Hamiltonian that describes the time-dependent interaction with the field in eqn 2.25 is H' = -er·E(t), where the electric dipole operator is -er. This interaction with the radiation stimulates transitions from state 1 to state 2 at a rate Rate ∝ |eE0|² |⟨2| r·e_rad |1⟩|² ≡ |eE0|² × |D12·e_rad|². (2.26)

The concise expression in Dirac notation is convenient for later use. This treatment assumes that the amplitude of the electric field is uniform over the atom so that it can be taken outside the integral over the atomic wavefunctions, i.e. that E0 does not depend on r. We write the dipole matrix element as the product D12 = I_rad × I_ang. (2.27)

The radial integral is I_rad = ∫ R*_{n2,l2}(r) r R_{n1,l1}(r) r² dr. (2.28)

The angular integral is I_ang = ∫∫ Y*_{l2,m2}(θ,φ) r·e_rad Y_{l1,m1}(θ,φ) sinθ dθ dφ, (2.29) where r̂ = r/r. The radial integral is not normally zero although it can be small for transitions between states whose radial wavefunctions have a small overlap, e.g. when n1 is small and n2 is large (or the other way round). In contrast, the I_ang = 0 unless strict criteria are satisfied—these are the selection rules.

2.2.1 Selection rules The selection rules that govern allowed transitions arise from the angular integral in eqn 2.29 which contains the angular dependence of the interaction r̂·e_rad for a given polarization of the radiation. The mathematics requires that we calculate I_ang for an atom with a well-defined quantisation axis (invariably chosen to be the z-axis) and radiation that has a well-defined polarization and direction of propagation. This corresponds to the physical situation of an atom experiencing the Zeeman effect of an external magnetic field, as described in Section 1.8; that treatment of the electron as a classical oscillator showed that the components of different frequencies within the Zeeman pattern have different polarizations. We use the same nomenclature of π- and σ-transitions here; transverse observation refers to radiation emitted perpendicular to the magnetic field, and longitudinal observation is along the z-axis. To calculate I_ang we write the unit vector r̂ in the direction of the...

外部场)或辐射是未极化的(或两者兼有)，则计算结束时需对所有角度取平均。

向量r可表示为： r = x ex + y ey + z ez = sinθcosφ ex + sinθsinφ ey + cosθ ez. (2.30)

将θ和φ的函数用球谐函数表示： sinθcosφ = √(2π) (Y₁,₋₁ − Y₁,₁), sinθsinφ = i√(2π) (Y₁,₋₁ + Y₁,₁), (2.31)

cosθ = √(4π) Y₁,₀, 可得： r ∝ Y₁,₋₁ (ex/√2 + i ey) + Y₁,₀ ez + Y₁,₁ (−ex/√2 + i ey). (2.32)

我们将极化矢量一般地写成： e_rad = A_σ₋ (ex/√2 − i ey) + A_π ez + A_σ₊ (ex/√2 + i ey), (2.33)

其中A_π取决于电场沿z轴的分量，而xy平面内的分量则写成两个圆偏振的叠加，振幅为A_σ₊和A_σ₋(而不是用笛卡尔基中的线偏振表示)。27 同样，27 我们将看到标签π, σ₊和σ₋指的是辐射所激发的跃迁类型；对此只需知道原子位置处电场的行为。与此电场相关的偏振态，例如它是右旋还是左旋圆偏振辐射，也取决于传播方向(波矢)，但我们将避免在此原理讨论中详细处理偏振约定。然而，在设置实际实验时，显然拥有正确的偏振非常重要。

在第1.8节中，电子的经典运动是用三个特征矢量来写的：沿z轴的振荡运动和xy平面内的圆周运动(顺时针和逆时针方向)。

由r用角函数Y_{l,m}(θ,φ)表示(l=1)的式子可得，原子上感应的偶极矩正比于28 28 这些特征矢量具有以下性质： (ex/√2 + i ey)(ex/√2 − i ey) = 1 以及 (ex/√2 ± i ey)(ex/√2 ± i ey) = 0.

r · e_rad ∝ A_σ₋ Y₁,₋₁ + A_z Y₁,₀ + A_σ₊ Y₁,₊₁. (2.34)

以下各节将讨论由这三项产生的跃迁。29 29 在球张量表示中(Woodgate 1980)，三个矢量分量写为A₋₁, A₀和A₊₁，这对更一般的应用很方便；但将公式2.34写成极化形式以及球谐函数来自原子响应(感应偶极矩)，磁量子数不会改变，Δm_l = 0。30 30 另有其他方法见下文及练习2.9。

π-跃迁电场沿z轴的分量A_z在原子上诱导的偶极矩正比于e_rad · ez = cosθ，而对波函数角度部分的积分是： ∫₀²π ∫₀^π Y_{l₂,m₂}(θ,φ) cosθ Y_{l₁,m₁}(θ,φ) sinθ dθ dφ. (2.35)

为了计算这个积分，我们利用其绕z轴旋转的对称性。30 系统具有柱对称性，因此该积分值在绕z轴旋转任意角度φ₀后保持不变： I_ang = e^{i(m₁−m₂)φ₀} I_ang. (2.36)

此方程在I_ang = 0或m_{l₁} = m_{l₂}时成立。对于这种情况，磁量子数不变，Δm_l = 0。31 31 我们使用m_l以区别于m_s，即在角动量中引入的磁量子数。对空间变量的特定函数不需要进一步说明。

σ-跃迁 xy平面内的振荡电场分量激发σ-跃迁。公式2.34表明，振幅为A_σ₊的圆偏振辐射在原子上激发振荡偶极矩，正比于Y₁,₁ ∝ sinθ e^{iφ}，其角度积分为： ∫₀²π ∫₀^π Y_{l₂,m₂}(θ,φ) sinθ e^{iφ} Y_{l₁,m₁}(θ,φ) sinθ dθ dφ. (2.37)

再次考虑绕z轴旋转的对称性，表明除非m_{l₁} − m_{l₂} + 1 = 0，否则I_ang = 0。原子与相反旋向的圆偏振辐射相互作用导致类似的积分，但e^{iφ} → e^{−iφ}；除非m_{l₁} − m_{l₂} − 1 = 0，否则该积分I_ang = 0。因此σ-跃迁的选择定则是Δm_l = ±1。

我们已经分别找到了控制三种可能辐射偏振下Δm_l变化的选择定则。当偏振光与具有明确取向的原子(例如处于外磁场中的原子)相互作用时，适用这些定则。如果光是非偏振的，或者没有确定的量子化轴，或者两者兼有，则Δm_l = 0, ±1。

示例 2.1 纵向观测电磁辐射是横波，其振荡电场垂直于传播方向，e_rad · k = 0。因此，波矢k = k ez的辐射具有A_z = 0，π-跃迁不会发生。32 沿z轴传播的圆偏振辐射是一种特殊情况，根据辐射的旋向，要么发生Δm_l = +1，要么发生Δm_l = −1的跃迁，但不会两者同时发生。

32 这种行为也出现在第1.8节正常塞曼效应的经典模型中，但本节的量子处理表明，它是纵向观测的一个普遍特征——不仅仅适用于正常塞曼效应。

2.2.2 对θ的积分在角度积分中，l=1的球谐函数(来自公式2.34)夹在初始态和末态的角度动量波函数之间，因此 I_ang ∝ ∫₀²π ∫₀^π Y_{l₂,m₂} Y_{1,m} Y_{l₁,m₁} sinθ dθ dφ. (2.38)

33 参见量子力学中角动量的相关文献；正交归一性关系为： 为了计算这个角度积分，我们使用以下公式：33 Y_{1,m} Y_{l₁,m₁} = A Y_{l₁+1, m₁+m} + B Y_{l₁−1, m₁+m}, (2.39)

其中A和B是常数，其具体值我们无需关心。

34 我们有： ∫₀²π ∫₀^π Y_{l',m'} Y_{l,m} sinθ dθ dφ = δ_{l',l} δ_{m',m}.

当l'=l时，这简化为表2.1中的归一化。

因此，根据球谐函数的正交性34，我们得到： I_ang ∝ A δ_{l₂, l₁+1} δ_{m₂, m₁+m} + B δ_{l₂, l₁−1} δ_{m₂, m₁+m}.

δ函数给出了之前找到的选择定则，即Δm_l = m，其中m = 0, ±1取决于偏振，以及Δl = ±1。在数学上，代表与辐射相互作用的l=1的函数被夹在初始态和末态的轨道角动量本征函数之间。因此，Δl = ±1的规则可以解释为携带一个单位角动量的光子的角动量守恒，ℏ (图2.8针对总角动量的情况说明了这一推理)。35 35 此论证仅适用于电偶极辐射。更高阶的项，例如四极辐射，可以给出Δl > 1。

磁量子数的较高阶变化也与此图像一致——光子角动量沿z轴的分量为Δm_l = 0, ±1。角动量守恒并不能解释为什么Δl ≠ 0——这源于宇称，如下所述。

2.2.3 宇称宇称是原子和分子物理中一个重要的对称性质，在将其应用于选择定则之前，我们将先解释其一般用途。宇称变换是通过原点的反演，由r → −r给出。这等价于以下极坐标的变换： θ → π − θ：反射， φ → φ + π：旋转。

反射产生原始系统的镜像，宇称也被称为镜像对称。氢原子的镜像具有与原始原子相同的能级，因为库仑势在反射后保持不变。事实证明，所有电磁相互作用在反射后“看起来相同”，所有原子都具有宇称对称性。36 为了找到宇称的本征值，我们使用完整的量子力学表示，用帽子区分算符P与其本征值P： 36 这可以在量子力学中通过证明这些相互作用的哈密顿算符与宇称算符对易来正式证明。核物理中的弱相互作用不具有镜像对称性，违反了宇称守恒。弱相互作用对原子极其微小的影响已在极其仔细和精确的实验中测量到。

P̂ ψ = P ψ, (2.40)

由此可得P̂² ψ = P² ψ。两次连续的宇称操作对应于没有变化(恒等算符)，即r → −r → r。因此P² = 1。所以宇称算符的本征值为P = 1和−1，分别对应于偶宇称和奇宇称波函数： P̂ ψ = ψ 或 P̂ ψ = −ψ.

这两个本征值都出现在球谐函数中： P̂ Y_{l,m} = (−1)^l Y_{l,m}. (2.41)

角度积分的值在宇称变换下不变37，所以 37 参见例如Mandl (1992)。

I_ang = (−1)^{l₂+l₁+1} I_ang. (2.42)

因此，除非初始态和末态具有相反的宇称，否则积分为零(见练习2.12)。特别是，电偶极跃迁要求轨道角动量量子数发生奇数变化(Δl ≠ 0)。38 38 径向积分不受宇称变换影响。

上述宇称算符作用于波函数的处理方法相当普遍，即使在复杂原子中，波函数也具有确定的宇称。本节中我们讨论的选择定则及其他定则列于附录C中。如果两个态之间的电偶极矩阵元为零，则可能发生其他类型的跃迁，但其速率比允许跃迁慢许多个数量级。

原子氢n = 1、2和3壳层之间的允许跃迁如图2.2所示，作为选择定则的一个例子。2s组态没有向下的允许跃迁；这使其成为亚稳态，即具有约0.125秒的非常长的寿命。39 39 这一特殊性质被用于实验中。

最后，关于光谱的 spectroscopic notation. It can be seen in Fig. 2.2 that the allowed transitions give rise to several series of lines. The series of lines to the ground configuration is called the p-series, where p stands for principal—this is the only series observed in absorption⁴⁰—hence p labels configurations with l = 1. The s-series of lines goes from l=0 configurations (to a level with l=1), and similarly the d-series goes from l=2 configurations; s and d stand for sharp and diffuse, respectively.⁴¹

Fig. 2.2 Allowed transitions between the configurations of hydrogen obey the selection rule ∆l = ±1. The configurations with l = 0,1,2,3,4,... are labelled s,p,d,f,g, and so on alphabetically (the usual convention). In the special case of hydrogen the energy does not depend on the quantum number l.

⁴⁰For hydrogen this is the Lyman series, as marked on Fig. 1.1.

⁴¹These names reflect the appearance of the lines in the first experimental observations.

## 2.3 Fine structure

Relativistic effects lead to small splittings of the atomic energy levels called fine structure. We estimated the size of this structure in Section 1.4 by comparing the speed of electrons in classical orbits with the speed of light.⁴² In this section we look at how to calculate fine structure by treating relativistic effects as a perturbation to the solutions of the Schrödinger equation. This approach requires the concept that electrons have spin.

⁴²By considering elliptical orbits, rather than just circular ones, Sommerfeld refined Bohr’s theory to obtain a relativistic expression for the energy levels in hydrogen that gave very accurate predictions of the fine structure; however, details of that approach are not given here.

2.3.1 Spin of the electron

In addition to the evidence provided by observations of the fine structure itself, that is described in this section, two other experiments showed that the electron has spin angular momentum, not just orbital angular momentum. One of these pieces of experimental evidence for spin was the observation of the so-called anomalous Zeeman effect. For many atoms, e.g. hydrogen and sodium, the splitting of their spectral lines in a magnetic field does not have the pattern predicted by the normal Zeeman effect (that we found classically in Section 1.8). This anomalous Zeeman effect has a straightforward explanation in terms of electron spin (as shown in Section 5.5). The second experiment was the famous Stern–Gerlach experiment that will be described in Section 6.4.1.⁴³

⁴³The fine structure, anomalous Zeeman effect and Stern–Gerlach experiment all involve the interaction of the electron’s magnetic moment with a magnetic field—the internal field of the atom in the case of fine structure. Stern and Gerlach detected the magnetic interaction by its influence on the atom’s motion, whereas the Zeeman effect and fine structure are observed by spectroscopy.

Unlike orbital angular momentum, spin does not have eigenstates that are functions of the angular coordinates. Spin is a more abstract concept and it is convenient to write its eigenstates in Dirac’s ket notation as |s mₛ⟩. The full wavefunction for a one-electron atom is the product of the radial, angular and spin wavefunctions: Ψ = Rₙ,ₗ(r) Yₗ,ₘ(θ,φ) |s mₛ⟩. Or, using ket notation for all of the angular momentum, not just the spin, Ψ = Rₙ,ₗ(r) |l mₗ s mₛ⟩. (2.43)

These atomic wavefunctions provide a basis in which to calculate the effect of perturbations on the atom. However, some problems do not require the full machinery of (degenerate) perturbation theory and for the time being we shall treat the orbital and spin angular momenta by analogy with classical vectors. To a large extent this vector model is intuitively obvious and we start to use it without formal derivations. But note the following points. An often-used shorthand for the spin eigenfunctions is spin-up: |s = 1/2, mₛ = 1/2⟩ ≡ |↑⟩, (2.44) and similarly |↓⟩ for the mₛ = −1/2 state (spin-down). However, in quantum mechanics the angular momentum cannot be completely aligned ‘up’ or ‘down’ with respect to the z-axis, otherwise the x- and y-components would be zero and we would know all three components simultaneously.⁴⁴ The vector model mimics this feature with classical vectors drawn with length |s| = √[s(s+1)] = √3/2. (Only the expectation value of the square of the angular momentum has meaning in quantum mechanics.) The spin-up and spin-down states are as illustrated in Fig. 2.3 with components along the z-axis of ±1. We can think of the vector as rotating around the z-axis, or just having an undefined direction in the xy-plane corresponding to a lack of knowledge of the x- and y-components (see also Grant and Phillips 2001).

⁴⁴This is not possible since the operators for the x-, y- and z-components of angular momentum do not commute (save in a few special cases; we can know that sₓ = sᵧ = s_z = 0 if s = 0).

The name ‘spin’ invokes an analogy with a classical system spinning on its axis, e.g. a sphere rotating about an axis through its centre of mass, but this mental picture has to be treated with caution; spin cannot be equal to the sum of the orbital angular momenta of the constituents since that will always be an integer multiple of ℏ. In any case, the electron is a structureless elementary particle with no measurable size. So we are left with the experimental fact that the electron has an intrinsic spin angular momentum of ℏ/2 and these half-integer values are perfectly acceptable within the general theory of angular momentum in quantum mechanics.

Fig. 2.3 The representation of (a) spin-up and (b) spin-down states as vectors precessing around the z-axis.

2.3.2 The spin–orbit interaction

The Schrödinger equation is non-relativistic, as can readily be seen by looking at the kinetic-energy operator that is equivalent to the non-relativistic expression p²/2m. Some of the relativistic effects can be taken into account as follows. An electron moving through an electric field E experiences an effective magnetic field B given by B = −(1/c²) v × E. (2.45) This is a consequence of the way an electric field behaves under a Lorentz transformation from a stationary to a moving frame in special relativity. Although a derivation of this equation is not given here, it is certainly plausible since special relativity and electromagnetism are intimately linked through the speed of light c = 1/√(ε₀μ₀). This equation for the speed of electromagnetic waves in a vacuum comes from Maxwell’s equations; ε₀ being associated with the electric field and μ₀ with the magnetic field. Rearrangement to give μ₀ = 1/(ε₀c²) suggests that magnetic fields arise from electrodynamics and relativity.⁴⁵

⁴⁵The Biot–Savart law for the magnetic field from a current flowing along a straight wire can be recovered from the Lorentz transformation and Coulomb’s law (Griffiths 1999). However, this link can only be made in this direction for simple cases and generally the phenomenon of magnetism cannot be ‘derived’ in this way.

We now manipulate eqn 2.45 into a convenient form, by substituting for the electric field in terms of the gradient of the potential energy V and unit vector in the radial direction: E = −(1/e) (∂V/∂r) r̂. (2.46) The factor of e comes in because the electron’s potential energy V equals its charge −e times the electrostatic potential. From eqn 2.45 we have B = −(1/c²) v × [−(1/e)(∂V/∂r) r̂] = (1/(mc²e))(∂V/∂r) (m v × r̂) = (1/(mc²e))(∂V/∂r) L, (2.47) where the orbital angular momentum is L = r × m v. The electron has an intrinsic magnetic moment μ = −gₛμ_B s, where the spin has a magnitude of |s| = √[s(s+1)] = √3/2 (in units of ℏ) and gₛ ≈ 2, so the moment has a magnitude close to one Bohr magneton (μ_B = eℏ/2m). The interaction of the electron’s magnetic moment with the orbital field gives the Hamiltonian H = −μ · B = gₛμ_B s · [(1/(mc²e))(∂V/∂r) L]. (2.48)

However, this expression gives energy splittings about twice as large as observed. The discrepancy comes from the Thomas precession—a relativistic effect that arises because we are calculating the magnetic field in a frame of reference that is not stationary but rotates as the electron moves about the nucleus. The effect is taken into account by replacing gₛ with gₛ − 1 ≈ 1.⁴⁶ Finally, we find the spin–orbit interaction, including the Thomas precession factor, is⁴⁷ Hₛ₋ₒ = (gₛ − 1) [1/(2m²c²)] (∂V/∂r) s · L. (2.49)

⁴⁶This is almost equivalent to using gₛ/2 ≈ 1, but gₛ − 1 is more accurate at the level of precision where the small deviation of gₛ from 2 is important (Haar and Curtis 1987). For further discussion of Thomas precession see Cowan (1981), Eisberg and Resnick (1985) and Munoz (2001).

⁴⁷We have derived this classically, e.g. by using L = r × m v. However, the same expression can be obtained from the fully relativistic Dirac equation for an electron in a Coulomb potential by making a low-velocity approximation, see Sakurai (1967). That quantum mechanical approach justifies treating L and s as operators.

For the Coulomb potential in hydrogen we have (∂V/∂r)/r = (e²/4πε₀)/r³. (2.50) The expectation value of this Hamiltonian gives an energy change of⁴⁸ Eₛ₋ₒ = [1/(2m²c²)] (e²/4πε₀) ⟨1/r³⟩ ⟨s · L⟩. (2.51)

⁴⁸Using the approximation gₛ − 1 ≈ 1.

The separation into a product of radial and angular expectation values follows from the separability of the wavefunction. The integral 1/r³ is given in eqn 2.23. However, we have not yet discussed how to deal with interactions that have the form of dot products of two angular momenta; let us start by defining the total angular momentum of the atom as the sum of its orbital and spin angular momenta, j = L + s. (2.52) This is a conserved quantity for a system without any external torque acting on it, e.g. an atom in a field-free region.

The spin–orbit interaction between l and s causes these vectors to change direction, and because their sum is constrained to be equal to j they move around as shown in Fig. 2.4. In this precession about j the magnitudes of l and s remain constant. The magnetic moment (proportional to s) is not altered in an interaction with a magnetic field, and because of the symmetrical form of the interaction in eqn 2.49, we do not expect l to have any differently. See also Blundell (2001) and Section 5.1.

Squaring and rearranging eqn 2.52, we find that 2s·l = j² − l² − s². Hence we can find the expectation value in terms of the known values for j², l² and s² as

⟨s·l⟩ = {j(j+1) − l(l+1) − s(s+1)}. (2.53)

Thus the spin–orbit interaction produces a shift in energy of

E s−o = β {j(j+1) − l(l+1) − s(s+1)}, (2.54)

where the spin–orbit constant β is (from eqns 2.51 and 2.23)

β = (1 / 2m_e²c²) (e² / 4πε₀) 1 / (na₀)³ l(l+1/2)(l+1) . (2.55)

A single electron has s = 1/2 so, for each l, its total angular momentum quantum number j has two possible values:

j = l + 1/2 or l − 1/2.

From eqn 2.54 we find that the energy interval between these levels, ΔE s−o = E j=l+1/2 − E j=l−1/2, is

ΔE s−o = β (l + 1/2) = (cR α²) / (n³ l(l+1)) . (2.56)

As shown in Section 1.9, m_eαca₀ = ħ and hcR∞ = (e²/4πε₀)/(2a₀). Or, expressed in terms of the gross energy E(n) in eqn 1.10,

ΔE s−o = α² / (n l(l+1)) E(n). (2.57)

This agrees with the qualitative discussion in Section 1.4, where we showed that relativistic effects cause energy changes of order α² times the gross structure. The more complete expression above shows that the energy intervals between levels decrease as n and l increase. The largest interval in hydrogen occurs for n = 2 and l = 1; for this configuration the spin–orbit interaction leads to levels with j = 1/2 and j = 3/2. The full designation of these levels is 2p²P₁/₂ and 2p²P₃/₂, in the notation that will be introduced for the LS-coupling scheme. But some of the quantum numbers (defined in Chapter 5) are superfluous for atoms with a single valence electron and a convenient short form is to denote these two levels by ²P₁/₂ and ²P₃/₂; these correspond to nPj, where P represents the (total) orbital angular momentum for this case. (The capital letters are consistent with later usage.) Similarly, we may write ²S₁/₂ for the 2s²S level; ³D₃/₂ and ³D₅/₂ for the j = 3/2 and 5/2 levels, respectively, that arise from the 3d configuration. Another short form found in the literature is 2²P₁/₂ and 2²P₃/₂. But the full notation must be used whenever ambiguity might arise.

2.3.3 The fine structure of hydrogen

As an example of fine structure, we look in detail at the levels that arise from the n = 2 and n = 3 shells of hydrogen. Equation 2.54 predicts that, for the 2p configuration, the fine-structure levels have energies of

E s−o(²P₁/₂) = −β 2p, E s−o(²P₃/₂) = +½ β 2p,

as shown in Fig. 2.5(a). For the 3d configuration

E s−o(³D₃/₂) = −½ β 3d, E s−o(³D₅/₂) = +β 3d,

as shown in Fig. 2.5(b). For both configurations, it is easy to see that the spin–orbit interaction does not shift the mean energy

E̅ = [(2j+1)Ej(n,l) + (2j'+1)Ej'(n,l)] / (2(2l+1)), (2.58)

where j' = l−1/2 and j = l+1/2 for the two levels. This calculation of the ‘centre of gravity’ for all the states takes into account the degeneracy of each level.

The spin–orbit interaction does not affect the 2S₁/₂ or 3S₁/₂ so we might expect these levels to lie close to the centre of gravity of the configurations with l > 0. This is not the case. Fig. 2.6 shows the energies of the levels for the n = 3 shell given by a fully relativistic calculation. We can see that there are other effects of similar magnitude to the spin–orbit interaction that affect these levels in hydrogen. Quite remarkably, these additional relativistic effects shift the levels by just the right amount to make nP₁/₂ levels degenerate with the nS₁/₂ levels, and nP₃/₂ degenerate with nD₃/₂. This structure does not occur by chance, but points to a deeper underlying cause. The full explanation of these observations requires relativistic quantum mechanics and the technical details of such calculations lie beyond the scope of this book. We shall simply quote the solution of the Dirac equation for an electron in a Coulomb potential; this gives a formula for the energy E_Dirac(n, j) that depends only on n and j, i.e. it gives the same energy for levels of the same n and j but different l, as in the cases above. In a comparison of the exact relativistic solution of the Dirac equation and the non-relativistic energy levels, three relativistic effects can be distinguished.

(a) There is a straightforward relativistic shift of the energy (or equivalently mass), related to the binomial expansion of γ = (1−v²/c²)⁻¹/², in eqn 1.16. The term of order v²/c² gives the non-relativistic kinetic energy p²/2m. The next term in the expansion is proportional to v⁴/c⁴ and gives an energy shift of order v²/c² times the gross structure—this is the effect that we estimated in Section 1.4.

(b) For electrons with l≠0, the comparison of the Dirac and Schrödinger equations shows that there is a spin–orbit interaction of the form given above, with the Thomas precession factor naturally included.

(c) For electrons with l = 0 there is a Darwin term proportional to |ψ(r = 0)|² that has no classical analogue (see Woodgate (1980) for further details).

That these different contributions conspire together to perturb the wavefunctions such that levels of the same n and j are degenerate seems improbable from a non-relativistic point of view. It is worth reiterating the statement above that this structure arises from the relativistic Dirac equation; making an approximation for small v²/c² shows that these three corrections, and no others, need to be applied to the (non-relativistic) energies found from the Schrödinger equation.

2.3.4 The Lamb shift

Figure 2.7 shows the actual energy levels of the n=2 and n=3 shells. According to relativistic quantum theory the 2S₁/₂ level should be exactly degenerate with 2P₁/₂ because they both have n=2 and j=1/2, but in reality there is an energy interval between them, E(2S₁/₂) − E(2P₁/₂) ≈ 1 GHz. The shift of the 2S₁/₂ level to a higher energy (lower binding energy) than the E_Dirac(n=2, j=1/₂) is about one-tenth of the interval between the two fine-structure levels, E(2P₃/₂) − E(2P₁/₂) ≈ 11 GHz. Although small, this discrepancy in hydrogen was of great historical importance in physics. For this simple one-electron atom the predictions of the Dirac equation are very precise and that theory cannot account for Lamb and Retherford’s experimental measurement that the 2S₁/₂ level is indeed higher than the 2P₁/₂ level. The explanation of this Lamb shift goes beyond relativistic quantum mechanics and requires quantum electrodynamics (QED)—the quantum field theory that describes electromagnetic interactions. Indeed, the observation of the Lamb shift experiment was a stimulus for the development of this theory. An intriguing feature of QED is so-called vacuum fluctuations—regions of free space are not regarded as being completely empty but are permeated by fluctuating electromagnetic fields. The QED effects lead to a significant energy shift for electrons with l = 0 and hence break the degeneracy of 2S₁/₂ and 2P₁/₂. The largest QED shift occurs for the 1S₁/₂ ground level of hydrogen but there is no other level nearby and so a determination of its energy requires a precise measurement of a single frequency.

The energy levels of s-electrons shift upwards relative to the position \(E_{\text{Dirac}}(n=2, j=1/2)\) and are therefore not degenerate with the \(2p \, ^2P_{1/2}\) level. Such a shift occurs for all the s-electrons (but the size of the energy shift decreases with increasing \(n\)). The explanation of this shift, known as the Lamb shift, takes us beyond relativistic quantum mechanics into the realm of quantum electrodynamics (QED)—the quantum field theory that describes electromagnetic interactions.

**Fig. 2.8** The conservation of total angular momentum in electric dipole transitions that gives the selection rule in eqn 2.59 can be represented as vector addition. The photon has one unit of angular momentum, and so to go from level \(j_1\) to \(j_2\) the vectors must form a triangle, as shown for the case of (a) \(j_1 = 1/2\) to \(j_2 = 1/2\), (b) \(j_1 = 1/2\) to \(j_2 = 3/2\) and (c) \(j_1 = 3/2\) to \(j_2 = 3/2\).

The near degeneracy of the two \(j = 1/2\) levels with \(n = 2\) was crucial in Lamb’s experiment. Another important feature in that experiment was the metastability of the \(2S_{1/2}\) level, whose lifetime was given in Section 2.2.3. That level decays \(\sim 10^8\) times more slowly than that of \(2P_{1/2}\). In an atomic beam of hydrogen (at room temperature) the atoms have typical velocities of about 3000 m s\(^{-1}\) and atoms excited into the \(2p\) configuration travel an average distance of only \(5 \times 10^{-6}\) m before decaying with the emission of Lyman-\(\alpha\) radiation. In contrast, metastable atoms travel the full length of the apparatus (\(\sim\) 1 m) and are de-excited when they collide with a detector (or the wall of the vacuum chamber). Hydrogen, and hydrogenic systems, are still used for experimental tests of fundamental theory because their simplicity allows very precise predictions.

**2.3.5 Transitions between fine-structure levels** Transitions in hydrogen between the fine-structure levels with principal quantum numbers \(n = 2\) and \(3\) give the components of the Balmer-\(\alpha\) line shown in Fig. 2.7; in order of increasing energy, the seven allowed transitions between the levels with different \(j\) are as follows: \[ 2P_{3/2} - 3S_{1/2}, \quad 2P_{3/2} - 3D_{3/2}, \quad 2P_{3/2} - 3D_{5/2}, \quad 2S_{1/2} - 3P_{1/2}, \quad 2P_{1/2} - 3S_{1/2}, \quad 2S_{1/2} - 3P_{3/2}, \quad 2P_{1/2} - 3D_{3/2}.

\]

These obey the selection rule \(\Delta l = \pm 1\) but an additional rule prevents a transition between \(2P_{1/2}\) and \(3D_{5/2}\), namely that the change of the total angular momentum quantum number in an electric dipole transition obeys \[ \Delta j = 0, \pm 1. \qquad (2.59)

\]

This selection rule may be explained by angular momentum conservation (as mentioned in Section 2.2.2). This rule can be expressed in terms of vector addition, as shown in Fig. 2.8; the conservation condition is equivalent to being able to form a triangle from the three vectors representing \(j\) of the initial state, the final state, and a unit vector for the (one unit of) angular momentum carried by the photon. Hence, this selection rule is sometimes referred to as the triangle rule. The projection of \(j\) along the z-axis can change by \(\Delta m_j = 0, \pm 1\). (Appendix C gives a summary of all selection rules.)

**Further reading** Much of the material covered in this chapter can be found in the introductory quantum mechanics and atomic physics texts listed in the References. For particular topics the following are useful: Segrè (1980) gives an overview of the historical development, and Series (1988) reviews the work on hydrogen, including the important Lamb shift experiment.

**Exercises** (2.1) Angular-momentum eigenfunctions (a) Verify that all the eigenfunctions with \(l = 1\) are orthogonal to \(Y_{0,0}\).

(b) Verify that all the eigenfunctions with \(l = 1\) are orthogonal to those with \(l=2\).

(2.2) Angular-momentum eigenfunctions (a) Find the eigenfunction with orbital angular momentum quantum number \(l\) and magnetic quantum number \(m=l-1\).

(b) Verify that \(Y_{l,l-1}\) is orthogonal to \(Y_{l-1,l-1}\).

(2.3) Radial wavefunctions Verify eqn 2.23 for \(n=2, l=1\) by calculating the radial integral (for \(Z = 1\)).

(2.4) Hydrogen For a hydrogen atom the normalised wavefunction of an electron in the 1s state, assuming a point nucleus, is \[ \psi(r) = \frac{1}{( \pi a_0^3 )^{1/2}} e^{-r/a_0}, \]

where \(a_0\) is the Bohr radius. Find an approximate expression for the probability of finding the electron in a small sphere of radius \(r_b \ll a_0\) centred on the proton. What is the electronic charge density in this region? Sketch the form of the charge distribution for one cycle of oscillation.

(2.5) Hydrogen The Balmer-\(\alpha\) spectral line is observed from a (weak) discharge in a lamp that contains a mixture of hydrogen and deuterium at room temperature. Comment on the feasibility of carrying out an experiment using a Fabry–Pérot étalon to resolve (a) the isotope shift, (b) the fine structure and (c) the Lamb shift.

(2.6) Transitions Estimate the lifetime of the excited state in a two-level atom when the transition wavelength is (a) 100 nm and (b) 1000 nm. In what spectral regions do these wavelengths lie?

(2.7) Selection rules By explicit calculation of integrals over \(\theta\), for the case of \(\pi\)-polarization only, verify that p to d transitions are allowed, but not s to d.

(2.8) Spin–orbit interaction The spin–orbit interaction splits a single-electron configuration into two levels with total angular momentum quantum numbers \(j = l + 1/2\) and \(j' = l-1/2\). Show that this interaction does not shift the mean energy (centre of gravity) of all the states given by \((2j+1)E_j + (2j'+1)E_{j'}\).

(2.9) Selection rule for the magnetic quantum number Show that the angular integrals for \(\sigma\)-transitions contain the factor \[ \int_0^{2\pi} e^{i(m_{l_1} - m_{l_2} \pm 1)\phi} d\phi.

\]

Hence derive the selection rule \(\Delta m_l = \pm 1\) for this polarization. Similarly, derive the selection rule for the \(\pi\)-transitions.

(2.10) Transitions An atom in a superposition of two states has the wavefunction \[ \Psi(t) = A \psi_1(r) e^{-i E_1 t/\hbar} + B \psi_2(r) e^{-i E_2 t/\hbar}.

\]

The distribution of electronic charge is given by \[ -e |\Psi(t)|^2 = -e \left[ |A \psi_1|^2 + |B \psi_2|^2 + |2A^*B \psi_1^* \psi_2| \cos(\omega_{12} t - \phi) \right].

\]

Part of this oscillates at the (angular) frequency of the transition \(\omega_{12} = \omega_2 - \omega_1 = (E_2 - E_1)/\hbar\).

(a) A hydrogen atom is in a superposition of the 1s ground state, \(\psi_1 = R_{1,0}(r) Y_{0,0}(\theta,\phi)\), and the \(m_l=0\) state of the 2p configuration, \(\psi_2 = R_{2,1}(r) Y_{0,0}(\theta,\phi)\). Calculate the amplitude of this dipole, in units of \(e a_0\), for \(A=B=1/\sqrt{2}\).

(b) The atom in a superposition state may have an oscillating electric dipole moment \[ -e \mathbf{D}(t) = -e \langle \Psi^*(t) \mathbf{r} \Psi(t) \rangle.

\]

What are the conditions on \(\psi_1\) and \(\psi_2\) for which \(\mathbf{D}(t) \neq 0\)?

(c) Show that an atom in a superposition of the same states as in part (a) has a dipole moment of \[ -e \mathbf{D}(t) = -e |2A^*B| I_{\text{ang}} \times \int_0^\infty r R_{2,1}(r) R_{1,0}(r) r^2 dr \cos(\omega_{12} t) \hat{\mathbf{e}}_z, \]

where \(I_{\text{ang}}\) is an integral with respect to \(\theta\) and \(\phi\). Calculate the amplitude of this dipole, in units of \(e a_0\), for \(A=B=1/\sqrt{2}\).

(d) A hydrogen atom is in a superposition of the 1s ground state and the \(m_l=1\) state of the 2p configuration, \(\psi_2 = R_{2,1}(r) Y_{1,1}(\theta,\phi)\). Sketch the form of the charge distribution at various points in its cycle of oscillation.

(e) Comment on the relationship between the time dependence of the charge distributions sketched in this exercise and the motion of the electron in the classical model of the Zeeman effect (Section 1.8).

(2.11) Angular eigenfunctions We shall find the angular momentum eigenfunctions using ladder operators, by assuming that for some value of \(l\) there is a maximum value of the magnetic quantum number \(m_{\text{max}}\). For this case \(Y_{l,m_{\text{max}}} \propto \Theta(\theta) e^{i m_{\text{max}} \phi}\) and the function \(\Theta(\theta)\) can be found from \[ l + \Theta(\theta) \exp(i m_{\text{max}} \phi) = 0.

\]

(a) Show that \(\Theta(\theta)\) satisfies the equation \[ \frac{1}{\Theta(\theta)} \frac{\partial \Theta(\theta)}{\partial \theta} = \frac{m_{\text{max}} \cos\theta}{\sin\theta}.

\]

(b) Find the solution of the equation for \(\Theta(\theta)\). (Both sides have the form \(f'(\theta)/f(\theta)\) whose integral is \(\ln\{f(\theta)\}\).) By substituting this solution into eqn 2.5 to show that \(b = m_{\text{max}} (m_{\text{max}} + 1)\), or otherwise, obtain eqn 2.10.

(2.12) Parity and selection rules Show that eqn 2.42 implies that \(l_2 - l_1\) is odd. Hence, or otherwise, prove that \(I_{\text{ang}}\) is zero unless the initial and final states have opposite parity.

(2.13) Selection rules in hydrogen Hydrogen atoms are excited (by a pulse of laser light that drives a multi-photon process) to a specific configuration and the subsequent spontaneous emission is resolved using a spectrograph. Infrared and visible spectral lines are detected only at the wavelengths 4.05 µm, 1.87 µm and 0.656 µm. Explain these observations and give the values of \(n\) and \(l\) for the configurations involved in these transitions.

**Web site:** http://www.physics.ox.ac.uk/users/foot This site has answers to some of the exercises, corrections and other supplementary information.

# Helium Helium has only two electrons but this simplicity is deceptive. To treat systems with two particles requires new concepts that also apply to multi-particle systems in many branches of physics, and it is very worthwhile to study them carefully using the example of helium. There is truth in the saying that atomic physicists count ‘one, two, many’ and a detailed understanding of the two-electron system is sufficient for much of the atomic structure in this book.

## 3.1 The ground state of helium Two electrons in the Coulomb potential of a charge \(Ze\), e.g. the nucleus of an atom, obey a Schrödinger equation of the form \[ \left[ -\frac{\hbar^2}{2m_1} \nabla_1^2 - \frac{\hbar^2}{2m_2} \nabla_2^2 + \frac{e^2}{4\pi\varepsilon_0} \left( -\frac{Z}{r_1} - \frac{Z}{r_2} + \frac{1}{r_{12}} \right) \right] \psi = E \psi. \qquad (3.1)

\]

Here \(r_{12} = |\mathbf{r}_1 - \mathbf{r}_2|\) is the distance between electron 1 and electron 2 and the electrostatic repulsion of electrons is proportional to \(1/r_{12}\). Neglecting this mutual repulsion for the time being, we can write the equation as \[ (H_1 + H_2) \psi = E^{(0)} \psi, \qquad (3.2)

\]

where \[ H_1 \equiv -\frac{\hbar^2}{2m} \nabla_1^2 - \frac{Ze^2}{4\pi\varepsilon_0 r_1} \qquad (3.3)

\]

and \(H_2\) is a similar expression for electron 2. Writing the atomic wavefunction as a product of the wavefunctions for each electron, \(\psi = \psi(1)\psi(2)\), allows us to separate eqn 3.2 into two single-electron Schrödinger equations: \[ H_1 \psi(1) = E_1 \psi(1), \qquad H_2 \psi(2) = E_2 \psi(2).

\]

ψ(1) = (3.4)

and a similar equation for ψ(2) with energy E. The solutions of these one-electron equations are hydrogenic wavefunctions with energies given by the Rydberg formula. Helium has Z = 2 and in its ground state both electrons have energy E₁s = E₂s = −4hcR∞ = −54.4 eV. Thus the total energy of the atom (neglecting repulsion) is E(0) = E₁ + E₂ = −109 eV. (3.5)

Now we need to calculate the perturbation produced by the electron–electron repulsion. The system has the spatial wavefunction ψ = R₁s(r₁)R₁s(r₂) × (1/√4π)(1/√4π), (3.6) where radial wavefunctions are defined in Table 2.2 and 1/√4π is the angular part of an s-electron wavefunction. The expectation value of the repulsion is (see Section 3.3) ⟨ψ| e²/(4πε₀ r₁₂) |ψ⟩ = 34 eV. (3.7) Adding this to the (zeroth-order) estimate E(0) gives an energy of E(1s²) = −109 + 34 = −75 eV. It takes an energy of 75 eV to remove both electrons from a helium atom leaving a bare helium nucleus He²⁺ — the second ionization energy. To go from He⁺ to He⁺⁺ takes 54.4 eV, so this estimate suggests that the first ionization energy (required to remove one electron from He to create He⁺) is IE(He) ≈ 75 − 54 ≈ 21 eV. But the expectation value in eqn 3.7 is not small compared to the binding energy and therefore the perturbation has a significant effect on the wavefunctions. The necessary adjustment of the wavefunctions can be accounted for by the variational method.³ This method gives a value close to the measured ionization energy 24.6 eV. Helium has the highest first ionization energy of all elements because of its closed n=1 shell. For a plot of the ionization energies of the elements see Grant and Phillips (2001, Chapter 11, Fig. 18).⁴

According to the Pauli exclusion principle, two electrons cannot have the same set of quantum numbers. Therefore there must be some additional quantum number associated with the two 1s-electrons in the ground state of helium — this is their spin (introduced in Section 2.3.1). The observed filling-up of the atomic (sub-)shells in the periodic table implies that two spin states are associated with each set of spatial quantum numbers n, l, ml.⁵ However, electrostatic energies do not depend on spin and we can find the spatial wavefunctions separately from the problem of finding the spin eigenfunctions.

³ This is a standard quantum mechanical technique whose mathematical details are given in quantum texts. The essential principle of this technique is to find an expression for the energy in terms of a parameter — an effective atomic number in the case of helium — and then minimise the energy with respect to this parameter, i.e. study the variation in the energy as a function of the chosen parameter.

⁴ This is accessible at http://www.oup.co.uk/best.textbooks/physics/ephys/illustrations/ along with other illustrations of elementary quantum ideas.

⁵ It is often said that ‘one electron is in a spin-up state and the other is spin-down’; what this really means is defined in the discussion of spin for the excited states of helium.

## 3.2 Excited states of helium

To find the energy of the excited states we use the same procedure as for the ground state — at first we neglect the mutual repulsion term and separate eqn 3.1 into two one-electron equations that have solutions⁶: u₁s(1) = R₁s(r₁) × (1/√4π), uₙₗ(2) = Rₙₗ(r₂) Yₗ,ₘ(θ₂, φ₂)

for the configuration 1snl. The spatial part of the atomic wavefunction is the product ψₛₚₐcₑ = u₁s(1) uₙₗ(2). (3.8)

⁶ The spatial wavefunction u contains both radial and angular parts but the energy does not depend on the magnetic quantum number, so we drop m as a subscript on u. The repulsion from a spherically-symmetric 1s wavefunction does not depend on the orientation of the other electron. To show this mathematically we could carry m through all the calculations and examine the resulting angular integrals, but this is cumbersome.

Another wavefunction has the same energy, namely ψₛₚₐcₑ = u₁s(2) uₙₗ(1). (3.9)

These two states are related by a permutation of the labels on the electrons, 1 ↔ 2; the energy cannot depend on the labeling of identical particles so there is exchange degeneracy. To consider the effect of the repulsive term on this pair of wavefunctions with the same energy (degenerate states) we need degenerate perturbation theory. There are two approaches. The look-before-you-leap approach is first to form eigenstates of the perturbation from linear combinations of the initial states.⁷ In this new basis the determination of the eigenenergies of the states is simple. It is instructive, however, simply to press ahead and go through the algebra once.⁸

We rewrite the Schrödinger equation (eqn 3.1) as (H₀ + H')ψ = Eψ, (3.10)

where H₀ = H₁ + H₂, and we consider the mutual repulsion of the electrons H' = e²/(4πε₀ r₁₂) as a perturbation. We also rewrite eqn 3.2 as H₀ ψ = E(0)ψ, (3.11)

where E(0) = E₁ + E₂ is the unperturbed energy. Subtraction of eqn 3.11 from eqn 3.10 gives the energy change produced by the perturbation, ΔE = E − E(0), as H'ψ = ΔEψ. (3.12)

A general expression for the wavefunction with energy E(0) is a linear combination of expressions 3.8 and 3.9, with arbitrary constants a and b, ψ = a u₁s(1) uₙₗ(2) + b u₁s(2) uₙₗ(1). (3.13)

Substitution into eqn 3.12, multiplication by either u₁s*(1) uₙₗ*(2) or u₁s*(2) uₙₗ*(1), and then integration over the spatial coordinates for each electron (r₁, θ₁, φ₁ and r₂, θ₂, φ₂) gives two coupled equations that we write as [ J  K ] [a]   [ΔE a]

[ K  J ] [b] = [ΔE b]. (3.14)

This is eqn 3.12 in matrix form. The direct integral is J = ⟨u₁s(1) uₙₗ(2) | e²/(4πε₀ r₁₂) | u₁s(1) uₙₗ(2)⟩ = (1/4πε₀) ∫ (ρ₁s(r₁) ρₙₗ(r₂) / r₁₂) dr³₁ dr³₂, (3.15)

where ρ₁s(1) = −e|u₁s(1)|² is the charge density distribution for electron 1, and similarly for ρₙₗ(2). This direct integral represents the Coulomb repulsion of these charge clouds (Fig. 3.1). The exchange integral is K = ⟨u₁s(1) uₙₗ(2) | e²/(4πε₀ r₁₂) | u₁s(2) uₙₗ(1)⟩. (3.16)

Unlike the direct integral, this does not have a simple classical interpretation in terms of charge (or probability) distributions — the exchange integral depends on interference of the amplitudes. The spherical symmetry of the 1s wavefunction makes the integrals straightforward to evaluate (Exercises 3.6 and 3.7).

The eigenvalues ΔE in eqn 3.14 are found from | J − ΔE   K       | |  K       J − ΔE  | = 0. (3.17)

The roots of this determinantal equation are ΔE = J ± K. The direct integral shifts both levels together but the exchange integral leads to an energy splitting of 2K (see Fig. 3.2). Substitution back into eqn 3.14 gives the two eigenvectors in which b = a and b = −a. These correspond to symmetric (S) and antisymmetric (A) wavefunctions: ψₛₚₐcₑ(S) = (1/√2) {u₁s(1) uₙₗ(2) + u₁s(2) uₙₗ(1)}, ψₐₛₚₐcₑ(A) = (1/√2) {u₁s(1) uₙₗ(2) − u₁s(2) uₙₗ(1)}.

The wavefunction ψA has an eigenenergy of E(0) + J − K, and this is lower than the energy E(0) + J + K for ψS. (For the 1snl configurations in helium K is positive.)⁹ This is often interpreted as the electrons ‘avoiding’ each other, i.e. ψₐₛₚₐcₑ = 0 for r₁ = r₂, and for this wavefunction the probability of finding electron 1 close to electron 2 is small (see Exercise 3.3). This anticorrelation of the two electrons makes the expectation of the Coulomb repulsion between the electrons smaller than for ψₛₚₐcₑ.

⁷ This is guided by looking for eigenstates of symmetry operators that commute with the Hamiltonian for the interaction, as in Section 4.5.

⁸ In the light of this experience one can take the shortcut in future.

⁹ It is easy to check which wavefunction corresponds to which eigenvalue by substitution into the original equation.

The occurrence of symmetric and antisymmetric wavefunctions has a classical analogue illustrated in Fig. 3.3. A system of two oscillators, with the same resonance frequency, that interact (e.g. they are joined together by a spring) has antisymmetric and symmetric normal modes as illustrated in Fig. 3.3(b) and (c). These modes and their frequencies are found in Appendix A as an example of the application of degenerate perturbation theory in Newtonian mechanics.¹⁰ The exchange integral decreases as n and l increase because of the reduced overlap between the wavefunctions of the excited electron and the 1s-electron. These trends are an obvious consequence of the form of the wavefunctions: the excited electron’s average orbit radius increases with energy and hence with n; the variation with l arises because the effective potential from the angular momentum (‘centrifugal’ barrier) leads to the wavefunction of the excited electron being small at small r. However, in the treatment as described above, the direct integral does not tend to zero as n and l increase, as shown by the following physical argument.

¹⁰ Another example is the classical treatment of the normal Zeeman effect.

Fig. 3.1 The direct integral in a 1sns configuration of helium corresponds to the Coulomb repulsion between two spherically-symmetric charge clouds made up of shells of charge like those shown.

Fig. 3.2 The effect of the direct and exchange integrals on the energy of a 1sns triplet term is shown. The triplet terms have an energy separation of twice the exchange integral (2K).

Fig. 3.3 An illustration of degenerate perturbation in a classical system. (a) Two harmonic oscillators with the same oscillation frequency ω₀ — each spring has a mass on one end and its other end is attached to a rigid support. An interaction, represented here by another spring that connects the masses, couples the motions of the two masses. The normal modes of the system are (b) an in-phase oscillation at ω₀, in which the spring between the masses does not change length, and (c) an out-of-phase oscillation at a higher frequency. Appendix A gives the equations for this system of two masses and three springs, and also for the equivalent system of three masses joined by two springs that models a triatomic molecule, e.g. carbon dioxide.

The excited electron ‘sees’ the nuclear charge of +2e surrounded by the 1s electronic charge distribution, i.e. in the region far from the nucleus where the nl-electron’s wavefunction has a significant value, it experiences a Coulomb potential of charge +1e. Thus the excited electron has an energy similar to that of an electron in the hydrogen atom, as shown in Fig. 3.4. But we have started with the assumption that both the 1s- and nl-electrons have an energy given by the Rydberg formula for Z = 2. The direct integral J equals the difference between these energies.11 This work was an early triumph for wave mechanics since previously it had not been possible to calculate the structure of helium.12

In this section we found the wavefunctions and energy levels in helium by direct calculation but looking back we can see how to anticipate the answer by making use of symmetry arguments. The Hamiltonian for the electrostatic repulsion, proportional to 1/r12 ≡ 1/|r1 − r2|, commutes with the operator that interchanges the particle labels 1 and 2, i.e. the swap operation 1 ↔ 2. (Although we shall not give this operator a symbol it is obvious that it leaves the value of 1/r12 unchanged.) Commuting operators have simultaneous eigenfunctions. This prompts us to construct the symmetrised wavefunctions ψS_space and ψA_space.13 In this basis of eigenstates it is simple to calculate the effect of the electrostatic repulsion.

11 This can also be seen from eqn 3.15. The integration over r1, θ1 and φ1 leads to a repulsive Coulomb potential ∼e/4πε0r2 that cancels part of the attractive potential of the nucleus, when r2 is greater than the values of r1 where ψ1s is appreciable.

12 For hydrogen, the solution of Schrödinger’s equation reproduced the energy levels calculated by the Bohr–Sommerfeld theory. However, wave mechanics does give more information about hydrogen than the old quantum theory, e.g. it allows a detailed calculation of transition rates.

## 3.2 Excited states of helium

Fig. 3.4 The energy levels of the helium atom with those of hydrogen for comparison. The 1s² ground configuration is tightly bound. For the excited configurations of helium the 1s-electron screens the outer electron from the nuclear charge so that the 1snl configurations in helium have similar energy to the shell with principal quantum number n in hydrogen. The hydrogenic levels are indicated on the right. The interval between the ¹L and ³L terms (equal to twice the exchange integral) is clear for the 1s2s, 1s2p, 1s3s, 1s3p and 1s4s configurations but it is smaller for higher n and l.

13 For two electrons, swapping the particle labels twice brings us back to where we started, so ψ(1,2) = ±ψ(2,1). Therefore the two possible eigenvalues are 1 for ψS_space and −1 for ψA_space.

3.2.1 Spin eigenstates

The electrostatic repulsion between the two electrons leads to the wavefunctions ψS_space and ψA_space in the excited states of the helium atom. The ground state is a special case where both electrons have the same spatial wavefunction, so only a symmetric solution exists. We did not consider spin since electrostatic interactions depend on the charge of the particles, not their spin. Neither H nor H(cid:1) contains any reference to the spin of the electrons. Spin does, however, have a profound effect on atomic wavefunctions. This arises from the deep connection between spin and the symmetry of the wavefunction of indistinguishable particles.14 Note that here we are considering the total wavefunction in the systems that includes both the spatial part (found in the previous section) and the spin. Fermions have wavefunctions that are antisymmetric with respect to particle-label interchange, and bosons have symmetric ones. As a consequence of this symmetry property, fermions and bosons fill up the levels of a system in different ways, i.e. they obey different quantum statistics.

14 Indistinguishable means that the particles are identical and have the freedom to exchange positions, e.g. atoms in a gas which obey Fermi–Dirac or Bose–Einstein statistics depending on their spin. In contrast, atoms in a solid can be treated as distinguishable, even if they are identical, because they have fixed positions—we could label the atoms 1, 2, etc. and still know which is which at some later time.

Electrons are fermions so atoms have total wavefunctions that are antisymmetric with respect to permutation of the electron labels. This requires ψS_space to associate with an antisymmetric spin function ψA_spin, and the other way round:

ψ = ψS_space ψA_spin or ψA_space ψS_spin . (3.18)

These antisymmetrised wavefunctions that we have constructed fulfil the requirement of having particular symmetry with respect to the interchange of indistinguishable particles. Now we shall find the spin eigenfunctions explicitly. We use the shorthand notation where ↑ and ↓ represent ms = 1/2 and −1/2, respectively. Two electrons have four possible combinations: the three symmetric functions,

ψS_spin = |↑↑⟩ = √1/2 {|↑↓⟩ + |↓↑⟩} (3.19)

= |↓↓⟩,

corresponding to S = 1 and MS = +1, 0, −1; and an antisymmetric function

ψA_spin = √1/2 {|↑↓⟩ − |↓↑⟩}, (3.20)

corresponding to S = 0 (with MS = 0).15 Spectroscopists label the eigenstates of the electrostatic interactions with the symbol 2S+1L, where S is the total spin and L is the total orbital angular momentum quantum number. The 1snl configurations in helium have L = l, so the allowed terms are ¹L and ³L, e.g. the 1s2s configuration in helium gives rise to the terms ¹S and ³S, where S represents L=0.16

15 These statements about the result of adding two s=1/2 angular momenta can be proved by formal angular momentum theory. Simplified treatments describe S = 0 as having one electron with ‘spin-up’ and the other with ‘spin-down’; but both MS = 0 states are linear combinations of the states |ms1=+1/2, ms2=−1/2⟩ and |ms1=−1/2, ms2=+1/2⟩.

16 The letter ‘S’ appears over-used in this established notation but no ambiguity arises in practice. The symbol S for the total spin is italic because this is a variable, whereas the symbols S for L=0 and s for l=0 are not italic.

In summary, we have calculated the structure of helium in two distinct stages.

(1) Energies Degenerate perturbation theory gives the space wavefunctions ψS_space and ψA_space with energies split by twice the exchange integral. In helium the degeneracy arises because the two electrons are identical particles so there is exchange degeneracy, but the treatment is similar for systems where a degeneracy arises by accident.

(2) Spin We determined the spin associated with each energy level by constructing symmetrised wavefunctions. The product of the spatial functions and the spin eigenstates gives the total atomic wavefunction that must be antisymmetric with respect to particle-label interchange.

Exchange degeneracy, exchange integrals, degenerate perturbation theory and symmetrised wavefunctions all occur in helium and their interrelationship is not straightforward so that misconceptions abound. A common misinterpretation is to infer that because levels with different total spin, S = 0 and 1, have different energies then there is a spin-dependent interaction—this is not correct, but sometimes in condensed matter physics it is useful to pretend that it is! (See Blundell 2001.) The interactions that determine the gross structure of helium are entirely electrostatic and depend only on the charge and position of the particles. Also, degenerate perturbation theory is sometimes regarded as a mysterious quantum phenomenon. Appendix A gives further discussion and shows that symmetric and antisymmetric normal modes occur when two classical systems, with similar energy, interact, e.g. two coupled oscillators.

3.2.2 Transitions in helium

To determine which transitions are allowed between the energy levels of helium we need a selection rule for spin: the total spin quantum number does not change in electric dipole transitions. In the matrix element ⟨ψ_f|r|ψ_i⟩ the operator r does not act on spin; therefore, if the ψ_final and ψ_initial do not have the same value of S, then their spin functions are orthogonal and the matrix element equals zero.17 This selection rule gives the transitions shown in Fig. 3.5.

17 This anticipates a more general discussion of this and other selection rules for the LS-coupling scheme in a later chapter.

Fig. 3.5 The allowed transitions between the terms of helium are governed by the selection rule ΔS = 0 in addition to the rule Δl = ±1 found previously. Since there are no transitions between singlets and triplets it is convenient to draw them as two separate systems. Notice that in the radiative decay of helium atoms excited to high-lying levels there are bottlenecks in the metastable 1s2s¹S and 1s2s³S terms.

## 3.3 Evaluation of the integrals in helium

In this section we shall calculate the direct and exchange integrals to make quantitative predictions for some of the energy levels in the helium atom, based on the theory described in the previous sections. This provides an example of the use of atomic wavefunctions to carry out a calculation where there are no corresponding classical orbits and gives an indication of the complexities that arise in systems with more than one electron. The evaluation of the integrals requires care and some further details are given in Appendix B. The important point to be learnt from this section, however, is not the mathematical techniques but rather to see that the integrals arise from the Coulomb interaction between electrons treated by straightforward quantum mechanics.

3.3.1 Ground state

To calculate the energy of the 1s² configuration we need to find the expectation value of e²/4πε0r12 in eqn 3.1—this calculation is the same as the evaluation of the mutual repulsion between two charge distributions in classical electrostatics, as in eqn 3.15 with ρ1s(r1) and ρnl(r2) = ρ1s(r2). The integral can be considered in di...

Different ways. We could calculate the energy of the charge distribution of electron 1 in the potential created by electron 2, or the other way around. This section does neither; it uses a method that treats each electron symmetrically (as in Appendix B), but of course each approach gives the same numerical result. Electron 1 produces an electrostatic potential at radial distance r given by V₁₂(r₂) = (1 / (4πε₀ r₂²)) ∫₀ʳ² ρ(r₁) d³r₁. (3.21)

The spherical symmetry of s-electrons means that the charge in the region r < r₂ acts like a point charge at the origin, so that V₁₂(r₂) = Q(r₂) / (4πε₀ r₂²), where Q(r₂) is the charge within a radius of r₂ from the origin, which is given by¹⁸ Q(r₂) = ∫₀ʳ² ρ(r₁) 4πr₁² dr₁. (3.22)

Here Q(∞) = −e.

The electrostatic energy that arises from the repulsion equals E = ∫ V₁₂(r₂) ρ(r₂) 4πr₂² dr₂. (3.23)

For the 1s² configuration there is an exactly equal contribution to the energy from V₂₁(r₁), the (partial) potential at r₁ produced by electron 2. Thus the total energy of the repulsion between the electrons is twice that in eqn 3.23.¹⁹ Using the radial wavefunction for a 1s-electron, we find J₁ₛ² = 2 × (e²/(4πε₀)) ∫₀^∞ ∫₀^∞ r₁² 1/r₁₂ r₂² 1/2 dr₁ dr₂ = (e²/(4πε₀)) (5/8) (4Z/a₀)³ ∫₀^∞ e^{-(Z/a₀)r₁} r₁² dr₁ ∫₀^∞ e^{-(Z/a₀)r₂} r₂² dr₂ = (e²/(4πε₀)) (5/8) (4Z/a₀)³ (2! / (Z/a₀)³)² = (5/4) (e²/(4πε₀)) (a₀/Z) = (13.6 eV) × (5Z/4). (3.24)

For helium this gives J_{1s²}^{Z=2} = 34 eV.

As is usual in calculations of the interaction between electric charge distributions, one must be careful to avoid double counting. This method of calculation avoids this pitfall, as shown by the general argument in Appendix B. An alternative method is used in Woodgate (1980), Problem 5.5.

3.3.2 Excited states: the direct integral A 1snl configuration of helium has an energy close to that of an nl-electron in hydrogen, e.g. in the 1s2p configuration the 2p-electron has a similar binding energy to the n = 2 shell of hydrogen. The obvious explanation, in Bohr’s model, is that the 2p-electron lies outside the 1s-orbit so that the inner electron screens the outer one from the full nuclear charge. Applying an analogous argument to the quantum treatment of helium leads to the Hamiltonian H = H₀ₐ + Hₐ′, where²⁰ H₀ₐ = − (ħ²/2m) (∇₁² + ∇₂²) − e²/(4πε₀ r₁) + e²/(4πε₀ r₂), (3.25)

and Hₐ′ = (e²/(4πε₀)) (1/r₁₂ − 1/r₂). (3.26)

The effect of the repulsion proportional to 1/r₁₂ can be considered in terms of potentials like that in eqn 3.21 (and Appendix B). The potential at the position of the outer electron r₂ arising from the charge distribution of electron 1 accounts for a large portion of the total repulsion: V₁₂(r₂) ≈ e²/(4πε₀ r₂) in the region where ρₙₗ(r₂) has an appreciable value. Hence it makes sense to include e²/(4πε₀ r₂) in the zeroth-order Hamiltonian H₀ₐ and treat the (small) part left over as a perturbation Hₐ′.

In the expression for H₀ₐ, electron 2 experiences the Coulomb attraction of a charge +1e. In Hₐ′ the subtraction of e²/(4πε₀ r₂) from the mutual repulsion means that the perturbation tends to zero at a large distance from the nucleus (which is intuitively reasonable). This decomposition differs from that in Section 3.1. The different treatment of the two electrons makes the perturbation theory a little tricky, but Heisenberg did the calculation as described in Bethe and Salpeter (1957) or Bethe and Salpeter (1977); he found the direct integral J₁ₛₙₗ = (e²/(4πε₀)) ∫∫ |u₁ₛ(1)|² |uₙₗₘ(2)|² (1/r₁₂) d³r₁ d³r₂. (3.27)

This must be evaluated with the appropriate wavefunctions, i.e. u_{nₗₘ}^{Z=1} rather than u_{nₗ}^{Z}, and u_{1s}^{Z=2} as before.²¹ For the excited electron uₙₗₘ = Rₙₗ(r)Yₗₘ(θ,φ), where Rₙₗ(r) is the radial function for Z = 1. We write the direct integral as J₁ₛₙₗ = (e²/(4πε₀)) ∫₀^∞ ∫₀^∞ J(r₁, r₂) R₁ₛ²(r₁) Rₙₗ²(r₂) r₁² dr₁ r₂² dr₂, (3.28)

where the angular parts are contained in the function²² J(r₁, r₂) = (1/(4πr₁₂)) ∫₀^{2π} ∫₀^π |Yₗₘ(θ₁,φ₁)|² sinθ₁ dθ₁ dφ₁ ∫₀^{2π} ∫₀^π sinθ₂ dθ₂ dφ₂. (3.29)

We have not derived this integral rigorously but it has an intuitively reasonable form.

The calculation of this integral requires the expansion of 1/r₁₂ in terms of spherical harmonics:²³ 1/r₁₂ = Σ_{k=0}^∞ Σ_{q=-k}^k (4π/(2k+1)) (r_<^k / r_>^{k+1}) Yₖ,ᵧ*(θ₁,φ₁) Yₖ,ᵧ(θ₂,φ₂) (3.30)

for r₁ > r₂ (and r₁ ↔ r₂ when r₂ > r₁). Only the term for k = 0 survives in the integration over angles in eqn 3.29 to give²⁴ J(r₁, r₂) = (1/r₂) for r₁ < r₂, J(r₁, r₂) = (1/r₁) for r₁ > r₂.

Here Yₖ,ᵧ(θ,φ) = (−1)ᵧ Yₖ,₋ᵧ(θ,φ). When k ≠ 0 the integral of the function Yₖ,ᵧ(θ₁,φ₁) over θ₁ and φ₁ equals zero.

When r₁ < r₂ the original screening argument applies and eqn 3.25 gives a good description. When r₁ > r₂ the appropriate potential is proportional to −2/r₁ − 1/r₂ and J(r₁, r₂) accounts for the difference between this and −2/r₁ − 1/r₂ used in H₀ₐ. Thus we find J₁ₛₙₗ = (e²/(4πε₀)) ∫₀^∞ ∫₀^∞ R₁ₛ²(r₁) r₁² dr₁ ∫_{r₁}^∞ Rₙₗ²(r₂) r₂ dr₂ + (e²/(4πε₀)) ∫₀^∞ Rₙₗ²(r₂) r₂² dr₂ ∫₀^{r₂} R₁ₛ²(r₁) r₁ dr₁. (3.31)

Evaluation of this integral for the 1s2p configuration (in Exercise 3.6) gives J₁ₛ₂ₚ = −2.8×10⁻² eV—three orders of magnitude smaller than J_{1s²}^{Z=2} in eqn 3.7 (evaluated from eqn 3.24). The unperturbed wavefunction for Z = 1 has energy equal to that of the corresponding level in hydrogen and the small negative direct integral accounts for the incompleteness of the screening of the nl-electron by the inner electron.

3.3.3 Excited states: the exchange integral The exchange integral has the same form as eqn 3.16 but with u_{nₗₘ}^{Z=1} rather than u_{nₗₘ}^{Z=2} (and u_{1s}^{Z=2} as before). Within the spatial wavefunction uₙₗₘ = Rₙₗ(r)Yₗₘ(θ,φ) only the radial part depends on Z. We write the exchange integral as (cf. eqn 3.28)

K₁ₛₙₗ = (e²/(4πε₀)) ∫∫ K(r₁, r₂) R₁ₛ(r₁) Rₙₗ(r₁) R₁ₛ(r₂) Rₙₗ(r₂) r₁² dr₁ r₂² dr₂. (3.32)

The function K(r₁, r₂) containing the angular integrals is (cf. eqn 3.29)

K(r₁, r₂) = (1/(4πr₁₂)) ∫ Yₗₘ*(θ₁,φ₁) Yₗₘ(θ₂,φ₂) sinθ₁ dθ₁ dφ₁ sinθ₂ dθ₂ dφ₂. (3.33)

For the 1snp configuration only the second term of the expansion in eqn 3.30, with k = 1, survives in the integration because of the orthogonality of the spherical harmonic functions (see Exercise 3.7), to give K(r₁, r₂) = (r₁/(3r₂²)) for r₁ < r₂, K(r₁, r₂) = (r₂/(3r₁²)) for r₁ > r₂. (3.34)

Carrying out the integration over the radial wavefunctions in eqn 3.32 for the 1s2p configuration gives the splitting between ³P and ¹P as 2K₁ₛ₂ₚ ≈ 0.21 eV (close to the measured value of 0.25 eV).

The assumption that the excited electron lies outside the 1s wavefunction does not work so well for 1sns configurations since ψₙₛ(0) has a finite value and the above method of calculating J and K is less accurate.²⁵ The 1s2s configuration of helium has a singlet–triplet separation of E₁ₛ − E₃ₛ = 2K₁ₛ₂ₛ ≈ 0.80 eV and the direct integral is also larger than that for 1s2p—these trends are evident in Fig. 3.4 (see also Exercise 3.7).²⁶ At small r the wavefunction of an ns-electron deviates significantly from u_{nₛ}^{Z=1}; for this reason 1s2p was chosen as an example above.

The overlap of the 1s and nl wavefunctions becomes smaller as n and l increase. In Heisenberg’s treatment where screening is taken into account, the direct integral gives the deviation from the hydrogenic levels (which could be characterised by a quantum defect as in the alkalis, see Chapter 4). For electrons with l ≠ 0 the term ħ²l(l+1)/2mr² in the Schrödinger equation causes the electron’s wavefunction to lie almost entirely outside the region where u_{1s}^{Z=2} = R₁ₛ(r)/√(4π) has a significant value.

In some respects, helium is a more typical atom than hydrogen. The Schrödinger and Dirac equations can be solved exactly for the one-electron system, but not for helium or other atoms with more electrons. Thus in a careful study of helium we encounter the approximations needed to treat multi-electron atoms, and this is very important for understanding atomic structure in general. Helium also gives a good example of the influence of identical particles on the occupation of the states in quantum systems. The energy levels of the helium atom (and the existence of exchange integrals) do not depend on the fact that the two electrons are identical, as demonstrated in Exercises 3.3 and 3.4; however, this is a common point of confusion. The books recommended for further reading give clear and accurate descriptions of helium that reward careful study.

Further reading The recommended books are divided into two categories corresponding to the two main themes in this chapter: (a) a description of how to calculate the electrostatic energy in an atom with more than one electron, which introduces principles that can be used in atoms with more electrons; and (b) a discussion of the influence of identical particles on the statistics of a quantum system that is important throughout physics.

The influence of identical particles on the occupation of the quantum levels of a system with many particles, i.e. Bose–Einstein and Fermi–Dirac statistics, is discussed in statistical mechanics texts. Clear descriptions of helium may be found in the following textbooks: Cohen-Tannoudji et al. (1977), Woodgate (1980) and Mandl (1992). The calculation of the direct and exchange integrals in Section 3.3 is based on the definitive work by Bethe and Salpeter (1957), or see Bethe and Jackiw (1986).

A very instructive comparison can be made between the properties of the two electrons in helium and the nuclear spin statistics of homonuclear diatomic molecules²⁷ described in Atkins (1983, 1994).²⁸ There are diatomic molecules with nuclei that are identical bosons, identical fermions and cases of two similar but not identical particles.

²⁷ Molecules made up of two atoms with identical nuclei.

Articles, and their 28 These books also summarise the helium atom and the quantum mechanics of these molecular systems is very closely related to atomic physics. study gives a wider perspective than the study of helium alone. The nuclei of the two atoms in a hydrogen molecule are protons which are fermions (like the two electrons in helium). 29 For reasons explained in the above references, we can consider only those parts of the molecular wavefunction that describe the rotation ψ_rot and the nuclear spin states � is sufficient to say that a sodium atom in its ground state has the configuration 3s. A sodium atom with one electron in the 3s level, and no others, is an excited state of the highly-charged ion Na^+10 — this esoteric system can be produced in the laboratory but confusion with the common sodium atom is unlikely. Caesium Cs 1s^22s^22p^63s^23p^63d^104s^24p^64d^105s^25p^66s.

The alert reader will notice that the sub-shells of the heavier alkalis are not filled in the same order as the hydrogenic energy levels, e.g. electrons occupy the 4s level in potassium before the 3d level (for reasons that emerge later in this chapter). Thus, strictly speaking, we should say that the inert gases have full sub-shells, e.g. argon has the electronic configuration 1s^22s^22p^63s^23p^6 with the 3d sub-shell unoccupied.

Each alkali metal comes next to an inert gas in the periodic table and much of the chemistry of the alkalis can be explained by the simple picture of their atoms as having a single unpaired electron outside a core of closed electronic sub-shells surrounding the nucleus. The unpaired valence electron determines the chemical bonding properties; since it takes less energy to remove this outer electron than to pull an electron out of a closed sub-shell (see Table 4.1), thus the alkalis can form singly-charged positive ions and are chemically reactive.

However, we need more than this simple picture to explain the details of the spectra of the alkalis and in the following we shall consider the wavefunctions.

## 4.2 The quantum defect

The energy of an electron in the potential proportional to 1/r depends only on its principal quantum number n, e.g. in hydrogen the 3s, 3p and 3d configurations all have the same gross energy. These three levels are not degenerate in sodium, or any atom with more than one electron, and this section explains why. Figure 4.1 shows the probability density of 3s-, 3p- and 3d-electrons in sodium. The wavefunctions in sodium have a similar shape (number of nodes) to those in hydrogen. The 3d wavefunction has a single lobe outside the core so that it experiences almost the same potential as in a hydrogen atom; therefore this electron, and other d configurations in sodium with n>3, have binding energies similar to those in hydrogen, as shown in Fig. 4.2. In contrast, the wavefunctions for the s-electrons have a significant value at small r — they penetrate inside the core and 'see' more of the nuclear charge. Thus the screening of the nuclear charge by the other electrons in the atom is less effective for ns configurations than for nd, and s-electrons have lower energy than d-electrons with the same principal quantum number. (The np-electrons lie between these two.) The following modified form of Bohr’s formula works amazingly well for the energy levels of the alkalis:

E(n,l) = -hc R_∞ / (n - δ_l)^2   (4.1)

A quantity δ_l, called the quantum defect, is subtracted from the principal quantum number to give an effective principal quantum number n* = n - δ_l. The values of the quantum defects for each l can be estimated by inspecting the energy levels shown in Fig. 4.2. The d-electrons have a very small quantum defect, δ_d ≈ 0, since their energies are nearly hydrogenic. We can see that the 3p configuration in sodium has comparable energy to the n=2 shell in hydrogen, and similarly for 4p and n=3, etc.; thus δ_p ∼ 1. It is also clear that the quantum defect for s-electrons is greater than that for p-electrons. A more detailed analysis shows that all the energy levels of sodium can be parametrised by the above formula and only three quantum defects: δ_s = 1.35, δ_p = 0.86, δ_d = 0.01, δ_l ≈ 0.00 for l >2.

There is a small variation with n (see Exercise 4.3). Having examined the variation in the quantum defects with orbital angular momentum quantum number for a given element, now let us compare the quantum defects in different alkalis. The data in Table 4.1 show that the alkalis have similar ionization energies despite the variation in atomic number. Thus the effective principal quantum numbers n* = (13.6 eV / IE)^(1/2) (from eqn 4.1) are remarkably similar for all the ground configurations of the alkalis, as shown in Table 4.2.

In potassium the lowering of the energy for the s-electrons leads to the 4s sub-shell filling before 3d. By caesium (spelt cesium in the US) the 6s configuration has lower energy than 4f (δ_f ≈ 0 for Cs). The exercises give other examples, and quantum defects are tabulated in Kuhn (1969) and Woodgate (1980), amongst others.

## 4.3 The central-field approximation

The previous section showed that the modification of Bohr’s formula by the quantum defects gives reasonably accurate values for the energies of the levels in alkalis. We described an alkali metal atom as a single electron orbiting around a core with a net charge of +1e, i.e. the nucleus surrounded by N -1 electrons. This is a top-down approach where we consider just the energy required to remove the valence electron from the rest of the atom; this binding energy is equivalent to the ionization energy of the atom. In this section we start from the bottom up and consider the energy of all the electrons. The Hamiltonian for N electrons in the Coulomb potential of a charge +Ze is

H = -∑_i [∇_i²/(2m) - Ze²/(4πε₀r_i)] + ∑_{j>i} e²/(4πε₀r_ij).   (4.2)

The first two terms are the kinetic energy and potential energy for each electron in the Coulomb field of a nucleus of charge Z. The term with r_ij = |r_i - r_j| in the denominator is the electrostatic repulsion between the two electrons at r_i and r_j. The sum is taken over all electrons with j > i to avoid double counting. This electrostatic repulsion is too large to be treated as a perturbation; indeed, at large distances the repulsion cancels out most of the attraction to the nucleus. To proceed further we make the physically reasonable assumption that a large part of the repulsion between the electrons can be treated as a central potential S(r). This follows because the closed sub-shells within the core have a spherical charge distribution, and therefore the interactions between the different shells and between shells and the valence electron are also spherically symmetric. In this central-field approximation the total potential energy depends only on the radial coordinate:

V_CF(r) = -Ze²/(4πε₀r) + S(r).   (4.3)

In this approximation the Hamiltonian becomes

H_CF = ∑_i [ -∇_i²/(2m) + V_CF(r_i) ].   (4.4)

For this form of potential, the Schrödinger equation...

for N electrons, Hψ = E ψ, can be separated into N one-electron equations, i.e.

atom writing the total wavefunction as a product of single-electron wavefunctions, namely atom = ψ ··· ψN, (4.5)

leads to N equations of the form − (∇²/2m + V_CF(r₁)) ψ₁ = E₁ ψ₁, (4.6)

and similar for electrons i = 2 to N. This assumes that all the electrons see the same potential, which is not as obvious as it may appear.

This symmetric wavefunction is useful to start with (cf. the treatment of helium before including the effects of exchange symmetry); however, we know that the overall wavefunction for electrons, including spin, should be antisymmetric with respect to an interchange of the particle labels. (Proper antisymmetric wavefunctions are used in the Hartree–Fock method mentioned later in this chapter.) The total energy of the system is E atom = E₁ + E₂ + ... + EN. The Schrödinger equations for each electron (eqn 4.6) can be separated into parts to give wavefunctions of the form ψ₁ = R(r₁) Y_{l₁,m₁} ψ_spin(1). Angular momentum is conserved in a central field and the angular equation gives the standard orbital angular momentum wavefunctions, as in hydrogen. In the radial equation, however, we have V_CF(r) rather than a potential proportional to 1/r and so the equation for P(r) = rR(r) is − (1/(2m) d²P/dr² + V_CF(r) + ħ²l(l+1)/(2mr²)) P(r) = E P(r). (4.7)

To solve this equation we need to know the form of V_CF(r) and compute the wavefunctions numerically. However, we can learn a lot about the behaviour of the system by thinking about the form of the solutions, without actually getting bogged down in the technicalities of solving the equations. At small distances the electrons experience the full nuclear charge so that the central electric field is E(r) → (Ze/(4πε₀ r²)) r̂. (4.8)

The alkalis The change-over from the short- to the long-range is not calculated but is drawn to be a reasonable guess, using the following criteria. The typical radius of the 1s wavefunction around the nucleus of charge +Ze = +11e is about a₀/11, and so Z_eff will start to drop at this distance. We know that Z_eff ∼ 1 at the distance at which the 3d wavefunction has appreciable probability since that eigenstate has nearly the same energy as in hydrogen. The form of the function Z_eff(r) can be found quantitatively by the Thomas–Fermi method described in Woodgate (1980).

At large distances the other N − 1 electrons screen most of the nuclear charge so that the field is equivalent to that of charge +1e: E(r) → (e/(4πε₀ r²)) r̂. (4.9)

These two limits can be incorporated in a central field of the form E_CF(r) → (Z_eff e/(4πε₀ r²)) r̂. (4.10)

The effective atomic number Z_eff(r) has limiting values of Z_eff(0) = Z and Z_eff(r) → 1 as r → ∞, as sketched in Fig. 4.3. The potential energy of an electron in the central field is obtained by integrating from infinity: V_CF(r) = e ∫_r^∞ |E_CF(r')| dr'. (4.11)

The form of this potential is shown in Fig. 4.4.

So far, in our discussion of the sodium atom in terms of the wavefunction of the valence electron in a central field we have neglected the fact that the central field itself depends on the configuration of the electrons in the atom. For a more accurate description we must take into account the effect of the outer electron on the other electrons, and hence on the central field. The energy of the whole atom is the sum of the energies of the individual electrons (in eqn 4.6), e.g. a sodium atom in the 3s configuration has energy E(1s² 2s² 2p⁶ 3s) = 2E₁s + 2E₂s + 6E₂p + E₃s = E_core + E₃s. This is the energy of the neutral atom relative to the bare nucleus (Na¹¹⁺). It is more useful to measure the binding energy relative to the singly-charged ion (Na⁺) with energy E(1s² 2s² 2p⁶) = 2E'₁s + 2E'₂s + 6E'₂p = E'_core. The dashes are significant—the ten electrons in the ion and the ten electrons in the core of the atom have slightly different binding energies because the central field is not the same in the two cases. The ionization energy is IE = E atom - E ion = (E core - E' core) + E₃s. From the point of view of the valence electron, the difference E core - E' core is attributed to core polarization, i.e. a change in the distribution of charge in the core produced by the valence electron. To calculate the energy of multi-electron atoms properly we should consider the energy of the whole system rather than focusing attention on only the valence electron. For example, neon has the ground configuration 1s² 2s² 2p⁶ and the electric field changes significantly when an electron is excited out of the 2p subshell, e.g. into the 1s² 2s² 2p⁵ 3s configuration.

The alkalis Quantum defects can be considered simply as empirical quantities that happen to give a good way of parametrising the energies of the alkalis but there is a physical reason for the form of eqn 4.1. In any potential that tends to 1/r at long range the levels of bound states bunch together as the energy increases—at the top of the well the classically allowed region gets larger and so the intervals between the eigenenergies and the stationary solutions get smaller. More quantitatively, in Exercise 1.12 it was shown, using the correspondence principle, that such a potential has energies E ∝ 1/k², with Δk = 1 between energy levels, but k is not itself necessarily an integer. For the special case of a potential proportional to 1/r for all distances, k is an integer that we call the principal quantum number n and the lowest energy level turns out to be n = 1. For a general potential in the central-field approximation we have seen that it is convenient to write k in terms of the integer n as k = n − δ, where δ is a non-integer (quantum defect). To find the actual energy levels of an alkali and hence δ (for a given value of l) requires the numerical calculation of the wavefunctions, as outlined in the following section.

## 4.4 Numerical solution of the Schrödinger equation

Before describing particular methods of solution, let us look at the general features of the wavefunction for particles in potential wells. The radial equation for P(r) has the form d²P/dr² = − (2m/ħ²) {E − V(r)} P, (4.12)

where the potential V(r) includes the angular momentum term in eqn 4.7. Classically, the particle is confined to the region where E − V(r) > 0 since the kinetic energy must be positive. The positions where E = V(r) are the classical turning points where the particle instantaneously comes to rest, cf. at the ends of the swing of a pendulum. The quantum wavefunctions are oscillatory in the classically allowed region, with the curvature and number of nodes both increasing as E − V(r) increases, as shown in Fig. 4.6. The wavefunctions penetrate some way into the classically forbidden region where E − V(r) < 0; but in this region the solutions decay exponentially and the probability falls off rapidly.

How can we find P(r) in eqn 4.12 without knowing the potential V(r)? The answer is firstly to find the wavefunctions for a potential V_CF(r) that is ‘a reasonable guess’, consistent with eqn 4.11 and the limits on the central electric field in the previous equations. Then, secondly, we Numerical solution of the Schrödinger equation Fig. 4.6 The potential in the central-field approximation including the term that is proportional to l(l + 1)/r² is drawn here for l = 2 and the same approximate electrostatic V_CF(r) as shown in Fig. 4.4. The function P(r) = rR(r) was drawn for n = 6 and l = 2 using the method described in Exercise 4.10.

make the assumed potential correspond closely to the real potential, as described in the next section. Equation 4.12 is a second-order differential equation and we can numerically calculate P(r), the value of the function at r, from two nearby values, e.g. u(r−δr) and u(r−2δr). Thus, working from near r = 0, the method gives the numerical value of the function at all points going out as far as is necessary. The region of the calculation needs to extend beyond the classical turning point(s) by an amount that depends on the energy of the wavefunction being calculated.

General features are clearly seen in the plots produced in Exercise 4.10. Actually, that exercise describes a method of finding the radial wavefunction R(r) rather than P(r) = rR(r) but similar principles apply. If you carry out the exercise you will find that the behaviour at large r depends very sensitively on the energy E—the wavefunction diverges if E is not an eigenenergy of the potential—this gives a way of searching for those eigenenergies. If the wavefunction diverges upwards for E' and downwards for E'' then we know that an eigenenergy of the system Ek lies between these two values, E' < Ek < E''. Testing further values between these upper and lower bounds narrows the range and gives a more precise value of Ek (as in the Newton–Raphson method for finding roots). This so-called 'shooting' method is the least sophisticated method of computing wavefunctions and energies, but it is adequate for illustrating the principles of such calculations. Results are not given here since they can readily be calculated—the reader is strongly encouraged to implement the numerical method of solution, using a spreadsheet program, as described in Exercise 4.10. This shows how to find the wavefunctions for an electron in an arbitrary potential and verifies that the energy levels obey a quantum defect formula such as eqn 4.1 in any potential that is proportional to 1/r at long range (see Fig. 4.7).

Fig. 4.7 Simple modifications of the potential energy that could be used (a) for the numerical solution of the Schrödinger equation described in Exercise 4.10. For all these potentials V(r) = −e²/4πε₀r for r > r_core. (a) Inside the radial distance r_core the potential energy is V(r) = −Ze²/4πε₀r + V_offset, drawn here for Z = 3 and an offset chosen so that V(r) is continuous at r = r_core. This corresponds to the situation where the charge of the core is an infinitely thin shell. The deep potential in the inner region means that the wavefunction has a high curvature, so small steps must be used in the numerical calculation (in this region). The hypothetical potentials in (b) and (c) are useful for testing the numerical method and for showing why the eigenenergies of any potential proportional to 1/r at long range obey a quantum defect formula (like eqn 4.1). The form of the solution depends sensitively on the energy in the outer region r > r_core, but in the inner region where |E| << |V(r)| it does not, e.g. the number of nodes ('wiggles') in this region changes slowly with energy E. Thus, broadly speaking, the problem reduces to finding the wavefunction in the outer region that matches boundary conditions, at r = r_core, that are almost independent of the energy—the potential energy curve shown in (b) is an extreme example that gives useful insight into the behaviour of the wavefunction for more realistic central fields.

4.4.1 Self-consistent solutions The numerical method described above, or a more sophisticated one, can be used to find the wavefunctions and energies for a given potential in the central-field approximation. Now we shall think about how to determine V_CF itself. The potential of the central field in eqn 4.2 includes the electrostatic repulsion of the electrons. To calculate this mutual repulsion we need to know where the electrons are, i.e. their wavefunctions, but to find the wavefunctions we need to know the potential. This argument is circular. However, going round and round this loop can be useful in the following sense. As stated above, the method starts by making a reasonable estimate of V_CF and then computing the electronic wavefunctions for this potential. These wavefunctions are then used to calculate a new average potential (using the central-field approximation) that is more realistic than the initial guess. This improved potential is then used to calculate more accurate wavefunctions, and so on. On successive iterations, the changes in the potential and wavefunctions should get smaller and converge to a self-consistent solution, i.e. where the wavefunctions give a certain V_CF(r), and solving the radial equation for that central potential gives back the same wavefunctions (within the required precision). This self-consistent method was devised by Hartree. However, the wavefunctions of multi-electron atoms are not simply products of individual wavefunctions as in eqn 4.5. In our treatment of the excited configurations of helium we found that the two-electron wavefunctions had to be antisymmetric with respect to the permutation of the electron labels. This symmetry requirement for identical fermions was met by constructing symmetrised wavefunctions that were linear combinations of the simple product states (i.e. the spatial part of these functions is ψ_space^A and ψ_space^S). A convenient way to extend this symmetrisation to N particles is to write the wavefunction as a Slater determinant:

Ψ = 1/√N! | ψa(1) ψa(2) ... ψa(N) | | ψb(1) ψb(2) ... ψb(N) | | ψc(1) ψc(2) ... ψc(N) | |      ...                | | ψx(1) ψx(2) ... ψx(N) |

Here a, b, c, ..., x are the possible sets of quantum numbers of the individual electrons, and 1, 2, ..., N are the electron labels. The change of sign of a determinant on the interchange of two columns makes the wavefunction antisymmetric. The Hartree–Fock method uses such symmetrised wavefunctions for self-consistent calculations and nowadays this is the standard way of computing wavefunctions, as described in Bransden and Joachain (2003). In practice, numerical methods need to be adapted to the particular problem being considered, e.g. numerical values of the radial wavefunctions that give accurate energies may not give a good value for a quantity such as the expectation value 1/r³ that is very sensitive to the behaviour at short range.

## 4.5 The spin–orbit interaction: a quantum mechanical approach

The spin–orbit interaction βs·l (see eqn 2.49) splits the energy levels to give fine structure. For the single valence in an alkali we could treat this interaction in exactly the same way as for hydrogen in Chapter 2, i.e. use the vector model that treats the angular momenta as vectors obeying classical mechanics (supplemented with rules such as the restriction of the angular momentum to integer or half-integer values). However, in this chapter we shall use a quantum mechanical treatment and regard the vector model as a useful physical picture that illustrates the behaviour of the quantum mechanical operators. The previous discussion of fine structure in terms of the vector model had two steps that require further justification.

(a) The possible values of the total angular momentum obtained by the addition of the electron’s spin, s = 1/2, and its orbital angular momentum are j = l + 1/2 or l − 1/2. This is a consequence of the rules for the addition of angular momentum in quantum mechanics (vector addition but with the resultant quantised).

(b) The vectors have squared magnitudes given by j² = j(j + 1), l² = l(l + 1) and s² = 3/4, where j and l are the relevant angular momentum quantum numbers.

Step (b) arises from taking the expectation values of the quantum operators in the Hamiltonian for the spin–orbit interaction. This is not straightforward since the atomic wavefunctions R(r)|lmlsms⟩ are not eigenstates of this operator—this means that we must face the complications of degenerate perturbation theory. This situation arises frequently in atomic physics and merits a careful discussion.

We wish to determine the effect of an interaction of the form s·l on the angular eigenfunctions |lmlsms⟩. These are eigenstates of the operators l², lz, s² and sz labelled by the respective eigenvalues. There are 2(2l + 1) degenerate eigenstates for each value of l because the energy does not depend on the orientation of the atom in space, or the direction of its spin, i.e. energy is independent of ml and ms. The states |lmlsms⟩ are not eigenstates of s·l because this operator does not commute with lz and sz: [s·l, lz] ≠ 0 and [s·l, sz] ≠ 0. Quantum operators only have simultaneous eigenfunctions if they commute. Since |lmlsms⟩ is an eigenstate of lz it cannot simultaneously be an eigenstate of s·l, and similarly for sz. However, s·l does commute with l² and s²: [s·l, l²] = 0 and [s·l, s²] = 0 (which are easy to prove since sx, sy, sz, lx, ly and lz all commute with s² and l²). So l and s are good quantum numbers in fine structure. Good quantum numbers correspond to constants of motion in classical mechanics—the magnitudes of l and s are constant but the orientations of these vectors change because of their mutual interaction, as shown in Fig. 4.8. If we try to evaluate the expectation value using wavefunctions that are not eigenstates of the operator then things get complicated.

omplicated. We would find that the wave functions are mixed by the perturbation, i.e. in the matrix formulation of quantum mechanics the matrix representing the spin–orbit interaction in this basis has off-diagonal elements. The matrix could be diagonalised by following the standard procedure for finding the eigenvalues and eigenvectors, but a p-electron gives six degenerate states so the direct approach would require the diagonalisation of a 6×6 matrix. It is much better to find the eigenfunctions at the outset and work in the appropriate eigenbasis. This ‘look-before-you-leap’ approach requires some preliminary reasoning.

We define the operator for the total angular momentum as j = l + s. The operator j² commutes with the interaction, as does its component jz: [s·l, j²] = 0 and [s·l, jz] = 0. Thus j and mj are good quantum numbers. Hence suitable eigenstates for calculating the expectation value of s·l are |lsjmj⟩. Mathematically these new eigenfunctions can be expressed as combinations of the old basis set:

|lsjmj⟩ = Σ_mlsms C(lsjmj; ml,ms)|lmlsms⟩.

Each eigenfunction labelled by l, s, j and mj is a linear combination of the eigenfunctions with the same values of l and s but various values of ml and ms. The coefficients C are the Clebsch–Gordan coefficients and their values for many possible combinations of angular momenta are tabulated in more advanced books. Particular values of Clebsch–Gordan coefficients are not needed for the problems in this book but it is important to know that, in principle, one set of functions can be expressed in terms of another complete set—with the same number of eigenfunctions in each basis.

Finally, we use the identity j² = l² + s² + 2s·l to express the expectation value of the spin–orbit interaction as ⟨lsjmj | s·l | lsjmj⟩ = ½ ⟨lsjmj | j² − l² − s² | lsjmj⟩ = ½ {j(j+1) − l(l+1) − s(s+1)}.

The states |lsjmj⟩ are eigenstates of the operators j², l² and s². The importance of the proper quantum treatment may not yet be apparent since all we appear to have gained over the vector model is being able to write the wave functions symbolically as |lsjmj⟩. We will, however, need the proper quantum treatment when we consider further interactions that perturb these wavefunctions.

## 4.6 Fine structure in the alkalis

The fine structure in the alkalis is well approximated by an empirical modification of eqn 2.56 called the Landé formula:

ΔE_FS ∝ (Z_eff² / (n*)³) * l(l+1) α²hcR_∞. (4.13)

In the denominator the effective principal quantum number cubed (n*)³ (defined in Section 4.2) replaces n³. The effective atomic number Z_eff, which was defined in the discussion of the central-field approximation, tends to the inner atomic number Z → Z as r → 0 (where the electron ‘sees’ most of the nuclear charge); outside the core the field corresponds to an outer atomic number Z ≈ 1 (for neutral atoms). The Landé formula can be justified by seeing how the central-field approximation modifies the calculation of the fine structure in hydrogen (Section 2.3.2). The spin–orbit interaction depends on the electric field that the electron moves through; in an alkali metal atom this field is proportional to Z_eff(r) / r³ rather than 1/r³ as in hydrogen. Thus the expectation value of the spin–orbit interaction depends on:

Z_eff(r) / r³ = -(1/r³) * (∂V_CF(r)/∂r)

rather than 1/r³ as in hydrogen (eqn 2.51). This results in fine structure for the alkalis, given by the Landé formula, that scales as Z²—this lies between the dependence on Z⁴ for hydrogenic ions (no screening) and the other extreme of no dependence on atomic number for complete screening. The effective principal quantum number n* is remarkably similar across the alkalis, as noted in Section 4.2.

As a particular numerical example of the scaling, consider the fine structure of sodium (Z = 11) and of caesium (Z = 55). The 3p configuration of sodium has a fine-structure splitting of 1700 m⁻¹, so for a Z²-dependence the fine structure of the 6p configuration of caesium should be (using n* from Table 4.2):

1.7×10³ × (55/11)² × (2.1/2.4)³ = 28.5×10³ m⁻¹.

This estimate gives only half the actual value of 55.4×10³ m⁻¹, but the prediction is much better than if we had used a Z⁴ scaling. (A logarithmic plot of the energies of the gross and fine structure against atomic number is given in Fig. 5.7. This shows that the actual trend of the fine structure lies close to the Z²-dependence predicted.)

The fine structure causes the familiar yellow line in sodium to be a doublet comprised of the two wavelengths λ = 589.0 nm and 589.6 nm. This, and other doublets in the emission spectrum of sodium, can be resolved by a standard spectrograph. In caesium the transitions between the lowest energy configurations (6s–6p) give spectral lines at λ = 852 nm and 894 nm—this ‘fine structure’ is not very fine.

4.6.1 Relative intensities of fine-structure transitions

The transitions between the fine-structure levels of the alkalis obey the same selection rules as in hydrogen since the angular momentum functions are the same in both cases. It takes a considerable amount of calculation to find absolute values of the transition rates but we can find the relative intensities of the transitions between different fine-structure levels from a simple physical argument. As an example we shall look at p to s transitions in sodium, as shown in Fig. 4.9. The ²S₁/₂ – ²P₁/₂ transition has half the intensity of the ²S₁/₂ – ²P₃/₂ transition. This 1:2 intensity ratio arises because the strength of each component is proportional to the statistical weight of the levels (2j+1). This gives 2:4 for j = 1/2 and 3/2. To explain this we first consider the situation without fine structure. For the 3p configuration the wavefunctions have the form R₃ₚ(r)|lmlsms⟩ and the decay rate of these states (to 3s) is independent of the values of ml and ms. Linear combinations of the states R(r)|lmlsms⟩ with different values of ml and ms (but the same values of n, l and s, and hence the same lifetime) make up the eigenstates of the fine structure, |lsjmj⟩. Therefore an alkali atom has the same lifetime for both values of j.

If each state has the same excitation rate, as in a gas discharge lamp for example, then all the states will have equal populations and the intensity of a given component of the line is proportional to the number of contributing mj states. Similarly, the fine structure of transitions from s to p configurations, e.g. ³P₃/₂ – ⁵S₁/₂ and ³P₁/₂ – ⁵S₁/₂, have an intensity ratio of 2:1—in this case the lower frequency component has twice the intensity of the higher component, i.e. the opposite of the p to s transition shown in Fig. 4.9 (and such information can be used to identify the lines in an observed spectrum). More generally, there is a sum rule for intensities: the sum of the intensities to, or from, a given level is proportional to its degeneracy; this can be used when both upper and lower configurations have fine structure (see Exercise 4.8).

The discussion of the fine structure has shown that spin leads to a splitting of energy levels of a given n, of which l levels have different j. These fine-structure levels are degenerate with respect to mj, but an external magnetic field removes this degeneracy. The calculation of the effect of an external magnetic field in Chapter 1 was a classical treatment that led to the normal Zeeman effect. This does not accurately describe what happens for atoms with one valence electron because the contribution of the spin magnetic moment leads to an anomalous Zeeman effect. The splitting of the fine-structure level into 2j + 1 states (or Zeeman sub-levels) in an applied field is shown in Fig. 4.10. It is straightforward to calculate the Zeeman energy for an atom with a single valence electron, as shown in quantum texts, but to avoid repetition the standard treatment is not given here; in the next chapter we shall derive a general result for the effect of a magnetic field on an atom.

general formula for the Zeeman effect on atoms with any number of valence electrons is E_Zeeman = g_j µ_B B m_j. The factor g_j arises from the projection of the contributions to the magnetic moment from valence electrons that covers the single-electron case (see Exercise 5.13).

We also look at the Zeeman effect on hyperfine structure in Chapter 6. lands onto j (see Exercise 5.13).

Further reading

This chapter has concentrated on the alkalis and mentioned the neighbouring inert gases; a more general discussion of the periodic table is given in Physical chemistry by Atkins (1994).

The self-consistent calculations of atomic wavefunctions are discussed in Hartree (1957), Slater (1960), Cowan(1981), in addition to the textbook by Bransden and Joachain (2003).

The numerical solution of the Schrödinger equation for the bound states of a central field in Exercise 4.10 is discussed in French and Taylor (1978), Eisberg and Resnick (1985) and Rioux (1991). Such numerical methods can also be applied to particles with positive energies in the potential to model scattering in quantum mechanics, as described in Greenhow (1990). The numerical method described in this book has deliberately been kept simple to allow quick implementation, but the Numerov method is more precise for this type of problem.

Exercises

(4.1) Configuration of the electrons in francium Write down the full electronic configuration of francium (atomic number Z = 87). This element comes below caesium in the periodic table.

(4.2) Finding the series limit for sodium Eight ultraviolet absorption lines in sodium have wavenumbers of 38541, 39299, 39795, 40137, 40383, 40566, 40706, 40814, in units of cm−1. Devise an extrapolation procedure to find the ionization limit of sodium with a precision justified by the data. Convert the result into electron volts. (You may find a spreadsheet program useful for manipulating the numbers.)

What is the effective principal quantum number n* of the valence electron in the ground configuration?

(4.3) Quantum defects of sodium The binding energies of the 3s, 4s, 5s and 6s configurations in sodium are 5.14 eV, 1.92 eV, 1.01 eV and 0.63 eV, respectively. Calculate the quantum defects for these configurations and comment on what you find.

Estimate the binding energy of the 8s configuration and make a comparison with the n=8 shell in hydrogen.

(4.4) Quantum defect (a) An emission line in the spectrum of an alkali has three fine-structure components corresponding to the transitions 2P 3/2 –2D 3/2, 2P 3/2 –2D 5/2 and 2P 1/2 –2D 3/2. These components have intensities a, b and c, respectively, that are in the ratio 1:9:5. Show that these satisfy the rule that the sum of the intensities of the transitions to, or from, a given level is proportional to its statistical weight (2J+1).

(4.5) Application of quantum defects to helium and helium-like ions Configuration Binding energy(cm−1)

1s2s 35250 1s2p 28206 1s3s 14266 1s3p 12430 1s3d 12214

(a) Calculate the wavelength of the 1s2p–1s3d line in helium and compare it with the Balmer-α line in hydrogen.

(b) Calculate the quantum defects for the configurations of helium in the table. Estimate the binding energies of the 1s4l configurations.

(c) The levels belonging to the 1s4f configuration of the Li+ ion all lie at an energy of 72.24 eV above the ion’s ground state. Estimate the second ionization energy of this ion. Answer: 75.64 eV.

(4.6) Quantum defects and fine structure of potassium An atomic vapour of potassium absorbs light at the wavelengths (in nm): 769.9, 766.5, 404.7, 404.4, 344.7 and 344.6. These correspond to transitions from the ground configuration 4s. Explain these observations as fully as you can and estimate the mean wavelength of the next doublet in the series, and its splitting. (Potassium has IE=4.34 eV.) 28

(4.7) The Z-scaling of fine structure Calculate the fine-structure splitting of the 3p configuration of the hydrogen-like ion Na+10 (in eV).

Explain why it is larger than the fine structure of the same configuration in the neutral sodium (0.002 eV) and hydrogen (1.3×10−5 eV).

(4.8) Relative intensities of fine-structure components Estimate the wavelength of laser radiation that excites the 5s 2S 1/2 –7s 2S 1/2 transition in rubidium by simultaneous absorption of two photons with the same frequency (IE(Rb) = 4.17 eV). (Two-photon spectroscopy is described in Section 8.4 but specific details are not required here.)

(b) Sketch an energy-level diagram of the fine-structure levels of the two terms nd 2D and n' f 2F (for n' > n). Mark the three allowed electric dipole transitions and find their relative intensities.

(4.9) Spherical symmetry of a full sub-shell The sum l over m=−l |Yl,m|2 is spherically symmetric. Show this for the specific case of l = 1 and comment on the relevance of the general expression, that is true for all values of l, to the central-field approximation.

(4.10) Numerical solution of the Schrödinger equation This exercise goes through a method of finding the wavefunctions and their energies for a potential (in the central-field approximation). This shows how numerical calculations are carried out in a simple case that can be implemented easily on a computer with readily available spreadsheet programs. 29 Of course, the properties of hydrogen-like atoms are well known and so the first stage really serves as a way of testing the numerical method (and checking that the formulae have been typed correctly). It is straightforward to extend the numerical method to deal with other cases, e.g. the potentials in the central-field approximation illustrated in Fig. 4.7. 30

(a) Derivation of the equations

Show from eqn 2.4, and other equations in Chapter 2, that

d²R/dx² + (2/x) dR/dx + (E – V(x)) R(x) = 0, (4.14)

where the position and energy have been turned into dimensionless variables: x=r/a₀ and E' is the energy in units of e²/8πε₀a₀ = 13.6 eV (equal to half the atomic unit of energy used in some of the references). 31 In these units the effective potential is

V'(x)= l(l+1)/x² – 2/x, (4.15)

where l is the orbital angular momentum quantum number.

The derivatives of a function f(x) can be approximated by

df/dx ≈ [f(x+δ/2)+f(x−δ/2)] / δ,

d²f/dx² ≈ [f(x+δ)+f(x−δ)−2f(x)] / δ²,

where δ is a small step size. 32 Show that the second derivative follows by applying the procedure used to obtain the first derivative twice. Show also that substitution into eqn 4.14 gives the following expression for the value of the function at x+δ in terms of its value at the two previous points:

R(x+δ)= 2R(x) + (V'(x)−E) R(x)δ² – (1 – δ/x) R(x−δ) (1 + δ/x). (4.16)

If we start the calculation near the origin then

R(2δ)= [2 + (V'(δ)−E) δ²] R(δ),

R(3δ)= 2R(2δ) + (V'(2δ)−E) R(2δ)δ² + R(δ),

etc. Note that in the first equation the value of R(x) at x=2δ depends only on R(δ)—it can easily be seen why by inspection of eqn 4.16 for the case of x = δ (for this value of x the coefficient of R(0) is zero). Thus the calculation starts at x=δ and works outwards from there. 33 At all other positions (x > δ) the value of the function depends on its values at the two preceding points. From these recursion relations we can calculate the function at all subsequent points.

The calculated functions will not be normalised and the starting conditions can be multiplied by an arbitrary constant without affecting the eigenenergies, as will become clear from looking at the results. In the following R(δ) = 1 is the suggested choice but any starting value works.

(b) Implementation of the numerical method using a spreadsheet program

Follow these instructions.

1. Type the given text labels into cells A1, B1, C1, D2, E2 and F2 and the three numbers into cells D1, E1 and F1 so that it has the following form:

| A    | B    | C    | D    | E    | F    | |------|------|------|------|------|------| | x    | V(x) | psi  | 0.02 | -0.25| 1    | | step | energy| ang.mom.|      |      |      |

Column A will contain the x-coordinates, the potential will be in column B and the function in column C. Cells D1, E1 and F1 contain the step size, energy and orbital angular momentum quantum number (l=1), respectively.

2. Put 0 into A2 and the formula =A2+$D$1 into A3. Copy cell A3 to the block A4:A1002. (Or start with a smaller number of steps and adjust D1 accordingly.)

3. The potential diverges at x = 0 so type inf. into B2 (or leave it blank, remembering not to refer to it). Put the formula =-2/A3 +$F$1*($F$1+1)/(A3*A3) into cell B3 (as in eqn 4.15). Copy B3 into the block B4:B1002.

4. This is the crucial stage that calculates the function. Type the number 1 into cell C3. The formula for cell C4 needs to be typed carefully as a single continuous expression even though it may span several lines on the screen: =2*C3+(($B$1-C3)*C3*$D$1^2) - (1-($D$1/A3))*C2*(1+($D$1/A3))

Copy cell C4 into the block C5:C1002.

5. (a) Plot the values of x (column A) against psi (column C). A large positive or negative energy will make the function diverge exponentially at large x.

(b) Now you need to find the correct energy that gives a bound state. Choose a trial energy in E1, e.g. −0.25. Make a copy of the worksheet and change the trial energy. Compare the graphs. The correct eigenenergy is that value which gives a solution that goes to zero at large x without diverging to +∞ or −∞. (The divergence is exponential, so even a small energy discrepancy gives a large effect.) Try the different energies again with bigger and smaller step sizes in D1. It is important to search for the eigenenergy using an appropriate range of x. The eigenenergy lies between the two values of the trial energy that give opposite divergence, i.e. upwards and downwards on the graph.

(iii) Change F1 to 0 and find a solution for l=0.

6. Produce a set of graphs labelled clearly with the trial energy that illustrate the principles of the numerical solution, for the two functions with n = 2 and two other cases. Compare the eigenenergies with the Bohr formula.

Calculate the effective principal quantum number for each of the solutions, e.g. by putting =SQRT(-1/E1) in G1 (and the label n* in G2).

(The search for eigenenergies can be automated by exploiting the spreadsheet’s ability to optimise parameters subject to constraints (e.g. using the Solver in Excel).)

28 For a discussion of how to determine the quantum defect for a series of lines by an iterative method see Softley (1994).

29 With a spreadsheet it is very easy to make changes, e.g. to find out how different potentials affect the eigenenergies and wavefunctions.

30 It is intended to put more details on the website associated with this book, see introduction for the address.

31 The electron mass m_e=1 in these units. Or, more strictly, its reduced mass.

32 This abbreviation should not be confused with the quantum defect.

33 This example is an exception to the general requirement that the solution of a second-order differential equation, such as that for a harmonic oscillator, requires a knowledge of the function at two points to define both the value of the function and its derivative.

g. the ‘Goal Seek’ command, or C3. (We leave C2 blank since, as explained similar). Ask the program to make the last above, the value of the function at x = 0 value of the function (in cell C1002) have does not affect the solution given by the re- the value of zero by adjusting the energy cursion relation in eqn 4.16.) Now move to (cell E1). This procedure can be recorded cell C4 and enter the following formula for as a macro that searches for the eigenener- the recursion relation: gies with a single button click.)

=( 2*C3+(B3-$E$1)*C3*$D$1*$D$1 7. Implement one, or more, of the following - (1-$D$1/A3)*C2 )/ (1+$D$1/A3). suggestions for improving the basic method described above.

Copy this into the block C5:C1002. Create an xy-plot of the wavefunction (with data (i) Find the eigenenergies for a potential points connected by smooth lines and no that tends to the Coulomb potential markers); the x series is A2:A1002 and the (−2/x in dimensionless units) at long y series is C2:C1002. Insert this graph on range, like those shown in Fig. 4.7, the sheet.

and show that the quantum defects for

## 5. Now play around with the parameters and that potential depend on l but only

observe the effect on the wavefunction for weakly on n.

a particular energy.

(ii) For the potential shown in Fig. 4.7(c)

(i) Show that the initial value of the func- compare the wavefunction in the inner tion does not affect its shape, or the and outer regions for several different eigenenergy, by putting 0.1 (or any energies. Give a qualitative explana- number) into cell C3. tion of the observed behaviour.

(ii) Change the energy, e.g. put -0.251 (iii) Calculate the function P(r) = rR(r)

into cell E1, then -0.249, and ob- by putting A3*C3 in cell D3 and copy- serve the change in behaviour at large ing this to the rest of the column.

Exercises for Chapter 4 79 Make a plot of P(r), R(r) and V(r) for sheet) you can calculate the electric at least two different values of n and dipole matrix elements (and their ra- l. Adjust the value in C3, as in stage tios), e.g. |<3p|r|2s>|^2/|<3p|r|1s>|^2 = 5(i), to scale the functions to conve- 36, as in Exercise 7.6 (not forgetting nient values for plotting on the same the ω^3 factor from eqn 7.23).

axes as the potential.

(vi) Assess the accuracy of this numerical (iv) Attempt a semi-quantitative calcula- method by calculating some eigenen- tion of the quantum defects in the ergies using different stepsizes. (More lithium atom, e.g. model V_CF(r) as in sophisticated methods of numerical in- Fig. 4.7(a) for some reasonable choice tegration provided in mathematical of r_core.34 software packages can be compared to (v) Numerically calculate the sum of the simple method, if desired, but the r^2 R^2(r) δ for all the values of the emphasis here is on the atomic physics function and divide through by its rather than the computation. Note square root to normalise the wave- that methods that calculate higher function. With normalised functions derivatives of the function cannot cope (stored in a column of the spread- with discontinuities in the potential.)

Web site: http://www.physics.ox.ac.uk/users/foot This site has answers to some of the exercises, corrections and other supplementary information.

34 This simple model corresponds to all the inner electron charge being concentrated on a spherical shell. Making the tran- sition from the inner to outer regions smoother does not make much difference to the qualitative behaviour, as you can check with the program.

5 LS The -coupling scheme In this chapter we shall look at atoms with two valence electrons, e.g. al- 5.1 Fine structure in the kaline earth metals such as Mg and Ca. The structures of these elements LS-coupling scheme 83 have many similarities with helium, and we shall also use the central- 5.2 The jj-coupling scheme 84 field approximation that was introduced for the alkalis in the previous 5.3 Intermediate coupling: chapter. We start with the Hamiltonian for N electrons in eqn 4.2 and the transition between insert the expression for the central potential V_CF(r) (eqn 4.3) to give coupling schemes 86 H = sum_i=1^N [ -1/2 ∇_i^2 + V_CF(r_i) + 1/2 sum_{j>i} e^2/4πε_0 r_ij - S(r_i) ].

## 5.4 LS-coupling rules

5.5 jj-coupling rules 92 This Hamiltonian can be written as H = H_CF + H_re, where the central-

## 5.6 Summary 93 field Hamiltonian H_CF is that defined in eqn 4.4 and

Further reading 94 H_re = sum_i=1^N sum_{j>i} e^2/4πε_0 r_ij - sum_i=1^N S(r_i) (5.1)

Exercises 94 is the residual electrostatic interaction. This represents that part of the re- pulsion not taken into account by the central field. One might think that 1 Choosing S(r) to account for all the field left over is somehow non-central. This is not necessarily true.

For configurations such as 1s2s in He, or 3s4s in Mg, both electrons have the repulsion between the spherically- spherically-symmetric distributions but a central field cannot completely symmetric core and the electrons out- account for the repulsion between them—a potential V_CF(r) does not in- side the closed shells, and also within clude the effect of the correlation of the electrons’ positions that leads the core, leaves the repulsion between to the exchange integral.1 The residual electrostatic interaction perturbs the two valence electrons, i.e. H_re ≈ e^2/4πε_0 r_12. This approximation high- the electronic configurations n1 l1 n2 l2 that are the eigenstates of the cen- lights the similarity with helium (al- tral field. These angular momentum eigenstates for the two electrons are though the expectation value is eval- products of their orbital and spin functions |l1 ml1 s1 ms1>|l2 ml2 s2 ms2> uated with different wavefunctions).

and their energy does not depend on the atom’s orientation so that all However, it is no simple task to use this approximation for accurate calculations—S(r)

the different ml states are degenerate, e.g. the configuration 3p4p has can be chosen to include most of the (2l1 + 1)(2l2 + 1) = 9 degenerate combinations of Y_{l1,m1} Y_{l2,m2}.2 Each direct integral (cf. Section 3.3.2). For of these spatial states has four spin functions associated with it, but alkali metal atoms, which we studied in we do not need to consider thirty-six degenerate states since the prob- the last chapter, the repulsion between lem separates into spatial and spin parts, as in helium. Nevertheless, electrons gives a spherically-symmetric potential, so that H_re = 0.

the direct approach would require diagonalising matrices of larger di- 2 For two p-electrons we cannot ignore mensions than the simple 2×2 matrix whose determinant was given in ml as we did in the treatment of 1sml eqn 3.17. Therefore, instead of that brute-force approach, we use the configurations in helium. Configura- tions with one, or more, s-electrons can ‘look-before-you-leap’ method that starts by finding the eigenstates of be treated in the way already described the perturbation H_re. In that representation, H_re is a diagonal matrix for helium but with the radial wave- with the eigenvalues as its diagonal elements.

functions calculated numerically.

The LS-coupling scheme 81 The interaction between the electrons, from their electrostatic repul- sion, causes their orbital angular momenta to change, i.e. in the vector model l1 and l2 change direction, but their magnitudes remain constant.

This internal interaction does not change the total orbital angular mo- mentum L = l1 + l2, so l1 and l2 move (or precess) around this vector, as illustrated in Fig. 5.1. When no external torque acts on the atom, L has a fixed orientation in space so its z-component ML is also a constant of the motion (ml1 and ml2 are not good quantum numbers). This classical picture of conservation of total angular momentum corresponds to the quantum mechanical result that the operators L^2 and L_z both commute with H_re:3 [L^2, H_re] = 0 and [L_z, H_re] = 0. (5.2) Fig. 5.1 The residual electrostatic in- teraction causes l1 and l2 to precess Since H_re does not depend on spin it must also be true that around their resultant L = l1 + l2.

[S^2, H_re] = 0 and [S_z, H_re] = 0. (5.3)

Actually, H_re also commutes with the individual spins s1 and s2 but we chose eigenfunctions of S to antisymmetrise the wave function as in helium—the spin eigenstates for two electrons are ψ_A and ψ_S for S = 0 and 1, respectively.4 The quantum numbers L, ML, S and MS 4 The Hamiltonian H commutes with have well-defined values in this Russell–Saunders or LS-coupling scheme.

the exchange (or swap) operator X_ij Thus the eigenstates of H_re are |L ML S MS>. In the LS-coupling scheme to interchange the labels i and j simultaneously eigenfunctions of both the energy levels labelled by L and S are called terms (and there is operators exist. This is obviously true for degeneracy with respect to ML and MS). We saw examples of 1L and the Hamiltonian of the helium atom in 3L terms for the 1snl configurations in helium where the LS-coupling eqn 3.1 (which looks the same if 1 ↔ 2), scheme is a very good approximation. A more complex example is an but it also holds for eqn 5.1. In general, npn′p configuration, e.g. 3p4p in silicon, that has six terms as follows: swapping particles with the same mass l1 = 1, l2 = 1 ⇒ L = 0, 1 or 2, and charge does not change the Hamil- s1 = 1/2, s2 = 1/2 ⇒ S = 0 or 1; tonian for the electrostatic interactions terms: ^{2S+1}L = 1S, 1P, 1D, 3S, 3P, 3D.

of a system.

The direct and exchange integrals that determine the energies of these terms are complicated to evaluate (see Woodgate (1980) for details)

and here we shall simply make some empirical observations based on the terms diagrams in Figs 5.2 and 5.3. The (2l1 + 1)(2l2 + 1) = 9 degenerate states of orbital angular momentum become the 1 + 3 + 5 = 9 states of ML associated with the S, P and D terms, respectively.

As in helium, linear combinations of the four degenerate spin states lead to triplet and one singlet terms but, unlike helium, triplets do not necessarily lie below singlets. Also, the 3p2 configuration has fewer terms than the 3p4p configuration for equivalent electrons, because of the Pauli exclusion principle (see Exercise 5.6).

In the special case of ground configurations of equ Equivalent electrons: the spin and orbital angular momentum of the lowest-energy term follow some empirical rules, called Hund’s rules: the lowest-energy term has the largest value of S consistent with the Pauli exclusion principle. Two electrons cannot both have the same set of quantum numbers.

The LS-coupling scheme

The terms of the 3p4p configuration in silicon all lie about 6 eV above the ground state. The residual electrostatic interaction leads to energy differences of ∼0.2 eV between the terms, and the fine-structure splitting is an order of magnitude smaller, as indicated for the 3P and 3D terms. This structure is well described by the LS-coupling scheme.

The energies of terms of the 3p2 configuration of silicon. For equivalent electrons the Pauli exclusion principle restricts the number of terms—there are only three compared to the six in the 3p4p configuration. The lowest-energy term is 3P, in accordance with Hund’s rules, and this is the ground state of silicon atoms.

Hund’s rules are so commonly misapplied that it is worth spelling out that they only apply to the lowest term of the ground configuration for cases where there is only one incomplete subshell. There are several such terms then the one with the largest L is lowest. The lowest term in the 3p2 configuration is consistent with these rules; the rule says nothing about the ordering of the other terms (or about any of the terms in the 3p4p configuration). Configurations of equivalent electrons are especially important since they occur in the ground configuration of elements in the periodic table, e.g. for the 3d6 configuration in iron, Hund’s rules give the lowest term as 5D (see Exercise 5.6). The large total spin has important consequences for magnetism (Blundell 2001).

## 5.1 Fine structure in the LS-coupling scheme

Fine structure arises from the spin–orbit interaction for each of the unpaired electrons given by the Hamiltonian H s−o = β1 s1 · l1 + β2 s2 · l2. For atoms with two valence electrons H s−o acts as a perturbation on the states |LMLSMS⟩. In the vector model, this interaction between the spin and orbital angular momentum causes L and S to change direction, so that neither Lz nor Sz remains constant; but the total electronic angular momentum J = L + S, and its z-component Jz, are both constant because no external torque acts on the atom. We shall now evaluate the effect of the perturbation H s−o on a term using the vector model. In the vector-model description of the LS-coupling scheme, the orbital angular momenta of the two electrons l1 and l2 precess around L, as shown in Fig. 5.4; the components perpendicular to this fixed direction average to zero (over time) so that only the component of these vectors along L needs to be considered, e.g. l1 → l1 ·L /|L|2 L. The time average l1 ·L in the vector model becomes the expectation value ⟨l1 ·L⟩ in quantum mechanics; also we have to use L(L+1) for the magnitude-squared of the vector. Applying the same projection procedure to the spins leads to

H s−o = β1 [S(S+1) / S·S] S·L [L(L+1) / L·L] + β2 [S(S+1) / S·S] S·L [L(L+1) / L·L] = βLS S·L. (5.4)

The derivation of this equation by the vector model that argues by analogy with classical vectors can be fully justified by reference to the theory of angular momentum. It can be shown that, in the basis |JMJ⟩ of the eigenstates of a general angular momentum operator J and its component Jz, the matrix elements of any vector operator V are proportional to those of J, i.e. ⟨JMJ |V|JMJ⟩ = c⟨JMJ |J|JMJ⟩. Figure 5.5 gives a pictorial representation of why it is only the component of V along J that is well defined. We want to apply this result to the case where V = l1 or l2 in the basis of eigenstates |LML⟩, and analogously for the spins. For ⟨LML |l1 |LML⟩ = c⟨LML |L|LML⟩ the constant c is determined by taking the dot product of both sides with L to give c = ⟨LML |l1 ·L|LML⟩ / ⟨LML |L·L|LML⟩ hence

⟨LML |l1 |LML⟩ = [⟨l1 ·L⟩ / L(L+1)] ⟨LML |L|LML⟩. (5.5)

This is an example of the projection theorem and can also be applied to l2 and to s1 and s2 in the basis of eigenstates |SMS⟩. It is clear that, for diagonal matrix elements, these quantum mechanical results give the same result of the vector model.

Equation 5.4 has the same form as the spin–orbit interaction for the single-electron case but with capital letters rather than s·l. The constant βLS that gives the spin–orbit interaction for each term is related to that for the individual electrons (see Exercise 5.2). The energy shift is

E s−o = βLS ⟨S·L⟩. (5.6)

To find this energy we need to evaluate the expectation value of the operator L·S = (J·J − L·L − S·S)/2 for each term 2S+1L. Each term has (2S+1)(2L+1) degenerate states. Any linear combination of these states is also an eigenstate with the same electrostatic energy and we can use this freedom to choose suitable eigenstates and make the calculation of the (magnetic) spin–orbit interaction straightforward. We shall use the states |LSJMJ⟩; these are linear combinations of the basis states |LMLSMS⟩ but we do not need to determine their exact form to find the eigenenergies. Evaluation of eqn 5.6 with the states |LSJMJ⟩ gives

E s−o = βLS {J(J+1) − L(L+1) − S(S+1)}. (5.7)

Thus the energy interval between adjacent J levels is

ΔE FS = EJ − EJ−1 = βLS J. (5.8)

This is called the interval rule. For example, a 3P term (L=1=S) has three J levels: 2S+1LJ = 3P0, 3P1, 3P2 (see Fig. 5.6); and the separation between J = 2 and J = 1 is twice that between J = 1 and J = 0. The existence of an interval rule in the fine structure of a two-electron system generally indicates that the LS-coupling scheme is a good approximation (see the ‘Exercises’ in this chapter); however, the converse is not true. The LS-coupling scheme gives a very accurate description of the energy levels of helium but the fine structure does not exhibit an interval rule (see Example 5.2 later in this chapter).

It is important not to confuse LS-coupling (or Russell–Saunders coupling) with the interaction between L and S given by βLS S· = 1/2 or 3/2; so there are two levels, denoted by (j₁, j₂) = (1/2,1/2) and (1/2,3/2). The residual electrostatic interaction acts as a perturbation on the jj-coupled levels; it causes the angular momenta of the electrons to be coupled to give total angular momentum J = j₁ + j₂ (as illustrated in Fig. 5.8). Since there is no external torque on the atom, M_J is also a good quantum number. For an sp configuration there are pairs of J levels for each of the two original jj-coupled levels, e.g. (j₁, j₂) = (1/2,1/2), J = 0, 1 and (1/2,3/2), J = 1, 2. This doublet structure, shown in Fig. 5.10, contrasts with the singlets and triplets in the LS-coupling scheme.

Fig. 5.8 The jj-coupling scheme. The spin–orbit interaction energy is large compared to the E_re. (Cf. Fig. 5.4 for the LS-coupling scheme.)

In summary, the conditions for LS- and jj-coupling are as follows:¹² LS-coupling scheme: E_re ≫ E_{s-o}, jj-coupling scheme: E_{s-o} ≫ E_re.

¹²In both of these cases we assume an isolated configuration, i.e. that the energy separation of the different configurations in the central field is greater than the perturbation produced by E_re and E_{s-o}.

## 5.3 Intermediate coupling: the transition between coupling schemes

In this section we shall look at examples of angular momentum coupling schemes in two-electron systems. Figure 5.9 shows energy-level diagrams of Mg and Hg and the following example looks at the structure of these atoms.

### Example 5.1 **3s3p, Mg** | **6s6p, Hg** --- | ---

## 2.1850 | 3.76

## 2.1870 | 3.94

## 2.1911 | 4.40

## 3.5051 | 5.40

The table gives the energy levels, in units of 10⁶ m⁻¹ measured from the ground state, for the 3s3p configuration in magnesium (Z = 12) and 6s6p in mercury (Z = 80). We shall use these data to identify the levels and assign further quantum numbers.

For an sp configuration we expect ¹P and ³P terms. In the case of magnesium we see that the spacings between the three lowest levels are 2000 m⁻¹ and 4100 m⁻¹; these are close to the 1 to 2 ratio expected from the interval rule for the levels with J = 0, 1 and 2 that arise from the triplet. The LS-coupling scheme gives an accurate description because the fine structure is much smaller than the energy separation (E_re ∼ 1.3×10⁶ m⁻¹) between the ³P term at ∼ 2.2×10⁶ m⁻¹ and the ¹P level at 3.5 × 10⁶ m⁻¹. In mercury the spacings of the levels, going down the table, are 0.18, 0.46 and 1.0 (in units of 10⁶ m⁻¹); these levels are not so clearly separated into a singlet and triplet. Taking the lowest three levels as ³P₀, ³P₁ and ³P₂ we see that the interval rule is not well obeyed since 0.46/0.18 = 2.6 (not 2).¹³ This deviation from the LS-coupling scheme is hardly surprising since this configuration has a spin–orbit interaction only slightly smaller than the singlet–triplet separation. However, even for this heavy atom, the LS-coupling scheme gives a closer approximation than the jj-coupling scheme.

¹³This identification of the levels is supported by other information, e.g. the determination of J from the Zeeman effect and the theoretically predicted behaviour of an sp configuration shown in Fig. 5.10.

Fig. 5.9 The terms of helium, magnesium and mercury are plotted on the same energy scale (with hydrogen on the left for comparison). The fine structure of the lighter atoms is too small to be seen on this scale and the LS-coupling scheme gives a very accurate description. This scheme gives an approximate description for the low-lying terms of mercury even though it has a much larger fine structure, e.g. for the 6s6p configuration the E_re > E_{s-o} but the interval rule is not obeyed because the spin–orbit interaction is not very small compared to the residual electrostatic interaction. The 1s² configuration of helium is not shown; it has a binding energy of −24.6 eV (see Fig. 3.4). The 1s2s and 1s2p configurations of helium lie close to the n = 2 shell in hydrogen, and similarly the 1s3l configurations lie close to the n = 3 shell. In magnesium, the terms of the 3snf configurations have very similar energies to those in hydrogen, but the differences get larger as l decreases. The energies of the terms in mercury have large differences from the hydrogen energy levels. Much can be learnt by carefully studying this term diagram, e.g. there is a ¹P term which has similar energy in the three configurations: 1s2p, 3s3p and 6s6p in He, Mg and Hg, respectively—thus the effective quantum number n* is similar despite the increase in n. Complex terms arise when both valence electrons are excited in Mg, e.g. the 3p² configuration, and the 5d⁹6s²6p configuration in Hg.

Fig. 5.10 A theoretical plot of the energy levels that arise from an sp configuration as a function of the strength of the spin–orbit interaction parameter β (of the p-electron defined in eqn 2.55). For β = 0 the two terms, ³P and ¹P, have an energy separation equal to twice the exchange integral; this residual electrostatic energy is assumed to be constant and only β varies in the plot. As β increases the fine structure of the triplet becomes observable. As β increases further the spin–orbit and residual electrostatic interactions become comparable and the LS-coupling scheme ceases to be a good approximation: the interval rule and (LS-coupling) selection rules break down (as in mercury, see Fig. 5.9). At large β the jj-coupling scheme is appropriate. The operator J commutes with H_{s−o} (and H_re); therefore H_{s−o} only mixes levels of the same J, e.g. the two J = 1 levels in this case. (The energies of the J = 0 and 2 levels are straight lines because their wavefunctions do not change.) Exercise 5.8 gives an example of this transition between the two coupling schemes for np(n+1)s configurations with n = 3 to 5 (that have small exchange integrals).

### Example 5.2 The 1s2p configuration in helium **J** | **E (m⁻¹)** --- | --- 2 | 16908687 1 | 16908694 0 | 16908793 1 | 17113500

The table gives the values of J and the energy, in units of m⁻¹ measured from the ground state, for the levels of the 1s2p configuration in helium. The ³P term has a fine-structure splitting of about 100 m⁻¹ that is much smaller than the singlet–triplet separation of 10⁶ m⁻¹ from the electrostatic interaction (twice the exchange integral). Thus the LS-coupling scheme gives an excellent description of the helium atom and the selection rules in Table 5.1 are well obeyed. But the interval rule is not obeyed—the intervals between the J levels are 7 m⁻¹ and 99 m⁻¹ and the fine structure is inverted. This occurs in helium because spin–spin and spin–other-orbit interactions have an energy comparable with that of the spin–orbit interaction.¹⁴ However, for atoms other than helium, the rapid increase in the strength of the spin–orbit interaction with Z ensures that H_{s−o} dominates over the others. Therefore the fine structure of atoms in the LS-coupling scheme usually leads to an interval rule.

¹⁴The spin–spin interaction arises from the interaction between two magnetic dipoles (independent of any relative motion). See eqn 6.12 and its explanation.

Further examples of energy levels are given in the exercises at the end of this chapter. Figure 5.10 shows a theoretical plot of the transition from the LS- to the jj-coupling scheme for an sp configuration. Conservation of the total angular momentum means that J is a good quantum number even in the intermediate coupling regime and can always be used to label the levels. The notation ²ˢ⁺¹L_J for the LS-coupling scheme is often used even for systems in the intermediate regime and also for one-electron systems, e.g. 1s ²S₁/₂ for the ground state of hydrogen.

Table 5.1 Selection rules for electric dipole (E1) transitions in the LS-coupling scheme. Rules 1–4 apply to all electric dipole transitions; rules 5 and 6 are obeyed only when L and S are good quantum numbers. The right-hand column gives the structure to which the rule applies.

1.  ΔJ = 0, ±1 (J = 0 ⇸ J' = 0) — Level 2.  ΔM_J = 0, ±1 (M_J = 0 ⇸ M_J' = 0 if ΔJ = 0) — State

## 3.  Parity changes — Configuration

4.  Δl = ±1 (One electron jump) — Configuration 5.  ΔL = 0, ±1 (L = 0 ⇸ L' = 0) — Term 6.  ΔS = 0 — Term

## 5.4 Selection rules in the LS-coupling scheme

Table 5.1 gives the selection rules for electric dipole transitions in the LS-coupling scheme (listed approximately in the order of their strictness). The rule for J reflects the conservation of this quantity and is strictly obeyed; it incorporates the rule for Δj in eqn 2.59, but with the additional restriction J = 0 ⇸ J' = 0 that affects the levels with J = 0 that occur in atoms with more than one valence electron. The rule for ΔM_J follows from that for ΔJ: the emission, or absorption, of a photon cannot change the component along the z-axis by more than the change in the total atomic angular momentum. (This rule is relevant when the states are resolved, as in the Zeeman effect described in the following section.)¹⁵ The requirement for an overall change in parity and the selection rule for orbital angular momentum were discussed in Section 2.2. In a configuration nl...n'l' only one electron changes its value of l (and may also change n). The rule for ΔL allows transitions such as 3p4s ³P₁ – 3p4p ³P₁. The selection rule ΔS = 0 arises because the electric dipole operator does not act on spin, as noted in Chapter 3 on helium; as a consequence, singlets and triplets form two unconnected sets of energy levels, as shown in Fig. 3.5. Similarly, the singlet and triplet terms of magnesium shown in Fig. 5.9 could be rearranged. In the mercury atom, however, transitions with ΔS = 1 occur, such as 6s2 ¹S₀ – 6s6p ³P₁, that gives a so-called intercombination line with a wavelength of 254 nm.¹⁶ This arises because this heavy atom is not accurately described by the LS-coupling scheme.

¹⁵There is no simple physical explanation of why an M_J = 0 to M_J = 0 transition is forbidden. It is a result of the symmetry of the dipole matrix element ⟨γJM_J=0|r|γ'J'M'_J=0⟩, where γ and γ' represent the other quantum numbers. The particular case of J = J' = 1 and ΔM_J = 0 is discussed in Budker et al. (2003).

¹⁶This line comes from the second level in the table given in Example 5.1, since that is the ³P₁ level.

ng scheme and the spin-orbit interaction mixes some 1P wavefunction into the wavefunction for the term that has been labelled 3P (this being its major component). Although not completely forbidden, the rate of this transition is considerably less than it would be for a fully-allowed transition at the same wavelength; however, the intercombination line from a mercury lamp is strong because many of the atoms excited to triplet terms will decay back to the ground state via this transition (see Fig. 5.9).

## 5.5 The Zeeman effect

The Zeeman effect for atoms with a single valence electron was not presented in earlier chapters to avoid repetition and that case is covered by the general expression derived here for the LS-coupling scheme. The atom’s magnetic moment has orbital and spin contributions (see Blundell 2001, Chapter 2):

µ = −µL − gsµS. (5.9)

The interaction of the atom with an external magnetic field is described by HZE = −µ·B. The expectation value of this Hamiltonian can be calculated in the basis |LSJMJ⟩, provided that EZE ≪ Es−o ≪ Ere, i.e. the interaction can be treated as a perturbation to the fine-structure levels of the terms in the LS-coupling scheme. In the vector model we project the magnetic moment onto J (see Fig. 5.11) following the same rules as are used in treating fine structure in the LS-coupling scheme (and taking B=Bẑ). This gives

EZE = −⟨J| J·B = − (⟨L·J⟩/J + gs⟨S·J⟩/J ) BJz. (5.10)

In the vector model the quantities in angled brackets are time averages. In a quantum description treatment the quantities ⟨···⟩ are expectation values of the form ⟨JMJ |···|JMJ ⟩. In the vector model

EZE = gJµBMJ, (5.11)

where the Landé g-factor is gJ = {⟨L·J⟩ + gs⟨S·J⟩}/{J(J +1)}. Assuming that gs ≈ 2 (see Section 2.3.4) gives

gJ = 3S(S+1)−L(L+1) / 2J(J +1) . (5.12)

Singlet terms have S = 0 so J=L and gJ = 1 (no projection is necessary). Thus singlets all have the same Zeeman splitting between MJ states and transitions between singlet terms exhibit the normal Zeeman effect (shown in Fig. 5.12). The ∆MJ = ±1 transitions have frequencies shifted by ±µB/h with respect to the ∆MJ = 0 transitions.

In atoms with two valence electrons the transitions between triplet terms exhibit the anomalous Zeeman effect. The observed pattern depends on the values of gJ and J for the upper and lower levels, as shown in Fig. 5.13. In both the normal and anomalous effects the π-transitions (∆MJ = 0) and σ-transitions (∆MJ = ±1) have the same polarizations as in the classical model in Section 1.8. Other examples in Exercises 5.10 to 5.12 show how observation of the Zeeman pattern gives information about the angular momentum coupling in the atom. (The Zeeman effect observed for the 2P1/2–2S1/2 and 2P3/2–2S1/2 transitions that arise between the fine-structure components of the alkalis and hydrogen is treated in Exercise 5.13.) Exercise 5.14 goes through the Paschen–Back effect that occurs in a strong external magnetic field—see Fig. 5.14.

## 5.6 Summary

Figure 5.15 shows the different layers of structure in a case where the LS-coupling scheme is a good approximation, i.e. the residual electrostatic interaction dominates the two magnetic interactions (spin–orbit and with an external magnetic field). The spin–orbit interaction splits terms into different J levels. The Zeeman effect of a weak magnetic field splits the levels into states of given MJ, that are also referred to as Zeeman sub-levels.

There are various ways in which this simple picture can break down.

(a) Configuration mixing occurs if the residual electrostatic interaction is not small compared to the energy gap between the configurations—this is common in atoms with complex electronic structure.

(b) The jj-coupling scheme is a better approximation than LS-coupling or Russell–Saunders coupling when the spin–orbit interaction is greater than the residual electrostatic interaction.

(c) The Paschen–Back effect arises when the interaction with an external magnetic field is stronger than the spin–orbit interaction (with the internal field). This condition is difficult to achieve except for atoms with a low atomic number and hence small fine structure. Similar physics arises in the study of the Zeeman effect on hyperfine structure where the transition between the low-field and high-field regimes occurs at values of the magnetic field that are easily accessible in experiments (see Section 6.3).

Further reading

The mathematical methods that describe the way in which angular momenta couple together form the backbone of the theory of atomic structure. In this chapter the quantum mechanical operators have been treated by analogy with classical vectors (the vector model) and the Wigner–Eckart theorem was mentioned to justify the projection theorem. Graduate-level texts give a more comprehensive discussion of the quantum theory of angular momentum, e.g. Cowan (1981), Brink and Satchler (1993) and Sobelman (1996).

Exercises

(5.1) Description of the LS-coupling scheme

Explain what is meant by the central-field approximation and show how it leads to the concept of electron configurations. Explain how perturbations arising from (a) the residual electrostatic interactions, and (b) the magnetic spin–orbit interactions, modify the structure of an isolated multi-electron configuration in the LS-coupling limit.

(5.2) Fine structure in the LS-coupling scheme

Show from eqn 5.4 that the J levels of the 3P term in the 3s4p configuration have a separation given by eqn 5.8 with βLS = β4p/2 (where β4p is the spin–orbit interaction of the 4p-electron).

(5.3) The LS-coupling scheme and the interval rule in calcium

Write down the ground configuration of calcium (Z = 20). The line at 610nm in the spectrum of neutral calcium consists of three components at relative positions 0, 106 and 158 (in units of cm−1). Identify the terms and levels involved in these transitions.

The spectrum also contains a multiplet of six lines with wavenumbers 5019, 5033, 5055, 5125, 5139 and 5177 (in units of cm−1). Identify the terms and levels involved. Draw a diagram of the relevant energy levels and the transitions between them. What further experiment could be carried out to check the assignment of quantum numbers?

(5.4) The LS-coupling scheme in zinc

The ground configuration of zinc is 4s2. The seven lowest energy levels of zinc are 0, 32311, 32501, 32890, 46745, 53672 and 55789 (in units of cm−1). Sketch an energy-level diagram that shows these levels with appropriate quantum numbers. What evidence do these levels provide that the LS-coupling scheme describes this atom. Show the electric dipole transitions that are allowed between the levels.

(5.5) The LS-coupling scheme and Hund’s rules

The 5D term has the lowest energy.) Specify the lowest-energy term for each of the five configurations nd, nd2, nd3, nd4 and nd5.

(5.7) Transition from LS- to jj-coupling

3s3p, Mg 3s3p, Fe14+

## 2.1850 23.386

3p4s, Si 3p7s, Si

## 2.1870 23.966 J Energy (106m−1) J Energy (106m−1)

## 2.1911 25.378

## 3.5051 35.193 0 3.968 0 6.154

1 3.976 1 6.160 2 3.996 2 6.182 1 4.099 1 6.188

The table gives the energy levels, in units of 106m−1 measured from the ground state, of the 3s3p configuration in neutral magnesium (Z = 12) and the magnesium-like ion Fe14+. Suggest, with reasons, further quantum numbers to identify these levels. Calculate the ratio of the spin–orbit interaction energies in the 3s3p configuration of Mg and Fe14+, and explain your result. Discuss the occurrence in the solar spectrum of a strong line at 41.726nm that originates from Fe14+. Would you expect a corresponding transition in neutral Mg? (5.6) LS-coupling for configurations with equivalent electrons

The table gives J-values and energies (in units of 106m−1 measured from the ground state) of the levels in the 3p4s and 3p7s configurations of silicon. Suggest further quantum numbers to identify the levels.

Why do the two configurations have nearly the same value of EJ=2 − EJ=0 but quite different energy separations between the two J = 1 states?

(5.8) Angular-momentum coupling schemes

4p5s, germanium 5p6s, tin J Energy (106m−1) J Energy (106m−1)

0 3.75 0 3.47 1 3.77 1 3.49 2 3.91 2 3.86 1 4.00 1 3.93

The table gives the J-values and energies (in units of 106m−1 measured from the ground state) of the levels in the configurations 4p5s in Ge and 5p6s in Sn. Data for the 3p4s configuration in Si are given in the previous exercise. How well does the LS-coupling scheme describe the energy levels of the np(n+1)s configurations with n = 3, 4 and 5? Give a physical reason for the observed trends in the energy levels.

One of the J = 1 levels in Ge has a Landé g-factor of gJ = 1.06. Which level would you expect this to be and why?

(a) List the values of the magnetic quantum numbers ml1, ms1, ml2 and ms2 for the two electrons in an np2 configuration to show that fifteen degenerate states exist within the central-field approximation. Write down the values of ML = ml1 + ml2 and MS = ms1 + ms2 associated with each of these states to show that the only possible terms in the LS-coupling scheme are 1S, 3P and 1D.

(b) The 1s22s22p2 configuration of doubly-ionized oxygen has levels at relative positions 0, 113, 307, 20271 and 43184 (in units of cm−1) above the ground state, and its spectrum contains weak emission lines at 19964cm−1 and 20158cm−1. Identify the quantum numbers for each of the levels and discuss the extent to which the LS-coupling scheme describes this multiplet.

(c) For six d-electrons, in the same sub-shell, write a list of the values of the ms and ml for the individual electrons corresponding to MS = 2 and ML = 2. Briefly discuss why this is the maximum value of MS, and why ML ≤ 2 for this particular value of MS. (Hence from 96 The LS-coupling scheme (5.9) Selection rules in the LS-coupling scheme State the selection rules that determine the configurations, terms and levels that can be connected by an electric dipole transition in the LS-coupling approximation. Explain which rules are rigorous, and which depend on the validity of the coupling scheme. Give a physical justification for three of these rules.

Which of the following are allowed for electric dipole transitions in the LS-coupling scheme: (a) 1s2s 3S1 –1s3d 3D1, (b) 1s2p 3P1 –1s3d 3D3, (c) 2s2p 3P1 –2p2 3P1, (d) 3p2 3P1 –3p2 3P2, (e) 3p6 1S0 –3p53d 1D2?

The transition 4d105s 2D5/2 – 4d105p 2P3/2 appears to involve two electrons jumping at the same time. This arises from configuration mixing—the residual electrostatic interaction may mix configurations. The commutation relations in eqns 5.2 and 5.3 imply that H only mixes terms of the same L, S and J. Suggest a suitable configuration that gives rise to a 2P3/2 level that could mix with the 4d105p configuration to cause this transition.

(5.10) The anomalous Zeeman effect What selection rule governs ∆MJ in electric dipole transitions? Verify that the 3S – 3P transition leads to the pattern of nine equally-spaced lines shown in Fig. 5.13 when viewed perpendicular to a weak magnetic field. Find the spacing for a magnetic flux density of 1T.

(5.11) The anomalous Zeeman effect Draw an energy-level diagram for the states of 3S and 3P levels in a weak magnetic field. Indicate the allowed electric dipole transitions between the Zeeman states. Draw the pattern of lines observed perpendicular to the field on a frequency scale (marked in units of µB/h).

(5.12) The anomalous Zeeman effect The above Zeeman pattern is observed for a spectral line that originates from one of the levels of a 3P term in the spectrum of a two-electron system; the numbers indicate the relative separations of the lines, observed perpendicular to the direction of the applied magnetic field. Identify L, S and J for the two levels in the transition.22 (5.13) The anomalous Zeeman effect in alkalis Note that atoms with one valence electron are not discussed explicitly in the text.

(a) Give the values of gJ for the one-electron levels 2S1/2, 2P1/2 and 2P3/2.

(b) Show that the Zeeman pattern for the 3s 2S1/2 – 3p 2P3/2 transition in sodium has six equally-spaced lines when viewed perpendicular to a weak magnetic field. Find the spacing (in GHz) for a magnetic flux density of 1T. Sketch the Zeeman pattern observed along the magnetic field.

(c) Sketch the Zeeman pattern observed perpendicular to a weak magnetic field for the 3s 2S1/2 – 3p 2P1/2 transition in sodium.

(d) The two fine-structure components of the 3s–3p transition in sodium in parts (b) and (c) have wavelengths of 589.6nm and 589.0nm, respectively. What magnetic flux density produces a Zeeman splitting comparable with the fine structure?23 (5.14) The Paschen–Back effect In a strong magnetic field L and S precess independently about the field direction (as shown in Fig. 5.14), so that J and MJ are not good quantum numbers and appropriate eigenstates are |LMLSMS⟩. This is called the Paschen–Back effect. In this regime the LS-coupling selection rules are ∆ML = 0, ±1 and ∆MS = 0 (because the electric dipole operator does not act on the spin).24 Show that the Paschen–Back effect leads to a pattern of three lines with the same spacing as in the normal Zeeman effect (i.e. the same as if we completely ignore spin).25 21 In the discussion of the LS-coupling scheme we treated Hre as a perturbation on a configuration and assumed that Ere is small compared to the energy separation between the configurations in the central field. This is rarely true for high-lying configurations of complex atoms.

22 The relative intensities of the components have not been indicated.

23 This value is greater than 1T so the assumption of a weak field in part (b) is valid.

24 The rules for J and MJ are not relevant in this regime.

25 The Paschen–Back effect occurs when the valence electrons interact more strongly with the external magnetic field than with the orbital field in Hs−o. The LS-coupling scheme still describes this system, i.e. L and S are good quantum numbers.

Hyperfine structure and isotope shift

## 6.1 Hyperfine structure

Up to this point we have regarded the nucleus as an object of charge +Ze and mass M, but it has a magnetic moment µI that is related to the nuclear spin I by µI = gIµNI. (6.1)

Comparing this to the electron’s magnetic moment −gsµBs we see that there is no minus sign.1 Nuclei have much smaller magnetic moments than electrons; the nuclear magneton µN is related to the Bohr magneton µB by the electron-to-proton mass ratio: µN = µB me/M1 ≈ µB /1836. (6.2)

The interaction of µI with the magnetic flux density created by the atomic electrons Be gives the Hamiltonian H = −µI · Be. (6.3) HFS This gives rise to hyperfine structure which, as its name suggests, is smaller than fine structure. Nevertheless, it is readily observable for isotopes that have a nuclear spin (I ≠ 0).

The magnetic field at the nucleus is largest for s-electrons and we shall calculate this case first. For completeness the hyperfine structure for electrons with l ≠ 0 is also briefly discussed, as well as other effects that can have similar magnitude.

6.1.1 Hyperfine structure for s-electrons We have previously considered the atomic electrons as having a charge distribution of density −e|ψ(r)|2, e.g. in the interpretation of the direct integral in helium in eqn 3.15 (see also eqn 6.22). To calculate magnetic interactions we need to consider an s-electron as a distribution of magnetisation given by M = −gsµs|ψ(r)|2. (6.4)

This corresponds to the total magnetic moment of the electron −gsµs spread out so that each volume element d3r has a fraction |ψ(r)|2 d3r of the total. For s-electrons this distribution is spherically symmetric and surrounds the nucleus, as illustrated in Fig. 6.1. To calculate the field at r = 0 we shall use the result from classical electromagnetism2 that inside a uniformly magnetised sphere the magnetic flux density is B = (2/3)µ0M. (6.5)

However, we must be careful when applying this result since the distribution in eqn 6.4 is not uniform—it is a function of r. We consider the spherical boundary at r = r spherical distribution 3 This does not correspond to anything physical in the atom but is chosen for mathematical convenience. The radius \( r_b \) should be greater than the radius of the nucleus \( r_N \), and it is easy to see that the nuclear nucleons have a size of a few fermi (\( 10^{-15} \, \text{m} \)), that is six orders of magnitude less.

(a) A sphere of radius \( r = r_b \), where \( r_b \approx a_0 \) so that the electronic wavefunction squared has a constant value of \( |\psi(0)|^2 \) throughout this inner region, as indicated on Fig. 6.2. From eqn 6.5 the field inside this uniformly magnetised sphere is

\[ \mathbf{B} = -\frac{g_s \mu_B}{4\pi} |\psi_{ns}(0)|^2 \mathbf{s}. \tag{6.6} \]

The magnetisation is a function of \( r \) only and therefore each shell has a uniform magnetisation \( M(r) \) between \( r \) and \( r+dr \). The proof that these shells do not produce a magnetic flux density at \( r = 0 \) does not require \( M(r) \) to be the same for all the shells, and clearly this is not the case. Alternatively, this result can be obtained by integrating the contributions to the field at the origin from the magnetic moments \( M(r) d^3 r \) over all angles (\( \theta \) and \( \phi \)).

(b) The part of the distribution outside the sphere \( r > r_b \) produces no field at \( r = 0 \), as shown by the following argument. Equation 6.5 for the field inside a sphere does not depend on the radius of that sphere—it gives the same field for a sphere of radius \( r \) and a sphere of radius \( r+dr \). Therefore the contribution from each shell of thickness \( dr \) is zero. The region \( r > r_b \) can be considered as being made up of many such shells that give no additional contribution to the field.

Putting this field and \( \mu \) from eqn 6.1 into eqn 6.3 gives

\[ H_{\text{HFS}} = g_I \mu_N \mathbf{I} \cdot \frac{3}{4\pi} \mu_0 g_s \mu_B |\psi_{ns}(0)|^2 \mathbf{s} = A \mathbf{I} \cdot \mathbf{s}. \tag{6.7} \]

Fig. 6.2(a) The probability density \( |\psi(r)|^2 \) of an s-electron at small distances (\( r \ll a_0 \)) is almost constant. The distribution of nuclear matter \( \rho_N(r) \) gives an indication of the nuclear radius \( r_N \). To calculate the interaction of the nuclear magnetic moment with an s-electron the region is divided into two parts by a boundary surface of radius \( r = r_b \gg r_N \) (as also shown in Fig. 6.1). The inner region corresponds to a sphere of uniform magnetisation that produces a flux density \( B_e \) at \( r = 0 \). The nuclear magnetic moment interacts with this field.

This is called the Fermi contact interaction since it depends on \( |\psi_{ns}(0)|^2 \) being finite. It can also be expressed as

\[ H_{\text{HFS}} = A \mathbf{I} \cdot \mathbf{J} \tag{6.8} \]

because \( \mathbf{J} = \mathbf{s} \) for \( l = 0 \). It is useful to write down this more general form at an early stage since it turns out that an interaction proportional to \( \mathbf{I} \cdot \mathbf{J} \) is also obtained when \( l \neq 0 \).

We have already considered the effect of an interaction proportional to a dot product of two angular momenta when looking at the spin–orbit interaction \( \beta \mathbf{S} \cdot \mathbf{L} \) (eqn 5.4). In the same way the hyperfine interaction in eqn 6.8 causes \( \mathbf{I} \) and \( \mathbf{J} \) to change direction but the total angular momentum of the atom \( \mathbf{F} = \mathbf{I} + \mathbf{J} \) remains constant. The quantities \( \math ΔE Quadrupole)

That exercise also shows how this rule can be used to deduce F and 12This interval rule for magnetic dipole hence the nuclear spin I from a given hyperfine structure.12 hyperfine structure can be disrupted by The hyperfine-structure constant A(n,l,j) is smaller for l > 0 than the quadrupole interaction. Some nu- for l = 0 and the same n. Exact calculation shows that the hyperfine- clei are not spherical and their charge distribution has a quadrupole moment structure constants of the hydrogenic levels np 2P 1/2 and ns 2S 1/2 are that interacts with the gradient of the in the ratio electric field at the nucleus. This elec- A(n2P 1/2 ) 1 = . (6.15)

tric quadrupole interaction turns out to A(n2S ) 3 have an energy comparable to the inter- 1/2 action of the magnetic dipole moment This ratio is smaller in the alkalis, e.g. ∼ 1/10 in the examples below, µI with Be. Nuclei, and atoms, do not because the closed shells of electrons screen the nuclear charge more have static electric dipole moments (for states of definite parity). effectively for p-electrons than for s-electrons.

6.1.4 Comparison of hyperfine and fine structures The analogy between hyperfine and fine structures is summarised in Table 6.1.

For fine structure in the alkalis we found the Landé formula (eqn 4.13)

## Z2 Z2

FS (n ∗)

α2hcR∞. (6.16)

The Z4 scaling for a hydrogenic system is reduced to E ∝ Z2 for neu- FS tral atoms since the effective outer atomic number is Z = 1, and Z ∼ Z o i gives a reasonable approximation in the inner region. Applying similar considerations to the hyperfine structure shows that the dependence on Z3 in eqn 6.10 reduces to Z Z2 m HFS (n ∗)

3 M α2hcR∞. (6.17)

The mass ratio arises from µ /µ = m /M . Hyperfine structure scales N B e p as Z, whereas fine structure scales as Z2; thus E varies much less HFS than E , as the following comparison of the splittings for Na and Cs FS shows.

## 6.1 Hyperfine structure

Na, Z =11 Cs, Z =55 E(3p 2P 3/2 )−E(3p 2P 1/2 ), E(6p 2P 3/2 )−E(6p 2P 1/2 ), ∆f =510 GHz ∆f =16600 GHz

## FS FS

For the ground state 3s 2S 1/2 , For the ground state 6s 2S 1/2 , ∆f =1.8 GHz ∆f =9.2 GHz

## HFS HFS

For 3p 2P 1/2 , For 6p 2P 1/2 , ∆f =0.18 GHz ∆f =1.2 GHz

## HFS HFS

The hyperfine splitting of the ground states and the fine-structure splitting of the first excited states are indicated on the plot of energies against Z in Fig. 6.5. The values shown are only a guideline; e.g. different Energy (eV) Gross structure Residual electrostatic energy Fine structure (first excited state)

Hyperfine structure (ground state)

Hg Mg He 10−1 Cs 10−2 10−3 Na Fig. 6.5 A logarithmic plot of the energy of various structures against atomic number Z; the hyperfine split- ting of the ground state is plotted with 10−4 data from Fig. 5.7. All the points are close to the maximum values of that quantity for low-lying configurations, terms, levels and hyperfine levels (as 10−5 appropriate) of neutral atoms with one or two valence electrons, and these il- lustrate how these quantities vary with Z. This is only a rough guideline in Mg H He Na Cs Hg particular cases; higher-lying configura- 10−6 tions in neutral atoms have smaller val- 1 10 100 ues and in highly-ionized systems the structures have higher energies.

104 Hyperfine structure and isotope shift isotopes of the same element have different hyperfine splittings because the magnetic moment µI depends on the nuclear structure. The ground state of hydrogen has an especially large hyperfine structure that is greater than that of lithium (Z =3), see Exercise 6.3.

Example 6.2 Hyperfine structure of europium Figure 6.6 shows an experimental trace of a 4f76s2 8S − 4f76s6d 8D 7/2 11/2 transition in europium obtained by Doppler-free laser spectroscopy (Kro- 13Two-photon spectroscopy is ex- nfeldt and Weber 1991).13 The ground level (4f76s2 8S 7/2 ) has a small plained in Section 8.4 hyperfine structure, from the unpaired f-electrons, that causes the small splitting of the peaks labelled 3, 4, 5, 6 and 7 (barely resolved for peak 3); however, this detail will not be considered further in the following 14It is straightforward to apply the in- analysis,14 which concentrates on the much larger hyperfine structure of terval rule even when both the lower the 4f76s6d 8D level that arises mainly from the unpaired s-electron.

11/2 and upper levels have hyperfine struc- The spectrum has a dozen main peaks. Since J = 11/2 a naive anal- ture.

ysis might suppose that I ≈ J and so the observed peaks arise from transitions to the 2J+1=12 hyperfine levels expected in this case, i.e.

F = I+J, I+J−1, ..., I−J+1 and I−J. This is obviously wrong for various reasons: it is clear that the pattern of all twelve peaks does not fit any simple rule and also this element has two stable isotopes 151Eu and 153Eu. As indicated by their similar shape, the peaks labelled 3, 4, 5, 6 and 7 all belong to same isotope (151Eu) and this can be verified by the interval rule as shown in the following table.

## I II III IV V

Peak Position (GHz) EF−1−EF (GHz) Ratio of differences, x x h x−1 3 21.96 – – – 4 19.14 2.82 – – 5 15.61 3.53 1.252 5.0 6 11.37 4.24 1.201 6.0 7 6.42 4.95 1.167 7.0 g 0.77 5.65 1.141 8.1 7 6 5 4 3 0 5 10 15 20 Fig. 6.6 An experimental trace of a 4f76s2 8S 7/2 – 4f76s6d 8D 11/2 transition in europium obtained by Doppler-free laser spectroscopy (Kronfeldt and Weber 1991). Copyright 1991 by the American Physical Society.

## 6.2 Isotope shift

Column II in this table gives the positions of the peaks15 measured 15The highest peak in the case of the from Fig. 6.6. Column III gives the difference between the frequencies in closely-spaced pairs.

column II (the intervals between the peaks), e.g. 21.96−19.14= 2.82.

Column IV gives the ratio of the intervals in column III, e.g. 3.53/2.82= 1.252. The interval rule for hyperfine structure in eqn 6.14 predicts that x= EF − EF−1 AF . (6.18)

EF−1 − EF−2 A(F −1) F −1 Rearrangement gives the total angular momentum F in terms of x as F = . (6.19)

x−1 The numerical values of this quantity in column V (that have been cal- culated from the data by the above procedure) confirm that F has the value used to label the peaks. Moreover, we find that peak g fits the in- 16The proof of this result using opera- terval rule with F = 8. Thus, since this level has J = 11/2, this isotope tors can be found in quantum mechan- (151Eu) must have a nuclear spin of I = 5/2 — this follows from the rules ics texts. It can be justified by anal- for the addition of angular momentum which allow values of F between ogy with vector addition: the maxi- F = I+J = 8 and F = |I−J| = 3.16 Exercise 6.5 shows that the mum value occurs when the two an- max min gular momentum vectors point in the other six peaks a to f also obey an interval rule and they all belong to same direction and the minimum value another isotope (153Eu).

when they are anti-parallel.

## 6.2 Isotope shift

In addition to the (magnetic dipole) hyperfine interaction in eqn 6.8 there are several other effects that may have a comparable magnitude (or might even be larger).17 This section describes two effects that lead 17The quadrupole interaction was to a difference in the frequency of the spectral lines emitted by different noted in Table 6.1, but will not be dis- cussed further.

isotopes of an element.

6.2.1 Mass effects In Chapter 1 we saw that, in the Bohr model, energies are proportional to the reduced mass of the electron, given in eqn 1.13, and this scal- ing also applies to the solutions of the Schrödinger equation. Thus a transition between two levels of energies E and E has a wavenumber 1 2 ν% = (E − E )/hc that is related to ν% ∞, the value for a ‘theoretical’ 1 2 atom with a nucleus of infinite mass, by ν% = ν% ∞ × N , (6.20)

+M 18Strictly, atomic mass units should be used rather than Mp. The difference where M N is the mass of the nucleus. However, ν% ∞ cannot be measured. between the mass of an atom and its What we can observe is the difference in wavenumbers between two nucleus equals the mass of the electrons isotopes of an element, e.g. hydrogen and deuterium for Z = 1. In including the contribution from their binding energy. However, for this esti- general, for two isotopes with atomic masses A(cid:1) and A(cid:1)(cid:1), we can make the approximation M N = A(cid:1) M p or A(cid:1)(cid:1) M p , so that18 cis y.

we do not need to know MN pre-

106 Hyperfine structure and isotope shift ∆ν% Mass = ν% A(cid:1)(cid:1) − ν% A(cid:1) = 1 + m ν% ∞ / A(cid:1)(cid:1) M − 1 + m ν% ∞ / A(cid:1) M e p e p ≈ m ν% 1 − A(cid:1)(cid:1) M e − 1 − A(cid:1) M p p m δA ≈ A(cid:1) A(cid:1)(cid:1)

ν% ∞. (6.21)

This is called the normal mass shift and the energy difference hc∆ν% Mass is plotted in Fig. 6.7, assuming that δA = 1, A ≈ A(cid:1) ≈ 2Z, and that E − E ≈ 2 eV for a visible transition. The mass shift is largest for 2 1 hydrogen and deuterium where A(cid:1)(cid:1) = 2A(cid:1) ≈ 2M (Exercise 1.1); it is p larger than the fine structure in this case. For atoms with more than one electron there is also a specific mass shift that has the same order of 19See Exercise 6.12 and also Woodgate magnitude as the normal mass effect, but is much harder to calculate.19 (1980). Equation 6.20 shows that the mass shift always leads to the heavier isotope having a higher wavenumber — by definition the reduced mass of the electron is less than m , and as the atomic mass increases the energy e levels become closer to those of the theoretical atom with a nucleus of infinite mass.

6.2.2 Volume shift Although nuclei have radii which are small compared to the scale of electronic wavefunctions, r ≪ a , the nuclear size has a measurable N 0 effect on spectral lines. This finite nuclear size effect can be calculated as a perturbation in two complementary ways. A simple method uses Gauss’ theorem to determine how the electric field of the nuclear charge distribution differs from −Ze/4πε r2 for r ≈ r (see Woodgate 1980).

0 N Alternatively, to calculate the electrostatic interaction of two overlap- ping charge distributions (as in eqn 3.15, for example) we can equally 20For hyperfine structure we were con- well find the energy of the nucleus in the potential created by the elec- cerned with the nuclear magnetic mo- tronic charge distribution (in an analogous way to the calculation of the ment

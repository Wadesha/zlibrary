# David Tong Lectures on Solid State Physicssolidstate

> 来源文件：pre_David_Tong_Lectures_on_Solid_State_Physicssolidstate.txt
> 字符数（约）：211038
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Solid State Physics University of Cambridge Part II Mathematical Tripos David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 0BA, UK http://www.damtp.cam.ac.uk/user/tong/solidstate.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources There are many excellent books on Solid State Physics. The two canonical books are • Ashcroft and Mermin, Solid State Physics • Kittel, Introduction to Solid State Physics Both of these go substantially beyond the material covered in this course. Personally, I have a slight preference for the verbosity of Ashcroft and Mermin.

A somewhat friendlier, easier going book is • Steve Simon, Solid State Physics Basics It covers only the basics, but does so very well. (An earlier draft can be downloaded from Steve Simon’s homepage; see below for a link.)

A number of lecture notes are available on the web. Links can be found on the course webpage: http://www.damtp.cam.ac.uk/user/tong/solidstate.html

Contents

## 0. Introduction

## 1. Particles in a Magnetic Field

## 1.1 Gauge Fields

1.1.1 The Hamiltonian 3 1.1.2 Gauge Transformations 4

## 1.2 Landau Levels

1.2.1 Degeneracy 7 1.2.2 Symmetric Gauge 9 1.2.3 An Invitation to the Quantum Hall Effect 10

## 1.3 The Aharonov-Bohm Effect

1.3.1 Particles Moving around a Flux Tube 13 1.3.2 Aharonov-Bohm Scattering 15

## 1.4 Magnetic Monopoles

1.4.1 Dirac Quantisation 16 1.4.2 A Patchwork of Gauge Fields 19 1.4.3 Monopoles and Angular Momentum 20

## 1.5 Spin in a Magnetic Field

1.5.1 Spin Precession 24 1.5.2 A First Look at the Zeeman Effect 25

## 2. Band Structure

## 2.1 Electrons Moving in One Dimension

2.1.1 The Tight-Binding Model 26 2.1.2 Nearly Free Electrons 32 2.1.3 The Floquet Matrix 39 2.1.4 Bloch’s Theorem in One Dimension 41

## 2.2 Lattices

2.2.1 Bravais Lattices 46 2.2.2 The Reciprocal Lattice 52 2.2.3 The Brillouin Zone 55

## 2.3 Band Structure

2.3.1 Bloch’s Theorem 58 2.3.2 Nearly Free Electrons in Three Dimensions 60 2.3.3 Wannier Functions 64 2.3.4 Tight-Binding in Three Dimensions 65 2.3.5 Deriving the Tight-Binding Model 66

## 2.4 Scattering Off a Lattice

2.4.1 The Bragg Condition 75 2.4.2 The Structure Factor 76 2.4.3 The Debye-Waller Factor 78

## 3. Electron Dynamics in Solids

## 3.1 Fermi Surfaces

3.1.1 Metals vs Insulators 81 3.1.2 The Discovery of Band Structure 86 3.1.3 Graphene 87

## 3.2 Dynamics of Bloch Electrons

3.2.1 Velocity 92 3.2.2 The Effective Mass 94 3.2.3 Semi-Classical Equation of Motion 95 3.2.4 Holes 97 3.2.5 Drude Model Again 99

## 3.3 Bloch Electrons in a Magnetic Field

3.3.1 Semi-Classical Motion 101 3.3.2 Cyclotron Frequency 103 3.3.3 Onsager-Bohr-Sommerfeld Quantisation 104 3.3.4 Quantum Oscillations 106

## 4. Phonons

## 4.1 Lattices in One Dimension

4.1.1 A Monatomic Chain 109 4.1.2 A Diatomic Chain 111 4.1.3 Peierls Transition 113 4.1.4 Quantum Vibrations 116 4.1.5 The Mössbauer Effect 120

## 4.2 From Atoms to Fields

4.2.1 Phonons in Three Dimensions 123 4.2.2 From Fields to Phonons 125

Acknowledgements This material is taught as part of the “Applications in Quantum Mechanics” course of the Cambridge mathematical tripos.

## 0. Introduction

Solid state physics is the study of “stuff”, of how the wonderfully diverse properties of solids can emerge from the simple laws that govern electrons and atoms.

There is one, over-riding, practical reason for wanting to understand the behaviour of stuff: this is how we build things. In particular, it is how we build the delicate and powerful technologies that underlie our society. Important though they are, such practicalities will take a back seat in our story. Instead, our mantra is “knowledge for its own sake”. Indeed, the subject of solid state physics turns out to be one of extraordinary subtlety and beauty. If such knowledge ultimately proves useful, this is merely a happy corollary.

We will develop only the basics of solid state physics. We will learn how electrons glide through seemingly impenetrable solids, how their collective motion is described by a Fermi surface, and how the vibrations of the underlying atoms get tied into bundles of energy known as phonons. We will learn that electrons in magnetic fields can do strange things and start to explore some of the roles that geometry and topology play in quantum physics.

One of the ultimate surprises of solid state physics is how the subject later dovetails with ideas from particle physics. At first glance, one might have thought these two disciplines should have nothing to do with each other. Yet one of the most striking themes in modern physics is how ideas from one have influenced the other. In large part this is because both subjects rest on some of the deepest principles in physics: ideas such as symmetry, topology and universality. Although much of what we cover in these lectures will be at a basic level, we will nonetheless see some hint s of these deeper connections. We will, for example, see the Dirac equation — originally introduced to unify relativity and quantum mechanics — emerging from graphene. We will learn how the vibrations of a lattice, and the resulting phonons, provide a baby introduction to quantum field theory.

## 1. Particles in a Magnetic Field

The purpose of this chapter is to understand how quantum particles react to magnetic fields. In contrast to later sections, we will not yet place these particles inside solids, for the simple reason that there is plenty of interesting behaviour to discover before we do this. Later, in Section 3.1, we will understand how these magnetic fields affect the electrons in solids. Before we get to describe quantum effects, we first need to highlight a few of the more subtle aspects that arise when discussing classical physics in the presence of a magnetic field.

## 1.1 Gauge Fields

Recall from our lectures on Electromagnetism that the electric field E(x,t) and magnetic field B(x,t) can be written in terms of a scalar potential ϕ(x,t) and a vector potential A(x,t), ∂A E = −∇ϕ− and B = ∇×A (1.1)

∂t Both ϕ and A are referred to as gauge fields. When we first learn electromagnetism, they are introduced Schrödinger方程

最后，我们可以转向量子理论。我们将在下一节研究能谱，但首先我们想了解规范变换如何作用。遵循通常的量子化程序，我们将正则动量替换为

p → −iℏ∇

因此，处于电场和磁场中的粒子的含时薛定谔方程具有如下形式

iℏ ∂ψ/∂t = Hψ = (−iℏ∇−qA)² ψ/(2m) + qϕψ (1.7)

将动能项移位以包含矢势A有时被称为最小耦合。

在求解能谱之前，有两个教训值得注意。首先，不可能仅用E和B来表述在电场和磁场中运动的粒子的量子力学。我们不得不引入规范场A和ϕ。这可能会让你怀疑，或许A和ϕ的意义不止我们最初想的那么简单。我们将在第1.3节看到这个问题的答案。（剧透：答案是肯定的。）

第二个教训来自于考察方程(1.7)在规范变换下的表现。很容易验证，只有当波函数本身也随一个位置相关的相位变换时，薛定谔方程才是协变的（即变换性质良好）

ψ(x,t) → e^{iqα(x,t)/ℏ} ψ(x,t) (1.8)

这与在磁场存在下p不是规范不变量的事实密切相关。重要的是，这个规范变换不影响由|ψ|²给出的物理概率。

证明薛定谔方程在规范变换(1.8)下变换良好的最简单方法是定义协变导数

D_t = ∂_t + iqϕ/ℏ 和 D_i = ∂_i − iqA_i/ℏ

用这些协变导数表示，薛定谔方程变为

iℏ D_t ψ = − (ℏ²/2m) D²ψ (1.9)

这些协变导数被设计为在规范变换(1.6)和(1.8)下表现良好。你可以验证它们只获得一个相位：

D_t ψ → e^{iqα/ℏ} D_t ψ 和 D_i ψ → e^{iqα/ℏ} D_i ψ

这确保了薛定谔方程(1.9)是协变的。

## 1.2 朗道能级

我们现在的任务是求解薛定谔方程的能谱和波函数。我们感兴趣的是电场为零（E = 0）且磁场恒定的情况。量子哈密顿量为

H = (p−qA)²/(2m) (1.10)

我们取磁场沿z方向，即B = (0,0,B)。为了进行下去，我们需要找到一个满足∇×A = B的规范势A。当然，选择不是唯一的。这里我们选择

A = (0, xB, 0) (1.11)

这被称为朗道规范。注意，磁场B = (0,0,B)在(x,y)平面的平移对称和旋转对称下是不变的。然而，A的选择不是；它破坏了x方向的平移对称（但y方向未破坏）和旋转对称。这意味着，虽然物理结果在所有对称性下都是不变的，但中间计算过程不会明显表现出不变性。这种妥协在处理磁场时是典型的。

哈密顿量(1.10)变为

H = (p_x² + (p_y − qBx)² + p_z²)/(2m)

由于我们在y和z方向有明显的平移不变性，我们有[p_y, H] = [p_z, H] = 0，因此可以寻找同时也是p_y和p_z本征态的能量本征态。这启发我们使用试探波函数

ψ(x) = e^{ik_y y + ik_z z} χ(x) (1.12)

用动量算符p_y = −iℏ∂_y和p_z = −iℏ∂_z作用在这个波函数上，我们得到

p_y ψ = ℏk_y ψ 和 p_z ψ = ℏk_z ψ

不含时薛定谔方程为Hψ = Eψ。将我们的试探解(1.12)代入，只需将p_y和p_z替换为它们的本征值，我们得到

Hψ(x) = [p_x²/(2m) + (ℏk_y − qBx)²/(2m) + ℏ²k_z²/(2m)] ψ(x) = Eψ(x)

我们可以将其写为关于函数χ(x)的本征值方程。我们有

H̃ χ(x) = (E − ℏ²k_z²/(2m)) χ(x)

其中H̃是我们非常熟悉的形式：它是一个在x方向的谐振子哈密顿量，其中心从原点位移了，

H̃ = p_x²/(2m) + (1/2) m ω_B² (x − k_y l_B²)² (1.13)

谐振子的频率是回旋频率ω = qB/m，我们还引入了一个长度尺度l_B。这是一个特征长度尺度，它支配着磁场中的任何量子现象。它被称为磁长度。

l_B = √(ℏ/(qB))

为了让你有个概念，在1特斯拉的磁场中，电子的磁长度约为l_B ≈ 2.5×10^{-8} m。

在哈密顿量(1.13)中发生了一些相当奇怪的事情：y方向的动量ℏk_y变成了x方向谐振子的位置，后者现在中心位于x = k_y l_B²。

我们可以立即写出(1.13)的能量本征值；它们就是谐振子的本征值

E = ℏω (n + 1/2) + ℏ²k_z²/(2m)，n = 0,1,2,... (1.14)

波函数依赖于三个量子数，n ∈ ℕ 以及 k_y, k_z ∈ ℝ。

ψ_{n,k}(x,y) ∼ e^{ik_yy+ik_zz} H_n\left( \frac{y}{l_B} \right) e^{-(x-k_yl_B^2)^2/2l_B^2} \tag{1.15} with H the usual Hermite polynomial wavefunctions of the harmonic oscillator. The ∼ reflects the fact that we have made no attempt to normalise these wavefunctions. The wavefunctions look like strips, extended in the y direction but exponentially localised around x = k_yl_B^2 in the x direction. However, you shouldn’t read too much into this. As we will see shortly, there is large degeneracy of wavefunctions and by taking linear combinations of these states we can cook up wavefunctions that have pretty much any shape you like.

1.2.1 Degeneracy The dynamics of the particle in the z-direction is unaffected by the magnetic field B = (0,0,B). To focus on the novel physics, let’s restrict to particles with k_z = 0. The energy spectrum then coincides with that of a harmonic oscillator, E = ℏ\omega_B \left( n + \frac{1}{2} \right) \tag{1.16} In the present context, these are called Landau levels. We see that, in the presence of a magnetic field, the energy levels of a particle become equally spaced, with the gap between each level proportional to the magnetic field B. Note that the energy spectrum looks very different from a free particle moving in the (x,y)-plane.

The states in a given Landau level are not unique. Instead, there is a huge degeneracy, with many states having the same energy. We can see this in the form of the wavefunctions (1.15) which, when k_z = 0, depend on two quantum numbers, n and k_y. Yet the energy (1.16) is independent of k_y.

Let’s determine how large this degeneracy of states is. To do so, we need to restrict ourselves to a finite region of the (x,y)-plane. We pick a rectangle with sides of lengths L_x and L_y. We want to know how many states fit inside this rectangle.

Having a finite size L_y is like putting the system in a box in the y-direction. The wavefunctions must obey \psi(x,y+L_y,z) = \psi(x,y,z) \implies e^{ik_yL_y} = 1 This means that the momentum k_y is quantised in units of 2π/L_y.

Having a finite size L_x is somewhat more subtle. The reason is that, as we mentioned above, the gauge choice (1.11) does not have manifest translational invariance in the x-direction. This means that our argument will be a little heuristic. Because the wavefunctions (1.15) are exponentially localised around x = k_yl_B^2, for a finite sample restricted to 0 ≤ x ≤ L_x we would expect the allowed k_y values to range between 0 ≤ k_y ≤ L_x/l_B^2. The end result is that the number of states in each Landau level is given by N = \int_0^{L_x/l_B^2} \frac{L_y}{2\pi} dk_y = \frac{L_xL_y}{2\pi l_B^2} = \frac{qBA}{2\pi\hbar} \tag{1.17} where A = L_xL_y is the area of the sample. Strictly speaking, we should take the integer part of the answer above.

The degeneracy (1.17) is very very large. Throwing in some numbers, there are around 10^{10} degenerate states per Landau level for electrons in a region of area A = 1 cm^2 in a magnetic field B ∼ 0.1 T. This large degeneracy ultimately leads to an array of dramatic and surprising physics.

1.2.2 Symmetric Gauge It is worthwhile to repeat the calculations above using a different gauge choice. This will give us a slightly different perspective on the physics. A natural choice is symmetric gauge A = -\frac{1}{2} x \times B = \frac{B}{2} (-y, x, 0) \tag{1.18} This choice of gauge breaks translational symmetry in both the x and the y directions. However, it does preserve rotational symmetry about the origin. This means that angular momentum is now a good quantum number to label states.

In this gauge, the Hamiltonian is given by H = \frac{1}{2m} \left[ \left( p_x + \frac{qBy}{2} \right)^2 + \left( p_y - \frac{qBx}{2} \right)^2 \right] + p_z^2 = -\frac{\hbar^2}{2m} \nabla^2 - \frac{qB}{2m} L_z + \frac{q^2B^2}{8m} (x^2 + y^2) \tag{1.19} where we’ve introduced the angular momentum operator L_z = x p_y - y p_x We’ll again restrict to motion in the (x,y)-plane, so we focus on states with k_z = 0.

It turns out that complex variables are particularly well suited to describing states in symmetric gauge, in particular in the lowest Landau level with n = 0. We define w = x + iy and \bar{w} = x - iy Correspondingly, the complex derivatives are \partial = \frac{1}{2} \left( \frac{\partial}{\partial x} - i \frac{\partial}{\partial y} \right) and \bar{\partial} = \frac{1}{2} \left( \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} \right)

which obey \partial w = \bar{\partial} \bar{w} = 1 and \bar{\partial} w = \partial \bar{w} = 0. The Hamiltonian, restricted to states with k_z = 0, is then given by H = -\frac{2\hbar^2}{m} \partial \bar{\partial} - \frac{\omega_B}{2} L_z + \frac{m\omega_B^2}{8} w\bar{w} where now L_z = \hbar (w \partial - \bar{w} \bar{\partial})

It is simple to check that the states in the lowest Landau level take the form \psi_0 (w,\bar{w}) = f(w) e^{-|w|^2 / 4l_B^2} for any holomorphic function f(w). These all obey H \psi_0 (w,\bar{w}) = \hbar\omega_B \psi_0 (w,\bar{w})

which is the statement that they lie in the lowest Landau level with n = 0. We can further distinguish these states by requiring that they are also eigenvalues of L_z. These are satisfied by the monomials, \psi_0 = w^M e^{-|w|^2 / 4l_B^2} \implies L_z \psi_0 = \hbar M \psi_0 \tag{1.20} for some positive integer M.

Degeneracy Revisited In symmetric gauge, the profiles of the wavefunctions (1.20) form concentric rings around the origin. The higher the angular momentum M, the further out they are localised. The key point is that the wavefunctions are all holomorphic in the coordinate w, and the only singularity comes from the Gaussian factor. As we will see in the next section, the choice of symmetric gauge is particularly useful when we want to describe quantum Hall droplets.

the ring.

This, of course, is very different from the strip-like wavefunctions that we saw in Landau gauge (1.15). You shouldn't read too much into this other than the fact that the profile of the wavefunctions is not telling us anything physical as it is not gauge invariant.

However, it's worth revisiting the degeneracy of states in symmetric gauge. The probability for a particle with angular momentum M is peaked on a ring of radius r = 2Ml. This means that in a disc shaped region of area A = πR^2, the number of states is roughly (the integer part of)

N ≈ qBA / (2πℏ) = A / (2πl^2) = BA / B (2πℏ)

which agrees with our earlier result (1.17).

1.2.3 An Invitation to the Quantum Hall Effect Take a system with some fixed number of electrons, which are restricted to move in the (x,y)-plane. The charge of the electron is q = −e. In the presence of a magnetic field, these will first fill up the N = eBA/2πℏ states in the n = 0 lowest Landau level. If any are left over they will then start to fill up the n = 1 Landau level, and so on.

Now suppose that we increase the magnetic field B. The number of states N housed in each Landau level will increase, leading to a depletion of the higher Landau levels. At certain, very special values of B, we will find some number of Landau levels that are exactly filled. However, generically there will be a highest Landau level which is only partially filled.

This successive depletion of Landau levels gives rise to a number of striking signatures in different physical quantities. Often these quantities oscillate, or jump discontinuously as the number of occupied Landau levels varies. One particular example is the de Haas van Alphen oscillations seen in the magnetic susceptibility which we describe in Section 3.3.4. Another example is the behaviour of the resistivity ρ. This relates the current density J = (J_x, J_y) to the applied electric field E = (E_x, E_y), E = ρJ In the presence of an applied magnetic field B = (0,0,B), the electrons move in circles. This results in components of the current which are both parallel and perpendicular to the electric field. This is modelled straightforwardly by taking ρ to be a matrix ρ = ( ρ_xx   ρ_xy )

( -ρ_xy  ρ_xx )

where the form of the matrix follows from rotational invariance. Here ρ_xx is called the longitudinal resistivity while ρ_xy is called the Hall resistivity.

In very clean samples, in strong magnetic fields, both components of the resistivity exhibit very surprising behaviour. This is shown in the left-hand figure above. The Hall resistivity ρ_xy increases with B by forming a series of plateaux, on which it takes values ρ_xy = (h/e^2) * (1/ν) where ν ∈ ℕ The value of ν (which is labelled i = 2,3,... in the data shown above) is measured to be an integer to extraordinary accuracy — around one part in 10^9. Meanwhile, the longitudinal resistivity vanishes when ρ_xy lies on a plateaux, but spikes whenever there is a transition between different plateaux. This phenomenon, called the integer Quantum Hall Effect, was discovered by Klaus von Klitzing in 1980. For this, he was awarded the Nobel prize in 1985.

It turns out that the integer quantum Hall effect is a direct consequence of the existence of discrete Landau levels. The plateaux occur when precisely ν ∈ ℤ^+ Landau levels are filled. Of course, we're very used to seeing integers arising in quantum mechanics — this, after all, is what the "quantum" in quantum mechanics means. However, the quantisation of the resistivity ρ_xy is something of a surprise because this is a macroscopic quantity, involving the collective behaviour of many trillions of electrons, swarming through a hot and dirty system. A full understanding of the integer quantum Hall effect requires an appreciation of how the mathematics of topology fits in with quantum mechanics. David Thouless (and, to some extent, Duncan Haldane) were awarded the 2016 Nobel prize for understanding the underlying role of topology in this system.

Subsequently it was realised that similar behaviour also happens when Landau levels are partially filled. However, it doesn't occur for any filling, but only very special values. This is referred to as the fractional quantum Hall effect. The data is shown in the right-hand figure. You can see clear plateaux when the lowest Landau level has ν = 1/3 of its states filled. There is another plateaux when ν = 2/5 of the states are filled, followed by a bewildering pattern of further plateaux, all of which occur when ν is some rational number. This was discovered by Tsui and Störmer in 1982. It called the Fractional Quantum Hall Effect. The 1998 Nobel prize was awarded to Tsui and Stormer, together with Laughlin who pioneered the first theoretical ideas to explain this behaviour.

The fractional quantum Hall effect cannot be explained by treating the electrons as free. Instead, it requires us to take interactions into account. We have seen that each Landau level has a macroscopically large degeneracy. This degeneracy is lifted by interactions, resulting in a new form of quantum liquid which exhibits some magical properties. For example, in this state of matter the electron — which, of course, is an indivisible particle — can split into constituent parts! The ν = 1 state has excitations which carry 1/3 of the charge of an electron. In other quantum Hall states, the excitations have charge 1/5 or 1/4 of the electron. These particles also have a number of other, even stranger properties to do with their quantum statistics and there is hope that these may underly the construction of a quantum computer.

We will not delve into any further details of the quantum Hall effect. Suffice to say that it is one of the richest and most beautiful subjects in theoretical physics. You can find a fuller exploration of these ideas in the lecture notes devoted to the Quantum Hall Effect.

## 1.3 The Aharonov-Bohm Effect

In our course on Electromagnetism, we learned that the gauge potential A is unphysical: the physical quantities that affect the motion of a particle are the electric and magnetic fields. Yet we’ve seen above that we cannot formulate quantum mechanics without introducing the gauge fields A and ϕ. This might lead us to wonder whether there is more to life than E and B alone. In this section we will see that things are, indeed, somewhat more subtle.

1.3.1 Particles Moving around a Flux Tube

Consider the set-up shown in the figure. We have a solenoid of area A, carrying magnetic field B = (0,0,B) and therefore magnetic flux Φ = BA. Outside the solenoid the magnetic field is zero. However, the vector potential is not. This follows from Stokes’ theorem which tells us that the line integral outside the solenoid is given by

∮ A·dx = ∫ B·dS = Φ

This is simply solved in cylindrical polar coordinates by A = Φ / (2πr).

Now consider a charged quantum particle restricted to lie in a ring of radius r outside the solenoid. The only dynamical degree of freedom is the angular coordinate ϕ ∈ [0,2π). The Hamiltonian is

H = (1/2m)(p - qA_ϕ)² = -ℏ² (∂_ϕ - i qΦ/(2πℏ))² / (2mr²)

We’d like to see how the presence of this solenoid affects the particle. The energy eigenstates are simply

ψ = e^{inϕ} / √(2πr), n ∈ Z (1.21)

where the requirement that ψ is single valued around the circle means that we must take n ∈ Z. Plugging this into the time independent Schrödinger equation Hψ = Eψ, we find the spectrum

E = (ℏ²/(2mr²)) (n - qΦ/(2πℏ))² = (ℏ²/(2mr²)) (n - Φ/Φ₀)², n ∈ Z

where we’ve defined the quantum of flux Φ₀ = 2πℏ/q. (Usually this quantum of flux is defined using the electron charge q = -e, with the minus signs massaged so that Φ₀ ≡ 2πℏ/e > 0.)

Note that if Φ is an integer multiple of Φ₀, then the spectrum is unaffected by the solenoid. But if the flux in the solenoid is not an integral multiple of Φ₀ — and there is no reason that it should be — then the spectrum gets shifted. We see that the energy of the particle knows about the flux Φ even though the particle never goes near the region with magnetic field. The resulting energy spectrum is shown in Figure 6.

There is a slightly different way of looking at this result. Away from the solenoid, the gauge field is a total divergence

A = ∇α with α = Φϕ/(2π)

This means that we can try to remove it by redefining the wavefunction to be

ψ → ψ' = exp(-iqα/ℏ) ψ = exp(-iqΦ ϕ/(2πℏ)) ψ

However, there is an issue: the wavefunction should be single-valued. This, after all, is how we got the quantisation condition n ∈ Z in (1.21). This means that the gauge transformation above is allowed only if Φ is an integer multiple of Φ₀ = 2πℏ/q. Only in this case is the particle unaffected by the solenoid. The obstacle arises from the fact that the wavefunction of the particle winds around the solenoid. We see here the first glimpses of how topology starts to feed into quantum mechanics.

There are a number of further lessons lurking in this simple quantum mechanical set-up. You can read about them in the lectures on the Quantum Hall Effect (see Section 1.5.3) and the lectures on Gauge Theory (see Section 3.6.1).

1.3.2 Aharonov-Bohm Scattering

The fact that a quantum particle can be affected by A even when restricted to regions where B = 0 was first pointed out by Aharonov a and Bohm in a context which is closely related to the story above. They revisited the famous double-slit experiment, but now with a twist: a solenoid carrying flux Φ is hidden behind the wall. This set-up is shown in the figure below. Once again, the particle is forbidden from going near the solenoid.

Nonetheless, the presence of the magnetic flux affects the resulting interference pattern, shown as the dotted line in the figure. Consider a particle that obeys the free Schrödinger equation,

$$ -i\hbar\nabla - q\mathbf{A} \psi = E\psi $$

We can formally remove the gauge field by writing

$$ \psi(\mathbf{x}) = \exp\left( \frac{iq}{\hbar} \int \mathbf{A}(\mathbf{x}') \cdot d\mathbf{x}' \right) \phi(\mathbf{x}) $$

where the integral is over any path. Crucially, however, in the double-slit experiment there are two paths, $P_1$ and $P_2$. The phase picked up by the particle due to the gauge field differs depending on which path is taken. The phase difference is given by

$$ \Delta\theta = \frac{q}{\hbar} \int_{P_1} \mathbf{A} \cdot d\mathbf{x} - \frac{q}{\hbar} \int_{P_2} \mathbf{A} \cdot d\mathbf{x} = \frac{q}{\hbar} \oint \mathbf{A} \cdot d\mathbf{x} = \frac{q}{\hbar} \int \mathbf{B} \cdot d\mathbf{S} $$

Note that neither the phase arising from path $P_1$, nor the phase arising from path $P_2$, is gauge invariant. However, the difference between the two phases is gauge invariant. As we see above, it is given by the flux through the solenoid. This is the Aharonov-Bohm phase, $e^{iq\Phi/\hbar}$, an extra contribution that arises when charged particles move around magnetic fields.

The Aharonov-Bohm phase manifests in the interference pattern seen on the screen. As Φ is changed, the interference pattern shifts, an effect which has been experimentally observed. Only when Φ is an integer multiple of Φ is the particle unaware of the presence of the solenoid.

## 1.4 Magnetic Monopoles

A magnetic monopole is a hypothetical object which emits a radial magnetic field of the form

$$ \mathbf{B} = \frac{g \hat{\mathbf{r}}}{4\pi r^2} \implies \int d\mathbf{S} \cdot \mathbf{B} = g \quad (1.22) $$

Here $g$ is called the magnetic charge.

We learned in our first course on Electromagnetism that magnetic monopoles don’t exist. First, and most importantly, they have never been observed. Second, there’s a law of physics which insists that they can’t exist. This is the Maxwell equation

$$ \nabla \cdot \mathbf{B} = 0 $$

Third, this particular Maxwell equation would appear to be non-negotiable. This is because it follows from the definition of the magnetic field in terms of the gauge field

$$ \mathbf{B} = \nabla \times \mathbf{A} \implies \nabla \cdot \mathbf{B} = 0 $$

Moreover, as we’ve seen above, the gauge field $\mathbf{A}$ is necessary to describe the quantum physics of particles moving in magnetic fields. Indeed, the Aharonov-Bohm effect tells us that there is non-local information stored in $\mathbf{A}$ that can only be detected by particles undergoing closed loops. All of this points to the fact that we would be wasting our time discussing magnetic monopoles any further.

Happily, there is a glorious loophole in all of these arguments, first discovered by Dirac, and magnetic monopoles play a crucial role in our understanding of the more subtle effects in gauge theories. The essence of this loophole is that there is an ambiguity in how we define the gauge potentials. In this section, we will see how this arises.

1.4.1 Dirac Quantisation It turns out that not any magnetic charge $g$ is compatible with quantum mechanics. Here we present several different arguments for the allowed values of $g$.

We start with the simplest and most physical of these arguments. Suppose that a particle with charge $q$ moves along some closed path $C$ in the background of some gauge potential $\mathbf{A}(\mathbf{x})$. Then, upon returning to its initial starting position, the wavefunction of the particle picks up a phase

$$ \psi \rightarrow e^{iq\alpha/\hbar} \psi \quad \text{with} \quad \alpha = \oint_C \mathbf{A} \cdot d\mathbf{x} \quad (1.23) $$

This is the Aharonov-Bohm phase described above.

The phase of the wavefunction is not an observable quantity in quantum mechanics. However, as we described above, the phase in (1.23) is really a phase difference. We could, for example, place a particle in a superposition of two states, one of which stays still while the other travels around the loop $C$. The subsequent interference will depend on the phase $e^{iq\alpha/\hbar}$, just like in the Aharonov-Bohm effect.

Let’s now see what this has to do with magnetic monopoles. We place our particle, with electric charge $q$, in the background of a magnetic monopole with magnetic charge $g$. We keep the magnetic monopole fixed, and let the electric particle undergo some journey along a path $C$. We will ask only that the path $C$ avoids the origin where the magnetic monopole is sitting. This is shown in the left-hand panel of the figure. Upon returning, the particle picks up a phase $e^{iq\alpha/\hbar}$ with

$$ \alpha = \oint_C \mathbf{A} \cdot d\mathbf{x} = \int_S \mathbf{B} \cdot d\mathbf{S} $$

where, as shown in the figure, $S$ is the area enclosed by $C$. Using the fact that $\int_{S^2} \mathbf{B} \cdot d\mathbf{S} = g$, if the surface $S$ makes a solid angle $\Omega$, this phase can be written as

$$ \alpha = \frac{\Omega g}{4\pi} $$

However, there’s an ambiguity in this computation. Instead of integrating over $S$, it is equally valid to calculate the phase by integrating over $S'$, shown in the right-hand panel of the figure. The solid angle formed by $S'$ is $\Omega' = 4\pi - \Omega$. The phase is then given by

$$ \alpha' = \frac{(4\pi - \Omega) g}{4\pi} $$ where the overall minus sign comes because the surface S′ has the opposite orientation to S. As we mentioned above, the phase shift that we get in these calculations is observable: we can’t tolerate different answers from different calculations. This means that we must have eiqα/ℏ = eiqα′/ℏ. This gives the condition qg = 2πℏn with n ∈ Z (1.24)

This is the famous Dirac quantisation condition. The smallest such magnetic charge has n = 1. It coincides with the quantum of flux, g = Φ = 2πℏ/q.

Above we worked with a single particle of charge q. Obviously, the same argument must hold for any other particle of charge q′. There are two possibilities. The first is that all particles carry charge that is an integer multiple of some smallest unit. In this case, it’s sufficient to impose the Dirac quantisation condition (1.24) where q is the smallest unit of charge. For example, in our world we should take q = ±e to be the electron or proton charge (or, if we look more closely in the Standard Model, we might choose to take q = −e/3, the charge of the down quark).

The second possibility is that the particles carry electric charges which are irrational multiples of each other. For example, there may be a particle with charge q and another particle with charge 2q. In this case, no magnetic monopoles are allowed. It’s sometimes said that the existence of a magnetic monopole would imply the quantisation of electric charges. This, however, has it backwards. (It also misses the point that we have a wonderful explanation of the quantisation of charges from the story of anomaly cancellation in the Standard Model.) There are two possible groups that could underly gauge transformations in electromagnetism. The first is U(1); this has integer valued charges and admits magnetic monopoles. The second possibility is R; this has irrational electric charges and forbids monopoles. All the evidence in our world points to the fact that electromagnetism is governed by U(1) and that magnetic monopoles should exist.

Above we looked at an electrically charged particle moving in the background of a magnetically charged particle. It is simple to generalise the discussion to particles that carry both electric and magnetic charges. These are called dyons. For two dyons, with charges (q₁, g₁) and (q₂, g₂), the generalisation of the Dirac quantisation condition requires q₁g₂ − q₂g₁ ∈ 2πℏZ This is sometimes called the Dirac-Zwanziger condition.

1.4.2 A Patchwork of Gauge Fields

The discussion above shows how quantum mechanics constrains the allowed values of magnetic charge. It did not, however, address the main obstacle to constructing a magnetic monopole out of gauge fields A when the condition B = ∇×A would seem to explicitly forbid such objects.

Let’s see how to do this. Our goal is to write down a configuration of gauge fields which give rise to the magnetic field (1.22) of a monopole which we will place at the origin. However, we will need to be careful about what we want such a gauge field to look like. The first point is that we won’t insist that the gauge field is well defined at the origin. After all, the gauge fields arising from an electron are not well defined at the position of an electron and it would be churlish to require more from a monopole. This fact gives us our first bit of leeway, because now we need to write down gauge fields on ℝ³\{0}, as opposed to ℝ³ and the space with a point cut out enjoys some non-trivial topology that we will make use of.

Consider the following gauge connection, written in spherical polar coordinates A_ϕ^N = (g/4πr) (1−cosθ)/sinθ (1.25)

The resulting magnetic field is B = ∇×A = (1/(r sinθ)) ∂_θ(A^N_ϕ sinθ) r̂ − (1/r) ∂_r(r A^N_ϕ) θ̂ Substituting in (1.25) gives B = (g/4πr²) r̂ (1.26)

In other words, this gauge field results in the magnetic monopole. But how is this possible? Didn’t we learn in kindergarten that if we can write B = ∇ × A then ∫ dS·B = 0? How does the gauge potential (1.25) manage to avoid this conclusion? The answer is that A^N_ϕ in (1.25) is actually a singular gauge connection. It’s not just singular at the origin, where we’ve agreed this is allowed, but it is singular along an entire half-line that extends from the origin to infinity. This is due to the 1/sinθ term which diverges at θ = 0 and θ = π. However, the numerator 1−cosθ has a zero when θ = 0 and the gauge connection is fine there. But the singularity along the half-line θ = π remains. The upshot is that this gauge connection is not acceptable along the line of the south pole, but is fine elsewhere. This is what the superscript N is there to remind us: we can work with this gauge connection as long as we keep north.

Now consider a different gauge connection A_ϕ^S = − (g/4πr) (1+cosθ)/sinθ (1.27)

This again gives rise to the magnetic field (1.26). This time it is well behaved at θ = π, but singular at the north pole θ = 0. The superscript S is there to remind us that this connection is fine as long As we keep south. At this point, we make use of the ambiguity in the gauge connection. We are going to take AN in the northern hemisphere and AS in the southern hemisphere. This is allowed because the two gauge potentials are the same up to a gauge transformation, A → A + ∇α. Recalling the expression for ∇α in spherical polars, we find that for θ ≠ 0,π, we can indeed relate AN and AS by a gauge transformation, AN = AS + ∂ϕ α where α = (gϕ)/(2πr sinθ). (1.28) However, there’s still a question remaining: is this gauge transformation allowed? The problem is that the function α is not single valued: α(ϕ = 2π) = α(ϕ = 0) + g. And this should concern us because, as we’ve seen in (1.8), the gauge transformation also acts on the wavefunction of a quantum particle ψ → e^{iqα/ℏ}. There’s no reason that we should require the gauge transformation α to be single-valued, but we do want the wavefunction ψ to be single-valued. This holds for the gauge transformation (1.28) provided that we have qg = 2πℏn with n ∈ Z. This, of course, is the Dirac quantisation condition (1.24). Mathematically, we have constructed a topologically non-trivial U(1) bundle over the S2 surrounding the origin. In this context, the integer n is called the first Chern number.

1.4.3 Monopoles and Angular Momentum

Here we provide yet another derivation of the Dirac quantisation condition, this time due to Saha. The key idea is that the quantisation of magnetic charge actually follows from the more familiar quantisation of angular momentum. The twist is that, in the presence of a magnetic monopole, angular momentum isn’t quite what you thought. To set the scene, let’s go back to the Lorentz force law dp/dt = qẋ × B, with p = mẋ. Recall from our discussion in Section 1.1.1 that p defined here is not the canonical momentum, a fact which is hiding in the background in the following derivation. Now let’s consider this equation in the presence of a magnetic monopole, with B = (g/4π)(r̂/r²). The monopole has rotational symmetry so we would expect that the angular momentum, x × p, is conserved. Let’s check: d(x × p)/dt = ẋ × p + x × ṗ = x × (qẋ × B) = (qg/4πr³) x × (ẋ × x) = −(qg/4π) (d/dt)(r̂). We see that in the presence of a magnetic monopole, the naive angular momentum x × p is not conserved! However, as we also noticed in the lectures on Classical Dynamics (see Section 4.3.2), we can easily write down a modified angular momentum that is conserved, namely L = x × p − (qg/4π) r̂. The extra term can be thought of as the angular momentum stored in E×B. The surprise is that the system has angular momentum even when the particle doesn’t move. Before we move on, there’s a nice and quick corollary that we can draw from this. The angular momentum vector L does not change with time. But the angle that the particle makes with this vector is L·r̂ = −qg/(4π) = constant. This means that the particle moves on a cone, with axis L and angle cosθ = −qg/(4πL). So far, our discussion has been classical. Now we invoke some simple quantum mechanics: the angular momentum should be quantised. In particular, the angular momentum in the z-direction should be Lz ∈ (1/2)ℏZ. Using the result above, we have qg/(4π) = (1/2)ℏn ⇒ qg = 2πℏn with n ∈ Z. Once again, we find the Dirac quantisation condition.

## 1.5 Spin in a Magnetic Field

As we’ve seen in previous courses, particles often carry an intrinsic angular momentum called spin S. This spin is quantised in half-integer units. For example, electrons have spin 1/2 and their spin operator is written in terms of the Pauli matrices σ, S = (ℏ/2)σ. Importantly, the spin of any particle couples to a background magnetic field B. The key idea here is that the intrinsic spin acts like a magnetic moment m which couples to the magnetic field through the Hamiltonian H = −m·B. The question we would like to answer is: what magnetic moment m should we associate with spin? A full answer to this question would require an extended detour into the Dirac equation. Here we provide only some basic motivation. First consider a particle of charge q moving with velocity v around a circle of radius r as shown in the figure. From our lectures on Electromagnetism, we know that the associated magnetic moment is given by m = (q/2)r × v = (q/2m)L, where L = mr × v is the orbital angular momentum of the particle. Indeed, we already saw the resulting coupling H = −(q/2m)L·B in our derivation of the Hamiltonian in symmetric gauge (1.19). Since the spin of a particle is another contribution to the angular momentum, we might anticipate that the associated magnetic moment takes the form m = g(q/2m)S, where g is some dimensionless number. (Note: g is unrelated to the magnetic charge that we discussed in the previous section!) This, it turns out, is the right answer. However, the value of g depends on the particle under consideration. The upshot is that we should include a term in the Hamiltonian of the form H = − g-factor

For fundamental particles with spin 1/2 — such as the electron — there is a long and interesting history associated to determining the value of g. For the electron, this was first measured experimentally to be g ≈ 2. Soon afterwards, Dirac wrote down his famous relativistic equation for the electron. One of its first successes was the theoretical prediction g = 2 for any spin 1/2 particle. This means, for example, that the neutrinos and quarks also have g = 2.

This, however, was not the end of the story. With the development of quantum field theory, it was realised that there are corrections to the value g = 2. These can be calculated and take the form of a series expansion, starting with g = 2 (1 + α/2π + ...) ≈ 2.00232, where α = e²/4πϵ ℏc ≈ 1/137 is the dimensionless fine structure constant which characterises the strength of the Coulomb force. The most accurate experimental measurement of the electron magnetic moment now yields the result g ≈ 2.00231930436182 ± 2.6 × 10⁻¹³. Theoretical calculations agree to the first ten significant figures or so. This is the most impressive agreement between theory and experiment in all of science! Beyond that, the value of α is not known accurately enough to make a comparison. Indeed, now the measurement of the electron magnetic moment is used to define the fine structure constant α.

While all fundamental spin 1/2 particles have g ≈ 2, this does not hold for more complicated objects. For example, the proton has g ≈ 5.588, while the neutron — which of course, is a neutral particle, but still carries a magnetic moment — has g ≈ −3.823, where, because the neutron is neutral, the charge q = 0 is used in the formula (1.29). These measurements were one of the early hints that the proton and neutron are composite objects.

1.5.1 Spin Precession Consider a constant magnetic field B = (0,0,B). We would like to understand how this affects the spin of an electron. We’ll take g = 2. We write the electric charge of the electron as q = −e so the Hamiltonian is H = eℏ/2m σ ·B. The eigenstates are simply the spin-up |↑⟩ and spin-down |↓⟩ states in the z-direction. They have energies H|↑⟩ = ℏω_B/2 |↑⟩ and H|↓⟩ = −ℏω_B/2 |↓⟩, where ω_B = eB/m is the cyclotron frequency which appears throughout this chapter.

What happens if we do not sit in an energy eigenstate? A general spin state can be expressed in spherical polar coordinates as |ψ(θ,ϕ)⟩ = cos(θ/2)|↑⟩ + e^(iϕ)sin(θ/2)|↓⟩. As a check, note that |ψ(θ = π/2,ϕ)⟩ is an eigenstate of σ_x when ϕ = 0,π and an eigenstate of σ_y when ϕ = π/2,3π/2 as it should be. The evolution of this state is determined by the time-dependent Schrödinger equation iℏ ∂|ψ⟩/∂t = H|ψ⟩, which is easily solved to give |ψ(θ,ϕ;t)⟩ = e^(-iω_B t/2) [cos(θ/2)|↑⟩ + e^(i(ϕ+ω_B t)) sin(θ/2)|↓⟩]. We see that the effect of the magnetic field is to cause the spin to precess about the B axis, as shown in the figure.

1.5.2 A First Look at the Zeeman Effect The Zeeman effect describes the splitting of atomic energy levels in the presence of a magnetic field. Consider, for example, the hydrogen atom with Hamiltonian H = −ℏ²/2m ∇² − e²/4πϵ r. The energy levels are given by E_n = −α²mc²/(2n²), n ∈ ℤ, where α is the fine structure constant. Each energy level has a degeneracy of states. These are labelled by the angular momentum l = 0,1,...,n−1 and the z-component of angular momentum m_l = −l,...,+l. Furthermore, each electron carries one of two spin states labelled by m_s = ±1/2. This results in a degeneracy given by Degeneracy = Σ_{l=0}^{n-1} 2(2l+1) = 2n².

Now we add a magnetic field B = (0,0,B). As we have seen, this results in a perturbation to the Hamiltonian which, to leading order in B, is given by ∆H = (L + g S)·B/2m. In the presence of such a magnetic field, the degeneracy of the states is split. The energy levels now depend on the quantum numbers n, m_l and m_s and are given by E_{n,m_l,m_s} = E_n + (m_l + 2m_s) eB/2m. The Zeeman effect is developed further in the Lectures on Topics in Quantum Mechanics.

## 2. Band Structure

In this chapter, we start our journey into the world of condensed matter physics. This is the study of the properties of “stuff”. Here, our interest lies in a particular and familiar kind of stuff: solids. Solids are collections of tightly bound atoms. For most solids, these atoms arrange themselves in regular patterns on an underlying crystalline lattice. Some of the electrons of the atom then disassociate themselves from their parent atom and wander through the lattice environment. The properties of these electrons determine many of the properties of the solid, not least its ability to conduct electricity. One might imagine that the electrons in a solid move in a fairly random fashion, as they bounce from one lattice site to another, like a ball in a pinball machine. However, as we will see, this is not at all the case: the more fluid nature of quantum particles allows them to glide through a regular lattice, almost unimpeded.

impeded, with a distorted energy spectrum the only memory of the underlying lattice.

In this chapter, we will focus on understanding how the energy of an electron depends on its momentum when it moves in a lattice environment. The usual formula for kinetic energy, E = 1/2 mv^2 = p^2/2m, is one of the first things we learn in theoretical physics as children. As we will see, a lattice changes this in interesting ways, the consequences of which we will explore in chapter 3.

## 2.1 Electrons Moving in One Dimension

We begin with some particularly simple toy models which capture much of the relevant physics. These toy models describe an electron moving in a one-dimensional lattice. We’ll take what lessons we can from this before moving onto more realistic descriptions of electrons moving in higher dimensions.

2.1.1 The Tight-Binding Model

The tight-binding model is a caricature of electron motion in solid in which space is made discrete. The electron can sit only on the locations of atoms in the solid and has some small probability to hop to a neighbouring site due to quantum tunnelling.

To start with our “solid” consists of a one-dimensional lattice of atoms. This is described by N points arranged along a line, each separated by distance a.

Consider a single electron moving on this lattice. We will assume that the electron can only sit on a given lattice point; it’s not allowed to roam between lattice points. This is supposed to mimic the idea that electrons are bound to the atoms in a lattice and goes by the name of the tight-binding approximation. (We’ll see exactly what we’re neglecting in this approximation later.)

When the electron sits on the nth atom, we denote the quantum state as |n⟩. These states are considered orthogonal to each other, so ⟨n|m⟩ = δ_nm. Clearly the total Hilbert space has dimension N, and is spanned by |n⟩ with n = 1,...,N.

What kind of Hamiltonian will govern the dynamics of this electron? If the electron just remains on a given atom, an appropriate Hamiltonian would be H = E_0 ∑_n |n⟩⟨n|. Each of the position states |n⟩ is an energy eigenstate of H with energy E_0. The electrons governed by this Hamiltonian don’t move. This Hamiltonian is boring.

To make things more interesting, we need to include the possibility that the electron can tunnel from one site to another. How to do this? Well, the Hamiltonian governs time evolution. In some small time increment of time ∆t, a state evolves as |ψ⟩ → |ψ⟩− i∆t H|ψ⟩+O(∆t^2). This means that if we want the possibility for the electron to hop from one site to another, we should include in the Hamiltonian a term of the form |m⟩⟨n| which takes an electron at site n and moves it to an electron at site m.

There is one last ingredient that we want to feed into our model: locality. We don’t want electrons to disappear and reappear many thousands of lattice spacings down the line. We want our model to describe electrons hopping from one atom to neighbouring atoms. This motivates our final form of the Hamiltonian, H = E_0 ∑_n |n⟩⟨n| − t ∑_n (|n⟩⟨n+1| + |n+1⟩⟨n|) (2.1)

First a comment on notation: the parameter t is called the hopping parameter. It is not time; it is simply a number which determines the probability that a particle will hop to a neighbouring site. (More precisely, the ratio t^2/E_0^2 will determine the probability of hopping.) It’s annoying notation, but unfortunately t is the canonical name for this hopping parameter so it’s best we get used to it now.

Now back to the physics encoded in H. We’ve chosen a Hamiltonian that only includes hopping terms between neighbouring sites. This is the simplest choice; we will describe more general choices later. Moreover, the probability of hopping to the left is the same as the probability of hopping to the right. This is required because H must be a Hermitian operator.

There’s one final issue that we have to address before solving for the spectrum of H: what happens at the edges? Again, there are a number of different possibilities but none of the choices affect the physics that we’re interested in here. The simplest option is simply to declare that the lattice is periodic. This is best achieved by introducing a new state |N +1⟩, which sits to the right of |N⟩, and is identified with |N +1⟩ ≡ |1⟩.

Solving the Tight-Binding Model

Let’s now solve for the energy eigenstates of the Hamiltonian (2.1). A general state can be expanded as |ψ⟩ = ∑_m ψ_m |m⟩, with ψ ∈ C. Substituting this into the Schrödinger equation gives H|ψ⟩ = E|ψ⟩ ⇒ E_0 ∑_m ψ_m |m⟩ − t ∑_m (ψ_m |m⟩ + ψ_m |m+1⟩) = E ∑_m ψ_m |m⟩.

If we now take the overlap with a given state ⟨n|, we get the set of linear equations for the coefficients ψ_n: ⟨n|H|ψ⟩ = E⟨n|ψ⟩ ⇒ E_0 ψ_n − t(ψ_n+1 + ψ_n−1) = E ψ_n (2.2)

These kind of equations arise fairly often in physics. (Indeed, they will arise again in Section 4 when we come to discuss the vibrations of a lattice.) They are solved by the ansatz ψ_n = e ikna (2.3)

Or, if we want to ensure that the wavefunction is normalised, ψ = eikna/ N. The exponent k is called the wavenumber. The quantity p = ℏk plays a role similar to momentum in our discrete model; we will discuss the ways in which it is like momentum in Section 2.1.4. We’ll also often be lazy and refer to k as momentum.

The wavenumber has a number of properties. First, the set of solutions remain the same if we shift k → k +2π/a so the wavenumber takes values in k ∈ (−π/a, +π/a) (2.4)

This range of k is given the fancy name Brillouin zone. We’ll see why this is a useful concept that deserves its own name in Section 2.2.

There is also a condition on the allowed values of k coming from the requirement of periodicity. We want ψN+1 = ψ1, which means that eikNa = 1. This requires that k is quantised in units of 2π/aN. In other words, within the Brillouin zone (2.4) there are exactly N quantum states of the form (2.3). But that’s what we expect as it’s the dimension of our Hilbert space; the states (2.3) form a different basis.

States of the form (2.3) have the property that ψn±1 = e±ika ψn This immediately ensures that equation (2.2) is solved for any value of k, with the energy eigenvalue E(k) = E0 −2tcos(ka) (2.5)

Figure 13: The spectrum is shown in the figure for t > 0. (The plot was made with a = t = 1 and E0 = 2.) The states with k > 0 describe electrons which move to the right; those with k < 0 describe electrons moving to the left.

There is a wealth of physics hiding in this simple result, and much of the following sections will be fleshing out these ideas. Here we highlight a few pertinent points • The electrons do not like to sit still. The eigenstates |n⟩ of the original Hamiltonian H were localised in space. One might naively think that adding a tiny hopping parameter t would result in eigenstates that were spread over a few sites. But this is wrong. Instead, all energy eigenstates are spread throughout the whole lattice. Arbitrarily small local interactions result in completely delocalised energy eigenstates.

• The energy eigenstates of H were completely degenerate. Adding the hopping term lifts this degeneracy. Instead, the eigenstates are labelled by the wavevector k and have energies (2.5) that lie in a range E(k) ∈ [E0 − 2t, E0 + 2t]. This range of energies is referred to a band and the difference between the maximum and minimum energy (which is 4t in this case) is called the band width. In our simple model, we have just a single energy band. In subsequent models, we will see multiple bands emerging.

• For suitably small momentum, k ≪ π/a, we can Taylor expand the energy (2.5) as E(k) ≈ (E0 −2t)+ta2k2 Up to a constant, this takes the same form as a free particle moving in the continuum, E_free = ℏ2k2 / 2m (2.6)

This is telling us that low energy, low momentum particles are unaware that they are moving on an underlying lattice. Instead, they act as if they are moving along a continuous line with effective mass m⋆ = ℏ2/2ta2. Notice that in this model the effective mass has nothing to do with the physical mass of the electron; it is inherited from properties of the lattice.

• There is a cute reciprocity between the properties of momentum and position. We know from our first course on quantum mechanics that if space is made finite — for example, a particle in a box, or a particle moving on a circle — then momentum becomes discrete. We also saw this above as the periodic boundary conditions enforced the wavenumber to be quantised in units of 2π/Na. However, our tight-binding model also exhibits the converse phenomenon: when we make space discrete, momentum becomes periodic: it has to lie in the Brillouin zone (2.4). More generally, discreteness is the Fourier transform of compactness.

A First Look at Metals and Insulators There’s further physics to uncover if we consider more than one electron moving in the lattice. This section is just to give a flavour of these ideas; we will discuss them in more detail in Section 3.1. For simplicity, we will assume that the electrons do not interact with each other. Now the state of the system is governed by the Pauli exclusion principle: two electrons are not allowed to occupy the same state.

As we have seen, our tight-binding model contains N states. However, each electron has two internal states, spin |↑⟩ and spin |↓⟩. This means that, in total, each electron can be in one of 2N different states. Invoking the Pauli exclusion principle, we see that our tight-binding model makes sense as long as the number of electrons is less than or equal to 2N.

The Pauli exclusion principle means that the ground state of a multi-electron system has interesting properties. The first two electrons that we put in the system can both sit in the lowest energy state with k = 0 as long as they have opposite spins. The next electron that we put in finds these states occupied; it must sit in the next available energy state which has k = ±2π/Na. An and so this continues, with subsequent electrons sitting in the lowest energy states which have not previously been occupied. The net result is that the electrons fill all states up to some final k which is known as the Fermi momentum. The boundary between the occupied and unoccupied states is known as the Fermi surface. Note that it is a surface in momentum space, rather than in real space. We will describe this in more detail in Section 3.1. (See also the lectures on Statistical Physics.)

How many electrons exist in a real material? Here something nice happens, because the electrons which are hopping around the lattice come from the atoms themselves. One sometimes talks about each atom “donating” an electron. Following our chemist friends, these are called valence electrons. Given that our lattice contains N atoms, it’s most natural to talk about the situation where the system contains ZN electrons, with Z an integer. The atom is said to have valency Z.

Suppose Z = 1, so we have N electrons. Then only half of the states are filled and k = π/2a. Note that there are as many electrons moving to the left (with k < 0) as there are electrons moving to the right (k > 0). This is the statement that there is no current in the ground state of the system.

We can now ask: what are the low-energy excitations of the system? We see that there are many: we can take any electron just below the Fermi surface and promote it to an electron just above the Fermi surface at a relatively small cost in energy. This becomes particularly relevant if we perturb the system slightly. For example, we could ask: what happens if we apply an electric field? As we will describe in more detail in 3.1.1, the ground state of the system re-arranges itself at just a small cost of energy: some left-moving states below the Fermi surface become unoccupied, while right-moving states above the Fermi surface become occupied. Now, however, there are more electrons with k > 0 than with k < 0. This results in an electrical current. What we have just described is a conductor.

Let’s contrast this with what happens when we have 2N electrons in the system. Now we don’t get any choice about how to occupy states since all are occupied. Said another way, the multi-particle Hilbert space contains just a single state: the fully filled band. This time, if we perturb with an electric field then the electrons can’t move anywhere, simply because there’s nowhere for them to go: they are locked in place by the Pauli principle. This means that, despite the presence of the electric field, there is no electric current. This is what we call an insulator. (It is sometimes said to be a band insulator to distinguish it from other mechanisms that also lead to insulating behaviour.)

The difference between a conductor and an insulator is one of the most striking characterisations of materials, one that we all learn in high school. The rough sketch above is telling us that this distinction arises due to quantum phenomena: the formation of energy bands and the Pauli exclusion principle. We’ll explore this more in Section 3.1.

2.1.2 Nearly Free Electrons

The tight-binding model is an extreme cartoon of the real physics in which space is discrete; electrons are stuck on atomic sites with a non-vanishing probability to hop to a neighbouring site. In this section we present another cartoon that is designed to capture the opposite extreme.

We will assume that our electron is free to move anywhere along the line, parameterised by the position x. To mimic the underlying lattice, we add a weak, periodic potential V(x). This means that we consider the Hamiltonian H = p²/(2m) + V(x)

where p = −iℏd/dx is the usual momentum operator. The periodicity of the potential means that it satisfies V(x+a) = V(x) (2.7)

For example, the potential could take the form of a sine wave, or a square wave, or it could be an infinite series of delta functions. For much of our discussion we won’t need the exact form of the potential.

To avoid discussing edge effects, it’s again useful to consider the particle moving on a circle S1 of length (circumference) L. This is compatible with the periodicity requirement (2.7) only if L/a = N ∈ Z. The integer N plays the role of the number of atoms in the lattice.

In the absence of the potential, the eigenstates are the familiar plane waves |k⟩, labelled by the momentum p = ℏk. Because we are on a circle, the wavenumber k is quantised in units of 2π/L. The associated wavefunctions are ψₖ(x) = ⟨x|k⟩ = √(1/L) e^(ikx) (2.8)

These states are orthonormal, with ⟨k|k′⟩ = ∫ dx e^(i(k′−k)x) = δ_{k,k′} (2.9)

(Recall that we are living on a circle)

cycle, so the momenta k are discrete and the Kronecker delta is the appropriate thing to put on the right-hand side.) Meanwhile, the energy of a free particle is given by E(k) = ℏ²k² / 2m  (2.10)

Our goal is to understand how the presence of the potential V(x) affects this energy spectrum. To do this, we work perturbatively. However, perturbation theory in the present situation is a little more subtle than usual. Let's see why.

Recall that the first thing we usually do in perturbation theory is decide whether we have non-degenerate or degenerate energy eigenstates. Which do we have in the present case? Well, all states are trivially degenerate because the energy of a free particle moving to the right is the same as the energy of a free particle moving to the left: E(k) = E(-k). But the fact that the two states |k⟩ and |-k⟩ have the same energy does not necessarily mean that we have to use degenerate perturbation theory. This is only true if the perturbation causes the two states to mix.

To see what happens we will need to compute matrix elements ⟨k|V|k'⟩. The key bit of physics is the statement that the potential is periodic (2.7). This ensures that it can be Fourier expanded V(x) = Σ_{n∈ℤ} Vₙ e^{2πinx/a}  with  Vₙ = V*₋ₙ where the Fourier coefficients follow from the inverse transformation Vₙ = (1/a) ∫₀ᵃ dx V(x) e^{-2πinx/a} The matrix elements are then given by ⟨k|V|k'⟩ = (1/a) Σ_{n∈ℤ} Σ_{n∈ℤ} ∫ dx Vₙ e^{i(k' - k + 2πn/a)x} = Σ_{n∈ℤ} Vₙ δ_{k-k', 2πn/a}  (2.11)

We see that we get mixing only when k = k' + 2πn/a for some integer n. In particular, we get mixing between degenerate states |k⟩ and |-k⟩ only when k = πn/a for some n. The first time that this happens is when k = π/a. But we've seen this value of momentum before: it is the edge of the Brillouin zone (2.4). This is the first hint that the tight-binding model and nearly free electron model share some common features.

With this background, let's now try to sketch the basic features of the energy spectrum as a function of k.

Low Momentum: With low momentum |k| ≪ π/a, there is no mixing between states at leading order in perturbation theory (and very little mixing at higher order). In this regime we can use our standard results from non-degenerate perturbation theory. Expanding the energy to second order, we have E(k) = ℏ²k²/2m + ⟨k|V|k⟩ + Σ_{k'≠k} |⟨k|V|k'⟩|² / (E₀(k) - E₀(k')) + ...  (2.12)

From (2.11), we know that the first order correction is ⟨k|V|k⟩ = V₀, and so just gives a constant shift to the energy, independent of k. Meanwhile, the second order term only gets contributions from |k'⟩ = |k + 2πn/a⟩ for some n. When |k| ≪ π/a, these corrections are small. We learn that, for small momenta, the particle moves as if unaffected by the potential. Intuitively, the de Broglie wavelength 2π/k of the particle is much greater than the wavelength a of the potential, and the particle just glides over it unimpeded.

The formula (2.12) holds for low momenta. It also holds for momenta πn/a ≪ k ≪ π(n+1)/a which are far from the special points where mixing occurs. However, the formula knows about its own failings because if we attempt to use it when k = nπ/a for some n, the numerator ⟨k|V|-k⟩ is finite while the denominator becomes zero. Whenever perturbation theory diverges in this manner it's because we're doing something wrong. In this case it's because we should be working with degenerate perturbation theory.

At the Edge of the Brillouin Zone: Let's consider the momentum eigenstates which sit right at the edge of the Brillouin zone, k = π/a, or at integer multiples k = nπ/a.

As we've seen, these are the values which mix due to the potential perturbation and we must work with degenerate perturbation theory.

Let's recall the basics of degenerate perturbation theory. We focus on the subsector of the Hilbert space formed by the two degenerate states, in our case |k⟩ and |k'⟩ = |-k⟩. To leading order in perturbation theory, the new energy eigenstates will be some linear combination of these original states α|k⟩ + β|k'⟩. We would like to figure out what choice of α and β will diagonalise the new Hamiltonian. There will be two such choices since there must, at the end of the day, remain two energy eigenstates. To determine the correct choice of these coefficients, we write the Schrödinger equation, restricted to this subsector, in matrix form ( ⟨k|H|k⟩   ⟨k|H|k'⟩ ) ( α )   ( α )

(             ⟨k'|H|k⟩   ⟨k'|H|k'⟩ ) ( β ) = E ( β )  (2.13)

We've computed the individual matrix elements above: using the fact that the states |k⟩ are orthonormal (2.9), the unperturbed energy (2.10) and the potential matrix elements (2.11), our eigenvalue equation becomes ( E₀(k)+V₀     Vₙ     ) ( α )   ( α )

(        V*ₙ   E₀(k')+V₀ ) ( β ) = E ( β )  (2.14)

where, for the value k = -k' = nπ/a of interest, E₀(k) = E₀(k') = n²ℏ²π²/2ma². It's simple to determine the eigenvalues E of this matrix: they are given by the roots of the quadratic characteristic equation

ℏ² n²π² (E₀(k)+V₀−E)² −|Vₙ|² = 0 ⇒ E = ℏ² n²π² / (2m a²) + V₀ ± |Vₙ| (2.15)

This is important. We see that a gap opens up in the spectrum at the values k = ±nπ/a. The size of the gap is proportional to 2|Vₙ|.

It’s simple to understand what’s going on here. Consider the simple potential V = 2V₀ cos(2πx / a)

which gives rise to a gap only at k = ±π/a. The eigenvectors of the matrix are (α,β) = (1,−1) and (α,β) = (1,1), corresponding to the wavefunctions ψ₊(x) = ⟨x| |k⟩+|−k⟩ ∼ cos(πx / a)

ψ₋(x) = ⟨x| |k⟩−|−k⟩ ∼ sin(πx / a)

The density of electrons is proportional to |ψ|². Plotting these densities on top of the potential, we see that ψ₊ describes electrons that are gathered around the peaks of the potential, while ψ₋ describes electrons gathered around the minima. It is no surprise that the energy of ψ₊ is higher than that of ψ₋.

Close to the Edge of the Brillouin Zone: Now consider an electron with k = +nπ/a + δ for some small δ. As we’ve seen, the potential causes plane wave states to mix only if their wavenumbers differ by some multiple of 2π/a. This means that |k⟩ = |nπ/a+δ⟩ will mix with |k′⟩ = |−nπ/a+δ⟩. These states don’t quite have the same kinetic energy, but they have very nearly the same kinetic energy. And, as we will see, the perturbation due to the potential V will mean that these states still mix strongly.

To see this mixing, we need once again to solve the eigenvalue equation (2.13) or, equivalently, (2.14). The eigenvalues are given by solutions to the quadratic equation (E₀(k)+V₀−E)(E₀(k′)+V₀−E) − |Vₙ|² = 0 (2.16)

The only difference from our previous discussion is that E(k) and E(k′) are now given by E(k) = ℏ² / (2m) (nπ/a + δ)² and E(k′) = ℏ² / (2m) (nπ/a − δ)²

and the quadratic equation (2.16) becomes ( ℏ² / (2m) (nπ/a + δ)² + V₀ − E )( ℏ² / (2m) (nπ/a − δ)² + V₀ − E ) − |Vₙ|² = 0

This equation has two solutions, E = E±, given by E± = ℏ² n²π² / (2m a²) + V₀ ± √( |Vₙ|² + ( ℏ² 2nπδ / (2m a) )² )

We’re ultimately interested in this expression when δ is small, where we anticipate that the effect of mixing will be important. But, as a sanity check, let’s first expand it in the opposite regime, when we’re far from the edge of the Brillouin zone and δ is large compared to the gap Vₙ. In this case, a little bit of algebra shows that the eigenvalues can be written as E± = E₀(nπ/a ± δ) + V₀ ± |Vₙ|² / ( E₀(nπ/a + δ) − E₀(nπ/a − δ) )

But this coincides with the expression that we got from second-order, non-degenerate perturbation theory (2.12). (Or, more precisely, because we have kept just a single mixing term in our discussion above we get just a single term in the sum in (2.12); for some choice of potentials, keeping further terms may be important.)

Our real interest is what happens close to the edge of the Brillouin zone when δ is small compared to the gap Vₙ. In this case we can expand the square-root to give E± ≈ ℏ² n²π² / (2m a²) + V₀ ± |Vₙ| + ℏ² / (2m) ( 1 ± (n²ℏ²π²) / (ma²|Vₙ|) ) δ²

The first collection of terms coincide with the energy at the edge of the Brillouin zone (2.15), as indeed it must. For us, the important new point is in the second term which tells us that as we approach the gaps, the energy is quadratic in the momentum δ.

Band Structure

We now have all we need to sketch the rough form of the energy spectrum E(k). The original quadratic spectrum is deformed with a number of striking features:

• For small momenta, k ≪ π/a, the spectrum remains roughly unchanged.

• The energy spectrum splits into distinct bands, with gaps arising at k = nπ/a with n ∈ Z. The size of these gaps is given by 2|Vₙ|, where Vₙ is the appropriate Fourier mode of the potential.

• The region of momentum space corresponding to the nth energy band is called the nth Brillouin zone. However, we usually call the 1st Brillouin zone simply the Brillouin zone.

• As we approach the edge of a band, the spectrum is quadratic. In particular, dE/dk → 0 at the end of a band.

The relationship E(k) between energy and momentum is usually called the dispersion relation. In the present case, it is best summarised in a figure.

Note that the spectrum within the first Brillouin zone |k| ≤ π/a, looks very similar to what we saw in the tight-binding model. The qualitative differences in the two models arise because the tight-binding model has a finite number of states, all contained in the first Brillouin zone, while the nearly-free electron model has an infinite number of states which continue for |k| > π/a.

2.1.3 The Floquet Matrix

One of the main lessons that we learned above is that there are gaps in the energy spectrum. It’s hard to overstate the importance of these gaps. Indeed, as we saw briefly above, and will describe in more detail in 3.1.1, the gaps are responsible for some of the most 材料最显著的特性之一，是导体与绝缘体之间的区别。由于其扮演的重要角色，我们将在此描述另一种观察能谱中能隙出现的方式，该方式不依赖于微扰理论。考虑一个一般的周期性势能V(x) = V(x + a)。我们关注的是薛定谔方程的解：

-ħ²/(2m) * d²ψ/dx² + V(x)ψ(x) = Eψ(x)  (2.17)

由于这是一个二阶微分方程，我们知道必然存在两个解ψ₁(x)和ψ₂(x)。然而，因为势能是周期性的，ψ₁(x + a)和ψ₂(x + a)也必须是解。因此，这两组解通过某个线性变换相关联：

[ψ₁(x+a)]       [ψ₁(x)]

[        ] = F(E) [        ]  (2.18)

[ψ₂(x+a)]       [ψ₂(x)]

其中F(E)是一个2×2矩阵，正如记号所暗示的，它依赖于解的能量E。它被称为Floquet矩阵，并具有一些优良性质。

– 39 –

**命题：** det(F) = 1。

**证明：** 首先进行一些运算。我们对(2.18)求导得到：

[ψ'₁(x+a)]       [ψ'₁(x)]

[        ] = F(E) [        ]

[ψ'₂(x+a)]       [ψ'₂(x)]

我们可以通过引入2×2矩阵W(x)将其与之前的方程结合起来：

W(x) = [ψ₁(x)  ψ'₁(x)]

[ψ₂(x)  ψ'₂(x)]

它满足矩阵方程：

W(x+a) = F(E)W(x)  (2.19)

考虑det W = ψ₁ψ'₂ - ψ'₁ψ₂。你可能从之前的微分方程课程中认出这是朗斯基行列式。可以简单证明，利用薛定谔方程(2.17)，有(det W)' = 0。这意味着det W与x无关，因此特别地，det W(x + a) = det W(x)。取(2.19)的行列式告诉我们det F = 1，如命题所述。□

**命题：** Tr F 是实数。

**证明：** 我们总是可以选择原始波函数ψ₁(x)和ψ₂(x)对所有x都取实值。（如果它们不是，只需取实部，这也是薛定谔方程的解。）在此选择下，Floquet矩阵本身具有实数元素，因此其迹显然是实数。但迹与我们选择的波函数基无关。任何其他选择都通过一个变换F → AFA⁻¹（其中A是可逆矩阵）相关联，这保持迹不变。因此，即使F(E)的分量是复数，其迹也保持实数。□

为了理解(2.18)解的结构，我们查看F(E)的特征值λ₊和λ₋。当然，它们也依赖于解的能量E。由于det F = 1，它们满足λ₊λ₋ = 1。它们满足特征方程：

λ² - (Tr F(E))λ + 1 = 0

我们得到的解的类型取决于(Tr F(E))² < 4还是(Tr F(E))² > 4。

(Tr F(E))² < 4：在这种情况下，根是复数且大小相等。我们可以写成：

λ₊ = eⁱᵏᵃ 和 λ₋ = e⁻ⁱᵏᵃ

其中k（假设根是不同的）在范围|k| < π/a内。为了理解这对(2.18)的解意味着什么，我们引入F的左特征向量(α₊, β₊)F = λ₊(α₊, β₊)。那么线性组合ψ₊ = α₊ψ₁ + β₊ψ₂满足：

ψ₊(x+a) = eⁱᵏᵃψ₊(x)

ψ₋类似。这些是扩展态，平均来说均匀分布在晶格中。它们对应于能谱中的能带。

(Tr F(E))² > 4：现在特征值的形式为：

λ₁ = eᵘᵃ 和 λ₂ = e⁻ᵘᵃ

对于某个μ。相应的本征态现在满足：

ψ±(x+a) = e±ᵘᵃψ±(x)

这种形式的态是不允许的：当x → +∞或x → -∞时，它们是发散的。能量E的这些值就是能谱中能隙出现的地方。

当F(E) = 4且两个特征值简并（同为+1或同为-1）时，我们需要做更多的工作。这种情况对应于能带边缘。考虑两个特征值都是+1的情况。回想一下，在你关于向量和矩阵的第一门课程中，尝试将这样的2×2矩阵对角化可能导致两种不同的标准形：

PF(E)P⁻¹ = [1 0]  或  PF(E)P⁻¹ = [1 0]

[0 1]                  [1 1]

在前一种情况下，有两个允许的解。在后一种情况下，你可以检查出一个解是允许的，而另一个解随x线性增长。

2.1.4 一维布洛赫定理

在上述两种模型中，我们最终都用动量ℏk来标记状态。值得停下来问一下：我们为什么这么做？我们应该如何理解k？

– 41 –

在讨论这个问题之前，让我们回过头来问一个更基本的问题：为什么我们用动量来标记自由粒子的状态？这里的答案是因为动量守恒。在量子理论中，这意味着动量算符与哈密顿量对易：[p, H] = 0，因此我们可以同时用能量和动量来标记状态。最终，诺特定理告诉我们，这种守恒律源于系统的平移不变性。

现在让我们看看我们的晶格系统。我们不再具有平移不变性。相应地，在近自由电子模型中，[p, H] ≠ 0。希望这现在让我们的原始问题更清晰：为什么我们可以用k来标记状态？

s by k?!

While we don’t have full, continuous translational invariance, both the models that we discussed do have a discrete version of translational invariance x → x+a. As we now show, this is sufficient to ensure that we can label states by something very similar to “momentum”. However, the values of this momentum are restricted. This result is known as Bloch’s Theorem. Here we prove the theorem for our one-dimensional system; we will revisit it in Section 2.3.1 in higher dimensions.

The Translation Operator For concreteness, let’s work with continuous space where states are described by a wavefunction ψ(x). (There is a simple generalisation to discrete situations such as the tight-binding model that we describe below.) We introduce the translation operator T as T ψ(x) = ψ(x+l)

First note that T is a unitary operator. To see this, we just need to look at the overlap ⟨ϕ|T |ψ⟩ = dx ϕ(x)⋆T ψ(x) = dx ϕ(x)⋆ψ(x+l)

l l = dx ϕ(x−l)⋆ψ(x) = dx [T ϕ(x)]⋆ψ(x)

−l where, in the step to the second line, we’ve simply shifted the origin. This tells us that T† = T . But clearly T−1 = T as well, so T† = T−1 and the translation operator is l −l l −l l l unitary as claimed.

Next note that the set of translation operators form an Abelian group, T T = T (2.20)

l1 l2 l1+l2 with [T ,T ] = 0.

l1 l2

The translation operator is a close cousin of the familiar momentum operator p = −iℏ dx.

The relationship between the two is as follows: the unitary translation operator is the exponentiation of the Hermitian momentum operator T = eilp/ℏ.

To see this, we expand the exponent and observe that T ψ(x) = ψ(x + l) is just a compact way of expressing the Taylor expansion of a function T ψ(x) = (1 + ilp/ℏ + (ilp/ℏ)2/2! + ...) ψ(x)

= (1 + l d/dx + l2 d2/dx2/2! + ...) ψ(x) = ψ(x+l)

We say that the momentum operator is the “generator” of infinitesimal translations.

A quantum system is said to be invariant under translations by l if [H,T ] = 0 (2.21)

Phrased in this way, we can describe both continuous translational symmetry and discrete translational symmetry. A system has continuous translational invariance if (2.21) holds for all l. In this case, we may equivalently say that [p,H] = 0. Alternatively, a system may have discrete translational invariance if (2.21) holds only when l is an integer multiple of the lattice spacing a. Now p does not commute with H.

Let’s look at the case of discrete symmetry. Now we can’t simultaneously diagonalise p and H, but we can simultaneously diagonalise T and H. In other words, energy eigenstates can be labelled by the eigenvalues of T . But T is a unitary operator and a its eigenvalues are simply a phase, eiθ for some θ. Moreover, we want the eigenvalues to respect the group structure (2.20). This is achieved if we write the eigenvalue of T as eiθ = eikl for some k, so that the eigenvalue of T coincides with the eigenvalue of na Tn. The upshot is that eigenstates are labelled by some k, such that T ψ (x) = ψ (x+a) = eikaψ (x)

a k k k

Now comes the rub. Because the eigenvalue is a phase, there is an arbitrariness in this labelling: states labelled by k have the same eigenvalue under T as states labelled by k + 2π/a. To remedy this, we will simply require that k lies in the range k ∈ (−π/a, π/a] (2.22)

We recognise this as the first Brillouin zone.

This, then, is the essence of physics on a lattice. We can still label states by k, but it now lies in a finite range. Note that we can approximate a system with continuous translational symmetry by taking a arbitrarily small; in this limit we get the usual result k ∈ R.

This discussion leads us directly to: Bloch’s Theorem in One Dimension: In a periodic potential, V(x) = V(x+a), there exists a basis of energy eigenstates that can be written as ψ (x) = eikxu (x)

k k where u (x) = u (x+a) is a periodic function and k lies in the Brillouin zone (2.22).

k k Proof: We take ψ to be an eigenstate of the translation operator T , so that k a ψ (x+a) = eikaψ (x). Then u (x+a) = e−ik(x+a)ψ (x+a) = e−ikxψ (x) = u (x). □ k k k k k k

Bloch’s theorem is rather surprising. One might think that the presence of a periodic potential would dramatically alter the energy eigenstates, perhaps localising them in some region of space. Bloch’s theorem is telling us that this doesn’t happen: instead the plane wave states eikx are altered only by a periodic function u(x), sometimes referred to as a Bloch function, and the fact that the wavenumber is restricted to the first Brillouin zone.

Finally, note that we’ve couched the above discussion in terms of wavefunctions ψ(x), but everything works equally well for the tight-binding model with the translation operator defined by T |n⟩ = |n+1⟩.

Crystal Momentum The quantity p = ℏk is the quantity that replaces momentum in the presence of a lattice. It is called the crystal momentum.

Note, however, that it doesn’t have the simple interpretation of "mass × velocity". (We will describe how to compute the velocity of a particle in terms of the crystal momentum in Section 3.2.1.) Crystal momentum is conserved. This becomes particularly important when we consider multiple particles moving in a lattice and their interactions. This, of course, sounds the same as the usual story of momentum. Except there’s a twist: crystal momentum is conserved only mod 2π/a. It is perfectly possible for two particles to collide in a lattice environment and their final crystal momentum to differ from their initial crystal momentum by some multiple of 2π/a. Roughly speaking, the lattice absorbs the excess momentum.

This motivates us to re-think how we draw the energy spectrum. Those parts of the spectrum that lie outside the first Brillouin zone should really be viewed as having the same crystal momentum. To show this, we draw the energy spectrum as a multi-valued function of k ∈ [−π/a,π/a). The spectrum that we previously saw in Figure 18 then looks like The original way of drawing the spectrum is known as the extended zone scheme. The new way is known as the reduced zone scheme. Both have their uses. Note that edges of the Brillouin zone are identified: k = π/a is the same as k = −π/a. In other words, the Brillouin zone is topologically a circle.

In the reduced zone scheme, states are labelled by both k ∈ [−π/a,π/a) and an integer n = 1,2,... which tells us which band we are talking about.

**2.2 Lattices**

The ideas that we described above all go over to higher dimensions. The key difference is that lattices in higher dimensions are somewhat more complicated than a row of points. In this section, we introduce the terminology needed to describe different kinds of lattices. In Section 2.3, we’ll return to look at what happens to electrons moving in these lattice environments.

**2.2.1 Bravais Lattices**

The simplest kind of lattice is called a Bravais lattice. This is a periodic array of points defined by integer sums of linearly independent basis vectors a. In two-dimensions, a Bravais lattice Λ is defined by Λ = {r = n₁a₁ + n₂a₂, nᵢ ∈ Z}. An obvious example is the square lattice shown to the right. We will see further examples shortly.

In three dimensions, a Bravais lattice is defined by Λ = {r = n₁a₁ + n₂a₂ + n₃a₃, nᵢ ∈ Z}. These lattices have the property that any point looks just the same as any other point. In mathematics, such an object would simply be called a lattice. Here we add the word Bravais to distinguish these from more general kinds of lattices that we will meet shortly.

The basis vectors a are called primitive lattice vectors. They are not unique. As an example, look at the 2-dimensional square lattice below. We could choose basis vectors (a₁,a₂) or (a′₁,a₂). Both will do the job.

A primitive unit cell is a region of space which, when translated by the primitive lattice vectors a, tessellates the space. This means that the cells fit together, without overlapping and without leaving any gaps. These primitive unit cells are not unique. As an example, let’s look again at the 2-dimensional square lattice. Each of the three possibilities shown below is a good unit cell.

Each primitive unit cell contains a single lattice point. This is obvious in the second and third examples above. In the first example, there are four lattice points associated to the corners of the primitive unit cell, but each is shared by four other cells. Counting these as a 1/4 each, we see that there is again just a single lattice point in the primitive unit cell.

Although the primitive unit cells are not unique, each has the same volume. It is given by V = |a₁ · (a₂ × a₃)|. Because each primitive unit cell is associated to a single lattice point, V = 1/n where n is the density of lattice points.

Note finally that the primitive unit cell need not have the full symmetry of the lattice. For example, the third possible unit cell shown above for the square lattice is not invariant under 90° rotations.

For any lattice, there is a canonical choice of primitive unit cell that does inherit the symmetry of the underlying lattice. This is called the Wigner-Seitz cell, Γ. (It sometimes goes by the name of the Voronoi cell.) Pick a lattice point which we choose to be at the origin. The Wigner-Seitz cell is defined to be the region of space around such that the origin is the closest lattice point. In equations, Γ = {x : |x| < |x−r| ∀ r ∈ Λ s.t. r ≠ 0}.

The Wigner-Seitz cells for square and triangular lattices are given by There is a simple way to construct the Wigner-Seitz cell. Draw lines from the origin to all other lattice points. For each of these lines, construct the perpendicular bi-sectors; these are lines in 2d and planes in 3d. The Wigner-Seitz cell is the inner area bounded by these bi-sectors. Here’s another example.

**Examples of Bravais Lattices in 2d** 让我们看一些例子。在二维中，布拉维格子由两个不平行的向量 a₁ 和 a₂ 定义，它们之间的夹角 θ ≠ 0。然而，其中一些格子比其他格子更为特殊。例如，当 |a₁| = |a₂| 且 θ = π/2 时，该格子为正方形，并具有额外的旋转对称性。

如果两个布拉维格子共享相同的对称群，则认为它们是等价的。根据这个定义，二维中存在五种可能的布拉维格子。它们是： • 正方形：|a₁| = |a₂| 且 θ = π/2。它具有四重旋转对称性和反射对称性。

• 三角形：|a₁| = |a₂| 且 θ = π/3 或 θ = 2π/3。这也被称为六角格子。它具有六重旋转对称性。

• 长方形：|a₁| ≠ |a₂| 且 θ = π/2。具有反射对称性。

• 体心长方形：|a₁| ≠ |a₂| 且 θ ≠ π/2，但其原始基矢应满足 (2a₂ - a₁) · a₁ = 0。这意味着该格子看起来像一个在中心多了一个点的矩形。

• 斜方形：|a₁| ≠ |a₂|，且没有特殊条件。它包含所有其他情况。

正方形、三角形和斜方形格子在前一页中已示出，我们还绘制了它们的维格纳-塞兹原胞。

**并非所有格子都是布拉维格子**

并非所有感兴趣的格子都是布拉维格子。一个二维中特别重要的格子形状像蜂窝，如下所示。

这个格子描述了一种叫做石墨烯的材料，我们将在第 3.1.3 节中更详细地描述。该格子不是布拉维格子，因为并非所有点都是相同的。要理解这一点，考虑从格子中取出的一个六边形单元，如下图所示。

每个红点是相同的：它们左边有一个邻居，右边对角线方向有两个邻居。但白点是不同的。每个白点右边有一个邻居，左边对角线方向有两个邻居。

像这样的格子最好通过将其分解为原子组来思考，其中每个组的某个元素位于布拉维格子的顶点上。对于蜂窝格子，我们可以考虑原子组。红色顶点构成一个三角形格子，其原始格矢为 a₁ = (√3/2 a, 1/2 a), a₂ = (√3/2 a, -1/2 a)

同时，每个红色顶点都伴随着一个白色顶点，该白色顶点位移为 d = (-a, 0)

这样我们就构建了蜂窝格子。

这种构造方法可以推广。我们可以将任何格子描述为重复的原子组，其中每个组位于一个底层布拉维格子 Λ 上。组中的每个原子相对于布拉维格子顶点位移一个向量 dᵢ。每个标记为 dᵢ 的原子组被称为基矢。例如，对于蜂窝格子，我们选择红色原子的基矢 d₁ = 0，白色原子的基矢 d₂ = d，因为红色原子位于底层三角形格子的位置上。通常没有要求任何原子必须位于底层布拉维格子的顶点上。整个格子则由布拉维格子和基矢的并集描述：Λ ∪ {Λ + dᵢ}。

**三维布拉维格子的例子**

三维中有 14 种不同的布拉维格子。幸运的是，我们不需要全部了解。实际上，我们将只描述在自然界中最常出现的三种。它们是： • 立方：这是最简单的格子。其原始格矢与欧几里得轴对齐 a₁ = a x̂, a₂ = a ŷ, a₃ = a ẑ 原始胞体积为 V = a³。维格纳-塞兹原胞也是一个立方体，围绕其中一个格点居中。

• 体心立方 (BCC)：这是一个立方格子，在每个立方体的中心增加了一个点。我们可以取其原始格矢为 a₁ = a x̂, a₂ = a ŷ, a₃ = a (x̂ + ŷ + ẑ)/2 然而，一个更对称的选择是 a₁ = a (−x̂ + ŷ + ẑ)/2, a₂ = a (x̂ − ŷ + ẑ)/2, a₃ = a (x̂ + ŷ − ẑ)/2 其原始单胞体积为 V = a³/2。

BCC 格子也可以被视为一个立方格子，其基矢为两个原子，位移分别为 d₁ = 0 和 d₂ = a(x̂ + ŷ + ẑ)/2。然而，这并不影响 BCC 格子本身是布拉维格子这一事实。

• 面心立方 (FCC)：这同样是基于立方格子构建的，现在在每个面的中心增加了一个点。其原始格矢为 a₁ = a (ŷ + ẑ)/2, a₂ = a (x̂ + ẑ)/2, a₃ = a (x̂ + ŷ)/2 原始单胞体积为 V = a³/4。

FCC 格子也可以被视为一个立方格子，其基矢为四个原子，分别位于 d₁ = 0, d₂ = a(x̂ + ŷ)/2, d₃ = a(x̂ + ẑ)/2 和 d₄ = a(ŷ + ẑ)/2。

ê + ẑ).

Nonetheless, it is also a Bravais lattice in its own right.

Examples of FCC structures include several of the Alkaline earth metals (Be, Ca, Sr), many of the transition metals (Sc, Ni, Pd, Pt, Rh, Ir, Cu, Ag, Au)

and the Noble gases (Ne, Ar, Kr, Xe) when in solid form, again with a ≈ 3 to 6×10−10 m in each case.

The Wigner-Seitz cells for the BCC and FCC lattices are polyhedra, sitting inside a cube. For example, the Wigner-Seitz cell for the BCC lattice is shown in the left-hand figure.

Examples of non-Bravais Lattices in 3d As in the 2d examples above, we can describe non-Bravais crystals in terms of a basis of atoms sitting on an underlying Bravais lattice. Here are two particularly simple examples.

Figure 25: Wigner-Seitz cell for BCC Figure 26: Salt.

Diamond is made up of two, interlaced FCC lattices, with carbon atoms sitting at the basis points d = 0 and d = a(1/2)(x̂ + ŷ + ẑ). Silicon and germanium also adopt this structure.

Another example is salt (NaCl). Here, the basic structure is a cubic lattice, but with Na and Cl atoms sitting at alternate sites. It’s best to think of this as two, interlaced FCC lattices, but shifted differently from diamond. The basis consists of a Na atom at d = 0 and a Cl atom at d = a(1/2)(x̂ + ŷ + ẑ). This basis then sits on top of an FCC lattice.

2.2.2 The Reciprocal Lattice Given a Bravais lattice Λ, defined by primitive vectors aᵢ, the reciprocal lattice Λ⋆ is defined by the set of points Λ⋆ = {k = Σᵢ nᵢ bᵢ, nᵢ ∈ ℤ} where the new primitive vectors bᵢ obey aᵢ · bⱼ = 2πδᵢⱼ  (2.24)

Λ⋆ is sometimes referred to as the dual lattice. In three dimensions, we can simply construct the lattice vectors bᵢ by bᵢ = (2π/V) εᵢⱼₖ aⱼ × aₖ where V is the volume of unit cell of Λ (2.23). We can also invert this relation to get aᵢ = (2π/V⋆) εᵢⱼₖ bⱼ × bₖ where V⋆ = |b₁ · (b₂ × b₃)| = (2π)³/V is the volume of Γ⋆, the unit cell of Λ⋆. Note that this shows that the reciprocal of the reciprocal lattice gives you back the original.

The condition (2.24) can also be stated as the requirement that e^(i k·r) = 1  ∀ r ∈ Λ, k ∈ Λ⋆  (2.25)

which provides an alternative definition of the reciprocal lattice.

Here are some examples: • The cubic lattice has a₁ = a x̂, a₂ = a ŷ and a₃ = a ẑ. The reciprocal lattice is also cubic, with primitive vectors b₁ = (2π/a) x̂, b₂ = (2π/a) ŷ and b₃ = (2π/a) ẑ • The BCC lattice has a₁ = a(−x̂ + ŷ + ẑ)/2, a₂ = a(x̂ − ŷ + ẑ)/2 and a₃ = a(x̂ + ŷ − ẑ)/2.

The reciprocal lattice vectors are b₁ = (2π/a)(ŷ + ẑ), b₂ = (2π/a)(x̂ + ẑ) and b₃ = (2π/a)(x̂ + ŷ). But we’ve seen these before: they are the lattice vectors for a FCC lattice with the sides of the cubic cell of length 4π/a.

We see that the reciprocal of a BCC lattice is an FCC lattice and vice versa.

The Reciprocal Lattice and Fourier Transforms The reciprocal lattice should not be thought of as sitting in the same space as the original. This follows on dimensional grounds. The original lattice vectors aᵢ have the dimension of length, [aᵢ] = L. The definition (2.24) then requires the dual lattice vectors bᵢ to have dimension [bᵢ] = 1/L. The reciprocal lattice should be thought of as living in Fourier space which, in physics language, is the same thing as momentum space. As we’ll now see, the reciprocal lattice plays an important role in the Fourier transform.

Consider a function f(x) where, for definiteness, we’ll take x ∈ ℝ³. Suppose that this function has the periodicity of the lattice Λ, which means that f(x) = f(x+r) for all r ∈ Λ. The Fourier transform is f̃(k) = ∫ d³x e^(-i k·x) f(x) = Σ_{r∈Λ} ∫_Γ d³x e^(-i k·(x+r)) f(x+r)

= Σ_{r∈Λ} e^(-i k·r) ∫_Γ d³x e^(-i k·x) f(x)  (2.26)

In the second equality, we have replaced the integral over ℝ³ with a sum over lattice points, together with an integral over the Wigner-Seitz cell Γ. In going to the second line, we have used the periodicity of f(x). We see that the Fourier transform comes with the overall factor ∆(k) = Σ_{r∈Λ} e^(-i k·r)  (2.27)

This is an interesting quantity. It has the following property:

Claim: ∆(k) = 0 unless k ∈ Λ⋆.

Proof: Since we’re summing over all lattice sites, we could equally well write ∆(k) = Σ_{r∈Λ} e^(-i k·(r−r₀)) for any r₀ ∈ Λ. This tells us that ∆(k) = e^(i k·r₀) ∆(k) for any r₀ ∈ Λ.

This means that ∆(k) = 0 unless e^(i k·r₀) = 1 for all r₀ ∈ Λ. But this is equivalent to saying that ∆(k) = 0 unless k ∈ Λ⋆. □ In fact, we can get a better handle on the function (strictly, a distribution) ∆(k).

We have Claim: ∆(k) = V⋆ Σ_{q∈Λ⋆} δ(k−q).

Proof: We can expand k = Σᵢ kᵢ bᵢ, with kᵢ ∈ ℝ, and r = Σᵢ nᵢ aᵢ with nᵢ ∈ ℤ.

Then, using (2.24), we have ∆(k) = σ(k₁)σ(k₂)σ(k₃) where σ(k) = Σ_{n=−∞}^{∞} e^(-2πi k n)

The range of the sum in σ(k) is appropriate for an infinite lattice. If, instead, we had a finite lattice with, say, N +1 points in each direction, (assume, for convenience, that N is even), we would replace σ(k) with Σ_{n=−N/2}^{N/2} e^(-2πi k n) = e^(-2πi k (N/2+1)) (e^(2πi k (N+1)) − 1) / (e^(2πi k) − 1) = e^(πi k N) sin((N+1)π k) / sin(π k)

σ(k) = Σ_{n=-N/2}^{N} e^{-2πikn}/N = e^{-2πik} - e^{πik} sin(πk)

This function is plotted on the right for -1/2 < k < 1/2. We have chosen a measly N = 10 in this plot, but already we see that the function is heavily peaked near the origin: when k ~ O(1/N), then σ(k) ~ O(N). As N → ∞, this peak becomes narrower and taller and the area under it tends towards 1. To see this last point, replace sin(πk) ≈ πk and use the fact that ∫_{-∞}^{+∞} sin(x)/x dx = π. This shows that the peak near the origin tends towards a delta function.

Figure 27: The function σ(k) is periodic. We learn that, for large N, σ(k) just becomes a series of delta functions, restricting k to be integer valued lim_{N→∞} σ(k) = Σ_{n=-∞}^{∞} δ(k - n)

Looking back at (2.27), we see that these delta functions mean that the Fourier transform is only non-vanishing when k = Σ_i k_i b_i with k_i ∈ Z. But this is precisely the condition that k lies in the reciprocal lattice. We have Δ(k) = Σ_{r∈Λ} e^{-ik·r} = V* Σ_{q∈Λ*} δ(k - q)    (2.28)

We can understand this formula as follows: if k ∈ Λ*, then e^{-ik·r} = 1 for all r ∈ Λ and summing over all lattice points gives us infinity. In contrast, if k ∉ Λ*, then the phases e^{-ik·r} oscillate wildly for different r and cancel each other out. □ The upshot is that if we start with a continuous function f(x) with periodicity Λ, then the Fourier transform (2.26) has support only at discrete points Λ*, f ̃(k) = Δ(k) S(k) with S(k) = ∫ d^3x e^{-ik·x} f(x)

Here S(k) is known as the structure factor. Alternatively, inverting the Fourier transform, we have f(x) = (1/(2π)^3) ∫ d^3k e^{ik·x} f ̃(k) = (V*/(2π)^3) Σ_{q∈Λ*} e^{iq·x} S(q)    (2.29)

This tells us that any periodic function is a sum of plane waves whose wavevectors lie on the reciprocal lattice. We’ll revisit these ideas in Section 2.4 when we discuss x-ray scattering from a lattice.

2.2.3 The Brillouin Zone The Wigner-Seitz cell of the reciprocal lattice is called the Brillouin zone.

We already saw the concept of the Brillouin zone in our one-dimensional lattice. Let’s check that this coincides with the definition given above. The one-dimensional lattice is defined by a single number, a, which determines the lattice spacing. The Wigner-Seitz cell is defined as those points which lie closer to the origin than any other lattice point, namely r ∈ [-a/2, a/2). The reciprocal lattice is defined by (2.24) which, in this context, gives the lattice spacing b = 2π/a. The Wigner-Seitz cell of this reciprocal lattice consists of those points which lie between [-b/2, b/2) = [-π/a, π/a). This coincides with what we called the Brillouin zone in Section 2.1.

The Brillouin zone is also called the first Brillouin zone. As it is the Wigner-Seitz cell, it is defined as all points in reciprocal space that are closest to a given lattice point, say the origin. The nth Brillouin zone is defined as all points in reciprocal space that are nth closest to the origin. All these higher Brillouin zones have the same volume as the first.

Figure 28: The Brillouin zones for a 2d square lattice. The first is shown in yellow, the second in pink, the third in blue.

We can construct the Brillouin zone boundaries by drawing the perpendicular bisectors between the origin and each other point in Λ*. The region enclosing the origin is the first Brillouin zone. The region you can reach by crossing just a single bisector is the second Brillouin zone, and so on. In fact, this definition generalises the Brillouin zone beyond the simple Bravais lattices.

As an example, consider the square lattice in 2d. The reciprocal lattice is also square. The first few Brillouin zones on this square lattice are shown in Figure 28.

For the one-dimensional lattice that we looked at in Section 2.1, we saw that the conserved momentum lies within the first Brillouin zone. This will also be true in higher dimensions. This motivates us to work in the reduced zone scheme, in which these higher Brillouin zones are mapped back into the first. This is achieved by translating them by some lattice vector. The higher Brillouin zones of the square lattice in the reduced zone scheme are shown in Figure 29.

Finally, note that the edges of the Brillouin zone should be identified; they label the same momentum state k. For one-dimensional lattices, this results in the Brillouin zone having the topology of a circle. For d-dimensional lattices, the Brillouin zone is topologically a torus T^d.

Figure 29: The first three Brillouin zones for a square lattice in the reduced zone scheme.

Crystallographic Notation The Brillouin zone of real materials is a three-dimensional space. We often want to describe how certain quantities – such as the energy of the electrons – vary as we move around the Brillouin zone. To display this information graphically, we need to find a way to depict the underlying Brillouin zone as a two-dimensional, or even one-dimensional space. Crystallographers have developed a notation 对于某些高度对称的布里渊区点，会用字母来标记。从这些字母，你还应该记住所讨论的底层晶格是什么。例如，所有布里渊区都有一个原点。“原点”这个概念出现在数学和物理的许多不同部分，几乎所有人都同意将其标记为“0”。几乎是所有人，但不包括我们的晶体学朋友。相反，他们将原点称为Γ。

从这里开始，事情变得更加令人困惑，尽管如果你看足够多这样的标记，你会习惯它。例如，对于立方晶格，每个面的中心称为X，每条边的中心称为M，而每个角称为R。图30显示了BCC和FCC晶格的各种标记。

## 2.3 能带结构

“当我开始思考这个问题时，我觉得主要问题在于解释电子如何能溜过金属中的所有离子……我欣喜地发现，波函数与自由电子的平面波之差仅在于一个周期性调制。这太简单了，以至于我不认为它会是什么重大发现，但当我把它展示给海森堡时，他立刻说：‘就是它了。’”——费利克斯·布洛赫

现在我们已经发展了描述高维晶格的语言，是时候理解电子在固定晶格背景下运动时的行为了。我们在第2.1节一维晶格的背景下已经看到了许多主要思想。这里我们将描述向高维度的推广。

图30：布里渊区上各种特殊点的标记。

2.3.1 布洛赫定理

考虑一个在具有布拉维晶格Λ周期性的势场V(x)中运动的电子， V(x+r) = V(x) 对所有r ∈ Λ成立布洛赫定理指出，能量本征态的形式为 ψ_k(x) = e^{ik·x} u_k(x)

其中u_k(x)具有与晶格相同的周期性，即u_k(x+r) = u_k(x) 对所有r ∈ Λ成立。

有多种方法可以证明布洛赫定理。这里我们将使用平移算子的概念给出一个简单的证明，类似于我们在第2.1.4节看到的一维证明。稍后，在第2.3.2节，我们将通过将薛定谔方程分解为傅里叶模来提供更直接的证明。

我们的出发点是，哈密顿量在晶格矢量r ∈ Λ的离散平移下不变。正如我们在第2.1.4节所解释的，这些平移由幺正算子T_r实现。这些算子构成一个阿贝尔群， T_r T_{r'} = T_{r+r'} (2.30)

并且与哈密顿量对易：[H, T_r] = 0。这意味着我们可以同时对角化H和T_r，因此能量本征态也由每个T_r的本征值标记。因为T_r是幺正的，这只是一个相位。但我们还必须尊重群结构(2.30)。假设一个给定的本征态平移一个基矢a_i给出的本征值为 T_{a_i} ψ(x) = ψ(x+a_i) = e^{iθ_i} ψ(x)

那么平移一个一般的晶格矢量r = Σ_i n_i a_i 必须给出 T_r ψ(x) = ψ(x+r) = e^{i Σ_i n_i θ_i} ψ(x) = e^{ik·r} ψ(x)

其中矢量k定义为满足k·a_i = θ_i。换句话说，我们可以用矢量k来标记T_r的本征态。它们满足 T_r ψ_k(x) = ψ_k(x+r) = e^{ik·r} ψ_k(x)

现在我们只需考虑函数u_k(x) = e^{-ik·x} ψ_k(x)。布洛赫定理的陈述是u_k(x)具有Λ的周期性，这确实是正确的，因为 u_k(x+r) = e^{-ik·(x+r)} ψ_k(x+r) = e^{-ik·x} e^{-ik·r} e^{ik·r} ψ_k(x) = e^{-ik·x} ψ_k(x) = u_k(x)。

晶体动量能量本征态由波矢k标记，称为晶体动量。这个晶体动量的定义存在模糊性。这与真实动量不同。能量本征态没有明确的动量，因为它们不是动量算子p = -iℏ∇的本征态，除非u_k(x)是常数。尽管如此，我们将看到晶体动量扮演着与真实动量类似的角色。为此，我们经常简单地将k称为“动量”。

晶体动量的定义存在模糊性。考虑一个晶体动量为k' = k+q的态，其中q ∈ Λ*是倒格矢。那么 ψ_{k'}(x) = e^{ik·x} e^{iq·x} u_k(x) = e^{ik·x} ũ_k(x)

其中ũ_k(x) = e^{iq·x} u_k(x) 根据倒格子的定义(2.25)也具有Λ的周期性。

与一维的例子一样，我们有不同的选择。我们可以选择用位于第一布里渊区内的k来标记态。在这种情况下，通常会有许多具有相同k但不同能量的态。这就是简约布里渊区方案。在这种情况下，能量本征态由两个指标标记，ψ_{k,n}，其中k是晶体动量，n称为能带索引。（我们很快会看到例子。）

或者，我们可以用任意k ∈ R^d（其中d是问题的维度）来标记态。这就是扩展布里渊区方案。在这种情况下，由k标记的态，如果它们相差Λ*，则具有相同的晶体动量。

2.3.2 近自由电子 in Three Dimensions

Consider an electron moving in R3 in the presence of a weak potential V(x). We’ll assume that this potential has the periodicity of a Bravais lattice Λ, so V(x) = V(x+r) for all r ∈ Λ. We treat this potential as a perturbation on the free electron. This means that we start with plane wave states |k⟩ with wavefunctions ⟨x|k⟩ ∼ eik·x with energy E (k) = ℏk2/2m. We want to see how these states and their energy levels are affected by the presence of the potential. The discussion will follow closely the one-dimensional case that we saw in Section 2.1.2 and we only highlight the differences.

When performing perturbation theory, we’re going to have to consider the potential V(x) sandwiched between plane-wave states, ⟨k|V(x)|k′⟩ = ∫Volume d3x ei(k′−k)·xV(x)

However, we’ve already seen in (2.29) that the Fourier transform of a periodic function can be written as a sum over wavevectors that lie in the reciprocal lattice Λ⋆, V(x) = ∑q∈Λ⋆ eiq·xV (Note: here V is the Fourier component of the potential and should not be confused with the volumes of unit cells which were denoted as V and V⋆ in Section 2.2.) This means that ⟨k|V(x)|k′⟩ is non-vanishing only when the two momenta differ by k−k′ = q, where q ∈ Λ⋆. This has a simple physical interpretation: a plane wave state |k⟩ can scatter into another plane wave state |k′⟩ only if they differ by a reciprocal lattice vector. In other words, only momenta q, with q ∈ Λ⋆, can be absorbed by the lattice.

Another Perspective on Bloch’s Theorem

The fact that a plane wave state |k⟩ can only scatter into states |k−q⟩, with q ∈ Λ⋆, provides a simple viewpoint on Bloch’s theorem, one that reconciles the quantum state with the naive picture of the particle bouncing off lattice sites like a ball in a pinball machine. Suppose that the particle starts in some state |k⟩. After scattering, we might expect it to be some superposition of all the possible scattering states |k−q⟩. In other words, ψ (x) = ∑q∈Λ⋆ ei(k−q)·xc k k−q for some coefficients c k−q. We can write this as ψ (x) = ∑q∈Λ⋆ eik·x e−iq·xc k k−q = eik·xu k (x)

where, by construction, u k (x+r) = u k (x) for all r ∈ Λ. But this is precisely the form guaranteed by Bloch’s theorem.

Although the discussion here holds at first order in perturbation theory, it is not hard to extend this argument to give an alternative proof of Bloch’s theorem, which essentially comes down to analysing the different Fourier modes of the Schrödinger equation.

Band Structure

Let’s now look at what becomes of the energy levels after we include the perturbation. We will see that, as in the 1d example, they form bands. The resulting eigenstates ψ k,n (x) and their associated energy levels E n (k) are referred to as the band structure of the system.

Low Momentum: Far from the edge of the Brillouin zone, the states |k⟩ can only scatter into states |k+q⟩ with greatly different energy. In this case, we can work with non-degenerate perturbation theory to compute the corrections to the energy levels.

On the Boundary of the Brillouin zone: Things get more interesting when we have to use degenerate perturbation theory. This occurs whenever the state |k⟩ has the same energy as another state |k+q⟩ with q ∈ Λ⋆, E 0 (k) = E 0 (k+q) ⇒ k2 = (k+q)2 ⇒ 2k·q+q2 = 0 This condition is satisfied whenever we can write k = − q+k where q · k = 0. This is the condition that we sit on the perpendicular bisector of the origin and the lattice point −q ∈ Λ⋆. But, as we explained in Section 2.2.3, these bisectors form the boundaries of the Brillouin zones. We learn something important: momentum states are degenerate only when they lie on the boundary of a Brillouin zone. This agrees with what we found in our one-dimensional example in Section 2.1.2.

[Figure 31: Energy contours for nearly-free electrons in the first Brillouin zone.]

We know from experience what the effect of the perturbation V(x) will be: it will lift the degeneracy. This means that a gap opens at the boundary of the Brillouin zone. For example, the energy of states just inside the first Brillouin zone will be pushed down, while the energy of those states just outside the first Brillouin zone will be pushed up. Note that the size of this gap will vary as we move around the boundary.

There is one further subtlety that we should mention. At a generic point on the boundary of the Brillouin zone, the degeneracy will usually be two-fold. However, at special points — such as edges, or corners — it is often higher. In this case, we must work with all degenerate states when computing the gap.

All of this is well illustrated with an example. However, it’s illustrated even better if you do the example yourself! The problem of nearly free electrons in a two-dimensional square lattice is on the problem sheet. The resulting energy contours are shown in Figure 31.

Plotting Band Structures in Three Dimensions

For three-dimensional lattice, we run into the problem of depicting the band structure in a way that is both informative and readable.

We can then compare this to the band structure of real materials. The dispersion relation for silicon is also shown in Figure 32. This has a diamond lattice structure, which is plotted as FCC. Note that you can clearly see the energy gap of around 1.1 eV between the bands.

Figure 32: Free band structure (in red) for BCC and FCC, together with the band structure for silicon, exhibiting a gap.

How Many States in the Brillouin Zone?

The Brillouin zone consists of all wavevectors k that lie within the Wigner-Seitz cell of the reciprocal lattice Λ⋆. How many quantum states does it hold? Well, if the spatial lattice Λ is infinite in extent then k can take any continuous value and there are an infinite number of states in the Brillouin zone. But what if the spatial lattice is finite in size?

In this section we will count the number of quantum states in the Brillouin zone of a finite spatial lattice Λ. We will find a lovely answer: the number of states is equal to N, the number of lattice sites.

Recall that the lattice Λ consists of all vectors r = Σ_i n_i a_i where a_i are the primitive lattice vectors and n_i ∈ Z. For a finite lattice, we simply restrict the value of these integers to be 0 ≤ n_i < N_i for some N_i. The total number of lattice sites is then N = N_1 N_2 N_3 (assuming a three-dimensional lattice). The total volume of the lattice is VN where V = |a_1 ·(a_2 ×a_3)| is the volume of the unit cell.

The basic physics is something that we’ve met before: if we put a particle in a box, then the momentum ℏk becomes quantised. This arises because of the boundary conditions that we place on the wavefunction. It’s simplest to think about a finite, periodic lattice where we require that the wavefunction inherits this periodicity, so that ψ(x+N_i a_i) = ψ(x) for each i = 1,2,3 (2.31)

But we know from Bloch’s theorem that energy eigenstates take the form ψ_k(x) = eik·x u_k(x) where u_k(x+a_i) = u_k(x). This means that the periodicity condition (2.31) becomes e^(i N_i k·a_i) = 1 ⇒ k = Σ_i m_i b_i where m_i ∈ Z and b_i are the primitive vectors of the reciprocal lattice defined in (2.24). This is sometimes called the Born-von Karmen boundary condition.

This is the quantisation of momentum that we would expect in a finite system. The states are now labelled by integers m_i ∈ Z. Each state can be thought of as occupying a volume in k-space, given by |b_1 ·(b_2 ×b_3)| / (N_1 N_2 N_3)

where V⋆ is the volume of the Brillouin zone. We see that the number of states that live inside the Brillouin zone is precisely N, the number of sites in the spatial lattice.

2.3.3 Wannier Functions Bloch’s theorem tells that the energy eigenstates can be written in the form ψ_k(x) = eik·x u_k(x)

with k lying in the first Brillouin zone and u_k(x) a periodic function. Clearly these are delocalised throughout the crystal. For some purposes, it’s useful to think about these Bloch waves as arising from the sum of states, each of which is localised at a given lattice site. These states are called Wannier functions; they are defined as w_r(x) = (1/√N) Σ_k e^(-ik·r) ψ_k(x) (2.32)

where the sum is over all k in the first Brillouin zone.

The basic idea is that the Wannier wavefunction w_r(x) is localised around the lattice site r ∈ Λ. Indeed, using the periodicity properties of the Bloch wavefunction, it’s simple to show that w_(r+r′)(x) = w_r(x), which means that we can write w_r(x) = w(x−r).

The Wannier functions aren’t unique. We can always do a phase rotation ψ_k(x) → e^(iχ(k)) ψ_k(x) in the definition (2.32). Different choices of χ(k) result in differing amounts of localisation of the state w_r(x) around the lattice site r.

We can invert the definition of the Wannier function to write the original Bloch wavefunction as ψ_k(x) = (1/√N) Σ_{r∈Λ} e^(ik·r) w(x−r) (2.33)

which follows from (2.28).

The Wannier functions have one final, nice property: they are orthonormal in the sense that ∫ d^3x w⋆(x−r′)w(x−r) = (1/N) Σ_{k,k′} ∫ d^3x e^(ik′·r′−ik·r) ψ⋆_k′(x) ψ_k(x)

= (1/N) Σ_k e^(ik·(r′−r)) = δ(r−r′)

where, in going to the second line, we have used the orthogonality of Bloch wavefunctions for different k (which, in turn, follows because they are eigenstates of the Hamiltonian with different energies).

2.3.4 Tight-Binding in Three Dimensions We started our discussion of band structure in Section 2.1.1 with the one-dimensional tight binding model. This is a toy Hamiltonian describing electrons hopping from one lattice site to another. Here we’ll look at this same class of models in higher dimensional lattices.

We assume that the electron can only sit on a site of the lattice r ∈ Λ. The Hilbert space is then spanned by the states |r⟩ with r ∈ Λ. We want to write write down a Hamiltonian which describes a particle hopping between these sites. There are many different ways to do this; the simplest is H = E₀ Σ_r |r⟩⟨r| - Σ_{r, r'} t_{r-r'} (|r⟩⟨r'| + |r'⟩⟨r|)

where the label ⟨rr'⟩ means that we only sum over pairs of sites r and r' which are nearest neighbours in the lattice. Alternatively, if these nearest neighbours are connected by a set of lattice vectors a, then we can write this as H = Σ_r∈Λ E₀ |r⟩⟨r| - Σ_{r∈Λ, a} t_a |r⟩⟨r+a| (2.34)

Note that we've just got one term here, since if |r+a⟩ is a nearest neighbour, then so is |r−a⟩. The Hamiltonian is Hermitian provided t_a = t_{-a}. This Hamiltonian is easily solved. The eigenstates take the form |ψ(k)⟩ = (1/√N) Σ_{r∈Λ} e^{ik·r} |r⟩ (2.35)

where N is the total number of lattice sites. It's simple to check that these states satisfy H|ψ(k)⟩ = E(k)|ψ(k)⟩ with E(k) = E₀ - Σ_a 2t_a cos(k·a) (2.36)

where the factor of 1/2 is there because we are still summing over all nearest neighbours, including ±a. This exhibits all the properties of that we saw in the tight-binding model. The energy eigenstates (2.35) are no longer localised, but are instead spread throughout the lattice. The states form just a single band labelled, as usual, but by crystal momentum k lying in the first Brillouin zone. This is to be expected in the tight-binding model as we start with N states, one per lattice site, and we know that each Brillouin zone accommodates precisely N states.

As a specific example, consider a cubic lattice. The nearest neighbour lattice sites are a ∈ {(±a,0,0), (0,±a,0), (0,0,±a)} and the hopping parameters are the same in all directions: t_a = t. The dispersion relation is then given by E(k) = E₀ - 2t (cos(k_x a) + cos(k_y a) + cos(k_z a)) (2.37)

The width of this band is ΔE = E_max - E_min = 12t.

Note that for small k, the dispersion relation takes the form of a free particle E(k) = constant + ℏ²k²/(2m⋆) + ...

where the effective mass m⋆ is determined by various parameters of the underlying lattice, m⋆ = ℏ²/(2ta²). However, at higher k the energy is distorted away from that of a free particle. For example, you can check that k_x ± k_y = ∓π/a (with k_z = 0) is a line of constant energy.

2.3.5 Deriving the Tight-Binding Model Above, we have simply written down the tight-binding model. But it's interesting to ask how we can derive it from first principles. In particular, this will tell us what physics it captures and what physics it misses.

To do this, we start by considering a single atom which we place at the origin. The Hamiltonian for a single electron orbiting this atom takes the familiar form H_atom = p²/(2m) + V_atom(x). The electrons will bind to the atom with eigenstates ϕ_n(x) and discrete energies ϵ_n < 0, which obey H_atom ϕ_n(x) = ϵ_n ϕ_n(x). A sketch of a typical potential V_atom(x) and the binding energies ϵ_n is shown on the right. There will also be scattering states, with energies ϵ > 0, which are not bound to the atom.

Our real interest lies in a lattice of these atoms. The resulting potential is V_lattice(x) = Σ_{r∈Λ} V_atom(x−r). This is shown in Figure 34 for a one-dimensional lattice. What happens to the energy levels? Roughly speaking, we expect those electrons with large binding energies — those shown at the bottom of the spectrum — to remain close to their host atoms. But those that are bound more weakly become free to move. This happens because the tails of their wavefunctions have substantial overlap with electrons on neighbouring atoms, causing these states to mix. This is the physics captured by the tight-binding model. The weakly bound electrons which become dislodged from their host atoms are called valence electrons. (These are the same electrons which typically sit in outer shells and give rise to bonding in chemistry.) As we've seen previously, these electrons will form a band of extended states.

Let's see how to translate this intuition into equations. We want to solve the Hamiltonian H_lattice = p²/(2m) + V(x) (2.38). Our goal is to write the energy eigenstates in terms of the localised atomic states ϕ_n(x). Getting an exact solution is hard; instead, we're going to guess an approximate solution.

Extended states Localised states Figure 34: Extended and localised states in a lattice potential.

First, let's assume that there is just a single valence electron with localised wavefunction ϕ(x) with energy ϵ. We know that the eigenstates of (2.38) must have Bloch form. We can build such a Bloch state from the localised state ϕ(x) by writing ψ_k(x) = (1/√N) Σ_{r∈Λ} e^{ik·r} ϕ(x−r) (2.39), where N is the number of lattice sites. This is a Bloch state because for any a ∈ Λ, we have ψ_k(x+a) = e^{ik·a} ψ_k(x). Note that this is the same kind of state (2.35) that solved our original tight-binding model. Note also that this ansatz takes the same form as the expansion in terms of Wannier functions (2.33). However, in contrast to Wannier functions, the localised function ϕ(x) here is assumed to be a solution for a single isolated atom, not an optimally localised function for the lattice.

ast to Wannier functions, the wavefunctions ϕ(x) localised around different lattice sites are not orthogonal. This difference will be important below.

The expected energy for the state (2.39) is E(k) = ⟨ψ_k |H|ψ_k⟩ / ⟨ψ_k |ψ_k⟩

First, the denominator.

⟨ψ_k |ψ_k⟩ = ∫ d³x Σ_{r,r'∈Λ} e^{ik·(r'−r)} ϕ⋆(x−r)ϕ(x−r')

= ∫ d³x Σ_{r∈Λ} e^{-ik·r} ϕ⋆(x−r)ϕ(x)

≡ 1 + Σ_{r≠0} e^{-ik·r} α(r)

where, in going to the second line, we’ve used the translational invariance of the lattice. The function α(r) measures the overlap of the wavefunctions localised at lattice sites separated by r.

Next the numerator. To compute this, we write H = H_atom + ∆V(x) where ∆V(x) = V_lattice(x) − V_atom(x) = Σ_{r∈Λ,r≠0} V_atom(x−r)

We then have ⟨ψ_k |H|ψ_k⟩ = ∫ d³x Σ_{r,r'∈Λ} e^{ik·(r'−r)} ϕ⋆(x−r)(H_atom + ∆V)ϕ(x−r')

= ∫ d³x Σ_{r∈Λ} e^{-ik·r} ϕ⋆(x−r)(H_atom + ∆V)ϕ(x)

≡ ϵ ⟨ψ_k |ψ_k⟩ + ∆ϵ + Σ_{r≠0} e^{-ik·r} γ(r)

Here ∆ϵ is the shift in the energy of the bound state ϕ(x) due to the potential ∆V, ∆ϵ = ∫ d³x ϕ⋆(x)∆V(x)ϕ(x)

Meanwhile, the last term arises from the overlap of localised atoms on different sites γ(r) = ∫ d³x ϕ⋆(x−r)∆V(x)ϕ(x)

The upshot of this is an expression for the expected energy of the Bloch wave (2.39)

E(k) = ϵ + (∆ϵ + Σ_{r≠0} e^{-ik·r} γ(r)) / (1 + Σ_{r≠0} e^{-ik·r} α(r))

Under the assumption that α(r) ≪ 1, we can expand out the denominator (1+x)⁻¹ ≈ 1−x, and write E(k) = ϵ + ∆ϵ + Σ_{r≠0} e^{-ik·r} [γ(r) − α(r)∆ϵ] (2.40)

This still looks rather complicated. However, the expression simplifies because the overlap functions α(r) and γ(r) both drop off quickly with separation. Very often, it’s sufficient to take these to be non-zero only when r are the nearest neighbour lattice sites. Sometimes we need to go to next-to-nearest neighbours.

An Example: s-Orbitals

Let’s assume that α(r) and γ(r) are important only for r connecting nearest neighbour lattice sites; all others will be taken to vanish. We’ll further take the valence electron to sit in the s-orbital. This has two consequences: first, the localised wavefunction is rotationally invariant, so that ϕ(r) = ϕ(r). Second, the wavefunction can be taken to be real, so ϕ⋆(x) = ϕ(x). With these restrictions, we have α(r) = ∫ d³x ϕ(x−r)ϕ(x) = α(−r)

We want a similar expression for γ(r). For this, we need to make one further assumption: we want the crystal to have inversion symmetry. This means that V(x) = V(−x) or, more pertinently for us, ∆V(x) = ∆V(−x). We can then write γ(r) = ∫ d³x ϕ(x−r)∆V(x)ϕ(x)

= ∫ d³x' ϕ(−x' −r)∆V(−x')ϕ(−x')

= ∫ d³x' ϕ(|x' +r|)∆V(x')ϕ(|x'|)

= γ(−r)

where we have defined x' = −x in the second line and used both the inversion symmetry and rotational invariance of the s-orbital in the third. Now we can write the energy (2.40) in a slightly nicer form. We need to remember that the vectors r span a lattice which ensures that if r is a nearest neighbour site then −r is too. We then have E(k) = ϵ + ∆ϵ + Σ_{a} cos(k·a) [γ(a) − ∆ϵ α(a)] (2.41)

where a are the nearest neighbour lattice sites. We recognise this as the dispersion relation that we found in our original tight-binding model (2.36), with E = ϵ + ∆ϵ and t = γ(a) − ∆ϵ α(a).

So far we’ve shown that the state (2.39) has the same energy as eigenstates of the tight-binding Hamiltonian. But we haven’t yet understood when the state (2.39) is a good approximation to the true eigenstate of the Hamiltonian (2.38).

We can intuit the answer to this question by looking in more detail at (2.41). We see that the localised eigenstates ϕ(x), each of which had energy ϵ, have spread into a band with energies E(k). For this calculation to be valid, it’s important that this band doesn’t mix with other states. This means that the energies E(k) shouldn’t be too low, so that it has overlap with the energies of more deeply bound states. Nor should E(k) be too high, so that it overlaps with the energies of the scattering states which will give rise to higher bands. If the various lattice parameters are chosen so that it sits between these two values, our ansatz (2.39) will be a good approximation to the true wavefunction. Another way of saying this is that if we focus on states in the first band, we can approximate the Hamiltonian (2.38) describing a lattice of atoms by the tight-binding Hamiltonian (2.34).

A Linear Combination of Atomic Orbitals

What should we do if the band of interest does overlap with bands from more deeply bound states? The answer is that we should go back to our original ansatz (2.39) and replace it with something more general, namely ψ_k(x) = (1/√N) Σ_{r∈Λ} Σ_n c_n e^{ik·r} ϕ_n(x−r) (2.42)

where this time we sum over all localised states of interest, ϕ_n(x) with energies ϵ_n. These are now weighted with coefficients c_n which we will determine shortly. This kind of ansatz is known as a linear combination of atomic orbitals. Among people who play these kind of games, it is common enough to have its own acronym (LCAO obviously). The wavefunction (2.42) should be viewed as a variational ansatz for the eigenstates, where we get to vary the parameters c. The expected energy is again E(k) = ⟨ψ_k|H|ψ_k⟩ / ⟨ψ_k|ψ_k⟩ where, repeating the calculations that we just saw, we have ⟨ψ_k|ψ_k⟩ = ∫_Λ Σ_{r∈Λ} Σ_{n,n'} c_{n'}* c_n e^{-ik·r} d^3x ϕ_{n'}*(x-r)ϕ_n(x)

≡ Σ_{r∈Λ} Σ_{n,n'} c_{n'}* c_n e^{-ik·r} α_{n,n'}(r)  (2.43)

and ⟨ψ_k|H|ψ_k⟩ = ∫_Λ Σ_{r∈Λ} Σ_{n,n'} c_{n'}* c_n e^{-ik·r} d^3x ϕ_{n'}*(x-r)(H + ΔV_atom)ϕ_n(x)

≡ Σ_{r∈Λ} Σ_{n,n'} c_{n'}* c_n e^{-ik·r} [ ϵ_n α_{n,n'}(r) + γ_{n,n'}(r) ]  (2.44)

Note that we’ve used slightly different notation from before. We haven’t isolated the piece α_{n,n'}(r=0) = δ_{n,n'}, nor the analogous Δϵ piece corresponding to γ_{n,n'}(r=0). Instead, we continue to sum over all lattice points r ∈ Λ, including the origin.

The variational principle says that we should minimise the expected energy over all c_n. This means we should solve ∂E(k)/∂c_{n'}* = [1/⟨ψ_k|ψ_k⟩] ∂⟨ψ_k|H|ψ_k⟩/∂c_{n'}* - [⟨ψ_k|H|ψ_k⟩/⟨ψ_k|ψ_k⟩^2] ∂⟨ψ_k|ψ_k⟩/∂c_{n'}* = 0 ⇒ ∂⟨ψ_k|H|ψ_k⟩/∂c_{n'}* - E(k) ∂⟨ψ_k|ψ_k⟩/∂c_{n'}* = 0 Using our expressions (2.43) and (2.44), we can write the resulting expression as the matrix equation Σ_{n,n'} M_{n,n'}(k) c_n = 0  (2.45)

where M_{n,n'}(k) is the Hermitian matrix M_{n,n'}(k) = Σ_{r∈Λ} e^{-ik·r} [ γ_{n,n'}(r) - (E(k) - ϵ_n) α_{n,n'}(r) ]

The requirement (2.45) that M_{n,n'}(k) has a zero eigenvalue can be equivalently written as det M_{n,n'}(k) = 0 Let’s think about how to view this equation. The matrix M_{n,n'}(k) is a function of the various parameters which encode the underlying lattice dynamics as well as E(k). But what we want to figure out is the dispersion relation E(k). We should view the condition det M_{n,n'}(k) = 0 as an equation for E(k).

Suppose that we include p localised states at each site, so M_{n,n'}(k) is a p×p matrix. Then det M_{n,n'}(k) = 0 is a polynomial in E(k) of degree p. This polynomial will have p roots; these are the energies E_m(k) of p bands. In each case, the corresponding null eigenvector is c which tells us how the atomic orbitals mix in the Bloch state (2.42).

## 2.4 Scattering Off a Lattice

Finally, we come to an important question: how do we know that solids are made of lattices? The answer, of course, is scattering. Firing a beam of particles — whether neutrons, electrons or photons in the X-ray spectrum — at the solid reveals a characteristic diffraction pattern. Our goal here is to understand this within the general context of scattering theory.

In what follows, we will assume a knowledge of the basics of scattering theory. Full details can be found in the lectures on Topics in Quantum Mechanics.

Our starting point is the standard asymptotic expression describing a wave scattering off a central potential, localised around the origin, ψ(r) ∼ e^{ik·r} + f(k; k') e^{ikr}/r  (2.46)

Here we’re using the notation, introduced in earlier sections, of the scattered momentum k' = k \hat{r}.

The idea here is that if you sit far away in the direction \hat{r}, you will effectively see a wave with momentum k'. We therefore write f(k,k') to mean the same thing as f(k; θ, ϕ).

Suppose now that the wave scatters off a potential which is localised at some other position, r = R. Then the equation (2.46) becomes ψ(r) ∼ e^{ik·(r-R)} + f(k,k') e^{ik|r-R|}/|r-R| For r → ∞, we can expand |r-R| = (r^2 + R^2 - 2r·R)^{1/2} ≈ r(1 - 2r·R/r^2)^{1/2} ≈ r - \hat{r}·R We then have ψ(r) ∼ e^{-ik·R} [ e^{ik·r} + f(k,k') e^{-i(k'-k)·R} e^{ikr}/r ]  (2.47)

The overall factor is unimportant, since our interest lies in the phase shift between the incident wave and the scattered wave. We see that we get an effective scattering amplitude f_eff(k; \hat{r}) = f(k,k') e^{iq·R} where we have defined the transferred momentum q = k - k' Now let’s turn to a lattice of points Λ. Ignoring multiple scatterings, the amplitude is simply the sum of the amplitudes from each lattice point f_Λ(k,k') = f(k,k') Σ_{R∈Λ} e^{iq·R}  (2.48)

However, we already discussed the sum Δ(q) = Σ_{R∈Λ} e^{iq·R} in Section 2.2.2. The sum has the nice property that it vanishes unless q lies in the reciprocal lattice Λ*. This is simple to see: since we have an infinite lattice it must be true that, for any vector R_0 ∈ Λ, Δ(q) ≡ Σ_{R∈Λ} e^{iq·R} = Σ_{R∈Λ} e^{iq·(R-R_0)} = e^{-iq·R_0} Δ(q)

This means that either e^{-iq·R_0} = 1 or Δ(q) = 0. The former result is equivalent to the statement that q ∈ Λ*. More generally, Σ_{R∈Λ} e^{iq·R} ≡ Δ(q) = V* Σ_{Q∈Λ*} δ(q-Q)  (2.49)

where V* is the volume of the unit cell of Λ*. We see that Δ(q) is very strongly (formally, infinitely) peaked on the reciprocal lattice.

The upshot of this discussion is a lovely result: there is scattering from a lattice if and only if k - k' ∈ Λ*  (2.50)

This is known as the Laue condition. If the scattered momentum does not satisfy this condition, then the interference between all the different scattering sites results in a vanishing wave. Only when the Laue condition is obeyed is this interference constructive and scattering observed.

Alternatively, the Laue condition can be viewed as momentum conservation, with the intuition — garnered from Section 2 — that the lattice can only absorb momentum in Λ⋆.

Solutions to the Laue condition are not generic. If you take a lattice with a fixed orientation and fire a beam with fixed k, chances are that there are no solutions to (2.50). To see this, consider the reciprocal lattice as shown in the left-hand panel of the figure. From the tip of k draw a sphere of radius k. This is sometimes known as the Ewald sphere and its surface gives the possible transferred momenta q = k − k′. There is scattering only if this surface passes through a point on the reciprocal lattice. To get scattering, we must therefore either find a wave to vary the incoming momentum k, or find a way to vary the orientation of the lattice. But when this is achieved, the outgoing photons k′ = k̂r sit only at very specific positions. In this way, we get to literally take a photograph of the reciprocal lattice! The resulting diffraction pattern for salt (NaCl) which has a cubic lattice structure is shown in the right-hand panel. The four-fold symmetry of the reciprocal lattice is clearly visible.

Figure 35: The Ewald sphere, drawn in the reciprocal lattice.

Figure 36: Salt.

2.4.1 The Bragg Condition

There is an equivalent phrasing of the Laue condition in real space. Suppose that the momentum vectors obey k−k′ = Q ∈ Λ⋆. Since Q is a lattice vector, so too is nQ for all n ∈ Z. Suppose that Q is minimal, so that nQ is not a lattice vector for any n < 1. Defining the angle θ by k·k′ = k²cosθ, we can take the square of the equation above to get

2k²(1−cosθ) = 4k²sin²(θ/2) = Q² ⇒ 2ksin(θ/2) = Q.

We can massage this further. The vector Q ∈ Λ⋆ defines a set of parallel planes in Λ. Known as Bragg planes, these are labelled by an integer n and defined by those a ∈ Λ which obey a·Q = 2πn. The distance between successive planes is d = 2π/Q. Furthermore, the wavevector k corresponds to a wavelength λ = 2π/k. We learn that the Laue condition written as the requirement that λ = 2dsin(θ/2).

Repeating this argument for vectors nQ with n ∈ Z, we get nλ = 2dsin(θ/2).

This is the Bragg condition. It has a simple interpretation. For n = 1, we assume that the wave scatters off two consecutive planes of the lattice, as shown in the figure. The wave which hits the lower plane travels an extra distance of 2x = 2dsin(θ/2). The Bragg condition requires this extra distance to coincide with the wavelength of light. In other words, it is the statement that waves reflecting off consecutive planes interfere constructively.

Figure 37: [Description of the Bragg scattering diagram, not provided in text]

The Bragg condition gives us licence to think about scattering of light off planes in the lattice, rather than individual lattice sites. Moreover, it tells us that the wavelength of light should be comparable to the atomic separation in the crystal. This means x-rays. The technique of x-ray crystallography was pioneered by Max von Laue, who won the 1914 Nobel prize. The Bragg law was developed by William Bragg, a fellow of Trinity and director of the Cavendish. He shared the 1915 Nobel prize in physics with his father, also William Bragg, for their development of crystallographic techniques. X-ray crystallography remains the most important technique to determine the structure of materials. Two examples of historical interest are shown in the figures. The picture on the left is something of an enigma since it has five-fold symmetry. Yet there are no Bravais lattices with this symmetry! The diffraction picture is revealing a quasi-crystal, an ordered but non-periodic crystal.

Figure 38: A quasi-crystal.

The image on the right was taken by Rosalind Franklin and is known as “photograph 51”. It provided a major, and somewhat controversial, hint to Crick and Watson in their discovery of the structure of DNA.

Figure 39: DNA, Photograph 51.

2.4.2 The Structure Factor

Many crystals are described by a repeating basis of atoms, where each group sits on an underlying Bravais lattice Λ. The atoms in the group are displaced from the vertex of the Bravais lattice by a vector d. We saw several examples of this in Section 2. In such a situation, the scattering amplitude (2.48) is replaced by

f(k,k′) = Δ(q) S(q)

where

S(q) = ∑_i f_i(k,k′) e^{iq·d_i}

We have allowed for the possibility that each atom in the basis has a different scattering amplitude f(k,k′). The function S(q) is called the geometric structure factor.

An Example: BCC Lattice

As an example, consider the BCC lattice viewed as a simple cubic lattice of size a, with two basis vectors sitting at d₁ = 0 and d₂ = a(1,1,1)/2. If we take the atoms on the points d₁ and d₂ to be identical, then the associated scattering amplitudes are also equal: f₁ = f₂ = f.

We know that the scattering amplitude is non-vanishing only if the transferred momentum q lies on the reciprocal lattice, meaning

q = (2π/a) (n₁, n₂, n₃), n_i ∈ Z

This then gives the structure factor

S(q) = f eiq·d1 +eiq·d2

= f (1+eiπ i ni ) = 2 n even 0 n odd

We see that not all points in the reciprocal lattice Λ⋆ contribute. If we draw the reciprocal, simple cubic lattice and delete the odd points, as shown in the right-hand figure, we find ourselves left with a FCC lattice. (Admittedly, the perspective in the figure isn’t great.) But this is exactly what we expect since it is the reciprocal of the BCC lattice.

Another Example: Diamond A diamond lattice consists of two, interlaced FCC lattices with basis vectors d = 0 and d = a(1,1,1). An FCC lattice has reciprocal lattice vectors b = 2π(−1,1,1), b = 2π(1,−1,1) and b = 2π(1,1,−1). For q = n b , the structure factor is

2 n = 0 mod 4 1+i n = 1 mod 4 S(q) = f ( 1+ei(π/2) i ni ) = i 0 n i = 2 mod 4 1−i n = 3 mod 4

2.4.3 The Debye-Waller Factor So far, we’ve treated the lattice as a fixed, unmoving object. But we know from our discussion in Section 4 that this is not realistic. The underlying atoms can move. We would like to know what effect this has on the scattering off a lattice.

Let’s return to our result (2.48) for the scattering amplitude off a Bravais lattice Λ,

f (k,k′) = f(k,k′) eiq·Rn

where f(k,k′) is the amplitude for scattering from each site, q = k−k′, and R ∈ Λ. Since the atoms can move, the position R are no longer fixed. We should replace

Rn → Rn +un(t)

where, as in Section 4, u describes the deviation of the lattice from equilibrium. In general, this deviation could arise from either thermal effects or quantum effects. In keeping with the theme of these lectures, we will restrict to the latter. But this is conceptually interesting: it means that the scattering amplitude includes the factor

∆ ˜ (q) = eiq·Rneiq·un

which is now a quantum operator. This is telling us something important. When a particle – whether photon or neutron – scatters off the lattice, it can now excite a phonon mode. The scattering amplitude is a quantum operator because it includes all possible end-states of the lattice.

This opens up a whole slew of new physics. We could, for example, now start to compute inelastic scattering, in which the particle deposits some energy in the lattice. Here, however, we will content ourselves with elastic scattering, which means that the the lattice sits in its ground state |0⟩ both before and after the scattering. For this, we need to compute

∆ ˜ (q) = eiq·Rn⟨0|eiq·un(t)|0⟩

To proceed, we need the results of Section 4.1.4 in which we treated lattice vibrations quantum mechanically. For simplicity, let’s consider a simple cubic lattice so that the the matrix element above factorises into terms in the x, y and z direction. For each of these, we can use the formalism that we developed for the one-dimensional lattice.

The matrix element ⟨0|eiq·un|0⟩ is independent of time and is also translationally invariant. This means that we can evaluate it at t = 0 and at the lattice site n = 0. For a one-dimensional lattice with N sites, the expansion (4.11) gives

u = a(k)+a†(k) ≡ A+A†

Here we’ve used the rescaling (4.14) so that the creation and annihilation operators obey the usual commutation relations [a(k),a†(k′)] = δk,k′. The operators a†(k) create a phonon with momentum k and energy ω(k). The operators A and A† then obey

[A,A†] =

Our goal now is to compute ⟨0|eiq(A+A†)|0⟩. For this we use the BCH formula,

eiq(A+A†) = eiqA†eiqAe − 1 q2[A†,A]

But the ground state of the lattice is defined to obey a |0⟩ = 0 for all l. This means that eiqA|0⟩ = |0⟩. We end up with the result

⟨0|eiq·u0|0⟩ = e−W(q) where W(q) =

This is called the Debye-Waller factor. We see that the scattering amplitude becomes

f (k,k′) = e−W(q)f(k,k′)∆(q)

Note that, perhaps surprisingly, the atomic vibrations do not broaden the Bragg peaks away from q ∈ Λ⋆. Instead, they only diminish their intensity.

## 3. Electron Dynamics in Solids

In the previous chapter we have seen how the single-electron energy states form a band structure in the presence of a lattice. Our goal now is to understand the consequences of this, so that we can start to get a feel for some of the basic properties of materials. There is one feature in particular that will be important: materials don’t just have one electron sitting in them. They have lots. A large part of condensed matter physics is concerned with in understanding the collective behaviour of this swarm of electrons. This can often involve the interactions between electrons giving rise to subtle and surprising effects. However, for our initial foray into this problem, we will make a fairly brutal simplificati We will ignore the interactions between electrons. Ultimately, much of the basic physics that we describe below is unchanged if we turn on interactions, although the reason for this turns out to be rather deep.

## 3.1 Fermi Surfaces

Even in the absence of any interactions, electrons are still affected by the presence of others. This is because electrons are fermions, and so subject to the Pauli exclusion principle. This is the statement that only one electron can sit in any given state. As we will see below, the Pauli exclusion principle, coupled with the general features of band structure, goes some way towards explaining the main properties of materials.

Free Electrons As a simple example, suppose that we have no lattice. We take a cubic box, with sides of length L, and throw in some large number of electrons. What is the lowest energy state of this system? Free electrons sit in eigenstates with momentum ℏk and energy E = ℏ²k²/2m. Because we have a system of finite size, momenta are quantised as k = 2πn / L. Further, they also carry one of two spin states, |↑⟩ or |↓⟩.

The first electron can sit in the state k = 0 with, say, spin |↑⟩. The second electron can also have k = 0, but must have spin |↓⟩, opposite to the first. Neither of these electrons costs any energy. However, the next electron is not so lucky. The minimum energy state it can sit in has n = (1,0,0). Including spin and momentum there are a total of six electrons which can carry momentum |k| = 2π/L. As we go on, we fill out a ball in momentum space. This ball is called the Fermi sea and the boundary of the ball is called the Fermi surface. The states on the Fermi surface are said to have Fermi momentum ℏk_F and Fermi energy E_F = ℏ²k_F²/2m. Various properties of the free Fermi sea are explored in the lectures on Statistical Physics.

3.1.1 Metals vs Insulators Here we would like to understand what becomes of the Fermi sea and, more importantly, the Fermi surface in the presence of a lattice. Let’s recapitulate some important facts that we’ll need to proceed: • A lattice causes the energy spectrum to split into bands. We saw in Section 2.3.2 that a Bravais lattice with N sites results in each band having N momentum states. These are either labelled by momenta in the first Brillouin zone (in the reduced zone scheme) or by momentum in successive Brillouin zones (in the extended zone scheme).

• Because each electron carries one of two spin states, each band can accommodate 2N electrons.

• Each atom of the lattice provides an integer number of electrons, Z, which are free to roam the material. These are called valence electrons and the atom is said to have valence Z.

From this, we can piece the rest of the story together. We’ll discuss the situation for two-dimensional square lattices because it’s simple to draw the Brillouin zones. But everything we say carries over for more complicated lattices in three-dimensions.

Suppose that our atoms have valence Z = 1. There are then N electrons, which can be comfortably housed inside the first Brillouin zone. In the left-hand of Figure 43 we have drawn the Fermi surface for free electrons inside the first Brillouin zone. However, we know that the effect of the lattice is to reduce the energy at the edges of the Brillouin zone. We expect, therefore, that the Fermi surface — which is the equipotential E — will be distorted as shown in the middle figure, with states closer to the edge of the Brillouin zone filled preferentially. Note that the area inside the Fermi surface remains the same.

If the effects of the lattice get very strong, it may be that the Fermi surface touches the edge of the Brillouin zone as shown in the right-hand drawing in Figure 43. Because the Brillouin zone is a torus, if the Fermi surface is to be smooth then it must hit the edge of the Brillouin zone at right-angles.

This same physics can be seen in real Fermi surfaces. Lithium has valence Z = 1. It forms a BCC lattice, and so the Brillouin zone is FCC. Its Fermi surface is shown above, plotted within its Brillouin zone. Copper also has valency Z = 1, with a FCC lattice and hence BCC Brillouin zone. Here the effects of the lattice are somewhat stronger, and the Fermi surface touches the Brillouin zone.

In all of these cases, there are unoccupied states with arbitrarily small energy above E_F. (Strictly speaking, this statement holds only in the limit L → ∞ of an infinitely large lattice.) This means that if we perturb the system in any way, the electrons will easily be able to respond. Note, however, that only those electrons close to the Fermi surface can respond; those that lie deep within the Fermi sea are locked there by the Pauli exclusion principle and require much larger amounts of energy if they wish to escape.

This is an important point, so I’ll say it again. In most situations, only those electrons which lie on the Fermi surface can actually do anything. This is why Fermi surfaces play such a crucial role in our understanding of materials.

2This,andotherpicturesofFermisurfaces,aretakenfromhttp://www.phys.ufl.edu/fermisurface/.

– 82 – Figure 46: Fermi surfaces for valence Z = 2 with increasing lattice strength, moving from a metal to an insulator.

Materials with a Fermi surface are called metals. Suppose, for example, that we apply a small electric field to the sample. The electrons that lie at the Fermi surface can move to different available states in order to minimize their energy in the presence of the electric field. This results in a current that flows, the key characteristic of a metal. We’ll discuss more about how electrons in lattices respond to outside influences in Section 3.2 Before we move on, a couple of comments: • The Fermi energy of metals is huge, corresponding to a temperature of E /k ∼ F B 104 K, much higher than the melting temperature. For this reason, the zero temperature analysis is a good starting point for thinking about real materials.

• Metals have a very large number of low-energy excitations, proportional to the area of the Fermi surface. This makes metals a particularly interesting theoretical challenge.

Let’s now consider atoms with valency Z = 2. These have 2N mobile electrons, exactly the right number to fill the first band. However, in the free electron picture, this is not what happens. Instead, they partially fill the first Brillouin zone and then spill over into the second Brillouin zone. The resulting Fermi surface, drawn in the extended zone scheme, is shown in left-hand picture of Figure 46 If the effects of the lattice are weak, this will not be greatly changed. Both the first and second Brillouin zones Figure 47: Beryllium will have available states close to the Fermi surface as shown in the middle picture. These materials remain metals. We sometimes talk – 83 – 3 3 3 3 1 1st zone 3rd zone 2 2 3 3 3 3 2nd zone 3rd zone re−drawn Figure 48: Fermi surfaces for valence Z = 3.

of electrons in the second band, and holes (i.e. absence of electrons) in the first band.

We will discuss this further in Section 3.2. Beryllium provides an example of a metal with Z = 2; its Fermi surface is shown in the figure, now plotted in the reduced zone scheme. It includes both an electron Fermi surface (the cigar-like shapes around the edge) and a hole Fermi surface (the crown in the middle).

Finally, if the effects of the lattice become very strong, the gap between the two bands is large enough to overcome the original difference in kinetic energies. This occurs when the lowest lying state in the second band is higher than the highest state in the first. Now the electrons fill the first band. The second band is empty. The Fermi sea looks like the right-hand picture in Figure 46. This is qualitatively different from previous situations. There is no Fermi surface and, correspondingly, no low-energy excitations. Any electron that wishes to change its state can only do so by jumping to the next band. But that costs a finite amount of energy, equal to the gap between bands. This means that all the electrons are now locked in place and cannot respond to arbitrarily small outside influences. We call such materials insulators. (Sometimes they are referred to as band insulators to highlight the fact that it is the band structure which prevents the electrons from moving.)

This basic characterisation remains for higher valency Z. Systems with partially filled bands are metals; systems with only fully-filled bands are insulators. Note that a metal may well have several fully-filled bands, before we get to a partially filled band.

In such circumstances, we usually differentiate between the fully-filled lower bands — which are called valence bands — and the partially filled conduction band.

– 84 – The Fermi surfaces may exist in several different bands. An example of a Fermi surface for Z = 3 is shown in Figure 48, the first three Brillouin zones are shown separately in the reduced zone scheme. At first glance, it appears that the Fermi surface in the 3rd Brillouin zone is disconnected. However, we have to remember that the edges of the Brillouin zone are identified. Re-drawn, with the origin taken to be k = (π/a,π/a), we see the Fermi surface is connected, taking the rosette shape shown.

Looking Forwards We have seen how band structure allows us to classify all materials as metals or in- sulators. This, however, is just the beginning, the first chapter in a long and detailed story which extends from physics into materials science. To whet the appetite, here are three twists that we can add to this basic classification.

• For insulators, the energy required to reach the first excited state is set by the band gap ∆ which, in turn, is determined by microscopic considerations. Materi- als whose band gap is smaller than ∆ ≲ 2 eV or so behave as insulators at small temperature, but starts to conduct at higher temp At elevated temperatures, electrons are thermally excited from the valence band to the conduction band. Such materials are called semiconductors. They have the property that their conductivity increases as the temperature increases. (This is in contrast to metals whose conductivity decreases as temperature increases.) John Bardeen, Walter Brattain and William Shockley won the 1956 Nobel prize for developing their understanding of semiconductors into a working transistor. This, then, changed the world.

• There are some materials which have Z = 1 but are, nonetheless, insulators. An example is nickel oxide NiO. This contradicts our predictions using elementary band structure. The reason is that, for these materials, we cannot ignore the interactions between electrons. Roughly speaking, the repulsive force dominates the physics and effectively prohibits two electrons from sitting on the same site, even if they have different spins. But with only one spin state allowed per site, each band houses only N electrons. Materials with this property are referred to as Mott insulators. Nevill Mott, Cavendish professor and master of Caius, won the 1977 Nobel prize, in part for this discovery.

• For a long time band insulators were considered boring. The gap to the first excited state means that they can’t do anything when prodded gently. This attitude changed relatively recently when it was realised that you can be boring in different ways. There is a topological classification of how the phase of the quantum states winds as you move around the Brillouin zone. Materials in which this winding is non-trivial are called topological insulators. They have wonderful and surprising properties, most notably on their edges where they come alive with interesting and novel physics. David Thouless and Duncan Haldane won the 2016 Nobel prize for their early, pioneering work on this topic.

More generally, there is a lesson above that holds in a much wider context. Our classification of materials into metals and insulators hinges on whether or not we can excite a multi-electron system with an arbitrarily small cost in energy. For insulators, this is not possible: we require a finite injection of energy to reach the excited states. Such systems are referred to as gapped, meaning that there is finite energy gap between the ground state and first excited state. Meanwhile, systems like metals are called gapless. Deciding whether any given quantum system is gapped or gapless is one of the most basic questions we can ask. It can also be one of the hardest. For example, the question of whether a quantum system known as Yang-Mills theory has a gap is one of the six unsolved millennium maths problems.

3.1.2 The Discovery of Band Structure

Much of the basic theory of band structure was laid down by Felix Bloch in 1928 as part of his doctoral thesis. As we have seen, Bloch’s name is attached to large swathes of the subject. He had an extremely successful career, winning the Nobel prize in 1952, working as the first director-general of CERN, and building the fledgling physics department at Stanford University.

However, Bloch missed the key insight that band structure explains the difference between metals and insulators. This was made by Alan Wilson, a name less well known to physicists. Wilson was a student of Ralph Fowler in Cambridge. In 1931, he took up a research position with Heisenberg and it was here that he made his important breakthrough. He returned on a visit to Cambridge to spread the joy of his newfound discovery, only to find that no one very much cared. At the time, Cambridge was in the thrall of Rutherford and his motto: “There are two kinds of science, physics and stamp collecting”. And when Rutherford said “physics”, he meant “nuclear physics”.

This, from Nevill Mott, “I first heard of [Wilson’s discovery] when Fowler was explaining it to Charles Ellis, one of Rutherford’s closest collaborators, who said ‘very interesting’ in a tone which implied that he was not interested at all. Neither was I.”

Nevill Mott went on to win the Nobel prize for generalising Wilson’s ideas. Wilson himself didn’t do so badly either. He left academia and moved to industry, rising to become chairman of Glaxo.

3.1.3 Graphene

Graphene is a two-dimensional lattice of carbon atoms, arranged in a honeycomb structure as shown in the figure. Although it is straightforward to build many layers of these lattices — a substance known as graphite — it was long thought that a purely two-dimensional lattice would be unstable to thermal fluctuations and impossible to create. This changed in 2004 when Andre Geim and Konstantin Novoselov at the University of Manchester succeeded in isolating two-dimensional graphene. For this, they won the 2010 Nobel prize. As we now show, the band structure of graphene is particularly interesting.

First, some basic lattice facts. We described the honeycomb lattice in Section 2.2.1.

It is not Bravais. Instead, it is best thought of as two triangular sublattices. We define the primitive lattice vectors √ √ 3a √ 3a √ a = ( 3,1) and a = ( 3,−1)

1 2 2 2 where a the distance between neighbouring atoms, which in graphene is about a ≈ 1.4×10−10 m. These lattice vectors are shown in the figure.

Sublattice A is defined as all the points r = n a +n a with n ∈ Z. These are the 1 1 2 2 i red dots in the figure. Sublattice B is defined as all points r = n a +n a +d with 1 1 2 2 d = (−a,0). These are the white dots.

The reciprocal lattice is generated by vectors b satisfying a ·b = 2πδ . These are j i j ij 2π √ 2π √ b = (1, 3) and b = (1,− 3)

1 2 3a 3a – 87 – This reciprocal lattice is also triangular, rotated 90◦ from the orig- b inal. The Brillouin zone is constructed in the usual manner by drawing perpendicular boundaries between the origin and each other point in the reciprocal lattice. This is shown in the figure.

K’ We shortly see that the corners of the Brillouin zone carry par- ticular interest. It naively appears that there are 6 corners, but b this should really be viewed as two sets of three. This follows be- cause any points in the Brillouin zone which are connected by a Figure 51: reciprocal lattice vector are identified. Representatives of the two, inequivalent corners of the Brillouin zone are given by (cid:18) (cid:19) (cid:18) (cid:19)

1 2π 1 1 2π 1 K = (2b +b ) = 1, √ and K′ = (b +2b ) = 1,−√ (3.1)

1 2 1 2 3 3a 3 3 3a 3 These are shown in the figure above.

Tight Binding for Graphene The carbon atoms in graphene have valency Z = 1, with the p -atomic orbital aban- doned by their parent ions and free to roam the lattice. In this context, it is usually called the π-orbital. We therefore write down a tight-binding model in which this elec- troncanhopfromoneatomicsitetoanother. Wewillworkonlywithnearestneighbour interactions which, for the honeycomb lattice, means that the Hamiltonian admits hop- ping from a site of the A-lattice to the three nearest neighbours on the B-lattice, and vice versa. The Hamiltonian is given by (cid:88) (cid:104) (cid:105)

H = −t |r;A⟩⟨r;B|+|r;A⟩⟨r+a ;B|+|r;A⟩⟨r+a ;B|+h.c. (3.2)

1 2 r∈Λ where we’re using the notation |r;A⟩ = |r⟩ and |r;B⟩ = |r+d⟩ with d = (−a,0)

Comparing to (2.34), we have set E = 0, on the grounds that it doesn’t change any of the physics. For what it’s worth, t ≈ 2.8 eV in graphene, although we won’t need the precise value to get at the key physics.

The energy eigenstates are again plane waves, but now with a suitable mixture of A and B sublattices. We make the ansatz 1 (cid:88) (cid:16) (cid:17)

|ψ(k)⟩ = √ eik·r c |r;A⟩+c |r;B⟩ A B 2N r∈Λ – 88 – Plugging this into the Schro¨dinger equation, we find that c and c must satisfy the A B eigenvalue equation (cid:32) (cid:33)(cid:32) (cid:33) (cid:32) (cid:33)

0 γ(k) c c A A = E(k) (3.3)

γ⋆(k) 0 c c B B where (cid:16) (cid:17)

γ(k) = −t 1+eik·a1 +eik·a2 The energy eigenvalues of (3.3) are simply E(k) = ±|γ(k)| We can write this as (cid:12) (cid:32)√ (cid:33)(cid:12)2 (cid:12) (cid:12)2 (cid:12) 3k a (cid:12)

E(k)2 = t2(cid:12)1+eik·a1 +eik·a2(cid:12) = t2(cid:12)1+2e3ikxa/2 cos y (cid:12)

(cid:12) (cid:12) (cid:12) 2 (cid:12)

(cid:12) (cid:12)

Expanding this out, we get the energy eigenvalues (cid:118) (cid:117) (cid:18) (cid:19) (cid:32)√ (cid:33) (cid:32)√ (cid:33)

(cid:117) 3k a 3k a 3k a E(k) = ±t(cid:116)1+4cos x cos y +4cos2 y 2 2 2 Note that the energy spectrum is a double cover of the first Brillouin zone, symmetric about E = 0. This doubling can be traced to the fact that the honeycomb lattice consists of two intertwined Bravais lattices. Because the carbon atoms have valency Z = 1, only the lower band with E(k) < 0 will be filled.

The surprise of graphene is that these two bands meet at special points. These occur on the corners k = K and k = K′ (3.1), where cos(3k a/2) = −1 and cos( 3k a/2) = x y 1/2. The resulting band structure is shown in Figure 523. Because the lower band is filled, the Fermi surface in graphene consists of just two points, K and K′ where the bands meet. It is an example of a semi-metal.

Emergent Relativistic Physics The points k = K and K′ where the bands meet are known as Dirac points. To see why, we linearise about these points. Write k = K+q 3The image is taken from the exciting-code website.

– 89 – Figure 52: The band structure of graphene.

A little Taylor expansion shows that in the vicinity of the Dirac points, the dispersion relation is linear 3ta E(k) ≈ ± |q| But this is the same kind of energy-momentum relation that we meet in relativistic physics for massless particles! In that case, we have E = |p|c where p is the momentum and c is the speed of light. For graphene, we have E(k) ≈ ℏv |q| whereℏqisthemomentummeasuredwithrespecttotheDiracpointandv = 3ta/2ℏis thespeedatwhichtheexcitationspropagate. Ingraphene,v isabout300timessmaller than the speed of light. Nonetheless, it remains true that the low-energy excitations of graphene are gov 由相同的方程支配，这些方程我们在相对论量子场论中也会遇到。这部分解释了人们对石墨烯感到兴奋的原因：我们可以在简单的桌面实验中测试量子场论的思想。

我们可以通过回到哈密顿量(3.2)来更深入地探究其相对论结构。在狄拉克点k = K附近，我们有 γ(k) = -t[1 - 2e^(3iq_xa/2) cos((√3 q_y a)/2)]

= -t[1 - 2e^(3iq_xa/2)(cos((√3 q_y a)/2) - (√3/2) sin((√3 q_y a)/2))]

≈ -t[1 - 2(1 + (3iq_xa)/4 + ...)(1 - (3q_y^2 a^2)/8 + ...)]

≈ v_F ℏ (iq_x - q_y)

这意味着在狄拉克点k = K附近的哈密顿量形式为 H = v_F ℏ [0, iq_x - q_y; -iq_x - q_y, 0] = -v_F ℏ(q_x σ_y + q_y σ_x) (3.4)

其中σ_x和σ_y是泡利矩阵。但这就是一个无质量粒子在二维空间中运动的狄拉克方程，有时被称为泡利方程。（注意：我们最初选择的蜂窝晶格方向导致了这个略显繁琐的哈密顿量表达式。如果我们一开始就旋转90°，就会得到更简洁的H = ℏ v_F q·σ，其中σ = (σ_x, σ_y)。）

这里存在某种讽刺。在原始的狄拉克方程中，2×2矩阵结构源于电子携带自旋。但(3.4)中矩阵结构的起源并非如此。实际上，我们在讨论中从未提及自旋。相反，在石墨烯中，涌现的“自旋”自由度来自于两个A和B子晶格的存在。

在另一个狄拉克点附近，我们会得到非常相似的方程。展开k = K' + q'，得到相应的哈密顿量 H = -v_F ℏ(q_x σ_y - q_y σ_x)

符号的差异有时被称为不同的手性或螺旋性。你将在量子场论讲座的高能物理学中学到更多关于此的内容。

如上所述，我们尚未包含电子的自旋。这很简单：上述讨论只需重复两次，一次对应自旋|↑⟩，一次对应自旋|↓⟩。结论是石墨烯的低能激发由四个无质量的狄拉克费米子描述。一对来自电子的自旋简并；另一对来自两个狄拉克点K和K'的存在，有时被称为谷简并。

## 3.2 布洛赫电子的动力学

在本节中，我们更仔细地研究晶格环境中运动的电子如何对外力做出反应。我们称这些电子为布洛赫电子。我们首先描述一些熟悉的量如何为布洛赫电子重新定义。

为简化起见，考虑一个绝缘体并加入一个额外的电子。这个孤立的电子独自位于一个原本未占据的能带中。它可占据的状态具有能量E(k)，其中k位于第一布里渊区。（能量还应该有一个进一步的离散指标来标记电子所在的特定能带，但我们在下文中会略去这一点。）尽管处于这种环境中，我们仍然可以为这个电子分配一些标准属性。

3.2.1 速度电子的平均速度v为 v = (1/ℏ) ∂E/∂k (3.5)

首先注意，这正是波包的群速度（一个我们之前在电磁学讲座中遇到的概念）。然而，“平均速度”在量子力学中有特定含义，要证明(3.5)，我们应该直接计算v = ⟨ψ|(-iℏ∇)|ψ⟩。

布洛赫定理确保电子本征态具有形式 ψ_k(x) = e^(ik·x) u_k(x)

其中k在布里渊区内。与能量一样，我们略去了波函数上的离散能带指标。完整的波函数满足Hψ_k(x) = E(k)ψ_k(x)，因此u_k(x)服从 H_k u_k(x) = E(k)u_k(x)，其中H_k = (-i∇ + k)²/(2m) + V(x) (3.6)

我们将使用一个巧妙的技巧。考虑哈密顿量H_{k+q}，将其展开为 H_{k+q} = H_k + q·(∂H/∂k) + (1/2) q_i q_j (∂²H/∂k_i ∂k_j) (3.7)

对于小的q，我们将此视为对H_k的微扰。根据一阶微扰理论的结果，我们知道能量本征值的偏移量为 ΔE = ⟨u_k| (∂H/∂k)·q |u_k⟩ 但我们确切知道结果：它就是E(k+q)。将其在q中展开到一阶，我们得到结果 ⟨u_k| (∂H/∂k) |u_k⟩ = ∂E/∂k 但这正是我们需要的。使用(3.6)的H_k表达式，左边是 (ℏ²/m) ⟨u_k|(-i∇ + k)|u_k⟩ = (ℏ/m) ⟨ψ_k|(-iℏ∇)|ψ_k⟩ = ℏ v 这给出了我们期望的结果(3.5)。

令人惊讶的是，晶体中的本征态具有固定的平均速度。人们可能天真地认为粒子会与晶体碰撞，四处弹跳，相应的平均速度会消失。然而布洛赫定理的美妙之处在于事实并非如此。电子可以相当愉快地滑过晶体结构。

满带既不载流也不传热在继续之前，我们可以利用上述结果来证明…… ove a simple result: a completely filled band does not contribute to the current. This is true whether the filled band is part of an insulator, or part of a metal. (In the latter case, there will also be a partially filled band which will contribute to the current.)

The current carried by each electron is j = −ev where −e is the electron charge. From (3.5), the total current of a filled band is then

j = − 2e ∫(BZ) d³k/(2π)³ ∂E/∂k  (3.8)

where the overall factor of 2 counts the spin degeneracy. This integral vanishes. This follows because E(k) is a periodic function over the Brillouin zone and the total derivative of any periodic function always integrates to zero.

Alternatively, if the crystal has an inversion symmetry then there is a more direct proof. The energy satisfies E(k) = E(−k), which means that ∂E(k)/∂k = −∂E(−k)/∂k and the contributions to the integral cancel between the two halves of the Brillouin zone.

The same argument shows that a filled band cannot transport energy in the form of heat. The heat current is defined as

j = 2 ∫(BZ) d³k/(2π)³ ½ E²v = ∫(BZ) d³k/(2π)³ E ∂(E²)/∂k

which again vanishes when integrated over a filled band. This means that the electrons trapped in insulators can conduct neither electricity nor heat. Note, however, that while there is nothing else charged that can conduct electricity, there are other degrees of freedom – in particular, phonons – which can conduct heat.

3.2.2 The Effective Mass

We define the effective mass tensor to be

m*ij = ℏ² (∂²E/∂ki∂kj)−1

where we should view the right-hand side as the inverse of a matrix.

For simplicity, we will mostly consider isotropic systems, for which m*ij = m*δij and the effective mass of the electron is given by

m* = ℏ² (∂²E/∂k²)−1  (3.9)

where the derivative is now taken in any direction. This definition reduces to something very familiar when the electron sits at the bottom of the band, where we can Taylor expand to find

E = Emin + ℏ²|k−kmin|²/(2m*) + ...

This is the usual dispersion relation for a non-relativistic particle.

The effective mass m* has more unusual properties higher up in the band. For a typical band structure, m* becomes infinite at some point in the middle, and is negative close to the top of the band. We'll see how to interpret this negative effective mass in Section 3.2.4.

In most materials, the effective mass m* near the bottom of the band is somewhere between 0.01 and 10 times the actual mass of the electron. But there are exceptions. Near the Dirac point, graphene has an infinite effective mass by the definition (3.9), although this is more because we've used a non-relativistic definition of mass which is rather daft when applied to graphene. More pertinently, there are substances known, appropriately, as heavy fermion materials where the effective electron mass is around a 1000 times heavier than the actual mass.

A Microscopic View on the Effective Mass

We can get an explicit expression for the effective mass tensor m*ij in terms of the microscopic electron states. This follows by continuing the slick trick we used above, now thinking about the Hamiltonian (3.7) at second order in perturbation theory. This time, we find the inverse mass matrix is given by

(m*)−1ij = δij/m + (1/m²) Σn′≠n ⟨ψn,k|pi|ψn′,k⟩⟨ψn,k|pj|ψn′,k⟩/(En(k)−En′(k)) − h.c.

where n labels the band of each state. Note that the second term takes the familiar form that arises in second order perturbation theory. We see that, microscopically, the additional contributions to the effective mass come from matrix elements between different bands. Nearby bands of a higher energy give a negative contribution to the effective mass; nearby bands of a lower energy give a positive contribution.

3.2.3 Semi-Classical Equation of Motion

Suppose now that we subject the electron to an external potential force of the form F = −∇U(x). The correct way to proceed is to add U(x) to the Hamiltonian and solve again for the eigenstates. However, in many circumstances, we can work semi-classically. For this, we need that U(x) is small enough that it does not distort the band structure and, moreover, does not vary greatly over distances comparable to the lattice spacing.

We continue to restrict attention to the electron lying in a single band. To proceed, we should think in terms of wavepackets, rather than plane waves. This means that the electron has some localised momentum k and some localised position x, within the bounds allowed by the Heisenberg uncertainty relation. We then treat this wavepacket as if it was a classical particle, where the position x and momentum ℏk depend on time. This is sometimes referred to as a semi-classical approach.

The total energy of this semi-classical particle is E(k)+U(x) where E(k) is the band energy. The position and momentum evolve such that the total energy is conserved. This gives

d/dt (E(k(t))) )+U(x(t)) = · +∇U · = v· ℏ +∇U = 0 dt ∂k dt dt dt which is satisfied when dk ℏ = −∇U = F (3.10)

dt This should be viewed as a variant of Newton’s equation, now adapted to the lattice environment. In fact, we can make it look even more similar to Newton’s equation. For an isotropic system, the effective “mass times acceleration” is dv m⋆ d ( ∂E ) m⋆ ( dk ∂ ) ∂E dk m⋆ = = · = ℏ = F (3.11)

dt ℏ dt ∂k ℏ dt ∂k ∂k dt where you might want to use index notation to convince yourself of the step in the mid- dle where we lost the effective mass m⋆. It’s rather nice that, despite the complications of the lattice, we still get to use some old equations that we know and love. Of course, the key to this was really the definition (3.9) of what we mean by effective mass m⋆.

An Example: Bloch Oscillations Consider a Bloch electron, exposed to a constant electric field E. The semi-classical equation of motion is eE ℏk ˙ = −eE ⇒ k(t) = k(0)− t So the crystal momentum k increases linearly. At first glance, this is unsurprising. But it leads to a rather surprising effect. This is because k is really periodic, valued in the Brillouin zone. Like a character in a 1980s video game, when the electron leaves one edge of the Brillouin zone, it reappears on the other side.

We can see what this means in terms of velocity.

For a typical one-dimensional band structure shown on the right, the velocity v ∼ k in the middle of the band, but v ∼ −k as the particle approaches the edge of the Brillouin zone. In other words, a constant electric field gives rise to an oscillating velocity, and hence an oscillat- ing current! This surprising effect is called Bloch oscilla- tions.

As an example, consider a one-dimensional system with a tight-binding form of band structure E = −Ccos(ka)

Then the velocity in a constant electric field oscillates as ( )

Ca Ca eEa v(k) = sin(ka) = − sin t ℏ ℏ ℏ The Bloch frequency is ω = eEa/ℏ. If we construct a wavepacket from several different energy eigenstates, then the position of the particle will similarly oscillate back and forth. This effect was first predicted by Leo Esaki in 1970.

Bloch oscillations are somewhat counterintuitive. They mean that a DC electric field applied to a pure crystal does not lead to a DC current! Yet we’ve all done experiments in school where we measure the DC current in a metal! This only arises because a metal is not a perfect crystal and the electrons are scattered by impurities or thermal lattice vibrations (phonons) which destroy the coherency of Bloch oscillations and lead to a current.

Bloch oscillations are delicate. The system must be extremely clean so that the particle does not collide with anything else over the time necessary to see the oscillations. This is too much to ask in solid state crystals. However, Bloch oscillations have been observed in other contexts, such as cold atoms in an artificial lattice. The time variation of the velocity of Caesium atoms in an optical lattice is shown in the figure4.

3.2.4 Holes Consider a totally filled band, and remove one electron. We’re left with a vacancy in the otherwise filled band. In a zen-like manoeuvre, we ascribe properties to the absence of the particle. Indeed, as we will now see, this vacancy moves as if it were itself an independent particle. We call this particle a hole.

Recall that our definition (3.9) means that the effective mass of electrons is negative near the top of the band. Indeed, expanding around the maximum, the dispersion relation for electrons reads ℏ2 E(k) = E + |k−k |2 +...

max 2m⋆ max and the negative effective mass m⋆ < 0 ensures that electrons have less energy as the move away from the maximum.

Now consider filling all states except one. As the hole moves away from the maximum, it costs more energy (because we’re subtracting less energy!). This suggests that we should write the energy of the hole as ℏ2 E (k) = −E(k) = −E + |k−k |2 +...

hole max 2m⋆ max hole where m⋆ = −m⋆ hole so that the effective mass of the hole is positive near the top of the band, but becomes negative if the hole makes it all the way down to the bottom.

The hole has other properties. Suppose that we take away an electron with momen- tum k. Then the resulting hole can be thought of as having momentum −k. This suggests that we define k = −k (3.12)

hole However, the velocity of the hole is the same as that of the missing electron 1∂E 1∂E hole v = = = v hole ℏ ∂k ℏ ∂k hole This too is intuitive, since the hole is moving in the same direction as the electron that we took away.

The definitions above mean that the hole obeys the Newtonian force law with m⋆ hole = −F = F (3.13)

hole dt hole At first sight, this is surprising: the hole experiences an opposite force to the electron.

But there’s a very simple interpretation. The force that we typically wish to apply to our system is an electric field E which, for an electron, gives rise to F = −eE. The minus sign in (3.13) is simply telling us that the hole should be thought of as carrying charge +e, the opposite of the electron, F = +eE for the hole.

We can also reach this same conclusion by computing the current. We saw in (3.8) that a fully filled band carries no current. This means that the current carried by a partially filled band is j = −2e ∫ d³k/(2π)³ v(k) (filled) = +2e ∫ d³k/(2π)³ v(k) (unfilled). The filled states are electrons carrying charge −e; the unfilled states are holes, carrying charge +e.

Finally, it’s worth mentioning that the idea of holes in band structure provides a fairly decent analogy for anti-matter in high-energy physics. There too the electron has a positively charged cousin, now called the positron. In both cases, the two particles can come together and annihilate. In solids, this releases a few eV of energy, given by the gap between bands. In high-energy physics, this releases a million times more energy, given by the rest mass of the electron.

3.2.5 Drude Model Again The essence of Bloch’s theorem is that electrons can travel through perfect crystals unimpeded. And yet, in the real world, this does not happen. Even the best metals have a resistance, in which any current degrades and ultimately relaxes to zero. This happens because metals are not perfect crystals, and the electrons collide with impurities and vacancies, as well as thermally vibrations called phonons.

We can model these effects in our semi-classical description by working with the electron equation of motion called the Drude model m⋆ v̇ = −eE − (m⋆/τ)v (3.14). Here E is the applied electric field and τ is the scattering time, which should be thought of as the average time between collisions.

We have already met the Drude model in the lectures on Electromagnetism when we tried to describe the conductivity in metals classically. We have now included the quantum effects of lattices and the Fermi surface yet, rather remarkably, the equation remains essentially unchanged. The only difference is that the effective mass m⋆ will depend on k, and hence on v, if the electron is not close to the minimum of the band.

In equilibrium, the velocity of the electron is v = − (eτ/m⋆)E (3.15). The proportionality constant is called the mobility, µ = |eτ/m⋆|. The total current density j = −env where n is the density of charge carriers. The equation (3.15) then becomes j = σE where σ is the conductivity, σ = e²τn/m⋆ (3.16). We also define the resistivity ρ = 1/σ. This is the same result that we found in our earlier classical analysis, except the mass m is replaced by the effective mass m⋆.

There is, however, one crucial difference that the existence of the Fermi surface has introduced. When bands are mostly unfilled, it is best to think of the charge carriers in terms of negatively charged electrons, with positive effective mass m⋆. But when bands are mostly filled, it is best to think of the charge carriers in terms of positively charged holes, also with positive mass m⋆_hole. In this case, we should replace the Drude model (3.14) with the equivalent version for holes, m⋆_hole v̇ = +eE − (m⋆_hole/τ)v (3.17).

This means that certain materials can appear to have positive charge carriers, even though the only things actually moving are electrons. The different sign in the charge carrier doesn’t show up in the conductivity (3.16), which depends on e². To see it, we need to throw in an extra ingredient.

Hall Resistivity The standard technique to measure the charge of a material is to apply a magnetic field B. Classically, particles of opposite charges will bend in opposite directions, perpendicular to B. In a material, this results in the classical Hall effect.

We will discuss the motion of Bloch electrons in a magnetic field in much more detail in Section 3.3. (And we will discuss the Hall effect in much much more detail in other lectures.) Here, we simply want to show how this effect reveals the difference between electrons and holes. For electrons, we adapt the Drude model (3.14) by adding a Lorentz force, m⋆ v̇ = −e(E + v×B) − (m⋆/τ)v. We once again look for equilibrium solutions with v̇ = 0. Writing j = −nev, we now must solve the vector equation (1/ne)j×B + j/(ne²τ) = E.

The solution to this is E = ρj, where the resistivity ρ is now a 3×3 matrix. If we take B = (0,0,B), then we have ρ = [ρ_xx, ρ_xy, 0; -ρ_xy, ρ_xx, 0; 0, 0, ρ_xx], where the diagonal, longitudinal resistivity is ρ_xx = 1/σ where σ is given in (3.16). The novelty is the off-diagonal, Hall resistivity ρ_xy = −B/(ne). We often define the Hall coefficient R as R = ρ_xy/B = −1/(ne).

This, as promised, depends on the charge e. This means that if we were to repeat the above analysis for holes (3.17) rather than electrons, we would find a Hall coefficient which differs by a minus sign.

There are metals – such as beryllium and magnesium – whose Hall coefficient has the “wrong sign”. We drew the Fermi surface for beryllium in Section 3.1.1; it contains both electrons and holes. In this case, we should add two contributions with opposite signs. It turns out that the holes are the dominant charge carrier.

## 3.3 Bloch Electrons in a Magnetic Field

In this section, we continue our study of Bloch electrons, but now subjected to an external magnetic field B. (Note that what we call B should really be called H; it is the magnetising field, after taking into account any bound currents.) Magnetic fields play a particularly important role in solids because, as we shall see, they allow us to map out the Fermi surface.

3.3.1 Semi-Classical Motion

We again use our semi-classical equation of motion (3.10) for the electron, now with the Lorentz force law

$$ \hbar \frac{d\mathbf{k}}{dt} = -e\mathbf{v} \times \mathbf{B} \quad (3.18)

$$

where the velocity and momentum are once again related by

$$ \mathbf{v} = \frac{1}{\hbar} \frac{\partial E}{\partial \mathbf{k}} \quad (3.19)

$$

From these two equations, we learn two facts. First, the component of k parallel to B is constant: $d(\mathbf{k} \cdot \mathbf{B})/dt = 0$. Second, the electron traces out a path of constant energy in k-space. This is because

$$ \frac{dE}{dt} = \frac{\partial E}{\partial \mathbf{k}} \cdot \frac{d\mathbf{k}}{dt} = -e\mathbf{v} \cdot (\mathbf{v} \times \mathbf{B}) = 0 $$

These two facts are sufficient for us to draw the orbit in k-space.

The Fermi surface is, by definition, a surface of constant energy. The electrons orbit the surface, perpendicular to B. It’s pictured on the right for a spherical Fermi surface, corresponding to free electrons.

Holes have an opposite electric charge, and so traverse the Fermi surface in the opposite direction. However, we have to also remember that $\dot{\mathbf{k}}$ also has a relative minus sign (3.12). As an example, consider a metal with Z = 2, which has both electron and hole Fermi surfaces. In Figure 56, we have drawn the Fermi surfaces of holes (in purple) and electrons (in yellow) in the extended zone scheme, and shown their direction of propagation in a magnetic field.

Figure 55: hole

Holes in the first band Electrons in the second band

Figure 56: Pockets of electrons and holes for free electrons with Z = 2.

Orbits in Real Space

We can also look at the path $\mathbf{r}(t)$ that these orbits trace out in real space. Consider

$$ \hat{\mathbf{B}} \times \hbar \dot{\mathbf{k}} = -e\hat{\mathbf{B}} \times (\dot{\mathbf{r}} \times \mathbf{B}) = -eB \dot{\mathbf{r}} \quad (3.20)

$$

where $\mathbf{r}$ is the position of the electron, projected onto a plane perpendicular to B,

$$ \mathbf{r}_{\perp} = \mathbf{r} - (\mathbf{B} \cdot \mathbf{r}) \hat{\mathbf{B}} $$

Integrating (3.20), we find

$$ \mathbf{r}_{\perp}(t) = \mathbf{r}_{\perp}(0) - \frac{\hat{\mathbf{B}}}{eB} \times \big( \mathbf{k}(t) - \mathbf{k}(0) \big) \quad (3.21)

$$

In other words, the particle follows the same shape trajectory as in k-space, but rotated about B and scaled by the magnetic length $l^2 = \hbar/eB$. For free electrons, with a spherical Fermi surface, this reproduces the classical result that electrons move in circles. However, as the Fermi surface becomes distorted by band effects this need no longer be the case, and the orbits in real space are no longer circles. For example, the electrons trace out the rosette-like shape in the Z = 3 Fermi surface that we saw in Figure 48.

In extreme cases its possible for the real space orbits to not be closed curves at all. This happens, for example, if the Fermi surface is distorted more in one direction than another, so it looks like the picture on the right, with electrons performing a loop in the Brillouin zone. These are called open Fermi surfaces.

Figure 57:

3.3.2 Cyclotron Frequency

Let’s compute the time taken for the electron to complete a closed orbit in k-space. The time taken to travel between two points on the orbit $\mathbf{k} = \mathbf{k}(t_1)$ and $\mathbf{k} = \mathbf{k}(t_2)$ is given by the line integral

$$ t_2 - t_1 = \int_{\mathbf{k}_1}^{\mathbf{k}_2} \frac{d\mathbf{k}}{|\dot{\mathbf{k}}|} $$

We can use (3.20) to relate $|\dot{\mathbf{k}}|$ to the perpendicular velocity,

$$ |\dot{\mathbf{k}}| = \frac{eB}{\hbar} |\dot{\mathbf{r}}_{\perp}| = \frac{eB}{\hbar^2} \left| \frac{\partial E}{\partial \mathbf{k}_{\perp}} \right| $$

so we have

$$ t_2 - t_1 = \frac{\hbar^2}{eB} \int_{\mathbf{k}_1}^{\mathbf{k}_2} \frac{d\mathbf{k}}{|\partial E / \partial \mathbf{k}_{\perp}|} $$

This has a rather nice geometric interpretation. Consider two orbits, both lying in the same plane perpendicular to B, but with the second having a slightly higher Fermi energy $E+\Delta E$. To achieve this, the orbit must sit slightly outside the first, with momentum

$$ \mathbf{k}' = \mathbf{k} + \Delta(\mathbf{k}) \frac{\partial E}{\partial \mathbf{k}} $$

where, as the notation suggests, $\Delta(\mathbf{k})$ can change as we move around the orbit. We require that $\Delta(\mathbf{k})$ is such that the second orbit also has constant energy,

$$ \Delta E = \left| \frac{\partial E}{\partial \mathbf{k}} \right| \Delta(\mathbf{k})

$$

The time taken to traverse the orbit can then be written as

$$ t_2 - t_1 = \frac{\hbar^2}{eB \Delta E} \int_{\mathbf{k}_1}^{\mathbf{k}_2} \Delta(\mathbf{k}) d\mathbf{k} $$

But this is simply the area of the strip that separates the two orbits; this area, which we call $A_{12}$, is coloured in the figure. In the limit $\Delta E \to 0$, we have

$$ t_2 - t_1 = \frac{\hbar^2}{eB} \frac{\partial A_{12}}{\partial E} $$

We can now apply this formula to compute the time taken to complete a closed orbit. Let $A(E)$ denote the area enclosed by the orbit. (Note that this will depend not only on E but also on the component of the momentum $\mathbf{k} \cdot \mathbf{B}$ parallel to the magnetic field.) The time taken to complete an orbit is The cyclotron frequency is defined as \[ \omega_c = \frac{2\pi e B}{\hbar^2 \partial A(E)/\partial E} \qquad (3.22)

\]

One can check that the cyclotron frequency agrees with the usual result, $\omega = eB/m$, for free electrons.

The fact that the cyclotron frequency $\omega_c$ depends on some property of the Fermi surface – namely $\partial A/\partial E$ – is important because the cyclotron frequency is something that can be measured in experiments, since the electrons sit at resonance to absorb microwaves tuned to the same frequency. This gives us our first hint as to how we might measure properties of the Fermi surface.

**3.3.3 Onsager-Bohr-Sommerfeld Quantisation**

The combination of magnetic fields and Fermi surfaces gives rise to a host of further physics but to see this we will have to work a little harder.

The heart of the problem is that, in classical physics, the Lorentz force does no work. In the Hamiltonian formalism, this translates into the statement that the energy does not depend on $B$ when written in terms of the canonical momenta. Whenever the energetics of a system depend on the magnetic field, there must be some quantum mechanics going on underneath. In the present case, this means that we need to go slightly beyond the simple semi-classical description that we’ve met above, to find some of the discreteness that quantum mechanics introduces into the problem.

(As an aside: this problem is embodied in the Bohr-van-Leeuwen theorem, which states that there can be no classical magnetism. We describe how quantum mechanics can circumvent this in the discussion of Landau diamagnetism in the lectures on Statistical Physics.)

To proceed, we would ideally like to quantise electrons in the presence of both a lattice and a magnetic field. This is hard. We’ve learned how to quantise in the presence of a magnetic field in Section 1 and in the presence of a lattice in Section 2, but including both turns out to be a much more difficult problem. Nonetheless, as we now show, there’s a way to cobble together an approximation solution.

This cobbled-together quantisation was first proposed by Onsager, but follows an earlier pre-quantum quantisation of Bohr and Sommerfeld which suggests that, in any system, an approximation to the quantisation of energy levels can be found by setting \[ \oint \mathbf{p} \cdot d\mathbf{r} = \hbar (n + \gamma) \qquad (3.23)

\]

with $n \in \mathbb{Z}$ and $\gamma$ an arbitrary constant. This Bohr-Sommerfeld quantisation does not, in general, agree with the exact result from solving the Schrödinger equation. However, it tends to capture the correct physics for large $n$, where the system goes over to its semi-classical description.

In the present context, we apply Bohr-Sommerfeld quantisation to our semi-classical model (3.18) and (3.19). We have \[ \frac{1}{2\pi} \oint \mathbf{p} \cdot d\mathbf{r} = \frac{\hbar}{2\pi} \oint \mathbf{k} \cdot d\mathbf{r} = \frac{\hbar}{2\pi e B} \oint \mathbf{k} \cdot (d\mathbf{k} \times \mathbf{B})

\]

where, in the last equality, we have used our result (3.20). But this integral simply captures the cross-sectional area of the orbit in $\mathbf{k}$-space. This is the area $A(E)$ that we met above. We learn that the Bohr-Sommerfeld quantisation condition (3.23) leads to a quantisation of the cross-sectional areas of the Fermi surface in the presence of a magnetic field, \[ A_n = \frac{2\pi e B}{\hbar} (n + \gamma) \qquad (3.24)

\]

This quantisation of area is actually a variant of the Landau level quantisation that we met in Section 1.2. There are different ways of seeing this. First, note that, for fixed $k_z$, we can write the cyclotron frequency (3.22) as the difference between consecutive energy levels \[ \omega_c = \frac{2\pi e B}{\hbar^2} \frac{E_{n+1} - E_n}{A_{n+1} - A_n} = \frac{E_{n+1} - E_n}{\hbar} \]

Rearranging, this gives \[ E_n = \hbar \omega_c (n + \text{constant})

\]

which coincides with our Landau level spectrum (1.14), except that the old cyclotron frequency $\omega = eB/m$ has been replaced by $\omega_c$.

Alternatively, we could look at the quantisation of area in real space, rather than in $\mathbf{k}$-space. We saw in (3.21), that the orbit in real space has the same shape as that in $\mathbf{k}$-space, but is scaled by a factor of $l^2 = \hbar/eB$. This means that the flux through any such orbit is given by \[ \Phi_n = B A_n = \left( \frac{\hbar}{e B} \right) \cdot \frac{2\pi e B}{\hbar} (n + \gamma) \Phi_0 = (n + \gamma) \Phi_0 \qquad (3.25)

\]

where $\Phi_0 = 2\pi\hbar/e$ is the so-called quantum of flux. But this ties in nicely with our discussion in Section 1.2 of Landau levels in the absence of a lattice, where we saw that the degeneracy of states in each level is (1.17)

\[ N = \frac{B A}{\Phi_0} \]

which should clearly be an integer.

The quantisation (3.24) due to a background magnetic field results in a re-arrangement of the Fermi surface, which now sit in Landau tubes whose areas are quantised. A typical example is shown on the right. (Figure 59).

**3.3.4 Quantum Oscillations**

The formation of Landau tubes gives rise to a number of fairly striking experimental signatures.

Consider a Fermi surface with energy $E$ and a second surface slightly inside with energy $E - dE$. The region between these contains the accessible states if we probe the system with a small amount of energy $dE$. Now consider a Landau tube of cross-sectional area $A_n$, intersecting our Fermi surface. Typically, the Landau tube will intersect the Fermi surface only in some small region, as shown in left-hand picture of Figure...

This means that the number of states that can contribute to physical processes will be fairly small. In the language that we introduced in the Statistical Physics lectures, the density of states g(E) dE within this Landau tube will be small. However, something special happens if the area A happens to coincide with an extremal area of the Fermi surface. Because the Fermi surface curves much more slowly at such points, the density of states g(E) dE is greatly enhanced at this point. This is shown in the right-hand picture of Figure 60. In fact, one can show that the density of states actually diverges at this point as g(E) ∼ (E − E)−1/2.

Figure 60: Landau tubes intersecting the Fermi surface: when the area of the tube coincides with an extremal cross-section of the Fermi surface, there is a large enhancement in the available states.

We learn that when the area quantisation takes special values, there are many more electrons that can contribute to any physical process. However, the area quantisation condition (3.24) changes with the magnetic field. This means that as we increase the magnetic field, the areas of Landau tubes will increase and will, occasionally, overlap with an extremal area in the Fermi surface. Indeed, if we denote the extremal cross-sectional area of the Fermi surface as Aext, we must get an enhancement in the density of available states whenever A = (n+γ) 2πeB/ℏ = An for some n. We don’t know what γ is, but this doesn’t matter: the density of states should occur over and over again, at intervals given by ∆1/B = ℏ Aext / (2πe). Such oscillations are seen in a wide variety of physical measurements and go by the collective name of quantum oscillations.

The first, and most prominent example of quantum oscillation is the de Haas-van Alphen effect, in which the magnetisation M = −∂F/∂B varies with magnetic field. The experimental data for gold is shown in Figure 61. Note that there are two oscillation frequencies visible in the data. The Fermi surface of gold is shown on the right. For the oscillations above, the magnetic field is parallel to the neck of the Fermi surface, as shown in the figure. The two frequencies then arise because there are two extremal cross-sections – the neck and the belly. As the direction of the magnetic field is changed, different extremal cross-sections become relevant. In this way, we can map out the entire Fermi surface.

The magnetisation is not the only quantity to exhibit oscillations. In fact, the large enhancement in the density of states affects nearly all observables. For example, oscillations in the conductivity are known as the Shubnikov-de Haas effect. The experimental technique for measuring Fermi surfaces was pioneered by Brian Pippard, Cavendish professor and the first president of Clare Hall. Today, the techniques of quantum oscillations play an important role in attempts to better understand some of the more mysterious materials, such as unconventional superconductors.

Figure 61: dHvA oscillations for gold. The horizontal axis is B, plotted in kG.

## 4. Phonons

Until now, we’ve discussed lattices in which the atoms are fixed in place. This is, of course, somewhat unrealistic. In materials, atoms can jiggle, oscillating back and forth about their equilibrium position. The result of their collective effort is what we call sound waves or, at the quantum level, phonons. In this section we explore the physics of this jiggling.

## 4.1 Lattices in One Dimension

Much of the interesting physics can be illustrated by sticking to one-dimensional examples.

4.1.1 A Monotonic Chain

We start with a simple one-dimensional lattice consisting of N equally spaced, identical atoms, each of mass m. This is shown below. We denote the position of each atom as xn, with n = 1,...,N. In equilibrium, the atoms sit at x = na with a the lattice spacing.

The potential that holds the atoms in place takes the form V(xn − xn−1). For small deviations from equilibrium, a generic potential always looks like a harmonic oscillator. The deviation from equilibrium for the nth atom is given by un(t) = xn(t) − na. The Hamiltonian governing the dynamics is then a bunch of coupled harmonic oscillators H = Σn pn²/2m + λ/2 Σn (un − un−1)² (4.1) where pn = mµn and λ is the spring constant. (It is not to be confused with the wavelength.) The resulting equations of motion are mµ̈n = −λ(2un − un−1 − un+1) (4.2)

To solve this equation, we need to stipulate some boundary conditions. It’s simplest to impose periodic boundary conditions, extending n ∈ Z and requiring un+N = un. For N ≫ 1, which is our interest, other boundary conditions do not qualitatively change the physics. We can then write the solution to (4.2) as un = A e−iωt−ikna (4.3)

uation is linear, we can always take real and imaginary parts of this solution. Moreover, the linearity ensures that the overall amplitude A will remain arbitrary. The properties of the lattice put restrictions on the allowed values of k. First note that the solution is invariant under k → k + 2π/a. This means that we can restrict k to lie in the first Brillouin zone, k ∈ (-π/a, π/a]. Next, the periodic boundary conditions u_{N+1} = u_1 require that k takes values k = 2πl / (Na) with l = -N/2, ..., N/2. where, to make life somewhat easier, we will assume that N is even so l is an integer. We see that, as in previous sections, the short distance structure of the lattice determines the range of k. Meanwhile, the macroscopic size of the lattice determines the short distance structure of k. This, of course, is the essence of the Fourier transform. Before we proceed, it’s worth mentioning that the minimum wavenumber k = 2π/Na was something that we required when discussing the Debye model of phonons in the Statistical Physics lectures. Our final task is to determine the frequency ω in terms of k. Substituting the ansatz into the formula (4.2), we have mω² = λ (2 - e^{ika} - e^{-ika}) = 4λ sin²(ka/2) We find the dispersion relation ω = 2 √(λ/m) |sin(ka/2)| This dispersion relation is sketched Figure 63, with k ranging over the first Brillouin zone. Figure 63: Phonon dispersion relation for a monatomic chain. Many aspects of the above discussion are familiar from the discussion of electrons in the tight-binding model. In both cases, we end up with a dispersion relation over the Brillouin zone. But there are some important differences. In particular, at small values of k, the dispersion relation for phonons is linear ω ≈ ak √(λ/m) This is in contrast to the electron propagation where we get the dispersion relation for a non-relativistic, massive particle (2.6). Instead, the dispersion relation for phonons is more reminiscent of the massless, relativistic dispersion relation for light. For phonons, the ripples travel with speed c = a √(λ/m) (4.4) This is the speed of sound in the material.

4.1.2 A Diatomic Chain Consider now a linear chain of atoms, consisting of alternating atoms of different types. a mass m mass M The atoms on even sites have mass m; those on odd sites have mass M. For simplicity, we’ll take the restoring forces between these atoms to be the same. The equations of motion are mu¨_{2n} = -λ(2u_{2n} - u_{2n-1} - u_{2n+1}) Mu¨_{2n+1} = -λ(2u_{2n+1} - u_{2n} - u_{2n+2}) Figure 64: Phonon dispersion relation for a diatomic chain. We make the ansatz u_{2n} = Ae^{-iωt - 2ikna} and u_{2n+1} = Be^{-iωt - 2ikna} Note that these solutions are now invariant under k → k + π/a. This reflects the fact that, if we take the identity of the atoms into account, the periodicity of the lattice is doubled. Correspondingly, the Brillouin zone is halved and k now lies in the range k ∈ (-π/2a, π/2a]. (4.5) Plugging our ansatz into the two equations of motion, we find a relation between the two amplitudes A and B, [m 0; 0 M] [A; B] ω² = λ [2 -(1+e^{-2ika}); -(1+e^{2ika}) 2] [A; B] (4.6) This is viewed as an eigenvalue equation. The frequency ω is determined in terms of the wavenumber k by requiring that the appropriate determinant vanishes. This time we find that there are two frequencies for each wavevector, given by ω±² = λ/(mM) {m+M ± √[(m−M)² + 4mM cos²(ka)]} The resulting dispersion relation is sketched in Figure 64 in the first Brillouin zone (4.5). Note that there is a gap in the spectrum on the boundary of the Brillouin zone, k = ±π/2a, given by ΔE = ℏ(ω+ − ω-) = ℏ √(2λ) |√(1/m) − √(1/M)| For m = M, the gap closes, and we reproduce the previous dispersion relation, now plotted on half the original Brillouin zone.

The lower ω part of the dispersion relation is called the acoustic branch. The upper ω part is called the optical branch. To understand where these names come from, we need to look a little more closely at the physical origin of these two branches. This comes from studying the eigenvectors of (4.6) which tells us the relative amplitudes of the two types of atoms. This is simplest to do in the limit k → 0. In this limit the acoustic branch has ω = 0 and is associated to the eigenvector [A; B] = [1; 1] The atoms move in phase in the acoustic branch. Meanwhile, in the optical branch we have ω² = 2λ(M^{-1} + m^{-1}) with eigenvector [A; B] = [M; -m] In the optical branch, the atoms move out of phase. Now we can explain the name. Often in a lattice, different sites contain ions of alternating charges: say, + on even sites and − on odd sites.

But alternating charges oscillating out of phase create an electric dipole of frequency ω(k). This means that these vibrations of the lattice can emit or absorb light. This is the reason they are called “optical” phonons.

Although our discussion has been restricted to one-dimensional lattices, the same basic characterisation of phonon branches occurs for higher dimensional lattices. Acoustic branches have linear dispersion ω ∼ k for low momenta, while optical branches have non-vanishing frequency, typically higher than the acoustic branch. The data for the phonon spectrum of NaCl is shown on the right⁶ and clearly exhibits these features.

⁶ This was taken from “Phonon Dispersion Relations in NaCl”, by G. Raumo, L. Almqvist and R. Stedman, Phys. Rev. 178 (1969).

4.1.3 Peierls Transition

We now throw in two separate ingredients: we will consider the band structure of electrons, but also allow the underlying atoms to move. There is something rather special and surprising that happens for one-dimensional lattices.

We consider the simple situation described in Section 4.1.1 where we have a one-dimensional lattice with spacing a. Suppose, further, that there is a single electron per lattice site. Because of the spin degree of freedom, it results in a half-filled band, as explained in Section 2.1. In other words, we have a conductor.

Consider a distortion of the lattice, in which successive pairs of atoms move closer to each other, as shown below.

Clearly this costs some energy since the atoms move away from their equilibrium positions. If each atom moves by an amount δx, we expect that the total energy cost is of order

U_lattice ∼ Nλ(δx)² (4.7)

What effect does this have on the electrons? The distortion has changed the lattice periodicity from a to 2a. This, in turn, will halve the Brillouin zone so the electron states are now labeled by

k ∈ (−π/2a, π/2a)

More importantly, from the analysis of Section 2.1, we expect that a gap will open up in the electron spectrum at the edges of the Brillouin zone, k = ±π/2a. In particular, the energies of the filled electron states will be pushed down; those of the empty electron states will be pushed up, as shown in the Figure 66. The question that we want to ask is: what is the energy reduction due to the electrons? In particular, is this more or less than the energy U_lattice that it cost to make the distortion in the first place?

Let’s denote the dispersion relation before the distortion as E₀(k), and the dispersion relation after the distortion as E₋(k) for |k| ∈ [0, π/2a) and E₊(k) for |k| ∈ [π/2a, π/a).

The energy cost of the distortion due to the electrons is

U_electron = −2 (Na/2π) ∫₋π/2a^{π/2a} dk [E₀(k) − E₋(k)] (4.8)

Here the overall minus sign is because the electrons lose energy, the factor of 2 is to account for the spin degree of freedom, while the factor of Na/2π is the density of states of the electrons.

To proceed, we need to get a better handle on E₀(k) and E₋(k). Neither are particularly nice functions. However, for a small distortion, we expect that the band structure is changed only in the immediate vicinity of k = π/2a. Whatever the form of E₀(k), we can always approximate it by a linear function in this region,

E₀(k) ≈ µ + νq with q = k − π/2a (4.9)

where µ = E₀(π/2a) and ν = ∂E₀/∂k, again evaluated at k = π/2a. Note that q < 0 for the filled states, and q > 0 for the unfilled states.

We can compute E₋(k) in this region by the same kind of analysis that we did in Section 2.1. Suppose that the distortion opens up a gap ∆ at k = π/2a. Since there is no gap unless there is a distortion of the lattice, we expect that

∆ ∼ δx (4.10)

(or perhaps δx to some power). To compute E₋(k) in the vicinity of the gap, we can use our earlier result (2.16). Adapted to the present context, the energy E close to k = π/2a is given by

[E(π/2a+q) − E][E(π/2a−q) − E] − ∆² = 0

Using our linearisation (4.9) of E₀, we can solve this quadratic to find the dispersion relation

E±(q) = µ ± (ν²q² + ∆²)^{1/2}

Note that when evaluated at q = 0, we find the gap E₊ − E₋ = ∆, as expected. The filled states sit in the lower branch E₋. The energy gained by the electrons (4.8) is dominated by the regions k = ±π/2a. By symmetry, it is the same in both and given by

U_electron ≈ − (Na/π) ∫₋Λ⁰ dq [νq + (ν²q² + ∆²)^{1/2}]

Here we have introduced a lower cut-off −Λ on the integral; it will not ultimately be important where we take this cut-off, although we will require νΛ ≫ ∆. The integral is straightforward to evaluate exactly. However, our interest lies in what happens when ∆ is small. In this limit, we have

U_electron ≈ − (Na/π) [−∆²/16ν − (∆²/8ν) log(∆/4νΛ)]

Both terms contribute to the decrease in energy of the electrons. The first term is of order ∆2 and hence, through (4.10), of order δx2. This competes with the energy cost from the lattice distortion (4.7), but there is no guarantee that it is either bigger or smaller. The second term with the log is more interesting. For small ∆, this always beats the quadratic cost of the lattice distortion (4.7).

We reach a surprising conclusion: a half-filled band in one-dimension is unstable. The lattice rearranges itself to turn the metal into an insulator. This is known as the Peierls transition; it is an example of a metal-insulator transition. This striking behaviour can be seen in one-dimensional polymer chains, such as the catchily named TTF-TCNQ shown in the figure 7. The resistivity – plotted on the vertical axis – rises sharply when the temperature drops to the scale ∆. (The figure also reveals another feature: as the pressure is increased, the resistivity no longer rises quite as sharply, and by the time you get to 8 GPa there is no rise at all. This is because the interactions between electrons become important.)

4.1.4 Quantum Vibrations Our discussion so far has treated the phonons purely classically. Now we turn to their quantisation. At heart this is not difficult – after all, we just have a bunch of harmonic oscillators. However, they are coupled in an interesting way and the trick is to disentangle them. It turns out that we’ve already achieved this disentangling by writing down the classical solutions.

[7 This data is taken from “Recent progress in high-pressure studies on organic conductors”, by S. Yasuzuka and K. Murata (2009)]

We have a classical solution (4.3) for each k = 2πl/Na with l = −N/2,...,N/2. We will call the corresponding frequency ω_l = 2√(λ/m)|sin(k_l a/2)|. We can introduce a different amplitude for each l. The most general classical solution then takes the form u_n(t) = X_0(t) + ∑_{l≠0} [ α_l e^{-i(ω_l t - k_l n a)} + α†_l e^{i(ω_l t - k_l n a)} ] (4.11)

This requires some explanation. First, we sum over all modes l = −N/2,...,+N/2 with the exception of l = 0. This has been singled out and written as X_0(t). It is the centre of mass, reflecting the fact that the entire lattice can move as one. The amplitudes for each l ≠ 0 mode are denoted α_l. Finally, we have taken the real part of the solution because, ultimately, u_n(t) should be real. Note that we’ve denoted the complex conjugation by α† rather than α⋆ in anticipation of the quantisation that we will turn to shortly.

The momentum p_n(t) = m u̇_n is given by p_n(t) = P_0(t) + ∑_{l≠0} [ -imω_l α_l e^{-i(ω_l t - k_l n a)} + imω_l α†_l e^{i(ω_l t - k_l n a)} ]

Now we turn to the quantum theory. We promote u_n and p_n to operators acting on a Hilbert space. We should think of u_n(t) and p_n(t) as operators in the Heisenberg representation; we can get the corresponding operators in the Schrödinger representation simply by setting t = 0.

Since u_n and p_n are operators, the amplitudes α_l and α†_l must also be operators if we want these equations to continue to make sense. We can invert the equations above by setting t = 0 and looking at ∑_n e^{-i k_l n a} = ∑_n ∑_{l'} [ α_{l'} e^{-i(k_l - k_{l'}) n a} + α†_{l'} e^{-i(k_l + k_{l'}) n a} ] = N(α_l + α†_{-l})

Similarly, ∑_n e^{i k_l n a} = ∑_n ∑_{l'} [ -imω_{l'} α_{l'} e^{i(k_l - k_{l'}) n a} + imω_{l'} α†_{l'} e^{i(k_l + k_{l'}) n a} ] = -i N m ω_l (α_l - α†_{-l})

where we’ve used the fact that ω_l = ω_{-l}. We can invert these equations to find α_l = (1 / (2 m ω_l N)) ∑_n e^{-i k_l n a} (m ω_l u_n + i p_n)

α†_l = (1 / (2 m ω_l N)) ∑_n e^{i k_l n a} (m ω_l u_n - i p_n) (4.12)

Similarly, we can write the centre of mass coordinates — which are also now operators — as X_0 = (1 / N) ∑_n u_n   and   P_0 = (1 / N) ∑_n p_n (4.13)

At this point, we’re ready to turn to the commutation relations. The position and momentum of each atom satisfy [u_n, p_{n'}] = iℏ δ_{n,n'}

A short calculation using the expressions above reveals that X_0 and P_0 obey the relations [X_0, P_0] = iℏ / N

Meanwhile, the amplitudes obey the commutation relations [α_l, α†_{l'}] = δ_{l,l'} / (2 m ω_l N)   and   [α_l, α_{l'}] = [α†_l, α†_{l'}] = 0

This is something that we’ve seen before: they are simply the creation and annihilation operators of a simple harmonic oscillator. We rescale α_l = √(ℏ / (2 m ω_l N)) a_l (4.14)

then our new operators a_l obey [a_l, a†_{l'}] = δ_{l,l'}   and   [a_l, a_{l'}] = [a†_l, a†_{l'}] = 0

Phonons We now turn to the Hamiltonian (4.1). Substituting in our expressions (4.12) and (4.13), and after a bit of tedious algebra, we find the Hamiltonian H = P_0²/(2M) + ∑_{l≠0} (a†_l a_l + 1/2) ℏω_l

Here M = N m is the mass of the entire lattice. Since this is a macroscopically large object, we set P_0 = 0 and focus on the Hilbert space arising from the creation operators a†_l. After our manipulations, these are simply N, decoupled harmonic oscillators.

The ground state of the system is a state |0⟩.

Each harmonic oscillator gives a contribution of ℏω /2 to the zero-point energy E of l 0 the ground state. However, this is of no interest. All we care about is the energy difference between excited states and the ground state. For this reason, it’s common practice to redefine the Hamiltonian to be simply H = ∑ ℏω a†a l l l l≠0 so that H|0⟩ = 0.

The excited states of the lattice are identical to the excited states of the harmonic oscillators. For each l, the first excited state is given by a†|0⟩ and has energy E = ℏω .

l l However, although the mathematics is identical to that of the harmonic oscillator, the physical interpretation of this state is rather different. That’s because it has a further quantum number associated to it: this state carries crystal momentum ℏk . But an object which carries both energy and momentum is what we call a particle! In this case, it’s a particle which, like all momentum eigenstates, is not localised in space. This particle is a quantum of the lattice vibration. It is called the phonon.

Note that the coupling between the atoms has lead to a quantitative change in the physics. If there was no coupling between atoms, each would oscillate with frequency ω and the minimum energy required to excite the system would be ∼ ℏω. However, when the atoms are coupled together, the normal modes now vibrate with frequencies ω . For small k, these are ω ≈ √(λ/m)·πl/N. The key thing to notice here is the factor l l of 1/N. In the limit of an infinite lattice, N → ∞, there are excited states with infinitesimally small energies. We say that the system is gapless, meaning that there is no gap between the ground state and first excited state. In general, the question of whether a bunch interacting particles is gapped or gapless is one of the most basic (and, sometimes, most subtle) questions that you can ask about a system.

Any state in the Hilbert space can be written in the form |ψ⟩ = √l (a†)n |0⟩ n !

and has energy H|ψ⟩ = ∑ ℏn ω l l

This state should be thought of as described n phonons and decomposes into n phonons with momentum ℏk for each l. The full Hilbert space constructed in this way contains states consisting of an arbitrary number of particles. It is referred to as a Fock space.

Because the creation operators a† commute with each other, there is no difference between the state |ψ⟩ ∼ a†a†|0⟩ and |ψ⟩ ∼ a†a†|0⟩. This is the statement that phonons l l′ l′ l are bosons.

The idea that harmonic oscillator creation operators actually create particles sometimes goes by the terrible name of second quantisation. It is misleading — nothing has been quantised twice.

Quantisation of Acoustic and Optical Phonons

It is not difficult to adapt the discussion above to vibrations of a diatomic lattice that we met in Section 4.1.2. We introduce two polarization vectors, e (k). These are eigenvectors obeying the matrix equation (4.6), [ 2  −(1+e−2ika) ] [ ω²   0 ] [ e (k) ]

[                ] [      ] [      ] = ± e (k)

[ −(1+e2ika)  2  ] [ 0    λ ] [   ±  ]        ± [                ] [      ] [      ]

m   0 We then write the general solution as u 2n (t)   ∑   ∑   √(ℏ/(2Nω (k))) { a (k)e (k)ei(ωst+2kna) +a†(k)e⋆(k)e−i(ωst+2kna) } u 2n+1 (t) =  k∈BZ s=±       s        s s         s s     s where the creation operators obey [a (k),a (k′)†] = δ δ  and [a (k),a (k′)] = [a†(k),a (k′)†] = 0 s s′ s,s′ k,k′ s s′ s s′

Now the operators a† (k) create acoustic phonons while a† (k) create optical phonons, − + each with momentum ℏk.

4.1.5 The M¨ossbauer Effect

There’s a rather nice application of phonons that goes by the name of the M¨ossbauer effect. This is to do with how nuclei in solids absorb gamma rays.

To understand this, we first need to think about atoms absorb light, and then contrast this with how nuclei absorb light. To this end, consider a gas of atoms, all sitting in the ground state. If we shine light on the atoms at very specific frequencies, then the atoms will absorb the light by jumping to excited states. The frequency should be E = ℏν = E γ excite where E is the energy difference between the excited state and the ground state.

excite Once the atom absorbs a photon, it will sit in the excited state for some time and then decay. If it drops back down to the ground state, the emitted photon will again have energy E and can be absorbed by another atom. This then repeats, a process known as resonant absorption.

However, a little thought shows that the situation is slightly more complicated than we’ve made out. Suppose, for simplicity, that the original atom was at rest. In the collision with the atom, both energy and momentum must be conserved. The momentum of the incoming photon is p = E /c and, after the collision, this is transferred to the γ γ atom, so p = E /c. This means that the atom has kinetic energy from the recoil, atom γ p²     E²γ E =  atom =      (4.15)

recoil 2M   2Mc² where M is the mass of the atom. (The speed of the atom is small enough that we can use the non-relativistic form of kine tic energy.) So we see that it’s not quite right to say that the energy of the photon should be tuned to the energy difference E_excite because this ignores the energy that goes into the recoil. Instead, the incoming photon should have slightly higher energy, E_γ = E_excite + E_recoil, or E_γ = E_excite + E^2_excite / (2Mc^2) ⇒ E_γ ≈ E_excite + E^2_excite / (2Mc^2) + ... (4.16)

Meanwhile, when the atom now decays back to the ground state, it will emit the photon in a random direction. This means that the atom typically remains in motion; indeed, it’s quite possible that the kinetic energy of atom increases yet again if it emits the photon back in the direction it came. All of this means that the energy of the emitted photon that the atom emits is smaller than the energy of the photon that it absorbed. The question is: what happens next? In particular, is it possible for this emitted photon to be re-absorbed by a different atom so that we get resonant absorption? This is now a quantitative question, rather than a qualitative question. The key point is that you don’t need to tune the frequency of light exactly to E_excite in order to excite an atom. Instead, there is a range of energies – a so-called line width – that will do the job. This line width is related to the lifetime τ of the excited state by ∆E ∼ ℏ/τ. (See the chapter on scattering in the lectures on Topics in Quantum Mechanics for more details.)

Let’s put in some numbers. The energy needed to excite an electron from one level to another is measured in E_excite ≈ eV. Meanwhile the mass of, say, an iron atom is around Mc^2 ∼ 5×10^4 MeV. This means that the correction term (4.16) in the photon energy is of order ∆E ≈ 10^−11 eV. This is significantly smaller than the line width of atomic excitations, and the discussion above has no relevance to absorption of light due to transitions of electrons from one energy level to another.

However, things are very different when it comes to nuclear transitions. Now the relevant excitation energy is of order E_excite ≈ 10^4 eV, corresponding to soft gamma rays, and the correction term (4.16) in the photon energy due to recoil effects is ∆E ≈ 10^−3 eV. This time the energy is significantly larger than the line width: a typical nuclear excitation has lifetime τ ∼ 10^−7 seconds and a width Γ ∼ 10^−8 eV. The upshot of this argument is that, while X-ray absorption lines are seen corresponding to atomic excitations, we should not expect to see a repeat in the gamma-ray spectrum associated to nuclear excitations.

And yet.... while it’s true that gamma ray resonant absorption lines are not seen in gasses, they are seen solids. This is the Mössbauer effect. The important point is that a nucleus in an atom is coupled to all the other atoms through the bonds in a solid. A nucleus will recoil when hit by a photon, as in the discussion above, but now the atom will bounce back into position and the energy E_recoil will typically be distributed into phonon degrees of freedom. When there are a large number of phonons excited, the story is not different from that told above, and the emitted photon has a sufficiently different frequency to kill resonant absorption. However, there is some probability that no phonons are created, but instead the entire solid moves absorbs the momentum of the photon. In this case, the recoil energy is still given by (4.15) but with M is the mass of the solid, rather than the mass of a single atom. This gives an extra factor of around 10^23 in the denominator, and the recoil energy becomes negligible. For this to happen, the entire solid must react coherently as a single quantum object! The resulting gamma ray resonant absorption spectrum is indeed observed.

If we look at a solid at suitably macroscopic distances, we don’t notice the underlying atomic structure. Nonetheless, it’s still straightforward to detect sound waves. This suggests that we should be able to formulate a continuum description of the solid that is ignorant of the underlying atomic make-up.

With this in mind, we define the displacement field for a one-dimensional lattice. This is a function u(x,t). It is initially defined only at the lattice points u(x = na) = u_n. However, we then extend this field to all x ∈ R, with the proviso that our theory will cease to make sense if u(x) varies appreciably on scales smaller than a.

The equation governing the atomic displacements is (4.2)

m ü_n = -λ(2u_n - u_{n-1} - u_{n+1})

In the continuum limit, this difference equation becomes the wave equation ∂²u/∂t² = λ′ ∂²u/∂x² (4.17)

where ρ = m/a is the density of our one-dimensional solid, and λ′ = λa. These are the macroscopic parameters. Note, in particular, that the speed of sound (4.4) can be written purely in terms of these macroscopic parameters, c² = λ′/ρ.

The equation of motion (4.17) can be derived from the action S = ∫ dt dx [ (ρ/2) (∂u/∂t)² - (λ′/2) (∂u/∂x)² ]

This is the field theory for the phonons of a one-dimensional solid.

4.2.1 Phonons in Three Dimensions

For three-dimensional solids, there are three displacement fields, u (x), one for each direction in which the lattice can deform. In general, the resulting action can depend on various quantities ∂u /∂xj. However, if the underlying lattice is such that the long-wavelength dynamics is rotationally invariant, then the action can only be a function of the symmetric combination

$$ u_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right) $$

If we want an equation of motion linear in the displacement, then the most general action is a function of u_{ij}u_{ij} or u_{kk}^2 . (The term u_{kk} is a total derivative and does not affect the equation of motion). We have

$$ S = \int dt d^3x \left[ \frac{\rho}{2} \left( \frac{\partial u_i}{\partial t} \right)^2 - 2\mu u_{ij}u_{ij} - \lambda u_{ii}u_{jj} \right] \quad (4.18) $$

The coefficients μ and λ are called Lamé coefficients; they characterise the underlying solid.

This action gives rise to the equations of motion

$$ \rho \frac{\partial^2 u_i}{\partial t^2} = (\mu+\lambda) \frac{\partial^2 u_j}{\partial x_i \partial x_j} + \mu \frac{\partial^2 u_i}{\partial x_j \partial x_j} \quad (4.19) $$

We can look for solutions of the form

$$ u_i(x,t) = \epsilon_i e^{i(\mathbf{k} \cdot \mathbf{x} + \omega t)} $$

where $\epsilon_i$ determines the polarisation of the wave. Plugging this ansatz into the equation of motion gives us the relation

$$ \rho \omega^2 \epsilon_i = \mu k^2 \epsilon_i + (\mu+\lambda)(\epsilon \cdot \mathbf{k})k_i $$

The frequency of the wave depends on the polarisation. There are two different options. Longitudinal waves have $\mathbf{k} \sim \epsilon$. These have dispersion

$$ \omega^2 = \frac{2\mu+\lambda}{\rho} k^2 \quad (4.20) $$

Meanwhile, transverse waves have $\epsilon \cdot \mathbf{k} = 0$ and dispersion

$$ \omega^2 = \frac{\mu}{\rho} k^2 \quad (4.21) $$

Note that both of these dispersion relations are linear. The continuum approximation only captures the low-k limit of the full lattice system and does not see the bending of the dispersion relation close to the edge of the Brillouin zone. This is because it is valid only at long wavelengths, $ka \ll 1$.

The general solution to (4.19) is then

$$ u_i(x,t) = \sum_s \int \frac{d^3k}{(2\pi)^3} \frac{1}{\sqrt{2\rho \omega_s(\mathbf{k})}} \left( a_s(\mathbf{k})e^{i(\mathbf{k} \cdot \mathbf{x} - \omega_s t)} + a_s^{\dagger}(\mathbf{k})e^{-i(\mathbf{k} \cdot \mathbf{x} - \omega_s t)} \right) \quad (4.22) $$

where the s sum is over the three polarisation vectors, two transverse and one longitudinal. The frequencies $\omega_s(\mathbf{k})$ correspond to either (4.20) or (4.21) depending on the choice of s.

4.2.2 From Fields to Phonons

Although we have discarded the underlying atoms, this does not mean that we have lost the discrete nature of phonons. To recover them, we must quantise the field theory defined by the action (4.18). This is the subject of Quantum Field Theory. You will learn much (much) more about this in next year’s lectures. What follows is merely a brief taster for things to come.

To quantise the field, we need only follow the same path that we took in Section 4.1.4. At every step, we simply replace the discrete index n with the continuous index x. Note, in particular, that x is not a dynamical variable in field theory; it is simply a label.

First, we turn the field u(x) into an operator. This means that the amplitudes $a_s(\mathbf{k})$ and $a_s^{\dagger}(\mathbf{k})$ in (4.22) also become operators. To proceed, we need the momentum conjugate to $u_i(x,t)$. This too is now a field, and is determined by the usual rules of classical dynamics,

$$ \pi_i(x) = \frac{\partial \mathcal{L}}{\partial \dot{u}_i} = \rho \dot{u}_i $$

Written in terms of the solution (4.22), we have

$$ \pi_i(x,t) = \rho \sum_s \int \frac{d^3k}{(2\pi)^3} \frac{1}{\sqrt{2\rho \omega_s(\mathbf{k})}} \left( -i\omega_s a_s(\mathbf{k})e^{i(\mathbf{k} \cdot \mathbf{x} - \omega_s t)} + i\omega_s a_s^{\dagger}(\mathbf{k})e^{-i(\mathbf{k} \cdot \mathbf{x} - \omega_s t)} \right) $$

The canonical commutation relations are the field-theoretical analog of the usual position-momentum commutation relations,

$$ [u_i(x), \pi_j(x')] = i\hbar \delta_{ij} \delta^3(x-x') $$

At this point we have some straightforward but tedious calculations ahead of us. We will skip these on the grounds that you will see them in glorious detail in later courses. The first is an inverse Fourier transform, which expresses $a_s(\mathbf{k})$ and $a_s^{\dagger}(\mathbf{k})$ in terms of $u_i(x)$ and $\pi_i(x)$. The result is analogous to (4.12). We then use this to determine the commutation relations,

$$ [a_s(\mathbf{k}), a_{s'}^{\dagger}(\mathbf{k}')] = \delta_{ss'} \delta^3(\mathbf{k}-\mathbf{k}') \quad \text{and} \quad [a_s(\mathbf{k}), a_{s'}(\mathbf{k}')] = [a_s^{\dagger}(\mathbf{k}), a_{s'}^{\dagger}(\mathbf{k}')] = 0 $$

This is the statement that these are creation and annihilation operators for harmonic oscillators, now labelled by both a discrete polarisation index s = 1,2,3 as well as the continuous momentum index k.

The next fairly tedious calculation is the Hamiltonian. This too follows from standard rules of classical dynamics, together with a bunch of Fourier transforms. When the dust settles, we find that, up to an irrelevant overall constant,

$$ H = \sum_s \int \frac{d^3k}{(2\pi)^3} \hbar \omega_s(\mathbf{k}) a_s^{\dagger}(\mathbf{k}) a_s(\mathbf{k}) $$

This is simply the Hamiltonian for an infinite number of harmonic oscillators.

The interpretation is the same as we saw in Section 4.1.4. We define the ground state of the field theory to obey $a_s(\mathbf{k})|0\rangle = 0$ for all s and for all k. The Fourier modes of the field $a_s^{\dagger}(\mathbf{k})$ are then to be viewed as creating and destroying phonons which carry momentum $\hbar \mathbf{k}$, polarisation $\epsilon_s$ and energy $\hbar \omega_s(\mathbf{k})$. In this way, we see particles emerging from an underlying field.

Lessons for the Future

This has been a very quick pass through some basic quantum field theory, applied to the vibrations of the lattice. Buried within the mathematics of this sect ion are two key physical ideas. The first is that a coarse grained description of atomic vibrations can be described in terms of a continuous field. The second is that quantisation of the field results in particles that, in the present context, we call phonons.

There is a very important lesson to take from the second of these ideas, a lesson which extends well beyond the study of solids. All of the fundamental particles that we know of in Nature – whether electrons, quarks, photons, or anything else — arise from the quantisation of an underlying field. This is entirely analogous to the way that phonons arose in the discussion above.

Is there also a lesson to take away from the first idea above? Could it be that the fundamental fields of Nature themselves arise from coarse-graining something smaller? The honest answer is that we don't know. However, perhaps surprisingly, all signs point towards this not being the case. First, and most importantly, there is no experimental evidence that the fundamental fields in our Universe have a discrete underpinning. But at the theoretical level, there are some deep mathematical reasons — to do with chiral fermions and topology — which suggest that it is not possible to find a discrete system from which the known laws of physics emerge. It would appear that our Universe does not have something akin to the atomic lattice which underlies the phonon field. Understanding these issues remains a vibrant topic of research, both in condensed matter physics and in high energy physics.

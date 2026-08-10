# David Tong Lectures on Kinetic Theorykintheory

> 来源文件：pre_David_Tong_Lectures_on_Kinetic_Theorykintheory.txt
> 字符数（约）：179646
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Michaelmas Term 2012 Preprint typeset in JHEP style - HYPER VERSION Kinetic Theory University of Cambridge Graduate Course David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 OBA, UK http://www.damtp.cam.ac.uk/user/tong/kinetic.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources This lecture course covers three topics: kinetic theory, stochastic processes and linear response. Most decent books on statistical mechanics will have a section covering non-equilibrium topics in general. However, if you’re looking for details beyond the basics, you’ll probably need a different book for each topic. Some good general purpose books are: • Huang, Statistical Mechanics • Kardar, Statistical Physics of Particles • Reif, Fundamentals of Statistical and Thermal Physics Both Huang and Kardar treat kinetic theory and the Boltzmann equation before they move onto statistical mechanics. Much of Section 2 of these notes follows the path laid down in these books. Reif ends with a much wider ranging discussion of kinetic theory, transport and stochastic processes.

For more details on kinetic theory: • Chapman and Cowling, The Mathematical Theory of Non-Uniform Gases • Lifshitz and Pitaevskii, Physical Kinetics Both of these are old school. The first was published in 1939 although the latest edition, written in 1970, is modern enough to cover all the developments that we touch upon in this course. The last volume of the course by Landau and Lifshitz covers kinetic theory. This book was written substantially later than the earlier volumes, decades after Landau’s death.

For more details on stochastic processes: • Van Kampen, Stochastic Processes in Physics and Chemistry The topic of linear response is usually covered in books on many body theory or more general condensed matter. Two excellent modern books, both with a chapter on response theory, are • Altland and Simons, Condensed Matter Field Theory • Chaikin and Lubensky, Principles of Condensed Matter Physics Finally, there are a number of good lecture notes and resources on the web, collated at http://www.damtp.cam.ac.uk/user/tong/kinetic.html

Contents

## 1. Things Bumping Into Other Things

## 1.1 Introduction

## 1.2 Basics of Collisions

1.2.1 Relaxation Time 3

## 1.3 Basics of Transport

1.3.1 Diffusion 5 1.3.2 Viscosity 7 1.3.3 Thermal Conductivity 10 1.3.4 Conservation Means Diffusion 12

## 2. Kinetic Theory

## 2.1 From Liouville to BBGKY

2.1.1 The BBGKY Hierarchy 16

## 2.2 The Boltzmann Equation

2.2.1 Motivating the Boltzmann Equation 20 2.2.2 Equilibrium and Detailed Balance 23 2.2.3 A Better Derivation 25

## 2.3 The H-Theorem

## 2.4 A First Look at Hydrodynamics

2.4.1 Conserved Quantities 36 2.4.2 Ideal Fluids 42

## 2.5 Transport with Collisions

2.5.1 Relaxation Time Approximation 46 2.5.2 Thermal Conductivity Revisited 47 2.5.3 Viscosity Revisited 48

## 2.6 A Second Look: The Navier-Stokes Equation

## 3. Stochastic Processes

## 3.1 The Langevin Equation

3.1.1 Diffusion in a Very Viscous Fluid 54 3.1.2 Diffusion in a Less Viscous Liquid 56 3.1.3 The Einstein Relation 58 3.1.4 Noise Probability Distributions 59 3.1.5 Stochastic Processes for Fields 62

## 3.2 The Fokker-Planck Equation

3.2.1 The Diffusion Equation 63 3.2.2 Meet the Fokker-Planck Equation 64 3.2.3 Velocity Diffusion 69 3.2.4 Path Integrals: Schrödinger, Feynman, Fokker and Planck 73 3.2.5 Stochastic Calculus 77

## 4. Linear Response

## 4.1 Response Functions

4.1.1 Linear Response 80 4.1.2 Analyticity and Causality 81 4.1.3 Kramers-Kronig Relation 83

## 4.2 Classical Examples

4.2.1 The Damped Harmonic Oscillator 87 4.2.2 Dissipation 90 4.2.3 Hydrodynamic Response 91

## 4.3 Quantum Mechanics and the Kubo Formula

4.3.1 Dissipation Again 94 4.3.2 Fluctuation-Dissipation Theorem 96

## 4.4 Response in Quantum Field Theory

Acknowledgements These lecture notes are far from original. They borrow heavily both from the books described above and the online resources listed on the course webpage. My thanks to Daniele Dorigoni for help explaining the tricky factor of 1/2 in the path integral for the Fokker-Planck equation.

## 1. Things Bumping Into Other Things

## 1.1 Introduction

The purpose of this course is to describe a number of basic topics in non-equilibrium statistical mechanics.

If you’ve taken a first course in Statistical Mechanics, you’ll know that the whole machinery of ensembles and partition functions only works when applied to systems in equilibrium. Equilibrium is defined to be a state in which, at least on the coarse grained level, things don’t change. Of course, if you have a hot system and you look closely enough, everything is flying around on the atomic level. But if you focus only on macroscopic variables then, in equilibrium, all is calm.

At first, the restriction to equilibrium sounds rather limiting. But it’s not. This is because the state of equilibrium is very special: if you take any system and wait long enough, it will always settle down to equilibrium.

ough then it will eventually relax down to equilibrium. (This is sometimes said to be the −1th law of thermodynamics). Of course, this begs the question of why equilibrium is special. Why do all systems eventually reach this state. How do they approach this state? How does such irreversible behaviour arise from the fundamental laws of physics which are, for all intents and purposes, invariant under time reversal? Moreover, what if you’re not happy to just sit back and watch an equilibrium system? Suppose you want to stir it or splash it or attach a couple of crocodile clips and zap it. How will it respond? These are the kind of questions that we will begin to answer in this course.

While there is typically only a single equilibrium state, for a system with 10^23 particles, there are many many ways to be out-of-equilibrium. Most of these states are uninteresting in the sense that they will be so complicated that no general features will emerge. Moreover, such states will be fleeting, rapidly changing to another complicated configuration. If we’re to have any chance of making progress, we need to be careful about the kind of states we discuss and the kind of questions that we ask. We would like to identify features in the dynamics of 10^23 particles that persist for long periods of time. We will see that such features arise for systems that are close to equilibrium. Indeed, throughout this course, the dramatic sounding “non-equilibrium” will really mean “almost-equilibrium”.

Each of the four sections in these lecture notes can be read more or less independently. In the rest of this introductory section, we will introduce a few basic tools to describe how quantities change in a gas. This will really be a baby version of kinetic theory, with nothing more sophisticated than Newtonian thinking applied to a bunch of billiard balls. But it will allow us to develop some basic intuition for the rudiments of the subject. While many of the formulae we derive in this section are rather heuristic, all will be revisited Section 2 where we use the Boltzmann equation to give a more rigorous view on the subject, understanding transport phenomena and deriving the equations of fluid mechanics starting from first principles. Section 3 introduces the subject of random jittery motion, usually called stochastic processes. Finally, in Section 4 we turn the stir-it-splash-it-zap-it question and develop the machinery necessary to describe how systems respond when prodded.

## 1.2 Basics of Collisions

Let’s start by considering N molecules in a gas of volume V. We will begin by ignoring all interactions between particles. Instead, we will treat the molecules as spheres of a finite size which will allow collisions to occur. For the most part, we won’t rely on the results of earlier courses on statistical mechanics. There is, however, one exception: in the rest of this section, we will need the Maxwell-Boltzmann probability distribution for the velocities in a gas^1.

f(⃗v)d^3v = (m/(2πk_B T))^{3/2} e^{-mv^2/2k_B T} d^3v (1.1)

The distribution f(⃗v)d^3v is the probability that a molecule has velocity within a small volume d^3v in the neighbourhood of ⃗v.

We denote the diameter of the particle as d. Obviously its radius is d/2. Viewed head on, the particle appears as a disc with area π(d/2)^2. However, more relevant for our purposes is the effective cross-sectional area of the particle, πd^2. To see why this is, focus on a single particle as it makes its way through the gas. If it travels a distance l, it will sweep out a volume πd^2 l as shown in Figure 1 and collide with any other particle whose centre lies within this volume.

The mean free path is defined to be the average distance travelled by the molecule between each collision. This is given by πd^2 l = V/N, or

l = V/(N πd^2) = 1/(n πd^2) (1.2)

where n = N/V is the particle density.

^1 This result will be re-derived in Section 2 when we discuss the Boltzmann equation. You can also find a simple derivation in the lectures on Statistical Physics.

Figure 1: A particle of radius d/2 travels, on average, a length l between each collision. In this time it sweeps out a volume πd^2 l.

In what follows, we’ll assume that our gas is dilute, meaning l ≫ d. For typical gases d ∼ 10^{-10} m while, at atmospheric pressure, l ∼ 10^{-7} m.

1.2.1 Relaxation Time

The average time between collisions is called the scattering time or relaxation time, τ = l / v̄_rel.

You might think that v̄_rel is the average speed of a given particle. This isn’t quite true. Since we’re interested in the rate of collisions, the speed of other particles approaching is just as important as the speed of the particle you’re looking at. So we should take v_rel to be the average relative speed of the molecules. For two particles with velocities ⃗v and ⃗v′, the average relative speed is

v̄_rel^2 = ⟨(⃗v − ⃗v′)^2⟩ = ∫ d^3⃗v ∫ d^3⃗v′ (⃗v − ⃗v′)^2 f(⃗v) f(⃗v′) = ⟨v^2⟩ + ⟨v′^2⟩ − 2⟨⃗v · ⃗v′⟩ (1.3)

where f(⃗v) in the first line is the Maxwell-Boltzmann distribution (1.1). The fact 我们已经将分布 f(⃗v)f(⃗v′) 在第一行中相乘，这意味着我们假设两个粒子的速度是不相关的。这个假设我们将在第2节中再讨论。

(1.3)中的最后一项为零：⟨⃗v ·⃗v′⟩ = 0。这基于旋转对称性。由于每个粒子的速度是独立的，只需知道平均速度（不是速率！）在，例如，x方向上为零：⟨v_x⟩ = 0。同时，⟨v_x^2⟩ = ⟨v_x′^2⟩，这意味着 v_rel^2 = 2⟨v_x^2⟩。从麦克斯韦-玻尔兹曼分布(1.1)计算⟨v_x^2⟩是一个简单的练习，其结果与直接根据能量均分定理得到的结果相同：⟨v_x^2⟩ = 3k_B T/m。我们有 v_rel^2 = 6k_B T / m 而弛豫时间由下式给出 τ = (1 / (nπd^2)) * sqrt(m / (6k_B T))

注意，随着温度下降，平均自由程保持不变。然而，碰撞之间的时间增加了。

弛豫时间有一个略有不同的解释，这很有用。假设一个分子在时间t和时间t+dt之间发生碰撞的概率由wdt给出，其中w是一个常数，称为碰撞率。注意，在陈述这一点时，我们对碰撞的性质做了更多假设。特别是，w是一个常数这一事实意味着不保留先前碰撞的记忆：仅仅因为你不久前已经被撞击过，再次被撞击的机会并不会受到影响。

如果P(t)是分子在时间t之前未受伤害地存活下来的概率，那么它进一步在时间t+dt之前没有发生碰撞的概率是 P(t+dt) = P(t)(1−wdt)

将其写成微分方程，我们有 dP/dt = −wP ⇒ P(t) = e^{−wt} 其中我们选择了归一化条件使得P(0) = 1且P(∞) = 0。有了这个，我们可以计算碰撞之间的平均时间。但这正是我们上面称为弛豫时间的量。它是 τ = ∫_0^∞ P(t) dt = 1/w 我们得知1/τ是碰撞率。

## 1.3 输运基础

我们现在转向事物如何移动的问题。当然，在热系统中，微观组分总是在运动，即使在平衡态下。我们的目标是理解当系统偏离平衡时，某些宏观性质如何移动。我们将考察的性质都与一个守恒量相关：粒子数、能量或动量。这些量随时间变化的过程通常被称为输运。正如我们将看到的，所有这些量通常以达到平衡态的方式流动。

1.3.1 扩散将一滴墨水滴入一杯水中。它是如何扩散的？更一般地，我们关注一种特定粒子的运动——一种有漂亮颜色或奇怪气味的粒子——当它穿过液体或气体的普通背景时。任何粒子的真实动力学，正如你可能预料的，是有些抖动的。这里我们将看一个捕捉这种物理的简单模型。

随机游走考虑一个晶格，目前我们将其视为一维的。晶格位点之间的间距由平均自由程l设定，经过时间τ后，粒子向左或向右跳跃。跳跃的方向完全是随机的：50%的时间向左，50%的时间向右。这个模型被称为随机游走。

粒子从原点出发，我们想知道它在时间t = Nτ时位于x = ml的概率P(x,t)。（这里m是一个整数；它不是粒子的质量！）。我们将从一个简单的组合推导开始。为简单起见，我们取N为偶数，并考虑m ≪ N。要到达x = ml，粒子必须进行½(N + m)次向前跳跃和½(N − m)次向后跳跃。概率就是我们可以进行此操作的不同方式的数量除以2^N，即所有可能组合的总数。

P(x,t) = (2^N * N!) / [ (½(N+m))! * (½(N−m))! ] ≈ (2 / sqrt(πN)) * e^{−m^2/(2N)} = (2 / sqrt(πt)) * e^{−x^2 τ / (2 l^2 t)} (1.4)

其中，在第二步中，阶乘已被斯特林近似所取代，并且我们也对m/N进行了领头阶展开。（为了得到前因子，我们需要在斯特林展开中进行到三阶）。

粒子的概率分布是一个不断扩散的高斯系综。均值简单地是⟨x⟩ = 0，反映了粒子向前和向后移动的可能性相等。方差是 ⟨x^2⟩ = (l^2 / τ) * t (1.5)

粒子行进的均方根（rms）距离增长为⟨x^2⟩ ∼ t。这是随机游走的特征行为。

将我们的随机游走分析重复到三维是简单的。对于立方晶格，我们假设每个方向上的运动是独立且等可能的。平均而言，粒子每3τ时间才在x方向上移动一次，所以(1.5)应被替换为⟨x^2⟩ = l^2 t / (3τ)。但这意味着覆盖的总均方根距离保持不变 ⟨⃗x^2⟩ = ⟨x^2⟩ + ⟨y^2⟩ + ⟨z^2⟩ = (l^2 / τ) * t

扩散 Diffusion Equation We can recast the above discussion in terms of a differential equation for the density of particles, n = N/V. Away from equilibrium, the density is not a constant. It is, in general, a function of time and space. We expect any gradient, ∇n, in the density of particles to lead to a flow, from the high density region to the low.

We’ll again restrict first to the case of one-dimension. Consider the density at some fixed time: n = n(x,t). We’d like to derive an expression for the density at the point x a short time ∆t later. Of course, some particles will leave, but others will come in to replace them. Any particle which is at x at time t+∆t must have been sitting at some other position x−∆x at time t. Here ∆x should be viewed as a random variable since some move one way, some the other. This means that we can write an expression for the density at time t+∆t as an average over all the different ∆x, n(t+∆t,x) = ⟨n(t,x−∆x)⟩ = ⟨n(t,x)− ⟨∆x⟩+ ⟨∆x2⟩+...⟩ ∂n 1∂2n = n(t,x)− ⟨∆x⟩+ ⟨∆x2⟩+...

∂x 2∂x2

The term with the first order derivative vanishes because, on average, particles are equally likely to go either way, meaning ⟨∆x⟩ = 0. Taylor expanding the left-hand-side, we arrive at the diffusion equation ∂n ∂2n = D ∂t ∂x2

where the diffusion constant is D = ⟨∆x2⟩/2∆t. We expect this to be related to our two quantities, the mean free path l and scattering time τ. On dimensional grounds, we must have D ∼ l2/τ

Solutions to the diffusion equation evolve so as to iron out any inhomogeneities in particle density. As an example, suppose that all N particles start out life sitting at the origin, giving us the initial condition n(x,t = 0) = Nδ(x). The solution to the diffusion equation with this initial condition is an ever-spreading Gaussian, n(x,t) = N / √(4πDt) * e^(-x²/4Dt)

This reproduces the discretised result (1.4). Viewing the average distance travelled as the width of the cloud of particles, we again have the result ⟨x2⟩ = 2Dt

It is simple to extend the derivation above to three dimensions. Going through the same steps, we now find the 3d diffusion equation, ∂n/∂t = D∇²n

This is also known as Fick’s (second) law. We again expect that D ∼ l²/τ. (Although the overall numerical factor is not necessarily the same as the 1d case. In fact, in simple analysis it is a factor of 3 less). The Gaussian again provides a solution, now with ⟨⃗x2⟩ = 6Dt

As we will now show, a number of other processes also follow this general diffusive form.

1.3.2 Viscosity Viscosity is a form of internal friction experienced by a fluid. It can be measured by placing a fluid between two plates, a distance d apart in the z direction. Holding lower plate stationary, the top plate is moved at a constant speed, u, in the x direction. But you don’t get to do this for free: the fluid pushes back. If you want to d:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1)

keep the plate moving at a constant speed, you have to Figure 2: apply a force F.

Near the upper plate, a friction force causes the fluid to be dragged along with the same speed u. However, near the lower plate, the fluid remains stationary. This sets up a velocity gradient, u (z), with u (d) = u and u (0) = 0. Experimentally, it is found x x x that the force per unit area which must be exerted on the upper plate is proportional to this velocity gradient, F du u = η ≈ η (1.6)

A dz d wherethesecondequalityholdsforsmalldistancesd. Thecoefficientofproportionality, η, is called the viscosity. (Or, more correctly, the dynamic viscosity).

– 7 – We would like to derive both the force law (1.6) and the viscosity η from first princi- ples. It’s simple to get an intuition for what’s happening on the atomic level: when the molecules collide with the upper plate, they pick up some x-momentum. They then collide with other molecules lower down, imparting some of this x-momentum to new molecules, which then collide with other molecules lower down, and so on. In this way, we set up the velocity gradient in the z direction.

We’ll think of a slab of gas at some fixed value of z. To figure out the force acting on this slab, we need to work out two things: the number of particles moving through the slab per unit of time; and the extra momentum in the x-direction that each particle imparts to the molecules in the slab.

Let’s first deal with the number of particles. The density of particles in the fluid is n = N/V. How many of these pass through a slab in the z-direction in a given length of time depends on how fast they’re travelling in the z-direction (obv!). But we know how many particles there are with each speed: this is given by the Maxwell-Boltzmann distribution (1.1). The net result is that the number of particles, per unit time, per unit area, whose velocity is lies close to ⃗v (in a box of size d3⃗v), passing through a horizontal slab is # of particles per unit time per unit area = nv f(⃗v)d3v (1.7)

Now let’s figure out the momentum that each of these molecules imparts. Consider a particle at some position z. It gets hit from below, it gets hit from above. The hits from above are likely to give it more momentum in the x direction; those from below, less. Let’s consider those ariving from above. If they arrive from a position z + ∆z, then they impart x-momentum du ∆p = m(u (z +∆z)−u (z)) ≈ m ∆z (1.8)

x x dz What is the distance ∆z here? Well, this depends on the angle the particles come in at. They have travelled the mean free path l, so if they arrive at θ l l cosθ angle θ then we must have Figure 3: ∆z = lcosθ Here θ ∈ [0,π/2) for particles arriving from above. But the same argument also holds for particles coming in from below. These have θ ∈ (π/2,π] and, correspondingly, – 8 – ∆z < 0 which, from (1.8), tells us that these particles typically absorb momentum from the layer at z.

Our goal is to work out the force per unit area acting on any z slice. This is given by the rate of change of momentum F 1 ∆p = − A A ∆t where the minus sign arises because F defined in (1.6) is the force you need to apply to keep the flow moving (while ∆p/∆t is the force of the fluid pushing back). The rate of change of momentum per unit area is simply the product of our two expressions (1.7)

and (1.8). We have (cid:90)

= −n d3v∆pv f(⃗v)

du (cid:90) (cid:18)

(cid:19)3/2 = −mn x d3vv e−mv2/2kBT lcosθ dz 2πk T We’ve actually done something sly in this second line which is not really justified.

We’re assuming that the fluid has an average velocity ⟨v ⟩ = u in the x-direction.

x x Yet, at the same time we’ve used the Maxwell-Boltzmann distribution for the velocity of the particles which has ⟨v ⟩ = 0. Presumably this is not too bad if the speed of the flow u ≪ ⟨v⟩, the average speed of the particles in the fluid, but we really should be more careful in quantifying this. Nonetheless, the spirit of this section is just to get a heuristic feel for the physics, so let’s push on regardless. Writing the velocity integral in polar coordinates, we have F = −mn du x (cid:90) dvv2 (cid:90) π dθ sinθ (cid:90) 2π dϕ(−vcosθ)lcosθ (cid:18) m (cid:19)3/2 e − 2 m kB v2 T (1.9)

A dz 2πk T 0 0 B At this stage we can trivially do the (cid:82)

dϕ integral and (cid:82)π dθcos2θsinθ = 2/3. We’re left with F mnldu (cid:90) (cid:18)

(cid:19)3/2 = x dv4πv3 e−βmv2/2 (1.10)

A 3 dz 2πk T (cid:82)

But the integral dv is simply the expre expression for the average speed ⟨v⟩ in the gas. We have our final expression, F = 1 du = mnl⟨v⟩ A 3 dz Comparing with (1.6), our expression for the viscosity is η = mnl⟨v⟩ (1.11)

There is something surprising about the viscosity: it is independent of the density n = N/V of the gas. At first sight that looks like a wrong statement because, obviously, there is a factor of n sitting in (1.11). But remember that the mean free path depends inversely on the density, l ∼ 1/n, as we can see from (1.2). The fact that the viscosity does not depend on the fluid density is rather counterintuitive. You might think that denser gasses should be more viscous. But the derivation above provides the explanation for this behaviour: if you halve the density, there are half as many molecules moving down. But each travels twice as far and therefore imparts twice the momentum kick ∆p when they finally hit.

The expression (1.11) holds a special place in the history of physics. It was first derived by Maxwell and is arguably the first truly novel prediction that was made using kinetic theory, providing important evidence for the existence of atoms which, at the time, were not universally believed. Indeed, Maxwell himself was surprised by the fact that η is independent of the density of the gas, writing at the time “Such a consequence of the mathematical theory is very startling and the only experiment I have met with on the subject does not seem to confirm it”.

Maxwell rose to the challenge, building the apparatus and performing the experiment that confirmed his own prediction.

1.3.3 Thermal Conductivity The next transport process we will look at is the conduction of heat. Place a fluid between two plates, each held at a different temperature. Empirically, one finds a flow of energy in the fluid. This is described by the heat flow vector, ⃗q, defined by the energy per unit time passing through a unit area (which is perpendicular to ⃗q). Empirically, the flow of heat is proportional to the temperature gradient, ⃗q = −κ∇T (1.12)

where κ is called the thermal conductivity. Once again, we would like to derive both this empirical law, as well as an expression for κ.

Our calculation follows the same path that we took to determine the viscosity. Let’s set up a temperature gradient in the z-direction. The number of particles with velocity ⃗v that pass through a slab at position z per unit time per unit area is again given by (1.7). We’ll use equipartition and assume that the average energy of a particle at position z is given by E(z) = 3/2 k_B T(z)

We also need to know how particles deposit or gain energy when they reach the slab. If a particle came from a hot place with temperature T(z+∆z), we’ll assume the particle deposits the difference in energy. Similarly, if the particle arrives from a colder place, we’ll assume it absorbs the difference. This means ∆E = E(z +∆z)−E(z) = 3/2 k_B dT/dz ∆z Recall that the height ∆z from which the particle arrives depends on both the mean free path and the angle at which it comes in: ∆z = lcosθ.

As in the derivation of the viscosity, there is something a little dodgy in what we’ve written above. We’ve equated the energy deposited or gained by a particle with the average energy. But this energy transfer will certainly depend on the velocity of the particle and which is dictated by the Maxwell-Boltzmann distribution in (1.7). As in the derivation of the viscosity, we will simply ignore this fact and proceed. We’ll do better in the next section.

Modulo the concerns above, we now have enough information to compute the heat flow. It is |⃗q| = ∫ n d³v ∆E v f(v)

Doing the integrals d³v using the same steps that took us from (1.9) to (1.10), we derive the law of heat flow (1.12)

|⃗q| = − 1/2 k_B nl⟨v⟩ dT/dz The thermal conductivity is the proportionality constant. It is usually expressed in terms of the specific heat, c_V, of the ideal gas κ = c_V l⟨v⟩ (1.13)

where c_V = 3/2 n k_B 1.3.4 Conservation Means Diffusion Thermal conductivity is all about the transport of energy; viscosity is about the transport of momentum. But both energy and momentum have a very special property: they are conserved.

What’s more, because physics is local, we can make a stronger statement than just “the total energy doesn’t change”. If the energy in some region of space, E(⃗x), changes then it must show up in a neighbouring region of space. But that’s exactly what the heat flow ⃗q is telling us: how energy is moving from one point to the next. This local conservation law is captured by the equation.

dE/dt +∇·⃗q = 0 Once again equating energy with the thermal energy, E(⃗x) = 3/2 k_B T(⃗x), the continuity equation reads dT/dt = − 1/c_V ∇·⃗q = κ/c_V ∇²T (1.14)

This is the heat equation. It tells us that any inhomogeneities in temperature are smoothed out through diffusion with diffusion constant D = κ/c_V = 1/3 l⟨v⟩ ∼ l²/τ.

There is a similar story for momentum, p_i where i = 1,2,3 labels the three directions of space. The co continuity equation reads $$ \frac{\partial P_{ji}}{\partial x_j} + \frac{dp_i}{dt} = 0 $$ where $P_{ji}$ is the pressure tensor which describes the flux of $i$-momentum in the $j$-direction.

But looking back at our derivation of the viscosity in Section 1.3.2, this is precisely what we equated to the force $F/A$: the flux of $x$-momentum in the $z$-direction. (Actually there's an extra minus sign that follows from our previous definition of $F$). Combining the continuity equation with our earlier expression for the viscosity, we find $$ \frac{dp_x}{dt} = m n \frac{du}{dt} = \eta \frac{d^2u}{dz^2} $$ where, as in Section 1.3.2, we've restricted to situations with no velocity gradients in the $x$ and $y$ directions. The result is once again a diffusion equation, this time for gradients in velocity. And, once again, the diffusion constant given by $D = \eta/mn = \frac{1}{3} l \langle v \rangle \sim l^2/\tau$.

We learn that all roads lead to diffusion. For any conserved quantity – whether particle number, energy or momentum – any inhomogeneities in the system are smoothed away through the diffusion equation.

The equations that we've written down in this final section are rather hand-waving and, in cases, missing some interesting physics. The proper equations are those of hydrodynamics. The goal of the next section is to do a better job in deriving these.

## 2. Kinetic Theory

The purpose of this section is to lay down the foundations of kinetic theory, starting from the Hamiltonian description of $10^{23}$ particles, and ending with the Navier-Stokes equation of fluid dynamics. Our main tool in this task will be the Boltzmann equation. This will allow us to provide derivations of the transport properties that we sketched in the previous section, but without the more egregious inconsistencies that crept into our previous attempt. But, perhaps more importantly, the Boltzmann equation will also shed light on the deep issue of how irreversibility arises from time-reversible classical mechanics.

## 2.1 From Liouville to BBGKY

Our starting point is simply the Hamiltonian dynamics for $N$ identical point particles. Of course, as usual in statistical mechanics, here $N$ is ridiculously large: $N \sim O(10^{23})$ or something similar. We will take the Hamiltonian to be of the form $$ H = \sum_{i=1}^{N} \frac{\vec{p}_i^2}{2m} + \sum_{i=1}^{N} V(\vec{r}_i) + \sum_{i<j} U(\vec{r}_i - \vec{r}_j) \tag{2.1} $$ The Hamiltonian contains an external force $\vec{F} = -\nabla V$ that acts equally on all particles. There are also two-body interactions between particles, captured by the potential energy $U(\vec{r}_i - \vec{r}_j)$. At some point in our analysis (around Section 2.2.3) we will need to assume that this potential is short-ranged, meaning that $U(r) \approx 0$ for $r \gg d$ where, as in the last Section, $d$ is the atomic distance scale.

Hamilton's equations are $$ \frac{\partial \vec{p}_i}{\partial t} = -\frac{\partial H}{\partial \vec{r}_i}, \quad \frac{\partial \vec{r}_i}{\partial t} = \frac{\partial H}{\partial \vec{p}_i} \tag{2.2} $$ Our interest in this section will be in the evolution of a probability distribution, $f(\vec{r}_i, \vec{p}_i; t)$ over the $6N$ dimensional phase space. This function tells us the probability that the system will be found in the vicinity of the point $(\vec{r}_i, \vec{p}_i)$. As with all probabilities, the function is normalized as $$ \int \prod_{i=1}^{N} dV_i f(\vec{r}_i, \vec{p}_i; t) = 1 \quad \text{with} \quad dV_i = d^3r_i d^3p_i $$ Furthermore, because probability is locally conserved, it must obey a continuity equation: any change of probability in one part of phase space must be compensated by a flow into neighbouring regions. But now we're thinking in terms of phase space, the "$\nabla$" term in the continuity equation includes both $\partial/\partial \vec{r}_i$ and $\partial/\partial \vec{p}_i$ and, correspondingly, the velocity vector in phase space is $(\dot{\vec{r}}_i, \dot{\vec{p}}_i)$. The continuity equation of the probability distribution is then $$ \frac{\partial f}{\partial t} + \sum_i \frac{\partial}{\partial \vec{r}_i} \cdot (\dot{\vec{r}}_i f) + \sum_i \frac{\partial}{\partial \vec{p}_i} \cdot (\dot{\vec{p}}_i f) = 0 $$ where we're using the convention that we sum over the repeated index $i = 1,...,N$. But, using Hamilton's equations (2.2), this becomes $$ \frac{\partial f}{\partial t} + \sum_i \frac{\partial}{\partial \vec{r}_i} \cdot \left( f \frac{\partial H}{\partial \vec{p}_i} \right) - \sum_i \frac{\partial}{\partial \vec{p}_i} \cdot \left( f \frac{\partial H}{\partial \vec{r}_i} \right) = 0 $$ $$ \Rightarrow \frac{\partial f}{\partial t} + \sum_i \frac{\partial f}{\partial \vec{r}_i} \cdot \frac{\partial H}{\partial \vec{p}_i} - \sum_i \frac{\partial f}{\partial \vec{p}_i} \cdot \frac{\partial H}{\partial \vec{r}_i} = 0 $$ This final equation is the Liouville's equation. It is the statement that probability doesn't change as you follow it along any trajectory in phase space, as is seen by writing the Liouville equation as a total derivative, $$ \frac{df}{dt} = \frac{\partial f}{\partial t} + \sum_i \dot{\vec{r}}_i \cdot \frac{\partial f}{\partial \vec{r}_i} + \sum_i \dot{\vec{p}}_i \cdot \frac{\partial f}{\partial \vec{p}_i} = 0 $$ To get a feel for how probability distributions evolve, one often evokes the closely related Liouville's theorem$^2$. This is the statement that if you follow some region of phase space under Hamiltonian evolution, then its shape can change but its volume remains the same. This means that the probability distribution on phase space acts like an incompressible fluid. Suppose, for example, that it's a constant, $f$, over some region of phase space and zero everywhere else. Then the distribution can't spread out over a larger volume, lowering its value. Instead, it must always be $f$ over some region of phase space. The shape and position of this region can change, but not its volume.

The Liouville equation is often written using the Poisson bracket, $$ \{A,B\} = \sum_i \left( \frac{\partial A}{\partial \vec{r}_i} \cdot \frac{\partial B}{\partial \vec{p}_i} - \frac{\partial A}{\partial \vec{p}_i} \cdot \frac{\partial B}{\partial \vec{r}_i} \right)

$$ With this notation, Liouville’s equation becomes simply ∂f/∂t = {H,f} A fuller discussion of Hamiltonian mechanics and Liouville’s theorem can be found in the lectures on Classical Dynamics.

It’s worth making a few simple comments about these probability distributions. Firstly, an equilibrium distribution is one which has no explicit time dependence: ∂f/∂t = 0 which holds if {H,f} = 0. One way to satisfy this is if f is a function of H and the most famous example is the Boltzmann distribution, f ∼ e−βH. However, notice that there is nothing (so-far!) within the Hamiltonian framework that requires the equilibrium distribution to be Boltzmann: any function that Poisson commutes with H will do the job. We’ll come back to this point in Section 2.2.2.

Suppose that we have some function, A(⃗r_i, p⃗_i), on phase space. The expectation value of this function is given by ⟨A⟩ = ∫ dV A(⃗r_i, p⃗_i) f(⃗r_i, p⃗_i; t) (2.3)

This expectation value changes with time only if there is explicit time dependence in the distribution. (For example, this means that in equilibrium ⟨A⟩ is constant). We have d⟨A⟩/dt = ∫ dV A ∂f/∂t = ∫ dV A (∂f/∂p⃗_i · ∂H/∂⃗r_i - ∂f/∂⃗r_i · ∂H/∂p⃗_i)

= ∫ dV (- ∂A/∂p⃗_i · ∂H/∂⃗r_i + ∂A/∂⃗r_i · ∂H/∂p⃗_i) f (2.4)

where we have integrated by parts to get to the last line, throwing away boundary terms which is justified in this context because f is normalized which ensures that we must have f → 0 in asymptotic parts of phase space. Finally, we learn that d⟨A⟩/dt = ∫ dV {A,H} f = ⟨{A,H}⟩ (2.5)

This should be ringing some bells. The Poisson bracket notation makes these expressions for classical expectation values look very similar to quantum expectation values.

2.1.1 The BBGKY Hierarchy Although we’re admitting some ignorance in our description of the system by considering a probability distribution over N-particle phase space, this hasn’t really made our life any easier: we still have a function of ∼ 10^23 variables. To proceed, the plan is to limit our ambition. We’ll focus not on the probability distribution for all N particles but instead on the one-particle distribution function. This captures the expected number of particles lying at some point (⃗r, p⃗). It is defined by f_1(⃗r, p⃗; t) = N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N f(⃗r, ⃗r_2, ..., ⃗r_N, p⃗, p⃗_2, ..., p⃗_N; t)

Although we seem to have singled out the first particle for special treatment in the above expression, this isn’t really the case since all N of our particles are identical. This is also reflected in the factor N which sits out front which ensures that f_1 is normalized as ∫ d^3r d^3p f_1(⃗r, p⃗; t) = N (2.6)

For many purposes, the function f_1 is all we really need to know about a system. In particular, it captures many of the properties that we met in the previous chapter. For example, the average density of particles in real space is simply n(⃗r; t) = ∫ d^3p f_1(⃗r, p⃗; t) (2.7)

The average velocity of particles is ⃗u(⃗r; t) = ∫ d^3p (p⃗/m) f_1(⃗r, p⃗; t) (2.8)

and the energy flux is ⃗E(⃗r; t) = ∫ d^3p E(p⃗) f_1(⃗r, p⃗; t) (2.9)

where we usually take E(p⃗) = p^2/2m. All of these quantities (or at least close relations) will be discussed in some detail in Section 2.4.

Ideally we’d like to derive an equation governing f_1. To see how it changes with time, we can simply calculate: ∂f_1/∂t = N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N ∂f/∂t = N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N {H,f} Using the Hamiltonian given in (2.1), this becomes ∂f_1/∂t = N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N [ -∑_j (p⃗_j/m) · ∂f/∂⃗r_j + ∑_j ∂V/∂⃗r_j · ∂f/∂p⃗_j + ∑_{k<l} ∂U(⃗r_k - ⃗r_l)/∂⃗r_j · ∂f/∂p⃗_j ]

Now, whenever j = 2,...N, we can always integrate by parts to move the derivatives away from f and onto the other terms. And, in each case, the result is simply zero because when the derivative is with respect to ⃗r_j, the other terms depend only on p⃗_i and vice-versa. We’re left only with the terms that involve derivatives with respect to ⃗r_1 and p⃗_1 because we can’t integrate these by parts. Let’s revert to our previous notation and call ⃗r_1 ≡ ⃗r and p⃗_1 ≡ p⃗. We have ∂f_1/∂t = N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N [ - (p⃗/m) · ∂f/∂⃗r + ∂V(⃗r)/∂⃗r · ∂f/∂p⃗ + ∑_k ∂U(⃗r - ⃗r_k)/∂⃗r · ∂f/∂p⃗ ]

= {H_1, f_1} + N ∫ d^3r_2 ... d^3r_N d^3p_2 ... d^3p_N ∑_k ∂U(⃗r - ⃗r_k)/∂⃗r · ∂f/∂p⃗ (2.10)

where we have defined the one-particle Hamiltonian H_1 = p^2/2m + V(⃗r) (2.11)

Notice that H_1 includes the external force V acting on the particle, but it knows nothing about the interaction with the other particles. All of that information is included in the last term with U(⃗r - ⃗r_k). We see that the evolution of the one-particle distribution function is described by a Liouville-like equation, together with an extra term. We write ∂f_1/∂t = {H_1, f_1} + (∂f_1/∂t)_coll (2.12)

The first term is sometimes referred to as the streaming term.

streaming term. It tells you how the particles move in the absence of collisions. The second term, known as the collision integral, is given by the second term in (2.10). In fact, because all particles are the same, each of the (N −1) terms in ∑_{k=2}^{N} in (2.10) are identical and we can write

∂f₁/∂t = N(N −1) ∫d³r₂ ∫d³p₂ · (∂U(⃗r₁−⃗r₂)/∂⃗r₂) · (∂/∂⃗p₂) ∏_{i=3}^{N} ∫d³r_i ∫d³p_i f(⃗r₁,⃗r₂,...,⃗p₁,⃗p₂,...;t)

But now we’ve got something of a problem. The collision integral can’t be expressed in terms of the one-particle distribution function. And that’s not really surprising. As the name suggests, the collision integral captures the interactions – or collisions – of one particle with another. Yet f contains no information about where any of the other particles are in relation to the first. However some of that information is contained in the two-particle distribution function,

f₂(⃗r₁,⃗r₂,⃗p₁,⃗p₂;t) ≡ N(N −1) ∫d³r_i ∫d³p_i ∏_{i=3}^{N} f(⃗r₁,⃗r₂,...,⃗p₁,⃗p₂,...;t)

With this definition, the collision integral is written simply as

∂f₁/∂t|_{coll} = ∫d³r₂ ∫d³p₂ · (∂U(⃗r₁−⃗r₂)/∂⃗r₂) · (∂f₂/∂⃗p₂) (2.13)

The collision term doesn’t change the distribution of particles in space. This is captured by the particle density (2.7) which we get by simply integrating n = ∫d³p f. But, after integrating over d³p, we can perform an integrating by parts in the collision integral to see that it vanishes. In contrast, if we’re interested in the distribution of velocities – such as the current (2.8) or energy flux (2.9) – then the collision integral is important.

The upshot of all of this is that if we want to know how the one-particle distribution function evolves, we also need to know something about the two-particle distribution function. But we can always figure out how f₂ evolves by repeating the same calculation that we did above for f₁. It’s not hard to show that f₂ evolves by a Liouville-like equation, but with a corrected term that depends on the three-particle distribution function f₃. And f₃ evolves in a Liouville manner, but with a correction term that depends on f₄, and so on. In general, the n-particle distribution function

f_n(⃗r₁,...,⃗r_n,⃗p₁,...,⃗p_n;t) = N!/(N−n)! ∫d³r_i ∫d³p_i ∏_{i=n+1}^{N} f(⃗r₁,...,⃗r_N,⃗p₁,...,⃗p_N;t)

obeys the equation

∂f_n/∂t = {H_n, f_n} + ∑_{i=1}^{n} ∫d³r_{n+1} ∫d³p_{n+1} · (∂U(⃗r_i−⃗r_{n+1})/∂⃗r_i) · (∂f_{n+1}/∂⃗p_i) (2.14)

where the effective n-body Hamiltonian includes the external force and any interactions between the n particles but neglects interactions with any particles outside of this set,

H_n = ∑_{i=1}^{n} (⃗p_i²/(2m) + V(⃗r_i)) + ∑_{i<j≤n} U(⃗r_i−⃗r_j)

The equations (2.14) are known as the BBGKY hierarchy. (The initials stand for Bogoliubov, Born, Green, Kirkwood and Yvon). They are telling us that any group of n particles evolves in a Hamiltonian fashion, corrected by interactions with one of the particles outside that group. At first glance, it means that there’s no free lunch; if we want to understand everything in detail, then we’re going to have to calculate everything. We started with the Liouville equation governing a complicated function f of N ∼ O(10²³) variables and it looks like all we’ve done is replace it with O(10²³) coupled equations.

However, there is an advantage in working with the hierarchy of equations (2.14) because they isolate the interesting, simple variables, namely f₁ and other lower f_n. This means that the equations are in a form that is ripe to start implementing various approximations. Given a particular problem, we can decide which terms are important and, ideally, which terms are so small that they can be ignored, truncating the hierarchy to something manageable. Exactly how you do this depends on the problem at hand. Here we explain the simplest, and most useful, of these truncations: the Boltzmann equation.

## 2.2 The Boltzmann Equation

“Elegance is for tailors” Ludwig Boltzmann

In this section, we explain how to write down a closed equation for f₁ alone. This will be the famous Boltzmann equation. The main idea that we will use is that there are two time scales in the problem. One is the time between collisions, τ, known as the scattering time or relaxation time. The second is the collision time, τ_coll, which is roughly the time it takes for the process of collision between particles to occur. In situations where

τ ≫ τ_coll (2.15)

we should expect that, for much of the time, f₁ simply follows its Hamiltonian evolution with occasional perturbations by the collisions. This, for example, is what happens for the dilute gas. And this is the regime we will work in from now on.

At this stage, there is a right way and a less-right way to proceed. The right way is to derive the Boltzmann equation starting from the BBGKY hierarchy. And we will do this in Section 2.2.3. However, as we shall see, it’s a little fiddly. So instead we’ll start by taking the less-right option which has the advantage of getting the same answer but in a much easier fashion. This option is to simply guess what form the Boltzmann equation has to take.

2.2.1 Motivating the Boltzmann Equation We’ve already caught our first glimpse of the Boltzmann equation in (2.12), ∂f/∂t = {H₁,f} + (∂f/∂t)_coll (2.16)

But, of course, we don’t yet have an expression for the collision integral in terms of f. It’s clear from the definition (2.13) that the second term represents the change in momenta due to two-particle scattering. When τ ≫ τ_coll, the collisions occur occasionally, but abruptly. The collision integral should reflect the rate at which these collisions occur.

Suppose that our particle sits at (⃗r,p⃗) in phase space and collides with another particle at (⃗r,p⃗₂). Note that we’re assuming here that collisions are local in space so that the two particles sit at the same point. These particles can collide and emerge with momenta p⃗₁′ and p⃗₂′. We’ll define the rate for this process to occur to be Rate = ω(p⃗,p⃗₂|p⃗₁′,p⃗₂′)f₂(⃗r,⃗r,p⃗,p⃗₂)d³p₂d³p₁′d³p₂′ (2.17)

(Here we’ve dropped the explicit t dependence of f only to keep the notation down). The scattering function ω contains the information about the dynamics of the process. It looks as if this is a new quantity which we’ve introduced into the game. But, using standard classical mechanics techniques, one can compute ω for a given inter-atomic potential U(⃗r). (It is related to the differential cross-section; we will explain how to do this when we do things better in Section 2.2.3). For now, note that the rate is proportional to the two-body distribution function f₂ since this tells us the chance that two particles originally sit in (⃗r,p⃗) and (⃗r,p⃗₂).

We’d like to focus on the distribution of particles with some specified momentum p⃗. Two particles with momenta p⃗ and p⃗₂ can be transformed in two particles with momenta p⃗₁′ and p⃗₂′. Since both momenta and energy are conserved in the collision, we have p⃗ + p⃗₂ = p⃗₁′ + p⃗₂′ (2.18)

p² + p₂² = p₁′² + p₂′² (2.19)

There is actually an assumption that is hiding in these equations. In general, we’re considering particles in an external potential V. This provides a force on the particles which, in principle, could mean that the momentum and kinetic energy of the particles is not the same before and after the collision. To eliminate this possibility, we will assume that the potential only varies appreciably over macroscopic distance scales, so that it can be neglected on the scale of atomic collisions. This, of course, is entirely reasonable for most external potentials such as gravity or electric fields. Then (2.18) and (2.19) continue to hold.

While collisions can deflect particles out of a state with momentum p⃗ and into a different momentum, they can also deflect particles into a state with momentum p⃗. This suggests that the collision integral should contain two terms, (∂f₁/∂t)_coll = ∫ d³p₂d³p₁′d³p₂′ [ω(p⃗₁′,p⃗₂′|p⃗,p⃗₂)f₂(⃗r,⃗r,p⃗₁′,p⃗₂′) − ω(p⃗,p⃗₂|p⃗₁′,p⃗₂′)f₂(⃗r,⃗r,p⃗,p⃗₂)]

The first term captures scattering into the state p⃗, the second scattering out of the state p⃗.

The scattering function obeys a few simple requirements. Firstly, it is only non-vanishing for scattering events that obey the conservation of momentum (2.18) and energy (2.19). Moreover, the discrete symmetries of spacetime also give us some important information. Under time reversal, p⃗ → −p⃗ and, of course, what was coming in is now going out. This means that any scattering which is invariant under time reversal (which is more or less anything of interest) must obey ω(p⃗,p⃗₂|p⃗₁′,p⃗₂′) = ω(−p⃗₁′,−p⃗₂′|−p⃗,−p⃗₂)

Furthermore, under parity (⃗r,p⃗) → (−⃗r,−p⃗). So any scattering process which is parity invariant further obeys ω(p⃗,p⃗₂|p⃗₁′,p⃗₂′) = ω(−p⃗,−p⃗₂|−p⃗₁′,−p⃗₂′)

The combination of these two means that the scattering rate is invariant under exchange of ingoing and outgoing momenta, ω(p⃗,p⃗₂|p⃗₁′,p⃗₂′) = ω(p⃗₁′,p⃗₂′|p⃗,p⃗₂) (2.20)

(There is actually a further assumption of translational invariance here, since the scattering rate at position −⃗r should be equivalent to the scattering rate at position +⃗r). The symmetry property (2.20) allows us to simplify the collision integral to (∂f₁/∂t)_coll = ∫ d³p₂d³p₁′d³p₂′ ω(p⃗₁′,p⃗₂′|p⃗,p⃗₂) [f₂(⃗r,⃗r,p⃗₁′,p⃗₂′) − f₂(⃗r,⃗r,p⃗,p⃗₂)] (2.21)

To finish the derivation, we need to face up to our main goal of expressing the collision integral in terms of f₁ rather than f₂. We make the assumption that the velocities of two particles are uncorrelated, so that we can write f₂(⃗r,⃗r,p⃗,p⃗₂) = f₁(⃗r,p⃗)f₁(⃗r,p⃗₂) (2.22)

This assumption, which sometimes goes by the name of molecular chaos, seems innocuous enough. But actually it is far from innocent! To see why, let’s look 更仔细地审视我们实际所做的假设。观察式(2.21)，我们看到碰撞率被假定为正比于 f(⃗r, p⃗₁, p⃗₂)，其中 p⃗₁ 和 p⃗₂ 是碰撞前粒子的动量。这意味着，如果我们将式(2.22)代入(2.21)，我们实际上假设了碰撞前速度是不相关的。这听起来相当合理：你可以想象在碰撞过程中，两个粒子之间的速度变得相关。但在那之后，会有一段很长的时间 τ，直到其中一个粒子经历下一次碰撞。而且，这次碰撞通常是与一个完全不同的粒子发生的，这个新粒子的速度似乎与第一个粒子的速度毫无关系。然而，我们假设速度在碰撞前不相关而非碰撞后不相关，这一点相当巧妙地在博弈中引入了时间箭头。这具有深远的影响，我们将在推导 H 定理的第 2.3 节中看到。

最后，我们可以写下由下式给出的单粒子分布函数演化的封闭表达式： ∂f₁/∂t = {H₁, f₁} + (∂f₁/∂t)_coll  (2.23)

其中碰撞积分为： (∂f₁/∂t)_coll = ∫ d³p₂ d³p₁' d³p₂' ω(p⃗₁', p⃗₂' | p⃗₁, p⃗₂) [f₁(⃗r, p⃗₁') f₂(⃗r, p⃗₂') - f₁(⃗r, p⃗₁) f₂(⃗r, p⃗₂)]  (2.24)

这就是玻尔兹曼方程。它不是一个容易求解的方程！左边是微分方程，右边是积分，并且是非线性的。你可能不会惊讶地听到，精确解并不容易得到。我们将看看我们能做些什么。

2.2.2 平衡与细致平衡让我们通过重新审视满足 ∂f_eq/∂t = 0 的平衡分布问题，开始对玻尔兹曼方程的探索。我们已经知道，如果 f 是能量的任何函数，或者实际上是任何与 H 泊松对易的函数，那么 {f, H₁} = 0。为了清晰起见，让我们限制在外部力为零的情况，即 V(⃗r) = 0。那么，如果我们只看刘维尔方程，动量的任何函数都是平衡分布。但是碰撞积分的贡献呢？使碰撞积分为零的一个明显方法是找到一个满足细致平衡条件的分布： f_eq(⃗r, p⃗₁') f_eq(⃗r, p⃗₂') = f_eq(⃗r, p⃗₁) f_eq(⃗r, p⃗₂)  (2.25)

实际上，将其写成以下形式更有用： log(f_eq(⃗r, p⃗₁')) + log(f_eq(⃗r, p⃗₂')) = log(f_eq(⃗r, p⃗₁)) + log(f_eq(⃗r, p⃗₂))  (2.26)

我们如何确保这对所有动量都成立？右边的动量是碰撞前的；左边的是碰撞后的。从(2.26)的形式可以清楚地看出，log f_eq 的和在碰撞前后必须相同：换句话说，这个和在碰撞过程中必须守恒。但我们知道碰撞过程中什么量是守恒的：动量和能量，分别如式(2.18)和(2.19)所示。这意味着我们应该取： log(f_eq(⃗r, p⃗)) = β(μ - E(p⃗) + ⃗u·p⃗)  (2.27)

其中对于非相对论性粒子，E(p⃗) = p²/2m，而 μ、β 和 ⃗u 都是常数。我们将调整常数 μ 以确保 f 的整体归一化满足式(2.6)。然后，令 p⃗ = m⃗v，我们有： f_eq(⃗r, p⃗) = (V / (2πm))^{3/2} exp[-βm(⃗v - ⃗u)²/2]  (2.28)

如果我们将 β 识别为温度的倒数，这就重现了麦克斯韦-玻尔兹曼分布。这里 ⃗u 允许存在整体漂移速度的可能性。我们了解到，将碰撞项添加到刘维尔方程中，迫使我们在平衡时处于玻尔兹曼分布。

这里有一个评论，将在第 2.4 节中发挥重要作用。如果我们忽略流项 {H₁, f₁}，那么满足细致平衡条件(2.25)的解集要大得多。这些解仍然具有(2.27)的形式，但现在常数 μ、β 和 ⃗u 被提升为空间和时间的函数。换句话说，我们可以有： f_local(⃗r, p⃗; t) = n(⃗r, t) [β(⃗r, t) / (2πm)]^{3/2} exp{-β(⃗r, t) [m(⃗v - ⃗u(⃗r, t))²/2]}  (2.29)

这样的分布并不完全是平衡分布，因为虽然(2.23)中的碰撞积分为零，但流项并不为零。尽管如此，这类分布在后续内容中将被证明很重要。它们被称为处于局部平衡状态，粒子密度、温度和漂移速度在空间上变化。

量子玻尔兹曼方程我们上面的讨论完全针对经典粒子，并且在本节的剩余部分中，这将继续是我们的重点。然而，作为一个小插曲，让我们看看对于量子粒子情况会如何变化。我们将保持分子混沌的假设，因此 f₂ ~ f₁ f₁，如式(2.22)所示。主要区别出现在散射过程 p⃗₁ + p⃗₂ → p⃗₁' + p⃗₂' 的散射率(2.17)中，现在变为： Rate = ω(p⃗₁', p⃗₂' | p⃗₁, p⃗₂)

⃗,p⃗ |p⃗′,p⃗′)f (p⃗ )f (p⃗ ){1±f (p⃗′)}{1±f(p⃗′)}d3p d3p′d3p′ 2 1 2 1 1 1 2 1 1 2 2 1 2 The extra terms are in curly brackets. We pick the + sign for bosons and the − sign for fermions. The interpretation is particularly clear for fermions, where the number of particles in a given state can’t exceed one. Now it’s not enough to know the probability that initial state is filled. We also need to know that probability that the final state is free for the particle to scatter into: and that’s what the {1−f } factors are telling us. The remaining arguments go forward as before, resulting in the quantum Boltzmann equation (cid:18) (cid:19) (cid:90)

∂f (cid:104)

1 = d3p d3p′d3p′ ω(p⃗′,p⃗′|p⃗,p⃗ ) f (p⃗′)f (p⃗′){1±f (p⃗)}{1±f (p⃗ } ∂t 2 1 2 1 2 2 1 1 1 2 1 1 2 coll (cid:105)

−f (p⃗)f (p⃗ ){1±f (p⃗′)}{1±f (⃗r,p⃗′)} 1 1 2 1 1 1 2 To make contact with what we know, we can look again at the requirement for equilibrium. The condition of detailed balance now becomes (cid:18) feq(p⃗′) (cid:19) (cid:18) feq(p⃗′) (cid:19) (cid:18) feq(p⃗) (cid:19) (cid:18) feq(p⃗ ) (cid:19)

log 1 1 +log 1 2 = log 1 +log 1 2 1±feq(p⃗′) 1±feq(p⃗′) 1±feq(p⃗) 1±feq(p⃗ )

1 1 1 2 1 1 2 Which is again solved by relating each log to a linear combination of the energy and momentum. We find feq(p⃗) = 1 e−β(µ−E(p⃗)+⃗u·p⃗) ∓1 which reproduces the Bose-Einstein and Fermi-Dirac distributions.

2.2.3 A Better Derivation In Section 2.2.1, we derived an expression for the collision integral (2.24) using intuition for the scattering processes at play. But, of course, we have a mathematical expression for the collision integral in (2.13) involving the two-particle distribution function f . In this section we will sketch how one can derive (2.24) from (2.13). This will help clarify some of the approximations that we need to use. At the same time, we will also review some basic classical mechanics that connects the scattering rate ω to the inter-particle potential U(r).

We start by returning to the BBGKY hierarchy of equations. For simplicity, we’ll turn off the external potential V(⃗r) = 0. We don’t lose very much in doing this because most of the interesting physics is concerned with the scattering of atoms off each other. The first two equations in the hierarchy are (cid:18) (cid:19) (cid:90)

∂ p⃗ ∂ ∂U(⃗r −⃗r ) ∂f + 1 · f = d3r d3p 1 2 · 2 (2.30)

1 2 2 ∂t m ∂⃗r ∂⃗r ∂p⃗ 1 1 1 and (cid:18) (cid:20) (cid:21)(cid:19)

∂ p⃗ ∂ p⃗ ∂ 1∂U(⃗r −⃗r ) ∂ ∂ 1 2 1 2 + · + · − · − f = (2.31)

∂t m ∂⃗r m ∂⃗r 2 ∂⃗r ∂p⃗ ∂p⃗ 1 2 1 1 2 (cid:90) (cid:18) (cid:19)

∂U(⃗r −⃗r ) ∂ ∂U(⃗r −⃗r ) ∂ d3r d3p 1 3 · + 2 3 · f 3 3 3 ∂⃗r ∂p⃗ ∂⃗r ∂p⃗ 1 1 2 2 In both of these equations, we’ve gathered the streaming terms on the left, leaving only the higher distribution function on the right. To keep things clean, we’ve suppressed the arguments of the distribution functions: they are f = f (⃗r ,p⃗ ;t) and 1 1 1 1 f = f (⃗r ,⃗r ,p⃗ ,p⃗ ;t) and you can guess the arguments for f .

2 2 1 2 1 2 3

Our goal is to better understand the collision integral on the right-hand-side of (2.30). It seems reasonable to assume that when particles are far-separated, their distribution functions are uncorrelated. Here, “far separated” means that the distance between them is much farther than the atomic distance scale d over which the potential U(r) extends. We expect f (⃗r ,⃗r ,p⃗ ,p⃗ ;t) → f (⃗r ,p⃗ ;t)f (⃗r ,p⃗ ;t) when |⃗r −⃗r | ≫ d 2 1 2 1 2 1 1 1 1 2 2 1 1 But, a glance at the right-hand-side of (2.30) tells us that this isn’t the regime of interest. Instead, f is integrated ∂U(r)/∂r which varies significantly only over a region r ≤ d. This means that we need to understand f when two particles get close to each other.

We’ll start by getting a feel for the order of magnitude of various terms in the hierarchy of equations. Dimensionally, each term in brackets in (2.30) and (2.31) is an inverse time scale. The terms involving the inter-atomic potential U(r) are associated to the collision time τ .

coll 1 ∂U ∂ ∼ · τ ∂⃗r ∂p⃗ coll This is the time taken for a particle to cross the distance over which the potential U(r) varies which, for short range potentials, is comparable to the atomic distance scale, d, itself and τ ∼ coll v¯ rel where v¯ is the average relative speed between atoms. Our first approximation will be that this is the shortest time scale in the problem. This means that the terms involving ∂U/∂r are typically the largest terms in the equations above and determine how fast the distribution functions change.

With this in mind, we note that the equation for f is special because it is the only one which does not include any collision terms on the left of the equation (i.e. in the Hamiltonian H ). This means that the collision integral on the right-hand side of (2.30) will usually dominate the rate of change of f . (Note, however, we’ll meet some important exceptions to this statement in Section 2.4). In contrast, the equation that governs f has collision terms on both the left and the right-hand sides.

But, importantly, for dilute gases, the term on the right is much smaller than the term on the left. To see why this is, we need to compare the f3 term to the f2 term. If we were to integrate f over all space, we get ∫ d3r d3p f = Nf2 (where we’ve replaced (N − 2) ≈ N in the above expression). However, the right-hand side of (2.31) is not integrated over all of space. Instead, it picks up a non-zero contribution over an atomic scale ∼ d3. This means that the collision term on the right-hand-side of (2.31) is suppressed compared to the one on the left by a factor of Nd3/V where V is the volume of space. For gases that we live and breath every day, Nd3/V ∼ 10−3−10−4. We make use of this small number to truncate the hierarchy of equations and replace (2.31) with (∂/∂t + (p⃗1/m)·∂/∂⃗r1 + (p⃗2/m)·∂/∂⃗r2 − (∂U(⃗r1−⃗r2)/∂⃗r1)·(∂/∂p⃗1 − ∂/∂p⃗2)) f ≈ 0 (2.32)

This tells us that f2 typically varies on a time scale of τcoll and a length scale of d. Meanwhile, the variations of f1 is governed by the right-hand-side of (2.30) which, by the same arguments that we just made, are smaller than the variations of f2 by a factor of Nd3/V. In other words, f1 varies on the larger time scale τ1.

In fact, we can be a little more careful when we say that f2 varies on a time scale τcoll. We see that – as we would expect – only the relative position is affected by the collision term. For this reason, it’s useful to change coordinate to the centre of mass and the relative positions of the two particles. We write R = (⃗r1 +⃗r2) , ⃗r =⃗r1 −⃗r2 and similar for the momentum P = p⃗1 +p⃗2 , p⃗ = (p⃗1 −p⃗2)/2 And we can think of f2 = f2(R,⃗r,P,p⃗;t). The distribution function will depend on the centre of mass variables R and P in some slow fashion, much as f1 depends on position and momentum. In contrast, the dependence of f2 on the relative coordinates ⃗r and p⃗ is much faster – these vary over the short distance scale and can change on a time scale of order τcoll.

Since the relative distributions in f2 vary much more quickly than f1, we’ll assume that f2 reaches equilibrium and then feeds into the dynamics of f1. This means that, ignoring the slow variations in R and P, we will assume that ∂f2/∂t = 0 and replace (2.32) with the equilibrium condition (p⃗/m)·∂/∂⃗r − (∂U(⃗r)/∂⃗r)·∂/∂p⃗ f2 ≈ 0 (2.33)

This is now in a form that allows us to start manipulating the collision integral on the right-hand-side of (2.30). We have (∂f1/∂t)coll = ∫ d3r d3p (∂U(⃗r1−⃗r2)/∂⃗r1)·(∂f2/∂p⃗1)

= ∫ d3r d3p (∂U(⃗r)/∂⃗r)·(∂/∂p⃗ − ∂/∂p⃗) f2 = (1/m) ∫ d3r d3p (p⃗1 −p⃗2)·(∂f2/∂⃗r) (2.34)

|⃗r1−⃗r2|≤d where in the second line the extra term ∂/∂p⃗ vanishes if we integrate by parts and, in the third line, we’ve used our equilibrium condition (2.33), with the limits on the integral in place to remind us that only the region r ≤ d contributes to the collision integral.

A Review of Scattering Cross Sections To complete the story, we still need to turn (2.34) into the collision integral (2.24). But most of the work simply involves clarifying how the scattering rate ω(p⃗1,p⃗2|p⃗′1,p⃗′2) is defined for a given inter-atomic potential U(⃗r1−⃗r2). And, for this, we need to review the concept of the differential cross section.

Let’s think about the collision between two particles. They start with momenta p⃗i = m⃗vi and end with momenta p⃗′i = m⃗v′i with i = 1,2. Now let’s pick a favourite, say particle 1. We’ll sit in its rest frame and consider an onslaught of bombarding particles, each with velocity ⃗v2 −⃗v1. This beam of incoming particles do not all hit our favourite boy at the same point. Instead, they come in randomly distributed over the plane perpendicular to ⃗v2 −⃗v1. The flux, I, of these incoming particles is the number hitting this plane per area per second, I = |⃗v2 −⃗v1| Now spend some time staring at Figure 4. There are a number of quantities defined in this picture. First, the impact parameter, b, is the distance from the asymptotic trajectory to the dotted, centre line. We will use b and ϕ as polar coordinates to parameterize the plane perpendicular to the incoming particle. Next, the scattering angle, θ, is the angle by which the incoming particle is deflected. Finally, there are two solid angles, dσ and dΩ, depicted in the figure. Geometrically, we see that they are given by dσ = bdbdϕ and dΩ = sinθdθdϕ The number of particles scattered into dΩ in unit time is Idσ. We usually write this as I dσ/dΩ dΩ = Ibdbdϕ (2.35)

where the differential cross section is defined as |dσ/dΩ| = b |db/dθ| / sinθ d(b²) = (2.36)

dΩ sinθ dθ 2 dcosθ

You should think of this in the following way: for a fixed (⃗v₂ −⃗v₁), there is a unique relationship between the impact parameter b and the scattering angle θ and, for a given potential U(r), you need to figure this out to get |dσ/dΩ| as a function of θ.

Now we can compare this to the notation that we used earlier in (2.17). There we talked about the rate of scattering into a small area d³p′₁d³p′₂ in momentum space. But this is the same thing as the differential cross-section.

ω(p⃗,p⃗;p⃗′,p⃗′)d³p′₁d³p′₂ = |⃗v₂ −⃗v₁| |dσ/dΩ| dΩ (2.37)

(Note, if you’re worried about the fact that d³p′₁d³p′₂ is a six-dimensional area while dΩ is a two dimensional area, recall that conservation of energy and momenta provide four restrictions on the ability of particles to scatter. These are implicit on the left, but explicit on the right).

An Example: Hard Spheres

In Section 1.2, we modelled atoms as hard spheres of diameter d. It’s instructive to figure out the cross-section for such a hard sphere.

In fact, there are two different calculations that we can do. First, suppose that we throw point-like particles at a sphere of diameter d with an impact parameter b ≤ d/2. From the left-hand diagram in Figure 5, we see that the scattering angle is θ = π−2α, where

b = (d/2) sinα = (d/2) sin(π/2 − θ/2) = (d/2) cos(θ/2)

or

b² = (d²/4) cos²(θ/2) = (d²/8)(1+cosθ)

From (2.36), we then find the differential cross-section

|dσ/dΩ| = d²/16

The total cross-section is defined as

σ = 2π ∫ dθ sinθ (dσ/dΩ) = π (d/2)²

This provides a nice justification for the name because this is indeed the cross-sectional area of a sphere of radius d/2.

Alternatively, we could consider two identical hard spheres, each of diameter d, one scattering off the other. Now the geometry changes a little, as shown in the right-hand diagram in Figure 5. The impact parameter is now the distance between the centres of the spheres, and given by

b = 2× (d/2) sinα

Clearly we now need b ≤ d. The same calculation as above now gives

σ = πd²

This is the same effective cross-sectional area that we previously used back in Section 1.2 when discussing basic aspects of collisions.

Almost Done

With this refresher course on classical scattering, we can return to the collision integral (2.34) in the Boltzmann equation.

(∂f₁/∂t)_coll = ∫ d³r₂ ∫ d³p₂ (⃗v₂ −⃗v₁)·∇₂

|r₁−r₂|≤d

We’ll work in cylindrical polar coordinates shown in Figure 6. The direction parallel to ⃗v₂ −⃗v₁ is parameterized by x; the plane perpendicular is parameterised by ϕ and the impact parameter b. We’ve also shown the collision zone in this figure. Using the definitions (2.35) and (2.37), we have

(∂f₁/∂t)_coll = ∫ d³p₂ |⃗v₂ −⃗v₁| ∫ dϕ ∫ b db [∂f₂/∂x]_{x₁}^{x₂}

= ∫ d³p₂ ∫ d³p′₁d³p′₂ ω(p⃗′₁,p⃗′₂|p⃗₁,p⃗₂) [f₂(x₂)−f₂(x₁)]

It remains only to decide what form the two-particle distribution function f takes just before the collision at x = x₁ and just after the collision at x = x₂. At this point we invoke the assumption of molecular chaos. Just before we enter the collision, we assume that the two particles are uncorrelated. Moreover, we assume that the two particles are once again uncorrelated by the time they leave the collision, albeit now with their new momenta

f₂(x₁) = f₁(⃗r,p⃗₁;t)f₂(⃗r,p⃗₂;t) and f₂(x₂) = f₁(⃗r,p⃗′₁;t)f₂(⃗r,p⃗′₂;t)

Notice that all functions f are evaluated at the same point ⃗r in space since we’ve assumed that the single particle distribution function is suitably coarse grained that it doesn’t vary on scales of order d. With this final assumption, we get what we wanted: the collision integral is given by

(∂f₁/∂t)_coll = ∫ d³p₂ ∫ d³p′₁d³p′₂ ω(p⃗′₁,p⃗′₂|p⃗₁,p⃗₂) [f₁(⃗r,p⃗′₁)f₂(⃗r,p⃗′₂)−f₁(⃗r,p⃗₁)f₂(⃗r,p⃗₂)]

in agreement with (2.24).

## 2.3 The H-Theorem

The topics of thermodynamics and statistical mechanics are all to do with the equilibrium properties of systems. One of the key intuitive ideas that underpins their importance is that if you wait long enough, any system will eventually settle down to equilibrium. But how do we know this? Moreover, it seems that it would be rather tricky to prove: settling down to equilibrium clearly involves an arrow of time that distinguishes the future from the past. Yet the underlying classical mechanics is invariant under time reversal.

The purpose of this section is to demonstrate that, within the framework of the Boltzmann equation, systems do indeed settle down to equilibrium. As we described abov e, we have introduced an arrow of time into the Boltzmann equation. We didn’t do this in any crude way like adding friction to the system. Instead, we merely assumed that particle velocities were uncorrelated before collisions. That would seem to be a rather minor input but, as we will now show, it’s enough to demonstrate the approach to equilibrium.

Specifically, we will prove the “H-theorem”, named after a quantity H introduced by Boltzmann. (H is not to be confused with the Hamiltonian. Boltzmann originally called this quantity something like a German E, but the letter was somehow lost in translation and the name H stuck). This quantity is H(t) = ∫ d³r d³p f(⃗r, ⃗p; t) log(f(⃗r, ⃗p; t))

This kind of expression is familiar from our first Statistical Mechanics course where we saw that the entropy S for a probability distribution p is S = −k ∫ p log p. In other words, this quantity H is simply S = −k H The H-theorem, first proven by Boltzmann in 1872, is the statement that H always decreases with time. The entropy always increases. We will now prove this.

As in the derivation (2.4), when you’re looking at the variation of expectation values you only care about the explicit time dependence, meaning dH/dt = ∫ d³r d³p (log f + 1) ∂f/∂t = ∫ d³r d³p log f ∂f/∂t where we can drop the +1 because ∫ f = N is unchanging, ensuring that ∂(∫ f)/∂t = 0. Using the Boltzmann equation (2.23), we have dH/dt = ∫ d³r d³p log f · [−(∂V/∂⃗r) · (∂f/∂⃗p) + (⃗p/m) · (∂f/∂⃗r) + ∂f/∂t]coll But the first two terms in this expression both vanish. You can see this by integrating by parts twice, first moving the derivative away from f and onto log f, and then moving it back. We learn that the change in H is governed entirely by the collision terms dH/dt = ∫ d³r d³p log f (∂f/∂t)coll = ∫ d³r d³p d³p₁ d³p₂ d³p₁′ d³p₂′ ω(⃗p₁′, ⃗p₂′|⃗p₁, ⃗p₂) log f(⃗p₁)

× [f(⃗p₁′)f(⃗p₂′) − f(⃗p₁)f(⃗p₂)] (2.38)

where I’ve suppressed ⃗r and t arguments of f to keep things looking vaguely reasonable. I’ve also relabelled the integration variable ⃗p → ⃗p₁. At this stage, all momenta are integrated over so they are really nothing but dummy variables. Let’s relabel 1 ↔ 2 on the momenta. All the terms remain unchanged except the log. So we can also write dH/dt = ∫ d³r d³p d³p₁ d³p₂ d³p₁′ d³p₂′ ω(⃗p₁′, ⃗p₂′|⃗p₁, ⃗p₂) log f(⃗p₂)

× [f(⃗p₁′)f(⃗p₂′) − f(⃗p₁)f(⃗p₂)] (2.39)

Adding (2.38) and (2.39), we have the more symmetric looking expression dH/dt = (1/2) ∫ d³r d³p d³p₁ d³p₂ d³p₁′ d³p₂′ ω(⃗p₁′, ⃗p₂′|⃗p₁, ⃗p₂) log[f(⃗p₁)f(⃗p₂)]

× [f(⃗p₁′)f(⃗p₂′) − f(⃗p₁)f(⃗p₂)] (2.40)

Since all momenta are integrated over, we’re allowed to just flip the dummy indices again. This time we swap ⃗p ↔ ⃗p′ in the above expression. But, using the symmetry property (2.20), the scattering function remains unchanged³. We get dH/dt = −(1/2) ∫ d³r d³p d³p₁ d³p₂ d³p₁′ d³p₂′ ω(⃗p₁′, ⃗p₂′|⃗p₁, ⃗p₂) log[f(⃗p₁′)f(⃗p₂′)]

× [f(⃗p₁′)f(⃗p₂′) − f(⃗p₁)f(⃗p₂)] (2.41)

Finally, we add (2.40) and (2.41) to get dH/dt = −(1/4) ∫ d³r d³p d³p₁ d³p₂ d³p₁′ d³p₂′ ω(⃗p₁′, ⃗p₂′|⃗p₁, ⃗p₂) × {log[f(⃗p₁′)f(⃗p₂′)] − log[f(⃗p₁)f(⃗p₂)]} {f(⃗p₁′)f(⃗p₂′) − f(⃗p₁)f(⃗p₂)} (2.42)

The bottom line of this expression is a function (log x − log y)(x − y). It is positive for all values of x and y. Since the scattering rate is also positive, we have the proof of the H-theorem.

dH/dt ≤ 0 ⇔ dS/dt ≥ 0 And there we see the arrow of time seemingly emerging from time-invariant Hamiltonian mechanics! Clearly, this should be impossible, a point first made by Loschmidt soon after Boltzmann’s original derivation. But, as we saw earlier, everything hinges on the assumption of molecular chaos (2.22). This was where we broke time-reversal symmetry, ultimately ensuring that entropy increases only in the future. Had we instead decided in (2.21) that the rate of scattering was proportional to f after the collision, again assuming f ∼ f₁ f₂ then we would find that entropy always decreases as we move into the future.

There is much discussion in the literature about the importance of the H-theorem and its relationship to the second law of thermodynamics. Notably, it is not particularly hard to construct states which violate the H-theorem by virtue of their failure to obey the assumption of molecular chaos. Nonetheless, these states still obey a suitable second law of thermodynamics⁴.

The H-theorem is not a strict inequality. For some distributions, the entropy remains unchanged.

changed. From (2.42), we see that these obey f(p⃗′₁)f(p⃗′₂)−f(p⃗₁)f(p⃗₂)

But this is simply the requirement of detailed balance (2.25). And, as we have seen already, this is obeyed by any distribution satisfying the requirement of local equilibrium (2.29).

4This was first pointed out by E. T. Jaynes in the paper “Violation of Boltzmann’s H Theorem in Real Gases”, published in Physical Review A, volume 4, number 2 (1971).

## 2.4 A First Look at Hydrodynamics

Hydrodynamics is what you get if you take thermodynamics and splash it. You know from your first course on Statistical Mechanics that, at the most coarse grained level, the equilibrium properties of any system are governed by the thermodynamics. In the same manner, low energy, long wavelength, excitations of any system are described by hydrodynamics.

More precisely, hydrodynamics describes the dynamics of systems that are in local equilibrium, with parameters that vary slowly in space in time. As we will see, this means that the relevant dynamical variables are, in the simplest cases, • Density ρ(⃗r,t) = mn(⃗r,t)

• Temperature T(⃗r,t)

• Velocity ⃗u(⃗r,t)

Our goal in this section is to understand why these are the relevant variables to describe the system and to derive the equations that govern their dynamics.

2.4.1 Conserved Quantities We’ll start by answering the first question: why are these the variables of interest? The answer is that these are quantities which don’t relax back down to their equilibrium value in an atomic blink of an eye, but instead change on a much slower, domestic time scale. At heart, the reason for they have this property is that they are all associated to conserved quantities. Let’s see why.

Consider a general function A(⃗r,p⃗) over the single particle phase space. Because we live in real space instead of momentum space, the question of how things vary with ⃗r is more immediately interesting. For this reason, we integrate over momentum and define the average of a quantity A(⃗r,p⃗) to be ⟨A(⃗r,t)⟩ = ∫d³p A(⃗r,p⃗)f(⃗r,p⃗;t) / ∫d³p f(⃗r,p⃗;t)

However, we’ve already got a name for the denominator in this expression: it is the number density of particles n(⃗r,t) = ∫d³p f(⃗r,p⃗;t) (2.43)

(As a check of the consistency of our notation, if you plug the local equilibrium distribution (2.29) into this expression, then the n(⃗r,t) on the left-hand-side equals the n(⃗r,t) defined in (2.29)). So the average is ⟨A(⃗r,t)⟩ = ∫d³p A(⃗r,p⃗)f(⃗r,p⃗;t) / n(⃗r,t) (2.44)

It’s worth making a couple of simple remarks. Firstly, this is different from the average that we defined earlier in (2.3) when discussing Liouville evolution. Here we’re integrating only over momenta and the resulting average is a function of space. A related point is that we’re at liberty to take functions which depend only on ⃗r (and not on p⃗) in and out of the ⟨·⟩ brackets. So, for example, ⟨nA⟩ = n⟨A⟩.

We’re interested in how the average of A changes with time. We looked at this kind of question for Liouville evolution earlier in this section and found the answer (2.5). Now we want to ask the same question for the Boltzmann equation. Before we actually write down the answer, you can guess what it will look like: there will be a streaming term and a term due to the collision integral. Moreover, we know from our previous discussion that the term involving the collision integral will vary much faster than the streaming term.

Since we’re ultimately interested in quantities which vary slowly, this motivates looking at functions A which vanish when integrated against the collision integral. We will see shortly that the relevant criterion is ∫d³p A(⃗r,p⃗) (∂f/∂t)_coll = 0 We’d like to find quantities A which have this property for any distribution f. Using our expression for the collision integral (2.23), we want ∫d³p₁d³p₂d³p′₁d³p′₂ ω(p⃗′₁,p⃗′₂|p⃗₁,p⃗₂)A(⃗r,p⃗₁) [f(⃗r,p⃗′₁)f(⃗r,p⃗′₂)−f(⃗r,p⃗₁)f(⃗r,p⃗₂)] = 0 This now looks rather similar to equation (2.38), just with the logf replaced by A. Indeed, we can follow the steps between (2.38) and (2.41), using the symmetry properties of ω, to massage this into the form ∫d³p₁d³p₂d³p′₁d³p′₂ ω(p⃗′₁,p⃗′₂|p⃗₁,p⃗₂) [f(p⃗′₁)f(p⃗′₂)−f(p⃗₁)f(p⃗₂)] × [A(⃗r,p⃗₁)+A(⃗r,p⃗₂)−A(⃗r,p⃗′₁)−A(⃗r,p⃗′₂)] = 0 Now it’s clear that if we want this to vanish for all distributions, then A itself must have the property that it remains unchanged before and after the collision, A(⃗r,p⃗₁)+A(⃗r,p⃗₂) = A(⃗r,p⃗′₁)+A(⃗r,p⃗′₂) (2.45)

Quantities which obey this are sometimes called collisional invariants. Of course, in the simplest situation we already know what they are: momentum (2.18) and energy (2.19) and, not forgetting, the trivial solution A = 1. We’ll turn to each of these in turn shortly. But first let’s derive an expression for the time evolut ion of any quantity obeying (2.45).

Take the Boltzmann equation (2.23), multiply by a collisional invariant A(⃗r,⃗p) and integrate over d³p. Because the collision term vanishes, we have

∫ d³p A(⃗r,⃗p) [ ∂/∂t + (⃗p/m)·∂/∂⃗r + ⃗F·∂/∂⃗p ] f(⃗r,⃗p,t) = 0

where the external force is F = −∇V. We’ll integrate the last term by parts (remembering that the force ⃗F can depend on position but not on momentum). We can’t integrate the middle term by parts since we’re not integrating over space, but nonetheless, we’ll also rewrite it. Finally, since A has no explicit time dependence, we can take it inside the time derivative. We have

∫ d³p A ∂f/∂t + ∫ d³p A (⃗p/m)·∂f/∂⃗r − ∫ d³p (∂A/∂⃗r)·(⃗p/m) f − ∫ d³p (∂A/∂⃗p)·⃗F f = 0

Although this doesn’t really look like an improvement, the advantage of writing it in this way is apparent when we remember our expression for the average (2.44). Using this notation, we can write the evolution of A as

∂⟨nA⟩/∂t + ∂·⟨n⃗vA⟩/∂⃗r − n⟨⃗v·∂A/∂⃗r⟩ − n⟨⃗F·∂A/∂⃗p⟩ = 0 (2.46)

where ⃗v = ⃗p/m. This is our master equation that tells us how any collisional invariant changes. The next step is to look at specific quantities. There are three and we’ll take each in turn.

Density

Our first collisional invariant is the trivial one: A = 1. If we plug this into (2.46) we get the equation for the particle density n(⃗r,t),

∂n/∂t + ∂·(n⃗u)/∂⃗r = 0 (2.47)

where the average velocity ⃗u of the particles is defined by

⃗u(⃗r,t) = ⟨⃗v⟩

Notice that, once again, our notation is consistent with earlier definitions: if we pick the local equilibrium distribution (2.29), the ⃗u(⃗r,t) in (2.29) agrees with that defined above. The result (2.47) is the continuity equation, expressing the conservation of particle number. Notice, however, that this is not a closed expression for the particle density n: we need to know the velocity ⃗u as well.

It’s useful to give a couple of extra, trivial, definitions at this stage. First, although we won’t use this notation, the continuity equation is sometimes written in terms of the current, ⃗J(⃗r,t) = n(⃗r,t)⃗u(⃗r,t). In what follows, we will often replace the particle density with the mass density,

ρ(⃗r,t) = mn(⃗r,t)

Momentum

Our next collisional invariant is the momentum. We substitute A = m⃗v into (2.46) to find

∂(mnu_i)/∂t + ∂⟨mnv_iv_j⟩/∂r_j − ⟨nF_i⟩ = 0 (2.48)

We can play around with the middle term a little. We write

⟨v_iv_j⟩ = ⟨(v_i − u_i)(v_j − u_j)⟩ + u_i⟨v_j⟩ + u_j⟨v_i⟩ − u_iu_j = ⟨(v_i − u_i)(v_j − u_j)⟩ + u_iu_j

We define a new object known as the pressure tensor,

P_ij = P_ji = ρ⟨(v_i − u_i)(v_j − u_j)⟩

This tensor is computing the flux of i-momentum in the j-direction. It’s worth pausing to see why this is related to pressure. Clearly, the exact form of P_ij depends on the distribution of particles. But, we can evaluate the pressure tensor on the equilibrium, Maxwell-Boltzmann distribution (2.28). The calculation boils down to the same one we did in our first Statistical Physics course to compute equipartition: you find

P_ij = nk_BTδ_ij (2.49)

which, by the ideal gas law, is proportional to the pressure of the gas. Using this definition – together with the continuity equation (2.47) – we can write (2.48) as

ρ(∂u_i/∂t + u_j∂u_i/∂r_j) = nF_i − ∂P_ij/∂r_j (2.50)

This is the equation which captures momentum conservation in our system. Indeed, it has a simple interpretation in terms of Newton’s second law. The left-hand-side is the acceleration of an element of fluid. The combination of derivatives is sometimes called the material derivative,

D/Dt ≡ ∂/∂t + u_j∂/∂r_j (2.51)

It captures the rate of change of a quantity as seen by an observer swept along the streamline of the fluid. The right-hand side of (2.50) includes both the external force ⃗F and an additional term involving the internal pressure of the fluid. As we will see later, ultimately viscous terms will also come from here.

Note that, once again, the equation (2.50) does not provide a closed equation for the velocity ⃗u. You now need to know the pressure tensor P_ij which depends on the particular distribution.

Kinetic Energy

Our final collisional invariant is the kinetic energy of the particles. However, rather than take the absolute kinetic energy, it is slightly easier if we work with the relative kinetic energy,

A = m(⃗v − ⃗u)²

If we substitute this into the master equation⁵ (2.46), the term involving the force vanishes (because ⟨v_i − u_i⟩ = 0). However, the term that involves ∂A/∂r_i is not zero because the average velocity ⃗u depends on ⃗r. We have

(1/2) ∂⟨ρ(⃗v − ⃗u)²⟩/∂t + (1/2) ∂⟨ρv_j(⃗v − ⃗u)²⟩/∂r_j − ρ⟨v_j(v_i − u_i)∂u_i/∂r_j⟩ = 0 (2.52)

⁵There is actually a subtlety here. In deriving the master equation (2.46), we assumed that A has no explicit time dependence, but the A defined above does have explicit time dependence through ⃗u(⃗r,t). Nonetheless, you can check that (2.46) still holds, essentially because the extra term that you get is ∼⟨(⃗v−⃗u)·∂⃗u/∂t⟩=⟨⃗v−⃗u⟩·∂⃗u/∂t=0.

– 40 – At this point, we define the temperature, T(⃗r,t) of our non-equilibrium system. To do so, we fall back on the idea of equipartition and write 3 1 k T(⃗r,t) = m⟨(⃗v −⃗u(⃗r,t))2⟩ (2.53)

2 2 This coincides with our familiar definition of temperature for a system in local equilib- rium (2.29), but now extends this to a system that is out of equilibrium. Note that the temperature is a close relative of the pressure tensor, TrP = 3ρk T/m.

We also define a new quantity, the heat flux, q = mρ⟨(v −u ) (⃗v −⃗u)2⟩ (2.54)

i i i (This actually differs by an overall factor of m from the definition of ⃗q that we made in Section 1. This has the advantage of making the formulae we’re about to derive a little cleaner). The utility of both of these definitions becomes apparent if we play around with the middle term in (2.52). We can write 1 1 1 mρ⟨v (⃗v −⃗u)2⟩ = mρ⟨(v −u ) (⃗v −⃗u)2⟩+ mρu ⟨(⃗v −⃗u)2⟩ i i i i 2 2 2 = q + ρu k T i i B Invoking the definition of the pressure tensor (2.49), we can now rewrite (2.52) as (cid:18) (cid:19)

3 ∂ ∂ 3 ∂u (ρk T)+ q + ρu k T +mP = 0 B i i B ij 2∂t ∂r 2 ∂x i i Because P = P , we can replace ∂u /∂r in the last term with the symmetric tensor ij ji j i known as the rate of strain (and I promise this is the last new definition for a while!)

(cid:18) (cid:19)

1 ∂u ∂u i j U = + (2.55)

ij 2 ∂r ∂r j i Finally, with a little help from the continuity equation (2.47), our expression for the conservation of energy becomes (cid:18) (cid:19)

∂ ∂ 2∂q 2m ρ +u k T + + U P = 0 (2.56)

i B ij ij ∂t ∂r 3∂r 3 i i It’s been a bit of a slog, but finally we have three equations describing how the particle density n (2.47), the velocity ⃗u (2.50) and the temperature T (2.56) change with time.

It’s worth stressing that these equations hold for any distribution f . However, the – 41 – set of equations are not closed. The equation for n depends on ⃗u; the equation for ⃗u depends on P and the equation for T (which is related to the trace of P ) depends ij ij on a new quantity ⃗q. And to determine any of these, we need to solve the Boltzmann equation and compute the distribution f . But the Boltzmann equation is hard! How to do this?

2.4.2 Ideal Fluids Westartbysimplyguessingaformofthedistributionfunctionf (⃗r,p⃗;t). Weknowthat the collision term in the Boltzmann equation induces a fast relaxation to equilibrium, so if we’re looking for a slowly varying solution a good guess is to take a distribution for which (∂f /∂t) = 0. But we’ve already met distribution functions that obey this 1 coll condition in (2.29): they are those describing local equilibrium. Therefore, our first guess for the distribution, which we write as f(0), is local equilibrium (cid:18)

(cid:19)3/2 (cid:18)

(cid:19)

f(0)(⃗r,p⃗;t) = n(⃗r,t) exp − [(⃗v −⃗u(⃗r,t)]2 (2.57)

1 2πmk T(⃗r,t) 2k T(⃗r,t)

B B where p⃗ = m⃗v. In general, this distribution is not a solution to the Boltzmann equation since it does not vanish on the streaming terms. Nonetheless, we will take it as our first approximation to the true solution and later see what we’re missing.

The distribution is normalized so that the number density and temperature defined in (2.43) and (2.53) respectively coincide with n(⃗r,t) and T(⃗r,t) in (2.29). But we can also use the distribution to compute P and ⃗q. We have ij P = k n(⃗r,t)T(⃗r,t)δ ≡ P(⃗r,t)δ (2.58)

ij B ij ij and ⃗q = 0. We can substitute these expressions into our three conservation laws. The continuity equation (2.47) remains unchanged. Written in terms for ρ = mn, it reads (cid:18) (cid:19)

∂ ∂ ∂u +u ρ+ρ = 0 (2.59)

∂t ∂r ∂r j i Meanwhile, the equation (2.50) governing the velocity flow becomes the Euler equation describing fluid motion (cid:18) (cid:19)

∂ ∂ 1∂P F +u u + = (2.60)

j i ∂t ∂r ρ∂r m j i and the final equation (2.56) describing the flow of heat reduces to (cid:18) (cid:19)

∂ ∂ 2T ∂u +u T + = 0 (2.61)

∂t ∂r 3 ∂r j i – 42 – These set of equations describe the motion of an ideal fluid. While they are a good starting point for describing many properties of fluid mechanics, there is one thing that they are missing: dissipation. There is no irreversibility sown into these equations, no mechanism for the fluid to return to equilibrium.

We may have anticipated that these equations lack dissipation. Their starting point was the local equilibrium distribution (2.57) and we saw earlier that for such distribu- tions Boltzmann’s H-function does not decrease; the entropy does not increase. In fact, we can also show this statement directly from the equations above. We can combine (2.59) and (2.60) to find (cid:18) (cid:19)

∂ ∂ +u (ρT−3/2) = 0 ∂t ∂r which tells us that the quantity ρT−3/2 is constant along streamlines. But this is the requirement that motion along streamlines is adiabatic, not increasing the entropy. To see that this is the case, you need to go back to your earlier statistical mechanics or thermodynamics course6. The usual statement is that for an ideal gas, an adiabatic t Transformation leaves VT3/2 constant. Here we’re working with the density ρ = mN/V and this becomes ρT−3/2 is constant. Note, however, that in the present context ρ and T are not numbers, but functions of space and time: we are now talking about a local adiabatic change.

Sound Waves It is also simple to show explicitly that one can set up motion in the ideal fluid that doesn’t relax back down to equilibrium. We start with a fluid at rest, setting ⃗u = 0 and ρ = ρ¯ and T = T, with both ρ¯ and T constant. We now splash it (gently). That means that we perturb the system and linearise the resulting equations. We’ll analyse these perturbations in Fourier modes and write ρ(⃗r,t) = ρ¯+δρe−i(ωt−⃗k·⃗r)

and T(⃗r,t) = T +δT e−i(ωt−⃗k·⃗r) (2.62)

Furthermore, we’ll look for a particular kind of perturbation in which the fluid motion is parallel to the perturbation. In other words, we’re looking for a longitudinal wave ⃗u(⃗r,t) = ˆ δue−i(ωt−⃗k·⃗r) (2.63)

The linearised versions of (2.59), (2.60) and (2.61) then read δρ = ρ¯δu |k| 6See, for example, the discussion of the Carnot cycle in the lectures on Statistical Physics.

ω k T k B B δu = δρ+ δT | ⃗ k| mρ¯ m ω 2 δT = Tδu | ⃗ k| 3 There is one solution to these equations with zero frequency, ω = 0. These have δu = 0 while δρ = −ρ¯ and δT = T. (Note that this notation hides a small ϵ. It really means that δρ = −ϵρ¯ and δT = ϵT. Because the equations are linear and homogeneous, you can take any ϵ you like but, since we’re looking at small perturbations, it should be small). This solution has the property that P = mnk T is constant. But since, in the absence of an external force, pressure is the only driving term in (2.60), the fluid remains at rest, which is why δu = 0 for this solution.

Two further solutions to these equations both have δρ = ρ¯, δT = 2T ¯ and δu = ω/| ⃗ k| with the dispersion relation ω = ±v |k| with v = (2.64)

s s These are sound waves, the propagating version of the adiabatic change that we saw above: the combination ρT−3/2 is left unchanged by the compression and expansion of the fluid. The quantity v is the speed of sound.

## 2.5 Transport with Collisions

While it’s nice to have derived some simple equations describing fluid mechanics, as we’ve seen they’re missing dissipation. And, since the purported goal of these lectures is to understand how systems relax back to equilibrium, we should try to see what we’ve missed.

In fact, it’s clear what we’ve missed. Our first guess for the distribution function was local equilibrium f(0)(⃗r,p⃗;t) = n(⃗r,t) exp − [(⃗v −⃗u(⃗r,t)]2 (2.65)

1 2πmk T(⃗r,t) 2k T(⃗r,t)

B B We chose this on the grounds that it gives a vanishing contribution to the collision integral. But we never checked whether it actually solves the streaming terms in the Boltzmann equation. And, as we will now show, it doesn’t.

Using the definition of the Poisson bracket and the one-particle Hamiltonian H (2.11), we have ∂f(0) ∂f(0) ∂f(0) ∂f(0)

1 −{H ,f(0)} = 1 +F ⃗ · 1 +⃗v · 1 ∂t 1 1 ∂t ∂p⃗ ∂⃗r Now the dependence on p⃗ = m⃗v in local equilibrium is easy: it is simply ∂f(0) 1 1 = − (⃗v −⃗u)f(0)

∂p⃗ k T 1 Meanwhile all⃗r dependence and t dependence of f(0) lies in the functions n(⃗r,t), T(⃗r,t) and ⃗u(⃗r,t). From (2.65) we have ∂f(0) f(0)

1 = 1 ∂n n ∂f(0) 3f(0) m 1 = − 1 + (⃗v −⃗u)2f(0)

∂T 2 T 2k T2 1 ∂f(0) m 1 = (⃗v −⃗u)f(0)

∂⃗u k T 1 Using all these relations, we have ∂f(0) (cid:20) 1 (cid:18) m(⃗v −⃗u)2 3 (cid:19)

1 −{H ,f(0)} = D ˜ n+ − D ˜ T ∂t 1 1 n t 2k T2 2T t (cid:21)

m 1 + (⃗v −⃗u)·D ˜ ⃗u− F ⃗ ·(⃗v −⃗u) f(0) (2.66)

k T t k T 1 B B where we’ve introduced the notation D which differs from the material derivative D in that it depends on the velocity ⃗v rather than the average velocity ⃗u, t t ∂ ∂ ∂ D ≡ +⃗v · = D +(⃗v −⃗u)· t t ∂t ∂⃗r ∂⃗r Now our first attempt at deriving hydrodynamics gave us three equations describing how n (2.59), ⃗u (2.60) and T (2.61) change with time. We substitute these into (2.66). You’ll need a couple of lines of algebra, cancelling some terms, using the relationship P = nk T and the definition of U in (2.55), but it’s not hard to show that we ultimately get ∂f(0) (cid:20) 1 (cid:18) m 5 (cid:19)

1 −{H ,f(0)} = (⃗v −⃗u)2 − (⃗v −⃗u)·∇T (2.67)

∂t 1 1 T 2k T 2 (cid:18) (cid:19) (cid:21)

m 1 + (v −u )(v −u )− (⃗v −⃗u)2δ U f(0)

k T i i j j 3 ij ij 1 And there’s no reason that the right-hand-side is zero. So, unsurprisingly, f(0) does not solve the Boltzmann equation. However, the remaining term depends on ∇T and ∂⃗u/∂⃗r which means that we if we stick to long wavelength variations in the temperature and velocity then we almost have a solution. We need only add a little extra something to the distribution f = f(0) +δf (2.68)

1 1 1 Let’s see how this changes things.

2.5.1 Relaxation Time Approximation The correction term, δf , will contribute to the collision integral (2.24). Dropping the ⃗r argument for clarity, we have ∂f ∂t = ∫ d³p d³p′ d³p′ ω(p⃗′, p⃗′ | p⃗, p⃗) [f(p⃗′)f(p⃗′) − f(p⃗)f(p⃗)]

2 1 2 1 2 1 2 1 1 1 2 1 1 1 2 coll = ∫ d³p d³p′ d³p′ ω(p⃗′, p⃗′ | p⃗, p⃗) [f⁽⁰⁾(p⃗′)δf(p⃗′) + δf(p⃗′)f⁽⁰⁾(p⃗′)

2 1 2 1 2 1 2 1 1 1 2 1 1 2 − f⁽⁰⁾(p⃗)δf(p⃗) − δf(p⃗)f⁽⁰⁾(p⃗)]

1 1 1 2 1 1 2 where, in the second line, we have used the fact that f⁽⁰⁾ vanishes in the collision integral and ignored quadratic terms ∼ δf². The resulting collision integral is a linear function of δf. But it’s still kind of a mess and not easy to play with.

At this point, there is a proper way to proceed. This involves first taking more care in the expansion of δf (using what is known as the Chapman-Enskog expansion) and then treating the linear operator above correctly. However, there is a much easier way to make progress: we just replace the collision integral with another, much simpler function, that captures much of the relevant physics. We take ∂f₁/∂t |coll = −δf₁/τ (2.69)

where τ is the relaxation time which, as we’ve already seen, governs the rate of change of f. In general, τ could be momentum dependent. Here we’ll simply take it to be a constant.

The choice of operator (2.69) is called the relaxation time approximation. (Sometimes it is referred to as the Bhatnagar-Gross-Krook operator). It’s most certainly not exact. In fact, it’s a rather cheap approximation. But it will give us a good intuition for what’s going on. With this replacement, the Boltzmann equation becomes ∂(f⁽⁰⁾ + δf₁)/∂t − {H₁, f⁽⁰⁾ + δf₁} = −δf₁/τ But, since δf₁ ≪ f⁽⁰⁾, we can ignore δf₁ on the left-hand-side. Then, using (2.67), we have a simple expression for the extra contribution to the distribution function δf₁ = −τ [ (⃗v − ⃗u) · (m/2kT ∂T/∂⃗r) + (m/kT (v_i − u_i)(v_j − u_j) − 1/3 (⃗v − ⃗u)² δ_{ij}) ∂u_i/∂r_j ] f⁽⁰⁾ (2.70)

We can now use this small correction to the distribution to revisit some of the transport properties that we saw in Section 1.

2.5.2 Thermal Conductivity Revisited Let’s start by computing the heat flux q_i = mρ⟨(v_i − u_i) (⃗v − ⃗u)²⟩ (2.71)

using the corrected distribution (2.68). We’ve already seen that the local equilibrium distribution f⁽⁰⁾ gave ⃗q = 0, so the only contribution comes from δf₁. Moreover, only the first term in (2.70) contributes to (2.71). (The other is an odd function and vanishes when we do the integral). We have ⃗q = −κ∇T This is the same phenomenological law that we met in (1.12). The coefficient κ is the thermal conductivity and is given by κ = ∫ d³p (mτρ/2T) (⃗v − ⃗u)² (⃗v − ⃗u)² (m/2kT (⃗v − ⃗u)² − 5/2) f⁽⁰⁾ = (mτρ/6T) [⟨v⁶⟩₀ − (5m/2kT) ⟨v⁴⟩₀]

In the second line, we’ve replaced all (v − u) factors with v by performing a (⃗r-dependent) shift of the integration variable. The subscript ⟨·⟩ means that these averages are to be taken in the local Maxwell-Boltzmann distribution f⁽⁰⁾ with u = 0. These integrals are simple to perform. We have ⟨v⁴⟩₀ = 15k_B²T²/m² and ⟨v⁶⟩₀ = 105k_B³T³/m³, giving κ = τnk_B²T The factor of 5/2 here has followed us throughout the calculation. The reason for its presence is that its the specific heat at constant pressure, c_p = 5k_B/2.

This result is parameterically the same that we found earlier in (1.13). (Although you have to be a little careful to check this because, as we mentioned after (2.54), the definition of heat flux differs and, correspondingly, κ, differs by a factor of m. Moreover, the current formula is written in terms of slightly different variables. To make the comparison, you should rewrite the scattering time as τ ∼ 1/(mσn⟨v²⟩), where σ is the total cross-section and ⟨v²⟩ ∼ T/m by equipartition). The coefficient differs from our earlier derivation, but it’s not really to be trusted here, not least because the only definition of τ that we have is in the implementation of the relaxation time approximation.

We can also see how the equation (2.56) governing the flow of temperature is related to the more simplistic heat flow equation that we introduced in (1.14). For this we need to assume both a static fluid ⃗u = 0 and also that we can neglect changes in the thermal conductivity, ∂κ/∂⃗r ≈ 0. Then equation (2.56) reduces to the heat equation ρk_B ∂T/∂t = −κ∇²T 2.5.3 Viscosity Revisited Let’s now look at the shear viscosity. From our discussion in Section 1, we know that the relevant experimental set-up is a fluid with a velocity gradient, ∂u_x/∂z ≠ 0. The shear viscosity is associated to the flux of x-momentum in the z-direction. But this is precisely what is computed by the off-diagonal component of the pressure tensor, P_{xz} = ρ⟨(v_x − u_x)(v_z − u_z)⟩ We’ve already seen that the local equilibrium distribution gives a diagonal pressure tensor (2.58), corresponding to vanishing viscosity. What happens if we use the corrected distribution (2.68)? Now only the second term in (2.70) contributes (since the first term is an odd function of (v − u)). We writ P = P δ +Π (2.72)

ij ij ij

where the extra term Π is called the stress tensor and is given by ij ∫ ( )

mτρ 1 Π = U d3p (v −u )(v −u )(v −u )(v −u )− (⃗v −⃗u)2δ f(0)

ij k T kl j j i i k l k l 3 kl 1 [ ]

mτρ 1 = U ⟨v v v v ⟩ − δ ⟨v v v2⟩ kl i j k l 0 kl i j 0 k T 3

Before we compute Π , note that it is a traceless tensor. This is because the first ij term η|k|² ω = −i ρ̄ Once again, we see that these modes behave diffusively.

Navier Stokes Equation and Liquids Our derivation of the Navier-Stokes equation relied on the dilute gas approximation. However, the equation is more general than that. Indeed, it can be thought of as the most general expression in a derivative expansion for momentum transport (subject to various requirements). In fact, there is one extra parameter that we could include: ρ ∂/∂t (⃗u) + ρ⃗u·∇⃗u = −∇P + η∇²⃗u + (ζ + η/3) ∇(∇·⃗u)

where ζ is the bulk viscosity which vanished in our derivation above. Although the equation above governs transport in liquids, we should stress that first-principles computations of the viscosity (and also thermal conductivity) that we saw previously only hold in the dilute gas approximation.

## 3. Stochastic Processes

We learn in kindergarten about the phenomenon of Brownian motion, the random jittery movement that a particle suffers when it is placed in a liquid. Famously, it is caused by the constant bombardment due to molecules in the surrounding the liquid. Our goal in this section is to introduce the mathematical formalism that allows us to model such random behaviour.

## 3.1 The Langevin Equation

In contrast to the previous section, we will here focus on just a single particle. However, this particle will be sitting in a background medium. If we know the force F acting on the particle, its motion is entirely deterministic, governed by m⃗ẍ = −γ⃗ẋ + F (3.1)

In contrast to the previous section, this is not a Hamiltonian system. This is because we have included a friction term with a coefficient γ. This arises due to the viscosity, η, of the surrounding liquid that we met in the previous section. If we model the particle as a sphere of radius a then there is a formula due to Stokes which says γ = 6πηa. However, in what follows we shall simply treat γ as a fixed parameter. In the presence of a time independent force, the steady-state solution with ⃗ẍ = 0 is ⃗ẋ = F/γ For this reason, the quantity 1/γ is sometimes referred to as the mobility.

Returning to (3.1), for any specified force F, the path of the particle is fully determined. This is seemingly at odds with the random behaviour observed in Brownian motion. The way in which we reconcile these two points is, hopefully, obvious: in Brownian motion the force F that the particle feels is itself random. In fact, we will split the force into two pieces, F = −∇V + f(t)

Here V is a fixed background potential in which the particle is moving. Perhaps V arises because the particle is moving in gravity; perhaps because it is attached to a spring. But, either way, there is nothing random about V. In contrast, f(t) is the random force that the particle experiences due to all the other atoms in the liquid. It is sometimes referred to as noise. The resulting equation is called the Langevin equation m⃗ẍ = −γ⃗ẋ − ∇V + f(t) (3.2)

Although it looks just like an ordinary differential equation, it is, in fact, a different beast known as a stochastic differential equation. The reason that it’s different is that we don’t actually know what f(t) is. Yet, somehow, we must solve this equation anyway!

Let’s clarify what is meant by this. Suppose that you did know the microscopic force f(t) that is experienced by a given particle. Then you could, in principle, go ahead and solve the Langevin equation (3.2). But the next particle that you look at will experience a different force f(t) so you’ll have to solve (3.2) again. And for the third particle, you’ll have to solve it yet again. Clearly, this is going to become tedious. What’s more, it’s unrealistic to think that we will actually know f(t) in any specific case. Instead, we admit that we only know certain crude features of the force f(t) such as, for example, its average value. Then we might hope that this is sufficient information to figure out, say, the average value of ⃗x(t). That is the goal when solving the Langevin equation.

3.1.1 Diffusion in a Very Viscous Fluid We start by solving the Langevin equation in the case of vanishing potential, V = 0. (For an arbitrary potential, the Langevin equation is an unpleasant non-linear stochastic differential equation and is beyond our ambition in this course. However, we will discuss some properties of the case with potential in the following section when we introduce the Fokker-Planck equation). We can simplify the problem even further by considering Brownian motion in a very viscous liquid. In this case, motion is entirely dominated by the friction term in the Langevin equation and we ignore the inertial term, which is tantamount to setting m = 0.

When m = 0, we’re left with a first order equation, ⃗ẋ(t) = f(t)/γ For any f(t), this can be trivially integrated to give ⃗x(t) = ⃗x(0) + (1/γ) ∫₀ᵗ dt′ f(t′) (3.3)

At this point, we can’t go any further until we specify some of the properties of the noise f(t). Our fir First assumption is that, on average, the noise vanishes at any given time. We will denote averages by ⟨·⟩, so this assumption reads ⟨f(t)⟩ = 0 (3.4)

Taking the average of (3.3) then gives us the result: ⟨⃗x(t)⟩ = ⃗x(0)

This is deeply unsurprising: if the average noise vanishes, the average position of the particle is simply where we left it to begin with. Nonetheless, it’s worth stressing that this doesn’t mean that all particles sit where you leave them. It means that if you drop many identical particles at the origin, ⃗x(0) =⃗0, then they will all move but their average position — or their centre of mass — will remain at the origin.

We can get more information by looking at the variance of the position, ⟨(⃗x(t)−⃗x(0))2⟩ This will tell us the average spread of the particles. We can derive an expression for the variance by first squaring (3.3) and then taking the average, ⟨(⃗x(t)−⃗x(0))2⟩ = 1/γ2 ∫_0^t dt′ ∫_0^t dt′ ⟨⃗f(t′)·⃗f(t′)⟩ (3.5)

In order to compute this, we need to specify more information about the noise, namely its correlation function ⟨f_i(t_1)f_j(t_2)⟩ where we have resorted to index notation, i,j = 1,2,3 to denote the direction of the force. This is specifying how likely it is that the particle will receive a given kick f_j at time t_2 given that it received a kick f_i at time t_1.

In many cases of interest, including that of Brownian motion, the kicks imparted by the noise are both fast and uncorrelated. Let me explain what this means. Suppose that a given collision between our particle and an atom takes time τ_coll. Then if we focus on time scales less than τ_coll then there will clearly be a correlation between the forces imparted on our particle because these forces are due to the same process that’s already taking place. (If an atom is coming in from the left, then it’s still coming in from the left at a time t ≪ τ_coll later). However if we look on time scales t ≫ τ_coll, the force will be due to a different collision with a different atom. The statement that the noise is uncorrelated means that the force imparted by later collisions knows nothing about earlier collisions. Mathematically, this means ⟨f_i(t_1)f_j(t_2)⟩ = 0 when t_2−t_1 ≫ τ_coll The statement that the collisions are fast means that we only care about time scales t_2 − t_1 ≫ τ_coll and so can effectively take the limit τ_coll → 0. However, that doesn’t quite mean that we can just ignore this correlation function. Instead, when we take the limit τ_coll → 0, we’re left with a delta-function contribution, ⟨f_i(t_1)f_j(t_2)⟩ = 2Dγ^2 δ_ij δ(t_2−t_1) (3.6)

Here the factor of γ^2 has been put in for convenience. We will shortly see the interpretation of the coefficient D, which governs the strength of the correlations. Noise which obeys (3.4) and (3.6) is often referred to as white noise. It is valid whenever the environment relaxes back down to equilibrium much faster than the system of interest. This guarantees that, although the system is still reeling from the previous kick, the environment remembers nothing of what went before and kicks again, as fresh and random as the first time.

Using this expression for white noise, the variance (3.5) in the position of the particles is ⟨(⃗x(t)−⃗x(0))2⟩ = 6Dt (3.7)

This is an important result: the root-mean square of the distance increases as √t with time. This is characteristic behaviour of diffusion. The coefficient D is called the diffusion constant. (We put the factor of γ^2 in the correlation function (3.6) so that this equation would come out nicely).

3.1.2 Diffusion in a Less Viscous Liquid Let’s now return to the Langevin equation (3.2) and repeat our analysis, this time retaining the inertia term, so m ≠ 0. We will still set V = 0.

As before, computing average quantities — this time both velocity ⟨⃗x˙(t)⟩ and position ⟨⃗x(t)⟩ is straightforward and relatively uninteresting. For a given f(t), it is not difficult to solve (3.2). After multiplying by an integrating factor e^{γt/m}, the equation becomes d/dt (⃗x˙ e^{γt/m}) = (1/m) ⃗f(t) e^{γt/m} which can be happily integrated to give ⃗x˙(t) = ⃗x˙(0)e^{−γt/m} + 1/m ∫_0^t dt′ ⃗f(t′) e^{γ(t′−t)/m} (3.8)

We now use the fact that the average of noise vanishes (3.4) to find that the average velocity is simply that of a damped particle in the absence of any noise, ⟨⃗x˙(t)⟩ = ⃗x˙(0)e^{−γt/m} Similarly, to determine the average position we have ⃗x(t) = ⃗x(0) + ∫_0^t dt′ ⃗x˙(t′) (3.9)

From which we get ⟨⃗x(t)⟩ = ⃗x(0) + ∫_0^t dt′ ⟨⃗x˙(t′)⟩ = ⃗x(0) + ⃗x˙(0) (1−e^{−γt/m})

Again, this is unsurprising: when the average noise vanishes, the average position of the particle coincides with that of a particle that didn’t experience any noise.

Things get more interesting when we look at the expectation values of quadratic quantities. This includes the variance in position ⟨⃗x(t)·⃗x(t)⟩ and velocity ⟨⃗x˙(t)·⃗x˙(t)⟩, but also more general correlation functions in which the The two quantities are evaluated at different times. For example, the correlation function ⟨x˙_i(t_1)x˙_j(t_2)⟩ tells us information about the velocity of the particle at time t_2 given that we know its velocity at time t_1. From (3.8), we have the expression, ⟨x˙_i(t_1)x˙_j(t_2)⟩ = ⟨x˙_i(t_1)⟩⟨x˙_j(t_2)⟩ + (1/m^2) ∫_0^{t_1} dt'_1 ∫_0^{t_2} dt'_2 ⟨f_i(t'_1)f_j(t'_2)⟩ e^{γ(t'_1 + t'_2 - t_1 - t_2)/m} where we made use of the fact that ⟨f(t)⟩ = 0 to drop the terms linear in the noise f. If we use the white noise correlation function (3.6), and assume t_2 ≥ t_1 > 0, the integral in the second term becomes, ⟨x˙_i(t_1)x˙_j(t_2)⟩ = ⟨x˙_i(t_1)⟩⟨x˙_j(t_2)⟩ + (2Dγ^2 / m^2) δ_{ij} ∫_0^{t_1} dt'_1 e^{-γ(t_1 + t_2)/m} e^{2γt'_1/m} = ⟨x˙_i(t_1)⟩⟨x˙_j(t_2)⟩ + (Dγ / m) δ_{ij} (e^{-γ(t_2 - t_1)/m} - e^{-γ(t_1 + t_2)/m})

For very large times, t_1, t_2 → ∞, we can drop the last term as well as the average velocities since ⟨⃗x(t)⟩ → 0. We learn that the correlation between velocities decays exponentially as ⟨x˙_i(t_1)x˙_j(t_2)⟩ → (Dγ / m) δ_{ij} e^{-γ(t_2 - t_1)/m} This means that if you know the velocity of the particle at some time t_1, then you can be fairly confident that it will have a similar velocity at a time t_2 < t_1 + m/γ later. But if you wait longer than time m/γ then you would be a fool to make any bets on the velocity based only on your knowledge at time t_1.

Finally, we can also use this result to compute the average velocity-squared (which, of course, is the kinetic energy of the system). At late times, any initial velocity has died away and the resulting kinetic energy is due entirely to the bombardment by the environment. It is independent of time and given by ⟨⃗x˙(t)·⃗x˙(t)⟩ = 3Dγ / m (3.10)

One can compute similar correlation functions for position ⟨x_i(t_1)x_j(t_2)⟩. The expressions are a little more tricky but still quite manageable. (Combining equations (3.9) and (3.8), you can see that you will have a quadruple integral to perform and figuring out the limits is a little fiddly). At late times, it turns out that the variance of the position is given by the same expression that we saw for the viscous liquid (3.7), ⟨(⃗x(t) - ⃗x(0))^2⟩ = 6Dt (3.11)

again exhibiting the now-familiar t behaviour for the root-mean-square distance.

3.1.3 The Einstein Relation We brushed over something important and lovely in the previous discussion. We computed the average kinetic energy of a particle in (3.10). It is E = (1/2) m ⟨⃗x˙·⃗x˙⟩ = (3/2) Dγ But we already know what the average energy of a particle is when it’s bombarded by its environment: it is given by the equipartition theorem and, crucially, depends only on the temperature of the surroundings E = k_B T It must be therefore that the diffusion constant D is related to the mobility 1/γ by D = k_B T / γ (3.12)

That’s rather surprising! The diffusion constant captures the amount a particle is kicked around due to the background medium; the mobility expresses how hard it is for a particle to plough through the background medium. And yet they are related. This equation is telling us that diffusion and viscosity both have their microscopic origin in the random bombardment of molecules. Notice that D is inversely proportional to γ. Yet you might have thought that the amount the particle is kicked increases as the viscosity increases. Indeed, looking back at (3.6), you can see that the amount the particle is kicked is actually proportional to Dγ^2 ∼ Tγ. Which is more in line with our intuition.

Equation (3.12) is known as the Einstein relation. It is an important example of the fluctuation-dissipation theorem. The fluctuations of the particle as it undergoes its random walk are related to the drag force (or dissipation of momentum) that the particle feels as it moves through the fluid.

The Einstein relation gives an excellent way to determine Boltzmann’s constant experimentally. Watch a particle perform a Brownian jitter. After time t, the distance travelled by the particle (3.7) should be ⟨⃗x^2⟩ = (k_B T / (πηa)) t where we have used the Stokes formula γ = 6πηa to relate the mobility to the viscosity η and radius a of the particle. This experiment was done in 1909 by the French physicist Jean Baptiste Perrin and won him the 1926 Nobel prize.

3.1.4 Noise Probability Distributions So far, we’ve only needed to use the two pieces of information about the noise, namely, ⟨f(t)⟩ = 0 (3.13)

⟨f_i(t_1)f_j(t_2)⟩ = 2Dγ^2 δ_{ij} δ(t_1 - t_2) (3.14)

However, if we wanted to compute correlation functions involving more than two velocities or positions, it should be clear from the calculation that we would need to know higher moments of the probability distribution for f(t). In fact, the definition of white noise is that there are no non-trivial correlations other than ⟨f_i(t_1)f_j(t_2)⟩. This doesn’t mean that the higher correlation functions are vanishing, just that they can be reduced to the two-time correlators. This means that for N even, ⟨f_{i_1}(t_1)...f_{i_N}(t_N)⟩ = ⟨f_{i_1}(t_1)f_{i_2}(t_2)⟩...⟨f_{i_{N-1}}(t_{N-1})f_{i_N}(t_N)⟩ + permutations while, for N odd, ⟨f_{i1}(t1)...f_{iN}(tN)⟩ = 0. Another way of saying this is that all but the second cumulant of the probability distribution vanish.

Instead of specifying all these moments of the distribution, it is often much more useful to specify the probability distribution for f(t) directly. However, this is a slightly subtle object because we want to specify the probability for an entire function f(t), rather than a single random variable. This means that the probability distribution must be a functional: you give it a function f(t) and it spits back a number which, in this case, should be between zero and one.

The good news is that, among the class of probability distributions over functions, the white noise distribution is by far the easiest! If we were dealing with a single random variable, the distribution that has only two-point correlators but no higher is the Gaussian. And, suitably generalised, this also works for our functional probability distribution. The probability distribution that gives white noise is Prob[f(t)] = N exp(−∫_{-∞}^{+∞} dt f⃗(t)·f⃗(t) / 4Dγ²)

where N is a normalization factor which is needed to ensure that the sum over all probabilities gives unity. This “sum” is really a sum over all functions f(t) or, in other words, a functional integral. The normalization condition which fixes N is then ∫ Df(t) Prob[f(t)] = 1 (3.15)

With this probability distribution, all averaging over the noise can now be computed as a functional integral. If you have any function g(x), then its average is ⟨g(x)⟩ = N ∫ Df(t) g(x) e^{−∫ dt f⃗²/4Dγ²} where the notation x means the solution to the Langevin equation in the presence of a fixed source f.

Let’s now show that the Gaussian probability distribution indeed reproduces the white noise correlations as claimed. To do this, we first introduce an object Z[J(t)] known as a generating function. We can introduce a generating function for any probability distribution, so let’s keep things general for now and later specialise to the Gaussian distribution.

Z[J(t)] = ∫ Df(t) Prob[f(t)] exp(∫_{-∞}^{+∞} dt J⃗(t)·f⃗(t))

This generating function is a functional: it is a function of any function J(t) that we care to feed it. By construction, Z[0] = 1, courtesy of (3.15).

As the notation Z suggests, the generating function has much in common with the partition function that we work with in a first course of Statistical Mechanics. This is most apparent in the context of statistical field theories where the generating function is reminiscent of the partition function. Both are functional, or path, integrals. These objects are also important in quantum field theory where the names partition function and generating function are often used synonymously.

The function J that we have introduced is, in this context, really little more than a trick that allows us to encode all the correlation functions in Z[J]. To see how this works. Suppose that we differentiate Z with respect to J evaluated at some time t = t_i and then set J = 0. We have δZ/δJ_i(t_i)|_{J⃗=0} = ∫ Df(t) f_i(t_i) Prob[f(t)] = ⟨f_i(t_i)⟩ Playing the same game, first taking n derivatives, gives δⁿZ/(δJ_{i1}(t_{i1})...δJ_{in}(t_{in}))|_{J⃗=0} = ∫ Df(t) f_{i1}(t_{i1})...f_{in}(t_{in}) Prob[f(t)] = ⟨f_{i1}(t_{i1})...f_{in}(t_{in})⟩ So we see that if we can compute Z[J], then successive correlation functions are simply the coefficients of a Taylor expansion in J. This is particularly useful for the Gaussian distribution where the generating function is, Z[J⃗(t)] = N ∫ Df(t) exp(−∫_{-∞}^{+∞} dt [f⃗(t)·f⃗(t)/4Dγ² − J⃗(t)·f⃗(t)])

But this is nothing more than a Gaussian integral. (Ok, it’s an infinite number of Gaussian integrals because it’s a functional integral. But we shouldn’t let that phase us). We can easily compute it by completing the square Z[J⃗(t)] = N ∫ Df(t) exp(−1/(4Dγ²) ∫_{-∞}^{+∞} dt [f⃗(t) − 2Dγ²J⃗(t)]² − 4D²γ⁴ J⃗(t)·J⃗(t))

After the shift of variable, f⃗ → f⃗ − 2Dγ²J⃗, the integral reduces to (3.15), leaving behind Z[J⃗(t)] = exp(Dγ² ∫_{-∞}^{+∞} dt J⃗(t)·J⃗(t))

Now it is an easy matter to compute correlation functions. Taking one derivative, we have δZ/δJ_i(t_i) = 2Dγ² J_i(t_i) Z[J⃗]

But this vanishes when we set J = 0, in agreement with our requirement (3.13) that the average noise vanishes. Taking a second derivative gives, δ²Z/(δJ_i(t_i) δJ_j(t_j)) = 2Dγ² δ_{ij} δ(t_i − t_j) Z[J⃗] + 4D²γ⁴ J_i(t_i) J_j(t_j) Z[J⃗]

Now setting J = 0, only the first term survives and reproduces the meaning that Langevin-type equations are not restricted to particle positions. It is also of interest to write down stochastic processes for fields. For example, we may want to consider a time dependent process for some order parameter m(⃗r,t), influenced by noise ∂m/∂t = c∇²m − am − 2bm² + f where f(⃗r,t) is a random field with correlations ⟨f⟩ = 0 and ⟨f(⃗r₁,t₁)f(⃗r₂,t₂)⟩ ∼ δᵈ(⃗r₁ −⃗r₂)δ(t₁ − t₂)

A famous example of a stochastic process is provided by the fluctuating boundary between, say, a gas and a liquid. Denoting the height of the boundary as h(⃗r,t), the simplest description of the boundary fluctuations is given by the Edwards-Wilkinson equation, ∂h/∂t = ∇²h + f

A somewhat more accurate model is given by the Kardar-Parisi-Zhang equation, ∂h/∂t = ∇²h + λ(∇h)² + f

We won’t have anything to say about the properties of these equations in this course. An introduction can be found in the second book by Kardar.

## 3.2 The Fokker-Planck Equation

Drop a particle at some position, say ⃗x₀ at time t₀. If the subsequent evolution is noisy, so that it is governed by a stochastic Langevin equation, then we’ve got no way to know for sure where the particle will be. The best that we can do is talk about probabilities. We will denote the probability that the particle sits at ⃗x at time t as P(⃗x,t;⃗x₀,t₀).

In the previous section we expressed our uncertainty in the position of the particle in terms of correlation functions. Here we shift perspective a little. We would like to ask: what probability distribution P(⃗x,t;⃗x₀,t₀) would give rise to the same correlation functions that arose from the Langevin equation?

We should stress that we care nothing about the particular path ⃗x(t) that the particle took. The probability distribution over paths would be a rather complicated functional (rather like those we saw in Section 3.1.4). Instead we will ask the much simpler question of the probability that the particle sits at ⃗x at time t, regardless of how it got there.

It is simple to write down a formal expression for the probability distribution. Let’s denote the solution to the Langevin equation for a given noise function f as ⃗x_f. Of course, if we know the noise, then there is no uncertainty in the probability distribution for ⃗x. It is simply P(⃗x,t) = δ(⃗x − ⃗x_f). Now averaging over all possible noise, we can write the probability distribution as P(⃗x,t) = ⟨δ(⃗x − ⃗x_f)⟩ (3.16)

In this section, we shall show that the P(⃗x,t) obeys a simple partial differential equation known as the Fokker-Planck equation.

3.2.1 The Diffusion Equation

The simplest stochastic process we studied was a particle subject to random forces in a very viscous fluid. The Langevin equation is d⃗x(t)/dt = f(t)

In Section 3.1.1 we showed that the average position of the particle remains unchanged: if ⃗x(t = 0) = ⃗0 then ⟨⃗x(t)⟩ = ⃗0 for all t. But the variance of the particle undergoes a random walk (3.7), ⟨⃗x(t)²⟩ = 6Dt (3.17)

For this simple case, we won’t derive the probability distribution: we’ll just write it down. The probability distribution that reproduces this variance: it is just a Gaussian P(⃗x,t) = (4πDt)⁻³/² exp(−⃗x²/4Dt) (3.18)

where the factor out front is determined by the normalization requirement that ∫ d³x P(x,t) = 1 for all time t. Note that there is more information contained in this probability distribution than just the variance (3.17). Specifically, all higher cumulants vanish. (This means, for example, that ⟨⃗x³⟩ = 0 and ⟨⃗x⁴⟩ = 3⟨⃗x²⟩ and so on). But it is simple to check that this is indeed what arises from the Langevin equation with white noise described in Section 3.1.4.

The probability distribution (3.18) obeys the diffusion equation, ∂P/∂t = D∇²P

This is the simplest example of a Fokker-Planck equation. However, for more complicated versions of the Langevin equation, we will have to work harder to derive the analogous equation governing the probability distribution P.

3.2.2 Meet the Fokker-Planck Equation

Let’s now consider the more general stochastic process. We’ll still work in the viscous limit for now, setting m = 0 so that we have a first order Langevin equation, γ d⃗x/dt = −∇V + f (3.19)

A quadratic V corresponds to a harmonic oscillator potential and the Langevin equation is not difficult to solve. (In fact, mathematically it is the same problem that we solved in Section 3.1.2. You just have to replace ⃗x = ⃗v → ⃗x). Any other V gives rise to a non-linear stochastic equation (confusingly sometimes called “quasi-linear” in this context) and no general solution is available. Nonetheless, we will still be able to massage this into the form of a Fokker-Planck equation.

We begin by extracting some information from the Langevin equation. Consider a particle sitting at some point x at time t. If we look again a short time δt later, the particle will have moved a small amount δ⃗x = ⃗x(t + δt) − ⃗x(t) = (1/γ) ∫ₜᵗ⁺ᵟᵗ dt′ [−∇V + f(t′)] (3.20)

Here we’ve taken the average value of the noise function, f, over the small time interval.

However, we've assumed that the displacement of the particle δx is small enough so that we can evaluate the force ∇V at the original position x. (It turns out that this is ok in the present context but there are often pitfalls in making such assumptions in the theory of stochastic processes. We'll comment on one such pitfall at the end of this Section). We can now compute the average. Because ⟨f(t)⟩ = 0, we have ⟨δx⟩ = − ∇V δt (3.21)

The computation ⟨δx δx⟩ is also straightforward, i j γ²⟨δx δx⟩ = ⟨∂ V∂ V⟩δt² −δt dt′⟨∂ V f (t′)+∂ Vf (t′)⟩ i j i j i j j i + dt′ dt′′⟨f (t′)f (t′′)⟩ i j Both the first two terms are order δt². However, using (3.6), one of the integrals in the third term is killed by the delta function, leaving just one integral standing. This ensures that the third term is actually proportional to δt, ⟨δx δx⟩ = 2δ Dδt+O(δt²) (3.22)

i j ij We will ignore the terms of order δt². Moreover, It is simple to see that all higher correlation functions are higher order in δt. For example, ⟨x⁴⟩ ∼ δt². These too will be ignored.

Our strategy now is to construct a probability distribution that reproduces (3.21) and (3.22). We start by considering the conditional probability P(x,t+δt;x′,t) that the particle sits at x at time t+δt given that, a moment earlier, it was sitting at x′. From the definition (3.16) we can write this as P(x,t+δt;x′,t) = ⟨δ(x−x′ −δx)⟩ where δx is the random variable here; it is the distance moved in time δt. Next, we do something that may look fishy: we Taylor expand the delta-function. If you're nervous about expanding a distribution in this way, you could always regulate the delta function in your favourite manner to turn it into a well behaved function. However, more pertinently, we will see that the resulting expression sits inside an integral where any offending terms make perfect sense. For now, we just proceed naively P(x,t+δt;x′,t) = (1+⟨δx⟩ ∂/∂x′ + ½ ⟨δx δx⟩ ∂²/∂x′∂x′ +...) δ(x−x′) (3.23)

i i j We have truncated at second order because we want to compare this to (3.27) and, as we saw above, ⟨δx⟩ and ⟨δx²⟩ are the only terms that are order δt.

We now have all the information that we need. We just have to compare (3.27) and (3.23) and figure out how to deal with those delta functions. To do this, we need one more trick. Firstly, recall that our real interest is in the evolution of the probability P(x,t;x₀,t₀), given some initial, arbitrary starting position x(t = t₀) = x₀. There is an obvious property that this probability must satisfy: if you look at some intermediate time t < t′ < t, then the particle has to be somewhere. Written as an equation, this "has to be somewhere" property is called the Chapman-Kolmogorov equation P(x,t;x₀,t₀) = d³x′ P(x,t;x′,t′)P(x′,t′;x₀,t₀) (3.24)

Replacing t by t + δt, we can substitute our expression (3.23) into the Chapman-Kolmogorov equation, and then integrate by parts so that the derivatives on the delta function turn and hit P(x′,t′;x₀,t₀). The delta-function, now unattended by derivatives, kills the integral, leaving ∂/∂x (⟨δx⟩ P(x,t;x₀,t₀))

P(x,t+δt;x₀,t₀) = P(x,t;x₀,t₀)− i 0 0 + ½ ⟨δx δx⟩ ∂²/∂x ∂x P(x,t;x₀,t₀)+... (3.25)

i j i j 0 0 Using our expressions for ⟨δx⟩ and ⟨δxδx⟩ given in (3.21) and (3.22), this becomes P(x,t+δt;x₀,t₀) = P(x,t;x₀,t₀)+ (1/γ) ∂/∂x (∂V/∂x) P(x,t;x₀,t₀) δt i i 0 0 + D ∂²/∂x² P(x,t;x₀,t₀)δt+... (3.26)

But we can also get a much simpler expression for the left-hand side simply by Taylor expanding with respect to time, P(x,t+δt;x₀,t₀) = P(x,t;x₀,t₀)+ ∂/∂t P(x,t;x₀,t₀)δt+... (3.27)

Equating (3.27) with (3.26) gives us our final result, ∂P/∂t = (1/γ) ∇·(P∇V)+D∇²P (3.28)

This is the Fokker-Planck equation. This form also goes by the name of the Smoluchowski equation or, for probabilists, Kolomogorov's forward equation.

It is useful to write the Fokker-Planck equation as a continuity equation ∂P/∂t = −∇·J (3.29)

where the probability current is J = − (1/γ) P∇V +D∇P (3.30)

The second term is clearly due to diffusion (because there's a big capital D in front of it); the first term is due to the potential and is often referred to as the drift, meaning the overall motion of the particle due to background forces that we understand.

One advantage of writing the Fokker-Planck equation in terms of a current is that we see immediately that probability is conserved, meaning that if ∫d³xP = 1 at some point in time then it will remain so for all later times. This follows by a standard argument, ∂/∂t ∫d³xP = ∫d³x ∂P/∂t = ∫d³x ∇·J = 0 where the last equality follows because we have a total derivative (and we are implicitly assuming that there's no chance that the particle escapes to infinity so we can drop the boundary term).

boundary term).

The Fokker-Planck equation tells us how systems evolve. For some systems, such as those described by the diffusion equation, there is no end point to this evolution: the system just spreads out more and more. However, for generic potentials V there are time-independent solutions to the Fokker-Planck equation obeying ∇ · J = 0. These are the equilibrium configurations. The solution is given by P(⃗x) ∼ e−V(⃗x)/γD Using the Einstein relation (3.12), this becomes something very familiar. It is simply the Boltzmann distribution for a particle with energy V(⃗x) in thermal equilibrium P(⃗x) ∼ e−V(⃗x)/kBT (3.31)

Isn’t that nice! (Note that there’s no kinetic energy in the exponent as we set m = 0 as our starting point).

An Application: Escape over a Barrier As an application of the Fokker-Planck equation, consider thermal escape from the one-dimensional potential shown in Figure 7. We’ll assume that all the particles start off sitting close to the local minimum at xmin. We model the potential close to this point as V(x) ≈ ω2min (x−xmin)2/2 and we start our particles in a distribution that is effectively in local equilibrium (3.31), with P(x,t = 0) = √(ω2min / 2πkBT) e−ω2min (x−xmin)2/2kBT (3.32)

V(x)

x x x min max * Figure 7: Escape over a Barrier.

But, globally, xmin is not the lowest energy configuration and this probability distribution is not the equilibrium configuration. In fact, as drawn, the potential has no global minimum and there is no equilibrium distribution. So this isn’t what we’ll set out to find. Instead, we would like to calculate the rate at which particles leak out of the trap and over the barrier.

Although we’re clearly interested in a time dependent process, the way we proceed is to assume that the leakage is small and so can be effectively treated as a steady state process. This means that we think of the original probability distribution of particles (3.32) as a bath which, at least on the time scales of interest, is unchanging. The steady state leakage is modelled by a constant probability current J = J0, with J given by (3.30). Using the Einstein relation D = kBT/γ, we can rewrite this as J = − (kBT/γ) e−V(x)/kBT ∂/∂x ( e+V(x)/kBT P )

The first step is to integrate J e+V(x)/kBT between the minimum xmin and some distance far from all the action, x ≫ xmin, which we may as well call x = x⋆, ∫_{xmin}^{x⋆} dx J eV(x)/kBT = − [ eV(x⋆)/kBT P(x⋆) − eV(xmin)/kBT P(xmin) ]

But we can take the probability P(x⋆) to be vanishingly small compared to P(xmin) given in (3.32), leaving us with ∫_{xmin}^{x⋆} dx J eV(x)/kBT ≈ (kBT/γ) √(ω2min / 2πkBT) (3.33)

Meanwhile, the integral on the left-hand-side is dominated by the maximum of the potential. Let’s suppose that close to the maximum, the potential looks like V(x) ≈ Vmax − ω2max (x−xmax)2/2 Then we’ll write the integral as J0 ∫_{xmin}^{x⋆} dx eV(x)/kBT ≈ J0 eVmax/kBT √(2πkBT / ω2max) (3.34)

Combining the two expressions (3.33) and (3.34), we get our final result for the rate of escape over the barrier J ≈ (ωmin ωmax / 2πγ) e−Vmax/kBT 3.2.3 Velocity Diffusion So far we’ve ignored the inertia term, setting m = 0. Let’s now put it back in. We can start by setting the potential to zero, so that the Langevin equation is m⃗¨x = −γ⃗˙x + ⃗f(t)

But, we can trivially rewrite this as a first order equation involving ⃗v = ⃗˙x, m⃗˙v = −γ⃗v + ⃗f(t)

This means that if we’re only interested in the distribution over velocities, P(⃗v,t), then we have exactly the same problem that we’ve just looked at, simply replacing ⃗x → ⃗v and γ → m. (Actually, you need to be a little more careful. The diffusion constant D that appears in (3.28) was really Dγ2/γ2 where the numerator arose from the noise correlator and the denominator from the γ⃗x term in the Langevin equation. Only the latter changes, meaning that this combination gets replaced by Dγ2/m2). The resulting Fokker-Planck equation is ∂P/∂t = (1/m) ∂/∂⃗v · ( γP⃗v + (Dγ2/m) ∂P/∂⃗v ) (3.35)

The equilibrium distribution that follows from this obeys ∂P/∂t = 0, meaning ∂P/∂⃗v = − (m/Dγ) P⃗v ⇒ P = (m/2πkBT)^(3/2) e−m⃗v2/2kBT where we’ve again used the Einstein relation Dγ = kBT. This, of course, is the Maxwell-Boltzmann distribution.

In fact, we can do better than this. Suppose that we start all the particles off at t = 0 with some fixed velocity, ⃗v = ⃗v0. This means that the probability distribution is a delta-function, P(⃗v,t = 0) = δ3(⃗v − ⃗v0). We can write down a full time-dependent solution to the Fokker-Planck equation (3.35) with this initial condition.

P(⃗v,t) = (m / 2πkBT(1−e−2γt/m))^(3/2) exp( − m(⃗v − ⃗v0 e−γt/m)2 / 2kBT(1−e−2γt/m) )

As t → ∞, we return to the Maxwell-Boltzmann distribution. But now this tells us how we approach equilibrium.

The Kramers-Chandrasekhar Fokker-Planck Equation As our final example of a Fokker-Planck equation, we can consider the Langevin equation with both acceler ation term and potential term, ¨ ˙ ⃗ m⃗x = −γ⃗x−∇V +f(t)

Now we are looking for a probability distribution over phase space, P(⃗x,⃗x,t). The right way to proceed is to write this as two first-order equations. The first of these is simply the definition of velocity ⃗v = x˙. The second is the Langevin equation ˙ ⃗ m⃗v = −γ⃗v −∇V +f(t)

These can now be combined into a single Langevin equation for six variables. Once armed with this, we need only follow the method that we saw above to arrive at a Fokker-Planck equation for P(⃗x,⃗v,t), (cid:18) ∂ ∂ (cid:19) 1 ∂ (cid:18) ∂V (cid:19) Dγ2 ∂2P +vi P = γviP +P + (3.36)

∂t ∂xi m∂vi ∂xi m2 ∂vi∂vi This form of the Fokker-Planck equations is sometimes called the Kramers equation and sometimes called the Chandrasekhar equation.

Note that this equation is now capturing the same physics that we saw in the Boltz- mann equation: the probability distribution P(⃗x,⃗v,t) is the same object that we called f (⃗r,p⃗;t) in Section 2. Moreover, it is possible to derive this form of the Fokker-Planck equation, starting from the Boltzmann equation describing a heavy particle in a sur- rounding bath of light particles. The key approximation is that in small time intervals δt, the momentum of the heavy particle only changes by a small amount. Looking back, you can see that this was indeed an assumption in the derivation of the Fokker-Planck equation in Section 3.2.2, but not in the derivation of the Boltzmann equation.

– 70 – Integrating over Velocity The equation (3.36) governing the probability distribution over phase space P(⃗x,⃗v,t)

looks very different from the Fokker-Planck equation governing the probability distri- bution over configuration space (3.28). Yet the related Langevin equations are simply related by setting m = 0 or, equivalently, looking at systems with large γ. How can we derive (3.28) from (3.36)?

The computation involves a careful expansion of (3.36) in powers of 1/γ. Let’s see how this works. Firstly, we use the Einstein relation to write Dγ = k T, and rearrange the terms in (3.36) to become (cid:18)

k T ∂ vi(cid:19)

(cid:18)

∂ ∂ 1 ∂V ∂ (cid:19)

B + P = +vi − P (3.37)

∂vi m2 ∂vi m γ ∂t ∂xi m∂xi∂vi We’re going to solve this perturbatively in 1/γ, writing 1 1 P = P(0) + P(1) + P(2) +...

γ γ2 As our first pass at this, we drop anything that has a 1/γ, which mean that P(0) must be annihilated by the left-hand-side of (3.37). This is a simple differential equation, with solution P(0)(v,x,t) = e−mv2/2kBT ϕ(0)(x,t)

for any function ϕ(0)(x,t). Of course, the velocity dependence here is simply the Maxwell-Boltzmann distribution. To figure out what restrictions we have on ϕ(0), we need to go to the next order in perturbation theory. Keeping terms of O(1/γ), the differential equation (3.37) becomes ∂ (cid:18) k T ∂ vi(cid:19) (cid:18) ∂ ∂ vi ∂V (cid:19)

B + P(1) = +vi + ϕ(0)e−mv2/2kBT (3.38)

∂vi m2 ∂vi m ∂t ∂xi k T ∂xi But this equation cannot be solved for arbitrary ϕ(0). This is simplest to see if we just (cid:82)

integrate both sides over d3v: the left-hand-side is a total derivative and so vanishes.

On the right-hand-side, only one term remains standing and this must vanish. It is ∂ϕ(0)

= 0 ∂t So ϕ(0) = ϕ(0)(x). With this constraint, the solution to (3.38) is, again, straightforward to write down. It is (cid:18) ∂ϕ(0) m ∂V (cid:19)

P(1)(x,v,t) = −mvi − vi ϕ(0) +ϕ(1)(x,t) e−mv2/2kBT ∂xi k T ∂xi – 71 – Atthispoint, itdoesn’tlooklikewe’remakingmuchprogress. Westilldon’tknowwhat ϕ(0)(x)isandwe’venowhadtointroduceyetanotherarbitraryfunction,ϕ(1)(x,t)which carries all the time dependence. Let’s plug this once more into (3.37), now working to order O(1/γ2). After a little bit of algebra, the equation becomes (cid:18)

k T ∂ vi(cid:19) (cid:20)

(cid:18)

∂ 1 ∂V (cid:19)

B + P(2) = −mvivj + ϕ(0)

∂vi m2 ∂vi m ∂xi ∂xj k T ∂xj (cid:18) (cid:19)(cid:18) (cid:19)

∂V m ∂ 1 ∂V + δ − vivj + ϕ(0)

∂xi ij k T ∂xj k T ∂xj B B (cid:18) ∂ ∂ vi ∂V (cid:19) (cid:21)

+ +vi + ϕ(1) e−mv2/2kBT ∂t ∂xi k T ∂xi Once again, there’s a consistency condition that must be realised if this equation is (cid:82)

to have a solution. Integrating over d3v, the left-hand-side is a total derivative and therefore vanishes. Any term linear in v on the right-hand-side also vanishes. But so too do the terms on the second line: you can check that the Gaussian integral over the δ term exactly cancels the vivj term. The resulting consistency condition is ij ∂ϕ(1) ∂ (cid:18) ∂ 1 ∂V (cid:19)

= k T − ϕ(0) (3.39)

∂t B ∂xi ∂xi k T ∂xi where the overall factor of k T on the right-hand-side comes only arises when you do (cid:82)

the Gaussian integral over d3v.

Now we’re almost there. (Although it probably doesn’t feel like it!). Collecting what we’ve learned, to order O(1/γ), the probability distribution over phase space takes the form (cid:18) mvi∂ϕ(0) mvi ∂V ϕ(1)(cid:19)

P(x,v,t) = ϕ(0) − − ϕ(0) + e−mv2/2kBT γ ∂xi γk T ∂xi γ But to make contact with the earlier form of the Fokker-Planck equation (3.28), we want a distribution ove configuration space. We get this by simply integrating over velocities. We’ll also denote the resulting probability distribution as P(x,t), with only the arguments to tell us that it’s a different object: P(x,t) = ∫ d³v P(x,v,t) = √(2πkT/m) [ϕ⁽⁰⁾(x) + ϕ⁽¹⁾(x,t)]

But now we can use the consistency condition (3.39) to compute ∂P/∂t. Working only to order O(1/γ), this reads ∂P/∂t = (kT/γ) ∂/∂xⁱ (∂P/∂xⁱ + (1/kT) ∂V/∂xⁱ P)

Which is precisely the Fokker-Planck equation (3.28) that we saw previously.

3.2.4 Path Integrals: Schrödinger, Feynman, Fokker and Planck There is a close similarity between the Fokker-Planck equation and the Schrödinger equation in quantum mechanics. To see this, let’s return to the first order Langevin equation dx⃗/dt = -∇V + f⃗ (3.40)

and the corresponding Fokker-Planck equation (3.28). We can change variables to P(x,t) = e^{-V(x)/2γD} P̃(x,t) (3.41)

Substituting into the Fokker-Planck equation, we see that the rescaled probability P̃ obeys ∂P̃/∂t = D∇²P̃ + [ (1/2γ) ∇²V - (1/4γ²D) (∇V)² ] P̃ (3.42)

There are no first order gradients ∇P̃; only ∇²P̃. This form of the Fokker-Planck equation looks very similar to the Schrödinger equation.

iℏ ∂ψ/∂t = - (ℏ²/2m) ∇²ψ + U(x⃗)ψ All that’s missing is a factor of i on the left-hand-side. Otherwise, with a few trivial substitutions, the two equations look more or less the same. Note, however, that the relationship between the potentials is not obvious: if we want to relate the two equations, we should identify U = - (1/2γ) ∇²V + (1/4Dγ²) (∇V)² (3.43)

The relationship between the evolution of quantum and classical probabilities is also highlighted in the path integral formulation. Recall that the Schrödinger equation can be reformulated in terms of function integrals, with the quantum amplitude for a particle to travel from x⃗ᵢ at time tᵢ to x⃗f at time tf given by⁸.

⟨x⃗f, tf | x⃗ᵢ, tᵢ⟩ = ∫ 𝒩 𝒟x(t) exp[ (i/ℏ) ∫ dt ( (m/2) ẋ⃗² - U(x⃗) ) ]

⁸A derivation of the path integral from the Schrödinger equation can be found in the lectures on Classical Dynamics.

where 𝒩 is a normalization factor. Here the integral is over all paths which start at (x⃗ᵢ, tᵢ) and end at (x⃗f, tf). By analogy, we expect there to be a similar path integral formulation of the classical probability for a particle in the Langevin environment (3.40) to travel from x⃗ᵢ to x⃗f. Indeed, the existence of a path integral formulation for this problem is very natural. The essence of this can already be seen in the Chapman-Kolmogorov equation (3.24)

P(x⃗,t; x⃗₀,t₀) = ∫ d³x⃗′ P(x⃗,t; x⃗′,t′) P(x⃗′,t′; x⃗₀,t₀)

This simply says that to get from point A to point B, a particle has to pass through some position in between. And we sum up the probabilities for each position. Adding many more intervening time steps, as shown in Figure 8, naturally suggests that we should be summing over all possible paths.

Deriving the Path Integral Here we will sketch the derivation of the path integral formula for the Fokker-Planck equation. We’ve already met function integrals in Section 3.1.4 where we introduced the probability distribution for a given noise function f(t)

Prob[f(t)] = 𝒩 exp[ - (1/4Dγ²) ∫ dt f⃗(t)·f⃗(t) ] (3.44)

subject to the normalization condition ∫ 𝒟f(t) Prob[f(t)] = 1 (3.45)

But given a fixed noise profile f(t) and an initial condition, the path of the particle is fully determined by the Langevin equation (3.40). Let’s call this solution x⃗f(t). Then the probability that the particle takes the path x⃗f is the same as the probability that the force is f, Prob[x⃗f(t)] = Prob[f(t)] = 𝒩 exp[ - (1/4Dγ²) ∫ dt f⃗(t)·f⃗(t) ]

= 𝒩 exp[ - (1/4Dγ²) ∫ dt (γẋ⃗f + ∇V(x⃗f))² ]

where, in the last line, we’ve used the Langevin equation (3.40) to relate the force to the path taken. But since this equation holds for any path x⃗f, we can simply drop the f label. We have the probability that the particle takes a specific path x⃗(t) given by Prob[x⃗(t)] = 𝒩 exp[ - (1/4Dγ²) ∫ dt (γẋ⃗ + ∇V)² ]

The total probability to go from x⃗ᵢ to x⃗f should therefore just be the sum over all these paths. With one, slightly fiddly, subtlety: the probability is normalized in (3.45) with respect to the integration measure over noise variable f. And we want to integrate over paths. This means that we have to change integration variables and pick up a Jacobian factor for our troubles. We have Prob[x⃗f, tf; x⃗ᵢ, tᵢ] = 𝒩 ∫ 𝒟f(t) exp[ - (1/4Dγ²) ∫ dt (γẋ⃗f + ∇V(x⃗f))² ]

= 𝒩 ∫ 𝒟x(t) detM exp[ - (1/4Dγ²) ∫ dt (γẋ⃗ + ∇V)² ] (3.46)

Here the operator M(t,t′) that appears in the Jacobian can be thought of as δf(t)/δx(t′). It can be written down by returning to the Langevin equation.

on (3.40) which relates f and x, M(t,t′) = γ ∂/∂t δ(t−t′) + ∇²V δ(t−t′)

If we want to think in a simple minded way, we can consider this as a (very large) matrix M, with columns labelled by the index t and rows labelled by t′. We’ll write the two terms in this matrix as M = A+B so the determinant becomes det(A+B) = detA det(1+A⁻¹B) (3.47)

The first operator A = γ ∂/∂t δ(t−t′) doesn’t depend on the path and its determinant just gives a constant factor which can be absorbed into the normalization N. The operator A⁻¹ in the second term is defined in the usual way as ∫ dt′ A(t,t′) A⁻¹(t′,t′′) = δ(t−t′′)

where the integral over dt′ is simply summing over the rows of A and the columns of A⁻¹ as in usual matrix multiplication. It is simple to check that the inverse is simply the step function A⁻¹(t′,t′′) = θ(t′ −t′′) (3.48)

Now we write the second factor in (3.47) and expand, det(1+A⁻¹B) = exp Tr log(1+A⁻¹B) = exp Tr ∑ (A⁻¹B)ⁿ/n (3.49)

Here we should look in more detail at what this compact notation means. The term Tr A⁻¹B is really short-hand for Tr A⁻¹B = ∫ dt dt′ A⁻¹(t,t′) B(t′,t)

where the integral over dt′ is multiplying the matrices together while the integral over dt comes from taking the trace. Using (3.48) we have Tr A⁻¹B = ∫ dt dt′ θ(t−t′) ∇²V δ(t−t′) = ∫ dt (1/γ) θ(0) ∇²V The appearance of θ(0) may look a little odd. This function is defined to be θ(x) = +1 for x > 0 and θ(x) = 0 for x < 0. The only really sensible value at the origin is θ(0) = 1/2. Indeed, this follows from the standard regularizations of the step function, for example θ(x) = lim_{µ→0} (1/2 + (1/π) tan⁻¹(x/µ)) ⇒ θ(0) = 1/2 What happens to the higher powers of (A⁻¹B)ⁿ? Writing them out, we have Tr (A⁻¹B)ⁿ = ∫ dt₁ dt₂ ... dt₂ₙ₋₁ θ(t₁−t₂) δ(t₂−t₃) θ(t₃−t₄) δ(t₄−t₅) ... θ(t₂ₙ₋₂−t₂ₙ₋₁) δ(t₂ₙ₋₁−t₂ₙ) (∇²V)ⁿ / γⁿ where we have been a little sloppy in writing (∇²V)ⁿ because each of these is actually computed at a different time. We can use the delta-functions to do half of the integrals, say all the t for n odd. We get Tr (A⁻¹B)ⁿ = ∫ dt₂ dt₄ dt₆ ... θ(t₁−t₂) θ(t₃−t₄) θ(t₅−t₆) ... θ(t₂ₙ₋₁−t₂ₙ) (∇²V)ⁿ / γⁿ But this integral is only non-vanishing only if t₂ > t₄ > t₆ > ... > t₂ₙ₋₂ > t₂ₙ. In other words, the integral vanishes. (Note that you might think we could again get contributions from θ(0) = 1/2, but the integrals now mean that the integrand has support on a set of zero measure. And with no more delta-functions to rescue us, gives zero.) The upshot of this is that the determinant (3.49) can be expressed as a single exponential det(1+A⁻¹B) = exp( ∫ dt ∇²V / (2γ) )

We now have an expression for the measure factor in (3.46). Using this, the path integral for the probability becomes, Prob[x⃗_f, t_f; x⃗_i, t_i] = N′ ∫ Dx(t) exp( -∫ dt (γ x⃗˙ + ∇V)² / (4Dγ²) + ∫ dt ∇²V / (2γ) )

= N′ e^{[V(x_f)−V(x_i)]/(2γD)} ∫ Dx(t) exp( -∫ dt (x⃗˙² / (4D) + U) )

where U is given in (3.43). Notice that the prefactor e^{[V(x_f)−V(x_i)]/(2γD)} takes the same form as the map from probabilities P to the rescaled P in (3.41). This completes our derivation of the path integral formulation of probabilities.

3.2.5 Stochastic Calculus There is one final generalization of the Langevin equation that we will mention but won’t pursue in detail. Let’s return to the case m = 0, but generalise the noise term in the Langevin equation so that it is now spatially dependent. We write γ x⃗˙ = −∇V + b(x⃗) f(t) (3.50)

This is usually called the non-linear Langevin equation. The addition of the b(x⃗) multiplying the noise looks like a fairly innocuous change. But it’s not. In fact, annoyingly, this equation is not even well defined!

The problem is that the system gets a random kick at time t, the strength of which depends on its position at time t. But if the system is getting a delta-function impulse at time t then its position is not well defined. Mathematically, this problem arises when we look at the position after some small time δt. Our equation (3.20) now becomes δx⃗ = x⃗˙ δt = −(1/γ) ∇V δt + (1/γ) ∫_t^{t+δt} dt′ b(x⃗(t′)) f(t′)

and our trouble is in making sense of the last term. There are a couple of obvious ways we could move forward: • Ito: We could insist that the strength of the kick is related to the position of the particle immediately before the kick took place. Mathematically, we replace the integral with ∫_t^{t+δt} dt′ b(x⃗(t′)) f(t′) → b(x⃗(t)) ∫_t^{t+δt} dt′ f(t′)

This choice is known as Ito stochastic calculus.

• Stratonovich: Alternatively, we might argue that the kick isn’t really a delta function. It is really a process that takes place over a small, but finite, time. To model this, the strength of the kick should be determined by the average position over which this process takes place. Mathematically, we replace the integral with, (cid:90) t+δt 1 (cid:90) t+δt dt′b(⃗x(t′))f ⃗ (t′) −→ [b(⃗x(t+δt))+b(⃗x(t))] dt′f ⃗ (t′)

t t This choice is known as Stratonovich stochastic calculus.

Usually in physics, issues of this kind don’t matter too much. Typically, any way of regulating microscopic infinitesimals leads to the same macroscopic answers. However, this is not the case here and the Ito and Stratonovich methods give different answers in the continuum. In most applications of physics, including Brownian motion, the Stratonovich calculus is the right way to proceed because, as we argued when we first introduced noise, the delta-function arising in the correlation function ⟨f(t)f(t′)⟩ is just a convenient approximation to something more smooth. However, in other applications such as financial modelling, Ito calculus is correct.

The subject of stochastic calculus is a long one and won’t be described in this course.

For the Stratonovich choice, the Fokker-Planck equation turns out to be ∂P 1 (cid:2) (cid:3)

= ∇· P(∇V −Dγ2b∇b) +D∇2(b2P)

∂t γ This is also the form of the Fokker-Planck equation that you get by naively dividing ˙ ˙ (3.50) by b(⃗x) and the defining a new variable ⃗y = ⃗x/b which reduces the problem to our previous Langevin equation (3.19). In contrast, if we use Ito stochastic calculus, the b∇b term is absent in the resulting Fokker-Planck equation.

– 78 –

## 4. Linear Response

The goal of response theory is to figure out how a system reacts to outside influences.

These outside influences are things like applied electric and magnetic fields, or applied pressure, or an applied driving force due to some guy sticking a spoon into a quantum liquid and stirring.

We’ve already looked at a number of situations like this earlier in these lectures. If you apply a shearing force to a fluid, its response is to move; how much it moves is determined by the viscosity. If you apply a temperature gradient, the response is for heattoflow; theamountofheatisdeterminedbythethermalconductivity. However, in both of these cases, the outside influence was time independent. Our purpose here is to explore the more general case of time dependent influences. As we’ll see, by studying the response of the system at different frequencies, we learn important information about what’s going on inside the system itself.

## 4.1 Response Functions

Until now, our discussion has been almost entirely classical. Here we want to deal with both classical and quantum worlds. For both cases, we start by explaining mathemat- ically what is meant by an outside influence on a system.

Forces in Classical Dynamics Consider a simple dynamical system with some generalized coordinates x (t) which depend on time. If left alone, these coordinates will obey some equations of motion, x¨ +g (x˙,x) = 0 i i This dynamics need not necessarily be Hamiltonian. Indeed, often we’ll be interested in situations with friction. The outside influence in this example arises from perturbing the system by the addition of some driving forces F (t), so that the equations of motion become, x¨ +g (x˙,x) = F (t) (4.1)

i i i In this expression, x (t) are dynamical degrees of freedom. This is what we’re solving for. In contrast, F (t) are not dynamical: they’re forces that are under our control, like someone pulling on the end of a spring. We get to decide on the time dependence of each F (t).

– 79 – It may be useful to have an even more concrete example at the back of our minds.

For this, we take every physicist’s favorite toy: the simple harmonic oscillator. Here we’ll include a friction term, proportional to γ, so that we have the damped harmonic oscillator with equation of motion x¨+γx˙ +ω2x = F(t) (4.2)

We will discuss this model in some detail in section 4.2.

Sources in Quantum Mechanics In quantum mechanics, we introduce the outside influences in a slightly different man- ner. The observables of the system are now operators, O . We’ll work in the Heisenberg picture, so that the operators are time dependent: O = O(t). Left alone, the dynamics of these operators will be governed by a Hamiltonian H(O). However, we have no interest in leaving the system alone. We want to give it a kick. Mathematically this is achieved by adding an extra term to the Hamiltonian, H (t) = ϕ (t)O (t) (4.3)

source i i The ϕ (x) are referred to as sources. They are external fields that are under our control, analogous to the driving forces in the example above. Indeed, if we take a classical Hamiltonian and add a term of the form xϕ then the resulting Euler-Lagrange equations include the source ϕ on the right-hand-side in the same way that the force F appears in (4.2).

4.1.1 Linear Response We want to understand how our system reacts to the presence of the source or the drivingforce. Tobeconcrete,we’llchosetoworkinthelanguageofquantummechanics, but everything that we discuss in this section will also carry over to classical systems.

Our goal is to understand how the correlation functions of the theory chang when we turn on a source (or sources) ϕ(x). In general, it’s a difficult question to understand how the theory is deformed by the sources. To figure this out, we really just need to sit down and solve the theory all over again. However, we can make progress under the assumption that the source is a small perturbation of the original system. This is fairly restrictive but it’s the simplest place where we can make progress so, from now on, we focus on this limit. Mathematically, this means that we assume that the change in the expectation value of any operator is linear in the perturbing source. We write δ⟨O_i(t)⟩ = ∫ dt' χ_ij(t;t')ϕ_j(t') (4.4)

Here χ_ij(t;t') is known as a response function. We could write a similar expression for the classical dynamical system (4.1), where δ⟨O_i⟩ is replaced by x_i(t) and ϕ is replaced by the driving force F(t). In classical mechanics, it is clear from the form of the equation of motion (4.1) that the response function is simply the Green’s function for the system. For this reason, the response functions are often called Green’s functions and you’ll often see them denoted as G instead of χ.

From now on, we’ll assume that our system is invariant under time translations. In this case, we have χ_ij(t;t') = χ_ij(t−t')

and it is useful to perform a Fourier transform to work in frequency space. We define the Fourier transform of the function f(t) to be f(ω) = ∫ dt e^{iωt} f(t) and f(t) = ∫ (dω/2π) e^{-iωt} f(ω) (4.5)

In particular, we will use the convention where the two functions are distinguished only by their argument.

Taking the Fourier transform of (4.4) gives δ⟨O_i(ω)⟩ = ∫ dt' ∫ dt e^{iωt} χ_ij(t−t')ϕ_j(t')

= ∫ dt' ∫ dt e^{iω(t−t')} χ_ij(t−t') e^{iωt'} ϕ_j(t')

= χ_ij(ω) ϕ_j(ω) (4.6)

We learn the response is “local” in frequency space: if you shake something at frequency ω, it responds at frequency ω. Anything beyond this lies within the domain of non-linear response.

In this section we’ll describe some of the properties of the response function χ(ω) and how to interpret them. Many of these properties follow from very simple physical input. To avoid clutter, we’ll mostly drop both the i,j indices. When there’s something interesting to say, we’ll put them back in.

4.1.2 Analyticity and Causality If we work with a real source ϕ and a Hermitian operator O (which means a real expectation value ⟨O⟩) then χ(t) must also be real. Let’s see what this means for the Fourier transform χ(ω). It’s useful to introduce some new notation for the real and imaginary parts, χ(ω) = Reχ(ω) + i Imχ(ω)

≡ χ'(ω) + i χ''(ω)

This notation in terms of primes is fairly odd the first time you see it, but it’s standard in the literature. You just have to remember that, in this context, primes do not mean derivatives!

The real and imaginary parts of the response function χ(ω) have different interpretations. Let’s look at these in turn • Imaginary Part: We can write the imaginary piece as χ''(ω) = − (1/i) [χ(ω)−χ⋆(ω)]

= − (1/i) ∫_{-∞}^{+∞} dt χ(t)[e^{iωt} − e^{-iωt}]

= − (1/i) ∫_{-∞}^{+∞} dt e^{iωt}[χ(t)−χ(−t)]

We see that the imaginary part of χ(ω) is due to the part of the response function that is not invariant under time reversal t → −t. In other words, χ''(ω) knows about the arrow of time. Since microscopic systems are typically invariant under time reversal, the imaginary part χ''(ω) must be arising due to dissipative processes.

χ''(ω) is called the dissipative or absorptive part of the response function. It is also known as the spectral function. It will turn out to contain information about the density of states in the system that take part in absorptive processes. We’ll see this more clearly in an example shortly.

Finally, notice that χ''(ω) is an odd function, χ''(−ω) = −χ''(ω)

• Real Part: The same analysis as above shows that χ'(ω) = ∫_{-∞}^{+∞} dt e^{iωt}[χ(t)+χ(−t)]

The real part doesn’t care about the arrow of time. It is called the reactive part of the response function. It is an even function, χ'(−ω) = +χ'(ω)

Before we move on, we need to briefly mention what happens when we put the labels i,j back on the response functions. In this case, a similar analysis to that above shows that the dissipative response function comes from the anti-Hermitian part, χ''_ij(ω) = − (1/2i) [χ_ij(ω)−χ⋆_ji(ω)] (4.7)

Causality We can’t affect the past. This statement of causality means that any response function must satisfy χ(t) = 0 for all t < 0 For this reason, χ is often referred to as the causal Green’s function or retarded Green’s function and is sometimes denoted as G_R(t). Let’s see what this simple causality requirement means for the Fourier expansion of χ, χ(t) = ∫_{-∞}^{+∞} (dω/2π) e^{-iωt} χ(ω)

When t < 0, we can perform the integral by completing the contour in the upper-half plane (so that the exponent becomes −iω×(−i|t|) → −∞). The answer has to be zero. Of course, the integral is given by the sum of the residues inside the contour. So if we want the response function to vanish for all t < 0, it must be that χ(ω) has no poles in the upper-half plane. In other words, causality requires: χ(ω) is analytic for Imω > 0.

4.1.3 Kramers-Kronig Relation The fact that χ is analytic in the upper-half plane means that there is a relationship between the real and imaginary parts, χ′ and χ′′. This is called the Kramers-Kronig relation. Our task in this section is to derive it. We start by providing a few general mathematical statements about complex integrals.

A Discontinuous Function First, consider a general function ρ(ω). We’ll ask that ρ(ω) is meromorphic, meaning that it is analytic apart from isolated poles. But, for now, we won’t place any restrictions on the position of these poles. (We will shortly replace ρ(ω) by χ(ω) which, as we’ve just seen, has no poles in the upper half plane). We can define a new function f(ω) by the integral, f(ω) = 1/(iπ) ∫_a^b ρ(ω′)/(ω′ − ω) dω′ (4.8)

Here the integral is taken along the interval ω′ ∈ [a,b] of the real line. However, when ω also lies in this interval, we have a problem because the integral diverges at ω′ = ω. To avoid this, we can simply deform the contour of the integral into the complex plane, either running just above the singularity along ω′ + iϵ or just below the singularity along ω′ − iϵ. Alternatively (in fact, equivalently) we could just shift the position of the singularity to ω → ω ∓ ϵ. In both cases we just skim by the singularity and the integral is well defined. The only problem is that we get different answers depending on which way we do things. Indeed, the difference between the two answers is given by Cauchy’s residue theorem, [f(ω + iϵ) − f(ω − iϵ)] = ρ(ω) (4.9)

The difference between f(ω + iϵ) and f(ω − iϵ) means that the function f(ω) is discontinuous across the real axis for ω ∈ [a,b]. If ρ(ω) is everywhere analytic, this discontinuity is a branch cut.

We can also define the average of the two functions either side of the discontinuity. This is usually called the principal value, and is denoted by adding the symbol P before the integral, 1/2 [f(ω + iϵ) + f(ω − iϵ)] ≡ P 1/(iπ) ∫_a^b ρ(ω′)/(ω′ − ω) dω′ (4.10)

We can get a better handle on the meaning of this principal part if we look at the real and imaginary pieces of the denominator in the integrand 1/[ω′ − (ω ± iϵ)], 1/(ω′ − (ω ± iϵ)) = (ω′ − ω)/[(ω′ − ω)^2 + ϵ^2] ± iϵ/[(ω′ − ω)^2 + ϵ^2] (4.11)

By taking the sum of f(ω + iϵ) and f(ω − iϵ) in (4.10), we isolate the real part, the first term in (4.11). This is shown in the left-hand figure. It can be thought of as a suitably cut-off version of 1/(ω′−ω). It’s as if we have deleted a small segment of this function lying symmetrically about the divergent point ω and replaced it with a smooth function going through zero. This is the usual definition of the principal part of an integral.

We can also see the meaning of the imaginary part of 1/(ω′ − ω), the second term in (4.11). This is shown in the right-hand figure. As ϵ → 0, it tends towards a delta function, as expected from (4.9). For finite ϵ, it is a regularized version of the delta function.

Kramers-Kronig Let’s now apply this discussion to our response function χ(ω). We’ll be interested in the integral 1/(iπ) ∮_C χ(ω′)/(ω′ − ω) dω′, ω ∈ R (4.12)

where the contour C skims just above the real axis, before closing at infinity in the upper-half plane. We’ll need to make one additional assumption: that χ(z) falls off faster than 1/|z| at infinity. If this holds, the integral is the same as we consider in (4.8) with [a,b] → [−∞,+∞]. Indeed, in the language of the previous discussion, the integral is f(ω − iϵ), with ρ = χ.

We apply the formulae (4.9) and (4.10). It gives f(ω − iϵ) = 1/(iπ) [ P ∫_{-∞}^{+∞} χ(ω′)/(ω′ − ω) dω′ − χ(ω) ]

But we know the integral in (4.12) has to be zero since χ(ω) has no poles in the upper-half plane. This means that f(ω − iϵ) = 0, or χ(ω) = 1/(iπ) P ∫_{-∞}^{+∞} χ(ω′)/(ω′ − ω) dω′ (4.13)

The important part for us is that factor of “i” sitting in the denominator. Taking real and imaginary parts, we learn that Reχ(ω) = P/π ∫_{-∞}^{+∞} Imχ(ω′)/(ω′ − ω) dω′ (4.14)

and Imχ(ω) = −P/π ∫_{-∞}^{+∞} Reχ(ω′)/(ω′ − ω) dω′ (4.15)

These are the Kramers-Kronig relations. They follow from causality alone and tell us that the dissipative, imaginary part of the response function χ′′(ω) is determined in terms of the reactive, real part, χ′(ω) and vice-versa. However, the relationship is not local in frequency space: you need to know χ′(ω) for all frequencies in order to reconstruct χ′′ for any single frequency.

There’s another way of writing these relations which is also useful and tells us how we can reconstruct the full response function χ(ω) if we only know the dissipative part. To see this, look at 1/(iπ) ∫_{-∞}^{+∞} Imχ(ω′)/(ω′ − ω − iϵ) dω′ (4.16)

where the −iϵ in the denominator ominator tells us that this is an integral just below the real axis. Again using the formulae (4.9) and (4.10), we have ∫ +∞ dω′ Imχ(ω′) ∫ +∞ dω′ Imχ(ω′)

= Imχ(ω)+P iπ ω′ −ω −iϵ iπ ω′ −ω −iϵ −∞ −∞ = Imχ(ω)−iReχ(ω) (4.17)

Or, rewriting as χ(ω) = Reχ(ω)+iImχ(ω), we get ∫ +∞ dω′ Imχ(ω′)

χ(ω) = (4.18)

π ω′ −ω −iϵ −∞ If you know the dissipative part of the response function, you know everything.

An Application: Susceptibility Suppose that turning on a perturbation ϕ induces a response ⟨O⟩ for some observable of our system. Then the susceptibility is defined as χ = ∂⟨O⟩/∂ϕ |ω=0 We’ve called the susceptibility χ which is the same name that we gave to the response function. And, indeed, from the definition of linear response (4.4), the former is simply the zero frequency limit of the latter: χ = lim_{ω→0} χ(ω)

A common example, which we met in our first course in Statistical Mechanics, is the change of magnetization M of a system in response to an external magnetic field B. The aptly named magnetic susceptibility is given by χ = ∂M/∂B.

From (4.18), we can write the susceptibility as ∫ +∞ dω′ Imχ(ω′)

χ = (4.19)

π ω′ −iϵ −∞ We see that if you can do an experiment to determine how much the system absorbs at all frequencies, then from this information you can determine the response of the system at zero frequency. This is known as the thermodynamic sum rule.

## 4.2 Classical Examples

The definitions and manipulations of the previous section can appear somewhat abstract the first time you encounter them. Some simple examples should shed some light. The main example we’ll focus on is the same one that accompanies us through most of physics: the classical harmonic oscillator.

4.2.1 The Damped Harmonic Oscillator The equation of motion governing the damped harmonic oscillator in the presence of a driving force is x¨+γx˙ +ω2x = F(t) (4.20)

Here γ is the friction. We denote the undamped frequency as ω0, saving ω for the frequency of the driving force as in the previous section. We want to determine the response function, or Green’s function, χ(t − t′) of this system. This is the function which effectively solves the dynamics for us, meaning that if someone tells us the driving force F(t), the motion is given by x(t) = ∫ +∞ dt′χ(t−t′)F(t′) (4.21)

−∞ There is a standard method to figure out χ(t). Firstly, we introduce the (inverse) Fourier transform χ(t) = ∫ dω/(2π) e^{−iωt}χ(ω)

We plug this into the equation of motion (4.20) to get ∫ +∞ dω/(2π) ∫ +∞ dt′[−ω2 −iγω +ω2]e^{−iω(t−t′)}χ(ω)F(t′) = F(t)

−∞ −∞ which is solved if the ∫ dω gives a delta function. But since we can write a delta function as 2πδ(t) = ∫ dω e^{−iωt}, that can be achieved by simply taking χ(ω) = 1/(−ω2 −iγω +ω2) (4.22)

There’s a whole lot of simple physics sitting in this equation which we’ll now take some time to extract. All the lessons that we’ll learn carry over to more complicated systems.

Firstly, we can look at the susceptibility, meaning χ(ω = 0) = 1/ω2. This tells us how much the observable changes by a perturbation of the system, i.e. a static force: x = F/ω2 as expected.

Let’s look at the structure of the response function on the complex ω-plane. The poles sit at ω2 +iγω −ω2 = 0 or, solving the quadratic, at ω⋆ = −iγ/2 ± √(ω2 −γ2/4)

There are two different regimes that we should consider separately, • Underdamped: ω2 > γ2/4. In this case, the poles have both a real and imaginary part. They both sit on the lower half plane. This is in agreement with our general lesson of causality which tells us that the response function must be analytic in the upper-half plane • Overdamped: ω2 < γ2/4. Now the poles lie on the negative imaginary axis. Again, there are none in the upper-half place, consistent with causality.

We can gain some intuition by plotting the real and imaginary part of the response function for ω ∈ R. Firstly, the real part is shown in Figure 11 where we plot Reχ(ω) = (ω2 −ω2) / ((ω2 −ω2)2 +γ2ω2) (4.23)

This is the reactive part. The higher the function, the more the system will respond to a given frequency. Notice that Reχ(ω) is an even function, as expected.

More interesting is the dissipative part of the response function, Imχ(ω) = ωγ / ((ω2 −ω2)2 +γ2ω2) (4.24)

This is an odd function. In the underdamped case, this is plotted in Figure 12. Notice that Imχ is proportional to γ, the coefficient of friction. The function peaks around ±ω0, at frequencies where the system naturally vibrates. This is because this is where the system is able to absorb energy. However, as γ → 0, the imaginary part doesn’t become zero: instead it tend s towards two delta functions situated at ±ω.

4.2.2 Dissipation We can see directly how Imχ(ω) is related to dissipation by computing the energy absorbed by the system. This is what we used to call the work done on the system before we became all sophisticated and grown-up. It is dW/dt = F(t)ẋ(t)

= F(t) dt′χ(t−t′)F(t′)

= F(t) dt′ (−iω)e^{−iω(t−t′)}χ(ω)F(t′) dω/(2π)

= [−iωχ(ω)]e^{−i(ω+ω′)t}F(ω)F(ω′) dω dω′/(2π 2π)   (4.25)

Let’s drive the system with a force of a specific frequency Ω, so that F(t) = F₀ cosΩt = F₀ Re(e^{−iΩt})

Notice that it’s crucial to make sure that the force is real at this stage of the calculation because the reality of the force (or source) was the starting point for our discussion of the analytic properties of response functions in section 4.1.2. In a more pedestrian fashion, we can see that it’s going to be important because our equation above is not linear in F(ω), so it’s necessary to take the real part before progressing. Taking the Fourier transform, the driving force is F(ω) = 2πF₀ [δ(ω −Ω)+δ(ω +Ω)]

Inserting this into (4.25) gives dW/dt = −iF₀²Ω [χ(Ω)e^{−iΩt} −χ(−Ω)e^{+iΩt}] e^{−iΩt} +e^{iΩt}   (4.26)

This is still oscillating with time. It’s more useful to take an average over a cycle, ⟨dW/dt⟩ ≡ (Ω/(2π)) ∫₀^{2π/Ω} (dW/dt) dt = −iF₀²Ω[χ(Ω)−χ(−Ω)]

But we’ve already seen that Reχ(ω) is an even function, while Imχ(ω) is an odd function. This allows us to write dW/dt = 2F₀²Ω Imχ(Ω)   (4.27)

We see that the work done is proportional to Imχ. To derive this result, we didn’t need the exact form of the response function; only the even/odd property of the real/imaginary parts, which follow on general grounds. For our damped harmonic oscillator, we can now use the explicit form (4.24) to derive dW/dt = 2F₀² γΩ² / [(ω₀² −Ω²)² +(γΩ)²]

This is a maximum when we shake the harmonic oscillator at its natural frequency, Ω = ω₀. As this example illustrates, the imaginary part of the response function tells us the frequencies at which the system naturally vibrates. These are the frequencies where the system can absorb energy when shaken.

4.2.3 Hydrodynamic Response For our final classical example, we’ll briefly return to the topic of hydrodynamics. One difference with our present discussion is that the dynamical variables are now functions of both space and time. A typical example that we’ll focus on here is the mass density, ρ(x,t). Similarly, the driving force (or, in the context of quantum mechanics, the source) is similarly a function of space and time.

Rather than playing at the full Navier-Stokes equation, here we’ll instead just look at a simple model of diffusion. The continuity equation is ∂ρ/∂t + ∇·J = 0 We’ll write down a simple model for the current, J = −D∇ρ+F   (4.28)

where D is the diffusion constant and the first term gives rise to Fick’s law that we met already in Section 1. The second term, F = F(x,t), is the driving force. Combining this with the continuity equation gives, ∂ρ/∂t −D∇²ρ = −∇·F   (4.29)

We want to understand the response functions associated to this force. This includes both the response of ρ and the response of J.

For simplicity, let’s work in a single spatial dimension so that we can drop the vector indices. We write ρ(x,t) = ∫ dx′dt′ χ_{ρJ}(x′,t′;x,t)F(x′,t)

J(x,t) = ∫ dx′dt′ χ_{JJ}(x′,t′;x,t)F(x′,t)

where we’ve called the second label J on both of these functions to reflect the fact that F is a driving force for J. We follow our discussion of Section 4.1.1. We now assume that our system is invariant under both time and space translations which ensures that the response function depend only on t′−t and x′−x. We then Fourier transform with respect to both time and space. For example, ρ(ω,k) = ∫ dxdt e^{i(ωt−kx)}ρ(x,t)

Then in momentum and frequency space, the response functions become ρ(ω,k) = χ_{ρJ}(ω,k)F(ω,k)

J(ω,k) = χ_{JJ}(ω,k)F(ω,k)

The diffusion equation (4.29) immediately gives an expression for χ_{ρJ}. Substituting the resulting expression into (4.28) then gives us χ_{JJ}. The response functions are χ_{ρJ} = ik / (−iω +Dk²), χ_{JJ} = −iω / (−iω +Dk²)

Both of the denominator have poles on the imaginary axis at ω = −iDk². This is the characteristic behaviour of response functions capturing diffusion.

Our study of hydrodynamics in Sections 2.4 and 2.5 revealed a different method of transport, namely sound. For the ideal fluid of Section 2.4, the sound waves travelled without dissipation. The associated response function has the form χ_{sound} ∼ 1/(ω² −v²k²)

which is simply the Green’s function for the wave equation. If one includes the effect of dissipation, the poles of the response function pick up a (negative) imaginary part. For sound waves in the Navier-Stokes equation, we computed the location of these poles in (2.76).

## 4.3 Quantum Mechanics and the Kubo Formula

Let’s now return to quantum mechanics. Recall the basic set up: working in the Heisenberg picture, we add to a Hamiltonian the perturbation H(t) = ϕ(t)O(t) (4.30)

source j j where there is an implicit sum over j, labelling the operators in the theory and, correspondingly, the different sources that we can turn on. Usually in any given situation we only turn on a source for a single operator, but we may be interested in how this source affects the expectation value of any other operator in the theory, ⟨O⟩. However, if we restrict to small values of the source, we can address this using standard perturbation theory. We introduce the time evolution operator, U(t,t₀) = T exp(−i ∫ₜ₀ᵗ H_source(t′)dt′)

which is constructed to obey the operator equation idU/dt = H_source U. Then, switching to the interaction picture, states evolve as |ψ(t)⟩_I = U(t,t₀)|ψ(t₀)⟩_I We’ll usually be working in an ensemble of states described by a density matrix ρ. If, in the distant past t → −∞, the density matrix is given by ρ₀, then at some finite time it evolves as ρ(t) = U(t)ρ₀ U⁻¹(t)

with U(t) = U(t,t → −∞). From this we can compute the expectation value of any operator O in the presence of the sources ϕ. Working to first order in perturbation theory (from the third line below), we have ⟨O_i(t)⟩|_ϕ = Tr ρ(t)O_i(t)

= Tr ρ₀(t)U⁻¹(t)O_i(t)U(t)

≈ Tr ρ₀(t) (O_i(t) + i ∫₋∞ᵗ dt′ [H_source(t′), O_i(t)] + ...)

= ⟨O_i(t)⟩|_{ϕ=0} + i ∫₋∞ᵗ dt′ ⟨[H_source(t′), O_i(t)]⟩ + ...

Inserting our explicit expression for the source Hamiltonian gives the change in the expectation value, δ⟨O_i⟩ = ⟨O_i⟩_ϕ − ⟨O_i⟩_{ϕ=0}, δ⟨O_i⟩ = i ∫₋∞ᵗ dt′ ⟨[O_j(t′), O_i(t)]⟩ ϕ_j(t′)

= i ∫₋∞⁺∞ dt′ θ(t−t′) ⟨[O_j(t′), O_i(t)]⟩ ϕ_j(t′) (4.31)

where, in the second line, we have done nothing more than use the step function to extend the range of the time integration to +∞. Comparing this to our initial definition given in (4.4), we see that the response function in a quantum theory is given by the two-point function, χ_ij(t−t′) = −i θ(t−t′) ⟨[O_i(t), O_j(t′)]⟩ (4.32)

This important result is known as the Kubo formula. (Although sometimes the name “Kubo formula” is restricted to specific examples of this equation which govern transport properties in quantum field theory. We will derive these examples in Section 4.4).

4.3.1 Dissipation Again Before we make use of the Kubo formula, we will first return to the question of dissipation. Here we repeat the calculation of 4.2.2 where we showed that, for classical systems, the energy absorbed by a system is proportional to Imχ. Here we do the same for quantum systems. The calculation is a little tedious, but worth ploughing through.

As in the classical context, the work done is associated to the change in the energy of the system which, this time, can be written as dW/dt = d/dt Tr(ρH) = Tr(ρ̇H + ρḢ)

To compute physical observables, it doesn’t matter if we work in the Heisenberg or Schrödinger picture. So lets revert momentarily back to the Schrödinger picture. Here, the density matrix evolves as iρ̇ = [H,ρ], so the first term above vanishes. Meanwhile, the Hamiltonian H changes because we’re sitting there playing around with the source (4.30), providing an explicit time dependence. To simplify our life, we’ll assume that we turn on just a single source, ϕ. Then, in the Schrödinger picture Ḣ = O ϕ̇(t)

This gives us the energy lost by the system, dW/dt = Tr(ρ O ϕ̇) = ⟨O⟩_ϕ ϕ̇ = [⟨O⟩_{ϕ=0} + δ⟨O⟩] ϕ̇ We again look at a periodically varying source which we write as ϕ(t) = Re(ϕ₀ e⁻ⁱΩᵗ)

and we again compute the average work done over a complete cycle ⟨dW/dt⟩ = (Ω/2π) ∫₀^{2π/Ω} dt dW/dt The term ⟨O(⃗x)⟩ cancels out when integrated over the full cycle. This leaves us with ⟨dW/dt⟩ = (Ω/2π) ∫₀^{2π/Ω} dt ∫₋∞⁺∞ dt′ χ(t−t′) ϕ(t′) ϕ̇(t)

= (Ω/2π) ∫₀^{2π/Ω} dt ∫₋∞⁺∞ dt′ ∫ dω/(2π) χ(ω) e⁻ⁱω(t−t′)

× (ϕ₀ e⁻ⁱΩt′ + ϕ₀⋆ e⁺ⁱΩt′) (−iΩ ϕ₀ e⁻ⁱΩt + iΩ ϕ₀⋆ e⁺ⁱΩt)

= [χ(Ω) − χ(−Ω)] |ϕ₀|² iΩ where the ϕ₀² and ϕ₀⋆² terms have canceled out after performing the dt. Continuing, we only need the fact that the real part of χ is even while the imaginary part is odd. This gives us the result ⟨dW/dt⟩ = (1/2) Ω χ″(Ω) |ϕ₀|² (4.33)

Finally, this calculation tells us about another property of the response function. If we perform work on a system, the energy should increase. This translates into a positivity requirement Ω χ″(Ω) ≥ 0. More generally, the requirement is that Ω χ″_ij(Ω) is a positive definite matrix.

Spectral Representation In the case of the damped harmonic oscillator, we saw explicitly that the dissipation was proportional to the coefficient of friction, γ. But for our quantum systems, the dynamics is entirely Hamiltonian: there is no friction. So what is giving rise to the dissipation? In fact, the answer to this can also be found in our analysis of the harmonic oscillator, for there we found that in the limit γ → 0, the dissipative part of the response function χ″ doesn’t vanish but instead reduces to a pair of delta functions. Here we will s how that a similar property holds for a general quantum system. We’ll take the state of our quantum system to be described by a density matrix describing the canonical ensemble, ρ = e−βH. Taking the Fourier transform of the Kubo formula (4.32) gives

χ (ω) = −i ∫∞ dt eiωt Tr e−βH [O (t), O (0)]

ij i j

We will need to use the fact that operators evolve as O (t) = U−1 O (0) U with U = e−iHt and will evaluate χ (ω) by inserting a complete basis of energy states

χ (ω) = −i ∫∞ dt eiωt ∑ e−Emβ ⟨m|O |n⟩⟨n|O |m⟩ ei(Em−En)t ij 0 mn i j − ⟨m|O |n⟩⟨n|O |m⟩ ei(En−Em)t j i

To ensure that the integral is convergent for t > 0, we replace ω → ω + iϵ. Then performing the integral over dt gives

χ (ω + iϵ) = ∑ e−Emβ (O i ) mn (O j ) nm − (O j ) mn (O i ) nm ij m,n ω + Em − En + iϵ ω + En − Em + iϵ = ∑ (O i ) mn (O j ) nm ( e−Emβ − e−Enβ )

m,n ω + Em − En + iϵ

which tells us that the response function has poles just below the real axis, ω = Em − En − iϵ

Of course, we knew on general grounds that the poles couldn’t lie in the upper half-plane: we see that in a Hamiltonian system the poles lie essentially on the real axis (as ϵ → 0) at the values of the frequency that can excite the system from one energy level to another. In any finite quantum system, we have an isolated number of singularities. As in the case of the harmonic oscillator, in the limit ϵ → 0, the imaginary part of the response function doesn’t disappear: instead it becomes a sum of delta function spikes

χ′′ ∼ ∑ ϵ / ((ω + Em − En)2 + ϵ2) → ∑ δ(ω − (Em − En))

m,n m,n

The expression above is appropriate for quantum systems with discrete energy levels. However, in infinite systems — and, in particular, in the quantum field theories that we turn to shortly — these spikes can merge into smooth functions and dissipative behaviour can occur for all values of the frequency.

4.3.2 Fluctuation-Dissipation Theorem

We have seen above that the imaginary part of the response function governs the dissipation in a system. Yet, the Kubo formula (4.32) tells us that the response formula can be written in terms of a two-point correlation function in the quantum theory. And we know that such two-point functions provide a measure of the variance, or fluctuations, in the system. This is the essence of the fluctuation-dissipation theorem which we’ll now make more precise.

First, the form of the correlation function in (4.32) — with the commutator and funny theta term — isn’t the simplest kind of correlation we could image. The more basic correlation function is simply

S (t) ≡ ⟨O (t)O (0)⟩ ij i j

where we have used time translational invariance to set the time at which O is evaluated to zero. The Fourier transform of this correlation function is

S (ω) = ∫ dt eiωt S (t) (4.34)

ij ij

The content of the fluctuation-dissipation theorem is to relate the dissipative part of the response function to the fluctuations S(ω) in the vacuum state which, at finite temperature, means the canonical ensemble ρ = e−βH.

There is a fairly pedestrian proof of the theorem using spectral decomposition (i.e. inserting a complete basis of energy eigenstates as we did in the previous section). Here we instead give a somewhat slicker proof although, as we will see, it requires us to do something fishy somewhere. We proceed by writing an expression for the dissipative part of the response function using the Kubo formula (4.32),

χ′′(t) = − [χ (t) − χ (−t)]

ij 2 ij ji = − 1/2 θ(t) [⟨O (t)O (0)⟩ − ⟨O (0)O (t)⟩]

i j j i + 1/2 θ(−t) [⟨O (−t)O (0)⟩ − ⟨O (0)O (−t)⟩]

j i i j

By time translational invariance, we know that ⟨O (0)O (t)⟩ = ⟨O (−t)O (0)⟩. This means that the step functions arrange themselves to give θ(t) + θ(−t) = 1, leaving

χ′′(t) = − 1/2 ⟨O (t)O (0)⟩ + 1/2 ⟨O (−t)O (0)⟩ (4.35)

ij i j j i

But we can re-order the operators in the last term. To do this, we need to be sitting in the canonical ensemble, so that the expectation value is computed with respect to the Boltzmann density matrix. We then have

⟨O (−t)O (0)⟩ = Tr e−βH O (−t) O (0)

j i j i = Tr e−βH O (−t) eβH e−βH O (0)

j i = Tr e−βH O (0) O (−t + iβ)

i j = ⟨O (t − iβ) O (0)⟩ i j

The third line above is where we’ve done something slippery: we’ve treated the density matrix ρ = e−βH as a time evolution operator, but one which evolves the operator in the imaginary time direction! In the final line we’ve used time translational invariance, now both in real and imaginary time directions. While this may look dodgy, we can turn it into something more palatable by taking the Fourier transform. The dissipative part of the response function can be written in terms of correlation functions as

χ′′(t) = − 1/2 [⟨O (t)O (0)⟩ − ⟨O (t − iβ) O (0)⟩] (4.36)

ij i j i j

Taking the Fourier transform then gives us our final expression:

χ′′(ω) = − 1/2 (1 − e−βω) S (ω) (4.37)

ij ij

This is the fluctuation-dissipation theorem.

on theorem, relating the fluctuations in frequency space, captured by S(ω), to the dissipation, captured by χ''(ω). Indeed, a similar relationship holds already in classical physics; the most famous example is the Einstein relation that we met in Section 3.1.3.

The physics behind (4.37) is highlighted a little better if we invert the equation. We can write S_{ij}(ω) = -2[n_B(ω)+1]χ''_{ij}(ω)

where n_B(ω) = (e^{βω} - 1)^{-1} is the Bose-Einstein distribution function. Here we see explicitly the two contributions to the fluctuations: the n_B(ω) factor is due to thermal effects; the "+1" can be thought of as due to inherently quantum fluctuations. As usual, the classical limit occurs for high temperatures with βω ≪ 1 where n_B(ω) ≈ k_B T/ω. In this regime, the fluctuation dissipation theorem reduces to its classical counterpart S_{ij}(ω) = -2k_B T/ω χ''_{ij}(ω)

## 4.4 Response in Quantum Field Theory

We end these lectures by describing how response theory can be used to compute some of the transport properties that we’ve encountered in previous sections. To do this, we work with Quantum Field Theory where the operators become functions of space and time, O(⃗x,t). In the context of condensed matter, this is the right framework to describe many-body physics. In the context of particle physics, this is the right framework to describe everything.

Suppose that you take a quantum field theory, place it in a state with a finite amount of stuff (whatever that stuff is) and heat it up. What is the right description of the resulting dynamics? From our earlier discussion, we know the answer: the low-energy excitations of the system are described by hydrodynamics, simply because this is the universal description that applies to everything. (Actually, we’re brushing over something here: the exact form of the hydrodynamics depends on the symmetries of the theory, both broken and unbroken). All that remains is to identify the transport coefficients, such as viscosity and thermal conductivity, that arise in the hydrodynamic equations. But how to do that starting from the quantum field?

The answer to this question lies in the machinery of linear response that we developed above. For a quantum field, we again add source terms to the action, now of the form H_{source}(t) = ∫ d^{d-1}⃗x ϕ_i(⃗x,t) O_i(⃗x,t) (4.38)

The response function χ is again defined to be the change of the expectation values of O in the presence of the source ϕ, δ⟨O_i(⃗x,t)⟩ = ∫ d⃗x' dt' χ_{ij}(⃗x,t;⃗x',t') ϕ_j(⃗x',t') (4.39)

All the properties of the response function that we derived previously also hold in the context of quantum field theory. Indeed, for the most part, the label ⃗x and ⃗x' can be treated in the same way as the label i,j. Going through the steps leading to the Kubo formula (4.32), we now find χ_{ij}(⃗x,⃗x';t-t') = -iθ(t-t')⟨[O_i(⃗x,t), O_j(⃗x',t')]⟩ (4.40)

We learned in our first course on Quantum Field Theory that the two-point functions are Green’s functions. Usually, when thinking about scattering amplitudes, we work with time-ordered (Feynman) correlation functions that are relevant for building perturbation theory. Here, we interested in the retarded correlation functions, characterised by the presence of the step function sitting in front of (4.40).

Finally, if the system exhibits translational invariance in both space and time, then the response function depends only on the differences t-t' and ⃗x-⃗x'. In this situation it is useful to work in momentum and frequency space, so that the (4.39) becomes δ⟨O_i(k,ω)⟩ = χ_{ij}(k,ω) ϕ_j(k,ω) (4.41)

Electrical Conductivity

Consider a quantum field theory with a U(1) global symmetry. By Noether’s theorem, there is an associated conserved current J^μ = (J^0, J^i), obeying ∂_μ J^μ = 0. This current is an example of a composite operator. It couples to a source which is a gauge field A_μ(x), H_{source} = ∫ d^{d-1}⃗x A_μ J^μ (4.42)

Here A is the background gauge field of electromagnetism. However, for the purposes of our discussion, we do not take A to have dynamics of its own. Instead, we treat it as a fixed source, under our control.

There is, however, a slight subtlety. In the presence of the background gauge field, the current itself may be altered so that it depends on A. A simple, well known, example of this occurs for a free, relativistic, complex scalar field φ. The conserved current in the presence of the background field is given by J^μ = ie[φ†∂^μφ - (∂^μφ†)φ] - e^2 A^μ φ†φ (4.43)

where e is the electric charge. With this definition, the Lagrangian can be written in terms of covariant derivatives D_μφ = ∂_μφ - ieA_μφ, L = ∫ d^{d-1}⃗x |∂_μφ|^2 + A_μ J^μ = ∫ d^{d-1}⃗x |D_μφ|^2 (4.44)

For non-relativistic fields (either bosons or fermions), similar A terms arise in the current for the spatial components.

We want to derive the response of the system to a background electric field. Which, in more basic language, means that we want to derive Ohm’s law in our quantum field theory. This is ⟨J_i(k,ω)⟩ = σ_{ij}(k,ω) E_j(k,ω)

(4.45)

Here E is the background electric field in Fourier space and σ is the conductivity tensor. In a system with rotational and parity invariance (which, typically means in the absence of a magnetic field) we have σ = σδ, so that the current is parallel to the applied electric field. Here we will work with the more general case. Our goal is to get an expression for σ in terms of correlation functions in the field theory. Applying (4.41) with the perturbation (4.42), we have δ⟨J ⟩ = ⟨J ⟩−⟨J ⟩ = −i ∫ dt′d3⃗x ⟨[J (⃗x,t),J (⃗x′,t′)]⟩ A (⃗x′,t′) (4.46)

µ µ µ 0 µ ν 0 ν −∞ The subscript 0 here means the quantum average in the state A = 0 before we turn on the background field. Let’s start by looking at the term ⟨J ⟩. You might think that i 0 there are no currents before we turn on the background field. But, in fact, the extra term in (4.43) gives a contribution even if – as we’ll assume – the unperturbed state has no currents. This contribution is ⟨J ⟩ = e2A ⟨φ†φ⟩ = eA ρ i 0 i 0 i where ρ is the background charge density. Notice it is not correct to set A = 0 in this expression; the subscript 0 only means that we are evaluating the expectation value in the A = 0 quantum state.

Let’s now deal with the right-hand side of (4.46). If we work in A = 0 gauge (where things are simplest), the electric field is given by E = −A. In Fourier transform space, i i this becomes E (ω)

A (ω) = (4.47)

iω We can now simply Fourier transform (4.46) to get it in the form of Ohm’s law (4.45).

The conductivity tensor has two contributions: the first from the background charge density; the second from the retarded Green’s function eρ χ (k,ω)

ij σ = − δ + (4.48)

ij ij iω iω with the Fourier transform of the retarded Green’s function given in terms of the current-current correlation function χ ( ⃗ k,ω) = −i ∫ dtd3⃗x θ(t)ei(ωt−⃗k·⃗x)⟨[J (⃗x,t),J (⃗0,0)]⟩ ij i j −∞ This is the Kubo formula for conductivity.

Viscosity We already saw in Section 2 that viscosity is associated to the transport of momentum.

And, just as for electric charge, momentum is conserved. For field theories that are invariant under space and time translations, Noether’s theorem gives rise to four cur- rents, associated to energy and momentum conservation. These are usually packaged together into the stress-energy tensor Tµν, obeying ∂ Tµν = 0. (We already met this object in a slightly different guise in Section 2, where the spatial components appeared as the pressure tensor P and the temporal components as the overall velocity u ).

ij i The computation of viscosity in the framework of quantum field theory is entirely analogous to the computation of electrical conductivity. The electric current is simply replaced by the momentum current. Indeed, as we already saw in Section 2.5.3, the viscosity tells us the ease with which momentum in, say, the x-direction can be trans- ported in the z-direction. For such a set-up, the relevant component of the current is Txz. The analog of the formula for electrical conductivity can be re-interpreted as a formula for viscosity. There are two differences. Firstly, there is no background charge density. Secondly, the viscosity is for a constant force, meaning that we should take the ω → 0 and k → 0 limit of our equation. We have χ ( ⃗ k,ω) = −i ∫ dtd3⃗x θ(t)ei(ωt−⃗k·⃗x)⟨[T (⃗x,t),T (⃗0,0)]⟩ xz,xz xz xz −∞ and χ (0,ω)

xz,xz η = lim ω→0 iω This is the Kubo formula for viscosity.

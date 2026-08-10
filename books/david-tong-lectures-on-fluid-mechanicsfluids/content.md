# David Tong Lectures on Fluid Mechanicsfluids

> 来源文件：pre_David_Tong_Lectures_on_Fluid_Mechanicsfluids.txt
> 字符数（约）：251904
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Fluid Mechanics David Tong Department of Applied Mathematics and Theoretical Physics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 OBA, UK http://www.damtp.cam.ac.uk/user/tong/fluids.html d.tong@damtp.cam.ac.uk

Recommended Books and Resources There are many books on fluid mechanics, ranging from the eminently accessible to the dauntingly comprehensive. Here are a collection that I found useful.

• Van Dyke, An Album of Fluid Motion If you’re going to look at one book on fluid mechanics then it should be this one. It’s a book of pictures, many of them very pretty. While this likely sounds lightweight, in this case a picture really does paint 20 equations and helps build intuition for fluid flow. It’s difficult to buy at a reasonable price (at the time of writing, Amazon offer a paperback version for £833.82) but you can find versions on the internet.

• Acheson, Elementary Fluid Dynamics • Childress, An Introduction to Theoretical Fluid Mechanics If you’re going to look at a second book on fluid dynamics, it should probably be one of these, or something similar. Both are aimed at the beginner. They are clear and easygoing. I have a slight preference for Acheson which focuses more on the physics.

• George Batchelor, An Introduction to Fluid Dynamics This is considered the bible of fluid mechanics by many practitioners. It’s not particularly cuddly, but the explanations are clear enough and it is certainly comprehensive (unless you care about turbulence).

• Landau and Lifshitz, Fluid Mechanics An astonishing amount of physics is packed into this book, but it’s not the easiest read. Like Batchelor, it puts thermodynamics front and centre which is useful in making contact with other areas of physics which can otherwise feel hidden. (In these lectures, we only bring thermodynamics into the game when we describe sound waves.)

• Drazin and Reid, Hydrodynamic Stability For all your instability needs.

• Frisch, Turbulence A look at symmetries and scaling in turbulent flow.

Contents 1 Introduction 3

## 1.1 The Basics

1.1.1 Path Lines and Streamlines 6 1.1.2 The Material Time Derivative 8 1.1.3 Conservation of Mass 9 1.1.4 The Stream Function 10 2 Inviscid Flows 12

## 2.1 The Euler Equation

2.1.1 Under Pressure 13 2.1.2 The Euler Equation is Just Momentum Conservation 16 2.1.3 Archimedes’ Principle 17 2.1.4 Energy Conservation and Bernoulli’s Principle 18

## 2.2 Vorticity

2.2.1 The Vorticity Equation 26 2.2.2 Kelvin’s Circulation Theorem 29

## 2.3 Potential Flows in 3d

2.3.1 Boundary Conditions 33 2.3.2 Flow Around a Sphere 34 2.3.3 D’Alembert’s Paradox 38 2.3.4 A Bubble Rising 39

## 2.4 Potential Flows in 2d

2.4.1 Circulation Around a Cylinder 43 2.4.2 Lift and the Magnus Force 45

## 2.5 A Variational Principle

2.5.1 The Principle of Least Action 47 2.5.2 An Action Principle for Fluids 50 3 The Navier-Stokes Equation 55

## 3.1 Stress, Strain and Viscosity

3.1.1 Newtonian Fluids 60 3.1.2 Momentum and Energy Conservation Revisited 62

## 3.2 Some Simple Viscous Flows

3.2.1 The No-Slip Boundary Condition 64 3.2.2 Couette Flow 65 3.2.3 Poiseuille Flow 68 3.2.4 Vorticity Revisited and the Burgers Vortex 69

## 3.3 Dimensional Analysis

3.3.1 The Reynolds Number 73 3.3.2 Scaling 75

## 3.4 Stokes Flow

3.4.1 Flow Around a Sphere 78 3.4.2 Uniqueness and the Minimum Dissipation Theorem 83 3.4.3 Eddies in the Corner 85 3.4.4 Hele-Shaw Flow 89 3.4.5 Swimming at Low Reynolds Number 90

## 3.5 The Boundary Layer

3.5.1 Prandtl’s Boundary Layer Equation 96 3.5.2 An Infinite Flat Plate 98 3.5.3 Boundary Layers with Pressure Gradients 101 3.5.4 Separation 105 4 Waves 111

## 4.1 Surface Waves

4.1.1 Free Boundary Conditions 112 4.1.2 The Equations for Surface Waves 113 4.1.3 Surface Tension 121

## 4.2 Internal Gravity Waves

## 4.3 Because the Earth Spins

4.3.1 The Shallow Water Approximation 127 4.3.2 Geostrophic Balance and Poincar´e Waves 129 4.3.3 We Need to Talk About Kelvin Waves 133 4.3.4 Rossby Waves 135 4.3.5 Equatorial Waves 136 4.3.6 Chiral Waves are Topologically Protected 140

## 4.4 Sound Waves

4.4.1 Compressible Fluids and the Equation of State 144 4.4.2 Some Thermodynamics 146 4.4.3 Briefly, Heat Transport 149 4.4.4 The Equations for Sound Waves 150 4.4.5 Viscosity and Damping 154

## 4.5 Non-Linear Sound Waves

4.5.1 The Method of Characteristics 159 4.5.2 Soundcones 161 4.5.3 Wave Steepening and a Hint of Shock 164 4.5.4 Burgers’ Equation 167

## 4.6 Shocks

4.6.1 Jump Conditions 171 4.6.2 Shocks Start Supersonic 176 4.6.3 On Singularities and Physics 178 5 Instabilities 181

## 5.1 Kelvin-Helmholtz Instability

5.1.1 The Simplest Instability 185 5.1.2 Rolling Up The Vortex Sheet 187 5.1.3 Gravity Helps. Surface Tension Helps Too. 189 5.1.4 The Rayleigh-Taylor Instability 190

## 5.2 A Piece of Piss

5.2.1 Gravity Makes the Flow Thinner 195

## 5.3 Rayleigh-B´enard Convection

5.3.1 The Boussinesq Approximation 198 5.3.2 Perturbation Analysis 201

## 5.4 Instabilities of Inviscid Shear Flows

5.4.1 Rayleigh’s Criterion 207 5.4.2 Fjortoft’s Criterion 209 5.4.3 Howard’s Semi-circle Theorem 211 5.4.4 Couette Flow Revisited 213

## 5.5 Instabilities of Viscous Shear Flows

5.5.1 Poiseuille Flow Revisited 217 6 Turbulence 219

## 6.1 Mean Flow

6.1.1 The Reynolds Averaged Navier-Stokes Equation 221

## 6.2 Some Dimensional Analysis

6.2.1 Scale Invariance 227

## 6.3 Velocity Correlations

6.3.1 Navier-Stokes for Correlation Functions 233 6.3.2 The Structure of the Three-Point Function 236 6.3.3 The von Ka´rm´an-Howarth Equation 238 6.3.4 Kolmogorov’s 4/5 240

Acknowledgements I’m no expert on fluid mechanics. I wrote these notes primarily to teach myself the basics of the subject and I hope that others may find them useful. If, however, you would prefer to learn from someone who actually knows what they’re talking about then I put together a collection of resources that I found helpful on this webpage.

My thanks to Matt Davison, Mihalis Dafermos, Sean Hartnoll and Jorge Santos for helpful discussions on some of the topics included in these notes. I am supported by a Simons Investigator award.

1 Introduction Take anything in the universe, throw a bunch of it in a box, and turn up the heat. Then it doesn’t matter what you started with, the motion of this substance will be governed by the equations of fluid dynamics.

This is a remarkable statement. There are lots of different things in the universe and we go to great lengths to understand their properties. Yet if you heat them, most of the differences disappear. When things get hot, everything looks the same.

Here are some examples. Take any element in the periodic table and heat it until it melts, so that it is either a liquid or a gas. The motion of every element is governed by the same set of equations. The only reminder of what you started with is to be found in a handful of parameters of these equations which describe, among other things, the density and viscosity of the fluid. These will differ from element to element. But the basic set of equations are the same, regardless of whether you started with an alkaline earth metal or an inert gas.

This same story holds if we turn our attention to more exotic substances. For example, inside every proton and neutron sit three quarks. They have been trapped there since the Big Bang, held in place by the grip of the strong nuclear force. However, earlier this century, experimenters succeeded in colliding nuclei together with energies that were so high that the protons and neutrons themselves melted, freeing their imprisoned quarks and forming a novel state of matter known as a quark-gluon plasma. This plasma only lasts for a fraction of a second before it cools and once again forms protons and neutrons. But during that fraction of a second it moves. And the movement is described by the laws of fluid mechanics.

Here is an even more extreme example. Take spacetime itself. It is possible for spacetime to collapse in on itself to form a black hole and, due to the work of Hawking, we know that these black holes are hot objects. So a black hole can be viewed as a way to heat spacetime. Surprisingly, if you look at the equations that govern the event horizon of a black hole, you will once again find the laws of fluid mechanics.

All of which is to say that there is a wonderful universality to the laws that govern fluids. In certain circumstances, these laws describe literally everything. And this makes them interesting.

The reasons underlying this universality are well understood. At the microscopic level, fluids are ridiculously complicated objects, consisting of, say, 1023 atoms, each following its own path, while acting through various forces on the atoms around it. But much of this motion is fleeting and we lose little if we ignore it. Instead, we care only about patterns in the collective motion of the atoms that survive over long time scales. It turns out that these long-lived modes are all related to familiar conservation laws – conservation of mass, momentum and energy – and these conservation laws are universal and obeyed by all substances. This, ultimately, is why all fluids look the same: the equations of fluid dynamics are essentially the equations that govern how conserved quantities evolve in time. (This is a theme that will rear its head at various places in this course, but is not something that we dwell upon. In contrast, the idea that conservation laws underlie fluid mechanics will be the focal point of the lectures on Kinetic Theory which derive the Navier-Stokes equation starting from 1023 atoms, each obeying Newton’s laws.)

In addition to the universal aspect of fluid mechanics, the subject also has enormous practical applications. It explains, for example, why planes fly. (As we will recount later in these lectures, one of the more embarrassing episodes in the history of theoretical physics occurred in 1903 when the Wright brothers took to the air before physicists were able to ade adequately explain either lift or drag!) Fluid mechanics explains how oil flows through pipes and how the motion of the atmosphere manifests itself in the climate, and how many decades of focussing on the former has resulted in an urgent and desperate need to better understand the latter.

In this course we explore the basics of fluid mechanics. Our focus will not be on quarks and black holes, but nor will it be any particular application of fluid mechanics. Instead our goal is simply to understand the different things that fluids can do. Fluids are everywhere and they have a tendency to move. The purpose of these lectures is simply to construct and explore the equation governing this motion.

As we’ve stressed above, the motion of all fluids is described by the same basic set of equations. Prominent among these is the Navier-Stokes equation, accompanied by one or two of further equations describing the conservation of mass and, in some cases, the flow of heat. One of the themes of fluid mechanics is that a wonderful diversity of different behaviour emerges from these equations. As these lectures progress, we will find ourselves falling into a routine. Like Monet and his haystacks, we will return to the same theme over and over again, not because we did anything wrong the first time but because there is always something new to see. Attacking the same set of equations, but with slight change to the boundary condition, or a novel approximation scheme, will often yield something new and surprising. One of the delights of the subject lies in finding such riches sitting inside such simple equations.

## 1.1 The Basics

When we were kids, we are told that there are three phases of matter: solid, liquid and gas. As we grow older, we learn that this is a hopelessly naive view of the world. Nonetheless, it is the one that we will adopt in this course which is concerned only with the latter two. Liquids and gases are both examples of fluids. Roughly speaking, a fluid is a substance that flows when pushed. More rigorously, fluids are objects that are well described by the equations of these lectures.

The subject of fluid mechanics starts with a lie. (Applied mathematicians prefer the term "approximation".) The lie, sometimes dubbed the continuum hypothesis, is that fluids are indivisible continuous objects. The fluid can be then described by two smooth, continuous fields, • The density ρ(x,t) • The velocity u(x,t). Of course, we know that in reality fluids are made of molecules and this approximation must break down on atomic scales. But we also know from experience that if we look on suitably large scales, where we are coarse graining over a many many molecules, then the continuum description is remarkably good.

It is appropriate to start these lectures by stressing that we are dealing with an approximation. It will not be our last. The study of fluids is all about the art of approximation. The equations of fluid mechanics, simple as they are, cannot be solved in full generality and we will make progress only by simplifying. The skill is in learning what to keep and what to ignore. And we start by ignoring the existence of atoms.

It’s not just the discreteness of matter that is swept under the rug in the continuous description. We also ignore the vast majority of the motion of the constituent atoms and molecules that make up the fluid. At room temperature, these constituents are flying around at speeds of 100 ms−1 or so. (This is certainly true of gases. For liquids, the molecules are more closely bound to their neighbours and we have to think more carefully about what the velocity of a single molecule really means.) But most of this underlying atomic motion is neglected in our coarse-grained description. Instead, the velocity field u(x,t) describes the average, macroscopic motion of the fluid. In particular, there is a state of the fluid in which u(x,t) = 0 and we pretend that the fluid is completely still, even though the underlying particles are still flying around, just with no direction preferred over any other.

(As an aside: the internal motion of the constituents doesn’t show up in the velocity field u(x,t), but it does manifest itself in the temperature of the fluid which is another field T(x,t). We’ll elaborate on the role that temperature plays as these lectures progress but for now, and indeed for much of the lectures, we will be able to ignore it.) It is also worth elaborating on how to think about the position x that appears in the argument of the fields ρ(x,t) and u(x,t). This is some fixed position in space. This means, in particular, that u(x,t) is the velocity that would be measured by some fixed array of sensors embedded in the fluid, as opposed to sensors that drift along with the fluid. The use of fields ρ(x,t) and u(x,t) is called the Eulerian description.

We will also have use for a slightly different viewpoint, in which we think of individual “parcels of fluid”, each initially sitting at some position x and then following the flow by travelling at speed u(x,t). It’s not so easy to define what we mean by these “parcels of fluid” given that the underlying atoms are, as we described above, wandering off in all sorts of directions, often at high speed, with only the most scant regard for the velocity field u(x,t). But the concept of a fluid parcel that keeps its identity as the fluid moves is an extremely useful pretence. We will sometimes talk about a “particle” of fluid and we have in mind these parcels rather than the underlying atoms. The perspective in which we follow the trajectories of these parcels, and study the forces that act on them as if they were particles in classical mechanics, is called the Lagrangian description.

Throughout these lectures, all our equations will be written in the Eulerian description, using the velocity field u(x,t), but some intuition will come from a more Lagrangian way of thinking. Moreover, we will certainly have a need to understand the trajectories of particles that are embedded within the fluid. Indeed, we kick off with some simple observations.

1.1.1 Path Lines and Streamlines There are a number of ways to visualise the flow u(x,t) of a fluid. Here are the two most useful: • A pathline is the trajectory followed by a particle embedded within the fluid. • A streamline is a tangent to u(x,t) at every point x for fixed time t. In general, the tangents to a vector field F(x) are said to be integral curves for F. So the streamlines are integral curves for the velocity field at a fixed time.

If the flow is steady, meaning that ∂u/∂t = 0, then the pathlines and streamlines coincide. But, for time dependent flows, they differ. To see this, let’s drape some equations around the definitions above.

Figure 1. The pathlines for particles in the flow u = (yt,1) are shown on the left. These are a history of the flow. The middle and right hand figures show streamlines, with the right-hand figure at a later time.

First consider the pathline. A particle within the fluid will follow some trajectory x(t). At any time t, the velocity of this particle is given by the velocity field u evaluated at the position of the particle, meaning dx/dt (t) = u(x(t),t) (1.1). Given some initial starting point x(t = 0) = x₀, we can solve this equation to find the pathline.

In contrast, a streamline is a trajectory x(s) such that the tangents of x(s) coincide with the velocity field at a fixed time t, dx/ds (s) = u(x(s),t). In words, the streamline is a snapshot of the flow at some fixed time, while the pathline tells us about the actual history of the particle.

An Example Consider the two-dimensional flow given by u(x,t) = (αyt, β) for some fixed coefficients α and β. The pathline obeys dx/dt = αyt and dy/dt = β. The y component is solved by y = y₀ + βt, while the equation for the x component becomes ẋ = αyt = α(y₀ t + βt²), which gives x = x₀ + 1/2 α y₀ t² + 1/3 αβ t³. To get the pathline, we eliminate t to get the family of curves in the (x,y) plane x = x₀ + α/(2β²) (y − y₀)² + α/(3β²) (y − y₀)³. These are plotted on the left-hand plot of Figure 1 for various values of the starting point (x₀,y₀).

In contrast, to find the streamlines we instead solve dx/ds = αyt and dy/ds = β where the prime means d/ds. These now have the solutions y = y₀ + βs and x = x₀ + αy₀ t s + 1/2 αβ t s² where t is now some fixed parameter. These are shown in the middle and right-hand plots of Figures 1 for t > 0. Note that the pathlines and streamlines are not similar in this example: the former is a cubic curve, the latter a parabola. (Or, in the special case of t = 0, straight lines.) Moreover, the streamlines are time-dependent: the right-hand figure is a snapshot of the flow at a later time than the middle figure.

1.1.2 The Material Time Derivative As we stressed above, the density ρ(x,t) and velocity field u(x,t) are measured in the Eulerian sense at some fixed point x. But this leaves us with the question: how do we see things change in time if we’re drifting along with the fluid?

Specifically, suppose that there is some field ϕ(x,t) that we would like to measure. This might be the density of the fluid itself, or something else. The explicit time dependence in ϕ(x,t) tells us how this quantity changes with time if we’re sitting at some fixed position x. But if we’re drifting with the fluid, then we follow a pathline x(t) defined by (1.1). The value of field along this trajectory is given by ϕ(x(t),t) and the total time derivative is d/dt ϕ(x(t),t) = ∂ϕ/∂t + ẋ · ∇ϕ = ∂ϕ/∂t + u · ∇ϕ. The additional u · ∇ϕ term captures the change in ϕ because of the way we’re swept along by the fluid. The transport of some object as it’s carried along by a fluid is known as advection and, correspondingly, u · ∇ϕ is called the advective rate of change. This idea of a total time derivative will be important, so much so that we introduce some new notation for it (even though we already We have perfectly good notation in dϕ/dt!). We write Dϕ ∂ϕ = +u·∇ϕ Dt ∂t and call this the material derivative. It can be thought of as a bridge between the Eulerian description in terms of a fixed point x and the Lagrangian description which moves with the fluid.

1.1.3 Conservation of Mass

Our first equation of fluid mechanics is the simplest: it captures the fact that mass is conserved. Moreover, like all conservation laws in physics, mass is conserved locally. This means that if the mass of the fluid decreases at some point in space then it must have moved to a neighbouring point.

This fact is captured by the conservation equation, relating the density ρ and the velocity u, ∂ρ +∇·(ρu) = 0 (1.2)

∂t Equations of this kind are commonplace in physics because they appear whenever we have a conservation law. In particular, an identical equation appears in Electromagnetism where, in that context, ρ is the electric charge density and J = ρu is the electric current density. For us, ρ is the mass density and ρu is the mass flux density.

To see why (1.2) captures the conservation of mass, consider the mass M of fluid in some fixed region V, (cid:90)

M = ρ dV The change of this mass is given by (cid:90) (cid:90) (cid:90)

dM ∂ρ = dV = − ∇·(ρu) dV = − ρu·dS dt ∂t V V S where we have used the divergence theorem and S = ∂V is the boundary of the region V. This tells us that if there is no net flow of mass flux through the boundary S then the total mass M inside the region V remains constant. In other words, mass is conserved.

We can also write the mass conservation equation (1.2) using our new material derivative notation. It becomes Dρ +ρ∇·u = 0 (1.3)

Dt

Incompressible Fluids

Throughout much of these lectures notes we will make one further approximation: we will assume that fluids are incompressible, meaning that ρ(x,t) is a constant. In this case, ρ˙ = ∇ρ = 0 and the continuity equation (1.2) becomes simply ∇·u = 0 (1.4)

In the language of our Vector Calculus lectures, we say that the fluid flow is solenoidal or divergence free. The vast majority of these lectures will be devoted to finding the wonderfully diverse solutions to the equation (1.4).

In the fact, the requirement that ρ˙ = ∇ρ = 0 can be loosened slightly. We see from (1.3) that we only really require Dρ/Dt = 0 for the incompressible condition (1.4) to be enforced. This means that any individual parcel of fluid should not change its density as it’s swept along, but different parts of the larger fluid may have different densities. Such a situation is said to be stratified and arises, for example, in the ocean where the water is more dense at the bottom than the top. We’ll meet situations like these when we discuss some aspects of waves in Section 4.

The assumption that fluid flow is incompressible is not totally innocent. In fact, the phenomenon of fluids compressing and expanding as their density changes is so common that we give it a special name. This name is “sound”! It turns out that that assumption of incompressibility is good when the speed of the fluid |u| is much less than the speed of sound. For air at atmospheric pressure, the speed of sound is 340 ms−1; for water at room (or ocean) temperature it is around 1500 ms−1. For much of these lectures, we will restrict ourselves to flows much below these speeds and assume that ∇·u = 0. But, in Section 4.4, we will discuss the propagation of sound waves and then we will be forced to look more closely at the equations that govern compressible fluids.

1.1.4 The Stream Function

For incompressible fluids, satisfying ∇·u = 0, we can write the velocity field as u = ∇×A For many fluid flows, this isn’t particularly helpful since we have just swapped one vector field u for another A. However, when the flow is two-dimensional (in some sense) this provides a very useful simplification because it means that we get to exchange the vector field u for a scalar field Ψ called the stream function.

For example, suppose that the flow is independent of the z-direction, so that the velocity field takes the form u = (u (x,y,t),u (x,y,t),0)

1 2 Then the vector potential A can be written as ∂Ψ ∂Ψ A = (0,0,Ψ(x,y,t)) ⇒ u = and u = − 1 2 ∂y ∂x and the degrees of freedom are captured by the stream function Ψ(x,y,t). It has the nice property that lines of constant Ψ are streamlines of the flow. To see this, note that lines of constant Ψ have a and so take the integral form ∫ Other Forces = f dV The pressure acts on the surface of the volume V but we can massage it into a volume-type force through use of the divergence theorem. This gives ∫ ρ (Du/Dt) dV = ∫ (−∇P + f) dV over V 1 I am apparently alone in the world in thinking that the lower case p for pressure looks way too much like the density ρ for them to happily cohabit in the same equation.

The final step is to recall that this whole derivation holds for an arbitrary volume V within the fluid. Since it holds for all such V, the integrand itself must vanish. So we’re left with the differential equation of motion for the fluid ρ Du/Dt = −∇P + f (2.6)

This is the Euler equation. Finding solutions to this simple equation will occupy us for the rest of this section although we will, ultimately, replace it in Section 3 by the Navier-Stokes equation which includes the effects of viscosity. Fluids that obey the Euler equation are said to be ideal.

Importantly, the Euler equation is non-linear in the velocity field, although this is somewhat hidden in the notation above since the non-linearity sits in the material derivative: Du/Dt = ∂u/∂t + (u·∇)u.

Note that a constant pressure P throughout the fluid does nothing. This is because the pressure is isotropic: if one piece of fluid pushes on a neighbour, the neighbour pushes back with equal force. Interesting dynamics only arises when we have pressure differences across the fluid, as captured by ∇P.

The Euler equation is a vector equation. Combined with the requirement of incompressibility, ∇·u = 0, we have four equations in total. We will use these to solve for the four dynamical variables: P and u.

Looking Forwards: the Equation of State If you know one thing about gases, then it will be the ideal gas law. This relates the pressure P, volume V and temperature T of a gas by PV = Nk T where N is the number of molecules in the gas and k a universal constant of nature called Boltzmann’s constant that relates energy to temperature. (For what it’s worth, k ≈ 1.4 × 10−23 JK−1.) For our purposes, it’s more useful to think of the ideal gas law in terms of the density ρ = Nm/V rather than volume, where m is the mass of the constituent molecule, P = k ρT The ideal gas law is an example of an equation of state. It holds for strictly non-interacting gases. If we take into account interactions, either in gases or in liquids, it will be replaced by some other equation of state that again relates pressure P, density ρ and temperature T. (You can learn more about how to calculate the equation of state from first principles in the lectures on Statistical Physics.)

When we first meet the ideal gas law, we think of P, ρ and T as constants that characterise the whole system. But it also holds if they are promoted to the kind of local fields P(x,t), ρ(x,t) and T(x,t) that we work with in these lectures. For incompressible fluids, with ρ constant, the equation of state tells us that the temperature T(x,t) simply tracks the pressure P(x,t). For this reason we won’t need to consider it separately.

Things are more interesting if we have compressible fluids, in which ρ(x,t) is another dynamical variable. In this case the mass conservation equation (1.2) and Euler equation aren’t enough information to tell us what happens and we need another equation. It turns out that in this situation the right way forward is to use the equation of state to replace ρ(x,t) with the temperature field T(x,t) and then write down a separate equation for how heat flows in the system. (Roughly speaking, it is a version of the heat equation, with the material derivative replacing the usual time derivative.) We’ll explain this further in Section 4.4 when we discuss sound waves and we will be forced to think more carefully about the thermodynamics of fluids. (A fuller derivation can be found in the lectures on Kinetic Theory.)

2.1.2 The Euler Equation is Just Momentum Conservation Suppose that there is no external force on our fluid, so f = 0. Then the Euler equation can be written in the characteristic form of a conservation law ρ ∂u/∂t + ρ(u·∇)u + ∇P = 0 ⇒ ∂(ρ u)/∂t + ∂(ρ u u + Pδ)/∂x_j = 0 (2.7)

where we’ve used the assumption that the fluid is incompressible, both in taking ρ inside the derivatives and in using ∂_j u_j = 0.

It’s clear what is conserved here: it is simply the momentum in each of the three directions: ∫ ρ u_i dV. Associated to each conserved quantity is a current. The novelty here is that because the conserved quantity is itself a vector, the associated current is a tensor Π_{ij}. This tells us how the momentum in the ith direction is transported in the jth direction. The form of the momentum current can be read off from the equation above, Π_{ij} = ρ u_i u_j + P δ_{ij} The first, advective contribution describes the momentum due to the motion of the fluid. The pressure contribution to momentum is perhaps more surprising. It is a hint, even at this macroscopic level, that pressure is associated to something moving around. This something is, of course, the constituent atoms of molecules of the fluid that we have declared irrelevant for fluid mechanics.

There is a simple way of seeing why pressure is related to momentum. Take a box with some fluid inside and make a little hole in it. The pressure inside the box will force the fluid out of the hole. The rate at which momentum escapes from the box is equal to the pressure. (Or, more strictly, the pressure difference between the inside and outside of the box.)

2.1.3 Archimedes’ Principle Before exploring the full content of the Euler equation, we can extract some familiar and long-known results. To kick off, suppose that the fluid sits in a gravitational field. (Which, let’s face it, most do.) This means that we have an external force density f = ρg where g = −g ẑ is the gravitational acceleration and points downwards.

We can now look for the trivial solution to the Euler equation (2.6) in which the fluid is at rest, so u = 0. We see that the fluid must have a pressure gradient to counteract the gravitational field ∇P = ρg ⇒ P = P_0 − ρgz (2.8)

This is known as hydrostatic pressure. It is the pressure that pushes against the weight of the fluid above. (If you’re worried about the minus sign and the possibility of the pressure becoming negative, think of the surface of the fluid as sitting at z = 0, so that pressure only increases as we move down to z < 0.)

Suppose that we have some object partially immersed in a fluid as shown in the figure. We’ll set P = P_0 at z = 0 to be atmospheric pressure. Then we can ask: what is the force that the fluid exerts on the body? This is simply F = − ∫ P(z) dS where the minus sign is because dS is taken to have outward-pointing normal as shown in the figure, and the integral should be taken over the surface of the object that is immersed in the fluid. We can use the divergence theorem, together with our expression for the hydrostatic pressure (2.8) to write this as F = − ∫ ∇P dV = − ∫ ρg dV where the integral is now over the volume of displaced fluid. This is telling us that the force exerted by the fluid on the object is equal to the weight of the displaced fluid. Eureka! This, of course, is Archimedes principle. In equilibrium, the force F must balance the weight of the object itself. This can be achieved if the object is less dense than water, in which case it floats. Otherwise it sinks. This discussion hasn’t brought anything new to Archimedes idea. It’s really just the old argument wrapped in the language of vector calculus.

The results above also give us a reason to ignore gravity for much of this course. In the presence of a gravitational field, the pressure simply adapts as in (2.8) to cancel it. Therefore, in the presence of gravity, we can think of the pressure as P = P_0 − ρgz + P′ and Euler’s equation becomes ρ Du/Dt = −∇P′ and we proceed from there.

2.1.4 Energy Conservation and Bernoulli’s Principle In classical mechanics, it’s often useful to identify conserved quantities. The same is true in fluid mechanics and there is a way to rewrite the Euler equation that highlights one such conserved quantity. We start with the vector identity u × (∇ × u) = ∇(u·u) − (u·∇)u We use this to substitute for the non-linear (u·∇)u term in the Euler equation to get ρ [∂u/∂t + ∇(½|u|²) − u × (∇ × u)] = −∇P + f (2.9)

So far this doesn’t look any more useful. But now we dot with u to make the curly term disappear. We have ρ u·∂u/∂t + u·∇(½ρ|u|² + P) = u·f At this stage, we make one further assumption: we take the force to be conservative, meaning that we can write it in terms of a potential energy Φ(x,t), f = −∇Φ (2.10)

For example, the gravitational force can be written in this way. We then have ½ρ ∂|u|²/∂t + u·∇(½ρ|u|² + P + Φ) = 0 This is again of the form of a conservation equation. To see this, we again pull the u inside the ∇ using the fact that the fluid is incompressible so ∇·u = 0. (This is the same step that we did for the momentum conservation equation in (2.7).) We get the final form ½ρ ∂|u|²/∂t + ∇·(u H) = 0 (2.11)

where H = ½ρ|u|² + P + Φ (2.12)

There’s no mystery in what is being conserved here: the time derivative is acting on ½ρ|u|² which we recognise as the kinetic energy density of the fluid. The equation (2.11) is simply capturing energy conservation of the continuous fluid, with u H the energy flux.

For a steady fluid, satisfying ∂u/∂t = 0, we have u·∇H = 0 (2.13)

This is Bernoulli’s Theorem. It states that the quantity H is constant along streamlines. Roughly speaking, the fluid flows quickly in places where the pressure is low, and more slowly when the pressure builds.

An Example: Drinking from a Firehose Consider water flowing down a pipe which, at some point, narrows as shown in Figure 2. This might, for example, be the nozzle on a firehose. We’ll take the narrowing to be gradual so that the streamlines are smooth and follow the pipe.

narrows, the velocity must increase and Bernoulli’s theorem tells us that, for steady flows, the pressure also increases. Initially, the pipe has area A and the fluid has speed U. By the end the area has reduced to a < A and the speed to u. For incompressible fluids, the speed is dictated by the conservation of mass which tells us that the volume of fluid passing through any given slice of the pipe must remain the same, so UA = ua This immediately tells us that the speed of the flow in the narrow section is faster than in the initial section: u = UA/a. Meanwhile, Bernoulli’s theorem tells us that ρ U²/2 + P = u²/2 + p where P and p are the initial and final pressure respectively and we are ignoring any external forces. Rearranging, we have p = P + U²/2 (1 – A²/a²)

We see that because A > a, the pressure actually decreases as the pipe narrows. This makes sense: the decrease in pressure in the narrow section means that there is a pressure difference and this is precisely what causes the fluid to accelerate from speed U to speed u.

More Qualitative Applications There are other situations where Bernoulli’s principle gives us some useful intuition. For example, it’s possible to levitate a ping pong ball on a fast jet of air. You can achieve this by blowing through a straw or by using a hairdryer. The question is: why is the ball stable? Why doesn’t it fall off to one side? In this situation, the airflow is turbulent and it’s not entirely clear that Bernoulli’s principle, which requires a steady flow, can be invoked. Nonetheless, it does provide an answer. Suppose that the ball did move slightly off to one side and out of the main flow. Then the air will be moving faster in the middle of the flow, resulting in a lower pressure and the ball gets pushed back into the middle.

The most famous application of Bernoulli’s principle is to explain the lift experienced by an aerofoil. The air travels faster over the top of the wing than the bottom and the pressure difference results in a net upwards force. But this begs the question: why does the air travel faster over the top of the wing? One popular explanation (and one that I was told in school) is that the flow must reach the trailing edge of the wing at the same time, regardless of whether it goes up or down. But that doesn’t sound right! There’s no principle in physics that says you must reach your goal at the same time regardless of the path you take. (If there were, we wouldn’t need maps.) We will revisit this later in the course when we study flows around objects in some detail.

## 2.2 Vorticity

To characterise the shape of a velocity field u, we look at its derivatives. In general there are nine such derivatives, ∂u_i/∂x_j, with i,j = 1,2,3. But, for incompressible flows, we know that one linear combination vanishes: ∇·u = 0. The remaining derivatives can be decomposed as a symmetric and anti-symmetric tensor. The symmetric one is known as the rate of strain tensor, E_ij = 1/2 (∂u_i/∂x_j + ∂u_j/∂x_i) (2.14)

The anti-symmetric tensor is Ω_ij = 1/2 (∂u_i/∂x_j – ∂u_j/∂x_i)

It contains the same information as vector field, ω_i = –ε_ijk Ω_jk, which is more familiarly written as ω = ∇×u This is the vorticity. It tells us how the fluid swirls at each point in space. The integral curves associated to ω (i.e. the lines that are tangent to ω at each point x) are called vortex lines. Because ω = ∇×u, the vortex lines are perpendicular to streamlines.

Examples of Flows To get a feel for what the vorticity ω and rate of strain E are telling us, we can look at a couple of examples.

First consider the 2d flow u = α(–x, y, 0)

with α a constant. This is plotted on the left of Figure 3. The velocity field has ∇·u = 0 and also ω = 0, while the rate of strain tensor is E = α ( –1 0 0; 0 +1 0; 0 0 0 )

From the figure, you can see that the fluid is squeezed in one direction (the x-direction in this case) and stretched in the other (the y-direction). This is the characteristic feature of flows with a rate of strain. To see this, note that the rate of strain tensor is symmetric and so can always be diagonalised so that it takes the form E = ( E1 0 0; 0 E2 0; 0 0 E3 )

But, for incompressible fluids with ∇ · u = 0, we must have E1 + E2 + E3 = 0. So one eigenvalue is necessarily positive and another necessarily negative. These are the directions in which the flow is, respectively, stretched and squeezed.

Next consider the flow u = α(–y, x, 0) (2.15)

This has ∇·u = E = 0 and a constant vorticity everywhere in the fluid, ω = (0,0,2α). It is depicted on the right of Figure 3. Unsurprisingly, it exhibits a rotation. However, one should be wary of simply eyeballing a flow to decide on vorticity. To illustrate this, consider the example u = f(r)(–y, x, 0)

where f(r) is any function of r² = x² + y². (Note that we’re keeping the flow essentially two dimensional.) This is a generalisation of our previous flow (2.15) and the streamlines look identical for any choice f(r). The vorticity is ω = (0,0,ω(r)), with ω(r) = 1/r d/dr (r² f) (2.16)

Now the vorticity ω(r) varies in the radial direction. This means that if we take the specific choice of f = 1/r², then the vorticity vanishes, ω = 0, even though the flow is clearly rotating around the origin. This is because a non-zero vorticity ω(x) ≠ 0 at some point x means that the fluid is rotating locally around x, not just around the origin.

To build a more physical understanding for what vorticity means, suppose that we drop some propellers in the fluid, like those plastic windspinners that you can buy at the seaside. If you drop them in the fluid, they will move around the origin with the flow. But if the fluid has a vorticity then their orientation will also rotate as the move, as shown on the left-hand side of Figure 4. If the fluid has no vorticity, as is the case for f = 1/r², then they will remain in the same orientation as they move around, as shown in the right-hand figure.

In fact, things are a little more subtle than this. The specific choice u = (–y/r², x/r², 0) has the property that the integral of the velocity field around any circle C that surrounds the origin always gives ∮ u·dx = 2π This is because the velocity field drops off as 1/r, while the perimeter of the circle grows as r. But, by Stokes’ theorem, we have ∮ u·dx = ∫∫_S ω · dS = 2π where S is a surface with boundary ∂S = C. So it can’t quite be true that the vorticity ω vanishes everywhere! Indeed, the flow is singular at the origin x = y = 0 (which, in three dimensions, means that it is singular along the entire z-axis.) For the above calculation to be consistent, the vorticity must be non-zero along this axis, with ω = 2π δ²(r) ẑ This is sufficient for the flow to have rotation around the origin, even though it doesn’t have vorticity at any other point. This slightly subtle example will arise in some later applications. In fact, it’s not a bad approximation for what happens when you empty the bath, with the (admittedly finite size) plughole taking the place of r = 0.

The Biot-Savart Law We can invert the equation ω = ∇×u to get an expression for the velocity in terms of the vorticity. In fact, this is a calculation that we’ve done elsewhere and it’s worth taking the opportunity to remind ourselves of this.

In Electromagnetism, the magnetic field obeys ∇·B = 0 which means that it can be written in terms of a vector potential B = ∇×A. In the case of magnetostatics, the magnetic field is given by Ampère’s law ∇×B = μ₀ J ⇒ ∇²A = –μ₀ J with J the current density. This is just the Poisson equation for each component of A and can be solved using the Green’s function, A(x) = μ₀/(4π) ∫ d³x′ J(x′)/|x–x′| If we subsequently take the curl of this equation, then we get an expression for the magnetic field B in terms of the current density B(x) = μ₀/(4π) ∫ d³x′ J(x′)×(x–x′)/|x–x′|³ (2.17)

This is the Biot-Savart law.

But we can now repeat each of these steps for the fluid velocity. If the fluid is incompressible, so ∇ · u = 0, then we can introduce a vector potential A such that u = ∇ × A. This way of writing the velocity is at the heart of the idea of a stream function, as we saw in Section 1.1.4. The curl of the velocity is the vorticity, so we have ∇×u = ω ⇒ ∇²A = –ω Following the same steps that we took above, the vector potential can then be expressed as A(x,t) = 1/(4π) ∫ d³x′ ω(x′,t)/|x–x′| Again taking the curl gives the fluid analog of the Biot-Savart law u(x,t) = 1/(4π) ∫ d³x′ ω(x′,t)×(x–x′)/|x–x′|³ In fact, there’s an additional subtlety that’s important for fluids. While the expression above is true if the vorticity field ω(x,t) is defined everywhere in ℝ³, often that’s not the case for fluids. We may have boundaries, or obstacles in the fluid, that require us to impose certain boundary conditions. The most general form of the velocity is then u(x,t) = ∇ϕ(x,t) + 1/(4π) ∫ d³x′ ω(x′,t)×(x–x′)/|x–x′|³ (2.18)

where the u ∼ ∇ϕ piece doesn’t contribute to the vorticity because ∇ × ∇ϕ = 0. We can only reconstruct the velocity field from the vorticity up to this subtlety. In particular, there are situations – such as those we will meet in Sections 2.3 and 2.4 – where all the physics is sitting in the u ∼ ∇ϕ term.

While the mathematics leading to the electromagnetic and fluidic versions of the Biot-Savart law is identical, there are some differences. The first is conceptual. In electromagnetism, one thinks of the current J as something fixed and external, which determines the magnetic field B. In contrast, in fluid mechanics the vorticity ω is thought of as an object derived from the velocity field u. Nonetheless, there will be times in these lectures when it’s useful to think of vorticity as an object in its own right.

The second difference is more technical. The electromagnetic Biot-Savart law (2.17) holds only for static currents. There is a generalisation to time-dependent currents, but it requires us to take into account the time that it takes light to travel from the current to the place where the magnetic field is measured. (See Section 6 of the lectures on Electromagnetism.) In contrast, as shown, the fluid version (2.18) holds for time dependent flows, with the velocity and vorticity fields evaluated at the same time.

2.2.1 The Vorticity Equation

It is interesting to ask how the vorticity ω evolves. We return to the equation (2.9) that we previously used on the way to deriving Bernoulli’s formula, again restricted to a conservative force f = −∇Φ,

∂u/∂t + ρ∇(|u|²)/2 = ρu×ω − ∇P − ∇Φ (2.19)

If we take the curl of this, and use the fact that ∇×(∇anything) = 0, we have

∂ω/∂t = ∇×(u×ω)

We now use the vector identity

∇×(u×ω) = (∇·ω)u + (ω·∇)u − (∇·u)ω − (u·∇)ω

We have ∇·ω = 0 because the vorticity ω is itself a curl. And ∇·u = 0 because we’re dealing with an incompressible fluid. Rearranging the remaining terms, we have

Dω/Dt = (ω·∇)u (2.20)

This is the vorticity equation. It tells us how the vortex lines stretch and twist as the fluid evolves.

Using ∇·u = ∇·ω = 0, the vorticity equation can be rewritten as

∂ω_i/∂t + ∂(u_j ω_i − u_i ω_j)/∂x_j = 0

This is the standard form of a continuity equation, telling us that vorticity is conserved.

To try to get a feel for what the vorticity equation (2.20) is telling us, first suppose that the right-hand side vanished. Then the vorticity would simply drift with the fluid. We can get a sense for what the right-hand side means by considering two nearby points x₁(t) and x₂(t) at some time t, separated by a small distance

L(t) = x₂(t) − x₁(t)

We’ll think about how this material line segment evolves with the flow. At a later time t+δt, each of these end points has been swept along and now sit at

x_i(t+δt) ≈ x_i(t) + δx_i ≈ x_i(t) + u(x_i(t))δt

So the line segment L has evolved as

L(t+δt) ≈ x₂(t+δt) − x₁(t+δt)

≈ L(t) + [u(x₂(t)) − u(x₁(t))]δt

We now Taylor expand u(x₂) = u(x₁ + L) ≈ u(x₁) + L·∇u(x₁) to write this as

L(t+δt) ≈ L(t) + (L·∇)u(x(t))δt

where we have evaluated the gradient of the velocity field at x, which could be either x₁ or x₂ or anywhere in between: it doesn’t matter as they are close. In the limit δt → 0, all the ≈ signs become = signs. We see that a small line segment of the fluid evolves as

dL/dt = (L·∇)u

But the right-hand-side is the same form as we find in the vorticity equation (2.20). This is telling us that the lines of vorticity are stretched and twisted like the material lines of the fluid itself. We usually say that the vortex lines “move with the fluid”.

We can get a more direct expression for the change in the magnitude of the vorticity. First take the dot product of (2.20) with ω. This tells us how the magnitude (squared) of the vorticity |ω|² changes,

1/2 D|ω|²/Dt = ω·(ω·∇)u = ω_i ω_j ∂u_i/∂x_j

where, in the second term, we’ve resorted to index notation to clarify what is inner-producted with what. Note, however, that ω_i ω_j is symmetric in i and j so this picks out the strain of the flow defined in (2.14). We have

1/2 D|ω|²/Dt = ω·Eω (2.21)

We learn that vorticity is increased or decreased by the rate of strain in the flow.

Note that if, at some time, the vorticity vanishes everywhere, say ω(x,t = 0) = 0, then it will vanish everywhere at all subsequent times. This holds regardless of any conservative forces that might be at play. This prompts the question: where does vorticity come from in the first place? The answer is that it comes from non-conservative forces. These includes friction forces, as captured through the viscosity of the fluid, and the Coriolis force. We will devote Section 3 to understanding the effects of viscosity and see in a number of explicit examples how it gives rise to vorticity.

An Example

To illustrate how vortex lines stretch and twist, consider the flow

u(x,t) = u_strain(x) + u_rot(x,t) with u_strain = α(−x, −y, 2z)

u_rot = f(r,t)(−y, x, 0)

Both of these flows are similar to the examples given above. The strain flow stretches the fluid in the z direction, while squeezing in the (x,y)-plane; the rotational flow clearly rotates in the (x,y)-plane, with an angular velocity determined by the function f(r,t) where r² = x² + y².

The vorticity lies on the z-direction, with ω = (0,0,ω) and ω given by (2.16),

ω = (1/r) d(r²f)/dr

The vorticity equation (2.20) is then a partial differential equation for ω(r,t),

∂ω/∂t − αr ∂ω/∂r = 2αω

This is solved by

ω(r,t) = e^{2αt} W(r e^{αt}) (2.22)

for an arbitrary function W(r), which is the initial vorticity at time t = 0. We see that the strain indeed increases the vorticity, with an exponential growth in time. But the time dependence in the function W(r e^{αt}) gives a corresponding squeezing of the vorticity in the (x,y) plane. This effect is known as vortex stretching.

In this example, the vorticity is aligned with one of the principal axes of the rate of strain tensor. When this isn’t the case, the vortex lines get twisted by the strain.

Bernoulli’s Theorem Revisited

There is a version of Bernoulli’s theorem for the vortex lines, tangent to ω. To see this, we take the inner product of (2.19) with ω to find that, in a steady flow with ∂u/∂t = 0, we have

ω·∇H = 0

We learn that the Bernoulli function H, defined in (2.12), is constant both along streamlines (as in (2.13)) and along vortex lines.

If the vorticity vanishes everywhere, then the fluid is said to be irrotational. In this case, we can say more. For a steady, irrotational flow, the equation (2.9) tells us that Bernoulli’s function

H = ρu² + P + Φ

is actually constant everywhere in the fluid, not just along streamlines and vortex lines. We will explore these flows further in Section 2.3.

2.2.2 Kelvin’s Circulation Theorem

The circulation of a flow around a closed curve C is defined by

Γ = ∫_C u·dx

Now consider a material curve C(t), meaning that it follows the flow of the underlying fluid elements. We want to understand how the associated circulation Γ(t) changes. We have

DΓ/Dt = ∫_C (Du/Dt)·dx + ∫_C u·(D(dx)/Dt) (2.23)

We can replace Du/Dt in the first term using the Euler equation (2.6). Assuming a conservative force f = −∇Φ, this gives

∫_C (Du/Dt)·dx = ∫_C (−∇P − ∇Φ)·dx = 0

which vanishes because it is the integral of a gradient around a closed path. That leaves us with the second term in (2.23). The notation D(dx)/Dt is a little formal because the material derivative D/Dt was defined to act on fields, while here it’s acting on a line element. But the meaning is straightforward: it captures the way that the line element dx changes under the flow.

To see what this means in practice, we can return to the fundamentals. Consider a small, moving line element δx(t), with end points x₁(t) and x₂(t), so δx ≈ x₂ − x₁. We want to know how this line segment evolves. But this is the calculation that we just saw when building intuition for the meaning of the vorticity equation: there we called the material line segment L(t), but it is the same thing as δx in the present context. This tells us how the line element changes and gives meaning to the expression D(dx)/Dt: it is

D(dx)/Dt = (dx·∇)u

Using this in (2.23), we have

DΓ/Dt = ∫_C u·(dx·∇)u = ∫_C u_i (∂u_i/∂x_j) dx_j

where we’ve again resorted to index notation to clarify which objects are dotted together. This can be written as

DΓ/Dt = ∫_C (1/2) ∇(u·u)·dx = 0

which again vanishes because it is the integral of a gradient around a closed path. The upshot is that the circulation around any closed loop C(t) does not change when we follow this loop with the flow,

DΓ/Dt = 0

This is Kelvin’s Circulation Theorem.

To see the consequences of this result, first note that the circulation is related to the vorticity by Stokes theorem

Γ = ∫_S ω·dS (2.24)

where S is any surface with boundary ∂S = C. (It’s worth remembering at this point that Stokes learned about Stokes’ theorem from his friend William Thomson, later known as Lord Kelvin!) So the circulation theorem again tells us that a fluid that starts off as irrotational, with ω = 0, will remain irrotational.

More intuition comes if we focus on flows in which vorticity is localised. To this end, suppose that ω is non-vanishing only in some region of the fluid. Find a surface S such that the circulation defined in (2.24) is non-vanishing. As we vary the surface S, Γ can’t change. This means that the vorticity can’t be localised in a co-dimension three region of space: it must be extended along a tube-like region. This tube might extend to infinity, which is the case in the example of vorticity that we saw earlier in this section. Or it might form a vortex loop, as shown in the figure to the right. In either case, it can’t just end.

We learned previously that the magnitude of the vorticity can change due to the strain in the fluid (2.21). Now we see that, in a certain sense, vorticity must be conserved. There’s no contradiction here. As the magnitude of the vorticity increases, the area of the flux tube must decrease so that the vortex flux (2.24) remains unchanged. Indeed, we saw precisely this effect at play in the vortex (2.22). At heart, this is just the conservation of angular momentum: it is the fluid version of an ice skater who spins faster when they pull in their arms.

An Historical Aside

I think it’s fair to say that Kelvin got a little carried away with his results on vortices. He was so taken with the stability of vortices, and smoke rings in particular, that he proposed that they may form the basis of all matter, with different atoms arising as different knots of vortices. Some pictures from one of Kelvin’s original papers are shown in Figure 5.

With hindsight, Kelvin’s idea looks overly optimistic. Nonetheless, modern ideas In physics, it is suggested that they may contain a grain of truth. In quantum field theories, certain particles arise as so-called "solitons" in which the fields wrap themselves in some stable configuration, not unlike vortices in fluids. From a certain perspective, the proton and neutron can be viewed as solitons of an underlying pion field, known as a Skyrmion. (Admittedly, the more familiar story of the proton and neutron as made from three quarks is a more fundamental perspective.) Magnetic monopoles, if they exist, would be examples of solitons.

## 2.3 Potential Flows in

In this section we restrict ourselves to flows that are steady, so ∂u/∂t = 0, incompressible and irrotational. These latter two properties mean that ∇·u = 0 and ∇×u = 0.

This suggests two different vector calculus routes to attack the problem. We could use the first condition to write u = ∇×A. This was our previous stream function approach. However, it turns out to be more useful to use the irrotational property. If the domain of the flow is simply connected, then a vector field that obeys ∇×u = 0 can be written in terms of a potential ϕ such that u = ∇ϕ.

The requirement that the flow is incompressible, ∇·u = 0, then tells us that ∇²ϕ = 0.

This is very familiar: it is just the Laplace equation. A flow that is steady, incompressible and irrotational is called, for obvious reasons, a potential flow. Importantly, the Laplace equation is linear. That means that if we have two solutions then we can simply superpose them to get a third. The non-linearity of the Euler equation disappeared by virtue of the irrotational assumption.

To understand potential flows, all we have to do is solve the Laplace equation. The devil in the details is, as we shall see, largely in the boundary conditions imposed on the flow.

2.3.1 Boundary Conditions In many courses in theoretical physics, boundary conditions are relatively unimportant beyond the usual requirement that things fall off asymptotically. (There are, of course, counterexamples such as the study of electromagnetic waves in materials.) For fluids, however, many of the most important results come from imposing the right boundary conditions.

We’ll meet various kinds of boundary conditions in this course. For example, later when we come to discuss waves we’ll think about dynamical interfaces between two fluids. But, for now, we will restrict to the simplest kind: a solid boundary.

Suppose that the fluid comes into contact with a solid object. Maybe there’s a wall at the edge of the container. Or maybe there’s some object, like the wing of an aircraft, sitting in the fluid flow. What boundary condition should we impose?

Our first condition is completely obvious. The fluid can’t flow into the solid. To describe this mathematically, we introduce a normal vector n(x) at each point x on the boundary. If the boundary is flat, then n is constant. If the boundary curves in some way, then n changes accordingly. Provided that the boundary itself does not move, we must have n·u = 0 at each point of the boundary. This is the statement that nothing seeps into the solid. It is also the statement that the boundary of a fluid is a streamline.

We will also be interested in situations in which the boundary does move, with some velocity U. In this case, we place ourselves in the frame of the moving boundary, where the fluid velocity is u′ = u−U and the boundary condition is n·u′ = 0. Back in the original frame, we have n·u = n·U (2.25)

This simple statement that the solid is impermeable is sometimes called the kinematic boundary condition. It fixes the component of the fluid velocity perpendicular to the boundary.

We haven’t yet said anything about the component of the velocity that is tangential to the boundary. For example, we might think that a "no-slip" boundary condition should be imposed, which says that the layer of fluid right next to the boundary is stationary. Indeed, this will be important in certain fluid flows (actually, very important!) but these kinds of boundary conditions arise only when we take the viscosity of the fluid into account. For that reason we postpone their discussion to Section 3.

2.3.2 Flow Around a Sphere Perhaps the most familiar solution to the Laplace equation (and certainly the one most useful for Electromagnetism), is the spherically symmetric potential ϕ(r) = q/r (2.26)

for some constant q. This corresponds to a radial, three-dimensional flow u = q̂r / r².

Strictly speaking, this doesn’t satisfy the Laplace equation everywhere. Instead, it is the Green’s function, obeying ∇²ϕ = 4πqδ³(x).

The delta-function should be thought of as a source (for q > 0) or a sink (for q < 0) for the fluid.

This radially symmetric solution is simple, but of little immediate utility in the context of fluid dynamics because it’s hard to think of a situation in which a fluid spews out radially in 3d from some source. Instead we turn to (slightly) more complicated solutions. Our strategy is going to be a little bit cheap: rather than trying to solve a particular problem, we’ll instead write down some simple potentials and then try to interpret the results in terms of some fluid flow that might be of interest. We then declare success at having solved something important!

To make progress, we work with spherical polar coordinates x = r sinθ cosφ, y = r sinθ sinφ, z = r cosθ.

In these coordinates, the Laplacian takes the form ∇² = (1/r²) ∂/∂r (r² ∂/∂r) + (1/(r² sinθ)) ∂/∂θ (sinθ ∂/∂θ) + (1/(r² sin²θ)) ∂²/∂φ².

We’ll look for solutions that are independent of the coordinate φ. The most general such solution can be written in terms of Legendre polynomials Pₙ(cosθ), ϕ(r,θ) = Σₙ₌₀^∞ (Aₙ rⁿ + Bₙ / r^(n+1)) Pₙ(cosθ).

The radial solution that we saw above corresponds to the n = 0 term (with P₀(cosθ) = 1). The next simplest is the n = 1 term. Recalling that P₁(cosθ) = cosθ, this solution depends on two constants A and B, ϕ(r,θ) = A r + B cosθ / r² (2.27).

Both of these terms have a natural interpretation in terms of fluid flow. The first term can be rewritten as ϕ = A z, which tells us that it’s simply a straight, constant flow in the z-direction. This is shown in the left-hand side of Figure 6. The flow runs left to right in the figure, which means that I’ve made the slightly disorienting choice of taking the z-axis to lie horizontally. At large distances, this term dominates so we identify A = U as the asymptotic velocity.

The second term can be viewed, in the language of electromagnetism, as a dipole. To see this, consider a source and sink of the form (2.26) displaced slightly in some direction d. The potential is ϕ = q/r - q/|r+d| (2.28).

We then look at this at distances r ≫ |d|. We Taylor expand the second term as 1/|r+d| ≈ 1/r + d·∇(1/r) + ... = 1/r - d·r/r³ + ...

The potential (2.28) then becomes ϕ ≈ q d·r / r³ + ...

If we take the displacement to be aligned with the z-direction, so d = dẑ and d·r = d r cosθ, and subsequently take the limit |d| → 0 keeping the product qd fixed, then we get the second term in (2.27) with B = qd. The velocity field can be computed in spherical polar coordinates, u = ∂ϕ/∂r ˆr + (1/r) ∂ϕ/∂θ θ̂.

The resulting fluid flow is shown on the right in Figure 6.

Because the Laplace equation is linear, we can simply add these two flows together for any choice of A = U and B. The result is shown on the left-hand side of Figure 7. So far it’s not immediately obvious that we’ve constructed something useful. However, if we look at the velocity, we find something interesting. The radial and angular velocity are given by u_r = ∂ϕ/∂r = U - 2B cosθ / r³ and u_θ = (1/r) ∂ϕ/∂θ = -U sinθ - B sinθ / r³ (2.29).

Crucially, the radial velocity vanishes at a radius R where 2B/R³ = U.

This means that the flow has the appropriate boundary conditions to hold if there is a solid sphere of radius R at the origin. Nothing is flowing into the sphere! We then just ignore the previous flow inside the sphere at r < R completely. It is only what sits outside that matters. This is shown in the right-hand side of Figure 7. The point θ = 0 sits on the right of the sphere, and the point θ = π sits on the left, where the fluid comes from.

The upshot is that the potential ϕ = U (r + R³/(2r²)) cosθ (2.30)

describes a flow of asymptotic velocity U past a solid sphere of radius R. Standard uniqueness theorems then tell us that it is the flow with these properties.

We’ve chosen to describe a flow with asymptotic velocity U and a stationary sphere. Alternatively, we could boost by U. This means that we remove the constant U term in (2.30) to describe a fluid that is asymptotically stationary, but with a sphere moving through it at speed U.

The velocity perpendicular to the sphere vanishes, but the velocity u tangent to the surface of the sphere does not vanish when r = R. We may wonder how realistic this is for actual fluids and the answer, in many situations, is not very! We’ll revisit this when we come to discuss viscosity.

There are a number of interesting features of the flow (2.30). First, there are two points where the flow stops completely and u = 0. This happens on the surface of the sphere, r = R, at θ = 0 (on the right) and θ = π (on the left) as depicted by orange dots in Figure 7. This occurs when the fluid comes in with vanishing impact parameter and, on symmetry grounds, can’t tell whether to go up or down. So instead it stops. Points where the local fluid velocity vanishes are called stagnation points.

Next, we can look at the top and bottom of the sphere with θ = ±π/2. From (2.29), the tangential velocity there is u_θ = -U.

29), we see that the velocity on the boundary of the sphere is |u| = U top. In other words, the fluid speeds up as it moves past the sphere. In fact, this follows from Bernoulli’s principle as we explain below. Relatedly, you can see that the streamlines get squeezed together at the top and bottom of the sphere. This is familiar in other situations: stand at the top of a hill and it’s windier than it was at the bottom.

2.3.3 D’Alembert’s Paradox Next we calculate the pressure that the fluid exerts on the sphere. For this we use Bernoulli’s principle which says that the function H defined in (2.12) remains constant along streamlines (and, because the flow is irrotational, throughout the fluid). Asymptotically, H = ρU^2 + P where P is the asymptotic pressure of the flow. Meanwhile, on the surface of the sphere H = ρU^2 sin^2 θ + P(θ)

So the pressure on the surface of the sphere is P(θ) = P + ρU^2 (1 - (9/4) sin^2 θ) (2.31)

Here’s the weird thing: the pressure depends only on sin^2 θ. This means that the pressure exerted on the sphere at the front, where π/2 < θ ≤ π (this is on the left in the figure) is identical to the pressure exerted behind, where 0 ≤ θ < π/2 (on the right in the figure). And that doesn’t sound right at all! We know from experience that an object placed in a stream will suffer a drag force which, in this case, should serve to carry the sphere along with the flow. But that’s not what we find! Instead the flow finds a way to move seamlessly around the object, exerting no force.

Said differently, we can always boost our solution by speed U so that the fluid is stationary and the sphere is moving through it with speed U. The result above says that the sphere experiences no friction. It just glides through the fluid unimpeded.

Tantalising as this sounds, it’s simply not right. The fact that the maths differs so wildly from observation is known as the D’Alembert paradox, after the mathematic ce to the proceedings. We’ll now see how this manifests itself in a simple example.

2.4.1 Circulation Around a Cylinder We consider the flow around an infinite cylinder, aligned along the y direction. This ensures that the flow is effectively two-dimensional: we care only about the velocity in the (x,z)-plane.

The start of our story is the same as the flow around a sphere that we saw in the previous section. The most general solution to the 2d Laplace equation is ϕ(r,θ) = (A + B log r)(C + D θ) + Σ (Aₙ rⁿ cos(nθ+αₙ) + (Bₙ / rⁿ) cos(nθ+βₙ))

n=1 Here we focus on the flows with n = 1. The integration constants α₁ and β₁ will play no role so we set them to zero and look at: ϕ = U (r + (R² / r) cosθ) (2.33)

This is very similar to the 3d potential (2.27). Again, the first term describes a constant flow with asymptotic velocity U, a fact that we’ve anticipated in labelling the overall coefficient. The second term is now a two-dimensional dipole. Combined, they give rise to the velocity field u = (∂ϕ/∂r) r̂ + (1/r)(∂ϕ/∂θ) θ̂ = U (1 − (R² / r²)) cosθ r̂ − U (1 + (R² / r²)) sinθ θ̂ (2.34)

We see that the radial component has the property that u_r = U (1 − (R² / r²)) cosθ = 0 when r = R This means that this potential describes the flow past a solid cylinder of radius R. The velocity field u is shown on the right, with the two stagnation points shown in orange. The details are slightly different, but the qualitative features are the same as for the sphere.

Adding Circulation Things get more interesting if we add some circulation. Because the Laplace equation is linear, we can superpose the flow around the cylinder (2.33) with the rotation (2.32), ϕ = U (r + (R² / r) cosθ) + (Γ / 2π) θ (2.35)

The extra term affects only the angular part of the velocity, which now takes the form u = U (1 − (R² / r²)) cosθ r̂ + (−U (1 + (R² / r²)) sinθ + (Γ / 2πr)) θ̂ You can check that the associated stream function is Ψ = Ur (1 − (R² / r²)) sinθ − (Γ / 2π) log(r) (2.36)

To understand the effect on the flow, we can search for the stagnation points at which |u| = 0. Clearly u = 0 provided that we sit at radius r = R. The angular velocity then vanishes at the angle θ such that Γ = 4πUR sinθ But this has a solution only when |Γ| < 4πUR (where we’re taking U > 0). This suggests that the flow will be different for small and large circulation Γ.

We start by looking at small |Γ| < 4πUR so that there are two stagnation points on the surface of the cylinder at sinθ = Γ/4πUR. The corresponding flow is shown on the left hand side of Figure 8. (I’ve taken Γ < 0 in this figure for reasons that will become apparent below.) Note that the stagnation point plays an important role: this is where the fluid separates, with stream lines on either side taking different paths, one above the cylinder and the other below.

Meanwhile, when |Γ| > 4πUR, there is no stagnation point on the surface of the cylinder. Instead it now occurs at θ = π/2 (which ensures that u_r = 0) and a distance r from the centre, given by the solution to the quadratic r² − (Γ / 2πU) r + R² = 0 This ensures that u_θ = 0. The quadratic is guaranteed to have one positive root sitting outside the sphere provided that |Γ| > 4πUR. The flow is shown on the right-hand side of Figure 8, again with the stagnation point shown in orange.

2.4.2 Lift and the Magnus Force Now we can repeat the calculation that we performed for the sphere to answer the question: what’s the pressure that the fluid exerts on the cylinder? We use Bernoulli’s principle and the conservation of H throughout the flow. At infinity we have H = ρU² + P while, on the surface of the sphere, it is H = ρ (−2U sinθ + (Γ / 2πR))² + P(θ)

So the pressure on the surface of the sphere is P(θ) = P∞ + ½ρU² (1 − 4 sin²θ) + (UΓρ / πR) sinθ − (Γ²ρ / 8π²R²) (2.37)

The pressure acts radially on the sphere. We want to decompose this force to compute the component forces F in the z-direction (horizontal in the flow diagrams in Figure 8) and the x-direction (vertically in Figure 8). From the diagram on the right, we see that F_z = ∫₀²π P(θ) R cosθ dθ = 0 So there is no force in the direction of the flow. Or, said differently, there is no drag force. This is the same result that we saw for the sphere and leads to D’Alembert’s paradox. The novelty is that the force perpendicular to the asymptotic flow is non-vanishing: it receives a contribution from the sinθ term in (2.37), F_x = − ∫₀²π P(θ) R sinθ dθ = − ∫₀²π (UΓρ / πR) sin²θ dθ = −UΓρ The minus sign means that, for Γ < 0 as shown in Figure 8, the force is upwards. This makes sense: if you look at the figure, you see that the streamlines are closer together at the top of the cylinder. This means that the fluid is travelling faster at the top and, correspondingly, there is a lower pressure. Hence the upwards force. This force is called lift. (We took Γ < 0 in Figure 8 to save ourselves the embarrassment of having a force called “lift” that acts downwards.)

In the calculation above, we took the fluid to be circulating and the cylinder to be stationary. However, the same effect occurs if the cylinder rotates while the fluid has no circulation. In this situation, the lift force is referred to as the Magnus force. It is the same force that makes a ball swerve when you put spin on it.

## 2.5 A Variational Principle

All laws of physics can be expressed using the principle of least action. What about the laws of fluid mechanics?

The action principle is best suited to fundamental laws of physics where there is no friction at play. The full Navier-Stokes equation for fluids (that we will meet in Section 3) includes a friction term and so isn’t immediately amenable to a formulation using an action. But the Euler equation that we’ve studied in this section has no such friction term which suggests that it should be possible to write down an action that gives rise to the Euler equation. The question is: how?

This, it turns out, is not quite as straightforward as one might think. But it is possible and, moreover, gives some insight into the mathematical structure of the Euler equation. The purpose of this section is to describe this.

This section is something of a tangent to the rest of these notes and we won’t be returning to the action principle later in these lectures, not least because we’ll be embracing the full Navier-Stokes equation. Also, the terminology in this section can be a little confusing simply because Euler and Lagrange were rather impressive mathematicians. To give you a sense of this, our goal is to work in the Eulerian framework of fluid mechanics, rather than the Lagrangian framework, and then write down a Lagrangian and derive the Euler-Lagrange equations to reproduce the Euler equation. All clear? Good.

2.5.1 The Principle of Least Action We start by giving a review of the principle of least action, both in the framework of classical mechanics and also in classical field theory. You can read more about this in the lectures on Classical Dynamics and in the first section of the lectures on Quantum Field Theory.

First, Newtonian mechanics. We’ll consider a single particle with a position given by x ∈ R³. The position changes with time, so the trajectory of a particle traces out a curve x(t). Of all these possible trajectories, there is typically one that obeys the laws of physics. We want to know which one.

If the particle has mass m then its kinetic energy is T = ½mẋ². We’ll assume that the particle experiences a potential energy V(x). We then define the Lagrangian L(x, ẋ) = T − V (2.38)

and, from this, the action S[x(t)] = ∫ dt L(x, ẋ) = ∫ dt (½mẋ² − V(x)) (2.39)

The action assigns a number S to each trajectory x(t). (Strictly speaking, we should consider the action for all trajectories with certain boundary conditions specified, such as x(t₀) = x₀ and x(t₁) = x₁. This is important, but we’ll sweep it under the rug in what follows.)

The principle of least action states that the true trajectory x(t) followed by the particle is the one that extremises the action S. Mathematically, this means the following. Suppose that you have a putative trajectory x(t) with some action S. We look at all neighbouring trajectories x(t)+δx(t) and compute their action S +δS. The original trajectory is the one taken by the particle if δS = 0 for all variations δx(t).

For our action (2.39), we have S[x(t)+δx(t)] = ∫ dt [½m(ẋ + δẋ)² − V(x+δx)]

≈ ∫ dt [½m(ẋ² + 2ẋ·δẋ) − V(x) − ∇V·δx] = S + δS where, in going to the second line, we’ve ignored all terms of order δx² and higher. This gives us an expression for the variation of the action δS which we can now play with δS = ∫ dt [mẋ·δẋ − ∇V·δx] = ∫ dt [−mẍ − ∇V]·δx In the second equality we’ve integrated by parts and thrown away the boundary terms. (We’ve been careless about why one can throw away boundary terms after integration by parts; that’s the bit we’re sweeping under the rug.) The principle of least action states that the true trajectory has δS = 0 for all possible variations δx. This can only be true if the expression in square brackets vanishes, meaning mẍ = −∇V (2.40)

This, of course, is the Newtonian equation of motion. The principle of least action is just a recasting of this familiar result.

The action for a given equation of motion is not necessarily unique. Here, for example, is a different action that yields the same equation of motion (2.40). We will initially think of the position x(t) and velocity v(t) of the particle as independent quantities. We’ll then enforce the requirement v = ẋ through the use of a Lagrange multiplier. The upshot is that we can write down the action S[x(t), v(t), β(t)] = ∫ dt [½mv² − V(x) + β(t)·(v − ẋ)]

The equation of motion for β reproduces the constraint v = x˙, while the equation of motion for v tells us that we should identify the Lagrange multiplier with the velocity: m v = β. Finally, the equation of motion for x is β = −∇V. Combining these reproduces (2.40).

For the Newtonian particle, there’s clearly no advantage to writing the action (2.41) over (2.39). Indeed, it seems a little perverse to do so. But these kind of tricks can prove useful in other contexts and one of these turns out to be fluid dynamics.

**An Action for Fields**

The next conceptual step is to move from particles to fields. We will consider a scalar field φ(x,t) which associates a number to each point in space and time. Note, in particular, that the role of the spatial coordinate x has changed. In the context of Newtonian mechanics, x was the dynamical degree of freedom, something that evolves over time. But in field theory that’s no longer the case. Now x is just a label, like time t, and the field φ is the dynamical degree of freedom whose values depend on both space and time.

We would like to write down an action for this field. This means that we want to associate a number S to each possible field configuration φ(x,t). We start by defining the Lagrangian density L (although everyone simply refers to it as the “Lagrangian”). A natural choice, which is the analog of (2.38), is L(φ, φ˙, ∇φ) = (1/2) φ˙^2 − (1/2) c^2 (∇φ)^2 − V(φ).

We have a kinetic energy type term, φ˙^2, but now we have two different kinds of potential energy. The first, proportional to (∇φ)^2, is an energy arising from spatial gradients of the field. It comes with a constant coefficient c which has dimension [c] = LT^−1. In many situations, this is the speed of ripples of the field. In addition, we have a second potential energy V(φ) which depends only on φ and not on its derivatives. We pick different potentials V(φ) to model the situation that we’re interested in, just like V(x) in Newtonian mechanics. Typically one picks V(φ) so that it penalises large values of φ, e.g. V(φ) ∼ φ^2. Here we’ll keep V(φ) general.

We associate an action S to a given field configuration φ(x,t) by integrating the Lagrangian over both space and time, S = ∫ dt ∫ d^3x L = ∫ dt ∫ d^3x [ (1/2) φ˙^2 − (1/2) c^2 (∇φ)^2 − V(φ) ] (2.42)

It’s worth stressing, for the second time, the different roles that the spatial coordinate plays in (2.39) and (2.42). It has been demoted from its role as a dynamical degree of freedom in the former to a mere integration variable in the latter.

At this point, we proceed in much the same way as for the Newtonian particle. We take a reference field configuration φ(x,t) and compute its action S. Then we look at all nearby field configurations φ(x,t) + δφ(x,t) and compute their action S + δS. The original field configuration obeys the classical equations of motion if and only if δS = 0 for all δφ. In equations, we have S[φ + δφ] = ∫ dt ∫ d^3x [ (1/2) (φ˙ + δφ˙)^2 − (1/2) c^2 (∇φ + ∇δφ)^2 − V(φ + δφ) ]

≈ ∫ dt ∫ d^3x [ (1/2) (φ˙^2 + 2 φ˙ δφ˙) − (1/2) c^2 (∇φ^2 + ∇φ·∇δφ) − V(φ) − (∂V/∂φ) δφ ]

where, as before, we’ve truncated our expansion at leading order in δφ in the second line. From this we can extract the variation of the action δS = ∫ dt ∫ d^3x [ φ˙ δφ˙ − c^2 ∇φ·∇δφ − (∂V/∂φ) δφ ]

= ∫ dt ∫ d^3x [ −φ¨ + c^2 ∇^2 φ − (∂V/∂φ) ] δφ Here we’ve again integrated by parts, now with respect to both temporal and spatial derivatives, so that all terms are proportional to δφ. Requiring that δS = 0 for all possible δφ tells us that the expression in square brackets must vanish, so ∂^2φ/∂t^2 − c^2 ∇^2 φ = −(∂V/∂φ) (2.43)

This is the simplest equation of motion for a classical scalar field.

The equation of motion (2.43) doesn’t play a particularly prominent role in classical physics, where our heads are more likely to be turned by more sophisticated theories such as Electromagnetism or General Relativity. It does however, arise in various cameos and we’ll meet it briefly in Section 4.3.2 when discussing a certain kind of wave that is driven by the Coriolis force. The equation only really comes to the fore when we turn to Quantum Field Theory, where it plays more of a starring role.

**2.5.2 An Action Principle for Fluids**

Now we are in a position to construct an action principle for fluids. Our goal is to write down an action which reproduces the Euler equation for an incompressible fluid ρ (Du/Dt) = −∇P and ∇·u = 0 (2.44)

We could also include further forces, such as gravity, but since this doesn’t add extra conceptual issues we will just ignore it and focus on the simplest equations above.

The first question that we should ask is: what are the dynamical degrees of freedom for a fluid? Until now, we have viewed (2.44) as four equations for four variables, u and P. But we might suspect that these aren’t quite the right variables to construct an action. After all, when writing down an action for the Newtonian particle, it’s important that we vary with respect to the position x rather than the velocity x˙. And the same is true for a fluid. To build an action, we need to start thinking about the “position” of the fluid.

To this end, we will think of the configuration of the fluid as a map from ℝ^3 → ℝ^3, x ↦ α_i(x,t), i = 1,2,3. Here x label the fixed positions in space, while α_i(x,t) label parcels of the fluid. This is the Eulerian (as opposed to Lagrangian) description of a fluid. We will refer to α_i as the embedding coordinate of the fluid.

We will think of α_i(x,t) as the fields of our Lagrangian although, as we will see, they will need to be augmented by several more. But even before we get going, it’s worth pointing out that α_i(x,t) aren’t quite like other fields. This is because the map from ℝ^3 → ℝ^3 that describes our fluid must be invertible. For example, there’s no configuration of the fluid with, say, α_i(x,t) = 0. That would describe the entire fluid as sitting at a single point and that’s not allowed. In fact, because our fluid is incompressible, we should require that the map from ℝ^3 → ℝ^3 is volume preserving. This is assured if det(∂α_i/∂x_j) = 1 (2.45)

We will have to find a way to impose a constraint like this on our map.

(As an aside: these kind of constraints are not entirely unfamiliar. In general relativity, the dynamical degree of freedom is a metric g_μν(x,t) but, as with a fluid, we’re not allowed to set g_μν = 0. Instead, we must have det(g_μν) ≠ 0.)

We describe the fluid by the maps α_i. How do we define the velocity? You might naively think that it’s just α˙_i, but that’s not right. Instead, we need to think more physically. Suppose that you focus on one particular parcel of fluid, say the one labelled by α_i = (3,7,4). Then we can follow this parcel through the fluid. If α_i(x,t) changes then the parcel of fluid must have moved to some neighbouring point, which means that the velocity u is non-zero. This velocity is defined implicitly as ∂α_i/∂t + u·∇α_i = 0 (2.46)

Because the map from ℝ^3 → ℝ^3 is invertible, we can get an explicit expression for u in terms of α_i. Using the fact that the map preserves volumes (2.45), this is given by u_i(x,t) = −(1/2) ε_{ijk} ε_{lmn} (∂α_l/∂t) (∂α_m/∂x_j) (∂α_n/∂x_k).

To see this, you just need to use the definition of the determinant in terms of ε_{ijk}. It’s also straightforward to show that the condition (2.45) ensures that ∇ · u = 0 as expected. (You should use the expression for the determinant of a 3×3 matrix in terms of ε_{ijk}.)

Note that for these incompressible flows, with ∇·u = 0, the equation (2.46) takes the form of a conservation law ∂α_i/∂t + ∇·(u α_i) = 0. There is a simple physical intuition for this: it is just the statement that you can trace the evolution of a given parcel of fluid, a kind of “conservation of particle identity” if you like.

Now we’ve set-up the basic kinematical structure for fluids, our next job is to write down the action. Here a number of choices await us. It is possible to write down an action just for the embedding coordinates α_i(x,t), with the constraint (2.45) imposed by a Lagrange multiplier. While it’s possible, it’s also a little messy. It turns out to be more straightforward to write down an action for α_i and u_i, together with a collection of Lagrange multipliers. This is analogous to the slightly daft action (2.41) that we introduced for the Newtonian particle.

We take as our action S[α, u, ϕ, β] = ∫ dt ∫ d^3x [ ρ u^2/2 + ϕ ∇·u + β_i (∂α_i/∂t + u·∇α_i) ] (2.47)

The equations of motion arise from varying the action with respect to α_i(x,t), u_i(x,t) and the Lagrange multipliers ϕ(x,t) and β_i(x,t).

The Lagrange multipliers are easiest to deal with. Varying with respect to ϕ gives the incompressibility condition ∇·u = 0, now directly in terms of velocity rather than the more abstract (2.45). Meanwhile, varying with respect to β_i gives us the relation (2.46) between the embedding coordinate and velocity. That leaves us with the equations of motion that come from varying the action with respect to α_i and u_i. If we vary with respect to α_i, we have ∂β_i/∂t + u·∇β_i = 0 (2.48)

So we see that the Lagrange multipliers β_i obey the same equation (2.46) as the embedding coordinates. Meanwhile, varying with respect to the components of the velocity u gives the expression ρ u_i = ∇ϕ + β_j ∇α_j (2.49)

This is a curious equation, relating the velocity to ϕ, α and β. Note that the first term is familiar: it is just the kind of potential flow that we met in Sections 2.3 and 2.4, with the Lagrange multiplier playing the role of the potential. But the second term is less familiar and it’s not immediately obvious how this is related to the Euler equation. In particular, we haven’t yet seen how the pressure emerges in this framework.

To make progress, we compute Du/Dt using the expression (2.49). There’s a little bit of algebra involved, but it’s not too hard to show that ρ (Du_i/Dt) = ...

≡ ρ +uj = +β + ρu2 + j − j Dt ∂t ∂xj ∂xi ∂t j ∂t 2 Dt ∂xi Dt ∂xi But the last two terms vanish by virtue of (2.46) and (2.48). We’re left, Du ∂ϕ ∂αj 1 ρ = −∇P where P = − −β − ρu2 +constant Dt ∂t ∂t 2 with the pressure given, as shown, by a combination of the velocity and Lagrange multipliers. This is the promised Euler equation, now derived from an action principle.

A Slightly Simpler Action As we mentioned above, there are slightly simpler versions of the fluid action. Here we describe one that succeeds in eliminating the need for embedding coordinates completely. Instead, it uses the fact that a general velocity field u(x,t) in R3 can be written as u = ∇ϕ+β∇α (2.50) for some functions ϕ, β and α. (These functions are not unique.) This is sometimes known as the Clebsch representation. Note that it’s very similar to the form of the velocity (2.49) that arose from our previous variational principle, except now there is just a single α and β function rather than a triplet. There is a nice way of visualising the form of the velocity field (2.50). The first term is clearly the irrotational, potential flow that we met previously. The second term gives vorticity ω = ∇×u = ∇β ×∇α This is telling us that vortex lines (i.e. integral curves of ω) lie on the intersection of surfaces of constant α and constant β. Now consider the action (cid:90) (cid:20) (cid:21) ∂α 1 S = dtd3x −β − (∇ϕ+β∇α)2 (2.51) ∂t 2 This is closely related to our previous action (2.47): it’s what you get if you substitute the expression (2.49) for u into the action and drop the i = 1,2,3 indices on αi and β. Now when varying the action, we must remember that the velocity u is defined by (2.50). The equation of motion for ϕ then tells us that ∇ · u = 0. Meanwhile, the equations of motions for α and β are, respectively, Dβ Dα = 0 and = 0 Dt Dt

We can now repeat our previous calculation to once again find the Euler equation (cid:18) (cid:19) Du ∂ϕ ∂α 1 ρ = −∇P with P = ρ − −β − (∇ϕ+ on the surface of the volume and this ensures that it appears in the Navier-Stokes equation as the gradient ∇P as the surface integral is converted to a volume integral by the divergence theorem. Similarly, the friction forces also naturally act on the surface of the volume as a neighbouring piece of fluid brushes past. So our first task is to better understand what the general kind of force acting on a surface looks like.

Consider a small cubic volume V as shown in the figure. Obviously there are six sides, and there may be a force acting on each. The pressure force is special because it acts parallel to the normal on each side. But that not necessarily the case for all forces. In general, the force might act in any direction. Moreover, the direction of the force will generally depend on the orientation of the surface. For example, this is obviously true of pressure which is parallel to the normal. The figure to the right shows the normals to two faces in green, while the force acting on those faces is shown in red.

These considerations mean that to specify the force that acts on a surface, we first have to specify the orientation to the surface. This is achieved through the introduction of the stress tensor, σ. It is defined so that the force F acting on a small surface of area δA and normal n is given by F := f δA = σnδA Here f is the force per unit area. (Like pressure). In index notation, we have f_i = σ_{ij} n_j (3.4)

For pressure, the stress tensor takes the simple diagonal form σ_{ij} = -P δ_{ij} But, in general, it may take a more complicated form. Furthermore, for a fluid the stress tensor is itself a field σ_{ij}(x,t) that may vary in both space and time. This means that the forces acting on various parts of the fluid depend both on their position in the fluid and on the orientation of the surface that is considered.

The stress tensor has an important property: it is symmetric σ_{ij} = σ_{ji} We will now show this. Consider the (slightly messy) Figure 9 depicting a small cube with side lengths L. The two red lines depict the force (per unit area) in the x direction on the faces that are normal to the y direction. From (3.4) this force is σ_{12}. Meanwhile, the two purple lines depict the force in the y-direction on the faces that are normal to the x direction. This force is σ_{21}.

These four forces give rise to a torque. Each σ_{ij} is a force-per-unit-area, so the actual force is L^2 σ_{ij}. Furthermore, the moment of each force about the centre of the cube is L/2. This means that the total torque around a line parallel to the z-axis, through the centre of the cube, is τ_z = L^3(σ_{12} - σ_{21}) + O(L^4 ∂σ_{12}/∂y, L^4 ∂σ_{21}/∂x)

The leading term comes from the difference between σ_{12} and σ_{21}. The sub-leading terms come from the difference of, say, σ_{12} on the left and right-hand faces. (The statement that the cube is small is the assumption that σ_{ij} does not vary much over the length scale L.)

Further torque may come from bulk forces whose strength varies over the inside of the cube. But this torque will always be of order L^4 (times some suitable dimensionful parameter) so, for small cubes, the leading contribution to the torque is proportional to the difference (σ_{12} - σ_{21}) and scales as L^3.

But torques that scale as L^3 are bad. To see this, recall that the angular acceleration is given by ω˙ = τ/I where I is the moment of inertia. But the moment of inertia of any object always scales as L^5 (which is mass × L^2 = ρL^5) and so ω˙ ∼ 1/L^2. The actual speed of the object is v ∼ ωL so if the torque scales as L^3, the acceleration will diverge as v˙ ∼ 1/L for small L. That makes no sense. To avoid this we must have σ_{12} = σ_{21} Obviously the same argument works for all other components: σ_{ij} = σ_{ji}. The stress tensor is necessarily symmetric.

3.1.1 Newtonian Fluids With the technology of the stress tensor, it is straightforward to describe the effect of friction. A Newtonian fluid is one where the friction forces are linear in velocity. If we assume that the fluid is isotropic then the form of the force is pretty much fixed by rotational invariance: it must be a symmetric tensor constructed from ∇ and u and the only option is ∂_i u_j + ∂_j u_i. In fact, a symmetric tensor can be decomposed into its trace and a traceless piece (see the lectures on Vector Calculus) so in general we have, including the pressure term, σ_{ij} = -Pδ_{ij} + µ(∂_i u_j + ∂_j u_i - (2/3) ∇·u δ_{ij}) + ζ ∇·u δ_{ij} where, as we saw previously, µ is the dynamical shear viscosity. This time we’ve included the extra term proportional to ∇ · u with a coefficient ζ known as the bulk viscosity or sometimes the volume viscosity. Importantly, it can be shown that each of these coefficients is necessarily positive. For µ, this follows from energy dissipation and we will give the argument shortly. For ζ it turns out that this follows from considerations of entropy. However, in this course we are dealing only with incompressible fluids with ∇·u = 0 which means that we can forget all about the bulk viscosity. We have σ_{ij} = -Pδ_{ij} + 2µE_{ij} (3.5)

where E_{ij} is the rate of strain tensor that we met previously (2.14)

E_{ij} = (1/2)(∂_i u_j + ∂_j u_i) (3.6)

We can now use this form of the stress tensor in the equation of motion for the fluid. With a general surface force, captured by σ_{ij}, the equation of motion for a fluid (3.3) become ∫_V ρ (Du_i/Dt) dV = ∫_S σ_{ij} dS_j where we have neglected other forces such as gravity. We use the divergence theorem to change the surface integral into a volume integral ∫_V ρ (Du_i/Dt) dV = ∫_V (∂σ_{ij}/∂x_j) dV This formula holds for arbitrary volume V, so the equation of motion is ρ (Du_i/Dt) = ∂σ_{ij}/∂x_j (3.7)

From our equation (3.5), the right-hand side becomes ∂σ_{ij}/∂x_j = -∂P/∂x_i + µ(∂^2u_i/∂x_j∂x_j + ∂^2u_j/∂x_j∂x_i)

The second of these vanishes, again using our incompressibility condition ∇ · u = 0, and we’re left with promised Navier-Stokes equation, ρ (Du/Dt) = -∇P + µ∇^2u In what follows, we’ll often divide by the density to write the Navier-Stokes equation as Du/Dt = -(1/ρ) ∇P + ν∇^2u where, as defined earlier, ν = µ/ρ is the kinematic viscosity. We can also add further forces on the right-hand side to taste.

The derivation of the Navier-Stokes equation that we described above sits entirely within the continuum language that underlies this course. There is another remarkable, and ultimately better, derivation that really goes back to basics. This is due to Boltzmann. The derivation starts with the underlying ∼ 10^{23} atoms and tracks their interactions, albeit in a statistical way. It explains why the variables of the Navier-Stokes equation are the right thing to focus on if you care only about long-time physics and gives a microscopic explanation of the various terms. You can find this derivation in the lectures on Kinetic Theory.

3.1.2 Momentum and Energy Conservation Revisited For inviscid fluids, the Euler equation is simply the statement that momentum is conserved, while energy conservation (2.11) led to Bernoulli’s principle. What becomes of these in the presence of viscosity?

First momentum. Here there is no problem: in the absence of external forces, we can write the Navier-Stokes equation in the form of a continuity equation, telling us that momentum is conserved. The only difference from the Euler equation is that we get an extra term in the momentum current, proportional to the viscosity ∂(ρu_i)/∂t + ∂Π_{ij}/∂x_j = 0 with Π_{ij} = ρu_i u_j + Pδ_{ij} - 2µE_{ij} As before, we’ve used the fact that ∇·u = 0 for incompressible fluids. In particular, we’ve used this to keep Π_{ij} symmetric by taking the extra term proportional to the rate of strain tensor (3.6) rather than just ∂_j u_i.

This gives us another perspective on the Navier-Stokes equation: it is, like the Euler equation, simply conservation of momentum, but with an additional term in the momentum current coming from gradients of the velocity. The idea that gradients drive currents is something that also occurs in other, perhaps more familiar, contexts where it goes by the name of Fick’s law. For example, differences in temperature result in a heat current J ∼ ∇T.

What about energy? We will ignore other bulk forces for now. (We’ve already seen in Section 2.1.4 that conservative forces don’t spoil conservation of energy.) However, it’s useful to briefly return to the form of the Navier-Stokes equation (3.7) in which we allow for general stress forces σ_{ij}. Taking the inner product with the velocity u, the matter derivative becomes u·(Du/Dt) = u_i·(∂u_i/∂t + u_j ∂u_i/∂x_j) = (1/2)∂|u|^2/∂t + (1/2) u·∇|u|^2 and our proto-Navier-Stokes equation (3.7) becomes ρ (∂|u|^2/(2∂t) + u·∇|u|^2) = u_i (∂σ_{ij}/∂x_j)

Remember the game that we’re playing: we’d like to massage this into the continuity equation to see the conservation of energy. Using the fact the fluid is incompressible, so ∇·u = 0, we have ρ ∂(|u|^2/2)/∂t + ∂( (ρ|u|^2/2) u_j )/∂x_j - u_i σ_{ij} = -σ_{ij} (∂u_i/∂x_j) = -σ_{ij} E_{ij} where, in the second equality, we’ve used the fact that σ_{ij} = σ_{ji} so the contraction picks out the symmetric part of ∂u_i/∂x_j which is E_{ij}, the rate of strain tensor defined in (3.6). The two terms on the left-hand side take the form of a continuity equation. But now the right-hand side is not zero. This tells us that, in contrast to the Euler equation, energy is not conserved in the Navier-Stokes equation.

We can get an expression for how energy is low. If we integrate over some fixed volume V then we have ∫_V ρ ∂(|u|^2/2)/∂t dV + ∫_S ( (ρ|u|^2/2) u_j - u_i σ_{ij} ) dS_j = -∫_V σ_{ij} E_{ij} dV (3.8)

with S = ∂V. The volume term on the left-hand side is clearly the change in the kinetic energy In V. The surface term accounts for (some of) this change: the |u|2u term captures the energy that flows out through the surface, while the σ uj is the work done by the surface forces on the fluid contained in V. This includes the work done by the both the pressure and by the viscous forces. All of this is consistent with the conservation of energy. However, because the right-hand side of (3.8) doesn’t vanish is telling us that energy is, in fact, no longer conserved. Instead, the right-hand side tells us the rate at which energy is dissipated.

Dissipation = σ E dV = 2µ E E dV (3.9)

ij ij ij ij V V where, in the second equality, we’ve used the explicit form of the stress tensor (3.5). We see that the pressure doesn’t contribute to energy dissipation (because δ E = ∇ · u = 0). This, of course, is something that we found when studying the Euler equation. But we now see that one important consequence of viscosity is we no longer have energy conservation. Correspondingly, the Bernoulli’s principle no longer holds when the effects of viscosity are important.

The dissipation is the integral of a total square, so it clearly positive provided that µ > 0. And the minus sign on the right-hand side of (3.8) is telling us that energy is lost to friction, rather than gained. This is reason why we should take µ > 0. It is natural to ask: where did the energy go?! After all, energy is certainly conserved at a fundamental level. The answer is that it went into heat. The dissipation (3.9) is a transfer of energy from the macroscopic, coherent kinetic energy of the fluid, captured by the coarse-grained velocity field u, to some microscopic, incoherent internal motion of the underlying atoms. This internal motion is still kinetic energy, but not with any overall preferred direction. To properly account for this, we should understand how the temperature and entropy of the fluid changes due to these dissipative effects. As with friction forces in classical mechanics, we won’t attempt to do this here: we will simply count this as lost energy. (We will, however, return to the interplay of heat and energy in Section 4.4 when we discuss sound waves.)

## 3.2 Some Simple Viscous Flows

Our first task is to explore some very simple solutions to the Navier-Stokes equation (3.2). This will allow us to build some intuition for the role that viscosity plays.

3.2.1 The No-Slip Boundary Condition We’ve already seen the importance of boundary conditions in constructing fluid flows. For an inviscid flow, we introduced the obvious “you shall not pass” condition in Section 2.3, n·u = 0 (3.10), where n is the normal to a solid surface. This solid surface might be the walls of the container, or an obstacle sitting in the fluid like the sphere and cylinder we studied previously. If the solid object is itself moving with some velocity U then this condition becomes n·u = n·U.

For viscous fluids, we introduce a further boundary condition that restricts the flow tangent to a solid. This is the no-slip condition that states t·u = t·U (3.11), where t is now the vector tangent to the boundary. This states that the velocity of the fluid along the boundary must match the velocity of the boundary itself. It is sometimes written as the requirement that u−(u·n)n is continuous at the boundary.

The no-slip condition (3.11) doesn’t follow from the Navier-Stokes equation. Instead, it is something additional that we assert. It is, however, physically sensible and arises from the friction forces between the fluid and the boundary. Importantly, it is also the boundary condition that is observed to be correct for most experiments.

Note that the flows that we met in Section 2 describing fluids moving around spheres and cylinders do not obey the no-slip condition. Of course, they also failed miserably in explaining drag forces. This is our first hint that we should do a better job of describing the flows close to the boundary of an object. You might wonder why we just don’t search for other solutions to the Euler equations that include the no-slip condition. The reason is that there simply aren’t any such solutions. This is because the Euler equation is first order in spatial derivatives and we only get to impose one boundary condition, namely the impenetrability condition (3.10). In contrast, the Navier-Stokes equation is second order. This means that we must impose an additional boundary condition when solving the equation. The no-slip condition is the boundary condition of choice.

3.2.2 Couette Flow Take two infinite parallel plates lying in the (x,y) plane and separated by some distance h in the z-direction. The bottom plate is stationary while the top plate moves with a constant speed U in the x-direction. What happens to fluid trapped between them? We will look for a steady flow with ∂u/∂t with the velocity lying solely in the x-direction. The speed of the fluid depends only on the z direction, meaning u(x,t) = (u(z),0,0).

With this ansatz (u·∇)u = 0 so the material time derivative vanishes: Du/Dt = 0. There are no pressure gradients in the fluid, so the only surviving term in the Navier-Stokes equation comes from the viscosity, µ d²u/dz² = 0. The boundary conditions are u(0) = 0 and u(h) = U. This is an easy equation to solve and the velocity profile must increase linearly to match the speeds of the two plates, u(z) = Uz/h.

The result is known as Couette flow and is shown in the figure. Flows of this kind, in which adjacent layers of fluids move at different speeds, are collectively referred to as shear flows.

Couette flow is not a potential flow. The simplest way to see this is to note that, even though the flow doesn’t look like its rotating, it has vorticity ω = ∇×u = (0,U/h,0). This vorticity arises because we’ve implemented the no-slip boundary condition, ensuring that the upper plate drags the fluid along with it. This suggests that the no-slip boundary condition may be a way to generate vorticity. We will see later that this is an important observation.

It is a simple matter to compute the stress exerted on the fluid using (3.5), σ = -P 0 µU/h 0 -P 0 µU/h 0 -P This tells us that the force per unit area exerted by the top plate with n = zˆ is f = (µU/h,0,−P), while the bottom plate, with n = −zˆ exerts an equal and opposite force. We usually think of the bottom plate, and the distance h between the plates, as fixed externally. We then ask what force we have to exert on the upper plate to keep it moving if it has (large) area A. The answer is F/A = µU/h.

This is operational definition of viscosity µ that we met in our first course on Newtonian Mechanics. The work done by this pushing (again, per unit area) is just µU²/h. You can check that this agrees with the more formal definition of dissipation given in (3.9).

Circular Couette Flow The same basic idea arises in different geometries. Consider, for example, two concentric, infinite cylinders, aligned along the z-direction. The inner cylinder has radius R₁ and rotates with angular velocity Ω₁. The outer cylinder has radius R₂ and rotates with angular velocity Ω₂.

From the geometry, we see that the flow should be rotationally invariant, meaning that it takes the form u = Ω(r)(y,−x,0), where r² = x² + y² and Ω(r) is the angular velocity of the fluid. The no-slip condition implements the boundary conditions Ω(R₁) = Ω₁ and Ω(R₂) = Ω₂.

This time the story is a little different because we can no longer ignore the non-linear term in the Navier-Stokes equation, (u·∇)u = −rΩ²ˆr. But this is something familiar, it is just the outward pointing centrifugal force that comes from the rotation of the fluid. It gives rise to a pressure gradient in the fluid, with the radial pressure P(r) obeying ∂P/∂r = rΩ² ⇒ Du/Dt = −∇P.

Such a flow obeys the Euler equation for any choice of Ω(r). But to satisfy the Navier-Stokes equation we must have, in addition, µ∇²u = 0. A quick calculation shows that ∇²u = (3Ω′/r + Ω′′)(y,−x,0) so the angular velocity of the flow must take the form Ω′′ = −3Ω′/r ⇒ Ω = A + B/r².

The first term is just a constant rotation, while the second term corresponds to the irrotational line vortex that we met in Section 2.2. The no-slip boundary conditions fix these coefficients to be A = (Ω₂R₂² − Ω₁R₁²)/(R₂² − R₁²) and B = (Ω₁ − Ω₂)R₁²R₂²/(R₂² − R₁²).

This circular Couette flow is also known as Taylor-Couette flow. (Taylor gets his name attached because he discovered certain instabilities in the flow.)

3.2.3 Poiseuille Flow Here’s another simple example. Again, take a fluid sitting between two, infinite parallel plates lying in the (x,y) plane. This time it will be slightly more convenient if we separate them by distance 2h in the z-direction. We take them to sit at z = ±h.

In contrast to Couette flow, both plates are now stationary. However, this time we induce a constant pressure gradient through the fluid dP/dx = constant. We again look for a steady, shear flow of the form u = (u(z),0,0). The Navier-Stokes equation is now µ d²u/dz² = dP/dx = constant.

With the no-slip boundary conditions u(z = ±h) = 0, the solution is u(z) = − (1/(2µ)) (dP/dx) (h² − z²) (3.12). This is known as Poiseuille flow. The minus sign is sensible: it tells us that if the pressure is greatest to the left, so dP/dx < 0, then the fluid moves to the right. Clearly the speed increases as we move away from the edges and is maximum in the middle where z = 0. Again, the flow has vorticity induced by the no-slip boundary condition.

The stress (3.5) is σ = -P(x) 0 zdP/dx 0 -P(x) 0 zdP/dx 0 -P(x)

and, perhaps surprisingly, is independent of the viscosity. The top and bottom plates have normal n = ±zˆ and sits at z = ±h, giving a force per unit area f = (h dP/dx, 0, ∓P(x)).

The force exerted by each plate is now in the negative x direction, as it should be.

Circular Poiseuille Flow A simple generalisation of this story describes flow down a circular pipe of radius R with a constant pressure gradient. We work in cylindrical polar coordinates, (r,θ,x) with ≠ 0 The velocity takes the form u = u(r)x̂ The Navier-Stokes equation is ∇²u = (1/μ) dP/dx ⇒ r d/dr(r du/dr) = (r/μ) dP/dx The solution with the appropriate boundary conditions is u(r) = - (1/(4μ)) (dP/dx) (R² - r²)

This is known as Hagen-Poiseuille flow.

3.2.4 Vorticity Revisited and the Burgers Vortex As our final example of a flow, we will look at something that swirls. This gives us the opportunity to revisit vorticity in the presence of viscosity. Previously we derived the vorticity equation (2.20) from the Euler equation. We can follow the same steps, now taking the curl of the Navier-Stokes equation to find Dω/Dt = (ω·∇)u + ν∇²ω (3.13)

This is the vorticity equation for a viscous fluid. The term due to viscosity, naturally written in terms of ν = μ/ρ, should be viewed as analogous to the diffusion term in the heat equation. Just as viscosity gives rise to diffusion of momentum, so it gives rise to diffusion of vorticity too. It is telling us that if there is some vorticity localised in some region of space, the viscosity will tend to make it diffuse into neighbouring regions. For example, if you blow a smoke ring then the size of the ring will grow over time as the vorticity diffuses into neighbouring regions.

For inviscid fluids, the Kelvin circulation theorem told us that Γ = ∫ u·dx over a curve C(t) that moves with the fluid doesn't change. You can check that the addition of the viscosity term means that the circulation is no longer conserved in the full Navier-Stokes equations.

Burgers Vortex To highlight how viscosity changes the physics, we can return to the vortex solution that we saw back in Section 2.2. There we looked at a combination of a strain and rotation, u = u_strain(x) + u_rot(x,t) with u_strain = α(-x, -y, 2z)

u_rot = f(r,t)(-y, x, 0)

The strain part of the flow stretches the fluid in the z-direction, while squeezing in the (x,y)-plane; the rotational flow clearly rotates in the (x,y)-plane, giving rise to a vorticity ω = (0,0,ω) with ω given by (2.16), ω = (1/r) d(r²f)/dr (3.14)

The vorticity equation (3.13) is a partial differential equation for ω, ∂ω/∂t - αr (∂ω/∂r) - 2αω = ν (1/r) ∂/∂r (r ∂ω/∂r) (3.15)

Previously we solved this equation when ν = 0 to find an example of vortex stretching (2.22). The solution we found was time dependent, with ω(r,t) = e^(2αt) W(r e^(αt)) and shows the magnitude of vorticity increasing exponentially, while being squeezed in the (x,y) plane so that the overall flux is conserved, in a way that is consistent with the circulation theorem.

Now we want to solve the vorticity equation with ν ≠ 0 to include the effect of viscosity. We already noted that the contribution ν∇²ω to the vorticity equation looks like a diffusion term. This suggests that we might be able to find a time independent solution in which the squeezing of vorticity is balanced by an outward diffusion caused by the viscosity. For steady solutions, the equation (3.15) becomes αr²ω + νr d/dr (r dω/dr) = 0 We can integrate once to get dω/dr = - (α/ν) r ω where we've set the integration constant to zero by requiring that ω and ω' decay suitably quickly asymptotically. This equation gives an exponentially localised vorticity ω(r) = (Γα/(2πν)) e^(-αr²/(2ν))

Here Γ is a constant that determines the overall magnitude of vorticity. The slightly strange combination of constants that accompany it ensure that Γ can also be identified with the asymptotic circulation of the flow, Γ = ∫ ω · dS = 2π ∫₀^∞ r ω(r) dr We can then solve (3.14) to get the associated profile function for the angular velocity, f(r) = (Γ/(2πr²)) (1 - e^(-αr²/(2ν)))

This is Burgers vortex solution. It is the simplest model for a hurricane.

We can compute the dissipation due to the vortex. We first rewrite our previous formula (3.9) as Dissipation = 2μ ∫ d³x E_ij E_ij = μ ∫ d³x |ω|² where some simple algebra shows that the difference is a boundary term which vanishes at infinity. It is now a simple computation to get the dissipation per unit length Dissipation per unit length = 2πμ ∫₀^∞ r ω² dr = (Γ²αρ)/(4π)

where the density ρ has made an appearance through μ = νρ. Curiously, for fixed circulation Γ, the dissipation is independent of the viscosity ν.

## 3.3 Dimensional Analysis

The Navier-Stokes equation is ∂u/∂t + u·∇u = -(1/ρ)∇P + ν∇²u (3.16)

Each term has dimension LT⁻². This means that the dimension of the kinematic viscosity ν is [ν] = L²T⁻¹ Fluid Kinematic Viscosity (m²s⁻¹) Dynamic Viscosity (Nsm⁻²)

Air 1.5×10⁻⁵ 1.8×10⁻⁵ Water 10⁻⁶ 10⁻³ Honey ~ 10⁻³ ~ 10 Pitch ~ 10⁵ ~ 10⁸ Table 1. The viscosities of some substances at room temperature.

Meanwhile, the dimension of dynamic viscosity μ = ρν is [μ] = ML⁻¹T⁻¹ Values of these viscosities for various fluids are shown in Table 1. To get a sense of the scales involved, we can do some further dimensional analysis. The kinematic viscosity has dimension of velocity times distance. For a fluid, the relevant internal velocity (as opposed to the velocity of some flow) is the speed of sound, c_s. On dimensional grounds, this is given by c_s ~ √(k_B T / m)

where T is the temperature, k_B is Boltzmann's constant and m is the mass of the constituent atom or molecule. (We'll derive this formula, together with the overall coefficient, in Section 4.4. You can also find a derivation in the lectures on Kinetic Theory.) Meanwhile, the relevant distance scale is the average separation a of atoms in the fluid. This suggests that the viscosity should be of order ν ~ c_s a For water, c_s ~ 1000 ms⁻¹, with a characteristic separation between molecules of a ~ 10⁻⁹ m. This gives ν ~ 10⁻⁶ m²s⁻¹ which is, indeed, in the right ballpark.

For some fluids, the internal molecular forces are strong, resulting in a much higher viscosity. Honey is a particularly familiar example. One of the most viscous fluids is pitch, also known as tar, which has a viscosity many orders of magnitude higher than water.

At the other end of the spectrum, superfluids, such as Helium-4 at low temperatures, have strictly zero viscosity. This is very much a quantum mechanical effect and a proper description requires us to leave the comfortable classical realm of these lectures.

3.3.1 The Reynolds Number Solving the Navier-Stokes equation (3.16) in full generality is, to put it mildly, a challenging problem. We make progress only by making some approximation. This involves deciding which terms, if any, can be ignored in any given situation. The obvious thing to do is to ask whether the viscosity is small or large. But this question in itself doesn't make any sense. Viscosity is dimensionful. There's no meaning to it being absolutely small or absolutely large. It can only be small or large relative to something else. That something else depends on the flow. Suppose that the flow has a characteristic speed U and length L. Here U could be the speed of the fluid relative to some boundary, or the rotational speed of the fluid. Similarly L could be some geometrical distance over which the flow changes. From this we can construct a dimensionless ratio called the Reynolds number Re = UL/ν (3.17)

Roughly speaking, this captures the relative importance of the inertial term u·∇u and the viscosity term ν∇²u, (inertial term) / (viscosity term) = |u·∇u| / |ν∇²u| ~ (U²/L) / (νU/L²) = U L / ν = Re With very broad brush, fluid flows can be characterised in one of two different types: • High Reynolds Number, Re ≫ 1: In this case, the flow is inertia dominated. In many cases, we can drop the viscosity term and return to the Euler equation that we studied in Section 2. Flows at high Reynolds number have an associated time scale that comes from equating the kinetic term ∂u/∂t with the inertial term. This time scale is simply the time it takes the fluid to move some distance: T ~ L/U.

For example, for the flow past an aircraft wing, U ~ 100 ms⁻¹ while L ~ 1 m is the width of the wing. Using the value ν ~ 10⁻⁵, we have Re ~ 10⁷ ≫ 1 which suggests that the viscosity term is unimportant for such flows.

However, this example also suggests that we should be nervous about such simple arguments. If we can really neglect viscosity at high Reynolds number then we run smack into the d'Alembert paradox that we met previously because, as we saw in Section 2.3, the Euler equation doesn't correctly capture the drag force that a fluid exerts on an object. Indeed, the argument that we can ignore the viscosity term is precisely what led to physicists being unable to understand how planes fly! We'll resolve these issues in Section 3.5 where we will see that, even at high Reynolds number, there can be situations where the viscosity term is important after all because it qualitatively changes certain aspects of the flow, in particular through the introduction of a so-called "boundary layer".

• Low Reynolds Number, Re ≪ 1: In this case, the flow is dominated by viscosity. If we ignore both the inertial term and the pressure term, then the Navier-Stokes equation becomes ∂u/∂t = ν∇²u (3.18)

As we've seen previously, this is heat equation that describes diffusion. It's telling us that flows at low Reynolds number exhibit diffusive transport of momentum, with the kinematic viscosity understood as a measure of momentum diffusivity. In this regime, the time scale associated to the flow is T ~ L²/ν.

For example, consider a bug of size L ~ 10⁻⁵ m moving in water. It could be bombing along at a whopping U ~ 10⁻⁵ ms⁻¹ – that's one body length every second – but the associated Reynolds number is Re ~ 10⁻⁵. This suggests that inertia is negligible and the motion is entirely governed by viscous forces. It's like swimming through treacle.

雷诺数Re仍约为10⁻⁴。在昆虫的世界里，黏性主导一切。我们将在第3.4节进一步探讨低雷诺数的世界。

其他无量纲比在不同情况下，我们可以构建更多无量纲比来表征流动并帮助我们对原方程做出良好近似。例如，如果流动具有某种特征时间尺度T——或许是因为流动受到了某种驱动——那么我们可以构建斯特劳哈尔数： Sr = UT / L 这也写作Sr = Lω/U，其中ω是振荡频率。斯特劳哈尔数告诉我们加速度项∂u/∂t ~ U/T与惯性项u·∇u ~ U²/L的相对重要性，当Sr ≫ 1时，加速度项占主导。

当我们加入更多力时，可以得到更多无量纲数。例如： • 欧拉数捕捉了压力梯度与惯性项的相对重要性：Eu = ∆P / (ρU²)

• 弗劳德数捕捉了惯性项~ U²/L与重力~ g的相对重要性：Fr = √(gL)

随着这些讲义的推进，我们将遇到其他无量纲量。在第4.6节，我们将遇到马赫数，它衡量流动速度与声速的比较；在第5.3节，我们将遇到瑞利数和普朗特数，当温差很重要时，这两者都扮演着角色。

3.3.2 标度律我们通过加入高阶导数项∇²u，将欧拉方程升级为纳维-斯托克斯方程。但如果我们乐于添加一个含有两阶导数的项，为什么不继续添加四阶导数项？或者十六阶导数项？为什么我们应该止步于此？

事实上，高阶导数项之所以无关紧要是有原因的，至少在足够大的距离尺度上观察是如此。（术语“无关紧要”在物理学语言中具有技术含义，但幸运的是，在此上下文中它与通常含义一致！）

为了看到这一点，注意在无任何外力的情况下，纳维-斯托克斯方程： ∂u/∂t + u·∇u = -∇P/ρ + ν∇²u 具有一种新颖的标度对称性： t → λ²t, x → λx, u → λ⁻¹u, P → λ⁻²P  (3.19)

在此标度下，整个纳维-斯托克斯方程乘以一个整体因子λ⁻³。但关键在于，所有项都以相同方式标度。这意味着，如果我们找到纳维-斯托克斯方程的一个解，那么我们总可以通过某个因子λ进行重新缩放，从而得到另一个解。因为空间坐标按x → λx缩放，随着λ增大，流动中的任何特征——例如涡旋——显然会变得更大。注意雷诺数（3.17）在此标度变换下是不变的：Re → Re。这在很大程度上是它之所以重要的原因：雷诺数是表征流动的一种标度不变的方式。

现在，假设你一时兴起，决定要在纳维-斯托克斯方程中加入更多项。你应该保留旋转对称性和伽利略变换（即u的常数平移），但除此之外你可以写任何你喜欢的项。你添加的项将包含一定数目的时间导数、空间导数以及场u和P的因子。示意性地，我们可能有： ∂u/∂t + u·∇u = -∇P/ρ + ν∇²u + O(∂ₜⁿ¹, ∇ⁿ², uⁿ³, Pⁿ⁴)

其中整数n_i（i=1,2,3,4）告诉我们出现的各种对象的数量。我们可以询问这个新项在标度对称性（3.19）下的表现如何。我们有： O(∂ₜⁿ¹, ∇ⁿ², uⁿ³, Pⁿ⁴) → λ⁻⁽²ⁿ¹ + n₂ + n₃ + 2ⁿ⁴⁾ O(∂ₜⁿ¹, ∇ⁿ², uⁿ³, Pⁿ⁴)

关键点在于，纳维-斯托克斯方程已经包含了主要项，每一项都按λ⁻³缩放。你试图构造的任何新项，其标度因子都比λ⁻³衰减得更快。这意味着，如果你试图将流动缩放到更大的长度尺度上，那么这些附加项在确定解的形式方面所起的作用将越来越小。特别地，在足够大的长度尺度上，它们总是不如出现在纳维-斯托克斯方程中的那些项重要。这就是我们说它们“无关紧要”的意思。

这并不是说高阶导数项在任何情况下都永远不重要。如果场的梯度足够大，那么高阶导数项当然会与其他项竞争。但它们需要多大？答案由这些高阶导数项的系数控制，这些系数表征了流体。从量纲分析来看，这些系数必须具有某些长度或时间量纲，相关尺度由某种微观相互作用设定。但这些新尺度很可能由微观物理设定——例如底层分子的平均自由程——并且我们当然不期望流体力学在存在如此尺度上的剧烈变化时仍然适用。

这段讨论的结论是，纳维-斯托克斯方程之所以特殊，是因为每一项都按λ⁻³缩放，而任何其他项总是更加“无关紧要”。因此，我们从不添加任何高阶导数项。相反，我们反其道而行之！在这些讲义剩余部分的大量工作中，我们将弄清楚在某些情况下可以忽略纳维-斯托克斯方程中的哪些项，以期方程最终能变得足够简单而得以求解。

## 3.4 斯托克斯流

在低雷诺数（Re ≪ 1）下，流动由黏性主导。在许多情况下，我们可以完全忽略物质导数Du/Dt：对于感兴趣的物理过程来说它并不重要。剩下的就是斯托克斯方程： ∇P = µ∇²u 和 ∇·u = 0  (3.20)

我们将这些视为四个未知数（u和P）的四个方程。当然，应该用无滑移边界条件来增补，这适用于我们这个超黏性的斯托克斯世界。在某些情况下，我们可能希望在第一个方程中添加额外的外力f。

斯托克斯方程的解被称为斯托克斯流，有时也称为蠕动流。它们描述了诸如微生物在水中游动等众多现象。在求解动力学方程时，缺少时间导数是不寻常的。这意味着流体对任何施加的力都会瞬时反应。在某种意义上，流体没有自己的“生命”，因为不存在传播的波。相反，它只是执行“指令”。更令人惊讶的是，缺少任何时间导数意味着任何流动都是可逆的。施加一个外力F一段时间，流体会演化。然后施加相反的力-F相同时间，它会再次演化回去，恢复到原始状态。有一些戏剧性的演示：在低雷诺数流体中滴入一些墨水。墨水不会分散，而只是停留在那里。然后搅动流体，墨水如预期那样旋转并与流体混合。但当搅拌反向时，混合也随之反向，直到墨水回到其原始起点⁴。这种行为通常是热力学第二定律所禁止的。但在低雷诺数下，情况有所不同。

这种可逆行为有些令人不安。部分原因在于，正如我们上面所见，流体中的耗散仅因黏性而产生。这意味着流体中的熵增也源于黏性。然而，当黏性完全占主导时，动力学变得可逆，熵没有增加！或者，更准确地说，由于我们忽略了时间导数项，根本就没有动力学过程。

⁴这是一个相当精彩的视频，演示了这种效应。也可以在一部老派纪录片中看到，伟大的流体动力学家G.I. Taylor亲自进行了搅拌。

求解斯托克斯方程在本节的剩余部分，我们将在几种不同的环境中探讨斯托克斯流。我们可以进行一些简单的运算来突出斯托克斯方程的数学结构。对∇P = µ∇²u两边取散度，并利用∇·u = 0的事实，可知压力必然是调和函数： ∇²P = 0  (3.21)

同时，对两边取旋度告诉我们涡量ω = ∇×u也是调和的： ∇²ω = 0  (3.22)

最后，对两边作用∇²，并利用∇²P = 0的事实，表明速度本身是“双调和”的，即： ∇⁴u := ∇²∇²u = 0 在某些情况下，这是求解方程的一个有用起点。但对于我们的第一个应用，我们将采用不同的路径。

3.4.1 球体绕流我们想重复第2.3节中为无黏流体所做的关于球体绕流的计算。在那种情况下，我们通过将均匀流与偶极子流叠加，并将奇点隐藏在球体后面来求得解。因为斯托克斯方程是线性的，类似的策略很可能再次奏效，现在针对高黏性流体。我们将看到确实如此，尽管某些细节有所改变。

为了启动，我们将寻找方程组（3.20）的格林函数。这是一个速度场u和一个压力P，满足： µ∇²u - ∇P = -aδ³(x)  (3.23)

以及∇·u = 0的要求。方程（3.23）的右边包含一个任意向量a。

结论：斯托克斯方程组的格林函数是： u = G a 和 P = (x·a) / (4πr³)  (3.24)

其中G是矩阵： G = (1/(8πµ)) * (δᵢⱼ/r + xᵢxⱼ/r³)

张量G被称为斯托克斯子（Stokeslet）。

G中的两项协同确保∇·u = 0。斯托克斯子流场如图所示，其中a = ẑ指向右方。

证明：首先，我们将验证解（3.24）在除r=0外的所有地方都满足µ∇²u = ∇P。然后我们将验证德尔塔函数的系数是正确的。

首先看速度项。我们有： µ∇²u = ∇² [ (aᵢ + (xᵢ xⱼ aⱼ)/r²) / (8πr) ]  —— 原始推导有误，按原文公式复原应为：µ∇²u = ∇² [ (a_i/r) + (x_i x_j a_j)/r³ ] / (8π)

我们认出第一项1/r是∇²的格林函数（我们在第2.3节讨论势流时已经遇到过这个解释），其中∇²(1/r) = -4πδ(x)。显然这对方程（3.23）右边的德尔塔函数有贡献，但系数仅为1。我们将看到…… at another 1 comes from the other terms. Staying away from \( r = 0 \) for now, a little bit of algebra is needed to differentiate the second term twice. We have \[ \mu \nabla^2 u_i = \partial_j \partial_j \left( \frac{1}{8\pi} \frac{x_i x_j a_j}{r^3} \right) = \frac{1}{4\pi} \left( \frac{a_i - 3 x_i x_j a_j / r^2}{r^3} \right) \quad \text{for } r \neq 0 \tag{3.25} \]

But now it’s simple to check that this is cancelled by the pressure \[ (\nabla P)_i = \partial_i P = \frac{1}{4\pi} \left( \frac{a_i - 3 x_i x_j a_j / r^2}{r^3} \right) \quad \text{for } r \neq 0 \]

So we do indeed have a solution to (3.23) away from the origin. Now we just need to check that the \( 1/8\pi \) normalisation of \( G \) gives the correct strength for the delta function. For this we integrate over a ball of radius \( R \) centred at the origin, and use the divergence theorem to convert this into an integral over the sphere \( S^2 \) of radius \( R \), \[ \int (\mu \nabla^2 u_j - \partial_j P) d^3x = \int_{S^2} \left( \mu \partial_i G_{jk} a_k - \delta_{kj} a_j \right) d^2 S_i \]

\[ = \frac{a_j}{8\pi} \int_{S^2} d^2 S_i \left( \partial_{kj} + \delta_{kj} \left( \frac{x_i}{r} - \frac{2x_i}{r} \right) \right)

\]

\[ = \frac{a_j}{8\pi} \int_{S^2} d^2 S_i \left( - \frac{\delta_{jk} x_i}{r^3} - \frac{\delta_{ik} x_j}{r^3} + \frac{\delta_{ij} x_k}{r^3} - \frac{3x_i x_j x_k}{r^5} \right)

\]

At this stage, it’s all about the placement of indices. The first term is straightforward: it is the usual integral of a radial field over a sphere and gives \[ \frac{a_j}{8\pi} \int_{S^2} d^2 S_i \left( - \frac{\delta_{jk} x_i}{r^3} \right) = - \frac{1}{2} a_k \]

This is the same factor of \( 1/2 \) contribution that we noted above. The remaining three terms in the integral must, ultimately, be proportional to \( \delta_{kj} \) because that’s the only invariant tensor available. A standard trick (see, for example, the lectures on Vector Calculus) is to take the trace over \( k \) and \( j \) indices and evaluate the integral: this then gives \( 3\times \) the coefficient in front of \( \delta_{kj} \). If we do this, we find that the second and third terms cancel, while the final term is \[ \frac{a_j}{8\pi} \int_{S^2} d^2 S_i \left( - \frac{3 x_i x_j x_k}{r^5} \right) = - \frac{1}{2} a_k \]

That’s the extra factor of \( 1/2 \) that we were looking for. We learn that our flow and pressure do indeed satisfy (3.23). □

Given a basic solution like (3.23), we can always generate further solutions by differentiating. These solutions will be more singular at the origin, but drop off quicker asymptotically. This is how the dipole solution is generated for potential flow (and, in fact, for electromagnetism). And it turns out to be what we need to solve our problem of the sphere. The relevant flow is again referred to as a dipole and is given by \[ u_{\text{dipole}} = (\nabla^2 G) a \quad \text{with} \quad (\nabla^2 G)_{ij} = \frac{1}{4\pi\mu} \left( \delta_{ij} - \frac{3 x_i x_j}{r^2} \right)

\]

where we computed \( \nabla^2 G \) previously in (3.25). The associated pressure field is simply \( P_{\text{dipole}} = 0 \) because, as we saw in (3.21), the original pressure (3.23) is necessarily a harmonic function.

We now have all the ingredients to solve our problem of interest: a Stokes flow around a sphere of radius \( R \). Importantly, this flow must satisfy the no-slip condition which means that \( u = 0 \) for all \( |\mathbf{x}| = R \).

We start with a superposition of the different flows that we’ve found. We take a constant flow \( u = U \), together with some combination of the Stokeslet and dipole flows. Both the latter flows involve some constant vector \( a \) and, on symmetry grounds, this must be proportional to the asymptotic velocity \( U \). We’re left with \[ u = U + \frac{1}{4\pi\mu} (\alpha G + \beta \nabla^2 G) U \]

\[ = U \left( 1 + \frac{\alpha}{2r} + \frac{\alpha \beta}{r^3} + \frac{\alpha}{2r^3} (U \cdot x) x - \frac{3 \alpha \beta}{r^5} (U \cdot x) x \right)

\]

where \( \alpha \) and \( \beta \) are constants that are fixed by the boundary condition on the sphere. As we’ve seen, this requires that \( u = 0 \) when \( |x| = R \), which is achieved only if both terms are individually vanishing. So we must have \[ \beta = \frac{R^2}{6} \quad \text{and} \quad \alpha = - \frac{3R}{2} \]

so our final flow for a very viscous fluid around a sphere is \[ u = U \left( 1 - \frac{3R}{4r} - \frac{R^3}{4r^3} + (U \cdot x) x \left( \frac{3R}{4r^3} + \frac{3R^3}{4r^5} \right) \right) \tag{3.26} \]

This is shown in Figure 10. By eye, the flow outside the sphere doesn’t look wildly different from the potential flow that we saw in Section 2.3. But there is a key difference that is clear if you look closely at the left-hand figure, before we placed the sphere over it. The fluid inside is moving in the opposite direction to the flow outside. (In contrast, for the potential flow shown in Figure 7, the fluid inside moves in the same direction as the fluid outside.) This is what ensures the existence of a surface \( r = R \) for which the flow is strictly vanishing, as befits the no-slip boundary condition. This, it turns out, makes a big difference.

The difference first manifests itself in the pressure field, which is \[ P = P_\infty - \frac{3}{2} \mu U \cdot x / r^3 \]

If we take \( U = U \hat{z} \) and work in spherical polar coordinates, the pressure on the surface of the sphere is \[ P = P_\infty - \frac{3U\mu \cos\theta}{2R} \]

This means that the pressure is bigger than \( P_\infty \) on the front of the sphere (the left in the figure) where \( \pi/2 < \theta \leq \pi \) and \( \cos\theta < 0 \). The pressure is less than \( P_\infty \) at the back of the sphere where \( 0 \leq \theta < \pi/2 \). This, of course, sounds very reasonable: it’s simply because the flow is exerting pressure on the sphere. But it was this simple physics that was noticeably absent in the potential flow of Section 2.3 (see equation (2.31) for the analogous equation in that case). This is the first hint that we may be on the way to finally understanding the drag force.

### Such a Drag

The pressure is not the only force that the sphere experiences. The technology to compute the drag force comes from the stress tensor (3.5)

\[ \sigma_{ij} = -P \delta_{ij} + 2\mu E_{ij} \]

where \( E_{ij} \) is the rate of strain tensor. We can compute this for the flow (3.26). It simplifies somewhat when evaluated on the surface of the sphere: \[ E_{ij}(|\mathbf{x}| = R) = \frac{3}{4R^2} (U_i x_j + U_j x_i) - \frac{3}{2R^4} (U \cdot x) x_i x_j \]

To compute the force experienced by any point on the sphere, we consider \( \sigma_{ij} n_j = \sigma_{ij} (x_j / R) \) where \( n = x/R \) is the unit normal to the surface of the sphere. Using our expressions above, we have (ignoring the asymptotic pressure \( P_\infty \) which has no net effect on the sphere), \[ \sigma_{ij} n_j = \frac{3\mu (U \cdot x) x_i}{2R^3} + 2\mu \left( \frac{3U_i}{4R} - \frac{3(U \cdot x) x_i}{4R^3} \right)

\]

We see that, rather nicely, the first term from the pressure cancels the final term from the strain. This means that the force acting on any point of the sphere is constant, and in the direction \( U \) of the asymptotic flow \[ \sigma_{ij} n_j = \frac{3\mu}{2R} U_i \]

It’s now very easy to compute the drag force: we just integrate this over the whole sphere, getting an additional factor of the surface area \( 4\pi R^2 \). The total drag force acting on the sphere is \[ \text{Drag Force} = 6\pi\mu R U \tag{3.27} \]

This is known as Stokes’ law. It is the drag experienced by a sphere moving at very low Reynolds number.

### 3.4.2 Uniqueness and the Minimum Dissipation Theorem

We found a solution for the flow around the sphere. But it turns out that it is *the* solution: there is no other with the same boundary conditions. This follows from a uniqueness theorem that is proven in the same way as the uniqueness of solutions to the Laplace equation (see the lectures on Vector Calculus).

Suppose that we have two solutions, \( u_1 \) and \( u_2 \), both obeying non-slip boundary conditions on the surface. Then the difference \( v = u_1 - u_2 \) necessarily vanishes on the boundary. With \( \tilde{P} = P_1 - P_2 \) the difference in the pressure fields, we have \[ 0 = \int v \cdot (\mu \nabla^2 v - \nabla \tilde{P}) dV = \int_{\partial V} \mu v_j (\partial_i v_j - \partial_j v_i) dS_i - \int_V (\partial_j v_i)^2 dV \]

The first term on the right-hand side vanishes because it’s a total derivative and \( v = 0 \) on the boundary \( \partial V \). Moreover, the second term is the integral of a total square so this can be zero only if the integrand vanishes: \( \partial_j v_i = 0 \). Hence \( v = 0 \) everywhere and our original solutions \( u_1 \) and \( u_2 \) were the same.

### Stokes Flow Dissipates Less Than Any Other Flow

Here’s a cute mathematical result. Among all the incompressible flows with the same boundary condition, the Stokes flow dissipates the least energy.

To prove this, suppose that we have a solution \( u \) and \( P \) to the Stokes equations with no external force (3.20), and a second flow \( \tilde{u} \) that satisfies the same boundary conditions but is otherwise arbitrary. Recall from (3.9) that the energy dissipated by an arbitrary flow \( \tilde{u} \) is (3.9)

\[ \text{Dissipation} = 2\mu \int \tilde{E}_{ij} \tilde{E}_{ij} dV \]

\[ = 2\mu \int \left[ E_{ij} E_{ij} + (\tilde{E}_{ij} - E_{ij})^2 + 2 E_{ij} (\tilde{E}_{ij} - E_{ij}) \right] dV \]

\[ \geq 2\mu \int \left[ E_{ij} E_{ij} + 2 E_{ij} (\tilde{E}_{ij} - E_{ij}) \right] dV \]

\[ = \text{Stokes Dissipation} + 4\mu \int E_{ij} (\tilde{E}_{ij} - E_{ij}) dV \]

We’ll now show that this second integral actually vanishes. To see this, recall that the stress tensor for the Stokes flow is \[ \sigma_{ij} = -P \delta_{ij} + 2\mu E_{ij} \]

Importantly, the stress tensor is divergence free for the Stokes flow, \[ \partial_i \sigma_{ij} = -\partial_j P + \mu \nabla^2 u_j = 0 \tag{3.28} \]

where the other term in \( E_{ij} \) vanishes because it involves \( \partial_i u_i = 0 \) and the whole thing is equal to zero by virtue of the Stokes equations. This is the special property of the Stokes flow that we need. If we now contract the Stokes stress with the strain tensor \( E_{ij} \) for any other flow, we have \[ \sigma_{ij} \tilde{E}_{ij} = 2\mu E_{ij} \tilde{E}_{ij} \]

where the other term \( -P \tilde{E}_{ii} \) vanishes because the flow is incompressible and \( \tilde{E}_{ii} = \nabla \cdot \tilde{u} \). We now have \[ 4\mu \int E_{ij} (\tilde{E}_{ij} - E_{ij}) dV = 2 \int \sigma_{ij} (\tilde{E}_{ij} - E_{ij}) dV \]

\[ = 2 \int \sigma_{ij} (\partial_i \tilde{u}_j - \partial_j \tilde{u}_i) dV \]

\[ = 2 \int \partial_i [\sigma_{ij} (\tilde{u}_j - u_j)] dV = 0 \]

where, in the second line, we’ve used the fact that \( \sigma_{ij} \) is symmetric and, in the final line, we’ve used the special property of the Stokes flow (3.28), together with the divergence theorem which means that the integral only cares about the boundary where, by assumption, \( \tilde{u} = u \). The upshot is that for any flow \( \tilde{u} \) that is not a Stokes flow, we necessarily have \[ \int \tilde{E}_{ij} \tilde{E}_{ij} dV > \int E_{ij} E_{ij} dV \]

The dissipation from other flows is always greater than the corresponding Stokes flow. This is the Helmholtz minimum dissipation theorem.

There is, it turns out, a deep relationship between drag and dissipation, known as the fluctuation dissipation theorem. (We describe this in...

the lectures on Kinetic Theory.)

The fact that the Stokes flow has the smallest dissipation translates into the statement that it also results in the smallest drag. This means that, as we increase the Reynolds number, the drag on the sphere will only increase beyond that given by Stokes law (3.27). Indeed, one can set up a perturbation expansion to understand the effects of the terms in the Navier-Stokes equation that we neglected. This is an expansion in the Reynolds number Re ≪ 1 and the leading order term turns out to be Drag Force = 6πµRU 1+ Re+...

3.4.3 Eddies in the Corner As you might imagine, there are many different flows that exhibit interesting properties. Here is another one. We simply look at fluid passing around a corner. This corner has an opening angle that we denote as 2α. We want to know what happens.

This problem is effectively two-dimensional and can be solved quite straightforwardly by working in cylindrical polar coordinates and introducing a stream function Ψ(r,θ). Recall from Section 1.1.4 that the stream function allows us to construct a vector field A = Ψẑ and, from that, an incompressible flow u = ∇ × A. In cylindrical polar coordinates, the resulting flow is u = 1/r ∂Ψ/∂θ ŕ − ∂Ψ/∂r θ̂ (3.29)

The associated vorticity is ω = ∇×u = −(∇²Ψ)ẑ with ∇²Ψ = 1/r ∂/∂r (r ∂Ψ/∂r) + 1/r² ∂²Ψ/∂θ² But we’ve seen in (3.22) that the vorticity ω is harmonic for Stokes flows, which means that the stream function must be biharmonic ∇⁴Ψ = ∇²(∇²Ψ) = 0 The form of the equation suggests that it might be fruitful to look for scale-invariant, separable solutions of the form Ψ(r,θ) = r^λ f(θ)

for some exponent λ and some function f(θ). The biharmonic condition then becomes a differential equation for f, ∇⁴Ψ = r^{λ-4} [∂²/∂θ² + λ² + (λ-2)²] f(θ) = 0 The solution is simply f(θ) = Asin(λθ) + Bcos(λθ) + Csin((λ-2)θ) + Dcos((λ-2)θ)

with four integrations constants as well as the exponent λ still to be determined. At this point we bring out some boundary conditions. We’ll arrange the geometry so that the boundaries lie at θ = ±α. The fluid comes in close to one boundary, and out close to the other, meaning that the radial component of the flow should be an odd function of θ. The expression (3.29) then tells us that the stream function should be an even function of θ, so A = C = 0.

We now have two further boundary conditions since both components of u must vanish along the boundary. The requirement that no fluid moves into the boundary is ∂Ψ/∂r |_{θ=±α} = 0 ⇒ Bcos(λα) + Dcos((λ-2)α) = 0 Meanwhile, the no-slip condition tells us that ∂Ψ/∂θ |_{θ=±α} = 0 ⇒ Bλsin(λα) + D(λ-2)sin((λ-2)α) = 0 Or, combined, λ sin(λα) cos((λ-2)α) = (λ-2)cos(λα) sin((λ-2)α)

This equation always has the solution λ = 1, but the conditions above tell us that if λ = 1 then B = −D and, correspondingly, Ψ = 0. This is not what we want. So we’ll look for solutions with λ ≠ 1. Expand each sin and cos above in terms of ei(whatever) and rearrange to get sin²((λ-1)α) / (λ-1) = −sin²(2α)

This equation determines the exponent λ in terms of the opening angle of the corner 2α, admittedly in a slightly opaque form. To understand what it’s telling us, write x = 2(λ-1)α, so the equation becomes sin(x)/x = −sin(2α)/(2α) (3.30)

Suppose that the opening angle α is small. Then, as you can see from Figure 11, the value of sin(2α)/(2α) is large. But there is no value of x for which sin(x)/x has the equal negative value. So for small opening angles, we can’t solve (3.30), at least not for real x.

As the opening angle gets bigger, we do get solutions. The smallest value of sin(x)/x occurs at the first minimum, which sits at x ≈ 1.43π ⇒ sin(x)/x ≈ −0.217 This corresponds to a value of 2α given by 2α ≈ 0.813π ≈ 146◦ ⇒ sin(2α)/(2α) ≈ +0.217 We learn that there is a critical value of the opening angle, given by 2α_crit ≈ 146◦

For opening angles larger than this, we can find solutions to (3.30). A contour plot of the stream function for 2α = 160◦ is shown in the figure to the right. The lines of constant value are the streamlines and they simply flow around the corner undisturbed.

What happens when the opening angle is smaller than 146◦? Now, no solutions to (3.30) exist. Or, said more precisely, no real solutions exist! There are, however, always complex solutions. For example, suppose that we have a right angle corner, with 2α = π/2 < 2α_crit. Then there is an infinite sequence of complex solutions to (3.30), starting with λ ≈ 3.74+1.12i, λ ≈ 7.84+1.66i, ...

What is the interpretation of these solutions? If we have a solution with λ = λ_1 + iλ_2 then, because the velocity (3.29) is a linear function of Ψ, we can take the real part of the stream function to get Ψ(r,θ) = Re[ r^λ f(θ) ] = r^{λ_1}[cos(λ_2 log r)Re(f(θ)) − sin(λ_2 log r)Im(f(θ))]

That cos(log r) behaviour is striking! For a fixed angle θ, it gives rise to increasingly wild oscillations as r → 0, albeit with decreasing amplitude because of the overall r^{λ_1} scaling. You can check that this means that the angular velocity u·θ is also oscillating in sign as r → 0. This is telling us that the flow no longer takes the simple form, as shown in the figure for large opening angle, but instead develops eddies. In fact, there are an infinite number of these eddies, becoming increasingly small as r → 0. These are known as Moffatt eddies.

The stream function for a right-angle corner is shown in the figure, clearly exhibiting one such eddy. The logarithm means that both the size of the eddies, and the amplitude of the stream function, vary exponentially. The centres of consecutive eddies lie at λ_2 log(r_{n+1}) = λ_2 log(r_n) − π ⇒ r_{n+1} = e^{-π/λ_2} r_n and this also characterises the size of the eddies. (If you squint, you can just see a second eddie in the figure centred around x ≈ 0,2.) Meanwhile, the size of the stream function scales as |Ψ(r_{n+1})| / |Ψ(r_n)| ∼ (r_{n+1}/r_n)^{λ_1} = e^{-λ_1 π/λ_2} The magnitude of velocities involves a derivative of stream function, u ∼ ∂Ψ/∂r, and so scale as (r_{n+1}/r_n)^{λ_1-1} = e^{-(λ_1-1)π/λ_2}. For the right-angle corner shown in this figure, this ratio is around 2000. This exponential scaling doesn’t just make it difficult to plot the eddies; it also makes it difficult to experimentally observe more than two or three.

Although the eddies get smaller as you approach the vertex, the flow also becomes slower so it takes significantly longer for a particle to orbit the smaller eddies than the larger ones.

3.4.4 Hele-Shaw Flow In this short section, we look at a particular way of restricting Stokes flow to two dimensions. However, rather than simply solving the 2d version of Stokes equations, we instead do something more physical. We trap the fluid between two parallel, stationary plates, separated by a distance h. This scale will be much smaller than any other scale, such as the size of any object that the fluid moves around.

We separate the plates in the z-direction and consider situations in which the fluid flows only in the (x,y)-plane u = (u(x,y,z), v(z,y,z), 0)

and we now solve the Stokes equation ∇P = µ∇²u The first thing to realise is that gradients in the z direction are of order ∂/∂z ∼ 1/h and so are much bigger than anything else. (These gradients can’t vanish because the no-slip condition means that u vanishes at z = 0 and z = a but we want it to be non-vanishing in the middle.) We work in the approximation that these z-gradients are entirely accounted for by the pressure µ ∂²u/∂z² = ∇P ⇒ u = (z(z −a)/2µ) ∂P/∂x and v = (z(z −a)/2µ) ∂P/∂y where the boundary conditions have been chosen so that the no-slip condition is satisfied. This is the same kind of velocity profile that we saw for Poiseuille flow (3.12), but now in 2d rather than 1d. In the present context, it is known as Hele-Shaw flow. (One person, not two! He chose, I think rather unusually, to adopt both his father’s and his mother’s name.)

But Hele-Shaw flow is something very familiar: we have a situation where the 2d velocity field u_2d = (u,v) is given by u_2d = ∇_2d ϕ with ϕ(x,y;z) = P(x,y) z(z −a)/(2µ)

and with ∇_2d = (∂_x, ∂_y). In other words, we’re back in the realm of 2d potential flow that we solved in Section 2.4. This means, for example, that if you place a cylinder between the plates, with its axis pointing in the z-direction, then the velocity flow around it coincides with the velocity (2.34) that we previously calculated.

There is an irony here. We originally introduced potential flow as a description of completely inviscid fluids. Yet the same solutions also describe extremely viscous fluids when sandwiched between plates! In fact the irony runs deeper. If you attempt to go to a regime where viscosity can be neglected – which means high Reynolds number – then another effect, known as the boundary layer, kicks in and the flows don’t look at all like potential flows near objects. (We describe this in Section 3.5.) So, in fact, the only way to genuinely manufacture the inviscid potential flows of Section 2.4 is to work with very viscous fluids.

There is, however, a difference between Hele-Shaw flows and the general 2d potential flow. Hele-Shaw flows can have no circulation in the (x,y)-plane, Γ = ∮ u·dx = 0 This is because, as we showed in Section 2.4, circulation arises only from potentials that are not single-valued. In contrast, the potential for Hele-Shaw flows is effectively the pressure P(x,y) and this is certainly single-valued. The upshot is that Hele-Shaw flows don’t include those flows shown in Figure 8 which induce a lift force on the obstacle.

3.4.5 Swimming at Low Reynolds Numb Given the obvious constraints of their biology, scallops are remarkably elegant swimmers (5 as this video shows). They open their shells, then quickly close them, forcing water out through the hinges to propel themselves forward.

This strategy works in the ocean. But it would be hopeless at low Reynolds number. This is because, as we mentioned at the beginning of this section, the lack of time derivatives in the Stokes equations means that motion at low Reynolds number is reversible. When friction dominates, the speed at which a scallop opens or closes its shell is irrelevant. It moves in one direction when the shell opens, and comes back the same amount when it closes. A scallop dropped in honey can no longer swim. Although it surely tastes nice.

To swim at low Reynolds number, you need a different strategy. You can’t just flap your arms (or your legs or your fins) back and forth, because what is done by the forward flap is undone by the backward one. Instead, you need to change your shape in some way that is not, itself, time reversible. In other words, you need something like breaststroke.

Such non-reversible strategies have been developed by micro-organisms living in water, for whom life is lived at low Reynolds number. For example, the bacterium E. coli has a helical flagellum which rotates to make it swim (6 A number of videos of micro-organisms swimming can be found on the webpage of Howard Berg, one of the pioneers of low Reynolds number physics. The story is described further in a famous and charming paper by E. Purcell called “Life at Low Reynolds Number”. The underlying theory is closely related to the rotation of deformable (as opposed to rigid) bodies that is covered in the lectures on Classical Dynamics).

In this section, we describe a very simple model that captures the essence of swimming at low Reynolds number. It also captures the tension between finding a mathematical model that is easy to solve, and finding one that looks vaguely like a living creature.

An Infinite, Wavey Plate As our proxy micro-organism, we take an infinite thin plate, lying in the (x,z)-plane. (Admittedly, this object is unlikely to make a good pet.) The plate “swims” by wriggling so that a wave passes down in the x-direction, meaning that the position of the plate in the y-direction, which is perpendicular to the flat plate, is y(x) = Asin(kx−ωt)

Here A is the amplitude of the wave, which has wavenumber k and frequency ω. Said another way, the wave has wavelength λ = 2π/k and travels with speed c = ω/k.

We want to understand the flow that results from this wriggling. Our goal is to show that the wriggling induces a constant asymptotic velocity in the fluid. This isn’t quite swimming of course: it’s staying still and making all the universe move around you. But, by Galilean relativity, this is equivalent to the fluid staying still and the plate moving. And that’s what we mean by swimming.

To proceed, we introduce a stream function Ψ(x,y), so that u = (u,v,0) with u = ∂Ψ/∂y and v = −∂Ψ/∂x. Repeating the argument that we saw for corner flows, we know that ω = ∇ × u = −∇²Ψ ẑ and ∇²ω = 0, which, combined, tell us that ∇⁴Ψ = 0.

We must solve this, subject to the no-slip requirement that the velocity of the flow matches that of the plate, u = 0 and v = −Aωcos(kx−ωt) on y = Asin(kx−ωt) (3.31)

We’ll also impose suitable boundary conditions asymptotically. We’ll flag these up as we go along.

Simple as the equations above are, it’s not straightforward to solve them because the boundary condition (3.31) is evaluated on the waving plate. To proceed, we need an approximation. Roughly speaking, we want the amplitude of the wave A to be small in the hope that the boundary condition is easier to implement. But A is dimensionful, so it has to be small relative to something else and the only other length scale we have is the wavelength. So the relevant dimensionless expansion parameter is ε = Ak ≪ 1.

To understand how to write our equations in terms of a Taylor expansion, it’s useful to introduce dimensionless distances and a dimensionless stream function ˜x = kx, ˜y = ky, ˜Ψ = kΨ/(Aω).

The boundary conditions (3.31) then become ∂˜Ψ/∂˜y = 0 and ∂˜Ψ/∂˜x = cos(˜x−ωt) on ˜y = εsin(˜x−ωt).

Now we can see that, for ε ≪ 1, we do indeed impose the boundary condition on a value of ˜y that is small. It means that we can Taylor expand the function ˜Ψ around ˜y = 0, so these boundary conditions read (∂˜Ψ/∂˜y)|_{˜y=εsin(˜x−ωt)} = (∂˜Ψ/∂˜y)|_{˜y=0} + εsin(˜x−ωt) (∂²˜Ψ/∂˜y²)|_{˜y=0} + ... = 0 (3.32)

and (∂˜Ψ/∂˜x)|_{˜y=εsin(˜x−ωt)} = (∂˜Ψ/∂˜x)|_{˜y=0} + εsin(˜x−ωt) (∂²˜Ψ/∂˜x∂˜y)|_{˜y=0} + ... = cos(˜x−ωt) (3.33)

We now expand the stream function itself in powers of ε, ˜Ψ = ˜Ψ₀ + ε˜Ψ₁ + ...

Each ˜Ψₙ is biharmonic, meaning that it satisfies ∇⁴˜Ψₙ = 0 for n = 0,1,2,.... But each ˜Ψₙ obeys different boundary conditions at ˜y = 0. We start with ˜Ψ₀ which has boundary conditions ∂˜Ψ₀/∂˜y = 0 and ∂˜Ψ₀/∂˜x = cos(˜x−ωt) on ˜y = 0.

The biharmonic function obeying these boundary conditions in the region above the plate, ˜y > 0, is ˜Ψ₀ = (1+˜y)e^{−˜y}sin(˜x−ωt) (3.34), which obeys ∇²˜Ψ₀ = −2e^{−˜y}sin(˜x − ωt) and so ∇⁴˜Ψ₀ = 0. Note that we’ve thrown away a similar solution that scales as e^{+˜y} on the grounds that it gives an unbounded velocity field as ˜y → +∞. A solution of this kind is relevant below the plate for ˜y < 0.

The first correction to this solution is ˜Ψ₁ which, from (3.32) and (3.33), obeys ∂˜Ψ₁/∂˜y + sin(˜x−ωt) ∂²˜Ψ₀/∂˜y² = 0 and ∂˜Ψ₁/∂˜x + sin(˜x−ωt) ∂²˜Ψ₀/∂˜x∂˜y = 0. Both boundary conditions should again be imposed at ˜y = 0. Using our solution (3.34) for ˜Ψ₀, these become ∂˜Ψ₁/∂˜y = sin²(˜x−ωt) and ∂˜Ψ₁/∂˜x = 0 on ˜y = 0.

The sin² term is where our interest lies. We decompose this into Fourier modes by using the double angle formula sin²˜x = (1−cos2˜x)/2. The cos2˜x term is just telling us that the second harmonic is excited. That’s little surprise. The constant term is more interesting as it tells us that there must be a constant component to the fluid motion. Indeed, you can check that the biharmonic function obeying these boundary conditions is ˜Ψ₁ = (1/2)˜y − (1/2)˜ye^{−2˜y}cos(2(˜x−ωt)).

Again, this solution holds above the plate for ˜y > 0. There is again an analogous solution with a e^{+˜y} below the plate but with the same constant (1/2)˜y term. That linear term is what we’re after. Putting the various constants back in, it gives a contribution to the stream function that looks like Ψ = (1/2)A²k²cy + ... where the ... are the oscillatory terms that drop off as e^{−ky} or e^{−2ky} as we move away from the plate. The constant term is telling us that, far away from the plate, there is necessarily a constant fluid velocity u → (1/2)A²k²c x̂ as y → +∞.

Alternatively, if we boost to another frame so that the fluid is asymptotically stationary, then the plate must be moving to the left with speed U = (1/2)A²k²c. In other words, the plate is swimming. The speed is proportional to the speed c with which waves propagate down the plate but, at least in this approximation, suppressed by ε² = A²k² ≪ 1.

## 3.5 The Boundary Layer

In the previous section, we focussed on very viscous flow at low Reynolds number. Now we turn to the opposite regime of high Reynolds number. We’re going to revisit the question of flows around some fixed object, like a sphere or the wing of an aircraft. When the Reynolds number is large, the inertia term in the Navier-Stokes equation should dominate over the viscosity term, Re = inertial term |u·∇u| / viscosity term |ν∇²u| ≫ 1.

For example, for a plane flying we have Re ∼ 10⁷. Given this, it’s tempting to think that we can drop the viscosity term completely. But this brings us back to the Euler equation and, as we have seen in Section 2, inviscid flows do not give rise to any drag on an object. Something is amiss! In fact it turns out that, no matter how small the viscosity, it still plays an important role.

Mathematically this is because the character of the Navier-Stokes equation changes if we set ν = 0. With ν ≠ 0, we have an equation that is second order in spatial derivatives. When ν = 0, it changes to an equation that is first order. As we have commented previously, this means that we must impose two boundary conditions when solving the ν ≠ 0 Navier-Stokes equation, but only a single boundary condition when solving the Euler equation. The boundary condition that is expendable is the no-slip condition and, in its absence, solutions exhibit no drag force. However, as soon as we have ν, no matter how small, we’re back in business and we can impose the no-slip condition to our heart’s content.

Physically, a continuous flow with a no-slip boundary condition must have a layer of almost-stationary fluid sitting next to the object. This is the boundary layer. The purpose of this section is to understand some of its properties.

We can make progress with some simple dimensional analysis, coupled with a little intuition built on what we’ve learned so far. For example, one of the most basic questions that we can ask is: what is the width of the boundary layer? It seems plausible that when the fluid first hits the leading edge of the object, only those molecules immediately in contact know about its existence. But, as we look further down the flow, more and more of the fluid should be affected. How much?

Suppose that our object has length L, and travels relative to the fluid with speed U. The Reynolds number is then Re = UL/ν. By assumption, Re ≫ 1.

Any fluid element takes a time T = L/U to move past the object. Close to the object, the fluid will be affected by the no-slip condition and it is reasonable to think that the near-boundary behaviour...

mimics that of Couette or Poiseuille flow. One of the simple, yet important facts about these flows is that they have vorticity, as the fluid near the boundary travels at different speeds. And we know from the vorticity equation (3.13) that viscosity causes vorticity to diffuse, with diffusion constant ν. Importantly, diffusion spreads as time rather than linearly in time. This means that in the time scale T, the vorticity will diffuse a distance δ ∼ νT ∼ √(νL) ∼ √(L/Re) (3.35)

This is the result for the width of the boundary layer that we wanted. It suggests that, at high Reynolds number, there are actually two length scales in the game. The first is the size L of the object. The second, δ ≪ L, is the width of a boundary layer that surrounds the object where the effects of both viscosity and vorticity are important. The existence of this thin boundary layer is the 1905 insight of Prandtl.

Outside of the boundary layer, we may neglect viscosity and the fluid is well described by the Eulerian flows of Section 2.3. But much of the physics is dictated by what happens inside the boundary layer where there are large velocity gradients. We want to better understand the properties of this boundary layer.

3.5.1 Prandtl’s Boundary Layer Equation

As usual, we don’t want to attack the full Navier-Stokes equations. Instead, we will extract the relevant equations that will suffice to model the boundary layer.

We’ll set things up as follows. We consider a two-dimensional flow in the (x,y)-plane. As shown in Figure 13, we’ll take a thin plate that extends in the x-direction sitting at y = 0. The flow is two-dimensional and we write u = (u,v). Asymptotically, u → (U,0). We impose the no-slip boundary condition u = v = 0 on the plate at y = 0. Incompressibility tells us that ∂u/∂x + ∂v/∂y = 0 (3.36)

We’ll also look only at steady flows, so there are no time derivatives. The full Navier-Stokes equations then read u ∂u/∂x + v ∂u/∂y = -1/ρ ∂P/∂x + ν(∂²u/∂x² + ∂²u/∂y²) (3.37)

u ∂v/∂x + v ∂v/∂y = -1/ρ ∂P/∂y + ν(∂²v/∂x² + ∂²v/∂y²) (3.38)

We want to ask: which of these terms can we safely ignore? And which should we keep in the boundary layer?

We look at how the flow changes over a horizontal scale L. We start with the assumption that velocities vary in the x-direction only over the scale L, but may vary in the y-direction on the much smaller scale δ ≪ L. Our goal is to construct a consistent truncation of (3.37) and (3.38) such that the terms we’re omitting are systematically smaller by a factor of the dimensionless parameter δ/L.

Our first piece of information comes from the incompressibility condition (3.36), with the terms scaling as ∂u/∂x ∼ U/L and ∂v/∂y ∼ v/δ ⇒ v ∼ U(δ/L) (3.39)

So the vertical velocity v is much smaller than the horizontal velocity U. This equation is telling us that the fluid flow is deflected only through a small angle ∼ δ/L.

Now let’s look to the Navier-Stokes equations (3.37) and (3.38). Both terms on the left-hand side of (3.37) scale as U²/L, while both terms on the left-hand side of (3.38) scale as U²δ/L². This means that the equation (3.38) is significantly less important than (3.37). In particular, if we assume that the pressure terms have the same order of magnitude then this tells us that |∂P/∂y| ∼ (δ/L) |∂P/∂x|

So, to leading order, pressure becomes a function only of the horizontal distance: P = P(x).

Now we turn to the second order terms on the right-hand-side of (3.37). We have ∂²u/∂x² ∼ U/L² and ∂²u/∂y² ∼ U/δ²

The second of these is clearly the most important, and we may ignore the ∂²u/∂x² term. Moreover, assuming that the ∂²u/∂y² term has the same order of magnitude as those on the left-hand side tells us that U²/L ∼ νU/δ² ⇒ δ ∼ √(νL/U) ∼ √(L/Re)

which confirms our earlier estimate (3.35) and reassures us that the whole approximation scheme is valid at large Reynolds number.

The upshot is that, when solving for the fluid in the boundary layer, we may ignore the y-component of the Navier-Stokes equation (3.38) and the x-component (3.37) simplifies to u ∂u/∂x + v ∂u/∂y = -1/ρ dP/dx + ν ∂²u/∂y² (3.40)

This is the Prandtl boundary layer equation. It should be solved in conjunction with the incompressibility condition (3.36).

There is one final finesse. We know that the pressure is approximately a function only of x. This means that we are at liberty to evaluate the pressure P(x) far from the boundary layer, y ≫ δ. But here the viscosity terms may be neglected completely, and the flow is governed by the Euler equation. The velocity field takes some profile u → (U(x),0) as y/δ → ∞, where U(x) → U as x → −∞. The Euler equation then tells us that, for a steady flow, -1/ρ dP/dx = U ∂U/∂x (3.41)

which can be substituted into (3.40).

Our next task is to solve (3.40). Far from the plate, the term proportional to ν is unimportant. There is a mathematical framework to solve equations of this kind, whose characteristic form differs in some limit such as ν → 0. This is the theory of "matched asymptotic expansion". We won’t need this in what follows. Instead, we’ll look just at some simple examples.

3.5.2 An Infinite Flat Plate

Our simple example is a semi-infinite flat plate. The plate starts at x = 0, which we refer to as the leading edge. It then continues indefinitely.

Asymptotically, the flow is constant, u → (U,0) as y/δ → ∞ so, from (3.41), we have dP/dx = 0 and the Prandtl equation becomes u ∂u/∂x + v ∂u/∂y = ν ∂²u/∂y² (3.42)

The flow is two-dimensional so we can again use a stream function Ψ(x,y), such that u = (u,v) with u = ∂Ψ/∂y and v = -∂Ψ/∂x.

If we take the stream function to scale as Ψ ∼ Uδ then, with the scalings described above, we expect to get u ∼ U and v ∼ (δ/L)U which is what we want. In looking for a solution, we’ll be guided by Figure 13. We know that as we move further in the x-direction, the width δ of the boundary layer grows. We will search for "self-similar" solutions in which the velocity profile within the boundary layer remains the same, but gets stretched in the y direction as the layer grows. Mathematically, this means that we’ll search for solutions of the form Ψ(x,y) = U δ(x) f(η)

where η is the rescaled y coordinate, η = y / δ(x), where δ(x) is the size of the boundary layer (3.35)

δ(x) = √(νx/U) (3.43)

(Note: for once δ(x) has nothing to do with the Dirac delta function!) For our whole approximation to be valid, we required δ ≪ L which, in the present context means δ(x) ≪ x ⇒ x ≫ ν/U. In other words, we can only trust what follows a distance ν/U from the leading edge of the plate. It only gives a good description beyond that point.

The velocity in the x-direction is u = U f′

Meanwhile, the y-direction, we have v = -U δ′ f - U δ f′ = -U (f - η f′) δ′ (3.44)

Now we can start building the various terms in the Prandtl equation (3.42). We have ∂u/∂x = -U f′′ (η / δ) δ′ and ∂u/∂y = U f′′ / δ and ∂²u/∂y² = U f′′′ / δ²

So putting it all together, the Prandtl equation (3.42) becomes - U² η (δ′/δ) f′′ f′ - U² (f - η f′) f′′ (δ′/δ) = ν U f′′′ / δ²

Two of the terms happily cancel, and we’re left with U δ′ δ f f′′ + ν f′′′ = 0

But, from (3.43), we have δ′ δ = ν/(2U) so our problem reduces to an ordinary, third order differential equation for f(η), f′′′ + f f′′ = 0 (3.45)

We need to solve this subject to the no-slip boundary condition f = f′ = 0 at η = 0 and the asymptotic requirement f′ → 1 as η → ∞ which ensures that, far from the plate, u → (U,0).

There’s no analytic solution to this equation. But it’s straightforward to solve the equation numerically. The resulting velocity profile is shown in the figure on the right and is known as the Blasius boundary layer. The distance from the plate y ∼ η is plotted vertically and the velocity u ∼ f′[η] plotted horizontally. You can see that the velocity interpolates from its zero value on the plate, to the asymptotic value. The graph also gives a more accurate estimate of the thickness of boundary layer as something like ∼ 4-5 times δ, by which point the velocity is pretty much at its asymptotic value.

The numerical solution tells us something else. Asymptotically, as η → ∞, we find that f(η) ≈ η - 1.72 + O(1/η)

This means that, far from the plate, there is vertical component to the velocity (3.44), v ≈ 1.72 √(νU / (4x)) as y/δ → ∞

This is capturing what we saw previously in (3.39): the fluid is deflected by an angle ∼ δ/L. This angle gets smaller as we get further from the leading edge. This is because the boundary layer increases, and so the velocity gradient – which is always such that the velocity changes from zero to U – decreases as x gets larger, and this fact is reflected by the velocity component in the y-direction infinitely far from the plate. The would-be divergence at x = 0 is mitigated by the fact that, as we have seen, our solution only makes sense for distances x ≫ ν/U from the leading edge.

The Drag Force on a Finite Plate

Strictly, the calculation above holds for an infinite plate. We’ve also seen that it fails within a distance ν/U of the leading edge, and one may expect that it similarly fails near the trailing edge. But we may hope that, for large L, it gives a suitable approximation of the boundary layer over much of a finite plate. With this assumption, we can compute the drag force.

The force on the plate comes from the appropriate component of the stress tensor (3.5). For a single boundary layer, we have σ = ρν (∂u/∂y + ∂v/∂x) |_{y=0} = ρν (U/δ) f′′(0) (3.46)

where only the ∂u/∂y term contributes because ∂v/∂x vanishes at y = 0. We use the numerical solution to evaluate f′′(0) ≈ 0.33. We also need to remember that there are two boundary layers, one on each side. So the total drag force is F = 2 × 0.33 × ρ ν^{1/2} U^{3/2} ∫_0^L (1/√x) dx = 1.32 ρ ν^{1/2} U^{3/2} (2√L) ≈ 2.64 ρ ν^{1/2} U^{3/2} L^{1/2} 0.33ρν^{1/2}U^{3/2}L^{1/2} drag Note that the drag force increases as L rather than proportional to L as one might naively expect. This is because, as the boundary layer thickens, the velocity gradients decrease and, hence, so too does the stress on the plate.

This is our first honest resolution of d’Alembert’s paradox: the drag force for an object at high Reynolds number, where one might think that the Euler equation is sufficient, is non-zero. We see explicitly that the drag does vanish if we set ν = 0. If we embed the viscosity in the dimensionless Reynolds number Re = UL/ν, we have F_{drag} = 1.33ρ U^2 L / Re Taken at face value, this says that the drag force is, in fact, vanishing in the limit Re → ∞. But, sadly, there’s another catch awaiting us. The calculation above breaks down at large Reynolds numbers due to the effects of turbulence. Experimentally, this is found to happen at Re ∼ 10^5 or 10^6.

3.5.3 Boundary Layers with Pressure Gradients There is a generalisation of the ideas above that exhibits some novel behaviour within the boundary layer. This will be important in the next section when we look at the fate of the boundary layer when it leaves an object.

The generalisation involves looking at boundary layers in flows that are accelerating or decelerating asymptotically. We will again take a semi-infinite flat plate. Far from the boundary layer, the fluid flow takes the form u → (U(x),0), now with U(x) = U (x/l)^m (3.47)

with l some length scale and m a parameter that determines the acceleration. Note that when m < 0 our velocity profile (3.47) diverges at x = 0. We deal with this by ignoring it: our interest is only in the behaviour of the boundary layer downstream at x > 0.

From (3.41), we must have a pressure gradient driving this flow (1/ρ) dP/dx = -U dU/dx = - (m U^2 / l) (x/l)^{2m-1} There are two distinct cases that will interest us: • m > 0: Accelerating flow with dP/dx < 0.

• m < 0: Decelerating flow with dP/dx > 0.

This is the asymptotic pressure gradient. But, by the arguments of Section 3.5.1, there is no change in the pressure in the y-direction, perpendicular to the plate. This means that the boundary layer also experiences the pressure gradient dP/dx. Our goal is to understand how the boundary layer reacts to this gradient.

The Prandtl equation is u ∂u/∂x + v ∂u/∂y = U dU/dx + ν ∂²u/∂y² (3.48)

We again seek a self-similar solution, now of the form Ψ(x,y) = U(x)δ(x)f(η)

Here U(x) is given by (3.47), while δ(x) is a generalisation of our previous expression for the boundary layer thickness, δ(x) = √(νx / U(x))

which takes into account the x-dependence of the asymptotic velocity. Note that, for accelerating flows, the boundary layer becomes thinner, relative to the m = 0 case, as the flow proceeds. It becomes thicker for decelerating flows. Finally, η = y/δ(x) is the rescaled y-coordinate, as before.

The velocity in the x-direction and y-directions are now u = U f′ and v = - (Uδ)′ f + U η f′ δ′ After a small amount of algebra, the Prandtl equation (3.48) becomes U U′ f′² - (Uδ)′/δ f f′′ = U U′ + (νU / δ²) f′′′ Now we use the explicit expression for the asymptotic velocity (3.47), which tells us that U ∼ x^m and Uδ ∼ x^{(m+1)/2}. Substituting these into the equation above, we see that all terms scale as U²/x and we may divide by this. Happily, the partial differential equation reduces once again to an ordinary differential equation, m f′² - (m+1) f f′′ = m + f′′′ This reduces to our previous equation (3.45) when m = 0.

Again, we solve this subject to the boundary conditions f = f′ = 0 at η = 0 and f′ → 1 as η → ∞ The solutions are known as the Falkner-Scan family of boundary layers. The velocity profiles u ∼ f′(η) for a number of different flows are shown in the figure. The colours correspond, from top to bottom, to m = −0.09 (in cyan), m = −0.07 (in green), m = 0 (in blue), m = 0.2 (in red) and m = 0.7 (in magenta).

For accelerating flows, with m > 0, there isn’t a great deal of difference from our previous results. One can show that the solution to the equations is unique and, as you can see from the graph, the velocity profiles all live underneath the m = 0 curve, coming in at ever more acute angles at the origin. This can be understood because there is a greater transfer of momentum from the accelerating fluid above. It also has consequence: the angle at which the graph intersects the origin is related to (the inverse of) f′′(0). As the acceleration increases, so too does f′′(0). But, from (3.46), means that the force imparted on the plate due to the boundary layer also increases.

At first glance, things don’t look too different for decelerating flows with m < 0 either. Two are shown in the figure: m = −0.07 (in green) and m = −0.09 (in cyan). Now the graphs come in more steeply at the origin, corresponding to a smaller value of f′′(0) and, correspondingly, a smaller stress on the plate. But when we look more closely, there is a surprise waiting us: numerically, we find that for some critical value m_crit, the solution actually comes into the origin vertically, m = m_crit ≈ −0.0904 ⇒ f′′(0) = 0 In other words, for a critical deceleration, there is no friction force between the plate and fluid!

What’s going on here? Consider an element of fluid near the boundary. It has a force to the right due to the fluid moving above it. But there are also forces to the left, both from the pressure gradient dP/dx > 0 and from the viscous force of the boundary. At m = m_crit, these precisely cancel. The result is that not only is u = 0 on the boundary, but also du/dy = 0.

What happens if we decrease m below the value m_crit? Naively, one might have thought that one would find solutions with du/dy < 0, which would mean the fluid closest to the boundary actually flows in the opposite direction. It turns out that this doesn’t happen. There are no solutions for m < m_crit.

However, there are further solutions that do exhibit reverse flows. It turns out that these solutions exist for any m_crit < m < 0 where there are two branches of solutions. The first, given above, has u > 0 everywhere. The second has a region with u < 0 close to the plate. An example is shown in the figure for m = −0.05. It has f′′(0) ≈ −0.1. In this case, a fluid element in the region closest to the boundary has a velocity in the opposite direction to the rest of the flow. This reverse flow can be understood as the pressure gradient pushing to the left, while the force from both the fluid above it, and also from the plate, pushes to the right.

It seems that these boundary solutions with reverse flow cannot be set-up in experiment because they are thought to be unstable in this particular context. Nonetheless, the existence of such reversed boundary layers is crucial to understand the next topic that we turn to. This is the fate of the boundary layer when the boundary ends.

Figure 14. The flow, from left to right, around a streamlined object at Re ≈ 7000. On the left, the object is aligned with the streamlines and the boundary layer merges smoothly into the flow at the trailing edge. On the right, the object is inclined by 5°. The boundary layer separates from the object on the upper edge.

3.5.4 Separation So far we’ve understood how the boundary layer develops, but only by restricting to a flat, semi-infinite plate. Needless to say, that’s not particularly realistic. Most objects are neither flat, nor semi-infinite. Clearly, we need to understand the physics of the boundary layer for objects that are curved and finite.

This, it turns out, is not so easy. Until now, we’ve made progress by finding clever ways to reduce the Navier-Stokes equations to an ordinary differential equation which can then easily be solved. But the problem that we’re now interested in offers no such simplification. That means that to get a complete handle on the problem we must resort to solving partial differential equations numerically. Which is possible, but challenging, and beyond the scope of these lectures. Instead we will make do with some rather qualitative arguments, piecing together various bits of physics that we’ve learned so far.

First, we can gain some intuition for what’s going on by turning to experiment7.

Figure 14 shows the stream lines for a high Reynolds number flow (Re ≈ 7000) around an elegantly pointy object. In the figure on the left, the object is aligned with the streamlines, which glide around much like the flows that we’ve discussed so far in these lectures. Such flows, where there is little mixing between adjacent layers of the fluid, are called laminar. A boundary layer forms around the object but, at least as far as the photograph shows, appears to merge seamlessly back into the bulk fluid at the tail end.

On the right of Figure 14 is the same object, again at Re ∼ 7000, but now tilted at an angle of 5°. The flow is again laminar at the front and below the object. But you can see that something screwy is happening on the upper trailing edge. There is clearly a streamline that moves away from the object, leaving a swirling indeterminate flow beneath it.

The same phenomenon occurs for less aerodynamic objects. Figures 15 and 16 show flows moving past a circular cylinder. The first flow, at Re ≈ 10, clearly shows an anti-symmetry between the front and back of the cylinder as the streamlines separate from the body. This is unsurprising, but sits in stark contrast to the potential flows and Stokes flows that we’ve seen previously, where it’s difficult to see by eye the difference between the front and back of the flow. (See, for comparison, Figure 7 or Figure 10.)

In the second picture in Figure 15, the Reynolds number has increased to Re ≈ 26 and we again see the flow separating from the body, this time clearly leaving two counter-circulating eddies in its wake.

The Reynolds numbers in Figure 15 are fairly low and it’s not at all obvious that we can use the theory of boundary layers, which relies on the approximation Re ≫ 1. But this is surely valid for the picture in Figure 16, now at Re ≈ 2000. Now we clearly see that the laminar flow at the front of the cylinder separates somewhere near the top of the cylinder, leaving a turbulent flow in its wake.

There are a bunch of things to unpack here. First, how do we extend the theory of a boundary layer to a curved object like those shown in the figures? Second, why does the flow separate from the object at some point? And, finally, how can we understand the physics of the wake left behind? We’ll deal with each of these in turn.

Here is a cartoon of the physics. First, extending the theory of the boundary layer to a curved object turns out to be fairly straightforward. We use the same equations as before, but with x and y now curvilinear coordinates: x is the coordinate along the boundary and y the coordinate perpendicular. The boundary layer is so thin that, locally, it barely notices the curvature. All we must do is ensure that the pressure in the boundary layer is given by (3.41), -1/ρ dP/dx = U ∂U/∂x. Here, as a first approximation to U(x), we should take the near-boundary limit of the flow that surrounds the boundary layer. Provided that this flow isn’t turbulent, we can use the near-boundary limit of the inviscid potential flows that we described in Section 2.3. But we know how the pressure changes over the sphere or cylinder due to a potential flow. (The answer for the sphere was given in (2.31) and the result for the cylinder is similar.) There we saw that the pressure directly at the front and back is the same as the asymptotic pressure, but the pressure reduces as you move up or down over the sphere and takes its minimum value at the top and bottom. Crucially, the pressure for an inviscid potential flow is symmetric on the front and back: this, of course, was what lead to d’Alembert’s paradox.

Now we can see what this means for the boundary layer. On the front edge of the cylinder, the pressure is decreasing, P′ < 0. This corresponds to an accelerating flow. But on the back edge, the pressure is increasing, P′ > 0, and the flow is decelerating. This suggests that we might get the kind of behaviour that we observed for decelerating flows in the Falkner-Scan family of boundary layers. In particular, at some point the velocity u tangential to the boundary will obey (∂u/∂y)|_{y=0} = 0, where y is the direction perpendicular to the boundary. This is the separation point, with the streamline bifurcating and leaving the boundary. Beyond this point, one expects reverse flow close to the boundary. Beyond the separation point, the boundary layer moves off into the bulk of the fluid, leaving behind the wake. A sketch of the scenario is shown in Figure 17.

The boundary layer itself cannot just dissolve once it has separated from the boundary. One might reasonably wonder what distinguishes it from the bulk of the fluid. After all, they’re made from the same stuff. The answer is that the boundary layer has vorticity, generated by the no-slip condition ω = -ẑ(∂v/∂x - ∂u/∂y) ≈ -ẑ ∂u/∂y, where the first term dominates in the boundary layer approximation. For the boundary layers described above, we have |ω| = Uf′′(0)/δ. Meanwhile, as we saw previously, the outer laminar flow is irrotational. The vorticity persists in the wake that trails the objects.

For low Reynolds number, the stream flow is low and this vorticity has time to diffuse due to the effects of viscosity. The result is the two large eddies trailing the object seen in Figure 15. The flow is steady. These are steady eddies.

But as the Reynolds number is increased to around Re ∼ 100, something more interesting happens. One of the eddies grows until it peels off from the boundary in a process known as vortex shedding. The flow then curls back around the boundary and a new eddy forms. Meanwhile, the eddie on the other side then undergoes the same process. The result is a gorgeous flow pattern of alternating eddies known as the von K´arm´an vortex street. An example is shown in Figure 18. At these Reynolds numbers, there is no steady flow of the kind that we’ve searched for in these lectures. Instead, the flow is time dependent, but periodic.

There is much that we have swept under the carpet in the discussion above. The elephant in the room is turbulence. As the pictures clearly show, for large Reynolds number the flow is far from laminar. Indeed, the flow is no longer even two dimensional, but twists and turns in a noisy fashion in three dimensions. This occurs for Re ≳ 10⁴ when the wake becomes turbulent as shown in Figure 16. A process known as turbulent mixing causes the pressure to be uniform across the turbulent wake, and equal to its value at the point of separation. This means that there is a much lower pressure behind the object and, correspondingly, a much larger drag force.

As the Reynolds number is increased yet further to Re ≳ 10⁵ something novel happens: now the boundary layer itself becomes turbulent. The same turbulent mixing means that vorticity can be transferred vertically much more efficiently, and the result is that the boundary layer gets thicker. This has two, competing effects. The first is that the drag due to the turbulent boundary layer increases compared to the laminar boundary layer. The second is that the separation of the boundary layer is delayed, with the reversed flow happening further downstream. This results in a narrower wake which reduces the drag. It turns out that this reduced drag from the narrower wake is more than sufficient to compensate for the increased drag due to the turbulent boundary layer, and the result is that, surprisingly, the drag force actually drops suddenly at this Reynolds number. This goes by the name of the drag crisis.

4 Waves Our story so far has involved the bulk motion of fluids, flowing from one place to another, sometimes trying to negotiate obstacles in their way. But fluids are more subtle and interesting than this. They contain mechanisms to transfer energy through space, but without the bulk of the fluid travelling very far. This is achieved this through oscillatory behaviour known as waves.

Waves are familiar, both from our everyday experience as well as from other areas of physics. Our purpose in this section is to explore some of large variety of waves that can occur in fluids. This includes, in Section 4.4, sound waves which gives us an opportunity to look at some of the novelties that arise with compressible fluids.

## 4.1 Surface Waves

“Now, the next waves of interest, that are easily seen by everyone and which are usually used as an example of waves in elementary courses, are water waves. As we shall soon see, they are the worst possible example, because they are in no respects like sound and light; they have all the complications that waves can have.” Richard Feynman We start with waves travelling on the surface of a fluid. These include waves on the ocean. As Feynman points out, there are a surprisingly large number of subtleties that arise in understanding these waves.

Viscosity will not play a leading role in our story, so we return to the Euler equation of Section 2, ρ(∂u/∂t + u·∇u) = -∇P + ρg (4.1). We’ve included the effects of gravity on the right-hand side. As we will see, this provides the restoring force needed to create waves.

We will shortly solve the Euler equation using the same techniques that we met in Section 2. All of the novelties come, like so many things in fluid dynamics, from the boundary conditions. So before we get going, we need to think about the kind of boundary condition we should impose on the surface of a fluid.

4.1.1 Free Boundary Conditions The surface of a fluid is best viewed as the interface between two different fluids. In the case of the ocean, this is the water and the air above. But we could also have a situation where we have two immiscible liquids, like oil and water. The surface is free to move, and so is sometimes referred to as a free boundary.

Suppose that the boundary lies close to some z ≈ constant surface, as shown in Figure 19. Clearly this is appropriate for the surface of the ocean. The surface can fluctuate and, in general, is described by some function F(x,t) = z −η(x,y;t) = 0 (4.2). The normal to such a surface is parallel to ∇F (as shown, for example, in the lectures on Vector Calculus), n ∼ ∇F = (-∂η/∂x, -∂η/∂y, 1). Meanwhile, the velocity of the interface is, by construction, in the z direc ∂η U = (0,0, )

∂t The appropriate boundary condition Wavevector k = k̄. Then we can Taylor expand the frequency and write ω(k) = ω(k̄) + (k − k̄) (∂ω/∂k)|_{k=k̄} + ...

Substituting this into the expression for the wavepacket, we have η(x,t) ≈ ∫ (dk/2π) e^{-iω(k̄)t} a(k) e^{ik(x−v_g t)} (4.14)

where v_g = (∂ω/∂k)|_{k=k̄} (4.15)

This is called the group velocity of the wave. It’s clear from the form (4.14) that v_g is the speed at which the wavepacket moves. If ω ∼ k then the wave doesn’t disperse and the group velocity coincides with the speed c = ω/k that we defined previously, known as the phase velocity. But, in general, the two differ. The group velocity is the speed at which energy (and, in other contexts, information) is transported by the wave.

For the surface waves considered here, ω ∼ k^{1/2} and so the group velocity and phase velocity are related by v_g(k) = (1/2)c(k). The wavepackets travel at half the speed of the individual Fourier modes.

The Velocity Field It is a simple matter to compute the velocity field of the fluid. Substituting for the various integration constants, we have the potential ϕ = Re[ −i (ωη_0 / k) * (cosh(kz + kH) / sinh(kH)) * e^{ikx − iωt} ]

which now just has a single undetermined integration constant η_0 that fixes the amplitude of the wave. Our approximations above mean that the solution should be trusted only when η_0 k ≪ 1. For once we’ve explicitly reminded ourselves that we should take the real part of the potential when computing the velocity u = ∇ϕ. We have u_x = (ωη_0 / sinh(kH)) * cosh(kz + kH) cos(kx − ωt)

u_z = (ωη_0 / sinh(kH)) * sinh(kz + kH) sin(kx − ωt)

The velocity profile is plotted in Figure 21 for deep water waves (on the left) and for shallow water waves (on the right). In both cases, the velocity of the water is mostly up/down, despite the fact that the wave travels to the right. In the trough of the wave, the water is moving up on the left and down on the right. In the peak of the wave, this is reversed: the water moves down on the left and up on the right. The net effect is that the wave travels to the right.

There’s something misleading about the figure for deep water waves. In this case, e^{-kH} ≈ 0 and the velocity profile is well approximated by u_x ≈ ωη_0 e^{kz} cos(kx − ωt)

u_z ≈ ωη_0 e^{kz} sin(kx − ωt) (4.16)

We see that the magnitude of the velocity |u| ≈ ωη_0 e^{kz} decreases exponentially from its value at the surface z = 0. It means that all the action is really taking place within a depth of one wavelength or so from the surface. In contrast, for shallow water waves the speed does not vary greatly with height.

For deep water waves, the ratio of the fluid speed to the wave speed is |u|/c ≈ kη_0 e^{kz}. The condition (4.8) is tantamount to the requirement that kη_0 ≪ 1. In other words, the wave travels much faster than the fluid from which it’s made.

Particle Paths Suppose that you drop a small ball into the flow that follows an element of fluid on its travels. What path does it take? As we described in Section 1.1, the trajectory x(t) is called a pathline and is governed by the equation (1.1)

dx/dt = u(x(t), t) (4.17)

which we should solve given some initial starting point x(t = 0) = x_0.

To solve this, we will assume that the particle doesn’t get far from its original starting position and approximate the velocity field u(x, t) by its Taylor expansion about x_0, u(x, t) ≈ u(x_0, t) + ((x − x_0) · ∇) u(x_0, t) + ... (4.18)

If we keep just the first term, the equation for the pathline becomes dx/dt = (ωη_0 / sinh(kH)) * cosh(kz_0 + kH) cos(kx_0 − ωt)

sinh(kz_0 + kH) sin(kx_0 − ωt)

⇒ x(t) = x_0 + (η_0 / sinh(kH)) * (−cosh(kz_0 + kH) sin(kx_0 − ωt))

sinh(kz_0 + kH) cos(kx_0 − ωt)

This is telling us that the particles travel in ellipses, squashed in the vertical direction. For deep water waves, these ellipses become circles with x(t) = x_0 + η_0 e^{kz_0} (−sin(kx_0 − ωt)) (4.19)

cos(kx_0 − ωt)

The ellipses or circles become exponentially smaller as the depth increases. The vertical component of the velocity is in phase with the crests of the wave, η ∼ cos(kx−ωt). Meanwhile, the horizontal component ensures that the particle goes clockwise for waves that propagate to the right.

We can also look at the effect of the second term in (4.18). Things are simplest if we restrict attention to deep water waves, with velocity (4.16) and particle position (4.19). If we use our leading order expression (4.19) for x(t) we find, after a little algebra, ((x(t) − x_0) · ∇) u = ωk η_0^2 e^{2kz_0} When substituted into (4.17), this has the interpretation of a constant, horizontal drift velocity for the particles, given by v_drift = ωk η_0^2 e^{2kz_0} = c (k η_0 e^{kz_0})^2 This is known as Stokes’ drift. The ellipses traced by the particles don’t quite close, but slowly inch their way in the direction in which the wave propagates. Note that there is a hierarchy of speeds, v_drift ≪ |u| ≪ c with k η_0 e^{kz_0} ≪ 1 the small, dimensionless number that governs successive ratios. The Stokes’ drift v_drift is the speed at which matter bobbing in the waves moves.

4.1.3 Surface Tension If you’re a molecule, a liquid is a nice, comfortable place to spend your time. You’re attracted to all your neighbouring molecules, but are afforded enough freedom to wander off on your own.

Things get more precarious at the surface of the liquid. There are now fewer neighbours to keep you company. As each neighbour offers a welcoming, attractive potential, the fact that you now find yourself a little isolated means that you are sitting in a higher energy state. This, in turn, means that, collectively, the molecules in a liquid can lower their energy by keeping the area of the surface as small as possible. This results in a force called surface tension. This force is the reason that droplets of water, or soap bubbles, are round: the sphere has the minimal surface area.

The existence of surface tension means that pressure need no longer be continuous across the surface. Instead, the surface can tolerate a local pressure difference by bending slightly and letting the surface tension push back. Said another way, the surface tension provides another restoring force for the wave motion.

This physics is captured by a change to the boundary condition (4.4). For a surface with embedding z = η(x,y,t), the pressure difference should now be P(x,y,η(x,y)) − P_0 = −γ ∇^2 η (4.20)

with γ the surface tension and ∇^2 η = ∂^2 η/∂x^2 + ∂^2 η/∂y^2 the 2d Laplacian which is the appropriate characterisation of the curvature of the surface.

We would like to understand how the existence of surface tension affects the dynamics of waves. If we follow through our derivation of the time-dependent Bernoulli principle, equation (4.7) is replaced by (∂ϕ/∂t + (1/2) |∇ϕ|^2 + P/ρ + gη − (γ/ρ) ∇^2 η)|_{z=η} = f(t)

After linearisation, the final condition in (4.9) becomes (∂ϕ/∂t)|_{z=0} + gη − (γ/ρ) ∇^2 η = ˜f(t) (4.21)

with f(t) a function that can depend on time but, crucially, must be independent of space. We now make our usual ansatz for waves propagating in the x-direction, ϕ(x,z,t) = ϕ_0(z) e^{ikx − iωt} and η(x,t) = η_0 e^{ikx − iωt} Much proceeds as before. In fact, we can see how the surface tension affects the story just by staring at (4.21) where we see that it accompanies the gravitational acceleration: we just need to replace g with g → g + (γk^2)/ρ = g (1 + l_c^2 k^2) (4.22)

in all our previous formulae. Here we’ve introduced the length scale l_c = √(γ/(gρ)) (4.23)

This is known as the capillary length. From (4.22), we see that long wavelength modes with λ ≫ l_c, so l_c k ≪ 1, are pretty much unaffected by surface tension. In contrast, surface tension effects dominate when the wavelength becomes short, λ ≪ l_c, so l_c k ≫ 1. Waves with λ ≲ l_c are referred to capillary waves.

For water at room temperature, l_c ≈ 3 mm. The capillary waves are little ripples on the water, up to a wavelength of 1 cm or so (with the factor of 2π in the definition of the wavelength raising us above l_c.)

The general dispersion relation is ω^2 = gk (1 + l_c^2 k^2) tanh(kH) (4.24)

while the phase velocity is c = √[(1 + l_c^2 k^2) tanh(kH)/k]

For capillary waves, with l_c k ≫ 1, in deep water, so kH ≫ 1, we have c ≈ √(γk/ρ)

In contrast to surface waves driven by gravity (4.12), the short wavelength modes now travel faster. Furthermore, the group velocity (4.15) is v_g(k) = (3/2)c. The wavepackets now travel faster than the individual Fourier modes.

## 4.2 Internal Gravity Waves

Gravitational waves are the ripples of the spacetime continuum that emerge from violent events such as the collision of two black holes. That, sadly, is not the topic of discussion here. Instead, “gravity waves” describe the disappointingly mundane phenomenon of fluids bobbing up and down due to gravity. If you want to learn more about gravitational waves, you’ll need to open the lectures on General Relativity. Otherwise, read on.

Gravity waves are simply waves in fluids where the restoring force is provided by gravity. The surface waves above are examples (at least those with wavelength longer than the capillary length where surface tension is negligible). In this section we study gravity waves in the bulk of the fluid, as opposed to on the surface.

Stratified Flows and Buoyancy Frequency A flow is said to be stratified if the density ρ varies from place to place. Typically this happens because of gravity and the density is a function of the vertical direction: ρ = ρ(z).

Consider a small ball immersed in a stratified flow. If the ball has density ρ = ρ(z_0) for some height z_0 then, by Archimedes principle, it will naturally sit at height z = z_0. This is where the weight of water that it displaces is equal to its own weight. Suppose now that we displace the ball upwards by some small amount δz. The density of the fluid there is ρ(z + δz) ≈ ρ(z) + (∂ρ/∂z)|_{z0} δz Now the weight of the displaced water differs from that of the ball, resulting in a net upwards force, Upwards Force ≈ g (∂ρ/∂z)|_{z0} δz If ∂ρ/∂z > 0 then the ball's original position was unstable, and it flies upwards. But most stratified flows have density larger at the bottom than at the top, so ∂ρ/∂z < 0. In this case, the ball oscillates about its equilibrium position, enacting simple harmonic motion with a frequency N^2 = - (g/ρ) (∂ρ/∂z) (4.25)

This is called the buoyancy frequency or, sometimes, the Brunt–Väisälä frequency. In what follows, we’ll look at similar motion but for the fluid itself. Note that we haven’t specified how ρ(z) depends on the height z. Nor will we do this throughout the rest of this section. This follows only when we introduce an equation of state relating pressure and density. We’ll meet this in Section 4.4.

Equations for Gravity Waves Until now, the incompressibility condition was forced upon by the requirement that the density is constant. For stratified flows, this is no longer the case. Nonetheless, it is still physically sensible to insist on incompressibility (at least for speeds smaller than the sound speed)

∇·u = 0 With this, mass conservation becomes the requirement, ∂ρ/∂t + ∇·(ρu) = 0 ⇒ Dρ/Dt = ∂ρ/∂t + u·∇ρ = 0 In addition, we will ignore viscosity and look at gravity waves in the Euler equation, now in the presence of gravity ρ (∂u/∂t + u·∇u) = -∇P - ρ(z) g ẑ We’ll consider a boring background, with u = 0 and the pressure P(z) related to the density ρ(z) through the Euler equation, by dP/dz = -g ρ(z)

Now we look at small perturbations around this background. The gravity waves of interest travel in the horizontal x-direction, while bobbing up and down in the vertical z-direction. To this end, we look for solutions of the form u(x,t) = (u_x, 0, u_z) e^{i k_x x + i k_z z - i ω t} with u_x and u_z constant. Both the density and pressure exhibit the same wavelike behaviour, ρ(x,z,t) = ρ_0(z) + ρ̃ e^{i k_x x + i k_z z - i ω t} and P(x,z,t) = P_0(z) + P̃ e^{i k_x x + i k_z z - i ω t} The incompressibility condition tells us that k_x u_x + k_z u_z = 0 (4.26)

Even before we proceed, this equation is telling us that k·u = 0. In other words, the waves are transverse. This is like light waves (which have E·k = B·k = 0) but contrasts with the sound waves that we will meet in Section 4.4.

For the other equations, we linearise, throwing away any terms quadratic in perturbations. Mass conservation gives -i ω ρ̃ + u_z dρ_0/dz = 0 and the two components of the Euler equation are -i ρ_0 ω u_x = -i k_x P̃ and -i ρ_0 ω u_z = -i k_z P̃ - g ρ̃ Solving these simultaneous equations gives us the dispersion relation for the frequency of gravity waves, ω = ± N (4.27) / sqrt(k_x^2 + k_z^2)

with N the buoyancy frequency (4.25). Note that we necessarily have ω ≤ N. Moreover, the frequency is non-vanishing only if k_z ≠ 0. We can, however, consider the extreme example with k_z = 0. In this case ω = N. The incompressibility condition then tells us that we must have u_x = 0. This, in turn, means that we have a wave in the x-direction since k_x ≠ 0 but with the motion of the fluid bobbing up and down with buoyancy frequency in the z-direction.

In general, the gravity wave propagates in the direction k = (k_x, 0, k_z)

The slight surprise comes when we compute the group velocity. For a one dimensional wave, this is v_g = ∂ω/∂k. For a higher dimensional waves, like we have here, the relevant definition is v_g = x̂ ∂ω/∂k_x + ẑ ∂ω/∂k_z For the dispersion relation (4.27), this gives v_g = (N k / (k_x^2 + k_z^2)^{3/2}) (k_z, 0, -k_x)

Strangely, group velocity is perpendicular to the direction of the wave, v_g·k = 0. This means that both wavepackets and energy propagate in the direction v_g, but this is orthogonal to the direction k of the wave itself! It is somewhat less surprising when you realise that v_g is parallel to the velocity u of the fluid.

## 4.3 Because the Earth Spins

In this section we take something of a diversion. We will explore some novel phenomena that arise when fluids rotate. The main motivation from this comes from the fact that Earth spins and this gives rise to some new types of waves with rather interesting properties. Recall from the lectures on Dynamics and Relativity that if we sit in a reference frame that rotates with constant angular velocity Ω then we experience two fictitious forces. These are the centrifugal force, proportional to Ω×(Ω×x) and the Coriolis force, proportional to 2Ω×u. For fluids, these appear as forces on the right-hand side of the Navier-Stokes equation. Throughout this section, we will neglect viscosity and work with the Euler equation in a rotating frame, so we have ∂u/∂t + u·∇u = - (1/ρ) ∇P + g - 2Ω×u - Ω×(Ω×x) (4.28)

The centrifugal force is not particularly interesting for our purposes. Locally, it simply redefines what we mean by “down” since, like gravity, it can be written as the gradient of a potential energy. We will simply ignore it. As we will see, all the interesting physics arises from the Coriolis force.

4.3.1 The Shallow Water Approximation In what follows, we will make the so-called shallow water approximation. We will assume that the extent of the fluid in the horizontal directions, labelled by x and y, is much greater than the height of the fluid in the vertical z-direction. For our purposes, the Atlantic ocean counts as “shallow” since it is, on average, around 3.5 km deep but several thousand km wide. Similarly, the atmosphere also counts as “shallow” and the phenomena that we describe can be found in both.

Our choice of coordinates is shown in the figure to the right. Locally, “up” is in the z-direction, “North” is in the y-direction, and “East” is the x-direction. We define the Coriolis parameter f = 2Ω·ẑ (4.29)

If we’re considering flows where we can neglect the curvature of the Earth, then we restrict attention to a given tangent plane as shown and take f to be constant. In contrast, if we need to take into account the curvature of the Earth, then f will be a function f = f(y), reflecting the fact that as we move along the surface the local “up” direction ẑ changes, while the spin Ω remains fixed. In what follows, we will consider both situations in which f is taken to be constant and, in Section 4.3.5, situations in which f varies.

Our initial set-up will be similar to that of water waves described in Section 4.1. We’ll take the average depth of the water to be H, with a flat, solid base at z = -H and a varying surface at z = η(x,y,t) with |η| ≪ H as shown in Figure 20. (Clearly the flat bottom is more appropriate for the ocean than the atmosphere!) Next, we assume that the velocities in the horizontal direction are independent of the depth, so u = (u, v, w) with u = u(x,y,t), v = v(x,y,t) and w = w(x,y,z,t)

Note that this is where our set-up starts to differ from the water waves of Section 4.1. The vertical velocity can be eliminated in favour of the height fluctuation η(x,y,t) by using the incompressibility condition ∇·u = 0 ⇒ ∂w/∂z = - ∂u/∂x - ∂v/∂y We integrate over the vertical z-direction, and use the free boundary condition (4.3), which tells us that w(z = η) = Dη/Dt and w(z = -H) = 0. We then have ∂η/∂t + u ∂η/∂x + v ∂η/∂y = -(H + η) (∂u/∂x + ∂v/∂y) (4.30)

This is the first of our shallow water equations.

Next, we assume that the pressure in the vertical direction adapts to balance the gravitational force. This hydrostatic approximation is what led us to Archimedes principle in Section 2.1.3. We also need the boundary condition P = P_0 on the surface at z = η, meaning that we take the pressure to be P = P_0 - ρ g (z - η) (4.31)

In the Navier-Stokes equation (4.28), we can then replace - (1/ρ) ∇P + g = -g ∇η. With these pieces in place, the remaining two Navier-Stokes equations read ∂u/∂t + u ∂u/∂x + v ∂u/∂y = f v - g ∂η/∂x (4.32)

∂v/∂t + u ∂v/∂x + v ∂v/∂y = -f u - g ∂η/∂y (4.33)

As usual, we want an excuse to drop the non-linear terms to make life easy. If a flow has characteristic velocity U, changing over some length scale L then these non-linear terms scale as U^2/L. This should be compared with the Coriolis terms which scale as f U. We introduce a dimensionless number, this time called the Rossby number Ro, Ro = U / (f L)

It’s appropriate to drop the non-linear terms for flows with Ro ≪ 1. The rotation of the Earth is Ω ≈ 10^{-4} s^{-1} while typical atmospheric or oceanic speeds are around U ∼ 10 m s^{-1}. That means that Ro ≈ 10^5 m / L We see that we can think about dropping the non-linear terms only for very long wavelength perturbations. For L ∼ 10^3 km, we have Ro ≈ 0.1 which, while admittedly < 1 is barely ≪ 1. Nonetheless, this is the approximation that we will make. We further linearise the first equation (4.30), leaving us with our three linear shallow water equations ∂η/∂t = -H (∂u/∂x + ∂v/∂y) (4.34)

∂u/∂t = f v - g ∂η/∂x (4.35)

∂v/∂t = -f u - g ∂η/∂y (4.36)

In the rest of this section, we will solve these equations in various scenarios for u(x,y,t), v(x,y,t) and η(x,y,t).

4.3.2 Geostrophic Balance and Poincaré Waves We’re going to find a number of different solutions to the linearised shallow water equations (4.34), (4.35) and (4.36). Among these will be wave-like solutions. But, more surprisingly, we will also find some time independent solutions that are more interesting than just an ocean with a flat surface h = constant.

It’s simple to see the existence of time independent solutions by setting ∂/∂t = 0 in (4.34), (4.35) and (4.36). Solutions can be built from any divergent free flow, with ∇·u = 0, that obeys u = - (g/f) ∂η/∂y and v = + (g/f) ∂η/∂x (4.37)

Here the height η acts like a streamfunction of the kind we met in Section 1.1.4. Steady-state solutions of this form are said to be in geostrophic balance. It’s easy to understand the balance of forces underlying geostrophic balance. Suppose that there is some bump in the hei ght of the fluid. Gravity, of course, wants to pull this down but, because the underlying fluid is incompressible, it results in a horizontal force in the direction ∇η. The velocity in geostrophic balance is such that it gives rise to Coriolis force that balances gravity.

Flows in geostrophic balance (4.37) obey u · ∇η = 0. In other words, the flow is along lines of constant height η. But, from hydrostatic balance (4.31), we know that the pressure in the fluid is proportional to the height. In other words, the flow is along isobars. This is familiar from weather maps, where wind blows along lines of constant pressure, rather than from high to low pressure as one might naively expect. The large scale flow of both the ocean and atmosphere is largely in geostrophic balance.

Potential Vorticity

Our next task is to understand time-dependent solutions to the shallow water equations. To do this, it’s best to first look more closely at the various conserved quantities. In fact, it’s best if we briefly return to the full non-linear equations (4.30), (4.32) and (4.33). These admit two conserved quantities. The first is simply the height, whose conservation follows from the underlying conservation of mass ∂h/∂t + ∇·(uh) = 0 with h = H + η (4.38)

The second is conservation of vorticity. It can be checked that ∂W/∂t + ∇·(uW) = 0 with W = −∂v/∂x + ∂u/∂y + f (4.39)

In this equation, both ∇ and u are now 2d vectors, rather than 3d. Note that the vorticity includes the extra +f contribution from the Coriolis force.

Both (4.38) and (4.39) are continuity equations, which is the usual conservation law that we know and love. Elsewhere in these lectures, we’ve been able to use the incompressibility condition ∇ · u = 0 to extract the velocity u from the clutches of the spatial derivative and write equations of this form as the vanishing of a material derivative. But we’re not allowed to do this in the present context because the 2d velocity u does not necessarily obey ∇ · u = 0. The fluid is still incompressible of course, but the 2d velocity u can pile up at some point at the expense of increasing the height. Indeed, this is what our first equation (4.38) is telling us. Nonetheless, we can combine (4.38) and (4.39) to construct a quantity that has vanishing material derivative. This is DQ/Dt = ∂Q/∂t + u·∇Q = 0 with Q = W/h = (−∂v/∂x + ∂u/∂y + f)/(H + η) (4.40)

The quantity Q is called the potential vorticity. The equation DQ/Dt = 0 is telling us that the value of the potential vorticity doesn’t change as we follow the flow.

The discussion above is for the full non-linear equations. Something rather striking happens when we restrict to the linear equations. We linearise the conservations laws (4.38) and (4.39) about h = H and W = f, to find ∂h/∂t + H∇·u = 0 and ∂W/∂t + f∇·u = 0

The surprising fact is that these both have the same current: it is simply the velocity u. This means that we can eliminate the current to find the linearised conservation law ∂Q/∂t = 0 with Q = −∂v/∂x + ∂u/∂y − fη/H (4.41)

The quantity Q is (up to constant term and a scaling by H) the linearised potential vorticity. We see that Q is independent of time. That’s a much stronger statement than our usual conservation laws. Usually when something is conserved, its value can change at some point in space by moving to a neighbouring point. That’s the physics of the continuity equation. But now we learn that the function Q simply can’t change at any point in space! That adds a rigidity to the system that will be responsible for some of the features we’ll see below.

Poincaré Waves

With this understanding of potential vorticity in hand, we’ll now turn to some wave solutions of the linearised shallow water equations (4.34), (4.35) and (4.36). If there were no rotation, it’s clear what would happen. With f = 0, it’s simple to check that the equations (4.34), (4.35) and (4.36) become the wave equation η¨= c²∇²η with c² = gH. This describes surface waves propagating with speed c and reproduces our previous result (4.13) for long wavelength waves.

The Coriolis force changes this. If we assume that f = constant (which means that we are neglecting the effects of the curvature of the Earth), then the wave equation that we derive from (4.34), (4.35) and (4.36) is ∂²η/∂t² = c²∇²η − Hf(∂v/∂x − ∂u/∂y) with c² = gH

The additional terms can be rewritten in terms of the potential vorticity (4.41) to get ∂²η/∂t² − c²∇²η + f²η = −HfQ (4.42)

where Q is the potential vorticity which, as we have seen above, is a constant function that doesn’t change with time. For a given problem, one might have to solve (4.42) for some fixed Q. But, in addition, one can always add solutions to the complimentary solution which solves the homogeneous equation ∂²η/∂t² − c²∇²η + f²η = 0 (4.43)

where, as before, c² = gH. This is a rather famous equation that, in the world of Quantum Field Theory, it is known as the Klein-Gordon equation. It is a simple matter to find solutions by writing η(x,t) = η̃ e^{iωt−ik·x} with x = (x,y) and k = (k_x, k_y). This solves (4.43) provided that the frequency ω and wavevector k obey the dispersion relation ω² = c²k² + f² (4.44)

These are known as Poincaré waves. They are a form of gravity wave, since gravity acts as the restoring force, as seen in the speed c = √(gH). But their properties are affected by the Coriolis force. They are sometimes referred to as inertia-gravity waves.

For long wavelengths, k → 0, Poincaré waves have a finite frequency, set by the Coriolis parameter ω → f. In the language of quantum mechanics, we say that the spectrum is gapped, the “gap” being the smallest frequency at which the system oscillates. (In quantum mechanics this translates into a gap in the energy spectrum because E = ℏω.)

The cross-over from “short” to “long” wavelengths happens at the length scale R = c/f = √(gH)/f (4.45)

This is known as the Rossby radius of deformation. It is the characteristic length scale in the shallow water equations. (For the ocean at mid-latitudes, one has R ≈ 1000 km.) Short wavelength modes, with k ≫ R⁻¹, act just like usual surface waves, with ω ≈ ck. It’s the long wavelength modes, with k ≪ R⁻¹, that feel the effect of the Coriolis force. In this limit, we can neglect the η-terms in (4.34) and (4.35) to find that the velocities obey u̇ = fv and v̇ = −fu. This tells us that the wave velocity in the x and y-directions are π/2 out of phase.

In preparation for what follows, it’s worth redoing the above calculation in a slightly different way. We write our three, linearised shallow water equations (4.34), (4.35) and (4.36) as a combined matrix eigenvalue equation ∂Ψ/∂t = i M Ψ with M = [[0, -c∂_x, -c∂_y], [-c∂_x, 0, f], [-c∂_y, -f, 0]] and Ψ = [[√(g/H)η], [u], [v]] (4.46)

We’ve done some cosmetic manipulations to get the equation in this form. In addition to rescaling the η variable, we’ve also multiplied everything by a factor of i. This makes the resulting equation look very much like a time-dependent Schrödinger equation. In particular, the matrix M is Hermitian. With our wave ansatz Ψ = Ψ̃ e^{iωt−ik·x}, this becomes a standard eigenvalue problem [[0, ck_x, ck_y], [ck_x, 0, -if], [ck_y, if, 0]] Ψ̃ = ω Ψ̃ (4.47)

Because this is a Hermitian matrix, the eigenvalues are guaranteed to be real. They are ω = ± √(c²k² + f²) and ω = 0 (4.48)

We recognise the first of these as the dispersion relation for Poincaré waves (4.44). In addition, there are a collection of solutions with ω = 0. In the context of condensed matter physics, this is known as a flat band (because if you plot ω vs k it is a flat plane.) The existence of the flat band follows from the functional conservation of the potential vorticity. It is telling us that there are additional, time independent equilibrium solutions. These are solutions like (4.45) that exhibit geostrophic balance.

4.3.3 We Need to Talk About Kelvin Waves

Everyone likes a trip to the coast. Now it’s our turn. For the purposes of this course, the coast is not going to be very exciting. It’s simply a boundary of our fluid, which we will take to run North/South. The fluid exists only in the x ≥ 0 direction. For x < 0, there is only land.

Obviously we must put a boundary condition u = 0 at x = 0, ensuring that no flow passes the boundary. In fact, we’ll do something more extreme than this. We will search for solutions that have u = 0 everywhere. The linearised shallow water equation (4.35) then becomes v = (g/f) ∂η/∂x (4.49)

This is telling us that the fluid lives in geostrophic balance in the x-direction, with the pressure gradient from ∂η/∂x pushing against the Coriolis force that arises because the fluid has velocity v in the y-direction. Meanwhile, the other two shallow water equations (4.34) and (4.35) become ∂η/∂t = −H ∂v/∂y and ∂v/∂t = −g ∂η/∂y

These are standard wave-like equations. If we make the usual ansatz that v = v₀(x) e^{iωt−iky} and η = η₀(x) e^{iωt−iky}, these become ωη₀ = kHv₀ and ωv₀ = gkη₀ ⇒ ω² = c²k² with the speed given by c = √(gH) as for our previous examples. So far, things look fairly standard. But there’s a slight twist in the tail. This arises when we return to (4.49) which tells us the profile of the water near the boundary. We have ∂η/∂x = (fω)/(kc²) η₀

Our dispersion relation ω² = c²k² naively suggests that we have two options: ω = +ck or ω = −ck. But that’s not right. Suppose that we take f > 0, which is appropriate if we are in the Northern hemisphere. Then if we pick ω = +ck we’re in trouble, because the height of the water will grow exponentially away from the boundary: η₀(x) ∼ e^{+fx/c}. And that’s bad. It means that we should throw away this solution. The only physical solution has ω = −ck with the water profile decaying exponentially away from the boundary, η₀(x) ∼ e^{−fx/c}. This means that the boundary waves propagate only in one direction which, in the current set-up, is the negative y-direction, also known as South. These are known as Kelvin waves.

Waves that propagate only in one direction are said to be chiral. In the Northern hemisphere, with f > 0, Kelvin waves propagate so that the land always sits to their right. (In other words, if these waves are propagating on the boundary of a lake, then they move in an anti-clockwise direction.) In the Southern hemisphere, where f < 0, the same argument tells us the we must have the ω = +ck solution, so Kelvin waves propagate with the land to its left as it moves.

Chiral waves also make an appearance in various condensed matter systems where, as here, they typically live at the edge of some system. In that context, there is often some deep topological reason for the emergence of such chiral waves. The same is also true here and we will elaborate on this further in Section 4.3.6.

4.3.4 Rossby Waves As we’ve seen, the linearised shallow water equations admit time independent solutions in geostrophic balance, solving (4.37). But objects that are strictly unmoving are rare in Nature. One can ask: is there something that can coax flows to geostrophic balance to move? The answer, as we shall see, is yes. In this section, we will see that if we look at scales over which the Coriolis parameter f is no longer constant, then flows in geostrophic balance start to evolve in time. This is known as quasi-geostrophic balance. Crucially, the evolution of flows in quasi-geostrophic balance happens much more slowly than the dynamics of Poincaré waves that we saw above. That means that it is this quasi-geostrophic flow governs the long-time dynamics of the ocean and atmosphere. The purpose of this section is to construct the equations that describe this flow.

At different latitudes θ, the Coriolis parameter is given by f = 2Ωsinθ, where Ω = 2π day−1. To capture the variation of the Coriolis parameter, it will suffice to consider just the leading term in the Taylor expansion f = f + βy with y the direction points North. Our strategy will be to turn again to the conservation of potential vorticity (4.40), DQ/Dt = 0 with Q = (1/H + η)(∂v/∂x − ∂u/∂y) + f.

You can check that this equations remains valid even when f = f(x). We will consider flows with Rossby number Ro ≪ 1 that are very close to geostrophic balance (4.37). This means that we can replace the vorticity in the expression with, ∂v/∂x − ∂u/∂y = ∇²η ≈ (g/f) ∇²η.

We further assume that variations in the height are small, so η ≪ H, and the potential vorticity can be written solely in terms of the height fluctuations η. Ignoring an overall constant term, we have Q ≈ (f₀/H²) [c² ∇²η − f₀² η + βH f₀ y]. (4.50)

As we’ve seen, potential vorticity is materially conserved and, using the geostrophic balance condition (4.37), this too becomes an equation that can be written solely in terms of the height DQ/Dt = 0 ⇒ Q ∂η/∂t + (g/f₀) ∂η/∂y ∂Q/∂x − (g/f₀) ∂η/∂x ∂Q/∂y = 0. (4.51)

This is now a dynamical equation for the height η. It is known as the shallow water quasi-geostrophic equation.

The quasi-geostrophic equation looks a little daunting. But we can easily extract some simple physics. We linearise about a flat surface with η = 0 and drop any term quadratic in η. The equation then becomes ∂/∂t (c² ∇²η − f₀² η) + c² β ∂η/∂x = 0.

We see clearly that the term with β, which captures the variation of the Coriolis parameter, is driving the dynamics. If we look for plane wave solutions with η = η₀ ei(ωt−k·x), we find the dispersion relation ω = −βc² kx / (c²k² + f₀²). (4.52)

When β = 0, this gives us the flat band ω = 0 that corresponds to steady-state geostrophically balanced flows. But once we take into account the variation of the Coriolis parameter, these flows start to move. The resulting waves are called Rossby waves. The minus sign in (4.52) is important. It is telling us that long wavelength (small k) waves travel in a westward direction. This is indeed the dominant motion of the ocean seen in satellite images. These images clearly reveal Rossby waves that take months, or even years, to cross the Pacific ocean.

It’s useful to summarise what we’ve seen here. The shallow water equations admit two classes of solutions: fast-moving Poincaré waves and slow-moving quasi-geostrophic flows, including Rossby waves. The magic of the quasi-geostrophic equation (4.51) is that it has successfully filtered out the fast-moving Poincaré waves, leaving us just with the slow-moving modes. It is what is referred to in other areas of physics as the “low energy (or frequency) effective field theory”. Historically, the development of the quasi-geostrophic equation was crucial in developing successful weather prediction.

4.3.5 Equatorial Waves We now ask: what happens when we sit at the equator. Here the Coriolis parameter (4.29) vanishes, f = 2Ω·ẑ = 0 and one might naively think that there can’t be any interesting physics due to the Coriolis force. In fact, things are more subtle and more interesting.

To find the more interesting physics, we look a little away from the equator. If we Taylor expand, the Coriolis parameter becomes position dependent f(y) = βy.

Here the y-direction is North, and y = 0 corresponds to the equator. The parameter β has dimension [β] = L−1T−1. We can form a distance scale Leq = (c/β)^(1/2).

For the Earth’s oceans, this is around Leq ≈ 250 km. It is somewhat larger for the atmosphere.

We again arrange the height perturbation η(x,y,t) and the velocities u(x,y,t) and v(x,y,t) as a vector Ψ(x,y,t) as in (4.46). This time we will look for solutions that are localised near the equator but propagate as waves in the x-direction (i.e. East/West), Ψ(x,y,t) = Ỹ(y) ei(ωt−ikx). (4.53)

The shallow water equations now become [ 0, ck, ic∂/∂y; ck, 0, −iβy; ic∂/∂y, iβy, 0 ] Ỹ = ω Ỹ.

Again, we’re looking for eigenmodes of this equation. As in the case when f was constant, we expect different branches.

Equatorial Kelvin Waves To kick us off, there is a special solution to (4.53). This occurs when v = 0, so there is no velocity in the y-direction. The equations coming from the first two components of (4.53) are simply algebraic. They relate ũ = (ω/kH) η̃ and result in the dispersion relation ω² = c²k² ⇒ ω = ±ck. (4.54)

We’re left just with the third component of (4.53), which governs the profile of η̃(y) and ũ(y) in the y-direction, c² ∂η̃/∂H ∂y = −βy ũ ⇒ ∂η̃/∂y = −(ω/ck)(y/L²eq) η̃.

The key feature of the solution comes from that factor of ω/ck on the right-hand side. From the dispersion relation (4.54), this is either ±1. However, the resulting solution is only normalisable, and localised around the equator, if we take the positive sign ω = +ck ⇒ η̃ = η₀ e^(−y²/2L²eq).

The other choice of sign, with ω = −ck, leads to a divergent solution η̃ ∼ e^(+y²) which is not physically permissible. The upshot is rather nice: we have waves at the equator that only travel in the positive x-direction. In other words, they only go east. In analogy with the coastal waves that we met in Section 4.3.3, these are known as equatorial Kelvin waves.

Rossby, Poincaré and Yanai Waves Let’s now return to the general problem of equatorial waves, given by the Schrödinger-like equation (4.53). The second component of (4.53) is algebraic and allows us to eliminate ũ in favour of ṽ and η̃. This results in a pair of coupled, first order differential equations i (∂/∂y − βky/ω) ṽ = (ω − c²k²/Hω) η̃, i (∂/∂y + βky/ω) η̃ = (ω − β²y²/c²ω) ṽ. (4.55)

We can eliminate η̃ to manipulate this into a second order differential equation for ṽ alone. After a little bit of algebra, this is [−c² ∂²/∂y² + β²y²] ṽ = [ω² − c²k² − βc²k/ω] ṽ.

But this is an equation that we’ve seen elsewhere: it is the Schrödinger equation for the harmonic oscillator that we met in our first course in Quantum Mechanics. In that context, we write [−ℏ² ∂²/2m∂y² + (1/2) m ω̄² y²] ψ_n = E_n ψ_n, where m is the mass of the particle and ω̄ is the frequency of the harmonic oscillator (not to be confused with ω, the frequency of our waves the we’re trying to determine). Because we are again interested in normalisable solutions, we can simply import our results from quantum mechanics. The velocity ṽ(y) is given by Hermite polynomials. More importantly, the energies of the harmonic oscillator are, famously, E_n = ℏω̄ (n + 1/2) with n = 0,1,...

Translating back into the variables of our equatorial waves, the dispersion relation is given by ω³ − ω (c²k² + βc(1+2n)) − βc²k = 0 with n = 0,1,2,.... (4.56)

We’ll now look at these for different n. We’ll see, the n = 0 waves are somewhat different from the n ≥ 1 waves.

Let’s start with the n = 0 waves. First note that in this case (4.56) has a root ω = −ck. Naively, this looks like a wave moving in the opposite direction to the Kelvin wave. But it is a spurious solution. This is because although ṽ(y) is normalisable, when we plug this solution into (4.55) we find that η̃(y) is non-normalisable: it has a piece that diverges as η̃ ∼ e^(+y²/2L²eq). So this solution should be thrown out. It turns out that it’s the only spurious solution and all others are fine.

If we factor out the spurious ω = −ck solution, then we find a single n = 0 wave, with dispersion relation ω = ± (ck/2) [1 ± √(1 + 4βc/(c²k²))]^(1/2).

This too is a chiral wave. At large wavenumber, it has the same dispersion relation ω ∼ +ck as the Kelvin wave. However, it differs at small wavenumber, with the dispersion relation affected by the Coriolis force. These are known as Yanai waves. (They are also sometimes called mixed Rossby-gravity waves.) The velocity profile is Gaussian around the equator, with ṽ ∼ e^(−y²/2L²eq).

For n ≥ 1, the general shape of the dispersion relation takes the same form. There are three branches of modes, which are modified versions of the dispersion relations (4.48) that we saw when f is constant. We again see the dispersion relations correspond...

According to Poincaré waves, with their characteristic gapped spectrum, asymptoting to ω → ±ck. In addition, we see that our flat band, which previously had ω = 0, is also deformed. Now, it is no longer flat, but asymptotes to ω → −β/k for large |k|. These are equatorial Rossby waves. The various modes for n = 0,1,2,3, together with the Kelvin wave, are shown in Figure 22. Note that the dispersion relation for the Rossby waves is much flatter than those of the Poincaré waves. Correspondingly, the group velocity of the Rossby waves will be much slower.

4.3.6 Chiral Waves are Topologically Protected

As we mentioned previously, chiral waves appear in various condensed matter systems. The most familiar example is the Quantum Hall Effect, where a sample of electrons in a magnetic field has chiral modes propagating on its edge. In the context of condensed matter, it turns out that the presence of chiral edge modes can be traced to some interesting topological features of the system, an observation that led to many new developments in the field. The purpose of this section is to point out that, rather wonderfully, the same is true for chiral waves in fluids. I should warn you that this section is something of a departure from the rest of the notes and the motivation is, in part, simply to illustrate the unity of physics. We will describe the topology associated to equatorial chiral modes. (There is a similar, but more complicated, story for coastal Kelvin waves.) The idea is that the existence of the two chiral modes – Kelvin and Yanai – is a direct consequence of topology in momentum space.

To set the scene, we will return to the case of constant Coriolis parameter f. As we’ve seen in (4.48), there are three bands with dispersion ω = ± √(c²k² + f²) and ω = 0 (4.57). The resulting bands are shown in Figure 23 for three cases: f > 0, f = 0 and f < 0. For f ≠ 0, there is a gap between the geostrophic flat band and the Poincaré waves. This gap closes when f = 0. The fact that the gap closes at f = 0 is closely related to the existence of the chiral equatorial waves. The question that the topological approach addresses is: how robust is this situation? Could we, for example, add some further parameters to the problem so that, as we vary f from positive to negative, the gap never closes? Topology tells us that the answer to this is: no. There must always be some point that looks like the f = 0 figure where the gap closes.

The reason for this is that there is a subtle difference between the f > 0 and f < 0 situations. This difference doesn’t show up in dispersion relations (4.57) which are clearly symmetric under f → −f. Instead, we have to look more closely at what’s going on in each band. Recall from (4.47) that the frequencies arise as the solution to the following eigenvalue problem

\begin{pmatrix} 0 & ck_x & ck_y \\ ck_x & 0 & -if \\ ck_y & if & 0 \end{pmatrix} \tilde{\Psi} = \omega \tilde{\Psi}

We will focus on the positive frequency band of Poincaré waves, with ω(k) = + √(c²k² + f²). As we’ve already mentioned, the eigenvalues are clearly invariant under f → −f. To see the difference between +f and −f we need to look at the eigenvector. This is given by

\tilde{\Psi}(k,f) = \frac{1}{\sqrt{2\omega^2 k^2}} \begin{pmatrix} ck^2 \\ k\omega - ifk \\ k\omega + ifk \end{pmatrix}

Obviously, the eigenvector depends on the wavenumber k. This means that as we move around momentum space, labelled by k ∈ R², the eigenvector \tilde{\Psi} evolves in C³. The key idea is that as we explore all of momentum space, the eigenvector may twist within the larger space C³. This twist is where topology enters the story.

The fact that eigenvectors twist and turn in a larger space is more familiar in the context of quantum mechanics where it goes by the name of Berry phase. (You can read about this both in the lectures on Topics in Quantum Mechanics and in the lectures on the Quantum Hall Effect.) We will not review this in detail, but simply state how to characterise the topology of the eigenvector. First, given an eigenvector \tilde{\Psi} we define the Berry connection, A_i(k) = -i \tilde{\Psi}^\dagger \partial_{k_i} \tilde{\Psi} for i = 1,2. A short calculation shows that A = (k_y, -k_x) \frac{c^2 f}{(f^2 + c^2 k^2)^{3/2}}. The Berry connection has the same mathematical structure as the gauge potential in electromagnetism. In particular, as the next step we compute something akin to the magnetic field, B = \partial_1 A_2 - \partial_2 A_1 = \frac{c^2 f}{(f^2 + c^2 k^2)^{3/2}}. This is known as the Berry curvature. Finally, we integrate this curvature over momentum space to get an object known as the Chern number, which we calculate to be C = \frac{1}{2\pi} \int_{\mathbb{R}^2} d^2k B = \text{sign}[f] (4.58).

Note that, as promised, the Chern number distinguishes between f positive and f negative: we have C = +1 for f > 0 and C = −1 for f < 0. At this stage the argument becomes slightly delicate. When the Chern number is computed by integrating over a compact space (i.e. one which doesn’t stretch to infinity), then there is a mathematical result that says C ∈ ℤ. (In physics, this is usually referred to as Dirac quantisation.) The fact that C is integer valued is important. It is telling us that we have some discrete way of characterising the system, even though the underlying fluids are continuous. This is the essence of topology.

However, things are not so straightforward for our fluids because the integral (4.58) is not over a compact space but instead over R². (This is not a problem in condensed matter systems because the underlying spatial lattice means that momentum lives in a compact Brillouin zone.) And there’s no mathematical theorem that says such an integral should be integer valued. Indeed, if you integrate the magnetic flux through a solenoid then you can get anything at all. There are a couple of ways around this and we will take the cheapest. Note that asymptotically, as |k| → ∞, we have A → 0. In fact, more importantly, we have ∫ A dk_i → 0 as the integration curve is taken out to infinity. This is a property of short wavelength modes and so should hold regardless of any deformation of the system which doesn’t affect arbitrarily short wavelengths. So we insist that A is trivial asymptotically and this allows us to effectively compactify the problem, by adding a point at infinity and viewing R² ∪ {∞} = S². Correspondingly, we learn that the Chern number C – which is clearly an integer in (4.58) – should remain an integer no of the gas. You can find derivations of both these equations of state in the lectures on Statistical Physics. We can make contact with our previous equation if we replace the volume with the density ρ of the fluid, ρ = Nm where m is the mass of the each individual particle in the fluid. Then the ideal gas law becomes P = ρkT / m (4.60)

When we first meet the equation of state, we think of P, ρ ∼ 1/V and T as numbers that describe the global, equilibrium properties of the system. However, the whole point of fluid mechanics is that we can understand what happens as we move away from equilibrium. To achieve this, we assume that locally the system is still described by P, ρ and T but these are now dynamical fields whose values can vary in space and in time. The equation of state now gives a local relationship between these quantities, for example P(x,t) = ρ(x,t)kT(x,t) / m The existence of the equation of state tells us why we need to start thinking about temperature. If the pressure P and density ρ are changing, then so too is T. Indeed, this is true even when ρ is constant but throughout these lectures we have implicitly assumed that T(x,t) simply tracks the pressure P(x,t). Now, however, we need to think more carefully about how T changes.

4.4.2 Some Thermodynamics The correct way to proceed is to derive an equation of motion for the temperature T(x,t). For now, however, we’ll take something of a shortcut. For completeness, we will then describe the better approach in Section 4.4.3.

The shortcut that we have in mind is called the adiabatic approximation. Heuristically, this means that we assume that the timescale over which the fluid moves is much shorter than the timescale of heat diffusion within the fluid. Mathematically, it means that we assume a quantity called entropy is conserved. The purpose of this section is to review some basic facts about thermodynamics, the purpose of which is to lead us to the following, simple result: under the adiabatic approximation ρ^γ = constant (4.61)

where γ is the ratio of heat capacities γ = c_P / c_V and will be defined below. For air, γ ≈ 1.4. Starting in Section 4.4.4 we’ll make use of this result to study the properties of sound waves.

For now, we’ll revert to the older setting where P, V and T as just numbers that characterise the global property of an equilibrium system. We then need to turn to the laws of thermodynamics. (A much fuller discussion of this material can be found in Section 4 of the lectures on Statistical Physics.)

The first law of thermodynamics says that the energy E of a system can change in one of two ways: either by adding heat δQ, or by adding work, δW dE = δQ + δW The energy is a function of the system, but both heat and work are things that you do to the system. There’s no sense in which we can talk about the "work" of a gas or the "heat" of a gas; only the heat added to a gas. Roughly speaking, this is the reason that we write the terms on the right-hand side as δQ and δW instead of dQ and dW. However, it should be possible to describe the effect of both the work done and the heat added in terms of changes to the state of the system. For the work done, this is straightforward. If the fluid has pressure P and we squeeze it by changing its volume, then the infinitesimal work done is δW = −PdV To write a similar statement for the heat added to a gas we need to turn to the second law of thermodynamics. This is the statement that the state of the system in equilibrium can be characterised by a function S(T,P) known as entropy. Furthermore, for a reversible change we have δQ = TdS This definition, relating entropy to heat, is due to Clausius. Subsequently, Boltzmann understood entropy in terms of counting microscopic arrangements of atoms. A large part of the course on Statistical Physics is to understand why these two definitions are actually equivalent. For our purposes, we’ll only need the definition above.

Adiabatic processes, of which sound waves are an example, have δQ = 0. You might think that this means we can simply ignore the heat term. Sadly, that’s not quite true! We need to understand a little better what heat actually is before we can discard it.

Next, we need the idea of a heat capacity. This is straightforward: it measures how much the temperature of a system rises if you add some heat. (Actually, it’s defined to be the inverse of this.) The subtle point is that you must specify what you are holding fixed when you do this experiment. You could, for example, hold the volume fixed. The corresponding heat capacity C_V is defined by C_V = T (∂S/∂T)_V = (∂E/∂T)_V where, in the second equality, we’ve used the first law of thermodynamics dE = TdS − PdV where the −PdV term doesn’t contribute precisely because we’re holding the volume fixed. Alternatively, we can add heat keeping the pressure fixed, rather than the volume. Again, using the first law, we have C_P = T (∂S/∂T)_P = (∂E/∂T)_P + P (∂V/∂T)_P (4.62)

In this case, the temperature is expected to rise less because the energy from the heat must now also do work expanding the volume of the gas. Correspondingly, we expect C_P > C_V. We often talk about the specific heats, which is the heat capacity per unit volume: c_V = C_V/V and c_P = C_P/V.

The Ideal Gas So far, our discussion has been general. To make progress, we now focus on a specific system: the ideal gas, with the familiar equation of state PV = NkT This is a good approximation for dilute gases, like the air in this room. It’s not a good approximation for liquids.

The final fact that we need is known as equipartition. It is the statement that, at temperature T, the energy of each microscopic degree of freedom is given by ½kT. This means that if we have a gas of N "monatomic" particles, meaning that each particle is itself a structureless object, then E = ³⁄₂NkT for monatomic gases where the 3 comes because each particle can move in three dimensions. However, if the particles comprising the gas have additional internal degrees of freedom then equipartition ensures that these too contribute to the energy. For example, a diatomic molecule can be viewed as a dumbbell-like object. It has three translational degrees of freedom, but also two rotational degrees of freedom. (The rotation about the axis doesn’t count⁸.) This means that the energy is E = ⁵⁄₂NkT for diatomic gases Air is mostly N₂ and O₂, both of which are diatomic molecules, so this is the energy of air.

We can now compute the heat capacities for the different ideal gases. We have C_V = ³⁄₂Nk and C_P = ⁵⁄₂Nk for monatomic gases and C_V = ⁵⁄₂Nk and C_P = ⁷⁄₂Nk for diatomic gases Note that, in both cases, C_P − C_V = Nk, which follows from (4.62), together with the equation of state. It will be useful to define the ratio of the heat capacities γ = C_P / C_V = { ⁵⁄₃ for monatomic gases { ⁷⁄₅ for diatomic gases This is where we get the statement that γ ≈ 1.4 for air.

⁸ Rather wonderfully, this is a quantum mechanical effect! Both the rotation about the axis and the vibrational mode of the dumbbell have a minimum energy required to excite them due to quantum mechanics, and this energy is higher than kT at room temperatures. The same is true of the rotational mode of a monatomic gas.

Finally, we can use the technology above to compute the entropy of an ideal gas. We start from the first law, now written as dS = (1/T)dE + (P/T)dV = (C_V/T)dT + (Nk/V)dV We now replace Nk = C_P − C_V and integrate to get S = C_V log(T/T₀) + (C_P − C_V) log(V/V₀)

= C_V log( T / (V^(γ−1)) ) (4.63)

( T₀ / V₀ )

= C_P log( (PV^γ)^(−1/γ) ) / const.

( P₀ V₀ )

This means that if entropy is to remain constant under some change, the pressure and volume must scale so that PV^γ is constant. Or, written in terms of the density ρ ∼ 1/V, P / ρ^γ = constant (4.64)

This is the result (4.61) that we advertised at the beginning of this section.

4.4.3 Briefly, Heat Transport There’s a more sophisticated way of stating the result above, in which we focus directly on the dynamics of the temperature field T(x,t). For an ideal fluid, the temperature is governed by the transport equation ∂T/∂t + u·∇T + (γ − 1)T ∇·u = 0 (4.65)

We won’t derive this here. (You can find the derivation in the lectures on Kinetic Theory.) But we can at least see how it reproduces the result above. To see this, note that the requirement of constant entropy can also be written as TV^(γ−1) ∼ Tρ^(1−γ) is constant, as in (4.63). But with T and ρ both fields, we can see how these evolve within the fluid. The appropriate meaning of "constant" is that the material derivative vanishes. We have D(Tρ^(1−γ))/Dt = (∂/∂t + u·∇)(Tρ^(1−γ))

= (1−γ)ρ^(1−γ)T∇·u + T(∂ρ^(1−γ)/∂t + u·∇ρ^(1−γ))

Here the first term follows from (4.65). We can evaluate the second term using the conservation of mass (4.59). We find D(Tρ^(1−γ))/Dt = 0 as expected for adiabatic evolution.

This language has the advantage that it allows us to go beyond ideal fluids. In fact, the heat transport equation (4.65) should be viewed as analogous to the Euler equation for the velocity: both are missing the effect of dissipation. For the velocity field, this is captured by viscosity. For the temperature field, it is captured by heat conductivity κ. This appears as an additional term in the heat equation ∂T/∂t + u·∇T + (γ − 1)T ∇·u = (κm / (γ ρ k)) ∇²T (4.66)

where the strange collection of coefficients on the right-hand side means that the coefficient multiplying ∇²T can be identified as κ/c_P where c_P = ρk γ/((γ−1)m) is the specific heat at constant pressure. These terms tell us how heat diffuses in the fluid. Indeed, in the absence of any flow, so u = 0, it reduces to the heat equation ∂T/∂t = (κ / c_P) ∇²T The adiabatic approximation that we invoke...

The statement that the diffusion of heat can be neglected in the problem of interest. And that problem is, of course, sound waves.

4.4.4 The Equations for Sound Waves Finally, after that long preamble, we can turn to the subject of interest: sound waves. We will initially ignore viscosity (remedying this in Section 4.4.5) and work with the Euler equation

ρ ∂u/∂t + u·∇u = −∇P

Our starting point is the simplest possible solution to the Euler equation: a stationary fluid, with constant density and pressure

u = 0 , ρ = ρ₀ , P = P₀

We then study small perturbations about this background. We will take

ρ = ρ₀ + ρ̃ and P = P₀ + P̃

with the perturbations small, meaning ρ̃ ≪ ρ₀ and P̃ ≪ P₀. We’ll also take u to be small, in the sense that we keep terms only linear in u, ρ̃ and P̃. The linearised Euler equation then becomes

ρ₀ ∂u/∂t = −∇P̃   (4.67)

We augment this with the equation of mass conservation,

∂ρ̃/∂t + ρ₀ ∇·u = 0   (4.68)

We can combine these by taking the gradient ∇ of the first and the time derivative of the second. This gives

∂²ρ̃/∂t² − ∇²P̃ = 0   (4.69)

At this point, we need to invoke the adiabatic approximation (4.64) which, after linearising, becomes

((P₀ + P̃)/(ρ₀ + ρ̃)^γ) = constant ⇒ P̃ − γρ̃ = 0

The equation (4.69) then becomes

∂²ρ̃/∂t² − c²ₛ∇²ρ̃ = 0   (4.70)

This is the wave equation. The speed of sound is given by

c = sqrt(γP₀/ρ₀)   (4.71)

For an ideal gas, the equation of state (4.60) relates this to the temperature T₀ of the background fluid, and the mass m of the constituent particles,

c = sqrt(γk_B T₀ / m)   (4.72)

We see that the speed of sound depends on the temperature. For the air at 20◦, the speed is c ≈ 340 ms⁻¹. This was first measured by Newton by clapping his hands in Nevile’s court, Trinity College. (He got a value around 300 ms⁻¹.)

A General Fluid The equation (4.69) holds for any fluid while, the subsequent derivation of the wave equation, we restricted to the ideal gas. But we get the same wave equation for any equation of state; it’s just the speed of sound that changes.

It’s useful to think of the pressure as a function of

P = P(ρ, S)

(It’s perhaps more natural to think of P = P(V, T). The density is trivially related to the volume by ρ ∼ 1/V. But the entropy S is a conjugate variable to the temperature T and it is also possible to think of pressure as a function of entropy. This kind of “what function depends on what variable” is a large part of the game of thermodynamics.)

Taylor expanding, the fluctuations in pressure and density are then related by

P̃ = (∂P/∂ρ) ρ̃

In general, the speed of sound is then given by

c = sqrt(∂P/∂ρ)   (4.73)

Measurements of this derivative are usually given in terms of the bulk modulus, defined to be K = ρ ∂P/∂ρ. For water at 20◦, this is K ≈ 200 Nm⁻². It’s much higher than the corresponding value for gases, reflecting the fact that it is more difficult to squeeze water than air. The density of water is ρ ≈ 10³ kgm⁻³. The speed of sound in water is then much higher than in air, c ≈ 1500 ms⁻¹.

Sound Waves are Longitudinal The wave equation (4.70) is solved by any Fourier mode

ρ̃(x, t) = ρ̂ e^(ik·x − iωt)   (4.74)

Here ρ̂ is the constant amplitude of the wave. In the exponent, ω is the frequency and k is the wavevector which points in the direction of propagation. The two are related by the dispersion relation

ω = c |k|

This is now a dispersion relation that doesn’t disperse, in the sense that all wavelengths propagate with the same speed. As we’ve seen, this contrasts with the surface waves of Section 4.1. Because the wave equation is linear, we can combine many Fourier modes to make a wavepacket. If this is made from wavevectors k that all point in the same direction, then the wavepacket will keep its shape as it moves. We can also see this directly from the wave equation. If the wave is moving in the x-direction, then the wave equation is solved by any function of the form

ρ̃ = F(t − x/cₛ) + G(t + x/cₛ)   (4.75)

Here F and G are the profiles of two wave packets, moving to the right and left respectively.

We can reconstruct the pressure and velocity oscillations from our original, first order equations. The pressure perturbations are simply given by P̃ = c²ₛ ρ̃. From (4.68) we have

û(x, t) = (k / (ω ρ₀)) P̃(x, t) = (k / (ω ρ₀)) ρ̃(x, t)

The oscillations of the fluid velocity and the pressure are all in phase with the density. The velocity oscillations are also parallel to the direction k in which the wave travels. Such waves are called longitudinal.

Spherically Symmetric Waves Although we can construct any solution from the Fourier modes (4.74), that’s often not the best way to proceed. For example, if we have some localised source which, for convenience, we will assume is spherically symmetric then it’s clear that we are best served by working in spherical polar coordinates. Ignoring the angular directions, the wave equation becomes

∂²ρ̃/∂t² − c²ₛ∇²ρ̃ = 0 ⇒ ∂²(rρ̃)/∂t² − c²ₛ ∂²(rρ̃)/∂r² = 0

This is now a 1d wave equation. It is solved, analogously to (4.75) by any two functions

ρ̃(r, t) = [F(t − r/cₛ) + G(t + r/cₛ)] / (4πr)

The factor of 4π is just for convenience. The function F describes the outgoing wave, while G describes the incoming wave. In many situations, there’s no wave coming in from infinity so we set G = 0. This is the choice we make here.

The associated velocity field is most simply computed from (4.67) using P̃ = c²ₛ ρ̃. To write down the solution, we need to integrate the wave profile. We write

F(t − r/cₛ) = Q̇(t − r/cₛ)

In spherical polars, we then have

∇P̃ = −(c²ₛ/(4πr²)) [ Q̈(t − r/cₛ) − (cₛ/r) Q̇(t − r/cₛ) ] r̂

and, comparing to (4.67), the velocity field is radial, with

u(r, t) = (c²ₛ/(4πρ₀)) [ Q(t − r/cₛ)/r² + Q̇(t − r/cₛ)/(cₛ r) ] r̂   (4.76)

Close to the source, the first term dominates; far away the second term dominates.

As an example, consider the sound waves generated by a pulsating sphere of radius a. We’ll take this sphere to beat in and out, with frequency ω and amplitude ϵ, so the radius changes with time as

R(t) = a + ϵ e^(iωt) ⇒ Ṙ = iω ϵ e^(iωt)

The solution must take the form (4.76) for some Q(t) = A e^(iωt). This means that

u(r, t) = (A c²ₛ/(4πρ₀)) [ e^(iω(t − r/cₛ))/r² + iω e^(iω(t − r/cₛ))/(cₛ r) ] r̂

This is subject to the requirement that the fluid velocity matches that of the sphere on its surface, i.e.

u(R(t), t) = Ṙ r̂ ⇒ u(a, t) + ∂u/∂r ϵ e^(iωt) + ... = iω ϵ e^(iωt) r̂

Since u ∼ O(ωϵ), the second term in the above expression is lower order and it will suffice to set

u(a, t) = iω ϵ e^(iωt) r̂ ⇒ (A c²ₛ/(4πρ₀)) [ iω/a + 1/a² ] e^(−iωa/cₛ) = iω ϵ

which fixes the overall coefficient A.

4.4.5 Viscosity and Damping It is natural to ask: how does viscosity affect the propagation of sound? Because viscosity is dissipative, any process will necessarily increase the entropy and so is no longer adiabatic. This means that we can’t just use the simple relation P ρ⁻γ and must instead turn to the more sophisticated description in terms of the temperature field.

We met the heat transport equation in (4.66)

∂T/∂t + u·∇T + (γ − 1) T ∇·u = κ m / (γ ρ k_B) ∇²T

This should be augmented with the Navier-Stokes equation

ρ ∂u/∂t + ρ u·∇u = −∇P + µ∇²u + (µ/3 + ζ) ∇(∇·u)

together with mass conservation and an appropriate equation of state that relates P, ρ and T. We’ll stick with the ideal gas equation of state, so

P = k_B T ρ / m

and we substitute this into the Navier-Stokes equation. For dilute gases, it turns out that ζ ≈ 0 so we choose to set it to zero. (It doesn’t qualitatively change the physics because, as you can see, the shear viscosity µ already appears in the relevant term.)

Our goal is to reproduce our previous results about sound waves in this framework, and then to understand how these results are affected by the viscosity µ and the heat conductivity κ.

As before, we start with a stationary fluid but now also include the fact that it has constant temperature

u = 0 , ρ = ρ₀ , T = T₀

We then consider time-dependent perturbations,

u = û k̂ e^(ik·x − iωt)

ρ = ρ₀ + ρ̂ e^(ik·x − iωt)

T = T₀ + T̂ e^(ik·x − iωt)

Note that we’re looking for longitudinal waves, with û parallel to k. Linearising, the mass conservation equation tells us that

ω ρ̂ = ρ₀ k û

The linearised heat transport equation is

−iω T̂ + i(γ − 1) T₀ k û = − k² κ m / (γ ρ₀ k_B) T̂

where c²ₛ = ρ₀ k_B γ T₀ / ((γ − 1) m). Last, the linearised Navier-Stokes equation is

−iρ₀ ω û = − i k_B k T₀ ρ̂ / m + i k_B k T₀ T̂ / T₀ − µ k² û − (i µ k² / 3) û

We can write these simultaneous equations as a matrix,

M [ρ̂; û; T̂] = ω [ρ̂; û; T̂] with M = [ρ₀ k; k k_B T₀ / m ρ₀ − 4i µ k² / (3 ρ₀ k) k_B k / m; 0 (γ − 1) T₀ k − i κ k² / c²ₛ V]   (4.77)

The frequencies of the perturbations ω are given by the eigenvalues of the matrix M. As we will see, this will give the dispersion relation between ω and k. Note, moreover, that the elements of the matrix are real except for those that multiply the dissipative coefficients µ and κ. We’ll see what this means for the physics shortly.

First let’s look at what happens when µ = κ = 0. There are solutions

[ρ̂; û; T̂] = ϵ [ρ₀; ω/k; (γ − 1) T₀]

with ϵ some small, dimensionless parameter needed for the linearised approximation to be valid. This immediately solves the first two and third equations, while the second requires

m ω² = γ k_B T₀ k² ⇒ ω = ± sqrt(γ k_B T₀ / m) k = ± cₛ k

But this is just our previous result (4.72) for the speed of sound. Moreover, we see that this perturbation has (γ − 1) T₀ ρ̂ − ρ₀ T̂ = 0 which means that T/ρ^(γ−1) is constant. But this is the expected behaviour (4.63) for an adiabatic deformation of the fluid. So, in the limit that the dissipative effects vanish, we do indeed recover the adiabatic sound waves of the previous section.

There is also a novel solution to the equation (4.77) with µ = κ = 0 that we haven’t seen previously. This has û = 0 and

T₀ ρ̂ + ρ₀ T̂ = 0

a combination that ensures that P ∼ ρT is constant in this perturbation. This corresponds to isothermal waves.

rturbation. It solves the matrix equation above only when ω = 0. Because the pressure is constant, there is no restoring force for this perturbation.

Having made contact with our previous result, we can now see how it’s changed when we turn on viscosity µ and heat conductivity κ. Rather than directly finding the eigenvectors, we can take a bit of a shortcut to extract just the eigenvalues ω. First note that the determinant and trace of M are given by detM = i κc2 / (γc c) k4 and TrM = −i κ/(γc) + k2 (4 µ / (3 ρ₀))

The product of the three eigenvalues must be equal to detM. When µ = κ = 0, we know that one of the eigenvalues vanishes and the other two were ±c_s k. But now we see that the three must multiply to give something proportional to κ. This means that, to leading order in κ, the zero eigenvalue that arose from perturbations of constant pressure must change to −c_s^2 k^2 ω = detM ⇒ ω = −i (κ / (γc_s)) k^2 The frequency is imaginary and negative. This is telling us that the modes decay exponentially quickly. To see this, write ω = −iΓ. Then the behaviour of all modes goes as e^{−iωt} = e^{−Γt}. The behaviour that we find above scales as ω ∼ −ik^2. This is characteristic of diffusion. It is the kind of behaviour that we get from the heat equation.

The two remaining modes are what becomes of sound waves. These too are expected to get a dissipative contribution. If we anticipate that they take the form ω = ±c_s k − iΓ̃ possibly with some change to the sound speed, then we can compute Γ̃ by noting that the trace must equal the sum of all three eigenvalues, so −2iΓ̃ − i k^2 (κ/(γc_s)) = TrM ⇒ Γ̃ = (1/2) (κ/(γc) + (4µ γ−1)/(3m ρ₀ γ c_s))

We see that the effect of viscosity and of heat conduction is similar: the sound waves diffuse and decay over time, with their lifetime set by 1/Γ.

In addition, we can ask about velocity perturbations that are transverse to the wave, so that k · u = 0. These are known as shear perturbations. It’s straightforward to see that mass conservation and heat transport require ρ̃= T̃ = 0, while the linearised Navier-Stokes equation gives the dispersion relation ω = −i ν k^2 We see that these modes also behave diffusively.

## 4.5 Non-Linear Sound Waves

So far, throughout this section we’ve only considered linear wave equations. For surface waves we went to some lengths to pick an approximation which made our equations linear and for sound wave we dropped the u·∇u term in the Navier-Stokes equation. This is a good first step since linear equations are significantly easier to solve than non-linear equations. But it’s natural to wonder: under what circumstances are the non-linearities important? And what effect do they have? Here we start to address such questions, albeit in the somewhat restricted context of waves propagating in one dimension.

We’ll revisit our analysis of sound waves, but now restricted to 1d. Our defining equations are the continuity equation ∂ρ/∂t + ∂(ρu)/∂x = 0 (4.78)

and the Euler equation ∂u/∂t + u ∂u/∂x = − (1/ρ) ∂P/∂x (4.79)

Previously we dropped the u∂u/∂x term. Our goal now is to understand what role it plays.

So far we have two equations for three variables: u, P and ρ. As we stressed previously in Section 4.4, we must add one further equation. Rather than getting all hot and bothered by introducing temperature, we will instead work directly with an adiabatic equation of state that relates the pressure to the density, P = P(ρ)

For example, for the ideal gas undergoing adiabatic deformations, we showed that the relevant equation is Pρ^{−γ} = constant with γ = c_P/c_V the ratio of specific heats. (See equation (4.64).) We’ll turn to this example later but for now we keep things general. We also saw that in the previous section that, in the linearised approximation, the speed of sound is given by (4.73), c_s^2(ρ) = (dP/dρ)

(Previously we wrote this as a partial derivative, keeping entropy S fixed. In this section we assume that entropy is fixed and view P only as a function of ρ.) One of the things we would like to learn is the sense in which c_s retains its interpretation as the speed of sound waves beyond the linearised approximation.

4.5.1 The Method of Characteristics From the definition of c_s^2, together with (4.78), we have ∂P/∂t + u ∂P/∂x = c_s^2 (∂ρ/∂t + u ∂ρ/∂x) = −ρ c_s^2 ∂u/∂x (4.80)

To make progress, we’re going to rewrite the Euler equation (4.79) and our equation for pressure (4.80) in a clever way. Starting from (4.79), we have (∂/∂t + (u−c_s) ∂/∂x) u = − (1/ρ) ∂P/∂x − c_s ∂u/∂x = (1/(ρc_s)) (∂/∂t + (u−c_s) ∂/∂x) P (4.81)

where, to get to the second line, we’ve used (4.80). There’s a nice symmetry between the left- and right-hand side of this equation, with the same differential operator appearing in both. The only difference between them is that extra function 1/(ρc_s) sitting on the right-hand side. To make things look even more symmetric, we define the new variable, Q(ρ) = ∫_{ρ₀}^{ρ} c_s(ρ′)/ρ′ dρ′ (4.82)

with ρ₀ some useful fiducial, constant density such as the asymptotic value of the density if such a thing exists. This has the property that ∂Q/∂t = (c_s/ρ) ∂ρ/∂t = (1/(ρc_s)) ∂P/∂t and ∂Q/∂x = (1/(ρc_s)) ∂P/∂x This means that we can write (4.81) as (∂/∂t + (u−c_s) ∂/∂x) (u−Q) = 0 The same argument, with some minus signs flipped, also gives (∂/∂t + (u+c_s) ∂/∂x) (u+Q) = 0

We introduce the Riemann invariants R± = u±Q (4.83)

These obey the Riemann wave equation (∂/∂t + (u±c_s) ∂/∂x) R± = 0 (4.84)

We next want to understand what this equation is telling us. To this end, for a given flow u(x,t) with density ρ(x,t), we construct two collections of characteristic curves, C±. These are worldlines in the spacetime parameterised by (x,t), defined by C±: dx/dt = u(x,t)±c_s(x,t) (4.85)

We introduce two new coordinates in spacetime: ξ+ and ξ−. These have the property that ξ± are constant on the characteristic curves C± respectively. Then the meaning of (4.84) is: Claim: R± is constant on characteristic curves C±.

Proof: To show this, we just need to think carefully about what depends on what. Suppose that we vary both ξ+ and ξ− a tiny bit. Then we move in the t direction an infinitesimal amount dt = (∂t/∂ξ+)|_{ξ−} dξ+ + (∂t/∂ξ−)|_{ξ+} dξ− and we move in the x direction an infinitesimal amount dx = (∂x/∂ξ+)|_{ξ−} dξ+ + (∂x/∂ξ−)|_{ξ+} dξ− On the characteristic curves C+ we know that ξ+ is constant, so we have C+: dξ+ = 0 ⇒ (∂x/∂ξ−)|_{ξ+} / (dt/dξ−)|_{ξ+} = (∂t/∂ξ−)|_{ξ+} = (u+c_s) (∂t/∂ξ−)|_{ξ+} Now, if we view R+(x,t) as a function R+(ξ+,ξ−), then (∂R+/∂ξ−)|_{ξ+} = (∂R+/∂t)|_{ξ+} (∂t/∂ξ−)|_{ξ+} + (∂R+/∂x)|_{ξ+} (∂x/∂ξ−)|_{ξ+} = (∂R+/∂t + (u+c_s) ∂R+/∂x) (∂t/∂ξ−)|_{ξ+} = 0 In other words, R+(ξ+,ξ−) is really just a function of a single variable, R+(ξ+). The same argument also tells us that R− = R−(ξ−). So if we move along a characteristic curve C+, where ξ+ is constant, then R+ doesn’t change. Similarly, R− doesn’t change if we move along a characteristic curve C−. □

It’s worth taking stock of what we’ve achieved. Our goal is to solve for the flow u(x,t) and the density ρ(x,t). We haven’t done this yet! However, we have showed that, if we can solve it, then we can construct characteristic curves C± on which the variables R± are constant. And R±, in turn, depends on u and ρ that we are trying to figure out. All of which means that the Riemann invariants don’t immediately solve our problem, but they should contain some information that we can exploit. Furthermore, if it’s possible to somehow figure out R±(x,t) then it’s straightforward to reconstruct the velocity field which, from (4.83), is given by u(x,t) = (R+(ξ+)+R−(ξ−))

This is the generalisation of the more familiar solution to the linearised wave equation (4.75), u(x,t) = F(x−c_s t)+G(x+c_s t)

which describes wave packets moving left and right at a constant speed c_s.

4.5.2 Soundcones The equations (4.84) are telling us that the something is propagating in the fluid with speed c_s relative to the flow.

To see this more clearly, consider some initial disturbance with u(x,0) ≠ 0 for |x| < L as shown in Figure 25. We’ll also assume that the density ρ(x,t) differs from some asymptotic value ρ₀ only within this same region. From (4.82), this ensures that Q = 0 outside of this region so R±(x,0) = 0 for |x| > L.

We can draw this on a spacetime diagram, with the vertical axis labelled by c₀ t where c₀ = c_s(ρ₀) is the asymptotic sound speed. This ensures that linearised sound waves travel at ±45° in the diagram, rather like light rays in Minkowski space. In analogy with special relativity, we will say that the pair of characteristic curves C± emerging from any point form a soundcone. (In fact, the analogy works better with general relativity where the lightcones depend on the curvature of spacetime, just like the soundcone depends on the flow u and density ρ.)

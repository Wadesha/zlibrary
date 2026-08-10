# Feynman Simplified 1D Angular Momentum Sound Waves Symmetry Vision Robert L Piccioni Z Library

> 来源文件：pre_Feynman_Simplified_1D_Angular_Momentum_Sound_Waves_Symmetry_Vision_Robert_L_Piccioni_Z_Library.txt
> 字符数（约）：249495
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Feynman Simplified 1D: Angular Momentum, Sound, Waves, Symmetry & Vision Everyone’s Guide to the Feynman Lectures on Physics by Robert L. Piccioni, Ph.D.

Copyright © 2014 by Robert L. Piccioni Published by Real Science Publishing 3949 Freshwind Circle Westlake Village, CA 91361, USA Edited by Joan Piccioni Visit our web site www.guidetothecosmos.com Everyone’s Guide to the Feynman Lectures on Physics Feynman Simplified gives mere mortals access to the fabled Feynman Lectures on Physics.

This Book Feynman Simplified: 1D covers about a quarter of Volume 1, the freshman course, of The Feynman Lectures on Physics. The topics we explore include: Angular Momentum Moments of Inertia Rotations in Three-Dimensions Sound & Beat Frequencies Modes & Harmonics Fourier Series & Transforms Complex Waves Symmetry Properties of Natural Laws To find out about other eBooks in the Feynman Simplified series, and to receive corrections and updates, click HERE.

I welcome your comments and suggestions. Please contact me through my WEBSITE.

If you enjoy this eBook please do me the great favor of rating it on Amazon.com or BN.com.

Table of Contents

## Chapter 39: Rotation & Angular Momentum

## Chapter 40: Centers & Moments of Rotation

## Chapter 41: 3D Rotation & Review of Rotation

## Chapter 42: Physics of Waves & Sound

## Chapter 43: Theory of Beats

## Chapter 44: Modes of Oscillation

## Chapter 45: Harmonics & Fourier Analysis

## Chapter 46: Complex Waves

## Chapter 47: Review of Physics of Waves

## Chapter 48: Physics of Vision

## Chapter 49: Symmetry & Physical Laws

## Chapter

Rotation & Angular Momentum We have so far explored Newton’s laws as they apply to point particles, and objects that we can assume are equivalent to point particles. An example of the latter is the gravitational attraction of the Earth and Sun, which Newton proved can be calculated assuming all of each body’s mass is concentrated at its center.

We can now move up to more complex objects and motions.

As Feynman says in V1p18-1: “When the world becomes more complicated, it also becomes more interesting… the phenomena associated with the mechanics of a more complex object…are really quite striking.” We will start with the simplest cases, preparing ourselves for the “really quite striking” ones to come later. In this chapter, we will examine rotations of rigid bodies in two-dimensions moving at non-relativistic velocities, so that we can employ Newtonian mechanics.

Parabolic path of center of mass From our prior studies, we know how to calculate the motion of a football thrown by a quarterback to a receiver. Assume the QB releases the ball at time t = 0, at location x=y=z=0, with velocity v=(vx,0,vz), where +z is straight up and +x is downfield. Ignoring air resistance, if the ball were a single point, its trajectory would be: x(t) = vx t y(t) = 0 z(t) = vz t – 1/2 g t² This arcing curve is called a parabola, as illustrated in Figure 39-1.

Figure 39-1 Parabolic Path Of Thrown Ball The motion is much more complicated if a more complex object is thrown, such as a gaucho’s bolo, three balls tied to a string. But even then, there is something that still moves in a parabolic arc — some central essence moves in a perfect parabola, while all else flails around it. That central essence is called the center of mass, a kind of average of the locations of all the particles within the complex object. The center of mass, often-abbreviated CM, is a mathematically determined point that doesn’t even have to be a material part of the object. For three balls attached to a loop of rope, the center of mass is a point in-between the balls where nothing exists.

Let’s examine F, the sum of all forces on all particles within a complex object. Label the particles j = 1 to some enormous number N. The jth particle experiences a force Fj equal to its mass mj times its acceleration, which equals the second derivative of its position rj. Recall the linearity of differentiation: d(A+B)/dt = dA/dt + dB/dt.

F = Σ Fj = Σ {d²(mjrj) / dt²} F = d²( Σ {mjrj} ) / dt² Define: M = Σ {mj} R = Σ {mjrj} / M Rewriting the prior equations with these definitions yields: F = M d²(R) / dt² We have recovered the equation for the motion of a single point body of mass M and position R. As defined above, M equals the mass of the complex object and R is the position of its center of mass. Everything we learned before about the motion of a single point body applies directly to the motion of the CM of a complex body.

In V1p18-2, Feynman suggests mentally separating the forces on each particle into two groups: internal and external. Newton’s third law (action begets reaction) ensures that the forces between particle j and particle k in the body are equal and opposite; hence they cancel one another in the sum F. Indeed all internal forces sum to zero in the calculation of F. This means the motion of the center of mass is determined only by the external forces.

only by external forces, such as Earth’s gravity. Imagine a rocket ship in outer space. If it is sufficiently isolated, we could assume it experiences no external forces and is stationary in an appropriate reference frame. More precisely, its center of mass is stationary. If the crew moves toward the front of the ship, the ship itself must move backward to keep the center of mass stationary. Indeed, this must happen on the International Space Station, although since the ISS is enormously more massive than its crew, this effect is imperceptible. Newton’s third law prevents a rocket ship from moving its own center of mass, but it can propel part of its mass (the ship) by expelling another part (the fuel). In whatever manner its rockets fire, the CM of all the ship’s original mass remains stationary in an appropriate reference frame. In any other reference frame, the ship’s CM moves at a constant velocity, regardless of how or whether its rockets fire.

Since we know how to analyze the motion of the center of mass of a complex body, let’s now examine the motion of the rest of the body. We’ll make things simpler by considering only rigid bodies, those whose atoms are so strongly bound to one another that their relative orientations do not change. We thus avoid dealing with bending, twisting, and vibrating. Having agreed on all these constraints, the only motion left is for the body to rotate as one single object. What does “rotating” mean? A three-dimensional object rotates around an axis, whereas a two-dimensional object rotates about a single point. Figure 39-2 illustrates rotation in two-dimensions. On the left side, the darker rectangle is rotated about the XY origin by a small angle, resulting in the lighter rectangle. The right side of this figure focuses on the rectangle’s upper right corner, labeled P. Initially, the radial line from the XY origin to P lies at angle ø relative to the x-axis. Rotation increases that angle by dø, moving the rectangle’s upper right corner P to position Q.

In the figure, the line u is perpendicular to r, hence the angle between u and the vertical dotted line is also ø. Let the coordinates of P be (x,y) and of Q be (x+dx,y+dy). From trigonometry, we find these relationships: x = r cosø, y = r sinø, u = r tan(dø), u = dx = –r sinø dø, u = dy = +r cosø dø. If we measure angles in radians, and take the limit of dø going to zero, we have: u = r dø, u = –y dø, u = +x dø. If dø occurs during an infinitesimal time interval dt, and we define ω = dø/dt, the equations become: v = dx/dt = –y ω, v = dydt = +x ω, v2 = v2+v2 = ω2 (y2+x2), v = ω r. The last equation jibes with P moving to Q, a distance u = r dø, in time dt, making v = r dø/dt = r ω.

A quick note about measuring angles in radians. As mentioned earlier, in equations and calculations we always measure angles in radians rather than degrees. Radians are convenient: the arc length subtended by angle θ equals rθ, for radius r. For example, for θ = π/2, arc length = π r/2, both corresponding to 1/4 of a full circle. In the text, we sometimes use the more colloquial 90 degrees, rather than π/2, but in equations it’s always radians. To clarify the rotational parameters, Feynman stresses the analogy with linear motion. In linear motion we have position r, velocity v = dr/dt, acceleration a = d2r/dt2, and force F = ma. In rotational motion we have angular position ø, angular velocity ω = dø/dt, angular acceleration α = d2ø/dt2, and perhaps an unknown X. Isn’t there some angular X analogous to force?

Ask and ye shall receive: X is torque, from the Latin word torquere, to twist. We’ll follow Feynman’s lead and find quantitative expressions for torque by considering the work energy expended in rotating an object. Recall that for linear motion, work equals force times the distance through which the force acts. By analogy, work will equal torque times the angle through which the torque acts. Going back to our rectangle in Figure 39-2, pushing on the rectangle at point P and turning it by angle dø requires work W, according to: W = F • ds = (F dx + F dy). Using the expressions derived above for dx and dy, we derive the equation for torque τ in 2D: W = (–y dø F + x dø F), W = τ dø, τ = + x F – y F. You might recognize the combination xy – yx; it’s the vector cross product. So, we can rewrite this equation in vector form, which we’ll discover later is also valid in 3D, as: τ = r × F. If multiple torques act on a body, they simply add like vectors, as do forces in linear motion. Since an object can have only one rotation angle dø (in 2D), the above equations generalized for multiple torques, labeled j = 1 through N, are: τ = Σ {x F – y F }, W = τ dø. Unlike a force, a torque is defined relative to the center of rotation in 2D, or the axis of rotation in 3D. The math shows this because r, x, and y are all measured from the center of rotation to the point at whic where the torque acts. One can calculate a torque about any point (or axis in 3D), but the values relative to different points will likely be quite different.

If, and only if, the sum of all torques is zero, the body will be in rotational equilibrium — its rotational velocity ω = dθ/dt will be constant. This is analogous to a body moving at a constant velocity if and only if the sum of all forces is zero. Complete dynamic equilibrium requires both the sum of all forces and the sum of all torques to be zero to ensure the body does not accelerate linearly or rotationally.

Let’s take another look at the torque equation. Figure 39-3 shows force F acting at point P on a rigid body.

Figure 39-3 Torque From Force F at Position r

For convenience, choose coordinates which place the center of rotation at x=y=0, P on the x-axis, and define r to be the radial vector from the center of rotation to P. The light dotted arc shows the rotational path of P. The angle between F and r is θ. If we extend the line of F infinitely far in both directions (the dashed line), b is the distance of closest approach of that line to the center, and the radial line b is perpendicular to the dashed extension of F.

If the body rotates slightly by an angle dθ (counterclockwise for dθ > 0), point P will move upward (+y-direction) a distance r dθ, and the work done will be F r dθ. Since work = F • ds, the x-component of F does not contribute because it is perpendicular to the motion. The torque equation for our current situation (x = r and y = 0) is: τ = + x F – 0, so τ = + r F = r F sinθ. The work done is W = r F dθ = τ dθ.

Since only the component of force perpendicular to the radial vector contributes to torque, torque equals F r sinθ, which as you may recall from Chapter 6 is the definition of the cross product; hence, this confirms τ = r × F.

Now, let’s get back to b, the distance of closest approach of F to the center of rotation in Figure 39-3. This parameter is also called the lever arm of the force, or its impact parameter. Note that b is one side of a right triangle of which r is the hypotenuse. The interior angle of that triangle at P equals θ, so: τ = F r sinθ and b = r sinθ. Therefore, τ = F b.

The above give us several ways to calculate torque, the last being force multiplied by its lever arm. By now you might be wondering whether all this center-of-mass and torque stuff is actually useful or is merely esoteric physics. If so, you’ll be surprised how enjoyable (and profitable) all this stuff can be. When Feynman taught me how to play pool, lesson #1 was where to hold the cue stick. If you grab it just anywhere, the stick is apt to turn unexpectedly when you shoot. This is because your stroke may apply a torque, rotating the stick and ruining your hopes for victory. To avoid torquing the cue stick, hold it at its center of mass — there’s no torque when a force is applied with zero lever arm.

How can you conveniently find the CM of a tapered rod? Put your two index fingers a couple feet apart and point them straight ahead and level. Now balance the stick across your fingers, and slowly move your fingers together, while keeping the cue stick balanced. Where they meet is the CM. Why? Because, at any instant, the finger closer to the CM will bear most of the stick’s weight, causing greater friction on that finger than on the one farther from the CM. Hence, the farther finger will slide while the other is stuck by friction. As you move your fingers together, the stick will slide over one finger and then the other, alternating as the farther finger moves closer. When you master this, you’ll be ready for Feynman’s pool lesson #2: spin.

Angular Momentum

We are ready to move beyond rigid bodies. We’ll now consider any collection of particles, even those that do not form a material body. Examples include: seed heads of dandelions; marbles tossed in the air; a chain; stars in a galaxy; or electrons in a particle beam. We will also no longer require that each particle turn in perfectly circular rotation. With this generalization our results will be applicable to elliptically orbiting planets, and particles following other irregular paths.

At the beginning of this chapter, we discussed how to calculate the center of mass of an array of particles, and how to calculate its motion due to external forces. Here we will consider the twists and turns due to the torques associated with all the forces acting on the particles.

Begin with just one such particle. As before, in 2D: τ = x F_y – y F_x. Substituting the components of force from Newton’s second law (F_x = m d²x/dt², F_y = m d²y/dt²) gives τ = xm d²y/dt² – ym d²x/dt². This can be rewritten as the time derivative of a quantity: τ = d {xm dy/dt – ym dx/dt } /dt.

Wow, how did I know how to do the last step? Some of you might be brilliant enough to figure that out by yourselves, but I read it in V1p18-5. We can show this is true by working backwards: τ = d {xm dy/dt – ym dx/dt } /dt = (dx/dt)(m dy/dt) + xm d²y/dt² – (dy/dt)(m dx/dt) – ym d²x/dt². Simplifying cancels the first and third terms, leaving τ = xm d²y/dt² – ym d²x/dt², which matches our earlier expression.

So, torque is the rate of change of {xm dy/dt – ym dx/dt }, just as force is the rate of change of momentum. We therefore call {…} the 角动量 L。在二维情况下： L = {x d(my)/dt – y d(mx)/dt } L = x p – y p y x τ = dL/dt 本章中我们所做的一切都基于牛顿定律，但最后三个方程在相对论情况下同样正确。

正如我们有多种扭矩表达式，也可以写出等效的角动量表达式。设 b 为 p 的力臂，μ 为 r 与 p 之间的夹角，则有： L = x p – y p y x L = r × p L = r p sinµ L = p b

基于对角动量的理解，让我们重新审视开普勒第二定律。对于一颗绕恒星运动的行星，维持其轨道运动的力是一个源自恒星中心的径向矢量。因此该力的力臂为零，即行星不受扭矩作用，其角动量不会改变（0 = τ = dL/dt）。利用上述方程并参照图 39-4，我们在所有变化均为无穷小的极限条件下得出： L = r mv sinµ r dθ = v sinµ 扫过的面积 = 1/2 r (r dθ)

面积 = 1/2 r (v sinµ)

面积 = 1/2 L/m d(area)/dt = dL/dt /(2m) = 0 图 39-4 行星扫过面积

在计算扫过的面积时，我们使用的是大三角形的面积而非小三角形的面积，因为小三角形的两边与无穷小量成比例，在极限情况下可以忽略。我们的结论是：行星在相等时间内扫过相等的面积，这与开普勒的描述一致。他的第二定律是在无扭矩作用下角动量守恒的直接结果。

角动量守恒回顾本章开头，我们对一个大物体内部所有粒子的力和加速度进行了求和。我们发现所有内力相互抵消，只剩下加速物体质心的外力。这种简洁性源于牛顿定律的线性以及作用力与反作用力定律。

现在我们将对旋转运动执行相同的过程：对物体中每个粒子的扭矩和角动量进行求和。

设 L_j 和 τ_j 为第 j 个粒子的角动量及其所受扭矩。设 L 和 τ 为物体的总角动量及所受总扭矩。则： L = Σ L_j τ = Σ τ_j τ = Σ dL_j/dt τ = dL/dt

同样，所有内扭矩（由内力引起的扭矩）因作用力与反作用力大小相等、方向完全相反而相互抵消。因此 τ 中仅剩外力产生的扭矩。所以，物体总角动量的变化率等于作用于其上的总外扭矩。方程为： dL/dt = τ_external

该方程无论大复合物体内部发生什么，无论该物体是否刚体，也无论绕何轴运动，都成立。一个非常重要的特例是：当所有外扭矩之和为零时，物体的总角动量保持不变。因此，任何封闭系统的总角动量都是守恒的。

转动惯量 V1p18-7 接下来我们将考虑角动量的变化如何影响物体的旋转速度。再次设想一个刚体，其所有粒子在二维中绕同一点以相同速率旋转。该物体中的所有粒子将绕旋转中心做圆周运动，且都以相同的角速度 ω = dø/dt 旋转。设第 j 个粒子的径向距离为 r_j，线速度为 v_j（v_j = r_j ω），其角动量为 L_j。注意，对于圆周运动，对所有 j，v_j 总是垂直于 r_j。

L_j = m_j v_j r_j = m_j r_j^2 ω L = Σ L_j = ω Σ m_j r_j^2 L = I ω

此处我们定义物体的转动惯量 I = Σ m_j r_j^2。正如质量 m 乘以线速度 v 等于线动量 p，转动惯量 I 乘以角速度 ω 等于角动量 L。质量与转动惯量的关键区别在于后者与物体尺寸的平方成正比。对于直线运动，我们得知可以假设物体的所有质量集中于单个点来进行分析。显然，对于旋转运动而言，这一点并不成立。

这种效应最戏剧性的展示或许是花样滑冰锦标赛中精彩的“旋转”动作。滑冰者伸展四肢在小圆圈中旋转，如图 39-5 左侧所示。当他们随后将手臂和腿收拢成紧凑姿势时，如图右侧所示，其转动惯量减小，为保持角动量守恒，其旋转速度增加。

图 39-5 花样滑冰者的“旋转”

有些滑冰者可以将角速度从每秒 2.5 转提高到每秒 6.0 转。这快了 2.4 倍。由于 L = Iω 必须恒定，他们之前的 I_B ω_B 和之后的 I_A ω_A 必须相等：I_B ω_B = I_A ω_A。这意味着滑冰者必须将转动惯量减少 2.4 倍，这需要将平均 r 减小到其原始宽度的 64%。这似乎是一个相当 a feat, given that their heads and torsos don’t shrink. Each arm weighs about 6% of a person’s total weight, while each leg is about 20% — you do the math.

Rotational Kinetic Energy The one key quantity of rotational mechanics that we have yet to examine is rotational kinetic energy. We discussed the angular momentum L of a rotating object, the work done by torque W = τ dφ, and how torques change angular momentum τ = dL/dt. Just as linear motion results in kinetic energy, so does rotational motion.

What is the kinetic energy of an object rotating with angular velocity ω? Since the rotational analog of mass m is moment of inertia I, and the analog of linear velocity v is angular velocity ω, it’s no surprise that the analog of ½ m v² is ½ I ω². Let’s show this is indeed true.

Consider a collection of particles that are all rotating with angular velocity ω. Let the mass of the jth particle be m_j and its distance to the rotational axis be r_j. Each particle’s linear velocity v_j equals ω r_j. Hence the total kinetic energy of all particles, according to the laws of Newtonian mechanics for linear motion, is: T = Σ {½ m_j (ω r_j)²} T = ½ ω² Σ {m_j r_j²} T = ½ ω² I

Note that we must not double-count energy. The kinetic energy of the jth particle is m_j(ω r_j)²/2; we need to account for that once, either as linear kinetic energy or as rotational kinetic energy, but not as both. One could legitimately ignore rotational kinetic energy and do the sum of m_j(ω r_j)²/2, but it’s generally much easier to use the rotational kinetic energy equation Iω²/2 and get the result in one calculation. Take your pick, but do not include both in any conservation of energy analysis.

Feynman raises an interesting question about spinning figure skaters. When skaters pull their arms and legs inward to spin faster, their angular momenta remain constant since no torques are present. Hence L_B = L_A, where the labels B and A refer to before and after. What about their rotational kinetic energies?

L_B = L_A I_B ω_B = I_A ω_A ω_A = ω_B I_B / I_A T_A = ½ I_A (ω_B I_B / I_A)² T_A = ½ ω_B² I_B² / I_A T_A = T_B (I_B / I_A)

To spin faster, skaters reduce their moments of inertia, I_A < I_B. This means kinetic energy increases as skaters pull in their arms and legs. Skaters must supply the added energy, exerting considerable force pulling mass inward against its natural tendency to fly outward.

## Chapter 39 Review: Key Ideas

1. For linear motion, the internal forces among a collection of particles cancel one another, leaving only external forces to act on the center of mass of the particles, as if it were a single object.

2. For rotational motion, we define angular position φ, angular velocity ω = dφ/dt, angular acceleration α = d²φ/dt², torque τ = r × F, the lever arm of force b, the angle μ between r and F or between r and p, angular momentum L, and moment of inertia I = L/ω. These relationships exist: Work W = τ φ τ = F r sinμ = r × F τ = F b τ = dL/dt L = r × p L = r p sinμ L = p b I = Σ m_j r_j² Kinetic energy T = ½ I ω²

Compared below are the linear and rotational variables of prime interest.

## Chapter

Centers & Moments of Rotation

This chapter examines the centers of mass and moments of inertia of large bodies.

Properties of Center of Mass In the prior chapter, we considered a large collection of particles with many forces acting on them. The particles could be molecules of a gas, atoms within a rigid body, or stars within a galaxy. We found that the internal forces amongst these particles summed to zero due to Newton’s third law of action and reaction. That left us to deal only with any external forces acting on these particles. We found it useful to define a center of mass (CM) of any group of particles as follows: R = Σ {m_j r_j} / M Here R is the position vector of the CM, m_j and r_j are the mass and position vector of the jth particle, M = Σ {m_j} is the total mass of all particles, and the sum extends over j = 1…N, with N being the number of particles in the group. As with any vector equation in 3D, the above is shorthand for three equations, one in each of any three mutually orthogonal spatial directions.

Imagine initially that every particle has the same mass m. The equation for the center of mass is then: R = m Σ {r_j} / (N m) = Σ {r_j} / N This means R is just the average position of all its parts, which is a perfectly reasonable definition of “center.”

Now, let’s imagine we have n particles of type A that have mass m, and n particles of type B that have mass 2m. Our equation then becomes: R = [ Σ {m r_{jA}} + Σ {2m r_{jB}} ] / (n m + 2 n m)

R = [ Σ {r_{jA}} + 2 Σ {r_{jB}} ] / (3 n)

Above, we sum over all n A-particles in the first term and all n B-particles in the second term. While there are equal numbers of A- and B-particles, the B-particles have twice as much effect due to their greater mass. This also seems reasonable, particularly since we can imagine each B-particle being...

two particles of mass m glued together, thereby making R the average position of 3n particles, 2/3rds of which happen to be paired.

Let’s now put some bounds on R. Consider for a moment only the x-direction and let Xmin be the minimum value of the x components of all N particles. Now compute:

R_x = Σ {m_j x_j} / M

R_x = Σ {m_j (x_j – Xmin + Xmin)} / M

R_x = Xmin + Σ {m_j (x_j – Xmin)} / M

To get the last equation, we pulled the constant Xmin out of the summation; its coefficient was Σ {m_j}/M = 1. Now, we know (x_j – Xmin) ≥ 0 for every j because Xmin is the minimum of all x_j. Hence R_x ≥ Xmin. We can similarly show that R_x ≤ Xmax, the maximum of all x_j. This means the x component of the center of mass must be in the range Xmin to Xmax; similarly for the y and z components. Therefore the center of mass of any collection of particles must lie within an envelope completely surrounding all particles, which is entirely reasonable.

This doesn’t mean the center of mass is necessarily coincident with any of its particles. A donut, for example, has its center of mass in the hole in its middle.

Next consider joining two objects A and B that have masses M_A and M_B and centers of mass R_A and R_B. What can we say about the center of mass of the combined object, whose mass is M = M_A + M_B?

R = Σ {m_j r_j} / M

R = (Σ {m_{jA} r_j} + Σ {m_{jB} r_j}) / M

R = (M_A R_A + M_B R_B)/ M

R = R_A (M_A–M)/M + M_B R_B / M

R = R_A + (R_B – R_A) (M_B/M)

This means the CM of the combined object must lie somewhere along the line connecting the CMs of its two constituent parts. Clearly this can be extended to any number of combined objects.

If the collection of particles is symmetric, its center of mass will be located along the line of symmetry. For example, the isosceles triangle shown on the left side of Figure 40-1 is symmetric about its vertical median, so its CM must lie along that line. This is because each point on the left side of the line of symmetry has a corresponding point on the right side. (Recall that a triangle’s three median lines run from each corner to the midpoint of the opposite side.)

Figure 40-1 Isosceles and Oblique Triangles

Now examine the oblique triangle on the right side of Figure 40-1. It has no symmetries, but if its mass is uniformly distributed, we know immediately that its center of mass is where its three medians intersect. Why? Imagine dividing this triangle into a series of narrow strips parallel to the bottom side. The center of each strip is on the median line from the upper corner, because by definition half the points are to the left and half to the right of the median. Therefore, the CM of every strip lies along that median. As demonstrated above, the CM of all strips combined must lie along the line connecting their CMs, which is the vertical median. Similarly, the center of mass must lie along each of the other two medians. All this means is that the CM is at the intersection of the three medians.

Mathematical Methods

This section explores more complex mathematical techniques for finding centers of mass, and provides another opportunity to sharpen one’s math skills.

For a symmetric object, such as the isosceles triangle in Figure 40-1, we said symmetry ensures the center of mass is along its symmetry axis. Let’s now show that mathematically.

Let x be the horizontal axis and let the line of symmetry be at x = 0. By “symmetric about x = 0”, we mean whatever exists at +x must also exist at –x. So in the sum Σ {m_j x_j}, for every j there must be a corresponding k such that m_j x_j = –m_k x_k. The summation must therefore equal 0, and the x component of the CM is at the symmetry axis x = 0.

Consider a body with multiple symmetries, such as a rectangle, which has both horizontal and vertical symmetry. Its center of mass must lie along both its horizontal and vertical symmetry axes. This means its center of mass must be at its midpoint.

A useful tool for finding centers of mass is a theorem by Pappus of Alexandria, one of the last great ancient Greek geometers. The following statement of Pappus’ centroid theorem is somewhat clearer and more precise than that of V1p19-4.

Pappus’ Centroid Theorem: any planar surface rotated about an external axis, sweeps through a volume V such that V = A d, where A is the area of the surface and d is the distance that its centroid moves.

The centroid is the average position of all points within the surface, which for a uniform mass density is also the center of mass. Define XY coordinates with x=y=0 at the centroid, with the y-axis parallel to the axis of rotation, and D being the distance from the centroid to the axis of rotation, as shown in Figure 40-2.

Figure 40-2 Pappus Centroid Theorem

For a rotation angle dθ, the distance moved by a point at position (x,y) equals (D–x) dθ. We can calculate the volume V swept by the area by summing the distance moved by each point within the surface. One could write that as a sum Σ of small areas, each dx × dy, or equivalently one could write an integral equation for V: V = ∫ (D–x) dθ dx dy V = dθ ∫ D dx dy – dθ ∫ x dx dy V = dθ D A

Above, we recognize that ∫dxdy equals the area A, and ∫(x)dxdy = A times the centroid’s x coordinate, which in our coordinate system is identically zero. Thus, the volume swept equals the area of the surface times dθ D, the distance moved by the centroid, proving Pappus’ theorem. This theorem applies to any sequence of rotations about any sequence of axes, as long as the axes are all external to the surface.

Now let’s use this theorem to find a center of mass. In Figure 40-3, a right triangle of height H and base length D is rotated 2π radians around its vertical side, sweeping out the volume of a cone, while its CM, a distance x from the axis of rotation, rotates around the smaller circle.

Figure 40-3 Cone Swept by Rotating Triangle

The volume of this cone equals πHD²/3, the distance the centroid travels equals 2πx, and the area of the triangle equals DH/2. Thus Pappus’ theorem states: (d) (A) = V (2πx) (DH/2) = πHD²/3 x = D/3

If we instead rotate the triangle about its horizontal side, we similarly find the y coordinate of the centroid: y = H/3.

Another example: consider a semicircular disk, half a pizza. The area of the half pizza equals (π r²/2). Rotating the half pizza 2π radians about its straight edge, we get a ball of volume 4πr³/3. Let x again be the distance from CM to rotation axis. The CM moves a distance 2πx through the rotation. The equation for x is: (2πx) (π r²/2) = 4πr³/3 x = 4r / 3π

Now let’s ask: what is the centroid of the crust of that half pizza? Let the crust’s width be w, making its area πwr. Rotating it as before sweeps a shell of volume 4πwr², yielding: (2πx) (πwr) = 4πwr² x = 2r / π

Insights on Scaling

In V1p19-2, Feynman raises a subtle point. We have found that the motion of the center of mass of a collection of particles follows the same Newtonian laws that apply to the individual particles. This means Newton’s laws have the property that they scale: they apply equally well to pebbles, boulders, planets, stars, and galaxies. Remarkably, no new principles of mechanics emerge as we scale up from pebbles to galaxies. The universe didn’t have to be that way, but it is because, as Feynman says, “… the fundamental gears and wheels of the universe are of atomic dimensions.” Those fundamental “gears and wheels” actually follow the rules of quantum mechanics, which are far more complex than the rules of Newtonian mechanics. Newton’s laws are what emerge when the behaviors of trillions of particles are averaged — Newton’s laws are the asymptotic limit of the quantum behaviors of a vast number of subatomic particles. Scaling up from atoms to pebbles already brings us extremely close to the asymptotic limit; scaling up from pebbles to galaxies makes no perceptible change in basic mechanics. At least, that is our current understanding.

Moment of Inertia V1p19-5

We next turn to moment of inertia, the rotational analog of mass. Recall that the moment of inertia, I, depends on two things: what is rotating and how far “what” is from the axis of rotation. The moment of inertia of a collection of particles is the sum over all particles (j=1…N) of each particle’s mass m times the square of its distance to the rotational axis r: I = Σ m r² If the rotation is about the z-axis, and the object has a uniform mass density µ, we can write this equation as an integral over the object’s volume: I = µ ∫ (x² + y²) dx dy dz M = µ ∫ dx dy dz

Our first example is rotating a long bar around its end. Assume a bar of mass M and length L lies along the x-direction, from x=0 to x=L. (I’m using L here for length, not for angular momentum. Sorry, but that’s what physicists do: you’ll see this everywhere. With practice, you’ll immediately know which meaning is intended.) Let’s rotate the bar about the y-axis at x=0. This is a bit like a single-bladed propeller. Let µ be the bar’s mass density per unit length (µ=M/L). The moment of inertia equals the integral of µx² from x=0 to x=L.

I = µ ∫ x² dx = µ x³/3; from x=0 to x=L I = µ (L³/3 – 0)

I = M L²/3

Now let’s rotate the bar about its midpoint, still around an axis perpendicular to its length. We use the same integral, but this time the limits are x = –L/2 to x = +L/2.

I = µ {(+L/2)³/3 – (–L/2)³/3)

I = µ {L³/24 +L³/24} I = M L²/12

Equivalently, we could have computed the integral: I = µ ∫ (x–L/2)² dx; from x=0 to x=L which gives the same result. Try it.

Feynman points out yet another approach. Since the summation Σ m r² is linear, the moment of inertia of two objects around a common axis of rotation equals the sum of the objects’ individual moments of inertia. This is written mathematically as: I = Σ m r² AB jAB j j I = Σ m r² + Σ m r² AB jA j j jB j j I = I + I

## AB A B

This linearity property applies to both addition and subtraction: the moment of inertia of a ring equals the moment of inertia of a disk minus the moment of inertia of the disk’s inner hole (if any).

of the missing center. This is true only if all parts rotate about the same axis.

Now apply the linearity property to the bar of length L rotating about its midpoint: think of the bar consisting of two half-bars, each of mass M/2 and length L/2, which are joined end-to-end and are rotating about their joint. From an earlier result, the moment of inertia of two half-bars rotating about their ends is: I = 2{ (M/2) (L/2)²/3 } I = M L²/12

Whenever I can think of two different ways of calculating something, I do both, because even I make mistakes. If you’re perfect, you needn’t waste time double-checking.

Next, we discuss the parallel-axis theorem. It is extremely useful to separate the moment of inertia I of a large body about the Z axis into two parts: (1) the moment of inertia of its center of mass around the Z axis, plus (2) the moment of inertia of all the body’s parts around its center of mass. Let’s see how this is done, starting again with the fundamental equation for the moment of inertia of a collection of particles about the Z axis (x=y=0). Let M be the body’s total mass and X_CM and Y_CM be the coordinates of its center of mass.

I = Σ m_j r_j² I = Σ m_j {x_j² + y_j²}

Examine the x part.

x_j² = [(x_j–X_CM) + X_CM]² x_j² = (x_j–X_CM)² + 2(x_j–X_CM)X_CM + X_CM²

The last two terms are easy to sum: Σ m_j X_CM² = M X_CM² 2X_CM Σ m_j {(x_j–X_CM)} = 0

Putting those into the x sum yields: Σ m_j x_j² = M X_CM² + Σ m_j {(x_j–X_CM)²}

Similarly for y. So, the moment of inertia becomes: I = M(X_CM²+Y_CM²) + Σ m_j {(x_j–X_CM)²+(y_j–Y_CM)²} I = M R_CM² + I_CM

The first term is the body’s moment of inertia of its center of mass about axis Z, and I_CM is the body’s moment of inertia around its center of mass.

The benefit of the parallel-axis theorem is that once we calculate moments of inertia for a body of some shape around its CM, we need just one more term to obtain the moment of inertia of that body around any axis. We don’t need to start over every time summing mr² for each particle. An essential requirement for using this theorem is that the axis of rotation about the center of mass and the axis about which the center of mass rotates must be parallel. Axes matter: the moment of inertia of the bar we discussed above is much greater around the z-axis, which we computed, than it is around the x-axis along the bar’s length.

Another useful theorem applies to any very thin flat object rotated about an axis perpendicular to its surface. Let x and y be the axes within the surface and z be the perpendicular axis, and let I_x, I_y and I_z be the moments of inertia about each axis. The theorem is: I_z = I_x + I_y. This is because the z coordinates of all the body’s particles are zero, or at least much smaller than the x and y coordinates. Here’s why: I_x + I_y = Σ m_j {(x_j²+z_j²) + (y_j²+z_j²)} I_x + I_y = Σ m_j {(x_j²) + (y_j²)} I_x + I_y = I_z

A table of moments of inertia for some common shapes is at the end of this chapter.

## Chapter 40 Review: Key Ideas

## 1. A body’s center of mass must lie within an envelope containing all its parts

2. The CM of a two-part object lies along the line connecting the CM of each individual part.

## 3. The center of mass of a symmetric body lies along its line of symmetry

4. Pappus’ centroid theorem is: the volume swept by a surface rotating about an external axis equals its area times the distance that its centroid moves.

5. The moment of inertia of a multi-part object equals the sum of the moments of each part, provided all rotate about the same axis.

6. The parallel-axis theorem is: I = M R_CM² + I_CM. A body’s moment of inertia I about an axis Z, equals the moment of inertia of the body about its own center of mass, I_CM, plus M R_CM², its mass times the square of the distance of its center of mass to Z, the axis of rotation.

Some Common Moments of Inertia

## Chapter

Rotations: 3D & Review

In this chapter, we will examine rotations in three-dimensions, using Newtonian mechanics and vector algebra. In V1p20-1, Feynman says that the behavior of the rotating wheel is “…one of the most remarkable and amusing consequences of mechanics.” He saved that amusement for later in the lecture.

While looking forward with anticipation, we must first prepare by extending our 2D knowledge of rotational motion to three-dimensions. That is best done using vectors. What we learned about 2D rotations remains valid, but must be expanded.

Recall our 2D equations for angular momentum L and torque τ: L_y = x p_z – z p_x  (Note: Original text likely contains a typo; the standard 2D form is often given for a specific plane. Assuming the provided text is: L = x p_y – y p_x for the xy-plane, and similarly for other planes as described.)

τ_y = dL_y/dt τ_y = x F_z – z F_x

These equations describe activity in the xy-plane. If we correctly guess the signs using the right-hand rule, we can easily write similar equations for activity in the zx-plane and the yz-plane. In V1p20-1, Feynman asks us to ponder if we need to continue writing new equations for countless other planes beyond these three. Fortunately, that is unnecessary. We already know that three orthogonal axes are sufficient to describe all possible linear motions in 3D. After all, what "3D" means is that there are three independent dimensions of space, no more, no less. Rotational motion is no different in this regard: three orthogonal planes are necessary and sufficient to describe all possible rotational motion in 3D. In fact, three orthogonal planes are really the same thing as three orthogonal axes. The xy-plane is defined as that surface which is everywhere perpendicular to the z-axis — a vector in the +z direction, such as (0,0,1), defines the xy-plane. Similarly, the vector (0,1,0) defines the zx-plane, while (1,0,0) defines the yz-plane.

The angular momentum L = x p – y p is in fact a vector in the z-direction; +z if L>0, and –z if L<0.

The torque τ = x F – y F is similarly also a vector in the z-direction. The proper 3D equations are: L = +x p –y p L = +y p –z p L = +z p –x p τ = +x F –y F τ = +y F –z F τ = +z F –x F In each equation above, the two terms on the right side are the same except: (1) the coordinate labels are exchanged, and (2) the second has a minus sign. The rule for signs is based on the order of three coordinates x, y, and z. Namely, for L = +x p –y p, the plus term on the right has the coordinate combination zxy: the z component of L, the x component of position vector r, and the y component of p, while the minus term has combination zyx.

The rule for signs is: even combinations xyz, yzx, and zxy have a plus sign, while odd combinations xzy, yxz, and zyx have a minus sign. The meaning of even and odd is: the normal alphabetic sequence is xyz; combinations of those letters achieved using an even number of swaps of two consecutive letters are called even, while the others are called odd. For example, xyz becomes xzy with swap #1 (yz to zy), and becomes zxy after swap #2 (xz to zx), hence zxy is an even combination with a plus sign and xzy is an odd combination with a minus sign. This is consistent with the right-hand rule for orienting coordinate axes and for evaluating cross products. Physicists on another planet might well use the left-hand rule; their physics would work just fine, but with reversed signs. (I wonder what would happen on a planet with three-handed physicists.)

We can write the above equations more conveniently using vector notation: τ = r × F τ = dL/dt L = r × p Since torque and angular momentum are both vectors, the equations relating them are true in every spatial direction.

With cross products, one must remember the correct order of the vectors; r × F and F × r have opposite signs — if you use the second, you’ll get the wrong answer. Note that r appears first in both the torque and angular momentum equations.

The following story may help, or not. The SLAC computer center assigned each authorized user a unique three-letter code, usually their initials. Apparently, they already had an RLP, so they gave me RXP. That prompted my clever colleagues to call me: Angular Momentum Piccioni. (Believe it or not, but that actually passed for humor in graduate school.)

If you’re not sure how to answer the question: “So, what’s your sign?” perhaps this will help. Recall the standard notation for angles in trigonometry. In the xy-plane, zero degrees is the horizontal direction to the right (+x) and 90 degrees is vertically up in the plane (+y). Angles grow more positive in the counterclockwise direction. If an object is rotating counterclockwise, its angle is increasing and its angular velocity ω is > 0. Using your right hand, aim your fingers along that object’s path, turning them counterclockwise. Your thumb is now pointed toward you in the +z-direction.

Perhaps surprisingly, like the linear velocity v, the angular velocity ω is a vector: it has a direction, the axis of rotation, and a magnitude, the rate of rotation, dθ/dt. Some vector equations involving ω are: τ•ω = power expended by torque L = I ω If the sum of all torques in one direction equals zero, the angular momentum in that same direction will not change — it will be conserved. This is exactly analogous to linear momentum being conserved in one direction if all forces sum to zero in that direction. When τ=0, the sum of all torques is zero in every direction, and angular momentum is conserved about every axis in every direction.

Another useful vector equation for rotational motion relates the linear velocity v of a particle at position r rotating with angular velocity ω: v = ω × r. Indeed, an even more general equation holds: dq/dt = ω × q, for any vector q rotating with angular velocity ω.

In V1p20-4, Feynman lists rules for manipulating vectors in 3D using the dot and cross products. I added a few more. Here a, b, and c are vectors and h is any constant. Keep in mind that when a = b × c, a is perpendicular to both b and c.

1. (ha)•b = h(a•b)

2. (ha)×b = h(a×b)

3. b•a = a•b 4. b×a = –a×b 5. a×a = 0 6. a×(b+c) = a×b + a×c 7. a•(b×c) = (a×b)•c 8. a×(b×c) = b(a•c) – c(a•b)

9. a•(a×b) = 0

Gyroscopes V1p20-5 We now come to Feynman’s “most remarkable and amusing” spinning wheel: the gyroscope.

Imagine a person holding a spinning wheel while sitting on a chair that swivels freely. The wheel’s axis is initially horizontal. To demonstrate the conservation of angular momentum, the person (a physicist, who else?) turns the wheel’s axis upward so that it now points vertically. Initially, the total angular momentum of the entire system — wheel, chair, and physicist — about the vertical axis was zero. The only external torque is the floor pushing upward to support the system’s weight. Since a vertical torque can’t change vertical angular momentum, the total angular momentum about the vertical axis must be conserved. To achieve this, the chair and physicist must rotate in the opposite direction of the wheel. That states the result we expect — angular momentum conservation — but exactly how are the chair and physicist forced to rotate?

Figure 41-1 illustrates a gyroscope with forces +F and –F being applied to the ends of its axle. The force is in the +x-direction on the left and in the –x-direction on the right. Initially, at time A, the gyroscope is spinning about the y-axis with angular velocity ω_A and angular momentum L_A.

Figure 41-1 Gyroscope with Torques The two forces F produce a torque τ in the +z direction, which causes the gyroscope to rotate about the x-axis with angular velocity Ω. At time B, a short time interval dt after time A, the gyroscope’s axis has rotated about the x-axis by angle dθ. Both ω_A and L_A rotate about the x-axis toward the z-axis to their new directions ω_B and L_B. Although it’s not labeled in the figure, dθ is the angle between L_A and L_B. Let’s go through the math to see why each part of this description is correct.

Let b equal the lever arm of force F acting on each end of the axle. On the left, b is in the –y-direction and F is in the +x-direction. For clarity, let’s do this for the left side in both component and vector notation: τ_z = xF – yF = 0 – (–b)F τ = r×F = (–b) F (times –1 as zyx is odd)

We get the same result for the right side of the figure, where both b and F flip polarities. The total torque is then τ = 2bF. This total torque rotates angular momentum L, changing its direction but not its magnitude. At time A shown in the figure, the axle is horizontal, the torque is vertical, and L is in the +y-direction. In the infinitesimal time interval dt, the vertical torque increases the vertical component of L, by: dL_z = dt τ_z Since dθ is the angle through which L rotates in time dt, we also have: dL = L dθ Combining these yields: dt τ = L dθ τ = L dθ/dt = L Ω Recalling the equation dq/dt = ω × q, and that Ω = dθ/dt, we can write this in vector notation as: τ = dL/dt = Ω × L Thus applying force F to each end of the axle rotates the axis of rotation about the x-axis at the rate Ω = 2bF/L. To turn the spinning wheel’s axle from horizontal to vertical, the physicist must apply such forces to the axle. By Newton’s third law, the axle applies equal and opposite forces to the physicist making his head spin, along with all the rest of him and the chair.

One might wonder what happened to the original horizontal angular momentum. When the axle was turned vertically, L became zero. Why didn’t the physicist and chair start rotating about the y-axis? The answer is the floor. L isn’t conserved because the floor applies an external torque by pushing up against the chair and preventing it from flipping and rotating about the y-axis.

The same ideas apply to spinning tops. As shown in Figure 41-2, gravity exerts force F, pulling the top downward. We treat that force as acting on the top at R_CM, the top’s center of mass. This creates a horizontal torque that changes the direction of the top’s axis of rotation.

Figure 41-2 Spinning Top with Precession Ω The top spins rapidly about its axis, while its axis of rotation slowly precesses, turning about the vertical direction of gravity’s pull. The equations for the precession rate Ω are: τ = R_CM × F τ = Ω × L τ = Ω × ω I The direction of precession is horizontal, perpendicular to the applied force.

Math or Miracle?

In V1p20-6, Feynman muses about the extent to which we really understand gyroscopes. Yes, we know all the equations and can describe their behavior mathematically. But, do we really understand it in a visceral sense? Who would be comfortable saying: “Of course the gyroscope’s motion is perpendicular to the applied force”?

Feynman adds this very important guidance: “It will turn out, as we go to more and more advanced physics, that many simple things can be deduced mathematically more rapidly than they can be really understood in a fundamental or simple sense. This is a strange characteristic, and as we get into more and more advanced work there are circumstances in which mathematics will produce results which no one has really been able to understand in any direct fashion.” Can we better understand why a gyroscope moves perpendicular to the ap applied force? Figure 41-3 shows that the particles of the gyroscope are not moving entirely within the xz-plane.

Figure 41-3 Gyroscope with Torques

The two F forces are trying to turn the gyroscope about the z-axis. The forces move the spinning particles very slightly in the +y-direction on the +x side, as shown. On the –x side, the particles move in the –y-direction (not shown). This out-of-plane motion turns the gyroscope, rotating it slightly about the x-axis, as explained above.

Nutation What we’ve described in the prior section is the steady precession of a gyroscope subject to a constant torque. This circumstance would occur if one end of the axle were supported on a gimbal bearing, and the other end were lovingly put into motion at exactly the right precession rate. In other words, smooth uniform precession is an equilibrium state in which the precession rate precisely matches the applied torque.

But, what if precession and torque don’t match? For example, what if we hold the free end of the axle stationary, and then let go? While we were holding it stationary, we had to support its weight, thereby balancing the gravitational torque. But when we release the axle, the gyroscope is suddenly exposed to the torque of gravity. Is it really possible that the downward pull of gravity, which we all know so well, pushes the gyroscope sideways instead of down? As Feynman says in V1p20-7: “Anyone in his right mind would think that the [gyroscope] would fall.”

What really happens is that the free end of the axle does start to fall and it also starts to precess. Like a mass on a string that is stretched and then released, the gyroscope will overshoot. Its axle will drop below its equilibrium height and precess too fast, faster than the rate that matches the gravitational torque. The excess precession rate will drive the axle upward, again overshooting equilibrium, whereupon the cycle repeats. This oscillating process, shown in Figure 41-4, is called nutation.

Figure 41-4 Nutating Gyroscope

Without friction or other damping, the path of the free end of the axle would be a cycloid, the path of a stone stuck in the tread of an automobile tire. More realistically, friction damps the nutation and the oscillations diminish. The gyroscope eventually settles into equilibrium, with its precession rate matching the gravitational torque. At equilibrium, the axle end will be somewhat below its starting point. This lower height causes a slight tilt that reduces the vertical component of angular momentum of the spinning motion, which balances the increased vertical angular momentum of precession. The detailed equations involve third-order polynomials and are quite complex, hence Feynman’s amusement.

Principal Axis Theorem The principal axis theorem states: every rigid body, however irregular, has three mutually orthogonal axes through its center of mass such that when rotating about any one of these axes, the body’s angular momentum is parallel to its angular velocity. In addition, the two axes that correspond to the body’s maximum and minimum moments of inertia are both principal axes. We’ll examine below a situation involving rotation about a non-principal axis. But first, let’s finish discussing principal axes.

If a body has a symmetry property, as does an isosceles triangle, the line of symmetry is a principal axis.

Consider any body, define coordinates such that the body’s principal axes are along the x, y, and z directions, and call the moments of inertia about these axes I_x, I_y, and I_z. We can write any angular velocity vector ω and angular momentum L as: ω = (ω_x, ω_y, ω_z)

L = (L_x, L_y, L_z)

L = (I_x ω_x, I_y ω_y, I_z ω_z)

The kinetic energy of rotational motion is then: T = 1/2 L • ω

Finally, we arrive at the promised example of rotation along a non-principal axis. As shown in Figure 41-5, a disk is mounted askew on a rod that passes through the disk’s CM. The axis of rotation is the centerline of the rod, but that is not a principal axis of this disk.

Figure 41-5 Rotation About Non-Principal Axis

Choose the z-axis to be perpendicular to the disk face, passing through the CM, and pick any two orthogonal diameters of the disk to be the x and y axes. By symmetry, our coordinate axes are the disk’s three principal axes. As shown at the end of this chapter, the moments of inertia of a disk of mass M and radius R are MR^2/2 about the z-axis and MR^2/4 about both the x and y axes. As above, we can write the angular velocity vector ω and angular momentum L as: L = (I_x ω_x, I_y ω_y, I_z ω_z)

ω = (ω_x, ω_y, ω_z)

L = (ω_x, ω_y, 2ω_z) MR^2/4

The key point here is that angular momentum L is not parallel to ω, the axis of rotation. This means that as the rod turns, L is constantly changing, requiring continual torques in ever changing directions. Whatever bearings hold this rod in place will be substantially stressed. This is one reason it pays to get your tires balanced and aligned.

Moments of Inertia of Disk & Ring We’ll do the calculation later.

For a ring with outer radius R, inner radius r, total mass M, and area mass density µ (M = µπ[R²–r²]). A disk is the special case of r = 0. First find the moment of inertia I for the axis of rotation through the CM and perpendicular to the ring's plane by integrating over the disk's radial coordinate u, from u=r to u=R. The distance from the disk point at (u,θ) to the axis of rotation equals u. At each value of u, the arc length around the disk equals 2πu. The integral sums (mass/area) × (distance to axis)² × (area).

I = ∫ µ u² 2πu du; u from r to R I = 2πµ ∫ u³ du I = 2πµ u⁴/4; u from r to R I = πµ (R⁴–r⁴)/2 I = πµ (R²–r²)(R²+r²)/2 I = M(R²+r²)/2

It may seem surprising that a larger r, the hole radius, seems to increase I. A larger r does increase the average distance from the rotational axis, but it also reduces M. From the prior equation I = πµ (R⁴–r⁴)/2, we see that the net effect of larger r is actually to reduce I, as expected. Now calculate the moment of inertia for any diameter across the ring; call that the y-axis. The distance of the disk point at (x,y) to the axis of rotation equals x.

I = ∫ µ x² 2πu du; u from r to R This looks like a tough integral; it's time for a valuable clever trick. If we compute I about the x-axis, we get the same equation except x² would be replaced by y². Since the ring is circularly symmetric, I must equal I. It is much easier to calculate I+I and then divide by 2.

y x y I = 1/2 ∫ µ (x²+y²) 2πu du; u from r to R I = 1/2 ∫ µ (u²) 2πu du; u from r to R I = πµ u⁴/4; u from r to R I = πµ (R⁴–r⁴)/4 I = πµ (R²–r²)(R²+r²)/4 I = M(R²+r²)/4

Rotational Motion Review Chapters 39, 40 & 41 For linear motion, the internal forces among a collection of particles cancel one another, leaving only external forces to act on the center of mass of the particles, as if it were a single object. Primary linear and rotational variables are compared below.

In evaluating terms in a cross product, such as L = +x p –y p, the sign rule is: even combinations xyz, z y x yzx, and zxy have plus signs, while odd combinations xzy, yxz, and zyx, have minus signs. The number of swaps from xyz determines if a combination is even or odd.

For rotational motion, we define: ℓ, the lever arm of force F θ, the angle between r & F or r & p These additional relationships exist: Work W = τ dθ τ = F r sinθ = r × F τ = F ℓ τ = dL/dt L = r × p L = r p sinθ L = p ℓ I = m r² Kinetic energy T = 1/2 I ω²

Centers of Mass (CM) & Moments of Inertia A body's CM lies within an envelope containing all its parts. The CM of a two-part object lies along the line connecting the CM of each individual part. The CM of a symmetric body lies along its line of symmetry.

The moment of inertia of a multi-part object equals the sum of the moments of each part, provided all rotate about the same axis.

The Pappus centroid theorem says the volume swept by a surface rotating about an external axis equals its area times the distance its centroid moves.

The parallel-axis theorem states I = MR² + I_CM. A body's moment of inertia I about an axis Z, equals the moment of inertia of the body about its own center of mass, I_CM, plus MR², its mass times the square of the distance of its center of mass to Z, the axis of rotation.

The principal axis theorem states every rigid body has three mutually orthogonal axes through its CM such that when rotating about any one of these axes the body's L is parallel to ω. Also, the two axes that correspond to the maximum and minimum moments of inertia of that body are both principal axes.

3D Rotations that are "Quite Striking"

Angular velocity ω is a vector; its direction is the axis of rotation and its magnitude is the rotation rate. Some equations involving ω are: τ•ω = power expended by torque L = I ω, definition of angular momentum dq/dt = ω×q, for any q rotating at ω When a gyroscope is subjected to a torque, it precesses with angular velocity Ω, according to: τ = dL/dt = Ω × L = Ω × ω I

Some Common Moments of Inertia

## Chapter

Physics of Waves & Sound In this chapter, we begin exploring the physics of waves, a phenomenon that in V1p47-1 Feynman says: "appears in many contexts throughout physics. …Waves are related to oscillating systems… wave oscillations appear not only as time-oscillations at one place, but propagate in space as well."

We have often encountered oscillations and waves in our prior studies. Harmonic oscillators execute repetitive cycles, moving about fixed locations (Feynman Simplified 1B Chapters 12 through 14), while light waves (Feynman Simplified 1C Chapters 30 through 38) oscillate in both time and space. We discovered how the interference of light waves explains reflection, refraction, and other intriguing phenomena.

We now consider some additional aspects of wave behavior. One such behavior is interference in time, in which the interference of two combining waves changes with time rather than position.

ons, and interfere due to reflections from boundaries. Other aspects of wave behavior arise when wave velocities change due to differences in the media that the waves traverse. Yet another wave behavior involves wave velocities that vary with wavelength, which we discuss in the next chapter.

In this chapter, we confine our attention to waves whose velocities are the same at all wavelengths. We know from our everyday experience that neither the speed of sound nor the speed of light changes appreciably over the range of wavelengths to which humans are sensitive. If for example, high frequency sound traveled faster than low frequency sound, a concert would sound quite different in the front row than in the rear balcony. The bass vocal would appear late in the balcony. Similarly, if red light traveled faster than blue light, a distant flash of white light would appear red initially, would rapidly become white, and then would finally turn blue. The absence of such effects confirms that the speeds of the sound and light we perceive do not change with wavelength.

Wave Motion

Waves are motion. They move through space and change over time. Let’s briefly review the wave terminology presented in Chapter 31. As illustrated in Figure 42-1, waves oscillate in identically repeating cycles. Wavelength λ is the spatial extent of one complete cycle, the distance between consecutive crests or troughs. Amplitude A is how high the wave goes up above and goes down below its average.

Figure 42-1 Wave Terminology

If the above wave were moving to the left, its entire shape would move left in unison as if it were a solid object. If we focus on a specific point, such as point Q, we would see the wave height going up and down as time passes, oscillating between +A and –A. If the wave goes through 9 full cycles per second, its frequency f is 9 cycles/second, or 9 Hertz, which is abbreviated 9 Hz. The product of wavelength and frequency equals the wave’s velocity v: λf=v; (meters/cycle) times (cycles/second) = (meters/second). Frequency can also be expressed in radians/second: the angular frequency ω=2πf. Another important quantity is the wave number k, which equals 2π/λ and has units of radians/meter.

Figure 42-2 shows a hypothetical example of an electric field from an accelerating charge.

Figure 42-2 Electric Field E vs. Time t and Distance r/c

The upper part of the image plots field E versus time t, at two fixed positions. The solid line represents E(t) near the accelerating charge, and the dashed line is E(t) at a greater distance r. Since electric fields travel at the speed of light, the time shift between the solid and dashed curves equals r/c. As often discussed earlier, a remote observer sees E(t*), the field at retarded time t*=t–r/c. The lower part of Figure 42-2 plots the electric field seen at various positions at a fixed time. The horizontal axis is distance r from the source divided by the wave speed c. Here we see that A, the field at an earlier time, has traveled farther than B, the field at a later time.

In general, the electric field’s wave height is most simply represented as a function of r–ct: f(r–ct). To demonstrate this, compare the field E at a position r and time t with E at position r+Δr and time t+Δt: f(r+Δr –c[t+Δt]) = f(r–ct + [Δr–cΔt]) f(r+Δr –c[t+Δt]) = f(r–ct), if Δr = cΔt. This means every part of the wave is reproduced identically at all values of Δr and Δt for which Δr=cΔt. Hence the entire waveform moves in unison through space at velocity c.

The above analysis can be applied to other types of waves. Any wave phenomenon governed by a linear differential equation and with the same velocity v at all frequencies can be represented by a function of the form f(r–vt).

Propagation of Sound

Unlike light, we know that sound needs a medium to travel through — sound cannot travel through vacuum. This is because sound is the organized motion of the atoms and molecules of which the medium is composed. Its motion is determined by the properties of those atoms and molecules. As such, Feynman says in V1p47-2: “In short, sound is a branch of mechanics, and so it is to be understood in terms of Newton’s laws.” He provides this important insight: “We shall give a derivation of the properties of the propagation of sound between the source and the receiver as a consequence of Newton’s laws, and we shall not consider the interaction with the source and the receiver. Ordinarily we emphasize a result rather than a particular derivation of it. In this chapter we take the opposite view. The point here, in a certain sense, is the derivation itself. This problem of explaining new phenomena in terms of old ones, when we know the laws of the old ones, is perhaps the greatest art of mathematical physics. The mathematical physicist has two problems: one is to find solutions, given the equations, and the other is to find the equations which describe a new phenomenon. The derivation here is an example of the second kind of problem.” Consider the simplest example of sound propagation: motion in one dimension through air.

We must first understand the physics of what happens when an object moves through air. As it moves, an object pushes air molecules out of its way. If the object moves very slowly, air will simply flow around the object with only minor disturbance. From Chapter 15, we know the average molecular velocity due to thermal energy is given by: m v² / 2 = 3 kT / 2 avg Here T is temperature measured in Kelvin, and k is Boltzmann’s constant (not the wave number which is also denoted by k). For nitrogen molecules (N₂) at 293K (20ºC, 68ºF): v ≈ 509 m/s.

avg

When an object moves rapidly through air, faster than air can gently flow out of its way, the air becomes compressed and its pressure rises. This high-pressure air compresses neighboring air molecules, resulting in a pressure wave that spreads outward through space, as illustrated in Figure 42-3.

Figure 42-3 Sequential Views of Pressure Wave In Air In the above image, the dots represent air molecules and the black rectangle is a piston. The left quarter of the image shows an initially static condition. In the second quarter, the piston expands, compressing the adjacent air molecules, raising their pressure. In the third and fourth quarters, air molecules compress adjacent molecules, resulting in a pressure wave moving to the right.

What variables do we need to analyze this process? Since this process is dynamic, changing in both space and time, we must know key variables as functions of both position and time. Those key variables are density, pressure, and displacement, the latter being how much the air molecules have moved. Molecular velocities and accelerations are also important, but these are calculable by taking time derivatives of displacements.

If the original source of sound is very far away, the wavefront, the surface of a wave crest, is nearly flat. If the direction of motion is along the x-axis, the flat wavefront comprises a yz-plane perpendicular to the x-axis. By symmetry, the values of all variables must be the same at all y and all z. This reduces the problem to one spatial dimension, and we can write the displacement as D(x,t).

The Newtonian analysis of sound that we will present relates the displacement, density, and pressure of small gas volumes — in V1p47-3 Feynman calls these elements of gas. This analysis makes certain assumptions about the size of these gas elements and the wavelengths of the sound waves that propagate through them.

Firstly, in order to apply the principles of thermodynamics, the gas elements in our analysis must be much larger than atoms. From Chapters 15 through 24, we know that concepts like pressure and density are valid on macroscopic scales, but not on atomic scales. An individual molecule does not have a well-defined pressure, but millions of gas molecules do. For our macroscopic descriptors — density, pressure, and displacement — to be valid, our gas elements must be much larger than the mean free path of individual molecules.

Secondly, the sound waves of interest must have wavelengths much longer than that same molecular mean free path. For a pressure-density wave to move through a gas, energy must flow from molecules in one region to molecules in adjacent regions. Molecules moving away from higher-pressure regions must collide with molecules in neighboring regions and thereby transfer energy to them.

For pressure-density waves with wavelengths much longer than the mean free path, molecules undergo many collisions in moving from high-pressure to low-pressure regions. Myriad collisions efficiently transfer energy, thus maintaining the wave’s driving force and keeping the wave moving forward.

Conversely, for pressure-density waves with wavelengths much shorter than the mean free path, molecules can undergo few if any collisions while moving far enough to equalize pressure differences. Here, energy is not efficiently transferred, the driving force is not sustained, and the wave rapidly fades away.

The result of this effect is that sound travels farther when its wavelength is longer and its frequency is lower. A particularly impressive example is the infrasonic communication of elephants. Infrasonic denotes frequencies below 20 Hz, the limit of human hearing. Elephants can communicate via infrasound across distances of up to 17 km (11 miles). By comparison, human vocalizations have minimum frequencies of 70 Hz for men and 140 Hz for women.

These assumptions are entirely valid for typical sound waves. Under normal conditions, the mean free path in air is typically about 0.1 microns, while the wavelength of 3 kHz sound is about one million times larger at 0.1 meters.

The Sound Wave Equation The physics of sound involves the interaction of three effects:

## 1. Gas motion creates density gradients

## 2. Density gradients create pressure gradients

## 3. Pressure gradients drive gas motion

Note that the gas density we are discussing here is its mass mass per unit volume, not the number of molecules per unit volume.

We begin with the second effect. From Chapter 15, recall the ideal gas law: PV = NkT. Here P is pressure, N is the number of molecules in volume V, T is temperature in Kelvin, and k is Boltzmann’s constant. Assuming that T is constant, pressure P will be a function of only (N/V). In an ideal gas at constant temperature, pressure is: P = ρkT/m. Here m is the average molecular mass, and ρ is the mass density. While air is a nearly ideal gas, let’s be more general and allow pressure to be an unknown function of density: P = g(ρ).

It is convenient to define equilibrium values of key variables with a subscript zero: at equilibrium, without sound waves, the gas pressure is P₀ and its density is ρ₀, with P₀ = g(ρ₀). At sea level, the average atmospheric pressure P₀ is 1.01325 bars, where 1 bar = 10⁵ newton/m² = 10⁵ kg/m·sec².

Experimentally, we find that the pressure changes caused by sound waves are quite small, typically parts per million of P₀. Sound intensity is measured using a logarithmic scale, since that nearly matches the response curve of human hearing. An rms (root-mean-square) pressure change of ΔP corresponds to a sound intensity in db (decibels) of: Sound Intensity I = 20 log₁₀(ΔP/P_ref) db. Here P_ref = 2×10⁻¹⁰ bar. To calculate rms, take the square root of the average of the square of the pressure change throughout a complete cycle. For a sinusoidal wave, the rms amplitude equals the peak amplitude divided by √2.

Some examples of sound intensity are: 60 dB = 10³ P_ref = 2×10⁻⁷ bar: conversation 80 dB = 10⁴ P_ref = 2×10⁻⁶ bar: screaming child 100 dB = 10⁵ P_ref = 2×10⁻⁵ bar: chainsaw 120 dB = 10⁶ P_ref = 2×10⁻⁴ bar: rock concert

We see that sound waves change air pressure by only parts per ten-thousand to parts per ten-million. Hearing loss can result from excess exposure to loud sounds. Audiologists recommend these maximum continuous exposure limits: 10 seconds at a rock concert, 15 minutes operating a chainsaw, and 12 hours with screaming children. Other issues may reduce one’s tolerance to much shorter durations. Millions of years of human evolution have resulted in an intense parental sensitivity to their child’s scream.

We will later consider much louder sounds, such as explosions. Here, we will consider only pressure changes much smaller than 1 bar. Let: ρ = ρ₀ + dρ, with dρ << ρ₀ P = P₀ + dP, dP << P₀ P₀ = g(ρ₀)

P = g(ρ₀) + [dg(ρ)/dρ] dρ

Here the term in [ ]’s is the first derivative of g(ρ) with respect to ρ, evaluated at ρ₀. We are neglecting higher order derivatives because dρ is very small. To reduce clutter, define the term in [ ]’s to be κ, resulting in: P = P₀ + dP = g(ρ₀) + κ dρ.

{Eqn. 2}: dP = κ dρ, near equilibrium.

For now, this relationship between density changes and pressures changes is all we need for effect #2 from the list of three effects at the start of this section.

Let’s next address effect #1: gas motion creates density gradients. Figure 42-4 illustrates changes to an element of air (the shaded box). The gas element is originally on the left side of the image, and is then displaced toward the right.

Figure 42-4 Displacement of Element of Air.

Recall our displacement model: each element at x and t is displaced by D(x,t). Therefore the displacements D₁ and D₂ in the figure are: x₃ = x₁ + D₁ = x₁ + D(x₁,t)

x₄ = x₂ + D₂ = x₂ + D(x₂,t)

While the volume of the element may change, the number of molecules within the element and their average mass do not. This means density times volume must be constant. In our analysis, changes only occur in the x-direction; the element’s cross sectional area in the yz-plane, σ, is constant. Hence: ρ₂ σ (x₂–x₁) = ρ₀ σ (x₄–x₃)

ρ₂ (x₂–x₁) = ρ₀ [(x₄–x₃)]

ρ₂ = ρ₀ + ρ₀ { [D(x₂,t)–D(x₁,t)]/(x₂–x₁) }

In the limit that x₂ goes to x₁, the expression in { }’s becomes the first derivative of displacement D with respect to position x. To be more precise, this is a partial derivative. We discussed partial derivatives in Chapter 22. Briefly, D is a function of two independent variables: position x and time t. This partial derivative describes the change in D resulting from a change in x, at constant t. Using ρ₀ = ρ₀ +dρ₀, we have: ρ₂ - ρ₀ = -dρ = (ρ₀ +dρ) ∂D/∂x.

{Eqn. 1}: dρ = – ρ₀ ∂D/∂x.

In the last step, we dropped dρ from the coefficient of ∂D/∂x, since dρ<<ρ₀. Feynman notes that this equation makes good physics sense. We should always look for the physics that our equations strive to represent. The gas density must change if the displacements are different at different x positions. Feynman adds that the sign is correct: where the displacement increases, the gas elements are stretched and the density decreases. This is the equation we need for effect #1.

We next address the last effect listed at the start of this section: pressure gradients drive gas motion. Motion is driven by force, so we need an equation relating pressure.

gradient to force.

Figure 42-5 shows the pressure gradient on a gas element between x₁ and x₂.

Figure 42-5 Pressure Difference on Gas Element

The net force F in the +x-direction equals [P₁–P₂] multiplied by σ, the cross sectional area of the gas element: F = [P₁–P₂] σ F = [P(x₁) – P(x₂)] σ

In the limit that x₁ goes to x₂ and dx = x₂ – x₁ becomes infinitesimal, force F becomes: F = – {[P(x₂)–P(x₁)] / (x₂–x₁)} (x₂–x₁) σ F = – (∂P/∂x) σ dx

Force F accelerates the gas element, which has mass ρ (dx)σ. The acceleration is the second partial derivative of displacement D, according to: (ρ dx σ) ∂²D/∂t² = F (ρ dx σ) ∂²D/∂t² = – (∂P/∂x) dx σ {Eqn. 3}: ∂P/∂x = – ρ ∂²D/∂t²

I repeat {Eqn. 1} and {Eqn. 2} for your convenience: {Eqn. 1}: dρ = – ρ ∂D/∂x {Eqn. 2}: dP = κ dρ, near equilibrium

We next combine these equations, firstly using {Eqn. 2} and {Eqn. 3} to eliminate dP: κ dρ = dP κ ∂ρ/∂x = ∂P/∂x κ ∂ρ/∂x = – ρ ∂²D/∂t²

We next combine this with {Eqn. 1} to eliminate dρ: dρ = – ρ ∂D/∂x ∂ρ/∂x = – ρ ∂²D/∂x² – κ ρ ∂²D/∂x² = – ρ ∂²D/∂t² κ ∂²D/∂x² = ∂²D/∂t²

Feynman then substitutes κ with c², the square of the speed of sound, yielding the wave equation for sound: ∂²D/∂x² = ∂²D/∂t² / c²

Solutions of Sound’s Wave Equation

In V1p47-6, Feynman says we should examine this equation to determine if it “really does describe the essential properties of sound in matter.”

Let’s first examine whether the general wave equation f(r–vt) satisfies the wave equation for sound. Since we are working in only one dimension, here r=x. Let u=x–vt.

∂²f/∂x² = [∂/∂x] [∂f/∂x]

∂²f/∂x² = [(∂u/∂x) ∂/∂u] [(∂f/∂u) (∂u/∂x)]

∂²f/∂x² = [(1) ∂/∂u] [(∂f/∂u) (1)]

∂²f/∂x² = ∂²f/∂u²

Similarly: ∂²f/∂t² = [∂/∂t] [∂f/∂t]

∂²f/∂t² = [(∂u/∂t) ∂/∂u] [(∂f/∂u) (∂u/∂t)]

∂²f/∂t² = [(–v) ∂/∂u] [(∂f/∂u) (–v)]

∂²f/∂t² = + v² ∂²f/∂u²

Putting these together: ∂²f/∂u² = ∂²f/∂x² = ∂²f/∂t² / v²

which corresponds exactly to the sound wave equation with v=c.

Feynman says: “We find, therefore, from the laws of mechanics that any sound disturbance propagates with the velocity c, and in addition we find that:” c = √κ = √(dP/dρ)₀ where the final “0” indicates the derivative evaluated at equilibrium pressure and density.

Feynman emphasizes that: “we have related the wave velocity to a property of the medium.” The sound wave equation clearly applies equally well to waves moving toward –x, since the equation contains the even power c² and not any odd power such as c.

Now consider the sum of two sound waves: D(x,t) and S(x,t), both of which satisfy the wave equation.

∂²D/∂x² = ∂²D/∂t² / c² ∂²S/∂x² = ∂²S/∂t² / c²

For any H(x,t) = αD(x,t) + βS(x,t), where α and β are arbitrary constants: ∂²H/∂x² = α∂²D/∂x² + β∂²S/∂x² ∂²H/∂x² = {α∂²D/∂t² + β∂²S/∂t² } / c² ∂²H/∂x² = [∂² {αD + βS} /∂t²] / c² ∂²H/∂x² = ∂²{H}/∂t² / c²

This means our sound wave equation complies with the principle of linear superposition, as is evident from the fact that it is linear in the displacement D.

Speed of Sound

From above, the speed of sound is given by: c = √(dP/dρ)₀

We now need to address any temperature changes that might occur as a sound wave propagates through a medium. We know that temperature increases when a gas is compressed, and that temperature decreases when a gas expands.

In V1p47-7, Feynman relates an interesting story: “Newton was the first to calculate the change of pressure with density, and he supposed that the temperature remained unchanged. He argued that the heat was conducted from one region to the other so rapidly that the temperature could not raise or fall. This argument gives the isothermal speed of sound, and it is wrong. The correct deduction was given later by Laplace, who put forward the opposite idea — that the pressure and temperature change adiabatically in a sound wave. The heat flow from the compressed region to the rarefied is negligible so long as the wavelength is long compared with the mean free path.”

The modest heat flow does not affect sound’s speed but does lead to energy loss, which increases as the wavelength approaches the mean free path.

Assuming adiabatic change — no heat flow — thermodynamics states (Chapter 15): PV^γ = constant#1 Here, γ is the specific heat ratio. Since density is inversely proportional to volume, this can be rewritten: P = constant#2 × ρ^γ

Next take the derivative with respect to P.

1 = constant#2 × γ ρ^(γ–1) dρ/dP 1 = (P / ρ^γ) × γ ρ^(γ–1) dρ/dP dP = (P / ρ) × γ dρ dP/P = γ dρ/ρ

Plugging this into the equation for the speed of sound: c² = (dP/dρ) = γP/ρ s₀

The total mass of the gas equals ρV, density times volume, which equals mN, the average molecular mass times number of molecules. Employing that and the equation for an ideal gas, PV=NkT, we have: c² = γP/ρ = γ (PV) / (ρV)

c² = γ (NkT) / (mN)

c² = γkT/m

Since temperature is the only variable in the last equation, we learn that the speed of sound is proportional to the square root of temperature.

We also know that kT = m<v²>/3, where <v²> is the average molecular velocity squared.

Plugging that in yields: c = <v> √(γ/3)

For air, γ ≈ 1.4: c ≈ <v> 0.68 At the start of this chapter, we calculated that the average velocity of nitrogen molecules in air is typically 509 m/s at 20ºC. For oxygen molecules that velocity is 477 m/s. The weighted average (4 N per O) velocity is 503 m/s, which yields: c in air @ 20ºC ≈ 343.5 m/s = 1127 feet/sec = 1236.7 km/hr = 768.5 mph This is very close to the measured value of 343.3 m/s. If we included heavier gases, such as argon, the average velocity would decrease and better approximate the true speed of sound in air.

Again, Feynman notes that this result makes physics sense. Sound propagation depends on gas molecules banging into one another, so it makes sense that sound waves propagate at roughly the same speed as the gas molecules move.

## Chapter 42 Review: Key Ideas

Any wave phenomenon governed by a linear differential equation and with the same velocity v at all frequencies can be represented by a function of the form f(r–vt).

Feynman says sound is to be understood in terms of Newton’s laws of mechanics. He adds “explaining new phenomena in terms of old ones, when we know the laws of the old ones, is perhaps the greatest art of mathematical physics. The mathematical physicist has two problems: one is to find solutions, given the equations, and the other is to find the equations which describe a new phenomenon.” Our macroscopic analysis of sound propagation uses descriptors — density ρ, pressure P, and displacement D — that are valid for gas volumes much larger than the mean free path of individual molecules but much smaller than the wavelength of sound waves. Typically in air, the mean free path is about 0.1 microns, while the wavelength of 3 kHz sound is about one million times larger.

The physics of sound involves the interaction of three effects: gas motion creates density gradients; density gradients create pressure gradients; and pressure gradients drive gas motion. Another key factor is that, as sound propagates, heat flow is minimal; gas expansion and compression are adiabatic. The three equations that relate these effects, and the resulting wave equation are: {Eqn. 1}: dρ = – ρ ∂D/∂x {Eqn. 2}: dP = κ dρ, near equilibrium {Eqn. 3}: ∂P/∂x = – ρ ∂2D/∂t2 ∂2D/∂x2 = ∂2D/∂t2 / c2 Here c is the speed of sound.

For specific heat ratio γ, pressure P, mass density ρ, temperature T, molecular mass m, average molecular velocity <v>, and Boltzmann’s constant k, the equations for c are: c2 = (dP/dρ) = γP/ρ = γkT/m = <v2> (γ/3)

c in air @ 20ºC ≈ 343.5 m/s = 1127 feet/sec This is very close to the measured value of 343.3 m/s.

## Chapter 43 Theory of Beats

In this chapter, we discuss for the first time the interference of two waves of different frequencies. In V1p48-1, Feynman says it is easy to guess what will happen.

Start with two waves of the same frequency that arrive at point P along two different paths. If the waves arrive with zero relative phase shift, they interfere constructively. In this case, at point P: if the waves are light, it is bright; if the waves are sound, it is loud; and if the waves are electrons, there are many, to paraphrase Feynman.

Conversely, if the waves arrive 180º out of phase, they interfere destructively and the intensity at P is zero.

Now imagine that someone is gradually and uniformly turning a knob that adds a phase shift to one of the two waves. The relative phase angle will cycle slowly from 0º through 360º, and the interference will cycle from completely constructive to completely destructive and back again.

But, as Feynman points out, a wave whose phase is changing at a uniform rate is exactly the same as a wave with a slightly different frequency. To make that more concrete, consider a wave of frequency 36 Hz, 36 full cycles per second. Now gradually delay its phase angle at the rate of 10º per wave cycle. In one second, the wave will oscillate 35 times instead of 36 times, making its effective frequency 35 Hz.

Therefore, we expect two waves of slightly different frequencies to gradually cycle from completely constructive interference to completely destructive interference and back again.

Adding Waves Mathematically Consider two waves arriving at point P, one with the wave equation cos(ωt) and the other with cos(ωt). The total wave at P is simply the sum of the two cosines, as illustrated in Figure 43-1.

Figure 43-1 Two Similar Cosines and Their Sum As the figure demonstrates, where the crests of both waves align the intensity of their sum is large, and where the crest of one wave aligns with the trough of the other the intensity of their sum is small.

In Chapter 32, we encountered the useful formula: cosA + cosB = 2 cos[(A+B)/2] cos[(A–B)/2]

We can apply that formula here, with these definitions: ω = (ω+ω)/2 1 2 Δω=(ω–ω)/2 1 2 cos(ωt)+cos(ωt) = 2cos(ωt) cos(Δωt)

1 2 Let’s examine the case where ω and ω are quite close, (Δω<<ω), and calculate the intensity at P.

1 2 I = | 2 cos(ωt) cos(Δωt) |2 I = 4 < cos2(ωt) > < cos2( Δωt) > I = 4 (1/2) [1+cos(2Δωt)]/2 I = 1 + cos(2Δωt)

where we have taken the average over a full cycle of the high frequency term cos(ωt), but not averaged the low frequency term. The last equation shows that while the total wave at P oscillates rapidly at frequency ω, it slowly waxes and wanes at frequency 2Δω. Its intensity has a maximum of 2 and a minimum of zero.

Frequency 2Δω = ω – ω, is called the beat frequency.

1 2

Let’s redo this analysis with two waves of different amplitudes and frequencies. This time, we will use complex exponentials. Combine the waves:

A = A₁ exp{iω₁t} + A₂ exp{iω₂t}

The intensity is:

I = A A* I = [A₁exp{iω₁t}+A₂exp{iω₂t}]

× [A₁exp{–iω₁t}+A₂exp{–iω₂t}]

I = A₁² + A₁A₂ exp{i[ω₁–ω₂]t} + A₂² + A₁A₂ exp{–i[ω₁–ω₂]t}

I = A₁² + A₁A₂ {cos([ω₁–ω₂]t) + i sin([ω₁–ω₂]t)} + A₂² + A₁A₂ {cos([ω₁–ω₂]t) – i sin([ω₁–ω₂]t)}

I = A₁² + A₂² + 2A₁A₂ cos([ω₁–ω₂]t)

The intensity slowly oscillates at frequency (ω₁–ω₂) between the values (A₁+A₂)² and (A₁–A₂)². For A₁=A₂=1, this reduces our prior result.

Commercial Broadcasting Radio and television broadcasting employ the principle of linear superposition. They combine a high-frequency carrier wave with a low-frequency signal, and broadcast the resulting sum. Individual receivers remove the carrier wave, and present us with the remaining signal.

For AM radio, the carrier frequency is typically between 500 and 1700 kHz. Each channel is allocated a bandwidth of 10 kHz for their signal, which is adequate for normal conversation but not for high-fidelity music.

As above, the carrier wave has the form: C cos(Ωt). The carrier carries no information; its function is to separate the transmission from one station or channel from other broadcasts.

The signal wave carries the information being transmitted. Normal sound waves vibrate the membrane of a microphone, which converts those vibrations into electrical signals with the same waveform. The signal can have a very complex waveform, which shouldn’t be surprising considering the complexity of speech.

As discussed in Chapter 14, any realistic waveform can be represented by a series of cosine functions using Fourier transforms. In general, any waveform equals an integral over all frequencies of cosines, with a weighting factor for each frequency.

For simplicity, assume the signal is a pure tone, a wave composed of a single frequency, of the form: S cos(ωt). The carrier and signal are summed, producing the broadcast wave illustrated in Figure 43-2.

Figure 43-2 AM Radio Broadcast

The changing amplitude of the broadcast wave leads to the name: AM for amplitude modulation. For visual clarity, the two frequencies combined in the figure have a ratio of only about 10:1. In actual AM broadcasting, the ratio is typically 100:1 or more.

In V1p48-4, Feynman says a broadcast wave can be represented by:

A = C cos(Ωt) {1 + (S/C) cos(ωt)}

This can be rearranged as:

A = C cos(Ωt) + S cos(Ωt) cos(ωt)

A = C cos(Ωt)+ S[cos({Ω+ω}t) +cos({Ω–ω}t)]/2

The three terms above are the carrier at frequency Ω, and two side bands at Ω+ω and Ω–ω, as illustrated in Figure 43-3.

Figure 43-3 Plot of Intensity vs. Frequency

The figure presents the combined AM frequency spectrum when the signal is a pure tone. For more complex signals, additional side bands appear. The lower side band and upper side band contain exactly the same information content: they are redundant. For more efficient use of the available broadcast spectrum, clever engineers have implemented circuitry that eliminates the lower side band before broadcasting and restores that signal within the receiver.

FM radio provides higher fidelity and greater immunity from interference than AM. In FM, the amplitude of the broadcast wave does not change but its frequency does; hence the name FM for frequency modulation.

Again, a carrier frequency provides channel separation but no information. Carrier frequencies range from 88 to 108 MHz, with 200 kHz separation. Since human hearing does not extend beyond 30 kHz, the 200 kHz channel separation is more than sufficient to provide complete stereo audio fidelity and minimize interference from neighboring channels and other sources.

Information is transmitted via a signal that modulates the carrier frequency. The broadcast signal has the form:

A cos( [Ω + ω(t)] t)

Here ω(t) is the signal wave’s effective instantaneous frequency at time t.

The signal wave is often multiplexed, divided into several subbands, each providing distinct information. For example, broadcasting music in stereo is accomplished with L+R and L–R subbands. The L+R subband carries the signal for the sum of waveforms for the Left and Right speakers, while L–R carries the signal for the difference of those waveforms. Radio receivers that support stereo separately decode both subbands and drive the left speaker with the sum and the right speaker with the difference. Mono receivers simply drive all speakers with L+R.

In V1p48-5, Feyn One describes television broadcasting for black and white, 500×500 pixel resolution, which amounts to a signal bandwidth of 4 MHz. No one has a TV like that anymore. Today’s HDTV’s typically have resolutions of 1920×1080 pixels, and three 8-bit color channels. That would amount to a signal bandwidth of 1500 MHz. HDTV is practical only due to major advancements in data compression technology that reduce the transmitted signal bandwidth to 20 MHz or less.

From a mathematical standpoint, the ability to compress a 1500 MHz signal into a 20 MHz broadcast band means that the original information content is only about 1%. (For some shows, the interesting information content is even less than that.) Needless to say, the technologies in modern TV’s are light-years ahead of those of 50 years ago.

Wave Velocities

A wave composed of a single frequency can be represented by: exp{i(ωt–kx)} Here k is the wave number (radians per meter), and the wave’s velocity v equals ω/k. More precisely, ω/k is the phase velocity, as we will discuss shortly. We can rewrite the wave equation as: exp{ik(vt–x)}, or exp{iω(t–x/v)}

Combining two waves of equal amplitudes but different frequencies: A = exp{i(ω₁t–k₁x)} + exp{i(ω₂t–k₂x)} For the simple case of equal phase velocities, where v₁=ω₁/k₁=ω₂/k₂=v₂, the combined wave reduces to: A = exp{iω₁(t–x/v)} + exp{iω₂(t–x/v)} Substituting retarded time t*=t–x/v, this is the same equation discussed earlier that leads to wave modulation. The only change is that now we clearly see the modulation traveling through space: for every time increment Δt, the wave moves forward by Δx=vΔt.

Now let’s go back to the general case, where the two wave velocities may be different, and define: ω = (ω₁+ω₂)/2 Δω = (ω₁–ω₂)/2 k = (k₁+k₂)/2 Δk = (k₁–k₂)/2 Note that: ω₁ = ω + Δω ω₂ = ω – Δω k₁ = k + Δk k₂ = k – Δk Using Δω and Δk, we have these expressions: exp{i(ω₁t–k₁x)} = exp{i(ωt–kx)} exp{+i(Δωt–Δkx)} exp{i(ω₂t–k₂x)} = exp{i(ωt–kx)} exp{–i(Δωt–Δkx)} Now rearrange the equation for combined waves: A = exp{i(ω₁t–k₁x)} + exp{i(ω₂t–k₂x)} A = exp{i(ωt–kx)} [exp{i(Δωt–Δkx)} + exp{–i(Δωt–Δkx)}] A = exp{i(ωt–kx)} [2 cos(Δωt–Δkx)] This is another modulated wave. It oscillates at ω, travels at velocity v=ω/k, and is modulated by the term in [ ]’s, which depends on frequency and wave number differences.

Next, we consider a new situation: a light wave of a single frequency traveling through a medium where ω and k are not simply inversely proportional. Chapter 34 discusses the index of refraction: n. In transparent media, the apparent speed of light is reduced to c/n, where n is given by: n = 1+ q²N/{2εm(Ω²–ω²)} We say “apparent” speed of light, because photons always travel at speed c. The wave propagation velocity is reduced in a refractive medium because light is continuously absorbed and re-emitted with phase shifts that delay the wave.

A wave’s phase angle changes with distance according to the product kx. But as a wave moves through a refractive medium, the medium continuously adds a phase shift to the wave. The total phase shift ø is proportional to the distance traveled in the medium — the more atoms the wave passes the more its phase is shifted — thus ø=bx, for some constant b. This is equivalent to changing the value of k: k*=k+b. A wave entering a refractive medium doesn’t change its frequency ω, but when n>1, its wave number k increases and its wavelength λ decreases (λ=2π/k). With the same number of cycles per second but less distance per cycle, the wave’s velocity ω/k apparently decreases.

Since this apparently slower speed is due to phase changes, ω/k=c/n is called the wave’s phase velocity. It is the ratio of (phase angle change in radians per second) / (phase angle change in radians per meter) = (meters/second). An even more startling effect occurs when x-rays pass through normal materials, or when light passes through a gas of free electrons. In these cases, the medium’s resonant frequency Ω can be very small or even zero. When Ω<<ω, the refractive index simplifies to: n = 1 – β/ω² Here β = q²N/{2εm} is a constant that is certainly positive, since each of its component factors is positive. This means n<1, and, quite remarkably, the phase velocity c/n is greater than the speed of light.

Let’s examine this in more detail. For the above index of refraction, where n<1: ω/k = c/n k = nω/c k = ω/c – β/ωc Recall our equation for combined waves: A = exp{i(ωt–kx)} [2 cos(Δωt–Δkx)] For Δω << ω, and Δk << k, the combined wave A oscillates rapidly due to the exponential term, and is modulated more slowly by the cosine term. The velocity of the fast oscillation is ω/k, which is greater than c. But the velocity of the modulation, which is called the group velocity, is: v_g = Δω / Δk In the limit that Δω and Δk become infinitesimal: v_g = dω/dk We can calculate the group velocity from the equation for k and ω: ω – β/ω = ck dω/dk – (–β/ω²)(dω/dk) = c v_g = dω/dk = c / (1 + β/ω²) Since β>0, group velocity v_g is less s than c.

While the phase velocity ω/k>c, the group velocity dω/dk<c.

What is the physical significance of these different "velocities"?

In Vol. I, pp. 48-7, Feynman discusses this using the example of two waves moving in the same direction with slightly different velocities. He imagines riding on one wave's crest while looking at the crest of the other wave. He states, but does not demonstrate, that a slight change in one wave's phase can dramatically change the phase of the sum of both waves. Frankly, this discussion isn't very satisfying.

Phase, Group & Signal Velocities The balance of this section supplements the Feynman Lectures. Before getting into the mathematics, we describe here the essential differences between these three ways of characterizing wave velocity.

Signal velocity is the maximum speed at which information or particles can travel; it never exceeds c, the speed of light.

Phase velocity is the speed of a single-frequency wave, an idealization that almost never represents actual reality. Phase velocity is not restricted by special relativity.

Group velocity is the speed of a wave packet (described below) composed of multiple frequencies. In almost all cases, group velocity is less than c.

Let's consider some examples. Imagine a series of masses on springs, equally spaced along the x-axis, with each mass oscillating independently up and down in the y-direction, as shown in Figure 43-4.

Figure 43-4 Independent Oscillators Since the masses oscillate independently, we can make them oscillate in any manner we wish. Let's choose: y(x,t) = cos(ωt–kx)

At a fixed time t, some masses will be at their peak y. These are the masses for which: ωt – kx = 2nπ, for any integer n x = ωt/k – 2nπ/k There is no doubt that the equation for y(x,t) is a wave equation. As time progresses, we see the locations of peak mass heights move to the right at velocity ω/k.

We can choose the phase velocity ω/k to have any value, even 137c — much faster than light speed. But none of this violates special relativity. None of the masses are moving faster than c. No information is being transmitted faster than c, because the masses are not causally linked: no mass determines the motion of any other mass. The phase velocity describes the motion of a mathematically defined point, but that point has no physical significance.

A single frequency cannot transmit information because its form never changes; it is precisely predictable, completely unlike information. Indeed, a single-frequency wave can exist only if it fills all space and time. Single frequency waves are idealizations that help us understand complex phenomena, but they are as physically unrealistic as frictionless motion and perfectly reversible heat engines.

Real waves are wave packets composed of multiple frequencies, which we will shortly discuss. To transmit information we must modulate a wave, an example of which is shown in Figure 43-5.

Figure 43-5 Modulated Wave This modulated wave has the now familiar form: A = cos(ωt–kx) cos(Δωt–Δkx)

The phase velocity corresponds to the rapid oscillation due to the first cosine term. The group velocity corresponds to the slower waxing and waning of the amplitude, the envelope of the wave train, due to the second cosine term. The name "group velocity" arises because the envelope appears to divide the wave into groups, each containing many individual oscillations. The large central bulge in Figure 43-5 is one such group.

As this wave evolves over time, the rapid oscillations move from group to group. This is because the rapid oscillations move faster (at the phase velocity) than do the groups (at the group velocity).

In normal materials, the resonant frequencies Ω are much higher than optical frequencies. This means the index of refraction n is greater than 1 and increases very slowly with increasing frequency and wave number. All this makes the group velocity less than c, as shown below.

n = 1+ β/(Ω2–ω2)

n = 1+ β/{Ω2 (1–ω2/Ω2)} ≈ 1+ (β/Ω2)(1+ω2/Ω2)} dn/dω = 2ωβ/Ω4 ck = nω c dk/dω = ω dn/dω + n c dk/dω = 2ω2β/Ω4 + n Ω4/Ω4 v = dω/dk = c Ω4 / {2ω2β + nΩ4} For n > 1, v is definitely less than c.

However, there is a final caveat. Near the medium's resonant frequency Ω, the refractive index n may decrease with increasing frequency. This is called anomalous dispersion. From our studies of harmonic oscillators (Chapter 13), we know that damping factors (friction, radiation, and other energy dissipation) can become important in systems near resonance. Energy dissipation is highly frequency-dependent and distorts the wave shape, precluding a definitive definition of "velocity". In such cases, we must add the damping factor iµω to the denominator in the refractive index equation, as follows: n = 1+β/(Ω2–ω2+iµω)

dn/dω = –β(–2ω+iµ)/(Ω2–ω2+iµω)2 When ω is very near Ω: dn/dω = –β(2ω–iµ)/(µ2ω2)

Here, dn/dω can be negative and the group velocity may exceed the speed of light.

In very exotic synthetic materials, the group velocity can even be zero or negative.

ative. In all such cases, group velocity is no longer connected to real physical motion. These exotic materials demonstrate the extraordinary capabilities of modern materials technologies. Nonetheless, and despite provocative media headlines, it remains true that photons always travel at speed c and information does not propagate faster than light nor backwards in time. Experiments performed in 2012 show that, even in such exotic materials, no information and no particles travel faster than c.

Quantum Mechanics & Wave Packets

In quantum mechanics, each particle has a wavelength λ according to de Broglie’s equation: λ=h/p, where h is Planck’s constant and p is the particle’s momentum. Particles are represented by wave packets, which are sums of many waves of different wavelengths, as shown in Figure 43-6.

Figure 43-6 Wave Packet Representation of Particle

According to quantum theory, the particle wave packet is a probability amplitude. The probability of finding a particle at any specified location at any specified time is proportional to the square of the particle’s probability amplitude at that location and time. The probability amplitude ψ obeys a wave equation, and has the form: ψ = A exp{iωt–kx}

Quantum mechanics is the subject of Volume 3 of the Feynman Lectures, which we explore beginning with Feynman Simplified 3A. Here, we wish to determine how non-quantum relativistic particle kinematics relates to the quantum wave packet representation.

In non-quantum special relativity, the relationships between energy E, momentum p, rest mass m, and velocity v are: E = γmc², p = γmv, E² = p²c² + m²c⁴, where γ = 1/√(1–v²/c²)

In quantum mechanics, the relationships between energy, momentum, wave frequency ω, and wave number k are: E = ħω, p = ħk, where ħ (“h-bar”) is Planck’s constant divided by 2π.

Substituting the quantum equations for E and p into the relativistic equations yields: ħ²ω² = ħ²k²c² + m²c⁴, ω = c√(k² + m²c²/ħ²)

The last equation shows that for m>0, ω>ck, and the phase velocity ω/k is greater than c. Now calculate the group velocity. dω/dk = c (1/2) (2k) / √(k² + m²c²/ħ²), dω/dk = c k / √(k² + m²c²/ħ²). Since the denominator must be greater than k, the group velocity is always less than c. The denominator is in fact just ω/c. This leads to: dω/dk = c k / (ω/c), dω/dk = c² (p/ħ) / (E/ħ), dω/dk = c² p/E, dω/dk = c² (γmv) / (γmc²), dω/dk = v.

This confirms that the group velocity of the quantum wave representation equals the non-quantum relativistic velocity, as it must. Quantum theory must reduce to classical mechanics in the limit of large-scale phenomena, where ħ is negligible.

Waves in 1D

From the prior chapter, we discovered that the wave equation in one dimension is: ∂²D/∂x² = ∂²D/∂t² / v². For sound waves, D is the displacement of the medium, and v is the speed of sound. Light satisfies the same equation, with D replaced by the electric field and v replaced by c.

For sound waves, pressure P and density ρ also satisfy the same equation, which we now demonstrate. Recall these key equations from the last chapter: ρ = ρ₀ + dρ, with dρ << ρ₀; P = P₀ + dP, dP << P₀. {Eqn. 1}: dρ = – ρ₀ ∂D/∂x. {Eqn. 2}: dP = κ dρ, near equilibrium. {Eqn. 3}: ∂P/∂x = – ρ₀ ∂²D/∂t².

Take the partial derivative with respect to x of the wave equation: ∂²(∂D/∂x)/∂x² = ∂²(∂D/∂x)/∂t² / v². From {Eqn. 1}, replace ∂D/∂x: ∂²(–dρ/ρ₀)/∂x² = ∂²(–dρ/ρ₀)/∂t² / v², ∂²(dρ)/∂x² = ∂²(dρ)/∂t² / v², ∂²(ρ)/∂x² = ∂²(ρ)/∂t² / v². From {Eqn. 2} and the next to last equation: ∂²(dP/κ)/∂x² = ∂²(dP/κ)/∂t² / v², ∂²(P)/∂x² = ∂²(P)/∂t² / v².

Waves in 3D

To generalize our wave equation to three dimensions of space, we just replace kx with k•r: k•r = kₓx + k_y y + k_z z, k² = k•k, ω = kv. In V1p48-9, Feynman says we could re-derive the wave equation in three dimensions by analyzing pressure gradients, density gradients, and displacements in 3D. Instead, he only quotes the final result. We derive the 3D wave equation as follows. A = exp{i(ωt–k•r)}, ∂A/∂t = iω exp{i(ωt–k•r)}, ∂²A/∂t² = –ω² A, ∂A/∂x = –ikₓ A, ∂²A/∂x² = –kₓ² A, ∂²A/∂y² = –k_y² A, ∂²A/∂z² = –k_z² A. Substituting these into: ω² / v² = k² = kₓ² + k_y² + k_z², yields: (–1/Av²) ∂²A/∂t² = (–1/A) ∂²A/∂x² + (–1/A) ∂²A/∂y² + (–1/A) ∂²A/∂z², which reduces to the wave equation in three spatial dimensions. ∂²A/∂t² / v² = ∂²A/∂x² + ∂²A/∂y² + ∂²A/∂z².

In the last section, we derived this equation of quantum mechanics: ħ²ω² = ħ²k²c² + m²c⁴. We can now replace ω² and k² with the above second order partial derivatives, and obtain: ∂²ψ/∂x² + ∂²ψ/∂y² + ∂²ψ/∂z² – ∂²ψ/∂t²/c² = (ψ m²c²/ħ²). Here, ψ is a particle’s probability amplitude. Feynman says this is: “the great equation of quantum mechanics for a free particle.” He emphasizes the relativistic character of the equation, with the four dimensions of spacetime appearing in the canonical invariant form: ∂x² + ∂y² + ∂z² – ∂t²/c². And like all wave equations, this one is linear in ψ, consistent with the principle of linear superposition.

Two Coupled Pendulums

In V1p48-10, Feynman says the phenomenon “拍频现象相当奇特且有些与众不同。” 考虑两个由弹簧连接的单摆。它们的长度完全相同，因此摆动周期也相同。摆球质量相等，但如图43-7所示，为便于观察，左侧摆球画得更大。

图43-7 由弹簧连接的单摆两个单摆最初都静止。在t=0时，右侧单摆开始运动，前后摆动，方向垂直于屏幕（朝向和远离你）。当它摆动时，会拉伸弹簧，从而对最初静止的左侧单摆施加力。由于两个单摆的固有振荡频率相同，左侧单摆正以其固有频率被驱动，导致其振荡幅度不断增大。

随着时间推移，能量从右侧摆球转移到左侧摆球。最终，在其所有初始能量都转移到左侧摆球后，右侧摆球完全停止。然后过程反向进行，由左侧摆球驱动并将能量转移给右侧摆球。最终，左侧摆球也静止。若无摩擦，整个过程将无限循环重复。

这个有趣的现象如何与拍频理论相关联？

单独观察每个摆球，它们以某个频率快速振荡，其幅度则随时间以较慢的频率起伏变化——这正是我们现已完全理解的拍频现象。每个摆球的运动是两个频率略有不同的运动的叠加，其形式为： cos(ω₁t) + cos(ω₂t) = 2 cos[ωt] cos[Δωt]

其中 ω = (ω₁+ω₂)/2 Δω = (ω₁–ω₂)/2 费曼做出了如下重要观察： “因此，应该有可能在这个系统中找到另外两种运动，并声称我们所看到的是这两种解[另外两种运动]的叠加，因为这是一个线性系统。确实很容易找到两种启动运动的方式，每一种都是完美的单频运动——绝对周期性的。” 这两种定态解如图43-8所示。这里我们从边缘角度（相对于图43-7旋转90度）观察单摆。在图左侧，两个单摆一起摆动；而在右侧，它们彼此反向摆动。

图43-8 耦合单摆的定态模式左侧所示运动的数学形式为： {左}：A_W = A_B = cos(ω₁t)

其中A_W是白色摆球的振幅，A_B是黑色摆球的振幅。此时弹簧不受力，因此两个摆球互不施力。两者都以其固有频率振荡。

右侧所示运动的数学形式为： {右}：A_W = –A_B = cos(ω₂t)

此时，当摆球反向摆动时，弹簧会伸缩；每个摆球都拉扯对方。这增加了单摆的恢复力，从而提高了振荡频率。因此ω₂ > ω₁。

将这两个定态解相加，就得到了我们最初描述的那种能量逐渐从一个摆球转移到另一个摆球的运动。

{左} + {右}：cos(ω₁t) + cos(ω₂t)

因此，我们有两种分析这个有趣现象的方法：(1) 使用两个频率之间的拍频理论；(2) 对不同频率的定态解求和。

## 第43章回顾：核心思想

## 1. 当两个不同频率的波叠加时，合成波可表示为：

cos(ω₁t) + cos(ω₂t) = 2 cos(ωt) cos(Δωt)

其中 ω = (ω₁+ω₂)/2，Δω = (ω₁–ω₂)/2 合成波的强度I为： I = 1 + cos(2Δωt)

当初始波频率相近时（Δω << ω），合成波以频率ω快速振荡，同时其幅度以频率2Δω缓慢起伏，该频率称为拍频。

## 2. 在折射率为n的材料中，

n = 1 + β/(Ω² – ω² + iµω)

其中β为正数常量，Ω为材料共振频率，µ为阻尼因子。当µ和Ω可忽略时，n ≈ 1 – β/ω²，且dn/dω > 0。此时n < 1，并且： 相速度 = ω/k = c/n = c/(1–β/ω²) > c。

但是， 群速度 = dω/dk = c/(1+β/ω²) < c。

当ω ≈ Ω且能量耗散显著时，µ较大，dn/dω可能为负。此时群速度可能大于c。然而，任何信号或粒子都不会超过光速c。

## 3. 三维波动方程为：

∂²A/∂t² / v² = ∂²A/∂x² + ∂²A/∂y² + ∂²A/∂z²

## 4. 量子力学中粒子概率幅ψ的波动方程为：

∂²ψ/∂x² + ∂²ψ/∂y² + ∂²ψ/∂z² – (1/c²)∂²ψ/∂t² = ψ m²c²/ħ²

## 5. 由弹簧连接的两个单摆具有两种定态模式，对应两个不同频率。若初始时一个单摆静止而另一个在运动，则能量会根据拍频理论的方程，逐渐在两个单摆之间来回转移。

## 第44章

振动模式在V1p49-1中，费曼以这样一句引人注目的话开启了关于振动模式的章节： “本章将探讨一些由振动模式产生的重要现象” of confining waves in some finite region. We will be led first to discover a few particular facts about vibrating strings, for example, and the generalization of these facts will give us a principle which is probably the most far-reaching principle of mathematical physics.”

Wave Reflection In one dimension, the wave equation is: ∂2y/∂x2 = ∂2y/∂t2 / v2 Here y is the displacement (wave height), x is the horizontal position, t is time, and v is the wave velocity. Since the only occurrence of v in this equation is v2, the equation is equally satisfied by waves with both positive and negative velocities. Thus the general solution to the 1D wave equation is: y(x,t) = f(x–vt) + g(x+vt)

Here f and g are any functions that satisfy the wave equation, f represents a wave moving in the +x direction, and g represents a wave moving in the –x direction.

Now consider a string of uniform density and tension that extends from x=0 to x=+∞. The string is tied to a solid wall at x=y=0, but is free to move everywhere else. This means y(0,t) must equal 0 for all t, which requires: y(0,t) = 0 = f(0–vt) + g(0+vt)

g(+vt) = – f(–vt)

Since the last equation is valid for all t, it must be true that: g(ξ) = –f(–ξ) for all ξ In particular: g(x+vt) = –f(–x–vt)

Plugging this into our general wave solution, we get the following equation for this string: y(x,t) = f(x–vt) – f(–x–vt)

In V1p49-1, Feynman suggests we think of this expression representing two waves moving in opposite directions. Figure 44-1 displays the time evolution of two waves corresponding to the two terms in the above equation, with the upper wave moving toward –x and the lower wave moving toward +x. The shaded region represents the wall; so all the action at negative x is entirely imagined.

Figure 44-1 Time Evolution of Two Waves with Opposite Velocity and Polarity The sum of the upper and lower waves is always zero at x=0, consistent with the string being tied at x=y=0. This two-opposite-wave solution guarantees y(0,t)=0, whether or not the string is actually tied down.

Figure 44-1 shows the key result: a wave that starts at positive x and moves toward –x. It is reflected and inverted at its fixed end — the polarity of its velocity and displacement are both reversed.

Reflection of Sine Waves Next consider periodic waves, which we will represent with complex numbers.

f(x–vt) = exp{iω(t–x/v)} f(–x–vt) = exp{iω(t+x/v)} y(x,t) = exp{iω(t–x/v)} – exp{iω(t+x/v)} y(x,t) = exp{iωt} [exp{–iωx/v} – exp{+iωx/v}]

y(x,t) = exp{iωt} (–2i) sin(ωx/v)

Don’t worry about the (–2i); we could get rid of that by adding a complex constant to the exponent. As usual, the physical solutions we seek are the real parts of our complex equations. If we are not concerned with the initial phase angle, we can write the solution as: y(x,t) = A cos(ωt) sin(ωx/v)

Here A is any constant. This result has several remarkable features.

At any specific time t, the shape of the string is a sine function. Whenever ωt = nπ, for any integer n, y(x,t)=0 for all x, and the string displacement is zero everywhere. Additionally, at every point along the x-axis, the wave oscillates at frequency ω. The amplitude of oscillation varies with x, but the frequency is the same everywhere. The string displacement is always zero where ωx/v=nπ, for any integer n. These values of x are called nodes. The wavelength equals twice the distance between adjacent nodes (like any sine function), which is given by: λ = 2π v / ω This type of motion, in which all points move sinusoidally with the same frequency and phase, but with possibly different amplitudes, is called a mode. Having the same phase means every point passes through zero displacement at the same time.

Waves of Finite Length Next consider a string of length L that is fixed at both ends so that: y(0,t) = y(L,t) = 0 for all times t.

For a finite length string fixed at both ends, all displacement waves are reflected and inverted at each end, as illustrated in Figure 44-2. This follows from the same logic we used for a string that extends from x=0 to x=+∞.

Figure 44-2 Reflections from String Ends

At any specific point x along the string, the displacement is a periodic function as the wave bounces back and forth at the string’s fixed ends. Figure 44-3 illustrates this for a point near the left end of the string.

Figure 44-3 Displacement vs. Time at any Point In this figure, the earliest bump (smallest time t) occurs as the wave passes moving toward –x. After the wave is reflected and inverted at x=0, it causes the second bump as it moves toward +x. The third bump occurs after the wave reflects at x=L. This completes one cycle. The period between full cycles is 2L/v.

While the above function, y(t), is periodic, it clearly isn’t sinusoidal. In Chapter 14 we discovered the wonderful properties of linear differential equations, of which the wave equation is one example. We know that any linear combination of any solutions of a linear equation must also be a solution. Sinusoidal functi Sinusoidal solutions are solutions of the wave equation, and we learned that almost any function can be written as a linear combination of sinusoidal functions (a Fourier series or transform). It therefore makes sense to begin the analysis of a linear system by first finding all sinusoidal solutions. One can then describe all other solutions as linear sums of the sinusoidal solutions. Recalling that wave number k equals ω/v, the sinusoidal solutions have the form: y(x,t) = A exp{iωt} sin(kx)

While any k and any wavelength λ is a solution to an infinite string tied at one end, only certain values of ω and k yield solutions for a string of length L. Clearly, the requirement is: sin(kL) = 0 which requires: kL = nπ, for any integer n>0 In V1p49-3, Feynman says the most important characteristic of a wave confined to a finite space is that it can have only certain frequencies — certain modes. Here the allowed frequencies and wavelengths are: ω = kv = nvπ/L, for any integer n>0 λ = 2πv/ω = 2L/n Each value of n corresponds to one mode. Defining ωₙ and kₙ to be the frequency and wave number of mode n, any sum of the following form will be a solution for the motion of a finite string fixed at both ends: y(x,t) = Σ Aₙ exp{iωₙt+øₙ} sin(kₙx)

where Aₙ and øₙ are any selected amplitudes and phases. To match a complex waveform, the sum may need to extend to n=∞.

Note that each mode, by itself, represents a standing wave — the wave oscillates in amplitude, but its shape and position don’t change — the wave is stationary. Nonetheless, a sum of modes is generally not stationary since each mode has a different shape and oscillates at a different frequency.

Within the context of linear systems, Feynman adds: “No matter how complicated the system is, it always turns out that there are some patterns of motion which have a perfect sinusoidal time dependence, but with frequencies that are a property of the particular system and the nature of its boundaries.” “Any motion at all can be analyzed by assuming that it is the sum of the motions of all the different modes, combined with appropriate amplitudes and phases.” Modes in Two Dimensions Two-dimensional waves are more complex but also more interesting.

Feynman was an outstanding drummer, with a remarkable sense of rhythm. As I mentioned before, he could beat an 11-to-13 rhythm on the bongo drums (11 ω_LEFT = 13 ω_RIGHT, precisely). While knowing these aren’t typical musical instruments, in V1p49-3 he considers the modes of a rectangular drumhead.

Figure 44-4 shows a rectangular drumhead of length L and height H, which is fixed at its perimeter by a clamp that is shown in gray.

Figure 44-4 Rectangular Drumhead Fixed at Perimeter We can write the equation for a two-dimensional wave as: z(x,y,t) = A exp{iωt} exp{–ik_x x} exp{–ik_y y} Here, z is the vertical displacement of the drumhead, A is the amplitude, ω is frequency, and k_x and k_y are the x and y components of the wave number vector k.

Constraining the drumhead at its perimeter requires: z(0,y,t) = z(L,y,t) = 0 for all y and t z(x,0,t) = z(x,H,t) = 0 for all x and t We attack this problem using the same logic as with the one-dimensional string. To ensure no motion at x=0, we sum waves moving in opposite x-directions that always cancel one another at x=0. This effectively replaces the exponential factor exp{–ik_x x} with sin(k_x x) in the wave equation. (There is also a factor of –2i, which merely changes the definition of amplitude A).

To ensure no motion at x=L, we include only sine waves with nodes at x=L, which requires: sin(k_x L) = 0 k_x = nπ/L, for any integer n>0 We next repeat this process for the y-direction. This replaces the exponential factor exp{–ik_y y} with sin(k_y y) in the wave equation, and adds this requirement: sin(k_y H) = 0 k_y = mπ/H, for any integer m>0 These two equations yield the magnitude of the wave vector k: k•k = k² = k_x² + k_y² k² = π² (n²/L² + m²/H²)

From these possible values of k, we find the possible wavelengths and frequencies of all modes.

ωₙₘ = kv = vπ √(n²/L² + m²/H²)

λₙₘ = 2π/k = 2/√(n²/L² + m²/H²)

The shape of each possible mode has the form: Mₙₘ(x,y) = sin(nπx/L) sin(mπy/H)

Several modes of a drumhead with L=2H are illustrated in Figure 44-5, where the + and – signs indicate maximum and minimum values of Mₙₘ(x,y), and the dotted lines indicate the nodes, where Mₙₘ(x,y) is zero.

Figure 44-5 Sample Modes of Drumhead Any drumhead vibration can be represented as a linear sum of modes: z(x,y,t) = Σ Aₙₘ sin(ωₙₘ t+øₙₘ) Mₙₘ(x,y)

Again this summation can be extended to n=m=∞.

In V1p49-5, Feynman stresses the most important point of this analysis, noting that: “… the frequencies are not multiples of each other, nor are they multiples of any number. The idea that the natural frequencies are harmonically related is not generally true. It is not true for a system of more than one dimension, nor is it true for one-dimensional systems which are more complicated than a string with uniform density and tension.

a example of the latter is a hanging chain in which the tension is higher at the top than at the bottom. If such a chain is set in harmonic oscillation, there are various modes and frequencies, but the frequencies are not simple multiples of any number, nor are the mode shapes sinusoidal.

The modes of more complicated systems are still more elaborate. For example, inside the mouth we have a cavity above the vocal cords, and by moving the tongue and the lips, and so forth, we make an open-ended pipe or a closed-ended pipe of different diameters and shapes; it is a terribly complicated resonator, but it is a resonator nevertheless. Now when one talks with the vocal cords, they are made to produce some kind of tone. The tone is rather complicated and there are many sounds coming out, but the cavity of the mouth further modifies that tone because of the various resonant frequencies of the cavity. For instance, a singer can sing various vowels, a, or o, or oo, and so forth, at the same pitch, but they sound different because the various harmonics are in resonance in this cavity to different degrees. The very great importance of the resonant frequencies of a cavity in modifying the voice sounds can be demonstrated by a simple experiment. Since the speed of sound goes as the reciprocal of the square root of the density, the speed of sound may be varied by using different gases. If one uses helium instead of air, so that the density is lower, the speed of sound is much higher, and all the frequencies of a cavity will be raised. Consequently if one fills one’s lungs with helium before speaking, the character of his voice will be drastically altered even though the vocal cords may still be vibrating at the same frequency.” [He’ll sound like Donald Duck.]

Coupled Pendulums In this section, Feynman reexamines the coupled pendulums of the last chapter, and employs a mode-based analysis. As shown in Figure , two identical pendulums are connected by a spring. This time, they will swing right-to-left within the plane of the screen. Figure 44-6 Two Pendulums With Spring. While the string and drumhead have an infinite number of modes, these coupled pendulums have only two: their motions are either exactly the same, or exactly opposite. We will assume the x and y motions shown in the figure are much less than the pendulums’ length L. In this case, the restoring force is proportional to the horizontal displacement and we can treat this as a linear system. Without the spring, the equations for the right and left pendulums are: m dx2/dt2 = – m Ω2x m dy2/dt2 = – m Ω2y. Here, m is the pendulums’ mass, Ω is the pendulums’ natural frequency of oscillation, and the horizontal displacements from equilibrium are x for the right pendulum and y for the left pendulum. From Chapter 14, we know the equation for the natural frequency: Ω = √(g/L) where g is the acceleration of Earth’s gravity. We now add the spring, with spring constant k, which changes the restoring forces. If x>y, the spring stretches and exerts a force that pulls the pendulums together. If x<y, the spring compresses and exerts a force that pushes the pendulums apart. Those forces are described by the same equation F=k(x–y). The equations of motions are: m dx2/dt2 = – m Ω2x – k(x–y) m dy2/dt2 = – m Ω2y + k(x–y). By symmetry, both pendulums must oscillate at the same frequency (if not, which of the two identical pendulums oscillates faster?). Try a solution of the form: x = A exp{iωt} y = B exp{iωt}. Also by symmetry, the magnitudes of A and B must be equal, but their phases may be different. Substituting the trial solutions into the equations of motion yields: –mω2Aexp{iωt} = –mΩ2Aexp{iωt} –k(A–B)exp{iωt} –mω2Bexp{iωt} = –mΩ2Bexp{iωt} +k(A–B)exp{iωt} (ω2 – Ω2 – k/m) A = –B k/m (ω2 – Ω2 – k/m) B = –A k/m. Feynman notes that these equations appear to have two unknowns, A and B. But actually, these equations do not determine the magnitude of either A or B, but only their ratio. The two equations give the same ratio only for special values of ω. We can easily solve these equations by multiplying them together. (ω2 – Ω2 – k/m)2 AB = AB (k/m)2. If the pendulums are motionless (A=B=0), ω is meaningless. If either pendulum moves, so must the other, in which case AB is non-zero, and we get: (ω2 – Ω2 – k/m) = ± k/m ω2 = Ω2 + k/m ± k/m. The two solutions are: ω2 = Ω2 ω2 = Ω2 + 2k/m. Plugging these values into the equations of motion, we find that the first solution corresponds to both pendulums oscillating at their natural frequency (ω=Ω) with A=B — the pendulums swing together (x=y) with no force exerted by the spring. In this first solution, the spring could be removed without effect. The second solution corresponds to a higher frequency oscillation (ω>Ω) with A=–B and the spring playing an active role in driving the motion.

Comments on Linear Systems Feynman concludes, in V1p49-7, by describing the theory of linear systems as: “the most general and wonderful principle of mathematical ph Physics.

We have discussed this earlier, in Chapter 14, but it is worth repeating. Any physical system governed by a linear differential equation with constant coefficients can be solved with exponential functions. A differential equation is linear if the independent variable appears only to the first power. Having constant coefficients means the system characteristics (pendulum lengths, spring constants, etc.) don’t change over time. These exponential solutions may include sine and cosine functions, since these are exponentials with imaginary exponents. Any behavior of such systems, however complex, can be represented as a linear sum of exponential solutions.

For example, even if a system’s periodic motion is not sinusoidal, it may be represented by the sum of sinusoidal functions of various frequencies, amplitudes, and phases. The characteristics of the system will determine the types and combinations of sinusoidal functions that represent its motion.

Relation of Modes to Quantum Mechanics

Probability amplitudes play a central role in understanding quantum systems. For example, the square of the magnitude of an electron’s probability amplitude at (x,t) equals the probability that this electron will be found at position x at time t. Probability amplitudes are governed by linear differential equations and satisfy a wave equation. Additionally, quantum mechanics establishes a direct relationship between a particle’s energy and the wave frequency of its probability amplitude. Therefore, we can restate the principle of linear systems in terms of energy. In V1p49-8, Feynman says:

“A quantum-mechanical system, for example an atom, need not have a definite energy, just as a simple mechanical system does not have to have a definite frequency; but no matter how the system behaves, its behavior can always be represented as a superposition of states of definite energy. The energy of each state is a characteristic of the atom, and so is the pattern of amplitude which determines the probability of finding particles in different places. The general motion can be described by giving the amplitude of each of these different energy states. This is the origin of energy levels in quantum mechanics. Since quantum mechanics is represented by waves, in the circumstance in which the electron does not have enough energy to ultimately escape from the proton, they are confined waves. Like the confined waves of a string, there are definite frequencies for the solution of the wave equation for quantum mechanics. The quantum-mechanical interpretation is that these are definite energies. Therefore a quantum-mechanical system, because it is represented by waves, can have definite states of fixed energy; examples are the energy levels of various atoms.”

## Chapter 44 Review: Key Ideas

1.  Periodic motion in which all points move sinusoidally with the same frequency and phase, but with possibly different amplitudes, is called a mode. Having the same phase means every point passes through zero displacement at the same time. Locations at which the displacement is always zero are called nodes.

2.  A wave confined to a finite space, and constrained to have zero displacement at its boundaries, has only certain possible modes. In a 1D space of length L, the allowed frequencies and modes are: ω = nvπ/L, for any integer n>0 M(x) = sin(nπx/L)

Here v is the wave velocity. The most general equation of motion is: z(x,t) = Σ A sin(ωnt+øn) M(x)

n n n n n 3.  In a 2D space of length L and height H, the allowed frequencies and modes are: ωnm = vπ √(n2/L2+m2/H2), for integer n, m Mnm (x,y) = sin(nπx/L) sin(mπy/H)

The most general equation of motion is: z(x,y,t) = Σ Anm sin(ωnmt+ønm) Mnm (x,y)

nm nm nm nm nm

## 4.  Feynman says:

“No matter how complicated the system is, it always turns out that there are some patterns of motion which have a perfect sinusoidal time dependence, but with frequencies that are a property of the particular system and the nature of its boundaries.” “Any motion at all can be analyzed by assuming that it is the sum of the motions of all the different modes, combined with appropriate amplitudes and phases.”

## Chapter

Harmonics & Fourier Analysis

Harmony in Music

In V1p50-1, Feynman begins the lecture on harmonics with a tale about Pythagoras of Samos, believed to have lived from 570 to 495 B.C. Pythagoras is best known for his theorem on right triangles. He is also credited with discovering that there are only five Platonic solids, polyhedrons whose faces are all congruent regular polygons; these have 4, 6, 8, 12, and 20 faces.

But of particular interest to harmonics is Pythagoras’ discovery that, as Feynman says, “two similar strings under the same tension and differing only in length, when sounded together give an effect that is pleasant to the ear if the lengths of the strings are in the ratio of two small integers.” For example, a 2:1 ratio corresponds to a musical octave and a 2:3 ratio is called a fifth.

Feynman continues with a long but com pelling philosophical discussion: “Pythagoras was so impressed by this discovery that he made it the basis of a school…which held mystic beliefs in the great powers of numbers. It was believed that something similar would be found out about the planets—or “spheres.” We sometimes hear the expression: “the music of the spheres.” The idea was that there would be some numerical relationships between the orbits of the planets or between other things in nature. People usually think that this is just a kind of superstition held by the Greeks. But is it so different from our own scientific interest in quantitative relationships? Pythagoras’ discovery was the first example, outside geometry, of any numerical relationship in nature. It must have been very surprising to suddenly discover that there was a fact of nature that involved a simple numerical relationship. Simple measurements of lengths gave a prediction about something which had no apparent connection to geometry—the production of pleasant sounds. This discovery led to the extension that perhaps a good tool for understanding nature would be arithmetic and mathematical analysis. The results of modern science justify that point of view.” “Pythagoras could only have made his discovery by making an experimental observation. Yet this important aspect does not seem to have impressed him. If it had, physics might have had a much earlier start. (It is always easy to look back at what someone else has done and to decide what he should have done!)” “We might remark on a third aspect of this very interesting discovery: that the discovery had to do with two notes that sound pleasant to the ear. We may question whether we are any better off than Pythagoras in understanding why only certain sounds are pleasant to our ear. The general theory of aesthetics is probably no further advanced now than in the time of Pythagoras. In this one discovery of the Greeks, there are the three aspects: experiment, mathematical relationships, and aesthetics. Physics has made great progress on only the first two parts. This chapter will deal with our present-day understanding of the discovery of Pythagoras.” Musical notes, the ones we consider harmonious, have repetitive waveforms. An example is shown in the upper half of Figure 45-1.

Figure 45-1 A Musical Note (Above) vs. Noise By comparison, random vibrations of air molecules hitting our ears produce the unpleasant sensation we call noise, which is shown in the lower half of the figure.

A pleasant musical note is much more complex than a simple sine wave, which may be as unpleasant as noise.

Feynman says musicians characterize musical tones in terms of loudness, pitch, and quality.

Loudness simply corresponds to the amplitude of the sound wave, the magnitude of pressure changes that we measure in decibels. Pitch corresponds to frequency, the rate of repetition of the most basic pattern of the musical tone. Quality corresponds to the complexity of the waveform, which corresponds to the multiplicity of frequencies from which the waveform is composed.

As Feynman says in V1p50-2: “An oboe, a violin, or a soprano are still distinguishable even when they sound notes of the same pitch.” This is due to differences in the contributions of frequencies other than the basic frequency – due to differences in harmonics.

Consider a plucked string. From the last chapter, we know that strings have infinitely many possible vibrational modes. Depending on how it is plucked, some combination of modes becomes active. The oscillation due to each mode travels toward each end of the string, reflects at each end, and continues bouncing back and forth, while slowly diminishing due to energy losses.

But importantly, the oscillations of each mode repeat with the same period: T=2L/v. This is because the wave velocity v is determined solely by the string density and tension; hence, v is the same for all modes. The period T=2L/v is simply the time required for a wave of velocity v to: (1) travel from any starting point to either end; (2) reflect and travel to the opposite end; and finally (3) reflect at that end and return to the starting point. However complex the waveform, it must repeat making the same sound pattern with a period of T=2L/v.

Fourier Series As we have often said, any physically realistic waveform, however complex, can be represented by a linear sum of sinusoidal functions. Let’s now discover the mathematical procedure by which this is accomplished: the Fourier series.

In the last chapter, we found the following equations for a one-dimensional vibrating string of length L, with wave velocity v: ω = nvπ/L, for any integer n>0 f(x,t) = Σ A sin(ωt+ø) sin(nπx/L)

n n n n We noted that any string displacement function f(x,t), however complex, can be represented by the above sum.

Let us now restrict our attention to one value of x and consider f(t) at that x. The factor sin(nπx/L) is then constant, and can be absorbed into the A‘s. Let’s also define ω=vπ/L, w which is the frequency at which all modes repeat: ω=2π/T=2π/(2L/v). The most general waveform is then represented by: f(t) = Σ A_n sin(nωt+ø_n)

Alternatively, we can replace the phase angles ø_n with cosine functions, by using: sin(nωt+ø_n) = sin(nωt) cos(ø_n) + sin(ø_n) cos(nωt)

Cos(ø_n) and sin(ø_n) are constants that can be absorbed into the coefficients of sin(nωt) and cos(nωt). This provides another expression for the most general waveform: f(t) = Σ { a_n cos(nωt) + b_n sin(nωt) }

The above expression is called the Fourier series for f(t), a function that repeats with frequency ω. In musical terms, the n=1 term is called the first harmonic, n=2 is the second harmonic, etc. Waves are almost always expressed with an average value of zero, such as sin(x), but the above sums can accommodate waves with offsets, such as 1+sin(x), by including an n=0 term, which is simply the constant a_0.

Figure 45-2 shows how increasing the number of terms in a Fourier series better approximates a square wave. A true square wave is shown in Figure 45-3.

Figure 45-2 Fourier Series Fit To Square Wave Upper Left: f(ωt) and f(3ωt)

Lower Left: f(5ωt) and Fit with n=1,3 Upper Right: Fit with n=1,3,5 Lower Right: Fit with n=1,3,5,7

Musical Quality & Consonance Fourier series help us describe the musical concepts of quality and consonance. Even when the tones from a violin and an oboe have the same pitch (the same ω), the differing characteristics of these instruments produce sounds with differing harmonic contributions — differing coefficients in their Fourier series representations. Musicians say violins and oboes have different tone qualities. Sounds that contain only one harmonic are called pure tones. Sounds composed of many strong harmonics are called rich tones.

In V1p50-3, Feynman explains that electric organs have keys that select pitch and stops that control the contributions of higher harmonics. With different stops, an electric organ can approximate the sound of a flute, an oboe, or a violin. I say “approximate” because electric organs don’t have a Stradivarius stop, at least so far. Feynman notes that our ears detect the intensity of sound at various frequencies, but not the phase differences — human hearing is not sensitive to phase angles, the ø in the above equations. Therefore instruments such as electric organs need only generate either sin(nωt) or cos(nωt) but not both. Other applications are more demanding, requiring both the sine and cosine of each frequency in the Fourier series.

It is also interesting that we distinguish vowels, such as “a” and “e”, by the quality of their sounds, their harmonic compositions. We produce the different vowel sounds by changing the shape of our mouths to change the contribution of various harmonics. Feynman notes that the shape of our mouths emphasize certain specific frequencies, and that these frequencies do not change when our vocal cords produce a different pitch. Thus, tone quality, the ratios of various frequencies, of a spoken “e” changes at different pitches (different ω’s). We seem to distinguish vowels more by specific frequencies rather than frequency ratios.

In V1p50-4, Feynman returns to Pythagoras’ discovery that two strings produce a pleasant sound when their lengths are in the ratio of two small integers. Perhaps we can now understand why this is so. Each string produces sounds at several harmonics: ω, 2ω, 3ω, …. If the strings have a length ratio of 3:2, for example, they produce sounds at these frequencies: L=3: modes at (vπ/3) × (1, 2, 3, …)

L=2: modes at (vπ/2) × (1, 2, 3, …)

Note that the third harmonic of the L=3 string matches the second harmonic of the L=2 string; both have frequencies of vπ. When the higher harmonics match, beats are eliminated. Recall from Chapter 43 the equation for the intensity I of the sum of two waves of frequencies ω_1 and ω_2: cos(ω_1 t) + cos(ω_2 t) = 2 cos(ω t) cos(Δω t)

with ω = (ω_1+ω_2)/2 and Δω=(ω_1–ω_2)/2 I = 1 + cos(2Δω t)

Here 2Δω is the beat frequency, the frequency at which the sound slowly waxes and wanes. If the two frequencies are exactly equal, Δω=0, we hear a pure tone without beats. But if the two frequencies are close but unequal, we hear an annoying beat: OOOoooOOOooo.

A small-number ratio eliminates annoying higher harmonic beats, making the sound more pleasant. This is called consonance. When string lengths differ from a small-number ratio, their combined sound has beats and is called dissonant. Stringed instruments can be accurately tuned by adjusting string tension until beats vanish.

Using a piano as an example, Feynman offers a charming illustration of harmonic consonance. Let's label three successive C’s near the middle of the keyboard as C, C*, and C** and similarly the three next higher G’s as G, G*, and G**. Recall that frequencies double for each octave. The frequencies of these keys are in these ratios: C, C*, C** : 2, 4, 8 G, G*, G**: 3, 6, 12 Feynman says: “press C* slowly—so that it does not sound but We cause the damper to be lifted. If we then sound C, it will produce its own fundamental [the frequency 2 above] and some second harmonic [4]. The second harmonic will set the strings of C* into vibration. If we now release C (keeping C* pressed) the damper will stop the vibration of the C strings, and we can hear (softly) the note C* as it dies away. In a similar way, the third harmonic of C [3×2=6] can cause a vibration of G* [6]. Or the sixth of C [6×2=12] (now getting much weaker) can set up a vibration in the fundamental of G** [12].

“A somewhat different result is obtained if we press G quietly and then sound C*. The third harmonic of C* [3×4=12] will correspond to the fourth harmonic of G [4×3=12], so only the fourth harmonic of G will be excited. We can hear (if we listen closely) the sound of G** which is two octaves above the G we have pressed! It is easy to think up many more combinations for this game.”

He notes that the major scale has three major chords (FAC, CEG, and GBD) that are each in the frequency ratio 4:5:6. That fact, plus the doubling of frequency in each octave, fully defines the “ideal” scale called just intonation. For practical reasons, Feynman says keyboard instruments are not tuned this way, but are tempered with 12 equal frequency ratios of 1: 2^(1/12) ≈ 1:1.0595. A fifth is no longer in the ratio 3:2 but rather 2^(7/12) ≈ 1.4983; apparently, that’s close enough for most of us. Near middle C, that corresponds to a beat frequency of 1 cycle per 2.2 seconds. Since most musical notes have shorter durations, most of us don’t hear the beats.

Calculating Fourier Coefficients

Fourier analysis is a powerful tool for linear systems because any periodic function f is a sum of sine and cosine functions, with some set of Fourier coefficients. We can often solve difficult equations for the special case of simple sinusoidal functions. The solution for the complex function f is then simply the sum of the sinusoidal solutions, with the appropriate Fourier coefficients.

All we need is a procedure to compute the Fourier coefficients. Not surprisingly, the person who developed this procedure was Jean-Baptiste Joseph Fourier.

Consider again the Fourier series: f(t) = Σ { a_n cos(nωt) + b_n sin(nωt) }

Integrate f(t) over one full period T = 2π/ω. The integral of sine and cosine over a full cycle is zero. Hence only the cosine part of the n=0 term remains on the right hand side after integration.

∫_T f(t) dt = ∫_T a_0 cos(0) dt = T a_0 a_0 = (1/T) ∫_T f(t) dt

Fourier discovered that calculating the other coefficients isn’t much harder. Multiply the Fourier series by cos(jωt) for some integer j>0, and then integrate over T:

∫_T f(t) cos(jωt) dt = Σ_n { ∫_T a_n cos(nωt) cos(jωt) dt } + Σ_n { ∫_T b_n sin(nωt) cos(jωt) dt }

Note that: 2 cos(nωt) cos(jωt) = cos([n+j]ωt) + cos([n–j]ωt)

2 sin(nωt) cos(jωt) = sin([n+j]ωt) + sin([n–j]ωt)

2 sin(nωt) sin(jωt) = cos([n–j]ωt) – cos([n+j]ωt)

We will use the first two equations now and the third equation later. Each term on the right side of each equation is a sinusoidal function of frequency mω, for m either n+j or n–j. If m is non-zero, the integral over period T of either sine or cosine is zero. Therefore we have shown that after integrating from t=0 to t=T=2π/ω:

∫ cos(nωt) cos(jωt) dt = T/2 if n=j, else = 0 ∫ sin(nωt) cos(jωt) dt = 0 for any n,j ∫ sin(nωt) sin(jωt) dt = T/2 if n=j, else = 0

The prior integral becomes:

∫_T f(t) cos(jωt) dt = ∫_T a_j cos(jωt) cos(jωt) dt = a_j T/2 a_j = (2/T) ∫_T f(t) cos(jωt) dt

We can repeat this logic multiplying f(t) by sin(jωt), and integrating over T. The result is: b_j = (2/T) ∫_T f(t) sin(jωt) dt

We have been very successful analyzing many repetitive motion problems using exponentials with complex exponents. We can employ that technique here as well and rewrite the Fourier equations as:

f(t) = Real part of Σ { z_n exp(inωt) }, with z_n = a_n + ib_n = (2/T) ∫_T f(t) exp(–inωt) dt, for n≥1 z_0 = a_0 = (1/T) ∫_T f(t) dt, and b_0 = 0

Fourier Series of Square Wave

Feynman next examines the simple example of the Fourier series for a square wave. Let the square wave be a periodic function, repeating with period T and defined by: f(t) = +1 for 0 ≤ t < T/2 f(t) = –1 for T/2 ≤ t < T f(t+T) = f(t) for any t

The square wave function is shown in Figure 45-3.

Figure 45-3. Square Wave Function

Clearly a_0, the average value of f(t), is zero. To compute the other coefficients, we must separate each integral into two parts: (1) the integral from t=0 to t=T/2, where f(t)=1; and (2) the integral from t=T/2 to t=T, where f(t)=–1. Recall ωT=2π.

a_j = (2/T) { ∫_1 cos(jωt) dt – ∫_2 cos(jωt) dt } b_j = (2/T) { ∫_1 sin(jωt) dt – ∫_2 sin(jωt) dt }

a_j = (2/Tjω) { sin(jωT/2) – 0 – sin(jωT) + sin(jωT/2) } b_j = (2/Tjω) {–cos(jωT/2)+1 + cos(jωT)–cos(jωT/2) }

a_j = (1/jπ) { 2sin(jπ) – sin(j2π) } b_j = (1/jπ) { 1 –2cos(jπ) + cos(j2π) }

a_j = (1/jπ) { 0 – 0 } b_j = (1/jπ) { 2 –2cos(jπ) }

a_j = 0 for all j b_j = 0 for j even b_j = (4/jπ) for j odd t(t) = (4/π) {sin(ωt) + sin(3ωt)/3 + sin(5ωt)/5 + … } Feynman shows that we can obtain an equation for the sum of an interesting infinite series by setting ωt=π/2.

f(T/4) = +1 = (4/π) {1 –1/3 + 1/5 –1/7 + … } Feynman also notes that the Fourier series of a square wave cannot exactly match the square wave at its discontinuity (t=T/2 in this case). Here we find: f(T/2) = (4/π) {sin(π) + sin(3π)/3 + sin(5π)/5 + …} = 0 The Fourier series yields the value half way between the square wave’s value at t<T/2 and t>T/2. This seems reasonable. Natural phenomena are almost never discontinuous. Any physically realistic function that goes from +1 to –1 must pass through zero.

Fourier Transform of Gaussian Feynman doesn’t do this, but let’s find the Fourier representation of a Gaussian distribution. Gaussians are very important because many natural phenomena follow such distributions. The equation for a Gaussian distribution, G(x), centered at x=0, with standard deviation σ (mean square variance = σ²), is: G(x) = exp{–x²/2σ²} / √(2πσ²)

Rather than compute the Fourier series, which is a sum of discrete frequencies, we will instead perform a Fourier transform that is an integral over all frequencies. The Fourier series is most appropriate for waves confined to a finite space, whereas the Fourier transform corresponds to the limit when that space grows toward infinity. The Fourier transform, S(k), is a function of wave number k given by an integral over x, from x=–∞ to x=+∞: S(k) = ∫ f(x) exp{–ikx} dx / √(2π)

Here S(k) is the Fourier transform of function f(x). For a Gaussian: S(k) = ∫ exp{–x²/2σ² –ikx} dx / (2πσ)

This exponent isn’t the prettiest we’ve seen, but it is integrable with a neat trick called “completing the square.” We can make the exponent a perfect square by adding the right constant.

–(x/σ√2 + A)² = –x²/2σ² – 2xA/σ√2 – A² To complete the square we want: 2xA/σ√2 = ikx A = ikσ/√2 We can therefore rewrite the exponent as: –x²/2σ² –ikx = –(x/σ+ikσ)²/2 –k²σ²/2 The integral then becomes: S(k) = ∫ exp{–(x/σ+ikσ)²/2} exp{–k²σ²/2} dx / (2πσ)

We next substitute u = x/σ+ikσ, and du = dx/σ.

S(k) = exp{–k²σ²/2} ∫ exp{–u²/2} σdu / (2πσ)

S(k) = exp{–k²σ²/2} √(2π) / (2π)

S(k) = exp{–k²σ²/2} / √(2π)

We see that the Fourier transform of a Gaussian, G(x), is also a Gaussian, S(k). Also note that the standard deviation of G(x) is σ, while the standard deviation of S(k) is 1/σ.

For any Gaussian distribution, about 50% of the population is contained within 1/√2 standard deviations of the mean. In the context of a wave packet, we can view 1/√2 standard deviations as being the uncertainties Δx and Δk in the values of x and k, respectively. The product of these two uncertainties is: Δx Δk = (σ/√2) (1/σ√2) = 1/2 This analysis proves that reducing Δx increases Δk, and vice versa, demonstrating the unavoidable tradeoff between the uncertainty of a wave packet’s location and the uncertainty of its wave number. Since quantum mechanics equates momentum p with ħk, we have proven: Δx Δp = ħ/2, for Gaussian distributions which is the Heisenberg Uncertainty principle of quantum mechanics.

Fourier Series & Energy The energy carried by a wave is proportional to its amplitude squared. For a wave, f(t), that repeats with period T, the energy it carries is given by an integral over one full period T.

E ~ ∫ f(t)² dt If f(t) is represented by a Fourier series, with coefficients aₙ and bₙ, as above, we can expand the energy equation as follows: E ~ ∫ { Σₙ [aₙ cos(nωt) + bₙ sin(nωt)] }² dt E ~ ∫ { Σₙ [aₙ cos(nωt) + bₙ sin(nωt)] } × { Σⱼ [aⱼ cos(jωt) + bⱼ sin(jωt)] } dt Here, we have changed the summation index in the second { } to j. This allows us to rewrite the integrand as: Σₙⱼ [aₙ cos(nωt) aⱼ cos(jωt) + aₙ cos(nωt) bⱼ sin(jωt) + bₙ sin(nωt) aⱼ cos(jωt) + bₙ sin(nωt) bⱼ sin(jωt) ]

As shown earlier, when integrated over a full period T, cos(nωt) sin(jωt) is zero for all n and j. Also cos(nωt) cos(jωt), and sin(nωt) sin(jωt) are nonzero only when n=j. Eliminating these terms reduces the summation to: Σₙ [ aₙ² cos²(nωt) + bₙ² sin²(nωt) ]

Putting this back into the integral we get: E ~ ∫ { Σₙ [ aₙ² cos²(nωt) + bₙ² sin²(nωt) ] } dt For n=0, cos²(0)=1 and sin²(0)=0.

For n>0, cos²(nωt) and sin²(nωt) each average 1/2.

The result is: E ~ ∫ f(t)² dt = T a₀² + (T/2) Σₙ>0 [aₙ² + bₙ²]

In V1p50-8, Feynman calls this equation the energy theorem. It says a wave’s energy equals the sum of the energies of each of its Fourier components.

We can obtain the sum of another infinite series by applying this theorem to the Fourier series for a square wave, which we derived above. For a square wave, f(t)² is always 1.

∫ f(t)² dt = T = (T/2) (4/π)² {1+ 1/3² + 1/5² + 1/7² + … } Feynman says using the energy theorem on the Fourier series for f(t)=(t–T/2)² proves the equation for another infinite sum: π⁴/90 = 1 + 1/2⁴ + 1/3⁴ + 1/4⁴ + … Do you want to try to prove that? I provide the solution at the end of this chapter.

Nonlinear Systems So far, we 我们已经分析了一些被认为是线性的系统。这是一种理想化情况，对于许多现实世界中的系统，它可能只是近似正确。虽然最一般的非线性系统无法简单地分析，但我们可以从稍微非线性系统的有趣行为中获得一些洞见。

现在让我们考虑非线性响应的影响，例如电路中的电流与电压并不严格成正比的情况。

考虑一个设备，它接收输入 x(t) 并产生相应的响应 y(t)。例子包括产生电流 y 的电压 x，或者产生位移 y 的力 x。线性设备的 x 和 y 之间的关系具有以下形式： y(t) = K x(t)

这里的 K 是一个比例常数，它始终不变——对于所有的 x 和所有的 t 都相同。相比之下，在非线性设备中，关系可能具有以下形式： y(t) = K [x(t) + εx2(t)]

如果 ε 足够小，非线性项 εx2(t) 相对于 x(t) 来说很小。

考虑一个正弦输入 x 及其响应 y，如图 45-4 所示。

x(t) = cos(ωt)

y(t) = K[cos(ωt) + εcos2(ωt)]

图 45-4 线性响应（浅色）与非线性响应（深色）

如果 ε 为零，响应将是线性的，对应于图 45-4 中较浅的曲线。如果 ε 很小但大于零，响应则略有非线性，对应于较深的曲线。

我们可以利用恒等式 2cos2(θ) = 1–cos(2θ) 重写前面的方程。

y(t) = K cos(ωt) + Kε/2 – (Kε/2) cos(2ωt)

上面三项中的第一项是频率 ω 与输入 x 相同的正常线性响应。第二项给 y(t) 增加了一个常数偏移，移动了其平均值。整个响应曲线的这种移动被称为整流。

第三项给 y(t) 增加了一个更高频率的谐波。费曼指出，这是我们假设了与 x2 成正比的非线性，所以这个谐波是二次谐波（输入频率的两倍）。他说，与 x3 或 x4 成正比的非线性会分别增加三次和四次谐波。最一般的非线性会引入整个谐波频谱。

谐波的增加，以第三项为例，被称为调制，这是我们在第 43 章中研究过的过程。

现在考虑一个非线性设备对由两个不同频率和幅度的分量组成的输入的响应。

x(t) = A cos(ωt) + B cos(Ωt)

y(t) = K [x(t) + εx2(t)]

y(t) = K x(t) + Kε [A cos(ωt) + B cos(Ωt)]2 y(t) = K x(t) + Kε [A2cos2(ωt) + B2cos2(Ωt)]

+ 2KεAB cos(ωt) cos(Ωt)

方括号中的项与前面的例子相同；它产生二次谐波。在第 43 章中，我们经常处理包含不同频率余弦乘积的项，就像上面的最后一项。这些项会产生位于 ω 与 Ω 之和及差的频率上的边带余弦。进行熟悉的代换可得： y(t) = KA cos(ωt) + KB cos(Ωt) + (Kε/2) [A2+B2]

– (Kε/2) [A2cos(2ωt) + B2cos(2Ωt)]

+ KεAB {cos([ω+Ω]t) + cos([ω–Ω]t)} 这里我们得到了多种有趣效应的组合： 线性响应：KA cos(ωt) + KB cos(Ωt)

整流：(Kε/2) [A2+B2]

谐波：A2cos(2ωt) + B2cos(2Ωt)

边带：cos([ω+Ω]t) + cos([ω–Ω]t)

正如在第 43 章中，如果 ω≈Ω，边带包含一个频率约为 2ω 的项和另一个频率为 ω–Ω 的项。如果 ω>>Ω，两个边带的频率几乎相同。看待这个项的另一种完全等效的方式是考虑其先前形式：cos(ωt) cos(Ωt)。如果 ω≈Ω，正如我们在第 43 章中发现的，这个项会产生拍频。如果 ω>>Ω，我们可以说信号以频率 ω 振荡，同时被频率 Ω 缓慢调制。这两种描述都是完全正确的。

请注意，所有的非线性效应都与幅度的二次方成正比：A2、B2 或 AB。这意味着非线性效应对较大的输入更为重要，例如更强的电信号。

这些非线性效应——整流、谐波、调制、和差频——具有许多实际意义。

在 V1p50-9 中，费曼指出人耳被认为是有些非线性的。即使是单调的输入，非常响亮的声音也会给我们带来谐波以及和差频的感觉。此外，包括放大器和扬声器在内的音频组件也从来不是完全线性的。许多人认为这些非线性现象令人不快，以至于愿意为保真度更高（非线性更少）的设备支付更多费用。费曼指出，由于未知的原因，人们对自己耳朵的非线性的反感似乎不如对扬声器的非线性那么强烈。

最后，费曼回顾了我们之前对光引起电子振荡并发射辐射的研究，这些辐射与入射光干涉，导致了折射。他说我们假设电子对光的电场线性响应是一个非常好的近似，但并非完全准确。随着高功率激光器的发展，科学家们观察到了微小的非线性效应。通过玻璃的红色激光会产生微弱的蓝光，即二次谐 harmonic of red, due to electrons’ slightly nonlinear response.

Solution to Infinite Sum

Let’s find the Fourier series expansion for f(t)=t². Feynman suggested f(t)=(t–T/2)² but that’s needlessly messy; simply shifting the time axis gives us a cleaner equation. Since t² is an even function t²=(–t)², the Fourier series will not have any sine function contributions (b=0 for all n). The coefficients we need are: a₀ = (1/T) ∫_T f(t) dt aⱼ = (2/T) ∫_T f(t) cos(jωt) dt

The integrals cover the range t=–T/2 to t=+T/2.

a₀ = (1/T) ∫_T t² dt = t³ / (3T) evaluated at the limits a₀ = {T³/8 – [–T]³/8} / (3T) = T²/12

Next, calculate aⱼ: aⱼ = (2/T) ∫_T t² cos(jωt) dt

Make the substitution x=jωt. The integration limits become x=±jωT/2=±jπ.

aⱼ = (2/T) ∫_T x² cos(x) dx / (jω)³

We find the integral we need from tables (or you can derive this using integration by parts): ∫ x² cos(x) dx = 2x cos(x) + (x²–2) sin(x)

Evaluating this at the limits yields: 2 (jπ) cos(jπ) – 2 (–jπ) cos(–jπ)} + 0 = 4jπ (–1)ʲ

The final 0 in the first line arises from terms proportional to sin(jπ)=0. Note that cos(jπ) equals –1 when j is odd and +1 when j is even, which we have written as (–1)ʲ.

Plugging this into the equation for aⱼ gives us: aⱼ = (2/T) 4jπ (–1)ʲ / (jω)³ aⱼ = (2/T) (T/j2π)³ 4jπ (–1)ʲ aⱼ = (T/jπ)² (–1)ʲ

Finally, we use the energy theorem: ∫_T f(t)² dt = T a₀² + (T/2) Σ_{n>0} [aₙ² + bₙ²]

∫_T t⁴ dt = T (T²/12)² + (T/2) Σ_{n>0} [ (T/jπ)² (–1)ʲ ]² (1/5) {T⁵/32–[–T]⁵/32} = T⁵/144 + (T/2) Σ_{n>0} [ (T/jπ)⁴ ]

(1/5) = (1/9) + 8 Σ_{n>0} (1/jπ)⁴ 9/45 – 5/45 = 8 Σ_{n>0} (1/jπ)⁴ 1/90 = Σ_{n>0} (1/jπ)⁴ π⁴ / 90 = 1 + 1/2⁴ + 1/3⁴ + 1/4⁴ + …

## Chapter 45 Review: Key Ideas

In each section below, ∫ denotes integration over one full period T.

## 1. Musical tones are characterized in terms of loudness, pitch, and quality

Loudness is the amplitude of a sound wave Pitch is the frequency of a tone’s most basic pattern Quality corresponds to the multiplicity of frequencies from which a waveform is composed

## 2. The intensity I of the sum of two musical tones of frequencies ω₁ and ω₂ is:

I = 1 + cos(2Δωt)

Here 2Δω = ω₁–ω₂ is the beat frequency at which sound intensity slowly waxes and wanes.

When instrument string lengths have a small-number ratio, their harmonics match with Δω=0 and beats are eliminated, producing the pleasing effect called consonance. At other length ratios, the combined sound has beats and is called dissonant.

3. Any function f(t) that repeats with period T has a Fourier series representation that is a sum of sine and cosine functions.

f(t) = Σ_{n} { aₙ cos(nωt) + bₙ sin(nωt) } where T=2π/ω, and a₀ = (1/T) ∫_T f(t) dt b₀ = 0 aⱼ = (2/T) ∫_T f(t) cos(jωt) dt bⱼ = (2/T) ∫_T f(t) sin(jωt) dt

Here we have employed these relationships: ∫ cos(nωt) cos(jωt) dt = T/2 if n=j>0, else = 0 ∫ sin(nωt) cos(jωt) dt = 0 for any n,j ∫ sin(nωt) sin(jωt) dt = T/2 if n=j>0, else = 0

4. We can rewrite the Fourier equations using exponentials with complex exponents as: f(t) = Real part of Σ_{n} { zₙ exp(inωt) } zₙ = aₙ + i bₙ = (2/T) ∫_T f(t) exp(–inωt) dt, for n≥1 a₀ = (1/T) ∫_T f(t) dt, and b₀ = 0

## 5. Any function G(x) has a Fourier transform S(k) given by:

S(k) = ∫_{–∞}^{+∞} G(x) exp{–ikx} dx / √(2π)

If G(x) is a Gaussian distribution, S(k) will also be Gaussian: G(x) = exp{–x²/2σ²} / √(2πσ²)

S(k) = exp{–k²σ²/2} / √(2π)

The standard deviation of G(x) is σ, while the standard deviation of S(k) is 1/σ. Let Δx and Δk be the uncertainties in the values of x and k of a wave packet. Define these uncertainties to be the limits that include 50% of the population of each Gaussian distribution, and note that quantum mechanics equates momentum p with ħk. The resulting Δx and Δp satisfy the uncertainty principle: Δx Δp = ħ / 2.

6. The energy of a wave is proportional to its amplitude squared, averaged over a full period T, which equals the sum of the average amplitudes squared of the wave’s Fourier components.

E ~ (1/T) ∫_T f(t)² dt = a₀² + (1/2) Σ_{n>0} [aₙ² + bₙ²]

## 7. Fourier analysis helps evaluate some interesting infinite series:

π/4 = 1 –1/3 + 1/5 –1/7 + … π⁴/90 = 1 + 1/2⁴ + 1/3⁴ + 1/4⁴ + …

## Chapter

Complex Waves

In V1p51-1, Feynman says this lecture is about “some of the more complex phenomena associated with waves.” He adds that he will discuss these phenomena qualitatively rather than quantitatively because they are “too complicated to analyze in detail here.” Indeed this chapter contains fewer equations than normal.

Bow Waves

The first topic concerns waves created by a source moving faster than the wave velocity. Consider the example of a jet flying faster than the speed of sound in air. Let the jet’s velocity be v in the +x-direction. At each point P along the jet’s path, the jet compresses the air in front of it, creating a pressure wave that spreads outward in all directions at the speed of sound, c.

Figure 46-1 shows the crests of pressure waves emitted at equally spaced times. All such waves will be tangent to a common line, thus creating a bow wave, as we will demonstrate.

Figure 46-1 Jet (grey) Creating Bow Wave

An Intense Conical Wave With Half-Angle θ

The image in Figure 46-1 corresponds to time t=0, when the tip of the jet is at x=0. Consider the largest wave on the left side of the image. Define T to be the time that wave was emitted, and define X to be the position of the jet at time T; X is also the position of the wave’s emission point. Both T and X are negative quantities. From the jet’s velocity, we know that X=vT, which is the length of hypotenuse of the right triangle shown in the image with dotted lines. From the wave’s speed, we know that the radius of the largest wave equal Tc, which is the length of the side of the right triangle farthest from the jet. Therefore: sinθ = Tc/vT = c/v. We chose the left most wave as an example, but the same analysis applies to all other waves created by the jet at other times. Thus all wave crests are tangent to the same line at angle θ. They interfere constructively and produce a high intensity wavefront — a bow wave.

The figure shows a 2D cross-section. In all three dimensions, the bow wave is conical with θ being one-half the cone angle.

Recall that we assumed v>c, that the speed of the jet, v, is faster than the speed of sound, c. There is no bow wave if v<c.

Feynman notes that a bow wave is created whether or not the jet itself makes any sound — sound is created by the mere act of moving through air faster than the speed of sound. Figure 46-2 clearly illustrates a bow wave coming from a bullet. Bullets are not sources of sound in and of themselves; it is their high-speed passage through air that creates sound waves.

Figure 46-2 Shock Wave of a Bullet

The pressure wave created by the bullet causes changes in the refractive index of the air it passes through, changes that are captured photographically in this image. From the cone half-angle of about 50º, we can estimate the bullet’s velocity: sin(50º) = 0.77 = c/v, so v = 1.3 c ≈ 448 m/s = 1008 mph. Note however that the leading edge of the cone is slightly curved rather than sharply pointed. This results from the extreme magnitude of the air disturbance at the bullet’s leading edge. This is called a shock wave, which we will discuss shortly.

Cherenkov Radiation

Bow waves also arise when a particle moves faster than light in a refractive medium. As discussed in Chapter 34, in a material with refractive index n, the phase velocity of light is reduced to c/n. For glass, n~1.5 and c/n~2/3.

The velocities of cosmic rays or elementary particles produced by high-energy particle accelerators often approach c, the speed of light in vacuum. These particles can have a velocity v greater than the phase velocity of light in glass or other materials. In these circumstances, particles produce bow waves – light emitted with a cone half-angle given by sinθ = c/(nv). This bow wave light is called Cherenkov radiation.

Experimental high-energy physicists employ this effect to measure particle velocities from the angle of Cherenkov radiation: v = c/(nsinθ). Even without precisely measuring the cone half-angle, Cherenkov radiation can confirm the type of particle traversing a detector.

Let me describe how this works. Particle accelerators often produce secondary beams composed of many different types of particles. As a particle beam passes through a magnet, each particle turns an angle α that is inversely proportional to its momentum p: α=M/p, for some constant M determined by the magnet. Selecting only those particles that bend by a specific angle selects those with a specific momentum. If these particles subsequently pass through an appropriate refractive medium, some types of particles will produce Cherenkov radiation while others won’t. The presence or absence of Cherenkov radiation can identify the type of particle.

For example, consider particles of momentum 500 MeV/c traversing glass (c/n=0.67). Protons (mass 938 MeV/c^2) would have velocity 0.47c and would not produce Cherenkov radiation (c/(nv)=1.41, which isn’t the sine of any angle). Kaons (mass 494 MeV/c^2) would have velocity 0.71c (c/(nv)=0.94) and would produce Cherenkov radiation at θ=70º. Pions (mass 140 MeV/c^2) would have velocity 0.96c (c/(nv)=0.69) and would also produce Cherenkov radiation at θ=44º. A second Cherenkov detector with refractive index n=1.33 (water) would distinguish kaons (c/(nv)=1.06) from pions (c/(nv)=0.78).

Here we use these relativistic equations from Chapter 26 (m is rest mass): E^2 = m^2c^4 + p^2c^2, and E/(mc^2) = γ = 1/√{1–(v/c)^2}. To simplify the above discussion, I assumed a beam of particles that all had electric charge +1. The bending angle α due to a magnet is also proportional to the particle’s electric charge. Positively and negatively charged particles bend in opposite directions. This means an alpha particle (2 protons and 2 neutrons) of momentum 1000 MeV/c will bend by the same angle as a proton of momentum 500 MeV/c. Identifying particle types in high-energy interactions usually reli es on a combination of several different techniques.

Shock Waves

In Chapter 42, we derived the following equations for the speed of sound: c² = (dP/dρ)₀ = γP/ρ = γkT/m = ⟨v²⟩ (γ/3)

Here P is pressure, ρ is density, γ is the specific heat ratio, T is temperature, m is the average molecular mass, ⟨v²⟩ is the average of the molecular velocity squared, k is Boltzmann’s constant, and the notation (X)₀ means “X evaluated at equilibrium”. In this case, X is dP/dρ, the derivative of pressure with respect to density.

This equation shows that, in any specific medium, the speed of sound is simply proportional to the square root of γT. However, our derivation assumed an ideal gas and only small changes in gas properties, including temperature, pressure, and density. We also assumed sound wavelengths much larger than the molecular mean free path.

All those assumptions are reasonable for many types of sound. For speech, ΔP/P is only a part per million. However, when the source of sound is extremely energetic — a jet, a bullet, or a lightning bolt — pressure changes can be extreme, approaching ΔP≈P, and increasing the wave velocity by perhaps 20%. This is the condition we describe as a shock wave.

In cases of extreme pressure increase, gas behind the wavefront (the wave’s leading edge) is highly compressed relative to gas in front of the wavefront (the gas not yet disturbed). The adiabatically (no heat transfer) compressed gas becomes hotter, making the speed of sound higher behind the wavefront than it is in front of the wave.

Secondary sound waves, those created after the primary sound wave, propagate at higher speeds in the hotter gas behind the primary wavefront. These secondary sound waves will therefore tend to catch up to the primary wavefront. Figure 46-3 depicts three successive moments in time, during which two secondary wavefronts catch up to the primary wavefront at the left.

Figure 46-3 Two Secondary Waves Advance Toward Primary Wavefront As Seen At Three Successive Times

Secondary waves may be produced by parts of the high-speed object that are behind the leading edge, such as a jet’s wings and tail fins. Secondary waves may also be produced by air turbulence itself. This effect sharpens the wavefront and increases its amplitude, greatly increasing the pressure derivative. Most sounds we hear from distant sources build gradually, gently alerting us to something coming. However, in the case of shock waves, many smaller sound waves accumulate and arrive nearly simultaneously. There is no gentle warning before the sudden BOOM. Hence the term “shock.”

For extremely energetic events, shock waves form almost instantly. For lower intensity sounds, the sound wave may dissipate before the wavefront can sharpen appreciably.

In V1p51-3, Feynman explains that the curvature near the apex of a projectile, as seen near the bullet tip in Figure 46-2, can be understood in terms of pressure changes. The air pressure change is higher near the apex than it is off to the side. The speed of sound is therefore higher near the apex, making sinθ and θ larger.

Feynman adds that shock waves always travel faster than the normal speed of sound, the speed for lower intensity waves. Perhaps from personal experience, he says: “The sound wave from an atomic bomb explosion travels much faster than the speed of sound for a while, until it gets so far out that it is weakened to such an extent from spreading that the pressure bump is small compared with atmospheric pressure. The speed of the bump then approaches the speed of sound in the gas into which it is going. (Incidentally, it always turns out that the speed of the shock is higher than the speed of sound in the gas ahead, but is lower than the speed of sound in the gas behind. That is, impulses from the back will arrive at the front, but the front rides into the medium in which it is going faster than the normal speed of signals. So one cannot tell, acoustically, that the shock is coming until it is too late. The light from the bomb arrives first, but one cannot tell that the shock is coming until it arrives, because there is no sound signal coming ahead of it.)”

Waves In Solids

Solid materials support two types of waves: 1. longitudinal waves, also called compression waves; 2. transverse waves, also called shear waves.

Compression waves in solids are analogous to sound waves in air. When a solid is struck at point P, atoms near P are compressed, they push on neighboring atoms, sending a pressure wave outward from P throughout the solid.

Transverse or shearing waves occur only in solids, not in gases or liquids. When a solid is twisted or pushed at one end and then released, it reacts like a spring. It recoils toward its equilibrium state, overshoots, recoils back, and continues oscillating until its energy of motion dissipates. Ultimately the atoms of the solid return to their original positions. In V1p51-4, Feynman says this is the key property of solids that distinguish them from liquids.

fluids. If a liquid is similarly deformed and allowed to stabilize before being released, its atoms remain in their new locations and do not return to their original positions.

Perhaps more vividly, if you push on a block of Jello, it jiggles for a while and ultimately ends up as it started. If you move a spoon through a bowl of milk, then hold the spoon still for some time, and finally slowly remove the spoon, milk molecules will remain in their final position and will not snap back to their starting locations.

One similarity exists between shear waves in solids and light waves: the oscillation is perpendicular to the wave’s direction of motion.

In general, compression waves and shear waves travel through solids at different speeds. In all cases, the speed of longitudinal waves exceeds that of transverse waves. In a pure crystal, shear wave velocities vary depending on their orientation to the crystal axes.

For wavelengths much longer than the solid’s atomic spacing, wave speeds in solids do not vary substantially with wavelength. For very short wavelengths, the atomic spacing creates a dispersion effect, causing the velocity to vary with wavelength, or equivalently with wave number. The shortest possible transverse wave corresponds to neighboring atoms moving in opposite directions.

Feynman says: “The shortest wavelengths are so short that they are not usually [attainable in practice]. However they are of great interest because, in the theory of thermodynamics of a solid, the heat properties of a solid, for example specific heats, can be analyzed in terms of the properties of the short sound waves. Going to the extreme of sound waves of ever shorter wavelength, one necessarily comes to the individual motions of the atoms; the two things are the same ultimately.” Seismic waves traveling through Earth’s interior are particularly interesting examples of sound waves in solids. The most dramatic such waves are created by earthquakes. Seismic waves from an earthquake start at the focus, the origin of the quake, with wavelengths that are much longer than those we normally associate with sound. But they truly are sound waves, organized vibrations of atoms in the solid material within the Earth. (An earthquake’s epicenter is the point on Earth’s surface directly above the focus.)

The Earth is not homogeneous. Its pressure, temperature, density, compressibility, and other properties change with depth, and sometimes also with horizontal position. Longitudinal and transverse waves depend differently on the material properties, and therefore travel at different speeds and along different trajectories. Additionally, the speed of each type of seismic wave changes as it propagates, with the result that the waves do not travel in straight lines. The varying material properties are equivalent to changing indices of refraction, causing the waves to curve. Some of these complex trajectories are illustrated in Figure 46-4.

Figure 46-4 Map of Seismic Waves From Earthquake Due to these complexities, seismographs at different locations may record quite different waveforms, and each may record immensely complicated waveforms. Figure 46-5 shows seismographs along three axes from the devastating earthquake that hit Tohoku, Japan on April 7, 2011. The earthquake and subsequent 40m-high tsunami killed nearly 19,000 people and led to the meltdown of three reactors at the Fukushima nuclear power plant.

Figure 46-5 Seismographs of Motion in Three Axes for Tohoku, Japan, April 7 2011, Magnitude 9.0 Earthquake. Axes from Top to Bottom: Vertical, North-South, East-West One might well look at these seismographs and be convinced that none could ever hope to understand their complexity.

But quite remarkably, through comprehensive observation and diligent analysis, as Feynman says in V1p51-6: “The details have been worked out… We know what the speeds of various kinds of waves are at every depth. Knowing that, therefore, it is possible to figure out what the normal modes of the earth are, because we know the speed of propagation of sound waves—in other words, the elastic properties of both kinds of waves at every depth.” Seismology, the study of seismic waves, is our only means of probing Earth’s depths, and has enabled scientists to determine the basic internal structure of our planet. (Solar seismology has also illuminated the internal structure of the Sun.)

From the surface down, here is a brief description of Earth’s structure.

The Crust is 5 to 50 km (3 to 44 miles) thick and composed of various silicate rocks. Many of these rocks are less than 100 million years old, which indicates dynamic surface activity. But, a very few rocks are 4.4 billion years old, which indicates Earth has had a solid crust for at least that long.

The Upper Mantle extends to depth of 700 km (420 miles). It is composed of iron-rich silicate rocks that are ductile, able to flow over geological time scales.

The Lower Mantle extends to depth of 2900 km (1740 miles), maki The Upper Core is a shell about 2200 km (1300 miles) thick. It is composed of liquid iron and nickel with a density of about 11 g/cm³. Being liquid, the upper core (also called the outer core) does not support transverse sound waves. Motion of the liquid iron and nickel is credited with producing Earth’s magnetic field.

The Inner Core is a ball of radius 1220 km (730 miles), and is composed of iron (perhaps 80%) and nickel with a density of about 12.8 g/cm³. It is either a solid ball or a plasma with solid-like properties.

Water Waves: Tidal Bores

In Vol. I, Feynman says: “Actually water is much more complicated than sound.” Our first topic on water waves is a shock wave phenomenon: tidal bores. These result from the “piling up of waves” that sharpen and intensify the wavefront of a rising tide.

As Feynman later shows, the speed of long water waves increases as a body of water deepens. In a tidal bore, an initial wave deepens the water thereby increasing the speed of following waves. Secondary waves catch up to the primary wave, increasing the height and steepness of the wavefront. This effect is particularly impressive in long, narrow, shallow channels that open into large bodies of water. Such channels often experience large tidal swings and severe currents as water rushes into the channels at high tide and out again at low tide.

The tide doesn’t simply rise, it arrives in massive walls of water. Tidal bores aren’t waves in the traditional sense; they have no trough, the water level doesn’t drop after the crest passes.

Figure 46-6 shows a striking example of a tidal bore: the pororoca, which occurs in the mouth of the Amazon River during equinoxes. A pororoca can be 4m high (13 feet). One surfer rode a pororoca for 37 minutes, traveling 12.5 km (7.5 miles), for an average speed of 20 km/h (13 mph). Note the vigorous and chaotic churning at the wavefront.

Two schematic side views of a tidal bore are shown in Figure 46-7; the upper image corresponds to time t, and the lower image to time t+dt. In these images, the water behind the wavefront (left side) has depth H, and the undisturbed water (right side) has depth L. The incoming tide is moving toward +x at velocity v, but the tidal bore’s wavefront is moving faster, at velocity u. The not-yet-disturbed upstream water is shown in dark gray. We will analyze the tidal bore in a reference frame in which the upstream water is stationary.

During the infinitesimal time interval dt, the incoming tide advances a distance v·dt, while the wavefront advances a distance u·dt. The incoming tide flows up and over the upstream water, filling the vertically dashed area. The ratio of velocities u/v equals the ratio of heights H/(H–L) since the total amount of water does not change. Here’s why. Let W be the channel width (the dimension perpendicular to your screen). The volume of incoming water equals:

v·dt·H·W

The volume of water in the vertically dashed area equals:

u·dt·(H–L)·W

Equating these volumes yields:

v = u (H–L)/H

Note that u is greater than v.

The next step is calculating the pressure difference that creates the force pushing the tidal bore forward. When we analyzed atmospheric air pressure in Chapter 16, we found that the pressure at any altitude is exactly what is required to keep the air above that altitude from falling down. Similarly, within any body of water, the pressure at any depth equals the weight per unit area of the water above that depth.

For mass density ρ, acceleration of gravity g, the water pressure P at depth y equals:

P(y) = ρ g y

The average pressure ⟨P⟩ at the face of the wavefront is ρg times the average y, which equals:

⟨P⟩ = ρgH/2

That pressure is exerted over an area equal to W·H, resulting in a force of:

F_BORE = ρgWH²/2, toward +x

Similarly, the not-yet-disturbed upstream water exerts a pressure in the opposite direction, resulting in a force of:

F_UPST = ρgWL²/2, toward –x

The net force pushing the wavefront equals:

F = F_BORE – F_UPST = ρgW(H²–L²)/2

The final step is calculating the water’s momentum change and equating that to the above driving force.

During time interval dt, a volume of water equal to v·dt·H·W is accelerated from velocity v to velocity u. This is the water previously flowing within the rising tide that fills the advancing wavefront during dt. This volume multiplied by its mass density ρ and by the velocity increase (u–v) yields a momentum increase of:

dp = v dt H W ρ (u–v)

Since the derivative of momentum equals force,

dp/dt = F

v H W ρ (u–v) = ρg (H²–L²) W/2

v (u–v) = g(H²–L²)/2H

Using the previously derived expression for v:

v = u (H–L)/H

u–v = u – u(1–L/H) = uL/H

v (u–v) = g(H²–L²)/2H

u(H–L)/H · (uL/H) = g (H–L)(H+L) /2H

u² L/H² = g(H+L)/2H

u² = g(H+L)H/2L

Frankly, I was confused by Feynman’s analysis. For the tidal bore to continue, its properties at t+dt should be the same as at time t, etc.

Except for its upstream advance. In particular, all the water behind the wavefront should have velocity v at t+dt, as it did at time t. Yet, in the lower image of Figure 46- ase. Group velocity is the speed at which the physical wave (the wave packet) moves, while the phase velocity is the speed of an oscillation of a single frequency. Feynman explains how a physical wave can move slower than an individual frequency of which it is composed. He says: "If one looks at the bunch of waves that are made by a boat traveling along, following a particular crest, he finds that it moves forward in the group and gradually gets weaker and dies out in the front, and mystically and mysteriously a weak one in the back works its way forward and gets stronger. In short, the waves are moving through the group while the group is only moving at half the speed that the waves are moving."

Perhaps surprisingly, longer wavelength waves travel faster than shorter waves. When waves from a distant high-speed boat reach a small dinghy, the dinghy will first bob up and down slowly as the longest waves pass, and will bob ever more rapidly as shorter waves come later.

Bow Waves in Water

At the start of this chapter, we analyzed bow waves for sound in air and for light in refractive media. We found that the bow waves flair out at a fixed angle. In those cases, the cone half-angle gets smaller as the projectile goes faster.

But for the waves in a boat’s wake, the situation is far more complex because phase velocity and group velocity are not equal in water, and both velocities vary with wavelength. Figure 46-9 shows the complex wave pattern created by a boat moving at a constant speed that is faster than the wave speed.

Figure 46-9 Boat Wake

Feynman says: “…we have waves in the back with fronts moving parallel to the motion of the boat, and then we have little waves on the sides at other angles. This entire pattern of waves can, with ingenuity, be analyzed by knowing only this: that the phase velocity is proportional to the square root of the wavelength. The trick is that the pattern of waves is stationary relative to the (constant-velocity) boat; any other pattern would get lost from the boat.”

Ripples

The restoring force for long waves is gravity. But for very short waves, the primary restoring force becomes capillary attraction, also called surface tension.

In V1p51-8, Feynman provides without derivation the equation for the phase velocity of waves whose restoring force is due entirely to surface tension.

v = √(kτ/ρ), for ripples

Here τ is the surface tension and ρ is the water density. We can again calculate the group velocity: ω = k v = k3/2 √(τ/ρ)

v = dω/dk v = (3/2) k1/2√(τ/ρ)

v = (3/2) v G P

The group velocity approaches 3/2 of the phase velocity for very short waves and approaches 1/2 of the phase velocity for very long waves.

Comparing ripples with long waves, both phase and group velocities have the opposite dependence on wave number k. Whereas long-wave velocities increase with wavelength λ (decrease with k), short-wave velocities decrease with wavelength (increase with k).

Real waves, of course, are subject to both gravity and surface tension. Hence their phase velocities are given by: v = √ [kτ/ρ + g/k]

v = √ [2πτ/ρλ + gλ/2π]

Figure 46-10 is a graph of the phase velocity.

Figure 46-10 Phase Velocity in cm/s (Vertically) vs. Wavelength in cm (Horizontally)

The key features are: the phase velocity is large for long wavelength; grows without limit as the wavelength approaches zero; and has a minimum at an intermediate wavelength, which we will call λ MIN.

Unlike sound waves in air, a sudden disturbance does not produce a wave with a sharp wavefront, because in water the different wavelength components of the wave travel at different speeds. Any sudden disturbance at a remote location results in ripples first, followed by long waves, and finally by waves of medium wavelength.

To calculate λ MIN, let’s find the minimum of v 2 rather than v P P; it’s less messy and both clearly are minimum at the same value of λ MIN.

0 = d(v 2)/dk = –2πτ/ρλ2 + g/2π λ MIN = 2π √(τ/ρg)

k MIN = √(ρg/τ)

Typical values for the constants are: τ = 73 gram/s2 ρ = 1 gram/cm3 g = 981 cm/s2

These yield the minimum phase velocity: v P = √ [459/λ + 156λ] cm/sec, with λ in cm.

v P MIN = 23 cm/sec at λ = 1.7 cm v P MIN = 0.52 mph at λ = 0.8 inches

Feynman adds some interesting comments about the complexity of familiar waves: "An interesting feature about capillary waves can be seen in the disturbances made by an object moving through the water. From the point of view of the object itself, the water is flowing past, and the waves which ultimately sit around it are always the waves which have just the right speed to stay still with the object in the water. Similarly, around an object in a stream, with the stream flowing by, the pattern of waves is stationary, and at just the right wavelengths to go at the same speed as the water going by. But if the group velocity is less than the phase velocity, then the disturbances propagate out backwards in the stream, because the group velocity is not quite enough to keep up with the stream. If 群速度大于相速度时，波形会出现在物体前方。若仔细观察水流中的物体，可以看到其前方有细小的涟漪，后方则形成长长的“尾迹”。

这类现象的另一个有趣实例可见于液体倾倒过程。例如，若将牛奶快速从瓶中倒出，可以看到流出的液流中交叉出现许多线条。这些是从边缘扰动处产生并向外传播的波，类似于水流中物体周围的波纹。两侧的效应共同形成了这种交叉图案。

**破浪** 波在浅水中传播速度较慢。这一点在波浪接近海岸时尤为重要。当后方波浪在较深水域中速度更快并赶上前方波浪时，波群会聚集并形成激波。由于近岸处水深通常急剧变化，所产生的激波远比之前讨论的更为复杂。这一问题尚未得到解析解，但我们都清楚其实际表现——参见图46-11。

图46-11 海岸附近的破浪我亲爱的妻子琼拍摄了我在毛伊岛冲浪的照片——嗯，或许那只是在我的梦中。

**第46章复习：核心要点** 1. 物体在介质中的速度超过该介质中的波速时，会产生锥形的船首波。对物理学家而言，一个重要例子是粒子在折射介质中运动时发出的切伦科夫辐射。设物体速度为v，波速为c，则锥半角θ满足： sinθ = c/v 2. 当尾波速度快于前方波浪时，会产生激波。高强度声波会加热所经过的空气，从而提高后续声波的波速。随着波间距减小，波幅增大、宽度变窄，形成突然的巨响。激波的传播速度总是快于较低强度的波。

3. 固体中可传播两种波：纵波（又称压缩波）和横波（又称剪切波）。固体中的压缩波类似于空气中的声波。横波仅存在于固体中，而在气体或液体中无法传播。在横波中，波的振动方向垂直于传播方向；在纵波中，振动方向则与传播方向平行。

4. 地震学研究地球内部传播的波，使我们得以确定其结构。地球从表面向下的主要分层（及厚度）为：地壳（5至50公里）；上地幔（650公里）；下地幔（2200公里）；外核（2200公里）；以及内核（1220公里）。

## 5. 涌潮出现在强涨潮期间，在浅窄的河道中，由于来波“堆积”而产生激波效应。

## 6. 水波并不搬运水体。当波通过时，每个分子大致沿圆形路径运动，并近似返回起点。该圆形路径位于垂直于波阵面的竖直平面内。开阔深水中波的相速度由下式给出：

v = √ [2πτ/ρλ + gλ/2π]

其中τ为水的表面张力，ρ为密度，g为重力加速度，λ为波长。短波时第一项占主导，此时表面张力（毛细效应）是主要恢复力；长波时第二项占主导，此时重力是主要恢复力。

**第47章** **波的综述** 本章回顾第42至46章探讨的波现象的物理学。

## 1. 任何由线性微分方程支配且在所有频率下具有相同速度v的波现象，都可用形如f(r–vt)的函数表示。

## 2. 三维波动方程为：

∂²A/∂t² / v² = ∂²A/∂x² + ∂²A/∂y² + ∂²A/∂z²

## 3. 对于形如sin(ωt–kx)的周期波，ω为角频率（弧度/秒），k为波数（弧度/米）。波速有三种表征方式：

信号速度是信息或粒子能够传播的最大速度；它永远不会超过光速c。

相速度 = ω/k，是单频波的速度，这是一种几乎从不代表实际的理想化。相速度不受狭义相对论限制。

群速度 = dω/dk，是多频波包的速度。几乎所有情况下，群速度小于光速c。

4. 声音的物理学可通过牛顿力学定律理解。它涉及三种效应的相互作用：气体运动产生密度梯度；密度梯度产生压强梯度；压强梯度驱动气体运动。另一个关键因素是：声音传播时热流极小，气体的膨胀与压缩是绝热过程。

## 5. 当两个频率不同（ω₁和ω₂）的波叠加时，合成波可表示为：

cos(ω₁t) + c cos(ω₁t) + cos(ω₂t) = 2 cos(ωt) cos(Δωt)

ω = (ω₁ + ω₂)/2 Δω = (ω₁ – ω₂)/2

The intensity I of the combined wave is: I = 1 + cos(2Δωt)

When the waves have similar frequencies, Δω<<ω, the wave oscillates rapidly at frequency ω, while its amplitude waxes and wanes slowly at frequency 2Δω, which is called the beat frequency.

When musical instruments’ string lengths have a small-number ratio, their harmonics match with Δω=0 and beats are eliminated, producing the pleasing effect called consonance. At other length ratios, the combined sound has beats and is called dissonant.

6. Periodic motion in which all points move sinusoidally with the same frequency and phase, but with possibly different amplitudes, is called a mode. Having the same phase means every point passes through zero displacement at the same time. Locations at which the displacement is always zero are called nodes.

A wave with velocity v confined to a finite space, and constrained to have zero displacement at its boundaries, has only certain possible modes. In a 1D space of length L: ωₙ = nvπ/L, for any integer n>0 Mₙ(x) = sin(nπx/L)

In a 2D space of length L and height H: ωₙₘ = vπ √(n²/L²+m²/H²), for integer n,m>0 Mₙₘ(x,y) = sin(nπx/L) sin(mπy/H)

7. Feynman says: “Any [periodic] motion at all can be analyzed by assuming that it is the sum of the motions of all the different modes, combined with appropriate amplitudes and phases.”

## 8. Musical tones are characterized in terms of loudness, pitch, and quality

Loudness is the amplitude of a sound wave.

Pitch is the frequency of a tone’s most basic pattern.

Quality corresponds to the multiplicity of frequencies from which a waveform is composed.

9. Any function f(t) that repeats with period T (T=2π/ω) has a Fourier series representation that is a sum of sine and cosine functions. (∫ denotes the integral over a full period T.)

f(t) = Σₙ { aₙ cos(nωt) + bₙ sin(nωt) } a₀ = (1/T) ∫₀ᵀ f(t) dt b₀ = 0 aⱼ = (2/T) ∫₀ᵀ f(t) cos(jωt) dt bⱼ = (2/T) ∫₀ᵀ f(t) sin(jωt) dt

The energy of a wave, averaged over a full period T, is proportional to the sum of the squares of the amplitudes of the wave’s Fourier components, averaged over a full period.

E ~ ∫₀ᵀ f(t)² dt = T a₀² + (T/2) Σₙ>0 [aₙ² + bₙ²]

In complex number notation, the Fourier equations are: f(t) = Real part of Σₙ { zₙ exp(inωt) } zₙ = aₙ +ibₙ = (2/T) ∫₀ᵀ f(t) exp(–inωt) dt, for n≥1 a₀ = (1/T) ∫₀ᵀ f(t) dt, and b₀ = 0

10. Any function G(x) has a Fourier transform S(k) given by this integral from x=–∞ to x=+∞: S(k) = ∫_{-∞}^{+∞} G(x) exp{–ikx} dx / √(2π)

If G(x) is a Gaussian distribution, S(k) will also be Gaussian: G(x) = exp{–x²/2σ²} / √(2πσ²)

S(k) = exp{–k²σ²/2} / √(2π)

The standard deviation of G(x) is σ, while the standard deviation of S(k) is 1/σ.

11. An object moving with velocity v through a medium with wave speed c produces bow waves with a conical shape if v>c. The cone half-angle θ is given by: sinθ = c/v

12. Shock waves occur when trailing waves move faster than the waves in front of them. High intensity sound waves heat the air they pass through thereby increasing the speed of the sound waves that follow. Shock waves always travel faster than low intensity sound waves.

13. Tidal bores occur in strong rising tides, in shallow narrow channels, as incoming waves “pile up” creating a shock wave effect.

14. Solid materials support two types of waves: longitudinal waves, also called compression waves; and transverse waves, also called shear waves. Compression waves in solids are analogous to sound waves in air. Transverse waves occur only in solids, not in gases or liquids. Wave oscillations are perpendicular to the wave’s direction of motion in transverse waves and along the direction of motion for longitudinal waves.

15. Seismology, the study of waves traveling through Earth’s interior, has enabled us to determine our planet’s internal structure.

16. Water waves do not transport water. As a wave passes, each molecule moves in a roughly circular path, approximately returning to its starting point. This circular path lies in a vertical plane that is perpendicular to the wavefront. The phase velocity of waves in open, deep water is given by: v = √ [2πτ/ρλ + gλ/2π]

Here τ is water’s surface tension, ρ its density, g is the acceleration of gravity, and λ is the wavelength.

The first term dominates for short waves, where surface tension (the capillary effect) is the primary restoring force. The second term dominates for long waves, where gravity is the primary restoring force.

## Chapter 48: The Physics of Vision

Vision is a complex process involving physics and physiology. As this is a physics course, we will focus more on the former. In V1p35-1, Feynman begins this topic by looking into the eye.

The Human Eye

A stationary human right eye has a field of view that extends from the central line of sight: 95º to the right, 60º to the left, 75º downward, and 60º upward. The left eye covers the same range on the opposite side. Each eye rotates about ±45º. The combination of eye rot Rotation and field of view gives us an angular range of 280º horizontally and 225º vertically, without turning our head. That leaves us blind to only an 80º-wide zone directly behind us. In terms of an analog clock, with 12 o’clock being straight ahead and 3:00 to the right, our blind zone is between 4:40 and 7:20, hence fighter pilots’ concern about what’s on their “6.” (I wonder why evolution didn’t produce a creature with a third eye at the back of its head.)

The full range of light intensities through which our vision operates effectively is 100 trillion to 1. The iris controls the eye’s entrance aperture, the pupil, whose diameter ranges from 2 mm to 8 mm, but is typically 4 mm. In terms of intensity discrimination, we can detect stationary objects with as little as a 1% intensity contrast.

Figure 48-1 shows a horizontal cross section of a right human eye. Light rays enter through the cornea, refract, and are focused on the retina.

Figure 48-1 Diagram of Human Eye 1. Conjunctiva, 2. Sclera, 3. Cornea, 4. Aqueous humor, 5. Lens, 6. Pupil, 7. Uvea, 8. Iris, 9. Ciliary body, 10. Choroid, 11. Vitreous humor, 12. Retina, 13. Macula, 14. Blind spot, 15. Optic nerve

Optics of Vision The eye features a two-element optical system composed of the cornea and the lens. Its total focusing power is 43 diopters, meaning that it can focus from infinity to as close as 1m/43 = 2.3 cm (0.9 inches). The aqueous humor fills the space between cornea and lens, and the vitreous humor fills the space between lens and retina; both are almost entirely water.

The cornea provides about 2/3rds of the eye’s focusing power due to its shape and the change of refractive index at its exterior surface. The cornea’s index of refraction is 1.37, which is substantially larger than the index of air (1.0003), but only slightly larger than the index of water (1.33). Since the bending of light at a surface is determined by the change in refractive index across that surface, our vision performs well in air but not in water. Underwater, we lose most of our focusing power and our vision becomes blurry. This can be remedied with a diving mask that maintains air in front of our eyes.

The shape of the cornea is superior to that of normal man-made optics. Mass-produced lenses are spherical, and therefore suffer from spherical aberration that limits their performance (see Chapter 30). (Eyeglass lenses correct astigmatism with the addition of a cylindrical surface on the opposite side). By comparison, the cornea is less curved at its sides than a sphere, having a shape that reduces spherical aberration.

The lens consists of multiple layers, called laminae, whose arrangement is similar to an onion. To enhance transparency, mature lens cells have no nerves, blood vessels, connective tissues, mitochondria, or nuclei. Lens cells are nourished by the aqueous humor. The refractive index of the lens varies, being 1.406 in the center and 1.386 at its edges. This variation gives the lens greater focusing power than is possible with a uniform index. The shape of the lens is adjusted to optimally focus objects of interest. For distant objects, the ciliary muscles relax and the lens flattens. For nearby objects, the ciliary muscles contract, making the lens more curved and thicker at its center.

The Retina The eye’s light sensor is the retina, which contains a variety of photoreceptors and covers about 2/3rds of the eyeball’s inner surface.

At the periphery of the visual field, photoreceptors are sparsely distributed. Here, neural density declines much more rapidly, because up to 100 receptors feed into a single nerve fiber. Peripheral acuity is therefore quite limited. Receptor density and acuity increase steadily toward the center of the visual field. The highest acuity is provided by the 0.2 mm-wide foveola that lies at the center of the macula. Each receptor in the foveola is connected to an individual nerve fiber, with the result that the foveola drives about half of the fibers in the optic nerve. The foveola enables reading and other precise visual activities.

Vision employs two types of photoreceptors: rods and cones. In the 1990’s, it was discovered that a small percentage of the eye’s ganglion cells are also photosensitive. The ganglion receptors sense overall light intensity for the control of the pupil, and possibly to inform the circadian rhythm.

The 120 million rod receptors in a human eye cover the bulk of our visual field, and provide black and white vision. Rods are extremely sensitive, up to 10,000 times more sensitive than cones. In optimal conditions, a rod cell can be triggered by a single photon of light. However, a neural response requires 5 to 10 photons detected within 0.1 seconds. Rods cells are about 2 microns in diameter.

The 6 million cone receptors provide color vision, and require much higher light intensity. This is why we see only black and white at low light levels. Cone cells are typically 6 microns in diameter, but are thinner in the Densely packed foveola. Humans have three types of cones, each type being sensitive to a different range of wavelengths of light. Some other species have four or five types of cones, and are able to see infrared and ultraviolet light that we cannot.

Cones are sharply concentrated in the macula, as shown in Figure 48-2.

Figure 48-2 Density of Rods & Cones Across Visual Field Dark Line Marks 10 Million Photoreceptors Per Square cm

In V1p36-2, Feynman explains that the retina is effectively part of the brain. In embryonic development, he says: “a piece of the brain comes out in front, and long fibers grow back, connecting the eyes to the brain. The retina is organized in just the way the brain is organized and, as someone has beautifully put it, ‘The brain has developed a way to look out upon the world’.”

After photoreceptors detect light, signal processing starts immediately in the retina itself. The retina has ten layers of cells that process an estimated 9 million bits of visual information per second, before sending the results on to the brain. Retinal processing provides rapid edge and motion detection, which are essential survival traits.

One puzzling feature of our visual system is that our retinas seem “inverted.” In all vertebrates, the photoreceptors are on the backside of the retina, the side farthest from the pupil. Light must therefore travel through the entire retina to reach its photoreceptors. Nerves run across the front side of the retina, the side nearest the pupil. On their way to the brain, these nerves pass through a void in the retina called the blind spot.

The blind spot contains no photoreceptors, which results in each eye being blind to a small portion of its visual field that is typically 15º to the temporal side of the primary line of sight. Since the left and right eyes’ blind spots are in different parts of our field of view, each spot is noticeable only when the other eye is closed.

By contrast, the retinas of cephalopods, such as octopus and squid, are not “inverted.” Their photoreceptors are on the light-facing side of their retinas, and their nerves run across the backside. As a result, cephalopods have no blind spots.

Some physiologists suggest that our “inverted” retinas facilitate blood flow to our energy-intensive retinas, more than compensating for what seems to be a poor optical design. In V1p36-4, Feynman is not so kind, calling the inverted design of our retinas “apparently stupid.”

Color & Light Intensity

In V1p35-2, Feynman remarks on a striking feature of our vision: dark adaptation. When light levels diminish rapidly, we see very little initially. Then slowly our eyes become increasingly sensitive, and eventually, we may be able to see quite well — but only in black and white. Our cone receptors do not function in the dark, so our dark vision comes only from rods.

In Feynman’s day, astronomers observing faint nebulas by eye often saw them only in black and white, whereas long-exposure photographic images of the same objects demonstrated beautiful colors. The difference, of course, was due to our visual insensitivity to color at low light intensity. In modern professional astronomy, naked-eye viewing and film photography have been largely replaced by high-performance CCD imaging due to its much greater sensitivity.

This effect is even more interesting because the colors we perceive change with light intensity. Figure 48-3 illustrates how the sensitivity of each type of photoreceptor varies with wavelength. Here each curve is normalized to the same peak sensitivity.

Figure 48-3 Spectral Response of Various Receptors

Cones are designated blue, green, or red according to the colors of their peak sensitivity — or by short, medium, or long according to the corresponding wavelengths.

Note that rods are reasonably sensitive to blue light but not to red light. Therefore, as Feynman notes, when comparing pieces of red and blue paper, red might seem brighter in daylight but darker at night. In daylight, we see the red paper very well with our red cones, while our rods-only night vision is very insensitive to red. This is called the Purkinje effect.

Astronomers take advantage of the Purkinje effect. Using red lights that activate cone receptors, astronomers can find their way in the dark without ruining the dark adaptation of their rod cells. This is important because astronomers spend so much time in the dark.

Another interesting visual effect involves what astronomers call averted vision. Our high-acuity foveola contains few if any rods, making it useless in dim light. We are accustomed to aligning our foveola with objects of special interest, but that is counterproductive in darkness. Naked-eye astronomers train themselves to concentrate on areas outside the center of their field of view. They avert their vision to place objects where the retina has a higher density of rods and provides the best night vision.

Two other peculiar features of our vision arise at the periphery of our visual field. Since our cones are concentrated along our primary line of sight, we do not see colors peripherally even in bright light. An object that crosses our field of view becomes colorful as it crosses our primary line of sight. Our peripheral vision does excel, however, at detecting motion. The retina’s image processing layers promptly alert us to objects moving into our field of view; clearly this is a survival mechanism.

Measuring Color Response In V1p35-3, Feynman addresses the question of what does “color” mean in our visual system? We all know that our instruments can precisely measure light intensity as a function of wavelength. But the question is: what color do our eyes perceive when viewing various combinations of wavelengths? If green light enters our eyes we will see green — that is simply the definition of “green.” But are there other combinations of light that also look “green”? The answer turns out to be: Yes.

Many different combinations of wavelengths of various intensities will look “green” to us, because our three-color vision senses only a subset of all possible combinations of light wavelengths. While the human eye can distinguish 10 million different colors, there are an infinite number of wavelengths and an infinite number of ways of combining them.

So how can we measure and quantify what we mean by “green”?

It would be enormously difficult, perhaps impossible, to determine what each person senses when they see certain combinations of wavelengths or to determine which stimuli look “green.” Instead, Feynman says, the most effective approach is a null experiment. In general, null experiments consist of finding circumstances where two entities are equal — where their difference is null. Such experiments often achieve astonishing precision. A prime example is the Michael-Morley null experiment confirming the equality of the speed of light in different directions.

In a color null experiment, a subject views two light sources, each a combination of wavelengths. The composition of one source is adjusted until the subject says two sources appear identical. By repeating the experiment with many subjects, one discovers the extent to which these wavelength combinations are universally indistinguishable. This technique avoids the conundrum of whether or not people experience the same sensation from the same light.

In his lecture, Feynman demonstrated the technique using four light projectors. Three projectors produced colored spots of any desired intensity, with one each for red, green, and blue. The fourth projector produced a large white circle with a black spot at its center.

Initially, Feynman turned on only the green and red lights, producing a shade of yellow. Different projector intensities produce various shades of green, yellow, orange, and red. Feynman showed that any specific color can be produced in other ways as well. For example, some combination of green and red make a shade of orange, but that same shade can be made from orange and white, or yellow and red.

Let’s represent this mathematically. Denote the projector colors using R for red, G for green, and B for blue. Define r, g and b to be the intensities of the red, green, and blue projectors. The resultant color Z for any combination of three projector intensities is: Z = rR + gG + bB The question is: can we make all the colors visible to humans from just red, green, and blue?

Feynman demonstrated that equal intensities of RGB made a “fairly nice white.” But when the three colors were projected onto the central black spot from the fourth projector, its annular white ring surrounding the color spots no longer seemed white, but was somewhat yellowish.

Feynman then tried to make brown, which, in V1p35-4, he says is very difficult.

“People who give lectures on color make all the ‘bright’ colors, but they never make brown, and it is hard to recall ever having seen brown light. As a matter of fact, this color is never used for any stage effect, one never sees a spotlight with brown light; so we think it might be impossible to make brown … we point out that brown light is merely something that we are not used to seeing without its background. As a matter of fact, we can make it by mixing some red and yellow. To prove that we are looking at brown light, we merely increase the brightness of the annular background against which we see the very same light, and we see that that is, in fact, what we call brown! Brown is always a dark color next to a lighter background.”

Mixing Colors The first important principle of color mixing is that color combinations can be indistinguishable to human eyes, even if their spectral compositions are different. Mathematically, let X and Z be two different combinations of light wavelengths. If X and Z are indistinguishable to our eyes, we will say for the present purposes that they are equal: X = Z, if we can’t see the difference If we now add any Q, some other combination of light wavelengths, t X + Q = Z + Q Let’s be clear about what this equation represents. If we shine light X at one spot and shine light Z at another spot, and then shine the additional light Q on both spots, the resultant colors of the two spots are as indistinguishable to human eyes as are X and Z. This means that the colors of emitted light are additive. Paint and ink colors are different. Both paint and ink absorb rather than emit light, hence their colors are subtractive.

In V1p35-5, Feynman says it is very important to note that the indistinguishability of two colors does not change when the state of our eyes changes. If for example, we stare at a bright red light for a long time, and then look at white paper, that paper will appear greenish. This is because our photoreceptor response to red diminishes under intense exposure and takes some time to recover. Nonetheless, any X and Z that are equal, by the above definition, remain equal even during such changes in our visual response. Each might appear different as our eyes change, with less red in this example, but they will still appear identical.

This principle of color mixing holds as long as the light intensity adequately activates our cone cells. The second important principle of color mixing is that any visible color can be made by mixing three primary colors, such as red, green, and blue. (There is a caveat coming shortly.) The only restriction on the choice of primary colors is that they must be linearly independent: none of the three can equal any sum of the other two.

In V1p36-2, Feynman points out how surprising this principle might be to most non-physicists. “The total sensation that is associated with the absorption characteristics of the three [cone types] acting together is not necessarily the sum of the individual sensations. We all agree that yellow simply does not seem to be reddish green; … presumably the sensation of light is due to some other process than a simple mixture like a chord in music, where the three notes are there at the same time and if we listen hard we can hear them individually. We cannot look hard [at yellow] and see the red and the green.”

Combining colors can be elegantly represented using vectors, as first demonstrated by Schrödinger who is more famous for quantum mechanics and bizarre cats.

Let our three primary colors be: A, B, and C. And let colors X and Z be represented by: X = aₓA + bₓB + cₓC Z = aᵤA + bᵤB + cᵤC

Then the color Q = X + Z is: Q = (aₓ + aᵤ)A + (bₓ + bᵤ)B + (cₓ + cᵤ)C

This is equivalent to the vector equation: Q = X + Z

We can perform color analysis using our vector analysis skills. The primary colors A, B, and C are the three axes of the color space. Any color X is equivalent to a vector in that space with coordinates aₓ, bₓ, and cₓ. Adding colors is just a matter of adding their vectors.

Here is the caveat: producing some colors from three primary colors may require negative intensities. For example, if red, yellow, and blue are the primary colors, no combination of those colors from three projectors shining on the same spot will match green from a fourth projector shining on an adjacent spot. But we can get a color match with some trickery. If we add red to the green spot, we will be able to adjust the three primary color projectors to match the green-red spot. In fact, we will only need to project some yellow and some blue. We can write this mathematically: G + rR = yY + bB G = –rR + yY + bB

This means we can match any visible color with any set of linearly independent primary colors, but we might need a negative intensity. While theoretically satisfying, this isn’t usually a practical solution.

Some sets of primary colors provide a greater range of color combinations than others, without using negative intensities. RGB is the most common choice for additive colors. In printing, where colors are subtractive, the standard choice is CMYK: cyan (blue-green), magenta (blue-red), yellow, and black.

Chromaticity Diagram Three primary colors form the axes of a 3-dimensional space. Normalizing the three primary intensities to produce a constant combined intensity reduces the color space to two dimensions. This is equivalent to reducing 3D space to the surface of a 2D sphere by normalizing all vectors to the same radius.

On that basis, colors are characterized using a 2D chromaticity diagram. The diagram plots the limits of human sensitivity to various wavelength combinations, as determined experimentally by examining many individuals.

One standard format for this diagram is CIE 1931 shown in Figure 48-4. The diagram has a horseshoe shape, with a straight line across the bottom from blue (420 nm) on the left to red (680 nm) on the right, and a curved end at green (520 nm) in the upper left.

Figure 48-4 CIE 1931 Chromaticity Diagram Numbers on Periphery are Wavelengths in nm

Those with black and white ereaders can view this color image on their computer at http://www.guidetothecosmos.com/feynman/ F1D-color.html.

On the CIE diagram, I have superimposed the position of R, G, and B, along with the triangle that connects them. Any color within the triangle can be represented by a linear combination of these primary colors, with positive coefficients. Colors outside the triangle can be represented, but only with some negative coefficients. The main areas that are lost with positive-only coefficients are green.

Any specific wavelength of light (any pure monochromatic light of only one frequency) can be represented by a linear sum of primary colors, using both positive and negative coefficients. In the 1920’s this was carefully done for all wavelengths in the visible range by W. David Wright and John Guild. Their results, shown in Figure 48-5, are the basis of the CIE diagram.

Figure 48-5 RGB Coefficients of Monochromatic Light vs. Wavelength λ Monochromatic colors (single wavelength light) are on the CIE diagram’s edges, while mixed wavelength light is in its interior. All points in the interior are linear combinations, with coefficients between 0 and 1, of the monochromatic light on the perimeter.

## Chapter 48 Review: Key Ideas

1. The human visual system has a field of view that spans 280º horizontally and 225º vertically. Its focusing power is 43 diopters, enabling us to focus from infinity to 2.3 cm (0.9 inches).

2. The photoreceptors in each retina include 120 million rods that see the world in black and white, and 6 million cones of three types that detect color. The three types of cones correspond to peak sensitivities at blue, green, and red wavelengths. The density of cones is very strongly peaked in the foveola, which provides high-acuity vision. The density of rods is nearly zero in the foveola. Rod density peaks in an annular ring surrounding the foveola, and decreases rapidly toward the edge of the visual field.

3. Rods are highly sensitive to light, up to 10,000 times more sensitive than cones. In dim light, our cones are useless and we see only in black and white.

4. The retina is an extension of the brain that originates in the embryonic brain. Processing of the 9 million bits of visual information per second begins in the retina, with the results transferred through the optic nerve to the brain.

5. The first principle of color mixing is that color combinations can be indistinguishable to human eyes even if their spectral compositions are different. Two indistinguishable colors remain indistinguishable even when the state of our eyes changes.

6. The second principle of color mixing is that any visible color can be made from three primary colors, such as red, green, and blue (possibly with some negative coefficients), provided those colors are linearly independent. Color mixing is elegantly represented with vectors. For primary colors A, B, and C, let colors X and Z be written: X = aₓ A + bₓ B + cₓ C Z = a_z A + b_z B + c_z C Then the color Q = X + Z is: Q = (aₓ + a_z) A + (bₓ + b_z) B + (cₓ + c_z) C This is equivalent to the vector equation: Q = X + Z 7. A chromaticity diagram shows all the colors humans can perceive. The diagram is horseshoe shaped, with a straight line across the bottom from blue on the left to red on the right, and a curved end at green in the upper left. Monochromatic colors (single wavelength light) are on the diagram’s edges, while mixed wavelength light is in its interior.

## Chapter

Symmetry & Physical Laws Symmetry has become one of the most powerful concepts in theoretical physics. In trying to identify the laws governing new phenomena, physicists are able to exclude a wide variety of potential but incorrect solutions on the basis of symmetry.

In V1p52-1, Feynman begins his lecture on symmetry and physical laws with this poetic and insightful introduction: “Symmetry is fascinating to the human mind, and everyone likes objects or patterns that are in some way symmetrical. It is an interesting fact that nature often exhibits certain kinds of symmetry in the objects we find in the world around us. Perhaps the most symmetrical object imaginable is a sphere, and nature is full of spheres—stars, planets, water droplets in clouds. The crystals found in rocks exhibit many different kinds of symmetry, the study of which tells us some important things about the structure of solids. Even the animal and vegetable worlds show some degree of symmetry, although the symmetry of a flower or of a bee is not as perfect or as fundamental as is that of a crystal.

“But our main concern here is not with the fact that the objects of nature are often symmetrical. Rather, we wish to examine some of the even more remarkable symmetries of the universe—the symmetries that exist in the basic laws themselves which govern the operation of the physical world.” Feynman attributes the best definition of symmetry to Herman Weyl. In my own words: An entity E is symmetric under process S if S leaves E indistinguishable from its original state.

For example, rotating a sphere about the vertical axis through any angle will leave it indistinguishable from its original state.

axis leaves it indistinguishable from its original state; this makes a sphere symmetric with respect to rotation about that axis. More generally, a sphere is symmetric under the process of rotation by any angle about any axis.

A more interesting example is that kinetic energy is symmetric with respect to time reversal, which is the replacement of t by –t. Let’s see what this means.

K.E. (t) = m v2 /2 = m (dx/dt)2 /2 K.E.(–t) = m (dx/d[–t])2 /2 K.E.(–t) = m (dx/dt)2 /2 = K.E.(t)

To understand what this means, consider taking a video of an object moving with velocity +v, and later play the video backwards. In reverse, the video shows the object moving with velocity –v, now going in the opposite direction. But in both forward and reverse, the object has the same kinetic energy. This is because the kinetic energy equation contains v2, which doesn’t change values under time reversal. If time reversal symmetry is a universal property of nature, kinetic energy must be the same in forward and reverse time. That means the kinetic energy equation cannot contain terms like v3.

The following symmetry processes are universally valid.

Translation in Space Translation in Time Spatial Rotation Motion at Constant Velocity Exchange of Identical Particles Change of Quantum Phase CPT Symmetry

The following symmetry processes are valid for all but the weak interaction.

Spatial Reflection Time Reversal Exchange of Matter & Antimatter

As Feynman stresses, the natural laws as we now know them have these symmetries. We can only teach what we know now, and remain open to new discoveries that could teach us all something more.

Translations in Space & Time By translation in space or time physicists mean moving to some other location in space or some other moment in time. Translational symmetry means that the laws of nature are invariant under any translations of the following form:

x is replaced by x + Δx y is replaced by y + Δy z is replaced by z + Δz t is replaced by t + Δt

A simple example is: F = m dv/dt

Let’s make the above translation, marking the translated v and F with asterisks.

v* = d(x+Δx)/d(t+Δt)

F* = m dv*/d(t+Δt)

Because Δx is a constant, any change in (x+Δx) must equal the change in x. Similarly for (t+Δt) and t. We therefore have:

d(t+Δt) = dt d(x+Δx) = dx

v* = d(x+Δx)/d(t+Δt) = dx/dt = v F* = m dv*/d(t+Δt) = m dv/dt = F

Science might well be impossible if natural laws were not symmetric under space and time translations. For example, how could we make sense of our world if natural phenomena behaved differently in my lab compared with your lab, or if observations we make today are not reproducible tomorrow?

Some things, of course, do change with position and time. Atmospheric pressure is not the same atop Mt. Everest as it is at the Dead Sea. Atmospheric pressure also changes as the weather changes. When we look for symmetries, we must exclude varying external factors.

So, by translational symmetry we mean natural laws are invariant when everything is translated, or at least everything that might influence an observation of interest. Ultimately, what this really means is that space and time are homogeneous: all locations in space are intrinsically identical and indistinguishable, as are all instants in time. The laws of nature may specify time differences or distances between points, but they do not reference specific instants in times or points in space. The mass of the electron and the strength of its electric field are meaningful concepts only because competent measurements yield the same values everywhere and always.

The laws of nature, as currently known, break down at the center of black holes and at the instant of the Big Bang. Therefore, these are exceptions to the universal principle of space and time homogeneity and translational symmetry.

Rotational Symmetry In addition to being homogeneous, space is isotropic, which means it is the same in all directions. One might think a homogeneous space is necessarily isotropic, but that’s not true. One can imagine a space that is expanding in the x direction, but not in the y or z directions. That space is homogeneous because the same rule applies everywhere, but it is not isotropic because x is different from y and z. The converse, though, is true: if a space is isotropic, it is necessarily homogenous. The proof is: if a space were not homogeneous, at least one point would be different, hence the direction to that point would be different from other directions; thus proving the space is not isotropic. This is an example of proving a proposition by proving its contrapositive.

Because all directions in space are identical and indistinguishable, rotating everything of interest by any angle about any axis leaves the laws of nature invariant.

Constant Velocity Symmetry The Special Theory of Relativity (Chapter 25) states that the laws of nature are invariant under a transformation of constant velocity. This means that adding a constant velocity of any amount in any direct 对事物的一切可能变化具有不变性，并不会产生任何物理上可观测的后果。回想一下，恒定速度意味着以恒定速率沿恒定方向运动；地球绕太阳运行并非恒定速度，因为其运动方向在持续变化。

我们将这种对称性解释为：绝对速度在物理上是没有意义的；不存在一个普遍的参考标准，所有其他速度都是相对于它来定义的。自然定律只能依赖于相对速度——速度的差值或变化——而不能依赖于绝对速度。

在《费曼物理学讲义》第一卷第52-2节中，费曼说：“事实上，正是对相对性问题的研究[由爱因斯坦完成]，最尖锐地将物理学家的注意力集中在物理定律中的对称性上。”

**全同粒子交换对称性**

以上都是空间和时间的对称性。另一种完全不同的对称性是全同粒子交换对称性。

这种对称性指出，如果交换任意两个全同粒子，将不会产生任何物理上可观测的后果。正如费曼指出的，有些人可能会反对上述陈述是同义反复——“全同”的定义就是无后果的互换性。或许该陈述可以有更好的表述，但争论语义对我们学习物理没有帮助。

这一原理的完整背景很有启发性。我们的可观测宇宙包含10的90次方个粒子，它们全部属于仅有的101种类型（数字少了89位）。此外，每种类型的所有粒子都是绝对相同的，其方式完全不同于任何宏观实体。在日常生活中，我们可能说两个东西是相同的，比如来自同一铸币厂的两枚硬币，但实际上，它们永远不相同。两个宏观实体不可能拥有完全相同的中子、质子和电子数量。形成鲜明对比的是，即使是自然本身也无法区分一个电子的内禀属性与其他任何10的80次方个电子的区别。说它们可以互换且完全没有物理上可观测的后果，确实是一个深刻的陈述。

**无效的对称性**

至此，你可能想知道：是否一切都在所有可想象的方式上都是对称的？不。实际上，有许多可能的对称性是自然界选择不遵守的。

自然界相对于恒定角速度不是对称的，尽管它相对于恒定线速度是对称的。如果一个初始静止的物体后来以恒定角速度旋转，会产生非常明显的可观测变化。角速度存在一个绝对标准。通过使用傅科摆或类似装置，我们可以轻易确定一个物体的角速度何时为零弧度每秒，而无需参考任何外部实体。

此外，自然界不是标度不变的。费曼指出，一个1米宽的钠原子容器辐射波长为589纳米的光，一个10米宽的钠原子容器也辐射相同波长的光，而不是5890纳米。这有很多原因，其中之一是钠原子只有一种尺寸。

费曼提供了另一个标度不变性不成立的例子。有人因用火柴棍粘合建造一座著名大教堂的微型模型而成为新闻人物。如果我们想象将他的模型放大到与真实教堂同等大小，它可能会立即坍塌；木质横梁不够坚固。如果每个维度都放大100倍，每个物体的重量将增加100的立方倍，即100万倍。同时，每根垂直梁的横截面积将增加100的平方倍，即10,000倍。这意味着垂直梁单位面积上的重量增加了100倍。在某个放大系数下，原本坚固的木质结构会因自身重量而垮塌。这就是为什么摩天大楼是用钢材建造的。这也是为什么大象腿骨与鸟类或昆虫腿骨的比例截然不同。

有时标度不变性对大型事物有利。老虎单位质量损失的热量远少于鼩鼱，后者必须不断进食以补偿热量损失。在水中，鲸鱼甚至人类游泳所需的努力远少于细菌，对细菌而言，水似乎像蜂蜜对我们一样粘稠。

最终，自然现象不是标度不变的，因为粒子和原子无法按比例缩放。顺便提一句，一位美国物理学家去日内瓦附近的著名高能研究中心CERN做实验。他知道欧洲人使用公制单位，因此为他的设备图纸准备了所有尺寸的厘米标注。他不知道欧洲的工程图纸全部使用毫米。最终，CERN机械车间交付了他原意设计的十分之一尺寸模型，并附了一张便条，说明工作延迟是因为他没有使用标准螺丝尺寸。他们根据他不正确的图纸手工精密加工了每一颗螺丝。实验被延迟了，但这个模型堪称一件艺术品。

perhaps reflecting the heritage of Swiss watchmaking.

Is Time Reversal Symmetric? Does reversing the "arrow of time", by playing a video backwards for example, result in any violations of natural laws? Are the laws of nature equally satisfied by the actions we observe regardless of whether the video is played forward or backward?

From everyday experience the answer seems to be obvious: time reversal is not a symmetry of nature. Imagine a video of a decanter of wine falling off a table and crashing onto the carpet, shattering the decanter and splattering the wine. The reversed video shows wine un-soaking from the carpet, glass fragments and wine droplets flying together to form a decanter that fills with wine and jumps upward back onto the table. How ridiculous!

Yet, at an atomic level, (almost) all the laws of nature are precisely time-reversal-invariant. Time reversal is a symmetry of nature at its fundamental level. If we examine the microscopic motions shown in the reversed video, each atom's actions would be entirely consistent with all natural laws, including the conservation of energy and momentum as well as Newton's laws of motion. (I said "almost" because of certain weak force interactions that we will discuss later and that are beyond everyday experience.)

Why the stark distinction between the obvious irreversibility of time macroscopically, and the fundamental reversibility of time microscopically? While physicists debate the importance of this distinction, it is agreed that the difference is explained by entropy (Chapters 21 and 23). The second law of thermodynamics states that entropy increases in all irreversible processes (all macroscopic processes are irreversible). Entropy thus distinguishes forward and backward time: entropy grows as time runs forward, and diminishes as time runs backward. The "arrow of time" points toward greater entropy.

Recall that thermodynamics describes the large-scale properties — temperature, pressure, entropy, etc. — of systems with vast numbers of atoms. Individual atoms do not have a definable pressure, only vast collections of atoms do. The laws of thermodynamics, including the second law, are statements about what's probable. The probability of a system's entropy decreasing isn't exactly zero, but it does drop exponentially with the number of particles in that system. For a system of 10^20 particles, the probability of the system's entropy decreasing is absurdly small. One atom of wine might bounce off the carpet and land back on top of the table, but an entire decanter filled with wine will not — not in a trillion times the age of the universe.

Thus the "arrow of time" is important but is not as fundamental as the conservation of electric charge. We believe electric charge is conserved always, everywhere, and in every possible interaction — no ifs, ands, ors, or buts. By comparison, the "arrow of time" is very well defined in large enough systems, but is meaningless at the fundamental level, where nature is (almost) completely symmetric with respect to time reversal.

Symmetry & Conservation Laws

The symmetries of natural laws have profound consequences. As Feynman says in V1p52-3: "A fact that most physicists still find somewhat staggering, a most profound and beautiful thing, is that, in quantum mechanics, for each of the rules of symmetry there is a corresponding conservation law."

This profound principle is named Noether's theorem for the famed mathematician Amalie Emmy Noether. Her theorem actually does apply in Newtonian physics as well as in modern physics. In quantum mechanics, Noether's theorem becomes more expansive, as we will discover later in this course. The proof of Noether's theorem isn't overly complex, but requires introducing more mathematics than is merited at this point.

Examples of Noether's theorem are:

1. Translation symmetry in the x-direction implies the conservation of the x-component of momentum. Similarly for y and z.

## 2. Spatial rotational symmetry implies the conservation of angular momentum

## 3. Translation symmetry in time implies the conservation of energy

An example from quantum mechanics is invariance under a change of phase angle. In quantum mechanics, physical observables are determined by the squares of the magnitudes of probability amplitudes: Prob(A) = |Ψ(A)|^2. Shifting the phase of all probability amplitudes by a constant angle θ has no observable effect: |Ψ(A)exp{iθ}|^2 = |Ψ(A)|^2 |exp{iθ}|^2 = |Ψ(A)|^2.

Feynman says: "The conservation law which is connected with the quantum-mechanical phase seems to be the conservation of electrical charge. This is altogether a very interesting business!"

Spatial Reflection

Spatial reflection is the process of inverting one spatial dimension, such as replacing x with –x. Spatial reflection is the same as substituting one phenomenon with its mirror image.

In V1p52-4, Feynman considers two identical clocks, physical clocks made of real gears and so forth, but with one being the exact mirror image of the other.

of the other — all the parts in clock L are the mirror image, and are assembled in the mirror image fashion, to those of clock R. So while clock R runs clockwise, clock L runs counterclockwise. If we start both clocks at the same time, will they forever keep the same time? That seems reasonable. We can think of no reason why they shouldn’t keep the same time (with their hands moving in opposite directions). But do they?

Let’s assume for now that the clocks do run identically. If so, they could not be used to distinguish “right” from “left” by any purely physical means. If we sent both clocks to a scientist on Mars who is unfamiliar with “right” and “left”, nothing we could say would help him identify which clock is “left.”

Feynman suggests we look to nature for phenomena that might possibly be fundamentally right-handed or left-handed, phenomena with distinct chirality. Many complex molecules have left-handed and right-handed versions. In Chapter 33, we discussed optical activity, the ability of a molecule to rotate the polarization of light. Right-handed molecules rotate light’s polarization counterclockwise when viewed along light’s velocity vector. Left-handed molecules rotate the polarization clockwise.

The form in which I’ve defined the rotation direction is observer-independent: from every vantage point, the polarization rotates about the velocity vector in the same manner. This invariant definition is how particle physicists describe the spin of elementary particles. However, optical activity was originally analyzed by looking at light that had passed through a liquid of chiral molecules. Here the observer’s line of sight is anti-parallel to light’s velocity vector (light is coming toward the observer). In this specific observer orientation, the polarization rotation direction is reversed: right-hand molecules rotate polarization clockwise. This observer-specific definition is standard in chemistry.

In some cases, both chiralities of a given molecule occur with equal abundance; those can’t help us define “right” and “left.” However, it turns out that some molecules occur predominately or entirely in one chirality. For example, all organically produced protein molecules are left-handed, and all organically produced sugar molecules are right-handed.

In V1p52-5, Feynman relates an amusing scenario. A solution of organically produced sugar molecules (all right-handed) rotates light polarization clockwise. A solution of the same sugar molecules produced artificially (equally right- and left-handed) does not rotate light’s polarization. But bacteria added to this solution will eat half the sugar (the right-handed half), after which the remaining sugar molecules (now all left-handed) rotate light’s polarization clockwise with respect to light’s velocity vector. He says: “It seems very confusing, but is easily explained.”

Biochemists can easily produce the opposite-handed versions of such molecules. These opposite versions are chemical equivalent to the naturally occurring versions. Detailed analysis shows both have the same energy levels, chemical reaction rates, and in purely artificial reactions (using no organic compounds) equal numbers of both chiralities are produced.

Yet, all life on Earth uses only one chirality. Scientists believe this is evidence that life on Earth had one common origin that by random chance selected the chiralities that all subsequent life employs. Feynman muses that if we were able to construct a frog with all its molecules of the opposite chirality, call it a left-hand frog, it would function like any real right-hand frog. The only problem is that our frog wouldn’t find any left-hand food. Earth has only right-hand flies that he can’t digest.

Thus, we could tell our Martian scientist that “left” is the direction in which his DNA spirals. That would work if life on Mars had a common origin with life on Earth. If not, the odds are 50-50 that a completely independent life form has our chirality.

The chirality of molecules, therefore, is not fundamentally one-handed. As a universal rule, chemical processes seem left/right symmetric.

Reflection of Vectors & Vector Equations

In V1p52-6, Feynman explores some subtleties associated with the mirror reflection of vectors and equations involving vectors. The essential point here is that not all of the vectors that physicists employ have the same reflection properties. Vectors belong to two distinct categories: polar and axial.

Polar vectors are simpler and more familiar. Shown in Figure 49-1 are examples of polar vectors: the vector AW from point A to point W; and the vector from the origin of a coordinate system to point T.

Figure 49-1 Mirror Reflection of Polar Vectors

Polar vectors change under reflection; if the mirror lies in the yz-plane, just the x-component of a polar vector changes sign under reflection. Other polar vectors include: velocity, acceleration, momentum, and force.

Axial vectors, often called pseudovectors, are more The complex. Consider the example of a disk spinning in the yz-plane. The velocity of each atom in the disk lies entirely within the yz-plane; nothing is moving in the x-direction. Yet, we define the angular velocity ω and the angular momentum L as vectors that are parallel to the x-axis (see Chapters 39 and 41).

We can define axial vectors this way because, in three dimensions, every plane defines a direction perpendicular to its surface. Motion entirely within the yz-plane identifies x as a special direction: only lines parallel to the x-axis are perpendicular to the plane in which the motion occurs. Mathematically, the perpendicular to a plane is given by the cross product of two non-parallel vectors that lie entirely within that plane.

Unlike polar vectors, axial vectors are defined with cross products that explicitly employ the right-hand rule.

In V1p52-7, Feynman uses the right-hand rule in one paragraph and the left-hand rule in another paragraph, without being as clear about this as he might be. I will be more explicit.

The angular velocity vector is a typical axial vector, with a cross product whose sign is set by convention according to the right-hand rule: ω = v × r Writing out all the components of this vector equation yields three equations (right-hand rule): ωx = +vy r_z – vz r_y ωy = +vz r_x – vx r_z ωz = +vx r_y – vy r_x

Exchanging x with –x changes vx to –vx, and r_x to –r_x. The resultant ω, call it ω*, is (in the right-hand rule): ω*_x = +vy r_z – vz r_y ω*_y = +vz (–r_x) – (–vx) r_z ω*_z = +(–vx) r_y – vy (–r_x)

ω*_x = +ω_x ω*_y = –ω_y ω*_z = –ω_z

We see that the sign changes in axial vectors are opposite to those of polar vectors. For a reflection of the x-axis (a mirror in the yz-plane), the sign changes are in a polar vector’s x-component and an axial vector’s y- and z-components.

This is illustrated in Figure 49-2; note that ω changes sign when it is parallel to the mirror and not when it is perpendicular to it.

Figure 49-2 Mirror Reflection of Axial Vectors

Above, we just reversed the x-axis. If we instead switched from a right-handed universe to a left-handed universe, every “right” would be replaced by a “left.” In addition to reversing the x-axis, we would also need to switch to the left-hand rule. That would reverse the sign of the cross product, inverting the sign of every component of ω*. Reversing x and using the left-hand rule yields ω**: ω**_x = –vy r_z + vz r_y ω**_y = –vz (–r_x) + (–vx) r_z ω**_z = –(–vx) r_y + vy (–r_x)

ω**_x = –ω*_x ω**_y = –ω*_y ω**_z = –ω*_z ω**_x = –ω_x ω**_y = +ω_y ω**_z = +ω_z

Upon reversing x and using the left-hand rule, axial vectors change the same way that polar vectors do: only the x-components change sign.

Let’s consider another example, an electric charge moving in a magnetic field. We will thoroughly explore electromagnetism later in this course. For now, know that magnetic fields are created by moving electric charges. A bar of iron wrapped with a current-carrying wire makes a simple magnet. By convention, we draw magnetic field lines B emanating from a magnet’s north pole and converging on its south pole. The Lorentz force F exerted by such a magnet on an electron with charge q (q<0) and velocity v is: F = qv × B

According to the right-hand rule, for electron velocity v in the –z-direction (going into the screen) and a magnetic field B pointed in the +y direction (up), force F points in the –x-direction (left), as shown on the left side of Figure 49-3. The arrows on the wires wrapping the bar magnets indicate the direction of electrical current flow.

Figure 49-3 Mirror Reflection of Magnet and Force F on an Electron Moving Into the Screen

The right side of the figure is the mirror image of the left side. In the mirror image, note that the electrical current flow is reversed. This reverses the magnet’s north and south poles, making the magnetic field B point in the opposite direction (down). The electron’s velocity v does not reverse, because it is a polar vector parallel to the mirror (going into the screen). By the right-hand rule, force F reverses direction and points toward +x (right).

Feynman urges us to ignore all the labels for a moment and focus on the physical actions. Electrons in the wire create a magnetic field that exerts a force on another electron. It makes sense that if we reverse the direction of the electrons in the wire, the force they exert will also reverse. Note that this is true only if we use the right-hand rule in both cases; we do not change hands when analyzing a mirror image. (If you are going to think of this in terms of what electrons in the wire do to a free electron, be aware that electrical current flow is defined as the direction of flow of positive charge. The wire’s electrons flow in the opposite direction. Benjamin Franklin defined the polarity of electrical current, and unfortunately he guessed wrong.)

Can We Tell Right from Left?

So far we have not identified any fundamental natural process that distingu distishes left from right. It seems every natural process and its mirror image have exactly the same characteristics. There is no experiment we can perform (at least so far) whose result will always be left. Without providing a physical object or an image labeled “left/right”, we seem unable to explain to a Martian physicist what we mean by “left.” Indeed, after extensive observation, physicists are highly confident that three of nature’s forces — gravity, electromagnetism, and the strong nuclear force — obey reflection symmetry; they are completely left-right invariant.

This leaves only the weak force, often a non-conformist. Weak force interactions are rich in exotic phenomena because they exclude the vastly more common “normal” phenomena that occur in strong and electromagnetic interactions.

In one of the major advances of 20th century physics, particle physicists proved the weak force is not symmetric under spatial reflection. Frank Yang and T. D. Lee provided the theoretical direction and Madame Wu led the experiment that proved parity violation in weak force interactions. In 1957, Yang and Lee, but quite remarkably not Wu, were awarded the Nobel Prize for this discovery. Wu was however awarded the first Wolfe Prize in Physics in 1978, and became the first female president of the American Physical Society.

Along those lines, Madame Wu often spoke about the paucity of women scientists in America. She said: " ... it is shameful that there are so few women in science... In China there are many, many women in physics. There is a misconception in America that women scientists are all dowdy spinsters. This is the fault of men. In Chinese society, a woman is valued for what she is, and men encourage her to accomplishments — yet she remains eternally feminine."

Much of what follows explores intriguing aspects of quantum particle physics for which we have not given you an adequate background. Read it to get a feeling for what modern physics is all about. If you can’t understand some parts, don’t be discouraged. There is much left to learn before it will all make sense. Feynman always believed that students should be exposed to more than they can digest in order to give them something more than mere facts: a sense of why learning physics is worth their effort.

In quantum particle physics, reflection symmetry is characterized by the term parity, and denoted by the symbol P. If a system undergoes spatial reflection (x is replaced by –x), its probability amplitude is multiplied by exp{iø}. After two reflections, the amplitude has been multiplied by that factor squared. But two reflections restore the system to its original state. Therefore: [exp{iø}]2 = 1, exp{iø} = ±1. Both alternatives exist in nature (in quantum mechanics they almost always do). Systems with a reflection factor of +1 are said to have positive parity or even parity, while those with –1 have negative parity or odd parity. Each type of particle has its own intrinsic parity. Protons, neutrons, and electrons all have parity P=+1. The pion has parity P=–1.

Parity & The Tau-Theta Puzzle Based on macro-world experience, physicists had long assumed that all nature’s forces were fundamentally reflection-invariant. In particle physics terms this means parity must be conserved in any interaction: if the parity of a system is initially even (odd), it must remain even (odd) after any interaction.

This belief was seriously questioned for the first time in the 1950’s due to observations of the decays of two recently discovered particles, the tau and the theta. Both particles decayed very slowly via the weak force. (They decayed in billionths of a second; strong force decays occur in trillionths of a trillionth of a second.) The theta decayed to two pions, so its parity had to be P=(–1)2=+1. The tau decayed to three pions, so its parity had to be P=(–1)3=–1. The problem was: the tau and theta had the same mass and the same lifetime. It was ultimately recognized the tau and theta were in fact the same particle, which we now call the kaon. The kaon could not have both even and odd parity, so something was clearly wrong in the current thinking.

Yang and Lee showed that no one had yet really tested parity conservation in weak force interactions. Encouraged by Lee, Madame Wu observed radioactive cobalt decays in a strong magnetic field. At extremely low temperatures, cobalt atoms align with the magnetic field before decaying and emitting electrons. This experiment observed the electrons preferentially traveling toward the magnet’s north pole.

That result violates reflection symmetry. Let the magnetic field B initially point toward +z. Electrons move toward the magnets’ north pole, toward –z. Now reverse the x-axis (x is replaced by –x). The current in the magnets’ coils reverses direction, B reverses direction, and electrons moving toward the magnet’s north pole must go toward +z. But since we didn’t invert the z-axis, electrons originally moving toward –z are also moving toward –z in the mirror world, which is different from the experimental result.

toward -z in the mirror image. Since the experiment showed that electrons always move toward the north pole, the mirror image reaction is impossible. Madame Wu’s experiment proved parity is not always conserved in weak interactions. This allows negative parity kaons to decay to both positive and negative parity states. Now, we can tell our Martian friend which way is “right.” If he runs the Wu experiment and the electrons go down (toward the center of Mars), the electric current is flowing clockwise (as viewed looking upward along B). If you remember the old analog clocks, as a clock’s second hand passes the top, it is moving toward the right. Alternatively, the angular velocity vector points away from you when you look perpendicular to the plane of clockwise motion, provided you use the right-hand rule. Parity violation was an unwelcome shock that forced substantial revisions to physical theories. Physicists scrutinized all other known symmetries to determine if they were violated under any conditions. This became a major field of research. The weak interaction is now understood as mediated by intermediate vector bosons (particles with spin 1) that combine both polar and axial vectors in equal measures. The polar vector has even parity while the axial vector has odd parity. In the center of mass of decays involving the weak force, electrons, neutrinos, and similar particles always have left-hand circularly polarized spin, while antielectrons and antineutrinos always have right-hand circularly polarized spin. (We discussed circular polarization of photons in Chapter 36.)

Antimatter: The list of symmetries at the start of this chapter included symmetry under the exchange of matter and antimatter. In 1931, P. A. M. Dirac predicted the existence of antimatter on the basis of symmetries in the equations of quantum mechanics. The antielectron, also called the positron, was discovered in 1932. The antiproton was discovered in 1955, and the antineutron in 1956. By now, the antiparticles of all fermions have been discovered. Bosons are their own antiparticles. In V1p52-10, Feynman muses that one day physicists could make anti-atoms. It took 40 years, but antihydrogen was produced in 2002. While important for research, no one should get excited about antimatter-powered spaceships. At full capacity, CERN can produce 10 million antiprotons per minute. If 100% of those are successfully combined with positrons producing antihydrogen, they could reach 1 gram of antihydrogen in about 100 billion years. Antiparticles have the same mass and spin as their particle namesakes, but they have the opposite electric charge and other quantum numbers. Quantum numbers are the defining characteristics of particles. As a result, if a particle and its antiparticle are combined, the net sum of all quantum numbers is zero, leaving their mass-energy as the only non-cancelling quantity. Such pairs annihilate: they cease to exist and their mass-energies are converted into radiation or other particles. Such annihilations are absolute and total: no traces of the original particles remain. When Feynman gave his lectures, the laws of nature appeared indifferent to whether particles are made of matter or antimatter. In physics jargon: natural laws appeared symmetric under CP symmetry, matter/antimatter exchange; or equivalently, the laws are CP-invariant. CP is the combined symmetry of two operations: spatial reflection P, and charge conjugation C. Charge conjugation means inverting the polarity of all electric charges. Since C and P are independent operators, the order of operations is irrelevant: CP=PC. Also note that CC=PP=1, as each switches back and forth between two states. Fundamental principles of quantum theory state that CP is equivalent to exchanging matter and antimatter. We now know that gravity, electromagnetism, and strong nuclear interactions are invariant under the three symmetries: P, C, and CP. The weak force is a different story once again. Consider building 4 clocks. Build Clock1 from normal matter. Make Clock2 the mirror image of Clock1, also from normal matter. Build Clock3 just like Clock1, but from antimatter. Finally, make the Clock4 the mirror image of Clock3, also from antimatter. Thus, we can represent the relationships as: Clock2 = P(Clock1); Clock3 = C(Clock1); Clock4 = P(Clock3)= CP(Clock1); Clock3 = CPP(Clock1) = CP(Clock2). If the time-keeping mechanisms of these clocks depended on any combination of gravitational, strong, and electromagnetic forces, all four clocks would keep exactly the same time. But, if the clock timing is determined by a weak force process, such as cobalt decay, the four clocks will not all keep the same time. Since weak force interactions violate parity conservation, we know that Clock2 need not operate identically to Clock1. That correctly leads us to suspect that Clock4 need not operate identically to Clock3. What about the other two pairings? If CP is a valid symmetry of the weak force, Clock Clock4 will operate identically to Clock1, and Clock3 will operate identically to Clock2.

At the time of the Feynman Lectures, the available evidence was consistent with CP being a valid symmetry of the weak force. This provided some relief to physicists. They had lost parity as a universal symmetry, but at least they still had CP.

In V1p52-11, Feynman highlights an implicit assumption we made earlier. When we gave our Martian friend instructions on how to identify “right”, we assumed he is made of matter, just like us. If we eventually build spaceships and meet in empty space, midway between Earth and Mars, we should take care as we rush to greet one another. Feynman says: “if he puts out his left hand, watch out!” If our Martian friend were made of antimatter and if the weak force respects CP-symmetry, antielectrons in his Madame Wu experiment built of antimatter would head for the anti-magnet’s south poles, and his “right” would be our “left.”

This is all just in fun. After landing numerous JPL spacecraft on Mars, we are sure it isn’t made of antimatter.

In fact, precise astronomical observations with the Fermi Gamma-ray Space Telescope (FGST) fail to show any substantial concentrations of antimatter anywhere in the universe. Some few antiparticles are continually created by high-energy events, but there is no evidence for antimatter stars in antimatter galaxies.

Our understanding of symmetries changed again in 1964, when James Cronin and Val Fitch announced observations of CP-violation in hadronic kaon decays (kaons decaying to pions). For this work, they were awarded the Nobel Prize. In 1971, my own thesis experiment showed that CP is also violated in leptonic kaon decays (decays that include muons).

While parity violation is a 100% effect (neutrinos are all left-handed), CP violation is only a 0.3% effect, making it much harder to study.

Physicists have no meaningful explanation for why the weak force should violate P, C, or CP. We just know that it does, and that this is a very good thing indeed.

The Big Bang almost certainly created equal amounts of matter and antimatter. Within the first one second of cosmic existence, CP-violating processes had made matter slightly more abundant than antimatter. Essentially all antimatter particles then annihilated with corresponding matter particles, releasing a fabulous amount of light that we now call the Cosmic Microwave Background radiation. Only the slight excess of matter, one part per billion, survived to form all the stars and planets that exist today. Without CP-violation the universe would be empty. There wouldn’t even be a physics book anywhere to explain why.

CPT Symmetry This section supplements the Feynman Lectures. As quantum theory shows, CPT symmetry is one of the most fundamental principles in physics. This is the combined symmetry of C (exchanging positive and negative charges), P (spatial reflection), and T (time reversal). As mentioned earlier, CP is equivalent to exchanging matter and antimatter.

CPT is an exact symmetry of all physical interactions. CPT symmetry says that any process involving particles moving forward in time can occur identically with antiparticles moving backward in time. Based on CPT symmetry, Feynman said that perhaps antielectrons were nothing other than electrons going backwards in time. Indeed, his famous Feynman diagrams make that assumption.

Given that CPT symmetry is universal and exact, a violation of CP symmetry implies a violation of T, time reversal symmetry. But, while CP violation were observed in weak interactions 50 years ago, time reversal symmetry violations have never been observed in any fundamental interaction. Physicists believe this is due to experimental challenges, rather than lack of T violation.

Broken Symmetries In V1p52-11, Feynman says: “The marvelous thing about it is that…over a wide range of important phenomena — over a tremendous range of physics, all the laws … seem to be symmetrical. On the other hand, this little extra piece says, ‘No, the laws are not symmetrical!’ How is it that nature can be almost symmetrical, but not perfectly symmetrical? What shall we make of this? ” Feynman notes that humans tend to equate symmetry with beauty and perfection. He reminds us that the ancient Greeks were so enthralled by the perfection of circles that they insisted that planetary orbits had to be circular. The understanding and acceptance that orbits are actually elliptical was a major advance in science. But that advance gave scientists a lot to explain. If orbits were exactly circular, the explanation is simple: they’re perfect. Explaining why orbits are nearly circular is much more complex.

Feynman ends the first year course saying: “So our problem is to explain where symmetry comes from. Why is nature so nearly symmetrical? No one has any idea why.” Fifty years later, we still lack a convincing explanation. Perhaps you will have the brilliant idea that we all await.

## Chapter 49 Review: Key Ideas

1.

The following symmetry processes are universally valid.

Translation in Space, Translation in Time, Spatial Rotation, Motion at Constant Velocity, Exchange of Identical Particles, Change of Quantum Phase, CPT Symmetry.

The following symmetry processes are valid for all but the weak interaction.

Spatial Reflection, parity P; Time Reversal, T; Exchange of Matter & Antimatter, CP.

Noether’s theorem states that for each symmetry there is a corresponding conservation law.

Translation in space corresponds to conservation of momentum.

Translation in time corresponds to conservation of energy.

Time is obviously irreversible macroscopically (try reassembling a broken egg), but the fundamental laws of nature are completely reversible microscopically (excluding the weak force). The difference is explained by entropy.

The second law of thermodynamics states entropy increases in all macroscopic processes, thus distinguishing forward and backward time. The “arrow of time” points toward greater entropy.

Thermodynamics describes the large-scale properties of vast numbers of atoms; its laws are statements about what’s probable. The probability of a system’s entropy decreasing isn’t exactly zero, but it does drop exponentially with the number of particles in that system. The “arrow of time” is important but is not as fundamental as the conservation of electric charge.

Physicists use two types of vectors — polar and axial — that respond differently to spatial reflection.

Polar vectors include: position, velocity, acceleration, momentum, and force.

Axial vectors include: angular velocity, angular momentum, and torque.

Unlike polar vectors, axial vectors are defined with cross products that explicitly employ the right-hand rule. For a reflection of the x-axis (a mirror in the yz-plane), the sign changes are in a polar vector’s x-component and an axial vector’s y- and z-components.

Particle physicists have shown that the strong nuclear force, electromagnetism, and gravity are invariant under the symmetries: P (parity or spatial reflection)

C (charge conjugation)

CP (both C and P, in any order)

Weak force interactions can violate all these symmetries.

Meet The Author Congratulations and thank you for reading my book. I know your time is valuable, and I sincerely hope you enjoyed this experience.

I’d like to tell you something about myself and share some stories.

First, the obligatory bio (as if 3 “tweets”-worth can define anyone): I have a B.S. in physics from Caltech, a Ph.D. in high-energy particle physics from Stanford University, and was on the faculty of Harvard University. Now “retired,” I teach at the Osher Institutes at UCLA and CSUCI, where students honored me as “Teacher of the Year.” In between, I ran eight high-tech companies and hold patents in medical, semiconductor, and energy technologies.

My goal is to help more people appreciate and enjoy science. We all know one doesn’t have to be a world-class musician to appreciate great music — all of us can do that. I believe the same is true for science — everyone can enjoy the exciting discoveries and intriguing mysteries of our universe.

I’ve given 400+ presentations to general audiences of all ages and backgrounds, and have written 3 printed books and 29 eBooks. My books have won national and international competitions, and are among the highest rated physics books on Amazon.com. I’m delighted that two of these recently became the 2nd and 3rd best sellers in their fields.

Richard Feynman was a friend and colleague of my father, Oreste Piccioni, so I knew him well before entering Caltech. On several occasions, Feynman drove from Pasadena to San Diego to sail on our small boat and have dinner at our home. Feynman, my father, my brother and I once went to the movies to see “Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb.” It was particularly poignant watching this movie next to one of the Manhattan Project’s key physicists.

At Caltech I was privileged to learn physics directly from this greatest scientist of our age. I absorbed all I could. His style and enthusiasm were as important as the facts and equations. Top professors typically teach only upper-level graduate classes. But Feynman realized traditional introductory physics didn’t well prepare students for modern physics. He thought even beginners should be exposed to relativity, quantum mechanics, and particles physics. So he created a whole new curriculum and personally taught freshman and sophomore physics in the academic years 1961-62 and 1962-63.

The best students thrived on a cornucopia of exciting frontier science, but many others did not.

Although Caltech may be the world’s most selective science school, about half its elite and eager students drowned in Feynman’s class. Even a classmate, who decades later received the Nobel Prize in Physics, struggled in this class. Feynman once told me that students sometimes gave him the “stink eye” — he added: “Me thinks he didn’t understand angular momentum.” omentum.”

Some mundane factors made the class very tough: Feynman’s book wasn’t written yet; class notes came out many weeks late; and traditional helpers (teaching assistants and upper classmen) didn’t understand physics the way Feynman taught it.

But the biggest problem was that so much challenging material flew by so quickly. Like most elite scientists, Feynman’s teaching mission was to inspire the one or two students who might become leading physicists of the next generation. He said in his preface that he was surprised and delighted that 10% of the class did very well.

My goal is to reach the other 90%.

It’s a great shame that so many had so much difficulty with the original course — there is so much great science to enjoy. I hope to help change that and bring Feynman’s genius to a wider audience. Please let me know how I can make Feynman Simplified even better — contact me through my WEBSITE.

While you’re there, check out my other books and sign-up for my newsletters.

Printed Books, each top-rated by Amazon readers: Everyone's Guide to Atoms, Einstein, and the Universe Can Life Be Merely An Accident?

A World Without Einstein The Everyone's Guide Series of Short eBooks Einstein: His Struggles, and Ultimate Success, plus Special Relativity: 3 Volumes, A to Z General Relativity: 4 Volumes, from Introduction to Differential Topology Quantum Mechanics: 5 Volumes, from Introduction to Entanglement Higgs, Bosons, & Fermions… Introduction to Particle Physics Cosmology Our Universe: 5 Volumes, everything under the Sun Our Place in the Universe: a gentle overview Black Holes, Supernovae & More We are Stardust Searching for Earth 2.0 Smarter Energy Timeless Atoms Science & Faith

Table of Contents

## Chapter 39 Rotation & Angular Momentum

## Chapter 40 Centers & Moments of Rotation

## Chapter 41 Rotations: 3D & Review

## Chapter 42 Physics of Waves & Sound

## Chapter 43 Theory of Beats

## Chapter 44 Modes of Oscillation

## Chapter 45 Harmonics & Fourier Analysis

## Chapter 46 Complex Waves

## Chapter 47 Review of Waves

## Chapter 48 The Physics of Vision

## Chapter 49 Symmetry & Physical Laws

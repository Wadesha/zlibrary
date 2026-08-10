# Feynman Simplified 2A Maxwells Equations Electrostatics Robert L Piccioni Z Library

> 来源文件：pre_Feynman_Simplified_2A_Maxwells_Equations_Electrostatics_Robert_L_Piccioni_Z_Library.txt
> 字符数（约）：293076
> 语言：mix
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Feynman Simplified 2A: Maxwell's Equations & Electrostatics Everyone’s Guide to the Feynman Lectures on Physics by Robert L. Piccioni, Ph.D.

Copyright © 2014 by Robert L. Piccioni Published by Real Science Publishing 3949 Freshwind Circle Westlake Village, CA 91361, USA Edited by Joan Piccioni Visit our web site www.guidetothecosmos.com Everyone’s Guide to the Feynman Lectures on Physics Feynman Simplified gives mere mortals access to the fabled Feynman Lectures on Physics.

This Book Feynman Simplified: 2A covers the first quarter of Volume 2 of The Feynman Lectures on Physics. The topics we explore include: Maxwell’s Equations of Electromagnetism Algebra & Calculus of Vector Fields Gauss’ & Stokes’ Theorems Electrostatics with Conductors & Dielectrics Electrostatic Energy Electricity in the Atmosphere Why The Same Equations Appear Throughout Physics To find out about other eBooks in the Feynman Simplified series, click HERE.

I welcome your comments and suggestions. Please contact me through my WEBSITE.

If you enjoy this eBook please do me the great favor of rating it on Amazon.com or BN.com.

Table of Contents

## Chapter 1: Overview of Electromagnetism

## Chapter 2: Gradient, Divergence & Curl

## Chapter 3: Line, Surface & Volume Integrals

## Chapter 4: Electrostatics

## Chapter 5: Gauss’s Law Applications

## Chapter 6: Dipole Electric Fields

## Chapter 7: Charges & Conductors

## Chapter 8: Electrostatic Energy

## Chapter 9: Electricity in the Atmosphere

## Chapter 10: Dielectric Materials

## Chapter 11: Inside Dielectrics

## Chapter 12: Electrostatic Analogs

## Chapter 13: Review

## Chapter

Overview of Electromagnetism This chapter provides a descriptive overview of electromagnetism.

In V2p1-1, Feynman begins the second year of his introductory physics course by saying: “Consider a force like gravitation which varies predominantly inversely as the square of the distance, but which is about a billion-billion-billion-billion times stronger. And with another difference. There are two kinds of “matter,” which we can call positive and negative. Like kinds repel and unlike kinds attract—unlike gravity where there is only attraction. [Dark energy was unknown 50 years ago.] What would happen?

“A bunch of positives would repel with an enormous force and spread out in all directions. A bunch of negatives would do the same. But an evenly mixed bunch of positives and negatives would do something completely different. The opposite pieces would be pulled together by the enormous attractions. The net result would be that the terrific forces would balance themselves out almost perfectly, by forming tight, fine mixtures of the positive and the negative, and between two separate bunches of such mixtures there would be practically no attraction or repulsion at all.

“There is such a force: the electrical force. And all matter is a mixture of positive protons and negative electrons which are attracting and repelling with this great force. So perfect is the balance, however, that when you stand near someone else you don’t feel any force at all. If there were even a little bit of unbalance you would know it. If you were standing at arm’s length from someone and each of you had one percent more electrons than protons, the repelling force would be incredible. How great? Enough to lift the Empire State Building? No! To lift Mount Everest? No! The repulsion would be enough to lift a “weight” equal to that of the entire earth!” The enormously strong electric force is responsible for most of the properties of matter that we observe. The electric force determines the structure of atoms and molecules, which in turn determine the large-scale characteristics of matter. An example, Feynman says, is the stiffness of the Empire State Building: its atoms are so tightly held in position by electric forces that it bends only 1 part in 10,000 in a 110 mph wind. (Height 1250 feet = 381 m; sway 1.5 inches = 3.8 cm; 110 mph = 176 k/h). [Some taller and more modern buildings sway much more. The world’s tallest building, the 2717-foot (828m) Burji Khalifa in Dubai, sways up to 5 feet (1.5m). If you stay there, try not to get seasick!]

The electric forces that give matter strength and rigidity arise because positive and negative charges are generally not precisely balanced everywhere on an atomic scale. A slight excess positive charge on one atom binds it tightly to another with a slight excess negative charge. Even atoms and molecules that are electrically neutral can have intrinsic or induced electric dipole moments, a displacement of the center of positive charge from the center of negative charge. Such dipoles exert powerful electric forces.

Since atoms are made of positively charged protons and negatively charged electrons, Feynman says you might ask: “If this electric force is so terrific, why don’t the protons and electrons just get on top of each other?” Why don’t they reduce their separation to zero? Quantum mechanics provides the answer. The Uncertainty Principle says that trying to confine an electron within a very small space inevitably increases its mean square momentum, making it impossible to keep the electron in that space. We will thoroughly explore this in Feynman Simplified 3A.

Feynman says your next question might be: “What holds the nucleus together?” Since all protons have a positive charge, why don’t nuclei with multiple protons fly apart? The answer is the strong nuclear force. For separations less than the diameter of a proton, the strong force is about 100 times stronger than the electric force. This means protons and neutrons very strongly attract one another if they are adjacent. For larger nuclei, the total strong force attraction grows linearly with the total number of protons and neutrons. By contrast, the electric force repulsion grows nearly quadratically with the number of protons. For large enough nuclei, the electric repulsion finally exceeds the nuclear attraction, and those nuclei fall apart.

Feynman says a third interesting question is: “What holds an electron together?” Electrons do not participate in the strong nuclear force, which sometimes overpowers the electric force. If an electron is a ball of “stuff” all of which has a negative charge, why doesn’t an electron’s left side push its right side away? Maybe, Feynman says, an electron doesn’t have “parts”. Maybe, an electron is a single point object, and maybe, he says: “electrical forces only act between different point charges, so that the electron does not act upon itself. Perhaps. All we can say is that the question of what holds the electron together has produced many difficulties in the attempts to form a complete theory of electromagnetism. The question has never been answered. We will entertain ourselves by discussing this subject more in later chapters.”

Electric forces and quantum rules combine in complex ways to determine the properties of matter. They determine which materials are hard, which are soft, which conduct electricity, and which do not. We will explore the most interesting of these phenomena in subsequent chapters. For now, we begin with the simplest challenges: the basic laws of electricity and magnetism.

The Lorentz Force We said earlier that the electric force acts predominantly, as does gravity, as an inverse-square law: the force F is proportional to 1/r2, where r is the distance between the interacting objects. Einstein’s theory of general relativity shows that gravity deviates from a pure 1/r2 dependence for large masses and short distances. The electric force also deviates from a pure 1/r2 dependence when electric charges are moving.

But regardless of the complexity of charges and motions, their combined effect can be represented by two vector fields: E the electric field, and B the magnetic field. From those fields, the force F on a body with charge q and velocity v is always given by a simple rule, the Lorentz force law: F = q(E + v×B). Here, both fields are evaluated at the location of the body. In general, E and B vary with position and time.

From Volume 1, we know how to calculate a body’s motion in response to any force F: d (γmv) /dt = F = q(E + v×B). Here, γ2=1/(1–v2/c2) is the usual relativistic factor that approaches 1 for velocities much less than c, the speed of light.

Linear Superposition of Fields In V2p1-3, Feynman says one of the most important principles of electromagnetism is linear superposition. This principles says that if there are two sets of arbitrary charges with arbitrary motions, and if set #1 produces fields E1 and B1, while set #2 produces fields E2 and B2, the fields produced by the sum of both sets of charges are the vector sums: E = E1 + E2, B = B1 + B2. One consequence of this principle is that if we know the E and B fields produced by a charge q with an arbitrary motion, we can calculate the E and B fields produced by any collection of charges. We would calculate the fields from each charge and sum them linearly.

Unfortunately, this is more difficult than it might sound. From Feynman Simplified 1C Chapter 32, the equations for the fields are: E = –q/(4πε){r/r3 +(r/c)d(r/r3)/dt +d2(r/r)/dt2/c2}, B = –r×E/rc. Here r is the “apparent location” of the charge, accounting for delays due to the finite speed of light. These equations are simple only when all charges are stationary.

Feynman says he will present a more convenient approach, one in which “the laws of electrodynamics appear to be the most easily manageable.”

Electric & Magnetic Fields In V2p1-3, Feynman explains that we should understand that the electric field E and the magnetic field B exist even if there are no charges present on which the fields can act. We have previously described fields in terms of how they exert forces on electric charges, but these fields are real entities in their own right, whether or not charges are present. We should think of these fields as vector quantities that 电场和磁场与每个时空事件 (x,y,z,t)、空间中的每个位置以及每个时刻都相关联。正如费曼所说，这些场决定了：“在时刻 t，位于 (x,y,z) 处的一个电荷所受的力，前提是放置这个电荷不会扰动产生这些场的所有其他电荷的位置或运动。”可以说，场决定了具有无穷小电荷（即电荷小到不会扰动任何其他事物）的物体所受的力。

我们可能会认为 E 和 B 包含六个 (x,y,z,t) 的函数，E 的三个分量各有一个函数，B 的三个分量各有一个函数。一种更数学化的方法——也是我们这门课程将要采用的方法——是将 E 和 B 视为两个向量场，它们都是 (x,y,z,t) 的函数。这里，“场”仅仅指一个函数，它在时空的不同事件处有不同的值；而“向量”意味着它在每个事件处的值是一个三维向量，例如 (Ex, Ey, Ez) 或 (Bx, By, Bz)。

让我们考虑两个场的例子。T(x,y,z,t) 可以表示整个地球大气层中随位置和时间变化的温度。T 是一个标量场，“标量”表示其值是简单的数字，例如 98.6ºF、100ºC 或 2.73K。相比之下，W(x,y,z,t) 可以表示地球大气层中每个 (x,y,z,t) 处的风速。风具有速度和方向，用一个三分量的速度向量来表示。W(x,y,z,t) 是一个向量场。

一个有趣的向量场的图形表示如图 1-1 所示。这里，每个箭头表示 xy 平面上一系列点处的向量值。

像所有其他向量一样，向量场的值可以用沿每个轴的坐标来表示，也可以用一个方向和一个大小来表示——分别对应箭头所指的方向和箭头的长度。在图 1-1 中，向量场的大小在图案的边缘比在中心附近要大得多，而该中心位于图像中心的右上方。

图 1-2 展示了向量场的另一种图形表示，即使用场线。场线是由上面使用的箭头延伸并融合在一起而形成的。每条场线都与其路径上的所有箭头平行，因此清晰地表示了向量场在每个点的方向。场值的大小由场线的密度表示。在向量场强的地方，即其值的大小最大的地方，场线密集排列。在场弱的地方，场线稀疏。图 1-2 描绘了一根条形磁铁的场线，其中 N 和 S 表示其北极和南极。

正如我们之前所见，运动电荷产生的电场和磁场的方程相当复杂。在《费曼物理学讲义》第二卷第一章第四节中，费曼解释说，电磁学“最容易处理”的方法是利用 E 场和 B 场本身的值之间的关系。E 和 B 受场方程支配，这些方程规定了场如何从一个点变化到下一个点，以及它们如何随时间变化。场方程比我们之前看到的方程更简单。

向量场

本节将研究向量场的两个重要性质：散度和旋度。我们将首先描述散度，然后再讨论旋度。

想象一个封闭的表面，比如一个球体，它包围了一个三维体积。（由二维球体包围的三维体积称为一个球。）现在加入一个向量场。图 1-3 显示了球体表面上各点的向量场箭头。如果向量场代表某种流体（如水或空气）的流动，我们可能想知道该流体是流入还是流出球体。

我们从图 1-3 中看到，靠近球体南北两极的箭头似乎平贴在表面上。看起来流体正从两极流出，沿着表面流向赤道。但是，我们也看到在赤道附近箭头是向外指的，表示流体正离开球体，远离原点 x=y=z=0。

是否通过表面有流动取决于表面上每个点处向量场的法向分量。也就是说，在球体上的每个点，向量是否有垂直于表面的分量；是否有任何部分突出或进入表面？如果每个箭头都完全位于表面内，则没有向内或向外的净流动。如果每个箭头都突出表面，则流体向外流动。

对于任何小面积 A，通过 A 的净流量等于（A 上向量场法向分量的平均值）乘以 A。我们称单位时间内的净流量为流过 A 的通量。用数学公式表示为： 通量 = (法向分量的平均值)

component) × A The net flow through the entire sphere equals the integral of the normal component of the vector field across the sphere, or equivalently, the average of the normal component times the area of the sphere. If the net flow is outward, we say the field has a positive divergence. If the net flow is inward, it has a negative divergence.

By analogy, we define the flux of electric or magnetic fields through any small area A as (the average value of the field normal to A) multiplied by A. We can then integrate that flux over any large surface of interest, whether the surface is closed or not.

The second important property of a vector field is whether or not it has a net rotation. Figure 1-4 shows a vector field with a completely symmetric rotation. This is a special case. In general, rotations can be irregular.

Figure 1-4 Circulating Vector Field by Allen McC

If this vector field represents fluid flow, we might consider immersing an imaginary tube and watching fluid circulate through it, as in Figure 1-5.

Figure 1-5 Fluid Circulating in Tube

The tube could have any arbitrary shape, but for simplicity we have chosen a circular shape, like a bicycle tire, aligned with the fluid’s symmetry. For a tube of constant cross-section and total length L, Feynman defines a vector field’s circulation as: Circulation=(average tangential component)×L

Here, we calculate the component of the field’s vector that is parallel to the tube’s axis, average that throughout the tube’s volume, and finally multiply by L. For a very narrow tube, this is equivalent to integrating the tangential component of the vector field along the entire tube length L.

Circulation corresponding to the right hand rule is called a positive curl, while the opposite circulation is called a negative curl.

Flux and circulation are sufficient to describe the equations for all electric and magnetic fields.

Laws of Electromagnetism

Let V be any volume enclosed by a closed surface S. Applying our flux concept to the vector fields E and B yields: (1) Flux of E through S = (Net charge within V)/ε (2) Flux of B through S = 0

Now let S be any open surface (one that is not closed), and let C be the curve that is the boundary of S. For a water glass, for example, S consists of the side and bottom surfaces, and C is the brim. The concept of circulation yields: (3) (Circulation of E around C) = d/dt (flux of B through S)

(4) (Circulation of B around C)•c2 = d/dt (flux of E through S) + (flux of electric current through S)/ε

Here c is the speed of light and ε (epsilon-zero) is a constant called the vacuum permittivity, a name that may not be worth remembering. As Feynman often said, the ideas are important, the names are not.

These equations show that electric fields arise from both static and dynamic sources: from electric charges according to the first equation; and from changing magnetic fields according to the third equation. Magnetic fields arise only dynamically: from changing electric fields and from currents (moving electric charges), both according to the fourth equation.

According to the second equation, nature contains no magnetic monopoles; there is no magnetic equivalent of a single electric charge. Some theories speculate that magnetic monopoles might have existed at the beginning of our universe, but intensive searches indicate that none exist today. We never find a magnetic north pole without an associated south pole.

The above four equations, in their proper mathematical form, combined with the Lorentz force equation are all the fundamental equations of electromagnetism. The remainder of Volume 2 is devoted to exploring the “elaborate” consequences of these equations.

Field Interaction Examples

Feynman illustrates some simple examples of the interactions of electric and magnetic fields described by the electromagnetic equations.

The first demonstration consists of a current j flowing through a wire suspended above a bar magnet, as shown in Figure 1-6.

Figure 1-6 Wire with Current j near Magnet

One sign convention of electromagnetism is that positive current flows from higher to lower voltage. Electric fields also point away from higher voltages toward lower voltages. The figure shows current j flowing from +V toward –V. By definition, current j equals charge q multiplied by its velocity v: j=qv. The physical reality is that electrical current is actually carried by negatively charged electrons flowing from lower voltages to higher voltages. Oh well.

Another sign convention is that magnetic field lines originate at a magnet’s north pole and terminate at its south pole. The dotted closed curve in the figure is one such field line. The magnetic field vector B in the figure points away from the magnet’s north pole.

As Figure 1-6 shows, B is vertical where the wire is closest to the magnet. Per the right hand rule, the cross product of vector j (pointing toward you, out of the screen) and B produces force F pointing to the left, in accordance with F=qv×B. You will notice that the Lorentz force equation gives us the correct F even though the sign convention describes positive charge moving one way and the reality is that negative charge moves the opposite way. Inverting the polarity of both q and v does not change F. If you are having trouble getting the proper direction of F: (1) position your right hand with your palm up and your index finger pointing parallel to j; (2) with your wrist stationary, rotate your index finger until it points parallel to B; (3) your thumb is now pointing parallel to F; (4) if your thumb is pointing the wrong way, try using your “other” right hand.

In V2p1-6, Feynman points out that if F pushes the wire to the left, there must be an equal but opposite force pushing something to the right. He adds: “Otherwise we could put the whole thing on a wagon and have a propulsion system that didn’t conserve momentum!” As generally occurs, the object exerting force F on the wire (the magnet) has an equal but opposite force exerted on it. How does that force arise?

Current j produces a magnetic field of its own that circulates around the wire, as illustrated in Figure 1-7. Figure 1-7 Magnetic Field From Wire. The B field from the wire exerts force F, pushing the magnet to the right, as shown in Figure 1-7, which we will discuss in more detail later.

The B field circling the wire is described by the above relation between the circulation of B around a closed curve C and the flux of current through S, the surface C encloses. Define C to be a circle centered on some point along the wire, enclosing a surface that is perpendicular to the wire. The two dotted circles in the figure are examples of C. At every point along C, B is tangential to C and has the same magnitude B. Since the same current flows through all circles of any diameter D larger than the wire, BD must be a constant. (Current flux is constant and is proportional to the circulation of B that equals B•πD.) As circle C gets larger, B must decrease. This means B is inversely proportional to the distance from the wire.

Now imagine turning off the current flowing through the wire by setting V=0. If we then push the wire sideways over the magnet, a new current will flow in the wire. This again demonstrates the Lorentz force: our push gives the electrons in the wire a sideways velocity v that is perpendicular to B, producing a force F that is parallel to the wire, with F=qv×B. Force F moves these electrons along the wire.

Now imagine that the wire is stationary, V is still zero, and we move the magnet sideways under the wire. Again a new current flows in the wire. As Feynman says in V2p1-9, this makes sense from the standpoint of special relativity: since absolute velocity is meaningless, nature makes no distinction between magnet-moves-left and wire-moves-right. The third of the above electromagnetic equations states that changing magnetic fields produce electric fields. When the magnet moves, electrons in the wire experience a changing magnetic field, and the resulting electric field pushes them along the wire.

The last two figures demonstrate that a current-carrying wire is deflected by an external magnetic field and that it produces a magnetic field of its own. This combination of effects means that two current-carrying wires will exert forces on one another through their magnetic fields. Figure 1-8 shows two parallel wires carrying currents in the same direction, and exerting attractive forces on one another. Figure 1-8 Parallel Currents Attract. If the currents in Figure 1-8 were in opposite directions, the wires would repel one another.

As we discussed in the prior section, if all electric fields are constant, magnetic fields can only arise from moving charges. Indeed, the B field from a magnet is actually due to moving charges within the magnet, as we will discuss later. To demonstrate this, we can replace the bar magnet in Figure 1-6 with a current flowing through a coiled wire, as shown in Figure 1-9. Figure 1-9 B Field from Current through Coil. As in Figure 1-6, the magnetic field B from the coil exerts a force F on the hanging, current-carrying wire. Current flowing through the coil acts like a bar magnet.

The currents in magnets are not streams of electrons continually flowing through the magnet’s interior. In some materials, magnetism arises from the orbital motion of electrons within each atom. But in the case of iron, magnetism arises from the intrinsic spin of vast numbers of electrons in different atoms that align their spins along the same axis. These are quantum mechanical effects that we will thoroughly explore as this course develops.

The four equations of electromagnetism do not require any additional terms to describe the fields arising from various types of magnets; we need only include the currents within the magnets that produce those fields.

Recall the fourth equation: (Circulation of B around C)•c2 = d/dt (flux of E through S) + (flux of electric current t hrough S)/ε In V2p1-8, Feynman says the middle line was first conceived by Maxwell, and is of great importance.

Without this term, Feynman says, the equations would not make sense. Let’s see why.

Consider a capacitor comprised of two conducting plates separated by a non-conducting gap. Imagine that the capacitor is being charged by a positive current j flowing onto its left plate, while an equal current j flows out of its right plate, as shown in Figure 1-10. The plates and the wires carrying these currents are also shown in dark gray. As we know, current j produces a circumferential magnetic field B around the wire leading to the left plate. Also, an electric field E grows between the plates as their charge difference increases.

Figure 1-10 Charging a Capacitor Now imagine surrounding the wire with two circles C and C (shown in black) that are each centered 1 2 on the wire. Let S be the disk (a 2-D flat surface) whose boundary is C. Let S be a surface whose 1 1 2 boundary is C and let S be bowl-shaped, enclosing the left plate on all but its left side. Surface S 2 2 2 entirely covers the gap between the capacitor plates. Surfaces S and S are shown in light gray.

1 2 As we said earlier, the circulation of B around C equals j, the current flux through S, divided by c2.

1 1 However, there is no current flux through S, as S does not intersect the wire. But there is a changing 2 2 flux of electric field E through S. We will later show that this changing electric flux produces exactly the same circulation of B around C as does current j around C. Logically, B must be the same on C 2 1 1 as it is on C. This is what Maxwell understood.

Another remarkable consequence of the electromagnetic equations, which we will fully explore in later chapters, is the mechanism of light. These equations show that a changing electric field produces a changing magnetic field that in turn produces a changing electric field. A combination of oscillating electric and magnetic fields can therefore be self-sustaining, even absent any electric charges. Indeed, that is the essence of light.

Why Fields?

In V2p1-9, Feynman debates the philosophy of electromagnetism. He says you might feel that: “fluxes and circulations are pretty abstract. There are electric fields at every point in space; then there are these ‘laws.’ But what is actually happening?

“Why can’t you explain it, for instance, by whatever it is that goes between the charges.” Feynman says many physicists historically resisted the notion that separated charges interact by means of invisible fields. They felt forces must be due to direct contact as they imagined in Newtonian mechanics. They felt some physical things, perhaps little gear wheels, must fill space and provide the mechanism that pushes like charges apart and pulls opposite charges together. The fallacy with that, Feynman says, is that real physical objects do not actually push or pull one another by direct contact.

As the atoms in a kicker’s shoe approach the atoms in a football, the electrons in both bodies repel one another, preventing “colliding” atoms from attaining zero separation. What seems like direct contact on a human scale is in fact action-at-a-distance on the atomic scale. Feynman says that the idea that forces are due to direct contact is mistaken.

As we will fully explore in Feynman Simplified 3B, Feynman shows in Quantum Electrodynamics (“QED”) that electromagnetism is fundamentally due to charged particles exchanging photons. The general concept that forces are due to boson exchange is extended in Quantum Field Theory (“QFT”)

to include the strong and weak forces (but not gravity). In both QED and QFT all actions are local and direct — there is no action-at-a-distance. Perhaps this means our philosophy of forces has come full circle.

Feynman also rejects the attempts of others to explain electrodynamics solely in terms of field lines.

Field lines, he says, fail to represent “the deepest principle of electrodynamics”: linear superposition. The field lines due to charge X cannot be directly added to those due to charge Y to yield the field lines due to X+Y. The field concept does properly represent linear superposition: the E and B vector fields due to X plus the E and B vector fields due to Y are exactly equal to the E and B vector fields due to X+Y.

Feynman says: “The only sensible question is what is the most convenient way to look at electrical effects. … The best way is to use the abstract field idea. That it is abstract is unfortunate, but necessary.

The attempts to try to represent the electric field as the motion of some kind of invisible gear wheels, or in terms of lines, or of stresses in some kind of material have used up more effort by physicists than it would have taken simply to get the right answers about electrodynamics. It is interesting that the correct equations for the behavior of light were worked out by [James]

MacCullagh in 1839. But people said to him: ‘Yes, but there is no real “我们无法相信这种抽象的方程业务，因为材料的力学特性或许能满足那些方程，而光作为一种振荡，必须在某种介质中振动。如果人们当时更开明一些，他们可能会更早地相信关于光行为的正确方程。”

磁性是一种相对论效应。我们发现，当两根平行导线通以同向电流时（见图1-8），它们彼此间会产生吸引力。这些力源于导线中运动电荷产生的磁场。但是，如果我们从这些电荷的静止参考系来观察这一切，它们按定义是静止的，因此无法产生磁场。然而，当沿着与吸引力垂直的方向、平行于导线运动的参考系中观察时，横向力必须依然存在。这种情况让磁力线或通过无形齿轮直接接触的支持者们难以解释。

正确的解释需要狭义相对论。费曼在《V2p1-10》中明确指出：“磁性实际上是一种相对论效应。”他说，对于以速度v运动的两个电子，我们应该预期对正常电力有一个量级为v²/c²的相对论修正。对于电流的典型速度，相对论因子与1的差异仅为5×10⁻²⁶。通常，如此微小的修正可以忽略不计。但费曼指出，两根导线中的正负电荷如此精确地平衡，以致占主导地位的电力相互抵消，只剩下了相对论修正，而我们称之为磁性。

费曼说：“电效应近乎完美的抵消……使得相对论效应（即磁性）得以被研究，正确的方程——精确到v²/c²量级——得以被发现，尽管物理学家当时并不知道正在发生什么。这就是为什么当相对论被发现时，电磁定律无需被修改。它们——与力学不同——在v²/c²的精度上已经是正确的。”

上述讨论是描述性的，但肯定不是精确的决定性分析。我的兄弟理查德·皮乔尼博士在《物理教师》上发表了一篇适当的分析，发表于2007年3月第45卷。（是的，皮乔尼家有三位物理学博士……目前是这样。）

从默默无闻到无处不在。费曼结束了这次讲座，他说：

“在希腊人研究的众多现象中，有两个非常奇怪的现象：如果你摩擦一块琥珀，你可以举起小片的莎草纸；还有一种来自马格尼西亚岛的奇特岩石能吸引铁。令人惊叹的是，这些是希腊人所知的唯一显现出电或磁效应的现象。原因……主要在于我们前面提到的电荷平衡的惊人精确性。后来，科学家们……揭示了一个又一个新现象，而这些现象实际上都是这些琥珀和/或磁石效应的某个方面。现在我们意识到，化学相互作用的现象，乃至生命本身，都应该用电磁学来理解。

“在人们对电磁学主题的理解发展的同时，超越前人想象的技术可能性正在出现：可以通过电报进行远距离通信，可以与几英里外的人通话而无需任何连接，可以运行庞大的电力系统……通过长达数百英里的电线连接到……成千上万的地方，驱动工业和家庭的机器——所有这一切都源于对电磁定律的知识。

“今天我们正在应用更微妙的效应。电场力，尽管巨大，也可以非常微小，我们可以控制它们并以多种方式使用它们。我们的仪器如此精密，我们可以根据一个男人对几百英里外一根细金属棒中电子的影响方式，来判断他在做什么。我们所要做的就是将那根棒用作电视接收器的天线！

“从人类历史的长远视角——比如说，从一万年后来看——毫无疑问，19世纪最重要的事件将被判断为麦克斯韦对电动力学定律的发现。”

费曼会对数字电子学、计算机、互联网和手机的发展感到惊讶……但他会发推特吗？

## 第一章回顾：关键思想。

• 电力主要随距离的平方反比变化，引力也是如此，但电力要强十亿亿亿亿倍。与普通物质的引力不同，电磁力并不总是吸引性的。物体可以带正电、负电或零电荷；两个正电荷相斥，两个负电荷相斥，而一个正电荷和一个负电荷相互吸引。

• 同种电荷间的强烈排斥力使物质分散，而强烈的吸引力…… Unlike charges thoroughly mixes positive and negative charges. The properties of electromagnetism determine the characteristics of atoms, giving matter form and strength.

• F = q(E + v×B) is the Lorentz force F on a body with charge q and velocity v, in an electric field E and a magnetic field B.

• Linear superposition says that if there are two sets of arbitrary charges with arbitrary motions, and if set #1 produces vector fields E1 and B1, while set #2 produces vector fields E2 and B2, the fields produced by the sum of both sets are the vector sums: E = E1 + E2 B = B1 + B2 • For any volume V enclosed by a closed surface S: Flux of E through S = (Net charge within V)/ε₀ Flux of B through S = 0 For any open surface S with curve C as its boundary: (Circulation of E around C) = -d/dt (flux of B through S)

(Circulation of B around C)•c² = d/dt (flux of E through S) + (flux of electric current through S)/ε₀ Here c is the speed of light and ε₀ (epsilon-zero) is a constant. These are all the basic equations of electromagnetism, in a conceptual format.

• Magnetism is a relativistic effect.

## Chapter 2: Gradient, Divergence & Curl

Before launching into the main topic, Feynman begins this lecture with insightful advice on how to understand physics. Perhaps this should have been presented in Volume 1. This is a very long quote, but Feynman’s advice is worth heeding.

He says: “The physicist needs a facility in looking at problems from several points of view. The exact analysis of real physical problems is usually quite complicated, and any particular physical situation may be too complicated to analyze directly by solving the differential equation. But one can still get a very good idea of the behavior of a system if one has some feel for the character of the solution in different circumstances. Ideas such as the field lines, capacitance, resistance, and inductance are, for such purposes, very useful. So we will spend much of our time analyzing them. … On the other hand, none of the heuristic models, such as field lines, is really adequate and accurate for all situations. There is only one precise way of presenting the laws, and that is by means of differential equations. They have the advantage of being fundamental and, so far as we know, precise. If you have learned the differential equations you can always go back to them. There is nothing to unlearn.

“It will take you some time to understand what should happen in different circumstances. … Each time you solve the equations, you will learn something about the character of the solutions. To keep these solutions in mind, it will be useful also to study their meaning in terms of field lines and of other concepts. This is the way you will really ‘understand’ the equations. That is the difference between mathematics and physics. … People who have very mathematical minds are often led astray when ‘studying’ physics because they lose sight of the physics. … [They say] ‘Maxwell equations are all there is to electrodynamics; it is admitted by the physicists that there is nothing which is not contained in the equations. The equations are complicated, but after all they are only mathematical equations and if I understand them mathematically inside out, I will understand the physics inside out.’ Only it doesn't work that way. … They fail because the actual physical situations in the real world are so complicated that it is necessary to have a much broader understanding of the equations.

“What it means really to understand an equation—that is, in more than a strictly mathematical sense—was described by Dirac. He said: ‘I understand what an equation means if I have a way of figuring out the characteristics of its solution without actually solving it.’ … A physical understanding is a completely unmathematical, imprecise, and inexact thing, but absolutely necessary for a physicist.

“Ordinarily, a course like this is given by developing gradually the physical ideas—by starting with simple situations and going on to more and more complicated situations. This requires that you continuously forget things you previously learned—things that are true in certain situations, but which are not true in general. For example, the ‘law’ that the electrical force depends on the square of the distance is not always true. We prefer the opposite approach. We prefer to take first the complete laws, and then to step back and apply them to simple situations, developing the physical ideas as we go along. And that is what we are going to do.”

Review of Vectors The major focus of this chapter is on vectors and their derivatives. We begin by reviewing what we have already learned about vectors.

In electromagnetism, unless specifically indicated otherwise, all vectors will be three dimensional, meaning they have three components that are typically denoted: A = (Ax, Ay, Az)

Each component can be a function of x, y, z, and t. However, not all three functions form a proper vector. The components of a proper vector transform in a specific manner when a coordinate system is rotated. We will expand on this later in this chapter.

In contrast to vectors, scalars are quantities with magnitude but without direction, like 7 and π. A proper scalar has the same magnitude in all coordinate systems.

Vector A can be multiplied by scalar s simply by multiplying each of A’s components by s: sA = (sA_x, sA_y, sA_z).

Vectors can be added as follows: Q = A + B = (A_x + B_x, A_y + B_y, A_z + B_z).

Vectors can be subtracted simply by changing all the plus signs above to minus signs.

Two vectors can be multiplied in two distinct ways. The first way is the dot product, which results in a scalar. q = A•B = A_xB_x + A_yB_y + A_zB_z.

The dot product of any vector A with itself equals the square of the vector’s magnitude |A| (its length): |A|^2 = A•A.

The other way to multiply vectors is the cross product, which results in a vector. Q = A×B, Q = (A_yB_z – A_zB_y, A_zB_x – A_xB_z, A_xB_y – A_yB_x).

Here, we use the right hand rule: the term Q_q = A_aB_b has a plus sign if the three indices qab are an even permutation of xyz, namely xyz, yzx, or zxy; the term has a minus sign if qab is an odd permutation, namely xzy, zyx, or yxz. Since A×B = – B×A, it is essential to keep vectors in the proper order.

The vector Q = A×B is perpendicular to both vectors A and B. Hence: A•(A×B) = 0 = B•(A×B).

The two vector products have interesting geometric properties. The dot product A•B equals the normal projection of one vector onto the other. Figure 2-1 shows B projected onto A with q = A•B = |A|•|B|•cosθ, where θ is the angle between the vectors. The dashed line from the tip of B is normal (perpendicular) to A. The dot product is greatest when the two vectors are parallel (when θ=0).

The magnitude |Q| of the cross product Q = A×B equals the area of the parallelogram whose sides are A and B, as shown in Figure 2-1. In this case, Q points out of the screen. The equation for the magnitude |Q| is: |Q| = |A| |B| sinθ. |Q| is greatest when the two vectors are orthogonal (when θ=90º).

There is no procedure for dividing one vector by another.

The following relationships are valid for any vectors A, B, and C: A×A = 0; A•(B×C) = (A×B)•C; A×(B×C) = B(A•C) – C(A•B).

Scalar & Vector Fields

In physics, a field is simply a function of the spatial coordinates, such as f(x,y,z). Fields also generally vary over time, so one might equally well write f(x,y,z,t).

A scalar field has a value at each point that is a scalar, a single number. Temperature is an excellent example of a scalar field. Figure 2-2 shows a temperature map of Midwest North America, ranging from 13ºF in Regina, Canada to 93ºF in Monterey, Mexico. Contour lines, called isotherms, have been drawn through locations having the same temperature.

Note the tight spacing of contour lines between Regina and Monterey, indicative of a rapid 80ºF temperature rise. This contrasts with the sparsely spaced contour line between Toronto and Houston, which differ by only 24ºF.

A different type of field is used to represent more complex phenomena. A vector field has a value at each point that is a vector. An example is the map of ocean currents shown in Figure 2-3; each arrow shows the current’s direction and speed at that location.

Another example of a vector field is heat flow. Figure 2-4 depicts heat flowing from a hot spot (white circle) above an isothermal plane (gray area at bottom). The boxed region of the main image is enlarged at the right.

The vector h indicates heat passing a selected point. Two planes (shown as gray bars) have areas A_2 and A_1. As Figure 2-4 indicates, A_2 is perpendicular to h but A_1 is not. We wish to know the amount of heat flowing through each plane. The vector n is a unit vector normal to plane A_1. Unit vectors have length 1.

We will define h in terms of the amount of thermal energy passing a selected point per unit time per unit area. We first define a surface that is perpendicular to h that has an infinitesimal area ΔA. We also define ΔJ to be the amount of thermal energy passing through ΔA per unit time. The equation for h is: h = (ΔJ/ΔA) e. Here e is a unit vector in the h direction.

Now compare the heat flow through A_1 and A_2. Let A_1 and A_2 be so close that the heat flow lines are effectively straight lines, and let θ be the angle between n and h. The component of vector h in the n direction, equivalently the projection of h onto n, equals n•h = |h|•cosθ. The magnitude of heat flowing through A_1 per unit area per unit time is: |h|•cosθ = n•h = (ΔJ/ΔA) cosθ.

Field Derivatives

Most physical laws are expressed as differential equations: they describe how things change across space and over time. We therefore need to know how to differentiate vectors and vector fields.

The time derivative of vector A is another vector: dA/dt = (dA_x/dt, dA_y/dt, dA_z/dt).

x y z

What about the spatial derivative? How do we take the derivative of the scalar field for temperature T? In V2p2-4, Feynman asks if we should take dT/dx or dT/dy or dT/dz? What about all three? Consider the combination of these three quantities: ĎT = (dT/dx, dT/dy, dT/dz), is this a vector?

Feynman says an easy way to determine if ĎT is a vector is to take the dot product of ĎT with something that we know is a vector. If the dot product is a proper scalar, we are assured that ĎT transforms like a proper vector. Let’s see how this works.

We evaluate the temperature scalar field at two points specified by position vectors P1 and P2, where the temperatures are T1 and T2, respectively. Neither the points nor the temperatures depend on any specific coordinate system: T has the same value at P1 in every coordinate system, as does ΔT=T2–T1.

Let’s choose a coordinate system (x,y,z) and write: ΔP = P2–P1 = (Δx, Δy, Δz)

Since P1 and P2 are vectors, ΔP is also a vector with components (Δx,Δy,Δz).

Now by the definition of the partial derivative we have: ΔT = (∂T/∂x) Δx + (∂T/∂y) Δy + (∂T/∂z) Δz

The left side of this equation is a proper scalar; it is the same in all coordinate systems. This means the right hand side must also be a proper scalar. Also, the right hand side is a dot product: ΔT = (∂T/∂x, ∂T/∂y, ∂T/∂z) • (Δx, Δy, Δz)

ΔT = ĎT • ΔP

This proves ĎT is also a proper vector. Indeed: Ď = (∂/∂x, ∂/∂y, ∂/∂z)

is called the gradient, and it always produces a proper vector when operating on a scalar field. The direction of the gradient vector is the direction in which the scalar field is increasing most rapidly, and the magnitude of the gradient is the rate of increase. The direction of the temperature gradient is opposite to the direction of heat flow; the gradient points toward maximum temperature rise, while heat flows from hot to cold.

The standard notation for the gradient is: [Note: The inverted Δ (∇) is not a character supported in eBooks. The original line is a picture, not text.] I will therefore use either “grad” or Ď to denote the gradient.

For those wishing a more mathematically compelling proof that Ď is a vector, Feynman next demonstrates that the components of ĎT transform under rotation just like a position vector, such as P.

Let’s rotate our original coordinate system (x,y,z) by angle θ about the z-axis to obtain the coordinate system (x*,y*,z*). The equations relating these coordinate systems are: x* = x cosθ + y sinθ y* = y cosθ – x sinθ z* = z x = x* cosθ – y* sinθ y = y* cosθ + x* sinθ

In the *-coordinate system, the derivative of temperature T is: ΔT = ∂T/∂x* Δx* + ∂T/∂y* Δy* + ∂T/∂z* Δz*

Substituting coordinates yields: ΔT = ∂T/∂z* Δz + ∂T/∂x* (Δx cosθ + Δy sinθ)

+ ∂T/∂y* (Δy cosθ – Δx sinθ)

ΔT = ∂T/∂z* Δz + (∂T/∂x* cosθ – ∂T/∂y* sinθ) Δx + (∂T/∂y* cosθ + ∂T/∂x* sinθ) Δy

In the original coordinate system, the derivative of temperature T is: ΔT = ∂T/∂x Δx + ∂T/∂y Δy + ∂T/∂z Δz

Comparing the last two equations, we find: ∂T/∂x = ∂T/∂x* cosθ – ∂T/∂y* sinθ ∂T/∂y = ∂T/∂y* cosθ + ∂T/∂x* sinθ ∂T/∂z = ∂T/∂z*

Thus (∂/∂x,∂/∂y,∂/∂z) transforms like (x,y,z). Hence, Ď is an operator that is a proper vector; it is a vector operator. Ď operating on any scalar field produces a proper vector field. Feynman quotes the English physicist and mathematician James Hopwood Jeans saying such operators are “hungry for something to differentiate.”

We have established a very important relationship. For any scalar field ψ, and for any displacement Δr, the change in ψ resulting from that displacement is: Δψ = Ďψ • Δr

Feynman notes that in vector algebra: TĎ is not equal to ĎT Here ĎT is the gradient of scalar field T and is therefore a normal vector field, whereas TĎ is a vector operator, the vector operator Ď multiplied by a scalar function T. TĎ is a work in progress, an operator hungry to differentiate something; it isn’t finished until it is multiplied on its right side by a scalar field.

Gradient Operations

Gradients can also be applied to vector fields. Consider the dot product of the gradient with any vector field h: q = Ď•h = ∂hx/∂x + ∂hy/∂y + ∂hz/∂z Here, q is a scalar because the dot product of two vectors always produces a scalar. Feynman notes that this particular combination of derivatives of components is quite special; many other combinations, such as ∂hx/∂x, are neither scalars nor vectors. But this special combination has great physical significance. It is called the divergence of h, and is sometimes written: Ď•h = div{h} = ∂hx/∂x + ∂hy/∂y + ∂hz/∂z

Another way to combine the gradient with another vector is the cross product, which as we recall produces another vector.

Q = Ď×h Qx = ∂hz/∂y – ∂hy/∂z Qy = ∂hx/∂z – ∂hz/∂x Qz = ∂hy/∂x – ∂hx/∂y Q = Ď×h is called the curl of h, which can be written: Q = curl{h}

In V2p2-8, Feynman summarizes the three operations involving the operator Ď, each of which describes how fields change, without reference to any particular coordinate system.

ĎT = grad{T} is a vector Ď•h = div{h} is a scalar Ď×h = curl{h} is a vector

Maxwell’s Equations Using the gradient operator Ď we can succinctly and precisely write Maxwell’s equations, the primary equations of electromagnetism, as follows: Ď•E = ρ/ε Ď×E = – ∂B/∂t Ď•B = 0 c2 Ď×B = ∂E/∂t + j/ε Here, c is the speed of light, ρ is the charge density (electric charge per unit volume), j is the current density (electric current flowing through a unit area per unit time), and ε is a constant.

Heat Flow Equations In V2p2-8, Feynman demonstrates how this new vector algebra is employed, using the example of heat flow. Heat flow is quite complex in some materials. We will consider the simplest case: heat flowing in a metal.

Consider a 3-D block of metal whose opposite faces are held at two different temperatures, T₁ and T₂, as shown in Figure 2-5.

Figure 2-5 Heat Flow Through Metal Block For T₁ < T₂, heat will flow toward the right.

Let A be the block’s cross-sectional area, and let d be the distance heat flows from T₂ to T₁. Let J be the thermal energy flowing through the block per unit time. We know that J must be proportional to the cross-sectional area A, and also proportional to the driving force, the negative of the temperature gradient –(T₁–T₂)/d. The equation for J is: J = – κ (T₁–T₂) A/d Here, the constant κ is called the thermal conductivity. Let’s confirm the minus sign: positive thermal energy flows to the right if temperature decreases to the right, if the gradient (T₁–T₂)/d is negative.

If the geometry is more complex, we can take the limit as A and d become infinitesimal. At a small enough scale, at any point P, the heat flow vector field near P can be approximated as having a constant value h. If you understand that, skip to the next paragraph; else here is the explanation. Pick a coordinate system such that the x-axis is parallel to h at P. This means temperature is changing most rapidly in the +x-direction. At P, for a small displacement Δx, the change in temperature is: ΔT=(∂T/∂x)Δx. Choose Δx small enough to make ΔT negligible, and thereby make h nearly constant. This is the scale referred to above as “small enough.” We need not worry about ΔT in the y- and z-directions, because we aligned x in the direction of maximum temperature change.

Since h is nearly constant at this small scale, isotherms, surfaces of constant temperature, are nearly flat and nearly perpendicular to h. We can therefore apply the above equation derived for a block of metal. We align the block such that its opposite faces lie on flat isotherms. After relabeling the variables to stress their infinitesimal magnitude at this small scale, we have: ΔJ = – κ ΔT ΔA/Δd Recall that we defined the magnitude of h to equal ΔJ/ΔA. Since Δd is perpendicular to the isotherms, it is along the same axis as the gradient and the direction of heat flow; this makes ΔT/Δd equal to ĎT, the gradient of T. This yields: ΔJ/ΔA = – κ ΔT/Δd h = – κ ĎT Both sides of this equation are proper vectors. In V2p2-9, Feynman says this: “…is the generalization to arbitrary cases of the special relation for rectangular [blocks]. Later we should learn to write all sorts of elementary physics relations [in this] more sophisticated vector notation. This notation is useful not only because it makes the equations look simpler. It also shows most clearly the physical content of the equations without reference to any arbitrarily chosen coordinate system.”

Second Derivatives of Fields Feynman next lists all possible second derivatives of a scalar field T and a vector field h. These are: Ď•(ĎT)

Ď×(ĎT)

Ď(Ď•h)

Ď•(Ď×h)

Ď×(Ď×h)

Since the cross product of any vector with itself is always zero, the second in the above list is always zero, as shown here: Ď×(ĎT) = (Ď×Ď)T = 0 Feynman confirms this by checking the z-component.

{Ď×(ĎT)}z = Ďy(ĎT) – Ďx(ĎT)

{Ď×(ĎT)}z = ∂/∂x (∂T/∂y) – ∂/∂y (∂T/∂x)

{Ď×(ĎT)}z = ∂2T/∂x∂y – ∂2T/∂y∂x = 0 The last step holds because two partial derivatives commute; it makes no difference which derivative is done first. Hence, Ď×(Ďf)=0 for any scalar field f.

Another second derivative is also always zero: Ď•(Ď×h) = 0 This is because Q=Ď×h is a vector perpendicular to both Ď and h. Since Q and Ď are orthogonal, their dot product is zero.

These two conclusions lead us to two wonderful theorems of vector algebra that Feynman presents, but leaves the proofs to mathematicians.

Firstly, for any vector field A whose curl is zero (Ď×A=0), there exists a scalar field g such that: A = Ďg, if Ď×A=0 This says A must be the gradient of some scalar field g, if the curl of A is zero.

Secondly, for any vector field A whose divergence is zero (Ď•A=0), there exists a vector field G such that: A = Ď×G, if Ď•A=0 This says A must be the curl of some vector field G, if the divergence of A is zero.

These theorems are very useful in physics, since many physical fields have either zero divergence or zero curl.

We are left with three possible, non-zero, second deriva tives: ∇·(∇T)

∇(∇·h)

∇×(∇×h)

The first occurs often in physics, and is named the Laplacian, after the French mathematician and physicist Pierre-Simon Laplace. We can rewrite this: ∇·(∇T) = ∇·∇(T) = ∇²T ∇²T = ∂²T/∂x² + ∂²T/∂y² + ∂²T/∂z² Since ∇² is a dot product of two vectors, it is a scalar operator that can be applied to either scalar fields or vector fields. Applying ∇² to the vector field h for heat flow yields the vector quantity: ∇²h = ∂²h/∂x² + ∂²h/∂y² + ∂²h/∂z² Next, recall the following vector algebra equation from earlier in this chapter: A×(B×C) = B(A·C) – C(A·B)

We want to use this equation to evaluate one of the second derivatives of vector fields. But to do that, we have to be careful about the order of operators. Examining the last term above, if A, B, and C are all normal vectors, their order is unimportant.

C(A·B) = (A·B)C = C(B·A) = (B·A)C But if A and B are vector operators, the equations above are invalid. To obtain the correct result, we must maintain the order of C relative to the operators by using this form of the equation: A×(B×C) = B(A·C) – (A·B)C Using this correct form, we can rewrite one of the second derivative equations: ∇×(∇×h) = ∇(∇·h) – (∇·∇)h ∇×(∇×h) = ∇(∇·h) – ∇²h Feynman adds that we haven’t defined a vector operator for ∇×∇. By itself it is zero.

Pitfalls Feynman ends this lecture by highlighting two potential errors to avoid in the vector algebra of fields.

Firstly, for two scalar fields ψ and ø, the following expression: ∇ψ × ∇ø is not zero in general.

One might be tempted to say that ∇ψ is a scalar multiple of ∇, as is ∇ø. Therefore, ∇ψ×∇ø is a scalar multiple of ∇×∇, which is zero. Wrong! ∇ψ is Not a multiple of ∇, and the vectors ∇ψ and ∇ø will in general point in different directions because the scalar fields ψ and ø are different. Hence, the cross product will not be zero, in general. However, if ψ=ø, ∇ψ×∇ø will be zero.

Secondly, the rules for derivatives of fields are simpler in rectangular coordinate systems than in polar coordinate systems. For example, consider the x-component of the Laplacian of vector field h: (∇²h)_x = (∂²h_x/∂x² + ∂²h_x/∂y² + ∂²h_x/∂z²) = ∇²h_x The corresponding equation is not true for the radial component of h in a polar coordinate system. This is because “radial” points in different directions in different locations. It is safer to always express vector fields in rectangular coordinate systems.

Feynman promises to avoid leading you toward either of these pitfalls in this course.

## Chapter 2 Review: Key Ideas

• Vectors can be multiplied in two distinct ways. The dot product of vectors A and B is a scalar q.

q = A·B = A_xB_x + A_yB_y + A_zB_z The dot product of any vector A with itself equals the square of the vector’s magnitude |A| (its length).

The cross product of vectors A and B is a vector Q.

Q = A×B = (A_yB_z – A_zB_y, A_zB_x – A_xB_z, A_xB_y – A_yB_x)

If θ is the angle between vectors A and B: q = |A| |B| cosθ |Q| = |A| |B| sinθ The following relationships are valid for any vectors A, B, and C: A×A = 0 A·(B×C) = (A×B)•C A×(B×C) = B(A·C) – (A·B)C • A field is a function of spatial coordinates, such as f(x,y,z). Fields may also vary over time. A scalar field has a scalar value at each point, a single number that is the same in all coordinate systems. The temperature in Earth’s atmosphere is a scalar field.

A vector field has a value at each point that is a vector. A map of ocean currents, providing the current’s direction and speed at each location, is a vector field.

The gradient ∇ = (∂/∂x, ∂/∂y, ∂/∂z) produces a vector field when operating on a scalar field. For any scalar field ψ, and for any displacement Δr, the change in ψ resulting from that displacement is: Δψ = ∇ψ·Δr The divergence of a vector field h is a scalar field q: q = div{h} = ∇·h = ∂h_x/∂x + ∂h_y/∂y + ∂h_z/∂z The curl of a vector field h is a vector field Q: Q = curl{h} = ∇×h Q_x = ∂h_z/∂y – ∂h_y/∂z Q_y = ∂h_x/∂z – ∂h_z/∂x Q_z = ∂h_y/∂x – ∂h_x/∂y • With operator ∇, we can write Maxwell’s equations, the primary equations of electromagnetism, as: ∇·E = ρ/ε ∇×E = – ∂B/∂t ∇·B = 0 c² ∇×B = ∂E/∂t + j/ε Here, c is the speed of light, ρ is the charge density (electric charge per unit volume), j is the current density (electric current flowing across a unit area per unit time), and ε is a constant.

The possible second derivatives of a scalar field T and a vector field h are: ∇·(∇T) = ∇²T is a scalar field ∇×(∇T) = 0 ∇(∇·h) is a vector field ∇·(∇×h) = 0 ∇×(∇×h) = ∇(∇·h) – ∇²h is a vector field ∇·(∇h) = ∇²h is a vector field

## Chapter

Line, Surface & Volume Integrals Feynman says the many formulas developed in the prior chapter can all be summed up in one rule: the three derivative operators ∂/∂x, ∂/∂y, and ∂/∂z are components of a vector operator ∇.

In this chapter, we develop a greater understanding of the physical significance of the various derivatives of fields, which will in turn provide a greater understanding of vector field equations. We will find relationships between the integ The integrals of certain vector fields and certain derivatives of vector fields that will lead us to three fundamental theorems of vector calculus. In V2p3-1, Feynman says of these theorems: "They will be useful not only for interpreting the meaning and the content of the divergence and the curl, but also in working out general physical theories. These mathematical theorems are, for the theory of fields, what the theorem of the conservation of energy is to the mechanics of particles. General theorems like these are important for a deeper understanding of physics."

Line Integrals

In the prior chapter, we found that ∇g, the gradient of scalar field g, is a vector specifying the rate of change of g along each coordinate axis. It makes sense that the integral of the rate of change from A to B equals the total change from A to B.

To be more precise, let S and F be the position vectors of two points in space at which scalar function ψ has the values ψ(S) and ψ(F). Also, let Γ be any path that starts at S and ends at F, as shown in Figure 3-1.

Figure 3-1 Integral From S to F Along Path Γ

At each point P along path Γ, let ds be the curve’s tangent vector of infinitesimal length.

Our first theorem is:

ψ(F) – ψ(S) = ∫ ∇ψ • ds

This reads: the change in ψ from S to F equals the path integral along Γ of the tangential component of the gradient of ψ. Path integrals are also called line integrals, although there is no requirement that the path be a straight line.

We will now prove this theorem, not just to confirm its validity, but also to give you more insight into why it is true. If you prefer to skip the proof, proceed to the next section.

We will derive the above integral by taking the limiting case of path Γ being divided into a very large number of straight-line segments indexed j=1, 2, …N. Let the vector Δs_j run from the start of segment j to the start of segment j+1. Also, let ∇ψ_j be the value of ∇ψ at the center of segment j. Figure 3-2 illustrates the segmented path, and shows one displacement vector Δs_j.

Figure 3-2 Segmented Path Γ

For each segment j, Δψ_j, the change in ψ in that segment, equals: Δψ_j = ∇ψ_j • Δs_j

We sum Δψ_j over all segments and obtain: Σ ∇ψ_j • Δs_j

In the limit that N goes to infinity and all Δs_j’s go to zero, this sum becomes: Δψ = ψ(F) – ψ(S) = ∫ ∇ψ • ds

QED

Flux of Vector Field

We next seek to understand the flux of a vector field, employing the example of heat flow in a simple material such as a metal.

Inside a large block of metal, imagine defining a surface S completely enclosing a volume V. Heat is flowing within the large block, and we wish to know the amount of thermal energy flowing out of volume V. This is equivalent to knowing the amount of thermal energy flowing outward through surface S. Surface S and volume V could have any shape, but for simplicity Figure 3-3 depicts a rectangular box whose volume is V and whose six faces combine to form surface S. Imagine that the box is deep inside the much larger metal block.

Figure 3-3 Heat h Flowing Through da

Even for a volume and surface of great complexity, we can calculate the heat flow through S by calculating the flow through an infinitesimal portion of S of area da, shown in Figure 3-3 in dark gray, and then integrating the flow over all of S.

As we found earlier, the heat flow through da equals the normal component of h multiplied by da. With n being the unit vector normal to da, the heat flow through da is:

h • n da

The total heat flow through S is then:

Heat Flux through S = ∫ h • n da

The above surface integral equals the flux of h through surface S. The word flux became associated with such integrals when they were originally used to determine the flow of something physical (thermal energy in this case). We continue to use flux even when h represents something more abstract, such as an electric field. For example:

Flux of R through W = ∫ R • n da

This relationship between the flux of any vector field R through surface W and the surface integral of the normal component of R is quite general, and applies even if W is not a closed surface.

If the total amount of thermal energy within the large block of metal is constant (no heat sources or sinks), the amount of heat going outward through the closed surface S must equal the decrease in heat within V, the volume inside S. If Q is the total amount of heat within V, then the decrease in Q per unit time equals the heat flux through S. We write this:

∫ h • n da = –∂Q/∂t

Feynman says some people write d2a instead of da to stress that da is two-dimensional. He says he will assume that none of us need the “2” to remember that all areas are two-dimensional. Later, he uses dV to denote an infinitesimal volume, and he again assumes we don’t need d3V to remember that all volumes are three-dimensional.

Next we get a little tricky and cut volume V into two parts called volume V_a and volume V_b. Let S_ab be the area of the surface that separates the two volumes, let S_a be the surface area of the other 5 faces of V₁ and let S₂ be the surface area of the other 5 faces of V₂. This means the total surface area enclosing V₁ equals S₁+S_ab, while the total surface area enclosing V₂ equals S₂+S_ab. Note that the original surface area S=S₁+S₂.

Figure 3-4 Volume V Cut Into Two Parts by S_ab

Define n₁ to be the unit normal to S₁ pointing outward from V₁, and n₂ to be the unit normal to S₂ pointing outward from V₂. By definition, –n₁=n₂ everywhere on S_ab.

The analysis that follows will be valid for any vector field h, but if you wish to think of something specific, h could be heat flow.

The flux of h out of V₁ is: Flux out of V₁ = ∫ h•n₁ da + ∫ h•n₂ da over S₁                over S_ab

The flux of h out of V₂ is: Flux out of V₂ = ∫ h•n₁ da + ∫ h•n₂ da over S₂                over S_ab

The key point here is that the ∫ over S_ab terms in the prior two equations are equal in magnitude and opposite in polarity. The two integrals are over the same surface S_ab, both integrands are the normal component of the same vector field, but the normal vectors are in opposite directions. This makes physical sense: what flows out of V₁ through S_ab must flow into V₂ through S_ab.

In summing the prior two equations, the ∫ over S_ab terms cancel, yielding: Flux out of V₁ + Flux out of V₂ = ∫ h•n₁ da + ∫ h•n₂ da over S₁                over S₂

Since V₁ + V₂ = V, and S₁ + S₂ = S, the above equation is the same as the equation we derived for the undivided volume: Flux through S = Flux out of V = ∫ h•n da over S

The significance of all this is that we can subdivide volume V in any way we wish without changing the equality: (flux out of V) = (surface integral over S). We just need to sum all the smaller volumes and their enclosing surfaces. The only restriction on subdivision is the smaller volumes must completely fill V without any of them overlapping one another. This ensures every point P in V lies in one and only one smaller volume.

Gauss' Theorem

We will now use the ability to subdivide any volume to prove a wonderful theorem due to German mathematician Karl Friedrich Gauss, called either Gauss' theorem or the divergence theorem. The theorem is: ∫ h•n da = ∫ ∇•h dV over S      over V

This says the integral of flux of any vector field h out of a closed surface S equals the integral of the divergence of h throughout the enclosed volume V.

We will prove this theorem for any enclosed volume of any shape by subdividing that volume into tiny rectangular boxes. From the prior section, we know that if the theorem is true for one infinitesimal box, it must be true for the sum of any number of boxes that combine to form a large object of any shape.

We define an infinitesimal rectangular box, shown in Figure 3-5, whose opposite corners are: (0, 0, 0)

(Δx, Δy, Δz)

Figure 3-5 Rectangular Tiny Box: Δx × Δy × Δz

The volume dV and surface area dS of this infinitesimal box are: dV = Δx • Δy • Δz dS = 2(Δx • Δy + Δx • Δz + Δy • Δz)

First we consider the outward flux of a vector field h through the box face at x=0, which lies in the yz-plane. This flux is the integral across that face of the outward component of h, which is –h_x. The equation is: Flux out of x=0 face = ∫ (–h_x) dy dz over ΔyΔz

In the limit that the box size goes to zero, we can approximate h_x(y,z) by its average across the x=0 face, which reduces the above integral to: Flux out of x=0 face = –h_x(x=0) Δy Δz

Next consider the flux of h out of the box face at x=Δx. The outward component is now +h_x. By the same logic, the flux is: Flux out of x=Δx face = +h_x(x=Δx) Δy Δz

In the limit that Δx goes to zero, we can approximate h_x(x=Δx) using the definition of the partial derivative.

h_x(x=Δx) = h_x(x=0) + (∂h_x/∂x) Δx

We now add the fluxes out of the two box faces x=0 and x=Δx, yielding: Flux out of x-faces = Δy Δz × {–h_x(x=0) + [h_x(x=0) + (∂h_x/∂x) Δx] } Flux out of x-faces = (∂h_x/∂x) Δx Δy Δz

By the same logic, the flux out of the two y-faces and two z-faces are: Flux out of y-faces = (∂h_y/∂y) Δx Δy Δz Flux out of z-faces = (∂h_z/∂z) Δx Δy Δz

The total flux out of all six faces that comprise dS, is: Flux out of dS = ∇•h dV

Feynman says this shows the true meaning of the divergence of a vector field: ∇•h at any point P equals the outward flux of h per unit volume in the vicinity of P. Integrating the above equation over any surface S enclosing a volume V yields: Gauss' theorem: ∫ h•n da = ∫ ∇•h dV over S              over V

Example: Heat Conduction In V2p3-6, Feynman examines heat conduction in a metal as an example of the application of Gauss' theorem. Consider a hot block of metal that is gradually cooling down. Inside the metal, there are neither sources nor absorbers of heat; hence, heat energy is conserved within the metal's interior. If the heat within a volume V is decreasing, heat must be flowing out through its boundary, the surface S that encloses V.

Consider a tiny volume ΔV bounded by ΔS that is small enough to approximate ∇•h as constant throughout ΔV. We can then write: Heat flux = ∫ h•n da = ∫ ∇•h dV = ∇•h ΔV over ΔS        over ΔV

This heat flux must equal the rate of heat loss within ΔV. If we define q to be the heat per unit volume, then The total heat within ΔV equals qΔV, and we can write: Heat flux = – ∂(qΔV)/∂t ∇•h ΔV = – ∂q/∂t ΔV ∇•h = – ∂q/∂t

Feynman says: “Take careful note of the form of this equation; the form appears often in physics. It expresses a [local] conservation law—here the conservation of heat. We have expressed the same physical fact in another way in” the earlier equation: ∫ h•n da = –∂Q/∂t

The earlier equation expresses the conservation law in integral form, while the new equation expresses this in differential form. Gauss’ theorem ties these together. For any large volume V bounded by S containing total heat energy Q: ∫ h•n da = ∫ ∇•h dV = –∫ ∂q/∂t dV = –∂Q/∂t

Now consider a different situation. Imagine the large block of metal has a tiny heat source at its center. That heat source might come from the decay of a tiny concentration of radioactive atoms. Let’s approximate the heat source as being a single point P, and let W be the amount of energy per unit time the source releases. We will assume the remainder of the metal block conserves heat (no other heat sources or sinks). We also assume this situation has existed for a long time, long enough for the block to reach equilibrium, which means the temperature at each point has stabilized.

We ask: what is the heat flow vector field h throughout the metal block?

Since W is the heat energy flowing from the source, and the system is at equilibrium, the amount of heat flowing out of any volume that contains the source must also equal W. (If the amount of heat flowing out of V did not equal the amount of heat released by the source, the temperature within V would have to change.) Hence, the integral of h•n over any surface S enclosing the source must equal W.

We will simplify our analysis by considering a spherical surface S centered on the heat source. We shall also assume the edges of the large metal block are so far away from S that we can ignore edge effects. In this case, symmetry requires that the field h is entirely radial, and therefore h is normal to S everywhere. Feynman says our simplifications: “are adding a certain amount of guesswork—usually called ‘physical intuition’—to our mathematics in order to find the answer.” Feynman probably intended “guesswork” as a small joke. I would say we are making the problem solvable. The myriad practical complications of real world problems often make them mathematically intractable. We can’t learn much from unsolvable problems. Our goal here is to understand physical principles and methods; it is sensible to simplify.

Because h is entirely radial, the integral over a spherical surface S of radius R is: W = ∫ h•n da = h • 4πR² h = W/(4πR²) e

Here, e is the unit vector in the radial direction.

Now we consider a more general case. We return to a metal with no heat sources or sinks, but allow the block to have an arbitrary, non-equilibrium temperature distribution. In Chapter 2, we derived the following equation: h = – κ ∇T

Feynman cautions again that an isotropic, constant, thermal conductivity κ is a good approximation for simple cases like metals, but not for other materials.

Recall an equation derived above: ∇•h = – ∂q/∂t

Combining these two equations yields: –∂q/∂t = ∇•h = – κ ∇•∇T ∂q/∂t = κ ∇²T = κ (∂²T/∂x² + ∂²T/∂y² + ∂²T/∂z²)

We next assume that, at each point within the metal, temperature changes are proportional to changes in heat density q. We write this: C dT/dt = dq/dt

Here, C is the specific heat per unit volume (see Feynman Simplified 1B Chapter 22). Combining the prior two equations yields: dT/dt = (κ/C) ∇²T

This second order differential equation is called the heat diffusion equation. With constants other than κ and C, the diffusion equation is applicable to many physical phenomena, including the diffusion of gases, chemically inert atoms, and neutrons. We will explore some applications of the diffusion equation later in this course.

Here, we next turn to the circulation of a vector field.

Circulation of Vector Fields

In V2p3-8, Feynman says: “We obtained Gauss’ theorem by considering the integral over a surface, although it was not obvious at the beginning that we were going to be dealing with the divergence. …It was not at all clear that this would be the result. And so with an apparent equal lack of justification, we shall calculate something else about a vector and show that it is related to the curl.”

Consider a closed path Γ in a space containing a vector field C. At each point P along Γ, there is an infinitesimal vector ds that is tangent to curve Γ, as shown in Figure 3-6.

Figure 3-6 Path Γ, Tangent Vector ds & Vector Field C

The circulation of C around Γ is defined to be the integral around Γ of the tangential component of C. The right hand rule stipulates that we traverse Γ counterclockwise, as indicated by the circular arrow. This is written: circulation = ∫ C•ds

As Feynman notes, the term circulation originated when vector algebra was applied to fluid flow. Like flux, we now use circulation in t The description of any vector field, even when no material object is moving. We now follow the same approach used earlier with flux. We will show that if Γ is divided into small loops, the circulation around Γ equals the sum of the circulations around all the small loops. This will allow us to divide any closed curve into a collection of infinitesimal square loops that are much simpler to analyze. Ultimately this approach will yield another major theorem of vector algebra.

We begin by dividing path Γ into two smaller paths that together enclose the same area, as shown in Figure 3-7. The left loop consists two segments Γ_a and Γ_ab. The right loop consists of Γ_b and Γ_ab. The original path Γ=Γ_a+Γ_b.

Figure 3-7 Two Paths: Γ_a+Γ_ab & Γ_b+Γ_ab

The path for the left loop can start at Q, proceed along Γ_a to P, and then proceed along Γ_ab back to Q. The path for the right loop can start at Q, proceed along Γ_b to P, and then proceed along Γ_ab back to Q. The equations for the circulations around the left and right loops are: Left circ. = ∫ Γ_a C•ds + ∫ Γ_ab C•ds Right circ. = ∫ Γ_b C•ds + ∫ Γ_ab C•ds

We again note that the two ∫ Γ_ab terms are equal in magnitude and opposite in polarity. Both have the same path, the same vector field C, and equal but opposite tangent vectors ds. Therefore, the sum of both circulations is: Left + Right circ. = ∫ Γ_a C•ds + ∫ Γ_b C•ds Left + Right circ. = ∫ Γ C•ds = Γ circ.

This shows that the circulation around the left loop plus the circulation around the right loop equals the circulation around the original loop Γ.

We can therefore subdivide any closed loop into a number of smaller loops that enclose the same surface S without changing the total circulation of any vector field. The only restriction on subdivision is the smaller loops must completely fill Γ without any of them overlapping one another. This ensures every point P inside Γ lies inside one and only one smaller loop.

Stokes’ Theorem Given any vector field C and any surface S enclosed by a closed path Γ, we can subdivide the surface into infinitesimal areas, each enclosed by a rectangular loop. We define our coordinate system to align with one such loop that we call dΓ, as shown in Figure 3-8.

Figure 3-8 Circulation Around Rectangular Loop dΓ

The coordinates are (0,0) for the lower left corner, and (Δx,Δy) for the upper right corner. The integral around the rectangle is the sum of the integrals along the four sides. The integrals for the top and bottom sides, those parallel to the x-axis, are: Circ. X: Top + Bottom = ∫_{y=Δy} C•ds + ∫_{y=0} C•ds

For a small enough rectangle, we can approximate C(x,y) with its average value along each side. For both of these integrals, only the x-component of C contributes since ds is along the x-axis. Due to the counterclockwise path, ∫ds=+Δx in the left integral, and ∫ds=–Δx in the right integral. This reduces the above equation to: Circ. X = C_x(y=0) (+Δx) + C_x(y=Δy) (–Δx)

Again, we use the definition of the partial derivative to relate the two C values.

C_x(y=Δy) = C_x(y=0) + ∂C_x/∂y Δy

Putting this into the prior equation yields: Circ. X = {C_x(y=0) – [C_x(y=0) + ∂C_x/∂y Δy]} Δx Circ. X = – ∂C_x/∂y Δy Δx

Similarly, the circulation of the left and right sides totals: Circ. Y = C_y(x=0) (–Δy) + C_y(x=Δx) (+Δy)

Circ. Y = {–C_y(x=0) + [C_y(x=0) + ∂C_y/∂x Δx]} Δy Circ. Y = + ∂C_y/∂x Δx Δy

The total circulation around dΓ, the perimeter of the infinitesimal rectangle, is: Circ. dΓ = (∂C_y/∂x – ∂C_x/∂y) Δx Δy

The term in ( )’s is the z-component of the curl of C, and Δx•Δy is the area of the rectangle, which we shall call da. We rewrite this equation as: Circ. dΓ = (Ď×C)_z da

Since the z-axis is normal to the xy-plane, the z-component of the curl equals the dot product of the curl with n, the unit vector normal to da. By expressing the result entirely in terms of vectors, our result is independent of any particular coordinate system, and the same equation applies to every rectangular loop of which S and Γ are comprised.

Circ. dΓ = (Ď×C)•n da

One must take care to define n with the correct polarity, in accordance with the right hand rule. If you point the fingers of your right hand along path Γ, in the counterclockwise orientation, your thumb will point in the proper direction of n, out of the screen toward you, in this case.

Integrating over all infinitesimal rectangles, we obtain: Stokes’ theorem: ∫_S (Ď×C)•n da = ∫_Γ C•ds

This says the integral of the normal component of the curl of C across any surface S equals the total circulation of C around the closed path Γ that encloses S. Stokes’ theorem is named for Sir George Stokes, although the idea is said to have been suggested to Stokes by Lord Kelvin, and the theorem was first published many years later by Herman Hankel.

Fields With Zero Curl In this section, Feynman explores the special characteristics of curl-free vector fields.

If a vector field C has zero curl everywhere, Stokes’ theorem says its circulation around any closed path is zero. Now conside 一个闭合回路被分成两段：Γₐ和Γᵦ，如图3-9所示。

图3-9 形成闭合回路的两条路径由于Γₐ和Γᵦ的组合构成一个闭合回路，C围绕两段的逆时针环流之和必须为零。我们写为： 0 = ∫_{Γᵦ:Q→P} C·ds + ∫_{Γₐ:P→Q} C·ds ∫_{Γᵦ:Q→P} C·ds = – ∫_{Γₐ:P→Q} C·ds 这里左侧积分是从点Q沿路径Γᵦ到点P，右侧积分是从点P沿Γₐ到点Q。沿路径Γₐ反转方向会使右侧积分的极性反转。我们将其写为： ∫_{Γₐ:P→Q} C·ds = – ∫_{Γₐ:Q→P} C·ds 结合最后两个方程得到： ∫_{Γᵦ:Q→P} C·ds = ∫_{Γₐ:Q→P} C·ds 这意味着C·ds从Q到P的积分依赖于点Q和P，但与所取路径无关。实际上，我们可以取从Q到P的任何路径并得到相同结果。

我们在《费曼精简版1A》第10章讨论力和势能时，看到了同样的路径无关性。考虑重力的例子，它施加力F(r)并具有势能U(r)。回顾沿路径Γ的重力F所做的功W等于： W = ∫ F·ds 我们发现∫ F·ds与路径Γ无关，仅取决于Γ的端点。正是因为这种路径无关性，以下两个关系才成立： F = –∇U W = –ΔU 这些方程说明：(1) F等于势能的负梯度；(2) 功等于势能（一个标量场）变化量的负值。

关键点在于，因为矢量场F处处零旋度，所以它正比于某个标量场的梯度，这里就是U。

事实上，每个处处零旋度的矢量场都正比于某个标量场的梯度。我们在第2章用分量法证明了这一点，并在这里用矢量代数再次证明。

我们也可以演示该原理的逆命题：任何标量场的梯度的旋度处处为零。设ø(r)是任意标量场，∇ø是其梯度。沿任意路径Γ从Q到P的积分∫ ∇ø·ds必须等于ø(P)–ø(Q)，并且必须与Q和P之间的路径无关。这意味着沿任意闭合路径的积分∫ ∇ø·ds为零，根据斯托克斯定理，这意味着∇ø具有零旋度。即： ∇×(∇ø) = 0，对所有标量场ø成立现在考虑一个大曲面S被一个小闭合路径Γ所包围，如图3-10所示。

图3-10 被小闭合回路Γ包围的大曲面S 考虑当回路Γ逐渐变小，最终缩小到零尺寸时会发生什么。任何物理矢量场C在任何地方都是有限值。随着Γ的路径长度趋近于零，积分∫ C·ds也必须趋近于零。根据斯托克斯定理，这意味着： ∫_{S} (∇×C)·n da → 0 当 Γ → 0 这对任何闭合曲面S都必须成立。

现在回顾高斯定理，关于矢量场h的法向分量的面积分： ∫_{S} h·n da = ∫_{V} ∇·h dV 我们将∇×C替换h得到： ∫_{S} (∇×C)·n da = ∫_{V} ∇·(∇×C) dV 由于对于任何闭合曲面和任何矢量场C，左侧等于零，因此右侧也必须等于零。这意味着： ∇·(∇×C) = 0，对任意C恒成立我们在第2章也用分量法推导出了这个关系。

## 第3章回顾：关键思想

梯度算子∇是一个矢量算子，定义为： ∇ = (∂/∂x, ∂/∂y, ∂/∂z)

对于任意标量场ψ(r)和任意路径Γ： ψ(F) – ψ(S) = ∫_{Γ} ∇ψ · ds 这里，∫表示沿Γ的路径积分。这个方程表明，标量场梯度的路径积分仅取决于路径的端点，而与中间路径无关。

高斯定理说： ∫_{S} h·n da = ∫_{V} ∇·h dV 这里，h是任意矢量场，V是任意体积，S是包围V的曲面，n是S上各点的单位法向量。

斯托克斯定理说： ∫_{S} (∇×C)·n da = ∫_{Γ} C·ds 这里，C是任意矢量场，S是任意曲面，Γ是包围S的闭合回路，n是S上各点的单位法向量。

任何处处零旋度的矢量场都正比于某个标量场的梯度。

## 第4章

静电学麦克斯韦方程组在V2p4-1中，费曼说：“所有的电磁学都包含在麦克斯韦方程组中。” 运用我们掌握的矢量代数，我们将其写为： ∇·E = ρ/ε ∇×E = – ∂B/∂t ∇×B = ∂E/∂t + j/ε ∇·B = 0 这里，∇ = (∂/∂x, ∂/∂y, ∂/∂z)，ρ是电荷密度，j是电流密度，ε是常数，E和B分别是电场和磁场。

费曼说： “这些方程所描述的情况可能非常复杂。我们将首先考虑相对简单的情况，并学习如何处理它们，然后再讨论更复杂的情况。” 第一个简化是将我们自己限制在E和B场永不变化的情况下。这被称为静态。我们要求各处电荷密度恒定。这意味着所有电荷要么静止，要么以恒定电流流动。

在静态情况下，麦克斯韦方程组简化为两个解耦的方程组： equations: Electrostatics: ∇·E = ρ/ε₀ ∇×E = 0 Magnetostatics: ∇×B = j/ε₀ ∇·B = 0 In the static case, the E and B fields are not interconnected: they are governed by separate equations. Here, we can treat electricity and magnetism as if they were unrelated phenomena. Feynman stresses that the E and B fields become interconnected only when charges move or currents change. We will explore those intricacies later. First, we address the simpler static situations.

In electrostatics, the vector field E has a divergence but has zero curl. In magnetostatics, the vector field B has no divergence but has a non-zero curl. We will get lots of practice with vector algebra. The next nine chapters address electrostatics; the following five chapters address magnetostatics.

To make our start even simpler, Feynman says this lecture and the next will address only those situations in which the position of all electric charges are known. He says this case is “very simple—in fact almost trivial.” Perhaps not trivial, but certainly much simpler.

Coulomb’s Law & Superposition We begin with the simplest law of electromagnetism: Coulomb’s law, named after Charles Augustin de Coulomb. Coulomb’s law is an equation for the force between two stationary electric charges. It has exactly the same form as Newton’s gravitational force.

F(r) = q_r q_σ (r–σ) / (4πε₀ |r–σ|³)

Here, F(r) is the force exerted on charge q_r at position r by charge q_σ at position σ, and |u| denotes the magnitude of any vector u. This means u/|u| is a unit vector in the u-direction. The expression u/|u|³ provides both the direction of the force and its inverse-square dependence on the distance between the charges. Exchanging r and σ results in F(σ), the force exerted on charge q_σ at position σ by charge q_r at position r. It is easy to see that F(σ)=–F(r) in accordance with Newton’s law of action and reaction.

The proportionality constant 1/(4πε₀) is effectively a conversion factor between coulombs, the unit of charge, and kilograms, seconds, and meters. This constant has a defined value in terms of the speed of light. By international agreement: 1/(4πε₀) = 10⁻⁷ c², by definition = 8.988×10⁺⁹ newton-meter²/coulomb² = 8.988×10⁺⁹ volt-meter/coulomb If we set σ=0, we obtain the more familiar force equation: F(r) = q_r q_σ r / (4πε₀ |r|³)

For more than two stationary electric charges, we simply calculate the force vector F between each pair, and vectorially sum those forces. This is the principle of linear superposition that we have often discussed.

In V2p4-2, Feynman says: “That's all there is to electrostatics. If we combine the Coulomb law and the principle of superposition, there is nothing else. [Maxwell’s] electrostatic equations—say no more and no less.” While Coulomb’s law and linear superposition are sufficient to solve any electrostatic problem, the concept of an electric field E often simplifies the analysis. The electric field E(r) is defined to be the force per unit charge exerted on a charge at position r by all other charges. For the case of a single charge, we obtain the equation for E(r) simply by dividing the Coulomb equation by q.

E(r) = q_σ (r–σ) / (4πε₀ |r–σ|³)

Setting σ=0 yields the more familiar equation: E(r) = q_σ r / (4πε₀ |r|³)

The force equation then becomes: F(r) = q_r E(r)

The electric field E(r) is a simple way to obtain the force on any charge that might be at r. It thus has a physical meaning even if there is no charge there. This is the essence of the field concept.

When there are multiple charges q_j at positions σ_j, the electric field E(r) is this vector sum over all j: E(r) = Σ {q_j (r–σ_j) / (4πε₀ |r–σ_j|³) } This sum must not include any charge at σ=r. We exclude the possibility that a charge can exert a force on itself; this avoids an unwelcome zero in the denominator.

In V2p4-3, Feynman reminds us that E is a vector and explicitly writes out its x-component as: E_x(r) = (1/4πε₀) Σ_j {q_j (r_x –σ_jx) / [(r_x –σ_jx)²+(r_y –σ_jy)²+(r_z –σ_jz)²]³/2} Perhaps Feynman wrote this out to demonstrate the advantages of vector algebra.

When dealing with large scale objects, those much larger than protons and electrons, one can approximately describe electric charge as having a continuous density distribution: ρ(x,y,z). Integrating ρ over a tiny volume near σ yields the amount of charge per unit volume at σ.

For continuous charge densities, we can rewrite the electric field equation as: E(r) = ∫∫∫ {ρ(σ) (r–σ) / [4πε₀ |r–σ|³] } dV Here the triple integral is for σ running over all space other than the single point r. For brevity, I will not continue to explicitly show multiple integral signs where the intent is clear.

Feynman concludes this section with this humorous note: “We have completely solved all the electrostatic problems in which we know the locations of all of the charges. Given the charges, what are the fields? Answer: Do this integral. So there is nothing to the subject; it is just a case of doing complicated integrals over three dimensions.” dimensions—strictly a job for a computing machine!

With our integrals we can find the fields produced by a sheet of charge, from a line of charge, from a spherical shell of charge, or from any specified distribution. It is important to realize, as we go on to draw field lines, to talk about potentials, or to calculate divergences, that we already have the answer here. It is merely a matter of it being sometimes easier to do an integral by some clever guesswork than by actually carrying it out. The guesswork requires learning all kinds of strange things. In practice, it might be easier to forget trying to be clever and always to do the integral directly instead of being so smart. We are, however, going to try to be smart about it.

The Electric Potential

The electric potential is one form of potential energy: it is the energy an electric charge has by virtue of its position in an electric field. This is entirely analogous to the gravitational potential energy that a mass has by virtue of its position in a gravitational field. When a charge is moved from one location in an electric field to another, work is done. If a negative charge is moved closer to other negative charges, the work done is positive — it requires energy to push like charges together. Conversely, if a negative charge is moved closer to a positive charge, the work done is negative — electric potential energy is released, and may be converted into kinetic energy, heat, or other forms of energy.

The general equation for the work done in moving an object from point A to point B against a force F is: W = –∫ F • ds A–>B As in prior chapters, ds is the incremental tangent vector along the path from A to B. For the electric potential, we wish to find the energy per unit charge. We achieve this by setting q, the charge of the object subject to the field, equal to 1. This yields: W(q=1) = – ∫ E • ds r A–>B Clearly, W depends on the path’s end points A and B. But Feynman now raises the question of whether or not W depends on the path taken between A and B. We know that, in general, path integrals do depend on every point along the path. But we also know, from earlier chapters, that these integrals are path-independent when the integrand is the gradient of a scalar field. So, is W path-independent?

If two paths from A to B give two different values of W, we could utilize that difference to produce energy. Let’s imagine that along paths Γ_HI and Γ_LO the work required to go from A to B is W_HI and W_LO, with W_HI being greater than W_LO. Recall that any integral inverts polarity if we integrate in the reverse direction. If all this were true, we could: (1) Start at A (2) Expend energy W_LO to take path Γ_LO to B (3) Gain energy W_HI by taking path Γ_HI to A (4) Sell the energy difference W_HI – W_LO

Is this possible? Feynman says Yes, but only if something else maintains the energy of the field that exerts force on the charge. Indeed, many practical devices operate with fields exerting forces on charges, as we shall discover in this course. However, all such devices require moving charges to generate those fields. No device can supply field energy in an electrostatic situation. In the static case, W is the same for all paths, W_HI = W_LO, and no energy can be produced, as we now show.

Let’s us prove that in electrostatics, the path integral for work is path-independent. We will first prove this for the electric field from a single charge, and then use the principle of linear superposition to show that the proof applies to any collection of charges. To demonstrate how all our mathematical tools tie together, we will prove path-independence in three ways: by vector algebra; by conventional analysis; and graphically.

Vector algebra is the simplest approach. From Maxwell’s electrostatic equations, the curl of E is always zero. As shown in the prior chapter, this means E is the gradient of a scalar field, and we know the path integral of any gradient is path-independent. QED

For the other approaches, we define a polar coordinate system centered on the single charge q. The essential point here is that, in electrostatics, the electric field E due to a single charge at the origin is pointed entirely radially, in accordance with Coulomb’s law.

Let’s next examine the analytical approach. The integral for work on a unit charge q in a radial field reduces to: W(q=1) = – ∫ E dr r A–>B r W(q=1) = – ∫ q dr / (4πε r2)

r A–>B 0 The integrand has no azimuthal or polar angular dependence; it is a function of r only. The integral depends on the initial and final values of r, but not on how that change occurs. Because the field is entirely radial, the math provides no mechanism to specify the details of how the charge moves from A to B. The path integral has been reduced to a standard integral that is easily solved: ∫dr/r²=–1/r.

W(q=1) = + q / (4πε r) | r 0 A–>B W(q=1) = + (q/4πε) {1/r – 1/r } r 0 B A As we see, the result depends only on the path’s endpoints A and B.

费曼采用了一种更具图形性的方法。考虑两条从点A到点B的路径Γα和Γβ，如图4-1所示。

图4-1 从A到B的两条路径

我们在图4-1中看到，路径由一些线段组成，这些线段要么完全是方位角方向（恒定半径，变化方位角），要么完全是径向（恒定方位角，变化半径）。如果我们让这些线段足够短，任何连续路径都可以通过交替的方位角和径向线段，以任何所需的精度来近似。

让我们考虑路径Γα，并将其线段编号为k=1到k=N，其中线段1从A开始，线段N在B结束。我们还定义rk为线段k开始时的半径，定义rN+1为在B点的半径。

如果线段k是径向的，E•ds等于E dr，因为电场是径向的。无论dr是正还是负，这都成立。线段k的功积分为： W(q=1) = – ∫ E dr rk r W(q=1) = – ∫ q dr / (4πε₀ r²)

rk r W(q=1) = + (q/4πε₀) {1/r – 1/r} rk+1 k

如果线段k是方位角的，E•ds等于0，因为ds与径向电场E正交。上面的等式仍然成立。半径在方位角线段上没有变化，所以rk+1 = rk，{ }中的两项相互抵消。

因此，我们对于任何线段（径向或方位角）上的功都有相同的表达式。我们可以简单地将所有线段求和，以获得由单个电荷q产生的电场对单位电荷所做的总功。

W(q=1) = + (q/4πε₀) Σ {1/r – 1/r} k=1 to N k k+1 k

现在考察从k=1到k=N的求和。注意有两个半径只出现一次：当k=1时的r1和当k=N时的rN+1。回想r1 = rA 且 rN+1 = rB。所有其他的rm都出现两次，当k=m时贡献-1/rm，当k+1=m时贡献+1/rm。这些出现两次的rm的贡献相互抵消。求和结果只剩下： W(q=1) = + (q/4πε₀) {1/rB – 1/rA}

这再次证明了功只取决于端点，而与中间的路径无关。证毕。

因为图4-1中沿路径Γα和Γβ的路径积分相等，所以沿组合路径Γα + Γβ的积分必须为零，因为反向遍历任一路径会反转该路径积分的符号。由于这对所有路径都成立，根据斯托克斯定理，矢量场E的旋度必须为零。这与静电学的麦克斯韦方程组一致。

我们现在定义标量函数Φ(r,σ)为： Φ(r,σ) = (q/4πε₀) / |r–σ|

我们还定义标量函数φ(r)为： φ(r) = Φ(r,σ=0) = (q/4πε₀) / |r|

沿路径Γ所做的功W等于Φ（或φ）从起点A到终点B的变化。因此： W = Φ(rB,σ) – Φ(rA,σ)

实际上，Φ(r,σ)是位于位置σ的电荷q产生的电场在位置r处对单位电荷的电势能。当电荷q位于坐标(0,0,0)时，σ=0，Φ(r,σ)简化为φ(r)。我们定义这些电势使得它们在r=∞处都为零。这是最常见的定义。但像所有能量电势一样，只有电势差才具有物理意义。因此，我们可以在特定情况下根据需要向电势中添加任意常数。

我们现在已经证明了单个电荷q产生的电场中功的路径无关性。接下来我们希望将这一证明扩展到任何静态情况下的电荷集合。

回忆由线性叠加原理得出的，在位置r处由多个位于σj的电荷qj产生的电场方程： E(r) = (1/4πε₀) Σ {qj (r–σj) / |r–σj|³ } j

同样回忆在电场E中将单位电荷从A移动到B所做的功的方程： W(q=1) = – ∫ E • ds A–>B

将E的表达式代入W的方程： W(q=1) = – (1/4πε₀) ∫ Σ qj (r–σj)•ds / |r–σj|³ A–>B j

将求和移到积分外： W(q=1) = – (1/4πε₀) Σ qj ∫ (r–σj)•ds / |r–σj|³ j A–>B

我们现在可以分别计算求和中的每个积分，因为它们互不依赖。第j个积分Wj是在电荷qj（位于位置σj）的电场中移动单位电荷所做的功。根据电势能Φ的定义，该功等于： Wj = – qj ∫ (r–σj)•ds / |r–σj|³ A–>B

Wj = Φ(rB,σj) – Φ(rA,σj)

Wj = (qj/4πε₀) {1/|rB –σj| – 1/|rA –σj|}

将所有Wj求和，得到在所有电荷qj（位于σj）的总电场中将单位电荷从A移动到B所做的总功： W(q=1) = Σ Wj j W(q=1) = (1/4πε₀) Σ qj {1/|rB –σj| – 1/|rA –σj|} j

这证明了即使在多个电荷的情况下，所做的功也只取决于端点，而与中间路径无关。

我们可以重写标量电势φ的方程以适用于多个电荷，如下： φ(r) = Σ (qj/4πε₀) / |r–σj| j

φ(r)是单位电荷在r处由多个电荷qj（位于σj）产生的电场的电势。

将其代入功的方程： W(q=1) = φ(rB) – φ(rA)

我们已经证明，电场的线性叠加特性确保了电势的线性叠加。

对于一 continuous charge distribution, we replace summations with integrals.

ø(r) = (1/4πε) ∫ {ρ(σ) / |r - σ| } dV over all V Here, we integrate over all 3-D space with σ being the position vector of the integration point.

Gradient of Electric Potential In the prior section, we defined the scalar potential ø. Its physical significance is that ø(r) is the potential energy of a unit charge (q=+1) at position r in the electric field of a charge q located at (0,0,0). By defining ø(r) to be zero at r=∞, ø(r) is the energy required to move a unit charge from infinity to position r.

Recall this equation for the gradient of a function f for small displacements: Δf = ∂f/∂x Δx + ∂f/∂y Δy + ∂f/∂z Δz Δf = ∇f • Δr Here, r = (x,y,z) and Δr = (Δx,Δy,Δz).

Applying this equation to the scalar potential ø yields the change in ø for a small change in position.

Δø = ∇ø • Δr We now compare this to the work done in moving a unit charge from r to r+Δr.

W = – ∫ E • Δr In the prior section, we proved this path integral is path-independent, and its value equals the difference in ø at the two endpoints of the path. This is: W = ø(r+Δr) – ø(r) = Δø Combining these results yields: Δø = ∇ø • Δr = – ∫ E • Δr This must hold for all Δr. In the limit that Δr go to zero, this reduces to: E = –∇ø This also follows, as discussed in the prior section, from the fact that in electrostatics the curl of E is always zero. Coulomb’s law ensures that E is the gradient of a scalar, which ensures E has no curl.

All the math ties together, as it always does if one makes no mistakes.

The potential ø is important for practical reasons. We can always calculate the three components of E from three integrals of the form ∫(x/r3)dx. But it is often easier to calculate ø from one integral of the form ∫(1/r)dr, and then take the gradient.

In V2p4-7, Feynman says: “We should point out an important fact. For any radial force the work done is independent of the path, and there exists a potential. If you think about it, the entire argument we made above to show that the work integral was independent of the path depended only on the fact that the force from a single charge was radial and spherically symmetric. It did not depend on the fact that the dependence on distance was as 1/r2—there could have been any r dependence. The existence of a potential, and the fact that the curl of E is zero, comes really only from the symmetry and direction of the electrostatic forces.”

Inverse-Square Law & Electric Field We next consider the other equation of electrostatics: the relationship between the flux of E and the density of charge. This relationship does depend critically on the inverse-square law — that the field E from a charge q varies as 1/r2, where r is the distance from that charge.

The inverse-square law appears often in physics. Two examples are Newton’s force of gravity, and the intensity of light from a distant star. The inverse-square law seems entirely reasonable. If, for example, we accept that the energy of starlight is conserved, it must be true that the same amount of light energy passes through every sphere of any radius that is centered on a shining star. Since the area of a sphere is proportional to r2, it must be true that the intensity of starlight (energy per unit area) is proportional to 1/r2.

It seems “comforting” that electricity should be governed by the same “reasonable” law.

But Feynman goes to some lengths orthogonal to all radial lines from charge q. The lower surface has two sides labeled c and d that are tilted relative to the azimuthal direction. The tilt angle of side d is labeled θ.

Let’s determine the flux of E through the upper surface. As discussed in earlier chapters, the flux of a vector field through a closed surface equals the integral across that surface of E·n, E’s component normal to the surface. By our construction, the normal component of E along the four radial sides labeled e is zero, since E is entirely parallel to the e sides.

Conversely, E is entirely orthogonal to sides a and b; it is parallel to the normal of side b and antiparallel to the normal of side a. The fluxes through sides a and b are: Flux through a = –(area of a) q/(4πε₀rₐ²)

Flux through b = +(area of b) q/(4πε₀r_b²)

Since the 2-D areas of a and b are proportional to their radii squared, the two fluxes have equal magnitudes and opposite polarities. The total flux through the upper closed surface is therefore zero.

What about the lower surface with its tilted sides? Side d is tilted relative to the azimuthal direction by angle θ. This makes its area larger by the factor 1/cosθ, but also reduces E·n by the factor cosθ. The tilt angle makes no difference, so the flux through the lower closed surface is also zero.

As we discussed in proving Gauss’ theorem, any volume bounded by a closed surface can be subdivided into tiny volumes bounded by tiny closed surfaces similar to the surfaces in Figure 4-2. We conclude that the flux of E through any closed surface is zero, provided that it contains no charges.

What if a closed surface does contain an electric charge?

Consider the simplest case: a spherical surface S surrounding and centered on a single charge q, assumed to be a point source of zero size. By symmetry, the field E is normal to S everywhere. If r is the radius of S, the flux through S is: Flux through S = (area of S) q/(4πε₀r²)

Flux through S = (4πr²) q/(4πε₀r²)

Flux through S = q/ε₀ Note that this result does not depend on r — the same flux passes through a sphere of any radius.

But what if the enclosing surface isn’t a sphere? Must we solve some horrible integral?

No worries; Feynman has a trick. Imagine a closed surface S* that has a spherical hole inside it. A 2-D cross-section is shown in Figure 4-3. The spherical hole inside S* is centered on a charge q, represented by the black dot. This hole is connected to the exterior of S* by a tiny horizontal tube. Spherical surface S, also centered on charge q, lies within the hole inside S*. Both S and S* are continuous closed surfaces.

Figure 4-3 Large Surface S* with Small Hole S Consider the limit as the inner spherical part of S* shrinks down onto S, and the horizontal tube shrinks to zero.

From above, the flux of E flowing out of S equals q/ε₀. Hence, the flux flowing into the inner spherical portion of S* must be –q/ε₀ (minus since it is flowing into S*). Since S* contains no charges, the total flux throughout all of S* must be zero. In the limit that the horizontal tunnel goes to zero, the only remaining portion of S* is its exterior. This means the flux flowing out of the exterior of S* equals +q/ε₀.

This proves that the flux of E flowing out through any closed surface of any shape must equal q/ε₀, where q is the enclosed charge.

Feynman comments in V2p4-7&9 that one might conceive a “model” of the electric field in which charges emit tiny “bullets” that fly out in all directions, and that the number of “bullets” is conserved. That “model” would explain the inverse-square behavior of the electric field, and would be consistent with the flux calculations we just completed. He adds: “But does the model tell us anything more than we get simply by writing [the flux equations]? No one has succeeded in making these “bullets” do anything else but produce this one law. After that, they produce nothing but errors. That is why today we prefer to represent the electromagnetic field purely abstractly.” Gauss’s Law & The Electric Field We now wish to extend the results of the prior section to situations involving multiple charges. Two charges are sufficient to illustrate the principle.

Consider two charges q₁ and q₂ and the electric fields E₁ and E₂ that each produces. By linear superposition, the field due to both charges is E = E₁ + E₂.

Let’s calculate the flux through a closed surface S.

Flux through S = ∫ E·n da Flux through S = ∫ E₁·n da + ∫ E₂·n da If neither charge is within S, the flux out of S equals zero. If only q₁ is within S, the flux out of S equals q₁/ε₀. If both charges are within S, the flux out of S equals (q₁+q₂)/ε₀. Clearly, we can continue adding charges with the obvious result. This is: Gauss’ Law: ∫ E·n da = Q/ε₀ Here, Q is the net sum of all charges (positive charges minus negative charges) that lie within S.

For discrete charges, we write: Q = Σ qⱼ throughout interior of S For a continuous charge distribution ρ(r), we write: Q = ∫ ρ(r) dV ∫ ρ(r) dV Here, V is the volume enclosed by S.

In V2p4-10, Feynman stresses that Gauss’ law is valid only because the electric field has an inverse-square dependence on distance (one less power than the number of spatial dimensions). Feynman says Gauss’ law and Coulomb’s law are equivalent, but expressed in different ways.

We can also write Gauss’ law in differential form. From Chapter 3, we know that the divergence of E integrated throughout a volume V equals the flux of E through the surface enclosing V. For an infinitesimal volume dV, we can write this as: ∇·E dV = ρ dV / ε ∇·E = ρ / ε This is Maxwell’s first equation of electrostatics. We have shown that both of Maxwell’s equations of electrostatics are restatements of Coulomb’s law.

Field of a Charged Ball In Feynman Simplified 1A Chapter 10, we proved that the gravitational field outside a spherically symmetric ball of mass M and radius R depends only on M and not on R. We may, therefore, calculate the field assuming all its mass is concentrated at its center.

This theorem, first proven by Newton, is crucial for both inverse-square forces: gravity and electrostatics. Without it, we would face an enormous calculation for every gravitational and electrostatic problem. In V2p4-10, Feynman says: “For many years Newton didn’t make public his theory of gravity, because he couldn’t be sure this theorem was true.” Feynman says we can now prove this theorem for electrostatics in a much simpler manner.

Consider a ball of radius R, with a total charge Q that is distributed throughout its volume in a spherically symmetric manner. We wish to know the electric field E outside the ball, at a distance r from the ball’s center. We select a coordinate system centered on the ball.

Due to the spherical symmetry of Q, the electric field must also be spherically symmetric, and must point in the radial direction everywhere. Define an imaginary sphere S of radius r that surrounds the ball and is centered on the ball’s center, with r > R. The flux of E equals: Flux of E through S = ∫ E(r) da S r Flux of E through S = E(r) 4π r² Gauss’ law says that flux is related to the total charge Q within S by: Flux of E through S = Q / ε Therefore: E(r) 4π r² = Q / ε r₀ E(r) = Q / (4πε r²)

r₀ Since nothing in our derivation depends on the ball’s radius R, our result is valid for any R, including for a point charge with R=0.

Having developed an extensive vector algebra toolbox, proving this theorem is now simple. But this did not come for free. Much of what made the theorem difficult before had to be proven to fill our toolbox.

Field Lines In V2p4-11, Feynman says: “The two laws of electrostatics, one that the flux [of E] is proportional to the charge inside and the other that the electric field is the gradient of a potential, can also be represented geometrically.” Figure 4-4 depicts a 2-D cross-section of a 3-D physical situation. The solid arrows, called field lines, show the direction of the E field due to a positive charge at the center. Field lines are always tangent to the E field, which is radial everywhere for a single charge. Each field line originates at a positive charge and continues unbroken until reaching a negative charge.

Figure 4-4 Field Lines & Equipotentials: Single Charge We represent the strength of the electric field by the density of field lines. At each point P in 3-D space, we define “density” to be the number of field lines per unit area crossing a tiny plane perpendicular to E near P. For a single charge, E decreases as 1/r². The density of field lines will also drop as 1/r² if the lines never start or stop in empty space. If N field lines originate at charge q, and the same N field lines cross every sphere of radius r centered on that charge, their density will naturally decrease as 1/r² because the surface area of a sphere is proportional to r². Indeed, by making N proportional to q, the density of field lines is everywhere a direct indication of the strength of the electric field due to q.

Figure 4-4 also shows dashed circles that are equipotentials, surfaces with the same value of the electrostatic potential ø. The circles in the figure, from outside in, correspond to relative ø values of: 1, 2, 3, and 4. The equipotential surfaces must be perpendicular to the field lines everywhere.

Field lines provide meaningful graphic representations of electric fields. However, they do not sensibly represent the principle of linear superposition. Vectors make it easy to add the fields E and E due to charges q and q. But, graphically adding field lines from two separated charges q and q₂ yields utter nonsense. The field lines in Figure 4-4 are all straight lines; clearly two such images, slightly displaced, result in a bewildering array of crossing lines. That is an impossible result for the sum of two electric fields: the vector field E at point P cannot point in two different directions.

The true sum of two electric fields from two like charges is shown in Figure 4-5. The vector fields from each charge are added point by point to produce the total field shown. The field lines of the combined field curve to maintain the tangent property. The equipotential surfaces are also shown. The electric field is always perpendicular to the equipotential surfaces.

Figure 4-5 Field Lines From Two Equal Charges The sharply curved fields line in this figure are in stark contrast to the sum of two graphical representations of single charges.

## Chapter 4 Review: Key Ideas

In static situations in which charge densities are constant everywhere, the E and B fields never change and all electric charges are either stationary or flowing in constant currents. Here, Maxwell’s equations reduce to two de-coupled pairs of equations: Electrostatics: Ď•E = ρ/ε Ď×E = 0 Magnetostatics: Ď×B = j/ε Ď•B = 0 Coulomb’s law: for stationary charges, the force F(r) exerted on charge q at position r by charge q at position σ is: F(r) = q q (r–σ) / (4πε |r–σ|3)

Here, |u| denotes the magnitude of vector u 1/(4πε) = 10–7 c2 volt-meter/coulomb, by definition The electric field E(r) due to charge q at position σ is: E(r) = q (r–σ) / (4πε |r–σ|3)

The force equation then becomes: F(r) = q E(r)

By the principle of linear superposition, the electric field due to multiple charges q at positions σ is the vector sum: E(r) = Σ {q (r–σ) / [4πε |r–σ|3] } On scales much larger than protons and electrons, one can approximately describe electric charge as having a continuous density distribution: ρ(x,y,z). Integrating ρ over a tiny volume near σ yields the amount of charge per unit volume at σ. For continuous charge densities, the electric field is: E(r) = ∫ {ρ(σ) (r–σ / [4πε |r–σ|3] } dV The electric energy potential for discrete charges and for continuous charge densities are: ø(r) = (1/4πε) Σ {q / |r–r| } ø(r) = (1/4πε) ∫ {ρ(σ) / |r–σ| } dV The potential ø is related to E by: E = –Ďø Ď•E = Ď2ø = – ρ / ε Linear superposition of fields ensures the linear superposition of potentials.

The electric field at position r from a ball of radius R and total charge Q is: Gauss’ law: E(r) = Q / (4πε r2)

provided |r|>R and the distribution of Q is spherically symmetric. As this is independent of R, we may assume Q is a point charge (R=0).

Feynman says: “If we combine the Coulomb law and the principle of superposition, there is nothing else. [Maxwell’s] electrostatic equations—say no more and no less.”

## Chapter

Gauss’ Law in Action In V2p5-1, Feynman says: “There are two laws of electrostatics: the flux of the electric field from a volume is proportional to the charge inside—Gauss’ law; and the circulation of the electric field is zero—E is a gradient. From these two laws, all the predictions of electrostatics follow. But to say these things mathematically is one thing; to use them easily, and with a certain amount of ingenuity, is another.” This chapter hones our skills using Gauss’ law, and illuminates other physical principles.

No Equilibrium in Electrostatic Field Feynman poses the question of whether or not a point charge can be stationary — in a stable mechanical equilibrium — in an electrostatic field.

By stable equilibrium, physicists mean a state that: (1) doesn’t change if undisturbed; and (2) is self-restoring if slightly disturbed. For example, the ball at the bottom of a bowl on the left side of Figure 5-1 is in a stable equilibrium. If the ball is pushed slightly left or right, gravity and friction will eventually bring it back to rest at its starting position.

Figure 5-1 Equilibria: Stable (Left) & Unstable (Right)

The ball on the right side of Figure 5-1 is in an unstable equilibrium. If the ball were perfectly balanced and perfectly undisturbed, it might remain on top of the inverted bowl forever. But, any slight push exposes the ball to gravitational forces that push the ball ever farther from the top. Once this ball begins to move, it will never return to its starting position.

In the case of electrostatics, a charge Q placed exactly halfway between two equal charges q1 and q2 is in an unstable equilibrium. While it might remain there indefinitely in an ideal world, the slightest displacement will accelerate Q in one direction or another and it will never return to its starting position.

The question is: can a charged particle find a stable equilibrium in an electrostatic field? The answer is No, with one exception, as we will now show.

For any body to be stationary, the sum of all forces on that body must be zero. Let’s assume the only forces present are electrostatic. For a particle with charge +q to be stationary at position P, the electric field at P must be zero. For that particle to experience a restoring force for any slight displacement, the electrostatic force must point inward everywhere in the vicinity of P, which is shown at the center of Figure 5-2.

Figure 5-2 Restoring Forces P at Center Since q>0, this means the electric field E acting on q must point inward everywhere near P. Remember that the field acting on q does not include the field due to q; we do not permit charges to exert forces upon themselves.

Gauss’ law equates the flux of E through a closed surface to the charge within that surface. For the spherical surface of radius A sphere centered on P, whose cross-section is the thin circle in Figure 5-2, Gauss’ law says: 4π r² (-E) = Q/ε₀ Here, -E signifies that E is everywhere inward in this case. This means Q must be negative to provide the required restoring forces on the positively charged particle at P.

Our analysis shows that only if the positive particle is at exactly the same location as a negative charge, can it be in stable equilibrium. In empty space, there is no stable equilibrium for a charged particle in a non-zero electrostatic field.

Feynman then asks whether or not a stable equilibrium can exist for an assembly of charged particles. He considers two charges q₁ and q₂ attached to the ends of a rod at positions P₁ and P₂. The total force F on that rod must be inward everywhere to achieve stable equilibrium. The force is: F = q₁ E(P₁) + q₂ E(P₂)

Here E(P₁) is the electric field at P₁. We now take the divergence of F. In the vicinity of the rod, ∇·F must be negative if the vector field F is everywhere inward.

∇·F = q₁ ∇·E(P₁) + q₂ ∇·E(P₂)

In V2p5-2, Feynman says that in empty space ∇·E(P₁) and ∇·E(P₂) are both zero. That is a bit too fast; Feynman left something out that deserves discussion. We do not allow the field from q₁ to act on q₁, but it does act on q₂, and vice versa. To be more precise, let the total electric field be the sum of three parts: E₁: field due to q₁ E₂: field due to q₂ E₀: field due to all other remote charges With E₀ acting on both charges, and the field from one charge acting on the other but not on itself, the force equation is now: F = q₁ {E₂+E₀}(P₁) + q₂ {E₁+E₀}(P₂)

F = q₁ E₀(P₁) + q₂ E₀(P₂)

+ q₁ E₂(P₁) + q₂ E₁(P₂)

The lower line of the last equation is the force that q₁ and q₂ exert on one another. Since they are attached to the rod, the rod must exert an equal and opposite force to hold the charges in place. While we didn’t show that force in the total force equation, it is real and does cancel the lower line, leaving: F = q₁ E₀(P₁) + q₂ E₀(P₂)

Now take the divergence of this equation.

∇·F = q₁ ∇·E₀(P₁) + q₂ ∇·E₀(P₂)

If no other charges are in the vicinity of the rod, the divergence of E₀ is zero there. The equation reduces to: ∇·F = 0, which is incompatible with an inward-directed restoring force field.

With the same logic, we can add charges one by one and reach the same conclusion. This means a stable equilibrium does not exist for any rigid assembly of any number of charges in an electrostatic field in empty space.

However, if we introduce mechanical constraints, stable equilibria are possible. Figure 5-3 depicts a hollow tube that contains a positively charged particle (black dot) and constrains it to move only in the horizontal direction.

Figure 5-3 Charge in Tube in Field of Two Charges Two other positive charges, placed outside the tube along its axis, each produce an electric field that repels the positive charge within the tube. Exactly halfway between the two external charges, a stable equilibrium exists for the central charge. The tube exerts forces that prevent the central charge from moving up or down, and the fields from the external charges keep the central charge at the midpoint.

Should the central charge be displaced to the left, its distance r₁ to the left charge decreases and its distance r₂ to the right charge increases. The result is that the repulsive force from the left charge increases, since it is proportional to 1/r₁², while the repulsive force from the right charge decreases, since it is proportional to 1/r₂². The net effect is a force pushing the central charge to the right, back to the midpoint, thus maintaining equilibrium.

No Equilibrium Even With Conductors Continuing this investigation, Feynman now asks if a stable equilibrium is possible for a charge in empty space near conductors, since these allow charges to freely flow inside them.

Here again, there is no stable equilibrium for a charged particle in an electrostatic field.

We demonstrate this by considering a conductor of any shape and an isolated charge +q at position A, as depicted in part (1) of Figure 5-4. If position A did provide a stable equilibrium and we moved the charge to position B, as in part (2) of the figure, restoring forces would be required that would push the charge back to A.

Figure 5-4 Charges A & B Near Conductor (Dark Gray)

Let’s see why this is impossible. Moving charge +q from A to B is equivalent to leaving the original charge at A and adding a charge +q at B and a charge –q at A.

What happens to the charges in the conductor when we add +q at B and –q at A? Negative charges in the conductor will shift toward the new positive charge at B and away from the new negative charge at A. Also, positive charges will shift away from the new positive charge at B and toward the new negative charge at A. The total effect is to decrease the net charge near B (making that region more negative) and increase the net charge near A (making that region more positive).

re positive). That change produces a new electric field from the more positive vicinity of A toward the more negative vicinity of B, a field that adds to all previously existing fields. This new field pushes the charge +q at B away from A, which is exactly opposite of what a restoring force should do. Hence, there is no stable equilibrium at A, or at any other point outside the conductor.

In V2p5-2, Feynman concludes the investigation of stable equilibria in electrostatics by saying: “Our conclusions do not mean that it is not possible to balance a charge by electrical forces. It is possible if one is willing to control the locations or the sizes of the supporting charges with suitable devices. You know that a rod standing on its point in a gravitational field is unstable, but this does not prove that it cannot be balanced on the end of a finger. Similarly, a charge can be held in one spot by electric fields if they are variable. But not with a passive—that is, a static—system.”

Stability of Atoms

We have just shown that no stable equilibrium is possible for charged particles in empty space in an electrostatic field. This raises the interesting question: how can atoms be stable? How can electrons be stable in the electrostatic field of protons? The stability of atoms was a major, long-lasting mystery of science.

In V2p5-3, Feynman briefly reviews some failed attempts to explain the stability of atoms. British physicist J. J. Thompson discovered the electron in 1897, and received the 1906 Nobel Prize for his work. In 1904, Thompson proposed the “plum pudding” model of atoms: tiny electrons embedded here and there in a much larger amorphous mass of positive charge. The positively charged “pudding” held the electrons stationary by mechanical rather than electric forces.

But in 1909, scattering experiments performed by Hans Geiger and Ernest Marsden under the direction of Ernst Rutherford showed unexpected large-angle scattering of alpha particles incident on a gold foil. Rutherford correctly interpreted these results as demonstrating that atoms contain a very small, very massive, central core, contrary to Thompson’s model. Remarking on the first news of large-angle scattering, Rutherford said: “It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you. On consideration, I realized that this scattering backward must be the result of a single collision, and when I made calculations I saw that it was impossible to get anything of that order of magnitude unless you took a system in which the greater part of the mass of the atom was concentrated in a minute nucleus. It was then that I had the idea of an atom with a minute massive centre, carrying a charge.”

In 1911, Rutherford suggested atoms contained small positively charged nuclei surrounded by orbiting electrons. The orbital motion was intended to provide stability, as it does for planets orbiting stars. But that motion creates its own problem: circular motion requires acceleration (a change of direction), and accelerating charges radiate energy. This means electrons would rapidly lose energy and collapse into the nucleus.

In 1913, Niels Bohr proposed his atomic model with one essential improvement over Rutherford’s. Bohr said electrons are confined to a discrete set of orbits, unlike planets around stars. These allowed orbits must conform to rules of quantum mechanics, and no electron can ever orbit closer than the n=1 state, the allowed state with the least (most negative) energy.

A full and proper understanding of atoms will come when we study quantum mechanics in Feynman Simplified 3C. But we provide here some semi-classical insights. Quantum mechanics says that all particles, including electrons, have wavelengths given by: λ=h/p, where λ is the wavelength, h is Planck’s constant, and p is the particle’s momentum. The rule that specifies the allowed orbits can be stated in either of two equivalent ways: the orbital circumference must be an integral number of wavelengths (2πr=nλ); or the orbital angular momentum must be an integral multiple of h/2π (rp=nh/2π).

Additionally, the Uncertainty Principle of quantum mechanics explains why electrons cannot orbit arbitrarily close to the nucleus. If an electron is confined within a small distance Δx, Heisenberg says its momentum must span a range Δp given by: Δp=h/(4π Δx). An electron’s kinetic energy is proportional to p² and thus to +1/Δx². Its negative potential energy in the nuclear electrostatic field is proportional to –1/Δx. Hence, for a small enough Δx, as Δx decreases, an electron’s kinetic energy increases faster than its potential energy decreases. Without another source of energy, bound electrons don’t have enough energy to orbit very close to the nucleus. The math shows that an electron’s orbital radius, on average, cannot be smaller than 1 Bohr radius, the n=1 orbit.

about 0.529 angstroms.

Field From Charged Wire

We will now begin applying Gauss’ law to derive the electric field from several objects with special symmetries. In V2p5-3, Feynman says: “The ease with which these problems can be solved may give the misleading impression that the method is very powerful, and that one should be able to go on to many other problems. It is unfortunately not so. One soon exhausts the list of problems that can be solved easily with Gauss’ law. In later chapters we will develop more powerful methods for investigating electrostatic fields.”

For now, let’s enjoy the easy problems.

First consider the electric field from a wire of infinite length. Assume the wire has electric charge λ per unit length that is uniformly distributed throughout its length. By symmetry, the electric field E from the wire must be radially directed everywhere. If you understand why, skip to the next paragraph. For an infinite, uniform wire running from left to right, any point in space sees exactly the same infinite line of charge going to the left as going to the right. “By symmetry”, there is no physical reason to favor either left or right; hence, nothing of physical significance, including the field, can point left or point right. One might also wonder about a field that circles the wire like a ring. A ring field is excluded for two reasons: (1) the curl of E is zero in electrostatics; and (2) electrostatic field lines must start on positive charges and end on negative charges. The only remaining direction that E can have, in 3-D, is radial.

Now, we enclose part of the wire with a cylinder, as shown in Figure 5-5, and compute the flux of E through the surface of that cylinder.

Figure 5-5 Cylinder Enclosing Part of Infinitely Long Wire

Let r be the radius and L be the length of the cylinder. No flux passes through the flat end-faces of the cylinder that are perpendicular to the wire, because E is directed radially everywhere, parallel to the end-faces. The flux through the surface of the cylinder is: Flux through surface = 2π r L E(r)

The enclosed charge Q within the cylinder is: Q = λ L

By Gauss’ law: E(r) = λ / (2π ε r)

Field From Charged Plane

Next we consider the electric field from a plane surface of infinite length and width. Assume the plane has a positive electric charge density +σ per unit area that is uniformly distributed throughout the plane. By symmetry, the electric field E from the plane must be normal to its surface, and must have the same magnitude but opposite orientation above and below the plane. We enclose part of the plane with a box, as shown in cross-section in Figure 5-6. Let the box extend vertically a distance h above and h below the plane, and let the two lateral dimensions of the box be L.

Figure 5-6 Box Enclosing Part of Infinite Plane

No flux passes through the vertical surfaces of the box. The flux through the top and bottom surfaces are equal and their total is: Flux through top & bottom = 2L² E(h)

The enclosed charge Q within the box is: Q = σ L²

By Gauss’ law: E(h) = σ / 2ε

Note the perhaps surprising result that E(h) is not a function of h, the distance from the surface. The electric field from a plane has the same magnitude at every distance, all the way to infinity. That of course presumes an infinite plane of charge. Any actual plane must have finite dimensions, and E(h) would begin decreasing as h approaches the plane’s width.

Consider next two planes with opposite charges, as shown in Figure 5-7. We can find the E fields from each plane separately, as above, and then add them using the principle of linear superposition.

Figure 5-7 Two Oppositely Charged Planes

Note that the lengths of the arrows in Figure 5-7 are indicative of field extent not field strength; the two E fields have the same magnitude, as do the two E fields. Let the charge densities per unit area be σ⁺ for the upper plane and σ⁻ for the lower plane, with σ⁺ >0 and σ⁻ <0.

The magnitudes of the two electric fields are: E⁺ = +σ⁺ / 2ε₀ E⁻ = –σ⁻ / 2ε₀

Between the two planes, E⁺ and E⁻ are in the same direction. The net field is: Between two planes: E = (σ⁺ – σ⁻) / 2ε₀

Outside the planes (above both or below both), E⁺ and E⁻ are in opposite directions. If the number of positive charges on the upper plane exceeds the number of negative charges on the lower plane (if σ⁺ > –σ⁻), the net field points away from the planes with magnitude: Outside both planes: E = (σ⁺ + σ⁻) / 2ε₀

If σ⁺ = –σ⁻ = σ, if the charge densities are equal but opposite, we have: Between two planes: E = σ / ε₀ Outside both plates: E = 0

Field From Charged Ball

Next, we consider a ball of radius R with a uniform charge density ρ per unit volume. Feynman says this approximates a large atomic nucleus. The ball’s total charge equals its volume (4πR³/3) multiplied by ρ. Again by symmetry, the electric field E must be entirely radial everywhere. We define a spherical surface S with radius r that is centered on the ball.

ll’s center, as shown in Figure 5-8.

Figure 5-8 Charged Ball & Plot of E vs r

If S is inside the ball where r ≤ R, we have: Flux through S = 4π r² E(r)

Charge inside S = 4π ρ r³/3 Gauss’ law: E(r) = ρ r / 3ε Inside the ball, the field strength increases linearly with radius, as seen in the left portion of the plot in Figure 5-8.

If S is outside the ball where r ≥ R, we have: Flux through S = 4π r² E(r)

Charge inside S = 4π ρ R³/3 = Q Gauss’ law: E(r) = Q / (4πε r²)

This defines the curve in the right portion of the plot in Figure 5-8. The external field is the same as the field from a point charge Q, as we proved earlier.

Field Inside Charged Sphere Topologists define a sphere as the 2-D surface of a completely symmetric 3-D ball. Feynman calls that a shell. By either name, these are completely symmetric surfaces of zero or negligible thickness. If there is nothing inside such a surface, Gauss’ law tells us the interior E field is zero, even if the sphere itself is uniformly charged.

This is easy to prove. Imagine a spherical surface s of radius r inside a charged sphere S of radius R, with R>r, and with both spheres sharing the same center. Since the interior of the larger sphere is empty, there is no charge inside either sphere. This means the flux through s is zero, and by symmetry, this means E is zero everywhere on s. Since this is true for all r<R, E(r) is zero for all r<R.

Now, let demonstrate this another way: using Coulomb’s law instead of Gauss’ law. Consider a thin metal shell S with a uniform charge density of σ per unit area. We select any point P interior to the sphere. We then place at P the tips of two coaxial cones that each have cone angle θ. We extend the base of each cone to S, as shown in Figure 5-9. The common axis of the two cones may be oriented in any direction.

Figure 5-9 Two Cones With Tips at P In A Shell

Let r₁ be the distance from P to the left side of the sphere, and r₂ be the distance from P to the right side. For small θ, each cone subtends a circular area on the sphere of radius θ×(distance to P)/2. The area of the sphere subtended by each cone is: Left area: A₁ = πr₁² (θ/2)² Right area: A₂ = πr₂² (θ/2)²

The charge enclosed by each cone is σ•(subtended area). The electric fields at P due to the charge enclosed by each cone are: E₁(P) = σ πr₁² (θ/2)² /(4πε₀ r₁²) = σ θ² /(16ε₀)

E₂(P) = σ πr₂² (θ/2)² /(4πε₀ r₂²) = σ θ² /(16ε₀)

The two fields have exactly the same magnitude and point in exactly opposite directions. They therefore cancel at P. Since this is true for all cone orientations, and since we can divide the spherical surface into an infinite number of cone-pairs with infinitesimal cone angles, the total field at P from the entire spherical surface surrounding it is zero. Since P could be any point interior to the surface, we conclude that the electric field is zero throughout the sphere’s interior.

Feynman says that Benjamin Franklin is said to be the first person to discover that the field inside a metal sphere is zero.

Note that all the results obtained, from the charged line to the charged sphere, exactly match those derived for gravitation in Feynman Simplified 1A Chapter 10. This is because both the electrostatic E field and Newton’s gravitational field are inverse-square laws. None of these results would be valid if the distance dependence were anything other than 1/r².

Is the Inverse-Square Law Exact?

In V2p5-5, Feynman describes the experimental proof that this powerful inverse-square law is exact. How well do we know that the law isn’t 1/r²⁺ᵟ, for some small δ?

If we substituted 1/r² with 1/r²⁺ᵟ in the analysis of the charged sphere, the two electric fields would become: E₁(P) = σ πr₁² (θ/2)² /(4πε₀ r₁²⁺ᵟ)

E₂(P) = σ πr₂² (θ/2)² /(4πε₀ r₂²⁺ᵟ)

E₁(P) = σ θ² /(16ε₀ r₁ᵟ)

E₂(P) = σ θ² /(16ε₀ r₂ᵟ)

Now, if r₂ > r₁, E₂ will become less than E₁, and the field at P is no longer zero. The electric field would be greatest at all points inside the sphere that are near its surface. As Feynman says: “These conclusions suggest an elegant way of finding out whether the inverse square law is precisely correct. We need only determine whether or not the field inside of a uniformly charged spherical shell is precisely zero.”

Most extremely high precision experiments are null experiments: they directly measure small differences. It is generally very difficult to directly measure any physical quantity to a precision of, let’s say, 1 part per million (1 ppm) or better. Assume A and B are both about 1 million and that we measure each of them with a precision of ±1 ppm. The uncertainty in the difference of the measurements is ±√2. If A and B differ by 10, this is an uncertainty of ±14%. We would do much better if we could directly measure A–B with a precision of ±1 ppm.

For example, some American Quarter Horses can run a quarter-mile in under 21 seconds, passing the finish line at over 55 mph (about one inch per 0.001 seconds). If one horse ra In the track on Monday in 20.898 seconds, and another ran it on Tuesday in 20.899 seconds, no one with a manual stopwatch could be sure which horse was faster — human reflexes just aren’t fast enough to make such precise measurements. But if these two horses ran simultaneously in a real horse race, that difference — one inch — would be obvious in a photo finish.

When extremely high precision is needed, one important strategy is identifying a situation in which two effects cancel or almost cancel one another, and then measure their difference.

Hence, rather than trying to directly measure the exponent of radial dependence of the electric field, we obtain better precision by measuring the field inside a charged sphere, which cancels to zero if and only if the exponent of 1/r is exactly 2.

In 1873, Maxwell published an analysis claiming this exponent deviated from 2 by no more than 1 part in 21,600. In 1939, the experiment of Plimpton and Lawton showed that the deviation is no more than 2 parts per billion.

In 1971, E. R. Williams, J. E. Faller, and H. A. Hill achieved an amazing experimental result. A refined analysis by L. P. Fulcher in 1986, found the deviation δ was: δ = (1.0±1.2)×10–16. This is consistent with zero deviation from a pure 1/r² dependence.

One could interpret any deviation as being due to a non-zero photon mass. So interpreted, the Williams experiment sets this maximum limit: photon mass < 1.6×10–47 gram, photon mass < 1.8×10–17 electron mass.

The distance scale in the Williams experiment was 1.5 meters. With less precision, other experiments have confirmed the inverse-square law over distances of up to 10+11 m and down to 10–15 m, which is about the size of a proton. This is a total range of 26 orders of magnitude.

Electron-proton scattering experiments probing smaller distances than one proton diameter do show significant deviations from the inverse-square law. We now attribute these deviations to the proton not being a single point charge, but rather consisting of three charged quarks in complex “orbits.”

Fields In Conductors

As described above, measurements of fields within charged spheres have excluded deviations from the inverse-square law to 16 decimal digits. One might wonder whether such precision requires shells that are spherical to that same precision. That turns out to be unnecessary, which is very fortunate since such mechanical precision is unattainable. Indeed, the charged surface need not be spherical at all, any shape will do. It must however be conducting to ensure a uniform charge distribution.

Conductors are materials containing an abundance of electrons that can flow throughout the interiors of these materials with minimal resistance. The best conductors are metals. A dynamic external electric field can cause a continuing stream of electrons, an electric current, to flow within a conductor. But in an electrostatic situation, free electrons rapidly nullify any prior electric fields due to unbalanced charges within the conductor or external sources. With minimal resistance, electron flow stops only when E is exactly zero throughout the interior of a conductor. Since electrons in conductors flow at a substantial fraction of the speed of light, they reach a static condition extremely quickly.

Since E=0, the gradient of the electric potential inside a conductor is also zero. This means the potential is the same throughout the conductor’s interior and the entire conductor is an equipotential volume.

Even though the electric field is zero everywhere within a conductor, it can still have a net charge. Later in this course, Feynman shows that any net charge on a conductor lies on its surface; “within one or two atomic layers”, he says. We will assume here that any net charge exists only on a conductor’s surface.

In V2p5-8, Feynman says: “The electric field just outside the surface of a conductor must be normal to the surface. There can be no tangential component. If there were a tangential component, the electrons would move along the surface; there are no forces preventing that. Saying it another way: we know that the electric field lines must always go at right angles to an equipotential surface.”

At some point P on the surface of a conductor, we enclose a small portion of the surface with a box, as shown in Figure 5-10. Figure 5-10 Fields Ei Inside & EP Outside A Conductor

Since E is zero within the conductor, and is normal to the surface just outside the conductor, flux can only flow through the box face that is parallel to the surface and outside the conductor (the bottom face in the figure). If σ is the local charge density per unit area at P, Gauss’ laws tells us: Outside a conductor: E = σ / ε.

Feynman notes that this field is twice the field we derived for a plane with charge density σ. This difference here is that the charge on the surface at P is not the only charge in this situation. An isolated charged plane in empty space creates a field on both sides of its surface. Th The charge at P creates an inside field and an outside field, both of magnitude E=σ/2ε. This inside field must be canceled, since E=0 inside any conductor. The inside field due to the charge at P is in fact canceled by the field due to all the other surface charges, those not at P. The other charges create an outward-directed field at P of magnitude E=σ/2ε that cancels P’s inside field and doubles its outside field. We will not do the math here that demonstrates how the other charges “conspire”, as Feynman says, to accomplish this. However, if they didn’t so “conspire”, the field inside the conductor would not be zero.

Field in a Cavity Within a Metal

Having shown that E=0 within the interior of a conducting body, we can now show that E=0 inside an empty cavity of any shape inside a conductor of any shape. Figure 5-11 shows an odd-shaped dark gray conductor with a white cavity embedded in its interior.

Figure 5-11 White Cavity Within Gray Conductor

The figure shows possible positive and negative charges on the surface between the cavity and the body of the conductor; we will prove that such charges cannot exist. Figure 5-11 also shows a 1-D closed path Γ as a thin dashed curve, and the cross-section of a closed 2-D surface S as a broad dashed curve. S lies entirely within the body of the conductor and completely encloses the cavity. Since E=0 inside a conductor, the flux of E through S equals zero, and by Gauss’ law the net charge within S is zero. If the geometry were entirely spherically symmetric, this would prove that there were no charges within S. The current geometry, however, is not symmetric. For a surface of any shape, all that we can claim is that within S the amount of positive charge equals the amount of negative charge. Gauss’ law by itself does allow the charges indicated in Figure 5-11, provided that there are equal numbers of opposite charges.

As Feynman says: “any equal and opposite charges on the inner surface would slide around to meet each other, cancelling out completely.” We will prove this using the electrostatic equation that the curl of E is everywhere zero (∇×E=0). If there were separated positive and negative charges on the surface of a cavity inside a conductor, there would be field lines starting at a positive charge, traversing the cavity, and ending at a negative charge. We define path Γ in Figure 5-11 to start at a positive charge, follow such a field line across the cavity, and come back through the body of the conductor to that positive charge. Stokes’ theorem relates the integral of the normal component of the curl of any vector field across an area A enclosed by a curve Γ with the integral of the tangential component of that field along curve Γ. Recall from Chapter 3 that the equation is:

∫ (∇×E)•n da = ∫ E•ds

A          Γ

Here, n is the unit vector normal to surface A at each point, and ds is the incremental vector tangent to Γ at each point.

Since the curl of E is zero, we have:

0 = ∫ E•ds + ∫ E•ds

ΓC         ΓM

Here, we separated Γ into two parts: ΓC the portion through the empty cavity and ΓM the portion through the body of the metallic conductor. Since E=0 within the body of the conductor, the second integral above is zero. Also, by our definition of ΓC, E is always parallel to ds. The equation reduces to:

0 = ∫ E(s) ds

ΓC

If positive and negative really were separated on the cavity surface, E(s) would be greater than 0 all along ΓC, which is not allowed by the above equation. Hence, there cannot be any separated charges on the cavity surface, nor any fields within an empty cavity. Feynman notes that fields would exist within the cavity if there were fixed charges within it, such as charges in an insulating filling.

Thus, no static distribution of charges outside a conductor can produce electric fields in a cavity enclosed by that conductor. This explains why metal shielding protects electrical devices from external fields. The same logic in reverse proves that no static distribution of charges within a cavity enclosed by a conductor can produce fields outside that conductor.

As Feynman says: “Shielding works both ways!” He adds: “Now you also understand why it is safe to sit inside the high-voltage terminal of a million-volt Van de Graaff generator, without worrying about getting a shock—because of Gauss’ law.” Before trying that at home, be sure an expert sets up a proper Van de Graaff generator.

## Chapter 5 Review: Key Ideas

• Stable equilibrium is a state that doesn’t change if undisturbed, and that is self-restoring if slightly disturbed. In empty space, there is no stable equilibrium for a charged particle in an electrostatic field.

• A charged line of infinite length, with uniform charge density λ per unit length, produces a radial field E(r) given by: E(r) = λ / (2π ε r)

• A charged plane of infinite extent, with uniform charge density σ per unit area, produces a normal field E given by: E = σ / 2ε This field has the same strength at all distances from the plane. For two equal b ut oppositely charged planes, with uniform charge density σ per unit area, the fields are: Between two planes E = σ / ε Outside both plates E = 0 • A charged ball of radius R, with total charge Q and uniform charge density ρ per unit volume, produces a radial field E(r) given by: For r≤R: E(r) = ρ r / 3ε For r≥R: E(r) = Q / (4πε r2)

• Inside a sphere that is empty and conducting the electric field is zero, even if the sphere is charged.

• Experiments show the Coulomb field has a radial dependence of 1/r2+δ, where the deviation δ from a perfect inverse-square law is: δ = (1.0±1.2)×10–16 Interpreted as due to photons having a non-zero mass, the mass limit is: photon mass < 1.6×10–47 gram photon mass < 1.8×10–17 electron mass With varying precision, the inverse-square law is confirmed to distances of up to 10+11 m and down to 10–15 m, a total range of 26 orders of magnitude.

• A conductor, with local surface charge density σ per unit area, produces a normal external field E at its surface given by: E = σ / ε In a cavity within a conductor, the electric field is zero, regardless of charge density or the shapes of the conductor and cavity.

## Chapter 6 Dipole Electric Fields

In the next few chapters, we will explore the electric field in various static situations, while honing our new mathematical skills.

We found in Chapter 4 that the whole of electrostatics is embodied in two equations due to Maxwell: ∇•E = ρ / ε ∇×E = 0 Since the curl of any gradient is always zero, we can actually combine these into a single equation for the electric potential φ.

E = –∇φ ∇•∇φ = ∇²φ = – ρ / ε In rectilinear coordinates, the Laplacian operator ∇² is: ∇² = ∇•∇ = ∂2/∂x2 + ∂2/∂y2 + ∂2/∂z2 Hence, all the mathematics of electrostatics fundamentally amounts to solving the Laplacian equation for φ and then taking its gradient to obtain E.

For some problems, we begin knowing the charge distribution everywhere. These problems are particularly easy to solve. In Chapter 4, we found the potential φ at position r for two types of situations: (1) for discrete point charges q at positions r_j and (2) for a continuous charge distribution ρ(r). These are: φ(r) = (1/4πε₀) Σ q_j / |r–r_j| φ(r) = (1/4πε₀) ∫ {ρ(r') / |r–r'| } dV In the lower line, we integrate over all points r' in the space V containing the charge distribution ρ(r').

Feynman says the last few equations are well worth remembering, and not just for electrostatics. There are many situations in physics that are represented by equations of the form: ∇² X = Y These equations all have solutions of the form: Discrete: X(r) = α Σ Y_j / |r–r_j| Continuous: X(r) = α ∫ {Y(r') / |r–r'| } dV

Dipole Electric Fields Let’s begin with a simple example: the potential due to two opposite charges. We select a coordinate system such that the two charges are at: +q at (0,0,+d/2)

–q at (0,0,–d/2)

The potential is: 4πε φ(x,y,z) = +q / √[x² + y² + (z–d/2)²] –q / √[x² + y² + (z+d/2)²]

Now consider the important case in which the charge separation d is very small, much smaller than other distances of interest. In particular, for r² = x²+y²+z², we will assume d<<r.

The cleanest approach to evaluating φ for small d is differentiation.

Let W(δ) = 1/√[x² + y² + (z+δ/2)²]

W(δ) = [x² + y² + z² + zδ + δ²/4]–1/2 dW/dδ = (–1/2) [r² + zδ + δ²/4]–3/2 (z + δ/2)

In the limit of very small δ this reduces to: dW/dδ = (–1/2) [r²]–3/2 (z) = –z/2r³ By the definition of the derivative, we have: W(±d) = W(0) ± d (dW/dδ)

W(±d) = W(0) ± d (–z/2r³)

We can rewrite the equation for φ as follows: 4πε φ(x,y,z) = +q {W(0) – d (–z/2r³)} –q {W(0) + d (–z/2r³)} 4πε φ(x,y,z) = –qd (–z/2r³) –qd (–z/2r³)

φ(x,y,z) = q d z / (4πε r³)

In V2p6-2, Feynman derives the same result using several Taylor series that are very useful. Let’s see how this works.

As above, [x² + y² + (z±d/2)²] = [r² ± zd + d²/4]

We can drop d²/4 since we have assumed d<<r. The equation for φ is then: 4πε φ(x,y,z) = +q/√[r²–zd] –q/√[r²+zd]

4πε φ(x,y,z) = +q/r√[1–zd/r²] –q/r√[1+zd/r²]

To reduce clutter, define δ=zd/r², making our equation: 4πε φ(x,y,z) = +q/r√[1–δ] –q/r√[1+δ]

We now use the very useful Taylor series expansion: √(1±w) = 1 ±w/2 –w²/8 ±w³/16 – … Keeping only terms up to order w¹, the potential equation becomes: 4πε φ(x,y,z) = +q/r[1–δ/2] –q/r[1+δ/2]

Two other very useful Taylor series are: 1/(1–w) = 1 + w + w²/2! + w³/3! + ….

1/(1+w) = 1 – w + w²/2! – w³/3! + ….

To the same approximation, the potential equation reduces to: 4πε φ(x,y,z) = (q/r){ [1+δ/2] –[1–δ/2] } φ(x,y,z) = (q/r) {zd/r²} / (4πε)

φ(x,y,z) = q d z / (4πε r³)

Just as above.

The product qd is called the dipole moment. To reduce confusion and be consistent with other parts of these Lectures, I will use µ to denote the dipole moment. (In Volume 3, Feynman uses µ for dipole moment, but in parts of Volume 2, he uses p, which most of us associate with momentum.)

We can express the prior equation in vector notation. As we define our coordinate system, the separation d is along the z-axis. Hence, q•d•z φ(r) equals μ•r, where r=(x,y,z) and μ is a vector of magnitude qd that points from the negative charge to the positive charge. Note that μ is antiparallel to the electric field between the dipole charges. Thus, in vector notation: φ(r) = μ•r / (4πε r³).

We can write this yet another way by defining θ to be the angle between μ and r. With this definition: φ(r) = μ cosθ / (4πε r²).

Dipoles are important in nature. In many molecules, electric charge is balanced overall, but the centers of positive charge and negative charge are separated. Water is perhaps the most impactful dipolar molecule. The single oxygen nucleus pulls more forcefully on electrons than do the two hydrogen nuclei. This shifts electrons toward the oxygen and away from the hydrogens, making the oxygen side of a water molecule more positive than the hydrogen side. The dipole moment of water is equivalent to separating water’s 10 positive charges and 10 negative charges by 0.039 angstroms (0.0039 nm).

Taking our earlier version of potential φ, let’s calculate the electric field due to a dipole. Before we do, it will help to compute dr/dz. dr/dz = d(x²+y²+z²)^(1/2)/dz = (1/2)(x²+y²+z²)^(-1/2)(2z) = z/r. The x and y derivatives are clearly similar.

Now let’s calculate E, beginning with E_z. E_z = –∂φ/∂z = –∂{μz/(4πε r³)}/∂z. E_z = –(μ/4πε){1/r³ – 3z(dr/dz)/r⁴} = –(μ/4πε){1/r³ – 3z(z/r)/r⁴} = –(μ/4πε){1/r³ – 3z²/r⁵}.

Since z = r cosθ, we can write this: E_z = (μ/4πε) (3 cos²θ – 1)/r³.

Now the x-component: E_x = –(μz/4πε){–3(dr/dx)/r⁴} = –(μz/4πε){–3(x/r)/r⁴} = (μ/4πε){3xz/r⁵}.

By symmetry, the y-component is: E_y = (μ/4πε){3yz/r⁵}.

We can define the transverse component E_t, the component orthogonal to the dipole moment, as: E_t = √(E_y² + E_x²).

Recall the polar to rectilinear coordinate relationships: x = r sinθ cosβ, y = r sinθ sinβ, z = r cosθ. Here β is the azimuthal angle. Normally, one uses φ for the azimuthal angle, but I am switching to β here because we are using φ for the electric potential. These relationships mean: y² + x² = r² sin²θ (cos²β + sin²β), so √(y² + x²) = r sinθ.

Combining all this yields: E_t = (μ/4πε r³) (3 sinθ cosθ), E_z = (μ/4πε r³) (3 cos²θ – 1), and E_total = √(E_t² + E_z²) = (μ/4πε r³) √(3 cos²θ + 1). Note that the total field strength E at θ=0 is twice its value at θ=π/2, being proportional to √4 vs. √1. Thus, the field is twice as strong along the dipole axis where E is parallel to μ, as compared with the mid-plane equally distant from both charges where E is antiparallel to μ.

The above equation for E follows because: E_t² + E_z² = E_total². E_total² (4πε r³/μ)² = (9 sin²θ cos²θ) + (9 cos⁴θ – 6 cos²θ +1) = 9 cos²θ – 6 cos²θ +1 = 3 cos²θ +1.

Figure 6-1 shows a plot of E in the y=0 plane, with μ pointing up toward +z, and x being the horizontal axis.

Figure 6-1 Image of Dipole Field by HyperPhysics.

In V2p6-4, Feynman provides this sage advice on vector analysis: “The fundamental proofs can be expressed by elegant equations in a general form, but in making various calculations and analyses it is always a good idea to choose the axes in some convenient way. Notice that when we were finding the potential of a dipole we chose the z-axis along the direction of the dipole, rather than at some arbitrary angle. This made the work much easier. But then we wrote the equations in vector form so that they would no longer depend on any particular coordinate system. After that, we are allowed to choose any coordinate system we wish, knowing that the relation is, in general, true. It clearly doesn’t make any sense to bother with an arbitrary coordinate system at some complicated angle when you can choose a neat system for the particular problem—provided that the result can finally be expressed as a vector equation. So by all means take advantage of the fact that vector equations are independent of any coordinate system. On the other hand, if you are trying to calculate the divergence of a vector, instead of just looking at ∇•E and wondering what it is, don’t forget that it can always be spread out as: ∂Ex/∂x + ∂Ey/∂y +∂Ez/∂z. If you can then work out the x-, y-, and z-components of the electric field and differentiate them, you will have the divergence. There often seems to be a feeling that there is something inelegant—some kind of defeat involved—in writing out the components; that somehow there ought always to be a way to do everything with the vector operators. There is often no advantage to it. The first time we encounter a particular kind of problem, it usually helps to write out the components to be sure we understand what is going on. There is nothing inelegant about putting numbers into equations, and nothing inelegant about substituting the derivatives for the fancy symbols. In fact, there is often a certain cleverness in doing just that. Of course when you publish a paper in a professional journal it will look better—and be more easily understood—if you can write everything in vector form. Besides, it saves print.”

Dipole as a Gradient: We can rewrite e the dipole equation in an interesting way: ø(r) = µ•r / (4πε r3) = – (1/4πε) µ•Ď(1/r)

We demonstrate this as follows (recall that ∂r/∂z=z/r): Ď(r–1) = (∂r–1/∂x, ∂r–1/∂y, ∂r–1/∂z)

Ď(r–1) = [–1][r–2] (x/r, y/r, z/r)

Ď(1/r) = – r / r3

Feynman notes that this makes sense physically: r/r3 is the radial factor of E from a point charge, and E equals minus the gradient of the potential ø, whose radial factor is 1/r.

We can see the reason for this in yet another way. (Seeing something from different angles can better reveal its true nature.) Let’s imagine starting with two equal but opposite charges +q and –q, both located at (0,0,0). Clearly the two fields cancel and E=0 everywhere. Now imagine that we move +q slightly up the z-axis and move –q slightly down the z-axis. This creates a dipole. We will calculate the dipole’s potential by calculating the potential from each charge separately, and then adding them.

Recall from Chapter 4, the potential ø(r) from a point charge +q at position σ: ø(r) = (+q/4πε) / |r–σ| When σ=0, this reduces to the more familiar equation. Now let’s find how ø changes as we move +q slightly up the z-axis by distance Δσ. In V2p6-5, Feynman says moving the charge up is equivalent to moving the coordinate axes down by Δσ, which necessitates less math. This means taking the derivative of ø with respect to z in the vicinity of σ=0.

Δø = – ∂ø/∂z Δσ Δø = (–q/4πε) Δσ ∂(r–1)/∂z

This is the change in ø(r) due to moving charge +q from σ=(0,0,0) to σ=(0,0,Δσ). The potential itself equals its value for +q at (0,0,0) plus this Δø. This is: 4πε ø(r) = +q/r + q (–Δσ) ∂(r–1)/∂σ

Similarly, the potential from a charge –q at σ=(0,0,–Δσ) is: 4πε ø(r) = –q/r – q (+Δσ) ∂(r–1)/∂σ

The sum of the potentials from both charges is: 4πε ø(r) = – 2q (Δσ) ∂(r–1)/∂σ

Here 2(Δσ) is the distance between +q and –q, which is the dipole displacement d, and 2q(Δσ) is the dipole moment µ. Making that substitution yields: 4πε ø(r) = – µ ∂(r–1)/∂σ

We can recast this equation in vector form by realizing that its right hand side is the product of the z-components of two vector quantities. This is because we chose to align the z-axis with the dipole displacement. In any other coordinate system, the right hand side would be the dot product of these vector quantities. The generalized vector equation for the dipole potential is: ø(r) = – µ•Ď{ 1/(4πε r) }

The quantity in { }’s is the potential due to a unit charge.

In V2p6-5, Feynman says the technique used above is well worth remembering. He says: “Although we can always find the potential of a known charge distribution by an integration, it is sometimes possible to save time by getting the answer with a clever trick. … If we are given a charge distribution that can be made up of the sum of two distributions for which the potentials are already known, it is easy to find the desired potential by just adding the two known ones.”

Here’s another example: a sphere with a charge distribution that is proportional to the cosine of its polar angle. Although that sounds odd, it will arise when we study dielectrics. In polar coordinates, the sphere’s charge density is given by: σ(r,θ,β) = σ cosθ

Overall, the sphere has zero net charge, but it has excess positive charges near θ=0 and excess negative charges near θ=π. Feynman says we can model this sphere as the sum of two slightly displaced balls, one with uniform positive charge and the other with uniform negative charge, as shown in cross-section in Figure 6-2. Note that in this discussion, Feynman uses “sphere” unconventionally and inconsistently. A completely symmetric 3-D spherical body is properly called a ball; its 2-D surface is a sphere. Feynman calls both of these spheres.

Figure 6-2 Displaced Oppositely Charged Balls

Let the balls have radius R, and let their charge densities and centers be: Charge: +ρ; Center at (0,0,+d/2)

Charge: –ρ; Center at (0,0,–d/2)

Feynman says “you can show that” the balls’ net charge distribution is equivalent to a sphere with charge density: σ(θ) = σ cosθ

The resulting external and internal electric fields are: External: dipole field with µ = σ 4π R3/3 Internal: constant field E = – σ / 3ε

You may wish to tackle this challenge. Answers are provided at the end of this chapter.

Dipole Component of Complex Charges

Electric dipoles often play important roles in objects with complex charge distributions, such as molecules. Imagine an extended object with an arbitrary distribution of discrete charges q at positions d. Select any remote point P at position R, and define r to be the vector from charge q to P, as shown in Figure 6-3.

Figure 6-3 Dipole From Arbitrary Charge Distribution

Choose a coordinate system with its origin at the center of the charges; specifically we want the sum of d = (0,0,0). In saying that P is remote, we mean |R|>>|d| for any j. As the figure shows, for each charge #j: r + d = R |r|2 = |R–d|2 |r|2 = R•R –2R•d + d•d |r|2 =R2 (1 – 2R•d/R2 + d•d/R2)

The potential ø(R) is: ø(R) = (1/4πε) Σ { q / r } 0 j j j

We will now make a series of approximations of increasing precision. This will demonstrate what we can learn from each level of approximation.

Start with the crudest approximation: r=R for all j. This assumes P is so remote that the distances between individual charges q are completely insignificant; specifically, this assumes |d/R|=0. The potential then reduces to: j j ø(R) = (1/4πε) Q / R with Q = {Σ q } j j

Here, P is only affected by the object’s total charge Q. For many purposes this approximation is sufficient.

But, this is not the only affect that the charges q might have on P. To learn more, we need a more precise approximation. Recall from the description of Figure 6-3 that for each r: |r|2 = R2 (1 – 2R•d/R2 + d•d/R2)

j j j j

Define e to be the unit vector in the R direction (e =R/|R|). We now make a more precise approximation, keeping terms of order |d/R| and dropping smaller terms like |d/R|2. With the Taylor series approximations presented earlier, we have: R R j j r = R (1 – e •d / R)

j R j 1/r = (1/R) (1 + e •d / R)

j R j

The potential equation is then: ø(R) = (1/4πε) Σ { q (1 + e •d / R) /R} 0 j j R j ø(R) = (1/4πε) { Q/R + Σ q e •d /R2} 0 j j R j

We define the total dipole moment of the charge distribution as: µ = Σ q d j j j

This assumes the sum of d = (0,0,0). Then: ø(R) = (1/4πε) { Q/R + e •µ /R2} 0 R

The first term is the field from net total charge Q. At large R, this term dominates unless the object is nearly neutral. The second term is the dipole field due to µ. For many neutral objects, this is the dominant term. Water, for example, is highly reactive due to its strong dipole moment.

If we kept even smaller terms, such as |d/R|2, we would find a quadrupole term proportional to 1/R3. Carbon dioxide, for example, has zero net charge and zero dipole moment, but has a substantial quadrupole moment.

Fields From Oppositely Charged Balls

Here are the answers to Feynman’s suggested problems.

We must first examine a horizontal slice of a 3-D ball, as shown in Figure 6-4. We must calculate the volume of that slice, and also the area of the ball’s surface contained in that slice. Here, Z is the vertical axis, z is the vertical coordinate of the slice, dz is the slice thickness, R is the radius of the ball, and θ is the polar angle.

The horizontal slice through the ball is shown in dark gray. The ball’s corresponding surface area is shown in black; in cross-section we see only the left and right sides of this continuous band. Assume the ball has uniform charge density ρ per unit volume, and its surface has a varying charge density σ per unit area.

From the figure we see: z = R cosθ dz = – R sinθ dθ r = R sinθ r2 = R2 – z2

The charge dQ contained on the ball’s surface within the horizontal band equals its (charge density σ) times (circumference 2πr) times (width Rdθ), which is: dQ = σ (R dθ) 2π (r)

dQ = 2π σ R (R sinθ) dθ dQ = 2π σ R (–dz)

The charge dQ contained within the ball’s interior in the horizontal slice equals its (charge density ρ) times (height –dz) times (horizontal area πr2), which is: dQ = ρ (–dz) πr2 dQ = ρ (–dz) π(R2 – z2)

We now examine the problems Feynman suggested.

Two balls of uniform charge density +ρ and –ρ are displaced vertically by distance d, with the positive ball centered at z=+d/2 and the negative ball centered at z=–d/2. Moving a ball up d/2 is equivalent to moving the coordinate system down d/2. This means the charge contained in the horizontal slice due to the upper ball is: upper ball: dQ = +ρ (–dz) π{R2 – (z–d/2)2}

Similarly, the charge contained in the horizontal slice due to the lower ball is: lower ball: dQ = –ρ (–dz) π{R2 – (z+d/2)2}

We next sum those to obtain the total charge from the two balls: 2 balls: dQ = ρ (–dz) π {zd + zd} 2 balls: dQ = 2π ρ Rcosθ d (–dz)

For a sphere to contain the same amount of charge in the same horizontal band, its charge density must be given by: 2π σ R (–dz) = 2π ρ R cosθ d (–dz)

σ = ρd cosθ = σ cosθ where we define σ = ρd.

This proves Feynman’s first claim that two displaced oppositely charged balls have a charge distribution equivalent to a sphere with a cosθ charge distribution.

Now consider the dipole moment of these two charged balls. By symmetry, the dipole moment must be along the Z-axis; hence, we will deal only with the Z-components. We can write the equation of the dipole moment of a collection of charges as: µ = Σ (+q d) + Σ (–q) d U:j j j L:j j j

Here the first sum is for the upper ball and the second for the lower ball. Recall that the balls are identical in every way except that they have opposite charges. For every point in the upper ball, there is a corresponding opposite charge in the lower ball that is displaced by d in the –Z-direction. Therefore, we arrange the summation in corresponding pairs, as: µ = Σ { +q d –q (d –d) } j j j j j µ = Σ { +q d } = d Σ q j j j j is the total charge of one ball, the dipole moment of the two displaced balls is: µ = Q d = ρ d 4πR³/3 = σ 4πR³/3 That was the second of Feynman’s suggested problems. The last one concerns the electric field within the two slightly displaced balls. From Chapter 5, the field inside a uniformly charged ball centered at (0,0,0) is: E(r) = ρ r / 3ε Here, we have expressed this relationship in vector form, which is particularly easy since the field from a completely symmetric ball is always radial. Next, we displace the above field by ±(d/2)e, where e is the unit vector in the Z-direction.

upper ball: E(r) = +ρ (r – e d/2) / 3ε lower ball: E(r) = –ρ (r + e d/2) / 3ε The components of E for the sum of both balls are: Eₓ = { +ρ (x) –ρ(x) } / 3ε = 0 E_y = { +ρ (y) –ρ(y) } / 3ε = 0 E_z = { +ρ (z–d/2) –ρ(z+d/2) } / 3ε = –ρd / 3ε E_z = – σ / 3ε QED

## Chapter 6 Review: Key Ideas

• The Laplacian operator in rectilinear coordinates is: ∇² = ∇•∇ = ∂²/∂x² + ∂²/∂y² + ∂²/∂z² Many physical situations are represented by equations of the form: ∇² X = Y These equations all have solutions of the form: Discrete set of Y: X(r) = α Σ Yⱼ / |r–σⱼ| Continuous Y(σ) : X(r) = α ∫ Y(σ)/|r–σ| dV • For electrostatic charge density ρ: ∇²ø = – ρ / ε₀ ø(r) = (1/4πε₀) Σ qⱼ / |r–σⱼ| ø(r) = (1/4πε₀) ∫ ρ(σ)/|r–σ| dV • Dipole Moment: for two equal but opposite charges +q and –q, separated by vector d, the dipole moment µ and electric potential are: µ = qd, µ points from –q to +q.

ø(r) = µ•r / (4πε₀ r³) = – (1/4πε₀) µ•∇(1/r)

For any collection of discrete charges qⱼ at positions dⱼ, with sum of dⱼ = 0, and any remote position R: Total net charge Q = Σ { qⱼ } Dipole Moment µ = Σ qⱼ dⱼ ø(R) = (1/4πε₀) { Q/R + e_R •µ /R²} • Two charged balls with uniform charge densities +ρ and –ρ that are displaced by distance d have a net charge distribution equivalent to a spherical surface whose charge density is proportional to the cosine of its polar angle: σ=σ₀ cosθ, where σ₀ =ρd. The balls’ dipole moment and internal electric field are: µ = σ₀ 4πR³/3 E = – σ₀ / 3ε • Some useful Taylor series expansions are: √(1±w) = 1 ±w/2 –w²/8 ±w³/16 – … 1/(1–w) = 1 + w + w²/2! + w³/3! + ….

1/(1+w) = 1 – w + w²/2! – w³/3! + ….

## Chapter

Charges & Conductors In V2p6-8, Feynman says: “We have now finished with the examples we wish to cover of situations in which the charge distribution is known from the start. … We turn now to an entirely new kind of problem, the determination of the fields near charged conductors.” In this new kind of problem, the charge distributions within the conductors are initially unknown.

Fields of Charged Conductors If a conductor has a non-zero charge Q, that charge will spread across the conductor’s surface in a way that minimizes total energy, and that makes the entire conductor an equipotential. Individual charges move to the surface because that increases their separation and minimizes potential energy. The electric potential must be the same throughout a conductor, because any potential differences would create electric fields that would relocate charges until those electric fields were neutralized.

Feynman says there is no general analytical procedure to calculate the charge distribution on an arbitrary conductor. One can guess a trial distribution and use that to calculate the potential. If the potential is the same everywhere, the guess is correct. If not, that effort might inform a better guess. This is an ideal job for a computer, since it doesn’t get bored.

Alternatively, we can learn some tricks of the trade from a master.

Method of Image Charges The first trick is replacing conductors with image charges.

Let’s try a simple example: a charge near a plane. Figure 7-1 shows a horizontal conducting plane (in gray), and a point charge +q located a distance d above the plane. (Ignore the lower half of the image for now.) The figure shows a thick plane for clarity, but in our analysis, let’s assume it is extremely thin. The field lines at the plane must be perpendicular to it, because a conducting plane is an equipotential surface.

Figure 7-1 Point Charge Above Conducting Plane Let the z-axis be vertical, the x-axis be horizontal, and the y-axis be into the screen. Set the origin (0,0,0) at the plane immediately below charge +q that is at (0,0,+d). Define ρ to be the distance from (0,0,0) to any point P in the plane, which means: ρ² = x² + y² Now we replace the plane with an imaginary charge –q at (0,0,–d). This imaginary charge, called an image charge, is shown in Figure 7-1 in light tones. The essence of this trick is that the electric field everywhere above the conductor is exactly the same, either with the conductor or with the image charge.

Since the plane is halfway between opposite charges, its potential is zero.

With this trick, we can calculate the field for charge +q near a zero-potential conducting plane by using the dipole equation for that charge and an image charge –q.

In this case, a negative charge density is induced on the plane's surface that faces charge +q. This negative charge density σ(P) must create the same electric field that would be created by image charge –q. From the field at the plane's surface, we can calculate the charge density at any point P in the plane using Gauss' law: σ(P) = ε₀ E(P)

We get E(P) from the dipole equation with the image charge. Define r₊ to be the vector from charge +q to P and r₋ to be the vector from charge –q to P. By symmetry |r₊|² = |r₋|² = d² + ρ².

The field at P is: 4πε₀ E(P) = +q r₊/r₊³ – q r₋/r₋³ Since E is perpendicular to the plane at z=0, only the z-components of r₊ and r₋ contribute, the orthogonal components must cancel. The z-component of r₊ is –d and that of r₋ is +d.

The equations for E and σ become: 4πε₀ E(P) = +q(–d)/r₊³ – q(+d)/r₋³ σ(P) = –2qd / {4π (d²+ρ²)^{3/2} } Feynman suggests checking this result by integrating it over the whole plane. This is: ∫ σ = ∫ σ(ρ) 2πρ dρ, from ρ=0 to ∞ ∫ σ = – ∫ (qd/2π) (d²+ρ²)^{-3/2} 2πρ dρ Let u = ρ / d.

∫ σ = –qd ∫ d^{-3} (1+u²)^{-3/2} d² u du ∫ σ = –q {–(1+u²)^{-1/2}} ∞ = –q {–0 +1} = –q This is the required result: the total dipole charge equals zero, hence the plane's total charge must equal the image charge –q.

We can also calculate the force on charge +q — either by integrating the force due to the plane's charge distribution σ(ρ), or from the force due to the image charge –q. The second is clearly easier: F = (–e) (1/4πε₀) q² / (2d)² Here, e is the unit vector in the +z-direction.

Now we examine another example, using our trick in reverse: replacing a charge with a conductor. Consider a dipole formed by charges +q and –q, as shown in Figure 7-2. (Ignore the gray ellipse for the moment.) Here the dotted lines are equipotential surfaces, seen in a 2-D cross-section. Recall that electric fields, and thus field lines, are always perpendicular to equipotentials.

Figure 7-2 Charge Near Conductor We now replace the negative charge in the lower half of Figure 7-2 with a conductor (the gray ellipse), ensuring that the field outside the conductor does not change. To accomplish this, the conductor's surface S (the bold black curve) must exactly match an equipotential surface of the original dipole. (Compare the lower half and upper half of the image.) Additionally, the conductor's net charge must equal –q to ensure zero net flux through any large surface enclosing both the conductor and the charge +q.

As discussed in Chapter 5, the fields inside and outside a conducting surface are completely independent. The fields outside the gray conductor are unaffected by what happens inside the conductor: the conductor could be solid (as shown) or hollow.

This particular conductor has an ellipsoidal shape. We can now easily calculate the field from a point charge outside an ellipsoid. We simply imagine replacing the ellipsoid with a point charge of the opposite polarity and use the dipole field equation.

One final image charge example: a point charge +q at a distance b from the center of a conducting ball of radius R. Since the outside fields are independent of the fields inside a conductor, it makes no difference whether the conductor is a solid ball (as shown) or a hollow 2-D spherical surface.

Figure 7-3 Charge +q Near Conducting Ball Place an image charge Q along the symmetry axis at a distance d from the ball's center. We will now show that, for the right values of Q and d, replacing the ball with the image charge does not change the external field.

For any point P on the ball's surface, define the distance from P to +q to be r₁, and the distance from P to Q to be r₂. The potential at P equals the sum of the potential due to +q and the potential due to Q. This is: 4πε₀ ø(P) = +q/r₁ + Q/r₂ Since the ball is a conductor, it must have the same potential for all points P. One solution is to require the sphere to have zero potential, which means: 0 = +q/r₁ + Q/r₂ –Q/q = r₂/r₁ In V2p6-10, Feynman says a sphere satisfies this requirement because: "a sphere is the locus of all points for which the distances from two points are in a constant ratio." This nice theorem is due to Apollonius of Perga. Even if you missed that in geometry class, as did I, we can still solve this equation.

Moving P to the point on the sphere closest to +q, we find: r₁ = b – R r₂ = R – d (–Q/q) = (R–d) / (b–R)

Moving P to the point on the sphere farthest from +q, we find: r₁ = b + R r₂ = R + d (–Q/q) = (R+d) / (b+R)

Combining these yields: (R+d) / (b+R) = (–Q/q) = (R–d) / (b–R)

(R+d) (b–R) = (R–d) (b+R)

Rb –R² + db – dR = Rb + R² – db – dR 2db = 2R² d = R²/b (–Q/q) = (R–R²/b) / (b–R)

(–Q/q) = (bR–R²) / b(b–R) = R/b Q = –qR/b As noted earlier, this is one solution that provides an equipotential throughout a ball of radius R whose center is a distance b from an external point charge +q. In this solution, the potential of the ball is zero.

If we now add a charge Q* to the ball, its potential will change but the ball will remain an equipotential.

The principle of linear superposition allows us to add any charge we wish. Outside the ball, the electric field and electric potential are simply obtained by summing those due to +q, due to Q, and due to Q*. The force attracting +q to the ball is: F = –(1/4πε) {+qQ/(b–d)² + qQ*/b²} F = –(1/4πε) q(–qR/b) {1/(b–R²/b)² + Q*/Qb²} F = (1/4πε) (q²R/b³) {1/(1–R²/b²)² + Q*/Q}. Even if the total charge of the ball is zero, if Q*=–Q, the ball and the point charge +q will attract one another. The point charge +q induces an excess negative charge on the side of the ball nearest +q, and also induces an excess positive charge on the opposite side. Since +q is closer to the excess negative charge than to the excess positive charge, the lone charge and the ball attract one another. This is the same effect that we discovered in the mutual attraction of neutral atoms. (See Feynman Simplified 1A Chapter 9.) For Q*=–Q the net attractive force on +q is: F = (1/4πε) (q²R/b³) {1/(1–R²/b²)² –1}. In V2p6-11, Feynman muses about the force between two charged spheres. One can easily calculate the force assuming all their charge is at their centers. Or one could imagine the left sphere inducing an image charge in the right sphere, which induces an image charge in the left sphere, which … ad infinitum. This is like standing between two mirrors. Feynman says the resulting infinite series converges rapidly.

Parallel-Plate Capacitors: Next we consider two charged conducting parallel planes, as shown in Figure 7-4. Assume the plates have charge densities +σ and –σ, and are separated by distance d. As we found in Chapter 5, the field between the plates is σ/ε. Since the electric field equals minus the gradient of potential, we have (with z being the vertical axis): E = –∂φ/∂z. E Δz = –∂φ/∂z Δz. E (–d) = – Δφ. E d = Δφ = φ₊ – φ₋. V = E d = d σ/ε. Here φ₊ and φ₋ are the potentials of the positive and negative plates respectively, and V is the voltage difference between the plates. V is the work required to move a charge +1 from the negative plate to the positive plate, or equivalently, the energy released by moving a charge –1 from the negative plate to the positive plate. If the area of each plate is A, the total charge on each plate is given by: Q = ±σ A. Substituting this expression into the equation for voltage yields: V = Q d/Aε = Q / C. C = Aε/d, for two parallel plates. Here we define C to be the capacitance of the capacitor formed by two plates with area A and separation d. Capacitors were once called condensers, but that term is largely obsolete. The voltage across a capacitor is proportional to the charge it stores.

In V2p6-12, Feynman stresses that the linear relationship between capacitor charge and voltage is a consequence of the principle of linear superposition: doubling the charge, doubles the field, which doubles the voltage. From V = Q/C, we see that C has the units of coulombs per volt. A capacitor able to store 1 coulomb with a potential difference of 1 volt has a capacitance of 1 farad, a unit named in honor of Michael Faraday. In Feynman’s day, 1 farad was considered an enormous capacitance. Typical capacitances were in the picofarad to millifarad range (10⁻¹² to 10⁻³ farads). However, with modern technologies, even 400-farad capacitors are now quite reasonable, in both size and price.

From C = Aε/d, we see that ε has units of farads per meter, with a value of: ε₀ ≈ 8.854 picofarad / meter. Capacitors are ubiquitous in electronic circuitry. One picofarad, called 1 puff in physics slang, is approximately the capacitance of two 1 square-centimeter plates held 1 millimeter apart. I stress this because a theoretical physics student at Stanford was asked in his Ph.D. oral exam to guess the capacitance of two paper clips placed 1 centimeter apart. He would have passed even if his answer had been 100 times too high or too low. But he said “1 farad”, and was immediately failed. His professors thought even theorists should know at least something about hands-on physics. He was sent to a lab, and passed his orals a few months later.

Capacitors can take other shapes. The capacitance of a sphere of radius r is: C = 4πε r, for a sphere. Here, the “other side” of the capacitor is a sphere of infinite radius. This follows from our definition of potential. Recall our definition: φ = Q / (4πε r). The potential φ is zero at an infinite distance. Since φ and V both represent electric potential, and C=Q/V, we obtain the above equation for a sphere’s capacitance relative to infinity.

High-Voltage Breakdown: Recall the above expression for potential difference V: V=Ed. When the potential changes rapidly over short distances, the electric field grows extremely large, eventually with dramatic consequences. Consider the electric field near the sharply curving end of the conductor shown in Figure 7-5. Feynman says we can qualitatively understand why the field is strongest near a sharp tip. The charge density is higher at a sharp tip, and the field is proportional to the charge density.

at the tip, because charges there are farther from the bulk of the conductor than are charges along smoother parts of the surface.

Figure 7-5: Field Peaks At A Sharp Tip

Feynman offers a second, more quantitative explanation for the field peaking at a tip. Consider two conducting balls, one much larger than the other, that are connected by a conducting, infinitesimally thin wire, as shown in Figure 7-6.

Figure 7-6: Two Balls Connected by Wire

While the wire keeps the two balls at the same potential, Feynman says it has little impact on the fields around the two balls. Let the larger ball have radius R and charge Q, and let the smaller ball have radius r and charge q. The potential on the surface of both balls must be the same. Hence: (1/4πε₀) (q/r) = φ = (1/4πε₀) (Q/R)

q/r = Q/R q = Q (r/R)

The electric fields on the larger and smaller balls’ surfaces are: E_L = (1/4πε₀) Q/R² E_S = (1/4πε₀) q/r² E_S = (1/4πε₀) (Qr/R) /r² E_S = (1/4πε₀) Q /(rR)

E_S = E_L (R²)/(rR) = E_L (R/r)

For any given radius R of the large ball, the surface field of the small ball is inversely proportional to its radius — the smaller its radius, the larger its field.

This has important practical consequences. Air has a breakdown voltage of 3.0 million volts/meter (MV/m), in ideal conditions. If an electric field exceeds that level, electrons are torn from air molecules and accelerate toward the source of positive voltage. Each accelerating electron knocks other electrons from their atoms, creating an avalanche called an arc or a spark. On a small scale, this is what ignites gasoline in a car’s engine. On a very large scale, this is called lightning. For comparison, the ideal breakdown voltage is: up to 15 MV/m in mineral oil; up to 70 MV/m in pure water; 2000 MV/m in diamond; and 10¹⁵ V/m in a perfect vacuum. To avoid breakdown, high-voltage devices are carefully constructed to eliminate sharp corners.

Field Emission Microscopy One application of intentional voltage breakdown is field emission microscopy, one version of which is depicted in Figure 7-7.

Figure 7-7: Electron Field Emission Microscope

Here an electrode (dark gray) with a very sharp tip is held at a large negative voltage in a vacuum chamber. Electrons emitted at the tip accelerate toward a detection screen (shown in light gray) held at zero volts. Feynman says that, to a good approximation, electrons travel undeflected along radial lines from tip to screen. The pattern of screen impact points thus provides an image of the emitting tip, with a resolution of a few nm. Resolution is limited with electrons, due to their relatively long wavelengths and large, random, initial velocities. An alternative version achieves higher resolution by adding a small concentration of helium gas to the chamber, and setting the tip potential to a large positive voltage. A helium atom arriving at the tip is stripped of an electron, and the resulting ion accelerates toward the screen. Since helium ions have both shorter wavelengths and smaller initial velocities than electrons, this version has achieved resolutions of 0.5 nm, comparable to the size of a large atom. Figure 7-8 shows a helium-ion field emission microscope image of a platinum tip. Each dot is the image of an individual platinum atom.

Figure 7-8: Image due to Tatsuo Iwata

## Chapter 7 Review: Key Ideas

• Image charge: calculating fields near conductors is sometimes simplified by judiciously replacing conductors with image charges. The trick is to ensure that the image charge exactly replicates the fields external to the conductor. Example #1: a conducting plane near a point charge +q can be replaced by an image charge –q at the mirror image point of +q. Example #2: an ellipsoidal conductor near a point charge +q can be replaced by an image charge –q at the ellipsoid’s center. Example #3: a conducting ball of radius R whose center is a distance b from a point charge +q can be replaced by an image charge Q at a distance d from the ball’s center, provided that: d = R²/b, Q = –qR/b.

• A capacitor can be formed with two parallel plates, separated by distance d, each of area A, and with opposite charge densities +σ and –σ. The field E and voltage difference V between the plates are: E = σ/ε, V = E d. The total charge Q and the capacitance are: Q = σ A, V = Q d/Aε = Q / C, C = Aε/d, for two parallel plates. The capacitance of a sphere of radius r, relative to infinity, is: C = 4πε r, for a sphere.

• Electrostatic breakdown occurs when the field strength exceeds the breakdown voltage of the surrounding medium. Breakdown occurs when electrons are torn from atoms and avalanche toward the positive voltage, creating an arc, spark, or lightning. Breakdown occurs in air at 3.0 million volts/meter, in ideal conditions. Field emission microscopes employ high voltages in vacuum chambers to accelerate electrons or ions from sharp tips to detection screens, achieving resolutions down to the atomic scale.

## Chapter

Electrostatic Energy The principle of energy conservation...

能量守恒定律简化了许多力学问题，正如我们在本套《费曼物理学讲义》第一卷中所探讨的。在第三卷中，我们还将发现能量守恒在量子力学中是一项基本原理。

现在，我们将开始探讨能量守恒在电磁学中的影响。

**带电小球的能量**

回顾一下，两个电荷q₁和q₂相距r时产生的势能φ为： φ = (1/4πε₀) q₁q₂ / r 如果q₁和q₂极性相同（q₁q₂ > 0），φ是将两个电荷从无穷远处移到相距r所需做的功。如果q₁和q₂极性相反（q₁q₂ < 0），φ是同一过程中释放的能量。这个势φ就是两个电荷因彼此靠近而具有的静电势能。

根据线性叠加原理，一组N个电荷（q_j, j=1…N）的总势能是每对电荷势能之和。定义U为总静电能，可写为： U = (1/4πε₀) Σ_{j>k} q_j q_k / r_{jk} 其中，r_{jk}是电荷j和k之间的距离。注意，条件j>k确保每对电荷只被计算一次，同时也避免了对j=k时无穷大的自能项求和。

上述公式适用于离散电荷组。对于连续电荷分布ρ，我们将求和替换为积分： U = (1/8πε₀) ∫∫ ρ(r) ρ(σ) dr dσ / |r–σ| 注意分母中额外的因子2。这是因为积分中每对点A和B被计算了两次：一次当r=A，σ=B时；另一次当r=B，σ=A时。对于连续分布，我们不必担心r=σ时的贡献，因为ρ(r)仅在非零体积积分上才非零。

让我们通过一个例子进一步探讨：一个均匀带电小球的静电能U。U是将小球的所有物质从无限分散的初始状态聚集起来所需的能量。

想象通过一系列逐渐增大的同心球壳来组装这个小球。每个球壳有自己的半径r，无穷小厚度dr，以及总电荷dQ，由下式给出： dQ = 4π r² ρ dr 其中4πr²是球壳的表面积，ρ是单位体积的电荷密度。

图8-1（横截面示意图）展示了最新的球壳（黑色表示）正被添加到半径为r的小球（浅灰色表示）上，从而形成一个半径稍大的球（半径r+dr）。

（图注：图8-1 由同心球壳形成的小球）

将dQ从无穷远处移到小球上所需做的能量为： dU = (1/4πε₀) Q(r) dQ / r 其中，Q(r)是半径为r时小球的总电荷，为： Q(r) = ρ (4π/3) r³

将dQ、dU和Q(r)的表达式合并，得到： dU = (1/4πε₀) {ρ (4π/3) r³} {4πr² ρ dr} / r dU = ρ² (4π/3ε₀) r⁴ dr

我们将dU从r=0积分到最终半径R，完成计算。

U = ρ² (4π/15ε₀) R⁵

我们可以利用ρ与小球总电荷Q的关系来重写这个式子。

ρ = Q (3/4π) / R³ U = {Q² (9/16π²) / R⁶} (4π/15ε₀) R⁵ U = (3/5) Q² / (4πε₀ R)

这就是组装一个电荷为Q、半径为R的带电小球所做的功。这部分功转化为静电势能。

在《费曼物理学讲义》第二卷第8-2节中，费曼提到我们可以将这个方程解释为：小球内电荷的平均间距是5R/6。

**带电电容器的能量**

接下来我们计算将一个电容器充电至电压V所需的能量，其电容为C。

从一个由两个平行极板组成的未充电电容器开始。想象我们通过重复将无穷小电荷dq从一个极板移到另一个极板来建立电荷差。当电容器在电压V下带有电荷q时，移动dq所做的功为： dU = V dq 由于V = q / C，因此： dU = q dq / C

从q=0积分到最终电荷q=Q，得到： U = Q² / 2C 或者，因为Q = V C： U = C V² / 2

回顾一下，半径为R的球体相对于无穷远处的电容为： C = 4πε₀ R 利用这个电容，一个总电荷为Q的球体的静电能为： U = Q² / (8πε₀ R)

注意，一个球体的能量是具有相同半径和相同电荷的带电小球能量的5/6。

**带电电容器上的力**

正如我们在力学中使用F=–∇U来计算力一样，我们也可以利用能量的梯度来计算静电学中的力。

让我们计算上述电容器极板之间的力。设A为每个极板的面积，d为它们之间的间距，则电容为C=εA/d。由于极板带有异种电荷，它们之间的力是吸引力。想象将极板稍微分开一个距离Δd。所需做的功为： ΔW = F Δd 如果电容器的电荷Q不变，所做的功必须等于静电能的变化。这意味着： ΔW = Δ (Q² / 2C)

F Δd = (Q²/2) Δ(1/C)

正的Δd意味着1/C增大而C减小，因此该方程中的符号是正确的：增加间距d需要做正功。

吸引力两板之间的作用力为： FΔd = (Q²/2) Δ(d/εA)

FΔd = (Q²/2εA) Δd F = Q² / 2εA

让我们在单个电荷的层面上考察这个力。一块板上的总电荷为 Q=σA，其中 σ 是单位面积上的电荷密度。将一个 Q 因子替换为 σA，得到： F = Q σA / 2εA = Q σ / 2ε₀ 由于两板之间的电场为 E=σ/ε₀，方程变为： F = Q E / 2

为什么是 1/2？我们的标准方程是 F=qE；为什么这里不同？

在 Feynman Vol.2 Ch.8-4 中，Feynman 提供了这样的解释：并非所有的 Q 都暴露在完整的 E 中。我们之前说过导体中的过量电荷会移动到其表面。现在我们需要更精确地重述这一点。如果所有过量电荷都包含在零厚度的表面层内，那么体电荷密度将是无穷大的。因此，虽然电荷被限制在表面的一个薄层内，但这个层必须具有非零厚度，正如图 8-2 中浅灰色电容器板边缘的深灰色带所示。

Figure 8-2 Charge Layer at Surfaces of Capacitor Plates

导体内部的电场必须为零，而在板间表面的电场必须等于 σ/ε₀。对于表面层内均匀的电荷密度，图 8-2 显示了电场 E 随垂直坐标 z 的变化图。电场在每块板的内部为零，在表面层内迅速上升到 E，并在板间的间隙内保持该值。对于这种电荷密度分布，表面层中电荷所经历的平均电场为 E/2。因此，存在 1/2 这个因子。

我们上面假设在改变板间距 d 时，电容器的电荷 Q 是恒定的。如果我们改为将电容器连接到一个保持其电压恒定的电池，会发生什么？相关方程似乎是： U = C V² / 2 FΔd = ΔC V² / 2

起初，这里的符号似乎不对。增加 d 需要做正功，使得方程左侧为正。但增加 d 会减小 C，这使得右侧为负。答案是，最后一个方程忽略了电池所做的功。为了在 d 增加且 C 减小时保持恒定电压 V，电容器的电荷 Q 也必须减小。由于 Q=VC，电容器的电荷变化量必须为 ΔQ=V•ΔC，其中 ΔQ<0。

一定量的正电荷 ΔQ 必须从电容器的正极板流出，进入电池的正极。（或者更现实地说，一定数量的正电子必须从电容器的负极板流入电池的负极。）无论哪种方式，这都需要做功，大小等于： –V ΔQ 上面的负号是因为电池的电荷变化量等于减去电容器的电荷变化量 ΔQ。这个正能量变化必须包含在总能量变化 ΔU 中。正确的方程是： FΔd = ΔU = ΔC V²/2 – V ΔQ FΔd = ΔC V²/2 – V (V ΔC)

当 V 恒定时，FΔd = – ΔC V²/2

现在让我们回到在保持电荷恒定的情况下，增加电容器间距所做的功的方程。

FΔd = (Q²/2) Δ(1/C)

FΔd = (Q²/2) (–1/C²) ΔC 当 Q 恒定时，FΔd = – ΔC V²/2 当我们考虑到所有变化时，结果是一致的。

在 Feynman Vol.2 Ch.8-3 中，Feynman 指出电容器的配置可以比简单的两个平行板更复杂。图 8-3 展示了一个可变电容器，通过旋转两组交错排列的平行板中的一组，可以调节其电容。

Figure 8-3 Variable Capacitor

板呈半圆盘状。固定的一组显示为浅灰色。深灰色的那一组可以如图所示的角度 θ 旋转。两组重叠得越多，它们的总电容就越大。每组都连接到一根外部导线，显示为黑色。

由于其电容 C 与 θ 成正比，旋转会改变电容器的静电能，并需要一个力矩 τ。所做的功与 τ Δθ 成正比。

**离子晶体的能量** 接下来，我们利用静电能来揭示晶体中原子的性质。将单个原子结合在一起的力，以及将原子组结合成分子的力，几乎完全是电力。静电能在不同配置下的变化决定了原子如何相互作用。

考虑常见的食盐，这是一种简单的离子晶体，是由交替排列的正钠离子和负氯离子组成的三维点阵。图 8-4 描绘了食盐的二维横截面。

Figure 8-4 Alternating Sodium (+) & Chlorine (–) Ions

在《Feynman Simplified 1A》第 9 章中，我们讨论了原子间的力。我们发现，对于较大的间距，这些力通常是吸引力，而对于较小的间距则表现为强烈的斥力。两个原子的势能通常在由每种不同原子组合的性质决定的一个最佳间距处达到最小值。

作为一级近似，我们假设只要晶体保持完整，盐中的原子就保持在这个最佳间距，该间距是 Measured to be 2.81 angstroms.

Let’s see if our understanding of atoms and of electrostatic energy is sufficient to explain a basic property of salt: its total binding energy.

To completely separate all the atoms in salt, we must supply enough energy to vaporize the crystal (remove each pair of NaCl atoms from the crystal), and enough additional energy to dissociate each NaCl pair into individual Na and Cl ions. The total energy required to convert the crystal into individual, widely dispersed ions is measured to be 7.92 eV per NaCl pair. This means the binding energy of salt is 7.92 eV per NaCl pair. For brevity, we will call NaCl a “molecule”, as does Feynman, although ionic compound is its proper chemical description.

This binding energy can be expressed in other units. One electron-volt (eV) equals 1.602×10⁻¹⁹ joules, one kilocalorie (kcal) equals 4190 joules, and the number of molecules in a mole, Avogadro’s number, is 6.02×10²³. A useful ratio of these conversion factors is 1 eV/molecule = 23 kcal/mole.

In various units, W, the binding energy of salt is: W = 7.92 eV per molecule W = 7.64×10⁵ joules / mole W = 183 kcal / mole

Let’s see how close we can come to this measured value using our knowledge of electrostatics.

Each ion in the crystal has net charge ±1, and exists in the electrostatic potential created by all the other ions. The total binding energy of the ions is: U = Σ { q_j q_k / (4πε₀ r_{jk}) } for j<k

However, what we want is the binding energy per molecule, not per ion. By symmetry, Na ions have the same binding energy as Cl ions. If we exchange + and – in Figure 8-4, each charge exists in exactly the same array of equal and opposite charges at the same distances as it did before swapping polarities. Therefore, the binding energy per molecule is twice the binding energy per ion of either type. We can easily accommodate this by removing the requirement that j<k. The summation must continue to exclude j=k. The total binding energy of the molecules is: U = Σ { q_j q_k / (4πε₀ r_{jk}) } for j not = k

Feynman’s strategy to calculate U is to divide the summation into an infinite series of horizontal rows and evaluate each row separately. The sequence of rows is a bit tricky. It will be easier to follow with Figure 8-5, in which we see the crystal from the front and also from the end. The shadings now identify the row sequence rather than whether each atom is Na or Cl (that is still indicated with + and – signs). In the front view, we see the horizontal extent of each selected row, and in the end view we see only the ion at the end of each selected row.

Figure 8-5 Horizontal Rows in NaCl crystal

We will calculate the potential at the central Na ion that is shown in white. Let b be the atomic spacing, which is measured to be 2.81 angstroms.

We first calculate the contribution of the central row, shown in black. Secondly, we address the four adjacent rows that are shown in dark gray and are located above, below, in front (closer to you than the screen), and behind the first row. Thirdly come four diagonally-offset rows that are shown in light gray. The row sequence continues to infinity but we will stop long before then.

Let’s tackle the central black row. The two nearest ions have opposite charge and are at distance b. The next two ions have the same charge as our central ion and are at distance 2b. This alternating sequence continues indefinitely. Let U₁ be the binding energy of the white Na ion due to all ions in the same horizontal row. Its value is: U₁ = (q²/4πε₀) (–2/b +2/2b –2/3b +2/4b …)

U₁ = (–2q²/4πε₀ b) {1 –1/2 +1/3 –1/4 …}

The infinite sum in { }’s happens to equal 0.693, the natural logarithm of 2.

U₁ = (–2q²/4πε₀ b) {ln 2} U₁ = – 1.386 (q²/4πε₀ b)

Now consider the next row up (shown in dark gray). The ion directly above has the opposite charge of the central Na ion, and is at distance b. The two next nearest ions have the same charge as Na and are at distance b√2. The next two have opposite charges and are at distance b√5. The binding energy, U₂, due to this row is (I stopped after summing the nearest 2001 ions): U₂ = 12 eV U = (–1.747) 5.12 = –8.94 eV Feynman notes that our estimate is close, only about 13% more than the measured value. He says this validates our assumption that electrostatic forces are the dominant factor in atomic crystals, and adds: “This is the first time that we have obtained a specific property of a macroscopic substance from a knowledge of atomic physics. We will do much more later.” Now let’s address the 13% discrepancy. Feynman says this is due to atoms not being perfectly rigid balls. The atoms do repel one another when pushed together, but that repulsive force is not infinite. The electrostatic attraction of neighboring oppositely charged ions does squeeze the atomic spacing somewhat closer than their normal separation. This is much like compressing a box full of springs. When the springs are released, they release energy and reduce the effective binding energy.

If we knew the equation for the repulsive force, we could calculate the reduction in binding energy. Unfortunately, we haven’t yet learned enough about atoms to do that.

As an alternative, we can estimate the repulsive force from measurements of the compressibility of salt. The crystal’s resistance to compression is due to the repulsive force between atoms. From such measurements, Feynman says, it is determined that atomic repulsion reduces the electrostatic binding energy by about 11%. That reduces our estimate to 7.99 eV; still about 1% higher than the measured value.

Feynman says there is one more effect we have not yet considered (there almost always is in real world problems). All particles have thermal kinetic energy. From our studies of thermodynamics, we know that this energy amounts to kT/2 per degree of freedom, which equals 0.0129 eV, at room temperature. Our 1% remaining discrepancy amounts to 5.45 degrees of freedom, entirely reasonable for a diatomic molecule.

Nuclear Energy Levels In V2p8-6, Feynman explores what was then known about nuclear energy levels, and what could be learned by applying electrostatic energy analysis. These lectures preceded the discoveries that nucleons (protons and neutrons) are comprised of quarks and that the observed strong force between nucleons is a residual effect of a much stronger force between quarks. This section is of interest for the use of electrostatics and for historical reasons, but those seeking the best current knowledge of the strong interaction should look elsewhere.

Feynman describes attempts to understand the strong force through low-energy proton-proton scattering experiments. Physicists found that the strong force is almost as complicated as it can possibly be. By that we mean, the force varies with all possible parameters except one.

Firstly, the strong force varies strangely with distance. The force between two nucleons is zero if their separation is greater than a few proton radii. As the nucleons come quite close, the force becomes very strongly attractive — at least 100 times stronger than the electric force between opposite charges at the same separation. But if the nucleons become too close, the force become strongly repulsive.

Secondly, the force varies with the orientation of the nucleon spins. The force is quite different when the spins are parallel, as in part (a) of Figure 8-6, than when the spins are antiparallel, as in part (b). Figure 8-6 Nucleon-Nucleon Interaction Configurations Thirdly, the force is substantially different when the nucleon separation is parallel to the spin axis, as in parts (c) and (d), as compared with the separation being perpendicular to the spin axis, as in parts (a) and (b).

Fourthly, the force varies with the nucleons’ relative angular momentum, and is different if the orbital angular momentum is parallel to, versus antiparallel to, the spin angular momentum, as in parts (e) and (f) respectively.

Only one possible variation is not observed. The strong force is the same between two protons as it is between two neutrons as it is between a proton and a neutron. This indicates that the quark-quark forces are the same for all combinations of up and down quarks.

Feynman demonstrates this last point by examining two nuclei with equal numbers of nucleons, but different numbers of protons and neutrons. B11 has 5 protons and 6 neutrons, and is the dominant isotope of boron. C11 has 6 protons and 5 neutrons, and is a radioactive isotope of carbon with a half-life of 20 minutes. C11 decays to B11 when a proton changes into a neutron.

In terms of quarks, B11 has 16 up quarks and 17 down quarks, while C11 has 17 up quarks and 16 down quarks.

As Feynman says in V2p8-7: “In the nucleus the eleven [nucleons] interact with one another in a most complicated dance.” All nuclei have a ground state that has the minimum energy for that set of nucleons. Nuclei also have excited states in which one or more nucleons have additional angular momentum. If a nucleus is struck by an external particle of moderate energy, it may be driven into an excited state.

Typically, excited states rapidly shed their excess energy and drop back to the ground state.

In Figure 8-7, the excitation energies, the energies of excited states minus the energy of their ground state, are plotted vertically for B11 and C11. The energy of each state is listed in keV (1000 electron volts).

Figure 8-7 Excitation Energies of B11 & C11 in keV.

Feynman notes the similarity in the spacing of the energy levels of B11 & C11. The excitation energies of the first excited states of both nuclei are about 2060 keV, differing by only 6%. Both nuclei have big jumps to the second excited states that are nearly identical. Both have small jumps to the third excited states that differ by only 1.5%. Both have big jumps to the fourth excited states, followed by tiny jumps to the fifth excited states. He says this similarity shows that replacing a neutron with a proton, going from B11 to C11, changes the nuclear forces very little.

The ground state energies are different, however, with C11 being 1982 keV higher than B11. The absolute values of all excited states of C11 are also that much higher; what is plotted in Figure 8-7 are the energy differences between excited states and ground states. This makes sense since carbon’s 6 protons have greater mutual electrostatic repulsion than boron’s 5 protons. Greater repulsion means less binding energy (which is a negative quantity), and higher total energy.

The sum of particle masses is also different. A C11 atom has 1 more electron, 1 more proton, and 1 less neutron, than does B11. The C11–B11 particle mass difference is: +511 keV = mass electron +938,272 keV = mass proton –939,565 keV = mass neutron –782 keV = C11–B11 particle mass difference The total energy of any isolated atom, its rest mass, is the sum of the masses of its constituent particles minus their binding energy. For comparison, the orders of magnitude of various energies in B11 and C11 are: binding energy of electrons is tens of eV; binding energy of the nucleons is tens of MeV; and mass energies are ten GeV. We will therefore ignore the electrons’ binding energy.

The ground state energy, the atomic mass, is measured to be 1982 keV more for C11 than for B11. We therefore have: ΔU = (C11 mass) – (B11 mass) = 1982 keV =Δ(particle mass)+Δ(nuclear binding energy)

1982 = –782 + Δ(nuclear binding energy)

Δ(nuclear binding energy) = 2764 keV If strong force interactions are indeed identical for all pairs of nucleons, the only difference in nuclear binding energy is electrostatic, with more mutually repelling protons in carbon than in boron. Let’s try to estimate this energy difference using electrostatic theory.

In the simplest model, each nucleus is a ball of uniform charge density, whose total charge Q equals its atomic number Z (the number of protons) multiplied by q, the charge of one proton. At the beginning of this chapter we showed that a ball with total charge Q=Zq and radius R has total electrostatic potential energy: U = (3/5) (Zq)²/(4πε₀ R)

Recall that q²/4πε₀ = 14.39 eV-angstroms and that 1 angstrom = 10⁵ fermis, where 1 fermi (1 fm) = 10⁻¹⁵ m = 10⁻¹³ cm.

U = (3/5) (Z²/R) (1439 keV-fm)

U = 863 keV-fm Z² / R Scattering experiments on nuclei have determined that the radius of a nucleus of atomic mass number A (the number of nucleons) is well approximated by: R = r₀ A¹/³, with r₀ = 1.2 fm For A=11, (11)¹/³=2.22 and R=2.67 fm. The electrostatic potential energy for 11 nucleons with Z protons is: U = 863 keV-fm Z² / (2.67 fm)

U = 324 keV Z² Our estimated electrostatic potential energy difference between C11 and B11 in keV is: ΔU = 324 {Z²_C11 – Z²_B11} For Z=6 for carbon and Z=5 for boron, the term in { }’s equals 11 and our estimate of ΔU is 3562 keV, which exceeds 2764 keV by about 29%. Feynman says since we have discrete charges, and relatively few of those, we should replace Z² by Z(Z–1). That makes the term in { }’s equal to 10 and our estimated ΔU equal to 3240, still about 17% too high. Feynman says this really is: “not bad for our first nuclear computation!” Feynman says we can get even closer by assuming that 5 protons and 5 neutrons are some type of complete set that forms a core around which the 11th nucleon orbits. If the 11th nucleon is a neutron, there is no change in the electrostatic potential energy, but if the 11th nucleon is a proton, the increase in potential energy is: ΔU_est = (5q•1q)/(4πε₀ R)

ΔU_est = 5 (1439 keV-fm) / (2.67 fm)

ΔU_est = 2699 keV This is within 3% of the measured value of 2764 keV.

Feynman draws two conclusions from this analysis. Firstly, the laws of electrostatics seem to work down to dimensions as small as 1 fermi, and secondly, strong force interactions really are the same between all types of nucleon pairs.

None of this should be taken too seriously. A proper analysis requires quantum mechanics and a much deeper understanding of the strong force.

Electrostatic Field Energy We have previously derived equations for the electric potential and for e Electrostatic energy. For a continuous charge distribution ρ(r) these are: ø(r) = ∫ ρ(σ) dσ / (4πε |r–σ|) V 0 U = (1/2) ∫∫ ρ(r) ρ(σ) dr dσ / (4πε |r–σ|) V 0

As noted earlier, the factor of 1/2 before the double integral corrects for double counting. Each pair of charges A and B must contribute once to electrostatic energy, but the double integral includes each pair twice: once when r=A and σ=B and again when r=B and σ=A. Feynman notes that there is no convenient notation to avoid double counting by double integrals; the easiest approach is simply to divide by 2.

We can combine the prior equations to read: U = (1/2) ∫ ø(r) ρ(r) dr Here the integrand is the incremental charge ρ(r) dr multiplied by the potential at r. The total energy is the integral of that quantity over all space specified by volume V. The factor of 1/2 is still necessary since the double counting remains.

For two discrete charges, we can express their potential energy in three equivalent ways: U = q(r) ø(r) =q(r) q(σ) / (4πε |r–σ|) U = q(σ) ø(σ) =q(σ) q(r) / (4πε |r–σ|) U = (1/2) { q(r) ø(r) + q(σ) ø(σ) } This (1/2) factor corresponds exactly to the (1/2) factor in the double integral equation.

In V2p8-10, Feynman says: “An interesting question is: Where is the electrostatic energy located? One might also ask: Who cares? What is the meaning of such a question? If there is a pair of interacting charges, the combination has a certain energy. Do we need to say that the energy is located at one of the charges or the other, or at both, or in between? These questions may not make sense because we really know only that the total energy is conserved. The idea that the energy is located somewhere is not necessary. “Yet suppose that it did make sense to say, in general, that energy is located at a certain place, as it does for heat energy. We might then extend our principle of the conservation of energy with the idea that if the energy in a given volume changes, we should be able to account for the change by the flow of energy into or out of that volume. You realize that our early statement of the principle of the conservation of energy is still perfectly all right if some energy disappears at one place and appears somewhere else far away without anything passing (that is, without any special phenomena occurring) in the space between. We are, therefore, now discussing an extension of the idea of the conservation of energy. We might call it a principle of the local conservation of energy. Such a principle would say that the energy in any given volume changes only by the amount that flows into or out of the volume. It is indeed possible that energy is conserved locally in such a way. If it is, we would have a much more detailed law than the simple statement of the conservation of total energy. It does turn out that in nature energy is conserved locally. We can find formulas for where the energy is located and how it travels from place to place. “There is also a physical reason why it is imperative that we be able to say where energy is located. According to the theory of gravitation, all mass is a source of gravitational attraction. We also know, by E=mc2, that mass and energy are equivalent. All energy is, therefore, a source of gravitational force. If we could not locate the energy, we could not locate all the mass. We would not be able to say where the sources of the gravitational field are located. The theory of gravitation would be incomplete. “If we restrict ourselves to electrostatics there is really no way to tell where the energy is located. The complete Maxwell equations of electrodynamics give us much more information (although even then the answer is, strictly speaking, not unique.) We will therefore discuss this question in detail again in a later chapter. We will give you now only the result for the particular case of electrostatics. The energy is located in space, where the electric field is. This seems reasonable because we know that when charges are accelerated they radiate electric fields. We would like to say that when light or radio waves travel from one point to another, they carry their energy with them. But there are no charges in the waves. So we would like to locate the energy where the electromagnetic field is and not at the charges from which it came. We thus describe the energy, not in terms of the charges, but in terms of the fields they produce.”

We will now show that the energy of an electrostatic field E is given by: U = (ε/2) ∫ E•E dr 0 V This equation is interpreted as saying that, throughout all space, an electric field has an energy density given by: dU / dV = (ε/2) E•E = (ε/2) E2 0 0

Using a relationship for charge density found in Chapter 6, we can rewrite the integral equation. ρ = – ε Ď2ø U = (1/2) ∫ ø(r) ρ(r) dr U = –(ε/2) ∫ ø(r) Ď2ø dr 0 V

Let’s examine the x contribution to ø Ď2ø. {ø Ď2ø} = ø ∂2ø/∂x2 {ø Ď2ø} = {∂ (ø∂ø/∂x) /∂x} – {∂ø/∂x}2 The y and z terms are similar, and all three can be combined in a vector e equation as: φ ∇²φ = ∇ • (φ ∇φ) – ∇φ • ∇φ φ ∇²φ = ∇ • (φ ∇φ) – E • E Putting this back into the integral for U yields: U = –(ε₀/2) ∫ ∇ • (φ ∇φ) dr + (ε₀/2) ∫ E • E dr

## V  V

Per Gauss’ theorem, the divergence of (φ ∇φ) throughout volume V equals its normal component integrated across the surface S that encloses V.

U = –(ε₀/2) ∫ (φ ∇φ) • dS + (ε₀/2) ∫ E • E dr

## S  V

In V2p8-11 Feynman says the first integral goes to zero as volume V goes to infinity, enclosing all charges throughout all space. He notes that far from all charges, φ decreases as 1/r and ∇φ decreases as 1/r². This means the integrand is proportional to 1/r³, while the surface area increases only as r². For large enough r, Feynman says, the integral goes to zero as r goes to infinity. This is only true if the charge density ρ(r) approaches zero as r goes to infinity: space must extend beyond the farthest matter, or that matter must be electrically neutral. The second option is probably true, but the first probably isn’t.

Dropping the first integral gives the equation we sought to prove: U = (ε₀/2) ∫ E • E dr V Energy of a Point Charge The electric field from a point charge is: E = q / (4πε₀ r²)

Using the above equation for the energy density of the field, we get the following expression for the energy density from a point charge: dU / dV = (ε₀/2) E • E = (ε₀/2) E² dU / dV = (ε₀/2) q² / (16π²ε₀² r⁴)

dU / dV = q² / (32π²ε₀ r⁴)

The energy within a spherical shell of radius R, surface area 4πR², and thickness ΔR is: U = {4π R² ΔR} q² / (32π²ε₀ R⁴)

U = q² ΔR / (8πε₀ R²)

For any non-zero ΔR, U goes to infinity as R goes to zero. The same holds true even if ΔR is proportional to R.

This really makes no sense; a point charge cannot produce a field with infinite energy.

The problem is, as Feynman explains, that our equation for continuous charge distributions includes the self-energy of charge q in its own potential. This is contrary to our original stipulation that potential energy exists only between different charged objects.

Feynman notes we have a similar problem with the equation for the potential energy of a uniformly charged ball. From earlier in this chapter, that equation is: U = (3/5) Q² / (4πε₀ R)

This equation also gives infinite energy for a point charge.

The self-energy problem has bedeviled physicists since the early days of electromagnetism. It results directly from elementary charged particles being single point objects with infinite charge density. In V2p8-12, Feynman says: “We must conclude that the idea of locating the energy in the field is inconsistent with the assumption of the existence of point charges. One way out of the difficulty would be to say that elementary charges, such as an electron, are not points but are really small distributions of charge. Alternatively, we could say that there is something wrong in our theory of electricity at very small distances, or with the idea of the local conservation of energy. There are difficulties with either point of view. These difficulties have never been overcome; they exist to this day. Sometime later, when we have discussed some additional ideas, such as the momentum in an electromagnetic field, we will give a more complete account of these fundamental difficulties in our understanding of nature.”

## Chapter 8 Review: Key Ideas

• The electrostatic energy U of a uniformly charged ball of radius R and charge Q is: U = (3/5) Q² / (4πε₀ R)

For a sphere with total charge Q, radius R, and infinitesimal thickness: U = Q² / (8πε₀ R)

For a capacitor of capacitance C, voltage V, and charge Q (Q=VC): U = Q² / 2C = C V² / 2 The attractive force between two capacitor plates is: F = Q² / 2ε₀A For a crystal composed of alternating ions with charge +q and –q, and with atomic spacing b: U = – 1.747 (q²/4πε₀ b)

• The strong force is almost as complicated as it can possibly be, varying with all possible parameters except one. The strong force varies with: 1. distance, in a strange manner 2. spin orientation 3. spin-separation orientation 4. angular momentum-spin orientation But the strong force is the same for all combinations of nucleons.

• Electric field energy exists in the field itself. Its energy density is: dU / dV = (ε₀/2) E • E = (ε₀/2) E² The total energy within a volume V is: U = (ε₀/2) ∫ E • E dr V • Conversion constants: for q being the fundamental unit charge: q²/4πε₀ = 2.3068×10–28 newton-meter² q²/4πε₀ = 14.39 eV-angstroms

## Chapter 9 Electricity in the Atmosphere

Feynman begins this lecture saying in V2p9-1: “On an ordinary day over flat desert country, or over the sea, as one goes upward from the surface of the ground the electric potential increases by about 100 volts per meter. Thus there is a vertical electric field E of 100 volts/m in the air. The sign of the field corresponds to a negative charge on the earth’s surface. This means that outdoors the potential at the height of your nose is 200 volts higher than the potential at your feet! You might ask: ‘Why don’t we just stick a pair of electrodes out in the air and get free energy from it?’...” 空气相距一米，我们能否利用这100伏的电压来点亮电灯？' 或者你可能会想：'如果在我的鼻子和脚之间真的存在200伏的电势差，为什么我走到街上时不会触电呢？'

费曼解释说，你不会因为这个电压差而触电，因为人体是良好的导体。（不幸的是，这也是触电可能造成危险的原因。）作为导体，我们改变了周围的电场：电场线必须垂直于身体表面，等势线必须平行于身体表面。一个与地面接触的人会在其全身建立一个零伏的等势体，如图9-1所示。

图9-1 导体附近的等势线

请注意，空气通常是一种极差的导体，这就是这些电场能够维持的原因。电势梯度（即电场）因多种因素而变化显著。随着海拔升高，电场减弱，电势在30至50公里的高度达到约+300,000伏的最大值。再往上，大气电离程度足以成为良好的导体，从而中和大部分电场。

费曼描述了一种测量高度h处电势的有趣方法。将一个静电计连接到一个装有水的漏电金属桶上，桶用绝缘绳悬挂在高度h处。由于桶和水都是导体，费曼说它们最终会达到与周围空气相同的电势，水滴会带走多余的电荷。静电计将测量桶的电压。

费曼还描述了一种测量地球表面电场的方法。高斯定律将表面上的电场E与表面电荷密度σ联系起来：E=σ/ε。我们可以在地球表面附近放置一块导电板A，并通过一个测量电流的 galvanometer 将其接地。如图9-2所示。我们在板A上方放置第二块导电板B，也将其接地。如果垂直间距很小，我们可以假设两块板都与地球具有相同的电势，定义为零伏。这意味着板之间的电场为零。

图9-2 测量地球表面电荷

定义两个大小相等的封闭面1和2，如图9-2所示。在此设置中，电场仅在地球和板B上方的空气中非零。因此，通过面1和面2的电场通量仅通过其上部水平面。

为了使板B上方的电场与地球其他地方的电场相同，通过面1的通量必须等于通过面2的通量，这意味着板B上的表面电荷密度等于地球的表面电荷密度σ。在板B所示的位置，板A和板B下方的地球没有表面电荷。

如果我们现在移走板B，电流将从地球流向板A，以在A上建立相同的表面电荷密度σ，从而在其上方产生正常的电场。galvanometer将测量此电流。根据总电流和板面积，我们可以确定σ。

大气中的电流

科学家们还测量到一股微小的电流垂直向下流经大气层。其大小约为每平方米几皮安（10⁻¹²安培/平方米）。这表明空气不是完美的绝缘体。空气的微小导电性是由一小部分电离分子引起的，密度可能为每立方厘米几百到几千个。

空气分子可以被电离这一事实是在研究放射性材料时发现的。物理学家通过使用非常精确测量电荷的静电计证明辐射会使空气分子电离。

图9-3：带有两条金带的静电计

一个简单的静电计由一个真空室组成，室内有一个电极悬挂着两条相邻的金带，如图9-3所示。当电极充电时（此例中是通过接触带电棒），金带获得等量电荷并相互排斥，其偏转程度与电极电荷成正比。

图9-4展示了一种测量空气导电性的装置，间接测量电离空气分子的浓度。一个各侧均暴露于空气的电容器最初通过施加电压V来充电。与电源断开后，电容器会缓慢放电，因为空气中的电离分子中和了其电荷。

图9-4 测量空气导电性

静电计（显示为带箭头的圆圈）持续测量电容器电荷，并监测其放电速率。

由于放射性是已知的电离源，最初认为地球大气是由地壳内重元素衰变产生的辐射电离的。因此，大气电离在更高海拔处减弱似乎是合理的，因为分子距离辐射源更远。

are partially shielded by the air beneath.

However, in 1911 and 1912, Austrian physicist Victor Hess made a series of balloon ascents with an electrometer. Hess made the surprising discovery that the concentration of ionized air molecules increases with altitude, rather than decreasing as expected. Measurements made during a solar eclipse also showed that the Sun was not the primary ionization source.

With a balloon and electrometer, Victor Hess discovered cosmic rays.

In Earth’s atmosphere, there are a variety of charged objects, including: “small ions” comprised of free electrons, ionized atoms, and ionized molecules; and “large ions” comprised of microscopic dust particles attached to small ions. The concentrations of ions vary substantially, influenced by weather, altitude, and proximity to the major source of dust: land.

Atmospheric conductivity increases with altitude due to a greater abundance of cosmic rays and also due to a longer mean free path resulting from reduced air density. Above 50 km the atmosphere is sufficiently conducting to be considered an equipotential surface.

Although the atmospheric current density is small, only several picoamps per square meter, Feynman says the total current reaching Earth’s surface amounts to 1800 amps. With a 300,000 voltage drop, this current delivers about 600 megawatts of power.

In V2p9-3, Feynman says this large current flowing downward from the sky would neutralize Earth’s negative charge in about 30 minutes, if some other phenomenon did not continually maintain an equal upward current.

That phenomenon is lightning.

Over an 11 year span, from 1995 to 2005, NASA satellites recorded lightning strikes worldwide. You can view the results here: http://www.guidetothecosmos.com/downloads/Lightning.pdf The worldwide average rate of lightning strikes is 45.1 per second, 88% of which occur over land.

Despite the fact that 71% of Earth’s 510 million km2 (197 million miles2) surface is covered by water, only 12% of lightning strikes occur over the oceans. Land can become hotter than the oceans and can therefore pump more heat into the atmosphere.

The 88% of strikes that hit land are distributed by continent as: Africa 30%, Asia 14%, South America 19%, North America 12%, Europe 3%, and Australia/Philippines 10%. These data show a correlation between lightning and surface temperature.

Figure 9-5 shows the worldwide frequency of lightning strikes as a function of local time. It peaks sharply from 15:00 to 16:00 (3:00 to 4:00 pm). The five curves are for each three-month interval separately plus the yearly average. The highest rate is 115 strikes per second in June-July-August.

Figure 9-5 NASA: Lightning Strikes vs. Time The sharp peak in local time indicates lightning is driven by atmospheric heat that follows a daily pattern. The same effect enhances the rate during the summer months in the Northern Hemisphere.

Since most of Earth’s land area is north of the equator, world averages are substantially skewed northerly.

A thorough discussion of the electrical processes in thunderstorms, based on modern data not available to Feynman, is contained here: http://www.guidetothecosmos.com/downloads/Thunderstorms.pdf I provide here a brief and qualitative summary.

Thunderstorms The physics of thunderstorms is driven by: (1) warm air being less dense than cold air; (2) heat being released when water condenses or freezes; and (3) separation of positive and negative charges due to air convection and ion content.

Thunderstorms run through three stages: formation, maturation, and dissipation. A typical storm runs through the three stages in 30 minutes, but some last much longer.

In the first stage, the cumulus stage, air that is heated over hot terrain expands, reducing its density and making it buoyant. The resulting strong updraft can carry warm air to altitudes exceeding 40,000 feet (12 km). As warm air expands and rises, its temperature declines and its water vapor condenses, forming clouds. Condensation releases energy, the latent energy of vaporization that sustains the higher temperature and lower density of the cloud relative to the surrounding air.

During this stage, the cloud typically lifts about half a million metric tons of water vapor. When that amount of water vapor condenses, it releases 1015 joules of energy, 16 times the energy released by the Hiroshima atomic bomb.

Figure 9-6 NOAA: Stages of a Thunderstorm NOAA’s National Weather Service created the images in Figure 9-6 illustrating the cumulus (left), mature (center), and dissipating (right) stages of a thunderstorm.

In the second stage, the maturation stage, the top of the cloud reaches a layer of warmer air in the upper atmosphere. This stops the cloud’s further ascent. Water droplets grow larger and freeze, forming ice. During this transitional stage, air turbulence increases, often with hazardous consequences.

In the third stage, the dissipation stage, the cloud’s air cools and becomes sufficiently dense to l its buoyancy. A strong downdraft results that may extinguish the storm, if it is not too large.

Charge Separation in Thunderclouds

When water droplets move vertically at high speed they preferentially attach to “large ions” of one polarity. Figure 9-7 shows two water droplets (larger light gray circles), with the left droplet falling in a downdraft and the right one rising in an updraft.

(Figure 9-7 Falling & Rising Water Drops)

Recall that Earth’s atmosphere has an overall electric field of typically 100 V/m, with its surface being negative and the sky being positive. This field induces a dipole moment in water droplets, making their tops negative and bottoms positive.

In a strong draft, the droplets’ motion makes it far more likely that atmospheric ions (dark gray circles) will attach to the droplet’s leading face rather than its trailing face. Negative ions are likely to attach to a falling drop, while positive ions are likely to attach to a rising drop, as the figure depicts.

This brings negative charges downward and lifts positive charges upward. This effect makes cloud bottoms much more negatively charged than Earth’s surface, and cloud tops much more positively charged than the surrounding air at the same altitude. Feynman says these clouds’ voltage differences can reach 100 million V, several hundred times greater than the Earth-sky potential difference.

This much greater potential gradient drives away the excess negative charge normally on Earth’s surface, giving the surface beneath the cloud a net positive charge.

Lightning

Lightning can strike within a single cloud, between two clouds, or between a cloud and the ground. The latter is somewhat understood, the others less so.

Lightning begins with downward leaders, channels of highly ionized air that begin at cloud bottoms and proceed erratically toward the surface. Each leader starts moving rapidly along a path of least resistance, for a distance of typically 50 m. The leader then stops and accumulates a pool of charge. New leaders later start from these pools and proceed further. Once downward leaders get close to the ground, upward leaders may form at the tops of tall buildings or trees. Eventually, typically after tenths of a second, a continuous ionized path is established between the cloud base and the ground. The actual lightning bolt traverses that path, persisting for up to 200 microseconds.

Feynman says each lightning strike brings 20 to 30 coulombs of negative charge down to Earth, balancing the positive charge brought by atmospheric current during fair weather. The numbers roughly match: 25 coulombs/strike multiplied by 45 strikes/second equals 1125 amps, about 63% of the 1800 amps of atmospheric current that Feynman mentioned earlier.

Feynman ends this lecture quoting an advisor to King Xerxes of Persia, who seems to have been unheeded: “See how God with his lightning always smites the bigger animals and will not suffer them to wax insolent, while these of a lesser bulk chafe him not. How likewise his bolts fall ever on the highest houses and tallest trees … So, plainly, doth he love to bring down everything that exalts itself.”

Feynman counsels modesty, a rare trait amongst physicists.

## Chapter 9 Review: Key Ideas

Earth’s atmospheric electric field near the surface is typically 100 V/m pointing downward. The field weakens with increasing altitude, and the potential reaches a maximum of about +300,000 volts at an altitude of 30 to 50 km. Above that, the atmosphere is sufficiently ionized to be a good enough conductor to neutralize substantial electric fields.

Charged objects in our atmosphere include: “small ions” comprised of free electrons, ionized atoms, and ionized molecules; and “large ions” comprised of microscopic dust particles attached to small ions. The concentrations of ions vary substantially, influenced by weather, altitude, and proximity to land, the major source of dust.

Although the atmospheric current density is small, only several picoamps per square meter, Feynman says the positive current reaching Earth’s surface amounts to 1800 amps.

A thunderstorm typically lifts half a million metric tons of water vapor, releasing 10^15 joules when that vapor condenses.

The worldwide average rate of lightning strikes is 45.1 per second, 88% of which occur over land. Feynman says each lightning strike brings 20 to 30 coulombs of negative charge down to Earth, balancing the positive charge from fair weather atmospheric current.

## Chapter 10 Dielectric Materials

In previous chapters, we discussed the interaction of electric fields with conductors. We discovered that, in the presence of an external field, the conductor’s free charges cancel the field within the body of the conductor by appropriately positioning themselves along its surface.

We now turn our attention to the interaction of electric fields with insulators, non-conducting materials that contain no free-moving charges. What effect do insulators have on electric fields? In 2p10-1, Feynman says: “One might at first believe that there should be no effect whatsoever. However, using a simple electroscope and a parallel-plate capacitor, Faraday discovered that this was not so. His experiments showed that the capacitance of such a capacitor is increased when an insulator is put between the plates.”

If the insulator fills the entire gap between the capacitor’s parallel plates, the capacitance is multiplied by a factor κ, called the dielectric constant, that is an intrinsic property of the insulating material. The dielectric constant of vacuum is 1.

Without a dielectric, a capacitor with two parallel plates of area A, plate separation d, and charge density –σ on one plate and +σ on the other, has capacitance C, plate charge Q, and voltage V given by: C = εA / d Q = σA Q = VC

What Faraday observed was that placing an insulator between an isolated capacitor’s plates increases C. Since an isolated capacitor’s charge Q does not change, adding the insulator must reduce V and therefore must reduce the electric field between the plates.

Figure 10-1 shows a dielectric insulator (light gray) between two charged parallel plates (dark gray). Figure 10-1 Dielectric Between Capacitor Plates

Consider the electric field flux through the box bordered by dashed lines in Figure 10-1. Since the insulator reduces the electric field between the plates, it must reduce the flux through the surface of the box and must therefore reduce the net charge within the box. This means the insulator must have a net positive charge on its upper surface and a net negative charge on its lower surface.

The insulator increases the capacitance, but does not make it infinite. The electric field decreases, but remains greater than zero. This means the charge densities on the insulator surfaces are not as great as the charge densities on the conducting capacitor plates.

By comparison, imagine placing an isolated, uncharged conductor of thickness b between two capacitor plates that are separated by distance d, as shown in Figure 10-2. Figure 10-2 Conductor Between Capacitor Plates

The field within the central conductor must be zero, hence the charge densities on each pair of facing surfaces must have equal magnitude and opposite polarity. Since the upper surface of the central conductor has the same charge density as the upper surface of the lower capacitor plate, the electric field in the upper gap has the same value as it did without the central conductor. Similarly for the lower gap.

The voltage, however, does change with the addition of the central conductor. While the field is unchanged in the two gaps, it becomes zero within the added conductor. For the capacitor shown in Figure 10-2, the voltage and capacitance are: V = (σ/ε) {d – b} V = [dσ/ε] {1 – b/d} C = Q/V = σA / (ε/dσ) / {1 – b/d} C = [Aε/d] / {1 – b/d}

The terms in [ ]’s are values without the central conductor. The {1–b/d} term accounts for the central conductor: the voltage is multiplied by {1–b/d} and the capacitance is divided by {1–b/d}. Clearly, for b=0, these equations yield the normal values for a parallel-plate capacitor with a vacuum-filled gap. For 0<b<d, the voltage is reduced and the capacitance is increased.

In V2p10-2 Feynman discusses two possible, but inadequate, models of dielectrics. By reviewing the history of inadequate models, we can learn how science progresses. We rarely know if an idea is correct until we evaluate all its consequences and compare them with reality. We must typically explore many dead-ends before finding the way forward.

One model postulated that dielectrics are alternating layers of: perfect conductors; and ideal insulators that have κ=1. Substances with different dielectric constants would have different relative thicknesses of the two types of layers. This model provides the right behavior only in the direction perpendicular to the layers. However, most dielectrics are isotropic, contrary to this model.

An improved model postulates that dielectrics contain many tiny conducting spheres embedded in a perfectly insulating matrix. The electric field between capacitor plates would be reduced by the fraction of the dielectric’s volume that is occupied by conducting spheres in which the field is zero. This model becomes more realistic as the spheres become smaller and more numerous. It was considered that the spheres might be individual atoms, each perfectly conducting but perfectly insulated from its neighbors.

Polarization Vector P Ultimately, physicists realized that the key phenomenon in dielectrics is charge displacement. If a dielectric’s negative charges move toward the positive capacitor plate and its positive charges move toward the negative capacitor plate, that displacement creates an electric field that reduces the net field in the capacitor. This reduces the voltage across the capacitor and increases its capacitance.

We need not invent a new physics to explain dielectrics. What we already know about atoms is suf Atoms contain both positive and negative charges. In isolation, the centroids of these opposite charges are coincident: the average location of the positive charge exactly equals the average location of the negative charge. If the centroids were not coincident, their displacement would create a force that would pull the centroids together.

However, if an atom, even a neutral atom, is exposed to an external field E, its positive charge is pulled in the E direction while its negative charge is pulled in the opposite direction. We describe this by saying the external field induces a dipole moment in the atom.

The forces in atoms are complex and their correct description requires quantum mechanics. But for small changes, we can approximate any function, however complex, with a Taylor series. For a weak external field E, the Taylor series for atomic charge displacement δ is: δ = a₀ + a₁E + a₂E² + … We know that a₀ = 0 because there is no charge displacement absent an external field. For small E, we can neglect terms with E² and all higher powers of E. Thus the displacement δ is proportional to E, for small E. Let +q be the sum of an atom’s positive charges, –q be the sum of its negative charges, and δ be the separation between the centroids of each polarity. Such an atom has a dipole moment of qδ. If there are N atoms per unit volume, we define a polarization vector P as: P = N qδ (E/E)

Here (E/E) represents a unit vector in the E direction.

In the next chapter we will discuss how δ is related to the properties of the atoms in a dielectric. In this chapter we will assume δ is some constant that is characteristic of each type of insulating material.

Polarization Charges

We now consider how induced dipole moments, described by the polarization vector P, determine the behavior of dielectrics.

Let’s take the simplest case first: an electrically neutral, homogeneous dielectric with uniform P. In the interior of the dielectric, the net charge everywhere remains zero. In each infinitesimal volume dV, the same number of charges of each polarity move into dV as move out of dV. This isn’t true at the surface.

Figure 10-3 depicts a dielectric (light gray) sandwiched between a capacitor’s parallel plates (dark gray). By convention, a charge displacement δ corresponds to positive charges moving a distance δ in the +P direction and negative charges remained fixed. The reality is that electrons move far more than nuclei, but the two motions are mathematically equivalent.

At the top surface of the dielectric in Figure 10-3, positive charges create a layer of thickness δ. The magnitude of the charge density per unit area in this layer is: σ_pol = N q δ = |P| Similarly, positive charges vacate a layer of thickness δ at the bottom surface of the dielectric. This layer has charge density –σ_pol. Between these upper and lower layers, between the horizontal dashed lines in Figure 10-3, the dielectric continues to have zero net charge density as equal numbers of charges of both polarities move into and out of each small volume.

Define σ_cap to be the magnitude of the capacitor’s charge density per unit area. In Figure 10-3, the flux through the box bordered by dashed lines determines the field within the dielectric, according to: E = (σ_cap – σ_pol)/ε₀ The minus arises because the positive capacitor plate attracts the negative side of the dielectric’s dipoles, and vice versa. Note that σ_pol exists only because it is induced by σ_cap. If the capacitor is discharged, its charge flows out through the capacitor’s electrical connections, and σ_pol drops to zero as the dipole displacements become zero.

We can rewrite the prior equation by substituting σ_pol with |P|.

E = (σ_cap – |P|)/ε₀ Now recall that P is linearly proportional to E, which we express as: P = χ ε₀ E The proportionality constant χ is called the electric susceptibility of the dielectric material. The equation for E is then: E = (σ_cap – χ ε₀ E)/ε₀ E (1+χ) = σ_cap / ε₀ E = (σ_cap /ε₀) / (1+χ)

The voltage across the capacitor is E multiplied by the capacitor plate spacing d.

V = Ed = (dσ_cap /ε₀) / (1+χ)

The capacitance is: C = Q / V = (σ_cap A) {(1+χ) / (dσ_cap /ε₀)} C = Q / V = (Aε/d) (1+χ)

C = Q / V = (Aε/d) κ κ = 1+χ Our model of induced dipole moment explains how a dielectric increases capacitance. Exactly how the dipole is induced is addressed in the next chapter.

Non-Uniform Polarization

In V2p10-5, Feynman considers a more complex situation in which the polarization vector P varies within a dielectric.

Let’s first address the amount of charge moving through a surface S due to a polarization vector P(r). In Figure 10-4, the coordinate system is defined with P pointing up. Here θ is the angle between P and n, the normal to a surface S that is represented in cross-section by the bold diagonal line.

In Figure 10-4, positive charges everywhere are moving upward a distance δ, which is the magnitude of the dipole displacement δ. The charge passing through a surface element dS is proportional to the component of P perpendicular to the surface. The flux of polarization charge through the surface S is given by the surface integral of P · n dS.

distance δ. Every charge that is directly below S by a distance of no more than δ passes through S. Hence the flux through S is the (volume of the gray parallelepiped) multiplied by (the atomic density N) multiplied by (the atomic charge q). For A being the area of surface S, the flux equals: Flux = (A δ cosθ) N q For P being the magnitude of vector P: P = N δ q cosθ = P•n / P Flux = A P•n / P = A P•n Flux per unit area = P•n This result is what we obtained in our study of vector analysis.

Gauss’ law equates the decrease of charge –ΔQ in a volume V with the integral of the charge flux per unit area through the surface S that encloses V. This means: –ΔQ = ∫ P•n dS By Gauss’ theorem, this surface integral equals the volume integral of the divergence of P.

–ΔQ = ∫ P•n dS = ∫ ∇•P dV S V If we start with a neutral dielectric, ΔQ will be the charge density ρ (r) integrated over volume V.

pol The equation is: ΔQ = ∫ ρ (r) dV = – ∫ ∇•P dV V pol V Since this holds for any volume V, it follows that: ρ (r) = – ∇•P(r)

pol We see that a non-uniform polarization vector can create a non-zero charge density even within the body of a dielectric.

Note that this equation also provides a dielectric’s surface charge density. At a surface in the xy-plane, the changes due to a small change in z are: – ∇•P Δz = – (∂P/∂z) Δz = –ΔP = P ρ Δz = σ = P pol pol Here the (charge density per unit volume ρ) multiplied by (the layer thickness Δz) equals (the surface charge density σ per unit area).

Electrostatics with Dielectrics Some authors find it convenient to restate the electrostatic equations for the presence of dielectric materials. Whether or not you agree, it is useful to understand their notation.

Recall the equation: ∇•E = ρ/ε Here ρ is the volume density of all charges. We can separate the dielectric charge density ρ from ρ , the “free” charge density (all other charges).

pol free ∇•E = (ρ + ρ ) /ε free pol 0 ∇•E = (ρ – ∇•P) /ε free 0 ∇•(E + P/ε) = ρ /ε 0 free 0 Using the linear approximation P = χεE, we obtain: ∇•(E + χE) = ρ /ε free 0 ∇•(κE) = ρ /ε free 0 We leave κ inside the divergence in case it varies within the dielectric. If κ is uniform, it can be factored out and placed in the denominator of the right hand side.

Feynman says the other equation of electrostatics is unchanged: ∇×E = 0 For historical reasons, Maxwell’s equations were written in terms of a new vector field D as: D = εE + P When P is proportional to E, this can be written: D = εE (1+χ)

D = κεE D = εE Here ε is a new constant describing dielectric properties called the material’s permittivity, with ε being the permittivity of vacuum.

With these expressions for D, the electrostatic equations with dielectric are: ∇•(D) = ρ free ∇×E = 0 In V2p10-7, Feynman explains why he prefers to avoid using D: “Today we look upon these matters from another point of view, namely, that we have simpler equations in a vacuum, and if we exhibit in every case all the charges, whatever their origin, the equations are always correct. If we separate some of the charges away for convenience, or because we do not want to discuss what is going on in detail, then we can, if we wish, write our equations in any other form that may be convenient.

“One more point should be emphasized. An equation like D=εE is an attempt to describe a property of matter. But matter is extremely complicated, and such an equation is in fact not correct. For instance, if E gets too large, then D is no longer proportional to E. For some substances, the proportionality breaks down even with relatively small fields. Also, the “constant” of proportionality may depend on how fast E changes with time. Therefore this kind of equation is a kind of approximation, like Hooke’s law. It cannot be a deep and fundamental equation. On the other hand, our fundamental equations for E represent our deepest and most complete understanding of electrostatics.” Fields & Forces with Dielectrics We described above how dielectrics increase the capacitance of parallel-plate capacitors. The same effect is possible for capacitors of any shape under certain conditions.

The open space (vacuum) electrostatic equations are: ∇•E = ρ /ε 0 free 0 ∇×E = 0 The zero subscript has been added to stress that E is the vacuum field. Now consider a capacitor of any shape that is immersed in a non-conductive liquid whose dielectric constant is uniform, and whose polarization is linearly proportional to the electric field. The relevant equations are: ∇•(κE) = ρ /ε free 0 ∇×E = 0 Since κ is assumed constant, we can rewrite these equations as: ∇•(κE) = ρ /ε free 0 ∇×(κE) = 0 We now have exactly the same equations for E and for κE. This means any situation for which E is a solution also has E = E/κ as a solution. Adding the dielectric simply reduces the field everywhere by the factor κ.

Recall that voltage V=Ed and C=Q/V. If d and Q remain constant, dividing the electric field by κ reduces the voltage across the capacitor by κ, and multiplies its capacitance by κ.

dependence on κ.

The force between the opposite-polarity conductors of a capacitor can be calculated from the gradient of potential energy: F=–∇U. We found earlier that if the plates have equal but opposite charge densities, the potential energy is given by either of two equivalent equations:

U = Q²/2C = V²C/2

Assuming a constant charge Q, the force is:

F = – (Q²/2) ∇(1/C)

Since the dielectric multiplies C by κ, it also divides the forces between capacitor conductors by κ.

In Volume II, Chapter 10, Feynman says:

“One point should be emphasized. What we have said is true only if the dielectric is a liquid. Any motion of conductors that are embedded in a solid dielectric changes the mechanical stress conditions of the dielectric and alters its electrical properties, as well as causing some mechanical energy change in the dielectric. Moving the conductors in a liquid does not change the liquid. The liquid moves to a new place but its electrical characteristics are not changed.

“Many older books on electricity start with the ‘fundamental’ law that the force between two charges is: F=q₁q₂/(4πεκr²) a point of view which is thoroughly unsatisfactory. For one thing, it is not true in general; it is true only for a world filled with a liquid. Secondly, it depends on the fact that κ is a constant, which is only approximately true for most real materials. It is much better to start with Coulomb’s law for charges in a vacuum, which is always right (for stationary charges).

“What does happen in a solid? This is a very difficult problem which has not been solved, because it is, in a sense, indeterminate. …

“A surprisingly complicated problem in the theory of dielectrics is the following: Why does a charged object pick up little pieces of dielectric? If you comb your hair on a dry day, the comb readily picks up small scraps of paper. If you thought casually about it, you probably assumed the comb had one charge on it and the paper had the opposite charge on it. But the paper is initially electrically neutral. It hasn’t any net charge, but it is attracted anyway. It is true that sometimes the paper will come up to the comb and then fly away, repelled immediately after it touches the comb. The reason is, of course, that when the paper touches the comb, it picks up some negative charges and then the like charges repel. But that doesn’t answer the original question. Why did the paper come toward the comb in the first place?”

We can see why a charged body attracts dielectrics. Figure 10-5 shows a dielectric ball in the field of a positively charged body that is off the screen to the lower left.

Figure 10-5: Force F on Dielectric Ball in E Field

The field E polarizes the dielectric, moving its negative charges closer to and its positive charges farther from the positive body. In the case shown in Figure 10-5, the field is non-uniform, being stronger on the negative side of the dielectric ball than on the positive side. The difference in field strength across the ball coupled with the dielectric’s charge separation results in a net force pulling the ball toward the charged body.

If the body were negatively charged, the dielectric charges would reverse, and the net force would remain attractive.

The force is proportional to the field gradient ∇E. The force is also proportional to the dielectric’s dipole moment. When the dipole moment is proportional to the field E, the force F varies as:

F ~ E (∇E) = ∇(E²) / 2

The force is proportional to the gradient of E².

Now consider a dielectric that is partially inserted into the gap of a parallel-plate capacitor. What are the fields and forces?

Figure 10-6: Force F on Partially-Inserted Dielectric

Let L be the plate length, d be the plate separation, V be the voltage across the plates, κ be the dielectric constant, and x be the distance that the dielectric extends into the gap. Also let W be the plate width in the direction perpendicular to the screen.

Since the conducting plates are equipotential surfaces, the voltage between the plates must be the same everywhere — where the dielectric fills the gap (on the left) and where it is absent (on the right). This means the plate charge densities are different on the two sides, as given by:

Open gap: σ = εV / d

Filled gap: σ = κεV / d

The charge in each region is:

Open gap: Q = εVW(L–x) / d

Filled gap: Q = κεVW(x) / d

The total charge and capacitance are:

Q = (εVW/d) (L–x + κx)

C = (εW/d) (L–x + κx)

Assuming a constant capacitor charge, the force pulling the dielectric farther into the gap is:

F = – ∂U/∂x = – ∂ (Q²/2C) / ∂x

F = + (Q²/2) (1/C²) ∂C/∂x

F = (V²/2) (εW/d) (κ–1)

Calculating the force from the energy gradient is far simpler than summing the forces between all charges.

## Chapter 10 Review: Key Ideas

• An external field E induces a dipole moment in the atoms of an insulator. The field separates the centroids of each atom’s positive and negative charges by a displacement δ that is proportional to E, for small E. Let +q be the sum of an atom’s positive charges and –q be the sum of its negative charges; then the dipole moment is qδ.

let +q be the sum of its positive charges, –q be the sum of its negative charges, N be the number of atoms per unit volume. Such an atom has a dipole moment of qδ. The polarization vector P and induced surface charge density σ are: P = N qδ (E/|E|)

σ = N q δ = |P| The electric susceptibility χ and dielectric constant κ are defined by: P = χ ε E κ = 1+χ The field E, voltage V, and capacitance C of a capacitor whose gap spacing d is filled by a dielectric are: E = (σ/ε) / κ V = Ed = (dσ /ε) / κ C = Q / V = (Aε/d) κ • Some authors define a vector field D as: D = εE + P = εE ∇•(κE) = ρ /ε free 0 Here ρ is the charge density outside dielectrics, ε is a dielectric’s permittivity, with ε being the free 0 permittivity of vacuum. Feynman says these equations are not always valid and recommends using the vacuum equations that are always correct.

• In a non-uniform field, a dielectric is pulled toward the region of greatest field strength.

## Chapter

Inside Dielectrics In the prior chapter, we discussed how electric fields induce dipole moments in dielectrics, non- conductive materials. The dielectric constant κ, the average dipole moment per unit volume P, and the external field E are related by: (κ – 1) ε E = P This chapter explores how these dipole moments arise at the atomic level.

We will consider dielectrics of each of the three major phases of matter. In order of increasing complexity these are: gases, liquids, and solids.

For gases, we will consider two classes separately: polar molecules, and non-polar molecules.

Non-Polar Gases A non-polar molecule has no intrinsic dipole moment: absent an external field, its dipole moment is zero. All monatomic gases are non-polar, as are all diatomic gases composed of two identical atoms, such as H₂ and O₂ molecules.

In V2p11-1, Feynman begins with the simplest case, monatomic helium gas.

As described in the prior chapter, an external field pulls an atom’s electrons in one direction and pulls its nucleus in the opposite direction, displacing the centroids of positive and negative charge.

Feynman calls this electronic polarization. For weak fields, the displacement is proportional to the field strength.

Feynman notes that the polarization effect here is similar to the polarization of atoms that leads to the index of refraction that we explored in Feynman Simplified 1C Chapter 34. The only difference is that there we dealt with oscillating fields and here we are dealing with a static field.

There, we treated electrons in atoms as forced harmonic oscillators, and assumed nuclei are fixed. In an oscillating field, the electrons’ equation of motion is: m d²x/dt² + m ω² x = q E Here, m and q are the electron’s mass and charge, x is the electron’s displacement, E is the field, and ω is the electron’s natural frequency. For a field oscillating at frequency ω, the solution to the above equation is: x = qE / {m(ω² – ω²)} The harmonic system is in resonance when ω=ω. (Recall that all real systems have damping terms, not included above, that prevent x from becoming infinite.)

In the present case, our interest is in static fields for which ω=0. The solution then simplifies to: x = qE / (mω²)

For this displacement x, the dipole moment µ equals: µ = q²E / (mω²)

Feynman says physicists sometimes write this: µ = α ε E where α is the atomic polarizability given by: α = q² / (ε m ω²) = 4πe² / (m ω²)

Recall that e² is defined to be q²/4πε, for q being the elementary charge.

This result, based on the atoms-are-harmonic-oscillators model, concludes that the dipole moment is proportional to the field, as we assumed in the prior chapter.

With N being the number of atoms per unit volume, the polarization vector P is: P = Nµ = N α ε E Combining this with the first equation in this chapter, we have: (κ – 1) ε E = P = N α ε E (κ – 1) = N α = 4π N e² / (m ω²)

Our model predicts that κ–1, the change in dielectric constant relative to vacuum, is proportional to gas density and inversely proportional to the square of the atoms’ natural frequency.

Our model is rather simplistic; a true description of atomic behavior requires quantum mechanics.

Among other issues, atoms have many natural frequencies, not just one.

Nonetheless, let’s see how far this simple model takes us.

Using the Uncertainty Principle of quantum mechanics, we will discover in Feynman Simplified 3A

## Chapter 3 that an electron in a hydrogen atom has a binding energy E given by:

E = me⁴ / 2ħ² In V2p11-3, Feynman equates E, the energy required to remove hydrogen’s electron, with ħω, the energy corresponding to its natural frequency. We then have: ω = me⁴ / 2ħ³ Using this expression in the equation for α yields: α = 4πe² / (m ω²)

α = (4πe²/m) (4ħ⁶/m²e⁸)

α = 16π (ħ²/me²)³ α = 16π a³ Here a is the Bohr radius, which equals 0.529 angstroms.

Feynman says a monatomic gas at atmospheric pressure at 0ºC has 2.69×10¹⁹ atoms per cm³, which makes hydrogen’s dielectric constant equal to: κ = 1 + (2.69×10¹⁹) 16π (0.529×10–⁸)³ H Model: κ = 1.00020 For diatomic hydrogen, the measured value is: H Expt. : κ = 1.00026 The measured value corresponds to a 30% greater (κ–1) than our model. Feynman says the monatomic versus diatomic dielectric constants should be very similar; he attributes the 30% deviation to our overly simplistic atomic model. Nonetheless, our model is in the right ballpark. Feynman also quotes values for helium: He Model: κ = 1.000050 He Expt. : κ = 1.000068

Polar Gases

Some molecules have intrinsic dipole moments. The water molecule is the most important example. The oxygen nucleus exerts a stronger force on electrons than do the hydrogen nuclei, giving the oxygen a net negative charge and the hydrogens a net positive charge. The centroids of positive and negative charge are shown qualitatively in Figure 11-1. The charge separation is enlarged for clarity.

Figure 11-1 H2O Molecule

The dipole moment of water is µ = (10e)×0.039 angstroms. Here 10e is the total charge of water’s ten protons, which is also the negative of the total charge of its 10 electrons. The quoted displacement is about 6.7% of the radius of an oxygen atom. The angle between the two hydrogen-oxygen bonds is 104.45º.

Absent an external field, water molecules in the gas phase have their dipole moments pointing in random directions. But with an external field E, molecules with µ parallel to E have lower potential energy than molecules with other dipole orientations.

We can calculate the net polarization of a large population of water molecules using statistical mechanics. The first step is finding the electrostatic potential energy U of an arbitrary dipole orientation. Figure 11-2 shows charges +q and –q that are separated by displacement vector d. Also shown are the dipole moment vector µ and electric field vector E. The angle between µ and E is θ.

Figure 11-2 Dipole in Electric Field

The dipole’s potential energy U is the electric potential ø(r) multiplied by the charge at r, summed for both charges, which is: U = (+q) ø(at +q) + (–q) ø(at –q) U = q {ø(at +q) – ø(at –q)} U = q d•∇ø

The gradient of potential ø equals –E, and qd equals µ. This means: U = –µ•E = –µE cosθ Here µ and E are the magnitudes of vectors µ and E.

According to Boltzmann’s law (see Feynman Simplified 1B Chapter 16), the number of molecules with energy U is proportional to: exp{–U/kT}

Let n(θ) be the number of molecules per unit solid angle with dipole moment µ at angle θ relative to E. Boltzmann’s law says: n(θ) = n(0) exp{µE cosθ / kT}

Normally, the exponent is small and we can approximate this equation as: n(θ) = n(0) {1 + µE cosθ / kT}

This equation confirms that more molecules will have their dipoles aligned parallel (cosθ=1) than antiparallel (cosθ=–1) to E. Integrating n(θ) over all solid angles relates n(0) to N, the total number of molecules per unit volume: N = ∫∫ n(0) {1 + µE cosθ / kT} dβ dcosθ

Here β is the azimuthal angle that ranges from 0 to 2π, and cosθ ranges from +1 to –1.

N = n(0) 2π {cosθ + µE cos²θ / 2kT} | (+1 to –1) N = n(0) 2π {(+1+1) + µE (+1–1) / 2kT} N = n(0) 4π

We can now calculate the total polarization of this gas by integrating the polarization component along E multiplied by the number of molecules with that polarization. (By symmetry, the polarization must sum to zero along directions perpendicular to E.)

P = ∫∫ n(θ) µE cosθ dβ dcosθ P = 2π ∫ n(0) {1 + cosθ µE/kT} µ cosθ dcosθ P = (Nµ/2) {(cos²θ)/2 + cos³θ µE/3kT} | (+1 to –1) P = (Nµ/2) {(+1–1)/2 + (+1+1) µE/3kT} P = N µ² E / 3kT

The polarization is proportional to E, consistent with the analyses of the prior chapter. P is proportional to µ²: one factor of µ due to the alignment bias, and another factor that scales what is being averaged. P is also inversely proportional to T, because large thermal energy minimizes the significance of the dipole potential energy. This latter relationship is called Curie’s law, after Pierre Curie, who shared the 1903 Nobel Prize with his wife Marie Curie and Henry Becquerel.

Fields Within Dielectrics

Liquids and solids are typically several hundred times denser than gases. In dense matter, individual atoms are affected, not just by external fields, but also by fields produced by their many close neighbors. To calculate the polarization induced in one atom, we must know the total field acting upon it.

We will discuss liquids first, and move up to solids in a later section. In a liquid that fills the gap of a parallel-plate capacitor, the total electric field that an atom is exposed to is the sum of the field due to the charged plates, and the fields from other polarized atoms. Feynman says that this field varies very rapidly on a subatomic scale, being particularly strong near each nucleus and much weaker between atoms.

On a medium scale, a scale much larger than one atom yet much smaller than the gap between plates, the total field can be considered constant. Even with that approximation, the situation is complex. We demonstrate that by considering the fields inside two tiny boxes cut into the dielectric. (We imagine for the moment that the liquid is frozen.)

Figure 11-3 shows two small voids (white) in a dielectric (gray) between two capacitor plates (black). The left box extends vertically and the right box extends horizontally. The total electric field E points up.

Figure 11-3 Two Voids in Dielectric Filling Capacitor

We define a closed curve Γ that runs upward through the dielectric, loops around, and then runs downward through the center of the left box. We also define a closed surface S that encloses portions of the dielectric and the upper face of the right box.

Since the curl of E is always zero in electrostatics, Stokes’ theorem applied to the left box says: ∫ E•ds = ∇×E = 0 0 = E L – E L box E = E box Here L is the vertical length of Γ, E is the field strength within the body of the dielectric, and E is the magnitude of the field within the box that is also upward. We see that the field in the box equals the field in the body of the dielectric.

However, for the right box, polarization charges exist on its upper and lower surfaces. (These are not shown in the figure.) This means surface S encloses a charge –σ A, where A is the area of the dielectric that S encloses. The minus sign arises in this case because the polarization charge on the upper box face is negative. Gauss’ theorem says: pol E A – E A = – σ A / ε box pol 0 E = E + σ / ε = E + P / ε box pol 0 0

While all this is interesting, the field in neither the vertical box nor the horizontal box accurately represents the field acting on an individual atom. Atoms are spherical, or nearly so, even when polarized. Let’s consider therefore the field inside a spherical void in a dielectric.

By the principle of linear superposition, the field inside a spherical hole equals the field in the body of the dielectric minus the field inside a spherical ball that would precisely plug that hole. This is illustrated in Figure 11-4, where the arrows indicate polarization vectors.

Figure 11-4 Superposition: Bulk = Hole + Plug

The equation is: E = E + E hole plug

In Chapter 6 we solved the problem of two equal but oppositely charged balls that are slightly displaced, forming an electric dipole. (See Figure 6-3 in particular.) That result is directly applicable here.

E = – P / 3ε plug 0 The minus sign arises again because the polarization field opposes the applied external field. In V2p11-6, Feynman says this result shows that the field in a sphere is 1/3 of the way between a slot parallel to the field and a slot perpendicular to the field.

We now have the equation for the field inside a tiny spherical hole that we imagine is filled by an individual atom.

E = E – E = E + P / 3ε hole plug 0

Dielectric Constants of Liquids

Recall the equation for polarization found earlier in this chapter: P = Nµ = N α ε E 0 0 The field experienced by an atom in a liquid dielectric should be E , the quantity just derived, rather than E, the external field. Making this substitution, we obtain: hole P = N α ε (E + P / 3ε)

0 0 P – P Nα/3 = Nα εE P = εE Nα/(1–Nα/3)

κ–1 = Nα/(1–Nα/3)

This is called the Clausius-Mossotti equation.

Note that in the limit that Nα becomes very small (as in a gas), this equation reduces to the equation we used above for gases: κ–1=Nα.

To test the Clausius-Mossotti equation, Feynman compares dielectric constants for the gas phase and liquid phase of the same substance.

For example, the measured dielectric constant for carbon disulfide gas is 1.0029, which means Nα for CS is 0.0029. For liquid CS, N is 381 times greater. Assuming that α is unchanged, this means Nα=1.105 and κ–1=1.75 for liquid CS. This is about 7% more than the measured value of κ–1=1.64.

2 2 2 (I compare κ–1 rather than κ; no gold stars for correctly predicting 1.)

Our assumptions regarding the electric field on individual atoms, and also α being the same for gas and liquid phases, seem largely validated by this result.

Feynman does a similar comparison for oxygen, carbon tetrachloride, and argon. The model predictions for κ–1 are: 0.4% too high for O; 17% too high for CCl ; and 4% too low for Ar. The agreement is quite respectable for O and Ar, but it seems something occurs in CCl that we haven’t accounted for.

2 4 4

This analysis applies only to non-polar molecules. Feynman says if we do the same calculation for liquid HO, we get Nα=13.2 and κ–1=–3.9 versus a measured value of +79. Clearly our model does not properly account for intrinsic dipole moments. Feynman refers us to Introduction to Solid State Physics by Kittel for a more complete analysis.

Dielectric Constants of Solids

Solid dielectrics involve many of these same considerations, but with an additional feature: they may have permanent intrinsic polarizations. In V2p11-8, Feynman says wax is an example, due to its long molecules with dipole moments. If liquid wax is allowed to solidify in the presence of an applied external electric field, its molecular dipoles tend to align in opposition to the field. When wax hardens, this preferential a Alignment provides a permanent polarization that persists even if the external field is removed. Such solids are called electrets.

Isolated electrets have polarization charges on their surface. Feynman says electrets are the electrical analog of magnets. But when exposed to air or other media, free charges eventually neutralize electrets' surfaces and cancel their external fields.

Permanent polarizations also occur in some crystals. In these crystals, the unit cell, the pattern of atoms that repeats throughout the crystal, has a dipole moment. Since unit cells align with the same orientation, their dipole moments accumulate with macroscopic consequences. Figure 11-5 shows the unit cell of a prime example: PZT, a ceramic perovskite composed of lead, oxygen, and either zirconium or titanium. The metal ion, shown as the small central black dot, has charge +4 and may move up or down within the cell.

The external fields of such crystals are eventually neutralized by free atmospheric charges. But changes in the crystal structure can change the polarization fields more rapidly than free charges can neutralize them. If the structural change is due to heating, the effect is called pyroelectricity.

If the structural change is due to mechanical stress, the effect is called piezoelectricity. Indeed piezoelectricity is a bidirectional effect: if an external force bends a piezoelectric strip, it produces a voltage; and if a voltage is applied to a piezoelectric strip, it bends.

PZT is the most important piezoelectric material. It is used in many applications, including microphones and audio transmitters. A company in which I was VP of R&D developed a computerized Braille word-processor. Electronically-activated PZT levers raised and lowered plastic pins forming Braille characters, enabling blind students to compose and edit term papers. Physics can make a human difference.

Ferroelectricity

Ferroelectric materials have an interesting and more complex relationship between polarization and external fields.

Figure 11-6 shows the polarization P induced by an external field E for a normal dielectric (dashed line) and for a ferroelectric (hysteresis curve).

For a simple dielectric, P is linearly proportional to the applied field E: P=bE, for some constant b. In a ferroelectric, P is characterized by a hysteresis loop, depicted in Figure 11-6 as two offset "S" curves that are tangent to the upper and lower straight lines.

For large positive E, P increases linearly with E but with an offset of +P₀: P=bE+P₀, corresponding to the upper straight line in Figure 11-6. If E is very large, and positive at one time and later becomes zero, P does not become zero, as in a normal dielectric, but rather retains the value +P₀.

If E then drops below zero, progressively becoming more negative, P rapidly decreases, passes through zero at E=–E₀, and later decreases linearly as E continues decreasing. This linear behavior follows P=bE–P₀ and corresponds to the lower straight line. If E later becomes zero, P becomes –P₀.

Because ferroelectrics retain one of two states even without an applied voltage, they are used for digital non-volatile memory.

When a ferroelectrics' polarization rapidly reverses polarity, the abrupt field change is a readily detectable electrical signal.

A newly formed ferroelectric may initially have P=0. If a progressively increasing field is applied, P increases rapidly (the short curve from origin to upper straight line). Typically, a ferroelectric can be reset to P=0 by applying an alternating field of gradually decreasing strength.

A particularly interesting ferroelectric is barium titanate, BaTiO₃. It has five possible crystalline structures, each of which dominates within its own temperature range. In four of its five structures, barium titanate is ferroelectric.

Feynman says that above 118ºC barium titanate has an enormous dielectric constant, and below that temperature it abruptly acquires an intrinsic polarization. He then begins an extended analysis of the dielectric properties of barium titanate that he acknowledges is incomplete and imprecise, due to atomic interaction complexities that are not well understood. We will focus on the insightful physics rather than the detailed calculations.

Feynman says the total field at each individual atom in a solid is more complex than in a liquid. For liquids, molecules are uniformly distributed. But in crystals, atoms of various charges occupy fixed positions. Nonetheless, for a cubic unit cell, Feynman says the 1/3 factor derived for liquids is approximately correct.

Recall the Clausius-Mossotti equation that we derived for liquids: κ–1 = Nα/(1–Nα/3)

The right hand side is infinite when Nα=3, and is negative for Nα>3; neither result is realistic. What happens, Feynman says, is that the assumption that P is linearly proportional to E breaks down for large E. Yet his sub Subsequent analysis continues to assume linearity. He says as α increases, P increases, which increases the local field, which further increases P. He says: “What happens is that the lattice gets ‘locked in’ with a high, self-generated, internal polarization.”

Crystals typically expand somewhat as temperature increases, which results in the atomic density N decreasing. Hence, we can adjust Nα by adjusting temperature. Define T_c to be the critical temperature at which Nα=3, and define the thermal expansion coefficient β such that: Nα = 3 – β(T–T_c), for T>T_c For normal materials, β is small, only parts per million per ºC. The dielectric constant is then: κ–1 = {3 – β(T–T_c)} / (1–{3 – β(T–T_c)}/3)

κ–1 = {9 – 3β(T–T_c)} / β(T–T_c)

For small β, this reduces to: κ–1 = 9 / β(T–T_c), for T>T_c This is called the Curie-Weiss law. Feynman says that near T=T_c, κ can become as large as 100,000.

Feynman next proceeds to estimate induced dipole moments in barium titanate by calculating the field at one atom due to each vertical column of atoms in the crystal. This is similar to what we did for salt crystals in Chapter 8 (see Figure 8-5.) He focuses on the columns with the most atoms, those with alternating oxygen and titanium atoms, and ignores all other columns. He also assumes all atoms in each column are identical, even though oxygen atoms have charge –2 and titanium atoms have charge +4. He says: “It is not a serious simplification because all the important effects will still appear. This is one of the tricks of theoretical physics. One does a different problem because it is easier to figure out the first time—then when one understands how the thing works, it is time to put in all the complications.”

Feynman’s result is: α (BaTiO₃) = a³/0.383 = 21.8×10⁻²⁴ cm³ Here a is the vertical atomic spacing, which equals 2 angstroms. He says this should be compared to 16.3×10⁻²⁴ cm³, the average of the measured α values for oxygen (30.2×10⁻²⁴ cm³) and titanium (2.4×10⁻²⁴ cm³). So far, the calculation is 34% too high.

“But wait a moment!” Feynman says, we should add the ionic polarization of titanium atoms displaced within the unit cells, which he says must be 11.9×10⁻²⁴ cm³ to make his analysis work.

To conclude, Feynman says: “Why the titanium ion in barium titanate should have that much ionic polarizability is not known. Furthermore, why, at a lower temperature, it polarizes along the cube diagonal and the face diagonal equally well is not clear. If we figure out the actual size of the [atoms in the crystal] and ask whether the titanium is a little bit loose in the box formed by its neighboring oxygen atoms—which is what you would hope, so that it could be easily shifted—you find quite the contrary. It fits very tightly. The barium atoms are slightly loose, but if you let them be the ones that move, it doesn’t work out. So you see that the subject is really not one-hundred percent clear; there are still mysteries we would like to understand.”

Sometimes, the best laid plans of the best minds gang aft a-gley, to paraphrase the great Scottish poet Robbie Burns.

## Chapter 11 Review: Key Ideas

• The polarization vector P, with N being the number of atoms per unit volume, and α being the atomic polarizability, is: P = Nµ = N α ε₀ E • Modeling atomic electrons as forced harmonic oscillators, we estimate that atoms without intrinsic dipole moments have: α = q² / (ε₀ m ω²) = 4πe² / (m ω²)

(κ – 1) ε₀ E = P = N α ε₀ E (κ – 1) = N α = 4π Ne² / (m ω²)

Actual measured values are about 30% higher, indicating the limitations of this model.

• For gas molecules with intrinsic dipole moment µ, Curie’s law says the polarization is: P = N µ² E / 3kT The Clausius-Mossotti equation for liquid dielectrics without intrinsic dipole moments is: κ–1 = Nα/(1–Nα/3)

## Chapter

Electrostatic Analogs In this lecture, Feynman demonstrates how our knowledge of electrostatics applies directly to other phenomena far and wide.

Same Equations, Same Solutions In V2p12-1, Feynman says: “The total amount of information which has been acquired about the physical world since the beginning of scientific progress is enormous, and it seems almost impossible that any one person could know a reasonable fraction of it. But it is actually quite possible for a physicist to retain a broad knowledge of the physical world … The reasons for this are threefold: First, there are great principles which apply to all the different kinds of phenomena—such as the principles of the conservation of energy and of angular momentum. A thorough understanding of such principles gives an understanding of a great deal all at once. Second, there is the fact that many complicated phenomena, such as the behavior of solids under compression, really basically depend on electrical and quantum-mechanical forces, so that if one understands the fundamental laws of electricity and quantum mechanics, there is at least some possibility of understanding many of the phenomena that occur in complex situations.

Finally, there is a most remarkable coincidence: The equations for many different physical situations have exactly the same appearance. Of course, the symbols may be different…but the mathematical form of the equations is the same. This means that having studied one subject, we immediately have a great deal of direct and precise knowledge about the solutions of the equations of another.”

“We will find that the equations of electrostatics appear in several other places in physics. By a direct translation of the solutions (of course the same mathematical equations must have the same solutions) it is possible to solve problems in other fields with the same ease—or with the same difficulty—as in electrostatics. … It works both ways, of course—if the other subject has some particular characteristics that are known, then we can apply that knowledge to the corresponding electrostatic problem.”

To expand on Feynman’s point, I would add that the seemingly infinite diversity of observable phenomena result from only four particles interacting through only four forces. Four is a number that anyone can manage.

The equations of electrostatics (allowing for dielectrics) are: ∇•(κE) = ρ_free / ε₀ ∇×(κE) = 0

or the mathematically equivalent: E = –∇ø ∇•(κ∇ø) = – ρ_free / ε₀

Feynman says many phenomena are characterized by an equation of the form: ∇ • [A(r) ∇B(r)] = C(r)

Here, A, B, and C are scalar functions.

Heat Flow Let’s expand on the examination of heat flow that we began in Chapter 3. Consider now an inhomogeneous block of matter with a non-uniform temperature distribution T(r). Temperature differences will drive heat flow. We represent heat flow with a vector field h: at each location r, h points in the direction of maximum heat flow, and the magnitude of h equals the amount of heat energy flowing per unit time through a unit area normal to h. Gauss’ theorem says the total divergence of h, throughout any volume V, equals the amount of heat energy leaving V per unit time, according to: ∫ ∇•h dV = ∫ h•dS = rate of heat flow out of V V S

Here, S is the surface enclosing volume V.

Feynman poses a problem in which heat is generated or absorbed in various places according to a function s(r), with s>0 corresponding to heat generation and s<0 to absorption. To keep this problem analogous to electrostatics, the block of matter must have reached equilibrium; h, s, and T cannot be functions of time. This means: ∇•h(r) = s(r)

We also need an equation for h. We assume h is proportional to the gradient of temperature, according to: h(r) = – K(r) ∇T(r)

Since the material is said to be inhomogeneous, we allow the thermal conductivity K to vary with location. Feynman notes that the equation before last is fundamental — it expresses the conservation of energy. Whereas the last equation describes the behavior of this particular material approximately — no fundamental law ensures that heat flow is exactly linear with the gradient of temperature.

Combining these equations we obtain: ∇ • (K ∇T) = – s

This equation is mathematically identical to the electrostatic equation: ∇ • [κ ∇ø] = – ρ_free / ε₀

The solution of a heat problem must match the solution of an equivalent electrostatic problem. From a single point source of heat (or charge), T (or ø) varies as 1/r, and h (or E) varies as 1/r².

Now consider the specific example of two concentric pipes of radii r₁ and r₂, with r₁ < r₂. In the heat problem, let the inner pipe be a temperature T₁ and the outer pipe at T₂, as shown on the left side of Figure 12-1. Also let the gap between the pipes be filled with insulating material with uniform thermal conductivity K.

Figure 12-1 Concentric Pipes at Different Potentials

In the electrostatic problem, let the inner pipe be at potential ø₁ and the outer pipe at ø₂, as shown on the figure’s right side. Here the gap between the pipes is filled with a dielectric with constant κ. The figure shows representative h and E vectors.

We wish to find the heat loss G per unit time, per unit length of pipe. This is equivalent to finding the flux of E per unit length. We have already derived the electrostatic field outside a charged wire. Let’s see how the equivalent heat-flow problem is solved.

By symmetry h is entirely radial everywhere, and has magnitude h(r).

Imagine enclosing the inner pipe with a cylindrical surface S of length L and radius r, with r₁ < r < r₂. (Length is the dimension perpendicular to the screen.) At equilibrium, the same amount of heat energy G must flow through each such cylindrical surface regardless of its radius. Gauss’ law says: G = ∫ ∇•h dV = ∫ h dS = 2π r L h V S

We also have: h = – K ∇T = – K ∂T/∂r

Combining these yields: G / (2πL r) = – K ∂T/∂r

Integrate this from r=r₁ to r=r₂.

(G/2πLK) ∫ dr/r = – ∫ ∂T/∂r dr (G/2πLK) ln(r₂ /r₁ ) = – [T(r₂ ) – T(r₁ )]

G/L = (2πK) (T₁ – T₂) / ln(r₂ /r₁ )

Since G is equivalent to the flux of E, which equals the enclosed charge divided by ε, we have for the charge per unit length.

Length in the electrostatic problem: Q/L = (2πε) (φ₁ – φ₂) / ln(r₂ / r₁)

Next, we move on to another heat flow problem: what is Earth’s surface temperature distribution due to a deep magma chamber? The heat conductivity of land is much greater than that of air. For simplicity, let’s assume the conductivity of air is zero. The left side of Figure 12-2 depicts a heat source at a distance d below Earth’s surface (bold horizontal line). Arrows represent the field lines of heat flow vector field h.

Figure 12-2 Magma Chamber Under Earth’s Surface

Note that h must be horizontal everywhere at the surface, because we assumed no heat flows through air.

In V2p12-4, Feynman highlights a key limitation of the same-equations-same-solutions technique: the math may be equivalent, but sometimes physical equivalents do not exist. In this heat problem, we assumed air has zero thermal conductivity. However, no real material has zero dielectric constant; that isn’t forbidden mathematically, but none exists in nature. Sometimes we can’t use exactly the same solution, but we can use the same methods.

What electrostatic analog has a field with zero normal component everywhere on a surface? The only answer is the field between two equal charges of the same polarity that are equidistant above and below the surface, with the same dielectric constant everywhere. Below the surface, this electrostatic situation produces exactly the same E field as the h field in the thermal situation. Hence the solutions must be the same.

At a distance r from a point source, the analogs are: φ(r) = q/4πεκr T(r) = G/4πKr

For a point on the surface at a distance ρ from the vertical axis, the distance to the source is: r = √(ρ² + d²)

For two equal point sources on the vertical axis that are equidistant from the surface, the analogs are: φ(ρ) = q/2πεκr T(ρ) = G/2πKr

Drumhead

We next switch to mechanics: consider a drumhead, a thin elastic membrane, stretched taut, and rigidly affixed at its perimeter to an immovable frame. Figure 12-3 shows a drumhead attached to a circular frame (black oval). The drumhead is pulled up at one point and pushed down at another. How can we describe the shape of such a membrane?

Figure 12-3 Drumhead Deflected Up & Down

A drumhead’s restoring force is surface tension, the attraction of the membrane’s atoms for one another. The drumhead cannot move horizontally; its only degree of freedom is vertical motion within its constraining frame. This means each membrane atom is subject to equal forces, pulling it left and pulling it right, and also equal forces in the third dimension, pulling it into and out of the screen. These are the forces of surface tension. For simplicity, we will assume that, at each point within the membrane, these forces are equal in all directions.

Now consider a small rectangular patch of membrane of extent Δx by Δy. We number its edges 1 through 4, as shown in a top-down view in the upper half of Figure 12-4. We define τ to be the force of surface tension per unit length. All the atoms on the left side of edge 1 are pulling it to the left. Hence the total force is proportional to the number of atoms along edge 1, and thus proportional to its length.

Figure 12-4 Tension On Small Patch

Let’s first calculate forces in the x-direction, those acting on edge 1 and edge 2.

As a side view in the lower half of Figure 12-4 shows, surface tension vectors τ₁ and τ₂ are tangent to the plane of the membrane, the plane within which all atomic forces occur. Due to the membrane’s curvature, τ₁ and τ₂ need not be parallel; define θ₁ and θ₂ to be the angles between the horizontal axis and τ₁ and τ₂. Recall that we have assumed the tension has the same magnitude everywhere; it varies only in direction due to the membrane’s curvature.

Let u(x,y) be the vertical displacement of the drumhead at location (x,y). The net upward force along edges 1 and 2 is: ΔF₁₂ = τ Δy sinθ₂ – τ Δy sinθ₁

Here the minus sign arises because τ₁ is pulling downward. In general, for any small patch, τ₁ and τ₂ will point in nearly opposite directions. We will limit our analysis to small vertical displacements, so that θ ≈ sinθ ≈ tanθ. This simplifies our equation.

ΔF₁₂ = τ Δy tanθ₂ – τ Δy tanθ₁ ΔF₁₂ = τ Δy (∂u/∂x)₂ – τ Δy (∂u/∂x)₁

For small Δx and for any function g(x): g(x+Δx) – g(x) = Δx ∂g/∂x In this case, g = (∂u/∂x). That substitution yields: ΔF₁₂ = Δy Δx τ ∂[(∂u/∂x)]/∂x ΔF₁₂ = Δy Δx τ (∂²u/∂x²)

Similarly, the forces on edges 3 and 4 yield a net upward force that is obtained by simply exchanging x and y. The sum of the forces along all four edges is then: ΔF = Δy Δx τ { (∂²u/∂x²) + (∂²u/∂y²) } ΔF = Δy Δx τ ∇²u

Recall the Laplacian operator ∇² = ∂²/∂x² + ∂²/∂y², in 2-D.

At equilibrium, force ΔF must be balanced by an external force. Define f to be the external force per unit area in the upward direction. At equilibrium, the sum of all forces must be zero.

f Δy Δx + ΔF = 0 f = – τ ∇²u ∇²u = – f / τ

This matches the electrostatic Poisson equation: ∇²φ = – ρ_free / ε.

static equation: ∇²φ = –ρ/ε

Solutions to the electrostatic equations are also solutions to the drumhead equation, and vice versa. In Volume II, page 12-6, Feynman says: “The stretched rubber sheet has often been used as a way of solving complicated electrical problems experimentally. The analogy is used backwards! Various rods and bars are pushed against the sheet to heights that correspond to the potentials of a set of electrodes. Measurements of the height then give the electrical potential for the electrical situation. The analogy has been carried even further. If little balls are placed on the membrane, their motion corresponds approximately to the motion of electrons in the corresponding electric field. One can actually watch the “electrons” move on their trajectories. This method was used to design the complicated geometry of many photomultiplier tubes.” In modern times, digital computers perform such tasks faster, easier, and more precisely.

Figure 12-5 shows a cylindrically symmetric drumhead whose shape can be readily calculated using an electrostatic analog. Here, we see in cross-section a central rod pushing up on an elastic membrane that is fixed to the lip of an outer cylinder. Let u(x,y) be the drum head deflection at (x,y), and let r = √(x²+y²).

Deflection u is analogous to electric potential φ, and the rod and cylinder are analogous to two conductors with different voltages. The solution we derived for a charged wire applies to this problem as well. Deflection u (or potential φ) is proportional to –ln(r), and the slope of the drumhead (or E) is proportional to 1/r.

Neutron Diffusion

Now something completely different: neutron diffusion. In Feynman Simplified 1B Chapter 17, we explored the diffusion of ions in a gas, and the diffusion of one gas into another. Here we examine the diffusion of neutrons in graphite, a material comprised almost entirely of carbon atoms. Graphite is like diamond, only millions of times cheaper.

In graphite, slow neutrons are not absorbed by nuclei, but are scattered almost like billiard balls. Typically, their mean free path is several centimeters. Following the logic of that chapter, we define N(r) to be the neutron density per unit volume at r, and define flow vector J so that J•n is the number of neutrons per unit time per unit area flowing through a surface whose unit normal is n. In that chapter, we derived the equation: J = – (λv/3) ∇N Here, λ is the mean free path, and v is the mean speed (magnitude of velocity).

Neutrons can be released by various nuclear processes, including the decay of heavy elements such as uranium. In general, neutrons can also be absorbed by nuclei, although by choosing graphite we eliminate this consideration. Additionally, neutrons decay with a mean lifetime of 881.5 seconds. To accommodate all these factors, define S(r) to be the net number of neutrons created at r per unit time per unit volume.

Within any infinitesimal volume dV: ∂N/∂t = S – ∇·J This equation says: (the rate of change of the number of neutrons in dV) equals (the net number created in dV) minus (the net number flowing out of dV). Here, we have used Gauss’ theorem to relate the divergence of J to the flux of J out of dV.

Now our problem. Figure 12-6 shows a uniform ball of uranium of radius R (dark gray) embedded within a large block of graphite (light gray). At equilibrium, what is the neutron density at a distance r from the ball’s center?

At equilibrium, the diffusion equation is: ∇·J = S ∇·(∇N) = –3S/(λv)

∇²N = –3S/(λv)

This is equivalent to the electrostatic equation: ∇²φ = –ρ/ε N is analogous to φ, and 3S/(λv) is analogous to ρ/ε. The solution here is the same as the electrostatic solution for a charged ball. Outside a ball of uniform charge density ρ per unit volume, the potential is: φ(r>R) = ρR³/(3εr)

Inside the ball (where r<R), the field is: E(r<R) = ρr/(3ε)

We need to match these at r=R, so we first integrate E to get φ: φ(r<R) = – ∫₀ʳ ρr dr / (3ε) = – ρr²/(6ε) + C At r=R, the two equations must yield the same potential, which defines the arbitrary integration constant C.

ρR³/(3εR) = – ρR²/(6ε) + C C = ρR²/(2ε)

φ(r<R) = (ρ/(6ε)) (3R² – r²)

φ(r>R) = ρR³/(3εr)

For neutron density N: N(r<R) = (S/(2λv)) (3R² – r²)

N(r>R) = SR³/(λvr)

Note the densities at r=0 and r=R: N(r=0) = (S/(2λv)) (3R²)

N(r=R) = (S/(2λv)) (2R²)

Even though the uranium ball is a uniform source, there are 50% more neutrons per unit volume near its center than its edge. This is because neutrons leak out at the edge.

In Volume II, page 12-8, Feynman notes that many phenomena are described by these diffusion equations, and now you know how to solve them all!

Flow of “Dry” Water

The next example concerns fluid flow in an extremely idealized circumstance. To simplify the math, Feynman chooses a fluid that is incompressible and irrotational, and that has zero viscosity and zero surface tension. Irrotational means the fluid has zero circulation.

– the curl of its flow is zero everywhere. Feynman says there are a few liquids like this, but very few, and water is certainly not this simple. Apparently, the great mathematician John von Neumann said these approximations were for people wishing to study “dry water.”

Nonetheless, let’s see what we can learn about dry water.

To represent its flow, let ρ be the fluid’s density and v(r) be the fluid’s velocity at r. Since the fluid is incompressible, ρ must be the same throughout. The rate of mass flow equals ρv.

We will further assume that the amount of fluid does not change — there are no sources or drains to add or remove fluid. This means the divergence of v must be zero. Since we assumed the fluid is irrotational, the curl of v must also be zero.

We thus have two equations that match the electrostatic equations of empty space (no charges): ∇·v = 0 ∇×v = 0

By analogy with electrostatics, we define a scalar function ψ such that: v = –∇ψ

Pushing the analogy, Feynman calls ψ the velocity potential. But calling it a potential may be misleading. As Feynman notes, ψ is a purely mathematical construct with no physical reality; it certainly is not a form of potential energy.

With ψ, we have a Laplacian equation: ∇²ψ = 0

Feynman next considers how this equation can explain the flow of dry water past a stationary ball of radius R, as shown in cross-section in Figure 12-7.

Figure 12-7 Irrotational Flow Past Ball

The lines in Figure 12-7 indicate the path of dry water molecules flowing past the ball. The lines are parallel to the fluid velocity vector field v everywhere. Because the liquid is incompressible, it must flow faster as it curves around the ball’s surface. The central flow line does not pass through the ball, as this 2-D view might suggest, rather it flows in front of or behind the ball in the third dimension.

To solve any problem involving differential equations, we need the equation (in this case ∇²ψ=0), and we need boundary conditions. Here, the boundary conditions are:

## 1. No flow inside the ball

## 2. Uniform flow far from the ball

Let r be the distance between any point P and the ball’s center. Let the vertical axis be +z, with z=0 at the center (r=0). To satisfy (1), the radial component of v must be zero on the ball’s surface. This means: At r = R, v = 0 and thus ∂ψ/∂r = 0

To satisfy (2), v is constant and entirely vertical at large r. This means: For r >> R, –∇ψ = (0,0,+v)

The electrostatic analogy identifies velocity potential ψ with electric potential φ, and velocity v with electric field E. Feynman says the analogous electrostatic problem is a ball with dielectric constant κ=0 in a uniform external field. While there are no actual dielectrics with κ=0, the equations of electrostatics can be solved for that case, which Feynman does next.

Our problem can be conveniently separated into two parts: a uniform electric field E; plus a dielectric ball with uniform polarization that exactly cancels E inside its surface. From Chapter 6, we know that such a ball produces the same field as a tiny dipole at its center. The potential φ is therefore the sum of the potentials due to a uniform field and due to a dipole: φ = – E z + µ z / (4πε r³)

0 0

We see that for large r we obtain the sought-for uniform field. We only need to find a value of µ that satisfies boundary condition (1). To take the partial derivative with respect to r, let us first express z in terms of r. For polar angle θ, z=rcosθ. We then have: φ(r) = – E r cosθ + µ cosθ / (4πε r²)

0 0

∂φ/∂r = – E cosθ – 2 µ cosθ / (4πε r³)

0 0

We require that ∂φ/∂r = 0 at r = R, for all θ. Thus: 0 = – E cosθ – µ cosθ / (2πε R³)

0 0

µ = – 2πε R³ E 0 0

The complete equation for φ, and by analogy for ψ, is: φ = – E r cosθ (1 + R³ / 2r³)

ψ = – v r cosθ (1 + R³ / 2r³)

Uniformly Lighting a Plane

Here we consider a problem involving an integral: the illumination of a plane surface.

Let’s first consider a single-point light source L at the center of a sphere S of radius r. All light from the source must pass through the sphere. If the source radiates equally in all directions, the fraction of light passing through an area A on sphere S equals A/4πr², since 4πr² is the sphere’s total area.

Now add a horizontal plane a distance d below L, as shown in cross-section in Figure 12-8.

Figure 12-8 Lighting A Plane

If area A << 4πr², we can approximate A as being a flat surface. Let B be the area on the plane that is illuminated by light passing through A. If θ is the angle between the flat surface A and the flat surface B, the area of B is larger than A by 1/cosθ. Hence L , the light intensity per unit area on B, is smaller than L , the light intensity per unit area on A, by the factor cosθ.

L = L cosθ B A

L = K cosθ / r² = K d / r³

We see that L is proportional to d/r³, with K being the proportionality constant.

For the same geometry, the light intensity due to L corresponds to the normal component of E due to a point charge.

We now ask a somewhat different question. Imagine A classroom whose ceiling has an array of very long, tubular, uniformly bright, parallel fluorescent lights, with distance w between adjacent lights. We wish to evenly illuminate tables that are a distance d below the lights. What value of w provides illumination that is uniform to 1 part per 1000? (This is beyond what is perceptible by eye, but it makes the problem more interesting.)

This problem is equivalent to finding the variation of the electric potential due to a set of parallel charged wires. Figure 12-9 shows a cross-section of this array, with the wires (black dots) running perpendicular to the screen (parallel to the y-axis). Let z measure the distance below the array, and x measure the distance across the array.

Figure 12-9 Equipotentials Below Charged Wires

As we discovered in Feynman Simplified 1D Chapter 45, any periodic function can be represented by a Fourier series of sinusoidal functions. Since the wires repeat along x with separation w, the x-dependence of the electric potential ø must be of this form: ø = Σ f_n cos(2πnx/w)

Here, the sum is from n=0 to n=∞. Each f_n can only be a function of z, not x. We therefore describe ø as: ø(x,z) = Σ f_n(z) cos(2πnx/w)

To satisfy the equation ∇²ø=0 for all x, each term in the sum must independently satisfy that equation. Let’s examine this equation for the nth term in the Fourier series.

0 = ∇² {f_n(z) cos(2πnx/w)} 0 = ∂²f/∂z² cos(2πnx/w) – f_n (4π²n²/w²) cos(2πnx/w)

∂²f/∂z² = f_n (4π²n²/w²)

f_n = A_n exp{–2πnz/w}

Since exp{–2π} ≈ 1/535, we need only deal with the n=0 and n=1 terms to obtain the required precision. At the table tops, z=d, and the potential is: ø(x,d) = A_0 + A_1 exp{–2πd/w} cos(2πx/w)

Assuming A_0 and A_1 are comparable, setting w=0.91d ensures no more than a ±1 part in 1000 variation across x. Feynman says an exact calculation shows that A_1=2A_0, which changes the requirement to w=0.83d. It is remarkable how uniform is the illumination from widely spaced lights.

The Unity of Nature

After exploring the commonality of the equations in electrostatics with those of other seemingly different areas of physics, Feynman asks in V2p12-12: “Why are the equations from different phenomena so similar? We might say: ‘It is the underlying unity of nature.’ But what does that mean? …The ‘underlying unity’ might mean that everything is made out of the same stuff, and therefore obeys the same equations. That sounds like a good explanation, but let us think. The electrostatic potential, the diffusion of neutrons, heat flow—are we really dealing with the same stuff? Can we really imagine that the electrostatic potential is physically identical to the temperature, or to the density of particles? Certainly ø is not exactly the same as the thermal energy of particles.

“A closer look … shows, in fact, that the equations are not really identical. The differential equation [for neutron diffusion] is an approximation, because we assume that the neutrons are smoothly distributed in space.

“Is it possible that this is the clue? That the thing which is common to all the phenomena is the space, the framework into which the physics is put? As long as things are reasonably smooth in space, then the important things … will be the rates of change of quantities with position in space. That is why we always get an equation with a gradient. The derivatives must appear in the form of a gradient or a divergence; because the laws of physics are independent of direction, they must be expressible in vector form. The equations of electrostatics are the simplest vector equations that one can get which involve only the spatial derivatives of quantities. Any other simple problem—or simplification of a complicated problem—must look like electrostatics. What is common to all our problems is that they involve space and that we have imitated what is actually a complicated phenomenon by a simple differential equation.

“That leads us to another interesting question. Is the same statement perhaps also true for the electrostatic equations? Are they also correct only as a smoothed-out imitation of a really much more complicated microscopic world? Our currently most complete theory of electrodynamics does indeed have its difficulties at very short distances. So it is possible, in principle, that these equations are smoothed-out versions of something. They appear to be correct at distances down to about 10×–14 cm, but then they begin to look wrong. It is possible that there is some as yet undiscovered underlying “machinery,” … But no one has yet formulated a successful theory that works that way.

“Strangely enough, it turns out (for reasons that we do not at all understand) that the combination of relativity and quantum mechanics as we know them seems to forbid the invention of an equation that is fundamentally different from [∇²ø=–ρ/ε] and which does not at the same time lead to some kind of contradiction. Not simply a disagreement with experiment, but an internal contradiction. As, f For example, the prediction that the sum of the probabilities of all possible occurrences is not equal to unity, or that energies may sometimes come out as complex numbers… No one has yet made up a theory of electricity for which [∇²φ = –ρ/ε] is understood as a smoothed-out approximation to a mechanism underneath, and which does not lead ultimately to some kind of an absurdity. But, it must be added, it is also true that the assumption that [this equation] is valid for all distances, no matter how small, leads to absurdities of its own (the electrical energy of an electron is infinite)—absurdities from which no one yet knows an escape.

## Chapter 12 Review: Key Ideas

Many phenomena are characterized by equations of the form: ∇·[A(r) ∇B(r)] = C(r)

Here, A, B, and C are scalar functions. Having learned how to solve this equation in electrostatics, we now know how to solve equivalent equations in many other areas of physics — the same equations have the same solutions.

Feynman suggests that similar equations arise in many different phenomena because all phenomena are described in the same space. All current theories of physics assume space is continuous, homogeneous, and isotropic — that all locations and all directions are equivalent. This means our equations can only involve spatial differentials, not absolute coordinates. The equations must therefore be written in vector algebra with gradients and divergences. Since electrostatics involves the simplest version of such differentials, all simple problems look like electrostatic problems.

## Chapter 13 Review

• Conversion constants (with q the fundamental unit charge): 1/(4πε) = 10–⁷ c² ≈ 9.0×10⁺⁹ newton-meter²/coulomb² or volt-meter/coulomb q²/4πε = 2.3068×10–²⁸ newton-meter² q²/4πε = 14.39 eV-angstroms

• F = q(E + v×B) is the Lorentz force F on a body with charge q and velocity v, in an electric field E and a magnetic field B.

• Linear superposition: for N sets of arbitrary charges with arbitrary motions, if set #j produces vector fields Eⱼ and Bⱼ, the fields produced by the sum of all sets are the vector sums: E = Σⱼ Eⱼ B = Σⱼ Bⱼ

• The gradient ∇ = (∂/∂x, ∂/∂y, ∂/∂z). For any scalar field ψ and displacement Δr, the change in ψ in that displacement is: Δψ = grad{ψ}•Δr = ∇ψ•Δr

The divergence of a vector field h is a scalar field φ: φ = div{h} = ∇•h = ∂hₓ/∂x + ∂hᵧ/∂y + ∂h_z/∂z

The curl of a vector field h is a vector field Q: Q = curl{h} = ∇×h

The Laplacian operator in rectilinear coordinates is: ∇² = ∇•∇ = ∂²/∂x² + ∂²/∂y² + ∂²/∂z²

• With operator ∇, Maxwell’s equations of electromagnetism are: ∇•E = ρ/ε ∇×E = – ∂B/∂t ∇•B = 0 c² ∇×B = ∂E/∂t + j/ε

Here, c is the speed of light, ρ is the charge density per unit volume, and j is the current density per unit area per unit time.

The electric potential φ for discrete charges and for continuous charge densities are: φ(r) = (1/4πε₀) Σⱼ {qⱼ / |r–rⱼ| } φ(r) = (1/4πε₀) ∫_V {ρ(σ) / |r–σ| } dV

The potential φ is related to E by: E = –∇φ ∇•E = ∇²φ = – ρ / ε₀

Linear superposition of fields ensures the linear superposition of potentials.

• Gauss’ theorem relates the divergence of vector field h throughout a volume V to the flux of h through the surface S enclosing V.

∫_S h•n dS = ∫_V ∇•h dV

Here, n is the unit vector normal to S at each point.

Stokes’ theorem relates the curl of vector field C across surface S to the line integral around the boundary Γ enclosing S: ∫_S (∇×C)•n da = ∫_Γ C•ds

Any vector field with zero curl everywhere is proportional to the gradient of some scalar field.

• Electric field energy U exists in the field itself. Its energy density is: dU / dV = (ε₀/2) E•E = (ε₀/2) E²

• A charged line of infinite length, with uniform charge density λ per unit length, produces a radial field E(r) given by: E(r) = λ / (2π ε₀ r)

A charged plane of infinite extent, with uniform charge density σ per unit area, produces a normal field E given by: E = σ / 2ε₀

• A charged ball of radius R, with total charge Q and uniform charge density ρ per unit volume, produces a radial field E(r) and has electrostatic energy U given by: For r≤R: E(r) = ρ r / 3ε₀ For r≥R: E(r) = Q / (4πε₀ r²)

U = (3/5) Q² / (4πε₀ R)

• Inside a conductor, or an empty cavity enclosed by a conductor, the electric field is always zero.

• A parallel-plate capacitor whose plates each have area A, have opposite charge densities +σ and –σ, and are separated by an insulator with dielectric constant κ and thickness d, has field E, voltage V, charge Q, capacitance C, and stored energy U given by: E = σ/κε₀ Q = σ A C = Aκε₀/d V = E d = Q / C U = Q² / 2C = C V² / 2

• A sphere of radius R and charge Q has stored energy U and capacitance C relative to infinity given by: C = 4πε₀ R U = Q² / (8πε₀ R)

• Dipole Moment: for two equal but opposite charges +q and –q, separated by vector d, the dipole moment µ and electric potential are: µ = qd, µ points from –q to +q.

φ(r) = µ•r̂ / (4πε₀ r²) = – (1/4πε₀) µ•∇(1/r)

• In insulators, an external field E induces a dipole moment qδ… in each atom. For N atoms per unit volume, the induced polarization vector P, surface charge density σ, electric susceptibility χ, and dielectric constant κ are: P = N qδÊ σ = N qδ = |P| P = χε₀E κ = 1+χ • Some authors define a vector field D as: D = ε₀κE + P = ε₀E ∇·(κE) = ρ_free/ε₀ Here ρ_free is the charge density outside dielectrics, ε is a dielectric’s permittivity, with ε₀ being the permittivity of vacuum. Feynman says these equations are not always valid and recommends using the vacuum equations that are always correct.

Meet The Author Congratulations and thank you for reading my book. I know your time is valuable, and I sincerely hope you enjoyed this experience.

I’d like to tell you something about myself and share some stories.

First, the obligatory bio (as if 3 “tweets”-worth can define anyone): I have a B.S. in physics from Caltech, a Ph.D. in high-energy particle physics from Stanford University, and was on the faculty of Harvard University. Now “retired,” I teach at the Osher Institutes at UCLA and CSUCI, where students honored me as “Teacher of the Year.” In between, I ran eight high-tech companies and hold patents in medical, semiconductor, and energy technologies.

My goal is to help more people appreciate and enjoy science. We all know one doesn’t have to be a world-class musician to appreciate great music — all of us can do that. I believe the same is true for science — everyone can enjoy the exciting discoveries and intriguing mysteries of our universe.

I’ve given 400+ presentations to general audiences of all ages and backgrounds, and have written 3 printed books and 29 eBooks. My books have won national and international competitions, and are among the highest rated physics books on Amazon.com. I’m delighted that two of these recently became the 2nd and 3rd best sellers in their fields.

Richard Feynman was a friend and colleague of my father, Oreste Piccioni, so I knew him well before entering Caltech. On several occasions, Feynman drove from Pasadena to San Diego to sail on our small boat and have dinner at our home. Feynman, my father, my brother and I once went to the movies to see “Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb.” It was particularly poignant watching this movie next to one of the Manhattan Project’s key physicists.

At Caltech I was privileged to learn physics directly from this greatest scientist of our age. I absorbed all I could. His style and enthusiasm were as important as the facts and equations. Top professors typically teach only upper-level graduate classes. But Feynman realized traditional introductory physics didn’t well prepare students for modern physics. He thought even beginners should be exposed to relativity, quantum mechanics, and particle physics. So he created a whole new curriculum and personally taught freshman and sophomore physics in the academic years 1961-62 and 1962-63.

The best students thrived on a cornucopia of exciting frontier science, but many others did not. Although Caltech may be the world’s most selective science school, about half its elite and eager students drowned in Feynman’s class. Even a classmate, who decades later received the Nobel Prize in Physics, struggled in this class. Feynman once told me that students sometimes gave him the “stink eye” — he added: “Me thinks he didn’t understand angular momentum.” Some mundane factors made the class very tough: Feynman’s book wasn’t written yet; class notes came out many weeks late; and traditional helpers (teaching assistants and upper classmen) didn’t understand physics the way Feynman taught it.

But the biggest problem was that so much challenging material flew by so quickly. Like most elite scientists, Feynman’s teaching mission was to inspire the one or two students who might become leading physicists of the next generation. He said in his preface that he was surprised and delighted that 10% of the class did very well.

My goal is to reach the other 90%.

It’s a great shame that so many had so much difficulty with the original course — there is so much great science to enjoy. I hope to help change that and bring Feynman’s genius to a wider audience.

Please let me know how I can make Feynman Simplified even better — contact me through my WEBSITE.

While you’re there, check out my other books and sign-up for my newsletters.

Printed Books, each top-rated by Amazon readers: Everyone's Guide to Atoms, Einstein, and the Universe Can Life Be Merely An Accident?

A World Without Einstein The Everyone's Guide Series of Short eBooks Einstein: His Struggles, and Ultimate Success, plus Special Relativity: 3 Volumes, A to Z General Relativity: 4 Volumes, from Introduction to Differential Topology Quantum Mechanics: 5 Volumes, from Introduction to Entanglement Higgs, Bosons, & Fermions… Introduction to Particle Physics Cosmology Our Universe: 5 Volumes, everything under the Sun Our Place in the Universe: a gentle overview Black Holes, Supernovae & More We are Stardust Searching for Earth 2.0 Smarter Energy Timeless Atoms Science & Faith Table of Contents

## Chapter 1 Overview of Electromagnetism

## Chapter 2 Gradient, Divergence & Curl

## Chapter 3 Line, Surface & Volume Integrals

## Chapter 4 Electrostatics

## Chapter 5 Gauss' Law in Action

## Chapter 6 Dipole Electric Fields

## Chapter 7 Charges & Conductors

## Chapter 8 Electrostatic Energy

## Chapter 9 Electricity in the Atmosphere

## Chapter 10 Dielectric Materials

## Chapter 11 Inside Dielectrics

## Chapter 12 Electrostatic Analogs

## Chapter 13 Review

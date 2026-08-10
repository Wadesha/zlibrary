# Feynman Simplified 2C Electromagnetism in Relativity in Dense Matter Robert L Piccioni Z Library

> 来源文件：pre_Feynman_Simplified_2C_Electromagnetism_in_Relativity_in_Dense_Matter_Robert_L_Piccioni_Z_Library.txt
> 字符数（约）：230049
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Feynman Simplified 2C: Electromagnetism: in Relativity & in Dense Matter Everyone’s Guide to the Feynman Lectures on Physics by Robert L. Piccioni, Ph.D.

Copyright © 2015 by Robert L. Piccioni Published by Real Science Publishing 3949 Freshwind Circle, Westlake Village, CA 91361, USA Edited by Joan Piccioni Visit our web site www.guidetothecosmos.com

Everyone’s Guide to the Feynman Lectures on Physics Feynman Simplified gives mere mortals access to the fabled Feynman Lectures on Physics.

This Book Feynman Simplified: 2B covers one quarter of Volume 2 of The Feynman Lectures on Physics. The topics we explore include: Relativistic Maxwell’s Equations Lorentz Transform for Potentials & Fields Field Energy, Momentum & Mass Relativistic Particles in Fields Crystals Refraction & Reflection in Dense Matter Waveguides To find out about other eBooks in the Feynman Simplified series, click HERE. I welcome your comments and suggestions. Please contact me through my WEBSITE. If you enjoy this eBook please do me the great favor of rating it on Amazon.com or BN.com.

Table of Contents

## Chapter 25: Waveguides

## Chapter 26: Relativistic Electrodynamics

## Chapter 27: Transformation of Fields

## Chapter 28: Energy & Momentum of Fields

## Chapter 29: Electromagnetic Mass

## Chapter 30: Particles in Fields

## Chapter 31: Crystals

## Chapter 32: Refraction in Dense Matter

## Chapter 33: Reflection & Transmission

## Chapter 34: Clever Tricks

## Chapter 35: Review of Part 2C

## Chapter 25: Waveguides

In Chapter 23, we examined the behavior of simple circuit elements as a function of frequency. We learned that the character of those elements often changes dramatically as frequencies increase. In V2p24-1, Feynman says: “Another interesting technical problem is the connection of one object to another, so that electromagnetic energy can be transmitted between them. In low-frequency circuits the connection is made with wires, but this method doesn’t work very well at high frequencies because the circuits would radiate energy into all the space around them, and it is hard to control where the energy will go. The fields spread out around the wires; the currents and voltages are not “guided” very well by the wires. In this chapter we want to look into the ways that objects can be interconnected at high frequencies.” In this chapter, we examine the theory of transmission lines: the “guiding” of electromagnetic waves in confined spaces toward desired destinations.

For low frequency AC, such as 50 or 60 Hz, simple wires are adequate across distances up to hundreds of miles or kilometers. At 60 Hz, electromagnetic wavelengths in conductors may be 2000 miles (assuming wave velocity is about 2/3 of the speed of light). This means the quarter-wavelength at which radiation peaks is about 500 miles. At 50 Hz, the quarter-wavelength is about 1000 km. For kilohertz frequencies, such as local telephone wiring, twisted-pairs are employed to reduce crosstalk. Figure 25-1 shows four twisted-pairs that can carry four separate telephone conversations.

Figure 25-1: Four Twisted-Pairs Twisting makes it more difficult for one party to hear another party's conversation, and reduces interference by diminishing signal pick-up in one pair due to fields radiated by adjacent pairs.

Frequencies in the megahertz range are often transmitted through coaxial cables (“coax”). The simplest coax consists of two coaxial, thin hollow cylinders. Typically, the signal or power is transmitted through the central tube, while the outer tube is a ground shield connected to a zero-volt potential. Figure 25-2 shows an inner conductor with radius r, and an outer conductor with radius R.

Figure 25-2: Coaxial Cable One of the great advantages of coax is that its electromagnetic fields are completely contained in the space between the conductors (ideally). This means coaxial cables do not interfere with one another, even if many are bundled tightly together. They are also unaffected by external electrical devices or fields.

In Chapter 22, we found that the impedance Z of a transmission line with inductance L and capacitance C per unit length is: Z = √(L / C)

Let’s now analyze transmission through a coaxial cable from a different perspective. Figure 25-3 shows a cross-section of the interior of a coax (shown in gray), with the outer conductor at zero volts, and a signal propagating through the inner conductor that is represented by a solid black line. At a distance x from the start of the coax, let the signal voltage be V(x) and the current be J(x). A small distance further down the cable, at position x*, the signal has voltage V(x*) and current J(x*).

Figure 25-3: Signal In Coax For a time-varying current, the coax has an inductive impedance L per unit length. This causes a voltage drop given by: ΔV = V(x*) – V(x) = – L (x*–x) ∂J/∂t ΔV / Δx = – L ∂J/∂t In the limit that Δx goes to zero (x* goes to x), we obtain a differential e quation: ∂V/∂x = – L ∂J/∂t We obtain a second differential equation by considering the time-varying voltage. The coax has capacitance C per unit length, so in a small length Δx = (x*–x), the stored charge q is: q = C Δx V The net current flowing into Δx must equal the change in charge within Δx. This means: J(x) – J(x*) = ∂q/∂t = C Δx ∂V/∂t In the limit that Δx goes to zero, this means: – ∂J/∂x = C ∂V/∂t Feynman says these are the two basic differential equations for any transmission line, adding: “We could modify them to include the effects of resistance in the conductors or of leakage of charge through the insulation between the conductors, but for our present discussion we will just stay with the simple example.”

We now combine these equations using a familiar trick: differentiate the first equation with respect to x and the second with respect to t, so that both contain the term ∂2J/∂t∂x.

∂2V/∂x2 / L = – ∂2J/∂t∂x C ∂2V/∂t2 = – ∂2J/∂t∂x ∂2V/∂x2 – L C ∂2V/∂t2 = 0

The same trick, done the other way, yields two equations containing ∂2V/∂t∂x.

L ∂2J/∂t2 = – ∂2V/∂x∂t ∂2J/∂x2 / C = – ∂2V/∂x∂t ∂2J/∂x2 – C L ∂2J/∂t2 = 0

We see that both V and J satisfy the 1-D wave equation: ∂2ψ/∂x2 – ∂2ψ/∂t2 / v2 = 0 With v = 1/√(L C), all solutions are of the form: ψ = f(x–t/v) + g(x+t/v)

Here, f is a wave moving toward +x with a voltage and a current that we will call V and J , and g is a wave moving toward –x with V and J .

+ + – –

Let’s now calculate the key parameters of a coaxial cable: L, C, Z, and v.

Recall that in Chapter 18, we found the inductance of a solenoid by calculating its field energy. We will use the same approach here, and calculate the field energy of a coax.

The magnetic field energy is given by: U = (εc2/2) ∫ B•B dV The B field at a distance ρ from a wire carrying current J is: B = J / (2πεc2ρ)

In cylindrical coordinates, the volume integral over dV is: dV = ρ dx dβ dρ Here, x is the distance along the wire, ρ is the distance from the wire, and β is the azimuthal angle. The extra ρ arises because the distance moved by an incremental change in azimuthal angle is ρdβ.

The integral over dβ equals 2π, and the integral over dx equals X, the length of the cable. (I’d prefer L, but we’re already using L for inductance.) The integral over ρ is over the region between the two cylindrical conductors, from ρ=r to ρ=R. There is no magnetic field outside the coax, because there is no net current flow through a cross-sectional surface that includes both conductors.

The magnetic energy per unit length U/X is then: U = (εc2/2) ∫ 2πX ρ dρ J2 / (2πεc2ρ)2 U = (J2/2) ∫ X (dρ/ρ) / (2πεc2)

U / X = (J2/2) ∫ (dρ/ρ) / (2πεc2)

U / X = ln(R/r) J2 / (4πεc2)

Another equation for magnetic field energy is: U = LJ2/2 Equating these equations yields L, the inductance per unit length.

U/X = L J2 / 2X U/X = ln(R/r) J2 / (4πεc2)

L = L / X = ln(R/r) / (2πεc2)

Now on to the capacitance. In Chapter 12, we found the stored charge of a coaxial capacitor at voltage V (the analog of heat flow between two concentric pipes). In our current notation, the equation is: Q = (2πε) V X / ln(R/r)

C = Q / VX = (2πε) / ln(R/r)

This is the capacitance when the gap between conductors is empty (ideally, it would be vacuum). We therefore have the wave velocity v and impedance Z: 1/v2 = L C 1/v2 = {ln(R/r) / (2πεc2)} {(2πε) / ln(R/r)} 1/v2 = {1 / c2 } v = ± c Z2 = L / C Z2 = {ln(R/r) / (2πεc2)} / {(2πε) / ln(R/r)} Z2 = { ln(R/r)2 / (2πε)2c2) } Z = ln(R/r) / (2πεc)

Feynman says the constant 1/(2πεc) has the units of resistance and a value of 60 ohms. The ratio R/r is never very large, and the impedance varies only logarithmically with that ratio. The result is that almost all coaxial cables have impedances between 50 ohms and a few hundred ohms.

Real coax has a dielectric between the inner and outer conductors, which changes the above results.

Rectangular Waveguides In V2p24-4, Feynman says: “The next thing we want to talk about seems, at first sight, to be a striking phenomenon: if the central conductor is removed from the coaxial line, it can still carry electromagnetic power. In other words, at high enough frequencies a hollow tube will work just as well as one with wires. It is related to the mysterious way in which a resonant circuit of a [capacitor] and inductance gets replaced by nothing but a can at high frequencies.

“Although it may seem to be a remarkable thing when one has been thinking in terms of a transmission line as a distributed inductance and capacity, we all know that electromagnetic waves can travel along inside a hollow metal pipe. If the pipe is straight, we can see through it! So certainly electromagnetic waves go through a pipe.” Sometimes a simple observation is worth a thousand equations.

Let’s find out what kind of waves can go through a pipe. In this mode, the pipe is called a waveguide. While the basic principles are the same for pipes of all shapes, we will analyze a rectangular one.

We define a rectangular pipe that starts at z=0 and runs along the z-axis toward z=∞, with width X and height Y, as shown in the upper two images of Figure 25-4.

Figure 25-4 Rectangular Waveguide Assume an unspecified wave source at z<0. We know that the E and B fields of light waves are orthogonal to the direction of propagation. So, let’s first look for solutions in which E is entirely in the y-direction, as shown in the middle image of Figure 25-4.

The lower image shows the magnitude of E_y versus position x across the pipe. E_y must be zero at both edges of the pipe, at x=0 and x=X, because electric fields never have a component along the surface of an ideal conductor. If one did, charges in the conductor would move, immediately nullifying that field component.

We found a similar situation in Chapter 23, where the solution was a Bessel function. But that was in cylindrical geometry. Here, in rectangular geometry, the solution is a sinusoid of the form: E_y sin(k_x x)

This automatically ensures E_y=0 at the pipe wall at x=0. To also ensure E_y=0 at the pipe wall at x=X, we must require sin(k_x X)=0, which means k_x X=nπ, for any integer n>0.

For the z-dependence, let’s try a typical wave solution: exp{iωt–ik_z z}.

Putting these pieces together, we get: E_y = E_0 sin(k_x x) exp{iωt–ik_z z} Figure 25-5 shows the E and B fields in the waveguide, with E reaching its maximum at the left and right ends of the image, and reaching its minimum (most negative) in between.

Figure 25-5 Fields In Waveguide Inserting the expression for E_y into the 3-D wave equation yields: 0 = ∂²E_y/∂x² + ∂²E_y/∂y² + ∂²E_y/∂z² – (1/c²) ∂²E_y/∂t² 0 = – k_x² E_y – k_z² E_y – (–ω²/c²) E_y k_x² + k_z² = ω² / c² Since we already constrained k_x, this establishes a relationship between k_z and ω.

k_z = ± √ {(ω/c)² – (nπ/X)²} The “±” sign determines the wave direction: “+” for waves moving toward +z, and “–” for waves moving toward –z.

From this equation, we obtain the phase velocity (see Feynman Simplified 1D, Chapter 43): v_ph = ω / k_z The guide wavelength λ_wg, the wavelength inside the waveguide, is: λ_wg = 2π v_ph / ω In empty space, the wavelength is: λ_0 = 2πc/ω. Comparing the two wavelengths yields: λ_wg = 2π / √ {(ω/c)² – (nπ/X)²} λ_wg = 1 / √ {(ω/2πc)² – (n/2X)²} λ_wg = 1 / √ {(1/λ_0)² – (n/2X)²} λ_wg = λ_0 / √ {1 – (nλ_0/2X)²} For very high frequencies, when ω>>c/X, the waveguide wavelength approaches the free space wavelength. For visible light and typical waveguides, λ_wg and λ_0 are virtually equal.

Cutoff Frequency Now consider low frequency waves traveling through our pipe. Let’s focus on the lowest transverse mode, the least oscillation in the x-direction, which corresponds to n=1. As the frequency decreases, the wavelength increases at a faster than usual rate. In empty space, λ is inversely proportional to ω. But in a waveguide, we can rewrite the equation for λ_wg as (with Ω=πc/X): λ_wg = 2πc / √ { ω² – Ω² } λ_wg = 2πc / √ { (ω–Ω) (ω+Ω) } When ω is close to Ω, λ_wg becomes inversely proportional to 1/√(ω–Ω). This means λ_wg approaches infinity much more quickly than in empty space: at ω=Ω rather than at ω=0. Ω=πc/X is the cutoff frequency of a waveguide of width X for E orthogonal to the width.

Consider the wave number k_z for frequencies below the cutoff (for n=1). Let’s rewrite our prior equation for k_z: k_z = ± (1/c) √ {ω² – Ω²} k_z = ± i (1/c) √ {Ω² – ω²} k_z = ± i K with K = (1/c) √ {Ω² – ω²} When ω is less than cutoff frequency Ω, the wave number k_z is imaginary. This is not as crazy as it might sound. Let’s insert this imaginary wave number into the wave equation.

E_y = E_0 sin(k_x x) exp{iωt–ik_z z} E_y = E_0 sin(k_x x) exp{iωt} exp{±Kz} E_y = E_0 sin(k_x x) exp{iωt} exp{–Kz} In the last line, we assumed the wave source was at z<0, and therefore rejected the “+” sign that leads to an unrealistic exponentially increasing wave. The last equation describes an electric field that oscillates over time but decreases exponentially as it travels through the waveguide. Waves with ω<Ω cannot propagate much farther than z~1/K. Waves with frequencies below Ω are cutoff.

In V2p24-6, Feynman stresses this key point: “Normally, if we solve an equation in physics and get an imaginary number, it doesn’t mean anything physical. For waves, however, an imaginary wave number does mean something. The wave equation is still satisfied; it only means that the solution gives exponentially decreasing fields instead of propagating waves. So in any wave problem where k becomes imaginary for some frequency, it means that the form of the wave changes—the sine wave changes into an exponential.”

Guided Wave Speeds From above we have: k_z = (1/c) √ {ω² – Ω²} v_ph = ω / k_z Combining these yields a more revealing equation for the phase velocity: v_ph = ω c / √ {ω² – Ω²} v_ph = c / √ {1 – (Ω/ω)²} For ω<Ω, the phase velocity is imaginary; these frequencies are cutoff.

For ω>Ω, the denominator is less than 1, so v_ph > c. As we discussed in Feynman Simplified 1D, Chapter 43, a phase velocity greater than c does not violate relativity because it does not correspond to the transmission of information or energy.

Chapter 43, this does not violate special relativity because phase velocity is the speed of a pure sine wave, a mathematical entity that cannot represent any physical entity and cannot carry information. Only wave packets, comprised of multiple frequencies, can represent information or physical entities. When multiple frequencies are combined, forming a complex waveform, it is often impossible to definitively determine the resulting wave’s phase or velocity. Which feature should one track over time if the waveform is continually changing as some frequencies move faster than others?

Figure 25-6 shows a wave packet formed by a spectrum of high frequency sinusoids interfering with one another, producing wave groups, enclosed by an envelope (dotted lines).

Figure 25-6 Wave Packet & Groups

Individual single-frequency sinusoids within the wave packet can move faster than c, with their peaks advancing from group to group. However, the envelope and the groups it encloses move slower than c; their speed is the group velocity, given by: v_gp = dω/dk

Feynman calculates v_gp using dω/dk = 1/(dk/dω), as follows: dk/dω = (1/c) (1/2) [ω² – Ω²]^{-1/2} (2ω)

v_gp = dω/dk = 1 / dk/dω v_gp = c / {[ω² – Ω²]^{-1/2} (ω)} v_gp = c [1 – (Ω/ω)²]^{+1/2}

If that seems too tricky, one can reach the same result more conventionally by: c²k² = {ω² – Ω²} ω = √{ c²k² + Ω²} dω/dk = (1/2) 1/√{c²k² + Ω²} (2c²k)

v_gp = 1/√{ω² – Ω² + Ω²} c√{ω²–Ω²} v_gp = (c/ω) √{ω²–Ω²} v_gp = c √[1 – (Ω/ω)²]

As usual, Feynman’s trick gets the right result with less math.

For frequencies ω greater than the cutoff Ω, the group velocity will always be c or less.

For a waveguide, the product of phase velocity and group velocity is: v_ph v_gp = {ω/k} {dω/dk} = {c / √ [1 – (Ω/ω)²]} {c √[1 – (Ω/ω)²]} v_ph v_gp = c²

This relationship is generally not valid for waves propagating through matter, particularly in the case of anomalous refraction, as we discuss in later chapters.

Feynman emphasizes a “curious” and “interesting” similarity between a wave in a waveguide and a particle wave in relativistic quantum mechanics. Do not be surprised that this similarity hints at a deep underlying principle.

In relativistic quantum mechanics, a particle’s energy ħω, momentum ħk, and mass m are related by: U = ħω = √ {p²c² + m²c⁴} ħ²ω² = ħ²k²c² + m²c⁴ k = (1/c) √{ω² – (mc/ħ)²}

With Ω = mc/ħ, this equation matches that of a waveguide.

In a waveguide, energy propagates at the group velocity. The amount of energy transported per unit time equals (the energy density in the guide) multiplied by (the guide’s cross-sectional area) multiplied by (the group velocity). Feynman states without proof that the magnetic field and the electric field have equal energy densities in a waveguide. Hence the total power is: power = dU/dt = ε₀ E_rms² X Y v_gp

Here, E_rms is the root-mean-square electric field. Feynman doesn’t calculate this here, but we can.

From above, the electric field is: E_y = Real part [ E_x sin(kx) exp{iωt–ikz} ]

E_y = E_x sin(kx) cos(ωt–kz)

E_y = E_x sin(kx) × { cos(ωt)cos(kz) + sin(ωt)sin(kz) }

E_rms² = E_y² ∫∫∫ sin²(kx) dx dt dz × ∫∫∫{cos(ωt)cos(kz)+sin(ωt)sin(kz)}² dt dz

The average value of sin² or cos² over a full cycle is 1/2. The cross terms in the last line integrate to zero, since they contain integrands like cos(ωt)sin(ωt) that have an average value of zero over a full cycle. This leaves only the squared terms.

E_rms² = (E_x²/2) × ∫∫∫{cos²(ωt)cos²(kz)+sin²(ωt)sin²(kz)} dt dz E_rms² = (E_x²/2) {(1/2)(1/2)+(1/2)(1/2)} E_rms² = (E_x²/2) {1/2} E_rms = E_x /2

Measuring Waveguide Fields

We discovered in Chapter 23 that by opening a small hole in the wall of a resonant cavity and inserting a wire, we can inject energy or measure the internal fields. The same procedures apply to waveguides.

If an RF generator drives the inserted wire at any frequency greater than the cutoff frequency, energy is transferred to waves propagating down the waveguide. If instead, the wire is connected to an appropriate detector, the wire measures the wave energy at its location.

If a waveguide were infinitely long, waves would propagate indefinitely, according to the equations derived in the prior section. (We implicitly assumed above that the waveguide has no end.) Of course, real waveguides all have ends. But they can still act exactly like infinite waveguides if their ends are terminated properly with devices that absorb all incident wave energy.

Whether infinitely long or properly terminated, the same average energy is observed everywhere along the length of the waveguide.

By contrast, something very different happens when a waveguide has conducting end plates orthogonal to its axis. The result is exactly what we discovered about waves traveling along strings with immovable ends: waves are reflected and inverted at each end. (See Feynman Simplified 1D, Chapter 44). Waves moving toward +z and waves moving toward –z interfere with one another, forming standing waves, just as We found for the vibrating strings of violins. The E field equation for a standing wave is: E_y = E_x sin(k_x x) sin(k_z z) cos(ωt+β)

Here, β is an arbitrary phase angle, k_z = mπ/Z, Z is the waveguide’s length, and m is any integer greater than zero. The factor sin(k_z z) ensures the wave has E_z = 0 at both conducting end plates. With this factor, wave energy is no longer the same at all z. Instead, the energy is always maximal whenever kz is an odd multiple of π/2, and is zero whenever kz is a multiple of π.

Everything in this section describes the properties of waves with frequencies above the cutoff Ω. Below that frequency, waves decrease exponentially with z, and are oblivious to what happens at the waveguide’s end, provided Z is much longer than the absorption length 1/K.

Waveguide Plumbing

Coaxial cables can carry high-frequency signals, but their maximum power is limited by several factors. Because their central conductor is small, its current density is quite high. And since power dissipation is proportional to the square of current density, power losses and heat generation are major issues. Also, the central conductor must be supported, typically by an insulating dielectric that limits the maximum sustainable voltage and that usually dissipates large amounts of power at high frequencies.

By eliminating the central conductor, waveguides avoid many of the limitations of coax, particularly in the transmission of high-frequency high-power electromagnetic waves. In V2p25-8, Feynman notes that a typical application is coupling a radar generator to its antenna. Power from the generator travels through a waveguide that ends in a horn, an open-ended pipe that flares out and spreads the electromagnetic wave across a large antenna. Placing the horn at the focus of a parabolic antenna converts the wave into a wide beam focused in one direction with minimal angular divergence. A sample horn is shown in Figure 25-7.

Figure 25-7 Waveguide “Horn”

Assembling a waveguide system is called microwave plumbing, because it is more like connecting water pipes than electrical wires. Waveguide tubes are bolted together, turns are gently curved, and interconnections are carefully engineered.

One piece of plumbing is particularly interesting: the one-way coupler shown in Figure 25-8. The upper image shows the overall coupler, while the lower image zooms in on its critical feature. Waves can enter the lower pipe from either the left or right ports, and can pass straight through to the opposite port. But for selected frequencies, only waves entering from the left port can produce waves exiting the upper port.

Figure 25-8 One-Way Coupler

The key point here is the spacing of two holes between the upper and lower tubes. Each hole allows a portion of the waves in the lower tube to enter the upper tube. For waves entering the left port (solid lines), the path length to the upper port is the same regardless of which hole waves pass through. Therefore, waves from both holes interfere constructively, producing a wave that exits the upper port. Conversely, waves entering the right port (dashed lines) and passing through the two holes have two different path lengths to the upper port. When the distance between the holes equals one-quarter wavelength, waves from the two holes have a 180-degree relative phase shift; they interfere destructively, and no wave enters the upper tube.

Waveguide Modes

We have so far focused on one oscillation mode, characterized by: E_y = E_x sin(k_x x) exp{iωt–ik_z z} with k_x = π/X Here, the electric field is entirely in the y-direction, and it spans one-half wavelength in the x-direction. Clearly, there are many other possible modes, including modes with more oscillation in the x-direction (k_x = nπ/X, for n>1), and modes with more geometric complexity. If the electric field is entirely within the xy-plane, the magnetic field has a z-component, and the oscillation is called a transverse-electric (“TE”) mode. If E has a component in the z-direction, the magnetic field is entirely in the xy-plane, and the oscillation is called a transverse-magnetic (“TM”) mode.

In rectangular waveguides, the lowest cutoff frequency occurs in the TE mode that we examined first. This is because Ω = nπc/X is lowest when n=1 and the side dimension X is as large as possible. Typically, waveguides are used at frequencies just slightly higher than the lowest cutoff. This ensures that only the lowest mode propagates through the waveguide, which simplifies its use.

Feynman Remarkable Prospective

In V2p25-10, Feynman presents an intriguing insight explaining the origin of a waveguide’s cutoff frequency. We earlier derived the cutoff equation mathematically, showing that the wave number becomes imaginary at low frequencies. There is nothing wrong with that derivation. Indeed, the same analysis leads to even more profound results in quantum mechanics. But, here Feynman provides a different approach that is less “imaginary” and may appeal more to your physical intuition. This approach works only for rectangular waveguides, while the "imaginary" approach works for waveguides of any shape.

You have probably noticed that the waveguide's vertical size Y does not enter into any of our prior equations. Feynman says that, in the TE-E mode, our waveguide operates identically for any value of Y, even for Y=∞.

We therefore consider the waveguide shown in Figure 25-9, where the y-axis points out of the screen. The waveguide sidewalls at x=0 and at x=X extend to y=±∞. A vertical wire S that also extends to y=±∞ is located midway between the sidewalls, at x=X/2, z=0. The wire carries a current oscillating at frequency ω that produces electromagnetic waves that travel down the waveguide.

Figure 25-9: Wire Source Between Sidewalls

An isolated wire radiates cylindrical expanding waves. But the waveguide sidewalls constrain the wire's radiation pattern. Assuming the sidewalls are ideal conductors, electric fields must be perpendicular to the sidewalls at their surface. We learned how to satisfy that requirement in Chapter 7: the fields from a charge near a conducting plane are the same as the fields from a charge and an image charge.

In Volume 2, page 25-11, Feynman says: "The image idea works just as well for electrodynamics as it does for electrostatics, provided, of course, that we also include the retardations. We know that is true because we have often seen a mirror producing an image of a light source. And a mirror is [an almost ideal] conductor for electromagnetic waves with optical frequencies."

The fields from S₀ are unchanged by replacing the upper wall with an opposite polarity source (call that S₁) at x=2X; the same distance above the upper wall as S₀ is below it. We define the polarity of S₀ to be "+", which makes S₁ "–". By "opposite polarity" we mean the oscillating currents in S₀ and in S₁ have a relative phase shift of 180 degrees.

Similarly, the image of S₀ in the lower wall is an opposite polarity source (call that S₂) at x=–X/2; the same distance below the lower wall as S₀ is above it. The polarity of S₂ is "–".

But this is not the end by any means. As everyone who has stood between two parallel mirrors knows, one sees more than just two images; in fact one sees an infinite number of images. Each image produces another opposite polarity image of itself in the opposite mirror. The result here is an infinite column of sources of alternating polarities, as shown in Figure 25-10. The dotted lines indicate where the waveguide sidewalls originally were before being replaced by image sources.

Figure 25-10: Infinite Column of Sources

As Feynman says, this is: "in fact just what you would see if you looked at a wire placed halfway between two parallel mirrors." The field in the waveguide is the same either with sidewalls or with an infinite column of alternating sources.

We discovered how to solve this problem in Feynman Simplified 1C, Chapter 32, where we calculated the radiation field from various dipole arrays. (Feynman is showing us how all these different ideas fit together in one comprehensive theory.)

Close to the sources, the fields are quite complex. Fortunately, what we are interested in here is waveguide transmission. So in what follows, we will consider only fields far from the sources at z=0.

There is no direct radiation along the z-axis (the waveguide axis) because there are equal numbers of sources of opposite polarities that cancel one another. Where then do the waveguide's waves come from?

We also found in Feynman Simplified 1C that dipole arrays radiate in certain directions: the directions in which the waves from each source interfere constructively.

Figure 25-11 illustrates when this happens. Here, at some time t, we see plane waves radiating up and to the right, at an angle +θ relative to the z-axis. The light solid lines indicate wave crests, and the light dotted lines indicate wave troughs. The distance between consecutive crests (or troughs) is the wavelength λ.

Figure 25-11: Radiation at Angle +θ

Since we removed the waveguide walls, we will assume the remaining space is empty. The wave propagation velocity v is therefore c, the speed of light in vacuum, and λ = 2πc/ω.

Examine the gray right triangle that is enlarged in the lower portion of this image. The hypotenuse has length 2X, which is the distance between consecutive sources of the same polarity. The shortest side of the triangle has length u, and the angle at the top is θ.

For radiation from S₁ and from S₂ to interfere constructively, the extra distance u traveled from S₂ must be an integer number of wavelengths. This means: u = ±mλ with m an integer 2X sinθ = u sinθ = ±mλ / 2X

For now, we will just consider the case of m=1.

Note that this equation has no solutions for λ > 2X: a line of sources cannot constructively interfere at any angle if the wavelength is too great (if the frequency is low). We will see that this leads to the same cutoff criterion we found earlier.

Also note that "+" and "–" polarities produce waves with opposite phases.

polarity sources also interfere constructively with S at angle θ. A similar triangle drawn with S-S as the hypotenuse has sides that are half as large as the original triangle. The requirement for constructive interference between S and S is therefore u/2=λ/2, which is exactly what the opposite polarities of S and S provide.

1 0 0 1 0 Thus all sources radiate constructively at angle θ. By symmetry, they also radiate constructively at angle –θ, which is shown in Figure 25-12.

Figure 25-12 Radiation at Angle –θ Here, the radiation moves down and to the right, also at v=c with wavelength λ. The actual radiation pattern is the superposition of radiation at +θ and at –θ. That superposition at some time t is shown in Figure 25-13. Again, the dotted horizontal lines indicate where the waveguide walls were before being replaced by image sources.

Figure 25-13 Sum of +θ & –θ Radiation The three small dots with the letters A, B, and C below them indicate points where the +θ and –θ waves interfere maximally. Crests from both radiation patterns combine to produce the maximum positive E field at A and C, while their troughs combine to produce the minimum (greatest negative) E field at B.

As time t increases, the +θ waves move up and to the right while the –θ waves move down and to the right, both at speed c with wavelength λ. In one full wave period, the crest at point A moves to point C; hence, the distance AC equals one guide wavelength, which we called λwg above.

The distance AC is the length of the hypotenuse of the gray right triangle near the bottom of Figure 25-13. The middle-length side of this triangle is the distances between crests of the +θ wave, which is λ. And the angle between those two sides is θ. This defines the relationship between the two wavelengths:

λwg = λ / cosθ λwg = λ / √{1–sin²θ} λwg = λ / √{1–(λ/2X)²}

Recalling that the cutoff frequency is Ω=πc/X, and that λ=2πc/ω, we can rewrite this as:

λwg = λ / √{1–(Ω/ω)²}

We see that for ω<Ω, there is no real solution for λwg. Below the cutoff, there is no angle θ at which the sources interfere constructively, as we noted above.

For ω just slightly greater than the cutoff, the equation:

sinθ = ±mλ / 2X

has solutions only for m=1. For higher frequencies, as λ decreases, other radiation modes become possible.

Finally, we see that for ω>Ω, λwg>λ. A longer wavelength at the same frequency corresponds to a greater velocity. This confirms that the phase velocity, the speed of a single-frequency wave, can exceed c. Nonetheless, no real entities, including photons and energy, are ever transported faster than speed c.

## Chapter 25 Review: Key Ideas

• Transmission lines are characterized by two basic equations: ∂V/∂x = – L₀ ∂J/∂t ∂J/∂x = – C₀ ∂V/∂t Here, V is voltage, J is current, and C₀ and L₀ are the capacitance and inductance per unit length. Both V and J satisfy the 1-D wave equation with wave velocity v = 1/√(L₀C₀).

• A coaxial cable, with an inner conductor of radius r and an outer conductor of radius R, and vacuum between the conductors, has v=c and impedance z given by: z = ln(R/r) / (2πε₀c)

The constant 1/(2πε₀c) has a value of 60 ohms, hence almost all coaxial cables have impedances between 50 ohms and a few hundred ohms.

• For a rectangular waveguide of width X and height Y, with X>Y, the lowest mode is: Ey = Ex sin(kx) exp{iωt–ikz} k = π/X ck = ± √ {ω² – Ω²} Here, Ω = πc/X is the cutoff frequency: waves of lower frequency are rapidly attenuated. The “+” sign is for waves moving toward +z, and “–“ is for waves moving toward –z.

The phase velocity, group velocity, and guide wavelength are: vph = ω / kz = c / √ {1 – (Ω/ω)²} vgp = dω/dk = c √[1 – (Ω/ω)²]

λwg = 2πvph /ω = λ₀ / √[1 – (Ω/ω)²]

λ₀ = 2πc/ω is the vacuum wavelength.

The power transmitted through an X-by-Y rectangular waveguide is: power = dU/dt = ε₀ E²max X Y vgp / 4

The oscillatory modes of a waveguide are characterized as either TE or TM. Assume the waveguide’s axis is in the z-direction. In the TE mode, the electric field is entirely transverse within the xy-plane, and the magnetic field has a z-component. In the TM mode, B is entirely transverse within the xy-plane, and E has a z-component.

In rectangular waveguides, the lowest cutoff frequency occurs in the TE mode. Typically, waveguides are used at frequencies just slightly higher than the lowest Ω. This ensures that only the lowest mode propagates through the waveguide, which simplifies its use.

## Chapter

Relativistic Electrodynamics Invariance in Nature & Physical Laws

Throughout the development of physics, our understanding of nature has been advanced by discoveries of invariance: natural properties that remain the same when other conditions change. Physicists have repeatedly reformulated theories and physical laws to better represent newly discovered invariance principles.

A familiar example is rotational invariance: experiments show that nature has no preferred direction. If everything were rotated by any angle about any axis, all natural phenomena would remain the same. Physicists discovered that incorporating rotational invariance into the statement of physical laws is most conveniently achieved by employing vectors. For example: F = qv×B is rotationally invariant. If everything rotates by angle θ about the z-axis, or equivalently if our coordinate system rotates by angle –θ about the z-axis, this law remains valid. It is valid for any angle θ and any axis z.

While mastering vector algebra is initially challenging, it undeniably simplifies physical analysis. Even more importantly, vectors enable a deeper understanding of physical principles. Certainly, we could write the above law as: Fx = q(vyBz – vzBy)

Fy = q(vzBx – vxBz)

Fz = q(vxBy – vyBx)

These three equations yield the correct answer to any problem. However, rotations change the values of nine of these variables (all but q). Furthermore, the single vector equation makes a clearer statement of natural law than do the three component equations.

Using vectors, we have been able to express even more complex relationships in manageable forms. Maxwell’s equations are an excellent example: ∇•E = ρ/ε ∇×E = –∂B/∂t ∇•B = 0 c² ∇×B = j/ε + ∂E/∂t

Reading “a changing magnetic flux through a closed loop drives a circulating electric field around that loop” is much more meaningful than staring at the three equivalent component equations.

You already knew all that. Let’s now turn to two other invariance principles that will lead us to restate the equations of electromagnetism. These principles are relativity and the constancy of the speed of light, the two foundational principles of Einstein’s Special Theory of Relativity. We explored both these principles in detail in Feynman Simplified 1C, chapters 25 through 29.

First espoused by Galileo, the principle of relativity is: absolute velocity is meaningless, only relative velocities have physical consequence. All natural phenomena are the same in any reference frame moving at a constant velocity, regardless of that velocity. Einstein combined relativity with the postulate that the speed of light, in vacuum, has the same value c, in all reference frames, regardless of their velocity. (In special relativity, reference frames must have constant velocity; general relativity removes this requirement.)

Innumerable experiments have confirmed the principles of relativity and the constancy of c to astonishing levels of precision. New tests are continually being performed, both to achieve even greater precision and to extend the range of validated conditions. No principle of science is sacrosanct; all may be questioned thoughtfully, and subject to more stringent testing. Nonetheless, nearly all physicists agree that these two principles are among the most certain concepts of all human knowledge. To correctly represent nature, all physical theories and laws must properly incorporate both principles.

**Four-Vectors** As we discovered in 1C, the principles of relativity and the constancy of c are best incorporated into physical laws by employing 4-vectors in four-dimensional spacetime. For example, the coordinates of an event are represented by the position 4-vector: xμ = (ct, x, y, z). Here, subscript μ is an index that ranges over the values t, x, y, and z, selecting the desired component of the 4-vector x. This is analogous to the subscript j ranging over x, y, and z, selecting the desired component of the 3-vector F.

Another example is the momentum 4-vector, often called the 4-momentum: pμ = (E/c, px, py, pz).

Mastering 4-vectors in 4-D spacetime is also initially challenging. But learning this skill is essential to becoming a successful physicist, and it ultimately simplifies the math and illuminates a deeper understanding of nature. I assume that is your goal; why else would you be reading my book? We will find that everything we learned in 3-vector algebra can be expanded into 4-D spacetime with 4-vector algebra. Adding one more component is a small price to pay to see the universe in its full 4-D glory.

The first question is: What makes a valid 4-vector? What must we add as the fourth component to convert a proper 3-vector into a proper 4-vector? The answer starts with the criterion for a proper 3-vector: rotational invariance. The three components of a proper 3-vector cannot be just any three quantities one might pick. The combination (birthdate, weight, salary) is not a proper 3-vector. An example of a proper 3-vector is r=(x,y,z), the displacement between the origin of a coordinate system and a point P with those coordinate values.

The length of vector r is invariant under coordinate rotation: rotating a coordinate system by angle θ about the z-axis does not change the length of r, for any θ and z. Rotation also does not change the relationship of r to any another proper 3-vector: the angle between any two proper 3-vectors r and s is unchanged by any rotation. What all this ultimately means is It can be shown that a proper 3-vector r transforms into another proper 3-vector r* in a rotated coordinate system according to: r = (x, y, z)

r* = (xcosθ – ysinθ, ycosθ + xsinθ, z)

Note that the rotational transformation has one plus sign and one minus sign. One can apply the same rule to 3-D rotations of any amount in any direction. Since this transformation is linear, any linear sum of proper 3-vectors produces another proper 3-vector.

We can confirm that the rotational transformation does not change vector r’s length, whose square is the scalar product r•r.

r•r = x² + y² + z² r*•r* = x*² + y*² + z*² r*•r* = x²cos²θ – 2xycosθsinθ + y²sin²θ + z² + y²cos²θ + 2xycosθsinθ + x²sin²θ = x²(cos²θ+sin²θ) +y²(cos²θ+sin²θ) +z² r*•r* = x² + y² + z² = r•r

Similarly, proper 4-vectors must transform according to the Lorentz transformation. The Lorentz transformation is identical to the rotational transformation among the three spatial dimensions. With the addition of time as the fourth dimension, the Lorentz transformation adds a new procedure for boosts, transformations of velocity. The boost transformation from a reference frame S to a reference frame S* that is moving at speed v in the +x-direction relative to S, is: x* = γ (x – β ct)

ct* = γ (ct – β x)

y* = y z* = z Here, β=v/c, and γ=1/√(1–β²). One can apply the same rule for a boost of any amount in any direction.

Note that the Lorentz transformation has two minus signs and that time transforms as well as space; these are the essential differences that produce all relativistic effects. Since the Lorentz transformation is linear, any linear sum of proper 4-vectors produces another proper 4-vector.

Since the Lorentz transformation mixes components, the four components of a proper 4-vector must all have the same units: they must all be velocities, or all be distances, or all have the same units of some other type. This requirement was trivial and left unstated in 3-D, because spatial dimensions naturally have the same units. But in 4-D, one component is intrinsically different, hence care is required to ensure it has the same units as the other components. This is why the new component of the position 4-vector is ct and not just t.

Dimensional Analysis & c=1 For brevity, Feynman adopts a standard physics convention that distance and time shall be measured in units that make the speed of light c equal to 1. One can do this by measuring time in seconds and distance in light-seconds (the distance light travels in one second). Astronomers prefer to measure time in years and distances in light-years. Some experimental high-energy physicists measure time in nanoseconds and distance in feet. Either way, c=1.

Feynman adopts c=1 for most of two lectures, but not consistently. For your benefit, I will present the equations with all c’s included. In reading chapters 25 and 26 of Volume 2 of Feynman’s Lectures, you can restore missing c’s in his equations by: replacing each “t” with “ct” replacing each “v” with “v/c” replacing each “E” with “E/c” replacing each “ø” with “ø/c” replacing each “ρ” with “cρ” After that, check the units on both sides of each equation and put in c’s as necessary to dimensionally balance the equation.

Let me demonstrate this with an example: ∇×B = ∂E/∂t (with c=1 and j=0)

Using the replacement list above, the equation becomes: ∇×B = ∂(E/c)/∂(ct)

c² ∇×B = ∂E/∂t The replacements correctly restored the missing c’s. Alternatively, if one forgets the replacement list, one can go directly to balancing units, also called dimensional analysis. From the Lorentz force F=q(E+v×B), we know that the units of E must be the same as the units of vB; let’s write that [E]= [vB]. In dimensional analysis, ∇×B=∂E/∂t becomes: [B] / [x] = [E] / [t]

The units on the left are magnetic field B divided by distance x, because the curl is a spatial derivative with many terms of the form ΔB/Δx. The units on the right are electric field E divided by time t. Substituting [E]=[vB] yields: [B] = [x] [vB] / [t] = [v]² [B]

The units of distance [x] divided by time [t] are the units of velocity [v]. Every valid equation must have the same overall units on both sides. To balance this equation, we must multiply the left side by a velocity squared. Since we left out the c’s, this means the restored equation is: c² ∇×B = ∂E/∂t

Try this on a few equations that you already know. With a little practice, you will find dimensional analysis is easy and highly effective. If you want to be doubly sure, keep all the c’s and do dimensional analysis on your results.

4-Vector Scalar Product The 4-D scalar product has some surprises. Feynman defines the scalar product of two 4-vectors A and B to be: A_µ B^µ = +A_t B_t – A_x B_x – A_y B_y – A_z B_z Here, repeating the µ subscript invokes the Einstein convention, directing us to sum over all four values of the index µ, with the indicated minus signs. Elsewhere Feynman says: “It’s rather awkward to have those minus signs, but that’s the way the world is.”

There are several 对于指标约定、分量顺序和乘积项极性，存在不同的惯例。只要使用者保持一致，任何约定都能得出正确结果。这里我将采用费曼的约定，尽管现代最常见的惯例会反转上述等式右侧的所有符号。（也许是认为一个负号比三个负号更简洁。）

现在考察位置4矢量与自身的标量积；这本质上是对该4矢量进行平方。

x_μ = (ct, x, y, z)

x_μ x^μ = +c²t² – x² – y² – z² 由于上述部分项为负，x_μ x^μ 可能为正、零或负。如果将其解释为长度平方可能会令人不安，因此该标量积通常被称为间隔。

正如任意两个正常的3矢量的标量积是不变的，任意两个正常的4矢量的标量积也是不变的。让我们对位置和动量4矢量都验证这一点。

我们将假定一个静止参考系S和一个沿x轴以速度v运动的参考系S*。y和z分量在各情况下不变，为简洁起见，我将它们简写为[yz]。

x*_μ x*^μ = c²t*² – x*² – y*² – z*² x*_μ x*^μ = γ² (ct–βx)² – γ² (x–βct)² –[yz]

= γ²{c²t²–2βctx+β²x²–x²+2βcxt–β²c²t²}–[yz]

= γ² { c²t²(1–β²) – x²(1–β²)} –[yz]

x*_μ x*^μ = c²t² – x² – y² – z² = x_μ x^μ p_μ = (E/c, p_x, p_y, p_z)

p_μ p^μ = E²/c² – p_x² – p_y² – p_z² p_μ p^μ = E²/c² – p₀² = m²c² p*_μ p*^μ = E*²/c² – p*_x² – p*_y² – p*_z² p*_μ p*^μ = γ²(E/c–βp_x)² – γ²(p_x–βE/c)² –[yz]

= γ²{E²/c² –2βEp_x/c+β²p_x² –p_x²+2βp_xE/c–β²E²/c²} –[yz]

= γ²{E²/c²(1–β²) –p_x²(1–β²)} –[yz]

p*_μ p*^μ = E²/c² – p_x² – p_y² – p_z² p*_μ p*^μ = m²c² = p_μ p^μ 注意一个有用的关系：γ² (1–β²) = 1。

是否存在速度4矢量？是的，但必须小心。在V2p25-2中，费曼指出，不够聪明的人可能会尝试： dx_μ = (cdt, dx, dy, dz)。这是正确的 u_μ = dx_μ/dt = (cdt/dt, dx/dt, dy/dt, dz/dt)

u_μ = (c, v_x, v_y, v_z)。这是错误的问题在于dt不是不变量；它的值在不同参考系中不同。类比来说：(1, v_y/v_x, v_z/v_x) 不是一个正常的3矢量。

费曼给出了正确的方法。从动量4矢量出发。

p_μ = (E/c, p_x, p_y, p_z)

回忆 E = γmc², p = γmv，其中 m 是物体的静止质量。现在将 p_μ 除以不变量标量 m。洛伦兹变换的线性确保了4矢量的任何常数倍数也是4矢量。

u_μ = p_μ / m = (γ c, γ v_x, γ v_y, γ v_z)

我们已经证明了 u_μ 是一个4矢量，我们定义它为4-速度。它与自身的标量积是： u_μ u^μ = γ² (c² –v_x² –v_y² –v_z²)

u_μ u^μ = γ² (c²– v²) = c²

**如何制造反粒子** 你可以在家尝试……如果你有一大片土地（和数十亿美元闲钱的话）。

运用我们关于4矢量的知识，让我们分析产生新粒子的过程。

为了将尽可能多的能量集中在一个微小的、粒子尺度的体积内，物理学家使用蛮力，用可获得的最高能粒子去轰击其他粒子。让我们从最简单的、因此也是最先被进行的过程开始：用高能束流轰击静止靶。

如果束流由质子组成，感兴趣的基本过程是：束流质子-击中-靶质子；以及束流质子-击中-靶中子。让我们关注前者。由于粒子加速器极其昂贵且其成本随束流能量增加，我们特别感兴趣的是计算产生反质子所需的最低束流能量。

我们在两个参考系中考虑质子-质子碰撞：实验室系，其中靶是静止的；以及质心系，其中束流质子和靶质子具有大小相等、方向相反的动量。图26-1展示了实验室系和质心系中碰撞前后的状态。

图26-1 产生两个新粒子这里，黑色圆圈代表质子，空心圆代表反质子。

在《费曼简化版3C》第26章中，我们探讨了基本粒子和支配其相互作用的各种守恒定律。其中一个定律是总净夸克数守恒。就我们此处的目的而言，在适度能量下，夸克守恒的一个后果是（质子总数）减去（反质子总数）永远不变。这意味着要制造一个反质子，我们必须同时制造一个新的质子。我们不能只制造一个新粒子；必须制造成对的粒子。

因此，产生反质子所需的最小束流能量，就是产生一个质子-反质子对所需的最小能量。所以最终态有四个粒子：三个质子和一个反质子，如图26-1所示。

四个粒子所能具有的最小能量是它们的静止质量之和。只有当所有四个粒子静止且具有零动能时，才能达到这个最小值。这只在质心系中才可能发生。

frame, where the total momentum is zero. In any other frame, total momentum is non-zero and at least some particles must have non-zero kinetic energy.

We now employ four conservation laws, one for energy and one each for the three components of momentum. With 4-vectors, these four laws are combined into a single equation: pb_µ + pt_µ = pa_µ Here, pb_µ is the beam 4-momentum before collision, pt_µ is the target 4-momentum before collision, and pa_µ is the 4-momentum of the four-particle state after collision.

In V2p25-5, Feynman stresses that every 4-vector equation is valid in every reference frame, just as the 3-vector equation F=dp/dt is valid in every frame. It is wise to choose frames in which the math is simplest.

Taking the scalar product of each side with itself yields: (pb_µ + pt_µ)(pb_µ + pt_µ) = pa_µ pa_µ pb_µ pb_µ + 2 pt_µ pb_µ + pt_µ pt_µ = pa_µ pa_µ M²c² + 2 pt_µ pb_µ + M²c² = 16 M²c² Here, we used pX_µ pX_µ = mX² c²: the square of any object’s 4-momentum is always equal to the square of its rest mass multiplied by c². Let the proton rest mass be M. Since antiparticles have the same mass as the corresponding particles, the minimum energy of the four particle final state is 4M in the CM frame, if all four are stationary. We therefore have: pt_µ pb_µ = 7 M²c² Now switch to the Lab frame in which: stationary target: pt_µ = (Mc,0,0,0)

beam toward +x: pb_µ = (E/c,p,0,0)

pt_µ pb_µ = EM = 7 M²c² E = 7 Mc² Since E is the beam proton’s total energy, the minimum beam kinetic energy to produce antiprotons is 6 Mc², which is 5.63 GeV. The first particle accelerator capable of producing antiprotons was the Bevatron at the University of California at Berkeley, whose design energy was 6.2 GeV, about 10% more than the minimum energy. (The accelerator got its name because American physicists once denoted billion electron-volts by “BeV” instead of the now standard “GeV”.)

We now turn to a related question: for a proton beam of energy E hitting another proton, what is the maximum energy U available for the production of particles? (Here, “production” includes the two original protons.)

From above, we know that the total 4-momentum before and after the collision is: pb_µ + pt_µ = pa_µ Squaring each side yields: (pb_µ + pt_µ)(pb_µ + pt_µ) = pa_µ pa_µ M²c² + 2 pt_µ pb_µ + M²c² = pa_µ pa_µ The maximum U is attained when the energy used for motion is minimized, which is when all particles are stationary in the CM frame. In that case, the entire CM energy E_cm is available for particle masses, and the right hand side becomes U²/c².

2 pt_µ pb_µ + 2M²c² = U²/c² For a stationary target, we found that pt_µ pb_µ = EM, where E is the beam energy. This means: U = √ { 2Mc² (E+ Mc²) } This is unfortunate. Since costs scale almost linearly with E, a single-beam accelerator that costs 25 times as much delivers only 5 times the available energy.

This is why physicists switched to machines that deliver more bang for the buck. Colliding-beam accelerators produce two beams that circulate in opposite directions and periodically collide head-on. For colliding beams, the Lab frame is the CM frame, and all of the energy of both beams is available to produce particles. Hence: U = 2E A colliding-beam accelerator that costs 25 times as much delivers nearly 25 times the available energy. This is why we now build these much more complex accelerators. One of their many challenges is getting the two beams to actually collide. Aiming a beam at a large, stationary block of matter is trivial compared to aiming it at another beam that is 16 microns (0.0006 inches) wide and moving at virtually the speed of light.

4-D Gradient In three dimensions, we found that the differential operator combination: Ď = (∂/∂x, ∂/∂y, ∂/∂z)

transforms like a proper 3-vector. This is the 3-vector gradient operator. It is most commonly denoted by an inverted Δ, but since that symbol isn’t supported by all eBook formats, I use Ď instead.

We want to find the four-dimensional equivalent of Ď. In V2p25-6, Feynman shows that a seemingly reasonable choice is wrong, and then merely states the right answer. Let’s instead derive the correct 4-gradient.

Clearly the 4-gradient operator will be some combination of ∂/∂t, ∂/∂x, ∂/∂y, and ∂/∂z. By symmetry, the coefficients of the three spatial derivatives must all be the same. We also know that other spacetime 4-vectors often have minus signs in unexpected places. Without loss of generality, we set the coefficient of ∂/∂t to 1/c, and set the spatial coefficients to b, a quantity we seek to determine.

Let’s therefore try the combination: Ď_µ = (c–¹ ∂/∂t, b ∂/∂x, b ∂/∂y, b ∂/∂z)

The 4-gradient must transform like a proper 4-vector. Let’s examine the partial derivatives of a scalar function f in two reference frames: stationary frame S; and frame S* moving toward +x at velocity v.

To reduce clutter, we will ignore the y- and z-derivatives for now.

in S: Δf = ∂f/∂t Δt + ∂f/∂x Δx in S*: Δf = ∂f/∂t* Δt* + ∂f/∂x* Δx* We now use the Lorentz tr Transformation to relate Δt* and Δx* to Δt and Δx.

cΔt* = γ (cΔt – v c–1 Δx)

Δx* = γ (Δx – vΔt)

cΔt = γ (cΔt* + v c–1 Δx*)

Δx = γ (Δx* + vΔt*)

In S*: Δf = γ{ ∂f/∂t* (Δt – v c–2 Δx) + ∂f/∂x* (Δx – vΔt)} We find ∂f/∂t by setting Δx=0 and taking the limit of infinitesimal Δt.

(Δf/Δt) –> ∂f/∂t = γ{ ∂f/∂t* – v ∂f/∂x*} We also find ∂f/∂x by setting Δt=0 and taking the limit of infinitesimal Δx.

(Δf/Δx) –> ∂f/∂x = γ{ ∂f/∂x* – v c–2 ∂f/∂t*} Now, let’s compare these to the results of our trial 4-gradient Ď f and its Lorentz transformed version Ď*f.

Ď = (c–1 ∂/ in which its velocity is zero. The latter is particularly simple. Assume charge q is at rest at the origin of the S* coordinate system. The vector potential is zero for a stationary charge, leaving only the scalar potential, which is: φ* = q / (4πε r*). Here, r* is the distance in S* from the charge to the point P at which the fields are evaluated. The geometry is shown in Figure 26-2.

Figure 26-2 Moving Charge in 2 Frames

We can transform the potentials in S* back to our rest frame S according to: φ/c = γ (φ*/c + 0)

A = γ (0 + v c⁻¹ φ*/c)

A = 0 A = 0 φ = γ q / (4πε r*)

A = v φ / c²

The last remaining task is calculating r* in terms of S coordinates.

r* = √(x*² + y*² + z*²)

r* = √(γ²(x–vt)² + y² + z²)

This matches the result we derived (with much greater pain) using Liénard-Wiechert potentials in Chapter 21.

Maxwell in 2 Equations

In V2p25-10, Feynman says the basic equations of electromagnetism can be reduced to two equations written in 4-D vector algebra. These are: ☐A = j / (c²ε₀)

∂·j = 0

One might quibble, saying that we must include: ∂·A = 0, the Lorentz gauge F = q(E+v×B), the Lorentz force E = –∂φ – ∂A/∂t B = ∂×A Nonetheless, it is impressive how compact these equations have become.

Feynman says: “There, in one tiny space on the page, are all of the Maxwell equations—beautiful and simple. Did we learn anything from writing the equations this way, besides that they are beautiful and simple? In the first place, is it anything different from what we had before when we wrote everything out in all the various components? Can we from this equation deduce something that could not be deduced from the wave equations for the potentials in terms of the charges and currents? The answer is definitely no. The only thing we have been doing is changing the names of things—using a new notation. …What then is the significance of the fact that the equations can be written in this simple form? From the point of view of deducing anything directly, it doesn’t mean anything.”

He adds: “Perhaps, though, the simplicity of the equations means that nature also has a certain simplicity.”

Feynman’s Lectures preceded the now over-worked phrase “Theory of Everything.” But, he often foresaw future scientific and technological developments. Here is Feynman’s Theory of Everything from 1962.

“Let us show you something interesting that we have recently discovered: All of the laws of physics can be contained in one equation. That equation is: U = 0. What a simple equation! Of course, it is necessary to know what the symbol means. U is …the “unworldliness” … Here is how you calculate the unworldliness. You take all of the known physical laws and write them in a special form. For example, suppose you take the law of mechanics, F=ma, and rewrite it as F–ma=0. Then you can call (F–ma)–which should, of course, be zero—the “mismatch” of mechanics. Next, you take the square of this mismatch and call it U.”

He goes on to define U = (∂·E – ρ/ε₀)², etc. Once we have a U for each known equation of physics, we simply add them: U = Σ Uⱼ = 0, total unworldliness is zero.

In V2p25-11, Feynman continues: “So the ‘beautifully simple’ law U=0 is equivalent to the whole series of equations that you originally wrote down. It is therefore absolutely obvious that a simple notation that just hides the complexity in the definitions of symbols is not real simplicity. It is just a trick. The beauty that appears…is no more than a trick. When you unwrap the whole thing, you get back where you were before."

But he says the equations listed at the start of this section do far more than does U=0.

“However, there is more to the simplicity of the laws of electromagnetism written [as 4-vectors]. It means more, just as a theory of vector analysis means more. The fact that the electromagnetic equations can be written in a very particular notation which was designed for the four-dimensional geometry of the Lorentz transformations… It is because the Maxwell equations are invariant under those transformations that they can be written in a beautiful form.

"There is, however, another reason for writing our equations this way. It has been discovered—after Einstein guessed that it might be so—that all of the laws of physics are invariant under the Lorentz transformation. That is the principle of relativity. Therefore, if we invent a notation which shows immediately when a law is written down whether it is invariant or not, we can be sure that in trying to make new theories we will write only equations which are consistent with the principle of relativity.

"The fact that the Maxwell equations are simple in this particular notation is not a miracle, because the notation was invented with them in mind. But the interesting physical thing is that every law of physics—the propagation of meson waves or the behavior of neutrinos in beta decay, and so forth—must have this same invariance under the same transformation. Then when you are moving at a uniform velocity i 在飞船中，所有自然规律一同改变，因此不会出现新现象。正是因为相对性原理是自然界的事实，在四维矢量的记号下，世界的方程才会显得简洁。

**第26章复习：关键要点** • 固有四维矢量根据洛伦兹变换进行变换，这与三维空间旋转的欧几里得变换相同，但增加了对应速度变化的推进。要将四维矢量 C 从参考系 S 变换到相对于 S 以速度 v 沿 +x 方向运动的参考系 S* 中的 C*，推进为： C*_t = γ (C_t – β C_x)

C*_x = γ (C_x – β C_t)

C*_y = C_y C*_z = C_z 其中，β = v/c, γ = 1/√(1–β²), 且 γ²(1–β²) = 1。由于洛伦兹变换是线性的，任何固有四维矢量的线性组合仍产生另一个固有四维矢量。一些四维矢量及其平方是： 四维位置： x_μ = (ct, x, y, z)

x^μ x_μ = c²t² – x² – y² – z² 四维动量： p_μ = (E/c, p_x, p_y, p_z)

p^μ p_μ = E²/c² – p² = m²c² 四维速度： u_μ = (γ c, γ v_x, γ v_y, γ v_z)

u^μ u_μ = c² 四维电流： j_μ = (cρ, j_x, j_y, j_z)

四维势： A_μ = (φ/c, A_x, A_y, A_z)

• 电磁学的四维方程是： ☐ A_μ = j_μ / c²ε₀ ∂^μ j_μ = 0, 电荷守恒 ∂^μ A_μ = 0, 洛伦兹规范 F = q(E+v×B), 洛伦兹力 E = –∇φ – ∂A/∂t B = ∇×A

**三维和四维矢量代数** 矢量三维：A = (A_x, A_y, A_z)

四维：A_μ = (A_t, A_x, A_y, A_z) = (A_t, A)

矢量标积三维：A·B = A_x B_x + A_y B_y + A_z B_z 四维：A^μ B_μ = A_t B_t – A_x B_x – A_y B_y – A_z B_z

微分矢量算符三维：∇ = (∂/∂x, ∂/∂y, ∂/∂z)

四维：∂_μ = (c⁻¹ ∂/∂t, –∂/∂x, –∂/∂y, –∂/∂z)

标量场 f 的梯度三维：∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

四维：∂_μ f = (c⁻¹ ∂f/∂t, –∂f/∂x, –∂f/∂y, –∂f/∂z)

矢量场的散度三维：∇·A = ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z 四维：∂^μ A_μ = c⁻¹ ∂A_t/∂t + ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z

拉普拉斯算符 / 达朗贝尔算符三维：∇·∇ = ∂²/∂x² + ∂²/∂y² + ∂²/∂z² 四维：☐ = ∂^μ ∂_μ = c⁻² ∂²/∂t² – ∂²/∂x² – ∂²/∂y² – ∂²/∂z²

**第27章场的变换** 在第21章和第26章中，我们采用了两种不同的方法来推导运动电荷的电势 φ 和矢势 A。这里我们将用另一种方法来解决同一问题。当你试图解决一个复杂问题时，明智的做法是尝试多种方法。如果你用几种不同的方法得到了相同的结果，你就会对计算结果更有信心。

**恒定速度的电势** 考虑一个电荷从点P以恒定速度v向+x方向运动时，在点F产生的电势，如图27-1所示。

图27-1 点P处电荷在点F产生的场在《费曼物理学讲义》第II卷第26-1节中，费曼说：读者“不应该困惑”于他在这里使用了与先前章节不同的符号。我将努力减少这种混淆。

设点F的坐标为(x, y, z)。在时刻t，电荷q位于点P，坐标为(x–vt, 0, 0)，r是从P指向F的矢量。图27-1还显示了P_ret，即电荷q在推迟时刻t_ret的位置。从P_ret指向F的矢量是r_ret。将前一章的结果适配到这种新的符号下，我们有： φ = γ q / (4πε₀ r)

A_x = v φ / c² A_y = A_z = 0 r = |r| = √[γ²(x–vt)² + y² + z²]

注意，这些方程没有涉及推迟量：r是到F的距离，该距离是从点P——即在评估F点处场的同一时刻t——电荷所在的位置出发的。

我觉得这部分讲座内容相当令人困惑。费曼强调了一个重要观点，然后提出了一个看似合理的论证，最终却表明那个合理的论证是错误的。或许意在作为警示，他给出了以下警告： “每当你看到一个宣称‘极少数假设能推导出极大量结论’的笼统陈述时，你总会发现它是错误的。通常，如果你足够仔细地思考，会发现其中隐含了大量的、远非显而易见的假设。” 我认为这个警告部分恰当。确实，人们应始终意识到任何论断所依据的假设。当然，即使是杰出的科学家也常做出基于隐含且有时不合理的假设的笼统陈述，尤其是在商业媒体为追求轰动性标语而呈现“科学”时。因此，必须记住，陈述从来不是科学的证明；只有对自然的观察才能在科学中提供令人信服的证据。

然而，笼统陈述并非总是错误；其中一些已被观察充分证实，例如能量、动量和电荷守恒。这些应被珍视。为了区分实质内容与浮夸之词，物理学家必须运用他们自己的判断力，这种判断力是随时间发展起来的。物理学上的成功并非易事，不能仅靠机器人般死板地遵循几条简单规则来实现。

让我们现在仔细梳理费曼讲座的这部分，看看有什么值得学习。费曼强调…… 我们推导出的方程，假设电荷速度恒定，依赖于电荷在评估场时的位置，而不是我们经常所说的延迟时间 t_ret。这似乎与所有来自电荷 q 的效应都需要时间到达点 F 的确定事实相矛盾。点 F 在时刻 t 发生的事情怎么可能由点 P 在同一时刻 t 发生的事情决定呢？

这一点在第 21 章中讨论，我们将李纳-维谢尔方程与费曼关于运动电荷场的一般方程进行比较，该方程为：

(4πε) E(R,t) = +q{R/R³ + (R/c) d(R/R³)/dt + d²(R/R)/dt² / c²} B(R,t) = +R×E(R,t) / Rc

这里，R 是我们评估来自电荷 q 的场的位置，该电荷在时间 t_ret（即 q 发射这些场的时间）时位于 (0,0,0)，其中 t_ret = t - r/c。

由于以恒定速度运动的电荷加速度为零，费曼一般方程中的最后一项为零。我们在第 21 章中发现，对于这种情况，中间项恰好校正了延迟，即由于光速有限造成的时间延迟。因此，我们可以去掉中间项，并将 R 替换为 r，即从电荷在时刻 t 的位置到我们在时刻 t 评估场点的向量。

场的延迟是真实存在的，但经实验确认的电磁学方程会自动对其进行校正，只要所有电荷都以恒定速度运动。正如费曼所说，如果电荷具有恒定速度，它在时刻 t 对点 P 的作用完全由它在时刻 t_ret 对点 P 的作用决定。复杂的方程可能会掩盖这一现实，但它仍然是正确的。

一个要点是，更简单的方程在电荷于 t_ret 时刻加速度为零时有效，而那些场稍后会到达点 F 并在 P 点被发射。加速度在 t_ret 之前或之后可能不为零。

以上材料值得学习。

一条应避免的歧途本节描述了费曼在 V2p26-1,2 中讲述的故事，它可能看起来合理，但实际上是错误的。你可能会觉得它既有趣又有警示意义，但跳过本节直接阅读下一节也不会错过任何本质内容。

费曼说，如果我们做出“…假设势仅依赖于延迟时刻的位置和速度…”那么“一个以任何方式运动的电荷的完整势公式”可由以下给出：

φ = γ q / (4πε r)

A = v φ / c² A_y = A_z = 0 r = √{ γ²(x–vt)² + y² + z² }

从运动电荷在时刻 t 找到点 F 处势的方案是：(1) 在 t_ret 时刻找到电荷的位置和速度；(2) 假设电荷速度恒定，找出电荷在时刻 t 的位置；(3) 使用上述方程。

费曼说： “…[知道了]以任何方式运动的电荷的势，我们就有了完整的电动力学；我们可以通过叠加得到任何电荷分布的势。因此，我们可以通过写下麦克斯韦方程组或通过以下一系列评述来概括电动力学的所有现象。（记住它们，以防你被困在荒岛上。通过它们，一切都可以重建。当然，你会知道洛伦兹变换；在荒岛上或任何其他地方你都不会忘记它。）

“首先，A 是一个四维矢量。其次，静止电荷的库仑势是 q/4πε₀r。第三，以任意方式运动的电荷产生的势仅取决于延迟时刻的速度和位置。有了这三个事实，我们就拥有一切…”

然后他解释了这条歧途尽头的陷阱： “有时，一些粗心的人说，整个电动力学可以仅从洛伦兹变换和库仑定律推导出来。当然，这完全错误……场不仅依赖于路径上的位置和速度，还依赖于加速度。因此，在这个‘一切都可以从洛伦兹变换推导出来’的伟大陈述中，有几个额外的隐含假设。”

最后他以我之前引用的警告作结，其要点是：“如果一件事看起来好得难以置信，那它可能就不是真的。”

这个长故事的寓意很简单：不要在速度不恒定时使用恒定速度方程。

恒定速度场存在一些电荷速度恒定的有趣情况，例如在导体中流动的电子，或穿越探测器的高能粒子。在这种情况下，我们可以从恒定速度势中获得电场和磁场。

首先，回忆一下：

∂r⁻¹/∂z = – r⁻² ∂r/∂z ∂r⁻¹/∂z = – r⁻² (1/2) (1/r) (2z)

∂ (1/r) /∂z = – z/r³

我们现在用三维矢量代数计算 E 的三个分量：

E = – Ďφ – ∂A/∂t φ = γ q / (4πε r)

A = v φ / c² A_y = A_z = 0 r = √{ γ²(x–vt)² + y² + z² }

E_z = –∂φ/∂z – ∂A_z/∂t E_z = (γq/4πε₀) (z/r³)

类似地，

E_y = –∂φ/∂y – ∂A_y/∂t E_y = (γq/4πε₀) (y/r³)

x 分量更复杂。

E_x = –∂φ/∂x – ∂A_x/∂t E_x = –(γq/4πε₀) ∂r⁻¹/∂x – vc⁻² ∂φ/∂t We will deal with each term separately.

∂r⁻¹/∂x = (–r⁻²)(1/2r) γ² 2(x–vt) (1)

∂r⁻¹/∂x = –(1/r³) γ² (x–vt)

∂ø/∂t = (γq/4πε) (–1/2r³) γ² 2(x–vt) (–v)

∂ø/∂t = (γq/4πε) (1/r³) γ² v (x–vt)

E = (γq/4πε) {γ² – γ² v²c⁻²} (x–vt) / r³ E = (γq/4πε) (x–vt) / r³ We next calculate the three components of B from: B = ∇×A B_z = ∂A_y/∂x – ∂A_x/∂y B_z = – vc⁻² ∂ø/∂y As we found above, E_y = –∂ø/∂y since A_x=0. Hence: B_z = vc⁻² E_y Similarly, B_y = ∂A_x/∂z – ∂A_z/∂x B_y = vc⁻² ∂ø/∂z = – vc⁻² E_z Finally, B_x = ∂A_z/∂y – ∂A_y/∂z = 0, since A_y=A_z=0.

We can write B in one equation: B = v×E /c².

Now let’s examine the electric field as a whole. Combining the components derived above yields: E = (γq/4πεr³) (x–vt, y, z)

with r = √{ γ²(x–vt)² + y² + z² } Define X=x–vt. The coordinate system Xyz is centered where the charge is at time t. To be clear: q’s position is (x–vt,0,0) in xyz-coordinates, and (0,0,0) in Xyz-coordinates. The E field is: E(t,X,y,z) = (γq/4πεr³) (X, y, z)

E(t,R) = (γq/4πεr³) R with R = (X, y, z) and r = √{ γ²X² +y² +z²} Since E is directly proportional to R, E points radially outward from q everywhere for q>0, and radially inward for q<0. The factor γ² changes the shape of the electric field, making it decrease faster along the X-axis than along the other two axes. This is somewhat like squeezing the pattern of field lines in the direction of motion, as illustrated in Figure 27-2.

Figure 27-2 E from Stationary & Moving Charge In the X=0 plane, the magnitude of the electric field is: E(t,0,y,z) = γ (q/4πε) / (y² + z²)

This is the normal Coulomb field multiplied by γ, which equals 1 for v=0 but becomes enormous as v approaches the speed of light.

Along the X-axis, where y=z=0, the magnitude of the electric field is: E(t,X,0,0) = γ (q/4πε) / (γ² X²)

E(t,X,0,0) = (q/4πε) / (γ X²)

This is the normal Coulomb field divided by γ.

This means, as v approaches c, the electric field is greatly reduced along the direction of motion and greatly enhanced transverse to the motion.

The magnetic field has no X component. It circulates around the X-axis, like the magnetic field from a wire carrying current in the X-direction.

The magnetic field is given by: B = v×E /c² Since E is everywhere parallel to R, the magnetic field along the direction of motion is zero. (By definition, v is also along the direction of motion.)

A Puzzle for You In V2p26-5, Feynman presents a puzzle “for you to worry about.” Two electrons pass one another, moving in orthogonal directions, as shown in the upper half of Figure 27-3. The left electron is moving right with velocity v. The right electron is moving downward with velocity u. At the moment shown, the right electron crosses the left electron’s path, but with enough clearance to avoid a collision.

Figure 27-3 Forces on Passing Electrons Since electrons all have an identical charge q, their electric fields repel one another. The electric forces are horizontal and are labeled F_RH on the right electron and F_LH for the left electron, as shown in the lower half of Figure 27-3.

We previously found that moving charges create no magnetic fields along the direction of motion. This means the right electron experiences no magnetic field from the left electron. However, the left electron does experience a magnetic field and corresponding force from the right electron. That magnetic field is into the screen, leading to a force labeled F_LV that is vertically upward in the lower half of Figure 27-3.

Feynman says: “The electric forces on [the two electrons] are equal and opposite. However, there is a sidewise (magnetic) force on [the left electron] and no sidewise force on [the right electron]. Does action not equal reaction?” Actually, are you sure Feynman’s first statement correct? We just showed that at high velocities the transverse field that the right electron exerts on the left electron is enormously greater than the forward field that left exerts on right. Is Feynman correct that the electric forces are equal and opposite? And, does action equal reaction? You can check your answers in the last section of this chapter.

4-D Generalization of 3-D Curl We now want to derive the transformation rules for electric and magnetic fields. While it is possible to transform the potentials ø and A, and use these to calculate E and B in a moving frame, it is often more convenient to transform the fields directly.

In V2p26-5, Feynman says: “You might think that with every vector there should be something to make it a four-vector, so with E there’s got to be something else we can use for the fourth component. And also for B. But it’s not so. It’s quite different from what you would expect.” Let’s consider the x-component of the equation B=∇×A.

B_x = ∂A_z/∂y – ∂A_y/∂z Feynman says the expression on the right is a “zy-thing”, and labels it F_zy. By extension, for any pair of indices µ and σ that each range over four dimensions, we define: F_µσ = ∂A_µ/∂σ – ∂A_σ/∂µ So, for µ=z and σ=y, we have: F_zy = ∂A_z/∂y – ∂A_y/∂z = Similarly, F = ∂A/∂z – ∂A/∂x = B xz x z y F = ∂A/∂x – ∂A/∂y = B yx y x z

Let’s try a time index, recalling that A=ø/c.

F = c–1 ∂ø/∂z – c–1 ∂A/∂t tz z This would equal E if both terms on the right had minus signs. We can flip one sign by employing the 4-gradient operator Ď , which has opposite signs for the temporal and spatial derivatives. Recall that: Ď = (c–1 ∂/∂t, –∂/∂x, –∂/∂y, –∂/∂z)

Let’s try combinations with Ď: Ď A–Ď A = c–1 ∂A/∂t –(–∂ø/∂z)/c = –E/c t z z t z z Ď A–Ď A = c–1 ∂A/∂t –(–∂ø/∂x)/c = –E/c t x x t x x Ď A–Ď A = c–1 ∂A/∂t –(–∂ø/∂y)/c = –E/c t y y t y y

Going back and checking the combinations with two spatial indices yields: Ď A – Ď A = –∂A/∂z – (–∂A/∂y) = B z y y z y z x Ď A – Ď A = –∂A/∂x – (–∂A/∂z) = B x z z x z x y Ď A – Ď A = –∂A/∂y – (–∂A/∂x) = B y x x y x y z

We therefore redefine F as: µσ F = Ď A – Ď A µσ µ σ σ µ

So far, we have examined only six of the possible 4×4=16 index combinations, but it turns out that six is enough. From the definition of F , it is evident that: µσ F = – F µσ σµ and F = 0 µµ

The first line shows that six other index combinations are redundant, differing only by a sign. The last line shows that four combinations are identically zero. (6+6+4=16, so we are done.)

The F “thing”, is a 4×4 array called the Faraday tensor; it is an antisymmetric, rank two, 4-D µσ tensor. The 3 components of E and the 3 components of B are the 6 independent components of the 4×4 Faraday tensor F .

µσ

The Faraday tensor is shown in its complete form in the Review section at the end of this chapter. We will explore tensors later in this book. For now, the key point is that proper tensors transform according to the Lorentz transformation.

We should think of F as being the 4-D generalization of the 3-D curl.

µσ

3-D Versus 4–D

What a difference an added dimension makes.

In 3-D, the cross product of two 3-vectors is another 3-vector. Examples include the magnetic part of the Lorentz force F=qv×B, and angular momentum L=r×p. In 3-D, if v is along the x-axis and B is along the y-axis, F is compelled to be along the z-axis because that is the only direction orthogonal to both x and y. But this is not true in 4-D: the z- and t-axes are both orthogonal to both x and y; should F be along z or along t?

As Feynman says in V2p26-6, in mechanics the quantity m(xv–yv) has special importance: it is y x universally conserved. We might have named m(xv–yv) the “L ” angular momentum, similar to how y x xy we named F above.

zy

But in 3-D, of the 3×3=9 combinations of L , 3 are zero and 3 others are merely duplicates with the jk opposite polarity. That leaves only 3 truly unique L’s, which just happens to match the number of dimensions. Furthermore, it turns out that the three L’s transform as a proper 3-vector. Feynman says this is “just luck”. This is not true in 4-D. There are 6 independent F ’s in 4-D, and Feynman μσ succinctly says: “you can’t represent six things by four things.” That’s a “sweeping statement” you can take to the bank.

As a side note, in V2p26-8, Feynman congratulates you: “You’ve come a long way. Remember way back when we defined what a velocity meant? Now we are talking about ‘an antisymmetric tensor of the second rank in four dimensions’.”

What a ride! And, we are only halfway through the full course.

Transforming Fields

Now let’s discover how to transform a rank two tensor.

Consider the more general antisymmetric rank two tensor G : μσ G = C D – C D μσ μ σ σ μ where C and D are two arbitrary, proper 4-vectors.

We know how 4-vectors transform, so we can write equations for each of the components of G* , the μσ transform of G to a frame moving along the x-axis with velocity v and β=v/c. We know that C and D μσ transform as: C* = γ (C – β C)

t t x C* = γ (C – β C)

x x t C* = C and C* = C y y z z

Let’s begin with G* .

tx G* = C* D* – C* D* tx t x x t = γ2 (C – β C)(D – β D)

t x x t – γ2 (C – β C)(D – β D)

x t t x = γ2 (CD – βCD –βCD + β2CD)

t x x x t t x t – γ2 (CD – βCD –βCD + β2CD)

x t t t x x t x = γ2 (1–β2) (CD – CD)

t x x t + γ2 β (–CD –CD + CD +CD )

x x t t t t x x G* = CD – CD = G tx t x x t tx

So there is no change in the G component.

tx

The math for the other five components is provided at the end of this chapter.

Several versions of the transformation equations are provided in the Review section. For our present purposes the most convenient is: E* = E p p B* = B p p E* = γ (E + v×B)

t t B* = γ (B – v×E/c2)

t t

Here, E and B are the fields in the rest frame S, and E* and B* are the fields in a frame S* that is moving with velocity v relative to S. Also, the subscript p denotes the field component parallel to v, and the subscript t denotes the transverse field, the vector sum of the components perpendicular to v.

You recall the usual relativistic factor: γ=1/√(1–v2/c2).

Let’s consider a problem using the field transformation equations. Imagine a stationary capacitor with a fixed charge that we pass at a velocity v, moving parallel to its two plates. In the capacito Lab's rest frame S, it has no magnetic field and its electric field is entirely transverse to v; its fields are: B = 0 E = E

In the moving frame S*, the fields are: E* = γ E_t B* = –v γ E_t / c^2 = –v E*_t / c^2

Hence, moving perpendicular to the electric field creates a new transverse magnetic field, and enhances the transverse electric field. (My first edition copy of the Lectures erroneously says the transverse electric field is reduced.)

Now consider a static magnetic field B with no electric field, and imagine we pass it at a velocity v that is orthogonal to B. The fields in S* are: E*_p = B*_p = 0 E*_t = γ v×B B*_t = γ B

The transverse magnetic field is enhanced by γ, and a transverse electric field appears. In principle, this effect enables the measurement of velocities relative to a static magnetic field such as Earth’s field. Unfortunately, the magnitude of this effect is generally only millivolts per meter, much smaller than the naturally occurring variations of Earth’s electric field, which averages about 100 volts per meter.

Equations of Relativistic Motion

With relativistic equations for the electric and magnetic fields, the final step in analyzing their dynamic effect is finding the relativistic 4-D force equation. The Lorentz equation: F = q ( E + v×B )

is valid in 3-D for all velocities, provided we interpret F as dp/dt, the rate of change of momentum, rather than its original interpretation as ma, mass times acceleration. Thus, the universally valid 3-D force equation is: dp/dt = m d(γv)/dt = q ( E + v×B )

We seek a 4-D generalization of this 3-D equation. Since p_μ is a 4-vector with E/c = γmc as its time-component, our task would be easy if dp_μ/dt were a 4-vector with time-component c^{-1}dE/dt = F•v/c. Unfortunately, physics isn’t that easy. Any proper 4-vector divided by an invariant scalar yields another proper 4-vector. But dt is not invariant, since t is different in different inertial frames. We need a relativistically invariant replacement of dt.

In non-relativistic Newtonian mechanics, variables are expressed as functions of time t, such as x(t), and v(t). We track how these variables change as universal time t advances. We need something similar in 4-D: a relativistically universal measure of change.

We find what we need in Feynman Simplified 1C, Chapter 27: the invariant scalar proper time τ. In differential form, it is given by: c^2 dτ^2 = c^2 dt^2 – dx^2 – dy^2 – dz^2

We found in the prior chapter that the right side of this equation is the scalar product dx_μ dx^μ, where dx_μ is the infinitesimal displacement 4-vector (cdt, dx, dy, dz). Being a scalar product, dτ^2 is invariant, the same in every reference frame. We can therefore use proper time τ as a universal standard to measure rate of change.

For an object moving with velocity v: c^2 dτ^2 = dt^2 {c^2 – dx^2/dt^2 – dy^2/dt^2 – dz^2/dt^2} c^2 dτ^2 = dt^2 {c^2 – v_x^2 – v_y^2 – v_z^2} dτ = dt √(1 – v^2/c^2)

dτ = dt / γ γ dτ = dt

Since the Lorentz transformation is linear, the difference between two proper 4-vectors must also be a proper 4-vector. Define the differential change in 4-momentum dp_μ as (p_μ at proper time τ+dτ) minus (p_μ at proper time τ). The 4-vector dp_μ is written: dp_μ = (dE/c, dp_x, dp_y, dp_z)

Dividing any 4-vector C_μ by the invariant scalar dτ produces a proper 4-vector. And, as we take the limit as dτ goes to zero, we obtain the proper 4-D derivative: dC_μ/dτ. For p_μ, this is: d/dτ (p_μ) = (c^{-1} dE/dτ, dp_x/dτ, dp_y/dτ, dp_z/dτ)

dp_μ/dτ = γ (c^{-1} dE/dt, dp_x/dt, dp_y/dt, dp_z/dt)

f_μ = dp_μ/dτ = γ (F•v/c, F_x, F_y, F_z)

Using the relativistic 3-vector F and its components, Feynman defines f_μ as the 4-force, a proper 4-vector that transforms as Lorentz requires.

Any object’s proper time is the time kept by an ideal clock traveling along with that object as it moves with velocity v. In special relativity, v must be constant. In general relativity, v can vary arbitrarily, but the definition of proper time is more complex (the coefficients of dt^2, dx^2, dy^2, and dz^2 are functions of the four coordinates of curved spacetime.)

With the 4-force, we can write relativistic equations in 4-D that generalize their Newtonian equivalents.

p_μ = m u_μ = m dx_μ/dτ f_μ = m d^2x_μ/dτ^2

These relativistic equations are similar in form to Newton’s, but they differ both quantitatively and in their meaning. In V2p26-13, Feynman says: “It is unlike the case of Maxwell’s equations, where we were able to rewrite the equations in the relativistic form without any change in the meaning at all—but with just a change of notation.”

Now, let’s return to the Lorentz force equation and rewrite it in 4-D. Examine the x-component first: f_x = γ F_x = γ q( E_x + v_y B_z – v_z B_y )

We now replace 3-D components with 4-D components using 4-velocity u_μ = γ(c, v_x, v_y, v_z) and the Faraday tensor F_{μσ} shown in the Review section.

f_x = q { (u_t/c) F_{tx} – u_y F_{yx} – u_z F_{zx} }

Since F_{xx} = 0, we can add u_x F_{xx} to the sum in { }’s without changing the equation.

f_x = q { u_σ F_{σx} } Here, we sum over the repeated index σ, per the Einstein convention. By symmetry, we expect the equivalent results for f_y and f_z. Since t is sometimes a bit different from the spatial coordinates of 4-D spacetime, let’s examine f_t according to the 4-force definition.

f_t = γ F•v/c = γ q (E + v×B)•v/c

Since v×B is necessarily orthogonal to v, the B term is zero, which leaves:

f_t = γ q E•v/c

Now evaluate f_t according to our new equation:

f_t = q u^σ F_{tσ} f_t = q γ ( c F_{tt} – v_x F_{tx} – v_y F_{ty} – v_z F_{tz} )

f_t = q γ ( 0 + v_x E_x/c + v_y E_y/c + v_z E_z/c)

f_t = q γ v•E/c

Thus, our new equation gives the correct result for the t-component as well. The equation of motion can be written:

m d^2x/dτ^2 = f_µ = q u^σ F_{µσ}

**Other G* Components**

Here are the calculations for the five other G* components not provided above. Having done G*_{tx}, the next is G*_{ty}.

G*_{ty} = C*_t D*_y – C*_y D*_t = γ(C_t – βC_x)D_y – C_t γ(D_y – βD_t)   [Note: This line likely had a typo in the original; the provided calculation is for G*_{ty} but the terms don't directly match. I have preserved the text as written in the original source.]

= γ(C_t D_y –βC_x D_y –C_t D_y +βC_t D_y)

= γ(C_t D_y –C_t D_y –βC_x D_y +βC_t D_y)

G*_{ty} = γ (G_{ty} – βG_{xy})

G*_{tz} = γ (G_{tz} – βG_{xz}), by symmetry

Next is G*_{xy}.

G*_{xy} = C*_x D*_y – C*_y D*_x = γ(C_x – βC_t)D_y – γC_x(D_y – βD_t)   [Note: This line likely had a typo in the original; the provided calculation is for G*_{xy} but the terms don't directly match. I have preserved the text as written in the original source.]

= γ(C_x D_y –βC_t D_y –C_x D_y +βC_x D_t)

= γ(C_x D_y –C_x D_y –βC_t D_y +βC_x D_t)

G*_{xy} = γ(G_{xy} –βG_{ty})

G*_{xz} = γ(G_{xz} –vG_{tz}), by symmetry

Last is G*_{yz}.

G*_{yz} = C*_y D*_z – C*_z D*_y G*_{yz} = C_y D_z – C_z D_y = G_{yz}

**Answer to Feynman’s Puzzle**

The forces on the particles moving in orthogonal directions are not balanced, the forces of action and reaction between the particles are not equal and opposite, and the sum of their momentum is not conserved.

Before we apply for a Nobel Prize, realize that there is more to the problem than just the particles: there are fields, both electric and magnetic. As we will discover in the next chapter, these fields have both energy and momentum. When a field acts on a charge, that charge reacts on the field. Action and reaction in these interactions are equal and opposite, and total momentum and energy are always conserved.

**Chapter 27 Review: Key Ideas**

• The electric and magnetic fields at (t,R) from a charge q at (t,0,0,0) that is moving at constant velocity v are: E = R ( γq / 4πε r^3)

B = v×E /c^2 with R = (x, y, z) and r = √{ γ^2 x^2 +y^2 +z^2}

• Proper time τ is an invariant scalar; in differential form it is given by: c^2 dτ^2 = c^2 dt^2 – dx^2 – dy^2 – dz^2

We can use τ as a universal standard to measure rate of change. For an object moving with speed v: dτ = dt / γ γ dτ = dt with γ=1/√(1–v^2/c^2)

The proper 4-derivative of C is dC/dτ in the limit as dτ goes to zero. Here, C can be a scalar, 4-vector, or tensor. For p_µ, this is: dp_µ/dτ = γ (c^–1 dE/dt, dp_x/dt, dp_y/dt, dp_z/dt)

f_µ = dp_µ/dτ = m d^2x_µ/dτ^2 = γ (F•v/c, F_x, F_y, F_z)

Here, F is the force 3-vector.

The Lorentz force in 4-D form is: f_µ = q u^σ F_{µσ}

• The Faraday tensor is an antisymmetric rank two tensor; its 16 components are: [The tensor components are likely listed in the original but are missing from this extract. The text continues.]

• The field transformation equations are provided here in three equivalent versions. Here, E and B are the fields in the rest frame S, and E* and B* are the fields in a frame S* that is moving with velocity v relative to S. Also, the subscript p denotes the field component parallel to v, and the subscript t denotes the transverse field, the vector sum of the components perpendicular to v.

Version 1 E*_p = E_p B*_p = B_p E*_t = γ (E_t + v×B_t)

B*_t = γ (B_t – v×E_t/c^2)

Version 2 E*_x = E_x B*_x = B_x E*_y = γ (E_y – vB_z)

E*_z = γ (E_z + vB_y)

B*_y = γ (B_y + vE_z/c^2)

B*_z = γ (B_z – vE_y/c^2)

Version 3 E*_x = E_x B*_x = B_x E*_y = γ (E_y + v×B_y)   [Note: The expression v×B_y is unusual; it likely means (v×B)_y]

E*_z = γ (E_z + v×B_z)

B*_y = γ (B_y – v×E_y/c^2)

B*_z = γ (B_z – v×E_z/c^2)

**Chapter 28** **Energy & Momentum of Fields**

This chapter explores the energy and momentum carried by electric and magnetic fields. In V2p27-1, Feynman begins by examining the interplay of global and local conservation laws and special relativity.

**All Conservation Is Local**

Since we have become quite familiar with the conservation of electric charge, Feynman uses that principle as an example of conservation laws in general.

When we initially said that charge is conserved, we were not precise about where and how conservation occurs.

The least that “charge conservation” can mean is that net charge never changes globally. Global conservation requires only that net charge does not change everywhere, in all space taken as a whole. A global conservation law allows charge to disappear in London if an identical charge simultaneously appears in Edinburgh, or in Auckland, or perhaps in the Andromeda Galaxy. However strange it might seem, two opposite changes, however remote, do mathematically satisfy a global conservation law.

Later, we discovered that the law of conservation of charge requires much more than merely global conservation. It requires charge conservation locally: net charge does not change anywhere, at any single point in space.

We found that the amount of charge ρ within volume V can change only if charge flows into or out of that volume.

Charge is carried by a current j through the boundaries of V. In simpler words: charge can change here only by flowing elsewhere. The local charge conservation law is expressed in a differential equation that is independently valid at every point in space: ∂ρ/∂t + ∇·j = 0 Local charge conservation and current flow are thus intimately interconnected.

Feynman explains why special relativity requires conservation to be local rather than merely global. The key point is relativity’s rejection of universal simultaneity. If a charge disappears in London and another appears in Edinburgh, charge is conserved only if those events are simultaneous. If either preceded the other by time Δt, charge would not be globally conserved during Δt.

But special relativity (see Feynman Simplified 1C, Chapter 27) shows that separated events that are simultaneous in one reference frame are not simultaneous in any other frame moving at a different velocity. The only way that two events can be simultaneous in all reference frames is if the distance between them is zero. This means the only way that charge can be conserved in all reference frames is if charge is conserved locally, at every point in space.

To be universally valid, a conservation law must be local.

We discussed this in terms of charge conservation, but the same logic applies equally to any conservation law.

In particular, energy and momentum must also be conserved locally. Energy can change within some volume V only if some form of energy flows through the surface of V.

When an electron in an atom drops from a higher-energy orbit to a lower-energy orbit, the atom radiates light. To conserve energy, this radiated light must carry away the energy that the electron released. The energy of the light must equal the difference between the electron’s initial and final orbital energies (less a miniscule atomic recoil energy). (I use the word “light” to refer to electromagnetic waves of any frequency, since they are all fundamentally the same phenomenon.)

Since energy and momentum are united as two parts of 4-momentum, if light has energy it must also have momentum. (To be extremely picky, every particle has energy, and has zero momentum in its own rest frame. But there is no reference frame in which light is stationary.)

Energy of Fields We want now to quantitatively analyze the energy of electromagnetic fields in various circumstances. To do this, we need to quantify energy density and energy flow. We define u to be the electromagnetic field energy density per unit volume, and S to be the energy flow vector, the amount of energy per unit time per unit area passing through a surface perpendicular to S.

In V2p27-2, Feynman says: “in perfect analogy with the conservation of charge, we can write the ‘local’ law of [field] energy conservation” as: ∂u/∂t + ∇·S = 0 This equation is valid when the energy of the electromagnetic field is conserved, which it is not in general. Total energy of all types is locally conserved, but energy freely changes from one type to another. Feynman gives the example of walking into a dark room and switching on the lights; field energy suddenly increases, while the energy of the power grid decreases.

We can express this mathematically by defining M to be the energy of matter. We presume here that every entity in nature unambiguously has either non-zero mass (call that matter) or zero mass (call that radiation). At this time, we are not certain about the composition of dark energy and dark matter, but here we will deal only with the less esoteric non-dark forms of energy and matter.

We can generalize the prior equation to include changes in the energy of matter.

∂u/∂t + ∇·S + ∂M/∂t = 0 We now proceed as we did with charge density and current flow. Within a volume V, the total field energy U is the integral over V of energy density u.

U = ∫ u dV We next add the assumption that the only change in the energy of matter within V is due to its interaction with the electromagnetic fields within V. The rate of change of matter energy is power: F·v. If the only forces are due to fields, F must be the Lorentz force: F = q ( E + v×B )

The power expended by fields is: F·v = q E·v This is because (v×C)·v=0, for any vector C. We also know that qv=j, where j is the current density (current per unit volume).

Combining all these equations yields: ∂/∂t { ∫ u dV } + ∫ ∇·S dV + ∫ E·j dV = 0 ∫ { ∂u/∂t + ∇·S + E·j } dV = 0 Since this is true for any volume V, the integrand must be zero at every point in space, which means: ∂u/∂t + ∇·S + E·j = 0 This is called Poynting’s theorem.

All we need now are equations for u and S.

In V2p27-3, Feynman says he could just tell us what those equations are, but he would rather show us the derivations originally done by John Henry Poynting in 1884, “so you can see where [these equations] come from.” It is far better to know why something is true, rather than merely knowing what is true.

The derivations are presented in the last s 本章此节的结果为：

u = ε0 c² {B•B}/2 + ε0 {E•E}/2 S = ε0 c² E×B

其中 u 是场的能量密度，S 是能流密度，也被称为坡印廷矢量。

**场能量与能流密度的模糊性**

在《费曼物理学讲义》第二卷第27-6页，费曼解释道，没有人明确确定场能量的正确方程及其实际位置。广义相对论中的引力波能量也存在同样的问题。费曼说：

“我们想说明，我们并未真正‘证明’关于 u 和 S 的方程。我们所做的只是找到了可能的解。……通过进一步调整这些项，我们可能会找到关于 u 和 S 的另一个公式……但已找到的形式总是涉及场的各种导数（且总是包含二阶项，如二阶导数或一阶导数的平方）。事实上，存在无数种不同的 u 和 S 的可能性，而迄今为止，没有人想到用实验方法来判断哪一个才是正确的！人们猜测最简单的那个可能就是正确的，但我们必须承认，我们并不确定电磁场能量的实际空间位置究竟是什么。

有趣的是，似乎没有唯一的方法来解决场能量位置的不确定性。有时声称，这个问题可以通过使用广义相对论来解决，该理论指出所有能量都是引力吸引的源头。因此，如果我们想了解引力作用的方向，电场能量密度必须被正确定位。然而，迄今为止，没有人进行过如此精密的实验来确定电磁场的引力影响的确切位置。……尽管使用 u 和 S 得出的结果有时看起来很奇怪，但从未有人发现它们有任何错误——即与实验结果没有分歧。所以我们将遵循世界其他人的做法——此外，我们相信它很可能是完全正确的。”

**能流示例**

让我们考察这个新的能流矢量 S，了解它如何运作，以及它与我们已知知识的比较。

第一个例子是光。我们知道光由振荡的电场 E 和振荡的磁场 B 组成，其中 |B|=|E|/c，并且 B、E 和光速三者相互正交。这意味着：

S = ε0 c² E×B S = ε0 c² (E²/c)

S = ε0 c E²，方向沿运动方向

在《费曼简化版1C》第34章中，我们推导了光能流密度的方程，即单位时间通过单位面积的平均能量流。我们发现：

能流密度 = ε0 c <E²>

这里 <E²> 是光电场强度平方的平均值。这与坡印廷矢量相符。它也与能量密度 u 的方程一致。

u = ε0 c² {B•B}/2 + ε0 {E•E}/2

对于光，|B|=|E|/c，这意味着：

u = ε0 c² {E²/c²}/2 + ε0 {E²}/2 u = ε0 E²

由于该能量以速度 c 移动，其能流密度为：

能流密度 = u c = ε0 c E²

再次与坡印廷矢量相符。

接下来，我们考虑一个由频率为 ω 的电流充电的电容器中的能流。我们假设 ω 足够小，以至于电容器的电阻和电感可以忽略不计：R 和 ωL << 1/ωC。图28-1显示了一个圆形平行板电容器其中一块板的俯视图。电场 E 在各处都垂直于屏幕向外。E 在极板之间是均匀的，并与电容器的电荷成正比。八个黑点表示沿极板边缘选定位置处的 E 的方向。

**图28-1 充电电容器俯视图**

不断增大的 E 场在屏幕平面内产生一个逆时针的环形 B 场。极板边缘周围的圆圈代表该半径处的 B 场。一个与 E×B 成正比的坡印廷矢量 S 在八个点上被示出。这种情形是柱对称的，E 和 S 矢量场填充在电容器两极板之间的间隙中。

对于半径为 R、极板间距为 h 的电容器，间隙体积为 πR²h。在某一时刻 t，间隙中的电场能量密度 u(t) 和总电场能量 U(t) 由以下公式给出：

u(t) = {ε0 E(t)²}/2 U(t) = {πR²h} {ε0 E(t)²}/2

能量变化率为：

∂U/∂t = ε0 πR²h E ∂E/∂t

在《费曼物理学讲义》第二卷第27-7页，费曼说：

“因此，必须有能量从某个地方流入这个体积。当然你知道它一定是通过充电导线进来的——完全不是！它无法从那个方向进入极板之间的空间，因为 E 垂直于极板；E×B 必须平行于极板。”

我们可以根据麦克斯韦第四方程计算极板边缘处的 B 场大小 B(R)：

c² ∇×B = ∂E/∂t

B 在极板边缘的环路积分等于 ∂E/∂t 通过所围曲面的通量。

2πR c² B(R) = πR² ∂E/∂t B(R) = (R/(2c²)) ∂E/∂t

由于 S = ε0 c² E×B，

因此，间隙边缘各处坡印廷矢量的大小 S 为：

S = (ε0 R/2) E ∂E/∂t

柱形间隙的侧面积为…… The surface area between the plates at their perimeter is 2πRh. Note we are excluding the area of the plates themselves, since they are perpendicular to S. Since S has the same magnitude across this entire cylindrical surface, that surface area multiplied by S equals the total energy flux entering the capacitor gap through its edges. This is: energy flux = (εR/2) E ∂E/∂t (2πRh) energy flux = (επR²h) E ∂E/∂t This exactly matches ∂U/∂t as calculated above. The Poynting vector analysis says the field energy that builds within the capacitor gap enters that volume through its edges; that energy does not enter the capacitor gap by flowing through the two wires connected to its plates. That does seem odd, since the ultimate power source is a voltage generator connected to the capacitor by these two wires. Feynman says: “…here is one way of thinking about it. Suppose that we had some [opposite charges on opposite sides of] the capacitor and far away. When the charges are far away, there is a weak but enormously spread-out field that surrounds the capacitor. Then, as the charges come together, the field gets stronger nearer to the capacitor. So the field energy which is way out moves toward the capacitor and eventually ends up between the plates.” This is illustrated in Figure 28-2. As distant charges move onto the plates, charging the capacitor, the electric field lines compress, pushing energy into the gap between the plates. Figure 28-2 Charging Capacitor Side View The next Poynting vector example is energy flow in a resistive wire carrying a current j. Electrical energy is dissipated by the resistance and converted into heat. The resistance leads to a voltage drop along the wire with a corresponding electric field parallel to j, as shown in Figure 28-3. The electric field extends beyond the wire, because of the decreasing potential along the wire. Figure 28-3 Fields of Resistive Wire The current also produces a circumferential magnetic field B. The Poynting vector S points inward everywhere, toward the wire’s axis. This means there is a flow of energy from the external fields into the wire, providing the energy that is converted into heat in the resistive wire. In V2p27-8, Feynman says: “So our ‘crazy’ theory says that the electrons are getting their energy to generate heat because of the energy flowing into the wire from the field outside. Intuition would seem to tell us that the electrons get their energy from being pushed along the wire, so the energy should be flowing … along the wire. But the theory says that the electrons are really being pushed by an electric field, which has come from some charges very far away [charges that generate the voltage driving current j], and that the electrons get their energy for generating heat from these fields. The energy somehow flows from the distant charges into a wide area of space and then inward to the wire.” Our final example, which Feynman says should “really convince you that this theory is obviously nuts”, involves a charge attached to a magnet. In Figure 28-4, the central black dot represents a charge q attached to the center of a magnet whose north pole is up and south pole is down. Figure 28-4 Magnet & Charge The charge, magnet, and their fields are all stationary. Yet, E and B are orthogonal along the horizontal midplane, leading to a circumferential energy flow vector S in that plane. The amount of energy remains constant everywhere in this physically static situation, nonetheless the Poynting vector field says energy is continuously flowing in circles, like a game of musical chairs with music that never stops. Can this be real? Feynman points out that a permanent magnet is not as “stationary” as it might appear. Its magnetic field is generated by a permanently circulating current due to eternally spinning electrons. Feynman concludes this Poynting vector discussion saying: “You no doubt begin to get the impression that the Poynting theory at least partially violates your intuition as to where energy is located in an electromagnetic field. You might believe that you must revamp all your intuitions…But [that is] really not necessary. You [won’t] be in great trouble if you forget once in a while that the energy in a wire is flowing into the wire from the outside, rather than along the wire. It seems to be only rarely of value… It is not a vital detail, but it is clear that our ordinary intuitions are quite wrong.” Field Momentum Since electric and magnetic fields have energy, they must also have momentum, because when reference frames change, the Lorentz transformation mixes energy and momentum. We therefore seek an electromagnetic field momentum density g; g(r) equals the 3-vector momentum per unit volume at position r. Conservation of x-momentum within any volume V requires: 0 = ∂/∂t {x-momentum of matter in V} + ∫_V ∂g/∂t dV + ∂/∂t {x-momentum flowing out of V} In V2p27-9, Feynman says there is an important general theorem of mechanics that will help us here.

他说： “当有（任何类型的）能量流动时……单位时间流过单位面积的能量（除以c²）等于单位体积空间中的动量。” 这一普遍定理应用于电磁场能量即为： g = S / c² 费曼随后提供了“一些有趣的例子和论证来说服你这个普遍定理是正确的。” 第一个例子是一个盒子，每单位体积包含N个粒子，都以速度v运动。单位时间内通过垂直于v的面积A的粒子数是NvA（参见第10章，图10-4）。每个粒子的能量等于γmc²，其中m是粒子的静止质量，γ是通常的相对论因子1/√(1–v²/c²)。每个粒子的总动量等于γmv。结合这些，我们得到总能量U和总动量p通过A的速率： 通过A的能量流率 ∂U/∂t = NvA γmc² 通过A的动量流率 ∂p/∂t = NvA γmv 单位面积的能量流率 ∂U/∂t = Nv γmc² 单位体积的动量流率 ∂p/∂t = N γmv 在最后一行，我们除以的体积是vA：v是粒子单位时间行进的距离，乘以粒子通过的垂直于v的面积A。通量比为： (∂U/∂t / 面积) / (∂p/∂t / 体积) = c² 这证实了该定理对于一群速度相同的粒子成立。

接下来考虑光粒子。我们实际上在《费曼简化版1C》第34章中证明了光的这个定理。我们也可以将上面针对有质量粒子的证明加以调整以包括无质量的光子，因为其逻辑与粒子质量无关。我们通过设置v=c并将粒子能量γmc²替换为光子能量ħω来调整。上述方程变为： 通过A的能量流率 ∂U/∂t = NcA ħω 通过A的动量流率 ∂p/∂t = NcA ħω/c 单位面积的能量流率 ∂U/∂t = Nc ħω 单位体积的动量流率 ∂p/∂t = N ħω/c (∂U/∂t / 面积) / (∂p/∂t / 体积) = c² 最后一个例子源自阿尔伯特·爱因斯坦。我将用火箭船取代火车车厢来更新他最初的思想实验。由于这消除了关于摩擦的现实担忧，我相信阿尔伯特会同意的。

图28-5展示了火箭船在三个不同时刻的状态，见于其初始静止参考系。火箭船的货舱长度为y。

图28-5 子弹发射与火箭后坐在上方的图像中，时间t=0时，子弹从货舱后部射出并飞向船首。为了守恒水平动量，火箭船向后反冲，以速度v后退，如中间的图像所示。

在下方的图像中，时间t=T时，子弹到达货舱前部并被墙壁吸收，此时火箭船再次为了守恒动量而停止。在时间T内，火箭船向后移动了距离x=vT。

设子弹的质量为m，火箭船的质量为M（不含子弹）。对于任何具有速度u的有质量物体，其能量U和动量p由下式给出： U = γmc² p = γmu p / U = u / c² p = u (U/c²)

最后一个方程对于有质量的粒子和总是以u=c运动的无质量粒子都成立。为简洁起见，定义µ=U/c²。

从现在开始，我们将对抛体使用p = uµ，并且不对其质量做任何假设。我们假设火箭船的运动是非相对论的（v<<c）。

由于线性动量守恒，当抛体被发射时，我们有： M v = p = u µ 抛体穿过货舱所需的时间为： T = y / u 在时间T内，火箭船向后移动的距离为： x = v T x = (u µ / M) (y / u)

x = y µ / M 由于抛体向右移动了距离y，火箭船向左移动了距离x，因此总系统（抛体加火箭船）的质心向右移动了距离Δ，满足： Δ (M + µ) = µ y – M x Δ (M + µ) = µ y – M (y µ / M)

Δ = 0 这证实了一个力学的一般原理：任何系统的质心不能由内力移动（参见《费曼简化版1D》第39章）。这个原理源于牛顿第三定律，即作用与反作用；在一个孤立系统内，内力相互抵消，对整体系统没有影响。

爱因斯坦将这个公认的力学原理扩展到包括光。爱因斯坦说，如果抛体是能量为ħω=µc²的光子，同样的逻辑也必须适用。那么我们有： M v = ħω / c，以守恒动量 x = v T = v (y/c) = y (µ/M)

Δ (M + µ) = µ y – M (yµ / M) = 0 系统的质心再次保持不变，这是必然的。只有当光具有动量ħω/c时，火箭船才具有正确的反冲速度v。

我们关于电磁动量的最后一个例子也源于爱因斯坦。我们考虑一个盒子，也许是火箭船的货舱，以速度v运动，v远小于c。在时间t=0时，一个光子沿着盒子顶部从点A发射。在时间t=T时，光子在盒子底部的点B被吸收，如图28-6所示。盒子高度为h，质量为M（不含光子）。光子能量为ħω=µc²。

图28-6 光在运动盒子中从A到B的路径在这个思想实验中…… 实验中，爱因斯坦引导我们关注关于点 P 的角动量守恒，点 P 是一个由箭头指示的虚构空间点。点 P 是静止的；它位于盒子的边缘，但不属于盒子。这里感兴趣的角动量是一个垂直于屏幕、若为正则指向观察者的向量。

对于 t < 0，关于点 P 的角动量 L 为： L = Σ r × p = – (h/2)(Mv) – (h)(µv)

（此式适用于 t < 0）

这里，我们假设盒子的质心位于 P 点上方 h/2 处。我们还包含了在 A 点后来发射能量为 E 的光子所必需存在的质能项。在 t=0 之前，该质能以速度 v 与盒子一同运动。根据右手定则，对于任何在 P 点上方并向右运动的东西，r × p 为负。

对于 t > T，关于点 P 的角动量 L 似乎为： L = – hMv/2 – (0)µv ?

（此式适用于 t > T）

角动量似乎不守恒。这是因为质能 µ 从 A 点移动到了 B 点，使其关于点 P 的力臂从 h 减小到零。

爱因斯坦指出，这一分析忽略了角动量的一个重要贡献者：线性动量为 µc 的光子。

从 t=0 到 t=T，光子同时具有垂直和水平速度分量。为简化问题，我们假设光子的水平速度为 v；这使得盒子的水平速度在整个过程中保持为 v。令 u 为光子的垂直速度分量。

在 t=0，光子以向下的速度 u 发射，导致盒子向上反冲动量 uµ。在 A 点的该垂直动量对关于 P 的角动量没有贡献，因为其力臂为零。

但当光子在 B 点被吸收时，它将其动量传递给盒子。其水平分量对 P 的力臂为零，但垂直分量的力臂为 x。如图 28-6 所示，x 是光子在向下移动距离 h 的同时水平移动的距离，这意味着： T = h / u x = T v = (h/u)v

根据爱因斯坦的观点，关于点 P 的真实最终角动量 L 为： L = – hMv/2 – x µ u（适用于 t > T）

L = – hMv/2 – h v µ（适用于 t > T）

这恰好等于 L（t < 0）。这意味着角动量守恒，但前提是爱因斯坦关于光子携带动量的理论正确。

为了简化数学，我设定的点 P 与费曼图 27-8 中的点 P 位置不同。容易证明，如果关于 z=0 平面内某一点的 z 分量角动量守恒，则关于该平面内所有其他点的角动量也守恒。因此，不妨选择使数学计算最简单的点。

为了验证我的主张，比较 xy 平面内两点的 z 方向角动量：Lz₀₀ 关于原点 (0,0)，以及 LzXY 关于点 (X,Y)。

Lz₀₀ = Σ x py – y px LzXY = Σ (x–X) py – Σ (y–Y) px LzXY = Σ (x py – y px) – Σ X py + Σ Y px LzXY = Lz₀₀ – X Σ py + Y Σ px

由于 X 和 Y 是常数，并且线性动量分量 py 和 px 的总和守恒，如果 Lz₀₀ 守恒，则 LzXY 必须守恒。

场能量的坡印廷推导费曼说：我们以后的学习“不需要掌握这个推导”。这其实是“考试不会考”的委婉说法。由于本书没有考试，你或许愿意学习坡印廷关于场能量及其通量的推导。我认为其策略很有趣，数学也相对简单，在费曼量表上仅为 3.6 级。

坡印廷能量守恒定理为： E·j = – ∂u/∂t – ∇·S

策略是将上述方程的左边改写为以下形式： ∂X/∂t + ∇·Y，对于某些 X 和 Y。

我们知道 X = –u 和 Y = –S 是一个解，但可能不是唯一解。

我们首先利用麦克斯韦第四方程替换 j。

j = ε₀c² ∇×B – ε₀ ∂E/∂t E·j = ε₀c² E·(∇×B) – ε₀ E·(∂E/∂t)

E·j = ε₀c² E·(∇×B) – ε₀ ∂/∂t {E·E}/2

现在我们使用矢量代数中的以下恒等式，费曼对其给出了冗长而独特的证明。

E·(∇×B) = ∇·(B×E) + B·(∇×E)

最后一项可以利用麦克斯韦第二方程替换。

∇×E = –∂B/∂t E·(∇×B) = ∇·(B×E) + B·(–∂B/∂t)

E·(∇×B) = ∇·(B×E) – ∂/∂t {B·B}/2

进行此替换后得到： E·j = ε₀c² ∇·(B×E) – ε₀c² ∂/∂t {B·B}/2 – ε₀ ∂/∂t {E·E}/2

回顾坡印廷定理： E·j = – ∂u/∂t – ∇·S

将上述两个方程中的时间导数项和散度项分别等同，可得： u = ε₀c² {B·B}/2 + ε₀ {E·E}/2 S = ε₀c² E×B

在最后一行中，我们交换了 E 和 B 的顺序，并反转了叉积的符号。

## 第 28 章回顾：核心思想

• 守恒律必须是局域的，而不仅仅是全局的，才能普遍有效，狭义相对论证明了这一点。

局域电荷守恒与电流流动密切相关。

• 坡印廷定理描述了电磁场与物质相互作用中的能量守恒： ∂u/∂t + ∇·S + E·j = 0 u = ε₀c² {B·B}/2 + ε₀ {E·E}/2 S = ε₀c² E×B 此处 E 是电场，j 是电流密度，u 是场的能量密度，S 是坡印廷 the field energy per unit time passing through a unit area perpendicular to S.

The electromagnetic field momentum per unit volume is: g = S / c2

## Chapter

Electromagnetic Mass

In 28.1, Feynman begins this final lecture on the fundamentals of electromagnetism with this philosophical summary: "In bringing together relativity and Maxwell's equations, we have finished our main work on the theory of electromagnetism. There are, of course, some details we have skipped over and one large area that we will be concerned with in the future—the interaction of electromagnetic fields with matter. But we want to stop for a moment to show you that this tremendous edifice, which is such a beautiful success in explaining so many phenomena, ultimately falls on its face. When you follow any of our physics too far, you find that it always gets into some kind of trouble. Now we want to discuss a serious trouble—the failure of the classical electromagnetic theory. You can appreciate that there is a failure of all classical physics because of the quantum-mechanical effects. Classical mechanics is a mathematically consistent theory; it just doesn't agree with experience. It is interesting, though, that the classical theory of electromagnetism is an unsatisfactory theory all by itself. There are difficulties associated with the ideas of Maxwell's theory which are not solved by and not directly associated with quantum mechanics. You may say, 'Perhaps there's no use worrying about these difficulties. Since the quantum mechanics is going to change the laws of electrodynamics, we should wait to see what difficulties there are after the modification.' However, when electromagnetism is joined to quantum mechanics, the difficulties remain. So it will not be a waste of our time now to look at what these difficulties are. Also, they are of great historical importance. Furthermore, you may get some feeling of accomplishment from being able to go far enough with the theory to see everything—including all of its troubles."

We now address a fundamental dilemma common to most physical theories: coping with zero. Infinity has been a problem for science from its very beginning.

Zeno concluded that, despite the obvious absurdity, the swift Achilles could never overtake a plodding tortoise with a head start. He reasoned that in the time it took Achilles to get to where the tortoise was initially, the tortoise would have moved slightly further ahead, and by the time Achilles got there, the tortoise would have moved very slightly further ahead, and by … It seemed that Achilles' pursuit would never end.

Eventually, mathematicians learned to sum infinite series of that type, conquering that particular infinity. But, new discoveries often illuminated more infinities lurking in the shadows.

Infinity and zero, the flip side of infinity, still plague science. Many physicists believe that nothing real is ever truly infinite. The flip side may be that nothing real is ever truly zero.

Twenty-five centuries after Zeno, science has yet to completely and effectively cope with zero and infinity, the reciprocals of one another. I wish the next generation of physicists more success.

Field Energy of Point Charge The particular apparition of the zero/infinity monster that Feynman addresses here is the electromagnetic energy of a charge q of zero size, which we shall show is infinite.

Let's calculate the field energy of a stationary sphere (the 2-D surface of a 3-D ball) of radius R and total charge q. A stationary charge produces no magnetic field. At a distance r from its center, the magnitude of the electric field due to charge q is: E(r) = q / (4πε r2)

Its energy density at distance r is: u(r) = ε E2 / 2 The total field energy U is the integral of u(r) from R to infinity. Recall that there is no electric field inside a uniformly charged conductor.

U = (ε/2) ∫_{R}^{∞} E2 4πr2 dr If you know that 4πr2dr, the volume of a shell of radius r and thickness dr, is the proper volume element in polar coordinates, skip down to ENDSKIP. Else, here is the explanation.

The integral over all space in polar coordinates is: ∫∫∫ (stuff) dr (r dθ) (r sinθ dβ)

where θ is the polar angle ranging from 0 to π, and β is the azimuthal angle ranging from 0 to 2π. The reason for the extra factors is that a point at (r,θ,β) moves a distance dr when r changes by dr, moves a distance rdθ when θ changes by dθ, and moves a distance rsinθ dβ when β changes by dβ. The incremental volume is the product of the three incremental distances due to the incremental changes in the three coordinates. This is why these factors appear in the above integral. If (stuff) is not a function of either θ or β, the result of integrating over those angles is: ∫∫∫ (stuff) r2 sinθ dr dθ dβ = ∫∫ (stuff) 2πr2 dr sinθ dθ = ∫ (stuff) 4πr2 dr

## ENDSKIP

Continuing with the integral of u from R to infinity yields: U = (2πε) ∫_{R}^{∞} E2 r2 dr U = (2πε) ∫_{R}^{∞} { q2/(16π2ε2 r4) } r2 dr U = (q2/8πε) ∫_{R}^{∞} r–2 dr U = (q2/8πε)

U = – (q2/8πε) { 0 – R–1 } U = + (q2/8πεR)

Recall that we define: e2 = q2/(4πε), for q being the elementary charge. With that, the prior equation becomes: U = e2 / 2R

I showed every detail of this calculation because the result is dreadful. For point particles, as physicists have long believed electrons are, U is infinite. The classical theory of electromagnetism says the field surrounding a point charge has infinite energy.

In V2p28-2, Feynman says: “What’s wrong with an infinite energy? If the energy can’t get out, but must stay there forever, is there any real difficulty with an infinite energy? Of course, a quantity that comes out infinite may be annoying, but what really matters is only whether there are any observable physical effects. To answer that question, we must turn to something else besides the energy. Suppose we ask how the energy changes when we move the charge. Then, if the changes are infinite, we will be in trouble.”

I disagree with Feynman here. An infinite field energy, even for a stationary electron, is indisputably refuted by innumerable observations and is therefore absolutely wrong. Electrons and antielectrons annihilate one another, leaving behind 1.022 MeV of pure energy and zero electromagnetic field. They are also produced in pairs in the reverse process. If their fields had infinite energy, an infinite amount of energy would disappear from the universe during each pair annihilation, and an infinite amount of energy would appear from nowhere during each pair creation. These processes have been observed for over 60 years. If electrons had infinite field energy, energy would not be conserved.

Field Momentum of Moving Charge In V2p28-2, Feynman calculates the momentum g of the electromagnetic fields of an electron moving with velocity v, assuming v is non-relativistic. With charge q (the electron) at the origin of a polar coordinate system, we consider the fields due to q at a point P with coordinates (r,θ,β), as shown in Figure 29-1. The figure shows the field vectors E, B, and g at P (slightly displaced for clarity).

Figure 29-1 Moving Charge Geometry

To calculate the total field momentum, we will integrate over all space. The first step is to integrate over the azimuthal angle β. Figure 29-1 shows a ring at (r,θ) of cross-section dr by rdθ and radius rsinθ; the ring extends over the full range of β, zero to 2π. Due to symmetry about the horizontal axis, the direction of motion, only gsinθ, the horizontal component of g, contributes to the integral over β; all g components in the vertical plane of the ring sum to zero during integration.

The electric field is radial (inward for a negative charge), and B and g are given by: B = v×E / c2 g = ε E×B g = ε E×(v×E)/c2 g = (ε/c2) E(vEsinθ)

The total field momentum p is: p = ∫ (gsinθ) (dr) (r dθ) (rsinθ dβ)

p = ∫ (vεE2sin2θ/c2) 2πr2 sinθ dθ dr p = (v2πε/c2) ∫ E2r2 sin3θ dθ dr

The θ integral is solved by: ∫0π sin3θ dθ = ∫0π sin2θ (–dcosθ) = ∫0π (1–cos2θ) (–dcosθ) = {–cosθ + (cos3θ)/3} |0π = (1–1/3) – (–1 + 1/3) = 4/3

This leaves: p = (v 8πε /3c2) ∫0R E2r2 dr

We already did this integral for a static charge when we calculated the field energy. We will assume here that v is small enough to use that result here.

p = (v 8πε /3c2) (q2/16π2ε2R)

p = v q2 / (6πεc2 R)

p = 2 v e2 / (3 c2 R)

This doesn’t match the rest frame energy U=e2/2R — the 2/3 factor here should be 1/2. But, that’s not our biggest problem.

A much simpler approach than Feynman employed above is to calculate p with the Lorentz transformation. A charge moving with velocity v in frame S is equivalent to observing a stationary charge in a frame S* that is moving with velocity v. Since p*=0 in the charge’s rest frame, the transformation equation is: p = γ(p* + vE*/c2) = γ v E*/c2

This result is valid for any velocity v. For E* = e2/2R, and v<<c (γ~1), this yields: p = v e2 / (2 c2 R)

Using the Lorentz transformation, we obtain a more satisfying result: the momentum and rest energy imply the same effective mass.

U = e2 / (2R) = melec c2 p = v e2 / (2c2R) = melec v with melec = e2 / (2 c2 R)

Feynman fails to get back to the point he started earlier. He said if an electron’s field energy changes infinitely when it moves that would be real trouble, not just an annoyance. Since the momentum is infinite for R=0, whether we use 2/3 or 1/2, he should acknowledge the theory is unquestionably wrong.

Fifty years ago, Feynman recited a pious hope of his era, saying in V2p28-3: “Where does the mass come from? In our laws of mechanics we have supposed that every object “carries” a thing we call the mass—which also means that it “carries” a momentum proportional to its velocity. Now we discover that it is understandable that a charged particle carries a momentum proportional to its velocity. It might, in fact, be that the mass is just the effect of electrodynamics. The origin of mass has until now been unexplained. We have at last in the theory of electromagnetism a possibility of understanding a part of what mass is.” electrodynamics a grand opportunity to understand something that we never understood before.” Let’s assume for a moment that an electron’s observed mass m is entirely due to its electric field energy. This implies an electron radius R of: R = e2 / mc2 = e2 / (0.511 MeV) R = 2.8 fermi = 2.8×10–13 cm This is called the classical electron radius. In this definition, additional factors of 2/3, 1/2, or 4/5 can be added, depending on the how the charge is distributed — on a shell, throughout a ball, etc. No physicist believes that electrons really have a size even remotely as large as 2.8 fermi; the experimental limit is at least a million times smaller. Our modern understanding is that each elementary particle — including electrons, quarks, photons, and W’s, but excluding protons and neutrons — acquires mass in proportion to the strength of its interaction with Higgs bosons. W’s interact strongly with Higgs and are extremely massive (80.4 GeV), electrons interact only slightly with Higgs and have a tiny mass (0.511 MeV), and photons do not interact at all with Higgs and have zero mass. Protons and neutrons get 1% of their masses from the masses of their constituent quarks; the other 99% comes from quark motion and quark-quark interactions. None of this was known when Feynman gave these Lectures. Tinkering with Wrong Ideas For nine pages starting on V2p28-3, Feynman describes many futile attempts to reconcile particle masses with various versions of electromagnetic theory, including the orthodox classical version, the quantum mechanical version, and many “creative” alternatives. None successfully eliminates infinities or explains particle masses. I can confidently say that none of these failed ideas will be on any exam you will ever take. It might amuse you to see what crazy ideas desperate physicists pursued to solve this problem. But, even if you lived 1000 years, you won’t have enough time to learn all failed crazy ideas of physics-past. Your time would be better spent coming up with your own crazy ideas. Wolfgang Pauli once told a colleague: “Your theory is certainly crazy; the only question is whether it is crazy enough to be true.” I will therefore only highlight a few of the more interesting of these failed theories. In continuing to push the charged-sphere model of electrons, physicists found that an accelerating electron exerts a net force upon itself that resists that acceleration. This means the force required to accelerate an electron is more than would be expected from its rest mass alone. This self-force effectively increases the electron’s inertia. It should be noted that calling it a self-force is a bit misleading: some other entity is responsible for accelerating the electron. In V2p28-6, Feynman provides, without derivation, the form of this self-force: F = α (e2/c2R) ∂2x/∂t2 – (2/3) (e2/c3) ∂x3/∂t3 + β (e2R/c4) ∂x4/∂t4 – … Here α and β are two model-dependent constants of order 1. Only the first term is infinite for R=0, so much effort went into finding ways to get rid of it. For me, the most amusing crazy ideas are due to P. A. M. Dirac, John Archibald Wheeler and Richard P. Feynman, all outstanding theorists. Dirac proposed that charges can act on themselves, but when they do the interaction has equal but opposite contributions from both retarded and advanced waves. We are already familiar with retarded waves: because waves travel at a finite speed c, a field there now depends on what a charge here did earlier. Advanced waves are magic, Einstein might say “spooky”: a field there now depends on what a charge here does later, due to waves traveling at a speed c, but moving backwards in time. This crazy idea eliminates F’s nasty first term. Wheeler and Feynman modified Dirac’s idea. They proposed that each charged particle interacts with other charged particles, but not with itself, and that all electromagnetic interactions have equal contributions from both retarded and advanced waves. The not with itself dictum eliminated infinities by fiat. These ideas solve some problems, but turn out to be incompatible with quantum mechanics, to say nothing of relativity and common sense. QED: Ultimate Electromagnetism Our modern understanding of electromagnetism is based on quantum electrodynamics (QED), which was developed by Feynman, Schwinger, and Tomonaga. These three physicists shared the 1965 Nobel Prize for this achievement. QED incorporates special relativity, Maxwell’s equations, and the particle-exchange force model. The latter states that elementary particles exert forces upon one another through the exchange of other particles, typically bosons. QED eliminates infinities with a sophisticated form of brute force, called renormalization. It states that an electron has an infinitely negative bare mass plus an infinitely positive electromagnetic mass, and that their sum is the observed finite number: 0.511 MeV. I’m not making this up. Feynman has called renormalization a “shell game” and “hocus pocus” 尽管如此，量子电动力学是有效的。实验已经证实了QED的每一个预测，在某些情况下精确得惊人。

**强核力** 从V2p28-12页开始，费曼介绍了1960年代的强核力模型，这种力将原子核束缚在一起并使恒星发光。

在回顾理解强核力过程中的一个重要中间步骤之前，我将总结我们当前的理论：量子色动力学，它是粒子物理学标准模型的一部分。

我们现在相信，质子、中子和其他强相互作用粒子是由夸克组成的。主要的相互作用是夸克之间极其强大的吸引力，无论夸克属于哪种类型。这种相互作用通常被称为强力，它源于夸克与其他夸克交换名为胶子的玻色子。

强力的强度随着夸克分离距离的增加而增大，这不同于任何其他力。当两个夸克被强行拉开到一定距离时，强相互作用力场包含足够的能量转化为新产生的夸克-反夸克对的质量-能量。新的夸克会与现有夸克迅速结合。这实际上使得夸克无法被拉开——当开始将它们拉开时，新的夸克会填补空缺。这就是为什么我们从未观察到孤立的夸克。

我们观察到的核子（质子和中子）之间的吸引力，现在被视为主要相互作用的一个微小残留效应。每个核子内的三个夸克通过交换胶子被极其紧密地束缚在一起。虽然这些胶子主要被限制在一个核子内，但它们的粒子波的一小部分可能会溢出到相邻的核子，并对其内部的夸克施加吸引力。这种弱得多但仍然非常强大的力，通常被称为核力。

回到20世纪60年代初，夸克的存在尚未被普遍接受，费曼本人也不例外。当时的主流理论是汤川模型，该模型认为核子是基本粒子，通过交换介子相互吸引，介子是比电子重但比核子轻的粒子。

在V2p28-12中，费曼说：“由于人类大脑的局限性，我们无法构想出真正全新的东西；所以我们通过与我们所知事物的类比来进行论证。” 汤川提出介子具有一个波方程，与光子有些相似。但由于介子有质量，其波方程为： ∇²φ – μ²φ = 0 其中φ是标量场，μ与介子质量成正比。如果μ为零，这将是真空空间中光子的波方程。

如果我们假设φ不随时间变化，且仅依赖于r，波方程变为： ∇²φ = μ²φ ∂²(rφ)/∂r² = μ²(rφ)

rφ = K exp{±μr} 出于明显的原因，我们舍去正号，得到： φ = (K/r) exp{–μr} 这个势函数比1/r的电势下降得快得多，因为电磁力的交换粒子是无质量的光子（其等价方程中μ=0）。

μ的大小决定了强力的有效范围。最初，汤川估计强力的1费米范围意味着介子质量约为电子质量的200倍。这非常接近μ子的质量，后者是电子质量的209倍。一切看起来都很美好。

但是，1945年由三位迷人的意大利物理学家——马尔切洛·孔韦尔西、埃托雷·潘奇尼和奥雷斯特·皮乔尼（这个名字听起来很熟悉）——进行的实验证明，μ子没有强相互作用，因此不可能是汤川的粒子。

幸运的是，π介子在两年后被发现。π介子有三种电荷状态（+、-和0），质量在电子质量的264到273倍之间。π介子也参与强相互作用。它们的存在证实了汤川的模型，他也因此获得了1949年的诺贝尔奖。

现在，让我们允许φ具有常见的时间依赖性： φ = φ₀ exp{iωt – ikz} 将其代入波方程得到： ω²/c² – k² – μ² = 0 因为U = ħω 且 p = ħk，该方程变为： U² – p² = μ²ħ² m²c² = μ²ħ² m = μħ / c

**第29章回顾：关键思想** 总电荷为q、半径为R的均匀带电球体的电场能量为： U = + (q²/8πεR)

令 e² = q²/(4πε)，且q为元电荷，则上式变为： U = e² / 2R 一个以速度v（v<<c）运动的电荷，其电磁场的动量和等效质量为： p = β v e² / (c² R) = v m_elec m_elec = β e² / (c² R)

其中β取决于电荷的分布，通常是一个接近1的显著分数。

当R趋于零时，场能量和动量都趋于无穷大。这凸显了物理理论面临的一个持久挑战：如何有效地处理无穷大及其倒数零。

**第30章 粒子在场中** 本章探讨自由粒子在电磁场中的运动。具体来说，我们将研究物理学家如何为高能物理实验产生和控制强大的基本粒子束。粒子束是...

collection of free particles in the sense that the particles are not bound to one another.

Motion in a Constant Field

The simplest motions occur in a constant field of only one type: electric or magnetic.

In a constant electric field E, a charge accelerates with a constant force given by: F = q E

At velocities much less than c, this results in a constant acceleration. Feynman invites you to calculate the motion for relativistic velocities. You can compare your answer with mine at the end of the chapter.

In a constant magnetic field B, the force is: F = q v×B

F is always orthogonal to v, therefore the particle’s speed does not change but the direction of its velocity vector does change. A force that is always perpendicular to an object’s direction of motion causes that object to turn in a circle. The force required to keep something turning in a circle of radius R is: F = dp/dt = v* p* / R

Here v* and p* are the components of velocity and momentum within the plane of the circle. In our case, that plane is perpendicular to B. Thus we have: R = v* p* / F R = v* p* / (qv*B)

R = p* / (qB)

This equation has great practical importance. By measuring R for a particle’s trajectory in a known magnetic field, we can precisely determine p*/q. Charge q is typically ±1. Since negative and positive particles bend in opposite directions, the correct charge is generally obvious. The result is a precise measurement of p*, the momentum in the plane perpendicular to B.

A magnetic field B has no impact on a particle’s motion parallel to B, because the parallel component of velocity v does not contribute to F=qv×B. That parallel velocity therefore remains constant. The result is that the particle moves in a helix, as shown in top and side views in Figure 30-1.

Figure 30-1 Helical Motion in B Field

Here, we see the particle rising at one constant speed, while spiraling around the magnetic field at a second constant speed.

Momentum Spectrometer

A magnetic spectrometer uses the motion described above to analyze the momentum of individual charged particles. The spectrometer shown in Figure 30-2 features a large gray region of uniform magnetic field that points out of the screen. Particles enter the port labeled “In” and spiral in the magnetic field.

Figure 30-2 Magnetic Spectrometer

The upper image shows the trajectories of three particles of different momenta. By selecting only particles that enter the counter at 90 degrees, the spectrometer ensures that 2R equals the distance x shown in the figure. Particles hitting the counter have momentum p*=x/(2qB). Particles of lower momentum hit the bottom at smaller x’s and particles of higher momentum at larger x’s.

By moving the counter to different x’s, or by adding other counters at different x’s, the spectrometer determines the flux of particles with various momenta: it measures the momentum spectrum.

It is not essential that spectrometers bend particles 90 degrees, but that angle offers special benefits. As the lower image shows, particles of the same momentum but varying angles arrive at nearly the same x. This increases the counting rate and sensitivity of the spectrometer.

We learned earlier that infinitely long solenoids, hollow cylinders wrapped with current-carrying coils, have uniform internal magnetic fields. For practical devices of finite length, it is necessary to close the ends while maintaining a uniform field.

Figure 30-3 Uniform Field in Elliptical Solenoid

One solution is shown in Figure 30-3. Conducting coils are wound around an elliptical shell. The internal field will be uniform if there are the same number of turns in each vertical band of horizontal width Δx.

Electrostatic Lenses

In virtually all systems employing particle beams, focusing is of paramount importance. In oscilloscopes, analog TVs, and other cathode-ray tubes, an electron beam must come to a sharp focus at a desired point on a screen. In particle accelerators, proton beams must be focused as tightly as possible to increase collision rates.

In Feynman Simplified 1C, we explore optics, including the focusing of light. The concepts, limitations, mathematics, and vocabulary involved in focusing photons, the uncharged particles of light, are quite similar to those used in focusing charged particles.

In particular, the devices that focus charged particles are also called lenses. Charged particle lenses are characterized by focal lengths, magnifications, apertures, and the degree of various aberrations.

Let’s first examine an electrostatic lens. Consider two electrons (shown as solid black lines) that enter at the left of Figure 30-4, and pass through three sets of dark gray parallel plates. The outer plates are set to zero volts, and the inner plates to a positive voltage V. In the upper image, electric field lines are represented by light gray oval curves with arrows.

Figure 30-4 Saturno Electrostatic Lens

The lower image illustrates the focusing effect by zooming in on an electron traversing the plate gap at the lower left. The electron is deflected upward on the left side of the gap and downward on the right side. But, the deflection is larger on the left because it occurs closer to the plates, where the field is stronger.

As electrons traverse the right plate gap, they are closer to the central axis and farther from the plates. The right-gap deflections are smaller than and opposite to the left-gap deflections. But again, the right-gap deflection is greater on its left side than on its right side.

The net effect is to move electrons closer to the central axis and bend their trajectories inward, toward a focal point at the far right.

In V2p29-3, Feynman says: “For distances not too far from the axis, the total impulse through the lens is proportional to the distance from the axis (Can you see why?), and this is just the condition necessary for lens-type focusing.” Magnetic Lenses Magnetic lenses typically provide higher performance than electrostatic lenses, and are used in high-precision devices such as scanning electron microscopes (SEMs). Figure 30-5 shows the optics of a SEM. Electrons are emitted by a source at the top, and collimated by a spray aperture, forming a slowly diverging beam.

Figure 30-5 Saturno Magnetic Lens An electromagnet focuses the electron beam at a point near the bottom of the image.

Details of how this magnetic field focuses electrons are shown in Figure 30-6, an enlargement of the right half of the magnet’s center. We will describe an electron traversing the right side of the magnet; the left side is symmetrically identical.

Figure 30-6 Zoom of Magnetic Lens Magnetic field lines are represented here by dashed lines, and the electron’s trajectory is represented by a solid curve.

As the electron proceeds downward, it passes the magnet’s north poles first and experiences force f pointing out of the screen, as indicated in the figure. That outward motion then leads to another force g pointing to the left, toward the central axis. (Remember that electrons have negative charge.)

As the electron passes the magnet’s south poles, it experiences force f pointing into the screen, and force g pointing to the right, away from the central axis.

The resulting motion is similar to that in the electrostatic lens: the electron is closer to the central axis and is therefore in a weaker field as it passes the south poles. Thus, forces f and g are opposite to but weaker than forces f and g, respectively. The net effect is to move the electron toward the central axis, and bend it toward the focal point.

Microscope Resolution In Feynman Simplified 1C, Chapter 31, we find that diffraction limits the angular resolution of microscopes, telescopes, and all other “optical” systems, regardless of the imaging technology. The Rayleigh criterion for defining angular resolution is: θ ~ λ / W min Here, θ is the angular resolution diffraction limit, λ is the wavelength of the imaging particles, and W is the width of the limiting aperture, which is typically the optical system’s largest element.

For the largest optical telescopes, θ ~ 50 nano-radians (10 milliarcseconds). Radio astronomy is approaching θ = 1 milliarcsecond.

min The somewhat conservative Rayleigh criterion corresponds to the peak intensity of one point’s image aligning with the first null intensity of the image of a slightly displaced point, as shown in Figure 30-7.

Figure 30-7 Rayleigh Limit Here, 2β is the angle subtended by the full aperture, f is the distance from the imaged points to the aperture, and δ is the displacement between the closest points that can be resolved. These quantities are related by: tanβ = (W/2) / f δ = θ f min δ = (λ / W) (W / 2tanβ)

δ = λ / 2tanβ The key point is that resolution is proportional to wavelength λ; shorter wavelengths resolve finer details. For optical light, the resolution limits are typically 500 nm. Because electrons have much shorter wavelengths, modern SEMs can resolve 1 nm with 15 keV electrons.

In V2p29-4, Feynman notes that although 50-keV electrons have wavelengths of 0.005 nm, SEMs cannot reach this diffraction limit due to spherical aberration (see 1C, Chapter 30). He says any SEM with axial symmetry and constant electromagnetic fields has an irreducible spherical aberration that prevents substantially better resolution, even at much shorter electron wavelengths.

Modern atomic force microscopes, based on different imaging technologies, attain resolutions of 0.1 nm, comparable to the size of small atoms.

Particle Accelerators High-energy proton beams are accelerated in nearly circular machines: the older cyclotrons and the newer synchrotrons. As they circle, the beams repeatedly pass through RF electric fields that boost their energy, while magnetic fields control their trajectories. Proton beams circle in a horizontal plane passing through numerous primary magnets that gradually bend the beams around the accelerator, whose circumference can be many miles long.

Cyclotrons use constant ma Magnetic fields, hence the beam's orbital radius grows as its energy increases, and magnet size rapidly becomes a limiting factor. In synchrotrons, magnetic field strength increases as beam energy grows; field strength and beam energy increase synchronously.

Accelerators must overcome the imperfections of the real world: electromagnetic fields are never perfectly uniform, particle energies vary, particle trajectories are not precisely parallel, and identically charged particles repel one another, which tends to blow the beam apart.

Accelerators therefore employ additional magnets for both vertical and radial focusing. Vertical focusing keeps particles from rising far above or dropping far below the desired orbital plane. Radial focusing keeps particles near the desired orbital radius. The tolerance for deviations can be miniscule; the beam width at the LHC's collision points is only 16 microns.

Radial focusing magnets must direct particles inward if they are orbiting at too large a radius, while directing particles outward if they are at too small a radius. As described above, the magnetic field B that holds a particle of momentum p and unit charge in a circular orbit of radius R is: B = p / R. The derivative of this equation with respect to R is: dB/dR = – p / R² = – B / R. This means a field that maintains a constant circular orbit is governed by: (dB/B) / (dR/R) = –1.

For radial focusing, we need to do more than simply maintain a constant orbit. If R is too large, B must be larger than p/R to direct the particle inward. If R is too small, B must be less than p/R to direct the particle outward. Both requirements are met if B varies with R faster than the circular orbit condition. What we need is: dB/dR > – B / R. This can be rewritten as: n = (dB/B) / (dR/R) > –1. Here, n is the field index, also called the relative gradient, of the magnetic field.

Now, let's consider vertical focusing. Figure 30-8 shows a beam's eye view of a vertically focusing magnetic field. The center of the accelerator is far off to the left, and the proton beam (bull's eye symbol) is coming out of the screen. The magnetic field is strongest to the left, and decreases with increasing x, the horizontal coordinate.

Without any currents or electric fields in the empty space between the magnet poles, Maxwell's fourth equation is: ∇×B = 0. The y-component of this equation is: 0 = ∂Bz/∂x – ∂Bx/∂z. Since the field magnitude decreases with increasing x, but its shape stays the same, we know that ∂Bx/∂x is negative. Hence, ∂Bx/∂z must also be negative. Since Bx=0 on the horizontal symmetry axis z=0, this means Bx is negative above z=0 and positive below z=0.

Protons, with v out of the screen in the –y-direction, are deflected downward if they are above z=0 and deflected upward if they are below z=0. This is because for z>0: (v×B)z = – vx Bx = – |vx Bx| < 0, and for z<0: (v×B)z = – vx Bx = + |vx Bx| > 0. For z>0, both vx and Bx are negative. For z<0, vx is negative but Bx is positive.

With a magnetic field that decreases with increasing x, the field index n is negative: n = (dB/B) / (dR/R) = (dB/dR) (R/B) < 0. Therefore, the magnet shown provides both vertical and radial focusing provided that: –1 < n < 0.

Alternate Gradient Focusing

The magnet configuration described above is called weak focusing. Stronger radial focusing requires n>>1, but that causes vertical defocusing. Conversely, stronger vertical focusing requires n<<0, but that causes radial defocusing.

Surprisingly, and in direct violation of Murphy's Law, the combination of two magnetic lenses, one with n>>1 and the other with n<<0, provides both strong radial focusing and strong vertical focusing. Strong focusing was invented by mathematical physicist Ernest Currant and others at Brookhaven National Laboratory in 1952. (I grew up playing with his kids.) The first accelerator employing this principle was Brookhaven's Alternate Gradient Synchrotron (AGS), which was built in 1960 and achieved a beam energy of 33 GeV, a world record at that time.

Strong focusing typically employs quadrupole magnets that have two opposing north poles flanked by two opposing south poles. Quadrupole magnets have the special feature that their field strength varies linearly with the distance from the magnet's center, making them perfect lenses. The field of a quadrupole magnet is shown in Figure 30-9. The image shows the directions of the magnetic field B and Lorentz force F for protons going into the screen. Note that protons above or below the horizontal midline are focused vertically, while protons to the left or right of the vertical midline are defocused horizontally.

This orientation of poles provides vertical focusing. Reversing current flow in the electromagnets exchanges the positions of north and south poles, converting the quadrupole into a horizontal focusing lens. With proper spacing, alternating quadrupole magnets strongly focus the beam both vertically and radially, as illustrated in Figure 30-10.

Figure 30-10 Strong Focusing The upper image shows a beam moving to the right, traversing four quadrupole magnets, whose positions and orientations are indicated. The lower image shows representative beam cross sections on each end of each magnet. The first quadrupole focuses the beam horizontally and defocuses it vertically. The second quadrupole focuses vertically and defocuses horizontally. Each magnet provides stronger focusing than defocusing, because protons are deflected more the farther they are from the central axis.

We see that the beam cross section is progressively reduced after each quadrupole pair. Proper spacing of quadrupole magnets is essential for strong focusing. If the magnets are too far apart, defocused particles are lost before the next magnet can refocus them. If the magnets are too close, particles deflected toward the central axis do not move far enough to be effectively focused.

Motion In Orthogonal Fields In this chapter, we have so far discussed motion in single fields: E without B, or B without E. Another interesting situation is motion in combined E and B fields that are mutually perpendicular.

Figure 30-11 shows a proton moving in orthogonal electric and magnetic fields, assuming the proton’s initial velocity is parallel to E. Note that the entire motion is within a single plane; this is not a helix.

Figure 30-11 Cycloidal Motion In V2p29-8, Feynman says the proton’s motion is a combination of: drifting to the right at constant velocity in the direction of the electric field; and rotating in the plane of the screen perpendicular to B. As we found in other circumstances in Feynman Simplified 1B, Chapter 19, the drift velocity v_drift = E/B. The curved path that results is called a cycloid.

Motion in E Field Feynman suggested you calculate the motion of a charged particle in a constant electric field E, with no magnetic field. For non-relativistic velocities, the particle accelerates at a constant rate in the direction of the force F=qE. For relativistic velocities, the rate of acceleration diminishes as velocity increases. However, we know that the particle’s energy increases by F•x, where x is the distance traversed in the field. Assuming the particle is stationary at x=t=0, we have: (γ–1)m = qEx γ = (qEx/m) + 1 For brevity, define a to be qE/m, the non-relativistic acceleration, and define u=ax+1.

γ2 = 1/(1–v2/c2) = (ax+1)2 1–v2/c2 = u–2 v = c √ {1– u–2} From v = dx/dt, we can calculate the time to reach distance x as follows: t = ∫ (dt/dx) dx = ∫ dx / v ct = ∫ dx / √ {1 – u–2} ct = ∫ (du/a) u / √ {u2 – 1} act = √ {u2 – 1} |ax+1 act = √ {(ax+1)2 – 1} – √(0)

t = (1/ac) √{a2x2 +2ax} t = (x/c) √{1 + 2/ax} For very large x, this reduces to t = x/c. We can invert this equation to obtain x(t).

a2c2t2 = {a2x2 +2ax} a2x2 + 2ax – a2c2t2 = 0 x = {–a ± √(a2 + a4c2t2)}/a2 x = { √(1+a2c2t2) – 1} / a For very large t, this reduces to x = ct.

## Chapter 30 Review: Key Ideas

• A particle with charge q, in a magnetic field without an electric field, orbits in a circle of radius R in the plane perpendicular to B, and moves at constant speed parallel to B. For v* and p* being the components of velocity and momentum within the plane of the circle, radius R is given by: R = p* / (qB)

If B and q are known, measuring R determines p*.

• Electrostatic and magnetostatic lenses focus charged particles with fields that are zero on the symmetry axis and increase linearly with off-axis displacement.

• The Rayleigh criterion for the diffraction limit θ_min of an optical system’s angular resolution is: θ_min ~ λ / W Here, λ is the wavelength of the imaging particles, and W is the width of the limiting aperture. The Rayleigh criterion for the smallest resolvable displacement between two points is: δ = λ / 2tanβ where 2β is the angle at the points subtended by aperture W.

• Dipole magnets can provide both vertical and radial weak focusing of an orbiting particle beam if the field index n is within the following range: –1 < n = (dB/B) / (dR/R) < 0 Properly spaced quadrupole magnets of alternating gradients can provide both vertical and radial strong focusing.

• In constant E and B fields that are mutually orthogonal, a charged particle initially moving along the electric field drifts in that direction at constant speed v_drift = E/B, and rotates in the plane perpendicular to B. The curved path that results is called a cycloid.

## Chapter

Crystals The next 11 chapters explore electromagnetism in dense materials: solids and liquids.

This chapter is devoted to the geometry of crystals, solids with highly ordered structures formed by repeating patterns of atoms.

In V2p30-1, Feynman explains the driving force leading to these orderly structures: “When the atoms of matter are not moving around very much, they get stuck together and arrange themselves in a configuration with as low an energy as possible. If the atoms in a certain place have found a pattern w which seems to be of low energy, then the atoms somewhere else will probably make the same arrangement. For these reasons, we have in a solid material a repetitive pattern of atoms.

Solid bodies often contain atoms of different elements. We will assume each element is uniformly distributed throughout the solid body. The atoms in a solid share their outer electrons with neighboring atoms, thus forming chemical bonds with one another. The arrangement with the lowest energy is the most stable. Higher energy states can drop to lower energy states by releasing energy in the form of heat or light. The higher states are likely to keep dropping to lower and lower states until they hit bottom.

All carbon atoms have the same energy levels, as do all oxygen atoms, and all atoms of all other elements. (There are some very small differences between different isotopes, but those are negligible for our current purposes.) This means the same arrangement of elements has the same energy everywhere throughout the solid. Whatever the lowest energy arrangement is, it is likely to be repeated everywhere.

We define a solid’s unit cell to be the smallest set of repeating atoms. A perfect crystal is a solid that is entirely comprised of myriad copies of one unit cell that are placed side-by-side in three dimensions. Perhaps the simplest example is sodium chloride, table salt.

Here, chlorine atoms (the larger ones) alternate with sodium atoms in each of the three dimensions. In any crystal, there are three axes, not necessarily orthogonal, along which the unit cell repeats. Let’s define a coordinate system along these axes, with (0,0,0) at one corner of a unit cell, and define a, b, and c to be the smallest distances between unit cell repetitions along the three axes. A point at (x,y,z) is indistinguishable from the point at (0,0,0) whenever:

(x,y,z) = (ja, kb, mc)

for any integers j, k, m. It is important to specify that a, b, and c are the smallest repetition distances along each axis, because the crystal also repeats at innumerable other distances, such as 2a, 79a+3b+8c, etc. The repetition distances and the angles between the axes are collectively called the lattice parameters.

Each type of atom bonds more strongly to some types of atoms than others. Also, atoms may bond preferentially in certain directions. As a result, each type of crystal has certain directions in which it is strongest and other directions in which it is most easily cut. The latter directions are called cleavage planes. Since they cut through the same part of each unit cell in their path, cleavage planes are defined by:

(ja, any y, any z)

(any x, kb, any z)

(any x, any y, mc)

Recall that our coordinate system is along the lattice axes, which may not be orthogonal.

Crystal structures can be determined by x-ray diffraction, as discussed in Feynman Simplified 1C, Chapter 33.

Crystal Formation

Crystals form through the deposition of atoms from adjacent liquids or gases. Free atoms continually bounce into other atoms. A typical atom has 10 trillion collisions each second. Occasionally, colliding atoms bind to one another. If the bond is weak, the atoms are easily broken apart by thermal energy.

But occasionally, an atom will land on a partially formed unit cell on the surface of a crystal. If that atom fits the repeating cell pattern, it might enter a low-energy state where it is tightly bound. If conditions are stable and thermal energies are not excessive, the new atom may become attached to that unit cell indefinitely. Crystals grow as new unit cells form on their outer surfaces.

If conditions change rapidly, or if thermal energies are much greater than the unit cell’s binding energy, solids may form that are not crystalline.

Crystal growth rates span an immense range from fractions of a second to millions of years. Crystals may also grow at different rates along each of their three axes.

Chemical Bonds in Crystals

Chemical bonds are often described as being ionic or covalent. In diamond, each carbon atom bonds to four adjacent carbon atoms, and valence electrons are equally shared in covalent bonds. These bonds are typically quite strong. In NaCl, the electronegativity of chlorine is so much greater than that of sodium that the valence electron is almost completely captured by chlorine. The sodium atom effectively has charge +1 and the chlorine atom has charge –1; this is an ionic bond.

Unless the bonding atoms are identical, as in diamond, atomic bonds are never 100% ionic or 100% covalent, but are rather something in between.

A weaker type of bond occurs between neutral molecules. Sugar molecules, for example, have strong internal covalent bonds that fill all valence states. Neighboring sugar molecules bond very weakly by slightly polarizing one another. (See Feynman Simplified 1A, Chapter 9.) Sugar molecules can bond sufficiently to form a molecular crystal, but being weakly bound, these crystals break apart easily. Feynman says an extreme example of a molecular crystal is solid argon. Being a noble gas, argon’s valence states are completely filled. It is very difficult to remove an electron from an argon atom, but conversely, argon atoms have virtually no affinity for adding extra electrons. At sufficiently low temperatures, argon atoms accumulate in closely packed arrays that are very weakly bound.

Metals have yet another type of bonding. Individual atoms release valence electrons that form a negative sea of charge throughout the solid. This negative sea and the positive array of ions attract one another. The bonding is thus better described as array-to-sea rather than atom-to-atom.

Crystal Symmetries in 2-D The mathematics of filling a plane with repeating patterns, such that there are no gaps and no overlaps, is called tiling theory. One should understand tiling theory before cementing ceramic tiles onto a kitchen floor.

Highly ordered structures often have important symmetry properties; crystals are prime examples. Figure 31-3 shows triangular tiles filling a plane without gaps or overlaps. If this were a crystal, atoms would be positioned at each intersection. This 2-D crystal has three lattice parameters: lengths a and b, and the angle between. In this example, a and b have the same length and the angle between them is 60 degrees.

Figure 31-3 Tiling With Triangles Clearly, rotating this crystal by 60 degrees, or any multiple thereof, produces a new crystal indistinguishable from the original. We call this 6-fold symmetry (360º/60º=6): there are six orientations of the crystal that are indistinguishable.

In 2-D, rotating an object by 180 degrees produces its mirror image, which is an inversion relative to a specified plane. If the vertical axis is y, an inversion about y=0 results in flipping the polarity of all y-coordinates. In 3-D, inversions can be relative to a plane or to a single point; in the latter case, all coordinates are flipped relative to the inversion point.

An interesting question is: how many symmetries are possible in 2-D? For rotations, it turns out that the only possible symmetry angles are 60, 90, 120, and 180 degrees, corresponding to 6-fold, 4-fold, 3-fold, and 2-fold symmetry. Let’s see why 5-fold and (6+)-fold symmetries are impossible.

In Figures 31-4 and 31-5, lattice parameters a and b are the shortest repetition distances along the two axes. The horizontal lines are crystal planes with W being their separation.

Figure 31-4 shows a rotation of less than 60 degrees, corresponding to more than 6-fold symmetry. Point B corresponds to rotating point A by angle θ, and point C corresponds to rotating point A by angle 2θ.

Figure 31-4 No Symmetry For θ<60º For the crystal to be symmetric under rotations by angle θ, point C must be at a crystal location equivalent to point B. But for θ<60º, angle β>60º, which means length c is less than b, because: c = W / sinβ b = W / sinθ and sinβ > sinθ for β>θ

But c being less than b contradicts the definition that b is a shortest repetition distance. This excludes symmetries greater than 6-fold.

Figure 31-5 shows a rotation of 72 degrees, corresponding to 5-fold symmetry. Again, point B corresponds to rotating point A by angle θ, and point C corresponds to rotating point A by angle 2θ.

Figure 31-5 No 5-Fold Symmetry For θ=72º, β=180º–2θ=36º. Again length c is less than length b, the shortest repetition length along that axis. This rules out 5-fold symmetry.

In V2p30-6, Feynman says: “…it turns out that for two dimensions 17 distinct patterns are possible. … We will leave you with the game of trying to figure out all of the 17 possible patterns. It is peculiar how few of the 17 possible patterns are used in making wallpaper and fabrics. One always sees the same three or four basic patterns. Is this because of a lack of imagination of designers, or because many of the possible patterns are not pleasing to the eye?”

Crystal Symmetries in 3-D Real crystals are 3-dimensional, of course, so the next question is: how many distinct patterns exist in 3-D? Feynman says the answer is 230, all of which I describe in the following 400 pages. Just kidding.

Crystallographers define 7 major classes of crystal geometries, some with multiple variations. In all, these amount to 14 distinct unit cell shapes. I will show you images of each, and discuss the most important.

Lattice Geometries The simplest unit cell geometry may be hexagonal. Cubic (which comes next) and hexagonal close-packing achieve the highest density for identical round objects, such as atoms. A hexagonal geometry assumes all atoms in the crystal have the same size, and no preferential bonding orientation. Figure 31-6 shows a top view of hexagonally packed white circles representing atoms within a base plane, call that tier 1. Also shown are black circles representing a few atoms on the next higher tier.

r plane, tier 2, and one white circle representing a single atom on tier 3. Figure 31-6 Two Hexagonal Lattices: There are exactly two distinct ways to place the tier 3 atom: at position A shown on the left side, and at position C shown on the right side. At position C, the lattice is cubic, as indicated by the black outline of a tilted cube. At position A, the tier 3 atom is directly above a tier 1 atom, and the lattice is hexagonal.

The next simplest unit cell geometry is cubic, with all side lengths equal and all axes mutually orthogonal. Each unit cell has eight corners, and six faces. For clarity, in Figure 31-7 and the following images, the location of each atom’s center is indicated by a small dot in a nearly empty unit cell. In reality, the atoms are large enough to contact one another and fill most of the unit cell’s volume. Figure 31-7 Three Cubic Lattices: There are three cubic lattice variations that are distinguished by the location of the unit cell’s atoms. These variations and the number of atoms per unit cell (see below) are: simple: 2 atoms/cell, at corners only; body-centered: 3 atoms/cell, at corners & center; face-centered: 5 atoms/cell, at corners & centers of all faces. In counting the number of atoms per unit cell, one must carefully note how many cells share each atom. Consider the face-centered lattice for example: eight corner atoms are each shared by four cells, while six face atoms are each shared by two cells. The correct number of atoms per cell is 8/4 + 6/2 = 5.

Slightly less simple is the tetragonal lattice, with two sides of equal length, and all axes mutually orthogonal. This is shown in Figure 31-8. Figure 31-8 Two Tetragonal Lattices: The two variations are simple (2 atoms/cell) and body-centered (3 atoms/cell).

The next step up in complexity is the orthorhombic lattice. Here, all axes are mutually orthogonal, but all side lengths are different. The four variations are illustrated in Figure 30-9. Figure 31-9 Four Orthorhombic Lattices: From left to right, the variations are: simple, base-centered, body-centered, and face-centered. The numbers of atoms per unit cell are: 2, 3, 3, and 5, respectively. The new type is base-centered, which has one atom at each corner, and one atom at the center of one face. The image shows atoms at the center of the upper and lower faces, but one belongs to another cell.

Next is the rhombohedral lattice, in which none of the axes are orthogonal, but all side lengths are equal. The sole variation is illustrated in Figure 31-10. Figure 31-10 A Rhombohedral Lattice: The rhombohedral lattice contains 2 atoms per unit cell.

Next is the monoclinic lattice shown in Figure 31-11, in which two axes are orthogonal and the sides all have different lengths. Figure 31-11 Two Monoclinic Lattices: The monoclinic lattice has two variations: simple with 2 atoms per unit cell, and base-centered with 3 atoms per unit cell.

Finally, we have the triclinic lattice shown in Figure 31-12. Here, all side lengths are different and no axes are orthogonal. There are 2 atoms per unit cell. Figure 31-12 A Triclinic Lattice.

Metals: The ions in metals are typically arranged in either a cubic or hexagonal lattice for densest packing. In V2p30-8, Feynman says pure metal crystals: “…are, generally speaking, very ‘soft,’ because it is easy to slide one layer of the crystal over the next. You may think: ‘That’s ridiculous; metals are strong.’ Not so, a single crystal of a metal can be distorted very easily.” When a pure metal is subject to a shear force, atoms in two adjacent layers can slip past one another, as shown in the time sequence of images in Figure 31-13. Figure 31-13 Atoms Slipping In Shear: Here, time progresses from the upper image to the lower image. If the shear forces (arrows) are sufficient, atoms in one layer will jump one-by-one to the adjacent unit cell. One can think of this as a hole, or a vacancy, moving through the lattice in the direction of the force. Feynman says: “The slipping goes this way because it takes much less energy to lift one atom at a time over the hump than to lift a whole row. Once the force is enough to start the process, it goes the rest of the way very fast. ‘It turns out that in a real crystal, slipping will occur repeatedly at one plane, then will stop there and start at some other plane. The details of why it starts and stops are quite mysterious. It is, in fact, quite strange that successive regions of slip are often fairly evenly spaced.’” A missing atom, an impurity, or other imperfection inside a crystal may lead to a dislocation, as shown in Figure 31-14. Here, an atom is missing in the third row from the bottom. The lattice is distorted near the dislocation, but eventually restores its normal structure. Figure 31-14 Crystal Dislocation: Dotted lines in the figure show the bending of crystal planes near the dislocation. Dislocations can arise when crystals form, or from impurities, or from cuts or cracks originating at the crystal’s surface.

Ion implantation is a key process in the fabrication of semiconductors. Extremely pure silicon crystals are exposed to energetic ions that embed themselves deep within the crystal. Some implanted ions add negative charge carriers, making n-type regions. Other implanted ions add positive charge carriers, making p-type regions. The combinations create transistors.

Dislocations can propagate through a perfect lattice with very modest resistance. This makes the material soft, pliable, and reduces its mechanical strength.

But much more energy is required to move a dislocation through a grain boundary. Particularly in metals, a solid body is divided into countless grains, volumes much larger than individual unit cells but typically still microscopic. Figure 31-15 is a micrograph of a metal showing several grains and the boundaries between them. The scale bar is 30 microns long, the width of several hundred thousand atoms.

Figure 31-15 Grains & Grain Boundaries

Each grain is a crystal with a nearly perfect lattice. But the lattices in adjacent grains do not fit together. The seam between adjacent grains is called a grain boundary. Macroscopically, the solid is not one large crystal, but rather an amalgamation of many small crystals.

By stopping the propagation of dislocations, grain boundaries make the solid body hard and increase its mechanical strength. In many applications, materials are treated in various ways in order to increase grain number by reducing grain size. This can be achieved by adding impurities, by thermal methods, or by work hardening, such as hammering or bending.

In Vol. 2, page 30-9, Feynman recounts a cute parlor trick: "taking a bar of 'dead soft' copper and gently bending it around someone's wrist as a bracelet. In the process, it becomes work-hardened and cannot easily be unbent again!" (Some physicists will do almost anything to get a date; I’ve had better luck with the Uncertainty Principle.)

Crystal Growth At Dislocations

As mentioned earlier, crystal growth can be very slow. Growth is limited by the rate at which the right type of free atom randomly hits the right crystal site.

Growth is also impeded if the binding energy to that site is small compared to the free atom’s thermal energy. If the free atom happens to complete a unit cell, its binding energy is maximal, ensuring the crystal grows by one atom. But, if the free atom has to start a new unit cell, the binding energy at that site will be much less.

Figure 31-16 shows a crystal surface, with each box representing a completed unit cell. If a free atom lands at point A, its binding energy can only come from bonding to a few atoms on one side of the unit cell below it.

Figure 31-16 Crystal Growth Sites

If a free atom lands at point B, it could bond to atoms on the sides of two unit cells, resulting in more binding energy and greater odds of permanently joining the crystal. But, point C is even more favorable. Here a free atom can bond to atoms of three unit cells, thus increasing its binding energy and enhancing the crystal’s growth rate.

Perhaps surprising, an imperfect crystal can grow faster than a perfect one. Dislocations can enhance the number of sites like point C, and thereby increase a crystal’s growth rate. Consider the screw dislocation shown in Figure 31-17. This imperfection is a misalignment of crystal planes.

Figure 31-17 A Screw Dislocation

Here, the boxes represent complete unit cells. Note that the cells on the lower right surface are one tier lower than the cells on the upper left surface. However, one could still slide smoothly across the surface without having to step up. Starting at the lower right, slide along to the top edge of the image, and then slide over to the left edge. Without stepping up, you have risen one tier.

The exposed step, running from mid-left toward upper-right, provides a more favorable growth site than the surrounding flat surfaces.

Feynman concludes Chapter 30 of his Volume 2 by reproducing a 17-page research paper on the crystalline structure of metals that was published in 1947 by Bragg and Nye. I leave that to experts and future experts of materials science.

## Chapter 31 Review: Key Ideas

• Crystals are solids with highly ordered structures formed by repeating patterns of atoms. The unit cell is the smallest repeating atomic pattern. The six lattice parameters are the three angles between the three axes of the unit cell, and the three shortest repetition distances along those axes.

• Formation and Growth: crystals form through the deposition of atoms from adjacent liquids or gases. Growth rates range from fractions of a second to millions of years, and may differ along each axis. Growth can be accelerated by imperfections that expose more unit cell sides at the crystal surface.

• Symmetry is an important consideration in unit cell geometry and global crystal properties. The number of distinct unit cell patterns is 17 in 2-D, and 230 in 3-D.

Seven unit cell geometries are defined by crystallography.

晶体结构主要有七种类型：

## 1. 六方：简单六方

## 2. 立方：简单立方、体心立方、面心立方

## 3. 四方：简单四方、体心四方

## 4. 正交：简单正交、底心正交、体心正交、面心正交

## 5. 菱方：简单菱方

## 6. 单斜：简单单斜、底心单斜

## 7. 三斜：简单三斜

其中： 简单：每个角上有一个原子体心：简单立方结构加上体心一个原子底心：简单立方结构加上一个面心原子面心：简单立方结构加上每个面的中心各有一个原子。

• 晶体中的位错由缺失原子、杂质、表面机械损伤或其他缺陷引起。位错附近晶格会发生畸变，但最终会恢复正常结构。位错在完美晶体中可以自由传播，但会被晶界阻挡。具有许多晶界的小晶粒会使金属更硬更强。

## 第32章

稠密物质中的折射

在《费曼物理学教程》1C第34章中，我们研究了气体（一种低密度物质状态）的折射率。我们发现，通过气体的电磁波会加速电子，而这些电子会辐射出次级电磁波。主波与次波的干涉是折射现象的基础。通过限定在低密度气体，我们证明了忽略这些受激电子之间的相互作用是合理的。

这里我们去掉低密度的限制，将讨论范围扩展到固体和液体。我们现在准备好探索它们更为复杂的性质。

在V2p32-1中，费曼回顾了早期工作中六个重要的结论，我们将在本章中使用。相关公式、描述以及《费曼物理学教程》的相关章节如下：

阻尼振动：1B第13章 F = m { ∂²x/∂t² + µ ∂x/∂t + ω² x } x = (F/m) / (–ω² + iωµ + ω₀²)

气体折射率：1C第34章 n = 1 + Nq² / {2mε₀ (ω₀² – ω²)}

粒子迁移率：1B第19章 F = m ∂²x/∂t² + µ ∂x/∂t

电导率：1B第19章 µ = τ/m; σ = Nq²τ/m

极化率：2A第10章 ρ_pol = – ∇•P

电介质内的电场：2A第11章 E = E₀ + P / 3ε₀

费曼指出，我们已经掌握了理解稠密物质折射率所需的大部分重要概念。接下来的工作主要是将这些部分整合起来。

原子作为谐振子

在《费曼物理学教程》1C以及本章中，费曼将原子中的电子建模为谐振子。我们假设束缚电子与原子之间的力与电子偏离原子中心的位移成线性正比——就像微小的弹簧一样。

在V2p32-2中，费曼指出：“这不是原子的正确经典模型，但我们将稍后证明，正确的原子量子力学理论在简单情况下会给出与此模型等效的结果。”

在之前的分析中，我们在谐振子模型中没有考虑阻尼力，但这里我们将加入。带阻尼的谐振子力方程为： F = m { ∂²x/∂t² + µ ∂x/∂t + ω² x } 其中，电子质量为m，偏离原子中心的位移为x，固有频率为ω。阻尼力为µm乘以电子的速度。

我们这里采用的方法与1C第34章中的方法有很大不同。在那里，我们考虑入射电场E₀与由入射场激发的电子发射的次级场之间的干涉。而在这里，我们的分析将基于入射电场E₀引起的电介质物质的极化。

我们假设稠密物质是各向同性的，即在所有方向上具有相同的极化率。这意味着电介质的极化强度P与E₀成正比且方向一致。为避免沿多个轴向作用的复杂性，我们假设入射场沿+z方向传播，并在x方向上线性偏振。

在第11章中，我们发现稠密物质内部的电场是外部电场加上该物质极化场的叠加。各向同性电介质内的电场方程为： E = E₀ + P / 3ε₀ 正是这个局域电场驱动着谐振子。这意味着： qE = F = m { ∂²x/∂t² + µ ∂x/∂t + ω² x } 其中q是电子电荷。假设入射电场随时间正弦变化，那么局域电场和振子位移也必须以相同频率正弦变化。因此我们可以写出： E = E₀ exp{iωt} x = x₀ exp{iωt} ∂x/∂t = iωx ∂²x/∂t² = – ω²x

受迫振子方程的解（参见1B第13章）为： x = (q/m) E / (–ω² + iωµ + ω₀²)

我们将位移x视为感应偶极矩p，其表达式为： p = q x p = (q²/m) E / (–ω² + iωµ + ω₀²)

现在定义原子极化率α(ω)为： α(ω) = (q²/mε₀) / (–ω² + iωµ + ω₀²)

偶极矩可以写成： p = α(ω) ε₀ E

以上分析对于具有单一固有频率ω₀的经典谐振子是有效的。但量子力学表明原子具有多个固有振动频率，我们将用下标i来表示。每个固有频率ωᵢ都有一个权重因子fᵢ a damping force μ.

The ω correspond to excitation energies. In the real quantum world, electrons in atoms can have multiple states with different energy levels. The excitation energy ħω equals the difference between the energy of the ith excited state and the ground state, the lowest energy (unexcited) state. Also, f corresponds to the quantum mechanical transition probability between the ground state and excited state i.

We can incorporate these quantum refinements into the equation for α as follows: α(ω) = (q²/mε) Σ f_i /(–ω² +iωμ_i +ω_i²)

The total polarization P of dense matter in field E is: P = Np = α(ω) N ε E Here, N is the number of active electrons (oscillators) per unit volume. Thus the polarization of matter is proportional to E, but with a coefficient that may be complex. This means the polarization may be phase shifted relative to the electric field. At frequencies much higher than the highest natural frequency ω_i, α is inversely proportional to ω², and the polarization decreases rapidly to zero. The polarization will, however, be substantial whenever ω approaches a natural frequency — when ω is nearly equal to ω_i for some i.

Maxwell’s Equation in Dielectrics When matter is polarized, polarization charges and currents arise that must be included to properly solve Maxwell’s equations.

Polarization P is a vector field that like E may be a function of position and time.

Gauss’ law gives the polarization charge (whether or not P varies with time): ρ_pol = – ∇•P The polarization current equals (the number of charges per unit volume) multiplied by the electrons’ charge and velocity. This is: j_pol = N q v = N q ∂x/∂t j_pol = N (∂E/∂t) α(ω) ε j_pol = ∂P/∂t Assuming the only charges and currents that we need to deal with are those within the dense matter, Maxwell’s equations become: ∇•E = – ∇•P / ε ∇×E = – ∂B/∂t ∇•B = 0 c² ∇×B = ∂/∂t (E + P/ε)

Since we have explicitly included the polarization charges and currents, E in the above equations is the incident field.

Note that the mechanism of refraction does not stand out in these equations. We do not see interfering waves with phase shifts leading to an apparent reduction of wave velocity. All these effects are indeed here, but they are hidden within P. We can solve the differential equations without knowing the inner workings of P.

We start, as before, by taking the curl of Maxwell’s second equation: ∇×(∇×E) = – ∂(∇×B)/∂t ∇×(∇×E) = – (1/c²) ∂²(E + P/ε)/∂t² Now use the identity: ∇×(∇×Q) = ∇(∇•Q) – ∇²Q ∇(∇•E) – ∇²E = – (1/c²) ∂²(E + P/ε)/∂t² ∇(–∇•P/ε) – ∇²E = – (1/c²) ∂²(E + P/ε)/∂t² ∇²E – (1/c²) ∂²E/∂t² = – ∇(∇•P/ε) (1/εc²) ∂²P/∂t² The usual wave equation has zero on the right side in place of the two polarization terms. But, since P is a function of E, wave solutions are still possible.

With the incident wave moving in the +z-direction, let’s try a solution of the form: E_local = E_0 exp{iωt – ikz} This represents a wave moving with phase velocity ω/k.

If you remember why ω/k is the phase velocity, you might wish to skip down to ENDSKIP. Else, here is a reminder.

Recall that a wave moving at velocity v is represented by a function of the form: f(z–vt). To confirm this claim, compare f(z,t) to f(z+Δz,t+Δt): f( [z+Δz] – v [t+Δt] ) = f( z–vt + {Δz–vΔt} )

If Δz=vΔt, the term in { }’s is always zero. This means the function f always moves a distance Δz=vΔt during a time interval Δt. That is the definition of velocity v.

Here, the wave is of the form f( z – [ω/k] t), so v=ω/k.

We call this a phase velocity because it is the velocity of a wave comprised of only one frequency. A wave packet, a superposition of waves of different frequencies, moves at the group velocity dω/dk.

## ENDSKIP

We can now calculate the index of refraction n, defined by: v_ph = ω / k = c / n k = ω n / c Making this substitution changes the equation for E to: E_local = E_0 exp{iω (t – zn/c) } This equation represents a plane wave; it varies with time t and position z, but not with x or y. For each value of z, E has the same value everywhere in the xy-plane, and so does P, since P is a function of E.

This means ∇•P = ∂P/∂x = 0. This simplifies the wave equation to: ∇²E – (1/c²) ∂²E/∂t² = (1/εc²) ∂²P/∂t² ∂²E/∂z² – (1/c²) ∂²E/∂t² = (1/εc²) ∂²P/∂t² (– ω² n²/c² + ω²/c²) E = – ω² (1/εc²) P n² – 1 = (1/ε) P / E Now we must relate P and the incident field E. Recall two prior equations: E_local = E_x + P / 3ε P = α N ε E_local Combining these yields: P = α N ε (E_x + P / 3ε)

P – α N P / 3 = α N ε E_x P / E_x = α N ε / (1 – αN/3)

Putting this expression for P into the equation for n, yields: n² – 1 = (1/ε) α N ε / (1 – αN/3)

n² = 1 + α N / (1 – αN/3)

Let’s compare this to the result we obtained in Feynman Simplified 1C, Chapter 34, for a low-density gas.

gas: n = 1+ Nq² / {2mε(ω_i² – ω²)} For αN << 1, our current result simplifies to: n² = 1 + α N Now use the approximation (1+δ/2)²=1+δ, for δ<<1.

n = 1 + α N/2 α(ω) = (q²/mε)

Σ f_i /(–ω_i^2 + iωμ_i + ω_{0i}^2)

If we make the same simplifications here that we employed for gases — only one natural frequency and zero damping — our new equation matches the equation for gases.

Let’s now rewrite our new equation as follows: n^2 – 1 = α N / (1 – αN/3)

(n^2 – 1) (1 – αN/3) = αN (n^2 – 1) – (n^2 – 1) αN/3 = αN (n^2 – 1) = αN/3 ( 3 + n^2 – 1)

3 (n^2 – 1) / (n^2 + 2) = αN

In this form, this is the Clausius-Mossotti equation. With the equation for α, this becomes: 3(n^2–1)/(n^2+2) = αN = N (q^2/mε) Σ f_i /(–ω_i^2 + iωμ_i + ω_{0i}^2)

Feynman notes that atoms in solids and liquids interact strongly with their neighbors. One consequence is that the natural frequencies of atoms in dense matter may be quite different from those of isolated atoms of the same type. Additionally, many solids and liquids contain atoms of different types, each with their own natural frequency spectrum. Our equation can accommodate this complexity by including all elements in the summation and appropriately choosing N and the f’s.

Complex Index of Refraction Since α contains an imaginary term in its denominator, index n is typically a complex number. We can better understand the consequences by separating index n into real and imaginary parts. Note that: 1/(a+ib) = {1/(a+ib)} {(a–ib)/(a–ib)} 1/(a+ib) = (a–ib) / (a^2+b^2)

For a single natural frequency and very low density, index n would be: n = 1 + N(q^2/mε)/(–ω^2 + iωμ + ω_0^2)

n = 1 + N(q^2/mε) × (–ω^2 – iωμ + ω_0^2) / {(ω^2–ω_0^2)^2 + ω^2μ^2}

In normal circumstances the damping coefficient μ is positive. This equation shows that for μ>0, the imaginary part of n is negative. For multiple natural frequencies and high density, the math is much messier, but the idea is the same. Let n = n_r – in_i. Both n_r and n_i are positive and are functions of frequency ω.

We can now rewrite the prior equation for E using two exponentials, one real and one imaginary.

E = E_0 exp{iω(t – zn_r/c)} E = E_0 exp{iω(t – zn_r/c)} exp{–zn_iω/c)}

This represents an oscillating wave traveling at velocity c/n_r with exponentially decreasing amplitude. Since n_r is the factor by which the phase velocity is reduced, it corresponds to our normal definition of the refractive index. For proper normalization, let the dense matter begin at z=0 and extend through z=L, with L>0. Wave intensity I is the square of wave amplitude, so it decreases according to: Intensity I ~ exp{–βz}, for β = 2n_i ω/c Here β is called the absorption coefficient.

Figure 32-1 graphs I at t=0 versus distance z into the material.

Figure 32-1 Intensity vs. Distance into Matter This is the familiar behavior of damped oscillators. For larger β, the electromagnetic wave is absorbed more rapidly. Opaque materials thus have large β’s, while transparent materials have small β’s.

Index of Mixtures For solids or liquids with admixtures of different atoms or molecules, we can separate the refractive index equation as follows: 3(n^2–1)/(n^2+2) = Σ α_k N_k

Clearly, the index of a mixture is rather different from the sum of the indices of each constituent. Our analysis makes the claim that the quantity on the left side above equals the linear sum of the α_k N_k quantities on the right side. This prediction can be tested using real data. A good theorist always tries to put the predictions of their theories to the ultimate test: reality.

Feynman compares the predictions of the calculated refractive index with data from the Handbook of Chemistry and Physics. He doesn’t give a precise reference, but the numbers he quotes are consistent with those in my 1960-1961 Handbook, pages 2946-7 for sugar solutions at 20ºC. (I’d like to say I inherited that book, but the truth is that I actually am old enough to have bought that edition when it was new.)

The Handbook lists the refractive index of 851 different sugar solutions. Thankfully, Feynman tabulates data for only 5. Below is a simplified version of the rather confusing Table 32-2.

Each row contains values for one sugar solution. The left most column is the percentage of sugar. The column labeled “Sug” lists N_s/N_0, the number of sugar molecules per liter N_s, divided by Avogadro’s number N_0. The “Wat” column lists N_w /N_0, the number of water molecules per liter N_w, divided by N_0. The “Meas” column lists the value of αN_mix =3(n^2–1)/(n^2+2) for the measured value of n. The right most column, labeled “Calc”, is Feynman’s calculated value of αN_mix, based on some assumptions.

Feynman assumes the natural frequencies of sugar and water are the same for all sugar concentrations. Indeed, Feynman says he chose sugar (sucrose C_12H_22O_11) because it dissolves in water without changing chemically. He assumes water’s value of αN is 0.617, the measured value of the 0% sugar solution (how could it be anything else?). He also assumes sugar’s value of αN_s is the measured value for a pure sugar crystal, which is listed in the table as the 100% sugar solution. The calculated αN for each mixture is given by the sum of the water water and sugar contributions for each mix concentration, which are: water: (0.617 / 55.5) (N_w / N_0)

sugar: (0.960 / 4.64) (N_s / N_0)

Since we used the data for the 0% and 100% sugar solutions as the basis of our calculation, we cannot take credit for properly calculating those two values. The three other calculated values differ from the measured values by an average of 1%, so we might claim our analysis is 99% correct. Feynman does the comparison differently, and gets similar agreement. When comparing measurements to calculations, I prefer to convert the calculations to the same form as the measured data. One can parameterize a theory many different ways, but data reveals nature’s intent.

Waves in Metals

Can one really speak meaningfully about the refractive index of a metal that is opaque to light? Surprisingly, the answer is: Yes.

In metals, atoms contribute valence electrons that roam freely throughout the bulk of the solid, while the inner electrons are tightly bound to their atoms. The analysis we completed above can be applied to both free and bound electrons, but the free electrons contribute almost all of a metal’s refractive index.

Hence, we can simplify the analysis for metals by dealing only with the free electrons, those responsible for current flow. The number of active electrons per unit volume, N, now refers to free electrons only. We also no longer need to address mixtures of different types of atoms, since free electrons in a metal are all in the same environment, regardless of which atoms they originated in. Additionally, free electrons are not bound to specific sites. This means their restoring force is essentially zero. We can therefore eliminate ω_0, ω_i, and f_i from our calculations. Free electrons do however encounter some resistance, so we must maintain the iωµ term.

There is one other difference between metals and dielectrics. Metals do not polarize as dielectrics do. We therefore set P=0.

This reduces the refractive index equation for a metal to: n^2 = 1 + (N q^2 / mε) / (–ω^2 + iωµ)

We can even calculate µ. In Feynman Simplified 1B, Chapter 19, we explore electrical conductance. Free electrons in metals are subject to acceleration by applied voltages and also to collisions with metallic ions. Free electrons scatter in random directions after each collision, but are always accelerating toward the positive potential. We found that these combined effects result in an average drift velocity given by: v_drift = (qE/m) τ

Here, τ is the mean time between collisions, E is the electric field within the metal, and q and m are the electron’s charge and mass. This equation has a simple interpretation: immediately after each collision, the electron’s average velocity toward the positive potential is zero; during time τ, its acceleration is (qE/m), resulting in the velocity v_drift. To get the correct coefficient, one must average over the exponential distribution of τ.

Thus, due to continual collisions, free electrons, on average, drift at a constant velocity rather than accelerate. The driving force qE is therefore the drag force, which we define to be µmv. This means: qE = µ m (qE/m) τ µ = 1 / τ

For metals, measuring conductivity is convenient, whereas measuring τ is not. The equation for conductivity is: σ E = j

Both E and j are readily measurable. We also know that current j equals the number of free electrons multiplied by their average velocity.

j = N q v_drift

σ E = j = N (q^2 E / m) τ σ = (N q^2 / m) τ µ = 1 / τ = N q^2 / mσ

Putting this into the refractive index equation yields: n^2 = 1 + (N q^2 / mε) / (–ω^2 + iωµ)

n^2 = 1 + (σ / τε) / {iω (iω + µ)} n^2 = 1 + σ / {iωε (iωτ + 1)}

Clearly, the refractive index equation is much simpler in metals than in dielectrics.

Skin Depth & Plasma Frequency

Let’s examine the refractive index of a metal at various frequencies.

At low frequencies, where ωτ << 1 and ω << σ/ε, the index approaches: n^2 ≈ –iσ / (ωε)

In his lectures, Feynman says we can take this square root by noting that: √(–i) = (1 – i)/√2

We can verify that by squaring this equation, obtaining: –i = (1 – 2i – 1)/2

More generally, recall that complex numbers can be represented by exponentials. For example: –i = exp(–iπ/2)

√(–i) = exp(–iπ/4) = cos(π/4) – i sin(π/4) = (1 – i)/√2

This approach makes it easy to calculate any complex number raised to any power. Employing this in the current equation yields: n = {(1 – i)/√2} √(σ/ωε)

n = (1 – i) √(σ / 2ωε)

The real and imaginary parts of this index have the same magnitude. The wave amplitude decreases with z as: exp{–z (ω/c) √(σ / 2ωε)} = exp{–z √(σω / 2ε c^2)} = exp{–z/δ} with δ = √(2ε c^2 / σω)

The amplitude thus drops to 1/e ≈ 0.368 at z/δ=1, and δ is called the skin depth. (Note that we previously discussed the decrease in intensity, where the exponent is doubled.) Recall that this is applicable for low frequencies, where: ω << 1/τ and ω << σ/ε

Let’s consider some actual numbers, using copper as our example.

σ = 5.76×10^7 per ohm-meter weight/atom: 63.5 grams / 6.02×10^23 density: 8.9 grams / cm^3 atoms/cm^3: (8.9 / 63.5) × 6.02×10^23 = 8.49×10^22 m3: 8.44×1028 electron charge q: 1.6×10–19 coulomb electron mass m: 9.11×10–31 kilogram vacuum permittivity ε: 8.85×10–12 farad/meter Assuming one free electron per atom, we obtain: Mean collision time τ = 2.4×10–14 sec 1/τ = µ = 4.1×10+13 / sec σ/ε = 6.5×10+18 / sec These numbers mean our low-frequency analysis is valid in copper for frequencies below about 10+12 cycles per second, which is one trillion Hertz. The skin depth for such frequencies is given by: δ = 0.167 meters / √ω (radians/second)

For 10 GHz, ω=6.28×10+10 radians/second, δ=6.66 microns — a very thin skin indeed.

This is why, when we studied cavity resonances and waveguides, we did not need to consider fields within the conducting walls. This also explains why a very thin coating of highly conductive metal effectively cuts resistive losses: the fields enter only a microscopically thin layer.

Next, let’s turn to high frequency waves in metals. For ωτ>>1, the index approaches: n2 = 1 + σ / {iωε(iωτ)} = 1 – σ / (ω2ετ)

0 0 The index becomes entirely real, and remarkably is less than 1. This means the phase velocity is greater than the speed of light. We know from Feynman Simplified 1C, Chapter 34, that phase velocity, the speed of a single-frequency wave, cannot be the velocity of any real entity. Phase velocity may exceed c without contradicting special relativity.

A single-frequency wave is an idealization that is as unrealistic as frictionless motion; both simplify analysis and aid understanding, but neither is a true description of nature. A single-frequency wave has an absolutely definite energy (ΔEnergy=0), which by the Uncertainty Principle means it must extend over all time (Δt>ħ/ΔE=∞). With only one frequency, a wave can never start or stop. Real entities must be represented by wave packets comprising a range of frequencies; they travel at the group velocity dω/dk.

Substituting the expression for σ changes the refractive index equation to: n2 = 1 – (Nq2/m) τ / (ω2ετ)

n2 = 1 – Nq2 / mεω2 The quantity √(Nq2/mε) is called the plasma frequency ω. In terms of ω, we have: 0 p p n2 = 1 – ω2 / ω2 For ω<ω, the refractive index is complex. Waves propagate with real frequencies, and exponentially decreasing magnitudes due to the imaginary part of n.

For ω>ω, the refractive index is real; waves propagate without attenuation — the metal is transparent above ω.

For many metals, the plasma frequency is far beyond that of visible light. This is why only Superman can see through metals. For copper, it is 1.6×1016 Hertz. But for other metals, ω is in the ultraviolet part of the spectrum. The wavelengths corresponding to the measured and calculated plasma frequencies are compared below for several such metals. Wavelengths are stated in angstroms, with measurements to the left and calculations to the right.

Li : 1550 vs. 1550 Na: 2100 vs. 2090 K : 3150 vs. 2870 Rb: 3400 vs. 3220 The agreement is reasonably good, particularly since the measurements are actually quite difficult to do.

For midrange frequencies, the index of refraction in metals generally has both real and imaginary parts, leading to attenuated waves. Very thin metal layers can be partially transparent even at optical frequencies. Feynman notes that near high-temperature furnaces, goggles plated with a thin gold film allow workers to see visible light, while strongly absorbing intense infrared light that would damage their eyes.

In V2p32-13, Feynman says that if the equations for the refractive index look familiar, it is because they are almost identical to those for the dielectric constant κ that we studied in Chapter 11. This makes sense because both phenomena involve the polarization of matter. There we found: κ = 1 + Nα / (1 – Nα/3)

with α = q2 / (ε m ω2)

0 0 Here we have: n2 = 1 + α N / (1 – αN/3)

with α = (q2/mε) /(–ω2 +iωµ +ω2)

0 0 The dielectric constant is defined for static electric fields (ω=0). The dielectric constant κ is effectively the zero-frequency limit of n2, the refractive index squared.

Feynman concludes this topic saying: “Although we have been talking about wave propagation in metals, you appreciate by this time the universality of the phenomena of physics—that it doesn’t make any difference whether the free electrons are in a metal or whether they are in the plasma of the ionosphere of the earth, or in the atmosphere of a star. To understand radio propagation in the ionosphere, we can use the same expressions—using, of course, the proper values for N and τ. We can see now why long radio waves are absorbed or reflected by the ionosphere, whereas short waves go right through. (Short waves must be used for communication with satellites.)”

Historical Notation Feynman reminds us in V2p32-4 that, in Maxwell’s time, physicists did not understand atoms. They did not realize atoms polarize in dielectric materials exposed to external fields. They also did not realize that magnets contain circulating currents due to the atomic states of electrons. Unable to account for polarizatio On charges and currents, and electrons’ magnetic effects, they defined vector fields D and H in terms of the observed free charges and currents, ρ_free and j_free. D = ε₀E + P = εE ∇⋅D = ρ_free µ₀H = B ∇×H = j_free + ∂D/∂t

Feynman presents these equations because they still exist in many books, but he recommends not using them, saying: “These relations are only approximately true for some materials and even then only if the fields are not changing rapidly with time. …We think the right way is to keep the equations in terms of the fundamental quantities as we now understand them—and that’s how we have done it.”

## Chapter 32 Review: Key Ideas

• The index of refraction n of any material of any density is given by: α = (q²/mε₀) Σ f_i/(–ω² +iωµ_i +ω²_i) n² = 1 + α N / (1 – αN/3) 3(n²–1)/(n²+2) = α N

Here, α is the atomic polarizability, N is the number of active electrons per unit volume, q and m are the electron’s charge and mass, ω is the frequency of the incident electric field, and the summation is over all electron excited states. Excited state i has natural frequency ω_i, damping force mωµ_i, and weighting factor f. The last equation above is the Clausius-Mossotti equation.

Index n is complex in general. We define its real and imaginary parts as: n = n_r – in_i For positive damping, µ>0, n_i is also positive.

A mixture of k different materials has an index n given by: 3(n²–1)/(n²+2) = Σ α_k N_k

• Inside a material body, the electric field is: E = E₀ exp{iω(t–zn/c)} exp{–znω_i/c)} The field oscillates, moving toward +z at velocity c/n with exponentially decreasing amplitude. The intensity absorption coefficient β equals 2nω_i/c, meaning that the intensity decreases as exp{–βz}.

• In metals, the actions of free electrons dominate, and the refractive index becomes: n² = 1+ σ / {iωε₀ (iωτ +1) } Here, the metal’s conductivity is σ, and its mean collision time is τ. At low frequencies, below 10¹² cycles/sec in copper, the index approaches: n = (1–i) √(σ/2ωε₀) The field decreases exponentially as exp{–z/δ} with: skin depth δ=√(2ε₀c²/σω) In copper, δ=16.7 cm /√ω (radians/sec), which is 6.66 microns at 10 GHz.

The plasma frequency ω_p=√(Nq²/mε₀). At frequencies greater than ω_p, the index is: n² = 1 – ω² / ω²_p The index is real and the metal becomes transparent. Since n<1, the phase velocity is greater than c. But since phase velocity is not the speed of any real entity, this does not contradict special relativity. At frequencies less than ω_p, the index is complex. Waves propagate with real frequencies, and exponentially decreasing magnitudes.

## Chapter 33 Reflection Transmission

In Feynman Simplified 1C, Chapter 36, we studied the reflection and refraction (transmission) of light hitting a flat surface S separating two materials of different refractive indices, call them n₁ and n₂. Recall these results, illustrated in Figure 33-1:

Reflection: θ₃ = θ₁ Refraction, Snell’s law: n₁ sinθ₁ = n₂ sin θ₂ Reflected intensity, E parallel to S: R_s = I_s / I₀ R_s = sin²(θ₁–θ₂) / sin²(θ₁+θ₂)

Reflected intensity, E in incident plane: R_plane = I_plane / I₀ R_plane = tan²(θ₁–θ₂) / tan²(θ₁+θ₂)

Reflected intensity, normal incidence: θ₁ = θ₂ = θ₃ = 0 R_norm = I_norm / I₀ R_norm = (n₂–n₁)² / (n₂+n₁)²

Figure 33-1 Light Hitting Surface S

In the figure and equations above, x is the horizontal axis, y is the vertical axis, and z points out of the screen. The origin of the coordinate system is the point at which incident light hits surface S, the x=0 plane. All three θ’s are defined relative to the x-axis: θ₁ is the angle of the incident beam, θ₃ is the angle of the reflected beam, and θ₂ is the angle of the transmitted (refracted) beam. Also, I₀ is the intensity of the incident light beam that enters from the lower left, and the incident plane is the plane of your screen, the z=0 plane that contains the incident, reflected, and transmitted light beams.

In V2p33-1, Feynman says: “Our earlier discussion is really about as far as anyone would normally need to go with the subject, but we are going to do it all over again a different way. Why? One reason is that we assumed before that the indexes were real (no absorption in the materials). But another reason is that you should know how to deal with what happens to waves at surfaces from the point of view of Maxwell’s equations. We’ll get the same answers as before, but now from a straightforward solution of the wave problem, rather than by some clever arguments.”

Feynman seeks to teach us more than physics. He wants to help us learn how to be a physicist, how to think like a physicist, how to attack problems you have never seen before, indeed problems that no one has ever seen before.

Our purpose in this chapter is not primarily to derive the equations of reflection and refraction. We have those already. Our goal is to expand your toolbox — to learn analytical methods that you may need for even greater challenges. Reflection is the example on which we will hone our skills.

these new tools. Feynman stresses that reflection is not determined by the properties of the bulk material, but rather by its surface properties. Some exotic and interesting effects arise if the surface is irregular in shape or refractive index, with irregularities occurring over distances comparable to λ, the wavelength of incident light. These exotic effects include the shimmering colors of thin films of oil or plastic. Another effect is more practical: antireflective coatings on eyeglasses, comprised of thin films of different refractive indices. To simplify our discussion, we will assume S is perfectly flat and that the refractive index changes from n1 to n2 within a distance much less than λ.

Waves in Dense Matter

We begin by recalling some wave basics. Every wave can be represented as a linear superposition of single-frequency waves. Once we have the solution for a single-frequency wave of any frequency, we can use linear superposition to obtain solutions for any waveform. An electromagnetic wave has an electric field and a magnetic field that are mutually orthogonal. Let’s consider a single-frequency electric field E, represented by: E(r,t) = E0 exp{iωt – ik•r}. The vector k points in the direction that the wave is moving. The wave number k is the magnitude of k. The phase velocity vph equals ω/k, which equals c/n in a material of refractive index n. We thus have: |k| = k = 2π / λ; vph = ω / k = c / n; k = ω n / c. The derivatives of exponentials are particularly simple. For example: ∂E/∂t = iω E; ∂E/∂x = –ik E. In V2p33-2, Feynman points out that the gradient operator ∇ is effectively a vector product (for single-frequency sinusoidal waves). For any wave E(r,t) of the form shown above: ∇ E = (∂E/∂x, ∂E/∂y, ∂E/∂z); ∇ E = (–ikxE, –ikyE, –ikzE); ∇ E = –ik E. This also applies to curls and divergences. For example, the z-component of ∇×E equals the z-component of –ik×E, as the following confirms: (∇×E)z = ∂Ey/∂x – ∂Ex/∂y; (∇×E)z = –ikxEy + ikyEx; (∇×E)z = (–ik×E)z. Hence: ∇•E = –ik•E; ∇×E = –ik×E. Faraday’s law for a single-frequency wave becomes: ∇×E = – ∂B/∂t; –ik×E = –iωB; B = k×E / ω. This is a very simple demonstration that in an electromagnetic wave, the electric field, the magnetic field, and the direction of motion are all mutually orthogonal. Feynman doesn’t do this, but it is interesting to reverse the last equation. Let’s take the cross product of both sides with k, and employ an identity of vector algebra: A×(B×C) = B(A•C) – (A•B)C; ω k×B = k×(k×E) = k(k•E) – (k•k)E; E = B×k (c2/ωn2). In the last step, we used k•E=0 and k•k=(ωn/c)2. Let’s now consider the situation illustrated in Figure 33-1: light incident on the surface S separating two isotropic bodies of refractive index n1 and n2. All three waves — incident, reflected, and transmitted — propagate within the incident plane (z=0), and so kz=0 for each wave. We represent their electric fields by: incident: E1(r,t) = E01 exp{iωt – ik1•r}; refracted: E2(r,t) = E02 exp{iωt – ik2•r}; reflected: E3(r,t) = E03 exp{iωt – ik3•r}. Since the incident and reflected waves are in the same medium, with index n1, the wave numbers are: k1 = ω n1 / c; k2 = ω n2 / c; k3 = ω n1 / c. The magnetic fields for each wave are: B1 = k1 × E1 / ω; B2 = k2 × E2 / ω; B3 = k3 × E3 / ω.

Boundary Conditions

In V2p33-4, Feynman says: “All we have done so far is to describe the three waves; our problem now is to work out the parameters of the reflected and transmitted waves in terms of those of the incident wave. How can we do that? The three waves we have described satisfy Maxwell’s equations in the uniform material, but Maxwell’s equations must also be satisfied at the boundary between the two different materials. So we must now look at what happens right at the boundary. We will find that Maxwell’s equations demand that the three waves fit together in a certain way.” Boundary conditions are essential inputs to the solution of any differential equation. We know that a baseball flying through the air drops with an acceleration of 1g, which is 32 feet/sec2 or 9.8 m/sec2. We can definitively write: d2x/dt2 = – 1g. But this equation does not tell us whether a baseball becomes a home run, a grounder to the shortstop, an easy outfield fly, or a foul ball; the outcome depends on boundary conditions. We cannot calculate the ball’s path without knowing how the ball started — its initial position and velocity. Boundary conditions are sometimes obtained by observation and sometimes by applying physical laws. Galileo used the former when he dropped balls from the Leaning Tower of Pisa. An example of the latter is applying Faraday’s law to the y-component of the electric field across surface S. (The former is more dramatic.) In Figure 33-2, the rectangular loop Γ has height h, width w, and encircles a portion of surface S. Figure 33-2 Faraday Boundary Condition. Faraday’s law is: ∇×E = –∂B/∂t. This means the counterclockwise circulation of E around Γ equals minus the rate of change of the magnetic flux through the area A that Γ encloses. In the limit that width w goes to zero, so does area A, and the above equation reduces to: – E_{1y} + E_{2y} = – ∂/∂t { ∫ B•da } = 0 E_{1y} = E_{2y} The equations say: in the limit that area A goes to zero, the magnetic flux through A goes to zero, and the component of E parallel to the surface does not change.

Sometimes it isn’t easy to get all the boundary conditions we need to solve our differential equations. Feynman shows us a tool that can help. He begins by writing out all the components of Maxwell’s four equations in the presence of dielectric, non-magnetic matter.

ε₀ ∇•E = – ∇•P ε₀ (∂E_x/∂x+∂E_y/∂y+∂E_z/∂z) = – (∂P_x/∂x+∂P_y/∂y+∂P_z/∂z)

∇×E = –∂B/∂t ∂E_z/∂y – ∂E_y/∂z = – ∂B_x/∂t ∂E_x/∂z – ∂E_z/∂x = – ∂B_y/∂t ∂E_y/∂x – ∂E_x/∂y = – ∂B_z/∂t ∇•B = 0 = (∂B_x/∂x+∂B_y/∂y+∂B_z/∂z)

c² ∇×B = ∂E/∂t – ∂P/∂t /ε₀ c²(∂B_z/∂y–∂B_y/∂z)=∂E_x/∂t–∂P_x/∂t /ε₀ c²(∂B_x/∂z–∂B_z/∂x)=∂E_y/∂t–∂P_y/∂t /ε₀ c²(∂B_y/∂x–∂B_x/∂y)=∂E_z/∂t–∂P_z/∂t /ε₀ These equations hold everywhere, including at the boundary.

As Feynman says, we often think of boundaries as places where matter changes discontinuously. However, in the real world, change may be extremely rapid but never infinitely rapid. There is always a small transition zone. In this case, the transition is between index n₁ and index n₂, and between fields E₁-P₁-B₁ and fields E₂-P₂-B₂.

Figure 33-3 illustrates this point. Here, a magnified view shows field P rapidly changing in the vicinity of the boundary, the transition from white to gray. The exact shape of this curve is not particularly important.

Figure 33-3 Transition At Surface The key point is the magnitude of ∂P_x/∂x, the rate of change of P_x as incident light crosses the boundary. In the limit that the transition is extremely rapid, x-derivatives here will be extremely large, much larger than other derivatives.

Assuming that all other derivatives are negligible in comparison to x-derivatives, Maxwell’s equations simplify substantially at a sharp boundary.

ε₀ ∇•E = – ∇•P ε₀ ∂E_x/∂x +0 +0 = – ∂P_x/∂x +0 +0 ∇×E = –∂B/∂t ∂E_z/∂y – ∂E_y/∂z = –∂B_x/∂t ∂E_y/∂x = 0 ∂E_z/∂x = 0 ∇•B = 0 = ∂B_x/∂x c² ∇×B = ∂E/∂t – ∂P/∂t /ε₀ ε₀c² (∂B_z/∂y – ∂B_y/∂z) = ε₀∂E_x/∂t + ∂P_x/∂t c² ∂B_x/∂x = 0 c² ∂B_x/∂x = 0 Maxwell’s first equation reduces to: ∂/∂x {ε₀ E_x + P_x} = 0 This means {ε₀E_x+P_x} does not change across the boundary: it has the same value just outside the surface as it does just inside the surface. Mathematically, we say this quantity is continuous across the boundary. This is one important boundary condition.

In Maxwell’s second equation, the y-component is: ∂E_y/∂x = 0 This means E_y is continuous across the boundary.

The z-component similarly shows that E_z is continuous across the boundary.

The third equation shows that B_x is continuous across the boundary.

The fourth equation shows that B_y and B_z are continuous across the boundary.

Altogether, we have identified six boundary conditions, six quantities that are continuous across the boundary. These are: {ε₀E_x+P_x}, E_y, E_z, B_x, B_y and B_z Remember that we have assumed isotropic non-magnetic matter on both sides of the boundary.

Feynman says this general approach will help whenever fields cross a sharp boundary.

Match Making We can now match the three waves at the boundary S, and find what constraints that matching imposes on the fields.

Light has two polarization states. Let’s first consider the polarization state in which the electric field is perpendicular to the screen and incident plane, and is therefore parallel to surface S. The E fields are indicated in Figure 33-4 by the bull’s eyes, and the B fields by the attached arrows.

Figure 33-4 E Parallel to S For isotropic matter, all electron excitations and polarizations are perpendicular to the screen in this case, so we have: E_x = E_y = P_x = P_y = 0 everywhere Since the waves all propagate within the incident plane, orthogonal to the z-axis, we also know that k_z=0 for each wave.

On the right side of S, the only fields are the transmitted fields E₂ and B₂. On the left side of S, the incident and reflected fields are superposed. At the boundary, at x=0, the total field on the left and the field on the right must be the same. For the electric field, this means: E₁(r,t) + E₃(r,t) = E₂(r,t) at x=0 For each wave, k•r=k_y y, because x=0 and k_z=0. The prior equation becomes: E_{01} exp{iωt–ik_{1y} y} + E_{03} exp{iωt–ik_{3y} y} = E_{02} exp{iωt–ik_{2y} y} This equation must hold for all t and y. Let’s examine it for y=0.

E_{01} exp{iωt} + E_{03} exp{iωt} = E_{02} exp{iωt} This can be true for all t only if: ω₁ = ω₃ = ω₂ = ω We will therefore drop the subscript on ω. We could have derived this directly from physical laws: the secondary fields are driven by the incident field; whenever the driving field changes polarity, so must the driven fields.

Now let’s examine our boundary matching equation for t=0.

E_{01} exp{–ik_{1y} y} + E_{03} exp{–ik_{3y} y} = E_{02} exp{–ik_{2y} y} p{–ik y} 02 2y This can be true for all y only if: k = k = k = k y 1y 3y 2y We have another way of relating the three wave numbers. For each wave: k² = k² + k² = ω² n² / c² x y This means: ω² / c² = k² / n² = k² / n² = k² / n² 1 1 2 2 3 1 Hence, k² = k² 1 3 k² + k² = k² + k² 1x 1y 3x 3y Since the y-components are equal, so must be the squares of the x-components.

k = √(k²) = ± k 1x 3x 3x The positive sign corresponds to a wave moving toward +x, therefore only the minus sign makes sense for a reflected wave.

k = – k 3x 1x Since tanθ = k/k, this shows that θ and θ have the same magnitude and the opposite orientation, y x 1 3 confirming that the angle of reflection equals the angle of incidence. The reflected wave can now be written: E(r,t) = E exp{iωt + ik x – iky} 3 03 1x y For the transmitted wave we have: k = k = k y 1y 2y ω² / c² = k² / n² = k² / n² 1 1 2 2 k² n²/n² = k² = k² + k² 1 2 1 2 2x 2y This gives us an equation for k²: 2x k² = k² n²/n² – k² 2x 1 2 1 y If both n and n are real, then so are k and k. From the equation before last, this means: 1 2 1 2 k = k n/n 2 1 2 1 k sinθ = k = k 1 1 1y y k sinθ = k = k 2 2 2y y k sinθ = k sinθ 1 1 2 2 k sinθ = k sinθ n/n 1 1 1 2 2 1 n sinθ = n sinθ 1 1 2 2 This is Snell’s law, which is valid when both refractive indices are real.

In V2p33-9, Feynman says: “So far, we haven’t found anything new. We have just had the simple-minded delight of getting some obvious answers from a complicated mathematical machinery. Now we are ready to find the amplitudes of the waves which we have not yet known.” Since we have shown that: ω = ω = ω = ω 1 3 2 k = k = k = k y 1y 3y 2y the exponentials in each field at x=0 become: exp{ iωt – iky } Cancelling this common factor, the E-field matching equation now reduces to: E + E = E 01 03 02 To complete the solution, we need a second equation relating these quantities.

With E polarized along the z-axis, the matching equations for E and E are useless. Let’s see what the B-field-matching equations reveal. We found above that all three components of B are continuous across the boundary. B is zero everywhere, because E is parallel to the z-axis, so there are only two remaining boundary conditions: B = B and B = B . The x-component yields: x y 1x 2x 1y 2y B = (k×E) / ω = k E/ω x x y At x=0: B + B = B 1x 3x 2x k E /ω + k E /ω = k E /ω y 01 y 03 y 02 This adds nothing — it is the same equation we obtained earlier. The last boundary condition is the continuity of B.

B = (k×E) / ω = – k E/ω y y x At x=0: B + B = B 1y 3y 2y k E /ω + k E /ω = k E /ω 1x 01 3x 03 2x 02 Recall that k = –k , but k is different. We thus have a second independent equation, allowing us to solve for two unknowns, E and E , in terms of the incident field E .

3x 1x 2x 02 03 01 E + E = E 01 03 02 k E – k E = k E 1x 01 1x 03 2x 02 k E – k E = k (E + E )

1x 01 1x 03 2x 01 03 (k – k ) E = (k + k ) E 1x 2x 01 1x 2x 03 E = E (k – k ) / (k + k )

03 01 1x 2x 1x 2x E + E (k – k ) / (k + k ) = E 01 01 1x 2x 1x 2x 02 E = E (k + k + k – k ) / (k + k )

02 01 1x 2x 1x 2x 1x 2x E = E (2k ) / (k + k )

02 01 1x 1x 2x With k² = k² n²/n² – k², we have a complete solution for z-axis polarization.

2x 1 2 1 y For E polarized within the incident plane, E has both x- and y-components but B has only one component: B. This is illustrated in Figure 33-5.

z Figure 33-5 E in Incident Plane For this case, Feynman quotes the results without derivation. A full derivation is provided at the end of this chapter. The results are: |E | = |E | (n² k – n² k ) / (n² k + n² k )

03 01 2 1x 1 2x 2 1x 1 2x |E | = |E | (2 n n k ) / (n² k + n² k )

02 01 1 2 1x 2 1x 1 2x Let’s compare our new results with those in Feynman Simplified 1C, Chapter 36, where all indices are assumed to be real. For real indices, the components of k are real and are related to the wave propagation angles by: k = k cosθ = ω n cosθ / c 1x 1 1 1 1 k = k cosθ = ω n cosθ / c 2x 2 2 2 2 k = – k 3x 1x k = k = k sinθ = ω n sinθ / c 1y y 1 1 1 1 k = k = k sinθ = ω n sinθ / c 2y y 2 2 2 2 k = k 3y y For E polarized perpendicular to the incident plane, the new reflected wave equation becomes: E / E = (k – k ) / (k + k )

03 01 1x 2x 1x 2x = (n cosθ – n cosθ ) / (n cosθ + n cosθ )

1 1 2 2 1 1 2 2 Using Snell’s law, n = n sinθ / sinθ , we get: 2 1 1 2 E / E = n (cosθ – cosθ sinθ / sinθ )

03 01 1 1 2 1 2 / n (cosθ + cosθ sinθ / sinθ )

1 1 2 1 2 E / E = (cosθ sinθ – cosθ sinθ )

03 01 1 2 2 1 / (cosθ sinθ + cosθ sinθ )

1 2 2 1 E / E = sin(θ – θ ) / sin(θ + θ )

03 01 1 2 1 2 This matches the equation from Feynman Simplified 1C.

For E polarized parallel to the incident plane, the new reflected wave equation is: |E | / |E | = (n² k – n² k ) / (n² k + n² k )

03 01 2 1x 1 2x 2 1x 1 2x = (n² n cosθ – n² n cosθ )

2 1 1 1 2 2 / (n² n cosθ + n² n cosθ )

2 1 1 1 2 2 = (n cosθ – n cosθ )

2 1 1 2 / (n cosθ + n cosθ )

2 1 1 2 = (n cosθ sinθ / sinθ – n cosθ )

1 1 1 2 1 2 / (n cosθ sinθ / sinθ + n cosθ )

1 1 1 2 1 2 = (cosθ sinθ – cosθ sinθ )

1 1 2 2 / (cosθ sinθ + cosθ sinθ )

1 1 2 2 = (sin2θ – sin2θ ) / (sin2θ + sin2θ )

1 2 1 2 This matches the equation from Feynman Simplified 1C.

n²θ) / 1 2 1 2

We now employ the trig identity: sin²A ± sin²B = 2 sin(A±B) cos(–A±B)

|E₀₃| / |E₀₁| = [2 sin(θ₁ – θ₂) cos(θ₁ + θ₂)] / [2 sin(θ₁ + θ₂) cos(θ₁ – θ₂)]

|E₀₃| / |E₀₁| = tan(θ₁ – θ₂) / tan(θ₁ + θ₂)

This also matches the equation from Feynman Simplified 1C. We did not calculate the transmitted field amplitudes in 1C. We do that now for the case of real refractive indices.

For E polarized perpendicular to the incident plane, the new transmitted wave equation is: E₀₂ / E₀₁ = (2k₁ₓ) / (k₁ₓ + k₂ₓ)

= 2n₁cosθ₁ / n₁(cosθ₁ + cosθ₂ sinθ₁ /sinθ₂)

= 2cosθ₁ sinθ₂ / (cosθ₁ sinθ₂ + cosθ₂ sinθ₁)

E₀₂ / E₀₁ = 2 cosθ₁ sinθ₂ / sin(θ₁ + θ₂)

For E polarized parallel to the incident plane, the new transmitted wave equation is: |E₀₂| / |E₀₁| = (2n₁n₂k₁ₓ) / (n₂²k₁ₓ + n₁²k₂ₓ)

= 2n₁n₂ n₁cosθ₁ / (n₂² n₁cosθ₁ + n₁² n₂cosθ₂)

= 2 n₁cosθ₁ / (n₂cosθ₁ + n₁cosθ₂)

|E₀₂| / |E₀₁| = 2 / (n₂/n₁ + cosθ₂ /cosθ₁)

For the case of normal incidence, where all θ’s are zero and all polarizations are normal to surface S, the reflected wave equation becomes: |E₀₃| / |E₀₁| = (n₂²k₁ₓ – n₁²k₂ₓ) / (n₂²k₁ₓ + n₁²k₂ₓ)

|E₀₃| / |E₀₁| = (n₂²n₁ – n₁²n₂) / (n₂²n₁ + n₁²n₂)

|E₀₃| / |E₀₁| = (n₁ – n₂) / (n₁ + n₂)

This matches the equation from Feynman Simplified 1C.

Finally, the transmitted wave equation for normal incidence becomes: |E₀₂| / |E₀₁| = (2n₁n₂k₁ₓ) / (n₂²k₁ₓ + n₁²k₂ₓ)

= 2n₁n₂ n₁ / (n₂² n₁ + n₁² n₂)

|E₀₂| / |E₀₁| = 2 n₁ / (n₁ + n₂)

Reflection from Metals

In V2p33-11, Feynman says: “We can now use our results to understand the interesting phenomenon of reflection from metals. Why is it that metals are shiny?”

In the prior chapter, we found that the refractive indices of metal are complex numbers whose imaginary parts can be as large as their real parts.

To examine an even more extreme case, consider a substance whose refractive index is entirely imaginary: n = –in. The normal incidence reflection intensity ratio for such a substance is: R = Iᵣ / I₀ = |1 + in|² / |1 – in|² which equals 1. This means the surface is 100% reflective. Metals are not this extreme, but their refractive indices do have large imaginary parts, and they are highly reflective. Feynman says this exemplifies a general rule: “if any material gets to be a very good absorber at any frequency, the waves [of that frequency] are strongly reflected at the surface and very little gets inside to be absorbed. You can see this effect with strong dyes. Pure crystals of the strongest dyes have a ‘metallic’ shine.”

This is illustrated in Figure 33-6. White light shines on a glass plate whose opposite surface is coated with a red dye.

Figure 33-6 Effect of Red Dye

Red dyes transmit red light with minimal attenuation, while preventing the transmission of the complementary color: green. At the frequency of green light, the refractive index of red dye has a very large imaginary part. Red dyes do not absorb green light as much as they strongly reflect it.

Red ink and paint do the opposite; they strongly reflect red light and absorb other colors.

Total Internal Reflection

Previously, we considered light incident on a surface at which the refractive index increases. This results in light bending toward the normal to the surface.

But, when light is incident on a surface at which the refractive index decreases, it bends away from the normal, as shown in Figure 33-7.

Figure 33-7 Refraction For n₂ < n₁

We can still apply Snell’s law: n₁ sinθ₁ = n₂ sinθ₂

Clearly, if n₂ is less than n₁, θ₂ must be greater than θ₁.

Now what happens if θ₂ is 90 degrees? We then call the incident θ₁ the critical angle θc, given by: sinθc = n₂ / n₁

Since sinθ can never be greater than 1, at any incident angle greater than the critical angle there can be no transmitted wave and the incident wave must be entirely reflected. This is called total internal reflection, because light remains internal to the higher index material. One application of total internal reflection is keeping light within optical fibers in long distance communication systems.

With our new results, let’s examine exactly how total internal reflection arises. For simplicity, let the lower index substance be air with n₂=1, and let n=n₁>1. The equation for the x-component of the transmitted beam is: k₂ₓ² = k² / n₂² – kᵧ²

Now recall that: k=ωn₁/c, and kᵧ=k₁ sinθ₁.

k₂ₓ² = (ω²/c²) {1 – n₁² sin²θ₁}

For θ₁ > θc, sinθ₁ >1/n₁ and the term in { }’s is negative. This makes k₂ₓ entirely imaginary.

Let k₂ₓ = –ikᵢ.

Since we have seen this many times before, you know why we rejected the “+” option in taking the square root.

This makes the transmitted field: E(r,t) = E₀₂ exp{iωt – ik•r} E(r,t) = E₀₂ exp{iωt–ikᵧy} exp{–kᵢx}

Again, this electric field has an exponentially decreasing magnitude for x>0. Since the value of kᵢ is similar to the value of 1/λ, where λ is the wavelength The incident light wave is severely attenuated after extending into air by only a few wavelengths.

Figure 33-8 shows what happens when a second body with the same refractive index n is placed near the first, leaving only a thin gap of air between them. The transmitted wave is forbidden from entering the gap according to classical physics, because its wave number squared is negative. Nonetheless, if the gap is small enough, the transmitted wave seems to leap across the forbidden zone.

This is an example of the quantum phenomenon of barrier penetration, which we discuss thoroughly in Feynman Simplified 3A, Chapter 9. The key distinction between classical and quantum descriptions is that at x=0, the classical wave magnitude drops immediately to zero, whereas the quantum wave magnitude starts decreasing exponentially.

Even in the quantum world, a wave is never observed in a classically forbidden region; that observation would violate energy conservation. The wave arrives at surface S_L and simply reappears at surface S_R in the allowed zone on the other side of the barrier.

Figure 33-9 shows the magnitude of the transmitted wave decreasing exponentially with distance x from S_L. If S_L is close enough, a significant fraction of the original transmitted wave remains when it reaches the second refractive body. Some of the transmitted wave is reflected at S_R, while some is transmitted into the second body. There k becomes real once more, and the wave resumes oscillating with constant magnitude.

Demonstrating this effect with visible light is very difficult, because visible wavelengths are less than one micron. It is much easier using microwaves with wavelengths of several centimeters. In this demonstration, Feynman uses a microwave source, two detectors, and two paraffin prisms. The prisms are right triangles with both smaller angles being 45-degrees. Paraffin has a refractive index of 1.5 at λ = 3 cm. For a wave incident on a paraffin-air boundary the critical angle is: sinθ = (n in air) / (n in paraffin) = 1/1.5 θ = 41.8 degrees

This ensures total internal reflection for 3-cm microwaves. Microwaves incident on a surface inclined at 45 degrees will, therefore, be entirely reflected with θ₃ = θ₁ = 45 degrees. This amounts to bending 90 degrees relative to their incident direction.

We see this in the upper image of Figure 33-10. Microwaves from source M enter a paraffin prism at normal incidence. When they strike the inclined rear surface, the waves are totally reflected downward to detector A. No waves reach detector B.

In the middle image, two paraffin prisms are placed back-to-back, forming a square. For 3-cm microwaves, the gap between prisms is imperceptible; they pass straight through the square refractive body and arrive at detector B. No waves reach A.

In the lower image, with the two prisms separated by a thin gap, reflected waves reach A and transmitted waves reach B. The intensity of waves reaching B decreases exponentially with gap width, as is easily demonstrated by sliding the second prism.

E in Incident Plane

Here is the analysis for an incident wave with its electric field polarized within the incident plane. In this case, B is everywhere entirely along the z-axis, orthogonal to the incident plane. We can use some of the results from prior analysis, including: ω₁ = ω₃ = ω₂ k₃ₓ = –k₁ₓ

We follow Feynman’s advice and calculate the magnetic fields first, since they have only z-components. Let the magnetic fields for each wave be: incident: B₁ = B₀₁ exp{iωt – ik·r} refracted: B₂ = B₀₂ exp{iωt – ik·r} reflected: B₃ = B₀₃ exp{iωt – ik·r}

Since all waves are in the incident plane, each has k_z=0.

B₁ = B₀₁ exp{iωt –ik₁ₓx –ik₁ᵧy} B₂ = B₀₂ exp{iωt –ik₂ₓx –ik₂ᵧy} B₃ = B₀₃ exp{iωt +ik₁ₓx –ik₃ᵧy}

We also have from above: E = B×k (c²/ωn²)

For B entirely along the z-axis, we have: E_x = (c²/ωn²) (–k_y B_z)

E_y = (c²/ωn²) (+k_x B_z)

Maxwell’s equations at the sharp boundary at x=0 reduce to: ∂E/∂z = 0 ε₀c² (∂B_z/∂y) = ∂P_x/∂t + ε₀∂E_x/∂t ∂ {ε₀E_x + P_x} /∂x = 0 ∂ {E_y} /∂x = 0 ∂ {B_z} /∂x = 0

The continuity at x=0 of B_z yields (at t=0): B₀₁ exp{–ik_y y} + B₀₃ exp{–ik_y y} = B₀₂ exp{–ik_y y}

As before, this requires: k_y = k₁ᵧ = k₂ᵧ = k₃ᵧ B₀₁ + B₀₃ = B₀₂

Continuity at x=0 of E_y means: k₁ₓ B₀₁/n₁² – k₁ₓ B₀₃/n₁² = k₂ₓ B₀₂/n₂² n₂² k₁ₓ (B₀₁ – B₀₃) = n₁² k₂ₓ B₀₂

Combining the two equations relating B₀₁, B₀₂, and B₀₃ yields: k₁ₓ B₀₁ – k₁ₓ B₀₃ = k₂ₓ (B₀₁ + B₀₃) (n₁/n₂)² B₀₁ (n₂²k₁ₓ – n₁²k₂ₓ)

= B₀₃ (n₂²k₁ₓ + n₁²k₂ₓ)

For better clarity, let’s define m_ij = n_j² k_ix.

The last equation becomes: B₀₁ (m₂₁ – m₁₂) = B₀₃ (m₂₁ + m₁₂)

B₀₃ = B₀₁ (n₂²k₁ₓ – n₁²k₂ₓ) / (n₂²k₁ₓ + n₁²k₂ₓ)

Now, put this expression for B₀₃ into the equation for B₀₂.

B₀₂ = m₁₂ B₀₁ [m₂₁+m₁₂] / (m₂₁ (m₂₁+m₁₂) – m₂₁ B₀₁ [m₂₁–m₁₂])? No, let me correct this derivation step from the original.

Starting from the correct expression for B₀₂: B₀₂ = B₀₁ + B₀₃ = B₀₁ [1 + (n₂²k₁ₓ – n₁²k₂ₓ)/(n₂²k₁ₓ + n₁²k₂ₓ)]

= B₀₁ [ (n₂²k₁ₓ + n₁²k₂ₓ) + (n₂²k₁ₓ – n₁²k₂ₓ) ] / (n₂²k₁ₓ + n₁²k₂ₓ)

= B₀₁ [2 n₂² k₁ₓ] / (n₂²k₁ₓ + n₁²k₂ₓ)

This can be written as: B₀₂ = 2 m₂₁ B₀₁ / (m₂₁ + m₁₂)

(m²₁m²₁ + m²₁m²₁ – m²₁m²₁ + m²₁m²₁) B₀₁ B = B (2n²k) / (n²k + n²k)

02 01 2 1x 2 1x 1 2x

我们可以计算电场比率。

|E| = √(E² + E²)

x y |E| = (c²/ωn²) |B| √(k² + k²)

z x x |E| = (c²/ωn²) |B| ωn/c |E| = (c/n) |B| |E /E| = |B /B| n/n 03 01 03 01 1 1 |E /E| = (n²k – n²k) / (n²k + n²k)

03 01 2 1x 1 2x 2 1x 1 2x |E /E| = (2n²k) / (n²k + n²k) (n/n)

02 01 2 1x 2 1x 1 2x 1 2 |E /E| = (2nnk) / (n²k + n²k)

02 01 1 2 1x 2 1x 1 2x

QED

**Chapter 33 Review: Key Ideas** • 对于正弦波，梯度 ∇ 实际上是向量乘积。

对于 E(r,t) = E₀ exp{iωt – ik•r} ∇ E = (∂E/∂x, ∂E/∂y, ∂E/∂z)

∇ E = (–ikxE, –ikyE, –ikzE)

∇ E = –ik E ∇•E = –ik•E ∇×E = –ik×E ∇×E = – ∂B/∂t –ik×E = –iωB B = k×E / ω

• 对于入射在 x=0 平面上的光，该平面分隔了折射率为 n₁ (x<0) 和 n₂ (x>0) 的两种材料，我们定义三个电场： 入射：E₁(r,t) = E₀₁ exp{iωt – ik₁•r} 折射：E₂(r,t) = E₀₂ exp{iωt – ik₂•r} 反射：E₃(r,t) = E₀₃ exp{iωt – ik₃•r}

E 极化垂直于入射平面的解为： E₀₃ = E₀₁ (k₁x – k₂x) / (k₁x + k₂x)

E₀₂ = E₀₁ (2k₁x) / (k₁x + k₂x)

k²₂x = k²₁ n²₂/n²₁ – k²₁y

E 极化位于入射平面内的解为： |E₀₃| = |E₀₁| (n²₂k₁x – n²₁k₂x) / (n²₂k₁x + n²₁k₂x)

|E₀₂| = |E₀₁| (2n₁n₂k₁x) / (n²₂k₁x + n²₁k₂x)

正入射的解为： |E₀₃| / |E₀₁| = (n₂ – n₁) / (n₂ + n₁)

|E₀₂| / |E₀₁| = 2n₁ / (n₂ + n₁)

• 边界条件是任何微分方程求解的基本输入。

在 x=0 平面的尖锐边界处，∂/∂x 导数主导其他所有导数，麦克斯韦方程组简化为： ∂Ez/∂y – ∂Ey/∂z = –∂Bx/∂t ε₀c² (∂Bz/∂y – ∂By/∂z) = ∂Px/∂t + ε₀∂Ex/∂t ∂ {ε₀Ex+Px} /∂x = 0 ∂ {Ey} /∂x = 0 ∂ {Ez} /∂x = 0 ∂ {Bx} /∂x = 0 ∂ {By} /∂x = 0 ∂ {Bz} /∂x = 0

这意味着对于无穷小 ε，在 –ε < x < +ε 范围内，每个 {} 中的量的值是相同的。

• 红色染料传输红光时衰减最小，同时阻止其互补色绿色的传输。在绿光的频率下，红色染料的折射率具有非常大的虚部。红色染料并非像强烈反射绿光那样吸收它。红色墨水和颜料则相反；它们强烈反射红光并吸收其他颜色。

**Chapter 34** **Clever Tricks** 当费曼警告学生某个主题特别棘手且可能过于复杂时，全班同学都会去拿头盔。

在 v2p7-1 中，费曼说： “我们将首先描述一些解决导体问题的更精细的方法。不期望现在就能掌握这些更高级的方法。然而，了解使用更高级课程中可能学到的技术可以解决哪类问题可能会很有趣。然后我们将讨论两个电荷分布既不是固定的，也不是由导体携带，而是由其他物理定律决定的例子。”

这节课放在静电学学习的早期确实不合适，但既然你们现在是经验丰富的老兵，已经战胜了凶猛的微分方程，你们已准备好迎接这一挑战。无论如何，既然“不期望”你们掌握这些材料，它不会出现在任何考试中，你们尝试也不会有什么损失。实际上，我们经历过更糟的情况。

**The Laplace Equation** 在静电学和许多其他科学领域中，我们发现由拉普拉斯方程描述的问题： ∇² φ = 0 其中 φ 是一个标量场，满足特定的边界条件。费曼说，即使一个看似简单的拉普拉斯方程在数学上也可能难以处理。他举的一个例子是带电啤酒罐产生的场。（改述爱因斯坦的话：如果你在喝啤酒时想着静电场，你就没有给予啤酒应有的关注。爱因斯坦实际上谈论的是亲吻漂亮女孩，但也许同样的想法也适用于啤酒。）

存在一些可以解析求解的拉普拉斯方程类别。费曼说带电椭球体（一个美式橄榄球）的场可以精确求解。由此，我们可以通过使椭球体无限扁平得到扁平圆盘的解。带电（无眼）针的场则通过使椭球体无限拉长得到。

一类更易处理的问题出现在某一维度的变化要么为零，要么小到可以忽略的情况下。这些问题实际上是二维的，因此更简单。

考虑例如沿 z 轴的一根非常长的导线。在导线无限长的极限下，根据对称性，所有 z 方向的导数必须为零。于是我们得到二维拉普拉斯方程： ∂²φ/∂x² + ∂²φ/∂y² = 0

费曼说这个方程经常可以通过“……一个非常强大的间接数学技巧来求解，该技巧依赖于复变函数数学中的一个定理，我们将在下一章讨论。” I now describe.

Function of Complex Variables Let’s define a complex variable β=x+iy, where both x and y are real functions. All the usual mathematical functions of real variables can be extended to become functions of complex variables. We have done this before, for example, in analyzing harmonic phenomena with exponentials with complex exponents.

Any function F(β) can be expressed as the sum of its real and imaginary parts. Recall this example: exp{x+iy} = exp{x} (cosy + isiny)

Similarly, for two real functions U and V, let: F(β) = U(x,y) + i V(x,y)

For example: F(β) = β2 = x2 + 2ixy – y2 U(x,y) = x2 – y2 V(x,y) = 2xy Feynman then says: “Now we come to a miraculous mathematical theorem which is so delightful that we shall leave a proof of it for one of your courses in mathematics. (We should not reveal all the mysteries of mathematics, or that subject matter would become too dull.) It is this. For any ‘ordinary function’ (mathematicians will define it better) the functions U and V automatically satisfy the relations:” ∂U/∂x = + ∂V/∂y ∂V/∂x = – ∂U/∂y We can confirm that our example satisfies these relations.

∂U/∂x = + ∂V/∂y = +2x ∂V/∂x = – ∂U/∂y = +2y Taking the second order partial derivatives of the prior pair of equations yields: ∂2U/∂x2 = ∂2V/∂x∂y = – ∂2U/∂y2 ∂2U/∂x2 + ∂2U/∂y2 = 0 ∂2V/∂x2 = – ∂2U/∂x∂y = – ∂2V/∂y2 ∂2V/∂x2 + ∂2V/∂y2 = 0 Thus, we can pick any function F(β) and immediately have two solutions, U and V, to the Laplace equation. Feynman says: “We can write down as many solutions as we wish—by just making up functions—then we just have to find the problem that goes with each solution. It may sound backwards, but it’s a possible approach.” Let’s take an example.

F(β) = β2 = (x2 + iy)2 U(x,y) = x2 – y2 = some constant A V(x,y) = 2xy = some constant B The equations for both U and V are satisfied by hyperbolas. The lighter curves in Figure 34-1 are hyperbolas for various values of A. The darker curves are hyperbolas for various values of B. The lighter curves and darker curves always cross one another orthogonally.

Figure 34-1 Hyperbolic Curves These curves could represent many different physical phenomena.

The darker curves could be the magnetic field lines of a quadrupole magnet with north poles at top and bottom, and south poles at left and right. The lighter curves would then indicate the direction of forces exerted on charged particles moving perpendicular to the screen.

As Figure 34-3 shows, the lighter curves could be the equipotentials of an electrostatic quadrupole lens with positively charged gray conductors at top and bottom, and negatively charged gray conductors at left and right. The darker curves would then indicate the electric field lines.

Figure 34-2 Electrostatic Quadrupole Lens The curves corresponding to U(x,y) and those corresponding to V(x,y) will always cross at 90 degrees. For electrostatics, this means U can represent equipotentials and V can represent electric field lines, or the other way around. We therefore obtain solutions for two problems at once. For magnetostatics, either U or V can represent the magnetic field lines while the other represents force directions.

Feynman notes some other interesting choices of F.

F(β) = β1/2 provides the electric field near a thin plate.

F(β) = β3/2 provides the electric field outside a rectangular corner.

F(β) = log(β) provides the electric field of a charged wire.

F(β) = 1/β provides the electric field of a 2-D dipole, two parallel oppositely charged wires in close proximity.

Plasma Oscillations A different class of problems arises when charges are subject to both electromagnetic and mechanical forces.

An interesting example is plasma, the state of ionized gaseous matter. At very high temperatures, when kT is much greater than atomic binding energies, a neutral gas becomes a sea of free electrons and ionized atoms. (Recall from Feynman Simplified 1B, Chapter 15, that kT is Boltz 2 = mv²/2.) We can therefore neglect the atoms and consider only the motion of free electrons. Let’s define n to be the density of free electrons, and define their equilibrium density to be n₀, which for neutral plasma is also the equilibrium density of ions. Now consider what happens if a disturbance increases the free electron density in some volume V. With n > n₀, V has a net negative charge, and its electrons will repel one another. The outward flux of electrons drives the electron density in V back toward equilibrium. But, like a pendulum displaced from equilibrium, accelerating electrons overshoot equilibrium, driving n below n₀. Electrons will then be accelerated back into V. The electron density n(t) will in fact oscillate above and below n₀, until damped by some dissipative effect. For a pendulum, the oscillator’s restoring force is gravity. For plasma, the restoring force is electrostatic attraction and repulsion, which strives for neutral charge density everywhere.

In V2p.7-6, Feynman examines plasma density oscillations in one dimension; call that x. We will assume everything is in equilibrium prior to time 0. At time t, a disturbance slightly displaces free electrons at x by the amount s(x,t). Figure 34-3 illustrates how that disturbance changes electron densities. The upper image shows a group of electrons within the interval [x, x+Δx] at time 0. The lower image shows the same group of electrons displaced to the interval [x+s, p] at time t. Figure 34-3 Displaced Plasma. From the figure, we determine that the right edge of the group moves to: p = (x+Δx) + (s+Δs). The interval spanned by the group has therefore changed in size from Δx to Δx+Δs.

The free electron density at time 0 is n₀, and the number of free electrons in Δx is: #electrons in Δx at time 0: n₀ Δx. The number of electrons at time t in Δx+Δs is: #electrons in Δx+Δs at time t: n (Δx+Δs). These two numbers are equal, because this is the same group of electrons before and after being displaced. The density at time t is therefore: n₀ Δx = n (Δx + Δs), n = n₀ / (1 + Δs/Δx). For small changes, we can approximate this using the Taylor series: 1 / (1+ε) = 1 – ε + ε² – ε³ + … The free electron density, in the limit that Δx goes to zero, is: n(x,t) = n₀ {1 – ds(x,t)/dx }. Assuming the ion density is always n₀, the net charge density is: ρ = q n₀ – q₀ n₀ (1 – ds/dx), ρ = q₀ n₀ ds/dx.

Maxwell’s first equation ∇•E = ρ/ε₀ reduces in one dimension to: dE/dx = ρ/ε₀ = (q₀n₀/ε₀) ds/dx. Integration yields: E = (q₀n₀/ε₀) s + any constant. Since zero displacement, s=0, corresponds to zero net charge everywhere and zero electric field, the arbitrary integration constant must be zero. The force on a single electron is: F = –q₀ E = – (q₀²n₀/ε₀) s. We see that the restoring force F is proportional to the displacement s, which we know results in harmonic oscillation. Even at 100 million Kelvin, an electron’s kinetic energy is less than 9 keV, 1.8% of its rest mass. We can therefore use non-relativistic equations. The electrons’ equation of motion is: m ∂²s/∂t² = – (q₀²n₀/ε₀) s.

The solution has the form: s = A exp{iωt} with ω² = q₀²n / mε₀. Here, I added a subscript “e” to emphasize that the charge and mass are those of electrons. The plasma frequency ω_p for an electron gas varies only with density. If plasma is disturbed, its free electrons oscillate harmonically at frequency ω_p. Now using e²=q₀²/4πε₀, we have the most commonly cited equation for plasma frequency: ω_p² = 4π e² n₀ / m_e.

In V2p.7-7, Feynman says: “This natural resonance of a plasma has some interesting effects. For example, if one tries to propagate a radio wave through the ionosphere, one finds that it can penetrate only if its frequency is higher than the plasma frequency. Otherwise the signal is reflected back. We must use high frequencies if we wish to communicate with a satellite in space. On the other hand, if we wish to communicate with a radio station beyond the horizon, we must use frequencies lower than the plasma frequency, so that the signal will be reflected back to the earth. “Another interesting example of plasma oscillations occurs in metals. In a metal we have a contained plasma of positive ions, and free electrons. The density n₀ is very high, so ω_p is also. …Now, according to quantum mechanics, a harmonic oscillator with a natural frequency ω has energy levels which are separated by the energy increment ħω. If, then, one shoots electrons through, say, an aluminum foil, and makes very careful measurements of the electron energies on the other side, one might expect to find that the electrons sometimes lose the energy ħω to the plasma oscillations. … It was first observed experimentally in 1936 that electrons with energies of a few hundred to a few thousand electron volts lost energy in jumps when scattering from or going through a thin metal foil. The effect was not understood until 1953 when Bohm and Pines showed that the observations could be explained in terms of quantum excitations of 电解质中的胶体粒子

我们接下来研究另一种受电磁力和机械力共同支配的电荷现象。

胶体粒子属于中等尺寸——以人类尺度来看是显微的，但仍包含大量单个原子。大多数液体（包括水）中的中等尺寸粒子往往会聚结，形成越来越大的团块，最终要么浮到表面，要么沉到底部。

嗯，这是电中性的中等尺寸粒子的行为。但具有净电荷的中等尺寸粒子是胶体性的；它们相互排斥，避免结块，并保持悬浮在溶液中。

如果我们加入一撮盐，情况会变得更有趣。盐溶于水并分离成正钠离子和负氯离子。同时包含正负两种离子的溶液被称为电解质。带正电的胶体粒子吸引负氯离子，并排斥正钠离子。

在《费曼物理学讲义》第二卷第7-8节中，费曼探讨了这些离子在液体中靠近每个胶体粒子时如何分布。为简化起见，我们考虑一个一维情况。他说：

“如果我们将胶体粒子想象成一个半径非常大的球体——在原子尺度上！——那么我们可以将其表面的一小部分视为平面。（每当人们试图理解一个新现象时，采用一个稍微过度简化的模型是个好主意；然后，在通过这个模型理解了问题之后，人们就更能够着手进行更精确的计算。）”

离子分布产生了一个净电荷密度，记为ρ(x)，以及一个相应的电势φ(x)，它们的关系由下式给出：

∇²φ = – ρ / ε

统计力学的玻尔兹曼定律（参见《费曼物理学讲义简化版》1B，第16章）指出，在势能U(x)中处于热平衡的物体的分布n(x)由下式给出：

n(x) = n₀ exp{–U(x)/kT}

带电荷q的离子具有势能：

U(x) = qφ(x)

正离子的密度为：

n(x) = n₀ exp{–qφ / kT}

负离子的密度为：

n(x) = n₀ exp{+qφ / kT}

正指数不用担心，因为正如我们将很快看到的，φ会随着x的增加而迅速降至零。

净电荷密度为：

ρ(x) = q n₀ (exp{–qφ/kT} – exp{+qφ/kT})

将其与前面所述的麦克斯韦第一方程结合，可得：

d²φ/dx² = (qn₀/ε) [exp{+qφ/kT}–exp{–qφ/kT}]

费曼说，这个方程可以通过将两边乘以2dφ/dx并关于x积分来求解，对于任意qφ/kT都成立。

但是，为简化起见，让我们只考虑qφ << kT的情况，这对应于中等高温下的稀溶液。在这种情况下，指数可以近似为：

exp{±qφ/kT} ≈ 1 ± qφ/kT

于是微分方程变为：

d²φ/dx² = (qn₀/ε) (2qφ/kT)

d²φ/dx² = + (2q²n₀ / εkT) φ

该方程的解是：

φ = A exp{–x/D} + B exp{+x/D}

其中 D² = εkT / 2q²n₀

这里，常数A和B被选定以满足边界条件。由于势能无限指数增长是不现实的，B必须为零。这样剩下：

φ = A exp{–x/D}

其中，A是x=0（胶体粒子表面）处的电势，D是德拜长度。该方程表明离子包围着每个胶体粒子，屏蔽其电荷。离子外壳的厚度由德拜长度表征，德拜长度随温度升高而增加，随离子浓度增加而减小。

由σ（胶体粒子的表面电荷密度）我们可以计算A。在一维情况下，胶体粒子表面的电场与均匀带电平面的电场相同。

E(x=0) = σ / ε

我们也知道，在静电学中E=–∇φ。在一维情况下，这意味着：

E(x) = – ∂φ(x)/∂x = + φ / D

E(0) = A / D

因此，A = σ D / ε

所以 φ(x) = (σD/ε) exp{–x/D}

回忆 D² = εkT / 2q²n₀

我们看到，D随着盐浓度n₀的增加而减小。对于更咸的溶液，每个胶体粒子周围的离子外壳更薄，峰值电势φ(0)降低。在足够高的盐离子浓度下，离子外壳会很大程度上中和胶体粒子。费曼说，胶体粒子随后可以相互附着、聚结，并从溶液中沉淀出来。这被称为盐析胶体。

蛋白质分子也会发生类似效应。在《费曼物理学讲义》第二卷第7-10节中，费曼说：

“蛋白质分子是一条长而复杂且柔性的氨基酸链。分子上带有各种电荷，有时存在净电荷，例如负电荷，沿链分布。由于负电荷之间的相互排斥，蛋白质链保持伸展状态。同时，如果溶液中存在其他类似的链分子，它们也会因为相同的排斥效应而保持分离。因此，我们可以在液体中得到链分子的悬浮液。但是，如果我们向液体中加盐，我们改变了悬浮液的性质。当盐加入溶液，减小了德拜距离，链分子就能相互靠近……” ne another, and can also coil up. If enough salt is added to the solution, the chain molecules will precipitate out of the solution. There are many chemical effects of this kind that can be understood in terms of electrical forces.

Field from a Grid In many different applications, we want to produce the most uniform field using the least material. One example is uniformly illuminating a large room with the fewest long fluorescent tubes. Another example is a vacuum tube grid. The grid must establish a uniform field to accelerate electrons, but it must also allow those electrons to pass through the grid with minimal interference. Let’s find the field from an array of infinitely long, parallel, charged wires that are each a distance d from its neighbors. Figure 34-4 shows this array. Each black dot represents the cross-section of an infinitely long wire that is perpendicular to the screen.

Figure 34-4 Field of Wire Array Here, z is the distance below the array at which we will evaluate the field, and x is the horizontal axis with x=0 at the center of one specific wire. We want to determine how uniform the field is at distance z for wire spacing d. Since the array repeats horizontally at distance d, the field must also repeat over that distance. In Feynman Simplified 1D, Chapter 45, we found that any physically realistic periodic function can be represented by a Fourier series, a linear combination of sinusoidal functions. Since the field must peak near each wire, its x-dependence must be of the form: E(x,z) = Σ F(z) cos(n 2π x/d)

n n Since the center of the mth wire is at x=md, each cosine in the above sum peaks at the center of each wire. F(z) is the Fourier coefficient of the nth cosine term. The summation runs from n=0 to n=∞. Since the wires are infinitely long, there can be no variation of the field along their length. Except at the wires themselves, the E field satisfies an empty-space 2-D Laplace equation: 0 = ∂2E/∂x2 + ∂2E/∂z2 Putting the Fourier series representation into the Laplace equation yields: 0 = Σ C cos(2nπx/d)

n n with C = –(2nπ/d)2F +∂2F/∂z2 n n n The summation can be zero only if each C is zero. This is because two cosine functions with different frequencies do not have the same values everywhere. If that is unclear, we know from Feynman Simplified 1D, Chapter 45, that the Fourier series for function f=0 has coefficients that are all zero. We thus have: (2nπ/d)2 F = ∂2F/∂z2 n n F = A exp{–z/D}} n n with D = d / 2nπ Here, the A are arbitrary constants chosen to match boundary conditions. We see that the first harmonic, the n=1 term in the Fourier series, decreases by a factor of exp{–2π} = 0.0019 each time z increases by distance d. This term rapidly becomes negligible. The higher harmonics decrease even faster. At even a moderate distance below the array, the Fourier series is dominated by the zeroth harmonic, n=0, and E becomes: E(x,z) = A This matches the electric field from a uniformly charged plane. This analysis shows that even a sparse grid effectively establishes a uniform potential. Such grids are often used to shield electronics from external fields.

## Chapter 34 Review: Key Ideas

• Any function F of a complex variable β can be separated into its real and imaginary parts, as: F(β) = U(x,y) + i V(x,y)

For any physically realistic function F, the real functions U and V satisfy the relations: ∂U/∂x = + ∂V/∂y ∂V/∂x = – ∂U/∂y They also satisfy the 2-D Laplace equation: 0 = ∂2U/∂x2 + ∂2U/∂y2 = ∂2V/∂x2 + ∂2V/∂y2 Curves of constant U and curves of constant V always cross at 90 degrees. U and V are thus both solutions to some 2-D electrostatic problem.

• In Plasma, the state of ionized gaseous matter, atoms separate into a sea of free electrons and a sea of ionized atoms. Plasma is the most common state of matter throughout the universe. Stars are comprised of plasma, and so is Earth’s ionosphere. If plasma is disturbed, its free electrons oscillate harmonically about their equilibrium positions with plasma frequency ω, given by: ω2 = q2n / mε = 4πe2n /m p e 0 e 0 0 e Here, q and m are the electron charge and mass, n is the plasma equilibrium density, and e2=q2/4πε.

e e 0 e 0 • Colloidal particles remain suspended in ion-free liquid because they are charged and repel one another, thus preventing coagulation and precipitation. But, colloidal particles in an electrolytic solution become cloaked with oppositely charged ions. The potential ø at distance x from a colloidal particle’s surface is: ø(x) = (σD/ε) exp{–x/D} D2 = εkT / 2q2n 0 0 Here, D is the Debye length, σ is the colloidal particle’s surface charge density, and n is the ion density at x=0. If the ion density is high enough, colloidal particles are effectively neutralized. They can then coagulate and precipitate. This is salting out a colloid.

• The electric field from an array of infinitely long, parallel, charged wires, with uniform spacing d, is: E(x,z) = Σ F(z) cos(n 2π x/d)

n n Here, z is the distance from the array, x is the di The electric field E has the same phase across the array perpendicular to the wires, and F_n is the Fourier series coefficient of the nth term in the sum from n=0 to n=∞. Field E satisfies the 2-D Laplace equation (except at the wires), and has this solution: F_n = A_n exp{–z/D} with D = d / 2nπ.

The n=1 term decreases by a factor of exp{–2π}=0.0019 each time z increases by distance d, and rapidly becomes negligible. Terms for larger n decrease even faster. At even a moderate distance from the array, the Fourier series is dominated by the zeroth harmonic, n=0, and E becomes: E(x,z) = A.

• A particle with charge q, in a magnetic field without an electric field, orbits in a circle of radius R in the plane perpendicular to B, and simultaneously moves at constant speed parallel to B. For v* and p* being the components of velocity and momentum within the plane of the circle, radius R is given by: R = p* / (qB). If B and q are known, measuring R determines p*.

• Electrostatic and magnetostatic lenses focus charged particles with fields that are zero on the symmetry axis and increase linearly with off-axis displacement.

• The Rayleigh criterion for the diffraction limit θ_min of an optical system’s angular resolution is: θ_min ~ λ / W. Here, λ is the wavelength of the imaging particles, and W is the width of the limiting aperture. The Rayleigh criterion for the smallest resolvable displacement between two points is: δ = λ / 2tanβ, where 2β is the angle subtended by aperture W at the imaged points.

• Dipole magnets can provide both vertical and radial weak focusing of an orbiting particle beam if the field index n is within the following range: –1 < n = (dB/B) / (dR/R) < 0. Properly spaced quadrupole magnets of alternating gradients can provide both vertical and radial strong focusing.

• In constant E and B fields that are mutually orthogonal, a charged particle initially moving along the electric field drifts in that direction at constant speed v_drift = E/B, and rotates in the plane perpendicular to B. The curved path that results is called a cycloid.

• Crystals are solids with highly ordered structures formed by repeating patterns of atoms. The unit cell is the smallest repeating atomic pattern. The six lattice parameters are the three angles between the three axes of the unit cell, and the three shortest repetition distances along those axes. Crystal growth can be accelerated by imperfections that expose more unit cell sides at the crystal surface. Crystal dislocations arise from missing atoms, impurities, mechanical damage to the surface, or other imperfections. The lattice distorts near a dislocation, but eventually restores its normal structure. Dislocations propagate freely in perfect crystals, but are stopped by grain boundaries. Small grains with many boundaries make metals harder and stronger.

• The index of refraction n of any material of any density is given by: α = (q^2/mε_0) Σ_i f_i /(–ω^2 +iωµ_i +ω_i^2); n^2 = 1 + α N / (1 – αN/3); 3(n^2–1)/(n^2+2) = α N. Here, α is the atomic polarizability, N is the number of active electrons per unit volume, q and m are the electron’s charge and mass, and ω is the frequency of the incident electric field. The summation is over all electron excited states. Excited state i has natural frequency ω_i, damping force mω_iµ_i, and weighting factor f_i. Index n is complex in general; we separate its real and imaginary parts as: n = n_r – in_i.

• Inside a material body, the electric field is: E = E_0 exp{iω(t–zn_r/c)} exp{–zn_iω/c)}. The field oscillates, moving toward +z at velocity c/n_r with exponentially decreasing amplitude. The intensity absorption coefficient β equals 2n_iω/c, meaning that the intensity decreases as exp{–βz}.

• In metals, the actions of free electrons dominate, and the refractive index becomes: n^2 = 1+ σ / {iωε_0 (iωτ +1) }. Here, the metal’s conductivity is σ, and its mean collision time is τ. At low frequencies, below 10^12 cycles/sec in copper, the index approaches: n = (1–i) √(σ/2ωε_0). The field decreases exponentially as exp{–z/δ} with: skin depth δ = √(2ε_0c^2/σω). In copper, δ=16.7 cm /√ω (radians/sec), which is 6.66 microns at 10 GHz. The plasma frequency ω_p=√(Nq^2/mε_0). At frequencies greater than ω_p, the index is: n^2 = 1 – ω^2 / ω_p^2. The index is real and the metal becomes transparent. Since n<1, the phase velocity is greater than c. But since phase velocity is not the speed of any real entity, this does not contradict special relativity. At frequencies less than ω_p, the index is complex. Waves propagate with real frequencies, and exponentially decreasing magnitudes.

• For sinusoidal waves, the gradient Ď is effectively a vector product. For E(r,t) = E exp{iωt – ik•r}; Ď E = –ik E; Ď•E = –ik•E; Ď×E = –ik×E; Ď×E = – ∂B/∂t; –ik×E = –iωB; B = k×E / ω; E = B×k (c^2/ωn^2).

• Boundary conditions are essential inputs to the solution of any differential equation. At a sharp boundary at the x=0 plane, x-derivatives dominate all others and Maxwell’s equations reduce to: ∂E_y/∂y – ∂E_z/∂z = –∂B_x/∂t; εE_x = ε_0E_0.

2 (∂B/∂y – ∂B/∂z) = ∂P/∂t + ε∂E/∂t ∂ {εE+P} /∂x = 0 ∂ {E} /∂x = 0 ∂ {B} /∂x = 0 ∂ {B} /∂x = 0 ∂ {B} /∂x = 0 This means the value of each quantity in { }’s is the same for –ε<x<+ε, for infinitesimal ε.

• Red dyes transmit red light with minimal attenuation, while preventing the transmission of red’s complementary color: green. At the frequency of green light, the refractive index of a red dye has a very large imaginary part. Red dyes do not absorb green light as much as they strongly reflect it. Red ink and paint do the opposite; they strongly reflect red light and absorb other colors.

• Any function F of a complex variable β can be separated into its real and imaginary parts, as: F(β) = U(x,y) + i V(x,y). For any physically realistic function F, the functions U and V satisfy the relations: ∂U/∂x = + ∂V/∂y, ∂V/∂x = – ∂U/∂ Great science to enjoy. I hope to help change that and bring Feynman’s genius to a wider audience. Please let me know how I can make Feynman Simplified even better — contact me through my WEBSITE. While you’re there, check out my other books and sign-up for my newsletters.

Printed Books, each top-rated by Amazon readers: Everyone's Guide to Atoms, Einstein, and the Universe Can Life Be Merely An Accident?

A World Without Einstein

The Everyone's Guide Series of Short eBooks Einstein: His Struggles, and Ultimate Success, plus Special Relativity: 3 Volumes, A to Z General Relativity: 4 Volumes, from Introduction to Differential Topology Quantum Mechanics: 5 Volumes, from Introduction to Entanglement Higgs, Bosons, & Fermions… Introduction to Particle Physics Cosmology Our Universe: 5 Volumes, everything under the Sun Our Place in the Universe: a gentle overview Black Holes, Supernovae & More We are Stardust Searching for Earth 2.0 Smarter Energy Timeless Atoms Science & Faith

Table of Contents

## Chapter 25 Waveguides

## Chapter 26 Relativistic Electrodynamics

## Chapter 27 Transformation of Fields

## Chapter 28 Energy & Momentum of Fields

## Chapter 29 Electromagnetic Mass

## Chapter 30 Particles in Fields

## Chapter 31 Crystals

## Chapter 32 Refraction in Dense Matter

## Chapter 33 Reflection & Transmission

## Chapter 34 Clever Tricks

## Chapter 35 Review of 2C

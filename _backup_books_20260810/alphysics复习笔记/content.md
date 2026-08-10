# ALphysics复习笔记

> 来源文件：pre_ALphysics复习笔记.txt
> 字符数（约）：48968
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

This document is regularly updated. The latest version can be accessed at https://ronaldobutrus.com/revisionnotes.html. Latest update: 10 April 2022.

Ronaldo Butrus

1 PHYSICAL QUANTITIES AND UNITS

## 1.1 Physical quantities

- All physical quantities consist of a numerical magnitude and a unit.

## 1.2 SI units

- The main SI base quantities and their units are: mass (kg), length (m), time (s), current (A), temperature (K).

- Units of other quantities are derived from the base units above. E.g. speed = distance / time = [m] / [s] = [m s⁻¹].

- To check the homogeneity of equations (if they are equivalent), you can use the units of the different quantities: E.g. to compare mgh and ½mv²: mgh = [kg] [m s⁻²] [m] = [kg m² s⁻²]

½mv² = [kg] ([m s⁻¹])² = [kg m² s⁻²]

Both sides of the equation are identical, meaning we can use both equations for energy.

Prefix Symbol Value pico p ×10⁻¹² nano n ×10⁻⁹ micro μ ×10⁻⁶ milli m ×10⁻³ centi c ×10⁻² deci d ×10⁻¹ kilo k ×10³ mega M ×10⁶ giga G ×10⁹ tera T ×10¹²

## 1.3 Errors and uncertainties

- Types of errors: o systematic errors: an error caused by an inaccuracy in the system, e.g. calibration.

o random errors: an error caused by a lack of precision, changes in experimental conditions or value judgments in measurements. Repeat readings reduce the effect of random error on the mean.

- Accuracy and precision: o accuracy: how close to the ‘real value’ a measurement is o precision: how close measurements of the same value are to each other - No measurement can be made to absolute precision; there is always some uncertainty: o absolute uncertainty: a numerical uncertainty, e.g. 2.5±0.1 s o percentage uncertainty: an uncertainty expressed as a percentage of the reading, e.g. for 2.5±0.1 s, this would be 4%.

- Combining uncertainties: o for quantities that are added or subtracted: add absolute uncertainties o for quantities that are multiplied or divided: add percentage uncertainties o for quantities that are exponentiated: multiply percentage uncertainty by power

## 1.4 Scalars and vectors

- Scalar quantities: magnitude only, e.g. speed, mass, energy - Vector quantities: magnitude and direction, e.g. velocity, force, acceleration - Adding and subtracting coplanar vectors: - Resolving vectors to represent them as two perpendicular components:

2 KINEMATICS

## 2.1 Equations of motion

- Distance is a measure of length along a path travelled by a particle.

- Displacement is a measure of change of position, given by magnitude and direction.

- Speed is a measure of how fast a particle is moving.

- Velocity is speed in a given direction.

- Acceleration is the rate of change of velocity.

- Displacement is equal to the area under a velocity-time graph.

- Velocity is equal to the gradient of a displacement-time graph.

- Acceleration is equal to the gradient of a velocity-time graph.

v = u + at (derived from velocity = displacement / time)

a = (rate of change of velocity)

s = ut + ½at² (derived from area under uniform acceleration v-t graph)

s = vt − ½at² (derived from area under uniform acceleration v-t graph)

v² − u² = 2as (derived from v = u + at where a = (v - u)/t)

- An experiment to determine the acceleration of free fall using a falling object: o Attach electromagnet with ball-bearing to a clamp stand and place a trapdoor underneath the ball.

o Connect a timer to the electromagnet and trap door.

o Measure distance h between the bottom of the electromagnet and the top of the trapdoor.

o When the current to the electromagnet switches off, the ball drops and the timer starts.

o When the ball hits the trapdoor the timer stops.

o Record the time t and repeat the experiment for different values of h.

o Plot a graph of 2s against t².

o Draw a straight line of best fit.

o The acceleration is equal to the gradient of the line of best fit.

- In motion due to a uniform velocity in one direction and a uniform acceleration in a perpendicular direction, the components of the velocity can be treated separately.

- Therefore, acceleration in one direction does not affect the velocity in the perpendicular direction.

- This is an example of projectile motion.

3 DYNAMICS

## 3.1 Momentum and Newton’s laws of motion

- Mass is the property of an object that resists change in motion.

- Linear momentum is given by the product of mass and velocity.

p = mv - Force is the rate of change of momentum.

F = Δp / Δt Newton’s First Law Every object continues in its state of rest, or with uniform velocity, unless acted on by a resultant force.

Newton’s Second Law For an object of constant mass, its acceleration is directly proportional to the resultant force applied to it.

F = ma Newton’s Third Law Whenever one object exerts a force on another, the second object exerts an equal and opposite force on the first.

- Weight is the effect of gravitational field on a mass.

W = mg

## 3.2 Non-uniform motion

- Frictional forces and viscous/drag forces (such as air resistance) act in the direction opposite to the direction of motion.

- When an object falls in a uniform gravitational field with air resistance: o speed increases o force due to air resistance increases o until it is equal and opposite to weight o the resultant force approaches zero o the object reaches its terminal (constant) velocity

## 3.3 Linear momentum and its conservation

Principle of Conservation of Momentum If no external force acts on a system, the total momentum of the system remains constant.

- In collisions, the momentum of a system is always conserved but some change in kinetic energy may take place.

- Collisions can be: o perfectly elastic: relative speed of approach is equal to relative speed of separation o inelastic: relative speeds of approach and separation differ o perfectly inelastic: maximum amount of kinetic energy is lost (particles coalesce)

4 FORCES, DENSITY AND PRESSURE

## 4.1 Turning effect of forces

- The weight of an object may be taken as acting on a single point known as its centre of gravity.

The moment of a force is given by the product of the force and the perpendicular distance of the line of action of the force to the pivot.

T = Fd where T is the moment of the force, F is the force, and d is the perpendicular distance of the line of action of the force to the pivot.

A couple is a pair of forces that acts to produce rotation only.

The torque of a couple is given by the product of one of the forces and the perpendicular distance between the two forces.

T = Fd where T is the torque of the couple, F is (one) force, and d is the perpendicular distance between the two forces.

## 4.2 Equilibrium of forces

Principle of Moments For a body in rotational equilibrium, the sum of the clockwise moments about the point is equal to the sum of the anticlockwise moments about that point.

A system is in equilibrium if: - there is no resultant force - there is no resultant torque

A vector triangle can be used to show three coplanar forces (joined tip to tail) are in equilibrium.

## 4.3 Density and pressure

- Density is measured in mass per unit volume (i.e. kg m⁻³).

- Pressure is measured in force per unit area (i.e. N m⁻² or Pascal (Pa)).

- Hydrostatic pressure is given by: Δp = ρgΔh where Δp is the difference in hydrostatic pressure (Pa), ρ is the density (kg m⁻³), g is the gravitational field strength (N kg⁻¹), and Δh is the difference in height (m).

- Upthrust is a force acting on an object in a fluid due to a difference in hydrostatic pressure.

- This is equal and opposite to the weight of the fluid displaced by the object.

Archimedes’ Principle: F = ρgV where F is the upthrust (Pa), ρ is the density (kg m⁻³), g is the gravitational field strength (N kg⁻¹), and V is the volume of the fluid displaced (m³).

5 – Work, Energy & Power

## 5.1 Energy conservation

Work done is the energy transferred by moving a point in the direction of a force applied at that point, given by the product of the force and displacement.

W = Fs

Principle of Conservation of Energy Energy cannot be created or destroyed. It can only be converted from one form to another.

- The efficiency of a system is the ratio of useful energy output from the system to the total energy input.

- Power is work done per unit time.

P = W / t Using the equation for work done: W = Fs So, P = (Fs) / t Since s / t = v, where v is velocity, then: P = Fv (power needed to move force F at constant velocity v)

## 5.2 Gravitational potential energy and kinetic energy

For gravitational potential energy changes in a uniform gravitational field: W = Fs W = (mg)Δh ΔE = mgΔh

Consider an object of mass m moving with constant acceleration a where F = ma.

The velocity of the object changes from u to v in a distance s.

v² - u² = 2as Let u = 0: v² - 0² = 2as E = ½mv² Multiply both sides by m: ½mv² - ½mu² = ½(ma)s * 2 = Fs W = ½m(v² - u²)

6 – Deformation of Solids

## 6.1 Stress and Strain

- Deformation is caused by tensile or compressive forces.

- Terms relating to deformation: - load: force exerted on a body - extension: increase in length due to load - compression: decrease in length due to load - limit of proportionality: the point at which Hooke’s law is no longer true when stretching a material

- Hooke’s Law: the extension of a body is directly proportional to the applied force.

F ∝ x ⇒ F = kx where F is the force (N), k is the spring constant (N m⁻¹), and x is the extension (m).

- Stress, strain and Young modulus: - stress (σ): force per unit cross-sectional area of the wire (Formula: stress = F / A, Units: Pa)

- strain (ε): extension per unit of the unloaded length of the wire (Formula: strain = x / L, Units: none)

- Young modulus (E): stress / strain (Formula: E = (F / A) / (x / L) = FL / (Ax), Units: Pa)

- Determining the Young modulus of a metal in the form of a wire: - clamp one end of the wire between two wooden blocks held by a G-clamp - let the other end hang from a horizontally level pulley - attach very small weight to provide some tension for initial measurements - place a fixed ruler on the table adjacent to the wire - attach a tape marker to the wire - record the current distance along the ruler - incrementally add weights and record changes in length (and therefore the extension for that load) until the wire breaks (for breaking stress and strain values)

- plot a strain (x) – stress (y) graph - the gradient of the linear region is the best estimate for the Young modulus of the wire - a line of worst fit can be used to calculate an uncertainty in the value

## 6.2 Elastic and plastic behaviour

- Types of deformation: - elastic: spring will return to its original length when the load is removed - plastic: spring will not return to its original length when the load is removed - elastic limit: the point at which the spring ceases to show proportionality (i.e. the deformation transitions from elastic to plastic)

The area under a force-extension graph within its limit of proportionality represents the work done: average force = ½kx distance = x E = ½kx * x ⇒ E = ½kx²

7 – Waves

## 7.1 Progressive waves

- Wave motion: - in ropes: swaying a rope from side to side illustrates a transverse wave - in springs: sending impulses illustrates a longitudinal wave, and swaying from side to side illustrates a transverse wave - in ripple tanks: ripples on the water surface illustrate transverse waves

- Terms relating to waves: - displacement: distance of a particle in a wave from its equilibrium position - amplitude: maximum displacement in a wave from its equilibrium position - phase difference: the fraction of a cycle that passes between an object being at maximum displacement in a given direction and another object being at maximum displacement in that direction - period (T): time taken for one wavelength to pass a point on a wave, in seconds (s)

- frequency (f): number of waves that pass a given point in one second, in Hertz (Hz)

- wavelength (λ): distance between one point and the next corresponding point on a wave, in metres (m)

- speed: wave speed, v = distance / time = λ / T = fλ ⇒ v = fλ

- A cathode-ray oscilloscope (CRO) can be used to measure potential difference and short time intervals: - a potential difference applied to the x and y inputs controls the movement of the trace in the horizontal and vertical directions respectively - y-sensitivity is measured in volts per centimetre (V cm⁻¹)

- the rate at which the time-base voltage drags the spot across the screen is measured in either seconds per division (s div⁻¹) or divisions per second (div s⁻¹)

- E.g. assuming a y-sensitivity of 2 V div⁻¹ and a time-base of 0.05 s div⁻¹: Amplitude of larger pulse is 2 divisions, so 2×2 = 4 V.

Amplitude of smaller pulse is 1 division, so 1×2 = 2 V.

Time interval between the two larger pulses is 4 divisions, so 4×0.05 = 0.2 s.

Frequency, f = 1 / period = 1 / 0.2 = 5 Hz

- Energy is transferred by a progressive wave, e.g. water waves on the sea carry energy from where they form to where they crash onto the shore.

- The intensity of a wave is the energy transmitted per unit time per unit area at right angles to the wave velocity.

intensity = energy / (time × area) I = P / A in watts per metre squared (W m⁻²)

intensity ∝ (amplitude)². I ∝ x².

## 7.2 Transverse and longitudinal waves

- Types of waves: - transverse: oscillations perpendicular to direction of energy transfer - longitudinal: oscillations parallel to direction of energy transfer

## 7.3 Doppler effect for sound waves

- Doppler effect: when a source of sound waves moves relative to a stationary observer, the observed frequency is different from the source frequency.

f = (c / (c + v_s)) f_s (for a stationary observer)

where f_s is the source frequency, v_s is the source velocity, c is the wave velocity, and f is the observed frequency.

The directional component of the velocities must be relative.

## 7.4 Electromagnetic spectrum

- All electromagnetic waves are transverse waves that travel with the same speed c in free space where c ≈ 3×10⁸ m s⁻¹.

Type of radiation | Approximate wavelengths in free space (metres)

--- | --- Radio waves | 10⁰ Microwaves | 10⁻³ Infrared | 10⁻⁵ Visible light | 10⁻⁷ Ultraviolet | 10⁻⁸ X-rays | 10⁻¹⁰ Gamma rays | 10⁻¹⁵

- Wavelengths in the range 400 – 700nm in free space are visible to the human eye.

## 7.5 Polarisation

- Transverse waves are polarised if they are vibrating in one plane only.

- Polarising filters only transmit waves that are polarised parallel to their transmission axis.

Malus’ Law: I = I₀ cos²θ where I₀ is the maximum intensity (W m⁻²), I is the intensity of the transmitted light (W m⁻²), and θ is the angle between the polarised light and the transmission axis.

8 – Superposition

## 8.1 Stationary waves

- Principle of superposition When two or more waves cross at a point, the displacement at that point is equal to the sum of the displacements of the individual waves.

- Stationary waves are formed when two waves of the same type and frequency, travelling in opposite directions, meet.

Stationary waves in a stretched string: Stationary waves using microwaves: - the microwave (food-heating device) generates standing microwaves - antinodes have a lot of energy - this energy is transferred to the food - the dish rotates so that the antinodes are exposed to the food at different times to ensure even heating.

odes can heat the food as uniformly as possible.

Stationary waves in air columns:

8 – Superposition

## 8.2 Diffraction

- Diffraction is the spreading of waves after passing through a gap.

- Diffraction can be demonstrated by observing water in a ripple tank: This apparatus can be used to observe the movement of water waves in a ripple tank. Placing obstacles will cause diffraction to occur.

- The gap size must be comparable to the wavelength for diffraction to occur.

## 8.3 Interference

- Interference is when two waves of the same type meet and their displacements add or subtract: o if they are in phase the amplitudes are added (constructive interference) o if they are in antiphase the amplitudes are subtracted (destructive interference).

- Coherent waves have the same frequency and a constant phase difference.

Interference patterns in sound waves: Interference patterns in water waves: Interference patterns in microwaves: Interference patterns in light waves:

## 8.4 The diffraction grating

- To find the maximum number of fringes, set θ to 90.

- Remember to account for the middle fringe and those on the other side.

9 – Electricity

## 9.1 Electric current

- An electric current is a flow of charge carriers.

- The charge on charge carriers is quantised, i.e. it only exists in discrete amounts.

𝑄 = 𝐼𝑡 - For a current-carrying conductor: 𝐼 = 𝐴𝑛𝑣𝑞 where 𝐼 is the current through the conductor, 𝐴 is the cross-sectional area, 𝑛 is the number density of charge carriers, 𝑣 is the average drift velocity, 𝑞 is the charge of one electron.

## 9.2 Potential difference and power

- The potential difference across a component is the energy transferred per unit charge. 𝑉 = 𝑄/𝑡 - Power: 𝑃 = 𝑉𝐼 = (𝐼𝑅)𝐼 = 𝐼²𝑅 = 𝑉²/𝑅.

## 9.3 Resistance and resistivity

- Resistance is the opposition to the flow of electrons within a material, expressed as a ratio of the potential difference 𝑉 across a conductor to the current 𝐼 in it. 𝑉 = 𝐼𝑅 - Ohm’s Law: for a metallic conductor at a constant temperature, the current in the conductor is proportional to the potential difference across it.

Type of conductor | 𝐼-𝑉 graph | Explanation metallic conductor at constant temperature | At a constant temperature, current is directly proportional to potential difference. 𝐼 ∝𝑉 (obeys Ohm’s Law)

semiconductor diode | The diode conducts when the current is in the direction of the arrowhead on its circuit symbol. It has a very high resistance for small potential differences and its resistance decreases constantly after a set potential difference. They are not directly proportional.

filament lamp | As potential difference increases: - current increases - temperature increases - atoms in metal filament vibrate more so resist the passage of electrons more - resistance increases

- Resistivity is a property of a metal that defines how strongly it resists the flow of current. For a given current-carrying conductor: 𝑅 = 𝜌𝐿/𝐴 where 𝑅 is the resistance, 𝜌 is the resistivity, 𝐿 is the length, 𝐴 is the cross-sectional area.

- For a light-dependent resistor (LDR): o as light intensity increases o resistance decreases.

- For a thermistor (with a negative temperature coefficient): o as temperature increases o resistance decreases.

10 – D.C. Circuits

## 10.1 Practical circuits

- A single electrical energy source which uses chemical reactions to produce a current: cell - Multiple cells: battery - A device used for making or breaking electric current through a circuit: switch - A wire providing a low resistance path to the ground (so that in the event of a fault current passing through a metal case will pass to the ground instead of through a person): earth wire - Supplies power to at least one electrical load: power supply - A device that uses electromagnets to produce a repetitive sound: buzzer - A device that makes a sound when an electric current passes through it: bell - A power supply that uses an alternating current: AC power supply - A point where three or more circuit paths meet: junction - A device that converts sound waves into electrical signals: microphone - A device that converts electrical signals into sound waves: loudspeaker - A device for producing illumination: lamp - A resistor whose resistance does not change with changes in voltage or temperature: fixed resistor - A device which produces a rotational force when a current passes through it: motor - A device that produces a current when a rotational force is applied to it: generator - A resistor whose resistance can be adjusted: variable resistor - A resistor whose resistance decreases as temperature increases: NTC thermistor - Used to measure the magnitude of a current through a component: ammeter - Used to measure potential difference across a component: voltmeter - A resistor whose resistance decreases as light intensity increases: LDR - A device that converts electric current into heat: heater - Used to measure the magnitude and direction of current through a component: galvanometer

- The electromotive force (e.m.f.) of a source is the energy transferred per unit charge in driving charge around a complete circuit.

- Internal resistance is the resistance between the terminals of a power supply.

- Terminal potential difference is the potential difference across the terminals of a cell when a current is being delivered.

By conservation of energy, the electromotive force of a source is made up of: o a p.d. across an external resistor (load) of resistance 𝑅 and o a p.d. across an internal resistance 𝑟 𝐸 = 𝑉 + 𝑉 where 𝑉 = 𝐼𝑅 and 𝑉 = 𝐼𝑟, so 𝐸 = 𝐼𝑅 + 𝐼𝑟.

- A power supply with a high internal resistance will result in a lower terminal potential difference, and vice versa.

- A battery delivers maximum power to a circuit when the load resistance of the circuit is equal to the internal resistance of the battery.

Load resistance vs. Power dissipated in load r Load resistance, R /Ω

## 10.2 Kirchhoff’s laws

- Kirchhoff’s first law: the sum of the currents entering a junction in a circuit is always equal to the sum of the currents leaving the junction. 𝐼 = 𝐼 + 𝐼 + 𝐼 + ⋯ - Kirchhoff’s second law: the sum of the electromotive forces in a closed circuit is equal to the sum of the potential differences. 𝑉 = 𝑉 + 𝑉 + 𝑉 + ⋯ or 𝐸 = 𝐼𝑅 + 𝐼𝑅 + 𝐼𝑅 + ⋯ - Two or more resistors in series: 𝑉 = 𝑉 + 𝑉 + 𝑉 + ⋯ ⇒ 𝐼𝑅 = 𝐼𝑅 + 𝐼𝑅 + 𝐼𝑅 + ⋯ ⇒ 𝑅 = 𝑅 + 𝑅 + 𝑅 + ⋯ - Two or more resistors in parallel: 𝐼 = 𝐼 + 𝐼 + 𝐼 + ⋯ ⇒ 𝑉/𝑅 = 𝑉/𝑅 + 𝑉/𝑅 + 𝑉/𝑅 + ⋯ ⇒ 1/𝑅 = 1/𝑅 + 1/𝑅 + 1/𝑅 + ⋯

## 10.3 Potential dividers

- 𝑉 = 𝑉 * (𝑅 / (𝑅 + 𝑅))

As 𝑅 increases, 𝑅 consumes a larger proportion of the total potential difference, so 𝑉 increases.

As 𝑅 increases, 𝑅 consumes a smaller proportion of the total potential difference, so 𝑉 decreases.

- How a potential divider circuit works: o a fixed resistor and a variable resistor are connected in series o the variable resistor may take the form of an LDR, thermistor or similar o a component can be connected across one of the resistors (𝑉 ) o the potential difference across this component can be adjusted as needed.

- Thermistors and light-dependent resistors can be used instead of a regular variable resistor to provide a potential difference that is dependent on temperature and light intensity.

- This can be useful in systems relating to heating, streetlighting or even phone brightness sensors.

- Potentiometer: o a device that behaves as an adjustable potential divider o wiper controls how much of the resistor is ‘used’ and therefore the resistance o output voltage depends on the resistance o can be used as a means of comparing potential differences (using a galvanometer)

- A galvanometer is an analogue current-measuring instrument which shows both the magnitude and direction of the current flowing through it.

- A galvanometer can be used with a potential divider in null methods to compare potential differences: o the two-way switch is set to A o the wiper position is adjusted along a resistive wire until the galvanometer reads zero o at this point (balance point), the p.d. across 𝑙 is ‘balanced’ by the e.m.f. of A o there is no current flowing through cell A o the same process is repeated for B o resistance is directly proportional to the length of the resistive wire o therefore the ratios of e.m.f.’s and lengths are equal: 𝑁! / 𝑁" = 𝐾! / 𝐾"

11 – Particles Physics

## 11.1 Atoms, nuclei and radiation

- The α-scattering experiment: Observations | Conclusions most went straight through or were deviated by small angles (<10°) | most of atom is empty space very few were deviated by large angles (> 90°) | atom has a small, dense, positively charged nucleus 90°) mass and charge concentrated in (very small) nucleus - Nuclear model of the atom: mass and positive charge concentrated in nucleus nucleus is about 1/10000 size of atom nucleus made up of protons and neutrons electrons orbit nucleus at fixed energy levels nucleon number = no. of protons + neutrons proton number = no. of protons - Isotopes are forms of the same element with different numbers of neutrons in their nuclei.

- A nuclide is a class of nuclei that have a particular nucleon and proton number.

- Nuclides can be notated as ^A_Z X where A is the nucleon number and Z is the proton number.

- In nuclear processes, the nucleon number and charge are conserved.

- An antiparticle has the same mass but opposite charge to the corresponding particle.

- A positron is the antiparticle of an electron.

Type of radiation | Composition | Mass | Charge α | helium nucleus (2 protons + 2 neutrons) | 4u | +2e β⁻ | electron | u/2000 | -e β⁺ | positron (positive electron) | u/2000 | +e γ | short-wavelength electromagnetic waves | 0 | 0 - The unified atomic mass unit (u) is a unit of mass where 1u = 1.66×10⁻²⁷ kg.

- The force responsible for decay is weak nuclear force.

- The unified atomic mass unit (u) is a unit of mass where 1u = 1.66×10⁻²⁷ kg.

- The force responsible for decay is weak nuclear force.

11 – Particle Physics Type of decay | Nature | General equation | Energy α | nucleus emits two protons and two neutrons | ^A_Z X → ^{A-4}_{Z-2} Y + α | discrete energies that are equal for a particular radioactive nuclide | | ^{238}_{92} U → ^{234}_{90} Th + α | β⁻ | a neutron transforms into a proton, electron and antineutrino | ^A_Z X → ^A_{Z+1} Y + e⁻ + ν̅ + energy | continuous range of energies because even though the total decay energy is constant for a particular nuclide, the amount of energy transferred to the (anti)neutrino varies | | ^{214}_{82} Pb → ^{214}_{83} Bi + e⁻ + ν̅ + energy | β⁺ | a proton transforms into a neutron, positron and neutrino | ^A_Z X → ^A_{Z-1} Y + e⁺ + ν + energy | | | ^{30}_{15} P → ^{30}_{14} Si + e⁺ + ν + energy |

## 11.2 Fundamental particles

- A quark is a fundamental particle and there are six flavours (types) of quark.

- Antiquarks have the opposite charge of their respective quark.

QUARKS flavour | charge up (u) | +2/3 e down (d) | -1/3 e strange (s) | -1/3 e charm (c) | +2/3 e bottom (b) | -1/3 e top (t) | +2/3 e

ANTIQUARKS flavour | charge anti-up (ū) | -2/3 e anti-down (d̅) | +1/3 e anti-strange (s̅) | +1/3 e anti-charm (c̅) | -2/3 e anti-bottom (b̅) | +1/3 e anti-top (t̅) | -2/3 e - Protons and neutrons are not fundamental particles because they are composed of quarks.

proton: u u d charge: +e +e -e = +e 1 1 1 neutron: u d d charge: 0 +e -e -e = 0 1 1 1 - Subatomic particles are categorised as: hadrons: affected by strong nuclear force (holds protons and neutrons together)

in the nucleus (protons and neutrons)

made up of quarks baryons consist of three quarks mesons consist of one quark and one antiquark leptons: not affected by strong force not in the nucleus (electrons and antineutrinos)

are fundamental particles

12 – Motion in a Circle 12 MOTION IN A CIRCLE

## 12.1 Kinematics of uniform circular motion

- One radian (1 rad ≈ 57.3°) is equal to the angle subtended at the centre of a circle by an arc equal in length to the radius.

- Angular displacement is the change in angle (rad).

- Angular speed is the rate of change in angle (rad s⁻¹).

- Angular frequency is the number of complete rotations/oscillations per second (rad s⁻¹): ω = 2πf - Tangential velocity is the linear speed of an object in circular motion: v = ωr

## 12.2 Centripetal acceleration

- Centripetal acceleration is caused by a force of constant magnitude that is always perpendicular to the direction of motion. This causes circular motion with a constant angular speed.

a = rω² = v²/r F = ma ⇒ F = mrω² = mv²/r

13 – Gravitational fields 13 GRAVITATIONAL FIELDS

## 13.1 Gravitational field

- A gravitational field is an example of a field of force.

- Gravitational field is equal to force per unit mass (i.e. N kg⁻¹).

## 13.2 Gravitational force between point masses

- For a point outside a uniform sphere, the mass of the sphere may be considered to be a point mass at its centre.

Newton’s Law of Gravitation: the force between two point masses is directly proportional to the product of their masses and inversely proportional to the square of their separation distance, given by: F = Gm₁m₂ / r² . alternatively: F = GMm / r² - Circular orbits in gravitational fields can be analysed by relating the gravitational force (F = GMm / r²) to the centripetal acceleration it causes (F = ma).

- A satellite in a geostationary orbit remains at the same point above the Earth’s surface: has an orbital period of 24 hours orbits from west to east positioned directly above the Equator

## 13.3 Gravitational field of a point mass

- Gravitational field strength due to a point mass can be derived from Newton’s law of gravitation and the definition of gravitational field.

g = F/m = (GMm / r²) / m = GM / r² - For small changes in height near the Earth’s surface, g is approximately constant because a small change in height is small enough to consider negligible compared to the distance to the centre of mass of the Earth, i.e. Δh ≪ r.

## 13.4 Gravitational potential

- Gravitational potential at a point is the work done per unit mass in bringing a small test mass from infinity to the point.

Gravitational potential in the field due to a point mass is given as: φ = -GM / r - How the concept of gravitational potential leads to the gravitational potential energy of two point masses: let there be two objects of masses M and m respectively, r metres apart gravitational potential is work done per unit mass in bringing these masses together the energy stored in the objects which is overcoming this work done is called gravitational potential energy.

Gravitational potential energy of an object of mass m: E_p = -GMm / r and E_p = mgh E_total = E_k + E_p Escape velocity can be found by: E ≥ 0 ⇒ ½mv² - GMm/r ≥ 0 ⇒ v = √(2GM/r)

## 13.5 Gravitational field strength as a gradient

- Gravitational force is the rate of change of gravitational potential energy.

F = -dE_p/dr ⇒ F = -d/dr (-GMm/r)

E_p = -∫F dr ⇒ E_p = -∫(GMm/r²) dr - Gravitational field strength is the rate of change of gravitational potential.

g = -dφ/dr ⇒ g = -d/dr (-GM/r)

φ = -∫g dr ⇒ φ = -∫(GM/r²) dr

14 – Temperature 14 TEMPERATURE

## 14.1 Thermal equilibrium

- Thermal energy is transferred from a region of higher temperature to a region of lower temperature.

- Regions of equal temperature are in thermal equilibrium.

## 14.2 Temperature scales

- A physical property that varies with temperature may be used to measure temperature, e.g.: density of a liquid volume of a gas at constant pressure resistance of a metal e.m.f. of a thermocouple - A thermocouple is a device where one end of each of two wires of different metals are twisted together and the other ends are connected to the terminals of a sensitive voltmeter.

- The scale of thermodynamic temperature does not depend on the property of any particular substance.

- T/K = θ/°C + 273.15 - The lowest possible temperature is zero kelvin on the thermodynamic temperature scale.

- This is known as absolute zero, where particles have zero kinetic energy.

## 14.3 Specific heat capacity and specific latent heat

- Specific heat capacity is the thermal energy per unit mass to raise the temperature of a substance by 1K.

Q = mcΔT where Q is the thermal energy m is the mass of the substance c is the specific heat capacity T is the thermodynamic temperature - Specific latent heat is the thermal energy per unit mass required to change the state of a substance without changing its temperature.

- The specific latent heat of fusion is for changes between the solid and liquid states.

- The specific latent heat of vaporisation is for changes between the liquid and gas states.

Q = mL where Q is the thermal energy m is the mass of the substance L is the specific latent heat

15 – Ideal Gases 15 IDEAL GASES

## 15.1 The mole

- Amount of substance is an SI base quantity with the base unit mol.

- One mole of any substance is the amount containing a number of particles of that substance equal to the Avogadro constant N_A.

## 15.2 Equation of state

- A gas obeying pV ∝ T, where T is the thermodynamic temperature, is an ideal gas.

Equation of state for an ideal gas: pV = nRT or pV = NkT where n is the amount of substance (number of moles)

N is the number of molecules p is the pressure V is the volume T is the thermodynamic temperature R is the gas constant k is the Boltzmann constant given by k = R/N_A

## 15.3 Kinetic theory of gases

- The basic assumptions of the kinetic theory of gases: a gas consists of a very large number of molecules moving in random directions and random speeds all molecules behave as identical, hard, perfectly elastic spheres there are no forces of attraction or repulsion between molecules volume of the molecules is negligible with the volume of the containing vessel time of collisions between molecules is negligible compared to the time between collisions - How molecular movement causes pressure: a molecule of mass m is moving at a speed c ms⁻¹ it has a momentum p = mc kg ms⁻¹ when it collides with the wall of its container, it exerts an impulse on the wall.

在长方形容器中，速度方向改变，因此具有新的动量 𝑝 = −𝑚𝑐 kg ms⁻¹，动量变化 Δ𝑝 = −2𝑚𝑐 kg ms⁻¹，墙壁受到的冲量与之大小相等、方向相反（即 2𝑚𝑐 kg ms⁻¹）。

15 – 理想气体 - 在理想气体中，各个方向上的平均方均分速度相等：<c_x²> = <c_y²> = <c_z²>，且 <c²> = <c_x²> + <c_y²> + <c_z²>。

- 在长度为 𝐿 m 的容器中，气体分子在垂直于 x 轴的两壁之间运动所需时间为 2𝐿/𝑐，完成一次往返回到同一壁的时间为 4𝐿/𝑐。

在与壁碰撞时，压强可由力和面积计算得出： F = Δ𝑝/Δ𝑡 = 2𝑚𝑐 / (2𝐿/𝑐) = 𝑚𝑐²/𝐿 𝑝 = F/A = 𝑚𝑐²/𝐿 / (𝐿𝑊𝐻) = 𝑚𝑐²/ (𝐿²𝑊𝐻)

由于 𝑉 = 𝐿𝑊𝐻 且共有 𝑁 个分子，则有： 𝑝 = 𝑁𝑚<𝑐²> / 𝑉，即 𝑝𝑉 = 𝑁𝑚<𝑐²> 因为 <c²> = 3<𝑐_x²>，所以 𝑝𝑉 = 3𝑁𝑚<𝑐_x²>

比较 𝑝𝑉 的两个表达式：𝑝𝑉 = 𝑁𝑚<𝑐_x²> = 𝑁𝑘𝑇，可得 𝑚<𝑐_x²> = 𝑘𝑇，即 𝑚<𝑐²> = 3𝑘𝑇，因此 𝑚<𝑐_x²> = ½𝑚<𝑐²> = ³⁄₂𝑘𝑇。

所以分子的平均平动动能为 𝐸_k = ³⁄₂𝑘𝑇。

均方根速率 𝑐_rms 可通过 𝑐_rms = √<𝑐²> 求得：由 ½𝑚<𝑐²> = ³⁄₂𝑘𝑇 得到 <𝑐²> = 3𝑘𝑇/𝑚，故 𝑐_rms = √(3𝑘𝑇/𝑚)。

**公式总结：** 𝑝𝑉 = 𝑛𝑅𝑇 𝑝𝑉 = 𝑁𝑘𝑇 𝑝𝑉 = 𝑁𝑚<𝑐²>/3 = 2𝑁𝑚<𝑐_x²>/3 𝐸_k = ³⁄₂𝑘𝑇 <𝑐_x²> = <c_y²> = <c_z²> = <𝑐²>/3 𝑐_rms = √<𝑐²> = √(3𝑘𝑇/𝑚)

𝑚<𝑐_x²> = 𝑘𝑇

16 – 热力学

## 16.1 内能

- 内能： - 由系统的状态决定； - 可以表示为系统分子热运动的动能与分子间势能之和。

- 随着物体温度升高，其内能增加。

- 在理想气体中，分子间无相互作用力（即无势能），因此内能等于气体分子的总动能。

## 16.2 热力学第一定律

- 当气体体积在恒压下发生变化时： - 为改变体积需对气体做功（例如推动活塞）； - 气体的动能增加； - 气体的内能增加； - 气体对外做功以克服外部压力。

做功 𝑊 = 𝑝 Δ𝑉，其中 𝑊 是气体对外做的功，𝑝 是环境压强，Δ𝑉 是体积变化量。

- 热力学第一定律：Δ𝑈 = 𝑞 + 𝑊，其中 Δ𝑈 是内能增量，𝑞 是系统吸收的热量，𝑊 是对系统做的功。

17 – 振动

## 17.1 简谐运动

- 与振动相关的术语： - 位移：离开平衡位置的距离； - 振幅：最大位移； - 周期：完成一次全振动所需时间； - 频率：单位时间内振动的次数； - 角频率：角度变化率，一圈为 2𝜋 弧度； - 相位差：两粒子达到同方向最大位移之间经历的周期分数。

- 当加速度与偏离固定点的位移成正比且方向相反时，发生简谐运动。

- 简谐运动中粒子在位移 𝑥 处的加速度为：𝑎 = −𝜔²𝑥。

其解为 𝑥 = 𝑥₀ sin𝜔𝑡，由此可得加速度为 𝑎 = −𝑎₀ sin𝜔𝑡 或 𝑎 = −𝜔²𝑥₀ sin𝜔𝑡。

速度为 𝑣 = 𝑣₀ cos𝜔𝑡 或 𝑣 = �𝜔𝑥₀ cos𝜔𝑡 或 𝑣 = ±𝜔√(𝑥₀² − 𝑥²)。

其中 𝑎 为加速度，𝜔 为角频率，𝑡 为时间，𝑥 为位移，𝑥₀ 为振幅，𝑣 为速度，𝑣₀ 为最大速率，𝑎₀ 为最大加速度大小。

- 此图显示了简谐运动中粒子的位移、速度和加速度。

在零位移处，加速度为零（方向改变），速度达到最大且方向指向新加速度的方向。

在最大位移处，加速度最大（大小），速度为零。

## 17.2 简谐运动中的能量

- 简谐运动中，能量在粒子的动能和势能之间转换： - 在零位移处，粒子具有最大动能； - 在最大位移处，粒子具有最大势能； - 粒子的总能量为 𝐸_k + 𝐸_p。

- 简谐运动系统的总能量为：𝐸 = ½𝑚𝜔²𝑥₀²，其中 𝐸 为系统能量，𝑚 为粒子质量，𝜔 为角频率，𝑥₀ 为振幅。

## 17.3 阻尼、受迫振动与共振

- 阻尼由作用于振动系统的阻力引起。

- 阻尼相关术语： - 轻阻尼：导致振幅逐渐减小； - 临界阻尼：使振幅在尽可能短的时间内减至零，且不发生振动； - 重阻尼：导致位移呈指数衰减，比临界阻尼慢。

- 共振发生在振动系统被强迫以其固有频率振动时，此时振幅达到最大。

**公式总结：** 𝑥 = 𝑥₀ sin𝜔𝑡 𝑣 = 𝑣₀ cos𝜔𝑡 或 𝑣 = 𝜔𝑥₀ cos𝜔𝑡 𝑎 = −𝑎₀ sin𝜔𝑡 或 𝑎 = −𝜔²𝑥₀ sin𝜔𝑡 或 𝑎 = −𝜔²𝑥 𝐸 = ½𝑚𝜔²𝑥₀²

18 – 电场

## 18.1 电场与电场线

- 电场是静止电荷受力的空间区域。

- 电场强度定义为单位正电荷所受的力。

- 电荷在电场中受的力为：𝐹 = 𝑞𝐸，其中 𝐹 为力，𝑞 为电荷值，𝐸 为该点电场强度。

- 电场可用电场线表示： - 电场线必须垂直于电荷/带电极板。

## 18.2 匀强电场

- 带电平行板间匀强电场的场强为：𝐸 = Δ𝑉 / Δ𝑑，其中 𝐸 为电场强度，Δ𝑉 为电势差，Δ𝑑 为距离。

- 对于在匀强电场中运动的带电粒子： - 若初速度平行于场方向：末速度可通过电场对粒子做功转化的动能计算。

- 若初速度垂直于场方向：垂直分量受到恒定力（因此恒定加速度）指向其中一极板。

## 18.3 点电荷间的电场力

- 对于球形导体外部的点，导体上的电荷可视为位于球心的点电荷。

库仑定律：自由空间中两点电荷间的作用力与它们的电荷乘积成正比，与它们距离的平方成反比，表达式为： 𝐹 = (1/(4𝜋𝜀₀)) * (𝑄₁𝑄₂ / 𝑟²)，其中 𝐹 为力，𝑄₁ 和 𝑄₂ 为电荷值，𝜀₀ 为真空介电常数，𝑟 为点电荷间距离。

## 18.4 点电荷的电场

- 自由空间中点电荷产生的电场强度为：𝐸 = (1/(4𝜋𝜀₀)) * (𝑄 / 𝑟²)。

## 18.5 电势

- 一点处的电势是将一微小试探电荷从无穷远处移至该点过程中，单位正电荷所做的功。

- 一点处的电场强度等于该点电势梯度的负值：𝐸 = −𝑑𝑉/𝑑𝑟。

点电荷 𝑄 产生的电场中电势为：𝑉 = (1/(4𝜋𝜀₀)) * (𝑄 / 𝑟)。

- 两个点电荷的电势能是将两个孤立点电荷 𝑞 和 𝑄 从无穷远移至相距 𝑟 米时所做的功：𝐸_p = (1/(4𝜋𝜀₀)) * (𝑄𝑞 / 𝑟)。

**公式总结：** 𝐹 = 𝑞𝐸（电荷在电场中受的力）

𝐸 = Δ𝑉 / Δ𝑑（匀强电场的电场强度）

𝐹 = (1/(4𝜋𝜀₀)) * (𝑄₁𝑄₂ / 𝑟²)（自由空间中两点电荷间的作用力）

𝐸 = (1/(4𝜋𝜀₀)) * (𝑄 / 𝑟²)（自由空间中点电荷产生的电场强度）

𝑉 = (1/(4𝜋𝜀₀)) * (𝑄 / 𝑟)（点电荷电场中的电势）

𝐸_p = (1/(4𝜋𝜀₀)) * (𝑄𝑞 / 𝑟)（两个点电荷的电势能）

19 – 电容

## 19.1 电容器与电容

- 电容定义为： - 对于孤立球形导体：导体电荷与电势之比； - 对于平行板电容器：一块极板上存储的电荷与两极板间电势差之比。

电容 𝐶 = 𝑄 / 𝑉，其中 𝐶 为电容，𝑄 为电荷，𝑉 为电势差。

- 串联电容的组合： 总电压 𝑉_T = 𝑉₁ + 𝑉₂，由于电荷相同 𝑄_T = 𝑄₁ = 𝑄₂，故 𝑄_T/𝐶_T = 𝑄₁/𝐶₁ + 𝑄₂/𝐶₂，即 1/𝐶_T = 1/𝐶₁ + 1/𝐶₂。

- 并联电容的组合： 总电荷 𝑄_T = 𝑄₁ + 𝑄₂，因电压相同 𝑉_T = 𝑉₁ = 𝑉₂，故 𝑉_T 𝐶_T = 𝑉₁ 𝐶₁ + 𝑉₂ 𝐶₂，即 𝐶_T = 𝐶₁ + 𝐶₂。

## 19.2 电容器中储存的能量

- 电容器储存的电势能可通过其电荷-电压图线下的面积确定。

能量 𝑊 = ½𝑄𝑉 = ½𝐶𝑉²。

## 19.3 电容器放电

- 电容器通过电阻放电时，其电压、电荷和电流均呈指数下降。

𝑉 = 𝑉₀ 𝑒^(−𝑡/𝑅𝐶)，𝑄 = 𝑄₀ 𝑒^(−𝑡/𝑅𝐶)，𝐼 = 𝐼₀ 𝑒^(−𝑡/𝑅𝐶)。

- 电容器通过电阻放电的时间常数为：𝜏 = 𝑅𝐶。

where \( R \) is the load resistance \( C \) is the capacitance

20 – Magnetic Fields

## 20.1 Concept of a magnetic field

- A magnetic field is a region of space where a moving charge experiences a force.

- It is a field force produced either by moving charges or permanent magnets.

## 20.2 Force on a current-carrying conductor

- A force might act on a current-carrying conductor placed in a magnetic field.

\( F = BIL \sin\theta \)

where \( F \) is the force acting on the current-carrying conductor \( B \) is the magnetic flux density of the magnet causing the magnetic field \( I \) is the current through the conductor \( \theta \) is the angle between the conductor and the direction of the magnetic field

Fleming’s Left Hand Rule - Magnetic flux density is the force acting per unit current per unit length on a wire placed at right-angles to the magnetic field.

## 20.3 Force on a moving charge

\( F = BQv \sin\theta \)

where \( B \) is the magnetic flux density of the magnet causing the magnetic field \( Q \) is the size of the moving charge \( v \) is the speed of the moving charge \( \theta \) is the angle between the conductor and the direction of the magnetic field

- Hall Voltage: o when there is a current in the conductor, charge carriers will move perpendicular to the magnetic field o by Fleming’s Left Hand Rule, positive charges will ‘move’ to one side of the conductor, i.e. electrons will move to the other side of the conductor o a potential difference (Hall voltage) will develop across the conductor.

Force on each charge carrier (due to electric field strength \( E \)): \( F = qE \)

\( F = q \frac{V}{t} \)  （注：原文公式“𝑞¢ / [&£”推测为推导过程中的片段，结合下文修正）

Force on each charge carrier (due to magnetic field of flux density \( B \)): \( F = Bqv \)

When the electric field has been established, \( F_{\text{electric}} = F_{\text{magnetic}} \) and so: \( q \frac{V}{t} = Bqv \)

\( \frac{V}{t} = Bv \)

where \( I = ntvq = (td)nvq \) （注：原文片段“𝑞J K”等推测为推导中的中间步骤，此处整合为霍尔电压推导的逻辑链）

\( V = \frac{BI}{n t q} \)

- How a Hall probe is used to measure magnetic flux density: o a thin slice of semiconductor is placed perpendicular to the direction of magnetic field o the control unit passes a certain current through the semiconductor o hall voltage is displayed on the control unit (where \( V \propto B \))

o to ensure the slice is perpendicular to the magnetic field lines, it is rotated until the maximum reading is shown.

- A charged particle moving in a uniform magnetic field perpendicular to the direction of its motion: o for a charge \( q \) the perpendicular force due to the electric field is \( F = qE \)

o there is a vertical acceleration of the particle o it follows a parabolic path

- Velocity selection: o suppose an electric and magnetic field act in the same region, in opposite directions o \( Bqv = qE \)

o \( Bv = E \)

o \( v = \frac{E}{B} \)

o for charge carriers with velocity \( v \) they will not be deflected o for charge carriers with velocities greater or less than \( v \) they will be deflected

## 20.4 Magnetic fields due to currents

- Magnetic field pattern due to current in long straight wire - Magnetic field pattern due to current in flat circular coil - Right hand grip rule - Magnetic field pattern due to current in long solenoid - The magnetic field due to the current in a solenoid is increased by a ferrous core which concentrates the flux.

- Forces between current-carrying conductors: o a current-carrying conductor has a magnetic field around it o if a second current-carrying conductor is placed parallel to the first, the second conductor experiences a force due to the magnetic field of the first conductor o if the currents are in the same direction, the conductors move together o if the currents are in opposite directions, the conductors move apart

## 20.5 Electromagnetic induction

- Magnetic flux is the product of the magnetic flux density and cross-sectional area perpendicular to the direction of the magnetic flux density.

\( \Phi = BA \)

- Magnetic flux linkage is given by the product of the magnetic flux and number of turns in the coil.

\( N\Phi = BAN \)

- When the wire is moved through the magnetic field, an e.m.f. is induced, indicated by the current displayed on the galvanometer.

- The magnitude of the galvanometer reading (and induced e.m.f.) is increased by: o moving the wire faster relative to the magnet o increasing the number of turns on the loop

Fleming’s Right Hand Rule - Faraday’s Law: the e.m.f. induced is proportional to the rate of change of magnetic flux linkage.

- Lenz’s Law: the direction of the induced e.m.f. is such as to cause effects to oppose the change producing it.

\( \mathcal{E} = - \frac{d(N\Phi)}{dt} \)

where o \( \mathcal{E} \) is the induced e.m.f.

o \( N\Phi \) is the magnetic flux linkage

21 – Alternating Currents

## 21.1 Characteristics of alternating currents

- A sinusoidally alternating current or voltage can be represented by equations of the form: \( x = x_0 \sin \omega t \)

- Mean power in a resistive load is half the maximum power for a sinusoidal alternating current.

- Mean current and voltage is zero.

- The root-mean-square (r.m.s.) value of an alternating current or voltage is the value of the direct current or direct voltage that would deliver the same power.

\( I_{\text{rms}} = \frac{I_0}{\sqrt{2}} \)

\( V_{\text{rms}} = \frac{V_0}{\sqrt{2}} \)

## 21.2 Rectification and smoothing

- Half-wave rectification: Single diode only lets current flow in one direction.

- Full-wave rectification: Four diodes (bridge rectifier) cause current to take different route every half wave so half of wave is reversed.

- Full-wave rectification with smoothing: Capacitor charges up on rising part of cycle and discharges as capacitor output p.d. falls.

- The smoothing effect can be increased by increasing the time constant RC, and therefore the time taken for the capacitor to discharge, i.e.: o increasing capacitance o increasing load resistance

22 – Quantum Physics

## 22.1 Energy and momentum of a photon

- Electromagnetic radiation has a particulate nature.

- A photon is a quantum of electromagnetic energy, its energy given by: \( E = hf \) or \( E = \frac{hc}{\lambda} \)

where \( h \) is Planck’s constant \( f \) is the frequency of the electromagnetic wave \( \lambda \) is the wavelength of the electromagnetic wave \( c \) is the speed of light (\( 3.0 \times 10^8 \) m s\(^{-1} \))

- The electronvolt (eV) is a unit of energy: 1 eV = \( 1.60 \times 10^{-19} \) J - A photon has momentum \( p \), given by: \( p = \frac{h}{\lambda} \)

## 22.2 Photoelectric effect

- Photoelectrons may be emitted from a metal surface when it is illuminated by electromagnetic radiation.

- Each metal has a different: o threshold frequency: if the frequency is less than this, no electrons will be emitted no matter how bright the light source is o threshold wavelength: if the wavelength is more than this, the frequency will be less than the threshold frequency.

- How photoelectric emission works: o an electromagnetic wave is directed at a metal surface o photons (discrete packets) of energy are absorbed by the electrons in the metal o if a photon has energy greater than the work function energy of the metal, it will be emitted from the surface o the number of electrons emitted depends on light intensity.

- The energy of a photon is equal to the sum of the work function of the metal and its kinetic energy: \( hf = \phi + \frac{1}{2} m v_{\text{max}}^2 \)

where \( h \) is Planck’s constant \( f \) is the frequency of the electromagnetic wave \( \phi \) is the work function energy of the metal \( \frac{1}{2} m v_{\text{max}}^2 \) is the maximum kinetic energy of the emitted electron

- As the intensity of the electromagnetic wave is increased: o more photons reach the metal surface o these have the same energy as at a lower intensity o more electrons are emitted o each electron has the same maximum kinetic energy as before (this is independent of light intensity because the initial energy of the photon remains unchanged)

o photoelectric current is proportional to intensity

## 22.3 Wave-particle duality

- Different phenomena suggest different natures of electromagnetic radiation: o photoelectric effect: provides evidence for a particulate nature o interference and diffraction: provide evidence for a wave nature.

- The photoelectric effect provides evidence for a particulate nature because: o negligible time delay between illumination of the surface and emission of an electron o electrons are not emitted below the threshold frequency o rate of electron emission is proportional to intensity o maximum kinetic energy of electrons is dependent on the frequency o maximum kinetic energy of electrons is independent of intensity - Electron diffraction: o electrons are emitted from a hot cathode and accelerated towards a thin slice of graphite (which acts as a diffraction grating)

o bright rings are observed on the fluorescent screen o these are maxima (i.e. the electrons constructively interfered)

o this behaviour would not be expected for the assumed particulate nature of electrons o electron diffraction is evidence for the wave nature of particles - The de Broglie wavelength is the wavelength associated with a moving particle, given by: \( \lambda = \frac{h}{p} \)

where \( p \) is momentum of the moving particle

## 22.4 Energy levels in atoms and line spectra

- There are discrete electron energy levels in isolated atoms (e.g. atomic hydrogen).

- When an electron falls from a higher energy level to a lower energy level, it emits a photon.

- When an atom absorbs a photon, an electron moves to a higher energy level.

光子从较低能级跃迁到较高能级。

- 光子中的能量由能级变化决定，每次跃迁具有特定的能量变化。

- 对于具有四个能级的原子，发射的光子可能有六种波长（1 + 2 + 3）。

- 如果由这种元素产生的光通过棱镜分离为其组成波长，则会形成发射线光谱。

- 如果光通过这种元素，某些波长会被原子吸收，电子会移动到更高的能级。

- 然后，如果将光通过棱镜分离为其组成波长，则会形成吸收线光谱。

ℎf = E_i - E_f，其中 E_i 和 E_f 是电子的初始和最终能量，ℎf 是发射/吸收的光子的能量。

23 – Nuclear Physics 23 NUCLEAR PHYSICS

## 23.1 Mass defect and nuclear binding energy

- 能量与质量之间的等价性表示为： E = mc²，其中 E 是能量，m 是质量，c 是光速。

- 质量亏损是同位素的质量与其组成核子的质量之间的差值。

- 结合能是将原子核分离为其单独核子所需的能量。

- 每个核子的结合能可用作跨核子稳定性的更可比度量： - 最稳定的原子核具有最高的每核子结合能，且最不可能衰变。

- 核聚变是两个原子核结合形成单个原子核。

- 核裂变是一个大的原子核分裂形成较小的原子核。

- 为了使原子核变得更稳定，它要么发生聚变，要么发生裂变，以“更接近”最稳定的原子核： - 较小的核子数：经历聚变以变大 - 较大的核子数：经历裂变以变小 - 核反应中释放的能量可以使用以下公式计算： E = c² Δm

## 23.2 Radioactive decay

- 计数率的波动为放射性衰变的随机性提供了证据。

- 放射性衰变既是： - 自发的：不受温度或压力等外部因素影响 - 随机的：衰变时间无法预测 - 活度是每秒衰变的同位素原子核的数量。

- 衰变常数是原子核在单位时间内衰变的概率。

A = λN，其中 A 是活度，λ 是衰变常数，N 是原子核的数量。

- 放射性同位素的半衰期是其活度减半所需的时间： λ = ln2 / t_{1/2}（从 x = x₀ e^{-λt} 推导而来），其中 t_{1/2} 是半衰期（活度减半所需的时间）。

- 放射性衰变具有指数性质，其中 x = x₀ e^{-λt}，其中 x 是活度、衰变的原子核数或接收到的计数率，x₀ 是 x 的初始值（在 t = 0 时），λ 是衰变常数，t 是时间。

24 – Medical Physics 24 MEDICAL PHYSICS

## 24.1 Production and use of ultrasound

- 压电换能器可用于产生超声波。

- 超声波的产生： - 当在压电晶体两端施加电位差时，晶体形状会改变 - 晶体形状改变时会产生电动势 - 晶体以超声波频率范围（>20kHz）的振荡振动 - 将晶体切割成特定尺寸可以引起共振（振荡的最大振幅）

- 超声波的检测： - 当超声波返回时，它会引起晶体振动 - 这会在晶体两端产生交变电位差 - 该电位差可以由计算机处理 - 使用超声波： - 压电换能器产生超声波脉冲 - 脉冲在组织之间的边界处被反射 - 反射脉冲由换能器检测 - 反射波被检测到所用的时间可用于计算其距离（深度）

- 这用于获取有关内部结构的诊断信息 - 介质的特征声阻抗是介质中声速与其密度的乘积。

Z = ρc，其中 Z 是介质的特征声阻抗，ρ 是介质的密度，c 是介质中的声速。

- 两种介质之间边界的强度反射系数由以下公式给出： I_R / I_i = (Z₂ - Z₁)² / (Z₂ + Z₁)²，其中 I_R / I_i 是强度反射系数，Z₁ 和 Z₂ 是介质的特征声阻抗。

- 衰减是波在通过介质传播时由于介质中的能量吸收而导致的波强度降低： I = I₀ e^{-μx}，其中 I 是透射强度，I₀ 是入射（初始）强度，μ 是衰减/吸收系数，x 是介质的厚度。

## 24.2 Production and use of X-rays

- X射线是通过电子轰击金属靶产生的： - 使用电位差来加速电子 - 高速电子撞击金属靶，导致动能迅速损失 - 这导致X射线光子的发射 - 铝滤光片用于吸收长波长光子，否则这些光子会增加辐射剂量而无法穿透人体 - X射线束的硬度是其穿透能力。

- 硬度更大的射线束具有更短的波长。

- 由加速电位差产生的X射线的最小波长由以下公式给出： λ_min = hc / (eV)，其中 λ_min 是最小波长，e 是电子电荷，V 是加速电位差。

- X射线用于成像内部身体结构： - 它们穿透软组织（皮肤、脂肪、肌肉等）时强度损失很小 - 当到达骨骼时强度损失更大 - 胶片在骨骼位置对应的区域较浅，而在软组织区域（显影后）较暗 - 对比度是结构变黑程度的差异 - 计算机断层扫描（CT）扫描： - 结合从不同角度在同一截面拍摄的多张X射线图像以获得该截面的2D图像 - 沿轴重复此过程 - 结合多张2D图像以产生内部结构的3D图像

## 24.3 PET scanning

- 示踪剂是含有放射性原子核的物质，可以引入体内，然后被研究的组织吸收。

- 经历β⁺衰变的示踪剂用于正电子发射断层扫描。

- 当粒子与其反粒子相互作用时发生湮灭。

- 在此过程中，质能和动量守恒。

- PET扫描中的湮灭： - 示踪剂衰变发射正电子 - 当正电子与组织中的电子相互作用时，它们发生湮灭 - 这产生一对沿相反方向传播的γ射线光子 - 发射的γ射线光子的总能量由以下各项之和给出： - 正电子和电子的质能 - 正电子和电子的动能 - PET扫描的工作原理： - 示踪剂被引入体内 - 被研究的组织吸收 - 示踪剂衰变产生的正电子与组织中的电子湮灭 - 产生两个γ射线光子 - 它们传播到体外并可以被检测到 - γ射线光子的到达时间可以被处理以创建组织中示踪剂浓度的图像

25 – Astronomy & Cosmology 25 ASTRONOMY AND COSMOLOGY

## 25.1 Standard candles

- 光度是恒星辐射的总功率。

- 辐射通量强度的平方反比定律： F = L / (4πd²)，其中 F 是辐射通量强度，L 是其光度，d 是与源的距离。

- 标准烛光是已知光度的天体。

- 标准烛光可用于通过测量辐射通量强度（视亮度）和光度之间的关系来确定到星系的距离。

## 25.2 Stellar radii

- 维恩位移定律： λ_max ∝ 1/T，其中 λ_max 是辐射峰值强度的波长，T 是恒星的峰值表面热力学温度。

- 针对发射黑体辐射的球形物体的斯特藩-玻尔兹曼定律： L = 4πσr²T⁴，其中 L 是其光度，σ 是斯特藩-玻尔兹曼常数，r 是其半径，T 是其热力学温度。

## 25.3 Hubble’s law and the Big Bang theory

- 红移：遥远物体的发射光谱中的谱线显示其波长比已知值增加。

- 对于相对于观察者运动的源的电磁辐射的红移： Δλ / λ ≈ Δf / f ≈ v / c - 为什么红移导致宇宙正在膨胀的想法： - 红移数据表明几乎所有星系都在远离地球 - 星系距离越远，其红移越大 - 这意味着星系必须以越来越快的速度远离地球 - 因此，宇宙正以不断加快的速度膨胀 - 哈勃定律： v ≈ H₀ d，其中 v 是星系的径向速度，H₀ 是哈勃常数，d 是到星系的距离。

NUCLEAR PHYSICS

24 MEDICAL PHYSICS

25 ASTRONOMY AND COSMOLOGY

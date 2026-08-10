# David J Griffiths Introduction to Electrodynamics Addison Wesley 2012

> 来源文件：pre_David_J_Griffiths_Introduction_to_Electrodynamics_Addison_Wesley_2012.txt
> 字符数（约）：275464
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

INTRODUCTION TO ELECTRODYNAMICS Fourth Edition David J. Griffiths Reed College

Executive Editor: Jim Smith Senior Project Editor: Martha Steele Development Manager: Laura Kenney Managing Editor: Corinne Benson Production Project Manager: Dorothy Cox Production Management and Composition: Integra Cover Designer: Derek Bacchus Manufacturing Buyer: Dorothy Cox Marketing Manager: Will Moore

Credits and acknowledgments for materials borrowed from other sources and reproduced, with permission, in this textbook appear on the appropriate page within the text.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and the publisher was aware of a trademark claim, the designations have been printed in initial caps or all caps.

Library of Congress Cataloging-in-Publication Data Griffiths, David J. (David Jeffery), 1942- Introduction to electrodynamics / David J. Griffiths, Reed College. – Fourth edition.

pages cm Includes index.

ISBN-13: 978-0-321-85656-2 (alk. paper)

ISBN-10: 0-321-85656-2 (alk. paper)

## 1. Electrodynamics – Textbooks. I. Title

QC680.G74 2013

## 537.6 –dc23

2012029768 ISBN 10: 0-321-85656-2 ISBN 13: 978-0-321-85656-2 www.pearsonhighered.com 12345678910 — CRW — 1615141312

Contents Advertisement xiv 1 Vector Analysis 1

## 1.1 Vector Algebra

1.1.1 Vector Operations 1 1.1.2 Vector Algebra: Component Form 4 1.1.3 Triple Products 7 1.1.4 Position, Displacement, and Separation Vectors 8 1.1.5 How Vectors Transform 10

## 1.2 Differential Calculus

1.2.1 “Ordinary” Derivatives 13 1.2.2 Gradient 13 1.2.3 The Del Operator 16 1.2.4 The Divergence 17 1.2.5 The Curl 18 1.2.6 Product Rules 20 1.2.7 Second Derivatives 22

## 1.3 Integral Calculus

1.3.1 Line, Surface, and Volume Integrals 24 1.3.2 The Fundamental Theorem of Calculus 29 1.3.3 The Fundamental Theorem for Gradients 29 1.3.4 The Fundamental Theorem for Divergences 31 1.3.5 The Fundamental Theorem for Curls 34 1.3.6 Integration by Parts 36

## 1.4 Curvilinear Coordinates

1.4.1 Spherical Coordinates 38 1.4.2 Cylindrical Coordinates 43

## 1.5 The Dirac Delta Function

1.5.1 The Divergence of ˆr/r² 45 1.5.2 The One-Dimensional Dirac Delta Function 46 1.5.3 The Three-Dimensional Delta Function 50

## 1.6 The Theory of Vector Fields

1.6.1 The Helmholtz Theorem 52 1.6.2 Potentials 53 2 Electrostatics 59

## 2.1 The Electric Field

2.1.1 Introduction 59 2.1.2 Coulomb’s Law 60 2.1.3 The Electric Field 61 2.1.4 Continuous Charge Distributions 63

## 2.2 Divergence and Curl of Electrostatic Fields

2.2.1 Field Lines, Flux, and Gauss’s Law 66 2.2.2 The Divergence of E 71 2.2.3 Applications of Gauss’s Law 71 2.2.4 The Curl of E 77

## 2.3 Electric Potential

2.3.1 Introduction to Potential 78 2.3.2 Comments on Potential 80 2.3.3 Poisson’s Equation and Laplace’s Equation 83 2.3.4 The Potential of a Localized Charge Distribution 84 2.3.5 Boundary Conditions 88

## 2.4 Work and Energy in Electrostatics

2.4.1 The Work It Takes to Move a Charge 91 2.4.2 The Energy of a Point Charge Distribution 92 2.4.3 The Energy of a Continuous Charge Distribution 94 2.4.4 Comments on Electrostatic Energy 96

## 2.5 Conductors

2.5.1 Basic Properties 97 2.5.2 Induced Charges 99 2.5.3 Surface Charge and the Force on a Conductor 103 2.5.4 Capacitors 105 3 Potentials 113

## 3.1 Laplace’s Equation

3.1.1 Introduction 113 3.1.2 Laplace’s Equation in One Dimension 114 3.1.3 Laplace’s Equation in Two Dimensions 115 3.1.4 Laplace’s Equation in Three Dimensions 117 3.1.5 Boundary Conditions and Uniqueness Theorems 119 3.1.6 Conductors and the Second Uniqueness Theorem 121

## 3.2 The Method of Images

3.2.1 The Classic Image Problem 124 3.2.2 Induced Surface Charge 125 3.2.3 Force and Energy 126 3.2.4 Other Image Problems 127

## 3.3 Separation of Variables

3.3.1 Cartesian Coordinates 131 3.3.2 Spherical Coordinates 141

## 3.4 Multipole Expansion

3.4.1 Approximate Potentials at Large Distances 151 3.4.2 The Monopole and Dipole Terms 154 3.4.3 Origin of Coordinates in Multipole Expansions 157 3.4.4 The Electric Field of a Dipole 158 4 Electric Fields in Matter 167

## 4.1 Polarization

4.1.1 Dielectrics 167 4.1.2 Induced Dipoles 167 4.1.3 Alignment of Polar Molecules 170 4.1.4 Polarization 172

## 4.2 The Field of a Polarized Object

4.2.1 Bound Charges 173 4.2.2 Physical Interpretation of Bound Charges 176 4.2.3 The Field Inside a Dielectric 179

## 4.3 The Electric Displacement

4.3.1 Gauss’s Law in the Presence of Dielectrics 181 4.3.2 A Deceptive Parallel 184 4.3.3 Boundary Conditions 185

## 4.4 Linear Dielectrics

4.4.1 Susceptibility, Permittivity, Dielectric Constant 185 4.4.2 Boundary Value Problems with Linear Dielectrics 192 4.4.3 Energy in Dielectric Systems 197 4.4.4 Forces on Dielectrics 202 5 Magnetostatics 210

## 5.1 The Lorentz Force Law

5.1.1 Magnetic Fields 210 5.1.2 Magnetic Forces 212 5.1.3 Currents 216

## 5.2 The Biot-Savart Law

5.2.1 Steady Currents 223 5.2.2 The Magnetic Field of a Steady Current 224

## 5.3 The Divergence and Curl of B

5.3.1 Straight-Line Currents 229 5.3.2 The Divergence and Curl of B 231 5.3.3 Ampère’s Law 233 5.3.4 Comparison of Magnetostatics and Electrostatics 241

## 5.4 Magnetic Vector Potential

5.4.1 The Vector Potential 243 5.4.2 Boundary Conditions 249 5.4.3 Multipole Expansion of the Vector Potential 252 6 Magnetic Fields in Matter 266

## 6.1 Magnetization

6.1.1 Diamagnets, Paramagnets, Ferromagnets 266 6.1.2 Torques and Forces on Magnetic Dipoles 266 6.1.3 Effect of a Magnetic Field on Atomic Orbits 271 6.1.4 Magnetization 273

## 6.2 The Field of a Magnetized Object

6.2.1 Bound Currents 274 6.2.2 Physical Interpretation of Bound Currents 277 6.2.3 The Magnetic Field Inside Matter 279

## 6.3 The Auxiliary Field H

6.3.1 Ampère’s Law in Magnetized Materials 279 6.3.2 A Deceptive Parallel 283 6.3.3 Boundary Conditions 284

## 6.4 Linear and Nonlinear Media

6.4.1 Magnetic Susceptibility and Permeability 284 6.4.2 Ferromagnetism 288 7 Electrodynamics 296

## 7.1 Electromotive Force

7.1.1 Ohm’s Law 296 7.1.2 Electromotive Force 303 7.1.3 Motionalemf 305

## 7.2 Electromagnetic Induction

7.2.1 Faraday’s Law 312 7.2.2 The Induced Electric Field 317 7.2.3 Inductance 321 7.2.4 Energy in Magnetic Fields 328

## 7.3 Maxwell’s Equations

7.3.1 Electrodynamics Before Maxwell 332 7.3.2 How Maxwell Fixed Ampère’s Law 334 7.3.3 Maxwell’s Equations 337 7.3.4 Magnetic Charge 338 7.3.5 Maxwell’s Equations in Matter 340 7.3.6 Boundary Conditions 342 8 Conservation Laws 356

## 8.1 Charge and Energy

8.1.1 The Continuity Equation 356 8.1.2 Poynting’s Theorem 357

## 8.2 Momentum

8.2.1 Newton’s Third Law in Electrodynamics 360 8.2.2 Maxwell’s Stress Tensor 362 8.2.3 Conservation of Momentum 366 8.2.4 Angular Momentum 370

## 8.3 Magnetic Forces Do No Work

9 Electromagnetic Waves 382

## 9.1 Waves in One Dimension

9.1.1 The Wave Equation 382 9.1.2 Sinusoidal Waves 385 9.1.3 Boundary Conditions: Reflection and Transmission 388 9.1.4 Polarization 391

## 9.2 Electromagnetic Waves in Vacuum

9.2.1 The Wave Equation for E and B 393 9.2.2 Monochromatic Plane Waves 394 9.2.3 Energy and Momentum in Electromagnetic Waves 398

## 9.3 Electromagnetic Waves in Matter

9.3.1 Propagation in Linear Media 401 9.3.2 Reflection and Transmission at Normal Incidence 403 9.3.3 Reflection and Transmission at Oblique Incidence 405

## 9.4 Absorption and Dispersion

9.4.1 Electromagnetic Waves in Conductors 412 9.4.2 Reflection at a Conducting Surface 416 9.4.3 The Frequency Dependence of Permittivity 417

## 9.5 Guided Waves

9.5.1 Wave Guides 425 9.5.2 TE Waves in a Rectangular Wave Guide 428 9.5.3 The Coaxial Transmission Line 431 10 Potentials and Fields 436

## 10.1 The Potential Formulation

10.1.1 Scalar and Vector Potentials 436 10.1.2 Gauge Transformations 439 10.1.3 Coulomb Gauge and Lorenz Gauge 440 10.1.4 Lorentz Force Law in Potential Form 442

## 10.2 Continuous Distributions

10.2.1 Retarded Potentials 444 10.2.2 Jefimenko’s Equations 449

## 10.3 Point Charges

10.3.1 Liénard-Wiechert Potentials 451 10.3.2 The Fields of a Moving Point Charge 456 11 Radiation 466

## 11.1 Dipole Radiation

11.1.1 What is Radiation? 466 11.1.2 Electric Dipole Radiation 467 11.1.3 Magnetic Dipole Radiation 473 11.1.4 Radiation from an Arbitrary Source 477

## 11.2 Point Charges

11.2.1 Power Radiated by a Point Charge 482 11.2.2 Radiation Reaction 488 11.2.3 The Mechanism Responsible for the Radiation Reaction 492 12 Electrodynamics and Relativity 502

## 12.1 The Special Theory of Relativity

12.1.1 Einstein’s Postulates 502 12.1.2 The Geometry of Relativity 508 12.1.3 The Lorentz Transformations 519 12.1.4 The Structure of Spacetime 525

## 12.2 Relativistic Mechanics

12.2.1 Proper Time and Proper Velocity 532 12.2.2 Relativistic Energy and Momentum 535 12.2.3 Relativistic Kinematics 537 12.2.4 Relativistic Dynamics 542

## 12.3 Relativistic Electrodynamics

12.3.1 Magnetism as a Relativistic Phenomenon 550 12.3.2 How the Fields Transform 553 12.3.3 The Field Tensor 562 12.3.4 Electrodynamics in Tensor Notation 565 12.3.5 Relativistic Potentials 569 A Vector Calculus in Curvilinear Coordinates 575 A.1 Introduction 575 A.2 Notation 575 A.3 Gradient 576 A.4 Divergence 577 A.5 Curl 579 A.6 Laplacian 581 B The Helmholtz Theorem 582 C Units 585

Preface This is a textbook on electricity and magnetism, designed for an undergraduate course at the junior or senior level. It can be covered comfortably in two semesters, maybe even with room to spare for special topics (AC circuits, numerical methods, plasma physics, transmission lines, antenna theory, etc.) A one-semester course could reasonably stop after Chapter 7. Unlike quantum mechanics or thermal physics (for example), there is a fairly general consensus with respect to the teaching of electrodynamics; the subjects to be included, and even their order of presentation, are not particularly controversial, and textbooks differ mainly in Style and tone. My approach is perhaps less formal than most; I think this makes difficult ideas more interesting and accessible. For this new edition I have made a large number of small changes, in the interests of clarity and grace. In a few places I have corrected serious errors. I have added some problems and examples (and removed a few that were not effective). And I have included more references to the accessible literature (particularly the American Journal of Physics). I realize, of course, that most readers will not have the time or inclination to consult these resources, but I think it is worthwhile anyway, if only to emphasize that electrodynamics, notwithstanding its venerable age, is very much alive, and intriguing new discoveries are being made all the time. I hope that occasionally a problem will pique your curiosity, and you will be inspired to look up the reference—some of them are real gems.

I have maintained three items of unorthodox notation: • The Cartesian unit vectors are written x̂, ŷ, and ẑ (and, in general, all unit vectors inherit the letter of the corresponding coordinate).

• The distance from the z axis in cylindrical coordinates is designated by s, to avoid confusion with r (the distance from the origin, and the radial coordinate in spherical coordinates).

• The script letter r denotes the vector from a source point r' to the field point r (see Figure). Some authors prefer the more explicit (r − r'). But this makes many equations distractingly cumbersome, especially when the unit vector r̂ is involved. I realize that unwary readers are tempted to interpret r as r—it certainly makes the integrals easier! Please take note: r ≡ (r − r'), which is not the same as r. I think it’s good notation, but it does have to be handled with care.1

1 In MS Word, r is “Kaufmann font,” but this is very difficult to install in TeX. TeX users can download a pretty good facsimile from my website.

As in previous editions, I distinguish two kinds of problems. Some have a specific pedagogical purpose, and should be worked immediately after reading the section to which they pertain; these I have placed at the pertinent point within the chapter. (In a few cases the solution to a problem is used later in the text; these are indicated by a bullet (•) in the left margin.) Longer problems, or those of a more general nature, will be found at the end of each chapter. When I teach the subject, I assign some of these, and work a few of them in class. Unusually challenging problems are flagged by an exclamation point (!) in the margin. Many readers have asked that the answers to problems be provided at the back of the book; unfortunately, just as many are strenuously opposed. I have compromised, supplying answers when this seems particularly appropriate. A complete solution manual is available (to instructors) from the publisher; go to the Pearson website to order a copy.

I have benefitted from the comments of many colleagues. I cannot list them all here, but I would like to thank the following people for especially useful contributions to this edition: Burton Brody (Bard), Catherine Crouch (Swarthmore), Joel Franklin (Reed), Ted Jacobson (Maryland), Don Koks (Adelaide), Charles Lane (Berry), Kirk McDonald2 (Princeton), Jim McTavish (Liverpool), Rich Saenz (Cal Poly), Darrel Schroeter (Reed), Herschel Snodgrass (Lewis and Clark), and Larry Tankersley (Naval Academy). Practically everything I know about electrodynamics—certainly about teaching electrodynamics—I owe to Edward Purcell.

David J. Griffiths

2 Kirk’s website, http://www.hep.princeton.edu/~mcdonald/examples/, is a fantastic resource, with clever explanations, nifty problems, and useful references.

WHAT IS ELECTRODYNAMICS, AND HOW DOES IT FIT INTO THE GENERAL SCHEME OF PHYSICS?

Four Realms of Mechanics

In the diagram below, I have sketched out the four great realms of mechanics:

Classical Mechanics (Newton)  |  Quantum Mechanics (Bohr, Heisenberg, Schrödinger, et al.)

Special Relativity (Einstein)  |  Quantum Field Theory (Dirac, Pauli, Feynman, Schwinger, et al.)

Newtonian mechanics is adequate for most purposes in “everyday life,” but for objects moving at high speeds (near the speed of light) it is incorrect, and must be replaced by special relativity (introduced by Einstein in 1905); for objects that are extremely small (near the size of atoms) it fails for different reasons, and is superseded by quantum mechanics (developed by Bohr, Schrödinger, Heisenberg, and many others, in the 1920’s, mostly). For objects that are both very fast and very small (as is common in modern particle physics), a mechanics that combines relativity and quantum principles is in order; this relativistic quantum mechanics is known as quantum field theory—it was worked out in the thirties and forties, but even today it cannot claim to be a completely satisfactory system. In this book, save for the last chapter, we shall work exclusively in the domain of classical mechanics, although electrodynamics extends with unique simplicity to the other three realms. (In fact, the theory is in most respects automatically consistent with special relativity, for which it was, historically, the main stimulus.)

Four Kinds of Forces

Mechanics tells us how a system will behave when subjected to a given force. There are just four basic forces known (presently) to physics: I list them in the order of decreasing strength:

## 1. Strong

## 2. Electromagnetic

## 3. Weak

## 4. Gravitational

The brevity of this list may surprise you. Where is friction? Where is the “normal” force that keeps you from falling through the floor? Where are the chemical forces that bind molecules together? Where is the force of impact between two colliding billiard balls? The answer is that all these forces are electromagnetic. Indeed, it is scarcely an exaggeration to say that we live in an electromagnetic world—virtually every force we experience in everyday life, with the exception of gravity, is electromagnetic in origin.

The strong forces, which hold protons and neutrons together in the atomic nucleus, have extremely short range, so we do not “feel” them, in spite of the fact that they are a hundred times more powerful than electrical forces. The weak forces, which account for certain kinds of radioactive decay, are also of short range, and they are far weaker than electromagnetic forces. As for gravity, it is so pitifully feeble (compared to all of the others) that it is only by virtue of huge mass concentrations (like the earth and the sun) that we ever notice it at all. The electrical repulsion between two electrons is 10^42 times as large as their gravitational attraction, and if atoms were held together by gravitational (instead of electrical) forces, a single hydrogen atom would be much larger than the known universe.

Not only are electromagnetic forces overwhelmingly dominant in everyday life, they are also, at present, the only ones that are completely understood. There is, of course, a classical theory of gravity (Newton’s law of universal gravitation) and a relativistic one (Einstein’s general relativity), but no entirely satisfactory quantum mechanical theory of gravity has been constructed (though many people are working on it). At the present time there is a very successful (if cumbersome) theory for the weak interactions, and a strikingly attractive candidate (called chromodynamics) for the strong interactions. All these theories draw their inspiration from electrodynamics; none can claim conclusive experimental verification at this stage. So electrodynamics, a beautifully complete and successful theory, has become a kind of paradigm for physicists: an ideal model that other theories emulate.

The laws of classical electrodynamics were discovered in bits and pieces by Franklin, Coulomb, Ampère, Faraday, and others, but the person who completed the job, and packaged it all in the compact and consistent form it has today, was James Clerk Maxwell. The theory is now about 150 years old.

The Unification of Physical Theories

In the beginning, electricity and magnetism were entirely separate subjects. The one dealt with glass rods and cat’s fur, pith balls, batteries, currents, electrolysis, and lightning; the other with bar magnets, iron filings, compass needles, and the North Pole. But in 1820 Oersted noticed that an electric current could deflect a magnetic compass needle. Soon afterward, Ampère correctly postulated that all magnetic phenomena are due to electric charges in motion. Then, in 1831, Faraday discovered that a moving magnet generates an electric current. By the time Maxwell and Lorentz put the finishing touches on the theory, electricity and magnetism were inextricably intertwined. They could no longer be regarded as separate subjects, but rather as two aspects of a single subject: electromagnetism.

Faraday speculated that light, too, is electrical in nature. Maxwell’s theory provided spectacular justification for this hypothesis, and soon optics—the study of lenses, mirrors, prisms, interference, and diffraction—was incorporated into electromagnetism. Hertz, who presented the decisive experimental confirmation for Maxwell’s theory in 1888, put it this way: “The connection between light and electricity is now established ... In every flame, in every luminous particle, we see an electrical process... Thus, the domain of electricity extends over the whole of nature. It even affects ourselves intimately: we perceive that we possess... an electrical organ—the eye.” By 1900, then, three great branches of physics—electricity, magnetism, and optics—had merged into a single unified theory. (And it was soon apparent that visible light represents only a tiny “window” in the vast spectrum of electromagnetic radiation, from radio through microwaves, infrared and ultraviolet, to x-rays and gamma rays.)

Einstein dreamed of a further unification, which would combine gravity and electrodynamics, in much the same way as electricity and magnetism had been combined a century earlier. His unified field theory was not particularly successful, but in recent years the same impulse has spawned a hierarchy of increasingly ambitious (and speculative) unification schemes, beginning in the 1960s with the electroweak theory of Glashow, Weinberg, and Salam (which joins the weak and electromagnetic forces), and culminating in the 1980s with the superstring theory (which, according to its proponents, incorporates all four forces in a single “theory of everything”). At each step in this hierarchy, the mathematical difficulties mount, and the gap between inspired conjecture and experimental test widens; nevertheless, it is clear that the unification of forces initiated by electrodynamics has become a major theme in the progress of The Field Formulation of Electrodynamics

The fundamental problem a theory of electromagnetism hopes to solve is this: I hold up a bunch of electric charges here (and maybe shake them around); what happens to some other charge, over there? The classical solution takes the form of a field theory: We say that the space around an electric charge is permeated by electric and magnetic fields (the electromagnetic “odor,” as it were, of the charge). A second charge, in the presence of these fields, experiences a force; the fields, then, transmit the influence from one charge to the other—they “mediate” the interaction.

When a charge undergoes acceleration, a portion of the field “detaches” itself, in a sense, and travels off at the speed of light, carrying with it energy, momentum, and angular momentum. We call this electromagnetic radiation. Its existence invites (if not compels) us to regard the fields as independent dynamical entities in their own right, every bit as “real” as atoms or baseballs. Our interest accordingly shifts from the study of forces between charges to the theory of the fields themselves. But it takes a charge to produce an electromagnetic field, and it takes another charge to detect one, so we had best begin by reviewing the essential properties of electric charge.

Electric Charge

1.  Charge comes in two varieties, which we call “plus” and “minus,” because their effects tend to cancel (if you have +q and −q at the same point, electrically it is the same as having no charge there at all). This may seem too obvious to warrant comment, but I encourage you to contemplate other possibilities: what if there were 8 or 10 different species of charge? (In chromodynamics there are, in fact, three quantities analogous to electric charge, each of which may be positive or negative.) Or what if the two kinds did not tend to cancel? The extraordinary fact is that plus and minus charges occur in exactly equal amounts, to fantastic precision, in bulk matter, so that their effects are almost completely neutralized. Were it not for this, we would be subjected to enormous forces: a potato would explode violently if the cancellation were imperfect by as little as one part in 10^10.

2.  Charge is conserved: it cannot be created or destroyed—what there is now has always been. (A plus charge can “annihilate” an equal minus charge, but a plus charge cannot simply disappear by itself—something must pick up that electric charge.) So the total charge of the universe is fixed for all time. This is called global conservation of charge. Actually, I can say something much stronger: Global conservation would allow for a charge to disappear in New York and instantly reappear in San Francisco (that wouldn’t affect the total), and yet we know this doesn’t happen. If the charge was in New York and it went to San Francisco, then it must have passed along some continuous path from one to the other. This is called local conservation of charge. Later on we’ll see how to formulate a precise mathematical law expressing local conservation of charge—it’s called the continuity equation.

3.  Charge is quantized. Although nothing in classical electrodynamics requires that it be so, the fact is that electric charge comes only in discrete lumps—integer multiples of the basic unit of charge. If we call the charge on the proton +e, then the electron carries charge −e; the neutron charge zero; the pi mesons +e, 0, and −e; the carbon nucleus +6e; and so on (never 7.392e, or even 1/2e).³ This fundamental unit of charge is extremely small, so for practical purposes it is usually appropriate to ignore quantization altogether. Water, too, “really” consists of discrete lumps (molecules); yet, if we are dealing with reasonably large quantities of it we can treat it as a continuous fluid. This is in fact much closer to Maxwell’s own view; he knew nothing of electrons and protons—he must have pictured charge as a kind of “jelly” that could be divided up into portions of any size and smeared out at will.

³ Actually, protons and neutrons are composed of three quarks, which carry fractional charges (±2e/3 and ±1e/3). However, free quarks do not appear to exist in nature, and in any event, this does not alter the fact that charge is quantized; it merely reduces the size of the basic unit.

Units

The subject of electrodynamics is plagued by competing systems of units, which sometimes render it difficult for physicists to communicate with one another. The problem is far worse than in mechanics, where Neanderthals still speak of pounds and feet; in mechanics, at least all equations look the same, regardless of the units used to measure quantities. Newton’s second law remains F=ma, whether it is feet-pounds-seconds, kilograms-meters-seconds, or whatever. But this is not so in electromagnetism, where Coulomb’s law may appear variously as

F = (1/(4πε₀)) q₁ q₂ / r² r̂ (SI), or F = q₁ q₂ / r² r̂ (Gaussian), or F = (1/4π) q₁ q₂ / r² r̂ (HL).

Of the systems in common use, the two most popular are Gaussian (cgs) and SI (mks). Elementary particle theorists favor yet a third system: Heaviside-Lorentz. Although Gaussian units offer distinct theoretical advantages, most undergraduate instructors seem to prefer SI, I suppose because they incorporate the familiar household units (volts, amperes, and watts). In this book, therefore, I have used SI units. Appendix C provides a “dictionary” for converting the main results into Gaussian units.

## CHAPTER

Vector Analysis

## 1.1 VECTOR ALGEBRA

1.1.1 Vector Operations

If you walk 4 miles due north and then 3 miles due east (Fig. 1.1), you will have gone a total of 7 miles, but you’re not 7 miles from where you set out—you’re only 5. We need an arithmetic to describe quantities like this, which evidently do not add in the ordinary way. The reason they don’t, of course, is that displacements (straight line segments going from one point to another) have direction as well as magnitude (length), and it is essential to take both into account when you combine them. Such objects are called vectors: velocity, acceleration, force and momentum are other examples. By contrast, quantities that have magnitude but no direction are called scalars: examples include mass, charge, density, and temperature.

I shall use boldface (A, B, and so on) for vectors and ordinary type for scalars. The magnitude of a vector A is written |A| or, more simply, A. In diagrams, vectors are denoted by arrows: the length of the arrow is proportional to the magnitude of the vector, and the arrowhead indicates its direction. Minus A (−A) is a vector with the same magnitude as A but of opposite direction (Fig. 1.2). Note that vectors have magnitude and direction but not location: a displacement of 4 miles due north from Washington is represented by the same vector as a displacement 4 miles north from Baltimore (neglecting, of course, the curvature of the earth). On a diagram, therefore, you can slide the arrow around at will, as long as you don’t change its length or direction.

We define four vector operations: addition and three kinds of multiplication.

FIGURE 1.1 FIGURE 1.2

(i) Addition of two vectors. Place the tail of B at the head of A; the sum, A+B, is the vector from the tail of A to the head of B (Fig. 1.3). (This rule generalizes the obvious procedure for combining two displacements.) Addition is commutative:

A + B = B + A;

3 miles east followed by 4 miles north gets you to the same place as 4 miles north followed by 3 miles east. Addition is also associative:

(A + B) + C = A + (B + C).

To subtract a vector, add its opposite (Fig. 1.4):

A − B = A + (−B).

(ii) Multiplication by a scalar. Multiplication of a vector by a positive scalar a multiplies the magnitude but leaves the direction unchanged (Fig. 1.5). (If a is negative, the direction is reversed.) Scalar multiplication is distributive:

a(A + B) = aA + aB.

(iii) Dot product of two vectors. The dot product of two vectors is defined by

A · B ≡ AB cos θ, (1.1)

where θ is the angle they form when placed tail-to-tail (Fig. 1.6). Note that A · B is itself a scalar (hence the alternative name scalar product). The dot product is commutative,

A · B = B · A,

and distributive,

A · (B + C) = A · B + A · C. (1.2)

Geometrically, A · B is the product of A times the projection of B along A (or the product of B times the projection of A along B). If the two vectors are parallel, then A · B = AB. In particular, for any vector A,

A · A = A². (1.3)

If A and B are perpendicular, then A · B = 0.

FIGURE 1.5 FIGURE 1.6

Example 1.1. Let C = A − B (Fig. 1.7), and calculate the dot product of C with itself.

Solution

C · C = (A − B) · (A − B) = A · A − A · B − B · A + B · B,

or

C² = A² + B² − 2AB cos θ.

This is the law of cosines.

(iv) Cross product of two vectors. The cross product of two vectors is defined by

A × B ≡ AB sin θ n̂, (1.4)

where n̂ is a unit vector (vector of magnitude 1) pointing perpendicular to the plane of A and B. (I shall use a hat (ˆ) to denote unit vectors.) Of course, there are two directions perpendicular to any plane: “in” and “out.” The ambiguity is resolved by the right-hand rule: let your fingers point in the direction of the first vector and curl around (via the smaller angle) toward the second; then your thumb indicates the direction of n̂. (In Fig. 1.8, A × B points into the page; B × A points out of the page.) Note that A × B is itself a vector (hence the alternative name vector product). The cross product is distributive,

A × (B + C) = (A × B) + (A × C), (1.5)

but not commutative. In fact,

(B × A) = −(A × B). (1.6)

Geometrically, |A × B| is the area of the parallelogram generated by A and B (Fig. 1.8). If two vectors are parallel, their cross product is zero. In particular,

A × A = 0

for any vector A. (Here 0 is the zero vector, with magnitude 0.)

FIGURE 1.7 FIGURE 1.8

Problem 1.1 Using the definitions in Eqs. 1.1 and 1.4, and appropriate diagrams, show that the dot product and cross product are distributive, a) when the three vectors are coplanar; b) in the general case.

Problem 1.2 Is the cross product associative?

(A × B) × C =? A × (B × C).

If so, prove it; if not, provide a counterexample (the simpler the better).

1.1.2 Vector Algebra: Component Form

In the previous section, I defined the four vector operations (addition, scalar multiplication, dot product, and cross product) in “abstract” form—that is, without reference to any particular coordinate system. In practice, it is often easier to set up Cartesian coordinates x, y, z and work with vector components. Let x̂, ŷ, and ẑ be unit vectors parallel to the x, y, and z axes, respectively (Fig. 1.9(a)). An arbitrary vector A can be expanded in terms of these basis vectors (Fig. 1.9(b)):

FIGURE 1.9

A = A_x x̂ + A_y ŷ + A_z ẑ.

The numbers A_x, A_y, and A_z, are the “components” of A; geometrically, they aretheprojectionsofAalongthethreecoordinateaxes(Ax=A·xˆ, Ay=A·yˆ, Az=A·zˆ). We can now reformulate each of the four vector operations as a rule for manipulating components: A+B=(Axxˆ + Ayyˆ + Azzˆ)+(Bxxˆ + Byyˆ + Bzzˆ)

= (Ax+Bx)xˆ +(Ay+By)yˆ +(Az+Bz)zˆ. (1.7)

Rule (i): To add vectors, add like components.

aA=(aAx)xˆ +(aAy)yˆ +(aAz)zˆ. (1.8)

Rule (ii): To multiply by a scalar, multiply each component.

Because xˆ, yˆ, and zˆ are mutually perpendicular unit vectors, xˆ ·xˆ =yˆ ·yˆ =zˆ·zˆ =1; xˆ ·yˆ =xˆ ·zˆ =yˆ ·zˆ =0. (1.9)

Accordingly, A·B=(Axxˆ + Ayyˆ + Azzˆ)·(Bxxˆ + Byyˆ + Bzzˆ)

= AxBx + AyBy + AzBz. (1.10)

Rule (iii): To calculate the dot product, multiply like components, and add.

In particular, A·A= Ax2 + Ay2 + Az2, so A= √(Ax2 + Ay2 + Az2). (1.11)

(This is, if you like, the three-dimensional generalization of the Pythagorean theorem.)

Similarly, xˆ ×xˆ = yˆ ×yˆ =zˆ×zˆ =0, xˆ ×yˆ =−yˆ ×xˆ =zˆ, yˆ ×zˆ =−zˆ×yˆ =xˆ, zˆ×xˆ =−xˆ ×zˆ =yˆ. (1.12)

1 These signs pertain to a right-handed coordinate system (x-axis out of the page, y-axis to the right, z-axis up, or any rotated version thereof). In a left-handed system (z-axis down), the signs would be reversed: xˆ×yˆ=−zˆ, and so on. We shall use right-handed systems exclusively.

Therefore, A×B=(Axxˆ + Ayyˆ + Azzˆ)×(Bxxˆ + Byyˆ + Bzzˆ) (1.13)

=(AyBz−AzBy)xˆ +(AzBx−AxBz)yˆ +(AxBy−AyBx)zˆ.

This cumbersome expression can be written more neatly as a determinant: | xˆ yˆ zˆ | A×B=| Ax Ay Az | . (1.14)

| Bx By Bz | Rule (iv): To calculate the cross product, form the determinant whose first row is xˆ, yˆ, zˆ, whose second row is A (in component form), and whose third row is B.

Example 1.2. Find the angle between the face diagonals of a cube.

Solution We might as well use a cube of side 1, and place it as shown in Fig. 1.10, with one corner at the origin. The face diagonals A and B are A=1xˆ +0yˆ +1zˆ; B=0xˆ +1yˆ +1zˆ.

So, in component form, A·B=1·0+0·1+1·1=1.

On the other hand, in "abstract" form, A·B= ABcosθ = √2 √2 cosθ =2cosθ.

Therefore, cosθ =1/2, or θ =60◦.

Of course, you can get the answer more easily by drawing in a diagonal across the top of the cube, completing the equilateral triangle. But in cases where the geometry is not so simple, this device of comparing the abstract and component forms of the dot product can be a very efficient means of finding angles.

Problem 1.3 Find the angle between the body diagonals of a cube.

Problem 1.4 Use the cross product to find the components of the unit vector nˆ perpendicular to the shaded plane in Fig. 1.11.

1.1.3 Triple Products Since the cross product of two vectors is itself a vector, it can be dotted or crossed with a third vector to form a triple product.

(i) Scalar triple product: A·(B×C). Geometrically, |A·(B×C)| is the volume of the parallelepiped generated by A, B, and C, since |B×C| is the area of the base, and |Acosθ| is the altitude (Fig. 1.12). Evidently, A·(B×C)=B·(C×A)=C·(A×B), (1.15)

for they all correspond to the same figure. Note that "alphabetical" order is preserved—in view of Eq. 1.6, the "nonalphabetical" triple products, A·(C×B)=B·(A×C)=C·(B×A), have the opposite sign. In component form, | Ax Ay Az | A·(B×C)=| Bx By Bz | . (1.16)

| Cx Cy Cz | Note that the dot and cross can be interchanged: A·(B×C)=(A×B)·C (this follows immediately from Eq. 1.15); however, the placement of the parentheses is critical: (A·B)×C is a meaningless expression—you can’t make a cross product from a scalar and a vector.

(ii) Vector triple product: A×(B×C). The vector triple product can be simplified by the so-called BAC-CAB rule: A×(B×C)=B(A·C)−C(A·B). (1.17)

Notice that (A×B)×C=−C×(A×B)=−A(B·C)+B(A·C)

is an entirely different vector (cross-products are not associative). All higher vector products can be similarly reduced, often by repeated application of Eq. 1.17, so it is never necessary for an expression to contain more than one cross product in any term. For instance, (A×B)·(C×D)=(A·C)(B·D)−(A·D)(B·C); A×[B×(C×D)]=B[A·(C×D)]−(A·B)(C×D). (1.18)

Problem 1.5 Prove the BAC-CAB rule by writing out both sides in component form.

Problem 1.6 Prove that [A×(B×C)]+[B×(C×A)]+[C×(A×B)]=0.

Under what conditions does A×(B×C)=(A×B)×C?

1.1.4 Position, Displacement, and Separation Vectors The location of a point in three dimensions can be described by listing its Cartesian coordinates (x, y, z). The vector to that point from the origin (O) is called the position vector (Fig. 1.13): r≡ xxˆ +yyˆ +zzˆ. (1.19)

I will reserve the letter r for this purpose, throughout the book. Its magnitude, r = √(x2+y2+z2), (1.20)

is the distance from the origin, and r̂ = r/r = (xxˆ +yyˆ +zzˆ)/√(x2+y2+z2) (1.21)

is a unit vector pointing radially outward. The infinitesimal displacement vector, from (x, y, z) to (x+dx, y+dy, z+dz), is dl=dxxˆ +dyyˆ +dzzˆ. (1.22)

(We could call this dr, since that’s what it is, but it is useful to have a special notation for infinitesimal displacements.)

In electrodynamics, one frequently encounters problems involving two points—typically, a source point, r', where an electric charge is located, and a field point, r, at which you are calculating the electric or magnetic field (Fig. 1.14). It pays to adopt right from the start some short-hand notation for the separation vector from the source point to the field point. I shall use for this purpose the script letter r̿: r̿≡r−r'. (1.23)

Its magnitude is r̿=|r−r'|, (1.24)

and a unit vector in the direction from r' to r is r̂̿ = r̿/r̿ = (r−r')/|r−r'|. (1.25)

In Cartesian coordinates, r̿=(x−x')xˆ +(y−y')yˆ +(z−z')zˆ, (1.26)

r̿= √[(x−x')2+(y−y')2+(z−z')2], (1.27)

r̂̿ = [(x−x')xˆ +(y−y')yˆ +(z−z')zˆ]/√[(x−x')2+(y−y')2+(z−z')2] (1.28)

(from which you can appreciate the economy of the script- notation).

Problem 1.7 Find the separation vector from the source point (2, 8, 7) to the field point (4, 6, 8). Determine its magnitude (r̿), and construct the unit vector (r̂̿).

1.1.5 How Vectors Transform The definition of a vector as "a quantity with a magnitude and direction" is not altogether satisfactory: What precisely does "direction" mean? This may seem a pedantic question, but we shall soon encounter a species of derivative that looks rather like a vector, and we’ll want to know for sure whether it is one.

You might be inclined to say that a vector is anything that has three components that combine properly under addition. Well, how about this: We have a barrel of fruit that contains Nx pears, Ny apples, and Nz bananas. Is N=Nxxˆ +Nyyˆ +Nzzˆ a vector? It has three components, and when you add another barrel with Mx pears, My apples, and Mz bananas the result is (Nx+Mx) pears, (Ny+My) apples, (Nz+Mz) bananas. So it does add like a vector. Yet it’s obviously not a vector, in the physicist’s sense of the word, because it doesn’t really have a direction. What exactly is wrong with it?

The answer is that N does not transform properly when you change coordinates. The coordinate frame we use to describe positions in space is of course entirely arbitrary, but there is a specific geometrical transformation law for converting vector components from one frame to another. Suppose, for instance, the x,y,z system is rotated by angle φ, relative to x,y,z, about the common x = x axes. From Fig. 1.15, Ay = Acosθ, Az = Asinθ, while Ay = Acosθ' = Acos(θ−φ)= A(cosθcosφ+sinθsinφ)

=cosφAy +sinφAz, Az = Asinθ' = Asin(θ−φ)= A(sinθcosφ−cosθsinφ)

=−sinφAy +cosφAz.

We might express this conclusion in matrix notation: | Ay' |   | cosφ  sinφ |   | Ay | |     | = |           | * |    | . (1.29)

| Az' |   | -sinφ cosφ |   | Az | More generally, for rotation about an arbitrary axis in three dimensions, the transformation law takes the form | Ax' |   | Rxx Rxy Rxz |   | Ax | | Ay' | = | Ryx Ryy Ryz | * | Ay | , (1.30)

| Az' |   | Rzx Rzy Rzz |   | Az | or, more compactly, A'i = Σ(j=1 to 3) Rij Aj , (1.31)

where the index 1 stands for x, 2 for y, and 3 for z. The elements of the matrix R can be ascertained, for a given rotation, by the same sort of trigonometric arguments as we used for a rotation about the x axis.

Now: Do the components of N transform in this way? Of course not—it doesn’t matter what coordinates you use to represent positions in space; there are still just as many apples in the barrel. You can’t convert a pear into a banana by choosing a different set of axes, but you can turn Ax into Ay. Formally, then, a vector is any set of three components that transforms in the same manner as a displacement when you change coordinates. As always, displacement is the model for the behavior of all vectors.

By the way, a (second-rank) tensor is a quantity with nine components, Txx, Txy, Txz, Tyx, Tyy, Tyz, Tzx, Tzy, Tzz, which transform with two factors of R: T'xx = Rxx(RxxTxx + RxyTxy + RxzTxz)

+ Rxy(RyxTxx + RyyTxy + RyzTxz)

+ Rxz(RzxTxx + RzyTxy + RzzTxz), ...

or, more compactly, T'ij = Σ(k=1 to 3) Σ(l=1 to 3) Rik Rjl Tkl . (1.32)

In general, an nth-rank tensor has n indices and 3n components, and transforms with n factors of R. In this hierarchy, a vector is a tensor of rank 1, and a scalar is a tensor of rank zero.

Problem 1.8 (a) Prove that the two-dimensional rotation matrix (Eq. 1.29) preserves dot products. (That is, show that A'yB'y + A'zB'z = AyBy + AzBz .)

(b) What constraints must the elements (Rij) of the three-dimensional rotation matrix (Eq. 1.30) satisfy, in order to preserve the length of A (for all vectors A)?

Problem 1.9 Find the transformation matrix R that describes a rotation by 120◦ about an axis from the origin through the point (1, 1, 1). The rotation is clockwise as you look from the point (1, 1, 1) toward the origin.

ook down the axis toward the origin.

Problem 1.10 (a) How do the components of a vector**5** transform under a translation of coordinates (x = x, y = y − a, z = z, Fig. 1.16a)?

(b) How do the components of a vector transform under an inversion of coordinates (x = −x, y = −y, z = −z, Fig. 1.16b)?

(c) How do the components of a cross product (Eq. 1.13) transform under inversion? [The cross product of two vectors is properly called a pseudovector because of this “anomalous” behavior.] Is the cross product of two pseudovectors a vector, or a pseudovector? Name two pseudovector quantities in classical mechanics.

(d) How does the scalar triple product of three vectors transform under inversions? (Such an object is called a pseudoscalar.)

**4**A scalar does not change when you change coordinates. In particular, the components of a vector are not scalars, but the magnitude is.

**5**Beware: The vector r (Eq. 1.19) goes from a specific point in space (the origin, O) to the point P = (x, y, z). Under translations the new origin (O̅) is at a different location, and the arrow from O̅ to P is a completely different vector. The original vector r still goes from O to P, regardless of the coordinates used to label these points.

Suppose we have a function of one variable: f(x). Question: What does the derivative, df/dx, do for us? Answer: It tells us how rapidly the function f(x) varies when we change the argument x by a tiny amount, dx: df = (df/dx) dx. (1.33)

In words: If we increment x by an infinitesimal amount dx, then f changes by an amount df; the derivative is the proportionality factor. For example, in Fig. 1.17(a), the function varies slowly with x, and the derivative is correspondingly small. In Fig. 1.17(b), f increases rapidly with x, and the derivative is large, as you move away from x = 0.

Geometrical Interpretation: The derivative df/dx is the slope of the graph of f versus x.

Suppose, now, that we have a function of three variables—say, the temperature T(x, y, z) in this room. (Start out in one corner, and set up a system of axes; then for each point (x, y, z) in the room, T gives the temperature at that spot.) We want to generalize the notion of “derivative” to functions like T, which depend not on one but on three variables.

A derivative is supposed to tell us how fast the function varies, if we move a little distance. But this time the situation is more complicated, because it depends on what direction we move: If we go straight up, then the temperature will probably increase fairly rapidly, but if we move horizontally, it may not change much at all. In fact, the question “How fast does T vary?” has an infinite number of answers, one for each direction we might choose to explore.

Fortunately, the problem is not as bad as it looks. A theorem on partial derivatives states that dT = (∂T/∂x) dx + (∂T/∂y) dy + (∂T/∂z) dz. (1.34)

This tells us how T changes when we alter all three variables by the infinitesimal amounts dx, dy, dz. Notice that we do not require an infinite number of derivatives—three will suffice: the partial derivatives along each of the three coordinate directions.

Equation 1.34 is reminiscent of a dot product: dT = (∂T/∂x) x̂ + (∂T/∂y) ŷ + (∂T/∂z) ẑ · (dx x̂ + dy ŷ + dz ẑ)

= (∇T) · (dl), (1.35)

where ∇T ≡ (∂T/∂x) x̂ + (∂T/∂y) ŷ + (∂T/∂z) ẑ (1.36)

is the gradient of T. Note that ∇T is a vector quantity, with three components; it is the generalized derivative we have been looking for. Equation 1.35 is the three-dimensional version of Eq. 1.33.

Geometrical Interpretation of the Gradient: Like any vector, the gradient has magnitude and direction. To determine its geometrical meaning, let’s rewrite the dot product (Eq. 1.35) using Eq. 1.1: dT = ∇T · dl = |∇T| |dl| cosθ, (1.37)

where θ is the angle between ∇T and dl. Now, if we fix the magnitude |dl| and search around in various directions (that is, vary θ), the maximum change in T evidently occurs when θ = 0 (for then cosθ = 1). That is, for a fixed distance |dl|, dT is greatest when I move in the same direction as ∇T. Thus: The gradient ∇T points in the direction of maximum increase of the function T.

Moreover: The magnitude |∇T| gives the slope (rate of increase) along this maximal direction.

Imagine you are standing on a hillside. Look all around you, and find the direction of steepest ascent. That is the direction of the gradient. Now measure the slope in that direction (rise over run). That is the magnitude of the gradient. (Here the function we’re talking about is the height of the hill, and the coordinates it depends on are positions—latitude and longitude, say. This function depends on only two variables, not three, but the geometrical meaning of the gradient is easier to grasp in two dimensions.) Notice from Eq. 1.37 that the direction of maximum descent is opposite to the direction of maximum ascent, while at right angles (θ = 90°) the slope is zero (the gradient is perpendicular to the contour lines). You can conceive of surfaces that do not have these properties, but they always have “kinks” in them, and correspond to non differentiable functions.

What would it mean for the gradient to vanish? If ∇T = 0 at (x, y, z), then dT = 0 for small displacements about the point (x, y, z). This is, then, a stationary point of the function T(x, y, z). It could be a maximum (a summit), a minimum (a valley), a saddle point (a pass), or a “shoulder.” This is analogous to the situation for functions of one variable, where a vanishing derivative signals a maximum, a minimum, or an inflection. In particular, if you want to locate the extrema of a function of three variables, set its gradient equal to zero.

Example 1.3. Find the gradient of r = √(x² + y² + z²) (the magnitude of the position vector).

Solution ∇r = (∂r/∂x) x̂ + (∂r/∂y) ŷ + (∂r/∂z) ẑ = (1/(2√(x²+y²+z²))) 2x x̂ + (1/(2√(x²+y²+z²))) 2y ŷ + (1/(2√(x²+y²+z²))) 2z ẑ = (x x̂ + y ŷ + z ẑ)/√(x²+y²+z²) = r/r = r̂.

Does this make sense? Well, it says that the distance from the origin increases most rapidly in the radial direction, and that its rate of increase in that direction is 1... just what you’d expect.

Problem 1.11 Find the gradients of the following functions: (a) f(x, y, z) = x² + y³ + z⁴.

(b) f(x, y, z) = x² y³ z⁴.

(c) f(x, y, z) = eˣ sin(y) ln(z).

Problem 1.12 The height of a certain hill (in feet) is given by h(x, y) = 10(2xy − 3x² − 4y² − 18x + 28y + 12), where y is the distance (in miles) north, x the distance east of South Hadley.

(a) Where is the top of the hill located?

(b) How high is the hill?

(c) How steep is the slope (in feet per mile) at a point 1 mile north and one mile east of South Hadley? In what direction is the slope steepest, at that point?

• Problem 1.13 Let r be the separation vector from a fixed point (x′, y′, z′) to the point (x, y, z), and let r be its length. Show that (a) ∇(r²) = 2r.

(b) ∇(1/r) = −r̂ / r².

(c) What is the general formula for ∇(rⁿ)?

! Problem 1.14 Suppose that f is a function of two variables (y and z) only. Show that the gradient ∇f = (∂f/∂y) ŷ + (∂f/∂z) ẑ transforms as a vector under rotations, Eq. 1.29. [Hint: (∂f/∂y) = (∂f/∂y)(∂y/∂y) + (∂f/∂z)(∂z/∂y), and the analogous formula for ∂f/∂z. We know that y = y cosφ + z sinφ and z = −y sinφ + z cosφ; “solve” these equations for y and z (as functions of y and z), and compute the needed derivatives ∂y/∂y, ∂z/∂y, etc.]

The gradient has the formal appearance of a vector, ∇, “multiplying” a scalar T: ∇T = (x̂ ∂/∂x + ŷ ∂/∂y + ẑ ∂/∂z) T. (1.38)

(For once, I write the unit vectors to the left, just so no one will think this means ∂x̂/∂x, and so on—which would be zero, since x̂ is constant.) The term in parentheses is called del: ∇ ≡ x̂ ∂/∂x + ŷ ∂/∂y + ẑ ∂/∂z. (1.39)

Of course, del is not a vector, in the usual sense. Indeed, it doesn’t mean much until we provide it with a function to act upon. Furthermore, it does not “multiply” T; rather, it is an instruction to differentiate what follows. To be precise, then, we say that ∇ is a vector operator that acts upon T, not a vector that multiplies T. With this qualification, though, ∇ mimics the behavior of an ordinary vector in virtually every way; almost anything that can be done with other vectors can also be done with ∇, if we merely translate “multiply” by “act upon.” So by all means take the vector appearance of ∇ seriously: it is a marvelous piece of notational simplification, as you will appreciate if you ever consult Maxwell’s original work on electromagnetism, written without the benefit of ∇.

Now, an ordinary vector A can multiply in three ways:

## 1. By a scalar a: Aa;

## 2. By a vector B, via the dot product: A · B;

## 3. By a vector B via the cross product: A × B

Correspondingly, there are three ways the operator ∇ can act:

## 1. On a scalar function T: ∇T (the gradient);

## 2. On a vector function v, via the dot product: ∇ · v (the divergence);

## 3. On a vector function v, via the cross product: ∇ × v (the curl)

We have already discussed the gradient. In the following sections we examine the other two vector derivatives: divergence and curl.

From the definition of ∇ we construct the divergence: ∇ · v = (x̂ ∂/∂x + ŷ ∂/∂y + ẑ ∂/∂z) · (vₓ x̂ + vᵧ ŷ + v_z ẑ)

= ∂vₓ/∂x + ∂vᵧ/∂y + ∂v_z/∂z. (1.40)

Observe that the divergence of a vector function**6** v is itself a scalar ∇ · v.

Geometrical Interpretation: The name divergence is well chosen, for ∇ · v is a measure of how much the vector v spreads out (diverges) from the point in question. For example, the vector function in Fig. 1.18a has a large (positive) divergence (if the arrows pointed in, it would be a negative divergence), the function in Fig. 1.18b has zero divergence, and the function in Fig. 1.18c again has a positive divergence. (Please understand that v here is a function—there’s a different vector associated with every point in space. In the diagrams, of course, I can only draw the arrows at a few representative locations.)

Imagine standing at the edge of a pond. Sprinkle some sawdust or pine needles on the surface. If the material spreads out, then you dropped it at a point of positive divergence; if it collects together, you dropped it at a point of negative divergence. (The vector function v in this model is the velocity of the water at the surface—this is a two-dimensional example, but it helps give one a “feel” for what the divergence means. A point of positive divergence is a source, or “faucet”; a point of negative divergence is a sink, or “drain.”)

Example 1.4. Suppose the functions in Fig. 1.18 are v = r = x x̂ + y ŷ + z ẑ, v = ẑ, and v = z ẑ. Calculate their divergence.

Solution ∇·v = (1)+(1)+(1) = 3.

As anticipated, this function has a positive divergence.

∇·v = (0)+(0)+(0) = 0, as expected.

∇·v = (0)+(0)+(1) = 1.

Problem 1.15 Calculate the divergence of the following vector functions: (a) v = x²x̂ + 3xz²ŷ − 2xzẑ.

(b) v = xyx̂ + 2yzŷ + 3zxẑ.

(c) v = y²x̂ + (2xy + z²)ŷ + 2yzẑ.

Problem 1.16 Sketch the vector function v = r̂ / r², and compute its divergence. The answer may surprise you... can you explain it?

Problem 1.17 In two dimensions, show that the divergence transforms as a scalar under rotations. [Hint: Use Eq. 1.29 to determine v_y and v_z, and the method of Prob. 1.14 to calculate the derivatives. Your aim is to show that ∂v_y/∂y + ∂v_z/∂z = ∂v'_y/∂y' + ∂v'_z/∂z'.]

1.2.5 The Curl From the definition of ∇ we construct the curl: ∇×v = ∂v_z/∂y − ∂v_y/∂z) x̂ + (∂v_x/∂z − ∂v_z/∂x) ŷ + (∂v_y/∂x − ∂v_x/∂y) ẑ.   (1.41)

Notice that the curl of a vector function v is, like any cross product, a vector.

Geometrical Interpretation: The name curl is also well chosen, for ∇×v is a measure of how much the vector v swirls around the point in question. Thus the three functions in Fig. 1.18 all have zero curl (as you can easily check for yourself), whereas the functions in Fig. 1.19 have a substantial curl, pointing in the z direction, as the natural right-hand rule would suggest. Imagine (again) you are standing at the edge of a pond. Float a small paddle wheel (a cork with toothpicks pointing out radially would do); if it starts to rotate, then you placed it at a point of non-zero curl. A whirlpool would be a region of large curl.

Example 1.5. Suppose the function sketched in Fig. 1.19a is v = −y x̂ + x ŷ, and that in Fig. 1.19b is v = x ŷ. Calculate their curls.

Solution ∇×v = ∇×(−y x̂ + x ŷ) = 2ẑ, and ∇×v = ∇×(x ŷ) = ẑ.

As expected, these curls point in the +z direction. (Incidentally, they both have zero divergence, as you might guess from the pictures: nothing is "spreading out"... it just "swirls around.")

7 There's no such thing as the curl of a scalar.

Problem 1.18 Calculate the curls of the vector functions in Prob. 1.15.

Problem 1.19 Draw a circle in the xy plane. At a few representative points draw the vector v tangent to the circle, pointing in the clockwise direction. By comparing adjacent vectors, determine the sign of ∂v_y/∂y and ∂v_x/∂x. According to Eq. 1.41, then, what is the direction of ∇×v? Explain how this example illustrates the geometrical interpretation of the curl.

Problem 1.20 Construct a vector function that has zero divergence and zero curl everywhere. (A constant will do the job, of course, but make it something a little more interesting than that!)

1.2.6 Product Rules The calculation of ordinary derivatives is facilitated by a number of rules, such as the sum rule: d(f+g)/dx = df/dx + dg/dx, the rule for multiplying by a constant: d(kf)/dx = k df/dx, the product rule: d(fg)/dx = f dg/dx + g df/dx, and the quotient rule: d(f/g)/dx = (g df/dx − f dg/dx)/g².

Similar relations hold for the vector derivatives. Thus, ∇(f+g) = ∇f + ∇g, ∇·(A+B) = (∇·A) + (∇·B), ∇×(A+B) = (∇×A) + (∇×B), and ∇(kf) = k∇f, ∇·(kA) = k(∇·A), ∇×(kA) = k(∇×A), as you can check for yourself. The product rules are not quite so simple. There are two ways to construct a scalar as the product of two functions: fg (product of two scalar functions), A·B (dot product of two vector functions), and two ways to make a vector: fA (scalar times vector), A×B (cross product of two vectors).

Accordingly, there are six product rules, two for gradients: (i) ∇(fg) = f∇g + g∇f, (ii) ∇(A·B) = A×(∇×B) + B×(∇×A) + (A·∇)B + (B·∇)A, two for divergences: (iii) ∇·(fA) = f(∇·A) + A·(∇f), (iv) ∇·(A×B) = B·(∇×A) − A·(∇×B), and two for curls: (v) ∇×(fA) = f(∇×A) − A×(∇f), (vi) ∇×(A×B) = (B·∇)A − (A·∇)B + A(∇·B) − B(∇·A).

You will be using these product rules so frequently that I have put them inside the front cover for easy reference. The proofs come straight from the product rule for ordinary derivatives. For instance, ∇·(fA) = ∂(f A_x)/∂x + ∂(f A_y)/∂y + ∂(f A_z)/∂z = (∂f/∂x A_x + f ∂A_x/∂x) + (∂f/∂y A_y + f ∂A_y/∂y) + (∂f/∂z A_z + f ∂A_z/∂z)

= (∇f)·A + f(∇·A).

It is also possible to formulate three quotient rules: ∇(f/g) = (g∇f − f∇g)/g², ∇·(A/g) = (g(∇·A) − A·(∇g))/g², ∇×(A/g) = (g(∇×A) + A×(∇g))/g².

However, since these can be obtained quickly from the corresponding product rules, there is no point in listing them separately.

Problem 1.21 Prove product rules (i), (iv), and (v).

Problem 1.22 (a) If A and B are two vector functions, what does the expression (A·∇)B mean? (That is, what are its x, y, and z components, in terms of the Cartesian components of A, B, and ∇?)

(b) Compute (r̂·∇)r̂, where r̂ is the unit vector defined in Eq. 1.21.

(c) For the functions in Prob. 1.15, evaluate (v_a·∇)v_a.

Problem 1.23 (For masochists only.) Prove product rules (ii) and (vi). Refer to Prob. 1.22 for the definition of (A·∇)B.

Problem 1.24 Derive the three quotient rules.

Problem 1.25 (a) Check product rule (iv) (by calculating each term separately) for the functions A = x x̂ + 2y ŷ + 3z ẑ; B = 3y x̂ − 2x ŷ.

(b) Do the same for product rule (ii).

(c) Do the same for rule (vi).

1.2.7 Second Derivatives The gradient, the divergence, and the curl are the only first derivatives we can make with ∇; by applying ∇ twice, we can construct five species of second derivatives. The gradient ∇T is a vector, so we can take the divergence and curl of it: (1) Divergence of gradient: ∇·(∇T).

(2) Curl of gradient: ∇×(∇T).

The divergence ∇·v is a scalar—all we can do is take its gradient: (3) Gradient of divergence: ∇(∇·v).

The curl ∇×v is a vector, so we can take its divergence and curl: (4) Divergence of curl: ∇·(∇×v).

(5) Curl of curl: ∇×(∇×v).

This exhausts the possibilities, and in fact not all of them give anything new. Let's consider them one at a time: (1) ∇·(∇T) = ∂²T/∂x² + ∂²T/∂y² + ∂²T/∂z².   (1.42)

This object, which we write as ∇²T for short, is called the Laplacian of T; we shall be studying it in great detail later on. Notice that the Laplacian of a scalar T is a scalar. Occasionally, we shall speak of the Laplacian of a vector, ∇²v. By this we mean a vector quantity whose x-component is the Laplacian of v_x, and so on:8 ∇²v ≡ (∇²v_x)x̂ + (∇²v_y)ŷ + (∇²v_z)ẑ.   (1.43)

This is nothing more than a convenient extension of the meaning of ∇².

(2) The curl of a gradient is always zero: ∇×(∇T) = 0.   (1.44)

This is an important fact, which we shall use repeatedly; you can easily prove it from the definition of ∇, Eq. 1.39. Beware: You might think Eq. 1.44 is "obviously" true—isn't it just (∇×∇)T, and isn't the cross product of any vector (in this case, ∇) with itself always zero? This reasoning is suggestive, but not quite conclusive, since ∇ is an operator and does not "multiply" in the usual way. The proof of Eq. 1.44, in fact, hinges on the equality of cross derivatives: ∂²T/∂x∂y = ∂²T/∂y∂x.   (1.45)

If you think I'm being fussy, test your intuition on this one: (∇T)×(∇S). Is that always zero? (It would be, of course, if you replaced the ∇'s by an ordinary vector.)

(3) ∇(∇·v) seldom occurs in physical applications, and it has not been given any special name of its own—it's just the gradient of the divergence. Notice that ∇(∇·v) is not the same as the Laplacian of a vector: ∇²v = (∇·∇)v ≠ ∇(∇·v).

(4) The divergence of a curl, like the curl of a gradient, is always zero: ∇·(∇×v) = 0.   (1.46)

You can prove this for yourself. (Again, there is a fraudulent short-cut proof, using the vector identity A·(B×C) = (A×B)·C.)

(5) As you can check from the definition of ∇: ∇×(∇×v) = ∇(∇·v) − ∇²v.   (1.47)

So curl-of-curl gives nothing new; the first term is just number (3), and the second is the Laplacian (of a vector). (In fact, Eq. 1.47 is often used to define the Laplacian of a vector, in preference to Eq. 1.43, which makes explicit reference to Cartesian coordinates.)

Really, then, there are just two kinds of second derivatives: the Laplacian (which is of fundamental importance) and the gradient-of-divergence (which we seldom encounter). We could go through a similar ritual to work out third derivatives, but fortunately second derivatives suffice for practically all physical applications.

A final word on vector differential calculus: It all flows from the operator ∇, and from taking seriously its vectorial character. Even if you remembered only the definition of ∇, you could easily reconstruct all the rest.

Problem 1.26 Calculate the Laplacian of the following functions: (a) T = x² + 2xy + 3z + 4.

(b) T = sin x sin y sin z.

(c) T = e⁻⁵ˣ sin 4y cos 3z.

(d) v = x²x̂ + 3xz²ŷ − 2xzẑ.

Problem 1.27 Prove that the divergence of a curl is always zero. Check it for function v in Prob. 1.15.

Problem 1.28 Prove that the curl of a gradient is always zero. Check it for function (b) in Prob. 1.11.

## 1.3 Integral Calculus

1.3.1 Line, Surface, and Volume Integrals In electrodynamics, we encounter several different kinds of integrals, among which the most important are line (or path) integrals, surface integrals (or flux), and volume integrals.

(a) Line Integrals. A line integral is an expression of the form ∫_a^b v·dl,   (1.48)

where v is a vector function, dl is the infinitesimal displacement vector (Eq. 1.22), and the integral is to be carried out along a prescribed path P from point a to point b (Fig. 1.20). If the path in question forms a closed loop (that is, if b = a), I shall put a circle on the integral sign: ∮ v·dl.   (1.49)

At each point on the path, we take the dot product of v (evaluated at that point) with the displacement dl to the next point on the path. To a physicist, the most familiar example of a line integral is the work done by a force F: W = ∫ F·dl.

Ordinarily, the value of a line integral depends critically on the path taken from a to b, but there is an important special class of vector functions for which the line integral is independent of path and is determined entirely by the endpoints.

Points. It will be our business in due course to characterize this special class of vectors. (A force that has this property is called conservative.)

Example 1.6. Calculate the line integral of the function v = y² x̂ + 2x(y+1) ŷ from the point a = (1, -1, 0) to the point b = (2, 2, 0), along the paths (1) and (2) in Fig. 1.21. What is ∫ v·dl for the loop that goes from a to b along (1) and returns to a along (2)?

Solution As always, dl = dx x̂ + dy ŷ + dz ẑ. Path (1) consists of two parts. Along the “horizontal” segment, dy = dz = 0, so (i) dl = dx x̂, y = 1, v·dl = y² dx = dx, so ∫ v·dl = ∫ dx = 1.

On the “vertical” stretch, dx = dz = 0, so (ii) dl = dy ŷ, x = 2, v·dl = 2x(y+1) dy = 4(y+1) dy, so ∫ v·dl = ∫ 4(y+1) dy = 10.

By path (1), then, ∫ v·dl = 1 + 10 = 11.

Meanwhile, on path (2) x = y, dx = dy, and dz = 0, so dl = dx x̂ + dx ŷ, v·dl = x² dx + 2x(x+1) dx = (3x² + 2x) dx, and ∫_a^b v·dl = ∫_1^2 (3x² + 2x) dx = (x³ + x²)|_1^2 = 10.

(The strategy here is to get everything in terms of one variable; I could just as well have eliminated x in favor of y.)

For the loop that goes out (1) and back (2), then, ∮ v·dl = 11 − 10 = 1.

(b) Surface Integrals. A surface integral is an expression of the form ∫ v·da, (1.50)

where v is again some vector function, and the integral is over a specified surface S. Here da is an infinitesimal patch of area, with direction perpendicular to the surface (Fig. 1.22). There are, of course, two directions perpendicular to any surface, so the sign of a surface integral is intrinsically ambiguous. If the surface is closed (forming a “balloon”), in which case I shall again put a circle on the integral sign ∮ v·da, then tradition dictates that “outward” is positive, but for open surfaces it’s arbitrary. If v describes the flow of a fluid (mass per unit area per unit time), then v·da represents the total mass per unit time passing through the surface—hence the alternative name, “flux.”

Ordinarily, the value of a surface integral depends on the particular surface chosen, but there is a special class of vector functions for which it is independent of the surface and is determined entirely by the boundary line. An important task will be to characterize this special class of functions.

Example 1.7. Calculate the surface integral of v = 2xz x̂ + (x+2) ŷ + y(z²−3) ẑ over five sides (excluding the bottom) of the cubical box (side 2) in Fig. 1.23. Let “upward and outward” be the positive direction, as indicated by the arrows.

Solution Taking the sides one at a time: (i) x = 2, da = dy dz x̂, v·da = 2xz dy dz = 4z dy dz, so ∫ v·da = ∫∫ 4z dy dz = 16.

(ii) x = 0, da = −dy dz x̂, v·da = −2xz dy dz = 0, so ∫ v·da = 0.

(iii) y = 2, da = dx dz ŷ, v·da = (x+2) dx dz, so ∫ v·da = ∫∫ (x+2) dx dz = 12.

(iv) y = 0, da = −dx dz ŷ, v·da = −(x+2) dx dz, so ∫ v·da = −∫∫ (x+2) dx dz = −12.

(v) z = 2, da = dx dy ẑ, v·da = y(z²−3) dx dy = y dx dy, so ∫ v·da = ∫∫ y dx dy = 4.

The total flux is ∫_surface v·da = 16 + 0 + 12 − 12 + 4 = 20.

(c) Volume Integrals. A volume integral is an expression of the form ∫ T dτ, (1.51)

where T is a scalar function and dτ is an infinitesimal volume element. In Cartesian coordinates, dτ = dx dy dz. (1.52)

For example, if T is the density of a substance (which might vary from point to point), then the volume integral would give the total mass. Occasionally we shall encounter volume integrals of vector functions: ∫ v dτ = ∫ (v_x x̂ + v_y ŷ + v_z ẑ) dτ = x̂ ∫ v_x dτ + ŷ ∫ v_y dτ + ẑ ∫ v_z dτ; (1.53)

because the unit vectors (x̂, ŷ, and ẑ) are constants, they come outside the integral.

Example 1.8. Calculate the volume integral of T = xyz² over the prism in Fig. 1.24.

Solution You can do the three integrals in any order. Let’s do x first: it runs from 0 to (1−y), then y (it goes from 0 to 1), and finally z (0 to 3): ∫ T dτ = ∫_0^3 ∫_0^1 ∫_0^{1−y} z² y x dx dy dz = ∫_0^3 z² dz ∫_0^1 (1−y)² y dy = (9)(1/24) = 3/8.

Problem 1.29 Calculate the line integral of the function v = x² x̂ + 2yz ŷ + y² ẑ from the origin to the point (1,1,1) by three different routes: (a) (0,0,0)→(1,0,0)→(1,1,0)→(1,1,1).

(b) (0,0,0)→(0,0,1)→(0,1,1)→(1,1,1).

(c) The direct straight line.

(d) What is the line integral around the closed loop that goes out along path (a) and back along path (b)?

Problem 1.30 Calculate the surface integral of the function in Ex. 1.7, over the bottom of the box. For consistency, let “upward” be the positive direction. Does the surface integral depend only on the boundary line for this function? What is the total flux over the closed surface of the box (including the bottom)? [Note: For the closed surface, the positive direction is “outward,” and hence “down,” for the bottom face.]

Problem 1.31 Calculate the volume integral of the function T = z² over the tetrahedron with corners at (0,0,0), (1,0,0), (0,1,0), and (0,0,1).

1.3.2 The Fundamental Theorem of Calculus Suppose f(x) is a function of one variable. The fundamental theorem of calculus says: ∫_a^b (df/dx) dx = f(b) − f(a). (1.54)

In case this doesn’t look familiar, I’ll write it another way: ∫ F(x) dx = f(b) − f(a), where df/dx = F(x). The fundamental theorem tells you how to integrate F(x): you think up a function f(x) whose derivative is equal to F.

Geometrical Interpretation: According to Eq. 1.33, df = (df/dx) dx is the infinitesimal change in f when you go from (x) to (x + dx). The fundamental theorem (Eq. 1.54) says that if you chop the interval from a to b (Fig. 1.25) into many tiny pieces, dx, and add up the increments df from each little piece, the result is (not surprisingly) equal to the total change in f: f(b) − f(a). In other words, there are two ways to determine the total change in the function: either subtract the values at the ends or go step-by-step, adding up all the tiny increments as you go. You’ll get the same answer either way.

Notice the basic format of the fundamental theorem: the integral of a derivative over some region is given by the value of the function at the endpoints (boundaries). In vector calculus there are three species of derivative (gradient, divergence, and curl), and each has its own “fundamental theorem,” with essentially the same format. I don’t plan to prove these theorems here; rather, I will explain what they mean, and try to make them plausible. Proofs are given in Appendix A.

1.3.3 The Fundamental Theorem for Gradients Suppose we have a scalar function of three variables T(x,y,z). Starting at point a, we move a small distance dl (Fig. 1.26). According to Eq. 1.37, the function T will change by an amount dT = (∇T)·dl.

Now we move a little further, by an additional small displacement dl₂; the incremental change in T will be (∇T)·dl₂. In this manner, proceeding by infinitesimal steps, we make the journey to point b. At each step we compute the gradient of T (at that point) and dot it into the displacement dl… this gives us the change in T. Evidently the total change in T in going from a to b (along the path selected) is ∫ (∇T)·dl = T(b) − T(a). (1.55)

This is the fundamental theorem for gradients; like the “ordinary” fundamental theorem, it says that the integral (here a line integral) of a derivative (here the gradient) is given by the value of the function at the boundaries (a and b).

Geometrical Interpretation: Suppose you wanted to determine the height of the Eiffel Tower. You could climb the stairs, using a ruler to measure the rise at each step, and adding them all up (that’s the left side of Eq. 1.55), or you could place altimeters at the top and the bottom, and subtract the two readings (that’s the right side); you should get the same answer either way (that’s the fundamental theorem).

Incidentally, as we found in Ex. 1.6, line integrals ordinarily depend on the path taken from a to b. But the right side of Eq. 1.55 makes no reference to the path—only to the endpoints. Evidently, gradients have the special property that their line integrals are path independent: Corollary 1: ∫_a^b (∇T)·dl is independent of the path taken from a to b.

Corollary 2: ∮ (∇T)·dl = 0, since the beginning and end points are identical, and hence T(b) − T(a) = 0.

Example 1.9. Let T = xy², and take point a to be the origin (0,0,0) and b the point (2,1,0). Check the fundamental theorem for gradients.

Solution Although the integral is independent of path, we must pick a specific path in order to evaluate it. Let’s go out along the x axis (step i) and then up (step ii) (Fig. 1.27). As always, dl = dx x̂ + dy ŷ + dz ẑ; ∇T = y² x̂ + 2xy ŷ.

(i) y = 0; dl = dx x̂, ∇T·dl = y² dx = 0, so ∫ ∇T·dl = 0.

(ii) x = 2; dl = dy ŷ, ∇T·dl = 2xy dy = 4y dy, so ∫ ∇T·dl = ∫_0^1 4y dy = 2y²|_0^1 = 2.

The total line integral is 2. Is this consistent with the fundamental theorem? Yes: T(b) − T(a) = 2 − 0 = 2.

Now, just to convince you that the answer is independent of path, let me calculate the same integral along path iii (the straight line from a to b): (iii) y = (1/2)x, dy = (1/2)dx, ∇T·dl = y² dx + 2xy dy = (3/4)x² dx, so ∫ ∇T·dl = ∫_0^2 (3/4)x² dx = (1/4)x³|_0^2 = 2.

Problem 1.32 Check the fundamental theorem for gradients, using T = x² + 4xy + 2yz³, the points a = (0,0,0), b = (1,1,1), and the three paths in Fig. 1.28: (a) (0,0,0)→(1,0,0)→(1,1,0)→(1,1,1); (b) (0,0,0)→(0,0,1)→(0,1,1)→(1,1,1); (c) the parabolic path z = x²; y = x.

1.3.4 The Fundamental Theorem for Divergences The fundamental theorem for divergences states that: ∫_V (∇·v) dτ = ∮_S v·da. (1.56)

In honor, I suppose, of its great importance, this theorem has at least three special names: Gauss’ theorem, Green’s theorem, or simply the divergence theorem. Like the other “fundamental theorems,” it says that the integral of a derivative (in this case the divergence) over a region (in this case a volume, V) is equal to the value of the function at the boundary (in this case the surface S that bounds the volume). Notice that the boundary term is itself an integral (specifically, a surface integral). This is reasonable: the “boundary” of a line is just two endpoints, but the boundary of a volume is a (closed) surface.

Geometrical Interpretation: If v represents the flow of an incompressible fluid, then the flux of v (the right side of Eq. 1.56) is the total amount of fluid passing out through the surface, per unit time. Now, the diverge...

divergence measures the "spreading out" of the vectors from a point—a place of high divergence is like a "faucet," pouring out liquid. If we have a bunch of faucets in a region filled with incompressible fluid, an equal amount of liquid will be forced out through the boundaries of the region. In fact, there are two ways we could determine how much is being produced: (a) we could count up all the faucets, recording how much each puts out, or (b) we could go around the boundary, measuring the flow at each point, and add it all up. You get the same answer either way:

∫(faucets within the volume) = ∫(flow out through the surface).

This, in essence, is what the divergence theorem says.

Example 1.10. Check the divergence theorem using the function

**v** = y² **x̂** + (2xy + z²) **ŷ** + (2yz) **ẑ**

and a unit cube at the origin (Fig. 1.29).

Solution

In this case

∇ · **v** = 2(x + y),

and

∫_V ∇ · **v** dτ = ∫_0^1 ∫_0^1 ∫_0^1 2(x + y) dx dy dz,

∫_0^1 (x + y) dx = 1/2 + y,  ∫_0^1 (1/2 + y) dy = 1,  ∫_0^1 1 dz = 1.

Thus,

∫_V ∇ · **v** dτ = 2.

So much for the left side of the divergence theorem. To evaluate the surface integral we must consider separately the six faces of the cube:

(i) ∫ **v** · d**a** = ∫_0^1 ∫_0^1 y² dy dz = 1/3.

(ii) ∫ **v** · d**a** = − ∫_0^1 ∫_0^1 y² dy dz = −1/3.

(iii) ∫ **v** · d**a** = ∫_0^1 ∫_0^1 (2x + z²) dx dz = 4/3.

(iv) ∫ **v** · d**a** = − ∫_0^1 ∫_0^1 z² dx dz = −1/3.

(v) ∫ **v** · d**a** = ∫_0^1 ∫_0^1 2y dx dy = 1/3.

(vi) ∫ **v** · d**a** = − ∫_0^1 ∫_0^1 0 dx dy = 0.

So the total flux is:

∫ **v** · d**a** = 1/3 − 1/3 + 4/3 − 1/3 + 1/3 + 0 = 2,

as expected.

Problem 1.33 Test the divergence theorem for the function **v** = (xy) **x̂** + (2yz) **ŷ** + (3zx) **ẑ**. Take as your volume the cube shown in Fig. 1.30, with sides of length 2.

1.3.5 The Fundamental Theorem for Curls

The fundamental theorem for curls, which goes by the special name of Stokes' theorem, states that

∫_S (∇ × **v**) · d**a** = ∮_P **v** · d**l**. (1.57)

As always, the integral of a derivative (here, the curl) over a region (here, a patch of surface, S) is equal to the value of the function at the boundary (here, the perimeter of the patch, P). As in the case of the divergence theorem, the boundary term is itself an integral—specifically, a closed line integral.

Geometrical Interpretation: Recall that the curl measures the "twist" of the vectors **v**; a region of high curl is a whirlpool—if you put a tiny paddle wheel there, it will rotate. Now, the integral of the curl over some surface (or, more precisely, the flux of the curl through that surface) represents the "total amount of swirl," and we can determine that just as well by going around the edge and finding how much the flow is following the boundary (Fig. 1.31). Indeed, ∮ **v** · d**l** is sometimes called the circulation of **v**.

You may have noticed an apparent ambiguity in Stokes' theorem: concerning the boundary line integral, which way are we supposed to go around (clockwise or counterclockwise)? If we go the "wrong" way, we'll pick up an overall sign error. The answer is that it doesn't matter which way you go as long as you are consistent, for there is a compensating sign ambiguity in the surface integral: Which way does d**a** point? For a closed surface (as in the divergence theorem), d**a** points in the direction of the outward normal; but for an open surface, which way is "out"? Consistency in Stokes' theorem (as in all such matters) is given by the right-hand rule: if your fingers point in the direction of the line integral, then your thumb fixes the direction of d**a** (Fig. 1.32).

Now, there are plenty of surfaces (infinitely many) that share any given boundary line. Twist a paper clip into a loop, and dip it in soapy water. The soap film constitutes a surface, with the wire loop as its boundary. If you blow on it, the soap film will expand, making a larger surface, with the same boundary. Ordinarily, a flux integral depends critically on what surface you integrate over, but evidently this is not the case with curls. For Stokes' theorem says that ∫ (∇ × **v**) · d**a** is equal to the line integral of **v** around the boundary, and the latter makes no reference to the specific surface you choose.

Corollary 1: ∫ (∇ × **v**) · d**a** depends only on the boundary line, not on the particular surface used.

Corollary 2: ∫ (∇ × **v**) · d**a** = 0 for any closed surface, since the boundary line, like the mouth of a balloon, shrinks down to a point, and hence the right side of Eq. 1.57 vanishes.

These corollaries are analogous to those for the gradient theorem. We will develop the parallel further in due course.

Example 1.11. Suppose **v** = (2xz + 3y²) **ŷ** + (4yz²) **ẑ**. Check Stokes' theorem for the square surface shown in Fig. 1.33.

Solution

Here

∇ × **v** = (4z² − 2x) **x̂** + 2z **ẑ**  and  d**a** = dy dz **x̂**.

(In saying that d**a** points in the x direction, we are committing ourselves to a counterclockwise line integral. We could as well write d**a** = −dy dz **x̂**, but then we would be obliged to go clockwise.) Since x = 0 for this surface,

∫_S (∇ × **v**) · d**a** = ∫_0^1 ∫_0^1 4z² dy dz = 4/3.

Now, what about the line integral? We must break this up into four segments:

(i) x = 0, z = 0, **v** · d**l** = 3y² dy, ∫ **v** · d**l** = ∫_0^1 3y² dy = 1, (ii) x = 0, y = 1, **v** · d**l** = 4z² dz, ∫ **v** · d**l** = ∫_0^1 4z² dz = 4/3, (iii) x = 0, z = 1, **v** · d**l** = 3y² dy, ∫ **v** · d**l** = ∫_1^0 3y² dy = −1, (iv) x = 0, y = 0, **v** · d**l** = 0, ∫ **v** · d**l** = ∫_1^0 0 dz = 0.

So

∮ **v** · d**l** = 1 + 4/3 − 1 + 0 = 4/3.

It checks.

A point of strategy: notice how I handled step (iii). There is a temptation to write d**l** = −dy **ŷ** here, since the path goes to the left. You can get away with this, if you absolutely insist, by running the integral from 0 → 1. But it is much safer to say d**l** = dx **x̂** + dy **ŷ** + dz **ẑ** always (never any minus signs) and let the limits of the integral take care of the direction.

Problem 1.34 Test Stokes' theorem for the function **v** = (xy) **x̂** + (2yz) **ŷ** + (3zx) **ẑ**, using the triangular shaded area of Fig. 1.34.

Problem 1.35 Check Corollary 1 by using the same function and boundary line as in Ex. 1.11, but integrating over the five faces of the cube in Fig. 1.35. The back of the cube is open.

1.3.6 Integration by Parts

The technique known (awkwardly) as integration by parts exploits the product rule for derivatives:

d/dx (fg) = f (dg/dx) + g (df/dx).

Integrating both sides, and invoking the fundamental theorem:

∫_a^b (fg)' dx = (fg)|_a^b = ∫_a^b f (dg/dx) dx + ∫_a^b g (df/dx) dx,

or

∫_a^b f (dg/dx) dx = − ∫_a^b g (df/dx) dx + (fg)|_a^b . (1.58)

That's integration by parts. It applies to the situation in which you are called upon to integrate the product of one function (f) and the derivative of another (g); it says you can transfer the derivative from g to f, at the cost of a minus sign and a boundary term.

Example 1.12. Evaluate the integral

∫_0^∞ x e^{−x} dx.

Solution

The exponential can be expressed as a derivative:

d/dx (e^{−x}) = −e^{−x};

in this case, then, f(x) = x, g(x) = −e^{−x}, and df/dx = 1, so

∫_0^∞ x e^{−x} dx = ∫_0^∞ e^{−x} dx − (x e^{−x})|_0^∞ = −e^{−x}|_0^∞ = 1.

We can exploit the product rules of vector calculus, together with the appropriate fundamental theorems, in exactly the same way. For example, integrating

∇ · (f **A**) = f (∇ · **A**) + **A** · (∇f)

over a volume, and invoking the divergence theorem, yields

∫_V ∇ · (f **A**) dτ = ∫_V f (∇ · **A**) dτ + ∫_V **A** · (∇f) dτ = ∫_S f **A** · d**a**,

or

∫_V f (∇ · **A**) dτ = − ∫_V **A** · (∇f) dτ + ∫_S f **A** · d**a**. (1.59)

Here again the integrand is the product of one function (f) and the derivative (in this case the divergence) of another (**A**), and integration by parts licenses us to transfer the derivative from **A** to f (where it becomes a gradient), at the cost of a minus sign and a boundary term (in this case a surface integral).

You might wonder how often one is likely to encounter an integral involving the product of one function and the derivative of another; the answer is surprisingly often, and integration by parts turns out to be one of the most powerful tools in vector calculus.

Problem 1.36 (a) Show that ∫_S f (∇ × **A**) · d**a** = ∫_S [**A** × (∇f)] · d**a** + ∮_P f **A** · d**l**. (1.60)

(b) Show that ∫_V **B** · (∇ × **A**) dτ = ∫_V **A** · (∇ × **B**) dτ + ∫_S (**A** × **B**) · d**a**. (1.61)

## 1.4 CURVILINEAR COORDINATES

1.4.1 Spherical Coordinates

You can label a point P by its Cartesian coordinates (x, y, z), but sometimes it is more convenient to use spherical coordinates (r, θ, φ); r is the distance from the origin (the magnitude of the position vector **r**), θ (the angle down from the z axis) is called the polar angle, and φ (the angle around from the x axis) is the azimuthal angle. Their relation to Cartesian coordinates can be read from Fig. 1.36:

x = r sin θ cos φ,   y = r sin θ sin φ,   z = r cos θ. (1.62)

Figure 1.36 also shows three unit vectors, **r̂**, **θ̂**, **φ̂**, pointing in the direction of increase of the corresponding coordinates. They constitute an orthogonal (mutually perpendicular) basis set (just like **x̂**, **ŷ**, **ẑ**), and any vector **A** can be expressed in terms of them, in the usual way:

**A** = A_r **r̂** + A_θ **θ̂** + A_φ **φ̂**; (1.63)

A_r, A_θ, and A_φ are the radial, polar, and azimuthal components of **A**. In terms of the Cartesian unit vectors,

**r̂** = sin θ cos φ **x̂** + sin θ sin φ **ŷ** + cos θ **ẑ**, **θ̂** = cos θ cos φ **x̂** + cos θ sin φ **ŷ** − sin θ **ẑ**, (1.64)

**φ̂** = −sin φ **x̂** + cos φ **ŷ**,

as you can check for yourself (Prob. 1.38). I have put these formulas inside the back cover, for easy reference.

But there is a poisonous snake lurking here that I'd better warn you about: **r̂**, **θ̂**, and **φ̂** are associated with a particular point P, and they change direction as P moves around. For example, **r̂** always points radially outward, but "radially outward" can be the x direction, the y direction, or any other direction, depending on where you are. In Fig. 1.37, **A** = **ŷ** and **B** = −**ŷ**, and yet both of them would be written as A_r **r̂** in spherical coordinates. One could take account of this by explicitly indicating the point of reference: **r̂**(θ, φ), **θ̂**(θ, φ), **φ̂**(θ, φ), but this would be cumbersome, and as long as you are alert to the problem, I don't think it will cause difficulties.⁹ In particular, do not naïvely combine the spherical components of vectors associated with different points (in Fig. 1.37, **A** + **B** = 0, not 2 A_r **r̂**, and **A** · **B** = −1, not +1). Beware of differentiating a vector that is expressed in spherical coordinates;...

Since the unit vectors themselves are functions of position (∂r̂/∂θ = θ̂, for example). And do not take r̂, θ̂, and φ̂ outside an integral, as I did with x̂, ŷ, and ẑ in Eq. 1.53. In general, if you’re uncertain about the validity of an operation, rewrite the problem using Cartesian coordinates, for which this difficulty does not arise.

An infinitesimal displacement in the r̂ direction is simply dr (Fig. 1.38a), just as an infinitesimal element of length in the x direction is dx: dl_r = dr. (1.65)

I claimed back at the beginning that vectors have no location, and I’ll stand by that. The vectors themselves live “out there,” completely independent of our choice of coordinates. But the notation we use to represent them does depend on the point in question, in curvilinear coordinates.

On the other hand, an infinitesimal element of length in the θ̂ direction (Fig. 1.38b) is not just dθ (that’s an angle—it doesn’t even have the right units for a length); rather, dl_θ = r dθ. (1.66)

Similarly, an infinitesimal element of length in the φ̂ direction (Fig. 1.38c) is dl_φ = r sinθ dφ. (1.67)

Thus the general infinitesimal displacement dl is dl = dr r̂ + r dθ θ̂ + r sinθ dφ φ̂. (1.68)

This plays the role (in line integrals, for example) that dl = dx x̂ + dy ŷ + dz ẑ played in Cartesian coordinates.

The infinitesimal volume element dτ, in spherical coordinates, is the product of the three infinitesimal displacements: dτ = dl_r dl_θ dl_φ = r² sinθ dr dθ dφ. (1.69)

I cannot give you a general expression for surface elements da, since these depend on the orientation of the surface. You simply have to analyze the geometry for any given case (this goes for Cartesian and curvilinear coordinates alike). If you are integrating over the surface of a sphere, for instance, then r is constant, whereas θ and φ change (Fig. 1.39), so da = dl_θ dl_φ r̂ = r² sinθ dθ dφ r̂.

On the other hand, if the surface lies in the xy plane, say, so that θ is constant (to wit: π/2) while r and φ vary, then da = dl_r dl_φ θ̂ = r dr dφ θ̂.

Notice, finally, that r ranges from 0 to ∞, φ from 0 to 2π, and θ from 0 to π (not 2π—that would count every point twice).10

10 Alternatively, you could run φ from 0 to π (the “eastern hemisphere”) and cover the “western hemisphere” by extending θ from π up to 2π. But this is very bad notation, since, among other things, sinθ will then run negative, and you’ll have to put absolute value signs around that term in volume and surface elements (area and volume being intrinsically positive quantities).

Example 1.13. Find the volume of a sphere of radius R.

Solution V = ∫ dτ = ∫_{r=0}^{R} ∫_{θ=0}^{π} ∫_{φ=0}^{2π} r² sinθ dr dθ dφ = (∫_{0}^{R} r² dr)(∫_{0}^{π} sinθ dθ)(∫_{0}^{2π} dφ)

= (R³/3)(2)(2π) = (4/3)πR³ (not a big surprise).

So far we have talked only about the geometry of spherical coordinates. Now I would like to “translate” the vector derivatives (gradient, divergence, curl, and Laplacian) into r, θ, φ notation. In principle, this is entirely straightforward: in the case of the gradient, ∇T = ∂T/∂x x̂ + ∂T/∂y ŷ + ∂T/∂z ẑ, for instance, we would first use the chain rule to expand the partials: ∂T/∂x = (∂T/∂r)(∂r/∂x) + (∂T/∂θ)(∂θ/∂x) + (∂T/∂φ)(∂φ/∂x).

The terms in parentheses could be worked out from Eq. 1.62—or rather, the inverse of those equations (Prob. 1.37). Then we’d do the same for ∂T/∂y and ∂T/∂z. Finally, we’d substitute in the formulas for x̂, ŷ, and ẑ in terms of r̂, θ̂, and φ̂ (Prob. 1.38). It would take an hour to figure out the gradient in spherical coordinates by this brute-force method. I suppose this is how it was first done, but there is a much more efficient indirect approach, explained in Appendix A, which has the extra advantage of treating all coordinate systems at once. I described the “straightforward” method only to show you that there is nothing subtle or mysterious about transforming to spherical coordinates: you’re expressing the same quantity (gradient, divergence, or whatever) in different notation, that’s all.

Here, then, are the vector derivatives in spherical coordinates: Gradient: ∇T = ∂T/∂r r̂ + (1/r) ∂T/∂θ θ̂ + (1/(r sinθ)) ∂T/∂φ φ̂. (1.70)

Divergence: ∇·v = (1/r²) ∂/∂r (r² v_r) + (1/(r sinθ)) ∂/∂θ (sinθ v_θ) + (1/(r sinθ)) ∂v_φ/∂φ. (1.71)

Curl: ∇×v = (1/(r sinθ)) [ ∂/∂θ (sinθ v_φ) - ∂v_θ/∂φ ] r̂ + (1/r) [ (1/sinθ) ∂v_r/∂φ - ∂/∂r (r v_φ) ] θ̂ + (1/r) [ ∂/∂r (r v_θ) - ∂v_r/∂θ ] φ̂. (1.72)

Laplacian: ∇²T = (1/r²) ∂/∂r (r² ∂T/∂r) + (1/(r² sinθ)) ∂/∂θ (sinθ ∂T/∂θ) + (1/(r² sin²θ)) ∂²T/∂φ². (1.73)

For reference, these formulas are listed inside the front cover.

Problem 1.37 Find formulas for r, θ, φ in terms of x, y, z (the inverse, in other words, of Eq. 1.62).

• Problem 1.38 Express the unit vectors r̂, θ̂, φ̂ in terms of x̂, ŷ, ẑ (that is, derive Eq. 1.64). Check your answers several ways (r̂·r̂ =? 1, θ̂·φ̂ =? 0, r̂×θ̂ =? φ̂,...). Also work out the inverse formulas, giving x̂, ŷ, ẑ in terms of r̂, θ̂, φ̂ (and θ, φ).

• Problem 1.39 (a) Check the divergence theorem for the function v = r² r̂, using as your volume the sphere of radius R, centered at the origin.

(b) Do the same for v = (1/r²) r̂. (If the answer surprises you, look back at Prob. 1.16.)

Problem 1.40 Compute the divergence of the function v = (r cosθ) r̂ + (r sinθ) θ̂ + (r sinθ cosφ) φ̂.

Check the divergence theorem for this function, using as your volume the inverted hemispherical bowl of radius R, resting on the xy plane and centered at the origin (Fig. 1.40).

Problem 1.41 Compute the gradient and Laplacian of the function T = r (cosθ + sinθ cosφ). Check the Laplacian by converting T to Cartesian coordinates and using Eq. 1.42. Test the gradient theorem for this function, using the path shown in Fig. 1.41, from (0,0,0) to (0,0,2).

1.4.2 Cylindrical Coordinates The cylindrical coordinates (s, φ, z) of a point P are defined in Fig. 1.42. Notice that φ has the same meaning as in spherical coordinates, and z is the same as Cartesian; s is the distance to P from the z axis, whereas the spherical coordinate r is the distance from the origin. The relation to Cartesian coordinates is x = s cosφ, y = s sinφ, z = z. (1.74)

The unit vectors (Prob. 1.42) are ŝ = cosφ x̂ + sinφ ŷ, φ̂ = -sinφ x̂ + cosφ ŷ, (1.75)

ẑ = ẑ.

The infinitesimal displacements are dl_s = ds, dl_φ = s dφ, dl_z = dz, (1.76)

so dl = ds ŝ + s dφ φ̂ + dz ẑ, (1.77)

and the volume element is dτ = s ds dφ dz. (1.78)

The range of s is 0→∞, φ goes from 0→2π, and z from -∞ to ∞.

The vector derivatives in cylindrical coordinates are: Gradient: ∇T = ∂T/∂s ŝ + (1/s) ∂T/∂φ φ̂ + ∂T/∂z ẑ. (1.79)

Divergence: ∇·v = (1/s) ∂(s v_s)/∂s + (1/s) ∂v_φ/∂φ + ∂v_z/∂z. (1.80)

Curl: ∇×v = (1/s) [ ∂v_z/∂φ - ∂(s v_φ)/∂z ] ŝ + [ ∂v_s/∂z - ∂v_z/∂s ] φ̂ + (1/s) [ ∂(s v_φ)/∂s - ∂v_s/∂φ ] ẑ. (1.81)

Laplacian: ∇²T = (1/s) ∂/∂s (s ∂T/∂s) + (1/s²) ∂²T/∂φ² + ∂²T/∂z². (1.82)

These formulas are also listed inside the front cover.

Problem 1.42 Express the cylindrical unit vectors ŝ, φ̂, ẑ in terms of x̂, ŷ, ẑ (that is, derive Eq. 1.75). “Invert” your formulas to get x̂, ŷ, ẑ in terms of ŝ, φ̂, ẑ (and φ).

Problem 1.43 (a) Find the divergence of the function v = s (2 + sin2φ) ŝ + s sinφ cosφ φ̂ + 3z ẑ.

(b) Test the divergence theorem for this function, using the quarter-cylinder (radius 2, height 5) shown in Fig. 1.43.

(c) Find the curl of v.

## 1.5 THE DIRAC DELTA FUNCTION

1.5.1 The Divergence of r̂/r² Consider the vector function v = r̂/r². (1.83)

At every location, v is directed radially outward (Fig. 1.44); if ever there was a function that ought to have a large positive divergence, this is it. And yet, when you actually calculate the divergence (using Eq. 1.71), you get precisely zero: ∇·v = (1/r²) ∂/∂r (r² * (1/r²)) = (1/r²) ∂/∂r (1) = 0. (1.84)

(You will have encountered this paradox already, if you worked Prob. 1.16.) The plot thickens when we apply the divergence theorem to this function. Suppose we integrate over a sphere of radius R, centered at the origin (Prob. 1.38b); the surface integral is ∮ v·da = ∮ (r̂/R²)·(R² sinθ dθ dφ r̂) = (∫_{0}^{π} sinθ dθ)(∫_{0}^{2π} dφ) = 4π. (1.85)

But the volume integral, ∫ (∇·v) dτ, is zero, if we are really to believe Eq. 1.84. Does this mean that the divergence theorem is false? What’s going on here?

The source of the problem is the point r = 0, where v blows up (and where, in Eq. 1.84, we have unwittingly divided by zero). It is quite true that ∇·v = 0 everywhere except the origin, but right at the origin the situation is more complicated. Notice that the surface integral (Eq. 1.85) is independent of R; if the divergence theorem is right (and it is), we should get ∫ (∇·v) dτ = 4π for any sphere centered at the origin, no matter how small. Evidently the entire contribution must be coming from the point r = 0! Thus, ∇·v has the bizarre property that it vanishes everywhere except at one point, and yet its integral (over any volume containing that point) is 4π. No ordinary function behaves like that. (On the other hand, a physical example does come to mind: the density (mass per unit volume) of a point particle. It’s zero except at the exact location of the particle, and yet its integral is finite—namely, the mass of the particle.) What we have stumbled on is a mathematical object known to physicists as the Dirac delta function. It arises in many branches of theoretical physics. Moreover, the specific problem at hand (the divergence of the function r̂/r²) is not just some arcane curiosity—it is, in fact, central to the whole theory of electrodynamics. So it is worthwhile to pause here and study the Dirac delta function with some care.

1.5.2 The One-Dimensional Dirac Delta Function The one-dimensional Dirac delta function, δ(x), can be pictured as an infinitely high, infinitesimally narrow “spike,” with area 1 (Fig. 1.45). That is to say: δ(x) = { 0, if x ≠ 0 { ∞, if x = 0 and11 ∫_{-∞}^{∞} δ(x) dx = 1. (1.87)

11 Notice that the dimensions of δ(x) are one over the dimensions of its argument; if x is a length, δ(x) carries the units m⁻¹.

Technically, δ(x) is not a function at all, since its value is not finite at x = 0; in the mathematical literature it is known as a generalized function, or distribution. It is, if you like, the limit of a sequence of functions, such as rectangles R_n(x), of height n and width 1/n, centered at the origin, as n → ∞.

等腰三角形 \( T(x) \)，高度为 \( n \)，底边为 \( 2/n \)（图 1.46）。

如果 \( f(x) \) 是一个“普通”函数（即不是另一个δ函数——实际上，为安全起见，我们说 \( f(x) \) 是连续的），那么乘积 \( f(x)\delta(x) \) 除在 \( x = 0 \) 处外处处为零。因此 \[ f(x)\delta(x) = f(0)\delta(x). \tag{1.88} \]

（这是关于δ函数最重要的事实，所以请务必理解为什么它成立：由于乘积除在 \( x = 0 \) 外处处为零，我们不妨用 \( f(x) \) 在原点取的值来替换 \( f(x) \)。）特别地， \[ \int_{-\infty}^{\infty} f(x)\delta(x) dx = f(0) \int_{-\infty}^{\infty} \delta(x) dx = f(0). \tag{1.89} \]

因此，在积分号下，δ函数“挑出” \( f(x) \) 在 \( x = 0 \) 处的值。（这里及以下，积分不必从 \( -\infty \) 到 \( +\infty \)；只要积分区域覆盖δ函数所在的点，从 \( -a \) 到 \( +a \) 也同样可以。）

当然，我们可以将尖峰从 \( x = 0 \) 移动到另一点 \( x = a \)（图 1.47）： \[ \delta(x-a)

\]

面积 1 \[ a \quad x \]

图 1.47 \[ \delta(x-a) = \begin{cases} 0, & \text{如果 } x \neq a \\ \infty, & \text{如果 } x = a \end{cases}, \quad \text{且} \quad \int_{-\infty}^{\infty} \delta(x-a) dx = 1. \tag{1.90} \]

方程 1.88 变为 \[ f(x)\delta(x-a) = f(a)\delta(x-a), \tag{1.91} \]

而方程 1.89 推广为 \[ \int_{-\infty}^{\infty} f(x)\delta(x-a) dx = f(a). \tag{1.92} \]

例 1.14. 计算积分 \[ \int x^3 \delta(x-2) dx.

\]

解 δ函数挑出 \( x^3 \) 在点 \( x = 2 \) 处的值，因此积分结果为 \( 2^3 = 8 \)。然而，请注意，如果上限是 1（而不是 3），答案将是 0，因为此时尖峰位于积分区域之外。

尽管 δ 本身不是一个合法的函数，但关于 δ 的积分是完全可接受的。事实上，最好将δ函数视为总是打算在积分号下使用的东西。特别地，涉及δ函数的两个表达式（比如 \( D_1(x) \) 和 \( D_2(x) \)）被认为相等，如果对于所有（“普通”）函数 \( f(x) \)， \[ \int_{-\infty}^{\infty} f(x) D_1(x) dx = \int_{-\infty}^{\infty} f(x) D_2(x) dx, \tag{1.93} \]

12 我强调积分必须对任意 \( f(x) \) 相等。假设 \( D_1(x) \) 和 \( D_2(x) \) 实际上不同，比如在点 \( x=17 \) 的邻域内。那么我们可以选择一个在 \( x=17 \) 附近急剧峰值的函数 \( f(x) \)，这样积分就不会相等。

例 1.15. 证明 \[ \delta(kx) = \frac{1}{|k|} \delta(x), \tag{1.94} \]

其中 \( k \) 是任意（非零）常数。（特别地，\( \delta(-x) = \delta(x) \)。）

解对于任意测试函数 \( f(x) \)，考虑积分 \[ \int f(x) \delta(kx) dx.

\]

做变量替换，令 \( y \equiv kx \)，则 \( x = y/k \)，且 \( dx = (1/k) dy \)。如果 \( k \) 为正，积分范围仍从 \( -\infty \) 到 \( +\infty \)；但如果 \( k \) 为负，则 \( x = \infty \) 意味着 \( y = -\infty \)，反之亦然，因此积分上下限顺序相反。恢复“正确”的顺序需要一个负号。因此 \[ \int_{-\infty}^{\infty} f(x) \delta(kx) dx = \pm \int_{-\infty}^{\infty} f(y/k) \delta(y) \frac{dy}{k} = \pm \frac{1}{k} f(0) = \frac{1}{|k|} f(0).

\]

（负号适用于 \( k \) 为负的情况，我们通过最终在 \( k \) 周围加上绝对值符号来巧妙处理，如上所示。）因此，在积分号下，\( \delta(kx) \) 与 \( (1/|k|)\delta(x) \) 具有相同的效果： \[ \int_{-\infty}^{\infty} f(x) \delta(kx) dx = \int_{-\infty}^{\infty} f(x) \frac{1}{|k|} \delta(x) dx.

\]

根据判据方程 1.93，因此 \( \delta(kx) \) 和 \( (1/|k|)\delta(x) \) 相等。

问题 1.44 计算下列积分： (a) \( \int_{6}^{3x^2-2x-1) \delta(x-3) dx \).

(b) \( \int_{5}^{\cos x} \delta(x-\pi) dx \).

(c) \( \int_{3}^{x^3} \delta(x+1) dx \).

(d) \( \int_{-\infty}^{\infty} \ln(x+3) \delta(x+2) dx \).

问题 1.45 计算下列积分： (a) \( \int_{-2}^{2} (2x+3) \delta(3x) dx \).

(b) \( \int_{2}^{(x^3+3x+2) \delta(1-x) dx \).

(c) \( \int_{-1}^{1} 9x^2 \delta(3x+1) dx \).

(d) \( \int_{-\infty}^{a} \delta(x-b) dx \).

问题 1.46 (a) 证明 \[ x \frac{d}{dx} (\delta(x)) = -\delta(x).

\]

[提示：使用分部积分法。]

50 第1章 矢量分析

(b) 令 \( \theta(x) \) 为阶跃函数： \[ \theta(x) \equiv \begin{cases} 1, & \text{如果 } x > 0 \\ 0, & \text{如果 } x \leq 0 \end{cases}. \tag{1.95} \]

证明 \( d\theta/dx = \delta(x) \)。

1.5.3 三维δ函数将δ函数推广到三维很简单： \[ \delta^3(\mathbf{r}) = \delta(x)\delta(y)\delta(z). \tag{1.96} \]

（一如既往，\( \mathbf{r} \equiv x\hat{\mathbf{x}} + y\hat{\mathbf{y}} + z\hat{\mathbf{z}} \) 是位置矢量，从原点延伸到点 \( (x,y,z) \)。）这个三维δ函数除在 \( (0,0,0) \) 处外处处为零，在该点处发散。其体积积分为 1： \[ \int_{\text{全空间}} \delta^3(\mathbf{r}) d\tau = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \delta(x)\delta(y)\delta(z) \, dx\,dy\,dz = 1. \tag{1.97} \]

并且，推广方程 1.92， \[ \int_{\text{全空间}} f(\mathbf{r}) \delta^3(\mathbf{r}-\mathbf{a}) d\tau = f(\mathbf{a}). \tag{1.98} \]

与一维情况类似，与 δ 的积分挑出函数 \( f \) 在尖峰所在位置的值。

我们现在可以解决第 1.5.1 节中引入的悖论。如你所回忆，我们发现 \( \hat{\mathbf{r}}/r^2 \) 的散度除原点外处处为零，然而它在任何包含原点的体积上的积分是一个常数（即：\( 4\pi \)）。这些正是狄拉克δ函数的定义条件；显然 \[ \nabla \cdot \left( \frac{\hat{\mathbf{r}}}{r^2} \right) = 4\pi \delta^3(\mathbf{r}). \tag{1.99} \]

更一般地， \[ \nabla \cdot \left( \frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \right) = 4\pi \delta^3(\mathbf{r}), \tag{1.100} \]

其中，一如既往，\( \mathfrak{r} \equiv \mathbf{r} - \mathbf{r}' \) 是分离矢量。注意这里的微分是对 \( \mathbf{r} \) 进行的，而 \( \mathbf{r}' \) 保持恒定。顺便提一下，因为 \[ \nabla \left( \frac{1}{\mathfrak{r}} \right) = -\frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \tag{1.101} \]

（问题 1.13b），因此 \[ \nabla^2 \left( \frac{1}{\mathfrak{r}} \right) = -4\pi \delta^3(\mathbf{r}). \tag{1.102} \]

例 1.16. 计算积分 \[ J = \int_V (\mathfrak{r}^2 + 2) \nabla \cdot \left( \frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \right) d\tau, \]

其中 \( V \) 是一个以原点为中心、半径为 \( R \) 的球体。

解 1 使用方程 1.99 重写散度，并用方程 1.98 计算积分： \[ J = \int_V (\mathfrak{r}^2 + 2) 4\pi \delta^3(\mathbf{r}) d\tau = 4\pi (0 + 2) = 8\pi.

\]

这个一步到位的解法展示了δ函数的力量和优美，但我想向你展示第二种方法，虽然繁琐得多，但有助于说明分部积分法（第 1.3.6 节）。

解 2 使用方程 1.59，我们将导数从 \( \hat{\mathfrak{r}}/\mathfrak{r}^2 \) 转移到 \( (\mathfrak{r}^2 + 2) \) 上： \[ J = -\int_V \frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \cdot [\nabla(\mathfrak{r}^2 + 2)] d\tau + \oint_{\text{表面}} (\mathfrak{r}^2 + 2) \frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \cdot d\mathbf{a}.

\]

梯度是 \[ \nabla(\mathfrak{r}^2 + 2) = 2\mathfrak{r} \hat{\mathfrak{r}}, \]

因此体积积分变为 \[ \int_V \frac{2\mathfrak{r} \hat{\mathfrak{r}}}{\mathfrak{r}^2} \cdot \hat{\mathfrak{r}} d\tau = \int_V \frac{2}{r} d\tau = \int_0^R \int_0^\pi \int_0^{2\pi} \frac{2}{r} r^2 \sin\theta \, dr\,d\theta\,d\phi = 8\pi \int_0^R r \, dr = 4\pi R^2.

\]

同时，在球体边界上（此处 \( \mathfrak{r} = R \)）， \[ d\mathbf{a} = R^2 \sin\theta \, d\theta \, d\phi \, \hat{\mathbf{r}}, \]

因此表面积分是 \[ \oint (R^2 + 2) \frac{\hat{\mathbf{r}}}{R^2} \cdot (R^2 \sin\theta \, d\theta \, d\phi \, \hat{\mathbf{r}}) = (R^2 + 2) \int \sin\theta \, d\theta \, d\phi = 4\pi (R^2 + 2).

\]

将所有结果放在一起， \[ J = -4\pi R^2 + 4\pi (R^2 + 2) = 8\pi, \]

与之前一样。

13 在恰当的数学行话中，“球面”指表面，“球体”指它包围的体积。但物理学家（像往常一样）对这类事情很马虎，我用“球”这个词同时指代表面和体积。如果从上下文中意思不清楚，我会写“球面”或“球体”。语言警察告诉我前者是冗余的，后者是矛盾修辞法，但我的一些物理学同行的投票显示，这（对我们来说）是标准用法。

问题 1.47 (a) 写出位于 \( \mathbf{r}' \) 的点电荷 \( q \) 的体电荷密度 \( \rho(\mathbf{r}) \) 的表达式。确保 \( \rho \) 的体积分等于 \( q \)。

(b) 一个电偶极子的体电荷密度是多少？它由位于原点的点电荷 \( -q \) 和位于 \( \mathbf{a} \) 的点电荷 \( +q \) 组成。

(c) 一个均匀、无限薄、半径为 \( R \)、总电荷为 \( Q \)、以原点为中心的球壳的体电荷密度（用球坐标表示）是多少？[注意：对全空间的积分必须等于 \( Q \)。]

问题 1.48 计算下列积分： (a) \( \int (\mathfrak{r}^2 + \mathbf{r} \cdot \mathbf{a} + a^2) \delta^3(\mathbf{r}-\mathbf{a}) d\tau \)，其中 \( \mathbf{a} \) 是固定矢量，\( a \) 是其大小，积分遍及全空间。

(b) \( \int_V |\mathbf{r}-\mathbf{b}|^2 \delta^3(5\mathbf{r}) d\tau \)，其中 \( V \) 是以原点为中心、边长为 2 的立方体，且 \( \mathbf{b} = 4\hat{\mathbf{y}} + 3\hat{\mathbf{z}} \)。

(c) \( \int_V \left( r^4 + r^2 (\mathbf{r} \cdot \mathbf{c}) + c^4 \right) \delta^3(\mathbf{r}-\mathbf{c}) d\tau \)，其中 \( V \) 是以原点为中心、半径为 6 的球体，\( \mathbf{c} = 5\hat{\mathbf{x}} + 3\hat{\mathbf{y}} + 2\hat{\mathbf{z}} \)，\( c \) 是其大小。

(d) \( \int_V \mathbf{r} \cdot (\mathbf{d}-\mathbf{r}) \delta^3(\mathbf{e}-\mathbf{r}) d\tau \)，其中 \( \mathbf{d} = (1,2,3) \)，\( \mathbf{e} = (3,2,1) \)，\( V \) 是以 \( (2,2,2) \) 为中心、半径为 1.5 的球体。

问题 1.49 计算积分 \[ J = \int_V e^{-r} \nabla \cdot \left( \frac{\hat{\mathfrak{r}}}{\mathfrak{r}^2} \right) d\tau \]

（其中 \( V \) 是以原点为中心、半径为 \( R \) 的球体）用两种不同的方法，如例 1.16 所示。

## 1.6 矢量场理论

1.6.1 亥姆霍兹定理自法拉第以来，电学和磁学定律一直用矢量场 \( \mathbf{E} \) 和 \( \mathbf{B} \) 来表述。像许多物理定律一样，这些定律最紧凑地表示为微分方程。由于 \( \mathbf{E} \) 和 \( \mathbf{B} \) 是矢量，微分方程自然涉及矢量导数：散度和旋度。事实上，麦克斯韦将整个理论归纳为四个方程，分别指定了 \( \mathbf{E} \) 和 \( \mathbf{B} \) 的散度和旋度。

麦克斯韦的表述提出了一个重要的数学问题：一个矢量函数在多大程度上由其散度和旋度决定？换句话说，如果我告诉你 \( \mathbf{F} \)（代表 \( \mathbf{E} \) 或 \( \mathbf{B} \)，视情况而定）的散度是一个指定的（标量）函数 \( D \)， \[ \nabla \cdot \mathbf{F} = D, \]

且 \( \mathbf{F} \) 的旋度是一个指定的（矢量）函数 \( \mathbf{C} \)， \[ \nabla \times \mathbf{F} = \mathbf{C}, \]

（为了保持一致性，\( \mathbf{C} \) 必须是无散的，\( \nabla \cdot \mathbf{C} = 0 \)，因为旋度的散度总是零），那么你能确定函数 \( \mathbf{F} \) 吗？

嗯……不完全。例如，你可能在问题 1.20 中已经发现，存在许多函数，其散度和旋度处处都为零——当然，平凡的解 \( \mathbf{F} = 0 \)，但还有 \( \mathbf{F} = yz\hat{\mathbf{x}} + zx\hat{\mathbf{y}} + xy\hat{\mathbf{z}} \)，\( \mathbf{F} = \sin x \cosh y \hat{\mathbf{x}} - \cos x \sinh y \hat{\mathbf{y}} \)，等等。要解微分方程，还必须提供适当的边界条件。在电动力学中，我们通常要求场在“无穷远处”（远离所有电荷）趋于零。有了这个额外的信息，亥姆霍兹定理保证场由其散度和旋度唯一确定。（亥姆霍兹定理在附录 B 中讨论。）

1.6.2 势如果一个矢量场 \( (\mathbf{F}) \) 的旋度（处处）为 (b) ∮F·da是独立于表面的，对任何给定的边界线成立。

(c) ∮F·da = 0，对任何闭合曲面成立。

(d) F是某个矢量函数的旋度：F=∇×A。

矢量势不是唯一的——任意标量函数的梯度可以加到A上而不影响其旋度，因为梯度的旋度为零。

你现在应该能够证明这些定理中的所有联系，除了那些表明(a)、(b)或(c)蕴含(d)的。那些更微妙，将在后面讨论。顺便提一下，在所有情况下（无论其旋度和散度可能是什么）一个矢量场F都可以写成一个标量的梯度加上一个矢量的旋度：15 F = -∇V + ∇×A（总是）。 (1.105)

问题1.50 (a) 设F₁ = x²ẑ 和 F₂ = x̂x + ŷy + ẑz。计算F₁和F₂的散度和旋度。哪一个可以写成一个标量的梯度？找出一个能做到这一点的标量势。哪一个可以写成一个矢量的旋度？找出一个合适的矢量势。

15在物理学中，“场”一词泛指任何位置(x, y, z)和时间(t)的函数。但在电动力学中，两个特定的场（E和B）如此重要以至于抢先占用了这个词。因此从技术上讲，势也是“场”，但我们从不这样称呼它们。

## 1.6 矢量场理论

(b) 证明F = yzx̂ + zxŷ + xyẑ 既可以写成一个标量的梯度，也可以写成一个矢量的旋度。找出这个函数的标量势和矢量势。

问题1.51 对于定理1，证明(d)⇒(a)，(a)⇒(c)，(c)⇒(b)，(b)⇒(c)，以及(c)⇒(a)。

问题1.52 对于定理2，证明(d)⇒(a)，(a)⇒(c)，(c)⇒(b)，(b)⇒(c)，以及(c)⇒(a)。

问题1.53 (a) 问题1.15中的哪些矢量可以表示为一个标量的梯度？找出一个能做到这一点的标量函数。

(b) 哪些可以表示为一个矢量的旋度？找出一个这样的矢量。

更多关于第1章的问题问题1.54 对于函数 v = r²cosθ r̂ + r²cosφ θ̂ - r²cosθ sinφ φ̂，使用半径为R的球体的一个八分体（图1.48）作为你的体积来验证散度定理。确保你包含了整个表面。[答案：πR⁴/4]

问题1.55 使用函数 v = aŷx + bxŷ（a和b是常数）和xy平面内以原点为中心、半径为R的圆路径来验证斯托克斯定理。[答案：πR²(b-a)]

问题1.56 计算函数 v = 6x̂ + yz² ŷ + (3y + z) ẑ 沿图1.49所示三角形路径的线积分。使用斯托克斯定理验证你的答案。[答案：8/3]

问题1.57 计算函数 v = (r cos 2θ) r̂ - (r cos θ sin θ) θ̂ + 3r φ̂ 沿图1.50所示路径（点以其笛卡尔坐标标记）的线积分。用柱坐标或球坐标均可。使用斯托克斯定理验证你的答案。[答案：3π/2]

z (0,1,2)

R (0,1,0)

y 1 y (1,0,0) y x x 图1.48 图1.49 图1.50

56 第1章 矢量分析 (0,0,a)

30º (0,2a,0)

x (a,0,0) x 图1.51 图1.52

问题1.58 对于函数 v = ŷz，使用图1.51所示的三角形曲面验证斯托克斯定理。[答案：a²]

问题1.59 对于函数 v = r² sinθ r̂ + 4r² cosθ θ̂ + r² tanθ φ̂，使用图1.52所示的“冰淇淋锥”体积（顶部是球面，半径为R，中心在原点）来验证散度定理。[答案：(πR⁴/12)(2π + 3√3)]

问题1.60 这里有两个对基本定理的巧妙验证： (a) 结合梯度定理的推论2与斯托克斯定理（这里v=∇T）。证明结果与你已知的关于二阶导数的结论一致。

(b) 结合斯托克斯定理的推论2与散度定理。证明结果与你已知的结论一致。

• 问题1.61 尽管梯度、散度和旋度定理是矢量微积分的基本积分定理，但可以从它们推导出许多推论。证明： (a) ∫_V (∇T) dτ = ∫_S T da。[提示：在散度定理中令v=cT，其中c是常数；使用乘积法则。]

(b) ∫_V (∇×v) dτ = - ∫_S v× da。[提示：在散度定理中用(v×c)替换v。]

(c) ∫_V [T∇²U + (∇T)·(∇U)] dτ = ∫_S (T∇U)· da。[提示：在散度定理中令v=T∇U。]

(d) ∫_V (T∇²U - U∇²T) dτ = ∫_S (T∇U - U∇T)· da。[注：这有时被称为格林第二恒等式；它来自(c)，后者被称为格林恒等式。]

(e) ∫_S ∇T × da = - ∮_P T dl。[提示：在斯托克斯定理中令v=cT。]

## 1.6 矢量场理论

• 问题1.62 积分 a ≡ ∫_S da (1.106)

有时被称为曲面S的矢量面积。如果S恰好是平的，那么|a|显然是普通的（标量的）面积。

(a) 求半径为R的半球形碗的矢量面积。

(b) 证明对于任何闭合曲面，a=0。[提示：使用习题1.61a。]

(c) 证明对于共享相同边界的所有曲面，a是相同的。

(d) 证明 a = ½ ∮ r × dl, (1.107)

其中积分是沿边界线。[提示：一种方法是在原点处画出由该回路所对的锥体。将锥面分成许多无限小的三角楔形，每个楔形的顶点在原点，对边为dl，并利用叉积的几何解释（图1.8）。]

(e) 证明 ∮ (c·r) dl = a × c, (1.108)

对于任何常矢量c。[提示：在习题1.61e中令T = c·r。]

• 问题1.63 (a) 求函数 v = r̂ / r 的散度。首先直接计算，如式1.84。使用散度定理测试你的结果，如式1.85。在原点是否存在像 r̂/r² 那样的δ函数？rⁿ r̂的散度的一般公式是什么？[答案：∇·(rⁿ r̂) = (n+2)rⁿ⁻¹，除非n=-2，此时是4πδ³(r)；对于n<-2，散度在原点无定义。]

(b) 求 rⁿ r̂ 的旋度。使用习题1.61b测试你的结论。[答案：∇×(rⁿ r̂) = 0]

问题1.64 如果你不相信∇²(1/r) = -4πδ³(r)（式1.102，简单起见设r=0），尝试用√(r²+ε²)替换r，并观察当ε→0时会发生什么。16具体地，令 D(r, ε) ≡ - (1/4π) ∇² (1/√(r²+ε²))。

16此问题由Frederick Strauch建议。

58 第1章 矢量分析证明当ε→0时，它趋于δ³(r)： (a) 证明D(r, ε) = (3ε²/4π)(r² + ε²)^{-5/2}。

(b) 检验当ε→0时，D(0, ε) → ∞。

(c) 检验当ε→0时，对于所有r ≠ 0，D(r, ε) → 0。

(d) 检验D(r, ε)在整个空间上的积分为1。

## 第 2 章

静电学

## 2.1 电场

2.1.1 引言电动力学希望解决的基本问题如下（图2.1）：我们有一些电荷q₁, q₂, q₃, ...（称为源电荷）；它们对另一个电荷Q（称为试探电荷）施加什么力？源电荷的位置是给定的（作为时间的函数）；要计算试探粒子的轨迹。通常，源电荷和试探电荷都在运动。

这个问题的求解得益于叠加原理，该原理指出任意两个电荷之间的相互作用完全不受其他电荷存在的影响。这意味着为了确定作用在Q上的力，我们可以首先计算仅由q₁产生的力F₁（忽略其他所有电荷）；然后计算仅由q₂产生的力F₂；以此类推。最后，我们取所有这些单个力的矢量和：F = F₁ + F₂ + F₃ + ...。因此，如果我们能找到单个源电荷q作用在Q上的力，那么从原则上讲，问题就解决了（剩下的只是重复相同的操作并将其全部相加）。1

嗯，乍一看这似乎很简单：为什么不直接写下q作用在Q上的力的公式就完事了呢？我可以这么做，而且在第10章我会这么做，但你现在看到它会感到震惊，因为不仅作用在Q上的力取决于电荷之间的分离距离（图2.2），它还取决于q和Q的速度以及q的加速度。此外，重要的不是q此时此刻的位置、速度和加速度：电磁“新闻”以光速传播，因此对Q来说，重要的是q在信息发出时的早期时刻的位置、速度和加速度。

因此，尽管基本问题（“q作用在Q上的力是什么？”）很容易陈述，但直接面对它并不划算；相反，我们将分阶段处理它。与此同时，我们发展的理论将允许解决那些不以这种简单格式呈现的更微妙的电磁问题。首先，我们将考虑静电学的特殊情况，其中所有源电荷都是静止的（尽管试探电荷可能在运动）。

2.1.2 库仑定律作用在一个静止的点电荷q在距离r处对试探电荷Q的力是什么？答案（基于实验）由库仑定律给出： F = (1/4πε₀) (qQ/r²) r̂。 (2.1)

常数ε₀被称为（荒谬地）真空介电常数。在SI单位制中，力的单位是牛顿（N），距离的单位是米（m），电荷的单位是库仑（C）， ε₀ = 8.85 × 10⁻¹² C²/(N·m²)。

换句话说，力与电荷的乘积成正比，与分离距离的平方成反比。始终如一（第1.1.4节），r是从r'（q的位置）到r（Q的位置）的分离矢量： r = r - r'； (2.2)

r是它的大小，r̂是它的方向。力沿着从q到Q的直线指向；如果q和Q符号相同，则是排斥力；如果符号相反，则是吸引力。

库仑定律和叠加原理构成了静电学的物理基础——剩下的部分，除了一些物质的特殊性质外，是对这些基本规则的数学阐述。

问题2.1 (a) 十二个相等的电荷q，位于正十二边形的顶点（例如，时钟的每个数字上）。中心处试探电荷Q所受的净力是多少？

(b) 假设其中一个12个q被移除（“6点钟”位置的那个）。Q所受的力是多少？仔细解释你的推理。

## 2.1 电场

(c) 现在有13个相等的电荷q，放置在正十三边形的顶点。中心处试探电荷Q所受的力是多少？

(d) 如果其中一个13个q被移除，Q所受的力是多少？解释你的推理。

2.1.3 电场如果我们有几个点电荷q₁, q₂, ..., qₙ，它们到Q的距离分别是r₁, r₂, ..., rₙ，那么作用在Q上的总力显然是 F = F₁ + F₂ + ... = (Q/(4πε₀)) (q₁r̂₁/r₁² + q₂r̂₂/r₂² + q₃r̂₃/r₃² + ...) = (Q/(4πε₀)) Σᵢ (qᵢr̂ᵢ/rᵢ²)， 或者 F = QE， (2.3)

其中 E(r) ≡ 1/(4πε₀) Σᵢ (qᵢ/rᵢ²) r̂ᵢ. (2.4)

E is called the electric field of the source charges. Notice that it is a function of position (r), because the separation vectors rᵢ depend on the location of the field point P (Fig. 2.3). But it makes no reference to the test charge Q. The electric field is a vector quantity that varies from point to point and is determined by the configuration of source charges; physically, E(r) is the force per unit charge that would be exerted on a test charge, if you were to place one at P.

What exactly is an electric field? I have deliberately begun with what you might call the “minimal” interpretation of E, as an intermediate step in the calculation of electric forces. But I encourage you to think of the field as a “real” physical entity, filling the space around electric charges. Maxwell himself came to believe that electric and magnetic fields are stresses and strains in an invisible primordial jellylike “ether.” Special relativity has forced us to abandon the notion of ether, and with it Maxwell’s mechanical interpretation of electromagnetic fields. (It is even possible, though cumbersome, to formulate classical electrodynamics as an “action-at-a-distance” theory, and dispense with the field concept altogether.) I can’t tell you, then, what a field is—only how to calculate it and what it can do for you once you’ve got it.

Example 2.1. Find the electric field a distance z above the midpoint between two equal charges (q), a distance d apart (Fig. 2.4a).

Solution Let E₁ be the field of the left charge alone, and E₂ that of the right charge alone (Fig. 2.4b). Adding them (vectorially), the horizontal components cancel and the vertical components conspire: E = 2 * (1/(4πε₀)) * (q/r²) * cosθ.

Here r = √[z² + (d/2)²] and cosθ = z/r, so E = (1/(4πε₀)) * (2qz / [z² + (d/2)²]^{3/2}) ẑ.

Check: When z >> d you’re so far away that it just looks like a single charge 2q, so the field should reduce to E = (1/(4πε₀)) * (2q/z²) ẑ. And it does (just set d → 0 in the formula).

Problem 2.2 Find the electric field (magnitude and direction) a distance z above the midpoint between equal and opposite charges (±q), a distance d apart (same as Example 2.1, except that the charge at x = +d/2 is −q).

2.1.4 Continuous Charge Distributions Our definition of the electric field (Eq. 2.4) assumes that the source of the field is a collection of discrete point charges q. If, instead, the charge is distributed continuously over some region, the sum becomes an integral (Fig. 2.5a): E(r) = 1/(4πε₀) ∫ (1/r²) r̂ dq. (2.5)

If the charge is spread out along a line (Fig. 2.5b), with charge-per-unit-length λ, then dq = λ dl' (where dl' is an element of length along the line); if the charge is smeared out over a surface (Fig. 2.5c), with charge-per-unit-area σ, then dq = σ da' (where da' is an element of area on the surface); and if the charge fills a volume (Fig. 2.5d), with charge-per-unit-volume ρ, then dq = ρ dτ' (where dτ' is an element of volume): dq → λ dl' ∼ σ da' ∼ ρ dτ'.

Thus the electric field of a line charge is E(r) = 1/(4πε₀) ∫ [λ(r - r') / |r - r'|³] dl'; (2.6)

for a surface charge, E(r) = 1/(4πε₀) ∫ [σ(r - r') / |r - r'|³] da'; (2.7)

and for a volume charge, E(r) = 1/(4πε₀) ∫ [ρ(r - r') / |r - r'|³] dτ'. (2.8)

Equation 2.8 itself is often referred to as “Coulomb’s law,” because it is such a short step from the original (2.1), and because a volume charge is in a sense the most general and realistic case. Please note carefully the meaning of (r - r') in these formulas. Originally, in Eq. 2.4, (rᵢ) stood for the vector from the source charge q to the field point r. Correspondingly, in Eqs. 2.5–2.8, (r - r') is the vector from dq (therefore from dl', da', or dτ') to the field point r.²

²Warning: The unit vector r̂ is not constant; its direction depends on the source point r', and hence it cannot be taken outside the integrals (Eqs. 2.5–2.8). In practice, you must work with Cartesian components (x̂, ŷ, ẑ are constant, and do come out), even if you use curvilinear coordinates to perform the integration.

Example 2.2. Find the electric field a distance z above the midpoint of a straight line segment of length 2L that carries a uniform line charge λ (Fig. 2.6).

Solution The simplest method is to chop the line into symmetrically placed pairs (at ±x), quote the result of Ex. 2.1 (with d/2 → x, q → λdx), and integrate (x : 0 → L). But here’s a more general approach:³ r = z ẑ, r' = x x̂, dl' = dx; r - r' = z ẑ - x x̂, r = √(z² + x²), r̂ = (z ẑ - x x̂)/√(z² + x²).

E = (1/(4πε₀)) ∫_{-L}^{L} [λ(z ẑ - x x̂)/ (z² + x²)^{3/2}] dx = (λ/(4πε₀)) [ ẑ ∫_{-L}^{L} z/(z² + x²)^{3/2} dx - x̂ ∫_{-L}^{L} x/(z² + x²)^{3/2} dx ]

= (λ/(4πε₀)) [ ẑ √(x/(z²√(z²+x²)))|_{-L}^{L} - x̂ (-1/√(z²+x²))|_{-L}^{L} ]

= (1/(4πε₀)) * (2λL / (z√(z²+L²))) ẑ.

³Ordinarily I’ll put a prime on the source coordinates, but where no confusion can arise I’ll remove the prime to simplify the notation.

For points far from the line (z >> L), E ≅ (1/(4πε₀)) * (2λL/z²).

This makes sense: From far away the line looks like a point charge q = 2λL. In the limit L → ∞, on the other hand, we obtain the field of an infinite straight wire: E = (1/(4πε₀)) * (2λ/z). (2.9)

Problem 2.3 Find the electric field a distance z above one end of a straight line segment of length L (Fig. 2.7) that carries a uniform line charge λ. Check that your formula is consistent with what you would expect for the case z >> L.

Problem 2.4 Find the electric field a distance z above the center of a square loop (side a) carrying uniform line charge λ (Fig. 2.8). [Hint: Use the result of Ex. 2.2.]

Problem 2.5 Find the electric field a distance z above the center of a circular loop of radius R (Fig. 2.9) that carries a uniform line charge λ.

Problem 2.6 Find the electric field a distance z above the center of a flat circular disk of radius R (Fig. 2.10) that carries a uniform surface charge σ. What does your formula give in the limit R → ∞? Also check the case z >> R.

Problem 2.7 Find the electric field a distance z from the center of a spherical surface of radius R (Fig. 2.11) that carries a uniform charge density σ. Treat the case z < R (inside) as well as z > R (outside). Express your answers in terms of the total charge q on the sphere. [Hint: Use the law of cosines to write r in terms of R and θ. Be sure to take the positive square root: √(R²+z²−2Rz) = (R−z) if R>z, but it’s (z−R) if R<z.]

Problem 2.8 Use your result in Prob. 2.7 to find the field inside and outside a solid sphere of radius R that carries a uniform volume charge density ρ. Express your answers in terms of the total charge of the sphere, q. Draw a graph of |E| as a function of the distance from the center.

## 2.2 DIVERGENCE AND CURL OF ELECTROSTATIC FIELDS

2.2.1 Field Lines, Flux, and Gauss’s Law In principle, we are done with the subject of electrostatics. Equation 2.8 tells us how to compute the field of a charge distribution, and Eq. 2.3 tells us what the force on a charge Q placed in this field will be. Unfortunately, as you may have discovered in working Prob. 2.7, the integrals involved in computing E can be formidable, even for reasonably simple charge distributions. Much of the rest of electrostatics is devoted to assembling a bag of tools and tricks for avoiding these integrals. It all begins with the divergence and curl of E. I shall calculate the divergence of E directly from Eq. 2.8, in Sect. 2.2.2, but first I want to show you a more qualitative, and perhaps more illuminating, intuitive approach.

Let’s begin with the simplest possible case: a single point charge q, situated at the origin: E(r) = (1/(4πε₀)) * (q/r²) r̂. (2.10)

To get a “feel” for this field, I might sketch a few representative vectors, as in Fig. 2.12a. Because the field falls off like 1/r², the vectors get shorter as you go farther away from the origin; they always point radially outward. But there is a nicer way to represent this field, and that’s to connect up the arrows, to form field lines (Fig. 2.12b). You might think that I have thereby thrown away information about the strength of the field, which was contained in the length of the arrows. But actually I have not. The magnitude of the field is indicated by the density of the field lines: it’s strong near the center where the field lines are close together, and weak farther out, where they are relatively far apart.

In truth, the field-line diagram is deceptive, when I draw it on a two-dimensional surface, for the density of lines passing through a circle of radius r is the total number divided by the circumference (n/2πr), which goes like (1/r), not (1/r²). But if you imagine the model in three dimensions (a pincushion with needles sticking out in all directions), then the density of lines is the total number divided by the area of the sphere (n/4πr²), which does go like (1/r²).

Such diagrams are also convenient for representing more complicated fields. Of course, the number of lines you draw depends on how lazy you are (and how sharp your pencil is), though you ought to include enough to get an accurate sense of the field, and you must be consistent: If q gets 8 lines, then 2q deserves 16. And you must space them fairly—they emanate from a point charge symmetrically in all directions. Field lines begin on positive charges and end on negative ones; they cannot simply terminate in midair,⁴ though they may extend out to infinity. Moreover, field lines can never cross—at the intersection, the field would have two different directions at once! With all this in mind, it is easy to sketch the field of any simple configuration of point charges: Begin by drawing the lines in the neighborhood of each charge, and then connect them up or extend them to infinity (Figs. 2.13 and 2.14).

⁴If they did, the divergence of E would not be zero, and (as we shall soon see) that cannot happen in empty space.

In this model, the flux of E through a surface S, Φ_E ≡ ∫_S E · da, (2.11)

is a measure of the “number of field lines” passing through S. I put this in quotes because of course we can only draw a representative sample of the field lines—the total number would be infinite. But for a given sampling rate the flux is proportional to the number of lines drawn.

because the field strength, remember, is proportional to the density of field lines (the number per unit area), and hence $\mathbf{E} \cdot d \mathbf{a}$ is proportional to the number of lines passing through the infinitesimal area $d a$. (The dot product picks out the component of $d a$ along the direction of $\mathbf{E}$, as indicated in Fig. 2.15. It is the area in the plane perpendicular to $\mathbf{E}$ that we have in mind when we say that the density of field lines is the number per unit area.) This suggests that the flux through any closed surface is a measure of the total charge inside. For the field lines that originate on a positive charge must either pass out through the surface or else terminate on a negative charge inside (Fig. 2.16a). On the other hand, a charge outside the surface will contribute nothing to the total flux, since its field lines pass in one side and out the other (Fig. 2.16b). This is the essence of Gauss's law. Now let's make it quantitative.

In the case of a point charge $q$ at the origin, the flux of $\mathbf{E}$ through a spherical surface of radius $r$ is $$ \int_{S} \mathbf{E} \cdot d \mathbf{a}=\int_{0}^{\pi} \int_{0}^{2 \pi} \frac{1}{4 \pi \epsilon_{0}} \frac{q}{r^{2}} \hat{\mathbf{r}} \cdot\left(r^{2} \sin \theta d \theta d \phi \hat{\mathbf{r}}\right)=\frac{q}{\epsilon_{0}} . \tag{2.12} $$ Notice that the radius of the sphere cancels out, for while the surface area goes up as $r^{2}$, the field goes down as $1 / r^{2}$, so the product is constant. In terms of the field-line picture, this makes good sense, since the same number of field lines pass through any sphere centered at the origin, regardless of its size. In fact, it didn't have to be a sphere—any closed surface, whatever its shape, would be pierced by the same number of field lines. Evidently the flux through any surface enclosing the charge is $q / \epsilon_{0}$.

Now suppose that instead of a single charge at the origin, we have a bunch of charges scattered about. According to the principle of superposition, the total field is the (vector) sum of all the individual fields: $$ \mathbf{E}=\sum_{i=1}^{n} \mathbf{E}_{i} .

$$ The flux through a surface that encloses them all is $$ \int_{S} \mathbf{E} \cdot d \mathbf{a}=\sum_{i=1}^{n}\left(\int_{S} \mathbf{E}_{i} \cdot d \mathbf{a}\right)=\frac{1}{\epsilon_{0}} \sum_{i=1}^{n} q_{i} .

$$ For any closed surface, then, $$ \int_{S} \mathbf{E} \cdot d \mathbf{a}=\frac{Q_{\text {enc }}}{\epsilon_{0}}, \tag{2.13} $$ where $Q_{\text {enc }}$ is the total charge enclosed within the surface. This is the quantitative statement of Gauss's law. Although it contains no information that was not already present in Coulomb's law plus the principle of superposition, it is of almost magical power, as you will see in Sect. 2.2.3. Notice that it all hinges on the $1 / r^{2}$ character of Coulomb's law; without that the crucial cancellation of the $r$ 's in Eq. 2.12 would not take place, and the total flux of $\mathbf{E}$ would depend on the surface chosen, not merely on the total charge enclosed. Other $1 / r^{2}$ forces (I am thinking particularly of Newton's law of universal gravitation) will obey "Gauss's laws" of their own, and the applications we develop here carry over directly.

As it stands, Gauss's law is an integral equation, but we can easily turn it into a differential one, by applying the divergence theorem: $$ \int_{S} \mathbf{E} \cdot d \mathbf{a}=\int_{V}(\nabla \cdot \mathbf{E}) d \tau .

$$ Rewriting $Q_{\text {enc }}$ in terms of the charge density $\rho$, we have $$ Q_{\text {enc }}=\int_{V} \rho d \tau .

$$ So Gauss's law becomes $$ \int_{V}(\nabla \cdot \mathbf{E}) d \tau=\frac{1}{\epsilon_{0}} \int_{V} \rho d \tau .

$$ And since this holds for any volume, the integrands must be equal: $$ \nabla \cdot \mathbf{E}=\frac{\rho}{\epsilon_{0}} . \tag{2.14} $$ Equation 2.14 carries the same message as Eq. 2.13; it is Gauss's law in differential form. The differential version is tidier, but the integral form has the advantage in that it accommodates point, line, and surface charges more naturally.

Problem 2.9 Suppose the electric field in some region is found to be $\mathbf{E}=k r^{3} \hat{\mathbf{r}}$, in spherical coordinates ($k$ is some constant).

(a) Find the charge density $\rho$.

(b) Find the total charge contained in a sphere of radius $R$, centered at the origin. (Do it two different ways.)

Problem 2.10 A charge $q$ sits at the back corner of a cube, as shown in Fig. 2.17. What is the flux of $\mathbf{E}$ through the shaded side?

### 2.2.2 The Divergence of $\mathbf{E}$

Let's go back, now, and calculate the divergence of $\mathbf{E}$ directly from Eq. 2.8: $$ \mathbf{E}(\mathbf{r})=\frac{1}{4 \pi \epsilon_{0}} \int \frac{\hat{\mathbf{r}}}{r^{2}} \rho\left(\mathbf{r}^{\prime}\right) d \tau^{\prime} . \tag{2.15} $$ (Originally the integration was over the volume occupied by the charge, but I may as well extend it to all space, since $\rho=0$ in the exterior region anyway.) Noting that the $\mathbf{r}$-dependence is contained in $\mathbf{r}=\mathbf{r}-\mathbf{r}^{\prime}$, we have $$ \nabla \cdot \mathbf{E}=\frac{1}{4 \pi \epsilon_{0}} \int \nabla \cdot\left(\frac{\hat{\mathbf{r}}}{r^{2}}\right) \rho\left(\mathbf{r}^{\prime}\right) d \tau^{\prime} .

$$ This is precisely the divergence we calculated in Eq. 1.100: $$ \nabla \cdot\left(\frac{\hat{\mathbf{r}}}{r^{2}}\right)=4 \pi \delta^{3}(\mathbf{r}) .

$$ Thus $$ \nabla \cdot \mathbf{E}=\frac{1}{4 \pi \epsilon_{0}} \int 4 \pi \delta^{3}\left(\mathbf{r}-\mathbf{r}^{\prime}\right) \rho\left(\mathbf{r}^{\prime}\right) d \tau^{\prime}=\frac{1}{\epsilon_{0}} \rho(\mathbf{r}), \tag{2.16} $$ which is Gauss's law in differential form (Eq. 2.14). To recover the integral form (Eq. 2.13), we run the previous argument in reverse—integrate over a volume and apply the divergence theorem: $$ \int_{V} \nabla \cdot \mathbf{E} d \tau=\int_{S} \mathbf{E} \cdot d \mathbf{a}=\frac{1}{\epsilon_{0}} \int_{V} \rho d \tau=\frac{Q_{\text {enc }}}{\epsilon_{0}} .

$$

### 2.2.3 Applications of Gauss's Law

I must interrupt the theoretical development at this point to show you the extraordinary power of Gauss's law, in integral form. When symmetry permits, it affords by far the quickest and easiest way of computing electric fields. I'll illustrate the method with a series of examples.

Example 2.3. Find the field outside a uniformly charged solid sphere of radius $R$ and total charge $q$.

Solution Imagine a spherical surface at radius $r>R$ (Fig. 2.18); this is called a Gaussian surface in the trade. Gauss's law says that $$ \int \mathbf{E} \cdot d \mathbf{a}=\frac{Q_{\text {enc }}}{\epsilon_{0}}, $$ and in this case $Q_{\text {enc }}=q$. At first glance this doesn't seem to get us very far, because the quantity we want $(\mathbf{E})$ is buried inside the surface integral. Luckily, symmetry allows us to extract $\mathbf{E}$ from under the integral sign: $\mathbf{E}$ certainly points radially outward,${ }^{5}$ as does $d \mathbf{a}$, so we can drop the dot product, $$ \int \mathbf{E} \cdot d \mathbf{a}=\int |\mathbf{E}| d a, $$ and the magnitude of $\mathbf{E}$ is constant over the Gaussian surface, so it comes outside the integral: $$ \int |\mathbf{E}| d a=|\mathbf{E}| \int d a=|\mathbf{E}| 4 \pi r^{2} .

$$ Thus $$ |\mathbf{E}| 4 \pi r^{2}=\frac{q}{\epsilon_{0}}, $$ or $$ \mathbf{E}=\frac{1}{4 \pi \epsilon_{0}} \frac{q}{r^{2}} \hat{\mathbf{r}} .

$$ Notice a remarkable feature of this result: The field outside the sphere is exactly the same as it would have been if all the charge had been concentrated at the center.

Gauss's law is always true, but it is not always useful. If $\rho$ had not been uniform (or, at any rate, not spherically symmetrical), or if I had chosen some other shape for my Gaussian surface, it would still have been true that the flux of $\mathbf{E}$ is $q / \epsilon_{0}$, but $\mathbf{E}$ would not have pointed in the same direction as $d \mathbf{a}$, and its magnitude would not have been constant over the surface, and without that I cannot get $|\mathbf{E}|$ outside of the integral. Symmetry is crucial to this application of Gauss's law. As far as I know, there are only three kinds of symmetry that work:

## 1. Spherical symmetry. Make your Gaussian surface a concentric sphere

2. Cylindrical symmetry. Make your Gaussian surface a coaxial cylinder (Fig. 2.19).

3. Plane symmetry. Use a Gaussian "pillbox" that straddles the surface (Fig. 2.20).

Although (2) and (3) technically require infinitely long cylinders, and planes extending to infinity, we shall often use them to get approximate answers for "long" cylinders or "large" planes, at points far from the edges.

Example 2.4. A long cylinder (Fig. 2.21) carries a charge density that is proportional to the distance from the axis: $\rho=k s$, for some constant $k$. Find the electric field inside this cylinder.

Solution Draw a Gaussian cylinder of length $l$ and radius $s$. For this surface, Gauss's law states: $$ \int \mathbf{E} \cdot d \mathbf{a}=\frac{Q_{\text {enc }}}{\epsilon_{0}} .

$$ The enclosed charge is $$ Q_{\text {enc }}=\int \rho d \tau=\int\left(k s^{\prime}\right)\left(s^{\prime} d s^{\prime} d \phi d z\right)=2 \pi k l \int_{0}^{s} s^{\prime 2} d s^{\prime}=\frac{2 \pi k l s^{3}}{3} .

$$ Now, symmetry dictates that $\mathbf{E}$ must point radially outward, so for the curved portion of the Gaussian cylinder we have: $$ \int \mathbf{E} \cdot d \mathbf{a}=\int |\mathbf{E}| d a=|\mathbf{E}| \int d a=|\mathbf{E}| 2 \pi s l, $$ while the two ends contribute nothing (here $\mathbf{E}$ is perpendicular to $d \mathbf{a}$). Thus, $$ |\mathbf{E}| 2 \pi s l=\frac{1}{\epsilon_{0}} \frac{2 \pi k l s^{3}}{3}, $$ or, finally, $$ \mathbf{E}=\frac{k s^{2}}{3 \epsilon_{0}} \hat{\mathbf{s}} .

$$

Example 2.5. An infinite plane carries a uniform surface charge $\sigma$. Find its electric field.

Solution Draw a "Gaussian pillbox," extending equal distances above and below the plane (Fig. 2.22). Apply Gauss's law to this surface: $$ \int \mathbf{E} \cdot d \mathbf{a}=\frac{Q_{\text {enc }}}{\epsilon_{0}} .

$$ In this case, $Q_{\text {enc }}=\sigma A$, where $A$ is the area of the lid of the pillbox. By symmetry, $\mathbf{E}$ points away from the plane (upward for points above, downward for points below). So the top and bottom surfaces yield $$ \int \mathbf{E} \cdot d \mathbf{a}=2 A|\mathbf{E}|, $$ whereas the sides contribute nothing. Thus $$ 2 A|\mathbf{E}|=\frac{\sigma A}{\epsilon_{0}}, $$ or $$ \mathbf{E}=\frac{\sigma}{2 \epsilon_{0}} \hat{\mathbf{n}}, \tag{2.17} $$ where $\hat{\mathbf{n}}$ is a unit vector pointing away from the surface. In Prob. 2.6, you obtained this same result by a much more laborious method.

It seems surprising, at first, that the field of an infinite plane is independent of how far away you are. What about the $1 / r^{2}$ in Coulomb's law? The point is that as you move farther and farther away from the plane, more and more charge comes into your "field of view" (a cone shape extending out from your eye), and this compensates for the diminishing influence of any particular piece. The electric field of a sphere falls off like $1 / r^{2}$; the electric field of an infinite line falls off like $1 / r$; and the electric field of an infinite plane does not fall off at all (you cannot escape from an infinite plane).

Although the direct use of Gauss's law to compute electric fields is limited to cases of spherical, cylindrical, and planar symmetry, we can put together combinations of objects possessing such symmetry, even though the arrangement as a whole is not symmetrical. For example, invoking the principle of superposition, we could find the field in the vicinity of two uniformly charged parallel cylinders, or a sphere near an infinite charged plane.

Example 2.6. Two infinite parallel planes carry equal but opposite uniform charge densities $\pm \sigma$ (Fig. 2.23). Find the field in each of the three regions: (i) to the left of both, (ii) between them, (iii) to the right of both.

Solution The left plate produces a field $(1 / 2 \epsilon_{0}) \sigma$, which points away from 它（图2.24）—— 向左在区域（i），向右在区域（ii）和（iii）。右侧的极板带负电，产生一个大小为(1/2)ε₀σ的电场，方向指向它——即在区域（i）和（ii）中向右，在区域（iii）中向左。这两个电场在区域（i）和（iii）中相互抵消；在区域（ii）中相互叠加。结论：极板间的电场为σ/ε₀，方向向右；其他地方的电场为零。

## E E E

+ + + (i) (ii) (iii)

## E E E

− − − (i) (ii) (iii)

+σ −σ +σ −σ FIGURE 2.23 FIGURE 2.24

问题2.11 使用高斯定律，求半径为R、带有均匀面电荷密度σ的球壳内部和外部的电场。将你的答案与问题2.7进行比较。

问题2.12 使用高斯定律，求均匀带电固体球（电荷密度ρ）内部的电场。将你的答案与问题2.8进行比较。

问题2.13 求距离一条无限长、带有均匀线电荷λ的直导线s处的电场。与公式2.9进行比较。

问题2.14 求一个球体内部的电场，其电荷密度与到原点的距离成正比，即ρ = kr，其中k为常数。[提示：此电荷密度不均匀，你必须通过积分求出所包围的电荷。]

问题2.15 一个厚球壳的电荷密度为 ρ = (a ≤ r ≤ b)

r² （图2.25）。求三个区域中的电场：(i) r < a，(ii) a < r < b，(iii) r > b。对于b=2a的情况，画出|E|随r变化的图像。

问题2.16 一根长同轴电缆（图2.26）的内圆柱（半径a）带有均匀体电荷密度ρ，外圆柱壳（半径b）带有均匀面电荷密度。此面电荷为负，其大小恰好使电缆整体呈电中性。求三个区域中的电场：(i) 在内圆柱内部（s < a），(ii) 在圆柱之间（a < s < b），(iii) 在电缆外部（s > b）。画出|E|随s变化的图像。

a − b b + FIGURE 2.25 FIGURE 2.26

问题2.17 一个无限大平板，厚度为2d，带有均匀体电荷密度ρ（图2.27）。求电场，它是y的函数，其中y=0位于中心。画出E随y变化的图像，规定当E指向+y方向时为正，指向-y方向时为负。

问题2.18 两个半径均为R、分别带有均匀体电荷密度+ρ和−ρ的球体，放置成部分重叠（图2.28）。设从正电中心指向负电中心的矢量为d。证明重叠区域中的电场是恒定的，并求出其值。[提示：使用问题2.12的答案。]

2.2.4 E的旋度我将计算E的旋度，正如我在2.2.1节中计算散度那样，首先研究最简单的可能构型：位于原点的点电荷。在这种情况下， E = (1 / 4πε₀) * (q / r²) * r̂。

现在，看一下图2.12应该让你相信这个场的旋度必须为零，但我想我们应该给出比这更严格一些的推导。如果我们计算这个场从某点a到另一点b（图2.29）的线积分呢？

∫ E·dl 在球坐标系中，dl = dr r̂ + r dθ θ̂ + r sinθ dφ φ̂，所以 E·dl = (1 / 4πε₀) * (q / r²) dr。

因此， ∫_a^b E·dl = (1 / 4πε₀) ∫_{r_a}^{r_b} (q / r²) dr = - (1 / 4πε₀) q (1/r)|_{r_a}^{r_b} = (1 / 4πε₀) * (q / r_a - q / r_b)。(2.18)

其中r_a是原点到点a的距离，r_b是到b的距离。

绕闭合路径的积分显然为零（因为此时r_a = r_b）： ∮ E·dl = 0。(2.19)

因此，应用斯托克斯定理， ∇ × E = 0。(2.20)

现在，我只对位于原点的单个点电荷的场证明了式2.19和2.20，但这些结果并不涉及一个完全任意的坐标选择；无论电荷位于何处，它们都成立。此外，如果我们有许多电荷，叠加原理表明总场是它们各自场的矢量和： E = E₁ + E₂ + ...， 所以 ∇ × E = ∇ × (E₁ + E₂ + ...) = (∇ × E₁) + (∇ × E₂) + ... = 0。

因此，式2.19和2.20对于任何静态电荷分布都成立。

问题2.19 直接从式2.8计算∇ × E，使用2.2.2节的方法。如果你卡住了，可以参考问题1.63。

## 2.3 电势

2.3.1 电势简介电场E不是任意的矢量函数。它是一种非常特殊的矢量函数：旋度为零的函数。例如，E = y x̂ 就不可能是静电场；无论大小和位置如何，任何电荷集合都不可能产生这样的场。我们将利用电场的这一特殊性质，将一个矢量问题（求E）简化为一个简单得多的标量问题。1.6.2节的第一个定理断言，任何旋度为零的矢量都等于某个标量的梯度。我现在要做的就是在静电学的背景下证明那个论断。

因为∇ × E = 0，所以E绕任何闭合回路的线积分为零（这由斯托克斯定理得出）。因为∮ E·dl = 0，所以E从点a到点b的线积分对于所有路径都是相同的（否则你可以沿着路径(i)出去，沿着路径(ii)返回——图2.30——得到∮ E·dl ≠ 0）。因为线积分与路径无关，我们可以定义一个函数： V(r) ≡ - ∫_{O}^{r} E·dl。(2.21)

这里O是我们事先约定好的某个标准参考点；V因此仅依赖于点r。它被称为电势。

两点a和b之间的电势差为： V(b) - V(a) = - ∫_{O}^{b} E·dl + ∫_{O}^{a} E·dl = - ∫_{O}^{b} E·dl - ∫_{a}^{O} E·dl = - ∫_{a}^{b} E·dl。(2.22)

现在，梯度的基本定理指出： V(b) - V(a) = ∫_{a}^{b} (∇V)·dl， 所以 ∫_{a}^{b} (∇V)·dl = - ∫_{a}^{b} E·dl。

最后，由于这对任何点a和b都成立，被积函数必须相等： E = -∇V。(2.23)

方程2.23是方程2.21的微分形式；它表示电场是一个标量势的梯度，这正是我们想要证明的。

注意路径无关性（或者等价地，∇ × E = 0）在这个论证中所扮演的微妙但关键的角色。如果E的线积分取决于所走的路径，那么V的“定义”（方程2.21）将是无意义的。它根本不能定义一个函数，因为改变路径会改变V(r)的值。顺便说一句，不要让方程2.23中的负号分散你的注意力；它继承自方程2.21，在很大程度上只是一个惯例。

问题2.20 以下哪一个是不可能的静电场？(a) E = k[xy x̂ + 2yz ŷ + 3xz ẑ]；(b) E = k[y² x̂ + (2xy + z²) ŷ + 2yz ẑ]。这里k是具有适当单位的常数。对于可能的那个，求电势，以原点为参考点。通过计算∇V来检查你的答案。[提示：你必须选择一条特定的路径进行积分。选什么路径并不重要，因为答案与路径无关，但你根本无法积分，除非你心中有一个确定的路径。]

2.3.2 关于电势的评论 (i) 名称。“电势”这个名称是一个糟糕的误称，因为它不可避免地让你联想到电势能。这特别有误导性，因为“电势”和“电势能”之间确实存在联系，正如你将在2.4节中看到的。我很抱歉无法避开这个词。我最多能做的就是坚持一个一劳永逸的观点：“电势”和“电势能”是完全不同的术语，按理说应该有不同的名称。顺便说一句，电势为常数的曲面被称为等势面。

(ii) 电势表述的优点。如果你知道V，你可以很容易地得到E——只需取梯度：E = -∇V。当你停下来思考时，这相当非凡，因为E是一个矢量量（三个分量），而V是一个标量（一个分量）。一个函数怎么可能包含三个独立函数所能携带的所有信息？答案是E的三个分量看起来并非那么独立；事实上，它们通过我们一开始的条件∇ × E = 0被明确地相互关联。用分量表示， ∂Eₓ/∂y = ∂E_y/∂x, ∂E_y/∂z = ∂E_z/∂y, ∂E_z/∂x = ∂Eₓ/∂z。

这让我们回到我在2.3.1节开头的观察：E是一种非常特殊的矢量。电势表述所做的就是最大限度地利用这一特性，将一个矢量问题简化为一个标量问题，其中不需要为分量费神。

(iii) 参考点O。电势的定义存在一个本质的模糊性，因为参考点O的选择是任意的。更换参考点相当于给电势加上一个常数K： V'(r) = - ∫_{O'}^{r} E·dl = - ∫_{O'}^{O} E·dl - ∫_{O}^{r} E·dl = K + V(r)， 其中K是E从旧参考点O到新参考点O'的线积分。当然，给V加上一个常数不会影响两点之间的电势差： V'(b) - V'(a) = V(b) - V(a)， 因为K会相互抵消。（实际上，从方程2.22已经清楚，电势差与O无关，因为它可以写成E从a到b的线积分，不涉及O。）这种模糊性也不影响V的梯度： ∇V' = ∇V， 因为常数的导数为零。这就是为什么所有仅参考点选择不同的V都对应同一个场E。

电势本身并没有真正的物理意义，因为在任意给定点，我们可以通过重新安置O来随意调整它的值。在这个意义上，它类似于高度：如果我问你丹佛有多高，你可能会告诉我它海拔多高，因为那是一个方便且传统的参考点。但我们也可以约定以华盛顿特区、格林尼治或任何地方作为海拔的起点。那将从所有海平面读数中加上（或者说减去）一个固定的量，但它不会改变任何关于真实世界的事情。唯一具有内在意义的量是两点之间的高度差，无论你的参考面是什么，它都是相同的。

话虽如此，在静电学中确实有一个“自然”的点可以用作O——类似于海拔的海平面——那就是距离电荷无限远的点。因此，通常我们“将电势的零点设在无穷远”。（由于V(O)=0，选择一个参考点等价于选择一个使无穷远处电势为零的O。）

ting a place where V is to be zero.) But I must warn you that there is one special circumstance in which this convention fails: when the charge distribution itself extends to infinity. The symptom of trouble, in such cases, is that the potential blows up. For instance, the field of a uniformly charged plane is (σ/2ε₀) n̂, as we found in Ex. 2.5; if we naïvely put O = ∞, then the potential at height z above the plane becomes

V(z) = -∫_∞^z (σ/2ε₀) dz = - (σ/2ε₀) (z - ∞).

The remedy is simply to choose some other reference point (in this example you might use a point on the plane). Notice that the difficulty occurs only in textbook problems; in "real life" there is no such thing as a charge distribution that goes on forever, and we can always use infinity as our reference point.

(iv) Potential obeys the superposition principle. The original superposition principle pertains to the force on a test charge Q. It says that the total force on Q is the vector sum of the forces attributable to the source charges individually:

F = F₁ + F₂ + ...

Dividing through by Q, we see that the electric field, too, obeys the superposition principle:

E = E₁ + E₂ + ...

Integrating from the common reference point to r, it follows that the potential also satisfies such a principle:

V = V₁ + V₂ + ...

That is, the potential at any given point is the sum of the potentials due to all the source charges separately. Only this time it is an ordinary sum, not a vector sum, which makes it a lot easier to work with.

(v) Units of Potential. In our units, force is measured in newtons and charge in coulombs, so electric fields are in newtons per coulomb. Accordingly, potential is newton-meters per coulomb, or joules per coulomb. A joule per coulomb is a volt.

Example 2.7. Find the potential inside and outside a spherical shell of radius R (Fig. 2.31) that carries a uniform surface charge. Set the reference point at infinity.

Solution From Gauss’s law, the field outside is

E = (1/4πε₀) (q/r²) r̂,

where q is the total charge on the sphere. The field inside is zero. For points outside the sphere (r > R),

V(r) = -∫_∞^r E·dl = -∫_∞^r (1/4πε₀) (q/r'²) dr' = (1/4πε₀) (q/r')|_∞^r = (1/4πε₀) (q/r).

To find the potential inside the sphere (r < R), we must break the integral into two pieces, using in each region the field that prevails there:

V(r) = -∫_∞^R (1/4πε₀) (q/r'²) dr' - ∫_R^r (0) dr' = (1/4πε₀) (q/r')|_∞^R + 0 = (1/4πε₀) (q/R).

Notice that the potential is not zero inside the shell, even though the field is. V is a constant in this region, to be sure, so that ∇V = 0—that’s what matters. In problems of this type, you must always work your way in from the reference point; that’s where the potential is "nailed down." It is tempting to suppose that you could figure out the potential inside the sphere on the basis of the field there alone, but this is false: The potential inside the sphere is sensitive to what’s going on outside the sphere as well. If I placed a second uniformly charged shell out at radius R' > R, the potential inside R would change, even though the field would still be zero. Gauss’s law guarantees that charge exterior to a given point (that is, at larger r) produces no net field at that point, provided it is spherically or cylindrically symmetric, but there is no such rule for potential, when infinity is used as the reference point.

Problem 2.21 Find the potential inside and outside a uniformly charged solid sphere whose radius is R and whose total charge is q. Use infinity as your reference point. Compute the gradient of V in each region, and check that it yields the correct field. Sketch V(r).

Problem 2.22 Find the potential at a distance s from an infinitely long straight wire that carries a uniform line charge λ. Compute the gradient of your potential, and check that it yields the correct field.

Problem 2.23 For the charge configuration of Prob. 2.15, find the potential at the center, using infinity as your reference point.

Problem 2.24 For the configuration of Prob. 2.16, find the potential difference between a point on the axis and a point on the outer cylinder. Note that it is not necessary to commit yourself to a particular reference point, if you use Eq. 2.22.

2.3.3 Poisson’s Equation and Laplace’s Equation We found in Sect. 2.3.1 that the electric field can be written as the gradient of a scalar potential.

E = -∇V.

The question arises: What do the divergence and curl of E,

∇·E = ρ/ε₀ and ∇×E = 0,

look like, in terms of V? Well, ∇·E = ∇·(-∇V) = -∇²V, so, apart from that persistent minus sign, the divergence of E is the Laplacian of V. Gauss’s law, then, says

∇²V = -ρ/ε₀. (2.24)

This is known as Poisson’s equation. In regions where there is no charge, so ρ = 0, Poisson’s equation reduces to Laplace’s equation,

∇²V = 0. (2.25)

We’ll explore this equation more fully in Chapter 3.

So much for Gauss’s law. What about the curl law? This says that

∇×E = ∇×(-∇V) = 0.

But that’s no condition on V—curl of gradient is always zero. Of course, we used the curl law to show that E could be expressed as the gradient of a scalar, so it’s not really surprising that this works out: ∇×E = 0 permits E = -∇V; in return, E = -∇V guarantees ∇×E = 0. It takes only one differential equation (Poisson’s) to determine V, because V is a scalar; for E we needed two, the divergence and the curl.

2.3.4 The Potential of a Localized Charge Distribution I defined V in terms of E (Eq. 2.21). Ordinarily, though, it’s E that we’re looking for (if we already knew E, there wouldn’t be much point in calculating V). The idea is that it might be easier to get V first, and then calculate E by taking the gradient. Typically, then, we know where the charge is (that is, we know ρ), and we want to find V. Now, Poisson’s equation relates V and ρ, but unfortunately it’s "the wrong way around": it would give us ρ, if we knew V, whereas we want V, knowing ρ. What we must do, then, is "invert" Poisson’s equation. That’s the program for this section, although I shall do it by roundabout means, beginning, as always, with a point charge at the origin.

The electric field is E = (1/4πε₀) (1/r²) r̂, and dl = dr r̂ + r dθ θ̂ + r sinθ dφ φ̂ (Eq. 1.68), so

E·dl = (1/4πε₀) (1/r²) dr.

Setting the reference point at infinity, the potential of a point charge q at the origin is

V(r) = -∫_∞^r E·dl = -∫_∞^r (1/4πε₀) (1/r'²) dr' = (1/4πε₀) (1/r')|_∞^r = (1/4πε₀) (1/r).

(You see here the advantage of using infinity for the reference point: it kills the lower limit on the integral.) Notice the sign of V; presumably the conventional minus sign in the definition (Eq. 2.21) was chosen in order to make the potential of a positive charge come out positive. It is useful to remember that regions of positive charge are potential "hills," regions of negative charge are potential "valleys," and the electric field points "downhill," from plus toward minus.

In general, the potential of a point charge q is

V(r) = (1/4πε₀) (q/r), (2.26)

where r, as always, is the distance from q to r (Fig. 2.32). Invoking the superposition principle, then, the potential of a collection of charges is

V(r) = (1/4πε₀) Σᵢ (qᵢ/rᵢ), (2.27)

or, for a continuous distribution,

V(r) = (1/4πε₀) ∫ (1/r) dq.

In particular, for a volume charge, it’s

V(r) = (1/4πε₀) ∫ (ρ(r')/r) dτ'.

This is the equation we were looking for, telling us how to compute V when we know ρ; it is, if you like, the "solution" to Poisson’s equation, for a localized charge distribution.⁷ Compare Eq. 2.29 with the corresponding formula for the electric field in terms of ρ (Eq. 2.8):

E(r) = (1/4πε₀) ∫ (ρ(r')/r²) r̂ dτ'.

The main point to notice is that the pesky unit vector r̂ is gone, so there is no need to fuss with components. The potentials of line and surface charges are

V = (1/4πε₀) ∫ (λ(r')/r) dl' and V = (1/4πε₀) ∫ (σ(r')/r) da'. (2.30)

I should warn you that everything in this section is predicated on the assumption that the reference point is at infinity. This is hardly apparent in Eq. 2.29, but remember that we got that equation from the potential of a point charge at the origin, (1/4πε₀)(q/r), which is valid only when O = ∞. If you try to apply these formulas to one of those artificial problems in which the charge itself extends to infinity, the integral will diverge.

Example 2.8. Find the potential of a uniformly charged spherical shell of radius R (Fig. 2.33).

Solution This is the same problem we solved in Ex. 2.7, but this time let’s do it using Eq. 2.30:

V(r) = (1/4πε₀) ∫ (σ/r) da'.

We might as well set the point P on the z axis and use the law of cosines to express r:

r² = R² + z² - 2Rz cosθ'.

A differential element of surface area on the sphere is R² sinθ' dθ' dφ', so

4πε₀ V(z) = σ ∫ (R² sinθ' dθ' dφ') / √(R² + z² - 2Rz cosθ')

= 2πR²σ ∫ (π sinθ' dθ') / √(R² + z² - 2Rz cosθ')

= (2πR²σ / Rz) [√(R² + z² - 2Rz cosθ')] from 0 to π

= (2πRσ / z) [√((R+z)²) - √((R-z)²)]

= (2πRσ / z) [(R+z) - |R-z|].

At this stage, we must be very careful to take the positive root. For points outside the sphere, z is greater than R, and hence √((R-z)²) = z - R; for points inside the sphere, √((R-z)²) = R - z. Thus,

V(z) = (Rσ / 2ε₀z) [(R+z) - (z - R)] = (R²σ / ε₀ z), outside; V(z) = (Rσ / 2ε₀z) [(R+z) - (R - z)] = (Rσ / ε₀), inside.

In terms of r and the total charge on the shell, q = 4πR²σ,

V(r) = (1/4πε₀) (q/r), for r ≥ R, V(r) = (1/4πε₀) (q/R), for r ≤ R.

Of course, in this particular case, it was easier to get V by using Eq. 2.21 than Eq. 2.30, because Gauss’s law gave us E with so little effort. But if you compare Ex. 2.8 with Prob. 2.7, you will appreciate the power of the potential formulation.

Problem 2.25 Using Eqs. 2.27 and 2.30, find the potential at a distance z above the center of the charge distributions in Fig. 2.34. In each case, compute E = -∇V, and compare your answers with Ex. 2.1, Ex. 2.2, and Prob. 2.6, respectively. Suppose that we changed the right-hand charge in Fig. 2.34a to -q; what then is the potential at P? What field does that suggest? Compare your answer to Prob. 2.2, and explain carefully any discrepancy.

Problem 2.26 A conical...

The surface of an empty ice-cream cone carries a uniform surface charge σ. The height of the cone is h, as is the radius of the top. Find the potential difference between points a (the vertex) and b (the center of the top).

Problem 2.27 Find the potential on the axis of a uniformly charged solid cylinder, a distance z from the center. The length of the cylinder is L, its radius is R, and the charge density is ρ. Use your result to calculate the electric field at this point. (Assume that z > L/2.)

Problem 2.28 Use Eq. 2.29 to calculate the potential inside a uniformly charged solid sphere of radius R and total charge q. Compare your answer to Prob. 2.21.

Problem 2.29 Check that Eq. 2.29 satisfies Poisson’s equation, by applying the Laplacian and using Eq. 1.102.

2.3.5 Boundary Conditions

In the typical electrostatic problem you are given a source charge distribution ρ, and you want to find the electric field E it produces. Unless the symmetry of the problem allows a solution by Gauss’s law, it is generally to your advantage to calculate the potential first, as an intermediate step. These are the three fundamental quantities of electrostatics: ρ, E, and V. We have, in the course of our discussion, derived all six formulas interrelating them. These equations are neatly summarized in Fig. 2.35. We began with just two experimental observations: (1) the principle of superposition—a broad general rule applying to all electromagnetic forces, and (2) Coulomb’s law—the fundamental law of electrostatics. From these, all else followed.

You may have noticed, in studying Exs. 2.5 and 2.6, or working problems such as 2.7, 2.11, and 2.16, that the electric field always undergoes a discontinuity when you cross a surface charge σ. In fact, it is a simple matter to find the amount by which E changes at such a boundary. Suppose we draw a wafer-thin Gaussian pillbox, extending just barely over the edge in each direction (Fig. 2.36). Gauss’s law says that ∫ E · da = Q_enc / ε₀ = σA / ε₀, where A is the area of the pillbox lid. (If σ varies from point to point or the surface is curved, we must pick A to be extremely small.) Now, the sides of the pillbox contribute nothing to the flux, in the limit as the thickness ε goes to zero, so we are left with E⊥_above − E⊥_below = σ / ε₀, (2.31)

where E⊥ denotes the component of E that is perpendicular to the surface immediately above, and E⊥ is the same, only just below the surface. For consistency, we let “upward” be the positive direction for both. Conclusion: The normal component of E is discontinuous by an amount σ/ε₀ at any boundary. In particular, where there is no surface charge, E⊥ is continuous, as for instance at the surface of a uniformly charged solid sphere.

The tangential component of E, by contrast, is always continuous. For if we apply Eq. 2.19, ∫ E · dl = 0, to the thin rectangular loop of Fig. 2.37, the ends give nothing (as ε → 0), and the sides give (E_∥_above − E_∥_below)l, so E_∥_above = E_∥_below, (2.32)

where E_∥ stands for the components of E parallel to the surface. The boundary conditions on E (Eqs. 2.31 and 2.32) can be combined into a single formula: E_above − E_below = (σ / ε₀) n̂, (2.33)

where n̂ is a unit vector perpendicular to the surface, pointing from “below” to “above.”⁸

The potential, meanwhile, is continuous across any boundary (Fig. 2.38), since V_above − V_below = −∫ E · dl; as the path length shrinks to zero, so too does the integral: V_above = V_below. (2.34)

However, the gradient of V inherits the discontinuity in E; since E = −∇V, Eq. 2.33 implies that ∇V_above − ∇V_below = −(σ / ε₀) n̂, (2.35)

or, more conveniently, ∂V_above/∂n − ∂V_below/∂n = −σ / ε₀, (2.36)

where ∂V/∂n = ∇V · n̂ (2.37)

denotes the normal derivative of V (that is, the rate of change in the direction perpendicular to the surface).

Please note that these boundary conditions relate the fields and potentials just above and just below the surface. For example, the derivatives in Eq. 2.36 are the limiting values as we approach the surface from either side.

⁸ Notice that it doesn’t matter which side you call “above” and which “below,” since reversal would switch the direction of n̂. Incidentally, if you’re only interested in the field due to the (essentially flat) local patch of surface charge itself, the answer is (σ/2ε₀) n̂ immediately above the surface, and −(σ/2ε₀) n̂ immediately below. This follows from Ex. 2.5, for if you are close enough to the patch it “looks” like an infinite plane. Evidently the entire discontinuity in E is attributable to this local patch of surface charge.

Problem 2.30 (a) Check that the results of Exs. 2.5 and 2.6, and Prob. 2.11, are consistent with Eq. 2.33.

(b) Use Gauss’s law to find the field inside and outside a long hollow cylindrical tube, which carries a uniform surface charge σ. Check that your result is consistent with Eq. 2.33.

(c) Check that the result of Ex. 2.8 is consistent with boundary conditions 2.34 and 2.36.

## 2.4 Work and Energy in Electrostatics

2.4.1 The Work It Takes to Move a Charge

Suppose you have a stationary configuration of source charges, and you want to move a test charge Q from point a to point b (Fig. 2.39). Question: How much work will you have to do? At any point along the path, the electric force on Q is F = QE; the force you must exert, in opposition to this electrical force, is −QE. (If the sign bothers you, think about lifting a brick: gravity exerts a force mg downward, but you exert a force mg upward. Of course, you could apply an even greater force—then the brick would accelerate, and part of your effort would be “wasted” generating kinetic energy. What we’re interested in here is the minimum force you must exert to do the job.) The work you do is therefore W = ∫_a^b F · dl = −Q ∫_a^b E · dl = Q[V(b) − V(a)].

Notice that the answer is independent of the path you take from a to b; in mechanics, then, we would call the electrostatic force “conservative.” Dividing through by Q, we have V(b) − V(a) = W/Q. (2.38)

In words, the potential difference between points a and b is equal to the work per unit charge required to carry a particle from a to b. In particular, if you want to bring Q in from far away and stick it at point r, the work you must do is W = Q[V(r) − V(∞)], so, if you have set the reference point at infinity, W = QV(r). (2.39)

In this sense, potential is potential energy (the work it takes to create the system) per unit charge (just as the field is the force per unit charge).

2.4.2 The Energy of a Point Charge Distribution

How much work would it take to assemble an entire collection of point charges? Imagine bringing in the charges, one by one, from far away (Fig. 2.40). The first charge, q₁, takes no work, since there is no field yet to fight against. Now bring in q₂. According to Eq. 2.39, this will cost you q₂ V₁(r₂), where V₁ is the potential due to q₁, and r₂ is the place we’re putting q₂: W₂ = (1/4πε₀)(q₁q₂/r₁₂), (where r₁₂ is the distance between q₁ and q₂ once they are in position). As you bring in each charge, nail it down in its final location, so it doesn’t move when you bring in the next charge. Now bring in q₃; this requires work q₃ V₁,₂(r₃), where V₁,₂ is the potential due to charges q₁ and q₂, namely, (1/4πε₀)(q₁/r₁₃ + q₂/r₂₃). Thus W₃ = (1/4πε₀)(q₁q₃/r₁₃ + q₂q₃/r₂₃).

Similarly, the extra work to bring in q₄ will be W₄ = (1/4πε₀)(q₁q₄/r₁₄ + q₂q₄/r₂₄ + q₃q₄/r₃₄).

The total work necessary to assemble the first four charges, then, is W = (1/4πε₀)(q₁q₂/r₁₂ + q₁q₃/r₁₃ + q₁q₄/r₁₄ + q₂q₃/r₂₃ + q₂q₄/r₂₄ + q₃q₄/r₃₄).

You see the general rule: Take the product of each pair of charges, divide by their separation distance, and add it all up: W = (1/4πε₀) ∑_{i=1}^n ∑_{j>i}^n q_i q_j / r_ij. (2.40)

The stipulation j > i is to remind you not to count the same pair twice. A nicer way to accomplish this is intentionally to count each pair twice, and then divide by 2: W = (1/8πε₀) ∑_{i=1}^n ∑_{j≠i}^n q_i q_j / r_ij (2.41)

(we must still avoid i = j, of course). Notice that in this form the answer plainly does not depend on the order in which you assemble the charges, since every pair occurs in the sum.

Finally, let’s pull out the factor q_i: W = (1/2) ∑_{i=1}^n q_i [ (1/4πε₀) ∑_{j≠i}^n q_j / r_ij ].

The term in parentheses is the potential at point r_i (the position of q_i) due to all the other charges—all of them, now, not just the ones that were present at some stage during the assembly. Thus, W = (1/2) ∑_{i=1}^n q_i V(r_i). (2.42)

That’s how much work it takes to assemble a configuration of point charges; it’s also the amount of work you’d get back if you dismantled the system. In the meantime, it represents energy stored in the configuration (“potential” energy, if you insist, though for obvious reasons I prefer to avoid that word in this context).

Problem 2.31 (a) Three charges are situated at the corners of a square (side a), as shown in Fig. 2.41. How much work does it take to bring in another charge, +q, from far away and place it in the fourth corner?

(b) How much work does it take to assemble the whole configuration of four charges?

Problem 2.32 Two positive point charges, q_A and q_B (masses m_A and m_B) are at rest, held together by a massless string of length a. Now the string is cut, and the particles fly off in opposite directions. How fast is each one going, when they are far apart?

Problem 2.33 Consider an infinite chain of point charges, ±q (with alternating signs), strung out along the x axis, each a distance a from its nearest neighbors. Find the work per particle required to assemble this system. [Partial Answer: −αq²/(4πε₀a), for some dimensionless number α; your problem is to determine α. It is known as the Madelung constant. Calculating the Madelung constant for 2- and 3-dimensional arrays is much more subtle and difficult.]

2.4.3 The Energy of a Continuous Charge Distribution

For a volume charge density ρ, Eq. 2.42 becomes W = (1/2) ∫ ρV dτ. (2.43)

(The corresponding integrals for line and surface charges would be (1/2) ∫ λV dl and (1/2) ∫ σV da.) There is a lovely way to rewrite this result, in which ρ and V are eliminated in favor of E. First use Gauss’s law to express ρ in terms of E: ρ = ε₀ ∇·E, so W = (ε₀/2) ∫ (∇·E) V dτ.

\( \int (\nabla \cdot \mathbf{E}) V \, d\tau \).

Now use integration by parts (Eq. 1.59) to transfer the derivative from \( \mathbf{E} \) to \( V \): \[ \int (\nabla \cdot \mathbf{E}) V \, d\tau = - \int \mathbf{E} \cdot (\nabla V) \, d\tau + \oint V \mathbf{E} \cdot d\mathbf{a} \, . \]

But \( \nabla V = -\mathbf{E} \), so \[ W = \frac{\epsilon_0}{2} \left[ \int E^2 \, d\tau + \oint V \mathbf{E} \cdot d\mathbf{a} \right] . \] (2.44)

But what volume is this we're integrating over? Let's go back to the formula we started with, Eq. 2.43. From its derivation, it is clear that we should integrate over the region where the charge is located. But actually, any larger volume would do just as well: The "extra" territory we throw in will contribute nothing to the integral, since \( \rho = 0 \) out there. With this in mind, we return to Eq. 2.44. What happens here, as we enlarge the volume beyond the minimum necessary to trap all the charge? Well, the integral of \( E^2 \) can only increase (the integrand being positive); evidently the surface integral must decrease correspondingly to leave the sum intact. (In fact, at large distances from the charge, \( \mathbf{E} \) goes like \( 1/r^2 \) and \( V \) like \( 1/r \), while the surface area grows like \( r^2 \); roughly speaking, then, the surface integral goes down like \( 1/r \).) Please understand: Eq. 2.44 gives you the correct energy \( W \), whatever volume you use (as long as it encloses all the charge), but the contribution from the volume integral goes up, and that of the surface integral goes down, as you take larger and larger volumes. In particular, why not integrate over all space? Then the surface integral goes to zero, and we are left with \[ W = \frac{\epsilon_0}{2} \int E^2 \, d\tau \quad \text{(all space)}. \] (2.45)

Example 2.9. Find the energy of a uniformly charged spherical shell of total charge \( q \) and radius \( R \).

Solution 1 Use Eq. 2.43, in the version appropriate to surface charges: \[ W = \frac{1}{2} \int \sigma V \, da . \]

Now, the potential at the surface of this sphere is \( \frac{1}{4\pi\epsilon_0} \frac{q}{R} \) (a constant—Ex. 2.7), so \[ W = \frac{1}{2} \frac{q}{4\pi\epsilon_0 R} \int \sigma \, da = \frac{1}{8\pi\epsilon_0} \frac{q^2}{R} . \]

Solution 2 Use Eq. 2.45. Inside the sphere, \( \mathbf{E} = 0 \); outside, \[ \mathbf{E} = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{\mathbf{r}}, \quad \text{so} \quad E^2 = \frac{q^2}{(4\pi\epsilon_0)^2 r^4} . \]

Therefore, \[ W = \frac{\epsilon_0}{2} \int_{\text{outside}} (r^2 \sin\theta \, dr \, d\theta \, d\phi) \frac{q^2}{(4\pi\epsilon_0)^2 r^4} \]

\[ = \frac{q^2}{32\pi^2\epsilon_0} \int_0^{\pi} \sin\theta \, d\theta \int_0^{2\pi} d\phi \int_R^{\infty} \frac{dr}{r^2} = \frac{q^2}{8\pi\epsilon_0 R} . \]

Problem 2.34 Find the energy stored in a uniformly charged solid sphere of radius \( R \) and charge \( q \). Do it three different ways: (a) Use Eq. 2.43. You found the potential in Prob. 2.21.

(b) Use Eq. 2.45. Don't forget to integrate over all space.

(c) Use Eq. 2.44. Take a spherical volume of radius \( a \). What happens as \( a \to \infty \)?

Problem 2.35 Here is a fourth way of computing the energy of a uniformly charged solid sphere: Assemble it like a snowball, layer by layer, each time bringing in an infinitesimal charge \( dq \) from far away and smearing it uniformly over the surface, thereby increasing the radius. How much work \( dW \) does it take to build up the radius by an amount \( dr \)? Integrate this to find the work necessary to create the entire sphere of radius \( R \) and total charge \( q \).

2.4.4 Comments on Electrostatic Energy (i) A perplexing "inconsistency." Equation 2.45 clearly implies that the energy of a stationary charge distribution is always positive. On the other hand, Eq. 2.42 (from which 2.45 was in fact derived), can be positive or negative. For instance, according to Eq. 2.42, the energy of two equal but opposite charges a distance \( r \) apart is \( -(1/4\pi\epsilon_0)(q^2/r) \). What's gone wrong? Which equation is correct?

The answer is that both are correct, but they speak to slightly different questions. Equation 2.42 does not take into account the work necessary to make the point charges in the first place; we started with point charges and simply found the work required to bring them together. This is wise strategy, since Eq. 2.45 indicates that the energy of a point charge is in fact infinite: \[ W = \frac{\epsilon_0}{2} \int (r^2 \sin\theta \, dr \, d\theta \, d\phi) \frac{q^2}{(4\pi\epsilon_0)^2 r^4} = \frac{q^2}{8\pi\epsilon_0} \int_0^{\infty} \frac{dr}{r^2} = \infty . \]

Equation 2.45 is more complete, in the sense that it tells you the total energy stored in a charge configuration, but Eq. 2.42 is more appropriate when you're dealing with point charges, because we prefer (for good reason!) to leave out that portion of the total energy that is attributable to the fabrication of the point charges themselves. In practice, after all, the point charges (electrons, say) are given to us ready-made; all we do is move them around. Since we did not put them together, and we cannot take them apart, it is immaterial how much work the process would involve. (Still, the infinite energy of a point charge is a recurring source of embarrassment for electromagnetic theory, afflicting the quantum version as well as the classical. We shall return to the problem in Chapter 11.)

Now, you may wonder where the inconsistency crept into an apparently watertight derivation. The "flaw" lies between Eqs. 2.42 and 2.43: in the former, \( V(\mathbf{r}_i) \) represents the potential due to all the other charges but not \( q_i \), whereas in the latter, \( V(\mathbf{r}) \) is the full potential. For a continuous distribution, there is no distinction, since the amount of charge right at the point \( \mathbf{r} \) is vanishingly small, and its contribution to the potential is zero. But in the presence of point charges you'd better stick with Eq. 2.42.

(ii) Where is the energy stored? Equations 2.43 and 2.45 offer two different ways of calculating the same thing. The first is an integral over the charge distribution; the second is an integral over the field. These can involve completely different regions. For instance, in the case of the spherical shell (Ex. 2.9) the charge is confined to the surface, whereas the electric field is everywhere outside this surface. Where is the energy, then? Is it stored in the field, as Eq. 2.45 seems to suggest, or is it stored in the charge, as Eq. 2.43 implies? At the present stage this is simply an unanswerable question: I can tell you what the total energy is, and I can provide you with several different ways to compute it, but it is impertinent to worry about where the energy is located. In the context of radiation theory (Chapter 11) it is useful (and in general relativity it is essential) to regard the energy as stored in the field, with a density \( \frac{\epsilon_0}{2} E^2 = \) energy per unit volume. (2.46)

But in electrostatics one could just as well say it is stored in the charge, with a density \( \frac{1}{2} \rho V \). The difference is purely a matter of bookkeeping.

(iii) The superposition principle. Because electrostatic energy is quadratic in the fields, it does not obey a superposition principle. The energy of a compound system is not the sum of the energies of its parts considered separately—there are also "cross terms": \[ W_{\text{tot}} = \frac{\epsilon_0}{2} \int (E_1 + E_2)^2 \, d\tau \]

\[ = \frac{\epsilon_0}{2} \int \left( E_1^2 + E_2^2 + 2 \mathbf{E}_1 \cdot \mathbf{E}_2 \right) \, d\tau \]

\[ = W_1 + W_2 + \epsilon_0 \int \mathbf{E}_1 \cdot \mathbf{E}_2 \, d\tau . \] (2.47)

For example, if you double the charge everywhere, you quadruple the total energy.

Problem 2.36 Consider two concentric spherical shells, of radii \( a \) and \( b \). Suppose the inner one carries a charge \( q \), and the outer one a charge \( -q \) (both of them uniformly distributed over the surface). Calculate the energy of this configuration, (a) using Eq. 2.45, and (b) using Eq. 2.47 and the results of Ex. 2.9.

Problem 2.37 Find the interaction energy \( (\epsilon_0 \int \mathbf{E}_1 \cdot \mathbf{E}_2 \, d\tau \) in Eq. 2.47) for two point charges, \( q_1 \) and \( q_2 \), a distance \( a \) apart. [Hint: Put \( q_1 \) at the origin and \( q_2 \) on the \( z \) axis; use spherical coordinates, and do the \( r \) integral first.]

## 2.5 CONDUCTORS

2.5.1 Basic Properties In an insulator, such as glass or rubber, each electron is on a short leash, attached to a particular atom. In a metallic conductor, by contrast, one or more electrons per atom are free to roam. (In liquid conductors such as salt water, it is ions that do the moving.) A perfect conductor would contain an unlimited supply of free charges. In real life there are no perfect conductors, but metals come pretty close, for most purposes.

From this definition, the basic electrostatic properties of ideal conductors immediately follow: (i) \( \mathbf{E} = 0 \) inside a conductor. Why? Because if there were any field, those free charges would move, and it wouldn't be electrostatics any more. Hmm ... that's hardly a satisfactory explanation; maybe all it proves is that you can't have electrostatics when conductors are present. We had better examine what happens when you put a conductor into an external electric field \( \mathbf{E}_0 \) (Fig. 2.42). Initially, the field will drive any free positive charges to the right, and negative ones to the left. (In practice, it's the negative charges—electrons—that do the moving, but when they depart, the right side is left with a net positive charge—the stationary nuclei—so it doesn't really matter which charges move; the effect is the same.) When they come to the edge of the material, the charges pile up: plus on the right side, minus on the left. Now, these induced charges produce a field of their own, \( \mathbf{E}_1 \), which, as you can see from the figure, is in the opposite direction to \( \mathbf{E}_0 \). That's the crucial point, for it means that the field of the induced charges tends to cancel the original field. Charge will continue to flow until this cancellation is complete, and the resultant field inside the conductor is precisely zero.⁹ The whole process is practically instantaneous.

(ii) \( \rho = 0 \) inside a conductor. This follows from Gauss's law: \( \nabla \cdot \mathbf{E} = \rho/\epsilon_0 \). If \( \mathbf{E} \) is zero, so also is \( \rho \). There is still charge around, but exactly as much plus as minus, so the net charge density in the interior is zero.

(iii) Any net charge resides on the surface. That's the only place left.

(iv) A conductor is an equipotential. For if \( a \) and \( b \) are any two points within (or at the surface of) a given conductor, \( V(b) - V(a) = -\int_a^b \mathbf{E} \cdot d\mathbf{l} = 0 \), and hence \( V(a) = V(b) \).

(v) \( \mathbf{E} \) is perpendicular to the surface, just outside a conductor. Otherwise, as in (i), charge will immediately flow around the surface until it kills off the tangential component (Fig. 2.43). (Perpendicular to the surface, charge cannot flow, of course, since it is confined to the conducting object.)

\( \text{Figure 2.42: Charges induced on a conductor in an external electric field } \mathbf{E}_0. \)

\( \text{Figure 2.43: Just outside a conductor, the electric field is perpendicular to the surface.} \)

⁹ Outside the conductor the field is not zero, for here \( \mathbf{E}_0 \) and \( \mathbf{E}_1 \) do not tend to cancel.

I think it is astonishing that the charge on a conductor flows to the surface. Because of their mutual repulsion, the charges naturally spread out as much as possible, but for all of them to go to the surface seems like a waste of the interior space. Surely we could do better, from the point of view of making each charge as far as possible from its neighbors, to sprinkle some of them throughout the volume ... Well, it simply is not so. You do best to put all the charge on the surface, and this is true regardless of the size or shape of the conductor.¹⁰ The problem can also be phrased in terms of energy. Like any other free dynamical system, the charge on a conductor will seek the configuration that minimizes its potential energy. What property (iii) asserts is that the electrostatic energy of a solid object (with specified shape and total charge) is a minimum when that charge is spread over the surface. For instance, the energy of a sphere is (1/8πε₀)(q²/R) if the charge is uniformly distributed over the surface, as we found in Ex. 2.9, but it is greater, (3/20πε₀)(q²/R), if the charge is uniformly distributed throughout the volume (Prob. 2.34).

2.5.2 Induced Charges If you hold a charge +q near an uncharged conductor (Fig. 2.44), the two will attract one another. The reason for this is that q will pull minus charges over to the near side and repel plus charges to the far side. (Another way to think of it is that the charge moves around in such a way as to kill off the field of q for points inside the conductor, where the total field must be zero.) Since the negative induced charge is closer to q, there is a net force of attraction. (In Chapter 3 we shall calculate this force explicitly, for the case of a spherical conductor.)

When I speak of the field, charge, or potential “inside” a conductor, I mean in the “meat” of the conductor; if there is some hollow cavity in the conductor, and within that cavity you put some charge, then the field in the cavity will not be zero. But in a remarkable way the cavity and its contents are electrically isolated from the outside world by the surrounding conductor (Fig. 2.45). No external fields penetrate the conductor; they are canceled at the outer surface by the induced charge there. Similarly, the field due to charges within the cavity is canceled, for all exterior points, by the induced charge on the inner surface. However, the compensating charge left over on the outer surface of the conductor effectively “communicates” the presence of q to the outside world. The total charge induced on the cavity wall is equal and opposite to the charge inside, for if we surround the cavity with a Gaussian surface, all points of which are in the conductor (Fig. 2.45), ∫E·da=0, and hence (by Gauss’s law) the net enclosed charge must be zero. But Q_enclosed = q + q_induced, so q_induced = −q. Then if the conductor as a whole is electrically neutral, there must be a charge +q on its outer surface.

Example 2.10. An uncharged spherical conductor centered at the origin has a cavity of some weird shape carved out of it (Fig. 2.46). Somewhere within the cavity is a charge q. Question: What is the field outside the sphere?

Solution At first glance, it would appear that the answer depends on the shape of the cavity and the location of the charge. But that’s wrong: the answer is E = (1/4πε₀)(q/r²) r̂ regardless. The conductor conceals from us all information concerning the nature of the cavity, revealing only the total charge it contains. How can this be? Well, the charge +q induces an opposite charge −q on the wall of the cavity, which distributes itself in such a way that its field cancels that of q, for all points exterior to the cavity. Since the conductor carries no net charge, this leaves +q to distribute itself uniformly over the surface of the sphere. (It’s uniform because the asymmetrical influence of the point charge +q is negated by that of the induced charge −q on the inner surface.) For points outside the sphere, then, the only thing that survives is the field of the leftover +q, uniformly distributed over the outer surface.

It may occur to you that in one respect this argument is open to challenge: There are actually three fields at work here: E_q, E_induced, and E_leftover. All we know for certain is that the sum of the three is zero inside the conductor, yet I claimed that the first two alone cancel, while the third is separately zero there. Moreover, even if the first two cancel within the conductor, who is to say they still cancel for points outside? They do not, after all, cancel for points inside the cavity. I cannot give you a completely satisfactory answer at the moment, but this much at least is true: There exists a way of distributing −q over the inner surface so as to cancel the field of q at all exterior points. For that same cavity could have been carved out of a huge spherical conductor with a radius of 27 miles or light years or whatever. In that case, the leftover +q on the outer surface is simply too far away to produce a significant field, and the other two fields would have to accomplish the cancellation by themselves. So we know they can do it ... but are we sure they choose to? Perhaps for small spheres nature prefers some complicated three-way cancellation. Nope: As we’ll see in the uniqueness theorems of Chapter 3, electrostatics is very stingy with its options; there is always precisely one way—no more—of distributing the charge on a conductor so as to make the field inside zero. Having found a possible way, we are guaranteed that no alternative exists, even in principle.

If a cavity surrounded by conducting material is itself empty of charge, then the field within the cavity is zero. For any field line would have to begin and end on the cavity wall, going from a plus charge to a minus charge (Fig. 2.47). Letting that field line be part of a closed loop, the rest of which is entirely inside the conductor (where E=0), the integral ∫E·dl is distinctly positive, in violation of Eq. 2.19. It follows that E=0 within an empty cavity, and there is in fact no charge on the surface of the cavity. (This is why you are relatively safe inside a metal car during a thunderstorm—you may get cooked, if lightning strikes, but you will not be electrocuted. The same principle applies to the placement of sensitive apparatus inside a grounded Faraday cage, to shield out stray electric fields. In practice, the enclosure doesn’t even have to be solid conductor—chicken wire will often suffice.)

Problem 2.38 A metal sphere of radius R, carrying charge q, is surrounded by a thick concentric metal shell (inner radius a, outer radius b, as in Fig. 2.48). The shell carries no net charge.

(a) Find the surface charge density σ at R, at a, and at b.

(b) Find the potential at the center, using infinity as the reference point.

(c) Now the outer surface is touched to a grounding wire, which drains off charge and lowers its potential to zero (same as at infinity). How do your answers to (a) and (b) change?

Problem 2.39 Two spherical cavities, of radii a and b, are hollowed out from the interior of a (neutral) conducting sphere of radius R (Fig. 2.49). At the center of each cavity a point charge is placed—call these charges q_a and q_b.

(a) Find the surface charge densities σ_a, σ_b, and σ_R.

(b) What is the field outside the conductor?

(c) What is the field within each cavity?

(d) What is the force on q_a and q_b?

(e) Which of these answers would change if a third charge, q_c, were brought near the conductor?

Problem 2.40 (a) A point charge q is inside a cavity in an uncharged conductor (Fig. 2.45). Is the force on q necessarily zero?

(b) Is the force between a point charge and a nearby uncharged conductor always attractive?

2.5.3 Surface Charge and the Force on a Conductor Because the field inside a conductor is zero, boundary condition 2.33 requires that the field immediately outside is E = (σ/ε₀) n̂, (2.48)

consistent with our earlier conclusion that the field is normal to the surface. In terms of potential, Eq. 2.36 yields σ = −ε₀ (∂V/∂n). (2.49)

These equations enable you to calculate the surface charge on a conductor, if you can determine E or V; we shall use them frequently in the next chapter.

In the presence of an electric field, a surface charge will experience a force; the force per unit area, f, is σE. But there’s a problem here, for the electric field is discontinuous at a surface charge, so what are we supposed to use: E_above, E_below, or something in between? The answer is that we should use the average of the two: f = σ E_average = (1/2)σ (E_above + E_below). (2.50)

Why the average? The reason is very simple, though the telling makes it sound complicated: Let’s focus our attention on a tiny patch of surface surrounding the point in question (Fig. 2.50). (Make it small enough so it is essentially flat and the surface charge on it is essentially constant.) The total field consists of two parts—that attributable to the patch itself, and that due to everything else (other regions of the surface, as well as any external sources that may be present): E = E_patch + E_other.

Now, the patch cannot exert a force on itself, any more than you can lift yourself by standing in a basket and pulling up on the handles. The force on the patch, then, is due exclusively to E_other, and this suffers no discontinuity (if we removed the patch, the field in the “hole” would be perfectly smooth). The discontinuity is due entirely to the charge on the patch, which puts out a field (σ/2ε₀) on either side, pointing away from the surface. Thus, E_above = E_other + (σ/2ε₀) n̂, E_below = E_other − (σ/2ε₀) n̂, and hence E_other = (1/2)(E_above + E_below) = E_average.

Averaging is really just a device for removing the contribution of the patch itself.

That argument applies to any surface charge; in the particular case of a conductor, the field is zero inside and (σ/ε₀) n̂ outside (Eq. 2.48), so the average is (σ/2ε₀) n̂, and the force per unit area is f = (σ²/2ε₀) n̂. (2.51)

This amounts to an outward electrostatic pressure on the surface, tending to draw the conductor into the field, regardless of the sign of σ. Expressing the pressure in terms of the field just outside the surface, P = (ε₀/2) E². (2.52)

Problem 2.41 Two large metal plates (each of area A) are held a small distance d apart. Suppose we put a charge Q on each plate; what is the electrostatic pressure on the plates?

Problem 2.42 A metal sphere of radius R carries a total charge Q. What is the force of repulsion between the “northern” hemisphere and the “southern” hemisphere?

2.5.4 电容器假设我们有两个导体，其中一个带正电荷 +Q，另一个带负电荷 −Q（图2.51）。由于导体内部电势 V 是常数，我们可以明确定义它们之间的电势差： $$V = V_+ - V_- = -\int_{(-)}^{(+)} \mathbf{E} \cdot d\mathbf{l}$$ 我们不知道电荷在两个导体上如何分布，如果形状复杂，计算电场会非常困难，但我们知道一点：E 与 Q 成正比。因为根据库仑定律： $$\mathbf{E} = \frac{1}{4\pi\epsilon_0} \int \frac{\rho}{r^2} \hat{\mathbf{r}} \, d\tau$$ 所以如果 ρ 加倍，E 也加倍。等等！我们怎么知道 Q（以及 −Q）加倍就简单地让 ρ 加倍？也许电荷会重新分布，形成完全不同的构型，某些地方的 ρ 变为四倍，而其他地方减半，以保证每个导体上的总电荷加倍。事实上，这种担忧是多余的——Q 加倍确实会使 ρ 在所有地方加倍；它不会移动电荷分布。证明将在第3章给出；现在你只需相信我。

由于 E 与 Q 成正比，V 也如此。比例常数称为该排列的电容： $$C \equiv \frac{Q}{V} \quad (2.53)$$ 电容是一个纯粹的几何量，由两个导体的尺寸、形状和间距决定。在SI单位中，C 的单位是法拉（F）；一法拉是库仑每伏特。实际上，这太大而不实用；更常用的单位是微法拉（10⁻⁶ F）和皮法拉（10⁻¹² F）。

注意，根据定义，V 是正导体的电势减去负导体的电势；同样，Q 是正导体的电荷。因此，电容本质上是一个正量。（顺便说一句，你偶尔会听到有人谈论单个导体的电容。在这种情况下，带有负电荷的“第二个导体”是一个环绕该导体的无限大半径的想象中的球面壳。它对电场没有贡献，因此电容由公式2.53给出，其中 V 是以无穷远为参考点的电势。）

例如，求由两个相距 d、面积为 A 的金属表面组成的平行板电容器的电容（图2.52）。

解：如果我们在上板放 +Q，下板放 −Q，只要面积足够大且间距很小，电荷会均匀分布在两个表面上。于是，表面电荷密度为 σ = Q/A（上板），根据例2.6，电场为 (1/ε₀)Q/A。因此，板间电势差为： $$V = \frac{Qd}{A\epsilon_0}$$ 从而 $$C_0 = \frac{A\epsilon_0}{d} \quad (2.54)$$ 例如，如果板是边长为1 cm的正方形，间距为1 mm，则电容为 9×10⁻¹³ F。

例2.12 求两个同心金属球壳的电容，半径分别为 a 和 b。

解：在内球上放置电荷 +Q，外球上放置 −Q。球间电场为： $$\mathbf{E} = \frac{1}{4\pi\epsilon_0} \frac{Q}{r^2} \hat{\mathbf{r}}$$ 因此，它们之间的电势差为： $$V = -\int_{b}^{a} \mathbf{E} \cdot d\mathbf{l} = -\int_{b}^{a} \frac{Q}{4\pi\epsilon_0 r^2} dr = \frac{Q}{4\pi\epsilon_0} \left( \frac{1}{a} - \frac{1}{b} \right)$$ 如前所述，V 与 Q 成正比；电容为： $$C_0 = \frac{Q}{V} = 4\pi\epsilon_0 \frac{ab}{b - a}$$

要“给电容器充电”，你必须将电子从正极板移开并送到负极板。这样做时，你对抗着电场，电场将它们拉回正导体并推离负导体。那么，将电容器充电到最终电荷 Q 需要做多少功？假设在过程的某个中间阶段，正极板上的电荷为 q，因此电势差为 q/C。根据公式2.38，你必须做的功来输送下一个电荷元 dq 为： $$dW = \frac{q}{C} dq$$ 那么，从 q = 0 到 q = Q 所需的总功为： $$W = \int_{0}^{Q} \frac{q}{C} dq = \frac{Q^2}{2C}$$ 或者，由于 Q = CV， $$W = \frac{1}{2} CV^2 \quad (2.55)$$ 其中 V 是电容器的最终电势。

问题2.43 求两个同轴金属圆管（半径 a 和 b）的单位长度电容（图2.53）。

问题2.44 假设平行板电容器的板因相互吸引而彼此靠近一个无穷小距离 δ。(a) 用电场 E 和板面积 A 表示静电力所做的功。(b) 用公式2.46表示此过程中电场损失的能量。（这个问题应该很简单，但它包含了利用能量守恒推导公式2.52的萌芽。）

问题2.45 求均匀表面电荷密度为 σ 的正方形薄板（边长 a）中心上方高度 z 处的电场。检查极限情况 a → ∞ 和 z ≫ a 的结果。

问题2.46 如果某个区域的电场（球坐标）给定为表达式 $$\mathbf{E}(r) = k \left( 3\hat{\mathbf{r}} + 2\sin\theta\cos\theta\sin\phi \hat{\boldsymbol{\theta}} + \sin\theta\cos\phi \hat{\boldsymbol{\phi}} \right)$$ 其中 k 是常数，那么电荷密度是多少？

问题2.47 求均匀带电实心球的南半球对北半球的净作用力。用半径 R 和总电荷 Q 表示答案。

问题2.48 一个半径为 R 的倒置半球形碗具有均匀表面电荷密度 σ。求“北极”与中心之间的电势差。

问题2.49 一个半径为 R 的球具有电荷密度 ρ(r) = kr（k 是常数）。求该构型的能量。通过至少两种不同的方法计算来验证你的答案。

问题2.50 某些构型的电势给定为表达式 $$V(r) = A \frac{e^{-\lambda r}}{r}$$ 其中 A 和 λ 是常数。求电场 E(r)、电荷密度 ρ(r) 和总电荷 Q。

问题2.51 求均匀带电圆盘（半径 R，电荷密度 σ）边缘上的电势。[提示：首先证明 V = k(σR/πε₀)，其中 k 是某个无量纲数，你可以表示为一个积分。然后解析求出 k，或者用计算机计算。]

问题2.52 两根无限长导线平行于 x 轴，带有均匀电荷密度 +λ 和 −λ（图2.54）。(a) 求任意点 (x, y, z) 的电势，以原点为参考。(b) 证明等势面是圆柱面，并定位对应于给定电势 V 的圆柱面的轴和半径。

问题2.53 在真空二极管中，电子从热阴极（电势为零）“沸腾”出来，跨越间隙加速到阳极，阳极保持正电势 V。间隙内移动的电子云（称为空间电荷）很快积累到足以使阴极表面的电场减为零。此后，一个恒定电流 I 在板间流动。

假设板相对于间距很大（A ≫ d²，图2.55），因此可以忽略边缘效应。那么 V、ρ 和 v（电子速度）都只是 x 的函数。

(a) 写出板间区域的泊松方程。

(b) 假设电子从阴极静止开始，它们在电势为 V(x) 的点 x 处的速度是多少？

(c) 在稳态下，I 与 x 无关。那么 ρ 和 v 之间的关系是什么？

(d) 使用这三个结果，通过消去 ρ 和 v 来获得 V 的微分方程。

(e) 解这个方程得到 V 作为 x、V₀ 和 d 的函数。绘制 V(x)，并将其与无空间电荷时的电势进行比较。同时，求 ρ 和 v 作为 x 的函数。

(f) 证明 $$I = K V^{3/2} \quad (2.56)$$ 并求常数 K。（方程2.56称为Child-Langmuir定律。它也适用于其他几何结构，当空间电荷限制电流时。注意空间电荷限制的二极管是非线性的——它不遵守欧姆定律。）

问题2.54 想象一下，新的、极其精确的测量揭示了库仑定律的一个错误。两个点电荷之间的实际相互作用力被发现是： $$\mathbf{F} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2} \left(1 + \frac{r}{\lambda} e^{-r/\lambda}\right) \hat{\mathbf{r}}$$ 其中 λ 是一个新的自然常数（显然它具有长度量纲，是一个巨大的数字——比如已知宇宙半径的一半——因此修正很小，这就是为什么以前没人注意到这个差异）。你的任务是重新构建静电学以适应这一新发现。假设叠加原理仍然成立。

(a) 电荷分布 ρ 的电场是什么（替代公式2.8）？

(b) 这个电场是否可以表示为标量势？简要解释你是如何得出结论的。（无需正式证明——只需有说服力的论证。）

(c) 求点电荷 q 的电势——类似于公式2.26。（如果你对(b)的回答是“不”，最好回去改一下！）以 ∞ 为参考点。

(d) 对于位于原点的点电荷 q，证明 $$\oint \mathbf{E} \cdot d\mathbf{a} + \frac{1}{\lambda^2} \int V d\tau = \frac{q}{\epsilon_0}$$ 其中 S 是任意球心在 q 处的球面，V 是其体积。

(e) 证明这个结果可以推广： $$\oint \mathbf{E} \cdot d\mathbf{a} + \frac{1}{\lambda^2} \int V d\tau = \frac{Q_{\text{enc}}}{\epsilon_0}$$ 对于任何电荷分布。（这是新“静电学”中仅次于高斯定律的次佳结论。）

(f) 为这个世界绘制三角形图（类似于图2.35），填入所有适当的公式。（将泊松方程视为 V 的 ρ 表达式，而高斯定律（微分形式）视为 E 的 ρ 方程。）

(g) 证明导体上的部分电荷会均匀分布在整个体积内，其余部分留在表面上。[提示：E 在导体内部仍然为零。]

问题2.55 假设电场 E(x, y, z) 具有形式 $$E_x = ax, \quad E_y = 0, \quad E_z = 0$$ 其中 a 是常数。电荷密度是多少？当电荷密度均匀时，你如何解释电场指向特定方向的事实？

问题2.56 所有静电学都源于库仑定律的 1/r² 特性以及叠加原理。因此，可以为牛顿万有引力定律构建类似的理论。假设密度均匀，质量为 M、半径为 R 的球体的引力势能是多少？利用你的结果估算太阳的引力能（查找相关数字）。注意能量是负的——质量相互吸引，而（同种）电荷相互排斥。当物质“坠入”以形成太阳时，其能量转化为其他形式（通常是热和辐射）。

ally thermal, and it is subsequently released in the form of radiation. The sun radiates at a rate of 3.86×10²⁶ W; if all this came from gravitational energy, how long would the sun last? [The sun is in fact much older than that, so evidently this is not the source of its power.¹⁴]

Problem 2.57 We know that the charge on a conductor goes to the surface, but just how it distributes itself there is not easy to determine. One famous example in which the surface charge density can be calculated explicitly is the ellipsoid:

x²/a² + y²/b² + z²/c² = 1.

In this case¹⁵

σ = Q/(4πabc) [x²/a⁴ + y²/b⁴ + z²/c⁴]⁻¹/²,  (2.57)

where Q is the total charge. By choosing appropriate values for a, b, and c, obtain (from Eq. 2.57): (a) the net (both sides) surface charge density σ(r) on a circular disk of radius R; (b) the net surface charge density σ(x) on an infinite conducting “ribbon” in the xy plane, which straddles the y axis from x = −a to x = a (let λ be the total charge per unit length of ribbon); (c) the net charge per unit length λ(x) on a conducting “needle,” running from x = −a to x = a. In each case, sketch the graph of your result.

Problem 2.58 (a) Consider an equilateral triangle, inscribed in a circle of radius a, with a point charge q at each vertex. The electric field is zero (obviously) at the center, but (surprisingly) there are three other points inside the triangle where the field is zero. Where are they? [Answer: r = 0.285a—you’ll probably need a computer to get it.]

(b) For a regular n-sided polygon there are n points (in addition to the center) where the field is zero.¹⁶ Find their distance from the center for n=4 and n=5. What do you suppose happens as n→∞?

¹⁴ Lord Kelvin used this argument to counter Darwin’s theory of evolution, which called for a much older Earth. Of course, we now know that the source of the Sun’s energy is nuclear fusion, not gravity.

¹⁵ For the derivation (which are a real tour de force), see W.R. Smythe, Static and Dynamic Electricity, 3rd ed. (New York: Hemisphere, 1989), Sect. 5.02.

¹⁶ S.D. Baker, Am. J. Phys. 52, 165 (1984); D. Kiang and D.A. Tindall, Am. J. Phys. 53, 593 (1985).

Problem 2.59 Prove or disprove (with a counterexample) the following Theorem: Suppose a conductor carrying a net charge Q, when placed in an external electric field E_e, experiences a force F; if the external field is now reversed (E_e → −E_e), the force also reverses (F → −F).

What if we stipulate that the external field is uniform?

Problem 2.60 A point charge q is at the center of an uncharged spherical conducting shell, of inner radius a and outer radius b. Question: How much work would it take to move the charge out to infinity (through a tiny hole drilled in the shell)? [Answer: (q²/8πε₀)(1/a − 1/b).]

Problem 2.61 What is the minimum-energy configuration for a system of N equal point charges placed on or inside a circle of radius R?¹⁷ Because the charge on a conductor goes to the surface, you might think the N charges would arrange themselves (uniformly) around the circumference. Show (to the contrary) that for N = 12 it is better to place 11 on the circumference and one at the center. How about for N = 11 (is the energy lower if you put all 11 around the circumference, or if you put 10 on the circumference and one at the center)? [Hint: Do it numerically—you’ll need at least 4 significant digits. Express all energies as multiples of q²/4πε₀R]

¹⁷ M.G. Calkin, D. Kiang, and D.A. Tindall, Am. H. Phys. 55, 157 (1987).

Chapter3 Potentials

## 3.1 Laplace’s Equation

3.1.1 Introduction The primary task of electrostatics is to find the electric field of a given stationary charge distribution. In principle, this purpose is accomplished by Coulomb’s law, in the form of Eq. 2.8:

E(r) = (1/4πε₀) ∫ [r̂ / |r − r′|²] ρ(r′) dτ′.  (3.1)

Unfortunately, integrals of this type can be difficult to calculate for any but the simplest charge configurations. Occasionally we can get around this by exploiting symmetry and using Gauss’s law, but ordinarily the best strategy is first to calculate the potential, V, which is given by the somewhat more tractable Eq. 2.29:

V(r) = (1/4πε₀) ∫ [1 / |r − r′|] ρ(r′) dτ′.  (3.2)

Still, even this integral is often too tough to handle analytically. Moreover, in problems involving conductors ρ itself may not be known in advance; since charge is free to move around, the only thing we control directly is the total charge (or perhaps the potential) of each conductor.

In such cases, it is fruitful to recast the problem in differential form, using Poisson’s equation (2.24),

∇²V = −ρ/ε₀,  (3.3)

which, together with appropriate boundary conditions, is equivalent to Eq. 3.2. Very often, in fact, we are interested in finding the potential in a region where ρ = 0. (If ρ = 0 everywhere, of course, then V = 0, and there is nothing further to say—that’s not what I mean. There may be plenty of charge elsewhere, but we’re confining our attention to places where there is no charge.) In this case, Poisson’s equation reduces to Laplace’s equation:

∇²V = 0,  (3.4)

or, written out in Cartesian coordinates,

∂²V/∂x² + ∂²V/∂y² + ∂²V/∂z² = 0.  (3.5)

This formula is so fundamental to the subject that one might almost say electrostatics is the study of Laplace’s equation. At the same time, it is a ubiquitous equation, appearing in such diverse branches of physics as gravitation and magnetism, the theory of heat, and the study of soap bubbles. In mathematics, it plays a major role in analytic function theory. To get a feel for Laplace’s equation and its solutions (which are called harmonic functions), we shall begin with the one- and two-dimensional versions, which are easier to picture, and illustrate all the essential properties of the three-dimensional case.

3.1.2 Laplace’s Equation in One Dimension Suppose V depends on only one variable, x. Then Laplace’s equation becomes

d²V/dx² = 0.

The general solution is

V(x) = mx + b,  (3.6)

the equation for a straight line. It contains two undetermined constants (m and b), as is appropriate for a second-order (ordinary) differential equation. They are fixed, in any particular case, by the boundary conditions of that problem. For instance, it might be specified that V = 4 at x = 1, and V = 0 at x = 5. In that case, m = −1 and b = 5, so V = −x + 5 (see Fig. 3.1).

I want to call your attention to two features of this result; they may seem silly and obvious in one dimension, where I can write down the general solution explicitly, but the analogs in two and three dimensions are powerful and by no means obvious:

1 2 3 4 5 6 x FIGURE 3.1

## 1. V(x) is the average of V(x + a) and V(x − a), for any a:

V(x) = (1/2)[V(x + a) + V(x − a)].

Laplace’s equation is a kind of averaging instruction; it tells you to assign to the point x the average of the values to the left and to the right of x. Solutions to Laplace’s equation are, in this sense, as boring as they could possibly be, and yet fit the endpoints properly.

2. Laplace’s equation tolerates no local maxima or minima; extreme values of V must occur at the end points. Actually, this is a consequence of (1), for if there were a local maximum, V would be greater at that point than on either side, and therefore could not be the average. (Ordinarily, you expect the second derivative to be negative at a maximum and positive at a minimum. Since Laplace’s equation requires, on the contrary, that the second derivative is zero, it seems reasonable that solutions should exhibit no extrema. However, this is not a proof, since there exist functions that have maxima and minima at points where the second derivative vanishes: x⁴, for example, has such a minimum at the point x = 0.)

3.1.3 Laplace’s Equation in Two Dimensions If V depends on two variables, Laplace’s equation becomes

∂²V/∂x² + ∂²V/∂y² = 0.

This is no longer an ordinary differential equation (that is, one involving ordinary derivatives only); it is a partial differential equation. As a consequence, some of the simple rules you may be familiar with do not apply. For instance, the general solution to this equation doesn’t contain just two arbitrary constants—or, for that matter, any finite number—despite the fact that it’s a second-order equation. Indeed, one cannot write down a “general solution” (at least, not in a closed form like Eq. 3.6). Nevertheless, it is possible to deduce certain properties common to all solutions.

It may help to have a physical example in mind. Picture a thin rubber sheet (or a soap film) stretched over some support. For definiteness, suppose you take a cardboard box, cut a wavy line all the way around, and remove the top part (Fig. 3.2). Now glue a tightly stretched rubber membrane over the box, so that it fits like a drum head (it won’t be a flat drumhead, of course, unless you chose to cut the edges off straight). Now, if you lay out coordinates (x, y) on the bottom of the box, the height V(x, y) of the sheet above the point (x, y) will satisfy Laplace’s equation.¹ (The one-dimensional analog would be a rubber band stretched between two points. Of course, it would form a straight line.)

FIGURE 3.2

Harmonic functions in two dimensions have the same properties we noted in one dimension:

1. The value of V at a point (x, y) is the average of those around the point. More precisely, if you draw a circle of any radius R about the point (x, y), the average value of V on the circle is equal to the value at the center:

V(x, y) = (1/2πR) ∮ V dl.

circle

(This, incidentally, suggests the method of relaxation, on which computer solutions to Laplace’s equation are based: Starting with specified values for V at the boundary, and reasonable guesses for V on a grid of interior points, the first pass reassigns to each point the average of its nearest neighbors. The second pass repeats the process, using the corrected values, and so on. After a few iterations, the numbers begin to settle down, so that subsequent passes produce negligible changes, and a numerical solution to Laplace’s equation, with the given boundary values, has been achieved.)²

2. V has no local maxima or minima; all extrema occur at the boundaries. (As before, this follows from (1).) Again, Laplace’s equation picks the most featureless function possible, consistent with the boundary conditions: no hills, no valleys, just the smoothest conceivable surface. For instance, if you put a ping-pong ball on the stretched rubber sheet of Fig. 3.2, it will roll over to one side and fall off—it will not find a “pocket” somewhere to settle into, for Laplace’s equation allows no such dents in the surface. From a geometrical point of view, just as a straight

¹ Actually, the equation satisfied by a rubber sheet is

∂/∂x [ (∂V/∂x) / √(1 + (∂V/∂x)² + (∂V/∂y)²) ] + ∂/∂y [ (∂V/∂y) / √(1 + (∂V/∂x)² + (∂V/∂y)²) ] = 0, where g = 1 + (∂V/∂x)² + (∂V/∂y)²;

it reduces (approximately) to Laplace’s equation as long as the surface does not deviate too radically from a plane.

² See, for example, E.M. Purcell, Electricity and Magnetism, 2nd ed. (New York: McGraw-Hill, 1985), problem 3.30.

直线是两点间最短距离，因此二维空间中的调和函数使给定边界线所张成的表面积最小。

3.1.4 三维空间中的拉普拉斯方程在三维空间中，我既不能为你提供一个显式解（如在一维情形那样），也无法给出一个启发性的物理例子来引导你的直觉（如在二维情形所做的那样）。然而，以下两个性质依然成立，这次我将概述其证明。³

## 1.  点r处的电势V是半径为R、以r为中心的球面S上V的平均值：

V(r) = (1/(4πR²)) ∮_sphere V da.

2.  因此，V不可能有局部极大值或极小值；V的极值必须出现在边界上。（因为如果V在r点有一个局部极大值，那么根据极大值的性质，我可以画一个以r为中心的球面，在其上所有V的值——因此其平均值——都将小于r点的值。）

证明。让我们从计算一个位于球外的点电荷q在半径为R的球面上产生的平均电势开始。我们将球心置于原点，并选择坐标使q位于z轴上（图3.3）。球面上一点的电势为 V = (1/(4πε₀)) q / r_z，其中 r_z² = z² + R² - 2zR cosθ。因此， V_ave = (1/(4πR²)) ∫∫ (1/(4πε₀)) q / [z² + R² - 2zR cosθ]^{1/2} R² sinθ dθ dφ = (q/(4πε₀)) (1/(2zR)) [ (z+R) - (z-R) ] = q/(4πε₀ z).

但这正是电荷q在球心处产生的电势！根据叠加原理，对于任何位于球外的电荷集合也是如此：它们在球面上的平均电势等于它们在球心处产生的总电势。∎

问题3.1 找出半径为R的球面上，由位于球内（其他条件同上，但z < R）的点电荷q产生的平均电势。（当然，在这种情况下，球内区域不满足拉普拉斯方程。）证明一般而言， V_ave = V_center + Q_enc/(4πε₀ R)， 其中V_center是球心处由所有外部电荷产生的电势，Q_enc是总包围电荷。

问题3.2 用一句话证明恩肖定理：一个带电粒子不能仅靠静电力保持在稳定平衡中。例如，考虑图3.4中固定的正方体排列的电荷。乍看之下，中心的正电荷似乎会悬浮在空中，因为它被每个角落排斥。这个“静电瓶”的漏洞在哪里？

[要将核聚变作为实用能源，必须将等离子体（带电粒子的汤）加热到惊人的温度——如此之高，以至于接触会蒸发任何普通的容器。恩肖定理表明，静电约束也是不可行的。幸运的是，可以使用磁场来约束高温等离子体。]

## 3.1 拉普拉斯方程

问题3.3 在球坐标系中，求解拉普拉斯方程，其中V仅依赖于r。在柱坐标系中，同样求解，假设V仅依赖于s。

问题3.4 (a) 证明球面上，由球外电荷产生的平均电场等于球心处的电场。

(b) 球内电荷产生的平均电场是多少？

3.1.5 边界条件与唯一性定理拉普拉斯方程本身并不足以确定V；还必须提供合适的边界条件。这引出了一个微妙的问题：什么是合适的边界条件，足以确定答案，但又不会强到产生矛盾？一维情形很简单，因为通解 V = mx + b 包含两个任意常数，因此我们需要两个边界条件。例如，我们可以指定函数在每个端点的值，或者指定函数在一个端点的值及其导数，或者一个端点的值和另一个端点的导数，等等。但我们不能只指定一个端点的值或导数——这信息不足。指定两个端点的导数也不行——如果两者相等则冗余，如果不等则矛盾。

在二维或三维空间中，我们面对的是一个偏微分方程，什么样的边界条件可接受就不那么明显了。例如，一张紧绷的橡胶薄膜的形状是否由其拉伸的框架唯一确定，或者像罐头盖一样，可以从一个稳定构型跳到另一个稳定构型？答案，正如你的直觉所暗示的，是V由其边界上的值唯一确定（罐头盖显然不服从拉普拉斯方程）。然而，其他类型的边界条件也可以使用（见问题3.5）。证明一组提出的边界条件是否充分，通常以唯一性定理的形式呈现。静电学中有许多这样的定理，都遵循相同的基本格式——我将向你展示两个最有用的。⁴

第一唯一性定理：在体积V内，拉普拉斯方程的解由边界曲面S上给定的V值唯一确定。

证明。在图3.5中，我画出了这样一个区域及其边界。（内部可能还有“岛屿”，只要其所有表面上的V值都给定；另外，外边界可以在无穷远处，那里V通常取为零。）假设存在两个满足拉普拉斯方程的解： ∇²V₁ = 0 和 ∇²V₂ = 0， 两者在边界表面上都取指定的值。我想证明它们必须相等。技巧是考察它们的差： V₃ ≡ V₁ - V₂。

这个差值也服从拉普拉斯方程， ∇²V₃ = ∇²V₁ - ∇²V₂ = 0， 并且在所有边界上取值为零（因为V₁和V₂在那里相等）。但拉普拉斯方程不允许存在局部极大值或极小值——所有极值都出现在边界上。因此V₃的极大值和极小值都为零。所以V₃必须处处为零，因此 V₁ = V₂。∎

示例3.1. 证明，如果一个空腔完全被导电材料包围，且腔内没有电荷，则腔内的电势是常数。

解腔壁上的电势是某个常数V（这是第2.5.1节中的第(iV)点），因此腔内的电势是一个满足拉普拉斯方程并在边界上取常数值V的函数。不难想到这个问题的一个解：V = V₀处处成立。唯一性定理保证这是唯一的解。（因此，空腔内的电场为零——这与我们在第2.5.2节中通过相当不同的方法得到的结果相同。）

唯一性定理赋予你想象的自由。你如何得到解并不重要；如果(a)它满足拉普拉斯方程并且(b)它在边界上取正确的值，那么它就是正确的。你将会在学习镜像法时看到这种论证的威力。

顺便说一句，很容易改进第一唯一性定理：我假设所讨论的区域内没有电荷，因此电势服从拉普拉斯方程，但我们也可以引入一些电荷（在这种情况下V服从泊松方程）。论证是相同的，只是这次 ∇²V₁ = -ρ/ε₀, ∇²V₂ = -ρ/ε₀， 所以 ∇²V₃ = ∇²V₁ - ∇²V₂ = -ρ/ε₀ + ρ/ε₀ = 0.

再次地，差值(V₃ ≡ V₁ - V₂)服从拉普拉斯方程并在所有边界上取值为零，所以V₃ = 0，从而V₁ = V₂。

推论：体积V内的电势由以下条件唯一确定：(a) 区域内的电荷密度，和 (b) 所有边界上的V值。

3.1.6 导体与第二唯一性定理为静电问题设定边界条件最简单的方法是在包围感兴趣区域的所有表面上指定V的值。这种情况在实践中经常出现：在实验室中，我们有连接到电池（维持给定电势）或连接到地（实验人员用语，指V=0）的导体。然而，还有其他情况，我们不知道边界上的电荷，而是知道各个导体表面上的电荷。假设我在第一个导体上放置电荷Q_a，在第二个上放置Q_b，等等——我不告诉你电荷如何分布在每个导体表面上，因为一旦放上去，它就会以一种我无法控制的方式移动。而且，为了完备起见，假设导体之间的区域存在指定的电荷密度ρ。电场现在是否唯一确定？或者是否存在多种方式让电荷在它们各自的导体上排列，每种方式都导致不同的场？

第二唯一性定理：在一个被导体包围的体积V内，包含指定的电荷密度ρ，如果每个导体上的总电荷给定，则电场被唯一确定（图3.6）。（整个区域可以被另一个导体包围，也可以是无界的。）

证明。假设存在两个满足问题条件的场。它们在导体之间的空间都服从微分形式的高斯定律： ∇·E₁ = ρ/ε₀, ∇·E₂ = ρ/ε₀.

两者也服从积分形式的高斯定律，应用于包围每个导体的高斯面： ∮ E₁·da = Q_i/ε₀, ∮ E₂·da = Q_i/ε₀.

（第i个导体表面）（第i个导体表面）

类似地，对于外边界（无论是在包围导体的内部还是在无穷远处）， ∮ E₁·da = Q_tot/ε₀, ∮ E₂·da = Q_tot/ε₀.

（外边界）（外边界）

像之前一样，我们考察差值 E₃ ≡ E₁ - E₂， 它在导体之间的区域服从 ∇·E₃ = 0 (3.7)

并且在每个边界表面上 ∮ E₃·da = 0 (3.8)。

现在我们必须利用最后一条信息：虽然我们不知道电荷Q如何分布在第i个导体上，但我们知道每个导体是一个等势体，因此V在每个导体表面上是一个常数（不一定相同）。（它不必为零，对于...

the potentials V and V may not be equal—all we know for sure is that both are constant over any given conductor.) Next comes a trick. Invoking product rule number 5 (inside front cover), we find that ∇·(V E ) = V (∇·E ) + E ·(∇V ) = −(E )².

3 3 3 3 3 3 3 Here I have used Eq. 3.7, and E = −∇V . Integrating this over V, and applying 3 3 the divergence theorem to the left side: ∫ ∇·(V E ) dτ = ∫ V E ·da = − ∫ (E )² dτ.

3 3 3 3 3

## V S V

The surface integral covers all boundaries of the region in question—the conductors and outer boundary. Now V is constant over each surface (if the outer boundary is infinity, V = 0 there), so it comes outside each integral, and what remains is zero, according to Eq. 3.8. Therefore, ∫ (E )² dτ = 0.

But this integrand is never negative; the only way the integral can vanish is if E = 0 everywhere. Consequently, E = E , and the theorem is proved.

3 1 2

This proof was not easy, and there is a real danger that the theorem itself will seem more plausible to you than the proof. In case you think the second uniqueness theorem is “obvious,” consider this example of Purcell’s: Figure 3.7 shows a simple electrostatic configuration, consisting of four conductors with charges ±Q, situated so that the plusses are near the minuses. It all looks very comfortable. Now, what happens if we join them in pairs, by tiny wires, as indicated in Fig. 3.8? Since the positive charges are very near negative charges (which is where they like to be) you might well guess that nothing will happen—the configuration looks stable.

Well, that sounds reasonable, but it’s wrong. The configuration in Fig. 3.8 is impossible. For there are now effectively two conductors, and the total charge on each is zero. One possible way to distribute zero charge over these conductors is to have no accumulation of charge anywhere, and hence zero field everywhere (Fig. 3.9). By the second uniqueness theorem, this must be the solution: The charge will flow down the tiny wires, canceling itself off.

Problem 3.5 Prove that the field is uniquely determined when the charge density ρ is given and either V or the normal derivative ∂V/∂n is specified on each boundary surface. Do not assume the boundaries are conductors, or that V is constant over any given surface.

Problem 3.6 A more elegant proof of the second uniqueness theorem uses Green’s identity (Prob. 1.61c), with T = U = V . Supply the details.

## 3.2 THE METHOD OF IMAGES

3.2.1 The Classic Image Problem Suppose a point charge q is held a distance d above an infinite grounded conducting plane (Fig. 3.10). Question: What is the potential in the region above the plane? It’s not just (1/4πε₀)q/r, for q will induce a certain amount of negative charge on the nearby surface of the conductor; the total potential is due in part to q directly, and in part to this induced charge. But how can we possibly calculate the potential, when we don’t know how much charge is induced or how it is distributed?

From a mathematical point of view, our problem is to solve Poisson’s equation in the region z > 0, with a single point charge q at (0,0,d), subject to the boundary conditions:

## 1. V = 0 when z = 0 (since the conducting plane is grounded), and

## 2. V → 0 far from the charge—that is, for x² + y² + z² >> d²

The first uniqueness theorem (actually, its corollary) guarantees that there is only one function that meets these requirements. If by trick or clever guess we can discover such a function, it’s got to be the answer.

Trick: Forget about the actual problem; we’re going to study a completely different situation. This new configuration consists of two point charges, +q at (0,0,d) and −q at (0,0,−d), and no conducting plane (Fig. 3.11). For this configuration, I can easily write down the potential: V(x,y,z) = (1/4πε₀) (q/√(x²+y²+(z−d)²) − q/√(x²+y²+(z+d)²)). (3.9)

(The denominators represent the distances from (x,y,z) to the charges +q and −q, respectively.) It follows that

## 1. V = 0 when z = 0,

## 2. V → 0 for x² + y² + z² >> d²,

and the only charge in the region z > 0 is the point charge +q at (0,0,d). But these are precisely the conditions of the original problem! Evidently the second configuration happens to produce exactly the same potential as the first configuration, in the “upper” region z ≥ 0. (The “lower” region, z < 0, is completely different, but who cares? The upper part is all we need.) Conclusion: The potential of a point charge above an infinite grounded conductor is given by Eq. 3.9, for z ≥ 0.

Notice the crucial role played by the uniqueness theorem in this argument: without it, no one would believe this solution, since it was obtained for a completely different charge distribution. But the uniqueness theorem certifies it: If it satisfies Poisson’s equation in the region of interest, and assumes the correct value at the boundaries, then it must be right.

3.2.2 Induced Surface Charge Now that we know the potential, it is a straightforward matter to compute the surface charge σ induced on the conductor. According to Eq. 2.49, σ = −ε₀ (∂V/∂n), where ∂V/∂n is the normal derivative of V at the surface. In this case the normal direction is the z direction, so σ = −ε₀ (∂V/∂z)|_{z=0}.

From Eq. 3.9, ∂V/∂z = (1/4πε₀) ( q(z−d)/[x²+y²+(z−d)²]^{3/2} + q(z+d)/[x²+y²+(z+d)²]^{3/2} ), so σ(x,y) = −qd / [2π(x²+y²+d²)^{3/2}]. (3.10)

As expected, the induced charge is negative (assuming q is positive) and greatest at x = y = 0.

While we’re at it, let’s compute the total induced charge: Q = ∫ σ da.

This integral, over the xy plane, could be done in Cartesian coordinates, with da = dx dy, but it’s a little easier to use polar coordinates (r, φ), with r² = x² + y² and da = r dr dφ. Then σ(r) = −qd / [2π(r²+d²)^{3/2}], and Q = ∫₀^{2π} ∫₀^∞ [−qd / 2π(r²+d²)^{3/2}] r dr dφ = −qd ∫₀^∞ [1/(r²+d²)^{3/2}] r dr = −q. (3.11)

The total charge induced on the plane is −q, as (with benefit of hindsight) you can perhaps convince yourself it had to be.

3.2.3 Force and Energy The charge q is attracted toward the plane, because of the negative induced charge. Let’s calculate the force of attraction. Since the potential in the vicinity of q is the same as in the analog problem (the one with +q and −q but no conductor), so also is the field and, therefore, the force: F = − (1/4πε₀) (q²/(2d)²) ẑ. (3.12)

5 For an entirely different derivation of this result, see Prob. 3.38.

Beware: It is easy to get carried away, and assume that everything is the same in the two problems. Energy, however, is not the same. With the two point charges and no conductor, Eq. 2.42 gives W = − (1/4πε₀) (q²/(2d)). (3.13)

But for a single charge and conducting plane, the energy is half of this: W = − (1/4πε₀) (q²/(4d)). (3.14)

Why half? Think of the energy stored in the fields (Eq. 2.45): W = (ε₀/2) ∫ E² dτ.

In the first case, both the upper region (z > 0) and the lower region (z < 0) contribute—and by symmetry they contribute equally. But in the second case, only the upper region contains a nonzero field, and hence the energy is half as great.⁶ Of course, one could also determine the energy by calculating the work required to bring q in from infinity. The force required (to oppose the electrical force in Eq. 3.12) is (1/4πε₀)(q²/4z²) ẑ, so W = ∫_{∞}^{0} F·dl = ∫_{∞}^{0} (1/4πε₀) (q²/4z²) dz = (1/4πε₀) (−q²/(4z))|_{∞}^{0} = − (1/4πε₀) (q²/(4d)).

As I move q toward the conductor, I do work only on q. It is true that induced charge is moving in over the conductor, but this costs me nothing, since the whole conductor is at potential zero. By contrast, if I simultaneously bring in two point charges (with no conductor), I do work on both of them, and the total is (again) twice as great.

3.2.4 Other Image Problems The method just described is not limited to a single point charge; any stationary charge distribution near a grounded conducting plane can be treated in the same way, by introducing its mirror image—hence the name method of images. (Remember that the image charges have the opposite sign; this is what guarantees that the xy plane will be at potential zero.) There are also some exotic problems that can be handled in similar fashion; the nicest of these is the following.

⁶ For a generalization of this result, see M. M. Taddei, T. N. C. Mendes, and C. Farina, Eur. J. Phys. 30, 965 (2009), and Prob. 3.41b.

Example 3.2. A point charge q is situated a distance a from the center of a grounded conducting sphere of radius R (Fig. 3.12). Find the potential outside the sphere.

Solution Examine the completely different configuration, consisting of the point charge q together with another point charge q' = − (R/a) q, (3.15)

placed a distance b = R²/a (3.16)

to the right of the center of the sphere (Fig. 3.13). No conductor, now—just the two point charges. The potential of this configuration is V(r) = (1/4πε₀) (q/r + q'/r'), (3.17)

where r and r' are the distances from q and q', respectively. Now, it happens (see Prob. 3.8) that this potential vanishes at all points on the sphere, and therefore fits the boundary conditions for our original problem, in the exterior region.⁷ Conclusion: Eq. 3.17 is the potential of a point charge near a grounded conducting sphere. (Notice that b is less than R, so the “image” charge q' is safely inside the sphere—you cannot put image charges in the region where you are calculating V; that would change ρ, and you’d be solving Poisson’s equation with the wrong source.) In particular, the force of attraction between the charge and the sphere is F = (1/4πε₀) (q q'/(a−b)²) = − (1/4πε₀) (q² R a / (a²− R²)²). (3.18)

⁷ This solution is due to William Thomson (later Lord Kelvin), who published it in 1848, when he was just 24. It was apparently inspired by a theorem of Apollonius (200 BC) that says the locus of points with a fixed ratio of distances from two given points is a sphere. See J. C. Maxwell, “Treatise on Electricity and Magnetism, Vol. I,” Dover, New York, p. 245. I thank Gabriel Karl for this interesting history.

The method of images is delightfully simple ... when it works. But it is as much an art as a science, for you must somehow think up just the right “auxiliary” configuration, and for most shapes this is forbiddingly complicated, if not impossible.

Problem 3.7 Find the force on the charge +q in Fig. 3.14. (The xy plane is a grounded conductor.)

plane is a grounded conductor.

3d +q d −2q x V = 0 FIGURE 3.14 Problem 3.8 (a) Using the law of cosines, show that Eq. 3.17 can be written as follows: (1/4πε) [ q/√(r²+a²−2ra cosθ) − (q/R)/√(1+(ra/R²)−2(ra/R²) cosθ) ]

(3.19)

where r and θ are the usual spherical polar coordinates, with the z axis along the line through q. In this form, it is obvious that V = 0 on the sphere, r = R.

(b) Find the induced surface charge on the sphere, as a function of θ. Integrate this to get the total induced charge. (What should it be?)

(c) Calculate the energy of this configuration.

Problem 3.9 In Ex. 3.2 we assumed that the conducting sphere was grounded (V = 0). But with the addition of a second image charge, the same basic model will handle the case of a sphere at any potential V (relative, of course, to infinity). What charge should you use, and where should you put it? Find the force of attraction between a point charge q and a neutral conducting sphere.

Problem 3.10 A uniform line charge λ is placed on an infinite straight wire, a distance d above a grounded conducting plane. (Let’s say the wire runs parallel to the x-axis and directly above it, and the conducting plane is the xy plane.)

(a) Find the potential in the region above the plane. [Hint: Refer to Prob. 2.52.]

(b) Find the charge density σ induced on the conducting plane.

Problem 3.11 Two semi-infinite grounded conducting planes meet at right angles. In the region between them, there is a point charge q, situated as shown in Fig. 3.15. Set up the image configuration, and calculate the potential in this region. What charges do you need, and where should they be located? What is the force on q? How much work did it take to bring q in from infinity? Suppose the planes met at some angle other than 90◦; would you still be able to solve the problem by the method of images? If not, for what particular angles does the method work?

y y b q R R −d +d x a x V = 0 −V +V FIGURE 3.15 FIGURE 3.16 Problem 3.12 Two long, straight copper pipes, each of radius R, are held a distance 2d apart. One is at potential V₀, the other at −V₀ (Fig. 3.16). Find the potential everywhere. [Hint: Exploit the result of Prob. 2.52.]

## 3.3 SEPARATION OF VARIABLES

In this section we shall attack Laplace’s equation directly, using the method of separation of variables, which is the physicist’s favorite tool for solving partial differential equations. The method is applicable in circumstances where the potential (V) or the charge density (σ) is specified on the boundaries of some region, and we are asked to find the potential in the interior. The basic strategy is very simple: We look for solutions that are products of functions, each of which depends on only one of the coordinates. The algebraic details, however, can be formidable, so I’m going to develop the method through a sequence of examples. We’ll start with Cartesian coordinates and then do spherical coordinates (I’ll leave the cylindrical case for you to tackle on your own, in Prob. 3.24).

3.3.1 Cartesian Coordinates Example 3.3. Two infinite grounded metal plates lie parallel to the xz plane, one at y = 0, the other at y = a (Fig. 3.17). The left end, at x = 0, is closed off with an infinite strip insulated from the two plates, and maintained at a specific potential V₀(y). Find the potential inside this “slot.” a V = 0 V₀(y)

V = 0 FIGURE 3.17 Solution The configuration is independent of z, so this is really a two-dimensional problem. In mathematical terms, we must solve Laplace’s equation, ∂²V/∂x² + ∂²V/∂y² = 0, (3.20)

subject to the boundary conditions (i) V = 0 when y = 0, (ii) V = 0 when y = a, (3.21)

(iii) V = V₀(y) when x = 0, (iv) V → 0 as x → ∞.

(The latter, although not explicitly stated in the problem, is necessary on physical grounds: as you get farther and farther away from the “hot” strip at x = 0, the potential should drop to zero.) Since the potential is specified on all boundaries, the answer is uniquely determined.

The first step is to look for solutions in the form of products: V(x, y) = X(x)Y(y). (3.22)

On the face of it, this is an absurd restriction—the overwhelming majority of solutions to Laplace’s equation do not have such a form. For example, V(x, y) = (5x + 6y) satisfies Eq. 3.20, but you can’t express it as the product of a function x times a function y. Obviously, we’re only going to get a tiny subset of all possible solutions by this means, and it would be a miracle if one of them happened to fit the boundary conditions of our problem ... But hang on, because the solutions we do get are very special, and it turns out that by pasting them together we can construct the general solution.

Anyway, putting Eq. 3.22 into Eq. 3.20, we obtain Y d²X/dx² + X d²Y/dy² = 0.

The next step is to “separate the variables” (that is, collect all the x-dependence into one term and all the y-dependence into another). Typically, this is accomplished by dividing through by V: (1/X) d²X/dx² + (1/Y) d²Y/dy² = 0. (3.23)

Here the first term depends only on x and the second only on y; in other words, we have an equation of the form f(x) + g(y) = 0. (3.24)

Now, there’s only one way this could possibly be true: f and g must both be constant. For what if f(x) changed, as you vary x—then if we held y fixed and fiddled with x, the sum f(x) + g(y) would change, in violation of Eq. 3.24, which says it’s always zero. (That’s a simple but somehow rather elusive argument; don’t accept it without due thought, because the whole method rides on it.)

It follows from Eq. 3.23, then, that (1/X) d²X/dx² = C₁ and (1/Y) d²Y/dy² = C₂, with C₁ + C₂ = 0. (3.25)

One of these constants is positive, the other negative (or perhaps both are zero). In general, one must investigate all the possibilities; however, in our particular problem we need C₁ positive and C₂ negative, for reasons that will appear in a moment. Thus d²X/dx² = k²X, d²Y/dy² = −k²Y. (3.26)

Notice what has happened: A partial differential equation (3.20) has been converted into two ordinary differential equations (3.26). The advantage of this is obvious—ordinary differential equations are a lot easier to solve. Indeed: X(x) = A eᵏˣ + B e⁻ᵏˣ, Y(y) = C sin(ky) + D cos(ky), so V(x, y) = (A eᵏˣ + B e⁻ᵏˣ)(C sin(ky) + D cos(ky)). (3.27)

This is the appropriate separable solution to Laplace’s equation; it remains to impose the boundary conditions, and see what they tell us about the constants. To begin at the end, condition (iv) requires that A equal zero.⁸ Absorbing B into C and D, we are left with V(x, y) = e⁻ᵏˣ(C sin(ky) + D cos(ky)).

Condition (i) now demands that D equal zero, so V(x, y) = C e⁻ᵏˣ sin(ky). (3.28)

Meanwhile (ii) yields sin(ka) = 0, from which it follows that k = nπ/a, (n = 1, 2, 3, ...). (3.29)

(At this point you can see why I chose C₁ positive and C₂ negative: If X were sinusoidal, we could never arrange for it to go to zero at infinity, and if Y were exponential we could not make it vanish at both 0 and a. Incidentally, n = 0 is no good, for in that case the potential vanishes everywhere. And we have already excluded negative n’s.)

That’s as far as we can go, using separable solutions, and unless V₀(y) just happens to have the form sin(nπy/a) for some integer n, we simply can’t fit the final boundary condition at x = 0. But now comes the crucial step that redeems the method: Separation of variables has given us an infinite family of solutions (one for each n), and whereas none of them by itself satisfies the final boundary condition, it is possible to combine them in a way that does. Laplace’s equation is linear, in the sense that if V₁, V₂, V₃, ... satisfy it, so does any linear combination, V = α₁V₁ + α₂V₂ + α₃V₃ + ..., where α₁, α₂, ... are arbitrary constants. For ∇²V = α₁∇²V₁ + α₂∇²V₂ + ... = 0α₁ + 0α₂ + ... = 0.

Exploiting this fact, we can patch together the separable solutions (Eq. 3.28) to construct a much more general solution: V(x, y) = Σ (from n=1 to ∞) Cₙ e⁻ⁿπx/a sin(nπy/a). (3.30)

This still satisfies three of the boundary conditions; the question is, can we (by astute choice of the coefficients Cₙ) fit the final boundary condition (iii)?

V(0, y) = Σ (from n=1 to ∞) Cₙ sin(nπy/a) = V₀(y). (3.31)

Well, you may recognize this sum—it’s a Fourier sine series. And Dirichlet’s theorem⁹ guarantees that virtually any function V₀(y)—it can even have a finite number of discontinuities—can be expanded in such a series.

But how do we actually determine the coefficients Cₙ, buried as they are in that infinite sum? The device for accomplishing this is so lovely it deserves a name—I call it Fourier’s trick, though it seems Euler had used essentially the same idea somewhat earlier. Here’s how it goes: Multiply Eq. 3.31 by sin(n’πy/a) (where n’ is a positive integer), and integrate from 0 to a: ∫₀ᵃ [ Σ (from n=1 to ∞) Cₙ sin(nπy/a) ] sin(n’πy/a) dy = ∫₀ᵃ V₀(y) sin(n’πy/a) dy. (3.32)

You can work out the integral on the left for yourself; the answer is ∫₀ᵃ sin(nπy/a) sin(n’πy/a) dy = { 0, if n’ ≠ n; a/2, if n’ = n. } (3.33)

Thus all the terms in the series drop out, save only the one where n = n’, and the left side of Eq. 3.32 reduces to (a/2)Cₙ’. Conclusion:¹⁰ Cₙ = (2/a) ∫₀ᵃ V₀(y) sin(nπy/a) dy. (3.34)

That does it: Eq. 3.30 is the solution, with coefficients given by Eq. 3.34.

As a concrete example, suppose the strip at x = 0 is a metal plate with constant potential V₀ (remember, it’s insulated from the grounded plates at y = 0 and y = a). Then Cₙ = (2V₀/a) ∫₀ᵃ sin(nπy/a) dy = (2V₀/(nπ)) (1 − cos(nπ)) = { 0, if n is even; 4V₀/(nπ), if n is odd. } (3.35)

Thus V(x, y) = (4V₀/π) Σ (n=1,3,5...) (1/n) e⁻ⁿπx/a sin(nπy/a). (3.36)

Figure 3.18 is a plot of this potential; Fig. 3.19 shows how the first few terms in the Fourier series combine to make a better and better approximation to the constant V₀: (a) is n = 1 only, (b) includes n up to 5, (c) is the sum of the first 10 terms, and (d) is the sum of the first 100 terms.

Incidentally, the infinite series in Eq. 3.36 can be summed explicitly (try your hand at it, if you like); the result is V(x, y) = (2V₀/π) tan⁻¹ [ sin(πy/a) / sinh(πx/a) ]. (3.37)

In this form, it is easy to check that Laplace’s equation is obeyed and the four boundary conditions (Eq. 3.21) are satisfied.

The success of this method hinged on two extraordinary properties of the separable solutions (Eqs. 3.28 and 3.29): completeness and orthogonality. A set of functions f_n(y) is said to be complete if any other function f(y) can be expressed as a linear combination of them: f(y) = ∑_{n=1}^∞ C_n f_n(y). (3.38)

The functions sin(nπy/a) are complete on the interval 0 ≤ y ≤ a. It was this fact, guaranteed by Dirichlet’s theorem, that assured us Eq. 3.31 could be satisfied, given the proper choice of the coefficients C_n. (The proof of completeness, for a particular set of functions, is an extremely difficult business, and I’m afraid physicists tend to assume it’s true and leave the checking to others.) A set of functions is orthogonal if the integral of the product of any two different members of the set is zero: ∫ f_n(y) f_{n'}(y) dy = 0 for n' ≠ n. (3.39)

The sine functions are orthogonal (Eq. 3.33); this is the property on which Fourier’s trick is based, allowing us to kill off all terms but one in the infinite series and thereby solve for the coefficients C_n. (Proof of orthogonality is generally quite simple, either by direct integration or by analysis of the differential equation from which the functions came.)

Example 3.4. Two infinitely-long grounded metal plates, again at y = 0 and y = a, are connected at x = ±b by metal strips maintained at a constant potential V_0, as shown in Fig. 3.20 (a thin layer of insulation at each corner prevents them from shorting out). Find the potential inside the resulting rectangular pipe.

Solution Once again, the configuration is independent of z. Our problem is to solve Laplace’s equation ∂²V/∂x² + ∂²V/∂y² = 0, subject to the boundary conditions (i) V = 0 when y = 0, (ii) V = 0 when y = a, (iii) V = V_0 when x = b, (iv) V = V_0 when x = −b.

The argument runs as before, up to Eq. 3.27: V(x,y) = (A e^{kx} + B e^{-kx})(C sin ky + D cos ky).

V=0 V=0 x −b b FIGURE 3.20

This time, however, we cannot set A = 0; the region in question does not extend to x = ∞, so e^{kx} is perfectly acceptable. On the other hand, the situation is symmetric with respect to x, so V(−x,y) = V(x,y), and it follows that A = B. Using e^{kx} + e^{-kx} = 2 cosh kx, and absorbing 2A into C and D, we have V(x,y) = cosh kx (C sin ky + D cos ky).

Boundary conditions (i) and (ii) require, as before, that D = 0 and k = nπ/a, so V(x,y) = C cosh(nπx/a) sin(nπy/a). (3.41)

Because V(x,y) is even in x, it will automatically meet condition (iv) if it fits (iii). It remains, therefore, to construct the general linear combination, V(x,y) = ∑_{n=1}^∞ C_n cosh(nπx/a) sin(nπy/a), and pick the coefficients C_n in such a way as to satisfy condition (iii): V(b,y) = ∑_{n=1}^∞ C_n cosh(nπb/a) sin(nπy/a) = V_0.

This is the same problem in Fourier analysis that we faced before; I quote the result from Eq. 3.35: C_n cosh(nπb/a) = ⎨ 0, if n is even ⎩ 4V_0/(nπ), if n is odd

Conclusion: The potential in this case is given by V(x,y) = (4V_0/π) ∑_{n=1,3,5...} (1/n) [cosh(nπx/a) / cosh(nπb/a)] sin(nπy/a). (3.42)

This function is shown in Fig. 3.21.

1.0 y/a 0.5 0.0 1.0 V/Vo 0.5 0.0 – 1.0 – 1.5 0.0 0.5 x/b 1.0 FIGURE 3.21

Example 3.5. An infinitely long rectangular metal pipe (sides a and b) is grounded, but one end, at x = 0, is maintained at a specified potential V_0(y,z), as indicated in Fig. 3.22. Find the potential inside the pipe.

V = 0 V(y, z)

b x z V = 0 FIGURE 3.22

Solution This is a genuinely three-dimensional problem, ∂²V/∂x² + ∂²V/∂y² + ∂²V/∂z² = 0, (3.43)

subject to the boundary conditions (i) V = 0 when y = 0, (ii) V = 0 when y = a, (iii) V = 0 when z = 0, (iv) V = 0 when z = b, (v) V → 0 as x → ∞, (vi) V = V_0(y,z) when x = 0.

As always, we look for solutions that are products: V(x,y,z) = X(x)Y(y)Z(z). (3.45)

Putting this into Eq. 3.43, and dividing by V, we find (1/X)(d²X/dx²) + (1/Y)(d²Y/dy²) + (1/Z)(d²Z/dz²) = 0.

It follows that (1/X)(d²X/dx²) = C_1, (1/Y)(d²Y/dy²) = C_2, (1/Z)(d²Z/dz²) = C_3, with C_1 + C_2 + C_3 = 0.

Our previous experience (Ex. 3.3) suggests that C_1 must be positive, C_2 and C_3 negative. Setting C_2 = −k² and C_3 = −l², we have C_1 = k² + l², and hence d²X/dx² = (k² + l²) X, d²Y/dy² = −k² Y, d²Z/dz² = −l² Z. (3.46)

Once again, separation of variables has turned a partial differential equation into ordinary differential equations. The solutions are X(x) = A e^{√(k²+l²)x} + B e^{-√(k²+l²)x}, Y(y) = C sin ky + D cos ky, Z(z) = E sin lz + F cos lz.

Boundary condition (v) implies A = 0, (i) gives D = 0, and (iii) yields F = 0, whereas (ii) and (iv) require that k = nπ/a and l = mπ/b, where n and m are positive integers. Combining the remaining constants, we are left with V(x,y,z) = C e^{-π √((n/a)²+(m/b)²)x} sin(nπy/a) sin(mπz/b). (3.47)

This solution meets all the boundary conditions except (vi). It contains two unspecified integers (n and m), and the most general linear combination is a double sum: V(x,y,z) = ∑_{n=1}^∞ ∑_{m=1}^∞ C_{n,m} e^{-π √((n/a)²+(m/b)²)x} sin(nπy/a) sin(mπz/b). (3.48)

We hope to fit the remaining boundary condition, V(0,y,z) = ∑_{n=1}^∞ ∑_{m=1}^∞ C_{n,m} sin(nπy/a) sin(mπz/b) = V_0(y,z), (3.49)

by appropriate choice of the coefficients C_{n,m}. To determine these constants, we multiply by sin(n'πy/a) sin(m'πz/b), where n' and m' are arbitrary positive integers, and integrate: ∑_{n=1}^∞ ∑_{m=1}^∞ C_{n,m} ∫_0^a sin(nπy/a) sin(n'πy/a) dy ∫_0^b sin(mπz/b) sin(m'πz/b) dz = ∫_0^a ∫_0^b V_0(y,z) sin(n'πy/a) sin(m'πz/b) dy dz.

Quoting Eq. 3.33, the left side is (ab/4) C_{n',m'}, so C_{n,m} = (4/(ab)) ∫_0^a ∫_0^b V_0(y,z) sin(nπy/a) sin(mπz/b) dy dz. (3.50)

Equation 3.48, with the coefficients given by Eq. 3.50, is the solution to our problem.

For instance, if the end of the tube is a conductor at constant potential V_0, C_{n,m} = (4V_0/(ab)) ∫_0^a sin(nπy/a) dy ∫_0^b sin(mπz/b) dz ⎨ 0, if n or m is even, = (3.51)

⎩ 16V_0/(π²nm), if n and m are odd.

In this case V(x,y,z) = (16V_0/π²) ∑_{n,m=1,3,5...} (1/(nm)) e^{-π √((n/a)²+(m/b)²)x} sin(nπy/a) sin(mπz/b). (3.52)

Notice that the successive terms decrease rapidly; a reasonable approximation would be obtained by keeping only the first few.

Problem 3.13 Find the potential in the infinite slot of Ex. 3.3 if the boundary at x = 0 consists of two metal strips: one, from y = 0 to y = a/2, is held at a constant potential V_0, and the other, from y = a/2 to y = a, is at potential −V_0.

Problem 3.14 For the infinite slot (Ex. 3.3), determine the charge density σ(y) on the strip at x = 0, assuming it is a conductor at constant potential V_0.

Problem 3.15 A rectangular pipe, running parallel to the z-axis (from −∞ to +∞), has three grounded metal sides, at y = 0, y = a, and x = 0. The fourth side, at x = b, is maintained at a specified potential V_0(y).

(a) Develop a general formula for the potential inside the pipe.

(b) Find the potential explicitly, for the case V_0(y) = V_0 (a constant).

## 3.3 SeparationofVariables

Problem 3.16 A cubical box (sides of length a) consists of five metal plates, which are welded together and grounded (Fig. 3.23). The top is made of a separate sheet of metal, insulated from the others, and held at a constant potential V_0. Find the potential inside the box. [What should the potential at the center (a/2,a/2,a/2) be? Check numerically that your formula is consistent with this value.]11 FIGURE 3.23

3.3.2 SphericalCoordinates

In the examples considered so far, Cartesian coordinates were clearly appropriate, since the boundaries were planes. For round objects, spherical coordinates are more natural. In the spherical system, Laplace’s equation reads: (1/r²) ∂/∂r (r² ∂V/∂r) + (1/(r² sinθ)) ∂/∂θ (sinθ ∂V/∂θ) + (1/(r² sin²θ)) ∂²V/∂φ² = 0. (3.53)

I shall assume the problem has azimuthal symmetry, so that V is independent of φ;12 in that case, Eq. 3.53 reduces to (1/r²) ∂/∂r (r² ∂V/∂r) + (1/(r² sinθ)) ∂/∂θ (sinθ ∂V/∂θ) = 0. (3.54)

As before, we look for solutions that are products: V(r,θ) = R(r) Θ(θ). (3.55)

Putting this into Eq. 3.54, and dividing by V, (1/(R r²)) d/dr (r² dR/dr) + (1/(Θ sinθ)) d/dθ (sinθ dΘ/dθ) = 0. (3.56)

Since the first term depends only on r, and the second only on θ, it follows that each must be a constant: (1/(R r²)) d/dr (r² dR/dr) = l(l+1), (1/(Θ sinθ)) d/dθ (sinθ dΘ/dθ) = −l(l+1). (3.57)

Here l(l+1) is just a fancy way of writing the separation constant—you’ll see in a minute why this is convenient.

As always, separation of variables has converted a partial differential equation (3.54) into ordinary differential equations (3.57). The radial equation, d/dr (r² dR/dr) = l(l+1) R, (3.58)

has the general solution R(r) = A r^l + B / r^{l+1}, (3.59)

as you can easily check; A and B are the two arbitrary constants to be expected in the solution of a second-order differential equation. But the angular equation, d/dθ (sinθ dΘ/dθ) = −l(l+1) sinθ Θ, (3.60)

is not so simple. The solutions are Legendre polynomials in the variable cosθ: Θ(θ) = P_l(cosθ). (3.61)

P_l(x) is most conveniently defined by the Rodrigues formula: P_l(x) ≡ (1/(2^l l!)) d^l/dx^l (x²−1)^l. (3.62)

The first few Legendre polynomials are listed in Table 3.1.

P_0(x) = 1 P_1(x) = x P_2(x) = (3x²−1)/2 P_3(x) = (5x³−3x)/2 P_4(x) = (35x⁴−30x²+3)/8 P_5(x) = (63x⁵−70x³+15x)/8 TABLE 3.1 LegendrePolynomials.

Notice that P_l(x) is (as the name suggests) an lth-order polynomial in x; it contains only even powers, if l is even, and odd powers, if l is odd. The factor in front (1/2^l l!) was chosen in order that P_l(1) = 1. (3.63)

The Rodrigues formula obviously works only for nonnegative integer values of l. Moreover, it provides us with only one solution. But Eq. 3.60 is second-order, and it should possess two independent solutions, for every value of l. It turns out that these “other solutions” blow up at θ = 0 and/or θ = π, and are therefore unacceptable on physical grounds.13 For instance, the second solution for l = 0 is Θ(θ) = ln tan(θ/2). (3.64)

You might want to check for yourself that this satisfies Eq. 3.60.

In the case of azimuthal symmetry, then, the most general separable solution to Laplace’s equation, consistent with minimal physical requirements, is V(r,θ) = ∑_{l=0}^∞ (A_l r^l + B_l / r^{l+1}) P_l(cosθ).

V(r,θ) = ∑_{l=0}^{∞} [A_l r^l + \frac{B_l}{r^{l+1}}] P_l(cosθ)  (3.65)

The following examples illustrate the power of this important result.

Example 3.6. The potential V_0(θ) is specified on the surface of a hollow sphere, of radius R. Find the potential inside the sphere.

Solution

In this case, B_l = 0 for all l — otherwise the potential would blow up at the origin. Thus,

V(r,θ) = ∑_{l=0}^{∞} A_l r^l P_l(cosθ)  (3.66)

In rare cases where the z axis is excluded, these “other solutions” do have to be considered.

At r = R this must match the specified function V_0(θ):

V(R,θ) = ∑_{l=0}^{∞} A_l R^l P_l(cosθ) = V_0(θ)  (3.67)

Can this equation be satisfied, for an appropriate choice of coefficients A_l? Yes: The Legendre polynomials (like the sines) constitute a complete set of functions, on the interval -1 ≤ x ≤ 1 (0 ≤ θ ≤ π). How do we determine the constants? Again, by Fourier’s trick, for the Legendre polynomials (like the sines) are orthogonal functions: 14

∫_{-1}^{1} P_l(x) P_{l'}(x) dx = ∫_{0}^{π} P_l(cosθ) P_{l'}(cosθ) sinθ dθ = {0, if l' ≠ l; 2/(2l+1), if l' = l}  (3.68)

Thus, multiplying Eq. 3.67 by P_{l'}(cosθ) sinθ and integrating, we have

A_{l'} R^{l'} \frac{2}{2l'+1} = ∫_{0}^{π} V_0(θ) P_{l'}(cosθ) sinθ dθ,

or

A_l = \frac{2l+1}{2 R^l} ∫_{0}^{π} V_0(θ) P_l(cosθ) sinθ dθ.  (3.69)

Equation 3.66 is the solution to our problem, with the coefficients given by Eq. 3.69.

It can be difficult to evaluate integrals of the form 3.69 analytically, and in practice it is often easier to solve Eq. 3.67 “by eyeball.” 15 For instance, suppose we are told that the potential on the sphere is

V_0(θ) = k sin^2(θ/2),  (3.70)

where k is a constant. Using the half-angle formula, we rewrite this as

V_0(θ) = \frac{k}{2} (1 - cosθ) = \frac{k}{2} [P_0(cosθ) - P_1(cosθ)].

Putting this into Eq. 3.67, we read off immediately that A_0 = k/2, A_1 = -k/(2R), and all other A_l’s vanish. Therefore,

V(r,θ) = \frac{k}{2} r^0 P_0(cosθ) - \frac{k}{2R} r^1 P_1(cosθ) = \frac{k}{2} \left(1 - \frac{r}{R} cosθ\right).  (3.71)

Example 3.7. The potential V_0(θ) is again specified on the surface of a sphere of radius R, but this time we are asked to find the potential outside, assuming there is no charge there.

Solution

In this case it’s the A_l’s that must be zero (or else V would not go to zero at ∞), so

V(r,θ) = ∑_{l=0}^{∞} \frac{B_l}{r^{l+1}} P_l(cosθ).  (3.72)

At the surface of the sphere, we require that

V(R,θ) = ∑_{l=0}^{∞} \frac{B_l}{R^{l+1}} P_l(cosθ) = V_0(θ).

Multiplying by P_{l'}(cosθ) sinθ and integrating — exploiting, again, the orthogonality relation 3.68 — we have

\frac{B_{l'}}{R^{l'+1}} \frac{2}{2l'+1} = ∫_{0}^{π} V_0(θ) P_{l'}(cosθ) sinθ dθ,

or

B_l = \frac{2l+1}{2} R^{l+1} ∫_{0}^{π} V_0(θ) P_l(cosθ) sinθ dθ.  (3.73)

Equation 3.72, with the coefficients given by Eq. 3.73, is the solution to our problem.

Example 3.8. An uncharged metal sphere of radius R is placed in an otherwise uniform electric field E = E_0 ẑ. The field will push positive charge to the “northern” surface of the sphere, and — symmetrically — negative charge to the “southern” surface (Fig. 3.24). This induced charge, in turn, distorts the field in the neighborhood of the sphere. Find the potential in the region outside the sphere.

Solution

The sphere is an equipotential — we may as well set it to zero. Then by symmetry the entire xy plane is at potential zero. This time, however, V does not go to zero at large z. In fact, far from the sphere the field is E_0 ẑ, and hence

V → -E_0 z + C.

Since V = 0 in the equatorial plane, the constant C must be zero. Accordingly, the boundary conditions for this problem are

(i) V = 0 when r = R, (ii) V → -E_0 r cosθ for r ≫ R.  (3.74)

We must fit these boundary conditions with a function of the form 3.65.

The first condition yields

A_l R^l + \frac{B_l}{R^{l+1}} = 0,

or

B_l = -A_l R^{2l+1},  (3.75)

so

V(r,θ) = ∑_{l=0}^{∞} A_l \left(r^l - \frac{R^{2l+1}}{r^{l+1}}\right) P_l(cosθ).

For r ≫ R, the second term in parentheses is negligible, and therefore condition (ii) requires that

∑_{l=0}^{∞} A_l r^l P_l(cosθ) = -E_0 r cosθ.

Evidently only one term is present: l = 1. In fact, since P_1(cosθ) = cosθ, we can read off immediately

A_1 = -E_0, all other A_l’s zero.

Conclusion:

V(r,θ) = -E_0 \left(r - \frac{R^3}{r^2}\right) cosθ.  (3.76)

The first term (−E_0 r cosθ) is due to the external field; the contribution attributable to the induced charge is

E_0 \frac{R^3}{r^2} cosθ.

If you want to know the induced charge density, it can be calculated in the usual way:

σ(θ) = -ε_0 \frac{\partial V}{\partial r} \bigg|_{r=R} = ε_0 E_0 \left(1 + 2 \frac{R^3}{R^3}\right) cosθ = 3 ε_0 E_0 cosθ.  (3.77)

As expected, it is positive in the “northern” hemisphere (0 ≤ θ ≤ π/2) and negative in the “southern” (π/2 ≤ θ ≤ π).

Example 3.9. A specified charge density σ_0(θ) is glued over the surface of a spherical shell of radius R. Find the resulting potential inside and outside the sphere.

Solution

You could, of course, do this by direct integration:

V = \frac{1}{4πε_0} ∫ \frac{σ}{r} da,

but separation of variables is often easier. For the interior region, we have

V(r,θ) = ∑_{l=0}^{∞} A_l r^l P_l(cosθ)  (r ≤ R)  (3.78)

(no B terms — they blow up at the origin); in the exterior region

V(r,θ) = ∑_{l=0}^{∞} \frac{B_l}{r^{l+1}} P_l(cosθ)  (r ≥ R)  (3.79)

(no A terms — they don’t go to zero at infinity). These two functions must be joined together by the appropriate boundary conditions at the surface itself. First, the potential is continuous at r = R (Eq. 2.34):

∑_{l=0}^{∞} A_l R^l P_l(cosθ) = ∑_{l=0}^{∞} \frac{B_l}{R^{l+1}} P_l(cosθ).  (3.80)

It follows that the coefficients of like Legendre polynomials are equal:

B_l = A_l R^{2l+1}.  (3.81)

(To prove that formally, multiply both sides of Eq. 3.80 by P_{l'}(cosθ) sinθ and integrate from 0 to π, using the orthogonality relation 3.68.) Second, the radial derivative of V suffers a discontinuity at the surface (Eq. 2.36):

\left(\frac{\partial V^{out}}{\partial r} - \frac{\partial V^{in}}{\partial r}\right) \bigg|_{r=R} = -\frac{1}{ε_0} σ_0(θ).  (3.82)

Thus

∑_{l=0}^{∞} \left[ -(l+1) \frac{B_l}{R^{l+2}} - l A_l R^{l-1} \right] P_l(cosθ) = -\frac{σ_0(θ)}{ε_0},

or, using Eq. 3.81,

∑_{l=0}^{∞} (2l+1) A_l R^{l-1} P_l(cosθ) = \frac{σ_0(θ)}{ε_0}.  (3.83)

From here, the coefficients can be determined using Fourier’s trick:

A_l = \frac{1}{2 ε_0 R^{l-1}} ∫_{0}^{π} σ_0(θ) P_l(cosθ) sinθ dθ.  (3.84)

Equations 3.78 and 3.79 constitute the solution to our problem, with the coefficients given by Eqs. 3.81 and 3.84.

For instance, if

σ_0(θ) = k cosθ = k P_1(cosθ),  (3.85)

for some constant k, then all the A_l’s are zero except for The charge induced on the pipe. [Use your result from Prob. 3.24.]

Problem 3.26 Charge density σ(φ) = a sin 5φ (where a is a constant) is glued over the surface of an infinite cylinder of radius R (Fig. 3.25). Find the potential inside and outside the cylinder. [Use your result from Prob. 3.24.]

FIGURE 3.25

## 3.4 Multipole Expansion

3.4.1 Approximate Potentials at Large Distances

If you are very far away from a localized charge distribution, it “looks” like a point charge, and the potential is—to good approximation—(1/4πε₀)Q/r, where Q is the total charge. We have often used this as a check on formulas for V. But what if Q is zero? You might reply that the potential is then approximately zero, and of course, you’re right, in a sense (indeed, the potential at large r is pretty small even if Q is not zero). But we’re looking for something a bit more informative than that.

Example 3.10. A (physical) electric dipole consists of two equal and opposite charges (±q) separated by a distance d. Find the approximate potential at points far from the dipole.

Solution

Let r₋ be the distance from –q and r₊ the distance from +q (Fig. 3.26). Then V(r) = (1/4πε₀)(q/r₊ – q/r₋), and (from the law of cosines) r²± = r² + (d/2)² ∓ r d cosθ = r²[1 ∓ (d/(2r)) cosθ + (d/(2r))²]. We’re interested in the regime r >> d, so the third term is negligible, and the binomial expansion yields (r/r±)⁻¹ ∼= (1 ∓ (d/(2r)) cosθ)^{-1/2} ∼= 1 ± (d/(2r)) cosθ. Thus 1/r₊ – 1/r₋ ∼= (d cosθ)/r², and hence V(r) ∼= (1/4πε₀)(q d cosθ)/r². (3.90)

The potential of a dipole goes like 1/r² at large r; as we might have anticipated, it falls off more rapidly than the potential of a point charge. If we put together a pair of equal and opposite dipoles to make a quadrupole, the potential goes like 1/r³; for back-to-back quadrupoles (an octopole), it goes like 1/r⁴; and so on. Figure 3.27 summarizes this hierarchy; for completeness I have included the electric monopole (point charge), whose potential, of course, goes like 1/r.

+ – – + + – + + – + – – + – + Monopole Dipole Quadrupole Octopole (V ~ 1/r) (V ~ 1/r²) (V ~ 1/r³) (V ~ 1/r⁴)

FIGURE 3.27

Example 3.10 pertains to a very special charge configuration. I propose now to develop a systematic expansion for the potential of any localized charge distribution, in powers of 1/r. Figure 3.28 defines the relevant variables; the potential at r is given by V(r) = (1/4πε₀) ∫ (1/|r – r'|) ρ(r') dτ'. (3.91) Using the law of cosines, |r – r'|² = r² + (r')² – 2 r r' cosα = r²[1 + (r'/r)² – 2 (r'/r) cosα], where α is the angle between r and r'. Thus |r – r'| = r √(1 + ε), (3.92) with ε ≡ (r'/r)[ (r'/r) – 2 cosα ].

For points well outside the charge distribution, ε is much less than 1, and this invites a binomial expansion: 1/√(1+ε) = (1+ε)⁻¹/² = 1 – (1/2)ε + (3/8)ε² – (5/16)ε³ + ... , (3.93) or, in terms of r, r', and α: 1/|r – r'| = (1/r) [1 – (1/2){ (r'/r)² – 2 (r'/r) cosα } + (3/8){ (r'/r)² – 2 (r'/r) cosα }² – (5/16){ (r'/r)² – 2 (r'/r) cosα }³ + ... ] = (1/r) [1 + (r'/r) cosα + (r'/r)² (3 cos²α – 1)/2 + (r'/r)³ (5 cos³α – 3 cosα)/2 + ... ].

In the last step, I have collected together like powers of (r'/r); surprisingly, their coefficients (the terms in parentheses) are Legendre polynomials! The remarkable result¹⁶ is that 1/|r – r'| = (1/r) Σ_{n=0}^∞ (r'/r)^n P_n(cosα). (3.94)

Substituting this back into Eq. 3.91, and noting that r is a constant, as far as the integration is concerned, I conclude that V(r) = (1/4πε₀) Σ_{n=0}^∞ (1/r^{n+1}) ∫ (r')^n P_n(cosα) ρ(r') dτ', (3.95) or, more explicitly, V(r) = (1/4πε₀) [ (1/r) ∫ ρ(r') dτ' + (1/r²) ∫ r' cosα ρ(r') dτ' + (1/r³) ∫ (r')² (cos²α – 1/2) ρ(r') dτ' + ... ]. (3.96)

¹⁶ This suggests a second way of defining the Legendre polynomials (the first being Rodrigues’ formula); 1/|r – r'| is called the generating function for Legendre polynomials.

This is the desired result—the multipole expansion of V in powers of 1/r. The first term (n = 0) is the monopole contribution (it goes like 1/r); the second (n = 1) is the dipole (it goes like 1/r²); the third is quadrupole; the fourth octopole; and so on. Remember that α is the angle between r and r', so the integrals depend on the direction to the field point. If you are interested in the potential along the z' axis (or—putting it the other way around—if you orient your r' coordinates so the z' axis lies along r), then α is the usual polar angle θ'.

As it stands, Eq. 3.95 is exact, but it is useful primarily as an approximation scheme: the lowest non-zero term in the expansion provides the approximate potential at large r, and the successive terms tell us how to improve the approximation if greater precision is required.

Problem 3.27 A sphere of radius R, centered at the origin, carries charge density ρ(r,θ) = k (R – 2r) sinθ / r², where k is a constant, and r, θ are the usual spherical coordinates. Find the approximate potential for points on the z axis, far from the sphere.

Problem 3.28 A circular ring in the xy plane (radius R, centered at the origin) carries a uniform line charge λ. Find the first three terms (n=0,1,2) in the multipole expansion for V(r,θ).

3.4.2 The Monopole and Dipole Terms

Ordinarily, the multipole expansion is dominated (at large r) by the monopole term: V_mon(r) = Q / (4πε₀ r), (3.97) where Q = ∫ ρ dτ is the total charge of the configuration. This is just what we expect for the approximate potential at large distances from the charge. For a point charge at the origin, V_mon is the exact potential, not merely a first approximation at large r; in this case, all the higher multipoles vanish.

If the total charge is zero, the dominant term in the potential will be the dipole (unless, of course, it also vanishes): V_dip(r) = (1/4πε₀) (1/r²) ∫ r' cosα ρ(r') dτ'. Since α is the angle between r' and r (Fig. 3.28), r' cosα = r̂ · r', and the dipole potential can be written more succinctly: V_dip(r) = (1/4πε₀) (1/r²) r̂ · ∫ r' ρ(r') dτ'. This integral (which does not depend on r) is called the dipole moment of the distribution: p ≡ ∫ r' ρ(r') dτ', (3.98) and the dipole contribution to the potential simplifies to V_dip(r) = (1/4πε₀) (p · r̂)/r². (3.99)

The dipole moment is determined by the geometry (size, shape, and density) of the charge distribution. Equation 3.98 translates in the usual way (Sect. 2.1.4) for point, line, and surface charges. Thus, the dipole moment of a collection of point charges is p = Σ_{i=1}^n q_i r'_i. (3.100) For a physical dipole (equal and opposite charges, ±q), p = q r'_+ – q r'_– = q (r'_+ – r'_–) = q d, (3.101) where d is the vector from the negative charge to the positive one (Fig. 3.29).

Is this consistent with what we got in Ex. 3.10? Yes: If you put Eq. 3.101 into Eq. 3.99, you recover Eq. 3.90. Notice, however, that this is only the approximate potential of the physical dipole—evidently there are higher multipole contributions. Of course, as you go farther and farther away, V_dip becomes a better and better approximation, since the higher terms die off more rapidly with increasing r. By the same token, at a fixed r the dipole approximation improves as you shrink the separation d. To construct a perfect (point) dipole whose potential is given exactly by Eq. 3.99, you’d have to let d approach zero. Unfortunately, you then lose the dipole term too, unless you simultaneously arrange for q to go to infinity! A physical dipole becomes a pure dipole, then, in the rather artificial limit d → 0, q → ∞, with the product q d = p held fixed. When someone uses the word “dipole,” you can’t always tell whether they mean a physical dipole (with finite separation between the charges) or an ideal (point) dipole. If in doubt, assume that d is small enough (compared to r) that you can safely apply Eq. 3.99.

Dipole moments are vectors, and they add accordingly: if you have two dipoles, p₁ and p₂, the total dipole moment is p₁ + p₂. For instance, with four charges at the corners of a square, as shown in Fig. 3.30, the net dipole moment is zero. You can see this by combining the charges in pairs (vertically, ↓ + ↑ = 0, or horizontally, → + ← = 0) or by adding up the four contributions individually, using Eq. 3.100. This is a quadrupole, as I indicated earlier, and its potential is dominated by the quadrupole term in the multipole expansion.

Problem 3.29 Four particles (one of charge q, one of charge 3q, and two of charge –2q) are placed as shown in Fig. 3.31, each a distance a from the origin. Find a simple approximate formula for the potential, valid at points far from the origin. (Express your answer in spherical coordinates.)

3q a a –2q –2q y FIGURE 3.31

Problem 3.30 In Ex. 3.9, we derived the exact potential for a spherical shell of radius R, which carries a surface charge σ = k cosθ. (a) Calculate the dipole moment of this charge distribution. (b) Find the approximate potential, at points far from the sphere, and compare the exact answer (Eq. 3.87). What can you conclude about the higher multipoles?

Problem 3.31 For the dipole in Ex. 3.10, expand 1/r± to order (d/r)³, and use this to determine the quadrupole and octopole terms in the potential.

3.4.3 Origin of Coordinates in Multipole Expansions

I mentioned earlier that a point charge at the origin constitutes a “pure” monopole. If it is not at the origin, it’s no longer a pure monopole. For instance, the charge in Fig. 3.32 has a dipole moment p = q d ŷ, and a corresponding dipole term in its potential. The monopole potential (1/4πε₀) q/r is not quite correct for this configuration; rather, the exact potential is (1/4πε₀) q/r'. The multipole expansion is, remember, a series in inverse powers of r (the distance to the origin), and when we expand 1/r', we get all powers, not just the first.

So moving the origin (or, what amounts to the same thing, moving the charge) can radically alter a multipole expansion. The monopole moment Q does not change, since the total charge is obviously independent of the coordinate system. (In Fig. 3.32, the monopole term is (1/4πε₀) Q/r, regardless of the origin.) But the dipole moment does change. For the charge in Fig. 3.32, if the origin is at O, there is a dipole moment p = q d ŷ. If we shift the origin to O', the dipole moment becomes p' = q d ŷ – Q R̂. In general, the dipole moment depends on the choice of origin, unless the total charge Q is zero.

ole term was unaffected when we moved q away from the origin—it’s just that it was no longer the whole story: a dipole term—and for that matter all higher poles—appeared as well.) Ordinarily, the dipole moment does change when you shift the origin, but there is an important exception: If the total charge is zero, then the dipole moment is independent of the choice of origin.

For suppose we displace the origin by an amount a (Fig. 3.33). The new dipole moment is then p' = ∫ r' ρ(r') dτ' = ∫ (r' - a) ρ(r') dτ' = ∫ r' ρ(r') dτ' - a ∫ ρ(r') dτ' = p - Qa.

In particular, if Q = 0, then p' = p. So if someone asks for the dipole moment in Fig. 3.34(a), you can answer with confidence “qd,” but if you’re asked for the dipole moment in Fig. 3.34(b), the appropriate response would be “With respect to what origin?”

Problem 3.32 Two point charges, 3q and −q, are separated by a distance a. For each of the arrangements in Fig. 3.35, find (i) the monopole moment, (ii) the dipole moment, and (iii) the approximate potential (in spherical coordinates) at large r (include both the monopole and dipole contributions).

3.4.4 The Electric Field of a Dipole

So far we have worked only with potentials. Now I would like to calculate the electric field of a (perfect) dipole. If we choose coordinates so that p is at the origin and points in the z direction (Fig. 3.36), then the potential at r, θ is (Eq. 3.99): V_dip(r, θ) = (r̂·p)/(4πε₀ r²) = (p cosθ)/(4πε₀ r²).

To get the field, we take the negative gradient of V: E_r = -∂V/∂r = (2p cosθ)/(4πε₀ r³), E_θ = -(1/r) ∂V/∂θ = (p sinθ)/(4πε₀ r³), E_φ = -(1/(r sinθ)) ∂V/∂φ = 0.

Thus E_dip(r, θ) = (p/(4πε₀ r³)) (2 cosθ r̂ + sinθ θ̂).

This formula makes explicit reference to a particular coordinate system (spherical) and assumes a particular orientation for p (along z). It can be recast in a coordinate-free form, analogous to the potential in Eq. 3.99—see Prob. 3.36.

Notice that the dipole field falls off as the inverse cube of r; the monopole field (Q/(4πε₀ r²)) r̂ goes as the inverse square, of course. Quadrupole fields go like 1/r⁴, octopole like 1/r⁵, and so on. (This merely reflects the fact that monopole potentials fall off like 1/r, dipole like 1/r², quadrupole like 1/r³, and so on—the gradient introduces another factor of 1/r.)

Figure 3.37(a) shows the field lines of a “pure” dipole (Eq. 3.103). For comparison, I have also sketched the field lines for a “physical” dipole, in Fig. 3.37(b). Notice how similar the two pictures become if you blot out the central region; up close, however, they are entirely different. Only for points r ≫ d does Eq. 3.103 represent a valid approximation to the field of a physical dipole. As I mentioned earlier, this régime can be reached either by going to larger r or by squeezing the charges very close together.

Problem 3.33 A “pure” dipole p is situated at the origin, pointing in the z direction.

(a) What is the force on a point charge q at (a, 0, 0) (Cartesian coordinates)?

(b) What is the force on q at (0, 0, a)?

(c) How much work does it take to move q from (a, 0, 0) to (0, 0, a)?

Problem 3.34 Three point charges are located as shown in Fig. 3.38, each a distance a from the origin. Find the approximate electric field at points far from the origin. Express your answer in spherical coordinates, and include the two lowest orders in the multipole expansion.

Problem 3.35 A solid sphere, radius R, is centered at the origin. The “northern” hemisphere carries a uniform charge density ρ₀, and the “southern” hemisphere a uniform charge density −ρ₀. Find the approximate field E(r, θ) for points far from the sphere (r ≫ R).

• Problem 3.36 Show that the electric field of a (perfect) dipole (Eq. 3.103) can be written in the coordinate-free form E_dip(r) = (1/(4πε₀ r³)) [3(p·r̂)r̂ - p].

More Problems on Chapter 3

Problem 3.37 In Section 3.1.4, I proved that the electrostatic potential at any point P in a charge-free region is equal to its average value over any spherical surface (radius R) centered at P. Here’s an alternative argument that does not rely on Coulomb’s law, only on Laplace’s equation. We might as well set the origin at P. Let V_ave(R) be the average; first show that dV_ave/dR = (1/(4πR²)) ∫ ∇V · da (note that the R² in da cancels the 1/R² out front, so the only dependence on R is in V itself). Now use the divergence theorem, and conclude that if V satisfies Laplace’s equation, then V_ave(R) = V_ave(0) = V(P), for all R.

Problem 3.38 Here’s an alternative derivation of Eq. 3.10 (the surface charge density induced on a grounded conducting plane by a point charge q a distance d above the plane). This approach (which generalizes to many other problems) does not rely on the method of images. The total field is due in part to q, and in part to the induced surface charge. Write down the z components of these fields—in terms of q and the as-yet-unknown σ(x, y)—just below the surface. The sum must be zero, of course, because this is inside a conductor. Use that to determine σ.

Problem 3.39 Two infinite parallel grounded conducting planes are held a distance a apart. A point charge q is placed in the region between them, a distance x from one plate. Find the force on q. Check that your answer is correct for the special cases a → ∞ and x = a/2.

Problem 3.40 Two long straight wires, carrying opposite uniform line charges ±λ, are situated on either side of a long conducting cylinder (Fig. 3.39). The cylinder (which carries no net charge) has radius R, and the wires are a distance a from the axis. Find the potential.

Problem 3.41 Buckminsterfullerine is a molecule of 60 carbon atoms arranged like the stitching on a soccer ball. It may be approximated as a conducting spherical shell of radius R = 3.5 Å. A nearby electron would be attracted, according to Prob. 3.9, so it is not surprising that the ion C₆₀⁻ exists. (Imagine that the electron—on average—smears itself out uniformly over the surface.) But how about a second electron? At large distances it would be repelled by the ion, obviously, but at a certain distance r (from the center), the net force is zero, and closer than this it would be attracted. So an electron with enough energy to get in that close should bind.

(a) Find r, in Å. [You’ll have to do it numerically.]

(b) How much energy (in electron volts) would it take to push an electron in (from infinity) to the point r?

[Incidentally, the C₆₀²⁻ ion has been observed.]

Problem 3.42 You can use the superposition principle to combine solutions obtained by separation of variables. For example, in Prob. 3.16 you found the potential inside a cubical box, if five faces are grounded and the sixth is at a constant potential V₀; by a six-fold superposition of the result, you could obtain the potential inside a cube with the faces maintained at specified constant voltages V₁, V₂, ...V₆. In this way, using Ex. 3.4 and Prob. 3.15, find the potential inside a rectangular pipe with two facing sides (x = ±b) at potential V₀, a third (y = a) at V₀, and the last (at y = 0) grounded.

Problem 3.43 A conducting sphere of radius a, at potential V₀, is surrounded by a thin concentric spherical shell of radius b, over which someone has glued a surface charge σ(θ) = k cosθ, where k is a constant and θ is the usual spherical coordinate.

(a) Find the potential in each region: (i) r > b, and (ii) a < r < b.

(b) Find the induced surface charge σ(θ) on the conductor.

(c) What is the total charge of this system? Check that your answer is consistent with the behavior of V at large r.

Problem 3.44 A charge +Q is distributed uniformly along the z axis from z = −a to z = +a. Show that the electric potential at a point r is given by V(r, θ) = (Q/(4πε₀ r)) [1 + (2/3)(a/r)² P₂(cosθ) + (4/5)(a/r)⁴ P₄(cosθ) + ... ], for r > a.

Problem 3.45 A long cylindrical shell of radius R carries a uniform surface charge σ₀ on the upper half and an opposite charge −σ₀ on the lower half (Fig. 3.40). Find the electric potential inside and outside the cylinder.

Problem 3.46 A thin insulating rod, running from z = −a to z = +a, carries the indicated line charges. In each case, find the leading term in the multipole expansion of the potential: (a) λ = k cos(πz/2a), (b) λ = k sin(πz/a), (c) λ = k cos(πz/a), where k is a constant.

• Problem 3.47 Show that the average field inside a sphere of radius R, due to all the charge within the sphere, is E_ave = -p/(4πε₀ R³), where p is the total dipole moment. There are several ways to prove this delightfully simple result. Here’s one method: (a) Show that the average field due to a single charge q at point r inside the sphere is the same as the field at r due to a uniformly charged sphere with ρ = -q/(4πR³/3), namely ∫ (4π/(4πR³/3)) r̂ dτ', where r is the vector from r to dτ'.

(b) The latter can be found from Gauss’s law (see Prob. 2.12). Express the answer in terms of the dipole moment of q.

(c) Use the superposition principle to generalize to an arbitrary charge distribution.

(d) While you’re at it, show that the average field over the volume of a sphere, due to all the charges outside, is the same as the field they produce at the center.

Problem 3.48 (a) Using Eq. 3.103, calculate the average electric field of a dipole, over a spherical volume of radius R, centered at the origin. Do the angular integrals first. [Note: You must express r̂ and θ̂ in terms of x̂, ŷ, and ẑ (see back cover) before integrating. If you don’t understand why, reread the discussion in Sect. 1.4.1.]

Compare your answer with the general theorem (Eq. 3.105). The discrepancy here is related to the fact that the field of a dipole blows up at r = 0. The angular integral is zero, but the radial integral is infinite, so we really don’t know what to make of it.

key of the answer. To resolve this dilemma, let's say that Eq. 3.103 applies outside a tiny sphere of radius ε—its contribution to E is then unambiguously zero, and the whole answer has to come from the field inside the ε-sphere.

(b) What must the field inside the ε-sphere be, in order for the general theorem (Eq. 3.105) to hold? [Hint: since ε is arbitrarily small, we're talking about something that is infinite at r = 0 and whose integral over an infinitesimal volume is finite.] [Answer: −(p/3ε₀)δ³(r)]

Evidently, the true field of a dipole is E_dip(r) = (1/(4πε₀)) [3(p·r̂)r̂ − p] − p/(3ε₀) δ³(r).  (3.106)

²² Another method exploits the result of Prob. 3.4. See B.Y.-K. Hu, Eur. J. Phys. 30, L29 (2009).

You may wonder how we missed the delta-function term²³ when we calculated the field back in Sect. 3.4.4. The answer is that the differentiation leading to Eq. 3.103 is valid except at r = 0, but we should have known (from our experience in Sect. 1.5.1) that the point r = 0 would be problematic.²⁴

Problem 3.49 In Ex. 3.9, we obtained the potential of a spherical shell with surface charge σ(θ) = k cos θ. In Prob. 3.30, you found that the field is pure dipole outside; it's uniform inside (Eq. 3.86). Show that the limit R → 0 reproduces the delta-function term in Eq. 3.106.

Problem 3.50 (a) Suppose a charge distribution ρ₁(r) produces a potential V₁(r), and some other charge distribution ρ₂(r) produces a potential V₂(r). [The two situations may have nothing in common, for all I care—perhaps number 1 is a uniformly charged sphere and number 2 is a parallel-plate capacitor. Please understand that ρ₁ and ρ₂ are not present at the same time; we are talking about two different problems, one in which only ρ₁ is present, and another in which only ρ₂ is present.] Prove Green's reciprocity theorem:²⁵

∫ ρ₁ V₂ dτ = ∫ ρ₂ V₁ dτ (all space)          (all space)

[Hint: Evaluate ∫ E₁·E₂ dτ two ways, first writing E₁ = −∇V₁ and using integration by parts to transfer the derivative to E₂, then writing E₂ = −∇V₂ and transferring the derivative to E₁.]

(b) Suppose now that you have two separated conductors (Fig. 3.41). If you charge up conductor a by amount Q (leaving b uncharged), the resulting potential of b is, say, V_ab. On the other hand, if you put that same charge Q on conductor b (leaving a uncharged), the potential of a would be V_ba. Use Green's reciprocity theorem to show that V_ab = V_ba (an astonishing result, since we assumed nothing about the shapes or placement of the conductors).

[Figure 3.41: Two conductors a and b, with charge Q and potentials indicated.]

²³ There are other ways of getting the delta-function term in the field of a dipole—my own favorite is Prob. 3.49. Note that unless you are right on top of the dipole, Eq. 3.104 is perfectly adequate.

²⁴ See C.P. Frahm, Am. J. Phys. 51, 826 (1983). For applications, see D.J. Griffiths, Am. J. Phys. 50, 698 (1982). There are other (perhaps preferable) ways of expressing the contact (delta-function) term in Eq. 3.106; see A. Gsponer, Eur. J. Phys. 28, 267 (2007), J. Franklin, Am. J. Phys. 78, 1225 (2010), and V. Hnizdo, Eur. J. Phys. 32, 287 (2011).

²⁵ For interesting commentary, see B.Y.-K. Hu, Am. J. Phys. 69, 1280 (2001).

Problem 3.51 Use Green's reciprocity theorem (Prob. 3.50) to solve the following two problems. [Hint: for distribution 1, use the actual situation; for distribution 2, remove q, and set one of the conductors at potential V₀.]

(a) Both plates of a parallel-plate capacitor are grounded, and a point charge q is placed between them at a distance x from plate 1. The plate separation is d. Find the induced charge on each plate. [Answer: Q₁ = q(x/d − 1); Q₂ = −qx/d]

(b) Two concentric spherical conducting shells (radii a and b) are grounded, and a point charge q is placed between them (at radius r). Find the induced charge on each sphere.

Problem 3.52 (a) Show that the quadrupole term in the multipole expansion can be written V_quad(r) = (1/(4πε₀)) Σ_{i,j} r̂_i r̂_j Q_{ij} / r³ (in the notation of Eq. 1.31), where Q_{ij} ≡ ∫ [3r'_i r'_j − (r')² δ_{ij}] ρ(r') dτ'.

Here δ_{ij} = 1 if i = j = 0 if i ≠ j is the Kronecker delta, and Q_{ij} is the quadrupole moment of the charge distribution. Notice the hierarchy: V_mon = Q / (4πε₀ r); V_dip = Σ_i r̂_i p_i / (4πε₀ r²); V_quad = Σ_{i,j} r̂_i r̂_j Q_{ij} / (4πε₀ r³); ...

The monopole moment (Q) is a scalar, the dipole moment (p) is a vector, the quadrupole moment (Q_{ij}) is a second-rank tensor, and so on.

(b) Find all nine components of Q_{ij} for the configuration in Fig. 3.30 (assume the square has side a and lies in the xy plane, centered at the origin).

(c) Show that the quadrupole moment is independent of origin if the monopole and dipole moments both vanish. (This works all the way up the hierarchy—the lowest non-zero multipole moment is always independent of origin.)

(d) How would you define the octopole moment? Express the octopole term in the multipole expansion in terms of the octopole moment.

Problem 3.53 In Ex. 3.8 we determined the electric field outside a spherical conductor (radius R) placed in a uniform external field E₀. Solve the problem now using the method of images, and check that your answer agrees with Eq. 3.76. [Hint: Use Ex. 3.2, but put another charge, −q, diametrically opposite q. Let a → ∞, with (1/4πε₀)(2q/a²) = −E₀ held constant.]

! Problem 3.54 For the infinite rectangular pipe in Ex. 3.4, suppose the potential on the bottom (y = 0) and the two sides (x = ±b) is zero, but the potential on the top (y = a) is a nonzero constant V₀. Find the potential inside the pipe. [Note: This is a rotated version of Prob. 3.15(b), but set it up as in Ex. 3.4, using sinusoidal functions in y and hyperbolic sin x. It is an unusual case in which k = 0 must be included. Begin by finding the general solution to Eq. 3.26 when k = 0.]²⁶

Answer: V₀ y/a + (2V₀/π) Σ_{n=1}^∞ (−1)ⁿ cosh(nπx/a) sin(nπy/a) / (n cosh(nπb/a)).

Alternatively, using sinusoidal functions of x and hyperbolic sin y, −(2V₀/π) Σ_{n=1}^∞ (−1)ⁿ sinh(α_n y) cos(α_n x) / (α_n sinh(α_n a)), where α_n ≡ (2n−1)π/(2b).

! Problem 3.55 (a) A long metal pipe of square cross-section (side a) is grounded on three sides, while the fourth (which is insulated from the rest) is maintained at constant potential V₀. Find the net charge per unit length on the side opposite to V₀. [Hint: Use your answer to Prob. 3.15 or Prob. 3.54.]

(b) A long metal pipe of circular cross-section (radius R) is divided (lengthwise) into four equal sections, three of them grounded and the fourth maintained at constant potential V₀. Find the net charge per unit length on the section opposite to V₀. [Answer to both (a) and (b): λ = −(ε₀ V₀ / π) ln 2]²⁷

Problem 3.56 An ideal electric dipole is situated at the origin, and points in the z direction, as in Fig. 3.36. An electric charge is released from rest at a point in the xy plane. Show that it swings back and forth in a semi-circular arc, as though it were a pendulum supported at the origin.²⁸

Problem 3.57 A stationary electric dipole p = p ẑ is situated at the origin. A positive point charge q (mass m) executes circular motion (radius s) at constant speed in the field of the dipole. Characterize the plane of the orbit. Find the speed, angular momentum, and total energy of the charge.²⁹ Answer: L = √(qpm/3ε₀)

Problem 3.58 Find the charge density σ(θ) on the surface of a sphere (radius R) that produces the same electric field, for points exterior to the sphere, as a charge q at the point a < R on the z axis.

Answer: (q/4πR²) (R² − a²)(R² + a² − 2Ra cos θ)⁻³/²  (for the surface charge density, see Eq. 2.24 for the field.)

²⁶ For further discussion, see S. Hassani, Am. J. Phys. 59, 470 (1991).

²⁷ These are special cases of the Thompson-Lampard theorem; see J.D. Jackson, Am. J. Phys. 67, 107 (1999).

²⁸ This charming result is due to R.S. Jones, Am. J. Phys. 63, 1042 (1995).

²⁹ G.P. Sastry, V. Srinivas, and A.V. Madhav, Eur. J. Phys. 17, 275 (1996).

## CHAPTER

Electric Fields in Matter

## 4.1 POLARIZATION

4.1.1 Dielectrics

In this chapter, we shall study electric fields in matter. Matter, of course, comes in many varieties—solids, liquids, gases, metals, woods, glasses—and these substances do not all respond in the same way to electrostatic fields. Nevertheless, most everyday objects belong (at least, in good approximation) to one of two large classes: conductors and insulators (or dielectrics). We have already talked about conductors; these are substances that contain an "unlimited" supply of charges that are free to move about through the material. In practice, what this ordinarily means is that many of the electrons (one or two per atom, in a typical metal) are not associated with any particular nucleus, but roam around at will. In dielectrics, by contrast, all charges are attached to specific atoms or molecules—they're on a tight leash, and all they can do is move a bit within the atom or molecule. Such microscopic displacements are not as dramatic as the wholesale rearrangement of charge in a conductor, but their cumulative effects account for the characteristic behavior of dielectric materials. There are actually two principal mechanisms by which electric fields can distort the charge distribution of a dielectric atom or molecule: stretching and rotating. In the next two sections I'll discuss these processes.

4.1.2 Induced Dipoles

What happens to a neutral atom when it is placed in an electric field E? Your first guess might well be: "Absolutely nothing—since the atom is not charged, the field has no effect on it." But that is incorrect. Although the atom as a whole is electrically neutral, there is a positively charged core (the nucleus) and a negatively charged electron cloud surrounding it. These two regions of charge within the atom are influenced by the field: the nucleus is pushed in the direction of the field, and the electrons the opposite way. In principle, if the field is large enough, it can pull the atom apart completely, "ionizing" it (the substance then becomes a conductor). With less extreme fields, however, an equilibrium is soon established, for if the center of the electron cloud does not coincide with the nucleus, these positive and negative charges attract one another, and that holds the atom together. The two opposing forces—E pulling the electrons and nucleus apart, their mutual attraction drawing them back together—reach a balance, leaving the atom polarized, with plus charge shifted slightly one way, and minus the other. The atom now has a tiny dipole moment p, which points in the same direction as E. Typically, this induced dipole moment is approximately proportional to the field (as long as the latter is not too strong): p = αE.  (4.1)

The constant of proportionality α is called atomic polarizability. Its values for various atoms (and a few molecules) are listed in Table 4.1. Note that α has the dimensions of volume (4πε₀ times a volume, in SI units).

depends on the detailed structure of the atom in question. Table 4.1 lists some experimentally determined atomic polarizabilities.

Example 4.1. A primitive model for an atom consists of a point nucleus (+q) surrounded by a uniformly charged spherical cloud (−q) of radius a (Fig. 4.1). Calculate the atomic polarizability of such an atom.

Solution: In the presence of an external field E, the nucleus will be shifted slightly to the right and the electron cloud to the left, as shown in Fig. 4.2. (Because the actual displacements involved are extremely small, as you’ll see in Prob. 4.1, it is reasonable to assume that the electron cloud retains its spherical shape.) Say that equilibrium occurs when the nucleus is displaced a distance d from the center of the sphere. At that point, the external field pushing the nucleus to the right exactly balances the internal field pulling it to the left: E = E_e, where E_e is the field produced by the electron cloud. Now the field at a distance d from the center of a uniformly charged sphere is E_e = (1/(4πε₀)) * (q d / a³) (Prob. 2.12). At equilibrium, then, E_e = (1/(4πε₀)) * (q d / a³), or p = q d = (4πε₀ a³) E. The atomic polarizability is therefore α = 4πε₀ a³ = 3ε₀ v, (4.2) where v is the volume of the atom. Although this atomic model is extremely crude, the result (Eq. 4.2) is not too bad—it’s accurate to within a factor of four or so for many simple atoms.

For molecules the situation is not quite so simple, because frequently they polarize more readily in some directions than in others. Carbon dioxide (Fig. 4.3), for instance, has a polarizability of 4.5×10⁻⁴⁰ C²·m/N when you apply the field along the axis of the molecule, but only 2×10⁻⁴⁰ for fields perpendicular to this direction. When the field is at some angle to the axis, you must resolve it into parallel and perpendicular components, and multiply each by the pertinent polarizability: p = α⊥ E⊥ + α∥ E∥. In this case, the induced dipole moment may not even be in the same direction as E. And CO₂ is relatively simple, as molecules go, since the atoms at least arrange themselves in a straight line; for a completely asymmetrical molecule, Eq. 4.1 is replaced by the most general linear relation between E and p: p_x = α_xx E_x + α_xy E_y + α_xz E_z, p_y = α_yx E_x + α_yy E_y + α_yz E_z, p_z = α_zx E_x + α_zy E_y + α_zz E_z. (4.3) The set of nine constants α_ij constitute the polarizability tensor for the molecule. Their values depend on the orientation of the axes you use, though it is always possible to choose “principal” axes such that all the off-diagonal terms (α_xy, α_zx, etc.) vanish, leaving just three non-zero polarizabilities: α_xx, α_yy, and α_zz.

Problem 4.1: A hydrogen atom (with the Bohr radius of half an angstrom) is situated between two metal plates 1 mm apart, which are connected to opposite terminals of a 500 V battery. What fraction of the atomic radius does the separation distance d amount to, roughly? Estimate the voltage you would need with this apparatus to ionize the atom. [Use the value of α in Table 4.1. Moral: The displacements we’re talking about are minute, even on an atomic scale.]

Problem 4.2: According to quantum mechanics, the electron cloud for a hydrogen atom in the ground state has a charge density ρ(r) = (q/πa³) e^{-2r/a}, where q is the charge of the electron and a is the Bohr radius. Find the atomic polarizability of such an atom. [Hint: First calculate the electric field of the electron cloud, E_e(r); then expand the exponential, assuming r ≪ a.]

Problem 4.3: According to Eq. 4.1, the induced dipole moment of an atom is proportional to the external field. This is a “rule of thumb,” not a fundamental law, and it is easy to concoct exceptions—in theory. Suppose, for example, the charge density of the electron cloud were proportional to the distance from the center, out to a radius R. To what power of E would p be proportional in that case? Find the condition on ρ(r) such that Eq. 4.1 will hold in the weak-field limit.

Problem 4.4: A point charge q is situated at a large distance r from a neutral atom of polarizability α. Find the force of attraction between them.

Alignment of Polar Molecules: The neutral atom discussed in Sect. 4.1.2 had no dipole moment to start with—p was induced by the applied field. Some molecules have built-in, permanent dipole moments. In the water molecule, for example, the electrons tend to cluster around the oxygen atom (Fig. 4.4), and since the molecule is bent at 105°, this leaves a negative charge at the vertex and a net positive charge on the opposite side. (The dipole moment of water is unusually large: 6.1×10⁻³⁰ C·m; in fact, this is what accounts for its effectiveness as a solvent.) What happens when such molecules (called polar molecules) are placed in an electric field?

If the field is uniform, the force on the positive end, F+ = qE, exactly cancels the force on the negative end, F− = −qE (Fig. 4.5). However, there will be a torque: N = (r+ × F+) + (r− × F−) = (d/2) × (qE) + (−d/2) × (−qE) = qd × E. Thus a dipole p = qd in a uniform field E experiences a torque N = p × E. (4.4) Notice that N is in such a direction as to line p up parallel to E; a polar molecule that is free to rotate will swing around until it points in the direction of the applied field.

If the field is nonuniform, so that F+ does not exactly balance F−, there will be a net force on the dipole, in addition to the torque.

That does it, in principle. But a little sleight-of-hand casts this integral into a much more illuminating form. Observing that ∇(1/r) = -r̂ / r², we have V = (1/4πε₀) ∫ P · ∇(1/r) dτ'.

Integrating by parts, using product rule number 5 (in the front cover), gives V = (1/4πε₀) [ ∫ ∇·(P/r) dτ' - ∫ (1/r) (∇·P) dτ' ], or, invoking the divergence theorem, V = (1/4πε₀) ∮ (P·n̂) da / r - (1/4πε₀) ∫ (∇·P) dτ' / r. (4.10)

The first term looks like the potential of a surface charge σ_b ≡ P·n̂ (4.11)

(where n̂ is the normal unit vector), while the second term looks like the potential of a volume charge ρ_b ≡ -∇·P. (4.12)

With these definitions, Eq. 4.10 becomes V(r) = (1/4πε₀) ∮ σ_b da / r + (1/4πε₀) ∫ ρ_b dτ' / r. (4.13)

What this means is that the potential (and hence also the field) of a polarized object is the same as that produced by a volume charge density ρ_b = -∇·P plus a surface charge density σ_b = P·n̂. Instead of integrating the contributions of all the infinitesimal dipoles, as in Eq. 4.9, we could first find those bound charges, and then calculate the fields they produce, in the same way we calculate the field of any other volume and surface charges (for example, using Gauss's law).

Example 4.2. Find the electric field produced by a uniformly polarized sphere of radius R.

Solution We may as well choose the z axis to coincide with the direction of polarization (Fig. 4.9). The volume bound charge density ρ_b is zero, since P is uniform, but σ_b = P·n̂ = P cosθ, where θ is the usual spherical coordinate. What we want, then, is the field produced by a charge density P cosθ plastered over the surface of a sphere. But we already computed the potential of such a configuration, in Ex. 3.9: V(r,θ) = (P/3ε₀) r cosθ, for r ≤ R, (P R³/3ε₀ r²) cosθ, for r ≥ R.

Since r cosθ = z, the field inside the sphere is uniform: E = -∇V = - (P/3ε₀) ẑ = -P / 3ε₀, for r < R. (4.14)

This remarkable result will be very useful in what follows. Outside the sphere the potential is identical to that of a perfect dipole at the origin, V = (1/4πε₀) p·r̂ / r², for r ≥ R, (4.15)

whose dipole moment is, not surprisingly, equal to the total dipole moment of the sphere: p = (4πR³/3) P. (4.16)

The field of the uniformly polarized sphere is shown in Fig. 4.10.

Problem 4.10 A sphere of radius R carries a polarization P(r) = k r, where k is a constant and r is the vector from the center.

(a) Calculate the bound charges σ_b and ρ_b.

(b) Find the field inside and outside the sphere.

Problem 4.11 A short cylinder, of radius a and length L, carries a "frozen-in" uniform polarization P, parallel to its axis. Find the bound charge, and sketch the electric field (i) for L >> a, (ii) for L << a, and (iii) for L ≈ a. [This is known as a bar electret; it is the electrical analog to a bar magnet. In practice, only very special materials—barium titanate is the most "familiar" example—will hold a permanent electric polarization. That's why you can't buy electrets at the toy store.]

Problem 4.12 Calculate the potential of a uniformly polarized sphere (Ex. 4.2) directly from Eq. 4.9.

4.2.2 Physical Interpretation of Bound Charges In the last section we found that the field of a polarized object is identical to the field that would be produced by a certain distribution of "bound charges," σ_b and ρ_b. But this conclusion emerged in the course of abstract manipulations on the integral in Eq. 4.9, and left us with no clue as to the physical meaning of these bound charges. Indeed, some authors give you the impression that bound charges are in some sense "fictitious"—mere bookkeeping devices used to facilitate the calculation of fields. Nothing could be further from the truth: ρ_b and σ_b represent perfectly genuine accumulations of charge. In this section I'll explain how polarization leads to these charge distributions.

The basic idea is very simple: Suppose we have a long string of dipoles, as shown in Fig. 4.11. Along the line, the head of one effectively cancels the tail of its neighbor, but at the ends there are two charges left over: plus at the right end and minus at the left. It is as if we had peeled off an electron at one end and carried it all the way down to the other end, though in fact no single electron made the whole trip—a lot of tiny displacements add up to one large one. We call the net charge at the ends a bound charge to remind ourselves that it cannot be removed; in a dielectric every electron is attached to a specific atom or molecule. But apart from that, bound charge is no different from any other kind.

To calculate the actual amount of bound charge resulting from a given polarization, examine a "tube" of dielectric parallel to P. The dipole moment of the tiny chunk shown in Fig. 4.12 is P(Ad), where A is the cross-sectional area of the tube and d is the length of the chunk. In terms of the charge (q) at the end, this same dipole moment can be written qd. The bound charge that piles up at the right end of the tube is therefore q = P A.

If the ends have been sliced off perpendicularly, the surface charge density is σ_b = q / A_end = P.

For an oblique cut (Fig. 4.13), the charge is still the same, but A = A_end cosθ, so σ_b = q / A_end = P cosθ = P·n̂.

The effect of the polarization, then, is to paint a bound charge σ_b = P·n̂ over the surface of the material. This is exactly what we found by more rigorous means in Sect. 4.2.1. But now we know where the bound charge comes from.

If the polarization is nonuniform, we get accumulations of bound charge within the material, as well as on the surface. A glance at Fig. 4.14 suggests that a diverging P results in a pileup of negative charge. Indeed, the net bound charge ρ_b dτ in a given volume is equal and opposite to the amount that has been pushed out through the surface. The latter (by the same reasoning we used before) is P·n̂ per unit area, so ∫ ρ_b dτ = - ∮ P·da = - ∫ (∇·P) dτ.

Since this is true for any volume, we have ρ_b = -∇·P, confirming, again, the more rigorous conclusion of Sect. 4.2.1.

Example 4.3. There is another way of analyzing the uniformly polarized sphere (Ex. 4.2), which nicely illustrates the idea of a bound charge. What we have, really, is two spheres of charge: a positive sphere and a negative sphere. Without polarization the two are superimposed and cancel completely. But when the material is uniformly polarized, all the plus charges move slightly upward (the z direction), and all the minus charges move slightly downward (Fig. 4.15). The two spheres no longer overlap perfectly: at the top there's a "cap" of leftover positive charge and at the bottom a cap of negative charge. This "leftover" charge is precisely the bound surface charge σ_b.

In Prob. 2.18, you calculated the field in the region of overlap between two uniformly charged spheres; the answer was E = - (1/4πε₀) q d / R³, where q is the total charge of the positive sphere, d is the vector from the negative center to the positive center, and R is the radius of the sphere. We can express this in terms of the polarization of the sphere, p = q d = (4πR³/3) P, as E = -P / 3ε₀.

Meanwhile, for points outside, it is as though all the charge on each sphere were concentrated at the respective center. We have, then, a dipole, with potential V = (1/4πε₀) p·r̂ / r².

(Remember that d is some small fraction of an atomic radius; Fig. 4.15 is grossly exaggerated.) These answers agree, of course, with the results of Ex. 4.2.

Problem 4.13 A very long cylinder, of radius a, carries a uniform polarization P perpendicular to its axis. Find the electric field inside the cylinder. Show that the field outside the cylinder can be expressed in the form E(s) = (a²/2ε₀ s²) [2(P·ŝ) ŝ - P].

[Careful: I said "uniform," not "radial"!]

Problem 4.14 When you polarize a neutral dielectric, the charge moves a bit, but the total remains zero. This fact should be reflected in the bound charges σ_b and ρ_b. Prove from Eqs. 4.11 and 4.12 that the total bound charge vanishes.

4.2.3 The Field Inside a Dielectric I have been sloppy about the distinction between "pure" dipoles and "physical" dipoles. In developing the theory of bound charges, I assumed we were working with the pure kind—indeed, I started with Eq. 4.8, the formula for the potential of a perfect dipole. And yet, an actual polarized dielectric consists of physical dipoles, albeit extremely tiny ones. What is more, I presumed to represent discrete molecular dipoles by a continuous density function P. How can I justify this method? Outside the dielectric there is no real problem: here we are far away from the molecules (r is many times greater than the separation distance between plus and minus charges), so the dipole potential dominates overwhelmingly and the detailed "graininess" of the source is blurred by distance. Inside the dielectric, however, we can hardly pretend to be far from all the dipoles, and the procedure I used in Sect. 4.2.1 is open to serious challenge.

In fact, when you stop to think about it, the electric field inside matter must be fantastically complicated, on the microscopic level. If you happen to be very near an electron, the field is gigantic, whereas a short distance away it may be small or may point in a totally different direction. Moreover, an instant later, as the atoms move about, the field will have altered entirely. This true microscopic field would be utterly impossible to calculate, nor would it be of much interest if you could. Just as, for macroscopic purposes, we regard water as a continuous fluid, ignoring its molecular structure, so also we can ignore the microscopic bumps and wrinkles in the electric field inside matter, and concentrate on the macroscopic field. This is defined as the average field over regions large enough to contain many thousands of atoms (so that the uninteresting microscopic fluctuations are smoothed over), and yet small enough to ensure that we do not wash out any significant large-scale variations in the field. (In practice, this means we must average over regions much smaller than the dimensions of the object itself.) Ordinarily, the macroscopic field is what people mean when they speak of "the" field inside matter.

It remains to show that the macroscopic field is what we actually obtain when we use the method

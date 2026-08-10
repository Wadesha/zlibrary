# Applied General Relativity Theory and Applications in Astronomy Celestial Mechanics and Metrology Michael H Soffel Wen Biao Han Z Library

> 来源文件：pre_Applied_General_Relativity_Theory_and_Applications_in_Astronomy_Celestial_Mechanics_and_Metrology_Michael_H_Soffel_Wen_Biao_Han_Z_Library.txt
> 字符数（约）：265121
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Astronomy and Astrophysics Library

Michael H. Soffel – Wen-Biao Han

Applied General Relativity Theory and Applications in Astronomy, Celestial Mechanics and Metrology

Michael H. Soffel Institute of planetary geodesy, Lohrmann-Observatory, Dresden, Germany

Wen-Biao Han Shanghai Astronomical Observatory, Chinese Academy of Sciences, Shanghai, China

ISSN 0941-7834 ISSN 2196-9698 (electronic)

Astronomy and Astrophysics Library ISBN 978-3-030-19672-1 ISBN 978-3-030-19673-8 (eBook)

https://doi.org/10.1007/978-3-030-19673-8 © Springer Nature Switzerland AG 2019

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

The publisher, the authors, and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, express or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Cover illustration: ‘Space-Time curvature’ (2019) by M. Soffel and W.-B. Han with the St. Marien (Rostock) astronomical clock overlaid (photograph by M.L. Preis).

This Springer imprint is published by the registered company Springer Nature Switzerland AG.

The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

Preface

At present, there is a vast number of textbooks on Einstein’s theory of gravity (general relativity, GR) that are available for different kinds of readers and at different levels of technical complexity. There is a series of classical treatments, e.g., Eddington (1922), Tolman (1934), Bergmann (1942), Weyl (1950), Pauli (1958), Fock (1959), Synge (1960), Adler et al. (1965), Fokker (1965), Rindler (1969), Carmeli et al. (1970), Landau and Lifshitz (1971), Weinberg (1972), Møller (1972), Misner et al. (1973), and Hawking and Ellis (1973), but also many more modern books, like Geroch (1978), Wald (1984), Schutz (1985), Woodhouse (2007) or Carroll (2013) to name just a few. In addition, there are the Living Reviews in Relativity, such as e.g. Will (2006) or Blanchet (2014), that can be downloaded from the web for free.

Many books deal with tests of GR; the standard reference is Will (1993, 2006), but only a few deal with specific applications, e.g. in the important field of metrology. In the field of ‘Applied General Relativity’ it is essentially the books by Soffel (1989) and Kopeikin et al. (2011) where the reader can learn how general relativistic effects enter such fields as the realization of time scales, practical clock synchronization, satellite- and lunar laser ranging or very long baseline interferometry. Now, the first of these books is completely obsolete, whereas the second one is not really a textbook, written in a homogeneous style where the reader should be able to understand the arguments step-by-step.

In some sense, this book presents an improvement, extension and actualization of my old Springer book (Soffel 1989). This is especially true with respect to the selection of subjects treated in this book: the main emphasis lies on relativity in astrometry, celestial mechanics and metrology, thus on certain aspects of applied science. We have borrowed heavily from that book; some parts that we think are still up to date were taken almost literally (we have also borrowed several parts from Soffel and Langhans 2013). This book is clearly not a textbook on all aspects of Einstein’s theory of gravity (‘general relativity’, GR). Though some aspects related with exact solutions of the Einstein field equations are treated, the physics of objects with strong gravitational fields, like black holes, neutron stars or white dwarfs or gravitational waves, will not be discussed here.

In another sense, this is a completely new book. After Soffel (1989) came out, both, the theoretical relativistic formalisms and the observational techniques, have drastically been improved so that large parts of Soffel (1989) became obsolete. A good example for theoretical improvements is the Brumberg-Kopeikin Damour-Soffel-Xu (BK-DSX) formalism for relativistic celestial mechanics. For the first time in history, a new formalism for treating the relativistic celestial mechanics of systems of N arbitrarily composed and shaped, weakly self-gravitating, rotating, deformable bodies was introduced. This formalism is aimed at yielding a complete description, at the first post-Newtonian approximation level, of (1) the global dynamics of such N-body systems (‘external problem’), (2) the local gravitational structure of each body (‘internal problem’), and (3) the way the external and the internal problems fit together (‘theory of reference systems’) (Damour et al. 1991; DSX-I). This BK-DSX formalism is based on the first post-Newtonian approximation of Einstein’s theory of gravity, and an extension to higher orders will be difficult. Nevertheless, it is sufficient for many applications at the present level of accuracies.

The multipolar post-Minkowskian (MPM) formalism that has been worked out by Blanchet, Damour and Iyer (see Blanchet 2014 for an overview) is another example for that. Though important papers on that subject date back to the second half of the 1980s, it has only been in recent years that the MPM formalism has been worked out completely. The MPM formalism is able to describe the gravitational field of weak-field sources inside of some compact region basically to all orders of GM/(c²R) in a single coordinate system and has been employed very successfully to the emission of gravitational waves from binary systems.

Also the character of the book is very different from Soffel (1989). For example, a lot of work has been spent on didactical aspects, like a large number of (partially solved) exercises have been included. The title of the book, Applied General Relativity (AGR), points to two aspects: applied science on the one side and the theoretical framework of GR on the other side. It is not difficult to realize that these two aspects usually are represented by two different expert groups. It is one goal of the book to illustrate to one of these groups the discipline of the other. The field of AGR has advanced to a multidisciplinary stage so that both groups should fertilize each other.

Chapter 2 deals with the language of relativity: differential geometry, in which the reasons for that will be discussed later. This treatment is fairly standard. For more details, the reader is referred to the standard literature (e.g. Beyer and Gostiaux 1988; Pressley 2010; Bär 2011; Kobayashi and Nomizu 2014).

Chapter 3 introduces Newtonian celestial mechanics. It starts with the Weak Equivalence Principle (universality of free-fall) and Newton’s theory of gravity. Of special interest is the exterior gravitational field of some matter distribution (body) and its description with multipole moments. Here, in addition to the usual spherical moments that are based upon an expansion of the exterior Newtonian potentials in terms of spherical harmonics, the expansion in terms of Cartesian symmetric and trace-free (STF) tensors is introduced. Whereas the spherical moments are very well known, e.g., for geodesists under the name of ‘potential coefficients’, this is still not the case for the STF moments. For experts in relativity, they play a crucial role, e.g. because Lorentz transformations usually are formulated in Cartesian coordinates. As was, e.g., nicely demonstrated by Hartmann et al. (1994) the use of STF moments can be employed very efficiently, like for the derivation of translational and rotational equations of motion in the N-body problem or for a representation of the tidal potential in Newtonian celestial mechanics. The Newtonian two-body problem of two mass monopoles moving under their mutual gravitational attractive forces is treated exhaustively since it serves as basis for a description of the relativistic (post-Newtonian) two-body problem. The usual classical celestial mechanical first-order perturbation theory is outlined. There are special topics in classical celestial mechanics that are of interest for the central subject of the book, e.g. the anomalous perihelion shift of planetary orbits due to the action of other planets, which can be treated with such a first-order perturbation theory. Later, it will also be used in connection with relativistic dynamical problems such as planetary or satellite motion.

Chapter 4 is devoted to Maxwell’s theory of electromagnetism as an introduction to the field of relativity. Here, a metric tensor is introduced from a physical point of view for the first time, and the Lorentz transformation is derived. The electromagnetic field (Liénard-Wiechert potentials) of a moving point charge is discussed in some detail. The problem of the ‘speed of propagation’ in electromagnetism is exhaustively treated here. The attentive reader will ask for a reason for this. First, this problem is generally not understood very well, though all details can be found in the literature. One often hears that relativity means nothing moves faster than light in vacuum, which is absolutely not the case. Though causality is always assured by the use of retarded potentials, physics is full of superluminal speeds as explained in the text. To many readers, it might not be clear which velocity is restricted to the vacuum speed of light if the propagation of an electromagnetic wave through a dielectric medium is concerned. Another common error is that the use of retarded potentials implies retarded propagating action with the vacuum speed of light in all cases. In any case, this part sheds light on the problem of the ‘speed of gravity’ that has been the subject of many controversial discussions in the past.

Chapter 5 introduces Einstein’s theory of gravity. The field equations are derived, and the problem of coordinates, the gauge problem in GR, is discussed. Observables have to be coordinate-independent quantities (as measured objects, they cannot depend upon a certain coordinate system that a theoretician employs for his calculations) and, therefore, have to be described as scalars. This implies that observers and parts of the measuring devices (e.g. in form of tetrad-vectors) have to be introduced explicitly into the formalism. For AGR, there are only three types of observables that play a central role besides proper time (a time that might be read-off some idealized clock): (1) the ranging observable as measurable time interval between emission and reception of some electromagnetic signal (as in laser ranging) (2) the spectroscopic observable presenting measurable frequencies of some incident light ray and (3) the astrometric observable as the angle between two incident light rays as seen by some observer.

Chapter 5 also deals with the Landau-Lifshitz formulation of Einstein’s theory which presents the basis for the MPM formalism, a perturbation theory that formally can be extended to any order of corresponding small parameters. The Landau-Lifshitz formulation chooses the harmonic gauge from the beginning and works with the ‘gothic metric’ g̅^μν = -√-g g^μν instead of the usual one, g^μν (g = det g_μν).

Chapter 6 presents some exact solution of Einstein’s field equations in the vacuum that might be of some use for the field of AGR. I am not convinced that from a methodological point of view, it is preferable to start from some exact solutions before one deals with approximations: Einstein’s theory of gravity might be violated at some level of accuracy; to deal with exact models, a real problem has to be over-simplified and so on. Nevertheless, exact models sometimes might be of help how to extend a certain approximative framework to higher orders. In this chapter also, cosmologically relevant spacetimes are introduced in relation to the following question: How does the global expansion of the universe influence the gravitational physics in the solar system?

Chapter 6 also introduces multipole moments for stationary gravitational fields obeying the vacuum field equations and poses the properties of asymptotic flatness. Due to the definitions of Geroch (1970) and Hansen (1974), such field moments can be defined rigorously. Later, they will be related with body moments as integrals over the energy-momentum tensor of the body. Thorne in 1981 has introduced field moments differently by the structure of the metric tensor in special coordinates systems (asymptotically Cartesian and mass-centred coordinates) that were later shown to be equivalent to the Geroch-Hansen moments (Gürsel 1983).

Chapter 7 introduces the post-Newtonian approximation of GRT as slow-motion, weak-field approximation and the multipolar post-Minkowskian formalism. A canonical form of the metric tensor is discussed in the first post-Newtonian (PN) approximation, where the gravitational field is entirely described with two potentials only: a scalar potential w that generalizes the Newtonian gravitational potential U and a vector potential w that describes gravito-magnetic-type gravity resulting from matter currents (moving or rotating masses). The corresponding field equations are very similar to Maxwell’s equations of electromagnetism.

This chapter also deals with the exterior field of a body to first PN-order, where post-Newtonian multipole moments (Blanchet-Damour moments) come into play, and the last part is devoted to the multipolar post-Minkowskian (MPM) formalism. First applications, which do not require a formalism for the gravitational N-body problem, are discussed in Chap. 8 on the basis of the first PN framework. Discussed are the gravitational field of the Earth, equipotential surfaces, clocks and time scales (TCG, TAI, TT, UTC) in the vicinity of the Earth and in the barycentric system (TCB, TDB), clock synchronization, the gravitational light deflection and time delay in the field of a single central body, the PN motion of torque-free gyroscopes and the satellite motion in the field of a rotating Earth to PN-order.

Chapter 9 is devoted to the BK-DSX framework of relativistic celestial mechanics which is based upon a total of N + 1 different coordinate systems in the gravitational N-body problem: one global system with coordinates (ct, x) that, neglecting all matter outside the system of N bodies and assuming asymptotic flatness, extends to (spatial) infinity and is used to describe the overall motion of the N bodies and N local systems and one for each body A with coordinates (cT_A, X_A) that is co-moving with body A and used for a description of physics (e.g., geophysics) in the local A-system. For many applications, the BK-DSX formalism is the best one, providing highest accuracy at present.

Chapter 10 deals with the post-Newtonian gravitational N-body problem. Laws and equations of motion for the translational and rotational cases are discussed here. For a system of pure mass monopoles, the famous Lorentz-Droste Einstein-Infeld-Hofmann equations (in harmonic gauge) for translational motion are derived. They form the basis for any modern high-precision numerical ephemeris, such as one from the DE, INPOP or EPM series (see e.g. Soffel and Langhans 2013).

Chapter 11 is devoted to relativistic astrometry while Chap. 12 to relativistic metrology, where many techniques like pulsar timing, navigation by means of GNSS, satellite and lunar laser ranging (SLR and LLR), very long baseline interferometry (VLBI), etc. are theoretically described in a consistent relativistic framework.

Of course, there are other books that deal with Applied General Relativity in one way or another. We would like to mention especially the book by Kopeikin et al. (2011), where many of the subjects are in common with those of this book. A comparison, however, reveals that these books are of very different character.

It is the hope that this book fills the obvious gap in the field of ‘Applied General Relativity’. It is a textbook with a clear red thread, containing many exercises with solutions in most cases. We hope that we have not forgotten a field of application that really is of practical interest. It is a pleasure for us to thank all those people who have contributed to this book in one way or another: Andreas Bauch, Francisco Frutos, Franz Hofmann, Enrico Gerlach, Sergei Klioner, Sergei Kopeikin, Jürgen Müller, Gerhard Schäfer, Maximilian Schanner, Harald Schuh, Irina Tupikova and Sven Zschocke, to name just a few. Clearly, for all the mistakes, only the authors are responsible.

Dresden, Germany Michael H. Soffel Shanghai, China Wen-Biao Han April 2019 3.7.2 Kepler's First and Third Law .......... 87 3.7.3 Classification of the Conic Sections ....................... 89 3.7.4 Kepler's Equation ........................................... 91 3.7.5 Fourier-Analysis in the Elliptical Orbit .................... 94 3.7.6 The Elliptical Kepler Orbit in Space ....................... 95

## 3.8 Perturbation Theory

3.8.1 Variation of Constants ...................................... 100 3.8.2 Perturbation Equations, Derived from Vectorial Elements .................................................... 101 4 Relativity .................................................................... 115

## 4.1 Relativity

## 4.2 Electrodynamics and Special Theory of Relativity

4.2.1 Maxwell's Equations ....................................... 116

## 4.3 The Minkowskian Metric, Lorentz-Transformation

4.3.1 Addition of Velocities ...................................... 127 4.3.2 Thomas Precession ......................................... 128 4.3.3 General Coordinate Transformations and a Derivation of the Lorentz-Transformation ................. 132

## 4.4 The EM-Field of a Moving Point Charge

## 4.5 The Speed of Propagation in Electromagnetism

4.5.1 The Vacuum Case ........................................... 139 4.5.2 Propagation in a Uniform Dielectric Medium ............. 145

## 4.6 Energy and Momentum

5 Einstein's Theory of Gravity .............................................. 157

## 5.1 General Relativity

## 5.2 Einstein's Equivalence Principle

## 5.3 The Motion of Test Bodies

## 5.4 Einstein's Theory of Gravity

## 5.5 The Problem of Observables

5.5.1 The Ranging Observable ................................... 165 5.5.2 The Spectroscopic Observable ............................. 165 5.5.3 The Astrometric Observable ............................... 167

## 5.6 Tetrads and Tetrad Induced Coordinates

## 5.7 Proper Reference Systems of Accelerated Observers

## 5.8 The Landau-Lifshitz Formulation of GR

5.8.1 The Landau-Lifshitz Field Equations ...................... 179 5.8.2 Harmonic Gauge ............................................ 181 6 Exact Solutions—Field Moments ......................................... 185

## 6.1 Minkowskian Space-Time

## 6.2 Stationary Space-Times

6.2.1 Stationary Axially Symmetric Space-Times .............. 192 6.2.2 The Hartle-Thorne Metric .................................. 198 6.2.3 Static Axially Symmetric Space-Times ................... 199 6.2.4 Spherically Symmetric Space-Time ....................... 209

## 6.3 The Kerr Metric

6.3.1 Boyer-Lindquist Coordinates .............................. 213

## 6.4 Cosmologically Relevant Spacetimes

6.4.1 The Cosmological Principle ................................ 215 6.4.2 Robertson-Walker Metric .................................. 217 6.4.3 De Sitter Space ............................................. 221 6.4.4 Schwarzschild: De Sitter Solution ........................ 223

## 6.5 Field Moments

6.5.1 Geroch-Hansen Moments .................................. 224 6.5.2 Thorne Moments ............................................ 226 6.5.3 The FHP Theorem .......................................... 230 7 The Post-Newtonian and MPM Formalisms ............................. 235

## 7.1 The Post-Newtonian Expansion

## 7.2 The General Form of the Metric

## 7.3 Field Equations and the Gauge Problem

## 7.4 The External Post-Newtonian Field of a Body

## 7.5 The Multi-Polar, Post-Minkowskian (MPM) Formalism

## 7.6 Several Expansions

## 7.7 First Post-Minkowskian Approximation

## 7.8 The MPM Algorithm

7.8.1 The First PN Approximation ............................... 274 7.8.2 The MPM Iteration Scheme ................................ 283 8 First Applications of the PN-Formalism ................................. 289

## 8.1 Equipotential Surfaces and Relativistic Geoid

8.1.1 Post-Newtonian Equipotential Surfaces ................... 291

## 8.2 The Problem of Time in the Vicinity of the Earth

8.2.1 Synchronization of Nearby Clocks ........................ 293 8.2.2 Rates of Clocks in the Earth's Vicinity .................... 294 8.2.3 Synchronization of Clocks in the Vicinity of the Earth ... 296 8.2.4 Coordinate Time Synchronization ......................... 297 8.2.5 The Relation Between Coordinate and Proper Time ...... 298 8.2.6 Clock Comparisons: Practical Aspects .................... 300 8.2.7 TAI, TT and UTC ........................................... 304

## 8.3 Barycentric Timescales TCB, T_eph, TDB

## 8.4 Fairhead–Bretagnon Series

## 8.5 Light-Rays in the PN-Field of a Single Body

8.5.1 The Celestial Sphere ........................................ 314 8.5.2 The Astrometric Observable ............................... 314 8.5.3 The Gravitational Time Delay ............................. 316

## 8.6 The PN Motion of a Torque-Free Gyroscope

## 8.7 Geodesic Motion in the PN-Schwarzschild Field

## 8.8 Celestial Mechanical Perturbation Theory

8.8.1 Post-Newtonian Schwarzschild Effects .................... 329 8.8.2 The Lense-Thirring Effect ................................. 332 9 Astronomical Reference Systems ......................................... 337

## 9.1 The Problem of Celestial Mechanics

## 9.2 Transformation Between Global and Local Systems

## 9.3 Split of Local Potentials, Multipole-Moments

## 9.4 Local Harmonic Proper Coordinates

## 9.5 The Standard xμ → Xα Transformation

## 9.6 The Description of Tidal Forces

9.6.1 Post-Newtonian Tidal Moments ........................... 354

## 9.7 BCRS and the Expansion of the Universe

10 The Gravitational N-Body Problem ...................................... 367

## 10.1 Local Evolution Equations

## 10.2 The Translational Motion

10.2.1 The LD-EIH Lagrangian ................................... 374 10.2.2 Laws of Motion ............................................. 375 10.2.3 Equations of Motion ........................................ 377

## 10.3 The PN Two-Body Problem

10.3.1 The Brumberg Representation ............................. 382 10.3.2 The Wagoner-Will Representation ........................ 384 10.3.3 The Damour-Deruelle Representation ..................... 387

## 10.4 The Rotational Motion

10.4.1 Landau-Lifshitz and Fock Spin ............................ 392 10.4.2 The PN-Spin in the N Body Problem ..................... 394

## 10.5 Rigidly Rotating Multipoles

10.5.1 Angular Velocity ............................................ 397 10.5.2 Rigidly Rotating Multipoles ............................... 398 11 Light-Rays ................................................................... 401

## 11.1 Historical Remarks

## 11.2 Light-Rays for 1PN Stationary Multipoles

11.2.1 The Shapiro Time Delay ................................... 412 11.2.2 The Time Transfer Function ............................... 414 11.2.3 The TTF for a Body Slowly Moving with Constant Velocity ..................................................... 415

## 11.3 Light-Rays to Post-Minkowskian Order

11.3.1 The Shapiro Time Delay ................................... 421

## 11.4 The Klioner-Formalism

11.4.1 Relativistic Aberration ..................................... 424 11.4.2 Gravitational Light Deflection ............................. 425 11.4.3 Parallax ...................................................... 425 11.4.4 Proper Motion and Radial Velocity ........................ 426 12 Metrology .................................................................... 431

## 12.1 Pulsar Timing

12.1.1 Pulsar Timing Arrays ....................................... 442

## 12.2 GNSS

12.2.1 Global Positioning System ................................. 444 12.2.2 GLONASS .................................................. 448 12.2.3 GALILEO ................................................... 449 12.2.4 BEIDOU .................................................... 450

## 12.3 SLR–LLR

12.3.1 Satellite Laser Ranging ..................................... 450 12.3.2 Lunar Laser Ranging ....................................... 453

## 12.4 VLBI

12.4.1 The Gravitational Time Delay ............................. 465 12.4.2 The Geometrical Delay ..................................... 469 12.4.3 Radio Sources at Finite Distance .......................... 473

## 12.5 Doppler Measurements

## 12.6 Gyroscopes

12.6.1 Passive Sagnac Interferometers 480

## 12.7 Astrometry

12.7.1 Hipparcos 490 12.7.2 The Astrometric Project Gaia 493 13 Appendix 497

## 13.1 Legendre-Polynomials

13.1.1 Q(x) for x ≥ 1 498

## 13.2 Relations for STF-Tensors

## 13.3 Differential Geometry: Formulas

## 13.4 Spherically Symmetric Metric

## 13.5 Spherically Symmetric Static Metric

## 13.6 The Kerr Metric: Geometry

## 13.7 Relations Concerning Multipole-Moments

13.7.1 Multipole-Moments Derived from ξ-Moments 510 13.7.2 Multipole-Moments Derived from Spherical Weyl-Moments 512

## 13.8 Weyl-Moments as Functions of Mass Multipole-Moments

List of Acronyms AC Astrographic Catalog ADM Arnowitt-Deser-Misner adv Advanced ALGOS Algorithm Involved in the Determination of TAI APOLLO Apache Point Observatory Lunar Laser-ranging Operation BCRS Barycentric Celestial Reference System BD Blanchet-Damour BIPM Bureau International des Poids et Mesures can Canonical CMO Calculated Minus Observed DM Dispersion Measure EAL Echelle Atomique Libre, a free timescale EFE Einstein Field Equations EIH Einstein-Infeld-Hoffmann EM Electromagnetic FP Finite Part GCRS Geocentric Celestial Reference System GD Geodetic Deviation GLONASS Russian Satellite Navigation System GNSS Global Navigation Satellite Systems GPS Global Positioning System ILRS International Laser Ranging Service INRIM Istituto Nazionale di Ricerca Metrologica (Torino, Italy)

IPTA International Pulsar Timing Array ISM Interstellar Medium JD Julian Date LAGEOS Laser Geodynamics Satellite LLR Lunar Laser Ranging LL Landau-Lifshitz LNE-SYRTE Laboratoire national de métrologie et d’essais (Paris, France)

LT Lense-Thirring MPM Multipolar Post-Minkowski NANOGrav North American Nanohertz Observatory for Gravitational Waves NIST National Institute of Standards and Technology (Boulder, Colorado, USA)

NPL National Physical Laboratory (Middlesex, GB)

OCA Observatoire de la Côte d’Azur PN Post-Newtonian PPS Pulse Per Second PPTA Parkes Pulsar Timing Array PRN Pseudo Random Noise PTA Pulsar Timing Array PTB Physikalisch-Technische Bundesanstalt (Braunschweig, Germany)

ret Retarded RF Radio Frequency SATRE Satellite Time and Ranging Equipment SLR Satellite Laser Ranging STF Symmetric and Trace-Free TAI International Atomic Time TCB Barycentric Coordinate Time TCG Terrestrial Coordinate Time TIC Tetrad-Induced Coordinates TIC Time Interval Counter TS Time Scale TTF Time Transfer Function TT Terrestrial Time TWSTFT Two-Way Satellite Time and Frequency Transfer UT1 Phase Angle of Earth’s Rotation UTC Coordinated Universal Time VLBI Very Long Baseline Interferometry

List of Symbols List of symbols used in the text (acronyms can be found at the end of the book)

t Physical time coordinate, especially TCB T Time coordinate, especially T = TCG x^μ Coordinates dx^μ Coordinate differential T^μν Tensor αβ L Liederivative in the direction of v Γ Affine connection, usually Christoffel symbol νλ A_μ;ν Covariant derivative of A_μ with respect to x^ν R^ρ_αμν Curvature tensor R_μν Ricci tensor G_μν Einstein tensor g_μν Metric tensor ds^2 Infinitesimal distance between neighbouring points in a manifold g Determinant of g_μν : det g_μν |M| Determinant of matrix M [μ_1 μ_2 ... μ_n] Levi-Civita symbol ε^μ1μ2...μn Levi-Civita tensor U Newtonian gravitational potential U_tidal Newtonian tidal potential (C_lm, S_lm) Potential coefficients, spherical mass moments J_l, J_l^~ Spherical mass moments for axial symmetry and their dimensionless counterpart T_L STF part of T_L M STF mass moments S STF spin moments G STF (gravito-electric) tidal moments H STF (gravito-magnetic) tidal moments f True anomaly E Eccentric anomaly S, T, W Radial, transverse and normal component of the perturbing function M Mean anomaly E, B EM field vectors j^μ EM current density F_αβ EM field tensor A EM vector potential k^μ Wave vector, tangent to some light ray u^μ Four-velocity Ri Rotation matrix T^μν Energy-momentum tensor e_(α) Tetrad (field)

ω_(abc) Ricci rotation coefficients z_obs World-line of observer ω^μ Twist four vector w^μ Twist three vector E_mixed Complex Ernst potential ort± (1/2)(t_ret + t_adv)

g_μν Gothic metric tensor t^LL_αβ Landau-Lifshitz pseudotensor ε_B, ε_C, ε_G Expansion parameters δ(x) Dirac delta function (distribution)

f^(n)(x) nth derivative of f with respect to x Z_i, Z_e Inner and exterior zone w^k, h^k Potentials of the PN-metric k_n, h_n Love numbers f_plasma Plasma frequency X^α Local coordinates, usually geocentric coordinates Λ^μν Landau-Lifshitz complex ∂_i_∥, ∂_i_⊥ Partial derivatives with respect to x^i parallel and perpendicular to some three vector n t_obs Time of observation m_I, m_G Inertial and gravitational mass η Nordtvedt parameter P_l(x), Q_l(x) Legendre functions of the first and second kind

## Chapter 1 Introduction

In 1905, Albert Einstein published four papers that changed modern science fundamentally. Among them there was an article on the electrodynamics of moving bodies that laid the foundation of Special Relativity Theory (SRT) (Einstein 1905). About 10 years later, Einstein revolutionized Newton’s theory of gravitation and formulated a space-time geometrized picture of the gravitational interaction: Newton’s gravitational force was replaced by the curvature of space-time (Einstein 1915).

Actually Einstein’s theory of gravity (General Relativity) was an applied science from the very beginning when in 1915 Einstein derived the anomalous perihelion advance of Mercury, thus solving the most important problem of celestial mechanics of the nineteenth century (Roseveare 1982; Pais 1992). In 1859, Urbain Le Verrier was the first to report that the slow precession of Mercury’s orbit around the Sun could not be completely explained by Newtonian mechanics. For the first time in history he was able to compute the perturbations of the known planets onto Mercury’s perihelion advance: 153.6 from Jupiter, 277.8 from Venus, 90.0 from Earth, 7.3 from Saturn and 2.5 from Mars (in arc s/century). Together with the general precession of the classical astronomical reference system at epoch 1900 of 5025.6/cen. the calculations yield a total value of 5557.0/cen., whereas the observed value amounts to 5599.7/cen.(Will 1993). So the anomalous perihelion advance of Mercury is about 43 /cen., that was immediately derived from Einstein’s General Relativity without further obscure assumptions such as, e.g., the existence of a new planet, Vulcan, near the Sun.

In addition to that General Relativity was able to explain the deflection of light by the gravitational field of the Sun that amounts to 1.75 for a light-ray that just grazes the limb of the Sun. Since the light deflection angle decreases like 1/r with increasing distance from the Sun, for light rays incident at about 90 from the Sun the angle of light deflection still amounts to 4 mas (milliarcseconds).

In Einstein’s theory of gravity light-rays move along geodesics (“shortest curves between two points”) in curved space-time and the curvature of space deflects an observed stellar image outwards from the Sun. Historically, the light deflection in the gravitational field of the Sun had been first detected by the British expeditions to Sobral (Brazil) and Principe (Gulf of Guinea) taking photographic pictures of the solar vicinity during the solar eclipse on the 29th May, 1919. These measurements, though provided with large errors, confirmed the predictions from GRT and helped to make Einstein famous (e.g., Weinberg 1972; Soffel 1989; Will 1993).

Already in 1916, de Sitter (1917) derived a relativistic precession of the lunar orbit about the Earth when moving in the gravitational field of the Sun, now called the de Sitter effect or geodetic precession. In 1918, Lense and Thirring (Lense 1918; Thirring 1918, 1921; Lense and Thirring 1918; Mashhoon et al. 1984) predicted the precession of some satellite orbit about a central gravitating body due to its relativistic gravito-magnetic field induced by its rotational motion.

Despite of these early ‘applications’ General Relativity for a long time was mainly understood as some esoteric, mathematically oriented discipline far from ‘real applications’ in science and technology.

## 1.1 Time and Reference Systems

This situation, however, changed with the development of clocks with high accuracy and stability. A clock in principle is a frequency generator or oscillator with stochastic properties. Its accuracy describes the capability to realize the SI-second, whereas stability refers to the fluctuations around some averaged clock-frequency. Figure 1.1 shows the increase in accuracy of mechanical and atomic clock until the year 2000, when stabilities of order 10^{−15} for cesium fountains were achieved.

In 1927 the first quartz clock was built by Marrison and Horton (1928) at Bell Telephone Laboratories in Canada, whereas the first practical cesium atomic frequency standard was built at the National Physical Laboratory in England in 1955 by Louis Essen and Jack Parry (Fig. 1.2). Though cesium clocks especially in the form of fountains achieve a remarkable level of stability, they are clearly limited. A stability of order 10^{−15} can be achieved only after averaging over a day which presents a problem for real time applications. Now, the achievable stability of an atomic clock is related with the clock frequency that for cesium clocks lies in the microwave region at 9.2 GHz. Meanwhile optical clocks are built with clock frequencies of about 10^15 Hz, where comparable stabilities 扫描精度已经达到亚秒级。图1.3展示了基于微波和光学跃迁的原子钟分数频率不确定度的演化。很可能在不久的将来，光学钟将优于传统原子钟。关于光学钟的更多细节，读者可参考例如Ludlow等人（2015）及其引用的参考文献。同时，已有报道的分数频率不确定度达到了10^{-18}区域，例如NIST的27Al^+单离子钟（Chou等人2010）和JILA的87Sr光晶格钟（Bloom等人2014）（引自Poli等人2013）。这样一个稳定的时钟，其误差在宇宙年龄（约140亿年或4×10^17秒）之后也将小于一秒。这确实是一个令人惊叹的进步，并将以多种方式改变我们的世界。

早在1905年，爱因斯坦就证明，一个相对于某观察者以速度v运动的时钟，其时间会变慢，因子为√(1−(v/c)²)。需要注意的是，对于两个以恒定速度相对运动的时钟，情况对双方是完全对称的。然而，如果这种对称性被打破，例如，如果其中任一时钟经历了加速阶段，那么当它们被带到一起时，将会显示不同的时间。

在广义相对论中，是时空的曲率描述了引力相互作用。时间上的曲率难以可视化；它与引力红移相关：引力红移指的是，如果单色电磁信号穿过引力场，朝向牛顿势U较小的方向，其频率将发生红移。因此，位于x₁和x₂的两个时钟的自然频率f₁和f₂，满足关系f₂/f₁ = 1+[U(x₂)−U(x₁)]/c²，因此引力场中的时钟会变慢。

为了说明这一点，让我们考虑一个GPS卫星，它相对于地心以3874 m/s的速度运动。根据狭义相对论，相对于某个惯性地心观察者，GPS时钟变慢，因子为√(1−(v/c)²) ≈ 1+8.3×10^{-11}。这种时间膨胀会导致每天7.2 μs的时间误差，这应与GPS系统时间大约几十纳秒的精度（Müller等人2008）进行比较。时空曲率的贡献甚至更大：1−(ΔU/c²) ≈ 1+5.28×10^{-10}，其中ΔU是地球表面与卫星高度之间的引力势差。由于势能部分的符号与速度部分的符号相反，总效应为+4.45×10^{-10}，即GPS卫星时钟比地球上的接收器时钟每天快约38 μs（Müller等人2008）。

因为原子钟指示的观测时间（作为理想化的固有时τ）取决于时钟在该位置的速度和引力势，所以定义有用的时间标度就成了一个问题，即定义在特定时空部分有效的时间坐标，并将它们与特定一组原子钟的读数相关联。通常，时间坐标只是时空坐标系的一部分，例如地心天球参考系（GCRS），其坐标为(T, X)，通常选择地心为原点。GCRS的坐标T称为地心坐标时TCG，地心坐标时是地球附近（特别是大地测量学和地球物理学）物理学的基础时间标度（Soffel等人2003）。TCG是根据指示固有时τ的原子钟间接实现的，关系为dτ/d(TCG) ≈ 1−(U+v²/2)/c²。对于与地球共转的地球时钟，此关系为dτ/d(TCG) ≈ 1−U_g/c²，其中U_g是重力势，包括引力势和旋转势。因此，在等势面U=const上，原子钟的速率相同，而对于高度差ΔR，相对频率差Δf/f ≈ (GM/c²R) × (ΔR/R)，其中R是地球半径，(GM/c²R) = 7×10^{-10}。因此，对于ΔR = 1 km，相应的速率差约为10^{-13}，而稳定度达到10^{-18}的时钟应能测量小于1 cm的高度差。这提供了通过比较不同地点的光学钟读数来确定重力势微小差别的可能性，并弥合大地水准面（由GOCE等专用卫星确定）的全球尺度几何与局部几何之间的差距。为此，将采用玻璃纤维网络来比较可能相距1000公里的不同钟的速率。

这种与极精确的时间和频率测量相关的光学钟比较，将具有多种应用，例如在基础物理学（例如，Kozlov等人2018）中，人们寻找基本常数如精细结构常数α或电子与质子质量比的时间变化。在海洋学中，人们感兴趣的是相对于大地水准面的海面地形，以推断可能受气候变化影响的海流。

实际上，时间标度TCG是通过国际原子时TAI或地球时TT来实现的。最初，TT在IAU决议A4（1991）中定义为：“一个与地心坐标时（TCG）相差一个恒定速率的时间标度，TT的测量单位选择得使其在地球水准面上与SI单位一致”。当考虑低于10^{-17}的精度时，这个TT定义出现了一些缺陷，原因是地球水准面上U的不确定性以及大地水准面的实现（Müller等人2008；Petit 2003）。为此，IAU决定通过d(TT)/d(TCG) = 1 − L来固定TT-TCG关系，其中定义常数L = 6.969290134×10^{-10}，以确保与地球水准面上当前最佳估计值U = 62,636,856 (m/s)²（Groten 2000）的连续性。

地球时TT通过其关系TT = TAI + 32.184 s从国际原子时TAI导出。TAI源于全球各实验室400多个时钟的读数。这些读数，在归算到某个“准大地水准面”（与TT兼容）之后，首先生成一个称为自由原子时EAL的自由时间标度。从EAL中，TAI的频率最终由少数几个初级频率标准进行微调。

最后，协调世界时UTC，与TAI相差一个确定的闰秒数，以确保UTC与某个地球自转角度UT1之差始终小于0.9秒。这具有一个优点，即在很长的时间跨度内，UTC通过UT1与太阳保持联系，这对于日常生活有好处。如果不引入闰秒，UTC–UT1将主要由于潮汐效应导致的地球自转速率长期减慢而呈现长期漂移。各种区时（国家标准时间）通常与UTC相差整数小时，这根据地球表面被划分为时区。

TCG、TT、TAI和UTC是地心时间标度，应用于在适当选择的与地球共动的参考系中描述地球附近的物理学：它们是地心时间标度。特别是TCG是地心天球参考系（GCRS）的时间坐标，其原点通常选择与地心重合。对于其他目的，例如行星星历表或星际航天器导航，应使用质心时间标度。质心坐标时TCB是质心天球参考系（BCRS）的时间坐标，原点位于太阳系的质心。TCB的实现是通过其与TCG的关系来完成的：d(TCG)/d(TCB) ≈ 1−c^{-2} U_{ext}(z_E) + (1/2)v_E²。

一些最好的太阳系星历表，如喷气推进实验室（JPL）的DE星历表，并未使用TCB作为基本时间变量（Soffel和Langhans 2013）。最初的想法是使用一个时间标度T_eph，它与TT实际上只相差周期项，这些周期项由于太阳系运动中任意长的周期而无法以极限精度实现。因此，定义了另一个质心时间标度TDB，通过TDB = TCB − L_B × (JD − T_0) × 86,400 s + TDB_0给出，其中L_B = 1.550519768×10^{-8}，TDB_0 = −6.55×10^{-5} s。JD是儒略日，L_B = 1.550519768×10^{-8}的值是为最小化TDB与TT之间在DE405星历表下的线性漂移而选择的。由巴黎天文台开发的行星星历表称为INPOP（Fienga等人2009），是四维的，即除了太阳系天体的位置和速度外，自INPOP08起它还提供了TT-TDB值。

时间标度的建立离不开时钟同步和时间传递的程序。如今，时钟同步通过全球导航卫星系统（GNSS）或双向卫星时间频率传递（TWSTFT）来完成。使用载波相位TWSTFT测量进行频率传递，对于洲际距离，已报道的精度达到几皮秒量级（1秒积分时间），传递稳定度在100秒时达到10^{-14}量级（例如，Schäfer等人1999）。对于长达9000公里的非常长基线，已获得10^{-13}量级（在1秒时）的短期稳定度（例如，Fujieda等人2014）。由于相对论“效应”的量级为7×10^{-10}，它们显然必须被考虑在内。由于爱因斯坦的时钟同步程序（两个时钟 Clocks with constant distance are synchronized by some central device, located exactly in the middle between the two clocks, that emits electromagnetic signals to the two clocks simultaneously. The two clocks can then be synchronized from the arrival times of the signals) is not possible on the rotating Earth (due to the Sagnac effect in time) clock synchronization is usually a coordinate time synchronization using the relation between proper time and TCG: two clocks showing proper times τ1 and τ2 are synchronous if their corresponding TCG-values agree. Note, that the Sagnac effect can amount to hundreds of nanoseconds; a GPS timing error of one nanosecond can lead to a navigational error of 30cm (Ashby 2004).

## 1.2 Space

Geodetic or astronomical measurements of ‘space’ and thus the realization of spatial coordinates, usually involve electromagnetic signals being emitted by some observer, reflected by some device so that at least some photons return to the observer and the propagation time interval between emission and reception of the signal is measured. Measurement of ‘space’ then is based upon measurements of time. For short distances the geodesist uses tachymeters for local measurements of ‘space’. Of tremendous importance is the establishment of the spatial parts of geodetic-astronomical reference frames. For the Earth it is the International Terrestrial Reference System, the ITRS, with the ITRF as practical realization. The ITRS is geocentric with a center of mass referring to the whole Earth including oceans and atmosphere. Its spatial orientation was initially given by a BIH orientation at 1984.0 and the time evolution of the orientation is involving a plate tectonic model via a ‘no-net-rotation’ condition. Since 1988 the ITRS was presented in form of 13 realizations (ITRF89–ITRF2014), distributed by the International Earth Rotation and Reference Systems Service (IERS; formerly called: International Earth Rotation Service). Each realization estimates the geocentric coordinates and velocities of a set of stations observed by the Global Positioning System GPS, SLR (Satellite Laser Ranging), LLR (Lunar Laser Ranging), DORIS (Doppler Orbitography by Radiopositioning Integrated on Satellite) and VLBI (Very Long Baseline Interferometry) thus carefully mapping the complicated motion of the Earth’s crust. Relativity enters in many places, in metrology, satellite dynamics, dynamics of the solar system, signal propagation etc. that will be discussed in the main part of the book.

The International Celestial Reference System (ICRS) presently is the standard celestial quasi-inertial (i.e., with respect to rotations) reference system that extends far into the universe to the most distant objects in space. Its realization, the ICRF, is in the form of catalogues of extragalactic radio sources (mainly quasars), whose positions and structure images are obtained with VLBI. The original ICRF was adopted by the IAU in 1998, the update ICRF in 2009 and the ICRF in 2018. The ICRF contains positions of 4536 extragalactic sources out of which 303 have been identified as defining sources. Presently global distances on the Earth’s surface can be determined via VLBI with accuracy of a few mm; now, an accuracy of one millimeter corresponds to a light travel time of about 3ps and in a corresponding geodetic VLBI model all terms down to the order 0.3ps should be taken into account (Heinkelmann and Schuh 2010). At this level of accuracy a large number of relativistic ‘effects’ have to be taken into account, such as those resulting from the mass-monopole and quadrupole of solar system bodies to post-Newtonian order, post-post Newtonian terms related with the solar mass, velocity effects etc.

The ITRS might be directly related with the GCRS, the ICRS with the BCRS and the corresponding coordinates (t,x) (BCRS) and (T,X) (GCRS) are related by complicated space-time transformation that will extensively be discussed in this book. The applied aspects of relativity in the modern age can nicely be seen when one considers the motion of the ITRS with respect to the GCRS, that classically is split by introducing some intermediate system into an astronomically dominated part (precession-nutation, length of day (LOD) variations) and a geophysically dominated part (polar motion). This motion is described by Earth orientation parameters (EOP) whose dynamics results from the physics of the various subsystems of the Earth (atmosphere, ocean, hydrosphere, cryosphere, elastic mantle, fluid outer core, solid inner core) and their complex interactions, including the tidal effects from the Sun, Moon and planets (Fig.1.4). From this important information e.g., for global climate variations and even for anthropogenically induced environmental changes can be derived. Figure 1.5 clearly demonstrates that El Niño events can be seen in VLBI data on LOD variations. Periodically, El Niño appears every 3–7 years. The Spanish word El Niño means child but actually means Christ child, since this phenomenon usually appears around Christmas time. With the beginning of EN, the water in front of the coast of Peru becomes warmer and fish food from the cold water disappears. El Niño begins with a weakening of the trade winds who can even change their direction. Usually the trade winds blow very violently. After an EN event during one to 2 years again normal pressure gradients built up again and the trade winds blow normal again in the tropics of the Pacific. These oscillations of air pressure are also called Southern Oscillation, linked with El Niño this is called: El Niño SOUTHERN OSCILLATION (ENSO). It is not only the economically significant El Niño events that one can derive from VLBI data on EOPs, but also affects as mean sea level rise, melting of ice masses at the polar caps or glaciers. Most parts of your complicated system Earth can be monitored with modern geodetic techniques that for reaching utmost precision require models where relativity should be considered.

## 1.3 Astrometry

Astrometry, the discipline to measure stellar positions and velocities, has made a tremendous progress with the space astrometric missions Hipparcos and Gaia. The ESA satellite mission Hipparcos (1989–1993) measured the positions of about 120,000 stars with the precision of about 1mas (milli-arcsec), the Gaia mission (satellite launch: 19.12.2013) reaches incredible accuracies depending on stellar magnitudes: about 4μas for very bright stars. This corresponds roughly to the appearance of a one EUR coin on the Moon as seen from the Earth! Up to now Gaia data sets have been released containing information on 1.7 billion stars, quasars, asteroids and galaxies. This includes precise measures of distance and motion across the sky, brightness and colours for 1.3 billion stars (our Milky Way has about 100 billion stars), radial velocities for 7 million stars, stellar parameters for some 100 million stars, variability over time for 550,000 stars, and accurate orbital data for 14,000 asteroids. It should be clear that at the μas level of accuracy quite a refined relativistic model has to be used for the data analysis. In practice it is the relativistic Klioner-model called Gaia Relativity Model (GREM), extensively described in this book, that is used for the Gaia mission. The astrometric, photometric and spectral data from the Gaia mission will clearly revolutionize all parts of astrophysics. It will provide new insights into – the origin and evolution of our Milky Way galaxy, – stellar physics, – stellar multiple systems, – the field of Exo-planets, – solar system bodies and their dynamics, – the realization of astronomical reference frames, – fundamental physics, – quasars and distant galaxies.

For example, in the field of fundamental physics tests of Special and General Relativity will be performed and hopefully the Gaia data will shed some new light on the problem of dark matter. For more details the reader is referred to the literature (see the websites of ESA and the publications related with the Gaia mission).

## 1.4 Celestial Mechanics

We have already mentioned the relativistic perihelion advance of Mercury’s orbit due to the relativistic mass monopole of the Sun of order 42.98″/cy; this relativistic orbital precession amounts to 8.63″ for Venus, 3.84″ for the Earth, 1.35″ for Mars, 0.06″ for Jupiter and 0.01″ for Saturn (all in ″/cy.). Even for the motion of certain asteroids this relativistic perihelion precession should be taken into account. E.g., this orbital motion amounts to 0.101″/y for 1566 Icarus, 0.043″/y for 2062 Aten and 0.101″/y for 3200 Phaeton (Shadid-Saless and Yeomans 1994). In modern solar system ephemerides also the relativistic effects arising from the gravitational fields of the planets should be taken into account. For that reason the post-Newtonian equations of motion for a whole set of mass-monopoles (‘point masses’), the Einstein-Infeld-Hoffmann (EIH) equations are the basis of the three state-of-the-art solar system ephemerides: the American one, DE (Development Ephemeris; JPL); the Russian one, EPM (Ephemerides of Planets and the Moon; IPA, St. Petersburg); and the French one, INPOP (Intégration Numérique Planétaire de l’Observatoire de Paris) (Soffel and Langhans 2013 and references quoted therein).

With respect to the motion of artificial Earth satellites we have to keep in mind that the gravitational radius of the Earth RG = GM_E/c^2 is about 0.44cm. This implies that for a model of satellite motion relativistic terms become important for high precision orbit determination which is e.g., possible for the LAGEOS, LAGEOS II, and LARES. If an orbit cannot be determined with cm accuracy or better relativistic effects might be absorbed in the orbital parameters (Soffel and Frutos 2016). Figure 1.6 shows a variety of accelerations of some Earth satellite in km/s^2 as function of the orbits.

semi-major axis in km. The red curves labelled by ‘Moon’, ‘Sun’, ‘Venus’ and ‘Jupiter’ refer to the (Newtonian) tidal accelerations. The contributions from the various zonal harmonics of the Earth are indicated by the green curves with the corresponding index. The three dominant relativistic accelerations in the GCRS are: (1) the contribution from the post-Newtonian spherical field of the Earth (the Schwarzschild acceleration) (dotted blue curve, labelled rel. Monopole), (2) the Lense-Thirring acceleration due to the gravito-magnetic field of the rotating Earth (dotted red curve) and (3) the relativistic acceleration due to the oblateness of the Earth (dotted blue curve, labelled rel. Quadrupole). In addition to that since the GCRS is NOT (locally) inertial we face a relativistic Coriolis force related with geodesic precession. This leads to an additional nodal drift ⊙GP of satellite orbits; for the LAGEOS orbit this is of order 17.60 mas per year. For the LAGEOS orbit we also included estimates of the direct solar radiation pressure (⊘), (e.g. Anselmo et al. 1983), the Earth albedo (∇), infrared pressure (∇) and the atmospheric drag (maximal and minimal values) (Rubincam 1982). The orders of magnitude imply that for a measurement of relativistic effects (maybe apart from the Schwarzschild term) by means of SLR data from a single satellite, the even zonal harmonics of the Earth have to be known with extreme precision. E.g., the secular nodal drift of the LAGEOS orbit due to the Lense-Thirring effect of the rotating Earth is of order 2 (12/π) × 10^{-5} per revolution, roughly comparable with the effect from the l = 12 multipole. Ciufolini and colleagues (Ciufolini 1986a,b; Ciufolini and Pavlis 2004; Ciufolini et al. 2010, 2016; see also Iorio 2009a,b), however, succeeded to measure the Lense-Thirring effect with the orbital data of LAGEOS, LAGEOS II and LARES with a precision of a few percent.

## 1.5 Relativistic Astrophysics and Cosmology

For many researchers there are additional fields of Applied General Relativity of great importance, especially the fields of relativistic astrophysics and cosmology. The physics of compact objects (white dwarfs, neutron stars, black holes), of active galactic nuclei, quasars, dark matter, dark energy, the structure and evolution of the universe on all scales are very exciting and up to date topics of general interest. These topics have been treated exhaustively in the literature (e.g., Weinberg 1972; Rees et al. 1974; Kolb and Turner 1994; Zeldovich and Novikov 1997; Börner 2003; Dodelson 2003; Hyong 2006; Maggiore 2007; Demiański 2008; Weinberg 2008; Belusevic 2008; Giacconi and Ruffini 2009; Straumann 2012; Liddle 2015; Böhmer 2016; Ryden 2016; Maggiore 2018 to name just a few) and are not included in this book.

## Chapter 2 Elements of Differential Geometry

## 2.1 Space-Time Manifold and Fields

Physics deals with the behavior of certain objects (particles, bodies, fields, etc.) in 3-space in course of time. Formally, time and space can be combined to a 4-dimensional space-time, though the two entities, space and time, are always clearly distinguished. Usually 4-dimensional space-time is described by the mathematical picture of a manifold, a 4-dimensional space that locally looks like the Euclidean R⁴. Clearly this manifold picture is an idealization since arbitrarily small distances in space or time cannot be measured in principle. Moreover, because of quantum effects, one expects the manifold picture to break down for distances of order the Planck-length lₚ = (Għ/c³)^{1/2} ≈ 1.6 × 10^{-35} m or smaller. Presently, it is unclear how to describe gravitational physics at such small length scales.

Both the electromagnetic as well as the gravitational interaction are described with fields. Such fields are usually defined over a space-time manifold and characterize geometrical, i.e., coordinate independent physical objects (though below we will use coordinate components to describe them). Fundamental laws of physics, that are obeyed by such fields, are differential relations between the fundamental geometrical objects and, therefore, can also be formulated in a coordinate independent manner; they are formulated in the language of differential geometry. Using geometrical fields, like tensor fields, and coordinate independent laws of physics is often described as ‘principle of covariance’, though it basically is no ‘principle’, but a language form. E.g., in Chap. 3 on Newtonian Celestial Mechanics it is shown how Newton’s theory of gravity can be formulated in a covariant way.

Of course one way nature shows us lies in the selection of fields that one must use to describe the physical reality. The so-called equivalence principle implies that the gravitational interaction can be described with a single metric field. If, however, the equivalence principle breaks down at some level, then additional fields might play a role in the description of the gravitational interaction.

## 2.2 Coordinates, Differentials and Tensors

Mathematically a manifold (Fig. 2.1, an example of a two-dimensional manifold) is a triple (M, {U_α}, {φ_α}), where M is a set of points, {U_α} a collection of open sets in M with M = ∪_α U_α and {φ_α} are differentiable functions U_α → Rⁿ. For each point p ∈ M, there is at least one U_α with p ∈ U_α; then {φ_α} defines a local coordinate system in a surrounding U_α of p.

In a certain region R of an N-dimensional manifold M the various points of R are described by coordinates x^μ: R → Rⁿ, x^μ = (x¹, x², ..., xⁿ).

Example 2.1 An elementary example is the 2-dimensional Euclidean space that can be described by Cartesian coordinates (x¹, x²) = (x, y) or by polar coordinates with x̄¹ = r, x̄² = φ. The relation between these two sets of coordinates reads x = r cos φ; r = √(x² + y²)

y = r sin φ; φ = arctan(y/x).

Example 2.2 As another example we study the 3-dimensional Euclidean space. It can be described by Cartesian coordinates x^μ = (x, y, z).

Alternatively, we might use spherical coordinates (Fig. 2.2)

x̄^ν = (r, θ, φ).

The relation between two such sets of coordinates is a coordinate transformation x^μ → x̄^ν with r = √(x² + y² + z²)

θ = arctan(√(x² + y²)/z)

φ = arctan(y/x).

The inverse transformation reads x = r sin θ cos φ y = r sin θ sin φ z = r cos θ.

Objects dx^μ are called: coordinate differentials. Coordinate differentials transform under coordinate transformations according to the chain-rule. E.g., for the 3-dimensional Euclidean space in Cartesian and spherical coordinates we have: dx^μ = (∂x^μ/∂x̄^ν) dx̄^ν ≡ Σ_{ν=1}^3 (∂x^μ/∂x̄^ν) dx̄^ν, ∂x/∂r = sin θ cos φ, ∂x/∂θ = r cos θ cos φ, ∂x/∂φ = -r sin θ sin φ dx = (sin θ cos φ) dr + (r cos θ cos φ) dθ - (r sin θ sin φ) dφ ∂y/∂r = sin θ sin φ, ∂y/∂θ = r cos θ sin φ, ∂y/∂φ = r sin θ cos φ dy = (sin θ sin φ) dr + (r cos θ sin φ) dθ + (r sin θ cos φ) dφ, ∂z/∂r = cos θ, ∂z/∂θ = -r sin θ, ∂z/∂φ = 0 dz = cos θ dr - r sin θ dθ.

Here the Einstein’s summation convention was employed: over every pair of indices, one contravariant upper index and one covariant lower index, a summation is employed automatically even when the summation-symbol is dropped.

Generally we write dx^μ = (∂x^μ/∂x̄^ν) dx̄^ν.

The matrix (∂x^μ/∂x̄^ν) is called the (inverse) Jacobi-matrix.

Objects that transform like coordinate differentials dx^μ are called contravariant vectors: Ā^ν = A^μ (∂x̄^ν/∂x^μ).

Quantities T^{μ₁...μₙ}_{ν₁...νₘ} are called n-fold contravariant, m-fold covariant tensors if under a coordinate transformation they transform according to T̄^{λ₁...λₙ}_{σ₁...σₘ} = (∂x̄^{λ₁}/∂x^{μ₁}) ... (∂x̄^{λₙ}/∂x^{μₙ}) (∂x^{ν₁}/∂x̄^{σ₁}) ... (∂x^{νₘ}/∂x̄^{σₘ}) T^{μ₁...μₙ}_{ν₁...νₘ}.

One also says that such a tensor is of rank m + n (the total number of tensor indices). By this definition a contravariant vector is a one-fold contravariant tensor. A covariant vector A_ν is a one-fold covariant tensor that transforms according to Ā_σ = A_μ (∂x^μ/∂x̄^σ).

From the transformation rules it is clear that a set of tensors where each contravariant index has a corresponding covariant one and it is summed over all indices like in T^{μν}_{αβ} A^{α}_{μ} B^{β}_{ν} is a scalar, i.e., a coordinate independent object.

Exercise 2.1 Proof the last statement by considering general coordinate transformations.

2.2.1 Symmetrization and Antisymmetrization

Let A_{μν} and A_{μνλ} be arbitrary tensors. The components of the new completely symmetrized tensors are distinguished by round brackets (e.g., Misner et al. 1973; Exercise 3.12) and written as A_{(μν)} ≡ (1/2)(A_{μν} + A_{νμ})

A_{(μνλ)} ≡ (1/3!)(A_{μνλ} + A_{νλμ} + A_{λμν} + A_{νμλ} + A_{μλν} + A_{λνμ}).

Similarly, the corresponding completely antisymmetrized tensors are written with square brackets in the form A_{[μν]} ≡ (1/2)(A_{μν} - A_{νμ})

A_{[μνλ]} ≡ (1/3!)(A_{μνλ} + A_{νλμ} + A_{λμν} - A_{νμλ} - A_{μλν} - A_{λνμ}).

Exercise 2.2 Show that T_{μνλ} = A_{[μνλ]} with an arbitrary tensor A_{μνλ} changes sign if the indices of any pair are interchanged, e.g., T_{μνλ} = -T_{μλν}.

## 2.3 Tensor Algebra

There are several rules that follow from the definition of tensors: (1) The sum of two tensors of the same kind is again a tensor; (2) Multiplication of a tensor with a real number is again a tensor; (3) If T^{α₁...αₙ}_{β₁...βₘ} and S^{γ₁...γₒ}_{δ₁...δₚ} are tensors then also G^{α₁...αₙ γ₁...γₒ}_{β₁...βₘ δ₁...δₚ} = T^{α₁...αₙ}_{β₁...βₘ} · S^{γ₁...γₒ}_{δ₁...δₚ}; (4) If T^{α₁...αₙ}_{β₁...βₘ} is a tensor then also (summation over σ)

T^{α₁...αₙ₋₁σ}_{β₁...βₘ₋₁σ} This contraction process lowers the number of covariant- and contravariant indices by one respectively. In the same way any other pair of indices (one covariant and one contravariant) can be contracted.

## 2.4 The Lie-Derivative

A mapping φ : M → N between two manifolds, M and N, is called differentiable (diff) if for some pair of charts {U, φ} of M and {V, ψ} of N the mapping ψ ◦ φ ◦ φ⁻¹ from real numbers (coordinates for M) to real numbers (coordinates for N) is differentiable. A mapping φ : M → N is said to be a diffeomorphism, if φ is bijective (i.e., the inverse φ⁻¹ is well defined) and both, φ and φ⁻¹ are differentiable. Let v be a vector field on M. Then there is a curve γ(λ) through each point p ∈ M such that γ(0) = p and whose tangent vector at q = γ(λ) is just v(q).

In coordinates, let γ(λ) = xμ(λ) and vμ the coordinate components of v, then the integral curve xμ(λ) of v through p is uniquely determined by the first order differential equation dxμ/dλ = vμ(xν(λ)). (2.4.1)

By means of their integral curves a vector field v induces a family of diffeomorphisms φv in the neighborhood U(p) by taking each point of U a parameter distance λ along the integral curve of v, called the flow of v.

It is useful to describe the flow of v by a mapping of the form xμ → x'μ ≡ xμ + εvμ(x) (2.4.2)

where |ε| << 1. A scalar field φ then transforms, to first order in ε, as φ(x') = φ(xμ + εvμ(x)) = φ(x) + εL_v φ(x), (2.4.3)

where L_v φ ≡ vμ ∂μ φ (2.4.4)

is the Lie-derivative of φ in the direction of v and the comma denotes the partial derivative, ∂μ φ ≡ ∂φ/∂xμ.

Next we consider a covariant vector field with components u_μ. We first take u at the point q with coordinates x' and then transform it back to the point p with u'_μ(x) = u_ρ(x') = u_ρ(x') + εu_ρ,μ vρ = u_μ(x) + ε[L_v u]μ (2.4.5)

where [L_v u]μ = lim_{ε→0} (u'_μ(x) - u_μ(x))/ε = vρ ∂ρ uμ + uρ ∂μ vρ (2.4.6)

is the Lie-derivative of u in the direction of v. Similarly, g'_μν(x) = g_μν(x) + ε[L_v g]μν (2.4.7)

with [L_v g]μν = g_μν,κ vκ + g_κν ∂μ vκ + g_μκ ∂ν vκ. (2.4.8)

For a general r-fold contravariant, s-fold covariant tensor with components T^{μ1...μr}_{ν1...νs} the Lie-derivative is given by (L_v T)^{μ1...μr}_{ν1...νs} = T^{μ1...μr}_{ν1...νs,κ} vκ - T^{κ...μr}_{ν1...νs} ∂κ vμ1 - ... (all upper indices)

+ T^{μ1...μr}_{κ...νs} ∂ν1 vκ + ... (all lower indices). (2.4.9)

## 2.5 The Covariant Derivative

In the following we will assume the scalar-, vector- or tensor-fields to be differentiable over a certain part of the underlying manifold M. Let ϕ be a scalar field over M. Then ϕ ≡ ∂μ ϕ = Bμ is a covariant tensor field, since a coordinate transformation xμ → x'ν leads to B'_ν = ∂/∂x'ν ϕ = (∂xμ/∂x'ν) (∂ϕ/∂xμ) = (∂xμ/∂x'ν) Bμ.

The partial derivative acting on a scalar field yields a tensor field. This is, however, not the case if the partial derivative is applied to vector- and tensor fields of higher ranks. E.g., for a contravariant vector field we get dA'^ν = ∂x'^ν/∂xμ dAμ = (∂²x'^ν/∂xμ∂xσ) dxσ Aμ + (∂x'^ν/∂xμ) dAμ, i.e., only under linear transformations dAμ transforms as a tensor.

We now will introduce a derivative for tensor fields that leads to new tensors. To this end we consider again a contravariant differentiable vector field Aμ along some curve γ(λ) (Fig. 2.3). First we will consider such a vector field in some Euclidean space with Cartesian coordinates. Let us first consider a vector field with constant components in these coordinates, i.e., dAμ(xν) = 0. Now we switch to new coordinates x'^ν, where A'^ν = (∂x'^ν/∂xμ) Aμ will no longer be constant in general. Along γ(λ) A'^ν will vary according to dA'^ν/dλ = (∂²x'^ν/∂xμ∂xσ) (dxσ/dλ) Aμ + (∂x'^ν/∂xμ) (dAμ/dλ)

= (∂²x'^ν/∂xμ∂xσ) (∂xσ/∂x'^ρ) (dx'^ρ/dλ) A'^τ (∂xμ/∂x'^τ)

= -Γ^ν_{ρτ} A'^τ (dx'^ρ/dλ) (2.5.1)

with Γ^ν_{ρτ} = - (∂²x'^ν/∂xα∂xβ) (∂xα/∂x'^ρ) (∂xβ/∂x'^τ). (2.5.2)

That means that infinitesimal changes of Aμ along the curve γ(λ) are bi-linear in dxρ and Aμ itself. This form of Γ^ν_{ρτ} is valid only for our special case. For arbitrary vector fields we now write δAν = -Γ^ν_{ρτ} dxρ Aτ (2.5.3)

with at first arbitrary coefficients Γ^ν_{ρτ}. We will consider (2.5.3) as a rule for a parallel displacement of Aν from xμ(λ) to the neighboring point xμ(λ+dλ) = xμ + dxμ, i.e., Aν → A̅ν = Aν + δAν (Fig. 2.4).

Definition The quantities Γ^ν_{ρτ} are called affine connections if D Aν/Dλ = lim_{Δλ→0} (Aν(λ+Δλ) - A̅ν(λ, λ+Δλ))/Δλ (2.5.4)

is a tensor. In that case D Aν/Dλ is called the covariant derivative of Aν along γ(λ). We have D Aν = Aν|x+dx - A̅ν|x = Aν(xμ) + dAν - (Aν(xμ) - Γ^ν_{ρτ} Aτ dxρ)

= dAν + Γ^ν_{ρτ} Aτ dxρ and we see that for our special case above (Euclidean space, constant vector-components in Cartesian coordinates) the covariant derivative of Aν vanishes, if the affine connections Γ^ν_{ρτ} are given by (2.5.2).

Next we come to the transformation rule for affine connections. Let Γ^ν_{ρτ} be affine connections, then D Aν transforms as a vector and also A̅(xμ+dxμ), i.e., A̅'^ν(x'^ν + dx'^ν) = (∂x'^ν/∂ν)|_{x+dx} A̅μ(xν+dxν)

= (∂x'^ν/∂xμ + (∂²x'^ν/∂xμ∂xσ) dxσ) A̅μ(xμ+dxμ)

or A'^ν - Γ'^ν_{ρτ} dx'^ρ A'^τ = (∂x'^ν/∂xμ + (∂²x'^ν/∂xμ∂xσ) dxσ) (Aμ - Γ^μ_{αβ} dxα Aβ) (2.5.5)

at the place defined by xμ. Therefore, -Γ'^ν_{ρτ} dx'^ρ A'^τ = -Γ^μ_{αβ} (∂x'^ν/∂xμ - (∂²x'^ν/∂xα∂xβ)) dxα Aβ.

From dxα Aβ = (∂xα/∂x'^ρ) (∂xβ/∂x'^τ) dx'^ρ A'^τ we finally get the transformation rule for affine connections in the form Γ'^ν_{ρτ} = (∂x'^ν/∂xμ) (∂xα/∂x'^ρ) (∂xβ/∂x'^τ) Γ^μ_{αβ} - (∂²x'^ν/∂xα∂xβ) (∂xα/∂x'^ρ) (∂xβ/∂x'^τ) (2.5.6)

that reduces to (2.5.2) for the case Γ^μ_{αβ} = 0. One writes D Aν = dAν + Γ^ν_{ρτ} Aτ dxρ = Aν;ρ dxρ (2.5.7)

where Aν;ρ ≡ ∂ρ Aν + Γ^ν_{ρτ} Aτ (2.5.8)

is called the covariant derivative of Aν with respect to xρ. It generalizes the partial derivative, ∂ρ Aν ≡ ∂Aν/∂xρ.

Let Aν and Bμν be differentiable vector fields. Then AνB_ν is a scalar field and, therefore, δ(AνB_ν) = 0 = (δAν)B_ν + Aν(δB_ν) = (-Γ^ν_{ρτ} dxρ Aτ)B_ν + Aν(δB_ν)

or Aν(δB_ν) = Γ^ν_{ρτ} dxρ Aτ B_ν = (Γ^τ_{ρν} dxρ B_τ) Aν.

From this we derive δB_ν = +Γ^τ_{ρν} dxρ B_τ and D B_ν = B_ν;ρ dxρ, (2.5.9)

where B_ν;ρ ≡ ∂ρ B_ν - Γ^τ_{ρν} B_τ (2.5.10)

is the covariant derivative of B with respect to xρ. In a similar way the covariant derivative of an arbitrary tensor field is defined: T^{μ1...μr}_{ν1...νs};ρ = ∂ρ T^{μ1...μr}_{ν1...νs} + Γ^{μ1}_{ρκ} T^{κ...μr}_{ν1...νs} + ... + Γ^{μr}_{ρκ} T^{μ1...κ}_{ν1...νs} (2.5.11)

- Γ^{κ}_{ρν1} T^{μ1...μr}_{κ...νs} - ... - Γ^{κ}_{ρνs} T^{μ1...μr}_{ν1...κ}.

## 2.6 Geodesics

Let γ(λ) be some curve in M. The covariant derivative of some contravariant vector field Aν along γ is given by D Aν/Dλ = (∂ρ Aν + Γ^ν_{ρτ} Aτ) uρ where uρ ≡ dxρ/dλ (2.6.1)

is the tangent vector field to the curve γ(λ).

Definition The vector field Aν is called parallel along γ(λ) if D Aν/Dλ = dAν/dλ + Γ^ν_{ρτ} uρ Aτ = 0. (2.6.2)

A curve γ(λ) is called a geodesic if D uν/Dλ = h(λ) uν (2.6.3)

with uν ≡ dxν/dλ. Hence, a geodesic is a curve where the tangent vectors are parallel to themselves. The equation for a geodesic, therefore, reads d²xν/dλ² + Γ^ν_{ρτ} (dxρ/dλ) (dxτ/dλ) = h(λ) dxν/dλ. (2.6.4)

In general one can eliminate the right hand side of this equation by a suitable choice of the curve-parameter. Such a parameter is called affine. With respect to an affine parameter κ the geodetic-equation takes the form d²xν/dκ² + Γ^ν_{ρτ} (dxρ/dκ) (dxτ/dκ) = 0. (2.6.5)

## 2.7 Curvature- and Ricci Tensor

The curvature of a manifold is usually introduced by means of parallel transport of a vector around a closed curve. Such a situation is depicted in Fig. 2.5, where we start at the north pole of a sphere and consider the tangent vector t₁ to some meridian running through the pole and the equator. Since a meridian is a geodesic (see Example 2.2 below) parallel displacement of t₁ leads to the tangent vector e₁ at the point E₁ of the equator. Parallel transport along the equator to E₂ leads to e₂ and finally going back to the pole by parallel displacement along the meridian running through E₂ we end up with a vector t₂ that differs from t₁ because of the curvature of the sphere. For convenience let us consider the parallel transport of a covariant vector A along some curve xμ(λ). The changes of the coordinate components of A are then determined by (2.6.2)

0 = A_α;μ (dxμ/dλ) = (A_α,μ - Γ^β_{αμ} A_β) (dxμ/dλ)

= dA_α/dλ - Γ^β_{αμ} A_β (dxμ/dλ)

or ΔA_α = ∫ Γ^β_{αμ} A_β (dxμ/dλ) dλ. (2.7.1)

We now assume the curve γ given by xμ(λ) to be closed, i.e., xμ(λ₁) = xμ(λ₀) for some suitably chosen value of λ₁, given λ₀. One might then consider γ as the edge of some two-dimensional surface S, and divide S into small cells bounded by little closed curves γₙ (Weinberg 1972). From Fig. 2.6 it becomes clear that ΔA[γ] = Σ_n ΔA[γₙ].

In other words it is sufficient to consider the parallel transport of A around some sufficiently small surface. Let Xσ ≡ xσ(λ₀), e.g., the starting point of our route and xσ ≡ xσ(λ). We now will compute the change in A to second order in xσ - Xσ and since the integral over dxμ is of first order we need the changes of Γ^β_{αμ} and A_β only to first order. To first order in xσ - Xσ we get Γ^β_{αμ}(x) = Γ^β_{αμ}(X) + (xσ - Xσ) ∂σ Γ^β_{αμ}(X) + ...

β(X). (2.7.2)

αμ αμ ∂Xσ αμ Similarly, dropping all terms of second order in x − X one has from (2.7.1)

Aα(λ) = Aα(λ0) + (cid:6)β(X)Aβ(λ0)(xμ(λ) − Xμ). (2.7.3)

Inserting the last two relations into (2.7.1) one obtains an expression valid to second order in x − X: λ ∂ Aα(λ) = Aα(λ0) + (cid:6)β(X) + (xσ(λ) − Xσ) (cid:6)β(X)

λ0 αμ αμ ∂Xσ dxμ × Aβ(λ0) + (cid:6) ρβσ(X)Aρ(λ0)(xσ(λ) − Xσ) dλ dλ λ dxμ = Aα(λ0) + (cid:6)β(X)Aβ(λ0) dλ λ0 αμ β 0 dλ ∂ λ dxμ + (cid:6)ρ(X) + (cid:6) ρ(X)(cid:6)β(X) Aρ(λ0) (xσ(λ) − Xσ) dλ.

∂Xσ αμ βσ αμ ρ 0 dλ λ0 For a parallel transport around some small closed curve with xμ(λ0) = xμ(λ1)

obviously λ1 dxμ dλ = 0 dλ λ0 and the total change of A is of second order in x − X proportional to the surface element spanned by the small curve γ : ΔAα ≡ Aα(λ1) − Aα(λ0) (2.7.4)

= (cid:6)ρ(X) + (cid:6) ρ(X)(cid:6)β(X) Aρ(λ0) xσdxμ.

∂Xσ αμ βσ αμ ρ 0 The integral appearing on the right hand side of this equation can be interpreted as surface element ΔSσμ enclosed by xμ(λ) which is antisymmetric in σ and μ since λ1 d λ1 dxσ ΔSσμ = xσdxμ = (xσxμ)dλ − xμ dλ dλ dλ λ0 λ0 = − xμdxσ = −ΔSμσ .

For that reason we can replace the coefficient of ΔSσμ on the right hand side of (2.7.4) by its antisymmetric part and write ΔAα = Rραμσ ΔSμσ , (2.7.5)

where Rραμσ = (cid:6)ρασ,μ − (cid:6)ραμ,σ + (cid:6)βμ (cid:6)ρασ − (cid:6)βσ (cid:6)ραμ (2.7.6)

is called the curvature tensor. From its definition we see that the curvature tensor is antisymmetric in the last pair of indices: Rμνλσ = −Rμνσλ . (2.7.7)

Exercise 2.3 Proof by direct calculation that for any vector fields Aρ and A the following relations holds Aρ;σμ − Aρ;μσ = + R α ρ μσ Aα. (2.7.8)

and Aρ;σμ − Aρ;μσ = − R ρ α μσ Aα. (2.7.9)

Proof of (2.7.8): We have: Aρ;σ = Aρ,σ + (cid:6)σνρ Aν ≡ T ρσ, where T is a tensor. Therefore; Aρ;σμ = T ρσ;μ = T ρσ,μ + (cid:6)μρα T σα − (cid:6)μασ T αρ (2.7.10)

= (Aρ,σ + Aν (cid:6)ρσν) ,μ + (Aα,σ + Aν (cid:6)ασν) (cid:6)μρα − (Aρ,α + Aν (cid:6)ραν) (cid:6)μασ.

Using (2.7.10) relation (2.7.8) can be shown directly.

The second Bianchi identities are fundamental relations for the curvature tensor. They read: Rμνλσ;κ + Rμνκλ;σ + Rμνσκ;λ = 0. (2.7.11)

The proof of the second Bianchi identities (2.7.11) is especially simple if special coordinates are introduced at some arbitrary point P of the manifold: Riemann normal coordinates (see e.g., Sect. 11.6 in Misner et al. 1973) that in a 4-dimensional space-time are related with local inertial coordinates of some freely falling observer. In such coordinates the affine connections (cid:6) vanish at P, i.e., in Riemann normal coordinates (cid:6) νλμ (P) = 0 (2.7.12)

and derivatives thereof are given by the components of the curvature tensor (more about normal coordinates are presented in Sect. 5.6 where the manifold is assumed to have a metric and the set of basis vectors at a certain point of the manifold is chosen as orthonormal tetrad. The corresponding coordinates will then be called ‘tetrad-induced’). In Exercise 2.4 one proofs that the second Bianchi identities are true at some point P in Riemann normal coordinates. But, since the left hand side of these identities is a tensor the relations are true in any suitable coordinate system and at every point of the manifold.

Exercise 2.4 Proof by direct calculation the (second) Bianchi-identity by using Riemann normal coordinates at some point P.

Proof Using (2.7.12) the components of the curvature tensor are given by: Rμνλσ = (cid:6) μνσ,λ − (cid:6) μνλ,σ (2.7.13)

so that Rμνλσ;κ = Rμνλσ,κ = (cid:6) σνλ,κσ − (cid:6) λνσ,κλ Rμνκλ;σ = Rμνκλ,σ = (cid:6) λνκ,σλ − (cid:6) κνλ,σκ Rμνσκ;λ = Rμνσκ,λ = (cid:6) ν μ κ,σλ − (cid:6) ν μ σ,κλ .

Summing up the left hand sides, therefore, gives zero.

An object that will play an important role in the following is the Ricci tensor. The Ricci tensor Rμν is defined by Rμν ≡ Rσμσν = (cid:6) σν,μ − (cid:6) σμ,ν + (cid:6) κν (cid:6) σμ − (cid:6) σκ (cid:6) κν . (2.7.14)

## 2.8 The Metric Tensor

The geometry of a manifold is locally described by the metric tensor gμν. Consider two points P1 and P2 in the Euclidean 3-space. The distance Δs between the two points, according to the Pythagorean theorem, is given by (Fig. 2.7): (Δs)2 = (Δx)2 + (Δy)2 + (Δz)2 with Δx = x2 − x1 etc. Infinitesimally we write this as ds2 = dx2 + dy2 + dz2 (2.8.1)

or generally ds2 = gμν dxμdxν. (2.8.2)

gμν is called the metric tensor. Since ds2 has to be a coordinate independent object gμν is a two-fold covariant tensor. In our example gμν is given by gμν = ⎛ ⎞ 1 0 0 ⎝ 0 1 0 ⎠ ≡ δμν .

0 0 1 Since ds2 should be independent of the coordinates used and the transformation rule (2.2.5) for differentials the metric tensor gμν transforms according to gμν' = gαβ ∂xα ∂xβ ∂x'μ ∂x'ν . (2.8.3)

Since we know how the differentials dx, dy and dz in (2.8.1) transform into dr, dθ and dφ (relations (2.2.4)) we find for our Euclidean 3-space ds2 = dx2 + dy2 + dz2 = dr2 + r2(dθ2 + sin2θ dφ2). (2.8.4)

Thus, with respect to x1 = r, x2 = θ, x3 = φ the nonvanishing components of the metric tensor read: g11 = 1, g22 = gθθ = r2, g33 = gφφ = r2sin2θ. (2.8.5)

So, in general the metric tensor depends upon coordinates. The inverse metric tensor is denoted by gμν, i.e., gμν gλν = δ μ λ ≡ δμλ = { 1 if μ = λ 0 otherwise.

(2.8.6)

For our Euclidean 3-space gμν = ⎛ ⎞ 1 0 0 ⎝ 0 1 0 ⎠ (2.8.7)

0 0 1 in Cartesian coordinates and gμν = ⎛ ⎞ 1 0 0 ⎝ 0 r−2 0 ⎠ , (2.8.8)

0 0 r−2sin−2θ in spherical coordinates, i.e., the non-vanishing components read g11 = 1, g22 = r−2, g33 = r−2sin−2θ. (2.8.9)

Definition (Raising and Lowering of Indices) If a manifold is endowed with a metric tensor (and its inverse), we can associate with each contravariant tensor-index a corresponding covariant one and vise versa according to Aμ = gμν Aν ; Bμ = gμν Bν ; Tμστ = gμν T νστ etc.

Such process behind such mappings is called the raising and lowering of indices.

The metric tensor defines a scalar-product (A,B) of two vectors Aμ and Bν according to (A,B) ≡ gμν AμBν. (2.8.10)

If gμν is positive definite, i.e., if (A,B)| ∈ R+, ∀p ∈ M, A,B ≠ 0, gμν is called a Riemannian metric and (M,g) a Riemannian space. If (A,B) can also attain negative values one speaks of a pseudo-Riemannian metric and pseudo-Riemannian space.

## 2.9 Metric Connections

An affine connection (cid:6) μνσ is called metric, if the covariant derivative of the metric tensor vanishes, i.e., gμν;λ = gμν,λ − (cid:6) μ σλ gσν − (cid:6) ν σλ gσμ = 0. (2.9.1)

Metric connections conserve the scalar product of two vector-fields that are both parallel along some curve γ(λ). Let Aμ and Bν be vector-fields along γ, i.e., DAμ DBν = = 0.

Dλ Dλ The variation of (A,B) along γ is then given by d D Dg dxσ [gμνAμBν] = [gμνAμBν] = μν AμBν = gμν;σ AμBν dλ Dλ Dλ dλ and vanishes for metric connections. Especially the norm of a vector field parallel along γ is constant for a metric connection. Such a norm can be associated with natural constants such as the rest-mass of elementary particles etc. For that reason in the following we will always assume the connection to be metric if relativity comes into play.

Theorem 2.1 On a pseudo-Riemannian manifold (M,g) there is only one affine connection that is metric, i.e., condition (2.9.1) fixes the connection uniquely which in this case is given by the Christoffel-symbols (cid:6) μνλ = gμσ (g σν,λ + g σλ,ν − g νλ,σ ). (2.9.2)

Proof From (2.9.1) we get 0 = gμν;λ = gμν,λ − gσν (cid:6) μ σλ − gσμ (cid:6) ν σλ ≡ gμν,λ − (cid:6) ν|μλ − (cid:6) μ|νλ and therefore gμν,λ = +(cid:6) ν|μλ + (cid:6) μ|νλ gλμ,ν = +(cid:6) μ|λν + (cid:6) λ|μν −gνλ,μ = −(cid:6) λ|νμ − (cid:6) ν|λμ .

Adding these three equations leads us to (cid:6) μ|νλ = (gμν,λ + gμλ,ν − gνλ,μ ).

Raising the first index of (cid:6) μ|νλ then leads us to the Christoffel-symbols from (2.9.2).

Lemma 2.1 For metric connections the geodesics are curves of maximal (minimal) length between two points P1 and P2. Consider two fixed points P1 and P2 and all kinds of curves xμ(λ), where λ is some curve parameter, that connect these two points. If the connection is metric the geodesic connecting these two points will obey a relation of the form P2 dxμdxν δ gμν dλ = 0. (2.9.3)

dλ dλ P1 This relation can be understood in the following way: let x (λ) be the desired geodesic. One then considers small variations of that curve, i.e., curves of the form x μ (λ) + δxμ(λ) with fixed endpoints: δxμ(P1) = δxμ(P2) = 0.

With the rule ∂A δA(xμ) = δxμ ≡ A,μ δxμ (2.9.4)

∂xμ (i.e., the comma denotes a partial derivative) for any differentiable function A(xμ) and the notation dxμ df x˙μ ≡ ,(f)˙ ≡ dλ dλ we get ∫ 0 = (δgμν x˙μx˙ν + 2gμν x˙μ δx˙ν) dλ ∫ = (gμν,ρ δxρ x˙μx˙ν + 2gμρ x˙μ (δxρ)˙) dλ ∫ = (gμν,ρ x˙μx˙ν − (2gμρ x˙μ)˙) δxρ dλ ∫ = −2 (gμρ x¨μ + g˙μρ x˙μ − gμν,ρ x˙μx˙ν) δxρ dλ ∫ = −2 (gμρ x¨μ + gμρ,ν x˙νx˙μ − gμν,ρ x˙μx˙ν) δxρ dλ ∫ = −2 (gμρ x¨μ + (gμρ,ν + gνρ,μ − gμν,ρ) x˙μx˙ν) δxρ dλ ∫ = −2 (gαρ x¨α + gασ(gσν,μ + gμσ,ν − gμν,σ) x˙μx˙ν) δxρ dλ.

In the first line only the chain rule was used, in the second the variation of gμν was performed according to the rule (2.9.4), the 3rd line involved an integration by parts, in the 4th line a factor of 2 was taken in front of the integral and a dot-derivative was written out, the dot-derivative of gμν was written out in the 5th line, the middle-term in the 5th line was written symmetrically with respect to the indices μ and ν in the 6th line, and finally a factor gαρ was taken out of the bracket in the last line. I.e., the equation for the curve with extremal length reads x¨α + (cid:6)α μν x˙μx˙ν = 0, (2.9.5)

where (cid:6)α μν are just the Christoffel-symbols from (2.9.2).

As an example we compute the Christoffel symbols for the Euclidean 3-space in spherical coordinates x1 = r, x2 = θ, x3 = φ.

The components of the metric tensor are given by (2.8.5) and (2.8.9). From this we find e.g., (cid:6)2 = g22 (g22,1 + g12,2 − g22,1) = − sinθ cos θ.

Similarly, one gets for the non-vanishing Christoffel symbols: Γ^1_{22} = -r;  Γ^1_{33} = -r sin^2θ Γ^2_{21} = Γ^2_{12} = 1/r;  Γ^2_{33} = -sinθ cosθ (2.9.6)

Γ^3_{23} = Γ^3_{32} = cotθ;  Γ^3_{31} = Γ^3_{13} = 1/r

Example 2.2 As another example we consider the geodesics on a unit sphere (Fig. 2.8). As coordinates we choose usual spherical coordinates x^1 = θ, x^2 = φ with length element ds^2 = dθ^2 + sin^2θ dφ^2. (2.9.7)

For the Christoffel symbols we get from (2.9.6)

Γ^1_{22} = -sinθ cosθ;  Γ^2_{12} = Γ^2_{21} = cotθ.

For the geodesic equation one finds e.g., θ̈ + Γ^1_{μν} ẋ^μ ẋ^ν = 0 and the indices μ and ν both have to take the value 2. Therefore, θ̈ - sinθ cosθ φ̇^2 = 0. (2.9.8)

Similarly one finds φ̈ + 2 cotθ φ̇ θ̇ = 0. (2.9.9)

E.g., the geodesics through the poles θ^+ = 0, θ^- = π are given by the meridians φ = const., θ = λ, λ ∈ [0, π].

Fig. 2.8 Geodesics on the unit sphere running through the poles

2.9.1 Riemann Tensor and Its Symmetries

If the curvature tensor results from the Christoffel symbols of some metric tensor it is called Riemann tensor. The Riemann tensor has the following symmetries: R_{μνλσ} = -R_{νμλσ} R_{μνλσ} = -R_{μνσλ} (2.9.10)

R_{μνλσ} = +R_{λσμν}.

First Bianchi-identities (cyclic identities): R^μ_{νλσ} + R^μ_{σνλ} + R^μ_{λσν} = 0. (2.9.11)

The second Bianchi-identities, relation (2.7.11)

R^μ_{νλσ;κ} + R^μ_{νκλ;σ} + R^μ_{νσκ;λ} ≡ R^μ_{ν[λσ;κ]} = 0 (2.9.12)

have already been discussed in Exercise 2.4.

Exercise 2.5 Proof that the first Bianchi identities can be written in the form R^μ_{ν[λσ]} = 0. (2.9.13)

Proof Using the definition of R^μ_{ν[λσ]} and the relation (2.7.7) we get R^μ_{ν[λσ]} = (R^μ_{νλσ} + R^μ_{λσν} + R^μ_{σνλ}) = 0. (2.9.14)

Exercise 2.6 Proof the symmetries (2.9.10) of the Riemann tensor.

Exercise 2.7 Proof the first Bianchi-identity (2.9.11) using (2.9.14) and the condition Γ^μ_{νλ} = Γ^μ_{λν}.

Proof 3R^μ_{ν[λσ]} = Γ^μ_{νλ,σ} - Γ^μ_{νσ,λ} + Γ^μ_{αλ} Γ^α_{νσ} - Γ^μ_{ασ} Γ^α_{νλ} + Γ^μ_{λν,σ} - Γ^μ_{λσ,ν} + Γ^μ_{ασ} Γ^α_{λν} - Γ^μ_{αν} Γ^α_{λσ} + Γ^μ_{σλ,ν} - Γ^μ_{σν,λ} + Γ^μ_{αν} Γ^α_{σλ} - Γ^μ_{αλ} Γ^α_{σν} = (Γ^μ_{λν} - Γ^μ_{νλ})_{,σ} + (Γ^μ_{νσ} - Γ^μ_{σν})_{,λ} + (Γ^μ_{σλ} - Γ^μ_{λσ})_{,ν} + Γ^μ_{αλ} (Γ^α_{νσ} - Γ^α_{σν}) + Γ^μ_{ασ} (Γ^α_{λν} - Γ^α_{νλ}) + Γ^μ_{αν} (Γ^α_{σλ} - Γ^α_{λσ})

= 0.

The Einstein tensor G_{μν} is defined by G_{μν} ≡ R_{μν} - g_{μν} R, (2.9.15)

where R ≡ g^{μν} R_{μν} (2.9.16)

is the curvature scalar.

Exercise 2.8 Proof that the Einstein tensor is divergenceless, i.e.

G^μ_{ν;μ} = 0. (2.9.17)

Show that (2.9.17) is equivalent to the second Bianchi identity (2.7.11).

Exercise 2.9 Calculate the Riemann curvature tensor, the Ricci tensor, and the curvature scalar for a 2-sphere of radius a.

Solution The metric is given by (2.8.5) with dr^2 = 0, r = a and the Christoffel symbols can be taken from (2.9.6). Direct calculation gives R^1_{212} = R^θ_{φθφ} = ∂Γ^1_{22}/∂θ - ∂Γ^1_{21}/∂φ + Γ^1_{α1} Γ^α_{22} - Γ^1_{α2} Γ^α_{21} = ∂Γ^1_{22}/∂θ - Γ^1_{22} Γ^2_{21} = sin^2θ - cos^2θ + sinθ cosθ cotθ hence R^1_{212} = sin^2θ. (2.9.18)

Similarly we find R^2_{121} = 1. (2.9.19)

From this we find the components of the Ricci tensor R_{11} = 1, R_{22} = sin^2θ. (2.9.20)

Since g^{11} = a^{-2} and g^{22} = a^{-2} sin^{-2}θ the curvature scalar reads R = 2/a^2. (2.9.21)

Often a useful measure for the local curvature is the Kretschmann-scalar K. It is defined by K ≡ R_{μνλσ} R^{μνλσ}. (2.9.22)

## 2.10 The Levi-Civita Symbol and Tensor

The Levi-Civita symbol [μ_1 μ_2 ... μ_n] is defined to be completely antisymmetric, i.e., it changes sign when two indices are exchanged and [01...(n-1)] = +1 or [12...n] = +1. (2.10.1)

E.g., [0132] = -1, [321] = -1. In three dimensions one usually writes [ijk] ≡ ε_{ijk}.

The Levi-Civita symbol is especially useful when dealing with determinants. Let M^μ_{ν} be some n×n matrix, |M| ≡ Det(M), then [ν_1 ν_2 ... ν_n] |M| = M^{μ_1}_{ν_1} ··· M^{μ_n}_{ν_n} [μ_1 ... μ_n]. (2.10.2)

Think of [μ_1 ... μ_n] as being the coordinates of some geometrical object in flat R^n in some Cartesian coordinate system x^μ. We then consider a coordinate transformation x^μ → x'^ν and put M^μ_{ν} ≡ ∂x^μ/∂x'^ν.

Then from (2.10.2) we get [ν'_1 ... ν'_n] |∂x/∂x'| = (∂x'^{ν_1}/∂x^{μ_1}) ··· (∂x'^{ν_n}/∂x^{μ_n}) [μ_1 ... μ_n], (2.10.3)

where |∂x/∂x'| is the Jacobian of the transformation x' → x. We get [ν'_1 ... ν'_n] = |∂x'/∂x| (∂x'^{ν_1}/∂x^{μ_1}) ··· (∂x'^{ν_n}/∂x^{μ_n}) [μ_1 ... μ_n], (2.10.4)

since |∂x/∂x'| = |∂x'/∂x|^{-1}. (2.10.5)

Let J ≡ |∂x'/∂x| (2.10.6)

be the Jacobian of the transformation x → x', then a quantity that transforms as T'^{ν_1...ν_n} = J^m (∂x'^{ν_1}/∂x^{μ_1}) ··· (∂x'^{ν_n}/∂x^{μ_n}) T^{μ_1...μ_n} (2.10.7)

is called a tensor-density of weight m. From (2.10.4) we see that the Levi-Civita symbol can be considered as a tensor-density of weight +1. As an example consider the volume element d^n x that transforms as d^n x' = |∂x'/∂x| d^n x, (2.10.8)

hence it is a scalar density of weight +1.

Let us consider the determinant of the g_{μν}, g ≡ Det(g_{μν}) < 0 in a 4-dimensional spacetime manifold. From g'_{μν} = g_{ρσ} (∂x^ρ/∂x'^μ)(∂x^σ/∂x'^ν)

we get g' = |∂x'/∂x|^2 g. (2.10.9)

Thus g is a scalar density of weight -2 and we can use powers of √-g to convert each tensor density into a real tensor. E.g., √-g d^n x is an invariant volume element.

We define the Levi-Civita tensor generally by ε_{μ_1...μ_n} ≡ +√-g [μ_1 ... μ_n]. (2.10.10)

This implies that in a 4-dimensional spacetime ε_{0123} = +√-g; (2.10.11)

(Note, that Weinberg (1972) is using a different sign convention). We can then raise the indices with the inverse metric tensor ε^{μ_1...μ_n} = g^{μ_1 ν_1} ··· g^{μ_n ν_n} ε_{ν_1...ν_n} = sgn(g)/√|g| [μ_1 ... μ_n]. (2.10.12)

In a 4-dimensional spacetime ε^{μ_1...μ_4} = -√-g^{-1} ε_{μ_1...μ_4}. (2.10.13)

## 2.11 Symmetric Spaces

A space is called symmetric if the metric tensor is form-invariant under the flow of a vector-field ξ. For Eq. (2.4.7) form-invariance implies that g'_{μν}(x) = g_{μν}(x) or [L_ξ g]_{μν} = 0. (2.11.1)

The last equation can be re-written in the form 0 = g_{μν,κ} (g^{κσ} ξ_σ) + g_{μν} (g^{κσ} ξ_σ)_{,μ} + g_{κν} (g^{κσ} ξ_σ)_{,μ} + ... [Note: The derivation in the original text appears garbled here, but the conclusion is standard]

= ξ_{μ;ν} + ξ_{ν;μ} = 0. (2.11.2)

A vector-field ξ satisfying this Killing equation is called Killing vector-field. Each Killing vector-field describes a symmetry of the manifold. In that case the Lie-derivative of the metric tensor with respect to the Killing vector-field vanishes.

As an example we consider 3-dimensional Euclidean space with Cartesian coordinates where the Killing equation takes the form ξ_{i,j} + ξ_{j,i} = 0. (2.11.3)

One solution to this equation reads: ξ_i = const. that describes an infinitesimal translation of the form x → x + δξ. A second solution reads ξ_i = r_{ij} x^j (2.11.4)

with r_{ij} = -r_{ji} that describes an infinitesimal rotation about x=0.

2.11.1 Maximally Symmetric Spaces

A set of ξ^{(n)}_μ, n=1,...,N of N Killing vector fields is said to be linearly dependent if there are constants c_n such that c_n ξ^{(n)}_μ = 0, (2.11.5)

otherwise the ξ^{(n)}_μ's are said to be linearly independent. A space of dimension N is called maximally symmetric if it has N(N+1)/2 independent Killing vector fields.

Lemma 2.2 An N-dimensional space has at most N(N+1)/2 independent Killing vector fields.

Proof The definition of the Riemann curvature tensor and the first Bianchi-identity (2.9.11) imply that (e.g., Weinberg 1972; (13.1.8))

ξ^σ_{;ρμ} - ξ^σ_{;μρ} + ξ^μ_{;σρ} - ξ^μ_{;ρσ} + ξ^ρ_{;μσ} - ξ^ρ_{;σμ} = 0 (2.11.6)

for any vector field ξ^μ. From the Killing equation, ξ^μ_{;ν} = -ξ^ν_{;μ} one infers that ξ^ρ_{;μσ} = -ξ^μ_{;ρσ} etc. so that for a Killing vector field ξ^σ_{;ρμ} - ξ^σ_{;μρ} - ξ^μ_{;ρσ} = 0 (2.11.7)

and using relation (2.7.9), ξ^μ_{;ρσ} = R^σ_{λ ρμ} ξ^λ. (2.11.8)

Similarly all higher covariant derivatives of ξ at some point X can be derived from ξ^λ and ξ^λ_{;ν} at X. Therefore, ξ^λ(X) and ξ^λ_{;ν}(X) completely determine ξ^λ(x) if x is in a certain neighborhood of X. In some N-dimensional space ξ^λ has N independent components and ξ^λ_{;ν}, because of the Killing-equation, has N(N-1)/2 independent quantities which gives a total of maximally N(N+1)/2 independent Killing vector fields.

Lemma 2.3 If an N-dimensional space is maximally symmetric, then R_{μν} = (N-1)k g_{μν} (2.11.9)

R_{μνλσ} = k(g_{σν} g_{μλ} - g_{λν} g_{μσ}) (2.11.10)

where the curvature constant k is defined by R = R^{σ}_{σ} ≡ N(N-1)k. (2.11.11)

The proof is left as an exercise (see e.g. Weinberg 1972).

The curvature constant k has the dimension 1/length^2. As we have seen the curvature scalar for a two-sphere of radius r_0 is given by R = 2/r_0^2 so that k = r_0^{-2}.

2.11.2 Maximally Symmetric 3-Spaces

A 3-space is maximally symmetric if it has a total of six independent Killing vector fields. Clearly the flat Euclidean 3-space is maximally symmetric, but there are more 3-spaces with maximal symmetry. It is clear that such a 3-space is spherically symmetric so that in suitable spherical coordinates r, θ, φ the metric tensor takes the form ds^2 = e^{2β(r)} dr^2 + r^2 (dθ^2 + sin^2θ dφ^2). (2.11.12)

The non-vanishing components of the Ricci-tensor read (β'(r) ≡ dβ/dr): R_{rr} = β'(r)

R_{θθ} = e^{-2β(r)} (r β'(r) - 1) + 1 R_{φφ} = R_{θθ} sin^2θ. (2.11.13)

Using condition (2.11.9) for maximal symmetry, R_{ij} = 2k g_{ij}, one obtains e.g., β'(r) = e^{2β(r)} 2.12 GR Tensor 43 and thus β(r) = -½ ln(1 - k r^2). (2.11.14)

Thus in suitable coordinates the metric for a maximally symmetric 3-space takes the form ds^2 = dr^2/(1 - k r^2) + r^2 (dθ^2 + sin^2θ dφ^2). (2.11.15)

The case k = 0 is the flat Euclidean 3-space, if k > 0 the space has positive curvature describing a spherical closed space, if k < 0 the 3-space is called open.

## 2.12 GR Tensor

For the treatment of problems related with differential geometry the employment of a Computer Algebra System (CAS) such as REDUCE, MATHEMATICA or Maple is extremely useful.

e is useful. A very efficient tool for dealing with differential geometrical objects is a package called GRTensor. It was developed by Peter Musgrave, Denis Pollney and Kayll Lake from the Queen’s University at Kingston, Ontario in Canada. Originally GRTensor was a standard Maple package. GRTensorII version 1.50 was developed in 1994–1999 and updated by GRTensorIII to work efficiently also with new version of Maple (meanwhile it is also available for MATHEMATICA). GRTensorIII software is freely available with documentation and examples from https://github.com/grtensor/grtensor. If one has downloaded the GRTensorIII Maple package one can start with a new Maple file where you have to define the link to the library of GRTensorIII: libname:=libname, “libpath”: where ‘libpath’ could read, e.g.: D:\\Maple\\grtensor. If one wants to have access to the library of metrics one also has to define the corresponding link: grOptionMetricPath:= “metricpath”: where ‘metricpath’ could read D:\\Maple\\grtensor\\metrics.

As an illustration let us compute differential geometrical objects such as the Ricci tensor R_μν, the curvature tensor R_μνλσ, the Christoffel symbols Γ^ν_ρσ and the Kretschmann-scalar K for the Schwarzschild metric discussed in Chap. 6 in standard coordinates (t, r, θ, φ). To this end we first produce an ASCII file with the name ‘SchwarzSelf.mpl’ that reads: Ndim_ := 4: X1_ := r: X2_ := theta: X3_ := phi: X4_ := t: complex_ := {}: g11_ := 1/(1-2*m/r): g22_ := r^2: g33_ := sin(theta)^2*r^2: g44_ := -(1 - 2*m/r): Info_:= `Schwarzschild-metric`:

A program that does the job could read: > ##################################################### > # The Schwarzschild metric > ##################################################### > restart: > ##################################################### > # define the path to the grtensor library > ##################################################### > libname := libname, “D:\\Maple\\grtensor”: > with(grtensor); > ##################################################### > # define the path to the library of metrics > ##################################################### > grOptionMetricPath := “D:\\Maple\\grtensor\\metrics”: > ##################################################### > # load your private file for the Schwarzschild metric > # in standard coordinates (r, theta, phi, t)

> ##################################################### > qload( SchwarzSelf ): > ##################################################### > # display the components of g_ab > ##################################################### > grdisplay(g(dn,dn)): > ##################################################### > # calculate and display the components of R_ab > grcalc( R(dn,dn)): > grdisplay( R(dn,dn) ): > ##################################################### > # calculate and display the components of R_abcd > grcalc( R(dn,dn,dn,dn) ): > grdisplay( R(dn,dn,dn,dn) ): > ##################################################### > # display the components of Chr_ab^c > grdisplay( Chr(dn,dn,up) ): > ##################################################### > # calculate and display the Kretschmann scalar K > ##################################################### > grcalc(RiemSq): > grdisplay(RiemSq): > #####################################################

## 3.1 Newtonian Theory of Gravity

Newton’s theory of gravity is based upon absolute time and space (the Newtonian space-time). According to Newton’s Philosophiae Naturalis Principia Mathematica (originally published in 1687 in Latin), absolute time and space respectively are independent aspects of objective reality: Absolute, true and mathematical time, of itself, and from its own nature flows equably without regard to anything external, and by another name is called duration: relative, apparent and common time, is some sensible and external measure of duration by the means of motion, which is commonly used instead of true time...

According to Newton, absolute time exists independently of any perceiver and progresses at a consistent pace throughout the universe. Also, space in the Newtonian framework has absolute character, in the sense that it regulates the inertial forces that appear if some observer is accelerated (or rotates) with respect to Newton’s absolute space, and that cannot be understood as arising from some kind of interaction with the direct physical neighbourhood (in this sense Newton’s theory is ‘non-relativistic’ but nevertheless can be formulated in a covariant manner). The absolute aspects of the Newtonian space-time lead to the globally determined bundle of inertial frames, where inertial forces are absent, and to the symmetries defined by the Galilean group.

The Newtonian gravitational field equation relates the matter density ρ as source to the curvature tensor of the Newtonian space-time. Basically, the curvature tensor describes the tidal forces, i.e., relative accelerations of neighbouring ‘particles’ are the outcome of gradiometric measurements. A convenient way to describe this curvature tensor is by means of a Newtonian potential U(t, x), where t refers to the time- and x to the space coordinates of a point in the Newtonian space-time manifold.

If one is interested in the problem of celestial mechanics, then in Newton’s theory the form of U outside of a body is of special interest. The definition of a body here presents no problem: a certain space-time region V, where ρ has compact support. Note, that in a non-linear theory of gravity (such as Einstein’s theory), where gravitational fields also act as field generating sources, the definition of a body presents a real problem. For celestial mechanical problems the potential U outside a body, that determines the global equations of motion is usually expanded in terms of multipole moments. Such expansions usually converge outside some coordinate sphere of radius R that completely contains the body under consideration. There are different multipole expansions of the external potential of a body, the most common one being the expansion of U_ext in terms of (scalar) spherical harmonics Y_lm. An equivalent multipole expansion employs Cartesian Symmetric and Trace-Free (STF) tensors, i.e, mathematical objects T_{k1...kl} with l different Cartesian indices running over three Cartesian values (1,2,3), symmetric in all l indices and completely trace-free, i.e., if two indexes are set equal and summed over all three components, the object vanishes. It turns out, that the set of (scalar) spherical harmonics is equivalent to the set n̂_L, where n_L = n_{k1}···n_{kl}, n_k = x^k/r (x^k denotes the three Cartesian coordinates (x,y,z) and r^2 = x^2 + y^2 + z^2) and the hat indicates that all traces have to be removed from n_L. The multipole expansion in terms of STF-tensors is especially useful for the derivation of equations of motion and in relativistic theories, where Lorentz-transformations (usually formulated in terms of Cartesian coordinates) play an important role.

Below we illustrate various aspects of Newtonian celestial mechanics that will be useful for later applications related with General Relativity. These parts are fairly standard; less common might be the derivation of perturbation equations by means of the (perturbed) integrals of motion of the Keplerian two-body problem. This part should also serve as a bridge between readers that are more familiar with Newtonian celestial mechanics and those familiar with certain aspects of relativity.

## 3.2 The Newtonian Space-Time

3.2.1 The Galilean Group In Newton’s theory there exists an absolute time coordinate t that is determined uniquely up to linear transformations (origin and unit)

t → a t + b; a ∈ R^+, b ∈ R.

and preferred Cartesian inertial coordinates x with the following property: consider a closed system of N ‘particles’ (bodies i = 1, ..., N) interacting via a 2-body force of the form F_ij = x_ij · f(|x_ij|); x_ij = x_i − x_j, obeying the law “actio = reactio”: F_ij = −F_ji.

then the equations of motion read: m_i ẍ_i = ∑_{j≠i} F_ij. (1 ≤ i ≤ N) (3.2.1)

Since (t, x_i) are inertial coordinates no inertial forces appear in the dynamical equation of motion. If x_i(t) represents a solution of (3.2.1) then also x_i′(±t + b) ≡ R x_i(t) + v t + d, where v and d are constants and R is a constant rotation matrix. Hence, if (t, x) and (t′, x′) are inertial coordinates they are related by a Galilean transformation t′ = t + b x′ = R x + v t + d (3.2.2)

or simply for R = δ_ij, v = v e_x, d = b = 0 t′ = t x′ = x + v t. (3.2.3)

3.2.2 Weak Equivalence Principle and Newtonian Theory of Gravity Let us write the Newtonian law for the free-fall of test bodies in some external gravitational field produced by some mass M in the form m_I ẍ = − G M m_I / r^2 * x/r ≡ m_G g. (3.2.4)

Here, m_I denotes the inertial mass of the test body, m_G its (passive) gravitational mass and g is the gravitational acceleration.

Weak Equivalence Principle The m_G/m_I-ratio is identical for all test bodies, independent of their shape and composition.

This implies, that we can take m_I = m_G (3.2.5)

and therefore we can cancel the two masses of the test body in (3.2.4). In this way we are led to the Law of Galileo: In the Newtonian space-time there exists a preferred class of reference frames with Galilean coordinates x^μ = (x^0, x^1, x^2, x^3) = (t, x) (3.2.6)

in which the dynamical law for free-fall takes the form ẍ = ∇U. (3.2.7)

Here, the gravitational potential U is a coordinate and frame dependent function. We can now write this as d^2 x^i / dλ^2 + Γ^i_{νσ} (dx^ν / dλ) (dx^σ / dλ) = 0; d^2 t / dλ^2 = 0 (3.2.8)

with Γ^i_{00} = − ∂U / ∂x^i ≡ U_{,i} and all other quantities Γ^μ_{νσ} = 0 in our Galilean, i.e. Cartesian and inertial coordinate system. This is the surprising consequence of the weak equivalence principle or the universality of free fall: the equation for free-fall can be understood as geodesic equation in some affine space-time! From (3.2.8) we see that t = a λ + b with constants a and b; therefore, we can choose the affine parameter λ as the absolute Newtonian time t. Note, that (3.2.8) is written in covariant form, i.e., it is valid for arbitrary coordinates. No 因此，在牛顿理论中，人们不希望改变普适时间坐标，但经常需要在曲线坐标（例如球坐标）或旋转坐标下写出方程。如果点表示d/dλ，那么对于任意的空间坐标xj，自由落体方程(3.2.8)写作： x¨i + Γijk x˙jx˙k + 2Γi0j x˙j + Γi00 = 0. (3.2.10)

该方程现在也包含了曲线坐标下必要的项和惯性力。例如 Γi00 = −U,i + [Ω × (Ω × x)]i (3.2.11)

包含了离心力，而 Γi0j x˙j = (Ω × x˙)i (3.2.12)

包含了科里奥利力。这里，Ω是坐标相对于惯性坐标（例如伽利略坐标）的角速度。

练习3.1 由(3.2.10)计算在某个势场U中，在球坐标系xi = (r, θ, φ)（非旋转坐标）下，一个自由下落测试粒子的运动方程。

解 由于我们的坐标是惯性坐标，Γi0j = 0 且 Γi00 = −U,i。因此很明显，我们只需要计算克里斯托费尔符号Γijk，它们是由(2.9.6)给出的欧几里得3-空间在球坐标下的克里斯托费尔符号。因此，在球坐标系下，测试质量（例如卫星）的方程写作： r¨ − rθ˙2 − r sin²θ φ˙2 − Ur = 0 θ¨ + 2 (r˙/r) θ˙ − sinθ cosθ φ˙2 − Uθ = 0 (3.2.13)

φ¨ + 2 cotθ θ˙ φ˙ + 2 (r˙/r) φ˙ − Uφ = 0.

对于中心球对称单极场，U = μ/r，我们可以取固定的轨道平面，例如θ = π/2，这样(3.2.13b)就满足了。于是我们得到牛顿开普勒问题的通常方程： r¨ − rφ˙2 + μ / r² = 0 (3.2.14)

φ¨ + 2 (r˙/r) φ˙ = 0, 其中(3.2.14b)给出了形式为 r² φ˙ = const. (3.2.15)

的角动量积分。

现在，每一组仿射联络都有一个相关的曲率张量。在牛顿理论中，这个曲率张量不是黎曼曲率张量，因为牛顿时空没有一个（非退化的）时空度规；这里的空间是平坦的，度规是欧几里得度规，而且这个欧几里得空间-度规完全独立于时间-度规。在伽利略坐标系下，牛顿曲率张量写作： Ri0j0 = Γi00,j − Γi0j,0 + Γiκ00 Γκ0j − Γi0κ Γκ0j = Γi00,j = −U,ij. (3.2.16)

曲率张量的物理意义是它描述了潮汐力：“曲率张量” = “潮汐力张量”。

为了理解这一点，我们考虑一束自由下落的测试粒子。我们给每个粒子一个编号σ，因此σ₁是第一个粒子，σ₂是第二个，以此类推。我们设想有无穷多个这样的粒子，这样我们可以对编号σ求导（见图3.1）。那么从 x¨ − ∇U = 0 我们得到 (∂ / ∂σ) (d²xi / dt²) − ∂U / ∂xi = 0.

现在如果我们写 ∂ / ∂σ = (∂xj / ∂σ) (∂ / ∂xj) ≡ nj ∂ / ∂xj, (3.2.17)

其中nj可以理解为在恒定时间下连接两个相邻测试粒子的向量，我们得到 d²ni / dt² − (∂²U / ∂xi∂xj) nj = Ri0j0 nj = 0. (3.2.18)

这就是牛顿雅可比方程或测地偏离方程。它描述了两个相邻测试粒子在引力场影响下的相对运动，该引力场由作用在两个粒子上的引力差给出（这解释了为什么会出现牛顿势的二阶导数）。

我们现在来到场方程。在牛顿的引力理论中，这是泊松方程： ∇²U = −4πGρ. (3.2.19)

这里，∇²是拉普拉斯算子 ∇² = ∂²/∂x² + ∂²/∂y² + ∂²/∂z², G是牛顿引力常数，ρ是产生引力场的（引力）质量密度。利用(3.2.16)，我们可以将场方程写为 Ri0i = −∇²U = +4πGρ 或 R₀₀ = 4πGρ (3.2.20)

其中 R₀₀ = −∇²U. (3.2.21)

场方程这种形式的含义是清楚的：引力质量密度ρ产生了时空的曲率。在牛顿理论中，曲率是时间方向的；牛顿理论中的空间是欧几里得的，即平坦的。

## 3.3 物体的引力场

对于单个物体(E)，我们将对牛顿势U施加边界条件 lim_{|x|→∞} U(t, x) = 0 (3.3.1)

泊松方程(3.2.19)则蕴含 U(t, x) = G ∫_E ρ(t, x') / |x − x'| d³x' ≡ G ∫_E dM / |x − x'|. (3.3.2)

3.3.1 球谐多极矩在物质分布之外，即ρ = 0的地方，势U满足拉普拉斯方程 ∇²U(t, x) = 0 (3.3.3)

我们希望将(3.3.2)的右边用多极矩展开。为此，我们可以采用球谐函数（相位约定如Condon和Shortley (1953)或Jackson (1975)；特别是在大地测量文献中，球谐函数的相位约定通常差一个因子(-1)^m）

Y_lm(θ, φ) = N_lm P_lm(cosθ) e^{imφ} (m ≥ 0). (3.3.4)

这里，N_lm是归一化常数 N_lm ≡ √[ (2l + 1)(l − m)! / (4π (l + m)!) ]. (3.3.5)

P_lm(cosθ)是连带勒让德函数： P_lm(x) = (−1)^m (1 − x²)^{m/2} (d^m / dx^m) P_l(x), (3.3.6)

其中P_l(x)是由罗德里格斯公式定义的普通勒让德多项式 P_l(x) = (1 / (2^l l!)) (d^l / dx^l) (x² − 1)^l. (3.3.7)

那么连带勒让德多项式可以写成如下形式 P_lm(x) = ( (−1)^m / (2^l l!) ) (1 − x²)^{m/2} (d^{l+m} / dx^{l+m}) (x² − 1)^l. (3.3.8)

练习3.2 证明： P_l(x) = Σ_{k=0}^{[l/2]} [ (−1)^k (2l − 2k)! / (2^l k! (l − k)! (l − 2k)! ) ] x^{l−2k}, (3.3.9)

其中[l/2] ≡ k_max 等于l/2（如果l是偶数）或等于(l − 1)/2（如果l是奇数）。因此连带勒让德函数在我们的情况中是x = cosθ的有限多项式。

解 由二项式公式 (x² − 1)^l = Σ_{k=0}^l [ C(l, k) x^{2(l−k)} (−1)^k ]

以及 d^l / dx^l [ x^{2(l−k)} ] = (2l − 2k)(2l − 2k − 1)···(l − 2k + 1) x^{l−2k} = [ (2l − 2k)! / (l − 2k)! ] x^{l−2k} 我们得到 (d^l / dx^l) (x² − 1)^l = (d^l / dx^l) Σ_{k=0}^l [ C(l, k) (−1)^k x^{2(l−k)} ]

= Σ_{k=0}^{k_max} [ C(l, k) (−1)^k (2l − 2k)! / (l − 2k)! x^{l−2k} ]

= Σ_{k=0}^{k_max} [ l! / (k! (l − k)!) (−1)^k (2l − 2k)! / (l − 2k)! x^{l−2k} ]

= Σ_{k=0}^{k_max} [ (−1)^k l! (2l − 2k)! / (k! (l − k)! (l − 2k)!) x^{l−2k} ]

这与(3.3.9)一致。

练习3.3 利用(3.3.9)证明，对于m ≥ 0， (d^m / dx^m) P_l(x) = Σ_{k=0}^{[(l−m)/2]} a_{lmk} x^{l−m−2k} (3.3.10)

其中 a_{lmk} ≡ [ (−1)^k (2l − 2k)! ] / [ 2^l k! (l − k)! (l − m − 2k)! ]. (3.3.11)

利用(3.3.10)，我们看到对于m ≥ 0，Y_lm(θ, φ)可以写成如下形式 Y_lm(θ, φ) = (−1)^m N_lm (e^{iφ} sinθ)^m Σ_{k=0}^{[(l−m)/2]} a_{lmk} (cosθ)^{l−m−2k}. (3.3.12)

对于负的m值， Y_{l,−m}(θ, φ) = (−1)^m Y_{lm}^*(θ, φ) (3.3.13)

这对所有m值都成立。取所有可能的(l, m)值，它们在单位球上构成一组完备的正交归一函数；归一化和正交条件取如下形式 ∫_0^{2π} dφ ∫_0^π sinθ dθ Y_{l'm'}^*(θ, φ) Y_{lm}(θ, φ) = δ_{ll'} δ_{mm'}. (3.3.14)

此外，可以发现 Σ_{m=−l}^l |Y_{lm}(θ, φ)|² = (2l + 1) / (4π) (3.3.15)

以及 1 / |x − x'| = 4π Σ_{l=0}^∞ Σ_{m=−l}^l [ 1 / (2l + 1) ] (r_<^l / r_>^{l+1}) Y_{lm}^*(θ', φ') Y_{lm}(θ, φ). (3.3.16)

这里，r_< (r_>) 是 |x| 和 |x'| 中较小（较大）的值。对于少数较小的l值，Y_{lm}(θ, φ)的显式表达式如下： l = 0   Y₀₀ = 1 / √(4π)

l = 1   Y₁₁ = −√(15/(8π)) sinθ e^{iφ} Y₁₀ = √(3/(4π)) cosθ Y_{1,−1} = +√(15/(8π)) sinθ e^{-iφ} l = 2   Y₂₂ = (1/4) √(15/(2π)) sin²θ e^{2iφ} Y₂₁ = −√(15/(8π)) sinθ cosθ e^{iφ} Y₂₀ = √(5/(4π)) ( (3/2) cos²θ − 1/2 )

Y_{2,−1} = +√(15/(8π)) sinθ cosθ e^{-iφ} Y_{2,−2} = (1/4) √(15/(2π)) sin²θ e^{-2iφ} l = 3   Y₃₃ = −(1/4) √(35/(4π)) sin³θ e^{3iφ} Y₃₂ = (1/4) √(105/(2π)) sin²θ cosθ e^{2iφ} Y₃₁ = −(1/4) √(21/(4π)) sinθ (5 cos²θ − 1) e^{iφ} Y₃₀ = √(7/(4π)) ( (5/2) cos³θ − (3/2) cosθ )

Y_{3,−1} = +(1/4) √(21/(4π)) sinθ (5 cos²θ − 1) e^{-iφ} Y_{3,−2} = (1/4) √(105/(2π)) sin²θ cosθ e^{-2iφ} Y_{3,−3} = +(1/4) √(35/(4π)) sin³θ e^{-3iφ}

一些选定的球谐函数如图3.2所示。

将表达式(3.3.16)代入(3.3.2)，我们在物质分布之外（其中r_> = |x|，r_< = |x'|）得到 U(t, x) = G ∫_E d³x' [ 4πρ(t, x') Σ_{l,m} (1 / (2l + 1)) (r_<^l / r_>^{l+1}) Y_{lm}^*(θ', φ') Y_{lm}(θ, φ) ]

≡ G Σ_{l=0}^∞ Σ_{m=−l}^l [ M_{lm} Y_{lm}(θ, φ) / r_>^{l+1} ]. (3.3.17)

这里M_{lm}是物质分布的复数球质量多极矩。由于Y₀₀ = 1/√(4π)，M₀₀ = √(4π) M，其中M是物体的质量。我们假设这样的展开在一个完全包围物质分布的坐标球之外收敛。在实际中常使用不同的质量多极矩。令 Σ_{m=−l}^l M_{lm} Y_{lm}(θ, φ) = Σ_{m=0}^l P_{lm}(cosθ) [ C_{lm} cos(mφ) + S_{lm} sin(mφ) ] (3.3.18)

那么利用实数势系数C_{lm}和S_{lm}， U(t, x) = G Σ_{l=0}^∞ (1 / r^{l+1}) Σ_{m=0}^l P_{lm}(cosθ) [ C_{lm} cos(mφ) + S_{lm} sin(mφ) ]. (3.3.19)

在大地测量文献中，经常使用无量纲势系数C_{lm}^*和S_{lm}^*： U(t, x) = (GM / r) Σ_{l=0}^∞ (R / r)^l Σ_{m=0}^l P_{lm}(cosθ) [ C_{lm}^* cos(mφ) + S_{lm}^* sin(mφ) ] (3.3.20)

其中 C_{lm} = (M R^l) C_{lm}^* S_{lm} = (M R^l) S_{lm}^* (3.3.21)

R是中心体E的某个适当选择的半径。那么(C_{lm}, S_{lm})或(C_{lm}^*, S_{lm}^*)是实数多极矩，也被称为势系数。它们与我们的复数质量多极矩的关系是 C_{lm} = N_{lm} (2 − δ_{m0}) ℜ [ M_{lm} ]

S_{lm} = −2 N_{lm} (1 − δ_{m0}) ℑ [ M_{lm} ]

(3.3.22)

对于一个具有轴对称性的物体，在(3.3.20)中m = 0，因此（假设l = 1的质量偶极矩项消失）

U(t, x) = (GM / r) [ 1 − Σ_{l=2}^∞ J_l (R / r)^l P_l(cosθ) ] (3.3.23)

其中J_l = −C_{l0}^*。

通常的球质量多极矩（势系数）可以被笛卡尔质量多极矩取代。这些量是对称且无迹（STF）的笛卡尔张量，将在第3.3.3节中研究。

3.3.2 扁球体的球质量矩某个密度为ρ的物质分布的牛顿引力势U(t, x)在球坐标r, θ, φ下由下式给出 U(t, x) = G ∫ r'² dr' sinθ' dθ' dφ' ρ(t, x') / |x − x'|.

我们现在假设物质分布是轴对称且静态的，因此在外面我们从一个物体出发。

势函数可以写为： U(x) = 2πG ∫∫ (r'² sinθ' dr' dθ' ρ(r', θ')) / |x - x'|

其中方括号表示对角度φ'的平均。由(3.3.16)和球谐函数的表达式可知，对于轴对称情况，只有m=0的项有贡献，因此： 1 / |x - x'| = Σ (r'^l / r^{l+1}) P_l(cosθ) P_l(cosθ')

因此： U(x) = 2πG Σ [1 / r^{l+1}] ∫₀^{R(θ')} ∫₀^π dr' π sinθ' dθ' r'^{l+2} ρ(r', θ') P_l(cosθ') P_l(cosθ)

其中 R(θ) 定义了物体的外边界。假设 ρ(r', θ') = ρ = 常数，我们可以写成： U(x) = Σ [J_l P_l(cosθ)] / r^{l+1} 其中 J_l = 2πGρ ∫₀^{R(θ')} ∫₀^π dr' sinθ' dθ' r'^{l+2} P_l(cosθ')

对r'的积分结果为： J_l = (2πGρ / (l+3)) ∫₀^π sinθ' dθ' R^{l+3}(θ') P_l(cosθ')

令 z = cosθ'，则有： J_l = (2πGρ / (l+3)) ∫_{-1}^{+1} dz P_l(z) [R(z)]^{l+3}

现在假设物体的形状为扁椭球体，在笛卡尔坐标系中由下式给出： 1 = x²/a² + z²/c²

其中a(c)是旋转椭球体的半长轴（半短轴）。对于我们的扁体，a > c。由此得到： 1 = R² sin²θ / a² + R² cos²θ / c² 或 R(z) = [1 + αz²]^{-1/2} 其中 α ≡ (a² - c²) / c²

由于R(z) = R(-z)，所有奇数多极矩 J_{2n+1} 均为零。对于偶数质量矩，l = 2n，我们得到： J_{2n} = [4πGρ a^{2n+3} / ((2n+1)(2n+3))] (-α)^n (1 + α)^{-n-1/2} = (-1)^n [3GMc^{2n} / ((2n+1)(2n+3))] α^n

这里我们用到了（Magnus et al. 1981）： ∫_{-1}^{+1} [P_{2n}(z) / (1 + αz²)^{n+3/2}] dz = 2 (-α)^n (1 + α)^{-n-1/2} / (2n+1)

M = (4π/3) ρ a³ (1 + α)^{-1/2} 是椭球体的质量（体积 V = (4π/3)a²c），并且 α / (1 + α) = α c² / a²

通过引入无量纲质量多极矩 J̃： J̃_l = J_l / (GM a^l)

我们得到： J̃_{2n} = (-1)^n ε²ⁿ / ((2n+1)(2n+3))

其中椭率 ε 由下式定义： ε² = 1 - c² / a²

这个结果(3.3.33)可以在例如 Antonov et al. (1988) 或 Pohanka (2011) 中找到。

练习3.4 使用公式 1 / |x - x'| = (1 / r_<) Σ (r_<^l / r_>^l) P_l(cosφ)

其中 r_< (r_>) 是 |x| 和 |x'| 中较小（较大）的值，φ 是 x 和 x' 之间的夹角，如图3.3所示，推导质量为M、半径为a的环在环平面内环内部的势能。同时计算位于该点的单位质量的引力加速度。

解：牛顿势能 U 由下式给出： U = G ∫ dm' / |x - x'| 其中 dm' = (M/2π)dφ'。利用(3.3.34)我们得到： U = (GM/a) Σ [I_l (r/a)^l]

其中 I_l ≡ (1/2π) ∫₀^{2π} P_l(cosφ) dφ 现在，l为奇数时 I_l = 0，并且 I_{2k} = P_{2k}(0) = (-1)^k (2k)! / (2^{2k} (k!)²)

因此，环在环平面内环内部的牛顿引力势能为： U = (GM/a) Σ_{k=0}^∞ P_{2k}(0) (r/a)^{2k} 由环引起的加速度（n = x/r）为： a_{ring} = (∂U/∂r) · n = (GM/a²) Σ_{k=1}^∞ (2k) P_{2k}(0) (r/a)^{2k-1} n

3.3.3 STF张量一个笛卡尔l阶张量是一组实数或复数 T_{i₁i₂...i_l}，有l个不同的指标 i₁ 到 i_l，每个取值为1,2,3或等价的(x,y,z)。一个笛卡尔1阶张量就是三元向量 T_i，其中 i = 1,2,3 = x,y,z。一个笛卡尔2阶张量是一个3×3矩阵 T_{ij}，其中 i,j = 1,2,3。为了简洁，通常将一组l个笛卡尔指标缩写为多指标，例如 L ≡ i₁i₂...i_l。通常假定爱因斯坦求和约定，即如果某个指标出现两次，则自动对该指标求和，例如： A_L B_L ≡ A_{i₁i₂...i_l} B_{i₁i₂...i_l} ≡ Σ_{i₁=1}^3 ... Σ_{i_l=1}^3 A_{i₁i₂...i_l} B_{i₁i₂...i_l} 给定一个笛卡尔张量 T_L，我们用圆括号表示其对称部分： T_{(L)} = T_{(i₁...i_l)} = (1/l!) Σ_σ T_{i_{σ(1)}...i_{σ(l)}} 其中 σ 遍历 (1,2,...,l) 的所有 l! 个排列。如果 T_L 是一个笛卡尔l阶张量；我们将任意两个指标取为相同并随后求和的量称为 T_L 的迹。如果 T_L 的每个迹都为零，则称之为无迹的。非常重要的是对称无迹（STF）笛卡尔张量。T_L 的STF部分记为 T̂_L ≡ T_{<L>} ≡ T_{<i₁...i_l>}。STF部分的显式表达式为（Pirani 1964; Thorne 1980）： T̂_L = Σ_{k=0}^{[l/2]} a_{lk} δ_{i₁i₂} ... δ_{i_{2k-1}i_{2k}} S_{i_{2k+1}...i_l} 其中 S_L = T_{(L)} a_{lk} = (l! / (2l-1)!!) * (-1)^k (2l-2k-1)!! / ((l-2k)! (2k)!!)

[l/2]表示 l/2 的整数部分，即小于或等于 l/2 的最大整数。例如， T̂_{ij} = T_{(ij)} - (1/3) δ_{ij} T_{aa} T̂_{ijk} = T_{(ijk)} - (1/5) [δ_{ij} T_{(kaa)} + δ_{jk} T_{(iaa)} + δ_{ki} T_{(jaa)}]

对于每个正整数 l，有： l! = l·(l-1)·(l-2)···2·1;  l!! = l·(l-2)·(l-4)···(1或2).

以及 (2l)!! = 2^l l!;  (2l+1)!! = (2l+1)! / (2^l l!);  (l choose k) = l! / (k! (l-k)!)

练习3.5 证明STF张量的公式(3.3.41)与(3.3.42)，并证明(3.3.42)中的系数 a_{lk} 也可以写成如下形式： a_{lk} = (-1)^k * (l choose k) * (2l choose 2k) / (2k choose k)

证明：此练习的证明可在Pirani (1964) 中找到。

如果我们用 e_j (j = 1,2,3) 表示笛卡尔基向量（其中 e_k^j = δ_k^j），可以验证，STF l阶张量的 (2l+1) 维向量空间的一组基可以由 E⁺ ⊗···⊗ E⁺ ⊗ E⁰ ⊗···⊗ E⁰ 的STF部分构造出来，其中 E⁺ ≡ e₁ + i e₂ = (1, i, 0)ᵀ,   E⁰ ≡ e₃ = (0, 0, 1)ᵀ （其中 i² = -1）及其复共轭。更精确地说，这样一组基是 Ŷ_{lm}，其中 -l ≤ m ≤ +l，对于 m ≥ 0， Ŷ_{lm} = A_{lm} E^L_{lm} 其中 E^L_{lm} = E⁺ ... E⁺ (i₁ ... i_m) E⁰ ... E⁰ (i_{m+1} ... i_l)

且 A_{lm} = (-1)^m (2l-1)!! / [4π (l-m)! (l+m)!]^{1/2} 显式地（例如，Thorne (1980) 的(2.12)；见练习(3.6)）： Ŷ_{lm} = Ŷ_{lm}^{k₁...k_l} = (-1)^m N_{lm} Σ_{j=0}^{[(l-m)/2]} a_{lmj} [δ_{k₁}^{(1)} + iδ_{k₁}^{(2)}] ... [δ_{k_m}^{(1)} + iδ_{k_m}^{(2)}] × [δ_{k_{m+1}}^{(3)} ... δ_{k_{m+2j}}^{(3)}] [δ_{k_{m+2j+1}}^{(a₁)} δ_{k_{m+2j+2}}^{(a₁)}] ... [δ_{k_{l-1}}^{(a_j)} δ_{k_l}^{(a_j)}]

其中 a_{lmj} 由(3.3.11)给出。对于 m < 0，我们有： Ŷ_{lm} = (-1)^m (Ŷ_{l,-m})^* 正交性条件为： Ŷ_{lm} (Ŷ_{l'm'})^* = δ_{mm'} δ_{ll'} / (2l+1)!!

许多关于STF张量的重要关系是已知的（例如，Blanchet and Damour 1986; Thorne 1980）。其中一些列在附录中。

STF张量和基本张量 Ŷ_{lm} 的重要性源于它们与通常的标量球谐函数 Y_{lm} 的关系。Ŷ_{lm} 与这些球谐函数之间的基本关系由下式给出（x = r sinθ cosφ, y = r sinθ sinφ, z = r cosθ）： n_x + i n_y = x/r + i y/r = sinθ e^{iφ};  n_z = z/r = cosθ.

它读作： Y_{lm} = Ŷ_{lm} n^L = Ŷ_{lm} n̂^L 其中 n^L = n^{i₁...i_l} = (x^{i₁} ... x^{i_l}) / r^l 利用正交性关系(3.3.52)，可以导出逆关系： n̂^L = Σ_{m=-l}^{l} [4π l! / (2l+1)!!] Ŷ_{lm} Y_{lm}^* 练习3.6 利用关系式(3.3.12)推导表达式(3.3.54)

Y_{lm} = Ŷ_{lm} n^L.

证明：由于在 Ŷ_{lm} n^L 的求和中，n_x + i n_y = e^{iφ} sinθ 且 n_z = cosθ，我们可以将形式为 δ^{(1)} + iδ^{(2)} 的 m 个项各替换为 e^{iφ} sinθ，将形式为 δ^{(3)} 的 l - m - 2j 个项替换为 cosθ。与 n 的迹相关的 j 个形式为 δ^a δ^a 的项应被替换为 1，因为 n_a n^a = 1，因此我们最终得到 Y_{lm}(θ, φ) 的关系式(3.3.12)。

让我们说明 l = 0,1,2 时的关系式(3.3.54)。对于 l = 0，归一化给出单个数字 1/√(4π)。对于 l = 1，我们有显式： Ŷ_{11}^{j} = -√(3/8π) E⁺_j,  Ŷ_{10}^{j} = √(3/4π) E⁰_j,  Ŷ_{1,-1}^{j} = +√(3/8π) E⁻_j 其中 E⁻ = (E⁺)* = (-i, 1, 0)ᵀ.

容易看出 Y_{1m} = Ŷ_{1m}^j x_j / r。对于 l = 2，我们有： Ŷ_{22}^{jk} = +√(3/5) * 1/(4π) * [ 1/2   i/2    0;   i/2   -1/2   0;   0     0     0]

Ŷ_{21}^{jk} = -√(3/5) * 1/(4π) * [ 0     0      1/2; 0     0      i/2; 1/2   i/2    0]

Ŷ_{20}^{jk} = +1/√(5) * 1/(4π) * [ -1    0      0;   0     -1     0;   0     0      2]

Ŷ_{2,-1}^{jk} = +√(3/5) * 1/(4π) * [ 0     0      1/2; 0     0     -i/2; 1/2  -i/2    0]

Ŷ_{2,-2}^{jk} = +√(3/5) * 1/(4π) * [ 1    -i      0;  -i    -1     0;   0     0      0]

并且容易验证 Y_{2m} = Ŷ_{2m}^{jk} x_j x_k / r²。

练习3.7 使用关系式(3.3.50)得到 Ŷ_{20}^{k₁k₂} 的表达式(3.3.59)。利用这个结果证明 Y_{20} = Ŷ_{20}^{k₁k₂} n_{k₁} n_{k₂}.

证明：我们有 Ŷ_{20}^{k₁k₂} = N_{20} (a_{200} δ_{k₁}^{(3)} δ_{k₂}^{(3)} + a_{201} δ_{k₁}^{(s)} δ_{k₂}^{(s)})

其中 N_{20} = 5/(4π), a_{200} = 3/2 且 a_{201} = -1/2。因此， Ŷ_{20}^{k₁k₂} = (1/2) N_{20} (3 δ_{k₁}^{(3)} δ_{k₂}^{(3)} - δ_{k₁}^{(s)} δ_{k₂}^{(s)})

这与(3.3.59)一致。此外，Ŷ_{20}^{k₁k₂} n_{k₁} n_{k₂} = (1/2) N_{20} (3 n_z n_z - 1) = Y_{20}。

假设 T_{L} 是某个笛卡尔STF l阶张量。那么它总是可以写成如下形式： T̂_L = Σ_{m=-l}^{l} T_{lm} Ŷ_{lm}^L 其中，由于归一化关系(3.3.52)，(2l+1)个数 T_{lm} 由下式给出： T_{lm} = [4π l! / (2l+1)!!] T̂_L (Ŷ_{lm}^L)^* 通常， T_{l,-m} = (-1)^m (T_{lm})^*.

对于 l=1，得到： T_{11} = -√(4π/3) (T_{12} - i T_{23})? (注：具体分量表达式需根据张量定义确定，但形式类似)

T_{10} = +√(4π/3) T_{33}?

对于 l=2： T_{22} = +1/√(15π) (T̂_{11} - T̂_{22} - 2i T̂_{12})?

T_{21} = -1/√(15π) (T̂_{13} - T̂_{23})?

T_{20} = +1/√(5π) T̂_{33}?

另一个有用的公式是： Ŷ_{lm}^L ∂_L (1/r) = N_{lm} a_{lm0} (∂_x + i ∂_y)^m ∂_z^{l-m} (1/r)

由此可以导出著名的麦克斯韦关系： Ŷ_{lm}^L ∂_L (1/r) = (-1)^l (2l-1)!! Y_{lm} / r^{l+1} 显式地（参见 Hobson 1955）： (-1)^ We can write the Newtonian potential in the form U(t,x) = G ∫ d³x' ρ(x') / |x - x'|  (3.3.69)

=G ∑_{l≥0} (-1)^l / l! ∫ d³x' ρ(x') x'^{i1} ··· x'^{il} ∂_{i1} ··· ∂_{il} (1/r) .

Let ϕ_{i1...il} ≡ ∂_{i1} ··· ∂_{il} (1/r) ≡ ∂_{xi1} ··· ∂_{xil} (1/r) .

Then because of □ = 0  (3.3.70)

the symmetric Cartesian (every index takes the values x, y, z) tensor ϕ is trace-free, i.e., ϕ_{i1j...j} = 0 etc. ϕ is a Cartesian STF-tensor.

Let ϕ_L = ϕ̂_L = ∂_L (1/r) .  (3.3.71)

Then ϕ̂_L = (-1)^l (2l-1)!! n̂_L / r^{l+1} .  (3.3.72)

The proof of this important relation is by induction: for l = 0 we get ϕ = 1/r in agreement with (3.3.72). For l = 1 we get ϕ_i = ∂_i (1/r) = -x^i / r^3 = -n_i / r^2 also in accordance with (3.3.72). We now assume this relation to be valid for l. Then (trace-terms)

ϕ_{L+1} = ∂_i { x^L_i / r } = ∂_i { (-1)^l (2l-1)!! x^L / r^{2l+1} } = (-1)^l (2l-1)!! x^L ∂_i (1 / r^{2l+1}) + tt = (-1)^{l+1} (2(l+1)-1)!! x^L x^i / r^{2l+3} + tt = (-1)^{l+1} (2(l+1)-1)!! n̂_{L+1} / r^{2l+3} + tt as was to be shown. With that result we can write the Cartesian multipole expansion of U in the form U(t,x) = G ∑_{l≥0} (2l-1)!! / l! M̂_L n̂_L / r^{l+1} .  (3.3.73)

Using the obvious fact that A̅_L B̅_L = A_L B_L = A̅_L B̅_L  (3.3.74)

we have M_L = M̂_L = ∫ d³x' ρ(x') x̂'^L .  (3.3.75)

This Cartesian multipole expansion of U is equivalent to the expansion in terms of spherical harmonics.

Clearly the mass multipole moments, M_L in the Cartesian language, depend upon the origin of the Cartesian coordinate system x. Let M^x_L be the Cartesian mass moments with respect to some coordinates x; let x = y + d with y being a new set of Cartesian coordinates whose origin differs by the constant vector d from that of the x-system. Then, from the definition of M_L one obtains: M^x_L = ∑_{K≤L} (L choose K) d^{L-K} M^y_K .  (3.3.76)

Thus, associated with a single body there is a unique Cartesian inertial system that is mass-centered where the mass dipole moment vanishes.

Using relations (3.3.17) and (3.3.73) the correspondence between the Cartesian moments M_L and the potential coefficients (C_lm, S_lm) or the spherical mass-moments M_lm can be found. Using also (3.3.13) and (3.3.51) one finds that our Cartesian and spherical mass multipole moments, M_L and M_lm are related by M_lm = (4π / (2l+1)) (Ŷ_lm)* · M̂_L .  (3.3.77)

The inverse relation is obtained by projecting with Ŷ_{lm'}, summing over m' and using the orthogonality relation (3.3.52): M̂_L = (l! / (2l-1)!!) ∑_{m=-l}^{l} M_lm Ŷ_lm .  (3.3.78)

Exercise 3.8 Derive the relations between the Cartesian and spherical quadrupole mass-moments (l = 2) explicitly simply by expressing the spherical harmonics in terms of Cartesian coordinates.

Solution We start with U^{(2)}(x) = (G / r^3) [ P_2 C_{20} + P_{21} (C_{21} cosφ + S_{21} sinφ) + P_{22} (C_{22} cos2φ + S_{22} sin2φ) ] .

Since (x = r sinθ cosφ, y = r sinθ sinφ, z = r cosφ), r^2 P_20 = (2z^2 - x^2 - y^2)/2 r^2 P_21 cosφ = 3xz r^2 P_21 sinφ = 3yz r^2 P_22 cos2φ = 3(x^2 - y^2)

r^2 P_22 sin2φ = 6xy, we get U^{(2)}(x) = (G / r^5) [ C_{20} (2z^2 - x^2 - y^2)/2 + 3C_{21} xz + 3S_{21} yz + 3C_{22} (x^2 - y^2) + 6S_{22} xy] .  (3.3.79)

In the STF-language we have U^{(2)}(x) = (3G / (2 r^5)) M_{ij} x^i x^j ,  (3.3.80)

where a complete summation over i and j over 1, 2, 3 is assumed. Considering, e.g., the xz-term, one has (G / r^5) 3 C_{21} xz = (G / r^5) 3 M_{13} xz so that M_{13} = C_{21} .

In this way one finds M_{11} = +2C_{22} - C_{20} M_{22} = -2C_{22} - C_{20} M_{33} = C_{20} M_{12} = 2S_{22} M_{13} = C_{21} M_{23} = S_{21} .  (3.3.81)

Because of symmetry and the tracelessness, i.e., M_{11} + M_{22} + M_{33} = 0, there are five independent components of M_{ij}. The inverse relations read C_{20} = M_{33} - (1/2)(M_{11} + M_{22})

C_{21} = M_{13} C_{22} = (1/2)(M_{11} - M_{22})  (3.3.82)

S_{21} = M_{23} S_{22} = (1/2)M_{12} .

Exercise 3.9 Derive the relations between M_{ijk} and the potential coefficients C_lm and S_lm for l = 3 by using relations (3.3.22).

Solution From (3.3.47) we get Y_{ijk}^{(3)m} = A · E^{(3)m} = A · ( E_{ijk}^{(3)m} - (1/5) ( δ_{ij} E_{kaa}^{(3)m} + δ_{ki} E_{jaa}^{(3)m} + δ_{jk} E_{iaa}^{(3)m} ) )

that reads explicitly for m = 0, 1, 2, 3 Y_{ijk}^{(3)0} = (15 / 12π) (1/2) { 7 δ_{i1} δ_{j1} δ_{k1} - (1/5) [ δ_{ij} δ_{k1} + δ_{ki} δ_{j1} + δ_{jk} δ_{i1} ] } Y_{ijk}^{(3)1} = -(15 / 12π) (1/4) { (1/3) [ (δ_{i1} + i δ_{i2}) δ_{j1} δ_{k1} + (δ_{j1} + i δ_{j2}) δ_{k1} δ_{i1} + (δ_{k1} + i δ_{k2}) δ_{i1} δ_{j1} ]

- (1/15) [ δ_{ij} (δ_{k1} + i δ_{k2}) + δ_{ki} (δ_{j1} + i δ_{j2}) + δ_{jk} (δ_{i1} + i δ_{i2}) ] } Y_{ijk}^{(3)2} = (15 / 30π) (1/4) { (1/3) [ (δ_{i1} + i δ_{i2}) (δ_{j1} + i δ_{j2}) δ_{k1} + (δ_{i1} + i δ_{i2}) (δ_{k1} + i δ_{k2}) δ_{j1} + (δ_{j1} + i δ_{j2}) (δ_{k1} + i δ_{k2}) δ_{i1} ] } Y_{ijk}^{(3)3} = -(15 / 180π) (1/4) { (δ_{i1} + i δ_{i2}) (δ_{j1} + i δ_{j2}) (δ_{k1} + i δ_{k2}) } with (3.3.78) the Cartesian STF-multipole moments can be computed: M̂_L = (l! / (2l-1)!!) ∑_{m=-l}^{l} M_lm Ŷ_lm = (2l! / (2l-1)!!) ∑_{m=0}^{l} (M_lm Ŷ_lm)

For l=3: M̂_{ijk} = (6/15) ∑_{m=0}^{3} (M_{3m} Y_{ijk}^{(3)m})

so that M_{111} = -(3/5) C_{31} + 6 C_{33}   M_{112} = -(3/5) S_{31} + 6 S_{33} M_{122} = -(1/5) C_{31} - 6 C_{33}   M_{222} = -(1/5) S_{31} - 6 S_{33} M_{113} = -(2/5) C_{30} + 2 C_{32}   M_{223} = -(2/5) C_{30} - 2 C_{32} M_{123} = +2 S_{32} .

## 3.4 The Tidal Potential

3.4.1 Newtonian Tidal Moments For the description of tidal forces the equivalence principle is of special relevance. This principle implies that in suitable local coordinates (t, X) the gravitational action of external bodies can be described by some tidal potential U_tidal of the form U_tidal(X) = U_ext(z + X) - U_ext(z) - d²z/dt² · X .  (3.4.1)

For an observer in free-fall, d²z_i/dt² = ∂_i U_ext(z), so that the linear term in the effective potential vanishes and an expansion in terms of co-moving spatial coordinates starts with quadratic terms. Deviations from such free-fall behavior of some astronomical body results either from non-gravitational forces acting on the body or from couplings to the external gravitational field resulting from the non-spherical components of the body's own gravitational field.

In practise it is common to expand U_eff in a tidal-series, i.e., a Taylor-series in positive powers of X, U_eff(X) = G_i X^i + (1/2!) G_{ij} X^i X^j + ... + (1/l!) G_{i1...il} X^{i1} ... X^{il} + ...  (3.4.2)

where the Newtonian tidal-moments felt by body E read G_i(t) ≡ ∂_i U_ext(z_E) - d²z_E^i/dt² , G_{i1...il}(t) ≡ ∂_{i1} ... ∂_{il} U_ext(z_E) (l ≥ 2).

Because of the Laplace equation, □U = 0 outside body A, the tidal moments G_{i1...il} are automatically symmetric and trace-free (L ≡ i_1 ... i_l)

G_L ≡ STF [ ∂_L U_ext(z_E) ] (l ≥ 2).  (3.4.4)

Thus, with the tidal moments of (3.4.3) U_tidal can be written as U_tidal = ∑_{l=1}^{∞} (1/l!) G_L X^L .  (3.4.5)

with the Newtonian tidal-moments G_L which are STF-tensors.

Assuming z_E to coincide with the geocenter (center of mass) and inserting the expression (see (3.5.5) below)

d²z_E^i/dt² = G ∑_{A≠E} ∑_{l=0}^{∞} ∑_{j=0}^{∞} (-1)^j / (l! j!) M_L M_A ∂_E (1 / r_{EA}^{l+j+1}) , where ∂_E ≡ ∂/∂z_E^i and r_{EA} ≡ |z_E - z_A|, the tidal potential can be written in the form: U_tidal(t,X) = ∑_{A≠E} [ ∑_{l=2}^{∞} ∑_{j=0}^{∞} ( (-1)^j / (l! j!) ) M_L X^L ∂_E (1 / r_{EA}^{l+j+1})

- ∑_{l=1}^{∞} ∑_{j=0}^{∞} ( (-1)^j / (l! j!) ) M_L M_J X^i ∂_E (1 / r_{EA}^{l+j+1}) ] .  (3.4.7)

The second term on the right hand side of (3.4.7) (the geodesic deviation term) results from the fact that due to higher multipole couplings the Earth (E) is not freely falling. Expression (3.4.7) is the most general form of the tidal potential since all mass multipole moments of the bodies are taken into account. Replacing the Cartesian multipole moments by their spherical counterparts one gets the spherical representation of the tidal potential (X given by (R, θ, φ), z_E - z_A given by (r_{EA}, θ_{EA}, φ_{EA}))

U_tidal(t,X) = ∑_{A≠E} ∑_{l=2}^{∞} ∑_{m=-l}^{l} G (-1)^l (4π / (2l+1)) γ_{lm} R^l M_A Y_{lm}^{*} (θ, φ) Y_{l+j, m+k}^{jk} (θ_{EA}, φ_{EA}) / r_{EA}^{l+j+1} - ∑_{E} ∑_{l=1}^{∞} ∑_{m=-l}^{l} G (-1)^l γ_{lm} M_E M_A X^i ∂_E Y_{l+j, m+k}^{jk} (θ_{EA}, φ_{EA}) / r_{EA}^{l+j+1} .

Here, ∇ (r^p Y_{pq}) = - [ (2p+3) (α_+ Y_{p+1, q-1} + α_- Y_{p+1, q+1}) - p Y_{p-1, q} ] / (2p)

with α_± ≡ [ (p ∓ q + 2)(p ∓ q + 1) ]^{1/2}, α_0 ≡ [ (p + q + 1)(p - q + 1) ]^{1/2}.  (3.4.9)

Exercise 3.10 Proof that expression (3.4.8) for the tidal potential in spherical coordinates follows from the Cartesian expression (3.4.7) (Hartmann et al. 1994).

3.4.2 The l = 2 Tidal Potential for External Point-Masses The tidal potential in the vicinity of the Earth's surface is dominated by the l = 2 term. E.g., for the Moon as external body, the l = 3 term is smaller by a factor of (R / d) ≈ (6400km / 400,000km) ≈ 0.016.

In the following we will concentrate on the l = 2 tidal potential raised by one external point mass A. For l > 1 generally we have (d_A = |X_A|)

G_L = ∂_L U_A(x_E) = G M_A ∂_L (1 / |x - x_A|) = (2l-1)!! G M_A n̂_A (X) / (d_A^{l+ φ changes due to the rotation of the Earth. Since the inertial motion of Moon and Sun about the Earth is ‘slow’, φ has almost a diurnal period. For that reason, V20 describes the long-period tides, V21 the diurnal tides and V22 the semi-diurnal tides.

Concentrating on V21, relevant for nutation, we have

V21 = GM_A P1(cosθ) P1(cosθ_A) cos(φ−φ_A) / d3^3

Since cos(φ−φ_A) = cosφ cosφ_A + sinφ sinφ_A, V21 can be written in the form

V21 = −GM_A P1(cosθ_A) [XZ·cosφ_A + YZ sinφ_A] / d3^3

= 3 GM_A [(X Z)·XZ + (Y Z)·YZ] / d5^5. (3.4.21)

## 3.5 Translational Equations of Motion

Considering the gravitational N-body problem in the accelerated E-frame, the evolution equations for the motion of matter read:

∂ρ/∂t + ∂(ρVi)/∂Xj = 0,

∂(ρVi)/∂t + ∂(ρViVj)/∂Xj + tij = ρ ∂Ueff/∂Xi.

Here, V = vi − dzi/dt is the velocity with respect to the local frame and tij denotes the 3×3 material stress tensor. Using these local equations of motion, one finds

dME(t)/dt = 0,

d²ME(t)/dt² = ∫ d³X ρ ∂Uidal/∂Xi = Σ_{l=0}^∞ M ŜEGE. (3.5.2)

Note, that the self-potential UE does not contribute to the right hand side of the second equation of (3.5.2) (‘action and reaction principle’). Let us now assume the origin of the local E-system to coincide with the center of mass of body E defined by the vanishing of the mass dipole moment

ME = 0. (3.5.3)

Then, the global equation of motion for zi(t) can be obtained from the equilibrium condition (’d’Alembert’s principle’, see D’Alembert 1743)

d²ME/dt² = 0. (3.5.4)

Using (3.5.2) and expression (3.4.3) for GE, Eq. (3.5.4) leads to:

−M_E d²zi/dt² = M_E ∂/∂zi [−UE(z)] = Σ_{l=1}^∞ M_E GE

or, writing GE explicitly

M_E d²zi/dt² = G Σ_{l=0}^∞ Σ_{j=0}^∞ [(-1)^j M_E M_A ∂E 1 / (l! j! L_J iLJ r)], (3.5.5)

where A ≠ E, LJ = |z_E - z_A|.

Here again ∂E ≡ ∂/∂zi etc. and r = |zE − zA|. It is interesting to note that the force acting on body E can be written as the gradient of a two-body interaction potential, i.e.,

M_E d²zi/dt² = ∇_{zE} Σ_{A≠E} UEA (3.5.6)

with

UEA = G Σ_{l=0}^∞ Σ_{j=0}^∞ [(-1)^j M_E M_A ∂E / (l! j! L_J LJ|z_E − z_A|)]. (3.5.7)

This condensed formula contains all multipole-multipole couplings. Using (3.3.66) and (3.3.78) this expression is easily converted to the representation with spherical harmonics (e.g., Gleixner 1982; Ilk 1983; Hartmann et al. 1994)

UEA = G Σ_{l=0}^∞ Σ_{m=-l}^l Σ_{j=0}^∞ Σ_{k=-l}^l M_E M_A (-1)^l γlm Y_{l+j,m+k}(θ_EA, φ_EA), (3.5.8)

where zE − zA = ̂ (r, θ_EA, φ_EA) and γlm is given by (3.3.67).

## 3.6 Rotational Equations of Motion

In the local E-frame we define the spin vector (intrinsic total angular momentum vector) of body E by (dropping the index E if possible)

S ≡ ∫ d³X ρ Xa Vb. (3.6.1)

Using the local evolution equations (3.5.1) we obtain

D_i ≡ dSi/dt = ∫ d³X ρ Xa ∂U_tidal/∂Xb. (3.6.2)

Also here the self-potential U does not contribute. We then get:

D = Σ_{A≠E} M_E G Σ_{l=0}^∞ [1/(l! aL bL)]

= Σ_{l=0}^∞ Σ_{j=0}^∞ [(-1)^j M_E M_A ∂E / (l! j! aL J bLJ r)], (3.6.3)

where A ≠ E.

The conversion to the spherical representation is tedious (see Hartmann et al. 1994); one obtains (Y = Y(θ_EA, φ_EA)):

D = G Σ_{A≠E} Σ_{l=0}^∞ Σ_{m=-l}^l Σ_{j=0}^∞ Σ_{k=-j}^j [(-1)^l γlm k M_E^l M_A^j / r^{l+j+1}] [α_{pq} Y_{p,q} - β_{pq} Y_{p,q-1} - im Y_{p,q}], (3.6.4)

where

α ≡ (l+m)(p−q+1)/(2(p+q)), β ≡ (l−m)(p+q+1)/(2(p−q)) (3.6.5)

and

p = l+j, q = m+k.

3.6.1 The Torque Resulting from an External Mass-Monopole

We will now concentrate on the torque

D = ∫ d³X ρ Xa XL G Σ_{l≥0} [1/(l! bL)]

induced by a single external mass-monopole M0. Since

γ00 = 1/√(4π) and MA = 4π M0, the torque is given by:

D = G M_A Σ_{l,m} (−LY_lm)|A / R^{l+1}, (3.6.6)

with

LY_lm = imY_lm for z-component,

and for other components:

LY_lm = + (a+ Y+ + a− Y−) for x-component, LY_lm = + (a+ Y+ − a− Y−) for y-component,

where

a± = [(l±m+1)(l∓m)]^{1/2}

and

Y± = Y^{l,m±1}.

3.6.1.1 The Torque as Lie-Derivative of U

Now, L can be understood as an operator, that has an interesting physical meaning. For an external point-mass the external potential is given by (R = r_EA)

U_ext = GM_A / 3.6 Rotational Equations of Motion

and

∂_c U_ext = −GM_A (Xc − Xc_A) / |X−X_A|^3.

It is easy to see that the term with Xc does not contribute to the torque. Therefore,

D_a = ∫ GM_A Xc_abc d³X ρ Xb / |X−X_A|^3.

Since

∂_b U(X) = −G ∫ d³X’ (Xb − X’_b) / |X−X’|^3,

the torque resulting from a tide generating point-mass MA can be written in the form

D_a = ∫ M_A Xc_abc ∂_b U|_A. (3.6.8)

This equation can be interpreted in the following way:

E_pot ≡ −M_A U_E(X_A) (3.6.9)

is the potential energy of the point-mass M_A in the gravitational field of body E, and the torque (3.6.8) is given in geocentric coordinates X by

D_a = L_a E_pot, (3.6.10)

where

L_a = X_b ∂_c (3.6.11)

is the Lie-derivative with respect to an infinitesimal rotation about the corresponding axis. In quantum-mechanics −iL presents the usual angular-momentum operator (ħ = 1); for that reason many relations involving L can be found in any textbook about quantum-mechanics.

Using

U_E(R,θ,φ) = G Σ_{l=0}^∞ Σ_{m=-l}^l M_lm Y_lm(θ,φ) / R^{l+1}, (3.6.12)

where (R,θ,φ) are the polar coordinates of X (X = R sinθ cosφ, Y = R sinθ sinφ, Z = R cosθ), the torque can be written in the form of (3.6.6):

D = G M_A Σ_{l,m} (−LY_lm)|A / R^{l+1},

since the derivatives of R do not contribute to the torque. The following relations for the angular momentum operator in spherical coordinates are well known:

L_x = −sinφ ∂_θ − cotθ cosφ ∂_φ L_y = +cosφ ∂_θ − cotθ sinφ ∂_φ (3.6.13)

L_z = +∂_φ

Defining

L_± ≡ e^{±iφ} [±∂_θ + i cotθ ∂_φ] (3.6.14)

one finds

L_± Y_lm = i {(l±m+1)(l∓m)}^{1/2} Y^{l,m±1} (3.6.15)

and, in this way, we recover our old formula (3.6.8) for the torque.

## 3.7 The Newtonian 2-Body Problem

3.7.1 Integrals of Motion

Let us consider two celestial bodies as mass-monopoles with masses m1 and m2, that move solely due to their mutual gravitational attractions. Let r1 and r2 be the two position vectors in some suitably chosen inertial coordinate system. From (3.5.5) we get the two dynamical equations

m1 r̈1 = −G m1 m2 (r1 − r2) / |r1 − r2|^3 m2 r̈2 = −G m1 m2 (r2 − r1) / |r2 − r1|^3. (3.7.1)

These equations imply the existence of 12 scalar constants of integration for the two initial positions 7.13)

Here, P is a unit vector (|P| = 1). Since P lies in the orbital plane perpendicular to C, e and P present the last two integration constants. The vector L = GMeP is called the Runge-Lenz vector. From the Laplace-integral (3.7.13) we can write the Runge-Lenz vector in the form

L = v × C − GM r/r = v² − GM/r − (r·v)v. (3.7.14)

3.7.2 Orbital Equation; Kepler’s First and Third Law

The orbital equation can be derived from the Laplace-integral (3.7.13). Since (a × b)·c = (c × a)·b we get

C² = C·C = (r × ṙ)·C = (ṙ × C)·r = GMr (1 + P·r).

We will denote the angle between P and r by f, the true anomaly. With P·r = cos f we get the orbital equation in the form

r = p / (1 + e cos f) (3.7.15)

with p = C²/(GM).

This is Kepler’s first law: the orbit of every planet is an ellipse with the Sun at one of the two foci (Fig. 3.5).

The point of closest approach of the two bodies, the pericenter, is given by f = 0, implying that the Runge-Lenz vector or our vector P points towards the pericenter. The value of the numerical eccentricity e of the conic section indicates if the orbit is an ellipse (e < 1), parabola (e = 1) or hyperbola (e > 1). In case of an ellipse

p = a(1 − e²), (3.7.16)

where a denotes the semi-major axis of the ellipse.

For the elliptical orbit, according to the area rule with A_ellipse = πa²(1 − e²)^{1/2}, C = 2A/T = 2πa²(1 − e²)^{1/2}/T, where T denotes the orbital period. From C² = GMa(1 − e²) we get (2π/n) = (GM)^{1/2} / a^{3/2} with n = (GM/a³)^{1/2}, implying Kepler’s third law in the form GM = n²a³. (3.7.17)

Note, that for two planets moving about the Sun this law in correct form reads 1 = [ (M + m) / (4π² a³) ] T². (3.7.18)

Only if we neglect the planetary masses with respect to the solar mass the cubes of the semi-major axes are proportional to the squares of the orbital periods. Finally we would like to remark that for the motion relative to the center-of-mass |r₁ − r_S| = p₁ / [1 + e cos(f − f₁₀)]; |r₂ − r_S| = p₂ / [1 + e cos(f − f₂₀)]

with p₁ = (m₂/M) p; p₂ = (m₁/M) p.

3.7.3 Classification of the Conic Sections

A classification of the conic sections can be managed by means of the energy-integral (1/2) ṙ² − GM/r = h.

With r = r e_r; ṙ = ṙ e_r + r ḟ e_f we get ṙ² + (r ḟ)² − 2 GM/r = 2h; Furthermore, C = |r × ṙ| = |r e_r × (ṙ e_r + r ḟ e_f)| = r² ḟ.

With r = p/(1 + e cos f) and p = C²/(GM) we get for e < 1: ṙ² = [2GM/r] − [C²/r²] + 2h = [2(GM)²/C²] (1 + e cos f) − [C²(GM)²/C⁴] (1 + e cos f)² + 2h = [ (GM)²/C² ] (1 − e² cos² f) + 2h.

On the other hand ṙ_dot = (p e sin f / (1 + e cos f)²) ḟ = (r² ḟ / p) e sin f = (C / p) e sin f = (μ / C) e sin f, with μ = GM. A comparison reveals ṙ² = (μ²/C²) (1 − e² + e² sin² f) + 2h = (μ² e² / C²) sin² f or h = −(1/2)(μ²/C²)(1 − e²) = −μ / (2a). (3.7.19)

This implies that for an elliptical orbit with e < 1 the specific energy h is negative; the orbit is bound. h is determined by the semi-major axis of the relative motion. Figure 3.6 shows the different conic sections presenting possible orbits in the Keplerian two-body problem.

For the case of hyperbolic orbits with e > 1 one finds h = +μ/(2|a|) > 0 and the specific energy h just vanishes, h = 0, for parabolic orbits with e = 1.

If we write the energy conservation in the elliptical orbit in the form v² = [2μ/r] + 2h = μ [2/r − 1/a], we see that the velocity in a circular orbit, e = 0, is simply v = √(GM/r).

3.7.4 Kepler’s Equation

After we have found the form of the 2-body orbit we now turn to the time dependence in the elliptical orbit. To this end it is useful to introduce Cartesian coordinates with origin in the center of the orbital ellipse. Let b = a(1 − e²)^{1/2} be the semi-minor axis of the ellipse. We then write (x, y) = (a cos E, b sin E), where the angle E is called eccentric anomaly.

From Fig. 3.7 we see that r cos f = a (cos E − e)

r sin f = a (1 − e²)^{1/2} sin E. (3.7.20)

From this we get r = (r² cos² f + r² sin² f)^{1/2} = a (cos² E − 2e cos E + e² + (1 − e²) sin² E)^{1/2} = a (1 − 2e cos E + e² cos² E)^{1/2} or r = a (1 − e cos E). (3.7.21)

This result, using r = a(1 − e²)/(1 + e cos f), leads to an expression for cos f: cos f = (cos E − e) / (1 − e cos E). (3.7.22)

From this we get sin f = [(1 − e²)^{1/2} sin E] / (1 − e cos E) (3.7.23)

and analogous one finds cos E = (e + cos f) / (1 + e cos f); sin E = [(1 − e²)^{1/2} sin f] / (1 + e cos f). (3.7.24)

Later we will need an expression for df/dE. To this end we will first differentiate the expression for sin f, relation (3.7.23), with respect to E: d/dE (sin f) = cos f (df/dE) = d/dE [ (1 − e²)^{1/2} sin E / (1 − e cos E) ]

= (1 − e²)^{1/2} [ (1 − e cos E) cos E − e sin² E ] / (1 − e cos E)² = (1 − e²)^{1/2} (cos E − e) / (1 − e cos E)² and obtain df/dE = (1 − e²) / (1 − e cos E). (3.7.25)

Similarly one finds dE/df = (1 − e²) / (1 + e cos f).

For practical calculations another relation between f and E is useful: tan(f/2) = [1 − cos f] / [1 + cos f] = [1 − e cos E − cos E + e] / [1 − e cos E + cos E − e]

= [ (1 + e)(1 − cos E) ] / [ (1 − e)(1 + cos E) ] = [ (1 + e)/(1 − e) ] tan²(E/2)

or tan(f/2) = [ (1 + e)/(1 − e) ]^{1/2} tan(E/2). (3.7.26)

The time dependence in the elliptical orbit is finally obtained from the area rule. From r² ḟ = C one derives C (t − t₀) = ∫_{f₀}^{f} r²(v) dv = ∫_{E₀}^{E} a² (1 − e cos E)² (df/dE) dE = a² (1 − e²)^{1/2} ∫_{E₀}^{E} (1 − e cos E) dE = a² (1 − e²)^{1/2} [E − e sin E]_{E₀}^{E}, or, using C² = μa(1 − e²)

μ^{1/2} a^{1/2} (t − t₀) = a² [E − e sin E]_{E₀}^{E}.

If we divide both sides by a² we get a factor of (μ/a³)^{1/2} = n on the left hand side. Again, n is the mean motion as it appears in Kepler’s third law, n² a³ = GM. This, finally, leads us to Kepler’s equation M = E − e sin E, (3.7.27)

where the angle M, M = n (t − T) (3.7.28)

is called mean anomaly. For a circular orbit true and mean anomaly are equal. For the elliptical case we image to have a further fictitious body that moves along a circular orbit with the same mean motion, n, as our celestial body. This fictitious body only serves for the calculation of the time dependence in the orbit. The quantity T indicates the time of perigee passage, where M = E = f = 0 and real and fictitious body meet after each revolution.

The time dependence in the elliptical orbit then follows from Eq. (3.7.28): for any instance of time we first compute the mean anomaly M. Kepler’s equation (3.7.27) can then be solved for the eccentric anomaly E and relation (3.7.26) leads to the true anomaly f that appears in the orbital equation (3.7.15).

Given the mean anomaly M, Kepler’s equation presents a transcendental equation for the eccentric anomaly E. Many different methods to solve Kepler’s equation can be found in the literature.

One possibility, for small value of e, is a solution by iteration. Let E₀ be a zeroth order approximation to E, then we can derive a correction ΔE from Kepler’s equation: M = E − e sin E = E₀ + ΔE − e sin(E₀ + ΔE)

= E₀ − e sin E₀ + (1 − e cos E₀) ΔE + ...

i.e., ΔE ≈ (M − M₀) / (1 − e cos E₀); M₀ = E₀ − e sin E₀.

It is clear that this procedure can be iterated; experience shows that for e < 0.2 such an iteration usually converges.

3.7.5 Fourier-Analysis in the Elliptical Orbit

Another possibility to solve Kepler’s equation is to expand E − M = e sin E as an odd function of E (and hence also of M) in a Fourier-series of the form e sin E = Σ_{s=1}^{∞} 2 b_s sin(s M)

with b_s = (1/(sπ)) ∫_{0}^{π} (e sin E) sin(s M) dM = − (1/(sπ)) ∫_{0}^{π} (e sin E) d(cos(s M))

= (1/(sπ)) [ cos(s M) e sin E |_{0}^{π} − ∫_{0}^{π} cos(s M) d(e sin E) ]

= (1/(sπ)) [ 0 − ∫_{0}^{π} cos(s M) dE ]

= (1/(sπ)) ∫_{0}^{π} cos[s (E − e sin E)] dE = J_s(se), where J_s(z) are Bessel-functions (of the first kind). For small values of e these Bessel-functions admit a Taylor-series expansion of the form 2 J₁(1e) = e − e³/8 + O(e⁵)

2 J₂(2e) = e² − e⁴/6 + O(e⁶)

2 J₃(3e) = 9e³/4 + O(e⁵)

2 J₄(4e) = 4e⁴/3 + O(e⁶).

The first terms result from the asymptotic behavior of J_s(z). For fixed values of s (positive integers) and z → 0 one gets: J_s(z) ∼ (1/s!) (z/2)^s.

Therefore, e sin E = Σ_{s=1}^{∞} J_s(se) sin(s M)

and therefore, E = M + Σ_{s=1}^{∞} J_s(se) sin(s M). (3.7.29)

Inserting the Taylor-series expansion for the Bessel-functions we obtain E = M + [ e − (1/8)e³ ] sin M + [ (1/2)e² − (1/6)e⁴ ] sin 2M + [ (9/8)e³ ] sin 3M + [ (2/3)e⁴ ] sin 4M + O(e⁵). (3.7.30)

Also the other variables in the elliptical motion can be expressed in terms of corresponding Fourier-series. E.g., a differentiation of Kepler’s equation with respect to t leads to: n = (1 − e cos E) (dE/dt) = (r/a) (dE/dt), i.e., (a/r) (dE/dt) / n = 1 + 2 Σ_{s=1}^{∞} J_s(se) cos(s M). (3.7.31)

3.7.6 The Elliptical Kepler Orbit in Space

So far we have characterized the position of one celestial body with respect to the other by elements a, e and M, quantities defined in the space-fixed orbital plane. If an arbitrary x-axis is chosen in the orbital plane then we also need the angle between this x-axis and the direction towards the pericenter. This argument of the pericenter is usually denoted by ω. For practical applications it is useful, however, to employ a different reference plane. In satellite theory usually one uses a suitably defined equatorial plane as reference plane for orbital elements.

This situation is depicted in Fig. 3.8. The reference plane, e.g., the celestial equator at a certain epoch, is the x−y-plane of our fundamental Newtonian inertial reference system. The astronomical x-axis might be defined by the vernal equinox, i.e., the intersection of the reference plane with the (mean) ecliptic of the epoch.

The line of intersection between reference and orbital plane is called line of nodes. It defines two points in the Keplerian orbit: the ascending and the descending node. If the body crosses the reference plane from negative (positive) to positive (negative) z-values it goes through the ascending (descending) node. In Fig. 3.8 we see further elements I and Ω that define the orientation of the orbital plane in space. I describes the inclination of the orbital plane with respect to the reference plane. The argument of the ascending node, Ω, describes the angle between the x-axis of our fundamental reference system and the direction towards the ascending node. The argument of the pericenter, ω is reckoned from the ascending node. Altogether, the Keplerian orbit in space can be characterized by six orbital elements (a, e, ω, Ω, I, T), equivalent to the Cartesian vectors of position and velocity for a given 3.7.6.1 Calculation of x and x˙ from the Orbital Elements Let the Cartesian coordinates of our inertial reference system be denoted by (x,y,z). Let us introduce a second (right-handed) Cartesian coordinate system (X,Y,Z) with the properties: the X−Y-plane agrees with the orbital plane and the X-axis points towards the pericenter. The Z-axis points perpendicular to the orbital plane in the direction of the angular momentum vector. The coordinates of our celestial body are then given by X = r cos f = a(cos E − e); Y = r sin f = a(1 − e^2)^(1/2) sin E; Z = 0. (3.7.32)

Using Ė = (a/r)n, that follows from Kepler’s equation, dM/dt = n = (1 − e cos E)Ė, one finds for the velocity Ẋ = −aĖ sin E = −(a^2 n / r) sin E; Ẏ = (a^2 n / r)(1 − e^2)^(1/2) cos E; Ż = 0. (3.7.33)

Now, two right-handed Cartesian coordinate systems with the same origin are related by a rotation matrix, in our case x = R_{xX} · X. (3.7.34)

To get from X to x we first have to rotate about the Z-axis by an angle −ω (a rotation with a positive rotation angle is counter-clockwise if we look from positive values on the rotation axis onto the plane where the coordinate are rotated) which transforms the X-axis into the line of nodes, a second rotation about this new X′-axis by an angle −I so that the new X′′−Y′′-plane agrees with the fundamental x−y-plane, plus a third rotation about the z-axis by an angle −Ω. Thus, R_{xX} = R_3(−Ω) · R_1(−I) · R_3(−ω) (3.7.35)

with R_1(θ) = ⎛ 1   0       0    ⎞ ⎝ 0   cos θ   sin θ ⎠ (3.7.36)

0  −sin θ   cos θ and R_3(θ) = ⎛ cos θ   sin θ   0 ⎞ ⎝−sin θ   cos θ   0 ⎠ . (3.7.37)

0       0       1 One finds: R_{xX} = cos Ω cos ω − sin Ω sin ω cos I R_{xY} = −cos Ω sin ω − sin Ω cos ω cos I R_{xZ} = sin Ω sin I R_{yX} = sin Ω cos ω + cos Ω sin ω cos I R_{yY} = −sin Ω sin ω + cos Ω cos ω cos I R_{yZ} = −cos Ω sin I R_{zX} = sin ω sin I R_{zY} = cos ω sin I R_{zZ} = cos I. (3.7.38)

Since the same rotation matrix applies for the corresponding velocity vectors, Ẋ and ẋ, we can express x and ẋ by means of the orbital elements. E.g., one gets x = R_{xX} X + R_{xY} Y + R_{xZ} Z = [cos Ω cos ω − sin Ω sin ω cos I] r cos f + [−cos Ω sin ω − sin Ω cos ω cos I] r sin f = r[cos Ω (cos ω cos f − sin ω sin f) − sin Ω (sin ω cos f + cos ω sin f) cos I]

= r[cos Ω cos(ω + f) − sin Ω sin(ω + f) cos I].

In this way for the position vector one finds: x = r[cos Ω cos u − sin Ω sin u cos I]

y = r[sin Ω cos u + cos Ω sin u cos I]

z = r sin u sin I, (3.7.39)

where u ≡ ω + f.

For any given instance of time r can be obtained from r = p / (1 + e cos f), where p = a(1 − e^2). The true anomaly f results from the Kepler equation and relation (3.7.26) between f and E.

3.7.6.2 Calculation of Orbital Elements from x and ẋ The specific angular momentum vector C = x × ẋ has Cartesian components C_x = y ż − z ẏ C_y = z ẋ − x ż (3.7.40)

C_z = x ẏ − y ẋ, from which we can calculate the quantity p (μ = GM): p = C^2 / μ. (3.7.41)

With r^2 = x^2 one obtains the semi-major axis a from v^2 = ẋ^2 = μ (2/r − 1/a). (3.7.42)

The inclination I is obtained from I = arccos[C_z / C]. (3.7.43)

We then compute the Runge-Lenz or eccentricity vector L = (v^2 − μ/r) x − (x · v) v (3.7.44)

from which we get the eccentricity by e = |L| / (GM) (3.7.45)

and the true anomaly f by f = arccos (L · x) / (|L| |x|)   for x · v ≥ 0 2π − arccos (L · x) / (|L| |x|) otherwise. (3.7.46)

The eccentric anomaly E is then given by E = 2 arctan[ sqrt((1+e)/(1−e)) tan(f/2) ]. (3.7.47)

The longitude of the ascending node Ω and the argument of the pericenter ω are then obtained by means of the nodal vector n pointing towards the ascending node: n = e_z × C = (−C_y, C_x, 0). (3.7.48)

One has Ω = arccos (n_x / |n|)   for n_y ≥ 0 2π − arccos (n_x / |n|) for n_y < 0 (3.7.49)

and ω = arccos (L · n) / (|L| |n|)   for L_z ≥ 0 2π − arccos (L · n) / (|L| |n|) for L_z < 0. (3.7.50)

Finally the mean anomaly M is obtained from Kepler’s equation M = E − e sin E.

## 3.8 Perturbation Theory

3.8.1 Variation of Constants Let us now consider a perturbed Keplerian problem, where the equation of motion takes the form r̈ = ∇(U + R) (3.8.1)

with U = GM / r.

Here, the quantity R is called perturbing function and we will assume that |R| << |U|.

Without the perturbing function R we face our Kepler-problem that is completely integrable with r = r(α, t); ṙ = ṙ(α, t). (3.8.2)

Here α stands for the complete set of orbital elements α = (a, e, I, Ω, ω, T).

We now think of getting a solution of (3.8.1) by considering the orbital elements α as time dependent quantities. In this case one speaks of variation of constants. We can then write dr/dt = ∂r/∂t + Σ (∂r/∂α_i) dα_i/dt ≡ ∂r/∂t + (∂r/∂α) · α̇.

If, for each instance of time, we want the velocity in the perturbed orbit to agree with the corresponding velocity of the instantaneous Keplerian orbit, we can require an osculation condition of the form (∂r/∂α) · α̇ = 0. (3.8.3)

In that case the perturbed orbit is described with osculating orbital elements. For each instance of time the elements α(t) describe an osculating ellipse that yields the position and velocity in the actual perturbed orbit.

3.8.2 Perturbation Equations, Derived from Vectorial Elements 3.8.2.1 Vectorial Elements in the Kepler-Problem In the Kepler problem we had r̈ = −(GM / r^2) (r / r)

and for each instance of time t the solution is given by the six time independent orbital parameters a, e, I, Ω, ω and M = −nT. The first five of these orbital elements are determined by the vectors C, the specific angular momentum vector, and L, the Runge-Lenz vector, with C = r × ṙ; L = ṙ × (r × ṙ) − (GM) (r / r).

We now introduce a system of three orthonormal unit vectors, l, m, k, such that: – l lies in the nodal line of the orbit pointing towards the ascending node, – m lies in the orbital plane perpendicularly to l – k in the direction of C, perpendicular to the orbital plane.

These unit vectors (Fig. 3.9) are given by l = (cos Ω, sin Ω, 0); m = (−cos I sin Ω, cos I cos Ω, sin I); k = (sin I sin Ω, −sin I cos Ω, cos I). (3.8.4)

The position vector can then be written as r = r [l cos(ω + f) + m sin(ω + f)].

In the orbital plane we can rotate the two unit vectors l and m by the angle ω such that one of them, P, points towards the pericenter P = l cos ω + m sin ω; Q = −l sin ω + m cos ω. (3.8.5)

The two vectorial elements C and L can then be written as (p = a(1−e^2)): C = (GM p)^(1/2) k; L = GMe P. (3.8.6)

For the Keplerian orbit we have: r = r (P cos f + Q sin f) (3.8.7)

ṙ = (GM / p)^(1/2) [−P sin f + Q (cos f + e)]. (3.8.8)

3.8.2.2 Perturbation Theory with Vectorial Elements With a perturbing acceleration F the dynamical equation now reads r̈ = −(GM / r^2) (r / r) + F. (3.8.9)

We now image a solution of this equation to be given by a set of osculating elements. Five of these six elements can be derived from the vectorial elements k, P and Q. The time dependence of a, e, I, Ω and ω is then determined by the time dependence of these three vectorial elements. E.g., dk/dt = d/dt (sin I sin Ω, −sin I cos Ω, cos I)

= sin I dΩ/dt (cos Ω, sin Ω, 0) + dI/dt (cos I cos Ω, cos I sin Ω, −sin I)

= sin I dΩ/dt l + dI/dt m, or dk/dt = sin I dΩ/dt l − dI/dt m. (3.8.10)

Similarly one finds dP/dt = (dω/dt + dΩ/dt cos I) Q + (dI/dt sin ω − dΩ/dt cos ω sin I) k (3.8.11)

dQ/dt = −(dω/dt + dΩ/dt cos I) P + (dI/dt cos ω + dΩ/dt sin ω sin I) k. (3.8.12)

From these relations we can derive the temporal variations of the two vectorial elements C and L. From dC/dt = (GM p)^(1/2)/2 p dp/dt k + (GM p)^(1/2) dk/dt we get dC/dt = (GM p)^(1/2)/2 p dp/dt k + (GM p)^(1/2) (sin I dΩ/dt l − dI/dt m). (3.8.13)

From dL/dt = GM de/dt P + GMe dP/dt it follows that dL/dt = GM de/dt P + GMe [(dω/dt + dΩ/dt cos I) Q + (dI/dt sin ω − dΩ/dt cos ω sin I) k]. (3.8.14)

On the other hand there are relations between the Runge-Lenz vector L and the perturbing acceleration F. From C = r × ṙ; dC/dt = r × r̈ one sees that dC/dt = r × F. (3.8.15)

Due to L = ṙ × (r × ṙ) − (GM) (r / r)

one finds that dL/dt = d/dt [ṙ × (r × ṙ)] − d/dt [ (GM) (r / r) ]

= r̈ × (r × ṙ) + ṙ × (r × r̈) − (GM) d/dt (r / r).

The last term cancels with the corresponding term in the unperturbed equation so that we obtain dL/dt = F × (r × ṙ) + ṙ × (r × F)

= 2(ṙ · F) − (r · F) ṙ − (r · ṙ) F. (3.8.16)

A scalar multiplication of dC/dt with k, l, m and of dL/dt with P and Q yields five independent perturbation equations (Fig. 3.10).

Let us derive two of them in detail. From GM = n^2 a^3 we get (GM p)^(1/2) = (n^2 a^4 (1−e^2))^(1/2) = n a^2 sqrt(1−e^2).

Using (3.8.13) we get dC/dt · l = n a^2 sqrt(1−e^2) sin I dΩ/dt = (r × F) · l.

Now, r = r [l cos(ω + f) + m sin(ω + f)], so that the right hand side is equal to r sin(ω + f) (m × F) · l = r sin(ω + f) (l × m) · F = r sin(ω + f) W, with W ≡ k · F.

From this we finally obtain dΩ/dt = [r sin(ω + f) / (n a^2 sqrt(1−e^2) sin I)] W.

If we project the C-equation onto m, we obtain −n a^2 sqrt(1−e^2) dI/dt = dC/dt · m = (r × F) · m = r cos(ω + f) (l × F) · m = r cos(ω + f) (m × l) · F = −r cos(ω + f) W.

Hence, dI/dt = [r cos(ω + f) / (n a^2 sqrt(1−e^2))] W.

We define S ≡ (1/r) (r · F), T ≡ (1/r) (k × r) · F, W ≡ k · F. (3.8.17)

S is the radial component of F, T the transverse component perpendicular to the radial direction in the orbital plane. W is called the normal component of F. Since r = r (P cos f + Q sin f)

we have S = (P · F) cos f + (Q · F) sin f T = (Q · F) cos f − (P · F) sin f.

In this way five (out of a total number of six) perturbation equations can be derived: da/dt = (2p / (n sqrt(1−e^2))) [S e sin f + T (1 + e cos f) / r]

de/dt = (sqrt(1−e^2) / (n a)) [S sin f + T (cos f + cos E)]

dI/dt = [r cos(ω + f) / (n a^2 sqrt(1−e^2))] W dΩ/dt = [r sin(ω + f) / (n a^2 sqrt(1−e^2) sin I)] W dω/dt = −cos I dΩ/dt + (sqrt(1−e^2) / (n a e)) [−S cos f + T (1 + r/p) sin f]. (3.8.18)

These equations have to be augmented with an additional one for M or T. This last equation will be derived from the osculation condition for the velocity dr/dt. From r = r (P cos f + Q sin f) we obtain dr/dt = ṙ (P cos f + Q sin f) + r (−P sin f + Q cos f) df/dt + r (Ṗ cos f + Q̇ sin f).

Inserting Ṗ, Q̇ and ṙ = (GM/p)^(1/2) e sin f we obtain: ṙ = (GM/p)^(1/2) e sin f (P cos f + Q sin f) + r (−P sin f + Q cos f) df/dt + r [ (dω/dt + dΩ/dt cos I) Q + (dI/dt sin ω − dΩ/dt cos ω sin I) k ] cos f + r [ −(dω/dt + dΩ/dt cos I) P + (dI/dt cos ω + dΩ/dt sin ω sin I) k ] sin f.

Solving for df/dt and using the definition of the mean motion n = (GM/a^3)^(1/2) and the relation between the eccentric and true anomaly leads to the sixth perturbation equation, which describes the time evolution of the mean anomaly M.

I +k sinω −cosωsinI cosf dt dt dt dt dω dΩ dI dΩ +r −P +cosI +k cosω +sinωsinI sinf .

dt dt dt dt The osculation condition then implies that the right hand side of this equation, according to (3.8.8), should be equal to GM [−Psinf +Q(cosf +e)].

The terms proportional to Q yield df na2 dω dΩ = 1−e²− +cosI .

dt r² dt dt Correspondingly, for the eccentric anomaly one finds dE na r dω dΩ sinf de = − +cosI + .

dt r a(1−e²)¹/² dt dt 1−e² dt Using Kepler’s equation, M =E−esinE, we get dM dE de dE r dE de = − sinE−ecosE = −sinE .

dt dt dt dt a dt dt In the Kepler problem we had M =M₀ +n(t −T), that, in case of osculating elements, leads to dM dM₀ dn =n+ 0 + ·(t −T).

dt dt dt This implies, that we would in the time derivative of the mean anomaly we would face terms proportional to time t. To avoid such terms in the presence of perturbations, one defines the mean anomaly via M =M₀ + ndt. (3.8.19)

t₀ Then, dM dM₀ r dE de =n+ 0 = −sinE .

dt dt a dt dt In this equation we can finally insert the expressions for the time derivatives of E and e. In this way the last perturbation equation can be derived. It reads: dM dω dΩ 2r 0 =− 1−e² +cosI −S . (3.8.20)

dt dt dt na² Equations (3.8.18) and (3.8.20) are the usual celestial mechanical perturbation equation in STW-form (or Gauss-form). So far these equations are exact, i.e., it was not assumed that the perturbation is small compared to the Keplerian acceleration.

Instead of the argument of perigee ω and the mean anomaly M one often uses the longitude of perihelion ϖ, and the mean longitude at the epoch λ, given by ϖ =ω+Ω (3.8.21)

and M +ϖ = ndt +λ. (3.8.22)

These quantities obey the relations dϖ dΩ I 1−e² r =2 sin² + −Scosf +T 1+ sinf (3.8.23)

dt dt 2 nae p and dλ e² dϖ dΩ I 2rS = √ +2 1−e² sin² − . (3.8.24)

dt 1+ 1−e² dt dt 2 na² To derive another form of the perturbation equations that was first derived by Lagrange, we assume that the perturbing acceleration can be derived from a potential R =R(t,r), the perturbing function, ∂R F= . (3.8.25)

∂r Let α be some orbital element. Then, ∂R ∂R ∂r ∂r = · =F· .

∂α ∂r ∂α ∂α From r =a(1−ecosE) one finds ∂r/∂a =r/a and, therefore, ∂r r = , ∂a a leading to ∂R ∂r 1 r =F· = F·r= S. (3.8.26)

∂a ∂a a a Similarly one finds ∂R r =a −cosf S+sinf 1+ T ∂e p ∂R =rW sin(ω+f)

∂I ∂R =rT (3.8.27)

∂ω ∂R =rT cosI −rcos(ω+f)sinIW ∂Ω ∂R a p = √ esinf S+ T .

∂M 1−e² r Inserting these relations into the STW-form of the perturbation equations (3.8.18)

and (3.8.20), we obtain the Lagrange-equations in the form: da 2 ∂R =− dt n²a∂T de 1 ∂R 1 ∂R =− 1−e² + (1−e²)

dt na²e ∂ω n ∂T dI 1 ∂R ∂R = √ cosI − dt na² 1−e²sinI ∂ω ∂Ω dω 1−e² ∂R cotI ∂R = − √ (3.8.28)

dt na²e ∂e na² 1−e² ∂I dΩ 1 ∂R = √ dt na² 1−e²sinI ∂I dT 1−e² ∂R 2 ∂R = + .

dt n²a²e ∂e n²a ∂a Exercise 3.11 Derive the Lagrange perturbation equations.

Solution From dΩ rsin(ω+f)

= √ W dt na² 1−e²sinI and ∂R rWsin(ω+f)= ∂I we get the dΩ/dt equation. Furthermore, dI rcos(ω+f)sinI = √ W dt na² 1−e²sinI ∂R =(na² 1−e²sinI) −1 − +rcosIT ∂Ω ∂R ∂R =(na² 1−e²sinI) −1 − +cosI .

∂Ω ∂ω The last Lagrange-equation for the time of passage through the pericenter T, can also be written in the form dM 1−e² ∂R 2 ∂R =n− − . (3.8.29)

dt na²e ∂e na ∂a To employ the Lagrange form of the perturbation equation the perturbing acceler- ation requires a scalar potential, R, that has to be expressed in terms of the orbital elements R =R(a,e,I,Ω,ω,T).

Exercise 3.12 Calculate the secular Newtonian perihelion precession of Mercury’s orbit due to the gravitational action of an outer planet with mass M* and semi-major axis a*. To this end smear the mass M* along a ring of radius a*. Consider the orbit of Mercury to lie in the ring’s plane. Employ Gauss’ perturbation equation for ω (Mercury) by considering only lowest order terms in the eccentricity e of Mercury’s orbit.

Solution From Exercise 3.4 we know that the ring produces a radially outward acceleration of form GM* ∞ ( r )²ᵏ⁻¹ a_ring = ² * Σ P₂ₖ(0) · n ≡ S · n.

a* a* 2k k=1 Gauss’ perturbation equation for the argument of perihelion ω reads S cosf ω˙ =− , nae where we neglected e²-terms in the numerator. Using GM =n²a³ (M: solar mass)

the average precession velocity per revolution of Mercury reads: M* n ∞ ( a )²ᵏ⁺¹ (ω˙)_rev =− (2k)P₂ₖ(0) < cosf > , (3.8.30)

M e 2k a* k=1 where 1 2π <Q>≡ QdM.

2π Since df a = +O(e²)

dM r we get r²ᵏ⁻¹ 1 2π r²ᵏ⁺¹ e < cosf >= cosf df =− (2k+1).

a 2π a 2 The average perihelion precession (radians) per revolution therefore reads: M* ∞ ( a )²ᵏ⁺¹ (Δω)_rev =π η (3.8.31)

M k a* k=1 with ηₖ =2k(2k+1)P₂ₖ(0).

One has 3 45 525 11025 218295 η₁ = η₂ = η₃ = η₄ = η₅ = .

2 16 128 2048 32768 Mercury makes 414.9 revolutions per century so to get the result in arcsec/century one has to multiply the precession per revolution, (3.8.31), by a factor of

## 414.9 3600

2π For the contributions of the various planets to Mercury’s secular perihelion preces- sion see Table 3.1. Modern values are from Will (1993).

Table 3.1 Perihelion precession of Mercury’s orbit due to outer planets in arcsec./century Pert. planet Modern value Le Verrier Value from (3.8.31)

Venus 277.8 280.6 280.9 Earth 90.0 83.6 95.0 Mars 2.5 2.6 2.3 Jupiter 153.6 152.6 159.9 Saturn 7.3 7.2 7.7 Exercise 3.13 Compute the precession of Mercury’s longitude of perihelion ϖ = Ω + ω due to the oblateness J₂ of the Sun by means of Lagrange’s perturbation equations. To this end consider a non-vanishing small inclination of Mercury’s orbit with respect to the solar equator.

Solution The relevant perturbation equations read: dω 1−e² ∂R cotI ∂R = − √ dt na²e ∂e na² 1−e² ∂I dΩ 1 ∂R = √ .

dt na² 1−e²sinI ∂I From (3.3.20) we find a perturbing function of the form GM R² 2 3 1 R =− J cos²θ − , (3.8.32)

r r 2 2 where cosθ = z/r = sinIsinu (u = ω+f). Inserting R into the corresponding perturbation equation we get (p =a(1−e²))

dω 3 R² 2 5 = J n 2− sin²I dt 2 p 2 or R² 2 5 (Δω)_rev =3πJ₂ 2− sin²I (3.8.33)

2 p 2 for the drift per revolution. Neglecting the inclination term we get: R² 2 (Δω)_rev =6πJ₂ . (3.8.34)

Similarly for the secular drift of the node one obtains: dΩ 3 R² =− J ncosI, (3.8.35)

dt 2 p or R² (ΔΩ)_rev =−3πJ₂ cosI. (3.8.36)

Neglecting the inclination, we end up with a secular precession of Mercury’s longitude of perihelion ϖ of (e.g., Will 1993)

R² 2 (Δϖ)_rev =3πJ₂ . (3.8.37)

Inserting numbers J₂ = 2×10⁻⁷, R = 6.96×10⁸m, a = 5.79×10¹⁰m and e=0.2 we obtain a drift for ϖ of Δϖ =1.3×10⁵ J₂ =2.6×10⁻² arc-seconds per century.

## Chapter

Relativity

## 4.1 Relativity

Already in 1864 Maxwell (1864, 1865) published his fundamental equations of electromagnetism that contain a central natural constant: the vacuum speed of light c. Later, it was found by experiments that the vacuum speed of light velocity c obeys a principle of constancy. This principle of the constancy of the speed of light in vacuum has a harmless part, as well as a critical one. The harmless part says that c is independent of light frequency, amplitude and polarization, as well as the speed of light-source. The critical part, however, says that the vacuum speed of light is also independent upon the speed of the observer which was first tested in the famous experiment by Michelson and Morley (1887) (for modern tests see e.g., Antonini et al. 2005; Eisele et al. 2009; Haugan and Will 1987; Herrmann et al. 2005, 2009; Müller et al. 2003, 2007; Stanwix et al. 2005, 2006; Wolf et al. 2003, 2004). Because of this constancy of the vacuum speed of light, the absolute character of Newtonian space-time had to be abandoned and the Galilean group that relates different inertial systems in the absence of gravity has to be replaced by the Lorentz (Poincaré)

group. A space-time with this symmetry is called ‘relativistic’. In the absence of gravitational fields the physical structure is called ‘Special Relativity’. Einstein’s theory of gravity is called ‘General Relativity’, though it is not more relativistic than ‘Special Relativity’ and both theories will be formulated covariantly (of course accelerated observers can be discussed in the framework of ‘Special Relativity’).

## 4.2 Electrodynamics and Special Theory of Relativity

4.2.1 Maxwell’s Equations We will discuss the theory of electromagnetism first in the absence of gravity. In that case a set of preferred inertial coordinates t and ξⁱ can be introduced in which dynamical equations of motion take a particularly simple form. Introducing four time-space coordinates of the same dimension (length), xμ = (x⁰,x¹,x²,x³) = (ct,ξⁱ), we will call them Minkowskian coordinates in the following. The charge density ρ(t,x) and the current density j(t,x) act as sources of the electromagnetic field. Since j represents the flow of moving charges it is related with ρ by a continuity equation expressing the law of charge conservation of the form ∂ρ +∇·j=0 (4.2.1)

∂t in Minkowskian coordinates. Introducing a contravariant charge-current vector jμ in a four-dimensional Minkowskian space-time by jμ =(cρ,j) (4.2.2)

the continuity equation (4.2.1) can be written simply as jμ =0 (4.2.3)

,μ since ∂jμ ∂j⁰ ∂jⁱ ∂ρ jμ = = + = +∇·j=0.

,μ ∂xμ ∂ct ∂ξⁱ ∂t The electromagnetic field in vacuum is described by the electric field strength E(t,x) and the magnetic field strength B(t,x). These We are related with the field sources by the inhomogeneous Maxwell equations ∇·E = ρ/ε₀  (4.2.4)

∇×B = (1/c²) ∂E/∂t + μ₀j.  (4.2.5)

Here, ε₀ = 8.8542 × 10⁻¹² C²N⁻¹m⁻²  (4.2.6)

is the electric permittivity of free space and μ₀ = 4π10⁻⁷ NA⁻²  (4.2.7)

is the magnetic permeability of free space. These two constants are related with the vacuum speed of light by c² = 1/(ε₀μ₀).  (4.2.8)

The first Maxwell equation (4.2.4) is Coulomb’s law. For a point charge Q located at the origin of our coordinate system we have ∫_V (∇·E) d³x = ∮_∂V E·df = 4πr²E, where Gauß’ theorem was used, so that E(t,x) = (1/(4πε₀)) * (Q/r²) * (x/r)  (4.2.9)

(Coulomb’s law). With the Coulomb potential Φ(t,x) = (1/(4πε₀)) * (Q/r)  (4.2.10)

the electric field strength vector E is obtained from E = -∇Φ.  (4.2.11)

The second Maxwell equation (4.2.5) describes Ampère’s law.

The remaining two homogeneous Maxwell equations read: ∇·B = 0  (4.2.12)

∇×E + ∂B/∂t = 0.  (4.2.13)

The third equation (4.2.12) states the absence of free magnetic monopoles whereas the last one describes Faraday’s law.

It is convenient to introduce the electromagnetic field strength tensor Fαβ = ⎛ 0         Eₓ/c      Eᵧ/c      E_z/c    ⎞ ⎜-Eₓ/c      0        -B_z       B_y      ⎟.

⎜-Eᵧ/c      B_z       0        -B_x     ⎟ ⎝-E_z/c    -B_y       B_x       0        ⎠ (4.2.14)

Note that F₀ᵢ = c⁻¹Eᵢ; Fᵢⱼ = εᵢⱼₖBₖ.  (4.2.15)

Here εᵢⱼₖ = +1 if (ijk) is an even permutation of (123), it is -1 for an odd permutation of (123) and zero otherwise. The inhomogeneous Maxwell equations can then be written as Fαβ,β = μ₀jα.  (4.2.16)

Exercise 4.1 Proof that (4.2.16) is equivalent to the two inhomogeneous Maxwell equations (4.2.4) and (4.2.5).

Solution: If we put α = 0 we get ∂_μ F⁰μ = (1/c) ∂F⁰ⁱ/∂xⁱ = (1/c) ∇·E = μ₀cρ.

Since c² = (ε₀μ₀)⁻¹ Maxwell’s equation (4.2.4) is recovered.

For α = i one finds Eq. (4.2.5): (1/c) ∂Fⁱ⁰/∂t + ∂Fⁱʲ/∂xʲ = -(1/c²) ∂Eⁱ/∂t + εⁱⱼₖ ∂Bₖ/∂xʲ = μ₀jⁱ.

The homogeneous Maxwell equations (4.2.12) and (4.2.13) can be written in the form Fαβ,γ + Fβγ,α + Fγα,β = 0,  (4.2.17)

where F^αβ = ⎛ 0        -Eₓ/c     -Eᵧ/c     -E_z/c   ⎞ ⎜ Eₓ/c      0        -B_z       B_y      ⎟.

⎜ Eᵧ/c      B_z       0        -B_x     ⎟ ⎝ E_z/c    -B_y       B_x       0        ⎠ (4.2.18)

Note that F^αβ is obtained from Fαβ by changing the sign of E.

Exercise 4.2 Proof that (4.2.17) is equivalent to the two homogeneous Maxwell equations (4.2.12) and (4.2.13).

Proof: Taking α = 1, β = 2, γ = 3 we get ∂F₁₂/∂x³ + ∂F₂₃/∂x¹ + ∂F₃₁/∂x² = ∂B_z/∂z + ∂Bₓ/∂x + ∂B_y/∂y = ∇·B = 0.

If we set one index to zero, e.g., α = 0, one finds e.g., for β = 1, γ = 2: ∂F₀₁/∂x² + ∂F₁₂/∂x⁰ + ∂F₂₀/∂x¹ = -(1/c) ∂Eₓ/∂y + (1/c) ∂B_z/∂t + (1/c) ∂E_y/∂x, i.e., the z-component of (4.2.13).

Introducing an electromagnetic potential vector Aμ by Fμν = Aν,μ - Aμ,ν  (4.2.19)

and Aμ = (Φ/c, A) ≡ (A₀, Aⁱ)  (4.2.20)

we find e.g., Eₓ = cF₀¹ = c(A¹,₀ - A₀,₁) = -∂ₓΦ - ∂_t Aₓ and B_z = F₁₂ = A₂,₁ - A₁,₂ = ∂ₓA_y - ∂_y Aₓ.

Generally one has E = -∂A/∂t - ∇Φ, B = ∇×A.  (4.2.21)

Note that from the last relations the components of the potential vector Aμ are not determined uniquely; instead one can impose certain gauge conditions that fix Aμ. One useful gauge condition is the Lorentz-gauge A^α,α = (1/c²) ∂_t Φ + ∇·A = 0.  (4.2.22)

With the Lorentz-gauge the inhomogeneous Maxwell equations take the form □A^α = -(1/c²) ∂²A^α/∂t² + ∇²A^α = -μ₀j^α.  (4.2.23)

Here □ is the usual Laplacian ∇² = ∂²/∂x² + ∂²/∂y² + ∂²/∂z².  (4.2.24)

Exercise 4.3 Show that the last statement is true. First write (4.2.4) and (4.2.5) with the potentials Φ and A. Then use the Lorentz-gauge condition to derive the wave equation (4.2.23).

A special solution of the inhomogeneous wave equation (4.2.23) is given by the retarded potential A^α_ret(t,x) = (μ₀/4π) ∫ [j^α(t_ret, x') / |x - x'|] d³x',  (4.2.25)

where t_ret ≡ t - |x - x'|/c  (4.2.26)

is called the retarded time.

We finally come to the equation of motion for a sufficiently small test charge q. In a Minkowskian coordinate system it reads dp/dt = q (E + v × B/c).  (4.2.27)

Here p is the momentum of the particle with charge q and the right hand side is known as the Lorentz-force.

## 4.3 The Minkowskian Metric, Lorentz-Transformation

It is quite obvious that the 3-dimensional space in SRT is the Euclidean R³. There are several equivalent ways to introduce a 4-dimensional space-time metric tensor gμν in Minkowski space. We first consider the differential operator appearing in the wave-equation (4.2.23): □ ≡ - (1/c²) ∂²/∂t² + ∇²  (4.3.1)

that can be written as □ = ημν ∂/∂x^μ ∂/∂x^ν,  (4.3.2)

where ημν = diag(-1, +1, +1, +1) ≡ ημν  (4.3.3)

is a good candidate for a 4-dimensional metric tensor. Let us consider the vacuum wave equation □A^α = 0  (4.3.4)

in Minkowskian coordinates. Obviously plane waves A^α(t,x) = A^α₀ exp(ik_μ x^μ) ≡ A^α₀ exp(iϕ)  (4.3.5)

are solutions of the wave equation provided -k₀k⁰ + k_ikⁱ = ημν k_μ k_ν = 0 = ημν k^μ k^ν, where k_μ = (-k₀, k_i).  (4.3.6)

If we consider ημν as components of a metric tensor gμν (μ,ν = 0,1,2,3) in Minkowskian coordinates then the wave vectors k or k^μ are of zero length; they are called null-vectors. Integral curves of k^μ are light-rays that run perpendicular to the surfaces of constant phase ϕ. Let us consider a certain light-ray x^μ(λ). The curve parameter is assumed to have the dimension of length, e.g., λ = ct. In a certain point its tangent vector is given by dx^μ/dλ ∝ k^μ and we will choose the constant such that k^μ = (f/c) * dx^μ/dλ  (4.3.7)

(the wave vector) has the dimension of an inverse length and f is a constant frequency (Fig. 4.1).

Fig. 4.1 Surfaces of constant phase, light rays and wave-vectors k.

From 0 = ημν k^μ k^ν = ημν (dx^μ/dλ) (dx^ν/dλ) = gμν (dx^μ/dλ) (dx^ν/dλ)  (4.3.8)

the identification of ημν with a metric tensor becomes clear. In other words: in the 4-dimensional Minkowskian manifold one introduces a metric tensor gμν that reduces to ημν in Minkowskian coordinates. From a physical point of view this metric tensor has several fundamental properties. As we have already seen: Metric Property 1: Light-rays are curves of zero length (null-curves).

In Minkowskian coordinates this simply means that 0 = ds² = -c²dt² + dx², i.e., the speed of light c takes a constant value in every Minkowskian coordinate system.

This constancy of the speed of light has profound consequences for our understanding and measurement of time. Consider some primitive version of an idealized light-clock consisting of two mirrors in vacuum (see Fig. 4.2) with constant separation L and some light signal bouncing to and fro between the two mirrors. At first the two mirrors are considered to be at rest. In that case the time needed for the signal to travel from one mirror to the other and back is given by 2L Δτ = --- .

In the right part of Fig. 4.2 the same situation is depicted with the two mirrors moving in the direction of their extensions with constant speed v. Also in this case the observer measures the same propagation velocity for the light pulse. According to the Pythagorean theorem we now get (v Δt / 2)² + L² = (c Δt / 2)² from which we derive Δτ Δt = ------ .

√(1 - v²/c²)

In words: a moving clock appears to go slower.

Fig. 4.2 (a) the light-clock at rest. Here a light impulse is reflected to and fro between two mirrors of constant separation L; (b) the moving light-clock. Here the two mirrors move with constant speed v with respect to some observer along the mirror’s extensions.

Metric Property 2: If x^μ(λ) is the worldline of an idealized clock then the proper time interval dτ as indicated by the clock is related with the metric tensor via: dτ² = -ds² / c²  (4.3.10)

where the length element ds refers to two neighbouring points on x^μ(λ).

Let us describe the clock’s worldline in Minkowskian coordinates x^μ. Then ds² = -c²dt² + dx² = -c²dt² (1 - v²/c²)

or -ds² / c² = dt²(1 - v²/c²)

in accordance with relation (4.3.9).

Exercise 4.4 Compute the metric tensor gμν with a Minkowskian time coordinate t and spatial spherical coordinates r, θ, φ.

Solution: It is clear that we only have to take the metric of Euclidean R³ from Eq. (2.8.5) and add the time part of the metric, i.e., ds² = -c²dt² + dr² + r²(dθ² + sin²θ dφ²).  (4.3.11)

For a massive particle or body proper time τ is a natural quantity to parametrize its worldline γ: x^μ(τ). The tangent vector onto γ u^μ ≡ dx^μ/dτ = (c, vⁱ)  (4.3.12)

with dxⁱ vⁱ = ---  (4.3.13)

dt is called 4-velocity of the body. In Minkowskian coordinates we have ημν u^α u^β = ημν (dx^α/dτ)(dx^β/dτ) = ds²/dτ² = -c².  (4.3.14)

The introduction of a 4-dimensional metric tensor gμν has many advantages. E.g., one can relate co- and contravariant components of a tensor as in A_μ = gμν A^ν; Tαβ = gασ T^σ_β  (4.3.15)

etc. Furthermore, all equations of physics can be written in a coordinate independent manner, i.e., in covariant form, by using covariant derivatives. E.g., Maxwell’s equations in any coordinate system take the form (4π/c) jα = Fαβ;β  (4.3.16)

F[αβ;γ] = 0  (4.3.17)

and the continuity equation can be written as jμ;μ = 0.  (4.3.18)

Let us come to the force equation for a small test charge q. Let us define fμ ≡ Fμν u^ν  (4.3.19)

with u_ν = gμν u^μ.

In Minkowskian coordinates where gμν = ημν we have u_ν = (-c, vⁱ). The spatial part of fμ then reads in such coordinates fⁱ = Fⁱ⁰ u₀ + Fⁱʲ u_j = cEⁱ + εⁱⱼₖ Bₖ vʲ or f = q(E + v × B/c)  (4.3.20)

proportional to the Lorentz-force from Eq. (4.2.27). Let pμ = mu^μ = (p⁰, p)  (4.3.21)

be the 4-momentum of a body of mass m and Du^μ a^μ ≡ --- = u^μ;ν u^ν  (4.3.22)

dτ its 4-acceleration. Then the covariant version of the force equation (4.2.27) reads ma^μ = Fμν u^ν.  (4.3.23)

Finally the metric tensor leads to a generalization of the Galilean group. We have already used the fact that the metric tensor gμν takes the same form in every set of inertial (Minkowskian) coordinates, i.e., gμν = ημν = diag(-1, +1, +1, +1).  (4.3.24)

We can use this condition of metric invariance to derive the transformation rules between two such inertial coordinate systems x^μ and x'^ν. Assuming first the two x-axes to be aligned and v is the constant velocity of the x'-system with respect to the x-system, then one finds a space-time coordinate transformation of the form (y' = y, z' = z)

t' = γ (t - vx/c²)

x' = γ (x - vt)  (4.3.25)

with γ ≡ (1 - v²/c²)^(-1/2).  (4.3.26)

Obviously this restricted Lorentz-transformation reduces to the Galilean-transfor For some calculations the relation (βi ≡ vi/c)

viγ2 v (γ − 1) = βiβ (4.3.30)

v2 1+γ k is useful. The inverse transformation, x → x, reads: v·x t = γ t + c2 (4.3.31)

(x·v)

x = x + (γ − 1) v + γvt.

v2 Since γ = (1 − v²/c²)⁻¹/² = 1 + v²/(2c²) + 3v⁴/(8c⁴) + O(c⁻⁶) (4.3.32)

we get a post-Galilean transformation (Chandrasekhar and Contopoulos 1967) of the form t = (1 + v²/(2c²) + 3v⁴/(8c⁴)) t − (1 + v²/(2c²) + O(c⁻⁵)) (v·x)/c² (4.3.33)

x = x − (1 + v²/(2c²)) vt + (v·x)v/(2c²) + O(c⁻⁴). (4.3.34)

4.3.1 Addition of Velocities We again consider two inertial systems, x and x', where we write Xα = (cT, X) instead of x α.

Let v be the constant velocity of the origin of the x'-system with respect to the x-system. We then consider a particle that moves with constant velocity w in the x'-system, i.e., its trajectory reads: X = wT. At first we consider w to be parallel to v and orient the two spatial coordinates such that both velocities point in the x-direction. In the x-system the trajectory of the particle is then given by X = wT and a one-dimensional Lorentz-transformation t = γ(T + vX/c²), x = γ(X + vT) leads to x = γT(w + v) and t = γT(1 + vw/c²), so that for u = x/t we get u = (v + w) / (1 + vw/c²).

So for w being parallel to v we have a rule for the addition of velocities of the form u = (v + w) / (1 + β_v · β_w) (4.3.35)

with β_v ≡ v/c; β_w ≡ w/c.

Next we consider the case that w is orthogonal to v in the sense that formally v·w = 0 and the v·X-terms vanish in the general Lorentz-transformation (4.3.31). Following the same argument but now with x = wT + γvT we get: u = v + (γ − 1) w⊥. (4.3.36)

Combining results (4.3.35) and (4.3.36) we get the general relativistic law for the addition of velocities u = (v + w∥ + (γ − 1) w⊥) / (1 + β_v · β_w). (4.3.37)

Exercise 4.5 Use the relations w = w∥ + w⊥ (4.3.38)

with w∥ = (v·w)v / v²; w⊥ = w − w∥ (4.3.39)

to show that (4.3.37) can be written in the form (γ = (1 − v²/c²)⁻¹/²): u = 1/(1 + β_v · β_w) [ (γ − 1) w + (1 + γ/(1 + γ)) (β_v · β_w) v ]. (4.3.40)

4.3.2 Thomas Precession We now consider three inertial systems: xμ, x'μ and x''μ, where the origin of x' moves with constant velocity v with respect to x and the origin of x'' moves with constant velocity w in x'. From the last section we know that the origin of x'' moves with velocity u (given by (4.3.37)) in x. We now consider the two Lorentz-boosts to go from xμ to x''μ: x''μ = Λμν(w) Λνκ(v) xκ ≡ Tμκ xκ (4.3.41)

with Λ(v) being given by (4.3.28) in the form Λ00 = γ, Λ0i = −γβi, Λi0 = −γβi, Λij = δij + γ/(1 + γ) βiβj.

Λ(w) and Λ(u) are of the same form with γ and β being replaced by γ_w, β_w or γ_u, β_u respectively and ask, if this is in agreement with the single boost Λ(u).

We first consider the simple case that w = v, where β_u ≡ u/c = 2β/(1+β²) with β = v/c, one finds (γ = (1−β²)⁻¹/², Λμν = Λμν(v))

T00 = Λ00 Λ0σ = (1+β²)/(1−β²) = Λ00(u)

T0i = Λ0i Λ0σ = −2γ²β = Λ0i(u)

Ti0 = Λi0 Λ0σ = −2γ²βi = Λi0(u)

Tij = Λiσ Λσj = δij + 2γ²βiβj = Λij(u).

This agreement between Tμν and Λ(u) is true for all w and v which are parallel to each other.

Exercise 4.6 Show that if w and v are parallel to each other, then Tμν = Λμν(u).

Let us now consider the case where v and w are not parallel to each other; for simplicity we take v = (v,0,0) and w = (0,w,0), so that v and w are orthogonal to each other, i.e., v·w = 0. For this special case ui = vδi1 + (γ_v − 1) wδi2 and β_u² ≡ u²/c² = 1 − (γ_v γ_w)⁻². (4.3.43)

From the last equation we see that γ_u = (1 − β_u²)⁻¹/² = γ_v γ_w, (4.3.44)

where γ_v ≡ (1−β_v²)⁻¹/², β_v ≡ v/c and γ_w ≡ (1−β_w²)⁻¹/², β_w ≡ w/c. We get T00 = γ_u T0i = −γ_u γ_v β_v δi1 − γ_u γ_w β_w δi2 Ti0 = −γ_v γ_v β_v δi1 − γ_u γ_w β_w δi2 Tij = δij + γ_u γ_v γ_w β_v β_w δi1 δj2 + (γ_v − 1) δi1 δj1 + (γ_w − 1) δi2 δj2 and Λ00(u) = γ_u Λ0i(u) = −γ_u β_v δi1 − γ_u β_w δi2 Λi0(u) = −γ_u β_v δi1 − γ_u β_w δi2 Λij(u) = δij + ((γ_u−1)/β_u²) β_v² δi1 δj1 + ((γ_u−1)/β_u²) β_w² δi2 δj2 + (γ_u−1) β_v β_w (δi1 δj2 + δi2 δj1).

From this we see that T00 = Λ00(u), but Ti0 ≠ Λi0(u). It turns out that Tiσ = Riσj Λjσ(u) (4.3.47)

where Riσj is a 3×3-rotation matrix. For our example with v = (v,0,0) and w = (0,w,0) it is clear that this matrix describes a rotation about the unchanged z-axis, i.e., Riσj(α) = ( cosα  sinα  0; -sinα  cosα  0; 0  0  1 ).

Let us consider (4.3.47) with σ = 0, leading to the two equations T10 = R1j(α) Λj0(u) = +cosα Λ10(u) + sinα Λ20(u)

T20 = R2j(α) Λj0(u) = −sinα Λ10(u) + cosα Λ20(u)

from which we get cosα = (γ_v γ_u β_v² + γ_w γ_u β_w²) / (γ_u² β_v² + γ_u² β_w²).

Some re-writing yields 1 + cosα = (1 + γ_v + γ_w + γ_u)² / ((1+γ_v)(1+γ_w)(1+γ_u)). (4.3.51)

Exercise 4.7 Assuming v = (v,0,0) and w = (0,w,0) compute sinα and cosα. Then check relation (4.3.47) for σ = j numerically for β_v = 0.777555 and β_w = 0.643354.

Solution One finds that cosα = 0.941260, sinα = −0.337682, so that e.g., for σ = 1: T11 = 1.590293, Λ11 = 1.847779, Λ21 = 0.441087, i.e., T11 = cosα Λ11 + sinα Λ21 up to rounding errors.

For arbitrary velocities v and w one finds: Tiσ = Riαj(u) Λjσ(u); T00 = Λ00(u). (4.3.52)

Here, Riαj is a 3×3-rotation matrix with Riαj Rkαj = δik; it is called the Thomas rotation matrix (Thomas 1926). This important fact is often expressed symbolically by: boost ◦ boost = rotation ◦ boost.

Many authors have derived expressions for the rotation matrix appearing in (4.3.52), e.g., Salingeros (1986) or Sexl and Urbantke (2001). However, the most compact and exact form was given by Klioner (2008): Rij = δij + (viwj/c²) A + (wivj/c²) B + (viwj/c²) C + (wiwj/c²) D with A = (1−γ_w) γ_v² / ((1+γ_v)(1+γ_u))

B = γ_v γ_w (1 + 2 γ_u γ_v γ_w) / (1+γ_u)(1+γ_v)(1+γ_w)

C = −γ_v γ_w / (1+γ_u)

D = γ_w² (1−γ_v) / ((1+γ_w)(1+γ_u)).

Here, γ_w = (1−w²/c²)⁻¹/² etc. If w is parallel to v so that w = av, then Rij = δij + (vi vj/c²) (A + aB + aC + a²D) = δij, since the expression in the bracket vanishes. The angle α of Thomas-rotation can be derived from the trace of Ri using the standard formula 1 + 2 cosα = Riis (4.3.55)

which leads to expression (4.3.51) above. From the above it is clear that if v and w are parallel then α = 0.

From (4.3.53) we can derive many results from the literature. E.g., Rij = δij + 2γ_v/(1+γ_w) β_w [iβv + O(β²). (4.3.56)

Here, A [iB j] ≡ 1/2 (AiBj − AjBi). Defining δβ ≡ β_u − β_v this equation can be re-written as (Klioner 2008)

Rij = δij + (2γ²/(1+γ)) δβ [iβj] + O(|δβ|²), (4.3.57)

where β = β_v and γ = γ_v. This expression that can be found, e.g., in Jackson (1975) and Møller (1972).

Exercise 4.8 Take the general expression (4.3.53) and analyse the situation where v = (v,0,0) and w = (0,w,0). Especially show that R11 = R22, or Aβ_w² = Dβ_w² and R12 = −R21 or B = −C. Derive expression (4.3.51) from R11 = cosα = 1 + Aβ_w².

For accelerated motion the accelerated frame has a local inertial frame at every instant of time with the consequence that Thomas-rotation leads to a precession of some ‘inertial axis’ in space. If we consider an accelerated torque-free gyroscope then it will precess around kinematically non-rotating axes with Thomas-precession frequency: Ω_T = − (1/2c²) (γ²/(γ+1)) v × a, (4.3.58)

with v and a being the velocity and acceleration of the gyro. Thomas precession (Thomas 1926) plays a role in atomic physics because of the electron spin. Here the Thomas precession leads to an interaction energy of E = S·Ω_T that can be rewritten to take a form similar to that of the usual spin-orbit coupling resulting from the magnetic dipole interaction of the electron spin (Jackson 1975; Soffel 1989): E = S·Ω_T = − (1/(2m²c²)) (S·L) (dV/dr), (4.3.59)

where L denotes the electronic angular momentum and V the Coulomb potential of the nucleus. Thomas precession therefore reduces the spin-orbit interaction energy by a factor of two.

4.3.3 General Coordinate Transformations and a Derivation of the Lorentz-Transformation We will now derive the Lorentz-transformation in a constructive manner. Let us consider two coordinate systems xμ = (ct, x^i) and Xα = (cT, X^a) with corresponding metric tensors gμν and Gαβ and gμν = Gαβ = diag(−1, +1, +1, +1). (4.3.60)

Let us write the transformation Xα → xμ in the general form xμ(Xα) = zμ(T) + eμ(T) Xa + ξμ(T, Xa), (4.3.61)

where ξμ is at least quadratic in Xa. Let Aμα = ∂xμ/∂Xα (4.3.62)

be the Jacobi-matrix of this transformation. Because of (4.3.60) the transformation rule for the metric tensor leads to (summation over the index i)

Gαβ = Aαμ Aβν gμν = −Aα0 Aβ0 + Aαi Aβi (4.3.63)

or explicitly −1 = −A00 A00 + A0i A0i 0 = −A00 A0a + A0i Aai δab = −Aa0 Ab0 + Aai Abi.

Generally we have A0μ = ėμ(T) + (1/c) d/dT (eμ(T) Xa + ξμ)

Aaμ = eμ(T) + ∂ξμ/∂Xa, (4.3.65)

where ėμ(T) ≡ dzμ/dT |...

cid:12) (4.3.66)

0 c dT dT Xa=0 1dzi vi ei(T)≡ = e0(T). (4.3.67)

0 c dT c 0 Here, dzi vi ≡ (4.3.68)

dt is the coordinate velocity of the origin of the Xα-system as seen in xμ coordinates.

For the transformation between two inertial systems with (4.3.60) we assume that ξμ(T,Xa)=0, eμ(T)=0 (4.3.69)

dT a and show that the matching conditions (4.3.64) can indeed be satisfied. With these assumptions, that will be discussed later, they read: −1=−e0e0+eiei (4.3.70)

0 0 0 0 0=−e0e0+eiei (4.3.71)

0 a 0 a δ =−e0e0+eiei . (4.3.72)

ab a b a b

Inserting ei =e0vi/c into (4.3.70) we get 0 0 (cid:7) (cid:8)

v2 −1/2 e0 =γ = 1− (4.3.73)

0 c2 and, therefore, ei =γ . (4.3.74)

0 c

From (4.3.71) and (4.3.72) we obtain e0 = ei (4.3.75)

a c a and (cid:9) (cid:10)

γ −1 ei = δij +vivj R j , (4.3.76)

a v2 a where R is a constant rotation matrix with R j R j =δ . (4.3.77)

a b ab

Exercise 4.9 Proof by direct calculation that ei from (4.3.76) solves the matching equation (4.3.72).

Finally, inserting expression (4.3.76) for ei into (4.3.75) one finds e0 =γ Ri . (4.3.78)

a c a A comparison with (4.3.27) shows that for Ri =δ this transformation agrees with the Lorentz-transformation above.

## 4.4 The EM-Field of a Moving Point Charge

Let us consider a point charge q with arbitrary world-line L. For its description it is useful to introduce the Dirac delta function δ(x). In the mathematical language it is a distribution (e.g., Lighthill 1958) with the following properties: δ(x−a)=0 for x (cid:16)=a (4.4.1)

(cid:13)

+∞ f(x)δ(x−a)dx =f(a) (4.4.2)

−∞ (cid:6)

δ(f(x))= (cid:12) (cid:12) (cid:12) (cid:12) δ(x−x i ), (4.4.3)

(cid:12)df(x )(cid:12)

i dx i where f(x) is assumed to have only simple zeros, located at x = x . The 3-dimensional delta function δ3(x) is defined by δ3(x)=δ(x)δ(y)δ(z). (4.4.4)

The current density of our point charge can then be written as jμ =(cρ;j)=quμ(t)δ3(x−z(t)) (4.4.5)

if z(t) parametrizes the world-line of q. We now want to solve the corresponding wave equation (at several places we write x for a 4-dimensional point in space-time with coordinates (t,x))

(cid:2)Aμ(x)=−μ jμ(x).

(cid:7)

Let us define a Green’s function D(x,x ) such that (cid:2)D(x−x (cid:7) )=−δ4(x−x (cid:7) )=−δ(ct −ct (cid:7) )δ3(x−x (cid:7) ). (4.4.6)

One of such Green’s functions, the retarded Green’s function D (x −x (cid:7) ), satisfying (4.4.6), is given by (see e.g., Poisson and Will 2014, Box 6.5)

R D (x−x (cid:7) )= (cid:13)(x0−x (cid:7)0 )δ(x0−x (cid:7)0−|x−x (cid:7)|) (4.4.7)

R 4π|x−x(cid:7)| where (cid:21)

1x0 >0 (cid:13)(x0)= (4.4.8)

0otherwise.

is the Heaviside step-function. Note, that the appearance of (cid:13)(x0 −x (cid:7)0) ensures causality, i.e., a current density at x cannot influence physics in the past of x.

The retarded solution of the wave equation can therefore be written as (cid:13)

A μ (x)=μ d4x (cid:7) D (x−x (cid:7) )jμ(x (cid:7) ) (4.4.9)

## R 0 R

since (cid:13)

(cid:3) (cid:4)

(cid:2)A μ (x)=μ d4x (cid:7) (cid:2)D (x−x (cid:7) ) jμ(x (cid:7) )

## R 0 R

(cid:13) (4.4.10)

=−μ d4x (cid:7) δ4(x−x (cid:7) )jμ(x (cid:7) )=−μ jμ(x).

0 0

For our moving point charge we obtain for x0 >x (cid:7)0 (cid:14) (cid:15)

(cid:13) δ t (cid:7)−t + |x−x(cid:7)| A μ (t,x)= μ 0 q d4x (cid:7) c uμ(t (cid:7) )δ3(x−z(t (cid:7) ))

R 4π c |x−x(cid:7)| (cid:13) (cid:9) (cid:10) (4.4.11)

μ uμ(t (cid:7) ) |x−z(t (cid:7) )| = 0 q dt (cid:7) δ t (cid:7)−t + .

4π |x−z(t(cid:7))| c

Let r(t)≡x−z(t); r(t)≡|r(t)|; n(t)≡r(t)/r(t).

Then, using (cid:13) (cid:9) (cid:10)

g(x)

g(x)δ[f(x)−α]dx = (4.4.12)

df/dx f(x)=α with f(t (cid:7) )≡t (cid:7)+r(t (cid:7) )/c and df ≡κ =1−n(t (cid:7) )·β(t (cid:7) )

dt(cid:7)

we obtain (cid:9) (cid:10)

μ uμ A μ (t,x)= 0 q . (4.4.13)

R 4π κr These are the Liénard-Wiechert potentials for a point-charge q. β(t) is the instantaneous velocity of the point charge divided by c: β =z˙/c. The index ‘R’ refers to an event e on L with proper time τ such that R q R x0 =ct >ct(τ ) (4.4.14)

and x0−z0(τ )=|x−z(τ )|, (4.4.15)

R R i.e., e = e is given by the intersection of L with the backward light-cone through the event (ct,x) (i.e., the space-time point where the potentials and fields are to be evaluated) (Fig. 4.3). Since κr| =[r −r·β] =[(x0−z0)−(x−z)·β] =ρ(t ) (4.4.16)

tR tR tR R with ρ ≡|η (xα −zα)e β| (4.4.17)

αβ 0 and e μ ≡ dzμ/d(ct) = uμ/c, we can write the Liénard-Wiechert potentials in the Lorentz-invariant form (cid:9) (cid:10)

μ uμ Aμ(t,x)= 0 q (4.4.18)

4π ρ or (cid:14) (cid:15)

1 q (cid:19)(t,x)= 4π(cid:9) (cid:14) 0 κ (cid:15) r R (4.4.19)

μ qv A(t,x)= 0 .

4π κr R

Exercise 4.10 Expand the expression (4.4.17) in terms of 1/c and show that up to terms of order 1/c4 (cid:7) (cid:8)

1 1 ρ(t ,x)=r 1+ (β·n)2+ a·r . (4.4.20)

R 2 2c2

From the Liénard-Wiechert potentials, the E- and B-fields can be derived (a derivation can be found e.g., in Jackson 1975): E(t,x)= q (cid:9) (n−β)(1−β2) (cid:10) + q (cid:14) n × ’ (n−β)×β ˙ ((cid:15)

4π(cid:9) 0 κ3r2 R 4π(cid:9) 0 κ3r R (4.4.21)

and B(t,x)= (n×E). (4.4.22)

c2 It is interesting to note, that the Liénard-Wiechert potentials depend only on position and velocity of the charge at retarded time and NOT upon its acceleration. However, since the E- and B-fields are obtained by differentiation of the potentials the acceleration of q enters explicitly. Looking at (4.4.21) we see that the fields are given by two terms: the first term is independent of acceleration and falls off as r−2; this is the static field carried by the charge. The second term depends linearly on the acceleration of the charge. It falls off as 1/r and both, E- and B-field, are transverse to the radius vector r. This is a typical radiation field that is dominant in the far zone from the charge.

Exercise 4.11 Consider two inertial systems, I and I , where the origin z of I (moving system) moves with constant speed in I so that z=vt (Fig. 4.4). Consider some event with coordinates T, X in I and t, x in I . Let T = T −|X|/c be the retarded time in the moving system. By means of Lorentz-transformations show that the corresponding retarded time t can be expressed in the form X x X R v·r 1/2 t =t −γ2 −γ2 r2−(β×r)2 , (4.4.23)

R c2 with r(t)≡x−z(t).

Solution A Lorentz-transformation v(v·r)

X=r+ (γ −1)

c2 leads to X2 =r2+γ2(β·r)2, so that |X|=(r2+γ2(β·r)2)1/2 =γ (r2(1−β2)+(β·r)2)1/2 =γ (r2−(β×r)2)1/2.

Therefore, t =γT =γT −γ2(r2−(β×r)2)1/2.

R R A Lorentz-transformation yields v·x T =γt −γ c2 and we get the result (4.4.23) with x=r(t)+vt.

## 4.5 The Speed of Propagation in Electromagnetism

The form of the Liénard-Wiechert potentials might suggest that the electromagnetic interaction in vacuum ‘propagates with the vacuum speed of light’. This point, however, gave rise to a lot of confusion in the literature and that is the main motivation for this section (another one being the ‘speed of gravity’ problem). One thing, however, should be clear from the beginning: causality is automatically assured by the choice of the retarded Green’s function. So the real question concerning the problem of ‘propagation’ in electromagnetism is: what is possible under the condition that causality is not violated.

4.5.1 The Vacuum Case

4.5.1.1 The Uniformly Moving Point Charge

Let us first consider a point charge q moving with constant velocity in some inertial system I with coordinates (ct,x). According to (4.4.21) the electric field at some field point is given by (cid:9) (cid:10)

q n−β E(t,x)= . (4.5.1)

4π(cid:9) γ2κ3r2 0 R Let r(t) be a vector pointing from the charge at position βct to the field point x: r(t)≡x−βct. Then, r =|r|, n=r/r and κ =(r −r·β)/r so that q r(t )−r(t )β E(t,x)= R R . (4.5.2)

4π(cid:9) γ2(r(t )−r(t )·β)3 0 R R Now, t is determined from the equation |x−βct | t =t − R so that r(t )=c(t −t ). (4.5.3)

R R Thus r(t )−r(t )β =r(t) (4.5.4)

R R and q r(t)

E(t,x)= . (4.5.5)

4π(cid:9) γ2(r(t )−r(t )·β)3 0 R R From (4.5.4) we also infer that r(t )−r(t )·β =r(t)[(1−β2)ρ−βcosφ], (4.5.6)

R R where ρ ≡r(t )/r(t) and r(t)·β =r(t)βcosφ. From (4.5.4) one also finds that (1−β2)ρ−βcosφ =(1−β2sin2φ)1/2 (4.5.7)

so that q r(t)

E(t,x)= ·k (4.5.8)

4π(cid:9) r3(t)

with k = . (4.5.9)

γ2(1−β2sin2φ)3/2 So apart from the factor k that equals one if we neglect β2-terms and results from a Lorentz-transformation from an inertial system I(cid:7), co-moving with the charge to our reference system I, the result is just the static electric field of a point charge at rest. To talk about some ‘speed of propagation’ is obviously meaningless for this situation (Fig. 4.5).

4.5.1.2 The Harmonic Hertzian Dipole

Let us consider two charges of equal magnitude but opposite sign separated by a small distance that oscillate with a period ω such that j(t,x)=j(x)e −iωt, ρ(t,x)=ρ(x)e −iωt. (4.5.10)

Such an equation should be understood that on the right hand side the real part should be taken. Such a Hertzian dipole is depicted in Fig. 4.5 7) x (cid:7) (4.5.18)

是两个电荷的恒定电偶极矩。因此， μ ei(cid:19)

A(t,x)=− 0 iωp (4.5.19)

4π r 这意味着，矢势始终与偶极矩方向平行，并呈现为从原点向外传播的球面波形式。

Taking the orientation of p in z-direction the vector potential in spherical coordinates takes the form A =Acosθ; A =−Asinθ; A =0 (4.5.20)

r θ φ with μ ei(cid:19)

A=− 0 iωp . (4.5.21)

4π r The B-field is obtained from the vector potential A by B=∇×A: (cid:7) (cid:8)

μ ei(cid:19) i B(t,x)= 0 k2c(n×p ) 1+ (4.5.22)

4π r kr or in spherical coordinates (see Fig. 4.6)

(cid:7) (cid:8)

μ ei(cid:19) i B =B =0; B =− 0 k2cp sinθ 1+ . (4.5.23)

r θ φ 0 4π r kr Finally, the E-field is obtained from the Ampère-Maxwell equation c2 E=i ∇×B, (4.5.24)

(cid:9) (cid:7) (cid:8) (cid:10)

1 ei(cid:19) 1 ik E(t,x)= k2(n×p )×n +[3n(n·p )−p ] − ei(cid:19)

4π(cid:9) 0 r 0 0 r3 r2 (4.5.25)

or in spherical coordinates (cid:7) (cid:8)

i i ei(cid:19)

E =− 2kp cosθ 1+ r 4π(cid:9) 0 kr r2 (cid:7) (cid:8)

1 i 1 ei(cid:19) (4.5.26)

E =− k2p sinθ 1+ − θ 4π(cid:9) 0 kr k2r2 r E =0.

In the near zone the dominating fields are 1 e −iωt lim E(t,x)= [3n(n·p )−p ] (4.5.27)

kr→0 4π(cid:9)

0 0 r3 μ e −iωt lim B(t,x)=i 0 kc(n×p ) . (4.5.28)

kr→0 4π 0 r2 The E-field, that dominates over the magnetic field very close to the dipole is just the static electric dipole field, apart from the oscillatory part. In the far zone, lim E(t,x)=cB×n (4.5.29)

kr→∞ μ ei(cid:19)

lim B(t,x)= 0 k2c(n×p ) (4.5.30)

kr→∞ 4π r which is a typical radiation field. The Poynting-vector, describing the electromagnetic energy-flux density S= (E×B) (4.5.31)

takes the form # (cid:26) (cid:27)

c cos2(cid:19) cos(cid:19)sin(cid:19)

S= 16π2(cid:9)0 k4p 2sin2θn r2 kr3 +k2p 2[(3cos2θ−1)n−2cosθpˆ (cid:26) (cid:7) (cid:8)(cid:10))

cos2(cid:19)−sin2(cid:19) k 1 × +cos(cid:19)sin(cid:19) − r4 r3 kr5 (4.5.32)

where pˆ ≡ p /|p |. Note, that this expression is also valid in the near zone. Thus the energy flux shows a very complex behavior especially in the near zone. When, however, we consider a time average over one full period with <cos2(cid:19)>=<sin2(cid:19)>= ; <sin(cid:19)cos(cid:19)>=0 the simpler result reads (cid:26) (cid:27)

1 k4p2sin2θ <S>= 0 nc. (4.5.33)

32π2(cid:9) r2 This expression is not only valid in the far-zone but also in the near-zone. In the far zone <S>= Enc, (4.5.34)

where (cid:9) 1 E = 0 E2+ B2 (4.5.35)

2 2μ is the electromagnetic energy-density.

4.5.2 Propagation in a Uniform Dielectric Medium 4.5.2.1 The Front Velocity A dielectric medium tends to be polarized in the presence of an electric field. If an electromagnetic wave propagates through such a medium electrons will be accelerated and add their contribution to the incident wave. To account for these polarization effects an electric displacement field D is introduced with D=(cid:9) (cid:9)E, (4.5.36)

where (cid:9) is the relative permittivity of the (isotropic) medium. It is related with the susceptibility χ(ω) by (cid:9)(ω)=1+χ(ω). (4.5.37)

Often the permittivity is derived from a Lorentz-model where electrons with charge e and mass m are harmonically coupled to protons with characteristic oscillation frequency ω so that ω2 (cid:9)(ω)=1+ p , (4.5.38)

ω2−ω2−igωω 0 0 where g a dimensionless damping constant and (cid:24)

N e2 ω = e (4.5.39)

(cid:9) m 0 e is the plasma frequency with N being the electron number density.

The wave equations in such a medium take the form (cid:7) (cid:8)

(cid:9) ∂2 − +(cid:16) E=0 c2∂t2 (4.5.40)

∂B ∇×E=− .

∂t Plane wave solutions of (4.5.40) can be written as E=E ei(k·x−ωt), B=B ei(k·x−ωt) (4.5.41)

0 0 with B =(k×E )/ω (4.5.42)

0 0 and ω c v = = , (4.5.43)

k n where n= (cid:9) (4.5.44)

is the medium’s index of refraction. v is the phase velocity, i.e., the velocity for (cid:19) ≡ k·x−ωt = const. For the Lorentz-model (4.5.38) the index of refraction is a function of ω: the medium is dispersive. Figure 4.7 shows the real part of (cid:9) and the phase velocity with n = (cid:21)( (cid:9)) for the Lorentz-model (4.5.38) (ω = 1, ω = 0.1, g = 0.1). One sees that in the vicinity of the resonance at ω = ω the phase velocity becomes larger than the vacuum speed of light.

We now consider a one-dimensional problem (Fitzpatrick 2015): a dispersive uniform medium extends from x = 0 to x = +∞. An incident wave of frequency ω∗ coming from negative x-values is supposed to have an amplitude (cid:21)

0 fort <0 f(t)= (4.5.45)

sin(ω∗t)fort ≥0 at x = 0 and we ask how the wave propagates to a point x > 0 in the medium. As shown e.g., in Fitzpatrick (2015) the amplitude for x ≥ 0 can be written as (cid:13)

1 dω f(t,x)= (cid:21) ei(kx−ωt) (4.5.46)

2π C ω−ω∗ where the integration contour in the complex ω-plane C + ={ω|ω I ≡(cid:20)(ω)=z∈R + } (4.5.47)

extends from ω ≡(cid:21)(ω)=+∞ to −∞. For t < 0 we can choose z→+∞ so that the integrand has a term exp(ω t) that vanishes exponentially so that f(t,x)=0 as it has to be.

Exercise 4.12 Show that for x ≥ 0 the wave amplitude obeying (4.5.45) is given by expression (4.5.46). The proof is given in Fitzpatrick (2015).

Let s ≡ t−x/c. For s < 0 (or v > c) we can again choose z→∞ so that in the Lorentz-model * + ω ω ω2 1/2 k = n= 1+ p −→ for |ω|→∞. (4.5.48)

c c ω2−ω2−igωω c 0 0 In that case i(kx−ωt)=−iω(t −x/c)=−iωs has a large negative real part so that f(t,x) = 0. Thus the wave-front cannot propagate through the dispersive medium with velocity greater than c.

We now consider s > 0 (v < c) but very small. Starting from (cid:13)

f(t,x)= ω∗ ei([k−ω/c]x−ωs)

dω (4.5.49)

2π C ω2−ω∗ 2 that is equivalent to (4.5.46) for s being sufficiently small we can deform C + into a large semi-circle of radius R in the upper ω-plane plus two segments of the real axis as shown in Fig. 4.8.

Because of the denominator ω2−ω∗ 2 the integrand tends to zero as 1/ω2 for large |ω| on the real ω-axis. Adding the integration along the dotted curve in Fig. 4.8 along which the integrand vanishes exponentially for s > 0 and large values of R we get (cid:16)

f(t,x)= ω∗ ei([k−ω/c]x−ωs)

dω . (4.5.50)

2π ω2−ω∗ 2 For |ω|→∞ one has ⎛(cid:24) ⎞ k− ω → ω ⎝ 1− ω p 2 −1 ⎠(cid:9)− ω p 2 c c ω2 2cω so that (cid:16)

f(t,x)= ω∗ e [i(ξ/ω−ωs)]

dω (4.5.51)

2π ω2 with ω2 ξ ≡ p x. (4.5.52)

2c We now parametrize the integration circle by writing (cid:25)

ω= eiu, (4.5.53)

(0≤u≤2π) so that (cid:25)

dω s =i e −iudu ω2 ξ and (cid:25) (cid:13)

f(t,x)=i ω∗ s 2π e −2i ξscosue −iudu 2π ξ (cid:25) (cid:13) (4.5.54)

=i ω∗ s 2π e −2i ξscosucosudu.

2π ξ The last line follows from (cid:13)

2π cosn(u)sin(u)du=0 which results from cos(π ±x) = −cos(x) and sin(π ±x) = ∓sin(x). Now, the Bessel function of first order (Fig. 4.9) is given by (cid:13)

i 2π J (z)=− eizcosθcosθdθ (4.5.55)

2π so that (cid:25)

(cid:2)

f(t,x)=ω∗ J (2 ξs) (4.5.56)

since J (−z) = −J (z). Equation (4.5.56) describes the behavior of the Sommerfeld-precursor. Its amplitude is extremely small compared to that of the incident wave since |f | ∼ ω∗ s/ξ = ω∗/ω (cid:14) 1. Since ξ is proportional to x the amplitude of the Sommerfeld-precursor decreases like 1/x with increasing value of x. The initial period of oscillation is determined by the first maximum of J where s ∼1/ξ, hence its oscillation frequency is extremely high and independent of ω∗.

4.5.2.2 The Group-Velocity We now consider a one-dimensional wave-packet with amplitude (cid:13)

+∞ f(t,x)= dkF(k)ei(kx−ωt) (4.5.57)

−∞ and first assume the wave packet to be almost monochromatic with dominant wave vector k . To perform the integral ω has to be considered implicitly a function of k. Substituting a linear relation of the form ω(k)(cid:9)ω +(k−k )v (4.5.58)

0 0 gr with (cid:7) (cid:8)

dω v ≡ (4.5.59)

gr dk leads to (cid:13)

+∞ f(t,x)=ei(k0x−ω0t) dkF(k)ei(k−k0)(x−vgrt).

(4.5.60)

−∞ The first factor describes a perfect monochromatic wave with wave-vector k with peaks and troughs moving with phase velocity v = ω /k under the envelope of the wave-packet. The second term implies that the envelope propagates with the group-velocity v . For a general wave-packet with large bandwidth partial waves with different frequencies will propagate with different velocities; nevertheless the group-velocity (4.5.59) indicates the propagation velocity of the peak of a wave-packet. Since ph 0 0 gr k(ω)= n(ω) (4.5.61)

for a complex index of refraction the group-velocity can be written in the form (cid:7) (cid:8)

1 d((cid:21)(k)) 1 d((cid:21)(n))

= = (cid:21)(n)+ω . (4.5.62)

v dω c dω gr Under certain conditions the group-velocity can exceed the vacuum speed of light. E.g., Chiao (1993) considers a gas of inverted two-level atoms where the relative permittivity can be modeled with ω2 (cid:9)(ω)=n2(ω)=1− p (4.5.63)

ω2−ω2−igωω 0 0 differing from the Lorentz-model of (4.5.38) by the sign of the second term, thus converting damping into amplification. In the limit of small frequencies, ω (cid:14) ω a wave group propagates with superluminal velocity since (cid:24)

1 n 1 ω2 1 (cid:9) (cid:9) 1− p < . (4.5.64)

v gr c c ω 0 2 c This result for small frequencies does not depend on the specific model (4.5.63); from the Kramers-Kronig relations (e.g., Landau and Lifshitz 1960) between Real and Imaginary part of the susceptibility χ one finds that (cid:9)(0)<1 and hence n(0)<1 if (cid:20)χ(ω) < 0 (e.g., Chiao 1993) implying that both, phase- and group-velocity, exceed the vacuum speed of light without violating causality.

Sommerfeld and Brillouin (Brilluoin 1960) have discussed other propagation velocities besides the phase-, front- and group-velocity: an ‘energy-velocity’ at which energy is transported by the wave and a ‘signal-velocity’ at which the half-maximum amplitude travels. One finds that also these velocities can exceed the vacuum speed of light. It is only the front-velocity of the Sommerfeld precursor that is never larger than c.

In recent decades such superluminal wave propagations have been detected in many experiments using single photons (Steinberg and Chiao 1995), at optical frequencies (Spielmann et al. 1994) a inducing microwaves (Mojahedi et al. 2000a, b; Ranfagni et al. 1991, 1993; Mugnai et al. 1998; Enders and Nimtz 1992, 1993).

## 4.6 Energy and Momentum

We first note that the 4-velocity of some small body has an absolute value that does not change with time. Using metric property 2 (Eq. (4.3.10)) we find gμν uμ uν = gμν (dxμ/dτ)(dxν/dτ) = (ds/dτ)² = -c². (4.6.1)

From this we immediately infer the absolute value of the 4-momentum gμν pμ pν = -p⁰p⁰ + p² = -m²c². (4.6.2)

The time component of pμ is related with the body’s energy E by p⁰ = iE/c, (4.6.3)

i.e., E² = (mc²)² + p²c². (4.6.4)

For a small momentum |p| << mc we have E = √(m²c⁴ + p²c²) = mc² + p²/(2m) + ... , (4.6.5)

where p²/(2m) is the usual kinetic energy of the body and mc² is its rest-energy. In words: even for zero momentum a body of mass m possesses an energy of E = mc². (4.6.6)

This relation between mass and energy is of special importance for our theory of gravity since mass-density acts as source of the gravitational field in Newton’s theory. Therefore in any relativistic theory of gravity it must be energy and momentum that produce gravity. If one considers a continuous distribution of non-interacting particles (dust) with 4-velocities uμ one defines an energy-momentum tensor Tμν by Tμν = ρ uμ uν. (4.6.7)

Here ρ is the rest-mass (energy) density that is measured if one moves together with the ensemble of particles. For an ideal fluid (no shear stresses, anisotropic pressure, viscosity etc.) the energy-momentum tensor reads Tμν = (ρ + p/c²) uμ uν + p gμν, (4.6.8)

where p is the pressure. Generally every continuous distribution of matter or field can be associated with a corresponding symmetric energy-momentum tensor. As further example the energy-momentum tensor of the electromagnetic field takes the form Tμν = (1/(4π)) [ Fμα Fνα - (1/4) gμν Fαβ Fαβ ]. (4.6.9)

Evaluating this expression in Minkowskian coordinates we find Fαβ Fαβ = 2 F₀i F₀i + Fij Fij = -2E² + 2B² F₀α F₀α = F₀i F₀i = E² F₀α Fiα = F₀j Fij = (E × B)i Fiα Fjα = Fi0 Fj0 + Fik Fjk = -Ei Ej + (Eijk Bk) (Ejlm Blm)

= -Ei Ej + (δil δjm - δim δjl) Bk Bl = - (Ei Ej + Bi Bj) + B² δij.

Therefore, T₀₀ = (1/(4π)) F₀α F₀α - (1/(4π))(1/4) Fαβ Fαβ = (1/(4π)) E² - (1/(4π))(1/2)(-2E² + 2B²), i.e., the energy-density of the electromagnetic field T₀₀ is given by T₀₀ = (E² + B²)/(8π). (4.6.10)

For the energy-momentum current one finds T₀i = (1/(4π)) (F₀α Fiα) = (E × B)i / (4π), (4.6.11)

known as the Poynting vector of the field. Finally for the Maxwell stress tensor Tij we get Tij = (1/(4π)) [ Fiα Fjα - (1/4) δij Fαβ Fαβ ]

= (1/(4π)) [ - (Ei Ej + Bi Bj) + (1/2) (E² + B²) δij ]. (4.6.12)

Just as the continuity equation (4.2.3) indicates the conservation of electric charge the equation ∂ν Tμν = 0 (4.6.13)

indicates the conservation of energy and momentum of some continuous matter or field distribution in some Minkowskian coordinate system. Clearly in an arbitrary coordinate system this relation reads Tμν ;ν = 0 (4.6.14)

where we have replaced the partial derivatives by the covariant ones. As an example we consider this law for an ideal fluid with local density ρ, pressure p and temperature T. In Minkowskian coordinates it reads 0 = ∂ν Tμν = ∂ν [ p ημν + (ρ + p/c²) uμ uν ]. (4.6.15)

Since ηαβ uα uβ = -c² (relation (4.3.14))

∂γ (ηαβ uα uβ) = 2 ηαβ uβ ∂γ uα and we obtain 0 = ηαβ uβ ∂γ Tαγ = uβ [ ∂β p - ∂γ ((ρ c² + p) uγ) ]. (4.6.16)

This result can be written in a very elegant manner (Weinberg 1972). Let us think of the fluid to be composed of infinitely many infinitesimally small particles. As far as mass and energy are concerned these particles will be the baryons of ordinary matter. Let n be the baryon number density that can be measured if one moves with the matter. The law of baryon number conservation can then be formulated with a baryon current 4-vector Nμ = n uμ (4.6.17)

in the form ∂μ Nμ = ∂μ (n uμ) = 0. (4.6.18)

Using this law we can rewrite (4.6.16) as 0 = uβ [ ∂β p - ∂β ((ρ c² + p)/n) n - ((ρ c² + p)/n) ∂β n ]

= - n uβ [ ∂β (p/n) + ∂β (ρ c²/n) ]. (4.6.19)

We can now employ the first law of thermodynamics in the form T ds = p d(1/n) + d(ρ c²/n) (4.6.20)

or T ∂β s = ∂β (p/n) + ∂β (ρ c²/n)

where the quantity s is the entropy per baryon. With this the conservation equation (4.6.19) simply reads 0 = uβ ∂β s = ∂s/∂τ. (4.6.21)

In other words: entropy per baryon is conserved if one moves together with the fluid.

Putting μ = i in (4.6.13) one finds the relativistic Euler equation of hydrodynamics in the form: ∂v/∂t + (v·∇)v = -∇p/(ρ + p/c²) - (1/c²) [(1 - v²/c²) / (ρ + p/c²)] v (∂p/∂t). (4.6.22)

Exercise 4.13 Derive the Euler equation (4.6.22) from (4.6.13) by putting μ = i by using the law of entropy conservation.

## Chapter

Einstein’s Theory of Gravity

## 5.1 General Relativity

Special Relativity can be described as physics in a 4-dimensional space-time manifold M with metric tensor gμν that reduces to ημν = diag(-1, +1, +1, +1) in any global inertial coordinate system. Such selected global coordinates exist because the geometry of Minkowskian space-time is flat, i.e., the curvature and Ricci tensor vanish. Einstein’s theory of gravity is also a structure (M, g), but space-time geometry in the presence of gravitational fields is not longer flat, the curvature tensor describing the tidal actions. For vanishing gravitational fields the structure (M, g) reduces to the Minkowskian space-time; it is fully in accordance with all experiments from Special Relativity.

In General Relativity (GR) all aspects of gravitational fields are contained in the space-time metric tensor. A necessary prerequisite this is the Equivalence principle, that also shows the role of Special Relativity in Einstein’s GT. The weak form of the equivalence principle (the universality of free-fall) has already been discussed. The Einstein equivalence principle (EEP) generalizes this to all non-gravitational laws of physics: in any freely falling system all non-gravitational laws of physics take their form from Special Relativity. In some sense certain aspects of gravity disappear in a freely falling reference frame. Such aspects are related with the affine connections of space-time geometry that are not tensors and can be transformed to zero at any point p ∈ M by a suitable coordinate transformation. This, however, by no means implies that some existing gravitational field inside such a freely-falling system is zero; if the curvature tensor has non-vanishing components in one coordinate system then there is no coordinate system where it completely vanishes at any point p ∈ M. This means that the EEP simply says that at each point p of the space-time manifold there are local coordinates such that the metric tensor reduces to the Minkowskian tensor where effects from gravity do not appear.

Einstein’s equivalence principle implies that a reasonable theory of gravity should be a metric theory with (M, g) as basic structure and possible additional fields ψ, taking part in the gravitational interaction. General Relativity is the simplest of all such metric theories, where all additional fields ψ = 0. Sources of the gravitational field, i.e., all forms of energy and momentum as well as gravity fields itself, produce curvature of space-time which again determines the dynamical behavior of the sources.

## 5.2 Einstein’s Equivalence Principle

Einstein’s theory of gravity generalizes the results from Minkowski space-time theory by considering also gravitational fields. A hint of how to incorporate gravity into the space-time structure comes from the phenomenon of gravitational redshift.

Let us consider two identical clocks at rest in some gravitational potential U(x). Clock 1 is assumed to be located a distance H above clock 2. Then, because of the gravitational redshift the natural frequencies of the two clocks, f₁ and f₂, are related by f₂/f₁ = 1 + [U(x₂) - U(x₁)]/c². (5.2.1)

It is not difficult to see that the gravitational redshift of electromagnetic waves is a consequence of a certain form of the equivalence principle. This will also make it clear why clocks in a gravitational field are running slower (Fig. 5.1).

Fig. 5.1 Three static clocks in some gravitational field. The larger the gravitational potential the slower the clock runs Einstein’s Equivalence Principle Everywhere in the universe and for all times in sufficiently small freely falling laboratories all non-gravitational laws of physics take their form from Special Relativity.

In other words: such freely falling systems are locally inertial. Let us now consider two clocks at rest in some external gravitational field (Fig. 5.2). Obviously the two clocks are not freely falling; instead they are at rest in some system that is accelerated upwards, i.e., away from the center of gravitational attraction. With respect to some freely falling local inertial coordinate system xμ = (ct, xi) the world-lines of the two clocks are depicted in Fig. 5.2. We now consider a light-pulse being emitted from clock 1 in the direction of clock 2. In a first approximation z₁ = gt²/2 + H and z₂ = gt²/2 and the velocities are given by v = gt. Since in the accelerated system where the two clocks are at rest the situation is stationary and we might choose for simplicity t = 0 for the emission event. Neglecting (v/c)² terms t will agree with the proper times indicated by the two clocks. Then for gH/c² << 1 the signal will arrive at clock 2 at t- ≈ H/c. The crucial point is that at the point of reception the second clock has a finite velocity v = gt = gH/c in the direction of the first clock. Let the first clock emit a second pulse at t = δt₁ immediately after the first one. The arrival time at clock 2 then is t+ = H/c + δt₁ - (v/c) δt₁ since during the interval δt₁ it has moved a distance v δt₁ in the direction of clock 1, i.e., the effective distance is only H - v δt₁ instead of H. Hence the time that has elapsed during the reception...

of the two pulses at clock 2 is

$$\delta t = t^+ - t^- = \delta t \left( 1 - \frac{g_{00}U(x_2) - U(x_1)}{c^2} \right) \approx \delta t \left( 1 - \frac{2}{c^2} \right)$$

in accordance with the gravitational redshift formula (5.2.1). Thus from the standpoint of Einstein’s Equivalence Principle the gravitational redshift results from the first-order Doppler shift of frequencies. Einstein’s form of the equivalence principle has the consequence that gravity can be described by a metric theory, i.e., (see e.g., Will 1993 for more details)

- by at least a $g_{\mu\nu}$-field and possibly by “other g-fields”; - these “other g-fields” only couple to the $g_{\mu\nu}$-field but not to matter-fields directly; - at each point in space-time there is a local freely falling system (Einstein’s elevator) where the space-time metric $g_{\mu\nu}$ reduces to the flat space-time metric $\eta_{\mu\nu}$; - the world-lines of uncharged test particles are geodesics of $g_{\mu\nu}$.

The last point follows from the fact that these world-lines are straight lines in a freely falling system, i.e., geodesics with respect to the flat space-time metric. Hence, they must be geodesics with respect to the space-time metric $g_{\mu\nu}$.

Metric Property 3: Sufficiently small (uncharged) test bodies move along geodesics of the metric tensor.

The gravitational redshift can then be described in a very elegant manner: we incorporate the gravitational potential $U$ into the metric and write in suitable coordinates

$$ds^2 = -\left(1 - \frac{2U}{c^2}\right) c^2 dt^2 + (dx)^2 \quad (5.2.2)$$

or

$$g_{00} = -1 + \frac{2U}{c^2}; \quad g_{0i} = 0; \quad g_{ij} = \delta_{ij}. \quad (5.2.3)$$

Assuming again metric property 2 (Eq. (4.3.10)) for two clocks at rest ($dx=0$) we get for each of the two clocks $i$:

$$d\tau_i^2 = -\frac{1}{c^2} ds^2 = \left(1 - \frac{2U(x_i)}{c^2}\right) dt^2$$

or

$$d\tau_i \approx \left(1 - \frac{U(x_i)}{c^2}\right) dt. \quad (5.2.4)$$

From this we derive

$$\frac{f_2}{f_1} = \frac{d\tau_1}{d\tau_2} \approx \frac{1 - U(x_1)/c^2}{1 - U(x_2)/c^2} \approx 1 + \frac{1}{c^2} [U(x_2) - U(x_1)]$$

in accordance with (5.2.1).

## 5.3 The Motion of Test Bodies

Let us consider the geometry that is determined by the metric (5.2.3) in more detail where we restrict our discussion to terms of order $c^{-2}$. The inverse metric tensor in this approximation is given by

$$g^{00} = -1 - \frac{2U}{c^2}; \quad g^{0i} = 0; \quad g^{ij} = \delta_{ij}. \quad (5.3.1)$$

From this we derive the non-vanishing Christoffel-symbols:

$$\Gamma^0_{0i} = \Gamma^0_{i0} = \Gamma^i_{00} = -\frac{1}{c^2} U_{,i}. \quad (5.3.2)$$

We now come to the geodesic equation

$$\frac{d^2 x^\mu}{d\lambda^2} + \Gamma^\mu_{\nu\sigma} \frac{dx^\nu}{d\lambda} \frac{dx^\sigma}{d\lambda} = 0.$$

Here $\lambda$ is an affine parameter that might be replaced by the time coordinate $t$ (which is not an affine parameter) in the $\mu=i$ equation:

$$\frac{d^2 x_i}{dt^2} = \frac{d}{d\lambda} \left( \frac{dt}{d\lambda} \right) \left[ \frac{d}{d\lambda} \left( \frac{dt}{d\lambda} \right) \frac{dx_i}{d\lambda} \right] - \left( \frac{dt}{d\lambda} \right)^{-2} \frac{d^2 x_i}{d\lambda^2} - \left( \frac{dt}{d\lambda} \right)^{-3} \frac{d^2 t}{d\lambda^2} \frac{dx_i}{d\lambda} \quad (5.3.3)$$

$$= - \left( \frac{dt}{d\lambda} \right)^{-2} \left( \Gamma^i_{\nu\sigma} \frac{dx^\nu}{d\lambda} \frac{dx^\sigma}{d\lambda} + \Gamma^0_{\nu\sigma} \frac{dx^\nu}{d\lambda} \frac{dx^\sigma}{d\lambda} \frac{dx_i}{dt} \right). \quad (5.3.4)$$

In more detail this reads ($v_i \equiv dx_i/dt$)

$$\frac{d^2 x_i}{dt^2} = -c^2 \left( \Gamma^i_{00} + 2\Gamma^i_{0j} \frac{v_j}{c} + \Gamma^i_{jk} \frac{v_j v_k}{c^2} \right) - \left( \Gamma^0_{00} + 2\Gamma^0_{0j} \frac{v_j}{c} + \Gamma^0_{jk} \frac{v_j v_k}{c^2} \right) \frac{v_i}{c}. \quad (5.3.5)$$

Considering the Christoffel-symbols from (5.3.2) we see that the right hand side of this equation has a term of order $c^0$ resulting from $\Gamma^i_{00}$. Keeping only this $c$-independent term the geodesic equation reads

$$\frac{d^2 x_i}{dt^2} = -c^2 \Gamma^i_{00} = U_{,i}. \quad (5.3.6)$$

This, however, is precisely the equation of free-fall of a sufficiently small test body in Newton’s theory of gravity in Galilean coordinates (Cartesian and inertial).

## 5.4 Einstein’s Theory of Gravity

Einstein’s theory of gravity is the ‘simplest’ of all reasonable metric theories of gravity. In Einstein’s theory there are no other g-fields but only one space-time metric that also describes gravity.

Metric property 3 indicates an intimate relation between Newton’s theory of gravity and a relativistic one. In both theories test particles move along geodesics of the space-time geometry. As we have seen the Newtonian field equation for the potential $U$ relates the Ricci-tensor of space-time with the field generating source. Now in relativity the source of the gravitational field obviously must be the energy-momentum tensor $T_{\mu\nu}$ and Einstein’s field equations for the metric tensor take the form

$$F_{\mu\nu}(g, \partial g, \partial^2 g) = \kappa T_{\mu\nu}$$

where $F_{\mu\nu}$ is a function of $g_{\mu\nu}$ and its first and second partial derivatives with respect to the coordinates $x^\mu$. Because of the conservation laws for energy and momentum, Eq. (4.6.14) we have to require

$$F_{\mu\nu}^{\phantom{\mu\nu};\nu} = 0. \quad (5.4.1)$$

Theorem 5.1 (Lovelock 1972) The most general tensor $F_{\mu\nu}(g, \partial g, \partial^2 g)$ that is divergenceless, i.e., obeys Eq. (5.4.1) is of the form

$$F_{\mu\nu} = a G_{\mu\nu} + b g_{\mu\nu} \quad (5.4.2)$$

where $G_{\mu\nu}$ are the components of the Einstein-tensor.

The usual Einstein’s field equations are obtained with $a = 1$ and $b = 0$:

$$G_{\mu\nu} = \kappa T_{\mu\nu} \quad (5.4.3)$$

or

$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \kappa T_{\mu\nu}. \quad (5.4.4)$$

Another important form of the field equations is obtained by contracting equation (5.4.4) with $g^{\mu\nu}$ (i.e., by taking its trace):

$$R - \frac{1}{2} R = -\frac{1}{2} R = \kappa T,$$

where

$$T \equiv g^{\mu\nu} T_{\mu\nu} \quad (5.4.5)$$

is the trace of the energy-momentum tensor. Inserting this result for the curvature scalar $R$ into Einstein’s field equations leads to the alternative form

$$R_{\mu\nu} = \kappa \left( T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T \right) \equiv \kappa \hat{T}_{\mu\nu}. \quad (5.4.6)$$

Finally we have to determine the coupling constant $\kappa$. To this end we consider the ‘Newtonian limit’ of these field equations. In Newton’s theory only the matter density $\rho$ acts as source of the gravitational field. This density to lowest order is contained in the time-time component of the energy-momentum tensor, considering a continuous distribution of energy and momentum. From (4.6.7) we see that

$$T_{00} = -T = \rho c^2 + \dots \quad (5.4.7)$$

and for that reason the Newtonian field equation must be contained in the time-time component of (5.4.6):

$$R_{00} = \kappa \left( T_{00} - \frac{1}{2} g_{00} T \right) \approx \frac{1}{2} \kappa \rho c^2.$$

The left hand side to order $c^{-2}$ can be taken from Eq. (3.2.21) keeping in mind that now $x^0 = ct$ and the dimension of the Einstein tensor is (length)$^{-2}$:

$$R = R_{00} = -\frac{\nabla U}{c^2} + \dots.$$

Hence to lowest order the Einstein field equations lead to

$$-\nabla U = -\frac{\kappa}{2} \rho c^4$$

and a comparison with the Poisson equation (3.2.19) shows that

$$\kappa = \frac{8\pi G}{c^4}.$$

Einstein’s field equations form a complicated set of ten partial differential equations of second order. Because of the Bianchi identities these ten equations are not independent from each other but only six of them. Hence, the equations determine six out of ten degrees of freedom of the metric tensor $g_{\mu\nu}$. Four degrees of freedom for the metric tensor remain, expressing the freedom in the choice of the four space-time coordinates. Of course the field equations cannot tell what coordinates should be used; instead the coordinates can be fixed by four (more or less) arbitrary conditions for the metric tensor. This is the coordinate or “gauge” freedom of the theory. This gauge freedom is one of the most important differences to the classical Newtonian case. In Newton’s theory time is absolute, so there is a preferred time coordinate which is fixed uniquely up to origin and unit. Out of the many possible spatial coordinates the inertial (Cartesian) ones which in Newton’s theory exist globally are preferred. They are determined uniquely up to origin, unit and orientation in space (determined e.g., by three Euler angles). All these preferred coordinates, however, do not exist in Einstein’s theory of gravity. However, the situation is not too bad for isolated systems with an asymptotically flat space-time. E.g., the solar system might be idealized in this manner: we forget about distant masses and think of the solar system as being isolated. Then far from the solar system the gravitational field will become very small and space-time will approach flat space-time from Special Relativity Theory in this idealized picture. Then in the asymptotic region preferred (inertial and Cartesian) coordinates exist such that there

$$g_{\mu\nu} \rightarrow \eta_{\mu\nu}. \quad (5.4.8)$$

If, however, we get closer to the gravitating masses preferred coordinates cease to exist; i.e., many different coordinates have equal rights.

If we choose $a = 1$ and $b = \Lambda$ in Lovelock’s Theorem then we end up with field equations of the form with a $\Lambda$ term

$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}. \quad (5.4.9)$$

In this case the constant $\Lambda$ is called the cosmological constant. It is obvious that the $\Lambda$-term can be absorbed in the energy-momentum tensor by replacing $T_{\mu\nu}$ by

$$\tilde{T}_{\mu\nu} \equiv T_{\mu\nu} - \kappa^{-1} \Lambda g_{\mu\nu}. \quad (5.4.10)$$

Usually it is assumed that $\Lambda$ is related with the energy density of the quantum vacuum pervading the whole universe and might have a value of about $10^{-52} \mathrm{m}^{-2}$ (Peebles and Ratra 2003). Metric (5.4.9) plays an important role in modern cosmology.

## 5.5 The Problem of Observables

Since in Einstein’s theory of gravity the coordinates usually have no direct physical meaning the problem of observables is a serious one. It should be clear that observables are independent of any set of coordinates used by some theorist to describe the system of interest. In other words: observables have to be described by scalars, coordinate independent quantities. First one chooses some appropriate coordinate system and draws a coordinate picture of the system of interest. Then one constructs the observables as scalars from such a coordinate picture.

5.5.1 The Ranging Observable

Let us consider a typical astronomical measurement in the solar system: lunar laser ranging (LLR). Here laser pulses are emitted from LLR-stations on the Earth to retroreflectors on the lunar surface. A few photons per pulse find their way back into the receiving telescope of the station and one measures the total travel time of a pulse from the station to the Moon and back. This situation is depicted in Fig. 5.3. In the right part of the figure we see the world-line of the clock with the two events E: emission of the pulse and R: reception of the pulse. The observed time interval between E and R is then given by

$$\Delta \tau = \int d\tau \quad (5.5.1)$$

with

$$d\tau^2 = -\frac{ds^2}{c^2}.$$

In practise this indicated time interval $\Delta \tau$ can then be related with a corresponding interval of some other timescale.

5.5.2 The Spectroscopic Observable

We now consider the following problem: one observer emits some monochromatic electromagnetic wave of frequency $f_E$. Another observer receives this signal and measures the frequency $f_R$ and we ask about the relation between the two.

(Figure caption: Fig. 5.3 Left: A central observable for celestial mechanics, the ranging observable, is a propagation time interval between emission and reception of some electromagnetic pulse. In Lunar Laser Ranging it is a laser pulse that travels from some LLR-station on the Earth to some retro-reflector on the lunar surface and back to the ground station.)

Right: the observable is the proper time interval that has elapsed between the instant of emission and the instant of reception of an electromagnetic pulse.

The spectroscopic observable is the frequency ratio fR/fE. Some observer (emitter) emits some electromagnetic signal of frequency fE. This signal is observed by another observer (receiver) who measures the frequency fR.

Frequencies. If we concentrate upon one single light-ray propagating from the emitter to the receiver the situation is shown in Fig. 5.4. Here γ* is the world-line of the emitter, γ that of the receiver, γ* that of the light ray. Let uμ be the 4-velocity of the emitter at the point of emission, uμ that of the receiver at the point of reception. Let kμ be the tangent vector onto γ* then according to (4.3.7) the frequency ratio is given by fR / fE = (g μν kμ uν)R / (g μν kμ uν)E . (5.5.2)

Let us analyze this situation in Minkowski space in the absence of gravitational fields. Let us choose a Minkowskian coordinate system such that the receiver is at rest in the event of reception, i.e., uμ = (c, 0).

If the emitter has coordinate velocity v at the point of emission then uμ = γ(c, v).

Since kμ is a null-vector we can write in Minkowskian coordinates kμ = const. × (1, n) (5.5.3)

with δij ni nj = 1.

The normalization constant in kμ will not play a role if only frequency ratios are considered. With β ≡ v/c (5.5.4)

we then get fR / fE = [γ(1 - β·n)]^{-1} or fR = fE (1 - β²)^{1/2} / (1 - β·n). (5.5.5)

This is the well-known formula for the Doppler-effect in electromagnetism.

5.5.3 The Astrometric Observable In astrometry the principle observable is the observed angle between two incident light-rays. This situation is depicted in Fig. 5.5. Here γ(λ) is the worldline of the observer, γ*1 and γ*2 are two light-rays from two different astronomical sources that are simultaneously observed by the observer in some event O. Let uμ be the 4-velocity of the observer in O, k1μ and k2μ be the wave vectors of the two incident light-rays. Then Pμν ≡ δμν + (1/c²) uμ uν (5.5.6)

is a projection tensor that projects vectors into their components perpendicular to uμ, i.e., Pμν uν = uμ + (1/c²) uμ uν uν = 0 (5.5.7)

The astrometric observable: the observed angle θ between two incident light-rays γ*1 and γ*2. The observer’s worldline is γ(λ) and kμ are tangent vectors to the light-rays.

since uν uν = -c². In some sense uμ points into the time-direction of the observer and the projection operator points into the space ‘experienced’ by the observer. Now kμ are null-vectors but k̄μ ≡ Pμν kν (5.5.8)

is a spacelike vector of non-vanishing length. For uμ = γc(1, β) kμ = (1, n)

we find uμ kν = -γc(1 - β·n) (5.5.9)

and therefore k̄μ = kμ - γ(1 - β·n) uμ. (5.5.10)

From this it is not difficult to see that |k̄μ| ≡ (g μν k̄μ k̄ν)^{1/2} = γ(1 - β·n). (5.5.11)

The observed angle θ between two incident light-rays γ*1 and γ*2 is generally given by cosθ = (g μν k1μ k2ν) / (|k̄1μ| |k̄2μ|). (5.5.12)

In the absence of gravity fields from (5.5.12) we get cosθ = (n1·n2 - 1 + γ²(1 - β·n1)(1 - β·n2)) / (γ²(1 - β·n1)(1 - β·n2)). (5.5.13)

This is the aberration formula if gravity fields play no role. A Taylor expansion in terms of c^{-1} yields cosθ = n1·n2 + (n1·n2 - 1)((n1 + n2)·β + (n1·β)² + (n2·β)² + (n1·β)(n2·β) - β²) + O(c^{-3}). (5.5.14)

## 5.6 Tetrads and Tetrad Induced Coordinates

Consider some massless observer E that moves through empty space with a space capsule and wants to perform some local experiment inside of his spacecraft. Let us describe the motion of E in some coordinate system xμ by some timelike worldline LE, given by zEμ(λ), where λ is some affine parameter. Let us choose this parameter λ as the observer’s proper time τ also denoted by T. The tangent vector uμ ≡ dzEμ/dT then is the observer’s 4-velocity that is normalized according to g μν (dzEμ/dT)(dzEν/dT) = ds²/dT² = -c², (5.6.1)

since ds² = -c²dτ² along the observer’s world-line. In the following we will denote the unit vector in the direction of uμ by e(0)μ ≡ uμ/c. (5.6.2)

Let aμ ≡ uμ;ν uν (5.6.3)

be the observer’s 4-acceleration, a vector that is perpendicular to uμ since aμ uμ = (g μν uμ uν);σ uσ = 0 (5.6.4)

in virtue of the normalization condition and g μν;σ = 0.

A set of four orthonormal vectors e(α)μ (α = 0,1,2,3) with e(0)μ being given by (5.6.2) and g μν e(α)μ e(β)ν = ηαβ (5.6.5)

along LE is called a tetrad field along LE. Such tetrad fields are valuable quantities that can be used in different respects, e.g., for the construction of observables. They can also be used to define useful local coordinates Xα = (cT, Xa) for the observer. First the local time coordinate T will be chosen as proper time τ of the observer whose world-line should be given by Xa = 0, i.e., the observer is located at the spatial origin of his local coordinate system. Next we define: a local system of coordinates Xα is called tetrad-induced if e(α)μ = ∂xμ/∂Xα | LE. (5.6.6)

From this definition we find that the tetrad vectors in tetrad-induced coordinates (TIC) take a particularly simple form η(αβ) ≡ e(α)μ e(β)ν g μν | LE = (∂Xβ/∂Xγ) | LE (∂Xα/∂Xδ) | LE δγδ = δαβ . (5.6.7)

Using this condition in TIC we find G αβ | LE = ηαβ . (5.6.8)

Hence, TIC are locally Minkowskian. We will now construct certain TIC in the neighbourhood of LE by imposing certain constraints on the Christoffel-symbols. To this end we consider the following quantities (E(γ)ρ, D E(α)ρ) ≡ G ρσ E(β)σ;κ E(α)κ;γ . (5.6.9)

Because of the simple form of tetrad vectors in TIC, Eq. (5.6.7), we have E(β)ρ;κ = E(β)ρ,κ + (ρ κτ) E(β)τ = (ρ κτ) E(β)τ that leads to (E(γ)ρ, D E(α)ρ) | LE = ηβγ (ρ αβ) | LE . (5.6.10)

Lemma 5.1 The Christoffel-symbols in TIC obey the following relations at LE: (0 00) = 0, (a 00) = (0 0a) = Aa/c², (b 0a) = Ω(a)(b)/c, (5.6.11)

where Aa are the spatial tetrad components of the 4-acceleration of E, i.e., Aa ≡ g μν e(a)μ aν (5.6.12)

and Ω(a)(b) ≡ c·(E(b)ρ, D E(a)ρ). (5.6.13)

The quantities Ω(a)(b) are called Ricci-rotation coefficients.

Exercise 5.1 Use the orthonormality of tetrad vectors to proof the antisymmetry of rotation coefficients Ω(a)(b) = -Ω(b)(a). (5.6.14)

The proof of Lemma 5.1 follows from (5.6.10), the definition of the 4-acceleration and the orthonormality of tetrad vectors. This Lemma implies that all Christoffel-symbols of TIC at the observer’s worldline are fixed apart from (α bc).

We now have several possibilities to fix these remaining quantities at LE.

Exercise 5.2 Suppose the X, Y, Z coordinate lines Y(α), which are integral curves to the tetrad e(α), are geodesics, parametrized with proper length s. Show that for that case (α bc) | LE = 0. (5.6.15)

Corresponding TIC will be called local geodetic proper coordinates.

The last Exercise shows one possible choice for (α bc). Another one is given by TIC that are locally harmonic. The harmonicity condition at LE can be written in the form G αβ (λ αβ) = 0, i.e., (λ aa) = (λ 00). (5.6.16)

One solution of the harmonicity condition along LE reads (0 bc) = 0, (bc a) = - (δba Ac + δca Ab - δbc Aa)/c². (5.6.17)

We will call local TIC with such Christoffel-symbols local harmonic proper coordinates.

Because the covariant derivative of the metric tensor vanishes, i.e., 0 = G αβ;γ = G αβ,γ - (α δγ) G δβ - (β δγ) G αδ , (5.6.18)

the Christoffel-symbols at LE determine the partial derivatives of G αβ at the worldline of E.

Exercise 5.3 Show that condition (5.6.18) for local geodetic proper coordinates leads to G αβ,0 = 0, G ab,c = 0, G 00,a = 2Aa/c², G 0a,b = (1/c) Ω(abc). (5.6.19)

Together with G αβ | LE = ηαβ this leads to a metric tensor of the form G 00 = -(1 + 2 A·X/c² + O(|X|²)), G 0a = (1/c) Ω(abc) Xc + O(|X|²), (5.6.20)

G ab = δab + O(|X|²)

with Ω(abc) = Ω(c) Ω(ab)c. (5.6.21)

For local harmonic proper coordinates condition (5.6.18) leads to G αβ,0 = 0, G ab,c = (1/c²) δab Ac, G 00,a = 2Aa/c², G 0a,b = (1/c) Ω(abc) (5.6.22)

at the observer’s world-line. Using G αβ | LE = ηαβ this leads to a metric tensor of the form G 00 = -(1 + 2 A·X/c² + O(|X|²)), G 0a = (1/c) Ω(abc) Xc + O(|X|²), (5.6.23)

G ab = δab (1 - 2 A·X/c² + O(|x|²)), where Ω(abc) is again given by relation (5.6.21).

Finally, let us try to understand the meaning of our ‘angular velocity’ Ω(b). To this end the definition of the Fermi-derivative is useful. Let Bμ be some contravariant vector-field along LE with tangent vector field eμ = uμ/c and 4-acceleration aμ. Then the Fermi-derivative DFBμ is defined by DF Bμ ≡ Du Bμ + (1/c³)(uν Bν) aμ - (1/c³)(aν Bν) uμ (5.6.24)

with Du Bμ ≡ c Bμ;ν e(ν 0) . (5.6.25)

Exercise 5.4 Show that the Fermi-derivative has the following properties: (i) DF e(0)μ = 0.

(ii) Let Aμ and Bμ be two contravariant vector-fields along LE with DF Aμ = DF Bμ = 0.

Then g μν Aμ Bν | LE = const.

(iii) Let Aμ be some contravariant vector-field along LE, perpendicular to uμ, then DF Aμ = (Du Aμ)⊥, where ⊥ denotes the projection of a vector Bμ perpendicular to uμ, i.e., B⊥μ ≡ (δμν + (1/c²) uμ uν) Bν.

Let us now consider the vector-field Cμ ≡ Du e(a)μ | LE .

Obviously we can decompose Cμ according to Cμ = - Cσ e(σ 0) e(μ 0) + Cσ e(σ b) e(μ b)

i.e., at the observer’s worldline we get Du e(a)μ = - g ρσ (Du e(a)ρ) e(σ 0) e(μ 0) + g ρσ (Du e(a)ρ) e(σ b) e(μ b) . (5.6.26)

From the orthonormality condition g ρσ e(σ 0) e(a)ρ = 0 we get g ρσ (Du e(a)ρ) e(σ 0) + g ρσ (Du e(0)ρ) e(a)σ = 0 that we can use to rewrite the first term in the right-hand side of (5.6.26). Adding to this equation a vanishing uμ-term we get along LE: DF e(a)μ = Ω(a)(b) e(b)μ / c . (5.6.27)

This relation proofs the following:

Theorem 5.2 If the tetrads e(α)μ along LE are Fermi-Walker transported, i.e., DF e(α)μ = 0, the Ricci rotation-coefficients vanish, i.e., Ω(a)(b) = 0.

Finally let us study the motion of a test-body in free-fall in the e vicinity of the observer. Let \(Z_\alpha(T) \equiv (cT, Z_a)\) denote the world-line of this test-body, given by a geodesic of the form \[ \frac{d^2 Z_a}{dT^2} = -\Gamma^\alpha_{\beta\gamma} \frac{dZ^\beta}{dT} \frac{dZ^\gamma}{dT} + \Gamma^0_{\beta\gamma} \frac{dZ^\beta}{dT} \frac{dZ^\gamma}{dT} \frac{dZ^a}{dT}, \]

that we will analyze at \(L\), i.e., for \(Z_a = 0\). By taking into account of the corresponding Christoffel-symbols at \(X^a = 0\) this equation in local harmonic proper coordinates takes the form \[ \frac{d^2 \vec{Z}}{dT^2} + 2(\vec{\Omega} \times \vec{V}) = -\frac{1}{c^2} \left(1 - \frac{V^2}{c^2}\right) \vec{A} \quad (5.6.28)

\]

with \(\vec{V} \equiv d\vec{Z}/dT\). Hence, \(\vec{\Omega}\) describes nothing but a Coriolis-force due to the rotational motion of spatial axes. The term on the right-hand side of (5.6.28) presents the inertial acceleration due to the 4-acceleration of the observer.

Exercise 5.5 Show that in local geodetic proper coordinates the geodesic equation at \(L\) takes the form (seealso Misner et al. 1973, Exercise (13.14))

\[ \frac{d^2 \vec{Z}}{dT^2} + 2(\vec{\Omega} \times \vec{V}) = -\vec{A} + \frac{1}{c^2} \vec{V}(\vec{V} \cdot \vec{A}). \quad (5.6.29)

\]

Local TIC will be called dynamically non-rotating or locally inertial if \(\vec{\Omega} = 0\). In that case the local reference system will show no inertial forces due to the rotational motion of spatial basis vectors. Technically speaking this means that \(G_{0a} = 0\) for dynamically non-rotating local coordinates. As we have seen the dynamically non-rotating local proper coordinates result from Fermi-transported tetrad vectors.

## 5.7 Proper Reference Systems of Accelerated Observers

Let us start with inertial Minkowskian coordinates \(x^\mu = (ct, \vec{x})\) and consider an observer that is moving along the x-axis with constant 4-acceleration, i.e., \[ a^\mu a_\mu = -a_0 a^0 + a_1 a^1 = g^2. \quad (5.7.1)

\]

Together with \(u^\mu u_\mu = -c^2\) or \[ u_0 u^0 - u_1 u^1 = c^2 \quad (5.7.2)

\]

and \(u^\mu a_\mu = 0\), i.e., \[ u_0 a^0 - u_1 a^1 = 0 \quad (5.7.3)

\]

we get \[ g^2 = \frac{a_1 a^1}{u_0 u^0} = \frac{a_0 a^0}{u_1 u^1} \]

or \[ g = c \frac{a_1}{u^0} = c \frac{a_0}{u^1}. \quad (5.7.4)

\]

Thus, \[ a^0 = \frac{du^0}{d\tau} = \frac{g}{c} u^1 \quad (5.7.5)

\]

\[ a^1 = \frac{du^1}{d\tau} = \frac{g}{c} u^0.

\]

A special solution of these two differential equations is given by \[ z^0_{\text{obs}}(\tau) = \frac{c^2}{g} \sinh \alpha \quad (5.7.6)

\]

\[ z^1_{\text{obs}}(\tau) = \frac{c^2}{g} \cosh \alpha \]

with \[ \alpha = \frac{g \tau}{c}.

\]

From this we get \[ u^0(\tau) = \frac{dz^0_{\text{obs}}}{d\tau} = c \cosh \alpha \quad (5.7.7)

\]

\[ u^1(\tau) = \frac{dz^1_{\text{obs}}}{d\tau} = c \sinh \alpha \]

and \[ a^0(\tau) = \frac{du^0}{d\tau} = g \sinh \alpha \quad (5.7.8)

\]

\[ a^1(\tau) = \frac{du^1}{d\tau} = g \cosh \alpha.

\]

Since \(\cosh^2 x - \sinh^2 x = 1\) the trajectory of the observer, \(L_{\text{obs}}\), is given by \[ x_{\text{obs}}^2 - c^2 t_{\text{obs}}^2 = \frac{c^4}{g^2}, \quad (5.7.9)

\]

i.e., by a hyperbola in our inertial Minkowskian coordinates. Next we construct a local co-moving tetrad field along \(L_{\text{obs}}\). The observer’s 4-velocity reads \[ u^\mu = \frac{dz_{\text{obs}}}{d\tau} = c(\cosh \alpha, \sinh \alpha, 0, 0)

\]

so that the unit vector \(\vec{e}_{(0)}^\mu\) in the direction of \(u^\mu\) is given by \[ \vec{e}_{(0)}^\mu = \frac{u^\mu}{c} = (\cosh \alpha, \sinh \alpha, 0, 0). \quad (5.7.10)

\]

The corresponding spatial tetrad vectors, kinematically non-rotating with respect to the original Minkowskian coordinates, can then be chosen according to \[ \vec{e}_{(1)}^\mu = (\sinh \alpha, \cosh \alpha, 0, 0)

\]

\[ \vec{e}_{(2)}^\mu = (0, 0, 1, 0) \quad (5.7.11)

\]

\[ \vec{e}_{(3)}^\mu = (0, 0, 0, 1).

\]

It is interesting to note that this tetrad field can easily be obtained from the Minkowskian basic vectors at rest: \[ \bar{\vec{e}}_{(\alpha)}^\mu = \delta^\mu_\alpha. \quad (5.7.12)

\]

We first write the tetrads \(\vec{e}_{(\alpha)}^\mu\) in terms of the observer’s coordinate velocity \[ v = \frac{dz_{\text{obs}}}{dt} = \left(\frac{dz_{\text{obs}}}{d\tau}\right)^{-1} = c \cdot \tanh \alpha. \quad (5.7.13)

\]

With \[ \beta \equiv \frac{v}{c} = \tanh \alpha; \quad \gamma \equiv (1 - \beta^2)^{-1/2} = \cosh \alpha \]

we get \[ \vec{e}_{(0)}^\mu = \gamma (1, \beta, 0, 0) \quad (5.7.14)

\]

\[ \vec{e}_{(1)}^\mu = \gamma (\beta, 1, 0, 0).

\]

From this we see that the co-moving tetrads can be obtained from \(\bar{\vec{e}}_{(\beta)}^\mu\) by means of a Lorentz-boost: \[ \vec{e}_{(\alpha)}^\mu = \mathcal{L}_{(\alpha)}^{(\beta)}(\beta) \, \bar{\vec{e}}_{(\beta)}^\mu \quad (5.7.15)

\]

with \[ \mathcal{L}_{(\alpha)}^{(\beta)}(\beta) = \begin{pmatrix} \gamma & \gamma\beta & 0 & 0 \\ \gamma\beta & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}. \quad (5.7.16)

\]

Next we consider the coordinate transformation from inertial Minkowskian coordinates \(x^\mu = (ct, \vec{x})\) to local co-moving coordinates \(X^\alpha = (cT, \vec{X})\) with \(T = \tau\), the proper-time of the observer, with the ansatz \[ x^\mu(X^\alpha) = z^\mu(T) + \vec{e}_{(a)}^\mu X^a + \xi^\mu(T, \vec{X}), \quad (5.7.17)

\]

where \(\xi^\mu\) is at least of second order in \(|\vec{X}|\). For the Jacobian of this transformation \[ A^\mu_{\ \ \nu} \equiv \frac{\partial x^\mu}{\partial X^\nu} \quad (5.7.18)

\]

we get \[ A^0_{\ \ 0} = \vec{e}_{(0)}^0 + \frac{1}{c} \frac{d\vec{e}_{(a)}^0}{dT} X^a + \xi^0_{\ ,0} \quad (5.7.19)

\]

\[ A^\mu_{\ \ a} = \vec{e}_{(a)}^\mu + \xi^\mu_{\ ,a}.

\]

Since \[ \frac{d}{dT} \vec{e}_{(0)} = \frac{g}{c} \vec{e}_{(1)}; \quad \frac{d}{dT} \vec{e}_{(1)} = \frac{g}{c} \vec{e}_{(0)} \]

\(A^\mu_{\ \ \nu}\) can be written in the form \[ A^0_{\ \ 0} = \tilde{\eta} \, \vec{e}_{(0)}^0 + \xi^0_{\ ,0} \quad (5.7.20)

\]

with \[ \tilde{\eta} = 1 + \frac{g X}{c^2}.

\]

Now, our original Minkowskian coordinates are both geodetic and harmonic. For the local coordinates the condition of TIC ensures that the local metric tensor, \(G_{\alpha\beta}\), is Minkowskian at the origin, i.e., \(G_{\alpha\beta}(X = 0) = \eta_{\alpha\beta}\). Higher order terms in \(|\vec{X}|\), linear, quadratic and higher are not fixed so far. We can fix them by coordinate conditions that we can impose on the local coordinates or we can specify the transformation functions \(\xi^\mu\).

Let us start with \[ \xi^\mu = 0. \quad (5.7.21)

\]

Then the metric tensor \(G_{\alpha\beta}\) in local coordinates according to the tensor transformation rule takes the form: \[ G_{00} = A^\alpha_{\ \ 0} A^\beta_{\ \ 0} \eta_{\alpha\beta} = -A^0_{\ \ 0} A^0_{\ \ 0} + A^i_{\ \ 0} A^i_{\ \ 0} = -(\tilde{\eta})^2 \]

\[ G_{0a} = A^\alpha_{\ \ 0} A^\beta_{\ \ a} \eta_{\alpha\beta} = -A^0_{\ \ 0} A^0_{\ \ a} + A^i_{\ \ 0} A^i_{\ \ a} = 0 \quad (5.7.22)

\]

\[ G_{ab} = A^\alpha_{\ \ a} A^\beta_{\ \ b} \eta_{\alpha\beta} = -A^0_{\ \ a} A^0_{\ \ b} + A^i_{\ \ a} A^i_{\ \ b} = \delta_{ab} \]

or \[ ds^2 = -\left(1 + \frac{g X}{c^2}\right)^2 c^2 dT^2 + dX^2. \quad (5.7.23)

\]

Exercise 5.6 Proof that the spatial coordinate lines \(X = \text{const.}\); \(T = \tau = \text{const.}\) are geodesics, i.e., the coordinates \((cT, \vec{X})\) defined by \(\xi^\mu = 0\) are geodetic proper coordinates.

Next we will assume a special form of the local metric tensor \[ G_{00} = -\left(1 + \frac{2g X}{c^2}\right) + O(c^{-4})

\]

\[ G_{0a} = 0 \quad (5.7.24)

\]

\[ G_{ab} = \delta_{ab} \left(1 - \frac{2g X}{c^2}\right) + O(c^{-4}).

\]

In that case \[ G \equiv -\det(G_{\alpha\beta}) = 1 - \frac{4g X}{c^2} + O(c^{-4}) \quad (5.7.25)

\]

and \[ G G^{ab} = \delta^{ab} + O(c^{-4}), \quad (5.7.26)

\]

so that these spatial coordinates are harmonic up to terms of order \(c^{-4}\).

Exercise 5.7 Show that the local metric (5.7.24) can be obtained with \[ \xi^0(T, \vec{X}) = O(c^{-3})

\]

\[ \xi^a(T, \vec{X}) = \frac{1}{2} \eta^{ai} \left( T_i(T) \frac{1}{c^2} \left[ A X^2 - X^a (\vec{A} \cdot \vec{X}) \right] \right) + O(c^{-4}) \quad (5.7.27)

\]

where \[ A_a = \eta_{\mu\nu} \vec{e}_{(a)}^\mu \frac{d^2 z^\nu_{\text{obs}}}{dT^2} = (g, 0, 0). \quad (5.7.28)

\]

## 5.8 The Landau-Lifshitz Formulation of GR

5.8.1 The Landau-Lifshitz Field Equations Landau and Lifshitz (1941, 1971) have derived a special form of the Einstein field equations, which presents a very useful starting point for solving the field equations with perturbative expansions. The atomic variable of the Landau-Lifshitz (LL) formalism is called \(h^{\alpha\beta}\), defined by (5.8.13) and the field equation in harmonic gauge are quasi-linear hyperbolic differential equations of the form \(\Box h^{\alpha\beta} = (16\pi G/c^4)\tau^{\alpha\beta}\), where \(\Box \equiv \eta^{\mu\nu}\partial_{\mu\nu}\) is the flat space d’Alembertian (the flat space wave operator) and \(\tau^{\alpha\beta}\) is the gravitational source tensor, that itself contains \(h^{\alpha\beta}\)-terms. Under a condition of ‘no incoming gravitational radiation’, the field equations (in harmonic gauge) can formally be solved in terms of retarded integrals (see (5.8.36) below) over quantities involving the atomic variable itself. To derive explicit results for \(h^{\alpha\beta}\), the source term \(\tau^{\alpha\beta}\) can be expanded in terms of small quantities as measures of weak gravitational fields, small velocities and small internal stresses. The MPM-formalism discussed in Chap. 7 presents such a scheme, where suitable expansions of \(\tau^{\alpha\beta}\) lead to fully explicit expressions for \(h^{\alpha\beta}\), even at high orders in the small parameters.

The LL-formalism is based upon the ‘gothic metric’, defined by \[ \mathfrak{g}^{\alpha\beta} \equiv -g g^{\alpha\beta}, \quad (5.8.1)

\]

where \(g \equiv \det(g_{\alpha\beta})\). Note, that \(\mathfrak{g}^{\alpha\beta}\) is not a tensor but a tensor density. Let \(g_{\alpha\beta}\) be the inverse of \(\mathfrak{g}^{\alpha\beta}\) and \(g \equiv \det(g_{\alpha\beta})\). Then, \[ g = \det(g_{\alpha\beta}) = \det(-g \mathfrak{g}^{\alpha\beta}) = g^2 \det(\mathfrak{g}^{\alpha\beta}) = g. \quad (5.8.2)

\]

If we take the inverse matrix of \[ \mathfrak{g}_{\alpha\beta} = (-g)^{-1/2} g_{\alpha\beta} \]

we therefore get \[ \sqrt{-g} \, g^{\alpha\beta} = \sqrt{-g} \, g_{\alpha\beta} = \mathfrak{g}^{\alpha\beta}. \quad (5.8.3)

\]

Let us define (e.g., Poisson and Will 2014)

\[ H^{\alpha\mu\beta\nu} \equiv g^{\alpha\beta} g^{\mu\nu} - g^{\alpha\nu} g^{\beta\mu}. \quad (5.8.4)

\]

Now, \(H^{\alpha\mu\beta\nu}\) has the same properties as the Riemann tensor, \[ H^{\alpha\mu\beta\nu} = -H^{\mu\alpha\beta\nu}, \quad H^{\alpha\mu\beta\nu} = -H^{\alpha\mu\nu\beta}, \quad H^{\alpha\mu\beta\nu} = +H^{\beta\nu\alpha\mu}. \quad (5.8.5)

\]

\[ \frac{16\pi G}{c^4} \partial_\mu H^{\alpha\mu\beta\nu} = 2\sqrt{-g} G^{\alpha\beta} + \sqrt{-g} \, t^{\alpha\beta}_{LL} \quad (5.8.6)

\]

where \(G^{\alpha\beta} = R^{\alpha\beta} - (1/2)g^{\alpha\beta} R\) is the Einstein tensor and \(t^{\alpha\beta}_{LL}\) is the Landau-Lifshitz pseudotensor: \[ \frac{16\pi G}{c^4} \sqrt{-g} \, t^{\alpha\beta}_{LL} = g^{\alpha\beta} g_{\lambda\mu,\rho} g^{\lambda\nu} g^{\rho\mu} - g^{\alpha\lambda} g_{\lambda\mu,\rho} g^{\beta\nu} g^{\mu\rho} \]

\[ - g^{\beta\lambda} g_{\lambda\mu,\rho} g^{\alpha\nu} g^{\mu\rho} + g g_{\nu\rho} g^{\alpha\lambda} g^{\beta\mu} \quad (5.8.7)

\]

\[ + \frac{1}{8} (2g^{\alpha\lambda} g^{\beta\mu} - g^{\alpha\beta} g^{\lambda\mu})(2g_{\nu\rho,\sigma} g_{\rho\sigma,\tau} g^{\nu\tau} - g_{\rho\sigma,\nu\tau}) g^{\ 在谐和规范下，场方程写为 □hαβ = 16πG/c⁴ |g|Tαβ + Ξαβ (5.8.31)

其中“引力源项” Ξαβ 表示为 Ξαβ ≡ 16πG/c⁴ |g|tLL αβ + hαν hβμ,ν ,μ − hμν hαβ,μν 或者，明确写出 Ξαβ = hαν,μ hβμ,ν − hμν,μ hαβ,ν + 1/2 gαβ gλμ hλν,ρ hρμ,ν − (gαλ gμν hβν,ρ hμρ,λ + gβλ gμν hαν,ρ hμρ,λ ) + gλμ gνρ hαλ,ν hβμ,ρ (5.8.32)

+ 1/8 (2gαλ gβμ − gαβ gλμ) (2gνρ gστ − gρσ gντ) hντ,λ hρσ,μ.

我们看到，引力源项包含至少是h的二次项以及其一阶和二阶导数的度规张量的乘积。我们用明显的记号写出 Ξαβ = Ξαβ[h,h]₂ + Ξαβ[h,h,h]₃ + O(h⁴) (5.8.33)

其中 Ξαβ₂ = −1/2 hρσ ∂ρ ∂σ hαβ + 1/2 ∂α hρσ ∂β hρσ − 1/4 ∂α h ∂β h + ∂ρ hασ (∂σ hβρ + ∂ρ hβσ)

− 2 ∂(α hρσ ∂ρ hβ)σ + ηαβ [ −1/8 ∂ρ h ∂τ hρσ + 1/8 ∂ρ h ∂ρ h + 1/4 h ∂σ hρτ ].

(5.8.34)

所有指标都用闵可夫斯基度规 ημν 升降；h ≡ ηαβ hαβ；指标周围的括号表示对称化。Ξαβ₂ 和 Ξαβ₃ 的显式表达式可在 Blanchet and Faye (2001a) 中找到。

在某些假设下，场方程 (5.8.28) 可以形式上求解。通常施加某种“无入射辐射”条件，形式为 [∂t hαβ(t, x)] = 0 for t ≤ −T. (5.8.35)

在此条件下，方程 (5.8.28) 形式上解为 hαβ(t, x) = 16πG/c⁴ R⁻¹ ταβ (5.8.36)

其中 (R⁻¹ f)(t, x) ≡ −1/(4πR) ∫ d³x' f(tRet, x')/|x − x'| (5.8.37)

其中推迟时间 tRet 由下式给出 tRet ≡ t − |x − x'|/c. (5.8.38)

## 第6章 精确解——场矩

爱因斯坦场方程的精确解在应用广义相对论领域（如果我们排除相对论天体物理学和宇宙学）并不扮演核心角色；然而，它们可以作为理解重力起作用的某些实际系统方面的指南，并作为构建近似形式的辅助。EFE已发现大量精确解；读者可参阅标准文献（例如，Stephani et al. 2003; Griffiths and Podolsky 2009）。

## 6.1 闵可夫斯基时空

显然，爱因斯坦场方程最简单的真空解是闵可夫斯基时空，其中在闵可夫斯基坐标中，度规取形式 gμν = ημν = diag(−1, +1, +1, +1). (6.1.1)

Killing方程 ∇(ν ξμ) = 0, (6.1.2)

则读作 ξμ,ν + ξν,μ = 0 解的形式为 ξμ = aμ + bμν xν (6.1.3)

其中 bμν = −bνμ.

这导致总共10个独立的Killing矢量场。aμ 描述4个独立的无穷小时空平移。b_ij 项描述绕k轴的无穷小旋转，其中(ijk) εijk ≠ 0。例如，对于 b12 = −b21 = 1，Killing矢量场的空间分量为 Rk = (y, −x, 0)，描述绕z轴的无穷小旋转，因为变换 x' = x cosθ + y sinθ, y' = −x sinθ + y cosθ 到θ的一阶可以写成 x' = x + θ Rk。

我们现在将证明由 b0i 诱导的剩余三个Killing变换等价于三种形式的洛伦兹提升 ct' = γ(ct − βx); x' = γ(x − βct)

或等价地 ct' = coshα · ct − sinhα · x; x' = −sinhα · ct + coshα · x (6.1.4)

其中我们写 β = tanhα，因此 γ = coshα。让我们现在在具有坐标 xμ = (x⁰, x) 的二维时空中论证。在本小节的剩余部分，我们将 x 写为 (x⁰, x)。选择 b01 = −b10 = 1，我们得到 ξμ = −(x, x⁰)，因此无穷小Killing变换为： x' = x + ξ = x − θ D̂ x (6.1.5)

其中 D̂ = [0 1; 1 0]. (6.1.6)

对于非无穷小变换，我们将 θ 替换为 α 并写为 x' = exp(−α D̂) · x = ∑_{m=0}^{∞} (−1)^m / m! α^m D̂^m · x. (6.1.7)

现在，D̂ 的每个偶数次幂等于单位矩阵，而每个奇数次幂等于 D̂ 本身。因此， x' = [∑_{m=0}^{∞} (−1) α^{2m+1} / (2m+1)! [0 1; 1 0] + ∑_{m=0}^{∞} α^{2m} / (2m)! [1 0; 0 1]] x = [−sinhα [0 1; 1 0] + coshα [1 0; 0 1]] x (6.1.8)

这等价于 (6.1.4)。由于最多可以有 n(n+1)/2 个独立的Killing矢量场，闵可夫斯基时空是最大对称的（例如，Weinberg 1972）。

## 6.2 静态时空

如果存在一个类时的Killing矢量场，则称时空流形是静态的。考虑一束类时曲线 xμ(λ)，它以适当选择的时间坐标 λ = x⁰ 参数化，使得其切矢量场取形式 ξμ = (1, 0, 0, 0)。那么， [Lξ g]μν = dxσ / dλ ∂gμν / ∂xσ = 1/c ∂gμν / ∂t.

因此，如果一个时空是静态的，并且有一个满足Killing方程 (6.1.2) 的类时Killing矢量场，则可以选择时间坐标 t，使得度规张量的分量独立于 t。Killing矢量场 ξμ 然后定义一个量 f， f = −ξμ ξμ = −gμν ξμ ξν > 0, (6.2.1)

即 ξμ 的（正）模长。此外，ξμ 的扭转4-矢量 ωμ 定义为 ωμ = εμνλσ ξν ∇λ ξσ = εμνλσ ξν gλρ ξσ,ρ. (6.2.2)

Killing矢量场的模长与所选时钟之间的红移效应有关。扭转矢量衡量Killing矢量场偏离正交于一族3-曲面的程度。

引理6.1 发现 ∇[μ ων] = εμνλσ ξλ Rκσ ξκ. (6.2.3)

证明 我们首先将 ∇[μ ων] 重写为 ∇[μ ων] = − εμνλσ ελσαβ ∇α ωβ, (6.2.4)

因为 ∇α εμνλσ = 0。然后利用 (6.2.2)，我们得到 ∇[μ ων] = − εμνλσ [ελσαβ εβγρτ ∇α ξγ ∇ρ ξτ]

= − εμνλσ [6 ∇α (ξ[α ∇λ ξσ])] (此处原文推导有误，应为利用Killing方程和曲率张量恒等式，最终得到 ∇[μ ων] = εμνλσ ξλ Rσκ ξκ)

...

= εμνλσ ξλ Rσκ ξα. (6.2.5)

由于Killing方程，第四行的第一项消失；对于第四行的第二项，利用方程 (2.11.8) 得到第五行的第一项，该项也因黎曼张量的反对称性而消失；第五行中第二项和第三项的和由于Killing方程为零；然后再次使用方程 (2.11.8) 得到最终结果。

因此，在 Rσκ = 0 的真空区域，扭转矢量承认一个势 ω，ωμ = ∇μ ω, (6.2.6)

称为扭转势。

关系式 (6.1.2)、(6.2.1) 和 (6.2.2) 是投影形式（例如，Geroch 1971）的基础，该形式将4维时空 (M, g) 的微分几何结构与3空间 M(3) 中的相应结构联系起来。这个3空间可以选择为 ξμ 的所有轨迹的集合；也就是说，M(3) 的一个元素是 M 中一条处处与 ξμ 相切的曲线。如果 ξμ 是超曲面正交的（见下文）且 ω = 0，则 M(3) 可以用 t = const 超曲面表示。

静态时空在适应坐标中的度规可以写成形式（例如，Israel and Wilson 1972; Kinnersley 1973）

ds² = −f(cdt + wi dxi)² + f⁻¹ hij dxidxj (6.2.7)

其中 i, j = 1, 2, 3，且度规函数 f, wi, hij 独立于 t。

(6.2.7) 中的数量 hij 定义了 M(3) 上的一个度规张量。通常，例如在非适应坐标中，将存在一个度规张量 hμν = fgμν + ξμ ξν (6.2.8)

在 M(3) 上，其相应的协变导数记为 Di。在 ξμ = (1, 0, 0, 0) 的适应坐标中，3空间的度规取形式 hij = −g00 gij + g0i g0j. (6.2.9)

让我们用 ∇μ 和 Rμν 表示 (M, g) 中的协变导数和里奇张量，用 Di 和 Rij(3) 表示 (M(3), h) 中的相应量。(M(3), h) 中的拉普拉斯算子将记为 D² ≡ Di Di. (6.2.10)

(6.2.7) 中的3-矢量 w 与扭转4-矢量场的空间部分相关（例如，Kinnersley 1973）

ω = f² D × w. (6.2.11)

这个关系可以在 ξμ = (1, 0, 0, 0) 的适应坐标中通过直接计算验证。

场方程然后可以写成（例如，Tanabe 1976; Bäckdahl and Herberthson 2005; Bäckdahl 2008, Eqs. (11)）

f D² f = Di f Di f − Di ω Di ω (6.2.12)

f D² ω = 2 Di f Di ω (6.2.13)

2 f² Rij(3) = (Di f)(Dj f) + (Di ω)(Dj ω). (6.2.14)

证明基本上可以在 Geroch (1978) 的附录中找到，并对 hij（本文中称为 h）进行了轻微修改。证明中涉及两个基本方程： ... (6.2.15) (此处公式符号混乱，略)

∇α ∇β ξγ = Rγαβδ ξδ (6.2.16)

这些方程中的第一个可以在 Killing矢量场 ξα = (1, 0, 0, 0) 和 ξα = −(f, fwi) 的适应坐标中通过直接计算最好地证明，第二个则留作练习（见下文）。将 D² 应用于 (6.2.1) 并使用上述两个方程，我们得到 f 的场方程 (6.2.12)。取 (6.2.2) 的散度，记住 ωμ = ∇μ ω 并再次使用上述两个方程，我们得到扭转势 ω 的场方程。

令人非常感兴趣的是 ω = 0 的静态情况。令 f = e²ψ，真空场方程采取形式 Di Di ψ = 0 (6.2.17)

Rij(3) = 2 Di ψ Dj ψ. (6.2.18)

第一个场方程 (6.2.17) 是势 ψ 的（协变）拉普拉斯方程。在牛顿极限下 f = −g00 = 1 − 2U/c²，因此 ψ = −U/c²。Rij(3) 是 1/c⁴ 量级。

练习6.1 证明关系式 ξσ;λν = Rμνλσ ξμ (6.2.19)

该式用于推导场方程 (6.2.12) (Geroch 1978, (A13))。

证明 我们使用Killing方程 ξσ;λ = −ξλ;σ, 曲率张量的定义 ξσ;λν − ξσ;νλ = −Rμσνλ ξμ 以及第一比安基恒等式 Rμσνλ + Rμλσν + Rμνλσ = 0 来重写 (6.2.19) 的左边： ξσ;λν = −Rμσνλ ξμ + ξσ;νλ = −Rμσνλ ξμ − ξν;σλ = −Rμσνλ ξμ − Rμνσλ ξμ + ξλ;νσ = −(Rμσνλ + Rμνσλ + Rμλσν) ξμ − ξσ;λν 因此 2 ξσ;λν = −(Rμσνλ + Rμνσλ + Rμλσν) ξμ = 2 Rμνλσ ξμ.

如果给定3-度规 hij，则完整的4维时空由一个复值势 E 决定， E ≡ f + iω, (6.2.20)

称为恩斯特势（Ernst 1968a, b; Israel and Wilson 1972; Kinnersley 1973）。使用恩斯特势，f 和 ω 的场方程采取形式 f D² E = Di E Di E (6.2.21)

其中 f = ℜ(E) = 1/2 (E + E*). (6.2.22)

方程 (6.2.21) 称为恩斯特方程。

通常，代替恩斯特势 E，使用势 ξ，其中 ξ ≡ (1 + E)/(1 − E), (6.2.23)

因此 E = (ξ − 1)/(ξ + 1). (6.2.24)

ξ + 1 is introduced. Then the vacuum field equations take the form (e.g., Hoenselaers and Perjés 1980)

θD²ξ = 2ξ * D ξDξ (6.2.25)

θ²R (3) = D ξD ξ * + D ξ * D ξ = 2[D ξD ξ * ] (6.2.26)

ij i j i j i j with θ ≡ ξ * ξ − 1. (6.2.27)

The derivation of the above equations is straightforward. Expressing θ and D ξ in terms of f and ω, one gets 4f θ = , (1−E)(1−E*)

2D E D ξ = i , i (1−E)² 2D²E(1−E) + 4D EDξ E D²ξ = i i .

(1−E)³

Using these relations in (6.2.25) and (6.2.26) we recover the field equations in the form (6.2.12)–(6.2.14). For example, (6.2.25) becomes f[(1−E)D²E + 2D EDξ E] = (1+E*) D EDξ E, i i i from which we get (6.2.21). The right hand side of (6.2.26) reads 1+E 1+E* 1+E* 1+E 8[(D f)(D f) + (D ω)(D ω)]

D D + D D = i j i j , i 1−E j 1−E* i 1−E* j 1−E (1−E)²(1−E*)² from which we get (6.2.14) with the above expression for θ.

6.2.1 Stationary Axially Symmetric Space-Times A stationary space-time is called axially symmetric if it has a space-like Killing vector-field ημ with closed integral curves around some symmetry axis. In canonical Weyl coordinates (t,ρ,z,φ) ((ρ,z) are a special kind of cylindrical coordinates) the metric can be written in Weyl-Lewis-Papapetrou form (e.g., Papapetrou 1953) as: ds² = −f(cdt − Wdφ)² + f⁻¹ e²γ (dρ² + dz²) + ρ²dφ² , (6.2.28)

where f = f(ρ,z), W = W(ρ,z), γ = γ(ρ,z). The vacuum field equations can be divided into primary and secondary equations. The primary equations take the form f(f,ρρ + ρ⁻¹f,ρ + f,zz) − f,ρ² − f,z² + ρ⁻²f⁴(W,ρ² + W,z²) = 0 (6.2.29)

(ρ⁻¹f²W,ρ),ρ + (ρ⁻¹f²W,z),z = 0. (6.2.30)

The secondary equations read γ,ρ = ¼ ρf⁻²(f,ρ² − f,z²) − ¼ ρ⁻¹f²(W,ρ² − W,z²), (6.2.31)

γ,z = ½ ρf⁻²f,ρf,z − ½ ρ⁻¹f²W,ρW,z. (6.2.32)

The above equations can be derived from the vacuum field equation Rμν = 0 using the definition of the Ricci tensor. For example the 00-component of Rμν reads c²ρ²e⁻²γ [f(f,ρρ + ρ⁻¹f,ρ + f,zz) − f,ρ² − f,z² + ρ⁻²f⁴(W,ρ² + W,z²)]

R₀₀ = , (6.2.33)

2 3f²W² + ρ² so that the vacuum relation R₀₀ = 0 reduces to (6.2.29). Similarly, one derives the remaining three vacuum field equations.

Exercise 6.2 Prove the remaining field equations (6.2.30), (6.2.31) and (6.2.32)

from Rμν = 0.

The secondary equations suggest an over-determination of γ. However, taking the partial derivative of (6.2.31) with respect to z and the derivative of (6.2.32) with respect to ρ we get γ,ρz = γ,zρ by using the primary equations. Therefore γ can be solved by quadrature if the functions f and W have been found from the primary equations (e.g., Wald 1984; Islam 1985): γ(b) − γ(a) = ∫ₐᵇ (γ,ρ dρ + γ,z dz). (6.2.34)

As a result, finding the stationary and axisymmetric vacuum solutions of Einstein’s field equations reduces to first solving the primary equations for f and W in ordinary 3D Euclidean space, and then the function γ is obtained from (6.2.34).

Clearly, this greatly simplifies the problem of solving the original Einstein field equation for the ten unknown components of gμν.

Equation (6.2.30) implies the existence of a potential ω(ρ,z) such that ω,ρ = +ρ⁻¹f²W,z   ω,z = −ρ⁻¹f²W,ρ. (6.2.35)

This potential ω agrees with the scalar twist potential of the metric (6.2.28).

Relation (6.2.35) is often written as ∇ω = ρ⁻¹f²∇̃ W (6.2.36)

with ∇ = (∂ρ, ∂z) and ∇̃ = (∂z, −∂ρ). Another way of writing this relation is (Ernst 1968a,b)

∇ω = ρ⁻¹f² n̂φ × ∇W, (6.2.37)

where n̂φ is a unit vector in a azimuthal direction. This is because of n̂φ × n̂ρ = −n̂z and n̂φ × n̂z = n̂ρ.

Exercise 6.3 Show that the potential ω from (6.2.35) agrees with the twist potential of the metric (6.2.28).

Considering that in cylindrical coordinates ∇² = 1/ρ ∂/∂ρ (ρ ∂/∂ρ) + ∂²/∂z² + 1/ρ² ∂²/∂φ², the two primary field equations can then be written in the form f∇²f − f,ρ² − f,z² + ω,ρ² + ω,z² = 0 (6.2.38)

f∇²ω − 2f,ρ ω,ρ − 2f,z ω,z = 0 and the secondary equations can be written with the Ernst-potential, E ≡ f + iω, as γ,ρ = ¼ ρf⁻²(E,ρ E*,ρ − E,z E*,z ), (6.2.39)

γ,z = ¼ ρf⁻²(E,ρ E*,z + E,z E*,ρ ).

Often, instead of canonical Weyl coordinates (ρ,z), Weyl spherical or Weyl prolate spheroidal coordinates are employed. Weyl spherical coordinates (r,θ) are defined as r = (ρ² + z²)¹/²; cosθ = z/r. (6.2.40)

Prolate spheroidal coordinates (PS-coordinates) (μ,ν,ϕ) are defined by x = σ sinh μ sin ν cos ϕ y = σ sinh μ sin ν sin ϕ (6.2.41)

z = σ cosh μ cos ν, where σ is a constant with the dimension of a length (for the so-called Schwarzschild metric the constant σ will be identified with m = GM/c²; see below). μ is a non-negative real number, ν ∈ [0,π] and ϕ ∈ [0,2π]. Surfaces of constant μ are prolate spheroids, ν = const. surfaces are hyperboloids of revolution with focal points x± = (0,0,±σ) (see Fig. 6.1). Distances from the two focal points are given by (ρ² = x² + y²): r± ≡ √[ρ² + (z±σ)²] = σ(cosh μ ± cos ν). (6.2.42)

Exercise 6.4 Show that r± = σ(cosh μ ± cos ν).

Solution The result is directly obtained with sinh²μ = cosh²μ − 1.

Often, instead of (μ,ν,ϕ) an alternative set of prolate spheroidal coordinates (ζ,τ,φ) is used, where ζ ≡ (r+ + r−) / (2σ)

τ ≡ (r+ − r−) / (2σ) (6.2.43)

ϕ ≡ arctan(y/x). (6.2.44)

There is a unique relation between such PS-coordinates and Cartesian ones: x = σ √[(ζ²−1)(1−τ²)] cos ϕ y = σ √[(ζ²−1)(1−τ²)] sin ϕ (6.2.45)

z = σ ζ τ.

In the following, following the notation of the standard literature, we will denote the PS-coordinates (ζ,τ) by (x,y) having in mind that in the following part x and y are not Cartesian coordinates.

We now use the relations between the canonical Weyl coordinates (ρ,z) and PS-coordinates (x,y): ρ = σ √[(x²−1)(1−y²)], z = σ x y, to derive the relation dρ² + dz² = σ² [ x²(1−y²) dx²/(x²−1) + y²(x²−1) dy²/(1−y²) + (x² dy² + y² dx²) ]

= σ² [ y²(x²−1) dx²/(x²−1) + x²(1−y²) dy²/(1−y²) + (x² dy² + y² dx²) ]

= σ² (x²−y²) [ dx²/(x²−1) + dy²/(1−y²) ]. (6.2.46)

So in PS-coordinates (t,x,y,φ) the stationary axisymmetric vacuum Weyl-Lewis- Papapetrou metric takes the form ds² = −f(cdt − Wdφ)² + σ²f⁻¹ e²γ (x²−y²) [ dx²/(x²−1) + dy²/(1−y²) ] + (x²−1)(1−y²)dφ² , (6.2.47)

where σ is a constant. In the Ernst equation (6.2.21), Re(E) D²E = Dξ E Dξ E*, the Laplacian is now the usual Laplacian in Euclidian 3-space and D the usual gradient operator. In canonical Weyl coordinates ∇²E = E,ρρ + (1/ρ)E,ρ + E,zz ∇E · ∇E = (E,ρ)² + (E,z)². (6.2.48)

and in PS-coordinates ∇²E = 1/[σ²(x²−y²)] { ∂x [(x²−1) ∂x] + ∂y [(1−y²) ∂y] } E (6.2.49)

∇E · ∇E = 1/[σ²(x²−y²)] { (x²−1)(E,x)² + (1−y²)(E,y)² }. (6.2.50)

Exercise 6.5 Derive relations (6.2.49) and (6.2.50) that appear in the Ernst equation.

Proof E.g., ∂/∂x = (∂ρ/∂x) ∂/∂ρ + (∂z/∂x) ∂/∂z,   ∂/∂y = (∂ρ/∂y) ∂/∂ρ + (∂z/∂y) ∂/∂z, ∂²/∂x² = (∂²ρ/∂x²) ∂/∂ρ + (∂ρ/∂x)² ∂²/∂ρ² + (∂²z/∂x²) ∂/∂z + (∂z/∂x)² ∂²/∂z² + ..., with ∂ρ/∂x = σ x √[(1−y²)/(x²−1)],   ∂ρ/∂y = −σ y √[(x²−1)/(1−y²)], ∂²ρ/∂x² = −σ (1−y²)/(x²−1)³/²,   ∂²ρ/∂y² = σ (x²−1)/(1−y²)³/², ∂z/∂x = σ y,   ∂z/∂y = σ x,   ∂²z/∂x² = ∂²z/∂y² = 0.

Corresponding relations involving derivatives with respect to y can be derived.

Then, e.g., ∂x [(x²−1) ∂x] + ∂y [(1−y²) ∂y] E = (x²−1) ∂²ρ/∂x² E,ρ + (1−y²) ∂²ρ/∂y² E,ρ + (x²−1)(∂ρ/∂x)² E,ρρ + (1−y²)(∂ρ/∂y)² E,ρρ + (x²−1) ∂²z/∂x² E,z + (1−y²) ∂²z/∂y² E,z + (x²−1)(∂z/∂x)² E,zz + (1−y²)(∂z/∂y)² E,zz + cross terms involving mixed derivatives...

= σ²(x²−y²) [ E,ρρ + (1/ρ)E,ρ + E,zz ]. (6.2.51)

With the Ernst ξ-potential ξ = (1+E)/(1−E)

the Ernst equation (6.2.25) takes the form (ξξ * − 1) ∇²ξ = 2ξ * ∇ξ · ∇ξ. (6.2.52)

We notice that a useful feature of (6.2.49) and (6.2.50) is that both operators appearing there are symmetric under the interchange of the PS-coordinates x and y. Consequently, if ξ(x,y) is a solution of Eq. (6.2.52), then so is ξ(y,x). In this way, when ξ = x is a solution (the Schwarzschild solution, to be discussed later), then ξ = y is a new solution of the vacuum field equations. Therefore, a linear combination of the solutions ξ = x and ξ = y also satisfies (6.2.52). In this way one obtains an important solution to (6.2.52) (Ernst 1968a,b) in the form: ξ = x cos λ − i y sin λ, (6.2.53)

where λ is a constant. This is the ξ-potential of the Kerr metric to be discussed later.

Exercise 6.6 Show that ξ = x and ξ = y, where x and y are PS-coordinates are solutions to the vacuum field equations (6.2.52).

6.2.2 The Hartle-Thorne Metric The Hartle-Thorne metric is an ‘exact’ solution of vacuum Einstein field equations that describes the exterior of any slowly and rigidly rotating, stationary and axially symmetric body (Abramowicz et al. 2003). The metric is given with accuracy including second order terms in the dimensionless angular momentum parameter j ≡ S/(M m c) (where m ≡ GM/c²) and terms to first order in the dimensionless quadrupole parameter q = −Q/(M m²) (Hartle 1967; Hartle and Sharp 1967; Hartle and Thorne 1968). In spherical coordinates (ct,r,θ,φ) the Hartle-Thorne metric reads: ds² = gₜₜ c²dt² + gᵣᵣ dr² + gθθ dθ² + gφφ dφ² + gφₜ dφ cdt + gₜφ cdt dφ (6.2.54)

with: gₜₜ = −(1−2m/r)[1 + j² F₁ + q F₂]

gᵣᵣ = (1−2m/r)⁻¹[1 + j² G₁ − q F₂]

gθθ = r²[1 + j² H₁ + q H₂] (6.2.55)

gφφ = r² sin²θ[1 + j² H₁ + q H₂]

gₜφ = gφₜ = 2(m²/r) j sin²θ and (u = cosθ)

F₁ = [8m r⁴ (r−2m)]⁻¹ × [u²(48m⁶ − 8m⁵ r − 24m⁴ r² − 30m³ r³ − 60m² r⁴ + 135m r⁵ − 45r⁶)

+ (r−m)(16m⁵ + 8m⁴ r − 10m² r³ − 30m r⁴ + 15r⁵)] + A₁(r)

F₂ = [8m r (r−2m)]⁻¹ (5(3u²−1)(r−m)(2m²+6mr−3r²)) − A₁(r)

G₁ = [8m r⁴ (r−2m)]⁻¹ ((L−72m⁵ r) − 3u² (L−56m⁵ r)) − A₁(r)

L = 80m⁶ + 8m⁴ r² + 10m³ r³ + 20m² r⁴ − 45m r⁵ + 15r⁶ A₁ = (15r(2−2m)(1−3u²)/(16m²)) ln(r/(r−2m))

H₁ = (8m r⁴)⁻¹ (1−3u²)(16m⁵ + 8m⁴ r − 10m² r³ + 15m r⁴ + 15r⁵) + A₂(r)

H₂ = 8m r⁻¹ (5(1−3u²)(2m²−3m r−3r²)) − A₂(r)

A₂ = (15(r²−2m²)(3u²−1)/(16m²)) ln(r/(r−2m)). (6.2.56)

For j = q = 0 the Hartle-Thorne metric reduces to the Schwarzschild metric in standard coordinates. Abramowicz et al. (2003) have shown how to get the Kerr metric in Boyer-Lindquist coordinates (see below) to the corresponding accuracy.

The Hartle-Thorne metric can be used to describe the exterior gravitational field of rotating neutron stars. Bauböck et al. (2013) gave some empirical fitting for neutron-star parameters.

t parameters that appear in this metric.

6.2.3 Static Axially Symmetric Space-Times

A stationary space-time is called static, if the twist-vector ω = 0. In that case the space-like Killing vector field is called hypersurface orthogonal. A foliation of space-time into slices of space-like hypersurfaces is given by some scalar function S(x), x ∈ M, that serves as label; a certain space-like hypersurface is given by Σ = {x | S(x) = s = const.}.

A vector-field V is said to be hypersurface orthogonal, if it is proportional to the gradient of some scalar function S(x), i.e., if V_α = g(x) · S_,α. (6.2.57)

Then, V_[α;β] = g_,β S_,α - g_,α S_,β so that V_[α;β] is proportional to V_[μνλσ] V^ν;λ V^σ = 0.

Thus a stationary space-time is static if the timelike KVF (Killing vector field) is hypersurface orthogonal. The metric of a static axially symmetric space-time is conveniently written with canonical Weyl coordinates (ct, ρ, z, φ) with f = e^{2ψ} in the form ds^2 = -e^{2ψ} (cdt)^2 + e^{-2ψ} [e^{2γ} (dρ^2 + dz^2) + ρ^2 dφ^2]. (6.2.58)

We see that ρ, z are a kind of cylindrical coordinates, called Weyl cylindrical coordinates. The potential ψ obey the vacuum field equation ψ_{,ρρ} + ρ^{-1} ψ_{,ρ} + ψ_{,zz} = 0, (6.2.59)

which is nothing but the Laplace equation in flat space, ∇ψ = 0, in cylindrical coordinates with ∇ = ∂_{ρρ} + ρ^{-1} ∂_ρ + ∂_{zz}.

Taking W = 0 and f = -e^{2ψ} in Eqs.(6.2.31),(6.2.32), the potential γ = γ(ρ,z) is determined from the field equations γ_{,ρ} = ρ (ψ_{,ρ}^2 - ψ_{,z}^2) (6.2.60)

γ_{,z} = 2ρ ψ_{,ρ} ψ_{,z}. (6.2.61)

Again taking W = 0 and f = -e^{2ψ} in the metric (6.2.47), correspondingly in prolate spheroidal coordinates we have: ds^2 = -e^{2ψ} (cdt)^2 + σ^2 e^{-2ψ} [e^{2γ} (x^2 - y^2) (dx^2/(x^2-1) + dy^2/(1-y^2)) + (x^2-1)(1-y^2) dφ^2]. (6.2.62)

To get the Schwarzschild metric (see below) with x = r/m - 1 and y = cosθ in usual Schwarzschild coordinates we write σ = m. From Eq.(6.2.49), the field equation for ψ takes the form (e.g., Quevedo and Mashhoon 1985)

[(x^2-1) ψ_{,x}]_{,x} + [(1-y^2) ψ_{,y}]_{,y} = 0, (6.2.63)

which can be solved by separation of variables, ψ(x,y) = F(x) G(y), (6.2.64)

so that (6.2.63) reduces to the Legendre equations for F and G [(x^2-1) F_{,x}]_{,x} - ν(ν+1) F = 0, [(1-y^2) G_{,y}]_{,y} + ν(ν+1) G = 0, (6.2.65)

where ν is a constant. To avoid logarithmic singularities at y = ±1, ν must be an integer and since ψ = 0 for x → ∞ the solution for ψ takes the form ψ = ∑_{n=0}^{∞} (-1)^{n+1} q_n Q_n(x) P_n(y), (6.2.66)

where P_n(y) are Legendre-polynomials of the first kind and Q_n(x) are Legendre functions of the second kind for x ≥ 1 P_0(y) = 1 P_1(y) = y P_2(y) = (3y^2-1)/2 Q_0(x) = (1/2) ln((x+1)/(x-1))

Q_1(x) = (x/2) ln((x+1)/(x-1)) - 1 Q_2(x) = (1/4)(3x^2-1) ln((x+1)/(x-1)) - (3/2)x. (6.2.67)

The field equations for the potential γ read: γ_{,x} = (1-y^2)/(x^2-y^2) [x(x^2-1) ψ_{,x}^2 - x(1-y^2) ψ_{,y}^2 - 2y(x^2-1) ψ_{,x} ψ_{,y}], γ_{,y} = (x^2-1)/(x^2-y^2) [y(x^2-1) ψ_{,x}^2 - y(1-y^2) ψ_{,y}^2 + 2x(1-y^2) ψ_{,x} ψ_{,y}]. (6.2.68)

Exercise 6.7 Prove the above field equations for γ.

Solution Considering γ = γ_{,ρ} ρ_{,x} + γ_{,z} z_{,x}, γ = γ_{,ρ} ρ_{,y} + γ_{,z} z_{,y}, then use Eqs.(6.2.31),(6.2.32) and E_{,ρ} = (E_{,x} z_{,y} - E_{,y} z_{,x}) / (ρ_{,x} z_{,y} - ρ_{,y} z_{,x}), E_{,z} = (E_{,x} ρ_{,y} - E_{,y} ρ_{,x}) / (ρ_{,y} z_{,x} - ρ_{,x} z_{,y}) (6.2.69)

with E = f = e^{2ψ}, we can directly get the above field equations for γ in PS-coordinates.

Lemma 6.2 (Quevedo 1989) Let ψ be asymptotically flat, i.e., lim_{x→∞} ψ(x,y) = 0 and vanish on the symmetry axis, i.e., γ(x,±1) = 0, then γ(x,y) = (x^2-1) ∫_{-1}^{y} [A(x,y)/(x^2-y^2)] dy, (6.2.70)

with A(x,y) = y(x^2-1) ψ_{,x}^2 - y(1-y^2) ψ_{,y}^2 + 2x(1-y^2) ψ_{,x} ψ_{,y}. (6.2.71)

In Weyl spherical coordinates the general solution for ψ reads ψ = ∑_{l=0}^{∞} (a_l / r^{l+1}) P_l(cosθ). (6.2.72)

Where the (spherical) Weyl-moments a_l are constant numbers. Then the potential γ is given by γ = ∑_{l,k=0}^{∞} [(l+1)(k+1)/(l+k+2)] a_l a_k / r^{l+k+2} (P_{l+1} P_{k+1} - P_l P_k). (6.2.73)

Lemma 6.3 Lemma (Hernández-Pastora and Martin 1993)

The spherical and prolate spheroidal Weyl moments, a_n and q_n are related by; a_n = (-m)^{n+1} ∑_{j=0}^{T} [n! / ((n+k+1)!!(n-k)!!)] q_k (6.2.74)

with k = 2j and T = n/2 for even values of n and k = 2j + 1, T = (n-1)/2 for odd values of n.

If ψ has equatorial symmetry then it has only even Weyl moments, i.e., q_{2n+1} = a_{2n+1} = 0.

6.2.3.1 The Schwarzschild Metric

The simplest case for a static metric in prolate spheroidal coordinates is q_2 = 1 with (P_1(y) = y)

ψ = -Q_0(x) = -(1/2) ln((x+1)/(x-1)). (6.2.75)

The potential γ takes the form γ = (1/2) ln((x^2-1)/(x^2-y^2)). (6.2.76)

Taking ψ, γ in (6.2.62) and setting σ = m, so that the Schwarzschild metric in prolate spheroidal coordinates reads ds^2 = -[(x-1)/(x+1)] (cdt)^2 + m^2 [(x+1)/(x-1)] dx^2 + m^2 [(x^2-1)/(1-y^2)] dy^2 + m^2 (x^2-1)(1-y^2) dφ^2 (6.2.77)

or, using x = r/m - 1 and y = cosθ, ds^2 = -(1 - 2m/r) (cdt)^2 + (1 - 2m/r)^{-1} dr^2 + r^2 (dθ^2 + sin^2θ dφ^2). (6.2.78)

Such coordinates (ct, r, θ, φ) are called standard Schwarzschild coordinates. If we write m = GM/c^2 (6.2.79)

the parameter M will be identified with the (field) mass of Schwarzschild space-time.

The corresponding spherical Weyl moments read: a_{2n} = - m^{2n+1}. (6.2.80)

The Ernst-potential E in PS coordinates takes the form E = f = (x-1)/(x+1) = (l-m)/(l+m) = -g_{00} (6.2.81)

with l ≡ mx.

The ξ-potential reads ξ = (1+E)/(1-E) = x. (6.2.82)

With l_± = ρ^2 + (z ± m)^2 the Schwarzschild-metric in canonical Weyl coordinates (ct, ρ, z, φ) takes the form (l = r - m)

ds^2 = -[(l-m)/(l+m)] (cdt)^2 + [(l+m)/(l+r_-)] (dρ^2 + dz^2) + [(l+m)/(l-m)] ρ^2 dφ^2. (6.2.83)

The transformation to standard Schwarzschild-coordinates is obtained with ρ = √[r(r-2m)] sinθ; z = (r - m) cosθ (6.2.84)

so that l+m = r, l-m = r-2m and l_± = ±(m cosθ ± (r - m)). (6.2.85)

6.2.3.2 The Erez-Rosen Metric

The Erez-Rosen (ER) metric (Erez and Rosen 1959; Doroshkevich et al. 1966; Winicour et al. 1968; Young and Coulter 1969) is an extension of the Schwarzschild-metric by choosing q_0 = 1 and q_2 = q as non-vanishing PS Weyl moments. Then, ψ_ER = -Q_0(x) - q P_2(y) Q_2(x)

= -(1/2) ln((x+1)/(x-1)) - (q/2) (3y^2-1) [ (1/4)(3x^2-1) ln((x+1)/(x-1)) - (3/2)x ]. (6.2.86)

The corresponding potential γ takes the form (e.g., Bini et al. 2013 and references quoted therein)

γ_ER = (1/2)(1+q)^2 ln((x^2-1)/(x^2-y^2)) + 2q(1-P_2) Q_1 + q^2(1-P_2) · [(1+P_2)(Q_1^2 - Q_2^2)

+ (1/2)(x^2-1)(2Q_2^2 - 3x Q_1 Q_2 + 3Q_0 Q_2 - Q_2')], (6.2.87)

with P_n ≡ P_n(y), Q_n ≡ Q_n(x) and Q_2' ≡ dQ_2(x)/dx.

By relation (6.2.74) the spherical Weyl moments for the Erez-Rosen metric read: a_{2n} = - [m^{2n+1} / (2n+1)] [1 + q]. (6.2.88)

As we shall see later, the parameter q can be related with a quadrupole moment of the ER space-time.

Exercise 6.8 Store the ER metric in PS coordinates (ct, x, y, φ) in a file ER.mpl. Then write a little program using GRTensor to check that it solves the vacuum field equations R_{μν} = 0. Also check the field equations for the potential γ given the function ψ(x,y) (Fig. 6.2).

## 6.2 Stationary Space-Times

Ndim_ := 4: X1_ := x: X2_ := Y: X3_ := phi: X4_ := t: g11_ := m^2*exp(2*gammap-2*psi)*(x^2-y^2)/(x^2-1): g22_ := m^2*exp(2*gammap-2*psi)*(x^2-y^2)/(1-y^2): g33_ := m^2*exp(-2*psi)*(x^2-1)*(1-y^2): g44_ := -exp(2*psi): psi := - 1/2*ln((x+1)/(x-1)) - q*P2*Q2; gammap := 1/2*(1+q)^2*ln((x^2-1)/(x^2-y^2)) + 2*q*(1-P2)*Q1 + q^2*(1-P2)*((1+P2)*(Q1^2-Q2^2)

+ 1/2*(x^2-1)*(2*Q2^2 - 3*x*Q1*Q2 + 3*Q0*Q2 - Q2p)); P2 := 1/2*(3*y^2-1); Q0 := 1/2*ln((x+1)/(x-1)); Q1 := x/2*ln((x+1)/(x-1)) - 1; Q2 := 1/4*(3*x^2-1)*ln((x+1)/(x-1)) - 3/2*x; Q2p := 3/2*x*ln((x+1)/(x-1)) - 1/2*(3*x^2-1)/(x^2-1) - 3/2; Info_:=`Erez-Rosen metric in prolate spheroidal coordinates (x = r/m-1, y = cos(theta), phi,t)`: Fig. 6.2 A file ER.mpl for the Erez-Rosen metric

The file ER.mpl could look like this: The corresponding Maple file could read: > ####################################################### > ####################################################### > restart: > libname := libname, "D:\\Maple\\grtensor": > with(grtensor); > grOptionMetricPath := "D:\\Maple\\grtensor\\metrics": > qload( ER ): > psi; > gammap; > ########################################################### > # check the field equations for gammap > ########################################################### > px := diff(psi,x): > py := diff(psi,y): > Rx := (1-y^2)/(x^2-y^2)*(x*(x^2-1)*px^2 > - x*(1-y^2)*py^2-2*y*(x^2-1)*px*py): > difx := simplify(diff(gammap,x) - Rx); > Ry := (x^2-1)/(x^2-y^2)*(y*(x^2-1)*px^2 > - y*(1-y^2)*py^2+2*x*(1-y^2)*px*py): > dify := simplify(diff(gammap,y) - Ry); > ########################################################### > ########################################################### > # for q = 0 we get the Schwarzschild metric > ########################################################### > Gtt := grcomponent(g(dn,dn), [t,t]): > GStt := simplify(subs(q=0,x = r/m-1,y=cos(theta),Gtt)); > Gxx := grcomponent(g(dn,dn), [x,x]): > GSxx := simplify(subs(q=0,x = r/m-1,y=cos(theta),Gxx)); > Gyy := grcomponent(g(dn,dn), [y,y]): > GSyy := simplify(subs(q=0,x = r/m-1,y=cos(theta),Gyy)); > Gphiphi := grcomponent(g(dn,dn), [phi,phi]): > GSphiphi := simplify(subs(q=0,x = r/m-1,y=cos(theta),Gphiphi)); > ########################################################### > grcalc( R(dn,dn) ): > grdisplay( R(dn,dn) ): > ###########################################################

6.2.3.3 The Quevedo-Mashhoon M-Q-S Metric

The Quevedo-Mashhoon M-Q-S metric is a stationary axisymmetric solution of the vacuum field equations. It has three parameters: M (mass), Q (quadrupole-moment) and S (spin) and generalizes the Schwarzschild (Q=S=0), the Erez-Rosen (S=0) and the Kerr-metric (Q=0).

The QM M-Q-S spacetime in PS-coordinates (ct, x, y, φ) is of the form (6.2.47) with (Quevedo and Mash with a = S/(Mc) (α = 0 for a = 0), q = -Q/(M m^2) and m ≡ GM/c^2.

For q = 0, i.e., the Kerr geometry, the Ernst ξ potential from (6.2.89) reads: ξ = \frac{x(1 - α^2) + 2i α y}{K (1 + α^2)} (6.2.91)

and using (1 - α^2)/(1 + α^2) = σ/m and 2α/(1 + α^2) = -a/m we get ξ = \frac{σ x - i a y}{K}. (6.2.92)

In spherical Weyl coordinates (ct, r, θ, φ), the QM metric takes the form ds^2 = -f (c dt - W dφ)^2 + \frac{e^{2γ} dr^2}{[(r - m)^2 - (m^2 - a^2) cos^2 θ]} + dθ^2 + sin^2 θ dφ^2, (6.2.93)

where Δ = r^2 - 2mr + a^2 and the relation between PS and spherical Weyl coordinates are r = σ \sqrt{x^2 + y^2 - 1}, θ = x y / \sqrt{x^2 + y^2 - 1}.

The QM M-Q-S metric can be used to describe the exterior asymptotically flat gravitational field of a rotating body with an arbitrary quadrupole mass-moment; the Hartle-Thorne solution mentioned before is valid for the exterior field of a slowly rotating and slightly deformed object. Finally, we would like to mention that more general stationary and axisymmetric vacuum solutions have been derived that contain a set of infinitely many independent parameters q_n, describing relativistic mass multi-pole moments and a single parameter a related with the spin of the central 'body' (higher orders spin-moments are then uniquely determined by (q_n, a)). Examples are the generalized Quevedo-Mashhoon metric (1991) and the Manko-Novikov metric (1992).

Exercise 6.9 Show that the QM M-Q-S metric for vanishes quadrupole parameter q (the Kerr-metric) leads to f = -\frac{m^2 - σ^2 x^2 - a^2 y^2}{(σ x + m)^2 + a^2 y^2}, W = 2ma \frac{(σ x + m)(1 - y^2)}{σ^2 x^2 + a^2 y^2 - m^2}, (6.2.94)

e^{2γ} = \frac{σ^2 x^2 + a^2 y^2 - m^2}{σ^2 (x^2 - y^2)}.

From this show that in the Schwarzschild case q = a = 0 the QM M-Q-S metric yields: f = (1 - x)/(1 + x), W = 0 and exp(2γ) = (x^2 - 1)/(x^2 - y^2).

6.2.4 Spherically Symmetric Space-Time A spherically symmetric space-time is invariant under rotations so that coordinates x^μ = (ct, r, θ, φ) can be chosen in such a way that the metric on a constant t, constant r hypersurface takes the form dl^2 = r^2 (dθ^2 + sin^2 θ dφ^2) ≡ r^2 dΩ^2. (6.2.95)

The metric in adapted coordinates can be written in the form (e.g., Weinberg 1972; Misner et al. 1973)

ds^2 = -A(t, r) c^2 dt^2 + B(t, r) dr^2 + r^2 dΩ^2 (6.2.96)

that is often written in the form ds^2 = -e^{2Φ} c^2 dt^2 + e^{2Λ} dr^2 + r^2 dΩ^2, (6.2.97)

where Φ = Φ(t, r) and Λ = Λ(t, r). Corresponding Christoffel-symbols, components of the Riemann and Ricci-tensor can be found in Appendix. We now consider the vacuum field equations, R_{μν} = 0. The equation R_{tr,0} = (2/r) Λ_{,0} = 0 (6.2.98)

tells us that Λ is independent of t, Λ = Λ(r). Then, e^{2(Λ - Φ)} R_{tt} + R_{rr} = (2/r)(Φ_{,r} + Λ_{,r}) = 0 (6.2.99)

tells us that Φ + Λ is a function of t only: Φ + Λ = f(t). (6.2.100)

Then we can define a new time coordinate T by T = \int e^{f(t)} dt (6.2.101)

so that the metric takes the form ds^2 = -e^{-2Λ(r)} c^2 dT^2 + e^{2Λ(r)} dr^2 + r^2 dΩ^2. (6.2.102)

Finally the equation R_{θθ} = 0 leads to e^{-2Λ} = 1 - \frac{k}{r}, (6.2.103)

where k is an integration constant. If we put k = 2m we get the standard form of the Schwarzschild metric ds^2 = -\left(1 - \frac{2m}{r}\right) c^2 dt^2 + \left(1 - \frac{2m}{r}\right)^{-1} dr^2 + r^2 dΩ^2.

Thus we have proven Birkhoff's Theorem: Theorem 6.1 (Birkhoff's Theorem) A spherically symmetric vacuum space-time is necessarily locally isometric to the static Schwarzschild geometry.

This Theorem was first formulated by Jebson in 1921 and later proven by Birkhoff in 1923.

6.2.4.1 Harmonic Coordinates For important reasons the harmonic gauge plays an important role in many applications. A function f(x^μ) is called harmonic, if □ f ≡ \frac{1}{\sqrt{-g}} \partial_μ (\sqrt{-g} g^{μν} ∂_ν f) = 0. (6.2.104)

Note that in three-dimensional Euclidean space, R^3, the operator □ reduces to the usual Laplacian Δ. Harmonic coordinates x^μ satisfy the harmonicity condition □ x^μ = \partial_ν (\sqrt{-g} g^{μν}) = 0. (6.2.105)

Our standard Schwarzschild coordinates can be transformed into harmonic ones with a change of the radial coordinate (Klioner and Soffel (2005)). We will construct coordinates X^α = (ct, X, Y, Z) with X = R(r) sin θ cos φ, Y = R(r) sin θ sin φ, Z = R(r) cos θ (6.2.106)

so that they obey the harmonicity condition (6.2.105). For our static spherically symmetric metric in standard coordinates we have: g^{μν} ∂_μ ∂_ν = - \frac{1}{c^2 A} ∂_tt + \frac{1}{B} ∂_rr + \frac{1}{r^2} ∂_{θθ} + \frac{1}{r^2 sin^2 θ} ∂_{φφ} (6.2.107)

and g^{μν} Γ^λ_{μν} ∂_λ = - \frac{1}{2AB} ∂_r A + \frac{1}{2B^2} ∂_r B - \frac{1}{rB} ∂_r - \frac{cot θ}{r^2 B} ∂_θ. (6.2.108)

One immediately finds that the standard time-coordinate t is harmonic. For the spatial coordinates X^i we obtain g^{μν} ∂_μ ∂_ν X^i - g^{μν} Γ^λ_{μν} ∂_λ X^i = \frac{A}{BR} R_{,r} + \frac{2}{r} - R \left( \frac{1}{2A} R_{,r} + \frac{1}{2B} R_{,r} \right) - \frac{1}{R^2}, (6.2.109)

i.e., they are harmonic if \frac{A}{2A} R_{,r} + \frac{2}{r} - R \left( \frac{1}{2A} R_{,r} + \frac{1}{2B} R_{,r} \right) - \frac{1}{R^2} = 0 (6.2.110)

or equivalently (r^2 A^{1/2} B^{-1/2} R_{,r}) = 2 A^{1/2} B^{1/2} R. (6.2.111)

In these harmonic coordinates the metric takes the form ds^2 = -A c^2 dt^2 + \frac{r^2}{R^2} dX^2 + \left( \frac{r^2}{R^2} - \frac{r^2}{R^2 R_{,r}^2} \right) (X·dX)^2. (6.2.112)

To get the Schwarzschild metric

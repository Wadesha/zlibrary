# Modern Quantum Mechanics J J Sakurai Jim Napolitano Z Library

> 来源文件：pre_Modern_Quantum_Mechanics_J_J_Sakurai_Jim_Napolitano_Z_Library.txt
> 字符数（约）：245451
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Modern Quantum Mechanics

Modern Quantum Mechanics is a classic graduate level textbook, covering the main quantum mechanics concepts in a clear, organized, and engaging manner. The original author, J. J. Sakurai, was a renowned theorist in particle theory. The Third Edition, revised by Jim Napolitano, introduces topics that extend the text’s usefulness into the twenty-first century such as advanced mathematical techniques associated with quantum-mechanical calculations, while at the same time retaining classic developments such as neutron interferometer experiments, Feynman path integrals, correlation measurements, and Bell’s inequality. A solution manual for instructors using this textbook can be downloaded from www.cambridge.org/sakurai3.

J. J. Sakurai was a noted theorist in particle physics and Professor of Physics at UCLA (1970–1982) and University of Chicago (1964–1970). He received his Ph.D. from Cornell University in 1958. He contributed greatly to the field of particle physics before passing away at the age of 49 in 1982, while he was visiting CERN in Geneva.

In addition he held visiting staff appointments at the California Institute of Technology, Universities of Tokyo and Nagoya, University of Paris d’Orsay, Scuola Normale Superiore at Pisa, Stanford Linear Accelerator, CERN at Geneva, and Max Planck Institute at Munich. He was a Sloan Fellow (1962–1966), Fellow of the American Physical Society (1964–1982), a Guggenheim Fellow (1975–1976) and a von Humboldt Fellow (1981–1982).

Jim Napolitano is Professor of Physics and Department Chair at the College of Science and Technology, Temple University. He is an experimental nuclear physicist, with over 320 articles published in refereed journals and an h-index of 81. He shared in the 2016 Breakthrough Prize in Fundamental Physics and currently works on experiments using parity-violating electron scattering. An innovative educator, he has developed coursework and curricula at Rensselaer Polytechnic Institute and Temple University. In all cases, his teaching and instructional development make use of modern techniques. Professor Napolitano has also published textbooks on quantum mechanics, experimental physics, and using MATHEMATICA for physics.

Modern Quantum Mechanics Third Edition J. J. SAKURAI JIM NAPOLITANO Temple University, Philadelphia, PA

University Printing House, Cambridge CB2 8BS, United Kingdom One Liberty Plaza, 20th Floor, New York, NY 10006, USA 477 Williamstown Road, Port Melbourne, VIC 3207, Australia 314–321, 3rd Floor, Plot 3, Splendor Forum, Jasola District Centre, New Delhi – 110025, India 79 Anson Road, #06-04/06, Singapore 079906

Cambridge University Press is part of the University of Cambridge.

It furthers the University’s mission by disseminating knowledge in the pursuit of education, learning, and research at the highest international levels of excellence.

www.cambridge.org

Information on this title: www.cambridge.org/9781108473224 DOI: 10.1017/9781108587280 © Cambridge University Press 2021

This publication is in copyright. Subject to statutory exception and to the provisions of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published 2021 Printed in the United Kingdom by TJ International Ltd, Padstow Cornwall A catalogue record for this publication is available from the British Library.

ISBN 978-1-108-47322-4 Hardback

Additional resources for this publication at www.cambridge.org/sakurai3.

Cambridge University Press has no responsibility for the persistence or accuracy of URLs for external or third-party internet websites referred to in this publication and does not guarantee that any content on such websites is, or will remain, accurate or appropriate.

Contents

In Memoriam to J. J. Sakurai xix Foreword from the First Edition xxi

1 Fundamental Concepts 1

## 1.1 The Stern–Gerlach Experiment

1.1.1 Description of the Experiment 2 1.1.2 Sequential Stern–Gerlach Experiments 4 1.1.3 Analogy with Polarization of Light 6

## 1.2 Kets, Bras, and Operators

1.2.1 Ket Space 10 1.2.2 Bra Space and Inner Products 12 1.2.3 Operators 13 1.2.4 Multiplication 14 1.2.5 The Associative Axiom 15

## 1.3 Base Kets and Matrix Representations

1.3.1 Eigenkets of an Observable 16 1.3.2 Eigenkets as Base Kets 17 1.3.3 Matrix Representations 18 1.3.4 Spin ½ Systems 21

## 1.4 Measurements, Observables, and the Uncertainty Relations

1.4.1 Measurements 22 1.4.2 Spin ½ Systems, Once Again 24 1.4.3 Compatible Observables 27 1.4.4 Incompatible Observables 29 1.4.5 The Uncertainty Relation 31

## 1.5 Change of Basis

1.5.1 Transformation Operator 33 1.5.2 Transformation Matrix 34 1.5.3 Diagonalization 35 1.5.4 Unitary Equivalent Observables 36

## 1.6 Position, Momentum, and Translation

1.6.1 Continuous Spectra 37 1.6.2 Position Eigenkets and Position Measurements 38 1.6.3 Translation 40 1.6.4 Momentum as a Generator of Translation 42 1.6.5 The Canonical Commutation Relations 45

## 1.7 Wave Functions in Position and Momentum Space

1.7.1 Position-Space Wave Function 47 1.7.2 Momentum Operator in the Position Basis 49 1.7.3 Momentum-Space Wave Function 49 1.7.4 Gaussian Wave Packets 51 1.7.5 Generalization to Three Dimensions 53 Problems 54

2 Quantum Dynamics 62

## 2.1 Time Evolution and the Schrödinger Equation

2.1.1 Time-Evolution Operator 62 2.1.2 The Schrödinger Equation 65 2.1.3 Energy Eigenkets 67 2.1.4 Time Dependence of Expectation Values 68 2.1.5 Spin Precession 69 2.1.6 Neutrino Oscillations 71 2.1.7 Correlation Amplitude and the Energy-Time Uncertainty Relation 74

## 2.2 The Schrödinger Versus the Heisenberg Picture

2.2.1 Unitary Operators 75 2.2.2 State Kets and Observables in the Schrödinger and the Heisenberg Pictures 77 2.2.3 The Heisenberg Equation of Motion 78 2.2.4 Free Particles: Ehrenfest’s Theorem 79 2.2.5 Base Kets and Transition Amplitudes 81

## 2.3 Simple Harmonic Oscillator

2.3.1 Energy Eigenkets and Energy Eigenvalues 83 2.3.2 Time Development of the Oscillator 88

## 2.4 Schrödinger’s Wave Equation

2.4.1 Time-Dependent Wave Equation 91 2.4.2 The Time-Independent Wave Equation 92 2.4.3 Interpretations of the Wave Function 94 2.4.4 The Classical Limit 96

## 2.5 Elementary Solutions to Schrödinger’s Wave Equation

2.5.1 Free Particle in Three Dimensions 97 2.5.2 The Simple Harmonic Oscillator 99 2.5.3 The Linear Potential 101 2.5.4 The WKB (Semiclassical) Approximation 104

## 2.6 Propagators and Feynman Path Integrals

2.6.1 Propagators in Wave Mechanics 108 2.6.2 Propagator as a Transition Amplitude 112 2.6.3 Path Integrals as the Sum over Paths 114 2.6.4 Feynman’s Formulation 115

## 2.7 Potentials and Gauge Transformations

2.7.1 Constant Potentials 120 2.7.2 Gravity in Quantum Mechanics 122 2.7.3 Gauge Transformations in Electromagnetism 126 2.7.4 The Aharonov–Bohm Effect 131 2.7.5 Magnetic Monopole 135 Problems 138

3 Theory of Angular Momentum 149

## 3.1 Rotations and Angular Momentum Commutation Relations

3.1.1 Finite Versus Infinitesimal Rotations 149 3.1.2 Infinitesimal Rotations in Quantum Mechanics 152 3.1.3 Finite Rotations in Quantum Mechanics 153 3.1.4 Commutation Relations for Angular Momentum 154

## 3.2 Spin ½ Systems and Finite Rotations

3.2.1 Rotation Operator for Spin ½ 155 3.2.2 Spin Precession Revisited 157 3.2.3 Neutron Interferometry Experiment to Study 2π Rotations 158 3.2.4 Pauli Two-Component Formalism 159 3.2.5 Rotations in the Two-Component Formalism 161

## 3.3 SO(3), SU(2), and Euler Rotations

3.3.1 Orthogonal Group 163 3.3.2 Unitary Unimodular Group 164 3.3.3 Euler Rotations 166

## 3.4 Density Operators and Pure Versus Mixed Ensembles

3.4.1 Polarized Versus Unpolarized Beams 169 3.4.2 Ensemble Averages and Density Operator 170 3.4.3 Time Evolution of Ensembles 175 3.4.4 Continuum Generalizations 176 3.4.5 Quantum Statistical Mechanics 176

## 3.5 Eigenvalues and Eigenstates of Angular Momentum

3.5.1 Commutation Relations and the Ladder Operators 180 3.5.2 Eigenvalues of J² and Jz 182 3.5.3 Matrix Elements of Angular-Momentum Operators 184 3.5.4 Representations of the Rotation Operator 185

## 3.6 Orbital Angular Momentum

3.6.1 Orbital Angular Momentum as Rotation Generator 188 3.6.2 Spherical Harmonics 191 3.6.3 Spherical Harmonics as Rotation Matrices 194

## 3.7 Schrödinger’s Equation for Central Potentials

3.7.1 The Radial Equation 196 3.7.2 The Free Particle and Infinite Spherical Well 198 3.7.3 The Isotropic Harmonic Oscillator 199 3.7.4 The Coulomb Potential 201

## 3.8 Addition of Angular Momenta

3.8.1 Simple Examples of Angular-Momentum Addition 205 3.8.2 Formal Theory of Angular-Momentum Addition 208 3.8.3 Recursion Relations for the Clebsch–Gordan Coefficients 212 3.8.4 Clebsch–Gordan Coefficients and Rotation Matrices 216

## 3.9 Schwinger’s Oscillator Model of Angular Momentum

3.9.1 Angular Momentum and Uncoupled Oscillators 218 3.9.2 Explicit Formula for Rotation Matrices 222

## 3.10 Spin Correlation Measurements and Bell’s Inequality

3.10.1 Correlations in Spin-Singlet States 224 3.10.2 Einstein’s Locality Principle and Bell’s Inequality 226 3.10.3 Quantum Mechanics and Bell’s Inequality 229

## 3.11 Tensor Operators

3.11.1 Vector Operator 231 3.11.2 Cartesian Tensors Versus Irreducible Tensors 3.11.3 Product of Tensors 3.11.4 Matrix Elements of Tensor Operators; the Wigner–Eckart Theorem Problems

4 Symmetry in Quantum Mechanics

## 4.1 Symmetries, Conservation Laws, and Degeneracies

4.1.1 Symmetries in Classical Physics 4.1.2 Symmetry in Quantum Mechanics 4.1.3 Degeneracies 4.1.4 SO(4) Symmetry in the Coulomb Potential

## 4.2 Discrete Symmetries, Parity, or Space Inversion

4.2.1 Wave Functions under Parity 4.2.2 Symmetrical Double-Well Potential 4.2.3 Parity-Selection Rule 4.2.4 Parity Nonconservation

## 4.3 Lattice Translation as a Discrete Symmetry

## 4.4 The Time-Reversal Discrete Symmetry

4.4.1 Digression on Symmetry Operations 4.4.2 Time-Reversal Operator 4.4.3 Wave Function 4.4.4 Time Reversal for a Spin 1 System 4.4.5 Interactions with Electric and Magnetic Fields; Kramers Degeneracy Problems

5 Approximation Methods

## 5.1 Time-Independent Perturbation Theory: Nondegenerate Case

5.1.1 Statement of the Problem 5.1.2 The Two-State Problem 5.1.3 Formal Development of Perturbation Expansion 5.1.4 Wave Function Renormalization 5.1.5 Elementary Examples

## 5.2 Time-Independent Perturbation Theory: The Degenerate Case

5.2.1 Linear Stark Effect

## 5.3 Hydrogenlike Atoms: Fine Structure and the Zeeman Effect

5.3.1 The Relativistic Correction to the Kinetic Energy 5.3.2 Spin-Orbit Interaction and Fine Structure 5.3.3 The Zeeman Effect 5.3.4 Vander Waals’ Interaction

## 5.4 Variational Methods

## 5.5 Time-Dependent Potentials: The Interaction Picture

5.5.1 Statement of the Problem 5.5.2 The Interaction Picture 5.5.3 Time-Dependent Two-State Problems: Nuclear Magnetic Resonance, Masers, and So Forth 5.5.4 Spin Magnetic Resonance 5.5.5 Maser

## 5.6 Hamiltonians with Extreme Time Dependence

5.6.1 Sudden Approximation 5.6.2 Adiabatic Approximation 5.6.3 Berry’s Phase 5.6.4 Example: Berry’s Phase for Spin 1 5.6.5 Aharonov–Bohm and Magnetic Monopoles Revisited

## 5.7 Time-Dependent Perturbation Theory

5.7.1 Dyson Series 5.7.2 Transition Probability 5.7.3 Constant Perturbation 5.7.4 Harmonic Perturbation

## 5.8 Applications to Interactions with the Classical Radiation Field

5.8.1 Absorption and Stimulated Emission 5.8.2 Electric Dipole Approximation 5.8.3 Photoelectric Effect 5.8.4 Spontaneous Emission

## 5.9 Energy Shift and Decay Width

Problems

6 Scattering Theory

## 6.1 Scattering as a Time-Dependent Perturbation

6.1.1 Transition Rates and Cross Sections 6.1.2 Solving for the T Matrix 6.1.3 Scattering from the Future to the Past

## 6.2 The Scattering Amplitude

6.2.1 Wave Packet Description 6.2.2 The Optical Theorem

## 6.3 The Born Approximation

6.3.1 The Higher-Order Born Approximation

## 6.4 Phase Shifts and Partial Waves

6.4.1 Free-Particle States 6.4.2 Partial-Wave Expansion 6.4.3 Unitarity and Phase Shifts 6.4.4 Determination of Phase Shifts 6.4.5 Hard-Sphere Scattering

## 6.5 Eikonal Approximation

6.5.1 Partial Waves and the Eikonal Approximation

## 6.6 Low-Energy Scattering and Bound States

6.6.1 Rectangular Well or Barrier 6.6.2 Zero-Energy Scattering and Bound States 6.6.3 Bound States as Poles of S(k)

## 6.7 Resonance Scattering

## 6.8 Symmetry Considerations in Scattering

## 6.9 Inelastic Electron-Atom Scattering

6.9.1 Nuclear Form Factor Problems

7 Identical Particles

## 7.1 Permutation Symmetry

## 7.2 Symmetrization Postulate

## 7.3 Two-Electron System

## 7.4 The Helium Atom

## 7.5 Multiparticle States

## 7.6 Density Functional Theory

7.6.1 The Energy Functional for a Single Particle 7.6.2 The Hohenberg–Kohn Theorem 7.6.3 The Kohn–Sham Equations 7.6.4 Models of the Exchange-Correlation Energy 7.6.5 Application to the Helium Atom

## 7.7 Quantum Fields

7.7.1 Second Quantization 7.7.2 Dynamical Variables in Second Quantization 7.7.3 Example: The Degenerate Electron Gas

## 7.8 Quantization of the Electromagnetic Field

7.8.1 Maxwell’s Equations in Free Space 7.8.2 Photons and Energy Quantization 7.8.3 The Casimir Effect 7.8.4 Concluding Remarks Problems

8 Relativistic Quantum Mechanics

## 8.1 Paths to Relativistic Quantum Mechanics

8.1.1 Natural Units 8.1.2 The Energy of a Free Relativistic Particle 8.1.3 The Klein–Gordon Equation 8.1.4 An Interpretation of Negative Energies 8.1.5 The Klein–Gordon Field 8.1.6 Summary: The Klein–Gordon Equation and the Scalar Field

## 8.2 The Dirac Equation

8.2.1 The Conserved Current 8.2.2 Free-Particle Solutions 8.2.3 Interpretation of Negative Energies 8.2.4 Electromagnetic Interactions

## 8.3 Symmetries of the Dirac Equation

8.3.1 Angular Momentum 8.3.2 Parity 8.3.3 Charge Conjugation 8.3.4 Time Reversal 8.3.5 CPT

## 8.4 Solving with a Central Potential

8.4.1 The One-Electron Atom

## 8.5 Relativistic Quantum Field Theory

Problems

## Appendix A Electromagnetic Units

## Appendix B Elementary Solutions to Schrödinger’s Wave Equation

## Appendix C Hamiltonian for a Charge in an Electromagnetic Field

## Appendix D Proof of the Angular-Momentum Rule (3.358)

## Appendix E Finding Clebsch–Gordan Coefficients

## Appendix F Notes on Complex Variables

Bibliography Index

Preface This book covers the material on quantum mechanics typically found in a first year graduate physics curriculum. The approach emphasizes states, operators, eigenvalues, and representations from the start. Building on these foundations, the reader sees, for example, how the Schrödinger representation is just one of several ways to realize quantum dynamics, and how classical physics emerges as an approximation. This approach also helps the reader gain an appreciation of purely quantum-mechanical phenomena, for example the magnetic moment and spin of an electron, that have no classical analogue.

The intended audience is the same as for earlier editions, that is, students having taken upper level undergraduate coursework in quantum physics, classical mechanics and electromagnetism, multivariable calculus, and ordinary and partial differential equations.

Professor Jun John Sakurai originally conceived the idea for this textbook, I think inspired by Dirac’s monograph. Sakurai’s life was cut short suddenly, as he was preparing the first manuscript. His colleague San Fu Tuan took over as Editor, completing a seven chapter manuscript for Addison-Wesley, who published the First Edition in 1985 and a Revised Edition in 1993. Some time later, I started work on the Second Edition for Pearson (who had since acquired Addison-Wesley). This volume contained a lot of new material, including an eighth chapter, and was published in 2010. The text was reissued by Cambridge University Press in 2017, which was also when I started work on the Third Edition.

Quantum mechanics has always fascinated me, but it was the First Edition of Modern Quantum Mechanics that finally explained to me the logical progression from fundamental assumptions to practical applications, with classical physics emerging as an approximation. When I first taught this material at Rensselaer Polytechnic Institute, I used the Revised Edition, but found myself supplementing with my own notes on solutions of the Schrödinger equation and other topics. I also tried to use my course to prepare students for quantum field theory, introducing second quantization and relativistic quantum mechanics, neither of which were included in Sakurai’s book.

I was therefore pleased to be asked to take on the Second Edition. Sections were added to Chapters Two and Three on solutions to the Schrödinger equation. I reversed the order of Chapters Six and Seven, so that Scattering Theory came first, and I reworked the treatment so that it was based on the formal theory of time-dependent perturbations. The following chapter on Identical Particles was augmented to include second quantization and the quantization of the free electromagnetic field, and I added a new chapter on Relativistic Quantum Mechanics. I also included several connections throughout the book to experimental measurements, and worked to fix a number of idiosyncrasies that I found when I taught out of the book.

The result was a text that, I thought, achieved my goal of a high level treatment respecting Sakurai’s vision, adding reference to additional modern concepts and experiment, and preparing the reader for quantum field theory and beyond. The first two chapters lay the mathematical and physical foundations for the rest of the book, and connect the reader to undergraduate topics in wave mechanics. Chapter Three covers angular momentum from the perspective of the rotation operator, with strong connections to important concepts such as the density operator, central potentials, and Bell’s inequality. Groups are also introduced here, with further exposition in Chapter Four. Applications to “real world” problems are the focus of Chapters Five and Six, all the while keeping to the focus of building on the fundamentals. Chapters Seven and Eight move the discussion towards the “next” course in quantum mechanics, covering many-body formalism and the inclusion of special relativity.

The Third Edition keeps the same ordering of the eight chapters. Significant new material has been added, but I also worked to clarify some of the discussions and to fix various issues that I discovered after teaching out of the Second Edition. In fact, I compiled a long list of “Typographical Errors, Mistakes, and Comments” based on covering nearly the entire book in class, and working through all of the end-of-chapter problems. The Third Edition addresses all of the errors. It also addresses most of the comments.

having to give up upon some only for lack of time.

There are three new sections of new material. Despite its increasing use in condensed matter physics, I found no treatments of density functional theory in any quantum mechanics textbook. So, I added Section 7.6 to introduce the subject and take it through to its application in the helium atom. A reviewer’s suggestion inspired me to add Section 8.1.5 to show how the Klein–Gordon field, built using second quantization, fixes the problems of negative energies and nonpositive definite probability currents in the Klein–Gordon wave equation. The Second Edition treated spontaneous emission only as an end-of-chapter problem, but Section 5.8.4 now goes through the derivation, with some details and numerical calculations left as problems.

I added new appendices on the Hamiltonian for a Charge in an Electromagnetic Field, Notes on Complex Analysis, and Calculating Clebsch–Gordan Coefficients. The appendix on Electromagnetic Units has been significantly revised, and I updated the appendix on Elementary Solutions to Schrödinger’s Wave Equation to better connect to the discussions in the text.

Instructors may elect to pick and choose from topics in the book, and not necessarily in the order of presentation. Chapter One should be covered first, since it lays down the notation and fundamental assumptions. One could then, for example, take parts of Chapters Three and Four to expand on operators, observables, and symmetries, prior to discussing dynamics in Chapter Two. Many other combinations are possible. Indeed, throughout the book, I have tried to refer to other places in the text where relevant related material is covered or discussed.

As befits a graduate level textbook, the strategy here is to lay down the principles, following up with implications by deduction. Some example calculations are carried through in the text, but the end-of-chapter problems are generally meant to extend the discussion, and not simply practice what was covered. As such, I recommend that instructors choose problems, from the text or otherwise, that follow this idea, including connection to experimental measurements, where practical.

In several places in the book, either explicitly or implicitly, computer calculations are necessary to completely follow the arguments or to work the problems. I worked through these using MATHEMATICA, and am happy to share the code with anyone who would like to see it, but any other programming language or application can also be used, of course.

Producing the Second Edition was a long process that would not have been possible without help from many, many people. Colleagues in physics include John Cummings, Jack Fishburn, Joel Giedt, David Hertzog, Barry Holstein, Bob Jaffe, Matthew Kirby, Joe Levinger, Alan Litke, Kam-Biu Luk, Bob McKeown, Harry Nelson, Joe Paki, Murray Peshkin, Olivier Pfister, Mike Snow, John Townsend, San Fu Tuan, David Van Baak, Dirk Walecka, and Tony Zee. The people at Addison-Wesley/Pearson who guided me included Adam Black, Ashley Eklund, Deb Greco, Dyan Menezes, John Rogosich, and Jim Smith. So many others were very helpful to me as I developed the Third Edition. This includes colleagues Kieron Burke, Mark Caprio, Carl Carlson, Benjamin Chandran, Chris Cocuzza, Martha Constantinou, Patrick Fasano, Jeremias Gonzalez, Aaron Kaplan (with special thanks for helping me learn DFT), Toh-Ming Lu, Carl Maes, Andreas Metz, Jerry Miller, Djordje Minic, Adilson Motter, Nick Murphy, Steve Naculich, Celso Nishi, John Perdew, Jon Rosner, and Roland Winkler. I am forever grateful to Simon Capelin at Cambridge University Press, for first bringing to me the possibility of republishing the Second Edition, and encouraging me to consider a Third Edition. Other key people at CUP include Jane Adams, Nick Gibbons, Lisa Pinto, and Ilaria Tassistro.

I can only offer my sincere apologies to people I should have listed, but whose name doesn’t appear because I’ve been careless with notekeeping. There are also the very many people who, over the past several years, offered comments, some of which I’ve not been able to incorporate.

Finally, I give a special acknowledgement for Stuart Freedman, my mentor, colleague, and friend. Stuart’s Ph.D. thesis experiment was the first verification of the violation of Bell’s inequality, and he used this to stoke my interest in quantum mechanics. His guidance during my years as a graduate student and young scientist shaped my career, and he remained my friend and counselor until his untimely passing.

Jim Napolitano Philadelphia, PA

Preface to the Revised First Edition

Since 1989 the Editor has enthusiastically pursued a revised edition of Modern Quantum Mechanics by his late great friend J. J. Sakurai, in order to extend this text’s usefulness into the twenty-first century. Much consultation took place with the panel of Sakurai friends who helped with the original edition, but in particular with Professor Yasuo Hara of Tsukuba University and Professor Akio Sakurai of Kyoto Sangyo University in Japan.

This book is intended for the first year graduate student who has studied quantum mechanics at the junior or senior level. It does not provide an introduction to quantum mechanics for the beginner. The reader should have had some experience in solving time-dependent and time-independent wave equations. A familiarity with the time evolution of the Gaussian wave packet in a force-free region is assumed, as is the ability to solve one-dimensional transmission-reflection problems. Some of the general properties of the energy eigenfunctions and the energy eigenvalues should also be known to the student who uses this text.

The major motivation for this project is to revise the main text. There are three important additions and/or changes to the revised edition, which otherwise preserves the original version unchanged. These include a reworking of certain portions of Section 5.2 on time-independent perturbation theory for the degenerate case by Professor Kenneth Johnson of M.I.T., taking into account a subtle point that has not been properly treated by a number of texts on quantum mechanics in this country. Professor Roger Newton of Indiana University contributed refinements on lifetime broadening in Stark effect, additional explanations of phase shifts at resonances, the optical theorem, and on non-normalizable state. These appear as “remarks by the editor” or “editor’s note” in the revised edition. Professor Thomas Fulton of the Johns Hopkins University reworked his Coulomb Scattering contribution (Section 7.13) so that it now appears as a shorter text portion emphasizing the physics, with the mathematical details relegated to Appendix C.

Though not a major part of the text, some additions were deemed necessary to take into account developments in quantum mechanics that have become prominent since November 1, 1982. To this end, two supplements are included at the end of the text. Supplement I is on adiabatic change and geometrical phase (popularized by M. V. Berry since 1983) and is actually an English translation of the supplement on this subject written by Professor Akio Sakurai for the Japanese version of Modern Quantum Mechanics (copyright © Yoshioka-Shoten Publishing of Kyoto). Supplement II is on non-exponential decays written by my colleague here, Professor Xerxes Tata, and read over by Professor E. C. G. Sudarshan of the University of Texas at Austin. Though non-exponential decays have a long history theoretically, experimental work on transition rates that tests indirectly such decays was done only in 1990. Introduction of additional material is of course a subjective matter on the part of the Editor; the readers will evaluate for themselves its appropriateness. Thanks to Professor Akio Sakurai, the revised edition has been “finely tooth combed” for misprint errors of the first ten printings of the original edition. My colleague, Professor Sandip Pakvasa, provided overall guidance and encouragement to me throughout this process of revision.

In addition to the acknowledgments above, my former students Li Ping, Shi Xiaohong, and Yasunaga Suzuki provided the sounding board for ideas on the revised edition when taking my graduate quantum mechanics course at the University of Hawaii during the spring of 1992. Suzuki provided the initial translation from Japanese of Supplement I as a course term paper. Dr. Andy Acker provided me with computer graphic assistance. The Department of Physics and Astronomy and particularly the High Energy Physics Group of the University of Hawaii at Manoa provided again both the facilities and a conducive atmosphere for me to carry out my editorial task. Finally I wish to express my gratitude to Physics (and sponsoring) Senior Editor, Stuart Johnson, and his Editorial Assistant, Jennifer Duggan, as well as Senior Production Coordinator Amy Willcutt, of Addison-Wesley for their encouragement and optimism that the revised edition will indeed materialize.

San Fu TUAN Honolulu, Hawaii

In Memoriam to J.J. Sakurai

Jun John Sakurai was born in 1933 in Tokyo and came to the United States as a high school student in 1949. He studied at Harvard and at Cornell, where he received his Ph.D. in 1958. He was then appointed assistant professor of Physics at the University of Chicago, and became a full professor in 1964. He stayed at Chicago until 1970 when he moved to the University of California at Los Angeles, where he remained until his death. During his lifetime he wrote 119 articles in theoretical physics of elementary particles as well as several books and monographs on both quantum and particle theory.

The discipline of theoretical physics has as its principal aim the formulation of theoretical descriptions of the physical world that are at once concise and comprehensive. Because nature is subtle and complex, the pursuit of theoretical physics requires bold and enthusiastic ventures to the frontiers of newly discovered phenomena. This is an area in which Sakurai reigned supreme with his uncanny physical insight and intuition and also his ability to explain these phenomena in illuminating physical terms to the unsophisticated. One has but to read his very lucid textbooks on Invariance Principles and Elementary Particles and Advanced Quantum Mechanics as well as his reviews and summer school lectures to appreciate this. Without exaggeration I could say that much of what I did understand in particle physics came from these and from his Articles and private tutoring.

When Sakurai was still a graduate student, he proposed what is now known as the V-A theory of weak interactions, independently of (and simultaneously with) Richard Feynman, Murray Gell-Mann, Robert Marshak, and George Sudarshan. In 1960 he published in Annals of Physics a prophetic paper, probably his single most important one. It was concerned with the first serious attempt to construct a theory of strong interactions based on Abelian and non-Abelian (Yang–Mills) gauge invariance. This seminal work induced theorists to attempt an understanding of the mechanisms of mass generation for gauge (vector) fields, now realized as the Higgs mechanism. Above all it stimulated the search for a realistic unification of forces under the gauge principle, now crowned with success in the celebrated Glashow–Weinberg–Salam unification of weak and electromagnetic forces.

On the phenomenological side, Sakurai pursued and vigorously advocated the vector mesons dominance model of hadron dynamics. He was the first to discuss the mixing of ω and φ meson states. Indeed, he made numerous important contributions to particle physics phenomenology in a much more general sense, as his heart was always close to experimental activities.

I knew Jun John for more than 25 years, and I had the greatest admiration not only for his immense powers as a theoretical physicist but also for the warmth and generosity of his spirit. Though a graduate student himself at Cornell during 1957–1958, he took time from his own pioneering research in K-nucleon dispersion relations to help me (via extensive correspondence) with my Ph.D. thesis on the same subject at Berkeley. Both Sandip Pakvasa and I were privileged to be associated with one of his last papers on weak couplings of heavy quarks, which displayed once more his infectious and intuitive style of doing physics. It is of course gratifying to us in retrospect that Jun John counted this paper among the score of his published works that he particularly enjoyed.

The physics community suffered a great loss at Jun John Sakurai's death. The personal sense of loss is a severe one for me. Hence I am profoundly thankful for the opportunity to edit and complete his manuscript on Modern Quantum Mechanics for publication. In my faith no greater gift can be given me than an opportunity to show my respect and love for Jun John through meaningful service.

San Fu Tuan

Foreword from the First Edition J. J. Sakurai was always a very welcome guest here at CERN, for he was one of those rare theorists to whom the experimental facts are even more interesting than the theoretical game itself. Nevertheless, he delighted in theoretical physics and in its teaching, a subject on which he held strong opinions. He thought that much theoretical physics teaching was both too narrow and too remote from application: "...we see a number of sophisticated, yet uneducated, theoreticians who are conversant in the LSZ formalism of the Heisenberg field operators, but do not know why an excited atom radiates, or are ignorant of the quantum theoretic derivation of Rayleigh's law that accounts for the blueness of the sky." And he insisted that the student must be able to use what has been taught: "The reader who has read the book but cannot do the exercises has learned nothing."

He put these principles to work in his fine book Advanced Quantum Mechanics (1967) and in Invariance Principles and Elementary Particles (1964), both of which have been very much used in the CERN library. This new book, Modern Quantum Mechanics, should be used even more, by a larger and less specialized group. The book combines breadth of interest with a thorough practicality. Its readers will find here what they need to know, with a sustained and successful effort to make it intelligible.

J. J. Sakurai's sudden death on November 1, 1982 left this book unfinished. Reinhold Bertlmann and I helped Mrs. Sakurai sort out her husband's papers at CERN. Among them we found a rough, handwritten version of most of the book and a large collection of exercises. Though only three chapters had been completely finished, it was clear that the bulk of the creative work had been done. It was also clear that much work remained to fill in gaps, polish the writing, and put the manuscript in order.

That the book is now finished is due to the determination of Noriko Sakurai and the dedication of San Fu Tuan. Upon her husband's death, Mrs. Sakurai resolved immediately that his last effort should not go to waste. With great courage and dignity she became the driving force behind the project, overcoming all obstacles and setting the high standards to be maintained. San Fu Tuan willingly gave his time and energy to the editing and completion of Sakurai's work. Perhaps only others close to the hectic field of high-energy theoretical physics can fully appreciate the sacrifice involved.

For me personally, J. J. had long been far more than just a particularly distinguished colleague. It saddens me that we will never again laugh together at physics and physicists and life in general, and that he will not see the success of his last work. But I am happy that it has been brought to fruition.

John S. Bell CERN, Geneva

1 Fundamental Concepts The revolutionary change in our understanding of microscopic phenomena that took place during the first 27 years of the twentieth century is unprecedented in the history of natural sciences. Not only did we witness severe limitations in the validity of classical physics, but we found the alternative theory that replaced the classical physical theories to be far richer in scope and far richer in its range of applicability.

The most traditional way to begin a study of quantum mechanics is to follow the historical developments – Planck's radiation law, the Einstein–Debye theory of specific heats, the Bohr atom, de Broglie's matter waves, and so forth – together with careful analyses of some key experiments such as the Compton effect, the Franck–Hertz experiment, and the Davisson–Germer–Thompson experiment. In that way we may come to appreciate how the physicists in the first quarter of the twentieth century were forced to abandon, little by little, the cherished concepts of classical physics and how, despite earlier false starts and wrong turns, the great masters – Heisenberg, Schrödinger, and Dirac, among others – finally succeeded in formulating quantum mechanics as we know it today.

However, we do not follow the historical approach in this book. Instead, we start with an example that illustrates, perhaps more than any other example, the inadequacy of classical concepts in a fundamental way. We hope that by exposing the reader to a "shock treatment" at the onset, he or she may be attuned to what we might call the "

∂z z ∂z where we have ignored the components of B in directions other than the z-direction. Because the atom as a whole is very heavy, we expect that the classical concept of trajectory can be legitimately applied, a point which can be justified using the Heisenberg uncertainty principle to be derived later. With the arrangement of Figure 1.1, the μ > 0 (S < 0) atom experiences an upward force, while the μ < 0 (S > 0) atom experiences a downward force. The beam is then expected to be split according to the values of μ_z. In other words, the SG (Stern–Gerlach) apparatus “measures” the z-component of μ or, equivalently, the z-component of S up to a proportionality factor.

The atoms in the oven are randomly oriented; there is no preferred direction for the orientation of μ. If the electron were like a classical spinning object, we would expect all values of μ_z to be realized between |μ| and −|μ|. This would lead us to expect a continuous bundle of beams coming out of the SG apparatus, as indicated in Figure 1.1, spread more or less evenly over the expected range. Instead, what we experimentally observe is more like the situation also shown in Figure 1.1, where two “spots” are observed, corresponding to one “up” and one “down” orientation. In other words, the SG apparatus splits the original silver beam from the oven into two distinct components, a phenomenon referred to in the early days of quantum theory as “space quantization.” To the extent that μ can be identified within a proportionality factor with the electron spin S, only two possible values of the z-component of S are observed to be possible, S up and S down, which we call S + and S −. The two possible values of S_z are multiples of some fundamental unit of angular momentum; numerically it turns out that S_z = ℏ/2 and −ℏ/2, where ℏ = 1.0546 × 10^{-27} erg-s = 6.5822 × 10^{-16} eV-s. (1.3) This “quantization” of the electron spin angular momentum^{3} is the first important feature we deduce from the Stern–Gerlach experiment.

^{3} An understanding of the roots of this quantization lies in the application of relativity to quantum mechanics. See Section 8.2 of this book for a discussion.

Figure 1.2a shows the result one would have expected from the experiment. According to classical physics, the beam should have spread itself over a vertical distance corresponding to the (continuous) range of orientation of the magnetic moment. Instead, one observes Figure 1.2b which is completely at odds with classical physics. The beam mysteriously splits itself into two parts, one corresponding to spin “up” and the other to spin “down.”

Of course, there is nothing sacred about the up-down direction or the z-axis. We could just as well have applied an inhomogeneous field in a horizontal direction, say in the x-direction, with the beam proceeding in the y-direction. In this manner we could have separated the beam from the oven into an S_x^+ component and an S_x^− component.

1.1.2 Sequential Stern–Gerlach Experiments

Let us now consider a sequential Stern–Gerlach experiment. By this we mean that the atomic beam goes through two or more SG apparatuses in sequence. The first arrangement we consider is relatively straightforward. We subject the beam coming out of the oven to the arrangement shown in Figure 1.3a, where SG_z stands for an apparatus with the inhomogeneous magnetic field in the z-direction, as usual. We then block the S_z^− component coming out of the first SG_z apparatus and let the remaining S_z^+ component be subjected to another SG_z apparatus. This time there is only one beam component coming out of the second apparatus, just the S_z^+ component. This is perhaps not so surprising; after all if the atom spins are up, they are expected to remain so, short of any external field that rotates the spins between the first and the second SG_z apparatuses.

A little more interesting is the arrangement shown in Figure 1.3b. Here the first SG apparatus is the same as before but the second one (SG_x) has an inhomogeneous magnetic field in the x-direction. The S_z^+ beam that enters the second apparatus (SG_x) is now split into two components, an S_x^+ component and an S_x^− component, with equal intensities. How can we explain this? Does it mean that 50% of the atoms in the S_z^+ beam coming out of the first apparatus (SG_z) are made up of atoms characterized by both S_z^+ and S_x^+, while the remaining 50% have both S_z^+ and S_x^−? It turns out that such a picture runs into difficulty, as will be shown below.

We now consider a third step, the arrangement shown in Figure 1.3c, which most dramatically illustrates the peculiarities of quantum-mechanical systems. This time we add to the arrangement of Figure 1.3b yet a third apparatus, of the SG_z type. It is observed experimentally that two components emerge from the third apparatus, not one; the emerging beams are seen to have both an S_z^+ component and an S_z^− component. This is a complete surprise because after the atoms emerged from the first apparatus, we made sure that the S_z^− component was completely blocked. How is it possible that the S_z^− component which, we thought, we eliminated earlier reappears? The model in which the atoms entering the third apparatus are visualized to have both S_z^+ and S_x^+ is clearly unsatisfactory.

This example is often used to illustrate that in quantum mechanics we cannot determine both S_z and S_x simultaneously. More precisely, we can say that the selection of the S_z^+ beam by the second apparatus (SG_x) completely destroys any previous information about S_z.

It is amusing to compare this situation with that of a spinning top in classical mechanics, where the angular momentum L = I ω (1.4) can be measured by determining the components of the angular velocity vector ω. By observing how fast the object is spinning in which direction we can determine ω_x, ω_y, and ω_z simultaneously. The moment of inertia I is computable if we know the mass density and the geometric shape of the spinning top, so there is no difficulty in specifying both L_x and L_y in this classical situation.

It is to be clearly understood that the limitation we have encountered in determining S_z and S_x is not due to the incompetence of the experimentalist. By improving the experimental techniques we cannot make the S_z^− component out of the third apparatus in Figure 1.3c disappear. The peculiarities of quantum mechanics are imposed upon us by the experiment itself. The limitation is, in fact, inherent in microscopic phenomena.

1.1.3 Analogy with Polarization of Light

Because this situation looks so novel, some analogy with a familiar classical situation may be helpful here. To this end we now digress to consider the polarization of light waves. This analogy will help us develop a mathematical framework for formulating the postulates of quantum mechanics.

Consider a monochromatic light wave propagating in the z-direction. A linearly polarized (or plane polarized) light with a polarization vector in the x-direction, which we call for short an x-polarized light, has a space-time dependent electric field oscillating in the x-direction E = E \hat{x} cos(kz − ωt). (1.5) Likewise, we may consider a y-polarized light, also propagating in the z-direction, E = E \hat{y} cos(kz − ωt). (1.6) Polarized light beams of type (1.5) or (1.6) can be obtained by letting an unpolarized light beam go through a Polaroid filter. We call a filter that selects only beams polarized in the x-direction an x-filter. An x-filter, of course, becomes a y-filter when rotated by 90° about the propagation (z) direction. It is well known that when we let a light beam go through an x-filter and subsequently let it impinge on a y-filter, no light beam comes out provided, of course, we are dealing with 100% efficient Polaroids; see Figure 1.4a.

The situation is even more interesting if we insert between the x-filter and the y-filter yet another Polaroid that selects only a beam polarized in the direction—which we call the x'-direction—that makes an angle of 45° with the x-direction in the xy-plane; see Figure 1.4b. This time, there is a light beam coming out of the y-filter despite the fact that right after the beam went through the x-filter it did not have any polarization component in the y-direction. In other words, once the x'-filter intervenes and selects the x'-polarized beam, it is immaterial whether the beam was previously x-polarized. The selection of the x'-polarized beam by the second Polaroid destroys any previous information on light polarization.

Notice that this situation is quite analogous to the situation that we encountered earlier with the SG arrangement of Figure 1.3b, provided that the following correspondence is made: S_z^± atoms ↔ x-, y-polarized light S_x^± atoms ↔ x'-, y'-polarized light, (1.7)

where the x' and y' axes are defined as in Figure 1.5.

Let us examine how we can quantitatively describe the behavior of 45°-polarized beams (x' and y' polarized beams) within the framework of classical electrodynamics. Using Figure 1.5 we obtain E \hat{x}' cos(kz − ωt) = E \left( \frac{1}{\sqrt{2}} \hat{x} cos(kz − ωt) + \frac{1}{\sqrt{2}} \hat{y} cos(kz − ωt) \right), E \hat{y}' cos(kz − ωt) = E \left( -\frac{1}{\sqrt{2}} \hat{x} cos(kz − ωt) + \frac{1}{\sqrt{2}} \hat{y} cos(kz − ωt) \right). (1.8)

In the triple-filter arrangement of Figure 1.4b the beam coming out of the first Polaroid is an \hat{x}-polarized beam, which can be regarded as a linear combination of an x'-polarized beam and a y'-polarized beam. The second Polaroid selects the x'-polarized beam, which can in turn be regarded as a linear combination of an x-polarized and a y-polarized beam. And finally, the third Polaroid selects the y-polarized component.

Applying correspondence (1.7) from the sequential Stern–Gerlach experiment of Figure 1.3c, to the triple-filter experiment of Figure 1.4b suggests that we might be able to represent the spin state of a silver atom by some kind of vector in a new kind of two-dimensional vector space, an abstract vector space not to be confused with the usual two-dimensional (xy) space. Just as x̂ and ŷ in (1.8) are the base vectors used to decompose the polarization vector x̂ of the x̂-polarized light, it is reasonable to represent the S+ state by a vector, which we call a ket in the Dirac notation to be developed fully in the next section. We denote this vector by |S_z;+⟩ and write it as a linear combination of two base vectors, |S_z;+⟩ and |S_z;−⟩, which correspond to the S+ and the S− states, respectively.

So we may conjecture |S_x;+⟩ = 1/√2 |S_z;+⟩ + 1/√2 |S_z;−⟩ (1.9a)

|S_x;−⟩ = −1/√2 |S_z;+⟩ + 1/√2 |S_z;−⟩ (1.9b)

in analogy with (1.8). Later we will show how to obtain these expressions using the general formalism of quantum mechanics.

Thus the unblocked component coming out of the second (SG x̂) apparatus of Figure 1.3c is to be regarded as a superposition of S+ and S− in the sense of (1.9a). It is for this reason that two components emerge from the third (SG ẑ) apparatus.

The next question of immediate concern is: How are we going to represent the S± states? Symmetry arguments suggest that if we observe an S± beam going in the x-direction and subject it to an SG ŷ apparatus, the resulting situation will be very similar to the case where an S± beam going in the y-direction is subjected to an SG x̂ apparatus. The kets for S± should then be regarded as a linear combination of |S_y;±⟩, but it appears from (1.9) that we have already used up the available possibilities in writing |S_x;±⟩. How can our vector space formalism distinguish S_y± states from S_x± states?

An analogy with polarized light again rescues us here. This time we consider a circularly polarized beam of light, which can be obtained by letting a linearly polarized light pass through a quarter-wave plate. When we pass such a circularly polarized light through an x-filter or a y-filter, we again obtain either an x-polarized beam or a y-polarized beam of equal intensity. Yet everybody knows that the circularly polarized light is totally different from the 45°-linearly polarized (x̂-polarized or ŷ-polarized) light.

Mathematically, how do we represent a circularly polarized light? A right circularly polarized light is nothing more than a linear combination of an x-polarized light and a y-polarized light, where the oscillation of the electric field for the y-polarized component is 90° out of phase with that of the x-polarized component:⁴ E = E [1/√2 x̂ cos(kz − ωt) + 1/√2 ŷ cos(kz − ωt + π/2)]. (1.10)

It is more elegant to use complex notation by introducing ε as follows: Re(ε) = E/E. (1.11)

For a right circularly polarized light, we can then write ε = 1/√2 x̂ e^{i(kz − ωt)} + 1/√2 ŷ e^{i(kz − ωt)}, (1.12)

where we have used i = e^{iπ/2}.

We can make the following analogy with the spin states of silver atoms: S+ atom ↔ right circularly polarized beam, S− atom ↔ left circularly polarized beam. (1.13)

Applying this analogy to (1.12), we see that if we are allowed to make the coefficients preceding base kets complex, there is no difficulty in accommodating the S± atoms in our vector space formalism: |S_y;±⟩ = 1/√2 |S_z;+⟩ ± i/√2 |S_z;−⟩, (1.14)

which are obviously different from (1.9). We thus see that the two-dimensional vector space needed to describe the spin states of silver atoms must be a complex vector space; an arbitrary vector in the vector space is written as a linear combination of the base vectors |S_z;±⟩ with, in general, complex coefficients. The fact that the necessity of complex numbers is already apparent in such an elementary example is rather remarkable.

The reader must have noted by this time that we have deliberately avoided talking about photons. In other words, we have completely ignored the quantum aspect of light; nowhere did we mention the polarization states of individual photons. The analogy we worked out is between kets in an abstract vector space that describes the spin states of individual atoms with the polarization vectors of the classical electromagnetic field. Actually we could have made the analogy even more vivid by introducing the photon concept and talking about the probability of finding a circularly polarized photon in a linearly polarized state, and so forth; however, that is not needed here. Without doing so, we have already accomplished the main goal of this section: to introduce the idea that quantum-mechanical states are to be represented by vectors in an abstract complex vector space.⁵

Finally, before outlining the mathematical formalism of quantum mechanics, we remark that the physics of a Stern–Gerlach apparatus is of far more than simply academic interest. The ability to separate spin states of atoms has tremendous practical interest as well. Figure 1.6 shows the use of the Stern–Gerlach technique to analyze the result of spin manipulation in an atomic beam of cesium atoms. The only stable isotope, 133Cs, of this alkali atom has a nuclear spin I=7/2, and the experiment sorts out the F=4 hyperfine magnetic substate, giving nine spin orientations. This is only one of many examples where this once mysterious effect is used for practical devices. Of course, all of these uses only go to firmly establish this effect, and the quantum-mechanical principles which we will now present and further develop.

## 1.2 Kets, Bras, and Operators

In the preceding section we showed how analyses of the Stern–Gerlach experiment led us to consider a complex vector space. In this and the following section we formulate the basic mathematics of vector spaces as used in quantum mechanics. Our notation throughout this book is the bra and ket notation developed by P. A. M. Dirac. The theory of linear vector spaces had, of course, been known to mathematicians prior to the birth of quantum mechanics, but Dirac’s way of introducing vector spaces has many advantages, especially from the physicist’s point of view.

1.2.1 Ket Space

We consider a complex vector space whose dimensionality is specified according to the nature of a physical system under consideration. In Stern–Gerlach type experiments where the only quantum-mechanical degree of freedom is the spin of an atom, the dimensionality is determined by the number of alternative paths the atoms can follow when subjected to an SG apparatus; in the case of the silver atoms of the previous section, the dimensionality is just two, corresponding to the two possible values Sz can assume.⁶ Later, in Section 1.6, we consider the case of continuous spectra, for example, the position (coordinate) or momentum of a particle, where the number of alternatives is nondenumerably infinite, in which case the vector space in question is known as a Hilbert space after D. Hilbert, who studied vector spaces in infinite dimensions.

In quantum mechanics a physical state, for example, a silver atom with a definite spin orientation, is represented by a state vector in a complex vector space. Following Dirac, we call such a vector a ket and denote it by |α⟩. This state ket is postulated to contain complete information about the physical state; everything we are allowed to ask about the state is contained in the ket. Two kets can be added: |α⟩ + |β⟩ = |γ⟩. (1.15)

The sum |γ⟩ is just another ket. If we multiply |α⟩ by a complex number c, the resulting product c|α⟩ is another ket. The number c can stand on the left or on the right of a ket; it makes no difference: c|α⟩ = |α⟩c. (1.16)

In the particular case where c is zero, the resulting ket is said to be a null ket.

One of the physics postulates is that |α⟩ and c|α⟩, with c ≠ 0, represent the same physical state. In other words, only the “direction” in vector space is of significance. Mathematicians may prefer to say that we are here dealing with rays rather than vectors.

An observable, such as momentum and spin components, can be represented by an operator, such as A, in the vector space in question. Quite generally, an operator acts on a ket from the left, A·(|α⟩) = A|α⟩, (1.17)

which is yet another ket. There will be more on multiplication operations later.

In general, A|α⟩ is not a constant times |α⟩. However, there are particular kets of importance, known as eigenkets of operator A, denoted by |a′⟩, |a″⟩, |a‴⟩, ... (1.18)

with the property A|a′⟩ = a′|a′⟩, A|a″⟩ = a″|a″⟩, ... (1.19)

where a′, a″, ... are just numbers. Notice that applying A to an eigenket just reproduces the same ket apart from a multiplicative number. The set of numbers {a′, a″, a‴, ...}, more compactly denoted by {a′}, is called the set of eigenvalues of operator A. When it becomes necessary to order eigenvalues in a specific manner, {a(1), a(2), a(3), ...} may be used in place of {a′, a″, a‴, ...}.

The physical state corresponding to an eigenket is called an eigenstate. In the simplest case of spin-1/2 systems, the eigenvalue-eigenket relation (1.19) is expressed as Sz|Sz;+⟩ = (ħ/2)|Sz;+⟩, Sz|Sz;−⟩ = −(ħ/2)|Sz;−⟩, (1.20)

where |Sz;±⟩ are eigenkets of operator Sz with eigenvalues ±ħ/2. Here we could have used just |ħ/2⟩ for |Sz;+⟩ in conformity with the notation where an eigenket is labeled by its eigenvalue, but the notation |S_x; ±⟩, already used in the previous section, is more convenient here because we also consider eigenkets of S_x:

$$S_x |S_x; ±\rangle = ± |S_x; ±\rangle. \tag{1.21}$$

We remarked earlier that the dimensionality of the vector space is determined by the number of alternatives in Stern–Gerlach type experiments. More formally, we are concerned with an N-dimensional vector space spanned by the N eigenkets of observable A. Any arbitrary ket |α⟩ can be written as

$$|\alpha\rangle = \sum_{a'} c_{a'} |a'\rangle, \tag{1.22}$$

with a', a'', ... up to a^{(N)}, where c_{a'} is a complex coefficient. The question of the uniqueness of such an expansion will be postponed until we prove the orthogonality of eigenkets.

**1.2.2 Bra Space and Inner Products**

The vector space we have been dealing with is a ket space. We now introduce the notion of a bra space, a vector space "dual to" the ket space. We postulate that corresponding to every ket |α⟩ there exists a bra, denoted by ⟨α|, in this dual, or bra, space. The bra space is spanned by eigenbras ⟨a'| which correspond to the eigenkets {|a'⟩}. There is a one-to-one correspondence between a ket space and a bra space:

$$|\alpha\rangle \leftrightarrow_{DC} \langle\alpha|$$

$$|a'\rangle, |a''\rangle, ... \leftrightarrow_{DC} \langle a'|, \langle a''|, ... \tag{1.23}$$

$$|\alpha\rangle + |\beta\rangle \leftrightarrow_{DC} \langle\alpha| + \langle\beta|$$

where DC stands for dual correspondence. Roughly speaking, we can regard the bra space as some kind of mirror image of the ket space.

The bra dual to c|α⟩ is postulated to be c*⟨α|, not c⟨α|, which is a very important point. More generally, we have

$$c_\alpha |\alpha\rangle + c_\beta |\beta\rangle \leftrightarrow_{DC} c_\alpha^* \langle\alpha| + c_\beta^* \langle\beta|. \tag{1.24}$$

We now define the inner product of a bra and a ket.⁷ The product is written as a bra standing on the left and a ket standing on the right, for example,

$$\langle\beta|\alpha\rangle = (\langle\beta|) \cdot (|\alpha\rangle). \tag{1.25}$$

bra(c)ket

This product is, in general, a complex number. Notice that in forming an inner product we always take one vector from the bra space and one vector from the ket space.

We postulate two fundamental properties of inner products. First,

$$\langle\beta|\alpha\rangle = \langle\alpha|\beta\rangle^*. \tag{1.26}$$

⁷ In the literature an inner product is often referred to as a scalar product because it is analogous to a·b in Euclidean space; in this book, however, we reserve the term scalar for a quantity invariant under rotations in the usual three-dimensional space.

In other words, ⟨β|α⟩ and ⟨α|β⟩ are complex conjugates of each other. Notice that even though the inner product is, in some sense, analogous to the familiar scalar product a·b, ⟨β|α⟩ must be clearly distinguished from ⟨α|β⟩; the analogous distinction is not needed in real vector space because a·b is equal to b·a. Using (1.26) we can immediately deduce that ⟨α|α⟩ must be a real number. To prove this just let ⟨β| → ⟨α|.

The second postulate on inner products is

$$\langle\alpha|\alpha\rangle \ge 0, \tag{1.27}$$

where the equality sign holds only if |α⟩ is a null ket. This is sometimes known as the postulate of positive definite metric. From a physicist’s point of view, this postulate is essential for the probabilistic interpretation of quantum mechanics, as will become apparent later.⁸

Two kets |α⟩ and |β⟩ are said to be orthogonal if

$$\langle\alpha|\beta\rangle = 0, \tag{1.28}$$

even though in the definition of the inner product the bra ⟨α| appears. The orthogonality relation (1.28) also implies, via (1.26),

$$\langle\beta|\alpha\rangle = 0. \tag{1.29}$$

Given a ket which is not a null ket, we can form a normalized ket |\tilde{\alpha}\rangle, where

$$|\tilde{\alpha}\rangle = \frac{1}{\sqrt{\langle\alpha|\alpha\rangle}} |\alpha\rangle, \tag{1.30}$$

with the property

$$\langle\tilde{\alpha}|\tilde{\alpha}\rangle = 1. \tag{1.31}$$

Quite generally, ⟨α|α⟩ is known as the norm of |α⟩, analogous to the magnitude of vector a·a = |\vec{a}| in Euclidean vector space. Because |α⟩ and c|α⟩ represent the same physical state, we might as well require that the kets we use for physical states be normalized in the sense of (1.31).⁹

**1.2.3 Operators**

As we remarked earlier, observables like momentum and spin components are to be represented by operators that can act on kets. We can consider a more general class of operators that act on kets; they will be denoted by X, Y, and so forth, while A, B, and so on will be used for a restrictive class of operators that correspond to observables.

An operator acts on a ket from the left side,

$$X \cdot (|\alpha\rangle) = X|\alpha\rangle, \tag{1.32}$$

⁸ Attempts to abandon this postulate led to physical theories with "indefinite metric." We shall not be concerned with such theories in this book.

⁹ For eigenkets of observables with continuous spectra, different normalization conventions will be used; see Section 1.6.

and the resulting product is another ket. Operators X and Y are said to be equal,

$$X = Y, \tag{1.33}$$

if

$$X|\alpha\rangle = Y|\alpha\rangle \tag{1.34}$$

for an arbitrary ket in the ket space in question. Operator X is said to be the null operator if, for any arbitrary ket |α⟩, we have

$$X|\alpha\rangle = 0. \tag{1.35}$$

Operators can be added; addition operations are commutative and associative:

$$X + Y = Y + X, \tag{1.36a}$$

$$X + (Y + Z) = (X + Y) + Z. \tag{1.36b}$$

With the single exception of the time-reversal operator to be considered in Chapter 4, the operators that appear in this book are all linear, that is,

$$X(c_\alpha |\alpha\rangle + c_\beta |\beta\rangle) = c_\alpha X|\alpha\rangle + c_\beta X|\beta\rangle. \tag{1.37}$$

An operator X always acts on a bra from the right side

$$(\langle\alpha|) \cdot X = \langle\alpha|X, \tag{1.38}$$

and the resulting product is another bra. The ket X|α⟩ and the bra ⟨α|X are, in general, not dual to each other. We define the symbol X† as

$$X|\alpha\rangle \leftrightarrow_{DC} \langle\alpha|X^\dagger. \tag{1.39}$$

The operator X† is called the Hermitian adjoint, or simply the adjoint, of X. An operator X is said to be Hermitian if

$$X = X^\dagger. \tag{1.40}$$

**1.2.4 Multiplication**

Operators X and Y can be multiplied. Multiplication operations are, in general, noncommutative, that is,

$$XY \ne YX. \tag{1.41}$$

Multiplication operations are, however, associative:

$$X(YZ) = (XY)Z = XYZ. \tag{1.42}$$

We also have

$$X(Y|\alpha\rangle) = (XY)|\alpha\rangle = XY|\alpha\rangle, \quad (\langle\beta|X)Y = \langle\beta|(XY) = \langle\beta|XY. \tag{1.43}$$

Notice that

$$(XY)^\dagger = Y^\dagger X^\dagger \tag{1.44}$$

because

$$XY|\alpha\rangle = X(Y|\alpha\rangle) \leftrightarrow_{DC} (\langle\alpha|Y^\dagger)X^\dagger = \langle\alpha|Y^\dagger X^\dagger. \tag{1.45}$$

So far, we have considered the following products: ⟨β|α⟩, X|α⟩, ⟨α|X, and XY. Are there other products we are allowed to form? Let us multiply |β⟩ and ⟨α|, in that order. The resulting product

$$(|\beta\rangle) \cdot (\langle\alpha|) = |\beta\rangle\langle\alpha| \tag{1.46}$$

is known as the outer product of |β⟩ and ⟨α|. We will emphasize in a moment that |β⟩⟨α| is to be regarded as an operator; hence it is fundamentally different from the inner product ⟨β|α⟩, which is just a number.

There are also "illegal products." We have already mentioned that an operator must stand on the left of a ket or on the right of a bra. In other words, |α⟩X and X⟨α| are examples of illegal products. They are neither kets, nor bras, nor operators; they are simply nonsensical. Products like |α⟩|β⟩ and ⟨α|⟨β| are also illegal when |α⟩ and |β⟩ (⟨α| and ⟨β|) are ket (bra) vectors belonging to the same ket (bra) space.¹⁰

**1.2.5 The Associative Axiom**

As is clear from (1.42), multiplication operations among operators are associative. Actually the associative property is postulated to hold quite generally as long as we are dealing with "legal" multiplications among kets, bras, and operators. Dirac calls this important postulate the associative axiom of multiplication.

To illustrate the power of this axiom let us first consider an outer product acting on a ket:

$$(|\beta\rangle\langle\alpha|) \cdot |\gamma\rangle. \tag{1.47}$$

Because of the associative axiom, we can regard this equally well as

$$|\beta\rangle \cdot (\langle\alpha|\gamma\rangle), \tag{1.48}$$

where ⟨α|γ⟩ is just a number. So the outer product acting on a ket is just another ket; in other words, |β⟩⟨α| can be regarded as an operator. Because (1.47) and (1.48) are equal, we may as well omit the dots and let |β⟩⟨α|γ⟩ stand for the operator |β⟩⟨α| acting on |γ⟩ or, equivalently, the number ⟨α|γ⟩ multiplying |β⟩. (On the other hand, if (1.48) is written as (⟨α|γ⟩)·|β⟩, we cannot afford to omit the dot and brackets because the resulting expression would look illegal.) Notice that the operator |β⟩⟨α| rotates |γ⟩ into the direction of |β⟩. It is easy to see that if

$$X = |\beta\rangle\langle\alpha|, \tag{1.49}$$

¹⁰ Later in the book we will encounter products like |α⟩|β⟩, which are more appropriately written as |α⟩⊗|β⟩, but in such cases |α⟩ and |β⟩ always refer to kets from different vector spaces. For instance, the first ket belongs to the vector space for electron spin, the second ket to the vector space for electron orbital angular momentum; or the first ket lies in the vector space of particle 1, the second ket in the vector space of particle 2, and so forth.

then

$$X^\dagger = |\alpha\rangle\langle\beta|, \tag{1.50}$$

which is left as an exercise.

In a second important illustration of the associative axiom, we note that

$$(\langle\beta|) \cdot (X|\alpha\rangle) = (\langle\beta|X) \cdot (|\alpha\rangle). \tag{1.51}$$

bra ket bra ket

Because the two sides are equal, we might as well use the more compact notation

$$\langle\beta|X|\alpha\rangle \tag{1.52}$$

to stand for either side of (1.51). Recall now that ⟨α|X† is the bra that is dual to X|α⟩, so

$$\langle\beta|X|\alpha\rangle = \langle\beta| \cdot (X|\alpha\rangle)$$

$$= \{(\langle\alpha|X^\dagger) \cdot |\beta\rangle\}^*$$

$$= \langle\alpha|X^\dagger|\beta\rangle^*, \tag{1.53}$$

where, in addition to the associative axiom, we used the fundamental property of the inner product (1.26). For a Hermitian X we have

$$\langle\beta|X|\alpha\rangle = \langle\alpha|X|\beta\rangle^*. \tag{1.54}$$

**1.3 Base Kets and Matrix Representations**

**1.3.1 Eigenkets of an Observable**

Let us consider the eigenkets and eigenvalues of a Hermitian operator A. We use the symbol A, reserved earlier for an observable, because in quantum mechanics Hermitian operators of interest quite often turn out to be the operators representing some physical observables. We begin by stating an important theorem.

**Theorem 1** The eigenvalues of a Hermitian operator A are real; the eigenkets of A corresponding to different eigenvalues are orthogonal.

**Proof** First, recall that

$$A|a'\rangle = a'|a'\rangle. \tag{1.55}$$

Because A is Hermitian, we also have

$$\langle a''|A = a''^*\langle a''|, \tag{1.56}$$

where a', a'', ... are eigenvalues of A. If we multiply both sides of (1.55) by ⟨a''| on the left, both sides of (1.56) by |a'⟩ on the right, and subtract, we obtain

$$(a' - a'')...$$ ⟨a'|a⟩ = 0. (1.57)

## 1.3 Base Kets and Matrix Representations

Now a' and a'' can be taken to be either the same or different. Let us first choose them to be the same; we then deduce the reality condition (the first half of the theorem)

a' = a'*, (1.58)

where we have used the fact that |a'⟩ is not a null ket. Let us now assume a' and a'' to be different. Because of the just proved reality condition, the difference a' - a''* that appears in (1.57) is equal to a' - a'', which cannot vanish, by assumption. The inner product ⟨a''|a'⟩ must then vanish: ⟨a''|a'⟩ = 0 (a' ≠ a''), (1.59)

which proves the orthogonality property (the second half of the theorem). □

We expect on physical grounds that an observable has real eigenvalues, a point that will become clearer in the next section, where measurements in quantum mechanics will be discussed. The theorem just proved guarantees the reality of eigenvalues whenever the operator is Hermitian. That is why we talk about Hermitian observables in quantum mechanics.

It is conventional to normalize |a'⟩ so the {|a'⟩} form an orthonormal set: ⟨a''|a'⟩ = δ_{a''a'}. (1.60)

We may logically ask: Is this set of eigenkets complete? Since we started our discussion by asserting that the whole ket space is spanned by the eigenkets of A, the eigenkets of A must therefore form a complete set by construction of our ket space.11

1.3.2 Eigenkets as Base Kets

We have seen that the normalized eigenkets of A form a complete orthonormal set. An arbitrary ket in the ket space can be expanded in terms of the eigenkets of A. In other words, the eigenkets of A are to be used as base kets in much the same way as a set of mutually orthogonal unit vectors is used as base vectors in Euclidean space.

Given an arbitrary ket |α⟩ in the ket space spanned by the eigenkets of A, let us attempt to expand it as follows: |α⟩ = ∑_{a'} c_{a'} |a'⟩. (1.61)

Multiplying ⟨a''| on the left and using the orthonormality property (1.60), we can immediately find the expansion coefficient, c_{a'} = ⟨a'|α⟩. (1.62)

In other words, we have |α⟩ = ∑_{a'} |a'⟩⟨a'|α⟩, (1.63)

which is analogous to an expansion of a vector V in (real) Euclidean space: V = ∑_i ē_i (ē_i · V), (1.64)

where {ē_i} form an orthogonal set of unit vectors. We now recall the associative axiom of multiplication: |a'⟩⟨a'|α⟩ can be regarded either as the number ⟨a'|α⟩ multiplying |a'⟩ or, equivalently, as the operator |a'⟩⟨a'| acting on |α⟩. Because |α⟩ in (1.63) is an arbitrary ket, we must have ∑_{a'} |a'⟩⟨a'| = 1, (1.65)

where the 1 on the right-hand side is to be understood as the identity operator. Equation (1.65) is known as the completeness relation or closure.

It is difficult to overestimate the usefulness of (1.65). Given a chain of kets, operators, or bras multiplied in legal orders, we can insert, in any place at our convenience, the identity operator written in the form (1.65). Consider, for example ⟨α|α⟩; by inserting the identity operator between ⟨α| and |α⟩, we obtain ⟨α|α⟩ = ⟨α| · ∑_{a'} |a'⟩⟨a'| · |α⟩ = ∑_{a'} |⟨a'|α⟩|^2. (1.66)

This, incidentally, shows that if |α⟩ is normalized, then the expansion coefficients in (1.61) must satisfy ∑_{a'} |c_{a'}|^2 = ∑_{a'} |⟨a'|α⟩|^2 = 1. (1.67)

Let us now look at |a'⟩⟨a'| that appears in (1.65). Since this is an outer product, it must be an operator. Let it operate on |α⟩: (|a'⟩⟨a'|) · |α⟩ = |a'⟩⟨a'|α⟩ = c_{a'} |a'⟩. (1.68)

We see that |a'⟩⟨a'| selects that portion of the ket |α⟩ parallel to |a'⟩, so |a'⟩⟨a'| is known as the projection operator along the base ket |a'⟩ and is denoted by Λ_{a'}: Λ_{a'} ≡ |a'⟩⟨a'|. (1.69)

The completeness relation (1.65) can now be written as ∑_{a'} Λ_{a'} = 1. (1.70)

1.3.3 Matrix Representations

Having specified the base kets, we now show how to represent an operator, say X, by a square matrix. First, using (1.65) twice, we write the operator X as X = ∑_{a''} ∑_{a'} |a''⟩⟨a''|X|a'⟩⟨a'|. (1.71)

There are altogether N^2 numbers of the form ⟨a''|X|a'⟩, where N is the dimensionality of the ket space. We may arrange them into an N × N square matrix such that the column and row indices appear as follows: ⟨a''|X|a'⟩. (1.72)

row column Explicitly we may write the matrix as X = ⟨a(1)|X|a(1)⟩   ⟨a(1)|X|a(2)⟩   ⋯ ⟨a(2)|X|a(1)⟩   ⟨a(2)|X|a(2)⟩   ⋯ , (1.73)

.       .       .

.       .       .

.       .       ⋱ where the symbol = stands for “is represented by.”12

Using (1.53), we can write ⟨a''|X|a'⟩ = ⟨a'|X†|a''⟩^*. (1.74)

At last, the Hermitian adjoint operation, originally defined by (1.39), has been related to the (perhaps more familiar) concept of complex conjugate transpose. If an operator B is Hermitian, we have ⟨a''|B|a'⟩ = ⟨a'|B|a''⟩^*. (1.75)

The way we arranged ⟨a''|X|a'⟩ into a square matrix is in conformity with the usual rule of matrix multiplication. To see this just note that the matrix representation of the operator relation Z = XY (1.76)

reads ⟨a''|Z|a'⟩ = ⟨a''|XY|a'⟩ = ∑_{a'''} ⟨a''|X|a'''⟩⟨a'''|Y|a'⟩. (1.77)

Again, all we have done is to insert the identity operator, written in the form (1.65), between X and Y!

Let us now examine how the ket relation |γ⟩ = X|α⟩ (1.78)

can be represented using our base kets. The expansion coefficients of |γ⟩ can be obtained by multiplying ⟨a'| on the left: ⟨a'|γ⟩ = ⟨a'|X|α⟩ = ∑_{a''} ⟨a'|X|a''⟩⟨a''|α⟩. (1.79)

But this can be seen as an application of the rule for multiplying a square matrix with a column matrix, once the expansion coefficients of |α⟩ and |γ⟩ are themselves arranged to form column matrices as follows: |α⟩ = ⟨a(1)|α⟩ ,   |γ⟩ = ⟨a(1)|γ⟩ , ⟨a(2)|α⟩       ⟨a(2)|γ⟩ ⟨a(3)|α⟩       ⟨a(3)|γ⟩ . .              . .

. .              . .

.                .

. (1.80)

Likewise, given ⟨γ| = ⟨α|X, (1.81)

we can regard ⟨γ|a'⟩ = ∑_{a''} ⟨α|a''⟩⟨a''|X|a'⟩. (1.82)

So a bra is represented by a row matrix as follows: ⟨γ| = (⟨γ|a(1)⟩, ⟨γ|a(2)⟩, ⟨γ|a(3)⟩, ...) = (⟨a(1)|γ⟩^*, ⟨a(2)|γ⟩^*, ⟨a(3)|γ⟩^*, ...). (1.83)

Note the appearance of complex conjugation when the elements of the column matrix are written as in (1.83). The inner product ⟨β|α⟩ can be written as the product of the row matrix representing ⟨β| with the column matrix representing |α⟩: ⟨β|α⟩ = ∑_{a'} ⟨β|a'⟩⟨a'|α⟩ = (⟨a(1)|β⟩^*, ⟨a(2)|β⟩^*, ...) ⟨a(1)|α⟩ ⟨a(2)|α⟩ . (1.84)

. .

.

If we multiply the row matrix representing ⟨α| with the column matrix representing |β⟩, then we obtain just the complex conjugate of the preceding expression, which is consistent with the fundamental property of the inner product (1.26). Finally, the matrix representation of the outer product |β⟩⟨α| is easily seen to be |β⟩⟨α| = ⟨a(1)|β⟩⟨a(1)|α⟩^*   ⟨a(1)|β⟩⟨a(2)|α⟩^*   ⋯ ⟨a(2)|β⟩⟨a(1)|α⟩^*   ⟨a(2)|β⟩⟨a(2)|α⟩^*   ⋯ . (1.85)

.             .               .

.             .               .

.             .               ⋱ The matrix representation of an observable A becomes particularly simple if the eigenkets of A themselves are used as the base kets. First, we have A = ∑_{a''} ∑_{a'} |a''⟩⟨a''|A|a'⟩⟨a'|. (1.86)

But the square matrix ⟨a''|A|a'⟩ is obviously diagonal, ⟨a''|A|a'⟩ = ⟨a'|A|a'⟩δ_{a'a''} = a' δ_{a'a''}, (1.87)

so A = ∑_{a'} a' |a'⟩⟨a'| = ∑_{a'} a' Λ_{a'}. (1.88)

1.3.4 Spin 1/2 Systems

It is here instructive to consider the special case of spin 1/2 systems. The base kets used are |S_z; ±⟩, which we denote, for brevity, as |±⟩. The simplest operator in the ket space spanned by |±⟩ is the identity operator, which, according to (1.65), can be written as 1 = |+⟩⟨+| + |−⟩⟨−|. (1.89)

According to (1.88), we must be able to write S_z as S_z = (ħ/2)[|+⟩⟨+| − |−⟩⟨−|]. (1.90)

The eigenket-eigenvalue relation S_z |±⟩ = ± (ħ/2)|±⟩ (1.91)

immediately follows from the orthonormality property of |±⟩.

It is also instructive to look at two other operators, S_+ ≡ ħ |+⟩⟨−|,   S_− ≡ ħ |−⟩⟨+|, (1.92)

which are both seen to be non-Hermitian. The operator \(S_+\), acting on the spin-down ket \(|-\rangle\), turns \(|-\rangle\) into the spin-up ket \(|+\rangle\) multiplied by \(\hbar\). On the other hand, the spin-up ket \(|+\rangle\), when acted upon by \(S_+\), becomes a null ket. So the physical interpretation of \(S_+\) is that it raises the spin component by one unit of \(\hbar\); if the spin component cannot be raised any further, we automatically get a null state. Likewise, \(S_-\) can be interpreted as an operator that lowers the spin component by one unit of \(\hbar\). Later we will show that \(S_\pm\) can be written as \(S_x \pm i S_y\).

In constructing the matrix representations of the angular-momentum operators, it is customary to label the column (row) indices in descending order of angular-momentum components, that is, the first entry corresponds to the maximum angular-momentum component, the second, the next highest, and so forth. In our particular case of spin \(\frac{1}{2}\) systems, we have \[ |+\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |-\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \tag{1.93a} \]

\[ S_+ = \hbar \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad S_- = \hbar \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}. \tag{1.93b} \]

We will come back to these explicit expressions when we discuss the Pauli two-component formalism in Chapter 3.

## 1.4 Measurements, Observables, and the Uncertainty Relations

1.4.1 Measurements

Having developed the mathematics of ket spaces, we are now in a position to discuss the quantum theory of measurement processes. This is not a particularly easy subject for beginners, so we first turn to the words of the great master, P. A. M. Dirac, for guidance (Dirac(1958), p. 36): "A measurement always causes the system to jump into an eigenstate of the dynamical variable that is being measured." What does all this mean? We interpret Dirac’s words as follows: Before a measurement of observable \(A\) is made, the system is assumed to be represented by some linear combination \[ |\alpha\rangle = \sum_{a'} c_{a'} |a'\rangle = \sum_{a'} |a'\rangle\langle a'|\alpha\rangle. \tag{1.94} \]

When the measurement is performed, the system is "thrown into" one of the eigenstates, say \(|a'\rangle\), of observable \(A\). In other words, \[ |\alpha\rangle \xrightarrow{A\text{-measurement}} |a'\rangle. \tag{1.95} \]

For example, a silver atom with an arbitrary spin orientation will change into either \(|S_z; +\rangle\) or \(|S_z; -\rangle\) when subjected to an SG apparatus of type \(SG\hat{z}\). Thus a measurement usually changes the state. The only exception is when the state is already in one of the eigenstates of the observable being measured, in which case \[ |a'\rangle \xrightarrow{A\text{-measurement}} |a'\rangle \tag{1.96} \]

with certainty, as will be discussed further. When the measurement causes \(|\alpha\rangle\) to change into \(|a'\rangle\), it is said that \(A\) is measured to be \(a'\). It is in this sense that the result of a measurement yields one of the eigenvalues of the observable being measured.

Given (1.94), which is the state ket of a physical system before the measurement, we do not know in advance into which of the various \(|a'\rangle\) the system will be thrown as the result of the measurement. We do postulate, however, that the probability for jumping into some particular \(|a'\rangle\) is given by \[ \text{Probability for } a' = |\langle a'|\alpha\rangle|^2, \tag{1.97} \]

provided that \(|\alpha\rangle\) is normalized.

Although we have been talking about a single physical system, to determine probability (1.97) empirically, we must consider a great number of measurements performed on an ensemble, that is, a collection, of identically prepared physical systems, all characterized by the same ket \(|\alpha\rangle\). Such an ensemble is known as a pure ensemble. (We will say more about ensembles in Chapter 3.) As an example, a beam of silver atoms which survive the first \(SG\hat{z}\) apparatus of Figure 1.3 with the \(S_z\) \(-\) component blocked is an example of a pure ensemble because every member atom of the ensemble is characterized by \(|S_z; +\rangle\).

The probabilistic interpretation (1.97) for the squared inner product \(|\langle a'|\alpha\rangle|^2\) is one of the fundamental postulates of quantum mechanics, so it cannot be proven. Let us note, however, that it makes good sense in extreme cases. Suppose the state ket is \(|a'\rangle\) itself even before a measurement is made; then according to (1.97), the probability for getting \(a'\), or, more precisely, for being thrown into \(|a'\rangle\), as the result of the measurement is predicted to be 1, which is just what we expect. By measuring \(A\) once again, we, of course, get \(|a'\rangle\) only; quite generally, repeated measurements of the same observable in succession yield the same result. If, on the other hand, we are interested in the probability for the system initially characterized by \(|a'\rangle\) to be thrown into some other eigenket \(|a''\rangle\) with \(a'' \neq a'\), then (1.97) gives zero because of the orthogonality between \(|a'\rangle\) and \(|a''\rangle\). From the point of view of measurement theory, orthogonal kets correspond to mutually exclusive alternatives; for example, if a spin \(\frac{1}{2}\) system is in \(|S_z; +\rangle\), it is not in \(|S_z; -\rangle\) with certainty.

Quite generally, the probability for anything must be nonnegative. Furthermore, the probabilities for the various alternative possibilities must add up to unity. Both of these expectations are met by our probability postulate (1.97).

We define the expectation value of \(A\) taken with respect to state \(|\alpha\rangle\) as \[ \langle A \rangle \equiv \langle \alpha|A|\alpha\rangle. \tag{1.98} \]

To make sure that we are referring to state \(|\alpha\rangle\), the notation \(\langle A \rangle_\alpha\) is sometimes used. Equation (1.98) is a definition; however, it agrees with our intuitive notion of average measured value because it can be written as \[ \langle A \rangle = \sum_{a'} \sum_{a''} \langle \alpha|a''\rangle \langle a''|A|a'\rangle \langle a'|\alpha\rangle = \sum_{a'} a' |\langle a'|\alpha\rangle|^2. \tag{1.99} \]

It is very important not to confuse eigenvalues with expectation values. For example, the expectation value of \(S_z\) for spin \(\frac{1}{2}\) systems can assume any real value between \(-\hbar/2\) and \(+\hbar/2\), say \(0.273\hbar\); in contrast, the eigenvalue of \(S_z\) assumes only two values, \(\hbar/2\) and \(-\hbar/2\).

To clarify further the meaning of measurements in quantum mechanics, we introduce the notion of a selective measurement, or filtration. In Section 1.1 we considered a Stern–Gerlach arrangement where we let only one of the spin components pass out of the apparatus while we completely blocked the other component. More generally, we imagine a measurement process with a device that selects only one of the eigenkets of \(A\), say \(|a'\rangle\), and rejects all others; see Figure 1.7. This is what we mean by a selective measurement; it is also called filtration because only one of the \(A\) eigenkets filters through the ordeal. Mathematically we can say that such a selective measurement amounts to applying the projection operator \(\Lambda_{a'}\) to \(|\alpha\rangle\): \[ \Lambda_{a'}|\alpha\rangle = |a'\rangle\langle a'|\alpha\rangle. \tag{1.100} \]

J. Schwinger has developed a formalism of quantum mechanics based on a thorough examination of selective measurements. He introduces a measurement symbol \(M(a')\) in the beginning, which is identical to \(\Lambda_{a'}\) or \(|a'\rangle\langle a'|\) in our notation, and deduces a number of properties of \(M(a')\) (and also of \(M(b',a')\) which amount to \(|b'\rangle\langle a'|\)) by studying the outcome of various Stern–Gerlach type experiments. In this way he motivates the entire mathematics of kets, bras, and operators. In this book we do not follow Schwinger’s path; the interested reader may consult Gottfried(1966).

1.4.2 Spin \(\frac{1}{2}\) Systems, Once Again

Before proceeding with a general discussion of observables, we once again consider spin \(\frac{1}{2}\) systems. This time we show that the results of sequential Stern–Gerlach experiments, when combined with the postulates of quantum mechanics discussed so far, are sufficient to determine not only the \(S_x\), \(S_y\) eigenkets, \(|S_x; \pm\rangle\) and \(|S_y; \pm\rangle\), but also the operators \(S_x\) and \(S_y\) themselves.

First, we recall that when the \(S_x\) \(+\) beam is subjected to an apparatus of type \(SG\hat{z}\), the beam splits into two components with equal intensities. This means that the probability for the \(S_x\) \(+\) state to be thrown into \(|S_z; \pm\rangle\), simply denoted as \(|\pm\rangle\), is \(\frac{1}{2}\) each; hence, \[ |\langle +|S_x; +\rangle| = |\langle -|S_x; +\rangle| = \frac{1}{\sqrt{2}}. \tag{1.101} \]

We can therefore construct the \(S_x\) \(+\) ket as follows: \[ |S_x; +\rangle = \frac{1}{\sqrt{2}} |+\rangle + \frac{1}{\sqrt{2}} e^{i\delta_1} |-\rangle, \tag{1.102} \]

with \(\delta_1\) real. In writing (1.102) we have used the fact that the overall phase (common to both \(|+\rangle\) and \(|-\rangle\)) of a state ket is immaterial; the coefficient of \(|+\rangle\) can be chosen to be real and positive by convention. The \(S_x\) \(-\) ket must be orthogonal to the \(S_x\) \(+\) ket because the \(S_x\) \(+\) alternative and \(S_x\) \(-\) alternative are mutually exclusive. This orthogonality requirement leads to \[ |S_x; -\rangle = \frac{1}{\sqrt{2}} |+\rangle - \frac{1}{\sqrt{2}} e^{i\delta_1} |-\rangle, \tag{1.103} \]

where we have, again, chosen the coefficient of \(|+\rangle\) to be real and positive by convention.

We can now construct the operator \(S_x\) using (1.88) as follows: \[ \begin{aligned} S_x &= \frac{\hbar}{2} [(|S_x; +\rangle\langle S_x; +|) - (|S_x; -\rangle\langle S_x; -|)] \\ &= \frac{\hbar}{2} [e^{-i\delta_1} (|+\rangle\langle -|) + e^{i\delta_1} (|-\rangle\langle +|)].

\end{aligned} \tag{1.104} \]

Notice that the \(S_x\) we have constructed is Hermitian, just as it must be. A similar argument with \(S_x\) replaced by \(S_y\) leads to \[ |S_y; \pm\rangle = \frac{1}{\sqrt{2}} |+\rangle \pm \frac{1}{\sqrt{2}} e^{i\delta_2} |-\rangle, \tag{1.105} \]

\[ S_y = \frac{\hbar}{2} [e^{-i\delta_2} (|+\rangle\langle -|) + e^{i\delta_2} (|-\rangle\langle +|)]. \tag{1.106} \]

Is there any way of determining \(\delta_1\) and \(\delta_2\)? Actually there is one piece of information we have not yet used. Suppose we have a beam of spin \(\frac{1}{2}\) atoms moving in the \(z\)-direction. We can consider a sequential Stern–Gerlach experiment with \(SG\hat{x}\) followed by \(SG\hat{y}\). The results of such an experiment are completely analogous to the earlier case leading to (1.101): \[ |\langle S_y; \pm|S_x; +\rangle| = |\langle S_y; \pm|S_x; -\rangle| = \frac{1}{\sqrt{2}}, \tag{1.107} \]

which is not surprising in view of the invariance of physical systems under rotations. Inserting (1.103) and (1.105) into (1.107), we obtain \[ |1 \pm e^{i(\delta_1 - \delta_2)}| = \frac{1}{\sqrt{2}} \times 2 = \sqrt{2}, \tag{1.108} \]

which is satisfied only if \[ \delta_1 - \delta_2 = \frac{\pi}{2} \text{ or } -\frac{\pi}{2}. \tag{1.109} \]

We thus have the intriguing possibility See that the matrix elements of S_x and S_y cannot all be real. If the S_x matrix elements are real, the S_y matrix elements must be purely imaginary (and vice versa). Just from this extremely simple example, the introduction of complex numbers is seen to be an essential feature in quantum mechanics. It is convenient to take the S_x matrix elements to be real 14 and set δ_1 = 0; if we were to choose δ_1 = π, the positive x-axis would be oriented in the opposite direction. The second phase angle δ_2 must then be −π/2 or π/2. The fact that there is still an ambiguity of this kind is not surprising. We have not yet specified whether the coordinate system we are using is right-handed or left-handed; given the x- and the z-axes there is still a twofold ambiguity in the choice of the positive y-axis. Later we will discuss angular momentum as a generator of rotations using the right-handed coordinate system; it can then be shown that δ_2 = π/2 is the correct choice.

To summarize, we have |S_x; ±⟩ = (1/√2) (|+⟩ ± |−⟩), (1.110a)

|S_y; ±⟩ = (1/√2) (|+⟩ ± i |−⟩), (1.110b)

14 This can always be done by adjusting arbitrary phase factors in the definition of |+⟩ and |−⟩. This point will become clearer in Chapter 3, where the behavior of |±⟩ under rotations will be discussed.

S_x = (ℏ/2) [(|+⟩⟨−|) + (|−⟩⟨+|)], (1.111a)

S_y = (ℏ/2) [−i(|+⟩⟨−|) + i(|−⟩⟨+|)]. (1.111b)

The S_x ± and S_y ± eigenkets given here are seen to be in agreement with our earlier guesses (1.9) and (1.14) based on an analogy with linearly and circularly polarized light. (Note, in this comparison, that only the relative phase between the |+⟩ and ⟨−| components is of physical significance.) Furthermore, the non-Hermitian S± operators defined by (1.92) can now be written as S± = S_x ± i S_y. (1.112)

The operators S_x and S_y, together with S_z given earlier, can be readily shown to satisfy the commutation relations [S_i, S_j] = i ε_{ijk} ℏ S_k, (1.113)

and the anticommutation relations {S_i, S_j} = ℏ^2 δ_{ij}, (1.114)

where the commutator [,] and the anticommutator {,} are defined by [A, B] ≡ AB − BA, (1.115a)

{A, B} ≡ AB + BA. (1.115b)

(We make use of the totally antisymmetric symbol ε_{ijk} which has the value +1 for ε_{123} and any cyclic permutation of indices, the value −1 for ε_{213} and any cyclic permutation of indices, and the value 0 when any two indices are the same. We also make use of the implied summation convention, that is the assumption that we perform a summation over any pair of repeated indices.) The commutation relations in (1.113) will be recognized as the simplest realization of the angular-momentum commutation relations, whose significance will be discussed in detail in Chapter 3. In contrast, the anticommutation relations in (1.114) turn out to be a special property of spin 1 systems.

We can also define the operator S·S, or S^2 for short, as follows: S^2 ≡ S_x^2 + S_y^2 + S_z^2. (1.116)

Because of (1.114), this operator turns out to be just a constant multiple of the identity operator S^2 = (3/4) ℏ^2. (1.117)

We obviously have [S^2, S] = 0. (1.118)

As will be shown in Chapter 3, for spins higher than 1, S^2 is no longer a multiple of the identity operator; however, (1.118) still holds.

1.4.3 Compatible Observables Returning now to the general formalism, we will discuss compatible versus incompatible observables. Observables A and B are defined to be compatible when the corresponding operators commute, [A, B] = 0, (1.119)

and incompatible when [A, B] ≠ 0. (1.120)

For example, S^2 and S_z are compatible observables, while S_x and S_z are incompatible observables.

Let us first consider the case of compatible observables A and B. As usual, we assume that the ket space is spanned by the eigenkets of A. We may also regard the same ket space as being spanned by the eigenkets of B. We now ask: How are the A eigenkets related to the B eigenkets when A and B are compatible observables?

Before answering this question we must touch upon a very important point we have bypassed earlier, the concept of degeneracy. Suppose there are two (or more) linearly independent eigenkets of A having the same eigenvalue; then the eigenvalues of the two eigenkets are said to be degenerate. In such a case the notation |a'⟩ that labels the eigenket by its eigenvalue alone does not give a complete description; furthermore, we may recall that our earlier theorem on the orthogonality of different eigenkets was proved under the assumption of no degeneracy. Even worse, the whole concept that the ket space is spanned by {|a'⟩} appears to run into difficulty when the dimensionality of the ket space is larger than the number of distinct eigenvalues of A. Fortunately, in practical applications in quantum mechanics, it is usually the case that in such a situation the eigenvalues of some other commuting observable, say B, can be used to label the degenerate eigenkets.

Now we are ready to state an important theorem.

Theorem 2 Suppose that A and B are compatible observables, and the eigenvalues of A are nondegenerate. Then the matrix elements ⟨a''|B|a'⟩ are all diagonal. (Recall here that the matrix elements of A are already diagonal if {|a'⟩} are used as the base kets.)

Proof The proof of this important theorem is extremely simple. Using the definition (1.119) of compatible observables, we observe that ⟨a''|[A, B]|a'⟩ = (a'' − a') ⟨a''|B|a'⟩ = 0. (1.121)

So ⟨a''|B|a'⟩ must vanish unless a' = a'', which proves our assertion.

We can write the matrix elements of B as ⟨a''|B|a'⟩ = δ_{a'a''} ⟨a'|B|a'⟩. (1.122)

So both A and B can be represented by diagonal matrices with the same set of base kets. Using (1.71) and (1.122) we can write B as B = Σ_{a'} |a'⟩ ⟨a'|B|a'| ⟨a'|. (1.123)

Suppose that this operator acts on an eigenket of A: B|a'⟩ = Σ_{a''} |a''⟩ ⟨a''|B|a''⟩ ⟨a''|a'⟩ = (⟨a'|B|a'|) |a'⟩. (1.124)

But this is nothing other than the eigenvalue equation for the operator B with eigenvalue b' ≡ ⟨a'|B|a'⟩. (1.125)

The ket |a'⟩ is therefore a simultaneous eigenket of A and B. Just to be impartial to both operators, we may use |a', b'⟩ to characterize this simultaneous eigenket.

We have seen that compatible observables have simultaneous eigenkets. Even though the proof given is for the case where the A eigenkets are nondegenerate, the statement holds even if there is an n-fold degeneracy, that is, A|a'^(i)⟩ = a'|a'^(i)⟩ for i = 1, 2, ..., n (1.126)

where |a'^(i)⟩ are n mutually orthonormal eigenkets of A, all with the same eigenvalue a'. To see this, all we need to do is construct appropriate linear combinations of |a'^(i)⟩ that diagonalize the B operator by following the diagonalization procedure to be discussed in Section 1.5.

A simultaneous eigenket of A and B, denoted by |a', b'⟩, has the property A|a', b'⟩ = a'|a', b'⟩, (1.127a)

B|a', b'⟩ = b'|a', b'⟩. (1.127b)

When there is no degeneracy, this notation is somewhat superfluous because it is clear from (1.125) that if we specify a', we necessarily know the b' that appears in |a', b'⟩. The notation |a', b'⟩ is much more powerful when there are degeneracies. A simple example may be used to illustrate this point.

Even though a complete discussion of orbital angular momentum will not appear in this book until Chapter 3, the reader may be familiar from his or her earlier training in elementary wave mechanics that the eigenvalues of L^2 (orbital angular momentum squared) and L_z (the z-component of orbital angular momentum) are ℏ^2 l(l+1) and m ℏ, respectively, with l an integer and m = −l, −l+1, ..., +l. To characterize an orbital angular momentum state completely, it is necessary to specify both l and m. For example, if we just say l = 1, the m value can still be 0, +1, or −1; if we just say m = 1, l can be 1, 2, 3, 4, and so on. Only by specifying both l and m do we succeed in uniquely characterizing the orbital angular momentum state in question. Quite often a collective index K' is used to stand for (a', b'), so that |K'⟩ = |a', b'⟩. (1.128)

We can obviously generalize our considerations to a situation where there are several (more than two) mutually compatible observables, namely, [A, B] = [B, C] = [A, C] = ··· = 0. (1.129)

Assume that we have found a maximal set of commuting observables; that is, we cannot add any more observables to our list without violating (1.129). The eigenvalues of individual operators A, B, C, ... may have degeneracies, but if we specify a combination (a', b', c', ...), then the corresponding simultaneous eigenket of A, B, C, ... is uniquely specified. We can again use a collective index K' to stand for (a', b', c', ...). The orthonormality relation for |K'⟩ = |a', b', c', ...⟩ (1.130)

reads ⟨K''|K'⟩ = δ_{K'K''} = δ_{aa''} δ_{bb''} δ_{cc''}..., (1.131)

while the completeness relation, or closure, can be written as Σ_{K'} |K'⟩⟨K'| = Σ_{a'} Σ_{b'} Σ_{c'} ... |a', b', c', ...⟩⟨a', b', c', ...| = 1. (1.132)

We now consider measurements of A and B when they are compatible observables. Suppose we measure A first and obtain result a'. Subsequently, we may measure B and get result b'. Finally we measure A again. It follows from our measurement formalism that the third measurement always gives a' with certainty, that is, the second (B) measurement does not destroy the previous information obtained in the first (A) measurement. This is rather obvious when the eigenvalues of A are nondegenerate: |α⟩ − A − measurement → |a', b'⟩ − B − measurement → |a', b'⟩ − A − measurement → a' with certainty.

When there is degeneracy, the argument goes as follows: After the first (A) measurement, which yields a′, the system is thrown into some linear combination ∑_{i} c(i)|a′, b(i)⟩, (1.134) where n is the degree of degeneracy and the kets |a′, b(i)⟩ all have the same eigenvalue a′ as far as operator A is concerned. The second (B) measurement may select just one of the terms in the linear combination (1.134), say, |a′, b(j)⟩, but the third (A) measurement applied to it still yields a′. Whether or not there is degeneracy, A measurements and B measurements do not interfere. The term compatible is indeed deemed appropriate.

1.4.4 Incompatible Observables

We now turn to incompatible observables, which are more nontrivial. The first point to be emphasized is that incompatible observables do not have a complete set of simultaneous eigenkets. To show this let us assume the converse to be true. There would then exist a set of simultaneous eigenkets with property (1.127a) and (1.127b). Clearly, AB|a′, b′⟩ = A b′|a′, b′⟩ = a′ b′|a′, b′⟩. (1.135) Likewise, BA|a′, b′⟩ = B a′|a′, b′⟩ = a′ b′|a′, b′⟩ mean an operator fulfilling the conditions U†U=1  (1.158)

as well as UU†=1.  (1.159)

Proof: We prove this theorem by explicit construction. We assert that the operator U= ∑|b(k)⟩⟨a(k)|  (1.160)

will do the job and we apply this U to |a(l)⟩. Clearly, U|a(l)⟩=|b(l)⟩  (1.161)

is guaranteed by the orthonormality of {|a(α)⟩}. Furthermore, U is unitary: U†U= ∑_k ∑_l |a(l)⟩⟨b(l)|b(k)⟩⟨a(k)|= ∑_k |a(k)⟩⟨a(k)|=1,  (1.162)

where we have used the orthonormality of {|b(β)⟩} and the completeness of {|a(α)⟩}. We obtain relation (1.159) in an analogous manner. □

1.5.2 Transformation Matrix It is instructive to study the matrix representation of the U operator in the old {|a(α)⟩} basis. We have ⟨a(k)|U|a(l)⟩=⟨a(k)|b(l)⟩,  (1.163)

which is obvious from (1.161). In other words, the matrix elements of the U operator are built up of the inner products of old base bras and new base kets. We recall that the rotation matrix in three dimensions that changes one set of unit base vectors (x̂, ŷ, ẑ) into another set (x̂', ŷ', ẑ') can be written as (Goldstein et al. (2002), pp. 134–144 for example)

R = ⎛ ⎞ ⎝ x̂·x̂'  x̂·ŷ'  x̂·ẑ' ⎠ ŷ·x̂'  ŷ·ŷ'  ŷ·ẑ'   .  (1.164)

ẑ·x̂'  ẑ·ŷ'  ẑ·ẑ'

The square matrix made up of ⟨a(k)|U|a(l)⟩ is referred to as the transformation matrix from the {|a(α)⟩} basis to the {|b(β)⟩} basis.

Given an arbitrary ket |α⟩ whose expansion coefficients ⟨a(α)|α⟩ are known in the old basis, |α⟩= ∑_α |a(α)⟩⟨a(α)|α⟩,  (1.165)

how can we obtain ⟨b(β)|α⟩, the expansion coefficients in the new basis? The answer is very simple: Just multiply (1.165) (with α replaced by a(l) to avoid confusion) by ⟨b(k)|: ⟨b(k)|α⟩= ∑_l ⟨b(k)|a(l)⟩⟨a(l)|α⟩= ∑_l ⟨a(k)|U†|a(l)⟩⟨a(l)|α⟩.  (1.166)

In matrix notation, (1.166) states that the column matrix for |α⟩ in the new basis can be obtained just by applying the square matrix U† to the column matrix in the old basis: (new) = (U†)(old).  (1.167)

The relationships between the old matrix elements and the new matrix elements are also easy to obtain: ⟨b(k)|X|b(l)⟩= ∑_m ∑_n ⟨b(k)|a(m)⟩⟨a(m)|X|a(n)⟩⟨a(n)|b(l)⟩ = ∑_m ∑_n ⟨a(k)|U†|a(m)⟩⟨a(m)|X|a(n)⟩⟨a(n)|U|a(l)⟩.  (1.168)

This is simply the well-known formula for a similarity transformation in matrix algebra, X' = U†XU.  (1.169)

The trace of an operator X is defined as the sum of diagonal elements: tr(X)= ∑_α ⟨a(α)|X|a(α)⟩.  (1.170)

Even though a particular set of base kets is used in the definition, tr(X) turns out to be independent of representation, as shown: ∑_α ⟨a(α)|X|a(α)⟩ = ∑_α ∑_β ∑_β' ⟨a(α)|b(β)⟩⟨b(β)|X|b(β')⟩⟨b(β')|a(α)⟩ = ∑_β ∑_β' ⟨b(β')|b(β)⟩⟨b(β)|X|b(β')⟩ = ∑_β ⟨b(β)|X|b(β)⟩.  (1.171)

We can also prove tr(XY)=tr(YX),  (1.172a)

tr(U†XU)=tr(X),  (1.172b)

tr(|a(α)⟩⟨a(α')|)=δ_{αα'},  (1.172c)

tr(|b(β)⟩⟨a(α)|)=⟨a(α)|b(β)⟩.  (1.172d)

1.5.3 Diagonalization So far we have not discussed how to find the eigenvalues and eigenkets of an operator B whose matrix elements in the old {|a(α)⟩} basis are assumed to be known. This problem turns out to be equivalent to that of finding the unitary matrix that diagonalizes B. Even though the reader may already be familiar with the diagonalization procedure in matrix algebra, it is worth working out this problem using the Dirac bra-ket notation.

We are interested in obtaining the eigenvalue b(β) and the eigenket |b(β)⟩ with the property B|b(β)⟩=b(β)|b(β)⟩.  (1.173)

First, we rewrite this as ∑_α ⟨a(α')|B|a(α)⟩⟨a(α)|b(β)⟩=b(β)⟨a(α')|b(β)⟩.  (1.174)

When |b(β)⟩ in (1.173) stands for the l-th eigenket of operator B, we can write (1.174) in matrix notation as follows: ⎛ ⎞⎛ ⎞   ⎛ ⎞ B₁₁ B₁₂ B₁₃ ... ⎜C₁(l)⎟   ⎜C₁(l)⎟ ⎜B₂₁ B₂₂ B₂₃ ... ⎟⎜C₂(l)⎟=b(l)⎜C₂(l)⎟,  (1.175)

⎝B₃₁ B₃₂ B₃₃ ... ⎠⎝C₃(l)⎠   ⎝C₃(l)⎠ .   .   .   . . ... .   .   . .

with B_ij =⟨a(i)|B|a(j)⟩,  (1.176a)

and C(l) =⟨a(k)|b(l)⟩,  (1.176b)

where i, j, k run up to N, the dimensionality of the ket space. As we know from linear algebra, nontrivial solutions for C(l) are possible only if the characteristic equation det(B−λI)=0  (1.177)

is satisfied. This is an N-th order algebraic equation for λ, and the N roots obtained are to be identified with the various b(l) we are trying to determine. Knowing b(l) we can solve for the corresponding C(l) up to an overall constant to be determined from the normalization condition. Comparing (1.176b) with (1.163), we see that the C(l) are just the elements of the unitary matrix involved in the change of basis {|a(α)⟩} → {|b(β)⟩}.

For this procedure the Hermiticity of B is important. For example, consider S₊ defined by (1.92) or (1.112). This operator is obviously non-Hermitian. The corresponding matrix, which reads in the S_z basis as S₊ = ħ ⎛ 0 1 ⎞ ,  (1.178)

⎝ 0 0 ⎠ cannot be diagonalized by any unitary matrix. In Chapter 2 we will encounter eigenkets of a non-Hermitian operator in connection with a coherent state of a simple harmonic oscillator. Such eigenkets, however, are known not to form a complete orthonormal set, and the formalism we have developed in this section cannot be immediately applied.

1.5.4 Unitary Equivalent Observables We conclude this section by discussing a remarkable theorem on the unitary transform of an observable.

Theorem 4: Consider again two sets of orthonormal basis {|a(α)⟩} and {|b(β)⟩} connected by the U operator (1.160). Knowing U, we may construct a unitary transform of A, UAU⁻¹; then A and UAU⁻¹ are said to be unitary equivalent observables. The eigenvalue equation for A, A|a(l)⟩=a(l)|a(l)⟩,  (1.179)

clearly implies that UAU⁻¹U|a(l)⟩=a(l)U|a(l)⟩.  (1.180)

But this can be rewritten as (UAU⁻¹)|b(l)⟩=a(l)|b(l)⟩.  (1.181)

This deceptively simple result is quite profound. It tells us that the |b(β)⟩ are eigenkets of UAU⁻¹ with exactly the same eigenvalues as the A eigenvalues. In other words, unitary equivalent observables have identical spectra.

The eigenket |b(l)⟩, by definition, satisfies the relationship B|b(l)⟩=b(l)|b(l)⟩.  (1.182)

Comparing (1.181) and (1.182), we infer that B and UAU⁻¹ are simultaneously diagonalizable.

A natural question is, is UAU⁻¹ the same as B itself? The answer quite often is yes in cases of physical interest. Take, for example, S_x and S_z. They are related by a unitary operator, which, as we will discuss in Chapter 3, is actually the rotation operator around the y-axis by angle π/2. In this case S_x itself is the unitary transform of S_z. Because we know that S_x and S_z exhibit the same set of eigenvalues, namely, +ħ/2 and −ħ/2, we see that our theorem holds in this particular example.

## 1.6 Position, Momentum, and Translation

1.6.1 Continuous Spectra The observables considered so far have all been assumed to exhibit discrete eigenvalue spectra. In quantum mechanics, however, there are observables with continuous eigenvalues.

Take, for instance, p_z, the z-component of momentum. In quantum mechanics this is again represented by a Hermitian operator. In contrast to S_z, however, the eigenvalues of p_z (in appropriate units) can assume any real value between −∞ and ∞.

The rigorous mathematics of a vector space spanned by eigenkets that exhibit a continuous spectrum is rather treacherous. The dimensionality of such a space is obviously infinite.

Fortunately, many of the results we worked out for a finite-dimensional vector space with discrete eigenvalues can immediately be generalized. In places where straightforward generalizations do not hold, we indicate danger signals.

We start with the analogue of eigenvalue equation (1.19), which, in the continuous spectrum case, is written as ξ|ξ'⟩=ξ'|ξ'⟩,  (1.183)

where ξ is an operator and ξ' is simply a number. The ket |ξ'⟩ is, in other words, an eigenket of operator ξ with eigenvalue ξ', just as |a(α)⟩ is an eigenket of operator A with eigenvalue a(α).

In pursuing this analogy we replace the Kronecker symbol by Dirac's δ-function, a discrete sum over the eigenvalues {a(α)} by an integral over the continuous variable ξ', so ⟨a(α)|a(α')⟩=δ_{αα'} → ⟨ξ'|ξ''⟩=δ(ξ'−ξ''),  (1.184a)

∑_α |a(α)⟩⟨a(α)|=1 → ∫dξ' |ξ'⟩⟨ξ'|=1,  (1.184b)

|α⟩= ∑_α |a(α)⟩⟨a(α)|α⟩ → |α⟩= ∫dξ' |ξ'⟩⟨ξ'|α⟩,  (1.184c)

∑_α |⟨a(α)|α⟩|²=1 → ∫dξ' |⟨ξ'|α⟩|²=1,  (1.184d)

⟨β|α⟩= ∑_α ⟨β|a(α)⟩⟨a(α)|α⟩ → ⟨β|α⟩= ∫dξ' ⟨β|ξ'⟩⟨ξ'|α⟩,  (1.184e)

⟨a(α')|A|a(α)⟩=a(α)δ_{αα'} → ⟨ξ''|ξ|ξ'⟩=ξ'δ(ξ''−ξ').  (1.184f)

Notice in particular how the completeness relation (1.184b) is used to obtain (1.184c) and (1.184e).

1.6.2 Position Eigenkets and Position Measurements In Section 1.4 we emphasized that a measurement in quantum mechanics is essentially a filtering process. To extend this idea to measurements of observables exhibiting continuous spectra it is best to work with a specific example. To this end we consider the position (or coordinate) operator in one dimension.

The eigenkets |x'⟩ of the position operator x satisfying x|x'⟩=x'|x'⟩  (1.185)

are postulated to form a complete set. Here x' is just a number with the dimen Section of length 0.23 cm, for example, while x is an operator. The state ket for an arbitrary physical state can be expanded in terms of {|x⟩}:

|α⟩ = ∫ dx′ |x′⟩⟨x′|α⟩. (1.186)

We now consider a highly idealized selective measurement of the position observable. Suppose we place a very tiny detector that clicks only when the particle is precisely at x′ and nowhere else. Immediately after the detector clicks, we can say that the state in question is represented by |x′⟩. In other words, when the detector clicks, |α⟩ abruptly “jumps into” |x′⟩ in much the same way as an arbitrary spin state jumps into the S_z+ (or S_z−) state when subjected to an SG apparatus of the S_z type.

In practice the best the detector can do is to locate the particle within a narrow interval around x′. A realistic detector clicks when a particle is observed to be located within some narrow range (x′ − Δ/2, x′ + Δ/2). When a count is registered in such a detector, the state ket changes abruptly as follows:

|α⟩ = ∫_{-∞}^{∞} dx′′ |x′′⟩⟨x′′|α⟩ --measurement--> ∫_{x′-Δ/2}^{x′+Δ/2} dx′′ |x′′⟩⟨x′′|α⟩. (1.187)

Assuming that ⟨x′′|α⟩ does not change appreciably within the narrow interval, the probability for the detector to click is given by

|⟨x′|α⟩|² dx′, (1.188)

where we have written dx′ for Δ. This is analogous to |⟨a′|α⟩|² for the probability for |α⟩ to be thrown into |a′⟩ when A is measured. The probability of recording the particle somewhere between −∞ and ∞ is given by

∫_{-∞}^{∞} dx′ |⟨x′|α⟩|², (1.189)

which is normalized to unity if |α⟩ is normalized:

⟨α|α⟩ = 1 ⇒ ∫_{-∞}^{∞} dx′ ⟨α|x′⟩⟨x′|α⟩ = 1. (1.190)

The reader familiar with wave mechanics may have recognized by this time that ⟨x′|α⟩ is the wave function for the physical state represented by |α⟩. We will say more about this identification of the expansion coefficient with the x-representation of the wave function in Section 1.7.

The notion of a position eigenket can be extended to three dimensions. It is assumed in nonrelativistic quantum mechanics that the position eigenkets |x′⟩ are complete. The state ket for a particle with internal degrees of freedom, such as spin, ignored can therefore be expanded in terms of {|x′⟩} as follows:

|α⟩ = ∫ d³x′ |x′⟩⟨x′|α⟩, (1.191)

where x′ stands for x′, y′, and z′; in other words, |x′⟩ is a simultaneous eigenket of the observables x, y, and z in the sense of Section 1.4:

|x′⟩ ≡ |x′, y′, z′⟩, (1.192a)

x|x′⟩ = x′|x′⟩, y|x′⟩ = y′|x′⟩, z|x′⟩ = z′|x′⟩. (1.192b)

To be able to consider such a simultaneous eigenket at all, we are implicitly assuming that the three components of the position vector can be measured simultaneously to arbitrary degrees of accuracy; hence, we must have

[x_i, x_j] = 0, (1.193)

where x_1, x_2, and x_3 stand for x, y, and z, respectively.

1.6.3 Translation

We now introduce the very important concept of translation, or spatial displacement. Suppose we start with a state that is well localized around x′. Let us consider an operation that changes this state into another well-localized state, this time around x′ + dx′ with everything else (for example, the spin direction) unchanged. Such an operation is defined to be an infinitesimal translation by dx′, and the operator that does the job is denoted by J(dx′):

J(dx′)|x′⟩ = |x′ + dx′⟩, (1.194)

where a possible arbitrary phase factor is set to unity by convention. Notice that the right-hand side of (1.194) is again a position eigenket, but this time with eigenvalue x′ + dx′. Obviously |x′⟩ is not an eigenket of the infinitesimal translation operator.

By expanding an arbitrary state ket |α⟩ in terms of the position eigenkets we can examine the effect of infinitesimal translation on |α⟩:

|α⟩ → J(dx′)|α⟩ = J(dx′) ∫ d³x′ |x′⟩⟨x′|α⟩ = ∫ d³x′ |x′ + dx′⟩⟨x′|α⟩. (1.195)

We also write the right-hand side of (1.195) as

∫ d³x′ |x′ + dx′⟩⟨x′|α⟩ = ∫ d³x′ |x′⟩⟨x′ − dx′|α⟩ (1.196)

because the integration is over all space and x′ is just an integration variable. This shows that the wave function of the translated state J(dx′)|α⟩ is obtained by substituting x′ − dx′ for x′ in ⟨x′|α⟩.

There is an equivalent approach to translation that is often treated in the literature. Instead of considering an infinitesimal translation of the physical system itself, we consider a change in the coordinate system being used such that the origin is shifted in the opposite direction, −dx′. Physically, in this alternative approach we are asking how the same state ket would look to another observer whose coordinate system is shifted by −dx′. In this book we try not to use this approach. Obviously it is important that we do not mix the two approaches!

We now list the properties of the infinitesimal translation operator J(dx′). The first property we demand is the unitarity property imposed by probability conservation. It is reasonable to require that if the ket |α⟩ is normalized to unity, the translated ket J(dx′)|α⟩ also be normalized to unity, so

⟨α|α⟩ = ⟨α|J†(dx′) J(dx′)|α⟩. (1.197)

This condition is guaranteed by demanding that the infinitesimal translation be unitary:

J†(dx′) J(dx′) = 1. (1.198)

Quite generally, the norm of a ket is preserved under unitary transformations. For the second property, suppose we consider two successive infinitesimal translations, first by dx′ and subsequently by dx′′, where dx′ and dx′′ need not be in the same direction. We expect the net result to be just a single translation operation by the vector sum dx′ + dx′′, so we demand that

J(dx′′) J(dx′) = J(dx′ + dx′′). (1.199)

For the third property, suppose we consider a translation in the opposite direction; we expect the opposite-direction translation to be the same as the inverse of the original translation:

J(−dx′) = J⁻¹(dx′). (1.200)

For the fourth property, we demand that as dx′ → 0, the translation operation reduce to the identity operation

lim_{dx′→0} J(dx′) = 1 (1.201)

and that the difference between J(dx′) and the identity operator be of first order in dx′.

We now demonstrate that if we take the infinitesimal translation operator to be

J(dx′) = 1 − i K · dx′, (1.202)

where the components of K, K_x, K_y, and K_z, are Hermitian operators, then all the properties listed are satisfied. The first property, the unitarity of J(dx′), is checked as follows:

J†(dx′) J(dx′) = (1 + i K†·dx′)(1 − i K·dx′)

= 1 − i (K − K†)·dx′ + O[(dx′)²]

≈ 1, (1.203)

where terms of second order in dx′ have been ignored for an infinitesimal translation. The second property (1.199) can also be proved as follows:

J(dx′′) J(dx′) = (1 − i K·dx′′)(1 − i K·dx′)

≈ 1 − i K·(dx′ + dx′′)

= J(dx′ + dx′′). (1.204)

The third and fourth properties are obviously satisfied by (1.202).

Accepting (1.202) to be the correct form for J(dx′), we are in a position to derive an extremely fundamental relation between the K operator and the x operator. First, note that

x J(dx′) |x′⟩ = x |x′ + dx′⟩ = (x′ + dx′) |x′ + dx′⟩ (1.205a)

and

J(dx′) x |x′⟩ = x′ J(dx′) |x′⟩ = x′ |x′ + dx′⟩; (1.205b)

hence,

[x, J(dx′)] |x′⟩ = dx′ |x′ + dx′⟩ ≈ dx′ |x′⟩, (1.206)

where the error made in writing the last part of (1.206) is of second order in dx′. Now |x′⟩ can be any position eigenket, and the position eigenkets are known to form a complete set. We must therefore have an operator identity

[x, J(dx′)] = dx′, (1.207)

or

−i x K·dx′ + i K·dx′ x = dx′, (1.208)

where on the right-hand sides of (1.207) and (1.208) dx′ is understood to be the number dx′ multiplied by the identity operator in the ket space spanned by |x′⟩. By choosing dx′ in the direction of x̂_j and forming the scalar product with x̂_i, we obtain

[x_i, K_j] = i δ_{ij}, (1.209)

where again δ_{ij} is understood to be multiplied by the identity operator.

1.6.4 Momentum as a Generator of Translation

Equation (1.209) is the fundamental commutation relation between the position operators x, y, z and the K operators K_x, K_y, K_z. Remember that so far the K operator is defined in terms of the infinitesimal translation operator by (1.202). What is the physical significance we can attach to K?

J. Schwinger, lecturing on quantum mechanics, once remarked, “… for fundamental properties we will borrow only names from classical physics.” In the present case we would like to borrow from classical mechanics the notion that momentum is the generator of an infinitesimal translation. An infinitesimal translation in classical mechanics can be regarded as a canonical transformation,

x_new ≡ X = x + dx, p_new ≡ P = p, (1.210)

obtainable from the generating function (Goldstein et al. (2002), pp. 386 and 403)

F(x, P) = x · P + p · dx, (1.211)

where p and P refer to the corresponding momenta.

This equation has a striking similarity to the infinitesimal translation operator (1.202) in quantum mechanics, particularly if we recall that x·P in (1.211) is the generating function for the identity transformation (X = x, P = p). We are therefore led to speculate that the operator K is in some sense related to the momentum operator in quantum mechanics.

Can the K operator be identified with the momentum operator?

to itself? Unfortunately the dimension is all wrong; the K operator has the dimension of 1/length because K·dx must be dimensionless. But it appears legitimate to set K = (1.212) universal constant with the dimension of action. From the fundamental postulates of quantum mechanics there is no way to determine the actual numerical value of the universal constant. Rather, this constant is needed here because, historically, classical physics was developed before quantum mechanics using units convenient for describing macroscopic quantities – the circumference of the Earth, the mass of 1cm3 of water, the duration of a mean solar day, and so forth. Had microscopic physics been formulated before macroscopic physics, the physicists would have almost certainly chosen the basic units in such a way that the universal constant appearing in (1.212) would be unity.

An analogy from electrostatics may be helpful here. The interaction energy between two particles of charge e separated at a distance r is proportional to e^2/r; in unrationalized Gaussian units, the proportionality factor is just 1, but in rationalized mks units, which may be convenient for electrical engineers, the proportionality factor is 1/4πε. (See Appendix A.) The universal constant that appears in (1.212) turns out to be the same as the constant ħ that appears in L. de Broglie’s relation, written in 1924, λ = 2πħ/p, (1.213) where λ is the wavelength of a “particle wave.” In other words, the K operator is the quantum-mechanical operator that corresponds to the wave number, that is, 2π times the reciprocal wavelength, usually denoted by k. With this identification the infinitesimal translation operator J(dx) reads J(dx) = 1 − ip·dx/ħ, (1.214) where p is the momentum operator. The commutation relation (1.209) now becomes [x_i, p_j] = iħδ_{ij}. (1.215)

The commutation relations (1.215) imply, for example, that x and p_x (but not x and p_y) are incompatible observables. It is therefore impossible to find simultaneous |α⟩ are often presented as separate postulates. One of the major advantages of our formalism, originally due to Dirac, is that the two kinds of probabilistic interpretations are unified; ψα(x′) is an expansion coefficient [see (1.235)] in much the same way as ca′ is. By following the footsteps of Dirac we come to appreciate the unity of quantum mechanics.

Consider the inner product ⟨β|α⟩. Using the completeness of |x′⟩, we have

∫ dx′ ⟨β|x′⟩⟨x′|α⟩ = ∫ dx′ ψ*β(x′) ψα(x′), (1.238)

so ⟨β|α⟩ characterizes the overlap between the two wave functions. Note that we are not defining ⟨β|α⟩ as the overlap integral; the identification of ⟨β|α⟩ with the overlap integral follows from our completeness postulate for |x′⟩. The more general interpretation of ⟨β|α⟩, independent of representations, is that it represents the probability amplitude for state |α⟩ to be found in state |β⟩.

This time let us interpret the expansion

|α⟩ = ∑ |a′⟩⟨a′|α⟩ (1.239)

a′

using the language of wave functions. We just multiply both sides of (1.239) by the position eigenbra ⟨x′| on the left. Thus

⟨x′|α⟩ = ∑ ⟨x′|a′⟩⟨a′|α⟩. (1.240)

a′

In the usual notation of wave mechanics this is recognized as

ψα(x′) = ∑ ca′ ua′(x′),

a′

where we have introduced an eigenfunction of operator A with eigenvalue a′:

ua′(x′) = ⟨x′|a′⟩. (1.241)

Let us now examine how ⟨β|A|α⟩ can be written using the wave functions for |α⟩ and |β⟩. Clearly, we have

∫ dx′ ∫ dx″ ⟨β|x′⟩⟨x′|A|x″⟩⟨x″|α⟩ = ∫ dx′ ∫ dx″ ψ*β(x′) ⟨x′|A|x″⟩ ψα(x″). (1.242)

So to be able to evaluate ⟨β|A|α⟩, we must know the matrix element ⟨x′|A|x″⟩, which is, in general, a function of the two variables x′ and x″.

An enormous simplification takes place if observable A is a function of the position operator x. In particular, consider

A = x², (1.243)

which actually appears in the Hamiltonian for the simple harmonic oscillator problem to be discussed in Chapter 2. We have

⟨x′|x²|x″⟩ = (⟨x′|) · (x″²|x″⟩) = x′² δ(x′ − x″), (1.244)

where we have used (1.233) and (1.234). The double integral (1.242) is now reduced to a single integral:

⟨β|x²|α⟩ = ∫ dx′ ⟨β|x′⟩ x′² ⟨x′|α⟩ = ∫ dx′ ψ*β(x′) x′² ψα(x′). (1.245)

In general,

⟨β|f(x)|α⟩ = ∫ dx′ ψ*β(x′) f(x′) ψα(x′). (1.246)

Note that the f(x) on the left-hand side of (1.246) is an operator, while the f(x′) on the right-hand side is not an operator.

1.7.2 Momentum Operator in the Position Basis

We now examine how the momentum operator may look in the x-basis, that is, in the representation where the position eigenkets are used as base kets. Our starting point is the definition of momentum as the generator of infinitesimal translations:

|α⟩ = dx′ J(Δx′) |x′⟩⟨x′|α⟩ = dx′ |x′ + Δx′⟩⟨x′|α⟩ = dx′ |x′⟩⟨x′ − Δx′|α⟩ = dx′ |x′⟩ (⟨x′|α⟩ − Δx′ ∂/∂x′ ⟨x′|α⟩). (1.247)

Comparison of both sides yields

p|α⟩ = dx′ |x′⟩ (−iħ ∂/∂x′) ⟨x′|α⟩ (1.248)

or

⟨x′|p|α⟩ = −iħ (∂/∂x′) ⟨x′|α⟩, (1.249)

where we have used the orthogonality property (1.234). For the matrix element p in the x-representation, we obtain

⟨x′|p|x″⟩ = −iħ δ(x′ − x″). (1.250)

From (1.248) we get a very important identity:

⟨β|p|α⟩ = ∫ dx′ ⟨β|x′⟩ (−iħ ∂/∂x′) ⟨x′|α⟩ = ∫ dx′ ψ*β(x′) (−iħ ∂/∂x′) ψα(x′). (1.251)

In our formalism (1.251) is not a postulate; rather, it has been derived using the basic properties of momentum. By repeatedly applying (1.249), we can also obtain

⟨x′|pⁿ|α⟩ = (−iħ)ⁿ (∂ⁿ/∂x′ⁿ) ⟨x′|α⟩, (1.252)

⟨β|pⁿ|α⟩ = ∫ dx′ ψ*β(x′) (−iħ)ⁿ (∂ⁿ/∂x′ⁿ) ψα(x′). (1.253)

1.7.3 Momentum-Space Wave Function

So far we have worked exclusively in the x-basis. There is actually a complete symmetry between x and p, apart from occasional minus signs, which we can infer from the canonical commutation relations. Let us now work in the p-basis, that is, in the momentum representation.

For simplicity we continue working in one-space. The base eigenkets in the p-basis specify

p|p′⟩ = p′|p′⟩ (1.254)

and

⟨p′|p″⟩ = δ(p′ − p″). (1.255)

The momentum eigenkets {|p′⟩} span the ket space in much the same way as the position eigenkets {|x′⟩}. An arbitrary state ket |α⟩ can therefore be expanded as follows:

|α⟩ = dp′ |p′⟩⟨p′|α⟩. (1.256)

We can give a probabilistic interpretation for the expansion coefficient ⟨p′|α⟩; the probability that a measurement of p gives eigenvalue p′ within a narrow interval dp′ is |⟨p′|α⟩|² dp′. It is customary to call ⟨p′|α⟩ the momentum-space wave function; the notation φα(p′) is often used:

⟨p′|α⟩ = φα(p′). (1.257)

If |α⟩ is normalized, we obtain

dp′ ⟨α|p′⟩⟨p′|α⟩ = dp′ |φα(p′)|² = 1. (1.258)

Let us now establish the connection between the x-representation and the p-representation. We recall that in the case of the discrete spectra, the change of basis from the old set {|a′⟩} to the new set {|b′⟩} is characterized by the transformation matrix (1.163). Likewise, we expect that the desired information is contained in ⟨x′|p′⟩, which is a function of x′ and p′, usually called the transformation function from the x-representation to the p-representation. To derive the explicit form of ⟨x′|p′⟩, first recall (1.249); letting |α⟩ be the momentum eigenket |p′⟩, we obtain

⟨x′|p|p′⟩ = −iħ (∂/∂x′) ⟨x′|p′⟩ (1.259)

or

p′ ⟨x′|p′⟩ = −iħ (∂/∂x′) ⟨x′|p′⟩. (1.260)

The solution to this differential equation for ⟨x′|p′⟩ is

⟨x′|p′⟩ = N exp(ip′x′/ħ), (1.261)

where N is the normalization constant to be determined in a moment. Even though the transformation function ⟨x′|p′⟩ is a function of two variables, x′ and p′, we can temporarily regard it as a function of x′ with p′ fixed. It can then be viewed as the probability amplitude for the momentum eigenstate specified by p′ to be found at position x′; in other words, it is just the wave function for the momentum eigenstate |p′⟩, often referred to as the momentum eigenfunction (still in the x-space). So (1.261) simply says that the wave function of a momentum eigenstate is a plane wave. It is amusing that we have obtained this plane wave solution without solving the Schrödinger equation (which we have not yet written down).

To get the normalization constant N let us first consider

⟨x′|x″⟩ = dp′ ⟨x′|p′⟩⟨p′|x″⟩. (1.262)

The left-hand side is just δ(x′ − x″); the right-hand side can be evaluated using the explicit form of ⟨x′|p′⟩:

δ(x′ − x″) = |N|² dp′ exp[ip′(x′ − x″)/ħ] = 2πħ |N|² δ(x′ − x″). (1.263)

Choosing N to be purely real and positive by convention, we finally have

⟨x′|p′⟩ = 1/√(2πħ) exp(ip′x′/ħ). (1.264)

We can now demonstrate how the position-space wave function is related to the momentum-space wave function. All we have to do is rewrite

⟨x′|α⟩ = dp′ ⟨x′|p′⟩⟨p′|α⟩ (1.265a)

and

⟨p′|α⟩ = dx′ ⟨p′|x′⟩⟨x′|α⟩ (1.265b)

as

ψα(x′) = 1/√(2πħ) dp′ exp(ip′x′/ħ) φα(p′) (1.266a)

and

φα(p′) = 1/√(2πħ) dx′ exp(−ip′x′/ħ) ψα(x′). (1.266b)

The pair of equations is just what one expects from Fourier’s inversion theorem. Apparently the mathematics we have developed somehow “knows” Fourier’s work on integral transforms.

1.7.4 Gaussian Wave Packets

It is instructive to look at a physical example to illustrate our basic formalism. We consider what is known as a Gaussian wave packet, whose x-space wave function is given by

⟨x′|α⟩ = 1/(π^{1/4} √d) exp(ikx′ − x′²/(2d²)). (1.267)

This is a plane wave with wavenumber k modulated by a Gaussian profile centered on the origin. The probability of observing the particle vanishes very rapidly for |x′| > d; more quantitatively, the probability d 密度|(cid:10)x(cid:5)|α(cid:8)|^2 具有宽度为 d 的高斯形状。我们现在计算 x、x^2、p 和 p^2 的期望值。由对称性可知，x 的期望值显然为零： ⟨x⟩ = ∫_{-∞}^{∞} dx ⟨α|x(x)⟨x|α⟩ = ∫_{-∞}^{∞} dx |⟨x|α⟩|^2 x = 0。 (1.268)

对于 x^2，我们得到 ⟨x^2⟩ = ∫_{-∞}^{∞} dx x^2 |⟨x|α⟩|^2 = (1/√π) ∫_{-∞}^{∞} dx x^2 exp(-x^2/d^2)

= d^2， (1.269)

这导致 (Δx)^2 = ⟨x^2⟩ - ⟨x⟩^2 = d^2， (1.270)

即位置算符的不确定度。p 和 p^2 的期望值也可以如下计算： ⟨p⟩ = ħ k， (1.271a)

⟨p^2⟩ = ħ^2/(2d^2) + ħ^2 k^2， (1.271b)

这留作练习。动量的不确定度因此由下式给出： (Δp)^2 = ⟨p^2⟩ - ⟨p⟩^2 = ħ^2/(2d^2)。 (1.272)

有了 (1.270) 和 (1.272)，我们可以检验海森堡不确定性关系 (1.216)；在这种情况下，不确定度积由下式给出： (Δx)^2 (Δp)^2 = ħ^2/2， (1.273)

与 d 无关，因此对于高斯波包，我们实际上得到一个等式关系，而非更一般性的不等式关系 (1.216)。因此，高斯波包常被称为最小不确定度波包。

现在我们转向动量空间。通过一个直接的积分，只需在指数中完成平方，我们得到 ⟨p|α⟩ = (1/√2πħ) * (1/π^{1/4}) * (1/√d) ∫_{-∞}^{∞} dx exp(ikx - x^2/(2d^2))

= √(d/ħπ) exp(-(p-ħk)^2 d^2/(2ħ^2))。 (1.274)

53 1.7 位置空间和动量空间中的波函数这个动量空间波函数提供了一种获得 ⟨p⟩ 和 ⟨p^2⟩ 的替代方法，这也留作练习。

找到具有动量 p 的粒子的概率在动量空间是高斯型的，以 ħk 为中心，正如找到粒子位于 x' 的概率在位置空间是高斯型的、以零为中心一样。此外，两个高斯的宽度彼此成反比，这只是表达不确定度积 ⟨(Δx)^2⟩⟨Δp^2⟩ 在 (1.273) 中显式计算的常数性的另一种方式。p 空间中的展宽越宽，x 空间中的展宽就越窄，反之亦然。

作为一个极端例子，假设我们让 d → ∞。位置空间波函数 (1.267) 随后变成一个延展到整个空间的平面波；找到粒子的概率只是常数，与 x' 无关。相反，动量空间波函数是 δ 函数型的，并在 ħk 处有一个尖锐的峰。在另一个极端，通过让 d→0，我们得到一个位置空间波函数像 δ 函数一样局域化，但动量空间波函数 (1.274) 只是常数，与 p' 无关。

我们已经看到，一个极其局域化的态（在 x 空间中）应被视为具有所有可能动量值的动量本征态的叠加。即使是那些动量可与 mc 相当或超过 mc 的动量本征态也必须包含在叠加中。然而，在如此高的动量值下，基于非相对论量子力学的描述注定会失效。18 尽管有这个限制，我们的形式体系，基于位置本征右矢 |x'⟩ 的存在，仍然具有广泛的应用领域。

1.7.5 推广到三维到目前为止，在本节中，我们为了简单起见只在一维空间中工作，但如果我们进行必要的修改，我们所做的一切都可以推广到三维空间。可以使用的位置本征右矢满足 x|x'⟩ = x'|x'⟩， (1.275)

或者动量本征右矢满足 p|p'⟩ = p'|p'⟩。 (1.276)

它们满足归一化条件 ⟨x'|x''⟩ = δ^3(x' - x'')， (1.277a)

和 ⟨p'|p''⟩ = δ^3(p' - p'')， (1.277b)

其中 δ^3 代表三维 δ 函数 δ^3(x' - x'') = δ(x' - x'') δ(y' - y'') δ(z' - z'')。 (1.278)

18 事实证明，局域态的概念在相对论量子力学中要复杂得多，因为存在“负能态”或对产生。参见本教材的第 8 章。

54 基本概念完备性关系为 ∫ d^3x' |x'⟩⟨x'| = 1， (1.279a)

和 ∫ d^3p' |p'⟩⟨p'| = 1， (1.279b)

可以用来展开任意态右矢： |α⟩ = ∫ d^3x' |x'⟩⟨x'|α⟩， (1.280a)

|α⟩ = ∫ d^3p' |p'⟩⟨p'|α⟩。 (1.280b)

展开系数 ⟨x'|α⟩ 和 ⟨p'|α⟩ 分别被认定为位置空间和动量空间中的波函数 ψ_α(x') 和 φ_α(p')。

动量算符，当取在 |β⟩ 和 ⟨α| 之间时，变为 ⟨β|p|α⟩ = ∫ d^3x' ψ_β*(x') (-iħ∇') ψ_α(x')。 (1.281)

类似于 (1.264) 的变换函数为 ⟨x'|p'⟩ = (1/(2πħ)^{3/2}) exp(ip'·x'/ħ)， (1.282)

因此 ψ_α(x') = (1/(2πħ)^{3/2}) ∫ d^3p' exp(ip'·x'/ħ) φ_α(p')， (1.283a)

和 φ_α(p') = (1/(2πħ)^{3/2}) ∫ d^3x' exp(-ip'·x'/ħ) ψ_α(x')。 (1.283b)

检查波函数的维度很有趣。在一维问题中，归一化要求 (1.190) 意味着 |⟨x'|α⟩|^2 具有长度倒数的维度，因此波函数本身必须具有 (长度)^{-1/2} 的维度。相比之下，三维问题中的波函数必须具有 (长度)^{-3/2} 的维度，因为 |⟨x'|α⟩|^2 在整个空间体积上的积分必须是 1（无量纲）。

问题 1.1 一束银原子是通过在烤箱中将蒸气加热到 1000°C 并选择速度接近热分布平均值的原子而产生的。该束通过一个一米长的、具有垂直梯度 10T/m 的磁场，并撞击磁体末端下游一米处的屏幕。假设银原子具有自旋 1/2 和一个玻尔磁子的磁矩，求屏幕上两个态之间的分离距离（以毫米为单位）。

55 问题

## 1.2 证明

[AB, CD] = -AC{D, B} + A{C, B}D - C{D, A}B + {C, A}DB。

## 1.3 对于自旋 1/2 态 |S_z; +⟩，评估不等式 (1.146) 的两边，即

(ΔA)^2 (ΔB)^2 ≥ |⟨[A, B]⟩|^2， 其中算符 A = S_x 和 B = S_y，并证明不等式成立。对算符 A = S_z 和 B = S_y 重复此过程。

## 1.4 假设一个 2x2 矩阵 X（不一定是厄米的，也不是幺正的）写成

X = a_0 I + σ·a， 其中矩阵 σ 在 (3.50) 中给出，a_0 和 a（k=1,2,3）是数字。

a. a_0 和 a_k 如何与 tr(X) 和 tr(σ_k X) 相关？

b. 用矩阵元素 X_ij 表示 a_0 和 a_k。

## 1.5 证明 2x2 矩阵 σ·a 的行列式在变换下不变

σ·a → σ·a' ≡ exp(-iσ·n̂ φ/2) σ·a exp(iσ·n̂ φ/2)， 其中矩阵 σ_k 在 (3.50) 中给出。当 n̂ 在正 z 方向时，用 a 表示 a'，并解释你的结果。

## 1.6 使用狄拉克符号代数，证明或评估以下内容：

a. tr(XY) = tr(YX)，其中 X 和 Y 是算符； b. (XY)† = Y†X†，其中 X 和 Y 是算符； c. exp[if(A)] = ? 用狄拉克符号形式表示，其中 A 是一个本征值已知的厄米算符； d. ∑_a' ψ_a'*(x) ψ_a'(x')，其中 ψ_a'(x) = ⟨x|a'⟩。

1.7 a. 考虑两个右矢 |α⟩ 和 |β⟩。假设 ⟨a'|α⟩, ⟨a''|α⟩, ... 和 ⟨a'|β⟩, ⟨a''|β⟩, ... 都是已知的，其中 |a'⟩, |a''⟩, ... 构成一组完备的基右矢。求算符 |α⟩⟨β| 在该基下的矩阵表示。

b. 现在考虑一个自旋 1/2 系统，并令 |α⟩ 和 |β⟩ 分别为 |S_z; +⟩ 和 |S_x; +⟩。明确写出对应于 |α⟩⟨β| 的方阵，在通常的（对角）基下。

## 1.8 假设 |i⟩ 和 |j⟩ 是某个厄米算符 A 的本征右矢。在什么条件下我们可以推断 |i⟩ + |j⟩ 也是 A 的本征右矢？证明你的答案。

## 1.9 考虑一个由厄米算符 A 的本征右矢 {|a'⟩} 张成的右矢空间。没有简并。

a. 证明 ∏_a' (A - a' I)

是零算符。

b. ∏_{a''≠a'} (A - a'' I) / (a' - a'') 的意义是什么？

c. 使用自旋 1/2 系统的 A = S_z 来说明 (a) 和 (b)。

## 1.10 利用 |+⟩ 和 |-⟩ 的正交归一性，证明

[S_i, S_j] = i ε_{ijk} ħ S_k， {S_i, S_j} = δ_{ij} ħ^2 I， 其中 S_x = (ħ/2) (|+⟩⟨-| + |-⟩⟨+|)， S_y = (ħ/2) (-i|+⟩⟨-| + i|-⟩⟨+|)， S_z = (ħ/2) (|+⟩⟨+| - |-⟩⟨-|)。

## 1.11 构造 |S·n̂; +⟩ 使得

S·n̂ |S·n̂; +⟩ = (ħ/2) |S·n̂; +⟩， 其中 n̂ 由图中所示的角度表征。将你的答案表示为 |+⟩ 和 |-⟩ 的线性组合。[注意：答案是 cos(β/2) |+⟩ + sin(β/2) e^{iα} |-⟩。

但不要仅仅验证这个答案满足上述本征值方程。相反，请将该问题作为一个直接的本征值问题来处理。也不要使用旋转算符，我们将在本书后面介绍它们。]

## 1.12 一个二态系统的哈密顿算符为

H = a (|1⟩⟨1| - |2⟩⟨2| + |1⟩⟨2| + |2⟩⟨1|)， 其中 a 是一个具有能量维度的数字。求能量本征值以及相应的能量本征右矢（作为 |1⟩ 和 |2⟩ 的线性组合）。

57 问题

## 1.13 一个二态系统的特征是哈密顿量

H H_{11}|1><1| + H_{22}|2><2| + H_{12}(|1><2| + |2><1|)

where H_{11}, H_{22}, and H_{12} are real numbers with the dimension of energy, and |1> and |2> are In particular, time is not an observable in the language of the previous chapter. It is nonsensical to talk about the time operator in the same sense as we talk about the position operator. Ironically, in the historical development of wave mechanics both L. de Broglie and E. Schrödinger were guided by a kind of covariant analogy between energy and time on the one hand and momentum and position (spatial coordinate) on the other. Yet when we now look at quantum mechanics in its finished form, there is not trace of a symmetrical treatment between time and space. The relativistic quantum theory of fields does treat the time and space coordinates on the same footing, but it does so only at the expense of demoting position from the status of being an observable to that of being just a parameter.

2.1.1 Time-Evolution Operator Our basic concern in this section is, How does a state ket change with time? Suppose we have a physical system whose state ket at t is represented by |α(cid:8). At later times, we do not, in general, expect the system to remain in the same state |α(cid:8). Let us denote the ket corresponding to the state at some later time by |α, t; t₀(cid:8) (t > t₀), (2.1)

where we have written α, t to remind ourselves that the system used to be in state |α(cid:8) at some earlier reference time t₀. Because time is assumed to be a continuous parameter, we expect lim_{t→t₀} |α, t; t₀(cid:8) = |α(cid:8) (2.2)

and we may as well use a shorthand notation, |α, t₀; t₀(cid:8) = |α, t₀(cid:8), (2.3)

for this. Our basic task is to study the time evolution of a state ket: |α, t₀(cid:8) --t−−im−e−−ev−olu−tio→n |α, t; t₀(cid:8). (2.4)

Put in another way, we are interested in asking how the state ket changes under a time displacement t → t.

As in the case of translation, the two kets are related by an operator which we call the time-evolution operator U(t, t₀): |α, t; t₀(cid:8) = U(t, t₀)|α, t₀(cid:8). (2.5)

What are some of the properties we would like to ascribe to the time-evolution operator? The first important property is the unitary requirement for U(t, t₀) that follows from probability conservation. Suppose that at t₀ the state ket is expanded in terms of the eigenkets of some observable A: |α, t₀(cid:8) = ∑_{a'} c_{a'}(t₀)|a'(cid:8). (2.6)

Likewise, at some later time, we have |α, t; t₀(cid:8) = ∑_{a'} c_{a'}(t)|a'(cid:8). (2.7)

In general, we do not expect the modulus of the individual expansion coefficient to remain the same:¹ |c_{a'}(t)| ≠ |c_{a'}(t₀)|. (2.8)

For instance, consider a spin 1 system with its spin magnetic moment subjected to a uniform magnetic field in the z-direction. To be specific, suppose that at t₀ the spin is in the positive x-direction; that is, the system is prepared in an eigenstate of Sₓ with eigenvalue ħ/2. As time goes on, the spin precesses in the xy-plane, as will be quantitatively demonstrated later in this section. This means that the probability for observing Sₓ is no longer unity at t > t₀; there is a finite probability for observing S₋ as well. Yet the sum of the probabilities for Sₓ and S₋ remains unity at all times. Generally, in the notation of (2.6) and (2.7), we must have ∑_{a'} |c_{a'}(t₀)|² = ∑_{a'} |c_{a'}(t)|² (2.9)

despite (2.8) for the individual expansion coefficients. Stated another way, if the state ket is initially normalized to unity, it must remain normalized to unity at all later times: ⟨α, t₀|α, t₀(cid:8) = 1 ⇒ ⟨α, t₀; t₀|α, t₀; t₀(cid:8) = 1. (2.10)

¹ We later show, however, that if the Hamiltonian commutes with A, then |c_{a'}(t)| is indeed equal to |c_{a'}(t₀)|.

As in the translation case, this property is guaranteed if the time-evolution operator is taken to be unitary. For this reason we take unitarity, U†(t, t₀)U(t, t₀) = 1, (2.11)

to be one of the fundamental properties of the U operator. It is no coincidence that many authors regard unitarity as being synonymous with probability conservation.

Another feature we require of the U operator is the composition property: U(t₂, t₀) = U(t₂, t₁)U(t₁, t₀) (t₂ > t₁ > t₀). (2.12)

This equation says that if we are interested in obtaining time evolution from t₀ to t₂, then we can obtain the same result by first considering time evolution from t₀ to t₁, then from t₁ to t₂, a reasonable requirement. Note that we read (2.12) from right to left!

It also turns out to be advantageous to consider an infinitesimal time-evolution operator U(t₀ + dt, t₀): |α, t₀; t₀ + dt(cid:8) = U(t₀ + dt, t₀)|α, t₀(cid:8). (2.13)

Because of continuity [see (2.2)], the infinitesimal time-evolution operator must reduce to the identity operator as dt goes to zero, lim_{dt→0} U(t₀ + dt, t₀) = 1, (2.14)

and as in the translation case, we expect the difference between U(t₀ + dt, t₀) and 1 to be of first order in dt.

We assert that all these requirements are satisfied by U(t₀ + dt, t₀) = 1 − iΩ dt, (2.15)

where Ω is a Hermitian operator,² Ω† = Ω. (2.16)

With (2.15) the infinitesimal time-displacement operator satisfies the composition property U(t₀ + dt₁ + dt₂, t₀) = U(t₀ + dt₁ + dt₂, t₀ + dt₁)U(t₀ + dt₁, t₀); (2.17)

it differs from the identity operator by a term of order dt. The unitarity property can also be checked as follows: U†(t₀ + dt, t₀)U(t₀ + dt, t₀) = (1 + iΩ† dt)(1 − iΩ dt) ≃ 1, (2.18)

to the extent that terms of order (dt)² or higher can be ignored.

² If the Ω operator depends on time explicitly, it must be evaluated at t₀.

The operator Ω has the dimension of frequency or inverse time. Is there any familiar observable with the dimension of frequency? We recall that in the old quantum theory, angular frequency ω is postulated to be related to energy by the Planck–Einstein relation E = ħω. (2.19)

Let us now borrow from classical mechanics the idea that the Hamiltonian is the generator of time evolution (Goldstein et al. (2002), pp. 401–402). It is then natural to relate Ω to the Hamiltonian operator H: Ω = H / ħ. (2.20)

To sum up, the infinitesimal time-evolution operator is written as U(t₀ + dt, t₀) = 1 − iH dt / ħ, (2.21)

where H, the Hamiltonian operator, is assumed to be Hermitian. The reader may ask whether the ħ introduced here is the same as the ħ that appears in the expression for the translation operator (1.214). This question can be answered by comparing the quantum-mechanical equation of motion we derive later with the classical equation of motion. It turns out that unless the two ħ are taken to be the same, we are unable to obtain a relation like dx/dt = p/m (2.22)

as the classical limit of the corresponding quantum-mechanical relation.

2.1.2 The Schrödinger Equation We are now in a position to derive the fundamental differential equation for the time-evolution operator U(t, t₀). We exploit the composition property of the time-evolution operator by letting t₁ → t, t₂ → t + dt in (2.12): U(t + dt, t₀) = U(t + dt, t)U(t, t₀) = (1 − iH dt / ħ) U(t, t₀), (2.23)

where the time difference t − t₀ need not be infinitesimal. We have U(t + dt, t₀) − U(t, t₀) = −i dt / ħ H U(t, t₀), (2.24)

which can be written in differential equation form: iħ ∂U(t, t₀)/∂t = H U(t, t₀). (2.25)

This is the Schrödinger equation for the time-evolution operator. Everything that has to do with time development follows from this fundamental equation.

Equation (2.25) immediately leads to the Schrödinger equation for a state ket. Multiplying both sides of (2.25) by |α, t₀(cid:8) on the right, we obtain iħ ∂U(t, t₀)/∂t |α, t₀(cid:8) = H U(t, t₀)|α, t₀(cid:8). (2.26)

But |α, t₀(cid:8) does not depend on t, so this is the same as iħ ∂|α, t; t₀(cid:8)/∂t = H |α, t; t₀(cid:8), (2.27)

where (2.5) has been used.

If we are given U(t, t₀) and, in addition, know how U(t, t₀) acts on the initial state ket |α, t₀(cid:8), it is not necessary to bother with the Schrödinger equation for the state ket (2.27). All we have to do is apply U(t, t₀) to |α, t₀(cid:8); in this manner we can obtain a state ket at any t. Our first task is therefore to derive formal solutions to the Schrödinger equation for the time-evolution operator (2.25). There are three cases to be treated separately.

Case 1. The Hamiltonian operator is independent of time. By this we mean that even when the parameter t is changed, the H operator remains unchanged. The Hamiltonian for a spin-magnetic moment interacting with a time-independent magnetic field is an example of this. The solution to (2.25) in such a case is given by U(t, t₀) = exp[−iH(t − t₀)/ħ]. (2.28)

To prove this let us expand the exponential as follows: exp[−iH(t − t₀)/ħ] = 1 + [−iH(t − t₀)/ħ] + [(-i)²H²(t − t₀)²/2!ħ²] + · · · . (2.29)

Because the time derivative of this expansion is given by ∂/∂t exp[−iH(t − t₀)/ħ] = [−iH/ħ] + [(-i)²H²(t − t₀)/ħ²] + · · · , (2.30)

expression (2.28) obviously satisfies differential equation (2.25). The boundary condition is also satisfied because as t → t₀, (2.28) reduces to the identity operator. An alternative way to obtain (2.28) is to compound successively infinitesimal time-evolution operators just as we did to obtain (1.218) for finite translation: lim_{N→∞} [1 − (iH/ħ)(t − t₀)/N]^N = exp[−iH(t − t₀)/ħ]. (2.31)

Case 2. The Hamiltonian operator H is time dependent but the H at different times commute. As an example, let us consider the spin-magnetic moment subjected to a magnetic field whose strength varies with time but whose direction is always unchanged. The formal solution to (2.25) in this case is U(t, t₀) = exp[−(i/ħ) ∫_{t₀}^{t} dt' H(t')]. (2.32)

This can be proved in a similar way. We simply replace H(t − t₀) in (2.29) and (2.30) by ∫_{t₀}^{t} dt' H(t').

Case 3. The H at different times do not commute. Continuing with the example involving spin-magnetic moment, we suppose, this time, that the magnetic field direction also changes with time: at t = t₁ in the x-direction, at t = t₂ in the y-direction, and so forth. Because Sₓ and Sᵧ do not commute, H(t₁) and H(t₂), which go like S·B, do not commute either. The formal solution in such a situation is given by U(t, t₀) = 1 + ∑_{n=1}^{∞} (-i/ħ)^n ∫_{t₀}^{t} dt_n ∫_{t₀}^{t_n} dt_{n-1} · · · ∫_{t₀}^{t₂} dt₁ H(t_n)H(t_{n-1}) · · · H(t₁), (2.33)

which is sometimes known as the Dyson series, after F. J. Dyson, who developed a perturbation expansion of this form in quantum field theory. We do not prove (2.33) now because the proof is very similar to the one presented in Chapter 5 for the time-evolution operator.

or in the interaction picture.

In elementary applications, only case 1 is of practical interest. In the remaining part of this chapter we assume that the H operator is time independent. We will encounter time-dependent Hamiltonians in Chapter 5.

2.1.3 Energy Eigenkets To be able to evaluate the effect of the time-evolution operator (2.28) on a general initial ket |α⟩, we must first know how it acts on the base kets used in expanding |α⟩. This is particularly straightforward if the base kets used are eigenkets of A such that [A, H] = 0; (2.34)

then the eigenkets of A are also eigenkets of H, called energy eigenkets, whose eigenvalues are denoted by E_a': H|a'⟩ = E_a'|a'⟩. (2.35)

We can now expand the time-evolution operator in terms of |a'⟩⟨a'|. Taking t = 0 for simplicity, we obtain exp(-iHt/ℏ) = Σ_{a'} Σ_{a''} |a'⟩⟨a'| exp(-iHt/ℏ) |a''⟩⟨a''| = Σ_{a'} |a'⟩ exp(-iE_{a'}t/ℏ) ⟨a'|. (2.36)

The time-evolution operator written in this form enables us to solve any initial-value problem once the expansion of the initial ket in terms of {|a'⟩} is known. As an example, suppose that the initial ket expansion reads |α, t_0=0⟩ = Σ_{a'} |a'⟩⟨a'|α⟩ = Σ_{a'} c_{a'}(t=0) |a'⟩. (2.37)

We then have |α, t_0=0; t⟩ = exp(-iHt/ℏ) |α, t_0=0⟩ = Σ_{a'} |a'⟩⟨a'|α⟩ exp(-iE_{a'}t/ℏ). (2.38)

In other words, the expansion coefficient changes with time as c_{a'}(t=0) → c_{a'}(t) = c_{a'}(t=0) exp(-iE_{a'}t/ℏ) (2.39)

with its modulus unchanged. Notice that the relative phases among various components do vary with time because the oscillation frequencies are different.

A special case of interest is where the initial state happens to be one of {|a'⟩} itself. We have |α, t_0=0⟩ = |a'⟩ (2.40)

initially, and at a later time |a, t_0=0; t⟩ = |a'⟩ exp(-iE_{a'}t/ℏ), (2.41)

so if the system is initially a simultaneous eigenstate of A and H, it remains so at all times. The most that can happen is the phase modulation, exp(-iE_{a'}t/ℏ). It is in this sense that an observable compatible with H [see (2.34)] is a constant of the motion. We will encounter this connection once again in a different form when we discuss the Heisenberg equation of motion.

In the foregoing discussion the basic task in quantum dynamics is reduced to finding an observable that commutes with H and evaluating its eigenvalues. Once that is done, we expand the initial ket in terms of the eigenkets of that observable and just apply the time-evolution operator. This last step merely amounts to changing the phase of each expansion coefficient, as indicated by (2.39).

Even though we worked out the case where there is just one observable A that commutes with H, our considerations can easily be generalized when there are several mutually compatible observables all also commuting with H: [A, B] = [B, C] = [A, C] = ··· = 0, [A, H] = [B, H] = [C, H] = ··· = 0. (2.42)

Using the collective index notation of Section 1.4 [see (1.130)], we have exp(-iHt/ℏ) = Σ_{K'} |K'⟩ exp(-iE_{K'}t/ℏ) ⟨K'|, (2.43)

where E_{K'} is uniquely specified once a', b', c', ... are specified. It is therefore of fundamental importance to find a complete set of mutually compatible observables that also commute with H. Once such a set is found, we express the initial ket as a superposition of the simultaneous eigenkets of A, B, C, ... and H. The final step is just to apply the time-evolution operator, written as (2.43). In this manner we can solve the most general initial-value problem with a time-independent H.

2.1.4 Time Dependence of Expectation Values It is instructive to study how the expectation value of an observable changes as a function of time. Suppose that at t=0 the initial state is one of the eigenstates of an observable A that commutes with H, as in (2.40). We now look at the expectation value of some other observable B, which need not commute with A nor with H. Because at a later time we have |a', t_0=0; t⟩ = U(t, 0)|a'⟩ (2.44)

for the state ket, ⟨B⟩ is given by ⟨B⟩ = (⟨a'|U†(t, 0)) · B · (U(t, 0)|a'⟩)

= ⟨a'| exp(iE_{a'}t/ℏ) B exp(-iE_{a'}t/ℏ) |a'⟩ = ⟨a'|B|a'⟩, (2.45)

which is independent of t. So the expectation value of an observable taken with respect to an energy eigenstate does not change with time. For this reason an energy eigenstate is often referred to as a stationary state.

The situation is more interesting when the expectation value is taken with respect to a superposition of energy eigenstates, or a nonstationary state. Suppose that initially we have |α, t_0=0⟩ = Σ_{a'} c_{a'} |a'⟩. (2.46)

We easily compute the expectation value of B to be ⟨B⟩ = Σ_{a'} c*_{a'} ⟨a'| exp(iE_{a'}t/ℏ) · B · Σ_{a''} c_{a''} exp(-iE_{a''}t/ℏ) |a''⟩ = Σ_{a'} Σ_{a''} c*_{a'} c_{a''} ⟨a'|B|a''⟩ exp(-i(E_{a''} - E_{a'})t/ℏ). (2.47)

So this time the expectation value consists of oscillating terms whose angular frequencies are determined by N. Bohr's frequency condition ω_{a''a'} = (E_{a''} - E_{a'})/ℏ. (2.48)

2.1.5 Spin Precession It is appropriate to treat an example here. We consider an extremely simple system which, however, illustrates the basic formalism we have developed.

We start with a Hamiltonian of a spin 1/2 system with magnetic moment eℏ/2m_e c subjected to an external magnetic field B: H = -(e/m_e c) S·B (2.49)

(e < 0 for the electron). Furthermore, we take B to be a static, uniform magnetic field in the z-direction. We can then write H as H = -(eB/m_e c) S_z. (2.50)

Because S_z and H differ just by a multiplicative constant, they obviously commute. The S_z eigenstates are also energy eigenstates, and the corresponding energy eigenvalues are E_± = ∓ (eℏB)/(2m_e c), for S_z = ±ℏ/2. (2.51)

It is convenient to define ω in such a way that the difference in the two energy eigenvalues is ℏω: ω ≡ |e|B/(m_e c). (2.52)

We can then rewrite the H operator simply as H = ω S_z. (2.53)

All the information on time development is contained in the time-evolution operator U(t, 0) = exp(-iω S_z t/ℏ). (2.54)

We apply this to the initial state. The base kets we must use in expanding the initial ket are obviously the S_z eigenkets, |+⟩ and |−⟩, which are also energy eigenkets. Suppose that at t=0 the system is characterized by |α⟩ = c_+ |+⟩ + c_- |−⟩. (2.55)

Upon applying (2.54), we see that the state ket at some later time is |α, t_0=0; t⟩ = c_+ exp(-iωt/2) |+⟩ + c_- exp(+iωt/2) |−⟩, (2.56)

where we have used H|±⟩ = (±ℏω/2) |±⟩. (2.57)

Specifically, let us suppose that the initial ket |α⟩ represents the spin-up (or, more precisely, S_z = +ℏ/2) state |+⟩, which means that c_+ = 1, c_- = 0. (2.58)

At a later time, (2.56) tells us that it is still in the spin-up state, which is no surprise because this is a stationary state.

Next, let us suppose that initially the system is in the S_x = +ℏ/2 state. Comparing (1.110a) with (2.55), we see that c_+ = c_- = 1/√2. (2.59)

It is straightforward to work out the probabilities for the system to be found in the S_z = ±ℏ/2 state at some later time t: |⟨S_z; ±|α, t_0=0; t⟩|^2 = |(1/√2)⟨+| ± (1/√2)⟨-| · [(1/√2) exp(-iωt/2) |+⟩ + (1/√2) exp(+iωt/2) |−⟩]|^2 = |(1/2)[exp(-iωt/2) ± exp(+iωt/2)]|^2 = cos²(ωt/2) for S_z = +ℏ/2, (2.60a)

= sin²(ωt/2) for S_z = -ℏ/2. (2.60b)

Even though the spin is initially in the positive x-direction, the magnetic field in the z-direction causes it to rotate; as a result, we obtain a finite probability for finding S_z = -ℏ/2 at some later time. The sum of the two probabilities is seen to be unity at all times, in agreement with the unitarity property of the time-evolution operator.

Using (1.99), we can write the expectation value of S_x as ⟨S_x⟩ = (ℏ/2) cos²(ωt/2) + (-ℏ/2) sin²(ωt/2)

= (ℏ/2) cosωt, (2.61)

so this quantity oscillates with an angular frequency corresponding to the difference of the two energy eigenvalues divided by ℏ, in agreement with our general formula (2.47).

Similar exercises with S_y and S_z show that ⟨S_y⟩ = (ℏ/2) sinωt (2.62a)

and ⟨S_z⟩ = 0. (2.62b)

Physically this means that the spin precesses in the xy-plane. We will comment further on spin precession when we discuss rotation operators in Chapter 3.

Experimentally, spin precession is well established. In fact, it is used as a tool for other investigations of fundamental quantum-mechanical phenomena. For example, the form of the Hamiltonian (2.49) can be derived for pointlike particles, such as electrons or muons, which obey the Dirac equation, for which the gyromagnetic ratio g = 2. (See Section 8.2.) However, higher-order corrections from quantum field theory predict a small but precisely calculable deviation from this, and it is a high priority to produce competitively precise measurements of g − 2.

Such an experiment has been recently completed. See Bennett et al., Phys. Rev. D, 73 (2006) 072003. Muons are injected into a “storage ring” designed so that their spins would precess in lock step with their momentum vector only if g ≡ 2. Consequently, observation of their precession measures g − 2 directly, facilitating a very precise result. Figure 2.1 shows the experimenters’ observation of the muon spin rotation over more than one hundred periods. They determine a value for g − 2 to a precision smaller than one part per million, which agrees reasonably well with the theoretical value.

2.1.6 Neutrino Oscillations A lovely example of quantum-mechanical dynamics leading to interference in a two-state system, bas Based on current physics research, is provided by the phenomenon known as neutrino oscillations.3 Neutrinos are elementary particles with no charge, and very small mass, much smaller than that of an electron. They are known to occur in nature in three distinct “flavors,” although for this discussion it suffices to only consider two of them. These two flavors are identified by their interactions which may be either with electrons, in which case we write νe, or with muons, that is νμ. These are in fact eigenstates of a Hamiltonian which controls those interactions.

On the other hand, it is possible (and, in fact, now known to be true) that neutrinos may have some other interactions, in which case their energy eigenvalues correspond to states that have a well-defined mass. These “mass eigenstates” would have eigenvalues E1 and E2, say, corresponding to masses m1 and m2, and might be denoted as |ν1⟩ and |ν2⟩. The “flavor eigenstates” are related to these through a simple unitary transformation, specified by some mixing angle θ, as follows: |νe⟩ = cosθ |ν1⟩ − sinθ |ν2⟩ (2.63a)

|νμ⟩ = sinθ |ν1⟩ + cosθ |ν2⟩. (2.63b)

If the mixing angle were zero, then |νe⟩ and |νμ⟩ would respectively be the same as |ν1⟩ and |ν2⟩. However, we know of no reason why this should be the case. Indeed, there is no strong theoretical bias for any particular value of θ, and it is a free parameter which, today, can only be determined through experiment.

Neutrino oscillation is the phenomenon by which we can measure the mixing angle. Suppose we prepare, at time t = 0, a momentum eigenstate of one flavor of neutrino, say |νe⟩. Then according to (2.63a) the two different mass eigenstate components will evolve with different frequencies, and therefore develop a relative phase difference. If the difference in the masses is small enough, then this phase difference can build up over a macroscopic distance. In fact, by measuring the interference as a function of difference, one can observe oscillations with a period that depends on the difference of masses, and an amplitude that depends on the mixing angle.

It is straightforward (see Problem 2.4 at the end of this chapter) to use (2.63) along with (2.28) and our quantum-mechanical postulates, and find a measurable quantity that exhibits neutrino oscillations. In this case, the Hamiltonian is just that for a free particle, but we need to take some care. Neutrinos are very low mass, so they are highly relativistic for any practical experimental conditions. Therefore, for a fixed momentum p, the energy eigenvalue for a neutrino of mass m is given to an extremely good approximation as E = (p²c² + m²c⁴)^{1/2} ≈ pc (1 + m²c² / (2p²)). (2.64)

If we then allow our state |νe⟩ to evolve, and then at some later time t ask what is the probability that it still appears as a |νe⟩ (as opposed to a |νμ⟩), we find P(νe → νe) = 1 − sin²2θ sin²(Δm²c⁴t / (4Eℏc)) (2.65)

where Δm² ≡ m1² − m2², L = ct is the flight distance of the neutrino, and E = pc is the nominal neutrino energy.

The oscillations predicted by (2.65) have been dramatically observed by the KamLAND experiment. See Figure 2.2. Neutrinos from a series of nuclear reactors are detected at a distance of ∼150 km, and the rate is compared to that expected from reactor power and properties. The curve is not a perfect sine wave because the reactors are not all at the same distance from the detector.

Fig. 2.2 Neutrino oscillations as observed by the KamLAND experiment, taken from Abe et al., Phys. Rev. Lett., 100 (2008) 221803. The oscillations as a function of L/E demonstrate interference between different mass eigenstates of neutrinos.

2.1.7 Correlation Amplitude and the Energy-Time Uncertainty Relation We conclude this section by asking how state kets at different times are correlated with each other. Suppose the initial state ket at t=0 of a physical system is given by |α⟩. With time it changes into |α, t=0; t⟩, which we obtain by applying the time-evolution operator. We are concerned with the extent to which the state ket at a later time t is similar to the state ket at t=0; we therefore construct the inner product between the two state kets at different times: C(t) ≡ ⟨α|α, t=0; t⟩ = ⟨α|U(t,0)|α⟩, (2.66)

which is known as the correlation amplitude. The modulus of C(t) provides a quantitative measure of the “resemblance” between the state kets at different times.

As an extreme example, consider the very special case where the initial ket |α⟩ is an eigenket of H; we then have C(t) = ⟨a′|a′, t=0; t⟩ = exp(−iE_{a′}t / ℏ), (2.67)

so the modulus of the correlation amplitude is unity at all times, which is not surprising for a stationary state. In the more general situation where the initial ket is represented by a superposition of {|a′⟩}, as in (2.37), we have C(t) = ∑_{a′} c_{a′}^* ⟨a′| ∑_{a′′} c_{a′′} exp(−iE_{a′′}t / ℏ) |a′′⟩ = ∑_{a′} |c_{a′}|^2 exp(−iE_{a′}t / ℏ). (2.68)

As we sum over many terms with oscillating time dependence of different frequencies, a strong cancellation is possible for moderately large values of t. We expect the correlation amplitude that starts with unity at t=0 to decrease in magnitude with time.

To estimate (2.68) in a more concrete manner, let us suppose that the state ket can be regarded as a superposition of so many energy eigenkets with similar energies that we can regard them as exhibiting essentially a quasi-continuous spectrum. It is then legitimate to replace the sum by the integral ∑_{a′} → ∫ dE ρ(E), c_{a′} → g(E), (2.69)

where ρ(E) characterizes the density of energy eigenstates. Expression (2.68) now becomes C(t) = ∫ dE |g(E)|^2 ρ(E) exp(−iEt / ℏ), (2.70)

subject to the normalization condition ∫ dE |g(E)|^2 ρ(E) = 1. (2.71)

In a realistic physical situation |g(E)|^2 ρ(E) may be peaked around E = E0 with width ΔE. Writing (2.70) as C(t) = exp(−iE₀t / ℏ) ∫ dE |g(E)|^2 ρ(E) exp(−i(E−E₀)t / ℏ), (2.72)

we see that as t becomes large, the integrand oscillates very rapidly unless the energy interval |E−E₀| is small compared with ℏ/t. If the interval for which |E−E₀| ≪ ℏ/t holds is much narrower than ΔE, the width of |g(E)|^2 ρ(E), we get essentially no contribution to C(t) because of strong cancellations. The characteristic time at which the modulus of the correlation amplitude starts becoming appreciably different from 1 is given by t ≈ ℏ / ΔE. (2.73)

Even though this equation is obtained for a superposition state with a quasi-continuous energy spectrum, it also makes sense for a two-level system; in the spin-precession problem considered earlier, the state ket, which is initially |S+⟩, starts losing its identity after ∼1/ω = ℏ/(E+ − E−), as is evident from (2.60).

To summarize, as a result of time evolution the state ket of a physical system ceases to retain its original form after a time interval of order ℏ/ΔE. In the literature this point is often said to illustrate the energy-time uncertainty relation Δt ΔE ≈ ℏ. (2.74)

However, it is to be clearly understood that this energy-time uncertainty relation is of a very different nature from the uncertainty relation between two incompatible observables discussed in Section 1.4. In Chapter 5 we will come back to (2.74) in connection with time-dependent perturbation theory.

## 2.2 The Schrödinger Versus the Heisenberg Picture

2.2.1 Unitary Operators In the previous section we introduced the concept of time development by considering the time-evolution operator that affects state kets; that approach to quantum dynamics is known as the Schrödinger picture. There is another formulation of quantum dynamics where observables, rather than state kets, vary with time; this second approach is known as the Heisenberg picture. Before discussing the differences between the two approaches in detail, we digress to make some general comments on unitary operators.

Unitary operators are used for many different purposes in quantum mechanics. In this book we introduced (Section 1.5) an operator satisfying the unitarity property. In that section we were concerned with the question of how the base kets in one representation are related to those in some other representations. The state kets themselves are assumed not to change as we switch to a different set of base kets even though the numerical values of the expansion coefficients for |α⟩ are, of course, different in different representations.

Subsequently we introduced two unitary operators that actually change the state kets, the translation operator of Section 1.6 and the time-evolution operator of Section 2.1. We have |α⟩ → U|α⟩, (2.75)

where U may stand for T(dx) or U(t, t0). Here U|α⟩ is the state ket corresponding to a physical system that has actually undergone translation or time evolution.

It is important to keep in mind that under a unitary transformation that changes the state kets, the inner product of a state bra and a state ket remains unchanged: ⟨β|α⟩ → ⟨β|U†U|α⟩ = ⟨β|α⟩. (2.76)

Using the fact that these transformations affect the state kets but not operators, we can infer how ⟨β|X|α⟩ must change: ⟨β|X|α⟩ → (⟨β|U†)·X·(U|α⟩) = ⟨β|U†XU|α⟩. (2.77)

We now make a very simple mathematical observation that follows from the associative axiom of multiplication.

(⟨β|U†)·X·(U|α⟩) = ⟨β|·(U†XU)·|α⟩. (2.78)

Is there any physics in this observation? This mathematical identity suggests two approaches to unitary transformations.

Approach 1: |α⟩ → U|α⟩, with operators operators unchanged. (2.79a)

Approach 2: X → U†XU, with state kets unchanged. (2.79b)

In classical physics we do not introduce state kets, yet we talk about translation, time evolution, and the like. This is possible because these operations actually change quantities such as x and L, which are observables of classical mechanics. We therefore conjecture that a closer connection with classical physics may be established if we follow approach 2.

A simple example may be helpful here. We go back to the infinitesimal translation operator T(d x). The formalism presented in Section 1.6 is based on approach 1; T(d x) affects the state kets, not the position operator: |α⟩ → |α⟩ − i p · d x / ℏ |α⟩, x → x. (2.80)

In contrast, if we follow approach 2, we obtain |α⟩ → |α⟩, x → (1 + i p · d x / ℏ) x (1 − i p · d x / ℏ)

= x + [i p · d x / ℏ, x]

= x + d x. (2.81)

We leave it as an exercise for the reader to show that both approaches lead to the same result for the expectation value of x: ⟨x⟩ → ⟨x⟩ + ⟨d x⟩. (2.82)

2.2.2 State Kets and Observables in the Schrödinger and the Heisenberg Pictures We now return to the time-evolution operator U(t, t₀). In the previous section we examined how state kets evolve with time. This means that we were following approach 1, known as the Schrödinger picture when applied to time evolution. Alternatively we may follow approach 2, known as the Heisenberg picture when applied to time evolution.

In the Schrödinger picture the operators corresponding to observables like x, p_y, and S_z are fixed in time, while state kets vary with time, as indicated in the previous section. In contrast, in the Heisenberg picture the operators corresponding to observables vary with time; the state kets are fixed, frozen so to speak, at what they were at t₀. It is convenient to set t₀ in U(t, t₀) to zero for simplicity and work with U(t), which is defined by U(t, t₀=0) ≡ U(t) = exp(−iHt / ℏ). (2.83)

Motivated by (2.79b) of approach 2, we define the Heisenberg picture observable by A(H)(t) ≡ U†(t) A(S) U(t), (2.84)

where the superscripts H and S stand for Heisenberg and Schrödinger, respectively.

At t=0, the Heisenberg picture observable and the corresponding Schrödinger picture observable coincide: A(H)(0) = A(S). (2.85)

The state kets also coincide between the two pictures at t=0; at later t the Heisenberg picture state ket is frozen to what it was at t=0: |α, t₀=0; t⟩_H = |α, t₀=0⟩_H, (2.86)

independent of t. This is in dramatic contrast with the Schrödinger picture state ket, |α, t₀=0; t⟩_S = U(t) |α, t₀=0⟩_S. (2.87)

The expectation value ⟨A⟩ is obviously the same in both pictures: ⟨α, t₀=0; t|_S A(S) |α, t₀=0; t⟩_S = ⟨α, t₀=0|_S U† A(S) U |α, t₀=0⟩_S = ⟨α, t₀=0; t|_H A(H)(t) |α, t₀=0; t⟩_H. (2.88)

2.2.3 The Heisenberg Equation of Motion We now derive the fundamental equation of motion in the Heisenberg picture. Assuming that A(S) does not depend explicitly on time, which is the case in most physical situations of interest, we obtain [by differentiating (2.84)]

dA(H)/dt = (∂U†/∂t) A(S) U + U† A(S) (∂U/∂t)

= (−1/(iℏ) U† H U) U† A(S) U + U† A(S) U (1/(iℏ) U† H U)

= (1/(iℏ)) [A(H), U† H U], (2.89)

where we have used [see (2.25)]

∂U/∂t = (1/(iℏ)) H U, (2.90a)

∂U†/∂t = (−1/(iℏ)) U† H. (2.90b)

Because H was originally introduced in the Schrödinger picture, we may be tempted to define H(H) = U† H U (2.91)

in accordance with (2.84). But in elementary applications where U is given by (2.83), U and H obviously commute; as a result, U† H U = H, (2.92)

so it is all right to write (2.89) as dA(H)/dt = (1/(iℏ)) [A(H), H]. (2.93)

This equation is known as the Heisenberg equation of motion. Notice that we have derived it using the properties of the time-evolution operator and the defining equation for A(H).

It is instructive to compare (2.93) with the classical equation of motion in Poisson bracket form. In classical physics, for a function A of q and p that does not involve time explicitly, we have (Goldstein et al. (2002), pp. 396–397)

dA/dt = [A, H]_{classical}. (2.94)

Again, we see that Dirac’s quantization rule (1.6.47) leads to the correct equation in quantum mechanics. Indeed, historically (2.93) was first written by P. A. M. Dirac, who, with his characteristic modesty, called it the Heisenberg equation of motion. It is worth noting, however, that (2.93) makes sense whether or not A(H) has a classical analogue. For example, the spin operator in the Heisenberg picture satisfies i dS_i(H)/dt = [S_i(H), H] / ℏ, (2.95)

which can be used to discuss spin precession, but this equation has no classical counterpart because S cannot be written as a function of q and p. Rather than insisting on Dirac’s rule, (1.229), we may argue that for quantities possessing classical counterparts, the correct classical equation can be obtained from the corresponding quantum-mechanical equation via the ansatz, [,]/(iℏ) → [,]_{classical}. (2.96)

Classical mechanics can be derived from quantum mechanics, but the opposite is not true.

2.2.4 Free Particles: Ehrenfest’s Theorem Whether we work in the Schrödinger picture or in the Heisenberg picture, to be able to use the equations of motion we must first learn how to construct the appropriate Hamiltonian operator. For a physical system with classical analogues, we assume the Hamiltonian to be of the same form as in classical physics; we merely replace the classical x_i and p_i by the corresponding operators in quantum mechanics. With this assumption we can reproduce the correct classical equations in the classical limit. Whenever an ambiguity arises because of noncommuting observables, we attempt to resolve it by requiring H to be Hermitian; for instance, we write the quantum-mechanical analogue of the classical product x_i p_i as ½(x_i p_i + p_i x_i). When the physical system in question has no classical analogues, we can only guess the structure of the Hamiltonian operator. We try various forms until we get the Hamiltonian that leads to results agreeing with empirical observation.

In practical applications it is often necessary to evaluate the commutator of x_i (or p_i) with functions of x_j and p_j. To this end the following formulas are found to be useful: [x_i, F(p)] = iℏ (∂F/∂p_i) (2.97a)

and [p_i, G(x)] = −iℏ (∂G/∂x_i), (2.97b)

where F and G are functions that can be expanded in powers of p_j and x_j, respectively. We can easily prove both formulas by repeatedly applying (1.232e).

We are now in a position to apply the Heisenberg equation of motion to a free particle of mass m. The Hamiltonian is taken to be of the same form as in classical mechanics: H = p²/(2m) = (p_x² + p_y² + p_z²)/(2m). (2.98)

We look at the observables p_i and x_i, which are understood to be the momentum and the position operator in the Heisenberg picture even though we omit the superscript (H). Because p_i commutes with any function of p, we have dp_i/dt = (1/(iℏ)) [p_i, H] = 0. (2.99)

Thus for a free particle, the momentum operator is a constant of the motion, which means that p_i(t) is the same as p_i(0) at all times. Quite generally, it is evident from the Heisenberg equation of motion (2.93) that whenever A(H) commutes with the Hamiltonian, A(H) is a constant of the motion. Next, dx_i/dt = (1/(iℏ)) [x_i, H] = (1/(iℏ)) (iℏ ∂/∂p_i) (Σ p_j²)/(2m)

= p_i/m = p_i(0)/m, (2.100)

where we have taken advantage of (2.97a), so we have the solution x_i(t) = x_i(0) + p_i(0) t / m, (2.101)

which is reminiscent of the classical trajectory equation for a uniform rectilinear motion.

It is important to note that even though we have [x_i(0), x_j(0)] = 0 (2.102)

at equal times, the commutator of the x_i at different times does not vanish; specifically, [x_i(t), x_j(0)] = [p_i(0) t / m, x_j(0)] = −iℏ t δ_{ij} / m. (2.103)

Applying the uncertainty relation (1.146) to this commutator, we obtain ⟨(Δx_i)²⟩_t ⟨(Δx_j)²⟩_{t=0} ≥ ℏ² t² / (4 m²). (2.104)

Among other things, this relation implies that even if the particle is well localized at t=0, its position becomes more and more uncertain with time, a conclusion which can also be obtained by studying the time-evolution behavior of free-particle wave packets in wave mechanics.

We now add a potential V(x) to our earlier free-particle Hamiltonian: H = p²/(2m) + V(x). (2.105)

Here V(x) is to be understood as a function of the x-, y-, and z-operators. Using (2.97b) this time, we obtain dp_i/dt = (1/(iℏ)) [p_i, V(x)] = −(∂V/∂x_i). (2.106)

On the other hand, we see that dx_i/dt = p_i/m (2.107)

still holds because x_i commutes with the newly added term V(x). We can use the Heisenberg equation of motion once again to deduce d²x_i/dt² = (1/(iℏ)) [dx_i/dt, H] = (1/(iℏ)) [p_i/m, H]

= (1/m) (dp_i/dt). (2.108)

Combining this with (2.32), we finally obtain in vectorial form m d²x/dt² = −∇V(x). (2.109)

This is the quantum-mechanical analogue of Newton’s second law. By taking the expectation values of both sides with respect to a Heisenberg state ket that does not move with time, we obtain m d²⟨x⟩/dt² = d⟨p⟩/dt = −⟨∇V(x)⟩. (2.110)

This is known as the Ehrenfest theorem after P. Ehrenfest, who derived it in 1927 using the formalism of wave mechanics. When written in this expectation form, its validity is independent of whether we are using the Heisenberg or the Schrödinger picture; after all, the expectation values are the same in the two pictures. In contrast, the operator form (2.109) is meaningful only if we understand x and p to be Heisenberg picture operators.

We note that in (2.110) the ℏ have completely disappeared. It is therefore not surprising that the center of a wave packet moves like a classical particle subjected to V(x).

2.2.5 Base Kets and Transition Amplitudes So far we have avoided asking how the base kets evolve in time. A common misconception is that as time goes on, all kets move in the Schrödinger picture and are stationary in the Heisenberg picture. This is not the case, as we will make clear shortly. The important point is to distinguish the behavior of state kets from that of base kets.

We started our discussion of ket spaces in Section 1.2 by remarking that the eigenkets of observables are to be used as base kets. What happens to the definin eigenvalue equation

A|α⟩ = α|α⟩  (2.111)

with time? In the Schrödinger picture, A does not change, so the base kets, obtained as the solutions to this eigenvalue equation at t=0, for instance, must remain unchanged. Unlike state kets, the base kets do not change in the Schrödinger picture.

The whole situation is very different in the Heisenberg picture, where the eigenvalue equation we must study is for the time-dependent operator A^(H)(t) = U†A(0)U. (2.112)

From (2.111) evaluated at t=0, when the two pictures coincide, we deduce U†A(0)UU†|α⟩ = αU†|α⟩, (2.113)

which implies an eigenvalue equation for A^(H): A^(H)(U†|α⟩) = α (U†|α⟩). (2.114)

If we continue to maintain the view that the eigenkets of observables form the base kets, then {U†|α⟩} must be used as the base kets in the Heisenberg picture. As time goes on, the Heisenberg picture base kets, denoted by |α, t⟩_H, move as follows: |α, t⟩_H = U†|α⟩. (2.115)

Because of the appearance of U† rather than U in (2.115), the Heisenberg picture base kets are seen to rotate oppositely when compared with the Schrödinger picture state kets; specifically, |α, t⟩_H satisfies the “wrong-sign Schrödinger equation” iℏ ∂/∂t |α, t⟩_H = -H|α, t⟩_H. (2.116)

As for the eigenvalues themselves, we see from (2.114) that they are unchanged with time. This is consistent with the theorem on unitary equivalent observables discussed in Section 1.5. Notice also the following expansion for A^(H)(t) in terms of the base kets and bras of the Heisenberg picture: A^(H)(t) = Σ_α |α, t⟩_H α ⟨α, t|_H = Σ_α U†|α⟩ α ⟨α|U = U†A^(S)U, (2.117)

which shows that everything is quite consistent provided that the Heisenberg base kets change as in (2.115).

We see that the expansion coefficients of a state ket in terms of base kets are the same in both pictures: c_α(t) = (⟨α| · (U|ψ, t=0⟩)) (the Schrödinger picture) (2.118a) c_α(t) = ((⟨α| · U) · |ψ, t=0⟩) (the Heisenberg picture). (2.118b)

Pictorially, we may say that the cosine of the angle between the state ket and the base ket is the same whether we rotate the state ket counterclockwise or the base ket clockwise. These considerations apply equally well to base kets that exhibit a continuous spectrum; in particular, the wave function ⟨x|α⟩ can be regarded either as (1) the inner product of the stationary position eigenbra with the moving state ket (the Schrödinger picture) or as (2) the inner product of the moving position eigenbra with the stationary state ket (the Heisenberg picture). We will discuss the time dependence of the wave function in Section 2.4, where we will derive the celebrated wave equation of Schrödinger.

To illustrate further the equivalence between the two pictures, we study transition amplitudes, which will play a fundamental role in Section 2.6. Suppose there is a physical system prepared at t=0 to be in an eigenstate of observable A with eigenvalue α. At some later time t we may ask: What is the probability amplitude, known as the transition amplitude, for the system to be found in an eigenstate of observable B with eigenvalue β? Here A and B can be the same or different. In the Schrödinger picture the state ket at t is given by U|α⟩, while the base kets |α⟩ and |β⟩ do not vary with time; so we have ⟨β| · (U|α⟩) (2.119) for this transition amplitude. In contrast, in the Heisenberg picture the state ket is stationary, that is, it remains as |α⟩ at all times, but the base kets evolve oppositely. So the transition amplitude is ((⟨β|U) · |α⟩). (2.120)

Obviously (2.119) and (2.120) are the same. They can both be written as ⟨β|U(t,0)|α⟩. (2.121)

In some loose sense this is the transition amplitude for “going” from state |α⟩ to state |β⟩.

To conclude this section let us summarize the differences between the Schrödinger picture and the Heisenberg picture; see Table 2.1.

Table 2.1 The Schrödinger Picture Versus the Heisenberg Picture Schrödinger picture | Heisenberg picture State ket Moving: (2.5), (2.27) | Stationary Observable Stationary | Moving: (2.84), (2.93)

Base ket Stationary | Moving oppositely: (2.115), (2.116)

## 2.3 Simple Harmonic Oscillator

The simple harmonic oscillator is one of the most important problems in quantum mechanics. It not only illustrates many of the basic concepts and methods of quantum mechanics, it also has much practical value. Essentially any potential well can be approximated by a simple harmonic oscillator, so it describes phenomena from molecular vibrations to nuclear structure. Furthermore, since the Hamiltonian is basically the sum of squares of two canonically conjugate variables, it is also an important starting point for much of quantum field theory.

2.3.1 Energy Eigenkets and Energy Eigenvalues

We begin our discussion with Dirac’s elegant operator method, which is based on the earlier work of M. Born and N. Wiener, to obtain the energy eigenkets and energy eigenvalues of the simple harmonic oscillator. The basic Hamiltonian is H = p²/(2m) + (mω²x²)/2, (2.122) where ω is the angular frequency of the classical oscillator related to the spring constant k in Hooke’s law via ω = √(k/m). The operators x and p are, of course, Hermitian. It is convenient to define two non-Hermitian operators, a = √(mω/(2ℏ)) (x + ip/(mω)), a† = √(mω/(2ℏ)) (x - ip/(mω)), (2.123) known as the annihilation operator and the creation operator, respectively, for reasons that will become evident shortly. Using the canonical commutation relations, we readily obtain [a, a†] = (−i[x, p] + i[p, x])/(2ℏ) = 1. (2.124)

We also define the number operator N = a†a, (2.125) which is obviously Hermitian. It is straightforward to show that a†a = (mω/(2ℏ)) (x² + p²/(m²ω²) + i[x, p]/(2ℏ)) = H/(ℏω) - 1/2, (2.126) so we have an important relation between the number operator and the Hamiltonian operator: H = ℏω(N + 1/2). (2.127)

Because H is just a linear function of N, N can be diagonalized simultaneously with H. We denote an energy eigenket of N by its eigenvalue n, so N|n⟩ = n|n⟩. (2.128)

We will later show that n must be a nonnegative integer. Because of (2.127) we also have H|n⟩ = (n + 1/2)ℏω|n⟩, (2.129) which means that the energy eigenvalues are given by E_n = (n + 1/2)ℏω. (2.130)

To appreciate the physical significance of a, a†, and N, let us first note that [N, a] = [a†a, a] = a†[a, a] + [a†, a]a = -a, (2.131) where we have used (2.124). Likewise, we can derive [N, a†] = a†. (2.132)

As a result, we have Na†|n⟩ = ([N, a†] + a†N)|n⟩ = (n + 1)a†|n⟩ (2.133a) and Na|n⟩ = ([N, a] + aN)|n⟩ = (n - 1)a|n⟩. (2.133b)

These relations imply that a†|n⟩ (a|n⟩) is also an eigenket of N with eigenvalue increased (decreased) by one. Because the increase (decrease) of n by one amounts to the creation (annihilation) of one quantum unit of energy ℏω, the term creation operator (annihilation operator) for a† (a) is deemed appropriate.

Equation (2.133b) implies that a|n⟩ and |n-1⟩ are the same up to a multiplicative constant. We write a|n⟩ = c|n-1⟩, (2.134) where c is a numerical constant to be determined from the requirement that both |n⟩ and |n-1⟩ be normalized. First, note that ⟨n|a†a|n⟩ = |c|². (2.135)

We can evaluate the left-hand side of (2.135) by noting that a†a is just the number operator, so n = |c|². (2.136)

Taking c to be real and positive by convention, we finally obtain a|n⟩ = √n |n-1⟩. (2.137)

Similarly, it is easy to show that a†|n⟩ = √(n+1) |n+1⟩. (2.138)

Suppose that we keep on applying the annihilation operator a to both sides of (2.137): a²|n⟩ = √(n(n-1)) |n-2⟩, a³|n⟩ = √(n(n-1)(n-2)) |n-3⟩, ... (2.139)

We can obtain numerical operator eigenkets with smaller and smaller n until the sequence terminates, which is bound to happen whenever we start with a positive integer n. One may argue that if we start with a noninteger n, the sequence will not terminate, leading to eigenkets with a negative value of n. But we also have the positivity requirement for the norm of a|n⟩: n = ⟨n|N|n⟩ = (⟨n|a†)·(a|n⟩) ≥ 0, (2.140) which implies that n can never be negative! So we conclude that the sequence must terminate with n=0 and that the allowed values of n are nonnegative integers.

Because the smallest possible value of n is zero, the ground state of the harmonic oscillator has E₀ = (1/2)ℏω. (2.141)

We can now successively apply the creation operator a† to the ground state |0⟩. Using (2.138), we obtain |1⟩ = a†|0⟩, |2⟩ = (a†/√2)|1⟩ = ((a†)²/√2)|0⟩, |3⟩ = (a†/√3)|2⟩ = ((a†)³/√(3!))|0⟩, ... |n⟩ = ((a†)ⁿ/√(n!))|0⟩. (2.142)

In this way we have succeeded in constructing simultaneous eigenkets of N and H with energy eigenvalues E_n = (n + 1/2)ℏω (n=0,1,2,3,...). (2.143)

From (2.137), (2.138), and the orthonormality requirement for {|n⟩}, we obtain the matrix elements ⟨n'|a|n⟩ = √n δ_{n', n-1}, ⟨n'|a†|n⟩ = √(n+1) δ_{n', n+1}. (2.144)

Using these together with x = √(ℏ/(2mω)) (a + a†), p = i√(mℏω/2) (-a + a†), (2.145)

we derive the matrix elements of the x and p operators: ⟨n'|x|n⟩ = √(ℏ/(2mω)) (√n δ_{n', n-1} + √(n+1) δ_{n', n+1}), (2.146a) ⟨n'|p|n⟩ = i√(mℏω/2) (-√n δ_{n', n-1} + √(n+1) δ_{n', n+1}). (2.146b)

Notice that neither x nor p is diagonal in the N-representation we are using. This is not surprising because x and p, like a and a†, do not commute with N.

The operator method can also be used to obtain the energy eigenfunctions in position space. Let us start with the ground state defined by a|0⟩ = 0, (2.147) which, in the x-representation, reads √(mω/(2ℏ)) (x + ℏ/(mω) d/dx) ψ₀(x) = 0. (2.148)

⟨x|p⟩=iħωp ⟨x|V⟩=|a|0⟩=⟨x|x+|0⟩=0. (2.148)

2ħ mω

## 2.3 Simple Harmonic Oscillator

Recalling (1.249), we can regard this as a differential equation for the ground-state wave function ⟨x|0⟩:

(d/dx - x)⟨x|0⟩=0, (2.149)

0dx

where we have introduced

x ≡ ħ, (2.150)

0 mω

which sets the length scale of the oscillator. We see that the normalized solution to (2.149) is

⟨x|0⟩= (1/√π^{1/4} x_0^{1/2}) exp(-x²/(2x_0²)). (2.151)

We can also obtain the energy eigenfunctions for excited states by evaluating

⟨x|1⟩=⟨x|a†|0⟩= (1/√(2x_0)) (d/dx - x)⟨x|0⟩, ⟨x|2⟩=⟨x|(a†)²|0⟩= (1/√(2² * 2!)) (1/x_0) (d/dx - x)²⟨x|0⟩, ...

(2.152)

In general, we obtain

⟨x|n⟩= (1/(π^{1/4} √(2ⁿ n! x_0^{n+1/2}))) (d/dx - x/x_0)ⁿ exp(-x²/(2x_0²)). (2.153)

It is instructive to look at the expectation values of x² and p² for the ground state. First, note that

x²= (ħ/(2mω)) (a² + a†² + a†a + aa†). (2.154)

When we take the expectation value of x², only the last term in (2.154) yields a nonvanishing contribution:

⟨x²⟩= (ħ/(2mω)) * (1/2) = ħ/(4mω). (2.155)

Likewise,

⟨p²⟩= (ħmω)/2. (2.156)

It follows that the expectation values of the kinetic and the potential energies are, respectively,

⟨p²/(2m)⟩= (ħω)/4 = ⟨H⟩/2 and ⟨mω²x²/2⟩= (ħω)/4 = ⟨H⟩/2, (2.157)

as expected from the virial theorem. From (2.146a) and (2.146b), it follows that

⟨x⟩=⟨p⟩=0, (2.158)

which also holds for the excited states. We therefore have

⟨(Δx)²⟩=⟨x²⟩= ħ/(2mω) and ⟨(Δp)²⟩=⟨p²⟩= (ħmω)/2, (2.159)

and we see that the uncertainty relation is satisfied in the minimum uncertainty product form:

⟨(Δx)²⟩⟨(Δp)²⟩= ħ²/4. (2.160)

This is not surprising because the ground-state wave function has a Gaussian shape. In contrast, the uncertainty products for the excited states are larger:

⟨(Δx)²⟩⟨(Δp)²⟩= (n + 1/2)ħ², (2.161)

as the reader may easily verify.

2.3.2 Time Development of the Oscillator

So far we have not discussed the time evolution of oscillator state kets nor of observables like x and p. Everything we have done is supposed to hold at some instant of time, say at t=0; the operators x, p, a, and a† are to be regarded either as Schrödinger picture operators (at all t) or as Heisenberg picture operators at t=0. In the remaining part of this section, we work exclusively in the Heisenberg picture, which means that x, p, a, and a† are all time dependent even though we do not explicitly write x_H(t), and so forth.

The Heisenberg equations of motion for p and x are, from (2.106) and (2.107),

dp/dt = -mω²x (2.162a)

and

dx/dt = p/m. (2.162b)

This pair of coupled differential equations is equivalent to two uncoupled differential equations for a and a†, namely,

da/dt = -iωa (2.163a)

and

da†/dt = iωa†, (2.163b)

whose solutions are

a(t) = a(0) exp(-iωt) and a†(t) = a†(0)exp(iωt). (2.164)

Incidentally, these relations explicitly show that N and H are time-independent operators even in the Heisenberg picture, as they must be. In terms of x and p, we can rewrite (2.164) as

x(t) + i p(t)/(mω) = [x(0) + i p(0)/(mω)] exp(-iωt), (2.165)

x(t) - i p(t)/(mω) = [x(0) - i p(0)/(mω)] exp(iωt).

Equating the Hermitian and anti-Hermitian parts of both sides separately, we deduce

x(t) = x(0) cos ωt + (p(0)/(mω)) sin ωt (2.166a)

and

p(t) = -mω x(0) sin ωt + p(0) cos ωt. (2.166b)

These look the same as the classical equations of motion. We see that the x and p operators “oscillate” just like their classical analogues.

For pedagogical reasons we now present an alternative derivation of (2.166a). Instead of solving the Heisenberg equation of motion, we attempt to evaluate

x(t) = exp(iHt/ħ) x(0) exp(-iHt/ħ). (2.167)

To this end we record a very useful formula:

exp(iGλ) A exp(-iGλ) = A + iλ[G, A] + (i²λ²/2!) [G, [G, A]] + ... + (iⁿλⁿ/n!) [G, [G, [G, ...[G, A]]]...] + ..., (2.168)

where G is a Hermitian operator and λ is a real parameter. We leave the proof of this formula, known as the Baker–Hausdorff lemma as an exercise. Applying this formula to (2.167), we obtain

exp(iHt/ħ) x(0) exp(-iHt/ħ)

= x(0) + (it/ħ) [H, x(0)] + (i²t²/(2!ħ²)) [H, [H, x(0)]] + ... (2.169)

Each term on the right-hand side can be reduced to either x or p by repeatedly using

[H, x(0)] = -iħ p(0)/m (2.170a)

and

[H, p(0)] = iħ mω² x(0). (2.170b)

Thus

exp(iHt/ħ) x(0) exp(-iHt/ħ)

= x(0) + (t/m) p(0) - (1/2!) t² ω² x(0) - (1/3!) (t³ω² p(0)/m) + ...

= x(0) cos ωt + (p(0)/(mω)) sin ωt, (2.171)

in agreement with (2.166a).

From (2.166a) and (2.166b), one may be tempted to conclude that ⟨x⟩ and ⟨p⟩ always oscillate with angular frequency ω. However, this inference is not correct. Take any energy eigenstate characterized by a definite value of n; the expectation value ⟨n|x(t)|n⟩ vanishes because the operators x(0) and p(0) change n by ±1 and |n⟩ and |n±1⟩ are orthogonal. This point is also obvious from our earlier conclusion (see Section 2.1) that the expectation value of an observable taken with respect to a stationary state does not vary with time. To observe oscillations reminiscent of the classical oscillator, we must look at a superposition of energy eigenstates such as

|α⟩ = c_0 |0⟩ + c_1 |1⟩. (2.172)

The expectation value of x(t) taken with respect to (2.172) does oscillate, as the reader may readily verify.

We have seen that an energy eigenstate does not behave like the classical oscillator – in the sense of oscillating expectation values for x and p – no matter how large n may be. We may logically ask: How can we construct a superposition of energy eigenstates that most closely imitates the classical oscillator? In wave function language, we want a wave packet that bounces back and forth without spreading in shape. It turns out that a coherent state defined by the eigenvalue equation for the non-Hermitian annihilation operator a,

a|λ⟩ = λ|λ⟩, (2.173)

with, in general, a complex eigenvalue λ does the desired job. The coherent state has many other remarkable properties.

## 1. When expressed as a superposition of energy (or N) eigenstates,

|λ⟩ = Σ_{n=0}^∞ f(n) |n⟩, (2.174)

the distribution of |f(n)|² with respect to n is of the Poisson type about some mean value n̄: |f(n)|² = (n̄ⁿ / n!) exp(-n̄). (2.175)

2. It can be obtained by translating the oscillator ground state by some finite distance.

## 3. It satisfies the minimum uncertainty product relation at all times

A systematic study of coherent states, pioneered by R. Glauber, is very rewarding; the reader is urged to work out Exercise 2.21 on this subject at the end of this chapter.

## 2.4 Schrödinger’s Wave Equation

2.4.1 Time-Dependent Wave Equation

We now turn to the Schrödinger picture and examine the time evolution of |α, t; t⟩ in the x-representation. In other words, our task is to study the behavior of the wave function

ψ(x', t) = ⟨x'|α, t; t⟩ (2.176)

as a function of time, where |α, t; t⟩ is a state ket in the Schrödinger picture at time t, and ⟨x'| is a time-independent position eigenbra with eigenvalue x'. The Hamiltonian operator is taken to be

H = p²/(2m) + V(x). (2.177)

The potential V(x) is a Hermitian operator; it is also local in the sense that in the x-representation we have

⟨x''|V(x)|x'⟩ = V(x') δ³(x' - x''), (2.178)

where V(x') is a real function of x'. Later in this book we will consider more complicated Hamiltonians: a time-dependent potential V(x,t); a nonlocal but separable potential where the right-hand side of (2.178) is replaced by v_1(x'') v_2(x'); a momentum-dependent interaction of the form p·A + A·p, where A is the vector potential in electrodynamics, and so on.

We now derive Schrödinger’s time-dependent wave equation. We first write the Schrödinger equation for a state ket (2.27) in the x-representation:

iħ ∂/∂t ⟨x'|α, t; t⟩ = ⟨x'|H|α, t; t⟩, (2.179)

where we have used the fact that the position eigenbras in the Schrödinger picture do not change with time. Using (1.252), we can write the kinetic-energy contribution to the right-hand side of (2.179) as

⟨x'|p²/(2m)|α, t; t⟩ = - (ħ²/(2m)) ∇'² ⟨x'|α, t; t⟩. (2.180)

As for V(x), we simply use

⟨x'|V(x) = ⟨x'|V(x'), (2.181)

where V(x') is no longer an operator. Combining everything, we deduce

iħ ∂/∂t ⟨x'|α, t; t⟩ = - (ħ²/(2m)) ∇'² ⟨x'|α, t; t⟩ + V(x') ⟨x'|α, t; t⟩, (2.182)

which we recognize to be the celebrated time-dependent wave equation of E. Schrödinger, usually written as

iħ ∂ψ(x', t)/∂t = - (ħ²/(2m)) ∇'² ψ(x', t) + V(x') ψ(x', t). (2.183)

The quantum mechanics based on wave equation (2.183) is known as wave mechanics. This equation is, in fact, the starting point of many textbooks on quantum mechanics. In our formalism, however, this is just the Schrödinger equation for a state ket written explicitly in the x-basis when the Hamiltonian operator is taken to be (2.177).

2.4.2 The Time-Independent Wave Equation

We now derive the partial differential equation satisfied by energy eigenfunctions. We showed in Section 2.1 that the time dependence of a stationary state is given by exp(-i E_{a'} t/ħ). This enables us to write its wave function as

⟨x'|a', t; t⟩ = ⟨x'|a'⟩ exp(-i E_{a'} t/ħ). (2.184)

(2.184)

where it is understood that initially the system is prepared in a simultaneous eigenstate of A and H with eigenvalues a and E a, respectively. Let us now substitute (2.184) into the time-dependent Schrödinger equation (2.182). We are then led to

$$-\frac{\hbar^2}{2m} \nabla^2 \phi_a(x) + V(x) \phi_a(x) = E_a \phi_a(x). \tag{2.185}$$

This partial differential equation is satisfied by the energy eigenfunction $\phi_a(x)$ with energy eigenvalue $E_a$. Actually, in wave mechanics where the Hamiltonian operator is given as a function of $x$ and $p$, as in (2.177), it is not necessary to refer explicitly to observable $A$ that commutes with $H$ because we can always choose $A$ to be that function of the observables $x$ and $p$ which coincides with $H$ itself. We may therefore omit reference to $a$ and simply write (2.185) as the partial differential equation to be satisfied by the energy eigenfunction $u_E(x)$:

$$-\frac{\hbar^2}{2m} \nabla^2 u_E(x) + V(x) u_E(x) = E u_E(x). \tag{2.186}$$

This is the time-independent wave equation of E. Schrödinger, announced in the first of four monumental papers, all written in the first half of 1926, that laid the foundations of wave mechanics. In the same paper, Schrödinger immediately applied (2.186) to derive the energy spectrum of the hydrogen atom.

To solve (2.186) some boundary condition has to be imposed. Suppose we seek a solution to (2.186) with

$$E < \lim_{|x| \to \infty} V(x), \tag{2.187}$$

where the inequality relation is to hold for $|x| \to \infty$ in any direction. The appropriate boundary condition to be used in this case is

$$u_E(x) \to 0 \quad \text{as} \quad |x| \to \infty. \tag{2.188}$$

Physically this means that the particle is bound or confined within a finite region of space. We know from the theory of partial differential equations that (2.186) subject to boundary condition (2.188) allows nontrivial solutions only for a discrete set of values of $E$. It is in this sense that the time-independent Schrödinger equation (2.186) yields the quantization of energy levels.6 Once the partial differential equation (2.186) is written, the problem of finding the energy levels of microscopic physical systems is as straightforward as that of finding the characteristic frequencies of vibrating strings or membranes. In both cases we solve boundary-value problems in mathematical physics.

A short digression on the history of quantum mechanics is in order here. The fact that exactly solvable eigenvalue problems in the theory of partial differential equations can also be treated using matrix methods was already known to mathematicians in the first quarter of the twentieth century. Furthermore, theoretical physicists like M. Born frequently consulted great mathematicians of the day – D. Hilbert and H. Weyl, in particular. Yet when matrix mechanics was born in the summer of 1925, it did not immediately occur to the theoretical physicists or to the mathematicians to reformulate it using the language of partial differential equations. Six months after Heisenberg’s pioneering paper, wave mechanics was proposed by Schrödinger. However, a close inspection of his papers shows that he was not at all influenced by the earlier works of Heisenberg, Born, and Jordan. Instead, the train of reasoning that led Schrödinger to formulate wave mechanics has its roots in W. R. Hamilton’s analogy between optics and mechanics, on which we will comment later, and the particle-wave hypothesis of L. de Broglie. Once wave mechanics was formulated, many people, including Schrödinger himself, showed the equivalence between wave mechanics and matrix mechanics.

It is assumed that the reader of this book has some experience in solving the time-dependent and time-independent wave equations. He or she should be familiar with the time evolution of a Gaussian wave packet in a force-free region; should be able to solve one-dimensional transmission-reflection problems involving a rectangular potential barrier, and the like; should have seen derived some simple solutions of the time-independent wave equation – a particle in a box, a particle in a square well, the simple harmonic oscillator, the hydrogen atom, and so on – and should also be familiar with some general properties of the energy eigenfunctions and energy eigenvalues, such as (1) the fact that the energy levels exhibit a discrete or continuous spectrum depending on whether or not (2.187) is

6 Schrödinger’s paper that announced (2.186) is appropriately entitled Quantisierung als Eigenwertproblem (Quantization as an Eigenvalue Problem).

satisfied and (2) the property that the energy eigenfunction in one dimension is sinusoidal or damped depending on whether $E - V(x)$ is positive or negative.

In this book, we do not thoroughly cover these more elementary topics and solutions. Some of these are pursued, for example the harmonic oscillator and hydrogen atom, but at a mathematical level somewhat higher than what is usually seen in undergraduate courses. In any case, a brief summary of elementary solutions to Schrödinger’s equations is presented in Appendix B.

### 2.4.3 Interpretations of the Wave Function

We now turn to discussions of the physical interpretations of the wave function. In Section 1.7 we commented on the probabilistic interpretation of $|\psi|^2$ that follows from the fact that $\langle x | \alpha, t_0; t \rangle$ is to be regarded as an expansion coefficient of $|\alpha, t_0; t\rangle$ in terms of the position eigenkets $\{|x\rangle\}$. The quantity $\rho(x, t)$ defined by

$$\rho(x, t) = |\psi(x, t)|^2 = |\langle x | \alpha, t_0; t \rangle|^2 \tag{2.189}$$

is therefore regarded as the probability density in wave mechanics. Specifically, when we use a detector that ascertains the presence of the particle within a small volume element $d^3x$ around $x$, the probability of recording a positive result at time $t$ is given by $\rho(x, t) d^3x$.

In the remainder of this section we use $x$ for $x$ because the position operator will not appear. Using Schrödinger’s time-dependent wave equation, it is straightforward to derive the continuity equation

$$\frac{\partial \rho}{\partial t} + \nabla \cdot j = 0, \tag{2.190}$$

where $\rho(x, t)$ stands for $|\psi|^2$ as before, and $j(x, t)$, known as the probability flux, is given by

$$j(x, t) = -\frac{i\hbar}{2m} \left[ \psi^* \nabla \psi - (\nabla \psi^*) \psi \right] = \frac{\hbar}{m} \operatorname{Im}(\psi^* \nabla \psi). \tag{2.191}$$

The reality of the potential $V$ (or the Hermiticity of the $V$ operator) has played a crucial role in our obtaining this result. Conversely, a complex potential can phenomenologically account for the disappearance of a particle; such a potential is often used for nuclear reactions where incident particles get absorbed by nuclei.

We may intuitively expect that the probability flux $j$ is related to momentum. This is indeed the case for $j$ integrated over all space. From (2.191) we obtain

$$\int d^3x \, j(x, t) = \frac{\langle p \rangle_t}{m}, \tag{2.192}$$

where $\langle p \rangle_t$ is the expectation value of the momentum operator at time $t$.

Equation (2.190) is reminiscent of the continuity equation in fluid dynamics that characterizes a hydrodynamic flow of a fluid in a source-free, sink-free region. Indeed, historically Schrödinger was first led to interpret $|\psi|^2$ as the actual matter density, or $e|\psi|^2$ as the actual electric charge density. If we adopt such a view, we are led to face some bizarre consequences.

A typical argument for a position measurement might go as follows. An atomic electron is to be regarded as a continuous distribution of matter filling up a finite region of space around the nucleus; yet, when a measurement is made to make sure that the electron is at some particular point, this continuous distribution of matter suddenly shrinks to a pointlike particle with no spatial extension. The more satisfactory statistical interpretation of $|\psi|^2$ as the probability density was first given by M. Born.

To understand the physical significance of the wave function, let us write it as

$$\psi(x, t) = \sqrt{\rho(x, t)} \exp\left( \frac{i S(x, t)}{\hbar} \right), \tag{2.193}$$

with $S$ real and $\rho > 0$, which can always be done for any complex function of $x$ and $t$. The meaning of $\rho$ has already been given. What is the physical interpretation of $S$? Noting that

$$\psi^* \nabla \psi = \sqrt{\rho} \nabla \sqrt{\rho} + i \sqrt{\rho} \nabla S, \tag{2.194}$$

we can write the probability flux as [see (2.191)]

$$j = \frac{\rho \nabla S}{m}. \tag{2.195}$$

We now see that there is more to the wave function than the fact that $|\psi|^2$ is the probability density; the gradient of the phase $S$ contains a vital piece of information. From (2.195) we see that the spatial variation of the phase of the wave function characterizes the probability flux; the stronger the phase variation, the more intense the flux. The direction of $j$ at some point $x$ is seen to be normal to the surface of a constant phase that goes through that point.

In the particularly simple example of a plane wave (a momentum eigenfunction)

$$\psi(x, t) \propto \exp\left( \frac{i p \cdot x}{\hbar} - \frac{i E t}{\hbar} \right), \tag{2.196}$$

where $p$ stands for the eigenvalue of the momentum operator. All this is evident because

$$\nabla S = p. \tag{2.197}$$

More generally, it is tempting to regard $\nabla S / \text{mass}$ as some kind of “velocity,”

$$“v” = \frac{\nabla S}{m}, \tag{2.198}$$

and to write the continuity equation (2.190) as

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho “v”) = 0, \tag{2.199}$$

just as in fluid dynamics. However, we would like to caution the reader against a too literal interpretation of $j$ as $\rho$ times the velocity defined at every point in space, because a simultaneous precision measurement of position and velocity would necessarily violate the uncertainty principle.

### 2.4.4 The Classical Limit

We now discuss the classical limit of wave mechanics. First, we substitute $\psi$ written in form (2.193) into both sides of the time-dependent wave equation. Straightforward differentiations lead to

$$\left[ -\frac{\hbar^2}{2m} \nabla^2 \sqrt{\rho} + \frac{2i}{\hbar} (\nabla \sqrt{\rho}) \cdot (\nabla S) - \frac{1}{\hbar^2} \sqrt{\rho} |\nabla S|^2 + \frac{i}{\hbar} \sqrt{\rho} \nabla^2 S + \sqrt{\rho} V \right] = i\hbar \left[ \frac{\partial \sqrt{\rho}}{\partial t} + \frac{i}{\hbar} \sqrt{\rho} \frac{\partial S}{\partial t} \right]. \tag{2.200}$$

So far everything has been exact. Let us suppose now that $\hbar$ can, in some sense, be regarded as a small quantity. The precise physical meaning of this approximation, to which we will come back later, is not evident now, but let us assume

$$\hbar |\nabla^2 S| \ll |\nabla S|^2, \tag{2.201}$$

and so forth. We can then collect terms in (2.200) that do not explicitly contain $\hbar$ to obtain a nonlinear partial differential equation for $S$:

$$\frac{1}{2m} |\nabla S(x, t)|^2 + V(x) + \frac{\partial S(x, t)}{\partial t} = 0. \tag{2.202}$$

We recognize this to be the Hamilton–Jacobi equation in classical mechanics, first written in 1836, where $S(x, t)$ stands for Hamilton’s principal function. So, not surprisingly, in the $\hbar \to 0$ limit, classical mechanics is contained in Schrödinger’s wave mechanics. We have a semicla classical interpretation of the phase of the wave function: h¯ times the phase is equal to Hamilton's principal function provided that h¯ can be regarded as a small quantity. Let us now look at a stationary state with time dependence exp(−iEt/h¯). This time dependence is anticipated from the fact that for a classical system with a constant Hamiltonian, Hamilton's principal function S is separable: S(x,t) = W(x) − Et, (2.203)

where W(x) is called Hamilton's characteristic function (Goldstein et al. (2002), pp.440–444). As time goes on, a surface of a constant S advances in much the same way as a surface of a constant phase in wave optics, a "wavefront," advances. The momentum in the classical Hamilton–Jacobi theory is given by P = ∇S = ∇W, (2.204)

class which is consistent with our earlier identification of ∇S/m with some kind of velocity. In classical mechanics the velocity vector is tangential to the particle trajectory, and as a result we can trace the trajectory by following continuously the direction of the velocity vector. The particle trajectory is like a ray in geometric optics because the ∇S that traces the trajectory is normal to the wavefront defined by a constant S. In this sense geometrical optics is to wave optics what classical mechanics is to wave mechanics.

One might wonder, in hindsight, why this optical-mechanical analogy was not fully exploited in the nineteenth century. The reason is that there was no motivation for regarding Hamilton's principal function as the phase of some traveling wave; the wave nature of a material particle did not become apparent until the 1920s. Besides, the basic unit of action h¯, which must enter into (2.193) for dimensional reasons, was missing in the physics of the nineteenth century.

## 2.5 Elementary Solutions to Schrödinger's Wave Equation

It is both instructive and useful to look at some relatively elementary solutions to (2.186) for particular choices of the potential energy function V(x). In this section we choose some particular examples to illustrate contemporary physics and/or which will be useful in later chapters of this textbook.

2.5.1 Free Particle in Three Dimensions The case V(x) = 0 has fundamental significance. We will consider the solution to Schrödinger's equation here in three dimensions using Cartesian coordinates. The solution in spherical coordinates will be left until our treatment of angular momentum is presented in the next chapter. Equation (2.186) becomes ∇² u_E(x) = −(2mE / h¯²) u_E(x). (2.205)

Define a vector k where k² = k_x² + k_y² + k_z² ≡ (2mE / h¯²) = (p² / h¯²), (2.206)

that is, p = h¯k. Differential equation (2.205) is easily solved using the technique known as "separation of variables." Writing u_E(x) = u_x(x) u_y(y) u_z(z) (2.207)

we arrive at [(1/u_x) d²u_x/dx² + k_x²] + [(1/u_y) d²u_y/dy² + k_y²] + [(1/u_z) d²u_z/dz² + k_z²] = 0. (2.208)

This leads to individual plane wave solutions u_w(w) = c_w e^(ik_w w) for w = x, y, z. Note that one gets the same energy E for values ±k_w.

Collecting these solutions, and combining the normalization constants, we obtain u_E(x) = c_x c_y c_z e^(ik_x x + ik_y y + ik_z z) = C e^(ik·x). (2.209)

The normalization constant C presents the usual difficulties, which are generally handled by using a δ-function normalization condition. It is convenient in many cases, however, to use a "big box" normalization, where all space is contained within a cube of side length L. We impose periodic boundary conditions on the box, and thereby obtain a finite normalization constant C. For any real calculation, we simply let the size L → ∞ at the end of the calculation.

Imposing the condition u_x(x + L) = u_x(x) we have k_x L = 2πn_x where n_x is an integer. That is k_x = (2π/L) n_x, k_y = (2π/L) n_y, k_z = (2π/L) n_z (2.210)

and the normalization criterion becomes 1 = ∫∫∫ dx dy dz u_E*(x) u_E(x) = L³ |C|² (2.211)

in which case C = 1/L^(3/2) and u_E(x) = (1/L^(3/2)) e^(ik·x). (2.212)

The energy eigenvalue is E = (p² / 2m) = (h¯² k² / 2m) = (h¯² / 2m) (2π/L)² (n_x² + n_y² + n_z²). (2.213)

The sixfold degeneracy we mentioned earlier corresponds to the six combinations of (±n_x, ±n_y, ±n_z), but the degeneracy can actually be much larger since, in some cases, there are various combinations of n_x, n_y, and n_z which can give the same E. In fact, in the (realistic) limit where L is very large, there can be a large number of states N which have an energy between E and E + dE. This "density of states" dN/dE is an important quantity for calculations of processes which include free particles. See, for example, the discussion of the photoelectric effect in Section 5.8.

To calculate the density of states, imagine a spherical shell in k space with radius |k| = 2π|n|/L and thickness d|k| = 2π d|n|/L. All states within this shell have energy E = h¯² k²/2m. The number of states dN within this shell is 4π n² d|n|. Therefore dN/dE = (4π n² d|n|) / (h¯² |k| d|k| / m) = (4π L³ / (2π)³) (m |k| / h¯²) = (m^(3/2) E^(1/2) L³) / (2π² h¯³). (2.214)

In a typical "real" calculation, the density of states will be multiplied by some probability that involves u_E*(x) u_E(x). In this case, the factors of L³ will cancel explicitly, so the limit L → ∞ is trivial. This "big box" normalization also yields the correct answer for the probability flux. Rewriting (2.196) with this normalization, we have ψ(x,t) = (1/L^(3/2)) exp(−(ip·x)/h¯ − iEt/h¯) (2.215)

in which case we find j(x,t) = (h¯/m) Im(ψ* ∇ψ) = (h¯k/m) (1/L³) = v ρ (2.216)

where ρ = 1/L³ is indeed the probability density.

2.5.2 The Simple Harmonic Oscillator We saw an elegant solution for the case V(x) = mω² x²/2 in Section 2.3, which yielded the energy eigenvalues, eigenstates, and wave functions. Here, we demonstrate a different approach which solves the differential equation −(h¯² / 2m) d²u_E(x)/dx² + (1/2) mω² x² u_E(x) = E u_E(x). (2.217)

Our approach will introduce the concept of generating functions, a generally useful technique which arises in many treatments of differential eigenvalue problems.

First, transform (2.217) using the dimensionless position y ≡ x/x₀ where x₀ ≡ √(h¯/mω). Also introduce a dimensionless energy variable ε ≡ 2E/h¯ω. The differential equation we need to solve becomes therefore d²u(y)/dy² + (ε − y²) u(y) = 0. (2.218)

For y → ±∞, the solution must tend to zero, otherwise the wave function will not be normalizable and hence unphysical. The differential equation w''(y) − y² w(y) = 0 has solutions w(y) ∝ exp(±y²/2), so we would have to choose the minus sign. We then "remove" the asymptotic behavior of the wave function by writing u(y) = h(y) e^(−y²/2) (2.219)

where the function h(y) satisfies the differential equation d²h/dy² − 2y dh/dy + (ε − 1) h(y) = 0. (2.220)

To this point, we have followed the traditional solution of the simple harmonic oscillator as found in many textbooks. Typically, one would now look for a series solution for h(y) and discover that a normalizable solution is only possible if the series terminates. (In fact, we use this approach for the three-dimensional isotropic harmonic oscillator in this book. See Section 3.7.) One forces this termination by imposing the condition that ε − 1 be an even, nonnegative integer 2n, n = 0,1,2,.... The solutions are then written using the resulting polynomials h_n(y). Of course, ε − 1 = 2n is equivalent to E = (n + 1/2) h¯ω, the quantization relation (2.143).

Let us take a different approach. Consider the "Hermite polynomials" H_n(x) defined by the "generating function" g(x,t) through g(x,t) ≡ e^(−t² + 2tx) (2.221a)

≡ ∑(from n=0 to ∞) [H_n(x) / n!] t^n. (2.221b)

Some properties of the H_n(x) are immediately obvious. For example, H_0(x) = 1. Also, since g(0,t) = e^(−t²) = ∑(from n=0 to ∞) [(-1)^n / n!] t^(2n) (2.222)

it is clear that H_n(0) = 0 if n is odd, since this series only involves even powers of t. On the other hand, if we restrict ourselves to even values of n, we have g(0,t) = e^(−t²) = ∑(from n=0 to ∞) [(-1)^(n/2) / (n/2)!] t^n = ∑(from n=0 to ∞) [(-1)^(n/2) n! / ((n/2)! n!)] t^n (2.223)

and so H_n(0) = (-1)^(n/2) n!/(n/2)!. Also, since g(−x,t) reverses the sign only on terms with odd powers of t, H_n(−x) = (−1)^n H_n(x).

We can take derivatives of g(x,t) to build the Hermite polynomials using recursion relations between them and their derivatives. The trick is that we can differentiate the analytic form of the generating function (2.221a) or the series form (2.221b) and then compare results. For example, if we take the derivative using (2.221a), then ∂g/∂x = 2t g(x,t) = 2 ∑(from n=0 to ∞) [H_n(x) / n!] t^(n+1) = 2 ∑(from n=0 to ∞) [(n+1) H_n(x) / (n+1)!] t^(n+1) (2.224)

where we inserted the series definition of the generating function after taking the derivative. On the other hand, we can take the derivative of (2.221b) directly, in which case ∂g/∂x = ∑(from n=0 to ∞) [H'_n(x) / n!] t^n. (2.225)

Comparing (2.224) and (2.225) shows that H'_n(x) = 2n H_{n−1}(x) (2.226)

This is enough information for us to build the Hermite polynomials: H_0(x) = 1 so H'_0(x) = 0, therefore H_1(x) = 2x so H'_1(x) = 2, therefore H_2(x) = 4x² − 2 so H'_2(x) = 8x, therefore H_3(x) = 8x³ − 12x ...

So far, this is just a curious mathematical exercise. To see why it is relevant to the simple harmonic oscillator, consider the derivative of the generating function with respect to t. If we start with (2.221a) then ∂g/∂t = −2t g(x,t) + 2x g(x,t)

= −∑(from n=0 to ∞) [2 H_n(x) / n!] t^(n+1) + ∑(from n=0 to ∞) [2x H_n(x) / n!] t^n = −∑(from n=0 to ∞) [2n H_{n−1}(x) / n!] t^n + ∑(from n=0 to ∞) [2x H_n(x) / n!] t^n. (2.227)

Or, if we differentiate (2.221b) then we have ∂g/∂t = ∑(from n=1 to ∞) [n H_n(x) / n!] t^(n−1) = ∑(from n=0 to ∞) [H_n(x) / n!] t^n. (2.228)

Comparing (2.227) and (2.228) gives us the recursion relation H_{n+1}(x) = 2x H_n(x) − 2n H_{n−1}(x) (2.229)

which we combine with (2.226) to find H''_n(x) = 2n · 2(n−1) H_{n−2}(x)

= 2n [2x H_{n−1}(x) − H_n(x)]

= 2x H'_n(x) − 2n H_n(x). (2.230)

In other words, the Hermite polynomials satisfy the differential equation H''_n(x) − 2x H'_n(x) + 2n H_n(x) = 0 (2.231)

where n is a nonnegative integer. This, however, is the same as the Schrödinger equation written as (2.220) since ε − 1 = 2n. That is, the wave functions for the simple harmonic oscillator are given by u_n(x) = c_n H_n(√(mω/h¯) x) e^(−mω x² / 2h¯) (2.232)

up to some normalization constant c_n. This constant can be determined from the orthogonality relationship ∫_{−∞}^{∞} H_n(x) H_m(x) e^{−x²} dx = √π 2^n n! δ_{nm} (2.233)

which is easily proved using the generating function. See Problem 2.25 at the end of this chapter.

Generating functions have a usefulness that far outreaches our limited application here. Among other things, many of the orthogonal polynomials which arise from solving the Schrödinger equation for different potentials, can be derived from generating functions. See, for example, Problem 3.30 in Chapter 3. The interested reader is encouraged to pursue this further, probably best from any one of the many excellent texts on mathematical physics.

2.5.3 The Linear Potential

Perhaps the first potential energy function, with bound states, to come to mind is the linear potential, namely V(x) = k|x| (2.234)

where k is an arbitrary positive constant. Given a total energy E, this potential has a classical turning point at a value x = a where E = ka. This point will be important for understanding the quantum behavior of a particle of mass m bound by this potential.

The Schrödinger equation becomes −ℏ²/2m * d²u_E/dx² + k|x| u_E(x) = E u_E(x). (2.235)

It is easiest to deal with the absolute value by restricting our attention to x ≥ 0. We can do this because V(−x) = V(x), so there are two types of solutions, namely u_E(−x) = ±u_E(x). In either case, we need u_E(x) to tend towards zero as x → ∞. If u_E(−x) = −u_E(x), then we need u_E(0) = 0. On the other hand, if u_E(−x) = +u_E(x), then we have u'_E(0) = 0, since u_E(ε) − u_E(−ε) ≡ 0, even for ε → 0. (As we will discuss in Chapter 4, we refer to these solutions as “odd” and “even” parity.)

Once again, we write the differential equation in terms of dimensionless variables, based on appropriate scales for length and energy. In this case, the dimensionless length scale is x₀ = (ℏ²/mk)^{1/3} and the dimensionless energy scale is E₀ = k x₀ = (ℏ²k²/m)^{1/3}. Defining y ≡ x/x₀ and ε ≡ E/E₀ allows us to rewrite (2.235) as d²u_E/dy² − 2(y − ε) u_E(y) = 0, y ≥ 0. (2.236)

Notice that y = ε when x = E/k, i.e. the classical turning point x = a. In fact, defining a translated position variable z ≡ 2^{1/3}(y − ε), (2.236) becomes d²u_E/dz² − z u_E(z) = 0. (2.237)

This is the Airy equation, and the solution is the Airy function Ai(z), plotted in Figure 2.3. The Airy function has a peculiar behavior, oscillatory for negative values of the argument, and decreasing rapidly towards zero for positive values. Of course, this is exactly the behavior we expect for the wave function, since z = 0 is the classical turning point.

Note that the boundary conditions at x = 0 translate into zeros for either Ai'(z) or Ai(z) where z = −2^{1/3}ε. In other words, the zeros of the Airy function or its derivative determine the quantized energies. One finds that Ai'(z) = 0 for z = −1.019, −3.249, −4.820,... (even) (2.238)

Ai(z) = 0 for z = −2.338, −4.088, −5.521,... (odd). (2.239)

For example, the ground-state energy is E₀ = (1.019/2^{1/3})(ℏ²k²/m)^{1/3}.

[Figure 2.3: The Airy function.]

[Figure 2.4: Experimental observation of the quantum-mechanical states of a bouncing neutron, from Nesvizhevsky et al., Phys. Rev. D, 67 (2003) 102002. The solid curve is a fit to the data based on classical physics. Note that the vertical scale is logarithmic.]

The quantum-theoretical treatment of the linear potential may appear to have little to do with the real world. It turns out, however, that a potential of type (2.234) is actually of practical interest in studying the energy spectrum of a quark-antiquark bound system, called quarkonium. In this case, the x in (2.234) is replaced by the quark-antiquark separation distance r. This constant k is empirically estimated to be in the neighborhood of 1 GeV/fm ≈ 1.6 × 10⁵ N, (2.240)

which corresponds to a gravitational force of about 16 tons.

Indeed, another real world example of the linear potential is the “bouncing ball.” One interprets (2.234) as the potential energy of a ball of mass m at a height x above the floor, and k = mg where g is the local acceleration due to gravity. Of course, this is the potential energy only for x ≥ 0 as there is an infinite potential barrier which causes the ball to “bounce.” Quantum mechanically, this means that only the odd parity solutions (2.239) are allowed.

The bouncing ball happens to be one of those rare cases where quantum-mechanical effects can be observed macroscopically. The trick is to have a very low mass “ball,” which has been achieved with neutrons by a group working at the Institut Laue-Langevin (ILL) in Grenoble, France. For neutrons with m = 1.68 × 10⁻²⁷ kg, the characteristic length scale is x₀ = (ℏ²/m²g)^{1/3} = 7.40 μm. The “allowed heights” to which a neutron can bounce are (2.338/2^{1/3})x₀ = 14 μm, (4.088/2^{1/3})x₀ = 24 μm, (5.521/2^{1/3})x₀ = 32 μm, and so on. These are small, but measurable with precision mechanical devices and very low energy, aka “ultracold,” neutrons. The experimenters’ results are shown in Figure 2.4. Plotted is the detected neutron rate as a function of the height of a slit which only allows neutrons to pass if they exceed this height. No neutrons are observed unless the height is at least ≈14 μm, and clear breaks are observed at ≈24 μm and ≈32 μm, in excellent agreement with the predictions of quantum mechanics.

2.5.4 The WKB (Semiclassical) Approximation

Having solved the problem of a linear potential, it is worthwhile to introduce an important approximation technique known as the WKB solution, after G. Wentzel, A. Kramers, and L. Brillouin. This technique is based on making use of regions where the wavelength is much shorter than the typical distance over which the potential energy varies. Such is never the case near classical turning points, but this is where the linear potential solution can be used to join the solutions on either side of them.

Again restricting ourselves to one dimension, we write Schrödinger’s wave equation as d²u_E/dx² + (2m/ℏ²)(E − V(x)) u_E(x) = 0. (2.241)

Define the quantities k(x) ≡ [(2m/ℏ²)(E − V(x))]^{1/2} for E > V(x) (2.242a)

k(x) ≡ −i κ(x) ≡ −i [(2m/ℏ²)(V(x) − E)]^{1/2} for E < V(x) (2.242b)

and so (2.241) becomes d²u_E/dx² + [k(x)]² u_E(x) = 0. (2.243)

Now, if V(x) were not changing with x, then k(x) would be a constant, and u(x) ∝ exp(±ikx) would solve (2.243). Consequently, if we assume that V(x) varies only “slowly” with x, then we are tempted to try a solution of the form u_E(x) ≡ exp[iW(x)/ℏ]. (2.244)

(The reason for including the ℏ will become apparent at the end of this section, when we discuss the physical interpretation of the WKB approximation.) In this case, (2.243) becomes iℏ d²W/dx² − (dW/dx)² + ℏ²[k(x)]² = 0 (2.245)

which is completely equivalent to Schrödinger’s equation, although rewritten in what appears to be a nasty form. However, we consider a solution to this equation under the condition that ℏ d²W/dx² << (dW/dx)². (2.246)

This quantifies our notion of a “slowly varying” potential V(x), and we will return soon to the physical significance of this condition.

Forging ahead for now, we use the condition (2.246) with our differential equation (2.245) to write a lowest-order approximation for W(x), namely W'(x) = ±ℏ k(x) (2.247)

leading to a first-order approximation for W(x), based on (dW/dx)² = ℏ²[k(x)]² + iℏ W''(x)

= ℏ²[k(x)]² ± iℏ² k'(x) (2.248)

where the second term in (2.248) is much smaller than the first, so that W(x) ≈ W₀(x) = ±ℏ ∫^{x}_{x'} [k²(x') ± i k'(x')]^{1/2} dx' ≈ ±ℏ ∫^{x}_{x'} k(x') [1 ± i k'(x')/(2k²(x'))] dx' = ±ℏ ∫^{x}_{x'} k(x') dx' + (i/2) ℏ ln[k(x)]. (2.249)

The WKB approximation for the wave function is given by (2.244) and the first-order approximation for (2.249) for W(x), namely u_E(x) ≈ exp[iW(x)/ℏ] = (1/[k(x)]^{1/2}) exp[±i ∫^{x}_{x'} k(x') dx']. (2.250)

Note that this specifies a choice of two solutions (±) either in the region where E > V(x), with k(x) from (2.242a), or in the region where E < V(x), with k(x) from (2.242b). Joining these two solutions across the classical turning point is the next task.

We do not discuss this joining procedure in detail, as it is discussed in many places (Schiff (1968), pp. 268–276, or Merzbacher (1998), Chapter 7, for example). Instead, we content ourselves with presenting the results of such an analysis for a potential well, schematically shown in Figure 2.5, with two turning points, x₁ and x₂. The wave function must behave like (2.250), with k(x) given by (2.242a) in region II, and by (2.242b) in regions I and III. The solutions in the neighborhood of the turning points, shown as a dashed line in Figure 2.5, are given by Airy functions, since we assume a linear approximation to the potential in these regions. Note that the asymptotic dependences of the Airy function are Ai(z) → (1/2√π) z^{-1/4} exp[−(2/3) z^{3/2}] z → +∞ (2.251a)

Ai(z) → (1/√π) |z|^{-1/4} cos[(2/3)|z|^{3/2} − π/4] z → −∞. (2.251b)

[Figure 2.5: Schematic diagram for behavior of the wave function u_E(x) in a potential well V(x) with turning points x₁ and x₂. Note the similarity with Figure 2.3 near the turning points.]

For connecting regions I and II, the correct linear combination of the two solutions (2.250) is determined by choosing the integration constants in such a way that (1/[V(x)−E]^{1/4}) exp[−(1/ℏ) ∫^{x₁}_{x} √(2m[V(x')−E]) dx']

→ (2/[E−V(x)]^{1/4}) cos[(1/ℏ) ∫^{x}_{x₁} √(2m[E−V(x')]) dx' − π/4]. (2.252)

Likewise, from region III into region II we have (1/[V(x)−E]^{1/4}) exp[−(1/ℏ) ∫^{x}_{x₂} √(2m[V(x')−E]) dx']

→ (2/[E−V(x)]^{1/4}) cos[(1/ℏ) ∫^{x₂}_{x} √(2m[E−V(x')]) dx' + π/4]. (2.253)

Of course, we must obtain the same form for the wave function in region II, regardless of which turning point is analyzed. This implies that the arguments of the cosine in (2.252) and (2.253) must differ at most by an integer multiple of π [not of 2π, because the signs of both sides of (2.253) can be reversed]. In this way we obtain a very interesting consistency condition, ∫^{x₂}_{x₁} √(2m[E−V(x)]) dx = (n + 1) π ℏ (n = 0, 1, 2, 3,...). (2.254)

Apart from the difference between n + 1 and n, this equation is simply the quantization condition of the old quantum theory due to A. Sommerfeld and W. Wilson, originally written in 1915 as ∫ p dq = n h, (2.255)

where h is Planck’s h, not Dirac’s ℏ, and the integral is evaluated over one whole period of the classical motion.

classical motion, from x1 to x2 and back.

## 2.5 Elementary Solutions to Schrödinger’s Wave Equation

Equation (2.254) can be used to obtain approximate expressions for the energy levels of a particle confined in a potential well. As an example, we consider the energy spectrum of a ball bouncing up and down over a hard surface, that is the "bouncing neutrons" discussed earlier in this section, namely V = { mgx for x > 0, ∞ for x < 0, } (2.256)

where x stands for the height of the ball measured from the hard surface. One might be tempted to use (2.254) directly with x1 = 0, x2 = E/(mg), (2.257)

which are the classical turning points of this problem. We note, however, that (2.254) was derived under the assumption that the WKB wave function "leaks into" the x < x1 region, while in our problem the wave function must strictly vanish for x ≤ x1 = 0. A much more satisfactory approach to this problem is to consider the odd-parity solutions, guaranteed to vanish at x = 0, of a modified problem defined by V(x) = mg|x| (−∞ < x < ∞) (2.258)

whose turning points are x1 = −E/(mg), x2 = E/(mg). (2.259)

The energy spectrum of the odd-parity states for this modified problem must clearly be the same as that of the original problem. The quantization condition then becomes ∫_{-E/mg}^{E/mg} dx √[2m(E−mg|x|)] = (n_{odd} + 1) π ħ (n_{odd} = 1,3,5,...) (2.260)

or, equivalently, ∫_{0}^{E/mg} dx √[2m(E−mgx)] = (n−1) π ħ (n=1,2,3,4,...). (2.261)

This integral is elementary, and we obtain E_n = (3(n−1)π/4)^{2/3} (mg²ħ²)^{1/3} (2.262)

for the quantized energy levels of the bouncing ball.

Table 2.2 compares the WKB approximation to the exact solution, using zeros of the Airy function, for the first 10 energy levels. We see that agreement is excellent even for small values of n and essentially exact for n ≫ 10.

Before concluding, let us return to the interpretation of the condition (2.246). It is exact in the case ħ → 0, suggesting a connection between the WKB approximation and the classical limit. In fact, using (2.244) the time-dependent wave function becomes ψ(x,t) ∝ u_n(x) exp(−iE_n t/ħ) = exp(iW(x)/ħ − iEt/ħ). (2.263)

Table 2.2: The Quantized Energies of a Bouncing Ball in Units of (mg²ħ²/2)^{1/3}

n      WKB      Exact 1      2.320    2.338 2      4.082    4.088 3      5.517    5.521 4      6.784    6.787 5      7.942    7.944 6      9.021    9.023 7      10.039   10.040 8      11.008   11.009 9      11.935   11.936 10     12.828   12.829

Comparing this to (2.193) and (2.203) we see that W(x) corresponds directly to Hamilton’s characteristic function. Indeed, condition (2.246) is the same as (2.201), the condition for reaching the classical limit. For these reasons, the WKB approximation is frequently referred to as a "semiclassical" approximation.

We also note that condition (2.246) is equivalent to |k'(x)| ≪ |k²(x)|. In terms of the de Broglie wavelength divided by 2π, this condition amounts to λ = ħ / √[2m(E−V(x))] ≪ 2[E−V(x)] / |dV/dx|. (2.264)

In other words, λ must be small compared with the characteristic distance over which the potential varies appreciably. Roughly speaking, the potential must be essentially constant over many wavelengths. Thus we see that the semiclassical picture is reliable in the short-wavelength limit.

## 2.6 Propagators and Feynman Path Integrals

2.6.1 Propagators in Wave Mechanics

In Section 2.1 we showed how the most general time-evolution problem with a time-independent Hamiltonian can be solved once we expand the initial ket in terms of the eigenkets of an observable that commutes with H. Let us translate this statement into the language of wave mechanics. We start with |α, t0; t⟩ = exp[−iH(t−t0)/ħ] |α, t0⟩ = ∑_a' |a'⟩⟨a'|α, t0⟩ exp[−iE_a'(t−t0)/ħ]. (2.265)

a'

Multiplying both sides by ⟨x'| on the left, we have ⟨x'|α, t0; t⟩ = ∑_a' ⟨x'|a'⟩⟨a'|α, t0⟩ exp[−iE_a'(t−t0)/ħ], (2.266)

a' which is of the form ψ(x', t) = ∑_a' c_{a'}(t) u_{a'}(x') exp[−iE_a'(t−t0)/ħ], (2.267)

a' with u_{a'}(x') = ⟨x'|a'⟩ (2.268)

standing for the eigenfunction of operator A with eigenvalue a'. Note also that ⟨a'|α, t0⟩ = ∫ d³x' ⟨a'|x'⟩⟨x'|α, t0⟩, (2.269)

which we recognize as the usual rule in wave mechanics for getting the expansion coefficients of the initial state: c_{a'}(t0) = ∫ d³x' u_{a'}^*(x') ψ(x', t0). (2.270)

All this should be straightforward and familiar. Now (2.266) together with (2.269) can also be visualized as some kind of integral operator acting on the initial wave function to yield the final wave function: ψ(x'', t) = ∫ d³x' K(x'', t; x', t0) ψ(x', t0). (2.271)

Here the kernel of the integral operator, known as the propagator in wave mechanics, is given by K(x'', t; x', t0) = ∑_a' ⟨x''|a'⟩⟨a'|x'⟩ exp[−iE_a'(t−t0)/ħ]. (2.272)

a' In any given problem the propagator depends only on the potential and is independent of the initial wave function. It can be constructed once the energy eigenfunctions and their eigenvalues are given.

Clearly, the time evolution of the wave function is completely predicted if K(x'', t; x', t0) is known and ψ(x', t0) is given initially. In this sense Schrödinger’s wave mechanics is a perfectly causal theory. The time development of a wave function subjected to some potential is as "deterministic" as anything else in classical mechanics provided that the system is left undisturbed. The only peculiar feature, if any, is that when a measurement intervenes, the wave function changes abruptly, in an uncontrollable way, into one of the eigenfunctions of the observable being measured.

There are two properties of the propagator worth recording here. First, for t > t0, K(x'', t; x', t0) satisfies Schrödinger’s time-dependent wave equation in the variables x'' and t, with x' and t0 fixed. This is evident from (2.272) because ⟨x''|a'⟩ exp[−iE_a'(t−t0)/ħ], being the wave function corresponding to U(t,t0)|a'⟩, satisfies the wave equation. Second, lim_{t→t0} K(x'', t; x', t0) = δ³(x''−x'), (2.273)

which is also obvious; as t → t0, because of the completeness of {|a'⟩}, sum (2.272) just reduces to ⟨x''|x'⟩.

Because of these two properties, the propagator (2.272), regarded as a function of x'', is simply the wave function at t of a particle which was localized precisely at x' at some earlier time t0. Indeed, this interpretation follows, perhaps more elegantly, from noting that (2.272) can also be written as K(x'', t; x', t0) = ⟨x''| exp[−iH(t−t0)/ħ] |x'⟩, (2.274)

where the time-evolution operator acting on |x'⟩ is just the state ket at time t of a system that was localized precisely at x' at time t0 (< t). If we wish to solve a more general problem where the initial wave function extends over a finite region of space, all we have to do is multiply ψ(x', t0) by the propagator K(x'', t; x', t0) and integrate over all space (that is, over x'). In this manner we can add the various contributions from different positions (x'). This situation is analogous to one in electrostatics; if we wish to find the electrostatic potential due to a general charge distribution ρ(x'), we first solve the point-charge problem, multiply the point-charge solution with the charge distribution, and integrate: φ(x) = ∫ d³x' ρ(x') / |x−x'|. (2.275)

The reader familiar with the theory of the Green functions must have recognized by this time that the propagator is simply the Green function for the time-dependent wave equation satisfying [−(ħ²/2m) ∇'² + V(x') − iħ ∂/∂t] K(x'', t; x', t0) = −iħ δ³(x''−x') δ(t−t0) (2.276)

with the boundary condition K(x', t; x', t0) = 0, for t < t0. (2.277)

The delta function δ(t−t0) is needed on the right-hand side of (2.276) because K varies discontinuously at t = t0.

The particular form of the propagator is, of course, dependent on the particular potential to which the particle is subjected. Consider, as an example, a free particle in one dimension. The obvious observable that commutes with H is momentum; |p'⟩ is a simultaneous eigenket of the operators p and H: p|p'⟩ = p'|p'⟩, H|p'⟩ = (p'²/2m) |p'⟩. (2.278)

The momentum eigenfunction is just the transformation function of Section 1.7 [see (1.264)] which is of the plane wave form. Combining everything, we have K(x'', t; x', t0) = (1/2πħ) ∫_{−∞}^{∞} dp' exp[ip'(x''−x')/ħ] exp[−ip'²(t−t0)/(2mħ)]. (2.279)

The Alternatively, the path-integral method to be described later. Notice that (2.282) is a periodic function of t with angular frequency ω, the classical oscillator frequency. This means, among other things, that a particle initially localized precisely at x' will return to its original position with certainty at 2π/ω (4π/ω, and so forth) later.

Certain space and time integrals derivable from K(x'', t; x', t) are of considerable interest. Without loss of generality we set t = 0 in the following. The first integral we consider is obtained by setting x'' = x' and integrating over all space. We have G(t) ≡ ∫ d^3 x' K(x', t; x', 0) = ∫ d^3 x' ∑ |⟨x' | a'⟩|^2 exp(-i E_{a'} t / ℏ) = ∑ exp(-i E_{a'} t / ℏ). (2.284)

This result is anticipated; recalling (2.274), we observe that setting x' = x'' and integrating are equivalent to taking the trace of the time-evolution operator in the x-representation. But the trace is independent of representations; it can be evaluated more readily using the {|a'} basis where the time-evolution operator is diagonal, which immediately leads to the last line of (2.284). Now we see that (2.284) is just the "sum over states," reminiscent of the partition function in statistical mechanics. In fact, if we analytically continue in the t variable and make t purely imaginary, with β defined by it / ℏ = β (2.285)

real and positive, we can identify (2.284) with the partition function itself: Z = ∑ exp(-β E_{a'}). (2.286)

For this reason some of the techniques encountered in studying propagators in quantum mechanics are also useful in statistical mechanics.

Next, let us consider the Laplace–Fourier transform of G(t): G̃(E) ≡ -i ∫_0^∞ dt G(t) exp(i E t / ℏ) / ℏ = -i ∫_0^∞ dt ∑ exp(-i E_{a'} t / ℏ) exp(i E t / ℏ) / ℏ. (2.287)

The integrand here oscillates indefinitely. But we can make the integral meaningful by letting E acquire a small positive imaginary part: E → E + iε. (2.288)

We then obtain, in the limit ε → 0, G̃(E) = ∑ 1 / (E - E_{a'}). (2.289)

Observe now that the complete energy spectrum is Lagrange’s equation of motion can be obtained.

2.6.4 Feynman’s Formulation

The basic difference between classical mechanics and quantum mechanics should now be apparent. In classical mechanics a definite path in the xt-plane is associated with the particle’s motion; in contrast, in quantum mechanics all possible paths must play roles including those which do not bear any resemblance to the classical path. Yet we must somehow be able to reproduce classical mechanics in a smooth manner in the limit ℏ → 0. How are we to accomplish this?

As a young graduate student at Princeton University, R.P. Feynman tried to attack this problem. In looking for a possible clue, he was said to be intrigued by a mysterious remark in Dirac’s book which, in our notation, amounts to the following statement:

exp[ i ∫_{t_2}^{t_1} dt L_classical(x, ẋ) ] corresponds to ⟨x_2, t_2 | x_1, t_1⟩.

ℏ

Feynman attempted to make sense out of this remark. Is “corresponds to” the same thing as “is equal to” or “is proportional to”? In so doing he was led to formulate a space-time approach to quantum mechanics based on path integrals.

In Feynman’s formulation the classical action plays a very important role. For compactness, we introduce a new notation:

S(n,n−1) ≡ ∫_{t_{n−1}}^{t_n} dt L_classical(x, ẋ). (2.300)

Because L_classical is a function of x and ẋ, S(n,n−1) is defined only after a definite classical path is specified along which the integration is to be carried out. So even though the path dependence is not explicit in this notation, it is understood that we are considering a particular path in evaluating the integral. Imagine now that we are following some prescribed path. We concentrate our attention on a small segment along that path, say between (x_{n−1}, t_{n−1}) and (x_n, t_n). According to Dirac, we are instructed to associate exp[i S(n,n−1)/ℏ] with that segment. Going along the definite path we are set to follow, we successively multiply expressions of this type to obtain

∏_{n=2}^N exp[ i S(n,n−1)/ℏ ] = exp[ i ∑_{n=2}^N S(n,n−1)/ℏ ] = exp[ i S(N,1)/ℏ ]. (2.301)

This does not yet give ⟨x_N, t_N | x_1, t_1⟩; rather, this equation is the contribution to ⟨x_N, t_N | x_1, t_1⟩ arising from the particular path we have considered. We must still integrate over x_2, x_3, ..., x_{N−1}. At the same time, exploiting the composition property, we let the time interval between t_{n−1} and t_n be infinitesimally small. Thus our candidate expression for ⟨x_N, t_N | x_1, t_1⟩ may be written, in some loose sense, as

⟨x_N, t_N | x_1, t_1⟩ ∼ ∑_{all paths} exp[ i S(N,1)/ℏ ], (2.302)

where the sum is to be taken over an innumerably infinite set of paths!

Before presenting a more precise formulation, let us see whether considerations along this line make sense in the classical limit. As ℏ → 0, the exponential in (2.302) oscillates very violently, so there is a tendency for cancellation among various contributions from neighboring paths. This is because exp[iS/ℏ] for some definite path and exp[iS/ℏ] for a slightly different path have very different phases because of the smallness of ℏ. So most paths do not contribute when ℏ is regarded as a small quantity. However, there is an important exception.

Suppose that we consider a path that satisfies

δS(N,1) = 0, (2.303)

where the change in S is due to a slight deformation of the path with the end points fixed. This is precisely the classical path by virtue of Hamilton’s principle. We denote the S that satisfies (2.303) by S_min. We now attempt to deform the path a little bit from the classical path. The resulting S is still equal to S_min to first order in deformation. This means that the phase of exp[iS/ℏ] does not vary very much as we deviate slightly from the classical path even if ℏ is small. As a result, as long as we stay near the classical path, constructive interference between neighboring paths is possible. In the ℏ → 0 limit, the major contributions must then arise from a very narrow strip (or a tube in higher dimensions) containing the classical path, as shown in Figure 2.7. Our (or Feynman’s) guess based on Dirac’s mysterious remark makes good sense because the classical path is singled out in the ℏ → 0 limit. To formulate Feynman’s conjecture more precisely, let us go back to ⟨x_n, t_n | x_{n−1}, t_{n−1}⟩, where the time difference t_n − t_{n−1} is assumed to be infinitesimally small. We write

⟨x_n, t_n | x_{n−1}, t_{n−1}⟩ = 1/w(Δt) exp[ i S(n,n−1)/ℏ ], (2.304)

117 2.6 Propagators and Feynman Path Integrals

where we evaluate S(n,n−1) in a moment in the Δt → 0 limit. Notice that we have inserted a weight factor, 1/w(Δt), which is assumed to depend only on the time interval t_n − t_{n−1} and not on V(x). That such a factor is needed is clear from dimensional considerations; according to the way we normalized our position eigenkets, ⟨x_n, t_n | x_{n−1}, t_{n−1}⟩ must have the dimension of 1/length.

We now look at the exponential in (2.304). Our task is to evaluate the Δt → 0 limit of S(n,n−1). Because the time interval is so small, it is legitimate to make a straight-line approximation to the path joining (x_{n−1}, t_{n−1}) and (x_n, t_n) as follows:

S(n,n−1) = ∫_{t_{n−1}}^{t_n} dt [ m ẋ²/2 − V(x) ]

≈ Δt [ m (x_n − x_{n−1})² / (2 Δt²) − V( (x_n + x_{n−1})/2 ) ]. (2.305)

As an example, we consider specifically the free-particle case, V=0. Equation (2.304) now becomes

⟨x_n, t_n | x_{n−1}, t_{n−1}⟩ = 1/w(Δt) exp[ i m (x_n − x_{n−1})² / (2 ℏ Δt) ]. (2.306)

We see that the exponent appearing here is completely identical to the one in the expression for the free-particle propagator (2.280). The reader may work out a similar comparison for the simple harmonic oscillator.

We remarked earlier that the weight factor 1/w(Δt) appearing in (2.304) is assumed to be independent of V(x), so we may as well evaluate it for the free particle. Noting the orthonormality, in the sense of δ-function, of Heisenberg picture position eigenkets at equal times,

⟨x_n, t_n | x_{n−1}, t_{n−1}⟩ |_{t_n = t_{n−1}} = δ(x_n − x_{n−1}), (2.307)

we obtain

1/w(Δt) = √( m / (2π i ℏ Δt) ), (2.308)

where we have used

∫_{−∞}^∞ dξ exp( i m ξ² / (2 ℏ Δt) ) = √( 2π i ℏ Δt / m ), (2.309a)

and

lim_{Δt→0} √( m / (2π i ℏ Δt) ) exp( i m ξ² / (2 ℏ Δt) ) = δ(ξ). (2.309b)

This weight factor is, of course, anticipated from the expression for the free-particle propagator (2.280).

To summarize, as Δt → 0, we are led to

⟨x_n, t_n | x_{n−1}, t_{n−1}⟩ = √( m / (2π i ℏ Δt) ) exp[ i S(n,n−1)/ℏ ]. (2.310)

The final expression for the transition amplitude with t_N − t_1 finite is

⟨x_N, t_N | x_1, t_1⟩ = lim_{N→∞} [ m / (2π i ℏ Δt) ]^{(N−1)/2} × ∫ dx_{N−1} ∫ dx_{N−2} ··· ∫ dx_2 ∏_{n=2}^N exp[ i S(n,n−1)/ℏ ], (2.311)

where the N → ∞ limit is taken with x_N and t_N fixed. It is customary here to define a new kind of multidimensional (in fact, infinite-dimensional) integral operator

∫_{x_1}^{x_N} D[x(t)] ≡ lim_{N→∞} [ m / (2π i ℏ Δt) ]^{(N−1)/2} ∫ dx_{N−1} ∫ dx_{N−2} ··· ∫ dx_2 (2.312)

and write (2.311) as

⟨x_N, t_N | x_1, t_1⟩ = ∫_{x_1}^{x_N} D[x(t)] exp[ (i/ℏ) ∫_{t_1}^{t_N} dt L_classical(x, ẋ) ]. (2.313)

This expression is known as Feynman’s path integral. Its meaning as the sum over all possible paths should be apparent from (2.311).

Our steps leading to (2.313) are not meant to be a derivation. Rather, we (or Feynman) have attempted a new formulation of quantum mechanics based on the concept of paths, motivated by Dirac’s mysterious remark. The only ideas we borrowed from the conventional form of quantum mechanics are (1) the superposition principle (used in summing the contributions from various alternate paths), (2) the composition property of the transition amplitude, and (3) classical correspondence in the ℏ → 0 limit.

Even though we obtained the same result as the conventional theory for the free-particle case, it is now obvious, from what we have done so far, that Feynman’s formulation is completely equivalent to Schrödinger’s wave mechanics. We conclude this section by proving that Feynman’s expression for ⟨x_N, t_N | x_1, t_1⟩ indeed satisfies Schrödinger’s time-dependent wave equation in the variables x_N, t_N, just as the propagator defined by (2.272).

We start with

⟨x_N, t_N | x_1, t_1⟩ = ∫ dx_{N−1} ⟨x_N, t_N | x_{N−1}, t_{N−1}⟩ ⟨x_{N−1}, t_{N−1} | x_1, t_1⟩ = ∫_{−∞}^∞ dx_{N−1} √( m / (2π i ℏ Δt) ) exp{ (i/ℏ)[ m (x_N − x_{N−1})² / (2 Δt) − V Δt ] } × ⟨x_{N−1}, t_{N−1} | x_1, t_1⟩, (2.314)

where we have assumed t_N − t_{N−1} to be infinitesimal. Introducing

ξ = x_N − x_{N−1} (2.315)

and letting x_N → x and t_N → t + Δt, we obtain

⟨x, t + Δt | x_1, t_1⟩ = √( m / (2π i ℏ Δt) ) ∫_{−∞}^∞ dξ exp[ (i/ℏ)( m ξ² / (2 Δt) − V Δt ) ] ⟨x − ξ, t | x_1, t_1⟩. (2.316)

As is evident from (2.309b), in the limit Δt → 0, the major contribution to this integral comes from the ξ ≈ 0 region. It is therefore legitimate to expand ⟨x − ξ, t | x_1, t_1⟩ in powers of ξ. We also expand ⟨x, t + Δt | x_1, t_1⟩ and exp(−i V Δt / ℏ) in powers of Δt, so

⟨x, t | x_1, t_1⟩ + Δt ∂/∂t ⟨x, t | x_1, t_1⟩ = √( m / (2π i ℏ Δt) ) ∫_{−∞}^∞ dξ exp( i m ξ² / (2 ℏ Δt) ) [1 − i V Δt / ℏ + ··· ]

× [ ⟨x, t | x_1, t_1⟩ − ξ ∂/∂x ⟨x, t | x_1, t_1⟩ + (ξ²/2) ∂²/∂x² ⟨x, t | x_1, t_1⟩ + ··· ], (2.317)

where we have dropped a term linear in ξ because it vanishes when integrated with respect to ξ. The ⟨x, t | x_1, t_1⟩ term on the left-hand side just matches the leading term on the right-hand side because of (2.309a). Collecting terms first order in Δt, we obtain

Δt ∂/∂t ⟨x, t | x_1, t_1⟩ = [ (2π i ℏ / m)^{−3/2} √(2π) / (2π i ℏ Δt) ] ⟨x, t | x_1, t_1⟩ − (Δt V / ℏ) ⟨x, t | x_1, t_1⟩, (2.318)

where we have used

∫_{−∞}^∞ dξ ξ² exp( i m ξ² / (2 ℏ Δt) ) = √(2π) ( i ℏ Δt / m )^{3/2}, (2.319)

obtained by differentiating (2.309a) with respect to Δt. In this manner we see that ⟨x, t | x_1, t_1⟩ satisfies Schrödinger’s time-dependent wave equation:

∂ iℏ ∂² ih̄ |x,t|x,t⟩ = − |x,t|x,t⟩ + V|x,t|x,t⟩. (2.320)

∂t 1 1 2m ∂x² 1 1 1 1

Thus we can conclude that |x,t|x,t⟩ constructed according to Feynman’s prescription is 1 1 the same as the propagator in Schrödinger’s wave mechanics.

Feynman’s space-time approach based on path integrals is not too convenient for attacking practical problems in nonrelativistic quantum mechanics. Even for the simple harmonic oscillator it is rather cumbersome to evaluate explicitly the relevant path integral. ¹¹ However, his approach is extremely gratifying from a conceptual point of view. By imposing a certain set of sensible requirements on a physical theory, we are inevitably led to a formalism equivalent to the usual formulation of quantum mechanics. It makes us wonder whether it is at all possible to construct a sensible alternative theory that is equally successful in accounting for microscopic phenomena.

Methods based on path integrals have been found to be very powerful in other branches of modern physics, such as quantum field theory and statistical mechanics. In this book the path-integral method will appear again when we discuss the Aharonov–Bohm effect. ¹²

## 2.7 Potentials and Gauge Transformations

2.7.1 Constant Potentials

In classical mechanics it is well known that the zero point of the potential energy is of no physical significance. The time development of dynamic variables such as x(t) and L(t) is independent of whether we use V(x) or V(x) + V₀ with V₀ constant in both space and time. The force that appears in Newton’s second law depends only on the gradient of the potential; an additive constant is clearly irrelevant. What is the analogous situation in quantum mechanics?

We look at the time evolution of a Schrödinger picture state ket subject to some potential. Let |α, t₀; t⟩ be a state ket in the presence of V(x), and |α, t₀; t⟩̃ the corresponding state ket appropriate for Ṽ(x) = V(x) + V₀. (2.321)

To be precise, let us agree that the initial conditions are such that both kets coincide with |α⟩ at t = t₀. If they represent the same physical situation, this can always be done by a suitable choice of the phase. Recalling that the state ket at t can be obtained by applying the time-evolution operator U(t, t₀) to the state ket at t₀, we obtain

|α, t₀; t⟩ = exp[−i(p²/(2m) + V(x) + V₀)(t − t₀)/ℏ] |α⟩ = exp[−iV₀(t − t₀)/ℏ] |α, t₀; t⟩. (2.322)

In other words, the ket computed under the influence of Ṽ has a time dependence different only by a phase factor exp[−iV₀(t − t₀)/ℏ]. For stationary states, this means that if the time dependence computed with V(x) is exp[−iE(t − t₀)/ℏ], then the corresponding time dependence computed with V(x) + V₀ is exp[−i(E + V₀)(t − t₀)/ℏ]. In other words, the use of Ṽ in place of V just amounts to the following change: E → E + V₀, (2.323)

which the reader probably guessed immediately. Observable effects such as the time evolution of expectation values of ⟨x⟩ and ⟨S⟩ always depend on energy differences [see (2.47)]; the Bohr frequencies that characterize the sinusoidal time dependence of expectation values are the same whether we use V(x) or V(x) + V₀. In general, there can be no difference in the expectation values of observables if every state ket in the world is multiplied by a common factor exp[−iV₀(t − t₀)/ℏ].

Trivial as it may seem, we see here the first example of a class of transformations known as gauge transformations. The change in our convention for the zero-point energy of the potential V(x) → V(x) + V₀ (2.324)

must be accompanied by a change in the state ket |α, t₀; t⟩ → exp[−iV₀(t − t₀)/ℏ] |α, t₀; t⟩. (2.325)

Of course, this change implies the following change in the wave function: ψ(x⃗ , t) → exp[−iV₀(t − t₀)/ℏ] ψ(x⃗ , t). (2.326)

Next we consider V that is spatially uniform but dependent on time. We then easily see that the analogue of (2.325) is |α, t₀; t⟩ → exp[−i/ℏ ∫_{t₀}^{t} V₀(t′) dt′] |α, t₀; t⟩. (2.327)

Physically, the use of V(x) + V₀(t) in place of V(x) simply means that we are choosing a new zero point of the energy scale at each instant of time.

Even though the choice of the absolute scale of the potential is arbitrary, potential differences are of nontrivial physical significance and, in fact, can be detected in a very striking way. To illustrate this point, let us consider the arrangement shown in Figure 2.8. A beam of charged particles is split into two parts, each of which enters a metallic cage. If we so desire, we can maintain a finite potential difference between the two cages by turning on a switch, as shown. A particle in the beam can be visualized as a wave packet whose dimension is much smaller than the dimension of the cage. Suppose we switch on the potential difference only after the wave packets enter the cages and switch it off before the wave packets leave the cages. The particle in the cage experiences no force because inside the cage the potential is spatially uniform; hence no electric field is present. Now let us recombine the two beam components in such a way that they meet in the interference region of Figure 2.8. Because of the existence of the potential, each beam component suffers a phase change, as indicated by (2.327). As a result, there is an observable interference term in the beam intensity in the interference region, namely, cos(φ₁ − φ₂), sin(φ₁ − φ₂), (2.328)

where φ₁ − φ₂ = (1/ℏ) ∫_{ti}^{tf} dt [V₂(t) − V₁(t)]. (2.329)

So despite the fact that the particle experiences no force, there is an observable effect that depends on whether V₂(t) − V₁(t) has been applied. Notice that this effect is purely quantum mechanical; in the limit ℏ → 0, the interesting interference effect is washed out because the oscillation of the cosine becomes infinitely rapid. ¹³

2.7.2 Gravity in Quantum Mechanics

There is an experiment that exhibits in a striking manner how a gravitational effect appears in quantum mechanics. Before describing it, we first comment on the role of gravity in both classical and quantum mechanics.

Consider the classical equation of motion for a purely falling body: mẍ = −m∇Φ_grav = −mgẑ. (2.330)

The mass term drops out; so in the absence of air resistance, a feather and a stone would behave in the same way – à la Galileo – under the influence of gravity. This is, of course, a direct consequence of the equality of the gravitational and the inertial masses. Because the mass does not appear in the equation of a particle trajectory, gravity in classical mechanics is often said to be a purely geometric theory.

The situation is rather different in quantum mechanics. In the wave-mechanical formulation, the analogue of (2.330) is [−(ℏ²/(2m))∇² + mΦ_grav] ψ = iℏ ∂ψ/∂t. (2.331)

The mass no longer cancels; instead it appears in the combination ℏ/m, so in a problem where ℏ appears, m is also expected to appear. We can see this point also using the Feynman path-integral formulation of a falling body based on

⟨xₙ, tₙ | xₙ₋₁, tₙ₋₁⟩ = (m/(2πiℏΔt)) exp{ i/ℏ ∫ dt (mẋ²/2 − mgz) }, (tₙ − tₙ₋₁ = Δt → 0). (2.332)

Here again we see that m appears in the combination m/ℏ. This is in sharp contrast with Hamilton’s classical approach, based on ∫_{t₁}^{t₂} dt (mẋ²/2 − mgz) = 0, (2.333)

where m can be eliminated in the very beginning.

Starting with the Schrödinger equation (2.331), we may derive the Ehrenfest theorem d²⟨x⟩/dt² = −gẑ. (2.334)

However, ℏ does not appear here, nor does m. To see a nontrivial quantum-mechanical effect of gravity, we must study effects in which ℏ appears explicitly – and consequently where we expect the mass to appear – in contrast with purely gravitational phenomena in classical mechanics.

Until 1975, there had been no direct experiment that established the presence of the mΦ_grav term in (2.331). To be sure, a free fall of an elementary particle had been observed, but the classical equation of motion, or the Ehrenfest theorem (2.334), where ℏ does not appear, sufficed to account for this. The famous “weight of photon” experiment of V. Pound and collaborators did not test gravity in the quantum domain either because they measured a frequency shift where ℏ does not explicitly appear.

On the microscopic scale, gravitational forces are too weak to be readily observable. To appreciate the difficulty involved in seeing gravity in bound-state problems, let us consider the ground state of an electron and a neutron bound by gravitational forces. This is the gravitational analogue of the hydrogen atom, where an electron and a proton are bound by Coulomb forces. At the same distance, the gravitational force between the electron and the neutron is weaker than the Coulomb force between the electron and the proton by a factor of ~2 × 10³⁹. The Bohr radius involved here can be obtained simply: a₀ = ℏ²/(e²m_e) → ℏ²/(G m²_e m_n), (2.335)

where G is Newton’s gravitational constant. If we substitute numbers in the equation, the Bohr radius of this gravitationally bound system turns out to be ~10³¹, or ~10¹³ light years, which is larger than the estimated radius of the universe by a few orders of magnitude!

We now discuss a remarkable phenomenon known as gravity-induced quantum interference. An early monoenergetic beam of particles, in practice, thermal neutrons, is split into two parts and then brought together as shown in Figure 2.9. In actual experiments the neutron beam is split and bent by silicon crystals, but the details of this beautiful art of neutron interferometry do not concern us here. Because the size of the wave packet can be assumed to be much smaller than the macroscopic dimension of the loop formed by the two alternate paths, we can apply the concept of a classical trajectory. Let us first suppose that path A→B→D and path A→C→D lie in a horizontal

¹¹ The reader is challenged to solve the simple harmonic oscillator problem using the Feynman path-integral method in Problem 2.44 of this chapter.

¹² The reader who is interested in the fundamentals and applications of path integrals may consult Feynman and Hibbs (1965) and also Zee (2010).

¹³ This gedanken experiment is the Minkowski-rotated form of the Aharonov–Bohm experiment to be discussed later in this section.

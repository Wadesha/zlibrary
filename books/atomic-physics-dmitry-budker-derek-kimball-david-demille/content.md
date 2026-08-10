# Atomic Physics Dmitry Budker Derek Kimball David DeMille Z Library

ATOMIC PHYSICS An Exploration through Problems and Solutions

ATOMIC PHYSICS An Exploration through Problems and Solutions Second Edition Dmitry Budker Department of Physics, University of California, Berkeley, USA Derek F. Kimball Department of Physics, California State University, East Bay, USA David P. DeMille Department of Physics, Yale University, New Haven, USA OXFORD UNIVERSITY PRESS

OXFORD UNIVERSITY PRESS Great Clarendon Street, Oxford OX2 6DP Oxford University Press is a department of the University of Oxford.

Reprinted with corrections 201 O stored in a retrieval system, or transmitted, in any form or by any means.

without the prior permission in writing of Oxford University Press.

or as expressly permitted by law, or under terms agreed with the appropriate reprographics rights organization. Enquiries concerning reproduction outside the scope of the above should be sent to the Rights Department.

To our teachers

ACKNOWLEDGMENTS This book would not have been possible without our mentors, colleagues, and students whose ideas inspired many of the problems and solutions found in this book. Their suggestions, guidance, and readings of countless drafts have been invaluable.

In particular, we would like to acknowledge the inspiration from and con- tributions of Victor Acosta, Evgeniy B. Alexandrov, Marcis Auzinsh, Lev M.

Barkov, Ilya Bezel, Sarah Bickman, Chris J. Bowers, G. A. Brooker, Sid B.

Cahn, Arman Cingoz, Eugene D. Commins, Andrew Dawes, Damon English, Victor Flambaum, Daniel Gauthier, Wojciech Gawlik, Jennie Guzman, Erwin Hahn, Theodor W. Hansch, Robert A. Harris, Chris Hovde, Larry Hunter, J. D.

Jackson, losif B. Khriplovich, Gleb L. Kotkin, Mikhail G. Kozlov, Vitaliy V.

Kresin, Chih-Hao Li, Yongmin Liu, Steve K. Lamoreaux, Alain Lapierre, Jon M. Leinaas, Robert Littlejohn, Richard Marrus, Jeff Moffitt, Hitoshi Murayama, Frank A. Narducci, Anh-Tuan D. Nguyen, A. I. Okunevich, J. B. Pendry, Simon M. Rochester, Michael V. Romalis, Yaniv Rosen, Neil Schafer-Ray, Gennady Shvets, Jason E. Stalnaker, Herbert Steiner, Mark Strovink, Alexander 0. Sushkov, Oleg P. Sushkov, Falguni Suthar, Mahiko Suzuki, Jeff T. Urban, Arkady I. Vain- shtein, Louis A. Villanueva, Ronald Walsworth, David S. Weiss, Eric Williams, Valeriy V. Yashchuk, Jun Ye, Jerzy Zachorowski, Vladimir G. Zelevinsky, and Max Zolotorev.

We would like to extend a special thanks to Damon English for providing the cover illustration.

The authors also acknowledge the support of their research, that motivated many of the problems in this book, by the National Science Foundation, the Office of Naval Research, and the Miller Institute for Basic Research in Science.

CONTENTS Pref ace to the Second Edition Pref ace to the First Edition XVII Notation XIX Atomic structure 1 .1 Ground state of phosphorus 1.2 Exchange interaction 1.3 Spin-orbit interaction 1.4 Hyperfine structure and Zeeman effect in hydrogen 1.5 Hydrogenic ions 1.6 Geonium 1.7 The Thomas-Fermi model (T)

1.8 Electrons in a shell 1.9 Isotope shifts and the King plot

## 1.10 Crude model of a negative ion

## 1.11 Hyperfine-interaction-induced mixing of states of different J

I .12 Electron density inside the nucleus (T)

## 1.13 Parity nonconservation in atoms

## 1.14 Parity nonconservation in anti-atoms

## 1.15 The anapole moment (T)

Atoms in external fields 2.1 Electric polarizability of the hydrogen ground state 2.2 Polarizabilities for highly excited atomic states 2.3 Using Stark shifts to measure electric fields 2.4 Larmor precession frequencies for alkali atoms 2.5 Magnetic field inside a magnetized sphere 2.6 Classical model of magnetic resonance 2.7 Energy level shifts due to oscillating fields (T)

2.8 Spin relaxation due to magnetic field inhomogeneity I 02 2.9 The E x v effect in vapor cells

## 2.10 Field ionization of hydrogenic ions

## 2.11 Electric-field shifts of magnetically split Zeeman sublevels

X CONTENTS

## 2.12 Geometric (Berry's) phase

## 2.13 Nuclear dipole-dipole relaxation

## 2.14 Magnetic spin precession of a free magnet

Interaction of atoms with light 3.1 Two-level system under periodic perturbation (T)

3.2 Quantization of the electromagnetic field (T)

3.3 Emission of light by atoms (T)

3.4 Absorption of light by atoms 3 .5 Resonant absorption cross-section 14 7 3.6 Absorption cross-section for a Doppler-broadened line 3.7 Saturation parameters (T)

3.8 Angular distribution and polarization of atomic fluorescence 3.9 Change in absorption due to optical pumping 3 .10 Optical pumping and the density matrix

## 3.11 Cascade decay

3 .12 Coherent laser excitation 17 5

## 3.13 Transit-time broadening

## 3.14 A quiz on fluorescence and light scattering

3 .15 Two-photon transition probability

## 3.16 Vanishing Raman scattering

## 3.17 Excitation of atoms by off-resonant laser pulses

## 3.18 Hyperfine-interaction-induced magnetic dipole (Ml) transi-

tions

## 3.19 Transitions with unresolved hyperfine structure

## 3.20 Optical pumping and quantum beats in Mercury

## 3.21 Thomson scattering

## 3.22 Classical mcxlel for a magnetic-dipole transition

## 3.23 Nonlinear three-wave mixing in isotropic chiral media

## 3.24 A negatively refracting atomic vapor?

## 3.25 Light propagation in anisotropic crystals

## 3.26 Electromagnetically induced transparency (EIT)

Interaction of light with atoms in external fields 4.1 Resonant Faraday rotation 4.2 Kerr effect in an atomic medium 4.3 The Hanle effect 4.4 Electric-field-induced decay of the hydrogen 2 2 S 1; 2 state 4.5 Stark-induced transitions (T)

4.6 Magnetic deflection of light 4.7 Classical model of an optical-pumping magnetometer

4.8 4.9 4.10 4.11 CONTENTS Searches for permanent electric dipole moments (T)

Sensitivity to electric dipole moments Absorption, dispersion, optical rotation, and induced elliptic- ity Optical rotation in a gas of polarized neutrons Atomic collisions 5.1 Collisions in a buffer gas 5.2 Spectral line broadening due to phase diffusion 5.3 Dicke narrowing 5.4 Basic concepts in spin exchange 5.5 The spin-temperature limit 5.6 Electron-randomization collisions 5.7 Larmor precession under conditions of rapid spin exchange 5.8 Penning ionization of metastable helium atoms Cold atoms 6.1 Laser cooling: basic ideas (T)

6.2 Magneto-optical traps 6.3 Zeeman slower 6.4 Bose-Einstein condensation (T)

6.5 Bose-Einstein condensation from an optical lattice 6.6 Cavity cooling 6.7 Cavity cooling for many particles: stochastic cooling 6.8 Fermi energy for a hannonic trap Molecules 7 .1 Amplitude of molecular vibrations 7 .2 Vibrational constants for the Morse potential 7 .3 Centrifugal distortion 7.4 Relative densities of atoms and molecules in a vapor 7 .5 Isotope shifts in molecular transitions 7 .6 Electric dipole moments of polar molecules 7 .7 Scalar coupling of nuclear spins in molecules 7 .8 Zeeman effect in diatomic molecules 7 .9 Omega-type doubling Experimental methods 8.1 Reflection of light from a moving mirror 8.2 Laser heating of a small particle

CONTENTS 8.3 Spectrum of frequency-modulated light 8.4 Frequency doubling of modulated light 8.5 Ring-down of a detuned cavity 8.6 Transmission through a light guide 8.7 Quantum fluctuations in light fields 8.8 Noise of a beamsplitter 8.9 Photon shot noise in polarimetry

## 8.10 Light-polarization control with a variable retarder

## 8.11 Pile-up in photon counting

## 8.12 Photons per mode in a laser beam

## 8.13 Tuning dye lasers

## 8.14 Matter-wave vs. optical Sagnac gyroscopes

## 8.15 Femtosecond laser pulses and frequency combs

## 8.16 Magnetic field fluctuations due to random thermal currents

## 8.17 Photodiodes and circuits (T)

Miscellaneous topics 9.1 Precession of a compass needle?

9.2 Ultracold neutron polarizer 9.3 Exponentially growing/decaying harmonic field 9.4 The magic angle 9.5 Understanding a Clebsch-Gordan coefficient selection rule 9.6 The Kapitsa pendulum 9.7 Visualization of atomic polarization 9.8 Estimate of elasticity and tensile strength of materials 9.9 The Casimir force A Units, conversion factors, and typical values B Reference data for hydrogen and alkali atoms C Spectroscopic notation for atoms and diatomic molecules D Description of polarization states of light D.I The Stokes parameters D.2 The Jones calculus E Euler angles and rotation matrices

CONTENTS F The Wigner-Eckart theorem and irreducible tensors F. I Wigner-Eckart theorem F.2 Irreducible tensors G The density matrix G. I Connection between the density matrix and the wavefunction G.2 Ensemble-averaged density matrix G.3 Time evolution of the density matrix: the Liouville equation G.4 Atomic polarization moments H Elements of the Feynman diagram technique I The 3-J and 6-J symbols I. I 3-J symbols 1.2 6-J symbols Bibliography Index

PREFACE TO THE SECOND EDITION The first edition of Atomic Physics: an exploration through problems and solu- tions appeared in 2003. We are truly delighted with the enthusiasm the book has been met with by students and colleagues, some of whom use the book as a supplementary resource for their classes, as well as a research reference.

For a while after the book appeared, we were pleasantly surprised with the relatively small number of errors and misprints found in the text. As time went on, however, a number of issues have been uncovered, ranging from benign misprints to, we are sorry to say, a few significant conceptual errors. We found some of these problems by ourselves (yes, we are among the ones who use the book as a research and teaching reference); others were found by our readers from near and far who were kind enough to e-mail us their criticisms. We are deeply indebted to everyone who has contributed.

The second edition, presently offered to the reader, has been prepared by two of the three authors of the original Atomic Physics, for which "error correction"

is one, but not the only motivation. New teaching and research experiences have stimulated us to come up with significant amount (over 70 pages) of new material: about twenty additional problems in various chapters, and a new Appendix. All the new material has been placed at the end of appropriate chapters, so the numbering of problems and appendices is compatible with the first edition.

PREFACE TO THE FIRST EDITION We have found that usually the best way to learn something new is to ask concrete questions and try to work out the answers. Often some of the simplest questions have surprising and unexpected answers, and some seemingly complex problems can be solved in a simple way. In this book we have collected some of these prob- lems and our solutions to them. The book encompasses many issues we faced as we ourselves made the transition from undergraduate students to practicing exper- imental atomic physicists and instructors. However, the text is not intended to be comprehensive, but rather addresses various aspects of atomic physics which we have found interesting and important.

In the course of doing atomic physics, we always find ourselves crossing boundaries into other subfields; the selection of problems reflects this gray area.

It also reflects our specific interests, with several problems about symmetry viola- tion, etc. that would not appear in more "standard" textbooks. It is our philosophy that working on specific problems usually helps with understanding of more gen- eral issues, and indeed may be the most useful way to really learn anything. It is our hope that some selection of the broad range of problems given here will pique the interest of any reader, and thus initiate this process.

Where possible, we try to emphasize approximation methods, dimensional considerations, limiting cases, and symmetry arguments as opposed to fonnal mathematics. We often appeal to pictures, tables, and graphs. This problem- solving approach is aimed at developing intuition about physical principles and fosters the important ability to perfonn "back-of-the-envelope" calculations. These are the tools we find most useful when trying to solve the types of problems we commonly encounter in the laboratory. Of course, on occasion a formal mathemat- ical approach (as painful as it could be) can lead to important insights. Generally, in order to deeply understand various aspects of physics, it is good to have both an intuitive picture as well as the appropriate mathematical tools.

This book is intended for advanced undergraduates and beginning graduate students interested in atomic, molecular and optical physics, and we assume that readers possess basic knowledge of quantum mechanics [at the level of Griffiths ( 1995), Bransden and Joachain ( 1989), or similar texts], electrodynamics [ at the level of Griffiths ( 1999), Purcell ( 1985), or similar texts], and thennodynamics [at the level of Reif ( 1965), Kittel and Kroemer ( 1980), or similar texts]. However, we hope that many of the problems will also be of interest to professional scientists.

xviii PREFACE TO THE FIRST EDITION In physics, there continues to be a raging debate over what is the best system of units to use and whether or not units should be standardized. We feel that the choice of units is a personal one, especially since converting between different systems is relatively straightforward. That said, in this book we have a tendency to use CGS units, since we find them most convenient (especially in problems involving electromagnetism).

We also set Ii = 1 when it is convenient to do so and measure energies in frequency units, as is common practice in atomic physics (since energy measurements are typically performed by measuring frequencies).

Each problem in the book is intended to stand on its own. If there is a particular subject in atomic physics that one is interested in learning about, there may be a problem about it in this book. We envision the reader turning right to that page and starting to try to figure it out. Hopefully, at the end of this exercise, one will have gained some familiarity with the topic, enabling her or him to understand more advanced, specialized literature on the subject, or go straight to the lab and get to work!

In the introduction to most problems there is a brief discussion of the relevance of the topic to modem atomic physics with references to research literature on the subject. The cited references are not intended to be comprehensive, but merely provide a starting point in a search for more information about the subject of the problem. We apologize in advance to the innumerable scientists whose important contributions are not mentioned. Also, for a few problems, especially in subfields of atomic physics dear to our hearts, there are some historical remarks. Of course, there is a great deal of history surrounding almost all of the topics covered in this book, and we could not tell all of it. Nonetheless, we thought a few, not widely known stories might be enjoyable.

Some of the problems are written as tutorials on various subjects in atomic physics [they are marked with a (T)]. In such problems, there are a series of short questions that are intended to guide the reader through some important mate- rial. Hopefully the reader will find this more entertaining and interactive than just reading the explanation straight through.

We hope you enjoy reading and using the book as much as we have enjoyed writing it!

Berkeley, Calif omia May 2003 D.B.

D. F. K.

D. P. D.

NOTATION The following is a table of symbols commonly used throughout the book, their meaning, and their value where appropriate.

Symbol Meaning Value m, me electron mass

## 9.1094 X 10- 28 g

0.5111\foV /c 2 mp proton mass

## 1.6726 X 10- 24 g

## 938.27 MeV /c

mn neutron mass

## 1.6750 X 10- 24 g

## 939.57 MeV /c

fin -mp difference between nucleon masses

## 1.293 MeV /c

e electron charge magnitude

## 4.8032 x 10- 10 esu

h Planck's constant

## 6.6261 x 10- 27 erg · s

Ii = h/(21r)

## 1.0546 x 10- 27 erg· s

C speed of I ight

## 2.99792458 x 1010 cm/s

o: = e2 /(lie)

fine structure constant 1/137.036 ao = 1i2 /(me 2 )

Bohr radius

## 5.292 x 10- 9

µo = e1i/(2mc)

Bohr magneton

## 0.93 x 10- 20 erg/G

## 1.40 MHz/G

## 5.79 x 10- 9 eV /G

µN = e1i/(2m,,c)

nuclear magneton

## 5.05 x 10- 24 erg/G

762 Hz/G Rx = me 4 /(41r1i3c)

Rydberg constant 109,737 cm- 1

## 3.2898 x 1015 Hz

kB Boltzmann's constant

## 1.38066 x 10- 16 erg/K

## 8.61735 x 10- 5 eV /K

L, l orbital angular momentum units of Ii S,s electron spin units of Ii J,j total electronic angular momentum units of Ii I nuclear spin units of Ii F total atomic angular momentum units of Ii

NOTATION In most locations, we remind the reader of the meaning of the symbols when they appear. Also see Appendix A for practical units, conversion factors, and typical values of various parameters.

When we deal with spin-1/2 systems, we will commonly employ the notation I+) and I-) to denote the spin up ( m = + 1 /2) and spin down ( m = -1 /2) states, respectively. Here m is the projection of the spin along the quantization axis in units of h.

The ubiquitous Clebsch-Gordan coefficients 1 describe the connection between the coupled basis IJ, M) and the uncoupled basis IJ1, M 1)IJ2, M2) (where J, J1, J2 are angular momenta and M, M 1, M2 are the projections of the respective angular momenta on the quantization axis): IJ,M) = L C(J1,hJ;M1,M2,.M)IJ1,M1)lhM2)

M1,~h IJ1, M1)lh M2) = L C(Ji, h J; Mi, M2, M)IJ, M).

J,M In the text we consistently use the notation: C(J1, J2, J; M1, M2, M) = (J1, M1, J2, M2IJ, M) , and employ the commonly used phase convention of Condon and Shortley ( 1970), Edmonds ( 1996), and Sobelman ( 1992).

1 The Clebsch-Gordan coefficients are also referred to as vector-coupling coefficients, vector- addition coefficients, and Wigner coefficients in the literature.

ATOMIC STRUCTURE

## 1.1 Ground state of phosphorus

One of the most important topics in atomic physics is the description of atomic energy levels. The study of atomic structure continues to be an exciting field, with increasingly precise measurements and improved calculational tools allowing ever more detailed comparisons between experiment and theory.

The first few problems in this chapter deal with some of the basic features of atomic energy levels in multi-electron atoms. In the simplest atom, hydrogen, most of the splitting between energy levels comes from the difference between the principal quantum numbers n for different states - the energy En of an electron in the hydrogen atom is given, approximately, by the famous Bohr fonnula, me 4 1 En~---- 2!i2 n2 ' (I.I)

where m is the mass of the electron and e is the absolute value of its charge.

As a first approximation, in more complex atoms we can consider the states of individual electrons as if they were moving in an effective centrally symmetric field created by the nucleus and the other electrons (the central field approxima- tion). In this case we can assign a principal quantum number n and an orbital angular momentum l to each electron (the distribution of the electrons among the states with various n's and l's is known as the electron configuration), and, as in hydrogen, the differences between the principal quantum numbers for differ- ent configurations are an important source of energy level splittings. In contrast to hydrogen, however, the energy of a particular configuration for a multi-electron atom is also dependent on l. This is because electrons with larger l values are, on average, further from the nucleus due to the centrifugal barrier, and the other elec- trons screen the nuclear charge. Based on these two general ideas, one expects that configurations for which electrons have the lowest possible values of n and l have the lowest energies. For s and p orbitals, it is most important to have the smallest value of n ("regular" configurations). However, one finds that in some cases, for

ATOMIC STRUCTURE d and / orbitals it can be energetically favorable for electrons to have higher n so that they can occupy states with lower l ("irregular" configurations 1 ).

Next one must consider in more detail the mutual electrostatic repulsion between the electrons. Already, the central field approximation has accounted for the spherically symmetric part of the potential due to the electron-electron interaction which is responsible for the screening of the nucleus. There is also a nonspherically symmetric part of the electron-electron potential related to the fact that it is energetically favorable for electrons to be as far apart as possible.

For a given configuration, the atomic states can be specified by the total orbital angular momentum l = L ~ and the total spin S = E Bi (this characteriza- tion of atomic states, valid for low to intermediate Z atoms, is known as the Russell-Saunders or L-S coupling scheme 2). Since the average separation between electrons are different for states with different L and S, these states are split in energy (see Problem 1.2). The states of a given configuration identified with particular L and S are known as the term.

There are empirical rules, known as Hund's rules [see, for example, Brans- den and Joachain (2003), Landau and Lifshitz (1977), or Herzberg (1944)], for determining which term has the lowest energy for a given configuration (in the Russell-Saunders coupling scheme). Hund's rules state that for the ground term with the lowest energy • the term with the largest S has the lowest energy, and • for a given S, the larger the total orbital angular momentum L the lower the energy (as long as there is only a single unfilled shell).

These rules ensure that the ground state electrons are, on average, as far apart as possible, which minimizes the electrostatic repulsion between them.

For both single and multi-electron atoms, there is also the spin-orbit interaction (see Problem 1.3) which causes splitting of states with different values of the total electronic angular momentum J (spin S coupled to orbital L). Since this splitting is typically considerably smaller than the energy differences from the previously discussed mechanisms, it is known as the fine-structure splitting.

1 An examr,le of such an irre§ular confi§uration is the ground state of potassium, which is ls 22s22p63s 3p64s instead of ls 2s 22p63s 3p63d.

2 In atoms with large Z, the spin-orbit energy (arising from relativistic effects) can become more imponant than the residual, nonspherical electrostatic interaction between the electrons. In such a case, it is useful to specify individual electron states by their total angular momentum J = f + i.

This is known as the j-j coupling scheme. In each coupling scheme, we are trying to begin our considerations with what are nearly the energy eigenfunctions for the atom, but in the general case neither L-S nor j-j coupling give the correct energy eigenfunctions.

GROUND STATE OF PHOSPHORUS Typically, the L, S, and J for a particular state are designated in spectroscopic notation (see, for example, Appendix C): 2S+lL J· ( 1.2)

In this problem, we consider all of the aforementioned interactions in order to detennine the energy level structure for the terms corresponding to the ground state configuration of phosphorus (P).

(a) What is the ground state configuration of P, Z = 15?

(b) What is the ground tenn and J value for P according to Hund's rules?

(c) What other terms are possible for the ground state configuration?

(d) For the term with the highest energy corresponding to the ground state config- uration, identified in part (c), can one say what value of J has the highest energy using first-order perturbation theory?

Hints In part (b ), we can make use of the fact that electrons in the filled subshells (ls, 2s, 2p, 3s) have total spin and total orbital angular momentum equal to zero, and so we need only consider the three outer electrons in the 3p orbital to determine the ground tenn.

For the ground term, first consider the maximum spin and maximum projection of the spin along the quantization axis for three electrons (according to Hund's first rule, this should be S for the ground term). What must be the orbital wavefunction in this case?

Part (d) is tricky! One can think of a subshell (which can hold a total of 2(2l + 1)

electrons) containing N electrons as consisting of N electrons or 2(2l + 1) - N holes. The spin-orbit splitting (to first order) has opposite sign for electrons and holes.

Solution (a) Phosphorus has sufficiently low Z that each shell fills regularly (there are no d or / states involved). A subshell can contain 2(2l + 1) electrons, where l is the orbital angular momentum quantum number for the individual electrons.

ATOMIC STRUCTURE Therefore, the ground state configuration is ( 1.3)

(b) The maximum total spin that three electrons can possess is S = 3/2. The S = 3/2 spin wavefunctions are symmetric under particle interchange. This can be seen from the fact that the stretched state IS, Als = S) is obviously symmetric ( 1.4)

and all the other S = 3/2 states can be obtained by application of the lowering operators_ = S 1_ + S2_ + S3_, which is symmetric and so cannot change the exchange symmetry of the spin states.

To satisfy the spin-statistics theorem, 3 we must choose a spatial wavefunction which is totally antisymmetric with respect to particle interchange. With three p electrons, we have l1 = 1, l2 = 1, and l3 = 1, in principle allowing L = 3, 2, 1 and 0, where Lis the total angular momentum of all three valence electrons.

However, in order to construct a totally antisymmetric wavefunction, one needs at least as many states as there are particles. This can be seen by considering the Slater determinant [see, for example, Bransden and Joachain (2003)), which provides a simple method for finding a totally antisymmetric wavef unction for a system of particles. In this case we have three particles in, let us say, states o, /3, and , . Then the totally antisymmetric wavefunction is given by: \JI - AS - v'fil o(l)

o:(2)

o(3)

/3(1)

/3(2)

/3(3)

,(1)

,(2)

,(3)

(l.5)

This wavefunction is clearly exchange antisymmetric, since interchanging two par- ticles is equivalent to interchanging two rows of the matrix, which changes the sign of the determinant. Furthermore, the determinant vanishes if two columns are the same, which occurs if any two of the states o, {3, or 1 are the same. Thus the Pauli exclusion principle is seen to be a consequence of the fact that electrons must be in exchange antisymmetric states.

Therefore, for S = 3/2, the allowed spatial wavefunction l·l/Jspace)

must involve a superposition of electrons in the m 1 = 1, m 1 = 0, and m 1 = -1 states (denoted 3 There is an important distinction between the symmetrization postulate and the spin-statistics theorem. The symmetrization postulate states that any wavefunction for a system of identical pani- cles must be either exchange symmetric or exchange antisymmetric (i.e., the wavefunction must be an eigenstate of the permutation operator). The spin-statistics theorem states that integer spin pani- cles (bosons) must be in an exchange symmetric state and half-integer spin particles (fermions) are in exchange antisymmetric states.

GROUND STATE OF PHOSPHORUS ,'---m' ! 1 ms',.!

+1/2 -1/2 • I • • I I FIG. 1.1 A simple way to figure out the ground state term according to Hund's rules for the case of phosphorus.

II), IO), l-1)), namely [using (1.5)], l'l/-'space)

= ~ [ll)alO)bl-l)c + I0)0 l-l)bll)c + 1-l)allhlO)c (1.6)

- 1-l)alO)bll)c -11) 0 1-l)blO)c - IO)all)bl-l)c] ' so that the total projection of the orbital angular momentum along the z-axis is ML = 0. Thus the only possible value for the orbital angular momentum is L = 0.

Here is another simple, graphical way to arrive at this conclusion. Consider the chart shown in Fig. 1.1. Each box corresponds to an individual electron state with unique quantum numbers. We want to think about the stretched state with maxi- mum S. The Pauli exclusion principle demands that we can only put one electron in each box (since otherwise we could not form an exchange antisymmetric state).

We put all electrons in m 8 = 1/2 boxes to maximize Ms (and hence S). Then the maximum projection of ML consistent with Ms = 3/2 is zero. This tells us that L = 0 for the ground state of phosphorus.

The final step is to figure out what J should be. Luckily, there is only one choice in this case, J = 3/2. Consequently, the ground state for phosphorus is ~ (1.7)

(c) As we have seen in part (b), 4S3; 2 is the only possible term when the electrons have total spin S = 3/2. But three electrons can also have total spin S = 1/2, so there are additional, higher-energy tenns possible for the given configuration.

Unlike the S = 3/2 spin wavefunctions which are exchange symmetric, the S = 1/2 spin wavefunctions possess no definite exchange symmetry, so the approach we used in part (b) in which we first considered the exchange symmetry of the spin wavefunctions and then the exchange symmetry of the orbital wavefunctions fails.

In order to construct totally antisymmetric wavefunctions for the three electrons

ATOMIC STRUCTURE TABLE 1.1 All possible single particle states for the ground state configuration of phosphorus grouped according to Ah and Ms. For completeness, we have written out all the states, but because of the symmetry between the Af L and -AJ L states and the Ms and - Ms states, only one comer of the chart is actually necessary for specifying all the states.

Ms Ah =2 M1., = 1 M 1. = 0 M1, = -1 M1., = -2 +!

(l+)(o+)(-1+)

(1 + )(o+ )( 1-)

(l+)(-1+)(1-)

(-1+)(0+)(1-)

(l+)(-l+)(-1-)

(-1+)(0+)(-1-)

+½ (1 + )(o+ }(o-)

(-1+)(1+)(0-)

( -1 + )(O+ )(0-)

(1 + )(o+ )(-1 - )

(l+)(o- )(1-)

(l+)(-1-)(1-)

(-1+)(0-)(1-)

(-1+)(1-)(-1-)

c -1 + )(o- )( -1 - > -½ co+ H 1 - }(o- > (l+)(-1-)(0-)

(0+)(-1-)(0-)

(0+)(1-)(-1-)

(1-)(0-)(-1-)

-~ for these higher-energy terms, we must consider products of spatial and spin states for each individual electron.

As pointed out in the discussion surrounding Eq. ( 1.5), in order to construct a totally antisymmetric wavefunction, one needs at least as many individual electron states as there are electrons. To determine the additional terms, we can write out all the possible states using the shorthand notation (m?1~)a(mf1 8 )b(m?1~)c, which actually refers to the completely antisymmetric wavefunction built from the three states according to Eq. ( 1.5). To satisfy the Pauli exclusion principle, we require that no two of the states for the three electrons are the same. This notation is equivalent to the chart representation described in part (b) - the chart shown in Fig. I.I corresponds to (1 +)(o+)(-1 +). Now we can make a table of all possible states grouped together by the projection of their total orbital angular momentum ML and the projection of their total spin Ms (Table l . l ).

The states described in Table l. l are eigenstates of the operators Lz and Sz, and by forming appropriate linear combinations one can construct eigenstates of L2, S2, Lz, and Sz. The states corresponding to a given term are eigenstates of the operators { L2, S2 , J 2, Jz}. Since both sets of eigenstates form a complete basis for our system, we know that there must be the same number of eigenstates in each set. To figure out the additional terms possible for the ground state configuration, we begin with a stretched state (ML = Land Ms = S) for a particular term, and count off how many states are in that term. We continue this process until we account for all 20 states in Table 1.1.

Let us begin with the term we already know about, 4 S. There are four states in this term (since J = 3/2), all with ML = 0, so that accounts for four states in the

EXCHANGE INTERACTION ML = 0 column of our table. Next, we see that there is one state [ ( 1 +) ( o+) ( 1 - ) ]

with ML = 2 and Ms = 1/2. This is the stretched state of a 2 D term. The possible values of the total electronic angular momentum for the 2 D term are J = 5/2 and J = 3 /2, so the 2 D term accounts for IO states (six with J = 5 /2 and four with J = 3/2), two in each ML column, one corresponding to Ms = 1/2 and the other with Ms = -1 /2 (since S = 1 /2 for the 2 D term).

There is another state with ML = l and Ms = 1/2 not accounted for by the 4 S or 2 D terms. This is the stretched state (the state with the maximum possi- ble projection of all angular momenta along the quantization axis) for a 2 P term, which accounts for the six remaining states (for the 2 P term we have J = 3/2 and J = l /2). This covers all the terms: 14s, 2 D, and 2 p - I ( 1.8)

(d) As mentioned in the hint, to first order the spin-orbit interaction has opposite sign for electrons and holes. Since the p3 configuration can be thought of as con- sisting of three holes or three electrons, we have that the energy splitting due to the spin-orbit interaction ~ELs satisfies ( 1.9)

so (1.10)

To first order, the 2 P 1; 2 and the 2 P 3; 2 states have the same energy.

## 1.2 Exchange interaction

In the nonrelativistic limit, the Hamiltonian describing the interaction of electrons with the nucleus is independent of the electron and nuclear spins. Nonetheless, as we have seen in Problem 1.1, energy levels in multi-electron atoms do depend on the spin state of the electrons. Consider a two-electron atom. The nonrelativistic Hamiltonian H is given by: ( I. 11)

where ( li2 ze2)

Ho = - L -V;.

+ - i=l 2me ' Ti ( 1.12)

and ATOMIC STRUCTURE e2 H1=1- -1· r1 - r2 (1.13)

Here Ho contains the Coulomb attraction of the electrons to the nucleus and H1 describes the Coulomb repulsion between the electrons, where Ti is the position of the i-th electron, and lr1 - r2 I is the distance between the electrons.

The overall electron wavefunction \JI is the product of a spatial wavefunction ·l/J and a spin function X· Fermi statistics demands that \JI must be antisymmetric with respect to particle interchange for identical particles with half-integer spin.

Thus if x is a triplet state (symmetric), then ,,µ must be antisymmetric; if X is a singlet state (antisymmetric), then 1/J must be symmetric. Thus the electron spin state dictates the symmetry of the spatial part of the wavefunction. It turns out that due to the Coulomb repulsion between the electrons (H 1), symmetric and antisymmetric spatial wavefunctions have different energies - this is called the exchange interaction [see, for example, Griffiths ( 1995) or Landau and Lifshitz (1977)].

(a) For the case where one electron is in the ground state and another electron is in an excited state with quantum numbers (n, l, m,), which spin state, the triplet or singlet, has higher energy?

(b) As a simple illustration of the exchange interaction, consider two electrons in a one-dimensional simple harmonic oscillator (SHO) potential. For the case where one of the electrons is in the ground state and the other is in the first excited state, calculate ((x2 - x1)2) for the triplet and singlet spin states, where x1 and x2 are the positions of the two electrons.

Solution (a) Consider the case where one electron is in the ground state ·l/)100(ri) and another electron is in an excited state "Pnlm, (r2). The symmetric 1/Js and antisym- metric 1Pa spatial wavefunctions are given by: 1/Js = y2[1P1oo{f1) · ·t/Jn1m,(f'2)

+ 1/J1oo(T2)

· 1/Jnlm,(f'1)]

1Pa = J2 [1/J1oo{f1)

· ·t/Jnlm, Vi) - 't/J1oo(f'2)

· ·t/Jnlm, ( 1--:-i)]

• (1.14)

If the electrons are in 1Pa, they can never occupy the same position since if r1 = 'r2 then 1Pa = 0. However, 1/Js # 0 if r1 = r2, so it is possible for the two electrons to be located at the same point. Thus it turns out that, on average, electrons in 'l/Js are closer to one another than electrons in 1Pa• Therefore H 1 causes a state

EXCHANGE INTERACTION with a symmetric spatial wavefunction to have a higher energy than one with an antisymmetric wavefunction, so the spin singlet states (x antisymmetric ---+ ·t/J symmetric) have higher energies than the triplet ones (x symmetric ---+ 't/J anti- symmetric). Based on this reasoning, we can plausibly argue that, in general, terms with higher total spin S have lower energy since they have more "antisymmetrical"

spatial wavefunctions, leading to less spatial overlap of the electron wavefunctions.

(b) We can illustrate this principle more explicitly by considering the expectation value ( ( x2 - x 1 )2) for two electrons in a ID simple harmonic oscillator potential.

For the ID SHO we have energy eigenstates In) with energy eigenvalues /iw( n + 1/2). Suppose that one electron is in the ground state IO) and the other electron is in the first excited state 11). For electrons in the triplet spin states, the spatial wavefunction must be exchange antisymmetric ( 1.15)

while for the singlet spin state, the spatial wavefunction must be exchange symmetric ( 1.16)

We can evaluate the expectation value of the distance between the electrons by expressing the position operators in terms of the raising and lowering operators for the two electrons [see, for example, Griffiths (1995)]: where ailn\ = v'n In - 1\ , a11n)i = Jn + 1 In+ l)i .

For the operator describing the distance between the electrons, we find (xi - x2)2 = x~ - 2x1x2 + x~ , where, by using Eq. ( 1.17), we obtain ( 1.17)

( 1.18)

( 1.19)

( 1.20)

( 1.21)

ATOMIC STRUCTURE Using the above relations, it is straightforward to show that while 31i ((x2 - xi) )triplet = - , rnw Ii ({x2 - xi) )singlet = - · rnw (1.22)

( 1.23)

Thus we see that, indeed, electrons in the triplet spin states are, on average, significantly further apart than those in the singlet states.

## 1.3 Spin-orbit interaction

Beyond the electrostatic attraction between the electrons and the nucleus and the electrostatic repulsion between the electrons (Problems 1.1 and 1.2), the next most important cause of energy level splittings in low Z atoms is the relativistic effects, which are responsible for what is known as the fine structure of atomic spectra.

For low-lying states in hydrogen, the fine structure splitting of the energy levels is a factor of rv o:2 smaller than the Bohr energies [Eq. ( 1. 1 )]. There are two causes of this splitting: ( 1) the interaction of the magnetic moment of the electrons with the effective magnetic field the electrons see due to their motion around the nucleus, and (2) relativistic corrections to the kinetic and potential energies of the electrons. In the following problem we consider only the splitting due to the spin-orbit interaction (I), which is the principal cause of fine-structure splitting for heavier atoms.

Consider the term 5 D for a multi-electron atom.

(a) What are the possible values of J?

(b) Show the splitting of the 5 D term due to the spin-orbit interaction on an energy level diagram. Indicate the value of J and the energy for each level in tenns of A, where the spin-orbit interaction is described by the Hamiltonian 4 I ....

....

H = AL · S .

( 1.24)

4 In a multi-electron atom, the .. single electron" spin-orbit coupling (meaning that the interaction between one electron's spin and another's orbital motion is ignored, which is a good approximation for elements located in the middle and end of the periodic system) is given by Assuming that the spin-orbit coupling is small compared to the electrostatic repulsion between the electrons, the Russell-Saunders coupling scheme (see Problem 1.1) is still valid and, to first order, we

SPIN-ORBIT INTERACTION 1 1 Assume A is positive, as is the case for subshells which are less than half-filled.

(c) What effect does the spin-orbit interaction have on the "center of gravity" (the mean perturbation of all the states of the term)?

Hints For part (c), you may find useful the following formulae for summations (which can be proved by induction): ( 1.25)

N L J 2 = !N(N + 1)(2N + 1), J=O ( 1.26)

and N L13 = ~N2(N + 1)2.

J=O ( 1.27)

Solution (a) Here we use the general rule for addition of angular momenta l + S = f: IL - SI < J < L + s ' ( 1.28)

which is known as the triangle inequality. Using ( 1.28), we find that the possible values of J are: I 5 D : S = 2, L = 2 --+ J = 4, 3, 2, 1, 0.

( 1.29)

(b) For the total angular momentum J we have the relation: ( 1.30)

need only calculate the diagonal matrix elements (L, S, J, MJIH'IL, S, J, !v/J). Seeking the overall shift of an atomic state with total orbital angular momentum l and total spin S, we note that the average orbital angular momentum f of an electron in such a state is ex l, and the average spin sis ex § (a consequence of the Wigner-Eckart theorem, see Appendix F), allowing us to write H' as is done in Eq. ( 1.24) [see, for example, Condon and Shortley ( 1970) or Landau and Lifshitz ( 1977)].

ATOMIC STRUCTURE 4A s ----D ----------------------------- '' \ ' -JA -5A -6A 'D 2 'D 1 SD FIG. 1.2 Splitting of the 5 D term due to the spin-orbit interaction H' = Al · S, with A > 0. We set Ii = 1 for convenience.

and therefore, by squaring both sides, we have J 2 = S2 + L 2 + 2£ · S .

Therefore the spin-orbit Hamiltonian ( 1.24) is H' = A (J2 - 52 - L2) .

(1.31)

(1.32)

The states described by the spectral terms 28+1 LJ are eigenstates of J 2, S2, and L2 • Therefore, they are also eigenstates of H' with eigenvalues Ali 2 AE = T[J(J + 1) - S(S + 1) - L(L + 1)].

(1.33)

Using Eq. ( 1.33) and setting h = 1 we can evaluate the energy shifts for states with various J's with S = 2, L = 2: ~E(J = 4) = 4A ~E(J = 3) = 0 ~E(J = 2) = -3A ~E(J = 1) = -5A ~E(J = 0) = -6A.

The energy level structure of this system is shown in Fig. 1.2.

( 1.34)

(1.35)

(1.36)

(1.37)

(1.38)

Note that the energy difference between adjacent components is given by tlE(J) - ~E(J - 1) = AJ.

(1.39)

This formula is known as the Lande interval rule.

HYPERFINE STRUCTURE AND ZEEMAN EFFECT IN HYDR<X,EN (c) The "center of gravity" of a term does not change due to the spin-orbit inter- action. This answer can be guessed, since we expect the average of L · S over all possible orientations of i and § to be zero.

Alternatively, one can use the summation formulae [Eqs. ( l .25)-( l .27)] to eval- uate the shift of the center of gravity. For each J there are (2J + 1) Zeeman sublevels, so that the average energy shift (~E) is given by the sum: A L+S (b,.E) = 2 L (2J + l)[J(J + 1) - S(S + 1) - L(L + 1)] = 0.

(1.40)

J=IL-SI

## 1.4 Hyperfine structure and Zeeman effect in hydrogen

In this classic problem, we are interested in what is known as the hyperfine struc- ture, which in general arises due to the interaction of atomic electrons with the electric and magnetic multipole fields of the nucleus (the most important being the magnetic dipole and electric quadrupole). The transition between the hyperfine levels in the ground state of hydrogen is responsible for the famous 21-cm line in radio astronomy (the wavelength of the radiation is 21 cm), and the splitting between these levels has been measured extremely precisely with the hydrogen maser. The transition between the ground state hyperfine levels of cesium is used for atomic clocks and this transition frequency defines the second.

(a) For the ground state of hydrogen (2S112), calculate the splitting of the F = 1 and F = 0 hyperfine levels (in MHz). What is the form of the Hamiltonian describing the hyperfine interaction?

(b) Consider the effect of a uniform magnetic field B = Bz on the ground state energy levels of hydrogen (the effects of external fields on atoms are considered in more detail in Chapters 2 and 4). For now, neglect the interaction of the pro- ton magnetic moment with the external magnetic field. Calculate the energies of the ground-electron-state levels of the hydrogen atom as a function of the applied magnetic field B.

(c) If one includes the interaction of the proton magnetic moment with the mag- netic field, two of the energy levels cross at a certain magnetic field value. Which levels cross and at what magnetic field does the crossing occur?

Hint For part (a), since the electron has no orbital angular momentum, one can think of the magnetic field from the electron Be being generated by a magnetization

ATOMIC STRUCTURE ( 1.41)

where 9e = 2 is the Lande g-factor for the electron, 5 and 1/J1oo(r) is then = 1, l = 0, m, = 0 ground state wavefunction of hydrogen.

Solution (a) The 1/)100( r) wavefunction is spherically symmetric, so we can envision the average magnetization produced by the electron ( 1.41) to consist of the contri~- tions of a series of concentric spherical balls each with constant magnetization Mi, so that ( 1.42)

Recalling from classical electromagnetism that the magnetic field inside a spheri- cal ball with constant magnetization M is given by (Griffiths 1999)

- 81r - B = 3 M, (1.43)

we have for the field at r = 0 B(O) = s; L Mi = s; Me(O) ' ( 1.44)

from which we can calculate the magnetic field seen by the proton using Eq. ( 1.41 ).

We assume that l1P1oo(r)l 2 = l1/Jioo(O)l 2 over the volume of the proton, 6 so - l61r - Be= -3µ0 l'I/J1oo(O)I S = - 3a~µoS, ( 1.45)

where we have made use of the fact that l1/J1oo(O)I = - 3 .

7rao ( 1.46)

The Hamiltonian H hf describing the interaction of the magnetic moment of the proton ~ with this magnetic field is thus _ - - - Hhf = -µp. Be= 3 39pµNµol. s' ao where 9p = 5.58 is the proton g-factor and µN is the nuclear magneton.

( 1.47)

5 Note that the standard sign convention for the Bohr magneton is positive, so the magnetic dipole moment of the electron is µe = -geµ,o.

6 An imponant point is that the hyperfine interaction in this case arises due to the wavefunction overlap between the proton and electron. This is somewhat subtle, as can be seen by comparing this analysis to that carried out in Problem 2.5 for a small ball carved out of a uniformly magnetized ball.

HYPERFINE STRUCTURE AND ZEEMAN EFFECT IN HYDROGEN Using the same trick employed in the derivation of the fine structure splitting in Problem 1.3, we find that the Hamiltonian has the form In units where Ii = 1, - - a 2)

H hf = al · S = - ( F - I - S .

a~ 5.58- 3µNµo ~ 1420 MHz, 3a0 and in terms of the eigenvalues of the angular momentum operators, a Hhr = 2 [F(F + 1) - J(J + 1) - S(S + 1)].

Therefore the hyperfine splitting in the ground state of hydrogen is I fl.Ehr~ 1420 MHz, I which corresponds to electromagnetic radiation of wavelength A = 21 cm.

( 1.48)

( 1.49)

( 1.50)

( 1.51)

(b) From Eq. ( 1.50), we see that the energy eigenstates for the Hamilto- nian describing the hyperfine interaction are also eigenstates of the operators { F 2 , Fz, 12 , S2 }. Therefore if we write out a matrix for this Hamiltonian in the coupled basis, it is diagonal. However, the Hamiltonian H B for the interaction of the magnetic moment of the electron with the external magnetic field ( 1.52)

is diagonal in the uncoupled basis (which is made up of eigenstates of the operators { 12 , 1 z, s2 , s z } >.

The relationship between the coupled and uncoupled bases is as follows IF= l,MF = 1) = l+)sI+)1, IF= 1,MF = 0) = v'2(1+)8 H1 + Hsl+)1), IF= 1,MF = -1) = l-)sl-)1, IF= 0,MF = 0) = v'2(l+)sl-)1 - Hsl+)1) · ( 1.53)

( 1.54)

( 1.55)

( 1.56)

Employing Eqs. ( 1.50) and ( 1.52), one finds for the matrix H for the overall Hamiltonian (Hhr + HB) in the coupled basis:

ATOMIC STRUCTURE I 1, 1)

11, -1)

I 1, o)

I0,0)

(1, 11 l + µ,oB (1, -11 ~ - µ,oB (1, Ol a µoB (0, Ol µoB 3a --:r We can use this matrix to solve for the energies of the states as a function of B by employing the Schrodinger equation ( 1.57)

which implies that (H - El)l'l/J) = 0.

( 1.58)

where 1 is the identity matrix. If (H - El) had an inverse, then we could multiply both sides of Eq. (1.58) by {H - El)- 1 to show that 11/J) = 0. Assuming 11/J)

-# 0, in order to satisfy Eq. ( 1.58), the matrix (H - El) must be singular. This implies that its detenninant is zero: i + µoB- E ~ - µoB- E % - E µoB µoB - 3f - E =0.

( 1.59)

The above expression is known as the secular equation. The matrix is block diagonal, so the energies are obtained by solving a 4 + µoB- E = 0, a 4 - µoB- E = 0, (: - E) (- 3: - E) - µiB 2 = 0 .

This gives the following energies a E1 = 4 + µoB, a E2 = 4 -µoB, a a ✓ µ2B2 E3 = -- + - 1 + 4........;o:;.__ a2 ' E4 = - a - a ✓l +4µlB2 a2 ' ( 1.60)

( 1.61)

( 1.62)

( 1.63)

( 1.64)

( 1.65)

( 1.66)

HYPERFINE STRUCTURE AND ZEEMAN EFFECT IN HYDROGEN F=O -3000 L-----.L..---.I-------L...---.1----------'------' B(G)

FIG. 1.3 Energies of the ground-state hyperfine manifold of hydrogen as a function of applied magnetic field. Such a plot is known as the Breit-Rabi diagram. At low fields, the system is well described in the coupled basis (F = 1, 0), while at high fields the energy eigen- states are best approximated by the uncoupled basis. The energies of the IF= 1, MF = 1)

and IF= 1, Af F = -1) states are linear in the magnetic field because they are not mixed with other states by the magnetic field [see Eqs. ( 1.53) and ( 1.55)).

which are plotted as a function of B in Fig. 1.3.

(c) If we include the effect of the proton's magnetic moment, we have j1 = ile + jlp, ( 1.67)

so ( 1.68)

In the high field limit we expect that the highest energy state should be the I+) s I-) 1 state. In the low field limit, the I 1, 1) = I+) s I+)

1 state is the highest energy state, so these two levels must cross at some magnetic field.

In part (b ), where we neglected the proton magnetic moment, for sufficiently high fields (2JJ,oB / a >> 1 ), the difference in energy between the two highest lying energy levels is [see Eqs. ( 1.63) and ( 1.65)): ( 1.69)

When the difference in energy between I+)

1 and I-) 1 due to the interaction of the proton's magnetic moment with the magnetic field is equal to this energy

ATOMIC STRUCTURE difference, then the levels will cross. This occurs for the magnetic field: a B~ ---- ~ 167kG.

2 X 5.58 X µN

## 1.5 Hydrogenic ions

( 1.70)

Hydrogen is an attractive object for the study of atomic structure because its simplicity allows accurate theoretical calculations which can be compared to experiment. A number of features in the energy-level structure of hydrogen are more pronounced in hydrogenic ions (atoms consisting of one electron bound to a nucleus with Z > 1) due to the larger nuclear charge. Hydrogenic ions are of interest for precision experiments testing quantum electrodynamics (Silver 200 I), measuring the mass of the electron ( Quint 200 I ), detennining the fine structure constant (Quint 200 I), and testing the Standard Model of electroweak interactions (Zolotorev and Budker 1997), to name a few.

For hydrogenic ions with nuclear charge Z, find the scaling with Z of: (a) the expectation values of r, I/ r, and I/ r 3, where r is the distance of the electron from the nucleus, (b) the expectation value of the potential energy V, ( c) the total energy E, (d) the probability to find the electron at the origin, l1P(r = 0)12, (e) l¾l/i(r = 0)12, (f) the fine structure energy splitting (see Problem 1.3), and (g) the hyperfine structure energy splitting due to the magnetic dipole moment of the nucleus (see Problem I .4). In this part, neglect the nonsystematic dependence of the nuclear dipole moments on Z.

Hints You should not have to use any explicit wavefunctions - just consider the dimensions of the quantities of interest.

HYDROGENIC IONS Solution First, let us consider how the natural length scale of hydrogen, the Bohr radius ao = h2 / me 2, compares to the natural length scale of a hydrogenic ion. The Hamiltonian for a hydrogenic ion is H = - n2 v'2 - ze2 .

2m r (1.71)

If we replace r with p = r / Z in the Hamiltonian (I. 71 ), taking into account that ( 1.72)

we have H = z2 (- /i2 v'2 - e2 ) .

2m, P p ( 1.73)

Thus the Hamiltonian for a hydrogenic ion can be put into one-to-one correspon- dence with the Hamiltonian for hydrogen by rescaling r by a factor of z- 1, so the natural length scale for a hydrogenic ion is ao a= z.

( 1.74)

One can also see from Eq. (l.73) that the total energy scales as Z 2 compared to hydrogen, which is the answer to part (c).

(a) As mentioned above, a = a0/Z is the only length scale for the system.

Therefore any quantity with units [length]n must scale as z-n. Thus, for any n, (b) The potential energy of an electron in a hydrogenic ion is Ze 2 V(r) = -- , r and, based on part (a), since r- 1 ex Z, it is clear that ( I. 75)

( 1.76)

( I. 77)

(c) Although we have already seen from Eq. (l.73) that (E) ex Z 2, we can also obtain this result by relating the total energy to the potential energy. According to

ATOMIC STRUCTURE the virial theorem, for two particles interacting via a central, conservative potential V ( r) = Crn, the expectation value of the kinetic energy (T) is given by (T) = n (V).

( 1.78)

For the electrostatic attraction between the nucleus and the electron, n = -1.

Therefore (E) = (T) + (V) = 2(V) , so we find (d) Since the hydrogenic wavefunctions are nonnalized, [ l1P(r)l 2 d3r = 1 , and it is apparent that l1P( r = 0) 12 has the dimensions [length)- 3 • Thus I 11P(r = 0)1 2 ex: Z • I (e) l¾1P(r = 0)12 has units of (lengthJ- 5, so evidently a -'lp(r = 0)

ex Z5 • 8r ( 1.79)

( 1.80)

( 1.81)

(1.82)

( 1.83)

(0 From the point-of-view of the electron, the nucleus of charge Z is orbiting around it with velocity v ~ Zoe (see Appendix A). Since the electric field f, due to the nucleus is f, = Ze 2 ' r ( 1.84)

the magnetic field B due to the relative motion of the electron and nucleus is B= Vx £ C Z2oe ""-J __ ,..._, .

r ( 1.85)

GEONIUM This magnetic field interacts with the spin magnetic dipole moment of the electron to induce an energy shift ( 1.86)

Since the expectation value of 1 / r 2 scales as Z 2, the fine-structure splitting scales as ( 1.87)

(g) In part (a) of Problem 1.4, we saw that the hyperfine energy splitting ~Ehr for an s state is <X 11/J(O)

12, because the hyperfine shift is due to the interaction of the nuclear dipole moment with the magnetic field generated by the magnetic dipole moment associated with the electron spin. Using the result of part (d), we see that I fl.Ehr CX: Z . I ( 1.88)

We get the same result for higher angular momentum states. Indeed, here one can view the hyperfine shift as arising from the interaction of the electron mag- netic dipole moment with the magnetic field due to the nuclear dipole moment (the problem can be solved from either perspective). Since the magnetic field of a dipole falls off as 1 /r 3, according to part (a) of this problem, ~Ehr <X ( r- 3) <X Z 3.

Note that the contribution to the hyperfine energy splitting from the nuclear quadrupole moment Qij, which arises from the interaction of Q with the electric field from the electron E = e / r 2, scales in the same way: fl.Ehf(Q) = Qij . OEi ~ Q OE ~ Qe ex: z3 .

OXj or r 3 ( 1.89)

## 1.6 Geonium

A beautiful and very useful "atomic system" was invented and perfected by Hans Dehmelt and co-workers (Dehmelt 1989). It consists of a single electron ( or positron) confined inside a Penning trap (Fig. 1.4). Dehmelt called this system "geonium" (Van Dyck, Jr. et al. 1976), since it is essentially an electron bound to the Earth. The geonium atom has enabled precise measurements of the electron and positron g-factors (Van Dyck, Jr. et al. 1987) which, in combination with the calculations of Kinoshita ( 1996), constitute one of the best tests of the fundamental theory of quantum electrodynamics and one of the most accurate determinations of the fine structure constant. These results have recently been improved by nearly an

ATOMIC STRUCfURE order of magnitude by Gabrielse and co-workers (Odom et al., 2006; Gabrielse et al., 2007) - the culmination of almost 20 years of development of new techniques since the 1987 measurement.

The quadrupolar electrostatic field produced by the Penning trap's electrodes is described by the scalar potential 4l = N(x2 + y2 - 2z2) .

(l.90)

In addition to the electrostatic field, there is a homogeneous leading magnetic field Bo = Boz. These fields can confine an electron to a region near the axis of the trap for many months! The electron's motion can be subdivided into axial oscillations (the electron moves along the symmetry axis of the trap (z), reversing direction when it comes too close to one of the negatively charged caps) and motion in the xy-plane (the cyclotron motion and a slow drift referred to as the magnetron motion).

(a) What is the axial oscillation frequency wz for motion of the electron along z (assume the electron is on-axis, x = y = 0)?

(b) Ignoring the effect of the electric quadrupole field, calculate the cyclotron frequency We with which the electron orbits about the trap axis.

(c) The Hamiltonian for the cyclotron motion can be put in one-to-one correspon- dence with the Hamiltonian for a one-dimensional simple harmonic oscillator (ID -Q/2 -Q/2 FIG. 1.4 Schematic picture of a Penning trap. The top and bottom conducting caps are charged to -Q /2 and the ring is charged to +Q, which generates a quadrupolar electrostatic field. A strong, homogeneous magnetic field Bo is applied in the z-direction. A nickel wire (magnetized to saturation by Bo) is wrapped around the center of the ring electrode to provide the .. bottle field" used to measure propenies of the trapped electron.

FIG. 1.5 Path of an electron in the midplane of a Penning trap executing magnetron and cyclotron motion. The path is a superposition of tight orbits associated with the cyclotron motion and an orbit with larger radius which is the magnetron motion. For illustrative purposes, the ratio of the period of the cyclotron motion to that of the magnetron motion has been increased by a factor of rv 105 compared to that for typical experimental conditions.

SHO). Show how this can be done (this was first realized by Landau in 1930, and the corresponding energy levels are known as Landau levels). Continue to ignore the electric quadrupole field.

(d) Consider an electron in the midplane of the trap (z = 0). Including both the homogeneous, z-directed magnetic field Bo and the electric force, calculate the frequencies of circular motion.

The faster frequency is the shifted cyclotron frequency w~ and the slow fre- quency Wm describes the magnetron motion (Fig. 1.5). The magnetron motion is a specific case of what is generally known as the E x B drift [see, for example, Jackson (1975)], where a charged particle in a combination of nonparallel mag- netic and electric fields tends to "drift" in a direction orthogonal to both fields.

Since in the present case, the magnetic field is in the .£-direction and the electric field is in the radial direction, the electron drifts in a circular path 7 centered about the trap axis.

It turns out that the magnetron motion can be described using the formalism of the ID SHO just like the cyclotron motion, except that as the magnetron quantum number q increases, the magnetron energy decreases (Brown and Gabrielse 1986).

This is because the electrostatic potential for an electron in the midplane of the trap is cl> = N(x2 + y2), which means that the larger the radius of the magnetron orbit, the lower the energy. Therefore the magnetron motion is unbound, in the sense that 7 Here we have decomposed the motion in the xy-plane into cyclotron and magnetron motion, both of which are circular.

ATOMIC STRUCTURE as the electron dissipates energy, q gets larger and larger until the particle collides with the ring electrode.

(e) For the Penning trap used in Dehmelt's experiments at the University of Wash- ington, the axial oscillation frequency was Wz = 21r x 60 ~IHz. A 5 T (50,000 G)

magnetic field was applied along the trap axis.

Sketch an energy level diagram for geonium with these experimen- tal parameters. What is the energy difference between the geonium states Im= +1/2,n,k,q)

and Im= -1/2,n + l,k,q), where mis the quantum num- ber describing the projection of the electron spin along z, n and q are the cyclotron and magnetron quantum numbers, and k is the quantum number describing axial oscillations?

(f) In addition to the fields discussed in the introduction to this problem, a weak "bottle" magnetic field Bb is applied to the electron, where Bb = -,B [ zxi:+ zy:Q - ( z2 - x ; y ) Z] .

( 1.91)

The bottle field allows measurement of the cyclotron, spin, and magnetron quan- tum numbers using what is known as the "continuous Stem-Gerlach" technique (Dehmelt 1989). The inhomogeneous bottle field interacts with the spin and motion of the electron (the magnetron and cyclotron motions, because they involve a charged particle moving in a circular orbit, produce magnetic dipole moments which interact with the bottle field). These interactions shift the axial oscillation frequency, which is measured with a radio-frequency resonant circuit.

In early geonium experiments, the magnetic bottle field was produced by a nickel wire (magnetized to saturation by Bo) wound about the ring electrode (Fig. I .4).

Show that the correction to the axial oscillation frequency Wz due to the spin orientation, cyclotron motion, and magnetron motion is given by: dWz ~ m + n + - + -q -- .

( Wm ) 2µof3 We ffleWz ( 1.92)

Hints In part (c), use the fact that the kinetic momentum mv of an electron in the pres- ence of a magnetic vector potential A is related to the canonical momentum pin the following way [see, for example, Griffiths ( 1999) or Landau and Lifshitz ( 1987)]: - - eA- mev = p - - , ( 1.93)

C

GEONIUM and this is the momentum that enters the kinetic energy term in the Hamiltonian.

For example, choose the vector potential to be ( 1.94)

and show that the effective Hamiltonian H~ describing motion in the xy-plane can be written ( 1.95)

where Yo is a constant.

In part (t), an effective magnetic dipole moment µ can be assigned to the mag- netron and cyclotron motion by setting the energy of the Landau levels equal to µBo.

Solution (a) On the axis of the Penning trap (x = y = 0), there is a restoring force 8<1> Fz = e az = -4eNz.

(1.96)

The effective spring constant for this simple harmonic motion is 4eN, so the axial oscillation frequency is Wz= f4eif_ v-:;;; ( 1.97)

(b) The force on the electron due to Bo must balance the centrifugal force in order to hold the electron in orbit: V WcT mew c r = e- Bo = e- Bo , ( 1 . )

C C where r = Jx 2 + y 2 is the radius of the electron's orbit and v - wcr is the electron's velocity. The cyclotron frequency is eB 0 We= - .

(J.99)

ffleC (c) The vector potential A for the uniform field in the z-direction can be written, for example, as: A= -Boyx.

( 1.100)

ATOMIC STRUCTURE Using Eq. ( 1.93), the Hamiltonian He governing the cyclotron motion is He= 2:J (Px - ~Boyf +p~ + P;] · Note that the Hamiltonian does not contain the coordinates x and z, so it commutes with the momenta in the x and z directions: (I.I 02)

The ref ore motion in the axial direction can be decoupled from the cyclotron motion in this case, and Px can be treated as a constant. We can rewrite the effective Hamiltonian H~ describing motion in the xy-plane as ( 1.103)

where Yo= C'JJx/(eB 0). Therefore the cyclotron motion can be described with the formalism developed for the 1 D simple harmonic oscillator, even though it is a two-dimensional problem.

(d) In the midplane of the trap, the force Fe due to the electric quadrupole field is radial, F.....

8'1> A 2 ~ A me A e = e OTT = e,,rr = 2WzTT , (1.104)

where we employed Eq. (1.97). This force subtracts from the radial force due to the magnetic field [Eq. ( 1.98)), (1.105)

The above relation yields [using Eq. ( 1.99)] a quadratic equation for the new frequencies w of circular motion in the midplane: w2 w2 - Wc;W + 2z = 0 .

(1.106)

We obtain two roots of this equation, giving us the shifted cyclotron frequency w~ and the magnetron frequency Wm: I Wz w ~w -- C 2wc ( 1.107)

and GEONIUM w2 ,._ z Wm,._ - .

2we (I.I 08)

These are approximate roots under the assumption that We >> Wz, as is the case in the experiment.

(e) From parts (a) and (c) and the statement of part (d), we know that the axial, cyclotron, and magnetron motions can be described using the formalism of the ID SHO. We must also recall that there is an energy splitting between the electron spin up and spin down states due to the magnetic field B0 . Therefore, the energy levels of geonium are specified by four quantum numbers: m, denoting the spin projection along the z-axis, n, describing the cyclotron motion, k, the axial quan- tum number, and q, the magnetron quantum number. The spin quantum number can take on the values ±1/2, while n, k, and q can equal 0, 1, 2, 3, ...

The energy of a particular state In, m, k, q) of geonium is given by Enmkq = 9eµoBom + hw~ ( n + 1)

+ liwz ( k + 1) -hwm ( q + 1) , (I.I 09)

where 9e is the electron g-factor. The values of the energy splittings, for the experimental conditions listed in the statement of the problem, are 9eµoBo ~ 2 x 1.4 MHz/G x 50, 000 G = 140 GHz , ( 1.110)

w~ ~ eB0 ~

## 4.8 x 10- 10 esu x 50,000 G

= 140 GHz, 21r 21rmec 21r x 9.1 x 10- 28 g x 3 x 1010 cm/s Wz - =60MHz, 21r Wm w; {60 MHz) 2 21r = 41rwc ~ 2 X 140 GHz ~ 13 kHz ' where we have made use of the fact that w~ ~ we.

(I.Ill)

( 1.112)

(1.113)

This gives us a basic idea of the energy levels for geonium. It is, of course, no accident that the frequencies given by Eqs. ( 1.110) and ( 1.111) are nearly the same.

Let us take a closer look at the nearly identical splittings between the different spin states and cyclotron states. Since eli µo = 2 ' ffieC (l.114)

• • • n = 3 -----c: n=2-----r n=l -----r n =O _ ___.___,.

ATOMIC STRUCfURE m=+l/2 --- 140GHz m=-1/2 ,~--~M • 164 MHz • • • __ k-_J _ _i k=2 60MHz ..------,-- k=l ' • • • FIG. 1.6 Geonium energy levels (not to scale). Adapted from Van Dyck, Jr. et al. ( 1978).

the difference in energy tiE between the geonium states Im= +1/2, n, k, q) and Im= -1/2,n+ l,k,q) is I t::,.E ::::::: (Ye - 2)µoBo ::::::: 164 MHz · I (1.115)

Thus, measuring this frequency difference enables a measurement of Ye - 2. The g-factor of the electron differs from 2 by a small amount~ o:/(21r) which can be accurately calculated using the theory of quantum electrodynamics.

A schematic sketch of the geonium energy levels is shown in Fig. 1.6.

(f) Here we again consider the axial oscillation frequency on-axis (x = y = 0), now taking into account the bottle field in conjunction with all the various motions.

The Hamiltonian H governing the axial motion is given by: H P~ ... B ...

~ ~ {32 2"2 = -2- - µ · b - e';I.' = -2- - µeff z + e"z , me me ( 1.116)

where µeff is the effective magnetic moment of the electron due to its spin, cyclotron and magnetron motion (discussed in detail below). Equation ( 1.116) is

GEONIUM the Hamiltonian for a ID SHO: H Pi ,22 = 2me + 2meWz z ' where the new axial oscillation frequency w: is given by: ,2 2µetrf3 4eN Wz =---+-.

me me ( 1.117)

(I.I 18)

The second tenn in Eq. ( 1.118) is the square of the unperturbed axial oscillation frequency Wz ( 1.97), so the axial oscillation frequency in the presence of the bottle field is given by: The correction to the axial oscillation frequency is thus given by dwz ~ - µeff /3 .

meWz Now we need to detennine µeff, which is given by: ( I. 119)

( 1.120)

(l.121)

where µ 8 is the spin magnetic moment, µc is the cyclotron magnetic moment, and µm is the magnetic moment due to magnetron motion. The spin magnetic moment is: (1.122)

If we assign an energy -µcBo to each of the Landau levels for the cyclotron motion, we can associate the cyclotron frequency with a magnetic moment according to: ( 1.123)

so that µc = -2µo(n+ D.

( 1.124)

The magnetron motion can be described in the same manner: ( 1.125)

ATOMIC STRUCTURE Employing the above relations in Eq. ( 1.120), we find: 6wz ~ 2µo/3 (m + n + -2 1 + (q + 1/2tm)

Wzffie We ( 1.126)

agreeing with the equation in the statement of the problem, if we neglect the 1/2 associated with the magnetron motion (since under typical experimental conditions q >> 1).

The axial oscillation frequency, therefore, is sensitive to the cyclotron, spin, and magnetron quantum numbers. Whenever the electron makes a quantum jump between energy levels, this is observed as a sudden shift in Wz. In practice, to measure Wz, an oscillating drive voltage is applied to the caps of the electrode (Fig. 1.4), and the amplitude of the axial oscillation greatly increases when the drive frequency hits resonance. This method of detection uses what is known as the "continuous Stem-Gerlach effect," since it is analogous to the classic experiment [see, for example, Griffiths ( 1995) or Bransden and Joachain (2003)] in which the trajectories of silver atoms in an atomic beam are perturbed by the interaction of their dipole moments with a magnetic field gradient.

A clever technique is employed to measure the 9e -2 anomaly [ discussed in part (e)]. An inhomogeneous, radio-frequency magnetic field at Wrt ~ 21r x 164 MHz is applied to the electron. If the inhomogeneous field was de, then an electron moving through the field would see a magnetic field oscillating at the cyclotron frequency. Because the field is oscillating with frequency Wn, the electron sees (in its rest frame) sidebands at w = we± wn. Thus when Wrt corresponds to the dif- ference ~E from Eq. ( 1.115) between the energy level splitting between different spin orientations and that between different cyclotron levels, spin flips are induced (since w = We + Wn = 9e/1-0Bo). The increased rate of spin flips is detected using the continuous Stem-Gerlach effect. This constitutes a direct measurement of the 9e - 2 anomaly.

## 1.7 The Thomas-Fermi model (T)

A starting point for precise numerical calculations of atomic energy levels in com- plex, multi-electron atoms is the theory developed independently by Thomas and Fermi [see, for example, Bransden and Joachain (2003) or Landau and Lifshitz ( 1977)]. The Thomas-Fermi model assumes that the electron cloud is a zero tem- perature Fermi gas. The central result of this model can be derived by balancing ~ electrostatic forces with the gradient of pressure (VP) produced as a consequence

THE THOMAS-FERMI MODEL (T)

of the Pauli exclusion principle: VP(r) = p(r)l(r)

= -en(r)[-V<P(r)], ( 1.127)

where p( r) = -en( r) is the charge density, n( r) is the electron number density, e ( r) = -V ¢( r) is the electric field, and ¢( r) is the electrostatic potential.

Equation ( 1.127) is the condition for hydrostatic equilibrium. This means that in the Thomas-Fermi model, we treat the electron cloud as a fluid, much like the atmosphere of the Earth, except here electrostatic forces due to the nucleus hold the fluid in rather than gravity. To describe the electron cloud in this manner, we assume that the electrons can be treated semiclassically and assume that we may apply statistical arguments. Such an approach is justified if the atom has a large number of electrons (N >> 1).

(a) Discuss why the condition N >> l allows one to use the semiclassical approximation.

Solution If N >> 1, because of the Pauli exclusion principle, many of the electrons must occupy states with large radial quantum numbers n. The key requirement for employing the semiclassical approximation is that there must be many oscillations of the wavefunction over the regions of space where the potential changes appre- ciably. In other words, the deBroglie wavelength Ade rv li/p must change slowly with respect to the distance from the nucleus: OAdB l a;:-<< .

( 1.128)

The typical angular momentum of an electron with radial quantum number n is given by L = rp rv nli , ( 1.129)

which implies that Ade rv r / n. Therefore, the condition ( I . 128) requires that n >> l, ( 1.130)

which is true for most electrons if N >> 1.

(b) Calculate the Fermi momentum PF (the momentum of the electron with the highest energy) for an electron gas in a small volume V. Use the fact that since the electron wavefunctions are semiclassical, they can be approximated by plane waves. Also assume that the number of electrons within V is large enough that one can apply statistical arguments.

Solution ATOMIC STRUCTURE The number of electron states dN with momenta between p and p + dp occupying a small volume V is given by (l.131)

where we have taken into account that the number of possible states per unit vol- ume is doubled for electrons due to their spin (compared to a particle without spin). The number of available electron states per unit volume (at zero tempera- ture, this is equal to the electron density since each state is occupied) can be found by integrating Eq. ( 1.131) from O to p F (the Fermi momentum), yielding N = _l_p} .

(1.132)

V 31r 2 !i3 From Eq. ( 1.132), we have ( 31r2 N)

1/3 PF= Ii V .

(l.133)

(c) Calculate the total kinetic energy K of the electron gas.

Solution The total kinetic energy K can be obtained by multiplying dN from Eq. ( 1.131)

by the kinetic energy per electron p2 /2m (where m is the electron mass) and integrating from Oto PF: (1.134)

Substituting the value of PF from Eq. ( 1.133) into our expression for kinetic energy ( 1.134) we obtain: (l.135)

(d) Using the thermodynamic relation for the Fermi pressure P = -dK/dV [valid at zero temperature, see Reif ( 1965)], obtain the pressure of the electron gas as a function of density. The Thomas-Fermi model assumes Vis small compared to the volume of the atom, so that P is the local pressure at a particular distance from the nucleus.

ELECTRONS IN A SHELL Solution Using the thermodynamic relation P = -dK/dV: ( 1.136)

which yields the pressure as a function of electron density n( r) in the atom 32/3 4/3 fi2 P(r) = : m [n(r)] 5/ 3 .

(l.137)

(e) Now use Eq. (1.137) in conjunction with Eq. (1.127) to obtain a relationship between the electrostatic potential </J( r) and the electron density n( r).

Solution Employing Eq. ( 1.137) in Eq. ( 1.127) and integrating gives ( 1.138)

where ¢0 is a constant of integration. Equation ( 1.138) is the central result of the Thomas-Fermi model.

Equation ( 1.138) can be combined with the Poisson equation, ( 1.139)

to obtain two independent equations for the two unknown functions n( r) and¢( r ), and values of these functions for various r can be obtained numerically, taking into account the appropriate boundary conditions [see, for example, Bransden and Joachain (2003), Landau and Lifshitz ( 1977), or Messiah ( 1966)].

## 1.8 Electrons in a shell

In this problem (Budker 1998a), intended to illustrate the basic principles of the Thomas-Fermi method, we consider the case of a large number of electrons at zero temperature placed inside a spherical cavity of radius a with impenetrable walls. This is like an atom without the nucleus ( of course, the walls are necessary to keep the electrons from flying apart due to the electrostatic repulsion). In the

ATOMIC STRUCfURE FIG. 1. 7 Electrons collect in a shell of thickness 6 near the wall.

followi~g problem we ignore all numerical factors, such as 4,r, in order to simplify expressions and concentrate on the scaling of various effects. Assume a >> ao, where ao = h 2 I ( me2) is the Bohr radius. Note that under the stated conditions, the Thomas-Fermi model (Problem 1.7) is applicable.

(a) Argue that the electrons collect in a thin shell of thickness 6 at the edge of the spherical cavity. Determine the scaling of 6 with respect to the number of electrons N and radius of the cavity a.

(b) For what N does the assumption that the electrons are nonrelativistic break down?

(c) What is the lower bound on N for which the assumptions of the Thomas-fenni model are satisfied? &ti mate 6 for the case of low N.

Hint For part (a), suppose that the shell contains half the electrons in the cavity.

Solution (a) The boundary conditions in this problem are, of course, quite different from those for an atom: here there is no positively charged nucleus at the center and there is an infinitely high potential barrier at r = a. Choosing the electrostatic potential as, for example,</,= Oat the boundary, the functions </>(r) and n(r) can be obtained by numerical integration of the Thomas-Fermi equation.

However, without resorting to detailed calculations, we can obtain a general idea of the spatial distribution of the electrons in the cavity. Consider a shell of thickness 6 bounded by the wall of the cavity containing half of the electrons (we will see that 6 « a). The Coulomb repulsion from the other electrons tends to compress the shell as a whole, pushing the shell toward the wall. We define the Coulomb pressure Pc as the repulsion force (rw N 2e2 /a 2) per unit surface area of

ELECTRONS IN A SHELL the shell: N 2e2 (1.140)

Pc"' a4 In equilibrium, this Coulomb pressure is balanced by the Fermi pressure p from Eq. (1.136) in Problem 1.7, li2 ( N )5/3 p"' m a25 ' where we have substituted V ~ a20. Setting P = Pc, we find tbat 2/5 3/5 a ao 6"' Nl/5 .

(1.141)

(1.142)

A be fi Eq ( I 142) r ~ a so indeed the electrons collect in s can seen rom .

.

, u '"'..:: ' .

.

a th· h II h f h ·ty It is particularly 1nterest1ng to note that the 1n s e at t e e ge o t e cav1 .

.

.

thickness of the shell decreases as more electrons are placed 10 the cavity.

(b) The assumption that the electrons are nonrelativistic _wil_l break down w_hen the Fermi momentum PF becomes of order me. By substttut10g Eq. (1.142) 10~0 the expression for PF [Eq. (1.133)], and supposing that t~e volume of the shell ts ~ a20 we obtain an expression for the Fermi momentum 10 terms of N: N2/s PF~ Ii 1/5 .

(1.143)

a4/5ao Setting PF = me, we find that the critical number of electrons N* for which the nonrelativistic approximation breaks down is N * (a2) -5/2 r'-1 2 a ' ao (l.144)

where a = e2 / lie is the fine structure constant.

(c) In order to see at which values of N the semiclassical approximation is valid, suppose that we gradually increase the number of electrons inside the cavity. At low densities, all electrons occupy the lowest radial state, which means that the se~iclassical approximation is invalid (Problem 1.7). Therefore, for low densities, most of the kinetic energy of the electrons is due to radial motion.

In this regime, we can estimate the thickness of the shell containing the elec- trons 6 by finding the minimum of the total energy E = K + U, where K is the

ATOMIC STRUCfURE kinetic energy and U is the potential energy due to the Coulomb repulsion between the electrons. For the 6 where the energy is minimized, aK au 86 + 86 = O.

(1.145)

Based on the Heisenberg uncertainty relation: ( 1.146)

where ~Pr is the uncertainty in the radial component of the electron momentum.

This tells us that the kinetic energy of radial motion, which as noted above is the dominant contribution to K, is (1.147)

so 8K Nli 2 -rv--- f)8 m83 · ( 1.148)

The Coulomb energy of the shell can be estimated from the work required to move the electrons in from the edge of the cavity by rv 8: N2e2 U rv --8 (1.149)

a2 from which we find 8U N 2e2 -rv .

a From Eqs. (1.146), (1.148), and (1.150) it follows that 2/3 1/3 a a0 <5 ~ Nl/3 ' ( 1.150)

(1.151)

which can be compared to Eq. ( 1.142), revealing a substantial difference between the two regimes.

In order to satisfy the Pauli principle, states of different angular momenta l are excited as the number of electrons in the cavity is increased. Setting the total number of electron states equal to the number of particles N, we have [see Eq. ( 1.25)]: L N = L)21 + 1) ~ L2 , ( 1.152)

l=O where L is the highest value of l which is excited.

ISOfOPE SHIFfS AND THE KING PLITT As we keep increasing N, at some point the kinetic energy due to the orbital motion of electrons with angular momentum L becomes equal to the kinetic energy of radial motion: --f'.J-- ma2 m'52 · (1.153)

At higher values of N, it is energetically favorable to excite higher radial modes, corresponding to the transition to the Thomas-Fenni regime discussed in part (a).

From Eqs. ( 1.152), ( 1.151 ), and ( 1.153), we obtain the lower bound N** on the value of N for which the Thomas-Fermi considerations apply: N ** f'.J ~ 2 • ao ( 1.154)

It is curious to note that this corresponds to a surface density of about one electron per Bohr radius squared.

The situation analyzed in this problem is difficult to realize experimentally because all materials are made of atoms, and so the impenetrable wall is unrealis- tic. However, such a situation could arise with quasiparticles in condensed matter physics.

## 1.9 Isotope shifts and the King plot

In atomic spectra, there appear small shifts of the transition energies for different isotopes. Such isotope shifts arise due to differences between the masses and the volumes of the nuclei. A commonly used method to separate experimentally mea- sured isotope shifts into mass and volume (or field) shift contributions is based on the so-called King plot (King 1963).

Consider two spectral lines A and B. Due to the isotope shifts, the resonance frequencies are slightly different for each of the isotopes. For pairs of isotopes, where the difference in neutron number LlN is always the same 8 and D.N is much smaller than the atomic mass, one can assume that • the isotope shift due to the finite nuclear volume can be expressed as a prod- uct of an electronic factor E (different for lines A and B, but the same for each isotope pair in a given spectral line) times a nuclear volume factor V (different for each pair of isotopes, but independent of which line is used), and 8 If the difference in neutron number is not the same, we can always normalize the isotope shifts to, for example, ~N = 1 or 2.

ATOMIC STRUCTURE TABLE 1.2 Isotope shifts (IS) for various pairs of Sm isotopes for the 562.18 nm 7 F1 -+ 7 H2 transi- tion and the 598.97 nm 7 Fo -+ 7 D1 transition. Data from Brand et al. ( 1978). The table indicates the difference in the measured transition frequencies, for example, the resonance frequency for the 562.18 nm line was 3093.6(16) MHz higher for 144 Sm than for 148 Sm.

Isotope pair IS (MHz) for 562.18 nm IS (MHz) for 598.97 nm ~N (144,148)

3093.6(16)

-2794.4( 17)

(148,150)

1938.3(15)

-1641.2(13)

(150,152)

2961.0(15)

-2308.0( 19)

(152,154)

1362.3(11)

-1242.4( 17)

(147,148)

970.4(7)

-826.0(4)

I (148,149)

473.3(4)

-493.8(4)

I • the mass effects M are the same, in any one line, for all pairs of isotopes. 9 From these assumptions, it follows that if one makes a plot in which the isotope shifts for isotope pairs in line B are plotted against the isotope shifts for the same isotope pairs in line A, the points will fall on a straight line.

An example of original isotope shift data (Brand et al. 1978) is shown in Table 1.2. In this experiment, isotope shifts were measured in a number of spec- tral lines of samarium using laser spectroscopy and an atomic beam. The laser and atomic beams intersected at right angles, and laser-induced fluorescence was detected in a third orthogonal direction. This setup minimizes the Doppler broadening (see, for example, Problem 3.6) of the spectral lines.

(a) Derive expressions for the slope and intercept of this line in terms of EA, EB, MA, and MB.

(b) Using the data in Table 1.2, make a King plot with the 598.97 nm 7 Fo --+ 7 D1 transition as line A and the 562.18 nm 7 F 1 --+ 7 H 2 transition as line B.

(c) The mass shift term M consists of two contributions: M = M(nms) + M(sms)

, (1.155)

where the abbreviations stand for normal mass shift (nms) and specific (or anoma- lous) mass shift (sms). The former is due to the fact that all atomic energy intervals are proportional to the reduced mass rather than just the electron mass. The latter is 9 To be exact, the variation of the mass shift with nuclear mass should be considered. Since here we assume that t:.N is much smaller than the atomic mass, this can be done by introducing a small correction factor which can be ignored for the purpose of this problem.

ISOTOPE SHIFfS AND THE KING PLITT due to the correlation between momenta of various electrons. One can think of the specific mass shift as arising from the formation of multi-electron "quasi particles"

which move about the nucleus (King 1984).

Using the empirical information that the sms contribution in the 598.97 nm 1 F0 ~ 1 D 1 transition is negligible, evaluate the mass shift for the 562.18 nm 7 F1 ~ 7 H 2 transition. Compare its magnitude and sign to the expected normal mass shift.

Solution (a) We let the isotope shifts for line A be the independent variable x and the isotope shifts for line B be the dependent variable y. Based on the assumptions stated in the problem, we have for the isotope shifts: X = EA¼+MA' y =EB½+ MB' ( 1.156)

(l.157)

where i is the label for the isotope pair. Using Eq. ( 1.156), we can write ¼ in tenns of x, EA, and MA, MA Yi= EAX- EA.

(l.158)

Substituting this expression into the equation for y ( 1.157) yields (1.159)

(b) Making sure to divide all isotope shifts by the difference in neutron number ~N for the given pair (see Table 1.2), we obtain the King plot shown in Fig. 1.8.

We see that the points indeed fall on a straight line.

(c) We begin by estimating the nonnal mass shift. For a single-electron atom, the finite mass of the nucleus can be taken into account by using the solution for an infinitely heavy nucleus and replacing the electron mass with the reduced mass µred: mMNA µred= m+MNA' (l.160)

where MN is the nucleon mass and A is the atomic mass number. Since energies of all atomic levels are proportional to this mass, a transition corresponding to an

ATOMIC STRUCfURE ~ (150,152)

u 1400 ;§ E 1200 C (148.150)

'° (147,148)

V)

(144,148)

... 800 ~ .-...

:z 600 (152,154)

~ (148,149)

:r: 400 ~ - ct:: :E fl)

8.

0 0 ~ Isotope shift (MH:zlAN) for 598.97 nm line FIG. 1.8 King plot for samarium transitions listed in Table 1.2.

isotope with mass number A is shifted compared to that of a (fictitious) isotope with infinite nuclear mass by: ~w = wo(µred - m) = wo( MNA - 1)

m+MNA ~-MNAwo.

(1.161)

Transitions corresponding to isotopes A and A + ~N are shifted by 6.w' = wo(- MNA +mMN6.N + M:A)

m~N ~ wo MNA2 , (1.162)

where we have made use of the fact that ~N << A. For the optical transitions near 600 nm considered here, with ~N = 1 as in our King plot (Fig. 1.8), this corresponds to ~w' ~ 5 x 1014 Hz 2 ~ 12 MHz .

1836 X 150 (1.163)

The mass shift for the 598.97 nm transition, MA in our case, is given by MA= M1nms) + Mtms> .

(1.164)

CRUDE MODEL OF A NEGATIVE ION We have shown that M~nms) ~ 12 MHz, while it is known empirically that M~sms)

is negligible. From the y-intercept on the King plot and Eq. ( 1.159), we find that the quantity MB - (EB/ EA)MA ~ -280 MHz. The slope of the King plot shows that (EB/EA) ~ -1. 5, so we obtain a mass shift of ~ -300 MHz for the 562. 18 nm transition, which is larger in magnitude and of opposite sign compared to the normal mass shift. Such large and originally unexpected specific mass shift contri- butions are often found in the rare earth elements when the number of /-electrons is different in the upper and lower states (the 562.18 nm transition is nominally between electron configurations 4/ 66s2 and 4/ 55d6s2).

## 1.10 Crude model of a negative ion

Singly charged negative ions (K = 1) are very common (Massey 1976), and sev- eral doubly charged (K = 2) negative ions of atoms [see Massey ( 1976), Chapter 5.8] and clusters (Vandenbosch et al. 1997) have been observed as well. It is not entirely obvious that such systems should be bound - one might expect that the Coulomb repulsion between an extra electron and the original Z electrons could overwhelm the attraction of the extra electron to the nucleus. Here we construct a crude model to see that such a conclusion need not be correct.

Using an electrostatic analogy, explain why it is possible to have bound states of a positive nucleus of charge +z with an electron cloud of charge -(Z + K), K>O.

Hint As a very crude model of an atom, consider electrons as a conducting shell, and neglect the exchange interaction between electrons (see Problem 1.2). The I I I I I I ------: I I I I I I FIG. 1.9 Charge Q• can hold together the parts of a conducting sphere carrying charge Q.

ATOMIC STRUCTURE exchange interaction is actually of great importance in many cases - nonetheless, this simple model illustrates the basic physical principle behind the existence of negative ions.

Solution Let us formulate the following electrostatics problem. Consider a thin spherical conducting shell which is charged to total charge Q. Suppose the sphere is cut into two parts. Since each of the two resulting parts carries a charge of the same sign, the two parts will tend to fly apart. What is the charge that one needs to put in the center of the sphere in order to keep the two parts together?

In order to answer this question, we use the following facts from electrostatics: • The pressure produced by an electric field Eis -E 2 /81r.

• The electric field inside a conductor is zero.

• The electric field from a uniformly charged spherical shell is zero inside the shell, and outside the shell, it is just as if all charge was in the center of the sphere.

If there is no charge in the center, there is no field inside the sphere, and the two parts are "sucked" apart by the negative pressure of the field outside. All we need to do to compensate for the negative outside pressure is put a charge (call it Q*) in the center such that the magnitude of the field inside the shell (near its surface) is the same as outside. The field inside is Q* / R2 (R is the shell radius, which will, of course, cancel). Outside, the field is ( Q + Q*) / R2• If we want to match the magnitudes of the fields inside and outside the shell, we need to have: Q* = -(Q + Q*) ⇒ Q* = -Q/2.

( 1.165)

Any charge of sign opposite to that of Q and magnitude larger than IQl/2, placed in the center, will hold the system together.

## 1.11 Hyperfine-interaction-induced mixing of states of dif-

ferent J Two atomic fine structure levels in a multi-electron atom, 2 P3; 2 and 2 P 1; 2, are separated by an energy gap ~E. The nuclear spin of the system is I = 1 /2.

Determine the admixture of the 2 P3; 2 , F = 1 state in the state that is nominally 2 P1;2, F = 1 if the energy separation between the 2 P3; 2 , F = 2 and 2 P3; 2, F = 1 hyperfine states is ~Ehr << ~E. Assume that the hyperfine interactions are

HYPERFINE-INTERACTION-INDUCED MIXING OF STATES OF DIFFERENT J 2 1:12 ---F=2 FIG. 1.10 Energy level diagram for two atomic fine structure levels, 2 P312 and 2 P1;2, with hyperfine splitting. Nuclear spin is / = 1 /2.

dominated by the Hamiltonian term 10 Hhr = af- S.

( 1.166)

Hyperfine-interaction-induced mixing of states with different J is important, for example, for understanding hyperfine structure splittings in situations where the fine structure intervals are relatively small. This occurs for certain excited states in He and He-like atoms [Bethe and Sal peter ( 1977), Section 44]. Another example is hyperfine-interaction-induced transitions between two levels of nominal J = 0 [see, for example, Fischer et al. (1997), Section 9.12, and Birkett et al. (1993)].

Hint Note that the Hamiltonian describing the hyperfine interaction does not mix states of different For MF. This is because H hr is a scalar operator (see Appendix F).

10 In general, the expression for the hyperfine Hamiltonian describing the interaction of the magnetic moment of the nucleus with a single atomic electron is (Sobelman 1992, Section 6.2.2)

Hhr = a,f. f- a,(s- 3(s· f)f] · f, where f is a unit vector along rand a, is a constant proportional to (r- 3 }. For multi-electron atoms, the general expression for the hyperfine splitting is composed of two parts, one proportional to f · S and another proportional to f · l. The relative importance of the two parts depends on the particular configuration. For example, in a two-electron atom where one electron is in the ground state and the other is in an excited state with l ~ 1, the term proportional to f •§dominates (Bethe and Salpeter 1977).

Solution ATOMIC STRUCfURE First we neglect the mixing of states with different J and relate ~Ehr to the coeffi- cient a appearing in Eq. (1.166). Note that the 2 P3; 2 , F = 2 state corresponds to a maximum possible projection of the vectors l, § and f onto each other. Therefore9 the expectation value off• § in this state is simply (f • §) = I/ 4.

Even though the hyperfine splitting is dominated by the term al · § in this problem, it is still the case that we can write, according to the usual formulae for hyperfine structure, A EF = 2[F(F + I) - J(J + I) - I(I +I)], ~Ehf = EF - EF-I =AF' ( 1.167)

(1.168)

where A is the hyperfine structure constant and EF represent hyperfine energy shifts. This is because both § and l are vector operators (see Appendix F), so (§) ex (J) and (L) ex (J), and we may write EF = (Hhr) = A(f · J), ( 1.169)

from which we obtain the formulae (1.167) and (1.168). In our case (J = 3/2, I= 1/2, F = 2, 1), so these formulae yield: A= ~Ehr/2, EF=2 = B~Ehf · ( 1.170)

(1.171)

Now we use the fact that the dominant contribution to the hyperfine splitting comes from al• § to write ( 1.172)

which gives us ( 1.173)

Now we evaluate the hyperfine interaction matrix element between the F = l states. As mentioned above, the interaction ( 1.166) can only mix states with the same value of F and Mp. We perform explicit calculations for Mp= 1; however, the result must not depend on Mp due to isotropy of space. We need to express the states in the IL, ML)IMs)IM1) basis. We do this by first expanding into the

HYPERFINE-INTERACTION-INDUCED MIXING OF STATES OF DIFFERENT J fJ, MJ)IM1) basis (using the Clebsch-Gordan coefficients): J3 I P3;2,F = 1,MF = 1} = 213/2,3/2}1-}1- 213/2, 1/2}1+}1' (1.174)

12 P1;2, F = 1, MF= 1) = I 1/2, 1/2)1+) / .

(1.175)

Next, we expand into the IL, ML)IMs)IM1) basis: J3 I P3;2, F = 1, MF= 1} = 211, 1)1+}8/-}1 - 2\/'311, l}Hsl+}1 (1.176)

- ./611, O}l+}sl+} 1, I 2P1;2, F = 1, MF= 1} = /i11, l}Hsl+}1 - Ja11,0}l+}sl+}1 · (J.177)

Next, we explicitly evaluate the matrix element of f • § between th~ st~tes ( 1.176) and ( 1.177). One way to perform this calculation is to express I · S in terms of the raising and lowering operators for the angular momenta f and § [see, for example, Griffiths ( 1995)]: for which I±= Ix± ily, S± =Bx± iSy, I±II, M1) = JI(/+ 1) - M1(M1 ± I) II, M1 ±I), S±IS, Ms)= ✓scs + I) - Ms(Ms ± I) IS, Ms± I).

Using Eqs. ( 1.178) and ( 1.179), we find that (l.178)

(1.179)

( 1.180)

(1.181)

(l.182)

Employing the expressions for the atomic states in terms of the IL, ML)IMs)IM1)

basis [Eqs. (1.176) and (1.177)] along with the relations ( 1.180) - ( 1.182), we obtain - .... 2 2 a ( P3;2,F= 1,MF= llal·SI P1;2,F= 1,MF= 1} = 3v'2, ~Ehf - v'2 .

( 1.183)

(l.184)

ATOMIC STRUCTURE ---- Finally, we determine the mixed eigenstate 12 P112, F = 1) from first-order perturbation theory: (I. I 85)

We see that, up to a numerical coefficient, the amplitude for the mixing of states with different J is given by the ratio of the hyperfine-structure interval to the fine- structure interval.

## 1.12 Electron density inside the nucleus (T)

A number of phenomena in atomic physics depend on the electron density inside the nucleus - for example, hyperfine structure (see Problems 1.4 and 1.5), isotope shifts (Problem 1.9), and parity nonconservation (Problem 1.13). In this problem, we determine the scaling with Z of the electron density inside the nucleus (r ~ 0) for s- and p-wave valence electrons in heavy, neutral, multi-electron atoms.

This result was first derived by Fermi and Segre ( 1933), and the discussion below roughly follows that of Landau and Lifshitz ( 1977) and Khriplovich ( 1991 ).

(a) We begin by considering the properties of a valence electron.

Argue that a single valence electron in a heavy, multi-electron atom is found primarily at distances ~ ao from the nucleus. Also note that the core electrons are found at distances~ ao.

Solution Let us imagine that we build up the multi-electron atom by starting with a bare nucleus and adding one electron at a time. The first electron added will create a hydrogenic ion, and so the electron's average distance (r) from the nucleus will be ~ a 0/ Z as discussed in Problem 1.5. As we continue to add electrons, because the nucleus is shielded by the electrons already in place, each successive electron added is more weakly bound than the previous. According to this simple picture, we conclude that ( r) has a larger value for the valence electron than for any of the other (core) electrons, i.e., the valence electron is indeed the "outer" electron. 11 11 When there are multiple valence electrons, this argument does not necessarily hold for some of the electrons. For instance, in the complicated valence shells of the transition metals and rare earth atoms, valence d and / electrons are actually held more tightly to the nucleus than the valence s- wave electrons. This is the reason that the chemical properties of the rare earths are all rather similar (determined predominantly by the valences-wave electrons).

ELECTRON DENSITY INSIDE THE NUCLEUS (T)

Just before the final, valence electron is added, we have a nucleus of charge +Ze surrounded by an approximately spherical distribution of Z - I core electrons - from a large distance, this looks just like the nucleus of a hydrogen atom. Therefore we expect the valence electron to orbit at a distance rv a0 from the nucleus.

Also, we can draw from our knowledge of chemical bonds and radii of different atoms to note that there is not a significant change in atomic radii as a function of Z and bond lengths are usually a few Bohr radii. Since it is the valence electrons that determine the chemical properties of an element and define the radius of the atom, we can say from these empirical facts that the valence electron spends most of its time at distances ~ ao.

This conclusion can also be arrived at using the Thomas-Fenni model (Prob- lem 1.7).

(b) Based on part (a), what can one say about the wavefunction of the valence s-wave electron in the region ~ a0 from the nucleus?

Solution We have learned that a valence electron spends most of its time beyond ao and most core electrons are at distances < a0 • The core electrons screen the nuclear charge in the region r ~ a0, so the wavefunction for a valence s electron beyond ao is similar to that for the hydrogen ls state (since the nucleus plus core electrons in this range "appears" to be a nucleus with charge +e): ( 1.186)

where C is a constant approximately independent of Z. The Z-independence of C follows from the fact that ( 1.187)

Although we will see that there is some nonzero probability for an electron to be found near the nucleus, because the valence electron is found predomi- nantly at distances ~ ao from the nucleus, equation ( 1.187) is generally a good approximation.

(c) Now we consider the region close to the nucleus. At what distance from the nucleus is the nuclear charge completely unscreened by core electrons? What is the form of the valences electron wavefunction in this region?

Solution ATOMIC STRUCfURE We know that the radius of a hydrogenic ion is ao/ Z (see Problem 1.5), and addi- tional electrons will have higher energy and therefore be,<: ao/Z away from the nucleus, so for ~ ~ we can regard the nucleus as completely unscreened. 12 In this region, 11/Js(r) = Ae-Zr/an ' I where the constant A has Z dependence which will be determined later.

(I.I 88)

(l.189)

(d) In between these two regions, show that the electron is quasiclassical (satis- fying the conditions for application of the WKB approximation 13), and determine the f onn of the wavefunction in this region in terms of r and the momentum of the electron p.

Solution In order to satisfy the assumptions of the WKB approximation, the wavefunction must oscillate many times within a distance where the potential energy changes significantly. This means that the deBroglie wavelength of the electron, Ii Ade = 21r- , p must change slowly with respect to the distance from the nucleus: {),X a:.B « 1 .

The WKB approximation does not apply for r ,<: a0 , since in this region the electron wavefunction does not oscillate.

( 1.190)

(1.191)

(l.192)

12 In fact, the Thomas-Fermi model shows that nuclear screening is already negligible for r << a0z- 113 , a much larger radius, but Eq. ( 1.188) is sufficient for our purposes.

13 This approximation is named for Wentzel, Kramers, and BriJJouin, who were the first to apply the method of "short wavelength asymptotics," commonly used in optics, to quantum mechanics (see, for example, Griffiths ( 1995), Bransden and Joachain ( 1989), or Landau and Lifshitz ( 1977)).

The method can, in fact, be applied to any wave system.

ELECTRON DENSITY INSIDE THE NUCLEUS (T)

In the region r << a0, the nuclear charge is not well screened by the core electrons, so we may crudely estimate that the effective nuclear charge Ze«( r) rv Z. Since the total energy of the valence electron is rather small (rv I eV), we estimate that the kinetic energy of the electron in this region is about equal to Ze 2 /r. Employing the classical approximation for the momentum of the electron in this region ~ p(r) ~ V--:;:-.

Thus the deBroglie wavelength satisfies {rao Ade(r) ~ VZ, so that ( 1.193)

( 1.194)

8Ade ~ fao_ (1.195)

ar V Zr Comparing expressions ( I .191) and ( 1.195), and noting again that the WKB approximation does not apply for r ~ a0 ( 1.192), we see that the condition for application of the WKB approximation ( 1.191) is satisfied as l_ong as ao < z << r rv ao.

( 1.196)

What does this quasiclassical wavefunction look like? If we introduce a radial function u( r) such that 111, ( ) _ u(r)

'f/S T - ' r (l.197)

the radial part of the three-dimensional Schrodinger equation reads d2u 2m dr 2 + li,2 [E - Ve«Ju(r) = 0, (I.I 98)

which is just the one-dimensional Schrodinger equation. The quasicJassical solutions for the ID case have the fonn [Griffiths ( 1995), for example]

u( r) :::;::j :;e±(i/li.) f p(r)dr , ( 1.199)

where B is a constant. For this problem, we are not interested in the phase factor, so we say that in the quasiclassical region ( 1.200)

AlOMIC STRUCTURE (e) Using the results above, determine the scaling of l'l/Js(O)l 2 with Z.

Solution To determine the Z-scaling of f¢8 (0)f2, we patch the three solutions for 1/Js(r)

obtained in parts (b), (c), and (d) together. At r rv ao, from Eqs. ( I .186) and ( I .200), we have B I ---rvce-.

aoJo:mc ( 1.20))

Since C is independent of Z, B must also be independent of Z.

At r rv ao/ Z, we have ZB A -1 ---===rv e ' aoJZo:mc (1.202)

where we made use of the fact that p rv Zo:mc (the momentum for a hydrogenic ion) near r rv a0/Z. Equation (1.202) means that A ex VZ, and consequently, (1.203)

(f) Use similar reasoning to obtain the approximate form of 'l/Jp(r) close to the nucleus.

Solution For the p-state, we can apply similar reasoning to that employed in finding the wavefunction for the s-state. Ignoring angular factors and keeping only terms up to CJ( r) (since we are interested in the behavior of the wavefunction at r ~ 0), we see that the p wavef unction should behave as 'Ip ( r) rv C .!_ e -r I ao P Pao > r rv ao ' (1.204)

Bp ao < < ( 1.205)

rv-- z rv r rv ao ' ryP A r e-Zr/ao < ao (1.206)

l"V p- rrv z.

ao As for the s-state [part (b) of this problem], because of the shielding of the nuclear charge by the core electrons, we expect Gp to be approximately independent of

PARITY NONCONSERVATION IN ATOMS Z. Matching the solutions for ·t/Jp(r) at r rv a0 shows that the constant Bp is also independent of Z. Matching the solutions for ·i/Jp(r) at r rv ao/Z requires that Thus, for r << a0 / Z, ( z)

3/2 Ap rv -ao

## 1.13 Parity nonconservation in atoms

( 1.207)

( 1.208)

Before the mid- l 950s, physicists believed that the laws of Nature were invari- ant with respect to spatial inversion (also known as the parity (P) transformation, which reverses the directions of alJ three spatial axes). Spatial inversion changes the handedness of an object or a process (a tenn stemming from the fact that P turns a glove for the left hand into a glove for the right hand). Spatial inversion is an example of a discrete transformation, as opposed to a continuous transforma- tion (for example, a finite rotation can be thought of as a succession of infinitely smaJI rotations).

In 1956, the belief in P-invariance was shattered by a series of experiments, where violation of this symmetry at a rv 100% level was discovered in weak- interaction-induced nuclear decays [see, for example, Trigg ( 1975), chapter I 0].

When Glashow ( 1961 ), Weinberg ( 1967), and Salam ( 1968) developed what came to be known as the Standard Model of electroweak interactions, they pre- dicted the existence of a neutral weak interaction mediated by a particle called the Zo boson. Even before the advent of the Standard Model, Zel'dovich ( I 959) had noted that if there were a parity-violating electron-nucleon weak neutral-current interaction, it would interfere with the regular electromagnetic interaction in an atom. Zel'dovich's estimate for the size of this effect, however, indicated that it would be too small to measure with experimental techniques available at that time.

Later, motivated by the new developments in weak interaction theory and the tremendous advances in laser spectroscopy, Bouchiat and Bouchiat ( 1974) rean- alyzed the possibiJity of searching for parity nonconservation (PNC) in atomic systems. They found that in fact the effects were considerably enhanced in heavy atoms, and according to the predictions of the Standard Model, should be observ- able. Based on this new analysis, many groups throughout the world began extensive experimental efforts to search for PNC effects in atoms.

The first experiments to observe PNC effects in atoms were carried out by Barkov and Zolotorev ( 1978) in Novisibirsk using the technique of optical rotation

ATOMIC STRUCTURE in bismuth and by Commins and co-workers (Con!i et al. _ 1979) at Berkeley using the Stark-interference method (see Problem 4.5) m thalhum. These experiments provided crucial evidence that helped establish the existence of the neutral weak current and were the first indications of the parity-violating nature of the neutral weak interaction.

At present, atomic PNC experiments continue to serve as stringent tests of the fundamental theory of electroweak interactions and as sensitive probes for new physics (Khriplovich 1991; Bouchiat and Bouchiat 1997; Budker 1998b ).

The most precise measurement of PNC effects in an atomic system to date was performed in Boulder by Wieman and collaborators (Wood et al. 1997), using the Stark-interference technique with cesium. This experiment also was the first to definitively observe nuclear-spin-dependent PNC effects, primarily due to the nuclear anapole moment ( discussed in detail in Problem 1.15 ). In this problem we restrict our considerations to nuclear-spin-independent PNC effects.

(a) In the nonrelativistic approximation and the limit of infinite Zo mass, the Hamiltonian Hw describing the weak interaction between the nucleus and a single electron is given by (Bouchiat and Bouchiat 1974): where we have ignored nuclear spin-dependent effects and G ~ 3 x 10- 12mc 2(!!:__)

F me (1.209)

( 1.210)

is Fermi's constant, sis the electron spin, pis the electron momentum, and ( 1.211)

is the dimensionless weak nuclear charge (N is the number of neutrons and sin 2 9w ~ 0.23 where 9w is the Weinberg mixing angle).

Show that Hw violates parity.

(b) From the mass of the Zo (mz ~ 92.6 GeV /c 2), estimate the range of the neutral weak interaction.

(c) Consider the mixing of the opposite parity states lns1;2) and ln'p1; 2) (these are single-particle states for the valence electron), where n, n' are the principal quantum numbers. Show that the mixing is enhanced in heavy atoms by a factor proportional to Z 3 • (d) What is the significance of the fact that the matrix element (n'p 1; 21Hwlns1; 2)

is imaginary?

PARITY NONCONSERVATION IN ATOMS (e) Calculate the PNC-induced mixing between the 2S1;2 and 2P1; 2 states in hydrogen. Recall that the states are split in energy only by the Lamb shift (~E ~ 1058 MHz).

(0 Based on the calculation in part (e) for hydrogen, estimate the order of magnitude of the PNC-induced mixing between the 6s 1; 2 and 6p1; 2 states in Cs.

Hints In part (d), consider the fact that although Hw violates parity it does respect time- reversal invariance (T). In particular, consider the application of an electric field to a state that is not an eigenstate of parity, and show that if the matrix element (n'P1;2IHwlns1;2) is not purely imaginary the system is T-violating.

Solution (a) To prove that Hw violates parity, it is sufficient to show that it does not com- mute with the parity operator P. If [Hw, P] =I 0, then the energy eigenstates of the atomic system are not in general also be eigenstates of the parity operator. In this case, a state with definite parity must be a superposition of different energy eigenstates. Therefore, if the system is left to evolve in time, the parity of the state will change - i.e., parity is not conserved.

How does Hw transform under the action of P? Because Hw ex: s · P, and s, like orbital angular momentum, is an axial vector (pseudovector) which does not change sign under P while pis a polar vector which does change sign: (l.212)

Operating P on both sides of Eq. ( 1.212), we find that ( 1.213)

so H w and P anticommute, which means that ( 1.214)

(b) In order for a Zo to be exchanged between an electron and the nucleus, it must occur on a time scale sufficiently short so as not to violate energy conservation.

According to the Heisenberg uncertainty relation, ~EL),.t "' h .

(1.215)

ATOMIC STRUCfURE Thus the range R of the neutral weak force is he R"'"' c~t"'"' - .

~E (1.216)

We let ~E be the minimum energy required for the creation of a Zo, mzc2. Then R he

## 197.3 MeV · fm

10_3 f rv -- rv ------ rv X m .

mzc 2

## 92.6 x 103 MeV

( 1.217)

Treating Hw as a point-like interaction is a very good approximation in atomic physics.

(c) To first order in time-independent perturbation theory, the weak Hamiltonian admixes some of the ln'p) state into an Ins) state according to (1.218)

where ~E = E 8 - Ep is the energy separation between the states (where E 8 is the energy of lns1; 2) and Ep is the energy of ln'p1; 2)). Because, as discussed in part (b), the interaction is point-like, the mixing between the sand p states depends on the s and p wavefunctions near the nucleus. From Problem 1.12, we have for the s state in the region r :5 a0/ Z ,.1, (r) ~ v"z e-Zr/a., o/S 3/2 ' ao (1.219)

where the factor of a~312 gives the wavefunction the correct dimensions. For the p-state in the same region, 1/Jp(r)

rv _ .!_e-Zr/ao .

( z)3/2 ao ao (1.220)

The weak Hamiltonian ( 1.209) has two terms. The second term does not contribute to the matrix element because (1.221)

This follows from the fact that an electron in an s-wave state has zero momentum at the origin, as well as the fact that the p wavefunction has a value of zero at r = 0. Thus only the first term contributes, and so the matrix element between the

PARITY NONCONSERVATION IN ATOMS ln'p) state and the Ins) state is given by ( 1.222)

( 1.223)

In the above estimate, we have set s • p = h,pr /2, since details of the angular distribution of p do not affect the Z-scaling.

From Eq. ( 1.220), we see that {Jl/Jp I ~ z3/2 or O ao and since then using Eq. ( 1.223), we have GFQwn (n P1;2IHwfns1;2) "'-i 4 Z · mca 0 The weak charge Qw is roughly proportional to the atomic number, so ( 1.224)

( 1.225)

(l.226)

( I .227)

Usually this result is understood as a consequence of the electron density inside the nucleus for s-states, l1/Js(O)l 2, scaling as Z (Problem 1.12), the momentum of the electron (which enters Hw) near the nucleus (where there is no shielding)

scaling as Z, and the scaling of Qw with Z. This explanation is equivalent to our considerations above if one takes into account the fact that the momentum operator acting on the p-wave state yields ( 1.228)

The observation that the PNC-induced mixing is inversely proportional to the energy difference between the states [Eq. ( 1.218)] has led to the suggestion to measure PNC in atoms with nearly degenerate opposite parity levels: the hydrogen 2s-2p system [Hinds ( 1988) and references therein] and heavy elements such as the rare earth atoms (Dzuba et al. 1986), e.g., samarium (Barkov et al. 1989;

ATOMIC STRUCTURE Wolfenden and Baird 1993), dysprosium (Budker et al. 1994; Nguyen et al. 1997), and ytterbium (DeMille 1995).

(d) The PNC-induced mixing between the ln'p) and Ins) states is imaginary [Eq. ( 1.226)] because the weak interaction violates parity but not time-reversal invariance (T).

Consider the application of a static electric field (along z) to an atom in the state lns112) [see Eq. (l.218)]. The Hamiltonian governing the interaction of the electric field with the atom is (in the single-electron approximation)

( 1.229)

where dis the electric dipole operator and Eo is the magnitude of the electric field E. The first-order energy shift due to the electric field is tlE(l)

= eEo(ns1;2lzlns1;2)

= eEo( (ns1;2I - i77(n'P1;2l)z(lns1;2) + i77ln'P1;2)) ~ ( 1.230)

( 1.231)

where we have implicitly assumed that the states lns 1;2) and ln'P1;2) have the same projection of total angular momentum on the quantization axis [so that they can be coupled by the Hamiltonian H1 ( 1.229)] and i77 is the PNC-induced mixing amplitude [Eqs. (l.218) and (1.226)]: .

(n'P1;2IHwlns1;2)

i1J = LlE .

Since z only connects states of opposite parity, we have LlE(l) = eEo(ns 1;2lzln'p 1; 2)(-i17 + i17) = 0, where we have made use of the fact that ( 1.232)

( 1.233)

(1.234)

Thus there is no linear Stark shift because i77 is purely imaginary.

If i77 had a real part, tlE(l)

would be nonzero, which would violate T- invariance. To see this, we note that if ~E(l) = -(d· E) =I= 0, then (d) -# 0.

The Wigner-Eckart theorem (Appendix F) states that any vector quantity must be proportional to the total angular momentum of the system, so: (d) oc (]) .

( l.235)

However, the time reversal operator T takes d ~ d while it takes J ~ -J, so the existence of a "permanent" electric dipole moment ( one that exists even in

PARITY NONCONSERVATION IN ATOMS the absence of an applied electric field) violates T-invariance (see Problem 4.8 for further discussion).

(e) The weak Hamiltonian is a scalar operator, so it only couples states having the same total angular momentum J and the same projection of angular momentum MJ. Thus we will consider the PNC-induced mixing between the MJ = 1/2 states, .

(2P1;2 MJ = 1/21Hwl2S1;2 MJ = 1/2)

i17 = ~E ' ( 1.236)

realizing that, because of rotational invariance, the M J = -1 /2 states have the same mixing amplitude.

To simplify the notation, taking into account Eq. ( 1.221 ), we may write ( 1.237)

where GF {3 = J2 2mcli Qw · ( 1.238)

The S and P states can be expressed as products of the spin wavefunctions, I+) and I-), and the spatial wavefunctions, In, l, m1), using Clebsch-Gordan coefficients: 12S1;2 MJ = 1/2) = 12, 0, 0) I+) ' ( 1.239)

l2P1;2 MJ = 1/2) = JI 12, 1, 1)1-) - II 12, l,O)I+).

( 1.240)

First we will finds· 'il2P 1; 2 MJ = 1/2). The operators· p, represented in the spin basis using the Pauli matrices, is given by Thus, in the spin basis, we have S · P l2P1;2 MJ = 1/2) = /i2 ( P+z.

Px tpy )]

( 1.241)

(l .242)

(1.243)

Px - ipy ) ( -I} 12, 1, 0) ) .

-pz Jj 12, 1, 1)

( 1.244)

ATOMIC STRUCfURE Substituting this into Eq. ( 1.236), we have . AE n/3 ZTJ/j = TX (-ff (2, 1, Ojpz63(r)j2, 0, 0) + /: (2, 1, ll(Px + ipy)t5 (r)l2, 0, 0))

.

( 1.245)

In the above equation, note that ( (2P 112 MJ = 1/21 S · _p), whi~h apJ>t:ars in the formula for TJ ( 1.236) when expression ( 1.237) for H w JS used, JS obtained frof'll ( 1.244) by Hermitian conjugation. Next we take into account the fact that in the spherical basis (see Appendix F)

so Pl = - ~ (px + ipy)

Po =pz .

P-I = v'2(px - zpy), (l.246)

() .247)

(l.248)

iTJdE = -r ( ~ (2, 1,01Po63(r)/2,0,0) +; (2. 1. ljp16 3(r)l2,0,0)).

(1.249)

Now we can apply the Wigner-Eckart theorem (Appendix F): (2, 1, OIPo63(r)l2, 0, 0) = ~(2, 111¢3(r)ll2, 0)(0, 0, 1, Oil, 0) ' (2, 1, llp163(r)l2, 0, 0) = ~(2, Ill¢ 3(r)ll2, 0)(0, 0, 1, ljl, 1) , () .250)

(1.25 I)

where (l1,m 1,K,qll2,m2) is the appropriate Clebsch-Gordan coefficient and (n2, l2/1¢ 3(r)/ln 1, l1) is the reduced matrix element. Both CJebsch-Gordan coef- ficients in ( 1.251) equal one, so using the fact that (2, 1, 0IPot5 3(r)l2, 0, 0) = (2, 1, llp1t53(r)l2, 0, 0) , in Eq. ( 1.249) we have - nf3v'3 TJdE - - 2i (2, 1, 0IPot5 (r)l2, 0, 0) .

(l.252)

(l.253)

Now we use the hydrogen wavefunctions in order to carry out the integral associated with the above matrix element. We begin by finding Po1P210(r). The

PARITY NONCONSERVATJON IN AlOMS momentum operator in the z-direction is given by li8 Po = Pz = -: - · z oz ( 1.254)

In order to differentiate the hydrogen wavefunctions, which are most conveniently expressed in spherical coordinates, with respect to z, we need to express fz in spherical coordinates: 14 a a sin 8 a - = cos8- - --- .

az 8r r 88 ( J .260)

The hydrogen wavefunction ¢2 1o(r, 8, </>) is ( ) _ r -r ; 2a., ¢210 r, fJ, </> - rn= 312 -e cos .

4v 21r a0 ao ( 1.261)

Employing Eqs. ( 1.260) and ( 1.261 ), we find that ( ~ Ii fJ ( ~ -iii ( r 2 8)

-r/2ao (I 262)

Po't/J210 r1 = -:-0 '¢210 r1 = rn= 512 l - -2 cos e · · z z 4v21ra 0 ao Now we are prepared to evaluate the integral in Eq. ( 1.253). Noting that we must take the complex conjugate of ( 1.262) and using the hydrogen wavefunction ¢200( r, 8, <P)

( ) _ 1 ( r )

-r/2a ¢200 r, 0, <I> - 2J2,r a3/2 1 - 2ao e ' 14 The gradient in spherical coordinates is given by - a,. 1a,.

1 a,.

V = 8r r + ~ 88 (} + r sin(} 8¢ <P ' while in Cartesian coordinates it is "

8,.

8,.

8,.

V = 8x X + 8y y + 8z z .

The spherical basis is related to the Cartesian basis by: f = sin Ocos ¢x + sin Osin ¢fJ + cos Oz, {J = cos (} cos ¢x + cos (} sin <PiJ - sin (} z ' ¢ = - sin </Jx + cos </>fJ • (1.263)

( 1.255)

( 1.256)

( 1.257)

( J.258)

( 1.259)

Using the above relations in ( 1.255), we find for the z-component of the gradient the expression given in Eq. ( 1.260).

AlOMIC STRUCfURE we obtain TJ!J.E = - h2/3J3! (1 -_,_· cos 2 ()) (1 - ~)e-r/a.,6 3(r)d 3r 321raJ 2ao 2ao ( I .264)

fi2{3J3 Using Eqs. ( I .238) and ( I .2 I 0) in ( I .265), we find !J.E __ (J_ GFQw rt - V 2 641r mcaJ = - (J_ 3 X 10-12 Qw lie(_!!:_)

V 2 641r a~ me = - {J_ 3 x 10-12 Qwa4mc2.

V 2 641r The weak charge for hydrogen, according to ( I .2 I I ), is Qw = I - 4sin 2 8w ~ 0.08.

Thus 17dE ~ -2 x 10- 18 eV.

(I .265)

( I .266)

(1.267)

(1.268)

(1.269)

(I .270)

The energy splitting between the 28 1; 2 and 2P 1; 2 states is given by the Lamb shift: D.E ~ 1058 MHz~ 4 x 10- 6 eV.

(1.271)

Therefore the PNC-induced mixing between the 28 1; 2 and 2P 1; 2 states in hydrogen is I 11 ~ -5 X 10-13 . I ( I .272)

Note that this effect is about an order of magnitude larger in deuterium, where the weak charge is Qw ~ -1. Experimental efforts to measure PNC effects in hydrogen are reviewed by Hinds ( 1988).

(0 As a rough estimate, we will say that the only differences between the PNC- induced mixing of states in hydrogen and the mixing in cesium are Z, Qw, and the energy level splitting. In this approximation, the amplitude 17( Cs) of the PNC- induced mixing between the 6s and 6p states in Cs is related to the amplitude of

PARITY NONCONSERVATION IN ANTI-ATOMS PNC-induced mixing of the 2s and 2p states in hydrogen, 11( H), by 71(Cs) ~ 71(H) Z 2Qw(Cs) AEH(2s, 2p)

Qw(H) ~Ecs(6s, 6p) ' ( J.273)

where Z = 55 is the atomic number of Cs, ~EH(2s, 2p) ~ 4 x 10- 6 eV is the splitting of the 2S 112 and 2P1; 2 states in hydrogen due to the Lamb shift, and llEcs(6s, 6p) is the energy separation between the 6s and 6p levels in Cs, ~E 0 ,(6s, 6p) rv -10 4 cm- 1 rv -1.25 eV.

(J.274)

Based on Eq. ( J .2 J )), we estimate the weak charge for Cs, Qw(Cs), to be ( 1.275)

close to the experimental result of -72.06( 46) (Wood et al. 1997), which differs from - 75 due to radiative corrections. 15 Using these values in ( 1.273), we get l 71(Cs) ~ -5 x 10- 12 • , ( 1.276)

A more detailed analysis for Cs leads to a result about twice as large 16 [see, for example, Khriplovich ( 1991) J.

Given the exceedingly small mixing amplitude, it is indeed a remarkable achievement that PNC in cesium has been measured to a fraction of a percent (Wood et al. 1997).

## 1.14 Parity nonconservation in anti-atoms

As discussed in Problem 1.13, parity nonconservation due to the neutral weak interaction manifests itself in atomic transitions. For example, for the highly 15 Radiative corrections are modifications to interactions due to higher-order processes - in the language of Feynman diagrams (Appendix H), they arise from diagrams with the same initial and final states but with more intermediate vertices than the lowest-order process [see, for example, the book by Griffiths ( I 987)]. For example, in the case considered here, the expression for Qw ( J .21 I) is based on Zo exchange between the nucleus and an electron. One of the Feynman diagrams describing a radiative correction to Qw involves a Zo propagating from the nucleus, then turning into a top quark and anti-top quark, which subsequently annihilate to create a Zo which then interacts with the electron.

16 One may note that because all the p-states in Cs are relatively far from the 6s state in energy, a proper calculation of PNC effects should include a sum over all p-states. However, the amplitudes of the couplings to states other than the 6p and 7p are rather small, and one can obtain a reasonably accurate prediction for the PNC-induced mixing by only including the admixtures of the 6p and 7p states into 6s. The PNC-induced mixing between 6s and 7p is a factor of~ 4 smaller than the 6s-6p mixing, so our estimate should give close to the right result for the total mixing of p-states into the 6s state.

ATOMIC STRUCTURE forbidden one-photon decay of unpolarized excited hydrogen f2S) ~ I IS)+,, (1.277)

the emitted photons have a preferred circular polarization. The effect is larger for deuterium, due to its larger weak charge Qw [Eq. (1.211)]. For deuterium, the degree of circular polarization of the photons is ,v 2 x 10- 4 • As it turns out, while P-invariance is violated, the symmetry is almost restored by performing the combined transformation of spatial inversion and charge con- jugation, 17 C. So far, the only examples of CP-violation have been found in the decays of neutral K- and B-mesons, and for the purpose of this problem, we will assume that CP is a good symmetry.

The question is: if hydrogen preferentially emits right-circularly polarized (R)

photons, 18 what is the sign of the preferred circular polarization for antihydrogen?

Antihydrogen has been produced at CERN (G. Baur et al. 1996) and FermiLab (G. Blanford et al. 1998) using particle accelerators. The antihydrogen produced in these experiments travel nearly at the speed of light with respect to the laboratory reference frame, making it exceedingly difficult to perform precision spectroscopy.

Low-energy antiprotons and cold positrons can be stored simultaneously in nested Penning traps (Gabrielse et al. 1999), and quite recently this method has been successfully used to produce cold antihydrogen (Amoretti et al. 2002, Gabrielse et al. 2002). This appears to be a promising route toward producing antihydrogen useful for spectroscopic tests. Antihydrogen may serve as an interesting system with which to test CPT and Lorentz invariance [see, for example, Holzscheiter and Charlton (1999) and Gabrielse (2001)].

Solution Consider the decay ( 1.277) as seen in the laboratory and in its mirror image (upper part of Fig. 1.11 ). Mirror reflection changes the R photons into L photons (L and R designate left- and right-circular polarization, respectively), so looking in the mirror, we see that excited hydrogen preferentially decays into L photons. This actually does not occur in reality, which is the essence of parity nonconservation: laws of nature are not the same in the real laboratory and its counterpart in the mirror. (In this case, the law of nature says that excited hydrogen preferentially decays into R photons.)

17 This transformation changes matter into antimatter.

18 In this book, we use the spectroscopists' convention for left and right circular polarization, where au+ photon (one with positive helicity, with the photon spin along its direction of propagation) is said to be left-circularly polarized, and a u _ photon is said to be right-circularly polarized.

PARITY NONCONSERVATION IN ANTI-ATOMS H(2S)➔H( IS)+ j'(R) 1:(2S)➔H( IS)+ )'(L)

H(2S)➔H( IS) + j'(R) I; (2S)➔ H (IS) + ')(R)

H(2S)➔H( IS)+ )<R)I H (2S)➔ H (IS)+ l(L)

CP FIG. 1.11 Hydrogen I 2S) -+ f IS) + ~ decay as seen in the laboratory, and upon action of various transformations: P, C, and the combined CP-transformation. H designates antihydrogen. --y(L)

and ~(R) designate photons and their preferential circular polarization.

Now, instead of a usual (P) mirror that inverts coordinates, 19 consider its C- analog. A "C-mirror" reverses all charges converting particles into antiparticles, but does not affect coordinates. Looking at the original process in such a mirror (middle part of Fig. 1.11 ), we see antihydrogen preferentially decaying into an R photon, and again, this does not occur in reality (C-violation).

In order to determine how antihydrogen actually decays, we can use CP- invariance, and look at the original process in a "CP-mirror" (the lower part of Fig. 1.11 ). Because of CP-invariance, whatever we see in the "CP-mirror" actu- ally corresponds to a real process that, at least in principle, can be reproduced in the laboratory. The conclusion is that antihydrogen preferentially decays into L photons, and the degree of circular polarization is the same as for hydrogen.

The same result can be obtained more formally. First consider hydrogen. Its Hamiltonian can be written as H = Ho +Hw, ( 1.278)

where Ho is the parity-conserving part of the Hamiltonian, and Hw is the parity- violating part. As we have seen in Problem 1.13, the parity-violating part of the Hamiltonian leads to mixing of eigenstates of Ho which have definite parity. In particular, an eigenstate of the full Hamiltonian is now (I .279)

19 Actually, a mirror inverts only one out of three coordinates, but this is not essential since inver- sion of all three coordinate axes is equivalent to inversion of just one of them followed by a rotation by 180 degrees around the inverted axis.

ATOMIC STRUCfURE Here we used first-order perturbation theory, E 2s and E2p are the energies of the corresponding eigenstates of Ho, and we neglected mixing of 12S) with all states other than the nearby l2P). As we have seen in Problem 1.13, the con- stant i1] turns out to be imaginary as a consequence of T-invariance. The form of Eq. ( 1.279) corresponds to the so-called "spin-helix," whose sign dictates the preferred handedness of the decay photon [see (Khriplovich 1991 ), Chapter 2 for details].

Now, let us analyze antihydrogen. In quantum field theory, antihydrogen is automatically included in the Hamiltonian, so generalizing ( 1.278) we write: H =Ho+ Hw +Ho+ Hw, (1.280)

i.e., we explicitly include the parity-conserving and parity nonconserving terms for antihydrogen (the bar designates quantities related to antihydrogen). CP-invariance means that the full Hamiltonian ( 1.280) is invariant under CP, so (l.281)

The analog of Eq. ( 1.279) for antihydrogen is: (l .282)

In order to evaluate i77, we can start with the definition of i17, and insert the identity (CP)- 1(CP) = 1 on both sides of the operator Hw: i1] = (2PIHwl2S) = (2Pl(CP)- 1(CP)Hw(CP)- 1(CP)l2S) (1.283)

E2s - E2p E2s - E2p _ (-2Pl(CP)Hw(CP)- 112S)

E2s - E2p = _ (2PIH wl2S) = _8 .

~-E2p (1.284)

(1.285)

Here we used the properties of the wavefunctions CPl2S) = 12S), CPl2P) = -l2P) (C just adds a bar, and P changes the sign of odd-parity wavefunctions), and the invariance of eigenenergies of Ho+ Ho with respect to CP. This shows that the sign of parity-violating mixing for antihydrogen is opposite to that for hydrogen, which implies preferential emission of L-photons, in agreement with our earlier conclusion.

THE ANAPOLE MOMENT (T)

## 1.15 The anapole moment (T)

The anapole (Zel'dovich 1958) is an electromagnetic moment 20 that appears, along with the more familiar moments such as the magnetic dipole, in the mul- tipole expansion of the vector potential of an electromagnetic current distribution of finite spatial extent, e.g., an atomic nucleus.

The anapole moment a of the system is defined as ii.= -1r f r2]U"!)d 3r, (1.286)

where J(r) is the current density. From this definition, as we will show in this problem, it follows that the anapole 's contribution to the vector potential is ( 1.287)

indicating that in order for a charged particle to "feel" the anapole moment it has to penetrate within the current distribution ( contact interaction).

20 Different electromagnetic moments correspond to the different rank tensors necessary to describe charge and current distributions.

~ a FIG. 1.12 The simplest system with nonvanishing "irreducible" anapole moment: a toroidal wind- ing which can be thought of as a succession of current loops offset from the origin. Figure courtesy of S. M. Rochester.

ATOMIC STRUCTURE In order to visualize the simplest systems possessing an anapole moment, first consider a current loop offset from the origin (Flambaum and Murray 1997).

Straight from the definition ( 1.286), there is a nonzero anapole moment pointing in the direction opposite to that of the current at a point furthest from the origin. A direct generalization of this is a toroidal winding (Fig. 1.12) where the current con- secutively flows through a series of such loops. Note that in this case, in contrast to a single loop, the magnetic field produced by the current is confined within the torus. In addition, the value of the anapole moment does not depend on the choice of the origin. The situation here is analogous to a single charge offset from the origin and a dipole formed by two opposite charges. One may say that the toroidal current is the simplest example of an "irreducible" anapole.

Now to the problem.

(a) Explain why only nuclei with nonzero spin can have an anapole moment, and why an anapole can only arise due to parity-violating interactions. 21 Solution As is true for any rank-one tensor (vector) characteristic of a system (in this case an atomic nucleus) the ana~le moment must be proportional to the total angular momentum of the system, f (see Appendix F). The parity-violating nature of the anapole moment becomes apparent when one considers the behavior of a and f under spatial inversion: while the latter is a pseudovector, the former is a normal vector just like J [see Eq. ( 1.286)]. Note, however, that the existence of an anapole moment does not violate time-reversal invariance because both ii, and fare T-odd.

(b) Now we will embark on the derivation of Eq. ( 1.287), which can be done similarly to the derivation of the "usual" moments (magnetic dipole, etc.), see, for example, Jackson ( 1975) or Landau and Lifshitz ( 1987). This part of the problem requires somewhat involved graduate-level mathematics (tensor algebra).

The derivation presented here follows that of Sushkov et al. ( 1984) and Khriplovich ( 1989, 1991 ). We start from the general expression for the vector potential A(R) = ! j [W> d3r , C IR- r1 ( 1.288)

and expand the integrand in powers of r / R (assuming R >> r). 22 21 The nuclear anapole moment, arising due to the weak interaction (Problem 1.13), was recently discovered in an atomic PNC experiment using cesium by Wood et al. ( 1997).

22 A conscientious reader may question the validity of this approach, since we begin by expand- ing the vector potential in the limit where R >> r and end up with a delta function [Eq. ( 1.287)).

Nonetheless, more rigorous derivations (Flambaum and Khriplovich 1980; Flambaum and Hanhart 1993) confirm the conclusions presented here.

THE ANAPOLE MOMENT (T)

Consider the zeroth-order tenn in the expansion of the vector potential ( 1.288).

Show that it vanishes for an atomic nucleus.

Solution It is convenient to use the vector fonn of the Taylor expansion: IR~r1 = ~-(vk~)rk+½(vkv,~)rkr1+ ... , ( 1.289)

where we foil ow the usual convention in which summation is assumed over repeated indices.

The zeroth-order tenn in the expansion of the vector potential ( 1.288) is thus J(O) ( R) = c~ J J(r)d3r.

( 1.290)

This quantity vanishes for atomic nuclei because there cannot be any average cur- rent for a system of finite size in a steady state (for which the spatial distribution of charges does not change with time).

(c) Now consider the first-order term in the expansion of the vector potential. Show that it corresponds to the potential due to a magnetic dipole.

Solution The integrand in the first-order term for each Cartesian component of the vector potential can be decomposed into a symmetric and an antisymmetric part: = -~ ( Vk ~) j [½(jirk + ikri) + ½(jirk - ikn)]d 3r. ( 1.291)

Next, we use a common trick involving Gauss' theorem that says that the vol- ume integral of a spatial derivative of an arbitrary well-behaved function f is equal to the surface integral of the function itself ( 1.292)

to show that the integral with the symmetric combination in Eq. ( 1.291) vanishes.

Indeed, consider the integral ( 1.293)

ATOMIC STRUCTURE Converting the integral over volume to a surface integral according to Eq. ( 1.292> and choosing the integration surface outside the boundaries of the system (where the current is zero), we see that the integral ( I .293) vanishes. On the other hand~ we also have 0 =JV m(rirk}m)d 3r = J ( t5mirk}m + rit5mk}m + Tirk VJ)d 3r.

( 1.294)

The last term in the integrand of ( I .294) vanishes because the divergence of the current is zero in a steady state. The other two terms correspond to the symmetric combination in Eq. ( 1.291 ).

We now consider the antisymmetric part of the integral in Eq. ( I .291 ): (1.295)

Because (1.296)

we recognize in Eq.( I .295) the familiar expression for the vector potential from a magnetic dipole m A~I) (ii) = 1TI, X ii R3 , ( 1.297)

where the magnetic dipole moment is defined as ( I .298)

(d) Finally, we tum to the second-order terms in the muJtipole expansion of the vector potential ( I .288) that will yield us the anapole moment: ( 1.299)

Show that all symmetric terms in Eq. ( I .299) vanish.

Solution The integrand in Eq. ( 1.299) is a third-order tensor (i.e., a tensor resulting from combining three vectors) that can generally be decomposed into irreducible ten- sors of ranks 3, 2, I , and 0, the first being totally symmetric with respect to the

THE ANAPOLE MOMENT (T)

components of the constituent vectors and the last being completely antisymmet- ric. 23 We now use a trick similar to that used in Eq. ( J .294) to show that the symmetric part of the tensor integrates to zero: 0 = J Vm(rirkrdm)d 3r = J (tSmiTkTdm + ritSmkTdm + TirktSmdm)d 3r = J (rkrdi + rirdk + rirk}1)d3r.

(J.300)

The remaining parts of the tensor in the integrand of Eq.( J .299) are antisymmetric rank-two tensors and rank-one tensors (i.e., vectors). 24 (e) Show that the antisymmetric rank-two part of the second order tenn in the vector potential expansion violates T-invariance.

Solution Note that aJJ of the remaining parts of the tensor in the integrand of ~q.( l .29~)

change sign under both spatial inversion (transforming r --+ -rand j --+ - j)

and time reversal (transforming r --+ rand J --+ -]).

By the Wigner-Eckart the- orem (Appendix F), any second-rank tensor characteristic of the system (in this case, nucleus) with total angular momentum I has to be proportional to the onlX irreducible second-rank tensor that can be constructed out of the components of/: (J.301)

which is even under both spatial inversion and time reversal. Therefore, the exis- tence of the second-rank moment (called the magnetic quadrupole moment) would violate both parity (P) and time-reversal (T) invariance. In this problem, we restrict ourselves to T-conserving moments and wilJ not further consider the magnetic quadrupole.

23 In order to see that the irreducible rank-three tensor is symmetric, it is possible to think of each of the constituent vectors (each described by three independent coordinates) as spin-one objects, and the irreducible rank-three tensor as a spin-three object. It is clear that to get a spin-three by combining three spin-ones, it is necessary to construct a totally symmetric wavefunction. For rank-zero, the only scalar that can be built out of the three vectors v1-a is their mixed product v1 · (v2 x va) = (vt)i(v2)

1(va)kfiJk, where fiJk is the totally antisymmetric (Levi-Civita) tensor. With two of the constituent vectors being the same, the rank-zero term vanishes.

24 A general third-order tensor (27 independent components) is decomposed into one irreducible rank-three tensor (7 components), two irreducible rank-two tensors (2 x 5 components), three vectors (3 x 3 components), and a scalar ( one component; see, for example, Varshalovich et al. ( 1988), Chapter 3.2.2); however in the present case the number of possible tensors is reduced because two of the constituent vectors are the same and only structures symmetric in the corresponding components are allowed.

ATOMIC STRUCfURE (f) Show that the remaining rank-one tensor in the second-order term of the vector potential expansion is a vector proportional to r 2 J.

Solution Let us now tum to the vectors that can be constructed out of TiTk)L· The only possibilities are: r 2J and r(r • J). It turns out that integrals over these two vectors are not independent. To see this, note that there is no summation over indices in Eq. ( 1.300), so the identity is valid for any set of components. If so, it is also true for sums of such components. In particular, the sum ( called the contraction of the tensor over two indices) gives Thus, it is sufficient to only consider the r 2 J structure.

(g) Using the above results, prove that the second order term in the expansion of the vector potential is given by (1.303)

where Vp is a dual vector for the antisymmetric second-order tensor Jkri - Jirk (see, for example, Arfken (1985), Chapter 3.4): (1.304)

This form explicitly accounts for the antisymmetry. The explicit expression of the components of V is found by contracting both sides of Eq. ( 1.304) with Ekiq and taking into account that ( 1.305)

( 1.306)

Solution Let us return to Eq. ( 1.299) and transform it taking into account Eq. ( 1.300) and the fact that the tensor (v'k V,-k) is symmetric in indices k and l. First, from Eq.

THE ANAPOLE MOMENT (T)

( 1.300) we have: ( J .307)

Substituting this into Eq. ( 1.299), we have: ( 1.308)

where in the last expression the symmetry of (Vk "v1 k) is used. One can combine Eqs. ( 1.299) and ( 1.308) (by adding ( 1.299) and ( 1.308) divided by two) to obtain a combination in the integrand that is antisymmetric in indices i and k: ( 1.309)

Using Eq. ( 1.304) in Eq. ( 1.309), we obtain the desired result: ( 1.3 J 0)

(h) The term .J;2> ( R) corresponds to the vector potential due to the anapole moment. Use Eq. ( 1.310) to prove Eq. ( 1.287).

Solution In order to complete the expansion of the integrand into irreducible structures, we can split the tensor Vpr, into its symmetric and antisymmetric parts. The symmetric

## part is a tensor of rank two and corresponds to the magnetic quadrupole moment

As we have discussed above, this moment violates time-reversal invariance and we do not consider it in this problem. We now tum to the antisymmetric part of Vpr, which we write, in analogy with Eq. ( 1.304 ), as 2(Vpr1 - Vtrp) = 2fptqWq, (l.311)

Substituting this into Eq. ( 1.310), and using the identity (l.312)

## ATOMIC STRUCTURE

we write (1.313)

We see that we have reduced the expression for the vector potential to the f onn that depends only on a single vector characteristic of the system, the integral of W. It is clear that it must be proportional to the anapole moment ( J .286). In order to see this explicitly, we use Eq. ( J .306) and its analog for the components of W and write: j ~d 3r = ~fpli J (Vpr, - Vtrp)d3r = ¾fpli J [Ekqp(jkrq - }qrk)r, - Ekql{jkrq - }qrk)rpJd3r ( 1.314)

where once again we have used the identity (1.312). The expression (1.314) can be simplified with the help of Eq. ( 1.302): (1.315)

where in the latter equality we have substituted the definition ( 1.286).

We are now ready to substitute the result ( 1.315) into the expression for the vector potential ( 1.313): (1.316)

The first term in Eq. ( 1.316) contains (1.317)

The last equality is just the statement of the Laplace equation for the scalar poten- tial of a point charge. Let us now discuss the second term in Eq. ( 1.316). It is proportional to ( vkv, ~}5ilak = vi(a-V ~), ( 1.318)

i.e., a gradient of a scalar function. Recall, however, that the vector potential is not unique: it is defined up to a gradient of an arbitrary scalar function; addition of such a function is called gauge transformation [see, for example, Landau and

THE ANAPOLE MOMENT (T)

Lifshitz ( 1987)]. 25 In fact, our starting point, Eq. ( 1.288), is written in a particular Coulomb gauge for which V • A = 0.

Skipping the second term in Eq. ( 1.316) because it can be eliminated by a gauge transformation and employing Eq. ( 1.317), we obtain the sought-for Eq. ( 1.287).

25 This is because the observables are fields rather than potentials. To find the magnetic field, we take the curl of A. Because the curl of a gradient is zero, the field is invariant with respect to a gauge transformation.

## ATOMS IN EXTERNAL FIELDS

## 2.1 Electric polarizability of the hydrogen ground state

This is a classic problem concerning a hydrogen atom in the ground state immersed a uniform electric field l. To second order in the electric field, the shift of the ground-state energy is (2.1)

where o is the polarizability.

Estimate the polarizability o for the hydrogen ground state. For the purposes of this estimate, one may neglect the fine (Problem I .3) and hyperfine (Problem 1.4)

structure, i.e., ignore effects associated with the electron spin. Compare this result to the polarizability of a classical conducting sphere of radius ao.

Measurements of electric polarizabilities have been used extensively to eluci- date atomic and molecular structure since they are sensitive probes of the electronic wavefunctions far from the nucleus.

Hint For an estimate of the polarizability, we can say that Ef) - E~o) ~ EI ) - E~ 0l, where Et> are the unperturbed hydrogen energies.

Solution The Hamiltonian describing this system is given by H= Ho+H1, where p2 e2 Ho=---2m r (2.2)

(2.3)

## ATOMS IN EXTERNAL FIELDS

is the Hamiltonian for a free hydrogen atom, and H1 is the perturbing Hamilto- nian due to the appJied electric field. Orienting the quantization axis (z) along the electric field gives H1 = -l- l = e£z = e£rcos8.

(2.4)

Since H 1 only connects states of opposite parity, there is no first-order shiF't (~E(I)), ~Ej 1) = (1, 0, 0IHi/1, 0, 0) = 0, (2.5)

where In, l, m) denotes the unperturbed state with principal quantum number n't orbital angular momentum quantum number l, and projection of orbital angular momentum along the z-axis mli. Therefore we must use second-order perturbation theory, where the energy shifts are given by 1 LlEf) = L n,l,m=,61,0,0 l(n, l, mlH1 II, 0, 0)/2 EiO) - EAO)

(2.6)

Therefore, based on Eqs. (2. I) and (2.6), the polarizability a can be found from / (n, l, m/H1 /1, 0, 0) /2 E[°) - E~o)

(2.7)

Using the approximation suggested in the hint, namely that Ef 0> - E~o) ~ E}°) _ (0)

E 2 , we have ~ 2a£ ~ (0)

(0) ~ /(n,l,m/H1/l,0,0)/ , E2 - E1 n,l,m (2.8)

where (in order to make later use of the completeness relation) we have included in the sum the n = 1, l = 0, m = 0 state, allowed since, as noted in Eq. (2.5), (1, 0, 0IH1/l, 0, 0) = 0. Now consider the sum L /(n,l,m/Hi/1,0,0)/ 2 = (l,0,0/H1 (L /n,l,m)(n,l,m/)H1/1,0,0)

n,l,m n,l,m = (1, 0, 0/H;/1, 0, 0) , (2.9)

.

1 Although the electric dipole selection rules for a z-oriented electric field (~l = ± 1, ~m = 0)

imply that many terms in the sum (2.6) are zero, we keep them in order to make explicit use of the completeness relation later in the calculation.

ELECTRIC POLARIZABILITY OF THE HYDROGEN GROUND STATE where we have made use of the completeness relation ,E /n, l, m)(n, l, m/ = 1 .

(2. 10)

n.l.m Based on Eqs. (2.8) and (2.9), we have 1 " 2 (l,0,0/Hf/1,0,0)

-oc.

:::::: (0)

{O)

.

E2 - El (2. I J)

The ground state wavefunction for hydrogen is .,/, ( ) _ _ -r/ao 'PIOO r - r= 3/2 e ' v1ra 0 (2. J 2)

so the matrix element in (2.1 I) is given by the integral The difference in energy between the ground and first excited states of hydrogen is Et> - E(O) = -~ (~ - 1)

= 3e2 .

2a0 Bao (2.14)

Employing Eqs. (2. J 3) and (2. I 4) in (2. J J ), we find an estimate for the polariz- ability of the ground state of hydrogen: o ~ -a3 ~ 0. 79 x 10- 24 cm3 • (2. I 5)

Because of the approximation made in Eq. (2.8), this is in fact an upper limit on the polarizability of the hydrogen ground state. It turns out that this is close to the exact value [see, for example, Bethe and SaJpeter (J 977)]: - a = -a3 ~ 0.67 x 10 24 cm3 .

(2. I 6)

It is also interesting to compare a to the polarizability of a classical conducting sphere of radius a0• The electric dipole moment i of the sphere is related to the

## ATOMS IN EXTERNAL AELDS

applied electric field f. by the poJarizabiJity 2 i=al.

(2. J 7)

The electrons on the conductor wiJJ arrange themselves so that the electric field on the sphere is perpendicular to the surf ace ( otherwise there would be a tangential force on the free charges). Outside the sphere, we can assume that t~e field due to the conductor is a dipole field. 3 The electric field f.d from a dipole d is (2.18)

At the surface of the sphere (r = a0) the component of l + ld not along f must vanish, so, for example, on the equator of the sphere (where J. f = 0) we have (2.19)

Thus the poJarizability of a classical conducting sphere is (2.20)

## 2.2 Polarizabilities for highly excited atomic states

Discuss the general scaling of electric polarizabilities with the principal quantum number n (for highly excited states).

Solution In the presence of an external electric field, an atomic energy level k shifts according to (2.21)

2 The connection between Eq. (2.17) and (2. I) follows from E=- d·de =- aede =--a:e .

Lr. - -, Lr. , , 3 This_ can be guessed from the high symmetry of the configuration: the conductor is spherically symmet,:ic and t~ electric field has only a direction. This guess indeed satisfies Poisson's equation, so by umqueness 1t must be the correct solution [see, for example, Jackson ( 1975)].

USING STARK SHIFTS 10 MEASURE ELECTRIC FIELDS where the sum is taken over all states i coupled to k by the electric dipole operator d, and the dipole matrix element dik (with quantization axis z) is given by dik = (ifdfk) = -(ifezfk) = -(ifercos8lk).

(2.22)

One can expect that the sum (2.21) is dominated by tenns corresponding to levels with close values of the principal quantum number n: ni ~ nk, since for these levels the energy denominators are smallest and dipole matrix elements are large because of good overlap between wavefunctions. The dipole matrix elements scale as the radius of the electron's orbits which go as n 2• This can be seen by comparing the expectation value of the energy determined by the virial theorem [Eq. ( 1.79)]: e 2 /1)

(En) = -2 \ ;:- , (2.23)

with the Bohr formula [Eq. ( J. J )]

(2.24)

fhe scaling of the energy denominators can be estimated from the fact that En <X 11,- 2, so the density of states that can couple to a given state goes as ( dEn/ dn )- 1 ex 11,3• Note that the number of states i relevant to this problem is smaller than the overall number of states with different values of quantum numbers n, l and m (which has an additional factor ex: n 2). This is because an electric field along i can only couple levels with the same value of m, and with values of l that differ by ;tl.

Combining the scaling factors (dik <X n 2 and Ei - Ek ex n- 3) in Eq. (2.21), we find that polarizabilities a of highly-excited states scale as I a ex n 7 ' I (2.25)

which is confirmed by more elaborate calculations [see, for example, Bethe and Salpeter ( J 977)].

2.3 Using Stark shifts to measure electric fields Suppose that one is measuring electric field strength by detennining the quadratic Stark shift of a given atomic energy level. Suppose that the Stark shift ~E can be measured to an absolute certainty 6dE which is independent of the field value, and corresponds to 6dE = 10-4 fdEf for an electric field of e = 10 kV/cm.

(2.26)

## ATOMS IN EXTERNAL FIELDS

(a) For a field value e ~ 10 kV/cm, what is the uncertainty t5e in the determination of e?

(b) What is the smaJJest field f,* that can be measured given this sensitivity 6~E to Stark shifts?

Solution (a) To lowest order, the Stark shift is proportional to the square of the electric field (Problem 2. I)

(2.27)

and we are given that the sensitivity to Stark shifts is <5~E = 10- 4 - l~E(e = 10 kV /cm)I.

(2.28)

From Eq. (2.27), the relationship between the uncertainty in the determination of e and the sensitivity to the Stark shift is: (2.29)

so we have (2.30)

Thus the uncertainty in the determination of the JO kV /cm field is: (2.3 J)

(~) Since t~e sensitivity to the Stark shifts is an absolute sensitivity (does not vary with electnc field), we have for any electric field e*: 6/lE = 10_4 • (10 kV /cm) 2 tiE(e*)

(e•)2 · (2.32)

The smallest detectable field is when t5tiE//tiE/ ~ 1. This occurs when: l e* = 100 V /cm . /

LARMOR PRECESSION FREQUENCIES FOR ALKALI ATOMS Why is the smallest detectable field e • so much larger than the uncertainty in determination of a larger field? The basic idea is that if we have a small field e' in addition to a larger field £0 , the Stark shift is given by t::..E = - ; (Co+ C') 2 ~ - ; (Cl+ 2C0C').

(2.33)

We see that the effect of the small field is enhanced by the presence of the larger field due to interference.

However, if all we have is the small field, the Stark shift is just (2.34)

so there is less sensitivity to the field.

Such ideas are also important in atomic experiments where small transition amplitudes are measured, e.g., parity-violation experiments where the very small tf8DSition amplitudes associated with the weak interaction (Problem 1.13) inter- fere with larger transition amplitudes arising from the electromagnetic interaction, allowing the parity-violating effects to be detected.

z.,4 Lar1nor precession frequencies for alkali atoms calculate the Lande factors for 2S1; 2 atomic states [for example, the ground elec- tronic states of hydrogen, alkali atoms, and elements of the I B group of the periodic table (copper, silver, gold)]. Include the effect of the nuclear spin /, b~t ignore the interaction of the nuclear magnetic moment with the external magnetic field. Give qualitative explanations of the relative sign of the Lande factors for states with total angular momentum F = I ± 1 /2, and the relative magnitudes of the Larmor frequencies for atoms with different values of/.

Solution The shift in the energy of an atomic level due to interaction of an external magnetic field with the magnetic moments due to the orbital angular momentum and the spin of the electron is given by: ~E = -jl-B.

(2.35)

Ignoring the effect of the nuclear magnetic moment, the magnetic moment of a particular atomic state is given by j1 = -µo(YLl, + gsS) , (2.36)

where 9L = 1 and gs~ 2 are the appropriate Lande factors. The magnetic moment can be related to the total angular momentum of the state J = i + § in the

## ATOMS IN EXTERNAL FIELDS

following way: (2.37)

from which it follows that _ ( (8- J) rt)

(µ) = -µo (J) + J(J + l) (Ji · (2.38)

Here - (8- J) rt (S) = J(J + 1) (J1 (2.39)

gives the mean value of 8 along J times a unit vector co-directed with J [this relation follows, for example, from the Wigner-Eckart theorem, see Appendix F].

Now we are able to solve for (8 • J) in terms of a set of eigenvalues of the system.

Employing the relations we find that i=f-8, L 2 = J2 + s2 - 28. J' (8 ·J) = J(J+l)+S(S+l)-L(L+l).

(2.40)

(2.41)

(2.42)

The relation between the magnetic moment of the system and the total angular momentum (2.38) thus becomes: (2.43)

where _ 1 J(J + 1) + S(S + 1) - L(L + 1)

gJ - + 2J(J + 1)

.

(2.44)

Accounting for the effect of the nucleus ~uires including the nuclear spin f ....

.... ....

in the total angular momentum F = I + J, while the interaction Hamiltonian remains the same since here we neglect the nuclear magnetic moment since it is considerably smaller than the Bohr magneton. The g-factor is therefore altered by

LARMOR PRECESSION FREQUENCIES FOR ALKALI ATOMS the projection of J along F. The calculation is similar to those above: (2.45)

where _ [F(F + 1) + J(J + 1) - I(I + 1)]

(2.46)

gF-gJ 2F(F+l)

.

For 2S 1; 2 states S = 1/2, L = 0, J = 1/2, and 9J = 2. The total angular momentum in this case can be F =I± 1/2. The Lande factor is given by F(F + 1) + 3/4 - I(I + 1)

YF = F(F + 1)

.

(2.47)

For F =I+ 1/2 we get: F(F + 1) + 3/4 - (F - 1/2)(F + 1/2)

gF = F(F+ 1)

(2.48)

F+ 1 - ---- F(F + 1)

F I+ 1/2 ' and for F = I - 1/2 we get: F(F + 1) + 3/4 - (F + 1/2)(F + 3/2)

gF = F(F+ 1)

(2.49)

-F -l ---------- - F(F + 1) - F + 1 - I+ l/2 .

Thus the Lande factors for 2S1; 2 atomic states are given by: I 9F = ±21: 1 · I (2.50)

The relative signs of the Lande factors and the magnitudes of the Larmor fre- quencies can be understood as follows. The torque r acting on the atom is almost entirely due to the magnetic moment of the electron, so - dF - B- T= dt ~ µe X .

(2.51)

Thus the Lande factor is a result of the relationship between the electronic angular momentum (responsible for Pe) and the total angular momentum F. As seen from Fig. 2. I, when F = I + l/2, the electronic angular momentum points in the

## ATOMS IN EXTERNAL FIELDS

~ ' J I F = I J F = l-J FIG. 2.1 Illustration of the relative orientation of J to the total angular momentum F for F = I± J.

direction of the total angular momentum, so the g-factor is positive. However, when F = I - I /2, the electronic angular momentum is directed oppositely to the total angular momentum and the g-factor is negative. Equation (2.51) also shows that the magnitude of the Larmor frequency, OL = gFµoB, must decrease as I grows because F increases while µe remains unaffected - so more angular momentum must be "dragged" around by the given torque.

## 2.5 Magnetic field inside a magnetized sphere

Consider a uniformly magnetized spherical ball of radius R. Imagine a sphere of radius r < R inside it. What is the magnetic field "seen" by the small sphere? This problem is relevant to optical pumping magnetometers utilizing magnetic reso- nance in oriented atoms contained in a vapor cell [see, for example, (Alexandrov et al. 1996)).

Solution First, we recall that the magnetic field inside a uniformly magnetized sphere is given by [see, for example, (Griffiths 1999)]: B- 81rM A = 3 z' (2.52)

where z is the direction of the magnetization.

The important point is that the magnetic field is unifonn and independent of the radius of the sphere.

## CLASSICAL MODEL OF MAGNETIC RESONANCE

Therefore, the field inside a small imaginary sphere within the large sphere is in this sense entirely "due to itself." Carving out a spherical cavity inside the sphere (by superimposing a sphere of opposite magnetization), one would see that the field inside the cavity is zero.

Therefore, the magnetic field which the imaginary sphere sees is: B(s1nall sphere) = 0.

(2.53)

This is good for optical pumping magnetometers because it allows them to sample the field due to external sources rather than the field produced by the atoms when they are polarized. (Note that this result does not hold for nonspherical cells or when contact interactions between atoms are taken into account.)

## 2.6 Classical model of magnetic resonance

In this problem, we consider the important phenomenon of magnetic resonance, which is a technique widely used in physics, chemistry, biology, and medicine.

The underlying principles of magnetic resonance can be used to explain, in gen- eral, the effects of periodic perturbations on atomic states. Many of the concepts discussed here will be used in subsequent problems. Note that the arguments used in this problem are purely classical - they do not rely on concepts from quantum mechanics (but are nevertheless, with a few minor modifications, applicable to quantum systems).

(a) Consider a particle with magnetic moment µ = ,J, where , is the gyro- magnetic ratio and j is the total angular momentum of the particle. Show that µ precesses around a static magnetic field Bo with the Larmor frequency f2L = ,Bo.

Assume that the field Bo is "suddenly" turned on [i.e., the magnetic field is turned on nonadiabatically - this will be discussed in more detail in part (d)].

(b) Now consider this precession in a frame rotating with respect to the "labora- tory" with an angular velocity w. Show that, in the rotating frame, the mag_!letic dipole precesses as if there were an additional, "fictitious" magnetic field Bf = w/,.

(c) Next we tum on an additional magnetic field B.1.(t) which rotates in the plane orthogonal to Bo (again this is done nonadiabatically). Choosing the z direction along Bo, we may say that (2.54)

## ATOMS IN EXTERNAL FIELDS

By going into a frame rotating so that B 1. ( t) appears to be stationary, find the time dependence of the projection of Jon the z-axis, Jz(t). Note the resonance occurring when w = nL.

(d) Consider an ensemble of particles whose magnetic momentsµ = ,J are ori- ented oppositely to B0• Suppose one wants to flip the orientation of the dipoles so that they point along B0• One way to accomplish this is to use the techniques of magnetic resonance considered in parts (a)-(c) of this problem. In order to flip the maximum number of magnetic moments, one must fine-tune the duration T and strength of B.1.(t) in order to produce what is known as a 1r-pulse (where ,B.1.r = 1r for w = flL)- This technique becomes less efficient in the presence of magnetic-field gradients - i.e., if not all of the particles in the ensemble see the same leading field.

There is a more robust method that relies on the concept of adiabatic passage.

Suppose that instead of suddenly turning on the field B.1(t), we start with B.1.(t)

rotating at a frequency w << nL, and then slowly sweep the frequency through resonance until we have w >> nL. 4 Explain how this method flips the magnetic dipoles and under what conditions it works.

Solution (a) The magnetic field Bo exerts a torque r on the magnetic dipole r = µ x Bo = 1 J x Bo which causes the angular momentum to change in time according to d]

- - dt = ,J x Bo.

(2.55)

(2.56)

Let us suppose that Bo is along z, and that J is at an angle (J with respect to Bo (see Fig. 2.2). Then, according to Eq. (2.56), the change of Jin a time dt is d] = 1 J Bo sin (J dt eq, , (2.57)

where the unit vector eq, points in a direction orthogonal to the plane containing - - - Bo and J, and J = IJI. We also have (Fig. 2.2)

(2.58)

4 Actually, this method works equally well if one starts with w >> {h and sweeps the field to w « {h. or if one sweeps {lL by changing Bo.

## CLASSICAL MODEL OF MAGNETIC RESONANCE

The ref ore, from Eqs. (2.57) and (2.58), we find that J and 11 precess around Bo at the frequency (2.59)

(b) The evolution of a vector v in the lab frame is related to its evolution in a frame rotating with angular velocity w according to the classical formula [see, for example, Marion and Thornton (1995)]: dvl dvl _ _ - =- +wxv.

dt lab dt rotating (2.60)

In the lab frame, we know that J evolves according to Eq. (2.56), so using Eq. (2.60), we find that in the rotating frame d]I = ,J x [Bo + ~] .

dt rotating (2.61)

If we compare Eq. (2.61) to Eq. (2.56), we see ~hat in the rot~ting f_!ame, the apparent magnetic field acting on the dipole is not Bo but rather Bo + Bf, where def> FIG. 2.2 The torque on a magnetic dipole ji, = ,J due to a static magnetic field Bo leads to precession of the magnetic dipole (see text).

Lab Frame

## ATOMS IN EXTERNAL FIELDS

I I +ro Rotating Frame FIG. 2.3 Magnetic fields in the lab frame and a frame rotating with B .L ( t) • BI is a "fictitious" field given by Note that if we choose w = - 1 Bo, the dipole appears to be stationary.

(2.62)

( c) If we go into a frame which rotates so that R .1 appears to be stationary, as we have seen in part (b), the apparent magnetic field in the z-direction has magnitude Bo - w / 1 (Fig. 2.3). Thus in the rotating frame, the dipole "sees" an effective static magnetic field Reff with magnitude Beff = ✓ Bl + ( Bo - ~)

.

(2.63)

The angle 'P between Reff and the z-axis is found from (2.64)

The dipole ji, precesses about Reff at a frequency (2.65)

As can be see~ from the diagram in Fig. 2.4, the amplitude of the change in the projection of J on the z-axis is given by (2.66)

## CLASSICAL MODEL OF MAGNETIC RESONANCE

z l -------- 2~J~ ..

1 ·------ FIG. 2.4 Precession about the effective magnetic field in the rotating frame.

Thus (after a few trigonometric substitutions and some algebra) the overall time- dependence of Jz is found to be (2.67)

where n is given by Eq. (2.65) and sin2 c.p is given by Eq. (2.66).

We can see from Eqs. (2.66) and (2.65) that when w = nL, sin2 cp = 1 and n = ,B.1. According to Eq. (2.67), this means that Jz oscillates between ±J at frequency n. This is because when B.1 rotates at nL, in the rotating frame it appears that there is no field along z, so the dipole precesses about B .1 at the appropriate Larmor frequency , B .l · This is the essence of magnetic resonance.

(d) Once again, let us work in a frame co-rotating with B.1(t). In this frame, the magnetic dipoles see an effective field Reff with magnitude given by Eq. (2.63)

pointing at an angle c.p [given by Eq. (2.64)] from the direction of Bo (see Fig. 2.3).

If one slowly sweeps the frequency w, the magnetic dipoles adiabatically follow the effective magnetic field. The effective magnetic field, sketched as a function of time in Fig. 2.5, rotates from pointing in the direction of Bo to pointing opposite ~ to Bo. This tells us that the procedure flips all the spins.

What are the conditions necessary to ensure adiabaticity?

## ATOMS IN EXTERNAL FIELDS

t 'y i .

······► ~ B.l.

Time (1)<<0 • ·····► • (t)>>!l FIG. 2.S Effective magnetic field in the rotating frame as the frequency of the transverse field is swept through resonance.

Qualitatively, the spins must precess about Beff many times during the time interval over which there is a significant change in the field, i.e.

1 aBeff ,Beff >> ~ 8t .

Beff (2.68)

Assuming a constant sweep rate of the frequency w, the adiabatic condition is satisfied as long as (2.69)

2.7 Energy level shifts due to oscillating fields (T)

In this tutorial we analyze the shift of atomic energy levels due to an electric field which varies in time, known as the AC Stark effect. The AC Stark effect is an invaluable tool for laser trapping and cooling and is a basic mechanism behind many nonlinear optical effects.

We will also see that the case of a time-varying magnetic field (AC Zeeman effect) is completely analogous to the AC Stark effect when there is a strong, static leading field Bo and a weak, oscillating field transverse to Bo applied to an atomic system.5 5 There is a fundamental difference between the Zeeman and Stark effects in that magnetic fields lead to first-order energy shifts while electric fields cause shifts only in second order. However, in the presence of a strong leading magnetic field, additional weak transverse fields only lead to second-order energy shifts, making this case fully analogous to the Stark effect.

ENERGY LEVEL SHIFfS DUE TO OSCILLATING FIELDS (T)

Consider an atom with two states la) and lb) separated in energy by wo (in this problem we use units where Ii = 1). The states are coupled by the electric dipole operator d and a sinusoidally varying electric field e0 sin Wm t is applied to the atom. Throughout this problem, we neglect the linewidths of the energy levels, i.e., the relaxation rate r for the states is much less than all other relevant frequencies in the problem ( lwo - Wm I, Wm, w0). The amplitude eo of the applied field is sufficiently small so that the effect of the electric field may be treated as a weak perturbation, i.e., deo << lwo - wml, Wm, wo.

Also note that this discussion is closely related to Problem 3.1, which deals with transitions between states of a two-level system induced by a periodic perturbation.

(a) If the modulation of the field is slow compared to the transition frequency (wm << wo), show that the average shifts of the energy levels are given by ~E ';::j ± d2ei ' (2.70)

2w0 where the plus and minus signs refer to the upper and lower states, respectively.

Sketch the energy spectrum for the case when wm << d2e5/wo and the case when Wm>> d2e5/wo.

Hint To describe the energy spectrum, it is useful to consider how the energy difference between the states leads to a time-dependent quantum-mechanical phase. Here, the atomic states can be seen as oscillators whose frequencies are being modulated by the Stark effect. The spectrum is also analogous to that of frequency-modulated light (see Problem 8.3).

The energy spectrum can then be described in terms of sidebands whose rela- tive amplitudes are given by the Bessel functions Jn(a), where o is the modulation index, using the formula [see, for example, Artlcen ( 1985) or Siegman ( 1986)]: eiosinO = L Jn(a)einO .

(2.71)

n=-oo Solution When the field is varying with Wm << w0, for short times, the electric field is effectively DC. Thus the time-dependent energy-level shifts are simply given by the DC-Stark shift formula (2.21 ): (2.72)

## ATOMS IN EXTERNAL FIELDS

(I.) >>.0 I rot0.12-2 %+ 012 roJ-012 + 2c.o,,.

(i) <<fl FIG. 2.6 Energy spectrum for the upper state of a two-level system subjected to an oscillating electric field. Note that the vertical scale for the two plots is not the same (the amplitudes of the sidebands in the lower plot are actually much smaller than pictured relative to those in the upper plot).

where we employ a time-dependent field (with a particular choice of phase) in place of a static field and the plus and minus signs refer to the upper and lower states, respectively. The average values of the shifts are thus given by Eq. (2.70)

ENERGY LEVEL SHIFfS DUE TO OSCILLATING FIELDS (T)

According to Eq. (2.72), the instantaneous energy w(t) of, for example, state lb) is given by w(t) = wo + ~E(t)

= wo + Osin 2 wmt n n =wo+---cos2w t m ' (2.73)

(2.74)

(2.75)

where n = d2e5/wo. The phase cp(t) acquired by state lb) in its time evolution is obtained through integration: <p(t) = l w(t')dt' = ( wo + ~)t - ( :J sin2wmt.

(2.76)

The time-dependent state l'l/Jb(t)) = e-icp(t) lb) can be described using formula (2.71 ): (2.77)

Thus we see that the energy spectrum is given by a set of sidebands centered around wo+0/2 and spaced by frequency intervals of2wm. The statistical weight of each energy sideband is given by the square of the Bessel functions Jn (a) where the modulation index is a = 0/4wm.

The character of this spectrum is discussed in Problem 8.3. For Wm << n, the modulation index is large. This corresponds to a slow sweep of the frequency, generating the spectrum shown in the lower plot of Fig. 2.6. For Wm >> n, the spec- trum is dominated by a single strong line at w0 + 0/2 - the next most prominent sidebands occur at ±2wm about the central frequency [upper plot in Fig. 2.6].

(b) In the near-resonant case (wm ~ w0), a relatively straightforward way to find the average AC Stark shift is by making a unitary transformation using the operator u u = (1 ~ )

Q e-1.Wmt ' so that the Hamiltonian for the system becomes H' = utHu (2.78)

(2.79)

6 By statistical weight we mean the following. Suppose we initially put an atom in one of the states, subject to the oscillating electric field, and then measure its energy with, for example, a probe field. The statistical weight gives us the probability that we measure the state to have a particular energy.

## ATOMS IN EXTERNAL FIELDS

and the states are transfonned according to (2.80)

The unitary transformation modifies the time-dependent Schrodinger equation in the following way (recall that we have set 1i = 1 ): 7 ( H' - iUt ~)

IV''} = i ! IV''} , (2.81)

so we say that the "effective Hamiltonian" H in the new basis is given by - t tau H = U HU - iU 8t .

(2.82)

It turns out that this transf onnation is mathematically equivalent to going into the rotating frame (as done for the case of a magnetic moment in a magnetic field in Problem 2.6). The next step is to apply the rotating wave approximation (in which all fast oscillating terms in the Hamiltonian are eliminated). Note that the term -iUt 9Jf-in the effective Hamiltonian accounts for the fact that the "rotating frame" is noninertial, causing the energy difference between the levels to become wo - Wm (see Problem 2.6).8 Find the AC Stark shifts in this regime.

7 Equation (2.81) can be derived starting from the usual time-dependent SchrHdinger equation: Hl1/J) = i ! 11/J)

, then multiplying both sides by ut and inserting the identity operator uut in appropriate locations: ut Huut11P> = iUt :t uut11P> , H'l1P') = iUt ! Vl,t,') ' H'l,t,') = iUt [ ( ~)

11/J')

+ U ! 11/J')] .

Here we have made use of Eqs. (2.79) and (2.80), and the above result directly yields Eq. (2.81 ).

8 "Going into the rotating frame" and making the ·•rotating wave approximation" are nothing but straightforward mathematical transformations. The geometric interpretation of the mathemat- ics is sensible in the case of magnetic resonance (Problem 2.6); however, in many cases where one wants to make the same mathematical transformation, it is impossible to use this geometric language. Nonetheless, because of the close mathematical analogy between such situations and magnetic resonance, the terminology is applied universally.

ENERGY LEVEL SHIFTS DUE TO OSCILLATING FIELDS (T)

Solution The Hamiltonian for the system is H=( 0 -deo sin Wm t -deo sin w11.,,t)

WQ ' (2.83)

and in the "rotating frame" we have for the effective Hamiltonian [Eq. (2.82)]

ii= utHu -wt 8u at = ( d~u (1 ~ e2iw,..t)

(2.84)

(2.85)

We see that the Hamiltonian consists of two components, one static and one rapidly rotating that is effectively averaged out (in the rotating wave approxima- tion, this rapidly rotating component is ignored), thus we have - ( 0 H ~ df.o 2i _ df.o )

2i wo-Wm (2.86)

In the rotating frame, we appear to have a DC Stark shift of two levels separated in energy by wo-wm caused by an electric field with magnitude eo/2.9 According to Eq. (2.21 ), the AC Stark shifts in this regime are given by (2.87)

where again the"+" corresponds to the upper state and the"-"

corresponds to the lower state.

(c) As mentioned earlier, there is a direct analogy between the AC Stark shift and the AC Zeeman shift. Consider a ~in- I /2 system ( e.g., an electron) subjected to a strong, leading magnetic field Bo = Boz, splitting the Zeeman sublevels by wo = gµoBo (where g is the appropriate Lande factor, for an electron 9e ~ 2). A weak, oscillatory transverse field (2.88)

is applied to the atom. Here µ 0B .1 is analogous to de0 for an electric field.

9 In Eq. (2.86), the overall factor of i (compared to the usual Hamiltonian for the DC Stark effect)

is merely a phase arising because the oscillating field is chosen to be proportional to sin(wmt) as opposed to cos( Wm t), and does not affect the energy eigenvalues for the system.

## ATOMS IN EXTERNAL FIELDS

Assuming that µ0B1. << lwo - wml (weak field limit), solve for the average energy level shifts due to the transverse field by going into a frame rotating at Wm in the same sense as the Larmor precession due to Bo and applying the rotating wave approximation. In order to describe the evolution of angular momentum in such a rotating frame, it may be convenient to introduce an additional, fictitious field (Problem 2.6)

(2.89)

which accounts for the effects of rotation.

Solution The oscillating, transverse magnetic field (2.88) can be written as a sum of two counter-rotating magnetic fields: B.1(t) = ~.l (sinwmtx + coswmtY) + ~.l (sinwmtX - coswmtY) • (2.90)

The Hamiltonian describing the interaction of Bl. ( t) with the atom is (2.91)

and we can write the magnetic moment (we will assume we are dealing with an electron so that g ~ 2) in terms of the Pauli matrices - f ( 0 1 ) A ( 0 -i ) A ( 1 0 ) A]

µ = -µo l 1 0 x + O Y + z ' (2.92)

where we are using the spinor representation in which lb)= I+) = ( ~ ) , (2.93)

la)= H = u) · (2.94)

Employing Eqs. (2.90) and (2.92) in Eq. (2.91 ), with a bit of algebra we find µo B .l f ( -ieiw,,. t )

( i e- iw.,, t ) ]

(2. 95)

H.1 = 2 l ie-iw,..t O + -ieiw..,t O .

Now we go into a frame rotating at Wm• This transformation. h~ two effects: (I)

it causes one rotating component of the transverse field to lose its tm~e d~pen~e~ce and appear to be a static field while the other component rotates at twice its ongmal

ENERGY LEVEL SHIFTS DUE TO OSCILLATING FIELDS (T)

frequency, and (2) it affects the perceived evolution of angular momentum - to account for this effect we introduce the fictitious magnetic field from Eq. (2.89)

(see Problem 2.6). In the rotating frame, our perturbing Hamiltonian now looks like H(rot) = iµoB.1 [( 0 -1 ) + ( _O e-i2w,,,t )]

, .l -ei2w,,, t (2.96)

while the Hamiltonian due to the leading field and the fictitious field can be written as H (rot) = ( Wo - Wm O )

.

(2.97)

Our next step is to make the rotating wave approximation. We simply drop all of the fast oscillating terms, which eliminates the second matrix in Eq. (2.96). This leaves us with the total Hamiltonian: H (rot) ,..._, (

## WO -

Wm -iµoB.1../2 )

(2.98)

tot "' iµoB .1../2 .

The factors of ½ in the off-diagonal terms of the matrix in Eq. (2.98) are due to the fact that in making the rotating wave approximation we have "thrown away"

half of the transverse field. Solving for the eigenvalues of this matrix gives us the perturbed energies: E± = ~ ( wo - Wm ± J µ~Bi + (wo - wm)2) .

(2.99)

Now we make use of the assumption that µ0B.1.. << lwo - wml to simplify Eq. (2.99): µ2B2 E+ ~ WO - Wm + 4( O .l ) , wo-Wm E_ ~ - µ~Bi .

4(wo -wm)

(2.100)

(2.10 I)

Finally, to go back into the lab frame we eliminate the energy shift due to the fictional field (2.89), and find µ2B2 E+ ~ wo + 4( .1 ) , wo-wm (2.102)

(2.103)

## ATOMS IN EXTERNAL FIELDS

These results are identical to those obtained for the AC Stark shift if we replace µoB.1 with d£o [Eq. (2.87)): (d) We can use a somewhat more formal approach [see, for example, the text by Townes and Schawlow (1975)) to derive a general expression for the AC Stark effect which we will find useful in several future problems. In the absence of the electric field, according to the time-dependent Schrodinger equation, the states of the atom are given by l1/Ji 0> ( t)) = la) , 11/Jf\t)) = e-iwotlb) .

(2. 104)

(2.105)

In the presence of the external field, the actual atomic states, l¢a(t)) and 11/Jb(t)), are a superposition of these unperturbed states, for example 10 (2.106)

Find differential equations for the amplitudes ca(t) and cb(t).

Solution Our goal is to find differential equations for the coefficients ca ( t) and cb( t) in Eq. (2.106). The Hamiltonian for the system is H = ( -deo sinwmt )

-deo sinwmt Wo .

(2.107)

According to the time-dependent Schrodinger equation, the atomic state should evolve according to i ! l1Pb(t)) = Hl1Pb(t)) .

(2.108)

Using Eqs. (2.106) and (2.107) in Eq. (2.108), we have i!!_ ( Ca(t)_ ) = ( -deo sinwmt Cb(t)e-iwut . )

dt Cb(t)e-iwut -deo sinwmt Ca(t) + wocb(t)e-iwot ' <2-109> 10 When one employs such a representation for the atomic state, one works in what is called the interaction picture [see, for example, Griffiths ( 1995)).

ENERGY LEVEL SHIFfS DUE TO OSCILLATING FIELDS (T)

so that dca • - = ideosinw t cb(t)e-l..v,,t dt ' (2.110)

(2.1 I I)

(e) Assuming that c0 (0) ~ 0 and cb(t) ~ e-ii.p(t)

in the differential equations from part (b), one can find an integral equation for <p(t). The imaginary part of cp describes the change of the probability amplitude for the atom to be found in I b)

(i.e., it represents transitions between lb) and la)), while the real part of i.p gives an additional phase shift in the evolution of the state.

Thus the energy shift of the state is given by (recall Ii= 1 here): ~E = dt Re[<p] .

(2.112)

Use this technique to determine the general formula for the AC Stark shift, and show that it agrees with the analysis of parts (a) and (b). In order to apply first- order time-dependent perturbation theory, one can assume that I cp( t) I << 1 in this analysis.

Solution Substituting cb( t) = e-ii.p(t)

into Eq. (2.111) yields d<p · · t -e-li{)

= -deo sinwmt Ca(t)etWu • dt (2.113)

Since we assume 'P << 1, we may say that e-icp ~ 1 in the above equation and we find d'{) - d"

.

t (t) iw.,t dt - - LQSIIlWm Ca e .

(2.114)

To solve this equation, we need to determine c0 (t). Using the same approximation (e-icp ~ 1) in the differential equation for ca(t) [Eq. (2.110)) allows us to write (2.115)

## I

## ATOMS IN EXTERNAL FIELDS

This integral can be done quite readily by employing the substitution .

t' SlilWm = 2-i (2.116)

and we find that d£o [e-i(wo-Wm )t e-i(wo+w,,. )t l C (t)=- ---+ · a 2i Wm - WO Wm + WO (2.117)

Next, we substitute the expression for c0 (t) from Eq. (2.117) into (2.114), allowing us to write an integral equation for the phase <.p(t): d2e21t ) ( eiw,,.t' e-iwmt' )

'IJ(t) = __ o (eiw,,.t' _ e-iw,,.t' ___ + ___ dt'.

Wm - WO Wm + WO (2.118)

The oscillatory terms time-average to zero, and we get d2e2 [ t t ]

Re[<.p(t)] = - 4 ° + + --- .

WO Wm WO -Wm (2.119)

By differentiating the above equation [according to Eq. (2.112)), we find that the AC Stark shift is given by 11 (2.120)

Note that the sign of the AC Stark shift changes depending on the detuning. This means that, for example, light fields detuned to the low-frequency side of an atomic resonance push energy levels apart while light fields tuned to the high frequency side of a transition push them together. Such light shifts are important for laser trapping and cooling.

11 One may wonder how Eq. (2.119) can be consistent with our initial assumption that lcp(t)I << 1, since cp(t) grows linearly with time. We made the assumption lcp(t)I « 1 in order to solve the differential equations to first order - now that we have obtained a first-order solution, we can substitute Cb(t) = e-i1'.Et into the right hand side of the differential equation (2.111) to obtain a second-order solution for cp( t). It turns out that the second-order solution is equivalent to Eq. (2.119)

with wo replaced by wo + ~E. Since ~E « w0 , this change can be neglected, and we find that in fact our solution is good to all orders and so the restriction that jcp(t)I « 1 is lifted.

ENERGY LEVEL SHIFfS DUE TO OSCILLATING FIELDS (T)

IOI In the limit where Wm << w0, as in part (a), we see that (2.120) reduces to Eq. (2.70), f),_E ~ ± d22e5 ' WO while under conditions where Wm ~ w0 we get Eq. (2.87)

/),.E ~ d2£ij .

4(wo - Wm)

It is important to note again that throughout our entire treatment we have neglected the nonzero width r of the energy levels, so the above formulae are inapplicable near resonance (lwo - wml ;Sf).

When the modulation frequency greatly exceeds the transition frequency (wm >> wo): (2.121)

(f) In applying the rotating wave approximation in parts (b) and ( c) of this tutorial, we set to zero all of the fast oscillating terms in the Hamiltonian. In fact, the fast oscillating terms (arising from the "counter-rotating" component of the field) lead to what is known as the Bloch-Siegert shift - which we will see is actually just a part of the overall AC Stark shift derived in the previous section [Eq. (2.120)].

Find the Bloch-Siegert shift of the energy levels due to the counter-rotating part of the field that was ignored in parts (b) and ( c) of this problem.

Solution Intuitively, we expect that the counter-rotating component of the field should lead to an AC Stark shift arising from a field with frequency -wm instead of Wm, so the Bloch-Siegert shifts are found by replacing wo - Wm in Eq. (2.87) with wo + wm: (2.122)

where the "+" is for the upper state and the " - " is for the lower state. This for- mula can be obtained by transforming to the counter-rotating frame and following exactly the same steps we took to obtain Eq. (2.87).

Since both the Bloch-Siegert shift (2.122) and the shift calculated in parts (b)

and (c) are small perturbations to the total energy, they add independently (any

## ATOMS IN EXTERNAL FIELDS

correlations are higher-order corrections which can be ignored). Thus the overall energy shifts are ~E = ± o + o , ( d2e2 d2e2 )

4(wo - Wm)

4(wo + Wm)

(2.123)

Equation (2.123) is identical to the general formula (2.120) for AC Stark shifts derived in part ( e) of the tutorial.

## 2.8 Spin relaxation due to magnetic field inhomogeneity

Atoms with total angular momentum F = 1/2 are contained in a buffer-gas-free vapor cell of radius R whose inner wall has an antirelaxation coating that prevents depolarization upon wall collisions. The wall collisions do, however, change the atoms' velocities in a random manner.

(a) Suppose the atoms are oriented along an average magnetic field Bo applied to the cell. Determine the rate of relaxation of the polarization due to small gradients of the magnetic field. Assume that the gradients correspond to components of the magnetic field, perpendicular to Bo, with the r.m.s. value of ~B << B0 • (Note that the characteristic time of such longitudinal relaxation is usually denoted T1, while the transverse relaxation time corresponding to relaxation of atomic polarization perpendicular to Bo is denoted T2.) Assume that the Lannor frequency flL = ,-,Bo ( ~ is the gyromagnetic ratio) is much faster than the rate of collisions of an atom with the wall: 0.LR/v >> 1, where v is the atoms' thermal velocity.

(b) Same as in part (a), except now assume that f!LR/v << 1.

(c) How would the rates 1/T 1 determined in parts (a) and (b) change if the cell is filled with a buffer gas so that the mean free path length is A << R? Assume that there is no depolarization in collisions with the buff er gas atoms.

(d) For atoms contained in a buffer-gas-free vapor cell, estimate the transverse relaxation rate 1 /T2 due to small variations of the leading magnetic field. Assume that there is a magnetic field of Bo + ~B in one half of the cell and of Bo - ~B in the other half, with ~B << B0 • Hint In part (a), as an atom flies about the cell, it experiences a magnetic field with mag- nitude ~ Bo whose direction is slowly changing due to the transverse gradients.

A frame aligned with the instantaneous direction of the total magnetic field would rotate with some characteristic angular velocity w. As in Problem 2.7, it may be

SPIN RELAXATION DUE TO MAGNETIC FIELD INHOMOGENEITY convenient to introduce an additional, fictitious field B 1 = -w / 1 which accounts for the effects of rotation.

Solution (a) Imagine an atom flying from one wall to another. The atom "sees" a small, slowly changing (compared to the Larmor frequency) transverse magnetic field.

This corresponds to a rotation of the total magnetic field vector with angular fre- quency w (perpendicular to the total field vector). The magnitude of w can be estimated as ~Bv W rv ---Bo R' (2.124)

since ~B / Bo is a typical angle through which the field rotates from the point of view of the atom as it flies across the cell and R/v is the typical transit time of the atom across the cell.

Let us now consider the frame moving with the atom whose z-axis is aligned with the total instantaneous magnetic field Btot (composed of Bo and a small addi- tion corresponding to the inhomogeneity). Since the Larmor frequency is much faster than the transit rate v / R of the atom across the cell, the atomic polariza- tion adiabatically follows the direction of Btot• Since this frame is rotating with angular frequency w, in order to describe the evolution of the angular momentum, we introduce the fictitious field B 1 = -W / 'Y as suggested in the hint. The total effective instantaneous field seen by the atom is thus Btot + BI.

Next, we note that during the atom's collision with the wall, while Btot remains unchanged. the fictitious field BI experiences a jump in both the direction and magnitude. This is because the atom's velocity changes, and, consequently, so does w.

Our problem is now reduced to finding the probability of flipping the direction of the angular momentum oriented along a leading magnetic field of magni- tude ~ Bo in the presence of a fluctuating transverse magnetic field B 1. with a characteristic magnitude ~B V B1. rv ---1Bo R' (2.125)

and a characteristic correlation time of R/v. 12 Note that B 1. is much smaller than ~B.

12 The reader may wonder if the motion of the atoms through the changing magnetic field in the cell, neglecting wall collisions (imagine a cell with enormous volume), would lead to longitudinal relaxation. Under the conditions in this part of the problem, the answer is no. This is because the atom sees the field changing adiabatically, so the atomic polarization follows the direction of the local field. All of the relaxation in this case comes from the nonadiabatic changes in the effective field due to the wall collisions.

## ATOMS IN EXTERNAL FIELDS

This problem can be solved by going to a frame which rotates in such a way as to eliminate the "leading field" B,oc.

In such a rotating frame ( ignoring the trans- verse field for now), the two magnetic sublevels are degenerate. The fluctuating transverse field B_1_ appears to rotate at the Lannor frequency nL = ,Btol ~ ,Bo about an axis along the leading field.

We can use yet another trick involving a change of basis to analyze transitions between these degenerate Zeeman sublevels. Let us say ~hat the quantization axis is initially along z which points along the leading field B,ot, and the atoms are all in the state I+) z' where the subscript z denotes the direction of the quantization axis. The fluctuating transverse field is rotating in the xy-plane. If we rotate the quantization axis by 1r /2 so it is along, for example, fl, then the atoms are seen to be in a superposition of Zeeman sublevels since (2.126)

The empty Zeeman sublevel can be described, in this new basis, as (2.127)

Equations (2.126) and (2.127) show that an angular momentum flip in the z-basis corresponds to a relative phase shift of 1r (i.e., rv 1) between the Zeeman sublevels in the y-basis.

The fluctuating field B 1. causes rapid (at the frequency ~ OL) excursions of phase between the Zeeman sublevels with a small amplitude ,B_1_/0L ~ B1./ Bo.

When the atom hits the wall, it is left with a random phase excess of the same order of magnitude.

Random phase increments upon successive wall collisions correspond to a ran- dom walk. Eventually, after~ (B1./ B0)- 2 random walk steps, the accumulated phase will be rv 1, corresponding to a significant probability of a flip. Since each random walk step takes time"' R/v, we finally have: (2.128)

This is directly related to the broadening of spectral lines via phase diffusion as discussed in Problem 5.2. Note that if the atoms were stationary (v = 0), according to Eq. (2.128) there would be no longitudinal relaxation. This is because the atoms would merely remain polarized along the local field Bo + llB, so the gradients would not alter the population of the Zeeman sublevels. However, the oscillating "fictitious" field causes nonadiabatic changes in the field experienced by the atoms

SPIN RELAXATION DUE TO MAGNETIC FIELD INHOMOGENEITY which are capable, as we have seen, of inducing transitions between the Zeeman sublevels.

(b) In this case, the period of Larmor precession is much longer than the time between wall collisions, so the atomic polarization is unable to adiabatically follow the local magnetic field as an atom traverses the cell. 13 Thus there is no suppression of the transverse field ~B [compare with Eq. (2.125)].

One can m!ke a transformation to a frame rotating at nL = ,Bo in which the leading field Bo vanishes (see Problem 2.6). Again, the two magnetic sublevels in this basis (quantization axis along .80 ) are degenerate. In this frame there is a transverse field of amplitude LlB fluctuating with characteristic time R/v. As in part (a), the process of flipping the projection of the angular momentum can be described in terms of a random walk: in this case, it takes ~ (,~BR/ v )2 random walk steps to acquire a significant probability of a transition to the other Zeeman sublevel. Again, each step takes time R/v, so (2.129)

One can also understand this process without going to the rotating frame.

The transverse magnetic field components LlB drive transitions between the M = ±1/2 Zeeman sublevels (where the quantization axis is chosen along Bo, so the Zeeman sublevels are separated in energy by , Bo). Atoms flying about the cell see a rapidly changing transverse field: because v / R >> , Bo, the frequency spec- trum of this rapidly changing field is much broader than the level separation , Bo.

If the widths of the Zeeman sub levels are r ~ 1 /T1, we see that since v / R >> r, only a small fraction r R/ v of the power in the varying transverse field has the correct frequency to induce transitions.

Consequently, we set 1 /T1 equal to the transition rate [given by Eq. (3.158)

from Problem 3.7, where d£o is replaced by ,LlB in this case]: , 2LlB 2 r R -T1 ~ r (v/ R) ~ ~(,,dB)

.

(2.130)

Note the opposite dependence on the transit time R/ v in Eqs. (2.128) and (2.129). As opposed to the case considered in (a) where OLR/v >> 1 and the atomic polarization follows the local field, here the motion of the atoms actually decreases the longitudinal relaxation rate. This is a result of motional averaging 13 One way to see this is that in order to adiabatically follow the local magnetic field the atomic polarization must precess sufficiently fast to average out any transverse components. Since the atomic polarization only precesses through a small angle ~ "YBoR/v between wall collisions, transverse components of the polarization are not averaged out.

## ATOMS IN EXTERNAL FIELDS

of the magnetic field gradients - an effect analogous to Dicke narrowing (Prob- lem 5.3). Also note that T1 in this case is independent of the leading magnetic field.

This regime of spin relaxation due to rapidly fluctuating magnetic field com- ponents is important in experiments involving the coherent manipulation of cold atoms guided near the surface of microchips (Henkel et al. 2003). In such exper- iments the fluctuating fields arise due to thermal currents in the conductors (see Problem 8.16), and the spin flips induced by this effect allow the polarized atoms to escape from the trapping potential.

(c) In the presence of sufficiently dense buffer gas, the velocity of a polarized atom changes on the spatial scale of the mean free path ;\. The scale of variation of the transve~ m~netic field components for a spatial extent on the order of .-X is aB;\/ R rv V · B;\. Thus, we can write expressions analogous to (2.128) and (2.129): _!_ ~ -y2(V. iJ)2 (VJ)

T1 Oi ;\ (2.131)

;\3( - _)2 - rv - ,yV · B T1 V (2.132)

These results, under certain approximations, were derived by Gamblin and Carver ( 1965), Schearer and Walters ( 1965), and Cates et al. ( 1988).

(d) Imagine two atoms in the cell, initially with the same polarization. If the atoms were stationary, with one residing in the half of the cell having magnetic field Bo + J).B and the other in the half of the cell with magnetic field Bo - ~B, the two atoms would dephase when the accumulated phase difference becomes (2.133)

However, since the atoms are moving about the cell, the field is effectively aver- aged over a trajectory, and the difference between the average magnetic field experienced by one atom and that experienced by the other arises only due to the random nature of their paths through the cell: ~B 6Bavg ~ ../N, (2.134)

where N is the average number of bounces before the atoms dephase. Therefore Eq. (2.133) is replaced by (2.135)

THEE x V EFFECT IN VAPOR CELLS Now, N is given by the ratio of the dephasing time T2 and the transit time rv R/ v: V N ~ RT2.

(2.136)

Thus, from Eqs. (2.135) and (2.136), we have (2.137)

from which we find that (2.138)

Note that T2 for this case is basically the same as T1 in part (b) [Eq. (2.129)].

This is no accident. In both cases, one can make a transformation to a frame rotat- ing at ,Bo in which the leading field vanishes (see Problem 2.6). Without a leading field, there is no difference between T1 and T2, and it is apparent that the cases considered in parts (b) and ( d) of this problem are identical.

We also note in passing that the problem of relaxation and dephasing of ele- mentary units of quantum information, qubits, is among the most important ones in the field of quantum computation. The issues at stake can be easily understood from the discussion in this problem. Although we have considered the case where the spins (i.e., qubits) move through an inhomogeneous field, the situation is anal- ogous to the case of stationary qubits experiencing fields that fluctuate in time.

These fluctuating fields lead to decoherence of the qubit states, in the form of decay of the diagonal (T1) or off-diagonal (T2) elements of the density matrix (Appendix G) describing the qubit.

~ 2.9 The E x V effect in vapor cells Consider atoms with total angular momentum F = 1/2 contained in a vapor cell.

A unifonn magnetic field Bo is applied inside the cell, corresponding to a Larmor frequency 0£. Estimate the shift in OL arising from the motional magnetic field when an electric field E, parallel to B~, is applied.

This problem is of crucial importance in experiments searching for permanent electric dipole moments (EDMs) of atoms and neutrons, as discussed, for example, by Khriplovich and Lamoreaux ( 1997) [Section 3.5.3]. An elementary particle, atom, or a molecule can possess an EDM only if both parity (P) and time-reversal invariance (T) are violated (see Problems 1.13 and 4.8).

Hint

## ATOMS IN EXTERNAL FIELDS

There are actually two regimes that should be considered: (I) the case where nL is much greater than the rate of velocity-changing collisions (either with the walls of the cell or with the molecules of a buffer gas), and (2) the case where nL is much less than the velocity-changing collision rate.

Solution An atom moving with ~elocity v "sees" an eff.ective magnetic field which is a vector sum of the field Bo and the motional or E x v magnetic field: - -

## EX V

B=Bo+-- (2.139)

The value of the motional field averaged over the ensemble of atoms contained in the cell is zero since ( v) = 0. On the other hand, the motional field gives a nonzero contribution to the r.m.s. value of the magnitude of B: B2 ~ B5 + ( ~v r , (2.140)

B~Bo (2.141)

where v is the characteristic velocity of the thermal motion and we have assumed that Bo >> Ev/ c. Thus we have tl.Brm., ~ (EV/c)2 .

Bo (2.142)

At first glance, it would appear that the average frequency shift associated with the motional field is given by (2. 143)

where, is the gyromagnetic ratio for the atoms under consideration (which could be either on the order of a Bohr magneton, or on the order of a nuclear magneton, depending on whether we have para- or diamagnetic atoms).

However, it turns out that Eq. (2.143) is only true when nL Tc >> I, where Tc is the average time between velocity-changing collisions. Let us now estimate ~nL in the opposite limiting case where nL Tc << 1, i.e., when the velocity of an atom

## THEE

x V EFFECT IN VAPOR CELLS -TC/tc rc/tc w FIG. 2. 7 Model of the spectrum produced by the fluctuating E x v magnetic field. Components of the spectrum with frequencies nL + w cancel the effect of components at f!L - w. There remains a residual, ··uncompensated" contribution (darker shading) which causes AC Zeeman shifts of the sublevels.

changes o~ a time scale much shorter than the period of the Larmor precession in the field Bo.

_ 'I}te motional field appears to an atom as a randomly changing transverse (since EIIBo) magnetic field with a characteristic time interval between the random changes of re. The spectrum of such a field has a characteristic width of 21r /re.

We model this spectrum as a top-hat power distribution (see Figure 2.7) from w = -1r /re tow = 1r /re. The magnitude of the AC Zeeman shift is the same for a given value of the detuning IOL - wl, but of opposite sign for components of the spectrum with w > OL and w < OL [see Problem 2.7, Eqs. (2.102) and (2.103)].

The spectral distribution of the motional field is symmetric with respect to w = 0, not OL, thus it causes AC Zeeman shifts between the two sublevels due to the "uncompensated" part of the spectrum shown in Figure 2.7. The uncompensated portion of the spectrum contains"' 20L/(21r /re) of the total power contained in the whole spectrum. The AC Zeeman shift in this case can be estimated from the square of the effective Zeeman shift due to the uncompensated field and from the effective detuning (1r /re), using the results of Problem 2.7: (2.144)

A more precise calculation based on the density matrix formalism (Appendix G) gives a result that is a factor of 1r2 /9 greater than our estimate [Eq.

(2.144)], see Khriplovich and Lamoreaux (1997).

Note that the sign of the shift is the same in both limiting cases. Also note the opposite dependence on Bo in Eqs. (2.143) and (2.144). In the limit where n L re << 1, Eq. (2.144) suggests that the E x v shift can be reduced by using, for example, a buffer gas to reduce re.

## ATOMS IN EXTERNAL FIELDS

2.10 Field ionization of hydrogenic ions If an electric field f, is applied to an atom in the i-direction, the potential energy of an electron at z --+ oo assumes infinitely large negative values. An electron can tunnel through the resulting potential barrier; this process is called field ionization.

The probability per unit time of field ionization W for hydrogen in the ground state is given, for example, in Section 77 of Landau and Lifshitz ( 1977): 4m 3e ( 2m 2e )

W = f,~1 exp - 3f.h,4 .

(2.145)

Starting from this expression, write down the field ionization probability for a hydrogenic ion with nuclear charge Z.

Field ionization can be an important problem in experiments involving highly charged ions in storage rings [see, for example, Zolotorev and Budker ( 1997) and references therein].

Solution In order to obtain the required Z-scaling, one can note that the nonrelativistic Hamiltonian H p2 ze2 - H = - - - + ee · r (2.146)

2me r for a hydrogenic ion is reduced to the hydrogen Hamiltonian by substituting e' e = v'Z (2.147)

and e=e''1z.

(2.148)

Therefore the field ionization probability for an ion is: - 4m~e 9 Z (- 2m~e 5 Z )

w - £n1 exp 3£n4 .

(2.149)

2.11 Electric-field shifts of magnetically split Zeeman sub- levels Atoms with angular momentum F = 1 are immersed in a magnetic field, so their magnetic sublevels are well separated. Determine additional level shifts of the

ELECTRIC-FIELD SHIFTS OF MAGNETICALLY SPLIT ZEEMAN SUBLEVELS Zeeman sublevels arising when a weak electric field £ is applied at an angle 0 to the magnetic field. Neglect the effect of the scalar polarizability (a 0) shifting all the sublevels by the same amount, but include the effect of the tensor polarizability (02), which in the frame where the z-axis is along the electric field is described by a diagonal Hamiltonian with matrix elements (2.150)

Solution The natural quantization axis for this problem is the direction of the magnetic field; transfonning the Hamiltonian (2.150) to the corresponding frame using the rotation matrix for F = I (Appendix E)

( ½(I+ cos,B)

'D(O, {3, 0) = - ~ sin /3 ½(I - cos,B)

we have: a · a ~ sin/3 ½(1 - cos/3))

cos /J v'2 sm /J , - ~ sin/3 ½(1 + cos/3)

H' = TI(O, 0, O)HTI-1(0, 0, 0)

3cos 2 8-1 = C 3 sin 8 coslJ - v'2 3(1-cos 2 9)

3 sin (J cos lJ v'2 -(3cos 2 0 - 1)

3 sin 8 cos lJ v'2 3(1-cos 2 9)

3 sin lJcoslJ v'2 3cos 2 8-1 (2.151)

(2.152)

(2. 153)

Because the electric field is weak, we can neglect the effect of the off-diagonal matrix elements in (2.153) as they do not contribute to energy-level shifts to firSt order in the electric perturbation (ex e2 ), and the additional electric-field shifts are given by diagonal matrix elements in (2.153).

Note that the result of this problem is valid for both static and oscillating elec- tric fields (see Problem 2.7). Also, the shift of each of the Zeeman sublevels goes as a function of 0 as the Legendre polynomial P2(0) = 3cos 2 0-1 .

(2.154)

Note that the shifts vanish when the electric field is at a "magic angle" (see Problem 9 .4) to the magnetic field.

It turns out that this result is not limited to F = I. For an arbitrary F, the shift t).E(M) of a Zeeman sublevel M is proportional to [see, for example, Happer

(1971)]

## ATOMS IN EXTERNAL FIELDS

b.E(M) ex. 3 cos2 0 - 1 [JM2 _ F(F + 1)] .

(2. 155)

.

.

~ 11 · way Noting that the This general result can be understood m the o owmg · l>ed Stark shifts are quadratic in the electric field e, the tensor shifts can be e~n h .

. h h cond rank tensor 1onne as t e contraction of a rank-two tensor Oik wit t e se be out of the electric field components, eiek. The polarizability tensor 0 i~ muSt proportional to the irreducible rank-two tensor formed out of the ato~ic angular momenta (since there are no other vectors available to describe the atomic syStem).

Therefore, according to Eq. (F.42) from Appendix F, we have Oik ex. FiFk - !p 2 -+ M 2 - !F(F + 1), (2.156)

where we have made use of the fact that the large magnetic field jj averages out components of F' not along B.

_ - Similarly, the magnetic field averages out components of e not along B, so the magnitude of the effective electric field "seen" by the atoms is e cos fJ · Hence the energy shift should be proportional to cos 2 fJ. The relation (2.155) is ?btained by subtracting off the average shift of the levels to isolate the tensor shift from the scalar shift.

2.12 Geometric (Berry's) phase Consider an atom in an electric or magnetic field that changes its direction in time, returning after a while to its initial direction. One might expect that, if the atom begins in an energy eigenstate -,J,{O), after a time t when the field returns to its initial direction, the atomic wavefunction -,J,(t) would be given by t/J(t) = tp{O) exp ( -! l E(t')dt') , (2.157)

where E(t) is the energy of the atomic state as a function of time. In fact, the atomic wavefunction can differ from that in Eq. (2.157) (even in the adiabatic limit, i.e., when the field direction is changing slowly) by a phase factor eia where o is the geometric or Berry's phase (Berry 1984).

The geometric phase is a troublesome systematic effect (Commins 1991) in experiments searching for permanent electric dipole moments (see Problem 4.8), and is of some interest in its own right [see, for example, Bouchiat ( 1989)).

Consider an atom in a J = 1 state in an electric field f, ( t) that rotates about the z-axis (Fig. 2.8). Although the exact contour and time evolution of the tip of

GEOMETRIC (BERRY'S) PHASE

## I I

the electric field vector is not essential (the answer depends only on the solid angle swept out by the electric field vector), to simplify the calculation let us assume that £(t) = £o(sin0coswt x + sin0sinwt fl+ cos0 z).

(2.158)

Find the geometric phase acquired after one complete rotation of the electric field (wt = 21r). Assume the field rotates slowly (i.e., w << ~/ It, where ~ is the characteristic energy splitting of the Zeeman sublevels due to the Stark effect).

Hint Following the method employed by Commins ( 1991 ), it is convenient to introduce the "instantaneous" basis states which correspond to the !vf = 0, ±1 Zeeman sub- levels with quantization axis along the electric field £. These states can be obtained by rotating the corresponding states for quantization axis chosen along z • z y FIG. 2.8 Geometry employed for the demonstration of the geometric phase. The electric field f rotates around the z-axis with frequency w.

l l 4

## ATOMS IN EXTERNAL AELDS

We can write the rotation matrix for Euler angles (wt, 8, O): 1J(wt, 8, 0) = 1J(wt, 0, 0) · '.D(0, 8, 0)

(2. 159)

( ½ ( 1 + cos 9)eiwt '72 sin 8 eiwt ½ ( 1 - cos 8)eiwt )

.

(J = -~2 SID cos sin8 V"L.

°72 .

½(l - cos8)e-iwt sin8 e-iwt ½(l + cos8)e-iwt In Eq. (2.159) matrix indices correspond to the M components in decreasing order, as usual - see Appendix E). The three instantaneous basis states are thus ( ½{1 +lcos_8)eiwt)

·,p I ( t) = - 72 SID 8 , ½(l - cos8)e-iwt (2.160)

( "72 sin 8 eiwt )

'I/Jo( t) = cos(} , sin(} e-iwt (2.161)

( 4 {l - cos 9)eiwt )

1/J-i (t) = '72 sin 9 .

½(l + cos 9)e-iwt (2.162)

Solution In the instantaneous basis [Eqs. (2.160)-(2.162)]. we have from the Schodinger equation (2.163)

where En is the energy of the states. The states are split by the quadratic Stark effect9 and to simplify the calculation we choose the zero for energy such that E±1 = 0, Eo = -.6..

(2.164)

(2.165)

An arbitrary wavefunction \JI ( t) can be decomposed into the instantaneous basis states '11(t) = L en(t)e-iE,.t/h'I/Jn(t) I (2.166)

n where en(t) are time-dependent coefficients describing the projection and we have explicitly separated out the phase factor e-iE.,.t/h resulting from the evolution of the basis states according to the Schodinger equation (2.163).

GEOMETRIC (BERRY'S) PHASE Taking the time derivative of the expression (2.166) for \ll(t), we find ~: = ~ e-iE,.t/h( ~71/Jn(t) - i~n Cn(t)'l/Jn(t) + Cn(t) B:n) , (2.)67)

We can also determine the time derivative of '11( t) from Eq. (2. J 63): ~: = - ~ L en(t)En'l/Jn(t) e-iE .. t/h.

(2.168)

n Combining the expressions (2.167) and (2.168), we arrive at the following equation: ~ e-iE,.t/h( ~n 1/Jn(t) + Cn(t) 8:n) = 0.

(2.169)

Next we multiply Eq. (2. I 69) by ¢"/n ( t) and make use of the fact that '¢"/n(t)¢n(t) = t5mn, where tSmn is the Kronecker delta: a:; = _ L e-i(E,.-E,..)t/hen(t)'l/J!n(t) a:n .

(2.)70)

n Since we are interested in the case of a slowly rotating electric field (w << ~/ Ii), the fast oscillating terms in Eq. (2.170) can be ignored - thus we only need ~o consider degenerate states. Now we use the explicit form of the instanta!1eous basis wavefunctions [Eqs. (2.160)-(2.162)] to evaluate the quantities ¢In ( t )¢n: t· iw iw 1/111/11 = 4(1 + cos0) - 4 (1 - cos0) = iwcos0, t · iw( )

iw 1/111/1-1 = 4 1 - cos 0 - 4(1 - cos 0) = 0, t • iw( iw ¢_11/11 = 4 1-cos 0)- 4 (1-cos 0) =0, .

.

¢J'ef/o = i; sin2 0 - i; sin2 0 = 0 , .

.

t .

'lW ( 'lW .

·I/J-11/1-1 = 4 1-cos0)

- 4 (1 +cos0) = -iwcos .

Employing the results [(2.171 )-(2.175)] in Eq. (2.170), we obtain 8c±1 ~ = ~iwcos0 C±1(t), yielding C± I ( t) = C±1 (O)e~iwt cos O • (2. )71)

(2. I 72)

(2.173)

(2.174)

(2.175)

(2.176)

(2.177)

## ATOMS IN EXTERNAL FIELDS

From Eq. (2.177) we see that indeed, for wt = 271", the coefficients C±I (2 11" /w)

differ from C±i (0) by a geometric phase factor: (2.178)

or (2.179)

where n is the solid angle subtended by the electric field vector.

.

Note that this result is identical to that for a slowly varying magnett~ field.

Also, as was pointed out above, the result does not depend on the field !raJ~ctory.

A generalization to a state with total angular momentum F and z-proJecuon M states that Berry's phase is o:M =-Mn.

(2.180)

There are also direct classical analogies (for example, in rotation of solid bodies)

explored in papers by Hannay ( 1985) and Montgomery ( 1991 ).

## 2.13 Nuclear dipole-dipole relaxation

<:o~sider a crystal in which atoms are "pinned" to a lattice that can be considered ngtd. Suppose that some of the atoms have nuclei with spin I = 1 /2 and non- vanishing magnetic moment, and that these nuclei have been oriented in some particular direction.

Assuming that the spins only interact with each other (by means of sensing each other's magnetic field), and that there is no interaction with the lattice other than that the lattice keeps the nuclei fixed in space, it is straightforward to estimate the spin-relaxation rate [see, for example, Kittel (2005), Chap. 13). Because magnetic field from a dipole falls as the inverse third power of the distance, it is clear that for a given spin, relaxation is determined by its closest neighbor(s). The relaxation rate can be estimated as the Larmor precession rate of a spin in its neighbor's field: 1 µN 2 rdd""

n ~ · (2.181)

Here µN is the nuclear magneton and r is the characteristic distance between the neighbors. If the distance between interacting spins is on the order of interatomic spacing for typical condensed matter (r rv 2ao), the relaxation rate is on the order of kilohertz. This relaxation provides a lower limit on the magnetic-resonance linewidth.

## NUCLEAR DIPOLE-DIPOLE RELAXATION

Consider a system of two nuclear spins pinned to the lattice but otherwise not interacting with the lattice. Show that total angular momentum of the spin system is generally not conseived. Explain how angular momentum is globally conserved in this case. Treat the problem quantum mechanically (although this is not really necessary to understand the phenomenon).

Solution The Hamiltonian describing the interaction between the spins is (2.182)

Here fi,1,2 = 91,2µNfi,2 are the magnetic moments of the two spins, 91,2 are their nuclear g-factors, fi,2 are their spin operators, r12 is the separation between the spins, and f12 is the unit vector in the direction of r12.

Let us examine whether the total spin projection M 1 + M2 onto a given quantization axis is a conserved quantity. In order to do this, we check whether the corresponding operator lz = liz + I 2z commutes with the Hamiltonian of Eq. (2.182).

[ "]

-g192µN[ (- ,.. )(- ,.. )

- -]

lz, H = rf liz + l2z, 3 /1 · r12 /2 · r12 - Ji · h · (2.183)

The commutator term (2.184)

but the other term in Eq. (2.183) is generally not. This is because, for example, I~ · f 12 is a linear combination of the operators Iix, /iy, and /iz, the first two of which do not commute with liz- Thus we see that the total spin angular momentum is not conserved in dipole- dipole interactions. It must be that angular momentum is exchanged with the lattice. In the case of a collision of two particles interacting via a dipole-dipole interaction, there is generally an additional degree of freedom - the relative angu- lar momentum of the particles' motion. In the case of the spins pinned to the lattice, the angular momentum acquired by the lattice is in the collective motion of the sample, and thus is usually too small to be observable. This is analogous to the situation when a tennis ball bounces off a wall - although the ball's linear momentum is not conserved, the massive wall does not move appreciably.

A detailed discussion of the evolution of systems of many spins on a lattice has been given by Sodickson and Waugh ( 1995).

## ATOMS IN EXTERNAL FIELDS

## 2.14 Magnetic spin precession of a free magnet

Suppose a permanent magnet producing a uniform magnetic field in the region between its poles freely floats in space without rotation (for example, within a spacecraft in free fall). An ensemble of unpolarized paramagnetic atoms is placed in this magnetic field. At time t = 0, a short pulse of circularly polarized light, propagating perpendicularly to the magnetic field, illuminates the atoms. Some of the photons are absorbed, transferring angular momentum to the atoms. Atoms in the excited state quickly decay to the ground state, so the result is long-lived ground-state atomic polarization (this is optical pumping; see, for example, Prob- lems 3.7, 3.9, 3.10, and 9.7). After pumping, the angular momentum of the atomic sample, oriented perpendicular to the magnetic field, undergoes Lannor precession.

Explain how angular momentum is conserved during this precession. Describe the motion of the magnet assuming that its moment of inertia is a diagonal tensor.

[A uniformly magnetized hollow spherical shell has the desired properties - see, for example, Jackson ( 1975), Section 5.10.]

Solution Assume that just after the atoms have been optically pumped, their angular momentum is oriented along fj. If the magnetic field of the magnet is in the z direction, the spins precess around z. Let us consider several points in the course of one period of the Larmor precession (Fig. 2.9).

FIG. 2.9 Optical pumping and Larmor precession within a freely floating permanent magnet. The magnet rotates as a whole (with angular velocity fl) in such a way as to conserve of the total angular momentum of the system. (Figure courtesy of Alain Lapierre.)

We will also assume that the amplitude of the motion of the magnet is small, so that Larmor precession can be considered unaffected by the magnet's motion.

Just after optical pumping, the magnet is still at rest. After a quarter of the Lannor period [Fig. 2.9 (b)], the atomic orientation is along x (assuming a particular sign of the Lande factor). At this point, in order for angular momentum to be conserved,

## MAGNETIC SPIN PRECESSION OF A FREE MAGNET

the magnet has to be rotating. For small rotation angles, rotations around orthogo- nal axes can be considered independently (this is generally not true because such rotations do not commute with each other). The magnet has to rotate around the fl axis to compensate for the fact that the atoms no longer contribute any angular momentum in that direction. It also has to rotate around x to compensate for the atomic orientation that now points in this direction. The direction of the atomic orientation and the rotation of the magnet at half and three quarters of the Lar- mor period are shown in Figs. 2.9 (c) and (d), respectively. The magnet rotates the fastest at one half of the Larmor period when the orientation is opposite to its initial direction. At the end of a Larmor period the magnet comes to rest.

An interesting feature of this motion is that although the magnet comes to rest, it does not return to its original orientation. It accumulates rotation around iJ.

This problem and Problem 2.13 share a common theme - we have explored the exchange of angular momentum between a quantum spin-system and its clas- sical environment. Related effects are the Einstein-de Haas effect and the Barnett effect [see, for example, Blundell (2003), Chap. I]. The essence of the Einstein-de Haas effect is rotation of a ferromagnetic sample which is initially at rest when it is demagnetized, for example, by bringing the temperature of the sample above the Curie temperature. The Barnett effect consists in magnetization of a rotating sample.

## INTERACTION OF ATOMS WITH LIGHT

3.1 Two-level system under periodic perturbation (T)

In this problem, we consider a system (e.g., an atom) that has two nondegenerate levels subject to a periodic perturbation that couples these two states. The goal is to describe the temporal evolution of the system, assuming that it is in the lower state initially, and that the lower state does not decay. The upper state decays to some other states with a rate r. This is one of the central problems in atomic and optical physics [in fact, there have been entire books written on the subject, see, for example, Allen and Eberly ( 1987)] arising in a great variety of situations, as will be discussed in a number of further problems. Note that the content of this problem is closely related to the phenomenon of magnetic resonance (Problem 2.6) and the discussion of the AC Stark and Zeeman shifts in Problem 2. 7.

(a) Find differential equations for the time-dependent probability amplitude to be in the upper state, b(t), and the amplitude to be in the lower state, a(t). For the periodic perturbation, assume the form V(t) = Voeiwt ' (3.1)

where Vo is real.

Solution The state of the system is described by the wavef unction ( a(t))

IVJ(t)) = b(t) .

(3.2)

The temporal evolution of the system (neglecting relaxation) can be described by the Schrodinger equation: (3.3)

## INTERACTION OF ATOMS WITH LIGHT

where we have set ri = l. The Hamiltonian is given by ( Vw( 0t)) , H = V*(t)

(3.4)

where w0 is the separation between the upper and the lower state of the two-level system. The explicit form of (3.3) assuming the Hamiltonian (3.4) and the form of the periodic perturbation (3.1) is: . da Vt iwtb(t)

i dt = oe ' idb = Voe-iwta(t) + wob(t).

dt (3.5)

(3.6)

In order to include relaxation, an additional term should be added 1 to the right hand side of equation (3.6): idb = V0e-iwta(t) + (wo - if /2)b(t).

dt (3.7)

This term ensures that the amplitude b(t) decays at a rater /2, and the population decays at a rate r.

(b) We now proceed to solve the equations with the initial condition IVJ(O)) = G) .

(3.8)

Analytical solutions are possible, particularly in a number of limiting cases.

Determine the probability P(t) = lb(t)l 2 of finding the system in the upper state under the conditions where ~ = w - wo = 0 and there is no relaxation (r = O).

One can solve for a(t) and b{t) by using what is known as the interaction picture via a unitary transformation. In the interaction picture, the unperturbed wavefunctions do not change in time. In the present case, this is exactly analogous to the frame rotating with frequency w = wo used in the analysis of magnetic resonance, as discussed in Problems 2.6 and 2. 7. Such a transformation removes the time dependence in the Hamiltonian H [Eq. (3.4)] and changes the energy 1 Introducing relaxation in this way is equivalent to using instead of (3.4) a nonHermitian Hamiltonian ( V(t) )

H = V*(t)

Wo - ir /2 .

We warn the readerthat while this works in this case (and some others), in general, it is not correct to .. Write in'" relaxation terms into the Hamiltonian, and in the density matrix formalism [see, for example, Appendix G and Stenholm ( 1984)) a separate .. relaxation matrix" is usually introduced.

TWO-LEVEL SYSTEM UNDER PERIODIC PERTURBATION (T)

separation between the states from w0 to w0 - w. Therefore, in the rotating frame, on resonance the two states are degenerate and the Hamiltonian is given by (3.9)

Solution Of course, this problem is exactly analogous to Problem 2.6, and can be solved b_y saying that the two-level system is a spin:1/2 particle in a static magnetic field Bo subjected to a rotating transverse field BJ_ ( t). Then the oscillations between the two levels correspond to the precession of the magnetic moment about the transverse field in the rotating frame.

Here we offer another method of solution. We can solve for the energy eigen- states of the matrix (3.9) using the same techniques as applied in Problem 1.4, and obtain 11}=~(!1)· 12} = ~G).

These eigenstates correspond to the energy eigenvalues E1 =-Vo, E2 =Vo.

(3.10)

(3.11)

(3.12)

(3. I 3)

The initial state 'f/,(0) [Eq. (3.8)] can be written as a superposition of the energy eigenstates 11) and 12): 11/1(0)} = (~) = ~{11} + 12}) = H ( !1) + (0 J .

(3.14)

According to the time-dependent Schrodinger equation (3.3), the energy eigenstates acquire a phase as they evolve in time 11/J(t)) = -1 vv.,tll} + e-i\1<,tl2})

.

v'2 (3.15)

Since the upper state can also be expressed as a linear superposition of 11) and 12), namely (3. I 6)

INTERACflON OF ATOMS WITH LIGHT 0.8 0.6 Q.

0.4 0.2 FIG- J. l Probability, P, of finding the system in the upper state. For this plot, ~ = w - wo = 0, r == O, and the penurbation strength is chosen to be Vo = 1, which defines the scaling of the time axis. Here the system is undergoing Rabi oscillations with maximal amplitude and at a frequency of 2Vo in agreement with Eq. (3.20).

the amplitude of finding the system in the upper state is given by b( t) = ~ (-(1 I + (21) { ei\.'i,tl 1) + e-iV.,t 12))

= _! { eiV.,t _ e-iVc,t)

= -i sin(Vot) .

(3.17)

(3.18)

(3.19)

Therefore the probability P( t) of finding the system in the upper state under these conditions is given by I P(t) = lb(t)1 2 = sin2 (Vot) · I (3.20)

Figure 3.1 shows the probability of finding the system in the upper state [this plot is obtained by numerically solving the time-dependent Schrodinger equation with the full Hamiltonian (3.7)]. One can see that this probability oscillates between 0 and I with a frequency of On = 2Vo. This frequency is called the resonant Rabi frequency. 2 At small times t, the probability of finding the system in the upper state increases quadratically with time. This is an interference effect. Consider an 2 Note that in the literature one also finds definitions which differ from this one by a numerical factor.

TWO-LEVEL SYSTEM UNDER PERIODIC PERTURBATION (T)

infinitesimal time interval dt. The quantum mechanical amplitude of finding the system in the upper state scales proportional to dt. In another interval of duration dt, as long as the upper state is essentially "empty" and stimulated emission back to the lower state can be neglected, there is a similar contribution to the upper state amplitude. The contribution from the two time intervals is thus twice in ampli- tude, and four times in transition probability compared to a single time interval.

The quadratic behavior can be limited (even before a significant population builds up in the upper state) when the contributions to the amplitude from different time intervals are not in phase. This dephasing can occur due to detuning of the per- turbation frequency from the resonance as will be considered in part (c) or due to relaxation as in part ( e ).

(c) Determine the probability P(t) = lb(t)12 of finding the system in the upper state for r = 0, assuming that a(t) ~ 1 throughout [this is the case, for example, when the magnitude of frequency detuning lw - w0 I greatly exceeds Vo].

Solution We can begin by writing b ( t) = (3 ( t) e - iwo t .

(3.21)

We choose this form because in the absence of the perturbation, Eq. (3.21) with {3( t) constant would satisfy the time-dependent Schrodinger equation (3.3). There- fore the entire effect of the perturbation is contained in the time dependence of f3.

Substituting expression (3.21) into the differential equation (3.6) yields: d{3 -iw0 t • {3(t) -iw 0 t _ "Vc -iwt (t)

· {3(t)e-iwc,t -e - iwo e - -i oe a - iwo · dt Cancelling like terms on either side of Eq. (3.22) leaves us with d(3 •17 -i~t (t)

- = -ivoe a .

dt Using the assumption that a(t) ~ 1, we integrate to solve for (3(t): /3( t) = -iVo lot e -itl.t' dt' = ~ (e-itl.t - 1)

= ~ e-itl.t/2 [~ sin ( ~t)] .

(3.22)

(3.23)

(3.24)

(3.25)

(3.26)

## INTERACTION OF ATOMS WITH LIGHT

0.08 0.06 Q.

0.04 0.02 FIG. J.2 Same as Fig. 3.1, but with ~ = 10. The system is undergoing Rabi oscillations with small amplitude and at a frequency close to ~ in accordance with Eq. (3.27).

Therefore, from Eqs. (3.21) and (3.26), the probability P(t) of finding the system in the excited state is given by (3.27)

The probability P(t) to find the system in the upper state is plotted in Fig. 3.2.

We have chosen Vo = 1 (since Vo has dimensions of frequency, this means that we have also chosen a particular calibration of the time axis). One can see that this probability (or the upper state population) oscillates between O and a small value with a frequency f2R ~ ~- (d) Knowing the resonant solution (3.20) and the far-detuned solution (3.27), guess the general solution for r = 0. This solution can also be obtained ana- lytically by solving the system of differential equations ((3.5) and (3.6)] without approximations [see, for example, Ramsey (1985), Chapter V].

Solution Interpolating between Eq. (3.27) and (3.20), the general solution is given by: {2Vo)

. 2 ( 1 [ 2] 1/2 )

P(t) = (2Vo)2 + A2 sm 2 (2V0 ) + A t .

(3.28)

TWO-LEVEL SYSTEM UNDER PERIODIC PERTURBATION (T)

Ir------------------- 0.8 0.6 Q..

0.4 0.2 FIG. 3.3 Same as Fig. 3.1, but with r = 0.3. The Rabi oscillations are damped.

Q..

IO FIG. 3.4 Same as Figs. 3.1 and 3.3, but with r = 10. The system no longer exhibits oscillatory behavior (overdamped regime). Note the change in the vertical scale.

(e) Next, we explore the effect of relaxation. To visualize various regimes of the system's behavior, plot the numerical solution of the system of Eqs. (3.5), (3.7)

on resonance (~ = 0) for r = 0.3 and r = 10. (One can use, for example, Mathematica® to find and plot the numerical solutions.)

Solution

## INTERACTION OF ATOMS WITH LIGHT

.

.

.

F 3 1 except now r = Figure 3.3 shows evolutton with the same parame~ers as •_g. · d to the loss of 0.3. One observes Rabi oscillations with decreasmg amphtude ;~ For higher atoms to other states. Such damped oscillations_ oc~ur for r < Thi:is illustrated values of r, the system is overdamped and oscdlatton ceases.

.

fi ) 1 in Fig. 3.4, where r = 10. (Note the change in the vertical scale 10 the g~~h .,n the overdamped regime, at short times, the upper state population grows as e e was no relaxation, but then it "saturates" at a small level Pm:u ~ (ntf (3.29)

and then eventually decays away. The maximum upper state population occurs at a time tmax r-v 21r/r.

b · th By solving the coupled differential equations (3.5) and (3.7),_ one O tams e general analytic formula for the time dependence of the populauon of the upper state: (3.30)

## 3.2 Quantization of the electromagnetic field (T)

In this tutorial, we will briefly review the quantization of the electromagneti~ field, which will provide us with some key insights useful in understanding many impor- tant phenomena, such as spontaneous emission (Problem 3.3), the noise properties of light fields (Problem 8.8), and the Casimir effect [see, for example, Lamoreaux ( 1997) and references therein] to name a few. Detailed discussions of this impor- tant topic can be found in many texts, for example, Heitler ( 1954 ), Sakurai ( 1967), Shankar (1994), and Loudon (2000).

In the quantization of the electromagnetic field, each mode of the electromag- netic field is put into one-to-one correspondence with a simple harmonic oscillator (SHO). A mode is defined by a wave vector k and a polarization i, and, for simplic- ity, we will restrict our considerations in this problem to a single mode. Including all modes involves summing the following results over all possible k (hence all possible frequencies w) and accounting for two orthogonal _polarizations.

Consider a light field described by a vector potential A(f, t) in the Coulomb gauge (in which V • A = 0).3 We assume no free currents or charges, so the . 3 As we will see in Problem 3.3, the vector potential turns out to be a useful representation for the hght field when we consider its interaction with atomic systems.

QUANTIZATION OF THE ELECTROMAGNETIC FIELD (T)

scalar potential can be set to zero. From Maxwell's equations one finds that A( r, t)

satisfies the wave equation 1 8 A "v A - c2 E)t2 = 0 .

(3.31)

Recall that the electric e(r, t) and magnetic B(r, t) fields are related to the vector potential via - 18.A £(rt)= --- , C 8t ' B(r,t) = V x A.

(3.32)

(3.33)

To see how the correspondence between a mode of the light field and an SHO is made, we start with the general solution to the wave equation (3.31) for a given mode: A-(- t) __ 1_ [r-, ,.. i(k•r-wt) + r-t* "'* -i(k-r-wt)]

(3.34)

r, - Jv vof e v 0 f e , where A is normalized with respect to a box of volume V (this box normaliza- tion is a technique to deal with the fact that plane waves are nominally of infinite extent and so cannot be nonnalized unless we restrict the volume over which we integrate). Making the change of notation C(t) = Coe-iwt ' (3.35)

we have (3.36)

or A(r, t) = Jv [c(t)i eik-r + c.c.] ' (3.37)

so that all of the time evolution is contained in C(t) (c.c. denotes the complex conjugate).

(a) Show that the total energy E of the light field is given by (3.38)

Solution INTERACflON

## OF ATOMS WITH LIGHT

The energy in the light field is given by E = 8~ [ (t: 2 + B 2)dV, (3.39)

and using Eqs. (3.32) and (3.33) with the expression for the vector potential (3.37)

we obtain for the electric and magnetic fields - 1 aA w [ ·f - ]

e = - C ot = cv'V iC(t)i e' ·T + c.c. , B = V x A= Jv [iC(t)(k x i)eik-r + c.c.] , where we have made use of the fact that, according to the definition (3.35), !c(t)

= -iwC(t).

Keeping in mind that i is a complex vector, hence "'* A f.

·f.= ' - w2 (k X i*) . (k X i) = k2 = 2 , C (3.40)

(3.41)

(3.42)

(3.43)

(3.44)

after some calculation one finds that quantities ex C(t) 2 or ex C*(t) 2 cancel when we add the square of the electric field to the square of the magnetic field and there are four terms <X IC(t)l • Summing these terms and integrating over the volume of the box we obtain Eq. (3.38): 1 w2 E = 21r c2 IC(t)I .

(b) Now consider a classical simple harmonic oscillator (SHO), whose Hamilto- nian is given by P2 mw2 Haho = 2m + -2-q2 ' (3.45)

where q is the position and p is the momentum of the particle with mass m. A standard trick is to rescale q and p according to p= ✓-,ii:wP, Q q=yriiw' (3.46)

(3.47)

QUANTIZATION OF THE ELECTROMAGNETIC FIELD (T)

so that W ( 2 2)

Hsho = 2 Q + P .

(3.48)

(The rescaling gives Q and P the same units.)

Assuming Q = ao cos wt, compare the time dependence of Q and P to the time dependence of the real and imaginary parts of C( t) [Eq. (3.35)]. Also compare the energy E in the electromagnetic field from Eq. (3.38) to the Hamiltonian for the SHO.

Solution We begin with the relation between q and p dq P = m dt ' and make the substitutions suggested in (3.46) and (3.47) to obtain dQ wP = dt .

Therefore Q(t) = aocoswt, P(t) = -ao sin wt.

(3.49)

(3.50)

(3.51)

(3.52)

This can be compared to the time dependences of the real and imaginary parts of C(t)

Re[C(t)] = Co cos wt, Im[C(t)] = -Co sin wt .

Furthermore, compare the Hamiltonian for the SHO W ( 2 2)

Hsho = 2 Q +P to the energy of the electromagnetic field from Eq. (3.38)

E = 2~ ~ (1Re[C(t)]l 2 + 1Im[C(t)]i2) .

(3.53)

(3.54)

(3.55)

This suggests that we can interpret the real and imaginary parts of C(t) as the Q and P variables for a harmonic oscillator. Completing the analogy by saying that

## INTERACTION OF ATOMS WITH LIGHT

C(t) oc Q + iP, and choosing an appropriate constant of proportionality, we have ~ C(t) = V~ (Q+iP), (3.56)

and for the Hamiltonian of any single mode of the free electromagnetic field we have W ( 2 2)

Hem= 2 Q +P • (3.57)

(c) Now that we have linked the electromagnetic field to the SHO, we can apply all the properties of the quantum mechanical SHO [see, for example, Griffiths ( 1995)

or Problem 1.2] to a mode of the electromagnetic field. Our first observation is that the energy eigenstates of the quantum mechanical SHO can be labelled In) where n = 0, 1, 2, 3 ... , and they have energies (3.58)

What is the meaning of the quantum number n in terms of a mode of the electromagnetic field?

Solution Each photon carries an energy hw, so the number of photons in a mode of the light field is En/ ( hw). For n >> 1, we have n ~ En/ ( hw), so n corresponds to the num- ber of photons in the mode. Note that even when there are no photons in the mode, the mode still has an energy hw /2. This is the famous zero-point energy. The existence of the zero-point energy of the electromagnetic field has been demon- strated in a plethora of quantum electrodynamical effects including, for example, a recent beautiful experiment by Lamoreaux ( 1997) measuring what is known as the Casimir effect [see the review by Milton (2001) and Problem 9.9). Nonetheless, the existence of the zero-point energy is mysterious, since if one sums over all pos- sible modes of the electromagnetic field, an enormous energy density is obtained.

According to general relativity, this energy density would profoundly affect the evolution of the universe in a manner inconsistent with experimental observations.

Understanding these issues, sometimes called the physics of the vacuum, is among the most important open issues in modem physics.

(d) As our final exercise, we define the creation and annihilation operators at and a, respectively (which are analogous to the raising and lowering operators for the

QUANTIZATION OF THE ELECTROMAGNETIC FIELD (T)

SHO): where One also has Q+·iP a=--- V2h' at= Q- iP v'2fi at In) = Jn + 1 In+ 1) , aln) = Jn In - 1), [a, at] = 1 .

[Q,P] =iii.

(3.59)

(3.60)

(3.61)

(3.62)

(3.63)

(3.64)

Write the vector potential (3.37) and the Hamiltonian Hem in terms of the creation and annihilation operators.

Solution According to Eqs. (3.59) and (3.56) we can write C(t) = ~ (Q + iP) = J21r:; a.

Thus the vector potential in Eq. (3.37) is given by - J21r/ic [ .k- - t .k- -]

A= Vw ai ei ·r + a i* e-i ·r .

We will make use of this form for the vector potential in Problem 3.3.

In order to express Hem in terms of a and at, consider ata = 2 1/Q - iP)(Q + iP)

= 2~ ( Q2 - iPQ + iQP + P 2)

= 211/Q2 + i[Q, P] + p2)

= 21,/Q2 + p2 - Ii) , (3.65)

(3.66)

(3.67)

(3.68)

(3.69)

(3.70)

## INTERACTION OF ATOMS WITH LIGHT

which gives us Q2 + P 2 = 1t( 2ata + 1) .

(3.71)

Employing Eq. (3.71) in (3.57), we obtain (3.72)

Note that according to the solution to part (c) [Eq. (3.58)], the operator at a yields the number of photons in the corresponding mode of the electromagnetic field, and for this reason it is generally known as the number operator.

## 3.3 Emission of light by atoms (T)

In this lengthy but important tutorial, we derive the formula for spontaneous and stimulated emission of light by an atomic system in the electric dipole (El)

approximation (we will specify exactly what we mean by this approximation somewhat later). The approach taken here is rather formal in contrast to most of the other problems in this book; more intuitive models of atomic transitions are dis- cussed in Problems 2.6 and 3.1. The main reason for this approach is that in order to understand the physical mechanism responsible for spontaneous emission, one must invoke the quantized electromagnetic field (Problem 3.2). This necessitates some level of formal mathematics. In addition, the mathematical tools employed in this tutorial (Fermi's Golden Rule, the Wigner-Eckart theorem, Clebsch-Gordan coefficients, etc.) are used in many important areas of atomic spectroscopy [see, for example, Sobelman (1992) and Scully and Zubairy (1997)], so it is useful to be acquainted with them.

Let us consider transitions between a ground level \g) with angular momentum J and an excited level \e) with angular momentum J'. The Zeeman sublevels are labelled by the projection of the angular momentum along the quantization axis (z): MJ and M~, respectively.4 The energy separation between le) and lg) is hw0 • The first tool we will need is Fermi's Golden Rule [see, for example, Griffiths ( 1995) or Bransden and Joachain ( 1989)], originally obtained by Dirac from first- order time-dependent perturbation theory.5 According to Fermi's Golden Rule, the 4 Since many practicing spectroscopists use the book by Sobelman (1992), we caution the reader that in his notation the initial state of a transition is always labelled J and the final state J'. In particular, for emission, this means that the upper state is J and the lower state is J', opposite to our convention.

5 By .. first order" we mean that we consider only first-order changes to the wavefunctions induced by the perturbing Hamiltonian H', meaning that the probability to make a transition between the states of interest during the time over which H' acts on the system must be small.

EMISSION OF LIGHT BY ATOMS (T)

differential transition rate dW/i from an initial state Ii) to a final state I/) for atoms subjected to a perturbation described by a Hamiltonian H' is given by (3.73)

where P1(E) is the density of states - the number of states I/) per unit energy - and P(E) is the distribution of energies that allow a transition to occur (this will be discussed in more detail below). In the following calculations, we employ the quantized electromagnetic field (Problem 3.2), so Ii) and If) include both the atomic state and the photon state. Because there are only a few possible atomic states in the problem we consider, p 1 ( E) is essentially the density of photon states.

(a) Calculate the density of states function PJ (E) for photons with a given polar- ization € and whose wave vectors k are in a differential solid angle dO (where our coordinate system is centered at the atom; recall that the photons must satisfy € • k = 0). For the purposes of normalization of the photon wavefunctions, suppose that the photons are contained in a box with volume V (as in Problem 3.2).

Solution The number of photon states dN in a differential volume of phase space is d3x d3p dN = (21r )3 fi3 so integrating over the volume of the "box" and making use of the relation p=nk for photons, we have V dN = (21r)3 k dk dO , (3.74)

(3.75)

(3.76)

where df! is the differential solid angle into which the photons are emitted. We assume the index of refraction is unity, so k = w / c = E / (lie) where w is the photon frequency, and hence V E 2dE dN = (21r )3 fi3c3 dO , (3.77)

or (3.78)

## INTERACTION OF ATOMS WITH LIGHT

(b) Equation (3. 78) gi~es the total number of photon ~tates with an energy bet"'.een E and E + dE in a sohd angle d{t but we must also mclude a factor that descnbes which photon states have the correct frequency so a transition can occur. This func- tion takes into account restrictions on the accessible final states such as energy conservation and momentum conservation. Here we will assume an infinitely heavy nucleus, so we do not have to bother with effects related to atomic recoil.

Let us also assume that the only source of line broadening is the finite lifetime 1/,y of the excited state caused by spontaneous emission from le} --+ lg} (later we will calculate the spontaneous emission rate ,y). We know from the Heisenberg uncer- tainty relationship that the finite lifetime of the upper state leads to an uncertainty in its energy: in particular, the decaying exponential governing the probability to be found in le) yields a Lorentzian distribution P(w) of allowed photon frequencies (see Problem 9.3), p w - "I /(21r)

( )- (w-wo)2+("!/2)2' (3.79)

where the distribution is normalized so that the integral over all frequencies is unity.

What is the the distribution of photon frequencies P( w) that allow a transition to occur in the limit where 1 approaches zero? What is the total transition rate integrated over all photon frequencies?

Solution As 1 --+ 0, P(w) --+ 6(w - wo), where <5(w - w0 ) is the Dirac delta function. To see this, we note three properties of P(w): • the width of the function P(w) is 1 , so it tends to zero as,--+ O; • the amplitude of P(w) on resonance (w = wo) is 2/(1r1 ), so it tends to oo; and • the integral over P( w) is unity if the range of integration includes wo and zero otherwise in the limit "Y --+ 0.

This ensures that P(w) --+ 6(w - wo) as 1 --+ 0. The result is intuitive since as the linewidth of the transition tends to zero, the only way to induce a transition is to exactly satisfy energy conservation. In this limit, Eq. (3.73) becomes: (3.80)

EMISSION OF LIGHT BY ATOMS (T)

Integrating over photon energies, we obtain the familiar form of Fermi's Golden Rule: (3.81)

(c) Next we address the matrix element (/IH'li). What is the correct form of the interaction Hamiltonian H'? We can begin by writing out the total Hamilto- nian for thJ atomic system in the presence of a light field described by a vector potential A(r, t) in the Coulomb gauge (see Problem 3.2). For simplicity, we will consider a single-electron atom ( extension of the theory to multi-electron atoms is straightforward by taking a sum over all electrons).

The total Hamiltonian for a one-electron atom in the presence of the light field is taken to be 1 [ e - ] 2 Ze H = - p+ -A(r,t)

- - , 2m r (3.82)

where the quantity p is the canonical momentum [see, for example, Griffiths ( 1999) or Landau and Lifshitz ( 1987) - recall that in this book we define the electron charge to be -e].

We break the Hamiltonian into a perturbing Hamiltonian H' and an unper- turbed Hamiltonian Ho.

Show that where H ~Ho+ H', p2 ze2 Ho=---2m r is the usual Hamiltonian for an unperturbed one-electron atom and where it is assumed that I e _, - H = -p·A, me What is the physical meaning of the condition (3.86)?

(3.83)

(3.84)

(3.85)

(3.86)

Solution

## INTERACTION OF ATOMS WITH LIGHT

Simply expanding the first term in the Hamiltonian H given in Eq. (3.82) yields 1 ( e -) 2 p e (- - - -)

e - p+-A =-+- p·A+A·p +2 2A.

2m 2m 2mc me (3.87)

The condition (3.86) allows us to ignore the tenn oc A2 , since it is small in comparison to the other terms, so p2 e ( - - )

Ze H';:::j-+- p·A+A·p --.

2m 2mc r (3.88)

Furthermore, the condition (3.86) also permits us to treat the terms involving A as a perturbation, so we say that p2 ze2 Ho=---2m r is our unperturbed Hamiltonian and H' = _e_ (P · A+ A· P)

2mc is the perturbing Hamiltonian.

Now consider the tenn P. A+ A. p = 2p. A+ A· P - p. A = 2p. A+ [ A, p] .

(3.89)

(3.90)

(3.91)

Recalling that pis the generator of infinitesimal translations [see, for example, Bransden and Joachain (1989)], we have [ A, p] = itf(7 . A , (3.92)

but since we are using the Coulomb gauge, V · A = 0. Using this fact and Eq. (3.91)

in (3.89), we obtain the sought after expression (3.85): I H' = ~p-A.

I The condition (3.86) merely implies that the forces due to the light field are much smaller than the electrostatic force binding the electron to the nucleus. This can be seen from the following argument. Since the vector potential oscillates with

EMISSION OF LIGHT BY ATOMS (T)

frequency w, based on Eq. (3.32) we can estimate that the amplitude of the light electric field e0 is 18A w e0 rv -- rv -A.

C Dt C ' so the force acting on the electron due to the light field is e Flight rv eeo rv w-A .

C Near resonance, we can say that e2 W~Worv- fiao · (3.93)

(3.94)

(3.95)

If we require that the force F bind rv e2 / a5 on the electron due to electrostatic attraction to the nucleus is much greater than Flight, after a bit of algebra we have the condition h e - >>-A.

ao (3.96)

From the Heisenberg uncertainty relation, we can say that p rv h/ ao, which gives us condition (3.86).

(d) As we have mentioned above, Ii) and I/) include both the atomic state and the photon state. In the following we perform calculations for a single mode of the electromagnetic field - later the density of states and distribution functions in Fermi's Golden Rule will account for the sum over suitable modes. Thus for a complete Hamiltonian which describes both the atom and the light field, we must include the Hamiltonian for the electromagnetic field Hem [Eq. (3.72)), so Htot = H + Hem = Ho + Hem + H' • (3.97)

The interpretation of Htot is straightforward: Ho is the Hamiltonian for the unper- turbed atomic system, Hem is the Hamiltonian for the free electromagnetic field, and H' describes the coupling between the two. Ignoring the perturbation H', we see that Ho and Hem act on completely separate systems, so the unperturbed energy eigenstates can be written simply as products of the atomic state and the photon state: IY, J, MJ)ln) and le, J', M;)ln').

Use the expression (3.66) for the vector potential A in terms of creation and annihilation operators in expression (3.85) for H' to obtain matrix elements for emission of a single photon.

Solution

## INTERACTION OF ATOMS WITH LIGHT

In terms of a and at,, we have for H': (3.98)

The initial state is Ii) = le, J', N/~)ln) and the final state is I/) = lg, J, MJ}ln').

Energy conservation [see part (b)] demands that the atom must impart an energy of ~ liwo to the electromagnetic field, son' = n + 1, meaning that this is an emission event. Then only the term with at in Eq. (3.98) contributes to the matrix element since (n + llaln) = 0, thus (/IH'li) = ~ 2,rn(n + 1) ( J M 1(-. "*) -ik•r1 J' 11,,rl)

g, , J p f. e e, , .1.nJ • Vw (3.99)

where we have used (3.100)

(e) In order to solve for the emission rate, we must now evaluate the matrix ele- ments between the atomic states. It is here that we employ the electric dipole (El) approximation mentioned at the beginning of the problem. We assume that the dimensions of the electron cloud are much smaller than the wavelength of the light, so that k•r<<l, (3.101)

and thus eik-r ,..._, 1.

Express the atomic matrix element in terms of r instead of p.

Solution We begin by invoking the Heisenberg equation of motion for the atomic variables [see, for example, Bransden and Joachain (1989), Griffiths (1995), or Landau and

EMISSION OF LIGHT BY ATOMS (T)

14 I Lifshitz ( 1977)]

[- u] = ·t:.dr = inp r,no ind .

t (3.102)

Using (3.102), we can write (g, J, MJIP· i*le, J', M~) = ~~ (g, J, MJl(f'Ho - Hor)· i*le, J', M~) (3.103)

= -imwo(g,J,MJlf•i*le,J',M~).

(3.104)

(f) Introducing the dipole operator d = -er, use the spherical basis and the Wigner-Eckart theorem (Appendix F) to express the transition rate for a single mode in terms of Clebsch-Gordan coefficients and the reduced matrix element (g, JI ldl le, J').

Solution In the spherical basis [see Eq. (F.30)], we have d-i* = Ldqf.q.

(3.105)

q We can employ the electric dipole approximation and Eqs. (3.99) and (3.105)

in (3.121) to obtain (3.106)

From the Wigner-Eckart theorem (F. l) we obtain (/IH'I ·) _ ·✓21rfiwo(n + 1} (g, Jlldlle, J') ~ (J' M' 1 qlJ M )€ - V ✓2J + I ~ ' J, ' ' J q ' q (3.107)

Taking the absolute value squared of the matrix element yields l(/IH'li)l2 = (3.108)

21rfiwo( n + 1) I (g, JI ldl le, J') 1 (~ (J' M' 1 IJ M )€ )

V 2J + I ~ ' J, 'q ' J q q Inserting Eqs. (3.108) and (3. 78) into Fermi's Golden Rule (3.81 ), and taking w = wo everywhere yields the fonnula for stimulated and spontaneous emission into a

INTERACflON

## OF ATOMS WITH LIGHT

single mode Here the term 1 in the factor ( n + 1) represents spontaneous emission while n represents stimulated emission.

(g) Calculate the rate of spontaneous emission in any direction with any polariza- tion, assuming the excited state is unpolarized. This is the spontaneous decay rate "Y mentioned in part (b ).

Solution Let us consider a particular polarization i for the spontaneously emitted light.

There are two independent polarizations for a given k, so we will multiply our final result by 2 (since we assume a completely unpolarized sample, there is no preferential direction in space). Without loss of generality, we will choose i. along the quantization axis (z), so €o = 1 and €±I = 0. Spontaneous emission is induced by vacuum fluctuations, i.e., the zero-point energy, so n = 0. Since all directions of space are equivalent in our problem, we must also sum over the possible ground state Zeeman sublevels (M) and average over the excited state sublevels (M').

Employing these arguments, we obtain from Eq. (3.109): dw(spont) = _!__ wJ l(g, Jlldlle, J'}l2 ""

(J' M' 1 OIJ M )2d0.

ge 21r hc3 (2J + 1)(2J' + 1) ~ L: ' J, ' ' J MJ M., (3.110)

Now we wish to evaluate the sum over the Clebsch-Gordan coefficients. According to the identity (true so long as Iii - i2l < i < ii + i2)7 LL 01,m1,h,m2li,m} 2 = 1.

(3.111)

m1 m2 6 This procedure is equivalent to calculating the decay rate for all three possible light polarizations from a given sublevel.

7 This formula comes from the fact that we can project the state vector Ii, m) onto the product basis Iii, m1)lh, m2). Since (j, mlj, m} = 1, the sum of the squares of all the coefficients in the expansion must be equal to unity, yielding Eq. (3.111 ).

EMISSION OF LIGHT BY ATOMS (T)

Using this identity (3.111 ), we write LL L (J', M~, l, qlJ, M1)2 = L (L L (J', M~, l, qlJ, M1)2)

q M., M.~ M.1 M:, q = L 1 = 2J + 1 .

(3.112)

M., The sum with one particular q should give a third of the total result, since isotropy of space demands that the contributions for different choices of q are the same, so we conclude that '°' '°' I ( , , 2J + i Ld .

.J J ,M1,l,0IJ,M1)I = , Al., M.~ (3.113)

thus dW(sporit) = _!_ wJ l(g, Jlldlle, J')l2 ge 61r lic3 2J' + 1 · (3.114)

Integrating over the solid angle and multiplying by 2 for the possible polarizations, we obtain 4w~ I (g, Jlldlle, J') 12 ' = 31ic3 2J' + 1 .

(3.115)

Here we have assumed that the state le) decays only to lg), so that the consid- ered transition is solely responsible for the spontaneous emission. If, as is often the case in real atomic systems, the state le) can decay to several different states IYi), we have 'Y = L 'Yi = L ~n , (3.116)

where ,i are the partial widths and the coefficients ~i are known as the branch- ing ratios. Therefore, in order to determine the magnitude of the reduced matrix element I (gi, JI ldl le, J') I between two particular states from experimentally mea- surable parameters, one must know both the lifetime 1/, and the branching ratio €i: (3.117)

## INTERACTION OF ATOMS WITH LIGHT

## 3.4 Absorption of light by atoms

Here we use the tools developed in Problem 3.3 for emission of light to address the inverse process: stimulated absorbtion of a photon by an atomic system. (The results of this calculation can be compared to those obtained in Problem 3.1 by a different approach.)

We consider the same system as in Problem 3.3: an atom with a ground level lg)

having zero energy and total angular momentum J, and an excited level le) with energy hwo having angular momentum J'. The Zeeman sublevels are labelled by the projection of the angular momentum along the quantization axis (z): MJ and M~, respectively.

Suppose a monochromatic light beam (bandwidth of light much narrower than the upper state width, ~, equal to the spontaneous emission rate) is incident on an atom in a particular Zeeman sublevel of the ground state. Assume the light is on resonance w = w0 and it is linearly polarized along the quantization axis z, and that the intensity is sufficiently small that the condition still holds.

To find the stimulated absorption rate, we again rely on Fermi's Golden Rule (3.73): but now, instead of the density of photon states from Eq. (3.78), we have a single final state (one photon absorbed from a single mcxle and the atom in a particular Zeeman sublevel of the upper state), thus p I = fJ ( hw - hwo).

(a) Use the Hamiltonian (3.98) and the electric dipole approximation to write an expression for the square of the matrix element (/ IH'li), where for stimulated absorption Ii)= lg, J, Mi)ln)

and I/)= le, J', M~)ln - 1).

(b) Use the Lorentzian distribution function (3.79) on resonance w = w0 in Fermi's Golden Rule to write the stimulated absorption rate in terms of the light electric field amplitude eo.

( c) Show that the absorption rate for the lg, J, M J) --+ I e, J', M~) transition is equal to the rate of stimulated emission for the le, J', M~) --+ lg, J, Mi) transition.

## ABSORPTION OF LIGHT BY ATOMS

Hint In part (c), it may be helpful to employ the relationship between reduced matrix elements (Sobelman 1992), 8 J' J I * (e,J'lldllg,J) = (-1)

- (g,Jlldlle,J)

, (3.118)

and the relationship between Clebsch-Gordan coefficients (Varshalovich et al.

1988), J J' +q 2J' + 1 ( , , (J,MJ,K,qlJ',M.',}=(-l)

- 2J+l J,Mj,K,-qlJ,MJ).

(3.119)

Solution (a) The perturbing Hamiltonian in the electric dipole approximation can be found using Eq. (3.98) and condition (3.101) to be H' = : ti§ [a(P· f) + at(p-i*)] .

(3.120)

Only the term with a in Eq. (3.98) contributes to the matrix element since (n - llatln) = 0, thus e ✓21r1in ( J' M' 1(- ")I (JIH'li} = ;;;_ Vw e, ' J p•f. g,J,MJ}, (3.121)

where we have used (n- llaln) = vfn (n- lln-1)

= vfn.

(3.122)

The matrix element (e, J', M~l(P · i)lg, J, MJ) is given by the complex conjugate of (3.104), so in the spherical basis we obtain: (3.123)

8 Considering the usual phase convention for the spherical harmonics (Y,m's), the reduced matrix elements for induced electric dipole moments are real, so Eq. (3.118) turns out to be: (e, J'lldllg, J) = (-l)J'-J (g, Jlldlle, J') .

## INTERACTION OF ATOMS WITH LIGHT

From the Wigner-Eckart theorem (F. I) we obtain (JIH'li} = -i ✓21rlu,;on (e,J'lldllg,J} LP,MJ,1,qlJ',M~}(-I)qLq.

V ✓2J' + 1 q (3.124)

For the case of z-polarizecl light9 q = 0 (lo = 19 f±1 = 0), therefore (/IH 'I ·) = - · ✓21rlu,;on (e, J'lldllY, J} (J M 1 OIJ' Af') .

V ✓2J' + I ' J' ' ' J (3.125)

Squaring the matrix element yields l(/IH 'l·)l 2 = 21rlu,;onl(e,J'lldllg,J}l 2 (J M 1 OIJ' M')2.

V 2J' + I ' J, ' ' J (3.126)

(b) The absorption rate for photons from a single mode of the electromagnetic field is given by substituting for J P( E) p I ( E)dE the resonant value of the Lorentzian distribution [Eq. (3.79)] 9 2/(1i1r,)9 into Fermi's Golden Rule (3.73): Weg = ,!2 l(JIH'li}l 2, (3.127)

where the square of the matrix element is given by Eq. (3.126).

All that is left to do is relate the number of photons in the mode n to the electric field amplitude to. The average light intensity I is given both by the time averaged magnitude of the Poynting vector and the product of the photon flux nc/V and energy per photon 1u,; n I= Vlu,;c.

Equating the two expressions for light intensity I gives Vt 2 n - - 81rlu,; .

Thus the square of the matrix element (3 .126) in terms of to is I (JIH'li} 12 = l(e, J'lldllg, J} 12£~ (J, MJ, 1, OIJ'' M~}2 2J' + 1 ' (3.128)

(3.129)

(3.130)

(3.131)

## RESONANT ABSORPTION CROSS-SECTION

yielding for the rate of absorption We = ~ l(e, J'lldllg, J)l2t6 (J, MJ, 1, OIJ', M~)2 , li2 2J' + 1 · (3.132)

(c) Under the considered conditions, from Eq. (3.109), we have fo th value squared of the matrix element describing stimulated emission r e absolute I( J M IH'I J' AI' )12 = 21r11Won l(g, Jlldlle, J')l2 ' ' g,, J e, ' J V 2J+l (J,MJ,l,OIJ,MJ)2_ (3.133)

Equation (3.130) can be used to express the number of photons in the mod .

terms of the electric field amplitude to, and, as discussed in part (b), e, n, in j P(E)pt(E)dE = n!-y .

(3.134)

Thus we have for the rate of stimulated emission w - ~ l(g, Jlldlle, J')l2t5 (J', M~, 1, OIJ, MJ) 2 ge - 'Y fi2 2J + I .

(3.135)

The final step is to use the relations given in the hint for the problem, Eqs. (3.118)

and (3.119) in Eq. (3.135), which gives us: w - ~ l(e, J'lldllg, J)l2t6 (J, MJ, 1,0IJ', M~)2 ge - 'Y fi2 2J' + 1 ' (3.136)

so indeed W9e = Weg· It is interesting to compare this argument with that given by Einstein to derive the A and B coefficients [see, for example, Griffiths ( 1995)].

## 3.5 Resonant absorption cross-section

A very convenient concept when studying the absorption of light by an atomic medium is the absorption cross-section a abs, where the excitation rate is given by the photon flux <f) times O"abs· Consider transitions between a ground level lg) with total angular momentum J and an excited level le) with angular momentum J', separated in energy by !iw0 • Assume the atoms are initially unpolarized, and that the incident light is on resonance (w = w0). Calculate the absorption cross-section (averaged over the initial sublevels MJ) assuming only homogeneous Lorentzian broadening of the transition.

Solution

## INTERACTION OF ATOMS WITH LIGHT

The resonant absorption cross-section a abs is given by (3. I 31)

where Weg is the excitation rate of atoms due to stimulated absorption. We c3'1 calculate Weg using Eq. (3.132) from Problem 3.4, where here we choose )in¢ polarization (but, as one can verify, the choice of polarization does not matter fof the final result!): w = _1 l{g, Jlldlle, J')l2e5 ~ ~ l{J M 1 OIJ' M' )12 eg 1'1ot h2(2J' + 1)(2J + 1) it~ ' J, ' ' J ' .I J (3. 138)

where rtot denotes the total width of the transition (including, for example, sponta- neous decay to other levels, pressure broadening, etc.) and in order to account for all possible transitions between different Zeeman sublevels, we have summed over the final states (M~) and averaged over the initial states (M J ). We use the formula (3.113) to write ~ ~ I (J M 1 01 J' M' ) 12 = 2J' + 1 ~ ~ , J, ' ' J .

(3. I 39)

M., M:, yielding Weg = _1 l(g,Jlldlle,J')l2e5 rtot 1i2 3(2J + 1) .

(3. t40)

The photon flux is given by (3.141)

so we have _ 81r wo 1 I {g, JI ldl le, J') 12 O' abs - - - -- _____ ____;__;_ .

C 1irtot 2J + 1 .

(3.142)

Next we can express the reduced dipole moment l{g, Jlldlle, J')I in terms of the spontaneous decay rate between le) and lg) [Eq. (3.115)), known as the partial

ABSORPTION CROSS-SECTION FOR A DOPPLER-BROADENED LINE width ,p: l(g, Jlldlle, 1'}1 2 = (2J' + 1)~ ~"Ip, 4 w0 which when substituted into Eq. (3.142) gives us or c2 2J' + 1 , lTabs = 21r2--- P .

Wo 2J + 1 / tot A2 2J' + 1 , l1 - ___ P abs - 21r 2J + 1 1 tot , (3.143)

(3.144)

(3.145)

where A is the wavelength of the transition. The factors 2J + 1 and 2J' + 1 are the statistical weights of the ground and excited states, respectively.

This is a very interesting and important result. Take, for example, a closed ( 1p = 1tot) J ~ J transition: (3.146)

which does not depend on anything except the wavelength of the light! Thus the resonant absorption cross-section a abs is the same for both weak and strong tran- sitions. The common notion that weak transitions have small absorption cross sections comes from the ,p/r1ot factor. Also note that, in fact, the same formula, Eq. (3.145), holds for magnetic dipole transitions (Ml), electric quadrupole (E2), etc.

3.6 Absorption cross-section for a Doppler-broadened line In dilute thermal atomic vapors, the dominant line broadening mechanism for opti- cal transitions is related to Doppler shifts of the light "seen" by moving atoms.

Suppose we consider fluorescence in the z-direction. For an atom moving with velocity Vz along i, the observed frequency of the emitted light is W 1 ~ W ( 1 + V;) .

(3.147)

The atoms in a vapor cell follow a Maxwellian velocity distribution, i.e., the density of atoms nv(vz)dvz with a velocity component along z between Vz and

Vz + dvz is

## INTERACTION OF ATOMS WITH LIGHT

~ -Mv~/(2kJJT)dvz .

nv(vz)dvz = n.otv ~ e (3.148)

.

.

.

s of the atom, and kB is Boltz- where n,ot 1s the total density of atoms, M 1s the ~as width of the transition, mann's constant. When Doppler broadening dominates the .

this leads, to a Gaussian distribution in the fluorescence spectrum.

(3.149)

· the detuning of the light where IF(~) is the fluorescence intensity,~ = w - wo ts frequency w from the resonance frequency wo, and (3.150)

is the Doppler width.

.

Suppose the peak resonant light absorption cross-section for _s~auonary ato~s is <10 (see Problem 3.5) and the homogeneous width of the tran~itton (FWHM~ ts '"'f. What is the peak absorption cross-section (o-v) if atoms are m thermal motion so the Doppler width is large: r D >> "(?

Solution In the absence of Doppler broadening, the homogeneous (Lorentzian) absorption profile is: (3.151)

where ~ = w - wo is the detuning of the light frequency w from the resonance frequency w0• In the limit of large Doppler width, the frequency-dependent cross-section is written in the form u(~) = uve-(6./fn)

• (3.152)

In order to relate u D and u0, we notice that Doppler broadening does not change the area under the absorption curve. Indeed, inhomogeneous broadening (i.e., broadening arising due to a difference in resonance frequencies for differ- ent atoms) just spreads the center frequencies of resonances for individual atoms

SATURATION PARAMETERS (T)

without affecting the shape of the absorption profile for each atom. We have: (3.153)

(3.154)

Setting these two integrals equal to each other we obtain: ~ "I r av= --ao ~ 0.89 x -ao.

2 rv rv (3.155)

3. 7 Saturation parameters (T)

Consider an ensemble of atoms that are illuminated by a light field. Suppose we want to measure some property of the atoms with the light - for example, we are interested in determining the strength of a particular transition. In this situation, we need to be careful that the light field itself does not perturb the property of the atoms we are trying to measure. On the other hand, perhaps we are interested in observing some nonlinear optical process or maybe we want to optically pump all of the atoms into a particular Zeeman sublevel. In these cases, it is necessary that the light field strongly perturb the atomic system.

The crucial parameter that characterizes what regime we are in - whether or not the light field strongly perturbs the populations of the atomic states - is called the saturation parameter K. The general form of the saturation parameter is excitation rate K=------ relaxation rate · (3.156)

The tricky part is that the exact form of K and the behavior of the system as a function of K depend on the specific system under consideration - the atomic level structure, the relaxation mechanisms, etc. In this problem, we consider a variety of systems in order to gain familiarity with calculating saturation parameters and understanding their implications.

In the following cases (a) and (b), assume that the light is tuned to resonance and that the optical depth is small, i.e.

(3. 157)

where f, is the length of the atomic sample, n is the atomic number density, and a abs is the appropriate absorption cross-section (see Problems 3.5 and 3.6). The quantity fo = {naabs)- 1 is commonly referred to as the absorption length. The

## INTERACTION OF ATOMS WITH LIGHT

I e > ___ , T;,ump I v 19> F 3 5 Level diagram for the two-level system considered in part ( a).

IG.

.

condition (3.157) ensures that the intensity of the light field does not significantly change as the light propagates through the sam~le and, ~s long. as all dimensions of the atomic sample are similarly small, that high atomic density effects such as radiation trappingg are not important. Additionally we assume that the average spacing between the atoms n - 1/ 3 is considerably larger than the wavelength of the light A. This allows us to ignore effects that involve cooperative behavior of the atoms [such as Dicke superradiance (Dicke 1954), see Problem 3.14].

(a) Consider two-level stationary atoms for which the only source of line broad- ening is the spontaneous decay of the upper state le) back to the lower state lg) (Fig. 3.5). Calculate the saturation parameter "' for the lg) __,.. le) transition for narrow-band (monochromatic) incident light, and find the dependence of the fluorescence intensity on ""· Solution !he excitation rater pump (we can think of the light effectively ''pumping" the atoms mto the excited state) is given by Eq. (3. I 32) from Problem 3.4: d2£2 r - pump - -- 10 (3.158)

where~ is the di~ole matrix element (eldlg) between the states, £0 is the amplitude of the hght electric field, ,o is the spontaneous decay rate of le) to lg), and we have 9_ If the atomic density is sufficiently high, there can be a significant probability that spontaneous)

emitted photons are re-absorbed. Thus the photons must diffuse out of the atomic sample h" ~ affects, for example, measurements of excited state Ii f eti mes. See, for example, Corney ( 1988; tc

SATURATION PARAMETERS (T)

set h = l. The relaxation rate in this problem is ,o, so from (3.156) we have (3.159)

The fluorescence intensity IF is proportional to the number of atoms in the excited state Ne multiplied by the spontaneous decay rate , 0 • To find the popula- tion of the upper state we can write rate equations for the number of atoms in the excited state Ne and the number of atoms in the ground state Ng: d:g = -r pumpNg +ho+ rpump)Ne , (3. 160)

d:e = +rpumpNg - ho+ r pump)Ne.

(3.161)

We also know that Ne + Ng = N, 01 where N,01 is the total number of atoms in the sample. We have included the pumping rate for both the lg) -+ le) transition and the le) --+ lg) transition because at sufficiently high light powers (K ~ 1), stimu- lated emission from the upper state becomes important compared to spontaneous emission. It is clear that the stimulated emission and absorption rates should be the same from time-reversal symmetry [this can also be seen from Einstein's famous argument involving an atomic gas in thermal equilibrium with a photon gas, which was used to derive the A and B coefficients; see, for example, Griffiths ( 1995) or Bransden and Joachain (1989)). In equilibrium, dN 9/dt and dNe/dt are zero, and we find that K, Ne = l + 2K N101 , (3.162)

so the fluorescence intensity is proportional to K/(1 + 2K) (Fig. 3.6).

(b) Now suppose we have a three-level system as shown in Fig. 3.7. The incident light is resonant with the lg) --+ le) transition and the excited state le) primarily decays to a metastable level Im,) at a rate , 0 • There is a slow relaxation rate ,rel << 10 of the metastable level back to the ground state. The states Im) and fg) could be, for example, different ground state hyperfine levels, and ,rei could be the result of collisional relaxation. Again assume that Doppler broadening may be ignored and that the excitation light is monochromatic.

Calculate the saturation parameter K for this situation, and find the dependence of the fluorescence intensity on "'· Solution The relaxation rate referred to in Eq. (3.156) is generally the slowest relaxation rate in the system, since this process becomes a 0 bottleneck" for the incoherent

INTERACflON OF ATOMS WITH LIGHT

## 0.5 r--~--~----------

0.4 -------- ~ 0.3 N.01 0.2 I I 0.1 K FIG. 3.6 Fractional population of excited state as a function of the saturation parameter "' for the case described in part (a). The fluorescence intensity / F is proponional to -roNe, I;ump FIG. 3. 7 Level diagram for the three-level system considered in pan (b ).

return of atoms to the ground state. Therefore in this case the saturation parameter is given by K=-- 101rel since ,re1 is the slowest rate in the problem.

(3.163)

To verify Eq. (3.163) and find the dependence of the spontaneous emission intensity on K we again write down the appropriate rate equations as we did in

SATURATION PARAMETERS (T)

## 0.5 r----~---.----

0.4 ~ 0.3 N.ot 0.2 0.1 ,/ ---------- J / -~---- --- -- - - -- -- K FIG. 3.8 Fractional population of excited state as a function of the sat .

urat1on paramet case described in part (b). For the plot we have chosen 'Yrel/'Yo = 0_2_ er"- for the part (a): dN 9 dt = -fpumpNg + "/re1Nm, dNe dt = + f pump Ng - "foNe , dNm dt = +"toNe - "/re1Nm , (3.164)

(3.165)

(3.166)

where we have negl~t~d stimulated_ emission (since the transition saturates long before stimulated em1ss1on becomes important). We also have the condition N = Ng + Ne + Nm. Setting the time derivatives of the populations equal to ze;~ to obtain the steady state result, after some algebra (and making use of the fact that ,rel << ,o) we find for the excited state population (Fig. 3.8)

(3.167)

Note that the maximum population in the upper state (obtained for K >> 1) is Ne(max) = rrel Ntot .

,o (3.168)

Again the fluorescence intensity is proportional to ,oNe, so the maximum fluores- cence intensity is smaller than in the two-level case by a factor of 2,rei/,0, since atoms tend to reside in the "bottleneck" state Im).

(c) Now we discuss the phenomenon of power broadening. Consider the atomic system discussed in part (b) of this problem (Fig. 3.7).

INTERACflON OF ATOMS WITH LIGHT Jf one scans the frequency of a laser through the atomic resonance at low light ~ers [K << 1, where K is given by expression (3.163)], one finds that the fluo- ~cence intensity measured as a function of detuning has a Lorentzian lineshape ,e .d h itll WI t ,o.

v,; What is the dependence of the fluorescence intensity IF( t:,,.) on detuning for ?

J8f8e K.

solution AS the excitation light is tuned through resonance with the lg) ~ le) transition, tile pumping rate r pump follows a Lorentzian dependence, 10 so we have an effective saturation parameter "-etr(~) that depends on the detuning Ll of the light from resonance: ,J/4 Ketr( t:,,.} = Kt:,,.

2 + "Y6 / 4 , (3.169)

wbere K is the resonant saturation parameter [Eq. (3.163)) and the Lorentzian is 11onnalized to unity on resonance. The effective saturation parameter Kerr( Ll) can t,e used directly in the rate equations in place of K, so we obtain from Eq. (3.167)

the fluorescence intensity IF(~) ex ,oNe as a function of detuning: "-eff( ~)

IF ( l:,,.) CX: l + Ketr( l:,,.) "Y rel N 101 ,5/4 = K, A 2 + 2/4 ( 2 4 ) TrelNtot u '0 1 + K, ~"Y• .......

•-.--.-- ~ 2 +"Yo 4 ,6/4 - l:,,.2 + {l + 11:)"YZ/ 4 K"'fre1N101 • This is just a Lorentzian profile with a width I "Y = -yoJl + 11: I known as the power-broadened linewidth.

(3.170)

(3.171)

(3.172)

(3.173)

( d) Finally, we consider how Doppler broadening affects our results. If the atoms in a sample have a thermal distribution of velocities, from the viewpoint of a moving atom the light frequency is shifted by an amount~ k·v, where k is the wave vector of the light and vis the atomic velocity. Averaging over all atomic velocities, as 10 This can be seen by calculating the stimulated absorption rate as done in Problem 3.4 without assuming the excitation light is on resonance, but rather using the Lorentzian profile from Eq. (3. 79).

SATURATION PARAMETERS (T)

~ ro=ro0+ k-v Frequency FIG. 3.9 When narrow-band excitation light is tuned to frequency w within a Doppler-broadened profile, the fluorescence is due to a particular group of atoms with velocities iJ whose Doppler shifts are ;S "Y.

mentioned in Problem 3.6, we have for IF(~) in the limit of large Doppler width f D >> ,o: 11 (3.174)

In contrast to the previously discussed homogeneous broadening mechanisms such as spontaneous emission and power broadening, Doppler broadening is an example of inhomogeneous broadening - the probability for emission and absorption is not the same for all atoms.

Again consider atoms with the energy level structure shown in Fig. 3.7, but now assume that the atoms have a thermal distribution of velocities. If we tune the narrow-band excitation light to a particular frequency within the Doppler profile, the light primarily interacts with a group of atoms whose velocities are such that the Doppler shifts are less than the homogeneous linewidth. Such a set of atoms is commonly referred to as a velocity group, illustrated in Fig. 3.9.

What is the dependence of fluorescence intensity on "' for such a Doppler- broadened medium?

11 A more accurate representation of the spectral profile, which takes into account both homoge- neous and inhomogeneous broadening mechanisms is the Voigt profile, which is a convolution of Lorentzian and Gaussian profiles [see, for example, Demtroder (1996) and Khriplovich (1991 )].

Solution

## INTERACTION OF ATOMS WITH LIGHT

.

hich the light interacts is The fraction 6N of the total number of atoms Ntot w•th w 6N rv _J_Ntot , rv (3.175)

. d red case , is the power- where 'Y is the homogeneous linewidth. For the co~si e 'quations for the broadened linewidth given by Eq. (3.173). Otherwise, .the ~t~ e art (b), and we resonant velocity group remain the same as those considere m P have: K, K, ,o N IF ex: --6N ex: --=== -r tot • 1 + K Jl + K D (3.176)

.

h fl escence intensity con- Note that m contrast to the Doppler-free case, t e uo~ tinues to increase (ex ,,j,i,) even for K » 1. This continues as long as 'YoJ~ + K « r D• In the opposite limit, -y0J1 + l'i, » r D, Doppler broadening may be ignored.

## 3.8 Angular distribution and polarization of atomic fluores-

cence Atoms are prepared in the M~ = 1 /2 Zeeman sub level of an excited state with angular momentum J' = 1 /2, from which they spontaneously decay to a lower state that also has J = 1 /2. No external fields are applied.

(a) What is the angular distribution of the emitted light intensity?

(b) What is the polarization state of the light emitted in a given direction?

Hint See Appendix D explaining how to specify light polarization states.

Solution (a) Assume that the atoms are at the origin of a Cartesian frame. The problem has axial symmetry with respect to the quantization axis (z), so it is sufficient to only consider radiation emitted in the direction whose vector lies in the x > 0, xz-semiplane. The direction of light propagation is therefore completely defined by the polar angle (J (Fig. 3.10). For a given 8, two independent, orthogonal light

ANGULAR DISTRIBUTION AND POLARIZATION OF ATOMIC FLUORESCENCE polarization directions can be chosen: i 1 = iJ and i 2 = fJ = cos fJ x - sin fJ i ~ (3.177)

which are directions orthogonal to the light propagation along k (Fig. 3.10).

There are two possible decay channels (Fig. 3.11 ). The amplitude A of the emission with a given polarization i into the final state IJ = 1/2, MJ) is A ex (J = 1/2, MJli · flJ' = 1/2, M~ = 1/2) .

(3.178)

According to the Wigner-Eckart theorem (Appendix F), only the q = 0 spherical component of i contributes to A for the decay to M J = 1 /2, and only the q = + 1 component of i (which picks out the q = -1 component of r, see Eq. (F.30) in

## Appendix F) contributes to A for the decay to MJ = -1/2. The amplitude A is

proportional to the corresponding Clebsch-Gordan coefficients, which are (1/2, 1/2, 1, -111/2, -1/2) = v1 for the a+ emission and (1/2, 1/2, 1,011/2, 1/2) = JI for 1r emission.

(3.179)

(3.180)

Let us first consider the 1r emission. In a classical picture, such emission is produced by a dipole oscillating along z (at the transition frequency). We can therefore expect that the largest emission intensity is in the equatorial plane (9 = 1r /2), and that there is no emission along z (fJ = 0, 1r). These expectations are confinned by the exact expressions. The intensity of the emission with a given = f e ' ,.~ .. f--------- - tom FIG. 3.10 Coordinate system for analys~s of atomic fluorescence: k is the light propagation direc- tion, Y (pointing into the page) and () are onhogonal light polarization directions. Because of cylindrical symmetry, we need only consider the xz-plane.

## INTERACTION OF ATOMS WITH LIGHT

I/3 1f .,,, Y to either one of the two FIG. 3.11 Atoms in the excited state J = 1/2, MJ = 1/2 can eca .

· ·ons respectively). The Zeeman sublevels of the lower J = 1 /2 state (the 1r and a+ emassa ' be · d"

. .

portional to the squares of the num rs m 1cate relative overall intensity of the em1ss1ons pro corresponding Clebsch-Gordan coefficients.

polarization vector for a given O ( as we have introduced above) is proportion~l to the square of the scalar product of the corresponding polarization vector and z: /~1r)(O) ex IY · zl2 = 0; 41r>(o)

oc 10. z1 2 = l(cosO X - sinO Z). z1 2 = sin 2 0.

(3.181)

(3.182)

Thus the overall intensity is J10/1r>(O) oc sin 2 8.

Now consider the u + emission. In a classical picture, such emission is produced by a dipole rotating (rather than oscillating) in the xy-plane. We can therefore ex~ct that the largest emission intensity is along z (8 = 0, 1r), while in the equa- tonal plane (8 = 1r /2), the emission should have one half of the intensity. (This is because the dipole's rotation can be decomposed into two orthogonal oscillations, and onl_y one of them is "seen" from the equatorial plane.) These expectations are_ a~am _confirmed by the calculation. Using the polarization vector for the u + em1ss1on m the f onn A 1 ( A O ")

£+ = - v'2 x+iy , (3.183)

we have J~CT>(o)

oc IY. i+l2 = Y. _I_(x + iy") 2 - ! .

v'2 2 ' (3.184)

i CT)

( 8)

, ...

## COS 2

e oc 8-i+ = (cos8x-sin8z)·-(x+iy)

--- v'2 (3.185)

ANGULAR DISTRIBUTION AND POLARIZATION OF ATOMIC FLUORESCENCE 0.75 0.5 0.25 - 0.25 -0. 5 - 0.75 ,/ ,, ,, I I I I I I I I I ,,,,.-- ·- .

I • ,I \ · f I / -·-·- / ' ' ' \ ---·- - -- · / I / \ \ \ I I I I "}' /1 ' I I I I I I I -0.75-0 .5-0.25

## 0.25 0.5 0.75

X FIG. 3.12 Normalized angular distributions of fluorescence intensity for 1r emission (dot-dashed line), u emission (dashed line), and the overall distribution (solid line), which is isotropic in the present case.

The total intensity of the a-emission is (3.186)

To find the overall intensity of radiation in a given direction, we need to add the two contributions, lto/'r) ( 0) and lto/o-) ( 0), weighted by the total probability of the corresponding emissions ( 1/3 and 2/3, respectively). The result is independent of (}, meaning that the total light intensity is emitted isotropically.

The normalized angular distributions for the 1r and a light and the overall isotropic distributions are shown in Fig. 3.12 (b) Even before any calculations, it is clear that for 0 = 0 or 1r, only the a light is seen, and therefore light is completely circularly polarized. In the equatorial plane (8 = 1r /2), equal amounts of independent contributions of the vertically polarized 1r light and horizontally polarized a light are seen, so the light is unpolarized.

For a general value of 0, a horizontally oriented polarizer (along y) will transmjt an intensity ex 1/2 from the a light, while a vertically oriented polarizer (along 0)

will transmit an intensity oc (cos2 0)/2 from the a light and oc (sin2 0)/2 from the

## INTERACTION OF ATOMS WITH LIGHT

1r light. Thus for the first Stokes parameter (Appendix D) we have: 81 = Ix - Iy _ 1 - cos2 (J - sin2 8 = O.

Io (3.187)

From symmetry, it is clear that S2 = 0 also. The linearly polarized 1r light cannot contribute to S3• From the discussion in part (a) [in particular Eqs. (3.184) and (3.185) ], we also see that the vector amplitude of the u + light emitted in a given direction can be written in the form cos (J A 1 ( A)

- ../2 fl- ../2 8 ex ../2 fl- icosfJ 8 , (3.188)

where we have removed the overall phase factor. By taking the scalar product of this amplitude with the amplitude vectors ,_, 1 ( A •(J")

€+ = - ../2 y + i (3.189)

for the left-circular polarization 12 and ,_, 1 ( A "IJA)

€_ = ../2 y - 1, (3.190)

for the right-circular polarization, we find that 83 = I+ - [ _ __ (l_+_cos_lJ_)2_-_(_1_-_c_o_s_lJ)_ 2 = cosfJ.

Io (3.191)

This shows that light emitted with fJ = 0 is left-circularly polarized, while light emitted with fJ = 1r is right-circularly polarized. The degree of polarization is P = I cos IJI in agreement with our qualitative argument above.

## 3.9 Change in absorption due to optical pumping

For J = 1 -+ J' electric dipole (El) transitions (with J' = 0, 1, 2), find the relative changes in populations of the J = 1 Zeeman sublevels as a result of optical pumping with linearly polarized light (assume the quantization axis along the axis of light polarization, i.e., 1r-polarization). Assume "closed" transitions (i.e., atoms excited to the upper level can only decay back to the lower level), that the excitation light is on resonance, the medium is optically thin, and that, in order to simplify 12 The circular polarization vectors i~ and i'_ are defined to be orthogonal to k, and we identify fl as the horizontal direction and -8 as the vertical direction to form an appropriate right-handed coordinate system [compare with Eq. (3.183)].

CHANGE IN ABSORPTION DUE TO OPTICAL PUMPING calculations, the optical pumping saturation parameter K (see Problem 3.7) is much less than one [assume a relaxation rate 1'rel << "Yo between the ground state Zeeman sublevels, where "Yo is the spontaneous decay rate (Problem 3.3)].

Verify that for the J = 1 --+ J' = 0, 1 cases, optical pumping leads to reduc- tion of further light absorption by the medium, while in the J = 1 --+ J' = 2 case the opposite is true: absorption increases as a result of optical pumping. This is a general property of J --+ J + 1 transitions (as opposed to J --+ J - 1, J tran- sitions) that holds for arbitrary light polarization [Kazantsev et al. ( 1985)]. Note that although we assume K small in this problem, the qualitative conclusion, that optical pumping reduces absorption for J --+ J - 1, J transitions and increases absorption for closed J --+ J + 1 transitions, holds for any K.

Solution As is often the case, it is helpful to think about a related problem that permits a simple solution in order to understand the basic effect. Consider optical pumping with circularly polarized light in the limit of large "'· (As noted in the statement of the problem, it turns out that the general result is independent of light polarization and holds for any K.) As Fig. 3.13 shows, for the 1 --+ 0, 1 transitions, the atoms will end up in states that do not absorb light (so-called dark states). However, for the 1 --+ 2 transition, the atoms are pumped into a state that does absorb light (a bright state).

According to the results of Problem 3.4, the absorption rate is proportional to the square of the Clebsch-Gordan coefficient describing the coupling between lower state and upper state. For a J = 1 --+ J' = 2 transition and a+ polarization, the relevant Clebsch-Gordan coefficients are: I I (J, M, 1, llJ 'M = M + 1) = 6 =1 (11, -1) --+ 12, 0))' (11,0)--+ 12, 1))' (11, 1) --+ 12, 2)) .

(3.192)

(3.193)

(3.194)

Thus the atoms are pumped into a state that has a stronger coupling to the light field, leading to increased absorption!

Prior to considering the specific cases, we outline the general approach to the problem. The first task is to determine the manner in which the light redistributes the population among the various ground state Zeeman sublevels, which is rather tricky for the general case. To find the density of atoms p9 (M) in a particular ground state sublevel IJ, M), we must find the rate at which atoms are being excited from IJ, M) and the flux Fsp(M) of atoms decaying back to IJ, M) via spontaneous emission from all the various excited state Zeeman sublevels I J', M')

## INTERACTION OF ATOMS WITH LIGHT

l ➔O l ➔l 1 ➔2 M=-2 M=-1 '-;i )

( I ( )

(.__ ) ·--,)

M=O M= 1 M= 2 FIG. 3.13 Illustration of the effects of optical pumping with a+ (left-circularly polarized) light on the populations of ground state Zeeman sublevels for closed J = 1 -+ J' = 0, 1, 2 transitions- (whose populations Pe(M') depend on populations and rates of excitation from the other ground state sublevels).

The basic rate equation for a given ground-state Zeeman sublevel is dp9 (M)

dt = -Weg(M)pg(M) + F sp(M) + 1're.(pg(avg) - p9 (M)] , (3. 195)

where We9 (M) is the excitation rate from a given ground state sublevel IJ, M) for 1r-polarized light and p9(avg) is the average population of a Zeeman sublevel. In

CHANGE IN ABSORPTION DUE TO OPTICAL PUMPING equilibrium dp9(M)/dt = 0, so we have Pg(M) = F,p(M) + 'Yre1Pg(avg) _ Weg(M) + rrel (3.196)

The condition "' << 1 allows us to say that the excitation rate is significantly smaller than the ground state relaxation rate ,rel, so (M)

( )

Fsp(A1)

Weg(M)

Pg ~ Pg avg + ------- - --- .

rrel Trel (3.197)

From the results of Problem 3.4 [Eq. (3.132)], we see that the excitation rate Weg(M) for 1r-polarized light is W': (M) = l(e, J'lldllg, J)l2eij (J, M, 1, OIJ', M}2 eg r'O 2J' + 1 ' (3.198)

where we have made use of the fact that for 1r-polarized light the Clebsch-Gordan coefficients vanish unless M = M' and we have set Ii = 1.

The flux of atoms Fsp(M) spontaneously decaying back to IJ, M) is given by F,p(M) = 'YO 2J' + l ~~ Pe(M')(J',M', 1,qlJ,M} 2 , (3.199)

· 2J+l L,L, M' q where q = 1, 0, -1 to allow for all possible polarizations of spontaneously emit- ted photons. For K << 1, we can follow the same basic approach as applied in part (b) of Problem 3.7 to see that the excited state population Pe(M') is given approximately by (At[') ~ (M') l(e, J'lldllo, J)l2e5 (J, M', 1, OIJ', M') 2 Pe Pg 2J' + 1 r'o (3.200)

( ) I (e, J'l ldl lo, J) 12e5 (J, M'' 1, OIJ'' M') 2 ~ Pg avg 'YJ 2J' + 1 ' (3.20 I)

where we have assumed that since "' is small, the ground state populations do not change significantly. Therefore F (M)

""".J ( ) l(e, J'lldllo, J)1 2e5 •P ~Pg avg 'Yo(2J + 1)

x }:}:(J,M',1,0IJ',M'} 2(J',M',1,qlJ,M} 2 .

(3.202)

M' q From Eqs. (3.197), (3.198), and (3.202), we see that the fractional change in the populations of the ground state Zeeman sublevels ~Pg(M) = Pg(M) - Pg(avg)

Pg{avg)

(3.203)

## INTERACTION OF ATOMS WITH LIGHT

is described by 8p9 (M) ~ [( '"''"' (J,M',1,0IJ',M')2(J',M',1,qlJ,M) )- (J,M,1,0IJ',M)

], ""

~ ~ 2J + 1 2J' + 1 M' q (3.204)

where the saturation parameter "' is defined here to be _ l(e, J'lldllg, J)l2e5 K, = .

(3.205)

101rel Now we are ready to consider the specific cases.

The 1 ~ 0 case: Since there is only one excited state Zeeman sublevel, only one of the ground state Zeeman sublevels, namely M = 0, interacts with the pump light (see Fig. 3.14). Atoms excited to the upper state decay with equal likelihood to any of the ground state sublevels. This can be deduced from the isotropy of space, since atoms in the IO, 0) state are unpolarized, and spontaneous emission cannot create polarization where none previously existed [ otherwise the vacuum, which induces spontaneous emission (Problems 3.2 and 3.3), would have a preferential direction!]. Therefore, the optical pumping process must decrease the population p9(0) and increase p9 (±1).

This reasoning is quickly confirmed using formula (3.204 ): 2K 8p9 (0) ~ -g , K, 8p9 (±1) ~ + g .

(3.206)

(3.207)

It is clear that optical pumping decreases absorption of the excitation light in the 1 ~ 0 case, since the population of the only ground state Zeeman sublevel that interacts with the light (the bright state) decreases, while the populations of states which do not interact with the light (the dark states) increase.

The 1 ~ 1 case: In this case two ground state sublevels (M = 1 and M = -1)

interact with the pump light while the M = 0 sublevel is a dark state (Fig. 3.14).

The IJ = 1, M = 0) ~ IJ' = 1, M' = 0) transition is forbidden because the Clebsch-Gordan coefficient (1, 0, 1, Oil, 0) vanishes (this is derived and explained in Problem 9.5). The transition rates from the M = 1 and M = -1 ground state sublevels are the same, and there is some probability for atoms excited to the upper states to decay to the dark state IJ = 1, M = 0). Thus optical pumping decreases absorption in this situation as well.

CHANGE IN ABSORPTION DUE TO OPTICAL p _j j 1 ➔0 l ➔l : ( ' ~ / ? ,-' ( r 1 ➔2 r'.' ., (- / ; _)

- I M=-2 M=-1 \ ~ c (~ ?

,: C < ( \ ( - - I ' ) s r - I - )

C I _)

} ( I __ )

I _)

•• M= 0 I r ::. . . )

'.

( ,\ ( 1/ M= I

## UMPING

M= 2 FIG. 3.14 Illustration of the effects of optical pumping with linearly polarized (1r) light on the populations of ground state Zeeman sublevels for closed J = I -. J' = o, 1, 2 transitions.

Again, Eq. (3.204) supports our intuitive argument: K 6p9 (0) ~ +- , K 6p9 (±1) ~ -- .

(3.208)

(3.209)

The 1 --+ 2 case: In this case, all three ground state Zeeman sublevels interact with the pump light, i.e., there are no dark states. The strength of the interaction with the pump light varies between the states, as can be seen by comparing the

## INTERACTION OF ATOMS WITH LIGHT

.

pJicated .

.

.

. s sufficiently com appropriate Clebsch-Gordan coefficients. This situation 1 ·t to readily compute that our formula (3.204) will pay dividends, as we can use 1 the relative change in the ground state populations: K, '5pg(O) ~ + 18 ' K, '5pg(±l) ~ - 36 .

(3.210)

(3.211)

sublevel increases, We see that the population of the M = 0 ground state Zeeman while the populations of the other sublevels decrease.

Clebsch-Gordan From Eq. (3.198) we see that the larger the square of the t coefficient (J M I o'tJ' M) 2 the higher the rate of absorption. If one cohmMpu es ' ' ' ' ' . .

· · .. nd that t e = the Clebsch-Gordan coefficients for the 1 -+ 2 trans1t1on, it is iou O 0 sublevel has the largest absorption rate - therefore, in contrast to ~he 1 -.

an . .

.

.

.

1. ht b orption in this case, Just as _,.

trans1t1ons, optical pumpmg mcreases 1g a s for the case of circularly polarized light.

.

.

J -+ J + 1 Note that, because of the effects discussed m this problem, closed transitions only "bleach" when the flux of photons absorbed equals the flux of photons generated by stimulated emission, i.e., when d2efi - 2-rvl.

(3.212)

This is in contrast to J -. J - 1, J transitions which bleach when all the atoms are pumped into dark states, i.e., when (3.213)

,o,re, 3.10 Optical pumping and the density matrix Atoms which are initially in an unpolarized ground state with J = 3/2 are subject to optical pumping with light which is near-resonant with a transition to an excited state with J' = 1/2. Assuming that all atoms excited to the J' = 1/2 state decay to a "trap" state other than the ground state and that other relaxation processes can be neglected, find the 4 x 4 density matrix describing the Zeeman sublevels of the J = 3/2 state after the optical pumping is complete (see Appendix G for more details about the density matrix, as well as a discussion of the polarization moments created by optical pumping in the case considered here). Consider the following two cases of light polarization: (a) left circular polarization (a+),

## OPTICAL PUMPING AND THE DENSITY MATRIX

(b) linear polarization along z, (c) linear polarization along x.

Solution (a) In this case, the states with MJ = -3/2 and MJ = -1/2 w·ll pumped out and the remaining two sublevels wiJJ not be affected ~ be ~ornpJeteJy ing in any way (Fig. 3.15). Choosing the nonnalization in such Y 0 PticaJ purnp- initial population for each Zeeman sublevel is equal to one we a way that the final ground state density matrix: ' can Write for the 1 0 0 0 1 0 0 p= 0 0 0 ' 0 0 0 0 (3.2J4)

where the matrix indices correspond to the MJ components in decreasi·n g OJi er.

(b) In this case, the light couples states with MJ = M~. so the MJ = ±l/ 2 state~ are depleted (Fig. 3.16). Thus we have for the resultant ground state density matnx: 1 0 0 0 0 0 0 0 p= 0 0 0 0 0 0 0 (3.215)

(c) Here, it is sufficient to notice that all atoms get pumped out of the ground state except the ones that are in the two possible x-nonabsorbing (dark) states /"Pf) that are formed by coherent superpositions of the sublevels pairs MJ _ M_,== -3/2 M.,== ~= 1/2 M_,= 3/2 FIG. 3.15 Optical pumping of a J = 3/2 -+ J' = 1/2 transition with Jeft-circularJy polarized light.

## INTERACTION OF ATOMS WITH LIGHT

I I( M.,= 1/2 ~= 3(2 i;,,c. 3-16 Optical pumping of a J = 3/2 -+ J' = 1 /2 transition with linearly polarized light.

M.,-1/2 M=3/2 'J Fie. 3. I 7 Optical pumping of a J = 3 /2 ---. J' = 1 /2 transition with x-polarized light.

--3;2, MJ = 1/2 and MJ = -1/2, MJ = 3/2 (Fig. 3.17). This effect, where tPUlation remains in a superposition of Zeeman sublevels even though all the eman sublevels are coupled to the light field, is known as coherent population trapping. As we shall see, despite the fancy name, the only difference between this ca~ and the one considered in part (b) of the problem is the choice of quantization ax.is.

An atom is in a dark state 11/Jd)

when the El-amplitudes of excitation to the Upper state sublevels are zero, i.e., (J' = 1/2, M~ = ±1/21 ee(t)r. € l'l/Jd)

= 0 .

(3.216)

~ere H = -d • l(t) = ef.(t)r. € is the Hamiltonian describing the atom-light Interaction, € is the light polarization vector, and for M~ = 1 /2, l1Pd) = C-1;2IJ = 3/2, MJ = -1/2) + C3;2IJ = 3/2, MJ = 3/2), (3.217)

and for M~ = -1/2 l1Pd)

= C_3;2IJ = 3/2, MJ = -3/2) + C1;2IJ = 3/2, MJ = 1/2) . (3.218)

The interaction Hamiltonian can be written in terms of spherical tensors in order to take advantage of the Wigner-Eckart theorem (Appendix F). In this case

## OPTICAL PUMPING AND THE DENSITY MATRIX

t = x, so we can use Eqs. (F.23) and (F.25) to write x = v'2(r_ - r+), thus

## I

(3.219)

(3.220)

where r ± are the q = ± l components of the vector operator r in the spherical basis.

Returning to Eq. (3.216) and using the Wigner-Eckart theorem (F. I)

( J , 111' I I . )

( J' 11 r 11 J)

, , , 1• Jr± J, MJ = J2J, + l (J, MJ, 1, ±llJ, MJ)

(3.221)

along with Eqs. (3.217) and (3.218), we obtain the conditions (3/2, 3/2, 1, -111/2, 1/2)C3;2 - (3/2, -1/2~ 1, lll/2, 1/2)C-1;2 = 0, (3.222)

(3/2, 1/2, 1, -111/2, -1/2)C 1;2 - (3/2, -3/2, 1, 111/2, -1/2)C_3/2 = 0.

(3.223)

These Clebsch-Gordan coefficients have the following values: (3/2, 3/2, 1, -111/2, 1/2) = v'2 , from which we obtain (3/2, -1/2, 1, 111/2, 1/2) = ~, (3/2, 1/2, 1, -111/2, -1/2) = ~, (3/2, -3/2, 1, lll/2, -1/2) = v'2, C-1/2 = C3;2v'3, C1;2 = C_3;2v'3.

(3.224)

(3.225)

(3.226)

(3.227)

(3.228)

(3.229)

We can also construct two linear combinations of the Zeeman sublevels which are orthogonal to the dark states l·l/Jf); these will be bright states, which - by analogy with part (b) - will be completely depleted by the optical pumping. We

## INTERACTION OF A10MS WITH LIGHT

can find the correct normalization for the density matrix by using the fact that the dark states each have unit population before and after optical pumping. Thus, we find p= -4 v'3 v'3 v'3 v'3 (3.230)

We note that this solution can also be obtained by rotating the density matrix obtained in part (b) by 1r /2 about the y-axis (using the appropriate quantum mechanical rotation matrix - see Appendix E). Indeed, the dark states 11/Ji)

are simply found by applying such a rotation to the states IJ = 3/2, MJ = ±3/2).

3.11 Cascade decay Consider an atom which has an excited state la) of the same parity as the ground state lg) (Fig. 3.18) which decays to an opposite-parity state lb) which in tum decays to the ground state. Suppose initially states la) and lb) are not populated.

Then at time t = t0 , la) is instantly populated. Suppose also that in an experiment, one detects fluorescence on the lb) --+ lg) transition and the detection system is insensitive to fluorescence at the wavelength of the la) --+ lb) transition.

(a) Derive the time dependence of the fluorescence signal in terms of the lifetimes of states la) and lb) (Ta and Tb, respectively).

(b) Analyze the limiting cases: Ta >> Tb, Ta << Tb, and Ta ~ Tb- b FIG. 3.18 Levels and transitions involved in a cascade decay (see text).

## CASCADE DECAY

1 5 Time (µS)

FIG. J.19 Fluorescence on the Dy lb) --+ lg) transition as a function of time (the fluorescence peak appears upside down in the figure because the output of the photomultiplier has negative polarity).

(c) Will the above analysis change if la) has additional decay channels to states other than I b) ?

(d) Figure 3.19 shows actual data from an experiment with atomic dysprosium (Budker et al. 1994). The state la) (E = 19797.96 cm- 1) was populated with a sequence of two short (duration rv7 ns) laser pulses. Fluorescence on the lb) -+ lg)

transition was detected with a fast photomultiplier. An interference filter was used to select fluorescence on the lb) --+ lg) transition at 564 nm. The data points on the figure were fit to the expected time dependence (derived in part (a) of this problem); the free parameters of the fit were: t0 , the overall signal amplitude, Ta, and Tb· Using the figure, estimate Ta and Tb.

Solution (a) Let us designate the populations of the states la) and lb) as Pa and Pb, cor- respondingly. The population of la) exponentially decays due to spontaneous emission to lb), therefore: Pa ( t) = Pa( to)e-(t-to)/T,, • (3.231)

The differential equation describing the time dependence of Pb(t) has a term describing population of lb) via spontaneous emission from la) and depopulation

INTERACl1ON OF ATOMS WITH LIGHT of lb) by decay to the ground state: Pb e-(t-to)/ru Pb Pb(t) = -pa(t) - - = Pa(to)--- 'b Ta Tb (3.232)

Equation (3.232) is an inhomogeneous linear differential equation. Its solution is the sum of the general solution of the homogeneous equation Pb(t) = _Pb (3.233)

Tb and a particular solution of Eq. (3.232). The latter can be found by forcing upon Pb(t) a time dependence of the form e-<t-to)/-r,.. The constant factors in the solu- tion of Eq. (3.232) are determined by the initial conditions: Pb(to) == O and Pb(to) = Pa(to)/r 0 • One therefore arrives at the following expression for Pb(t): Pb(t) = Tb Pa(to) (e-(t-to)/ru _ e-<t-to)/rb) .

(3.234)

Ta -Tb The fluorescence signal J= observed in the experiment is proportional to the rate at which atoms return to the ground state from lb) (this is the number of photons per second emitted on the lb) ---+ lg) transition): (3.235)

(b) If Ta << Tb, the atoms quickly (i.e., during time rv Ta) decay into state lb) and the trailing edge of the fluorescence pulse will be an exponential determined by Tb· If Ta >> Tb, the "bottleneck" is the decay of la) and at t >> Tb fluorescence decays with time constant Ta.

To analyze the case Ta ~Tb~ T, set Ta =Tb+ 6T. Then from Eq. (3.234) we have: Pb(t) ::::: ;TPa(to)e-(t-tn)/-r ( 1 - e-,h(t-tn)/-r )

~ ~p (t )e-<t-tn)/-r 6r( t - to)

,.._ 6T a o r2 ::::: (t - to) Pa(to)e-<t-to}/-r, T where we used the Taylor expansion of the exponential valid for 6T(t - to)/T 2 << 1.

(3.236)

For greater t's, the fluorescence signal just decays exponentially. Therefore, even though Eq. (3.235) may look somewhat singular at Ta = Tb, nothing special happens in this limit.

## COHERENT LASER EXCITATION

(c) The fluorescence signal time dependence will be the same except for the overall normalization.

(d) For the shown data, Ta = 7.9 µs, Tb = 2.2 µs. Note, however, that Eq. (3.235)

is symmetric with respect to interchange of states la) +-+ lb). Therefore there is no way to know which of the lifetimes is shorter without additional information about the system (e.g., detection of fluorescence on the la) ~ lb) transition).

## 3.12 Coherent laser excitation

Consider a J = 0 --+ J' = 1 atomic transition which is closed in the sense that all atoms excited to the upper J' = 1 state decay back to the lower J = 0 state.

Suppose that the atoms are illuminated with cw, narrow-band, resonant light which is a+-circularly polarized and that the saturation parameter (Problem 3.7) is very large: K >> 1, for example, "' = 1 000.

(a) What are the time-averaged probabilities of finding atoms in each of the four Zeeman sublevels: 11, 0), 11, ±1) and I0, 0)?

(b) Same as in part (a), but now suppose that the light, rather than being purely circularly polarized, has a small coherent admixture of the opposite ( a - ) circular polarization. The intensity of the a_ admixture is 1 % of the intensity of the a+ light.

(c) Same, but now assume that the a+ light is blocked out with a circular polarizer, so the atoms only see the a_ light of the same intensity as in part (b ).

Solution (a) No atoms are excited to either of the I 1, -1), I 1, 0) sublevels, so their popula- tion is zero. On the other hand, the transition between the I0, 0) and I 1, 1) sublevels is fully saturated (Problem 3. 7), so the time-averaged population is approximately I /2 in each of the sublevels, assuming that the total population is one.

(b) The light now excites a coherent superposition of the I 1, ± 1) upper state sub levels of the form 'lp e ~ I 1 , 1) + a I 1, -1) , (3.237)

where lal2 = 0.01, and the phase of a is determined by the relative phase of the two coherent circular components of the light.

Because the overall light intensity is as large as in part (a), the transition is still saturated, so the upper state (3.237) has time-averaged population ~ 1 /2 and the populations of the I 1, 1) and I 1, -1) sublevels are ~ 1 /2 and ~ 0.01 x 1 /2, respectively.

## INTERACTION OF ATOMS WITH LIGHT

(c) The light now excites only the I 1, -1) upper state sublevel. Since 1 % of the a+ intensity still corresponds to a large saturation parameter K = 0.01 x 1 000 = 10, the time-averaged population of the I 1, -1) sublevel is ~ 1 /2.

A similar increase in the population of this sublevel compared to part (b) can be achieved if instead of blocking the a+ component a magnetic field is applied that splits the J' = 1 sublevels and the light frequency is tuned to be in resonance only with the I 1, 0) ~ I 1, -1) transition.

The comparison of the cases (b) and (c) shows that the rate of a light-induced transition (in this case, I0, 0) --+ I 1, -1)) strongly depends on the presence of a resonant light field applied to an adjacent transition (in this case, I0, 0) ~ I 1, 1) ).

This effect belongs to a broad class of phenomena which includes electromagnet- ically induced transparency (Kocharovskaya 1992, Harris 1997) and are based on coherent interactions of multicomponent light with multiple states of a quantum system (atoms, molecules, solids, nuclei).

## 3.13 Transit-time broadening

A beam of atoms moving with velocity v = vx crosses a laser beam propagat- ing along y. The cw narrow-band laser beam has frequency WL, its z-dimensions are greater than those of the atomic beam, and its intensity is I ( x, z) = 10 for -w < x < w and zero elsewhere. Assume that the laser light is of sufficiently low intensity so that all saturation effects can be ignored. Also assume that the density of atoms in the beam is low enough so that the atomic beam may be treated as an optically thin medium.

(a) Estimate the broadening of the absorption line due to the finite time of interaction between atoms and the light (transit-time broadening).

(b) Suppose the laser is tuned to a transition between the atomic ground state and an excited state (separated in energy by hwo) with radiative lifetime r. For v = 5 x 104 cm/sand diameter 2w = 1 mm, estimate for which values of r transit-time broadening effect will dominate the line width.

(c) Using a classical and/or quantum mechanical picture, explain the additional lobes on the spectral profile of a transit-broadened line (see Fig. 3.20). Assume that the lifetime of the excited stater greatly exceeds the transit time rv 2w /v.

(d) What is the spectrum of a transit-broadened line if we instead assume a Gaus- sian spatial profile for the laser beam, i.e., I(x, z) = Ioe- 2x 2 /w 2 ? (The factor of 2 appears in the exponent because the beam radius is conventionally defined to correspond to the 1/e level for the electric field amplitude.)

## TRANSIT-TIME BROADENING

Solution (a) An atom traversing the laser beam "sees" a pulse of radiation with a duration 2w / v. This means that the effective radiation spectrum is broadened according to the uncertainty condition Therefore, DavD.t rv - .

21r V D.Vtransit rv • 7rW (b) For v = 5 x 104 cm/sand 2w = 1 mm, this corresponds to Davu-ansit rv 0.1 MHz.

The radiative width is Davradiative = -2 .

7r'T Therefore, the transit broadening dominates when I r»2µs. I (3.238)

(3.239)

(3.240)

(3.241)

(3.242)

(c) Suppose that the laser light phase is such that its electric field at the atom is e(t) = to cos(wLt). The intensity spectrum of this radiation can be found by (1)0 Frequency FIG. 3.20 Absorption spectrum for atomic transition where the lineshape is due to transit-time broadening.

## INTERACTION OF ATOMS WITH LIGHT

taking the Fourier component: 13 t=w/v I . t' I e(w) = eo cos(wLt )e-tw dt ' t=-w/v (3.243)

and evaluating the quantity I(w) ex: e (w )£(w )*. One finds, after some math, that sin 2 [(w - WL)w/v]

I(w) ex: ( )2 •

## W-WL

(3.244)

This function is centered around the laser frequency w L. If one scans the laser light frequency through the atomic resonance, the absorption spectrum [resulting from the spectral intensity distribution (3.244)] is that shown in Fig. 3.20 (in the limit where T >> w/v).

The lobes on the spectral profile are analogous to those that appear in the diffraction of light from a thin slit. In the case of a thin slit, the properties of a monochromatic field are modified by limiting the extent of the field in space, while in transit-time broadening, the properties of the field are modified by limiting the extent of the field in time.

(d) In this case, the time-dependent electric field seen by atoms passing through the laser beam is given by 2t2 / £(t) = £0 COS (wLt)e-v w , (3.245)

where we have transf onned the spatial dependence of the laser beam intensity into the time-dependence of the electric field by setting e ( t) equal to the square root of I(x = vt, z). As in part (c), we take the Fourier transform of £(t): e(w) = 1_: eo cos (wLt')e-v 2t' 2fw~ e-iwt' dt', (3.246)

and for I(w) ex: £(w)£(w)* we obtain I(w) ex: e-w2(w-w, .. )2/(2v2)

' (3.247)

where we have ignored far-off resonant terms involving factors of exp[-w 2(w + wL)2 /(2v 2)]. Thus the spectral profile in this case is a Gaussian. Note that the 13 The Fourier transform or the spectral distribution of an arbitrary time-dependent function F( t)

is defined as F(w) = L: F(t)e-iwtdt.

The inverse transformation is

A QUIZ ON FLUORESCENCE AND LIGHT SCATTERING intensity drops to the 1 / e point at lw - w LI = v'2( v / w ), whereas the first zeros of the profile shown in Fig. 3.20 occur at lw - wLI = 1rv/w.

3.14 A quiz on fluorescence and light scattering Here we present a collection of conceptual questions that are designed to test one's understanding of several key ideas in spontaneous emission and scattering, and help develop intuition in these subjects. In order to minimize possible confusion, we attempt to clearly specify a physical situation to which the question pertains, although the concept illustrated by the question may be of a more general nature.

Testing these questions on our colleagues (and ourselves) has convinced us that some of the questions may not be as trivial as might seem at first glance.

(a) A free two-level atom at rest in its ground state is irradiated by a pulse of off-resonant radiation with a Gaussian temporal profile. The light is nearly monochromatic, with spectral width limited by the finite duration of the pulse.

The light frequency detuning from resonance greatly exceeds both the radiative width of the upper state and the inverse duration of the light pulse. The excitation light can be considered arbitrarily weak. A photodetector detects photons scattered in a direction not along the direction of excitation light propagation.

Suppose that with the set up described above, it is found that the probability of detecting a scattered photon is P. How would this probability change if instead of a single atom we had two? Assume that the atoms are initially localized to a spatial region with linear dimensions much smaller than the reduced wavelength of the light A/21r. (The initial localization is the same as for the case of one atom.)

Assume that for the excitation pulse duration r, we have: Mc~x T << n/JJ (3.248)

where M is the mass of an atom, ~x is its initial localization, and that the two atoms do not interact with each other in the absence of light. What if we have N atoms?

(b) N >> 1 atoms are prepared as above, except they are all in the excited rather than the ground state. No light pulse is applied. How does the radiative decay time depend on N?

(c) N atoms are prepared as above, in the ground state; one atom in the excited state is added to the system. No excitation pulse is applied. How does the presence of the N ground state atoms affect the decay?

## INTERACTION OF ATOMS WITH LIGHT

(d) N atoms are prepared as above, in the ground state. A single resonant photon is sent into the sample and absorbed, creating one excitation among our N atoms.

How does the radiative decay time for this excitation depend on N?

(e) Same as (a), but the atoms are now three-level systems, and the detector is equipped with a color filter, so it is only sensitive to light resulting from Raman scattering into the third level.

(f) In the parts above we have assumed that the N atoms are prepared at zero temperature so their initial motion is only due to spatial localization. How would these results change for atoms of finite temperature? Assume that the excitation pulse is still much shorter than the inverse Doppler width of the transition.

(g) In the parts above we have assumed that the N atoms are free. What if they are confined in a trapping potential? Assume that the energies of the internal excita- tions (the upper and the third level) greatly exceed the energy associated with the confining potential.

(h) Weak resonant monochromatic light is scattered in a direction other than for- ward by a single two-level atom (scattering and resonance fluorescence are the same process in this case). Is the scattered radiation coherent with the input radi- ation? In other words, is it possible to observe steady interference fringes by combining the scattered light and a portion of the input light, for example, on a distant screen? Neglect atomic recoil.

Solution (a) The probability of detecting a scattered photon is four times larger in the case of two atoms (or oc N 2 in general). With the conditions specified in the question, it is impossible, even in principle, to determine which of the two atoms scattered a photon, and thus the amplitudes for scattering on the two atoms interfere construc- tively. The condition (3.248) is specified so that the Doppler broadening that arises due to atomic motion ( cf., for example, Problem 8.1) which is, in tum, due to the atoms' initial localization, is much smaller than the spectral width of the excit- ing and scattered light. Note also that the initial localization of atoms in a volume with linear dimensions smaller than the wavelength ensures that the initial momen- tum uncertainty (rv n/ ~x) exceeds the momentum kick due to photon scattering ( rv hw / c), and thus, it is impossible to say which atom scattered a photon based on its momentum after scattering.

(b) The questions (b) and (c) were originally formulated and answered in a sem- inal paper by R.H. Dicke (1954), which forms the basis of an entire subfield of modem optics and spectroscopy [see, for example, the monograph by Andreev et al. (1993)].

A QUIZ ON FLUORESCENCE AND LIGHT SCATTERING The answer to question (b) is that the excited state radiative lifetime will be ~ To/ N, where To is the radiative lifetime of an isolated atom. This is a cooperative emission effect that is known as Dicke superradiance. Its origin can be understood in the following qualitative way. At first, after the atoms have been prepared in the excited state, they "do not know" about each other, and their spontaneous emission proceeds independently. Because we have N atoms, the first flourescent photon appears after a characteristic time To/ N. Because the photon is produced where all the atoms are localized, and the atom-photon interaction cross-section is ,\2 /21r (see Problem 3.5), the first photon interacts with the system of atoms, causing the individual atomic dipoles to phase in, 14 thus inducing an "avalanche,"

which depletes the upper state population nearly instantaneously.

Note that since the number of emitted fluorescence photons is N, and the emission time is rv To/ N, the emission intensity is rv N 2 that of a single iso- lated atom. 15 A calculation [see Andreev et al. ( 1993), Sargent et al. (1977), and Allen and Eberly ( 1987)] shows that the peak intensity is N 2 / 4 of the single-atom intensity for N >> I.

(c) The presence of the ground state atoms affects the decay in an essential way: while the initial transition probability is the same as for a free excited atom, the overall probability of emitting a photon is 1 / N. This means that the radiation is mostly utrapped" within the medium for N >> 1. How can it be that one atom in the system is excited (we do not know which one because the atoms exchange their excitations through the electromagnetic field) but the system never radiates?

Actually, this is a purely classical effect. Assume there are two co-located iden- tical classical dipoles that can only lose their energy through radiation. There are two modes of the system's oscillation: the symmetric mode where the two dipoles oscillate in phase, and the antisymmetric mode where they oscillate with a phase shift of 1r. Clearly, the energy is radiated in the symmetric mode but there is no radiation at all for the antisymmetric mode. If a system is prepared with one dipole initially excited (i.e., a superposition of the symmetric and antisymmetric mode), half of the energy is radiated, while the remaining energy is stored in the antisym- metric collective oscillation of the two dipoles. For the case of N oscillators, the 14 Detailed theoretical treatments (Andreev et al. 1993) make a distinction between the interac- tions between the atoms through the radiation field that establish collective emission and stimulated emission.

15 Here we assume that the spectral width of the emitted radiation "" N /To is much smaller than the transition frequency. Also. because pulse shonening due to collective emission leads to spectral broadening, one may wonder how the energy balance is preserved. The explanation lies in the fact that the initial state has to be prepared in a short time compared to the emission time, for example, with a short pulse of radiation bringing each atom from the ground to the excited state (such an inverting pulse is called a "1r-pulse.") Because this pulse is short, there is inevitably an uncertainty in the energy of its photons, so there is no problem with the overall energy balance.

## INTERACTION OF ATOMS WITH LIGHT

solution of the classical problem [ see, for example, Andreev et al. ( 1993)] shows that N - 1 out of the total N modes do not radiate.

The quantum mechanical treatment developed by Dicke ( 1954) uses the notion of the collective pseudospin for the ensemble of N two-level atoms. The analogy with the real spin becomes obvious if instead of free two-level atoms, one thinks of spin-1/2 particles with magnetic moments placed in a uniform magnetic field (Allen and Eberly 1987). N atoms, all in the ground state, correspond to a sym- metric wavefunction with the pseudospin projection - N /2, while N atoms, all in the excited state, correspond to a symmetric wavefunction with the pseudospin projection N /2. Clearly, both these wavefunctions correspond to the total pseu- dospin of the system of N /2. It is straightforward to show that dipole transitions are only possible between states of the same total pseudospin. This has an immedi- ate consequence that out of the total N possible states with a single excited atom, only one (the totally symmetric state) can decay to the ground state with no atomic excitations. This is analogous to the classical result discussed above.

We have explained why the overall probability of the photon emission is 1 / N.

In part ( d), we will show that the only state with a single excitation that can radiate, the symmetric state, has a dipole moment coupling it to the ground state which is '1N times larger than that for a single atom. Thus the symmetric state with a single excitation radiates with N times higher intensity than a single excited atom. Since the weight of this state in the initial state is 1 / N, the total initial intensity is the same as for an isolated excited atom. On the other hand, since the total radiated energy is N times smaller, this also means that the characteristic emission time is ro/N.

(d) Each of the atoms in our sample upon absorption of the photon is prepared in a coherent superposition of the ground and excited states. The amplitude of the excited state in this superposition is 1/ '1N, so that summing the probability of finding the atoms in the excited state over all atoms we get one.

A coherent superposition of the upper and lower atomic states corresponds to a dipole moment (in this case, of amplitude 1 / '1N of its maximum value) oscillating at the frequency of the transition. We have N such dipoles that oscillate coherently.

Adding all the amplitudes and squaring, we get ( N · 1 / m)2 = N. Thus the intensity of the emission is enhanced by a factor of N compared to the case of an isolated atom, and the radiative decay time is decreased by N.

(e) In this case, the scattering probability scales linearly with the number of atoms.

Since the scattering process leaves an atom in a state different from its initial state, it is possible to tell exactly which atom scattered the light by doing an additional measurement after the fact. Thus, scattering amplitudes involving different atoms do not interfere.

## TWO-PHOTON TRANSITION PROBABILITY

(f) None of the results above change for atoms of finite temperature assuming that the excitation pulse is much shorter than the inverse Doppler width of the tran- sition. We note that in recent years, quantum degenerate atomic vapors, and in particular, Bose-Einstein condensates, became a new laboratory for experimen- tal investigation of collective emission and scattering processes, as reviewed by Ketterle and Inouye (200 I).

(g) The atoms occupy the energy levels of the confining potential, not necessarily one and the same level. 16 The Doppler width considerations are irrelevant in the case of a sufficiently strong potential, but the previous results remain valid if an atom scattering a photon is most likely to remain in the same energy level of the potential upon scattering [so that we still cannot tell which atom scattered the pho- ton, except for the case of part (c)]. The condition for this is that the recoil energy for an isolated atom is much smaller than the interval between adjacent energy lev- els of the trapping potential. This is completely analogous to the Mossbauer effect - the absence of recoil in nuclear emission/absorption of gamma rays when the emitter and absorber are part of a crystalline lattice [see, for example, Wertheim (1964)].

(h) The scattered light is indeed coherent with the excitation light, i.e. their rela- tive phase is not random. This can be understood from the fact that the scattered radiation is produced by the atomic dipole (corresponding to a superposition of the ground and excited states) whose oscillation frequency and phase are determined by the driving field. This is in contrast to the spontaneous emission for an atom initially prepared in the excited state, for which the phase of the emitted light is random. A detailed discussion of coherence properties of scattered and resonance fluorescence light is given in Chapter 8 of the book by Loudon (2000).

3.15 Two-photon transition probability Consider the system of energy levels shown in Figure 3.21. Estimate the two- photon transition probability for excitation of atoms from state Ii) to state I/) upon the action of two light fields of frequencies w 1, w2. Assume that the Ii) --+ lk) and lk) --+ I/) transitions are electric-dipole (El) allowed with transition moments dik and dk/, respectively. Neglect Doppler broadening, and assume the condition of two-photon resonance: (3.249)

In general, two-photon transitions arise in second-order perturbation theory, with the electric field of the light as the perturbation. Their amplitude contains 16 The maximum occupation number depends on whether the atoms are fermions or bosons.

## INTERACTION OF ATOMS WITH LIGHT

l/;--~- ____ !1k ----lk (a)

(b)

................

FIG. 3.21 Energy levels involved in a two-photon transition. Cases (a) and (b) differ by the order of absorption of photons with frequencies w1 , w2.

two terms, which are different in the order of absorption of the w1 and w2 photons [Figures 3.21(a) and (b)]. For simplicity, let us consider the case where (3.250)

so the term with an w 1 photon absorbed first [Figure 3.21(a)] dominates over the term where it is an w2 photon that is absorbed first [Figure 3.2l(b)]. Also, we assume that for single-photon detuning a = hw1 - (Ek - Ei) = EI - Ek - hw2, we have l~I >> rk, where rk is the natural width of the intermediate level.

Solution If only the first light field is present, the atoms undergo Rabi oscillations with frequency (3.251)

and the maximal amplitude of finding atoms in the state lk) is dike 1/(Mli)

(see Problem 3.1 ). Here e 1 is the electric field amplitude of the w1 light. Therefore the time averaged probability (Pk) to find an atom in lk) is (~ ) = ! dlke~ k 2 1i2fl~ .

(3.252)

Since now there is nonzero amplitude to find the atom in state lk), there appears the possibility for an atom to absorb an w2 photon and go to the state I/).

It is interesting to abandon for a moment the two-photon resonance condition (3.249) and discuss the absorption spectrum of such a system with respect to tuning of w2. From energy conservation, it is clear that there is absorption only when the condition (3.249) is satisfied (to within the transition linewidth); othetwise,

## VANISHING RAMAN SCATTERING

lbe~e is no absorption (including for hw2 = E1 - Ek), since then there would be an lll~balance between the energy of the two absorbed photons and the energy of ~tomic excitation. It is often said that in the presence of the field w 1 a virtual state •s excited (dashed lines in Figure 3.21 ), which is essentially state lk), except its energy is Ei + hw1.

According to this picture, we can consider the next stage of the excitation pro- cess as a single photon transition from the resonant virtual state to I/). Assuming th~t the Rabi frequency for this second stage is much smaller than the natural width of the final state r 1 (so that the system is in the overdamped regime, see Problem 3.1 ), the transition rate (the number of two-photon absorption events per atom per unit time) is given by (3.253)

(The factor of 1 /2 comes from the time-averaged population of the intermediate state [Eq. (3.252)].)

This expression shows that when both light fields are weak, the two-photon transition rate scales as the product of their intensities. For high intensity of the w1 light such that (dikei)

2 >> ~ 2, the transition rate becomes independent of the intensity of this field (saturation). Although formula (3.253) does not show saturation for strong w2 light, this is a consequence of an implicit assumption that we made in the derivation: namely, that the w2 field is sufficiently weak as not to affect the evolution of the two-level system consisting of states Ii) and lk)

in the presence of the w 1 field. A detailed calculation that does not rely on this assumption (Ter-Mikaelyan 1997) shows that in fact the two-photon transition rate as a function of the w2 intensity (for a given weak w 1 field) also saturates when ( dk/£ 2 ) 2 >> ~ 2 . It is interesting to note that when one of the fields w1, w2 is weak, the two-photon transition rate cannot exceed the resonant single-photon transition rate corresponding to the weak field, no matter how strong the other field is.

Various other aspects of two-photon transitions are discussed by, for example, Krainov et al. ( 1997).

3.16 Vanishing Raman scattering Raman scattering is a process in which a photon is removed from the incident light beam, and a photon of a different frequency is emitted. The atoms or molecules of the Raman medium are transferred to states other than the initial one in the process of scattering. Consider Raman scattering for a model energy level system

INTERACl1ON OF ATOMS WITH LIGHT shown in the absorption-emission diagram of Fig. 3.22. Using the Feynman dia- gram technique (Appendix H), write down the amplitude of the process. Show that this amplitude vanishes when the energy of the "'2P" level is exactly in the middle between the energies of "'2S" and 0 1S." The electric dipole transition amplitude between 1S and 2S is zero.

Solution The two possible Feynman diagrams (see Appendix H) for this process are shown in Fig. 3.23. The overall amplitude of the process is therefore (3.254)

2S 2P 1S FIG. 3.22 Raman catt rin in m d I y t m.

2S ..

2S ro ..

2P 2P I ro OJI ,,.J JS 1S FIG. 3.23 Feynman diagrams corresponding to the process depicted in Fig. 3.22.

EXCITATION OF ATOMS BY OFF-RESONANT LASER PULSES where we set Eis = 0 and dmn designates the corresponding dipole amplitude.

Energy conservation requires li(w1 - w2) = E28. With this, it is immediately seen from Eq. (3.254) that the amplitude vanishes when E2s = 2E 2p.

Note that when w1 is much greater than the energy level splittings between the 1S, 2S, and 2P levels. all energy differences between the levels are effectively zero. Thus Raman scattering also vanishes in the high frequency limit.

## 3.17 Excitation of atoms by off-resonant laser pulses

Consider two-level atoms ( originally in state 11)) interacting with an off-resonant laser pulse (Fig. 3.24). Suppose that the temporal profile of the pulse is Gaussian with full width at half maximum (FWHM) of T. Suppose further that the light, although it is near resonant, is well-detuned from the resonance so that ~ >> 1 / r, where ~ is the detuning. Assume also that r << 1 /r, where r is the total radiative width of the upper state.

(a) Assuming weak intensity of the light, estimate the probability of finding atoms in state 12) after the pulse is essentially over but the state 12) has not had time to decay via spontaneous emission. Discuss the dependence of this probability on ~- The partial width for the 12) --+ 11) decay is r p• (b) Discuss power broadening (see Problem 3.7) of the excitation spectral profile.

(In other words, how does the excitation line width scale with light power at high powers?)

FIG. 3.24 Excitation of atoms with an off-resonant laser pulse.

## I

INTERACflON OF ATOMS WITH LIGHT Note: This problem is based on the results of Makarov ( 1983); see also Letokhov ( 1987), Chapter 2.

Solution (a) Although atoms may undergo absorption-emission cycles while the light pulse is on, they should always return to the initial state after the pulse is over if we only consider one- and two-photon processes. A two-photon process must return the system to its original state in this two-level approximation, 17 while a process where a photon is absorbed from the laser beam and the atom remains in the upper state after the pulse is over is forbidden by energy conservation. This is an example of adiabatic evolution where the system follows the quantum state as it evolves under a time-dependent perturbation, and thus returns to the initial state after the perturbation subsides.

A nonzero excitation probability arises in the next order of perturbation theory, i.e., we need to consider a three-photon process: two laser photons are absorbed , and one photon is spontaneously emitted. Because the energy of the spontaneously emitted photon is not restricted to coincide with the frequency of the laser light, the three-photon process could be exactly resonant (or, more precisely, resonant within the width r), which allows the system to satisfy energy conservation, or, in other words, removes the condition of adiabaticity of the process.

Possible Feynman diagrams (see Appendix H) for a three-photon process where two laser photons (wl) are absorbed and one photon (ws) is spontaneously emitted are shown in Fig. 3.25. Of these diagrams, the diagram C is the most important because of the resonant enhancement of the corresponding amplitude: d3f,r£s V21 ~ V21 ( C) ~ r,,2 tl.2 .

(3.255)

Equation (3.255) shows that the probability of finding atoms in state 12) scales as ~ - 4 with respect to detuning. This should be contrasted, for example, with the more familiar Lorentzian line shape that gives a transition probability in the case of continuous wave monochromatic excitation whose wings drop as~ - 2 • The probability of finding atoms in state 12) after the laser pulse can be calcu- lated from the amplitude of Eq. (3.255) as discussed in Appendix H. Instead, we estimate this probability from the following qualitative argument.

We can view the excitation to the upper state 12) as a three-stage process.

First, the atom begins in state 11), the laser pulse smoothly "turns on," and the atom now has a probability d2f} /(~ 2) of being in the upper state (see Problem 3.1 ). However, if no spontaneous emission occurs during the pulse, the atom will adiabatically return to 11) once the pulse smoothly turns off.

17 We also neglect processes where, for example, an M 1 spontaneous photon is emitted.

EXCITATION OF ATOMS BY OFF-RESONANT LASER PULSES ~ (A)

w (B I w, ..

w, U)

I (J)/ WI ..

(C)

I U)

ro, FIG. 3.25 Feynman diagrams corresponding to three-photon processes where two laser photons are absorbed and one photon is spontaneously emitted. The diagram c is resonantly enhanced with respect to the diagrams A and B.

Thus we require a second ~tage: ~pontam~~us emission from 12) back to II)

during the pulse to break the achabat1c1ty condttton. The probability p spont for such a spontaneous emission event is the product of the population of 12) during the pulse, the spontaneous decay rate r p, and the duration of the pulse: (3.256)

If such an event occurs, at this instant the atom is reset to state I I) while the light field is still on.

## INTERACTION OF ATOMS WITH LIGHT

spontaneous emission event Time FIG. 3.26 A sketch of the temporal profile of the penurbation experienced by an atom which suddenly spontaneously decays back to the ground state 11) during the laser pulse. The sudden change in the perturbation breaks the adiabatic condition, allowing the transition to Proceed.

Finally, the third stage is excitation back to 12), but in such a way that the atom remains in 12) after the pulse is smoothly turned off. An important point regarding this third stage is that the perturbation trying to excite the atom to 12) has a temporal profile that looks like the sketch in Fig. 3.26. Because the perturbation appears to be "suddenly" switched on, the probability to end up in the excited state is,...._, d2£f /(2~ 2). One way to see this: the perturbation being suddenly turned on is equivalent to the pulse being suddenly turned off (for which the answer is more obvious).

Combining all these factors, we get for the probability (3.257)

(b) Power broadening occurs when df,l becomes comparable to Ii~, and thus the latter is no longer the largest relevant energy scale in the problem. With a given value of df,l, the detuning ~ * beyond which the probability of finding atoms in state 12) is described by Eq. (3.257) is thus given by ~ * ,...._, d£,/ Ii, i.e. the spectral width of the resonance scales as the square root of the pulse intensity, the usual scaling for power-broadened resonances [see Problem 3.7, Eq. (3.173)].

3.18 Hyperfine-interaction-induced magnetic dipole (Ml)

transitions Consider one-photon transitions between nS 1;2 and n' S1;2 states of the same par- ity (n, n' are the principal quantum numbers; n -:/= n') in an atom with a single

## HYPERFINE-INTERACTION-INDUCED

MAGNETIC DIPOLE (MI) TRANSITIONS s-electron above the closed shells, for example, the 6S 1; 2 --+ 7 S 1; 2 transition orig- inating from the ground state of Cs. The parity selection rule forbids this transition from proceeding as El; the magnetic (Ml) amplitude turns out to be strongly suppressed as well. In fact, the magnetic dipole Hamiltonian is given by (see, for example, Problem 1.4): HM1 = -µ · B = µo(l+ 2s)B, (3.258)

where j1, is the magnetic moment operator, B is the magnetic field of the light, and f and s are the orbital and spin angular momentum operators, respectively (note that ldoes not contribute for S --+ S transitions, so this term will be ignored in the subsequent discussion). The matrix element of the operator HM 1 between states with different principal quantum numbers is identically zero because the angular momentum operators do not affect the radial wavefunctions, and radial wavefunctions are orthogonal for states with different principal quantum numbers.

A nonzero contribution to the Ml amplitude on the order of 10- 4 µ 0 arises from configuration mixing of the 6S1; 2 and 7S1; 2 states with states that have electrons excited from the closed shells [see, for example, Khriplovich ( 1991 ), Chapter 5.1 ], the evaluation of which requires complicated atomic calculations. In this problem, we are concerned with another, nuclear spin-dependent contribution to the MI amplitude of comparable magnitude which arises due to off-diagonal hyperfine interactions (Problem 1.11 ).

Show that the hyperfine-interaction-induced Ml amplitude can be related to the hyperfine splittings ~Ehr in the upper and the lower state (which can be precisely measured) according to (Hoffnagle 1982): (~F'M'lfll~FM} = 2µo Jl:l:hf=~Ehrn (F- F')(F'M'l§JFM}, n' n (3.259)

where the tildes designate hyperfine-interaction-mixed states.

This effect turns out to be important in experiments measuring parity-violation in alkali atoms such as Cs (Problem 1.13).

Solution In the case of s-electrons, the hyperfine interaction between the magnetic moments of the nucleus and the electron is of contact character (the Fermi contact interaction) whose Hamiltonian can be written as (Problem 1.4): (3.260)

where c is a constant, 6 ( r) is the 8-function, and f is the nuclear spin operator.

The Hamiltonian (3.260) is a scalar operator with respect to atomic wavefunctions

## INTERACTION OF ATOMS WITH LIGHT

(Appendix F), and thus mixes only states of the same total angular momentum F and its projection M (and also, in general, with the same quantum numbers Land S, but not necessarily J, see Problem 1.11 ): ------ lnS112F M) = (FMIJ-s)FM)

I )

= lnS112FM) + aoff En_ En' In S112FM (3.261)

aorrF(F+l)-J(J+l)-s(s+l)l 'S FM)

= lnS112F M) + 2 En _ En' n 1/2 , (3.262)

------- (n' S1; 2F' M'I =(n' S1; 2F' M'I a0rrF'(F'+l)-J(l+l)-s(s+l)( S , , + 2 En' -En n i12F M 1.

(3.263)

In Eqs. (3.262) and (3.263), (3.264)

where 'l/Jn, "Pn• are the real wavefunctions of the corresponding s-states. The matrix element ofµ= -2µ 0sbetween the states (3.262) and (3.263) is then: ( -;---- , , 1 _ ------ F ( F + 1) - F' ( F' + 1) ( , , n 112F M µlnS112FM} = aoffµO En_ En' FM l§IFM), (3.265)

where we used the independence of the matrix elements of S of the principal quan- tum number. Note that the Ml amplitude (3.265) vanishes for F' = F. Since l = 0, there are only two possibilities for having F' # F: • F' = I+ 1/2; F = I - 1/2; F' - F = 1, and • F' = I - 1/2; F =I+ 1/2; F' - F = -1.

In either case, we have: F(F + 1) - F'(F' + 1) = (F - F')(2I + 1).

(3.266)

The remaining step in deriving Eq. (3.259) is to relate 0otr to the hyperfine structure splittings. Using the Hamiltonian (3.260), we find for the hyperfine shift

TRANSITIONS WITH UNRESOLVED HYPERFINE STRUCTURE of the levels: Ehrn(F) = (nFlc6(r)f · S,nF) = c,P~(O) F(F + l) - /(/ + l) - s(s + l), (3.267)

from which we have: and similarly for n', F'. From this and Eq. (3.264 ), it follows that J ~Ehrn' ~Ehrn I+ 1/2 lloff = (3.269)

which, upon substitution into Eq. (3.265) together with Eq. (3.266), yields the sought-for Eq. (3.259).

3.19 Transitions with unresolved hyperfine structure Consider an atomic transition between states with total electronic angular momen- tum J and J' respectively, where J = 1 /2 and J' = 1 /2. The nucleus of the atom has spin I = 1 /2. The initial and the excited state each have two hyperfine components with total angular momenta F ( or F') = 0 and F ( or F') = 1. We prepare the initial state such that its wavefunction is l·,P(O)) =IF= 1,M = 1) ~ = 1,M = -1)

(3.270)

and measure absorption of linearly polarized light [e.g., (a+ +a-)/v'2] propagat- ing along the quantization axis (z). Later on, as a result of, for example, Larmor precession in a magnetic field applied along z, the wavefunction of the initial state evolves into l·,P(t)) =IF= 1,M = 1) - IF= 1,M = -1)

v'2 (3.271)

at time t. Note that the evolution from 11/J(O))

to 11/J(t)) corresponds to Larmor precession by 1r /2 (here we neglect any overall phase factor which is not important for the present considerations).

(a) Assuming an electric-dipole (EI) transition where all hyperfine levels are spec- trally resolved, calculate the relative absorption coefficients for light tuned to each of the possible hyperfine-structure transitions. Compare these coefficients for the initial state being 11/J(O))

and l'l/J(t)).

## INTERACTION OF ATOMS WITH LIGHT

(b) Compare the absorpti_on coe~cients for the initial state being ll/J(O)) and ll/J( t))

for the case of light that 1s sufficiently broadband so that the upper-state hyperfine structure is unresolved.

(c) Give a qualitative explanation of the result of. part (b). Formulate a general theorem concerning light absorption from a polanzed state when the final-state hyperfine structure is unresolved.

Hint To solve this problem, it may be useful to employ the results of Problem 3.4 and the fact that the reduced dipole matrix element for a transition between hyperfine- structure levels can be found according to [see, for example, Appendix I and the book by Sobelman (1992), Sections 4.3.5 and 9.2.3]: (e, I, J', F'l ldllg, I, J, F)

=(-l)l+l+J+F'(e,J'lldllg,J)J(2F'+1)(2F+l){; ~ n.

<3-272> This result can be derived by expanding the initial and final states into the IJ, MJ)IJ, M 1) basis and applying rules for summation of combinations of the angular coefficients. Of course, the present problem can also be solved by applying the Clebsch-Gordan expansion without explicitly using the result (3.272).

Solution (a) From Eqs. (3.272) and (3.132), W _ ll(e,J'lldllg,J)j 2e~(J,M1,l,OIJ',M~)2 eg - r fi2 2J' + 1 ' we find the following relative absorption rates: lv,(0)) : F = 1 --+ F' = 0, W oc 2/3, F = 1 --+ F' = 1, W oc0.

lv,(t)) : (3.273)

F = 1 --+ F' = 0, W oc 0, F = 1 --+ F' = 1, W oc 2/3.

Note that for the given choice of light polarization, lv,(0)) is a dark state for the 1 --+ 1 transition and Iv,( t)) is a dark state for the 1 -+ 0 transition.

OPTICAL PUMPING AND QUANTUM BEATS IN MERCURY (b) If the final-state hyperfine structure is unresolved, in order to find the total absorption rate, we need to add the absorption rates for the 1 ~ 1 and 1 ~ 0 transitions. We see that, in this case, the absorption does not change when the wavefunction is rotated by 1r /2 around the quantization axis. In fact, it is also straightforward to see from this result that the absorption rate is invariant with respect to an arbitrary rotation of the initial state around z !

(c) The reason that absorption is invariant with respect to rotations of the atomic state when hyperfine structure is not resolved is that the total electronic angular momentum of the initial state is J = 1 /2 and such a state cannot support polar- ization moments (Problem 9.7 and Appendix G) with rank K higher than 2J = 1.

The polarization moments corresponding to the states l'l/J{O)) and l'l/1(t)) are of rank K = 0 (population) and K = 2 (alignment). When hyperfine structure is not resolved, we can neglect the nuclear-spin part of the wavefunction. However, since the electronic state cannot support alignment, it is impossible to detect the alignment of the initial state using light absorption.

The general theorem can be formulated as follows. Suppose we have a state with electronic angular momentum J, nuclear spin I and total angular momentum F. We prepare any kind of polarization in this state and want to probe it using weak probe light tuned to a transition to some other state with J', for which the hyperfine structure is unresolved. Then, the signal is only sensitive to the initial- state polarization moments of rank O < K < min{2, 2J}. Here we have taken into account the fact that one-photon transitions are insensitive to polarization moments with "" greater than 2 (alignment) because photons have spin I. In order to detect polarization moments of rank K, the atomic states involved in the transition as well as the light field must be able to support polarization moments of rank "'· Because the spatial symmetry of an angular-momentum state is directly related to polarization moments (Problem 9. 7), there is a consequence of the theorem for aeman beats. In general, if an atom is undergoing Larmor precession in a magnetic field, in the probe signal, one can observe contributions (beats) at the Larmor frequency (due to orientation) and twice the Larmor frequency (due to alignment). However, when the final-state hyperfine structure is unresolved, no beats can be observed for J = 0 states and only beats at the Larmor frequency (but not twice the Larmor frequency) can be observed for J = 1/2 states.

3.20 Optical pumping and quantum beats in Mercury This problem will provide an illustration of how nuclear spins can be optically polarized, even if the transitions' hyperfine structure is not spectrally resolved. It will also provide a nice demonstration of the phenomenon of hyperfine quantum beats [see Haroche (1976), for example]. Quantum beats occur when an atom is

INTERACfION OF ATOMS WITH LIGHT put into a superposition of different eige~states ~f the_ atomic Hamiltonian with distinct energies. In such a situation. light mteractmg with the atom exhibits oscil- latory behavior at the frequency corresponding to the energy splitting between the eigenstates. The oscillatory behavior can be observed, for example, in the inten- sity of fluorescence emitted in a particular direction or in the polarization of light absorbed or emitted.

The ground state of the mercury atom has total electronic angular momentum J = O, while the nuclear spin for 199Hg is I = 1 /2. Suppose we initially have unpolarized atoms, and we apply a short pulse of circularly polarized light tuned to resonance with a transition to an excited J' = 1 state.

(a) What are the hyperfine-structure levels in the ground and the excited state?

(b) What is the nuclear polarization (the average ~roject~on of the nuclear spin on the direction of the circular polarization of the hght) nght after the excitation pulse? Give a qualitative explanation to this result.

(c) What is the nuclear polarization as a function of time?

(d) Explain how the results above pertain to optical pumping of nuclear spins. In parts (b)-(c), only consider the atoms in the excited electronic state.

Solution (a) The hyperfine structure of the states involved is shown in Fig. 3.27 along with the laser-induced transitions. Obviously, there is no hyperfine splitting in the ground state because J = 0.

(b) Before the excitation pulse, we have an unpolarized ground state, i.e., an inco- herent mixture of the ground state Zeeman sublevels. With left-circularly polarized light, the atoms in the IF= 1/2, MF = 1/2) sublevel can only be excited to the IF' = 3/2, MF' = 3/2) sublevel, which is an eigenstate of the Hamiltonian for the atom. Therefore, upon excitation, there are no quantum beats associated with this state since the atom is not in a superposition state. Note that the polarization of the nucleus is not affected by the transition - the nucleus is just a "spectator" to the process.

Let us now consider the fate of the atoms that are initially in the IF = 1/2, MF = -1/2} sublevel. Such atoms are coherently excited to a superpo- sition of IF' = 3/2, MF, = 1/2) and IF' = 1/2, MF, = 1/2). Let us evaluate the corresponding amplitudes in terms of the reduced matrix element of the transition (J'lldllJ}. To do this, we find the values of the reduced matrix elements (F'lldllF}

F'= 3/:!

1/2 F = 1/2 OPTICAL PUMPING AND QUANTUM BEATS IN MERCURY -l/2 FIG. 3.27 Hyperfine structure and laser-induced transitions in a J = 0 ~ J' = 1 transition in 199 Hg (nuclear spin / = 1 /2).

according to Eq. (3.272) (see Problem 3.19), ((J' J)F'lldll(J I)F)

(3.274)

{ J' F' I } = (-l)J'+l+F+l J(2F + 1)(2F' + 1)

F J (J'lldllJ), which are -v'2(J'lldllJ)/3 for the case of F' = 1/2 and 2(J'lldllJ)/3 for the case of F' = 3/2. Using the Wigner-Eckart theorem [see Appendix F and

## Appendix I, Eq. (1.18)]

(F'MF'ldqlFJ\;fF) = (-l)F'-M,,,, ( MF' l MF)

(F'lldllF), (3.275)

- F' q F we find that the following superposition of the MF' = 1/2 states is excited from the F = 1/2, MF= -1/2 state (see Problem 3.4): 11/J)

= ~IF'= 3/2, MF' = 1/2) + ~IF'= 1/2, MF' = 1/2).

(3.276)

For further reference, we also write the wavefunction of the atoms excited from the IF = 1/2, MF = 1/2) state: I~) = IF'= 3/2, AJF' = 3/2).

(3.277)

Because the initial sublevels are incoherent, the wavefunctions 11/J)

and I cp) are also mutually incoherent.

INTERACl1ON OF ATOMS WITH LIGHT Expression (3.276) can ~ decomposed into the uncoupled basis IMJ,, Mi)

using Clebsch-Gordan coefficients 11/J) = G + D 11, -1/2) + ( f -f) 10, 1/2)

= 11, -1/2) , (3.278)

which shows explicitly that only the MJ, = 1 state for the electron is excited b the laser pulse, while the nucleus just "goes for the ride."

y A similar decomposition for the wavefunction (3.277) is trivial: lip) = 11, 1/2).

(3.279)

From Eqs. (3.278) and (3.279), we see that the nucleus, being in an incoherent mixture of the M1 = ±1/2 states with equal weight, remains unpolarized upon short-pulse excitation.

(c) In order to find the time dependence of nuclear polarization, we go back to Eq. (3.276), and add time dependence of the eigenfunctions by introducing the hyperfine frequency w = (EF'=l/ EF'=I/2)/li corresponding to the energy interval between the two hyperfine states: 11/J(t)) = (-1 IF'= 3/2, MF' = 1/2)e-iwt v'3 + Ji IF' = 1/2, MF, = 1/2)] e-t/ 2 T, (3.280)

where r is the lifetime of the J' = 1 state. Correspondingly, Eq. (3.278) becomes 11/J(t)) = [ Ge-iwt + D 11, -1/2) + ( f e-iwt - f) IO, 1/2)] e-t/2T, (3.28 I)

so that the average nuclear projection on the direction of the light circular polar- ization (taking into account also the atoms excited from the MF = 1/2 sublevel and assuming an initially equal distribution in the two ground state sublevels) for atoms in the excited state is: (Mi)~ [ 1e-iwt + ~ • (-½)

+ f e-iwt - f • G)

+ ½]

e-t/T (3.282)

From this expression we see that nuclear polarization, while zero at t = O, is generally non-zero at later times. The oscillations of the polarization (quantum beats) are superimposed on the exponential decay of the upper state.

## THOMSON SCATTERING

(d) This discussion shows that an optical-pumping cycle consisting of a h excitation followed by spontaneous decay back to the ground state . s on-pulse / increase population of the Af F = Ah = 1 2 state. Once there, the atoms ( or · s the cisely, their nuclei) are "trapped" as subsequent additional cycles ca ' rnore Pre- / Of h.

nnot rern them from the !vi 1 = 1 2 state.

course, t 1s conclusion is also tr 0 ve · · d h" · · ~ h 199H · ue for co tinuous exc1tat1on, an t 1s 1s, m 1act, ow g nuclei are optically n- purnped • practice [see Happer (1972), for example]. Note that, while resolvin h •n structure is not necessary for efficient pumping, it is necessary that th! /1:r~ne frequency w is not much smaller than the spontaneous relaxation rate 1 / YP rfine Note that, considering the results of Problem 3.19, even though we h '· .

.

ave acco plished optical pumping of the ground J = 0 state, as long as the u Ill- hyperfine structure is unresolved, we can only probe total population of t~per- state state. In other words, we cannot optically detect that the ground state he ground .

as been polanzed.

3.21 Thomson scattering Consider a free electron interacting with a light wave. Based on the cl .

.

. h 1· h .

. d h d" .

ass1caJ model m wh1c 1g t scattenng 1s ue to t e ra 1atton of the accelerating tron derive an expression for the total scattering cross-section Neglect the e e~-I ' .

.

· reco1 effects and the effects of the optical magnetic field. Formulate the conditions f · · be l"d or such approx1mat1on to va 1 .

Solution The electric force on the electron is F' = -el cos wt, (3.283)

where f. is the optical electric-field amplitude, w is the the frequency of the light, and we have chosen the phase of the wave arbitrarily. The ele~ron accelerates upon the action of this force and so produces an oscillating dipole d with the second time derivative •• - e L d=-coswt m.

(3.284)

where m is the electron mass. According to the classical dipole-radiation formulae, the total power radiated by the oscillating dipole is given by [Panofsky and Phillips

## INTERACTION OF ATOMS WITH LIGHT

( 1962), Sect. 20-2; Landau and Lifshitz, ( 1987), Sect. 67]

:.:. 2 p = 3c3 (d) , (3.285)

which, upon the substitution of Eq. (3.284) and integration over one period of the light oscillation gives (3.286)

By definition, the number of photons scattered per unit time by the electron is given by ~u, where ~ is the incident photon flux, and u is the sought-after scattering cross-section. In order to connect Eq. (3.286) with these quantities, we replace P with the number of photons scattered per unit time times the energy of a scattered photon, 1iw (which is the same as that of an incident photon, as long as we neglect recoil). Also, the average incident light intensity, <l>liw, is given by the average Poynting vector (3.287)

Solving Eq. (3.287) for e2 and making the corresponding substitutions into Eq. (3.286), we see that the Ii, factor cancels (after all, our derivation is classical)

along with w, and we get (3.288)

where r0 ~ 2.8 • 10- 13 cm is the classical radius of the electron.

In the derivation of Eq. (3.288) we have neglected photon recoil. A char- ~cteristic magnitude of the electron's momentum change in a scattering process IS (3.289)

which leads to a change in the electron's kinetic energy of t::.p2 fi2w2 t::,.E = 2m ~ mc 2 · (3.290)

As long as 1iw << mc 2, the change of the electron's energy, and, by energy con- servation, the energy difference between the incident and the scattered photons, is << liw, which justifies the no recoil approximation.

## CLASSICAL MODEL FOR A MAGNETIC-DIPOLE

## TRANSITION

In the derivation of Eq. (3.288) we also neglected the effect of the magnetic force on the electron. In other words, we assumed ev -B << <£.

C Here v is the amplitude of the electron's velocity as it undergoes the light-induced oscillation, and B == £ is the amplitude of the light magnetic field. This condi- tion is equivalent to saying that the electron's motion is nonrelativistic, v << c, or, equivalently, that the electron's displacement during half cycle of the oscilla- tion is much smaller than the light wavelength. For visible I ight, achieving the relativistic regime requires power densities on the order of 1017 W/cm 2 , a level readily achieved with mcxlem ultra-short-pulse lasers. The relativistic regime sig- nifies a host of interesting phenomena described by high-field electrodynamics (Hartemann, 2002), for example, generation of light at high harmonics of the input frequency in the course of the light interaction with the electron.

3.22 Classical model for a magnetic-dipole transition When we discuss electric-dipole interactions of atoms with light, we often use the "electron-on-a-spring" model (see, for example, Problem 3.21 ).

FIG. 3.28 Electron density in pure hydrogen IS and 2P, A/ = I states. Shown are contour plots obtained using hydrogen radial wavefunctions and spherical harmonics. There is no net elec- tric-dipole moment in either an S or a P state as the electron density is symmetric with respect to the nucleus.

It is interesting to consider the correspondence between the classical "electron- on-a-spring" model and the quantum mechanical model of light-atom interactions (see Probs. 3.1, 3.3, and 3.4 ). Classically, in order to have electric-dipole radiation, we need an oscillating ( or rotating) dipole. However, an atom in a particular energy eigenstate does not represent an oscillating dipole. An oscillating dipole requires a coherent superposition of non-degenerate states of opposite parity ( one can see this, for example, by considering a superposition of an s- and a p-orbital, see

## INTERACTION OF ATOMS WITH LIGHT

FIG.

3.29 A superposition of the two states shown in Fig.

## 3.28 (of the

form (In= 1, L = o, ft.;[= O) + e-iw,, st ln = 2, L = 1, M = 1))/J2 in the case shown here) cor- responds to an electron displaced to one side of the nucleus. The electron density rotates around the nucleus at a frequency corresponding to the energy interval between the S and p states (one period of such a rotation is shown in the figure), leading to El radiation. The arrow indi- cates the magnitude and points in the direction of the electron density excess ( opposite to the instantaneous direction of the electric dipole moment, since the electron charge is negative).

Figs. 3.28 and 3.29). Incidentally, these considerations show that there is no semi- classical picture for spontaneous emission from an excited state - semi-classically.

such states are stationary.

Devise a similar model for magnetic-dipole (Ml) interactions. It is helpful to begin by considering electron densities for states that are coupled in an Mt transition. For example, consider a transition between Zeeman components of an L = 1 state that are split in energy in a static magnetic field applied along z.

What does the superposition state look like in this situation? How does it evolve in time? Also discuss the correspondence of the classical and quantum pictures for magnetic-dipole radiation.

Solution In order to visualize the mechanism of the magnetic-dipole radiation, as suggested, we tum to the simple case of an Ml transition between Zeeman components of an

CLASSICAL MODEL FOR A MAGNETIC-DIPOLE TRANSITION FIG. 3.30 Contour plots of the electron density in pure hydrogen 2P, Al = 0 and 2P, Al :::: states.

FIG.

## 3.3 I

Contour plots of the electron density for a coherent superpos1t1on (In= 2, L = 1, M = 0) + exp (-iw10t)ln = 2, L = 1, A/= I) )/v'2 at different times. The nonzero value of w 10 results from the Zeeman shift of the A/ = I sublevel in a static magnetic field. Shown is one period of Larmor precession. The arrow indicates the magnitude and instantaneous direction of the magnetic dipole moment.

L = 1 state that are split in energy in a static magnetic field applied along z. Let us look at the electron densities corresponding to various states (Figs. 3.30, 3.31 ).

In this case, not only is there no electric dipole moment in the pure eigenstates, but neither is there any dipole moment in their coherent superpositions. A superposi- tion corresponds to two electron-density "bulges" that are symmetric with respect to the nucleus, but are displaced in the opposite directions with respect to the x-y

INTERACflON

## OF ATOMS WITH LIGHT

plane. 18 In the presence of a z-directed magnetic field, these bulges rotate around the z-axis at the Larmor frequency. It is easy to see from the definition of the magnetic dipole moment (see Problem 1.15)

m = ~ 11-;- X ](r)d 3r 2c (3.291)

(here J is the electric-current density) that the instantaneous direction of the sys- tem's magnetic dipole moment is tilted with respect to the z-axis, and is rotating around this axis at the Larmor frequency, causing MI radiation.

Note that a single rotating bulge symmetric with respect to the x-y plane would be a poor mcxlel in this case. First, such a distribution has an electric dipole moment. Second, although such a system has a magnetic-dipole moment, it does not change with time, and thus does not produce MI radiation.

## 3.23 Nonlinear three-wave mixing in isotropic chiral inedia

Usually, second-order nonlinear susceptibility, x( 2), is zero for an isotropic medium because most common isotropic media are centrosymmetric, i.e. their properties are invariant under spatial inversion [see, for example, Boyd (2003)].

However, as the following example shows, just because a medium is isotropic it does not necessarily follow that it is centrosymmetric!

Consider a gas or a liquid solution of chiral molecules. Such a medium is optically active - it rotates the plane of polarization of linearly polarized light propagating through the medium. The fact that the medium is isotropic means that the rotation angle does not depend either on the direction of light propagation or on the direction of the linear polarization.

On the basis of symmetry considerations, argue that: (a) the second-order susceptibility x( 2) is generally non-zero in such a medium (in the course of this argument recall why x( 2) = O for isotropic centrosymmetric media); (b) sum- and difference-frequency generation are forbidden in a geometry where all three light beams (the two input beams and the beam generated as a result of the nonlinear mixing) are collinear; and 18 The bulges occur in the regions of space where the M = 0 and the M = 1 parts of the wavefunc- tion interfere constructively, i.e., where these two pans are in phase. Conversely, the electron density is low where these two parts are out of phase and interfere destructively. The relative phases of the two components can be easily deduced by examining the explicit form of the spherical harmonics Yf 1 (8, </>).

NONLINEAR THREE-WAVE MIXING IN ISOfROPIC CHIRAL MEDIA (c) second-harmonic generation is forbidden.

(d) Electro-optical rotation can be thought of in terms of a x<2) wave-mixing pro- cess, where one of the "waves" is the de field. Suppose a static electric field is applied along the direction of propagation of linearly polarized light in an isotopic chiral medium. Can there be optical rotation linear in the applied static field?

Solution (a) Suppose two electromagnetic waves with electric-field amplitudes f 1 and £2 are present in the medium. In general, second-order nonlinear-optical processes (a.k.a. three-wave mixing) arise due to the medium's polarization which is bi-linear in these amplitudes: (2)

(2)C'lc-2 j\ oc Xijke,je,k, (3.292)

where x~Jk is the second-order nonlinear susceptibility tensor.

For an isotropic medium, any quantity describing the medium, including x~Jk, should be invariant with respect to rotations of the coordinate frame. This does not leave us much choice for constructing the susceptibility tensor, in fact, there is only one possibility available [see, for example, Riley et al. (2002), Sec. 21.8-9, or Weisstein (2005)]: (2)

Xijk oc f.ijk , (3.293)

where f. ijk is the completely antisymmetric (Levi-Civita) tensor.

Thus, we have: (3.294)

where c is the proportionality constant. Alternatively, this can be written as p(2) = cf 1 X £2 .

(3.295)

For a "normal" centrosymmetric medium, the proportionality coefficient c is just a scalar because all properties of the medium must remain invariant under spatial inversion. Let us examine what happens to the left-hand and right-hand side of Eq. (3.295) upon spatial inversion. Polarization of the medium p(2) is a polar vector, and thus changes sign upon spatial inversion. On the right-hand side, however, we have a product of two polar electric-field vectors, which is an axial vector invariant with respect to spatial inversion. This can only be the case when c (and, correspondingly, 3)(2)) is equal to zero. This proves the well-known fact that

INTERACflON OF ATOMS WITH LIGHT three-wave mixing is forbidden in isotropic media which are invariant with respect to spatial inversion.

A chiral medium, however, is not invariant with respect to inversion because this operation converts left-handed molecules into right-handed ones and vice versa. Therefore, there is a possibility that a part of the proportionality coeffi- cient c is actually a pseudoscalar, i.e., a rotationally-invariant scalar quantity that flips sign upon spatial inversion. With this, both sides of Eq. (3.295) are odd with respect to spatial inversion, and the second-order nonlinear polarization is generally non-zero.

(b) Nevertheless, the specific form of Eq. (3.295) restricts the allowed types of three-wave mixing. For example, the nonlinear polarization is zero for input waves of the same polarization. Also, if the two waves are co-propagating, the induced polarization is along the propagation direction, so the resultant wave generated by this polarization cannot propagate in the same direction (which would violate transversality - the fact that in isotropic, non-dissipative media the electric and magnetic fields of light must be orthogonal to the direction of light propagation).

(c) Suppose now that the two input waves are of the same frequency. At each point in the medium, we have two fields applied, however, according to the superposition principle, we can take a vector sum of these fields to obtain just one resultant field (with a generally complex polarization). But the vector product of any vector with itself is zero, and Eq. (3.295) once again leads us to the conclusion that three-wave mixing is forbidden in this case, i.e., coherent second-harmonic generation does not occur in isotropic chiral media. 19 (d) Let us now consider the possibility of electro-optical rotation. The geometry of the _problem is such that if we have initial light-field polarization ea, and a static field Ede, then the light polarization e' upon propagation through a thin slice of the medium can be written as _, - - - e = eo + aEdc x eo .

(3.296)

19 Here we have shown that two input waves of the same frequency cannot produce coherent second-harmonic output (independently of the waves' polarizations or propagation directions) in isotropic media in the framework of the dipole approximation. It turns out that, in the case of a sin- gle input beam, the result holds true even if all possible higher multipoles are considered (Andrews and Blake 1988). We can give a simple proof of this [different from the one by Andrews and Blake ( 1988)], once again, based on symmetry arguments. In this geometry, the only independent vectors in the problem are the amplitude £1H of the wave at the fundamental frequency, its wave vector k, and the polari1.ation of the second-hannonic wave £ 2H (the second-harmonic wave would need to have the wave vector 2k). Out of these vectors, it is impossible to construct an expression for the amplitude of the process that would be quadratic in £ 1 H, linear in £ 2H, and would not violate transversality, i.e., the requirement that £1H · k = l2H · k = 0.

A NEGATIVELY REFRACTING ATOMIC VAPOR?

Here a is a pseudoscalar proportional to the pseudoscalar part of c. Equation (3.296) can also be rewritten as _, - - E x Eo = -aEdc .

(3.297)

Equation (3.297) passes the test of spatial-inversion invariance; however, it fails the test of time-reversal invariance. Indeed, if we reverse the direction of time (which, in this case, would be equivalent to sending the light beam backwards), we would need to interchange the initial and final polarization vectors, which would flip the sign on the left-hand side of Eq. (3.297), while the right-hand side of Eq. (3.297) remains unchanged. We thus see that nonlinear electro-optical activity is forbidden. More generally, we see that three-wave mixing in isotropic chiral media can only occur between non-collinear waves of three different frequencies.

The fact that coherent wave-mixing, for example, second-harmonic generation is forbidden does not actually mean that if one shines light at fundamental fre- quency onto a sample there will be no second-harmonic light whatsoever coming out of the sample. Imagine a container with a large number of second-hannonic- generation crystals that are randomly oriented. The medium is macroscopically isotropic, but locally, it is highly anisotropic, so second-hannonic generation can occur on an individual crystal. The overall output will depend on imperfect can- celation of the amplitudes generated in different crystals, and will scale linearly with the number of crystals (as opposed to coherent second-harmonic generation where the output power scales as the square of the participating dipoles or the length of the medium). An experimental study of second-harmonic generation in microscopically isotropic water suspensions of anisotropic biological "particles"

and the associated theory have been discussed by Allcock et al. ( 1996).

In this problem, we have considered various cases where coherent x( 2) pro- cesses are forbidden in the bulk. In most cases, however, these prohibitions fail at the interfaces between different media where the media are no longer isotropic.

This is the basis for powerful non-linear optical techniques to study surfaces and interfaces [see, for example, Shen ( 1989)].

3.24 A negatively refracting atomic vapor?

Left-handed materials are media where the electric permittivity e and the magnetic permeabilityµ are both negative (the term is unfortunate and potentially confusing since "left-handedness"

in this context is different from chirality normally asso- ciated with handedness!). It can be shown from Maxwell's equations [see, for example, Veselago (2003), Pendry and Smith (2004), and Milonni (2004)] that, in this case, the refractive index is also negative, i.e., n = -y'eµ. For an electromag- netic wave propagating in such a medium, the wave vector (k) is in the direction

## INTERACTION OF ATOMS WITH LIGHT

opposite to £ x ii, so, for example, on: needs to use the left-hand instead of the right-hand rule to find the direction of H from the directions of k and £.

Such materials are of Pai:1icul~ int~re~t since a "perfect_" lens [Pendry (2000)], not subject to the ordinary d1ffract1on hm1t, can be made wnh a material having an index of refraction equal to -1 [the concept of a perfect lens and other fascinat- ing properties of electromagnetic wave propagation through negatively refracting materials are reviewed, for example, by Veselago (2003) and Pendry (2004a); see also Smith (2005) and Milonni (2004)].

Most materials with negative refractive indices work only for electromagnetic radiation in the radio-frequency and microwave domains. These so-called meta- materials are artificial structures built out of discrete elements such as split metal rings, wires, etc. However, it should~ noted tha~ recently ~h~ng et al. (2005) pro- duced a metal-dielectric-metal multilayer material that exh1b1ted a negative index of refraction for infrared light with wavelength around 2 µm. The production of this metamaterial operating in the near-IR required sophisticated nanofabrication techniques to create the required nanometer-scale spatially periodic structure.

Is it possible that under certain conditions an atomic vapor could act as a neg- atively refracting material? First see what one. wou~d want in terms of the energy levels and transitions in the atom. Next, consider 1f such a system can be found in practice. Estimate the required density of the atoms. (Make sure the system is reasonably transparent!)

Solution One idea for making a negatively refracting atomic vapor could be to exploit the fact that, for light frequencies above an atomic resonance, the permittivity of the vapor drops below unity. For a sufficiently dense vapor, it may become negative.

In order to create the desired material, we would need both the electric permittivity and magnetic permeability to be simultaneously negative.

We begin with the discussion of the electric permittivity and limit ourselves to the electron-on-a-spring model of an atom (since there is only a single resonance frequency for such a system, this is, in other words, a two-level atom). In this model, the electric susceptibility as a function of frequency w is found to be [see, for example, Griffiths (1999), Section 9.4.3]: 41rNe 2 c=l+-- me .

w0 - w - i,w (3.298)

Here N is the atomic number density, and wo and , are the resonance frequency and width, respectively. If we denote the detuning from resonance w - w0 = ~,

A NEGATIVELY REFRACTING ATOMIC VAPOR?

we can re-write Eq. (3.298) as 41rNe2 c=l---- me (wo + w)Ll - i,w (wo + w)2Ll2 + ,2w2 .

(3.299)

Note that the real part of the index of refraction is proportional to A far fro resonance whereas the imaginary part decreases as Ll 2 • In order for the permittivity c to be essentially real, the frequency w has to be sufficiently far away from resonance where we can neglect the imaginary term, in other words, Ll >> , , so that E ~ 1 _ 41r N e2 me (wo + w)Ll · (3.300)

In order for the permittivity to be negative, we need to have w > w0 (i.e., A > O), and N me(wo + w)Ll > .

41re (3.301)

From Eq. (3.301 ), it is seen that for large~ on the order of the atomic frequency w0 , the condition on the density can be re-written as (3.302)

i.e., the density should be greater than the density of condensed matter, about 1024 atoms/cm 3, which would mean that the system was no longer a vapor.20 Here we have used the fact that the energy difference between the atomic states !u.,;0 should be on the order of the Bohr energy e2 / ao (see Appendix A).

On the other hand, the density requirement [Eq. (3.301 )] is significantly relaxed as the frequency w approaches the resonance frequency wo. From Eqs. (3.301) and (3.302), we find that closer to resonance we require N>]_~ rv a~ wo .

(3.303)

Recall that for the refractive index to remain real we cannot operate too close to resonance, so there is a lower limit on ~ of several times the resonance width ,.

At the densities N necessary to satisfy Eq. (3.303), , is dominated by pressure broadening, i.e., (3.304)

where up is the pressure broadening cross-section and v is the thermal velocity of the atoms (for a typical room-temperature gas, pressure broadening dominates 20 Incidentally, there do exist solids with negative electric pennittivity. In addition, dense plasmas have been also produced that have e < 0.

INTERACflON OF ATOMS WITH LIGHT when N apv ~ 21r x 1 GHz, where 1 GHz is th~ typical value of the D~ppler width for an optical transition). Re-writing the requirement (3.303) by settmg il rv ""f and using the expression (3.304) for 1 , we discover that the condition becomes independent of N: > 1 UpV --- "' a~ wo · (3.305)

The question now becomes whether or not the inequality (3.305) can be satisfied by typical atoms. Atomic pressure broadening cross-sections are usually in the range of 10- 15 - 10- 14 cm2 (see Appendix A), so in fact it is possible for a room temperature gas (where v "' 104 cm/s) to achieve negative permittivities near resonance. For these conditions, the atomic density will be N '"" 1018 cm- 3 , six orders of magnitude smaller than in the far-detuned case, and c reaches negative values of order unity. Note, as Eq. (3.305) implies, that increasing the density past this point does not improve the situation. However, note that the condition (3.305)

does depend on the atoms' velocity v, so by using laser cooling (where thermal velocities can reach ;S 1 cm/s) or cryogenic techniques, the required density to achieve negative permittivities can be further reduced.

With the realization of the difficulties that arise when one is attempting to achieve an atomic vapor with negative electric permittivity, we now tum to the discussion of the magnetic permeability. Again, we will use a two-level model; however, in this case, the levels must be coupled by magnetic-dipole, rather than electric-dipole interaction. We can obtain the expression for the magnetic permit- tivity by analogy with Eq. (3.298) if we first rewrite it to introduce the transition dipole moment d as 41rNd2 c=l+ · mea 0 w0 - w - i1w (3.306)

Then, it is clear that the permeability is of the form 41rNµ5 µ= + ' mea 0 w~ - w - i1'w (3.307)

where µo is the Bohr magneton, w' and ,' are the frequency and width of the corresponding magnetic-dipole transition. 21 We can now easily obtain the conditions on the density necessary to make the permeability negative by following the same line of reasoning employed for the electric permittivity. The required density is thus the same as for the case of the 21 Here, we treat µ on the same footing as e. Some authors [e.g., Landau and Lifshitz (1995), Section 103] prefer, instead of treating electric and magnetic effects symmetrically, to take advantage of the relation between the electric and magnetic fields in an electromagnetic wave and introduce the magnetic effects via spatial dispersion of c, i.e., the dependence of e on the wave vector.

A NEGATIVELY REFRACTING ATOMIC VAPOR?

electric permittivity, except increased by a factor of ( d / µ 0 ) 2 "' 105• In the far- detuned regime, this would require densities larger than those of typical condensed matter, ruling out this possibility, while in the regime where w ---+ wo, typical levels of pressure broadening would prohibit negative values for µ for room temperature gases. For ultracold atomic gases, the required density (N "' 1019 cm- 3 ) is far too large for present technology.

Not only are the conditions for negative permittivity and negative permeabil- ity extraordinarily difficult to achieve in an atomic vapor, the conditions must be simultaneously satisfied at a particular frequency. We are thus left with a pessimistic assessment of the prospects of "left-handed" atomic vapors.

In our above considerations we have assumed that the electric dipole (E 1) and magnetic dipole (M 1) transitions are between the ground state of the atom and two distinct upper states, so the permittivity and permeability can be calculated independently. This seems a reasonable assumption, since E 1 transitions occur between states of opposite parity and M 1 transitions occur between states of the same parity. Recently, there has been a suggestion by Pendry (2004b) that the above requirements can be loosened somewhat in a chiral medium (molecular vapors, for example). The idea is similar to that employed in, for example, atomic parity violation experiments that take advantage of Stark-induced transitions (see discussion in Problem 4.5). In a chiral medium, the states have mixed parity, and thus transitions have both E 1 amplitudes (proportional to d) and M 1 amplitudes (proportional toµ). Interference between the Ml and El amplitudes enhances the magnetic dipole transition, and therefore the required density for negative perme- ability in a chiral medium is only a factor of"' d/ µ0 "' 2 x 137 larger than that for the permittivity. It is interesting to note that a similar situation can arise when nearly degenerate opposite parity levels are mixed with external fields, as in the case of hydrogen and dysprosium [Budker et al. (1994)]. Even so, achieving the vapor density ("' 1020 atoms/ cm 3) required for negative permeability in the small detuning regime would necessitate anomalously small pressure broadening. Using cold chiral molecules can reduce the required vapor density, but remains at present a technically difficult path to achieving a negatively refracting vapor.

One might wonder if electromagnetically induced transparency (EIT) in a multi-level atomic system might offer a possible solution to this dilemma - per- mitting high densities while maintaining narrow linewidths and small absorption.

Yet it appears that even with EIT the stringent requirements on the magnetic per- meability will be difficult to achieve in atomic vapors [Oktel and Mustecaplioglu (2004)). The use of quantum interference effects similar to EIT are being explored as a way to generate chirality while minimizing absorption [see, for example, Kastel et al. (2007)].

## INTERACTION OF ATOMS WITH LIGHT

## 3.25 Light propagation in anisotropic crystals

Recall the following results pertaining to linear plane-wave-light propagation in a transparent non-gyrotropic, anisotropic medium such as a uniaxial or biaxial crystal, for which the dielectric tensor eij is real and symmetric [these properties follow from energy conservation: see, for example, Fowles (1975), Section 6.7; Landau et al ( 1995 ), Section 97; Born and Wolf ( 1980), Chap. 14]: • For a given direction of the wave vector, there are two polarization eigen- modes, where the polarization is characterized by the direction of the electric displacement vector fJ. An eigenmode is a wave that propagates in the crystal maintaining its polarization.

• The two eigenmodes are linearly polarized with mutually orthogonal direc- tions of fJ.

Now on to the questions: (a) Why are the eigenmodes characterized by fJ rather than the electric field e?

(b) Why are there two eigenmodes?

(~) Why do the two eigenmodes correspond to mutually orthogonal directions of D?

(d) Why are the eigenmodes linearly polarized?

(e) Comment on the analogies between this problem and quantum mechanics.

Solution (a) For the case of a monochromatic light wave (of frequency w, so all quantities have temporal dependence e-iwt), Maxwell's equations take on the form: - - I 8ii iw - v x e = --- = -H C 8t C ' (3.308)

- - 1 afJ iw - V X H = -- = --D.

C 8t C (3.309)

LIGHT PROPAGATION IN ANISITTROPIC CRYSTALS Substituting the spatial dependence of all quantities in the form of eik-r (where k is the wave vector), we find: - - w - k x e = -H ' C - - w - k X H = --D.

C (3.310)

(3.311)

Equation (3.310) indicates that k is perpendicular to ii. Also, Eq. (3.31 I) shows that fJ is perpendicular to both k and ii. Thus, the vectors k, D, and ii are all mutually perpendicular. On the other hand, while £ is perpendicular to ii [Eq. (3.310)), it is not, in general, perpendicular to k in an anisotropic medium (Fig. 3.32).

-D k FIG. 3.32 Various vectors describing plane-wave propagation in an anisotropic medium.

(b-d) [Here we follow Bredov, et al. (1985), Section 29.]

First, let us eliminate ii from Eqs. (3.310) and (3.311) to obtain the wave equation - - - w - k x k x e = - 2 n (3.312)

C which, using the "BAC-minus-CAB" vector identity, becomes k(k. l) - lk 2 = - w2 D.

(3.313)

C

INTERACflON OF ATOMS WITH LIGHT This is a vector equation. We will choose a coordinate system with one of the axe~ along f, and look at the projections of each of the terms onto an axis (a) orthogonaJ to k. Since k has zero projection on this axis, the first term in Eq. (3.313) does not contribute, and we have: (3.3)4)

Until this point, we have only used Maxwell's equations, and have not used any information about the properties of the medium. All the relevant properties are contained in the material equations Di= CijCj.

(3.315)

These relations can be inverted to read ei = c;/DJ.

(3.3 J 6)

Since Eij is symmetric, so is its inverse, the inverse permittivity tensor c;; 1 [see, for example, Riley et al. (2002), Section 8.12].

Substituting Eq. (3.316) into Eq. (3.314 ), we have W c013D13k = c2 D0 .

(3.317)

In this equation, since D is confined to a plane, there are only two possible values of the indices o and /3, and the relevant components of c;J correspond to a 2 x 2 symmetric matrix.

Equation (3.317) can be regarded as an eigenvalue problem for the the 2 x 2 tensor c- 1, where the eigenvalues are n- 2 = w2 /(k 2c2), and n is the effective refractive index for a given eigenmode. We now recall that any symmetric tensor can be diagonalized, and the principal axes are orthogonal to each other [see, for example, Riley et al. (2002), Section 8:.} 3]. Thus, the eigenpolarizations corre- spond to two orthogonal directions of D along these principal axes, so the two eigenpolariz.ations are linear.

( e) The analogy with quantum mechanics can be made rather complete. In quantum mechanics, we often talk about temporal evolution of the wavefunction governed by the Hamiltonian. In this case, we deal with spatial propagation of an electro- magnetic wave, and we were able to reduce the propagation problem, using the Maxwell's equations and the material relations, to the eigenvalue problem (3.317)

analogous to that of finding eigenstates in a quantum-mechanical two-level sys- tem. It is interesting to note that "orthogonality" of eigenstates corresponding to distinct eigenvalues, which in quantum mechanics usually refers to Hilbert space, here can be understood literally - the two eigenpolarizations are orthogonal in real space.

## ELECTROMAGNETICALLY

INDUCED TRANSPARENCY (EIT)

## 3.26 Electromagnetically induced transparency (EIT)

The basic phenomenon of electromagneticaJJy induced transparency involves three levels and two light fields [Fig. 3.33(a)J. Suppose that, in the absence of Jight., alJ atoms reside in state I A). If a weak field (the probe field) is applied on resonance with the I A) --+ IC) transition, in the absence of other light fields, the probe field experiences absorption. However, if a strong light field (the drive field) is applied on resonance with the adjacent transition between levels IB) and IC), absorption on the probe transition vanishes. [There is vast literature available on the subject of EIT. A few accessible references include papers by Vrijen et al. () 996), Harris ( 1997), and Kasa pi ( 1996 ). ]

IC)

fC)

(a)

(b)

1B)

--, _______ IB_)

IA)

IA)

FIG. 3.33 (a) Illustration of the basic phenomenon of electromagneticaJJy induced transparency (EIT). Absorption on the probe (IA) ~ IC)) transition is suppressed when a strong drive field is applied on the adjacent transition between levels I B) and /C}. (b) EIT in the case where light frequencies are detuned from their respective one-photon resonances.

(a) Give a simple quantum-mechanical explanation of the EIT phenomenon. In particular, show that there is a coherent superposition of states /A) and /B) that does not absorb light from either probe or drive field (a dark state). Make the simplifying assumption that both light fields are monochromatic.

(b) What role does spontaneous emission play in EIT? For example, is sponta- neous emission necessary to put atoms originally prepared in state /A) into the dark coherent superposition of states I A) and I B)?

(c) In part (a), we considered the case where both the probe and the drive fields are tuned to their respective one-photon resonances. In this case, the two-photon (Raman) resonance condition is (3.3 I 8)

INTERACflON OF ATOMS WITH LIGHT where wp and wd are the probe and drive frequencies, respectively, and EA, E 8 are the energies of the corresponding states.

Now consider the same system, except that the light fields are not exactly on resonance with the corresponding one-photon transitions [Fig. 3.33(b)]. Since the strong drive light field is off-resonant, it causes ac-Stark shifts of the levels IB)

and IC) (see Problem 2.7), so the two-photon (Raman) resonance condition is no longer given by Eq. (3.318).

In this case, at what frequency of the probe light does absorption vanish due to EIT?

Solution (a) The basic EIT phenomenon can be understood by considering the interaction of an atomic system with the bichromatic light field consisting of the probe and drive light fields. The states IA) and 1B) are both coupled to the upper state IC) by the light field. In general, we can consider the interaction with IC) of any coherent superposition of states IA) and IB): 11/J) = alA) + blB) , (3.319)

where a and b are some constant complex coefficients.

The amplitude A for photon absorption in the dipole approximation is propor- tional to the prcxluct of the dipole transition matrix element and the optical electric field J. e (see, for example, Problem 3.4). In the present case, A oc (Cid· £Iv,) = a(CldlA)ep + b(CldlB)ed = adcAep + bdcBed, (3.320)

where ep is the amplitude of the probe field and ed is the amplitude of the drive field. In the above we neglect far off-resonant interactions such as the direct interaction of the drive light field with the I A) ~ IC) transition.

Here an essential point is that we add transition amplitudes (not probabilities).

The amplitude A in Eq. (3.320) vanishes when b = _ dcAf.p a .

dcBed (3.321)

When the condition (3.321) is satisfied, the atoms are in a dark state, 11/Jdark), where they do not interact with light (see also Problems 3.9 and 3.10). Note that choosing the ratio of the drive and probe intensities sufficiently high, we can have essentially all of the atomic population remaining in state IA).

Let us recap the situation. The atoms are in state IA), the probe light is applied on resonance with the IA) ~ IC) transition, but there is no absorption, where there would have been absorption in the absence of the light driving the 1B) +-+ IC)

transition. This is EIT.

ELECTROMAGNETICALLY INDUCED TRANSPARENCY (EIT)

But how does the atomic system end up in the dark state? It turns out that in practice preparing the system in the dark state is not difficult, since the system tends to self-adjust to be in the appropriate state for EIT to occur. The creation of a dark coherent superposition of atomic states is also known as coherent popu- lation trapping (see Problem 3.10). We briefly discuss this in the solution to part (b). Coherent population trapping is reviewed by Arimondo (1996) and coherent population transfer is reviewed by Bergmann et al. ( 1998).

(b) This is indeed a somewhat tricky question. Clearly there must be spontaneous emission in the system: we have level IC) that lies above levels IA) and 1B) and has non-zero electric-dipole matrix elements coupling to both IA) and 1B). Thus, if we populate level IC), there is necessarily spontaneous emission to the lower levels.

While this is true, it does not answer the question of the role of spontaneous emission in the generation of EIT.

It turns out that in some instances, spontaneous emission does indeed play a role in the creation of EIT. Imagine a situation where all atoms are initially in state IA), and the light fields are turned on abruptly. State IA) is a superposition of the dark state and the bright state (where the bright state is the coherent superposition of states IA) and IB) orthogonal to l"Pdark) ). The dark state component of IA) does not interact with light, but the bright component does. Therefore, after the light is turned on, some atoms will be excited. Following the excitation, an atom can spontaneously decay to levels IA) and 1B), which may land it either in the bright or the dark state. Since atoms are not re-excited from the dark state, eventually, all atoms are pumped into 11/Jdark)- This scenario, however, does not mean that spontaneous emission is always necessary for establishing EIT. It turns out that it is possible to put the system into the dark state without having any spontaneous emission to the lower levels. Here is how it can be done. Let us first tum on the drive field alone. This light drives transitions between two empty levels (1B) and IC)) and there is no fluorescence.

This means that the system happens to already be in the dark state [11/Jdark)

= IA)

for this particular light field, ep = 0, see Eq. (3.321 )]. Now we have to exer- cise some caution in turning on the probe field - if we tum it on abruptly, there will be fluorescence. However, if we tum this field on adiabatically (see Problems

## 2.6 and 3.17), the system will remain in the dark state. The atoms evolve into a

superposition of the states IA) and IB), and no spontaneous decay ever occurs!

This situation is directly analogous to many different adiabatic following prob- lems, for example, a classic problem in polarization optics where the goal is to rotate the direction of linear polarization of a light beam if only (ideal) dichroic polarizers are available. The trick is to pass the light through a sequence of such polarizers, each rotated by a very small angle with respect to its input linear polar- ization. In such an arrangement, the polarization rotation angle per polarizer is

## INTERACTION OF ATOMS WITH LIGHT

<P / N, where ¢ is the total desired rotation angle, N is the number of polarizers.

The fractional light-power loss per polarizer is ½ ( </> / N) 2 (for sufficiently large N).

Thus, the total loss (analogous to fluorescence in our problem) is </> 2 / {2N) and can be made as small as desired by increasing N.

The method of coherent population transfer of population between levels dis- cussed in this part is known as Stimulated Raman Adiabatic Passage (ST/RAP) (see Bergmann et al. ( 1998) and also the discussion of adiabatic passage in Problem 2.6].

(c) The dark state in our three-level system is decoupled from the light and thus is not subject to light shifts. Therefore EIT occurs when the condition (3.318) is satisfied, while the two-photon (Raman) resonance occurs at an ac-Stark shifted frequency.

Reality check: It often happens that various nonlinear optical processes occur concurrently, and it is not so easy to disentangle them and apply the simplified reasoning we have been practicing above in a realistic situation.

Let us illustrate this by checking our understanding of EIT against the results of a full quantum-mechanical calculation for the three-level system interacting with two light fields (as in Fig. 3.33). The calculation is set up in the following way. Atoms are assumed to leave at a rate , the region where they interact with the bichromatic light field (independently of which atomic state they are in). The depletion of the total population is compensated by assuming the same number of atoms entering the interaction region. The entering atoms are in the ground state IA). Figure 3.34 shows the transmission coefficient (as a function of the probe fre- quency, in relative units) of the probe light going through a thin atomic sample for various conditions: ( a) no drive field, (b) drive field resonant with the IB) ~ IC) transition, and (c) drive field detuned by one natural width 10 of level IC) towards lower frequencies.

It is also instructive to look at the steady-state populations of each of the states as a function of the probe frequency tuning (Fig. 3.35). Here state IC) is assumed to spontaneously decay to states IA) and IB) with branching ratios 1/2 for each of the two decay channels. The latter plot can also be compared with the case of an open system where state IC) spontaneously decays predominantly to states other than IA) and 1B) (Fig. 3.36). In the latter case, for a weak probe field, the absorption spectrum is exactly the same as that shown in Fig. 3.34, while the populations of states IB) and IC) are obviously very different.

We leave it to the reader to identify and discuss various features of the trans- mission and population distribution profiles shown in Figs. 3.34, 3.35 and 3.36.

ELECTROMAGNETICALLY INDUCED TRANSPARENCY {EIT)

::.::::::::__'\ . .

.

( a) 1 -:! )'11 0 ~,, - ____ J (b)

(c)

FIG. J.34 (a) Transmission of probe light in the absence of the drive field as a functio .

n ot the probe frequency detuning ~P from the IA) ~ IC} resonance expressed in the units of h t e natural width of level IC}, -;-0 . Levels IA} and 1B} do not decay, but atoms leave the intera t· .

.

.

c ion region (and are replenished) at a rate of "Y = 0.05-;-o. (b) Same as (a) but m the presence t· h .

0 t e dnve field with the drive frequency tuned to the I B) +-+ IC) resonance (drive detuning ' . .

.

represented by solid vertical line). The resonant Rabi frequency for the dnve field is 0.8'"" 0 h d .

,o.

as e hne indicates probe absorption without drive field. (c) Same as (b) but with the drive f .

requency tuned by ')'o towards lower frequencies from the 1B) +---> IC) resonance. Figure courtesy S. M.

Rochester.

This is a common research task for both experimentalists and theorists: applyi h. I .

ng physical models to understand grap 1ca representations of data or calculations. A detailed look at a closely related problem where analogous behavior is observed namely a closed three-level system where atoms do not enter or leave the interac~ tion region, including an analytic calculation of the I ineshapes, is given by Lounis and Cohen-Tannoudji ( 1992).

## INTERACTION OF ATOMS WITH LIGHT

(a (b)

C < FIG. 3.3S Steady-state populations oflevels IA), IB), and IC) for the cases (a), (b), and (c) of Fig.

3.34 for a closed system where level IC) spontaneously decays to levels IA) and 1B). The plot is for a very weak probe field, so only a tiny fraction of the population of level I A) leaves this state via interaction with the light. Figure courtesy S. M. Rochester.

## ELECTROMAGNETICALLY

INDUCED TRANSPARENCY (EIT)

(a)

(b)

(c)

j FIG. J.36 Same as in Fig. 3.35 but for an open system where state IC) spontaneously decays predominantly to states other than IA) and IB). Figure counesy S. M. Rochester.

## INTERACTION OF LIGHT WITH ATOMS

## IN EXTERNAL FIELDS

## 4.1 Resonant Faraday rotation

When linearly polarized light propagates through a medium immersed in a mag- netic field, the plane of light polarization at the output is rotated (Fig. 4.1 ); this effect was observed by Michael Faraday almost one hundred and fifty years ago (Faraday 1855). In 1898, the Italian physicists D. Macaluso and 0. M. Corbino discovered that Faraday rotation was resonantly enhanced near atomic absorption lines (Macaluso and Corbino 1898).1 Circular Components ---- Medium Linear Polarization Magn~ Field B ~ q>,' I r-,,,..._ I I I I I / I I I FIG. 4.1 Conceptual setup for observing Faraday rotation. Linearly polarized light enters a medium subjected to a longitudinal magnetic field B. Left- and right-circularly polarized (u + and u _, respectively) components of the light field acquire different phase shifts as they propagate through the medium, leading to rotation of the axis of light polarization by angle <p. (In gen- eral, there is also different absorption of the two circular components of the light field which gives rise to elliptical polarization at the output.)

1 This phenomenon is known as resonant linear Faraday rotation or the Macaluso-Corbino effect.

The Macaluso-Corbino effect is referred to as a linear effect because at sufficiently low light powers the rotation is light-power-independent.

[For a detailed discussion of Faraday rotation and other closely related phenomena, see the recent review of linear and nonlinear magneto-optical effects by Budker et al. (2002).]

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS mz= -1 m:= 0 FIG. 4.2 Energy level diagram for an F = 1 -+ F' = 0 atomic transition. Zeeman sublevels are shifted in the presence of a magnetic field, changing the resonance frequencies for left- and right-circularly polarized light.

Consider an F = 1 ~ F' = 0 atomic transition (Fig. 4.2); F and F' are the total angular momenta of the upper and lower state, respectively. Assume that the width of the transition is given by the spontaneous decay rate from the upper state ,o (i.e., there is no Doppler or other kinds of broadening), and the atomic vapor is of length f. A magnetic field is applied along the direction of light propagation.

Derive the dependence of the Faraday rotation angle cp on the magnetic field and the detuning of the light frequency w from the atomic resonance wo.

Hint For this problem it is convenient to choose the axis of quantization along the magnetic field, i.e., the direction of light propagation.

Solution Linearly polarized light incident on an atomic sample can be decomposed into left- ( a+) and right- (a_) circularly polarized components. When a magnetic field Bz is applied to the sample along the direction of light propagation (the longitudinal direction, z), the Zeeman shifts between adjacent magnetic sublevels (= 9FJ4JBz, where 9F is the Lande factor and µ0 is the Bohr magneton) cause the refractive indices for a+ and a_ light to differ (circular birefringence). This, in tum, causes the circular components of the linearly polarized light to change their relative phase as they propagate through the medium - leading to optical rotation.

For the Doppler-free case and narrow-band light, in the absence of the magnetic field, the complex refractive index n( w) can be described by a Lorentzian lineshape function [see, for example, Griffiths ( 1999) and Problems 3.1, 3.3]

(4.1)

## RESONANT FARADAY ROTATION

where xo is the am~litude of the lin~ar susceptibility. 2 The ma~netic field shifts the resonance frequencies for the two circular components, so the mdices of refract"

n± ( w) for left- and right-circular polarizations in the presence of the longitudi~:~ magnetic field become (4.2)

Acc~rdin_g to Eq. ( 4.2), the difference between the refractive indices for a+ and a_ hght 1s: 4gFµoBz/,o n+(w) - n_(w) = -21rxo 2 .

(4.3)

(2gFµoBz/10)

2 + ( 1 - 2i(w~•~"))

The plane of light polarization is defined by the relative phase of the two circular components. For example, A 1 (A A )

f.x = J2 f._ - f.+ A (A A )

fy = /2 f + + f - , (4.4)

where ix and i y represent light polarized along x and y, respectively.

Suppose the light is initially linearly polarized along the x-axis. Then the optical electric field can be described by £ = f.o ix cos(kz - wt)

(4.5)

= ~o [ ~ ei(k_z-wt)

_ ~ ei(k+z-wt)]

+ c.c., (4_6)

where e0 is the amplitude of the optical electric field, c.c. denotes the complex conjugate, and the magnitude of the wave vectors k± are given by k± = n±w.

C (4.7)

The imaginary part of the wave vector causes absorption, and the real part leads to refraction. A difference in absorption of the two circular components causes the 2 Note that there are a number of useful characterizations of the refractive index in terms of various physical quantities such as the linear susceptibility X, the microscopic atomic polarizability o (see Problems 2.1 and 2.2), and the dielectric constant E, namely: n = vfi_ = JI+ 41rx ~ 1 + 21rx = 1 + 21rNo, where N is the atomic concentration.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS light to acquire elliptical polarization (Fig. 4.1 ). The difference in the real parts of the indices of refraction causes optical rotation.

As the light propagates through the atomic vapor, the two circular components acquire a relative phase shift of wf </) = - · Re(n+ - n_), (4.8)

C where l is the path length in the vapor. If </J = 1r, then the initially x-polarized light has become y-polarized light, i.e.,

## 0.6 ,-----------,--,------,r-----------

"'O 0.5 0.4 0.3 0.2 s- 0.1 (a)

c:: 0.0 ~----~--------11--------- !...-.--.J -~ -0.1 5 -0.2 0:: -0.3 -0.4 -0.5 -0.6 '----1..----L--..J~----Ji..-------1"'--L---L.-_L___..____J 0.6 0.5 0.4 "'O 9- 0.3 C: 0.2 C: s 0.1 0:: 0.0 -0.1 -0.2 nnali d d tunin (4.9)

FIG. 4.3 Magneto-optical rotation for one absorption length (l = lo). (a) Magneto-optical rotation angle c.p as a function of longitudinal magnetic field for the case of zero detuning (w = wo). (b)

Rotation angle as a function of detuning for b = 1 [i.e., Bz = i'o/(2gFµo)].

## KERR EFFECT IN AN ATOMIC MEDIUM

Finally, we can use our expression for the magnetic-field-induced difference in the refractive indices for a± light [Eq. (4.3)] in Eq. (4.9) to find the dependence of Faraday rotation on the magnetic field and the light detuning from resonance .6 = w - wo: (2~/,o)

2 + [1 + b2 - (2~/,o)2]2 ' ( 4.10)

where b = 2gFµoBz/,o.

Equation (4.10) can also be expressed in tenns of the unsaturated absorption length on resonance fo = ( 41rxow / c )- 1 ( defined for Bz = 0, the absorption length is discussed in Problem 3.5). Figure 4.3 shows the magnetic field and light detuning dependence of the Faraday rotation. 3 When .6 = 0, we have 21rxowf b f b i.p= l+b 2fo 1 + b2 .

( 4.1 I)

It is interesting to note that the integral of rotation over light detuning is zero [Fig. 4.3(b)]. This is because Faraday rotation arises due to a relative shift in the refractive indices for left- and right-circularly polarized light, and the frequency integral over each of them is zero.

4.2 Kerr effect in an atomic medium If a transparent isotropic material is subject to an external electric field, the field induces a uniaxial anisotropy in the medium, which modifies its optical properties.

In particular, light with linear polarization parallel to the direction of the field will experience a slightly different index of refraction compared to light linearly polar- ized perpendicular to the direction of the field (the Kerr effect). The difference in the indices of refraction can be detected, for example, by measuring the ellipticity induced in light which is initially linearly polarized at 45° to the field (Fig. 4.4 ): - KE21rl C - A' (4.12)

where K is the Kerr constant, E is the applied field, l is the length of the sample, and A is the wavelength of light in vacuum. From Eq. ( 4.12), we see that the Kerr 3 In the limit where b « 1, the rotation angle is zero when lw - wo I = 'Yo/2. In experiments where the homogeneous broadening exceeds the inhomogeneous broadening (e.g., measurements of pressure broadening), this propeny offers a convenient way to measure the homogeneous width "Y of the transition. It is also significant that the separation between the zero-crossings is linearly dependent on 'Y even when 'Y is much smaller than the inhomogeneous width.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS constant can be calculated from the difference of the indices of refraction for light with linear polarization parallel and perpendicular to the applied static electric field: K E 2 = n11 - n.1. .

(4.13)

Estimate the Kerr constant K for the following systems, assuming the energy levels are as the 1s2 1 S0 (I 1S) ), 1s2p 1 P1 (12P) ), and 1s2s 1 So (12S)) in He, for near infrared and visible light (note that the frequency W£ of such light is far from the 11S) ~ l2P) resonance): (a) A two-level atom (the I IS) and l2P) states).

(b) A three-level atom (all three of the above states).

(c) Make an order of magnitude estimate of the Kerr constant for liquid helium.

Hint The density of liquid helium is ~ 0.1 g/cm3, the refractive index of liquid helium is n ~ 1.028, the lifetime of the l2P) state for a free helium atom (which lies ~ 21.22 eV above the ground state) is ~ 0.56 ns. The electric dipole matrix elements connecting 12P, M = 0) with 12S) (d2) and 11S) (d1) states have the ratio d2 / d1 ~ 6.9.

~ ~· I Ji:- Potarizer +V Light Polarization -V PD2 A/4 r~ -(:; , ______ ~· ---.'7 l1 ,- / --k(_ PDl Kerr Cell t· I \ Analyzer · C)

FIG. 4.4 Simplified schematic of the Kerr effect measurement. PD I and PD2 are photodetectors.

Figure courtesy V. V. Yashchuk.

## KERR EFFECT IN AN ATOMIC MEDIUM

Solution (a) We will estimate the Kerr constant in the following way. First, we will deter- mine the light-dependent energy shift 8 of the lower state in the presence of the static electric field. Then, we will connect this shift to the refractive index using the following relations: 8 = --o:£ ' (4.14)

where a is the polarizability (see Problems 2.1 and 2.2) and 0£ is the magnitude of the dipole moment induced in an atom by the light electric field of magni- tude£ [the factor of 1/2 arises in Eq. (4.14) because the dipole moment itself is proportional to the applied field - see, for example, Problem 2.1] and ( 4.15)

where f. is the dielectric constant of the medium and N is the atomic concentration.

[Eq. ( 4.15) follows from the fact that the electric induction is V = f£ = £ + 41rNo.]

If we choose the direction of the applied static field E as the quantization axis, the effect of this field is to shift the ground state down by dr E 2 / ni.JJ p (where W p is the frequency of the I 1S) --+ l2P) transition) and to shift the M = 0 Zeeman sublevel of the upper state up by the same amount [see Eq. (2.21) in Problem 2.2].

The wavefunctions of the lower and the M = 0 component of the upper states mixed by the electric field [ obtained by expanding the solutions of the two-level secular equation in the small mixing parameter d1E/(hwp ), see Problem l.4(b)]

are: ( 1 drE )

d1E .

la) ::::: 1 - 2 li,2wi I1s) - hwp I2P, M = 0), (4.16)

d1E ( 1 drE )

lb) ::::: hwp I1S) + 1 - 2 li,2wi l2P, M = 0) .

(4.17)

(Note that the factors of 1 /2 multiplying the dr E 2 / ( li2wi) terms in the above equations come from normalization of the wavefunctions la) and lb), and we keep only terms up to second order in E in the expansion.)

The dipole moment can be calculated from the lifetime r using the following relation (see Problem 3.3): 1 4wi 1 T - 31ic3 2J' + 1 l(1Slldll2P)I ' (4.18)

where J' = 1 is the total angular momentum of the upper state, and (ISi ldl l2P)

is the reduced dipole moment [the Wigner-Eckart theorem (Appendix F) relates

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS (1Slldll2P) to d1]. Perfonning this calculation, one obtains _ l(1Slldll2P)I ~ O 42 di - J3 ~ • eao .

(4. I 9)

Consider now the case of the light field parallel ~o the static field. Using tbe wavefunctions (4.16) and (4.17) perturbed by the static field as the new basis, 011e finds for the dipole moment between the upper and the lower state: ( 2djE )

dab = (bldla) = 1 - ri2wi di · (4.20)

The light field couples la) and lb), leading to a light-induced shift described by d2 e,2 811 ~ - hw : 2~ (4.21)

p p (4.22)

(4.23)

where we used wp - we~ wp.

A similar calculation for the light field perpendicular to the static field yields: d~£ ( 2d~ E )

8 .1 ~ - t;, • r,,2 2 · ( 4.24)

1,wp Wp From Eqs. (4.14) and (4.15), we see that n - 1 is proportional to the light- induced shift: We have n - 1 ~ 21rNo = -41rN £2 • (4.25)

41rN nu - n.1 ~ £2(8.1 - 811)

~ _ 4 N d~ (4d~E )

~ 7r t;.

• r,,2 2 1,wp Wp 4d2E 2 = - ri2i 2 ( n - 1) ' Wp (4.26)

(4.27)

(4.28)

where we define n-1 = 41r N di/ ( hw p) to be the index of refraction in the absence of the static field.

## KERR EFFECT IN AN ATOMIC MEDIUM

2S 2P hw11··-·1.· /::.----"'- hw1:.·- ! ..

hw1; liw1;.

IS FIG. 4.5 Kerr effect as a four-wave-mixing process. The Kerr effect in the static field is obtained in the limit w E ~ O; W£' ~ we. The 12S) state plays a significant role in the process as discussed in the text even though it does not couple to the I IS) state directly, and there is no resonant enhancement of the effect.

Consequently, from Eq. ( 4.13), we have (4.29)

(b) In the above estimate we have neglected the effect of the 12S) state of He. This state is very close in energy to the l2P) state, and, in fact, gives the dominant contribution to the electric polarizability of the latter. For this reason the 12S) state plays an important role in a realistic treatment of the present problem.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS The light-medium interaction responsible for the Kerr effect can be thought of as a nonlinear optical four-wave mixing (x( 3)) process, 4 where three low- frequency fields(£, E, and E) produce a new field(£'). Processes of this type may be represented by emission-absorption diagrams and by Feynman diagrams (see, for instance, Delone and Krainov ( 1988) and Appendix H], examples of which are shown in Fig. 4.5.

Let us compare the amplitude corresponding to a diagram with I1S) as the intermediate state to that with 12S) as the intermediate state (permutations of the static fields do not change anything, and we do not consider them). Using the Feynman diagram rules (Appendix H), we write the vertices and propagators for the case with I 1 S) (we = we,): d4 d4 v; 1S CX ---------- + (wp -we)(-we)(wp -we)

(wp + we)(wc)(wp + W£)

4d4 ~--1 .

Wp For the case with 12S) as the intermediate state, we have: (4.30)

TT d~d~ dyd~ v2s OC -----____,;;_--=------- + ------------ (wp -wc)(w2s - we)(wp - W£)

(wp + we)(w2s + W£)(Wp + w£)

(4.3 I)

Comparing the two amplitudes, we see that since d2 ~ 6.9d, the amplitude with I2S) as the intermediate state is greater than that with I1S) by a factor~

## 24. We

can therefore neglect the amplitude with I1S). (Note that although each individual diagram with 1S is "resonantly" enhanced due to the presence of a small quantity W£ in the denominator, the two diagrams different by the order of absorption and emission of light quanta nearly cancel. It is also important to note that the effect on the phase of light we are interested in is proportional to the forward scattering amplitude given by the Feynman diagrams, rather than its absolute value squared.)

Finally, based on our calculation of V1s and V2s, for the three-level system, in place of Eq. ( 4.29), we can write K ~ fi2 2 ( n - I)

Wp by replacing the factor -4d~ in Eq. (4.29) with the factor +2d~.

4 For an introduction to nonlinear optics, we recommend the book by Boyd (2003).

(4.32)

## THE HANLE EFFECT

(c) For the purpose of the estimate, we model the liquid as a collection of free atoms (which works for helium, but is generally a poor approximation for molecular liquids). Substituting the values of d2, /iwp_ n given in the hint yields I K ~ 2 x 10- 14 (kV/cm)- 2 · I (4.33)

As a numerical example, for the setup shown in Fig. 4.4, a I 0-cm long sample, A= 1 µm, and E = 50 kV/cm, the induced ellipticity is f rv 2 • 10- 5 .

This should only be considered an order of magnitude estimate because the optical properties of the actual He system are not well-described by the three-level model that we adopted here. In fact, in this model the index of refraction n is [using Eqs. (4.14) and (4.15); 12S) plays no role in this estimate]: 41rNdy n - 1 ~ --- .

ilWp (4.34)

Substituting the numbers for liquid He, we find n - 1 ~ 8 · 10- 3, which is smaller than the experimental value for He gas scaled to the density of liquid He by a factor of~ 4.

4.3 The Hanle effect Consider the experimental arrangement shown in Fig. 4.6, where an ensemble of atoms with ground state angular momentum J = 0 is located in a small volume centered at the origin. At time t = 0, the atoms are exposed to a short pulse of circularly polarized photons propagating along x, which drive a transition to an excited state with J = I. The atoms are in a magnetic field B = B0z. Because the incoming light is circularly polarized, the excited atoms initially have a projec- tion of angular momentum along x equal to Ii (or -Ii). However, the polarization vector then precesses with frequency nL (the Larmor frequency, proportional to B) because the excited atoms have magnetic moments (see, for example, Prob- lem 2.6). The excited state has a finite lifetime r = 1/,. When an atom decays it may emit a photon into the solid angle subtended by the detector, which lies along the y-axis. The detector contains a circular polarization analyzer, so that only positive-helicity (a+) fluorescence photons are detected.

What is the time dependence of the detector signal? How does the signal change with the sign of circular polarization of excitation photons and with the strength of the magnetic field Bo? Explain how one could use the described phenomenon, known as the Hanle effect, for excited state lifetime measurements.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS ·- • z --- ircularly polariz d light b am -- e)o t cor ---------'-- Atomic vapor FIG. 4.6 Schematic setup for an experiment measuring the Hanle effect. An atomic vapor at the origin is illuminated by a pulse of circularly polarized light propagating in the x-direction. A detector equipped with a circular polarization analyzer is positioned along the y-axis. The atomic vapor is immersed in a magnetic field jj which points in the z-direction.

Solution In this problem it is convenient to use different quantization axes in different steps of the solution. To describe the population process, we choose the quantization axis along x. Then the J = 1 states excited by left- and right-circularly polarized (u + and u _, respectively) photons are just IJ = 1, m = 1) = G) , (4.35)

IJ = 1,m = -1) = G) .

(4.36)

respectively.

Since the magnetic field is in the z-direction, in order to describe the pre- cession, it is convenient to choose the quantization axis along z. Note that an appropriate coordinate frame is obtained from the one we used to describe popula- tion by an Euler rotation (a = 0, {J = -1r /2,, = 0) given by the following J = I rotation matrix 1>( a, {J, 1) (Appendix E): 1 -[½ 1>{0, -7f /2, 0) = [½ -[½ .

(4.37)

[½ I

## THE HANLE EFFECT

Applying TI(O, -1r /2, 0) to the IJ = 1, m, = ±1) states gives l·~;(t = o)} = ~ ( ±(2)

, (4.38)

where the two signs correspond to the two possible circular polarizations of the incident photons. According to the time-dependent Schrodinger equation, the temporal evolution of this wavefunction is described by (4.39)

Here nL = gµoBo is the Larmor frequency (g is the appropriate Lande factor), and we have included the amplitude decay (hence 1 /2, not 1 in the exponential factor) due to the natural lifetime of the excited state. Finally, detection is most conveniently described in a frame with quantization axis in the y-direction. This frame is obtained from the previously used one by an Euler rotation (o = 1r /2, {3 = 1r /2, 1 = 0), so the wavefunction in the new frame takes on the form (see

## Appendix E):

l'l/J' ( t)) = -v'½ 1 2 v'½ e-,t/2 (ie-ind)

·-- ±\1'2 ·n -ieiu,.,t ( ±½ + ½ sin nLt)

_ J2 sin fht e -'Yt/ 2 .

=t=½ +½sin 0Lt (4.40)

(4.41)

The detector signal S ( t) is proportional to population of the m = 1 sublevel, and to the spontaneous decay rate: (4.42)

This represents a decaying oscillatory signal: the detector sees maximum signal when the angular momentum precesses in such a way that it is "pointing" towards the detector. 5 If the temporal resolution of the detector is much better than 1 / 1, the lifetime can be measured by fitting the observed time dependence to the expected dependence obtained above with 1 = I/, being a free parameter.

5 This statement is true when fh » ,. If, is large, the decay shifts the maxima in the detected intensity.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS ~ &> ·- f./)

0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1 \ \ Normalized Larmor Frequency (QJy)

FIG. 4. 7 Time-integrated Hanle signal as a function of Larmor frequency for left- and right-circu- larly polarized excitation light (solid and dashed curves, respectively). Fits to the curves allow one to extract the excited-state lifetime.

If the temporal resolution of the detector is poor (or the lifetime is short), the lifetime can be determined by measuring the dependence of the time-integrated signal on the magnetic field. The time-integrated signal is given by (X)

r ( 3 OL , )

S(OL) ex lo S(t)dt = 4 2, ± 2 ,2 + nj, - 2 ,2 + 40j, .

(4.43)

The signal S ( n L) is plotted as a function of the Larmor frequency in Fig. 4. 7. Note that the characteristic width of the dispersive part of the profile is , .

4.4 Electric-field-induced decay of the hydrogen 2 2 S112 state In hydrogen, the 2 2S 112 state lies higher in energy than the 2 2 P 1; 2 state by the Lamb shift <5 = 1058 MHz. In the absence of external electric fields, the 2 2 S 112 state has a very long natural lifetime(~ 1/8 s) and decays by two-photon emission to the ground 1 2 S 1; 2 state. The 2 2 P 1; 2 state has a short lifetime ( r2p ~ 1.6 x 9 s) since it can decay by single-photon electric dipole (EI) emission to the ground state (Lyman o line). When an external electric field is applied, the 2 2S 1; 2 state acquires an admixture of the 2 2 P 1; 2 state and its lifetime is shortened.

## ELECTRIC-FIELD-INDUCED

DECAY OF THE HYDROGEN 2 2 s112 STATE (a) For weak electric fields e, show that if the 2 2S112 state is populated at time t = O, its population decays with inverse lifetime (4.44)

where Wsp = 21r6 is the Lamb shift. Explain which electric fields can be considered "weak."

(b) Evaluate rate = 10 V /cm.

Solution (a) Suppose the electric field is applied in the z-direction. Consider a two-level system formed by the states 12 2S1;2, MJ = 1/2) and 12 2 P1;2, MJ = 1/2) (to simplify notation, we will subsequently denote the 2 2S1; 2 state as 2S and the 2 2 P 1; 2 state as 2P). The Hamiltonian for this system in the presence of an electric field is given by (where we set Ii = 1): H- (Wsp -de)

- -de -i,/2 .

(4.45)

Here the energy of the unperturbed 2 2 P1;2 state is chosen to be zero (we neglect the width of the 2S state) and the dipole moment d is given by d = -e(2S, MJ = 1/2lzl2P, MJ = 1/2)

(4.46)

= -e(2, 0, OI( +lz ( JI 12, 1, 1} 1-) - If 12, 1, O}I+})

(4.47)

e e = -(2,O,Olzl2,l,O)

= lil(2,O,Olrcos0l2,l,O), (4.48)

J3 v3 where we have used the notation In, l, m,) for the spatial wavefunctions and for the electron spin states we have employed our common notation in which lms = ±1/2) = 1±). We can evaluate the expression ford using the appropriate hydrogen wavefunctions [Eqs. (1.261) and (1.263)]

1 r 'l/J210(r,8,¢) = -- -e-r a 0 cos0 412-ir 312 ao v ~1r a0 _ _1_ ( _ ~)

-r/2a 'I/J2oo(r, 0, <P) - 2v/ifi a~/2 1 2ao e , and integrating. We find that d= -Jaeao.

(4.49)

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS Returning to the Hamiltonian matrix H, we see that since th~ electric field perturbation is nondiagonal, it does not cause first-order energy shifts. The wave- functions do, however, acquire first-order corrections. The perturbed wavefunctio corresponding to the 2S state, 128), is found by substituting A :::::: wsp (since t/ .

e energy is not shifted to first order) into the secular equat10n ( Wsp - ,\ -de ) . (a)

= 0 -de -i,/2 - ,\ b ' (4.50)

where b (lbl << lal) is the small admixture amplitude of the 2P state into the 28 state. Equation ( 4.50) indicates that b de -~----.

a W8p + i,/2 (4.5 I)

The decay rate of 128)

is given by the relative probability of finding atoms in the admixed 2P state times the 2P decay rate: d2e2 3,e 2a~e2 r = 1 w~ + 12/4 = !t2(wiv + 12/4) ' (4.52)

as advertised. The "weak" field condition is I ld£1«wsp· (4.53)

In the opposite case of ldel >> Wsp, the lifetime does not depend on e, as the 2S and 2P states are fully mixed, and the lifetime of both eigenstates is ~ 2r.

(b) We have the following values for the parameters in Eq. (4.52): which gives us Wsp = 21r X 1.058 X 109 s- 1; I = 6 X 108 s - l ; e = 10 V /cm= 30 esu/cm;

## 4.5 Stark-induced transitions (T)

(4.54)

(4.55)

(4.56)

(4.57)

Single-photon electric dipole (El) transitions between states In) and Im) of the same parity are forbidden [neglecting the effects of parity nonconservation (PNC)

STARK-INDUCED TRANSITIONS (T)

which are usually very small, see below and Problem 1.13]. However, a nonzero El transition amplitude between these states may be induced by application of a static electric field IE, which mixes states of opposite parity to both states In) and Im).

Such Stark-induced transitions (Bouchiat and Bouchiat 1975) have been used in several atomic-parity-nonconservation experiments [see, for example, Conti et al. ( 1979), Bouchiat et al. ( 1982), Wood et al. ( 1997), Nguyen et al. ( 1997), Guena et al. (2003)). The transition rate W between same-parity states has contribu- tions from both the Stark-induced transition amplit~de As and the parity-violating transition amplitude Apnc - the overall rate has an mterference term: (4.58)

The experimental method in which the interference term 2Re ( AsA~,_c] is mea- sured in order to determine Apnc is known as the Stark-interference technique.

This technique serves both to enhance the PNC signal (which is now proportional to 2Re[A 8A~c] as opposed to 1Apncj2)

and provide a method for distinguish- ing the PNC signal from background effects (since, for example, the PNC signal 2Re [ A 8A~c] reverses with the sign of the electric field).

(a) Show that the Stark-induced transition amplitude between the same-parity states Im) and In) can be represented as As = r(O) · (mlU(O) In) + T(l) · (mlU(l) In) + r( 2) · (mju( 2) In) , (4.59)

where T(tt) are the rank K irreducible parts of the reducible second-rank tensor formed out of the light electric field £ and the static electric field IE, (4.60)

and u(tt)

are the rank K irreducible parts of the appropriate tensor formed from atomic vectors.

What is the form of the matrix element (mlUijln)?

Solution Stark-induced transitions occur when the static electric field IE mixes states lrn)

and In) with opposite-parity states, and then the light field e drives transitions between the mixed states. Based on this physical picture, the transition amplitude can be written as (4.61)

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS where dis the electric-dipole operator, the sum goes over the intennediate states IP) of parity opposite to that of states In) and Im), En, Em, and Ep are the respec- tive unperturbed energies of the states fn), Im), and IP), and the two terms in (4.61) correspond to mixing of states IP) to the final and the initial state, respec- tively. Equation (4.61) can be expressed in the following form (where the sum over the repeated indices i, j, pis assumed): (4.62)

Factoring out the electric fields (which obviously commute with the atomic wavefunctions and operators), we write (4.63)

Thus the Stark-induced amplitude is described by the contraction of the rank-two tensor T (where Tij = lEiej) with the rank-two tensor U: (4.64)

The contraction of two rank-two tensors can be evaluated by first expanding each of the tensors into irreducible components ( of rank zero, one, and two), and then taking the sum of scalar products of the irreducible components of the same rank K (since the scalar product can only be formed between tensors of the same rank, see Appendix F). Thus the scalar product of T and (ml UJn) can be expressed in the fonn (see, for example, Varshalovich et al. 1988): (4.65)

(b) Write out the explicit form of the irreducible rank"' = 0, 1, 2 tensors built from the electric fields in the spherical basis.

Hint The general procedure for finding the explicit decomposition of a reducible rank ""

tensor built from two irreducible tensors of rank K1 and K2 in terms of irreducible spherical tensors is as follows. If one has an irreducible rank K1 tensor AK• and an irreducible rank "'2 tensor ]BK2, one can form the irreducible tensor product of

STARK-INDUCED TRANSITIONS (T)

rank "' (Varshalovich et al. 1988): (A"' 0B" ); = L (11:1,Q1,K2,q2l11:,q)A;/B;;.

(4.66)

Q1,Q2 One can also carry out the inverse decomposition of the rank Ii 1 + K2 reducible tensor A;/ IB;; according to K1+K2 ~ K11I])K2 - ~ (K1 QI K2 q2 IK q) (A K1 tO\ 1I])K2 )"

/"a.QI JIJ)Q2 - ~ ' ' ' ' 16' JD)

Q ' (4.67)

K=IK1 -K2I where q = q1 + q2.

The reducible rank-two tensor T, which is fonned from the two irreducible rank-one tensors 1E and l, can be decomposed into irreducible rank "' = o, I, 2 tensors T(K), whose components are given by r; = L (I,q1, 1,q2l11:,q)1EqJ:q2.

(4.68)

Q1,Q2 Solution One may expect that the rank-zero part of the reducible tensor T should be pro- portional to the scalar product 1E · l. Let us show this result formally, using the mathematical techniques discussed in the Hint. The electric-field vectors lEi and ei are irreducible rank-one tensors, which can be expressed in the spherical basis according to the formulae (F.23)-(F.25) given in Appendix F: lE± 1 = =F ~ (lEx ± ilEy) , lEo = lEz , ( 4.69)

£±1 = =F ~(£x ± i£y), £0 = £z .

(4.70)

According to Eq. ( 4.66), the irreducible rank-zero tensor product of 1E and l is (JE1 0 t:1)0 = _1_ 1E1t:1 __ 1_ JE1t:1 + _1 1E1 e1 O v'3 1 -1 v'3 0 0 v'3 -1 - = - v'3(1Ext'.x + lEyt'.y + 1Ez£z) = - v'3 lE · e , (4.71)

which differs by a numerical factor from the scalar product of the vectors. Thus for T8 we have (4.72)

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS As we know, the only rank-one object that can be formed out of two vectors is the vector product, so TJ ex ( E x l) q. This can be seen formally by canying out the same procedure we used above to find T/J: (4.73)

and so on. In Eq. (4.73), we made use of Eqs. (4.69), (4.70) and (4.66). In general we find the relation ' so the rank-one irreducible tensor components are given by I 'l (- -)

Tq = J2 IE x e q .

For the rank-two components, we have where according to Eq. (4.66), (4.74)

(4.75)

(4.76)

(4.77)

(4.78)

(4.79)

(4.80)

(4.81)

Similarly to how we have expressed the tensors T(tt)

in the spherical basis [Eqs. (4.72), (4.75), and (4.76)], the tensors u<tt) can also be expressed in the spherical basis. The Stark-induced transition amplitude can then be expressed

STARK-INDUCED TRANSITIONS (T)

in terms of irreducible spherical tensors [ using Eq. ( 4.65) and Eq. (F.31) from

## Appendix F]:

1 (- -)

o '°' i (- -)

As= - v'3 IE-£ (mlUoln) + ~ /2{-l)q IE x £ /m.lU~qln)

q + L{-l)q(IE 1 ®£ 1):(mlU~qln).

(4.82)

q (c) Use the Wigner-Eckart Theorem (Appendix F) to write the Stark-induced tran- sition amplitude between states Im,, F', !vi') and In~ F, AJ) in terms of Clebsch- Gordan coefficients.

Solution From Eq. ( 4.82) and the Wigner-Eckart theorem (F.1 ), we find for the Stark- induced amplitude: A = __ I (1E -l) (m, F'IIUolln, F) (FM O OIF'.

kf')

s y'3 J2F' + 1 ' ' ' , + ~(-I)M-M'(i Xe)

(m,F'IIUllln,F)

(F,M, l,M' - MIF' M')

y'2 q=A/-A/' J2F' + 1 ' + (-l)M-M' {IEl 0 et)K=2 (m, F'IIU211n, F) (F Af 2 Af' - !vllF' !vi')

q=M-M' J2F' + 1 ' ' ' ' .

(4.83)

In the literature [see, for example, Bouchiat and Bouchiat ( 1975); Drell and Commins ( 1985); Bowers et al. ( 1999); Bennett and Wieman ( 1999)], the Stark- induced amplitude is defined in terms of the real parameters o, {3, and 1, known as the scalar, vector, and tensor transition polarizabilities, respectively. These param- eters correspond to the three terms in the above expression. Unfortunately, there does not seem to be a universal convention on how to normalize these parameters.

In cases where the I tenn is zero (see part (d)), o characterizes the Stark-induced amplitude for collinear static electric field and light polarization, while {3 charac- terizes the amplitude when the light polarization is orthogonal to the static field.

In the case of transitions between s 1; 2 states (for example, the 6s 1; 2 ~ 7 s 1; 2 transition in Cs where parity-violation experiments have been carried out), the Stark-induced transition amplitude between states with total angular momenta F and F' can be conveniently written as: As= a i. e 6F,F'6M,M' + i,B(i X l). (F'M'l81FM)' (4.84)

where a is the Pauli spin operator.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS ( d) Discuss the angular momentum selection rules for transitions described by these polarizabilities.

Solution Angular momentum selection rules for various terms in Eq. (4.84) are the usual ones for tensors of appropriate rank; see Table 4.1. These selection rules follow from the properties of the Clebsch-Gordan coefficients.

Depending on the transition, different combinations of o, {3, and , may con- tribute. For example, for F = 1/2 --+ F' = 1/2, the electric-field-induced transition amplitude has a scalar and a vector component (Bouchiat and Bouchiat 1975), while for F = 0 ~ F' = 1, only the vector amplitude contributes.

TABLE 4.1 Various contributions to the transition polarizability and the corresponding selection rules for the total angular momentum F.

Q f3 ' Rank I Selection rules ~F=O tiF = 0, ± 1; 0 -++ 0 tiF = 0, ±1, ±2; 0 -++ 0; ! -++ !; 0 -++ 1; 1 -++ 0 (e) Discuss the limits of the approximations employed in the above analysis.

Solution In this tutorial, we have used first-order perturbation theory, which correspond- ingly limits the applicability of the result. In particular, the present results are only valid when the Stark shifts of the levels involved are much smaller than separations between these levels.

## 4.6 Magnetic deflection of light

Magneto-optical effects are usually observed by measuring how the Stokes param- eters (Appendix D) change when a light field traverses a medium exposed to a magnetic field [see Problems 4.1, 4.3, and 4.7, as well as the review by Bud- ker et al. (2002)]. Here we consider another magneto-optical effect, observed by Schlesser and Weis ( 1992): the deflection of a light beam as it passes through a medium immersed in a magnetic field.

## MAGNETIC DEFLECTION OF LIGHT

......

--------k ......

H <p ......

B ......

D FIG. 4.8 Geometrical relationship between the wave vector k, the induction vector jj and ma .

_ - gnet1c field H of the I ight, and the static magnetic field B applied to the medium.

Consider an isotropic medium to which a homogeneous magnetic field B is applied.

(a) Recall that the components of the induction vector jj are related to the components of the electric field E via (4.85)

where €ij is the dielectric permeability (permittivity) tensor. From symmetry considerations, show that Eij is given by: (4.86)

where f and i' are frequency-dependent complex scalars, and fijk is the Levi-Civita totally antisymmetric tensor.

(b) Show that if a linearly polarized wave with wave vector k enters such a medium perpendicular to its boundary, the Poynting vector - C ...

- S = 41rE x H, (4.87)

inside the medium (i.e., the direction of energy flow in the light beam) has a time- averaged value given by: - cE5 [,..

( - ,..

- ) ]

(S) :::::: B1r k + Im(i) sin cp cos cp B + sin cp (k x B)

, (4.88)

where E and ii are the electric and magnetic fields of the light, respectively, c.p is the angle between the incident light polarizati~n and the magnetic field B, and B is assumed to lie in the plane perpendicular to k (Fig. 4.8). Assume a nonmagnetic, weakly absorbing medium: Im(€), llm(i'B)I << Re(f) ~ 1.

The quantities E and B are the magnitudes of the optical electric field and the applied static magnetic field, respectively, and Eo is the amplitude of the optical field [i.e., E = Eo cos(wt), where w is the light frequency].

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS vapor cell FIG. 4.9 The change in the direction of E, and hence the Poynting vector S, inside a medium (e.g., an atomic vapor) leads to deflection of the light beam. The geometry shown in the figure is optimal for observation of deflection and corresponds to r.p = 1r /2 (see text).

(c) For the most favorable geometry, estimate the magnitude of the magnetic-field- induced deflection of a laser beam upon traversal of a cell of length £ containing resonant atomic vapor (Fig. 4.9).

Hint In part ( c ), make use of the fact that the component of the dielectric tensor e ..

responsible for magneto-optical phenomena such as magnetic-field-induced cii- cular birefringence and dichroism (Problem 4.1) is also responsible for magnetic deflection. Since the complex index of refraction is related to c via n= \I'€, (4.89)

one can use the fonnulae from Problem 4.1 to determine the magnitude of the magnetic-field-induced change of the refractive index.

Solution (a) The first tenn in Eq. ( 4.86) is the usual form of the permittivity tensor [see, for example, Griffiths ( 1999) and the text on Electrodynamics of Continuous Media by Landau et al. (1995)) for isotropic media. For such media, there are no preferred directions, and the induction vector fJ has to be collinear with E: D = eE.

(4.90)

When the magnetic field is applied, there appears another possibility of build- ing a vector quantity out of the vectors of the problem ( or more precisely, a vector of the light electric field E and the pseudovector B): B x E. This is represented by the second tenn in (4.86). The factor i is written explicitly in this term because the quantities e and i must be real in the case of transparent media. The relation between fJ and E should be invariant with respect to reversal of time. Both D

## MAGNETIC DEFLECTION OF LIGHT

and E are time-reversal-invariant (T-even), but Bis T-odd. Since under time rever- sal one should take complex conjugates of all operators (see Problem 1.13), the .; ensures the proper time-reversal symmetry.

(b) Since the light enters the medium at normal incidence, the direction off does not change. The direction of the magne~ic ~eld of ~e light is also unchanged. It follows from Maxw~}l's equations that k, D, and H are mutually perpendicular.

Thus the induction D is directed along the electric field of the incident light, i.e., along k xii. However in general, the electric field in the medium Eis not collinear with D.

From Equation (4.86), we write: (4.91)

Since ii = k x E, in order to find the Poynting vector, one needs to evaluate: § = 4: £ x ( k x E) .

(4.92)

Applying a well-known vector identity, (4.93)

we have __ cE2 [: _ ( k · E)]

S-- k-E E 2 .

41r (4.94)

First, we evaluate k • E using ( 4.91) and the fact that k · D = 0 (Fig. 4.8): (4.95)

where we have neglected tenns ex: i 2 B 2 • Since B x D is along k (Fig. 4.8), and the magnitude of the induction vector D ~ f E, we have " - i:YBE k • E ~ _ sin <.p • (4.96)

Thus we have for the Poynting vector _ cE ["' (B) -J S ::::: 4 1r k - ii D sin <pD , (4.97)

where again we ignore tenns ex: i 2 B 2•

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS Since k.l..B, we can resolve _ _ ( D. B) (.... _) [ D. ( kx B)]

D=B B2 +kxB B2 · (4.98)

Using Eq. (4.98) in (4.97), we obtain Eq. (4.88): _ cE2 [ ,,.

( - ,..

- ) ]

(S) ~ S1ro k + Im(')') sin <p cos <pB + sin <p(k x B)

.

Here we have taken into account (by taking the real part of the second tenn) that only the component of the light magnetic field in-phase with the electric field contributes to the average Poynting vector (4.87), and used the time average of (E 2) = EJ/2.

(c) From (4.88) it is seen that the largest deflection occurs at r.p = 1r/2.

In order to estimate the magnitude of the displacement for a near-resonant vapor, we follow the suggestion outlined in the hint to say that the magnitude 8n of the magnetic-field-induced change of the complex refractive index of the medium can be estimated as (see Problem 4.1 ): 6n ~ gµB (n - 1).

r (4.99)

Here gµB is the Zeeman shift. r is the width of the transition (e.g .• Doppler width), n is the magnetic-field-independent complex refractive index, and a weak magnetic field is assumed (lgµBI << r).

In the vicinity of a resonance, the maximal magnitudes of the real and imaginary parts of n - I are comparable, and can be estimated from 41rlm(n) lo/A f"'V 1, (4.100)

where lo is the absorption length (Problem 3. 7) and ,\ is the wavelength of light. Using this, we can estimate the magnitude of the relevant magnetic-field- dependent tenn in the dielectric tensor: I gµB ,\ Im(i)B f"'V ----. 41r r lo (4.101)

Using ( 4.10 I) and ( 4.88), we find that upon traversal of a length f in the medium, a light beam is deflected by: (4.102)

Note that the scale of the displacement is detennined by the wavelength.

CLASSICAL MODEL OF AN OPTICAL-PUMPING MAGNETOMETER In the work by Schlesser and Weis ( 1992), a room temperature vapor cell with f / lo rv 1 was used. Light was tuned to the D2 line (852 nm), and a magnetic field of 50 G corresponding to gµB/r "'..I 0.1 was applied. The observed beam displacement was rv 30 nm.

4. 7 Classical model of an optical-pumping magnetometer Figure 4. IO depicts a schematic diagram of an optical-pumping magnetometer operating in the so-called NI x scheme (the origin of this terminology will become apparent later on in this problem).

Circularly polarized resonant I ight Alkali metal vapor cell Magnetic coil ( rt)

A Z Photodetector Lock-in amplifier Reference -------1 Voltage -controlled oscillator Phase rotator Frequency counter (output)

FIG. 4.10 A simplified schematic of an optical pumping magnetometer of the Alx type.

The central element of the magnetometer is a cell containing the vapor of one of the alkali metals, usually Rb, Cs, or K. The vapor is illuminated with circularly polarized light resonant with either the DI or D2 transition. The intensity of the transmitted light is detected with a photodetector connected to a phase-sensitive (lock-in) amplifier. The reference for the lock-in amplifier is provided by an oscil- lator that also drives radio-frequency current through a magnetic coil surrounding the vapor cell. The magnetic field produced by the coil is collinear with the light propagation direction. The frequency of the oscillator is controlled by the (nearly de) voltage at its input provided by the output of the lock-in amplifier.

In this problem, we will show that under proper operating conditions, the photodetector signal and the rf magnetic field oscillate at the Larmor frequency

## INTERACTION

## OF LIGHT WITH ATOMS IN EXTERNAL FIELDS

corresponding to the field H. Measuring the frequency (for example, with a fre- quency counter) it is possible to determine the magnitude of H using the known value of the gyromagnetic ratio.6 In order to provide the simplest model of the magnetometer while still retain- ing its salient features, we will make a number of simplifying assumptions. First, instead of considering the quantum mechanical problem involving the rather com- plicated hyperfine-structure energy levels of the alkalis, we will model atoms as classical spins with gyromagnetic ratio 1, such that the spin exposed to a static .....

magnetic field H precesses around the direction of the field with Larmor fre- .....

quency 1 H. The component of the magnetization along H relaxes at a rate r 1 .....

(longitudinal relaxation), and the components perpendicular to H relax at a rate r2 (transverse relaxation). 7 Second, we will assume that the amplitude of the rf magnetic field is small compared with H and will neglect the component of the rf .....

magnetic field along z, the direction of H. This component leads to a fast mod- ulation of the Lann or frequency, which is not important for us here. Third, the remaining component of the rf magnetic field which oscillates in the direction perpendicular to z can be resolved into two counter-rotating components, one of which rotates in the same direction as the magnetic moments, while the other rotates in the opposite direction. Since we will be considering near-resonant con- ditions (i.e., when the rf frequency is close to the Larmor frequency), we will neglect the latter component (the rotating wave approximation - see Problem 2.7).

Let us assume that the optical pumping rate and the relaxation rates are all much smaller than the Larmor frequency. Then, in the absence of the rf magnetic field, there is a steady-state magnetization (which we designate Mo) along z. Indeed, while optical pumping produces magnetization at an angle to z, Larmor precession spreads the magnetic moment vectors, so their tips are unifonnly distributed on a circle in the xy-plane, so only the z-component "survives" averaging over the atomic ensemble. 8 6 For precise magnetic field measurements in the Eanh-field range where Mz magnetometers are commonly used, it is necessary to take into account the nonlinearity in the Zeeman energy shifts due to the mixing of different hyperfine components of the alkali atom ground states caused by the magnetic field (Problem 1.4 ).

7 The difference between the transverse and longitudinal relaxation in an ensemble may arise when individual spins precessing in the magnetic field ··see" slightly different magnetic fields (Prob- lem 2.8). In this situation, if, for example, the spins are originally oriented in the same direction at an angle to the magnetic field, they will eventually spread around due to unequal precession rates, so the transverse magnetization would vanish, while longitudinal magneti7.ation would persist. It is always true that r 2 > r l • 8 No net magnetization is created in the special case of ii perpendicular to the light propagation direction. This results in the appearance of a .. dark zone" of the magnetometer - an orientation of the device where it loses sensitivity to the magnetic field. Another such dark zone in the case of Mz magnetometers is when the magnetic field ii is along the light propagation direction, so the field applied by the rf magnetic coil is entirely longitudinal.

CLASSICAL MODEL OF AN OPTICAL-PUMPING MAGNETOMETER (a) Write down the differential equations describing the classical evolution of the Cartesian components of the magnetization, including the effects of both the static and rotating magnetic field and the longitudinal (r 1) and transverse (r 2)

relaxation.

(b) Find the steady state solution of these equations. Consider the cases of r 2 = r 1 and r2 >> r1.

(c) Referring to Fig. 4.10, explain the origin of the modulation of the light transmission signal. What is the purpose of the phase rotator?

Hint It is convenient to write the equations in the rotating frame, i.e., the frame in which the rotating rf field is static. First write the equations neglecting relaxation, and then add the relaxation terms "by hand." The resulting equations are known as the Bloch equations, as they were first derived in 1946 by magnetic resonance pioneer Felix Bloch.

Solution (a) The gyromagnetic ratio , is the proportionality coefficient between the - - magnetic moment of an atom M and its angular momentum F: - - M=,F.

(4.103)

The time derivative of the angular momentum due to the magnetic torque is: dF' - - dt = M X Ht, (4.104)

where Rt is the total magnetic field (static plus rotating), so that [multiplying both sides of Eq. (4.104) by, and using (4.104)]

dM - - &=fMXHt, (4.105)

Next, in order to eliminate explicit time dependence of the magnetic field, we go to the frame co-rotating with the rf field at frequency w. The time derivatives of the magnetic moment in the rotating frame and the lab frame are connected

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS according to (see Problem 2.6)

(4.106)

We will conduct the calculation in the rotating frame [coordinates x', y', z], and will not write the subscript. Rewriting Eq. (4.106) in terms of Cartesian compo- nents, assuming that the rotating field is pointing in the x' -direction, and adding the relaxation terms, we obtain the sought-for Bloch equations: d:x' = "(My' ( H - ~) - r 2Mx 1 , (4. 107)

d:y' = -"(Mx,(H - ~) + "(MzHr - f2My 1 , (4.108)

dMz ( dt = -"(My,Hr - f1 Mz - Mo) .

(4.109)

Here Hr is the magnitude of the rotating field and Mo is the equilibrium magne- tization in the absence of the rf field. Note that we have chosen the direction of the rotation of the rf field so that the magnitude of the z-directed magnetic field is reduced in the rotating frame.

(b) Setting to zero the derivatives on the left-hand-side of Eqs. ( 4.107 ,4.108,4. I 09)

(which we are allowed to do because the problem is stationary in the rotating frame), we obtain an inhomogeneous linear system Here ~ = ,H - w, and Wr magnetization, we obtain: (4.110)

,Hr.

Solving for the components of the Wr~ (4.111)

(4.112)

(4.113)

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

On resonance (Ll = 0), we have: Mx' =0, Wrf2 Wrf1 A1y' = lvfo r = Mo---- r~ + riw; r1r2 + w;' Mz = Mo q = Mo r 1r 2 f 2 + G.w 2 f I f2 + w 2 ' r1 r r ( 4.114)

(4.115)

(4.116)

i.e., in the rotating frame, the average magnetization is in the y' z-plane at an angle tan- (;:)

(4.117)

to the z-axis. The magnitude of the My' component as a function of wr reaches maximum at Wr = ✓r 1r 2· For Wr equal to this value, and for f I - f 2, My' = Mz, so the magnetization is at 1r / 4 to the z-direction. For r 2 >> r 1, the magnetization is at a small angle of Jr 1;r 2 to the z-axis.

(c) Going back to the laboratory frame, the steady-state (i.e., time-independent in the rotating frame) magnetization precesses around the z-axis with frequency w.

This precession leads to a temporal variation (with frequency w) of the projection of the magnetization on the light propagation direction. Since light is circularly polarized, this leads to a modulation in the transmission coefficient (see Problem 3.9). It is important to note that there is a phase shift of 1r /2 in the modulation resulting from Mx' and A1y'.

With an appropriate choice of phase between the rf field and the lock-in ampli- fier (facilitated by the phase rotator shown in Fig. 4.10), the detector may be made sensitive to the modulation due to Mx', which, according to Eq. ( 4.111 ), is an odd function of the mismatch ~ between the Larmor frequency corresponding to the field to be measured, H, and the rf frequency. The phase is adjusted in such a way as to "lock" the frequency output by the voltage-controlled oscillator to the Lar- mor frequency. Thus, the magnetometer is a self-oscillating frequency generator, whose frequency is determined by the external magnetic field.

## 4.8 Searches for permanent electric dipole moments (T)

Here we explore the possibility that an atom could possess a permanent electric dipole moment (EDM). We show that this can occur, for example, if the electron possesses an EDM. A long series of experiments have been performed to search for EDMs of many different particles: most prominently the neutron, various nuclei,

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS and the electron. An excellent review is the book by Khriplovich and Lamoreaux ( 1997).

In this problem, we consider a search for the electron EDM de. Presently, the best upper limit comes from an experiment by Commins and co-workers using atomic thallium (Regan et al. 2002): ldel ~ 1.5 x 10- 27 e ·cm.

(4.118)

(a) One may wonder why so much effort has been put into searching for EDMs of elementary particles, when it is well known that polar molecules like water have "permanent" dipole moments - in fact their value can be looked up in standard tables! In fact, polar molecules do not truly possess permanent EDMs.

The opposite-parity levels in polar molecules are sufficiently close in energy that the Stark mixing between them saturates for rather small electric fields and the molecules completely align themselves with the local electric field (see Problem 7.6). Thus they exhibit a linear Stark shift and appear to have a permanent dipole moment.

This same behavior occurs for the 2s and 2p states of atomic hydrogen, which are separated only by the Lamb shift. Calculate the Stark shift for these levels as a function of an applied electric field E, and show that in the limit d8pE ~ wsp the Stark shift is linear in E (where dsp is the electric dipole matrix element and Wsp = 21r x 1058 MHz is the 2s, 2p splitting). For what values of E is the Stark shift linear? (In this part of the problem, ignore the electron spin.)

Solution An electric field E along Z applied to a hydrogen atom mixes the 2s ~nd 2p levels, and because of the electric dipole selection rules (Problem 2.1 ), E only mixes states with m = m', i.e., 12, 0, 0) and 12, 1, 0) (here we label the atomic states In, l, m) ). Solving the secular equation (see Problem I .4) for the Hamiltonian H describing this system (Ii = 1), (4.119)

we obtain for the eigenenergies (4.120)

(4.121)

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

Here we have neglected relaxation of the levels. For small electric fields, dE << Wsp, we recover the usual quadratic dependence of energies on the electric field: d2 E2 E1 ~ __ s_p_ ~ Wsp .

d2 E2 E ~ + sp 2 ~ Wsp Wsp while for large fields, dE >> Wsp, we find E1 ~ -dspE, E2 ~ +dspE.

(4.122)

(4. I 23)

(4.124)

(4.125)

Indeed, for large electric fields we observe a linear Stark shift, and the atom appears to have a permanent dipole moment dsp, but this is because the states are now completely mixed by the electric field. The atom did not possess an intrinsic dipole moment prior to the application of the field.

The dipole matrix element dsp = -e(2, 1, 0lzl2, 0, 0)

(4.126)

was evaluated in Problem 4.4, where it was found that [Eq. (4.49)]

dsp = -v'3 eao.

(4.127)

Since eao ~ 1.28 MHz/ (V /cm) (Appendix A), linear Stark shifts occur for E >> Wsp ~ 250V/cm.

2dsp (4.128)

(b) One way to think about the consequences of an atomic EDM d: is to consider the Hamiltonian (4.129)

Show that the existence of such a dipole moment would violate parity (P) and time-reversal (T) invariance. (What vectors are available for d: to point along?)

This violation is the reason that EDMs are of such considerable interest. From a macroscopic viewpoint, it seems evident that nature has an arrow of time, 9 but 9 The prime example of an .. arrow of time" is the second law of thermodynamics which says that entropy cannot decrease for an isolated system. This law is based on the fact that the more microscopic states (microstates) available to a system for a given macroscopic state (macrostate), the more likely it is that the system will be in that macrostate. However, such an arrow of time neither implies nor depends on the laws of physics governing the dynamics of the system violating T-invariance. Therefore, it is, in principle, physically possible for a system to go from a state of high entropy to a state of low entropy, it is just extraordinarily unlikely that this would occur for statistically large systems. Such issues are discussed at length in the book by Sachs ( 1987).

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS the only evidence of T-violation in a microscopic system comes from the observa- tion of CP-violation in neutral K- and B-mesons (which, according to the widely held belief that nature respects the combined symmetry CPT, implies T-violation).

CP-violation is incorporated into the Standard Model phenomenologically, and the Standard Model's prediction for the size of the electron EDM due to this CP- violation is many orders of magnitude below the current experimental sensitivity.

The source of CP-violation remains, to a large degree, a mystery, and various pro- posals to explain this phenomenon (such as supersymmetry) often predict values for de that are presently experimentally accessible. Thus searches for ED Ms tum out to be a good way to test new theories in particle physics.

Solution <:.onsider the Hamiltonian describing the interaction of a permanent atomic EDM da with an electric field E: Hedm = -d: · £.

(4.130)

According to the Wigner-Eckart theorem, the expectation value of d: must be proportional to (ff), where Fis the total angular momentum of the atomic state ~Ap~~dix F). Thus the Wigner-Eckart theorem demands that d: is an ~xial vector, I.e., It 1s even under the parity transformation. On the other hand, E is a polar vector and therefore odd under P, so H edm turns out to be P-odd and therefore violates parity (see Problem 1.13).

Similarly, under time-reversal F --+ -F, implying that d: -+ -l 0 while Eis unchanged. Thus H edm is also odd under time reversal (T).

(c) Suppose that the electron possessed a permanent EDM de. Why is it not very practical to search for the EDM of a free electron?

Solution It is difficult to measure the EDM of a free electron since the electron is charged.

We are looking for the interaction of de with an electric field, but an applied elec- tric field will accelerate an electron out of the region of interest, terminating the experiment.

One may consider some type of trap to confine the electron (such as the Pen- ning trap discussed in Problem 1.6), but as we will see in part (d), only through

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

relativistic effects will de become observable. 10 In the case of the electron, it is far more practical to look for the EDM of a neutral atom, which (thanks to relativistic effects) turns out to be proportional to de.

(d) From part (c), it appears that a better way to look for an electron EDM is to measure the EDM of an atom, since the atom is neutral. But does an electron EDM produce an atomic EDM?

Argue that, according to nonrelativistic quantum mechanics, an electron EDM produces no measurable effects in an atom. This is commonly known as Schiff's theorem (Schiff 1963).

Solution Nonrelativistically, an atom can be viewed as a perfect conductor where only electrostatic forces are important. When exposed to an electric field, the atom is polarized in such a way that the external electric field is cancelled out within the atom by the internal field generated by the rearrangement of the electrons about the nucleus. This is clear because a neutral atom exposed to an electric field does not accelerate, therefore it feels no force. Consequently, the average electric field experienced by each of the constituent particles must be zero.

(e) Luckily, it turns out that due to relativistic effects, the applied electric field in fact appears to be "antiscreened." In other words, the atomic EDM da is actually enhanced compared to the EDM of the electron. This was the seminal discovery of Sandars ( 1965) that opened the door for many generations of electron EDM searches using paramagnetic atoms (those with unpaired electrons).

Argue that (4.131)

for the ground state of a paramagnetic neutral atom with atomic number Z.

Assume we are looking at the ground state of some heavy atom with a single valence electron, e.g., Cs. Make use of the fact that relativistic effects are most pronounced near the nucleus in the region r ;S a0/Z (see similar discussion in Problem 1.13).

10 In fact, it is feasible to search for the muon EDM using relativistic muons confined in a magnetic storage ring [see, for example, the paper by Semertzidis et al. (200 I)]. In principle, a similar exper- iment could be carried out for the electron, but it would likely not be competitive with the current limits on de obtained from atomic experiments.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS Hint Use the fact that the electron EDM induces the atomic EDM by mixing opposite- parity states. The main contribution to the mixing occurs near the nucleus (r < ao/Z) where the electron is most relativistic.

rv Solution The electron EDM de induces an atomic EDM da by mixing states of opposite parity. We can estimate the ratio between da and de with the fol~owing argument.

To measure an EDM, one applies an external electric field E and looks for an ene~y ~hift -d: . E ....

Alternatively, we can say that the energy shift is given by -(de · Eind), where Eind is the induced electric field "seen" by the electron. In fact, it has recently been pointed out (Commins et al. 2007) that there are some subtleties (and even widespread misconceptions in the literature) surrounding this issue. Commins et al. (2007) note that even in the relativistic case, (Eioo) = o.

!herefore it is the expectation value of the product (d: · Eind} that is nonvanishing m the relativistic case.

... ...

It is possible to estimate the rough magnitude of the product (de · Eind) using .

...

...

simple arguments. The quantity Bind is proportional to E for small external electric fields and saturates once the atom becomes fully polarized. In our estimate of the EDM enhancement factor, let us consider the magnitude of (d: · E1nd} = deEe« for the case of full polarization (where Eetr is the effective field magnitude).

From Schiff's theorem [discussed in part (d)], we know that in the nonrela- tivistic limit deEetr is zero, so here deEetr must arise entirely due to the motion of the electron. Since any quantity proportional to the average value of the elec- tron's velocity v must be zero, there can be no first-order term, so we expect that deEetr "V ( v2 / c2)deEint where Eint is the internal electric field of the atom. In the region r ;S a0/Z where relativistic effects are most prominent, v ,....., Zoe and the electric field due to the unscreened nucleus is (4. 132)

Thus we have (4.133)

for r ;S ao/Z.

... ...

How does this compare to the energy shift da · E "" daE for a fully polarized atom? We have assumed that the atom is fully polarized, so we estimate that (4.134)

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

for an atom with a single valence electron. By equating d0 E from Eq. (4. 134) with our estimate for deEeff from Eq. ( 4.133), we obtain I da ~ Z 3cx2de -I (4.135)

The ratio d0 / de is known as the EDM enhancement factor, and can evidently be>> 1 for heavy atoms. The enhancement factor is a useful concept in the weak- field regime (when the electric field is not large enough to fully polarize the atom, in which case the EDM-induced energy shift is proportional to daE). However, as noted above, once the field is large enough that the atomic polarization saturates, the energy shift becomes independent of E. This regime of full polarization is easily reached for atoms and molecules with nearly degenerate, opposite-parity levels [as noted in part (a) of this problem].

(f) Finally, we analyze a model experiment to measure an EDM using the method of separated oscillatory fields (Ramsey 1985). This is the basic technique employed in a number of EDM experiments, 11 as well as in generations of atomic clocks. Its main advantage is that it enables one to significantly decrease transit time broadening (Problem 3.13), which subsequently improves the precision with which one is able to measure the precession of atomic polarization. 12 Consider the experimental setup shown in Fig. 4.11. Throughout the experi- mental region there is a static magnetic field B, and in the center of the setup are electric field plates which create an electric field E parallel to B. These fields define the quantization axis (z).

After effusing out of the oven, atoms pass through a laser beam that optically pumps them into a particular Zeeman sublevel. Suppose that the atomic ground state has total angular momentum F = I and the laser is tuned to an F = I ~ F' = I El transition.

Assuming that the relevant saturation parameter is K >> 1, what is the state of the atoms after they leave the laser interaction region? (The laser is linearly polarized along z, as shown by the double arrow in Fig. 4.11.)

After interacting with the first laser beam, the atoms enter a region in which an rf magnetic field ( orthogonal to the page), oscillating at the Larmor frequency 9FµoB, is applied. The strength of the rf field is chosen so that the axis of the atomic polarization is rotated by 1r /2 (this stage uses the technique of magnetic 11 For example, Purcell and Ramsey ( 1950) originally proposed to search for a neutron EDM using separated oscillatory fields, and indeed carried out the experiment (Smith et al. 1957). This is also the method used to obtain the present best limit on the electron EDM (Regan et al. 2002).

12 Instead of using separated fields, one could imagine employing the traditional Rabi technique [see discussion, for example, in the book by Ramsey ( 1985)] with a large interaction region - comparable in size to the separation between the rf regions in Ramsey's method. This approach is unsatisfactory for the technical reason that it is difficult to maintain a homogeneous rf field over a large region and avoid broadening of the resonance due to gradients.

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS • ~Detector Laser beam ~ I RF B-field 2 ~ E • • • • • ~ B • • • Atomic beam _______ I RF B-field I Laserbeam 8 ◄ Oven z FIG. 4.11 Schematic setup for an EDM experiment using Ramsey's method of separated oscillatory fields (see text). Laser beams propagate into the page and are linearly polarized along z.

resonance, see Problem 2.6). What is the state of the atoms (expressed in the spinor representation) after they leave the first rf region?

Next the atoms pass through the electric field region where E shifts the energy of the MF = O state away from that of the MF = ±l states due to the usual quadratic Stark effect (see, for example, Problem 2.1). The MF = ±1 states are split due to the magnetic field. If the atom possesses an EDM, there is also a small contribution from da to the splitting between the MF = ± l states.

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

After exiting the electric field region, the atoms pass through a second rf region identical to the first, except that the phase of the second rf magnetic field can be offset by some amount ¢ from that in the first region. The detected signal is the fluorescence from atoms excited in the second laser-beam-interaction region. The second beam is also resonant with the F = 1 ~ F' = 1 transition and linearly polarized along z.

Show that for an appropriate choice of¢, the fluorescence signal is linear in d0 • (Assume that if ¢ = 0 and E = 0, the second rf region returns the atoms to the state that they were pumped into initially in the first laser interaction region.)

Note that this basic setup suffers from a serious problem. The atoms moving through the electric field see a motional magnetic field (Problem 2.9)

....

....

....

V Bmot =EX - , C (4.136)

which couples to the magnetic moment of the atoms and causes additional preces- sion which is linear in E. In practice, this effect can be distinguished from an EDM signal by, for example, having two counter-propagating atomic beams (since the effect reverses sign with v, unlike an EDM signal). In addition to this E x v effect, there are numerous other subtle effects [such as geometric phases (Problem 2.12), leakage currents, etc.] which must be understood and controlled.

Solution In the first laser interaction region, atoms are optically pumped into the MF = 0 sublevel (optical pumping for F ~ F transitions is discussed in Problem 3.9).

Since"' >> 1, we may assume that the atoms are completely pumped into the state ,~1) = (!)

(4.137)

in the spinor representation (Fig. 4.12). Note that with respect to the laser lighJ, 11/Ji)

is a dark state (see Problem 3.9). Also, since the polarization axis is along B, the magnetic field has no effect on this state.

The rf magnetic field in the first rf region rotates the atomic state by 1r /2 about y. Using the appropriate rotation matrix, 1)(0, 1r /2, 0), for such a transformation (Appendix E), we have 11/12)

= (-~~~ 11 '!2 1~~)

· (~)

= ~ ( ~) .

(4.138)

1/2 -1//2 1/2 v 2 -1 The condition for such a rotation is easy to see in the frame rotating with the Larrnor frequency nL = gµ 0B (Problem 2.6). The linearly polarized rf field Brr

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS After RF 8-field 2 (no EDM)

Just before RF B-field 2 (no EDM)

After RF 8-field I After first laser interaction Unpolarized sample out of oven X After RF 8-field 2 (with EDM)

~ "'~ ..... ·~ Just before RF B-field 2 ~ ~~, :fl (with EDM)

t FIG. 4.12 Probability surfaces (the distance to the origin is proportional to the probability of finding the projection M = F along this direction, see Problem 9.7) describing the atomic polarization at different stages of the model EDM experiment described in the text (see also Fig. 4.11 ).

can be represented as two circularly polarized fields. In the rotating frame, on resonance, one circular component appears to be a static transverse field of mag- nitude Bn/2. while the other appears to rotate at 2S'h. Making the rotating wave approximation (Problem 2.7), we neglect the fast rotating component. The atomic polarization precesses about the static transverse field with frequency gµ 0Bn/2. If the atoms have an average transit time of T, then the magnitude of the rf field is adjusted so that gµoBrt T = 1r (4.139)

to produce the desired rotation.

Now the atomic polarization axis is perpendicular to B, and the polarization precesses at the Larmor frequency nL: (4.140)

SEARCHES FOR PERMANENT ELECTRIC DIPOLE MOMENTS (T)

If the atom possesses an EDM, there is an additional phase shift between the states: l (e-i(fli.+d,,E)t)

l'l/,,3(t)) = - o .

J2 -ei(fli.+d,,E)t (4.141)

If we again go into the frame rotating with OL, we have (4.142)

Finally, the atoms enter a second rf region. The rf field in this region is phase shifted by </> with respect to the first rf field. Thus in the rotating frame with quan- tization axis along the rf field in the second region, the state of the atom as it enters the region is (4.143)

The rf field transforms the atomic polarization according to l'l/J~) = 1>(0, 1r ;2, o) l¢t 0t\ t))

(4.144)

- -1//2 1//2 · - ( 1/2 1//2 1/2)

l (e-i(daEt+<I>))

1/2 -1//2 1/2 J2 -ei(d .. Et+q,)

(4.145)

( J2 sin(d 0 Et + <P))

= - cos(d 0 Et + </>) .

J2 sin( d0 Et + <P)

(4.146)

The fluorescence signal ~ when the atoms enter the second laser interaction region is proportional to the population of the MF= ±1 states: (4.147)

If we choose</> = 1r / 4, we obtain (assuming d0 Et << 1, of course)

(4.148)

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS Note that if the direction of the electric field with respect to the magnetic field is reversed, one has 3=' ex 2 - d0 Et.

(4. 149)

which is the signature of an EDM.

## 4.9 Sensitivity to electric dipole moments

In Problem 4.8, we considered various aspects of experimental searches for a pennanent electric dipole moments (EDM). In this problem (based on the con- siderations of Budker et al. 2006) we will investigate what parameters detennine the sensitivity to the EDM for various experiments.

(a) Estimate the signal-to-noise ratio ( S / N) for a "traditional" spin-precession- type EDM experiment performed with an atomic beam or vapor (see Khriplovich and Lamoreaux 1997), such as the one described in part (t) of Problem 4.8. Express (SIN) in tenns of the number of particles/atoms N, the EDM d, the electric field applied E, the spin-relaxation timer, and the total measurement time T.

(b) Now consider an EDM experiment using condensed matter, as discussed by Shapiro (1968), Vasil'iev and Kolycheva (1978), Lamoreaux (2002), and oth- ers. Suppose that the experiment is conducted by applying an electric field to the sample and measuring the EDM-induced magnetization with an ideal (noise-free)

magnetometer. Assume the sample is at temperature 'J and that the populations of e~ergy levels corresponding to different spin orientations with respect to the elec- tnc field are described by the Boltzmann factor. What is the signal-to-noise ratio {S/N) in this case?

(c) When the temperature 'J of a condensed-matter sample becomes so low t~at the energy scale f associated with spin-spin interactions (for example, the dipole-dipole interaction discussed in Problem 2.13) exceeds k'J, the sample will tran~ition into a ferromagnetic or ant if erromagnetic state. In this regime, the sam- ple is no longer sensitive to EDMs. Assuming that the spin-relaxation time T for !he condensed matter sample considered in part (b) is determined by spin-spin mteractions so that f rv 1/r, show that the signal-to-noise ratio is the same as that for the "traditional" spin-precession-type considered in part (b).

Solution (a) In general, for any measurement scheme, the EDM-induced spin-precession angle is rv dEt, where t is the precession time. [For example, Eq. (4.149) of

## SENSITIVITY TO ELECTRIC DIPOLE MOMENTS

Problem 4.8 shows that for the considered scheme the EDM-induced fluorescence signal is ex dEt.] The maximum precession time is given by the spin relaxation timer, and the signal increases linearly with the number of atoms N. Thus for a "single-shot" measurement we have a signal (4.150)

Due to the uncertainty principle, any measurement of spin-projection results in a shot-to-shot random imbalance between the population of different Zeeman sublevels of order v'N, thus the noise associated with such a measurement is Ni rv JN.

The signal-to-noise ratio can be improved by repeating the measurements many times up to a total experiment time T, so that the experiment is performed n = T/r times, which gives the usual yri, improvement in the signal-to-noise ratio. 13 Therefore the signal-to-noise ratio for a "traditional" EDM experiment is given by (4.155)

(b) Our signal for a single-shot measurement is the EDM-induced magnetization of the sample, given by the difference between the number of spins pointing in the same direction as the electric field and the number of spins pointing in the opposite direction. Since the EDM-induced energy difference for different spin orientations 13 Th · II e improvement in signal-to-noise ratio can be understood as follows. Idea Y, repeate measurements do not change the expected mean value of the signal, so - n s = s = - Ls,= 'NdET = s1, n i=l (4.151)

~~- t~e uncenainty in S is given by combining the (uncorrelated) uncenainty Ni == ,IN of the in ividual measurements in quadrature: 6S= .!.~tNl; n i=l by multipl · bo .

.

· Ymg th sides of Eq. ( 4.152) by n and then squanng, we obtain (4.152)

n26S2 = n'N, (4.153)

or 6S=N= ~.

(4.154)

INTERACfION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS with respect to the electric field is vanishingly small, the signal is (4.156)

where µ is the magnetic moment of one spin and k is Boltzmann's constant. Note that the signal does not depend on the spin-relaxation time T.

In the absence of any external fields, at a given moment in time we have a random total magnetization (4.157)

As in the case of a precession experiment, the fact that this noise magnetization is random and changes in time can be used to improve the signal-to-noise ratio. The spin relaxation time r characterizes the correlation time of the fluctuations, telling us how long the random magnetization persists. If this time is too long, this may present a serious problem for the experiment. In other words, if the spins do not relax, each time a sample is prepared, there is a random signal, which would not average in time.

More formally, we have expressions ( 4.156) and ( 4.157) from which we can write (S/N) for a long measurement time T >> r: (S/N) ~ S1 ff~ dE fN'i'.

N 1 V -;: k'J' V -:;:- (4.158)

Key parameters for an experiment of this type are the relaxation r and the tempera- ture 'J'. Assuming that these parameters are independent, the experiment should be done at the lowest possible temperature to increase the degree of induced polariza- tion. In addition, it appears that it is beneficial to have fast spin relaxation (small r), so that the measurement can be repeated often (and thus efficiently average out the random magnetization. Note that such dependence of the sensitivity on r is the opposite of that in the case of precession experiments [Eq. (4.155)].

( c) The characteristic energy scale for the spin-spin interaction f. ,....., 1 / r determines the minimum temperature of the sample: k'J min ,....., f. ,....., 1 / r. Using this value for 'J' min in Eq. ( 4.158), we recover the signal-to-noise ratio for the spin-precession- type experiment: (S/N),....., dE✓NTr.

(4.159)

Considerations such as these are an extremely important early step in design- ing any precision measurement and in comparing the sensitivity of different experimental approaches.

ABSORPTION, DISPERSION, OPTICAL ROfATION, AND INDUCED ELLIPTICITY 4.10 Absorption, dispersion, optical rotation, and induced ellipticity S_!arting from the wave equation for a plane, monochromatic electromagnetic wave E propagating in the z-direction through a dielectric medium [see, for example, Boyd (2003), Section 2.1]

(4.160)

where w is the frequency and fi is the induced electric polarization of the medium caused by the light-atom interaction, find general expressions, in terms of the polarization fi and incident field E( z = 0), for the following quantities: I. The real part of the refractive index n, Re(n), associated with dispersion in the medium.

## 2. The imaginary part of the refractive index n, hn( n), associated with

absorption.

## 3. The optical rotation per unit length, ~

## 4. The induced ellipticity of the light per unit length, ~!

Assume the wave is initially (at z = 0) linearly polarized along x but that there can appear a transverse component of polarization Py as the wave propagates due to anisotropy in the medium or the application of external electric or magnetic fields. 14 The optical rotation angle, for small angles, is defined to be (4.161)

and the small-angle induced ellipticity is defined to be (4.162)

14 In a general anisotropic medium, a longitudinal component of polarization can be induced. Here we will restrict our considerations to electromagnetic waves with transverse polarization.

## INTERACTION

## OF LIGHT WITH ATOMS IN EXTERNAL FIELDS

Hint At z = 0 the electric field is E(o, t) = Eoe-iwti where Eo is real, and at z the field becomes E(z, t) = [Ex(z)x + Ey(z)y]ei(kz-wt) ' (4.163)

where we have separated the fast variation of the phase of the field, eikz, and the slow variation of the field amplitudes Ex ( z) and Ey ( z). Similarly, we can write the induced polarization fi(z, t) = [Px(z)X + Py(z)Y]ei(kz-wt) .

(4.164)

Additionally, we can identify the in-phase and out-of-phase [ with respect to the incident field E{O, t)] components of the polarization: Px = P1 - iP2, Py= P3 -iP4.

(4.165)

(4.166)

Assume that Ex ( z) and Ey ( z) vary slowly, so that terms proportional to the second derivative with respect to z of Ex(z) and Ey(z) can be neglected.

Solution For the refractive index n, we can use the approximate expression p n~I+21rx=I+21rE, (4.167)

~here X is the susceptibility and P and E are the magnitudes of the polariza- tion and field, respectively. Assuming the induced y-components of the field and polarization to be small relative to the x-components, we can say Px 21r ( . )

n ~ l + 21r- ~ 1 + -E P1 - iP2 , Ex o where we have employed expression ( 4.165). Therefore, and P2 Im(n) = -21r- .

Eo (4.168)

(4.169)

(4.170)

For the optical rotation and induced ellipticity, starting from the wave equation ( 4.160), we can write the differential equation for each polarization component of

ABSORPTION. DISPERSION. OPTICAL ROfATION, AND INDUCED ELLIPTICITY 269 the field (s = x, y) as W + _ E (z)ei(kz-wt)

= ~-P.

(z) i(kz-wt)

( 82 )

.

c2 iJ z 2 s c2 8t2 s e .

(4.171)

Evaluating the derivatives and dropping terms proportional to / 2 Es and 8 2 p I I .

.

. )

b .

z az2 s (the s ow y varymg approx1matmn , we o tam ( ;: Es(z) - k2Es(z) + 2-ikd!s )ei(kz-wt) = -4n-;: Ps(z)ei(kz-wt), (4.172)

or simply (4.173)

Evaluating Eq. (4.173) for they-components at z = 0 and assuming Ex ~ Eo and n ~ I (so k ~ w/c), we obtain dE w2 ik d/ = -2n- c2 Py(O) .

(4.174)

Employing expression ( 4.166) for Py, we obtain I dEy 21rw .

--- = -(zP3 + P4)

Eo dz cEo (4.175)

which yields, according to Eqs. (4.161) and (4.162), dcp 21rw P4 - ---- (4.176)

dz C Eo and de 21rw P3 dz= -c-Eo · (4.177)

Note that, perhaps somewhat counter-intuitively, optical rotation is propor- tional to the component of polarization 1r /2 out-of-phase with the incident light field and ellipticity is proportional to the in-phase polarization.

If one assumes that P 1. = Nd .1., where N is the atomic density of the medium and d1. is the amplitude of the induced dipole moment per atom orthogonal to the initial light polarization, we have dcp = 21rw N Im(d1.) .

dz cEo (4.178)

In the case of Faraday rotation where the width of the relevant transition is given by the natural width ,o (Problem 4.1 ), the above expression can be compared to,

INTERACTION OF LIGHT WITH ATOMS IN EXTERNAL FIELDS for example, Eq. (4.11) to see that for small magnetic fields [Bz << ,o/ (29FJlo)., where 9F is the Lande factor]

(4.179)

where a is the polarizability of the medium.

## 4.11 Optical rotation in a gas of polarized neutrons

Consider a medium consisting of polarized neutrons with number density N.

Suppose that linearly polarized light is propagating in a direction collinear with the direction of polarization. The light will undergo polarization rotation as it propagates through the medium.

Identify the physical mechanism responsible for the optical rotation, and give a rough estimate of the effect (ignore factors of order unity). As a numerical exam- ple, estimate optical rotation per unit length of a fully polarized neutron gas with a number density equivalent to that of condensed matter.

Solution Optical rotation arises due to the neutron's magnetic moment. The magnetic field of the light, il is perpendicular to the light-propagation direction, and thus also to the direction of neutron's polarization. This field causes the magnetic moment of a neutron to precess during each half period of the light wave by a small angle µNH <.p rv nw (4.180)

where µN is the nuclear magneton and w is the angular frequency of the light.

[This is the small angle approximation of the result (2.64) from Problem 2.6 in the far detuned limit.]

Thus there appears an oscillating component of the magnetic moment perpen- dicular to both the magnetic field of the light and the initial neutron polarization with an amplitude on the order of (4.181)

Note that the induced transverse magnetization will be 1r /2 out of phase with the light field.

From this, in analogy with the case of electric polarization of a medium [see., for example, Eq. (4.178) and surrounding discussion in Problem 4.10], we can

OPTICAL ROTATION IN A GAS OF POLARIZED NEUTRONS right away write an estimate for optical rotation per unit length d{)

21rw ]\r 21r Jl i - rv --Jlj_ rv --N.

df He he (4.182)

It is worth pointing out that, since the induced magnetization changes sign with reversal of the initial neutron magnetization, there is no optical rotation produced by unpolarized gas. This, of course, also follows from general symmetry prin- ciples. A notable property of the optical rotation described by Eq. ( 4.182) is the independence of the rotation angle of the frequency of light. Another interesting feature of the problem is that, since there is no induced magnetization along the light magnetic field, there is no usual refraction (see Problem 4.10, at least in the first-order approximation that we have been using in this discussion.

Putting in numbers, µN rv 10- 3 µB ~ 10- 23 in Gaussian units and if N = 1022 cm- 3, then from Eq. (4.182) we obtain an optical rotation on the order of 10- 7 rad/cm.

## ATOMIC COLLISIONS

5.1 Collisions in a buff er gas Suppose we have a volume containing gas of molecules at density n with collisional cross-section a.

What is the mean free path of a molecule between collisions and the average time between collisions?

Now suppose we add some gas of another sort (buffer gas) into the volume.

What will be the effect of the buffer gas on the rate of collisions of the original molecules between themselves? 1 Solution The mean free path A of a molecule between collisions is given by: A=-, na (5.1)

where n is the density and a is the collisional cross-section. The characteristic time between collisions is rv A/v, where v is the average relative thermal velocity.

If a buffer gas with density n' and cross-section a' (for collisions with the orig- inal molecules) is added into the system, the total collision rate , for the original molecules is: - + I I-I + 'Y = nav n a V = 'Yself !buffer, (5.2)

where v' is the average relative velocity between the molecules and buffer gas, and "Yself and ,buffer are the rates for self- and buffer-gas collisions, respectively.

Note that the collision rate between the original molecules is in fact unmodified, there are just more total collisions! Thus the introduction of the buffer gas does not change the time between collisions of the original molecules with themselves.

This result is illustrated in Fig. 5.1: a molecule moving about the cell traces out an effective volume VetT = avt, and the probability of a collision becomes about 1 This problem was inspired by V. V. Yashchuk.

## ATOMIC COLLISIONS

without buffer gas with buffer gas FIG. S. l A molecule moving about a cell without buffer gas and with buffer gas. Although the total collision frequency in the cell with the buffer gas is higher, the effective volume traced out by a molecule in a given time t is unchanged.

unity when the V eff = 1 / n. These parameters are independent of the frequency of collisions with the buffer gas. Note that this result is only true for equilibrium conditions; for example, we assume that the gases are well-mixed in the cell.

## 5.2 Spectral line broadening due to phase diffusion

Here we consider the broadening of spectral lines when radiating atoms in a sample experience a series of random phase shifts. Such phase shifts can be caused, for example, by collisions with other atoms (pressure broadening) or collisions with antirelaxation coated vapor cell walls. A related phenomenon is the phase diffusion of a laser oscillator which occurs due to spontaneous or thermal emission into the lasing mode. This is a fundamental limit on the linewidth of lasers [the so-called Schawlow-Townes limit; see, for example, Yariv ( 1989)].

(a) Consider an ensemble of identical oscillating dipoles of frequency w0 all in phase with each other at t = 0, each of which permanently oscillates at t >

## 0. Suppose, however, that the oscillators receive random small "kicks," so their

phases with respect to an unperturbed oscillator experience a random walk (step size </J1 << I; steps occur with time intervals tc). Allow the phase shifts to be positive or negative with equal probability. What is the spectrum of radiation for such an ensemble?

(b) Now consider a slightly more complicated problem.

First, allow for a statistical distribution of the number of kicks n experienced by atoms over a time t, which we will assume Poissonian: e-t/t,: (t/tc)n p(n, t) = , , n.

(5.3)

where p(n, t) is the probability that an atom experiences n collisions in time t (the mean number of kicks corresponding to the distribution (5.3) is (n) = t/tc)-

SPECTRAL LINE BROADENING DUE TO PHASE DIFFUSION Second, suppose that the phase shifts per kick are not the same. We will assume a normal (Gaussian) distribution with a mean value </J (l<PI << 1) and a dispersion </)2.2 Find the shift and broadening of the radiation spectrum in this case.

Solution (a) As a result of the random walk in phase, at time t, the oscillators will be distributed in phase according to the Gaussian distribution: (5.4)

where the Gaussian width is <Po ( t) = <P 1 ,/tit; .

(5.5)

Indeed, in a random walk the Gaussian width is just the step size times the square root of the number of steps [see, for example, Reif ( 1965)].

The amplitude of the radiation emitted by the ensemble at time t is the sum of the amplitudes from each oscillator; this is proportional to the quantity A( t) = loo P( c/>, t)ei(wut+,t,)dc/> = e -~+iwut .

(5.6)

-oo Taking the Fourier transform of this amplitude and then taking the absolute value squared of the result, we find that the spectral distribution of the radiation intensity is given by the Lorentzian function I(w) oc 12 / 4 , (w - wo)2 + , 2/4 (5.7)

where the full width at half maximum (FWHM) is (5.8)

This example illustrates a general point that the linewidth is given by the inverse time it takes a system to lose phase coherence: 3 it takes 1 / </>i steps for an oscillator to acquire a phase angle rv 1, which takes a time tc/ <PI.

2 The latter propeny holds, for example, when the phase shifts are caused by collisions with an antirelaxation coated cell wall. It follows from a distribution of wall-sticking times with a universal binding energy exceeding kB1' [see, for example, Goldenberg et al. ( 1961 )].

3 For example, this concept provides a simple way to derive the Doppler width. Suppose we have two atoms emitting light with frequency wo in their rest frames, but they have a relative velocity

## ATOMIC COLLISIONS

(b) Let us consider atoms that have experienced some fixed number of kicks n >>

## 1. Let <l>n

be the overall phase accumulated by an atom over n kicks. Because of the normal distribution of phase shifts in individual kicks (resulting in a random walk in phase), we have a Gaussian distribution of accumulated phases: - !,:.,,.

__ ,,,,,)2 p( <Pn' n) = J 21Tn</)2 e ., ... ,.2 (5.9)

where n<j) is the average phase accumulated in n kicks, and n<t,2 is the dispersion.

Taking into account the distributions (5.3) and (5.9), the oscillation amplitude averaged over the atomic ensemble is found as a weighted sum of the contributions from individual atoms ( ex ei(wot+<l>i), where <Pi is the phase accumulated by this individual atom): (5.10)

(5.11)

where in the last step we have explicitly evaluated the integral and the sum. Next, we use the fact that l<l>I << 1, and, expanding the exponential factor to second order in </>, we obtain: (5.12)

which says that the frequency of the oscillation is shifted by -¢/tc, and the amplitude decays at a rate </)2 /tc leading to line broadening.

Taking the Fourier transform of the amplitude, again we find for the spectral distribution (5.13)

v (in the direction of observation). As the distance between the atoms changes, so does the phase difference between light from the two atoms: ~""' = 21r~x ~ 21rvt '/J ,\ ,\ ' and when~¢"-' 1, we have

## DICKE NARROWING

However, in this case (5.14)

It is interesting to note that neglecting either one of the two random factors _ th number of collisions experienced by an atom, or the dispersion in phase shift e · · h" h .

I b ~ per colhs1on - leads to a decay rate w 1c 1s s ower y a ,actor of two.

5.3 Dicke narrowing For a moving atom, a resonance frequency wo is shifted due to the Doppler effect: ~w=wo(l-D, (5.15)

where v is the component of velocity along the direction of propagation of light.

For an ensemble of atoms with different velocities, this leads to the Doppler broadening of spectral lines. Imagine, however, that an atom is frequently chang- ing the direction of its motion (due to collisions with other atoms, for example)

without changing its internal state. In this case, the average value of v is zero and the Doppler broadening must be absent. Therefore, there are apparently two qualitatively different broadening regimes, depending on how frequently the velocity-changing events occur [Dicke ( 1953)].

For infrared and microwave atomic and molecular transitions, collisional elimi- nation of the Doppler width (Dicke narrowing) is easily observed. Figure 5.2 shows experimental data demonstrating Dicke narrowing of a microwave transition. 4 The frequency of the microwave transition (for free atoms) is 3,035,732,440 Hz, so the microwave wavelength (~ 10 cm) is comparable to the cell dimensions, cor- responding to the intermediate regime between regular Doppler broadening and its complete suppression due to the Dicke effect. As a result, the narrow, Doppler- free peak is seen superimposed on a broad [ rv 4 kHz (FWHM)] Doppler-broadened peak.

4 Data were taken with 85 Rb atoms contained in a I 0-cm diameter vapor cell with antirelaxation paraffin wall coating (Alexandrov et al. 2002). The atomic vapor density is such that the unsaturated absorption length is comparable to the cell diameter. The atoms are illuminated with laser light of frequency tuned to one of the hyperfine components of the DI resonance. The laser light optically pumps the atoms (Problem 3.10), so the resonant ground state hyperfine component is depopu- lated and light absorption is reduced. When a microwave magnetic field resonant with the transition between hyperfine components is applied, atoms are returned back to the resonant hyperfine state and light absorption is restored. Thus, the microwave transition can be detected by observing light transmission as a function of the microwave frequency, as shown in the plots.

C: ::::s C: OJJ ci5 ca C: V')

## ATOMIC COLLISIONS

Fr qu nc Iner m Fr qu ncy In r m n Hz)

Ftc. S.2 Experimental data (Budker et al. 2003) demonstrating Dicke narrowing of a microwave transition (see text). The spectra shown here correspond to the F = 3, M = 0 --+ F' = 2, M' = 0 transition. Such 0 --+ 0 hyperfine-structure transitions in alkali atoms are near- ly-insensitive to magnetic fields, and are used in frequency standards [atomic clocks - see Audoin and Guinot (2001) and Major (1998)]. The lower plot is a scan representing a zoom onto the Doppler-free feature seen in the upper plot The lower plot also shows a fit with a Lorentzian superimposed on a linear background. The fitted Lorentzian linewidth (fWHM)

is 10.9(3) Hz, which, due to residual light broadening, is slightly larger than the .. intrinsic" width of about 8. 7 Hz determined by wall collisions. The central frequency has nonzero offset from the transition frequency of free atoms due to the phase shifts in wall collisions (Problem 5.2).

In this problem we examine Dicke narrowing and make some estimates to see whether it is possible to observe it in optical transitions, with the velocity-changing events arising from collisions with buff er gas.

(a) Give classical and/or quantum mechanical arguments to show that transition between the two broadening regimes occurs when the mean free path L between velocity-changing collisions satisfies the condition L rv ,\, where ,\ = 21rc/wo is the radiation wavelength. Give an approximate expression for the residual Doppler width for L << .-\.

## DICKE NARROWING

(b) For a typical optical transition and atoms with thermal velocities, estimate the ambient gas pressure (in torr) necessary to achieve this condition, due to velocity-changing collisions with a buffer gas. Use typical values: temperature T rv 1000 K, velocity-changing collision cross-section a vcc rv 10- 15 cm 2 .

(c) The condition that the internal atomic state does not change in a collision severely limits the range of situations when Dicke narrowing can be observed.

In other words, it means that line broadening due to collisions has to be smaller than the Doppler width. Write out this condition in terms of the pressure broaden- ing cross-section apb. Convert apb into a pressure broadening coefficient 7]pb (units of MHz/torr). Compare the obtained value to the typical value rv IO MHz/torr.

Solution (a) Consider the radiating atom changing velocity as an oscillator with vary- ing (mcxfulated) frequency. As discussed in detail in Problem 8.3, there are two limiting cases in terms of the qualitative appearance of the spectrum. When the modulation index, i.e., the ratio between the amplitude of the modulation and the modulation frequency, is large, we have a broad, essentially continuous spectrum of widths given by the amplitude of the modulation. In the present problem, the analog of the amplitude of the frequency modulation is the Doppler width, and the analog of the modulation frequency is the frequency of velocity-changing colli- sions. Thus, the broad continuous spectrum corresponds to the Doppler-broadened spectrum in the absence of collisions.

Conversely, when the modulation index is small, the spectrum consists of side- bands separated by the modulation frequency, whose amplitude relative to the central unshifted peak rapidly decreases as the modulation index decreases. This regime corresponds to Dicke narrowing.

The modulation index is of order unity when the frequency of velocity- changing collisions is equal to the Doppler width r D for free atoms: (5.16)

rv rv -L' where 'V= ✓2~T (5.17)

is the thermal velocity of the atoms (M is the atomic mass).

If the atom is moving undisturbed, the Doppler shift ~w D is given by !:iw D = w '!!. = 21rv = 21r C A t>,.' (5.18)

## ATOMIC COLLISIONS

where t~ is the time it takes it to travel a distance A. From a Fourier picture, one can see that this result still holds when velocity changes. In the case L << A, an atom undergoes a random walk and the average displacement 8 in time t is . -Lj¥t ' L (5.19)

where the expression under the square root is the number of steps in the random walk. Hence, for L << A, and the residual Doppler width is Lv f D rv 21rA2.

(5.20)

(5.21)

Therefore, from Eqs. (5.16) and (5.21), the condition that atoms change the velocity direction frequently enough for the Dicke narrowing to occur translates into the condition that the mean free path is much smaller than the radiation wavelength.

(b) For an optical transition, (5.22)

The mean free path is ( nu vcc )- 1, where n is the ambient gas concentration.

The ref ore, the condition on n is: I n ;;: 1020 cm - 3 , (5.23)

which corresponds to rv 104 torr (or 10 atm).

(c) The condition that the atomic internal state does not change in a velocity- changing collision can be simply written as I O' pb « O' vcc • I The time between the internal-state changing collisions is tc rv -- nO'pbfJ and the corresponding spectral broadening is (5.24)

(5.25)

f pb rv nupbfl .

(5.26)

If apb << 10- 15 cm 2, then using the fact that I torr corresponds ton~ 1016 cm- 3 and fJ ~ 3 x 104 cm/s, for the pressure broadening coefficient we find that it has

## BASIC CONCEPTS IN SPIN EXCHANGE

to be (10 16 Clll-: 3) X (lo-IS cm 2) X (3 X 104 cm/s)

T/pb << 7r ~ 5 x 10- MHz/torr .

(5.27)

This is much smaller than the typical value 1/pb rv 10 MHz/torr, indicating that observing buffer-gas-induced Dicke narrowing in an optical transition - if possi- ble at all - requires a situation where the pressure broadening is unusually small.

Optical transitions with small pressure broadening approaching this value some- times occur in the closed shells of the rare earth elements (Alexandrov et al. 1984, Vedenin et al. 1986, Barkov et al. 1989). However, in spite of several experimental attempts, buffer-gas-induced Dicke narrowing in an optical transition has not yet been observed.

5.4 Basic concepts in spin exchange Spin exchange (SE) is a term describing a broad class of collisional phenomena involving the transfer of polarization from one atom to another, and in some cases, collisional relaxation of atomic polarization.

Spin-exchange is important, for example, where one is optically pumping alkali atoms contained in antirelaxation- (most often, paraffin-) coated vapor cells, where it is a major factor determining the equilibrium state of atomic polarization and the pumping and relaxation dynam- ics. A major application of spin-exchange collisions is to polarize systems where direct optical pumping is difficult, for example, nuclear polarization of noble gases in spin-exchange collisions with optically pumped alkali vapors.

There are several reviews, such as Happer ( 1972), Happer and van Wijngaarden ( 1987), Knize et al. ( 1988), and Happer et al. (2003), available in the litera- ture describing the physics and applications of spin-exchange collisions. In this problem we discuss some basic ideas and results in the theory of SE.

Consider a collision of two j = s = 1/2 atoms, A and B. For a given quanti- zation axis, the two possible spin states for each of the atoms are "spin-up," I+), and "spin-down," I-). A spin-exchange collision corresponds to a collision of a spin-up atom with a spin-down atom, in which the fonner atom comes out with spin-down, and the latter with spin-up (hence the tenn), e.g., (5.28)

Prior to the collision, the total spin of the two atoms can be either O (singlet), or I (triplet). The origin of SE can be traced to the difference in the interatomic poten- tials for the two cases; this difference is closely related to the idea of the exchange interaction discussed in Problem 1.2. In the singlet state, the spatial distribution of

1.0 0.8 0.6 0.4 - 0.2 > u ._.

~ -0.0 ..

u C: UJ -0.2 -0.4 -0.6 -0.8 -1.0

## ATOMIC COLLISIONS

. . . . . . . . . . . .

. . .. ·· ... .. .. .. .. ..

••••••••••• Triplet ·············· ······················· r(A)

FIG. S.3 Typical interatomic potential energy curves for two spin- I /2 atoms whose total spin cor- responds to the triplet (dashed line) and singlet (solid line) states. The singlet state corresponds to the molecular term 1 E+ (e.g., the ground state of an alkali dimer) while the triplet state corresponds to the molecular term 3 E+.

the electrons can overlap (since the spin wavefunction is antisymmetric, the spatial wavefunction is symmetric), so it is possible to form a stable molecule where the electrons' wavefunction is concentrated between the two nuclei and binds them together. Indeed, the majority of the most abundant diatomic molecules have 1 E+ ground states ( completely symmetrical with zero total spin, see Problem 7 .4 and Appendix C). In the triplet state, the electrons tend to be far apart so it is difficult to form a bound molecular state. For this reason, the triplet potential is either entirely repulsive (e.g., for H-H collisions), or contains only a very shallow minimum at large distances. By contrast, the singlet potential has a relatively deep well ( r.J e V)

and is attractive except at very short distances (rv ao). Figure 5.3 shows model potentials illustrating the contrast between the two cases.

The interatomic potentials can be thought of as consisting of a spin- independent part, Vo ( r), and a spin-dependent part, V1 ( r): (5.29)

(a) Find the explicit form of the triplet and singlet potentials, Vt(r) and V.(r), in terms of Vo(r) and V1 (r).

(b) Perf onn a crude estimate of the order of magnitude of the SE cross-sections.

Make use of the information shown in Fig. 5.3, and assume that for interatomic

## BASIC CONCEPTS IN SPIN EXCHANGE

separations r ~ 10 A the potential V1(r) ex r- 6 (a van der w 1 • I)

. .

aa s potent1a .

Which angular momentum charactenst1cs are conserved in SE coll•· · ·?

s10ns.

(c) Show that an appropriate expression for a "spin-exchange operator" is: - - '.J> = 2 + 2S A . s B.

(5.30)

Solution (a) The form of the triplet and singlet potentials follows from Eq. (5.29), and the explicit evaluation of the quantity - - 52 - 52 - 52 1 [ 3]

SA· Sa = ; 8 = 2 S(S + 1) - 2 , from which we obtain and ½(r) = Vo(r) + -V1(r)

Vs(r) = Vo(r) - 4Vi(r).

Here § = SA + SB is the total spin of the colliding pair.

(5.31)

(5.32)

(5.33)

(b) The difference V1 ( r) between the triplet and the singlet potentials is of an electrostatic nature (similar to the energy differences between different spin states in multi-electron atoms, see Problem 1.2), and is thus on the order of electron-volts over several Angstroms (Fig. 5.3).

Consider the collision of a spin-up atom with a spin-down atom. Initially, when the atoms are far apart, we can write their wavefunction 11/J)

as a superposition of the singlet IO, 0) and triplet I 1, 0) states (here we use the notation IS, Ms))

l'/P(O)) = l+)Al-)a = v'2{11,0) + IO,O)).

(5.34)

When the atoms become sufficiently near to one another, the triplet and singlet states acquire a relative phase due to the potential V1 ( r): (5.35)

where

## ATOMIC COLLISIONS

1 ft tl.<t>(t) = Ii Jo Vi(r(t)]dt.

(5.36)

For the purposes of a crude estimate, we express the accumulated phase difference in a collision ~<I> in terms of the duration of the collision Tc = r cl v, where r c is the average distance between the atoms during the collision and u is their relative velocity: (5.37)

When ~<I> ~ 1r, we see from (5.35) that the wavefunction describing the atoms becomes I-) A I+) 8 , so that indeed a SE collision has occurred. Thus the condition for SE to occur is (5.38)

where we assume that v"" 3 x 104 cm/s as is the case for a typical room temper- ature atomic vapor.5 We see from the plot in Fig. 5.3 that for r "" 10 A we have V1 ( r) "" 0.1 e V, so according to the fact that in the region r ~ 5 A., V1 ( r) scales as r- 6, we have T ~ 10 A_.

In combination with the requirement (5.38), we find that Tc rv 25 A.

(5.39)

(5.40)

The ref ore, we estimate the order of magnitude of the cross-section to be use "' 2 x 10- 13 cm2. Due to the crude nature of this estimate, it is about an order of magnitude too large - typical alkali atom spin-exchange cross-sections are I Use~ 2 X 10- 14 cm 2• I (5.41)

Although individual atomic spins change during a SE collision, the total spin of the system is approximately conserved. [There are so-called spin-destruction effects with orders of magnitude smaller cross-section (see Problem 5.8), but they are beyond the scope of our present consideration.]

5 It is not clear, a priori, whether v should indeed be the thennal velocity, or rather should be the velocity detennined by the kinetic energy gained by the atom as it "rolls down,_., the potential .. hill."

However, our estimate later shows that re is sufficiently large that it is acceptable to use the thermal velocity for v [Eq. (5.40)).

## THE SPIN-TEMPERATURE LIMIT

(c) The appropriate spin-exchange operator P must satisfy the following proper- ties: Pl+)Al+)B = l+)Al+)B' Pl+)Al-)n = 1-)Al+)B, Pl-)Al+)B = l+)Al-)B' Pl-)Al-)B = 1-)Al-)B · Introducing the standard spin-1/2 raising and lowering operators and rewriting Bx = 2(s+ + S_), Sy = 2/S+ - S_ ), one can express the operator (5.30) as (5.42)

(5.43)

(5.44)

(5.45)

(5.46)

(5.47)

(5.48)

(5.49)

Using this form, one can easily see that the operator P indeed has the required properties (5.42)-(5.45).

5.5 The spin-temperature limit In many optical pumping experiments using circularly polarized light, spin- exchange is the most rapid process in the system, occurring faster than both pumping and relaxation due to other kinds of collisions (e.g., collisions with the cell walls). In this case, the distribution of atoms among various Zeeman sublevels can be described by the spin temperature ({J- 1) [Anderson et al. ( 1960)] according to (5.50)

where p( Fz) is the population of a given Zeeman sub level.

Derive the distribution (5.50) from first principles assuming that total angular momentum of the system N ( Fz) is conserved ( N is the total number of atoms in the level F)., and that the system is in statistical equilibrium.

Solution

## ATOMIC COLLISIONS

Atoms in the system can be distributed among the Zeeman sublevels in a variety of ways, so that Ni atoms reside in the i-th sublevel. Each such distribution must satisfy the condition that the total number of atoms is N: (5.51)

and that the total angular momentum is L Ni(Fz)i = N(Fz)- (5.52)

For a given set of Ni's, let us calculate the number of ways it can be realized (here we assume a nondegenerate gas, so atoms can be assumed distinguishable).

We have N atoms, N 1 of which we wish to put in the first Zeeman sublevel. The number of ways we can do it is [see, for example, Reif ( 1965)): N!

111 = (N1)!(N - Ni)! .

(5.53)

With N1 atoms in the first sublevel, we have (5.54)

ways to put N2 atoms in the second Zeeman sublevel, and so on. The number of ways a given set of Ni's can be realized is then N!

S1=IIS1i=NI I.

l····Ni···· (5.55)

According to the general principles of statistical mechanics, the distribution of Ni's in equilibrium is such that the quantity (5.55) is maximized subject to the conditions of Eqs. (5.51) and (5.52). In other words, each allowed configuration is equally probable, and the equilibrium state corresponds to the distribution of populations that can be realized in a maximum number of ways.

Instead of maximizing the quantity (5.55) directly, it is more convenient to maximize its logarithm: a= Inn~ NlnN - N - L (Ni ln(Ni) - Ni), (5.56)

where we used the Stirling formula to expand the logarithms of the large numbers.

## ELECTRON-RANDOMIZATION

## COLLISIONS

In order to find the maximum of (5.56) subject to the conditions of Eqs. (5.51)

and (5.52), we use the Lagrange multiplier method [see, for example, Reif ( 1965)]

and set to zero the derivatives of the quantity 4> = r1 + <l' L Ni+ f3 L Ni(Fz)i, (5.57)

where o and f3 are the Lagrange multipliers. 6 We have: (5.58)

which yields (5.59)

The constants C and f3 can be found from Eqs. (5.51) and (5.52).

The concept of spin temperature is quite useful in understanding various aspects of optical pumping experiments; an example is given in Problem 5.7.

## 5.6 Electron-randomization collisions

Consider electron-randomization collisions of J = S = 1/2 atoms with, for example, spinless buffer gas atoms. Upon such a collision, the electron polar- ization of the atom is completely random - independent of its polarization prior to the collision. In this problem, we consider the effect of the nuclear spin / on the relaxation of atomic polarization.

Assuming that the duration of a collision is much shorter than the inverse fre- quency of the hyperfine interval and that / >> 1 /2, estimate how long it will take for an atomic polarization to relax if the characteristic electron-randomization time is T. 7 6 The idea behind the method of Lagrange multipliers can be understood as follows. The goal is to maximize a function/ (x) with respect to some variable x which is subject to a set of constraints {g( x) = 0, h( x) = 0, ... } . The derivatives with respect to x of the constraint functions are trivially equal to zero, so the derivative of the quantity f(x) +ag(x) +bh(x) + ... ,where a, b, ... are constants is also zero at the maximum of/ (x). This allows us to find /(x) in terms of the constants a, b, ....

Then, by choosing appropriate values for the constants a, b . ...• we can ensure that f(x) is maximized and the constraints are satisfied.

7 In general, the evolution of atomic polarization in this situation is quite complex, and for many observables (e.g. (Sz)), relaxation is described by more than one exponential [(Bouchiat 1963); see also Happer ( 1972) and Knize et al. ( 1988)). Here we are interested in estimating the longest time scale on which atomic polarization persists.

Solution

## ATOMIC COLLISIONS

Suppose, for example, that we start with an atom in a stretched state (Jz = J, lz = /). After one electron-randomization collision, the atomic polarization, although reduced, is not fully destroyed because most of the angular momentum of the atom was due to the nucleus (as I >> 1/2). After the collision, hyperfine interactions recouple the electron and the nuclear spins together, and the resulting change in MF is either O or I. In subsequent collisions, the change in MF will be 0, I, or -1, and the process can be thought of as a random walk. Since there are roughly (2/ + 1) possible values of MF, it takes on the order of (2/ + 1)2 random walk steps to spread the population over all sublevels (at which point the polarization is lost). Thus, the relevant time scale is I r' = (21 + 1 )

2r · I (5.60)

5. 7 Larmor precession under conditions of rapid spin exchange Consider a vapor of ground-state alkali atoms (J = S = 1/2, nuclear spin/)

in a magnetic field B. Suppose that the alkali density is so high that the spin-exchange rate (Problem 5.4) is much faster than the Larmor frequency nL of the atoms.

Detennine the rate of the magnetic precession of the average angular momen- tum vector (ff). Compare with the Larmor frequency for a free atom.

Assume that the atoms have nonzero average orientation, but their spin temper- ature (Problem 5.5) is high: 1 / (3 >> 1. Neglect the effect of the external magnetic field on the nuclear magnetic moment.

The regime of rapid spin exchange first investigated by Happer and co-workers (Happer and Tang 1973; Happer and Tam 1977) is important in extremely sensitive atomic magnetometers that are being developed for biomagnetic imaging (Kominis et al. 2003).

Solution Let us first neglect the magnetic field and assume that the orientation is along the quantization axis (z). The idea of the solution is to calculate the average total angular momentum of the ensemble (Fz) and the average electron spin (Sz). Then, we can assume that a weak (so magnetic precession is much slower than spin exchange) magnetic field of magnitude B is applied, for example, perpendicular to z which produces a torque of magnitude gsµ 0B(Sz) on the ensemble. The

LARMOR PRECESSION UNDER CONDITIONS OF RAPID SPIN EXCHANGE magnitude of the Larmor frequency can then be found according to (5.6 I)

According to the spin-temperature distribution, the average population of a sublevel with magnetic quantum number MF for a high spin temperature is 1 + /3A1F p(MF) = 2(2/ + 1)' (5.62)

which is true independently of which hyperfine state F this sublevel belongs to. In Eq. (5.62), we normalized the population by the total number of hyperfine structure sublevels for a state with J = 1/2.

The average angular momentum is /+1/2 F [I 1 ]

(Fz) = L L p(MF)MF = 4 + 31(/ + 1) /3, F=/-1/2 M,-•=-F (5.63)

where we carried out explicit summation using Eq. (5.62).

For an IF, MF) state, we can find the expectation value of Bz similarly to how we evaluated the 9F factors in Problem 2.4: (FM IS IF M ) = F(F + l) + /(/ + l) - 3/ 4 M (5.64)

' F z ' F 2F(F + I)

F· With this, we evaluate the ensemble-averaged value /+1/2 F (Sz) = L L p(MF)(F, MFISzlF, MF)= /3/4.

(5.65)

Similarly, /+1/2 F I L L p(MF)(F,MFllzlF,MF)

= 31(/ + 1)/3. (5.66)

F=l-1/2 M,.·=-F It is not surprising that the sum of average angular momenta of Eq. (5.65) and (5.66) yield the total average angular momentum of Eq. (5.63).

## ATOMIC COLLISIONS

Now that we have found (Fz) and (Sz), we can consider the effect of the magnetic field. Using Eqs. (5.65) and (5.63) in Eq. (5.61 ), we find n _ 2µo B L - Ii l+ jJ{J + 1) .

(5.67)

We can now compare this frequency to the magnitude of the Lannor frequency 9 nf for a free atom in a given hyperfine state (Problem 2.4)

nF = 2µo B.

L Ii 2/ + 1 Comparing this with Eq. (5.67), we find that _ 3(2/ + 1)

f}F OL- 3+4/(J+l)

L· (5.68)

(5.69)

It is interesting to note that, while an atom is continuously transferred between states with F = I+ 1/2 and F = I - 1/2 where the signs of the 9F factors are opposite (and of equal magnitude), there is net magnetic rotation of the average spin that is not too much slower than "normal" magnetic precession. For examp)e 9 for an I= 3/2 atom such as 87Rb, nL = (2/3)nf. The direction of the precession is the same as that for a free atom in the F = I+ 1/2 hyperfine state. The reason that this state "dominates" the precession of the average spin is that this state has more Zeeman sublevels (higher statistical weight) and that in the spin-temperature distribution, the difference in the population between the ±MF sublevels is the highest for the extreme sublevels with IMFI = I + 1/2 that are absent for the other hyperfine state.

## 5.8 Penning ionization of metastable helium atoms

Penning ionization is a process in which two atoms in a metastable state collide 9 and the excitation energy of one of them is transferred to the other, leading to ejection of one of the electrons of the latter atom.

A particular example of Penning ionization is collisions between 4He atoms (nuclear spin/ = 0), both of which are in the metastable 3 S1 state (4He*), resulting in a ground-state He atom, a He+ ion, and an electron. Generally, the cross-section for this process is quite large (on the order of 10- 13 cm 2 or larger); however9 if all the metastable helium atoms are prepared in one of the extreme Zeeman sublevels (M = 1 or M = -1), then the Penning ionization rate turns out to be suppressed by several orders of magnitude (Fedichev et al. 1996). This suppression played a

PENNING IONIZATION OF METASTABLE HELIUM ATOMS crucial role in the success of the experiments where Bose-Einstein condensation of 4 He* atoms was first demonstrated (Robert et al. 200 I ; Dos Santos et al. 200 I).

In this problem, we discuss the reasons for the suppression of Penning ion- ization for polarized 3 S1 4He atoms, and estimate the order of magnitude of the suppression.

(a) Discuss the qualitative reason why Penning ionization is suppressed for polarized 4He*.

(b) In order to estimate the degree of suppression of the Penning ionization for polarized atoms as compared to unpolarized atoms, we need to identify the process that leads to the ionization. Consider two atoms, both in the M = I state. Since the total angular momentum projection is A/pair = 2, the total spin of the system is S = 2. It turns out that the primary mechanism for Penning ionization of such a spin-polarized sample involves the dipole-dipole interaction between the magnetic moments associated with the atomic spins. The potential for this interaction is: (5.70)

Here 81,2 are the spin operators of the two atoms, R is the vector pointing from one nuclei to the other (and R is its magnitude), and the factor 4 is from the square of the Lande factor.

Show that the interaction (5. 70) does not preserve the total spin of the pair and estimate the characteristic order of magnitude of the interaction.

(c) According to the result of part (b), when two atoms collide, their total spin has a finite probability of changing in the course of the collision (the total angular momentum is conserved as spin angular momentum is exchanged with the angular momentum of the relative atomic motion). Once this happens, the spin-suppression of the Penning ionization is removed, and the collision results in ionization with high probability.

Estimate the order of magnitude of the probability P for changing the total spin assuming that the characteristic radii of al I interactions are on the order of ao, and that the depth of the interatomic potential is f"-..J 1 eV. The quantity P gives the estimate of the ratio of cross-sections for Penning ionization for polarized and unpolarized atoms.

Hint In part (b ), to show that the total spin is not conserved it is sufficient to explicitly calculate the matrix element (S = 0, Af = OIHdlS = 2, M = 2).

Solution

## ATOMIC COLLISIONS

(a) The total initial spin of a pair of colliding, polarized He* atoms is S = 2.

If Penning ionization occurs, the final state consists of two spin-1/2 particles (the He+ ion and the electron), and a spin-zero particle (the He ground-state atom); thus the maximum total spin of the final state is S = 1. Therefore, Penning ioniza- tion is suppressed: it requires a change in total spin, which cannot arise from the strong electric interactions responsible for most atomic collision processes. This is a similar suppression to that in radiative transitions (where the spin-flip or inter- combination transitions are typically suppressed by several orders of magnitude).

Another example of a similar effect is the relative suppression of spin-destruction vs. spin-exchange-collision cross-sections (Problem 5.4).

(b) One can show that the total spin is not conserved by the dipole-dipole interaction by showing that the Hamiltonian (5.70) does not commute with the operator (5.71)

The first term in (5.70) does commute with S2, so it is the second term that will prove to be noncommuting. However, instead of evaluating the commutator, let us calculate the specific matrix element as suggested in the Hint.

The initial and final states are resolved into the states of the individual spins according to IS= 2,M = 2) = ll)ill)2, IS= 0,M = 0) = IIhl -1)2 + I - I)ill)2 - IO)il0)2; v'3 (5.72)

(5.73)

here we use the notation IM)i for the i-th spin. It is, for reasons mentioned above, only the second tenn in (5.70) that contributes to the desired matrix element, so that (S = O,M = OIHdlS = 2,M = 2)

()( (S = 0, M = 01 ( 81 . R) ( 82 . R)

IS = 2, M = 2).

(5.74)

Expanding into spherical components (Vo = Vz; V± = =f (Vx ± iV11) / v'2), (5.75)

and using Eqs. (5.72) and (5.73), we find that the matrix element on the right-hand side of Eq. (5.74) is Ri/ v'3 ~ 0. Thus the dipole-dipole interaction does not conserve total spin.

PENNING IONIZATION OF METASTABLE HELIUM ATOMS (c) We will model the spin-changing collision in the following way. Consider a system originally in the S = 2 state. When the two colliding atoms approach within a distance ""' a0, they experience a perturbation of magnitude I Hd ~ µ~/a~ I (5.76)

that mixes different spin states. The perturbation acts for a characteristic collision time ao/v, where the characteristic velocity v is given by v~ /Wa, V -;;;;; (5.77)

where ma is the atomic mass and the interatomic potential Va rv 1 eV. Thus v ,v 106 cm/s. The amplitude of finding the system in the S = 0 state increases linearly in time for the duration of the collision, so a characteristic probability P of changing the spin during the collision is p rv ( µ~ ao)

2 ~ 10-5 lia3 ' 0 V (5.78)

which is in agreement with more detailed calculations (Fedichev 1996).

## COLD ATOMS

6.1 Laser cooling: basic ideas (T)

Laser cooling is an elegant and important tool that has been useful in many branches of atomic physics. For example, laser cooling has enabled the creation and study of Bose-Einstein condensates of dilute atomic vapors (Anderson et al.

1995, Bradley et al. 1995, Davis et al. 1995) and is a central feature in the latest generation of atomic clocks (Santarelli et al. 1999). The creation of cold atomic gases via laser cooling has provided a new venue in which to study atomic collision processes, nonlinear optical effects, and basic quantum-mechanical phenomena.

There are innumerable excellent reviews on this vast subject - good starting points are the Nobel lectures by Chu (I 998), Phillips ( 1998), and Cohen-Tannoudji ( 1998), as well as the text by Metcalf and Van der Straten ( 1999).

Here we will address some of the basic concepts involved in laser cooling. In previous chapters there were many problems dealing with the effect of light on internal atomic states [such as optical pumping (Problems 3.7, 3.9, and 3.10)), but in laser cooling and trapping we are interested in the mechanical effects of light on the external state of an atom, i.e. its position and momentum.

Consider a two-level atom initially at rest. Suppose that the atom is exposed to a beam of light tuned to resonance with the jg) -+ le) transition (where jg) is the atomic ground state and le) is the excited state). If a photon is absorbed by the atom, then the atom receives a momentum "kick" ~pwhere (6.1)

- where M is the mass of the atom, DA'v is the change in the atomic velocity, and k is the wave vector of the incident photon.

We must also account for spontaneous emission. The fluorescence photon will be emitted by the atom in a random direction (actually, as discussed in Problem 3.8, there may be favored emission directions depending on, for example, the polariza- tion of the incident light, but this is not essential at this stage). The ref ore, the atom recoils in a random direction due to spontaneous emission.

Thus we see that if a group of atoms is exposed to a resonant laser beam, they gain momentum in the direction of the beam and heat up due to the random kicks

## COLD ATOMS

I I FIG. 6.1 Schematic diagram of the setup for optical molasses. Six .. red-detuned" laser beams (frequencies lower than that of the atomic transition with which they are nearly resonant), arranged in pairs of counter-propagating beams in three mutually orthogonal directions, provide a velocity-dependent damping force that cools the atomic vapor.

from the spontaneously emitted photons. This is the basic principle behind the manipulation of atoms with laser light.

(a) Suppose we already have a cloud of two-level atoms at rest, and we shine laser beams at the cloud from six different directions as shown in Fig. 6.1, so that there is a pair of counter-propagating laser beams in three orthogonal directions. This is the setup for optical molasses. In this hypothetical situation, the atomic cloud starts with a temperature T = 0 and then heats up due to the light.

Suppose we expose the atomic cloud to the laser beams for a time r for which, on average, each atom has undergone a single absorption-emission cycle (assume that the light power is sufficiently small so that stimulated emission can be neglected, and that the vapor is sufficiently dilute so that radiation trapping is unimportant). What is the temperature T = 2T,., of the atomic cloud (T,., is the single-photon recoil temperature limit)? Estimate the numerical value of T,., for sodium atoms.

LASER COOLING: BASIC IDEAS (T)

Solution Since, on average, an atom has acquired one momentum kick ~pfrom an absorp- tion event and another kick ~p' from a spontaneous emission event, both in random directions and of equal magnitude, we say that the average energy of an atom in the cloud is (6.2)

where we used the facts that the magnitude of the wave vector is lkl = w / c where w is the light frequency and that the cross-term 2p • ~p' averages to zero over the atomic sample.

This corresponds to a thermal energy rv 2k 8 T1 , or li2w2 T-y ~ 2kBMc 2 ' (6.3)

where kB ~ 10- 4 eV /K is Boltzmann's constant.

For sodium atoms excited on their first resonant transition (DI line), we have flJ.,c)

rv 2 eV and Mc 2 ~ 23 X 109 eV, so T. rv (104 K/eV) · (2 eV)

~ 1 µK 2 x 23 x 109 eV ' (6.4)

a low temperature indeed!

(b) Let us again consider the optical molasses setup (Fig. 6.1 ), but this time we will show how one can cool a gas of atoms initially at a high (e.g. room) temperature.

Consider an atom moving with velocity v toward one of the laser beams. The frequency of the light in the rest frame of the atom is Doppler-shifted according to (6.5)

Suppose that the laser beam is "red-detuned," i.e., its frequency w is lower than the resonance frequency w0 for the fg) -+ le) transition of an atom at rest. Then - the laser light preferentially interacts with atoms moving opposite to k, and thus provides a slowing force in this direction. In the optical molasses, atoms are being slowed in all directions, which evidently leads to cooling. The optical molasses exerts a velocity-dependent force which is akin to a viscous drag on the atomic motion, hence the name.

As the atoms slow down, the detuning of the laser light must change in order to continue interacting with the atomic gas (since the Doppler width is becoming nar- rower). One way to continue the cooling process is to chirp (gradually increase) the

## COLD ATOMS

laser frequency. Another method, commonly used to slow atomic beams, involves shifting energy levels with a magnetic field and is discussed in Problem 6.3.

There appears to be no problem cooling atoms to temperatures where the Doppler width becomes comparable to the natural width of the transition '"Yo, since when the Doppler width r D is greater than "'Yo one can selectively address the velocity groups containing fast moving atoms.

What is the temperature T* of the atomic cloud when "'Yo ~ r D? Give a numerical estimate of T* for Na atoms.

Solution The Doppler width is given by rv = Wo ✓2kBT.

C M By equating r D with "'Yo we obtain For Na atoms, T * 2 Mc2 rv "'Yo k 2 • 2 BWo T*~40mK, (6.6)

(6.7)

(6.8)

which is considerably larger than the single-photon recoil limit T'Y [Eq. (6.4)).

(c) Once T* is reached the atomic transition is dominated by homogeneous broad- ening. To cool the atoms further, we must find an appropriate value for the laser detuning. If the laser is tuned so that w0-w >> "'Yo, there will be very few light-atom interactions, so the cooling force will be quite small. On the other hand, if w = w0 there is no cooling force at all. As a compromise we choose wo - w = "'Yo/2.

The atoms get kicks from all directions now, but if an atom is moving toward one beam, it would tend to get more kicks opposing its motion.

Consider motion in one dimension. Calculate the velocity-dependent force on the atoms for a one-dimensional optical molasses under these conditions.

Solution Since we have assumed a light power small enough that stimulated emission can be neglected, we also have (6.9)

LASER COOLING: BASIC IDEAS (T)

-- - C> --+ 0.75 0.5 ~ 0.25 ~ ~ / -0.25 -0.5 -0.75 p 2 ly c)

FIG. 6.2 Velocity-dependent force for a one-dimensional optical molasses in the regime where r D ;S -;-o. Note that atoms experience a force which opposes their motion, and in the range lvl << -;-oc/{2w) it is a linear restoring (spring) force in velocity space.

where "' is the resonant saturation parameter (Problem 3.7), d = (eldlg) is the dipole matrix element, and e0 is the amplitude of the optical electric field. Based on the considerations in Problem 3.7 [Eq. (3.172) with K << 1], we can say that the rate R at which the atoms scatter photons is R _ K10 ± - 2' 1 + (1 ± 2w ~)

')'o C (6.10)

where ± refers to laser beams propagating to the right and left, respectively, in the diagram at the top of Fig. 6.2. Note that we take the case K << I here for algebraic and conceptual simplicity; in most laser-cooling experiments, K ;S 1 is typical.

On average, each absorption-emission event imparts a momentum kick of w ~P± = ±h-e (6.11)

to the atom, so the average force due to the counter-propagating laser beams is (6.12)

(6.13)

where

## COLD ATOMS

which after some algebra yields (F} = _4 K"foliw /3 C 4 + {34 8fiw2K C which is plotted in Fig. 6.2.

(6.14)

v/c (6.15)

(d) Find to what temperature (Tv) the atoms can be cooled using this method.

Estimate the numerical value for this temperature To, known as the Doppler limit for temperature, for Na atoms.

Solution The average momentum imparted to the atomic cloud by the laser beams is zero, so (p) remains constant. On the other hand, (p2) is reduced by the mechanisms we have discussed above, but is also increased by random kicks from spontaneous emission and the random nature of the absorption events. We will determine the equilibrium value of (p2) by balancing the heating and cooling rates.

The characteristic velocity of the atoms is v= (6.16)

and the thermal energy of the gas is (6.17)

where we again consider motion in one dimension (extension to three dimensions will not change our basic conclusion substantially).

The rate of change of the energy E of the gas due to the cooling force described in part ( c) is given by {)E - 2 v2 !M I = (F)v ~ -2/iw K 2 , ui cool C (6.18)

where we employ Eq. (6.15) assuming that f3 << 1, i.e., wv / c << ,o.

Now we must account for the heating of the gas caused by the random nature of the atomic recoils due to absorption and emission. In a given absorption/emission

LASER COOLING: BASIC IDEAS (T)

cycle, the atom receives two random kicks of magnitude hw / c. The rate at which the atoms get these kicks is ~ "-,o [this follows from Eq. (6.10), where again we make use of the approximation f3 << I and recall that we have two laser beams].

This is just a random walk in momentum space, so we say that D I h2w2 -(Ji)

~ 2K,o--.

Dt heat c2 (6.19)

thus 8E li2w2 -I =1-t,0--.

Dt heat Mc 2 (6.20)

In equilibrium DEi +f)EI =0 fJt cool fJt heat ' (6.21)

so from the expressions (6.18) and (6.20) we obtain ~Mv2 = h,o .

(6.22)

Thus, from Eqs. (6.17) and (6.22), we have for the equilibrium temperature (6.23)

which is known as the Doppler limit. For Na atoms: TD~ 200µK.

(6.24)

This turns out to be the cooling limit for two-level atoms.

Interestingly, when experiments with 3D optical molasses were first performed, temperatures an order of magnitude lower than Tv were observed. The physical mechanisms which lead to such sub-Doppler cooling are related to the fact that real atoms used in the experiments are not two-level systems, but actually have Zeeman sublevels and hyperfine structure. Light shifts and optical pumping among these sublevels conspire to produce effects such as Sisyphus cooling which enable one to reach temperatures below Tv. These phenomena are well described in the article by Cohen-Tannoudji and Phillips ( 1990).

In fact, experimentalists have figured out how to beat the single-photon recoil temperature limit as well, taking advantage of velocity-dependent dark states (Aspect et al. 1988) and also using velocity-selective Raman transitions (Kasevich and Chu 1992).

(e) Relate the three temperature scales, T"f, T*, and Tv to one another.

Solution COLDAlOMS Comparing Eqs. (6.3), (6.8), and (6.23), we find the suggestive relationship

## 6.2 Magneto-optical traps

(6.25)

Although the optical molasses described in Problem 6.1 cools atoms, it does not trap them. There are many techniques used to spatially confine atoms [see Metcalf and Van der Straten ( 1999) ], but the most widely used atom trap is the magneto- optical trap (MITT) pioneered by Pritchard et al. ( 1986) and Raab et al. ( 1987)• The trapping mechanism in a MITT is analogous to the cooling mechanism for optical molasses - an inhomogeneous magnetic field causes the force due to light scattering to acquire a position dependence.

Consider a one-dimensional MITT (Fig. 6.3). Two counter-propagating taser beams, one left-circularly polarized (u+) and the other right-circularly polarized a cr .

• gn ti fi Id CJ.

a a_ cr =-/ f O

## M - J

\ti - J M {)

1 I FIG. 6.3 Schematic setup for a one-dimensional magneto-optical trap. Because the inhomogeneous magnetic field shifts the 7.eeman sublevels of the upper state, the atoms to the left of the trap center tend to scatter more photons from the laser beam propagating to the right while atoms to the right of the trap center scatter more photons from the laser beam propagating to the left. This creates a restoring force which keeps the atoms near the center of the trap. Since the laser beams also create an optical molasses (Problem 6.1 ), the atoms are cooled as well.

## MAGNETO-OPTICAL TRAPS

(a_), are directed at a cloud of atoms. 1 An inhomogeneous magnetic field B(z) = {3zi (6.26)

is applied to the atoms. Here {3 = 8B / 8z = constant. The light frequency is detuned by ,o/2 below resonance with an F9 = 0 --+ Fe = 1 transition., where ,o is the natural width of the transition and g, e refer to the ground and excited states., respectively. Assume that the Doppler width is much smaller than the natural linewidth for the atomic transition.

(a) Calculate the average, position-dependent force on the atoms due to light scattering.

(b) The light also cools the atomic sample as discussed in Problem 6.1, so the equation of motion for cold atoms in the trap takes on the form of that for a damped harmonic oscillator close to the trap center (the Doppler and Zeeman shifts are small in comparison to the natural linewidth , 0).

Find the oscillation frequency and damping constant near the center of the ID MOT. Fpr simplicity, assume here that the saturation parameter K (Problem 3.7) satisfies K << 1, although in typical MOT operating conditions K ;S 1. Give a numerical estimate of the characteristic damping time for a typical atom in a magnetic field gradient of 5 G / cm.

Solution (a) Using the same analysis applied in Problem 6.1 to derive Eq. (6.10), the photon scattering rates for the two beams are given by K,~ R± = 2 , ( • 7)

1 + [1 ± 2gµoB/(li,o)]

where g is the Lande factor and ± refer to the a± polarized light beams (recall that we have specified a detuning of , 0/2 from resonance). Note that all we have done to go from Eq. (6.10) to (6.27) is replace the Doppler shift with the Zeeman shift. Since each scattering event imparts, on average, a momentum kick of lik to the atom (where k is the wave vector), we have (6.28)

Since B = {3z, the force is position dependent; (F( z)) is plotted in Fig. 6.4.

1 Recall that the circular polarizations are defined with respect to the + z direction, not necessarily the light propagation direction.

## COLD ATOMS

0.75 ,.-..

0.5 ~ ""'--a 0.25 ~ ~ ..._., / ·', -0.25 ~ -0.5 V -0.75 Normalized position (2gµ 0~z/hy0 )

FIG. 6.4 Position-dependent force for a one-dimensional magneto-optical trap.

(b) Near the center of the trap, the Zeeman shifts are small compared to the natural linewidth of the transition, so we can write

## KJJJ

## KJJJ

(F(z)) ~ -8-gµoB(z)

= -8-gµof3z.

C C (6.29)

There is also the cooling force (6.15), which for sufficiently slow atoms is Kfu.u2 (F(v)) ~ -8 2 v.

C (6.30)

Thus the equation of motion for atoms in the ID Mar is M ..

s"'ru.u2 . s w f3 Z = - Z - K-gµo Z , C C (6.31)

which is the equation for a damped harmonic oscillator (M is the atomic mass).

Thus the atoms in the Mar are spatially confined and they slow down over time (cool). The oscillation frequency for the trap is given by 8 wgµo/3 wt = K Mc ' (6.32)

and the damping constant is (6.33)

## MAGNETO-OPTICAL TRAPS

To find out whether the harmonic oscillator is underdamped or overdamped, we compare the trap oscillation frequency to the damping rate: wl gµof3Mc 3 r 2 - 8/i2w3K ' t which can be rewritten as a product of some suggestive factors: where A is the wavelength of the light.

(6.34)

(6.35)

Since we have already assumed that the saturation parameter is less than unity, we can estimate that the first factor, (l61rK)- 1, is ;S 10- 2. The second factor in Eq. (6.35) is the ratio of the change in the Zeeman shift over the wavelength of the light, gµ 0{3A, and the energy of a photon, hw. We have {3 = 5 G/cm and A rv 5 x 10- 5 cm for an optical transition, so gµ 0{3A/ Ii ""' 21r x 1 Hz. The photon frequency is w ""' 21r x 1015, so gµ 0(3A/(hw) ""' 10- 15. The third factor is the ratio of rest energy of the atom and the photon energy, which has the value M c2 / ( hw) ""' 1011 for M = 100 amu. Combining these factors, we see that the motion is strongly overdamped, as long as"' is not too small: wt/ft ""' 10- 6 K- 1.

Since in typical MOT operating conditions"'""'

## 0.1 - 1, this is indeed the case

The characteristic damping time of the MOT can be estimated as follows. The differential equation governing the motion of an atom in the MOT is ·· r · o Z + tZ + WtZ = .

(6.36)

We guess the solution z(t) = z0eiwt, where zo is the atom's initial position and w is complex. Plugging this guess into Eq. (6.36) and solving for w we get w = irt ± J4wl - r; .

<637 )

In the strongly overdamped regime, Wt << r t/2, so we can estimate that w ~ i~t [u (1 _ 2;D J .

(6.38)

Thus w is pure imaginary. Suppose that at time t = 0 the atom is displaced from the center of the trap and has zero initial velocity. Then the general solution is z(t) ~ zo( Ae-r,t + Be-<wl/f,)t) , (6.39)

and since (6.40)

## COLD ATOMS

the slowest rate dominates the motion of the atom back to the center of the trap, namely: (6.4))

where ft hw T rv - rv -- rv 5 ms.

w'f gµ/3 (6.42)

## 6.3 Zeeman slower

In an experiment at the Lawrence Berkeley National Laboratory (Lu et al. 1994), short-lived radioactive 21Na atoms (22.5 s half-life) are produced by bombarding stable magnesium atoms with a beam of protons in the reaction p + 24Mg -+ 0 + 21 Na. The resulting sodium atoms are evaporated and a fraction of them are subsequently cooled and trapped in a magneto-optical trap (Problems 6.1 and 6.2).

A schematic of the apparatus is shown in Fig. 6.5.

The magnesium atoms (in the form of MgO ceramic disks) are placed in an oven where the interaction with a proton beam from an accelerator occurs. When the oven is heated (to 500 °C), an atomic beam of 21 Na is produced. As the atoms in the beam travel toward the magneto-optical trap, their transverse velocities are first reduced with laser beams in the transverse-cooling region. The atoms then travel a distance l = 1.2 m in a region where they are slowed to essentially zero longitudinal velocity by interaction with a counter-propagating laser beam before the actual trapping occurs. It is this slow-down region we will be concerned with in this problem.

The slowing laser beam is tuned near the F = 2 -+ F' = 3 hyperfine com- ponent of the 3 2S1; 2 -+ 3 2P3; 2 transition (D2 line, A = 589 nm, excited state lifetime r = 16 ns, nuclear spin I= 3/2) and has u+ polarization. The resonance frequency of the atoms in the beam is Doppler-shifted. As the atoms slow down, the Doppler shift decreases. In order to keep the atoms in resonance with the laser beam used for slowing, a spatially varying magnetic field is produced by a solenoid with nonunif onn winding.

(a) Assuming that the atoms are always in resonance with the slowing laser light, estimate the time it takes the atoms to stop for the case where the saturation parameter is"'= 1 (see Problem 3.7).

(b) Assume for simplicity that all atoms initially have the same longitudinal veloc- ity corresponding to the oven temperature. The laser is tuned near the zero-field resonance frequency.

Proton beam Trapping laser beam

## ZEEMAN SLOWER

Oven Transverse cooling beam -- Ion vacuum pump Zeeman slower solenoid Magneto-optical trap Slow down laser beam FIG. 6.S Schematic diagram of experimental apparatus for trapping and cooling of radioactive 21 Na atoms, from Lu et al. (1994).

## COLD ATOMS

Calculate the size and longitudinal coordinate dependence of the magnetic field that needs to be produced by the slow-down solenoid.

Solution (a) The relevant saturation parameter in this case is given by: d2e2 K= -2-, (6.43~ where dis the transition dipole moment, e is the electric field of the light, and 70 is the natural width of the excited state. Essentially, this says that the rate of pumping atoms from the ground state to the excited state, d2e2 I'pump ~ -- , ,o (6.44)

is equal to the rate of spontaneous decay from the excited state ,o.

Optical pumping to other levels does not occur because this is a closed transition, and there are 00 ground-level dark states for this transition (see Problem 3.9).

The average force (F) acting on the atoms due to the laser light is given by: ~P !ik (F) = ~t = 4T' (6.45)

where !ik is the momentum of an absorbed photon and r is the lifetime of the upper state.

Equation (6.45) can be understood as foJJows. For each absorption event, an atom receives a momentum kick in the direction of light propagation. There is no average momentum imparted to the atoms from spontaneous emission since ph0- tons are spontaneously emitted in (approximately) random directions. Now, dt is the time for one cycle of pumping and spontaneous emission. Since "' = 1, the rates of spontaneous emission, stimulated emission, and absorption are the same (~ ,o). We can then estimate that each cycle of absorption and emission takes 2T, and roughly half the time such a cycle involves spontaneous emission (no momen- tum is imparted to the atom by absorption followed by stimulated emission). Thus the effective time for slowing an atom by !ik / M is 4r. The average force for ,.\ = 589 nm and r = 16 ns is (F) ~ 2 x 10- 15 g · ~m = 2 x 10- 15 dynes.

(6.46)

s To determine the length of time that the laser must act on the atoms in order to stop them, we must know their initial momentum as they effuse from the oven.

## ZEEMAN SLOWER

The most probable velocity of an atom effusing from the oven can be found in the following way (Reif 1965). Consider a group of atoms inside the oven with velocities between v and v+dv headed toward the exit hole in the front of the oven.

The density of atoms n( v) with such a velocity is given by the MaxweJJ-Boltzmann distribution and the flux 4>( v) of such atoms leaving the oven is 4>(v) <X n(v)Av, (6.47)

(6.48)

where A is the area of the hole. Thus the most probable velocity v can be found by determining the velocity for which <P( v) is a maximum: {)<P -=0 8t (6.49)

for __ ✓3kBT V- M ' (6.50)

where M is the atomic mass. Note that this differs from the most probable speed of an atom inside the oven, which is J2k 8 T/M.

Based on (6.50), we find the most likely initial momentum p 0 of a sodium atom 1s: V IB Po =3kBTM ~ 3 x 10- g · -, s (6.5 I)

which corresponds to a thermal velocity of"' 105 emfs. The stopping time is given by the ratio of the initial momentum to the average light force, ts1op = (1;) ~ 1.5 X 10- 3 S , (6.52)

In the actual experiment, tstop ~ 3 x 10- 3 s, corresponding to K ~ 1/2.

(b) In this part of the problem, we assume that all atoms have the same initial veloc- ity and set "" = 1. We also make use of the fact that the closed, "cycling" transition is between the two stretched states of the F = 2 and F = 3 levels (i.e., MF= F), for which the Zeeman shifts are the same as for that of a spinless nucleus (ignor- ing the interaction of the nuclear magnetic moment with the field). Hence we just

3IO

## COLD ATOMS

work with the total electronic angular momentum J. The atoms are always kept in resonance by the magnetic field, so they undergo uniform deceleration: a= (F) = lik ~ 6 x 107 c1: .

M 4rM s (6.53)

Note that this is~ 6 x 104 g (where g is the acceleration due to Earth's gravitational field), i.e., the atoms emerge from the oven with the speed of a supersonic jet and are brought to a stop in I meter!

The light frequency is Doppler shifted by an amount v(z)

~w(z) =w-, C (6.54)

where z is the distance from the trap and v(z) is the atomic velocity as a function of the distance. The velocity as a function of distance in terms of the deceleration a IS v(z) = v'2az.

In order to keep the atoms on resonance, we need to equate the Zeeman shift created by the magnetic field to the Doppler shift ~w(z).

For u+ polarized light, atoms tend to be pumped into the MJ = 1/2 ground state Zeeman sublevel. Since atoms experience many optical pumping cycles, it is the energy difference between the 3 2S112 MJ = 1/2 and 3 2 P312 MJ = 3/2 states which is important for slowing the atomic beam. The Zeeman shift of the resonance frequency for u + polarized light is given by µoB(z)

~w = [Be · (3/2) - g9 • (1/2))

1i , (6.55)

where 9e = 4/3 and g9 = 2 are the excited and ground state Lande factors (Prob- lem 2.4), µo is the Bohr magneton and B(z) is the magnetic field as a function of distance from the trap. By equating the expressions (6.54) and (6.55), we find: Numerically, this result is: B(z) = hwo../2az .

µoc (6.56)

( 21r x 5 • 1014 Hz )

B(z) ~ 2 6 H /G 3 / v'IOS cm• s- 2 .,/z ~ 120.,/z G.

1r x 1.4 • 10 z cm s where z is the distance from the trap in cm.

BOSE-EINSTEIN CONDENSATION (T)

## 6.4 Bose-Einstein condensation (T)

Atom trapping and cooling (see, for example, Problems 6.1 and 6.2) paved the way for the observation of Bose-Einstein condensation (BEC) of atomic gases (Ander- son et al. 1995, Bradley et al. 1995, Davis et al. 1995), which has developed into a very exciting field of research at the boundary between atomic physics and condensed-matter physics [for reviews see the Nobel lectures by Cornell and Wie- man (2002) and Ketterle (2002) and the book by Pethick and Smith (2002)]. For some time it has been recognized that the phenomena of superfluidity and super- conductivity were somehow related to BEC, but since these phenomena had been observed in systems in which the interactions between the constituent particles play an important role, it was of considerable interest to create a BEC with an "ideal gas."

The signature of a BEC is that there is macroscopic occupation of a single quan- tum mechanical state describing the atomic motion. In a room-temperature atomic gas, there is an enormous number of accessible quantum mechanical states, so the probability that even two atoms are in the same state is very small. As the temper- ature of the gas is decreased, however, the number of accessible states becomes smaller, until at a certain very low temperature, called the Bose-condensation tem- perature, Tc, a large fraction of the (bosonic) atoms occupy the lowest energy quantum state. Intuitively, we can see that this regime should set in when the deBroglie wavelengths, Ade, of the atoms are equal to the characteristic distance between the atoms. Under these conditions, the accessible number of quantum mechanical states is about equal to the number of atoms.

This is a qualitatively different regime for the gas: now instead of each atom having a different position and momentum, as is generally the case for a room- temperature gas, the position and momentum of a large number of atoms are described by a single wavefunction.

In this tutorial, we derive Tc for a gas of N noninteracting bosonic atoms of mass m 0 in a box with volume V. We assume that the gas is in thermal contact with a heat bath. 2 (a) Using the simple picture that Bose-Einstein condensation occurs when the characteristic distance between atoms becomes comparable to their deBroglie wavelengths Ade, estimate the Bose-Einstein condensation temperature Tc.

2 It is imponant to note that these considerations are modified in the presence of a trapping potential. which is typically present in BEC experiments.

Solution

## COLD ATOMS

The deBroglie wavelength of an atom is given by: 21rn Ade=--, mav (6.57)

where v is the atomic velocity. The most probable velocity of a particle in a gas is given by: (6.58)

where T is the temperature of the gas. Thus the typical Ade for atoms in the gas as a function of temperature is given by: (6.59)

The deBroglie wavelength is equal to the interatomic separation when: Ade~ ( :)-l/J (6.tiO)

From Eqs. (6.59) and (6.60) we deduce the estimate for the Bose-Einstein condensation temperature Tc: (6.61)

(b) The above considerations are enough to get the basic scaling of Tc, but a rigor- ous approach is both instructive and provides a more precise numerical coefficient, which will tum out to be important in Problem 6.5.

Before we embark upon this relatively complicated calculation, let us outline our approach. We rely on the picture that the BEC transition occurs when a large fraction of atoms occupy the lowest energy state. We arrange the energies Ei that an atom in the box can possess in ascending order and, for simplicity, assume that they are distinct: 0 = fQ < fl < f2 < f3 < .. · We begin by finding an expression for the probability p( ni) of finding ni atoms in the quantum mechanical state Ii) having energy Ei. As mentioned in the intro- duction to the problem, for atomic gases well above the condensation temperature,

BOSE-EINSTEIN CONDENSATION (T)

p(ni) << 1 for ni > 0. The obtained expression can be used to see for what tem- perature the average number of atoms in the ground state, (No), becomes large.

We will see that (No) grows rapidly as a function of temperature below Tc.

One of the remarkable properties of a BEC, best illustrated by this formal approach, is the fact that, under the considered conditions (thermal contact with a heat bath), if more atoms are added to the sample, they join the condensate fraction (No). This is because the average number of atoms in the excited states (N*) is fixed by the temperature of the gas - all remaining atoms must occupy the ground state. This is why the chemical potential µ, which represents how much the energy of a system changes when the number of particles in the system changes, is close to zero for a BEC. This can be contrasted with a room-temperature gas where energy depends directly on N.

The first step is to find an expression for p(ni)- Since there are N atoms in the box with a total energy of E, the system is subject to two constraints: and Lni = N, i=O E = Lniii- i=O (6.62)

(6.63)

Use these constraints to express the probability p(ni) that ni atoms possess energy fi in terms of ni, fi, the temperature T, the chemical potential µ, and appropriate constants.

Solution According to statistical mechanics [see, for example, Reif ( 1965)], p( ni) is pro- portional to the number of microstates n which have ni atoms in state Ii). The quantity n is given by the number of accessible microstates Orest for the other N - ni atoms in the rest of the system consistent with the constraints, Eqs. (6.62)

and (6.63): p(ni) ex Orest(N - ni, E - nifi)- lt is convenient to use the entropy S = kB Inn, kB lnp(ni) = canst.+ Srest(N - ni, E - nifi)- (6.64)

(6.65)

Srest is approximately the total entropy in the system S, and we can expand Sin a power series in the variables N and E, kB lnp(ni) ~ const. + S(N, E) - ni ( :i) E - niii ( !!)

N' (6.66)

## COLD ATOMS

where we are justified in neglecting higher order terms in view of the fact that in general N >> ni and E >> nifi. Now we can make the following identificatio~ from thermodynamics (Reif 1965): (!!t = ~, (6.67)

and (6.68)

where µ is the chemical potential. Thus, by using Eqs. (6.67) and (6.68) in Eq. (6.66), we find that (6.69)

where (6.70)

and (6.7 I)

The term S(N, E) only contributes to the normalization as N and E are constant for the whole gas.

To find the exact probability, we must introduce the restriction (6.72)

and thus determine the normalization factor for p(ni, niEi). We note that the sum Zi of all the unnormalized probabilities from Eq. (6.69) is a geometric series: Zi = 1 + Ae-/3t.i + A2e- 213t.i + ...

- 1 - Ae-/3t.i .

(6.73)

Thus the probability to find ni atoms in state i is Ani e-ni{3E; p(ni)=---.

Zi (6.74)

(c) Use Eq. (6.74) to express the average number of atoms in the ground state (No)

and the excited states (N*) in terms of A [Eq. (6.71)) and a sum over Zi• Note the behavior of (No) as the chemical potential goes to zero.

BOSE-EINSTEIN CONDENSATION (T)

Solution The total number of atoms N equals the sum of the average number of atoms ( ni)

per state: (6.75)

wherep(ni)

is given by Eq. (6.74). Since (6.76)

we have for the total number of atoms N = f A 8(lnzi).

i=O [)A.

(6.77)

Thus the average number of atoms in the ground state is I (No) = 1 ~ A ' I (6.78)

and the average number of atoms in the excited states is (N*) = f A 8(lnzi)

.

i=l [)A.

(6.79)

Because (No) > 0, we see that the chemical potential µ < 0. Notice that as the chemical potential µ ~ 0, A ~ 1, so (No) ~ oo. This result is unphysical, since there are only N atoms in the gas. The paradox is resolved by saying that just above Tc, A is sufficiently less than unity so that almost all the atoms are in the excited states, i.e., (N*) = N. However, for the purposes of our calculation, A is so close to one that we may set A = 1 in (6.79). Then, as the temperature falls below Tc, the atoms will accumulate in the ground state. We will be able to find a formula for (N*) as a function of T, and then we will say that (No) = N - (N*) .

(6.80)

In other words, A is always just a bit smaller than one so that (No) < N [Eq. (6.78)).

## COLD ATOMS

(d) Now consider the probability p to find the entire system in one particular microstate. The quantity p, being the joint probability of finding no atoms in the ground state, n 1 atoms in the first excited state, and so on, will be the product of all the individual probabilities p(ni) given by Eq. (6.74): oo ( Ae-,Bt:i) n.

p=Il_,;_...._-.

Zi i=O (6.81)

The normalization factor in this case is known as the grand partition function Z: (6.82)

and is useful in calculating various thermodynamic properties of a system (Reif 1965) - in particular we will use Z to calculate Tc and the entropy S of the BEC.

Consider the natural logarithm of Z: lnZ. = Ltn 1 _ >..e-/3i • .

i=O (6.83)

By relating this quantity to the total number of atoms in the gas N, and setting it equal to (N*) with A= 1, we will be able to find the conditions for Bose-Einstein condensation.

Find the relationship between the total number of atoms in the gas N and In z.

Solution Based on Eqs. (6.77) and (6.83), we obtain for the total number of atoms I N = >..a!~ z. . I (e) If we separate out the ground state term (eo = 0) in Eq. (6.83), we have lnZ = ln 1 _ >.. + Ltn 1 _ >..e-f3i, .

i=l (6.84)

(6.85)

Evaluate the second term in Eq. (6.85), which corresponds to atoms not in the ground state, in terms of the function Fk(A), where (6.86)

BOSE-EINSTEIN CONDENSATION (T)

This is a function that can be numerically evaluated for different values of k and A. In particular, we will use this formula in Eq. (6.84) with A = 1 to obtain an expression for (N*) at Tc.

Solution First we recall that (as can be seen, for example, from Taylor expansion): xn In - = ~ - .

l-x ~ n n=l We can rewrite the second term in Eq. (6.85) as (6.87)

(6.88)

which can be evaluated as follows. For free atoms in a box (assuming no internal degrees of freedom), the single particle energies are given by: (6.89)

where q1, q2, and q3 are the quantum numbers describing the motion of the atom in the box (i.e., the quantization condition is that the momentum in a particular direction j is given by PJ = 1r !iq1 / L, where L is the length of a side of the box).

In this case, E~ 1 e-n/3t.; becomes the triple sum: (6.90)

## COLD ATOMS

which can be explicitly evaluated by converting to an integral: li2 7r2 ' ~ e-n~t, = ( ~ exp [-n.B 2ma V2/3 q2] )

( roo [ li2 7r2 ] )

= Jo exp -n.B 2ma V2/3 x2 dx V (makBT)

= n3/2 21rfi2 (6.9J)

The factor (makBT)

nq = 2-,rf;,2 ~ A~B (6.92)

is known as the quantum concentration.

We obtain from Eqs. (6.85), (6.88), and (6.91) the following expression for In Z: lnZ. = In l -A+ nqVFs12(A), (6.93)

where F5; 2(A) is given by Eq. (6.86).

(f) Now use the expression for In Z [Eq. (6.93)] in Eq. (6.84) to obtain a fonnula for the total number of atoms N. By setting (N*) = Nat T = Tc with A = 1, find the Bose condensation temperature Tc. Use the fact that F3;2(l) ~ 2.612.

(6.94)

Solution According to Eqs. (6.93) and (6.84), we have at T = Tc IN~ nqVF312(l) = (N*). , From Eq. (6.95) we obtain Tc: li2 (N)2/3 Tc = 3.31 makB V .

(6.95)

(6.96)

Comparing Eq. (6.96) to Eq. (6.61), we see that the exact Bose condensation temperature is smaller than our approximate expression by a factor of~ 6.

(g) Calculate Tc for a free gas of sodium atoms at a density of 1012 atoms/cm 3 •

BOSE-EINSTEIN CONDENSATION (T)

Solution The exact Bose-Einstein condensation temperature for a free gas of sodium atoms with a density of 1012 atoms/cm 3 is T, _ :3.31 · {6.6 x 10- 10 eV • s)2. (108 cm- 2)

c - (8.6 x 10- 5 eV /K) · (23 • 931 x 106 eV)/(3 x 1010 cm/s)

=7.1 x 10- 8 K.

This temperature, around one hundred nanokelvin, is an order of magnitude colder than the single-photon recoil limit for laser cooling (Problem 6.1 ). In order to bridge the gap between temperatures achievable with laser cooling and those required for formation of a BEC, the technique of evaporative cooling is com- monly employed (Masuhara et al. 1988). This involves loading the cold atoms into a magnetic trap and gradually reducing the depth of the trap so that the most energetic atoms escape while the others re-thennalize at a lower energy.

(h) Calculate the entropy S of a Bose gas below the critical temperature Tc. (We will use this information to help solve Problem 6.5.)

Hint In order to calculate the entropy S of a Bose gas, one can start by calculating the specific heat at constant volume, (DU)

Cv = ar V.

(6.97)

where U is the energy and T is the temperature of the BEC. After obtaining Cv, the entropy can be calculated from the thermodynamic identity TdS = dU, (6.98)

so at constant volume: _ {T CvdT' S - lo T' · (6.99)

The energy U of the BEC can be obtained by taking the derivative of the log- arithm of the grand partition function Z [see Eqs. (6.82) - (6.93)] with respect to

f3 = 1/(kBT): 3 Solution

## COLD ATOMS

8lnZ u = - {){J .

The grand partition function for a Bose gas is given by Eq. (6.93)

from which we can calculate the energy of the BEC using Eq. (6.100): Subsequently, for the specific heat we have: (6.100)

(6.101)

(6.102)

When the gas is at or below the Bose condensation temperature Tc, A -+ 1 and the second term in Eq. (6.102) is zero since A is independent of temperature. To relate Cv to the number of atoms N, we recall that at T = Tc the total number of atoms 3 This relation can be proven in the following way. The logarithm of the grand partition function is and thus - 8 In z = - ~ 8 In Zi = - ~ _!_ 8zi .

8/3 ~ 8/3 ~ Zi 8/3 I I

BOSE-EINSTEIN CONDENSATION (T)

is given by Using this result in Eq. (6.102), we obtain: _ 15 Fs;2(l)

,. ( T ) 3/ Cv - 4 p.

(l) NkB ,,, 3/2 1c Thus from Eq. (6.99) we get the entropy of the BEC: _ {T CvdT' S - lo T' _ 15 Fs;2(l)

fr (T')312 - 4 F3;2(l) NkB lo Tc dT = ~Fs;2(l) NkB(T)3/2 2 F3;2(l)

Tc ' so that ( T )3/2 S = 1.283 · N Tc .

(6.103)

(6.104)

(6.105)

(6.106)

This entropy can be compared to that for a classical gas. The energy U of a classical gas can be obtained from Eqs. (6.101) and (6.95) (where we do not take the limit ,\ -+ 1 ): U = ~F 5; 2 (,\) (N*)k 8 T.

(6.107)

2 F3;2(,X)

In the classical limit, ,\ << 1, so F5; 2(,X) ~ F3; 2(,X) ~ ,\, and (N*) = N.

The ref ore we recover from ( 6.107) the familiar formula U = 2NkBT.

(6.108)

From (6.97) and (6.99) we find (6.109)

which leads to a very different dependence of entropy upon T and N than in the case of a Bose gas below Tc [Eq. (6.106); note that S depends implicitly on N through Tc in (6.106)).

## COLD ATOMS

6.S Bose-Einstein condensation from an optical lattice Consider bosonic atoms in a 3D optical lattice. An optical lattice is an ato~ :;aJ created by a standing light wave, or in the considered case, an intersect: ole several standing light waves. The atoms are confined to lattice sites by the 1~_?), force arising from the AC Stark shifts due to the optical electric field (~oble_m1 okS The potential of the optical lattice is spatially periodic; in two dimension~ it O ee, like an "egg crate" [see Fig. 6.6; for detailed discussions of optical latuces, :nd for example, Guidoni and Verkerk ( 1999), Metcalf and Van der Straten ( 1999), Rolston (1998)].

and Suppose that atoms in each site are cooled to the lowest vibrational state, .0 a that there is no more than one atom per site (if more than one atom ends up ~ ces site, there is a high probability that one of the atoms will get kicked out). Latt~·ng with occupation numbers K. (i.e., average number of atoms per site) approac unity have been realized experimentally (DePue et al. 1999).

ttice If"' = 1, and the lattice is adiabatically removed (i.e., the intensity of the 1~ ess light fields is gradually lowered; the condition of adiabaticity is a tricky buSlO a in this case, but never mind this for the present problem!), the atoms becomet·at · Poten zero-temperature Bose-Einstein condensate (BEC). In fact, as the latttce h·ch wells lower, the atomic wavefunctions delocalize and eventually overlap (at w point the atoms have essentially zero momentum spread).

FIG. 6.6 Periodic potential of a two-dimensional optical lattice.

BOSE-EINSTEIN CONDENSATION FROM AN OPTICAL LATTICE Now consider K < 1. What is the smallest occupation number Ko, which will result in formation of BEC? [This problem is discussed in more detail by Olshanii and Weiss (2002).]

Hint The idea for solution is the following. If K is slightly less than unity, a BEC will still form, but not all atoms will be in the condensate phase and the temperature will be finite. There will be a critical value of the occupation number Ko, where this temperature equals the critical temperature for BEC, Tc. For K < Ko, no condensate will be formed.

If a process is adiabatic, entropy is conserved. To find Ko: (a) calculate the entropy of a partially filled lattice, (b) calculate the entropy of a Bose gas at the critical temperature, then (c) match these to determine Ko.

Solution (a) Calculating entropy for a partially filled lattice is simple combinatorics. Sup- pose we have P >> 1 sites in the lattice, of which KP sites are occupied. The number of different configurations for such a lattice (i.e., the number of different arrangements of occupied vs. empty sites) is: 0= P!

.

(KP)!(P - KP)!

The entropy is given by ( P! )

S = kB • ln(O) = kB · ln (1,,P)!(P _ 1,,P)!

= kB[ln(P!) - ln((KP)!) - ln((P - KP)!]

~ kBP[(K - 1) · ln(l - K) - K · ln(K)] .

(6.110)

(6.111)

Here we have used Stirling's formula to approximate the logarithms of factorials (In P! ~ P In P - P). As expected, the entropy vanishes for "' -+ 0 and for "' --+ 1 (there is only a single possible configuration of the lattice in both these cases), while reaching a maximum at "' = 1 /2 (Fig. 6. 7).

(b) The entropy Sofa BEC is given by Eq. (6.106), where in our case N = KP: S = 1.283 · ,,,p(~)

(6.112)

The entropy scales linearly with the number of atoms, and, accordingly, with "' (Fig. 6.7).

## COLD ATOMS

1.0 0.9 0.8 0.7 0.6 0..

0 b 0.5 s::: 0.4 0.3 0.2 0.1 0.0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0. 7 0.8 0.9 1.0 K FIG. 6. 7 Entropy per lattice site (expressed in units of ks) as a function of the occupation number K for a free Bose gas and an optical lattice.

( c) The entropies of a free Bose gas at T = Tc and an optical lattice as a function of "-are shown in Fig. 6.7. The condition for a BEC to form is that the lattice entropy is less than the entropy of the Bose gas at T = Tc, which occurs for K, > "-0 ~ 0.538.

## 6.6 Cavity cooling

In this problem we analyze various aspects of a recently proposed method of cool- ing atoms, molecules, and ions via cavity-enhanced scattering [see the paper by Vuletic and Chu (2000) and references therein].

(a) Consider first a stationary atom located on the axis of a symmetric, two-mirror, standing-wave cavity at a certain longitudinal position near the cavity's waist. The cavity is excited with light that is near-resonant to one of the cavity modes (of frequency we)- The excitation light frequency (wL) is far-detuned from the nearest atomic resonance w0, and its intensity is sufficiently weak so that the optical tran- sition is not saturated. Estimate the change in the cavity's resonance frequency due to the presence of the atom. Explain how the shift depends on the location of the atom with respect to the nodes and antinodes of the standing light wave.

## CAVITY COOLING

(b) Using the result of part (a), show that if the laser frequency is tuned (by a fraction of the width, ,c, of the cavity resonance) to a frequency which is lower than a cavity resonance (wL < we), the power circulating in the cavity is maximal when the atom resides near a minimum of the mechanical potential experienced by the atom due to the interaction with the light field.

(c) Suppose now that We - WL ~ ,c, and that the atom is moving along the axis of the cavity with a velocity v ~ v*, where kv* ~ ,e, i.e., during the cavity relaxation time 1/,c, the atom moves by a sizable fraction of the wavelength. Estimate the average power taken away from the atom (the effect tending to slow the atom down) and the slowing force. Discuss what happens for v << v* and for v >> v*.

Hint In the present problem, we have one atom in the volume of the cavity mode. This volume can be calculated using the Gaussian beam formulae given, for example, in Siegman ( 1986). Assuming a TEM 00 mode, a symmetric cavity of length L, and the beam waist w0 (at the center of the cavity), we have: j L/2 Vmocte = 1rw 2 (z)dz, -L/2 (6.113)

where V mode is the mode volume; w2 ( z) = wi [ 1 + ( z / z n)2]

, z is the waist at a distance z from the center of the cavity; ZR = 1rw5/ .;\ is the Rayleigh range, and A is the wavelength of the light. Explicit calculation for a symmetric resonator [see Siegman ( 1986) Chapter 19] yields: (6.114)

The second term in this expression is much smaller than the first one for cavities whose length is no larger than twice the Rayleigh range (all cavity configurations from planar-planar to confocal satisfy this condition). We neglect the second term in Eq. (6.114) in the following.

Solution (a) In the absence of saturation, the effect of the atom is equivalent to filling the cavity with a medium which has an effective refractive index n (In - 11 << 1). The change of the cavity resonance frequency is (6.115)

## COLD ATOMS

The effective refractive index n can be related to the atomic polarizability o (Problem 2.1) as was done in Problem 4.2. Namely9 we say that [Eq. (4.15)]

n - 1 ~ 21rNo, (6.116)

where N is the number density of atoms in the medium. Under the conditions of the present problem, where the detuning lwo - w LI is much greater than the width of the atomic transition 70, we have for the polarizability [see Eq. (2.87) from Problem 2.7]: ( ) , 2/i WO -WL where d is the transition dipole moment. Thus the index of refraction is 1rd2N n-1~----. li(wo -wL)

(6.117)

(6.118)

In our case, we have one atom in the volume of the mode V moc1e ~ 1rwgL, so N = • (6.119)

1rw0L Using Eqs. (6.118) and (6.115) yields: (6.120)

In the above considerations, we have not yet included the fact that the light field in the cavity is a standing wave. In fact, an atom located at a node does not "see" any light field, and thus cannot possibly affect the cavity. On the other hand, near an antinode, the atom sees maximal field amplitude (twice that in each of the counter-propagating running waves comprising the standing wave in the cavity), and thus its induced dipole moment has the greatest effect on the field in the cavity.

In order to establish this relation quantitatively, we notice that, in general, the effect of the medium on the cavity field (absorption and phase shift) is proportional to the product of the induced dipole moment and the local amplitude of the light field and is thus quadratic in this amplitude. Thus, in order to include the dependence on the location of the atom in the cavity, instead of Eq. ( 6.120), we write: ~We= -We !L Ii( <fl ) 2sin 2 k(z + L/2), w0 wo-WL (6.121)

where k is the wave vector of the light, and z + L /2 is the distance from one of the mirrors. Equation ( 6.121) reduces to Eq. ( 6.120) upon averaging over the atom's position.

Note that if the input frequency is tuned above the atomic resonance (w > v.J )

h · L 0, t e presence of the atom m the cavity pulls the resonance frequency of the cavity

## CAVITY COOLING

tow~ds higher frequencies, i.e., reduces its effective length. On the other hand, if the mput frequency is tuned below the atomic resonance (wL < w0), the presence of the atom in the cavity pulls the resonance frequency of the cavity towards lower frequencies and increases its effective length.

(b) The mechanical potential cl> arises due to the AC Stark shift of the atomic ground state [see, for example, Problem 2. 7J: d2e2 <J,~----- 4/i(wL - wo)' Where d is the dipole moment of the atomic optical transition, and e = 2co · sin k(z + L/2)

(6.122)

(6.123)

~s the amplitUde of the electric field of the light at a location z in the cavity, and f.o tbe amplitUde of each of the counter-running waves forming the standing wave.

Suppose first that WL > WQ. According to the argument of part (a), the pres- ;11nce of t~e atom near a crest pushes the cavity resonance freq~ency t~w~s higher it equencies, i.e., away from w L· This reduces the light_powe~ c1rculatm~ m th~ cav- J\~· On ~he other hand, if an atom is near a node, the c1rculatmg power_1s maximal.

corchng to Eq. ( 6.122), a node in this case also corresponds to a mimmum of the ~echanical potential (because the light-induced energy shift is positive). Thus the circuJ · · · · h h . I ating power is maximal when the atom 1s at a mm1mum of t e mec anica Potential (J).

· If w L < wo, the presence of the atom in the vicinity of a crest of the Sland- 1ng w ti · · ave pushes the cavity resonance frequency towards lower requencies, i.e., toward .

· · · h .

Th .

I .

8 W£. This increases the light power c1rculatmg m t e cavity.

e c1rcu- ating power is thus maximal when the atom is located at a crest of the standing ::e.

!'ccording to Eq. (6.122), this correspo~ds _to a mi~imum of the mechanical . ntial (because the light-induced energy shift 1s negative). Thus, as before, the circulating power is maximal when the atom is at a minimum of the mechanical Potential (J).

~e) The atom moving along the axis of the cavity is constantly climbing and Th~en~i~g the peaks of the light-shift-induced m~hanical pote?tial cl> (Fig. 6.8).

~ngm of the slowing force can be understood m the followmg manner. If an atom is resting at a minimum of cl> then the circulating power and the height of the mech~nical potential are maximal '[as discussed in part (b)J; for an atom resting at ~ maximu~ of cl>, the height of the mechanical potential is minimal. Changes in fi e mechanical potential persist for a characteristic time 'Y;1, so as an atom travels rom a minimum of ~ to a maximum, the height of the potential is greater than for

## COLD ATOMS

e ~ \ ....

C: d) ....

0..

Po ition FIG. 6.8 Illustration of the cavity cooling effect for w L > wo [note that the technique works equally well for WL < wo as discussed in part (b)]. Atom moving with velocity v in the mechanical potential 4> created by the standing light wave in an optical cavity. When the atom is at a node of the optical electric field, it has no effect on the cavity, and the circulating light power (and hence amplitude of 4>) is maximal (solid line in the plot of 4>). When the atom is at an antinode, the index of refraction is modified in such a way as to move the cavity resonance frequency away from the light frequency, thereby reducing the circulating light power and decreasing the amplitude of the potential 4> (dashed line). The cavity response is delayed by a characteristic time ,..,; 1, so as the atom moves along the cavity axis it always climbs a higher potential .. hill"

than it descends. Hence energy is transferred from the atom to the electromagnetic field in the cavity, and the atom slows down.

when an atom is travelling from a maximum to a minimum of ell. The net result is that the atom always climbs a higher "hill" than it is descending; hence it slows down (Vuletic and Chu 2000).

To estimate the slowing force, we first estimate the change of the power in the cavity and the height of the mechanical potential due to the atom. The circulating power goes from its maximum value to essentially zero when the cavity is tuned by ~ 1 c from the laser frequency. When the laser is tuned to the slope of the cavity transmission peak, we have: (6.124)

CAVITY COOLING FOR MANY PARTICLES: STOCHASTIC COOLING Using Eqs. (6.121) and (6.122), one finds for the change in the height of the potential: (6.125)

The average power P taken away from the atom can be estimated as the change of the potential given by Eq. (6.125) divided by the characteristic time,; 1: (6.126)

Although this expression does not explicitly depend on ,e, there is, of course, an implicit dependence through e5.

The average slowing force F can be found by dividing the power by the velocity of the atom (or, more precisely, its component along the cavity axis). Thus, the circulating power is maximal when the atom is at a minimum of the mechanical potential ~- If v << v*, the slowing force is reduced by a factor oc v because the atom covers a correspondingly shorter distance during the cavity relaxation time 1 / 'Ye• For v >> v*, the force falls off oc 1 / v because the atom travels over many minima and maxima of the mechanical potential, and the effect averages out. The overall expression for the cooling force including these factors is thus: (6. I 27)

This estimate is in agreement, up to a numerical factor, with the results of Vuletic and Chu (2000).

6. 7 Cavity cooling for many particles: stochastic cooling Based on the results of the previous problem, analyze the cavity cooling process for the practically important case of K >> 1 particles simultaneously present in the cavity. 4 In particular, find the change in the r.m.s. velocity of the atoms during the time interval ,;

## 1. Assume that the initial atomic velocities satisfy lvl << v*

[Eq. (6.127)]. What is the optimal cooling rate for the sample?

4 This problem was inspired by discussions with M. Zolotorev.

Solution

## COLD ATOMS

From Newton's second law and the expression for the cooling force obtained in the previous problem for a single atom with lvl << v• [Eq. (6.127)], we can write: dt ~ -~"YcV.

(6.128)

where 2d2E5 Jl We {'Ye~ !i2(wL - wo)2 wiL M(v•)2, (6.129)

and M is the mass of the atom and { is a dimensionless factor.

If many atoms are present in the cavity, each of these atoms affects the field circulating in the cavity as discussed in the previous problem, and the resulting modification of the mechanical potential affects not only the atom that caused a perturbation, but other atoms as well. We can account for this in the following way. Suppose at a certain time, the velocity of the i-th atom is Vi. After a time interval 1; 1, we have: v: = Vi - {(vi+ L vj cos((h3)) .

j¢i (6.130)

Here the factor cos( (Jij) is introduced to take into account that the influence of the j-th atom on the cavity field can either accelerate or decelerate the i-th atom depending on the relative phase of the motion of the two atoms with respect to the standing light wave.

As the next step, we will calculate the square of v; and average over all atoms in the cavity. (We work with the square of the velocity because the average velocity is zero.) From Eq. (6.130), we write: (vD 2 = (vi)

- 2vi{ (vi+ L vj cos(Oij))

j¢i + { 2 [vr + (L vj cos(Oij))

+ 2vi L vj cos(Oij)] .

(6.131)

j¢i j~i Averaging over the ensemble gives (K >> 1): - - - { 2K- (v')2 = v2 - 2{v2 + -v2.

(6.132)

The second term on the right-hand side of Eq. (6.132) describes the single-atom cooling, while the third term corresponds to collective heating.

## FERMI ENERGY FOR A HARMONIC TRAP

The magnitude of~ is proportional to the intensity of light in the cavity. While for the single-atom case the cooling rate is linear with {, this is not so in the case of many atoms. In fact, from Eq. (6.132) we see that for { > 4/ K, there is net heating rather than cooling. The optimum cooling rate corresponds to ~opt = 2/ K.

Substituting this into Eq. (6.132) and recalling the definition of~' we find that: Optimal cooling rate = 2;c , which may present a limitation for cooling large ensembles.

(6.133)

Note that the above discussion is in direct analogy with stochastic cooling of charged particles in accelerators and in ion traps (Ghosh 1995; Beverini et al.

1988). In stochastic cooling, the average displacement of the particles is deter- mined by measuring the induced charge on an electrode. This signal is then amplified and fed with an appropriate phase onto another electrode that corrects for the average displacement. Here also the optimal cooling rate is limited by the number of particles. In the cavity cooling scheme, the feedback mechanism is not external as in the case of the usual stochastic cooling, but is contained in the dynamics of the atom-cavity interactions (Gangl and Ritsch 2000).

Recent experiments (Chan et al. 2003) have shown that in addition to the effects discussed above, cooling forces arising from collective emission into the cavity mode can play a crucial, even dominant, role for many atoms [K rv 106 in the work of Chan et al. (2003)]. Consideration of such effects is left as an exercise for the reader!

## 6.8 Fermi energy for a harmonic trap

In addition to the creation of degenerate Bose gases discussed in Problems 6.4 and 6.5, atomic trapping and cooling techniques can be used to create ultracold gases of fermions (DeMarco and Jin 1999). The behavior of a degenerate Fermi gas is markedly different from that of a degenerate Bose gas - instead of a large fraction of atoms condensing in the ground state of an atomic trap as occurs for bosons at very low temperatures, only a single Fermi atom can occupy a given quantum state. Many fascinating quantum statistical phenomena related to Fermi degener- acy can be studied under the controlled environment of an atomic trap, such as the modification of atomic collisions (DeMarco et al. 200 I), a phase transition at very low temperatures to a superfluid state of Cooper-paired atoms (O'Hara et al.

2002; Weiping et al. 1999), shell structure (Schneider and Wallis 1998; Bruun and Burnett 1998), etc.

In this problem we find the Fermi energy for such a gas of atoms contained in a harmonic trapping potential.

## COLD A10MS

.

i- . de · I half-integer sptn part (a) Show that the Fermi energy for N (N » 1~ t n~1ca ic three-dimensional cles (in the same spin state) of mass m trapped tn an 1sotrop harmonic potential 2 ( 2 2)

V(x,y,z)

= 2mw x +Y + z (6.134)

is given by: Ep ~ h.w(6N) 113 .

(6.t35)

Assume EF ~ liw.

4offz.

(b) Estimate the Fermi temperature for N = lcf' atoms and w = 21r x (c) What is the Fermi energy for an anisotropic trap with Assume E F >> '1w, aliw.

Solution ·ck same (a) Let us measure the atoms' energies E in units of h.w. Suppose we pt ro-p0int integer value E » 1. (Here we set the zero of energy equal to the ~ itb high energy. This is a good approximation because we are concerned mostl~ w tions of .

.

.

N .

.

d.ffi t comb1na rf"h·s exc1tat1ons since ~ 1.) The question is: how many , eren C'? 1••' I to &1 • quantum numbers nz, nv, n.z are there that give the total energy equa tells us how many fermionic atoms can occupy a state with e~e~Y E · UcitlY= To answer this question, we can just count possible combinations exp nx ny nz number of states E I E-1 E-1 E-2 E-2 E-2 .

.

.

. .

.

.

.

.

.

.

.

## FERMI ENERGY FOR A HARMONIC TRAP

We see that the number of combinations giving the total energy equal to E is ~- E+2 E 2 n(E) = L.)i + 1) = --(E+ 1) ~ - .

i=O (6.137)

T~ find the Fenni energy, we sum up the number of possible states for all energies E < Ep [using Eq. (1.26)): n(E S Ep) = ~ n(E) ~ ! ~ E 2 = ! . Ep(l + Ep)(l + 2Ep) ~ E} L 2L E::1 E=l (6.138)

and set it equal to N. This gives the desired result (6.135).

(b) The Fenni temperature is given by Tp = Ep = !!:_w(6N) 113 • (6.139)

kB kB The fa t · I · .

A c or Ii/kB can be expressed in the following manner usmg re at1ons m PJ>endix A: r-== ~ ~ (200 eV · nm)(ll, 600 K/eV) = 8 x 10-12 K. 8 , (6.140)

B kBc 3 x 1017 nm/s giving us I Tp~400nK., (6.141)

:n th~ experiment of DeMarco and Jin (1999), in order to reach Tp, laser cooling CChniques, sympathetic cooling with a bosonic species, and evaporative cooling rnethOd 8 Were employed.

~N· .

~ oting that for the energy of excitation along x we have ahwnx mstead of n:t, and we can repeat the calculation of part (a): I Ep = hw(6Na) 113 • , (6.142)

## MOLECULES

## 7.1 Amplitude of molecular vibrations

Estimate the root-mean-square (r.m.s.) value of <5T = T - Te, where Tis the inter- nuclear separation, and Te is its equilibrium value, for a diatomic molecule in a low vibrational state.

Hint The equilibrium separation between nuclei in a typical diatomic molecule is on the order of several Bohr radii, re rv 4a0 , and the dissociation energy Do is on the order of R00 1 e2 Do rv he-- rv -- 10 ao ' (7.1)

where R 00 is the Rydberg constant. 1 To estimate the r.m.s. value of 6r, suppose that when 6r ~ a0, then the potential energy is zero. In other words, the dissoci- ation limit is reached when the bond is stretched by an amount comparable to its length. These observations are sufficient for performing the estimate required in this problem.

Solution Using a model of a molecule as two masses connected by a "spring," we can estimate the spring constant k from a5 R00 k- rv hc- (7.2)

1 The dissociation energy is designated to be the energy difference between the ground state of the molecule and the beginning of the continuum (minimum energy of unbound atoms). This is the work that must be done to dissociate a molecule initially in the ground state.

as

## MOLECULES

k ~ 2hclloo ~ .i:._ 3 .

(7.3)

5a0 5a0 From this, we obtain the well-known estimate for the frequency of molecuJar vibrations: (7.4)

where m is the mass of the electron and µ is the reduced mass of the two atoms.

If a molecule is in a low vibrational state, the energy of the vibration is "-' hw .b "1 • On the other hand, this energy can also be estimated as rv k( <Sr )2. Combining these two estimates, we get: (<Sr) rv -ao - 5 2~ µ (7.5)

or ( ) 1/4 ~r ~ ao : , (7.6)

which is rv O. lao for µ rv 5 a.u.

Note that essentially the same estimate applies to atomic vibrations in a crys- talline lattice for solids at low temperatures (kBT << hw). A similar approach can be applied to estimate r.m.s. vibration amplitudes (for both molecules and solids)

at higher temperatures.

7 .2 Vibrational constants for the Morse potential The interatomic potential for a diatomic molecule is often parameterized using the Morse potential (7.7)

shown schematically in Fig. 7. I. Here re is the equilibrium internuclear separation, and De and {3 are the parameters specifying the potential for a given system. 2 2 Note the difference between the dissociation energy Do introduced in Problem 7. I and De intro- duced here. The constant De, as can be seen in Fig. 7.1, is the energy difference between the bottom of the potential well and the continuum, while Do is the energy difference between the molecular ground state and the continuum. Thus they differ approximately by the zero-point energy: We De -Do~ 2 .

VIBRATIONAL CONSTANTS FOR THE MORSE POTENTIAL - ~ 01.> L..

~ C UJ -a ·.= C Q)

~ &.

Internuclear Separation (re)

FIG. 7.1 The Morse potential with f3 = 1. Internuclear separation is expressed • .

.

.

.

m umts of us equilibrium value re; energy is expressed m umts of dissociation energy De.

Express the vibrational constants of~ diatomic molecule we and WeXe in tenns of the parameters of the Morse potential and the reduced mass µ.. where th energies of the vibrational levels are given by (Herzberg 1989): e G(v) = We(v + ~) - WeXe (v + D + ... , (7.8)

where v = O, 1, 2, ... is the vibrational quantum number, the we term describes the equidistant levels of a harmonic oscillator, and the We Xe term accounts for anhannonicity. 3,4 Hint To find the anharmonicity, use the fact that the separation between adjacent vibra- tional levels approaches zero as the vibrational energy approaches the dissociation energy De.

Solution Expanding the Morse potential (Eq. 7.7) around r = re, one obtains V(r) ~ De{P(r - re) 2 , (7.9)

which is the harmonic potential. It is well-known that the frequency of the quantum mechanical harmonic oscillator We is the same as the frequency of the classical 3 In tables of molecular constants the quantities We and WeXe are measured in units of energy, often given in wavenumbers (cm- 1 ). See Appendix A for conversion factors between various units.

Here we set ft= 1, so frequency and energy units are the same.

4 While Eq. (7 .8) represents a general expansion for an anhannonic oscillator, it turns out that no higher order terms actually appear in an exact solution for the case of the Morse potential (see, for example, Herzberg ( 1989), Chapter III].

## MOLECULES

oscillator given by Jk]µ, where k is the "spring constant" which is found from k(r - re)2 _ D (32( _ ) 2 --2-- - e r Te (7.10)

to be k = 2Def32, yielding -{3MDe We - • µ (7 .11)

In order to find WeXe, we notice that, as seen from Eq. (7.8), the separation between adjacent vibrational levels decreases linearly with v: ~G(v) = G(v + 1) - G(v) = We - 2wexe(v + 1).

(7.12)

As pointed out in the hint, the distance between adjacent vibrational levels approaches zero as their energy approaches De. We can use this to relate the anhar- monicity We Xe to the parameters of the Morse potential. We note that the maximum value of the vibrational quantum number found by setting ~G(vmax) = 0 is (7.13)

The energy of the corresponding state is found by adding successive energy separations of Eq. (7.12): (7.14)

Setting this energy equal to De, we obtain: (7.15)

7 .3 Centrifugal distortion If a diatomic molecule is rotating, the resulting centrifugal force tends to pull the nuclei apart (this effect is known as centrifugal distortion). Estimate how the equilibrium internuclear separation changes as a function of the rotational quantum number a for low-lying vibrational states.

## CENTRIFUGAL DISTORTION

Show that this change in separation leads to a new term in the molecular energy of the form ~E = -Da2(a + 1)2 , (7.16)

where D = 4B~ (7.17)

.

We Here fi 2 (7.18)

B-- e - 2µr; is the rotational constant and We is the vibrational constant.

Solution In Problem 7 .2, we considered the interatomic potential V ( r) due to the charge distribution but did not account for energy due to rotational motion, Vn(r ). Clas- sically, the rotational energy Vn is given by the square of the angular momentum £ divided by twice the moment of inertia I0: Vn = 210 .

(7. I 9)

For a diatomic molecule the moment of inertia is Io = µr 2, where µ is the reduced mass, and the quantum mechanical expression for the square of the angular momentum is£}= n2a(a + 1), so we have n,2 Vn(r) = -2 2a(a + 1) .

µr (7.20)

One can include this rotational energy in an effective potential Veff( r) = V(r) + VR(r). For low-lying vibrational levels, we can expand the potential about the minimum of the effective potential r0 [just as we did for V ( r) in Problem 7 .2 to obtain Eq. (7.9)]: (7.21)

Thus, as before, we can model a diatomic molecule as two nuclei attached by a spring with constant k. To first order, the rotational motion affects ro, but not the spring constant k.

## MOLECULES

To find the dependence of the equilibrium separation To on a, we take the derivative of Vetr( T) and evaluate it at T = Te: (7.22)

Noting that for the interatomic potential V ( T)

dVI -0 dT r,: - ' (7.23)

we are able to use Eq. (7 .22) solve for To: n2 a(a + 1)

ro =Te+ -k • µ re (7.24)

Thus we see that indeed the centrifugal force tends to stretch the molecule. We can identify the spring constant with the vibrational constant We ( expressed in energy units) via the relation k = Ju..,/;/li 2 [see Eq. (7.8)), in which case we obtain (7.25)

If one neglects the centrifugal distortion, the rotational energy ER of a diatomic molecule is given by (7.26)

Including the centrifugal distortion, we replace Te with To in Eq. (7.26). Taylor expanding to first order gives (7.27)

Thus we indeed find that the centrifugal distortion changes the molecular energy by an amount (7.28)

where the constant D is given by Eq. (7 .17).

7.4 RELATIVE DENSITIES OF ATOMS AND MOLECULES IN A V

## APOR

Relative densities of atoms and molecules in a vapor In this problem we address a common issue in spectroscopy: the rel f .

.

.

Tb .

. h ed a ive abundance of vanous spe~1es m eqm I numd w_it a sh~tuhrat vapor. For example. in different types of expenments one may es1re a 1g er abundance of diatom· .

.

.

.

1c mo ecules as compared to their atomic const1tu~nts. or v1_ce versa. This problem relates this relative abundance to the spectroscopic properties of the molecular spe .

~ h c1es, 1or t e specific case of cesium (Cs).

(a) Consider a closed cell containing _a saturate~ vapor of Cs in equilibrium at temperature T. Suppose that the vapor 1s predominantly in the atomic fonn.

Calculate the relative abundance of Cs2. as a function of the following param- eters: T, the t~m_perature; .Pc-., the vapor pressure of the atomic Cs component; De, the dissociation energy of the molecular ground state (see Fig. 7. I); we. the vibrational constant of the ground state; Be. the rotational constant of the ground state; and I, the nuclear spin of the Cs atom.

Assume that the hyperfine structure of both atoms and molecules is negligible compared to k8 T. although the degeneracies induced by the nonzero nuclear spin must be taken into account. Note that the ground state of Cs is s112• and the ground state of Cs2 is 1 ~f (for a review of spectroscopic notation in atoms and molecules see Appendix C). 5 Assume that the rotational structure of Cs2 is that of a simple rigid rotor; that its vibrational structure is that of a harmonic oscillator; and that electronically excited levels of both the atom and the molecule have energies Ee>> kBT.

(b) Simplify the answer in the case We << kBT and Be << k8 T.

(c) Use the following data to numerically estimate the relative abundance of Cs2 in a sealed vapor cell, at room temperature and at T = 300°C: De ~ 0.45 eV; We ~ 42 cm- 1; Be~ 0.012 cm- 1; I= 7 /2; log10(P) = -T -1.4log 10(T) + 11.176 (7.29)

with Pin torr and Tin K. [Spectroscopic data are taken from Radzig and Smimov ( 1985); vapor pressure data are from Honig and Kramer ( 1969).]

5 Among the most abundant diatomic molecules, most have ground state spatial wavefunctions that are completely symmetrical with zero total spin, i.e., 1 E+, or, for a dimer, Et. Notable excep- tions are molecules such as 02 <3E;) and NO (2Il), which are known as free radicals because they are chemically unstable (though physicalJy stable) due to the fact that they have one or more unpaired electrons (hence nonzero spin S); see Herzberg ( 1971 ).

Solution

## MOLECULES

(a) We wish to find t~e equilibrium state of the reaction 2~s +-+ Cs2. A~c~rding to the law of mass action [see, for example, the book by Reif ( 1965)], equ1hbriurn occurs when (7.30)

where Ni is the number of particles of species i, and Zi is the single-panicle partition function of species i: z = L e-E(s)/(k11T)

.

s (7.3 I)

Here s enumerates all internal and external quantum states of the particle, and E( s) is the energy of state s. The partition function z is essentially a count of the number of states available to the particle, taking into account the weighting due to the Boltzmann factor.

Each degree of freedom for the system can be factored into a separate sum; in particular, if the degrees of freedom corresponding to the center of mass motion are factored out, Zi can be written as Zi = : 3 J d3r J e-p 2/(2m,k11T)d3p L e-E(s)/(k 11T)

s(int)

= :a (21rmikBT)3/2 L e-E(s)/(k11T)' s(int)

(7.32)

(7.33)

where mi is the mass of species i, and the sum is now over only the internal states of the particle.

Now we tum to enumerating the internal states of the species of interest. For the atoms, this is very simple. By assumption, the hyperfine structure is small compared to the thermal energy; thus, the available internal states of the atom are all effectively degenerate, and they can be numbered by counting the electronic and nuclear spin states. Taking the atomic ground state energy as E = 0, the sum over internal states in Eq. (7.33) is then just: L e-E(s)/(knT)

~ (2J + 1)(21 + 1) = 4/ + 2, s(int,Cs)

where we have used J = l/2 explicitly.

(7.34)

To calculate the partition function of the molecule, we must enumerate states of the internal rotational and vibrational structure. We use the standard f ormu- lae for rotational energy [E(8) = Be8(8 + 1), see Problem 7.3) and vibrational energy [E(v) = We (v + ½), see Problem 7.1), where a and v are the rotational and vibrational quantum numbers, respectively.

RELATIVE DENSITIES OF ATOMS AND MOLECULES IN A VAPOR To correctly count the molecular states, we must take into account the degener- acy due to nuclear spins. The overall molecular wavefunction must be symmetric with respect to the exchange of the Cs atoms, since Cs atoms are bosons. Since the ground state of Cs2 is a singlet state with respect to electron spin, the total diatomic electron-spin wavefunction is antisymmetric. Since the ground state of Cs2 is a gerade state, the symmetry of rotational levels is given by ( -1 )0. Thus, for odd rotational states (with a = 1, 3, ... ), the total nuclear spin wavefunction must be symmetric, i.e. / 101 = 2/, 2/ - 2, .... Conversely, for even rotational states, the total nuclear spin wavefunction must be antisymmetric. Let us explicitly count the states for the case I = half-integer, 0 odd. The nuclear spin degeneracy 9R of the rotational state with quantum number o is 2/ gn(a odd)= L (21101 + 1).

(7.35)

ltor=l,3, ...

There are I+ 1/2 terms in this sum; introducing the index k = (lto1 + 1)/2, we can write l+l/2 /+1/2 /+1/2 9n(aodd)= L (4k-1)= L 4k- L 1 k=l k=l k=l = 4 (I+ 1/2)(/ + 3/2) - (/ + 1/2) = (/ + 1)(2/ + 1).

(7.36)

Similarly, 9R(o even) = /(2/ + 1).

Finally, note that all bound states of the molecule have a common overall neg- ative energy shift with respect to the atomic states, equal in magnitude to De (see also Problem 7. I). We thus find that ~ e-E(s)/(k,,T)

= F(T· D B w )

~ - , e, e, e s(int,Cs2)

= exp (k~~)

(t.e-[(v+l/2)w,]/(k,,T)) (2/ + 1)

x (1 L (2a+ l)e-"·t;;i,+I) + (I+ 1) L (2a+ l)e_"•:;;'-,rn) ~ 3 even a odd (7.37)

## MOLECULES

from which we obtain ~ ~ e2ku'I' F(T; De, Be,We) = e"n,,.

-~ (21 + I)

I - e ",,,,.

x ((f (28 + l)e- "·:;;1,: ' + f (48' + 3)e - "·< 2;'':,:!,~2:1'+:i>)

.

8=0 8'=0 (7.38)

Thus, using Eqs. (7.33), (7.34), and (7.38), the law of mass action, Eq. (7.30), can be written as where we have written m = mes = mcs 2 /2. The fractional abundance of Cs2 is then Ncs 2 _ h3 ( k T)-3/2 F(T; De, Be,we)

N.

- nc, 1rm B (41 2)2 ' ~ + (7.40)

where ncs = ~~s/V is the atomic Cs density.

(b) We wish to find an approximate expression for F(T; De, Be, we)- In the limiting case We << kBT, ~ e 2k IJ'I' (7.41)

Now consider the expression E (2a + 1 )e-Bc8(8+I)/(kuT).

In the limiting 8=0 case Be << kBT, this can be approximated by the integral: (7.42)

= 2eµf4 j ye-µy2 dy (7.43)

kBT ~-=-- µ Be ' (7.44)

RELATIVE DENSITIES OF ATOMS AND MOLECULES IN A VAPO R where we definedµ= Be/(kBT), and made the change of variable _ S. ·1 I y - X + 1/2.

1m1 ar y, 00 L (4a' + 3) exp [-Be(2a' + 1)(2a' + 3)/(kBT)]

~ ! kBT 3'=0 2 Be .

(7.45)

Thus F(T; De, Be,we) ~ e,,',:·:,.

(kBT)

(2/ + 1) (1k 8 T + ! kBT)

We Be 2 Be ~ knT kBT (2/ + 1)2 = ek11I -------- (7.46)

We Be · and the fractional abundance of Cs2 is: (7.47)

It is instructive to note the origin of each of the terms on the right-hand side of Eq. (7.47). The first two factors ( ex ncs/T312 ) correspond to the ratio of phase- space volumes available for one molecule vs. two atoms. The exponential factor is the Boltzmann weighting appropriate for the binding energy of the molecule. The final two factors account for the number of vibrational and rotational sub levels populated at temperature T.

Note that the degeneracy due to the nuclear spin I is absent from this final expression. This can be understood by noting that - ignoring momentarily the com- plications due to exchange symmetry - the number of nuclear spin states available in each state of the molecule is just the square of the number available in each atom. Correctly taking into account the states forbidden by exchange symmetry can only modify this conclusion by a factor of order unity.

(c) To find a numerical value for the fractional dimer abundance, it is critical to choose a consistent system of units. Here we use CGS units, as usual throughout the book. We use the formulae from Appendix A to convert units. In particular, note that E[CGS] =he· E[cm- 1] , and E[CGS] = 1.6 x 10- 12 E[eV] .

We also use the ideal gas law: (7.48)

(7.49)

(7.50)

## MOLECULES

and the pressure conversion P[CGS] ~ 1.33 x 103 P[torr].

For T = 300°C ~ 573 K, from Eq. (7.29) we find: P(T) ~ 1.8 torr~

## 2.4 x 103(CGS] ;

k8 T ~ 7.9 x 10- 14 erg; De~ 7.2 x 10- 13 erg; We ~ 8.4 x 10- 15 erg; Be~ 2.4 x 10- 18 erg; m ~ 133mp ~ 2.2 x 10- 22 g .

(7.5 I)

These values make it clear that under these conditions, the approximations of Part (b) hold well. This finally yields (7.52)

At room temperature (T = 22°C), we find (7.53)

The difference in molecular abundance between these two temperatures is strongly affected by the difference in atomic Cs pressure; at room temperature this is only P ~ 1 x 10- 6 torr, six orders of magnitude less than at T = 300°C.

7 .5 Isotope shifts in molecular transitions Much as in atomic spectra (see Problem 1.9), shifts occur in lines of molecu- lar spectra due to the difference in mass and nuclear volume between different isotopes.

(a) Consider an energy level of the diatomic molecule AB, characterized by the quantum numbers 8 (rotation) and v (vibration), in a particular electronic state (labelled as Y). Determine the effect of substituting isotopic species B' for the original isotope B on the energy of this state. Show how the electronic energy Te(Y), the vibrational constant we(Y), and the rotational constant Be(Y) are

ISOfOPE SHIFTS IN MOLECULAR TRANSITIONS altered due to the change in nuclear mass. (For this problem we igno f'& .

' re e 1ects due to the change m nuclear volume.) Assume that the fractional chang • .

.

e m nuclear mass 1s small, 1.e., Llm = m,a, - m.a << m.a, where m. denotes F I h A .

h d .

mass.

or concreteness, assume a so t at 1s t e ommant mass of the mol .

ecu e, 1.e., fflB << m.A.

(b) Argue that, qualitatively, shifts in vibrational structure are the dominant iso- topic effect in molecular spectra. Show that these shifts can be substantially 1 I. .

h d."

arger than typical rotational sp 1ttmgs, so t at 111erent isotopic species can exhibit separated vibronic (=vibrational+ electronic) bandheads. 6 (c) The A( v' = 21) <-+ X ( v" = 0) transition ofICI has been studied extensively by laser spectroscopy [G. Bazalgette et al. ( 1999), and references therein]. Estimate the isotopic shift in the band head of this transition, upon substitution of 37 Cl for 35CI. Ignore hyperfine structure. Compare this shift to the typical rotational and vibrational splittings in this transition. You may use the following approximate data for ICI [Radzig and Smimov (1985)]: TABLE 7.1 Electronic state energies and rotational and vibrational constants for 135c1 (in cm- 1 ).

State 13742 212 0.084 0 384 0.114 Note that we have used the usual molecular notation, in which the ground elec- tronic state of the molecule is labelled as X, and higher-lying states are labelled with other letters such as A.

Hint In part (b ), use dimensional analysis to estimate the relative size of electronic, vibrational, and rotational splittings; from these, estimate the size of the isotopic shifts.

6 The term bandhead refers to the typical clustering of spectral lines in molecular electronic spec- tra, for any given vibronic transition. [See, for example, Herzberg ( 1989) for further discussion.] The bandhead usually occurs near the lowest rotational lines, i.e., near the energy difference between the 8' = 0 and 8" = 0 levels of the upper and lower vibronic states, respectively.

Solution

## MOLECULES

(a) The electronic energy Te depends on the isotopic mass through the reduced mass of the electron, µe: _ me(mA + mB)

( me )

µe - ______ ..:.._ ~ rne 1 - ---- .

me+ (mA + mB)

mA + mB (7.54)

(Note that we have assumed that the electron orbits both nuclei; this should be 8 reasonable approximation for an electron in a valence orbital.) Thus, the ratio of reduced electron masses for the two isotopic species is: , (1 me )

µe - mA+mn me ~m -~-----~~1+--- µe (1 _ ms; )

ffiA ffiA · mA+mu (7.55)

The Rydberg constant Roo is proportional to the electron mass. Thus, the electronic energy for the new isotopic species is (7.56)

To first order, the rotational and vibrational structure are shifted because the reduced mass of the molecular motion is altered with the change of nuclear mass. (There are also higher-order corrections to the rovibrational structure, e.g., those due to shifts in the electronic wavefunctions associated with the isotopic substitution; we ignore these here.)

The reduced mass of the molecular motion is: ffiAffiB µM = + ' ffiA ffiB (7.57)

where mA(B) is the mass of nucleus A(B). 7 Thus, the ratio of reduced masses for the two isotopic species is: µAf ffiB 1 ffiA + ffiB -=-- (7.58)

µM ffiB fflA + ffiB In the approximations ~m = m 8 , - mB << mB and mB << mA, this ratio can be simplified to read (7.59)

in addition, µM ~ µAf ~ mB.

7 Note that, strictly speaking, we should use instead the mass of atom A, i.e., the mass of nucleus A plus the mass of z electrons, where Z is the nuclear charge of species A. Under mo5l circumstances the mass of the electrons can be neglected in this calculation, and we do so here.

ISOfOPE SHIFTS IN MOLECULAR TRANSITIONS The vibrational frequency is detenninecl by the effective molecular spring con- stant k, such that We = J k / µ M (Problem 7. I). Thus, the vibrational constant for the new isotopic species is (7.60)

The rotational constant is determined by the moment of inertia of the molecule, I, such that Be = li2 /(2/). I is detenninecl by the internuclear spacing re and the molecular reduced mass: I = µMr;.

Thus, the rotational constant for the new isotopic species is (7.61)

(b) As suggested, we begin by estimating the relative size of electronic, vibra- tional, and rotational splittings in a molecule. Of course, we expect on dimensional grounds that the electronic energy is Te rv R 00 rv e2 /a0 • For the vibrational energy, consider the effective molecular spring constant k. Since this must be determined by electric forces, on dimensional grounds we expect k rv e2 / a~. Thus the ratio of vibrational to electronic energies is: (7.62)

For the rotational energy, note that the internuclear spacing is re rv ao, so that the moment of inertia is I rv µMai and the rotational constant is (7.63)

Thus the ratio of rotational to electronic energies is: Be !i2 ao li2 me - rv --- rv ---- rv - Te aiµM e2 aoe2 mB mB · (7.64)

Note that since me/m 8 << 1 for any nucleus B, we recover the well-known energy hierarchy: Be<< hwe << Te.

## MOLECULES

Now we can parameterize the isotopic shifts AEi due to each type of ltlotion.

For the electronic energy, we find (7.65)

For the vibrational energy, (7.66)

and for the rotational energy, ~m ~m me ~E-(rot.) = (Be - Be)= -Be""

--Te.

fiB fiBfiB (7.67)

Thus the isotopic shifts are in the ratio (7.68)

and we see that indeed I AEi(vib.) » AEi(rot.) » AEi(el.). , (7.69)

To compare the vibrational isotope shifts to the rotational energy, we write ~m fii':y: ~Ei(vib.)"' ffiBV mu e"' ~m~B Be mm,. Te fiB me .

II (7.70)

Using "typical" values like mB "' 20mp, ~m ~ 2mp, and noting that mp/me ~ 2000, we see that AEi(vib.) ~ Am {rjii ~ ~J20. 2000 ~ 20 » 1.

Be fiB V ffle (7.71)

Thus, the vibrational isotopic shift can indeed be large compared to the rotational splittings. The effect is particularly pronounced for high vibrational levels, with quantum number v >> 1, as the isotope shift is ~ 2v + 1 times larger than for the ground vibrational state.

ELECTRIC DIPOLE MOMENTS OF POLAR MOLECULES (c) We use Eq. (7.60), with ~m/rnB ~ 2/35, to find the shift in the vibrational constants ~we[X] = w~ - We~ -11 cm- 1 (7.72)

and (7.73)

Thus the shift in the frequency of the bandhead of the A(v' = 21) ~ X(v" = 0)

transition is 16.v ~ (21.5)(6) - (0.5)(11) ~ 123.5 cm- 1 . , (7.74)

Note that this shift is much larger than a typical rotational splitting ( rv 0.1 cm- 1)

and is actually comparable to the typical vibrational splitting in the A state!

## 7.6 Electric dipole moments of polar molecules

Consider a simplified model of a diatomic polar molecule, consisting of a rigid rotor [moment of inertia /, rotational constant Be = 1i2 /(2/)] with a permanent electric dipole moment J along the axis of the rotor. (We assume in this problem that the rotor has no internal structure.) The eigenstates of such a rotor are the states with definite values of the angular momentum a and its z-projection, m. In the center of mass frame of the rotor, the wavefunction of the state with quantum numbers (8, m) is simply the spherical harmonic: 'l/Ja,m(8, ¢) = Y;1 (8, ¢).

(a) Show that in any eigenstate, the expectation value of the electric dipole moment is (d) = 0.

(b) Suppose a weak electric field £ = £z is applied. Use perturbation theory to find the lowest-order energy shifts and the perturbed wavefunctions of the state with (nominal) quantum numbers 8 (where 8 is arbitrary) and m = 0. What is the condition under which £ may be considered weak?

(c) Show that (d) ;/ 0 for the perturbed states. Discuss the relative sign of (d) in the 18,m) = IO,O) and 11,0) states.

Solution (a) The dipole moment operator can be written as d = d[sin () cos </Jx + sin() sin <PY + cos() z].

(7.75)

## MOLECULES

Now we can parameterize the isotopic shifts tiEi due to each type of rootion, For the electronic energy, we find )

I me am me am fflB .

aEi(el.) = (Te - Te)= ---Te~ --- (- Te, mA mA fflB ffiB mA (7.65)

For the vibrational energy, (7.66)

and for the rotational energy, ( , am am me (7 67)

aEi rot.)= (Be - Be)= -Be"' --Te.

.

fflB fflB fflB Thus the isotopic shifts are in the ratio and we see that indeed \ tiEi(vib.) » tiEi(rot.) » tiEi(el.). \ (7.69)

To compare the vibrational isotope shifts to the rotational energy, we write (7.10)

I ~ Using "typical" values like m 8 ~ 20mp, tim ~ 2mp, and noting that mp me 2000, we see that ~Ei(vib.)

am~B --- "' - - "'-✓20-2000"' 20 ~ 1.

Be fflB me (7.70 Thus, the vibrational isotopic shift can indeed be large compared to the rotatio~:~ splittings. The effect is particularly pronounced for high vibrational levelS, w:he quantum number v » 1, as the isotope shift is i:::: 2v + 1 times larger thall for ground vibrational state.

ELECTRIC DIPOLE MOMENTS OF POLAR MOLECULES (c) We use F.q. (7.60), with ~ ~ . .

.

· constants m/mB ,..,_, 2/35, to find the shift m the v1brationaJ and Awe[X] = w~ - We~ -11 cm- 1 (7.72)

T ~we[AJ ~ -6 cm- 1 .

(7.73)

hus the sh"fi .

transition is I t ID the frequency of the bandhead of the A ( v' = 21) +-+ X ( v" = o)

Av~ (21.5)(6) - (0.5)(11) ~ 123.5 cm- 1 .

(7.74)

Note that th.

. .

.

.

. .

and is is shift 1s much larger than a typical rotat1onaJ sphttmg ( ~ 0.1 cm - 1)

actually comparable to the typicaJ vibrational splitting in the A state!

## 7.6 El ectric dipole moments of polar molecules

Con· sider a sim 1·fi d . .

f . .d rotor [ P I e model of a diatomic polar molecule, cons1st1ng o a ng1 elect . m~ment of inertia/, rotational constant Be = li2 /(21)] with a permanent nc d1poJ ....

.

.

bl that th e moment d along the axis of the rotor. (We assume 1n this pro em Slates e _rotor has no internal structure.) The eigenstates of such a rotor are the the ce WJth definite values of the angular momentum a and its Z-projection, m. In null).;ter of mass frame of the rotor, the wavefunction of the state with quantum (a) Sh rs (a,~) is simply the spherical harmonic: 'l/Ja,m(O, </>) = Y;r(o, </>).

is (d} :w;hat ID any eigenstate, the expectation value of the electric dipole moment (b) Su ..

find ttfse a weak electric field e = ez is applied. Use perturbation theory to With ( e ~West-order energy shifts and the perturbed wavefunctions of the state conditommal) quantum numbers a (where a is arbitrary) and m = 0. What is the •on Under which e may be considered weak?

(c) Show th it the la, rn) _at (di =I= 0 for the perturbed states. Discuss the relative sign of (d) in - IO, 0) and I 1, 0) states.

Solution (a) The dipole moment operator can be written as d = d[sin e cos </>i: +sine sin </>ii+ cos OZJ.

(7.75)

## MOLECULES

We use the standard definition of the spherical hannonics: {23 + 1) (a - ·m)! nm( fJ) im</J (a )' ra cos e ' 41r + m .

(7.76)

where P8 are the associated Legendre functions. The expectation value of dz in the state (a, m) is thus +1 (dz)= j jYt(O, <P)l2 cos(O)df2 ex/ IP8(x)l 2 xdx, (7.77)

This integral vanishes. since IP8(x)j 2 is an even function of x (and xis an odd function).

The expectation value of dx is 21r (dx) = j IYf(O, <P)l 2 sin(O) cos(<P)df2 ex/ cos(<P)d<P = 0.

(7.78)

Similarly, (dy) = 0.

Even without explicitly evaluating these integrals, the vanishing of (d) must be expected on symmetry grounds. Since the energy eigenstates of the rigid rotor are also eigenstates of parity (P) [with eigenvalue ( -1 )a], the expectation value of any P-odd operator such as J must vanish. Moreover, a nonzero value of (d) would also violate time-reversal invariance (T). The only spatial direction associated with an eigenstate is (8), so that (d) ex (8). However, (d) is even under T, while (8) is odd under T. Thus, if (d) # 0, T invariance would be violated.

The topic of possible P- and T-violating electric dipole moments in discussed in Problem 4.8.

(b) The perturbing Hamiltonian due to the electric field is I - - H = -d · e = -dze = -de cos fJ .

(7.79)

The first-order energy shifts due to H'. Eg!m)

= (H')ca.m)• vanish according to the result of part (a). To calculate the perturbed wavefunctions and second-order energy shifts of the states 18, m = 0), we must calculate the off-diagonal matrix elements of H': (8', m' I H' 18, o) = -de j Y8r:i'• ( e, <P) cos e Yf ( e, <P )dn .

(7.80)

ELECTRIC DIPOLE MOMENTS OF POLAR MOLECULES We simplify the integral by using the Wigner-Eckart theorem, and recognizing that cos 8 is an operator of rank "" = 1, with projection q = 0 (see Appendix F). Thus (8',m'I H' Ja,O) = -de (8~;;,s: 1!8) (8,0, 1,018',m') cdm', oc5a,.

a±i. (7.81)

(See Problem 9.5 for a discussion of why the matrix element vanishes for 8' = 8 and m' = m = 0.)

We can explicitly calculate the matrix element in Eq. (7.80) for the case m.' = m = 0: +l de J (8', 0I H' 18, 0) = -2 J{28' + 1)(28 + 1)

Pa,(x)xPa(x)dx - (7.82)

The integral over Legendre polynomials (Pa(x) = Pj(x)) can be evaluated using standard recursion formulae; Jackson ( 1975) shows that +l J P ( ) P ( )d 2(8 + 1)

(a' =a+ 1); 3' X X a X X = (28 + 1 ){28 + 3)

(7.83)

- (a' - a - 1)

(28 - 1 )(28 + 1)

- .

Thus (8',ol H' 18,o) = -de (8 + 1)

w' = 8 + 1); J(28 + 1)(28 +3)

(7.84)

= -de (8' = 8 - 1).

J(28 - 1)(28 + 1)

Recalling that the unperturbed energy of 18, m) is Ea= Be8(8+1), the second- order energy shifts are (after some algebra): (2)

1(8', m'I H' 18, 0)1 d2e2 E(a.o) = L Ea - E' = Be 2(28 - 1)(28 + 3) .

a'=o±1 a (7.85)

The first-order perturbed wavefunctions are: 18, 0/ 1) = 18, o) + 'r/- 18 - 1, o) + 11+ 18 + 1, o), (7.86)

where (8-1,01 H' 18,0)

de 'Tl- = --E- 0 --E-a--1- = - -2B-e -✓-;::{2=8=1=)(=28=+=;::1)

(7.87)

## MOLECULES

and (a+ 1,01 H' 1a,o) de T/+ = = - Ea - Ea+1 2Be ✓(28 + 1)(28 + 3)

(7.88)

The condition that the electric field is sufficiently weak to use perturbation theory can be written (for 8 > 0) as (7.89)

(c) From the same argument as in part (a), even for the perturbed states, (dx) === (dy) = 0. However, now (dz) =/= 0, for (dz)ca,o) = 2TJ-(8, 0I dz 18 - 1, 0) + 2TJ+ (8, 0I dz 18 + 1, 0)

= - 2 ((3 -1,0I H' 13,0)

2 + (3 + 1,01 H' 13,0) )

e Ea - Ea-1 Ea - Ea+1 (7.90)

( de)

= -d Be (23 - 1)(23+ 3) ' where we have used Eqs. (7.84), (7.87), and (7.88).

It is notable that the states with 8 = 0 and 8 = 1 have different signs of (dz): de (dz) (o,o) = +d . 3Be > 0 ' (7.91)

while de (dz)(l,O) = -d. 5Be < 0.

(7.92)

It may be surprising, at first glance, that the a = 1 state acquires a dipole moment in the direction opposite to the applied electric field! To understand this phe- nomenon, note that the sign difference persists (indeed, the magnitude of the difference increases) if we ignore mixing of the a = 2 state into the a = 1 state.

If we consider just the two-level system consisting of a = 0 and 8 = 1, the physi- cal meaning of the sign difference becomes more evident. Just as for any two-level system, applying a static perturbation causes the energies of the two levels to repel: the lower level 8 = 0 goes down in energy, and the upper level a = 1 goes up.

Since in this case the perturbation Hamiltonian is H' = -dzE, this energy shift can only occur because the perturbed states acquire a nonzero value of (dz). The different signs of the energy shifts must be correlated with different signs of (dz).

This is indeed what we have shown.

SCALAR COUPLING OF NUCLEAR SPINS IN MOLECULES We comment in passing that the nonzero value of (d) does not violate either of the symmetry arguments presented in the solution to part (a). For, in the presence of the external electric field (£), the eigenstates are no longer states of definite parity; and (d) ex (£) does not violate T-invariance, since both (d) and (£) are even under T.

The state-dependent dipole moment derived here may be useful for engineer- ing the state-dependent energy shifts required for quantum logic gates: see, for example, DeMille (2002) and Barenco et al. ( 1995).

7. 7 Scalar coupling of nuclear spins in molecules In this problem we investigate the phenomenon first discovered by Hahn and Maxwell ( 1952) of "J-coupling" (also known as scalar coupling) between nuclear spins in nucle~ mag~etic resonance (NMR) spectroscopy. For a system of two nuclear spins Ia and lb, this effect leads to a term in the Hamiltonian of the form (7.93)

(Here J is a coefficient that should not be confused with angular momentum.)

Let us assume that the two spins are oriented in the same direction. Note that the Hamiltonian (7.93) is independent of the angle between this direction and the vector f which points from one spin to the other. This distinguishes the J-coupling Hamiltonian from the direct dipole-dipole coupling Hamiltonian, Hd: (7.94)

where 9a(b)µNla(b)

is the magnetic moment of spin a(b), 9a(b) are the nuclear g-factors, µN is the nuclear magneton, and Tab is the distance between the spins.

Suppose that our two spins are associated with two nuclei in one and the same molecule. In liquid or gaseous samples, rotation of the molecule rapidly averages the dipole-dipole coupling term to zero, rendering it unobservable. 8 In contrast, the J-coupling term survives.

The J-coupling is used in conditional quantum logic gates in NMR-based quantum computers [for an introduction to and further references on quantum computers, see, for example, Nielsen and Chuang (2000)], and can be of help in unravelling the structure of complex molecules from their NMR spectra (Slichter 199()).

s We assume that the nuclear spins are decoupled from the molecular axis so that their orientation is unaffected by molecular rotations.

## MOLECULES

To understand the scalar coupling effect, we work with a toy model. Imagine a molecule consisting of a 3He atom in its ground state and a neutron (lb = In :::::: 1/2) at a fixed distance R from the 3He nucleus (la = I He = 1/2). This model Will capture most of the essential physics of the effect, while allowing us to use simple atomic wavefunctions rather than having to introduce molecular wavefunctions.

(a) Show that the average of Hd [Eq. (7.94)] over all directions f is zero.

(b) Show that the hyperfine interaction between atomic electrons and the 3He nucleus introduces a small admixture of the 1 s2s 3 S 1 state into the nominal I s2 1 So ground state. Find the size of this admixture. One may assume that the helium wavefunctions are simple products of hydrogenic wavefunctions for this purpose; that is, we ignore all effects of the electron-electron Coulomb interaction in this problem.

(c) Show that the 3 S1 admixture leads to a scalar coupling between the neutron spin and the 3He nuclear spin.

Find an expression for the size of the J-coupling as a function of R. Find the magnitude of J (in frequency units), and compare it to the size of the direct dipole- dipole coupling for a typical intranuclear separation in a molecule ( R ,....., 2ao).

Solution (a) Consider for specificity the case where the nuclear spin projections along the z- axis are m 1 a = m 1 b = + 1 /2; all other combinations of m 1,, and m 1,, give identical results. Define the direction of f by the polar angles ( (}, </J).

Then the numerator of Eq. (7.94) is - - - - la· lb - 3(/a · f)(lb · f) ex 1 - 3cos 8.

Thus, the average over all directions of the Hamiltonian (7. 94) is as claimed.

(Hd)n ex / (1 - 3 cos2 6)df2 ex / (1 - 3x 2)dx = 0, (7.95)

(7.96)

(b) The Hamiltonian of the hyperfine interaction for twos-state electrons interact- ing with the 3He nuclear spin is: H l61r (- 1-.£3(-)

- - .r3(- ))

hf= -3µ09HeµN s1 • au r1 + s2 · lau r2 = Hhfl + Hh/2, (7.97)

where the indices 1, 2 refer to the electrons. (See Problem 1.4 for a derivation of this Hamiltonian.) This is a scalar operator in the space of the total angular momen- tum F = S + I, but can couple terms with different values of total electron spin S;

SCALAR COUPLING OF NUCLEAR SPINS IN MOLECULES i.e., F and rn F are conserved quantities in the presence of H hf, but S is not. (See Problems 1.11 and 3.18 for other effects caused by off-diagonal hyperfine mixing.)

Thus, the hyperfine interaction causes the nominal 1s2 1S0 (/ = F = 1/2) ground state to obtain a small admixture of excited states such as the 1s2s 3 S1 ( F = I /2)

state.

Crudely, we can estimate the order of magnitude of this admixture as rv (aeao) (me aeao) (~) (a~)

rv me o 2 rv 10- 7 .

mp a0 e mp (7.98)

Here we have used the convenient relations and ignored factors of order unity.

To be more explicit, we calculate the matrix element (e, Mel Hhr 19, Mg), where and le,Me) = l1s2s 3S1(F= 1/2,Me)).

Since H hf is a scalar operator, only the matrix elements with Me = Mg = M are nonzero, and their values are independent of M. For concreteness, we choose M = I /2, and expand the spatial and spin wavefunctions: lg) = -t/Jis( f•i)¢1s( 'r2) ~ (lo:1.82) - l.810:2)) I i); je) = ~ { 1/J2s { f1 )1/J1s { 'r2) - 't/Jls { f1 )'t/J2s { 'r2))

X [ ~lo:10:2) 11) - IT.

lo:i,82) + I.Bi 02) I i)l V 3 V a v12 ' (7.100)

(7. I 01)

where t/J(r) are hydrogenic spatial wavefunctions; the states lo) and 1/3) refer to electron spin up and down respectively; and the states ll) and I!) refer to the 3He nuclear spin. Note that we have explicitly included the Clebsch-Gordan coefficients necessary to couple S = 1 and I = 1/2 together to fonn the (F = 1/2, M = 1/2) state of le).

Note that the two tenns of H hf, arising from the two electrons, differ only by the exchange of indices 1 +-+ 2. Since both wavefunctions le) and lg) are antisym- metric with respect to exchange, the matrix elements of both terms in H hf will be

## MOLECULES

identical. Thus we can write (el Hhf lg) = 2 (el Hhfl lg) = - 3!11"

Jl-OgtteµN (el 81 . fat5 3(f1) lg)

32,r 1 / ( - ) i-3 ( - )

( - ) d3 - = -3J1-0gHeµN y'2 1P2s r1 u r1 1P1s r1 r1 1 [ - _ - 1- - ]

X v'3 - (/Ji ii 81 · Ia 101 !) - 2 (01 ii s1 · Ia 101 i) + 2 (/h i S1 · Ia I.Bi f} .

(7. 102)

Calculating the matrix elements of i1 . fa using either the identities for spheric a)

components (see Problem 1.11) or the standard raising and lowering operators, we find (7. 103)

Using the explicit expressions for the hydrogenic wavefunctions and their energies (with nuclear charge Z = 2), the hyperfine-induced mixing coefficient 1/He is then (7. 104)

(c) Let the neutron position R be given in spherical coordinates as (R, 8, </J).

The admixture of the 1 s2s 3 S 1 state creates a nonzero magnetization at this position so one needs to introduce a second hyperfine-like contact term in the Hamiltonian:9 16,r ( - - - - )

Hn = -3µognµN 81 · Int5 (r1 - R) + 82 · Int5 (ii - R) .

(7. 105)

The quantum state taking into account the neutron (but before introducing the Hn)

1s: lo, fflHe, mn) = (lg, fflHe) + 7JHe le, ffiHe)) I mn) ' where we label the z-projections of ke and fn as mHe and mn, respectively. Thus, the first-order energy of interaction with the neutron is LlE~l) = (o, m, mnl Hn lo, m, mn) ~ 2,,He (e, m, mnl Hn lg, m, mn). (7.106)

Algebra similar to that in part (b) above yields the result (1)

32,r - - LlEn = µ;1'/HeJ4JJln1Pls (R, 8, <P) 1P2s (R, 8, </>)

ffiHemn = JI He · In, (7.107)

3v3 9 Note that similar to the direct dipole-dipole interaction of the two nuclear spins (7.94), the noncontact interaction of the neutron's spin with the induced magnetic moment of the atomic shell also vanishes upon molecular rotations.

## ZEEMAN EFFECT IN DIATOMIC MOLECULES

where J is independent of the angular position ( (), ¢) of the neutron, because of the isotropy of the s-state wavefunctions. Writing the hydrogenic ls and 2s wavefunctions explicitly, we find (7. 108)

For R ,....., 2ao, using 9He = -2.1 and 9n = -3.8, we find J ,.....,

## 0.3 Hz. Typi-

cal values in real molecules can be substantially larger, up to J ,....., 300 Hz. This discrepancy is easily understood: our toy model neglects the enhanced overlap of the electron wavefunctions with the second nucleus (the neutron here), due to the Coulomb attraction. Note finally that in our model the magnitude of the direct dipole-dipole coupling can be written as 9He9nµ N me ( )2 (Hd) ~ R3 = 4(R/ao)3o: 9He9n mp Roo, (7.109)

Thus -- ,....., --- Q2 - 1 - - e-3R/ao ,....., 3 X 10-5.

J ( R )

( R )

(Hd)

27 v'2 ao ao (7. I I 0)

Once again, in real molecules J can be enhanced by up to about three orders of magnitude compared to our simple estimate. Even with such an enhancement, however, the J-coupling strength is typically 1-2 orders of magnitude weaker than a direct dipole-dipole coupling.

7 .8 Zeeman effect in diatomic molecules The electric field due to the single nucleus of an atom is spherically symmetric, but for a diatomic molecule, the electric field from the pair of nuclei is cylindrically symmetric. Since the molecular electrons move in a non-spherically symmetric field, torques are exerted on the electrons by the field and their total angular momenta are not conserved. (Angular momentum is evidently transferred between the electrons and the rotation of the molecule.) However, because of the cylindri- cal symmetry about the internuclear axis in diatomic molecules, there is no torque on electrons about the axis, so the projection of the electronic angular momentum along the internuclear axis is conserved.

There are several different kinds of angular momenta associated with a diatomic molecule (see A__ppendix C). Neglecting nuclear spins, we have elec- tronic orbital momentum L with the magnitude of its projection on the internuclear

## MOLECULES

axis denoted A, electronic spin S with the magnitude (!.f the projection on the internuclear axis E, total electronic angular momentum Je with the magnitude of the projection on the internuclear axis n, rotational angular momentum of the molecule i (perpendicular to the internuclear axis - since by definition, rota ..

tions around the internuclear axis are electronic angular momentum), and the total angular momentum J of the molecule.

Depending on the relative magnitude of various interactions within the molecules, angular momenta should be coupled in different order giving rise to a number of the so-called Hund 's coupling cases [see, for example, Herzberg ( 1989), Landau and Lifshitz (1977), or Auzinsh and Ferber (1995)].

(a) Estimate the order of magnitude of the molecular magnetic moment resulting from molecular rotation.

(b) For molecules where there is a strong spin-orbit interaction, e.g., molecules i~volving heavy nuclei, one first adds i and § vectorially to form the resultant Je [this is known as Hund's case (c) - see Herzberg (1989)]. The total angular momentum J of a diatomic molecule is the sum of the total electronic angular momentum le and the rotational angular momentum l (7.11))

However, as noted at the beginning of the problem, le and l are not conserved quantities in a diatomic molecule because the electrons and nuclei exchange angu- lar momentum as the electrons move through the non-spherically-symmetric field.

In quantum mechanical terms, the eigenstates of the Hamiltonian for the molecule are superpositions of states with different values of Je but the same value of n, since the projection of le on the internuclear axis is conserved. Thus, as is the custom in much of the literature [for example, Herzberg ( 1989), Townes and Schawlow ( 1975), and Zare ( 1988)], one expresses Jin terms of the average val- ues of le (which is n, the component of le along the internuclear axis) and l (known commonly in the literature as simply the rotational angular momentum, denoted here as 8): 1 = (le + i) = n +a.

(7.112)

Consider a molecular state for which suitable quantum numbers are J and n.

Using the v~ctor model, find the Zeeman shift of sublevels in terms of the magnetic moment gµofl defined in the molecular frame. Assume that the strength of the magnetic field is sufficiently weak so that it does not alter the angular-momentum coupling. Neglect the magnetic moment due to molecular rotation estimated in part (a).

## ZEEMAN EFFECT IN DIATOMIC MOLECULES

Solution (a) For the purpose of the estimate, we can model the magnetic moment produced by a rotating molecule as that of a current loop in which a charge q rotates with radius r rv a0 (i.e., a typical molecular size), at a frequency characteristic of molecular rotation, Roe me Vrot rv 21rfi . µM' (7.113)

where µM is the molecular reduced mass (see, for example, Problem 7.5).

There are, in fact, two contributions of opposite sign to the current (Townes and Schawlow 1975): (I) that from the nuclei along with the electrons in closed shells bound to the individual nuclei (which partially screen the nuclear charge)

rotating about the center of mass, and (2) that from the valence electrons that form the molecular orbital. The contribution from the valence electrons depends on the details of the electronic wave function; often the contribution from the valence electrons can be the dominant contribution, and in some cases there is near can- celation of the two contributions [for example, this is true for alkali dimers in the ground state, see Auzinsh and Ferber (1995)). For a rough estimate assuming the absence of strong cancelation, we take fql rv e.

For a current loop, the magnetic moment is given by µ = iA/ c, where i is the magnitude of the current, and A is the loop area. Without perfonning an explicit calculation, we can just notice that the estimate is the same as for the magnetic moment of an atom due to the orbital angular momentum (which is rv µo), except the atomic frequency is replaced by the molecular rotation frequency (7 .113), which is rv µM /me rv mp/me times smaller. Thus, we estimate the order of magnitude of the magnetic moment associated with molecular rotations as (7.114)

where µN is the nuclear magneton.

(b) Neglecting the magnetic field, according to the vector model (Fig. 7.2), the total angular momentum J is conserved, while the component of the electronic angular-momentum vector along the internuclear axis O and the rotational angular- momentum vector ff are spread on cones around the direction of J (their vector sum is always equal to J).

The average projection of the magnetic moment (which is parallel to O; Fig. 7.2) on the total angular momentum J is then easily found from geometry as n gµon2 gµofl cos 8 = 9/1-0n---::. = ---;::=== , IJI ✓J(J + I)

(7.1 I 5)

## MOLECULES

-a internuclear ·····ax15······ FIG. 7.2 Vector-model representation of Hund's case (c). Vector J: is the electronic ang 1 - uu momentum, and{} is the average value (in the molecular frame) of the electron angular morne _ - - n tum directed along the internuclear axis. Vectors a (molecular rotatio~ and n are assumed to undergo nutation around the total angular momentum of the mole~ule J. The magnetic moment j1 is defined in the molecular-axis frame and is collinear with {}; IPI = gµ,o{}. Vector a is perpendicular to the molecular axis.

where we have employed the quantum-mechanical expression for the length of the total angular momentum v~tor. In the presence of the magnetic field, the total angular momentum vector J uEdergoes Zeeman precession around the direction of the field. The projection of Jon the magnetic field is M. Thl!_s, in order to find the average projection of the magnetic moment ( directed along J) on the magnetic field, we need to multiply (7 .115) by M / ✓ J ( J + I), resulting in M µ(M) = gµoO. J(J + l) , (7.116)

and the Zeeman shift of the M-sublevel is -µ(M)B, where Bis the magnetic- field magnitude.

Note that, according to Eq. (7 .116), the magnetic moment of a molecule rapidly decreases with J, and, correspondingly, for a given electronic state, with the value of rotational excitation. This is the reason why, typically, only a small (low-J) part of a molecular rotational band produces significant magneto-optical effects [see, for example, Budker et al. (2002)].

A detailed discussion of the molecular Zeeman effect in different Hund's cases can be found in books by Herzberg ( 1989) and Auzinsh and Ferber ( 1995).

## OMEGA-TYPE DOUBLING

7 .9 Omega-type doubling Consider a diatomic molecule for which the appropriate angular-momentum cou- pling scheme is described as follows. Due to strong LS coupling (as occurs for heavy nuclei), the electronic orbital angular momentum i and spin S couple into the total electronic angular momentum le. The magnitude of the projection of le on the internuclear axis is fl. This is referred to as Hund's case (c) [see, for exam- ple, Herzberg_ ( 1989) and Problem 7 .8). The rotation of the molecular frame is described by a, which is perpendicular to the internuclear axis. The total angular momentum of the molecule is J (see discussion in Problem 7.8). In this problem, we neglect nuclear spins.

Explain why each of the states with given values of total angular momentum J and its projection on a quantization axis !vi is split into a doublet of states of opposite parity (fl-type doubling). Estimate the magnitude of the energy splitting between the components of the doublet (for a given J) for n = 1.

Solution Neglecting molecular rotation, it is clear from the symmetry of the problem that the states that differ by the sign of the projection of the electronic angular momen- tum le on the internuclear axis (±fl) are of the same energy. This degeneracy is, however, lifted if one takes into account molecular rotation. 10 An eigenstate of the full Hamiltonian of an isolated, free diatomic molecule should be a state with a given value of the total angular momentum J, its projection M, and parity. Note that a state with a projection of le along the internuclear axis +n is not a state of definite parity, since applying the parity operator would leave the angular momentum le unchanged while the relative position of the nuclei reverse, so parity transforms the +fl state into the -fl state. Yet it can be readily seen that the states of definite parity are linear combinations of the states with +n and -n [see, for example, Zare ( 1988), Application 15]: if one fonns an equal superposition of the ±fl states, the parity operator will transfonn the state into itself up to an overall sign. How does molecular rotation split these levels?

Following Khriplovich ( 1991 ), Section 9.3 [see also Landau and Lifshitz ( 1977), Section 88 ], let us consider the operator for the rotational energy of the 10 The enormously useful theoretical framework where one treats motions that occur on different time scales independently (for example, ••freezing .. vibrations and rotations while considering elec- tronic motion) is called the Born-Oppenheimer approximation [see, for example, Lefebvre-Brion and Field (2004)]. Understanding the 0-type doubling effect clearly requires one to go beyond the Born-Oppenheimer approximation, as the effect arises due to coupling of the electronic motion and molecular rotation.

## MOLECULES

molecule (see Problem 7.3): (7. 117)

where ~ is the rotational angular momentum and / is the moment of inenia. In Problem 7.8, it was pointed out that because of the coupling of electronic angular momentum to molecular rotations, it is convenient to use the average value of .J.

(which is fi, the component o! fe along the internuclear axis) and the avera~ rotational angular momentum a, see Eq. (7.112): h2 - h2 - - Hn = 21 £,2 = 2/ (J - Je)2 li2(_ - - -)

= 2/ J 2 - 2J · Je + J]

( 2 - - 2)

= - J -2J-n+n 2/ ' (7.118)

where ~ indicates the appropriate average. The term J · fe = J · fi because J is constant and fixed in space (being the total angular momentum), whereas .J.

- e averages to n as discussed in Problem 7 .8.

Let us examine the three terms in the expression (7 .118). The first tenn is diagonal in the basis of molecular wavefunctions f J, n, M) and contributes to the rotational energy.

The second tenn can have both diagonal and off-diagonal matrix elements because the operator fl, being a vector operator (see Appendix F), can change the value of the projection on the molecular axis by 0, ±1. The diagonal matrix elements (J, 0, Mf2f · flf J, 0, M), according to the Wigner-Eckart theorem (see Appendix F), are the same, up to a numerical factor, as the matrix elements of the first tenn. Thus, the first tenn and the diagonal part of the second term determine the rotational energies of the molecular levels. It is interesting to note that the rota- tional energy has the same form as that for a molecule with zero electronic angular momentum (fl = 0), where the rotational energy is given by Be8(a + 1) , (7.119)

(where Be is the rotational constant) except that the molecular-frame rotational quantum number 8 is replaced by that of the total angular momentum J. An impor- tant difference here is that a takes on any nonnegative integer value, while J can be half-integer, and has to be greater than or equal to n (this qualitatively changes the spectrum since for n ;: 0 the usual low-lying rotational levels are "missing").

- - In addition, due to the tenn proportional to J · n in Eq. (7.118), the rotational constant Be is no longer given by simply Be = li2 /(21).

## OMEGA-TYPE DOUBLING

The third tenn on the right side of Eq. (7 .118) is diagonal in the I J, 0, M) basis, and only depends on the electronic state of the molecule. It gives an overall offset to the electronic energy, and is of no interest for us here.

Let us now tum to the off-diagonal matrix elements arising from the sec- ond term in Eq. (7 .118). We are interested in tracing how this term couples ±n states. Since, upon the action of this operator, the value of the electronic-angular- momentum projection on the molecular axis can change by ±1, the ±n states are only coupled in first-order perturbation theory if n = 1/2. It is clear from Eq. (7 .118) that the magnitude of 0-type doubling is on the order of the rotational energy splitting in this case.

What if fl > 1 /2? In this case, the ±n states can still be coupled, but this coupling only appears in the 20-th order of perturbation theory. For O = 1, this is the second order, and we can estimate the order of magnitude of the splitting as the square of the off-diagonal matrix elements between the states differing by one in the electronic-angular-momentum projection on the molecular axis divided by the energy separation between these states: AE J2B';_ ~ ef rv • En=1 - En=o (7.120)

Here we have used the customary notation for the 0-type-split doublet of levels (e, /). For low J, the doublet splitting is on the order of the rotational constant times me/mp [because the denominator in Eq. (7.120) is proportional to e2 / ao].

An explicit calculation of the matrix elements replaces the J 2 factor in Eq. (7.120) with J(J + 1) (and, of course, allows one to obtain a more accurate value of the splitting rather than just an order-of-magnitude estimate).

## EXPERIMENTAL METHODS

## 8.1 Reflection of light from a moving mirror

(a) A beam of monochromatic light of wavelength Ao propagates (through vac- uum) at an angle <.p to the vertical. A part of this beam is reflected by a semitransparent stationary mirror kl I (Fig. 8.1) and directed into a remote pho- todetector. The part of the beam transmitted though MI is reflected onto the same photodetector by a horizontally oriented mirror Jvf 2 which moves in the vertical direction with velocity v << c. The output of the photodetector is connected to 3 spectrum analyzer. Which frequency components will be seen?

To photodetector I <p : ,/i • I I Ml FIG. 8.1 Schematic diagram of setup for Problem 8.1 ( a). lncomi ng light with wave vector ko is reflected by the stationary mirror A/ I (producing light with wave vector k1) and the moving mirror A12 (producing light with wave vector k2 ). The two reflected beams are directed onto a photodetector. The photodetector averages over optical frequencies, but can detect the beat frequency between the two reflected beams.

## EXPERIMENTAL METHODS

JfV -..~ ............

...-....,...,..,......,.~,..

FIG. 8.2 Schematic diagram of setup for Problem 8.1 (b ). In this case we consider a single mirror moving with arbitrarily directed velocity v.

(b) A beam of light (wave vector kin) falls onto the surface of a mirror at an arbi- trary angle. What is the first-order Doppler shift in the magnitude of the wave vector (~k = fkoutl - fkinl)

resulting from the mirror's motion v (Fig. 8.2)?

Solution (a) The angular frequency of the incoming light is w0 = 21rc/ Ao. It remains unchanged upon reflection from the stationary mirror MI. In order to find the fre- quency of the light reflected from M2, it is convenient to first go to the frame moving with M2. Shifting to a frame moving with velocity v, the observed frequency of the light changes by ~w due to the Doppler effect: (8.1)

Therefore, in this frame, the incoming light has the Doppler-shifted frequency WI = WO ( 1 + ~ COS <p) .

(8.2)

As seen from this frame, the reflected light has the same frequency w1, but going back to the lab frame, we need to account for the Doppler shift once again [Eq. (8.1 )]. The angle between k2 and vis cp, and to go back to the lab frame, we are shifting to a reference frame moving with velocity -v. Therefore, the frequency of light reflected from M2 in the lab frame is: w2 = WI ( 1 + ; cos <p)

~ Wo ( 1 + :v cos <p) ' (8.3)

where we have neglected terms second order in (v/c). Assuming that the pho- todetector averages over optical frequencies, the spectrum analyzer will show a de

## LASER HEATING OF A SMALL PARTICLE

component of intensity and a component at V w2 - wo ~ 2kov cos 'P = 2wo- cos 'P , C where ko is the magnitude of the incoming light wave vector.

(8.4)

Note that the physical picture of the frequency shift upon reflection from a moving mirror can be used to understand the principle of acousto-optical frequency shifters. In these devices, the role of the moving mirror is played by a travelling sound wave from which the light is reflected.

(b) In the frame moving with the mirror, according to Eq. (8.1 ), the incoming light frequency is shifted by: (8.5)

The reflected wave has the same frequency in the moving frame, but when we transfonn back to the lab frame there is an additional Doppler shift of I - - ~w = kout.

V' (8.6)

so overall the frequency is shifted by (8.7)

and therefore the magnitude of the wave vector changes by tl.k = tl.k-v ' (8.8)

C where ~k = kout - kin• This result is used in Problem 8.14 to analyze gyroscopes based on the Sagnac effect.

## 8.2 Laser heating of a small particle

Consider the interaction of light of wavelength .,\ with a small spherical metal particle of radius a (ka << 1, where k = 21r / .,\). Estimate the power absorbed by the particle per unit time.

To solve this problem, devise a simple model that captures the essential physi- cal mechanism leading to heating. Discuss the dependence of the absorbed power on the particle's size and on the light frequency.

## EXPERIMENTAL

## METHODS

Make numerical estimates for the case of silver particles with a = l µm, A :::::: 10 µm, and a light pulse with total energy E = l J, beam cross-section A :::::: 1 cm 2, and pulse duration of,.,. = 10 ns. How hot will the particle be at the end of the pulse? Assume uniform heat distribution over the volume of the particle. 1 Hint First note that because of the small size of the metal particle (ka << 1), we can assume that it is immersed in uniform, quasistationary electric and magnetic fields.

The optical electric field inside the conductor is compensated by a redistribution of charge, which produces no sustained current and therefore very little heating.

On the other hand, a quasicontinuous current is required to compensate the optical magnetic field. Due to the resistivity of the metal, this leads to heating of the particle.

A useful concept in solving this problem is the skin depth (i.e., how deep the magnetic field penetrates into the metal), given by [see, for example, Griffiths (1999) or Jackson (1975)]: ...

_{lf2p .

1rµw (8.9)

Here p is resistivity, µ is magnetic permeability (µ ~ l for nonmagnetic materials), and w is the frequency of the electromagnetic field. For silver, p ~ 1.47 x 10- 6 {l · cm ~ 1.63 x 10- 18 CGS .

(8.10)

In order to obtain a numerical estimate for the heating of the silver particle, use the facts that the specific heat c,, for silver in the relevant temperature range is and the density of silver is J Cp~0.24-K, g· Pd~ 10.5~.

(8.11)

(8.12)

1 The assumption of uniform heat distribution over the volume of the particle is justified since the characteristic temperature diffusion time [see, for example, Baierlein ( 1999), Chapter 15] is td = CpPd • a2 ~ 6 x 10- 9 s < r .

K.t Here Kt ~ 4 W /cm/K is the thermal conductivity of silver, c,, is the specific heat, and Pd is the density of silver, given later in the problem.

## LASER HEATING OF A SMALL PARTICLE

Solution According to Eq. (8.9), the skin depth of silver is 8 ~ 1.1 X 10- 6 Clll <<a.

(8.13)

Therefore the magnetic field indeed does not penetrate into the depth of the metal particle, and the magnetic field of the light is compensated by an induced surface current. We will estimate the power deposited in the particle as resistive heating due to this current.

As discussed in the hint, since ka << 1, we can assume that the particle is immersed in a uniform quasistationary magnetic field. The induced magnetic moment (Griffiths 1999) is: (8.14)

where B is the magnetic field of the light wave. In Eq. (8.14) we have introduced an "effective loop current" i = cBa/(21r) that induces the same magnetic dipole moment for a circular loop of radius a. 2 The final step in the estimate is the calculation of the effective resistance R.

The transverse cross-section area of the current path is ~ 6 • a, and the average length of the path around the particle is ~ 1ra. From this we have R ~ p1r / 8, and the dissipated power (8.15)

Substituting the expression (8.9) for 6, and expressing the magnetic field of the light through the parameters of the laser beam we get: B2 E c 41r = rA' (8.16)

(8.17)

Equation (8.17) shows that the absorbed power increases as the square root of the light frequency (inversely proportional to the skin depth). One should note, 2 In Eq. (8.14) we used the fact that the magnetic polarizability of a conducting sphere is a3 /2.

This can be derived in a manner analogous to that employed in Problem 2.1 to derive the electric polarizability of a conducting sphere. The total magnetic field outside the sphere is the sum of the external uniform B-field and that of the induced dipole. The component of the total field normal to the surface of the sphere must be zero because B = 0 inside the sphere, and the component of B nonnal to the surface is continuous across the interface. This gives the desired result for the polarizability.

## EXPERIMENTAL METHODS

however, that the character of the skin effect in metals changes for frequencies cor- responding to light wavelengths below~ 10 µm [see, for example, Born and Wolf ( 1980), Chapter 13.2], where the skin depth becomes comparable to the scattering length of electrons in a metal, and the present model is not applicable.

Equation (8.17) also shows that the absorbed power scales as the geometrical cross-section of the particle (<X a2). This dependence should be contrasted with the power of the light scattered by the particle which scales as a6 (in proportion to the square of the induced electric dipole moment).

The numerical value of the absorbed power for the parameters of the problem is P ~ 4 x 10- 2 W, and the total absorbed energy during the pulse is Q ~ 4 X 10-IO J.

Assuming that the heat uniformly distributes over the volume of the particle, we find for the change in the particle's temperature: (8.18)

where Cp is the specific heat and m ~ 4.4 x 10- 11 g is the mass of the particle.

## 8.3 Spectrum of frequency-modulated light

Consider a field e(t), oscillating at central frequency w0, which is modulated with frequency n with modulation depth mn (mis the modulation index).

e(t) = eo exp [iwot + im sin nt] .

(8.19)

Using the standard Bessel function identity [see, for example, Siegman ( 1986),

## Section 27. 7)]

eimsinnt = L Jk(m)eiknt, (8.20)

k=-oo the spectrum of the field can be represented as a sum of frequency components (sidebands) whose relative amplitudes are given by the Bessel functions Jk(m).

Qualitatively describe the changes in the power spectrum of frequency- modulated light as the modulation index goes from small (m << 1) to large (m >> 1) values.

## SPECTRUM OF FREQUENCY-MODULATED LIGHT

I .

0.8.

~ 0.6; ., .

~ 0.4, 0.2: I .

r

## 0.8 '

~ 0.6' ~ ~ 0.4: 0.2 (a)

- I _I - k (b)

k 0.05 0.04 ~ 0.03 ~ 0.02;

## 0.01

(c)

k IO FIG. 8.3 Power spectrum of frequency-modulated field. The height of the k-th frequency compo- nent is given by Jf (m). (a) m = 0.4, (b) m = 2, (c) m = 40 (note the difference in both the vertical and horizontal scales).

Solution According to the identity (8.20), we have C(t)=Coexp[iwot+imsinnt]=Coeiw.,t L Jk(m)eiknt_ (8.21)

k=-oo When the modulation index is small [Fig. 8.3(a)], there are two small sidebands [containing ~ ( m/2) 2 of the total power each] that are separated from the carrier by ±n, and the other sidebands are negligibly small. As m increases [Fig. 8.3(b)], a larger number of sidebands gain prominence, while the central peak decreases.

## EXPERIMENTAL METHODS

Finally, for large m [Fig. 8.3(c)], sidebands in the entire range from w _ n n .

. h h" h . eel.

rn-1, to w + m~, are generally promment, wit 1g est power contam m the cornP<>nents towards the ends of the range.

A qualitative explanation for this is easily gained from a time-domain p,· Ctu,e.

A large modulation index corresponds to a deep frequency modulation. A the frequency oscillates in time, it "spends" the longest time near its turning pos· hd ..

"h ti ID~ t us epos1tmg most power m t e extreme requency components.

This qualitative change in the character of the spectrum is reminiscent f 8 transition from a quantum to a classical hannonic oscillator. The ground stat.

f the oscillator corresponds to maximal wavefunction density near the P<>sitio e ~f equilibrium, while a classical oscillator that can be seen as a coherent superpos -~-00 of a large number of quantum excitations has largest time-averaged density ~ the turning points.

## 8.4 Frequency doubling of modulated light

Consider a frequency-doubling device, e.g., a doubling crystal for laser light.

Given monochromatic radiation of frequency w at the input, the output is monochromatic radiation of frequency 2w with intensity proportional to the square of the input intensity. Suppose now that the input radiation is modulated at a fre- quency n, so its spectrum consists not only of the carrier frequency w, but also of sidebands at combination frequencies.

What is the frequency spectrum (frequencies and relative sizes of spectral com- ponents) at the output of the doubler? Assume that the bandwidth of the doubler is large enough to accommodate all the relevant frequency components. Consider the cases of weak amplitude and frequency modulation of the input radiation (i.e., first-order sidebands are much smaller than the carrier, and higher-order sidebands for the case of frequency modulation are negligible).

Solution The output of the doubler will consist of peaks at the carrier frequency 2w and side- bands at 2w ± n, i.e., while the carrier frequency doubles, the separation between the carrier and the sidebands remains unchanged.

There are several ways to see this. One is to consider modulation in the time domain. In the case of amplitude (frequency) modulation, when the input beam has, for example, the highest intensity (frequency), so does the output beam, and variations occur with the same periodicity given by the frequency n.

Another picture is that of frequency mixing. When more than one frequency component is present at the input, the "doubler" mixes all combinations of the

## FREQUENCY DOUBLING OF MODULATED LIGHT

input frequencies, which results not only in doubling the frequency of the car- rier and the sidebands (the latter results in sidebands of negligible size in the case of weak modulation), but also in generating radiation at the sum frequencies of the carrier and each of the sidebands. It is exactly these sum frequencies that correspond to the dominant sidebands at the output.

Now we tum to the discussion of the size of the sidebands relative to the carrier.

We will see that for both weak amplitude and frequency modulation, the ratio of the amplitude in each of the sidebands to that of the carrier at the output of the doubler is twice that at the input (which translates into a factor of four for the ratio of intensity in the carrier to intensity in the sidebands).

This is particularly easy to see in the case of the amplitude modulation. The electric field at the output of the doubler is: eOlll ex: e;/ ex: [(1 + t:sinfU)eiwtJ2 ~ (1 + 2t:sinnt)e 2iwt, (8.22)

where e is the modulation coefficient. Inspection of the last expression in (8.22)

reveals that the relative amplitude of the sidebands at the output is twice that at the input.

Consider now the case of frequency modulation. The instantaneous frequency of the input radiation can be written as Winst = w{l + Q sin Ot), (8.23)

where a << 1 is a coefficient characterizing the depth of the modulation. The phase </J(t) of the field is found by integration of the frequency (8.23) over time.

Neglecting a constant phase off set, we write the input electric field as C;0 (t) = Coeicf, + c.c. = Co exp [iw (t - ~ cos nt)] + c.c., where e.o is the field amplitude. 3 (8.24)

The amplitudes of the frequency components corresponding to the field (Eq. 8.24) are given by the Bessel functions Jk(m) (see Problem 8.3), where m = aw/0 is the phase modulation index [frequency modulation is in fact equiv- alent to phase modulation as one can see from Eqs. (8.23) and (8.24)], and k is the number of the sideband: k = 0 for the carrier, and k = ±l for the sidebands of interest. Inspecting the expressions (8.23) and (8.24), and using the fact that the modulation frequency n is the same at the output and at the input, one con- cludes that m increases by a factor of two from the output to the input (we have w ---+ 2w, a --+ o, n ---+ n, m --+ 2m upon doubling), which by the properties of 3 We caution the reader against a common mistake: the time-dependent electric field (8.24) is not equivalent to Eo exp (iw[l + a' cos Ot)t) + c.c. The latter form does not correspond to harmonic frequency modulation.

## EXPERIMENTAL METHODS

the Bessel functions translates into twice the relative amplitude in the sidebancas for the output.

Of course, exactly the same results are obtained using the language of f~- quency mixing via the nonlinear optical susceptibilities x<2> [see, for exarnpJe Boyd (2003)].

'

## 8.5 Ring-down of a detuned cavity

The technique of cavity ring-down spectroscopy (CRDS) involves exciting a res0- nant mode (or modes) of a high-finesse optical cavity, interrupting the input light and observing the exponential decay of the output intensity. Since the decay rat~ is determined by intracavity losses, the method allows one to sensitively measure very small intracavity losses and is free from backgrounds. It has been widely Used for characterizing cavity losses f such as those determined by mirror reflectivities (Anderson, et al. 1984)], and for detecting trace amounts of atomic and molecular species [see, for example, Ye and Hall (2000) and references therein].

Consider monochromatic input light and a two-mirror cavity.

(a) Assuming that the losses are determined by the reflectivities of the mirrors(~, i = 1, 2; <5i = 1 - Il,i << 1), find the intensity ring-down rate rrd• The length of the cavity is L. Discuss the dependence ( or lack thereot) of the ring-down time on the light frequency detuning from a cavity resonance.

(b) Suppose the output of the cavity that had been excited with monochromatic light (not necessarily resonant with the cavity mode) is sent to a high-resolution spectrometer whose input is gated in such a way that the spectrometer only "sees"

light emitted after the input to the cavity is interrupted. What spectral distribution wiJJ be detected as the cavity rings down?

Solution (a) It is convenient to solve this problem using the photon picture. A photon trapped inside the cavity has a probability of escaping the cavity of <51 or <5 2 upon a collision with the corresponding mirror. In one round trip of duration 2L/c, the escape probability is approximately <5 = <5 1 + <5 2• Thus, the ring-down rate is just <5c rrd = 2L , (8.25)

independent of the cavity detuning from resonance. The latter fact is sometimes used to effectively interrupt the input beam by taking the cavity out of resonance by rapidly translating one of its mirrors.

## TRANSMISSION THROUGH A LIGHT GUIDE

(b) The detected spectrum will be a Lorentzian (arising as a Fourier transform of exponential decay) with width (FWHM) 6w = rrd centered at the input light frequency.

Note that the behavior of an optical cavity is different from that of an electronic LRC oscillator, or a guitar string. If such an oscillator is driven at a nonresonant frequency, and the drive is suddenly removed, the circuit proceeds to oscillate at its resonance frequency ( or frequencies in the case of a string) as it damps.

## 8.6 Transmission through a light guide

Consider a light guide (Fig. 8.4) consisting of a cylindrical core with refractive (this is a common configuration for fiber-optic cables).

The ends of the light guide are cut perpendicular to the guide axis and pol- ished. A point source of light is placed close to one end of the guide. Calculate the maximum acceptance angle am for light to be transmitted through the guide and compute the solid angle of light accepted into the guide, assuming the surface of the fiber has an ideal antireflection coating. Also find a relationship between n 1 and n2 that maximizes transmission through the guide.

Solution At the first interface where the light enters the guide, we have from Snell's law (Fig. 8.4): sin a = n 1 sin /3 .

(8.26)

FIG. 8.4 Schematic diagram of a light guide.

## EXPERIMENTAL

## METHODS

In order for light to be transmitted through the guide, we require <.p = 1r /2 _ {3 to be greater than or equal to the critical angle for total internal reflec- tion [sin- 1(n2/ni)]. With a little trigonometry it can be shown that for these conditions, ✓n2 n2 . a< Sill /J • - n1 (8.27)

Combining Eqs. (8.26) and (8.27) yields: sin a < J n ~ - n~ .

(8.28)

Thus the maximum acceptance angle Om is given by I am= sin- 1 Jn~ -n~.

(8.29)

The solid angle of light accepted by the guide is given by: AO= 21r fo "' sinOdO = 21r(l - cos am).

(8.30)

Therefore the fraction of light not reflected at the entrance [see discussion of transmission coefficients and the Fresnel formulae in, for example, Fowles ( 1975))

which is transmitted by the core to the end of the guide is T = I - COS Om.

(8.3 I)

Transmission through the guide is maximized when (8.32)

Fiber optic cables, based on this phenomenon of total internal reflection, have found widespread use in telecommunications. Optical fibers can also exhibit an array of linear and nonlinear optical phenomena such as self-rotation, wave- mixing, and stimulated Raman and Brillouin scattering. An interesting application of such effects are wavelength-shifting fibers which convert incident light to dif- ferent wavelengths. Another fast growing area of research concerns photonic crystal optical fibers which consist of fibers containing repeatable structures with contrasting indices of refraction in their cross sections.

8. 7 Quantum fluctuations in light fields In a given experiment, there are usually many technical sources of noise that con- tribute to the uncertainty in the determination of a particular quantity of interest.

## QUANTUM FLUCTUATIONS IN LIGHT FIELDS

In principle, however, all of these sources of noise can be circumvented, until the noise in the experiment results entirely from quantum fluctuations (this is known as the standard quantum limit - see also Problem 8.9).

Thus the ultimate precision with which a measurement can be performed is governed by the Heisenberg uncertainty principle. Generally, if two observables are described by the operators A and B, then the variances (~A) 2 and (~B) 2 obey (8.33)

where ( ... ) denotes the expectation value, (A, B] is the commutator of A and B, and the standard deviation ~A of an observable A is given by (8.34)

How does the Heisenberg uncertainty principle limit the precision of optical measurements? It turns out that when the electromagnetic field is quantized (see Problem 3.2), the operators describing out-of-phase components of the optical field do not commute, and thus obey an uncertainty relation.

(a) Consider electromagnetic fields of a given mode that are described by the operators ec and es, where f.c = ~o ( a + at) , f.

8 =~;(a-at).

Here a and at are the photon annihilation and creation operators, f.o = ✓2~ (8.35)

(8.36)

(8.37)

is the single-photon electric-field amplitude (V is the normalization volume - see Problem 3.2), and we have set the overall phase of the field ( kz - wt) to zero.

Find the uncertainty relationship between the out-of-phase components of the optical field: ec and es.

(b) Coherent states of a single mode radiation field la), which can be produced with lasers, are "classical" electromagnetic fields and are eigenstates of the photon annihilation operator a (introduced in Problem 3.2), i.e., (8.38)

where lal is the amplitude of the field (in units of eo) and</> is its phase. The usual vacuum is also a coherent state with eigenvalue zero.

## EXPERIMENTAL METHODS

For a coherent field, we see that the expectation values of the operators Cc and cs are (cc) = (o:lcclo:) = colo:1 cos <t> , (cs) = (o:lcsfo:) = cola I sin </J.

(8.39)

(8.40)

Using Eq. (8.34) and the tools developed in Problem 3.2, find the variance in the photon number for a coherent state.

Solution (a) According to Eq. (8.33), the uncertainty relationship for Cc and Cs can be written in terms of the commutator [ec,£ 8 ] = !~ ([a,a]- [a,at]

+ [at,a]

- [at,at])

= i~5, (8.41)

wherewehaveusedthefactsthat [a,at] = -[at,a] = 1 and [a,a] = (at,at] =

## 0. Thus we have [using Eq. (8.33)]:

(8.42)

A state for which the relation (8.42) is satisfied as an equality is said to be a minimum uncertainty state.

(b) According to Eq. (8.34), the variance in the number of photons (~n) 2 in a particular mode of the electromagnetic field in a coherent state lo:) is given by (8.43)

where n = at a is the photon number operator discussed in Problem 3.2. We have (8.44)

and (n2) = (aln21a) = (alataatala) = (alat ( 1 + ata )ala) = lal2 + lal4 .

(8.45)

Using Eq. (8.44), the above relation (8.45) can be rewritten as (8.46)

QUANTUM FLUCfUATIONS IN LIGHT FIELDS oher nt i Id acuum Field uantum nu uation FIG. 8.S Phasor diagrams of coherent states. The plot on the left represents a coherent electro- magnetic field of amplitude lo:leo with phase </J. The plot on the right represents the vacuum field. The grey disks indicate the quantum fluctuations resulting from the fact that operators corresponding to the out-of-phase components of the electromagnetic field do not commute.

Thus, using Eqs. (8.44), (8.45), and (8.46), we obtain the result expected from Poissonian statistics: (8.47)

This is also known as the shot-noise limit.

Now it is apparent how the Heisenberg uncertainty principle limits the preci- sion of an optical measurement. Figure 8.5 shows the phasor representation of the out-of-phase components of the optical electric field for coherent states. We see that there is both an uncertainty in the phase and amplitude of a coherent field due to quantum fluctuations. Even when the amplitude of the field is zero, there are still r ("

un b r qu zin Pba e queezing FIG. 8.6 Phasor representation of the quantum fluctuations for squeezed states. The plot on the left shows number squeezing while the plot on the right shows phase squeezing. For minimum uncertainty states, the .. area" of the quantum fluctuations on the phase diagram does not change compared to the coherent states (Fig. 8.5), merely the distribution of the quantum fluctuations between the out-of-phase components.

## EXPERIMENTAL

## METHODS

quantum fluctuations, resulting from the zero-point energy of the quantized elec- tromagnetic field (Problem 3.2). Note that the quantum fluctuations of a coherent field are independent of its amplitude [Eq. (8.42)].

Although the Heisenberg relation (8.42) gives a minimum value for the Product of the variances (~t:c) 2 and (~t: 8 ) 2, it is possible to produce states which fulfill the uncertainty relation asymmetrically - such states are known as squeezed states (Caves 1981 ). Figure 8.6 shows phasor diagrams for squeezed states where the uncertainty in amplitude is reduced below the shot-noise limit (number squeezing)

and where the uncertainty in phase is reduced below the shot-noise limit (phase squeezing).

Over the last twenty years or so, there has been considerable progress in experimental techniques for producing squeezed states of light [see, for example~ Loudon and Knight (1987) and Walls and Milburn (1995)]. In general, a nonlin- ear optical interaction modifies the noise properties of light. An example of this is second-harmonic generation, which effectively removes large amplitude fluc- tuations because the second-hannonic generation proceeds more efficiently from more intense light. If the nonlinear interaction is phase-dependent - for example if the amplification depends on the phase of the optical field relative to the polariza- tion of the medium - squeezed light can be produced. Thus it turns out that many nonlinear optical processes, such as four-wave mixing, second-harmonic genera- tion, parametric amplification, and self-rotation of elliptical polarization, produce squeezed light.

## 8.8 Noise of a beamsplitter

Consider an ideal beamsplitter that divides an incoming light beam into two equal parts. If the incoming light field is in a coherent state with a mean number of photons (n), as seen in part (b) of Problem 8.7, the standard deviation of this photon number is '1(n). Each of the two output beams has a mean number of photons (n) /2.

Since the number of photons in each beam is reduced by a factor of two com- pared to the input beam, after the beamsplitter the amplitude of the electric field in each beam is ein/ v'2 where ein is the electric field amplitude at the input. If we say that the beamsplitter has the same effect on the fluctuations of the electric field, namely (8.48)

## NOISE OF A BEAMSPLITTER

utput · m In uc am utput b m a uum flu tu· ti n FIG. 8. 7 Schematic diagram of a beamsplitter.

then for the photon number n' in each of the output beams we would have I (£in± /).f,)2 ~ !(e~ ± 2£· ~C)

(n) ± ,/(n'; n ex v'2 v'2 '"" 2 ex 2 .

(8.49)

However, intuition correctly tells us that the two output beams are in coherent states, for which the fluctuations are J (n) /2, a factor of v'2 Iarger than suggested by Eq. (8.49).

The question is, what is the origin of the extra noise that makes the output states of the light coherent?

The correct argument resolving this issue was first introduced by Caves ( 1980).

Solution Since the incoming light field is in a coherent state with a mean number of photons (n) ex (t:ln), where ei-11 is the input optical electric field, the noise in the beam due to quantum fluctuations is (8.50)

where ~e describes the quantum fluctuations of the input beam (and, as noted in Problem 8.7, is independent of ein)- Because one actually observes that the fluctuations of photon number in the output beams are J (n) /2, consistent with the expected noise for coherent light, the beamsplitter must introduce additional noise into the output beams. This extra noise comes from the dark port of the beamsplitter (Fig. 8.7), where vacuum fluctuations enter. The vacuum fluctuations

## EXPERIMENTAL METHODS

are the same size as the fluctuations in the coherent beam (see Problem 8.7), and are uncorrelated with the input beam fluctuations. The vacuum fluctuations are also divided by v'2 by the beamsplitter. Adding the contributions to the noise in the output beams in quadrature, we find Maut = ✓~: + ~: - (8.51)

Therefore the quantum fluctuations of the electromagnetic field at the input and the output of the beamsplitter are the same: ~tout = ~e. Thus the quantum fluctuations of the photon number are consistent with those for coherent light 9 namely (8.52)

In experiments utilizing squeezed states of light (see Problem 8.7), it is essen- tial to maximize photodetector efficiency. This is because an imperfect detector can be modelled as an ideal photodetector preceded by a beamsplitter. The beam- splitter, as we have seen above, introduces additional noise through the dark pon 9 thereby diminishing the noise reduction obtained by squeezing.

## 8.9 Photon shot noise in polarimetry

A linearly polarized light beam falls onto a polarimeter consisting of an ideal polarizing beamsplitter (PBS) and two I 00%-quantum efficiency photodetectors counting photons at the two outputs of the PBS (Fig. 8.8). Suppose we wish to use the signals from the photodetectors to detennine the angle c.p between the plane of polarization and the axis of the PBS. Express the value of c.p, and its uncertainty 8cp, in terms of the number of photons counted in the detectors (N 1 and N 2, respec- tively, where N 1, N 2 >> 1). Assume the noise in each signal is dominated by shot noise.

Solution The value of cp can be found from the measurement using Malus's law,4 N1 = N sin 2 cp; N2 = N cos2 c.p, (8.53)

4 Malus's law states that, for an ideal linear polarizer (all light with polarization parallel to the polarizer axis is transmitted and all light orthogonally polarized is reflected), the transmitted electric field amplitude is et = e0 cos cp where eo is the amplitude of the incident optical field and <pis the angle between the light polarization and the polarizer axis.

## PHOTON SHOT NOISE IN POLARIMETRY

Polarizing beamsplitter Photodetectors FIG. 8.8 Measurement of the angle cp between the plane of light polarization and the axis of a polarizing beamsplitter.

where N = N 1 + N2 is the total number of detected photons. From Eqs. (8.53), we have: (8.54)

Since N 1 , N 2 >> 1, based on Poissonian statistics, the uncertainties in the num- bers N1, N2 and N are given by the square roots of these numbers. This means that if we perf onn our measurement again under the same conditions, we expect the new measured values of each of the numbers to fall within one standard deviation of the first measurement with a probability of 0.68.

Differentiating Eq. (8.54), we have: 2tancp8cp 8N1N2 - N18N2 ----- N?

cos2 cp (8.55)

Using the fact that 8N 1 = ,/Ni and 8N 2 = ~, Eqs. (8.53), and adding the errors in quadrature, we find from Eq. (8.55): () - cp - 2J"N' (8.56)

i.e., shot noise of the polarimeter is solely detennined by the overall number of detected photons and is independent of the angle cp.

Equation (8.56) represents the so-called standard quantum limit (SQL) for the sensitivity of a polarimetric measurement. In principle, this limit can be overcome by the use of squeezed states of light (as discussed in Problems 8.7 and 8.8); to date, however, squeezed light has not yet found practical application in polarime- try. This situation will, hopefully, change with further development of technologies enabling squeezed light production and high-efficiency light detection.

## EXPERIMENTAL METHODS

It may not be immediately obvious that the shot-noise fluctuations in the two channels are independent. In order to see this, we note that the input beam can be resolved into two coherent beams of opposite polarizati_ons along the two principal axes of the PBS, denoted II and .1. These beams go mto the appropriate output channels of the PBS without attenuation, and moreover, the quantum fluctuations in these two beams are independent. We have for the intensities of the two beams: I.1_ ex: e5 sin 2 'P ± 2eo sin 'P 1).£ .

With this picture, we get consistent expressions for the intensity and quantum fluctuations of the combined beam if we assume the fluctuations are independent and combine them in quadrature: I,01 = h + 111 = e~ ( sin 2 cp + cos2 cp) ± ✓ 4t:ij sin 2 cp ~e + 4t'.ij cos2 cp ~e = e5 ± 2eot).e .

## 8.10 Light-polarization control with a variable retarder

Linearly polarized light goes through a transparent variable retarder whose axis is oriented at an angle o 0 to the axis of the initial light polarization. The variable retarder [ which could be for example, a Pockets or a Kerr cell, a liquid-crystal device, or a photoelastic modulator; see, for instance, Huard ( 1997) or Yariv and Yeh ( 1984)] adds a phase difference 4> between the components of the light electric field parallel and perpendicular to its axis.

Describe the output polarization as a function of 4> as 4> changes between -1r and 1r. Note that when 4> = ±1r and 4> = ±1r /2, the variable retarder acts as a half-wave plate and a quarter-wave plate, respectively. Consider three cases (for which the formulae are very compact): (a) oo << 1, (b) o:o = 1r / 4, and (c) arbitrary o 0 but 4> << 1.

Hint It is helpful to use the Jones calculus described in Appendix D.

LIGHT-POLARIZATION CONTROL WITH A VARIABLE RETARDER ,r ,r ,r cl>= - - cl>= 0 cl>= - cl>= - ~ I I !

,r 2,r 5,r cl>= 2 cl>= - cl>= - cl>= ,r FIG. 8.9 An illustration of the change in light polarization upon propagation through a retarder inducing a phase shift of <I> in the vertical component of the light electric field with respect to the horizontal component. The input light has linear polarization tilted from the horizontal by an angle oo = 1r /16. The polarization ellipses are drawn by tracing the end of the electric field vector as the light phase changes in the range O ~ cp < 21r. Note that, while the ellipticity t is an odd function of cl>, the polarization angle o is an even function of cl>.

Solution (a) Let us say that the projections of the input light electric field on the axes of the retarder are proportional to cos o 0 cos wt ~ cos wt and sin ao cos wt ~ oo cos wt (since a 0 << 1), where wt is the phase of the input light. The two components of the field are often written omitting the cos wt factor in the form of the Jones vector (Appendix D)

(8.57)

At the output of the retarder, we have electric field components given by ( ao:i<I>)

= ( oo cos ~ : ia 0 sin ~) · (S.SS)

For small o 0 this corresponds to elliptical polarization with ellipticity (equal to the arctangent of the ratio of the polarization ellipse's semi-axes) off. ~ no sin cl> rotated by an angle o - no ~ o 0 ( cos cl> - 1) from the initial light polarization (Fig.

8.9).

The Jones matrix M corresponding to the variable retarder (axes along x and y) is evidently (8.59)

,r 4>=--6

## EXPERIMENTAL METHODS

5,r cl>=-6 FIG. 8.10 Same as Fig. 8.9, but the input light has linear polarization tilted from the horizontal by an angle a 0 = 1r / 4. In this case, the principal axis of the polarization ellipse does not rotate. For 4> = 1r /2 (quarter-wave retardation), the output polarization is circular. For 1r /2 < 4- < 3,r /2, the longer semi-axis of the polarization ellipse is perpendicular to the axis of the input polariza- tion. For 4> = 1r, the retarder effectively rotates the input polarization by 1r /2 despite the fact that the principal axes of the ellipse do not rotate at all.

(b) In the case of a 0 = 1r / 4 the Jones vector V' describing the output polarization is given by (8.60)

This case is illustrated in Fig. 8.10. Here one of the principal axes of the polar- ization ellipse always coincides with the initial polarization axis, and the ellipticity is f = ~/2. 5 (c) For small ~, we have (8.61)

and therefore the output polarization is given by V' "-J ( cos ao )

"-J sin ao(l + i~)

· (8.62)

5 Note that ellipticity for circularly polarized light is ±1r / 4.

## LIGHT-POLARIZATION

## CONTROL WITH A VARIABLE RETARDER

What is this state of polarization? It is easy to see if we rotate our frame of reference by -oo (to align the x-axis with the input polarization), then we have ~(-oo).

V' = ( co~oo - Sill Oo sin oo)

( cos oo )

( )

cosoo · sinoo(l + i~)

~ i~ sinoocosoo ' (8.63)

which is evidently elliptically polarized light with major axis along the initial light polarization. Therefore such a phase retarder introduces only ellipticity and causes no rotation.

Variable retarders are very useful in sensitive modulation polarimetry. Suppose we have a sample that introduces small rotation as and ellipticity f.s in the linearly polarized input light, and it is these quantities (as and f.s) that we wish to measure.

The simplest way to do it might be to place the sample between a crossed linear polarizer and analyzer and measure the transmitted intensity that is proportional to a~ + f.~. This method, however, has serious shortcomings. Apart from the fact that it does not provide an independent measurement of Os and f.s or their signs, it is also unsuitable for measuring ellipticities and rotations such that their effect on transmitted light is smaller than the extinction ratio of the polarizer and analyzer (i.e., the ratio of the transmitted and input intensity for a nominally crossed polar- izer and analyzer) which for the best crystalline polarizers is on the order 10- 6 to 10- 7 (Birich et al. 1994).6 Suppose that we place a variable retarder as considered in this problem in series with the sample between the polarizer and analyzer. We choose oo, for example, in such a way that, while o 0 << 1, it is much greater than Os, fs and the square root of the extinction ratio. In this case [using the results of part (a)], we have for the light intensity I transmitted through the analyzer: I~ Io{ (a+ os)2 + (€ + €s)2} ~ Io{ 05 cos2 ~ + 2oo(os cos~+ f.8 sin~)+ 05 sin2 ~} = Io{ 05 + 2oo(os cos~+ f.s sin~)}, (8.64)

(8.65)

(8.66)

where Io is the input intensity. If~ is modulated with frequency n and the output intensity is analyzed with a lock-in detector picking out the component of the signal at a given harmonic (f!, 20, etc.), the value of f.s can be extracted from an odd harmonic (I, 3, etc.) of the signal, while the value of 0 8 can be extracted from an even harmonic. Moreover, limitations due to finite extinction are largely overcome in this arrangement.

6 More precisely, if the signal intensity is much smaller than the intensity of the light transmitted through the analyzer due to finite extinction, the noise is dominated by the latter.

## EXPERIMENTAL METHODS

## 8.11 Pile-up in photon counting

A photon-counting system has N bins per unit time (for example, 256 bins per 1 µs). Assuming that on average n << N photons are detected per µs, and that the photon arrival times are uncorrelated, what is the probability that in a given µs, no more than one photon is detected in each bin (i.e .• there is no pile-up). 7 Solution There are Nn different combinations of how a sequence of n photons can distribute over N bins. If, however, we do not allow a photon to hit a bin that had been hit before, there are only N!/(N - n)! available combinations. Thus, the probability of no pile-up in a given µs is given by: N!

P=----.

(N - n)!Nn (8.67)

This probability drops very quickly with n, which is illustrated in Fig. 8.11 for N == 256. Already for n = 20, there is a ~ 50% chance of two photons hitting the same bin.

7 This problem was inspired by V. E. Matizen.

1, •• • • • • 0.

• 0.6 • • • • • • • • • • • • • • • • 0.2 • • •• ··•-..........._ · IO n FIG. 8.11 Probability that no more than one photon hits each of N = 256 bins as a function of the total number of photons n arriving during a given µs.

## PHOTONS PER MODE IN A LASER BEAM

## 8.12 Photons per mode in a laser beam

Consider a power build-up cavity which is an optical resonator with quality factor Q (Fig. 8.12). Assume that the resonator consists of two identical lossless mir- rors (with finite transmission coefficient), so the transmission of the resonant light through the cavity is unity. Suppose a narrow-band laser (laser linewidth narrower than the cavity linewidth), resonant with the cavity, delivers light power P into the cavity.

Calculate the number of photons n in the cavity. How many photons per mode are there in the output beam?

Solution The energy E inside the cavity, E = nilw, (8.68)

where w is the resonant frequency for the cavity, is governed by the rate equation where w ,=-Q (8.69)

(8.70)

is the cavity linewidth. Thus, in equilibrium, the number of photons in the cavity IS (8.71)

To answer the question of how many photons per mode are there in the output beam, we need to define what we mean by a mode in this case. The definition of a mode can depend on the experimental situation, i.e., the modes of the electromag- netic field in one cavity are not the same as those in a different cavity. For a free, p p FIG. 8.12 Schematic diagram of a power build-up cavity.

## EXPERIMENTAL METHODS

travelling electromagnetic wave, the _length of th~ mode volume is defined by the coherence length le = c/ "Yl where ,, 1s the bandwidth of the output light, which .

the considered case is determined by the bandwidth of the input light (which rr 1. .

can be as narrow as allowed by the Schawlow- 1ownes 1m1t - see Problem 5.2). The flux of photons through a cross-section of the mode is PI hw, and a mode volume passes through this cross section in a time le/ c = 1 / rl. Therefore, the number of photons in a mode of a laser beam is

## 8.13 Tuning dye lasers

p n----nw,,.

(8.72)

For many years, tunable dye lasers8 have been the workhorses of laser spec- troscopy. The gain media for dye lasers are organic molecules dissolved in liquids, which have very broad, continuous fluorescence spectra when excited by visi- ble or UV pump light. 9 Dye molecules which are excited by the pump light to a higher electronic state undergo fast (relaxation times are typically on the order of 10- 11 - 10- 12 s), collision-induced transitions to the lowest vibrational level of the excited state. Thus, for sufficiently intense pump light, the population of the lowest vibrational level of the excited state can exceed that of high-lying vibra- tional levels in the electronic ground state of the dye molecule. This population inversion enables the medium to lase.

In this problem, we discuss various techniques for tuning the frequency of pulsed and cw dye lasers.

(a) In a pulsed dye laser shown schematically in Fig. 8.13, the high reflector in the cavity is a diffraction grating in the Littrow configuration [ where the first-order reflection from the grating is fed back into the cavity, so the grating acts as a wavelength-selective reflector, see Demtroder ( 1996) for details]. Coarse tuning of the output frequency is done by tilting the diffraction grating, while fine tuning is accomplished by changing air pressure in the pressure box from O to 3 atm.

Estimate the fine tuning range of this laser for the output light in the visible. Can you suggest ways to increase this range?

8 Laser action in organic dyes was discovered independently by Sorokin and Lankard ( 1966) and Schafer et al. (1966), and important techniques enabling one to continuously tune the dye laser's frequency were developed by Soffer and McFarland ( 1967) and Hansch ( 1972), among others. See, for example, Duarte and Hillman ( 1990) for a comprehensive discussion of dye lasers.

9 The spectra are broad and continuous due to complete overlap of collisionally broadened spectral lines corresponding to transitions between different rovibronic components of the electronic states

Fabry-Perot etalon / Pr uriz d bo Diffraction grating

## TUNING DYE LASERS

Antireflection coated window Pump light Output mirror ~ FIG. 8.13 Schematic diagram of a pulsed dye laser.

---t> Output light (b) In a continuous wave (cw) dye laser, a narrow bandwidth is achieved by placing selective elements into the cavity: a birefringent (Lyot) filter, a thin glass plate (thin etalon) and a low-finesse Fabry-Perot interferometer (thick etalon). When the transmission peaks of all these elements and that of the cavity coincide, the laser emits light in a single longitudinal mode. In order to smoothly change the laser frequency, it is necessary to simultaneously adjust transmission peaks of the cavity and the selective elements. To achieve a smooth tuning range of the order of several GHz, it is usually sufficient to tune only the cavity and the thick etalon.

This can be accomplished by mounting one of the cavity mirrors and one of the thick etalon mirrors on piezo-mounts which can be moved by applying a voltage, thus changing the cavity length and the thick etalon spacing.

What is the length of the laser cavity and the air space between the thick etalon mirrors if their free spectral ranges (i.e., the spacing between their longitudinal modes) are 400 MHz and 10 GHz, respectively?

What is the necessary displacement of the piezo-mounted elements of the cavity and the thick etalon to tune the laser by 5 GHz?

Solution (a) First of all, note that by putting both the grating and the Fabry-Perot etalon in the same pressure box, one automatically obtains simultaneous and matched of the dye molecules. The collisional broadening results from interaction of the dye molecules with the sol vent.

## EXPERIMENTAL METHODS

tuning of both elements. Constructive interference conditions for the grating .

an the etalon can be wntten as

## KA -L

' (8.73)

where K is an integer and L is an appropriate length. For smooth tuning (i.e. .

h ") h . .

\ d L , ID the absence of frequency " ops , t e quant1t1es K, ~ an are constant and the output frequency change can be found from the relation: C C ( t5n)

v + t5v = (n + 8n)A ~ nA 1 - --:;; ' (8.74)

from which one obtains 18v ~ -v 8n.

(8.75)

Here n is the refractive index of the air in the pressure box (n - 1 ~ 2.8 x IQ-4 for A = 600 nm, and n - 1 is approximately proportional to the density of air under normal atmospheric conditions). For a pressure change of 3 atm and v == 5 x 1014 Hz, the frequency tuning range is ~ 400 GHz, corresponding to ~ 0.5 nm tuning range in the output wavelength. The tuning range may be increased by using a gas with higher refractive index than air, e.g., carbon dioxide (n - I ==

## 4.1 x 10- 4), isobutane (n - 1 = 1.3 x 10- 3), etc

Caution: cases are known where people caused serious damage to their lasers by trying to use gases which chemically reacted with optics coatings.

(b) For the free spectral range we have [assuming a two-mirror nondegenerate ( e.g., nonconfocal) configuration]: so and C tl.v = 2L ' I Lcavity = 37.5 cm I I Leta1on = 1.5 cm· I (8.76)

(8.77)

(8.78)

On resonance, there is an integer number of half-wavelengths in a length of the cavity and etalon: L _ nA _ nc - 2 - 211' (8.79)

where n is an integer number. During smooth frequency tuning, there are no "mode hops" and n remains constant. Therefore, taking the derivative of both sides of

(8. 79), we get: MATTER-WAVE VS. OPTICAL SAGNAC GYROSCOPES 6L L 6v V For 6v = 5 GHz and v = 5 x 1014 Hz(,\ = 600 111n): I '5Lcavily = -3. 75 µm I and I '5Le,alon = -0.15 µm.

## 8.14 Matter-wave vs. optical Sagnac gyroscopes

(8.80)

(8.81)

(8.82)

Consider gyroscopes based on the Sagnac effect (the fringe shift arising due to the rotation of an interferometer [see Figs. 8. I 4(a)-(c)]). Laser gyroscopes based on this principle are commonly used for navigation (for example, on board air- craft), while matter-wave-based gyroscopes of great promise have been recently demonstrated (Gustavson et al. 1997; Gustavson et al. 2000).

(a) Show that the phase shift produced by rotation of the interferometer with angular velocity O is Ll = N41rO-A ¢ AV ' (8.83)

where A is the area vector (a vector normal to the interferometer plane whose magnitude is equal to the enclosed area), ,\ is the wavelength of interfering photons or atoms, v is their propagation speed, and N is the number of times the interfering particles encircle the interferometer (N = 2 for the interferometer sketched in Fig. 8.14(a) and N = I for the interferometer sketched in Fig. 8.14(b).)

(b) Show that the sensitivity of a matter-based device (using particles of mass Af)

is better than that of a photon-based device (with the same area and particle flux)

by a factor ~ 1011.

(8.84)

Why are laser gyros still useful despite this large factor?

(c) Estimate the sensitivity in (rad/s)/ ~, where t(s) is the duration of the measurement in seconds, for a device using Cs atoms with a total flux through the interferometer of 1011 atoms/sec and area A = 20 mm 2.

## EXPERIMENTAL

## METHODS

(a)

On In ---· --- Out -- Out (b)

On In -- -- (c)

In FIG. 8.14 Schematic diagrams of various Sagnac interferometer configurations.

Solution (a) Let us ?rst consider the case o! photons. The Sagnac effect ~an I>«: th00:: of as resultmg from the Doppler shift upon reflection from a movmg mirror (.

Problem 8.1). Light with wave vector k reflecting from a mirror (slowly) movtn~ with velocity Vm experiences a first-order change in the magnitude of the wav vector of (S.85)

where in this case v = c is the speed of light. In the case of a nonrelativistic ~to: moving with velocity v « vm, elementary consideration of elastic scattering ro a moving mirror again leads to the result described by Eq. (8.85).

MATfER-WAVE VS. OPTICAL SAGNAC GYROSCOPES Using the fact that the velocity of a mirror is given by vm = 0 x r, where f is the radius vector of the mirror with respect to the interferometer rotation axis, Eq. (8.85) yields: ... ...

... ...

Ak = Ak . n x r = _ n . Ak x r .

(8.86)

V V ...

Note that no Doppler shift occurs when ~k is in the radial direction. A simple geometry for a Sagnac interferometer is the circular one shown in Fig. 8.14(c), where light is guided about a circle using, for example, a fiber-optic cable. In this setup, the magnitude of the wave vector is only Doppler-shifted at the input and the output. The change in the wave vector magnitude for the part of the wave reflected by the mirror at the input is ...

...

... , ...

I Ak = _ n . (f' _ f) x T = _ n · k x r = _ k nr ~ _ knr ' (8.87)

V V V V where k is the wave vector for the incident light (which is parallel tor, with mag- nitude k) and k' is the wave vector for the reflected light (which is orthogonal to r, with magnitude k' ~ k + ilk), and we ignore tenns to second order in (rO/v).

According to the expression (8.87), as the reflected light beam circulates around the loop, it accumulates a phase shift of magnitude 21r ...

...

A</> = f Ak r d8 = 21rr Ak = 2 kAO = 41rn . A (8.88)

lo .,\v ...

...

due to the rotation n, where fJ is the angle between rand -k.

The light trajectory in interferometers of more complex shape can be thought of in general as consisting of a series of infinitesimal circular arcs and radial regions.

If the light traces out an arbitrary path, we see that the resultant phase shift acquired by the light is given by r21r A</>= Jo Ak(r)r d8 (8.89)

where r is now a function of fJ and ilk(r) = kOr/v as before, only in this case instead of resulting solely from the initial reflection, it is obtained from a series of reflections off mirrors around the light path. Thus we have Ac/> = kn /2'"

r( 8)2 d8 = lAn ' v lo (8.90)

so the resulting phase shift per round trip is still given by Eq. (8.88).

## EXPERIMENTAL METHODS

Note that Eq. (8.90) can also be derived from a quite different perspective_ that of the Feynman path integrals, described in detail in the tutorial article by Storey and Cohen-Tannoudji (1994).

(b) From Equation (8.88), the phase shift is inversely proportional to Av. The deBroglie wavelength Ade is (8.9))

so ~<Patom - AphotonM C -

## M C2

~</Jphoton - 21r/i - liJ.JJ • (8.92)

For photons with frequencies in the visible range and cesium atoms, this ratio is ~ 7 · 1010• Laser gyroscopes remain highly competitive because they benefit from high available fluxes of collimated photons (high particle flux allows for high signal-to- noise ratio), it is easy to make interferometers with large area, and it is possible to make photons go around the interferometer many times (laser gyroscopes using optical fibers have N ,v 106).

(c) In an ideal interferometer, if n particles are detected, the uncertainty in the detennination of phase is ,v n- 112.10 Thus, from Eq. (8.88), we have: AV 80= 41rAJn _ Ii ~ 5 . 10_9 rad/s 2M A y'n Jt{s)

(8.93)

for Cs atoms, atomic flux of 1011 atoms/sec and area A = 20 mm 2• Note that atomic velocity cancels in Eq. (8.93).

## 8.15 Femtosecond laser pulses and frequency combs

In the past several years, revolutionary developments have occurred in the field of laser frequency metrology triggered by the advent of frequency combs.

A frequency comb is generated with an ultrafast laser system producing a peri- odic train of short light pulses (of typical duration ,v 10 - 15 fs; I fs = 10- 15 s).

The spectrum of a frequency comb can span more than an octave, i.e., the fre- quency near the high-frequency edge of the spectrum could be more than twice that at the low-frequency edge. Rather than being continuous, the spectrum of a 10 We assume here that the second-quantized particle wavefunction is a coherent state, so that fluctuations are detennined by shot noise; see Problems 8.7 and 8.9.

FEMTOSECOND LASER PULSES AND FREQUENCY COMBS c;mb consi sts of sharp equidistant peaks. Precisely controlling the positions of t ese peaks, one obtains a "frequency ruler" by which any frequency within the span of ~he comb can be precisely measured.

In this problem, we explore some of the most basic ideas behind the frequency comb technology. Both highly accessible, for example Udem et al. (2002) and Hall et al. (~00 I), and more technical review articles, for example Cundiff et al. (200 I), are available that cover this exciting area of research.

(a) _Suppose _a laser is producing a train of pulses such that the light intensity at a given spatial location in the laser beam (for example, at the output mirror) is exactly periodic in time.

. Show that the output consists of a set of sharp peaks whose frequencies are given by fn = nfr + Jo- (8.94)

~ere fr is t~e pulse repetition rate (typically, 108 Hz < fr < 109 Hz), n is an mte~er (typically, n "' 106), and Jo is the offset frequency which by a proper choice of n can be constrained by 0 < /o < fr.

Equation (8.94) shows that in order to control the absolute frequencies of the comb components, it is necessary to independently control the frequencies Ir and /o. We discuss how this is done in the next part of the problem.

(b) A schematic of one possible ultrafast laser configuration used to produce frequency combs is shown in Fig. 8.15. The gain medium is a titanium-doped sapphire crystal (Ti:sapphire) that is optically pumped by a cw laser (typically, A= 514 or 532 nm). The gain of Ti:sapphire spans a broad spectral range between approximately 700 and 1000 nm. The resonator configuration is a bow-tie-shaped four-mirror standing wave cavity with an important additional element - a prism pair - whose role we will discuss shortly.

Looking at Fig. 8.15, one might wonder why is this laser pulsed rather than cw? The trick is a beautiful technique of Kerr Jens mode-locking (KLM) invented in the early 1990s. The idea is that for Ti:sapphire, as for most other materials, the refractive index depends on the intensity of the light (this is a variety of the Kerr effect; see Problem 4.2): (8.95)

where no is the intensity-independent (linear) index, and n 2/ is the nonlinear part.

Because n2 is usually positive, the light "sees" a higher refractive index where the intensity is higher. In particular, for a Gaussian transverse spatial beam profile, the medium becomes a focusing lens. The resonator is aligned so that at low intensity (where Kerr lensing is negligible), cavity losses are high, while at sufficiently high intensity (as in a short pulse), Kerr lensing greatly reduces cavity losses. Thus, with sufficiently powerful pumping, the laser will generate a train of pulses. The pulse periodicity is given by the cavity round trip time. In the spectral domain, this

## EXPERIMENTAL METHODS

Pump Laser Ti:Sapphire Crystal FIG. 8.15 A schematic of an ultrafast Ti:sapphire laser. Self-mode-locking occurs due to the Ker- r-lensing effect which ensures that the cavity has lowest losses for highest light intensity, i.e., the shonest pulses. Translation and tilt of the cavity mirrors and changing the pump power are used to control the frequency of the comb components.

corresponds to a large number of longitudinal cavity modes, all oscillating with a definite phase relative to each other [hence the term mode-locking; see Siegman ( 1986) for an excellent in-depth introduction]. In this picture, the pulse repetition frequency is the beat frequency between adjacent modes.

The prism pair is introduced in the cavity in order to compensate for the effect of group velocity dispersion (GVD) - the difference in group velocity for light of different colors - that tends to broaden the duration of a pulse. The prisms are designed to make the total path length slightly longer for light of longer wavelengths, thus compensating for GVD.

The subject of this part of the problem is achieving control over both of the frequencies fr and Jo in Eq. (8.94). The repetition rate fr is controlled by small translations of one of the mirrors (Fig. 8.15).

What is the change in Jr when a mirror is translated by an amount ~L? Show that there is also a significant change in the comb's peak frequencies, and that, in fact, to a first approximation, the peaks move in frequency together and the separation between adjacent peaks remains constant.

This shows that another degree of freedom is needed to compensate for the frequency shift introduced by the mirror translation and to address the offset fre- quency f o- There are several ways to do it (see Fig. 8.15) including rotating the high reflector mirror (which changes the length of the prism material through which light travels, and thus changes the dispersion), and changing the power of the pump light (which changes the dispersion of the Ti:sapphire crystal).

These degrees of freedom allow one to control both fr and Jo (as they do not affect the average phase and group velocity of the light in the same way) but, unfortunately, they do not provide "orthogonal" access to these parameters. Details can be found in Hall et al. (200 I ).

FEMTOSECOND LASER PULSES AND FREQUENCY COMBS (c) In the previous Part of the problem, we have discussed how to produce a fre- quency ~omb and how to adjust each of its two fundamental frequencies fr and /o. _In th1s. Part of the problem, we discuss how to measure these parameters. Mea- su~m~ Ir is straightforward and can be done by counting the number of pulses per umt time. The access to Jo is more difficult, unless the comb spans more than an octave. ~ere we will discuss the latter case after we briefly digress to describe the product1~n of the octave-spanning combs .

. The direct output of an ultrafast Ti:sapphire laser has a typical fractional band- width of 8v Iv ~ 0.2, so it does not span an octave. Fortunately, there are methods that allow one to broaden the spectrum. The idea is that if light is passing through a phase modulator, each of the spectral components acquires sidebands separated from the original component by integer multiples of the modulation frequency (see Problem 8.3). Because an ultrashort light pulse propagating in a material produces strong self-modulation due to the intensity dependence of the refractive index, a very significant broadening can be achieved. In order to provide large light inten- sity and a long interaction length to enhance the nonlinear self-modulation effect one can use an optical fiber. I I A broader comb is generated by sending the output of an ultrafast Ti:sapphire laser through such a fiber. It is also possible to broaden the spectrum by inserting intracavity elements to introduce self-phase modulation and using special mirrors that compensate for the introduced GVD.

Now to the question. Show that if a frequency comb spans an octave, it is pos- sible to measure the offset frequency Jo by measuring the beat frequency between a frequency-doubled comb component near the low-frequency edge of the comb with the closest component near the high-frequency edge. 12 Solution (a) If the intensity of the light is periodic, i.e., I(t) = I(t +Tr), where Tr = 1/ fr is the period, then since I = ee•, the electric field e of the light also has to be periodic, however only up to a phase: (8.96)

or more generally, (8.97)

11 A limiting factor in this case could be GVD that acts to spread the pulse and reduce the in~ensity.

An excellent solution is offered by photonic crystal optical fibers which give small mode size and small GVD. Such fibers consist of a silica core surrounded by a pattern of small air holes.

12 In practice it is not necessary to select an individual low-frequency component. Sending t~e low- frequency part of the comb (selected with a dichroic mirror) onto a nonlinear crystal, one obtains not only frequency-doubled components, but also components at sum frequ~ncies (see Problem 8.4).

Each of these beats with a corresponding close-by component from the high-frequency part of the comb with the same beat frequency.

## EXPERIMENTAL METHODS

where k is an integer.

It is convenient to introduce a time-de"':ndent e!ectric field associated With 8 single pulse, e1 (t). In general, this field rapidly oscillates at the central or cllrrier light frequency.

The field of the entire pulse train is t:(t) = L t'.1(t - krr)eik.p • k We are now ready to evaluate the spectrum of the pulse train by talcing the FOUrier transform of the time-dependent electric field: e(w) = j L t:1(t - krr)ik'{)e-iwtdt (8.99)

-oo k = Leik'{)loo ei(t')e-iwt'e-iwkTrdt' = (Leik'{)-iwkrr)e1(w), k -oo k (8.100)

where to obtain the second equality we used t' = t - krr.

When a large number of terms is summed in Eq. (8.100), the result general)y averages to zero. However, if the contributions from different pulses (i.e. different values of k) add in phase, there appears a peak in the spectrum. This occurs when WTr - <{) = 21rn, (8. IOJ)

which can be rewritten as 21r 'P Wn = -n+-, Tr Tr (8.102)

yielding Eq. (8.94) upon division by 21r.

We see that the offset frequency /o = c.p/(21rTr) is related to the phase slippage between the electric field and its envelope that determines the intensity. This is called the carrier-envelope phase.

(b) A translation of a mirror by a small amount D.L changes the frequency of each cavity mode Ve by t:.L ~II ~ --II C L c, (8.103)

where L is the total effective length of the cavity. To first order, adjacent modes change in frequency by the same amount, so the mode pattern shifts as a whole.

This translates into a frequency shift of the comb.

MAGNETIC FIELD FLUCTUATIONS DUE TO RANDOM THERMAL CURRENTS The change in the repetition rate can either be calculated by taking the next order of approxi 1· · )\ .

ma 10n m uL/ L compared to Eq. (8.103), or directly from 2L L Tr= - ~ 2-.

(8.104)

Vg C Here Vg is the average group velocity and the factor of 2 appears because a pulse travels the length of the cavity twice in a round trip. From Eq. (8.104 ), we see that the change of the repetition frequency due to mirror translation is (8. I 05)

As a numerical example, for a laser with Jr = 100 MHz, and for ~L = 1 µm, ~e have 8/r ~ -70 Hz, while from Eq. (8.103), the shift of the comb as a whole 1s ~ -250 MHz.

(c) Let us say that we pick out a comb component at the low-frequency end of the comb spectrum with some value of n (see Eq. (8.94)]. If we double the frequency of this component, we get light with frequency 2n/r+2/ 0• Now ifwe interfere this light with a comb component in its high-frequency edge with frequency 2n/ r + lo (for example, combining the light beams on a photodetector), the resulting intensity will have a beat note at the difference frequency 2nJ r + 2/o - 2nJ r - Jo = Jo.

Thus, it is easy to directly measure the offset frequency if a comb spans an octave. There are also other methods of measuring Jo and the envelope-carrier phase that involve delaying a light pulse and interfering it with a subsequent pulse in the train of pulses (Jones et al. 2000).

8.16 Magnetic field fluctuations due to random thermal currents Estimate the r.m.s. magnitude of the magnetic induction at a distance a from a large (transverse dimensions>> a) thin (thickness 8 << a) sheet of metal of conductivity a. Assume that the metal sheet is at finite temperature T.

Make numerical estimates for aluminum at room temperature, a = 10 cm, 6 = 0.1 cm (the resistivity of aluminum is p(Al) ~ 2.42 x 10- 6 n · c1n). What is the frequency dependence of the fluctuating field? What changes in these results if the metal is of high magnetic permeability (e.g., a magnetic shielding material such as a CO-NETIC alloy with µ rv 105)?

The fluctuating magnetic fields from conductors have been analyzed in the con- text of applications of ultrasensitive magnetometry to biomagnetism (Nenonen et

## EXPERIMENTAL METHODS

al. 1996; Kominis et al. 2003) and the searches for a pennanent electric-dipole moment (Lamoreaux 1999).

Hint According to the Nyquist theorem [see, for example, Kittel and Kroemer ( 1980)]~ the voltage noise across a resistor R (commonly referred to as Johnson noise) is given by (8.106)

where k 8 is the Boltzmann constant and~/ is the measurement bandwidth [6./ = C /r where r is the measurement time and C is a numerical constant (usually 1 < C < 21r, depending on the details of the frequency response of the measurement device)].

Solution We will argue that the magnetic noise can be estimated by considering the pan of the sheet with transverse dimensions rv a in the vicinity of where the magnetic field is measured. We first note that the resistance associated with a region of transverse dimensions l"V b >> 6 is actually approximately independent of b and can be estimated as R l"V p / 6, where p is the resistivity of the metal.

The current arising due to the Johnson noise voltage (8.106) is thus 4kBT~f 4kBT~f6 (/) = R ~ P .

(8.107)

Since the current is distributed over the part of the metal sheet of typical dimensions rv b, it produces a magnetic field such that 2(/2)b2 (B2) l"V ---c2(b4 + r4) .

(8.108)

We have constructed the expression (8.108) in such a way that (B2) rv (/ 2) / ( cb )2 over a region of space with spatial extent l"V b, and dropping off as the fourth power of the distance at distances r >> b, corresponding to the usual form of the field from an element of current.

From this argument, we see that if we choose b << a, in order to calculate the magnetic field from a region of dimensions l"V a, we need to sum rv (a/b) 2 con- tributions to B 2, which adds up to the same result as for one region of dimensions l"V a. The region of the sheet outside this region does not contribute much because the field from each small region of dimensions l"V b with a given current scales as the inverse square of the distance, and thus its contribution to (B2) scales as the

MAGNETIC FIELD FLUCTUATIONS DUE TO RANDOM THERMAL CURRENTS inhverse fourth power of the distance, while the number of regions scales only as t e square of the distance.

We thus arrive at the estimate of the magnetic field noise: (8.109)

Alth0ugh we have carried out a very crude order of magnitude estimate, the result <8: 1 ~) reproduces the actual scaling of the effect, and the numerical coefficient is withm a factor~ 2 [see Nenonen (1996) and references therein].

Putting in the numbers: p(Al) ~ 2.42 -10- 6 n. cm, 1 n = 1/(9 x 1011) s/cm, T = 300 K, we get from Eq. (8.109): 6B = vlfifi} ~ 5 X 10-lO ~../M.

vHz (8.1 I 0)

. ~ote that the magnetic field noise is independent of frequency (white noise)

w1thm the approximations that we have used to derive Eq. (8.109).

In the above consideration, we have neglected currents induced in the metal by the changing magnetic field and the magnetic fields induced by these cur- rents (static approximation). Such currents are not negligible, however, at high frequencies.

Suppose we have some magnetic field of amplitude B changing with a fre- quency 21r I that pierces our region of the metal sheet of transverse dimensions ,......, a. The electromotive force induced by the changing flux is V 21rf Ba 2 .

emf rv , (8.111)

C the induced current is /ind ~ Vemf ~ 271" / Ba26 , R cp (8.112)

and the magnetic field induced by this current is B'~21rfB6a_ (8.113)

c2p The cut-off frequency above which the induced currents will tend to significantly reduce magnetic field fluctuations can be estimated by setting B' ,......, B: J* rv C p .

(8.1 I 4)

21r6a For our numerical example, /* ,......, 400 Hz. Note that at the frequency cut-off (8.114), for nonmagnetic materials(µ = 1), the skin depth given by [see, for

## EXPERIMENTAL METHODS

example, Problem 8.2): 21r(21r /)µ (8.115)

is ()s rv ✓a()/ (21r) >> ().

Returning to the static limit, a question regarding high-permeability materials is whether the magnetic field generated within the conductor will be shielded by the material itself [as suggested by Lamoreaux (1999)]? Although the specific relation of internal currents to magnetic fields outside the ~aterial is geometry dependent~ we can show that in general such currents are not shielded, by considering a simple example.

Imagine a linear current / flow_ing ~~all~I to the surf ace within the high- permeability material (which, for s1m~hc1ty, 1s as~umed to fill half the space); we wish to find the magnetic field outside the matenal. The solution of this prob- lem is well known [see, for example, Batygin et al. ( 1978) or Jackson (1975)]: the magnetic field outside the material is equivalent to that of a current of magnitude I'= 2µ I::::::: 2/ µ+1 (8.116)

flowing at the same location as the current I in the absence of the high-penneability material.

Thus, the field from the current is not generally shielded (it is actually enhanced in our example above); however, the presence of the high permeability material certainly changes the details of the field distribution.

The effect discussed in this problem actually has important consequences for the manipulation of Bose-Einstein condensates near the surface of microchips (Henkel et al. 2003), as thermal currents can create magnetic fields which depolarize the condensates (see Problem 2.8).

## 8.17 Photodiodes and circuits (T)

Photodiodes are perhaps the most common light detectors in a modem optical lab- oratory. They are used in a very broad variety of measurements ranging from those of intense light (laser beams) to those of weak light (laser-induced fluorescence), and from measurements of slow-varying signals (light power meters) to those of very fast signals (short laser or fluorescence pulses, beat notes between different laser fields). In the latter case, time resolution of small-area photodiode detectors can be as good as several picoseconds.

13 This is in disagreement with a statement in the paper by Lamoreaux ( 1999).

PHOfODIODES AND CIRCUITS (T)

TABLE 8.1 Som e representative room-temperature characteristics of a large-area silicon photodi- ode.

Parameter Active area Spectral response range Quantum efficiency (peak)

Maximum reverse-bias voltage, Vb Dark current (Vb= 10 mV)

Capacitance, C Shunt resistance, Rsh Series resistance, Rs Typical value I0mmxl0mm 190 nm to I 100 nm 85 % 5-30 V

## 0.2 nA (approx. ex active area)

1000 pF 200 Mfl 200 n In this tutorial, we will discuss some of the basic characteristics of photodiodes (Table 8.1 ), the common electrical circuits used in applications, and the fundamen- tal noise sources and limitations of photodiode-based light detectors. Additional in-depth information on the subject can be found in a book by Donati (2000), as well as in technical literature available from the photodiode manufacturers, for example, Hamamatsu (http://www.hama-comp.com/).

A photodiode is a semiconductor junction that acts as a regular diode in the absence of light. When light is absorbed in the photocliode, it creates electron- hole pairs. The quantum efficiency of this process, under favorable circumstances, may approach unity, i.e., there is one electron-hole pair created per each photon absorbed in the photocliode.

In order to detect these free charges created by light, one can put a load resistor RL across the output terminals of the diode (Fig. 8.16), and measure the resulting voltage. This is the so-called photovoltaic mode of operation.

(a) Assuming an 85% quantum efficiency, and the value of load resistor RL = 10 kfl, what are the output current and voltage for the power P = 1 µW of incident light with ,,\ = 650 nm?

Solution This light power corresponds to~ 3 x 1012 photons/s (see Appendix A), and, cor- respondingly, to~ 2.5 x 1012 electron-hole pairs created per second. The electrons and holes flow towards each other (and eventually recombine) causing the current through the load resistor of i ~ 2.5 x 1012 s- 1 x 1.6 x 10- 19 C ~ 0.4 µA, (8.117)

## EXPERIMENTAL METHODS

a)

b)

R A lph R h .,., c)

b d)

~ • ~ R' ~~ Out ~~ ~ Out -- + RL FIG. 8-16 (a) Symbolic representation of a photodiode. (b) A simplified equivalent circuit; Rsh ancl Ra are the shunt and series resistors, respectively. (c) A simple circuit with reverse-biasing of the photodiode; RL is the load resistor. (d) Operational amplifier circuit.

and a corresponding output voltage of I V = iRL ~ 4 m V.

(8.118)

In technical literature, the sensitivity of photodiodes to light at a partic~lar wavelength is often given in terms of photodiode current per unit light power, i.e., in units of A/W. In our case, from Eq. (8.117), we see that the sensitivity is abollt

## 0.4 A/W

While photovoltaic operation as we have just discussed can sometimes be useful, there are also various drawbacks. Firstly, the output voltage is linearly dependent on the incident light power only for low powers where the output volt- age is much smaller than the intrinsic forward voltage drop of the photodiode [see, for example, Horowitz and Hill (1989)], ~ 0.7 V for silicon diodes. A convenient way of thinking about this is to imagine the photodiode as an idealized diode (a device that conducts when forward biased, and represents an open circuit when reverse-biased) reverse-biased by an intrinsic voltage source of ~ 0. 7 V in series with the diode. Clearly, the output voltage is limited by the bias-voltage value.

PHaroDIODES AND CIRCUITS (T)

. This limitation can be easily mitigated by introducing an external bias and usmg the photodiode in the photoconductive mode as shown in Fig. 8.16(c). Here the output is essentially limited by the bias voltage.

It turns out that reverse biasing the photodiode has an additional advantage where fast response of the detector to time-varying light power is desired. Before we discuss this, let us figure out ...

(b) What is the output voltage corresponding to the photocurrent I ph oscillating at a frequency w and what is the bandwidth of the circuit shown in Fig. 8.16( c)

assuming that the input impedance of whatever device we use to measure the out- ~ut voltage is infinite, and that the bandwidth is limited by the elements in the idealized schematics of Figs. 8. I 6(b) and 8.16( c )? Assume that Rsh is infinitely large.

Solution Looking at Figs. 8.16 (b) and 8.16 ( c ), we see that the situation corresponds to a driven RC-circuit, and it is straightforward to derive that (8.119)

At zero frequency, the entire photocurrent flows through the load resistor. As the frequency increases, some of the photocurrent is shunted by the capacitance C • The bandwidth is traditionally defined as the frequency where the signal amplitude drops by a factor of \/'2. This level is also referred to as the 3-dB high-frequency cutoff because 20 log( v'2) ~ 3. From Eq. (8.119), we see that the so-defined bandwidth expressed in Hz, B, is I B = 21r(RL ~ Rs}C · I (8.120)

Now we are prepared to appreciate the additional advantage of reverse-biasing the diode. It turns out that the capacitance of the diode C decreases with the increase of the bias voltage. (Physically, this is because the width of the depleted area in the semiconductor junction increases with the reverse-bias voltage.) Thus, biasing the diode increases the bandwidth of the photodetector. A drawback of biasing the photodiode is that the dark current increases with the reverse-bias volt- age. Note that the exact dependences of the capacitance and dark current on the bias voltage vary between different diode types, so we only mention the trends here, and the reader should consult the manufacturer's data sheets for quantitative information.

## EXPERIMENTAL METHODS

Next, we tum to the discussion of various noise sources associated With measurements using photodiodes.

A fundamental contribution comes from the shot noise and is associated With discreteness of charges. If we perform a measurement with a nominally constant current I for a time t, the charge associated with this current is It, which cor- responds to N = It/ e elementary charges flowing through a cross-section of a conductor. Assuming that these charges are uncorrelated with each other, from Poissonian statistics, we can expect that the variance of this number is ( ~ N)

2 == N.

The r.m.s. deviation of the number of charges is then ./ff/e, which corresponds to the square of the shot-noise current of el /shot = f • (8.121)

Note that this quantity scales inversely proportional to the measurement time t. As long as the fluctuations at different points in time are independent, this is white noise whose spectral power density is independent of frequency. Equation (8.121)

is usually written in the form (8.122)

where the measurement ban~width ~/ is associated with the measurement time according to ~/ = 1/(2t). In analyzing circuits with current sources, the associated noise current source should be added to the original source.

The other important noise contribution comes from the thermal (Johnson) noise of the resistors. For a resistor R, the noise voltage squared is VJohnson 2 = 4kTR~f.

(8.123)

In an equivalent circuit, the noise voltage source appears in series with the corre- sponding resistor. We remark in passing that while there is thermal noise associated with resistors, there is none associated with capacitors or inductors. This is related to the general .fluctuation-dissipation theorem, see, for example the book by Reif (1965).

(c) What is the output noise of the circuit shown in Fig. 8.16(c)?

Solution As long as various noise sources are independent, they should be added in quadra- ture. Including the noise current sources due to the photo- and dark currents, and the Johnson noise of the resistors, after straightforward circuit analysis, we arrive

at (Vout 2)noise = PHOfODIODES AND CIRCUITS (T)

2e(/ph + Id)~f R'i (4kTRL~f)

1 + w2 (RL + R 8 ) 2C 2 + 1 + w2RLC 2 + (4kTRsh~f)R't(I +w 2R.h2C2)

(RL + Rsh)2 + w2Rsh2C2(RL + Rsh)2 + (4kTR 8~f)Rlw 2C 2 1 +(Rs+ RL)2w2C2 .

(8.124)

Here the first tenn describes the shot noise, while the other three terms describe contributions from the Johnson noise of the load, shunt, and series resistances, respectively; w = 21r f is the angular frequency at which the measurement is performed (with bandwidth ~/).

In deriving Eq. (8.124), we have assumed Rs << Rsh, as in all practical cases, and we also neglected the influence of the shunt resistance on the shot-noise tenn.

Now that we have expressions (8.119) and (8.124) for the signal and noise of the photocliocle circuit of Fig. 8.16( c ), we are ready to discuss under what circumstances this simple circuit is adequate for a given measurement task.

(d) Suppose we are interested in measuring light signals with a bandwidth B = 1 kHz with a photocliode with the characteristics given in Table 8.1 and the circuit of Fig. 8.16(c). Determine the appropriate value of the load resistance RL- Show that the Johnson noise of the load resistor dominates the other noise contributions in the absence of the light. Calculate the light power at which the shot noise of the photocurrent is roughly equal to the thermal noise of the load resistor. This gives a rough idea of the range of light powers where this simple circuit is adequate.

Solution The desired bandwidth determines the value of RL according to Eq. (8.120): RL ~ 21rCB ~ 160 kf2.

(8.125)

Using this value of RL, we find that the square of the output noise voltage due to the Johnson noise of the load resistor [Eq. (8.124)] is~ (1 µV) 2 where we assume the resistor is at room temperature, and set fl/ = B, w rv 21r B.

Substituting numerical values into the first tenn of Eq. (8.124 ), we find that the corresponding number for the dark-current shot noise is much smaller, ~ (3 x 10- 8 V)2• The Johnson noise contributions to the square of the output noise voltage from the shunt and the series resistance are found to be RL/ Rsh and

## EXPERIMENTAL METHODS

Rs/ RL times smaller than the contribution from the_ lo~d re~istor. Thus. indeed, the load resistor is the principal source of the dark nmse m this situation.

The photocurrent for which its shot noise is equal to the Johnson noise of th load resistor is found by equating the first two terms in Eq. (8.124 ): e 2kT / ph = - ~ 0.3 µA .

eRL (8.126)

This corresponds to rv 1012 photons impinging on the photodiode per second, or rv 0. 7 µ W of red (A = 650 nm) light power.

Finally, we briefly consider an improved photodiode circuit using an opera- tional amplifier (op-amp) shown in Fig. 8.16 ( d) that allows one to overcome some of the bandwidth and noise limitations of the simple circuit we have considered so far. A detailed treatment of photodiode amplifiers is given by Graeme ( 1996).

An op-amp is a high-gain (typically, 105 - 106) differential amplifier shown in Fig. 8.16(d) as a triangle with two inputs and an output (at the right venex).

One of the inputs of the op-amp is inverting (marked with a"-"), and the other one is non-inverting (marked with "+"). The output of the op-amp is connected , via a resistor R' to the inverting input, forming a negative feedback loop. In most practical cases, the operation of an op-amp with feedback can be analyzed using the two idealized golden rules (Horowitz and Hill, 1989, Chap. 4.03 ): I . The output attempts to do whatever is necessary to make the voltage difference between the inputs zero.

## 2. The inputs draw no current

Let us apply these rules to the circuit of Fig. 8.16( d). According to the first rule, the photodiode sees zero voltage at its terminal connected to the op-amp, so the load resistance is effectively zero. What happens to the photodiode's current?

Because, according to the second rule, the input of the op-amp draws no current, the current exactly equal and opposite to that of the photodiode has to be supplied by the output through the feedback restor R', so the output voltage is essentially (8.127)

There is also a great improvement in bandwidth associated with elimination of the load resistor RL. In fact, achieving high bandwidth while maintaining a large conversion coefficient between the photodiode current and the output voltage is the main purpose of the op-amp circuit. Note that integrated photodiode/op-amp packages are widely available commercially.

Next, we ...

( e) Discuss the noise properties of the op-amp circuit of Fig. 8.16( d).

Solution PHOTODIODES AND CIRCUITS (T)

First, we note that with the op-amp feedback arrangement, the Johnson noise of !he feedback resistor appears at the output essentially without modification. This is a co~sequence of the two golden rules. In the case of an op-amp circuit, it is convenient to recalculate all noise sources as effective photodiode noise current.

Fo~ the Johnson noise of the feedback resistor, we just need to divide the output noise voltage by R'.

ReP<:ating the analysis of the noise sources along the lines that led us to Eq.

<8-124) m the low-frequency limit, we obtain for the effective input noise current: (Ji/)noisc = 2e(Jph +Id)~/+ 4kT~f (~, + ~) · (8.128)

Fo~ low-light applications where large feedback resistor is desired, the Johnson noise of the shunt resistor emerges as the principal noise source (besides the shot ?oise). In analogy with Eq. (8.126), we find that the photodiode op-amp circuit 18 adequate for detecting photon fluxes of down to ~ 109 photons per second for R' ~ Rsh.

A significant improvement in the noise characteristics can be achieved by cool- ing the photodiode as the shunt resistance increases as the temperature is decreased (typically, by an order of magnitude for cooling the diode by 20 degrees).

In this brief tutorial, we have not discussed issues like the effect of non-ideal op-amps, bandwidth limitations due to the detailed physics of the semiconductor junction, imperfections due to stray capacitance of the photodiode package and leads, the effect of the measurement devices and cables used to connect them, etc.

However, we hope that what we have discussed is a good start in understanding photodiodes.

## MISCELLANEOUS TOPICS

## 9.1 Precession of a compass needle?

If a paramagnetic atom is oriented in a direction which is not collinear with the direction of an applied magnetic field, the magnetic moment of the atom precesses around the direction of the magnetic field at the Larmor frequency nL. For a needle of a magnetic compass, a very different behavior is usually observed. Assuming tbat the needle can freely rotate around its central pivot point, once released at rest at ~n angle to the magnetic field, the needle will undergo oscillations with respect to Its equilibrium orientation (where the needle's magnetic moment is aligned with the field). Explain the difference in the behavior of these two systems. Is it possible to create conditions where the needle will precess around the magnetic field?

Solution The difference in the behavior of the two systems is due to the difference in the relations between magnetic moments and angular momenta.

_ For an atom, the magnetic moment µ and the total angular momentum F are related through µ = ,F, (9.1)

where , rv µo is the gyromagnetic ratio. The angular momentum evolves due_ to the torque produced by the interaction of the magnetic moment with the applied field: dF - - - - = j1 X B = ,F X B' dt (9.2)

where we have set Ii = l. The solution of this equation gives the rotation of the vector F around B with angular velocity (9.3)

Let us now tum to the case of the needle. Assuming that the needle is magne- tized along its axis (magnetic moment density M), the total magnetic moment of

## MISCELLANEOUS TOPICS

the needle is - 2lM"

µn = 1rr n, (9.4)

where f,, is the unit vector along the needle's axis and we have assumed a sim 1 cylindrical shape (radius r and length l).

P e For common ferR?magnetic materials_ (e.~ .• ir~n), the total effective angular momentum per atom 1s on the order of umty (m umts of Ii), and a typical effecf gyromagnetic ratio is "f ~ 2µ0 [see, for example, Kittel (2005)). Thus, the ratio•v~ the magnetic moment of a magnetized ferromagnetic object to its intrinsic angul: momentum Lo is similar to that of a free atom.

However, a crucial difference between a free atom and a magnetized needle is that precession of the angular momentum of a free atom does not cause mechanical motion of the nucleus. For a needle, on the other hand, because the magnetic moment is "locked" to the crystalline lattice, its evolution in the magnetic field is coupled to the macroscopic motion of the needle.

Sup~se. for example, that the needle is rotating with an instantaneous angular velocity n around an axis perpendicular to the needle's axis and going through its center. The mechanical angular momentum associated with this rotation is 2z3 .... n 1rr P n L=lu= --u. 12 (9.5)

Here I is the moment of inertia and p is the mass density of the needle.

Let us estimate the magnitude IOI corresponding to 1£1 ~ Lo (which we des- ignate 0*). From the fact that each atom carries~ Ii of angular momentum, we have Lo ~ 1rr2l_f!_li, ma (9.6)

where ma is the mass of an atom, and p/ma is the number of atoms per unit volume. Comparing Eqs. (9.5) and (9.6), we have: * 12/i 12 x 10- 27 erg • s n ~ -- ~ ------------- ~ 1 s- 1 (9 7)

mal 2 56 x {1.7 x 10- 24 g) x (0.01 cm) 2 ' • where we have substituted numbers for a 0.01 cm-long iron needle.

One can identify two limiting cases in the motion of the needle. For IOI > > n•, the intrinsic angular momentum of the needle ca!! be neglected and the needle behaves in its usual way. On the other hand, when IOI < < n•, the intrinsic angular momentum dominates and the needle will be precessing (just like an atom) with the Larmor frequency. From Eq. (9.3), one estimates that a needle with the chosen dimensions will be precessing as long as B << 10- 7 G. It is possible to create such small well-controlled magnetic fields in a laboratory using high-quality magnetic shielding.

## ULTRACOLD NEUTRON POLARIZER

. A di~ec~ an~logy exists between this system and the familiar top with a fixed pivot spmnmg m a gravitational field. As long as the top spins sufficiently fast, it p~esses ar?und the vertical direction. However, if the spinning is slow, the top flips to the side, and no precession is observed.

## 9.2 Ultracold neutron polarizer

A key development in the study of neutrons has been the ability to confine them in "bottles" for times limited only by their beta decay (r ::::::: 900 s). The bottles, consisting of either matter or a magnetic field, are able to confine ultracold neu- trons (UCN) - those with thennal energies less than the potential barrier created by the material or a magnetic field [see Golub et al. ( 1991) for a detailed review of UCN technology and applications]. Such UCN are totally reflected at any angle of incidence to the bottle walls. Present experiments at the Institut Laue-Langevin in Grenoble, France and the St. Petersburg Institute of Nuclear Physics in Gatchina, Russia extract such UCN from the low-energy tail of the Maxwell distribution of neutrons ejected from a relatively cold (T rv 20 K) source. Ultracold neutrons can also be produced in even greater densities by inelastic scattering of cold neutrons in superfluid 4He [Ageron et al. ( 1978), Golub et al. ( 1983), Golub et al. ( 1991 ), and Huffman et al. (2000)).

Consider ultracold neutrons (UCN) with energy rv 10- 7 eV impinging on a layer of magnetized material with magnetic field B inside the material (see Fig. 9.1 ).

(a) Neglecting edge effects, what is the magnetic induction Bo outside the material?

(b) Calculate the minimum value of B necessary for this system to work as a UCN spin polarizer (i.e., transmitting neutrons with one polarization and reflecting those with the opposite polarization).

Ultracold neutrons ~ B +-.-.

.... _.++-+++++++ FIG. 9.1 A magnetized material can act as a polarizer for UCN.

Solution

## MISCELLANEOUS TOPICS

(a) Neglecting the edge effects is equivalent to treating the uniformly magneti~ material as a plate of infinite extent. Since the magnetic field inside the matenal is uniform, it can be described as a result of "bound" surface currents on the top and bottom of the plate, propagating in opposite directions. Such currents prod~ce uniform magnetic fields parallel to the surf ace and perpendicµlar to the directl;° of the current. Inside the material, the fields from these currents add to produce ' while outside the material they cancel, so (b) Inside the magnetized material, the energies of neutrons with spins o~ent1 alo?g or op~sit~ to the magnetic field are different becau~ of the interacuon S their magnetic dipole moments i4i with the magnetic field B. The total energY of a UCN is given by E = K-µn · B, (9.8)

where K is the UCN kinetic energy.

.

When the total energy of a UCN of the "wrong" polarization is negauve <.

K , ...

...

b the i.e., < ~ · Bl), neutrons of the wrong polarization are reflected Y t potential barrier. Given that K ~ 10- 7 e V and the neutron magnetic mome~ ~ = 9nµN /2 ~ 6 x 10- 12 eV/G (where 1/2 is the neutron spin, 9n ~ - 3·8 15 the Lande factor for the neutron, and µN ~ 3 x 10-12 eV/G is the nuclear ma~ne- !0n), the necessary magnetic induction for the plate to act as a UCN spin palanzer 1s: ' B ~ 1.1 X 10 4 G' I a value readily achieved with common ferromagnetic materials.

## 9.3 Exponentially growing/decaying harmonic field

The power spectrum of an exponentially decaying harmonically oscillating field is Lorentzian (for example, this is the case for spontaneous emission ~hen;: prepare an atom in an excited state at t = 0). What will be the spectrum tf we . h a "mirror image" to the time evolution, i.e., add exponential growth for t < 0 wit the same characteristic rate 'Y as the decay?

EXPONENTIALLY GROWING/DECAYING HARMONIC FIELD Understanding the relation between the temporal dependence of a signal and its spectrum is important, for example, in understanding lineshapes in transit broad- ening (Problem 3.13). We see here that "nonsharp" excitation not only alters the width of a Lorentzian profile but also distorts the spectral lineshape!

Solution The Fourier transform of an exponentially decaying harmonically oscillating field is a Lorentzian: (9.9)

where , is the decay rate for intensity and n is the oscillation frequency. The Fourier transf onn / + ( w) of an exponentially growing harmonically oscillating field is also a Lorentzian: I +(w) = j e-yt/2 sin(nt)e-iwtdt = --2 --.

_n ___ _ -oo -f + i1w - (0 2 - w2)

(9.10)

If we add these two results, we get for the Fourier transform of an exponentially growing then decaying function: -2i 1wfl (9.11)

To obtain the power spectrum, we take the norm-square of/ +(w) + f-(w), which gives: (9.12)

The above power spectrum is compared to the power spectrum of an exponentially decaying harmonic field in Fig. 9.2. The spectrum of the decaying field is broader than that of the sum of the growing and decaying fields. This difference is due to the sharp edge at t = 0 for the exponentially decaying field, which is known to have many Fourier components.

The power spectrum for an exponentially decaying harmonic field is given by: n2 lf-(w)l2 = ti+ (n2- w2)2 + i(n2 + w2) .

(9.13)

## MISCELLANEOUS TOPICS

0.8 a-.

~ 0.6 ~ 0.4 0.2 I ' ./ ~ FIG. 9.2 Dashed line: power spectrum of an exponentiaJly growing then decaying sinusoidal field ("y = 1, normalized to unity on resonance); Solid line: power spectrum of an exponentially decaying sinusoidal field for "'Y = 1.

If the approximations n, w >> ,, ~ are made (where Ll = n - w), the power spectrum for the growing and decaying hannonic field is given by: 4,2 lf+(w) + /_(w)l2 ~ (462 + -y2)2 .

while for the decaying hannonic field: 2 "-J 1/-(w)I ~ 46 2 + 12 · (9.14)

(9.15)

As one can see by comparing Eqs. (9.14) and (9.15), the power spectrum of the usual Lorentzian falls off as ~ - 2, whereas the power spectrum of the growing and decaying field falls off as Ll - 4•

## 9.4 The magic angle

In this problem, we give several examples where one encounters the "magic angle"

given by 8m = arccos ( Ja)

~ 54.74°, (9.16)

and then discuss a possible connection between these.

(a) Vector model for spin-1/2: In the quantum mechanical vector model, a state of angular momentum F and magnetic quantum number M is represented by a vector

## THE MAGIC ANGLE

of length hJF(F + 1), whose projection on the quantization axis (hM) is well defined~ ho~ever the overall angular momentum vector, as a consequence of the uncertat~ty m the transverse components, is "smeared" over a conical surface.

Consider the case of F = l /2. What is the half-angle of the cone?

(b) Polarized.fluorescence: Consider a resonance fluorescence experiment where at~ms are exc_ited with linearly polarized light, and the emitted light passes through a lmear pola~zer before reaching the detector. In general, (see for example, Prob- lem 3.8) emitted radiation of a given polarization is anisotropic in its spatial distribution .

. Show that if the polarization vector of the exciting light forms an angle 0m [given by Eq. (9.16)] with the axis of the linear polarizer in front of the detector, then the detected signal is insensitive to the anisotropic part of the fluorescence pattern.

We now briefly discuss an important consequence of this property for excited state lifetime measurements. Suppose one uses a pulsed laser with pulse duration much shorter than the excited state lifetime to excite the ground state lg) to the excited state le), and observes the time dependence of fluorescence due to the decay of le). Often it is convenient to observe a decay to a third level I/), rather than back to jg) because, for example, this allows one to easily suppress the signal due to laser light scattered into the photodetector.

While for a single state le), the temporal profile of the fluorescence is a decay- ing exponential, if there are several closely-lying substates of le) (for example, due to hyperfine structure) that are excited, there may appear modulation on top of the exponentially decaying signal known as quantum beats with frequencies corre- sponding to the energy separation between the excited sublevels. [For a review of quantum beats, see for example, Haroche ( 1976), Corney ( 1988), and Alexandrov et al. (1993).]

In some cases, for example, if the hyperfine structure constants for le) are not known, hyperfine quantum beats may present a problem for measuring the lifetime of le). However, an important property of quantum beats is that they are always associated with spatial redistribution of the radiation, and never occur in the total radiation intensity [this can be proven using Feynman diagram tech- niques (Appendix H) and is discussed in great detail, for example, in Alexandrov et al. (1993), Chapters 3.8-3.9). Thus, using the "magic angle" excitation-detection geometry, one can measure the time-dependence of the total intensity, free from the systematic effects associated with the quantum beats.

(c) Elimination of dipole-dipole coupling in NMR: The line width in nuclear mag- netic resonance [NMR; see, for example, Slichter ( 1990) for a detailed introduc- tion] is often limited by the dipole-dipole interaction between different nuclei that

## MISCELLANEOUS TOPICS

is described by the Hamiltonian _ - ma· ffib - 3(ma · f){mb · f)

H = -mb · Ba(r) = ' r (9.17)

where ma,b are the magnetic moments of the corresponding nuclei, Ba is th~ mag_: netic field produced by m0 (assumed to be located at the origin) at the location, r, of the second nucleus; f is the unit vector along r.

.

NMR experiments are usually performed in the presence of a strong leading magnetic field (which we assume is directed along i). In this case, all components of the magnetic moment vectors other than the z-components average to ~ro- From Eq. (9.17), we see that the dipole-dipole interaction depends on the position of the nuclei. For example, if r is along z, we have H = -2 (ma)zimb)z ' (9.18)

r while for r along x or fl, H = + (ma)zimb)z .

(9.19)

T Show that if the sample is continuously rotated around an axis tilted by the angle 8m [see Eq. (9.16)] from the z-axis, then the time-averaged dipole-dipole Hamiltonian is zero. This is a common technique allowing for higher spectral resolution in NMR measurements.

( d) What is the connection? In the examples above ( and in Problem 2.11 ), we have seen how the magic angle (9.16) appears in various contexts that are not obviously related to each other. To this list, one can add any problem where one encounters the Legendre polynomials, for example, electrostatic and magnetostatic boundary- value problems [Jackson (1975), Chapter 3], and quantum mechanical problems with wavefunctions for a particle in a central potential. Indeed, the Legendre polynomial vanishes for 8 = Bm.

3cos 2 8 - 1 P2=-- 2-- (9.20)

Speculate on whether the appearance of the magic angle in all these different problems signifies any profound physical connection between them.

Hint In part (b ), in order to show that the magic angle geometry is insensitive to the anisotropy of the radiation pattern, consider possible tensor components of le) that can be excited from the unpolarized state lg); and also, which tensor components can be detected by fluorescence in a given geometry.

## THE MAGIC ANGLE

Solution (a) For F = 1/2, the length of the angular momentum vector in units of ri is (9.21)

In the state, for example, with M = 1/2, 1/2 is also the height of the cone. The half-angle of the cone is found from trigonometry: 81; 2 = 8m given by Eq. (9.16).

(b) We are assuming the case of weak, broadband excitation (i.e., the spectral width of the excitation pulse broader than the distance between the sublevels of le)), and initially unpolarized ground state lg). What is the polarization of the excited state le)? Since the ground state is unpolarized, the polarization of the excited state is that of a photon, i.e., in addition to population (the rank-zero com- ponent of the excited state density matrix, see Appendix G), in general, there can also be orientation (rank-one), and alignment (rank-two). In the case of lin- early polarized light, orientation is absent (as is clear from symmetry - there is no preferred direction in space). Therefore, the only term that can lead to radia- tion anisotropy is alignment. Moreover, choosing the quantization axis along the excitation light polarization, from symmetry, we also see that the anisotropy cor- responds to 1,, = 2, q = 0, where 1,, and q are the tensor rank and component, respectively. What can we say about the spatial distribution of the fluorescence?

The intensity of the detected radiation (at a given distance between the detector and the source of the radiation) depends on the relative orientation of the radiated and detected polarizations. According to the Wigner-Eckart theorem (Appendix F), the anisotropy must transform upon spatial rotation as an eigenfunction of the angular momentum "' and projection q, i.e., as Y2°(8) in this case. (Here 8 is the angle between the radiated and detected polarizations.) Therefore, the intensity of the detected radiation can be written as (9.22)

where the coefficients A and B(t) (that depend on the concrete system) describe the isotropic and the anisotropic part of the radiation, respectively, and Yzm ( f), </J)

is a spherical harmonic. Note that from the symmetry of the problem [and, conse- quently, Y2° ( f), </J)] the emitted light has no </>-dependence. In expression (9 .22), it is explicitly seen that the anisotropic part averages away upon integration over all directions of polarization of the emitted light, and that quantum beats arise due to the time dependence of the anisotropic part.

Finally, since (9.23)

X

## MISCELLANEOUS 1UPICS

z ' q> ' ' ' ' ' ' ' ' ' ' ' ' (I)

' ' ' ' ' ' 'I ' z' y FIG. 9.3 Geometry for the calculation of the effect of spinning on dipole-dipole coupling.

where P2[cos(8)) is the Legendre polynomial, we see that the anisotropic pan (and.

correspondingly, the hyperfine quantum beats) are not observed in the magic angle geometry where fJ = 8m.1 For a rigorous discussion of the tensor expansion of the excited state density matrix (Appendix G), the reader is referred to Haroche ( 1976) and references therein.

(c) Because all but the z-components of the magnetic moment average out due to the presence of the strong leading magnetic field along z, we can rewrite the Hamiltonian (9.17) as H __ mz(a)mz(b) {l _ 3 2 () )

- COSr, r (9.24)

where 8r is the angle between rand the z-axis.

Suppose we rotate the sample around an axis (z') going through the origin and tilted with respect to the z-axis by an angle fJ (Fig. 9.3). For the present analysis, it is convenient to choose the directions of the other two "primed" axes in such a way that a rotation around y' by fJ brings z' in coincidence with z.

1 Note that, if the observation direction is fixed with respect to the excitation polarization, it may not always be possible to set the angle between the excitation and detection polarizations at 8m by adjusting the orientation of the polarizer in front of the detector. For this to be possible. the observation angle should be within ±Bm from the equatorial plane.

## THE MAGIC ANGLE

S~ppose f3 is the angle between f and Z', and <Po is the initial angle in the ro!ation plane as shown in Fig. 9.3. The coordinates of the radius vector in the pnmed frame are: x' = r sin (3 cos( </>o + wt), y' = r sin (3 sin( <Po + wt), (9.25)

(9.26)

Z 1 = T COS (3.

(9.27)

We are interested in finding the time average of the Hamiltonian (9.24), so we need to find z. Applying the rotation matrix for the rotation around y' by -8 ( cos()

sin())

, - sin()

cos()

we get z = r cos 8r = r[- sin() sin (3 cos( ¢0 + wt) + cos (3 cos 8], from which we obtain cos 8r = [- sin 0 sin /3 cos( ¢0 + wt) + cos /3 cos 0], (9.28)

(9.29)

(9.30)

which, upon squaring and averaging over a period of the rotation (and just a bit of algebra), leads to H mz(a)mz(b)

1 ( )( )

= r 3 • 2 1 - 3 cos 0 I - 3 cos {3 .

(9.31)

Choosing 0 = 8m nulls the average dipole-dipole interaction for any /3.

(d) A reader expecting to find here a definitive answer may be disappointed, as we only have our own speculations to offer.

Some connections are obvious and stem from the fact that if equations are the same for different problems, the solutions are also the same. For example, the Laplace equation appears both in electro- and magnetostatic problems, and in the solution of the Schrodinger equation for centrosymmetric problems. In other cases, exemplified by parts (a)-(c), the equations do not seem to be the same and the connections are, at least, not obvious, except for the fact that the value of the magic angle in each example is clearly related to the fact that space has three dimensions.

One of the central messages of this book is the universality of physical ideas underlying seemingly different phenomena, and the power of making analogies and using symmetries. However, we do not believe that this approach should be taken to the level of "numerology."

Is there a reason the number 1r appears in so many different contexts? (If this is not obvious, how about number 2?).

## MISCELLANEOUS TOPICS

## 9.5 Understanding a Clebsch-Gordan coefficient selection

rule Consider an electric (magnetic) dipole F = 1 ~ F' = 1 transition. According to the Wigner-Eckart theorem (Appendix F), the transition amplitude between the Zeeman sublevels M, M' is proportional to the reduced matrix element times the Clebsch-Gordan coefficient (F, M, 1, M' - MIF', M') = (1, Al, 1, M' - Mil, M').

(9.32)

It turns out that this Clebsch-Gordan coefficient vanishes for M = M' = 0, which means that a z-polarized electric (magnetic) field does not excite the M = 0 ~ M' = 0 transition (Fig. 9.4). Find a physical explanation for this result, which is important in many optical pumping experiments (see, for example, Problems 3.9 and 4.8).

Solution In elementary particle physics particles with intrinsic-angular-momentum one are called vector particles. Their internal state can be completely characterized by a polarization vector. The relation between the direction of the polarization vector and the quantum number M can be established by recalling the familiar case of the photon, as summarized in Table 9. I .

When we combine two angular-momentum-one particles into a composite system, we need to build the wavefunction of the combined system out of the wavefunctions of the constituents. The composite wavefunction has to be linear in the wavefunctions of the constituents.

M' = -1 M'=O M'= 1 M=-1 M=O M=l FIG. 9.4 Dipole transitions between M = !vi' = 0 are forbidden for an F -+ F transition (F = 1 in this diagram).

UNDERSTANDING A CLEBSCH-GORDAN COEFFICIENT SELECTION RULE TABLE 9•1 Correspondence between the quantum number A/ and the direction of the polarization vector for a panicle with intrinsic-angular-momentum one.

M Polarization vector cx.x-iiJ oc z + 1 ex x + iiJ Combining two angular-momentum-one particles, we can get F = 0 (scalar), F = I (vector), or F = 2 (tensor). In this case we need to combine a spin-one initial atomic state with a photon to obtain a vector (i.e., the final spin-one state).

Now, given polarization vectors e1 and e2, there is only one way to obtain a vector: (9.33)

But for the case of the M = O initial state and a z-polarized photon, both vectors e1 and e2 are parallel to z (see Table 9.1 ), so the vector product (9.33) is identically zero.

In other words, the amplitude of a process, where two spin-one particles with polarization vectors e1 and e2 combine into a resultant spin-one particle with polar- ization vector e, should be a scalar linear in all three polarization vectors. The only such possibility is (9.34)

which vanishes for all three vectors along z.

The selection rule discussed in this problem is a particular case of a more gen- eral selection rule, (F, 0, 1, 0IF, 0) = 0, which means that M = 0 ~ M' = 0 dipole transitions are forbidden for any F = F'.

One can see how the general selection rule arises by considering properties of the Clebsch-Gordan coefficients. The state IF', M') is fonned by combining the angular momentum of the photon with the angular momentum of the lower state F according to the Clebsch-Gordan expansion: IF', M') = L (F, M, 1, q = M' - MIF', M')IF, M)ll, q) .

(9.35)

M It is clear that no physical properties of the system should depend on the direction we choose for the quantization, so if we compare the Clebsch-Gordan expansion

## MISCELLANEOUS TOPICS

for the IF', -M') state, IF', -M') = L (F, -M, 1, -q = M - M'IF'. -M')IF, -M)ll, -q) , M = ± L (F, M, 1, q = M' - MIF'. M')IF, -M)ll, -q), M (9.36)

with Eq. (9.35), we see that the magnitudes of the corresponding Clebsch-Gordan coefficients must be equal: l(F,M,l,qlF',M')I = l(F,-Af~L-qlF',-M')I.

(9.37)

Since the Clebsch-Gordan coefficients are real, either (F, M, 1, qlF', M') = (F, -Af, 1, -qlF', -M')

(9.38)

or (F, M, 1, qlF', M') = -(F, -kl, 1, -qlF', -M')

.

(9.39)

One can show (using, for example, the raising and lowering operators) that for F' = F + 1 Eq. (9.38) holds, while for F' = F the two coefficients are related by a - sign according to (9.39). Thus we have (F,O, l,OIF,O) = -(F,O, 1,0IF,O), (9.40)

which proves that the Clebsch-Gordan coefficient (F, 0, 1, OIF, 0) is zero and that subsequently M = O --+ M' = 0 dipole transitions are forbidden for any F = F'.

## 9.6 The Kapitsa pendulum

In this problem we will discuss a beautiful effect - stabilization of harmonic motion about the unstable equilibrium point by application of a high-frequency perturbation. The effect is well-known in mechanics (the Kapitsa pendulum), and is also at the heart of quadrupole mass spectrometers and the so-called Paul traps for charged particles [Paul et al. ( 1958), Paul ( 1990), Ghosh ( 1995)]. It is also widely used in particle accelerators, for example, in radio-frequency quadrupole ion accelerators (Humphries 1986).

Frictionless motion of a point mass, m, is confined to a circle of radius R in a vertical plane.

(a) What is the frequency of small oscillations, no, of this system around the equilibrium point ( <.p = 0) in the absence of forces other than gravity?

## THE KAPITSA PENDULUM

g FIG. 9.S The Kapitsa pendulum.

For the remainder of the problem, suppose that a periodic force of magni- tude / sin(wt) with w >> Oo is applied to the mass in the vertical direction (see Fig. 9.5). Assume that the "fast" jitter of the mass is of amplitude smaller than the "slow" oscillation considered in part (a).

(b) Find the correction, n - 0 0, to the frequency of the "slow" oscillation of the pendulum.

(c) Show that when the amplitude of the force f is sufficiently large (how large?), r.p = 1r is also an equilibrium point in addition to r.p = 0.

(d) Find the frequency of small oscillations around r.p = 1r.

Solution (a) This is just a regular pendulum, so (9.41)

(b) Since the motion of the mass is restricted to the circle, the only relevant component of the force is that tangential to the circle: ft = f sin(wt) sin r.p .

(9.42)

The motion of the mass consists of a fast jitter (with frequency w) and a slow oscil- lation (with frequency~ 0 0). Writing r.p(t) = r.p 8 (t) + 'P1(t) (where the subscripts

MISCELLANEOUS lOPICS indicate slow and fast motion, respectively), we obtain the general equation of motion for this system (the so-called Mathieu equation): '{) 8 +'Pt= [- ~ + !R sin(wt)] sin(cp8 +'Pt).

(9.43)

Assuming 'Pf << I, we can expand this equation to first order in the small parameter: tp8 + 'Pf = [-!!..

+ _L sin(wt)] · (sin ';?s + 'Pf cos r.p8 ) • R mR (9.44)

In order to find the fast motion, we can neglect the slow motion and just assume that the fast oscillation occurs around a quasistationary value 'Ps• To first order9 we have: ..

I . ( t) .

'Pf = mR SID w sin 'Ps , 'Pf = -mL 2 sin(wt) sin 'Ps , (9.45)

(9.46)

where in the last step we have neglected constants of integration that do not con- tribute to the fast oscillation. Now we return to Eq. (9.44) and substitute the results (9.45) and (9.46). Averaging the fast-oscillating tenns, we get: ..

g .

.

'Ps = - R SID 'Ps - 2m 2 R2w2 cos 'Ps SID r.p8 • (9.47)

From Eq. (9.47) one can see that small slow oscillations around 'Ps = O occur at a frequency (9.48)

(c) Consider Eq. (9.47) near 'Ps = 1r. Introducing cp' = 'Ps - 1r, cp' << 1, we have: ••/ ( 9 )

I 'P = R - 2m 2R2w2 'P · (9.49)

An oscillatory solution is obtained when the quantity in parentheses in Eq. (9.49)

is negative.

( d) We obtain (9.50)

## VISUALIZATION OF ATOMIC POLARIZATION

9• 7 Visualization of atomic polarization In th~s problem, we outline a technique for visualizing atomic polarization by drawmg a surface in three dimensions representing the probability distribution ?f the _angular momentum vector (Rochester and Budker 200 I ). 2 This technique is pa_rticularly useful for understanding the symmetry properties of higher-order mu!tipole moments and understanding the time-evolution of atomic polarization durmg quantum beats.

In °rder to visualize the polarization state of atoms with total angular momen- tum F,_ ~e draw a surface whose distance r from the origin is proportional to the pro~ab_ihty ~f fin~ing the projection M = F along the radial direction. To find the radius m_a direction given by polar angles 0 and <p, we rotate the density matrix P (Appendix G) so that the quantization axis is along this direction p(0, 'P) = '.D( .p, 0, 0) p(0 = 0, <p = 0) '.Jr 1 ( <p, 0, 0)

(9.51)

and then take the PM=F,M=F element: r(0, cp) = p(0, ~)F,F · (9.52)

Here '.D(<p, 0, 0) is the appropriate quantum mechanical rotation matrix (Appendix E).

(a) Plot the probability surface for an ensemble of unpolarized atoms.

(b) Plot the probability surface for an ensemble of atoms in the stretched state F = I, M = I. What state multipoles 3 are present (see Appendix G)?

(c) Plot the probability surface for an ensemble of atoms in the state F = l, M = 0. What state multipoles are present in this case?

(d) This technique can be particularly helpful in seeing the dynamical behavior of atomic polarization (quantum beats) in the presence of external fields.

While it is straightforward to visualize the behavior of a polarized atomic ensemble in the presence of a magnetic field (this is just Larmor precession, see Problem 2.6), the phenomenon of quantum beats caused by an electric field (Stark beats) is more difficult to visualize.

Consider atoms with F = l which are initially in a stretched state along fl. Suppose an electric field f, is applied along i. Use the techniques of atomic polarization visualization to describe the evolution of the atomic polarization.

2 A similar approach has been used to describe molecular polarization and its evolution (Auzinsh and Ferber 1995), and to analyze anisotropy induced in atoms and molecules by elliptically polarized light (Milner and Prior 1999).

3 State muhipoles are a commonly used for characterizing atomic polarization, and, as mentioned above, the procedure for visualization of the polarization allows one to see the symmetries of the system. This, in tum, assists in understanding the optical properties of polarized atomic samples as discussed, for example, in a review by Budker et al. (2002).

Solution

## MISCELLANEOUS TOPICS

(a) For an unpolarized sample, the proba~ility to fin~ a~ atom_ in the stretched state IF, M = F) is the same for any choice of quant1za!1on axis. Therefore th probability surface is a sphere, i.e. r( 0, c.p) is a constant (Fig. 9.6).

e (b) The density matrix p(O, 0) (with quantization axis along z) describing ensemble of atoms with total angular momentum F = I, all in the M == I Zeem:: sublevel, is p(0,0) = G g g)

(9.53)

The rotation matrix 'D(cp, 0, 0) is given by (Appendix E)

'D( cp, 0, 0) = 'D(0, 0, 0) · 'D( c.p, 0, 0)

(9.54)

= - ~ sin0 ei"' cos0 "72 sm0 e-i,p , ( ½ ( 1 + cos 0)ei"' ~ sin 0 ½ ( 1 - _cos 0)e_-i"')

½(1-cosO)ei"' -~sin0 ½(l+cos0)e-i"' (9.55)

and we can obtain 'D( cp, 0, 0)- 1 [needed in Eq. (9.51)] by successively "undoing"

the rotations: 'D(c.p, 0, 0)- 1 = 'D(-cp, 0, 0) · 'D(0, -0, 0)

( ½(I+ cos0)e-i'P .

L)

- -smu - v'2 ½ (1 - cos 0)ei'P z ( X -"72 sin 0 e-i,p cos0 - 1 sin() ei'P v'2 (9.56)

½{I ~ c~s 0)e_-i"')

- v2 S111 () ei<p • ½ (1 + cos 0)eicp (9.57)

FIG. 9.6 Two-dimensional cross-section and three-dimensional surface representing the atomic polarization for an unpolarized atomic sample.

## VISUALIZATION OF ATOMIC POLARIZATION

z X FIG. 9. 7 Two-dimensional cross-section and three-dimensional surface representing the atomic polarization for an ensemble of atoms in the NI = l Zeeman sublevel of a state with total angular momentum F = l. The distance of the surface from the origin is given by r(0, c.p) from Eq. (9.59).

Thus the density matrix in the rotated frame is given by ( ¼(1 + cos0) 2 = 2J2 sinO{l + cosO)

¼(1-cos 2 0)

2J2 sin 0(1 + cos 0)

l sin 2 0 2J2 sinO{l - cosO)

¼(1-cos 20))

2J2 sin 0(1 - cos 0)

.

¼(I - cos0) 2 (9.58)

Therefore, according to Eq. (9.52), the probability surface is described by r(O, cp) = 4(1 + cos0) 2 • (9.59)

Note that since there is no dependence on <.p, the atomic polarization is cylindrically symmetric about the z-axis. This probability distribution is plotted in Fig. 9.7.

Based on the discussion in Appendix G, we know that the highest multipole that can appear corresponds to "" = 2 (quadrupole moment or alignment). The state multipoles, calculated according to Eq. (G.54), are given in Table 9.2.

(c) Following the same procedure applied in part (a), for an ensemble described by the density matrix (9.60)

MISCELLANEOUS lUPICS TABLE 9.2 Values of various multipole moments for an ensemble of atoms in the M = 1 Zeeman sublevel of a state with total angular momentum F = l. The superscript gives the rank of the multipole (K.) and the subscript is the component q. Note that multipoles of all possible ranks are present.

Multipole Value Monopole (0)

I Po 7a {l)

Pi Dipole (orientation)

(1)

Po (I)

P-1 (2)

P2 (2)

Pi Quadrupole (alignment)

(2)

I Po (2)

P-1 {2)

P-2 we obtain (9.61)

The corresponding probability surface is plotted in Fig. 9.8. The values of the multipole moments are given in Table 9.3. In this case, as expected from symmetry, there is no orientation.

Probability surfaces can be useful for visualizing the symmetries possessed by an ensemble of atoms and understanding their optical properties. For example, an atomic ensemble described by the polarization surface drawn in Fig. 9.7 clearly has a preferred direction, namely z. Such an ensemble can be expected to possess circular birefringence and circular dichroism for light propagating along z. Fig- ure 9.7 illustrates that there are more atoms in states with M = +1 as opposed to M = -1, so one expects different indices of refraction for left- and right- circularly polarized light. This is indeed a general property of atomic ensembles whose polarization possesses a preferred direction.

Similarly, an ensemble described by the probability surface shown in Fig. 9.8 evidently possesses linear dichroism and linear birefringence for light propagating along x or y.

## VISUALIZATION OF ATOMIC POLARIZATION

z z X FIG. 9.8 Two-dimensional cross-section and three-dimensional surface representing the atomic polarization for an ensemble of atoms in the A/ = 0 Zeeman sublevel of a state with total angular momentum F = 1.

TABLE 9.3 Values of various multipole moments for an ensemble of atoms in the !vi = o Zeeman sublevel of a state with total angular momentum F = 1.

Multipole Value Monopole (0)

Po (1)

P1 Dipole ( orientation)

( 1)

Po (I)

P-1 (2)

P2 (2)

P1 Quadrupole (alignment)

(2)

Po -~ (2)

P-1 (2)

P-2 This method is especially helpful for ensembles possessing high (K > 2) polar- ization moments for which the symmetries may not be immediately obvious from the form of the density matrix [see, for example, Yashchuk et al. (2003) and Budker et al. (2003)].

(d) Our first step is to write a density matrix for a stretched state oriented along fl. We can do this by beginning with the density matrix for a state stretched along z [Eq. (9.53)], and then rotating the coordinate frame appropriately. According to

CD

## MISCELLANEOUS TOPICS

z No rotation about z-axis necessary.

a=O y X Rotate about z-axis.

y=-7t/2 y ,,---.__ 2; ......._/ X z Rotate about y-axis.

P=-n12 y y FIG. 9.9 Frame rotation through Euler angles a, /3, "f for convening an atomic sample polarized along z to a sample polarized along y.

Appendix E, we require a rotation by the Euler angles /3 = -1r /2 and 'Y = -1r /2, as can be seen in Fig. 9.9.

Thus the density matrix describing the system at time t = O is given by ~) . 1)-1(0 - 7r - 7r)

o ' 2' 2 ' (9.62)

(9.63)

The next step is to use the Liouville equation (Appendix G) to determine the time dependence of the elements of the density matrix. The atomic polarization evolves due to the quadratic Stark splitting of the Zeeman sublevels, and we need only take into account the effect of the tensor polarizability 02 (since the scalar shift moves all the sublevels together) described by the formula (see Problem 2.11)

f, 2 3M 2 - F(F + 1)

H(M) = - 02 2 F(2F - 1)

' (9.64)

## VISUALIZATION OF ATOMIC POLARIZATION

so in the case of an F = I atom we have H = _ 0r G :2 ~) .

Using (9.65) in the Liouville equation (G.44), dp I dt = iii [H, p] ' we obtain the following set of differential equations (in matrix form): d (Pll dt Po1

## P-11

where PIO Pl-1)

( Poo Po-1 = -iwspo1

## P-10

## P-1-1

21r ws=-= TS iwspw O )

O -iwspo-1 , iwsP-10 (9.65)

(9.66)

(9.67)

is the Stark splitting (and hence the frequency of the Stark beats). The differential equations are independent and are easily solved, yielding for the time-dependent density matrix ( P11 (0)

Pw(0)eiwst P1-1 (0) )

P( t) = Pol (O)e-iw"t Poo(O)_ t Po-I (O)e-iw"t .

P-11(0)

P-w(0)eiws P-1-1(O)

(9.68)

The final step is to apply the visualization technique to see the dynamic evo- lution of the atomic polarization. Using the initial values of the density matrix elements PM,M'(0) from (9.63) in Eq. (9.68), and rotating the resultant density matrix by polar angles 9, <.p, we obtain (after a considerable amount of algebra) for the radius vector describing the probability surface [Eq. (9.52)]: r((J, <p, t) = 32 [10 - 2 cos(W) + cos (2(() - <p)) - 2 cos(2<p) + cos (2(() + <p))

+ 16 sin() sin cp cos wst + 8 cos cp sin 20 sin wst] . (9.69)

This surface is plotted in Fig. 9.10 for several values oft. Note that while the original state has both orientation and alignment (along y), during the evolution it goes through stages (see plots fort = rs/4 and t = 3rs/4) where there is only alignment. This is an example of alignment-to-orientation conversion [see Budker et al. (2002) and references therein].

## MISCELLANEOUS TOPICS

z z r 5r t= - t= -- ~ X z z 7r t = r t=-- X y FIG. 9.10 A sequence of probability surfaces representing electric-field-induced evolution of a state with F = 1. The state is initially stretched along y and an electric field is applied along z, causing Stark beats with period Ts. At t = o, one sees that the atomic polarization is identical to that discussed in part (b) of the present problem, except that the state is stretched in the y direction as opposed to the z direction (compare with Fig. 9.7). At t = Ts/4, we see that the ensemble is aligned with an axis along x + z (compare with Fig. 9.8), then at t = Ts/2 the ensemble has evolved to have orientation in the -fl direction, at t = 3Ts I 4 the sample possesses alignment with an axis along z - x, and finally at t = Ts the sample returns to its initial polarization. Along the way, one can see how the optical properties of the sample are modified as the symmetry of the atomic polarization changes. Figure from Rochester and Budker (200 I).

## 9.8 Estimate of elasticity and tensile strength of materials

The Young's modulus is the coefficient of proportionality between relative defor- mation of the medium and the stress ( measured in units of pressure). If a slab of a material of cross-section A and equilibrium length l is stretched or compressed (within elastic deformation limits), so its length changes by 6l, the resulting

ESTIMATE OF ELASTICITY AND TENSILE STRENGTH OF MATERIALS restoring force, according to the definition of the Young's modulus, E, is Llf F=-EA- l .

(9.70)

Tensile strength T is the maximum force per unit of cross-sectional area that can be applied to stretch a slab of a material before it breaks.

Based on the fact that materials are made of atoms, estimate maximal possible values of the Young's modulus and tensile strength.

A detailed discussion of the theory of mechanical properties of solids (includ- ing the tensor aspects that are beyond the scope of this problem) can be found in The Theory of Elasticity by Landau and Lifshitz ( 1999).

Solution Materials are composed of atoms that are attached to each other with chemi- cal bonds. Some of the largest interatomic binding energies are on the order of Eb rv 10 eV, and in materials where atoms are packed most densely, the distances between neighboring atoms are d rv 2 A. The dense packing that we are assuming means that there are on the order of d- 2 rv 3 x 1015 atoms per l-cm 2 cross-section of the material.

For the purpose of an estimate, we can assume that an atom of the material is in a potential that is harmonic up to displacements from the equilibrium on the order of d, and that the potential drops steeply at larger separations, so the height of the resulting potential barrier is rv Eb.

From this, we immediately estimate a "spring constant" k for one atom as (9.71)

From this microscopic picture, we can calculate the restoring force of a slab of material of cross-section A and equilibrium length f when its length is changed by ~f,: as (9.72)

where we have taken into account that Lld Llf f (9.73)

and Eq. (9.71). Comparing Eqs. (9.70) and (9.72), we see that 2Eb 24 eV 12 erg E ~ d3 ~ 2 x 10 cm3 ~ 3 x 10 cm3 = 300 GPa .

(9.74)

## MISCELLANEOUS TOPICS

This naive estimate comes within a factor of two of the largest values f the Young's modulus for common materials. For example, the largest value ; E _

## 534.4 GPa listed by Kaye and Laby ( 1995) is for tungsten carbide

- Next we tum to the estimate of the tensile strength, T. Assuming that the _ rial can be stretched all the way until dd ~ d, we can obtain an estimate fi m~ tensile strength by substituting dl/l = 1 into Eq. (9.70), which leads to T ~rE However, real-li~e ma~rials may ~ ex~ted to break at much lower t~- sions due to crystalhne-latt1ce defects, 1mpunt1es, surface effects, etc., that lead to nonuniform distribution of forces between different atoms. Indeed, the highest values of tensile strengt~ for common materials are below T ~ 3 - 5 GPa (for best tungsten wires and certam types of fiberglass).

It is interesting to note that in recent years, carbon nanotubes have been ro- duced with measured tensile strength of up to 63 GPa and theoretically estim:ted ultimate strength of up to 300 GPa, which, as we see, is close to the maximal possible strength for any imaginable material made of atoms (Eq. (9.74)]. An important feature of the carbon nanotube-based materials is that they are very light. One possible application is the idea (that may have seemed like bad sci- ence fiction before the advent of these new materials) of a space elevator (see http://www.isr.us/SEHome.asp) - a system for launching space vehicles, the cen- tral part of which is a cable stretched between the Earth and a counterbalance positioned beyond the geostationary orbit.

## 9.9 The Casimir force

Casimir forces, recently reviewed by S. K. Lamoreaux (2007), arise as a con- sequence of quantum fluctuations of the electromagnetic field (see Problem 3.2)

and play an essential role in interactions of objects on the sub-micron scale.

These forces are important in understanding a broad range of phenomena - from aggregation of colloidal particles (the original motivation of H. Casimir's work in the 1940s) to peculiar behavior of Bose-Einstein condensates in the vicinity of surfaces.

Based on the idea that the Casimir forces arise due to the perturbation of the electromagnetic vacuum field by the interacting objects, give a "back-of- the-envelope" estimate of the Casimir force between two parallel conducting plates separated by a distanced. What is the scaling of the force with distance?

Numerically estimate the force per unit area for a separation of d = 0.1 µm.

## THE CASIMIR FORCE

Solution Let us begin by calculating the number of possible modes of electromagnetic field in a box of volume V in a small interval of wave vector magnitudes near a value k (the density of photon states), a key ingredient in a standard calculation of black- body radiation. (Note that the shape and size of the box and the type of boundary condition on its surface do not affect the final answer.) We begin with the expres- sion (3.76) derived in Problem 3.3 for the differential number of photon mcxles with a given polarization: V dN = {21r)3 k dk dO., (9.75)

where dfl is the differential solid angle into which the possible k's are directed.

Since we have no restriction on the direction of k nor on the light polarization, we integrate over the solid angle and multiply by 2 for possible polarizations: (9.76)

and dividing by the volume V we obtain the number of modes per unit volume (9.77)

Next, we recall that, even at zero absolute temperature, zero-point fluctuations supply hw /2 of energy to each mode (Problem 3.2), where w = ck is the frequency of the mode.

The final crucial piece of physics in our estimate is the fact that the presence of the conductors restricts possible values of the component of the wave vector perpendicular to the plates k1. to values given by m1r k1_ = d , (9.18)

where m is a non-negative integer. For a crude estimate, we can say that modes with k ;S 1r / d are not allowed due to the presence of the conducting surfaces.

Thus, the energy density between the plates is smaller than it would have been in vacuum, and therefore, there is a negative pressure attracting the plates to each other. Considering a volume between portions of the plates of area A, we find that the excess electromagnetic-field energy fex is f 1r Id lick k2 lic1r2 A fex ~ Ad X lo 2 7r2dk = 8d3 .

(9.79)

Note that this is only an estimate as we have neglected the effect of the conductors on modes with wave vectors beyond our cut-off, and also the zero-point energy

## MISCELLANEOUS 1UPICS

of the Jow-k modes still present between the plates. Another serious issue that we are "sweeping under the rug" in this calculation is the divergence of the integral for the total energy density in the electromagnetic field both inside and outside the plates (this is briefly discussed in Problem 3.2).

The magnitude of the negative pressure corresponding to the attraction of the conducting plates is found from Eq. (9.79) by differentiating the excess energy with respect to d and dividing by area: 1 Of.ex 31icrr2 Pest = A 8d ~ - &J4 .

(9.80)

It turns out that our "back-of-the-envelope" approach, while reproducing the correct functional dependence of the Casimir force, including its d- 4 scaling, sig- nificantly overestimates the effect, and a more rigorous calculation gives [see 9 for example, Gerry and Knight (2005), pp. 31-33): 1ic7r2 P = -240d 4 • (9.81)

Plugging d = 0.1 µm into Eq. (9.81), we find that the attractive force between the plates is about I 00 dynes per square centimeter of area, · corresponding to a negative pressure of~ 10- 4 atm.

## APPENDIX A

UNITS, CONVERSION FACTORS, AND

## TYPICAL VALUES

In this appendix, we list some practical units, conversion factors, and typical values of miscellaneous parameters that we find quite useful in practice. The choice of which items to list and to use is quite a bit of a personal matter as each practicing physicist develops his or her own "portfolio."

• Atomic units Length= Bohr radius= ao: li2 ()

ao = - 2 ~ 0.5292 A, me (A. I)

where m and e are the mass and the magnitude of the charge of the electron, respectively.

Energy = twice hydrogen's ionization potential: e2 1ne4 - = - 2- = a 2 · m.c2 ~ 27.21 eV.

ao n , where o = e2 / he ~ 1/137 .036 is the fine structure constant.

The Rydberg constant R00 in wavenumbers is e2 -I R00 = - -1-:- ~ 1.09737 X 10 Clll , 2ao 21r,1,c where the oo denotes that we assume infinite nuclear mass.

Velocity = velocity of an electron in the first Bohr orbit: e2 - =oc.

/1, (A.2)

(A.3)

(A.4)

UNITS, CONVERSION FACTORS, AND TYPICAL VALUES ao li3 - = - 4 ~ 2.419 x 10 sec .

(A.5)

oc me These typical scales of various atomic parameters comprise a system of "atomic units" in which Ii = m = e = 1. This makes the speed of light c = o- 1 = 137.036 in atomic units and the above quantities constitute the units of length, energy, velocity, and time.

• Electric dipole moment eao ea0 :::::: 2.54 • 10- 18 esu · cm.

(A.6)

Molecular physicists typically express electric dipole moments in units of Debye = 10- 18 esu · cm, while the atomic unit of electric dipole moment is eao.

eao ,._ 28 MHz h ~ 1.

V/cm · (A.7)

(A.8)

Whenever one calculates the shift of energy levels by the Stark effect (OC or AC), it is necessary to multiply an electric dipole moment by an electric field. It is often convenient to express such a product in frequency units. The relation between the units of electric field is: 1 esu(E) ~ 300 V /cm.

• Bohr magneton µo eli e2 eli2 a µo = -- = - . -- = - . eao.

2mc 2/ic me 2 ~o ::::::

## 1.40 MHz/G

• Magnetic moments in terms of µo Electron magnetic moment: µe:::::: -(1 + 2:)µo:::::: -1.00116µ0.

Proton magnetic moment: 2.793 µp ~ 2. 793 · µN ~ 1836 µo, (A.9)

(A.IO)

(A. I I)

(A.12)

(A.13)

where µN = eli/(2mpc)

(mp is the proton mass) is the nuclear magneton and mp/m ~ 1836.

UNITS, CONVERSION FACTORS, AND TYPICAL VALUES Neutron magnetic moment: • Electric field strength in a light beam (A.14)

!he_ intensity / in a light bea~ averaged over a period of the light oscillation 1s given by the average Poyntmg vector - le- - le I= (ISi) = 2 41r 1e x HI = 2 41r e2, (A.15)

where £ is the light electric field amplitude.

( 111W)

4 mW (erg/s)

I - = 10- / · I :::::: 1.33. [E(V /cm)]2 c1n erg s · (A.16)

~hen calcula!ing the A~ Stark effec~ or transition rates induced by laser hght, one typically requires the amplitude of the electric field of the light for computations. This conversion relates this electric field to standard useful "laboratory" units describing the intensity of a laser beam.

• Number of photons in a light beam For a cw light beam of intensity I, area A, and wavelength A, the number of photons per second incident on a surface is given by: dN::::::

## 3.93 x 1015. 1(mW)

. A(cm2). A(nm) .

& cm2 ~o (A.17)

The number of photons in a light pulse of energy U is given by: N ~ 3.93 x 1015 · U(mJ) • A~~~) .

(A.18)

Equations (A.17) and (A.18) are normalized to the resonant wavelength of the Rb D2 line.

• Saturation parameter for a typical atomic transition The coupling strength between resonant light and a two-level system can be characterized by a saturation parameter (Problem 3.7): d2e2 [d(eao)]2I(~)

K = n,2,z - 1.23 X [?i(MHz)]2 .

(A.19)

Here d is the dipole moment of the transition, £ and / are the light elec- tric field amplitude and intensity, and 1'0 is the homogeneous width of the transition.

UNITS, CONVERSION FACTORS, AND TYPICAL VALUES • Planck's constant times the speed of light he lie~ 3.16 • 10- 17 erg· cm~ 197.3 MeV · fm ~ 197.3 eV ·nm.

(A.20)

• Magnetic field units l T = 10 4 G; 1 'Y == 10- 5 G .

(A.21)

In vacuum, magnetic induction B(G) equals magnetic field H(Oe). The SI unit of magnetic induc!i~n is the tesla, T. In geophysics and magnetometry, the commonly used umt 1s gamma, "Y· The magnetic field inside a long solenoid with winding density of n turns/ cm and current i is: 41rn .

H(Oe) = - i{esu)

C 41rn ( ~ 3 x 1010 i A) · 3 x 10 esu/ A 41r ~ 10 n(turns/cm).

i(A).

This relation defines another commonly used unit of magnetic field: 1 Ax turn/cm= 41r/l0 Oe ~ 1.26 Oe.

• Energy units 1 eV ~ 1.60 x 10- 19 J ~ 1.60 x 10- 12 erg ~he· 8066 cm- 1 ~ h • 2.41. 1014 Hz.

1 cm - l x c ~ 30 GHz .

(A.22)

(A.23)

(A.24)

(A.25)

The conversion (A.25) is derived from the relations between the frequency v, and wavelength A: v = c/ A.

The temperature corresponding to an energy E of 1 e V is T = E/kB ~ 11,600 K.

(A.26)

Here k8 ~ 1.38 x 10- 16 erg/K is the Boltzmann constant.

UNITS, CONVERSION FACTORS, AND TYPICAL VALUES • Gas density 1 torr~

## 1.33 x 103 dyne/c1n

(A.27)

is the pressure of a mercury column 1 mm high (on the surface of the Earth).

N(cm-3) = P(dyne/cm2) ~ 9.66 x 101s P(torr)

kBT T(K)

· (A.28)

Here T(K) is the absolute temperature. At room temperature, T = 293 K , N(cm- 3) ~ 3.3 x 1016 P(torr) .

(A.29)

At standard conditions [P = 760 torr, T = 273 K(0°C)], one mole of gas (NA ~ 6.02 x 1023 molecules) occupies a volume~ 22.4 l = 2.24 x 104 cin3.

• Doppler width The Doppler width, defined as r D = 21rv · VT/ c, where v is the transition frequency, and vr = (2kBT /m) 1/ 2 is the thermal velocity, for atoms of mass M(amu) at temperature T(K) is 780 nn1 r D ~ 21r x 306 :tvIHz x '( ) x /\ 11111 T(K)

293 K x M(amu) · (A.30)

In (A.30), we normalized all the parameters on which the Doppler width depends to those of the D2 transition in 85Rb for atoms at room temperature (vr ~ 2.39 x 104 cm/s).

• Pressure broadening In the literature, pressure broadening is often given in c1n - 1 / Amagat, or MHz/ Amagat. The Amagat number (also known as relative density, r.d.)

is the ratio of the density of a gas to the density of a standard atmosphere (~ 2.69 x 1019 cm- 3 ).

Typical cross-sections for pressure broadening are (A.31)

(although in some specific cases, these cross-sections can deviate from this value by several orders of magnitude in either direction). The rate of the broadening collisions can be estimated as r rv Navr.

(A.32)

For helium at room temperature, we get r r-v 8 · 103 MHz/ Amagat. Some authors prefer to use pressure broadening per unit pressure, rather than per unit density. Our example corresponds to rv 10 MHz/torr.

UNITS, CONVERSION FACTORS" AND TYPICAL VALUES • Lifetime of an experiment It is always helpful to remember that there are only ~ 7r x 107 seconds per year, and your funding will run out in 3-5 years if you do not get a result. so yoU have only 108 seconds to complete a measurement.

## APPENDIX B

## REFERENCE DATA FOR HYDROGEN

## AND ALKALI ATOMS

The origin of the term D-line does not come, as one might think, from the fact that the D-lines of the alkali atoms come in doublets. When Joseph von Fraunhofer did his pioneering studies of dark lines appearing in the spectrum of sunlight at the tum of the nineteenth century, he did not know the origin of these lines, and TABLE B.1 Parameters of the lowest-energy resonance transitions from the ground state for hydrogen (ls --+ 2p 1; 2 ,3; 2 ) and the alkali atoms [the DI (2) transitions: ns ---+ np1/2(J/2)]- Wavelengths are given in vacuum; I ldJ 11 is the reduced matrix element in the J-basis.

Atom Upper state Energy, cm - 1 Wavelength, nm Lifetime, ns lldJII, eao H 2 2 P1;2 82258.91 121.5674 1.60 1.05 2 2 P3;2 82259.27 121.5668 1.60 1.49 Li 2 2 P1;2 14903.66 670.976 27.1 3.33 2 2 P3;2 14904.00 670.961 27.1 4.71 Na 3 2 P1;2 16956.18 589.755 16.3 3.52 3 2 P3;2 16973.38 589.158 16.2 4.98 K 4 2 P1;2 12985.17 770.109 26.2 4.10 4 2 P3;2 13042.89 766.701 26.1 5.80 Rb 5 2 P1;2 12578.96 794.978 27.7 4.23 5 2 P3;2 12816.56 780.241 26.2 5.98 Cs 6 2 P1;2 11178.24 894.595 34.8 4.49 6 2 P3;2 11732.35 852.344 30.4 6.32 Fr 7 2 P1;2 12236.66 817.216 29.5 4.28 7 2 P3;2 13923.20 718.226 21.0 5.90

REFERENCE DATA FOR HYDROGEN AND ALKALI ATOMS simply labelled them A, B, C, ... The D-line was later associated with the transiti<>II in sodium.

## APPENDIX

C

## SPECTROSCOPIC NOTATION FOR

## ATOMS AND DIATOMIC MOLECULES

Atomic states are commonly described using spectroscopic notation (see, for example, Problem 1.1 ), which designates the spin multiplicity, 2S + 1, the total orbital angular momentum, L, and the total electronic angular momentum, J in the following format: 2S+IL J· Just as for single-electron states, instead of using numbers to designate the value of L one uses letters: L=O ~ s L=l ~ p L=2 ~ D L=3 ~ F L=4 ~ G where for L > 3 the sequence proceeds alphabetically (except for the fact that the letter J is skipped). For example, an atomic state with S = l, L = 2, and J = 3 is denoted 3 D3• An analogous spectroscopic notation exists to describe the electronic states of diatomic molecules. However, there are a number of subtleties in making the transition between atoms and molecules.

First of all, in molecules the total orbital angular momentum of the electrons is not conserved because of the coupling between the motion of the nuclei and the motion of the electrons. However, diatomic molecules do possess axial symmetry about an axis passing through the two nuclei - this implies that the projection of the electrons' orbital angular momentum onto this molecular axis is conserved. Thus molecular terms can be classified according to the absolute value of this projection, A. Similar to the notation for different values of L in atoms, for diatomic molecules

SPECTROSCOPIC NOf ATION FOR ATOMS AND DIATOMIC MOLECULES we have A=O A=l A=2 Secondly, although A designates the absolute value of the projection of the or~ital ~g~lar momentum onto the molecular axis, it does not tell us the sign of this proJect1on. 1 If the molecule is reflected through a plane passing through the molecular axis, the sign of this projection changes. Performing a second reflection through this plane returns the molecule to its initial state, which means that only the sign of the wavefunction can be changed by such a reflection. Molecular states which change sign under reflection are denoted with a - and those which do not are assigned a +.

As for atoms, for molecules we must account for the total spin of the electrons.

This additional degree of degeneracy is denoted just as it is for atoms. Thus, in diatomic molecules, the spectroscopic notation for electronic terms is (C.l)

In addition, it is often useful to include the absolute value of the projection of the total electronic angular momentum (spin plus orbital, the equivalent of J for atoms) on the internuclear axis, denoted as n. This number is placed as a subscript in spectroscopic notation: 2S+lA± n· (C.2)

Finally, if the two nuclei are identical (homonuclear molecules or dimers, e.g., N2), the molecule is also symmetric about the center of mass. If we per- f onn a transformation which inverts the position of the electrons r with respect to the center of mass (r-+ -f), the square of the electron wavefunction should be invariant. 2 Wavefunctions which do not change sign under this transformation are called gerade (g) and those which do change sign are denoted ungerade (u).

These German words mean even and odd, respectively. This designation is added as an additional subscrip~ so for homonuclear diatomic molecules the complete 1 In fac~ in some texts A is allowed to take on negative values, but here we adopt the more common convention of Herzberg ( 1989).

2 Note that this transformation is not equivalent to the parity transformation (P) discussed in, for example, Problem 1.13. P would invert the positions of the electrons and the nuclei, while the transformation we discuss here only inverts the position of the electrons.

SPECTROSCOPIC NOfATION FOR ATOMS AND DIATOMIC MOLECULES spectroscopic notation is (C.3)

## APPENDIX D

## DESCRIPTION OF POLARIZATION

## STATES OF LIGHT

D.1 The Stokes parameters A common parameterization of the light polarization states [see, for example, the book by Huard ( 1997)] is in terms of the Stokes parameters Pi defined in terms of directly measurable light intensities: Po = Ix + Iy = Io, P1 = Ix - Iy, P2 = I+1r/4 - I-1rf4, P3 = I+ - J_, (D. l)

where Ix and Iy are the time-averaged intensities of the light transmitted through an ideal linear polarizer with transmission axis oriented along the x- and y-axes (the light is assumed propagating in the z-direction), I±1r/4 are the intensities mea- sured when the polarizer is oriented along ±1r / 4 to the x- and y-axes, and I+ and I - are the intensities measured with a left- and right-circular analyzer, respectively.

The Stokes parameters can also be written in normalized form: Si= Pi/Po, i = 1,2,3.

(D.2)

While strictly monochromatic light is always polarized, in general, light could be unpolarized (so the only nonzero Stokes component is Po) or partially polarized.

The degree of polarization O < p < I is defined as ✓p2 + P.2 + p2 p= I 3_ Po (D.3)

DESCRIPTION OF POLARIZATION STATES OF LIGHT TABLE D.l Jones matrices for various optical elements [Jones ( 1941 ); see also, for example, Fowles (1975) and Huard (1997)]. The Jones matrix M' for an element whose axis is rotated by some angle fJ about z is obtained by applying the usual (see Appendix E) two-dimensional rotation matrices ~(fJ): M' = ~(-fJ) . M. ~(fJ).

Optical element Axis Linear polarizer Transmission axis along x Quarter-wave plate Fast axis along x Half-wave plate Fast axis along x or y D.2 The Jones calculus Jones matrix G ~)

(~ ~i)

(~ ~1)

Another convenient representation for light polarization is the Jones vector (Jones 1941 ), which describes the complex field (D.4)

- - where ex and ey are the complex field amplitudes, as a column vector V (D.5)

Note that the position- and time-dependent phase of the electromagnetic field, ( kz - wt) where k is the wave vector and w is the light frequency, is suppressed in the Jones representation. The actual field can be obtained by taking the real part of Eq. (D.4).

The Jones calculus is particularly useful for determining the effect of linear optical elements on the intensity and polarization of a light beam. Each optical element is represented by a 2 x 2 matrix (Table D. l) which acts on the Jones vector.

## THE JONES CALCULUS

As an example, consider a light beam linearly polarized along x that passes through a quarter-wave plate with its fast axis at 45° to x. The Jones matrix describ- ing the quarter-wave plate is obtained by rotating the matrix from Table D.1: M~/4 = ~(-1r/4) · MA/4" ~(1r/4) = (-1 i) (~ ~i) ( i = 1 G + : ~ + !)

= / G !) = e:t G n · The overall phase factor can generally be ignored, yielding , 1 (1 MA/4 = y'2 i (D.6)

(D.7)

Therefore we find that the transmitted light beam emerges with left circular polarization, described by the Jones vector V' = M~14 · V: (D.8)

## APPENDIX E

## EULER ANGLES AND ROTATION

## MATRICES

An arbitrary rotation of a Cartesian coordinate frame can be described by the three Euler angles, a, /3, and,.

We assume a right-handed frame, and define a positive rotation around an axis as one resulting in a translation of a right-hand screw in the positive direction with respect to this axis. A right-handed frame of arbitrary orientation can be obtained from the original one by performing three successive rotations: • A rotation by angle a (0 < a < 21r) around the z-axis.

• A rotation by angle f3 (0 < f3 < 1r) around the y' -axis (i.e., the y-axis of the frame resulting from the first rotation).

• A rotation by angle , (0 < , < 21r) around the z" -axis (i.e., the z-axis of the frame resulting from the first and second rotations).

If a point was described by coordinates ( x, y, z) in the original frame, its coor- dinates in the rotated frame are found by successive application of three rotation matrices corresponding too, {3, and,: ( cos 1 sin , 0)

(cos {3 0 - sin , cos , sin f3 0 - s in ,8) ( cos a - som Q cos,B Sina

## COSQ

0 ~)

(n - (E. l)

In many problems it is also necessary to know how quantum mechanical wave- functions transform under rotations of the coordinate frame. For example, if we have a wavefunction for a state of total angular momentum F written in the spinor representation, how do we write it in the new frame? A general solution to this problem and a detailed discussion can be found, for example, in the book by Edmonds ( 1996 ). In short, the new spinor is obtained from the original one by applying the operator (E.2)

## EULER ANGLES AND ROTATION MATRICES

.

fo' where the exponential of an operator is defined through a series expansion, example, 1,Q: A io: A A 2 exp 7Fz = 1 + -Fz + - - Fz + • • · ( · )

· 1 ( · )

,,, Ii 1i t jS For an~ F, the exponential operators for O and 'Y are diagonal, so the~r e:eC afl'1 to multiply the component of the spinor corresponding to M by exp( iM ) we exp(iM-y), respectively. The matrices for f3 are generally nondiagonal. l{ere list them for F = 1 /2: ex i{3 p = ( cos {3/2 sin (3/2), p Ii Y - sin {3/2 cos (3/2 and for F = 1: i{3 A (½(1 t cos /3) 72 sin /3 ½{1 1 - cos{3{3)) (S.S)

exp -R = -- sin {3 cos (3 ~2 sin · Ii Y ,/2 v~ ½(1-cos/3)

- ~ sin,8 ½(1 + cos/3)

In Eqs. (E.4) and (E.5), the order of the components in a spinor is assumed con:, sponding to decreasing M. Application of these matrices is discussed, ~or exa:ofl in Problems 4.3, 4.5, 4.8, and 9.7. Formulae for the quantum mechamcal ro matrices for an arbitrary F are given by Edmonds ( 1996).

## APPENDIX F

## THE WIGNER-ECKART THEOREM AND

## IRREDUCIBLE TENSORS

F.1 Wigner-Eckart theorem A ubiquitous feature of atomic physics problems is the necessity to calculate matrix elements of operators between various atomic states. An essential tool for performing such calculations is the Wigner-Eckart theorem, 1 which states that the matrix elements of an irreducible tensor operator (we will explain a bit later exactly what is meant by this term) r; between states of a general angular momen- tum basis are given by the product of a constant independent of magnetic quantum numbers (m, m', q) and an appropriate Clebsch-Gordan coefficient: (c' ·1 'ITKlc · ) _ (f ,i'IITKll~,j) ( • 1 ·' m')

(F.l)

..,,J,m q ..,,J,m - J2j'+I J,m,K,qJ, , where the quantity (F.2)

is known as the reduced matrix element, 2 and we employ the standard general angular momentum basis l~,j,m), with J 21~,j, m) = n?j(j + 1)1~,j, m)' Jzl~,j,m) = liml~,j,m), where ~ accounts for all other quantum numbers.

(F.3)

(F.4)

1 We do not prove the Wigner-Eckart theorem here, since proofs can be found in most advanced texts on quantum mechanics, such as those by Sakurai ( 1994) and Messiah ( 1966).

2 There is also another convention for the reduced matrix element, although it is less commonly used, in which({' ,j'll1'Kll{,j) absorbs the factor J2j' +I.so the Wigner-Eckart theorem reads: (( ,j', m'l1;' I{, j, m) = (( ,j'll1'K 11{,j)(j, m, K, qlj', m').

We consistently use the definition (F. I) throughout this book.

THE WIGNER-ECKART THEOREM AND IRREDUCIBLE TENSORS The significance of the Wigner-Eckart theorem lies in its explicit separation f the matrix element into two factors: the reduced matrix element ({', j' I IT,c II{, )

which is a property of the particular physical observable being considered, and ~ Clebsch-Gordan coefficient, which depends only on the geometry of the prob1e111 i.e., the orientation of the physical observables with respect to the quantizatio ' axis. What makes the theorem so useful is that all the dependence of the matri n element on the magnetic quantum numbers is contained in the Clebsch-Go~ coefficient. This allows one to easily determine matrix elements for all values of q, m, and m' once the feat has been accomplished for one particular case.

Before we proceed, it is necessary to specify what we mean by an irreducible tensor operator. For now we will just present the formal mathematical definitions and postpone until later further discussion of tensors and reducibility.

' A collection of 2K + 1 operators r;, where q = - K, . . . , K, is defined to be an irreducible tensor operator if [ Jz, r:] = tuJT: , [J±, r;] = nJK(K + 1) - q(q ± 1) T~ 1 , where J± are the raising and lowering operators J+ = Jx + iJy, J_ = Jx - iJy, so that (F.5)

(F.6)

(F.7)

(F.8)

J±l~,j, m) = nJj(j + 1) - m(m ± 1) l~,j, m ± 1).

(F.9)

Note that Eqs. (F.5) and (F.6) for irreducible tensor operators are analogous to Eqs. (F.4) and (F.9), where instead of operating with Jz or J± on a basis state, we form the commutator with a tensor operator. As q varies from -K, to +K,, the r;'s are the 2K + 1 components of the rank K irreducible tensor operator. From Eqs. (F.5) and (F.6), one can also derive: (F. 10)

where summation over the repeated index i is implied. From the above relations we see that "" is analogous to j, and q is analogous to m.

In order to gain intuition about the Wigner-Eckart theorem, it is helpful to consider some concrete examples. To simplify matters, let us investigate matrix elements between one and the same state, which are simply expectation values of the physical observable to which T;, corresponds. In this case, the Wigner-Eckan

## WIGNER-ECKART THEOREM

theorem reads: (TK) - ( C : IT"' IC : )

( ~' j II TK II {' j) ( .

I . )

q - ..,,J,m q ..,,J,m = J2j+l J,m,K,qJ,m.

(F. 11)

As our first example, we consider the spin-orbit Hamiltonian H80 = AL · § from Problem 1.3 for an atom with total angular momentum J = l + S. We begin by verifying that Hso is an irreducible tensor operator with respect to J and deter- mining its rank. 3 The spin-orbit Hamiltonian can be written as [see Problem 1.3, Eq. ( 1.32)]

A ( 2 2)

Hso = 2 J - S - L .

(F.12)

Thus we have (F.13)

Similarly, one can show that [J±, H 80 ] = 0. Therefore H 80 is, indeed, an irre- ducible tensor operator with K = 0 and q = 0. Such an operator is known as a scalar operator.

What does the Wigner-Eckart theorem say about scalar operators like Hso?

From Eq. (F.11) we have (H ) - (~,JIIHsoll~,j) (. . 0 01 · ' )

so - .

J, 1n, , J, m .

✓2J + 1 (F.14)

The Clebsch-Gordan coefficient is (j, m, 0, 0jj, m) = 1, so immediately we see that the expectation value of H80 is independent of m. This makes sense, because different Zeeman sublevels correspond to different orientations of the atomic system with respect to the quantization axis, but (H80 ) is independent of such orientation. 4 One may be tempted to think that any scalar quantity corresponds to a rank zero irreducible tensor operator. However, this turns out not to be the case. Consider the Hamiltonian H B describing the interaction of a magnetic field B with an atomic 3 Since the definitions (F.5) and (F.6) depend on the angular momentum J, the irreducible tensor is said to be defined with respect to a particular angular momentum operator, e.g., l, 1, or F.

4 Note that the hyperfine Hamiltonian considered in Problem 1.11, H hf = af · S, is a scalar operator with respect to the total angular momentum F (in general, Hamiltonians constructed only from internal atomic vectors like f, l, etc. are scalar operators). This means that the matrix elements are proportional to (F, MF, 0, OIF', M~), so Hhr can only mix states for which F = F' and M~ = MF.

THE WIGNER-ECKART THEOREM AND IRREDUCIBLE TENSORS state having magnetic moment µ: HB = -µ· B.

(F. 15)

HB is certainly a scalar, but if it were a rank-zero irreducible tensor operator, according to Eq. (F.14), each of the Zeeman sublevels would have the same energy.

We know from experiment that this is not the case.

The key point is that a scalar operator is defined to be an operator which is invariant under rotation of the atomic system with respect to the quantization axis.

When the atomic system is rotated, the direction of the magnetic dipole moment µ changes, but the external magnetic field B remains fixed with respect to the quantization axis. Thus the magnetic field has broken the spherical symmetry.

Based on the principle that scalar operators are invariant under rotations, scalar operators S must satisfy [J,s]

=0.

(F.16)

It is straightforward to verify that if S commutes with J, it will commute with Jz and J±, thereby satisfying conditions (F.5) and (F.6) for an irreducible tensor operator with "' = o.

If we choose our quantization axis z to be along the magnetic field B, we have (F.17)

One can use Eq. (F.17) to show that [ J, H 8 ] 'f" 0, verifying that H B is not a rank-zero irreducible tensor operator.

How can we use the Wigner-Eckart theorem to find the expectation value of HB? It turns out thatµ= g;JJ,olis a vector operator, and we can use the Wigner- Eckart theorem to find the expectation value (µ,). Forming the dot product of (µ)

with B yields (H8 ).

What is a vector operator? A vector operator V is defined to be a vector of operators, (F.18)

which satisfy (F.19)

where Eijk is the Levi-Civita completely antisymmetric tensor. 5 In order to use the Wigner-Eckart theorem, we must express the vector operator as an irreducible 5 This definition is intimately linked to the fact that angular momentum operators are the generators of infinitesimal rotations (Sakurai 1994 ).

## WIGNER-ECKART THEOREM

spherical tensor. To do so, we write V in the spherical basis: ,.

1 (""

'"")

e_ 1 = /2 X - iy , (F.20)

(F.21)

(F.22)

which, one can see, is complex and orthonormal ( e• . eq' = 6qq' ). The components of a vector operator in the spherical basis, q V 1 = - ~ (V x + iV y) , Vo= Vz' V_1 = ~(Vx - iVy), (F.23)

(F.24)

(F.25)

tum out to be the components of a rank-one irreducible tensor operator, for which K = 1 and q = 1, 0, -1. The vector V is expressed in terms of V q via (F.26)

Note that the scalar product of two vectors a and b, expressed in spherical coordinates, is given by ii. b = (a1ei + aoeo + a_1e~i) · (biei + 1>oeo + b_ie~i)

= {a1ei + aoe0 + a_1e~ 1) · (-b1e-1 + boeo - b_1ei)

= -a1b-1 + aobo - a_1b1 = L)-l)qaqLq, q (F.27)

(F.28)

(F.29)

(F.30)

where we have made use of the facts that e±1 = -e=f1 [see Eqs. (F.20) and (F.22)]

d .... "

~ an eq · eq' = uqq'· In fact, the result (F.30) can be generalized to irreducible tensors of arbitrary rank K: r(K>. u(ic> = ~)-1)qr;u~q.

(F.31)

q Consider the expectation value of a vector operator (V). According to the Wigner-Eckart theorem [Eq. (F.11 )] the expectation values of the components of

THE WIGNER-ECKART THEOREM AND IRREDUCIBLE TENSORS FIG. F.l The average value (denoted by the dashed arrow) of a vector v associated with a system that rotates with angular frequency w points along the rotation axis. This is an example of the basic concept underlying the Wigner-Eckan theorem.

V satisfy (V) = ({,JIIVll{,j)(.

1 11· m).

q J2j + 1 J, m, 'q ' (F.32)

Note that, in fact, J itself is a vector operator [this can be checked using Eq. (F.19)],6 so (J.) = ({,illJll{,i) (.

1 qfJ. m).

q J2j + 1 J, m, ' ' (F.33)

Comparing Eqs. (F.32) and (F.33) we see that (V) oc (i) , (F.34)

so the expectation value of any vector operator is always along the direction of the total angular momentum.

This result can be understood intuitively by considering a vector iJ associated with a rotating system (Fig. F. l ). Because the components of the vector which are not along the rotation axis are averaged out, the average value of the vector quantity must be along the rotation axis.

The Wigner-Eckart theorem is applied to a variety of atomic physics problems throughout this book. It is especially useful when one needs to calculate a matrix 6 Since P, = gJ µ,of, and j is a vector operator, it follows that P, is also a vector operator. This verifies our earlier claim regarding the calculation of (H s ).

## IRREDUCIBLE TENSORS

element between different states, since the Clebsch-Gordan coefficients immedi- ately provide selection rules for the matrix elements, and for nonzero terms they give the relative signs and magnitudes for different values of m,, m.', and q.

F.2 Irreducible tensors In this section, we discuss some basic examples of Cartesian tensors and their properties. A simple way to produce a rank-two tensor ~j is to construct what is known as a dyadic out of the Cartesian components of two vectors a and b: (F.35)

Such a tensor has nine components, and transforms under a spatial rotation by applying two rotation matrices ~J (one for each vector): T,,m = R,niRnjTij = RrniRnjllibj = RmiaiR,,,jbj = ambn .

(F.36)

(F.37)

This is in contrast to a vector, which transforms under rotations by applying one rotation matrix: (F.38)

and scalars, which are invariant under rotations. Generally, this is how the rank of a tensor is defined, by how many rotation matrices are required to transform the object under a spatial rotation.

However, it turns out that the dyadic described by Eq. (F.35) is reducible, mean- ing that it can be decomposed into an object that transforms like a scalar, an object that transforms like a vector, and an object that transforms like a second-rank tensor. Specifically, this is done as follows: (F.39)

The first term is a scalar (invariant under rotations), the second term is directly related to the vector product ii, x b, which behaves as a vector under rotations, and the final term is a symmetric traceless tensor of rank two. These tenns are known as irreducible tensors because, unlike the dyadic (F.35), they cannot be decomposed into tensors of lower rank.

THE WIGNER-ECKART THEOREM AND IRREDUCIBLE TENSORS Note that each of the terms in our decomposition of the dyadic (F.35) has 2tt+ 1 independent components: T (o) _ a-b~ ..

ij - U1,J has only one independent component, (F.40)

(F.41)

has three independent components, corresponding to the components of ii x b, and T(~) = (aibj + ajbi) _ ii· b ~.

.

~ .

(F.42)

has five independent components, since it is both symmetric and traceless. That gives 1 + 3 + 5 = 9 independent components, so we have recovered the original number of independent components of the dyadic.

Evidently, we can put the independent components of an irreducible rank- two Cartesian tensor ~~ 2> in correspondence with the 2K + 1 components of an irreducible spherical tensor TJ.

The relationship between the Cartesian tensor components ~~ 2> and the irreducible tensor components TJ are as follows [see, for example, Varshalovich et al. ( 1988)]: TJ = T;;), Tl1 = ~JI ( TJ~> ± iTJ:>)

, T2 = fi(T(2) - r.(2) ± 2iT( 2>)

±2 y 6 xx uu xu .

(F.43)

(F.44)

(F.45)

The decomposition of higher-rank tensors becomes quite complicated: for instance, from the 27 independent Cartesian components of a third-rank tensor, one can construct seven irreducible tensors ( one zero rank, three first rank, two second rank, and one third rank)! Not to mention that the decomposition is not umque.

For more detailed discussions of tensors and tensor operators, see texts such as Fano and Racah (1959) and Zare (1988).

## APPENDIX G

## THE DENSITY MATRIX

The density matrix is a tool which makes it possible to describe ensembles 1 of quantum systems (e.g., atoms) that are more general than the ensembles which can be described by a wavefunction. In this appendix, we review the basic properties of the density matrix and offer a few examples to illustrate how it can be used. The examples are intended to be simple enough to be solved without the density matrix (usually just by thinking for a moment!), and are merely intended for illustration.

For more detailed discussions, see, for example, the books by Stenholm ( 1984)

and Blum ( 1996).

G.1 Connection between the density matrix and the wave- function The key point of the density matrix is that it is a more general description of an ensemble than a wavefunction. A wavefunction can only describe an ensemble that is fully coherent (or pure), while the density matrix can also describe partially coherent or incoherent ensembles. What does this mean? Let us consider a simple example. Suppose we have an ensemble of N spin- I /2 atoms and consider only their internal states. If all of the atoms are in the same state, e.g., (G. I)

then we say that the ensemble is in a pure state. In this case, the wavefunction l'l/J)

is sufficient to describe the behavior of the entire ensemble.

Now suppose that the atoms undergo collisions 2 which change the relative phase between the spin up and spin down components for each atom in a random 1 An ensemble can either be assembled spatially (e.g., atoms contained in a vapor cell) or consist of sequential measurements separated temporally (under proper circumstances, this could even be a single quantum system).

2 Relaxation processes, such as collisions and spontaneous emission, tend to destroy coherence, and it turns out that such decoherence is one of the primary reasons that quantum-mechanical behavior is so difficult to observe in macroscopic systems.

## THE DENSITY MATRIX

way, so now, at a particular time, we have for the state of the i-th atom (G.2)

where <Pi is the aforementioned random phase.

The ensemble is now in a mixed state which could be described by a product wavefunction 1'11) of all the individual l,,t,(i)), N 1'11) = I1 IV'(i)) · (G.3)

i=l but for a gas of atoms consisting of, for example, 1012 atoms, it would be infeasible to try to keep track of the states of all atoms. It is also often unnecessary, since in many experiments we are interested only in the average properties of the atoms in the ensemble. [Note, however, that in the emerging field of quantum inf ormation the goal is indeed to keep track of many - or even all - of the parameters in a many-particle wavefunction such as the one written in (G.3).] Clearly, we require a formalism that will allow us to easily write down these average properties, which is exactly the purpose of the density matrix.

In general, the quantum mechanical state of the i-th atom, 11/J(i)(t)), can be written as a superposition of the available atomic states (G.4)

where the states Im) constitute an orthonormal basis for the system. We will now see how all of the information contained in the wavefunction 11/J(i)(t)) is also contained in the density matrix, whose elements P~n are given by P~n = c~(t) c~\t)* .

(G.5)

In our example of the internal states of a gas of spin-1/2 atoms, Eq. (G.4)

reduces to (G.6)

The expectation value of a physical observable, for example the projection of spin along the quantization axis Sz, is given by (G.7)

(G.8)

(G.9)

CONNECTION BETWEEN THE DENSITY MATRIX AND THE WAVEFUNCTION We can also write this expectation value in the following way: (G.10)

m,n We can write out the expression (G. I 0) for case of spin-I /2 atoms (Sz) = p~~(+ISzl+) + p~~(-ISzl+) + p~~(+ISzl-) + p~~(-ISzH, (G.11)

and since Sz is diagonal, we have (i)

(i)

(Sz) = P++(+ISzl+) + p __ (-ISzl-), = ~lc~l(t)i2-~jc~\t)j2, (G.12)

(G.13)

reproducing the result (G.9). The important point here is that the matrix (G.5) con- tains all the information about the atomic wavefunction. An even more convenient way to express the expectation value is (G.14)

where we use the matrix representation for the operator and, for the spin-I /2 case we have been considering, ( (i)

(i) )

(i) = P++ P+- .

p (i)

(i)

P-+ p __ (G.15)

Noting that Tr (p(i)] = 1 (since the trace of the matrix represents the total popula- tion which is one in this case), it can be readily verified that Eq. (G.14) reproduces (G.9): (G.16)

= Tr [ (p~~ p~~)

. (fi/2 0 )]

(i)

(i)

-fi/2 ' P-+ p __ (G.17)

Ii (i)

Ii (i)

= 2P++ - 2P-- .

(G.18)

This result can be generalized to any operator 0: the expectation value is (G.19)

## THE DENSITY MATRIX

G.2 Ensemble-averaged density matrix As one would guess, the measurable properties of a generic ( coherent or inco- herent) ensemble of many quantum systems is the average of the expectation values: (G.20)

N - 1 ~~ (i)

- N L..,L..,Pmn(nlSzlm), i=l m,n (G.21)

where (Sz) denotes the average over the entire ensemble. We can rearrange the factors in the sum (G.21) in the following manner -- ~ ( 1 ~ (i))

(Sz) = ~ (nlSzlm)

N {;;r Pmn , (G.22)

so it now makes sense to define N 1 ~ (i)

Pmn = N L.., Pmn (G.23)

i=l to be the elements of the ensemble-averaged density matrix (we will commonly refer to the ensemble-averaged density matrix as, simply, the density matrix). We can now write an equation analogous to (G.14) for the ensemble average: (s ) _ Tr[p · Sz]

z - Tr[p] · (G.24)

The probability that an atom in the sample is in state Im) is given by the diagonal tenns in the density matrix Pmm (populations); the off-diagonal elements Pmn (m ~ n) describe the degree of coherence between the states Im) and In).

Let us return to our example of spin- I /2 atoms. Now we will consider two samples of atoms, one that is fully polarized in the state (I+) + I-))/ v'2, Ppol = ~ G D , (G.25)

and one that is completely unpolarized with an equal mixture of atoms in I+) and 1-), 1 (1 0)

Punpol = 2 0 1 , (G.26)

where Ppo1 and Punpol are the normalized (Tr[p] = 1) density matrices for the respective ensembles. Note that the density matrix Punpol can only correspond to

## ENSEMBLE-AVERAGED

## DENSITY MATRIX

an incoherent ensemble (or statistical mixture) of atoms - an ensemble in a pure state cannot have such a density matrix (because there will necessarily be non-zero off-diagonal elements)!

Both ensembles have zero net polarization along the z-axis, as is readily verified using Eq. (G.24): (Sz)po1 = Tr[/Jpol · Bz] , _ [ 1 (1 1) (/i/2 0 )]

-Tr 2 1 1 .

-/i/2 ' [h(l -1)]

= Tr 4 1 -1 = 0' and (Sz)unpol = Tr[Punpol · Sz] ~ [1 (1 0) (/i/2 0 )]

= Tr 2 0 1 .

-/i/2 ' =Tr[:G ~1)]

=0.

(G.27)

(G.28)

(G.29)

(G.30)

(G.31)

(G.32)

However, the polarized sample does have a nonzero (and, in fact, maximal)

projection of spin along the x-axis (Sx)po1 = Tr[ppol · Sx] , = TrUG U · (/i~2 /i~ ) J, =Tr[:G U] = ~' whereas for the unpolarized sample, as we know, (Sx)unpol = 0: (Sx)unpol = TrU(~ n-(1t~2 /i~2)], =Tr[:(~ ~)] =0.

(G.33)

(G.34)

(G.35)

(G.36)

(G.37)

## THE DENSITY MATRIX

G.3 Time evolution of the density matrix: the Liouville equation The next important issue is to detennine how the density matrix evolves in time.

Given Eqs. (G.5) and (G.23), we see that ~ -~.;...

(ac~ (i)• (i) a~>*)

f)tPmn - N ~ &t en + cm 8t .

i=l (G.38)

From the Schrodinger equation, (G.39)

where His the Hamiltonian for the system, and with the expansion (G.4), we have (G.40)

Multiplying both sides of Eq. (G.40) by (kl and taking into account the orthonor- mality of the basis states yields the expression 8c(i)

~ = iii L (klHlm)c~(t).

(G.41)

This result can be used in Eq. (G.38) to obtain an expression for the time-evolution of a particular element of the density matrix: = ·n L ( (mlHlk)Pkn - Pmk(klHln)) .

Z k (G.43)

The above expression (G.43) can be rewritten in tenns of matrices, yielding dp I dt = ili[H,p]' (G.44)

which is known as the Liouville equation. This is the essential equation which governs the time evolution of the density matrix. Note that, so far, we have not included any relaxation in the problem.

TIME EVOLUTION OF THE DENSITY MATRIX: THE LIOUVILLE EQUATION Now let us return to the example of an ensemble of spin-1/2 atoms. Sup- pose that the atoms are immersed in an x-directed magnetic field B = B0x. The Hamiltonian for this system is H = -µ · B = gµoBoSx, = gµoBoli (0 1)

1 0 .

Using the above Hamiltonian in the Liouville equation (G.44), we obtain (G.46)

P+-) . (0 1)]

P-- I (G.47)

This gives us a set off our coupled differential equations for the four density matrix elements.

Next we analyze the behavior of this system for a variety of initial conditions.

We know that an unpolarized sample should not change under the influence of the magnetic field (neglecting, of course, thermal redistribution of population between the levels, which would involve some sort of relaxation mechanism). This can be verified using the Liouville equation and Punpol [Eq. (G.26)] as our initial condition, from which we find that 8p/8t evaluated at t = 0 is zero. Since none of the populations or coherences change initially, we can extrapolate to say that they are all constant in time.

Now consider an ensemble of atoms initially polarized along - z, so for the initial density matrix we have (G.48)

When this sample of atoms is suddenly exposed to the magnetic field, we expect them to precess with the Larmor frequency nL = gµoBo about the x-axis. Let us just consider short times 8t << nL 1, for which we expect the population of the I+)

state to grow quadratically in time (see, for example, Problems 2.6 and 3.1 ). The time derivative of P++ is proportional to the difference between the coherences, so

## THE DENSITY MATRIX

first we evaluate the time dependence of the coherences 8P+-1 _ igµoBo igµ 0Bo at t=O - lP++(O) - /J--(0)] = - , aP-+ I - igµoBo igµoBo Ot t=O - [P--(O) - P++(O)] = + · Using these expressions, (G.49) and (G.50), we indeed obtain 92µ2 n2 P++(6t) ~ o o ('5t)2 • (G.49)

(G.5O)

(G.50 Finally, we note that relaxation processes can be included in the Liouville equa- tion (also known as the equation of motion) by various means depending on tbe exact nature of the relaxation mechanism [see, for example, Stenholm (1984)). If the relaxation can be described simply as an exponential decay of the populations (for example, due to spontaneous emission to unobserved levels), then one maY use a diagonal relaxation matrix r (G.52)

where ,n is the relevant decay rate of the population of a particular level and hmn is the Kronecker delta. Then the equation of motion can be written as (G.53)

G.4 Atomic polarization moments The density matrix of an ensemble of atoms in a state with angular momentum F has {2F + 1) x {2F + 1) components PM,M', where M, M' refer to Zeem~ sublevels. The density matrix p can, in fact, be thought of as a tensor, and it is often useful to work with the irreducible components of p (see Appendix F).

One can represent p in the following way [see, for example, Omont ( 1977) and Varshalovich et al. ( 1988)]: 2F K P = L L pt>rt>, (G.54)

K=Oq=-K where TJk) are irreducible tensor components represented as (2F + 1) x (2F + 1)

matrices, and the coefficients p~K) with "" = 0, ... , 2F and q = -K, ...

,"" are

## ATOMIC POLARIZATION MOMENTS

called state multipoles. The p~K) are related to the PM.M' by F p~tt) = L (-l)F-M'(F,M,F,-M'IK,q)pM,M'.

M,M'=-F (G.55)

If the coefficients pt) are known, the density matrix PM.Al' can be reconstructed by a transformation inverse to Eq. (G.55): (G.56)

K,Q The representation of the operators rJ"") in the M, M' basis can be obtained using Eq. (G.56). For example, for F = 1, substituting p~"") = 6"",o6q,o we get T}O) = _l_ (~ D· (G.57)

v'3 0 substituting pt) = 8tt, 18q,o we obtain (1 D· Tt(l) = _1_ (G.58)

v'2 0 d fi (K)

- an or Pq = dK,2 q,o TJ2J = _1 (,~ V· (G.59)

v'6 0 The following terminology is used for the different state multipoles: p(O) - monopole moment (which is equal to the population divided by J2F + 1), p(I)

- vector moment or orientation, µ{2) - quadrupole moment or alignment, p( 3) - octupole moment, and p( 4) - hexadecapole moment. 3 Each of the moments p(K)

has 2K + 1 components.

The term polarization is used for the general case of an ensemble that has any moment with K > 0. When the Zeeman sublevels are not equally populated, p~tt) # 0 for some K > 0, and the medium is said to have longitudinal polarization.

3 There are other definitions of the terms "orientation" and 0 alignment" in the literature. For example, Zare ( 1988) designates alignment as any of the even moments in atomic polarization (quadrupole, hexadecapole, etc.), while he identifies orientation with the odd moments (dipole, octupole, etc.).

## THE DENSITY MATRIX

When there are coherences between the sublevels, p~"') =j; 0 for some q ~ o, and the medium is said to have transverse polarization. For a given quantization axis th 1 ·rud· 1 · · ( 1)

· (2)

• z, e ong1 ma onentat1on Po and longitudinal alignment Po are given by (I)

Po <X (Fz), P& 2> ex (3F; - F 2), (G.60)

respectively. One can explicitly see how these equations come about for the case of F = 1 by inspecting Eqs. (G.58) and (G.59).

Note also that optical pumping with circularly polarized light (in the absence of other external fields) generally creates multipoles of all orders (tt < 2F), while pumping with linearly polarized light creates only even-ordered multipoles. This latter fact is a consequence of a symmetry that is most clearly seen when the quan- tization axis is along the light polarization direction: in this case, it is clear that linearly polarized light creates no preferred direction in space, only a preferred axis.

To illustrate these points and gain some experience with the polarization moment formalism, let us consider the density matrices describing an ensemble of atoms with F = 3/2 in the ground state that are optically pumped by light near-resonant with a transition to an excited state F' = 1 /2. We assume that the excited state decays primarily to other states (an open system). This is exactly the situation considered in Problem 3.10, where it was found that if one pumps with u + light, the equilibrium density matrix is 1 0 0 0 1 0 1 0 0 p( q +) = 2 0 0 0 0 ' 0 0 0 0 while for light linearly polarized along x we obtain p(x) = 8 v'3 0 v'3 v'3 0 v'3 (G.61)

(G.62)

where here we have normalized the density matrices so the population is unity.

Now we wish to calculate the state multipoles for these ensembles. We can rewrite Eq. (G.55) in the following manner (G.63)

## ATOMIC POLARIZATION MOMENTS

where T(K, q) is a (2F + 1) x (2F + 1) (in this case, 4 x 4) matrix whose elements are given by TM,M 1 (K,q) = (-l)F-M'(F,M,F,-M'IK,q).

(G.64)

For example, we can calculate the monopole moment for both ensembles: (0)

Po (a+)= Tr[p(a+) · T(O,O)]

1 0 0 0 1/2 1 0 1 0 0 1/2 (G.65)

=Tr - = - ' 2 0 0 0 0 1/2 0 0 0 1/2 which agrees with the fact that the monopole moment is the population divided by ✓2F + 1. For pumping with x-polarization, p& 0\x) = Tr[p(x) · T(O, O)]

✓3 =Tr 8 J3 ✓3 ✓3 1/2 1/2 1/2 1/2 - (G.66)

What about orientation? Let us find the longitudinal orientation p& > for both ensembles: p&1)(a+) = Tr[p(a+) · T(l,O)]

1 0 0 0 =Tr 1 0 1 0 0 2 0 0 0 0 0 0 0 0 2v'5 2v'5 (G.67)

so as expected we find that the ensemble which had been optically pumped by circularly polarized light is oriented along z, whereas p& 1\x) = Tr[p(x) · T(l, O)]

✓3 2v'5 ✓3 = Tr - 2v'5 =0, ✓3 - 2v'5 v'3 0 - 2"'5 (G.68)

## THE DENSITY MATRIX

TABLE G.1 Values of various multipole moments of an F = 3/2 ground state which has been optically pumped by either u + or x-polarized light resonant with a F = 3 /2 --+ F' = 1 /2 transition. The highest multipole moment in this system corresponds to "' = 2F = 3. Note that in this special case, optical pumping with circularly polarized light does not create any alignment, which is not generally the case for an arbitrary F -+ F' transition.

Multipole a+ X Monopole (0)

Po (I)

P1 Dipole (orientation)

( 1)

Po 7s (I)

P-1 (2)

P2 (2)

P1 Quadrupole (alignment)

(2)

Po (2)

P-1 (2)

!~ P-2 (3)

P3 (3)

P2 (3)

P1 Octupole (3)

Po -ws (3)

P-1 (3)

P-2 (3)

P-3 so, as we know from symmetry, the sample optically pumped with x-polarized light is not oriented along z. Similar calculations can be performed for all the remaining possible polarization moments, and the results are shown in Table G.1.

## APPENDIX H

## ELEMENTS OF THE FEYNMAN

## DIAGRAM TECHNIQUE

In this appendix, we briefly review some of the most basic elements of the diagram technique for calculating transition amplitudes and probabilities in the framework of time-dependent perturbation theory. Feynman diagrams provide a very simple and convenient pictorial way of understanding the process, and also allow one to write down the mathematical expression for the transition amplitude (see Problems 3.16, 3.17, and 4.2). For a more detailed and rigorous discussion of the diagram technique, the reader is referred to, for example, the texts by Delone and Krainov ( 1985) and Cohen-Tannoudji et al. ( 1992). The use of the diagrams for calculating linear and nonlinear susceptibilities x(n) is discussed by Delone and Krainov ( 1985).

The starting point for our discussion is Fermi's Golden Rule: 21r Wji = filVJil P1(E), (H.I)

which relates the transition rate WJi from state f i) to state I/) with the matrix element of the perturbation VJi· Here p1(E) is the density of the final states in the energy space. The diagrams represent various contributions to the amplitude VJi• (t)

..

(t) ..

k k (t)

w FIG. H. l The two Feynman diagrams representing elastic photon scattering.

## ELEMENTS OF THE FEYNMAN DIAGRAM TECHNIQUE

On a Feynman diagram (Fig. H. l) often used in atomic and molecular physics and ~ptic_s, the evolution of atomic states is represented by vertical solid lines, and the ttme 1s assumed to increase from bottom to top. 1 Photons are shown by wavy lines propagating at an angle to the atomic state line (the trunk) of the diagram.

The intersection point between a photon line and the trunk is called a vertex. A photon line either ends in (photon absorption) or begins with (photon emission) a vertex.

The amplitude corresponding to a single diagram is constructed using the fol- lowing rules that follow from time-dependent perturbation theory and the quantum mechanical description of the electromagnetic field.

• Beginning from the bottom of the trunk and moving upwards, for each of the vertices, one writes the corresponding coupling strength as a product factor.

For example, using the electric dipole approximation for each of the absorp- tion/emission processes, the coupling factor is dmn, the dipole matrix element between the atomic states above and below a vertex.

• Each of the segments between two vertices is represented by a propagator ( each propagator enters the expression as a multiplicative factor)

Em + E hwm - ( Ei + E hwi) ' (H.2)

where Em and Ei represent the energies of the m-th and the initial state, and the sums are over the photon energies present in that state. When the considered process is near-resonant, i.e., when the propagator has a near-zero denominator, one needs to include the widths of the level by replacing E; with Ei - if i/2.

• Each incoming and outgoing photon line corresponding to a photon of frequency wa and polarization ea is represented by a multiplicative factor -i J21rhw 0 • eo incoming photon, iJ21rhw 0 • e; outgoing photon, (H.3)

(H.4)

respectively. These quantities are normalized to unit volume, so one need not explicitly write the volume neither here nor in the density of states.

• When there are nke photons (at a time corresponding to the bottom of the diagram) in the mode corresponding to an incoming photon, the factor (H.3)

should be multiplied by ..jnj;;.

• When there are nke photons (at a time corresponding to the bottom of the diagram) in the mode corresponding to an outgoing photon, the factor (H.4)

should be multiplied by v'nke + 1.

1 Note that there are numerous ways that Feynman diagrams are drawn in tenns of the direction of time, the meaning of various line shapes, etc.

## ELEMENTS OF THE FEYNMAN DIAGRAM TECHNIQUE

IS, 2P, M 1==0 FIG. H.2 The Feynman diagram describing radiative decay of an excited atomic state.

In the limit of a large number of photons in the mode where the photon field can be described classically, the photon factor is proportional to the amplitude of the electric field.

In order to find the amplitude v1i, one needs to sum the amplitudes correspond- ing to each of the possible distinguishable diagrams for a given process.

As a simple example illustrating the use of the Feynman diagrams, consider spontaneous radiative decay of the l2P, Mi = 0) state of hydrogen (Fig. H.2) (of course, all sublevels decay at the same rate).

Following the rules outlined above, one finds that for light-polarization direction at an angle 9 to the z-axis, V ·-'2 !iw d- -· .

( ) ~ l(JlldllJ')I ~2 (9)

= iv 7r • e = idz cos e v 27l"W = y'3 v ~1rW cos .

(H.5)

Substituting this into Eq. (H. I), and employing for the density of final states (tak- ing into account from energy conservation that !iw = E2p) the expression (see Problem 3.3)

2w2 PJ = (21r)2n2c3' we finally detennine the radiative width: r _ w. _ 2271"

l(JlldllJ')l2 2w 4l(JlldllJ')l2w - Ji - 3h 21rw (21r)2c3 - 91ic3 (H.6)

(H.7)

Here the factor 2/3 comes from the solid-angle integration of cos 9. The above for- mula (H.7) can be compared to Eq. (3.115) from Problem 3.3, which was derived without appealing to the Feynman diagram technique.

## APPENDIX I

## THE 3-J AND 6-J SYMBOLS

## 1.1 3-J symbols

Calculations in atomic physics often require changes of basis between eigenfunc- tions of different operators. One of the most common scenarios (at least in this book) is a change of basis between eigenfunctions of the angular momentum operators {Jr, Jiz, J?, J2z} (the uncoupled basis I J1, M1) IJ2, M2)) and eigen- functions of the operators {Jr, J?, J 2, Jz} (the coupled basis I J, M) ). For the most part, introductory quantum texts employ the Clebsch-Gordan coefficients to go between these different bases using the well-known formulae: IJ,M) = L (J1,M1,hM2IJ,M)IJ1,M1)lhM2), (I.I)

IY/1 ,M2 IJ1,M1)lhM2) = L(J1,M1,hM2IJ,M)IJ,M)

· (1.2)

J,M Most of the problems in this book can be solved easily enough by using the Clebsch-Gordan coefficients, but in a few problems it is helpful to employ an alternative formulation of the expansions (I.I) and (1.2) that uses the Wigner 3-j symbols (or simply, the 3-j symbols). The 3-j symbols, written as 2 x 3 matri- ces in parentheses, are directly related to the Clebsch-Gordan coefficients in the following way (Sobelman 1992; Varshalovich et al. 1988; Judd 1998)

(1.3)

Since the usual phase convention for the Clebsch-Gordan coefficients is chosen so that they are all real, the 3-j symbols are real as well. Furthermore, the trian- gular condition and the projection rule for the Clebsch-Gordan coefficients must necessarily carry over to the 3-j symbols, so that a 3-j symbol is zero unless it

satisfies and

## THE 3-J AND 6-J SYMBOLS

(1.4)

(1.5)

The advantage of using 3-j symbols is that they are designed to show the implicit symmetry relations of Eqs. (I.I) and (1.2) in a transparent and systematic way. For example, the Clebsch-Gordan coefficients obey the following relation: (J1,M1,J2,M2IJ,M) = (-I)J 1+J2 -J(J2,lvf2,J1,M1IJ,M).

(1.6)

This relation can be expressed using 3-j symbols by noting that, according to Eqs. (1.3) and (1.6), odd permutations of the columns of the 3-j symbol obey ( J1 J2 J) = (-I)J1+h+J ( J2 J1 J)

.

(1.7)

## M1 M2 M

/.th M1 M Furthermore, even permutations of the columns leave the value of a 3-j symbol unchanged: (ill f;2 it)= (it fA /J2)

= (;J2 it ti) .

(I.S)

One of the consequences of Eq. (1.7) is that all 3-j symbols with two identical columns are zero if J1 + J2 + J is odd, since if, for example, J1 = J2 = j and M1 = M2 = m, then Eq. (1.7) implies (! ! it) = (-1)2j+J (! ! it) ' (1.9)

which can only be satisfied if 2j + J is even or if (1.10)

A special case of this is the selection rule considered in Problem 9.5, where there is a dipole transition (K = 1) between a ground state and excited state with the same total angular momentum F = F'. The amplitude for a transition between the M = 0 and M' = 0 sublevels, A(M = 0 -+ M' = 0), is described by a matrix element involving the Clebsch-Gordan coefficient (F, 0, 1, OIF, 0), and so from Eqs. (1.3), (1.8), and (I. I 0)

A(M = 0-+ M' = 0) ex (~ ~ ~) = 0, (1.11)

since 2F + 1 is odd.

3-J SYMBOLS There are other simply stated symmetry relations involving 3-j symbols, such as (1.12)

and the sum rules derived from the orthonormality conditions for Clebsch-Gordan coefficients L(2J+I)

(fl J,M (1.13)

(1.14)

Clearly, any relation expressed in terms of the Clebsch-Gordan coefficients can be re-expressed in terms of the 3-j symbols. For example, the Wigner-Eckart theorem [Eq. (F.I)], (~, ., 'I K,I . )

(t,i'IITKll~,j) (.

, ., ')

._ ,J ,m Tq t,,J,m = J2j'+ 1 J,m,K,QJ ,m , can be re-written by substituting for the Clebsch-Gordan coefficient ( · I ·I ')

- (-1)-j+K-m' ✓2 ., + 1 (j Ii j' )

(I. 15)

J, m, K, q J , m - J q -m' ' an expression which can be derived from Eq. (1.3 ). Using (1.15) in (F. I) yields (t.',j', m'Ir;1u, m) = {-1)-j+K-m' (t.',/IITKIIU) (! ; _i~,) .

(1.16)

Employing Eq. (I. 7) to make another substitution, namely ( j K j' ,) = ( - I )j+K+j' ( j' , "' mj) , (1.17)

q -m -m q gives us the more elegant form of the Wigner-Eckart theorem, (t,',j', m'IT;lu, m) = (-1)i'-m' (t.',/IIT"IIU) ( _i~, ; !) . (1.18)

Much more infonnation about 3-j symbols (as well as 6-j and 9-j symbols)

can be found in the books by Sobelman ( 1992), Varshalovich et al. ( 1988), and Judd ( 1998), and symbolic and numerical values can be easily evaluated using programs such as Mathematica®.

1.2

## THE 3-J AND 6-J SYMBOLS

6-J symbols We have seen that with two angular momenta J 1 and J2 one can use either the Clebsch-Gordan coefficients or the 3-j symbols to relate the uncoupled basis IJi, Mi)IJ2, M2) to the coupled basis l(Ji, Ji), J, M) (here for clarity we label the state IJ, M) == l(Ji, J2), J, M) ). However, if we are interested in adding three angular momenta Ji, J2, and Ja to get the resultant J, the situation becomes somewhat more complicated. For instance, there is no unambiguous expansion of l~Ji, J2, Ja), J, M) in tenns of IJi, Mi)IJi. M2)1Ja. Ma): the expansion coeffi- cients depend on the order in which the angular momenta are added and on the value of the intennediate angular momenta resulting from the addition of the first two angular momenta (Judd 1998). However, if we specify the intermediate resul- tant vector Ja from adding, for example, Ji + Ji = J0 , then we are in fact able to unambiguously express the state l(Ji, J2), Ja, Ja, J, M) as a linear combination of the states !Ji, Mi)IJ2, M2)IJa, Ma). But we could just as easily add J2 + Ja == Jb to fonn an intennediate vector J6 and obtain the states l(J2, Ja), Jb, Ji, J, M).

Thus an important issue becomes how to transform between the basis l(Ji,J2),Ja, Ja, J, M) and the basis l(J2, Ja), J6, Ji, J, M). A very useful tool for this task is the Wigner 6-j symbol (or, simply, the 6-j symbol).

The transfonnation between the two bases can be described in terms of the coefficients (J 0 , Ja, J, MjJ 6, Ji, J, M), IJb, Ji, J, M) = "'f)Ja, Ja, J, MIJ 6, Ji, J, M)IJa, Ja, J, M) .

(1.19)

Immediately we can note that the coefficients are independent of M by applying, for example, the raising operator J+ to both sides of Eq. (1.19): J+IJb, Ji, J, M) = l)Ja, Ja, J, MIJb, Ji, J, M)J+IJa, Ja, J, M) , (1.20)

Jo or explicitly, J J(J + 1) - M(M + l)IJb, Ji, J, M + 1)

= L(Ja,Ja, J,MIJb, Ji, J,M)JJ(J + 1)- M(M + l)IJa, Ja, J,M + 1), (1.21)

so that, If we begin with M = -J, this shows by iteration that the coefficients are all equal, so they can be denoted simply as (Ja, J3, JIJb, Ji, J).

6-J SYMBOLS The 6-j symbols, which are written as 2 x 3 matrices in curly brackets, are directly related to these coefficients: (1.23)

Similar to 3-j symbols, 6-j symbols are real numbers, and they have sev- eral important symmetry properties. The 6-j symbols are zero unless they satisfy triangular conditions for the entries denoted by ◊'s: { ◊.

. } ◊ ◊ .

The triangular conditions for these entries are expressions of the triangular condi- tions for the addition of individual angular momenta (J 1 + J2 = Ja, for example).

The 6-j symbols are invariant under any permutation of the columns, for example { J1 J2 Ja} _ { J2 J1 Ja} (1.24)

L 1 L2 La - L2 L 1 La ' and are also invariant under an interchange of the upper and lower arguments in each of any two columns, (1.25)

An important context in atomic physics where the 6-j symbols appear and can be quite useful is when there is a need to relate the reduced matrix elements for some tensor operator TK, found in an uncoupled angular momentum basis, for example IJ, MJ) II, M 1 ), where J represents the total electronic angular momen- tum and I represents the nuclear spin, with the reduced matrix element in a coupled basis, for example IF, MF), where Fis the total angular momentum. If TK com- mutes with I, then the formula relating the reduced matrix elements [ derived, for example, in the books by Sobelman (1992) and Judd (1998)] is found to be ( J'' I' F' 11 TK 11 J, I' F)

= (-l)J'+l+F+ttJ(2F + 1)(2F' + 1) { ~ ~ ~ } (J'IITKIIJ) · (1.26)

Again we remind the reader that symbolic and numerical values for 6-j symbols can be easily evaluated using programs such as Mathematica®.

Bibliography Ageron, P., Mampe, W., Golub, R., and Pendelbury, J.M. (1978). Measure- ment of the ultra cold neutron production rate in an external liquid helium source. Physics Letters A, 66 (6), 469- 71.

Aleksandrov, E. B., Vedenin, V. D., and Kulyasov, V. N. ( 1984). Broadening and shift of thulium resonance lines by helium. Optika i Spektroskopiya, 56 ( 4 ), 596-600.

Alexandrov, E. B., Balabas, M. V., Pasgalev, A. S., Vershovskii, A. K., and Yakobson, N. N., ( 1996). Double-resonance atomic magnetometers: from gas discharge to laser pumping. Laser Physics, 6 (2), 244-51.

Alexandrov, E. B., Chaika, M. P., and Khvostenko, G. I. ( 1993). Interference of atomic states. Springer, New York.

Alexandrov, E. B., Balabas, M. V., Budker, D., English, D. S., Kimball, D.

F., Li, C.-H., and Yashchuk, V. V. (2002). Light-induced desorption of alkali atoms from paraffin coating. Physical Review A 66 (4), 042903.

Allcock, P., Andrews, D. L., Meech, S. R., and Wigman, A. J. ( 1996). Doubly forbidden second-harmonic generation from isotropic suspensions: Studies on the purple membrane of Halobacterium halobium. Physical Review A, 53 (4), 2788-91.

Allen, L. and Eberly, J. H. (1987). Optical resonance and two-level atoms.

Dover, New York.

Amoretti, M., et al. [ATHENA Collaboration], (2002). Production and detection of cold antihydrogen atoms. Nature, 419, 456-9.

Anderson, D. Z., Frisch, J. C., and Masser, C. S. ( 1984 ). Mirror reflectometer based on optical cavity decay time. Applied Optics, 23, (8), 1238-45.

Anderson, L. W., Pipkin, F. M., and Baird, J. C. ( 1960). Hyperfine structure of hydrogen, deuterium, and tritium. Physical Review, 120 ( 4 ), 1279-89.

Anderson, M. H., Ensher, J. R., Matthews, M. R., Wieman, C. E., and Cornell E. A. ( 1995). Observation of Bose-Einstein condensation in a dilute atomic vapor. Science, 269 (5221 ), 198-201.

Andreev, A. V., llinski, Yu. A., and Emelyanov, V. I. ( 1993). Cooperative effects in optics: superradiance and phase transitions. Institute of Physics Publishing, Bristol, Philadelphia.

Andrews, D. L. and Blake, N. (1988). Forbidden nature of multipolar contri- butions to second-hannonic generation in isotropic fluids. Physical Review A, 38 (6), 3113-15.

Arfken, G. B. ( 1985). Mathematical methods for physicists. Academic Press, Orlando.

Arimondo, E. ( 1996). Coherent population trapping in laser spectroscopy. In: Progess in Optics, ed. by E. Wolf, Elsevier Science B.V., New York, XXXV, 259-354.

Aspect, A., Arimondo, E., Kaiser, R., Vansteenkiste, N., and Cohen- Tannoudji, C. ( 1988) Laser cooling below the one-photon recoil energy by velocity-selective coherent population trapping. Physical Review Letters, 61 (7), 826-9.

Audoin, C. and Guinot, B. (2001). The measurement of time: time,frequency, and the atomic clock. Cambridge University Press, Cambridge.

Auzinsh, M., Budker, D., and Rochester, S. M. (2007). Optically polarized atoms, manuscript in preparation.

Auzinsh, M. and Ferber, R. ( 1995). Optical polarization of molecules.

Cambridge University Press, Cambridge.

Baierlein, R. ( 1999). Thermal physics. Cambridge University Press, Cam- bridge.

Barenco, A., Deutsch, D., Ekert, A., and Jozsa, R. ( 1995). Conditional quantum dynamics and logic gates. Physical Review Letters, 74 (20), 40836.

Barkov, L. M. and Zolotorev, M. ( 1978). Observation of parity nonconserva- tion in atomic transitions. Pis'ma v Zhumal Eksperimentalnoi i Teoreticheskoi Fiz.iki, 27, 379-83.

Barkov, L. M., Zolotorev M. S., and Melik-Pashaev, D. A. ( 1989). Study of monoatomic-samarium 4/6 8 2 7 F ~ 4/ 6682 5 D forbidden transitions. Optika i Spektroskopiya, 66 (3), 495-500.

Batygin, V. V., ter Haar, D., and Toptygin, I. N. ( 1978). Problems in electrodynamics. Academic Press, London.

Baur, G., Boero, G., Brauksiepe, S., Buzzo, A., Eyrich, W., Geyer, R., Grzonka, D., Hauffe, J., Kilian, K., LoVetere, M., Macri, M., Moosburger, M., Nellen, R., Oelert, W., Passaggio, S., Pozzo, A., Rohrich, K., Sachs,

## BIBLIOGRAPHY

K., Schepers, G., Sefzick, T., Simon, R. S., Stratmann, R., Stinzing, F., and Wolke, M. (1996). Production of antihydrogen. Physics Letters B, 368 (3), 251-8.

Bazalgette, G., Bachner, M., Champenois, C., Trenec, G., and Vigue, J.

( 1999). Saturation spectroscopy of the A-X transition of the ICI molecule.

European Physical Journal D, 6, 193-200.

Bennett, S. C. and Wieman, C. E. ( 1999). Measurement of the 6S to 7S tran- sition polarizability in atomic cesium and an improved test of the standard model. Physical Review Letters, 82 (12), 2484-2487.

Bergmann, K., Theuer, H., and Shore, B. W. ( 1998). Coherent population transfer among quantum states of atoms and molecules. Rev. Mod. Phys., 70 (3), I 003-1025.

Berry, M. V. ( 1984 ). Quanta) phase factors accompanying adiabatic changes.

Proceedings of the Royal Society of London, Series A, 392, (1802), 45-57.

Bethe, H. A. and Salpeter, E. E. ( 1977). Quantum mechanics of one- and two-electron atoms. Plenum, New York.

Beverini, N., Lagomarsino, V., Manuzio, G., Scuri, F., Testera, G., and Torelli, G. ( 1988). Stochastic cooling in Penning traps. Physical Review A, 38 (I), 107-14.

Birich, G. N., Bogdanov, Yu. V., Kanorskii, S. I., Sobelman, I. I., Sorokin, V.

N., Struk, I. I., and Yukov, E. A. ( 1994). Precision laser spectropolarimetry.

Journal of Russian Laser Research, 15 (6), 455- 76.

Birkett, B. B., Briand, J. P., Charles, P., Dietrich, D. D., Finlayson, K., Indelicato, P., Liesen, D., Marrus, R., and Simionovici, A. ( 1993). Hyper- fine quenching and measurement of the 2 3 Po - 3 P1 fine-structure splitting in helium-like silver. Physical Review A, 47 (4), R2454-8.

Blanford, G., Christian, D. C., Gollwitzer, K., Mandelkem, M., Munger, C.

T., Schultz, J., and Zioulas, G. (1998). Observation of atomic antihydrogen.

Physical Review Letters, 80 ( 14 ), 3037-40.

Blum, K. ( 1996). Density matrix theory and applications. Plenum Press, New York.

Blundell, S. (2003) Magnetism in condensed matter. Oxford University Press, Oxford.

Born, M. and Wolf, E. (1980). Principles of optics. Pergamon Press, New York.

Bouchiat, C. ( 1989). Berry phases for quadratic spin Hamiltonians taken from atomic and solid state physics: examples of Abelian gauge fields not connected to physical particles. Journal de Physique /, SO (9), I 041-5.

Bouchiat, M. A. ( 1963). Relaxation magnetique d' atomes de rubidium sur des parois paraffinees. Journal de Physique, 24, 379-90.

Bouchiat, M. A. and Bouchiat, C. (1974). Weak neutral currents in atomic physics. Physics Letters, 488 (2), 111-14.

Bouchiat, M. A. and Bouchiat, C. ( 1975). Parity violation induced by weak neutral currents in atomic physics II. Journal de Physique, 36 (6), 493.

Bouchiat, M. A. and Bouchiat, C. ( 1997). Parity violation in atoms. Repons on Progress in Physics, 60 ( 11 ), 1351-96.

Bouchiat, M. A., Guena, J ., Hunter, L., and Pottier, L. ( 1982). Observation of a parity violation in cesium. Physics Letters B, 1178 (5), 358-64.

Bowers, C. J., Budker, D., Freedman, S. J., Gwinner, G., Stalnaker, J. E., and DeMille, D. ( 1999). Experimental investigation of the 6s 2 1 So -+ 5d6s 3 D1,2 forbidden transitions in atomic ytterbium. Physical Review A, 59 (5), 3513- 3526.

Boyd, R. W. (2003). Nonlinear Optics. Academic Press, San Diego.

Bradley, C. C., Sackett, C. A., Tollett, J. J ., and Hulet, R. G. ( 1995). Evidence of Bose-Einstein condensation in an atomic gas with attractive interactions.

Physical Review Letters, 75 (9), 1687-90.

Brand, H., Nottbeck, B., Schulz, H. H., and Steudel, A. ( 1978). Laser-atomic- beam spectroscopy in the samarium I spectrum. Journal of Physics B, 11 (4), L99-Ll03.

Bransden, B. H. and Joachain, C. J. (1989). Introduction to quantum mechanics. Longman, Essex.

Bransden, B. H. and Joachain, C. J. (2003). Physics of atoms and molecules.

Pearson Education Ltd., Essex.

Bredov, M. M., Rumyantzev, V. V., and Toptygin, I. N. ( 1985). Klassicheskaya elektrodinamika (in Russian). Nauka, Moscow.

Brown, L. S. and Gabrielse, G. (1986). Geonium theory: physics of a single electron or ion in a Penning trap. Reviews of Modem Physics, 58 (I), 233-313.

Bruun, G. M. and Burnett, K. ( 1998). Interacting Fermi gas in a harmonic trap. Physical Review A, 58 (3), 2427-34.

## BIBLIOGRAPHY

Budker, D. ( 1998a). Electrons in a shell. American Journal of Physics, 66 (7), 572-3.

Budker, D. ( 1998b ). Parity nonconservation in atoms. In Physics Beyond the Standard Model (eds. P. Herczeg, C. M. Hoffman, and H. V. Klapdor- Kleingrothaus), pp. 418-41. World Scientific, Singapore.

Budker, D., DeMille, D., Commins, E. D., and Zolotorev, M. S. ( 1994). Exper- imental investigation of excited states in atomic dysprosium. Physical Review A, SO (I), 132-43.

Budker, D., Gawlik, W., Kimball, D. F., Rochester, S. M., Yashchuk, V. V., and Weis, A. (2002). Resonant nonlinear magneto-optical effects in atoms.

Reviews of Modern Physics, 74 ( 4 ), 1153-120 I.

Budker, D., Hollberg, L., Kimball, D. F., Kitching, J., Pustelny, S., and Yashchuk, V. V. (2003). Investigation of microwave transitions and nonlin- ear magneto-optical rotation in anti-relaxation-coated cells. Physical Review A, 71, 012903.

Budker, D., Kimball, D. F., Rochester, S. M., and Urban, J. T. (2003).

Alignment-to-orientation conversion and nuclear quadrupole resonance.

Chemical Physics Letters, 378 (3-4), 440-8.

Budker, D., Lamoreaux, S. K., Sushkov, A. 0., and Sushkov, 0. P. (2006).

Sensitivity of condensed-matter P- and T-violation experiments. Physical Review A, 73 (2), 022107.

Cates, G. D., Schaefer, S. R., and Happer, W. ( 1988). Relaxation of spins due to field inhomogeneities in gaseous samples at low magnetic fields and low pressures. Physical Review A, 37 (8), 2877.

Caves, C. M. ( 1980) Quantum-mechanical radiation-pressure fluctuations in an interferometer. Physical Review Letters, 45 (2), 75-9.

Caves, C. M. ( 1981 ). Quantum-mechanical noise in an interferometer. Physi- cal Review D, 23 (8), 1693-708.

Chan, H. W., Black, A. T., and Vuletic, V. (2003). Observation of collective- emission-induced cooling of atoms in an optical cavity.

Physical Review Letters , 90 (6), 063003.

Chu, S. ( 1998). Nobel lecture: The manipulation of neutral particles. Reviews of Modem Physics, 70 (3), 685706.

Cohen-Tannoudji, C. ( 1998). Nobel lecture: Manipulating atoms with pho- tons. Reviews of Modern Physics, 70 (3), 70719.

Coh~n-Tannoudji, C. N. and Phillips, w. D. ( 1990). New mechanisms for laser coolmg. Physics Today, 43 ( I 0), 33-40.

Cohen-Tannoudji, C., Dupont-Roe, J., and Grynberg, G. (1992). Atom-photon interactions: basic processes and applications. Wiley, New York.

Commins, E. D. ( 199 I). Berry's geometric phase and motional fields.

American Journal of Physics, 59 ( I 2), I 077-80.

Commins, E. D., Jackson, J. D., and DeMille, D. P. (2007). The electric dipole moment of the electron: An intuitive explanation for the evasion of Schifrs theorem. American Journal of Physics, 75 (6), 532-6.

Condon, E. U. and Shortley, G. H. ( I 970). The theory of atomic spectra.

Cambridge University Press, London.

Conti, R., Bucksbaum, P., Chu, s., Commins, E., and Hunter, L. ( 1979). Pre- liminary observation of parity nonconservation in atomic thallium. Physical Review Letters, 42 (6), 343-6.

Cornell, E. A. and Wieman, C. E. (2002). Nobel lecture: Bose-Einstein con- densation in a dilute gas, the first 70 years and some recent experiments.

Reviews of Modem Physics, 74 (3), 875-93.

Corney, A. ( 1988). Atomic and laser spectroscopy. Clarendon Press, Oxford.

Cundiff, S. T., Ye, J., and Hall, J. L. (2001). Optical frequency synthesis based on mode-locked lasers. Review of Scientific Instruments, 72 ( I 0), 3749- 71.

Davis, K. B., Mewes, M.-O., Andrews, M. R., van Druten, N. J., Durfee, D.

S., Kum, D. M., and Ketterle, W.( 1995). Bose-Einstein Condensation in a gas of sodium atoms. Physical Review Letters, 15 (22), 396973.

Dehmelt, H. ( 1989). Less is more: experiments with an individual atomic particle at rest in free space. American Journal of Physics, 58 (I), I 7-27.

Delone, N. B. and Krainov, V. P. ( 1985). Atoms in strong light.fields. Springer- Verlag, Berlin.

Delone, N. B. and Krainov, V. P. ( 1988). Fundamentals of nonlinear optics of atomic gases. Wiley, New York.

DeMarco, B. and Jin, D. S. ( 1999). Onset of Fermi degeneracy in a trapped atomic gas. Science, 285 (5434), 1703-6.

DeMarco, B., Papp, S. B., and Jin, D. S. (200 I). Pauli blocking of collisions in a quantum degenerate atomic fermi gas. Physical Review Letters, 86 (24), 5409-12.

## BIBLIOGRAPHY

DeMille, D. ( 1995). Parity nonconservation in the 6s2 1 S0 ___. 6s5d 3 D 1 transition in atomic ytterbium. Physical Review Letters, 74 (21 ), 4165-8.

DeMille, D. (2002). Quantum computation with trapped polar molecules.

Physical Review Letters, 88 (6), 067901.

Demtroder, W. ( 1996). Laser spectroscopy: basic concepts and instrumenta- tion. Springer, Berlin.

DePue, M. T., McCormick, C., Winoto, S. L., Oliver, S., and Weiss, D. S.

( 1999). Unity occupation of sites in a 3D optical lattice. Physical Review Letters, 82 (11 ), 2262-5.

Dicke, R. H. ( 1953 ). The effect of collisions upon the doppler width of spectral lines. Physical Review, 89 (2), 472-3.

Dicke, R. H. ( 1954 ). Coherence in spontaneous radiation process. Physical Review, 93 (I), 99-110.

Donati, S. (2000). Photodetectors. Prentiss Hall, Upper Saddle River, New Jersey.

Dos Santos, F. P., Leonard, J., Wang, J. M., Barrelet, C. J., Perales, F., Rasel, E., Unnikrishnan, C. S., Leduc, M., and Cohen-Tannoudji, C. (2001). Bose- Einstein condensation of metastable helium. Physical Review Letters, 86 ( 16), 3459-62.

Drell, P. S. and Commins, E. D. ( 1985). Parity nonconservation in atomic thallium. Physical Review A, 32 (4), 2196-2210.

Duarte, F. J. and Hillman, L. W. ( 1990). Dye laser principles. Academic Press, Boston.

Dzuba. V. A., Flambaum, V. V., and Khriplovich, I. B. (1986). Enhance- ment of P-nonconserving and T-nonconserving effects in rare-earth atoms.

Zeitschrift Fur Physik D, 1 (3), 243-5.

Edmonds, A. R. ( 1996). Angular momentum in quantum mechanics. Princeton University Press, Princeton.

Fano, U. and Racah, G. (1959). Irreducible tensorial sets. Academic Press, New York.

Faraday, M. ( 1855). Experimental research (London), III, 2164.

Fedichev, P. 0., Reynolds, M. W., Rahmanov, U. M., and Shlyapnikov, G.

V. ( 1996). Inelastic decay processes in a gas of spin-polarized triplet helium.

Physical Review A, 53 (3), 1447-53.

Fermi. E. and Segre, E. (1933). Zeitschriftfur Physik, 82, 729.

Fischer, C. H., Brage, T., and Jonsson, P. ( 1997). Computational atomic structure: an MCHF approach. Institute of Physics, Bristol.

Flambaum, V. V. and Hanhart, C. (1993). Magnetic interaction between rela- tivistic atomic electrons and parity nonconserving nuclear moments. Physical Review C, 48 (3), 1329-34.

Flambaum, V. V. and Khriplovich, I. B. ( 1980). P-odd nuclear-forces - a source of parity violation in atoms. Zhumal Eksperimentalnoi i Teoreticheskoi Fiziki, 79 (5), 1656-63; English translation: Soviet Physics, Journal of Experimental and Theoretical Physics (JEI'P), 52, 835-42.

Flambaum, V. V. and Murray, D. W. ( 1997). Anapole moment and nucleon weak interactions. Physical Review C, 56 (3), 1641.

Fowles, G. R. (1915). Introduction to modem optics. Dover, New York.

Gabrielse, G. (2001). Comparing the antiproton and proton, and opening the way to cold antihydrogen. Advances in Atomic, Molecular, and Optical Physics, 45, 1-39.

Gabrielse, G., Hall, D. S., Roach, T., Yesley, P., Khabbaz, A., Estrada, J., Heimann, C., and Kalinowsky, H. ( 1999). The ingredients of cold antihydro- gen: simultaneous confinement of antiprotons and positrons at 4 K. Physics Letters B, 455 ( 1-4), 311-15.

Gabrielse, G., Hanneke, D., Kinoshita, T., Nio, M., and Odom, B. (2006).

New determination of the fine structure constant from the electron g value and QED. Physical Review Letters, 97 (3), 030802.

Gabrielse, G., et al. [ATRAP Collaboration] (2002). Background-free obser- vation of cold antihydrogen with field-ionization analysis of its states.

Physical Review Leners, 89 (21 ), 213401.

Gamblin, R. L. and Carver, T. R. ( 1965). Polarization and relaxation processes in 3He gas. Physical Review, 138 (4A), 946.

Gangl, M. and Ritsch, H. (2000). Collective dynamical cooling of neutral particles in a high-Q optical cavity. Physical Review A, 61, ( 1 ), 011402/1-4.

Gerry, C. C. and Knight, P. L. (2005). Introductory Quantum Optics.

Cambridge University Press, Cambridge.

Ghosh, P. K. ( 1995). Ion traps. Oxford University Press, Oxford.

Glashow, S. L. (1961). Partial symmetries of weak interactions. Nuclear Physics, 22 (4), 579.

## BIBLIOGRAPHY

Goldenberg, H. M., Kleppner, D., and Ramsey, N. F. (1961). Atomic beam resonance experiments with stored beams. Physical Review, 123 (2), 530-7.

Golub, R., Jewell, C., Ageron, P., Mampe, W., Heckel, B., and Kilvington, I.

( 1983 ). Operation of a superthermal ultracold neutron source and the storage of ultracold neutrons in superfluid 4He. 'Zeitschrift fur Physik B, SI (3), 187- 93.

Golub, R., Richardson, D., and Lamoreaux, S. K. ( 1991 ). Ultra-cold neutrons.

Adam Hilger, Bristol.

Graeme, J. ( 1996). Photodiode amplifiers. McGraw-Hill, New York.

Griffiths, D. ( 1987). Introduction to elementary particles. Wiley, New York.

Griffiths, D. ( 1995). Introduction to quantum mechanics. Prentice-Hall, Upper Saddle River.

Griffiths, D. ( 1999). Introduction to electrodynamics. Prentice-Hall, Upper Saddle River.

Guena, J., Chauvat, D., Jacquier, Ph., Jahier, E., Lintz, M., Papoyan, A.

V., Sanguinetti, S., Sarkisyan, D., Wasan, A., and Bouchiat, M. A. (2003).

New manifestation of atomic parity violation in cesium: a chiral optical gain induced by linearly polarized 6S --+ 7S excitation. Physical Review Letters, 90 (14), 143001.

Guidoni, L. and Verkerk, P. ( 1999). Optical lattices: cold atoms ordered by light. Journal of Optics B, 1 (5), R23-R45.

Gustavson, T. L., Bouyer, P., and Kasevich, M. A. ( 1997). Precision rota- tion measurements with an atom interferometer gyroscope. Physical Review Letters, 78 ( 11 ), 2046-9.

Gustavson, T. L., Landragin, A., and Kasevich, M. A. (2000). Rotation sensing with a dual atom-interferometer Sagnac gyroscope. Classical and Quantum Gravity, 17 (12), 2385-98.

Hahn, E. L. and Maxwell, D. E. ( 1952). Spin echo measurements of nuclear spin coupling in molecules. Physical Review, 88 (5), 1070-84.

Hall, J. L., Ye, J., Diddams, S. A., Long-Sheng, M., Cundiff S. T., and Jones, D. J. (2001 ). Ultrasensitive spectroscopy, the ultrastable lasers, the ultrafast lasers, and the seriously nonlinear fiber: a new alliance for physics and metrology. /EEE Journal of Quantum Electronics, 37 (12), 1482-92.

Hannay, J. H. ( 1985). Angle variable holonomy in adiabatic excursion of an integrable Hamiltonian. Journal of Physics A - Mathematical and General, 18 (2), 221-30.

Hansch, T. W. ( 1972). Repetitively pulsed tunable dye laser for high- resolution spectroscopy. Applied Optics, 11 (4), 895.

Happer, W. ( 1971 ). Light propagation and light shifts in optical pumping experiments. Progress in Quantum Electronics, 1 (2), 51.

Happer, W. ( 1972). Optical pumping. Reviews of Modem Physics, 44 (2), 169-249.

Happer, W. and Tam, A. C. ( 1977). Effect of rapid spin exchange on the magnetic-resonance spectrum of alkali vapours. Physical Review A, 16, (5), 1877-91.

Happer, W. and Tang, H. (1973). Spin-exchange shift and narrowing of mag- netic resonance lines in optically pumped alkali vapours. Physical Review Letters, 31 (5), 273-6.

Happer, W. and van Wijngaarden, W. A. ( 1987). An optical-pumping primer.

Hyperfine Interactions, 38 ( 1-4), 435-70.

Happer, W., Walker, T., and Bonin, K. (2003). Optical pumping: principles and applications. (To be published).

Haroche, S. ( 1976). Quantum beats and time-resolved fluorescence spec- troscopy, in High-resolution laser spectroscopy, K. Shimoda, Ed. Springer- Verlag, Berlin.

Harris, S. E. ( 1997). Electromagnetically induced transparency. Physics Today, SO (7), 36-42.

Hartemann, F. V. (2002). High-field electrodynamics. CRC Press, Boca Raton, Florida.

Heitler, W. (1954). The quantum theory of radiation. Oxford University Press, London.

Henkel, C., Kruger, P., Folman, R., and Schmiedmayer, J. (2003). Fundamen- tal limits for coherent manipulation on atom chips. Applied Physics B, 76 (2), 173-82.

Herzberg, G. (1944). Atomic spectra and atomic structure. Dover, New York.

Herzberg, G. (1971). The spectra and structures of simple free radicals,· an introduction to molecular spectroscopy. Cornell University Press, Ithaca.

Herzberg, G. ( 1989). Molecular spectra and molecular structure, Volume I: Spectra of diatomic molecules. R. E. Krieger, Malabar, FL.

## BIBLIOGRAPHY

Hinds, E. A. ( 1988). Radiofrequency s~ctroscopy.

In The Spectrum of Atomic Hydrogen: Advances (ed. G. W. Senes), pp. 245-92. World Scientific, Singapore.

Hoffnagle, J. A. (1982). "Measurement of the forbidden 6s112 --+ 7 8112 tran- sition in atomic cesium." Dissertation for the degree of Doctor of Natural Sciences, Swiss Federal Institute of Technology.

Holzscheiter, M. H. and Charlton, M. ( 1999). Ultra-low energy antihydrogen.

Reports on Progress in Physics, 62 (I), 1-60.

Honig, R. E. and Kramer, D. A. ( 1969). Vapor pressure data for the solid and liquid elements. RCA Review, 30, 285-305.

Horowitz, P. and Hill, W. ( 1989). The art of electronics. Cambridge University Press, Cambridge, UK.

Huard, S. ( 1997). Polarization of light. Wiley, New York.

Huffman, P. R., Brome, C. R., Butterworth, J. S., Coakley, K. J., Dewey, M.

S., Dzhosyuk, S. N., Golub, R., Greene, G. L., Habicht, K., Lamoreaux, S. K., Mattoni, C. E. H., McKinsey, D. N., Wietfeldt, F. E., and Doyle, J. M. (2000).

Magnetic trapping of neutrons. Nature, 403 (6765), 62-4.

Humphries, S. ( 1986). Principles of charged particle acceleration. Wiley, New York.

Jackson, J. D. (1975). Classical electrodynamics. Wiley, New York.

Jones, D. J., Diddams, S. A., Ranka, J. K., Stentz, A., Windeler, R. S., Hall, J.

L., and Cundiff, S. T. (2000). Carrier-envelope phase control of femtosecond mode-locked laser and direct optical frequency synthesis. Science, 288 (5466), 635-9.

Jones, R. C. ( 1941 ). A new calculus for the treatment of optical systems.

Journal of the Optical Society of America, 31, 488-93.

Judd, B. R. ( 1998). Operator Techniques in Atomic Spectroscopy. Princeton University Press, Princeton, New Jersey.

Kasapi, A. ( 1996). Three-dimensional vector model for a three-state system.

J. Opt. Soc. Am. B, 13 (7), 1347-1351.

Kasevich, M. and Chu, S. ( 1992). Laser cooling below a photon recoil with three-level atoms. Physical Review Letters, 69 ( 12), 1741-4.

Kastel, J., Fleischhauer, M., Yelin, S. F., and Walsworth, R. L. (2007). Tun- able negative refraction without absorption via electromagnetically induced chirality. Physical Review Letters 99, 073602 (2007)

Kaye, G. W. C. and Laby, T. H. ( 1995). Tables of physical and chemical constants. Longman, Essex.

Kazantsev A. P., Smimov, V. S., Tumaikin, A. M., and Yagofarov, A. ( 1985).

Effect of spontaneous-photon recoil on mixing of atomic multipole moments in a polarized external field. Optika i Spektroskopiya, 58 (3), 500-6.

Ketterle, W. (2002). Nobel lecture: When atoms behave as waves: Bose- Einstein condensation and the atom laser. Reviews of Modem Physics, 74 (4), 1131-51.

Ketterle, W. and Inouye, S. (2001). Collective enhancement and suppression in Bose-Einstein condensates. Comptes Rendus de l'Academie des Sciences, Serie W (Physique, Astrophysique), 2 (3), 339-80.

Khriplovich, I. B. ( 1991 ). Parity nonconservation in atomic phenomena.

Gordon and Breach, Philadelphia.

Khriplovich, I. 8. and Lamoreaux, S. K. ( 1997). CP violation without strangeness: electric dipole moments of particles, atoms, and molecules.

Springer, Berlin.

King, W. H. ( 1963 ). Comments on article peculiarities of isotope shift in samarium spectrum. Journal of the Optical Society of America, 53, (5), 638.

King, W. H. ( 1984). Isotope shifts in atomic spectra. Plenum Press, New York.

Kinoshita, T. ( 1996). The fine structure constant. Reports on Progress in Physics, 59, 1459-92.

Kittel, C. (2005). Introduction to solid state physics. Wiley, New York.

Kittel, C. and Kroemer, H. ( 1980). Thermal physics. W. H. Freeman, San Francisco.

Knize, R. J ., Wu, Z., and Happer, W. ( 1988). Optical pumping and spin exchange in gas cells. Advances in Atomic and Molecular Physics, 24, 223-67.

Kocharovskaya, 0. ( 1992). Amplification and lasing without inversion.

Physics Reports, 219 (3-6), 175-90.

Kominis, I. K., Komack, T. W., Allred, J. C., and Romalis, M. V. (2003).

A sub-femtotesla multi-channel atomic magnetometer. Nature, 422, (6932), 59699.

Krainov, V. P., Reiss, H., and Smimov, B. M. ( 1997). Radiative processes in atomic physics. Wiley, New York.

Lamoreaux, S. K. ( 1997). Demonstration of the Casimir force in the 0.6 to 6 µm range. Physical Review Letters, 78 (I), 5-8.

## BIBLIOGRAPHY

Lamoreaux, S. K. ( 1999). Feeble magnetic fields generated by thermal fluctua- tions in extended metallic conductors: implications for electric-dipole moment experiments. Physical Review A, 60 (2), 1717.

Lamoreaux, S. K. (2002). Solid-state systems for the electron electric dipole moment and other fundamental measurements. Physical Review A 66, 022109.

Lamoreaux, S. K. (2007). Casimir forces: still surprising after 60 years.

Physics Today, 60, 40-45.

Landau, L. D. and Lifshitz, E. M. ( 1977). Quantum mechanics. Butterworth- Heinemann, Oxford.

Landau, L. D. and Lifshitz, E. M. ( 1987). The classical theory of fields.

Pergamon Press, Oxford.

Landau, L. D. and Lifshitz, E. M. (1999). Theory of elasticity. Pergamon Press, Oxford.

Landau, L. D., Lifshitz, E. M., and Pitaevskii, L. P. ( 1995). Electrodynamics of continuous media. Butterworth-Heinemann, Oxford.

Lefebvre-Brion, H. and Field, R. W. (2004). The Spectra and Dynamics of Diatomic Molecules. Elsevier, Academic Press, Amsterdam - Boston.

Letokhov, V. S. ( 1987). Laser photoionization spectroscopy. Academic Press, Orlando.

Loudon, R. (2000). The quantum theory of light. Oxford University Press, Oxford.

Loudon, R. and Knight, P. L. ( 1987). Squeezed light. Journal of Modem Optics, 34 (6-7), 709-59.

Lounis, B. and Cohen-Tannoudji, C. (1992). Coherent population trapping and Fano profiles. Journal of Physics II, 2, 579-92.

Lu, Z.-T., Bowers, C. J., Freedman, S. J., Fujikawa, B. K., Mortara, J. L., Shang, S.-Q., Coulter, K. P., and Young, L. (1994). Laser trapping of short- lived radioactive isotopes. Physical Review Letters, 72 (24), 3791-4.

Macaluso, D. and Corbino, 0. M. (1898). Nuovo Cimento, 8,257.

Major, F. G. ( 1998). The quantum beat: the physical principles of atomic clocks. Springer, New York.

Makarov, A. A. ( 1983). Excitation of atoms by off-resonance light pulses.

Zhurnal Eksperimental 'noi i Teoreticheskoi Fiziki, 85, 1192-1202.

M · J B · 0,fparticles and anon, · • and Thornton, S. T. ( 1995). Classical dynamics systems. Saunders College Pub., Fort Worth.

Massey. H. S. W. ( 1976). Negative ions. Cambridge University Press.

Cambridge.

Masuhara. N.. Doyle. J. M., Sandberg, J. C.. Kleppner, D.. Gr:eytak.

T .. 1 ·• H~s. H. F.,. and Kochanski. G. P. ( I 988). Evaporative c~!mg of spm-polanzed atomic hydrogen. Physical Review Letters. 61 (S). 935 · Messiah, A. ( 1966). Quantum mechanics. Wiley, New York.

Me~alf. H. J. and Van der Straten. P. ( 1999). Laser cooling and trapping.

Spnnger- Verlag, Berlin.

Milner. V. and Prior. Y. ( 1999). Biaxial spatial orientation of atomic angular momentum. Physical Review A, 59 (3 ), R 1738-41.

Milonni. P. W. (2004). Fast light, Slow Light, and Left-handed Light. Taylor and Francis, New York.

Milton. K. A. (2001). The Casimir effect: physical manifestations of zero- point energy. World Scientific, New Jersey.

Montgomery, R. (1991). How much does the rigid body rotate? A Berry's phase from the 18th century. American Journal of Physics, S9 (5), 394-8· Nenonen, J., Montonen, J., and Katila, T. (1996). Thennal noise in biomag- netic measurements. Review of Scientific Instruments, 67 (6), 2397 · Nielsen, M. A. and Chuang, I. L. (2000). Quantum computation and quantum information. Cambridge University Press, Cambridge.

Nguyen, A. T., Budker, D .• DeMille. D. and Zolotorev, M. ( 1997). Search for parity nonconservation in atomic dysprosium. Physical Review A, S6 (5), 3453-63.

Odom, B., Hanneke, D., D'Urso, B., and Gabrielse, G. (2006). New mea- surement of the electron magnetic moment using a one-electron quantum cyclotron. Physical Review Letters, 97 (3), 030801.

O'Hara, K. M., Hemmer, S. L., Gehm, M. E., Granade, S. R., and Thomas, J.

E. (2002). Observation of a strongly interacting degenerate fermi gas of atoms.

Science, 298 ( 5601 ), 2179-82.

Oktel, M. 0. and Mustecaplioglu, 0. E. (2004). Electromagnetically induced left-handedness in a dense gas of three-level atoms. Physical Review A, 70 (5), 053806.

## BIBLIOGRAPHY

Olshanii, M. and Weiss, D. (2002). Producing Bose-Einstein condensates using optical lattices. Physical Review Letters, 89 (9), 090404.

Omont, A. ( 1977). Irreducible components of density matrix - application to optical-pumping. Progress in Quantum Electronics, 5, 69-138.

Panofsky, W. K. H. and Phillips, M. ( 1962). Classical electricity and magnetism. Addison-Wesley, Reading, Massachusetts.

Pathria, R. K. ( 1996). Statistical mechanics. Butterworth-Heinemann, Oxford.

Paul, W. ( 1990). Electromagnetic traps for charged and neutral particles.

Reviews of Modern Physics, 62 (3), 531-40.

Paul, W., Reinhard, H.P., and von Zahn, U. (1958). Das elektrishe massen- filter als massenspektrometer und isotopentrenner. Zeitschrift fur Physik, 152, 143-82.

Pendry, J. B. (2000). Negative Refraction Makes a Perfect Lens. Physical Review Letters, 85 (18), 3966-69.

Pendry, J. B. (2004a). Negative Refraction. Contemporary Physics, 45 (3), 191-202.

Pendry, J.B. (2004b). Science, 306, 1353.

Pendry, J. B., and Smith, D. R. (2004). Reversing Light With Negative Refraction. Physics Today, 57 (6), 37-43.

Pethick, C. J. and Smith, H. (2002). Bose-Einstein condensation in dilute gases. Cambridge University Press, Cambridge.

Phillips, W. D. ( 1998). Nobel lecture: Laser cooling and trapping of neutral atoms. Reviews of Modern Physics, 70 (3), 72141.

Pritchard, D. E., Raab, E. L., Bagnato, V., Wieman, C. E., and Watts, R. N.

( 1986). Light traps using spontaneous forces. Physical Review Letters, 57 (3), 310313.

Purcell, E. M. ( 1985). Electricity and Magnetism. McGraw-Hill, New York.

Purcell, E. M. and Ramsey, N. F. ( 1950). On the possibility of electric dipole moments for elementary particles and nuclei. Physical Review, 78, (6), 807.

Quint, W. (2001). The g-Factor of the bound electron in hydrogenic ions. In Atomic Physics 17 (ed. E. Arimondo, P. De Natale, and M. Inguscio), Amer- ican Institute of Physics Conference Proceedings, Vol. 551, pp. 282-9. AIP, Melville, NY.

Raab, E., Prentiss, M. Cable, A., Chu, S., and Pritchard, D. (1987). Trapping of neutral sodium atoms with radiation pressure. Physical Review Letters, 59 (23), 2631-4.

Radzig, A. A. and Smimov, B. M. ( 1985). Reference data on atoms, molecules, and ions. Springer-Verlag, Berlin.

Ramsey, N. ( 1985). Molecular beams. Clarendon Press, Oxford.

~egan, B. C., Commins, E. o., Schmidt, C. J., and DeMille, D. (2002). New hmit on the electron electric dipole moment. Physical Review Letters, 88 (7), 071805.

Reif, F. ( 1965). Fundamentals of statistical and thermal physics. McGraw- Hill, New York.

Riley, K. F., Hobson, M. P., and Bence, S. J. (2002). Mathematical methods for physics and engineering. Cambridge University Press, Cambridge.

Robert, A., Sirjean, o., Browaeys, A., Poupard, J., Nowak, S., Boiron, D., Westbrook, C. I., and Aspect, A. (2001). A Bose-Einstein condensate of metastable atoms. Science, 292 (5516), 461-64.

Rochester, S. and Budker, D. (2001). Atomic polarization visualized. Ameri- can Journal of Physics, 69 (4), 450-4.

Rolston, S. ( 1998). Optical lattices. Physics World, 11 ( I 0), 27-32.

Sachs, R. G. ( 1987). The physics of time reversal. University of Chicago Pre~, Chicago.

Sakurai, J. J. (1967). Advanced quantum mechanics. Addison-Wesley, New York.

Sakurai, J. J. (1994). Modem quantum mechanics. Addison-Wesley, New York.

Salam, A. ( 1968). In Elementary particle theory, relativistic groups and ana- lyticity, Nobel Symposium, No. 8 (ed. N. Svartholm), 367. Wiley, New York.

Sandars, P. G. H. ( 1965). Electric dipole moment of an atom. Physics Leners, 14 (3), 194.

Santarelli, G., Laurent, Ph., Lemonde, P., Clairon, A. Mann, A. G., Chang, S., Luiten A. N., and Salomon, C. (1999). Quantum projection noise in an atomic fountain: a high stability cesium frequency standard. Physical Review Letters, 82 (23), 461922.

## BIBLIOGRAPHY

Sargent, M., Scully, M. 0., and Lamb, W. E. ( 1977). Laser physics. Addison- Wesley, Reading, MA.

Schafer, F. P., Schmidt, W., and Volze, J. ( 1966). Organic dye solution laser.

Applied Physics Letters, 9 (8), 306.

Schearer, L. D. and Walters, G. K. ( 1965). Nuclear spin-lattice relaxation in the presence of magnetic-field gradients. Physical Review, 139 (5A), 1398.

Schiff, L. I. ( 1963). Measurability of nuclear electric dipole moments.

Physical Review, 132 (5), 21942200.

Schlesser, R. and Weis, A. ( 1992). Light-beam deflection by cesium vapor in a transverse magnetic field. Optics Letters, 17 (14), 1015-17.

Schneider, J. and Wallis, H. ( 1998). Mesoscopic Fermi gas in a harmonic trap.

Physical Review A, 57 (2), 1253-9.

Scully, M. 0. and Zubairy, M. S. ( 1997). Quantum optics. Cambridge University Press, Cambridge.

Semertzidis, Y. K. et al. [Muon EDM Collaboration] (2001). A sensitive search for a muon electric dipole moment. In Quantum Electrodynamics and Physics of the Vacuum: QED 2000 (ed. G. Cantatore). American Institute of Physics Conference Proceedings, Vol. 564, pp. 263-8. AIP, Melville, NY.

Shankar, R. (1994). Principles of quantum mechanics. Plenum Press, New York.

Shapiro, F. L. ( 1968). Electric dipole moments of elementary particles. Sov.

Phys. Usp., 11 (3), 345-352.

Shen, Y. R. ( 1989). Surface properties probed by second-harmonic and sum- frequency generation. Nature, 337(6207), 519-25.

Siegman, A. E. (1986). Lasers. University Science Books, Mill Valley.

Silver, J. (2001 ). Tests of quantum electrodynamics in hydrogenic ions. In Atomic Physics 17 (ed. E. Arimondo, P. De Natale, and M. Inguscio). Amer- ican Institute of Physics Conference Proceedings, Vol. 551, pp. 282-9. AIP, Melville, NY.

Slichter, C. P. ( 1990). Principles of magnetic resonance. Springer-Verlag, Berlin.

Smith, D. R. (2005). See Prof. Smith's web page at Duke University: http://www.ee.duke.edu/ drsmith/.

Smith, J. H., Purcell, E. M., and Ramsey, N. F. ( 1957). Experimental limit to the electric dipole moment of the neutron. Physical Review, 108 (I), 120-2.

Sobelman. I. I. ( 1992). Atomic spectra and radiative transitions. Springer- Verlag, Berl in.

Sodic_kson: D. ~-• and Waugh, J. S. 0995 ). Spin diffusion on a lattice: Classical s1mulat1ons and spin coherent states. Phys. Rev. B, 52(9), 6467-79.

Soffe~, B. H. and McFarland. B. B. ( 1972). Continuously tunable narrow-band orgamc dye laser. Applied Physics Letters 10 (10), 266.

Sorokin, _P. P. and Lankard. J. R. (1966). Stimulated emission observed from an orgamc dye chloro-aluminum phthalocyanine. IBM Journal of Researr:h and Development, 10 (2), 162-3.

Stcnholm, S. ( 1984). Foundations of laser spectroscopy. Wiley, New York.

Storey, P. and Cohen-Tannoudji, C. (1994). The Feynman_ path integral approach to atomic interferometry. A tutorial. Journal de Physique II, 4 ( 11 ), 1999-2027.

~ushk~v, 0. _P., _Flambaum, v. v., and Khriplovich, I. B. _(1984). Possibil- ity of mvest1gatmg P- and T-odd nuclear forces in atomic and molecular experiments. Zhurnal Eksperimentalnoi i Teoreticheskoi Fizi/d, 87 (5), 1521· Ter-Mikaelyan, M. I. ( 1997). Simple atomic systems in resonant laser fields.

Uspekhi Fizicheskii Nauk, 167 (12), 1249.

Townes, C. H. and Schawlow, A. L. (1975). Microwave spectroscopy. Dover, New York.

Trigg, G. L. ( 1975). Landmark experiments in twentieth century physics.

Crane Russak, New York.

Udem, T., Holzwarth, R., and Hansch, T. w. (2002). Optical frequency metrology. Nature, 416 (6877), 233-7.

Van Dyck, Jr., R. S., Ekstrom, P., and Dehmelt, H. G. ( 1976). Axial, mag- netron, cyclotron, and spin-cyclotron beat frequencies measured on single electron almost at rest in free space (geonium). Nature, 262, 776.

Van Dyck, Jr., R. S., Schwinberg, P. B., and Dehmelt, H. G. ( 1978). Electron magnetic moment from geonium spectra. In New Frontiers in High Energy Physics (eds. B. Kursunoglu, A. Perlmutter, and L. F. Scott. Plenum, New York.

Van Dyck, Jr., R. S., Schwinberg, P., and Dehmelt, H. ( I 987). New high- precision comparison of electron and positron g factors. Physical Review Letters, 59 (I), 26-9.

## BIBLIOGRAPHY

Vandenbosch, R., Will, D. I., Cooper, C., Henry, B., and Liang, J. F. ( 1997).

Alkali carbide fragmentation, a new path to doubly-charged negative ions.

Chemical Physics Letters, 274 ( 1-3), 112-4.

Varshalovich, D. A .• Moskalev, A. N., and Khersonskii, V. K. (1988). Quan- tum theory of angular momentum: irreducible tensors, spherical harmonics, vectors coupling coefficients, 3nj symbols. World Scientific, Singapore.

Vasil'iev, B. V. and Kolycheva, E. V. (1978). Measurement of the electric dipole moment of the electron with a quantum interferometer. Soviet Physics - JEI'P, 47 (2), 243-6.

Vedenin, V. D., Kulyasov, V. N., Kurbatov, A. L., Rodin, N. V., Shubin, M.

V. (1986). The 12.76- mum forbidden line in neutral samarium absorption spectrum. Optika i Spektroskopiya, 60 (2), 239-43.

Vrijen, R. B., Lankhuijzen, G. M., Maas, D. J., and Noordam, L. D. (1996).

Adiabatic population transfer in multiphoton processess. Comments At. Mo/.

Phys., 33 (2), 67-81.

Vuletic, V. and Chu, S. (2000). Laser cooling of atoms, ions, or molecules by coherent scattering. Physical Review Letters, 84 (17), 3787-90.

Walls, D. F. and Milburn, G. J. (1995). Quantum optics. Springer, Berlin.

Weinberg, S. ( 1967). A model of leptons. Physical Review Letters, 19 (21 ), 1264-6.

Weiping, Z., Sackett, C. A., and Hulet, R. G. ( 1999). Optical detection of a Bardeen-Cooper-Schrieffer phase transition in a trapped atomic gas of fermionic atoms. Physical Review A, 60 (I), 504-7.

Weisstein, E. W. (2005) MathWorld - A Wolfram Web Resource.

http://mathworld.wolfram.com/IsotropicTensor.html Wertheim, G. K. (1964). Mossbauer effect: principles and applications.

Academic Press, New York.

Wolfenden, T. D. and Baird, P. E. G. (1993). An experimental search for enhanced parity nonconserving optical-rotation in samarium. Journal of Physics B, 26 (7), 1379-87.

Wood, C. S., Bennett, S. C., Cho, D., Masterson, B. P., Roberts, J. L., Tanner, C. E., and Wieman, C. E. ( 1997). Measurement of parity nonconservation and an anapole moment in cesium. Science, 275 (5307), 1759-63.

Yariv, A. ( 1989). Quantum electronics. Wiley, New York.

Yariv, A. and Yeh, P. (1984). Optical waves in crystals: propagation and control of laser radiation. Wiley, New York.

Yashchuk, V. V., Budker, D., Gawlik, W., Kimball, o. F., Malakyan, Y~.

P., and Rochester, S. M. (2003). Selective addressing of high-rank atomic polarization moments. Physical Review Letters, 90 (25), 253()()1/1-4.

Ye, J. and Hall, J. L. (2000). Cavity ringdown heterodyne spectroscopy: high sensitivity with microwatt light power. Physical Review A, 61 (6), 061802/1-4.

Zare, R. N. (1988). Angular momentum: understanding spatial aspects in chemistry and physics. Wiley, New York.

Zel'dovich, Ya. B. (1958). Electromagnetic interaction with parity violation.

Soviet Physics JEl'P, 6 (6), 1184-6.

Zel'dovich, Ya. B. ( 1959). Parity nonconservation in the I st order in the weak-interaction constant in electron scattering and other effects. Zhurnal Eksperimentalnoi i Teoreticheskoi Fiziki, 36, 964.

Zhang, S., Fan, W., Panoiu, N. C., Malloy, K. J., Osgood, R. M., and Bruec~ S. R. J. (2005). Experimental Demonstration of Near-Infrared Negative-Index Metamaterials. Physical Review Letters, 95 (13), 137404.

Zolotorev, M. and Budker, D. ( 1997). Parity nonconservation in relativistic hydrogenic ions. Physical Review Letters, 78 (25), 4717-20.

21-cm line. 13. 15 3-j symbols, 485-487 6-j symbols, 488 absorption cross-section. 14 7. 151 absorption length, 151. 227. 248 AC Stark effect, 90. 93-95, 98-100. 121. 445 AC Zeeman effect, 95 acousto-optical frequency shifter, 369 adiabatic evolution, 188, 323 adiabatic following, 89,217 adiabatic pa~sage, 86. 218 adiabatic polarization rotation with dichroic polarizers, 217 air refractive index, 394 alignment. 195, 423. 433. 477 alkali atom, 249, 449 aluminum. 403 Amagat number, 447 anapole momen~ 52, 65. 71 angular momentum lowering operator. 45, 285, 358. 462 raising operator, 45, 285, 358, 462 selection rules, 244 anharmonic oscillator, 337 anisotropic medium, 212 annihilation operator, 132, 139, 379 antihydrogen, 62 antiparticles, 63 antirelaxation coating, 102, 274, 275, 277, 281 arrow of time, 255 atom trap. 90. 311, 331 atomic beam, 38. 176. 261. 298, 306, 310 atomic clock, 13,259,278,295 atomic uniL~. 4-J3 axial vector (pseudovector), 53, 205, 246, 256 BAC-minus-CAB vector identity. 213 bandhead,347 bandheads vibronic, ~ Barnett effect. 119 beamsplitter, 382 dark pon, 383 polarizing (PBS). 384 beat frequency, -W3 Bessel functions, 91. 93, 372, 375 beta decay, 417 bichromatic light field, 216

## INDEX

biomagnetic imaging, 288 biomagnetism, 403 birefringent filter. 393 bismuth. 52 black-body radiation, 441 Bloch equations. 251 Bloch-Siegert shift, IO I Bohr formula, I. 79 Bohr magneton, xix. I 08. 224. 444 Bohr radius. xix. 19. 443 Boltzmann's constant, xix, 150, 446 Born-Oppenheimer approximation. 363 Bose-Einstein condensate (BEC). 183. 291. 295. 311.

322.440 energy. 319 entropy. 321 Bose-Einstein condensation temperature. 31 I. 312.

bosons.4,311,322,343 bottleneck. 153. 174 box normalization, 129. 135 Breit-Rabi diagram, 17 bright state. 163, 166, 171, 217 buffer gas, 102,109,273.287 C-violation, 63 canonical momentum. 24, 137 carbon dioxide. 394 carbon nanotubes, 440 carrier frequency, 374 carrier-envelope phase. 402 Cartesian ba~is, 59 ca~imir effect. 128, 132, 440 cavity cooling, 324. 329 cavity ring-down spectroscopy (CRDS). 376 cavity-enhanced scattering. 324 central field approximation. I centrifugal distortion, 338 centrosymmetric media, 204 cesium. 52. 341 charge conjugation. 62 chemical potential, 313 chiral medium, 204, 211 chiral molecules, 204 chirp, 297 circular birefringence. 224, 246, 434 circular dichroism, 246, 434 circular polarization, 62, 163. 168. 175. 224. 285.

302.388,478 analyzer. 233

cla~sical radius of the electron. 200 Clebsch-Gordan coefficients. xx. 45. 58. 134. 141.

145. 159. 163. 171. 244,357,426.461.

485--487 closed transition, 162, 308 CO-NETIC alloy. 403 coherencelength,392 coherent population trapping, 170, 217 coherent state, 379, 381,382,469 coherent superposition, 216 collective emission, 181, 331 collision-induced transition, 392 collisional broadening, 392 collisional cross-section, 273 collisional relaxation, 153, 281, 469 colloidal particles, 440 compa~s, 415 completeness relation, 77 condensed matter physics, 37 condensed-matter physics, 311 conducting sphere, 41, 75. 77. 78. 371 conductivity, 403 configuration mixing, 191 contact interaction, 65 continuous transformation. 51 Cooper pair, 331 cooperative emission. 181 core electrons. 46 Coulomb gauge, 73, 128. 137, 138 CP-violation. 62, 256 CPT invariance, 62 creation operator, 132, 139. 379 critical angle, 378 cross-section absorption, 147. 151 scattering. 199 crystal biaxial, 212 uniaxial. 212 Curie temperature, 119 cyclotron motion, 22 D-line, 449 damped oscillations, 128 dark port, 383, 384 dark state, 163, 166, 169, 194, 216, 261, 308 velocity-dependent, 30 I deBroglie wavelength, 311, 398 Debye, 444 decoherence, I 07, 469 degenerate Fermi gas, 331 density matrix, 107,109,122,168,423,432,469 ensemble-averaged, 472 density of states, 32, 79, 135,441 deuterium, 62 diamagnetic atom, I 08

## INDEX

diatomic molecule. 282, 335. 336. 339, 351, 451 relative abundance. 341 Dicke narrowing. I 06. 278 Dicke superradiance. 152, 181 dielectric constant. 229 dielectric permeability tensor. 212, 245 difference-frequency generation. 204 diffraction grating. 392 dimer, 282, 341. 452 dipole field. I 17 dipole-dipole interaction, 116, 291, 355, 421 dipole-dipole relaxation, 116 Dirac delta function, 136 discrete transformation. 51 dispersion. 210 dissociation energy. 335 Doppler broadening. 38, 149, 156, 277 Doppler limit for temperature, 300 Doppler shift. 149,277,310,368.397 Doppler width. 150, 275, 447 dyadic, 467 dye la~r. 392 continuou.~ wave, 393 pulsed, 392 dysprosium. 173 eigenmode, 212 Einstein A and B coefficients, 147, 153 Einstein-de Haas effect, 119 EIT. 176,211.215 ela"ticity, 439 electric dipole approximation, 134. 140, 144 operator. 79. 91,141,351 radiation. 199 selection rules. 76, 79, 254 transition, 134, 159, 162, 183. 186. 20 I, 236, 238 electric dipole moment, 444 collective. 182 induced.229,269,326,372 permanent (EDM), I 07. 112. 253. 264-266, 404 polar molecule. 351 electric displacement. 212 electric field single photon, 379 electric quadrupole transition. 149 electro-optical rotation. 205 electrodynamics high-field. 201 electromagnetic field energy. 130 Hamiltonian, 132, 139 mode, 128,132,139,146 noise, 128 polarization, 130 quantized, 128. 134

## INDEX

electromagnetically induced transparency (EIT). 176.

211. 215 electron charge. xix. 137. ~3 Lande g-factor. 14. 21 magnetic moment. ~ mass, xix. 443 electron-on-a-spring model, 20 I. 208 electron-randomiz.ation collisions, 287 elliptically polariz.ed light. 227, 388 ellipticity, 26 7 enhancement factor atomic EDM. 258 atomic PNC. 55 ensemble average. 472 entropy, 255. 313. 319, 323 equilibrium state. 286 etalon, 393 Euler angles, I 14. 436. 459 evaporative cooling, 319 exchange interaction. 8. 41, 281 extinction ratio, 389 Fabry-Perot interferometer, 393 Faraday rotation. 223. 269 feedback loop, 412 femtosecond la~r. 398 Fermi contact interaction, 191 Fermi degeneracy, 331 Fermi energy, 332 Fermi momentum, 31, 35 Fermi pressure, 33, 35 Fermi statistics. 8 Fermi temperature. 333 Fermi's constant G F. 52 Fermi's Golden Rule. 134, 137, 144. 481 fermions. 4, 331 ferromagnetic materials, 416 Feynman diagram, 186, 188, 232, 421, 481 trunk, 482 vertex.482 Feynman path integral, 398 fiber-optic cable, 377. 397,401 fictitious field. 96. 97. I 03 field ionization. 110 fine structure, IO. I 8, 21 fine structure constant a. xix. 443 finesse. 393 fluctuation-dissipation theorem, 41 O fluorescence, ISO, 153. 172,392,421 forward scattering, 232 forward voltage drop. 408 four-wave mixing. 232. 382 Fourier transfonn, 178,276,377,402,419 free radical, 341 freespectralrange,393,394 frequency comb. 398 frequency doubler. 3 7 4 frequency-modulated light. 91. 372 funding lack thereof. 448 FWHM (full width at half maximum). 187 gauge transformation. 72 Gau.~s· theorem. 67 Gaussian distribution, I SO, 275 Gaussian 1ight beam, 325 Gaussian spatial profile (for laser beam). 176 general relativity, 132 geometric (Berry's) phase, 112. 261 geometric series, 314 geonium. 21 axial motion. 22. 25 cyclotron motion, 22, 23, 25. 26 energy levels, 27. 28 magnetron motion, 23, 26 geostationary orbit, ~ gerade, 343, 452 gradient spherical coordinates, 59 grand partition function, 316 group velocity dispersion ( G VD), 400 gyromagnetic ratio, 85, I 02, I 08, 250. 415 gyroscope, 369 la~r. 395 matter-wave, 395 half-wave plate, 386, 456 handedness, 51 Hanle effect, 233 harmonic generation, 20 I harmonic oscillator, 9, 128, 304, 338, 341, 428 Heisenberg equation of motion. 140 Heisenberg uncertainty relation, 36. 53, 139, 379 helium, 228,290 liquid, 228 hexadecapole moment. 4 77 high-field electrodynamics, 20 I homogeneou.~ broadening, 147, 157, 298 homogeneou.~ width, 150, 227 homonuclear molecule, 452 Hund's ca~ (c), 360,363 Hund's coupling cases. 360 Hund's rules, 2 hydrogen, I, 10, 13--15, l7-19,53,58-60.62,63, 75.

76,81, II0,236,237,254,449.483 hydrogenic ions, I 8, I I 0 hyperfine interaction, 13. 21. 42, 191, 288. 356 hyperfine structure, 13, 18, 21. 44, ~. 192, 193. 421 ICI, 347 ideal ga~. 311

## INDEX

incoherent ensemble. 469 induction electric. 229. 245 ~nhomogeneous broadening, 150. 157 mstantaneous ba~is, 114, 115 interaction picture, 98, 122 ~nteratomic potential, 282, 336. 339 mtercombination line, 292 interference, 124 interferometer, 395 ~ntemuclear separation, 335. 338 ~oniz.ation potential, 443 ~rreducible tensor, 239-241. 467 ~rreducible tensor operators. 461 ~rreducible tensor product. 240 •sobutane, 394 isotope shift, 37, 46 ma.~ shift, 37 normal,38,39 specific (anomalous), 38. 41 molecules, 346 volume (field) shift. 37 isotropic media, 204 J-coupling, 355 j-j coupling scheme. 2 Johnson noise. 404, 410, 411 Jones calculus, 386,456 Jones matrix, 387 Jones vector, 387, 456 Kapitsa pendulum, 428 Kerr cell, 386 Kerr constant, 227 Kerr effect, 227, 399 Kerr lens mode-locking, 399 King plot, 37 Kronecker delta, 115, 476 Lagrange multiplier, 287 Lamb shift, 53, 60, 236 Lande factor, 81, 224, 235, 290 Lande interval rule, 12 Landau levels, 23 Laplace equation, 72, 425 Larmorfrequency,81,85, 102,107,195,204, 233 249,288,415,475 ' Larmor ~~ion, 96, 105, 109, 118 195 204 250 ' ' ' ' laser continuous wave, 399 dye,392 femtosecond, 398 TI:sapphire, 399 la~r cooling, 90, I 00, 295, 311, 319, 331 laser heating, 369 laser spectroscopy. 38. 51. 347, 392 laser-induced fluorescence. 38 lattice, I 16 law of ma~s action. J..J2. 344 left-handed materials. 207 Legendre function as.~ociated, 352 Legendre polynomial. 111,422,42 4 recursion formula. 353 Levi-Civita tensor. 69. 205. 245, 464 light guide. 377 light scattering. 372 linear birefringence. 434 linear dichroism. 43-J linear polarization. 169. 388. 423 linear polarizer. 456 linear re."toring force. 299, 302 Liouville equation. 436, 474 Littrow configuration. 392 lock-in amplifier. 249, 389 longitudinal mode, 393 longitudinal relaxation. I 02, 250 Lorentz invariance. 62 Lorentzian lineshape. 144, 156,224,275, 278, 377, lowering operator angular momentum, 45, 285, 358, 428, 462 simple harmonic oscillator, 9, 132 LRC oscillator. 377 Lyman o line, 236 Lyot filter, 393 Macaluso-Corbino effect, 223 macrostate, 255 magic angle, 111, 420, 422 magnetic deflection, 244 magnetic dipole moment, 68, 86. 233 magnetic dipole transition, 149, 191, 202 magnetic field, 446 gradient, I 02 motional, I 07, 261 magnetic induction, 446 magnetic moment, 415, 444, 445 magnetic permeability, 370 magnetic quadrupole moment, 69, 71 magnetic resonance, 84, 85, 121, 260, 355, 421 magnetized sphere, 84 magneto-optical eff ecl", 223, 244 magneto-optical trap (MOT), 302,306 magnetometer, 288, 403 M z scheme, 249 dark zone, 250 optical pumping, 84, 249 magnetron motion, 23 Malu.~'s law, 384 ma.~r. 13

mass action law of, 342, 344 ma.~s-spectrometer quadrupole. 428 material equations, 214 Mathieu equation, 430 Max well' s equations, 129. 207. 212, 214, 24 7 Maxwellian velocity distribution, 149 mean free path, I 06, 273, 280 mercury, 196 metamaterials, 208 meta"table state, 153, 290 microstate, 255, 313 microwave transition, 277 minimum uncenainty state, 380 mixed state, 470 mode hops, 394 mode of the electromagnetic field, 128. 132 mode volume, 325, 392 mode-locking, 400 modulation index. 91. 279, 372 pha~e, 375 modulation polarimetry, 389 molecular axis. 451 moment of inenia, 339,349,351,416 momentum kick, 297, 308 monopole moment, 4 77 Morse potential, 336 Mossbauer effect, 183 motional averaging, I 05 motional field, I 08 muon EDM, 257 negative ion, 41 neutral weak current. 52 neutron, 37, 52, I 07. 253. 356. 417. 418 magnetic moment. 445 mass, xix nonlinear optics, 151, 232, 295, 382 normal distribution, 276 nuclear magnetic resonance (NMR), 355, 421 nuclear magneton, xix nuclear quadrupole moment. 21 nuclear screening, 48 number operator, I~. 380 numerology, 425 Nyquist theorem, ~ octave, 398 octupole moment. 4 77 fl-type doubling. 363 one-electron atom Hamiltonian. 137 op-amp, 412 golden rules, 412 open system. 478

## INDEX

operational amplifier (op-amp), 412 golden rules. 412 optical cavity, 32..t. 376, 391 optical depth, 151 optical lattice, 322 optical molasses. 296. 302 optical pumping. 118, 151, 162. 168, 196, 259. 281.

285,295,..t26,478 optical pumping magnetometers (OPMs). 84, 85 optical rotation. 51. 205, 223. 267. 270 adiabatic. 217 optically active, 204 orientation. 195, 423. 434. 477. 479 overdamped regime. 128,305 paramagnetic atom, I 08, 257, 415 parametric amplification, 382 parity nonconservation, 46. 51. 53, 61, 66, 81, I 07.

191.238.255,256 parity selection rule, 191 partial width. 149 partial widths. 143 partially coherent ensemble. 469 partition function, 342 Paul trap. 428 Pauli exclusion principle, 4. 6 Pauli matrices, 57, 96,473 Penning ioniz.ation, 290 Penning trap, 21, 22, 62, 256 periodic perturbation. 91. 121, 122 periodic perturbations, 85 permittivity tensor. 246 perturbation theory, 134, 183, 244, 354. 481 pha"e diffusion. I 04 pha~-sensitive detector, 249 pha"or diagram, 381 photoconductive. 409 photodiode, 406, 408. 409. 411, 413 photoela"tic modulator. 386 photon energy, 146, 305 flux. 147, 445 photonic crystal fibers, 378 photonic crystal optical fibers. 40 I photovoltaic, 407 physics of the vacuum, 132 1r polariz.ation. 159, 165 1r-pulse, 86. 181 pile-up. 390 Planck's constant, 4--1-6 Pockels cell, 386 Poisson equation, 33 Poissonian distribution, 27 4. 381, 385 polar molecules. 254 polar vector, 53, 205, 256 polarizability

electric, 75, 78,229,270, 326 conducting sphere, 77 hydrogen ground state, 77 scalar, 111 tert~r. 111. 436 transition, 243 Rlagnetic ~onducting sphere, 371 P<>lanzation ato · 1 nu4c3, 02, 118. 196,259,262,263 267 268 I, 472,477 ' • • l"gh I \6;,.

128, 130, 159, 162, 163, 165, 169, 170, 228:~~·i:·if 3, 2212,214,223,22 5, 226, Pol .

.

' , , 45, 455 ~zat~on moment~, 168, 195, 431 Polanzat1on rotation adiabatic w·th d" L.- • • • icu.,oic polarizers 217 polanzat1on vector. 426 , population,472,477 power br~ening, 155, 187 • 190 power build-up cavity, 391 power spectrum, 420 powe~-broadened linewidth, 156 Poy.~tmg vector. 146, 200, 245, 247. 445 p~~~e broadening, 209,227,274 447 pn~c•p~ quantum number, I, 78 • ProJection rule, 485 propagator, 482 proton Lande g-factor, 14 magnetic moment, 17, 444 mass. xix pseudoscalar, 206 pseudospin, 182 pure state, 469 quadrupole moment, 433, 477 quantum beat~, 195, 196, 421, 423, 431 hyperfine, 195 quantum computer, I 07, 355 quantum concentration, 318 quantum efficiency, 384, 407 quantum field theory. 64 quantum fluctuations, 379 quantum logic gates, 355 quaner-wave plate, 386,456 quasicla~sical approximation (see semiclassical (WKB) approximation) 48 qua~ipanicles, 37, 39 ' qubits, 107 Rabi frequency, 124 Rabi oscillations, 128, 184 Rabi technique, 259 radiation trapping. 152, 18 I , 296 radiative corrections, 61

## INDEX

raising operator angular momentum. 45. 285, 358, 428, 462, 488 simple harmonic oscillator, 9, 132 Raman resonance condition, 215 Raman scattering. 180, 185 velocity-selective, 30 I Ramsey's method of separated oscillatory fields, 259 random walk. IOI. 274, 280, 288. 301 rank tensor, 467 rare eanh ato~. 55, 281 rate equation. 164 Rayleigh range. 325 red-detuned. 296 reduced ma~ 337. 339, 348 reduced matrix element. 141, 145, 148, 229, 461 refractive index. 224, 229, 246. 248. 267, 268, 325, 377.394.399 refractive index of the air, 394 relative density (r.d.). 447 relaxation, 122, 127 relaxation matrix. 476 resistivity, 370. 403 rigid rotor. 35 I root mean square (r.m.s.), 108, 329,335,403 rotating frame. 87. 94-96, I 04, 251, 261 rotating wave approximation, 94, 96, 97. 250,262 rotation matrix, 111, 114, 234. 431, 459 rotational constant. 339, 349, 35 I rotational level, 339. 342, 347. 350 rovibrational structure, 348. 392 Russell-Saunders (L-S) coupling scheme. 2, 10 Rydberg constan~ xix, 335, 348, 443 Sagnac effect, 369, 395 samarium, 38 saturated vapor pressure, 341 saturation parameter. 151, 163, 175,259,299,305.

306,445 scalar coupling, 355 scalar operator, 43, 57, 191, 357. 463 scalar polarizability. 111 scalar potential, 129 scattering cross-section, 199 Schawlow-Townes limit, 274. 392 Schiff's theorem. 257 Schrodinger equation, 98, 121, 235, 425. 474 second law of thermodynamics, 255 second-harmonic generation, 205, 382 secular equation, 16, 229. 238, 254 selection rule 0 ._... 0,427 self-modulation, 40 I self-rotation (of elliptical polarization), 382 semiclassical (WKB) approximation, 31, 35, 48 shot noise, 384, 398, 410-412

## INDEX

shot-noise limit. 381. 385 sidebands, 91, 279, 372, 374. 40 I a polarization. 159, 163. 302 signal-to-noise ratio. 26"'. 265 silver. 370 simple harmonic oscillator. 9. 22. 26. 128. 304, 338.

341. 428 Hamiltonian. 130 lowering operator. 9, 132 raising operator. 9. 132 single-photon recoil temperature limit, 296, 30 I, 319 Sisyphus cooling, 30 I skin depth. 370, 371. 405 Slater determinant. 4 Snell's law, 377 sodium, 297 solenoid, 306, "-'6 space elevator, 4-40 spatial dispersion. 21 O spatial inversion. 51, 204, 205 specific heat. 319, 370 spectral distribution, 178 spectral lines, 37, 38, 104,274,277. ~7. 392 spectrometer, 376 spectroscopic notation. 3, 341. 451 spectrum analyzer. '367 speed of light, xix. ~.

spherical ba~is, 59, 141, 145, 171. 358, 465 spherical harmonic, 352. 423 spin multiplicity, 451 spin temperature. 285, 288 spin-destruction effect~. 284, 292 spin-exchange,281,285,288,292 cross-section. 28-J operator. 283 spin-flip transition, 292 spin-helix, 6-' spin-orbit interaction. I 0, 463 spin-projection noise. 265 spin-statistics theorem, 4 spinor representation, 96. 261, 459 spontaneous decay rate, 142, 163. 235, 483 spontaneous emission. 128, 134, 136, 141. 142. 153, 157, 163, 166, 173. 179. 181, 183. 187-189, 274,295.297.300.308,469,476,483 spring constant, 335. 339, 349 squeezed states. 382, 38-J, 385 squeezing number, 381 pha~, 381 standard conditions, 44 7 standard deviation. 379, 382, 385 Standard Model of electroweak interactions, 51, 256 standard quantum limit. 379 standard quantum limit (SQL), 385 Stark beat~. 431 Stark effect, 79. 80, 90, 91, 93, 95, 99, I 00, 113. 114.

121,2.U.254.255.260,322.327.436-438.

AC.90,95, 100, 121.322.327.445 DC. 78.91 linear. 254 quadratic, 79, 260, 436 Stark-induced transition, 239 Stark-interference technique. 52. 81, 239 state multi pole. 431. 4 77 statistical mixture, 473 statistical weight, 290 Stem-Gerlach effect continuous. 30 stimulated absorption. 144. 153, 308 stimulated emission. 134. 153, 181, 298, 308 Stimulated Raman Adiabatic Pa.~sage (STIRAP). 218 Stirling formula. 286, 323 stochastic cooling. 331 Stokes parameter, 162, 244. 455 storage rings, 110 stress. 438 stretched state, 7, 288, 309. 431. -B2, 435 sub-Doppler cooling, 30 I sum-frequency generation. 204 summation formulae, 11 superconductivity, 311 superfluidity, 311, 331, 417 superposition of quantum states, 4, 53, 98, 104, 123.

169,175.182. 183,201,203,283,374,470 supersonic jet, 310 supersymmetry, 256 susceptibility linear. 225, 268, 481 nonlinear, 481 second-order, 204 symmetrization postulate. 4 T-violation. 53, 56, 66, 69, 107, 207. 247, 255. 352 Taylor expansion, 67, 174, 317 TEMoo mode, 325 temperature diffusion, 370 tensile strength, 439,440 tensor. 239-241 tensor contraction, 70 tensor polarizability. I 11. 436 tensor product, 240 thallium. 52, 254 thermal conductivity, 370 thermal noise, 411 Thoma~-Fermi model, 30. 33, 34. 47 Thomson scattering, 199 three-wave mixing, 205 time-reversal invariance, 53. 56, 66. 69. 71. I 07. 153.

207,247,255,352 total internal reflection, 378

tran.~it-time broadening, 176 tran.~ition polarizability, 243 transversality, 206 transverse relaxation. I 02, 250 trap dipole. 322 magneto-optical. 302 Paul. 428 Penning, 21, 22, 62, 256 trap state, 168 triangle inequality, 11, 485, 489 two-photon tran.~ition. 183, 236 ultracold neutron.~ (UCN), 417 ultrafa~t la~r system, 398 underdamped regime, 305 ungerade.452 unitary transfonnation, 93 vacuum state, 379 valence electron, 46 van der Waals potential, 283 variable retarder, 386 variance,379 vector identity, 247 vector moment, 477 vector operator, 44, 171, 364, 464-466 vector particle, 426 vector potential A. 24, 65, 66, 128, 133, 137 vector-addition coefficienL~, xx vector-coupling coefficients, xx velocity most probable, 309, 312 velocity group, 157 velocity-changing collisions, I 08. 277 vibrational constant, 339

## INDEX

vibrational level. 336. 337. 339. 342, 347, 350 virial theorem. 20. 79 vinual state. 185 viscous drag. 297 Voigt profile. 157 wave equation. 129 in dielectric medium. 267 wave vector. 128, 225. 2..J5, 297. 368, 397 wavefunction composite, 426 hydrogen, 14,58. 77,237,357 molecular, 343. 351. 452 wavenumbers, 337 weak charge, 60, 62 weak nuclear charge. 52 Weinberg mixing angle, 52 white noise, 405, 410 Wigner 3-j symbols. 485---487 Wigner 6-j symbols, 488 Wigner coefficients. xx Wigner-Eckan theorem. 11, 56, 58, 69, 82, 134, 141, 146,159,170,229,256,353,364,423,426, 461,487 WKB approximation, 48, 49 Young's modulu.~. 439, 440 Zo boson, 51 Zeeman beats, 195 Zeeman effect, 15, 17, 90, 203 AC, 90, 95, I 09, 121 DC,248,303 nonlinear, 250 Zeeman slower, 306 zero-point energy, 132,332,336,382

This book provides a bridge between the basic principles of physics learned as an undergraduate and the skills and knowledge required for advanced study and research in the exciting field of atomic physics. The text is organized in a unique and versatile format - as a collection of problems, hints, detailed solutions, and in-depth tutorials.

This enables the reader to open the book at any page and get a solid introduction to subjects on the cutting edge of atomic physics, such as frequency comb metrology, tests of fundamental symmetries with atoms, atomic magnetometers, atom trapping and cooling, and Bose-Einstein condensates. The text also includes problems and tutorials on important basics that every practicing atomic physicist should know, but approached from the perspective of experimentalists: formal calculations are avoided where possible in favor of'back-of-the-envelope' estimates, symmetry arguments, and physical ana- logies. The 2nd edition contains more than 10 new problems, and includes important updates, revisions, and corrections of several problems of the 1st edition.

Dmitry Budker is Professor of Physics at the University of California at Berkeley.

Derek F. Kimball is post-doctoral researcher in the Department of Physics, California State University-East Bay.

David P. DeMille is Professor of Physics at Yale Universit y, New Haven.

Coi·cr inw~c: The n m:r illustration is a schematic diagram of an atomic beam l'Xpcrimcnl , consisting of an own , chopper whcd for the atomic beam, collimator, laser inlL'raction region with pom.:r-huild -up cavity and cb .:tric lidd plates, and cross-section of a radio-fr'-''-Jllcncv interaction rcoion with ma,1nctic shiddin o and light pipes.

~ ~ t, ~ '- Similar experimental setups haw hl'l'n used in th'-· author s' research laboratories.

## ALSO PUBLISHED

## BY OXFORD UNIVERSITY

## PRESS

The Light Fantastic-A Modern Introduction to Classical and Quantum Optics I. R. Kenyon Quantum Optics - An Introduction A. M. Fox Modern Classical Optics G. A. Brooker Quantum Optics J. C. Garrison, R. Y. Chiao Atomic P_hysics C. J. Foot Optical Properties of Solids AM.Fox

## ISBN 978-0-19-953241-4

11111 111111 9 780199 532414
